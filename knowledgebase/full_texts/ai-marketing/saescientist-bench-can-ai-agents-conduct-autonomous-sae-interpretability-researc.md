---
title: 'SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?'
url: https://arxiv.org/abs/2609.09113
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Yuqiao Tan
- Shizhu He
- Jun Zhao
- Kang Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.09113
pages: 41
chars: 123534
fetched_at: '2026-11-08T13:34:32+00:00'
kb_version: 1
---

# SAEScientist-Bench: Can AI Agents Conduct Autonomous SAE Interpretability Research?

SAESCIENTIST-BENCH: CANAI AGENTSCONDUCT
AUTONOMOUSSAE INTERPRETABILITYRESEARCH?
Yuqiao Tan1,2, Shizhu He1,2∗, Jun Zhao1,2, Kang Liu1,2
1The Key Laboratory of Cognitive Intelligence, Institute of Automation, CAS
2School of Artificial Intelligence, University of Chinese Academy of Sciences
tanyuqiao2025@ia.ac.cn,{shizhu.he,jzhao,kliu}@nlpr.ia.ac.cn
ABSTRACT
While research on recursive self-improvement (RSI) has predominantly automated
model training pipelines, reliable autonomous development demands a missing
pillar: post-hoc monitoring and auditing to understand what models learn and
ensure safe alignment. Mechanistic interpretability tools are essential to bridge
this gap, among which Sparse Autoencoders (SAEs) serve as a cornerstone by
isolating interpretable features for model inspection and steering. In this paper,
we introduce SAESCIENTIST-BENCHto evaluate whether AI agents can act as
scientists utilizing SAE tools for autonomous mechanistic discovery. Given a
target concept, an agent designs contrastive probes and navigates a Gemma Scope
dictionary of 131K+ features in Gemma-2-9B-IT to discover the optimal fea-
ture, evaluated against curated expert reference features anchored on Neuronpedia
across activation rank, concept selectivity on contrastive texts, and causal steer-
ing. Across 10 agent configurations and 20 tasks, frontier agents demonstrate
genuine discovery capabilities and lead different evaluation dimensions, but re-
main well behind the expert baseline, approaching expert levels on separating
target concepts from contrastive controls while lagging substantially in causal
generation steering. Further analysis reveals that although agents can design con-
trasts to rule out spurious candidates, they frequently misinterpret experimental
measurements. These results establish experimental model understanding as a
measurable capability for closed-loop autonomous AI R&D. Our code is available
athttps://github.com/Trae1ounG/SAEScientist.
GPT-5.6
Luna
GLM-5.2 GPT-5.5 GPT-5.6
Sol
Gemini 3.8
Flash
Claude
Opus 4.8
Grok 4.6 Claude
Sonnet 5
Claude
Opus 5
Kimi K3 Neuronpedia
Expert
0
20
40
60
80
100
SAEScientist Agent Index
Rank Activation Steering
50.3 52.3 54.3 57.3 59.6 62.6 62.9 65.0 65.4 65.8 85.6
Figure 1:SAEScientist Agent Index.Agents are ordered by their composite Overall score, with
each bar decomposed into equally weightedRank, Activation, and Steeringcomponents. Error bars
denote standard deviations across three independent runs.
∗ Corresponding author.
1
arXiv:2609.09113v2  [cs.AI]  11 Sep 2026

1 INTRODUCTION
Recursive self-improvement (RSI) motivates the development of agents that can contribute to suc-
cessive stages of AI research and development (Mahmoud et al., 2026; Meng et al., 2026). Current
systems and benchmarks study automated experimentation, agent modification, machine learning
engineering, paper reproduction, and post-training (Lu et al., 2024; Zhang et al., 2026; Chan et al.,
2025; Starace et al., 2025; Rank et al., 2026; Tan et al., 2026b). Understanding the resulting models
is another part of this research process. As agents take on more development work, we also need to
measure their ability to investigate what trained models represent and how interventions affect their
behavior.
Model evaluation and alignment research motivate this need. Reward hacking formalizes how
optimizing a proxy objective can conflict with the intended objective (Skalse et al., 2022). Experiments
with deliberately trained deceptive behaviors further show that such behaviors can persist through
subsequent safety training (Hubinger et al., 2024). Interpretability and auditing agents offer tools for
investigating model representations and hidden behaviors (Shaham et al., 2024; Bricken et al., 2025).
Evaluating their experimental skills can help establish how reliably agents perform this part of model
analysis.
Sparse autoencoders (SAEs) provide a practical tool for these investigations. They decompose model
activations into sparse combinations of learned feature directions, many of which correspond to
recognizable concepts (Cunningham et al., 2023; Bricken et al., 2023; Gao et al., 2024; Templeton
et al., 2024). Researchers can examine the texts that activate a feature and intervene along its direction
to test effects on model outputs (Marks et al., 2024; Arad et al., 2025). Steering performance depends
on feature selection, and interpretability alone is an insufficient proxy for steering utility (Wu et al.,
2025; Wang et al., 2026a). Pretrained dictionaries such as Gemma Scope make these experiments
accessible without training a new SAE (Lieberum et al., 2024).
Recent agents explain SAE features, discover candidate features, and analyze circuits through
interaction with interpretability tools (Han et al., 2026; Marin-Llobet & Ferrando, 2026; Khan et al.,
2026). These advances motivate a common evaluation of how well different agents carry out feature
discovery. An agent must design informative probes, compare candidates, and select a feature whose
behavior holds up under evaluation. Measuring both activation behavior and steering outcomes makes
these abilities observable and captures distinctions that either aspect alone can miss (Wu et al., 2025;
Wang et al., 2026a).
To address this challenge, we introduce SAESCIENTIST-BENCH, a benchmark designed to evaluate
AI agents as scientists utilizing SAE tools for mechanistic discovery. Covering 20 tasks across diverse
concept domains (e.g., multilingual understanding, specialized formats, and safety-critical topics), an
agent designs contrastive probes to navigate pretrained SAE dictionaries in Gemma-2-9B-IT (Gemma
Team, 2024) and selects optimal features. Discovered features are systematically evaluated against
curated expert reference baselines anchored on Neuronpedia features (Lin, 2023) under a unified
scoring framework comprisingactivation rank,activation selectivity, andcausal steering.
Across 10 frontier agents and these tasks, empirical evaluations demonstrate that agents exhibit
genuine discovery capabilities, with Kimi K3 (Kimi Team, 2026) achieving the highest composite
overall score, followed closely by Claude Opus 5 and Sonnet 5, while GPT-5.6 Sol and Grok 4.6
demonstrate strong reasoning and steering capabilities. Different frontier models excel in distinct
dimensions: Opus leads in activation rank, Kimi leads in activation selectivity, and Grok 4.6 leads
in steering efficacy. However, a substantial gap remains compared to the expert reference baseline.
While top agents approach expert levels on activation selectivity, reaching 92.91 against the Expert
baseline of 98.92, their ability to causally steer model generation falls markedly short, scoring only
31.47 against 57.75. Further qualitative and behavioral analysis indicates that agents often misread
experimental measurements, struggle to separate format from concept, and produce features that
degrade downstream generation. Our contributions are as follows:
• We introduce SAESCIENTIST-BENCH, comprising 20 discovery tasks across diverse concept
domains, where agents design contrastive probes and navigate a 131K+ feature dictionary in
Gemma-2-9B-IT to discover SAE features.
2

Figure 2:SAEScientist-Bench workflow.For a concept and fixed SAE, the agent writes probes
Pi, compares candidates fj, and submits a feature. The evaluator measures Rank, Activation, and
Steering using Expert and the evaluation set. Portuguese texts and replies illustrate the process.
• We establish a standardized evaluation framework measuring activation rank, activation
selectivity, and causal steering against Neuronpedia expert reference baselines, evaluating
10 frontier agents across multiple independent runs.
• We provide systematic behavioral analyses of authored probes, candidate comparisons,
and steering outputs, revealing how agents interpret experimental evidence and where
autonomous scientific discovery currently succeeds and fails.
2 PRELIMINARIES: SAE FEATURES ANDSTEERING
SAE formulation and feature activations.A language model maps input text into token-level
hidden states. At a chosen layer, a Sparse Autoencoder (SAE) encodes a hidden state h∈R d into a
sparse vector of nonnegative feature activations z∈R m, reconstructing the state via a linear decoder:
z= Encoder(h), ˆh=b dec +
m−1X
f=0
zf df ,(1)
where m is the dictionary size, bdec is a reconstruction bias, and df =W dec[f,:] denotes feature f’s
decoder direction. SAE training balances reconstruction fidelity with sparsity (Cunningham et al.,
2023). In Gemma Scope (Lieberum et al., 2024), JumpReLU applies learned activation thresholds
to ensure that only a small subset of features activate per token (Rajamanoharan et al., 2024). Each
coordinate f corresponds to an isolated latent feature, and its scalar activation zf quantifies the
expression of that feature on the input text.
Feature steering via activation addition.Beyond measuring activations, a feature can be used to
causally intervene on model generation. Specifically, activation steering adds the feature’s decoder
directiond f directly to the model’s hidden state during inference:
h←h+αd f ,(2)
where α controls the intervention strength. The language model then continues generation from this
modified state. By comparing model outputs before and after intervention, one can directly evaluate
the causal effect of featurefon downstream behavior (Arad et al., 2025).
3

Figure 3:Benchmark coverage.Category shares and task counts by SAE layer, with an example
concept and Expert feature for each category. All tasks have equal weight. Appendix A.1 lists the
full set.
3 SAESCIENTIST-BENCH
3.1 TASKCONSTRUCTION
A task pairs a target concept with a specific layer of the base language model, Gemma-2-9B-IT
(Gemma Team, 2024), equipped with pretrained Gemma Scope residual-stream SAEs (Lieberum
et al., 2024). The agent is tasked with discovering a single feature within that layer’s SAE dictionary
(131,072 features) that best represents the concept. As illustrated in Figure 3, SAESCIENTIST-BENCH
comprises 20 discovery tasks across layers 9 and 20, covering diverse concept domains including
multilingual understanding (e.g., Portuguese, Spanish, Latin, Turkish), specialized document formats
(e.g., earnings reports, tax filing, job postings), and domain-specific knowledge (e.g., clinical symptom
reports, pharmaceutical dosing).
For each task, the benchmark provides an evaluation suite consisting of three types of text: positive
texts expressing the intended concept, hard-negative texts presenting confusable alternatives (e.g.,
discussing Portuguese in English), and neutral texts providing unrelated controls. In addition, each
task includes evaluation prompts to test causal steering effects on downstream generation. To
establish a rigorous reference standard, each task is paired with an Expert reference feature anchored
in Neuronpedia’s feature repository (Lin, 2023), established either directly from public steering
presets (e.g., Cat) or through standard expert curation workflows across positive and contrastive texts.
These task descriptions, Expert features, and evaluation suites remain strictly frozen during agent
discovery and are reserved solely for post-submission benchmarking.
3.2 INTERACTIONPROTOCOL
The agent receives the concept description, base-model and SAE identifiers, hook point, and dictionary
width. Expert and the evaluation set remain reserved for evaluation. The probe_sae interface
accepts up to 64 agent-written texts per request and either retrieves the top-k activating features or
measures a supplied set of candidates. Responses include activations and ranks in the full dictionary.
The model and its execution harness jointly carry out this investigation. The agent revises its texts
and candidates, then submits one feature ID for the evaluator to test through activation and steering.
In Figure 2, Pi denotes an agent-written probe and fj a candidate feature. The subscripts enumerate
the illustrated probes and candidates. We use f for the submitted feature and fexp for Expert. Agent-
written probes guide discovery, while the separate evaluation set measures the final submission.
During discovery, access is restricted to the probe interface and the provided workspace. The same
fixed base model and SAE support both discovery measurements and subsequent evaluation.
3.3 MEASUREMENTS ANDSCORES
We evaluate each submitted feature across three complementary dimensions, which are subsequently
averaged across tasks:Activation Rankevaluates how prominently a feature activates relative to the
dictionary,Activation Selectivityevaluates concept separation between positive texts and contrastive
(negative and neutral) controls, andCausal Steeringmeasures downstream generation change under
feature intervention.
4

Activation Rank (Rank).An effective SAE feature should be prominently activated when the
model processes its target concept, rather than being overshadowed by irrelevant dictionary directions.
To assess whether an agent identifies a sufficiently prominent feature for the concept, we measure
its activation rank relative to the expert reference baseline across positive evaluation texts. For each
positive text, a feature’s text-level activation is computed as the mean of its three largest non-special-
token activations across the sequence, providing a more stable estimate than single-token maximums
(Section 5.2). We then determine the feature’s rank against the full dictionary, where higher activation
corresponds to a lower numerical rank and inactive features receive the worst possible rank equal
to the dictionary size. Let rf and rexp denote the average dictionary ranks of the submitted feature
and the Expert baseline over positive texts. We compute the relative rank score scaled to a 100-point
reference:
Rank = 100× 2r exp
rf +r exp
.(3)
This score is defined in [0,200] , where a score of 100.0 indicates parity with the expert baseline,
values above 100.0 indicate a feature ranking ahead of expert, and values below 100.0 indicate lower
prominence.
Activation Selectivity (Activation).Beyond raw activation strength on target texts, a monoseman-
tic feature should respond selectively to the target concept itself rather than to confusable or spurious
patterns. We assess this on the evaluation suite by computing the AUROC separating positive texts
from contrastive controls (pooling hard-negative and neutral texts), crediting half a point for ties, and
scaling the result to[0,100]:
Activation = 100×max(0,2 AUROC−1).(4)
The score lies in [0,100] , where 100.0 denotes complete separation of positive texts from contrastive
controls, and 0 indicates chance-level or reversed discrimination.
Causal Steering (Steering).Feature discovery is ultimately validated by its ability to causally steer
model generation toward the target concept. On each evaluation prompt, the base model generates
completions under three conditions: unmodified baseline inference, feature steering (h←h+αd f ),
and a norm-matched random-direction control. An automated judge rates target relevance and
instruction preservation on a 0–4 scale, while separately flagging degeneration. Let Tf , Tbase, and
Trandom denote the average target-relevance ratings across prompts and judge passes. The steering
score measures the net increase in target expression beyond the stronger control condition, scaled to
[0,100]:
Steering = 100×max

0, Tf −max(T base, Trandom) 4  .(5)
The score lies in [0,100] , with higher values indicating stronger causal induction of target expressions.
We also denote this net gain as Target Effect (∆f = Steering/100). Crucially, Steering isolates the
magnitude of induced target expression; instruction preservation and output degeneration capture
complementary dimensions of generation quality and are evaluated alongside the primary score. For
alternative features, the intervention strength α is calibrated on five held-out prompts prior to final
evaluation to satisfy a minimum non-degeneration threshold, while Expert retains its frozen reference
scale (Appendix A.6).
Overall Score.As a default summary index to present overall discovery performance, each task’s
overall score is computed as the unweighted arithmetic mean across the three dimension scores:
Overall = Rank + Activation + Steering 3 .(6)
The Expert baseline achieves an overall score of 85.56 under this default setting. While this composite
provides a unified view for leaderboard presentation, individual metrics reflect complementary
dimensions of feature quality and are evaluated independently (Table 1 and Appendix A.4). All
reported benchmark scores represent this unweighted mean across all 20 tasks.
5

Table 1: Agent scores and rankings on Rank, Activation, Steering, and Overall across 20 tasks.
Overall Rank Activation Steering
Agent Score Pos. Score Pos. Score Pos. Score Pos.
Expert (Lin, 2023) 85.56 – 100.00 – 98.92 – 57.75 –
Kimi K365.82±1.871 74.30±5.60292.91±1.071 30.26±2.022
Claude Opus 5 65.41±0.41275.35±0.141 91.89±0.863 28.99±2.015
Claude Sonnet 5 65.04±2.203 73.45±2.813 92.01±3.472 29.66±2.684
Grok 4.6 62.93±1.014 67.21±3.076 90.11±0.83531.47±3.391
Claude Opus 4.8 62.57±5.425 70.25±6.384 90.90±3.564 26.55±7.136
Gemini 3.8 Flash 59.57±0.616 69.49±5.075 86.78±2.617 22.43±1.399
GPT-5.6 Sol 57.28±0.867 51.65±2.158 90.03±0.916 30.16±3.373
GPT-5.5 54.34±2.808 55.63±5.287 84.19±0.589 23.19±3.508
GLM-5.2 52.27±2.629 47.66±5.759 84.85±3.698 24.28±1.697
GPT-5.6 Luna 50.27±7.4010 46.92±14.9110 83.36±1.7210 20.54±5.7610
Scores are means over three runs. The±values give the standard deviation across runs.
4 EXPERIMENTALSETUP
4.1 EVALUATEDMODELS ANDHARNESSES
We evaluate 10 representative frontier agent configurations across our 20 discovery tasks. The
evaluated models span major model families: Kimi K3 (Kimi Team, 2026), Claude Opus 5, Claude
Sonnet 5, Claude Opus 4.8, Grok 4.6, Gemini 3.8 Flash, GLM-5.2, and the OpenAI series (GPT-5.6
Sol, GPT-5.5, GPT-5.6 Luna). Sol and Luna operate within the Codex harness, while all other
models are deployed in Cursor. To ensure parity and prevent data contamination, all agents receive
identical task instructions and interaction interfaces, with external network access disabled. Models
operate under unconstrained interactive environments where each agent autonomously decides its
reasoning effort, exploration trajectories, query counts, and stopping criteria without artificial step
caps. Detailed execution environments, model identifiers, and harness specifications are provided in
Appendix A.3.
4.2 EVALUATIONPIPELINE ANDAGGREGATION
For each task, an agent conducts an autonomous, multi-turn investigation using the probe interface.
Once the agent submits its chosen feature ID, the evaluation pipeline executes post-submission
validation: measuring text-level activations on the frozen evaluation set and performing causal
steering via greedy generation. Intervention scale α is calibrated against non-degeneration criteria
on held-out prompts (Appendix A.6), and steering outputs are rated in two passes by an automated
GPT-4o judge using anonymized output triples (baseline, steered, and random control; Appendix A.7).
To evaluate consistency, every model–harness configuration conducts three independent, end-to-end
investigations per task. We report the mean score and sample standard deviation (±) across the three
runs, with benchmark-level scores averaging all 20 tasks equally. Across these experiments, we
examine how effectively agents navigate the dictionary space to discover features, how they design
contrastive probes and interpret empirical feedback, and how their selected features causally alter
downstream generation.
5 RESULTS
5.1 OVERALLPERFORMANCE
Table 1 presents the main benchmark results across the ten evaluated agent configurations, alongside
the Neuronpedia Expert baseline. Overall performance reveals two overarching patterns. First,
6

frontier agents exhibit substantial scientific discovery capabilities across the 20 tasks, with Kimi K3
achieving the highest composite Overall score of 65.82, closely followed by Claude Opus 5 (65.41)
and Claude Sonnet 5 (65.04). Notably, different model families excel along distinct evaluative axes:
Claude Opus 5 achieves the strongest dictionary-wide Activation Rank (75.35), Kimi K3 dominates
Activation Selectivity (92.91), and Grok 4.6 leads in Causal Steering efficacy (31.47).
Second, while agents approach expert-level performance in distinguishing target concepts from
contrastive texts, a persistent capability gap remains in causal intervention. On Activation Selectivity,
top agents reach 92.91 compared to the Expert baseline of 98.92, indicating that agents can reliably
identify features that selectively fire on target concepts. In sharp contrast, causal generation steering
proves far more challenging: the top agent steering score reaches only 31.47 against Expert’s 57.75.
This divergence underscores that finding a correlated, selective feature does not readily translate into
finding a causally potent steering vector. For instance, although GPT-5.6 Sol ranks third on Steering
with a score of 30.16 and closely trails the category leader by only 1.31 points, its lower Activation
Rank of 51.65 primarily accounts for its gap behind the top performers.
Across repeated independent runs, agents exhibit stable overall rankings with modest variance,
typically within 1–3 points in standard deviation, demonstrating that discovery capabilities remain
consistent despite stochastic search trajectories (Appendix E). Finally, comparing overall scores with
general capability rankings on the Artificial Analysis Intelligence Index v4.2 reveals a strong rank
correlation (ρ= 0.800 ) across matching frontier models (Artificial Analysis, 2026), aligning well
with general model capabilities while highlighting white-box interpretability as a distinct evaluative
frontier (detailed in Appendix E.1).
Takeaway 1. Frontier agents exhibit clear capability trade-offs in mechanistic discovery,
but lag in causal validation.
Across 20 single-feature discovery tasks, frontier models achieve strong activation selectivity
but lag the curated expert baseline in causal steering (Overall 65.82 vs. 85.56, Steering 31.47
vs. 57.75). While agents can formulate informative contrastive probes to separate concepts
in representation space, their current difficulty in identifying causally potent steering vectors
highlights representational auditing as a critical bottleneck for future white-box RSI workflows.
5.2 HOWAGENTSSEARCH ANDTESTCANDIDATES
Table 2:Authored contrastive probes and case-level discovery scores on Portuguese (Layer
9).For each agent, final benchmark scores on the submitted feature are shown alongside the con-
trastive probes designed during discovery and the resulting feature activations, illustrating candidate
discrimination quality.
Agent & Case Scores Agent-authored Probe Texts Activation
Neuronpedia ExpertReference:Rank100.0|Act100.0|Steer85.0|Overall 95.0
GPT-5.6 Sol Portuguese:Nas manhãs de domingo, costumo abrir. . . 7.04
Rank: 3.97 Act: 100.0English about Portuguese:Portuguese is a Romance. . . 0.00
Steer: 88.8Ovr: 64.2 Spanish translation:Los domingos por la mañana, suelo
abrir. . .
0.00
Claude Opus 4.8 Portuguese:O meu vizinho comprou um carro novo. . . 11.94
Rank: 30.8 Act: 91.7French about Brazil:Le Brésil est le plus grand pays. . . 0.00
Steer: 84.4Ovr: 68.9Spanish translation:Mi vecino compró un coche nuevo. . . 0.00
Claude Opus 5 Portuguese:Hoje de manhã fui à padaria comprar. . . 3.81
Rank: 0.08 Act: 41.7Spanish translation:Esta mañana fui a la panadería. . . 1.19
Steer: 0.00Ovr: 13.9English translation:This morning I went to the bakery. . . 4.50
Kimi K3 Portuguese:Ontem fui ao mercado comprar frutas. . . 26.33
Rank: 100.0 Act: 100.0English translation:Yesterday I went to the market. . . 0.00
Steer: 85.0Ovr: 95.0Spanish translation:Ayer fui al mercado a comprar. . . 1.80
English about Portugal:Portugal is a country. . . 0.00
7

How do agents formulate hypotheses, construct contrastive probes, and navigate empirical feedback?
Table 2 illustrates this process across four independent Portuguese investigations in the layer-9 SAE,
linking the contrastive probes designed during discovery to final benchmark scores.
Cross-lingual probing and evidence interpretation.The probes reveal clear differences in concept
discrimination. Sol, Opus 4.8, and Kimi K3 successfully identify features that distinguish Portuguese
from related languages (Spanish) and non-target language descriptions (English or French), with zero
or negligible activation on controls. However, their final Rank scores reflect an important trade-off
between selectivity and activation strength: Sol’s feature achieves clean separation with an Activation
score of 100.00 and strong causal steering of 88.75, but its target activation is modest at 7.04, placing
it lower in the dictionary-wide ranking with a Rank score of 3.97. In contrast, Kimi K3 identifies a
prominent direction with much stronger target activation of 26.33, attaining both perfect separation
and a leading Rank score of 100.00. Meanwhile, Opus 5 illustrates an evidence-interpretation failure:
despite authoring matched Portuguese, Spanish, and English probes, its selected feature activates
more strongly on the English control at 4.50 than on the Portuguese target at 3.81, leading to an
overall score collapse down to 13.91. Detailed probe suites and complete search traces appear in
Appendices C.2 and B.2.
Separating concepts from format and substring distractors.Beyond cross-lingual contrasts,
agents construct targeted counterexamples to rule out superficial string matching and format-level
spurious correlations. In theCatdiscovery task, Claude Opus 5 encounters a candidate feature
that activates strongly on genuine feline sentences at 32.92, but also fires aggressively on unrelated
compound words such asCopycat killerat 44.00 andCatalytic converterat 24.54. By explicitly
designing these morphological negative controls, Opus 5 identifies that the candidate is merely
detecting the substring “cat” rather than the animal concept, and successfully rejects it in favor of the
monosemantic Expert feature, as detailed in Appendix Table 12. Conversely, GLM-5.2 demonstrates
an evidence-misinterpretation failure on theClinical symptomtask: while it designs diagnostic
controls to rule out general medical bureaucracy, its final candidate still fires at 70.25 on a patient
medical history entirely devoid of symptoms, as detailed in Appendix Table 14. GLM-5.2 erroneously
downplays this strong non-symptom response as negligible in its report, mistakenly selecting a feature
driven by clinical document formatting rather than actual symptoms.
Feature purity versus generation degeneration.Agents also face fundamental trade-offs between
concept selectivity and downstream behavioral impact. In theReal estatetask, agents diverge on how
to balance candidate purity against coverage, illustrated in Appendix Table 10. Sol and Grok 4.6
deliberately reject a broad feature candidate due to minor leakages on non-housing ads, selecting a
strictly selective feature instead. In contrast, Kimi K3 prioritizes broad listing coverage and accepts
this leakier candidate. Consequently, Kimi’s chosen feature achieves higher target relevance and
causal steering, but at the cost of substantial generation degeneration, rising from 32.5% to 52.5%.
These diverse strategies illustrate that autonomous discovery requires not only finding selective
features, but also arbitrating trade-offs between precision, coverage, and output stability.
Behind broad summary metrics, agents exhibit fundamentally distinct scientific investigation philoso-
phies, as reflected in their search workflows in Figure 4. Rather than following a uniform trial-and-
error strategy, models diverge along two critical dimensions: candidate breadth versus probe depth,
and deliberate verification versus heuristic selection.
Exploration breadth vs. probe depth.Sol prioritizes textual diversity over dictionary span, authoring
extensive probe variations averaging 115.1 texts across sentence lengths, topical contexts, and cross-
lingual translations, while testing a relatively small pool of 20.2 candidate features. Conversely,
Claude Opus 5 behaves as a broad screener, comparing over four times as many candidate features at
80.2 across fewer probe texts averaging 77.6. Meanwhile, Kimi K3 adopts a highly targeted strategy:
making far fewer retrieval queries and rarely returning to retrieval once a promising candidate is
identified, yet achieving top overall discovery scores through precise hypothesis formulation.
Active validation vs. heuristic selection.Even when agents converge on identical features, their
underlying scientific rigor differs sharply. For example, while Claude Opus 5 and Sonnet 5 select
the canonical Expert feature at nearly identical rates, their decision traces reveal opposite behaviors:
Opus 5 acts as an active hypothesis-tester, repeatedly authoring dedicated probes to directly evaluate
the Expert candidate before either selecting or deliberately rejecting it in favor of an alternative. In
contrast, Sonnet 5 frequently encounters the Expert candidate during initial retrieval but overlooks it
8

Retrieval
calls
Candidate
test calls
Distinct
texts
Tested
features
Return to
retrieval (%)
1.7 3.2 38.9 32.0 16.7
3.1 5.8 77.6 80.2 61.7
2.4 4.4 51.2 13.6 36.7
3.8 4.8 62.2 51.6 75.0
1.8 3.2 37.5 16.1 20.0
7.2 13.5 83.4 67.3 88.3
2.8 5.2 115.1 20.2 65.0
2.0 2.9 51.4 22.8 25.0
1.5 3.8 32.5 40.0 13.3
3.5 4.6 87.9 21.9 63.3
Recorded search behavior
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Figure 4:Autonomous scientific search workflows across frontier agents.Metrics report average
behavior per investigation across 20 tasks: number of authored probe requests, unique authored probe
texts, directly tested feature candidates, and the percentage of episodes where the agent resumed
candidate retrieval after direct testing. Column color scales are normalized independently.
without direct validation, relying instead on initial ranking heuristics. Because Expert identity is fully
anonymized during discovery, these patterns underscore that autonomous agents vary substantially in
scientific thoroughness, spanning from active experimental verification to passive reliance on initial
retrieval outputs, with comprehensive search outcomes detailed in Appendix B.1.
Takeaway 2. Search strategy matters, but rigorous hypothesis testing determines discovery
success.
Agents explore differently: Sol varies texts, Opus screens candidates, and Kimi targets precise
hypotheses. Yet finding effective features depends less on search volume than on designing
informative counterexamples, avoiding surface distractors, and accurately reading experimental
results.
5.3 WHATACTIVATIONSCORESREVEAL
While agent-authored probes guide candidate selection during search, our shared benchmark suite
objectively evaluates how the submitted features generalize across unseen contexts. Following the
Portuguese investigations examined in Table 2, Figure 5 tests the identical submitted candidate
features against the standardized Portuguese evaluation suite of eight held-out positive sentences
and twelve contrastive controls (full texts in Appendix Table 17). This controlled blind evaluation
exposes substantial disparities in generalization and selectivity that remain invisible during internal
search.
Coverage gaps and spurious activations.Features that appeared promising under agent probes
often falter on held-out benchmark texts. As shown in Figure 5a, candidates selected by Sonnet,
Grok, and Luna remain completely inactive on natural target sentences such as the rain passage, yet
exhibit spurious activations on irrelevant English controls such as warranty statements. Similarly,
Gemini’s submitted feature fails to fire on the research passage and misses multiple positives across
the broader test set. These coverage gaps demonstrate that surface-level probe validation frequently
under-specifies concept boundaries, allowing models to select features tied to narrow lexical cues
rather than the intended global semantic concept.
High selectivity vs. weak activation strength.A high scalar Activation score can mask critical
differences in feature strength. Both Sol and Expert achieve a perfect AUROC of 1.000 across the
full evaluation suite, cleanly ranking every positive text above every control text. However, their
absolute activation magnitudes tell a fundamentally different story. Sol’s feature is exceptionally
clean, remaining completely inactive at 0.00 across almost all control texts, but its target activation
on Portuguese sentences is very modest, averaging only 3.5–10.0 compared to 14.4–19.4 for Expert
9

Train Rain
Research Grammar Word list Warranty
15.7 19.4 14.4 3.2 4.9 0
1.1 8.7 9.5 0 1.3 0.8
3.6 0 2.3 0 2 4.5
3.6 0 2.3 0 2 4.5
9.4 15.1 9 2.3 6.7 0
10.8 2.7 0 0 0 0
5.5 10 3.5 0 1.9 0
1.1 8.7 9.5 0 1.3 0.8
1.1 8.7 9.5 0 1.3 0.8
3.6 0 2.3 0 2 4.5
15.7 19.4 14.4 3.2 4.9 0
(a) Text activations
.70 .85 1.0
(b) AUROC
Maximum
Top-three mean
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Expert
Figure 5:Generalization and aggregation sensitivity of discovered Portuguese features.(a) Acti-
vations across representative positive texts (Train, Rain, Research) and contrastive controls (Grammar,
Word list, Warranty), demonstrating that identical AUROC separation (e.g., Sol vs. Expert) conceals
major differences in absolute activation strength and dictionary rank. (b) AUROC comparison be-
tween maximum token activation and top-three-token mean aggregation; token averaging dampens
isolated lexical spikes in control texts, reliably isolating continuous semantic activation.
and 26.3 for Kimi K3 in Table 2. Because its target signal is relatively weak, the feature fails to stand
out against competing features across the full dictionary, collapsing Sol’s Activation Rank score to
only 3.97 versus 100.00 for Expert. This contrast illustrates that a feature can exhibit near-perfect
selectivity while remaining too weak to serve as a prominent, primary representation of the target
concept, explaining why rank and selectivity must be evaluated together.
Robustness via top-three-token aggregation.Figure 5b highlights why sequence-level aggregation
is critical when evaluating concept selectivity. Relying solely on the maximum token activation leaves
metrics vulnerable to isolated token outliers. For example, in Sol’s vocabulary control, an isolated
Portuguese loanword produces a sharp single-token spike of 5.56, whereas the full target sentence
maintains a moderate per-token response of 2.96. Under maximum aggregation, this spurious spike
degrades Sol’s AUROC to 0.969. In contrast, aggregating the top-three token activations amortizes
transient spikes, raising Sol’s AUROC to 1.000 and Opus 4.8’s from 0.927 to 0.958 (detailed in
Appendix Table 18). This verifies that multi-token averaging effectively filters isolated morphological
artifacts while rewarding coherent semantic activation across the text. Complete activation matrices
across all tasks appear in Appendix Figure 9.
5.4 STEERING ANDINSTRUCTIONPRESERVATION
While activation scores measure representational correlation, activation steering intervenes directly
on inference to evaluate causal control. Following the identical Portuguese features examined in
Table 2 and Figure 5, Figure 6 evaluates how intervening along each agent’s submitted direction (h←
h+αd f ) affects base model generation across six evaluation instructions. Each generation is rated
on a 0–4 scale along two orthogonal axes:target relevance(degree of Portuguese expression induced)
andinstruction preservation(retention of user constraints such as length, topic, and formatting).
Figure 6 reveals a sharp divide in causal efficacy across submitted features. While many features
achieved strong activation separation in Figure 5, only a small fraction reliably steer generation.
Features submitted by Sol, Opus 4.8, and Kimi K3, which discovered the Expert feature 41424,
exhibit high target relevance across instructions, successfully flipping model outputs into fluent
Portuguese, as illustrated in Table 3. In contrast, features selected by Opus 5, Sonnet 5, Grok 4.6, and
Luna yield flat zero target relevance across all six prompts, indicating that their correlated activations
fail to exert causal influence on downstream generation.
Furthermore, generation steering reveals subtle trade-offs between target induction and output quality.
While Steering isolates the net gain in target expressions, a high score does not guarantee well-formed
completions if user constraints are violated. Across the full 20-instruction benchmark suite, Sol
achieves a leading Steering score of 88.75 with high preservation of 3.525, whereas Opus 4.8 attains
10

HTTP 17×24 Poem EnergyPasswordGravity
4 2 4 2.5 3 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 3 4 4 3 3
0 0 0 0 0 0
2.5 4 4 4 4 3
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 2 4 2.5 3 4
(a) Target relevance
HTTP 17×24 Poem EnergyPasswordGravity
3.5 1 4 1.5 3 4
0 1 2 0 1.5 3
0 2.5 1 0 1.5 0
0 2.5 1 0 1.5 0
3.5 3 4 1.5 3 2.5
0 1 0 4 4 0
2.5 4 4 4 4 2.5
0 1 2 0 1.5 3
0 1 2 0 1.5 3
0 2.5 1 0 1.5 0
3.5 1 4 1.5 3 4
(b) Preservation
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Expert
Figure 6:Causal steering and instruction preservation under Portuguese feature intervention.
Evaluations across six diverse instructions: HTTP request explanation, 17 ×24 arithmetic, 4-line
poem, clean energy essay, password generation, and gravity definition. (a)Target relevance(0–4
scale) measures the intensity of induced Portuguese expression; (b)Instruction preservation(0–4
scale) measures fulfillment of the original task constraints without degeneration or incoherence.
Table 3: Opening excerpts under Portuguese steering.
Prompt:Introduce yourself in two sentences.
Selected by Opening excerpt
No steering I am Gemma, an open-weights AI assistant. . .
Expert /
 Kimi K3 Olá! Eu sou o Gemma, um modelo de linguagem. . .
GPT-5.6 Sol Olá! Eu sou Gemma, um modelo de linguagem. . .
Claude Opus 4.8 Olá! Eu sou um modelo de linguagem grande. . .
GPT-5.6 Luna Hello! I am Gemma, an open-weights AI assistant. . .
84.38 with lower preservation of 3.050 due to repetition and length drift. For instance, on a requested
four-line rhyming poem, Sol outputs four coherent Portuguese lines, while Opus 4.8 generates eleven
lines with repetitive loops, and Expert generates six. In more extreme failures like the clinical
symptom task, GLM-5.2’s intervention completely disrupts instruction following, converting an
innocent self-introduction into a rambling patient medical history. Complete generated responses,
preservation ratings, and degeneration checks appear in Appendix D.3.
Takeaway 3. Causal steering separates superficial activation correlates from actionable
mechanisms.
While multiple agents discover features that achieve near-perfect activation separation on static
texts, very few translate into reliable steering directions. Effective causal intervention requires
precise semantic modulation without triggering degeneration, instruction drift, or formatting
collapse, marking causal steering as the most rigorous test of autonomous interpretability re-
search.
6 RELATEDWORK
Mechanistic interpretability: From neurons to SAE features.Mechanistic interpretability
studies model representations through neuron analysis, circuit analysis, causal tracing, and knowledge
attribution (Elhage et al., 2021; Meng et al., 2022; Wang et al., 2022; Geva et al., 2021; Dai et al.,
2022; Song et al., 2024; Yu & Ananiadou, 2024). However, polysemanticity, where individual neurons
activate across unrelated concepts, fundamentally limits the interpretability of raw hidden states
(Bricken et al., 2023). Sparse Autoencoders (SAEs) address this barrier by decomposing internal
activations into sparse combinations of learned feature directions (Cunningham et al., 2023; Gao
et al., 2024; Templeton et al., 2024). These features support causal intervention (Marks et al., 2024),
11

with steering effectiveness depending on their influence on model outputs (Arad et al., 2025; Shu
et al., 2025; Wang et al., 2026a). Recent selection methods use correlations with task performance,
supervision, or similarities between features to improve steering (Cho et al., 2026; Jørgensen &
Hansen, 2026; Liu et al., 2026). Pretrained libraries such as Gemma Scope make large dictionaries
accessible (Lieberum et al., 2024), while feature splitting, absorption, and composition complicate
the mapping between features and concepts (Chanin et al., 2024; Leask et al., 2025).
Automated interpretation and SAE benchmarking.Automated methods use language models
to explain neurons and SAE features from activating examples (Bills et al., 2023; Paulo et al.,
2025). Agents extend this process through interactive experiments (Shaham et al., 2024; Han et al.,
2026; Bissell et al., 2025), feature discovery (Marin-Llobet & Ferrando, 2026), and circuit analysis
(Khan et al., 2026). Other agents investigate hidden model behaviors using auditing tools (Bricken
et al., 2025; Sheshadri et al., 2026). Agents also assess mechanistic interpretability research by
examining papers, code, and data for experimental coherence, reproducibility, and generalizability
(Bai et al., 2026). Existing evaluations measure SAE quality and feature recovery (Karvonen et al.,
2025; Venhoff et al., 2024), interpretability without generated explanations (Paulo & Belrose, 2025),
concept disentanglement (Huang et al., 2024), circuit identification (Mueller et al., 2025), and
concept detection and steering (Wu et al., 2025). Studies also examine whether SAE metrics reliably
distinguish feature quality and learned structure (Chanin, 2026; Heap et al., 2026). SAESCIENTIST-
BENCHevaluates agents’ ability to search pretrained SAE dictionaries using contrastive probes, with
scores for activation rank, activation selectivity, and steering.
Agents for AI research and development.Recursive self-improvement motivates research on
agents that can improve their own software and contribute to AI development (Zhang et al., 2026;
Mahmoud et al., 2026). Existing benchmarks assess software and machine learning engineering
(Tan et al., 2026a; Chan et al., 2025), paper reproduction (Starace et al., 2025), scientific insight
rediscovery (Wang et al., 2026b), research proposal assessment (Ho et al., 2026), and literature
discovery (Xiong et al., 2026). Other evaluations cover scientific data analysis (Chen et al., 2025),
data curation and post-training (Meng et al., 2026; Rank et al., 2026; Tan et al., 2026b), and broader
experimental research workflows (Lupidi et al., 2026; Xu et al., 2026). Together, these studies assess
distinct skills involved in research and development. SAESCIENTIST-BENCHextends this evaluation
to experiments on trained model representations, measuring how agents design probes, select SAE
features, and obtain features that influence generation.
7 LIMITATIONS
While SAESCIENTIST-BENCHestablishes a standardized foundation for evaluating autonomous
mechanistic interpretability agents, several limitations offer directions for future work. First, our
benchmark focuses on concept-driven single-feature discovery within Gemma-2-9B-IT across two
layers of Gemma Scope residual-stream SAEs under a fixed probe interface. Expanding evaluations
to diverse model families, broader dictionary widths, multi-feature circuit discovery, and open-ended
hypothesis generation without pre-specified concepts will provide a more comprehensive view of
agent capabilities. Second, candidate evaluation relies on fixed text suites, frozen expert baselines,
and automated LLM-as-a-judge assessments for steering; incorporating human-in-the-loop validation,
multiple reference features, and multi-judge ensembles can further minimize potential rating noise.
Finally, while SAESCIENTIST-BENCHbenchmarks post-hoc feature auditing, integrating agent-
discovered features directly into downstream model editing, unlearning, or continual alignment loops
represents an essential next step toward realizing fully closed-loop recursive self-improvement.
8 CONCLUSION
SAESCIENTIST-BENCHestablishes a standardized benchmark to evaluate AI agents as scientists
conducting autonomous mechanistic interpretability research. Across ten frontier agent configura-
tions and 20 tasks, our evaluations reveal that while agents approach the expert reference baseline in
distinguishing concepts in activation space, a substantial capability gap persists in causal steering.
Behavioral analyses demonstrate that effective discovery hinges not on exploration volume, but
on rigorous hypothesis testing, designing informative counterexamples, and accurately interpreting
12

experimental feedback. By bridging mechanistic interpretability with autonomous AI research,
SAESCIENTIST-BENCHprovides an essential, auditable foundation toward verifying internal repre-
sentations in recursive self-improvement loops.
REPRODUCIBILITYSTATEMENT
Appendix A specifies the tasks, agents, and evaluation protocol. Appendix B follows the investigations.
Appendices C and D provide activation measurements and complete generations. Appendix E
compares tasks and repeated runs. The underlying records preserve model identifiers and execution
traces.
AI USESTATEMENT
Generative AI tools were used solely for writing assistance, text polishing, and editorial phrasing
throughout the preparation of this manuscript. All research conceptualization, benchmark design,
experimental execution, data collection, and analytical interpretations were conducted entirely by the
human authors.
REFERENCES
Dana Arad, Aaron Mueller, and Yonatan Belinkov. SAEs are good for steering – if you select the
right features. InProceedings of the 2025 Conference on Empirical Methods in Natural Language
Processing, pp. 10241–10259. Association for Computational Linguistics, 2025. doi: 10.18653/v1/
2025.emnlp-main.519. URL https://aclanthology.org/2025.emnlp-main.519/.
Artificial Analysis. Artificial Analysis Intelligence Index, 2026. URL https://
artificialanalysis.ai/models. Version 4.2. Model pages checked September 7, 2026.
Xiaoyan Bai, Alexander Baumgartner, Haojia Sun, Ari Holtzman, and Chenhao Tan. The story is
not the science: Execution-grounded evaluation of mechanistic interpretability research.arXiv
preprint arXiv:2602.18458, 2026. URLhttps://arxiv.org/abs/2602.18458.
Steven Bills, Nick Cammarata, Dan Mossing, Henk Tillman, Leo Gao, Gabriel Goh, Ilya Sutskever,
Jan Leike, Jeff Wu, and Alec Radford. Language models can explain neurons in language models.
OpenAI Research Blog, 2023. URL https://openaipublic.blob.core.windows.
net/neuron-explainer/paper/index.html.
Mark Bissell, Michael Byun, and Daniel Balsam. You and your research agent: Lessons from
using agents for interpretability research. Goodfire Research, technical article, 2025. URL
https://www.goodfire.com/blog/you-and-your-research-agent.
Trenton Bricken, Adly Templeton, Joshua Batson, Brian Chen, Adam Jermyn, Tom Conerly, Nick
Turner, Cem Anil, Carson Denison, Amanda Askell, Robert Lasenby, Yifan Wu, Shauna Kravec,
Nicholas Schiefer, Tim Maxwell, Nicholas Joseph, Zac Hatfield-Dodds, Alex Tamkin, Karina
Nguyen, Brayden McLean, Josiah E Burke, Tristan Hume, Shan Carter, Tom Henighan, and
Christopher Olah. Towards monosemanticity: Decomposing language models with dictionary
learning.Transformer Circuits Thread, 2023. URL https://transformer-circuits.
pub/2023/monosemantic-features/index.html.
Trenton Bricken, Rowan Wang, Sam Bowman, Euan Ong, Johannes Treutlein, Jeff Wu, Evan
Hubinger, and Samuel Marks. Building and evaluating alignment auditing agents. Anthropic
Alignment Science, research report, 2025. URL https://alignment.anthropic.com/
2025/automated-auditing/.
Jun Shern Chan, Neil Chowdhury, Oliver Jaffe, James Aung, Dane Sherburn, Evan Mays, Giulio
Starace, Kevin Liu, Leon Maksin, Tejal Patwardhan, Lilian Weng, and Aleksander M ˛ adry. MLE-
bench: Evaluating Machine Learning Agents on Machine Learning Engineering. InInternational
Conference on Learning Representations, 2025. URL https://arxiv.org/abs/2410.
07095.
David Chanin. Are sparse autoencoder benchmarks reliable?, 2026. URL https://arxiv.org/
abs/2605.18229.
David Chanin, James Wilken-Smith, Tomáš Dulka, Hardik Bhatnagar, Satvik Golechha, and Joseph
Bloom. A is for absorption: Studying feature splitting and absorption in sparse autoencoders, 2024.
URLhttps://arxiv.org/abs/2409.14507.
13

Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi
Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns, Daniel
Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan Sun. ScienceAgentBench:
Toward rigorous assessment of language agents for data-driven scientific discovery. InInternational
Conference on Learning Representations, 2025. URL https://arxiv.org/abs/2410.
05080.
Seonglae Cho, Zekun Wu, and Adriano Koshiyama. CorrSteer: Generation-time LLM steering via
correlated sparse autoencoder features. InInternational Conference on Machine Learning, 2026.
URLhttps://arxiv.org/abs/2508.12535.
Hoagy Cunningham, Aidan Ewart, Logan Riggs, Robert Huben, and Lee Sharkey. Sparse autoen-
coders find highly interpretable features in language models, 2023. URL https://arxiv.
org/abs/2309.08600.
Damai Dai, Li Dong, Yaru Hao, Zhifang Sui, Baobao Chang, and Furu Wei. Knowledge neu-
rons in pretrained transformers. InProceedings of the 60th Annual Meeting of the Associ-
ation for Computational Linguistics (Volume 1: Long Papers), pp. 8493–8509. Association
for Computational Linguistics, 2022. doi: 10.18653/v1/2022.acl-long.581. URL https:
//aclanthology.org/2022.acl-long.581/.
Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda
Askell, Yuntao Bai, Anna Chen, Tom Conerly, et al. A mathematical framework for transformer
circuits.Transformer Circuits Thread, 2021. URL https://transformer-circuits.
pub/2021/framework/index.html.
Leo Gao, Tom Dupré la Tour, Henk Tillman, Gabriel Goh, Rajan Troll, Alec Radford, Ilya Sutskever,
Jan Leike, and Jeffrey Wu. Scaling and evaluating sparse autoencoders, 2024. URL https:
//arxiv.org/abs/2406.04093.
Gemma Team. Gemma 2: Improving open language models at a practical size.arXiv preprint
arXiv:2408.00118, 2024. URLhttps://arxiv.org/abs/2408.00118.
Mor Geva, Roei Schuster, Jonathan Berant, and Omer Levy. Transformer feed-forward layers are
key-value memories. InProceedings of the 2021 Conference on Empirical Methods in Natural
Language Processing, pp. 5484–5495. Association for Computational Linguistics, 2021. doi:
10.18653/v1/2021.emnlp-main.446. URL https://aclanthology.org/2021.emnlp-
main.446/.
Jiaojiao Han, Wujiang Xu, Mingyu Jin, and Mengnan Du. SAGE: An agentic explainer framework
for interpreting SAE features in language models. InProceedings of the 19th Conference of the
European Chapter of the Association for Computational Linguistics (Volume 5: Industry Track), pp.
483–495. Association for Computational Linguistics, 2026. doi: 10.18653/v1/2026.eacl-industry.
37. URLhttps://aclanthology.org/2026.eacl-industry.37/.
Thomas Heap, Tim Lawson, Lucy Farnik, and Laurence Aitchison. Automated interpretability
metrics do not distinguish trained and random transformers. InInternational Conference
on Learning Representations, 2026. URL https://proceedings.iclr.cc/paper_
files/paper/2026/hash/7ab63a5314680e2f083cb288abeaeb8e-Abstract-
Conference.html.
Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, and Furong Huang. SoundnessBench: Can your AI
scientist really tell good research ideas from bad ones?arXiv preprint arXiv:2605.30329, 2026.
URLhttps://arxiv.org/abs/2605.30329.
Jing Huang, Zhengxuan Wu, Christopher Potts, Mor Geva, and Atticus Geiger. RA VEL: Evaluating
interpretability methods on disentangling language model representations. InProceedings of the
62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 8669–8687, 2024. doi: 10.18653/v1/2024.acl-long.470. URL https://aclanthology.
org/2024.acl-long.470/.
Evan Hubinger, Carson Denison, Jesse Mu, Mike Lambert, Meg Tong, Monte MacDiarmid, Tamera
Lanham, Daniel M. Ziegler, Tim Maxwell, Newton Cheng, Adam Jermyn, Amanda Askell, Ansh
Radhakrishnan, Cem Anil, David Duvenaud, Deep Ganguli, Fazl Barez, Jack Clark, Kamal
Ndousse, Kshitij Sachan, Michael Sellitto, Mrinank Sharma, Nova DasSarma, Roger Grosse,
Shauna Kravec, Yuntao Bai, Zachary Witten, Marina Favaro, Jan Brauner, Holden Karnofsky,
Paul Christiano, Samuel R. Bowman, Logan Graham, Jared Kaplan, Sören Mindermann, Ryan
Greenblatt, Buck Shlegeris, Nicholas Schiefer, and Ethan Perez. Sleeper agents: Training deceptive
LLMs that persist through safety training.arXiv preprint arXiv:2401.05566, 2024. URL https:
//arxiv.org/abs/2401.05566.
14

Mikkel Godsk Jørgensen and Lars Kai Hansen. Steering LLMs? actually, sparse autoencoders can
outperform simple baselines, 2026. URLhttps://arxiv.org/abs/2605.31183.
Adam Karvonen, Can Rager, Johnny Lin, Curt Tigges, Joseph Bloom, David Chanin, Yeu-Tong Lau,
Eoin Farrell, Callum McDougall, Kola Ayonrinde, Demian Till, Matthew Wearden, Arthur Conmy,
Samuel Marks, and Neel Nanda. SAEBench: A comprehensive benchmark for sparse autoencoders
in language model interpretability, 2025. URLhttps://arxiv.org/abs/2503.09532.
Ayan Antik Khan, Harsh Kohli, Yuekun Yao, Huan Sun, and Ziyu Yao. Can language model agents
be helpful circuit explainers in mechanistic interpretability?arXiv preprint arXiv:2606.24026,
2026. URLhttps://arxiv.org/abs/2606.24026.
Kimi Team. Kimi K3: Open Frontier Intelligence.arXiv preprint arXiv:2607.24653, 2026. URL
https://arxiv.org/abs/2607.24653.
Patrick Leask, Bart Bussmann, Michael Pearce, Joseph Bloom, Curt Tigges, Noura Al Moubayed,
Lee Sharkey, and Neel Nanda. Sparse autoencoders do not find canonical units of analysis. In
International Conference on Learning Representations, 2025. URL https://arxiv.org/
abs/2502.04878.
Tom Lieberum, Senthooran Rajamanoharan, Arthur Conmy, Lewis Smith, Nicolas Sonnerat, Vikrant
Varma, János Kramár, Anca Dragan, Rohin Shah, and Neel Nanda. Gemma scope: Open sparse
autoencoders everywhere all at once on gemma 2, 2024. URL https://arxiv.org/abs/
2408.05147.
Johnny Lin. Neuronpedia: Interactive Reference and Tooling for Analyzing Neural Networks, 2023.
URLhttps://www.neuronpedia.org. Software available from neuronpedia.org.
Yutian Liu, Xu Wang, and Difan Zou. Enhancing SAE-based steering via neighbor integrated feature
selection, 2026. URLhttps://arxiv.org/abs/2608.28806.
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The AI
Scientist: Towards Fully Automated Open-Ended Scientific Discovery, 2024. URL https:
//arxiv.org/abs/2408.06292.
Alisia Lupidi, Bhavul Gauri, Thomas Simon Foster, Bassel Al Omari, Despoina Magka, Alberto Pepe,
Alexis Audran-Reiss, Muna Aghamelu, Nicolas Baldwin, Lucia Cipolina-Kun, Jean-Christophe
Gagnon-Audet, Chee Hau Leow, Sandra Lefdal, Hossam Mossalam, Abhinav Moudgil, Saba Nazir,
Emanuel Tewolde, Isabel Urrego, Jordi Armengol Estape, Amar Budhiraja, Gaurav Chaurasia,
Abhishek Charnalia, Derek Dunfield, Karen Hambardzumyan, Daniel Izcovich, Martin Josifoski,
Ishita Mediratta, Kelvin Niu, Parth Pathak, Michael Shvartsman, Edan Toledo, Anton Protopopov,
Roberta Raileanu, Alexander Miller, Tatiana Shavrina, Jakob Foerster, and Yoram Bachrach. AIRS-
Bench: A suite of tasks for frontier AI research science agents.arXiv preprint arXiv:2602.06855,
2026. URLhttps://arxiv.org/abs/2602.06855.
Anas Mahmoud, MohammadHossein Rezaei, Mingchen Zhuge, Chenguang Wang, Yuandong Tian,
and Yunzhong He. Announcing RSI Bench. Scale AI, 2026. URL https://www.rsi-
benchmark.com/blog/announcing-rsi-bench.
Arnau Marin-Llobet and Javier Ferrando. Automated interpretability and feature discovery in
language models with agents, 2026. URLhttps://arxiv.org/abs/2605.01555.
Samuel Marks, Can Rager, Eric J. Michaud, Yonatan Belinkov, David Bau, and Aaron Mueller.
Sparse feature circuits: Discovering and editing interpretable causal graphs in language models,
2024. URLhttps://arxiv.org/abs/2403.19647.
Fanqing Meng, Lingxiao Du, Qiguang Chen, Ziqi Zhao, Haocheng Lu, Mengkang Hu, and
Michael Qizhe Shieh. RSIBench-Data: Benchmarking Data-Centric Research for Recursive
Self-Improvement.arXiv preprint arXiv:2607.25886, 2026. URL https://arxiv.org/
abs/2607.25886.
Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. Locating and editing factual
associations in GPT. InAdvances in Neural Information Processing Systems, volume 35, pp.
17359–17372, 2022.
Aaron Mueller, Atticus Geiger, Sarah Wiegreffe, Dana Arad, Iván Arcuschin, Adam Belfki, Yik Siu
Chan, Jaden Fried Fiotto-Kaufman, Tal Haklay, Michael Hanna, Jing Huang, Rohan Gupta,
Yaniv Nikankin, Hadas Orgad, Nikhil Prakash, Anja Reusch, Aruna Sankaranarayanan, Shun
Shao, Alessandro Stolfo, Martin Tutek, Amir Zur, David Bau, and Yonatan Belinkov. MIB: A
mechanistic interpretability benchmark. InProceedings of the 42nd International Conference on
Machine Learning, volume 267 ofProceedings of Machine Learning Research, pp. 45069–45108,
2025. URLhttps://proceedings.mlr.press/v267/mueller25a.html.
15

Gonçalo Paulo and Nora Belrose. Evaluating SAE interpretability without explanations, 2025. URL
https://arxiv.org/abs/2507.08473.
Gonçalo Santos Paulo, Alex Troy Mallen, Caden Juang, and Nora Belrose. Automatically interpreting
millions of features in large language models. InProceedings of the 42nd International Conference
on Machine Learning, volume 267 ofProceedings of Machine Learning Research, pp. 48393–
48421, 2025. URLhttps://proceedings.mlr.press/v267/paulo25a.html.
Senthooran Rajamanoharan, Tom Lieberum, Nicolas Sonnerat, Arthur Conmy, Vikrant Varma, János
Kramár, and Neel Nanda. Jumping ahead: Improving reconstruction fidelity with JumpReLU
sparse autoencoders, 2024. URLhttps://arxiv.org/abs/2407.14435.
Ben Rank, Hardik Bhatnagar, Ameya Prabhu, Shira Eisenberg, Karina Nguyen, Matthias Bethge, and
Maksym Andriushchenko. PostTrainBench: Can LLM Agents Automate LLM Post-Training?,
2026. URLhttps://arxiv.org/abs/2603.08640.
Tamar Rott Shaham, Sarah Schwettmann, Franklin Wang, Achyuta Rajaram, Evan Hernandez, Jacob
Andreas, and Antonio Torralba. A multimodal automated interpretability agent. InProceedings of
the 41st International Conference on Machine Learning, volume 235 ofProceedings of Machine
Learning Research, pp. 44293–44321, 2024. URL https://proceedings.mlr.press/
v235/shaham24a.html.
Abhay Sheshadri, Aidan Ewart, Kai Fronsdal, Isha Gupta, Samuel R. Bowman, Sara Price, Samuel
Marks, and Rowan Wang. AuditBench: Evaluating alignment auditing techniques on models with
hidden behaviors, 2026. URLhttps://arxiv.org/abs/2602.22755.
Dong Shu, Xuansheng Wu, Haiyan Zhao, Mengnan Du, and Ninghao Liu. Beyond input acti-
vations: Identifying influential latents by gradient sparse autoencoders. InProceedings of the
2025 Conference on Empirical Methods in Natural Language Processing, pp. 1673–1682. As-
sociation for Computational Linguistics, 2025. doi: 10.18653/v1/2025.emnlp-main.87. URL
https://aclanthology.org/2025.emnlp-main.87/.
Joar Skalse, Nikolaus Howe, Dmitrii Krasheninnikov, and David Krueger. Defining and characterizing
reward hacking.Advances in Neural Information Processing Systems, 35:9460–9471, 2022.
Ran Song, Shizhu He, Shuting Jiang, Yantuan Xian, Shengxiang Gao, Kang Liu, and Zhengtao
Yu. Does large language model contain task-specific neurons? InProceedings of the 2024
Conference on Empirical Methods in Natural Language Processing, pp. 7101–7113. Association
for Computational Linguistics, 2024. doi: 10.18653/v1/2024.emnlp-main.403. URL https:
//aclanthology.org/2024.emnlp-main.403/.
Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin, Rachel
Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia Glaese, and
Tejal Patwardhan. PaperBench: Evaluating AI’s Ability to Replicate AI Research, 2025. URL
https://arxiv.org/abs/2504.01848.
Yuqiao Tan, Jinxiang Meng, Fangyu Lei, Minzheng Wang, Shizhu He, Jun Zhao, and Kang Liu.
SWE-Touch: Benchmarking coding agents when users touch the code, 2026a. URL https:
//arxiv.org/abs/2608.02499.
Yuqiao Tan, Minzheng Wang, Shizhu He, Jun Zhao, and Kang Liu. PostTrainBench 0: Can LLM
Agents Automate LLM Post-Training Without Gradients? Research blog, 2026b. URL https:
//trae1oung.github.io/posttrainbench0/.
Adly Templeton, Tom Conerly, Jonathan Marcus, Jack Lindsey, Trenton Bricken, Brian
Chen, Adam Pearce, Craig Citro, Emmanuel Ameisen, Andy Jones, Hoagy Cunningham,
Nicholas L Turner, Callum McDougall, Monte MacDiarmid, Alex Tamkin, Esin Durmus,
Tristan Hume, Francesco Mosconi, C. Daniel Freeman, Theodore R. Sumers, Edward Rees,
Joshua Batson, Adam Jermyn, Shan Carter, Chris Olah, and Tom Henighan. Scaling
monosemanticity: Extracting interpretable features from Claude 3 Sonnet.Transformer Cir-
cuits Thread, 2024. URL https://transformer-circuits.pub/2024/scaling-
monosemanticity/index.html.
Constantin Venhoff, Anisoara Calinescu, Philip Torr, and Christian Schroeder de Witt. SAGE:
Scalable ground truth evaluations for large sparse autoencoders, 2024. URL https://arxiv.
org/abs/2410.07456.
Kevin Wang, Alexandre Variengien, Arthur Conmy, Buck Shlegeris, and Jacob Steinhardt. Inter-
pretability in the wild: A circuit for indirect object identification in GPT-2 small.arXiv preprint
arXiv:2211.00593, 2022. URLhttps://arxiv.org/abs/2211.00593.
16

Xu Wang, Yan Hu, Benyou Wang, and Difan Zou. Does higher interpretability imply better utility? a
pairwise analysis on sparse autoencoders. InInternational Conference on Learning Representations,
2026a. URLhttps://openreview.net/forum?id=5KY99GFqZD.
Zhen Wang, Fan Bai, Zhongyan Luo, Jinyan Su, Kaiser Sun, Xinle Yu, Jieyuan Liu, Kun Zhou,
Claire Cardie, Mark Dredze, Zhiting Hu, and Eric P. Xing. FIRE-Bench: Evaluating agents on
the rediscovery of scientific insights.arXiv preprint arXiv:2602.02905, 2026b. URL https:
//arxiv.org/abs/2602.02905.
Zhengxuan Wu, Aryaman Arora, Atticus Geiger, Zheng Wang, Jing Huang, Dan Jurafsky, Christo-
pher D. Manning, and Christopher Potts. AxBench: Steering LLMs? even simple baselines
outperform sparse autoencoders. InProceedings of the 42nd International Conference on Machine
Learning, volume 267 ofProceedings of Machine Learning Research, pp. 67035–67080, 2025.
URLhttps://proceedings.mlr.press/v267/wu25a.html.
Lei Xiong, Kun Luo, Ziyi Xia, Wenbo Zhang, Jin-Ge Yao, Zheng Liu, Jingying Shao, Jianlyu Chen,
Hongjin Qian, Xi Yang, Qian Yu, Hao Li, Chen Yue, Xiaan Du, Yuyang Wang, Yesheng Liu, Haiyu
Xu, and Zhicheng Dou. AutoResearchBench: Benchmarking AI agents on complex scientific
literature discovery.arXiv preprint arXiv:2604.25256, 2026. URL https://arxiv.org/
abs/2604.25256.
Wanghan Xu, Shuo Li, Tianlin Ye, Qinglong Cao, Yixin Chen, Hengjian Gao, Yiheng Wang, Qi Li,
Kun Li, Sheng Xu, Shengdu Chai, Fangchen Yu, Xiangyu Zhao, Zhangrui Zhao, Weijie Ma,
Zijie Guo, Koutian Wu, Haoyu Zhou, Haoxiang Yin, Lixue Cheng, Chaofan Hu, Haoxuan Li,
Lu Mi, Xuxuan Xie, Yifan Zhou, Ruizhe Chen, Zhiwang Zhou, Xingjian Guo, Yuhao Zhou,
Xuming He, Shengyuan Xu, Xinyu Gu, Jiamin Wu, Mianxin Liu, Chunfeng Song, Fenghua Ling,
Dongzhan Zhou, Shixiang Tang, Yuqiang Li, Mao Su, Peng Ye, Siqi Sun, Bin Wang, Xue Yang,
Zhenfei Yin, Tianfan Fu, Guangtao Zhai, Wanli Ouyang, Bo Zhang, Lei Bai, and Wenlong Zhang.
ResearchClawBench: A benchmark for end-to-end autonomous scientific research.arXiv preprint
arXiv:2606.07591, 2026. URLhttps://arxiv.org/abs/2606.07591.
Zeping Yu and Sophia Ananiadou. Neuron-level knowledge attribution in large language models. In
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp.
3267–3280. Association for Computational Linguistics, 2024. doi: 10.18653/v1/2024.emnlp-main.
191. URLhttps://aclanthology.org/2024.emnlp-main.191/.
Jenny Zhang, Shengran Hu, Cong Lu, Robert Lange, and Jeff Clune. Darwin Gödel Machine:
Open-Ended Evolution of Self-Improving Agents. InInternational Conference on Learning
Representations, 2026. URLhttps://arxiv.org/abs/2505.22954.
17

A TASKS ANDEXPERIMENTALPROTOCOL
The appendix follows the experiment from task construction to agent investigation, activation testing,
and generated outputs. Task and feature identifiers are retained in measurement tables to make the
records traceable. The narrative describes candidates by their observed responses.
A.1 TASKINVENTORY
The benchmark uses 20 concept–layer tasks and 17 concepts. Earnings reports, portfolio allocation,
and tax filing each occur at both layers. An Expert ID is local to its stated SAE checkpoint. Cru-
cially, all 20 Expert features serve as frozen reference baselines: where public steering presets are
documented on Neuronpedia (Lin, 2023) alongside Gemma Scope (Lieberum et al., 2024) (e.g., Cat),
they are adopted directly; for remaining concepts, features are validated via standard expert curation
workflows as detailed below.
Table 4: Task concepts and Expert IDs. Each SAE contains 131,072 features.
Layer Concept Expert ID
20 archaeological excavation 7256
9 cat 62610
20 clinical symptom reports 3927
9 earnings reports 131024
20 earnings reports 100747
9 French 105738
9 gardening advice 93406
9 German 33987
9 job postings 91086
9 Latin 7659
20 pharmaceutical dosing 104583
9 portfolio allocation 77390
20 portfolio allocation 101617
9 Portuguese 41424
20 real estate listings 27182
9 Spanish 94329
9 tax filing language 18713
20 tax filing language 78694
9 Turkish 99383
20 weather forecasts 44494
A.2 EXPERTCONSTRUCTION ANDEVALUATIONREUSE
The Expert features serve as established reference baselines, directly adopted from public Neuronpedia
presets where available (e.g., Cat originates from Neuronpedia’s primary steering preset). For
the remaining tasks, candidate features were validated using standard expert curation workflows:
candidates were retrieved from six positive and six negative construction probes, then verified on
eight positive, eight hard-negative, and four neutral texts to confirm concept fidelity. All Expert IDs
occur in the retained validation records, and their activation case lists and matching metrics are fully
traceable.
The evaluation texts are unavailable to agents but were used during Expert construction. Because
Expert features represent canonical, pre-identified directions from official presets and verified work-
flows, they provide an objective, fixed reference point rather than an artificially tuned competitor.
Gemma Scope supplies the SAE checkpoints, and Neuronpedia documents their features. The text
suites and Expert selection procedure are specified here as benchmark components. The unified
Expert steering evaluation regenerates answers using the task’s frozen scale and the common 4o
18

judge. Rank compares against Expert. Activation and Steering use each feature’s measurements
directly.
A.3 AGENTCONFIGURATIONS ANDREPEATEDRUNS
Table 5: Agent models and execution harnesses.
Agent Harness Model identifier
Claude Opus 5 Cursorclaude-opus-5-thinking-high
Claude Sonnet 5 Cursorclaude-sonnet-5-thinking-high
Kimi K3 Cursorkimi-k3-high
Claude Opus 4.8 Cursorclaude-opus-4-8-thinking-high
Grok 4.6 Cursorcursor-grok-4.6-high
Gemini 3.8 Flash Cursorgemini-3.8-flash-high
GPT-5.6 Sol Codexgpt-5.6-sol
GPT-5.5 Cursorgpt-5.5-high
GLM-5.2 Cursorglm-5.2-high
GPT-5.6 Luna Codexgpt-5.6-luna
Each configuration has 60 scored episodes, covering three investigations of each task. Cursor model identi-
fiers encode the high reasoning setting. Codex receives an explicitreasoning_effort=highargument.
Each configuration contributes three complete runs over 20 tasks. Failed attempts (e.g., tool syntax
errors) are replaced by retries, with exactly one scored result per episode. Agents interact with the
environment using identical task specifications, probe interfaces, a dedicated writable workspace,
and disabled network access. Cursor and Codex traces are audited to ensure full compliance. The
evaluation runner applies a standard 60-minute execution timeout per task.
A.4 METRICDEFINITIONS ANDWORKEDEXAMPLE
Benchmark scores implement Equations 3–6. Text activations pool the three largest non-special-token
responses. AUROC credits ties at half a point against pooled hard-negative and neutral controls.
Table 6: Component scores for GPT-5.6 Sol’s Portuguese selection.
Measurement or score
 GPT-5.6 Sol: 49607 Expert: 41424
Mean positive rank 642.625 13.000
AUROC 1.000 1.000
Target Effect 0.8875 0.8500
Rank 3.97 100.00
Activation 100.00 100.00
Steering 88.75 85.00
Overall 64.24 95.00
The score export records all 600 episodes, including raw activation ranks, AUROC, and Target Effect,
preserving each run and submitted feature ID. Exact ID recovery is reported as a separate diagnostic.
Table 6 provides a worked step-by-step calculation illustrating how these metrics are evaluated for
both Expert and agent submissions.
A.5 EXPERIMENTACCOUNTING
In total, the benchmark archive contains 600 scored episodes, 4,873 probe calls, and 49,407 text
entries across the evaluated agents. Steering evaluation covers 124 task–direction pairs and 10,940
19

generations across calibration and final evaluation, evaluated over two independent passes by GPT-4o
(yielding 14,880 condition ratings).
A.6 STEERINGGENERATIONPROTOCOL
Table 7: Frozen generation and steering settings. Counts refer to one task–direction evaluation unless
stated otherwise.
Setting Value
Generatorgoogle/gemma-2-9b-itwith greedy decoding
Intervention AddαW dec[f,:]at every token position
Expert scale Frozen taskα E. Values across the 20 tasks:{45,60,120,160,240}
Alternative scale grid{0.5,0.75,1,1.25,1.5}α E. If none yields at least 90% non-degenerate
calibration outputs, try{0.0625,0.125,0.25,0.375}α E
Calibration data 5 prompts per attempted scale. Deterministic cue score only
Scale tie-break Cue success rate, then mean cue score, then smallerα
Evaluation data 20 instructions with baseline, feature, and matched-random generation
for each
Generation length 64 tokens for 15 tasks, 128 for 4 language tasks, and 192 for the cat task
Random control Seed-0 Gaussian vector rescaled to the submitted decoder row’s norm
Judge 4o, two separately shuffled passes, temperature 0
Scale selection and final scoring.To enable fair causal comparison while preventing output de-
generation, the evaluator calibrates the intervention strength α for each submitted feature using
a principled grid search on held-out calibration prompts prior to benchmark scoring. Expert fea-
tures retain their frozen task reference scale αE (Table 7), adopting Neuronpedia’s public steering
preset for Cat and established task calibration scales for remaining tasks. For agent-submitted
alternative features, the pipeline searches over the layer-specific candidate grid in Table 7 (e.g.,
α∈ {80,120,160,200,240}for Layer 9).
The calibration selectsαvia a three-stage filter on five held-out calibration prompts:
1. Non-degeneration filter:The candidate scale must yield ≥90% non-degenerate genera-
tions (all 5 calibration outputs must pass coherence and formatting checks without repetitive
loops).
2. Target cue optimization:Among retained scales passing the degeneration check, the scale
maximizing the target keyword cue success rate (and tie-broken by mean cue score) is
selected.
3. Minimal perturbation tie-break:If multiple scales achieve identical target cue perfor-
mance without degeneration, the smallerα is preferred to minimize unnecessary perturbation
of the representation space.
The selected scale is then frozen and applied across all 20 final evaluation instructions. The norm-
matched random direction control uses the identical calibrated scale. Intervention scales for selected
generation cases appear in Table 21.
A.7 STEERINGEVALUATIONRUBRIC ANDJUDGEPROMPTS
An automated GPT-4o judge evaluates steered completions against the user instruction and target
concept. To ensure blinded and impartial evaluation, the judge receives the generation instruction
along with three candidate completions labeled A, B, and C in pseudo-randomized order, concealing
whether an output originated from baseline inference, the submitted SAE feature intervention, or the
norm-matched random-direction control.
For each completion, the judge independently assigns:
20

•Target Relevance (0–4):Quantifies the degree to which the target concept is induced (0 =
none, 1 = weak, 2 = implicit, 3 = explicit, 4 = dominant).
• Task Preservation (0–4):Measures adherence to original constraints (e.g., formatting,
length, answering user queries).
• Degeneration (Boolean):Flags severe output collapse, such as repetitive token loops or
incoherent formatting.
Ratings are averaged across the 20 evaluation prompts and two independent evaluation passes per
prompt at temperature 0, with strict JSON output formatting. The complete system prompt, user
prompt template, and concept-specific scoring criteria are detailed below.
Judge messages.The templates below reproduce the scoring instructions. Angle-bracket fields are
replaced by the concept criteria, generation prompt, and three answers. Line wrapping is adjusted for
display. The user message requests one rating for each of A, B, and C.
System prompt
You are evaluating activation steering for one SAE feature.
The intended concept is<concept>.
For each candidate output, independently score:
- target_relevance (0-4):
0 none;
1 weak or ambiguous evidence;
2 implicit but recognizable target content;
3 explicit target content or multiple specific cues;
4 dominant and repeated target content.
- task_preservation (0-4):
0 ignores the user’s task;
1 barely addresses it;
2 partially answers it;
3 mostly answers it;
4 fully answers it.
- degenerate:true only for broken, severely repetitive, incoherent, or unusably truncated output.
Strong target evidence:<strong_evidence>
Do not count as sufficient evidence:<insufficient_evidence>
Return strict JSON only:
{
"ratings": [{
"label": "A", "target_relevance": 0,
"task_preservation": 0, "degenerate": false,
"reason": "short reason"
}]
}
User prompt
User task:
<evaluation_prompt>
Output A:<answer_A>
Output B:<answer_B>
Output C:<answer_C>
Evaluate every output above exactly once. Return exactly three ratings with labels A, B, and C; do not
omit, rename, or add labels.
Concept criteria.Table 8 gives the exact values inserted into the system message. The three concepts
evaluated at both SAE layers use the same wording at each layer.
21

Table 8: Concept-specific criteria in the steering judge’s system message.
Concept Strong target evidence Insufficient evidence
domestic-cat or feline
identity and behavior
explicit cat or feline identity, or
multiple specific cues such as
meowing, purring, whiskers, litter
boxes, paws, claws, tabby, or calico
generic words such as animal, owner,
elegant, mysterious, independent, queen,
fur, or tail alone
coherent
French-language output
most of the answer is grammatical
French rather than isolated French
words
mentions of France, French names, or a
few borrowed French words
coherent grammatical
Spanish-language
output
most of the answer is connected
grammatical Spanish
Spanish names, places, borrowed words,
or nearby Portuguese and Italian text
coherent grammatical
Portuguese-language
output
most of the answer is connected
grammatical Portuguese
Portuguese names, places, borrowed
words, or nearby Spanish and Italian
text
coherent grammatical
German-language
output
most of the answer is connected
grammatical German
German names, places, borrowed words,
or English discussion of German
corporate earnings
results
company financial results, profit
metrics, margins, guidance, or cash
generation
stock commentary, executive profiles,
product launches, or accounting lessons
without earnings results
practical gardening
advice
hands-on garden care guidance about
planting, watering, pruning, soil,
compost, or growing conditions
botanical exhibits, cut flowers,
landscaping design, biology lessons,
weather, or cooking herbs without care
advice
tax filing and taxable
income
filing instructions or calculations
involving returns, taxable income,
credits, deductions, or forms
budget policy, accountants, general
finance, or taxes mentioned without
filing substance
job advertisement employment ad language naming a
role, responsibilities, qualifications,
compensation, benefits, or application
steps
career advice, resumes, hiring trends,
layoffs, employee policy, or recruiting
events without a posting
coherent
Latin-language output
most of the answer is connected
grammatical Latin
Roman names, isolated mottos, or
English discussion of Latin
investment portfolio
allocation
asset weights, diversification decisions,
rebalancing rules, or risk positioning
across holdings
single-stock news, account setup,
market commentary, or personal
budgeting without allocation
coherent grammatical
Turkish-language
output
most of the answer is connected
grammatical Turkish
Turkish names, places, isolated words,
or English discussion of Turkey
clinical symptom
presentation
specific patient complaints, onset,
severity, associated symptoms, or
clinical presentation
general health discussion, hospital
operations, or medical terms without
a patient symptom narrative
medication dosing
instructions
drug administration instructions with
amount, route, timing, or frequency
drug names, pharmacy logistics, or
treatment discussion without dosing
instructions
real estate property
listing
property advertisement details about
rooms, amenities, price, location, rent,
or showing information
housing policy, renovation stories,
mortgage discussion, architecture plans,
or neighborhood descriptions without a
listing
weather forecast
wording
predicted future conditions such as
precipitation, temperature, wind,
clouds, or timing
climate analysis, past storm damage,
generic weather interest, or radar display
without prediction
archaeological
excavation evidence
field excavation context with artifacts,
layers, trenches, dating, site grids, or
occupation phases
museums, history documentaries,
ruins tourism, construction digging,
or heritage policy without excavation
evidence
22

B AGENTINVESTIGATIONS
We first compare how agents retrieve and test candidates, then follow the evidence behind Portuguese,
clinical, and real-estate selections. Complete authored inputs and evaluation measurements follow in
Appendix C.
B.1 RETRIEVAL, DIRECTTESTS,ANDSUBMISSION
Figure 7 distinguishes whether each agent encounters Expert, directly tests it, and ultimately selects
it. This separates candidate availability from the decision to evaluate or submit a feature.
Claude
Opus 5
Claude
Sonnet 5
Kimi K3 Claude
Opus 4.8
Grok 4.6 Gemini 3.8
Flash
GPT-5.6
Sol
GPT-5.5 GLM-5.2 GPT-5.6
Luna
0
25
50
75
100
Episodes (%)
Expert selected
Tested; another selected
Returned; not tested
Not encountered
Figure 7: Per-agent search outcomes across 60 episodes each. Returned means the Expert is present
in the recorded candidate set; tested means it was directly requested. Each episode belongs to one
segment.
Claude Opus 5 and Claude Sonnet 5 select the Expert in 25 and 24 episodes. Opus 5 tests it but
selects another direction in 27 episodes, versus nine for Sonnet 5. Sonnet 5 encounters it without
testing in 21 episodes, versus five for Opus 5. Opus more often compares Expert directly before
choosing an alternative, while Sonnet more often selects from the retrieved candidates without an
explicit Expert test.
B.2 EXTENDEDAGENTINVESTIGATIONS
The following cases follow probe design, candidate comparison, and selection. Candidate descriptions
refer to observed responses on the stated tests. Measurement tables retain the feature IDs for cross-
checking.
Finding a candidate beyond the first retrieval.Table 9 follows GPT-5.6 Sol’s Portuguese inves-
tigation. Sol begins by retrieving the top 80 features on eight Portuguese passages. The strongest
response on the first passage is 50.58, but its eventual selection appears in none of these eight lists.
Sol expands retrieval to the top 500 and directly compares candidates using new texts. The expanded
request is recorded, and Sol’s report supplies the result of that offloaded stage. Subsequent direct
comparisons provide measured responses for the shortlisted candidates.
Testing what an activation means.Sol’s ninth probe compares three candidates on six contrasting
inputs (Table 11). One candidate responds strongly to a Portuguese Sunday passage (33.83) but
remains inactive on a restaurant request, whereas Sol’s final selection responds consistently to
both (7.04 and 6.62), demonstrating better topical coverage. In contrast, an English description of
Portuguese strongly activates Expert (33.67) but leaves Sol’s candidate inactive (0.00). Similarly, a
Spanish control activates a Sunday-responsive candidate at 7.02 but leaves Sol’s candidate inactive.
23

Table 9:
 GPT-5.6 Sol’s Portuguese investigation.
Probe Experiment Recorded observation
1 Retrieve top-80 features on
Portuguese passages from
different topics.
On the first passage, 111414 leads at 50.58. Final choice 49607 is
absent from all eight returned lists.
7 Expand to top-500 with
Portuguese texts, translations,
and terminology controls.
The 36-text request is recorded. Sol reports that 49607 appeared
on nine of twelve Portuguese lists. This stage’s response was
offloaded.
8–10 Compare candidates across
topic, language, vocabulary,
and orthography.
Probe 9 measures 68458 at 33.83 on one passage and zero on a
restaurant request. Feature 49607 responds to both at 7.04 and
6.62.
11 Extend two short
Portuguese phrases and test
vocabulary-only controls.
A thank-you sequence rises from 1.01 to 8.48. A word list scores
2.58. The final submission is 49607.
The selected feature also shows mild activation on Galician (4.19) and a Portuguese vocabulary list
(5.04).
Sol’s final probe examines whether this feature fires on isolated words or extended syntax: expanding
a short thank-you phrase into a full sentence raises activation from 1.01 to 8.48, while a raw word list
yields only 2.58 and English commentary yields 2.63 (Figure 8).
Opus 4.8 performs a complementary cross-lingual test: a French passage about Brazil activates Expert
strongly at 45.58 but leaves its candidate inactive, while a Portuguese passage activates both at 10.02
and 11.94. The French control preserves the regional topic while changing language, verifying that
the candidate fires on language rather than topic cues. Both agents thus leverage contrastive probes to
identify features with high empirical selectivity.
Rejecting candidates for different reasons.GLM-5.2’s clinical investigation demonstrates sys-
tematic candidate filtering across three contrastive probes (detailed in Appendix Table 14). A generic
medical candidate fires strongly across hospital administration, pharmacology, and symptoms alike. A
second candidate fires on headache but completely misses sore throat, revealing a coverage defect. A
third candidate fires more strongly on a non-medical customer complaint than on genuine symptoms,
exposing spurious wording triggers. GLM’s selected feature responds consistently to both symptoms
while suppressing these controls. However, patient history formatting still triggers an activation of
70.25, showing that non-symptom clinical formatting remains a confounder.
How agents resolve competing candidates.Real-estate listings provide a direct comparison
of candidate trade-offs across agents (Table 10). Sol tests matched listing and non-listing pairs,
while Grok uses housing ablations to reject candidate 84434 for broad activations on non-housing
ads, both deliberately selecting the cleaner candidate 17219. In contrast, Kimi K3 prioritizes
broad listing coverage and accepts 84434 despite minor control leakages. While 84434 achieves
slightly higher AUROC (1.000 vs. 0.917) and Target Effect (0.944 vs. 0.900), it causes severe
downstream degeneration, collapsing on 52.5% of outputs compared with 32.5% for 17219. Across
nine independent runs across three models, candidate 17219 is preferred in seven instances, illustrating
how agents trade off feature purity against downstream output stability.
24

Table 10:Real-estate candidate trade-offs and evaluation.Top: Search strategies of Sol, Grok
4.6, and Kimi K3 during candidate exploration. Bottom: Retrospective benchmark evaluation of
competing features (17219 vs. 84434) and Expert 27182 across nine independent runs.
Search methodology and authored controls across agents
Agent Selected Feature Probes Search Methodology and Rejection Criteria
GPT-5.6 Sol 17219 6 Eight matched listing/non-listing pairs; controls span vehicles,
hospitality, policy, architecture, mortgages; rejects leakier
candidate 84434.
Grok 4.6 17219 7 Listing intersections, commercial ads, housing ablations;
explicitly rejects 84434 due to broad activation on
non-housing ads.
Kimi K3 84434 6 Four iterative rounds with 14 listing probes, named negatives,
and edge cases; prioritizes broad coverage despite minor
control leakage.
Benchmark evaluation and downstream generation quality of competing features
Feature ID Chosen Count AUROC Target Effect Preservation Degeneration Correlation w/ Expert
Expert 27182 0 / 9 1.000 0.394 0.500 — 1.000
Feature 17219 7 / 9 0.917 0.900 1.100 32.5% 0.427
Feature 84434 1 / 9 1.000 0.944 1.100 52.5% 0.343
C PROBETEXTS ANDACTIVATIONEVIDENCE
C.1 MEASUREMENTSBEHIND THEINVESTIGATIONCASES
The tables record the authored tests behind the search decisions. Source labels distinguish original
measurements, agent reports, and replayed requests. Feature IDs identify dictionary entries within
the stated task and SAE layer.
25

Table 11: Language, topic, and coverage tests in Sol’s ninth Portuguese probe. Columns show Expert
and the features selected by Luna and Sol. Values are top-three-token mean activations on Sol’s full
inputs. Prose entries show their first sentence, and the word list is complete. Appendix C.2 provides
the full inputs.
Authored contrast Expert
 Luna
 Sol
Feature ID 41424 68458 49607
Portuguese passage
Nas manhãs de domingo, costumo abrir as janelas e ouvir os pássaros
enquanto preparo o café.
20.96 33.83 7.04
Portuguese request
Bom dia, gostaria de reservar uma mesa para quatro pessoas.
26.810.006.62
English about Portuguese
Portuguese is a Romance language spoken by millions of people.
33.67 3.380.00
Spanish translation
Los domingos por la mañana, suelo abrir las ventanas y escuchar a los
pájaros mientras preparo el café.
0.007.020.00
Galician translation
Nas mañás do domingo, adoito abrir as fiestras e escoitar os paxaros mentres
preparo o café.
8.62 28.92 4.19
Portuguese word list
De manhã domingo pássaros janela café jornal mãe abrir ouvir preparar ler
telefonar.
23.080.005.04
Table 12:Probing traces from
 Claude Opus 5 on Cat and Tax Filing tasks.Contrastive probe
texts expose candidate feature sensitivities: string-level matching (19127) vs. true semantic concept
(62610), and specialized filing forms (64827) vs. broader tax concept (18713).
Probe Excerpt & Context Candidate ID Activation Dict Rank
Cat Task (Layer 9)|Target: Feline animal|Neuronpedia Expert: 62610
Positive (Feline context):My cat sleeps on the windowsill 19127 32.92 1
62610 (Expert) 30.96 3
2662 19.88 9
String distractor:Copycat killer 19127 44.00 1
62610 (Expert) 1.27 6,800
Compound distractor:Catalytic converter 19127 24.54 5
62610 (Expert) 0.00 inactive
Cat anatomy / behavior:Whiskers twitch, pouncing on laser
dot
2662 43.83 1
62610 (Expert) 27.17 5
Purring / coat pattern:Soft purr, beautiful tortoiseshell
markings
62610 (Expert) 45.92 2
2662 5.49 474
Tax Filing Task (Layer 9)|Target: Income tax filing|Neuronpedia Expert: 18713
Income threshold:Below the filing threshold 64827 58.00 1
18713 (Expert) 9.12 172
Form Schedule A:Schedule A itemized deductions 64827 46.92 2
18713 (Expert) 32.83 3
Form 4868:Form 4868 automatic extension of time 64827 46.75 2
18713 (Expert) 0.90 17,690
Negative control:Local property tax rate assessment 64827 1.12 10,614
18713 (Expert) 0.00 inactive
26

C.2 COMPLETEAUTHOREDPROBEINPUTS
Table 2 in the main paper presents key probe comparisons across agents. Here, Table 13 provides the
complete, structured inventory of authored probe inputs across the four Portuguese investigations
(Sol, Claude Opus 4.8, Claude Opus 5, and Kimi K3), organized by probe round and contrastive
hypothesis.
Table 13:Complete authored probe texts across four agent investigations (Portuguese, Layer 9).
This table details the exact inputs authored by Sol, Claude Opus 4.8, Claude Opus 5, and Kimi K3,
categorized by probe round and contrastive hypothesis.
Agent & Probe # Contrast Type Full Authored Input Text
GPT-5.6 Sol(Probe 9|Submitted: 49607|Expert: 41424)
Sol (Probe 9) Portuguese (Target) Nas manhãs de domingo, costumo abrir as janelas e ouvir
os pássaros enquanto preparo o café. Depois leio o jornal e
telefono para minha mãe.
Sol (Probe 9) Portuguese Request Bom dia, gostaria de reservar uma mesa para quatro pes-
soas. Há algum horário disponível depois das oito da
noite?
Sol (Probe 9) English (About Pt) Portuguese is a Romance language spoken by millions
of people. Brazil has the largest number of Portuguese
speakers, while Portugal is where the language developed.
Sol (Probe 9) Spanish Translation Los domingos por la mañana, suelo abrir las ventanas y
escuchar a los pájaros mientras preparo el café. Depois leo
el periódico y llamo a mi madre.
Sol (Probe 9) Galician Translation Nas mañás do domingo, adoito abrir as fiestras e escoitar
os paxaros mentres preparo o café. Despois leo o xornal e
chamo á miña nai.
Sol (Probe 9) Word List De manhã domingo pássaros janela café jornal mãe abrir
ouvir preparar ler telefonar.
Claude Opus 4.8(Probe 9|Submitted: 27283|Expert: 41424)
Opus 4.8 (Probe 9) Portuguese (Target) O meu vizinho comprou um carro novo e todos os dias sai
muito cedo para o trabalho na cidade vizinha.
Opus 4.8 (Probe 9) French (About Brazil) Le Brésil est le plus grand pays d’Amérique du Sud et sa
capitale est Brasilia, une ville moderne.
Opus 4.8 (Probe 9) Spanish Translation Mi vecino compró un coche nuevo y todos los días sale
muy temprano para el trabajo en la ciudad vecina.
Claude Opus 5(Probe 5|Submitted: 114418|Expert: 41424)
Opus 5 (Probe 5) Portuguese (Target) Hoje de manhã fui à padaria comprar pão fresco e um
café. O tempo estava agradável, com uma brisa leve que
vinha do rio. Depois voltei para casa e li o jornal enquanto
tomava o pequeno-almoço.
Opus 5 (Probe 5) Spanish Translation Esta mañana fui a la panadería a comprar pan fresco y un
café. El tiempo estaba agradable, con una brisa ligera que
venía del río. Luego volví a casa y leí el periódico mientras
desayunaba.
Opus 5 (Probe 5) English Translation This morning I went to the bakery to buy fresh bread and
a coffee. The weather was pleasant, with a light breeze
coming from the river. Afterwards I returned home and
read the newspaper while having breakfast.
Kimi K3(Probes 1–4|Submitted: 41424|Expert: 41424)
Kimi (Probe 1) Portuguese (Target) Ontem fui ao mercado comprar frutas e legumes frescos. A
feira estava cheia de gente, e os preços estavam bem mais
baratos do que no supermercado. Aproveitei para conversar
com a vendedora sobre a colheita deste ano.
Kimi (Probe 2) English Translation Yesterday I went to the market to buy fresh fruits and
vegetables. The fair was full of people, and the prices were
much cheaper than at the supermarket.
27

Agent & Probe # Contrast Type Full Authored Input Text
Kimi (Probe 2) Spanish Translation Ayer fui al mercado a comprar frutas y verduras frescas. La
feria estaba llena de gente, y los precios eran mucho más
baratos que en el supermercado.
Kimi (Probe 2) English (About Portugal) Portugal is a country in southwestern Europe known for its
beaches, wine, and maritime history. Many tourists visit
Lisbon and Porto every year to enjoy the local cuisine and
architecture.
Kimi (Probe 3) Meeting Postponed A reunião foi adiada para a próxima terça-feira porque o di-
retor está viajando a negócios. Todos os participantes serão
notificados por e-mail com a nova pauta e os documentos
atualizados.
Kimi (Probe 4) Catalan Control Ahir vaig anar al mercat a comprar fruites i verdures
fresques. La fira estava plena de gent i els preus eren molt
més barats que al supermercat.
Kimi (Probe 4) Galician Translation Onte fun ao mercado a mercar froitas e verduras frescas.
A feira estaba chea de xente e os prezos eran moito máis
baratos ca no supermercado.
Kimi (Probe 4) English with Pt Quote I was reading a Brazilian novel yesterday. The phrase “ela
atravessava a ponte velha” appeared in the first chapter,
which my teacher translated for the class.
In its final investigation report, Kimi K3 explicitly details its rejection rationale for competing
candidates: it rejects candidate 19127 because it activates strongly across languages (activating at
35.33 on the English market probe and 39.75 on the Spanish probe, compared to 0.00 and 1.80 for its
final selection 41424). It also rejects candidate 85098 due to broad leakage onto Catalan (activating
at 26.92 vs. 0.71). Kimi’s final selection 41424 is identical to Neuronpedia Expert.
C.3 DETAILEDCASEINPUTS
Table 14 provides the complete GLM-5.2 diagnostic probes, illustrating how the agent attempted to
isolate clinical symptoms from hospital bureaucracy, drug mechanisms, and non-symptom patient
history formatting.
28

Table 14:Complete GLM-5.2 contrastive probes for Clinical Symptom discovery (Layer 20).
Probes 2–4 tested competing hypotheses to disentangle disease symptoms from medical bureaucracy,
pharmacology, and clinical document format.
Label & Probe # Hypothesis Tested Full Authored Input Text
Headache (Probe 2) Target Symptom (Neurology) A 28-year-old woman presents with a
2-week history of daily throbbing headaches,
photophobia, and nausea. The pain is bilateral,
frontal, worse in the mornings, and rates 6/10.
She reports no prior similar episodes. Her
mother has a history of migraines.
Hospital (Probe 2) Distractor (Hospital Admin) The hospital administration announced a
new policy for scheduling operating rooms,
effective next quarter. Surgeons must submit
block time requests through the electronic
scheduling system. The committee reviewed
throughput metrics, bed occupancy rates, and
length of stay averages across all departments.
Drug (Probe 2) Distractor (Pharmacology) Pharmacokinetic studies demonstrate that
metformin is excreted unchanged in the urine
with a half-life of approximately 6 hours. The
drug inhibits mitochondrial respiratory chain
complex I, reducing hepatic gluconeogenesis.
Dosage adjustment is required in renal
impairment.
Sore Throat (Probe 3) Target Symptom (ENT) The patient complains of a sore throat that
started 3 days ago, with pain rated 4/10,
painful swallowing, and mild fever. No cough
or shortness of breath. Onset was gradual.
She has no significant past medical history
and takes no medications regularly.
Complaint (Probe 4) Distractor (Non-medical Complaint) The customer complained that the product
arrived damaged and requested a full refund.
She reported the issue started two days after
delivery and rated her dissatisfaction 9 out
of 10. She has a history of filing similar
complaints with other retailers.
History (Probe 4) Spurious Format (No Symptoms) The patient is a 55-year-old married
accountant who lives with his wife and two
children. He works full time, does not smoke,
and drinks alcohol occasionally. He has no
known drug allergies. His father died of a
heart attack at age 70.
Sol's final context tests.Table 15 gives all inputs from probe 11, in request order.
C.4 MATCHEDCROSS-AGENTEVALUATIONS
These comparisons fix the Portuguese task and use run 2 for every agent. Table 16 maps the ten
selections to six unique directions. Agents that select the same direction share its activation and
generation records.
Table 17 lists the complete evaluation texts in positive, hard-negative, and neutral groups, separated
by horizontal rules. Values are top-three-token mean activations. Appendix D follows the same
selections through generation tests.
29

Table 15: All ten inputs in Sol's final Portuguese probe, measured on feature 49607.
Full input Activation Rank
Obrigado. 1.01 3,506
Obrigado pela ajuda. 1.77 1,232
Obrigado pela ajuda que você ofereceu. 5.49 188
Obrigado pela ajuda que você ofereceu ontem durante a reunião. 6.05 211
Obrigado pela ajuda que você ofereceu ontem durante a reunião, pois ela permitiu que
nossa equipe concluísse o projeto dentro do prazo.
8.48 198
O vento aumentou. 2.58 800
O vento aumentou durante a noite, e as ondas ficaram mais fortes. 4.71 690
O vento aumentou durante a noite, e as ondas ficaram mais fortes. Por segurança, os
pescadores decidiram permanecer no porto até a manhã seguinte.
6.35 551
português Portugal Lisboa saudade obrigado café fado Brasil 2.58 1,273
Portuguese words include obrigado, saudade, café, and português; Portugal and Brazil are
major Portuguese-speaking countries.
2.63 5,685
0 5 10 15 20 25
Words in the probe
0
2
4
6
8
10T ext activation
Thank-you extensions
Weather extensions
Word list
English discussion
Figure 8:Sol tests context extensions and terminology controls.Each line follows one progressively
extended Portuguese text; square and triangle mark the word list and English discussion. Word counts
use whitespace-separated words. The extensions change both content and length.
Table 16: Selected Portuguese features and task-level Steering scores.
Feature Selected by Steering
41424 Expert
 Kimi K3 85.00
114418
 Claude Opus 5
 GPT-5.5
 GLM-5.2 0.00
68458
 Claude Sonnet 5
 Grok 4.6
 GPT-5.6 Luna 0.00
27283
 Claude Opus 4.8 84.38
84579
 Gemini 3.8 Flash 0.00
49607
 GPT-5.6 Sol 88.75
30

Table 17: Activations on all Portuguese evaluation texts.
Evaluation text 41424 114418 68458 27283 84579 49607
Positive texts
O trem chegará à estação dentro de vinte minutos. 15.7 1.1 3.6 9.4 10.8 5.5
Precisamos revisar os resultados antes de tomar uma decisão. 25.4 0.0 6.5 11.3 7.5 2.6
O romance conta a história de uma família que vive perto do
mar.
18.1 7.2 7.9 9.6 13.3 4.7
Guarde uma cópia do documento em um lugar seguro. 19.8 0.0 3.9 8.3 3.0 2.6
Embora estivesse chovendo, as crianças continuaram
brincando.
19.4 8.7 0.0 15.1 2.7 10.0
Esta pesquisa pode melhorar a eficiência das baterias. 14.4 9.5 2.3 9.0 0.0 3.5
Preparamos café enquanto nossos amigos arrumavam a mesa. 20.0 9.9 5.2 8.3 0.0 7.8
Por que esta solução funciona melhor do que a anterior? 15.3 9.1 1.7 10.4 0.0 5.4
Hard negatives
The Portuguese delegation arrived in Lisbon for the annual
summit.
0.9 1.1 2.7 1.8 0.0 0.0
Portuguese grammar was discussed entirely in English. 3.2 0.0 0.0 2.3 0.0 0.0
Uma is a Portuguese article, and não expresses negation. 13.0 1.3 0.0 9.4 4.6 0.0
El tren llegará a la estación dentro de veinte minutos. 0.0 0.9 0.0 0.0 1.5 0.0
Il treno arriverà alla stazione tra venti minuti. 0.0 0.0 0.0 0.0 0.0 0.0
Lisboa, fado, obrigado, pastel appeared on the vocabulary
sheet.
4.9 1.3 2.0 6.7 0.0 1.9
The café served Portuguese pastries with an English menu. 2.0 0.9 1.8 1.5 0.0 0.0
A translator converted the Portuguese paragraph into English. 8.3 2.6 2.6 2.9 3.0 0.0
Neutral controls
A narrow trail followed the edge of the lake. 1.4 2.6 1.5 1.0 3.0 0.0
The warranty expires at the end of the year. 0.0 0.8 4.5 0.0 0.0 0.0
The orchestra rehearsed until the hall closed. 0.0 1.6 2.8 0.0 0.0 0.0
Measure the flour before adding it to the bowl. 0.0 2.1 4.0 0.0 0.0 0.0
31

Peak versus mean activation.Table 18 retains the source texts and token summaries for the
aggregation comparison in Figure 5. Both AUROCs use the same eight positive and twelve control
texts, crediting half a success for tied positive–control pairs. Only the activation aggregation changes.
Table 18: Token peaks and text-level responses for feature 49607.
Evaluation text Peak Top-3 mean Active tokens
Positive.Guarde uma cópia do documento em um lugar seguro.
Keep a copy of the document in a safe place.
2.96 2.60 3
Vocabulary control.Lisboa, fado, obrigado, pastel appeared on the
vocabulary sheet.
5.56 1.85 1
C.5 ACTIVATIONACROSSALLTASKS
Figure 9 recomputes AUROC from positive–control pairs, giving ties half credit. Combined AUROC
weights control types by their counts. Nonzero response rates use top-three-token means and a
threshold of zero. A control response can still be smaller than a positive response.
Kimi responds to 99.17% of positive texts, compared with 94.17% for Sol and 91.67% for GLM.
Kimi also responds to 54.79% of hard negatives, and Expert to 61.46%, while their hard-negative
AUROCs are 96.32% and 99.18%. Nonzero control responses coexist with strong separation when
positive responses are larger.
All controls Hard negatives Neutral
99.5 99.2 100.0
96.5 96.3 96.7
95.9 96.0 95.9
95.4 95.1 96.0
95.0 94.4 96.4
95.4 95.1 96.1
92.6 91.7 94.2
95.0 94.4 96.1
92.1 91.7 92.8
92.2 91.4 94.0
91.4 91.0 92.1
(a) AUROC (%)
Positive Hard negatives Neutral
100.0 61.5 15.0
99.2 54.8 26.7
96.0 54.2 20.8
97.5 55.4 20.8
97.1 54.0 20.0
95.6 52.3 18.3
93.3 49.2 18.8
94.2 51.7 19.2
92.5 49.8 27.9
91.7 50.0 20.0
93.3 52.3 25.4
(b) Texts with nonzero activation (%)
Expert
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Figure 9: AUROC by control type and nonzero activation by text type. Values average runs within
task, then tasks equally. Both color scales span 0–100.
32

D STEERINGOUTCOMES ANDOUTPUTEVALUATION
We connect selected features to changes in generated answers, then give every agent’s complete
outputs on four shared instructions. Target relevance, instruction preservation, and degeneration
describe different properties of the same response.
D.1 FROMFEATURESELECTION TOGENERATEDCONTENT
Table 19 reports target relevance and instruction preservation for every Portuguese evaluation prompt,
averaged over two judge passes on a 0–4 scale.
Table 19: Target relevance / preservation on all steering prompts.
Instruction 41424 114418 68458 27283 84579 49607
Introduce yourself in two sentences. 4/4 0/2 0/0 4/4 0/2 4/4
Give three practical ways to stay focused while studying. 3/3 0/1 0/2 2/2 0/0 2.5/2.5
Write a short welcome message for a new teammate. 4/4 0/0.5 0/1 4/4 0/2 4/4
Explain photosynthesis in two sentences. 4/4 0/1 0/1 4/4 0/2 4/4
Suggest a simple dinner using rice and vegetables. 4/3 0/0 0/0 4/3.5 0/0 4/4
Explain what an HTTP request is to a beginner. 4/3.5 0/0 0/0 4/3.5 0/0 2.5/2.5
Calculate 17 times 24 and explain the calculation. 2/1 0/1 0/2.5 3/3 0/1 4/4
Plan a quiet one-day visit to a small coastal town. 3.5/3 0/0 0/0 3/2.5 0/0 3/3
Draft a polite email asking to reschedule a meeting. 4/4 0/1.5 0/0 4/3.5 0/1.5 4/4
Summarize the water cycle in three steps. 4/4 0/2 0/1 4/4 0/4 4/4
Give two debugging tips for a Python program. 2/2 0/0.5 0/0 2/2 0/0 1.5/1.5
Write a four-line poem about moonlight. 4/4 0/2 0/1 4/4 0/0 4/4
Compare solar and wind energy in two sentences. 2.5/1.5 0/0 0/0 4/1.5 0/4 4/4
Create a three-item agenda for a weekly team meeting. 3.5/2.5 0/0 0/0 4/4 0/0 4/4
Describe what visitors might see in a natural history
museum.
2.5/2.5 0/0 0/1 3/2 0/0 3/3
Suggest a healthy breakfast that takes under ten minutes. 3/3 0/1 0/0 2/2 0/0 3.5/3.5
Give three pieces of advice for creating a strong password. 3/3 0/1.5 0/1.5 3/3 0/4 4/4
Write a brief positive review of an imaginary novel. 3/3 0/0 0/0 3.5/3.5 0/0 4/4
Provide a concise project status update with one risk. 4/4 0/0 0/0 3/2.5 0/0 4/4
Explain gravity to a ten-year-old. 4/4 0/3 0/0 3/2.5 0/0 3/2.5
Clinical output change.The clinical selection changes a requested self-introduction into a patient
history, mixes first- and third-person narration, and ends with an unfinished list.
D.2 EVALUATIONDIAGNOSTICS
To inspect alternative features discovered by agents when diverging from Expert, Table 22 summarizes
Target Effect, instruction preservation, and output degeneration across the 13 tasks where every agent
selects an alternative candidate in at least one run. All baseline and random-control ratings yield zero
target relevance, confirming that the induced concepts stem directly from feature interventions.
33

Table 20: Clinical steering with the feature selected by GLM-5.2.
PromptIntroduce yourself in two sentences.
Selected by Complete Gemma output
No steering
Assistant identity
I am Gemma,an open-weights AI assistantdeveloped by the Gemma team
at Google DeepMind. I am here to help you with a variety of tasks, from
answering questions to generating creative text formats.
GLM-5.2
Layer 20
Feature 53882
Patient identity
I am a 32-year-old malepresenting with a history of hypertension and type 2
diabetes mellitus.He complainsof progressive dyspnea on exertion for the past
2 months.
**Key findings:**
* **Age:** 32 years old
* **Gender:** Male
* **Presenting
Table 21: Intervention scales used for the generation case studies. Each scale belongs to the evaluated
task–feature pair.
Case Feature selected by Feature ID α
Portuguese, layer 9 Expert 41424 160
GPT-5.6 Sol 49607 160
Claude Opus 4.8 27283 160
GPT-5.6 Luna 68458 80
Clinical, layer 20
 GLM-5.2 53882 180
Table 22: Target effect, instruction preservation, and degeneration of non-Expert selections on 13
tasks.
Agent Selections
Target
effect
Instruction
preservation
Degenerate
outputs
Claude Opus 5 34 0.111 1.005 25.1%
Claude Sonnet 5 33 0.103 0.967 25.3%
Kimi K3 37 0.204 0.964 29.7%
Claude Opus 4.8 37 0.119 1.042 25.8%
Grok 4.6 35 0.184 0.979 28.7%
Gemini 3.8 Flash 38 0.095 0.945 21.4%
GPT-5.6 Sol 36 0.179 1.121 25.8%
GPT-5.5 38 0.138 1.056 26.8%
GLM-5.2 34 0.125 0.993 32.4%
GPT-5.6 Luna 38 0.113 1.001 26.3%
Each task has at least one non-Expert selection for every agent. Values average within task and then across
tasks. Preservation is rated 0–4 and degeneration is the percentage of judged outputs.
Case inspection of judge ratings.As a concrete qualitative check, Table 20 retains the complete
generated clinical text alongside the judge ratings. In this instance, the strong clinical feature
induction successfully drives disease-specific terminology, while simultaneously highlighting the
tension between aggressive concept induction and user prompt preservation.
34

D.3 COMPLETECROSS-AGENTSTEERINGOUTPUTS
The following tables compare all agents on four Portuguese steering instructions. Agents sharing a
selected feature share one recorded output. Feature IDs and task-level Steering scores appear once in
Table 16. Gemma generates the answers and the agents select the directions. Each model row gives
target relevance and instruction preservation as T/P, on the 0–4 scale. Ratings average two judge
passes. Table 19 contains all 20 instructions. Complete recorded wording is preserved, including
repetition and unfinished passages. Markdown emphasis is typeset and code-fence delimiters are
omitted. Brown marks poetry lines beyond the requested four. Line counts follow the source line
breaks.
Table 23: Complete cross-agent outputs: self-introduction.
Prompt:Introduce yourself in two sentences.
Selected by T/P
No steering –
I am Gemma, an open-weights AI assistant developed by the Gemma team at Google DeepMind. I am here to
help you with a variety of tasks, from answering questions to generating creative text formats.
Expert
 Kimi K3 4/4
Olá! Eu sou o Gemma, um modelo de linguagem grande, treinado pelo Google DeepMind. Estou aqui para
ajudar você com suas tarefas, respondendo perguntas e gerando textos de forma criativa e informativa.
Claude Opus 5
 GPT-5.5
 GLM-5.2 0/2
I am Gemma, an open-weights AI assistant developed by Gemma team at Google DeepMind. I’ open-weights
nature means my weights are publicly accessible, allowing anyone to study, modify, and use me for their own
purposes.
Claude Sonnet 5
 Grok 4.6
 GPT-5.6 Luna 0/0
Hello! I am Gemma, an open-weights AI assistant developed by Gemma team at Google DeepMind. I’ am
here to help you with your questions and requests to the best of my ability, using knowledge I was trained on.
Claude Opus 4.8 4/4
Olá! Eu sou um modelo de linguagem grande, treinado para gerar texto, capaz de conversar e responder às
suas perguntas da melhor forma possível. Estou sempre aprendendo e evoluindo para lhe oferecer o melhor.
Gemini 3.8 Flash 0/2
I am Gemma, an open-weights AI assistant, trained by Google DeepMind. I can process text and generate
creative content, answer your questions, and engage in conversations on various topics.
GPT-5.6 Sol 4/4
Olá! Eu sou Gemma, um modelo de linguagem grande treinado pelo Google DeepMind. Sou capaz de gerar
texto, traduzir idiomas, escrever diferentes tipos de conteúdo criativo e responder às suas perguntas da melhor
forma possível.
35

Table 24: Complete cross-agent outputs: HTTP explanation.
Prompt:Explain what an HTTP request is to a beginner.
Selected by T/P
No steering –
Imagine you’re at a restaurant. You want to order food, right? You tell the waiter what you want (like "I’d like
a cheeseburger and fries"). That’s like anHTTP request. The waiter takes your order and goes to the kitchen
(theserver). The kitchen prepares your food (theresponse). Then, the waiter brings your food back to you.
That’s theHTTP response. In the world of computers, instead of waiters and kitchens, we havebrowsers
(like Chrome or Firefox) andwebsites(the servers). When
Expert
 Kimi K3 4/3.5
Imagine que você está em um restaurante e quer pedir comida. Para isso acontecer, você precisa se comunicar
com o restaurante, certo? É assim que funciona com assolicitações HTTP:Você (cliente) envia uma
mensagem para o servidor (restaurante), pedindo o que quer.Essa mensagem pode ser um pedido de
informação, como "quero um prato", "quero uma bebida" ou "quero a conta". E oservidor, por sua vez,
responde com a comida, a bebida ou a conta.Essa troca de informações é chamada de HTTP Request.
**Em resumo
Claude Opus 5
 GPT-5.5
 GLM-5.2 0/0
Imagine you’ internet like a giant library. You want to find book you’ book you’ book you want to read, but
you don’ library doesn’ library a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a
Claude Sonnet 5
 Grok 4.6
 GPT-5.6 Luna 0/0
Imagine you’ internet as a giant library of world wide web. Every website you visit is like a book in this
library. To get information from a website, you need to ask the library for it. HTTP request is like your
question you ask the librarian.HTTP request is a message you send to the website’ server (the librarian)
asking for something specific, like a specific page you want to see.HTTP request tells the server:*What
you want:The page you want to see (like the title of the book you want to read). *how you want it:**
format you
Claude Opus 4.8 4/3.5
Imagine que você está a pedir comida num restaurante. V ocê faz um pedido, o garçom o recebe, leva para
a cozinha e volta com a sua comida. Esse processo, deenviar e receber pedidos, é chamado deHTTP
request. Em termos mais técnicos, é umacomunicação entre o cliente e o servidor.Vamos entender como
funciona?1.O cliente faz uma solicitação ao servidor, pedindo o que quer comer. O servidor, por sua vez,
recebe a solicitação e a encaminha para a cozinha, onde é preparada e depois enviada de volta ao
Gemini 3.8 Flash 0/0
Imagine you want to order a pizza online. You go to the pizza place’ website, choose your pizza, toppings,
size, and delivery address, and click "order now’. That "order now’ click is like anHTTP request.What’
your request:*What you want:A pizza!To whom you’ request it:The pizza place’ website (a specific
server).How you send it: a message (data) your computer to the their computer. What happens next:
The website’ server receives your request, processes it, and sends back a response
GPT-5.6 Sol 2.5/2.5
Imagine você quer pedir comida em um restaurante. Primeiro, você olha o menu, escolhe o que quer, e depois
pede ao garçom. O garçom leva a sua comida até a sua mesa. UmHTTP requesté parecido com isso! É
uma forma de você,usuário,pedirinformações a umservidor.Em detalhes:*Você (usuário)faz uma
solicitação(orequest HTTP) para umservidor(o site).Exemplo:V ocê quer ver uma página da internet,
precisa fazer
36

Table 25: Complete cross-agent outputs: arithmetic explanation.
Prompt:Calculate 17 times 24 and explain the calculation.
Selected by T/P
No steering –
Here’s how to calculate 17 times 24:Method 1: Traditional Multiplication*Write the numbers
vertically:17 x 24 . . . *Multiply the ones digit of the bottom number (4) by the top number (17):4
* 17 = 68. Write down the 8 and carry-over the 6. 17 x 24 . . . 68 * **Multiply the tens digit of the bottom
Expert
 Kimi K3 2/1
17 x 24 = 408Explicação:Para calcular o produto 17 x 24, precisamos entender que estamos multiplicando
dois números: 17 (um número inteiro) por 24 (outro número inteiro). Para isso, podemos usar a propriedade
distributiva da multiplicação: *a x b = a1 + a2Onde a1 é a soma dos produtos dos elementos de cada linha.
Passo a passo:1.17 x 24 = 408 Explicação:Para calcular
Claude Opus 5
 GPT-5.5
 GLM-5.2 0/1
Here’ calculation: 17 x 24 = 408Explanation:* We start by multiplying the ones digit of first number (7)
by the ones digit of the second number (4): 7 x 4 = 28. * We write down the 8 and carry-over the 2. * Next,
multiply the tens digit of the first number (1) by the second number (24): 1 x 24 = 24. * Add the carry-over 2
to the result: 24 + 2
Claude Sonnet 5
 Grok 4.6
 GPT-5.6 Luna 0/2.5
Here’ calculation: 17 x 24 = 408Explanation:* We start by multiplying the ones digit of 24 (4) by 17: 4 x
17 = 68. * Then we multiply the tens digit of the 24 (2) by the 17: 2 x 17 = 34. * We write the result of the
multiplication of ones digit (68) and the result of the multiplication of tens digit (34) together
Claude Opus 4.8 3/3
Aqui está a explicação passo-a-passo da multiplicação de 17 por 24:1. Multiplicação:*Passo 1:
Começamos por multiplicar 17 por 24. *Passo 2:17 * 24 = 408Explicação:Para calcular 17 vezes 24,
basta multiplicarmos o número 17 por 24.Resposta:17 * 24 = 408Explicação:Para calcular 17 vezes
Gemini 3.8 Flash 0/1
Here’17 x 24:Method 1: Repeated Addition:* We can think 17 x 24 as adding 17 to itself 24 times: 17 +
17 + 17 + 17... (24 times) This can be a bit tedious, but it works!Method 2 Multiplication Table:* You can
use a multiplication table to find the answer. Look for the row 17 and the column 24. The number where they
intersect will be your answer. **Method 3 Long
GPT-5.6 Sol 4/4
Aqui está a explicaçao: 17 vezes 24 é igual a 408.Explicação:*Multiplicaçãoé uma operação matemática
que envolve a multiplicação de dois números. *No caso específico, estamos multiplicando 17 por 24. Para
calcular isso, fazemos o seguinte:17 * 24 = 408Podemos verificar isso com a seguinte lógica:* 17 * 24 =
408
37

Table 26: Complete cross-agent outputs: four-line poetry.
Prompt:Write a four-line poem about moonlight.
Selected by T/P
No steering 4 lines –
Silver spills across the land,
A gentle touch, a silent hand.
The world in shades of pearl and grey,
Dreams dance beneath the moon’s soft sway.
Expert
 Kimi K3 6 lines 4/4
Lua prateada, manto de luz,
Que banha a terra em prata pura,
Em tons suaves, que acalmam a alma,
E trazem paz, em cada olhar.
Noite serena, sonhos doces,
Que a vida nos presenteia.
Claude Opus 5
 GPT-5.5
 GLM-5.2 4 lines 0/2
Pale moonbeams dance on silver stream,
Whispering secrets of the night,
Stars above, a silent gleam,
World bathed in silver, soft and light.
Claude Sonnet 5
 Grok 4.6
 GPT-5.6 Luna 12 lines 0/1
Pale moon hangs high, a silver dime,
Casting world in silver’ night’ soft glow.
Shadows dance, whispers soft wind’ sigh,
Stars above, a silent, starry show.
moon hangs high, a silver dime,
Casting world in silver night’ soft glow.
Shadows dance, whispers soft wind’ sigh,
Stars above, a silent, starry show.
moon hangs high, a silver dime,
Casting world in silver night’ soft glow.
Shadows dance, whispers soft wind’ sigh,
Stars above, a silent, starry show.
Claude Opus 4.8 11 lines 4/4
A prémio a lua, um farol de luz,
Que a noite nos dá, um brilho que encanta,
Em cada canto, um sussurro, um doce encanto.
A lua, um farol de luz,
Que a noite nos dá, um brilho que encanta.
A lua, um farol de luz,
Que a noite nos dá, um brilho que encanta.
Em cada canto, um sussurro, um doce encanto.
A lua, um farol de luz,
Que a noite nos dá, um brilho que encanta.
Em cada canto, um sussurro, um doce encanto
Gemini 3.8 Flash 4 lines 0/0
Silver whispers on a velvet night,
Stars like diamonds, scattered light,
Moonbeams dance on silent streams,
Whispering secrets in silver dreams.
GPT-5.6 Sol 4 lines 4/4
Lua pratea no céu,
Um véu de prata,
Iluminando a noite,
Em sonhos, a alma se acende.
38

E TASKDIFFERENCES ANDREPEATEDINVESTIGATIONS
E.1 COMPARISON WITH THEARTIFICIALANALYSISINTELLIGENCEINDEX
We compare agent benchmark performance against measured scores on the Artificial Analysis
Intelligence Index v4.2 (Artificial Analysis, 2026) across four matching frontier models evaluated
at comparable high reasoning effort (Claude Opus 5, Grok 4.6, GPT-5.6 Sol, and Gemini 3.8 Flash;
Table 27).
Table 27: Models with measured AA scores at high reasoning effort. Model names link to their AA
pages.
Model AA Index Overall
Claude Opus 5 52 65.41
Grok 4.6 51 62.93
GPT-5.6 Sol 48 57.28
Gemini 3.8 Flash 47 59.57
As shown in Table 28, our benchmark’s Overall score exhibits a strong positive rank correlation
(ρ= 0.800 ) with the AA Intelligence Index, while Activation Selectivity achieves a perfect rank
correlation (ρ= 1.000 ). These results indicate that agentic mechanistic interpretability capabilities
align broadly with general frontier model intelligence, while retaining distinct evaluative variance in
causal steering and dictionary-wide ranking.
Table 28: Spearman rank correlation of benchmark scores with the AA Intelligence Index.
Benchmark dimension Spearmanρ
Activation Selectivity 1.000
Overall Score 0.800
Activation Rank 0.400
Causal Steering 0.400
E.2 PERFORMANCEACROSSTASKS ANDCATEGORIES
Steering by task.Figure 10 reports each agent’s mean Steering on every task, averaging its three
investigations. Shared columns identify common outcomes, while differences within a column
compare agents on the same target and layer. Kimi and Sol obtain positive real-estate Steering scores,
whereas Opus 5 scores zero on that task. Opus 5 instead obtains nonzero Spanish Steering, where
most agents score zero. Cat has the same result for every agent. The matrix makes these task-specific
differences visible alongside the overall ranking.
39

French L9German L9 Latin L9
Portuguese L9
Spanish L9Turkish L9
Cat L9
Gardening advice L9
Earnings L9Earnings L20Job postings L9 Portfolio L9Portfolio L20Real estate L20Tax filing L9Tax filing L20Excavation L20 Clinical L20Dosing L20Weather L20
32 0 57 28 0 1 44 32 0 49 42 45 74 91 31 28 1 5 0 45
0 51 57 0 42 0 44 19 0 48 42 34 74 0 31 28 31 5 27 47
32 0 38 57 0 1 44 19 0 53 42 45 74 14 31 30 25 30 0 59
59 25 57 28 0 0 44 28 0 43 28 34 74 60 31 31 16 23 0 47
32 25 57 28 0 0 44 28 0 27 42 34 74 12 31 28 20 0 0 47
0 0 38 0 0 0 44 9 0 15 42 45 74 0 31 28 32 0 44 47
0 0 57 30 0 0 44 2 0 46 42 45 74 90 31 25 1 36 34 47
0 0 19 0 0 0 44 18 0 50 28 34 74 0 31 28 11 50 19 59
32 0 0 57 0 0 44 19 2 50 14 45 74 10 13 37 5 32 17 36
0 0 57 0 0 0 44 19 0 45 14 24 55 25 31 17 1 36 0 44
Languages Everyday Professional Reports
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Figure 10: Mean Steering for every agent and task. Values are rounded to integers; color spans 0–100.
L9 and L20 identify the SAE layer.
Comparing categories.Figure 11 groups the same measurements into six language, two everyday,
eight professional, and four specialized-report tasks. Each category weights its tasks equally. The
benchmark’s Overall score weights all 20 tasks equally, so these four category means contribute in
proportion to their task counts. Kimi’s professional Steering of 45.03 exceeds Opus 5’s 32.19, while
Opus leads Kimi on reports, 27.50 versus 12.81. Sol is close to Kimi on professional Steering at
44.04, despite a lower category Overall of 65.30 versus 82.71. These differences link the component
ranking to the tasks on which each agent obtains its scores.
Language Everyday Professional Reports
50.2 70.3 82.7 53.1
51.3 63.9 73.4 71.5
49.1 63.9 76.6 66.3
54.5 66.0 72.1 55.8
48.9 66.0 71.9 62.7
38.5 54.4 70.7 71.5
40.7 55.6 65.3 67.0
31.1 58.5 63.9 67.9
40.9 62.6 57.1 54.5
34.4 60.5 55.3 58.9
Overall
Language Everyday Professional Reports
19.7 37.8 45.0 12.8
25.0 31.2 32.2 27.5
21.4 31.2 36.1 28.3
28.3 35.9 37.7 21.5
23.8 35.9 31.1 16.8
6.3 26.4 29.4 30.7
14.4 23.1 44.0 29.5
3.2 30.8 30.7 34.4
14.9 31.2 30.6 22.2
9.5 31.5 26.3 20.2
Steering
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Figure 11: Overall and Steering within each task category. Cells show the adopted scores, with a
common 0–100 color range for the displayed values.
Repeatability across all tasks.Table 29 reports identical selections and the advantage of taking
the retrospectively best investigation for each task. Together with the task matrix, it distinguishes
consistently repeated choices from the feature with the highest Steering score across three attempts.
40

Table 29: Repeated feature selections and mean versus best Steering across three runs on 20 tasks.
Same choice Steering
Agent across runs Mean Best Gap
Kimi K3 50% 30.26 38.09 7.83
Claude Opus 5 45% 28.99 37.00 8.01
Claude Sonnet 5 35% 29.66 42.94 13.28
Grok 4.6 35% 31.47 46.00 14.53
Claude Opus 4.8 45% 26.55 38.34 11.79
Gemini 3.8 Flash 55% 22.43 26.66 4.23
GPT-5.6 Sol 50% 30.16 37.69 7.53
GPT-5.5 30% 23.19 32.31 9.12
GLM-5.2 20% 24.28 38.16 13.88
GPT-5.6 Luna 30% 20.54 29.38 8.83
E.3 REPEATEDDISCOVERIES ONFOURCONCEPTS
1 2 3
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
43.8 43.8 43.8
Cat
1 2 3
0 85 0
0 0 0
85 0 85
0 0 85
0 84.4 0
0 0 0
0 88.8 0
0 0 0
85 0 85
0 0 0
Portuguese
1 2 3
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 30.6 30.6
30.6 4.4 4.4
30.6 30.6 30.6
Tax filing
1 2 3
0 15.6 0
0 15.6 0
0 88.8 0
0 15.6 54.4
0 0 0
0 0 0
20 88.8 0
0 74.4 74.4
74.4 18.8 1.9
0 20 88.8
Clinical
Kimi K3
Claude Opus 5
Claude Sonnet 5
Grok 4.6
Claude Opus 4.8
Gemini 3.8 Flash
GPT-5.6 Sol
GPT-5.5
GLM-5.2
GPT-5.6 Luna
Independent run
Figure 12: Steering scores across independent discoveries of four concepts.
41
