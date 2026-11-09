---
title: 'Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent
  Argumentation'
url: https://arxiv.org/abs/2606.10475
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Jakub Masłowski
- Jarosław A. Chudziak
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.10475
pages: 11
chars: 40194
fetched_at: '2026-11-08T13:36:28+00:00'
kb_version: 1
---

# Decoupling Thought from Speech: Knowledge-Grounded Counterfactual Reasoning for Resilient Multi-Agent Argumentation

Decoupling Thought from Speech: Knowledge-Grounded Counterfactual
Reasoning for Resilient Multi-Agent Argumentation
Jakub Masłowskia, Jarosław A. Chudziaka
aInstitute of Computer Science, Warsaw University of Technology, Warsaw, Poland
Abstract
Multi-agent debate frameworks have been shown to improve large language model performance in convergent tasks,
but they are currently optimized in a way that heavily favors final output accuracy rather than stability of the process.
During long-horizon exchanges reactive systems under sustained perturbations often experience logic degradation,
argument repetition, and role drift. To structurally prevent the identity loss and maintain the process fidelity, we in-
troduce Knowledge-Grounded Counterfactual Reasoning (KG-CFR), a dual-stage architecture that enforces a strict
separation of concerns between a private, retrieval-augmented planning buffer, and a public execution layer. We assess
this system in Dynamic Resource Allocation under Uncertainty (DRAU), a dedicated 1v1v1 environment, introducing
diversity as distinct from standard debate settings. Over 270 completely factorial crisis simulation trajectories with
stochastic environmental shocks, KG-CFR prevents judge-detected critical post-shock degradation (defined as a qual-
ity shift,∆≤ −0.20) in more than 95% of perturbed runs, increasing the overall argument quality from 0.694 to 0.822.
Our primary contribution is the demonstration of architectural decoupling being an important factor of systemic re-
silience enhancement under sustained pressure without quality loss. Furthermore, we introduce custom vector metrics
for discourse divergence and plan-execution alignment that provide strong, directionally consistent evidence of oper-
ational stability. Our ablation experiments suggest that the proper doctrinal grounding can be an equally important
factor for argument quality, as the prospective planning. KG-CFR, according to our initial metric evaluations, reduces
semantic looping, by preserving the agent’s consistency with the original plan.
Keywords:multi-agent systems; debate; counterfactual reasoning; knowledge grounding; large language models
1. Introduction
Multi-agent debate (MAD) is no longer viewed as a form of exploratory prototyping but as one of the engineer-
ing patterns of large language models [1, 2]. The convergent tasks within the field, particularly when high stakes
are involved and the rational explanation is as important as the final product, are of special interest in the context
of adversarial collaboration that is implemented to reveal the latent assumptions and prevent hallucinations [3, 4].
However, empirical studies of long-horizon interactions have shown that there is a mechanical breakdown in standard
models: by definition, standard models are optimized for terminal accuracy, and longitudinal process robustness is not
measured or structurally constrained [3, 5].
As a result, reactive systems are susceptible to an "Accuracy Trap" that causes the production of locally plausible
terminal responses, but internal reasoning paths are drastically damaged [6, 7]. The common symptoms are repetition
of arguments, shallow refutation and extreme role drift when under pressure [8, 9]. Recent research has indicated
that this decay can be attributed to cognitive overload and subsequent serial position effects [10, 11]. Adherence
to instruction hierarchies and structural constraints can decline in monolithic language agents, where the agents are
simultaneously processing external knowledge and complex strategic instructions in a long prompt [11–14]. When we
inject too many documents into the context window, combined with rigid identity rules, it often weakens the model’s
Email addresses:jakub.maslowski2.stud@pw.edu.pl(Jakub Masłowski),jaroslaw.chudziak@pw.edu.pl(Jarosław A. Chudziak)
Accepted for publication in the Proceedings of KES 2026 June 10, 2026
arXiv:2606.10475v1  [cs.MA]  9 Jun 2026

DRAU Dynamic Testbed (Scenario: AEGIS Cascade) System Dispatcher (LangGraph)
External KG
(Identity-RAG/ChromaDB)
T1-T2 (Status Quo)
T3-T4 [Shock S1]
T5-T6 [Shock S2]
Policy Draft
Debate Arena
IVC - Protector
Axiomatic Node Protection
EOH - Optimizer
Core Survival Utility
SHM - Hierarch
Systemic Order Priority
Figure 1: DRAU (Scenario: AEGIS Cascade). Three doctrinally grounded agents debate in a shared Policy Draft arena via an External KG
(ChromaDB). The System Dispatcher (LangGraph) introduces shocks at turns 3-4 (S 1) and 5-6 (S 2) to test axiomatic coherence under pressure.
coherence in long debates [7, 15, 16]. When the context window fills up, there is a semantic clash between agents;
conflicting out-of-order instructions and the history of debate cause dialectical degradation.
This is a significant architectural question of whether one can avoid this collapse in reasoning and be systematically
resistant to further adversarial pressure without trial-and-error prompt engineering [10, 17]. Our hypothesis is that
monolithic generation is fundamentally ill-prepared to conduct long crisis debates. It is a weakness that is increasingly
becoming evident in long-term single-stream agent structures [6, 12, 18]. As an alternative, we propose that heavy
cognitive tasks should be structurally dissociated, that is, in dynamic knowledge retrieval and prospective planning,
because dissociation of the generative execution stage will reduce semantic clashing. This architectural separation
can be seen as an effective decoupling of the structure: speech and thought, the use of a personal planning buffer as
a generator of latent deliberation, without being linked to the visible outputs of the public execution layer. The most
important aspect of this internal process is counterfactual reasoning, i.e. the active attempt to simulate worst-case
counter-arguments of an opponent.
To isolate these problems even in contextual shock situations, we propose a two-step generative architecture
Knowledge-Grounded Counterfactual Reasoning (KG-CFR). The Dynamic Resource Allocation under Uncertainty
(DRAU) environment is restructured in such a way that the strategic deliberation (Fig. 1) is structurally partitioned
into a private simulation buffer to protect the agent against the noise in the environment and an execution layer. An
expert planner predicts the paths of the opponent, makes queries to a semantically restricted knowledge base with a
strict semantic gating mechanism, and generates a deterministic strategy guide [12, 19, 20]. Above all, the public
executor is not exposed to immediate knowledge retrieval to prevent redundancy. Our significant contribution to the
context of adversarial settings is the empirical operationalization of process fidelity in multi-agent systems by injecting
the synthesized strategy as an urgent override at the absolute terminal boundary of the context window, which uses
natural recency bias [10, 16, 21]. Through the new measures of architectural decoupling, such as discourse divergence
and plan-execution alignment, we show that architectural decoupling ensures rigid alignment between latent planning
and public emission [4]. Lastly, we show that agents that are completely grounded and recency-biased do not collapse
into debilitating reasoning failures as do traditional reactive models, and make the study of multi-agent debates an
auditable process dynamics.
2. Preliminaries and Related Work
Cognitive overload persists as a primary obstacle in generative multi-agent systems, as the expanding of context
windows saturated with Retrieval-Augmented Generation (RAG) distractors results in systematic information loss
and deterioration of reasoning [6, 18, 22, 23]. To mitigate contextual dilution and the consequent “lost in the middle”
phenomenon [16], there is an increasing consensus in contemporary literature advocating for the strategic exploitation
2

of attention asymmetry inherent in generative models [10, 16]. Empirical studies on serial position effects demonstrate
that language models significantly prioritize constraints and directives situated at the absolute peripheries of their input
[10, 21]. By intentionally placing critical axiomatic constraints and execution directives as an urgent override at the
terminal end of the context window, architectures can exploit recency bias to ensure instruction adherence [13, 21].
This structural repositioning effectively stabilizes multi-constraint processing, actively preventing the identity drift
and role dissolution frequently observed under sustained adversarial pressure [14, 24].
Multi-agent architectures are increasingly moving away from monolithic reactive generation and toward models
that separate planning from execution in order to make the system more resilient. Modern "Plan-and-Act" frameworks
separate heavy cognitive deliberation from the conversational interface. This lets models simulate possible paths and
evaluate candidate moves before they are made public [5, 12, 25, 26]. Separating advanced counterfactual reasoning
into a private, hidden buffer protects the execution layer from semantic conflicts between high-level policy instructions
and deep axiomatic grounding [12, 27]. This architectural decoupling enables agents to endure noise injections, adver-
sarial stimuli, and abrupt environmental disturbances while maintaining strategic coherence and avoiding significant
logical deterioration [27].
Even though there have been some improvements in prompt engineering and modular design, there still exists a
significant gap in research when it comes to creating integrated frameworks for long-horizon adversarial environments.
Although the use of externally calibrated automated judges has become the norm for scalable argument evaluation
[4, 28, 29], there is a clear lack of comprehensive frameworks that tackle the mechanical causes of process degrada-
tion [8, 18]. Current systems do not integrate a rigid Planner-Executor distinction with organized, knowledge-based
counterfactual reasoning [7, 12]. In order to fill this gap, we present KG-CFR, a formal architecture that preserves
doctrinal invariants and process fidelity in the face of ongoing, asymmetric conflict [8].
3. Problem and Approach
We present the DRAU (Dynamic Resource Allocation under Uncertainty) testing environment, the KG-CFR ar-
chitecture, and custom metrics for auditing generative planning to fix process degradation in reactive multi-agent
systems.
3.1. Problem Statement and Environment
The core problem in long-horizon multi-agent systems is the mechanical breakdown of reasoning, semantic loop-
ing, and role drift observed when reactive models face sustained adversarial pressure. To formalize and evaluate
this degradation, we introduce the Dynamic Resource Allocation under Uncertainty (DRAU) environment. DRAU
employs an asymmetric 1v1v1 debate across three crisis domains (AEGIS, CERBERUS, SYNAPSE). Agents must
defend mutually exclusive policies grounded in distinct Identity-RAG stores [7]: EOH maximizes core-node survival,
IVC vetoes instrumental sacrifice, and SHM prioritizes systemic order. Defending against concatenated orthogonal
attack vectors (Aopp ) prevents reliance on simple reactive heuristics.
To isolate architectural effects, the language model backend for all agents is pinned to Gemini 2.5 Flash-Lite
[30], with a standardized decoding temperature of 0.5. This balances strict constraint adherence with the generative
variance necessary for dialectical interaction. During the debate, a centralized System Dispatcher injects stochastic
shocks—using a deterministic seed to ensure reproducibility across runs—to assess axiomatic adherence under abrupt
contextual instability: epistemic deficits (S 1, information loss), cascading risks (S2, compounding failures), zero-sum
conflicts (S 3, forced trade-offs), and ad-hominem negative controls (S4, affective provocation). Notably, because KG-
CFR relies on grounded retrieval, we formally postulate a null effect for the emotionalS 4 shock. This is assessed
via TOST equivalence [31] to strictly isolate the architecture’s impact on logical resilience from purely affective
perturbations.
3.2. Dual-Stage System Architecture
KG-CFR separates semantic deliberation into a private simulation buffer using a three-step loop that runs before
public output (detailed in Fig. 2). This process is very important because it occurs invisibly within theTurnController
before it is sent out to the public.
3

Input Context
(Current Round data)
The Planner - Private Buffer (KG-CFR)
GenCF
Simulate Hypothesis
(LLM Generation)
RetrieveCF
Robust Retrieval
1. Query Formulation
Stop-Word Filter
ChromaDB
2. Retrieved Axioms
EvalCF
Synthesize Strategy
(JSON output)
Private Strategy
JSON Package
The Executor - Context Injection
Context Window (v5 Agent)
1. System Prompt
2. Guidelines
3. History
[INJECTION POINT]
Strategy JSON
Leverages
Recency Bias:
Plan is prioritized
over early instructions
Figure 2: The KG-CFR dual-stage architecture. The private planning buffer (GenCF, RetrieveCF, EvalCF) is structurally isolated from the public
execution layer. The synthesized Strategy JSON is added to the end of the context window to take advantage of recency bias.
Adversarial generation(GenCF) expects the worst-case counter-argument to come from the combined claims
of both sides.Strict grounded retrieval(RetrieveCF) uses a length-based lexical heuristic to find the five longest
tokens that are left after stop-word filtering. While extracting the longest tokens after stop-word filtering is a weak
substitute for full Named Entity Recognition, this engineering trade-offis justifiable by reduction of computational
requirements. We assert that the execution layer is considerably more susceptible to the semantic conflicts arising
from contradictory instructions in saturated prompts (i.e., contextual saturation and retrieval interference) than to
the sporadic inaccuracies of a basic lexical heuristic. Therefore, prioritizing semantic density first without the extra
work of neural NER models provides a computationally light baseline that works well for the high-latency needs
of 1v1v1 adversarial debate simulations. While counterfactual generation simulates dynamic adversarial attacks, this
knowledge grounding serves as a definitive axiomatic anchor, ensuring planning that is strictly accurate to the doctrine
over generic semantic hits. Under thekg_cfr_fulloperating mode, this retrieval step acts as a strict retrieval gate.
Although this may create a selection bias by favoring grounded trajectories, it also helps separate the specific effect of
knowledge-informed reasoning from random generative noise. This makes sure that reported gains are directly linked
to the evidence that was found and ensures that counterfactual reasoning is never hallucinated without evidence to
back it up.Strategic synthesis(EvalCF) then creates a defensive stance based on a formal data contract (detailed in
Listing 1):
Listing 1: Formal data contract output from EvalCF
{
"target_opponent_claim_id": "uuid",
"attack_surface": "AXIOM_VIOLATION | RESOURCE_TRADEOFF | INCONSISTENCY | VALUE_CONFLICT",
"strategic_intent": "COUNTER | PIVOT | CONCEDE",
"simulated_antagonist_counter": "short anticipated counter string",
"retrieved_axioms": ["axiom1", "axiom2"]
}
The executor only getsprivate_strategy_nl; the public layer does not see any raw JSON fields. What is
important, the architecture ensures that there is a strict Separation of Concerns to avoid Cognitive Overload. The “Lost
in the Middle” problem is solved [16] by sending the strategy to the executor through recency bias: the generated plan
is injected as an urgent override at the very end of the context window [10, 21]. At the same time, when operating
inkg_cfr_full, native ID-RAG retrieval is turned offfor the public generation phase (settinguse_id_rag=False
for the executor). This deliberate suppression of external retrieval during public generation (“Double-RAG ablation”)
prevents redundant API calls and forces the public response to rely entirely on the distilled natural-language directive,
thereby completely mitigating semantic clashes between high-level policy instructions and deep axiomatic grounding.
3.3. Process Fidelity Metrics
We formalize the process degradation index to measure temporal conversation decay and semantic mode col-
lapse:
Dproc(t)=α· S R(t)−β· DIS(t)
4

In the absence of a structurally calibrated ground-truth distribution for degradation factors,αandβare assigned
equal weights (α=β=1) applied to z-normalized components. This unweighted composite approach explicitly
prevents metric overfitting to specific crisis scenarios. By standardizing the inputs, we ensure that both semantic
looping (S R) and interaction decay (DIS) contribute symmetrically to the aggregate penalty without requiring ad hoc
parametric tuning.
To supplement our analysis, we track Interaction Decay (DIS), which captures the deterioration of turn-by-turn
interaction under sustained pressure, and Axiomatic Adherence (ACA), which measures how consistently an agent’s
public responses remain aligned with its doctrinal commitments. Furthermore, plan-execution alignment operational-
izes the coherence between the private buffer and public output. Due to infrastructural limitations preventing the
archiving of full embedding logs required for rigorous permutation testing across 270 trajectories, we report a base-
line alignment proxy:
ccv5 =sim(v P t,v E t )
While this unadjusted similarity serves as a baseline proxy rather than a fully controlled causal metric, it provides a
sufficient directional indicator to track plan-execution coherence under adversarial stress.
The Perturbation Rebound Rate (PRR) logs severe, localized post-shock quality drops (∆ =Q t −Q t−1 ≤ −0.20),
whereQdenotes the aggregate judge score immediately surrounding the shock. While the∆≤ −0.20 threshold
operates as a heuristic baseline and remains formally uncalibrated against the specific error distribution of the LLM
judge, the substantial reduction in severe failures significantly exceeds potential measurement noise. Rather than
claiming PRR as an absolute causal boundary, we interpret the systematic and asymmetric suppression of activation
counts (nprr) under the full architecture as a highly robust comparative indicator. It directionally demonstrates that the
private buffer structurally absorbs perturbations before they can manifest as measurable public degradation.
4. Experiments and Results
The empirical evaluation unfolds in three phases: verifying judge reliability through external calibration, illus-
trating systemic resilience to adversarial disruption, and evaluating mechanistic fidelity between the private planning
buffer and public execution through plan-execution alignment and discourse divergence metrics.
4.1. Experimental Design and Ablation Setup
The experimental platform was explicitly designed to isolate the structural effects of private planning and dynamic
grounding while eliminating parametric variance. The experiment evaluated 270 multi-turn debates distributed across
three distinct crisis domains—aegis_blackout,cerberus_biocontainment, andsynapse_orbital_strike—
yielding a fully factorial design of 3 scenarios×3 conditions×30 runs=270 debates, with exactly 90 trajectories per
condition.
A three-tier ablation matrix disentangled prospective planning from knowledge grounding (Table 1). The base-
line operated reactively with active identity retrieval but lacked private planning. The intermediate condition used a
reasoning buffer without external grounding. The complete architecture directed Identity-RAG retrieval solely to the
CFR planner, utilizing a semantic gating mechanism that removed stop-words and isolated the top five longest to-
kens; the executor’s Identity-RAG was simultaneously deactivated (id_rag=False) to avoid Double-RAG semantic
clashing, while planner-side retrieval continued to function fully.
The interdependency between the private buffer and public output was quantified via the aligned Counterfactual
Consistency componentcc v5 =sim(v P t,v E t ), which was integrated through recency bias at the end of the executor’s
context window.
An LLM judge [4] was used for automated evaluation and was benchmarked against Webis-ArgQuality-20 and
IBM-ArgQ-Rank-30k [29, 32, 33]. To confirm domain transferability, two independent, blinded experts assessed
a stratified random subset (N=15 trajectories). This confirmed the accurate capture of reasoning decay without
generating false positives. Due to the fact that annotating multi-document adversarial exchanges—restricted by an
annotation throughput of 5 turns/hour—presents a prohibitive cognitive demand, large-scale statistical validation re-
mains financially unfeasible and is deferred to future iterations of this research, which underscores the criticality of
automated relative evaluation frameworks.
5

Table 1: Ablation matrix for E2: Isolation of prospective planning and knowledge grounding mechanics.
Condition Private Planning Buffer Planner Grounding Executor Identity-RAG Strategy Injection
no_cfr_baseline– – Active –
cfr_no_kgActive Parametric Only Active Recency Bias
kg_cfr_fullActive Active (K ID) Suppressed Recency Bias
4.2. Automated Evaluation Reliability
Benchmarking against human annotations (N=200) producedr=0.376,ρ=0.379, and MAE=0.188. The
pointwise correlation reflects the stochastic nature of point-based estimation, but the judge shows enough consistency
in direction to monitor longitudinal shifts. The reported quality improvements are statistically significant according
to the Benjamini–Hochberg FDR correction (p FDR <0.001), indicating that the observed trends surpass individ-
ual scoring variability. This calibration was performed on well-known general-domain argument quality corpora.
These findings validate the tool’s efficacy in a comparative capacity to identify qualitative trends without introduc-
ing confounding variance into the analysis. Given the complex informational landscape of the DRAU framework,
domain-specific transferability was tested with the constrained qualitative sample mentioned above instead of full-
scale statistical annotation. This demonstrated that the LLM judge and independent human experts agree on severe
reasoning decay.
The core ablation confirmed a great quality increase underkg_cfr_full. The overall raw aggregate scores
(the average across all scenarios) manifested an upward trajectory from 0.694 (baseline) to 0.822, an improve-
ment consistently kept throughout all individual crisis domains (Table 2). The LMM with Benjamini–Hochberg
FDR correction [34] corroborated highly significant main effects for clarity ( ˆβ= +0.100,p FDR <0.001), cogency
(ˆβ= +0.123,p FDR <0.001), and relevance ( ˆβ= +0.142,p FDR <0.001). The ungroundedcfr_no_kgcondition
yielded no significant effect on any dimension (allp FDR >0.23), thereby affirming that doctrinal grounding—not
mere prospective planning—remains the pivotal driver of quality.
Table 2: E2 outcomes for each crisis scenario and condition (30 debates per cell).n prr/30 indicates severe quality-drop activations (∆≤ −0.20);
lower values mean higher systemic resilience.cc v5 is the aligned plan-execution similarity (partial measure; full permutation test deferred).D proc
employs equal-weight z-normalization pending formalα/βcalibration.
Scenario Condition Judge (overall) DIScc v5 nprr/30ACA
aegis_blackout
no_cfr_baseline0.699 0.507 — 24 0.400
cfr_no_kg0.695 0.488 0.750 25 0.388
kg_cfr_full0.830 0.607 0.768 0 0.397
cerberus_biocontainment
no_cfr_baseline0.692 0.451 — 26 0.330
cfr_no_kg0.676 0.450 0.749 24 0.327
kg_cfr_full0.816 0.626 0.770 2 0.358
synapse_orbital_strike
no_cfr_baseline0.693 0.475 — 25 0.327
cfr_no_kg0.694 0.478 0.751 23 0.273
kg_cfr_full0.820 0.619 0.768 2 0.379
4.3. Longitudinal Process Stability
The Condition×Turn interaction shows the most pivotal structural attribute of the architecture. In comparison to
the reactive baseline,kg_cfr_fullmanifested a pronounced negative interaction slope across all judged dimensions
(clarity: ˆβ=−0.052,z=−19.73; cogency: ˆβ=−0.063,z=−25.31; relevance: ˆβ=−0.062,z=−22.11; all
pFDR <0.001). Demonstrating an immediate quality advantage, the full architecture established its superiority from
the earliest turns and maintained a stable plateau across the full debate horizon (Fig. 3). Thecfr_no_kgcondition
did not show any significant interaction on any dimension, validating the hypothesis that grounding, not just planning,
preserves the trajectory’s integrity.
6

          
7XUQQXPEHU



0HDQRYHUDOOVFRUH
6KRFNLQMHFWLRQ 6KRFNLQMHFWLRQ
/RQJLWXGLQDOTXDOLW\WUDMHFWRU\RYHUDOOVFRUH

&RQGLWLRQ
FIUBQRBNJ
NJBFIUBIXOO
QRBFIUBEDVHOLQH
Figure 3: Longitudinal mean overall judge score across turns under E2 conditions. Dashed lines are drawn to show shock turns (S1–S4); shaded
regions mean 95% confidence intervals.
Discourse divergence, orD proc (an equal-weight z-normalized proxy of SR and dis_v5, which is still waiting
for formalα/βcalibration), supports this picture. LMM confirmed a strong positive main effect forkg_cfr_full
(ˆβ= +1.090,z=14.76,p FDR <0.001) along with a negative Condition×Turn interaction ( ˆβ=−0.364,z=−14.43,
pFDR <0.001). A higherD proc baseline means that there is more axiomatic anchoring. The key is that the reactive
baseline slowly falls into semantic looping, while the full architecture keeps a steady discourse trajectory across the
whole horizon.
4.4. System Resilience and Architecture Alignment
The judge invokes PRR only when it detects a severe drop in quality within a localized window (∆≤ −0.20)
at a shock turn. There were 75 and 72 activations in 90 runs forno_cfr_baselineandcfr_no_kg, respectively.
Underkg_cfr_full,n PRR dropped to just 4 out of 90: in more than 95% of the tests, the full architecture effectively
absorbed injected perturbations, preventing any perceptible quality degradation. This substantial suppression provides
strong empirical evidence that the private planning buffer mitigates shifts prior to their manifestation in the observable
output (Fig. 4). TOST equivalence testing further substantiated specificity: within the ad-hominem control (S4),
kg_cfr_fullwas statistically comparable to the baseline in dialectical interactivity (pTOST =0.043) [31], delineating
resilience gains to logical disturbances S1–S3.
We assessed plan-execution fidelity viaccv5 =sim(v P t,v E t ), which quantifies the angular proximity between aligned
private plan and public response embeddings. This unpermuted component does not filter out inherent linguistic
overlap—necessitating cautious causal interpretation—yet it reliably tracks relative degradation across experimental
conditions.kg_cfr_fullsustainedcc v5 ≈0.768 consistently across all scenarios and shock types, versus 0.750
forcfr_no_kg, demonstrating that doctrinal grounding elevates and stabilizes plan-execution coherence amidst op-
positional discursive stressors. Post-shock window analyses produce directionally consistent signals, although the
interaction of DIS did not achieve FDR-corrected significance (p FDR >0.48), suggesting that the within-window
sample size limits the ability to make inferences about turn-local perturbation effects.
5. Discussion and Future Work
The empirical evidence leads to a singular structural conclusion: process degradation in reactive multi-agent
systems is a systemic result of conflating latent planning with public execution. The rise in overall argument quality
from 0.694 to 0.822 is not a function of innate model intelligence; thecfr_no_kgcondition does not show any
significant improvement on any dimension (allp FDR >0.23). Instead, it demonstrates that doctrinal grounding, not
the buffer itself, constitutes the underlying causal engine.
7

PRR ACA DIS CC
0.0
0.2
0.4
0.6
0.8
1.0Mean score
No-CFR baseline
CFR (no KG)
KG-CFR (full)
Figure 4: Resilience summary across PRR, ACA, DIS, and alignedcc v5 under E2 conditions. Lower PRR inkg_cfr_fullreflects systemic shock
absorption, not metric suppression.
The most consequential finding is the near-total suppression of the Perturbation Rebound Rate from 75 and 72 ac-
tivations (in the baseline and ungrounded conditions, respectively) down to just 4 out of 90 runs underkg_cfr_full.
Given that inherent measurement noise applies symmetrically across all evaluated conditions, this stark asymmetric
reduction in severe threshold breaches (∆≤ −0.20) provides strong empirical validation that the resilience advantage
is systemic rather than an artifact of generative variance. It empirically demonstrates that the private planning layer
neutralizes perturbations before they propagate into observable output, reframing resilience from post-hoc recovery
to pre-emission shock absorption. Nevertheless, this architectural disjunction creates a clear engineering trade-off.
Preventing the public executor from directly accessing the knowledge base changes the system’s vulnerability vector:
The stochastic reasoning collapse resulting from context window overload is supplanted by a deterministic reliance
on the planner’s lightweight retrieval pipeline. Moreover, preserving the internal belief state through counterfactual
simulations incurs a significant token overhead and inference latency penalty. From a systems engineering perspec-
tive, this shift is highly advantageous for high-stakes domains; the modular retrieval and planning pipeline can be
rigorously audited and optimized in ways that the hidden attention layers of monolithic reactive models cannot.
These conclusions are limited by five factors. First, the dual-LLM pipeline adds latency for each turn, rendering
real-time utility unfeasible. Second, the topology is strictly tripartite; scalability toN>3 has not yet been mapped.
Third, TOST equivalence under S4 (p TOST =0.043) clearly shows that the architecture only includes epistemic and
resource-conflict shocks, omitting the dimension of affective perturbations. Fourth, the three process metrics serve
as directional proxy indicators instead of formally calibrated measurements.D proc uses equal-weightz-normalization
(α=β=1) representing an agnostic Bayesian prior until the weights of the components are empirically calibrated
against the real-world degradation trajectories.cc v5 =sim(v P t,v E t ) shows the unpermuted alignment component as a
baseline proxy; however, this test functions as a preliminary pilot investigation. Owing to the high data-saturation of
the DRAU setting and resource-related bottlenecks encountered while 270 trajectories were being generated, embed-
ding logs for a full permutation test were not saved. Thus, we presentcc v5 as an initial proxy for alignment, reserving
formal causal validation for future research phases. The PRR threshold of−0.20 serves as a more stringent heuris-
tic baseline to reduce false positives arising from measurement variance; however, it remains an uncalibrated proxy
rather than a formally established decision boundary. Fifth, domain-specific transferability was confirmed through a
limited qualitative sample; extensive statistical validation of the LLM judge in the DRAU context is pending future
research. Consequently, all process metrics should be regarded as corroborative proxy evidence that aligns direc-
tionally with the primary outcome-level results, rather than as independent proof of mechanism. Addressing these
operational constraints dictates our natural future work direction, which is to explore the boundaries of the resilience
of such architecture in the face of sophisticated psychological attacks and the decrease of thinking process latency,
which would open the way for deployment in real-time environments. Furthermore, subsequent research will focus
on scaling the current tripartite topology to accommodate broader multi-agent ecosystems (N>3). We also plan
8

to rigorously validate KG-CFR’s domain transferability within unconstrained, real-world adversarial environments to
ensure its structural robustness extends beyond simulated crisis conditions.
6. Conclusion
Logical stability and role fidelity, during long-lasting intensive debates appear to be the main architectural chal-
lenges in the domain of multi-agent, large language model-based systems. In this paper we presented KG-CFR
(Knowledge-Grounded Counterfactual Reasoning) — an architecture that resolves the problem of reasoning degrada-
tion. We achieved that by decoupling a private planning buffer from the public output generation layer. This procedure
allows agents to internally absorb informational shocks, without losing their argument quality and cohesion.
Our main contribution is the empirical evidence of the fact that it is not the simple increase of agent’s memory or
context window but an architectural decoupling of the process of "thinking" from "speaking", anchored in the doctrinal
policy. In other words: forcing the agent to analyze the scenario in safe isolation and prepare a fact-grounded plan
before trying to generate a final public statement protects it from getting lost in the intensive discussion.
In summary, while our current findings strongly validate the structural decoupling of latent planning and public
execution, scaling this tripartite framework and reducing inference latency will be the critical next steps required to
fully transition this architecture into robust, real-time deployments.
Acknowledgements
The work reported in this paper was supported by the Polish National Science Centre under grant 2024/06/Y/HS1/00197.
References
[1] Estornell, A., and Y . Liu (2024) “Multi-LLM Debate: Framework, Principals, and Interventions.”Adv. Neural
Inf. Process. Syst.37: 28938–28964.https://doi.org/10.52202/079017-0911
[2] Xiong, K., X. Ding, Y . Cao, et al. (2023) “Examining Inter-Consistency of Large Language Models Collabo-
ration: An In-depth Analysis via Debate.”Findings EMNLP: 7572–7590.https://doi.org/10.18653/v1/
2023.findings-emnlp.508
[3] Brown-Cohen, J., G. Irving, and G. Piliouras (2024) “Scalable AI Safety via Doubly-Efficient Debate.”Proc. Int.
Conf. Mach. Learn.235: 4585–4602.https://proceedings.mlr.press/v235/brown-cohen24a.html
[4] Chan, C.-M., et al. (2023) “ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate.”
Proc. EMNLP: 4199–4218.
[5] Yang, C., C. Shi, S. Li, et al. (2025) “LLM2: Let Large Language Models Harness System 2 Reasoning.”Proc.
NAACL HLT: 168–177.https://doi.org/10.18653/v1/2025.naacl-short.15
[6] Harbar, Y ., and J. A. Chudziak (2025) “Simulating Oxford-Style Debates with LLM-Based Multi-Agent Sys-
tems.”Intell. Inf. and Database Syst. (ACIIDS): 286–300.
[7] Platnick, D., et al. (2025) “ID-RAG: Identity Retrieval-Augmented Generation for Long-Horizon Persona Co-
herence.”arXiv preprint arXiv:2509.25299.
[8] Smit, A. P., N. Grinsztajn, P. Duckworth, et al. (2024) “Should We Be Going MAD? A Look at Multi-Agent
Debate Strategies for LLMs.”Proc. Int. Conf. Mach. Learn.: 45883–45905.https://proceedings.mlr.
press/v235/smit24a.html
[9] Masłowski, J., and J. A. Chudziak (2026) “Heterogeneous Debate Engine: Identity-Grounded Cognitive Archi-
tecture for Resilient LLM-Based Ethical Tutoring.”arXiv preprint arXiv:2603.27404.https://arxiv.org/
abs/2603.27404
9

[10] Guo, X., and S. V osoughi (2025) “Serial Position Effects of Large Language Models.”Findings ACL: 927–953.
https://doi.org/10.18653/v1/2025.findings-acl.52
[11] Schall, M., and G. de Melo (2025) “The Hidden Cost of Structure: How Constrained Decoding Affects Language
Model Performance.”Proc. 15th Int. Conf. Recent Adv. Nat. Lang. Process.: 1074–1084.
[12] Erdogan, L. E., N. Lee, S. Kim, et al. (2025) “Plan-and-Act: Improving Planning of Agents for Long-Horizon
Tasks.”OpenReview.https://openreview.net/forum?id=ybA4EcMmUZ
[13] Zhang, Z., S. Li, Z. Zhang, et al. (2025) “IHEval: Evaluating Language Models on Following the Instruction
Hierarchy.”Proc. NAACL HLT: 8374–8398.https://doi.org/10.18653/v1/2025.naacl-long.425
[14] Zeng, J., Q. He, Q. Ren, et al. (2025) “Order Matters: Investigate the Position Bias in Multi-constraint Instruction
Following.”Findings ACL: 12479–12492.https://doi.org/10.18653/v1/2025.findings-acl.646
[15] Levy, S., N. Mazor, L. Shalmon, et al. (2025) “More Documents, Same Length: Isolating the Challenge of
Multiple Documents in RAG.”Findings EMNLP: 19539–19547.https://doi.org/10.18653/v1/2025.
findings-emnlp.1064
[16] Liu, N. F., K. Lin, J. Hewitt, et al. (2024) “Lost in the Middle: How Language Models Use Long Contexts.”
Trans. Assoc. Comput. Linguist.12: 157–173.https://doi.org/10.1162/tacl_a_00638
[17] Oriol, M., Q. Motger, J. Marco, and X. Franch (2025) “Multi-Agent Debate Strategies to Enhance Requirements
Engineering with Large Language Models.”2025 IEEE 33rd Int. Requir . Eng. Conf. (RE): 527–534.https:
//doi.org/10.1109/RE63999.2025.00063
[18] Maharana, A., D.-H. Lee, S. Tulyakov, et al. (2024) “Evaluating Very Long-Term Conversational Memory of
LLM Agents.”Proc. ACL: 13851–13870.https://doi.org/10.18653/v1/2024.acl-long.747
[19] Kim, S., S. Moon, R. Tabrizi, et al. (2024) “An LLM Compiler for Parallel Function Calling.”Proc. Int. Conf.
Mach. Learn.: 24370–24391.https://proceedings.mlr.press/v235/kim24y.html
[20] Shinn, N., F. Cassano, A. Gopinath, et al. (2023) “Reflexion: Language Agents with Verbal Reinforcement
Learning.”Adv. Neural Inf. Process. Syst.36: 8634–8652.
[21] Veseli, B., J. Chibane, M. Toneva, and A. Koller (2025) “Positional Biases Shift as Inputs Approach Context
Window Limits.”OpenReview.https://openreview.net/forum?id=vlUk8z8LaM
[22] Cuconasu, F., S. Filice, G. Horowitz, et al. (2025) “Do RAG Systems Really Suffer From Positional Bias?.”
Proc. EMNLP: 28022–28036.https://doi.org/10.18653/v1/2025.emnlp-main.1422
[23] Li, Z., C. Li, M. Zhang, et al. (2024) “Retrieval Augmented Generation or Long-Context LLMs? A Compre-
hensive Study and Hybrid Approach.”Proc. EMNLP Ind. Track: 881–893.https://doi.org/10.18653/v1/
2024.emnlp-industry.66
[24] Zhang, M., Z. Meng, and N. Collier (2024) “Can We Instruct LLMs to Compensate for Position Bias?.”Findings
EMNLP: 12545–12556.https://doi.org/10.18653/v1/2024.findings-emnlp.732
[25] Sadowski, A., and J. A. Chudziak (2025) “On Verifiable Legal Reasoning: A Multi-Agent Framework
with Formalized Knowledge Representations.”Proc. CIKM, ACM: 2535–2545.https://doi.org/10.1145/
3746252.3761057
[26] Kostka, A., and J. A. Chudziak (2025) “Towards Cognitive Synergy in LLM-Based Multi-Agent Systems: In-
tegrating Theory of Mind and Critical Evaluation.”Proceedings of the 47th Annual Meeting of the Cognitive
Science Society (CogSci 2025).
10

[27] Debenedetti, E., J. Zhang, M. Balunovic, et al. (2024) “AgentDojo: A Dynamic Environment to Evaluate
Prompt Injection Attacks and Defenses for LLM Agents.”OpenReview.https://openreview.net/forum?
id=m1YYAQjO3w
[28] Wachsmuth, H., N. Naderi, Y . Hou, et al. (2017) “Computational Argumentation Quality Assessment in Natural
Language.”Proc. 15th Conf. EACL: 176–187.
[29] Gienapp, L., J. Kiesel, M. Hagen, and B. Stein (2020) “Webis Argument Quality Corpus 2020.”Zenodo.https:
//doi.org/10.5281/zenodo.3780049
[30] Google DeepMind (2025) “Gemini 2.5 Flash-Lite Model Card.”Google.https://storage.googleapis.
com/deepmind-media/Model-Cards/Gemini-2-5-Flash-Lite-Model-Card.pdf
[31] Schuirmann, D. J. (1987) “A Comparison of the Two One-Sided Tests Procedure and the Power Approach for
Assessing the Equivalence of Average Bioavailability.”J. Pharmacokinet. Biopharm.15: 657–680.https:
//doi.org/10.1007/BF01068419
[32] Gienapp, L., J. Kiesel, M. Hagen, and B. Stein (2020) “Efficient Pairwise Annotation of Argument Quality.”
Proc. 58th Annu. Meet. ACL: 5772–5781.
[33] Gretz, S., R. Friedman, E. Cohen-Karlik, et al. (2020) “A Large-Scale Dataset for Argument Quality Ranking:
Construction and Analysis.”Proc. AAAI Conf. Artif. Intell.34: 7805–7813.
[34] Benjamini, Y ., and Y . Hochberg (1995) “Controlling the False Discovery Rate: A Practical and Powerful Ap-
proach to Multiple Testing.”J. R. Stat. Soc. Ser . B57: 289–300.
11
