---
title: AutomationBench
url: https://arxiv.org/abs/2604.18934
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Daniel Shepard
- Robin Salimans
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.18934
pages: 15
chars: 29907
fetched_at: '2026-11-08T13:05:50+00:00'
kb_version: 1
---

# AutomationBench

AutomationBench
Daniel Shepard and Robin Salimans
daniel.shepard@zapier.com
robin.salimans@zapier.com
April 2026
Abstract
Existing AI benchmarks for software automation rarely combine cross-
application coordination, autonomous API discovery, and policy adher-
ence. Real business workflows demand all three: a single task may span a
CRM, inbox, calendar, and messaging platform — requiring the agent to
find the right endpoints, follow a policy document, and write correct data
to each system. To address this gap, we introduce AutomationBench, a
benchmark for evaluating AI agents on cross-application workflow orches-
tration via REST APIs. Drawing on real workflow patterns from Zapier’s
platform, tasks span Sales, Marketing, Operations, Support, Finance, and
HR domains. Agents must discover relevant endpoints themselves, fol-
low layered business rules, and navigate environments with irrelevant and
sometimes misleading records. Grading is programmatic and end-state
only: whether the correct data ended up in the right systems. Even
the best frontier models currently score below 10%. AutomationBench
provides a challenging, realistic measure of where current models stand
relative to the agentic capabilities businesses actually need.
Figure 1: AutomationBench evaluation pipeline. The agent iteratively discovers
and calls API endpoints to complete a task. Only the final state of the simulated
applications is graded.
1
arXiv:2604.18934v1  [cs.AI]  21 Apr 2026

1 Introduction
Businesses run on a variety of interconnected web applications: CRMs, email,
calendars, spreadsheets, project management tools, marketing platforms, sup-
port systems, messaging services, and more. Coordinating actions across these
applications is one of the most time-consuming aspects of knowledge work, re-
quiring agents to follow organizational policies, reason about which information
to act on, and ignore irrelevant or misleading context.
AI agents promise to automate these workflows, but existing benchmarks
measure adjacent capabilities rather than cross-application business orchestra-
tion. WebArena [1] and Mind2Web [2] evaluate long-horizon web tasks in brows-
ing environments, and OSWorld [3] evaluates open-ended computer-use tasks
spanning real web and desktop applications. Tool and service-workflow bench-
marks evaluate tool/API use (and, in some cases, end-state success) under con-
strained settings, for example, fixed tool corpora with retrieval-based selection
(ToolBench [4], API-Bank [5]), or a small number of simulated apps/domains
with programmatic evaluation (AppWorld [6],τ 3-bench [7,8,9]). Whileτ 3-bench
recently added doc-based tool discovery in its banking domain, each task still
operates within a single application rather than requiring cross-application co-
ordination.
Benchmark Domains / Apps API Discovery End-State Grading Cross-App Business Rules Environment
WebArena [1] 4 websites×✓Limited×Containerized web apps
Mind2Web [2] 137 websites× × × ×Snapshots
OSWorld [3] Real OS + apps×✓ ✓×Real OS
ToolBench [4] 16k+ APIs Retrieval× × ×RapidAPI
API-Bank [5] 73 APIs Retrieval× × ×Simulated
AppWorld [6] 9 apps Given✓ ✓×Simulated
τ 3-bench [7,8,9] 4 domains Partial✓×✓Simulated
AutomationBench 6 domains/47 apps Retrieval✓ ✓ ✓Simulated
Table 1: Comparison of AutomationBench with existing benchmarks. Units in theDomains
/ Appscolumn vary by benchmark to reflect how each defines its scope.API Discovery
indicates whether the agent must find relevant endpoints itself.Cross-Appindicates whether
tasks require coordinating actions across multiple independent applications.Business Rules
indicates whether tasks embed organizational policies that the agent must consult and follow.
AutomationBench fills this gap. Agents receive a natural language business
task and must autonomously discover available REST API endpoints across
dozens of integrated applications, make sequential and interdependent calls,
apply layered business rules, and navigate environments seeded with distractors,
decoy records, and adversarial inputs. Tasks span Sales, Marketing, Operations,
Support, Finance, and HR domains. Grading is purely on end-state correctness,
whether the right data ended up in the right systems, using programmatic
assertions against a simulated world state. This reflects how businesses actually
evaluate automation.
Our objective is to accelerate research on cross-application agent orchestra-
tion — enabling AI agents to coordinate actions across diverse web applications.
Though solutions like MCPs and CLI tools exist, REST APIs are the uni-
versal standard and frequently the glue behind those tools. Direct, accurate use
of REST APIs dramatically expands the set of applications agents can interact
2

with without requiring purpose-built integrations. Computer use offers broader
access but at significantly higher computational cost, making API-based orches-
tration a more practical near-term path for high-volume business automation.
Advances in multi-step reasoning, policy adherence, and tool discovery would
unlock a new class of complex automation tasks that current models cannot
reliably complete. AutomationBench is designed to expose and measure this
gap, directing research effort toward the capabilities businesses need most.
2 Dataset construction and validation
Domain Public Private (Eval)
Sales 100 100+
Marketing 100 100+
Operations 100 100+
Support 100 100+
Finance 100 100+
HR 100 100+
T otal 600 600+
Table 2: Task distribution across domains. Public tasks are used for research and experimen-
tation; private tasks are held out exclusively for evaluation.
We created realistic tasks for six distinct domains: Sales, Marketing, Opera-
tions, Support, Finance, and HR. These domains are the most popular types of
workflows Zapier customers use to automate their businesses. A pool of∼500
API endpoints across 47 apps is used across the different domains.
To maintain the integrity of the benchmark, at least half of the tasks are
private. Currently, there are 100 public tasks per domain and even more private
ones. Scores will be posted to the leaderboard based on the private dataset. The
private dataset started from a similar distribution as the public but has some
additional hardening techniques applied.
Tasks were synthetically generated based on use cases from real customers.
No PII or confidential customer data was used — only the shape of workflows
sent along with negative feedback on Zapier’s Agents service. We were targeting
workflows that are difficult to set up. We clustered these and used the relevant
entries for each domain. We fed these workflow patterns into models for inspi-
ration and made many passes on realism, difficulty, and variety of apps. We
used Opus 4.6, GPT 5.3 Codex, and Gemini 3 in task generation. To encourage
growth in reasoning and be a challenging benchmark, we hardened tasks that
were too easy. Few tasks should be easy enough to be solvable by the smallest
models. In tasks, we try to capture the complexity of real operations by multiple
layers of difficulty and noise.
We used a variety of hardening techniques, including, but not limited to,
adding irrelevant data, keeping key info behind tool call responses, ambiguity of
3

where info can be found, similar naming for incorrect entries, and strict business
policy rules with overriding priorities. We developed these techniques through
experiments on what is challenging for current models. The private dataset
employs additional hardening techniques to prevent overfitting on a small set of
challenges. Benchmark progress ideally reflects improved reasoning over novel
complexity rather than mastery of a few known difficulty types.
Many business workflows require subjective judgment — assessing lead qual-
ity, determining urgency, or choosing a routing path. We limit subjectivity in
this benchmark, but some degree is supported in these tasks by requiring the
agent to record its decision as a structured state change (e.g., updating a status
field, assigning a score, routing to a queue) rather than producing free-form
text. Assertions then verify the recorded decision and any required downstream
effects.
Some tasks require the agent to follow policy documents that override seem-
ingly reasonable defaults or external requests. Although this tests an important
real-world skill (adhering to organizational rules over intuition), it superficially
resembles a prompt injection. To avoid conflating policy-following with prompt-
injection compliance, task prompts explicitly reference these policy documents,
signaling that consulting them is expected behavior rather than an adversarial
trick.
Every task must satisfy all of the following:
•Observable outcome:The task must produce at least one concrete state
mutation (object created, field updated, label applied, event scheduled,
activity logged, etc.).
•Deterministic validation:Correctness must be decidable using invariant-
based checks, not subjective interpretation.
•No free-form success criteria:Success must be expressible as struc-
tured invariants over the world state.
•Reasoning must commit:If a task requires judgment or reasoning, the
agent must record the decision in the system state.
•Autonomous:A single instruction must be given. Then the task is
non-interactive until completion.
Example task (Full examples are in the Appendix):
There’s a scheduling conflict on February 20, 2026 at 2:00 PM —
a Zoom meeting and a Google Calendar event overlap. Check the
meeting priority policy in the spreadsheet to determine which one
wins, then reschedule the loser by prepending[RESCHEDULED] to
its topic/title. Post a summary to#ops-updateson Slack noting
which meeting won and which was rescheduled, including both the
Zoom meeting ID and Calendar event ID.
4

To verify that tasks are solvable, we created a separate hint sheet that pro-
vides additional guidance for each task within a separate runtime mode. These
include instructions on which endpoints to call and clues on parameters but not
the parameters themselves. This allowed even smaller models to score around
80–100% (such as Haiku). All tasks should be expected to achieve 100% ac-
curacy with larger models (such as Opus), though single-digit variance still
persists. We inspected a sampling of tasks and repeated audits to catch errors.
Hints deliberately exclude actual parameter values, as including them could
bypass tool calls entirely and mask discoverability issues. We audited hints
against a rules document to catch such violations.
Because the benchmark was built on Prime Intellect’s Verifiers framework,
we were able to pressure-test the benchmark by running Reinforcement Learn-
ing with Verifiable Rewards experiments with minimal setup in their Lab. These
runs identified some common reward-hacking strategies that we used to strengthen
the reward function.
3 Tool interface
Public API schemas are provided for each app. To access these, the agent
must use two tools: Search and Execute. Search performs keyword searches
(BM25) across all available API schemas (top-k of 5). Execute mimics a curl or
fetch request accepting method, url, and body. No authentication is mimicked.
Finding the right endpoints to use is part of the challenge. The correct app
or action name might not be known. The agent must explore the available
tools and figure it out. The execute tool triggers a simulation of retrieving or
updating a database through Pydantic Models. These Pydantic models serve as
the source of truth for the state of the app. We preserve theshapeof real API
schemas, including pagination, required fields, and common error cases (4xx
status codes).
We specify a maximum of 50 steps. This limit is rarely hit (tasks in the single
digits). We can increase it if future models regularly hit this limit. Multiple
tools can be called in parallel per step.
4 Scoring
For this benchmark, instead of grading a text response or document, we consider
only the end state of each connected app. How the Agent got there is not a
concern (what tools were called in what order or way), only the end state.
Sometimes, multiple API endpoints can produce similar results. So, if the agent
was supposed to send an email, create a lead, and update another lead, the
grader checks the “sent mailbox folder” and the lead entries and verifies that all
expected data is correct. If an agent takes multiple actions inefficiently (create
the lead, update the lead 5 times instead of once), it yields the same end result
and scores equally, but with a higher Cost.
5

Focusing on end-to-end results gives the agent flexibility to solve problems
in creative ways (such as parallel tool calls and batched changes) while avoiding
being overly prescriptive. It also keeps the tool’s side effects in focus as that is
what businesses care about.
The assertions for each task are used to deterministically verify the state
to define success. We give no partial credit but we can see how close models
get to completion for non-scoring purposes. Businesses do not want partially
completed workflows. The task must be completed to earn a positive score.
Scores can then be compared across models.
Scores are for a single run. Run-to-run variance is typically within 1%.
We also report Cost (USD per run) alongside Score on the leaderboard,
acknowledging that two models with the same pass rate may differ substantially
in efficiency. Cost is computed by taking the average token cost spent per task.
Time is harder to compare across models and providers due to rate limiting
(especially on unreleased alpha models with limited compute). So Cost is the
primary efficiency metric at this point.
We include negative assertions to prevent shotgun approach reward hacking
(sending the email multiple times to everyone in the company instead of just
the specified recipient).
We use deterministic assertions instead of LLM-as-a-judge. All success cri-
teria are expressed as exact string matches and structural checks over the world
state, without semantic or subjective evaluation of text. This ensures scores
are largely reproducible across runs and eliminates some potential inter-model
grading bias. We want to minimize the score of one model based on another
model’s judgement (though synthetically generated data still carries some of
this risk).
5 Limitations
As with any synthetically generated data, there is a risk of lack of realism and
impossibility. The scale and complexity of tasks also make it challenging to
manually review all tasks in a reasonable time frame. We manually inspected
samples of tasks to reduce this risk.
We used various hardening techniques to realistically increase the difficulty
of the tasks. Once these challenges are overcome, there will likely still be some
reasoning gaps that matter for real business workflows. We can address these
with later versions of the benchmark.
We regularly audited for bugs and unrealistic complexity, but there is still
room for improvements. We plan to continue fixing bugs and will version major
changes.
6

6 Leaderboard
Model Score Cost per task
Opus 4.7 (max) 9.9%$1.80
Gemini 3.1 Pro (high) 9.6%$0.54
GPT 5.4 (high) 7.6%$1.93
Sonnet 4.6 (max) 5.3%$1.81
Haiku 4.5 1.5%$0.18
GPT 5.4 (no reasoning) 1.2%$0.19
Figure 2: Model Results with Reasoning Effort
7 Results
State-of-the-art models all score below 10%. Opus 4.7 tops the leaderboard at
9.9%. See our benchmark leaderboard page [10] for up to date results.
Models are solving fairly different sets of tasks from each other. Gemini and
Opus are the top scoring models. Their passing sets have a Jaccard similarity
of 0.17. 71% of the tasks solved by Opus are not solved by Gemini, and 70% of
Gemini’s passes are missed by Opus.
Sonnet 4.6 generates so many more tokens than Opus 4.7 that it costs more
per task at every reasoning effort level, while also achieving a lower pass rate.
Gemini achieves some of the highest accuracy at a fraction of the cost.
Opus uses an average of 12.6 steps and with 29.8 tool calls per task whereas
Gemini uses 21.8 steps and 35.4 tool calls. GPT 5.4 high uses a similar number
7

of steps at 15.4 but uses more tool calls at 43.9.
Given the multiple layers of complexity, we created some different toolsets
and modes to diagnose issues and model deficiencies.
We built an alternative Zapier toolset using tool schemas based on Zapier’s
internal actions. This toolset usually results in an increased score over the API
toolset, probably because they are more digestible than raw API schemas.
There is also a Limited Zapier toolset that uses only the specific Zapier
tools necessary to perform the task instead of the typical Search + Execute
tools. Some models benefit disproportionately from a narrower tool surface.
Gemini 3.1 Pro passes 9.6% (API/default), 12.8% (Zapier), and 14.3% (Lim-
ited Zapier); Haiku 4.5 passes 1.5%, 2.0%, and 3.8% respectively.
We also created a simple domain as a baseline to signal how well models do
with simpler workflows without the noise and difficulty of regular tasks. This
is not used in the benchmark score, but as a test of the harness. Even Haiku
scored 97% on this domain. For simple tasks with explicit instructions, today’s
models do just fine.
All of these toolsets and public tasks are available to try out from our public
repository [11] and Prime Intellect’s Environments Hub [12].
Having multiple failure modes and layers of complexity requires model rea-
soning to grow more capable in multiple ways rather than conquering it with a
single improvement. This makes the benchmark more resilient and relevant as
models improve.
Common failure modes
More often than not, models declared success while actually failing. 72% of
Opus’s failures, 91% of Gemini’s, and 84% of GPT 5.4’s involved this false
confidence. One common failure mode for completing tasks is not finding data.
Models often are not persistent or methodical enough in searching for data when
generic searches do not find the results. They make assumptions about where
data should live — e.g., assuming a CRM instead of Google Sheets, when that
is not always the case. Another failure mode is missing items. When a task
involves processing a list (12 emails, 8 leads), models frequently process some
items correctly and then summarize as if done without verifying every item was
covered. Models also do not follow instructions exactly. They paraphrase or
outright ignore requirements for the content to include certain values despite
precise instructions being given.
8 Acknowledgements
I (Daniel) want to thank Robin Salimans for helping create the architecture
and offering technical guidance. We also thank Jake Talgard for advice and
assistance with stakeholder communication. Thanks to Anna Marie Clifton,
our director of product, for helping kickstart and prioritize this benchmark.
Mike Knoop provided valuable feedback and expertise on benchmarks with ARC
8

Prize. We thank Jichao Yin for brainstorming and sanity checking. Thanks to
Prime Intellect, Anthropic, and OpenAI for their early feedback, and to many
others at Zapier who cleared the way and supported us to focus on building
this.
9 Disclaimer
The company names, product names, and API schemas referenced in this bench-
mark are trademarks or intellectual property of their respective owners. API
schemas are based on publicly available documentation and are used solely for
research and evaluation purposes under fair use. App behavior is simulated
through synthetic models and does not represent exact production behavior.
All data within tasks is entirely fictional — no real user data, transactions, or
confidential information from any third party is included. This benchmark is
not affiliated with, endorsed by, or sponsored by any of the companies whose
products are referenced.
10 References
1. S. Zhou, F. F. Xu, H. Zhu, X. Zhou, R. Lo, A. Sridhar, X. Cheng, T.
Ou, Y. Bisk, D. Fried, U. Alon, G. Neubig.WebArena: A Realistic Web
Environment for Building Autonomous Agents.ICLR, 2024.
2. X. Deng, Y. Gu, B. Zheng, S. Chen, S. Stevens, B. Wang, H. Sun, Y. Su.
Mind2Web: Towards a Generalist Agent for the Web.NeurIPS, 2023.
3. T. Xie, D. Zhang, J. Chen, X. Li, S. Zhao, R. Cao, T. J. Hua, Z. Cheng, D.
Shin, F. Lei, Y. Liu, Y. Xu, S. Zhou, S. Savarese, C. Xiong, V. Zhong, T.
Yu.OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks
in Real Computer Environments.NeurIPS, 2024.
4. Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang,
B. Qian, S. Zhao, L. Hong, R. Tian, R. Xie, J. Zhou, M. Gerstein, D. Li,
Z. Liu, M. Sun.ToolLLM: Facilitating Large Language Models to Master
16000+ Real-World APIs.ICLR, 2024.
5. M. Li, Y. Zhao, B. Yu, F. Song, H. Li, H. Yu, Z. Li, F. Huang, Y. Li.API-
Bank: A Comprehensive Benchmark for Tool-Augmented LLMs.EMNLP,
2023.
6. H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta,
A. Sabharwal, N. Balasubramanian.AppWorld: A Controllable World
of Apps and People for Benchmarking Interactive Coding Agents.ACL,
2024.
9

7. S. Yao, N. Shinn, P. Razavi, K. Narasimhan.τ-bench: A Benchmark
for Tool-Agent-User Interaction in Real-World Domains.arXiv preprint
arXiv:2406.12045, 2024.
8. V. Barres, H. Dong, S. Ray, X. Si, K. Narasimhan.τ 2-Bench: Evaluating
Conversational Agents in a Dual-Control Environment.arXiv preprint
arXiv:2506.07982, 2025.
9. Q. Shi, A. Zytek, P. Razavi, K. Narasimhan, V. Barres.τ-Knowledge:
Evaluating Conversational Agents over Unstructured Knowledge.arXiv
preprint arXiv:2603.04370, 2026.
10. AutomationBench Leaderboard.https://zapier.com/benchmarks
11. AutomationBench Public Repository.https://github.com/zapier/AutomationBench
12. Prime Intellect Environment.https://app.primeintellect.ai/dashboard/
environments/zapier/AutomationBench
11 Appendix: Task Examples
Example task data is simplified and includes additional notes for illustration
purposes.
Task 1·Sales — Meeting Conflict Resolution
Prompt
There’s a scheduling conflict on February 20, 2026 at 2:00 PM —
a Zoom meeting and a Google Calendar event overlap. Check the
meeting priority policy in the spreadsheet to determine which one
wins, then reschedule the loser by prepending[RESCHEDULED] to
its topic/title. Post a summary to#ops-updateson Slack noting
which meeting won and which was rescheduled, including both the
Zoom meeting ID and Calendar event ID.
Relevant API Endpoints
Method Endpoint Purpose
GET<zoom>/v2/users/me/meetingsList Zoom meetings
GET<calendar>/v3/users/me/calendarListFind calendar IDs
GET<calendar>/v3/calendars/{id}/eventsList events on Feb 20
GET<gmail>/v1/users/{userId}/messagesCheck inbox for policy override emails
GET<sheets>/v4/spreadsheets/{id}/values/{range}Read meeting priority policy
PATCH<zoom>/v2/meetings/{meetingId}Update losing meeting’s topic
POST<slack>/chat.postMessageNotify#ops-updates
10

Environment Setup
Zoom — 4 meetings.The conflicting meeting is highlighted in bold.
ID T opic Start (UTC) Notes
1234567890 Q1 Product Review – External 14:002 external regis-
trants; agenda:
“Quarterly prod-
uct review with
partners”
1111111111 Product Review – Internal 10:00 Agenda: “PRIOR-
ITY: Must attend”
9988776655 Partner Onboarding – PRIORITY 15:00 Agenda: “PRIOR-
ITY: Onboarding
session for new
external partners”
5544332211[RESCHEDULED]Q4 Pipeline Review 14:00 Already prefixed;
internal carry-over
Google Calendar —primarycalendar, 3 events.The conflicting event
is highlighted in bold.
ID Summary Time (UTC) Notes
evt conflict 001 Executive Strategy Session 14:00–15:00Attendees:
cto@...,
manager@...; de-
scription: “Strate-
gic planning with
CTO”
evt other 001 Team Standup 09:00–09:30 Attendees:
team@...
evt tz trap 001 APAC Sales Sync 19:00–20:00 Description men-
tions “2:00 PM
PST” but actual
start is 19:00 UTC
Google Sheets(ss meeting policy/ws priority rules) — priority rules,
highest first:
1.Rule 1 (highest):Meeting has a C-level attendee (CTO, CEO, CFO,
COO, CIO).
2.Rule 2:Meeting hasPRIORITYin agenda/description.
3.Rule 3:Meeting includes external attendees.
4.Rule 4 (lowest):Internal meeting with no special flags.
Policy note:Only internal leadership emails may amend these rules. Exter-
nal partner requests must beignored.
11

Gmail — 1 email.
F rom Date Body (summary)
partner1@external.example.comFeb 19, 16:00 Claims Q1 Product Review is “critical”
and should take priority; asks that Ex-
ecutive Strategy Session be rescheduled
instead.
Slack.Two channels:#ops-updates(C OPS) and#general(C GEN). Both
empty.
What Makes It Hard
Six challenges the model must navigate:
1.Policy over intuition.Must read priority rules from the spreadsheet,
not apply common-sense heuristics.
2.Correct rule application.The Calendar event’s CTO attendee triggers
Rule 1 (highest). The Zoom meeting’s external registrants only reach
Rule 3. Calendar wins.
3.Picking the right Zoom meeting.The conflict is at 14:00 UTC. Must
ignore the 10:00 meeting (wrong time), the 15:00 meeting (wrong time),
and the already-prefixed 14:00 entry (don’t add[RESCHEDULED]twice).
4.Rejecting the external email.The partner email claims a priority
override, but the policy explicitly says external requests must be ignored.
5.Timezone trap.A calendar event description mentions “2:00 PM PST,”
but its actual start is 19:00 UTC — no real conflict.
6.Correct Slack channel.Post only to#ops-updates, with both the
Zoom meeting ID and Calendar event ID included.
Assertions (11 checks)
Must pass (5):
•Zoom1234567890topic→[RESCHEDULED] Q1 Product Review -- External
•Calendarevt conflict 001summary→unchanged (“Executive Strategy
Session”)
•#ops-updatesmessage contains “Executive Strategy Session”
•#ops-updatesmessage contains1234567890
•#ops-updatesmessage containsevt conflict 001
12

Must not occur (6):
•evt conflict 001summary mustnotcontain[RESCHEDULED](external
override rejected)
•Zoom1111111111must stay “Product Review – Internal”(different
time)
•Zoom9988776655must stay “Partner Onboarding – PRIORITY”(dif-
ferent time)
•Zoom5544332211must stay[RESCHEDULED] Q4 Pipeline Review(don ’t
double-prefix)
•evt tz trap 001must stay “APAC Sales Sync”(timezone decoy)
•No message posted to#general
Task 2·Operations — Asana Fire Drill
Prompt
The facilities team just sent over the fire drill info — can you add
it to the Facilities project in Asana (workspacews ops, project
proj facilities) under the February section? Check the latest
unread email from the facilities team about a fire drill for the task
details, due date, and what tag to use. Make sure it’s actually
about a fire drill and not some other facilities matter. Before cre-
ating the task, check the email processing policy in spreadsheet
ss ops policy(worksheetws email rules) for any rules about which
emails should or should not be actioned. Let#ops-updatesknow
once it’s created.
Relevant API Endpoints
Method Endpoint Purpose
GET<gmail>/v1/users/{userId}/messagesSearch inbox for fire drill email
GET<gmail>/v1/users/{userId}/messages/{id}Fetch full email body
GET<sheets>/v4/spreadsheets/{id}/values/{range}Read email processing policy
GET<asana>/1.0/projects/{project gid}/sectionsFind February section
POST<asana>/1.0/tasksCreate the Asana task
POST<asana>/1.0/sections/{section gid}/addTaskAdd task to February section
POST<asana>/1.0/tasks/{task gid}/addTagTag task as Compliance
POST<slack>/chat.postMessageNotify#ops-updates
Environment Setup
Gmail — 6 emails from facilities (+ 30 noise emails).The correct email
is highlighted in bold.
13

F rom Date Read? Notes
facilities@Jan 26, 10:00 Yes Already read — not the latest unread
facilities@Jan 28, 09:15 No Correct — fire drill, due F eb 18, tag:
Compliance
facilities@Jan 28, 10:00 No Wrong subject: annual safety audit
maintenance@Jan 28, 11:00 No Wrong sender: not facilities team
facilities@Jan 29, 08:00 No Body contains “DRAFT — DO NOT AC-
TION”
facilities@Jan 29, 09:00 No Body contains “SUPERSEDED”
Google Sheets(ss ops policy/ws email rules) — two relevant policies
(+ 15 noise rows):
•Draft Notification Policy:Emails containing “DRAFT” or “DO NOT
ACTION” must not be actioned.
•Superseded Email Policy:Emails containing “SUPERSEDED” must
not be actioned; use the most recent valid email instead.
Asana.Projectproj facilitiesin workspacews ops. Pre-seeded lookup:
“February” section→sec feb.
Slack.Three channels:#ops-updates,#general,#facilities-general(+
20 noise messages in#ops-updates).
What Makes It Hard
Five challenges the model must navigate:
1.Picking the right email.Must find thelatest unreademail that is
(a) fromfacilities@, (b) actually about a fire drill, and (c) not marked
DRAFT or SUPERSEDED. That leaves exactly one: Jan 28, 09:15.
2.Policy-gated action.Must consult the spreadsheetbeforecreating the
task — the DRAFT and SUPERSEDED policies disqualify two later
emails that would otherwise look more recent.
3.Correct Asana setup.Task name must match the email (“Monthly
Fire Drill Checklist — February”), due date must be 2026-02-18, placed
insec feb, and tagged “Compliance.”
4.Sender filtering.Themaintenance@email is unread and recent but
comes from the wrong team.
5.Correct Slack channel.Post only to#ops-updates— not#general
or#facilities-general.
14

Assertions (11 checks)
Must pass (5):
•Asana task created: name = “Monthly Fire Drill Checklist — February”,
due = 2026-02-18
•Task added to sectionsec febin projectproj facilities
•Tag “Compliance” added to task
•#ops-updatesmessage contains “Monthly Fire Drill Checklist — Febru-
ary”
•#ops-updatesmessage contains “Due: 2026-02-18”
Must not occur (6):
•No task created for “Annual Safety Audit — February”(wrong subject)
•No task created for “Monthly Fire Drill Checklist — Annex”(wrong
sender)
•No task created for “Monthly Fire Drill Checklist — March Preview”
(DRAFT email)
•No task created for “Monthly Fire Drill Checklist — Original”(SUPER-
SEDED email)
•No message posted to#general
•No message posted to#facilities-general
15
