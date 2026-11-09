---
title: 'Driving Epidemic Models with AI Agents: the Epydemix Agent Framework'
url: https://arxiv.org/abs/2609.28692
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Nicolò Gozzi
- Ciro Cattuto
- Alessandro Vespignani
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28692
pages: 40
chars: 88114
fetched_at: '2026-11-08T13:33:48+00:00'
kb_version: 1
---

# Driving Epidemic Models with AI Agents: the Epydemix Agent Framework

Driving Epidemic Models with AI Agents: the Epydemix Agent
Framework
Nicolò Gozzi 1,2, Ciro Cattuto 1*, Alessandro Vespignani 2,1
1 ISI Foundation, Turin, Italy
2 Network Science Institute, Northeastern University, Boston, MA, USA
*Corresponding author: Ciro Cattuto, ciro.cattuto@isi.it
Abstract
Artificial Intelligence agents based on large language models provide convenient natural language
interfaces to scientific software, but reliability is not automatic. Here we introduce the Epydemix
Agent Framework, an additive layer over Epydemix, an open-source Python library for stochas-
tic compartmental epidemic modeling. The framework extends the library with four capabilities
to facilitate interaction with an AI agent: discovery of available models and parameters, preven-
tive validation of a declarative scenario specification, execution through tested library code, and
inspectability of results. These capabilities let an agent handle the entire modeling process, from
the natural-language description of the scenario to quantitative results, figures, and interpretation
of findings without writing custom code. Each step reads input files and saves results in a sepa-
rate output bundle, making the process auditable and reproducible. First, we show the end-to-end
workflow with a case study comparing vaccination strategies for a novel respiratory virus. Second,
we assessed the framework across50agent sessions and five modeling tasks by comparing the agent
use of the framework against the direct use of the Python interface. The framework reduced turns,
output tokens, and cost on most tasks, unless it trades resources for per-point reproducibility.
1 Introduction
Dynamic transmission models are widely used to simulate disease spread and to evaluate public health
interventions [1–4]. Realistic models simulate stochastic dynamics in age-structured populations, with
contact matrices, and include interventions as changes in dynamics over time. Several infectious disease
modeling tools exist as software libraries that expose programming interfaces, but their use requires
programming expertise. Graphical user interfaces remove this requirement but constrain what a user
can specify and simulate. The rise of Artificial Intelligence (AI) agents based on large language models
1
arXiv:2609.28692v2  [cs.AI]  21 Oct 2026

(LLMs) offers a third mode of interaction, in which a researcher describes a task in natural language and
an agent operates the software [5, 6]. Current AI agents can translate natural-language task descriptions
into sequences of operations performed via software tools [7]. As a result, they are now increasingly used
to write code, perform analyses, and coordinate workflows. In epidemic modeling, AI agents allow a
researcher to specify a scenario, configure a model, compare interventions, and interpret results without
writing code for each analysis. Agents with such capabilities include Anthropic’s Claude Code [8],
OpenAI’s Codex CLI [9], and open-source alternatives [10].
Epydemix [11] is an open-source Python package for the development, simulation, and calibration
of stochastic compartmental epidemic models. As with most scientific libraries, this package was not
designed for text-mediated interaction. Instead, Epydemix was developed for scripts and computational
notebooks, where configurations, model states, and results persist in memory as objects across function
calls. An AI agent cannot reliably preserve such objects between tool calls. It has no way to discover
library functionalities (e.g., available models and parameters) without reading source code or documen-
tation. Similarly, an agent cannot extract summary measures such as attack rates from a binary output
without writing custom code. Finally, sources of error may come from the agent itself. Indeed, it may
specify parameter values that appear plausible but are invalid or reference functions and parameters
that are not supported. These failure modes can have serious consequences in epidemic modeling, where
outputs are used to compare interventions and mitigation strategies and can ultimately inform actions.
More generally, the reliable use of a modeling library from an AI agent requires four capabilities
that a Python application programming interface (API) does not provide by default. The first one is
discoverability: programmatic access to available models and parameters, without requiring the agent to
read source code or documentation. The second isdeclarative specification: a self-contained description
of a scenario that can be validated before execution. The third isreliable and reproducible execution:
running validated scenario configurations through calls to tested library code rather than through custom
code the agent writes for the task. The last capability isinspectability: compact textual summaries of
simulation outputs, allowing the agent to obtain the quantities it needs without parsing raw outputs.
These capabilities also support researchers’ work. For instance, a declarative configuration can be in-
spected, edited, versioned, and shared. This also addresses a documented challenge of the field. A recent
audit could reproduce only a small fraction of sampled COVID-era modeling studies [12, 13], and several
omissions were identified in reproducibility checklists [14].
In this paper, we introduce the Epydemix Agent Framework. The framework implements the four
capabilities described above as an additive layer on top of the existing Epydemix Python API. This
approach leaves the library and all existing notebooks and scripts unchanged. Its interface is stateless
and file-based, so that each operation is a pure function of its input files. We demonstrate the end-to-end
workflow with a case study comparing four intervention strategies for a novel respiratory virus, and we
2

assess the framework across more than50agent sessions.
2 Materials and methods
We use the term AI agent to refer to a system built around an LLM that operates external software
through tool calling. A task is described to the agent through a natural language prompt [15]. It then
proceeds iteratively, selecting an operation, reading the returned result, and determining the next step
until the task is complete [16]. The key property is that agents interact with software libraries entirely
through text. The available functions, their arguments, and outputs must all be expressed as text and
fit within the agents’ context window.
2.1 The Epydemix library
Epydemix is an open-source Python package that supports the development and calibration of dynamic
transmission models with any compartmental structure and dynamic public health interventions [11]. To
allow simulations with realistic demographic and mixing patterns, a companion repository including age-
stratified distributions and social contact matrices is available [17]. The package adopts a discrete-chain
binomial process simulation engine and supports the full modeling pipeline, from model specification
and simulation to parameter inference, forecasting, and scenario projection. The epidemic model is built
as an object, with compartments and transitions added through method calls, and results returned as
in-memory objects.
2.2 The Epydemix Agent Framework
After being prompted with a natural-language scenario description, the agent framework proceeds
through a four-phase workflow (Fig. 1). During theDiscoverphase, the agent identifies the available
models and retrieves default parameter values drawn from the literature for the disease of interest. Dur-
ingDeclare, the scenario is encoded in a configuration file (in YAML format) and validated against the
parameter registry. Nothing is computed until validation passes. DuringRun, the framework executes
the simulation, calibration, or projection and writes the results to a self-contained output bundle. During
Inspect, the agent queries the output bundle for compact structured summaries and compares outcomes
across scenarios. The current implementation uses the YAML format, but the design is not tied to any
particular structured text format.
Six components implement this workflow on top of the existing Epydemix Python API (Fig. 2). Three
are on-disk artifacts the framework reads, writes, and inspects: the parameter registry, the declarative
configuration files, and the output bundles. Two are the elements that operate on those artifacts, namely
the command-line interface (CLI) and the inspection engine. The sixth, the agent contract, documents
3

1 2 3 4
Discover
What models
and parameters
exist?
Declare
Write a conﬁg,
validate before
spending compute
Run
Simulate, calibrate,
project. Bundled
outputs on disk
Inspect
Compact JSON
answers. Compare
scenarios
Natural language
scenario
Quantitative
results + ﬁgures
→ .epx bundle
Discovery & planning Compute & analysis
Figure 1:Canonical four-phase workflow of the Epydemix Agent Framework.Starting from
a natural-language scenario description, an AI agent progresses through four sequential phases: (1)
Discover: enumerate available models and retrieve literature-sourced parameter defaults; (2)Declare:
encode the scenario as a YAML configuration file and validate it against the parameter registry before any
computation; (3)Run: execute simulation, calibration, or projection, writing results to a self-contained
.epxoutput bundle; (4)Inspect: query the bundle for compact, structured summaries and compare
outcomes across scenarios. The framework is stateless: each phase operates exclusively on files, with no
Python objects persisting across calls.
the framework in a form the agent can read and understand its use.
Parameter registry.Each model built from one of the predefined base models (SIR, SEIR, SIS
and SEIAR), together with any optional module layered on it (waning immunity, vaccination, clinical
outcomes), carries a machine-readable registry of its parameters. For every parameter the registry records
its name and a natural-language description of its role in the dynamics, its kind (rate, probability,
count, duration, proportion or dimensionless), data type and expected shape (scalar, time-varying, age-
structured), its units, admissible range and default value, whether it is required, and other parameters
it depends on. An agent can therefore discover what a model accepts without reading its source code.
Declarative configuration.A scenario configuration is a single, short YAML file that documents
the model, the population (i.e., age distribution and contact matrices), the simulation time window,
and the parameter values. The same file is the input to every downstream component. Configurations
inherit through overlays, meaning that a scenario can import a base configuration and override only the
selected fields. A comparison of four intervention strategies therefore translates into four short overlays
on one single base file, which keeps the differences between them explicit. Configuration files can be
automatically validated for correctness, so that, e.g., out-of-range values and inconsistent settings are
detected before spending compute time.
Configuration-driven CLI.The agent controls the workflow via a command-line interface (CLI)
tool (epydemix). The CLI exposes each step of the workflow through dedicated sub-commands:models,
schema,defaults,validate,run,calibrate,project,inspect, andcompare. Each subcommand
4

reads its inputs from files and writes standardized output into structured JSON. No state is carried
between calls, so that every invocation is a pure function of its input files, and an agent or an automated
pipeline can drive the workflow without a persistent Python session. We adopted statelessness because
an agent cannot reliably hold Python objects across tool calls, while also letting a human script the same
commands.
Output bundles.Everyrun,calibrate, andprojectoperation returns its output in a standard-
ized bundle enclosed within an.epxdirectory. The bundle contains simulation trajectories as Parquet
files, posterior parameter samples for calibration runs, generated figures, and amanifest.jsonfile
recording the simulation metadata and source configuration. Each bundle also records its parent config-
uration and any upstream bundles it derives from. The provenance of a derived result can therefore be
reconstructed from the filesystem alone, without the need for an external log.
Inspection engine.The inspection engine supplies the summarization logic behind theinspect
andcomparesub-commands. It converts the bundle’s Parquet contents into compact JSON rather
than returning raw arrays, reporting summary statistics of trajectories such as quantiles, peak timing
and magnitude, attack rates, and pairwise differences between bundles. The agent thus obtains the
quantities needed for the analysis of the simulations within its context window.
Agent contract.The document an agent reads first is the contractAGENT.md. The file describes
the four-phase workflow, the configuration format with annotations for each field, the command-line
interface with its CLI subcommands, and the exact structure of the JSON output. The contract also
contains a set of worked-out examples. The first version of the contract was produced by having an
agent inspecting the Epydemix source code, documentation, and the CLI built on top of it. The contract
has then been refined iteratively by running the framework on an informal set of tasks, including the
examples distributed with the library, and then using a second agent to review the execution logs and
identify sources of friction. The revisions include a catalog of failure modes observed during development
together with their corrections, and a translation guide mapping natural-language disease descriptions
onto Epydemix compartments and transitions. The guide addresses the hardest step of theDeclare
phase, where the model structure must be fixed before assigning any parameter values.
The declarative configuration format covers common compartmental modeling workflows but not
the whole Epydemix API functionality. For example, a YAML configuration cannot express custom
transition functions, non-standard age-group structures, or post hoc result transformations. Since the
framework leaves the Epydemix API untouched, such functionalities remain available through direct API
interaction, though they do not inherit the validation, provenance, and reproducibility of the structured
interface. Indeed, the contract instructs the agent to use the CLI by default and to fall back on direct
API calls only when an operation cannot be expressed declaratively.
The Epydemix agent framework is open source and available athttps://github.com/epistorm/
5

Parameter registry
machine-readable metadata,
valid ranges, and units;
literature-sourced defaults;
JSON Schema export
Declarative
configuration
single ∼20-line YAML scenario;
model, population, parameters;
inheritance with overlays
Output bundles
self-contained Parquet trajectories,
posterior samples, manifest,
and figures; records its parent
Command-line interface (CLI)
One command surface for agent and human.
Subcommands models, schema, defaults, validate, run,
calibrate, project. Each reads its inputs from files and
returns structured JSON on standard output; every call
is a pure function of its input files.
Inspection engine
behind the inspect and compare
subcommands: quantiles,
peaks, attack rates, deltas
Agent contract (AGENT.md)
workflow · annotated configuration format · CLI command & output shapes · worked examples
Figure 2:The components of the Epydemix Agent Framework.The agent contract (AGENT.md,
top) is the document an agent reads first. The command-line interface (middle) is the single control
surface for both an AI agent and a human researcher, and the inspection engine is part of it. The three
data components (bottom) are the filesystem-backed artifacts that the framework reads and writes. The
agent contract and tooling create a layer over the existing Epydemix Python API without modifying it.
epydemix, under the same GPL-3.0 license as the core library.
2.3 Experimental setup
Software and installation.All agent sessions used Claude Code from the terminal (version v2.1.198)
with Claude Sonnet 5 as the underlying model, running under a Claude Pro subscription. We used
version 1.3.1 of Epydemix and version 1 of the agent framework (commit hash 55d4e33). Sessions were
run on July1st,2026. The framework and its dependencies can be installed from a terminal via
git clone https://github.com/epistorm/epydemix.git
cd epydemix
pip install -e ".[agent]"
We recommend the installation inside a dedicated virtual environment, for example viavenvor
conda. This installs theepydemixcommand-line interface together with the agent contract. If the
epydemixexecutable is not discoverable onPATHafter installation, the CLI can equivalently be invoked
aspython3 -m epydemix.cli.mainfrom the repository root. The framework requires that the agent
can read local files and issue shell commands, and that it is invoked from the repository root so that
AGENT.mdis discoverable. A complete walkthrough for reproducing the case study, including installation,
agent setup, and troubleshooting, is provided in the Supplementary Information (SI Guide S4).
Comparison conditions.We run experiments considering two different conditions. In theframe-
6

workcondition, the agent has access to the Epydemix CLI and to the agent contract, and is directed
to follow the four-phase workflow described above. In thedirect APIcondition, the agent receives the
same repository with all references to the CLI and the agent contract removed, and works through the
Epydemix Python API directly with the library documentation and examples available. The direct API
condition is therefore not in complete absence of tooling, but mimics the setup faced by a researcher using
a well-documented library with a coding agent, without any additional layer mediating the interaction.
Multi-task evaluation.Our main assessment covers five epidemiological modeling tasks: an
SEIRHD scenario comparison, an SIR calibration, a concatenated calibrate-then-project workflow, a
school-closure sweep, and a measles coverage sweep. Each task was repeated five times in each of the two
conditions, giving50agent sessions in total. All sessions started from identical initial conditions, and a
session could not access artifacts produced by another one. For each session, we extracted performance
metrics from the agent’s runtime system, namely wall-clock time, time spent in model requests, number
of turns, number of output tokens, and cost. Task definitions and per-session values are given in the
Supplementary Information (SI Additional Tasks S5).
Case study comparison.We additionally ran the vaccination case study of Section 3.1 four times
in each condition, giving eight further sessions. Each of these was split into two phases to separate agent
exploration from execution. In the first phase, the agent operated inplanmode, reading the available
context as well as the user’s prompt and producing an inspectable plan. This phase was read-only, since
tools that could modify state were unavailable. In this phase, no configuration files were written, and no
simulations were run. In the second phase, the agent operated inexecutemode and carried out the plan
step by step. The split allows the cost and runtime of exploratory reading and reasoning to be attributed
separately from those of the analysis itself.
Metrics and statistics.For each task and metric of the multi-task evaluation, we report the ratio
of the median in the framework condition to the median in the direct API condition, so that values
below one indicate lower resource use with the framework. Distribution-free confidence intervals for
the ratio are obtained using the Wilcoxon rank-sum statistic. With five observations per condition, the
attainable exact coverage is96.8%, which is the level we report throughout. Intervals are computed per
task and metric, without correction for multiple comparisons. For the case study comparison, we report
the coefficient of variation across the four runs of each condition. We report the planning and execution
phases separately. Costs are reported in US dollars as billed by the model provider at the time of the
sessions. The cost should not be interpreted as a stable estimate and is given just to compare between
conditions.
7

3 Results
3.1 Case study: vaccination scenarios
To illustrate the end-to-end workflow, we tasked an AI agent to compare vaccination strategies for
a simulated epidemic. The study considered a novel respiratory virus spreading in Italy in a fully
susceptible population. The disease assumptions include a basic reproduction numberR0 ≈2.5, a mean
latent period of3days, and a mean infectious period of5days. We also assumed that, on average,0.8%
of infections led to hospitalization, with a mean hospital stay of10days, and that an available vaccine
reduced susceptibility to infection by85%. The simulations covered16months and used55,000beds as
the national hospital-capacity threshold. The agent was instructed to include a no-vaccination baseline.
Instructions on vaccination rates and the timing and magnitude of the non-pharmaceutical intervention
in the combined strategy were left qualitative. This lack of detail is meant to test whether the agent can
translate informal descriptions into internally consistent parameter values. The agent’s input consists of
the contract and the verbatim prompt below:
Prompt given verbatim to the agent
Read AGENT.md first, then carry out the following study end-to-end using the epydemix CLI. Work through
the discover→declare→run→inspect workflow, use a shared base configuration with overlays for the
scenarios, and validate every config before running it.
Scenario.A novel respiratory virus is spreading in Italy in a fully susceptible population. Epidemiological
assumptions: basic reproduction number R0 ≈2.5, mean latent period≈3 days, mean infectious period≈5
days. About 0.8% of infected individuals are hospitalized, with a mean hospital stay of≈10 days. A vaccine
is available that reduces transmission by≈85%. Italy can dedicate≈55,000 hospital beds to this epidemic;
sustained occupancy above that line means the health system is overwhelmed. Use a real Italian population
with age-structured contact matrices (home, work, school, community) and simulate a 16-month horizon.
Important:derive thetransmission_ratefrom the target R 0 using the population’s contact structure —
do not use a preset transmission rate directly, since the contact matrix rescales it. Model hospitalization as
a disease outcome and include a vaccination compartment.
Compare four strategies:
1.No vaccination — the uncontrolled baseline.
2.Slow rollout — a low constant per-capita vaccination rate.
3.Rapid rollout — a high constant per-capita vaccination rate.
4.Combined — a moderate vaccination rate plus temporary non-pharmaceutical interventions (reduced
school and workplace contacts for a few months during the wave).
For each strategy report: peak hospital occupancy, the peak date, the number of days occupancy exceeds the
8

55,000-bed capacity, and the total attack rate with deltas against the no-vaccination baseline. Then produce
a single comparison figure showing hospital occupancy over time for all four strategies with the capacity line
marked, and write a short interpretation: which strategies keep the system under capacity, and what the
comparison implies for rollout speed versus combining measures.
We ran four instances of this study in the framework condition (Section 2.3). The agent made
the same key modeling choices in all four instances. It selected an SEIR model with vaccination and
hospitalization compartments and used the CLI’sschemacommand to confirm that the model contained
the compartments required by the scenarios. The transmission rate corresponding to the targetR0 was
derived considering the spectral radius of Italy’s combined contact matrix (ρ≈13.90) instead of using
a preset value. In every instance, the agent determined that the built-in attack-rate metric does not
apply to a leaky-vaccine model and computed the attack rate instead from the sum of the susceptible-
to-exposed and vaccinated-to-exposed transition flows, following the guidance in the contract. For the
Combinedscenario, it ran the baseline first to locate the epidemic peak, then placed the temporary
contact-reduction window around it. As expected, the four runs diverged on quantities and choices the
prompt left unspecified. For instance, each time the agent assigned different values for the per-capita
vaccination rates, though their ordering across strategies was always preserved (Slow rollout<Combined
<Rapid rollout). The agent also used different numbers of stochastic realizations, simulation start date,
and duration/magnitude of contact reduction in theCombinedscenario.
Figure 3 shows the hospital-occupancy trajectories, and the box below reproduces the agent’s final
report verbatim for one of the instances. The Supplementary Information (SI Plan S1) includes the
agent’s plan, along with the layout, schema, and column-naming conventions of the underlying output
bundle (SI Bundle S2). In this run, the no-vaccination baseline exceeded hospital capacity for33days
and peaked at roughly95,000occupied beds.Slow rolloutlowered the peak by about13,500beds but
still breached capacity for29days.Rapid rolloutheld peak occupancy below3,500beds and the attack
rate below6%. TheCombinedstrategy, at half the vaccination rate ofRapid rollout, also stayed below
capacity, but its attack rate was26.3%. That higher attack rate reflects transmission resuming after
lifting the contact-reduction intervention, while vaccination continued at the lower rate.
Agent output
Study complete
Setup:SEIR +vaccination+outcome: hospitalizationmodules on Italy’s real age-structured popu-
lation (59.4M, 4 contact layers).transmission_rate = 0.0359742derived fromR 0 = 2.5via the contact
matrix’s spectral radius (ρ≈13.899) rather than guessed. Sharedbase.yaml+ one overlay per scenario, all
validated before running. Bundles and configs live initaly_study/(repo root).
9

Results (deltas vs. no-vaccination baseline, Hospitalized_total, 55,000-bed capacity)
Metric No vaccination Slow rollout Rapid rollout Combined
(baseline) (0.001/day) (0.01/day) (0.005/day + NPIs)
Peak occupancy 94,781 81,309 3,183 15,299
(−13,472) (−91,598) (−79,482)
Peak date 2024-04-10 2024-04-14 2024-05-08 2024-04-26
(+4d) (+28d) (+16d)
Days over capacity 33 29 (−4) 0 (−33) 0 (−33)
Attack rate 80.4% 72.7% (−7.7 pp) 5.6% (−74.7 pp) 26.3% (−54.1 pp)
Combined scenario: rate 0.005/day + 70% school / 30% work contact reduction, 2024-03-20 to 2024-05-15.
Figure
italy_study/no_vax.epx/figures/hospital_capacity_comparison.png(also registered in that bundle’s
manifest).
Interpretation
Only rapid rollout and the combined strategy keep the system under the 55,000-bed line — slow rollout
still overwhelms capacity for 29 days, barely better than doing nothing. Rollout speed dominates: rapid
vaccination alone (0.01/day, no NPIs) beats the combined strategy on every metric despite the combined
scenario using a lower vaccination rate plus temporary contact reductions — vaccinating fast enough to
blunt the wave before it peaks is worth more than a moderate rate plus a few months of partial school/work
closures. The practical takeaway: if achievable, invest in rollout speed first; temporary NPIs are a useful
hedge when rapid rollout capacity doesn’t exist (moderate rate + NPIs still avoids capacity breach and cuts
attack rate by more than half), but they are a substitute for speed, not a superior complement to it, given
the specific rates and reduction assumptions used here.
It is worth stressing that the figures in the agent’s report carry more digits than the assumptions
support. For instance, the derived transmission rate is reported to seven significant figures. For the sake
of reproducing the agent results, we decided to report the verbatim output.
3.2 Framework and direct API use compared
3.2.1 The vaccination case study
We first compare the two agent conditions, framework and direct API use, in the vaccination case study
where the two-phase design separates exploration from execution, as presented in Section 3.1. The
two conditions reached similar qualitative epidemiological conclusions. In both conditions, the agent
identified rollout speed as the main factor associated with outcomes, and used the same strategies to
10

Figure 3:Hospital occupancy over the 16-month simulation horizonunder the four vaccination
strategies, for the representative framework run reported in Section 3.1, with the55,000-bed capacity
threshold marked (dashed red line). Solid lines show the median across 100 stochastic simulations; shaded
bands show the90%interval.
keep hospital occupancy below capacity. A detailed comparison of results and agent choices is given in
the Supplementary Information (SI Comparison S3). The mean total cost was $2.98 in the framework
condition and $4.89 in the direct API condition, a64%increase. Mean total runtime was582s with
the framework and835s without, an increase of43%(Fig. 4). These totals are split between planning
and execution. In the framework condition, the mean cost was divided48%to planning and52%to
execution, on average. In the direct API condition, the shares were56%for planning and44%for
execution. Runtime separated the conditions more sharply, with planning taking41%of total time
under the framework and60%without it. The plan-mode transcripts show why. Agents in the direct
API condition spent much of the planning phase reading the Epydemix source code for information that
theAGENT.mdcontract provides to the framework condition.
The framework condition also shows lower Run-to-run variation (Table 1). For cost, the coefficient
of variation was0.10during planning and0.15during execution, against0.19and0.35in the direct API
condition. For runtime, the corresponding values were0.15and0.17against0.30and0.40.
Metric (CV = std/mean) Phase Framework Direct API
Total cost Planning 0.100.19 Execution 0.150.35
Total duration Planning 0.150.30 Execution 0.170.40
Table 1: Coefficient of variation across the four case-study runs of each condition, for cost (USD)
and running time (seconds), broken down by planning-phase and execution-phase values. Lower values
indicate greater run-to-run consistency. The higher, less consistent value in each row is shown in bold.
11

Figure 4:Compute-budget distribution across the eight case-study runs.Top (A): total cost
per run in USD, stacked by phase (solid: planning; hatched: execution), colored by condition (green:
framework, run1–run4; orange: direct API, run5–run8). Bottom (B): wall-clock running time per run
in seconds, stacked in the same way. The rightmost bar in each condition group shows the across-run
average, with error bars giving±1standard deviation for each phase and the percentage of the total
contributed by planning and execution annotated alongside.
3.2.2 Additional modeling tasks
To provide a more thorough analysis, we ran the comparison between agent conditions across five addi-
tional modeling tasks, with five runs per task in each condition. Across tasks, the framework generally
reduced the computing resources the agent used (Table 2). TheCalibrate→Projecttask shows the
largest difference, with the framework condition completing the task in0.53×the wall-clock time,0.45×
the output tokens, and0.52×the cost, with the confidence interval excluding parity on every metric.SIR
calibrationandMeasles coverage sweeptasks show the same pattern. This suggests that a structured
interface and an explicit contract remove much of the exploratory work. The agent spends fewer turns
discovering how to set up and run a model and generates less text.
The comparison between the two operating conditions of the agent is, however, strongly task-
dependent. Interestingly, theSchool-closure sweeptask reverses the pattern. For this task, the framework
condition requires1.41×the API time,1.32×the output tokens, and1.81×the cost relative to the di-
rect API condition. The origin of this reversal can be traced back to the artifacts the agent produced.
12

Task Wall clock time (s) Time in API (s) # Turns # Output tokens Cost ($)
SEIRHD scenarios 1.05 [0.85, 4.78] 0.98 [0.73, 5.14] 0.77 [0.60, 0.96] 0.79 [0.68, 0.91] 0.91 [0.81, 1.04]
SIR calibration 0.73 [0.59, 0.95] 0.57 [0.53, 0.70] 0.62 [0.55, 0.72] 0.58 [0.49, 0.67] 0.71 [0.65, 0.95]
Calibrate→Project 0.53 [0.45, 0.57] 0.50 [0.43, 0.55] 0.63 [0.53, 0.70] 0.45 [0.37, 0.45] 0.52 [0.49, 0.73]
School-closure sweep 2.04 [1.24, 3.27] 1.41 [1.25, 2.24] 1.38 [1.00, 2.21] 1.32 [1.18, 2.23] 1.81 [1.34, 3.34]
Measles coverage sweep 0.81 [0.42, 1.12] 0.83 [0.62, 0.93] 0.80 [0.68, 0.89] 0.71 [0.62, 0.93] 0.88 [0.67, 1.05]
Table 2: Framework performance relative to direct use of the Epydemix Python API, by task. Each cell
reports the ratio of medians (framework/direct API) over5runs per condition, together with an exact
96.8%distribution-free confidence interval for the ratio (Wilcoxon rank-sum). Values below1indicate
lower resource use in the framework condition. Values in bold indicate ratios whose confidence interval
excludes1.
The task sweeps over18intervention start dates. The framework condition considers each sweep as an
independent run with its own configuration file and a self-describing bundle. In the direct API condition,
the same18sweeps run as a single Python loop that writes multiple output files. This implies that the
higher use of resources in the framework condition is not an efficiency loss. On the contrary, resources
are spent to have every step of the sweep recorded as an independent and auditable artifact, storing the
configuration that produced it, its outputs, a provenance record, and the random seed used for its gener-
ation. Re-executing a bundle’s stored configuration reproduces that point’s realizations, so the sweep is
reproducible point by point and not only in aggregate. The direct API sweep is not unreproducible per
se, but data preservation varies from run to run. In our testing across runs, it produced different result
schemas each time and retained raw per-point trajectories in only three cases out of five. In summary,
in this case the framework’s use of resources should be thought of as a trade-off for reproducibility and
not a performance regression.
4 Discussion
The Epydemix Agent Framework shows how an infectious disease modeling library can be reliably op-
erated by an AI agent through an additive interface. Across modeling tasks, agents working within
the framework generally used fewer turns, fewer output tokens, and less compute than agents working
directly with the Python API. In the vaccination case study, both working conditions reached the same
qualitative conclusions, but the framework condition was cheaper, faster, and more consistent from run
to run.
The framework is designed in a way that allows validation against the parameter registry before
the simulation begins. The specification stage catches invalid configurations, so users can correct them
before spending compute. This mechanism explains the shift from planning toward execution seen in
13

the case-study comparison (Section 3.2.1). The validated, self-contained configuration removes the need
to verify inputs through exploratory reading. TheSchool-closure sweeptask shows that the framework
condition could cost more than direct API use, because it ran18sweep points as independent bundles.
The extra cost pays off in the output’s properties rather than in a better result. Each point of the
sweep survives with its configuration, its seed, and its provenance, so the sweep is reproducible point
by point. In the direct API condition, that property held in just three out of five runs, and the output
schema differed in all five. This does not necessarily imply that the agent committed an error. However,
structured interfaces convert such properties (e.g., reproducibility) from a matter of the agent’s choices
into a matter of consistency of the interface. Whether the cost is worth paying depends on the specific
context.
Here we implemented library control using a text-based command-line interface (CLI) rather than,
for example, using a Model Context Protocol (MCP) server [18]. MCP standardizes tool discovery and
invocation through a client-server connection managed by the agent host, and the state of the server
needs to be managed. A CLI, instead, affords a stateless, file-based design: inputs and outputs can be
inspected and versioned, and the same commands run equally well for a human or an agent, with no
separate server process. If needed, nothing prevents the CLI from being exposed via an MCP server
later, without changing the workflow beneath it.
Our study has limitations stemming from the analysis of a single agentic coding tool and the limited
set of tasks used to test the framework. Moving from the demonstrations provided here to a systematic
evaluation of AI agent-driven modelling approaches will require community-defined benchmarks. In
particular, the definition of a representative set of infectious disease modeling tasks with specific measures
of correctness and reproducibility. Such a benchmark would turn potential failure modes documented in
the agent contract into measurable outcomes, allow different models and agent tooling to be compared on
the same tasks, and show which parts of this framework can be generalized beyond Epydemix. Whether
open-weight models perform comparably to closed ones [8–10] should be tested on a community-defined
benchmark.
As AI agents become a common way to operate scientific software, interfaces designed for them,
rather than for interactive programming sessions, can play a key role in making agent-driven epidemic
modeling efficient, auditable, and reproducible.
Acknowledgements
NG, CC and AV acknowledge partial support from the Lagrange Project of the ISI Foundation, funded
by CRT Foundation. AV acknowledges support from the cooperative agreement CDC-RFA-FT-23-0069
from the CDC’s Center for Forecasting and Outbreak Analytics. The findings and conclusions in this
14

studyarethoseoftheauthorsanddonotnecessarilyrepresenttheofficialpositionofthefundingagencies,
the CDC, or the U.S. Department of Health and Human Services of the United States.
Declaration of AI and AI-assisted technologies use
During the preparation of this work the author(s) used agent sessions in Claude Code from the ter-
minal (version v2.1.198) with Claude Sonnet 5 as the underlying model, running under a Claude Pro
subscription. We report verbatim prompt and output of one experiment. AI-assisted technologies were
utilized for proofreading, text editing, and structural formatting. Specifically, these tools were employed
to enhance grammatical clarity, improve readability, and align the text with the journal’s style guidelines.
All AI-generated suggestions were thoroughly reviewed and verified by the authors, who maintain full
responsibility for the final content.
Authors contributions
Competing interests
Authors declare no competing interests.
Data availability
The Epydemix Agent Framework is open-source software, released under the GPL-3.0 license, and is
available athttps://github.com/epistorm/epydemix. The agent contract (AGENT.md), CLI source
code, and documentation described in this paper are included in that repository. The full prompt and
agent output for the case study reported in Section 3 are reproduced verbatim in the main text; the
agent’s plan and a step-by-step guide to reproduce the case study from scratch are reported verbatim in
the Supplementary Information (SI Plan S1, SI Guide S4).
References
[1] Matt J Keeling and Pejman Rohani.Modeling infectious diseases in humans and animals. Princeton
university press, 2008.
[2] C Jessica E Metcalf, Dylan H Morris, and Sang Woo Park. Mathematical models to guide pandemic
response.Science, 369(6502):368–369, 2020.
[3] Chiara Poletto, Samuel V Scarpino, and Erik M Volz. Applications of predictive modelling early in
the COVID-19 epidemic.The Lancet Digital Health, 2(10):e498–e499, 2020.
15

[4] Eric T Lofgren, M Elizabeth Halloran, Caitlin M Rivers, John M Drake, Travis C Porco, Bryan
Lewis, Wan Yang, Alessandro Vespignani, Jeffrey Shaman, Joseph NS Eisenberg, et al. Mathemat-
ical models: A key tool for outbreak response.Proceedings of the National Academy of Sciences,
111(51):18095–18096, 2014.
[5] Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Petar Sirkovic, Artiom Myaskovsky,
Grzegorz Glowaty, Felix Weissenberger, Alessio Orlandi, Dan Popovici, Anil Palepu, Keran Rong,
Ryutaro Tanno, Khaled Saab, Fan Zhang, Jacob Blum, Andrew Carroll, Kavita Kulkarni, Ne-
nad Tomašev, Dina Zverinski, Ivor Rendulic, Elahe Vedadi, Florian Hasler, Luka Rimanic, Marina
Boia, Ivan Budiselic, Ben Feinstein, Mathias Bellaiche, Tom Sheffer, Jan Freyberg, Jeremy Rat-
cliff, Ottavia Bertolli, Katherine Chou, Avinatan Hassidim, Burak Gokturk, Amin Vahdat, Yuan
Guan, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R. D. Costa, José R. Penadés,
Gary Peltz, Yossi Matias, James Manyika, Demis Hassabis, Yunhan Xu, Pushmeet Kohli, Annal-
isa Pawlosky, Alan Karthikesalingam, and Vivek Natarajan. Accelerating scientific discovery with
co-scientist.Nature, 2026.
[6] Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak,
Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne Bergen, Carla P.
Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan Liu, Arjun Manrai, Deb-
ora Marks, Bharath Ramsundar, Le Song, Jimeng Sun, Jian Tang, Petar Veličković, Max Welling,
Linfeng Zhang, Connor W. Coley, Yoshua Bengio, and Marinka Zitnik. Scientific discovery in the
age of artificial intelligence.Nature, 620(7972):47–60, 2023.
[7] Chris Lu, Cong Lu, Robert Tjarko Lange, Yutaro Yamada, Shengran Hu, Jakob Foerster, David Ha,
and Jeff Clune. Towards end-to-end automation of ai research.Nature, 651(8107):914–919, 2026.
[8] Anthropic. Claude Code.https://www.anthropic.com/claude-code, 2025. Accessed: 2026-07-02.
[9] OpenAI. Codex CLI.https://github.com/openai/codex, 2025. Accessed: 2026-07-02.
[10] Anomaly. OpenCode: The open source AI coding agent.https://opencode.ai, 2025. Accessed:
2026-07-02.
[11] Nicolò Gozzi, Matteo Chinazzi, Jessica T Davis, Corrado Gioannini, Luca Rossi, Marco Ajelli,
Nicola Perra, and Alessandro Vespignani. Epydemix: An open-source Python package for epi-
demic modeling with integrated approximate Bayesian calibration.PLOS Computational Biology,
21(11):e1013735, 2025.
[12] Alec S. Henderson, Roslyn I. Hickson, Morgan Furlong, Emma S. McBryde, and Michael T. Meehan.
Reproducibility of COVID-era infectious disease models.Epidemics, 46:100743, 2024.
16

[13] Darya Pokutnaya, Bruce Childers, Alice E. Arcury-Quandt, Harry Hochheiser, and Willem G.
Van Panhuis. An implementation framework to improve the transparency and reproducibility of
computational models of infectious diseases.PLOS Computational Biology, 19(3):e1010856, 2023.
[14] Darya Pokutnaya, Willem G. Van Panhuis, Bruce Childers, Marquis S. Hawkins, Alice E. Arcury-
Quandt, Meghan Matlack, Kharlya Carpio, and Harry Hochheiser. Inter-rater reliability of the
infectious disease modeling reproducibility checklist (IDMRC) as applied to COVID-19 computa-
tional modeling research.BMC Infectious Diseases, 23:730, 2023.
[15] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach
themselves to use tools.Advances in neural information processing systems, 36:68539–68551, 2023.
[16] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.
ReAct: Synergizing reasoning and acting in language models.arXiv preprint arXiv:2210.03629,
2022.
[17] Epydemix Data: Demographic and contact data for epidemic modeling.https://github.com/
epistorm/epydemix-data, 2025. Accessed: May 2026.
[18] Anthropic. Introducing the Model Context Protocol.https://www.anthropic.com/news/model-
context-protocol, 2024. Accessed: 2026-07-02.
17

Supplementary Information
SI Plan S1: Agent plan (Claude Code, plan mode)
The following is the plan produced verbatim by the agent when invoked in plan mode, prior to any
execution.
Agent plan
Study: Novel Respiratory Virus in Italy — Vaccination Strategies
Context.
The user wants an end-to-endepydemixCLI study of a novel respiratory virus spreading in a fully susceptible
Italian population, comparing four vaccination/NPI strategies (no vaccination, slow rollout, rapid rollout,
combined rollout+NPIs) on hospital-capacity and attack-rate outcomes. The workflow must follow discover
→declare→run→inspect, use a shared base config with scenario overlays, validate every config before
running, and derivetransmission_ratefrom the targetR 0 via the population’s contact-matrix spectral
radius (not a preset value). Deliverable: a metrics table (deltas vs. no-vaccination baseline) and a single
comparison figure of hospital occupancy with the capacity line, plus a short written interpretation.
Discovery already performed (read-only, in this session):
•epydemix modelsconfirms SEIR is available; CLI binary lives at/opt/anaconda3/bin/epydemix(not
on default PATH — must prepend/opt/anaconda3/binor call by full path in every command).
•epydemix schema SEIR --vaccination --outcome hospitalizationconfirms the modular compo-
sition gives exactly the compartments/parameters needed:Susceptible, Exposed, Infected,
Recovered, Vaccinated, Hospitalized, paramstransmission_rate, incubation_rate, recove
ry_rate, vaccination_rate, vaccine_efficacy, hospitalization_rate, hospitalization_rec
overy_rate.vaccination_rateis a constant per-capita S→V rate (not a scheduled dose campaign)
— exactly matches “low/high constant per-capita vaccination rate” in the prompt.vaccine_efficac
yreduces breakthrough transmission (V→Exposed since backbone has E), matching “vaccine reduces
transmission by∼85%”.
•A throwaway config with this exact module combination +population: Italyvalidated successfully
(valid: true), confirming compartment naming (Susceptible/Exposed/Infected/Recovered/Vac
cinated/Hospitalized) forinitial_conditions.
•Computed Italy’s combined contact-matrix spectral radius directly (per the recipe in
AGENT.md“Parameter Discovery”):ρ≈13.8988, population total59,435,140across groups
[’0-4’,’5-19’,’20-49’,’50-64’,’65+’].transmission_rate=R0_target×recovery_rate/ρ=
2.5×0.2/13.8988≈0.035974.
18

Derived / assumed parameters.
Quantity Value Source
transmission_rate 0.035974derived from R 0=2.5, recov-
ery_rate=0.2, Italyρ≈13.8988
(computed above)
incubation_rate 0.3333331 / mean latent period (3 days)
recovery_rate 0.21 / mean infectious period (5 days)
hospitalization_rate 0.0080.8% of infected hospitalized
hospitalization_recovery_rate 0.11 / mean hospital stay (10 days)
vaccine_efficacy 0.8585% transmission reduction
Capacity line55000beds given
vaccination_rate(no vaccination)0.0baseline
vaccination_rate(slow rollout)0.001“low” constant per-capita rate (∼1/1000
day)
vaccination_rate(rapid rollout)0.01“high” constant per-capita rate (∼1/100
day)
vaccination_rate(combined)0.005“moderate”, between slow and rapid
NPI reduction (combined only) school 70%, work 30% temporary, 8 weeks during the wave
Simulation horizon:start_date:2024-01-01,end_date:2025-05-01(16 months),dt: 0.5.n_simulation
s:100per scenario (matchesAGENT.mdexample conventions; compartmental model at 5 age groups is cheap
regardless of the 59M population size).
Initial conditions (fraction mode, mirrors the Italy-population convention already used inAGENT.md’s SEIAR
example —∼100 people seeded in each of E and I):
Susceptible: 0.9999966350
Exposed: 0.0000016825
Infected: 0.0000016825
Recovered: 0.0
Vaccinated: 0.0
Hospitalized: 0.0
Directory layout.
Create under the repo (not scratch, since this is a real deliverable the user will want to keep and revisit):
epydemix/studies/italy_respiratory_virus/
configs/
base.yaml
19

scenario_no_vaccination.yaml
scenario_slow_rollout.yaml
scenario_rapid_rollout.yaml
scenario_combined.yaml
bundles/
no_vaccination.epx/
slow_rollout.epx/
rapid_rollout.epx/
combined.epx/
analyze.py # attack-rate + figure generation script
Steps.
1. Writeconfigs/base.yaml— shared model/population/simulation/initial_conditions:
model:
type: SEIR
vaccination: true
outcome: hospitalization
parameters:
transmission_rate: 0.035974
incubation_rate: 0.333333
recovery_rate: 0.2
vaccination_rate: 0.0
vaccine_efficacy: 0.85
hospitalization_rate: 0.008
hospitalization_recovery_rate: 0.1
population:
name: "Italy"
contact_layers: ["home", "work", "school", "community"]
simulation:
start_date: "2024-01-01"
end_date: "2025-05-01"
dt: 0.5
n_simulations: 100
initial_conditions:
Susceptible: 0.9999966350
Exposed: 0.0000016825
20

Infected: 0.0000016825
Recovered: 0.0
Vaccinated: 0.0
Hospitalized: 0.0
2. Write the three non-dependent overlays(each:base: base.yaml+ aparameters:key-merge
overriding onlyvaccination_rate):
•scenario_no_vaccination.yaml→vaccination_rate:0.0(explicit, self-documenting)
•scenario_slow_rollout.yaml→vaccination_rate:0.001
•scenario_rapid_rollout.yaml→vaccination_rate:0.01
3. Validate and run these three first(in dependency order —no_vaccinationmust run before we can
time the combined scenario’s NPI window):
epydemix validate configs/scenario_no_vaccination.yaml
epydemix run configs/scenario_no_vaccination.yaml -o bundles/no_vaccination.epx
epydemix validate configs/scenario_slow_rollout.yaml
epydemix run configs/scenario_slow_rollout.yaml -o bundles/slow_rollout.epx
epydemix validate configs/scenario_rapid_rollout.yaml
epydemix run configs/scenario_rapid_rollout.yaml -o bundles/rapid_rollout.epx
4. Determine the NPI window for the combined scenario:
epydemix inspect bundles/no_vaccination.epx peak -v Hospitalized_total
Set the intervention window to roughly 4 weeks before through 4 weeks after the median peak date (≈8
weeks total, “a few months during the wave”), clipped to stay within the simulation horizon.
5. Writescenario_combined.yaml:
base: base.yaml
parameters:
vaccination_rate: 0.005
interventions:
- layer: school
start_date: "<peak - 4w>"
end_date: "<peak + 4w>"
reduction: 0.7
- layer: work
start_date: "<peak - 4w>"
end_date: "<peak + 4w>"
21

reduction: 0.3
Validate and run:
epydemix validate configs/scenario_combined.yaml
epydemix run configs/scenario_combined.yaml -o bundles/combined.epx
6. Inspect / compare — built-in metrics(peak occupancy, peak date, days over capacity), with deltas
vs. the no-vaccination baseline:
epydemix compare bundles/no_vaccination.epx bundles/slow_rollout.epx \
bundles/rapid_rollout.epx bundles/combined.epx \
-n NoVaccination,SlowRollout,RapidRollout,Combined \
7. Attack rate — custom Python(perAGENT.md:attack_ratebuilt-in metric is wrong for vaccination
models; this is a leaky vaccine with a V→Exposed breakthrough transition, so bothS_to_E_totalandV_t
o_E_totalflows must be summed):
import pandas as pd
N = 59_435_140 # Italy total population, from population.total_population
for name, bundle in scenarios.items():
df = pd.read_parquet(f"{bundle}/transitions.parquet",
columns=["sim_id", "S_to_E_total", "V_to_E_total"])
attack = df.groupby("sim_id")[["S_to_E_total", "V_to_E_total"]].sum().sum(axis=1) / N *
100
# report median + 90% CI, and delta vs. no_vaccination median
Assemble a single summary table: peak occupancy, peak date, days over 55,000, attack rate — each as a
delta vs. no-vaccination baseline — for the three vaccinated scenarios (and absolute values for the baseline
itself).
8. Comparison figure(analyze.py, adaptingAGENT_EXAMPLES.mdRecipe 2 + Recipe 3): overlay median
Hospitalized_total(with a light 90% CI band) for all four scenarios,axhlineat 55,000 with a “Capacity
(55,000 beds)” label. Save tobundles/no_vaccination.epx/figures/hospital_capacity_comparison.pn
g, then register withadd_figure_to_manifest(...,description=...,variables=["Hospitalized_total"
]). Report the absolute figure path to the user.
9. Interpretation— short written summary (in chat, not a new file) covering: which strategies keep
median occupancy under 55,000 beds and for how long any exceed it; how peak occupancy and attack
rate scale with rollout speed (slow vs. rapid, holding NPIs fixed); and what the combined scenario’s delta
implies about moderate vaccination + temporary NPIs vs. vaccination speed alone (i.e., does combining
beat rapid-alone, and by how much, on peak occupancy / days-over-capacity / attack rate).
22

Verification.
•Every config passesepydemix validatewith"valid": truebefore it is run.
•After eachrun, confirm the bundle’smanifest.jsonlists the expected compartment columns (Susce
ptible_total,Exposed_total,Infected_total,Recovered_total,Vaccinated_total,Hospitalize
d_total) viaepydemix inspect <bundle> manifest.
•Sanity-check the no-vaccination baseline’s dynamics look like a single wave with total attack rate
broadly consistent with1−1/R 0-scale expectations for R0=2.5 (∼85–90% of an unmitigated fully-
susceptible population, tempered by the age-structured contact matrix) rather than something degen-
erate (e.g., near-0% or near-100% instantly), perAGENT.md’s warning to sanity-check dynamics after
derivingtransmission_rate.
•Confirmepydemix comparedeltas match hand-checked arithmetic for at least one metric.
•Open the saved PNG (or describe it) to confirm all four curves and the capacity line are visible and
legible before reporting completion.
SI Bundle S2: Structure of the.epxoutput bundle
Everyrun,calibrate, orprojectoperation writes a self-contained.epxdirectory. Listing 4 shows the
bundle produced for the no-vaccination baseline of the case study presented in the main text. The other
three scenario bundles follow an identical layout.
no_vaccination.epx/
manifest.json # metadata, file schema, provenance
config.yaml # the configuration that produced this bundle
compartments.parquet # compartment counts per simulation, date, age group
transitions.parquet # daily transition counts per simulation, date, age group
parameters.parquet # per-simulation parameter values
figures/
hospital_capacity_comparison.png
manifest.json. The manifest is a single JSON file recording everything needed to interpret the
bundle without opening the Parquet files: the Epydemix version, model type and compartment list, the
demographic groups used, the simulation window and number of stochastic realizations, the parameter
values used to produce the run, a per-file schema (column names, dtypes, and array shape) for each
Parquet file, usage hints for querying the bundle via the CLI or directly in Python, and a provenance
block recording the path to the exact configuration file that produced the bundle.
For the baseline scenario shown here:epydemix_version 1.3.1; modelSEIRwith compartments
23

Susceptible, Exposed, Infected, Recovered, Vaccinated, Hospitalized; 5 demographic groups
(0-4, 5-19, 20-49, 50-64, 65+); simulationwindow2024-01-01to2025-05-01(487dailytimesteps),
withn= 100stochastic simulations.
compartments.parquet. Onerowper(simulation, date)pair—100×487 = 48,700rowsforthisstudy
— indexed bysim_idanddate. For every compartment, the file stores one column per demographic
group plus an aggregate_totalcolumn, giving6compartments×6columns (5 age groups + total)
= 36data columns, plus the two index columns (38 columns total). Column naming follows the pattern
<Compartment>_<group>, e.g.Hospitalized_65+orHospitalized_total.
transitions.parquet. Same row structure and indexing ascompartments.parquet, but each col-
umn records thedaily flowbetween two compartments rather than a compartment’s standing count,
following the pattern<Source>_to_<Target>_<group>(e.g.Infected_to_Hospitalized_total,V
accinated_to_Exposed_totalfor vaccine-breakthrough infections). This is the file used to compute
derived quantities not natively exposed byinspectorcompare, such as the leaky-vaccine attack rate
reported in Section 3.1 (“Case study: vaccination scenarios”) of the main text, which sums theSuscept
ible_to_ExposedandVaccinated_to_Exposedflows over the simulation horizon.
parameters.parquet. Onerowpersimulation, recordingtheparametervaluesusedinthatstochastic
realization. For arunwith fixed parameters (as in this case study) the file carries only thesim_idindex,
since every simulation shares the same parameter values already recorded once inmanifest.json; for a
calibratebundle, this file instead carries one column per calibrated parameter, recording the accepted
posterior sample used in each simulation.
config.yaml. A verbatim copy of the declarative configuration that produced the bundle, duplicating
themodel,population,parameters,simulation, andinitial_conditionsblocks from the originating
scenariofile. Storingthiscopyinsidethebundle, ratherthanonlyreferencingthepathinmanifest.json,
makes the bundle self-contained: the exact configuration that produced a result travels with it even if
the original configuration file is later modified or deleted.
SI Comparison S3: With-framework vs. without-framework
This section reports run-by-run detail underlying the process and outcome comparisons in the main text,
using the four with-framework runs and four without-framework runs described in the main text.
Process comparison
Table S1 reports mean±std across the four runs of each condition, split by planning and execution
phase.
The without-framework condition is both slower and more expensive at every phase. The gap is
24

Phase Metric With framework Without framework
Planning Duration (s)240.2±33.0 504.0±168.0 Cost ($)1.43±0.17 2.73±0.60
Execution Duration (s)342.2±59.0 331.0±99.0 Cost ($)1.55±0.27 2.16±0.86
Total Duration (s)582.5±82.6 835.0±128.8 Cost ($)2.98±0.38 4.89±0.78
Table S1: Planning, execution, and total cost and duration, with-framework vs. without-framework
(n= 4per condition).
proportionallylargerindurationthanincost: planningtakesroughlytwiceaslongwithouttheframework
(240s vs.504s) but costs about1.9×as much ($1.43vs.$2.73), while execution duration is nearly
identical between conditions (342s vs.331s) despite execution cost still being∼40%higher without the
framework. This is consistent with the without-framework condition spending planning time reading
Epydemix’s source directly rather than a validated interface description, and then executing against a
less certain plan.
Content comparison
All eight runs converge on the same qualitative structure: no-vaccination and slow rollout both breach
the 55,000-bed capacity line for roughly a month, rapid rollout and combined both clear it in every run,
and rollout speed is the dominant lever when vaccination is the only intervention available.
Baseline.
No-vaccination peak occupancy is tightly clustered regardless of condition:94,755–99,079across all
eight runs (mean97,441±2,202).
Slow rollout.
Unlike rapid rollout, slow rollout shows no real cross-condition split (Table S2): mean peak occupancy
is within a few thousand beds between conditions (81,277vs.80,587), and every one of the eight runs,
in both conditions, still breaches the55,000-bed line for roughly a month. Slow rollout is the weakest
lever tested and is never sufficient to clear capacity on its own, in either condition.
Metric With framework Without framework
Peak occupancy (mean±std)81,277±4,279 80,587±6,843
Peak occupancy (range)78,223–87,318 73,630–87,849
Attack rate % (mean±std)72.5±2.3 71.6±4.1
Days over capacity 28–31 (all 4 runs) 26–31 (all 4 runs)
Table S2: Slow rollout outcomes, with-framework vs. without-framework.
25

Rapid rollout.
Every run in both conditions clears capacity (0 days over), but with markedly different variance
structure(TableS3). Without-frameworkrunsclustermoderatelyaroundahighermean; with-framework
runs are mostly very low but include one outlier (a single run that assumed a visibly more conservative
rate than its three siblings), which drives the wide with-framework standard deviation.
Metric With framework Without framework
Peak occupancy (mean±std)12,634±21,707 20,674±10,046
Peak occupancy (range)1,090–45,161 11,187–34,872
Attack rate % (mean±std)14.5±22.8 25.9±10.6
Days over capacity 0 (all 4 runs) 0 (all 4 runs)
Table S3: Rapid rollout outcomes, with-framework vs. without-framework.
Combined strategy.
Combined outcomes are more consistent than rapid rollout in both conditions, and clear capacity
in every run (Table S4). With-framework runs reach a lower mean peak and attack rate than without-
framework runs.
Metric With framework Without framework
Peak occupancy (mean±std)19,944±7,428 33,697±6,470
Attack rate % (mean±std)33.5±8.5 42.2±6.4
Days over capacity 0 (all 4 runs) 0 (all 4 runs)
Table S4: Combined strategy outcomes, with-framework vs. without-framework.
Assumed parameters.
The prompt specifies vaccination rates and NPI magnitudes only qualitatively (“low/moderate/high
constant per-capita rate”, “reduced school and workplace contacts for a few months”), so each run chose
its own numeric values (Table S5). Rapid-rollout rate means are essentially identical between conditions
(1.025%vs.1.028%/day); the outlier in Table S3 is a single with-framework run that picked0.50%/day
against a1.00–1.30%cluster from its three siblings, i.e. the same rate-ambiguity effect that in other
batches has shown up on the without-framework side. Slow-rollout rate means are closer between con-
ditions (0.115%vs.0.181%/day) than the outcome table above might suggest, and NPI magnitudes are
similar between conditions and less consequential for outcomes: the combined strategy clears capacity
in all eight runs regardless of the specific school/work reduction or window length chosen.
Caveats and summary
These are small samples (n= 4per condition), and a single differently-worded rate choice can flip a
whole condition’s headline outcome, as seen in the rapid-rollout outlier above. With-framework content
26

Parameter Condition Slow / school Rapid / work Combined / window
Vaccination rate (%/day) With framework0.115±0.015 1.025±0.327 0.425±0.075
Vaccination rate (%/day) Without framework0.181±0.064 1.028±0.357 0.464±0.097
NPI reduction (%) With framework62.5±13.0 47.5±10.9 82.0±15.0days
NPI reduction (%) Without framework55.0±5.0 38.8±7.4 85.0±8.7days
Table S5: Assumed vaccination rates (slow/rapid/combined) and NPI intervention magnitudes (school/-
work reduction, window length), mean±std across runs.
metrics were transcribed by hand from each run’s own result table, since the framework’s bundle format
has no single machine-readable summary file; without-framework metrics come directly from each run’s
results file.
The comparison does not change the picture in the main text: the without-framework condition
remains costlier and more planning-heavy, baseline dynamics converge tightly regardless of condition,
and unspecified vaccination-rate magnitudes remain the single largest source of cross-run disagreement
on whether rapid rollout alone suffices. Both conditions reach the same conclusion on which strategies
clear hospital capacity.
SI Guide S4: Step-by-step guide to reproduce the case study
Thissectionwalksthrough, commandbycommand, howtoreproducethevaccinationcasestudyreported
in the main text, starting from nothing but a terminal. No prior familiarity with Epydemix, the agent
framework, or Claude Code is assumed.
What you will need.
•A computer withPython3.9 or later andgitinstalled.
•A terminal (Terminal.app on macOS, PowerShell/WSL on Windows, or any terminal on Linux).
•An AI coding agent capable of reading local files and issuing shell commands. This guide uses
Claude Code, but the framework is agent-agnostic: any comparable terminal-based agent will work
the same way, since it interacts with Epydemix purely through the CLI andAGENT.md.
•An active subscription or API access for whichever agent you choose (e.g., a Claude account for
Claude Code).
Step 1 — Clone the repository and install the CLI.
Open a terminal and run:
git clone https://github.com/epistorm/epydemix.git
cd epydemix
27

pip install -e ".[agent]"
We recommend doing this inside a fresh virtual environment (python -m venv .venv && source
.venv/bin/activateon macOS/Linux, or thecondaequivalent) to avoid dependency conflicts with
other Python projects on your machine.
Step 2 — Verify the installation.
Confirm the CLI is working before involving an agent:
epydemix models
ThisshouldprintaJSONlistofavailablemodeltypes(e.g.SIR,SEIR,SIS).Iftheepydemixcommand
is not found even though installation succeeded, it may not be on your systemPATH; in that case, replace
epydemixwithpython3 -m epydemix.cli.mainin every command in this guide — the two forms are
equivalent.
Step 3 — Install and launch your AI agent.
Install Claude Code following Anthropic’s instructions for your platform, then launch itfrom the
repository root(theepydemixfolder created in Step 1):
claude
Launching from the repository root matters: it is what allows the agent to discoverAGENT.md, the
contract document thattells ithowto use theframework. Ifyouare using adifferent agent, the equivalent
step is simply to start it with the repository root as its working directory.
Step 4 — Give the agent the case-study prompt.
Copy the full prompt exactly as given in Section 3.1 of the main text and paste it as your first message
to the agent. Optionally, invoke the agent’s planning mode first (in Claude Code, this is a mode toggle
available before sending the message) to see its intended approach before it executes anything, as we did
in SI Plan S1.
Step 5 — Let the agent run.
The agent will work autonomously through the discover→declare→run→inspect workflow:
writing configuration files, validating them, launching simulations, and querying the results, without
further input from you. This typically takes several minutes, depending on the agent and simulation
settings. You do not need to do anything during this step, though you can watch the agent’s terminal
output to follow its progress.
28

Step 6 — Locate the outputs.
Once the agent finishes, it will report a summary directly in the chat and leave the full artifacts on
disk under the working directory it created, typically:
studies/italy_respiratory_virus/
configs/ # the YAML configuration files the agent wrote
bundles/ # one .epx output bundle per scenario (see SI Bundle S2)
analyze.py # the script that produced the comparison figure
The comparison figure itself sits inside the baseline bundle’sfigures/subfolder, e.g.bundles/no_v
accination.epx/figures/hospital_capacity_comparison.png.
Step 7 (optional) — Inspect the results yourself, without an agent.
Everything the agent did is also directly usable by a human from the same terminal. For example,
to see summary statistics for a single bundle:
epydemix inspect studies/italy_respiratory_virus/bundles/no_vaccination.epx summary -v
Hospitalized_total
or to compare two bundles directly:
epydemix compare studies/italy_respiratory_virus/bundles/no_vaccination.epx \
studies/italy_respiratory_virus/bundles/rapid_rollout.epx \
-m peak,peak_date -v Hospitalized_total
This is the same command-line surface the agent used throughout; nothing about the bundles or the
CLI is agent-specific, so any step in this guide can equally be carried out by hand.
Troubleshooting.
•epydemix: command not found.Usepython3 -m epydemix.cli.mainin place ofepydemix
throughout, as noted in Step 2.
•The agent cannot findAGENT.md.Confirm you launched the agent from inside the cloned
epydemixrepository root, not a subdirectory or an unrelated folder.
•Results differ slightly from those presented here.Two independent sources of variation are
expected. First, simulations are stochastic (Section 2, “Materials and methods”, of the main text),
so small numerical differences across runs of the same configuration are normal. Second, because
the prompt specifies rollout speed and intervention magnitude qualitatively rather than numerically
(Section 3.1 of the main text), a different agent run may choose somewhat different vaccination
rates, NPI timing or combination, or initial conditions than those reported here, provided they
29

remain internally consistent with the prompt’s intent. The qualitative pattern — rapid rollout and
the combined strategy avoiding capacity breach, slow rollout and no vaccination both breaching it
— should reproduce reliably even so.
SI Additional Tasks S5: Experiments with Additional Tasks
Setup
We compared two ways of driving Epydemix with a coding agent on a small set of5epidemiological
modeling tasks. We compared a “baseline” condition, in which the agent only has access to the library,
its documentation and its examples, against a “framework” condition in which the agent has access to
our framework. We ran each of the5tasks5times for each condition (2experimental conditions,5tasks,
5independent iterations) for a total of50agent sessions. Multiple iterations are necessary because the
behavior of agents is stochastic. The two conditions differ only in what we provide to the agent:
•Baseline condition:the Epydemix library from the GitHub repository with the agent framework
removed (noAGENT.mdcontract, no command-line interface, and no references to them), together
with its documentation and worked examples as Jupyter notebooks.
•Framework condition:the Epydemix library as above, plus the agent framework: theAGENT.md
contract and the framework tooling (command-line interface tool).
Agent harness
Each task was executed by a non-interactive Claude Code session driven by a purpose-built agent harness
and started by a single initial user prompt. No user interaction was possible. The settings of the session
are reported in the Table S6 below:
Setting Value
Agent runtime Claude Code 2.1.224, non-interactive
Modelclaude-sonnet-5
Reasoning effortmedium
Tools availableBash,Read,Write,Edit,
Glob,Grep,BashOutput,KillShell
Tools withheld sub-agents, task planning, web search and fetch
Local customization disabled (--safe-mode)
Prompt single initial user message
Table S6: Agent harness configuration.
30

The list of allowed tools was chosen so that both conditions have the capabilities required to carry out
the tasks (running shell commands and writing/executing custom Python code) but nothing that would
allow the agent to delegate or shortcut the work. Sub-agents and task-planning tools were withheld so
that the measured effort is that of a single agent. Web access was withheld so the agent could not consult
documentation outside of the Epydemix repository. The customization mechanism of Claude Code (e.g.,
skills, plugins, hooks, custom agents, external tool servers) were disabled using--safe-mode, so that
the local environment of the user could not influence the runs.
Isolation of task runs
Several measures were taken to isolate the task runs from one another:
•Workspace:Each session received a fresh workspace from the Epydemix library’s repository.
Results, scripts and transcripts from earlier runs could not reach an agent’s context.
•Environment:Each task run received its own Python virtual environment, with the same set
of data analysis packages together with the library’s own dependencies (numpy,pandas,scipy).
Plotting used a headless backend.
•Verification:Task run isolation was verified. Every filesystem path appearing in tool call was
checked, and any path outside of the execution workspace was flagged. Across the 50 sessions
reported here, no session violated the isolation constraint.
Execution and metrics
Tasks were run sequentially, with the two conditions (baseline vs framework) interleaved within each
iteration, so that both met comparable constraints of Claude Code (API load, rate-limit conditions,
etc.). Metrics were taken from the structured event stream emitted by the agent runtime: wall-clock
duration, time spent in model requests, the number of model turns, errors, and token usage decomposed
into input, output, cache-read and cache-creation counts. Overall, the50runs used 4.6 hours of agent
wall-clock time and∼84 million tokens.
Results: baseline vs framework
The table below reports the median value of the chosen execution metrics for each of the5tasks, for the
baseline condition and the framework condition.
31

Task Metric Baseline Framework
SEIRHD scenarios Wall clock time (s) 160[146, 177]169[142, 767]
Time in API calls (s) 146[126, 153]143[107, 748]
# Turns 30[24, 37]23[18, 26]
# Output tokens 12374[11 015, 14 188]9717[9 094, 10 909]
Cost ($) 0.785[0.698, 0.865]0.715[0.634, 0.774]
SIR calibration Wall clock time (s) 214[163, 237]156[126, 164]
Time in API calls (s) 146[126, 158]83[82, 95]
# Turns 39[37, 44]24[23, 28]
# Output tokens 12150[10 383, 13 471]7005[5 988, 7 668]
Cost ($) 0.892[0.673, 0.981]0.636[0.614, 0.709]
Calibrate→Project Wall clock time (s) 226[215, 263]119[114, 128]
Time in API calls (s) 197[193, 232]99[95, 108]
# Turns 43[40, 49]27[25, 30]
# Output tokens 17229[17 162, 20 693]7670[6 527, 7 806]
Cost ($) 1.308[0.929, 1.384]0.674[0.646, 0.708]
School-closure sweep Wall clock time (s) 292[226, 336]594[377, 860]
Time in API calls (s) 224[170, 231]314[281, 425]
# Turns 42[27, 45]58[42, 73]
# Output tokens 19970[11 806, 21 624]26312[23 695, 36 137]
Cost ($) 1.010[0.545, 1.115]1.824[1.358, 2.519]
Measles coverage sweep Wall clock time (s) 644[544, 1 012]519[346, 668]
Time in API calls (s) 372[337, 436]308[243, 344]
# Turns 45[42, 53]36[33, 40]
# Output tokens 33065[30 659, 37 857]23486[21 388, 30 821]
Cost ($) 1.560[1.312, 1.880]1.371[1.195, 1.487]
Table S7: Per-condition medians (5runs per cell) with the observed minimum–maximum range in square
brackets.Baselineis the bare Epydemix library, andFrameworkis the agent framework.
Task prompts
Each task prompt was assembled from three parts: a condition-specific orientation preamble, the task
body, and shared closing instructions. The preamble is the only part of the prompt that differs between
the two experimental arms. Task bodies are reported verbatim in the following section.
32

Preamble: Baseline condition (library only)
You are working inside the epydemix repository. epydemix is a Python library for compartmental
epidemic modeling. The library source is in`epydemix/`, the API documentation in`docs/`, worked
examples as Jupyter notebooks in`tutorials/`, and an overview in`README.md`. The package is already
installed in the active Python environment. Consult whatever you need, then carry out the following
task.
Preamble: Framework condition (agent framework)
Read AGENT.md at the repo root, then carry out the following task.
Closing instruction (identical in both conditions)
Work only inside your current working directory -- that is the repository root for this session. Do
not read or write anything outside it. Put every file you produce in a subdirectory called`outputs/`
(create it). When you are done, give a short summary of your results in your final message.
Task bodies
T1 (SEIRHD scenarios): Custom SEIRHD model, three intervention scenarios
MODEL:
Build a custom SEIRHD compartmental model for a respiratory pathogen in a population of 100,000:
S (Susceptible) -> E (Exposed) -> I (Infectious) -> H (Hospitalized) or R (Recovered) -> D (Dead, from
H) or R (Recovered, from H)
EPIDEMIOLOGY:
- Transmission through contact between S and I (community), and at a reduced rate between S and H
(nosocomial).
- Incubation period ~3 days (sigma = 0.33/day).
- Infectious period ~7 days (gamma = 0.14/day). At the end of it, 5% of cases are hospitalized, the
rest recover.
- Hospital stay ~10 days (gamma_hosp = 0.1/day). Among hospitalized, 15% die, the rest recover.
- Community transmission rate: beta = 0.45/day. Nosocomial transmission rate: beta_hosp = 0.05/day.
SCENARIOS:
Run three scenarios over 6 months (Sep 1, 2024 -> Mar 1, 2025), each with 200 simulations.
Seed the outbreak with a tiny fraction of exposed and infectious individuals.
- Baseline -- no intervention.
33

- Early intervention -- on October 1, 2024, transmission drops 40% (beta goes from 0.45 to 0.27) until
February 1, 2025.
- Late intervention -- same 40% reduction, but starting November 1, 2024 until February 1, 2025.
DELIVERABLES:
- Check that all three model setups are correct before running them.
- Run all three scenarios.
- Report, for each scenario, summary statistics and peak timing for I_total, H_total, D_total.
- Compute for each scenario: attack rate (%), peak hospital census (median + 90% CI), total deaths
(median + 90% CI),
days the hospital census exceeds 500 beds, lives saved vs. baseline.
- Produce three figures: epidemic curves (I_total), hospital capacity (H_total with a 500-bed line),
cumulative deaths (D_total) -- all as scenario overlays with uncertainty bands.
- Summarize: what does a 30-day delay in intervention cost?
T2 (SIR calibration): SIR calibration, posterior quality and two-parameter sensitivity
STEP 1: Generate synthetic observed data
Run a forward SIR simulation with these "true" parameters to produce synthetic outbreak data:
- Population: 100,000 (default flat population)
- transmission_rate: 0.35
- recovery_rate: 0.1
- Period: Jan 1 - Apr 30, 2024 (120 days)
- Initial conditions: S = 0.999, I = 0.001, R = 0.0
- 1 simulation (or take the median of a few)
Extract the daily Infected_total time-series from this run and save it as a CSV file (observed.csv
with
columns`date`and`cases`). This is the "observed data" we will calibrate against.
STEP 2: Calibrate transmission_rate
Set up a calibration that:
- Uses the same SIR model structure and recovery_rate = 0.1 (fixed).
- Defines a uniform prior on transmission_rate over [0.1, 0.8] -- deliberately wide, to test whether
the
calibration can recover the true value.
- Uses observed.csv as the observed data.
- Targets Infected_total as the comparison variable.
34

- Uses RMSE as the distance function.
- Uses the SMC strategy with 300 particles and 8 generations.
Define the base model setup once and reuse it for the calibration, so that the calibration only
specifies
what it adds on top. Check the calibration setup is correct, then run it.
STEP 3: Assess calibration quality
- Inspect the posterior: what is the estimated transmission_rate? Report mean, median, std, and 95%
CI.
How close is the posterior median to the true value of 0.35?
- Inspect the calibration fit: get the fit trajectories (quantiles 0.05, 0.5, 0.95 for Infected_total)
and
compare them to the observed data.
- Produce a figure with two panels:
- Left panel: posterior distribution of transmission_rate as a histogram, with a vertical line at
the
true value (0.35).
- Right panel: calibration fit -- observed data as black dots, median fit as a blue line, 90% CI as
a
shaded band.
STEP 4: Sensitivity -- calibrate both parameters
Now set up a second calibration (reusing the same base model setup) that calibrates both
transmission_rate and recovery_rate:
- transmission_rate: uniform prior [0.1, 0.8]
- recovery_rate: uniform prior [0.03, 0.3]
Run this calibration (300 particles, 8 generations). Then:
- Inspect the joint posterior. Report the estimated values and compare to the true values
(transmission_rate = 0.35, recovery_rate = 0.1).
- Produce a figure showing the joint posterior as a 2D scatter plot (transmission_rate on the x-axis,
recovery_rate on the y-axis), with the true values marked as a red cross.
DELIVERABLES
- The observed.csv file with the synthetic data.
- Two validated calibration setups (single-parameter and two-parameter), both built on a shared base.
- Two sets of calibration results, with posterior and fit inspection reported.
35

- Both figures.
- A brief summary: did the calibration recover the true parameters? How tight are the posteriors? Did
calibrating two parameters simultaneously make the estimates worse?
T3 (Calibrate→Project): Calibrate, then project baseline vs intervention
STEP 1: Generate synthetic observed data and calibrate
Simulate a synthetic outbreak (afterwards, we will calibrate against it).
Run a forward SIR simulation with these "true" parameters:
- Population: 500,000
- transmission_rate: 0.12
- recovery_rate: 0.04
- Period: Jan 1 - Mar 31, 2026 (~90 days)
- Initial conditions: S = 0.9999, I = 0.0001, R = 0.0
- 1 simulation
Extract Infected_total and save as observed.csv (columns: date, cases).
Run a calibration that:
- Fixes recovery_rate = 0.04.
- Places a uniform prior on transmission_rate over [0.03, 0.4].
- Uses the observed.csv generated above, targets Infected_total, uses RMSE distance.
- Uses the SMC strategy with 200 particles and 5 generations.
Validate and run the calibration. Inspect the posterior -- confirm that the estimated
transmission_rate is
reasonably close to 0.12.
STEP 2: BASELINE projection (no intervention)
Produce a projection that extends the simulation 3 months beyond the calibration period:
- Starting from the simulation parameters above, change only the simulation end date to 30 June 2026.
- 200 posterior samples.
Inspect the results: what are the projected peak date and magnitude for Infected_total? Get quantiles
(0.05, 0.5, 0.95).
STEP 3: Intervention projection
Produce a second projection (intervention):
- Extend to 30 June 2026 (same as baseline).
36

- Override the transmission rate, dropping it to 0.03 from April 15 through June 1 (this should drive
the
effective R0 below 1, suppressing the epidemic two weeks into the projection window).
- 200 posterior samples.
STEP 4: Compare scenarios
Compare the projection results: baseline vs intervention. Report the comparison results and the
deltas.
STEP 5: Visualize
Produce a single figure with two panels:
- Left panel: epidemic curves. Plot the median projected Infected_total for both scenarios (Baseline
as
blue, Intervention as orange) with 90% CIs as shaded bands. Mark the end of the calibration period
(March 31) with a vertical dashed line. Mark the beginning and end of the intervention. If the
observed
data from Step 1 is available, overlay it as black dots for the calibration window.
- Right panel: cumulative attack rate. Plot the median cumulative Recovered_total (as a fraction of
population) for both scenarios over the full projection period, with 90% CIs.
DELIVERABLES
- The synthetic observed.csv and a validated calibration output.
- Two projection outputs, each inspectable after the fact.
- The comparison of metrics (deltas) between the two scenarios.
- A two-panel figure comparing the scenarios.
- A brief summary: how much does the intervention reduce the peak? Delay it? Lower the final attack
rate?
Are the 90% CIs well-separated or do the scenarios overlap substantially?
T4 (School-closure sweep): Optimal timing of a three-week school closure (NY State)
Study the effect of a three-week school closure on a regular influenza season in New York State.
SETUP
- Use New York State's age-structured population and all available contact layers (home, school, work,
community).
- Influenza-like epidemiology, seeded with a small number of infectious individuals at the start of
the
season.
- The season runs 1 October 2026 -> 31 May 2027.
- Tune the model so that, with no intervention, the epidemic peaks around 15 February 2027. Report the
37

peak date you actually achieve and how you got there.
- Use 100 stochastic realizations per configuration.
INTERVENTION
A school closure removes all school-layer contacts for 21 consecutive days. Nothing else changes --
the
other contact layers are untouched.
QUESTION
Where in the season should those three weeks be placed to minimize the final attack rate, and how much
does the best placement actually buy you?
- Sweep the closure start date weekly from 1 December 2026 through 1 April 2027, running the full
season
for each start date.
- Also run the unmitigated season as the reference.
- For each start date compute the final attack rate (cumulative infections as a percentage of the
population), the peak incidence, and the peak date.
DELIVERABLES
- A table of closure start date -> final attack rate, peak incidence, peak date.
- The optimal start date, and the relative reduction in attack rate it achieves versus no closure.
- How sensitive the benefit is to timing: how much of the benefit is lost by starting two weeks too
early
or two weeks too late, and the range of start dates that come within 10% of the optimum's benefit.
- Two figures:
- Final attack rate vs. closure start date, with the unmitigated attack rate as a horizontal
reference
line and the unmitigated peak date marked.
- Epidemic curves over the season for three cases overlaid -- no closure, optimally timed closure,
and a
closure starting one month after the optimum -- with the closure windows shaded and uncertainty
bands.
- A short summary answering the question directly: what is the ideal placement, what relative impact
does
it achieve, and briefly why the optimum sits where it does.
T5 (Measles coverage sweep): Measles risk in Vermont across vaccination coverage
Study the potential impact of a measles outbreak in the state of Vermont if vaccination coverage falls
into the 80%-95% range.
SETUP
38

- Use Vermont's age-structured population and all available contact layers (home, school, work,
community).
- Measles epidemiology in an SEIR structure: latent period ~12 days, infectious period ~8 days, and a
transmission rate chosen to give a basic reproduction number typical of measles (R0 ~ 15). State the
R0
you actually obtain and how you determined it.
- MMR coverage is represented as immunity present before the outbreak starts: a covered individual is
immune at day 0 and plays no further part in transmission.
- Seed the outbreak with 5 imported infectious individuals on 1 January 2027 and run through
31 December 2027.
- Use 200 stochastic realizations per coverage level.
PART 1 -- Coverage sweep
Sweep coverage from 80% to 95% in steps of 1 percentage point. For each level report:
- the probability of a large outbreak (define a threshold, e.g. more than 1,000 cases, and say what
you
used),
- median total cases and the attack rate **among the initially susceptible** (do not count the
pre-existing immune as cases),
- peak incidence and peak date, with uncertainty.
PART 2 -- Imperfect vaccine
The MMR vaccine is not perfect. Repeat the sweep assuming it is 97% effective, so 3% of vaccinated
individuals remain fully susceptible. Does any coverage level in the 80%-95% range still reach herd
immunity?
PART 3 -- Age structure and targeting
At 88% coverage (97% vaccine efficacy), report the age-stratified attack rate and the share of total
cases
falling in each age group -- in particular the 0-4 group, who are largely too young to be fully
vaccinated.
Then: if Vermont could run a catch-up campaign targeting a single age group, raising that one group's
coverage to 98% while the rest stay at 88%, which group should it target to minimize total cases?
Compare
the candidate age groups, and say whether the best target is the group that carries the most cases or
the
one that drives the most transmission.
DELIVERABLES
- A table of coverage -> outbreak probability, total cases, attack rate, peak incidence, peak date,
for
both the perfect and the 97%-effective vaccine.
39

- A table comparing the single-age-group catch-up campaigns.
- A figure: total cases and outbreak probability against coverage, for both vaccine assumptions, with
the
theoretical herd-immunity threshold (1 - 1/R0) marked as a vertical line.
- A figure: epidemic curves at three representative coverage levels spanning the transition, with
uncertainty bands.
- A short summary: over what coverage range does outbreak risk collapse, how sharp is that transition,
and
how does the empirical threshold compare with 1 - 1/R0? What does an 80% versus a 95% Vermont look
like
in absolute numbers, and where should a catch-up campaign go?
40
