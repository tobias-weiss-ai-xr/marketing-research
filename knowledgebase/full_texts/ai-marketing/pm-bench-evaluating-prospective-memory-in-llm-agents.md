---
title: 'PM-Bench: Evaluating Prospective Memory in LLM Agents'
url: https://arxiv.org/abs/2607.12385
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: COLM 2026
authors:
- Genglin Liu
- Saadia Gabriel
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.12385
pages: 22
chars: 70439
fetched_at: '2026-11-08T13:36:06+00:00'
kb_version: 1
---

# PM-Bench: Evaluating Prospective Memory in LLM Agents

Published as a conference paper at COLM 2026
PM-Bench: Evaluating Prospective Memory in LLM Agents
Genglin Liu
University of California, Los Angeles
genglinliu@cs.ucla.edu
Saadia Gabriel
University of California, Los Angeles
Abstract
A significant challenge in agentic AI is prospective memory: the ability to
execute an intention at a specific future cue or state while other activities
are ongoing. We introduce PM-Bench, a text-based benchmark for measur-
ing prospective memory capabilities in modern LLM agents. Inspired by
the Virtual Week paradigm from cognitive science, PM-Bench evaluates
how well LLM agents maintain user intentions, execute delayed intentions,
and monitor latent environment changes. Over the course of a simulated
seven-day week, agents must continue an ongoing activity while decid-
ing whether any deferred task is due. We compare eight state-of-the-art
LLMs on PM-Bench under eight different agent configurations. PM-Bench
proves challenging across all settings: the best method, a GPT-5.4 agent,
reaches only 65.1% F1 score under our evaluation. Furthermore, no single
strategy for improving prospective memory dominates across models. We
release PM-Bench as a controlled testbed for diagnosing these failures and
developing training or inference-time interventions that support reliable
prospective behavior 1.
1 Introduction
LLM-driven agentic systems are increasingly expected to sustain long-horizon tasks, as
models can now browse, code, plan, use tools, and act over many turns rather than a
single prompt (Cao et al., 2026; Team et al., 2025; Wang et al., 2024; Jimenez et al., 2023;
Zhang et al., 2026b). As LLM assistants grow more capable, failures often occur not because
the system lacks relevant knowledge, but because it does not act on that knowledge at
the right moment (Gonzalez-Pumariega et al., 2025; Liu et al., 2025a). As illustrated in
Figure 1, a reliable assistant, in principle, should remember to carry out tasks that were
mentioned at a previous time. It should track rescheduling or cancellations, and stop acting
on plans that have already been completed or fulfilled. In cognitive science, this capability
is categorized as prospective memory: remembering to perform delayed intentions at an
appropriate time or event in the future (McDaniel & Einstein, 2007; Brandimonte et al.,
2014). Prospective memory is distinct from retrospective recall because success depends not
only on what is remembered, but also on whether tasks can be completed under distraction,
interference, and monitoring demands (Smith & Bayen, 2005; Dismukes, 2006; Anderson
et al., 2018). Its importance is not merely theoretical: in aviation, failures to remember
deferred cockpit actions have been linked to a substantial share of major airline accidents,
and in healthcare, self-reported forgetting of blood pressure medication has been associated
with worse cardiovascular outcomes (Dismukes, 2006; Nelson et al., 2006). Classic work on
human forgetting argues that prospective memory failures may account for roughly 50% of
these lapses in our daily life (Crovitz & Daniel, 1984).
This distinction matters for agentic benchmarking. Existing long-horizon evaluations for
LLMs increasingly stress software engineering, browsing, planning, proactive interaction,
and memory over extended sessions (Deng et al., 2023; Castillo-Bolado et al., 2024; Liu et al.,
2025c; Jimenez et al., 2023; Wei et al., 2025; Zhang et al., 2026b; Bian et al., 2026). Agent
memory methods and benchmarks have focused on retaining past user information, context
1Benchmark repo athttps://github.com/genglinliu/PMBench.git
1
arXiv:2607.12385v1  [cs.AI]  14 Jul 2026

Published as a conference paper at COLM 2026
Figure 1: Overview of PM-Bench. The benchmark adapts theVirtual Weekparadigm into a
seven-day text-based schedule in which an LLM agent must carry out deferred intentions at
the correct future time or event while continuing an ongoing activity. We propose a series of
competitive baselines that attempt to solve PM-Bench and expose critical challenges faced
by different agentic setups.
engineering that’s essentially implemented by retrieving from prior episodes or experiences,
or extending memory capacity through external stores and architectural changes (Li et al.,
2025; Lee et al., 2025; Packer et al., 2023; Zhong et al., 2024; Wang et al., 2026; Cheng et al.,
2026; Zhang et al., 2025). However, none of these existing efforts cleanly isolate whether an
intention is executed at the correct future cue or time. Recent concurrent work also suggests
that current LLMs continue to struggle with this problem (Mittal, 2026).
In light of this observation, we introduce PM-Bench, a text-based benchmark for prospective
memory in LLM agents. PM-Bench adapts the classicVirtual Weekparadigm from cognitive
science to a format that is executable for modern tool-using LLM agents (Rendell & Craik,
2000; Rendell & Henry, 2009; Mioni et al., 2015). In PM-Bench, scenarios unfold over a seven-
day schedule. At every step, the agent must continue an ongoing activity while deciding
whether any deferred intention should be executed at that given moment. A core design
goal of PM-Bench is to separatewhatthe agent remembers fromwhenit acts. The benchmark
consists of event-based and time-based tasks, cross-day obligations, rescheduling and
cancellations, as well as invisible state channels that require active monitoring. The design
principles of PM-Bench are inspired by relevant psychology studies on human subjects
(Einstein & McDaniel, 1990; Kourtesis & MacPherson, 2023).
PM-Bench comes with a comprehensive scoring pipeline to track fine-grained execution
errors, including misses, late completions, update or dependency violations, as well as
monitoring overhead. We propose a number of baselines for PM-Bench, with both single-
agent and multi-agent strategies. Across these settings, the main pattern is not simply
that models “forget”; it is that prospective behavior is hard to calibrate. Methods that
recover more due tasks often do so by becoming over-aggressive and increasing false alarms,
whereas conservative methods preserve precision by under-acting. PM-Bench is designed
to make this gap visible and analyzable, providing a controlled testbed for future training,
inference-time scaffolding, and agent-memory interventions.
In summary, this paper makes the following contributions:
• We introduce PM-Bench, a benchmark that evaluates LLM agents’ prospective
memory under ongoing activity. To this end, we provide a synthetic scenario frame-
work with scalable solvability validation, supporting cross-day tasks, environment
monitoring, and dynamic task updates (§3.1–3.3).
• We define an evaluation protocol that combines task performance, fine-grained
execution error analysis, and monitoring-cost accounting (§4.1).
2

Published as a conference paper at COLM 2026
• We present empirical comparisons across single-agent and multi-agent strategies
on recent frontier LLM backbones, showing that proactive monitoring remains a
challenging bottleneck in prospective behavior (§4.2–4.4).
2 Related Work
2.1 Agent Benchmarks and Proactive Behavior
Recent benchmarks have pushed LLM evaluation beyond one-shot prompting into in-
teractive environments for software engineering, browsing, asynchronous planning, and
continual improvement (Jimenez et al., 2023; Wei et al., 2025; Gonzalez-Pumariega et al.,
2025; Zhang et al., 2026b; Cai et al., 2025). Related dialogue work studies proactive assistance
and adaptation under changing conversational context (Deng et al., 2023; Liu et al., 2025c;
Castillo-Bolado et al., 2024; Tang et al., 2026). PM-Bench is complementary to both directions
but directly measures whether an agent can carry a future intention through ongoing activity
and execute it only when its cue or time condition is satisfied.
2.2 Long-term Memory for LLM Agents
Long-term memory in LLMs has been studied through multi-session dialogue, personalized
conversation, and interactive memory evaluation (Xu, 2021; Jang et al., 2023; Ahn et al., 2023;
Kim et al., 2023; Li et al., 2025; Lee et al., 2025; Maharana et al., 2024; Wu et al., 2024; Tan
et al., 2025a; Hu et al., 2025; Bian et al., 2026; Zhao et al., 2026; Jiayang et al., 2026; Shen et al.,
2026). Complementary systems work equips agents with reflective memory management,
persistent external memory, experience retrieval, memory-oriented abstractions, and explicit
memory modules in multi-agent simulations (Tan et al., 2025b; Packer et al., 2023; Zhong
et al., 2024; Xu et al., 2025; Kang et al., 2025; Wang & Chen, 2025; Wang et al., 2026; Zhang
et al., 2026a; Yan et al., 2025; Liu et al., 2025a;b). Prior work has also focused on architectural
modifications to expand controllable memory capacity beyond standard context windows
(Cheng et al., 2026; Zhang et al., 2025). However, this line of research emphasizes the
evaluation of retrospective memory capabilities. PM-Bench evaluates prospective rather
than retrospective memory: the question is not whether relevant content can be recovered,
but whether a stored intention is executed, updated, or withheld at the right future moment.
2.3 Prospective Memory Research in Cognitive Science
Prospective memory is a core construct in cognitive psychology concerning the formation,
maintenance, and later execution of intended actions (McDaniel & Einstein, 2007; Brandi-
monte et al., 2014). Classic work distinguishes event-based and time-based prospective
memory and shows that performance depends on available attention, monitoring strategy,
and interference from ongoing tasks (Einstein & McDaniel, 1990; Smith & Bayen, 2005;
Dismukes, 2006; Anderson et al., 2018; Kourtesis & MacPherson, 2023).
The closest methodological precursor to PM-Bench isVirtual Week, a board game style
cognitive test developed by Rendell & Craik (2000) to study the effects of aging and clinical
impairment. Virtual Week embeds multiple delayed intentions within continuous everyday
activity streams (Rendell & Craik, 2000; Rendell & Henry, 2009; Foster et al., 2013; Rose
et al., 2015; Mioni et al., 2015). PM-Bench adapts this paradigm to LLM agents.
3 PM-Bench: Benchmark Construction Pipeline
3.1 Scenario Design
We construct PM-Bench to evaluate prospective memory as a dynamic decision problem
rather than a static recall task. Scenarios are organized into a seven-day week with inten-
tionally irregular daily schedules. Each day consists of 10 to 13 time-anchored steps. At
every step, an agent model must continue an ongoing activity while deciding whether
any prospective action is due. This is the central challenge and novelty of the benchmark:
3

Published as a conference paper at COLM 2026
Figure 2: Human-facing PM-Bench evaluation interface. The main panel shows the current
narrative step and the required ongoing activity choices, while the side panel provides
queryable state channels and anonymous action handles for active tasks.
intentions must be maintained and executed under distraction and dynamically changing,
unpredictable task states.
Statistic Count
Days 7
Steps per day (range) 10–13
Total steps 80
Task definitions (total) 83
Scored executable tasks 81
Event-based tasks 57
Time-based tasks 26
Regular tasks 28
Non-regular tasks 55
Channel-triggered tasks 15
Cross-day tasks 7
Update events (total) 11
Cancel / Override / Reschedule 2 / 3 / 6
State channels 11
Lures (total) 74
Table 1: Summary statistics for the released
PM-Bench week. Beyond overall scale,
the table highlights variation in task struc-
ture, including trigger type (event- vs. time-
based), regularity (regular vs. non-regular),
monitoring dependence (channel-triggered),
and temporal scope (cross-day tasks).
Formally, a PM-Bench scenario is an ordered
sequence of decision points t∈ { 1, . . ., T}
spanning a seven-day week. A task in PM-
Bench is a deferred intention specified by a
natural-language label, a trigger condition,
and an executable action. For example, a task
may be time-based (“Take asthma medication
at 21:00”) or event-based (“Book the appoint-
ment when a slot opens in the portal”). As the
scenario unfolds, each task can remain active,
be completed, be canceled, or be modified by
an update.
At each step t, the agent receives a visible
observation ot consisting of the current nar-
rative scene, three ongoing activity options,
and a set of opaque prospective action han-
dles. The narrative scene is a short vignette
describing the current moment, such as “You
make breakfast” or “You see a neighbor wav-
ing from the sidewalk.” The ongoing activity
options are the mandatory A/B/C choices
used to advance the simulation, for example
“Pour coffee,” “Toast bread,” or “Check the
fridge.” The prospective action handles are
labeled as task i; they let the agent select currently available actions as structured outputs.
Let C denote the set of available state channels, such as the clock or email, which are hidden
by default and become observable only after explicit querying. Let Xt denote the set of
currently active task specifications at step t, for example, a breakfast medication task that is
still pending, a cross-day task that has been introduced but not yet cued, or a task waiting
on a state change.
Intuitively, the due set at step t is the subset of active tasks that should be executednow,
given the current visible scene, queried channel state, and latest updates. Formally, we
4

Published as a conference paper at COLM 2026
define it as
Dt ={τ∈ X t :τremains valid and its execution condition is satisfied at stept}.
Event-based tasks should be executed when a relevant cue is present either in the current
narrative scene or in a queried state channel. Time-based tasks should be completed when
the current step time matches the target time or falls within the allowed execution window.
PM-Bench is therefore not a pure memory-retrieval benchmark: success depends on whether
the agent can maintain and revise deferred intentions so that its executed action set aligns
withD t at the appropriate future step.
Agent interaction specification.Operationally, each step follows a query-then-act protocol.
Before committing to a decision, the agent may issue zero or more monitoring queries to
channels in C, such as the clock. After observing the returned channel contents, the agent
commits to an action
at = (ct,A t),
where ct denotes the required ongoing activity choice and At denotes the subset of prospec-
tive actions selected for execution at step t. Figure 2 a visual interface used in PM-Bench
simulations for illustrative purposes, though the LLM agents access the same structured
content in a text-only format during evaluation. Appendix Section A.1 provides a worked
step example and compact task-schema examples spanning time-based, hidden-channel,
and cross-day tasks.
3.2 Data Generation Pipeline
Data Generation Pipeline.A scenario stores day-level opening agendas, step-level narra-
tive scenes, task definitions, and optional channels for state monitoring. Table 1 summarizes
the size and composition of the released week. The benchmark is generated by a seeded
synthetic pipeline and then manually reviewed by the authors: it first samples seven distinct
day archetypes (e.g. a meeting-heavy day or a chore-heavy day) with intentionally irregular
schedules, instantiates routine, event-based, irregular, and channel-triggered tasks together
with lures, and then injects cross-day tasks and cancel, reschedule, and override events.
Generation is deterministic given a seed and uses rejection sampling until the resulting
week passes schema, consistency, and solvability checks. Appendix Section A.2 gives the
full generation recipe and reproduced composition details.
Task Composition and Long-Horizon Structure.PM-Bench increases long-horizon pres-
sure in two ways. First, cross-day tasks are announced on an earlier day but become
executable only when a cue appears later, so successful execution requires maintaining a
deferred intention across multiple intervening steps and days. Second, explicit cancellation
or rescheduling can revise a task’s cue, time, or action text, forcing the model to update
an existing intention instead of relying on the initial encoding. Each day also includes ran-
domized distractor actions with natural language labels, and runtime interaction exposes
anonymous action handles mapped to both true tasks and lures, so agents must act from
current due conditions rather than memorized identifiers. Appendix Section A.1 provides
concrete task examples under this shared schema.
State Channels and Proactive Monitoring.PM-Bench extends the event narratives with
11 query-based channels that represent external information sources such as new messages
and various status trackers. Relevant cues become available only if the agent queries the
appropriate channel, allowing the benchmark to test not only whether a model acts when
cued, but also whether it decides when monitoring is necessary. By embedding these
channel events into a step-level state while preserving a shared task schema and scoring
rule, PM-Bench probes proactive and selective monitoring in addition to the evaluation logic
for time- and event-based tasks. Appendix Section A.2 details the exact channel taxonomy
used in the released week.
5

Published as a conference paper at COLM 2026
Figure 3: The 4 Major Agent Setups Evaluated on PM-Bench.
3.3 Solvability and Consistency Validation
Every generated scenario is validated before use. We first check structural validity, such
as the presence of unique step and task identifiers, then enforce a set of conditions that
ensure that the simulation is solvable. Event tasks must reference cues that actually appear,
time tasks must align with valid step times, and update operations must point to valid
target tasks with realizable revised cues or times. In particular, same-day reschedules and
overrides are disallowed from silently moving a target backward relative to the update step.
Together, these checks make PM-Bench a controlled benchmark artifact in which failure
modes can all be attributed to model behavior, and this benchmark is completely solvable
under optimal proactive environment monitoring. Appendix Section A.3 lists the full
invariant set and gives a worked override example.
4 Experiments
4.1 Experimental Setup
All methods are evaluated on the same simulated PM-Bench week and scored with the same
replay-based evaluator. Each step presents a short narrative, three ongoing-activity choices
that enable the agent to proceed to the next step, and a menu of anonymous action handles
that mixes valid actions with lures. We evaluate 64 runs in total: 8 model backbones and 8
agent configurations. The model set spans closed-weight and open-weight frontier models:
GPT-5.4, GPT-5.3-Codex, Llama-3.3-70B-Instruct, Mistral-Large-3-675B-Instruct-2512,
mistral-small-3.2-24b-instruct, and Qwen3 at 8B, 14B, and 32B scales (Yang et al., 2025).
For model inference, we serve the Qwen-3 models on 4xH100 GPUs. We use the OpenRouter
2 API for all other LLMs that we evaluated. Appendix Section A.4 provides the full replay-
evaluator definition and diagnostic metric taxonomy, and A.5 gives the full operational
definitions and prompting details for all eight evaluated setups, including the replay-based
ablations. As illustrated in Figure 3, we use the following agent configurations:
Single-agent baseline.A single model navigating the environment without external
memory scaffolds, role decomposition, or any specialized prompting strategy. This is the
reference point for all other methods.
Todo-ledger single agent.This variant allows the agent to maintain an explicitin-context
ledger of pending intentions, expected cues or times, and completion status. The ledger is
carried forward across steps and updated at every turn, testing whether intuitive note-taking
can improve execution quality.
2https://openrouter.ai/
6

Published as a conference paper at COLM 2026
Heartbeat-augmented single agents.These variants add periodic monitoring nudges that
remind the agent to consider querying hidden-state channels. In the optional-heartbeat vari-
ant, the agent canchooseto enable or disable a periodic heartbeat by emitting set heartbeat
and selecting a 30- or 60-minute interval. We compare this agent-controlled setting against
two fixed schedules in which the runtimeautomaticallyenables heartbeat every 60 or 30
virtual minutes at the start of each day.
Hierarchical multi-agents.In this method, the main coordinator agent manages three
subagent specialists. As the coordinator agent delegates tasks, each subagent can track
a separate signal from the environment, and propose hidden-state queries. The system
executes the union of those query suggestions, and the coordinator then chooses the final
action set. This is our main multi-agent configuration.
Majority and unanimous voting ablations.To isolate the final aggregation policy from
subagents’ proposals, we replay each union-query rollout under two alternative action-
selection rules: majority vote and unanimous vote. These are deterministic replays over the
same per-step evidence, included to clarify whether the main bottleneck is query acquisition
or final action aggregation.
Primary metric.Our main outcome measure is set-level F1 over prospective action se-
lections. Let Dt denote the ground-truth due set at step t, and let ˆDt denote the set of
prospective actions selected by the agent at that step. We accumulate step-level set overlaps
over the full trajectory:
TP= ∑
t
|Dt ∩ ˆDt|,FP= ∑
t
| ˆDt \D t|,FN= ∑
t
|Dt \ ˆDt|.
Here, TP counts correctly selected due actions, FP counts selected actions that were not
actually due at that step, and FN counts due actions that the agent failed to select. We then
define
Set-F1= 2TP 2TP+FP+FN .
We emphasize this metric because neither precision nor recall alone captures successful
prospective memory in PM-Bench. Precision by itself rewards conservative under-selection,
while recall by itself could encourage spamming actions for every time step. A strong
agent must identify due intentions while suppressing incorrect actions, so Set-F1 is the most
faithful summary statistic for overall performance. Appendix Section A.4 expands this
definition with the full diagnostic error taxonomy and provides more details on a series of
auxiliary metrics, as well as a worked scoring example.
4.2 No Universal Best Scaffold Across Models and Metrics
Tables 2 and 3 show that PM-Bench does not have a universal winning scaffold. In the
aggregate, the best overall method is the optional-heartbeat single agent, with macro Set-F1
of 65.1%. The todo-ledger variant is the strongest low-noise alternative: it ranks second
on macro Set-F1 at 62.8% and has the lowest aggregate false-positive count among all
competitive setups. We’re particularly attentive to the FP count because a high FP indicates
the “spamming” behavior, where a model selects too many actions at every time step in
order to achieve a high hit rate.
The expanded aggregate view shows thatno single setup dominates every metric. Optional
heartbeat is best on overall Set-F1 and cross-day hit. Todo-ledger minimizes false positives
and attains the highest precision. Auto-heartbeat at 30 minutes is strongest on update-
sensitive execution. Figure 4 shows that the monitoring-oriented tasks follow a different
ordering, especially for tasks that require hidden-channel monitoring beyond the clock.
For the automatic-heartbeat setups, the 30-minute setup attains the best update hit rate
in Table 2 and the best hidden-channel-monitoring-required hit rate in Figure 4 at 15.8%,
but it also produces a large number of aggregate false positives, which brings the Set-F1
score down to 57.8%. The 60-minute schedule is slightly more conservative, but it still trails
7

Published as a conference paper at COLM 2026
Table 2: Aggregate comparison across all eight models. False positives and queries are totals
over all eight runs in each setup. Cross-day and update columns report hit rates on those
corresponding task subsets. † indicates replay-based ablations over the same hierarchical
union-query traces rather than fresh inference runs. Lower is better for FP .
Setup
Macro
Set-F1 (%)
Micro
Set-F1 (%) Precision (%) Cross-Day (%) Update (%) FP Queries
Single baseline 60.0 59.4 66.7 44.6 37.5 199 106
Todo ledger 62.8 62.873.237.5 41.7134118
Heartbeat (optional)65.1 65.070.650.044.4 178 130
Auto-heartbeat (60m) 56.6 52.2 62.0 32.1 44.4 422 172
Auto-heartbeat (30m) 57.8 51.5 63.2 35.747.2489 203
Hierarchical union-query 45.2 45.9 51.2 10.7 20.8 273 1661
Majority vote† 37.2 38.3 34.9 17.9 38.9 655 1661
Unanimous vote† 35.3 39.6 47.3 16.1 23.6 279 1661
Table 3: Per-model Set-F1 (%) by setup. Column abbreviations are as follows: Single = single-
agent baseline, Ledger = todo-ledger single agent, HB-opt = optional heartbeat decided
by agent, HB-60 = automatic heartbeat every 60 minutes, HB-30 = automatic 30-minute
heartbeat, UnionQ = hierarchical union-query multi-agent, M.V . = replay-based majority
vote, and U.V . = replay-based unanimous vote. Best result within each model is boldfaced.
† indicates replay-based ablations over the hierarchical union-query traces.
Model Single Ledger HB-opt HB-60 HB-30 Union M.V . † U.V .†
GPT-5.4 72.5 73.579.163.8 74.1 56.5 38.9 49.2
GPT-5.3-Codex78.974.8 76.6 74.8 71.0 55.9 39.4 47.2
Llama 3.3 70B 64.472.568.1 60.7 63.4 50.9 49.4 52.7
Mistral Large75.366.7 73.7 69.3 74.7 58.1 43.3 53.3
Mistral Small 52.663.453.0 52.7 51.6 33.6 27.6 17.2
Qwen3-32B 51.4 51.7 48.5 55.257.537.5 32.8 16.3
Qwen3-14B 43.152.350.0 34.0 30.3 43.6 41.1 31.0
Qwen3-8B 42.0 47.871.942.5 39.8 25.7 25.3 15.5
the optional-heartbeat and ledger variants on overall performance. To summarize, more
reminders do not automatically yield a better operating point.
The hierarchical multi-agent setup highlights a monitoring-heavy method, issuing 1661
total state queries across the eight models (Table 2), yet it remains behind the best single-
agent methods on Set-F1 in the same table. The replay-based vote ablations make the
tradeoff even clearer. Majority-vote boosts both clock-monitoring-required and hidden-
channel-monitoring-required hit rates in Figure 4, but this setup resulted in 655 false
positives and collapses to 37.2% macro Set-F1. Unanimous voting is more conservative
than majority vote, but it still underperforms the union-query coordinator on overall Set-F1.
This ablation shows that the bottleneck is not merely obtaining evidence to execute a task.
Appendix Section A.6 provides channel-level and more qualitative follow-up evidence
for this tradeoff.Surprisingly, the strongest scaffold is not consistent across models:
Table 3 shows that different backbones prefer different interventions. This suggests that
inference-time support methods do not provide uniform gains, but instead interact with
backbone-specific weaknesses in memory maintenance, monitoring, and action control.
4.3 Proactive Monitoring Remains Challenging Across Setups
Figure 4 shows a clear asymmetry across the three monitoring slices. Monitoring-required
tasks are hardest by a large margin for every setup, but the relationship between narrative-
cued tasks and clock-monitoring-required tasks depends on the scaffold. For the single-agent
family, narrative-cued tasks remain easier than clock-monitoring-required ones; in contrast,
the hierarchical multi-agent variants achieve higher hit rates on clock-monitoring tasks than
on narrative-cued tasks. This suggests thatagents could recover time-based intentions once
8

Published as a conference paper at COLM 2026
they decide to check the clock, yet struggle to preserve overall control on tasks that should
be executable directly from the visible narrative, similar to a catastrophic forgetting
phenomenon. Among the single-agent methods, automatic 30-minute heartbeat is strongest
on the monitoring-required slices in Figure 4, reaching 60.4% on clock-monitoring-required
tasks and 15.8% on hidden-channel-monitoring-required tasks. However, Table 2 shows
that this gain comes with 489 false positives and only 57.8% macro Set-F1. The best overall
method, optional heartbeat, reaches 54.7% on clock-monitoring-required tasks and 10.0% on
hidden-channel-monitoring-required tasks while retaining the strongest overall Set-F1. The
majority-vote setup reaches even higher monitoring-required hit rates than any single-agent
method, but only by collapsing the overall set-F1.
0 20 40 60 80
Hit rate (%)
Single baseline
T odo ledger
Heartbeat (optional)
Auto-heartbeat (60m)
Auto-heartbeat (30m)
Hierarchical union-query
Majority vote†
Unanimous vote†
78.9
80.1
83.6
77.1
77.1
45.2
47.3
38.7
46.4
45.3
54.7
55.2
60.4
60.4
67.7
49.5
3.3
1.7
10.0
10.8
15.8
5.0
16.7
3.3
No Monitoring Required (Narrative-cued)
Clock-Monitoring Required
Hidden Channel-Monitoring Required
Figure 4: Monitoring-oriented hit rates across dif-
ferent setups.
The hierarchical agent setup illustrates
that with more than one agent, a scaf-
fold could elicit broad proactive state
tracking: it issues an order of mag-
nitude more queries than any single-
agent configuration in our evaluation.
However, a high monitoring frequency
alone isn’t enough. In the multi-agent
setup, the hit rate on narrative-cued
tasks drops to 45.2% as shown in Fig-
ure 4, and its channel-monitoring hit
rate remains only 5.0% despite 1661 to-
tal queries in Table 2. The challenge
is then not just to monitor more; it is
to know when monitoring should end
and how queried evidence should be
converted into the final action set.
The Appendix Section A.6 breaks
down this failure mode by channel.
Figure 4 already shows that clock-
monitoring-required tasks are the only monitoring-required part that reaches above 50%
for the stronger setups, whereas all tasks that require other signal monitoring remain weak
even after aggregation across all eight models. Several methods remain exactly 0% on
multiple non-clock channels in Table 7, and the best channel-monitoring hit rate is only
16.7%.PM-Bench is therefore far from solved on the part of prospective memory that
most resembles real-world environment monitoring.
4.4 Cross-Day and Update-Sensitive Tasks Remain Unsolved
Cross-day and update-sensitive tasks remain difficult across all evaluated setups. Table 2
shows that the best cross-day result is the optional-heartbeat policy at 50.0% hit rate, fol-
lowed by the single-agent baseline at 44.6%. The hierarchical multi-agent setup, despite
its heavy monitoring behavior, reaches only 10.7% cross-day hit rate. This suggests that
agents could monitor actively and still fail to preserve a deferred commitment across
many intervening steps. Similarly, the best hit rate with updated task cues comes from
automatic 30-minute heartbeat at 47.2%, with the other two heartbeat setups close behind at
44.4%. No setup exceeds 50% on either cross-day or update-sensitive execution, and many
of these long-horizon tasks remain unsolved even for the strongest agent setups.
5 Conclusion
We introduce PM-Bench, a cognitive science-inspired benchmark for LLM agents that evalu-
ates prospective memory and proactivity. PM-Bench combines synthetic, scalable scenario
generation with validation to produce controlled yet realistic long-horizon evaluations.
Across single-agent and multi-agent methods, we find that current frontier LLMs remain
far from robust on this capability. The main empirical pattern is a precision-recall control
tradeoff: methods that recover more tasks on cue often take more actions than necessary,
9

Published as a conference paper at COLM 2026
while more conservative methods under-act. Proactive monitoring remains challenging
across setups, and cross-day and update-sensitive tasks remain largely unsolved. PM-Bench
therefore suggests that prospective memory should be treated as a distinct evaluation axis
for LLM agents rather than as a byproduct of longer context windows or generic memory
retrieval. The benchmark provides a novel testbed for diagnosing these failures and for
developing agents that can act on remembered intentions reliably over time.
Ethics Statement
PM-Bench is a synthetic benchmark generated from a seeded pipeline and manually re-
viewed by the authors. It does not contain real personal records, private communications,
or other sensitive user data. To the best of our knowledge, the released benchmark materials
therefore pose minimal privacy risk.
This work did not involve a human-subject experiment for the reported benchmark results.
The benchmark design is inspired by prior cognitive-science paradigms, but the evaluation
in this paper is conducted on synthetic scenarios and model outputs.
Large language models were used to assist with parts of the paper writing process and with
preparing the presentation formatting of certain tables and figures. All model-generated or
model-assisted content was checked in detail by the authors and revised as needed. The
authors are solely responsible for the final text, tables, results, and conclusions presented in
this paper.
We also caution against over-interpreting strong benchmark performance as evidence that
an agent is safe for real-world deployment in high-stakes settings. Prospective-memory
failures can matter in domains such as health, transportation, and other safety-critical
workflows, but PM-Bench is intended as a controlled diagnostic benchmark rather than as a
certification of readiness for such applications. More broadly, systems that become better
at proactive reminder-following and environment monitoring may also introduce risks of
over-automation, or unnecessary monitoring and resource consumption. We therefore view
this benchmark as a tool for measuring and mitigating such failure modes, not for justifying
unsupervised deployment.
References
Jaewoo Ahn, Yeda Song, Sangdoo Yun, and Gunhee Kim. Mpchat: Towards multimodal
persona-grounded conversation. InProceedings of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pp. 3354–3377, 2023.
Francis T Anderson, Jan Rummel, and Mark A McDaniel. Proceeding with care for successful
prospective memory: Do we delay ongoing responding or actively monitor for cues?
Journal of Experimental Psychology: Learning, Memory, and Cognition, 44(7):1036, 2018.
Haonan Bian, Zhiyuan Yao, Sen Hu, Zishan Xu, Shaolei Zhang, Yifu Guo, Ziliang Yang,
Xueran Han, Huacan Wang, and Ronghao Chen. Realmem: Benchmarking llms in
real-world memory-driven interaction.arXiv preprint arXiv:2601.06966, 2026.
Maria A Brandimonte, Gilles O Einstein, and Mark A McDaniel.Prospective memory: Theory
and applications. Psychology Press, 2014.
Yuxuan Cai, Yipeng Hao, Jie Zhou, Hang Yan, Zhikai Lei, Rui Zhen, Zhenhua Han, Yutao
Yang, Junsong Li, Qianjun Pan, et al. Building self-evolving agents via experience-driven
lifelong learning: A framework and benchmark.arXiv preprint arXiv:2508.19005, 2025.
Ruisheng Cao, Mouxiang Chen, Jiawei Chen, Zeyu Cui, Yunlong Feng, Binyuan Hui, Yuheng
Jing, Kaixin Li, Mingze Li, Junyang Lin, et al. Qwen3-coder-next technical report.arXiv
preprint arXiv:2603.00729, 2026.
David Castillo-Bolado, Joseph Davidson, Finlay Gray, and Marek Rosa. Beyond prompts:
Dynamic conversational benchmarking of large language models.Advances in Neural
Information Processing Systems, 37:42528–42565, 2024.
10

Published as a conference paper at COLM 2026
Xin Cheng, Wangding Zeng, Damai Dai, Qinyu Chen, Bingxuan Wang, Zhenda Xie, Kezhao
Huang, Xingkai Yu, Zhewen Hao, Yukun Li, et al. Conditional memory via scalable
lookup: A new axis of sparsity for large language models.arXiv preprint arXiv:2601.07372,
2026.
Herbert F Crovitz and Walter F Daniel. Measurements of everyday memory: Toward the
prevention of forgetting.Bulletin of the Psychonomic Society, 22(5):413–414, 1984.
Yang Deng, Lizi Liao, Liang Chen, Hongru Wang, Wenqiang Lei, and Tat-Seng Chua.
Prompting and evaluating large language models for proactive dialogues: Clarification,
target-guided, and non-collaboration. InFindings of the Association for Computational
Linguistics: EMNLP 2023, pp. 10602–10621, 2023.
Key Dismukes. Concurrent task management and prospective memory: pilot error as a
model for the vulnerability of experts. InProceedings of the Human Factors and Ergonomics
Society Annual Meeting, volume 50, pp. 909–913. SAGE Publications Sage CA: Los Angeles,
CA, 2006.
Gilles O Einstein and Mark A McDaniel. Normal aging and prospective memory.Journal of
Experimental Psychology: Learning, memory, and cognition, 16(4):717, 1990.
Erin R Foster, Nathan S Rose, Mark A McDaniel, and Peter G Rendell. Prospective memory
in parkinson disease during a virtual week: effects of both prospective and retrospective
demands.Neuropsychology, 27(2):170, 2013.
Gonzalo Gonzalez-Pumariega, Leong Su Yean, Neha Sunkara, and Sanjiban Choudhury.
Robotouille: An asynchronous planning benchmark for llm agents.arXiv preprint
arXiv:2502.05227, 2025.
Yuanzhe Hu, Yu Wang, and Julian McAuley. Evaluating memory in llm agents via incre-
mental multi-turn interactions.arXiv preprint arXiv:2507.05257, 2025.
Jihyoung Jang, Minseong Boo, and Hyounghun Kim. Conversation chronicles: Towards
diverse temporal and relational dynamics in multi-session conversations. InProceedings
of the 2023 conference on empirical methods in natural language processing, pp. 13584–13606,
2023.
Cheng Jiayang, Dongyu Ru, Lin Qiu, Yiyang Li, Xuezhi Cao, Yangqiu Song, and Xun-
liang Cai. Amemgym: Interactive memory benchmarking for assistants in long-horizon
conversations.arXiv preprint arXiv:2603.01966, 2026.
Carlos E Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and
Karthik Narasimhan. Swe-bench: Can language models resolve real-world github issues?
arXiv preprint arXiv:2310.06770, 2023.
Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting Bai. Memory os of ai agent. InProceedings
of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 25972–25981,
2025.
Hyunwoo Kim, Jack Hessel, Liwei Jiang, Peter West, Ximing Lu, Youngjae Yu, Pei Zhou,
Ronan Bras, Malihe Alikhani, Gunhee Kim, et al. Soda: Million-scale dialogue distillation
with social commonsense contextualization. InProceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing, pp. 12930–12949, 2023.
Panagiotis Kourtesis and Sarah E MacPherson. An ecologically valid examination of event-
based and time-based prospective memory using immersive virtual reality: The influence
of attention, memory, and executive function processes on real-world prospective memory.
Neuropsychological Rehabilitation, 33(2):255–280, 2023.
Dong-Ho Lee, Adyasha Maharana, Jay Pujara, Xiang Ren, and Francesco Barbieri. Realtalk:
A 21-day real-world dataset for long-term conversation.arXiv preprint arXiv:2502.13270,
2025.
11

Published as a conference paper at COLM 2026
Xintong Li, Jalend Bantupalli, Ria Dharmani, Yuwei Zhang, and Jingbo Shang. Toward multi-
session personalized conversation: A large-scale dataset and hierarchical tree framework
for implicit reasoning. InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pp. 11504–11517, 2025.
Genglin Liu, Shijie Geng, Sha Li, Hejie Cui, Sarah Zhang, Xin Liu, and Tianyi Liu. We-
bcoach: Self-evolving web agents with cross-session memory guidance.arXiv preprint
arXiv:2511.12997, 2025a.
Genglin Liu, Vivian T Le, Salman Rahman, Elisa Kreiss, Marzyeh Ghassemi, and Saadia
Gabriel. Mosaic: Modeling social ai for content dissemination and regulation in multi-
agent simulations. InProceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, pp. 6401–6428, 2025b.
Tianjian Liu, Fanqi Wan, Jiajian Guo, and Xiaojun Quan. Proactiveeval: A unified evaluation
framework for proactive dialogue agents.arXiv preprint arXiv:2508.20973, 2025c.
Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri,
and Yuwei Fang. Evaluating very long-term conversational memory of llm agents. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pp. 13851–13870, 2024.
Mark A McDaniel and Gilles O Einstein. Prospective memory: An overview and synthesis
of an emerging field. 2007.
Giovanna Mioni, Peter G Rendell, Franca Stablum, Luciano Gamberini, and Patrizia S
Bisiacchi. Test–retest consistency of virtual week: A task to investigate prospective
memory.Neuropsychological Rehabilitation, 25(3):419–447, 2015.
Avni Mittal. Did you forget what i asked? prospective memory failures in large language
models.arXiv preprint arXiv:2603.23530, 2026.
Mark R Nelson, Christopher M Reid, Philip Ryan, Kristyn Willson, and Lisa Yelland. Self-
reported adherence with medication and cardiovascular disease outcomes in the second
australian national blood pressure study (anbp2).Medical Journal of Australia, 185(9):
487–489, 2006.
Charles Packer, Vivian Fang, Shishir G Patil, Kevin Lin, Sarah Wooders, and Joseph E
Gonzalez. Memgpt: towards llms as operating systems. 2023.
Peter G Rendell and Fergus IM Craik. Virtual week and actual week: Age-related differences
in prospective memory.Applied Cognitive Psychology: The Official Journal of the Society for
Applied Research in Memory and Cognition, 14(7):S43–S62, 2000.
Peter G Rendell and Julie D Henry. A review of virtual week for prospective memory
assessment: Clinical implications.Brain impairment, 10(1):14–22, 2009.
Nathan S Rose, Peter G Rendell, Alexandra Hering, Matthias Kliegel, Gavin M Bidelman,
and Fergus IM Craik. Cognitive and neural plasticity in older adults’ prospective memory
following training with the virtual week computer game.Frontiers in Human Neuroscience,
9:592, 2015.
Yiting Shen, Kun Li, Wei Zhou, and Songlin Hu. Mem2actbench: A benchmark for evalu-
ating long-term memory utilization in task-oriented autonomous agents.arXiv preprint
arXiv:2601.19935, 2026.
Rebekah E Smith and Ute J Bayen. The effects of working memory resource availability
on prospective memory: A formal modeling approach.Experimental psychology, 52(4):
243–256, 2005.
Haoran Tan, Zeyu Zhang, Chen Ma, Xu Chen, Quanyu Dai, and Zhenhua Dong. Membench:
Towards more comprehensive evaluation on the memory of llm-based agents. InFindings
of the Association for Computational Linguistics: ACL 2025, pp. 19336–19352, 2025a.
12

Published as a conference paper at COLM 2026
Zhen Tan, Jun Yan, I-Hung Hsu, Rujun Han, Zifeng Wang, Long Le, Yiwen Song, Yanfei
Chen, Hamid Palangi, George Lee, et al. In prospect and retrospect: Reflective memory
management for long-term personalized dialogue agents. InProceedings of the 63rd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 8416–
8439, 2025b.
Yuanbo Tang, Huaze Tang, Tingyu Cao, Lam Nguyen, Anping Zhang, Xinwen Cao,
Chunkang Liu, Wenbo Ding, and Yang Li. Proactive agents, long-term user con-
text, vlm annotation, privacy protection, human-computer interaction.arXiv preprint
arXiv:2602.04482, 2026.
Kimi Team, Yifan Bai, Yiping Bao, Y Charles, Cheng Chen, Guanduo Chen, Haiting Chen,
Huarong Chen, Jiahao Chen, Ningxin Chen, et al. Kimi k2: Open agentic intelligence.
arXiv preprint arXiv:2507.20534, 2025.
Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi
Pan, Yueqi Song, Bowen Li, Jaskirat Singh, et al. Openhands: An open platform for ai
software developers as generalist agents.arXiv preprint arXiv:2407.16741, 2024.
Yu Wang and Xi Chen. Mirix: Multi-agent memory system for llm-based agents.arXiv
preprint arXiv:2507.07957, 2025.
Zhenting Wang, Huancheng Chen, Jiayun Wang, and Wei Wei. Memex (rl): Scaling long-
horizon llm agents via indexed experience memory.arXiv preprint arXiv:2603.04257,
2026.
Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford,
Hyung Won Chung, Alex Tachard Passos, William Fedus, and Amelia Glaese. Browsec-
omp: A simple yet challenging benchmark for browsing agents.arXiv preprint
arXiv:2504.12516, 2025.
Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. Long-
memeval: Benchmarking chat assistants on long-term interactive memory.arXiv preprint
arXiv:2410.10813, 2024.
J Xu. Beyond goldfish memory: Long-term open-domain conversation.arXiv preprint
arXiv:2107.07567, 2021.
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. A-mem:
Agentic memory for llm agents.arXiv preprint arXiv:2502.12110, 2025.
BY Yan, Chaofan Li, Hongjin Qian, Shuqi Lu, and Zheng Liu. General agentic memory via
deep research.arXiv preprint arXiv:2511.18423, 2025.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chang Gao, Chengen Huang, Chenxu Lv, et al. Qwen3 technical report.arXiv preprint
arXiv:2505.09388, 2025.
Alex L Zhang, Tim Kraska, and Omar Khattab. Recursive language models.arXiv preprint
arXiv:2512.24601, 2025.
Kehao Zhang, Shangtong Gui, Sheng Yang, Wei Chen, and Yang Feng. Learning to remem-
ber: End-to-end training of memory agents for long-context reasoning.arXiv preprint
arXiv:2602.18493, 2026a.
Yinger Zhang, Shutong Jiang, Renhao Li, Jianhong Tu, Yang Su, Lianghao Deng, Xudong
Guo, Chenxu Lv, and Junyang Lin. Deepplanning: Benchmarking long-horizon agentic
planning with verifiable constraints.arXiv preprint arXiv:2601.18137, 2026b.
Yujie Zhao, Boqin Yuan, Junbo Huang, Haocheng Yuan, Zhongming Yu, Haozhou Xu,
Lanxiang Hu, Abhilash Shankarampeta, Zimeng Huang, Wentao Ni, et al. Ama-bench:
Evaluating long-horizon memory for agentic applications.arXiv preprint arXiv:2602.22769,
2026.
13

Published as a conference paper at COLM 2026
Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. Memorybank: Enhanc-
ing large language models with long-term memory. InProceedings of the AAAI conference
on artificial intelligence, volume 38, pp. 19724–19731, 2024.
A Additional Benchmark Details and Results
This appendix is written as a reviewer-facing companion to the main paper. Section 3
gives the concise benchmark overview; the appendix records the corresponding interface
details, generation recipe, solvability checks, evaluator definitions, prompt mechanics, and
additional results for the benchmark week used in our experiments.
A.1 Benchmark Interface and Task Format
For reference, each PM-Bench step exposes four participant-visible objects. First, the agent
sees a short narrative vignette describing the current situation. Second, it must choose one
of three ongoing-activity options A/B/C to advance the day. Third, it receives an optional
action menu whose entries are anonymous handles of the form task N. Fourth, it may issue
hidden-state queries to the available state channels before making its final choice. The
evaluator scores the chosen ongoing-activity option only for protocol compliance, but it
scores the selected prospective actions against the step’s due set.
The runtime task schema is intentionally stable even though the visible handles are not.
Internally, each task has a canonical ID, a participant-visible label, an executableaction text,
a trigger type, and a status that evolves over the day. Event tasks store a cue id; time tasks
store a target time; channel-triggered tasks additionally specify a hidden cue channel;
some tasks specify cross day or depends on; and all tasks have an encoding field indicating
whether they become active at day start or at a later step. Runtime scoring uses the canonical
task IDs, but the participant only ever acts through the step-local anonymous handles.
Handles are reshuffled per day, so success depends on acting on current due conditions
rather than memorizing IDs. Because the runtime exposes anonymous handles rather than
stable task identifiers, the agent must choose actions from current due conditions rather than
from memorized IDs. The benchmark thus evaluates a joint capability: maintaining latent
intentions across intervening activity while also deciding when hidden-state monitoring is
necessary and which currently valid actions should be executed.
Regular tasks are repeated routines such as medication reminders that share a familiar
pattern across days. Non-regular tasks are one-off intentions that must be encoded from
the day’s opening agenda or from later update messages. Active tasks are available for
selection; completed tasks are hidden from later menus; canceled tasks remain scoreable if
selected incorrectly, which lets the evaluator detect stale-memory failures after cancels and
overrides.
Query-then-act interaction.Operationally, each step follows a query-then-act protocol.
Before committing to a decision, the agent may issue zero or more monitoring queries to
the hidden channels, such as the clock, email, or appointment portal. After observing any
returned channel contents, it must commit to a joint action consisting of one ongoing-activity
choice and a subset of currently visible prospective-action handles. This design keeps the
interaction format simple while ensuring that hidden-state monitoring and prospective
action selection are part of the same decision problem.
Worked step example.The following excerpt shows an illustrative runtime state from the
benchmark, abbreviated only by trimming the action menu to a few representative entries:
Narrative.Breakfast comes together while you’re already thinking two
steps ahead.
Ongoing options.A) Pour coffee B) Open a note C) Check the window
Action menu excerpt.
task 22: Take antibiotic at breakfast.
14

Published as a conference paper at COLM 2026
Table 4: Three compact task examples. These examples show the same underlying schema
instantiated as a time-triggered task, a same-day hidden-channel event, and a cross-day
deferred intention.
Example task Trigger fields What it tests
“Send the library email at 11:50”
(send library email 1 d1)
type=time, target time=11:50, non-
regular, active from day start
Time-based prospective execution
when the clock is hidden by default.
“Finish the intake form when the portal posts it”
(appointment form ready d1)
type=event,
cue id=appointment form ready d1,
cue channel=appointment portal
Same-day hidden-channel monitor-
ing and event-triggered execution.
“Bring the pickup code when you notice the
package locker light” (crossday 2)
type=event,
cue id=package locker light d6,
cross day=true, offset=1 day
Deferred cross-day intention mainte-
nance, where the cue appears on a
later day than the encoding instruc-
tion.
task 16: Finish the intake form.
task 20: Grab the grocery bag.
task 17: Pick up the hold.
task 4: Clean the mug in the sink.
At this step, the due set contains only the breakfast medication task, whose canonical ID
is antibiotic breakfast and whose current handle is task 22. The other visible handles
are either future active tasks or lures. A correct action is therefore any valid A/B/C choice
paired with task 22 and no additional prospective handles. This example illustrates two
core properties of PM-Bench: the menu mixes true tasks with distractors, and a task can be
active without yet being due.
A.2 Scenario Generation and Composition
The benchmark week used in our experiments is deterministic, so all models and agent
setups are evaluated on the same fixed scenario. Generation proceeds in four stages:
sampling seven distinct day archetypes with intentionally irregular schedules; instantiating
day-opening agendas, step-level narratives, and mixed task families; injecting cross-day
reminders together with cancel, reschedule, and override events; and validating the resulting
week before use.
Generation recipe.More concretely, each day archetype specifies a step-count range, a
time distribution across dayparts, and an allowed task-domain mix. The generator then
instantiates four routine tasks, 2–4 narrative event tasks, 1–2 one-off irregular tasks, 1–3
channel-triggered tasks, and 10–12 lure actions for that day. Cue families are deliberately
varied so that the benchmark does not collapse onto a single repeated lexical pattern. After
day-level construction, the generator injects cross-day tasks by announcing a future intention
on an earlier day and binding it to a cue on the target day, then applies cancel, reschedule,
and override events. Candidate weeks are accepted only if they pass schema, consistency,
and solvability validation.
The state-channel taxonomy is central to PM-Bench because hidden-channel monitoring
is part of the task. Delta channels expose event-like updates accumulated since the last
relevant state change. Snapshot channels expose the current status when queried. Process-
style snapshot channels are a structured subset of snapshots that progress through a staged
lifecycle, such asin progressbeforecomplete. Table 5 lists the exact taxonomy used in the
benchmark week analyzed here.
A.3 Solvability and Consistency Validation
The benchmark week is passed through a validator designed to rule out benchmark artifacts
that would otherwise confound interpretation. In particular, it is checked for the following
invariants:
• unique step IDs, task IDs, and lure IDs, with no lure-task ID collisions;
15

Published as a conference paper at COLM 2026
Table 5: PM-Bench state-channel taxonomy. Delta channels expose event-like updates when
queried, while snapshot channels expose the current status at query time. Process-style
snapshot channels additionally follow a staged lifecycle.
State Channel Type
clock snapshot
email delta
calendar delta
course portal delta
price tracker snapshot
bank balance snapshot
shipment status snapshot (process)
laundry status snapshot (process)
library hold delta
reservation waitlist delta
appointment portal delta
• monotonic step times within each day and valid time alignment for time-triggered
tasks;
• realizable event cues, including cues that appear either in narrative text or in the
appropriate hidden state channel;
• valid update targets, with cancel / override / reschedule operations pointing to
existing active tasks;
• no same-day reschedule or override that silently moves a task backward in time
relative to the update step;
• no stale canceled instructions in day openings or later visible reminders;
• no current-time leakage in step prose when time is meant to be hidden;
• valid cross-day exposure, meaning long-horizon tasks are introduced on an earlier
day and not re-announced as ordinary same-day tasks on the due day;
• valid dependencies, including existence checks and acyclicity;
• process-channel consistency, such as requiring anin progressstage before acomplete
stage on channels like shipment and laundry status.
Beyond these structural checks, PM-Bench also runs a perfect-play audit over the finished
scenario. This audit executes an oracle-style policy that monitors all necessary channels and
selects every currently due action. The scenario is accepted only if every non-canceled task
can be completed on time under this policy. This matters because it lets us attribute misses
to model behavior rather than to an impossible benchmark artifact.
Worked update example.Consider an override case in which the day-opening instruction
initially says to pick up the replacement filter when the hardware counter clears. A later
update changes the task to “Pick up the replacement filter when the follow-up text comes in,”
with a new cue ID but the same action text. After that update, the original cue is no longer
scoreable. The due set therefore doesnotcontain the task when the old hardware-counter
condition would have fired; it becomes due only when the updated follow-up-text cue
appears. This is the evaluator behavior used for overrides throughout PM-Bench.
A.4 Evaluation Protocol and Metrics
PM-Bench uses a replay-based evaluator over the logged trajectory. At each step t, the
scenario defines a due set Dt after applying all task activations, cancellations, overrides,
reschedules, and dependency constraints. The agent produces a chosen set ˆDt by selecting
some subset of the current anonymous handles, which the runtime maps back to canonical
task IDs before scoring.
16

Published as a conference paper at COLM 2026
The primary metric is set-level F1:
Set-F1= 2TP 2TP+FP+FN
where TP, FP, and FN are accumulated over all steps. We use Set-F1 as the headline metric
because PM-Bench penalizes both under-selection and over-selection: high recall can be
achieved by spamming actions, and high precision can be achieved by never acting. A
strong policy must surface due tasks while maintaining control over false positives.
In addition to Set-F1, the evaluator records a diagnostic breakdown:
•Hit / on-time execution: a due task is selected at its correct step.
• Late execution: an event task is selected one step late, or a time task is selected
within 60 virtual minutes after its target.
•Miss: a non-canceled task is never completed by the end of the day.
• False alarm: a chosen task is not due now, is not active yet, or is attempted after its
late window expires.
• Wrong-content: the agent acts on the wrong task at a step where some other task is
due.
• Update violation: the agent acts on a stale version of a task after a cancel, override,
or reschedule has changed what is valid.
• Dependency violation: the agent attempts a task before its prerequisite is com-
pleted.
•Exact-set-match: the chosen set equals the full due set for that step.
• Query counts: the evaluator separately records check time and hidden-channel
query statecalls.
• Proactive-required hit: the task required hidden-state monitoring rather than being
fully solvable from the visible narrative alone.
• Non-clock proactive hit: the proactive-required subset excluding pure clock checks.
Compact scoring example.Consider a step where the due set contains three tasks, for
example sending a budget note, responding to a moved calendar call, and checking in with
a manager. If an agent chooses only the first two, the evaluator records two true positives,
one false negative, zero false positives, and no exact-set match. If the agent instead chooses
the budget note together with an irrelevant action, the step contributes one true positive,
one false positive, and two false negatives; it also contributes a wrong-content error because
an irrelevant task was selected while valid due tasks remained unselected.
A.5 Agent Setups and Prompting
Table 6 defines the eight evaluated setups operationally.
The single-agent baseline, the optional-heartbeat setup, and the auto-heartbeat setups all
share the same base prompt. The ledger setup appends an additional ledger instruction
block. The hierarchical setup uses separate subagent and coordinator prompts. The exact
prompt templates below are the ones used in our experiments, with line wrapping adjusted
only for typesetting.
Single-agent base prompt.
You are taking a prospective memory evaluation that assess how
you remember to do things later. One virtual day equals one
circuit of the board (7 a.m. -> 10 p.m.). Time advances step by
step with event cards. Your goal is to remember to perform tasks
at the correct time or event without reminders.
17

Published as a conference paper at COLM 2026
Table 6: Operational definitions for the eight evaluated setups. † marks replay-based
ablations over the same hierarchical traces rather than fresh model rollouts.
Setup Type Operational definition
Single baseline live One model, no external memory scaffold, no heartbeat, no
subagents.
Todo ledger live Single-agent run with an in-context ledger carried and rewrit-
ten every step.
Heartbeat (optional) live Single-agent run where the model may enable or disable a
periodic heartbeat by emittingset heartbeat.
Auto-heartbeat (60m) live Heartbeat enabled automatically at day start every 60 virtual
minutes.
Auto-heartbeat (30m) live Heartbeat enabled automatically at day start every 30 virtual
minutes.
Hierarchical union-
query
live Three specialist subagents propose query suggestions and can-
didate due tasks; the runtime executes the union of suggested
queries and a coordinator makes the final action decision.
Majority vote† replay Replay over the same union-query evidence where task han-
dles proposed by more than half of subagents are selected.
Unanimous vote† replay Replay over the same union-query evidence where only han-
dles proposed by all subagents are selected.
You must voluntarily remember to perform tasks at the right
moment. If you are unsure, you may still act; that is allowed.
No reminders will be given for missed tasks.
Some cues will cancel, override, or reschedule tasks. Always
follow the most recent instruction for any task.
Each step presents a short vignette with three ongoing-task
options (A/B/C). Pick one of A/B/C to advance. A step-level
action menu is shown before each choice. You may perform one
or more actions from the action menu in the same step.
Each action appears as task_N: <action text>. Return task_N
handles in task_ids. If you do not perform an action, set
task_ids to []. Never repeat the same task_N handle in task_ids.
Do not dump the whole menu into task_ids; include only the handles
you are actually choosing now. Return at most 8 task handles in
one choose action.
Some tasks are triggered by state cues that are NOT shown in the
vignette. You can only observe these cues by proactively querying
state channels. Available state channels: clock, email, calendar,
course_portal, price_tracker, bank_balance, shipment_status,
laundry_status, library_hold, reservation_waitlist,
appointment_portal.
Use action=query_state to retrieve channel state (choice must be
NONE). The legacy action=check_time is supported and is equivalent
to query_state with channel=clock. No reminders will be given
about when to query state; you must decide when to check.
State responses are returned as a single line:
"State [channel]: <message>".
After any query, you still must make a choose action to advance.
Example (time check):
User: You sit at your desk and feel it's close to 16:30.
18

Published as a conference paper at COLM 2026
Model: {"action":"check_time","choice":"NONE","task_ids":[],
"channel":"clock"}
User: State [clock]: Time 15:58 | Stopwatch: 538 min
Model: {"action":"choose","choice":"B","task_ids":["task_7"],
"channel":"NONE"}
Always respond in JSON. Use these exact formats:
- {"action":"query_state","choice":"NONE","task_ids":[],
"channel":"calendar"}
- {"action":"check_time","choice":"NONE","task_ids":[],
"channel":"clock"}
- {"action":"choose","choice":"A","task_ids":[],"channel":"NONE"}
- {"action":"choose","choice":"B","task_ids":["task_1"],
"channel":"NONE"}
Heartbeat extensions.Optional-heartbeat runs append the following block to the base
prompt:
You may optionally configure a periodic heartbeat for proactive
monitoring. Use action=set_heartbeat with heartbeat_enabled=true
and heartbeat_minutes in [30, 60]. This heartbeat is strictly
periodic and is NOT aligned to cue times. It only nudges proactive
checking and does not reveal hidden cues. You can disable it later
with heartbeat_enabled=false. On each heartbeat, you may receive a
nudge listing channels worth checking.
Auto-heartbeat runs instead append a fixed sentence of the form:
For this run, heartbeat is auto-enabled at the start of each day
every 60 virtual minutes.
or the corresponding 30-minute variant. In the experiments reported here, the heartbeat-
message flag is not overridden, so the heartbeat runs appear to use the defaultchannel query
nudge rather than the latertask remindervariant.
Todo-ledger addendum.
You must maintain a compact TODO ledger that tracks tasks to do
later. Always return exactly one raw JSON object with keys:
action, choice, task_ids, channel, ledger.
The ledger is a list of objects with keys:
- task_id: string (use current action handle like "task_7",
not natural-language text)
- when: string (exact time like "11:00", a cue like
"cue: breakfast", or "unknown")
- status: "pending", "done", or "canceled"
- notes: short string (optional)
Keep the ledger concise and up to date.
- Hard limit: ledger must contain at most 5 items.
- If there are more than 5 possible reminders, keep the 5 most
urgent/likely.
- Keep notes very short (<= 8 words).
- Keep only tasks that still matter; remove completed items
immediately.
If a task's exact time is known but the current time is not
visible, use action=check_time to query the current time before
deciding. When you choose actions, task_ids must be action
handles from the current step menu.
19

Published as a conference paper at COLM 2026
Do not add extra keys outside the required JSON fields.
Do not include explanations, markdown, or code fences.
Hierarchical subagent prompt.
You are a PM-Bench subagent.
Role identity: <agent_name>
Your role:
1) Analyze the current PM-Bench step using your role guidance.
2) Propose state queries BEFORE task selection.
3) Propose tasks that might be due.
4) Propose tasks that should NOT be selected now.
Role guidance:
<role-specific guidance>
Output strict JSON only (no markdown, no code fences). Every
required key must be present. Return minimal compact JSON only
(single object, no extra text).
Rules:
- Use task handles from the current step menu only (task_n).
- Use channels from available channels only.
- If no items exist for a list, return [].
- Keep evidence concise and step-grounded; avoid speculation.
In the reported three-subagent setup, the role-specific guidance is:
• event watcher: focus on event-driven opportunities from current cues and active
handles.
•status watcher: focus on proactive monitoring duties and hidden-state checks.
•update watcher: focus on cancels, overrides, reschedules, and dependency risks.
Hierarchical coordinator prompt.
You are the coordinator for PM-Bench.
You receive current step context and structured subagent signals.
Return one valid PM-Bench action JSON.
Return minimal compact JSON only (single object, no extra text).
Rules:
- action is choose, query_state, or check_time.
- If action is choose: choice must be A/B/C and channel must be NONE.
- If action is query_state/check_time: choice must be NONE and
task_ids must be [].
- check_time must use channel=clock.
- task_ids must use action handles from the current menu only.
- Use the JSON key task_ids (do not use task_handles).
Decision policy:
- Subagent structured signals provide evidence, not final decisions.
- State query phase has already run from the de-duplicated union
of subagent query suggestions.
- When evidence indicates a task is due now, include its handle(s)
in task_ids on your choose action.
- A choose action with task_ids=[] is only appropriate when no task
20

Published as a conference paper at COLM 2026
Table 7: Proactive-required hit rate by hidden channel, aggregated across all eight models. †
indicates replay-based ablations over the same hierarchical union-query traces. The table
highlights that clock-based prospective memory is substantially easier than strictly proactive
non-clock monitoring.
Setup Appt. Bank Calendar Clock Course Email Waitlist Shipment
Single baseline 8.3 0.0 4.2 46.4 12.5 0.0 0.0 0.0
Todo ledger 4.2 0.0 4.2 45.3 0.0 0.0 0.0 0.0
Heartbeat (optional) 8.3 6.2 12.5 54.7 12.5 6.2 12.5 12.5
Auto-heartbeat (60m) 12.5 12.5 12.5 55.225.06.2 8.3 0.0
Auto-heartbeat (30m) 16.7 12.520.860.4 12.5 6.220.8 12.5
Hierarchical 12.5 6.2 0.0 60.4 12.5 0.0 4.2 0.0
Majority vote† 25.0 18.88.367.712.5 0.033.30.0
Unanimous vote† 4.2 6.2 4.2 49.5 0.0 0.0 4.2 0.0
has sufficient evidence of being due now.
- Prefer precise execution: avoid selecting tasks that are only
"later" / "not yet due" / speculative.
- Treat tasks_should_not_select as strong caution unless state
evidence clearly contradicts it.
- Make the final decision carefully; avoid majority-vote shortcuts.
Operationally, hierarchical union-query proceeds in two stages per step: subagents first
emit structured query suggestions and candidate due tasks, then the runtime executes the
deduplicated union of their query suggestions, and only then does the coordinator issue the
final PM action. The replay-based majority and unanimous ablations keep the same queried
evidence and replace only the final task-selection rule.
A.6 Additional Results and Failure Analysis
Table 7 breaks proactive-required performance down by hidden channel. The main paper
already contains the aggregate setup comparison, monitoring tradeoff summary, and per-
model breakdown; this appendix adds channel-level diagnostics together with qualitative
follow-up examples.
Why the best setup is model-dependent.Our working interpretation is that the interven-
tions stress different subskills. The todo-ledger primarily helps explicit intention mainte-
nance and action precision, while heartbeat variants primarily increase proactive monitoring
and recall, often together with more false positives. Different backbones appear to begin
from different operating points on this tradeoff, so the same scaffold can help one model
while pushing another toward over-querying or over-selection.
Qualitative failure cases.Three short examples illustrate the benchmark behaviors that
remain difficult even when aggregate metrics improve.
• Missed cross-day task.In one GPT-5.4 single-baseline run, a step required both
immediate visible actions and a deferred cross-day action that had been encoded
earlier. The agent executed only the immediate visible action. This is a characteristic
long-horizon failure: the salient local cue is acted on, but the deferred companion
intention is dropped.
• Update-sensitive miss.In one Qwen3-32B auto-heartbeat-30m run, a one-off task
had been rescheduled to 11:00 and became due at the same step as a routine
medication action. The agent checked the clock and executed only the routine
medication. The run therefore handled the visible routine but failed to carry forward
the rescheduled one-off task.
• Non-clock monitoring failure.In one GPT-5.4 single-baseline run, a task became
due only because a library-hold update was available on a hidden channel. The
21

Published as a conference paper at COLM 2026
agent chose nothing and never queried that channel. This is the strict proactive case
PM-Bench is designed to expose: nothing in the visible vignette was sufficient, so
the only path to success was querying the hidden channel.
22
