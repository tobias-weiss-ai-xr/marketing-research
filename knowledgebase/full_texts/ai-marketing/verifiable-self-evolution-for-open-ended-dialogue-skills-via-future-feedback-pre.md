---
title: Verifiable Self-Evolution for Open-Ended Dialogue Skills via Future-Feedback Prediction
url: https://arxiv.org/abs/2607.18973
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- ChaoJin Zhao
- Xuan Jiang
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.18973
pages: 7
chars: 21489
fetched_at: '2026-11-08T13:36:23+00:00'
kb_version: 1
---

# Verifiable Self-Evolution for Open-Ended Dialogue Skills via Future-Feedback Prediction

VERIFIABLESELF-EVOLUTION FOROPEN-ENDEDDIALOGUE
SKILLS VIAFUTURE-FEEDBACKPREDICTION
A PREPRINT
ChaoJin Zhao
ByteDance
zhaochaojin@bytedance.com
Xuan Jiang
ByteDance
jiangxuan.1217@bytedance.com
ABSTRACT
Textual skills provide a lightweight way to improve frozen language-model agents, but their self-
evolution normally requires a stable validation signal. Such signals are natural in mathematics or
code, where an answer can be checked after it changes, yet are problematic in open-ended dialogue:
changing the assistant response also changes the user’s next reaction, so a logged reaction cannot
directly evaluate a counterfactual response. We proposefuture-feedback skill evolution, which first
redirects self-evolution from prescribing the current answer to predicting whether the observed answer
will lead to a positive or negative subsequent user signal. This prediction task is verifiable on fixed
logged tuples and therefore supports validation-gated textual optimization. The evolved feedback
skill captures interpretable criteria for response quality and can subsequently serve as a diagnostic
and optimization target for answer skills. On a proprietary, privacy-preserving sales-assistant dataset,
careful quality filtering and a balanced resolved/unresolved split yield more than 75% prediction
accuracy. Beyond this result, the central contribution is a formulation that converts otherwise moving
conversational feedback into a fixed offline learning target, enabling reproducible skill evolution
without placing every candidate skill in live traffic. We discuss the boundary between observational
verification and counterfactual validity, and position the method as an offline optimization stage rather
than a replacement for final human or online evaluation.
Keywordsagent skill evolution·user feedback prediction·dialogue evaluation·language-model agents
1 Introduction
Large language model (LLM) agents are increasingly controlled by textualskills: persistent instructions that encode
domain procedures, quality criteria, and tool-use policies. Compared with parameter training, skill editing is inexpensive,
inspectable, and deployable without changing the underlying model. Recent work such as SkillOpt formalizes this idea
as text-space optimization: an optimizer proposes bounded edits to a skill, and an edit is retained only when it improves
a held-out score [Yang et al., 2026].
The validation score is the critical assumption. In verifiable domains, an altered response can still be checked against a
stable target. A mathematical proof can be re-evaluated, code can be executed, and structured outputs can be compared
with known answers [Gao et al., 2023]. Open-ended dialogue lacks this invariance. Consider a logged interaction
x= (C,H, Q1, A, Q2),
where C is contextual and user information, H is dialogue history, Q1 is the current request, A is the assistant response,
and Q2 is the user’s subsequent utterance or behavioral feedback. If an answer skill changes A into A′, the original
Q2 is no longer the reaction that would necessarily follow. Consequently, scoring A′ against the logged Q2 conflates
factual observation with an unobserved counterfactual.
This creates a practical obstacle for dialogue skill evolution. Without a fixed offline objective, each candidate answer
skill would ideally require human judgment or online A/B traffic. Iterative deployment is slow, expensive, and risky;
moreover, it provides no clean validation gate indicating whether textual self-evolution has converged.
arXiv:2607.18973v1  [cs.CL]  21 Jul 2026

Verifiable Dialogue Skill EvolutionA PREPRINT
Figure 1: Verification differs for the two skills. Revising SA produces a new answer A′ and an unknown subsequent
signal Q′ 2, so logged Q2 cannot validate the candidate. Revising SQ keeps (Q1, A, Q2) fixed, allowing every prediction
to be compared with observedQ 2.
We introduce a change of learning target. Instead of first evolving a skill that tells the assistanthow to answer, we evolve
a feedback-prediction skill that estimateshow a user will respond to an already observed answer. Given (C,H, Q1, A),
the predictor estimates whether the next signal indicates resolved/accepted or unresolved/rejected. Unlike counterfactual
answer evaluation, this task can be measured against a fixed logged label. Failed predictions are summarized into
bounded additions, deletions, or replacements in the feedback skill; candidates are accepted only when they improve
held-out performance.
The resulting feedback skill is useful beyond classification. To predict whether a user will accept an answer, it must
encode operational distinctions between superficially plausible responses and genuinely resolving ones: tool success
is not user adoption, a weak acknowledgment is not acceptance, a generic suggestion is not an actionable plan, and a
response must cover the user’s independent decision points. These rationales expose concrete directions for improving
the answer skill.
Our contributions are:
• We formulate the moving-target problem that prevents direct reuse of logged next-turn feedback for offline evolution
of open-ended answer skills.
• We propose validation-gated future-feedback skill evolution, turning logged human and behavioral signals into a
fixed, verifiable objective for textual skill optimization.
• We identify a feedback–generation duality: the interpretable rules required to predict dissatisfaction also provide
actionable diagnostics for answer generation.
• We report an industrial case study in which cleaned high-quality data and a balanced resolved/unresolved evaluation
produce over 75% accuracy, while explicitly separating observational prediction accuracy from counterfactual
guarantees.
Figure 1 makes the claim boundary explicit. Held-out logged data verifies evolution of the feedback-prediction skill
itself. Its learned criteria can guide answer-skill edits, but the resulting counterfactual answers require fresh human
judgments or online interactions; the original logged reaction is not a valid label for them.
2

Verifiable Dialogue Skill EvolutionA PREPRINT
2 Related Work
Textual skill and prompt optimization.Textual artifacts can serve as external, editable state for frozen models.
SkillOpt applies optimizer-style discipline to this space through bounded edits, held-out validation, and rejection of
non-improving candidates [Yang et al., 2026]. Our work adopts this validation-gated perspective but addresses a domain
in which the validation target itself changes when the generated response changes.
User satisfaction estimation.User satisfaction has long been studied as an automatic evaluation signal for dialogue
systems. The USS benchmark provides turn- and dialogue-level satisfaction annotations across multiple domains [Sun
et al., 2021]. SPUR uses supervised iterative prompting to learn interpretable satisfaction rubrics from labeled examples
[Lin et al., 2024]. These studies establish that satisfaction-related patterns can be learned from dialogue. Our focus is
not merely estimating satisfaction; it is using a verifiable feedback-prediction task as the optimization substrate for
self-evolving textual skills.
Predicting future dissatisfaction.See and Manning [2021] predict whether a user will express dissatisfaction in
the next turn and use that signal to rank chatbot responses. This is closely related to our predictive target. We differ
in treating the predictor’s textual policy itself as the object of validation-gated evolution and in extracting its learned
failure rationales as reusable skill knowledge.
Learned rewards and their limits.Human-feedback learning uses learned preference or reward models to optimize
model behavior [Ouyang et al., 2022]. Such models may fail under distribution shift or be exploited by optimization.
Our proposal is deliberately narrower: the logged-data objective verifies the evolution of the feedback skill on observed
interactions. It does not, by itself, prove that arbitrary answers optimized against that skill will satisfy users. Final
deployment still requires human or online confirmation.
3 Problem Formulation
3.1 Logged conversational feedback
Let
D={(X i, Ai, Yi)}N i=1, X i = (Ci,H i, Q1,i),
where Yi ∈ {0,1}is derived from the subsequent user utterance or a behavioral signal. In our application, Y= 1
means adopted or resolved andY= 0means unresolved.
An answer skillS A induces a response distribution
A∼p θ(A|X,S A),
for a frozen target model with parametersθ. The true utility of a new answer depends on an unknown reaction:
U(A ′) =E[Y ′ |X, A′].
For a logged record containing A, only Y is observed. Replacing A with A′ does not preserve the label because
generally
p(Y|X, A)̸=p(Y|X, A ′).
Thus, a fixed dataset cannot directly provide an unbiased validation score for arbitrary revisions ofS A.
3.2 A verifiable surrogate task
We instead optimize a feedback skillS F that predicts the observed label:
ˆY=f θ(X, A;SF ).
For every candidateS ′ F , the held-out score
J(S ′ F ) = 1 |Dval| X (X,A,Y)∈D val ⊮[fθ(X, A;S′ F ) =Y]
is measurable without changing the interaction. Other deployment-relevant metrics, such as asymmetric costs for false
positives, may be included inJ.
This shift does not make the feedback model a perfect counterfactual oracle. It does makeits own evolutionreproducible
and rejectable on fixed data, which is the property needed for disciplined textual optimization.
3

Verifiable Dialogue Skill EvolutionA PREPRINT
Figure 2: Formal comparison with a fixed log. Evolving SA changes A and leaves the subsequent Q′ 2 unknown.
EvolvingS Q predicts the recordedQ 2, so every edit remains testable on the same held-out data.
4 Method
4.1 Overview
Figure 2 contrasts direct answer-skill evolution with our approach. Direct evolution tries to reuse a reaction attached to
the old answer. Future-feedback evolution holds the logged answer fixed, learns a validated prediction skill, and then
uses its interpretable criteria to diagnose answer quality.
4.2 Feedback labels and data construction
Signals may originate from explicit user feedback, textual acceptance or rejection, and product-side behavioral events.
The implementation maps available evidence into a binary resolved/unresolved label. Silent termination is excluded
when its meaning is ambiguous; this avoids noisy labels but introduces selection bias, discussed in Section 7.
Data quality is essential. Raw production logs contain incomplete turns, proactive outreach that is not a response to
a user problem, duplicated or malformed records, weakly grounded labels, and missing conversational context. We
apply quality filters so that each retained example has a clear turn boundary, a usable response, and a high-confidence
subsequent label. We then construct train and test partitions with an approximately 1:1 resolved/unresolved ratio. This
prevents majority-class accuracy from obscuring whether the skill learns both outcomes.
4.3 Validation-gated skill evolution
Starting from an initial feedback skill S (0) F , the predictor produces a label and rationale for each training example.
At iteration t, an optimizer model receives high-value failures—especially confident false positives—and proposes a
bounded textual edit∆ (t):
˜SF (t+1) = Edit(S (t) F ,∆ (t)).
Both the current and candidate skills are evaluated on the held-out set. The candidate is accepted only if it improves the
primary validation objective; otherwise it is rejected:
S (t+1) F =
(
˜SF (t+1) , J( ˜SF (t+1) )> J(S (t) F ),
S (t) F ,otherwise.
4

Verifiable Dialogue Skill EvolutionA PREPRINT
A lexicographic variant can retain equal-accuracy candidates only when an asymmetric business utility improves.
Penalizing false positives more strongly is useful when declaring a user satisfied despite an unresolved issue is costlier
than conservatively predicting unresolved.
4.4 From prediction rationales to answer guidance
The evolved skill learns reusable distinctions. Representative rules include:
• successful tool execution or message delivery does not imply that the user adopted the result;
• greetings, product recommendations, reports, and calls to action do not by themselves resolve a user need;
• weak acknowledgments such as “OK” may indicate receipt rather than acceptance;
• parameter advice should specify an action and at least one operational anchor, such as a value, interface, time window,
or re-evaluation condition;
• the response should cover the independent decision points in the user’s latest request.
These rules can be transformed into diagnostics for SA. For example, a response recommending that a user “observe for
several days and adjust the parameter appropriately” appears helpful but lacks a target value and a trigger for further
adjustment. The feedback skill predicts unresolved and explains the missing actionability; the explanation can then
be distilled into an answer-skill instruction. In this paper, we establish this bridge conceptually and through observed
learned rules, but do not claim a separately measured end-to-end improvement ofS A.
5 Industrial Case Study
5.1 Setting
We evaluate the method on privacy-preserving interactions from a production sales-assistant scenario. Inputs include
available context, dialogue history, tool-use summaries, and the assistant’s current response. Labels indicate whether
subsequent user or behavioral evidence supports resolved/adopted versus unresolved/not adopted. All examples and
operational identifiers are anonymized, and no raw dialogue is released.
The latest evaluation uses a curated high-quality subset rather than the earlier unfiltered extraction. Train and test sets
are precisely partitioned and balanced to approximately equal positive and negative proportions. Because this paper
emphasizes the formulation and the data are proprietary, we report the verified aggregate result without disclosing
sensitive counts or traffic statistics.
5.2 Result
On the balanced held-out set, the evolved feedback skill achievesmore than 75% accuracy. A random or constant
classifier on this construction has approximately 50% accuracy, so the result indicates that the skill extracts meaningful
interaction-level signals rather than exploiting label prevalence.
Two engineering choices were decisive. First, data cleaning removed low-quality and weakly labeled interactions whose
conversational relation was ambiguous. Second, precise partitioning produced a balanced test set, making accuracy
directly interpretable across resolved and unresolved cases. We treat these as part of task construction rather than as a
novel modeling contribution: a verifiable objective is useful only when the labels and partitions faithfully represent the
behavior to be predicted.
The learned rules also provide qualitative evidence of convergence toward user-centered criteria. The predictor becomes
less likely to equate fluent sales language, completed workflows, or successful tools with actual resolution, and more
likely to require coverage, specificity, and an actionable next step.
5.3 What the result establishes
The experiment supports three claims. First, next-feedback prediction is learnable from cleaned conversational records.
Second, textual skill edits can be evaluated and gated on fixed held-out data. Third, the evolved artifact is interpretable
enough to expose recurring answer defects.
The result doesnotestablish that 75% observational accuracy is sufficient to optimize arbitrary counterfactual answers
safely. When the answer distribution moves, the predictor may also shift in accuracy. Our method therefore reduces the
5

Verifiable Dialogue Skill EvolutionA PREPRINT
need for repeated online testing during skill search, but does not eliminate a final human preference study or controlled
online validation for a deployed answer skill.
6 Discussion
6.1 Why predict feedback instead of directly judging answers?
A direct LLM judge can assign a score to a new answer, but its score may encode generic preferences rather than the
target users’ actual behavior. Future-feedback prediction ties the skill to observed human or behavioral outcomes. It
also produces an ordinary supervised validation loop: every prediction can be compared with a fixed label, and every
textual edit can be accepted or rejected reproducibly.
6.2 The feedback–generation duality
Prediction and generation are not identical, but they share a quality model. A predictor cannot reliably forecast
dissatisfaction without representing omissions, ambiguity, non-actionability, unsupported claims, and mismatches with
user intent. This creates a useful duality:
predictive failure criteria=⇒candidate generation constraints.
The feedback skill is therefore both an evaluator and a repository of response-quality knowledge. Future work can
automate the compilation of its rationales into answer-skill edits and validate those edits with a one-time counterfactual
human study.
6.3 Operational value
The framework changes the role of online evaluation. Instead of exposing every candidate skill to users, developers
can perform most iterations offline, reject non-improving candidates, inspect learned rules, and deploy only the final
candidate for controlled confirmation. This is especially valuable in customer-facing systems where careless exploration
can degrade trust.
7 Limitations
Counterfactual distribution shift.The predictor is validated on logged answers. Optimizing an answer skill may
generate out-of-distribution responses that exploit predictor weaknesses. The feedback skill should therefore be viewed
as a validated observational model and diagnostic oracle, not a proof of human satisfaction for arbitraryA ′.
Silent users.Interactions with no interpretable subsequent signal are excluded. Some may represent silent dissat-
isfaction, so the resulting labels cover explicit or behaviorally observable resolution more reliably than total user
satisfaction.
Data curation and reproducibility.The strongest reported result depends on proprietary cleaning rules and a private
production dataset. This is common in industrial dialogue research but limits external reproduction. Public satisfaction
datasets such as USS could test cross-domain generality in future work [Sun et al., 2021].
Binary feedback.Resolved/unresolved labels simplify graded, personalized satisfaction. A user can accept an answer
while remaining partly dissatisfied, or reject a correct answer for reasons outside response quality.
No additional answer-skill experiment.Consistent with the scope of this study, we do not report a new human
evaluation or online A/B test of an answer skill distilled from the feedback predictor. We therefore present rationale-to-
guidance transfer as a supported mechanism and research direction, not as a completed causal result.
8 Conclusion
Open-ended dialogue breaks the fixed-target assumption underlying validation-gated skill evolution: changing an
answer changes the feedback that would follow. We proposed future-feedback skill evolution, which makes the first
optimization target the prediction of logged user feedback rather than the direct generation of a counterfactual answer.
This yields a fixed offline objective for evolving an interpretable feedback skill. In a curated and balanced industrial
6

Verifiable Dialogue Skill EvolutionA PREPRINT
dataset, the method achieves over 75% held-out accuracy and learns criteria that distinguish superficial completion from
genuine resolution. The broader lesson is that verifiability in open dialogue can be recovered by choosing a prediction
target whose outcome has already been observed. This does not remove the need for final human validation, but it
makes the path to that validation more controlled, inspectable, and reproducible.
References
Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei
Liu, et al. Skillopt: Executive strategy for self-evolving agent skills.arXiv preprint arXiv:2605.23904, 2026.
Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and Graham Neubig. Pal:
Program-aided language models.Proceedings of the 40th International Conference on Machine Learning, 2023.
Weiwei Sun, Shuo Zhang, Krisztian Balog, Zhaochun Ren, Pengjie Ren, Zhumin Chen, and Maarten de Rijke.
Simulating user satisfaction for the evaluation of task-oriented dialogue systems. InProceedings of the 44th
International ACM SIGIR Conference on Research and Development in Information Retrieval, pages 2499–2506,
2021. doi: 10.1145/3404835.3463241.
Ying-Chun Lin, Jennifer Neville, Jack W. Stokes, Longqi Yang, Tara Safavi, Mengting Wan, Scott Counts, Siddharth
Suri, Reid Andersen, Xiaofeng Xu, et al. Interpretable user satisfaction estimation for conversational systems with
large language models.arXiv preprint arXiv:2403.12388, 2024.
Abigail See and Christopher Manning. Understanding and predicting user dissatisfaction in a neural generative chatbot.
InProceedings of the 22nd Annual Meeting of the Special Interest Group on Discourse and Dialogue, pages 1–12.
Association for Computational Linguistics, 2021. doi: 10.18653/v1/2021.sigdial-1.1.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela Mishkin, Chong Zhang, Sandhini
Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human feedback.
Advances in Neural Information Processing Systems, 35:27730–27744, 2022.
7
