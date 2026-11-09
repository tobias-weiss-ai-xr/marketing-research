---
title: 'Actionable CBFI: Integrating Structural Decomposition and Causal Counterfactual Recourse for Tabular
  Machine Learning'
url: https://arxiv.org/abs/2608.27821
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Sejong Oh
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.27821
pages: 18
chars: 59558
fetched_at: '2026-11-08T13:30:16+00:00'
kb_version: 1
---

# Actionable CBFI: Integrating Structural Decomposition and Causal Counterfactual Recourse for Tabular Machine Learning

Actionable CBFI: Prescriptive Interventional Diagnosis and Interaction-
Aware Escalation for Sparse Causal Algorithmic Recourse
Sejong Oh
Department of Software Science, Dankook University, Gyeonggi-do, Republic of Korea; e-mail:
sejongoh@dankook.ac.kr
ORCID: 0000-0002-9365-274X
Abstract
Algorithmic recourse tells an individual which feasible actions would change an unfavourable prediction.
Attribution scores such as SHAP explain why a prediction was made, but the most important causes are often
not the best levers. Causes may be immutable, and some actions work only through causal descendants or
only in combination with other actions. In this paper, we propose Actionable Case-Based Feature Importance
(A-CBFI), which changes the descriptive decomposition of Localized -CBFI into a prescriptive,
interventional diagnosis on a structural causal model (SCM). A -CBFI scores each actionable feature by the
best probability change that a do -intervention can reach. It prescribes the cheapest single action when one
exists and searches feature pairs and triples only when no single action is enough. Pairs are ranked by their
best joint probability change, which adds a best-response interventional interaction to the single-action gains.
We show analytically that interventional interaction comes not only from the model but also from path
blocking and shared descendants, which model -only interaction indices cannot see. We also show that
averaged interaction scores cancel exactly where additive targeting fails. We tested the proposed method on
ten tabular benchmarks in credit, health and education (6,657 recourse queries, three models, three random
splits, monotonicity constraints). A -CBFI was never significantly less successful than an untargeted causal
beam search. It prescribed fewer direct actions (1.10 vs 1.38) and needed 119 instead of 150 model
evaluations on average, including diagnosis (LEWIS -style causal recourse: 1857). The price was larger
individual changes. For 68.2% of the queries that a single action solves, it also offered substitutable single
actions at no extra cost. Overall, it was more successful than the LEWIS -style baseline and SHAP -guided
search. Non -causal counterfactual methods, which ignore downstream changes, were more successful on
Adult Income. Success gains over untargeted search were significant where causes are immutable and single
actions are insufficient (HELOC and Taiwan Default at the default threshold; Adult Income, German Credit,
Give Me Some Credit, Lending Loan, Pima Diabetes on harder queries), and they were never negative. On
CDC Diabetes, Student Dropout, Student Performance the methods were equivalent. The conclusions did not
change under misspecified causal graphs, including data-driven PC graphs and nonlinear structural equations.
Keywords: Algorithmic recourse; Counterfactual explanation; Structural causal model; Feature interaction;
Explainable artificial intelligence; Tabular machine learning
1. Introduction
Feature attribution methods such as LIME [1] and SHAP [2] are widely used to explain individual
predictions of tabular models. They answer a descriptive question: which feature values pushed this
prediction towards the unfavourable class? In consequential decisions such as lending, clinical risk screening
or student support, the affected person usually needs an answer to a different question. This question is
prescriptive: which feasible actions would change the outcome? Counterfactual explanations and algorithmic
recourse deal with the second question [3–7]. Causal recourse further requires that the recommended actions

respect the causal dependencies among features, which are modelled by a structural causal model (SCM)
[8,9].
One natural idea is to use attribution scores to decide where to search for recourse, and several methods do
so [10 –12]. However, the features that explain a prediction are not always the levers that can change it.
Mothilal et al. [13] showed that top -ranked LIME/SHAP features are often neither necessary nor sufficient
for changing a prediction. Fokkema et al. [14] proved that no attribution method can be both recourse -
sensitive and robust. Causes and levers differ for three reasons. First, the dominant causes may be immutable
(e.g. age or credit history). In this case, the lever must be a feature that contributes little to the current
prediction. Second, an action may work mainly through its causal descendants (a mediated lever). A model -
only attribution does not give credit to such an action. Third, an action may be effective only together with
another action (an interaction lever).
In earlier work, we proposed case -based feature importance (CBFI) [15]. CBFI sorts instances into four
groups according to whether a feature 𝐹𝑥  and the remaining features 𝐹𝑥(−)  each suffice for a correct
prediction: main effect (G1), alternative contribution (G2), common contribution (G3, both suffice) and
interaction (G4, neither suffices alone). Its instance -level variant, Localized -CBFI [16], decomposes a
prediction into main effects ( 𝐶G1) and pairwise interactions ( 𝐶G4) using permutation perturbations. Both
methods are descriptive. A preliminary version of the present work [17], which we call IGBS (interaction -
guided beam search) below, used averaged interventional scores. In this paper, we show that averaging
cancels the interactions that matter for recourse, and that diagnosing all pairs before the search dominates the
computation.
Therefore, we reformulate A-CBFI as a prescriptive diagnosis. The contributions of this paper are as follows:
• Prescriptive interventional diagnosis.  We define the single -lever score F1 and the pairwise best -
response interaction 𝐶G4 br as the best change of the adverse probability that do -interventions on an SCM
can reach. These scores differ from the averaged (descriptive) scores of Localized -CBFI and IGBS. We
also give the CBFI groups a prescriptive meaning: common (G3-type) support requires joint actions, and
cooperative (G4-type) support gives substitutable single actions (Section 3.2).
• Analysis of interventional interaction.  Lemma 1 identifies three sources of the interventional
interaction of two actions: a model term, a path -blocking term and a shared -descendant term. Model -
only interaction indices (e.g. SHAP interaction values) capture only the first one. Proposition 1 gives
conditions under which additive targeting provably fails and best -response pair diagnosis succeeds, and
it explains why averaged scores cancel (Section 3.3).
• A staged recourse algorithm.  A-CBFI prescribes the cheapest single action when one reaches the
decision boundary, and it searches pairs and triples only otherwise. In other words, the diagnosis is also
the first search stage, and its cost is counted end-to-end (Section 3.4).
• A controlled empirical study.  We compare A -CBFI with untargeted causal search, IGBS [17], a
LEWIS-style causal baseline [18], SHAP -guided search and DiCE [4] on ten datasets, three model
classes and three random splits (6,657 queries) with monotonicity constraints. The study includes a
component ablation, a difficulty sweep and a DAG -misspecification analysis. We report both where A -
CBFI helps and where it does not.
The rest of this paper is organised as follows. Section 2 reviews related work. Section 3 describes the
proposed method and its analysis. Section 4 explains the experimental setup, and Section 5 presents the
results. Section 6 discusses the limitations, and Section 7 concludes the paper.

2. Related work
2.1 Counterfactual explanations and algorithmic recourse
Wachter et al. [3] formulated a counterfactual explanation as the closest input that receives a different
prediction. Later methods added actionability and sparsity constraints for linear models [5], diversity [4],
model-agnostic satisfiability formulations (MACE) [19], search methods for tree ensembles (feature
tweaking, FOCUS) [20,21], plausibility on the data manifold [6,7,22] and robustness to model changes [23].
Benchmarks such as CARLA [24] and surveys [25] summarise this line of work. These methods assume that
each feature can be changed independently.
2.2 Causal and sequential recourse
Karimi et al. [8] argued that recourse should be framed as minimal interventions on an SCM. In this way, the
consequences of an action on its causal descendants are taken into account. When causal knowledge is
imperfect, a probabilistic treatment is required [9]. Mahajan et al. [26] preserve causal constraints in
counterfactuals. Ordered counterfactual explanations [27] and consequence -aware sequential recourse [28]
determine the order of actions. Improvement -focused causal recourse [29] and strategic classification [30]
distinguish actions that improve the true outcome from actions that only flip the predictor. A -CBFI uses a
given SCM in the same way as [8]. It focuses on which actions to search, not on their order.
2.3 Attribution, interaction and recourse
Interventional attribution methods include causal Shapley values [31], asymmetric Shapley values [32] and
Shapley Flow [33]. These methods distribute credit along the causal structure, and some methods attribute
credit to the edges of a DAG. Interaction attribution methods include SHAP interaction values [34], the
Shapley–Taylor index [35], Friedman's H -statistic [36] and Archipelago [37]. All of these methods are
descriptive. They explain a prediction. Some counterfactual -oriented variants use counterfactuals as the
background of SHAP [11], and others use attribution to select the features of a counterfactual [10,12]. The
work closest to our prescriptive single -lever score is LEWIS [18]. LEWIS estimates the probability that
setting an attribute to a value would flip a decision (sufficiency) and derives recourse from it. The
necessity/sufficiency framework of Watson et al. [38] is also related. A -CBFI differs from these methods in
three respects (Table 1). First, it uses instance -specific abduction on an SCM. Second, it treats interaction as
a best -response quantity and uses it to move from single to joint actions. Third, it reports direct actions
separately from downstream SCM changes.
Table 1. Positioning of A-CBFI relative to closely related approaches.
Approach Causal
model
Score type Interactions Search Output
SHAP / interaction values
[2,34]
No Descriptive Model-only – Attribution
Causal / asymmetric
Shapley [31,32]
Yes Descriptive – – Attribution
DiCE [4], MACE [19],
FOCUS [21]
No – Implicit Optimisation Counterfactual
Causal recourse [8,9] Yes – Implicit Optimisation Interventions
OrdCE [27], sequential
[28]
Partly Interaction matrix Ordering MILP / search Action sequence
LEWIS [18] Yes Prescriptive – Integer programme Interventions

(sufficiency)
Localized-CBFI [16] No Descriptive (𝐶G1,
𝐶G4)
Averaged – Decomposition
A-CBFI (this work) Yes Prescriptive (F1,
𝐶G4 br )
Best-
response
Staged
single→pair→triple
Direct actions +
downstream effects

3. Methodology
3.1 Setting
Let ℎ(𝑥) ∈ [0,1] be the predicted probability of the adverse class for an instance 𝑥 = (𝑥1, … , 𝑥𝑑) ∈ ℝ𝑑
described by 𝑑 features. We consider instances with ℎ(𝑥) > 𝜏 for the decision threshold 𝜏 (𝜏 = 0.5 unless
stated otherwise). An SCM ℳ = (𝒰, 𝒱, ℱ) over the features consists of three parts: a set of exogenous noise
variables 𝒰 = {𝑢1, … , 𝑢𝑑}, the endogenous variables 𝒱 = {𝑥1, … , 𝑥𝑑} (the features), and a set of structural
equations ℱ = {𝑓1, … , 𝑓𝑑}, one per feature. Each feature is given by 𝑥𝑗 = 𝑓𝑗(pa𝑗) + 𝑢𝑗, where the parents
pa𝑗 ⊆ 𝒱 ∖ {𝑥𝑗} are defined by a directed acyclic graph (DAG) 𝐺. The actionable set 𝐴 ⊆ {1, … , 𝑑} contains
the features that a person can change directly. Immutable features may still change through the SCM. We
follow the abduction –action–prediction scheme [39]. First, the instance -specific noise 𝑢̂𝑗 = 𝑥𝑗 − 𝑓𝑗(pa𝑗) is
abducted from 𝑥. Then, an intervention do(𝑥𝑆 = 𝑣) on a set 𝑆 ⊆ 𝐴 of intervened features with values 𝑣 ∈
ℝ|𝑆| replaces the equations of the features in 𝑆 by the values 𝑣. Finally, the descendants of 𝑆 are recomputed
in topological order with the abducted noise. This gives the counterfactual 𝑥cf = 𝑥do(𝑆=𝑣). Each actionable
feature may have a direction constraint (increase only or decrease only) and plausibility bounds, and these
are applied to every intervention. A recourse is an intervention with ℎ(𝑥cf) < 𝜏. Its direct -action count is
𝐿active = |𝑆|, and its cost is the MAD-scaled L1 distance between 𝑥 and 𝑥cf:
cost(𝑥, 𝑥cf) = ∑ |𝑥𝑗 cf − 𝑥𝑗| MAD𝑗𝑗 (1)
where MAD𝑗 is the median absolute deviation of feature 𝑗 on 2,000 background rows of the training data.
The cost includes downstream changes. The direct-action cost restricts the sum to 𝑗 ∈ 𝑆.
3.2 From descriptive to prescriptive CBFI
Localized-CBFI [16] decomposes a local prediction into the main effect 𝐶G1 of a feature and the pairwise
interaction 𝐶G4 of two features, and it estimates both by permutation. IGBS [17] replaced the permutation by
a do-intervention. For a set 𝑆 and values 𝑣, let 𝑔𝑆(𝑣) = ℎ(𝑥) − ℎ(𝑥do(𝑆=𝑣)) be the resulting reduction of the
adverse probability. We write 𝑔𝑖 = 𝑔{𝑖} and 𝑔𝑖𝑗 = 𝑔{𝑖,𝑗}. IGBS averaged these reductions over background
values:
𝐶G1(𝑖) = 𝐸𝑣[𝑔𝑖(𝑣)], 𝐶G4(𝑖, 𝑗) = 𝐸𝑣𝑖,𝑣𝑗[𝑔𝑖𝑗(𝑣𝑖, 𝑣𝑗) − 𝑔𝑖(𝑣𝑖) − 𝑔𝑗(𝑣𝑗)] (2)
where the expectation is taken over background rows 𝑟 drawn from the training data, with 𝑣 = 𝑟𝑆. For a pair,
𝑣𝑖 and 𝑣𝑗 are taken from the same row. These averaged scores answer a descriptive question: how much does
a feature move the prediction on average? Recourse asks a different question: what can be reached if the
value is chosen well? Therefore, A -CBFI uses the best -response (prescriptive) counterparts. They are
computed over the grid 𝑉𝑖 of allowed values of feature 𝑖 (Section 3.4) and 𝑉𝑖𝑗 = 𝑉𝑖 × 𝑉𝑗:

F1(𝑖) = max
𝑣∈𝑉𝑖
 𝑔𝑖(𝑣),  F2(𝑖, 𝑗) = max 𝑣∈𝑉𝑖𝑗  𝑔𝑖𝑗(𝑣), 𝐶G4 br(𝑖, 𝑗) = F2(𝑖, 𝑗) − F1(𝑖) − F1(𝑗) (3)
F1(𝑖) is the largest probability reduction that a single direct action on feature 𝑖 can achieve. F2(𝑖, 𝑗) is the
largest reduction that a joint action on 𝑖 and 𝑗 can achieve. If 𝐶G4 br > 0, the pair can reach further than its
members separately (super -additivity). If 𝐶G4 br < 0, the pair is redundant. The descriptive and prescriptive
versions share the CBFI decomposition, but they answer different questions. This is the main conceptual
difference from Localized -CBFI. In the escalation stage (Section 3.4), F2 is estimated as the best joint
reduction over 30 background rows (values clipped to the allowed directions and bounds). Pairs are ranked
by F2(𝑖, 𝑗) = F1(𝑖) + F1(𝑗) + 𝐶G4 br(𝑖, 𝑗). In other words, the ranking uses the single-lever gains plus the best-
response interaction.
Prescriptive reading of the CBFI groups.  CBFI [15] assigns a sample to one of four groups. The grouping
asks whether a feature 𝐹𝑥 alone and the remaining features 𝐹𝑥(−) alone each provide sufficient information
for the prediction. The four groups are main effect (G1, only 𝐹𝑥 suffices), alternative contribution (G2, only
𝐹𝑥(−) suffices), common contribution (G3, both suffice independently) and interaction (G4, neither suffices
alone). For recourse, the prediction to be sustained is the adverse one, and the groups obtain a prescriptive
meaning. A G1-type feature is a single lever. G3-type support is over-determination. If one of the supporting
features is changed, the other still sustains the adverse prediction. This means that a joint action is
necessary. G4-type support is a fragile conjunction. Changing either partner breaks it, so the partners are
substitutable single actions . We translate these groups into frequencies of successful interventions. The
following quantities are new definitions of this paper. They are not part of CBFI or Localized -CBFI. With
the success indicator 𝑠𝑆(𝑣) = 1[ℎ(𝑥do(𝑆=𝑣)) < 𝜏], 𝑠𝑖 = 𝑠{𝑖} and 𝑠𝑖𝑗 = 𝑠{𝑖,𝑗}, we define
PG1(𝑖) = Pr(𝑠𝑖 = 1),  PG3(𝑖, 𝑗) = Pr(𝑠𝑖𝑗 = 1, 𝑠𝑖 = 0, 𝑠𝑗 = 0),  PG4(𝑖, 𝑗) = Pr(𝑠𝑖 = 1, 𝑠𝑗 = 1) (4)
where the probabilities Pr are taken over values drawn as in (2). In terms of best -response gains, G3 -type
support appears as super -additivity (𝐶G4 br > 0), and G4-type support appears as sub -additivity (𝐶G4 br < 0). On
synthetic OR structures (redundant support), PG3 ≈ 0.45 and single actions succeeded for only 33.8% of
queries. On AND structures (cooperative support), PG4 ≈ 0.23 and both single actions succeeded for every
query. The sign of 𝐶G4 br identified the structure in 100% of queries. Therefore, A-CBFI moves to joint actions
by ranking pairs by F2, which contains 𝐶G4 br (the G3 side), and it uses the G4 side to report substitutable
single actions (Section 5.7). Estimating PG3 separately as an escalation signal did not help (Appendix C).
3.3 Analysis
Lemma 1 (sources of interventional interaction).  Consider two actionable features 𝑖, 𝑗 and an SCM with
additive noise. The interventional interaction 𝛿𝑖𝑗(𝑣) = 𝑔𝑖𝑗(𝑣𝑖, 𝑣𝑗) − 𝑔𝑖(𝑣𝑖) − 𝑔𝑗(𝑣𝑗) can be non -zero for
three reasons: (a) a model term, which is the second-order difference of ℎ in (𝑥𝑖, 𝑥𝑗) when neither feature is a
descendant of the other and they share no descendants; (b) a path-blocking term, which is non-zero when 𝑗 is
a descendant of 𝑖, because do(𝑥𝑗) cuts the effect of 𝑥𝑖 that flows through 𝑥𝑗; and (c) a shared -descendant
term, which is non -zero when a common descendant has a non -additive structural equation in its parents.
Model-only interaction indices (SHAP interaction values, Shapley –Taylor, H-statistic) are computed on ℎ
without the SCM. Therefore, they capture only term (a). For linear -logit models with linear structural
equations, the three terms add up exactly on the logit scale.
Proof sketch. We write the counterfactual under do(𝑆 = 𝑣) as 𝑥cf = 𝜓𝑆(𝑣; 𝑥, 𝑢̂), where 𝑢̂ is the abducted
noise. Consider models ℎ = 𝜎(𝑤⊤𝑥) that are linear in the logit, where 𝜎 is the logistic function and 𝑤 is the
coefficient vector. For the structural equation 𝑥𝑗 = 𝑎𝑥𝑖 + 𝑢𝑗  with coefficient 𝑎 , the logit interaction of

do(𝑥𝑖 = 𝑣𝑖) and do(𝑥𝑗 = 𝑣𝑗) is 𝑤𝑗𝑎(𝑣𝑖 − 𝑥𝑖). This term is non-zero although the model is additive (term b).
For 𝑥𝑘 = 𝛾𝑥𝑖𝑥𝑗 + 𝑢𝑘 with coefficient 𝛾 and ℎ depending on 𝑥𝑘 only, the interaction is −𝑤𝑘𝛾(𝑣𝑖 − 𝑥𝑖)(𝑣𝑗 −
𝑥𝑗), although ℎ does not depend on 𝑥𝑖 or 𝑥𝑗 at all (term c). The general case follows by expanding 𝜓𝑆 in the
descendants of 𝑆. Appendix B gives the details, and Section 5.1 verifies these closed forms numerically.
Proposition 1 (failure of additive and averaged targeting).  Let the adverse logit be 𝑐 − 𝛽𝑥𝑖𝑥𝑗 +
∑ 𝑤𝑘𝜑(𝑥𝑘)𝑘 + 𝑤0𝑥0 , where 𝑐  is an intercept, 𝛽 > 0  is the interaction strength, 𝜑  is a bounded
transformation and 𝑥0 is an immutable feature with weight 𝑤0. Consider an instance with 𝑥𝑖 ≈ 𝑥𝑗 ≈ 0 and a
large 𝑤0𝑥0. (i) The SHAP values and the averaged scores 𝐶G1(𝑖) and 𝐶G1(𝑗) are ≈ 0. On the logit scale, the
averaged interaction is 𝐶G4(𝑖, 𝑗) = 𝛽𝐸[(𝑣𝑖 − 𝑥𝑖)(𝑣𝑗 − 𝑥𝑗)] = 𝛽𝑥𝑖𝑥𝑗 ≈ 0  when 𝑣𝑖  and 𝑣𝑗  are uncorrelated
with mean zero in the background data. In other words, favourable and unfavourable value combinations
cancel. (ii) Suppose that no subset of 𝐾 features other than {𝑖, 𝑗} can lower the logit below 0 (the decoys have
bounded reach). Then every additive top -𝐾 rule that ranks features by SHAP, 𝐶G1 or 𝐶G1 + |𝐶G4| fails. On
the logit scale, however, F2(𝑖, 𝑗) ≈ max
(𝑣𝑖,𝑣𝑗)∈𝑉𝑖𝑗
 𝛽𝑣𝑖𝑣𝑗 grows with 𝛽, and the best -response pair rule succeeds
whenever max
(𝑣𝑖,𝑣𝑗)∈𝑉𝑖𝑗
 𝛽𝑣𝑖𝑣𝑗  exceeds the margin. Part (i) follows from the symmetry of the background
distribution, and part (ii) follows from the bounded reach of 𝜑. The proposition explains why averaged
interaction scores, including those of IGBS, cannot detect the interaction levers that matter for recourse.
3.4 The A-CBFI algorithm

Fig. 1. The A-CBFI pipeline. The prescriptive single-lever diagnosis is also the first search stage. Joint actions are
searched only when no single action reaches the decision boundary. Step 2 also returns the substitutable (G4 -type)
single actions, and Step 3 handles G3-type over-determination.
A-CBFI works in three stages (Fig. 1). Step 1 computes F1(𝑖) for every actionable feature 𝑖. It evaluates
do(𝑥𝑖 = 𝑣) for each allowed value 𝑣 ∈ 𝑉𝑖. The allowed values are quantiles of the training data, or the
observed levels of discrete features, filtered by direction and bounds. Step 2 returns the cheapest successful
single action if one exists. Therefore, the diagnosis of Step 1 is also the first search stage, and no evaluation
is spent on unused scores. Step 3 is executed only if no single action succeeds. It ranks features by F1, takes
the top 𝑀 (𝑀 = 6), and searches joint actions on the grid. In the F2-screened variant, it searches the top 𝑃
(𝑃 = 3) pairs by F2 estimated on 30 background rows, and then the top 𝑇 (𝑇 = 2) triples formed by adding
the best third feature. In the exhaustive variant (A-CBFI-topM), it searches all pairs and then all triples of the
top-𝑀 features. Among the successful candidates, the one with the minimal cost (1) is returned. In other
words, A-CBFI minimises the number of direct actions first and the cost second.
The number of model evaluations in Steps 1 –2 is ∑ |𝑉𝑖|𝑖∈𝐴  (typically 6 per feature), and it does not depend
on the number of pairs. IGBS [17] evaluated averaged scores for all features and all pairs before the search
(𝑂(|𝐴|2𝑛𝑏) evaluations for 𝑛𝑏 background samples). On our benchmarks, this cost 1142 evaluations per

query on average, compared with 119 for A -CBFI (Section 5.2). The output separates the direct actions
(𝐿active features and their new values) from the downstream changes predicted by the SCM (Section 5.6).
Because Step 1 evaluates every actionable feature, A -CBFI also returns the menu of all successful single
actions ordered by cost at no additional cost. These are the substitutable (G4-type) levers (Section 5.7).
4. Experimental setup
4.1 Datasets, actionability and SCMs
We used ten public tabular datasets (Table 2): six credit and income datasets, two health datasets and two
education datasets. For each dataset, we specified the following: which features are directly actionable (e.g.
balances, utilisation, recent inquiries, BMI and lifestyle, study time and tuition payment), which features are
immutable or not directly controllable (demographics, history, external scores, measured clinical conditions,
grades), monotonicity constraints for the actionable features (e.g. utilisation may only decrease), and a DAG
of domain relations (Appendix A). The DAGs were drafted from domain knowledge with the help of a large
language model and were reviewed by the author. Section 5.5 examines their influence. The structural
equations are linear regressions fitted on the training split. Heavy -tailed monetary variables in the Taiwan
and Give Me Some Credit data were log -transformed. Without this transformation, their median absolute
deviation is near zero and the cost (1) degenerates.
Table 2. Datasets. 𝑛: rows; 𝑑: features used; |𝐴|: directly actionable features; edges: DAG edges.
Dataset Domain 𝑛 𝑑 |𝐴| Edges Adverse outcome Source
HELOC Credit 9,871 23 7 12 RiskPerformance = Bad FICO / OpenML
45553
German Credit Credit 1,000 20 14 5 default = bad UCI
Taiwan Default Credit 30,000 13 4 9 default next month UCI 350
Give Me Some
Credit
Credit 150,000 10 4 6 distress within 2 years OpenML 46929
Adult Income Income 48,842 10 5 6 income <= 50K UCI
Lending Loan Credit 37,478 9 5 7 Charged Off Kaggle
CDC Diabetes Health 253,680 21 5 20 diabetes UCI 891
Pima Diabetes Health 768 8 5 7 Outcome = 1 UCI
Student Dropout Education 4,424 24 5 8 Dropout UCI 697
Student Performance Education 649 25 10 12 final grade G3 < 10 UCI 320

4.2 Models and protocol
For each dataset and random seed (0, 1, 2), we used a stratified 80:20 train/test split. Large datasets were
subsampled to 8,000 training rows. Three classifiers were trained on the training split: a random forest (100
trees, balanced class weights), an RBF support vector machine (balanced, Platt scaling) and XGBoost (100
trees). For each model, up to 100 test instances with ℎ(𝑥) > 0.5 were drawn at random as recourse queries.
All features were standardised with training statistics, and the background samples were 2,000 training rows.
All methods share the same SCM, constraints, grids (six quantile levels) and success criterion ℎ(𝑥cf) < 0.5.

4.3 Methods
We compare two variants of A -CBFI with six baselines. Four baselines are causal methods that search
interventions on the same SCM but select features differently (IGBS, untargeted search, LEWIS -style
recourse and SHAP -staged search). The other two are non -causal counterfactual methods (SHAP -CE and
DiCE). The methods are as follows:
• A-CBFI (Section 3.4, F2-screened escalation) and A-CBFI-topM (exhaustive escalation).
• IGBS [17]: the method of a preliminary version of this work. It ranks features by averaged interventional
scores |𝐶G1| + |𝐶G4|, prunes features below the 25th percentile (keeping at most 15) and runs an
interaction-guided beam search (width 5, depth ≤ 5, budget 500).
• Untargeted causal search: the same beam search over all actionable features without diagnosis. This is
an SCM-based recourse baseline in the spirit of [8].
• LEWIS-style causal recourse : our re-implementation of [18] on the same SCM. The sufficiency of an
action is the fraction of context neighbours (closest on immutable attributes and currently adverse)
whose abducted counterfactual becomes favourable. The cheapest action with sufficiency ≥ 0.5 that flips
the query is returned (singles first, then pairs).
• SHAP-staged: the staged search of A -CBFI with features ranked by |SHAP| (permutation SHAP, 100
background rows) instead of F1. This baseline isolates the diagnosis signal.
• SHAP-CE: a random grid search over the top max (3, ⌈0.25|𝐴|⌉) features by |SHAP| without an SCM,
and DiCE (dice-ml 0.12, random method) [4]. Both are non-causal.
We also evaluated a pair -selection rule based on the G3 frequency PG3 (eq. 4). Because it was inferior to
ranking by F2, it is reported in Appendix C.
4.4 Metrics and statistics
We report the success rate, 𝐿active, the cost (1) and the direct -action cost on successful queries. We also
report the number of model evaluations, including every evaluation spent on diagnosis or attribution. Success
is compared per query with exact McNemar tests. Costs are compared on queries where both methods
succeed, with Wilcoxon signed-rank tests and Holm correction.
5. Results
5.1 Synthetic validation of the analysis
We first verified Lemma 1 on three -node SCMs with known closed forms. We used a path -blocking
structure (𝑥1 → 𝑥2, additive logit) and a shared -descendant structure ( 𝑥3 = 𝛾𝑥1𝑥2 + 𝑢3, logit depending on
𝑥3 only). In both cases, the estimated interventional interaction matched the closed form to within 0.06 (e.g. -
1.208 vs -1.2 and -1.545 vs -1.6). The SHAP interaction index was exactly zero in both cases, and the SHAP
values of 𝑥1 and 𝑥2 were zero in the shared -descendant case. At 𝑥1 = 𝑥2 = 0, the averaged 𝐶G4 vanished in
all three mechanisms, whereas the best-response interaction was large, as Proposition 1 states.
We then planted a synergy pair in an eight -node SCM. In this SCM, the adverse risk is driven by an
immutable root, and the remaining actionable features have bounded reach (Fig. 2, left). We considered
queries where the pair is hidden ( |𝑥𝑖|, |𝑥𝑗| < 0.3) and the risk is high. On these queries, the best -response
pair rule found recourse with two actions in 86.1% of feasible queries with the true model and 92.2% with
XGBoost trained on SCM samples. The corresponding values were 7.9%/20.9% for SHAP and 10.9%/35.7%
for the averaged 𝐶G1 + 𝐶G4 score of IGBS. When the decoys themselves are strong levers (cause = lever, Fig.

2, right), all rules succeed in ≥ 89% of queries. This means that interaction -aware diagnosis is needed when
causes are immutable and levers are hidden.

Fig. 2. Success with two actions on high-risk queries with a hidden synergy pair (planted-synergy SCM). Left: the
adverse risk is driven by an immutable root. Right: control where the attributed features are also effective levers.
5.2 Benchmark results
Table 3. Recourse success (%), direct actions 𝐿active and model evaluations per query (including diagnosis), averaged
over three splits and three models. A-CBFI : untargeted counts queries solved by only one of the two methods.
Dataset Queries A-CBFI Untarg. IGBS LEWIS SHAP-
st.
SHAP-
CE
DiCE 𝐿active
A-
CBFI
𝐿active
Untarg.
Evals
A-
CBFI
Evals
Untarg.
Evals
IGBS
A-
CBFI:Untarg.
HELOC 900 62.4 58.3 59.3 33.4 53.4 33.3 43.3 1.43 1.78 349 180 1560 49:12
German Credit 334 100.0 99.7 99.7 100.0 100.0 99.7 92.8 1.01 1.20 68 500 5855 1:0
Taiwan Default 900 99.9 99.2 99.1 99.3 99.9 98.7 – 1.05 1.31 26 104 567 6:0
Give Me Some
Credit
900 97.1 96.7 96.1 96.7 96.1 94.2 – 1.04 1.27 33 103 566 5:1
Adult Income 900 87.3 86.2 84.1 84.8 87.4 94.4 94.4 1.12 1.56 117 194 888 21:11
Lending Loan 468 100.0 100.0 100.0 100.0 100.0 100.0 99.1 1.00 1.14 26 281 934 0:0
CDC Diabetes 900 98.7 98.7 98.7 98.0 98.2 97.9 94.9 1.00 1.02 11 9 774 0:0
Pima Diabetes 388 100.0 100.0 100.0 100.0 100.0 99.7 96.4 1.03 2.12 39 300 952 0:0
Student Dropout 900 32.9 32.9 32.2 7.3 28.4 25.4 – 1.34 1.39 279 47 805 6:6
Student Performance 67 89.6 92.5 92.5 55.2 76.1 70.1 – 1.25 1.35 168 162 2955 0:2
All 6657 83.4 82.6 82.3 75.2 81.3 78.6 – 1.10 1.38 119 150 1142
SHAP-CE and DiCE are non-causal (no SCM propagation); DiCE was run on the six original datasets only. LEWIS-style is a re-
implementation on the same SCM.
Table 3 summarises the results for 6,657 queries. A-CBFI solved 83.4% of all queries. The untargeted causal
search solved 82.6%, IGBS 82.3%, the LEWIS -style baseline 75.2% and SHAP -staged search 81.3%. The
non-causal SHAP-CE solved 78.6%. A-CBFI was never significantly worse than any causal baseline on any
dataset. On Adult Income, however, the non -causal DiCE and SHAP -CE solved more queries (94.4% and
94.4% vs 87.3%). Their counterfactuals ignore downstream changes. The success of A -CBFI was
significantly higher than that of the untargeted search on HELOC, Taiwan Default (McNemar p < 0.05), and
the two methods were statistically indistinguishable on the other datasets. HELOC is the clearest case. The
causes of adverse risk (delinquency, credit history, the external risk score) are not actionable, and single
changes in utilisation or balance often cannot reach the boundary. On this dataset, 35.2% of the successes of
A-CBFI came from the escalation stage.

A-CBFI prescribed 1.10 direct actions on average. This is fewer than untargeted search (1.38) and IGBS
(1.32). The LEWIS-style and SHAP-staged baselines also try single actions first. They were as sparse (1.10
and 1.08) but solved fewer queries. We counted every evaluation of every query, including failed ones. A -
CBFI needed 119 model evaluations per query on average, compared with 150, 1142 and 1857 for
untargeted search, IGBS and LEWIS-style recourse. It was cheaper than IGBS and LEWIS-style recourse on
every dataset, and cheaper than untargeted search on 6 of 10 datasets. On CDC Diabetes, HELOC, Student
Dropout, Student Performance, it was more expensive. On CDC Diabetes, this is because Step 1 evaluates
the grid of every actionable feature, while the beam search stops at its first success. On HELOC, Student
Dropout and Student Performance, many queries reach the escalation stage or fail after it. IGBS computes all
averaged scores before the search, and it required more model evaluations than untargeted search on every
dataset (1142 vs 150 on average). This means that a diagnosis pays off only when it is also the first search
stage.
Preferring fewer actions makes each action larger. On queries solved by both methods, the direct -action cost
of A-CBFI was significantly higher than that of untargeted search on 7 of 10 datasets (e.g. Adult Income
10.27 vs 8.81, German Credit 1.31 vs 1.15). It was not significantly different on CDC Diabetes (1.84 vs
1.84), Student Dropout (4.64 vs 4.62), Student Performance (2.19 vs 2.21). The reason is that one larger
change replaces two smaller ones. The cost of A -CBFI was lower than that of the LEWIS -style baseline on
10 of 10 datasets. When features were ranked by |SHAP| instead of F1 in the same staged search, success
decreased on Give Me Some Credit, HELOC, Student Dropout, Student Performance, and the evaluation
count increased by the cost of computing SHAP values.
5.3 Ablation of the escalation stage
A-CBFI uses interaction in Step 3. When no single action reaches the decision boundary, it must decide
which feature pairs to search. We tested whether best -response pair information ( F2, which adds the
interaction 𝐶G4 br to the single -lever gains) is a good basis for this decision. We kept the SCM, the grids and
the search fixed and changed only the pair -selection rule. The test used the 742 queries that no single action
could solve (HELOC 536, Adult Income 191, Pima Diabetes 10, German Credit 5; three splits, three models).
We compared F2 with four alternative signals: the additive sum F1(𝑖) + F1(𝑗), the averaged interaction of
IGBS, the sum of |SHAP| values and random pairs. We also compared it with two exhaustive references that
search all pairs and triples of the top -𝑀 single levers (A -CBFI-topM) or of all actionable features. Table 4
reports the success rate, the number of model evaluations and per-query McNemar comparisons with F2.
Table 4. Pair-selection rules in the escalation stage (Step 3) on queries that no single action could solve. Only the pair -
selection rule differs; the SCM, grids and search are identical.
Pair-selection rule Success (%) Evaluations F2 : rule (McNemar)
Best-response joint gain F2 (A-CBFI) 39.1 705 –
Averaged 𝐶G4 (IGBS) 33.4 738 59:17 (p <0.001)
Additive F1(𝑖) + F1(𝑗) 34.2 113 45:9 (p <0.001)
|SHAP| sum 30.9 36871 90:29 (p <0.001)
Random pairs 20.6 117 152:15 (p <0.001)
All pairs/triples of top-𝑀 (A-CBFI-topM) 46.4 602 0:54 (p <0.001)
All pairs/triples (exhaustive) 47.7 780 0:64 (p <0.001)

As a pair -selection signal, the best-response joint gain was better than the additive alternative (39.1% vs
34.2%), the averaged interaction of IGBS (33.4%), SHAP (30.9%) and random pairs (20.6%), all with p <
10⁻⁵. This result supports Proposition 1 on real data. However, searching all pairs and triples of the top -𝑀
single levers was even better (46.4%). It was also not more expensive (602 vs 705 evaluations), because the
direction constraints leave only a few allowed values per feature. Screening by F2 pays off only when the
search per pair is expensive (Section 5.4). Therefore, we provide both variants.
5.4 Does the advantage grow with difficulty?
A difference on a single dataset may be an artefact. Therefore, we systematically increased the difficulty of
every query. Success required ℎ(𝑥cf) < 𝜏 with 𝜏 ∈ {0.5,0.4,0.3,0.2}, and either all or a random half of the
actionable features were allowed (80 dataset×condition cells, 3 splits). A -CBFI was significantly better than
untargeted search in 33 cells and significantly worse in 0. In 6 cells, it showed a small, non-significant deficit
(at most 3.0 percentage points). Significant gains occurred on Adult Income, German Credit, Give Me Some
Credit, HELOC, Lending Loan, Pima Diabetes, Taiwan Default. With all actionable features, the mean gain
rose from 0.4 points at 𝜏 = 0.5 to 3.9 points at 𝜏 = 0.2 (Fig. 3). However, the increase depended on the
dataset. It held in 8 of 10 datasets with all features and in 5 of 10 with half of them. On CDC Diabetes,
Student Dropout, Student Performance, no condition showed a significant difference.
The escalation stage became essential on hard queries. Compared with Steps 1–2 alone, it added 7.2 points of
success at 𝜏 = 0.5 and 19.0 points at 𝜏 = 0.2 on average, and up to 52 points (German Credit). At 𝜏 = 0.2,
the exhaustive A -CBFI-topM was on average 1.2 points more successful than F2 screening. However, it
required 319 instead of 285 evaluations on average, and up to 2.9 times as many (German Credit, half
features: 1566 vs 545). Therefore, F2 screening is the cheaper option when the joint search space is large.

Fig. 3. Success gain of A-CBFI over untargeted causal search as recourse becomes harder (lower target probability 𝜏).
Grey: individual datasets; red: mean over ten datasets.
5.5 Sensitivity to the causal graph
The DAGs were not learned from data. Therefore, we re -ran A -CBFI and untargeted search on the six
original datasets (seed 0) under seven alternative SCMs: two random removals and two random reversals of
30% of the edges, the empty graph, a DAG learned with the PC algorithm (Fisher -z, 𝛼 = 0.05, causal-learn
[40]) and the reference DAG with nonlinear (gradient boosting) structural equations. Under every variant,
the success of A -CBFI was at least that of untargeted search on every dataset. This means that the
conclusions of Section 5.2 are robust.

The prescriptions of A-CBFI were also more stable. We measured the fraction of queries for which the same
direct actions were prescribed under the alternative graph and the reference graph. This fraction was higher
for A-CBFI than for untargeted search on most datasets (Fig. 4; e.g. Pima 0.87 vs 0.52, Adult 0.97 vs 0.86).
The reason is that single -lever prescriptions depend less on the propagated structure. However, the absolute
success depends on the graph when recourse relies on mediated effects. On HELOC, the success was 64.7%
with the reference DAG, but 43.0% without edges and 46.0% with the PC graph. Only 20.6% of its reference
prescriptions remained valid without propagation, because most of them work by improving the external risk
estimate. In other words, a mediated lever is valid only if the assumed mechanism is correct.

Fig. 4. Agreement of prescriptions under seven perturbed or learned SCMs with those under the reference SCM (mean
over variants).
5.6 Case studies
HELOC (random forest).  The applicant had an adverse probability of 0.75. The single -lever diagnosis
ranked netfractionrevolvingburden (0.20), numbank2natltradeswhighutilization (0.11),
netfractioninstallburden (0.07) by F1. However, no single action reached the boundary, and the untargeted
beam search failed within its budget. In the escalation stage, A -CBFI prescribed two direct actions,
netfractionrevolvingburden 37 → 0; numrevolvingtradeswbalance 7 → 2. The SCM propagates them to
numbank2natltradeswhighutilization 1 → -0.15; externalriskestimate 66 → 72.06; percenttradeswbalance 90
→ 75.78, and the adverse probability fell to 0.49 (502 model evaluations). The downstream changes are
reported as expected consequences, not as additional tasks. The slightly negative count is an artefact of the
linear structural equation (Section 6).
CDC Diabetes (random forest). For a respondent with an adverse probability of 0.57, one direct action was
enough: bmi 30 → 26 (7 evaluations). The SCM predicts downstream reductions of highbp, highchol,
heartdiseaseorattack, genhlth, physhlth, diffwalk (e.g. highbp 1 → 0.93; highchol 1 → 0.96, read as reduced
prevalence), and the probability falls to 0.49. The user receives the single prescribed action and its expected
consequences separately.
5.7 Substitutable single actions
Recourse is more useful when the person can choose among several actions [4]. Step 1 already evaluates
every actionable feature. Therefore, A -CBFI can return all successful single actions without extra model
evaluations. To measure how often such a menu exists, we used the 5,090 queries that a single action solves
on all ten datasets (three splits, three models). We counted the single actions that reach the decision
boundary and compared the cost of the second -cheapest action with that of the cheapest one. Table 5 reports
these quantities per dataset.

Table 5. Substitutable single actions on queries solved by a single action. Premium: median ratio of the cost of the
second-cheapest successful single action to that of the cheapest.
Dataset Queries ≥ 2 alternatives (%) Median alternatives Cost premium of 2nd
Lending Loan 467 99.8 4 1.94
German Credit 329 93.9 6 1.35
Taiwan Default 856 86.2 3 1.84
Give Me Some Credit 842 83.8 3 1.95
Pima Diabetes 378 83.6 2 2.30
Student Performance 47 76.6 3 1.45
CDC Diabetes 884 45.4 1 1.86
HELOC 364 42.0 1 1.68
Adult Income 709 38.5 1 2.12
Student Dropout 214 34.1 1 1.80
All 5090 68.2 2 1.91

Among these queries, 68.2% had at least two substitutable single actions (median 2). The second -cheapest
alternative cost 1.9 times as much as the cheapest one (median). The share was high on Lending Loan,
German Credit, Taiwan Default, Give Me Some Credit and Pima Diabetes (84 –99.8%) and low on CDC
Diabetes, HELOC, Adult Income and Student Dropout (34 –45%), where fewer levers act alone. We also
estimated the G4 frequency PG4 between the cheapest lever and each other feature on 30 background rows.
It ranked which alternatives succeed with an AUC of 0.87. This result is consistent with the reading of G4 -
type support as substitutability.
For the CDC respondent of Section 5.6, the menu is as follows: bmi 30 → 26 (cost 1.92, ℎ = 0.49); fruits 0
→ 1 (cost 2.09, ℎ = 0.45); veggies 0 → 1 (cost 2.59, ℎ = 0.46); physactivity 0 → 1 (cost 4.05, ℎ = 0.39).
The user can choose a larger change in one behaviour or a change in another behaviour.
6. Discussion and limitations
Main findings. The results support three claims. (i) A prescriptive diagnosis that is also the first search stage
makes causal recourse cheap and sparse. A -CBFI needed far fewer evaluations than IGBS and the
sufficiency-based LEWIS-style baseline on every dataset, and fewer than untargeted search on 6 of ten. It
also prescribed fewer direct actions than beam search on the same SCM. (ii) It is important to define
interaction as a best-response quantity. Averaged interaction scores cancel, and on real data the best-response
joint gain selected better pairs than the additive, averaged and SHAP -based alternatives. (iii) The success
gains over untargeted causal search are conditional. They appear when causes are immutable and single
actions are insufficient, and they grow on harder queries for some, but not all, datasets. We think this
conditional result is itself useful. On many standard benchmarks, one well -chosen action is enough, and the
choice of recourse method matters mainly for cost and sparsity.
Limitations. The limitations of this study are as follows. First, the SCMs are linear with additive noise, and
their DAGs were drafted with expert and LLM assistance. Binary variables are treated as continuous, which
gives fractional downstream values. A mediated lever is valid only if the assumed mechanism is correct
(Section 5.5). Second, A -CBFI optimises the predictor, not the true outcome. A lever that acts through a
proxy of the outcome may flip the model without improving the situation of the person [ 29,30]. Third, the

LEWIS-style baseline is a re-implementation, and DiCE was evaluated on six of the ten datasets. Fourth, the
preference for fewer actions increases the size of each action. Users who prefer several small changes should
use a cost -first search. Fifth, the difficulty sweep varies the target threshold and the actionable set, but not
the structure of the data-generating process. Finally, recourse prescriptions often lie in the tails of the training
distribution and transfer imperfectly across model classes. This property is shared by all the evaluated
methods.
7. Conclusion
In this paper, we changed the CBFI decomposition from a description of a prediction into a prescription for
changing it. A-CBFI scores actions by what they can reach, prescribes single actions first, and searches joint
actions only when necessary. As a result, it gives sparse causal recourse with fewer direct actions than beam
search, and it needs a fraction of the computation of its preliminary version IGBS and of sufficiency -based
recourse. Its success advantage over untargeted causal search is real but conditional. The advantage appears
where causes are immutable and levers must be combined. In future work, we will relax the linear SCM
assumption and incorporate uncertainty over the causal graph. We will also distinguish actions that improve
the outcome itself from those that only change the prediction. For this purpose, we will model the outcome
as a node of the SCM, as in improvement -focused causal recourse [29], and evaluate the method on semi -
synthetic data where the outcome mechanism is known.
Declarations
Funding. This work was supported by the National Research Foundation of Korea (NRF) grant funded by
the Korea government (MSIT) (No. RS-2026-25470060).
Competing interests. The author declares no competing interests.
Data and code availability.  All datasets are public (Table 2). Code and results are available at
https://github.com/dkumango/actionable_CBFI.
Use of generative AI.  Large language models were used to draft domain DAGs, which were reviewed by
the author and are listed in Appendix A, to assist with experiment code, and for language editing. The author
takes full responsibility for the content.
References
[1] Ribeiro MT, Singh S, Guestrin C (2016) “Why should I trust you?” Explaining the predictions of any classifier. In: Proc.
22nd ACM SIGKDD, pp 1135–1144
[2] Lundberg SM, Lee S-I (2017) A unified approach to interpreting model predictions. In: Advances in Neural Information
Processing Systems 30
[3] Wachter S, Mittelstadt B, Russell C (2017) Counterfactual explanations without opening the black box: automated
decisions and the GDPR. Harvard Journal of Law & Technology 31:841
[4] Mothilal RK, Sharma A, Tan C (2020) Explaining machine learning classifiers through diverse counterfactual
explanations. In: Proc. ACM FAT* 2020, pp 607–617
[5] Ustun B, Spangher A, Liu Y (2019) Actionable recourse in linear classification. In: Proc. ACM FAT* 2019, pp 10–19
[6] Poyiadzi R, Sokol K, Santos-Rodriguez R, De Bie T, Flach P (2020) FACE: feasible and actionable counterfactual
explanations. In: Proc. AAAI/ACM AIES, pp 344–350

[7] Pawelczyk M, Broelemann K, Kasneci G (2020) Learning model-agnostic counterfactual explanations for tabular data. In:
Proc. The Web Conference 2020, pp 3126–3132
[8] Karimi A-H, Schölkopf B, Valera I (2021) Algorithmic recourse: from counterfactual explanations to interventions. In:
Proc. ACM FAccT 2021, pp 353–362
[9] Karimi A-H, von Kügelgen J, Schölkopf B, Valera I (2020) Algorithmic recourse under imperfect causal knowledge: a
probabilistic approach. In: Advances in Neural Information Processing Systems 33
[10] Ramon Y, Martens D, Provost F, Evgeniou T (2020) A comparison of instance-level counterfactual explanation
algorithms for behavioral and textual data: SEDC, LIME-C and SHAP-C. Advances in Data Analysis and Classification
14:801–819
[11] Albini E, Long J, Dervovic D, Magazzeni D (2022) Counterfactual Shapley additive explanations. In: Proc. ACM FAccT
2022, pp 1054–1070
[12] Rathi S (2019) Generating counterfactual and contrastive explanations using SHAP. arXiv:1906.09293
[13] Mothilal RK, Mahajan D, Tan C, Sharma A (2021) Towards unifying feature attribution and counterfactual explanations:
different means to the same end. In: Proc. AAAI/ACM AIES, pp 652–663
[14] Fokkema H, de Heide R, van Erven T (2023) Attribution-based explanations that provide recourse cannot be robust.
Journal of Machine Learning Research 24(360):1–37
[15] Oh S (2022) Predictive case-based feature importance and interaction. Information Sciences 593:155–176
[16] Oh S (2026) Beyond feature attribution: recovering latent interaction structures in machine learning models via localized
CBFI. arXiv preprint arXiv:2610.34962
[17] Oh S (2026) Actionable CBFI: integrating structural decomposition and causal counterfactual recourse for tabular
machine learning. arXiv preprint arXiv:2608.27821v1
[18] Galhotra S, Pradhan R, Salimi B (2021) Explaining black-box algorithms using probabilistic contrastive counterfactuals.
In: Proc. ACM SIGMOD 2021, pp 577–590
[19] Karimi A-H, Barthe G, Balle B, Valera I (2020) Model-agnostic counterfactual explanations for consequential decisions.
In: Proc. AISTATS 2020, pp 895–905
[20] Tolomei G, Silvestri F, Haines A, Lalmas M (2017) Interpretable predictions of tree-based ensembles via actionable
feature tweaking. In: Proc. 23rd ACM SIGKDD, pp 465–474
[21] Lucic A, Oosterhuis H, Haned H, de Rijke M (2022) FOCUS: flexible optimizable counterfactual explanations for tree
ensembles. In: Proc. AAAI 2022, pp 5313–5322
[22] Laugel T, Lesot M-J, Marsala C, Renard X, Detyniecki M (2019) The dangers of post-hoc interpretability: unjustified
counterfactual explanations. In: Proc. IJCAI 2019, pp 2801–2807
[23] Upadhyay S, Joshi S, Lakkaraju H (2021) Towards robust and reliable algorithmic recourse. In: Advances in Neural
Information Processing Systems 34
[24] Pawelczyk M, Bielawski S, van den Heuvel J, Richter T, Kasneci G (2021) CARLA: a Python library to benchmark
algorithmic recourse and counterfactual explanation algorithms. In: NeurIPS Datasets and Benchmarks Track
[25] Verma S, Boonsanong V, Hoang M, Hines KE, Dickerson JP, Shah C (2020) Counterfactual explanations and
algorithmic recourses for machine learning: a review. arXiv:2010.10596
[26] Mahajan D, Tan C, Sharma A (2019) Preserving causal constraints in counterfactual explanations for machine learning
classifiers. arXiv:1912.03277
[27] Kanamori K, Takagi T, Kobayashi K, Ike Y, Uemura K, Arimura H (2021) Ordered counterfactual explanation by
mixed-integer linear optimization. In: Proc. AAAI 2021, pp 11564–11574
[28] Naumann P, Ntoutsi E (2021) Consequence-aware sequential counterfactual generation. In: Proc. ECML PKDD 2021, pp
682–698
[29] König G, Freiesleben T, Grosse-Wentrup M (2023) Improvement-focused causal recourse (ICR). In: Proc. AAAI 2023,
pp 11847–11855

[30] Miller J, Milli S, Hardt M (2020) Strategic classification is causal modeling in disguise. In: Proc. ICML 2020, pp 6917–
6926
[31] Heskes T, Sijben E, Bucur IG, Claassen T (2020) Causal Shapley values: exploiting causal knowledge to explain
individual predictions of complex models. In: Advances in Neural Information Processing Systems 33
[32] Frye C, Rowat C, Feige I (2020) Asymmetric Shapley values: incorporating causal knowledge into model-agnostic
explainability. In: Advances in Neural Information Processing Systems 33
[33] Wang J, Wiens J, Lundberg S (2021) Shapley Flow: a graph-based approach to interpreting model predictions. In: Proc.
AISTATS 2021, pp 721–729
[34] Lundberg SM, Erion G, Chen H, et al. (2020) From local explanations to global understanding with explainable AI for
trees. Nature Machine Intelligence 2:56–67
[35] Sundararajan M, Dhamdhere K, Agarwal A (2020) The Shapley Taylor interaction index. In: Proc. ICML 2020, pp 9259 –
9268
[36] Friedman JH, Popescu BE (2008) Predictive learning via rule ensembles. Annals of Applied Statistics 2(3):916–954
[37] Tsang M, Rambhatla S, Liu Y (2020) How does this interaction affect me? Interpretable attribution for feature
interactions. In: Advances in Neural Information Processing Systems 33
[38] Watson DS, Gultchin L, Taly A, Floridi L (2021) Local explanations via necessity and sufficiency: unifying theory and
practice. In: Proc. UAI 2021, pp 1382–1392
[39] Pearl J (2009) Causality: models, reasoning, and inference, 2nd edn. Cambridge University Press
[40] Zheng Y, Huang B, Chen W, et al. (2024) Causal-learn: causal discovery in Python. Journal of Machine Learning
Research 25(60):1–8
Dataset sources: FICO (2018) Explainable Machine Learning Challenge (HELOC); Hofmann H (1994) Statlog German Credit, UCI;
Yeh I-C, Lien C (2009) Expert Systems with Applications 36:2473–2480 (Taiwan default); Kaggle (2011) Give Me Some Credit;
Kohavi R (1996) KDD (Adult); Kaggle Financial Loan (Lending Club subset); CDC BRFSS 2015 via UCI 891 (CDC Diabetes
Health Indicators); Smith JW et al. (1988) Proc. SCAMC (Pima); Realinho V et al. (2022) Data 7(11):146 (Student Dropout); Cortez
P, Silva A (2008) Proc. FUBUTEC (Student Performance).

Appendix A. Actionability, constraints and causal graphs
HELOC. Not directly actionable: externalriskestimate, msinceoldesttradeopen, msincemostrecenttradeopen, averageminfile,
numsatisfactorytrades, numtrades60ever2derogpubrec, numtrades90ever2derogpubrec, percenttradesneverdelq,
msincemostrecentdelq, maxdelq2publicreclast12m, maxdelqever, numtotaltrades, percentinstalltrades,
msincemostrecentinqexcl7days, numinqlast6mexcl7days, percenttradeswbalance. Constraints: numtradesopeninlast12m ↓,
numinqlast6m ↓, netfractionrevolvingburden ↓, netfractioninstallburden ↓, numrevolvingtradeswbalance ↓,
numinstalltradeswbalance ↓, numbank2natltradeswhighutilization ↓. DAG edges: numrevolvingtradeswbalance →
percenttradeswbalance; numinstalltradeswbalance → percenttradeswbalance; numtotaltrades → percenttradeswbalance;
numinqlast6m → numinqlast6mexcl7days; numtradesopeninlast12m → numinqlast6m; netfractionrevolvingburden →
numbank2natltradeswhighutilization; netfractionrevolvingburden → externalriskestimate; numinqlast6m →
externalriskestimate; numbank2natltradeswhighutilization → externalriskestimate; percenttradesneverdelq →
externalriskestimate; maxdelqever → externalriskestimate; averageminfile → externalriskestimate.
German Credit. Not directly actionable: age, residence_history, personal_status, foreign_worker, credit_history, dependents.
Constraints: none. DAG edges: age → existing_credits; age → amount; months_loan_duration → amount; amount →
installment_rate; existing_credits → amount.
Taiwan Default. Not directly actionable: limit_bal, sex, education, marriage, age, pay_0, pay_2, pay_3, bill_amt2.
Constraints: bill_amt1 ↓, pay_amt1 ↑, pay_amt2 ↑, pay_amt3 ↑. DAG edges: age → limit_bal; education → limit_bal;
limit_bal → bill_amt1; bill_amt2 → bill_amt1; pay_amt2 → bill_amt1; pay_amt1 → pay_0; bill_amt1 → pay_0; pay_2 →
pay_0; pay_3 → pay_2.
Give Me Some Credit. Not directly actionable: age, numberoftime30_59dayspastduenotworse, numberoftimes90dayslate,
numberoftime60_89dayspastduenotworse, numberofdependents, numberrealestateloansorlines. Constraints:
revolvingutilizationofunsecuredlines ↓, debtratio ↓, monthlyincome ↑, numberofopencreditlinesandloans ↓. DAG edges: age
→ monthlyincome; age → numberofopencreditlinesandloans; monthlyincome → debtratio; numberofdependents → debtratio;
numberofopencreditlinesandloans → revolvingutilizationofunsecuredlines; numberrealestateloansorlines → debtratio.
Adult Income. Not directly actionable: age, education_num, race, sex, marital_status. Constraints: none. DAG edges: age →
education_num; age → hours_per_week; age → capital_gain; education_num → hours_per_week; education_num →
capital_gain; hours_per_week → capital_gain.
Lending Loan. Not directly actionable: annual_income, emp_length, int_rate, installment. Constraints: none. DAG edges:
annual_income → dti; annual_income → loan_amount; emp_length → int_rate; loan_amount → installment; term →
installment; loan_amount → int_rate; dti → int_rate.
CDC Diabetes. Not directly actionable: sex, age, education, income, smoker, stroke, heartdiseaseorattack, anyhealthcare,
nodocbccost, diffwalk, genhlth, menthlth, physhlth, highbp, highchol, cholcheck. Constraints: bmi ↓, physactivity ↑, fruits ↑,
veggies ↑, hvyalcoholconsump ↓; bmi ∈ [18.5, 100]. DAG edges: age → highbp; age → highchol; bmi → highbp; bmi →
highchol; physactivity → bmi; hvyalcoholconsump → highbp; smoker → highbp; education → income; income →
physactivity; bmi → genhlth; physactivity → genhlth; highbp → genhlth; age → genhlth; genhlth → physhlth; bmi →
diffwalk; age → diffwalk; highbp → heartdiseaseorattack; highchol → heartdiseaseorattack; age → heartdiseaseorattack;
smoker → heartdiseaseorattack.
Pima Diabetes. Not directly actionable: age, pregnancies, diabetespedigreefunction. Constraints: none. DAG edges: age →
pregnancies; age → bloodpressure; age → glucose; bmi → bloodpressure; bmi → skinthickness; bmi → insulin; glucose →
insulin.
Student Dropout. Not directly actionable: marital_status, course, daytime, prev_grade, admission_grade, displaced,
special_needs, gender, age_enroll, international, cu1_enrolled, cu1_evaluations, cu1_approved, cu1_grade, cu2_approved,
cu2_grade, unemployment, inflation, gdp. Constraints: debtor ↓, tuition_up_to_date ↑, scholarship ↑, cu2_enrolled ↑,
cu2_evaluations ↑. DAG edges: debtor → tuition_up_to_date; scholarship → tuition_up_to_date; tuition_up_to_date →
cu2_enrolled; cu2_enrolled → cu2_evaluations; cu2_evaluations → cu2_approved; cu1_approved → cu2_approved;
cu2_approved → cu2_grade; cu1_grade → cu2_grade.
Student Performance. Not directly actionable: school, sex, age, address, famsize, pstatus, medu, fedu, failures, health, famrel,
romantic, higher, traveltime, freetime. Constraints: studytime ↑, absences ↓, goout ↓, dalc ↓, walc ↓, paid ↑, internet ↑,
schoolsup ↑, famsup ↑. DAG edges: freetime → goout; goout → walc; goout → dalc; walc → absences; dalc → absences;

dalc → health; walc → health; medu → higher; higher → studytime; paid → studytime; address → traveltime; traveltime →
studytime.
Appendix B. Proof details for Lemma 1
Let 𝑆 ⊆ 𝐴  and write 𝑥do(𝑆=𝑣)  for the counterfactual obtained by replacing the equations of 𝑆  and recomputing
descendants with abducted noise. For two actionable features 𝑖, 𝑗 define the change 𝛥𝑆 = 𝑥do(𝑆=𝑣) − 𝑥, and let de(𝑖)
denote the set of causal descendants of 𝑖  in 𝐺 . If 𝑗 ∉ de(𝑖), 𝑖 ∉ de(𝑗) and de(𝑖) ∩ de(𝑗) = ∅, then 𝛥𝑖𝑗 = 𝛥𝑖 + 𝛥𝑗
coordinate-wise. In this case, 𝛿𝑖𝑗 reduces to the second -order difference of ℎ, which is the model term. If 𝑗 ∈ de(𝑖), the
intervention do(𝑥𝑗) fixes 𝑥𝑗 and blocks every path 𝑖 → ⋯ → 𝑗 → ⋯, so 𝛥𝑖𝑗 = 𝛥𝑖 + 𝛥𝑗 − 𝛥𝑖 via 𝑗, where 𝛥𝑖 via 𝑗 is the part
of 𝛥𝑖 transmitted through 𝑥𝑗. For linear ℎ (or to first order), this yields the non-zero path-blocking term 𝛻ℎ⊤𝛥𝑖 via 𝑗 in the
reduction 𝛿𝑖𝑗, where 𝛻ℎ is the gradient of the model. If de(𝑖) ∩ de(𝑗) ≠ ∅ and a common descendant 𝑘 has a non -
additive equation in its parents, then 𝛥𝑖𝑗,𝑘 ≠ 𝛥𝑖,𝑘 + 𝛥𝑗,𝑘, where 𝛥𝑖,𝑘 denotes the 𝑘-th coordinate of 𝛥𝑖. This produces the
shared-descendant term even when ℎ is additive in 𝑥𝑘. Model-only interaction indices evaluate ℎ on (𝑥𝑖, 𝑥𝑗) without 𝛥.
Therefore, they cannot contain the last two terms.
Appendix C. Negative results for the G3/G4 frequencies
PG3 as an escalation signal.  On the 1,567 queries of the ten datasets that no single action solves, ranking pairs by the
G3 frequency PG3 (eq. 4, 30 background rows) succeeded in 28.5% of queries, compared with 29.7% for F2, 27.1% for
the additive rule and 34.1% for exhaustive search over the top -𝑀 pairs and triples. Per query, PG3 solved 17 queries
that F2 did not and missed 36 that it solved (exact McNemar p = 0.013). Against exhaustive top -𝑀 search, the counts
were 0 vs 89. A frequency of joint -only flips over random background values is a noisier estimate of joint necessity
than the best-response gain. Therefore, we do not use it for search.
Difficulty prediction.  The maximum PG1 over actionable features predicted whether a query is solvable by a single
action with an AUC of 0.97 (max F1: 0.90), and the maximum PG3 predicted whether an unsolved -by-single query is
solvable by escalation with an AUC of 0.77. However, computing these frequencies (about (𝑀 + 𝑀(𝑀 − 1)/2) · 30
evaluations) costs more than running Steps 1 –3 directly. This means that the profile is useful only to explain why a
query is hard, not to save computation.
