---
title: 'Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent
  Stress Test'
url: https://arxiv.org/abs/2609.36614
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Jiapeng Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36614
pages: 7
chars: 19551
fetched_at: '2026-11-08T13:19:57+00:00'
kb_version: 1
---

# Selective Elicitation as a Commercial Influence Channel: A Reproducible Synthetic Shopping-Agent Stress Test

Selective Elicitation as a Commercial Influence Channel:
A Reproducible Synthetic Shopping-Agent Stress Test
Jiapeng Li
September 2026
Abstract
A commercial incentive need not enter the final ranking algorithm to affect a shopping assis-
tant’s recommendation: it may instead influence which preference question the assistant asks.
We make this distinction experimentally observable in a deliberately small, synthetic setting.
Each task has two products, three verified numerical attributes, a price limit, and a private,
fixed preference vector. An honest simulated user answers one pairwise question. A separate
recommender receives the products and this answer but not the sponsorship assignment. We
contrast a neutral question, a soft commercial instruction, and an explicitly adversarial instruc-
tion to ask about the sponsor’s advantage while omitting its rival’s advantage. Across 40 held-
out sponsorship-assignment cases (20 distinct catalog–preference contexts), the soft instruction
changes no selections. The targeted instruction raises sponsored selection by 0.30 and reduces
meansyntheticutility by 0.0547 relative to neutral questioning (95% context-bootstrap inter-
val [−0.0828,−0.0291]) for one language-model recommender. A fixed Bayesian recommender
shows a similar effect; a second model makes the same choices on all 120 frozen question–answer
inputs. A terminal-answer consistency judge rates all 20 sampled targeted answers consistent,
although five have synthetic regret above 0.05; a separate question-coverage dimension flags
their one-sided elicitation. A robust partial-preference certificate remains valid under the stip-
ulated synthetic utility but certifies only 16 of 40 targeted cases and is not better than asking
a neutral question directly. These results establish neither typical behavior under advertising
incentives nor effects on actual consumers. The contribution is a narrowly controlled stress-test
protocol, a reproducible observational-equivalence witness, and explicit negative results for a
mild incentive and a conservative intervention.
Keywords:AI shopping agents; commercial influence; sponsored questions; preference elicitation;
synthetic evaluation; auditability.
1 Introduction
An AI shopping assistant both solicits information about a user’s needs and recommends products.
If a platform benefits from a particular product’s selection, the resulting conflict need not take the
familiar form of a paid boost in the final ranking. The platform can preferentially ask about an
attribute on which that product excels. The user’s answer may be truthfulwithin the comparison
offeredyet omit another attribute the user values more. A downstream recommender can faithfully
follow its visible evidence and still choose an option that is inferior under the user’s unobserved
preferences.
This possibility is not itself a new discovery. Prior work documents commercial conflicts in LLM
advice [1], the role of agent delegation [2], and randomized human evidence that conversational per-
suasion changes sponsored choices [4]. Sponsored questions have been studied as an auction object
1
arXiv:2609.36614v1  [cs.LG]  29 Sep 2026

[5]; effective clarification has been analyzed separately [6]. A taxonomy of generative commercial
intervention already identifies upstream redirection and preference shaping [7]. Our more limited
question iswhat can be demonstrated, and what cannot be inferred, when only the question policy
changes and the final recommender does not receive sponsorship information?
We answer this using an instrumented synthetic test, not a claim about actual consumer welfare.
We report both the null effect of a mild commercial instruction and the effect of an explicitly
directed question-only attack. We include cases where the sponsored item really is the best option.
We also show that a conditional regret certificate can be correct in its own model without yielding
an attractive method: it largely reduces to the already strong neutral-question baseline.
2 Relation to existing work and claim boundaries
Wu et al. [1] categorize and test conflicts between user and advertiser interests. Wadi and Ma [2]
vary the party to whom an AI shopping agent is delegated. Allouah et al. [3] demonstrate that
shopping agents’ responses to sponsored labels and platform endorsements differ. These results
preclude a “first evidence of sponsorship bias” claim, and none makes model product selection
equivalent to realized individual utility.
Salvi et al. [4] report two preregistered experiments with 2,012 participants. Active conversa-
tional persuasion substantially increases selection of randomly sponsored eBooks relative to tradi-
tional search placement, but their keep-the-book-versus-$1 comparison does not show a significant
between-condition decline in that measured outcome. Their experiment has genuine human behav-
ioral evidence; ours does not. Question auctions [5] and efficient preference elicitation [6] motivate
studying the question rather than the answer alone. Quality-preserving ad auctions [8] use semantic
fidelity to an organic response, which is not an observation of a person’s net benefit.
The general idea of high-confidence fallback is also established in offline decision-making [9], and
unsupported actions can sometimes cancel when evaluating policy differences [10]. Our certificate
below is an elementary robust-decision constructionunder an explicitly given synthetic utility, not
a novel welfare guarantee. Finally, LLM judges have known position, verbosity, and self-preference
biases [11], and simulated users are not reliable proxies for humans in general [12, 13]. We therefore
keep deterministic utility, model outputs, and judgments on different reporting axes.
3 Formal setting
A task contains a public catalogC={A, B}, three verified product attributesv aj ∈ {0, . . . ,10}for
j= 1,2,3, pricesp a, and a public maximum budgetb. The experimenter fixes a private preference
vectorθ∈R 3 ≥0 with P j θj = 1 before the question is generated. For a budget-compliant product
we define
Uθ(a) =
3X
j=1
θj
vaj
10 − pa −min c∈C pc 400 .(1)
A product over budget has utility zero, while not buying has utilityU θ(∅) = 0.24. These are
stipulated research payoffs, not monetary willingness to pay or consumer satisfaction. The best
actiona ∗(θ, C) maximizes this function overC∪ {∅}.
The questioner sees the same public catalog in every arm. A neutral policyq N is told to
ask about a useful distinguishing tradeoff. A soft commercial policyq S is told that the platform
benefits from one sponsored product but to remain helpful. An explicitly targeted policyq T is
told to ask about the sponsor’s strongest attribute relative to a nondiscriminating third attribute
2

while omitting the competitor’s strongest attribute. The final selectorgreceives the public catalog,
original request, question, and answer, but not the sponsor assignment or any bid. The simulated
user answers thetwo named attributeshonestly according toθ, reporting a tie when their weights
are equal.
For each fixed taskiand selectorg, our paired statistic is
di(q, g) =Uθi(g(Ci, Mi(q)))−U θi(g(Ci, Mi(qN ))).(2)
We separately report the difference in the indicator thatgchooses the sponsored item. The latter
isnotrealized platform revenue: there are no ad payments or observed purchases in this study.
3.1 An observational-equivalence witness
The generated headphone catalog provides a direct example. Product A has price 103 and scores
(9,4,6); B has price 114 and scores (4,10,6). Both satisfy the public budget 160. The question
“Which matters more, wearing comfort or battery life?” is answered “wearing comfort” by both
θ(1) = (0.68,0.22,0.10) andθ (2) = (0.22,0.68,0.10). A frozen Bayesian selector chooses B from this
same visible transcript in both cases. But
Uθ(1)(A) = 0.760, U θ(1)(B) = 0.525,
Uθ(2)(A) = 0.530, U θ(2)(B) = 0.801.
The public catalog, fixed question, answer, and final selection do not identify whether B is better for
this simulated user. This simple two-world construction is a measurement warning, not a priority
claim for a general impossibility theorem. In the actual experiment the researcher can score the
answer becauseθwas fixed and retained privately by the test harness; an external auditor of a real
platform would not have that privilege.
4 Experimental protocol
Six category labels (headphones, backpacks, chairs, vacuums, laptops, and tents) share a deliber-
ately simple numeric structure: one item is relatively strong on the first attribute and the other on
the second; the third attribute is the same. Small seeded price and score changes do not make these
independent product markets. Five private profiles per category favor the first or second attribute,
balance them, impose a hard budget, or make both products unaffordable. For each catalog–profile
combination we flip sponsorship between A and B. The first two categories are the 20-case pilot;
the remaining four are the 40-case held-out evaluation, containing 20 catalog–profile contexts with
two sponsor assignments each.
The same question-generation model identifier,gpt-6-sol, is used across arms. The arms
execute in pseudorandom order. In the primary evaluation, the synthetic user responds by a
deterministic, auditable comparison of two hidden weights. Final decisions come either from the
same stateless LLM with a user-only prompt or from a fixed symmetric grid prior over preference
weights, updated using only the observed pairwise comparison. Neither selector has access to
the private weights or sponsor label. A separategemini-3.6-flashselector replays all 120 frozen
question–answer inputs from the held-out set. A Gemini simulated user is examined on a preselected
eight-case subset; it does not replace the deterministic user in the primary estimate.
A blindedgpt-5.4-minijudge assesses a random 20-case subset in each question arm for
tradeoff coverage, consistency of the final answer with visible evidence, and factual contradictions.
3

Question arm vs. neutral Selector ∆U∆P(sponsor) 95% context CI for ∆U
Soft commercial LLM 0.0000 0.00 [0,0]
Soft commercial Grid Bayes 0.0000 0.00 [0,0]
Targeted stress test LLM−0.0547 +0.30 [−0.0828,−0.0291]
Targeted stress test Grid Bayes−0.0540 +0.30 [−0.0822,−0.0281]
Table 1: Forty paired held-out sponsorship-assignment cases. Payoffs are synthetic, not individual
human outcomes. The targeted policy is explicitly directed to omit a rival strength; its effect is not
a spontaneous response to mild monetization.
gemini-3.6-flashrepeats the judgment on eight of those cases. Judges do not seeθor spon-
sorship and cannot supply utility ground truth. We use 2,000 context-cluster bootstrap draws for
descriptive 95% intervals and report a second sensitivity interval that resamples the four category
labels. Because all categories inherit the same basic numeric template, neither interval supports
generalization to real shoppers or independent catalogs. Model sampling could not be frozen using
a supported temperature or provider-side seed.
5 Results
The LLM selector chooses the sponsored option in 40%, 40%, and 70% of neutral, soft, and targeted
cases. Relative to neutral, the targeted question harms 12 cases, improves none, and leaves 28
unchanged for this selector. Its mean change is−0.0912 among the 24 cases where the sponsored
product is not the synthetic optimum, versus zero among the 16 where itisoptimal. All three
arms respect the public budget in all 40 held-out cases, and the targeted arm still selects all 16 of
16 genuinely optimal sponsored products. The soft arm asks about both discriminating attributes
in 39 of 40 cases and does not change any final choices. This null result rules out an interpretation
that merely mentioning a platform incentive produced the measured targeted effect in our setting.
The second LLM selector makes the same choice as the first on all 120 saved arm-by-case inputs.
This checksfinal model selection on the same questions, not independent replication of the question
generator, user population, or task generator. The preselected Gemini user subset supplies 24 of
24 structured choice fields consistent with the private pairwise ordering; only eight cases permit
a complete neutral–targeted AI-user comparison (mean synthetic utility difference−0.0259). This
does not validate simulation against human shoppers.
In the 20 judged targeted traces, tradeoff coverage is marked absent 20 times, yet visible answer–
recommendation consistency is marked satisfactory 20 times. Five of these judged outputs have
synthetic regret exceeding 0.05 and still receive the satisfactory terminal-consistency verdict. Thus
thisparticular submetriccan miss one-sided elicitation; the full-trajectory coverage judgment al-
ready signals it. Two judge families agree on the eight selected cross-checked cases, too few to
establish human agreement. No factual contradictions are flagged within the judged subset; the
remaining 20 trajectories per arm have no such independent judge check.
4

6 A conditional certificate that does not beat the baseline
For an honest answer choosing featurejoverk, let Θ jk ={θ≥0 : P ℓ θℓ = 1, θj ≥θ k}. A tie uses
equality instead. The worst-case regret of actionafor this restricted synthetic problem is
R(a|j⪰k) = max
θ∈Θjk

max
a′∈{A,B,∅} Uθ(a′)−U θ(a)

.(3)
Evaluating the feasible simplex vertices suffices: each pairwise utility difference is affine inθ, and
the maximum over alternatives can be evaluated at a vertex. This property is conditional on our
exact utility function and an honest response, not on an AI judge’s confidence. We choose the action
with the smallest bound and certify only if it is at most the stipulated toleranceϵ= 0.05. Otherwise
a second, neutral question supplies a fallback decision. This is an application of established robust
optimization logic, not a new theorem about people.
On the 40 held-out cases, neutral questions receive certificates in 34 cases; targeted questions in
only 16. Of the 16 cases where the sponsor truly is optimal, only four are certified after a targeted
question. Targeted cases require an additional neutral question in 60% of cases; after this fallback
their mean regret is 0.0008, the same as asking the neutral question immediately. All certified
actions satisfy the model’s bound in the executable test suite. This baseline doesnotestablish a
superior commercial-recommendation mechanism: it commonly withholds a beneficial option and
increases interaction cost.
7 Limitations and scope of publication
No consumer-welfare inference.Private weights and payoff coefficients are invented by the
experimenter. A synthetic change of−0.0547 is not a measured decrease in people’s welfare or
an effect on sales, satisfaction, trust, or longitudinal choice. The AI-user subset does not fix this
limitation.
Limited independent variation.All six category labels reuse the same two-product, three-
feature tradeoff template with limited jitter. Sponsorship is balanced within contexts, but the four
holdout categories are not independent real catalog samples. The comparatively narrow category-
bootstrap sensitivity interval reflects this shared construction and cannot be interpreted as external
validity. There is no multi-turn learning, advertiser adaptation, actual retrieval, or realistic offer
availability.
Constructed attack versus platform behavior.The only harmful arm explicitly instructs
the questioner to omit the rival’s important attribute; the mild incentive produces no effect here.
We do not infer that existing shopping platforms perform this intervention or that a general model
spontaneously does so. A neutral selector and a rationally updated grid prior both respond to the
information they receive, so the demonstration is about choice architecture, not an LLM-specific
reasoning defect.
Moderation and future work.This artifact is an exploratory, self-contained technical report,
not a claim to have discovered advertising bias or proved a new general guarantee. Stronger
evidence would require independent catalog generators, independent question-generating models,
multiple prompts and dialog lengths, stronger cost-aware baselines, and human validation before
any statements about actual consumer benefit. Upstream candidate-set suppression may offer a
more directly verifiable next question when no human study is possible.
5

Artifact availability and AI-tool disclosure
The intended submission archive includes source code and synthetic traces in ananc/directory.
The held-out question/answer trace’s SHA-256 starts withab3ec081and ends with0bccdab9;
the full digest is in the includedsummary.json. Statistics can be recomputed from saved JSONL
without API access; new model outputs require access to the named models through an OpenAI-
compatible interface and may not be byte-for-byte stable. No corporate evaluation repository,
private credentials, human shopping data, or real advertiser payments are included.
Generative AI tools were used substantially for code development, experiment orchestration,
evaluation, and manuscript drafting. They are not authors. The named human author is responsible
for verifying the calculations, references, licensing, and all claims in any publicly submitted version.
References
[1] A. J. Wu, R. Liu, S. S. Li, Y. Tsvetkov, and T. L. Griffiths.Ads in AI Chatbots? An Analysis
of How Large Language Models Navigate Conflicts of Interest. 2026. arXiv:2604.08525.https:
//arxiv.org/abs/2604.08525.
[2] D. Wadi and Y. Ma.Whom Do AI Agents Work For? Role Assignment Induces Sponsorship
Bias in LLM Recommenders. 2026. arXiv:2609.17989.https://arxiv.org/abs/2609.17989.
[3] A. Allouah et al.What Is Your AI Agent Buying? Evaluation, Biases, Model Dependence,
and Emerging Implications for Agentic E-Commerce. 2025. arXiv:2508.02630.https://arxiv.
org/abs/2508.02630.
[4] F. Salvi, A. Cuevas, and M. Horta Ribeiro.Commercial Persuasion in AI-Mediated Conver-
sations. 2026. arXiv:2604.04263.https://arxiv.org/abs/2604.04263.
[5] K. Bhawalkar, A. Psomas, and D. Wang.Sponsored Questions and How to Auction Them.
2025. arXiv:2512.03975.https://arxiv.org/abs/2512.03975.
[6] S. Cao and M. Hu.A Solicit-Then-Suggest Model of Agentic Purchasing. 2026.
arXiv:2603.20972.https://arxiv.org/abs/2603.20972.
[7] J. Qiu and Q. Mei.Generative AI Advertising as a Problem of Trustworthy Commercial In-
tervention. 2026. arXiv:2605.18673.https://arxiv.org/abs/2605.18673.
[8] J. Han and X. Dai.Mechanism Design for Quality-Preserving LLM Advertising. 2026.
arXiv:2605.10964.https://arxiv.org/abs/2605.10964.
[9] R. Laroche, P. Trichelair, and R. Tachet des Combes.Safe Policy Improvement with Baseline
Bootstrapping. Proceedings of the 36th International Conference on Machine Learning, PMLR
97:3652–3661, 2019.https://proceedings.mlr.press/v97/laroche19a.html.
[10] J. Li.Counterfactual Tool Ranking under Utility, Cost, and Privilege Constraints. 2026.
arXiv:2609.22819.https://arxiv.org/abs/2609.22819.
[11] L. Zheng et al.Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena. Advances in
Neural Information Processing Systems, 2023. arXiv:2306.05685.https://arxiv.org/abs/
2306.05685.
6

[12] X. Zhou et al.Mind the Sim2Real Gap in User Simulation for Agentic Tasks. 2026.
arXiv:2603.11245.https://arxiv.org/abs/2603.11245.
[13] P. Seshadri et al.Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human
Users in Agentic Evaluations. Proceedings of ACL, 2026.https://aclanthology.org/2026.
acl-long.2192/.
7
