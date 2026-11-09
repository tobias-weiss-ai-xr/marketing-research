---
title: 'From Preference to Reciprocity: Decentralized Matching with Empirically Grounded LLM-agent Based
  Modeling'
url: https://arxiv.org/abs/2609.34679
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Wangxuan Fan
- Xiaoyu Nie
- Zhoutian Shi
- Xiangcheng Meng
- Shipei Zeng
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.34679
pages: 36
chars: 104584
fetched_at: '2026-11-08T13:20:36+00:00'
kb_version: 1
---

# From Preference to Reciprocity: Decentralized Matching with Empirically Grounded LLM-agent Based Modeling

Preprint. Under review.
FROMPREFERENCE TORECIPROCITY: DECENTRAL-
IZEDMATCHING WITHEMPIRICALLYGROUNDED
LLM-AGENTBASEDMODELING
Wangxuan Fan∗ Xiaoyu Nie∗ Zhoutian Shi Xiangcheng Meng
Shipei Zeng Pin Gao Yan Hu † Zhongxiang Dai†
The Chinese University of Hong Kong, Shenzhen
{wangxuanfan,xiaoyunie,zhoutianshi,xiangchengmeng}@link.cuhk.edu.cn
{gaopin,huyan,daizhongxiang}@cuhk.edu.cn shipei.zeng@sribd.cn
ABSTRACT
Bipartite matching is a fundamental problem in game theory and market design.
Classical approaches such as Gale–Shapley assume complete preferences and cen-
tralized computation, whereas many real-world matching processes are decentral-
ized, asynchronous, and shaped by sequential interaction under limited informa-
tion. We propose a dynamic bipartite matching framework that combines large
language model (LLM) agents with contextual bandits. In a simulated Chinese
marriage market, economically grounded LLM agents evaluate locally encoun-
tered candidates, while agent-specific Logistic-UCB models learn reciprocal ac-
ceptance from realized proposal outcomes. The mechanism therefore separates
two decisions—whom do I like?andwho is likely to like me back?—without re-
quiring ex ante market-wide preference rankings. We first validate LLM-induced
mate preferences against the empirical conditional-logit reference across multiple
LLM backbones. In the50×50matching experiment, Bandit-UCB achieves the
highest mean mutual welfare (56.01 versus 54.87 for Gale–Shapley), a smaller
gender rank gap than the classical baselines, and the fewest blocking pairs among
the LLM-ABM policies. Learned acceptance models show economically inter-
pretable gender-differentiated associations, while counterfactual setups reveal no
systematic unilateral advantage from prior search knowledge. Overall, these re-
sults support the advantages of decentralized matching with LLM-based behav-
ioral modeling and online learning under incomplete information for economic
simulation and computational social science research.
1 INTRODUCTION
Two-sided matching is a fundamental problem in game theory and market design, with applica-
tions ranging from labor markets and school choice to marriage markets (Gale & Shapley, 1962;
Kamecke, 1992; Roth & Sotomayor, 1992). The classical Gale–Shapley deferred-acceptance algo-
rithm (Gale & Shapley, 1962) guarantees a stable matching by taking agents’ ordinal preference
rankings as given. While this formulation has been highly successful as a normative allocation
mechanism, it abstracts away from several features of naturally occurring matching processes (Eyu-
poglu et al., 2021; Axtell & Kimbrough, 2008; Zhang & Fang, 2024): agents typically observe
only a limited set of alternatives, interactions occur sequentially and asynchronously, and prefer-
ences or feasible opportunities may be learned only through experience. Moreover, stability does
not necessarily coincide with aggregate welfare. Both analytical and computational studies have
shown that restricting attention to stable outcomes can impose a non-negligible welfare cost (Axtell
& Kimbrough, 2008; Boudreau & Knoblauch, 2013; Chen et al., 2021; Ortega et al., 2024). These
∗Equal contribution.
†Corresponding author.
1
arXiv:2609.34679v1  [cs.LG]  28 Sep 2026

Preprint. Under review.
observations motivate a complementary view of matching: rather than asking only how to compute
an allocation given a complete preference profile, we study how preference information, beliefs, and
matches can jointly evolve through decentralized interaction.
Agent-based modeling (ABM) provides a natural bottom-up framework for such a perspective. By
specifying heterogeneous agents, local information, and interaction rules, ABMs generate aggre-
gate outcomes from repeated individual decisions (Epstein, 2012; Axtell & Farmer, 2025). This is
particularly relevant to marriage markets, where individual partner choices depend on the current
pool of available alternatives, while every new relationship changes that pool for subsequent deci-
sions (Kalmijn, 1998; Chiappori & Weiss, 2006; Van Bavel & Grow, 2016; Grow, 2019). Axtell &
Kimbrough (2008), for example, replace centralized deferred acceptance with decentralized search,
proposal, and rematching, achieving higher average welfare without preserving guaranteed stability,
which is not necessarily a strict desideratum in marriage markets. Yet decentralizing thematch-
ing processdoes not by itself solve the problem ofpreference formation: candidate rankings still
need to be specified before the matching dynamics begin. This is a central difficulty in agent-based
marriage-market modeling. As emphasized by Grow (2019), theories of mate choice are oftencom-
peting,multidimensional, andverbalrather than directly mathematical, forcing modelers to translate
behavioral assumptions into hand-designed utility functions and parameterizations.
Large language models (LLMs) provide a novel way to operationalize semantically rich behavioral
assumptions. Existing studies show that LLM agent-based modeling (LLM-ABM) can condition de-
cisions on heterogeneous personas and contextual information and can be embedded in agents that
interact over extended trajectories (Argyle et al., 2023; Aher et al., 2023; Park et al., 2023). How-
ever, we do not treat an LLM as an unconstrained oracle of human preferences: expressive behavior
is not necessarily economically valid behavior, motivating careful specification and validation when
LLMs are used as simulated economic actors (Horton et al., 2023; Ludwig et al., 2024). Nor do
we provide the agents with market-wide preference rankings in advance, or let them infer the re-
sults in one-shot. Instead, LLM valuation is triggered only when agents encounter one another. Yet
knowing how much an agent values a candidate does not reveal whether that candidate will recipro-
cate. Because the proposer observes acceptance only after making a proposal, reciprocity becomes a
sequential learning problem under partial feedback. This naturally motivates an agent-specific con-
textual bandit that learns, from realized interactions, which desirable candidates are likely to accept.
Unlike matching-bandit approaches that learn latent rewards or unknown preference rankings (Liu
et al., 2021; Dai & Jordan, 2021; Cen & Shah, 2022), our framework separatesbehavioral evalu-
ationfrominteraction learning: the LLM determines how much an agent values an encountered
candidate, while the bandit learns how likely that candidate is to accept.
Based on this separation, we develop a decentralized and asynchronous bipartite matching frame-
work that combines behaviorally grounded LLM agents with agent-specific contextual bandits. In
the marriage-market setting, agents encounter only locally available alternatives, evaluate them
through LLM-based preferences, and learn reciprocal acceptance from realized outcomes, with-
out requiring complete rankings in advance. Experiments on a simulated Chinese marriage market
validate the behavioral grounding of the agents and show favorable welfare–stability outcomes rel-
ative to classical and decentralized baselines, while learned acceptance models and counterfactual
experiments reveal structured reciprocal-choice patterns and the limits of unilateral information ad-
vantages.
Our contributions are threefold:
•Empirically grounded LLM-agent based modeling.We develop a general approach for
constructing and validating LLM agents from domain-specific empirical evidence, and in-
stantiate it in a marriage market using socioeconomic characteristics and gender-specific
mate-preference evidence. We validate the induced preferences against an empirical refer-
ence across multiple LLM backbones and market scales.
•Decoupled decentralized matching mechanism.We formulate matching as an asyn-
chronous local-interaction process that separates LLM-based partner valuation from agent-
specific reciprocity learning, without requiring agents to access complete preference rank-
ings. For a theoretically calibrated variant, we establish local proposal-regret bounds under
realizable and dynamically misspecified acceptance models.
2

Preprint. Under review.
•Economic evaluation and interpretable results.We show that the proposed framework
preserves the core two-sided matching problem while relaxing strong information assump-
tions, and achieves better overall welfare–stability outcomes. The learned reciprocal-
acceptance models yield economically interpretable patterns, while warm-start counterfac-
tuals reveal how prior market knowledge translates into individual and market-level match-
ing outcomes.
Our code is publicly available in our GitHub repository. Related work is reviewed in Appendix A.
2 EMPIRICALLYGROUNDEDLLM-AGENTMODELING
2.1 SYNTHETICPOPULATION WITHEMPIRICALHETEROGENEITY
Our modeling principle is to construct LLM agents from domain-specific empirical evidence rather
than unconstrained persona generation. This requires identifying behaviorally relevant observable
characteristics and preserving important population heterogeneity and dependence structures. The
resulting structured profiles provide both the population representation and the empirical basis for
downstream LLM-based behavioral evaluation.
We instantiate this approach in a synthetic Chinese marriage market. Each agent is endowed with
attributes emphasized in empirical studies of mate choice (Zhou et al., 2023), includingage, income,
education, family background, housing status, and physical appearance. These dimensions capture
thegender heterogeneityandsocial-class differencesdocumented in the empirical reference.
Following the dependency-aware construction of Li et al. (2026), we sample demographic vari-
ables to approximate observed population heterogeneity while preserving key relationships, such
as income–education dependence, rather than treating attributes independently. Demographic and
economic variables are based on the 2015 National 1% Population Sample Survey of China (Popula-
tion Census Office under the State Council & Department of Population and Employment Statistics,
National Bureau of Statistics, 2016), consistent with the period studied by Zhou et al. (2023), while
physical appearance is sampled from an approximately normal distribution based on empirical evi-
dence (Hamermesh & Biddle, 1993). Full sampling details and realized population composition are
reported in Appendix B.
2.2 LLM PERSONAS ANDMATEPREFERENCE
Each structured profile is rendered as a concise public persona containing only observable attributes
available to potential partners, ensuring that LLM evaluations use the same information encoded in
the demographic profile. The rendering template is provided in Appendix C.
To model mate preferences, we construct gender-specific prompts grounded in the regression ev-
idence of Zhou et al. (2023) and use chain-of-thought prompting (Wei et al., 2022) to structure
evaluation. The full private preference prompts are given in Appendix C.2.
2.3 VALIDATION OFMODELING
As discussed in Appendix A, validating persona-conditioned decisions is important for establishing
the economic interpretability of LLM-based social simulations. We therefore compare the mate-
preference rankings induced by our LLM agents with an empirical reference model derived from
Zhou et al. (2023). The reference model maps each candidate profile to a conditional-logit utility
under the corresponding gender-specific specification, while the LLM assigns an overall desirability
score from the evaluator’s public persona and private mate-preference prompt. We evaluate ranking
agreement using Kendall’sτ, weighted pairwise violation rate (WPVR), and top-Koverlap, with
definitions provided in Appendix D.
Figure 1 reports the validation results for a10×10market across five random seeds. Across all
three LLM backbones, preference-structured prompts achieve stronger alignment with the empirical
reference than the no-CoT baseline, indicating that the result is not specific to a single backbone. A
50×50scale-up validation is reported in Appendix F.
3

Preprint. Under review.
Male evaluators Female evaluators
0.0
0.2
0.4
0.6
0.8
1.0Mean across five seeds
(A) Kendall's τ (higher is better)
Male evaluators Female evaluators
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(B) WPVR (lower is better)
Male evaluators Female evaluators
0.0
0.2
0.4
0.6
0.8
1.0Mean across five seeds
(C) Hit@3 (higher is better)
Male evaluators Female evaluators
0.0
0.2
0.4
0.6
0.8
1.0
(D) Hit@5 (higher is better)
DeepSeek CoT Qwen CoT GPT-OSS CoT No-CoT baseline
Figure 1: Empirical-reference alignment in the 10×10 validation task. Bars show means across five
seeds and error bars show standard deviations.
Male
Female
0.36 0.25 0.12 0.14 0.02 0.82
0.31 0.64 -0.07 0.78 0.53 0.22
DeepSeek CoT
0.50 0.26 0.13 0.12 0.11 0.76
0.52 0.54 0.00 0.68 0.45 0.23
Qwen CoT
Age
Income Family
background
HousingEducationAppearance
Male
Female
0.32 0.24 -0.00 0.12 -0.00 0.83
0.21 0.74 0.02 0.62 0.63 0.28
GPT-OSS CoT
Age
Income Family
background
HousingEducationAppearance
0.68 0.34 0.10 0.29 0.32 0.30
0.58 0.62 0.08 0.60 0.25 0.19
No-CoT baseline
−0.2
0.0
0.2
0.4
0.6
0.8
Pearson correlation
Figure 2: Dimension-consistency heatmap for agents in the 10×10 validation. Entries report Pearson
correlations between overall desirability and dimension-level scores, averaged across five seeds.
4

Preprint. Under review.
Figure 2 provides a complementary internal-consistency diagnostic. Appearance is most strongly
associated with overall desirability for male agents, whereas female evaluations are more closely
associated with socioeconomic dimensions, particularly housing, income, and education. These pat-
terns are consistent with the gender-specific preference structure documented by Zhou et al. (2023),
while the no-CoT baseline fails to reproduce the same structure. Results for the50×50setting are
reported in Appendix F.
3 DECENTRALIZEDMATCHINGSYSTEM
3.1 A DECENTRALIZED ANDASYNCHRONOUSMATCHINGMARKET
We consider a two-sided marriage market with male agentsM={m 1, . . . , mNM }, female agents
W={w 1, . . . , wNW }, and populationA=M ∪ W. At periodt,µ t(i)denotes agenti’s current
partner, withµ t(i) =∅ifiis single andµ t(i) =j⇔µ t(j) =i. A match is eithertemporary
orpermanent. Temporary relationships remain contestable and can be replaced by later accepted
proposals, whereas permanently matched agents exit the active market.
The market evolves through decentralized and asynchronous activation. At the beginning of period
t, letA act t ⊆ Adenote agents that have not entered permanent matches. A period consists of|Aact t |
sequential activation opportunities, each sampling one agent uniformly with replacement from this
set. Thus, an agent may be activated multiple times within a period or not at all.
Activation does not give an agent access to the entire opposite side of the market. When agenti
is activated, it observes only a locally available candidate setC t(i)⊆ Pt(i), whereP t(i)denotes
the set of currently feasible agents on the opposite side who have not entered permanent matches
and the candidate setC t(i)is randomly sampled from this feasible pool. Decisions therefore depend
on both preferences and locally encountered opportunities. This differs from Gale–Shapley (Gale
& Shapley, 1962), which uses complete rankings in a centralized procedure, and from Axtell &
Kimbrough (2008), which decentralizes interaction but retains pre-specified preference lists.
3.2 WHOMDOI LIKE? LOCALLLM VALUATION
The first decision of an activated agent is a valuation problem:whom do I like?For evaluatori
and locally observed candidatej, the simulated agent in Section 2 produces a normalized subjective
utility represented by an overall preference score:
Ui(j)∈[0,1], U i(j)̸=U j(i)in general.(1)
The asymmetry is essential:i’s valuation ofjdoes not reveal whetherjwould reciprocate.
Letr i denote agenti’s reservation utility, the minimum acceptable partner utility. Its current bench-
mark is
bi,t =
(
ri, µ t(i) =∅,
max{ri, Ui(µt(i))}, µ t(i)̸=∅.
(2)
For eachj∈ Ct(i), define the utility improvement and eligible set by
∆Uij,t =U i(j)−b i,t,E t(i) ={j∈ Ct(i) : ∆Uij,t > ϵU , ϵU ≥0}.(3)
This eligibility condition separatespreferencefromstrategic search: only candidates preferred to
the current benchmark are considered, so reciprocal-acceptance learning cannot make an otherwise
undesirable candidate attractive. The LLM determines whom the agent wants; the remaining uncer-
tainty is which of these desirable candidates are likely to reciprocate.
3.3 WHOISLIKELY TOLIKEMEBACK? LOCALRECIPROCAL-ACCEPTANCELEARNING
The second decision concerns reciprocity:who is likely to like me back?Ifiproposes toj, the
receiver independently evaluatesiagainst its current benchmark,
bR j,t =
(
rj, µ t(j) =∅,
max{rj, Uj(µt(j))}, µ t(j)̸=∅. (4)
5

Preprint. Under review.
The realized response is
Yi→j,t =1

Uj(i)> bR j,t 	 ∈ {0,1}.(5)
Crucially, proposeridoes not observeU j(i), the receiver’s incumbent valuation, or its eventual
decision before proposing. Acceptance is revealed only after a proposal is made, so feedback is
observed only for candidates actually approached. Because proposal opportunities are limited, the
proposer must balance exploiting candidates believed likely to reciprocate with exploring uncertain
candidates whose responses are informative. This sequential decision problem with contextual,
partial feedback naturally motivates an agent-specific contextual bandit.
For each exposed candidatej, proposeriobserves a dyadic contextx (i) j,t =ϕ(z i, zj)∈R d con-
structed from the public personasz i andz j, and learns only from proposals it actually makes. Its
local history isH i,t ={(x (i) n , y(i) n )}Ni,t n=1. Unchosen candidates generate no label, and histories
are not shared across agents. The context construction and information restrictions are detailed in
Appendix G.
We approximate reciprocal acceptance using an agent-specific logistic working model,
pθi (x) :=σ(θ ⊤ i x), σ(z) = 1 1 +e −z .(6)
This is an approximation based on proposer-observable information: the receiver’s private bench-
mark changes with its current relationship, so acceptance probabilities need not follow a fixed lo-
gistic law even for the same public dyadic context. To balance exploitation and exploration, we
augment the fitted logit predictor with local uncertainty:
s(i) j,t =
r
x(i) j,t ⊤ V −1 i,t x(i) j,t,
pUCB,i ij,t =σ  bθ⊤ i,tx(i) j,t +β i,ts(i) j,t  . (7)
Here, bθi,t is fitted by localL 2-regularized logistic regression,V i,t is the corresponding regularized
Fisher-information matrix, andβ i,t controls exploration. The estimator and practical Logistic-UCB
derivation are provided in Appendix K.
Preference and reciprocal uncertainty are finally combined through
Iij,t = ∆Uij,tpUCB,i ij,t , j∈ E t(i).(8)
If the true acceptance probabilities conditional on the proposer’s current information were known,
maximizing their product with∆U ij,t would maximize expected one-step utility improvement
(Proposition L.1). Equation 8 replaces these probabilities with optimistic estimates from the work-
ing model, allocating proposals among already desirable candidates.
Theorem (Informal) 1(Local learning under dynamic misspecification).Under the boundedness
and predictability assumptions in Appendix L, fix a proposer whose true conditional acceptance
probabilities differ from a fixed logistic reference by at most a predictable envelopeη n for every
eligible candidate at attemptn. Logistic-UCB with the norm-constrained estimator and envelope-
calibrated confidence radii specified there satisfies, with probability at least1−δ,
RN ≤ eO

d √ N+
vuutdN NX
n=1
η2n +
NX
n=1
ηn

 .(9)
HereNcounts this proposer’s attempts,dis the context dimension, andR N measures cumulative
expected one-step improvement lost relative to an oracle facing the same eligible candidates and
knowing their true acceptance probabilities. The notation suppresses logarithmic factors, with other
problem constants fixed. Realizable acceptance (η n ≡0) recovers eO(d √ N)regret. For fixedd,
RN /N→0if0≤η n ≤1and PN n=1 ηn =o(N/logN).
In Appendix, Theorems L.1 and L.2 establish these local bounds along the learner’s realized market
trajectory formally.
6

Preprint. Under review.
3.4 DECENTRALIZEDMATCHINGPROTOCOL
When activated, agenti, either male or female, constructs the eligible setE t(i)and may make at
mostLproposals. LetR (q) t (i)denote the eligible candidates not yet approached before attemptq,
withR (1) t (i) =E t(i). At each attempt, the proposer selects the candidate with the highest proposal
index and observes the binary response:
j∗ = arg max
j∈R(q) t (i) Iij,t, y ∗ =Y i→j∗,t.(10)
The observation(x (i) j∗,t, y∗)is appended to proposeri’s local history, and its logistic model and
uncertainty estimate are updated. Following rejection,j ∗ is removed from the current search set
and proposal indices are recomputed before the next attempt. Following acceptance, any temporary
relationships involvingiorj ∗ are dissolved, their displaced partners return to the active market, and
(i, j∗)becomes a new temporary pair. The current activation then terminates.
At the end of periodt, each temporary pair independently becomes permanent with probability
ρt, which is named as lock or commitment probability. Permanently matched agents leave sub-
sequent search, while the remaining temporary pairs stay contestable. The active population and
feasible candidate pools are updated before the next period. The process continues until the max-
imum horizonTis reached or no active agents remain. Hence, the final allocation emerges from
repeated local exposure, bilateral LLM evaluation, proposal feedback, agent-specific learning, and
endogenous relationship revision rather than from a one-shot centralized procedure. The eligibility
and acceptance rules imply strict bilateral improvement for every accepted rematching, although
matched-pair welfare need not be monotone because displaced partners create externalities; these
properties are formalized in Appendix L. The full executable procedure of the algorithm is provided
in Appendix M.
Table 1:50×50market size matching results. Values are means±standard deviations over 50
seeds; bold, underlined, and italic mean values denote first, second, and third place among methods
for which each outcome metric is defined. The “Info required” column summarizes the information
regime, including both ex ante preference access and whether pairwise valuations are generated only
after local encounter.
Method Info required Mutual welfare↑Rank gap↓#Blocking↓Proposals↓
Baselines
Gale–Shapley Whole 54.87±0.29 2.74±0.530.00±0.00873.14±20.24
LLM-solver Whole 54.63±0.50 2.57±1.18 9.40 ±10.71 N/A
Axtell–Kimbrough Partial 54.73±0.39 2.43±0.83 19.90±14.02 31504.70±4280.30
LLM-ABM
Random eligible Local55.24±0.621.54±0.68 38.00±17.42 13781.90 ±2349.29
Utility-only Local 55.92 ±0.48 1.84 ±0.75 17.58±12.26 16753.14±2876.91
Bandit-UCBLocal56.01±0.592.11±0.7316.28±12.7616591.78±2376.70
4 EXPERIMENTS
4.1 VALIDATIONEXPERIMENTSETUP
Because behavioral validation establishes the basis for the matching mechanism, its results are pre-
sented earlier in Section 2.3; here we specify the experimental protocol. In each10×10validation
run, 10 male and 10 female evaluators score all 10 opposite-gender candidates, producing both an
overall desirability score and six dimension-level scores for every directional evaluation. We repeat
the experiment over five random seeds and compare four scoring conditions with three LLM back-
bones: DeepSeek-V4-Pro CoT, Qwen3.7-Plus CoT, GPT-OSS-120B CoT, and a no-CoT baseline
that omits the gender-specific mate-preference specification. Full metric definitions, the50×50
scale-up validation, and cross-backbone results are reported in Appendices D, F, and E.
4.2 MARKET-LEVELMATCHINGRESULTS
We evaluate the complete matching system on the same50×50synthetic marriage market. Di-
rectional LLM desirability scores are computed once for all cross-gender dyads as the evaluation
7

Preprint. Under review.
benchmark. These scores provide complete preference rankings for Gale & Shapley (1962), Axtell
& Kimbrough (2008), and a direct LLM-solver following Hosseini et al. (2026), which generates a
matching from the ranked inputs in one-shot. In contrast, LLM-ABM agents access valuations and
update rankings only when the corresponding candidates are locally encountered. The implemen-
tation and experimental results demonstrate the effectiveness of solving the bipartite problem using
distinct baselines and the proposed method.
We compare these baselines with three LLM-ABM proposal policies under common outcome met-
rics, reporting means and standard deviations over 50 random seeds. All three policies share the
same market dynamics: Random eligible samples uniformly from eligible candidates, Utility-only
selects the largest immediate utility improvement, and Bandit-UCB combines this improvement with
an optimistic estimate of reciprocal acceptance. We setρ= 0.05for both Axtell–Kimbrough and
the LLM-ABM policies. Detailed settings and metric definitions are provided in Appendix H.
Table 1 illustrates the trade-offs between information requirements, welfare, stability, and search
intensity. Gale–Shapley achieves zero blocking pairs but has the largest mean gender rank gap.
Axtell–Kimbrough relaxes centralized coordination while retaining pre-specified rankings, requiring
approximately 31,505 proposals. Despite receiving complete rankings, the LLM-solver produces
9.40 blocking pairs on average. It achieves fewer blocking pairs than the decentralized methods,
but lower mean mutual welfare and a larger mean rank gap than all three LLM-ABM policies. Its
proposal count is reported as N/A because direct matching generation does not involve a comparable
sequence of market proposals.
All three LLM-ABM policies achieve higher mean mutual welfare than the baselines using only
encounter-based information. Within this family, Random eligible yields the smallest rank gap and
fewest proposals, but the most blocking pairs. Utility-only improves welfare and reduces blocking,
while Bandit-UCB achieves the highest mean welfare (56.01) and lowest blocking count (16.28).
Its gains over Utility-only are modest and accompanied by a larger rank gap (2.11 versus 1.84),
reflecting trade-offs among welfare, stability, and gender balance. These results support the poten-
tial of decentralized matching without complete ex ante rankings and suggest incremental benefits
from reciprocity learning. Sensitivity to exploration and commitment parameters is examined in
Appendix J.
4.3 INTERPRETING THELEARNEDBANDITMODELS
Beyond guiding proposals, the bandit models summarize learned associations between observable
dyadic characteristics and reciprocal acceptance. Figure 3 presents aggregated private proposer-
specific Logistic-UCB coefficients in Panel 3a and a pooled receiver-perspective diagnostic in
Panel 3b. In the local models, age-gap coefficients are negative for both proposer genders, whereas
income and education coefficients are positive. The appearance coefficient is larger among male
proposers, while the education coefficient is larger among female proposers. These differences con-
cern acceptance predictions: male-proposer models predict responses from female receivers, and
vice versa. They therefore should not be interpreted as the proposers’ own valuation weights. The
negative same-family-background coefficients likewise describe conditional predictive associations,
rather than direct preferences against similar backgrounds.
The pooled diagnostic is fitted to realized proposals after simulation and is never available to agents
during matching. Under its receiver-to-proposer feature orientation, negative income, education, and
appearance coefficients associate favorable proposer characteristics with greater acceptance. Income
has a larger coefficient magnitude for female receivers, whereas appearance has a larger magnitude
for male receivers. These estimates complement the local models but need not coincide with them
because the conditioning and aggregation differ. Both panels provideassociational diagnostic evi-
dence: proposal observations are endogenously selected by the matching policy, and acceptance also
depends on receivers’ current relationships. The coefficients thus characterize predictive patterns in
realized interactions rather than identify structural or causal preference parameters.
4.4 COUNTERFACTUALINFORMATIONADVANTAGE
We finally ask whether prior matching-market experience creates a unilateral advantage in a new
market. In the individual warm-start counterfactual, one designated male agent receives Logistic-
8

Preprint. Under review.
Age gap Income gapEducation gapSame backgroundHousing advantageAppearance gap
1.0
0.5
0.0
0.5
1.0
1.5
Local coefficient
Male proposers Female proposers
(a) Local private models
Age gapIncome gapEducation gapSame backgroundHousing advantageAppearance gap
Male receivers
Female receivers
+1.62 -7.84 -1.68 -3.11 -2.19 -4.42
+3.67 -11.84 -2.12 -2.84 -2.42 -2.61
10
5
0
5
10
Pooled coefficient
(b) Post-hoc receiver diagnostic
Figure 3: Learned reciprocal-acceptance structure under Bandit-UCB. Panel (a) reports aggregated
coefficients from private proposer-specific models; Panel (b) reports a pooled receiver-perspective
diagnostic fitted after simulation and used only for interpretation.
0.0 0.2 0.4 0.6 0.8 1.0
Share of male focal agents
Own rank
Own score
Proposals
11
11
22
26
26
13
13
25
Improved Unchanged Worsened
5
 0 5
 rank
Own rank (11/50 improved)
5
 0 5
 score
Own score (11/50 improved)
100
 0 100
 proposals
Proposals (22/50 improved)
Figure 4: Individual warm-start effects across the 50 male focal agents. Effects are same-seed
treatment–control mean differences over ten held-out seeds and are oriented so that positive values
indicate improvement. The upper panel classifies focal agents by the sign of the effect; the lower
panels report the corresponding effect distributions.
UCB coefficients learned from prior simulations, while all others retain the standard cold-start spec-
ification. Across the 50 male focal agents evaluated over ten held-out seeds in Figure 4, 11 improve
their own tied rank and score, 26 remain unchanged, and 13 worsen. Proposal counts fall for 22
agents and rise for 25. Thus, prior search knowledge benefits some agents but worsens outcomes for
9

Preprint. Under review.
Table 2: Market-level counterfactual results for male-side information advantage. M rank and F rank
denote the average ranks of matched male and female agents for their realized partners, respectively.
Method Initial knowledge Mutual welfare↑M rank↓F rank↓Rank gap↓#Blocking↓Proposals↓
Gale–Shapley (men-proposing) Complete rankings 54.87±0.29 16.74±0.39 19.48±0.32 2.74±0.53 0.00±0.00 873.14±20.24
Cold-start Bandit-UCB Local 55.84±0.33 16.48±0.47 18.56±0.46 2.08±0.70 16.70±8.21 15829.50±2462.34
All-male warm-start Bandit-UCB Pooled maleθ55.71±0.44 16.56±0.73 18.68±0.47 2.12±0.76 15.80±4.66 15136.70±2210.78
slightly more, providing no systematic individual advantage. The full focal-agent distribution and
paired evaluation protocol appear in Appendix I.
Table 2 considers a stronger intervention: all male agents enter with pooled male-proposer coeffi-
cients. Relative to cold-start Bandit-UCB, mean mutual welfare and gender rank gap remain almost
unchanged, while fewer proposals and blocking pairs suggest reduced search burden and slightly
improved stability. The limited welfare effect reflects a defining feature of two-sided matching:
better proposal beliefs do not remove receivers’ right to reject, and shared information can inten-
sify same-side competition. Individual knowledge may therefore yield local gains, but its limited
market-wide benefit when widely shared is consistent with the constraints imposed by reciprocal
choice and same-side competition.
5 DISCUSSION
In conclusion, we propose a decentralized matching framework that integrates LLM-based behav-
ioral valuation with adaptive reciprocity learning. This framework facilitates the study of how di-
verse individual evaluations influence collective matching outcomes through repeated interactions.
By decoupling behavioral representation from the interaction mechanism, researchers can indepen-
dently vary behavioral assumptions, information access, and institutional rules to analyze their inter-
active effects. This enables computational experiments linking empirically informed agent behavior
with economic mechanism design. This modeling approach can be applied to labor markets, col-
laborative partnerships, and other contexts where local opportunity discovery and mutual agreement
are crucial. Limitations and future directions are discussed in Appendix N.
AIUSE STATEMENT
In this work, we used generative AI tools to improve the clarity and fluency of English writing and
to assist with code implementation and debugging. All AI-assisted text was reviewed and revised
by the authors, and all AI-assisted code was manually inspected, tested, and verified for correctness.
We did not use generative AI tools to generate research ideas, scientific claims, experimental results,
data, or citations. We take full responsibility for the final content of this work, including all text,
claims, code, and artifacts produced with the aid of generative AI.
REPRODUCIBILITY STATEMENT
The code for our framework is publicly available athttps://github.com/YuanJrShiuan/
LLM_ABM_Bipartite_Matching_for_Marriage. Experimental settings and implementa-
tion details are provided in the appendices.
REFERENCES
Yasin Abbasi-Yadkori, D´avid P´al, and Csaba Szepesv´ari. Improved algorithms for linear stochastic
bandits.Advances in neural information processing systems, 24, 2011.
Gati V . Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using large language models to simulate
multiple humans and replicate human subject studies. InProceedings of the 40th International
Conference on Machine Learning, volume 202 ofProceedings of Machine Learning Research,
pp. 337–371. PMLR, 2023.
10

Preprint. Under review.
Jacy Reese Anthis, Ryan Liu, Sean M Richardson, Austin C. Kozlowski, Bernard Koch, Erik Bryn-
jolfsson, James Evans, and Michael S. Bernstein. Position: LLM social simulations are a promis-
ing research method. InForty-second International Conference on Machine Learning Position
Paper Track, 2025. URLhttps://openreview.net/forum?id=cRBg1dtj7o.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples.Political Anal-
ysis, 31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
Robert L Axtell and J Doyne Farmer. Agent-based modeling in economics and finance: Past, present,
and future.Journal of Economic Literature, 63(1):197–287, 2025.
Robert L. Axtell and Steven O. Kimbrough. The high cost of stability in two-sided matching: How
much social welfare should be sacrificed in the pursuit of stability? InProceedings of the 2008
World Congress on Social Simulation, 2008.
James W Boudreau and Vicki Knoblauch. Preferences and the price of stability in matching markets.
Theory and decision, 74(4):565–589, 2013.
David M Buss. Sex differences in human mate preferences: Evolutionary hypotheses tested in 37
cultures.Behavioral and brain sciences, 12(1):1–14, 1989.
David M Buss and David P Schmitt. Sexual strategies theory: an evolutionary perspective on human
mating.Psychological review, 100(2):204, 1993.
Sarah H. Cen and Devavrat Shah. Regret, stability & fairness in matching markets with bandit learn-
ers. InProceedings of the 25th International Conference on Artificial Intelligence and Statistics,
volume 151 ofProceedings of Machine Learning Research, pp. 8938–8968. PMLR, 2022.
Jiehua Chen, Piotr Skowron, and Manuel Sorge. Matchings under preferences: Strength of stability
and tradeoffs.ACM Transactions on Economics and Computation, 9(4):1–55, 2021.
Yiting Chen, Tracy Xiao Liu, You Shan, and Songfa Zhong. The emergence of economic rationality
of gpt.Proceedings of the National Academy of Sciences, 120(51):e2316205120, 2023.
Pierre-Andr´e Chiappori and Yoram Weiss. Divorce, remarriage, and welfare: A general equilibrium
approach.Journal of the European Economic Association, 4(2-3):415–426, 2006.
Xiaowu Dai and Michael I. Jordan. Learning strategies in decentralized matching markets under
uncertain preferences.Journal of Machine Learning Research, 22(260):1–50, 2021.
Kingsley Davis. Intermarriage in caste societies.American anthropologist, 43(3):376–395, 1941.
Alice H Eagly, Paul W Eastwick, and Mary Johannesen-Schmidt. Possible selves in marital roles:
The impact of the anticipated division of labor on the mate preferences of women and men.
Personality and Social Psychology Bulletin, 35(4):403–414, 2009.
Joshua M Epstein.Generative social science: Studies in agent-based computational modeling.
Princeton University Press, 2012.
Selin Eyupoglu, Muge Fidan, Yavuz Gulesen, Ilayda Begum Izci, Berkan Teber, Baturay Yilmaz,
Ahmet Alkan, and Esra Erdem. Stable marriage problems with ties and incomplete prefer-
ences: An empirical comparison of asp, sat, ilp, cp, and local search methods.arXiv preprint
arXiv:2108.05165, 2021.
Sarah Filippi, Olivier Capp ´e, Aur ´elien Garivier, and Csaba Szepesv ´ari. Parametric bandits: The
generalized linear case. InAdvances in Neural Information Processing Systems, volume 23, pp.
586–594, 2010.
David Gale and Lloyd S Shapley. College admissions and the stability of marriage.The American
mathematical monthly, 69(1):9–15, 1962.
Andr´e Grow. How to design agent-based marriage market models: A review of current prac-
tices.Simulieren und Entscheiden: Entscheidungsmodellierung, Modellierungsentscheidungen,
Entscheidungsunterst¨utzung, pp. 59–83, 2019.
11

Preprint. Under review.
George Gui and Olivier Toubia. The challenge of using llms to simulate human behavior: A causal
inference perspective.arXiv preprint arXiv:2312.15524, 2023.
Daniel S Hamermesh and Jeff Biddle. Beauty and the labor market, 1993.
Anne Lundgaard Hansen, John J Horton, Sophia Kazinnik, Daniela Puzzello, and Ali Zarifhonarvar.
Simulating the survey of professional forecasters.Available at SSRN 5066286, 2026.
Yuzhi Hao and Danyang Xie. A multi-llm-agent-based framework for economic and public policy
analysis.China Journal of Econometrics, 5(3):615–630, 2025.
John J Horton, Apostolos Filippas, and Benjamin S Manning. Large language models as simulated
economic agents: What can we learn from homo silicus? Technical report, National Bureau of
Economic Research, 2023.
Hadi Hosseini, Samarth Khanna, and Ronak Singh. Matching markets meet llms: Algorithmic
reasoning with ranked preferences.Advances in Neural Information Processing Systems, 38:
18977–19023, 2026.
Matthijs Kalmijn. Intermarriage and homogamy: Causes, patterns, trends.Annual review of sociol-
ogy, 24(1):395–421, 1998.
Ulrich Kamecke. Two sided matching: A study in game-theoretic modeling and analysis, 1992.
Lihong Li, Yu Lu, and Dengyong Zhou. Provably optimal algorithms for generalized linear con-
textual bandits. InProceedings of the 34th International Conference on Machine Learning, vol-
ume 70 ofProceedings of Machine Learning Research, pp. 2071–2080. PMLR, 2017.
Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. EconAgent: Large language model-
empowered agents for simulating macroeconomic activities. InProceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 15523–
15536. Association for Computational Linguistics, 2024. doi: 10.18653/v1/2024.acl-long.829.
Xiaomin Li, Yuexing Hao, Jianheng Hou, Jintao Huang, Qianfeng Wen, Shirley Huang, Yifan Liu,
Xiaoyi Liu, Yilan Fan, Yijun Wang, et al. Matraix: Simulating the world with 8.3 billion persona
agents.arXiv preprint arXiv:2608.04205, 2026.
Yuantong Li, Chi-Hua Wang, Guang Cheng, and Will Wei Sun. Dynamic matching bandit for two-
sided online markets.arXiv preprint arXiv:2205.03699, 2022.
Lydia T. Liu, Feng Ruan, Horia Mania, and Michael I. Jordan. Bandit learning in decentralized
matching markets.Journal of Machine Learning Research, 22(211):1–34, 2021.
Jens Ludwig, Sendhil Mullainathan, and Ashesh Rambachan. Large language models: An applied
econometric framework.Annual Review of Economics, 18, 2024.
Miller McPherson, Lynn Smith-Lovin, and James M Cook. Birds of a feather: Homophily in social
networks.Annual review of sociology, 27(1):415–444, 2001.
Robert K Merton. Intermarriage and the social structure: Fact and theory.Psychiatry, 4(3):361–374,
1941.
Josu´e Ortega, Gabriel Ziegler, and R Pablo Arribillaga. Unimprovable students and inequality in
school choice. Technical report, QBS Research Paper, 2024.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interactive simulacra of human behavior. InProceedings
of the 36th annual acm symposium on user interface software and technology, pp. 1–22, 2023.
Population Census Office under the State Council and Department of Population and Employment
Statistics, National Bureau of Statistics.Tabulation on the 2015 1% Population Sampling Survey
of the People’s Republic of China. China Statistics Press, Beijing, 2016. Micro-data collected in
November 2015, commonly known as China’s mini-census.
12

Preprint. Under review.
Alvin E Roth and Marilda Sotomayor. Two-sided matching.Handbook of game theory with eco-
nomic applications, 1:485–541, 1992.
Haoyang Shang, Zhengyang Yan, and Xuan Liu. Love first, know later: Persona-based romantic
compatibility through llm text world engines.arXiv preprint arXiv:2512.11844, 2025.
Jan Van Bavel and Andr´e Grow. Introduction: Agent-based modelling as a tool to advance evolu-
tionary population theory. InAgent-based modelling in population studies: Concepts, methods,
and applications, pp. 3–27. Springer, 2016.
Jean E Veevers. The “real” marriage squeeze: Mate selection, mortality, and the mating gradient.
Sociological Perspectives, 31(2):169–189, 1988.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny
Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models.Advances in
neural information processing systems, 35:24824–24837, 2022.
Yuzhe Yang, Yifei Zhang, Minghao Wu, Kaidi Zhang, Yunmiao Zhang, Honghai Yu, Yan Hu, and
Benyou Wang. Twinmarket: A scalable behavioral and social simulation for financial markets.
Advances in Neural Information Processing Systems, 38:63469–63519, 2026.
Marcel Zentner and Alice H Eagly. A sociocultural framework for understanding partner preferences
of women and men: Integration of concepts and evidence.European Review of Social Psychology,
26(1):328–373, 2015.
Marcel Zentner and Klaudia Mitura. Stepping out of the caveman’s shadow: Nations’ gender gap
predicts degree of sex differentiation in mate preferences.Psychological science, 23(10):1176–
1185, 2012.
YiRui Zhang and Zhixuan Fang. Decentralized two-sided bandit learning in matching market. In
The 40th Conference on Uncertainty in Artificial Intelligence, 2024.
Jiaxu Zhou, Jen tse Huang, Xuhui Zhou, Man Ho Lam, Xintao Wang, Hao Zhu, Wenxuan Wang,
and Maarten Sap. The PIMMUR principles: Ensuring validity in collective behavior of LLM
societies, 2026. URLhttps://openreview.net/forum?id=I88toT6Leg.
Yang Zhou, Jia Yu, and Yu Xie. Gender differences and social class heterogeneity in mate prefer-
ences: An exploratory study based on the choice experiment approach.Sociological Studies, (6):
107–130, 2023. ISSN 1002-5936. URLhttp://sociologyol.ruc.edu.cn/shxyj/
fzshx/shfc/e96e3fbb12db4abe8eaff950c1bf9211.htm. In Chinese.
A RELATEDWORK
A.1 LLM SOCIALSIMULATION
A growing literature studies LLMs as conditional behavioral models and as components of interac-
tive social and economic simulations (Argyle et al., 2023; Park et al., 2023; Horton et al., 2023; Chen
et al., 2023; Gui & Toubia, 2023; Ludwig et al., 2024; Hansen et al., 2026; Hao & Xie, 2025; Li
et al., 2024; Yang et al., 2026). The evidence is promising but not uniformly generalizable: persona
conditioning, model choice, and task design can materially affect simulated behavior. Recent work
therefore emphasizes explicit validation targets and careful interpretation of collective LLM-agent
behavior (Anthis et al., 2025; Zhou et al., 2026; Ludwig et al., 2024). Our paper follows this view by
treating the LLM as a behaviorally expressive component of the matching system rather than as an
unconstrained oracle, and by validating the induced mate preferences against an empirical reference
before studying market-level outcomes.
13

Preprint. Under review.
A.2 MATEPREFERENCE FORMARRIAGE
Mate-choice research offers several partially competing explanations of partner preference, includ-
ing evolutionary psychology (Buss, 1989; Buss & Schmitt, 1993), sociocultural and social-role the-
ories (Eagly et al., 2009; Zentner & Mitura, 2012; Zentner & Eagly, 2015), status and resource
exchange (Davis, 1941; Merton, 1941; Kalmijn, 1998), homogamy and homophily (Kalmijn, 1998;
McPherson et al., 2001), and hypergamy or mating-gradient theories (Veevers, 1988). Because
these theories are often verbal, multidimensional, and only partly formalized, translating them into
fixed quantitative utility functions can be restrictive (Grow, 2019). Our behavioral specification is
grounded primarily in the choice experiment of Zhou et al. (2023), which studies six mate-preference
dimensions, including physical appearance, and documents substantial heterogeneity across gender
and social class. The LLM is used to operationalize this evidence within heterogeneous personas
without imposing a single hand-crafted mate-value function.
A.3 BIPARTITEMATCHING ANDLEARNING
Recent work has used LLMs either as solvers over ranked preferences (Hosseini et al., 2026) or
as centralized engines for persona-based compatibility estimation (Shang et al., 2025). A separate
literature studies matching under bandit feedback, including decentralized learning, stability, fair-
ness, and two-sided uncertainty (Liu et al., 2021; Dai & Jordan, 2021; Cen & Shah, 2022; Zhang &
Fang, 2024; Li et al., 2022). Our framework differs from both lines by separatingpartner valuation
fromreciprocal-acceptance learning: LLM agents evaluate only locally encountered candidates,
while agent-specific contextual bandits learn acceptance probabilities from realized binary proposal
outcomes. For the latter component, we use a logistic contextual-bandit construction motivated by
generalized-linear bandit methods (Filippi et al., 2010; Li et al., 2017).
B PERSONASAMPLING ANDDEPENDENCYSTRUCTURE
This appendix documents the synthetic population used throughout the validation and matching ex-
periments. The six observable persona dimensions follow the empirical setting described in Sec-
tion 2. Rather than sampling every attribute independently, the construction preserves selected
socioeconomic dependencies so that the resulting agents are coherent as joint profiles rather than
independent attribute bundles. Table 3 summarizes the sampling structure, and Table 4 reports the
realized composition of the 100-agent market used in the main experiments.
Table 3: Persona dimensions and sampling structure.
Dimension Values or scale Sampling and dependency structure
Age 20–50 Sampled from marriage-market-active age
groups according to the target population
distribution.
Income Monthly RMB income Generated conditional on educational attain-
ment around a reference monthly income of
1830 RMB.
Education Middle school or below; high
school; university and above
Sampled from population education proportions
and aggregated into three experimental cate-
gories.
Family background Urban; rural Sampled from the corresponding urban/rural
population composition.
Housing Owns house; no house Sampled conditionally on age, gender, and fam-
ily background.
Appearance Below average; average; attrac-
tive
Sampled from an approximately bell-shaped
distribution, with most probability mass as-
signed to average appearance.
14

Preprint. Under review.
Table 4: Realized composition of the 100-agent synthetic marriage market.
Attribute Male (n=50) Female (n=50) Overall (n=100)
Mean age 36.60 34.62 35.61
Mean monthly income 1881.24 RMB 1712.88 RMB 1797.06 RMB
Middle school or below 70% 72% 71%
High school 10% 14% 12%
University and above 20% 14% 17%
Urban family background 58% 56% 57%
Owns house 42% 40% 41%
Attractive appearance 8% 18% 13%
Average appearance 78% 66% 72%
Below-average appearance 14% 16% 15%
C PROMPTTEMPLATES FORLLM PERSONAS ANDMATEPREFERENCES
This appendix records the prompt templates used in the experiments. Public personas are deter-
ministic natural-language renderings of the sampled attributes, whereas the private mate-preference
prompt is available only to the evaluating agent. For each directional dyadic evaluation, the model
receives the evaluator’s public profile, the candidate’s public profile, and the evaluator’s gender-
specific private preference specification.
C.1 PUBLICPERSONARENDERINGTEMPLATE
Public persona template
For each generated profile, render the public persona as:
A [age]-year-old [gender] with [education phrase]. Financially, this individual earns a monthly
income of [actual monthly income] RMB (approximately [annual income] RMB per year) and
[housing phrase]. [family-background phrase]. In terms of physical appearance, this person is
evaluated as having an [appearance] appearance.
The structured fields stored with the persona are:agent id,gender,age,
actual monthly income,family background,housing,education level,
appearance, andshort description.
Dyadic scoring user message
YOUR OWN PUBLIC PROFILE (for Step 0 self-calibration)
Agent ID: [evaluator id]
Gender: [evaluator gender]
Age: [evaluator age]
Actual Monthly Income: [evaluator income] RMB
Family Background: [evaluator family background]
Housing: [evaluator housing]
Education Level: [evaluator education level]
Appearance: [evaluator appearance]
Short Description: [evaluator public persona]
CANDIDATE PUBLIC PROFILE (to evaluate)
Agent ID: [candidate id]
Gender: [candidate gender]
Age: [candidate age]
Actual Monthly Income: [candidate income] RMB
Family Background: [candidate family background]
15

Preprint. Under review.
Housing: [candidate housing]
Education Level: [candidate education level]
Appearance: [candidate appearance]
Short Description: [candidate public persona]
Evaluate the candidate strictly following your private preference theory. Output only the JSON
object; do not include markdown fences or extra commentary.
C.2 PRIVATEMATE-PREFERENCEPROMPTS
Male-agent private mate-preference prompt
You are a male agent in a simulated marriage market. You will evaluate opposite-gender candi-
dates using two inputs: your own public profile and the candidate’s public profile. Both profiles
contain age, actual monthly income, family background, housing, education level, appearance,
and short description.
Use the following internal five-step evaluation protocol before assigning scores. Do not output
your full reasoning chain. Only output structured dimension scores, an overall desirability score,
and a brief explanation.
Paper-aligned preference theory.Male agents place the strongest relative emphasis on physical
appearance. Income, housing, education, and family background still matter, but they are sec-
ondary. Candidate age has a negative effect when the candidate is older relative to the evaluator.
The evaluator’s own public profile should be used for self-positioning and relative comparison,
but it must not overturn the main gender-specific priority structure.
Step 0: Self-profile calibration.Inspect your own age, income, housing, education, family
background, and appearance. Use your own age as the reference point for relative age fit. Use
your own socioeconomic and appearance profile to calibrate expectations mildly and realistically.
Step 1: Appearance-dominant baseline check.Evaluate the candidate’s appearance first.
below averagereceives a large negative penalty;averageis an acceptable neutral baseline;
attractivereceives a strong positive premium. Appearance should be the most important
upward adjustment for male agents.
Step 2: Relative age disutility.Compare the candidate’s age with your own age. Desirability
should decrease smoothly as the candidate becomes older relative to you. Younger or similar-age
candidates should be evaluated more favorably than clearly older candidates.
Step 3: Secondary income and housing adjustment.Treat 1830 RMB/month as the baseline
monthly disposable income. Higher candidate income should increase desirability moderately.
Home ownership receives a positive bonus relative to no house. These socioeconomic compar-
isons remain secondary to appearance.
Step 4: Education and family-background screening.Evaluate education in the order
university and above>high school>middle school and below. Urban
family background may receive a very small bonus, but family background should have weak
influence on the final score.
Scoring instructions.Return dimension scores on a 0–100 scale:age fit,
income fit,family background fit,housing fit,education fit, and
appearance fit. Returnoverall desirabilityon a 0–100 scale. Do not compute
overall desirabilityas a simple average of dimension scores; it must reflect the prior-
ity structure above. Do not mention statistical coefficients, formulas, or the paper name. Keep
brief reasonunder 150 characters.
Output schema.{evaluator id, candidate id, dimension scores:
{age fit, income fit, family background fit, housing fit,
education fit, appearance fit}, overall desirability,
brief reason}.
The implemented prompt additionally includes few-shot calibration examples emphasizing that
an attractive candidate can outrank a more socioeconomically advantaged but below-average-
looking candidate, and that age fit is evaluated relative to the male evaluator.
16

Preprint. Under review.
Female-agent private mate-preference prompt
You are a female agent in a simulated marriage market. You will evaluate opposite-gender candi-
dates using two inputs: your own public profile and the candidate’s public profile. Both profiles
contain age, actual monthly income, family background, housing, education level, appearance,
and short description.
Use the following internal five-step evaluation protocol before assigning scores. Do not output
your full reasoning chain. Only output structured dimension scores, an overall desirability score,
and a brief explanation.
Paper-aligned preference theory.Female agents place the strongest relative emphasis on so-
cioeconomic resources and social-stratum indicators, especially housing, actual income, edu-
cation, and family background. Physical appearance still matters, especially when it is below
average, but it should not dominate socioeconomic resources. Candidate age has a negative ef-
fect when the candidate is older relative to the evaluator. The evaluator’s own public profile
should be used for self-positioning and relative comparison, but it must not overturn the main
female-agent priority structure.
Step 0: Self-profile calibration.Inspect your own age, income, housing, education, family
background, and appearance. Use your own age as the reference point for relative age fit. Use
your socioeconomic profile to calibrate expectations mildly and realistically.
Step 1: Socioeconomic resource gatekeeping.First evaluate the candidate’s housing and ac-
tual monthly income.owns housereceives a large positive bonus;no housereceives a clear
penalty, especially when income is also low. Treat 1830 RMB/month as the baseline monthly dis-
posable income. Higher income should translate into a strong monotonic increase in desirability.
Income and housing should be more decisive than appearance.
Step 2: Education and family-background alignment.Evaluate education in the order
university and above>high school>middle school and below. University
education receives a strong bonus; middle school or below receives a clear penalty. Urban family
background receives a distinct positive bonus relative to rural background. Education and family
background matter because they signal social stratum and class alignment.
Step 3: Appearance threshold check.Evaluate appearance after socioeconomic and class-
related traits.below averagereceives a meaningful negative penalty;averageis accept-
able;attractivereceives a positive bonus. The attractiveness bonus should not override
serious disadvantages in housing, income, education, and family background.
Step 4: Relative age sensitivity.Compare the candidate’s age with your own age. Desirability
should decrease as the candidate becomes older relative to you. Apply a clear penalty for sub-
stantially older candidates. The age penalty for female agents should be at least as strong as, and
often stronger than, the male-agent age penalty.
Scoring instructions.Return dimension scores on a 0–100 scale:age fit,
income fit,family background fit,housing fit,education fit, and
appearance fit. Returnoverall desirabilityon a 0–100 scale. Do not compute
overall desirabilityas a simple average of dimension scores; it must reflect the priority
structure above. Avoid excessive ties. Use decimal scores when candidates are close. Do not
mention statistical coefficients, formulas, or the paper name. Keepbrief reasonunder 150
characters.
Output schema.{evaluator id, candidate id, dimension scores:
{age fit, income fit, family background fit, housing fit,
education fit, appearance fit}, overall desirability,
brief reason}.
The implemented prompt additionally includes few-shot calibration examples emphasizing that
socioeconomic resources and class-alignment indicators can dominate attractiveness, and that
income and housing are traded off rather than reduced to a single attribute.
17

Preprint. Under review.
D VALIDATIONMETRICS
Lets ij denote the LLM desirability score assigned by evaluatorito candidatej, and letu ij denote
the corresponding utility from the gender-specific conditional-logit reference based on Zhou et al.
(2023). All ranking metrics are computed at the evaluator level and then aggregated across evaluators
and seeds.
Kendall’sτ.We report Kendall’sτ b, which accounts for ties,
τi = Ci −D iq
(Ci +D i +T (s) i )(Ci +D i +T (u) i ) ,(11)
whereC i andD i are concordant and discordant candidate pairs, whileT (s) i andT (u) i count pairs
tied only under the LLM score and reference utility, respectively. Higher values indicate stronger
ordinal agreement.
Weighted pairwise violation rate (WPVR).To place more weight on reversals between candi-
dates that are well separated by the reference model, we use
WPVRi =
P
a<b 1{(sia −s ib)(uia −u ib)<0} |uia −u ib|P
a<b |uia −u ib| .(12)
Lower values indicate fewer economically consequential ranking reversals.
Top-Koverlap.Agreement among the highest-ranked candidates is measured by
Overlap@Ki =

TopKLLM i ∩TopK Ref i

K .(13)
The labelsHit@3andHit@5in the main validation figure use this same set-overlap definition.
Because random overlap depends on candidate-pool size, these values should not be compared me-
chanically between the10×10and50×50settings.
Dimension consistency.As an internal diagnostic, we compute Pearson correlations between
overall desirability and each of the six dimension-level scores, separately by evaluator gender. This
checks whether the decomposition follows the intended gender-specific structure, but it is not an in-
dependent behavioral validation because both quantities are generated by the same LLM evaluation.
E ROBUSTNESSACROSSLLM BACKBONES
Table 5 reports the10×10validation across DeepSeek, Qwen, GPT-OSS, and the no-CoT specifica-
tion. For both evaluator genders, all preference-structured prompts achieve higher Kendall’sτand
lower WPVR than the no-CoT baseline. Although the absolute alignment varies across backbones,
the direction of the improvement is consistent, suggesting that the empirical-reference alignment is
not specific to a single LLM.
Table 5:10×10reference-alignment results across LLM backbones. Values are means±standard
deviations across five random seeds.
Model MaleτFemaleτMale WPVR Female WPVR
DeepSeek CoT 0.692±0.076 0.572±0.082 0.064±0.025 0.122±0.027
Qwen CoT 0.708±0.115 0.646±0.072 0.055±0.035 0.089±0.022
GPT-OSS CoT 0.666±0.103 0.502±0.092 0.073±0.042 0.158±0.030
No-CoT baseline 0.286±0.065 0.400±0.085 0.298±0.055 0.236±0.053
18

Preprint. Under review.
F 50×50 SCALE-UPVALIDATION
We repeat the preference validation on the full 100-agent population. Each of the 50 male and
50 female evaluators scores all 50 opposite-gender candidates, yielding 2,500 cross-gender dyads
and 5,000 directional evaluations. Table 6 reports the exact alignment statistics, while Figure 5
additionally shows dimension-level consistency. Kendall’sτand WPVR remain broadly comparable
to the10×10results, indicating that ordinal alignment persists as the candidate pool expands; top-K
overlap is naturally more demanding in the larger pool.
Table 6: DeepSeek alignment with the empirical preference reference in the50×50validation
market.
Metric Male evaluators Female evaluators
Kendall’sτ0.703±0.054 0.607±0.082
WPVR 0.054±0.018 0.105±0.039
Overlap@3 0.460±0.187 0.473±0.232
Overlap@5 0.684±0.133 0.448±0.186
Kendall's τ WPVR Hit@3 Hit@5
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
(A) DeepSeek CoT 50x50 oracle alignment
Age
Income Family
background
Housing EducationAppearance
Male
Female
0.48 0.28 0.12 0.12 0.16 0.78
0.30 0.69 0.14 0.64 0.65 0.30
(B) 50x50 dimension consistency
−0.2
0.0
0.2
0.4
0.6
0.8
Male Female
Figure 5: DeepSeek validation in the50×50market. Panel (a) reports reference-alignment metrics
by evaluator gender; Panel (b) reports dimension-consistency correlations.
G CONTEXTCONSTRUCTION FORLOCALRECIPROCAL-ACCEPTANCE
LEARNING
This appendix specifies the six-dimensionaldyadic compactrepresentation used by the local
Logistic-UCB models. For proposeriand candidatej, the context is written asx (i) j,t =ϕ(z i, zj)∈
R6, wherez i andz j contain the six public persona attributes introduced in Section 2. The represen-
tation summarizes only information observable before a proposal; it is intended to predict reciprocal
acceptance, not to reconstruct the receiver’s private utility function.
Table 7: Features in the local reciprocal-acceptance context. Gap and advantage variables follow the
proposer-oriented encoding used in the implementation.
Feature Interpretation
Age gap Age mismatch between proposer and candidate
Income gap Relative income difference
Education gap Relative education difference
Same background Indicator for shared family background
Housing advantage Relative housing-status advantage
Appearance gap Relative appearance difference
19

Preprint. Under review.
The decentralization constraint excludes receiver-side private quantities such asU j(i),U j(µt(j)),
andb R j,t, as well as the receiver’s complete ranking, future accept/reject decision, other proposers’
outcomes, and the parameters or histories of other local models. Agentilearns only from its own
realized proposal historyH i,t ={(x (i) n , y(i) n )}Ni,t n=1. A candidate who is observed but not approached
therefore generates no label rather than a rejection. This preserves the partial-feedback structure
required by the contextual-bandit interpretation.
H MAINMATCHINGEXPERIMENTSETTINGS ANDMETRICS
H.1 EXPERIMENTALPROTOCOL
The main experiment uses the same 50 male and 50 female agents described in Section 2. The LLM-
solver leverages DeepSeek-V4-Pro as the centralized solver, the same backbone of our LLM-ABM
markets of 50×50. For every ordered cross-gender dyad, the validated LLM preference model
produces a directional scores i(j)∈[0,100]: Gale–Shapley, Axtell–Kimbrough and LLM-solver
receive the preference information required by their mechanisms, whereas an LLM-agent gets its
preference only after the local encounter.
The “Info required” column in Table 1 summarizes this distinction.Wholedenotes complete market-
wide preferences available before matching;Partialdenotes decentralized interaction that still be-
gins from pre-specified preference lists; andLocaldenotes the proposed encounter-based regime, in
which no pairwise valuation or ranking is available to an agent before local exposure.
Table 8: Main LLM-ABM parameter configuration used in Table 1.
Parameter Value
Market size 50 male agents and 50 female agents
Repeated runs 50 random seeds
Main matching LLM scorer DeepSeek V4 Pro, temperature= 0.5, CoT prompt
Matching horizonT= 500periods
Candidate set size 25 candidates per activation when more are available
Reservation utilityr= 0.25on the normalized utility scale
Lock probabilityρ= 0.05per temporary relationship per period
Utility thresholdϵ U = 0.01
Logistic-UCB coefficientβ= 1.0
Logistic regularizationλ= 1.0
Proposal cost and switching cost 0
The three LLM-ABM policies share the same market dynamics and differ only in proposal selec-
tion.Random eligiblesamples uniformly from utility-improving candidates;Utility-onlychooses
the largest immediate utility gain; andBandit-UCBmaximizes∆U ij,tpUCB,i ij,t . Hence, Utility-only
isolates the incremental role of reciprocal-acceptance learning, while Random eligible provides a
non-strategic decentralized-search baseline.
H.2 EVALUATIONMETRICS
LetP(µ) ={(m, w) :µ(m) =w, m∈ M, w∈ W}denote the set of realized male–female pairs.
Mutual welfare.We report average bilateral desirability,
Mutual(µ) = 1 |P(µ)| X (m,w)∈P(µ) sm(w) +s w(m) 2 .(14)
This rewards matches that are jointly valued by both partners rather than optimizing one side alone.
Realized rank and gender rank gap.Using score-based tied ranks,
ranki(j) = 1 +
X
k∈C−i
1{si(k)> si(j)},(15)
20

Preprint. Under review.
whereC −i is the full opposite-side candidate set used only for ex post evaluation. If¯r M (µ)and
¯rW (µ)are the average realized partner ranks of matched men and women, then
RankGap(µ) =|¯rM (µ)−¯rW (µ)|.(16)
Blocking pairs.Letu i(j) =s i(j)/100and define the final benchmark
Bi(µ) =
(
max{ri, ui(µ(i))}, µ(i)̸=∅,
ri, µ(i) =∅. (17)
An unmatched pair(m, w)/∈ P(µ)is blocking whenum(w)> Bm(µ)andu w(m)> Bw(µ). This
is an ex post stability diagnostic; agents do not observe the blocking-pair set during matching.
Proposal volume.We count all proposal attempts as a measure of search intensity. Because
Gale–Shapley proposals are centralized algorithmic operations whereas LLM-ABM and Axtell–
Kimbrough proposals arise from decentralized interaction, this quantity is slightly different for cen-
tralized and decentralized scenarios.
I COUNTERFACTUALWARM-STARTEXPERIMENT
The counterfactual experiments in Section 4.4 use the same50×50population and Bandit-UCB
configuration as the main matching experiment. Source runs use the same 50 seeds as the main
experiment, whereas counterfactual evaluation uses another 10 seeds. The source phase provides
learned proposer-side Logistic-UCB coefficients that are used only for initialization in the treatment
conditions.
Individual warm start.Each male agent is treated as the focal agent in turn. Only that agent
receives the corresponding source-phase initialization; all other agents remain cold-start learners.
For every held-out seed, the warm-start run is paired with a cold-start Bandit-UCB run using the
same seed, holding fixed the stochastic market realization associated with the evaluation seed.
Male-side warm start.We also initialize all male agents with the pooled male-proposer coeffi-
cients learned from the source runs, while female agents remain cold-start learners. This stronger
intervention tests whether information that can help an individual retains its value once it is shared
across an entire side of the market.
Warm-starting changes only the initial coefficient vectorθ. It does not alter LLM utilities, candidate
exposure, reservation utilities, proposal rules, receiver behavior, or the observed proposal history,
and subsequent feedback can revise or erase the initial belief.
Table 9: Distribution of individual warm-start effects across male focal agents.
Metric Improved Unchanged Worsened Avg. gain Avg. loss Mean effect
Own rank 11 26 13 0.95 0.46 -0.15
Own score 11 26 13 0.95 0.55 -0.22
Proposals 22 3 25 8.20 15.37 -5.00
Table 9 uses the focal agent as the unit of analysis. “Avg. gain” reports the average signed improve-
ment among agents with a positive effect, while “Avg. loss” reports the average absolute loss among
agents with a non-positive effect, with unchanged agents contributing zero. For rank and proposal
volume, signs are oriented so that positive values indicate improvement; for score, higher values
directly indicate improvement.
J SENSITIVITYANALYSIS OFEXPLORATION ANDCOMMITMENT
We further examine how the LLM-ABM market responds to two key behavioral parameters: the
exploration coefficientβin Bandit-UCB and the permanent lock probabilityρ. Theβsweep varies
21

Preprint. Under review.
0 0.05 0.1 0.2 0.3 0.5 0.75 1 1.25 1.5 2 3 5
β values
0.94
0.95
0.96Final matched ratio
β sweep (ρ = 0.05)
Main setting
ρ sweep (β = 1)
0 0.05 0.1 0.2 0.3 0.5 0.75 1 1.25 1.5 2 3 5
β values
20
40
60Blocking number
β sweep (ρ = 0.05)
Main setting
ρ sweep (β = 1)
0 0.05 0.1 0.2 0.3 0.5 0.75 1 1.25 1.5 2 3 5
β values
5k
10k
15kProposal number
β sweep (ρ = 0.05)
Main setting
ρ sweep (β = 1)
0.01 0.015 0.02 0.03 0.04 0.05 0.075 0.1 0.125 0.15 0.2 0.3
ρ values
0.01 0.015 0.02 0.03 0.04 0.05 0.075 0.1 0.125 0.15 0.2 0.3
ρ values
0.01 0.015 0.02 0.03 0.04 0.05 0.075 0.1 0.125 0.15 0.2 0.3
ρ values
Figure 6: Sensitivity of market-level outcomes to exploration strengthβand lock probabilityρ. The
blue curve variesβwithρ= 0.05fixed, while the orange curve variesρwithβ= 1fixed. Shaded
regions indicate 95% confidence intervals across 50 seeds; stars mark the main experimental setting.
the strength of uncertainty-driven exploration while holdingρ= 0.05fixed, whereas theρsweep
varies the rate at which temporary matches become permanent while holdingβ= 1fixed. All
experiments use the same50×50market and 50 random seeds. For low-ρsettings, we use a smaller
per-activation proposal budget (L) to keep within-round search bounded.
Figure 6 shows that the final matched ratio remains relatively stable across both parameter sweeps
and stays close to the main setting for most values ofβandρ. This indicates that the market reaches
a high level of aggregate matching under a broad range of exploration and commitment intensities,
although some variation in the share of unmatched agents remains.
The blocking-pair results are more sensitive to the commitment parameter. Varyingβchanges the
number of blocking pairs only moderately, suggesting that the main stability pattern is not driven by
a narrow choice of exploration strength. In contrast,ρhas a more pronounced effect. Very low com-
22

Preprint. Under review.
mitment probabilities prolong the search process and leave more relationships unresolved, whereas
very high commitment probabilities cause agents to exit the market earlier and can lock in less stable
matches. The main setting,ρ= 0.05, lies in a relatively low-blocking region of the sensitivity curve
and provides a reasonable balance between continued search and timely commitment.
Proposal volume reveals a complementary search-intensity trade-off. Largerβgenerally increases
the number of proposals because stronger exploration encourages agents to consider more uncertain
candidates. Increasingρ, by contrast, sharply reduces proposal volume because agents become
permanently matched and leave the active market more quickly. This reduction in search intensity,
however, is accompanied by a higher blocking count at largeρ. Overall, the main configuration is
not selected to optimize any single metric in isolation; rather, it provides a balanced operating point
with a high final matched ratio, relatively few blocking pairs, and moderate proposal volume.
K DERIVATION OF THELOCALLOGISTIC-UCB DECISIONRULE
This appendix derives the practical Fisher-information-based proposal rule used in Section 3.3. Ap-
pendix L analyzes a calibrated variant and specifies its assumptions and scope.
K.1 LOCALLOGISTICACCEPTANCEMODEL
For proposeri, suppose reciprocal acceptance is represented by a logistic working model
Pr

Yi→j,t = 1|x (i) j,t

=σ

x(i) j,t ⊤ θi

,(18)
where
σ(z) = 1 1 + exp(−z).(19)
Given local proposal historyH i,t, the regularized negative log-likelihood is
Li,t(θ) =
Ni,tX
n=1
h
log

1 + exp

x(i) n ⊤ θ  −y (i) n x(i) n ⊤ θ i + λi 2 ∥θ∥2 2.(20)
Its gradient is
∇Li,t(θ) =
Ni,tX
n=1
h
σ

x(i) n ⊤ θ  −y (i) n i x(i) n +λ iθ.(21)
The Hessian is
∇2Li,t(θ) =λ iI+
Ni,tX
n=1
σ

x(i) n ⊤ θ  h 1−σ  x(i) n ⊤ θ i x(i) n x(i) n ⊤ .(22)
Evaluating Equation 22 at the fitted parameter bθi,t yields
Vi,t =λ iI+
Ni,tX
n=1
bp(i) n,t

1−bp(i) n,t

x(i) n x(i) n ⊤ ,(23)
which is the local curvature matrix used in the main text.
K.2 UNCERTAINTY IN THELOGITPREDICTOR
Suppose, for interpretation, that a local confidence region around the fitted parameter can be approx-
imated by
Ci,t =

θ:
θ− bθi,t  Vi,t ≤β i,t  ,(24)
23

Preprint. Under review.
where
∥z∥V =
√
z⊤V z.(25)
For a candidate contextx (i) j,t,
x(i) j,t ⊤  θ− bθi,t  =  V −1/2 i,t x(i) j,t ⊤  V 1/2 i,t  θ− bθi,t  (26)
≤
V −1/2 i,t x(i) j,t  2 V 1/2 i,t  θ− bθi,t  2 (27)
≤β i,t
r
x(i) j,t ⊤ V −1 i,t x(i) j,t.(28)
This motivates the uncertainty measure
s(i) j,t =
r
x(i) j,t ⊤ V −1 i,t x(i) j,t.(29)
The corresponding optimistic linear predictor is
zUCB,i ij,t = bθ⊤ i,tx(i) j,t +β i,ts(i) j,t.(30)
Since the sigmoid link is strictly increasing,
z1 ≤z 2 =⇒σ(z 1)≤σ(z 2),(31)
we obtain the optimistic acceptance prediction
pUCB,i ij,t =σ  bθ⊤ i,tx(i) j,t +β i,ts(i) j,t  .(32)
This construction follows the general optimistic principle used in generalized-linear contextual ban-
dits (Filippi et al., 2010; Li et al., 2017). Our particular use of the fitted logistic Hessian in Equa-
tion 23 should be understood as a local Fisher-information or Wald/Laplace-style approximation.
Because the Hessian of a logistic model depends on the unknown parameter itself, more refined
Logistic-UCB analyses can require nonlinear confidence sets and stronger regularity conditions.
Accordingly, in the main experiments,β i,t is treated as an exploration coefficient rather than as an
exact finite-sample confidence radius, and bθi,t is obtained from the unconstrained regularized prob-
lem. The analyzable variant in Appendix L instead restricts the estimator to a norm ball, which is
what makes its curvature constant follow from primitive bounds.
K.3 PROPOSALINDEX ASOPTIMISTICEXPECTEDUTILITYIMPROVEMENT
The bandit observes the binary response
Yi→j,t ∈ {0,1},(33)
but the economic objective of the proposer is not simply to maximize acceptance probability.
For an eligible candidatej∈ Et(i), define the realized utility improvement from a proposal as
Ri→j,t =Y i→j,t∆Uij,t.(34)
Conditional on the information available to proposeri,
E
h
Ri→j,t |x (i) j,t
i
= ∆Uij,t Pr

Yi→j,t = 1|x (i) j,t

.(35)
The eligible-set restriction implies
∆Uij,t >0.(36)
Therefore, replacing the unknown reciprocal-acceptance probability with an optimistic estimate pre-
serves the direction of the upper bound and leads to
Iij,t = ∆Uij,tpUCB,i ij,t .(37)
This derivation clarifies why the positivity restriction in Equation 3 is important. If∆U ij,t <0,
multiplication by a probability upper bound would reverse the relevant inequality, and Equation 37
would no longer admit the same optimistic expected-improvement interpretation.
24

Preprint. Under review.
L THEORETICALANALYSIS OFLOCALLEARNING ANDBILATERAL
REMATCHING
L.1 OVERVIEW OFTHEORETICALRESULTS
The theoretical analysis fixes one proposer and studies its own sequence of realized proposal at-
tempts. It is intentionally local: the benchmark is a myopic oracle facing the same currently eligible
candidates, rather than a market-wide matching trajectory. Under this scope, the appendix estab-
lishes five results.
R1. Oracle one-step optimality.If current reciprocal-acceptance probabilities were known,
maximizing∆U×pmaximizes the proposer’s conditional expected one-step utility im-
provement.
R2. Local pseudo-regret under a correctly specified working model.Under predictable
bounded contexts, bounded positive utility improvements, and a proposer-specificrealiz-
ablelogistic acceptance model, a theoretically calibrated Logistic-UCB rule with a norm-
constrained local estimator has sublinear local pseudo-regret with high probability. Exact
realizability need not hold in the mechanism of Section 3.3; R2 is stated as a benchmark
that isolates the statistical cost of learning reciprocation and supplies the reference rate for
R3.
R3. Dynamic misspecification.The decentralized design of Section 3.3 induces a non-
stationary acceptance law, so the logistic model is a working approximation rather than
a data-generating process. If it matches the true, time-varying acceptance probability up
to a bounded envelopeη n, the regret bound separates statistical learning error from an ex-
plicit cumulative misspecification term. Observable dynamic context can shrink this term
but cannot generally eliminate receiver-private state information by construction.
R4. Strict bilateral improvement.Every accepted rematching strictly improves the partner
utility of both consenting agents relative to their pre-proposal benchmarks.
R5. Matched-pair welfare non-monotonicity.Strict bilateral improvement does not imply
monotone matched-pair welfare because an accepted rematching can displace previous
partners. Consequently, local no-regret learning alone does not imply terminal optimal-
ity of the matched-pair welfare metric or stability.
The analysis uses a norm-constrained estimator and calibrated confidence radii, whereas the experi-
ments use an unconstrained estimator with fixed exploration. Remark L.1 explains the relationship
between the acceptance model and the simulated mechanism.
L.2 FORMALRESULTS
Proposal-time notation and learner filtration.Fix proposeriand index its own realized pro-
posal attempts byn= 1,2, . . ., distinct from the global market-period index. LetF n−1 be the
information available to the proposer immediately before attemptn. It contains the proposer’s past
proposal contexts and outcomes, the currently exposed and eligible candidate set, all public infor-
mation available for current candidates, the current fitted local model, and algorithmic randomness
revealed before the current proposal. It excludes receiver-private quantities that the mechanism does
not reveal, including the receiver’s private valuation of the proposer and the value of the receiver’s
incumbent relationship.
At attemptn, letR n be the current eligible candidate set. For eachj∈ R n, the proposer observes
xj,n ∈R d and a positive utility improvement∆U n(j)>0. LetY n(j)∈ {0,1}denote the potential
reciprocal-acceptance response that would be observed if candidatejwere selected at attemptn. If
candidatejis selected, write
Jn =j, X n :=x Jn,n, Y n :=Y n(Jn).
For each current candidate define
pn(j) :=P(Y n(j) = 1| Fn−1),
25

Preprint. Under review.
and the potential one-step proposal reward
Rn(j) :=Y n(j)∆Un(j), g n(j) :=E[R n(j)| Fn−1] = ∆Un(j)pn(j).
The selected contextX n is required to beFn−1-measurable. Thus the policy may adapt arbitrarily to
past outcomes and to the current candidate set, but must select the current context before observing
Yn.
Proposition L.1(R1: Oracle one-step proposal optimality).Condition onF n−1 and suppose the
proposer makes one current proposal fromR n. If the true conditional acceptance probabilities
{pn(j) :j∈ Rn}were known, then every
J ⋆ n ∈arg max j∈Rn ∆Un(j)pn(j)
maximizes the proposer’s conditional expected one-step utility improvement.
This is a myopic statement. If a rejection leaves a continuation opportunity within the same ac-
tivation, optimizing an entire sequence of proposals is a dynamic decision problem and need not
coincide with ranking candidates solely by one-step expected improvement.
Assumptions for local learning.
Assumption L.1(Predictable bounded contexts).For everyn,X n isF n−1-measurable and
∥Xn∥2 ≤L.
Assumption L.2(Realizable reciprocal acceptance).There exists a fixed proposer-specific param-
eterθ ⋆ ∈R d with∥θ ⋆∥2 ≤Ssuch that, for everynandeverycurrently eligible candidatej∈ R n,
pn(j) =P(Y n(j) = 1| Fn−1) =σ(x ⊤ j,nθ⋆), σ(z) = 1 1 +e −z .
In particular, becauseJ n isF n−1-measurable,E[Y n | Fn−1] =σ(X ⊤ n θ⋆).
The statement is made over the potential outcomes{Y n(j)}j∈Rn rather than only over the selected
action, because the regret analysis compares the chosen candidate with an unselected oracle candi-
date and therefore requires the model to describe counterfactual arms as well.
Remark L.1(Assumption L.2 need not hold exactly in our mechanism).Assumption L.2 need not
be satisfied by the matching system of Section 3.3. Acceptance there is generated by the threshold
ruleY i→j,t =1{U j(i)> b R j,t}, whereas the local contextx (i) j,t =ϕ(z i, zj)of Appendix G is built
from static public persona attributes and is therefore constant across attempts for a fixed ordered pair
(i, j). Because the receiver’s benchmarkbR j,t moves with its incumbent relationship and is excluded
from the proposer’s information set, two histories can share the same proposer-observable dyadic
context while inducing different conditional acceptance probabilities. Hence a single fixedθ ⋆ need
not representp n(j)across market states. This is a consequence of the information design rather than
a modeling oversight: receiver-private and time-varying thresholds are deliberately withheld from
proposers.
We nonetheless state Theorem L.1 under Assumption L.2 as a correctly specified benchmark. It iso-
lates the purely statistical difficulty of learning reciprocation when the working model is correct, and
it supplies the reference rate against which the misspecification penalty is measured. Theorem L.2,
which replaces realizability by the bounded-envelope Assumption L.4, is formulated for the form
of dynamic misspecification induced by the simulated mechanism; its sufficient conditions are not
claimed to be verified by the simulator.
Assumption L.3(Bounded positive utility improvement).For every current candidate,0<
∆Un(j)≤Dfor a finite constantD. Under utilities normalized to[0,1], one may takeD≤1.
Norm-constrained local estimator.Let
Θ :=

θ∈R d :∥θ∥ 2 ≤S
be the parameter set implied by the norm bound onθ ⋆, and define the regularized logistic objective
together with its constrained minimizer
Ln(θ) =
n−1X
m=1
h
log(1 +e X ⊤ mθ)−Y mX ⊤ mθ i + λ 2 ∥θ∥2 2, bθn := arg min θ∈Θ Ln(θ).
26

Preprint. Under review.
BecauseL n is strictly convex forλ >0andΘis convex and compact, bθn exists and is unique.
Restricting the estimator toΘis what turns the logistic curvature below into a derived quantity
determined by the primitive constantsLandS, rather than a condition imposed on the realized
estimator sequence. Define the matrices
Gn :=λI+
n−1X
m=1
XmX ⊤ m, V n :=λI+
n−1X
m=1
σ′(X ⊤ m bθn)XmX ⊤ m,
and the practical Fisher width
sn(x) :=
p
x⊤V −1n x.
Lemma L.1(Uniform local logistic curvature).Suppose Assumption L.1 holds andθ ⋆ ∈Θ, and set
κ :=σ ′(LS) = e−LS
(1 +e −LS)2 ∈(0, 1 4 ].
Then for everyn, everym < n, and everyu∈[0,1],
σ′

X ⊤ m[θ⋆ +u( bθn −θ ⋆)]  ≥κ .
Lemma L.1 supplies the curvature needed to convert score concentration into parameter concentra-
tion. The mechanism is thatθ ⋆ and bθn both lie in the convex setΘ, so the entire segment joining
them lies inΘand the logistic predictions entering the mean-value expansion cannot be arbitrarily
saturated. Under an unconstrained estimator the analogous statement would have to be assumed
directly on the fitted path, because∥ bθn∥2 is then only controlled by a bound that grows with the
sample size. Forδ∈(0,1), define
βn(δ) := 1 κ
"
√
λS+ 1 2
r
log detG n
λd + 2 log 1 δ
#
,(38)
and the deterministic upper bound
¯βn(δ) := 1 κ
"
√
λS+ 1 2
s
dlog

1 + (n−1)L 2
λd

+ 2 log 1 δ
#
.(39)
The theoretically calibrated optimistic probability is
pUCB n (j) :=σ  x⊤ j,n bθn +β n(δ)sn(xj,n)  .
Definition L.1(Local proposal pseudo-regret).Let
J ⋆ n ∈arg max j∈Rn ∆Un(j)pn(j), J n ∈arg max j∈Rn ∆Un(j)pUCB n (j).
The instantaneous local pseudo-regret and cumulative pseudo-regret are
rn := ∆Un(J ⋆ n)pn(J ⋆ n)−∆U n(Jn)pn(Jn),R N :=
NX
n=1
rn.
Theorem L.1(R2: Local regret under realizable reciprocal acceptance).Suppose Assumptions L.1–
L.3 hold,λ >0, andκ =σ ′(LS)is the curvature constant of Lemma L.1. Then, with probability at
least1−δ, simultaneously for all proposal attemptsn,
∥bθn −θ ⋆∥Gn ≤β n(δ)≤ ¯βn(δ),(40)
and, for every current candidate contextx,
σ(x⊤θ⋆)≤σ  x⊤ bθn +β n(δ) p x⊤V −1n x  .(41)
Consequently,
RN ≤ D ¯βN (δ) 2
s
N d
κ

1 + L2
λ

log

1 + N L2
λd

.(42)
For fixedL, S, λ, D,andκ,
RN = eO

d
√
N
κ3/2
!
, RN
N →0.
27

Preprint. Under review.
The benchmark in Theorem L.1 is a myopic oracle that faces the same current candidate set and
knows the true current reciprocal-acceptance probabilities. The result isolates the local learning loss
caused by uncertainty about reciprocation; it does not compare full-market trajectories generated
by different policies. As stated in Remark L.1, its realizability hypothesis need not be met by
our mechanism, so Theorem L.1 should be read as the correctly specified reference point for the
misspecified analysis that follows.
Dynamic misspecification and observable context.The matching system need not obey a sta-
tionary logistic law because a receiver’s acceptance threshold changes when its current relationship
changes, while the proposer is deliberately denied receiver-private information. We therefore also
analyze the logistic model as a working approximation based only on proposer-observable informa-
tion.
Assumption L.4(Bounded dynamic logistic misspecification).There exists a fixed reference pa-
rameterθ ⋆ with∥θ ⋆∥2 ≤S, i.e.θ ⋆ ∈Θ, and a predictable nonnegative sequence{η n}such that,
for everyj∈ Rn,
pn(j) =σ(x ⊤ j,nθ⋆) +b n(j),|b n(j)| ≤ηn,
withp n(j)∈[0,1].
One may augment the public dyadic context with dynamic variables known before the current pro-
posal, such as market stage, the proposer’s accumulated proposal count, or the proposer’s own re-
cent acceptance statistics. Such features remain predictable and can reduce misspecification. They
cannot, however, generally guarantee exact realizability under the present information design: two
market states may induce the same proposer-observable context but different receiver-private incum-
bent values and therefore different acceptance thresholds. Hence richer observable context should
be interpreted as potentially shrinking the envelopeη n, rather than automatically eliminating it;
increasing context dimension also enters the statistical bound throughd.
For selected historical actions writeb m :=b m(Jm). Define
βmis n (δ) := 1 κ

√ λS+ 1 2 r log detG n λd + 2 log 1 δ + vuut n−1X m=1 η2m   ,(43)
and
¯βmis n (δ) := 1 κ

√ λS+ 1 2
s
dlog

1 + (n−1)L 2
λd

+ 2 log 1 δ +
vuut n−1X
m=1
η2m

 .(44)
Let
¯pUCB n (j) :=σ  x⊤ j,n bθn +β mis n (δ)sn(xj,n)  ,
and suppose the policy selects
Jn ∈arg max j∈Rn ∆Un(j)¯pUCB n (j).
Theorem L.2(R3: Local regret under bounded dynamic misspecification).Suppose Assump-
tions L.1, L.3, and L.4 hold, withκ =σ ′(LS)as in Lemma L.1. Assumption L.2 isnotrequired.
Then, with probability at least1−δ, simultaneously for alln,
∥bθn −θ ⋆∥Gn ≤β mis n (δ).
Moreover, local pseudo-regret relative to the oracle that knows the true current probabilitiesp n(j)
satisfies
RN ≤ D ¯βmis N (δ) 2 s N d κ  1 + L2 λ  log  1 + N L2 λd  + 2D NX n=1 ηn.(45)
A simple sufficient condition for vanishing average local pseudo-regret is
NX
n=1
ηn =o
 N
logN

,
assuming0≤η n ≤1and the remaining problem constants are fixed.
28

Preprint. Under review.
The misspecification term in Theorem L.2 is not only a feature-engineering residual: under the de-
centralized information restriction it can also represent state variables intentionally hidden from the
proposer. Theorem L.2 is therefore formulated to accommodate the form of dynamic misspecifi-
cation induced by the mechanism of Section 3.3, and it reduces to Theorem L.1 whenη n ≡0.
Verifying the sufficient condition P n ηn =o(N/logN)requires knowledge of the receiver-side state that the design withholds from proposers; characterizingη n endogenously is left to future
work.
Bilateral rematching.For any agentk, define its pre-rematching individual benchmark utility
vk(µt) :=
rk, µ t(k) =∅,
Uk(µt(k)), µ t(k)̸=∅.
Proposition L.2(R4: Strict bilateral improvement of every accepted rematching).Suppose pro-
poseriselects an eligible candidatejat timetand the proposal is accepted. Then the newly formed
pair(i, j)strictly improves the individual partner utility of both consenting agents relative to their
pre-proposal benchmarks:
Ui(j)> vi(µt), U j(i)> vj(µt).
More precisely,
Ui(j)−b i,t > ϵU ≥0, U j(i)−b R j,t >0.
LetP(µ)denote the set of realized cross-side pairs in matchingµ. For consistency with the empirical
mutual-welfare metric, define total matched-pair welfare
Wtot(µ) :=
X
(a,b)∈P(µ)
Ua(b) +U b(a)
2 ,
and, whenP(µ)̸=∅, average mutual welfare
Wavg(µ) := Wtot(µ) |P(µ)| .
Proposition L.3(R5: Matched-pair welfare need not be monotone).There exists a finite two-sided
market and a temporary matchingµt such that an accepted proposal is a strict bilateral improvement
for the proposer and receiver as in Proposition L.2, yet the immediate rematching strictly decreases
both total matched-pair welfare and average mutual welfare:
Wtot(µt+1)< Wtot(µt), W avg(µt+1)< Wavg(µt).
The reason is a matching externality: the bilateral acceptance test internalizes the preferences of the
two consenting agents, but not the losses of partners displaced by the rematching.
Corollary L.1(Local learning guarantees do not imply global matching optimality).Even if
proposer-side local pseudo-regret in Theorem L.1 or Theorem L.2 is sublinear, this alone does not
imply monotone matched-pair welfare, terminal optimality of that welfare metric, or convergence to
a stable matching.
L.3 PROOFS
Proof of Proposition L.1.
Proof.Condition onF n−1. Since∆U n(j)is known before the current response, for every current
candidatej,
E[Rn(j)| Fn−1] =E[Y n(j)∆Un(j)| Fn−1]
= ∆Un(j)E[Yn(j)| Fn−1]
= ∆Un(j)pn(j).
Therefore any maximizer of∆U n(j)pn(j)maximizes conditional expected one-step utility im-
provement.
29

Preprint. Under review.
Specialization of Abbasi-Yadkori–P´al–Szepesv´ari.The only external concentration result used
in the learning proofs is the time-uniform self-normalized inequality of Abbasi-Yadkori et al. (2011),
Theorem 1. Their theorem applies to a predictable vector sequenceX m and a conditionally mean-
zero,R-sub-Gaussian scalar noise sequenceε m, with
St =
tX
m=1
εmXm, ¯Vt =V+
tX
m=1
XmX ⊤ m,
and yields, with probability at least1−δ, simultaneously for allt,
∥St∥2 ¯V −1 t ≤2R 2 log
 det( ¯Vt)1/2
det(V) 1/2δ

.
Under Assumption L.2, set
εm :=Y m −σ(X ⊤ mθ⋆), V=λI, t=n−1.
ThenE[ε m | Fm−1] = 0. Conditional onF m−1,Y m ∈ {0,1}, so Hoeffding’s lemma implies
that the centered Bernoulli noiseε m is conditionally1/2-sub-Gaussian. Moreover ¯Vn−1 =G n.
Therefore, with probability at least1−δ, simultaneously for everyn,
 n−1X m=1 εmXm  G−1 n ≤ 1 2 r log detG n λd + 2 log 1 δ .(46)
The adaptive proposal policy is compatible with this result because the theorem requires predictabil-
ity rather than i.i.d. contexts:X n may depend on the entire observed history and current candidate
set as long as it is chosen beforeY n is observed.
Proof of Lemma L.1.
Proof.Fixn,m < n, andu∈[0,1], and setθ u :=θ ⋆ +u( bθn −θ ⋆). Bothθ ⋆ and bθn belong toΘ,
which is convex, soθ u ∈Θand∥θ u∥2 ≤S. By Cauchy–Schwarz and Assumption L.1,

X ⊤ mθu

 ≤ ∥Xm∥2∥θu∥2 ≤LS.
The derivativeσ ′(z) =σ(z)(1−σ(z))is even and strictly decreasing in|z|, so|z| ≤LSimplies
σ′(z)≥σ ′(LS) =κ . Finallyκ ≤σ ′(0) = 1/4, andκ >0becauseLandSare finite.
Constrained logistic estimation error.BecauseL n is convex and differentiable andΘis convex,
the constrained minimizer satisfies the first-order variational inequality
D
∇Ln(bθn), θ− bθn
E
≥0for everyθ∈Θ.
Sinceθ ⋆ ∈Θ, choosingθ=θ ⋆ gives
D
∇Ln(bθn), en
E
≤0, e n := bθn −θ ⋆.(47)
When the norm constraint is inactive, Equation 47 holds with equality and reduces to the usual
unconstrained score equation, so the argument below covers both cases. Set
εm :=Y m −σ(X ⊤ mθ⋆), S n :=
n−1X
m=1
εmXm,
and substituteY m =σ(X ⊤ mθ⋆) +ε m into the gradient
∇Ln(bθn) =
n−1X
m=1
[σ(X ⊤ m bθn)−Y m]Xm +λ bθn
to obtain
∇Ln(bθn) =
n−1X
m=1
[σ(X ⊤ m bθn)−σ(X ⊤ mθ⋆)]Xm +λe n −(S n −λθ ⋆).(48)
30

Preprint. Under review.
For eachm < n, the scalar mean-value theorem gives a pointξm,n betweenX ⊤ mθ⋆ andX ⊤ m bθn such
that
σ(X ⊤ m bθn)−σ(X ⊤ mθ⋆) =σ ′(ξm,n)X ⊤ men.
Thus∇L n(bθn) =H nen −(S n −λθ ⋆), where
Hn :=λI+
n−1X
m=1
σ′(ξm,n)XmX ⊤ m,
and Equation 47 becomes
e⊤ n Hnen ≤e ⊤ n (Sn −λθ ⋆).
Eachξ m,n equalsX ⊤ mθu for someu∈[0,1], because the mapu7→X ⊤ m[θ⋆ +u( bθn −θ ⋆)]is affine
and traverses exactly the interval between the two endpoints. Lemma L.1 therefore implies
Hn ⪰λI+κ
n−1X
m=1
XmX ⊤ m ⪰κ Gn,
where the final inequality uses0< κ ≤1/4<1. Hence
κ∥en∥2 Gn ≤e ⊤ n Hnen
≤e ⊤ n (Sn −λθ ⋆)
≤ ∥en∥Gn

∥Sn∥G−1 n +λ∥θ ⋆∥G−1 n

.
SinceG n ⪰λI,
λ∥θ⋆∥G−1 n ≤ √ λ∥θ⋆∥2 ≤ √ λS.
Combining this with Equation 46 proves the first inequality in Equation 40. The determinant bound
log detG n
λd ≤dlog

1 + (n−1)L 2
λd

follows from the arithmetic–geometric mean inequality applied to the eigenvalues and yieldsβ n ≤ ¯βn.
At the fitted endpoint, Lemma L.1 applied withu= 1and the global boundσ ′(z)≤1/4≤1give
κGn ⪯V n ⪯G n.(49)
After inversion,
G−1 n ⪯V −1 n ⪯ 1 κ G−1 n .
For every candidate contextx,
|x⊤(bθn −θ ⋆)| ≤ ∥bθn −θ ⋆∥Gn ∥x∥G−1 n
≤β n(δ)∥x∥V −1 n .
Therefore
x⊤θ⋆ ≤x ⊤ bθn +β n(δ) p x⊤V −1n x,
and monotonicity of the sigmoid proves Equation 41.
Proof of Theorem L.1.On the confidence event, valid optimism and UCB maximization imply
∆Un(J ⋆ n)pn(J ⋆ n)≤∆U n(J ⋆ n)pUCB n (J ⋆ n)≤∆U n(Jn)pUCB n (Jn).
Hence
rn ≤∆U n(Jn)[pUCB n (Jn)−p n(Jn)].(50)
Lets n :=
q
X ⊤n V −1n Xn. The confidence event gives
|X ⊤ n (bθn −θ ⋆)| ≤βnsn.
31

Preprint. Under review.
Thus the optimistic logit exceeds the true logit by at most2β nsn. Sincesup z σ′(z) = 1/4, the
sigmoid is globally1/4-Lipschitz and
0≤p UCB n (Jn)−p n(Jn)≤ βn 2 sn.
Using∆U n(Jn)≤Din Equation 50,
rn ≤ Dβn 2 sn.(51)
From Equation 49,
s2 n ≤ 1 κ X ⊤ n G−1 n Xn.
Setq n :=X ⊤ n G−1 n Xn. SinceG n ⪰λI,0≤q n ≤L 2/λ. By the matrix determinant lemma,
log detG N+1
detG 1
=
NX
n=1
log(1 +q n).
For0≤q≤L 2/λ,
log(1 +q)≥ q 1 +q ≥ q 1 +L 2/λ .
Therefore
NX
n=1
s2 n ≤ d κ  1 + L2 λ  log  1 + N L2 λd  .
Cauchy–Schwarz yields
NX
n=1
sn ≤
s
N d
κ

1 + L2
λ

log

1 + N L2
λd

.(52)
Summing Equation 51, using monotonicity of ¯βn, and applying Equation 52 proves Equation 42.
Proof of Theorem L.2.Under Assumption L.4, for each selected historical action define
pm :=E[Y m | Fm−1], ξ m :=Y m −p m.
ThenE[ξ m | Fm−1] = 0, andξ m is conditionally1/2-sub-Gaussian. Also
Ym =σ(X ⊤ mθ⋆) +b m +ξ m.
Assumption L.4 givesθ ⋆ ∈Θ, so the variational inequality of Equation 47 applies verbatim. Re-
peating the mean-value expansion withY m decomposed as above gives
∇Ln(bθn) =H nen −
 n−1X
m=1
ξmXm +
n−1X
m=1
bmXm −λθ ⋆
!
,
and therefore
e⊤ n Hnen ≤e ⊤ n
 n−1X
m=1
ξmXm +
n−1X
m=1
bmXm −λθ ⋆
!
.
The martingale term obeys the same specialized self-normalized inequality above. For the bias term,
letXbe the matrix whosemth row isX ⊤ m and letb= (b 1, . . . , bn−1)⊤. Then
n−1X
m=1
bmXm =X ⊤b, G n =λI+X ⊤X.
The eigenvalues ofXG −1 n X⊤ ares 2 k/(λ+s 2 k)≤1, so
∥X⊤b∥2 G−1 n =b ⊤XG−1 n X⊤b
≤ ∥b∥2 2 ≤
n−1X
m=1
η2 m.
32

Preprint. Under review.
The same curvature argument based on Lemma L.1 therefore gives
∥bθn −θ ⋆∥Gn ≤β mis n (δ).
Now define the logistic reference¯pn(j) :=σ(x ⊤ j,nθ⋆)and its UCB
un(j) :=σ

x⊤ j,n bθn +β mis n sn(xj,n)  .
The confidence argument gives¯pn(j)≤u n(j), whereas misspecification givesp n(j)≤¯p n(j) +ηn.
For the true oracle actionJ ⋆ n,
∆Un(J ⋆ n)pn(J ⋆ n)≤∆U n(J ⋆ n)un(J ⋆ n) +Dη n
≤∆U n(Jn)un(Jn) +Dη n.
Subtracting the true expected gain of the selected action gives
rn ≤∆U n(Jn)[un(Jn)−p n(Jn)] +Dη n
≤∆U n(Jn)[un(Jn)−¯pn(Jn)] + 2Dηn.
The same1/4-Lipschitz argument yields
un(Jn)−¯pn(Jn)≤ βmis n 2 sn,
so
rn ≤ Dβ mis n 2 sn + 2Dηn.
Summing and applying Equation 52 proves Equation 45.
For the stated sufficient condition, if0≤η n ≤1and PN n=1 ηn =o(N/logN), then
NX
n=1
η2 n ≤
NX
n=1
ηn =o(N/logN).
Hence
qPN
n=1 η2n =o( p N/logN). Its contribution through ¯βmis N times the width sum iso(N);
the explicit P n ηn term is alsoo(N), while the ordinary statistical term is sublinear for fixed di- mension and constants. ThereforeR N /N→0.
Proof of Proposition L.2.
Proof.Becausejbelongs to the proposer’s eligible set,
∆Uij,t =U i(j)−b i,t > ϵU ≥0,
soU i(j)> bi,t. Ifiis single,b i,t =r i =v i(µt). Ifiis currently matched,
bi,t = max{ri, Ui(µt(i))} ≥Ui(µt(i)) =v i(µt).
ThusU i(j)> vi(µt). Acceptance byjmeansU j(i)> bR j,t. Ifjis single,b R j,t =r j =v j(µt); ifjis
matched,
bR j,t = max{rj, Uj(µt(j))} ≥Uj(µt(j)) =v j(µt).
HenceU j(i)> vj(µt)as well.
Proof of Proposition L.3.
Proof.ConsiderM={m 1, m2}andW={w 1, w2}, with reservation utilities below0.60and all
current relationships temporary. Let
µt ={(m 1, w1),(m 2, w2)},
and choose directional utilities
Um1 (w1) = 0.60, U w1 (m1) = 0.99, U m2 (w2) = 0.99, U w2 (m2) = 0.60,
33

Preprint. Under review.
with cross-pair values
Um1 (w2) = 0.65, U w2 (m1) = 0.65.
Takeϵ U <0.05. Thenm 1 strictly prefersw 2 to its current benchmark andw 2 acceptsm 1, so the
proposal is a strict bilateral improvement for the consenting agents. Before the proposal,
Wtot(µt) = 0.60 + 0.99 2 + 0.99 + 0.60 2 = 1.59, W avg(µt) = 0.795.
After acceptance, the two old temporary relationships are dissolved,w 1 andm 2 are displaced, and
immediately after rematching
µt+1 ={(m 1, w2)}.
Hence
Wtot(µt+1) =W avg(µt+1) = 0.65 + 0.65 2 = 0.65.
Both total matched-pair welfare and average mutual welfare therefore decrease. The decline is
caused by the losses of the displaced partners, which are not part of the bilateral acceptance test.
Proof of Corollary L.1.
Proof.The local regret theorems control only the loss in one-step expected proposer improvement
relative to a myopic acceptance-probability oracle. Proposition L.3 constructs a feasible accepted
rematching in which both consenting agents improve while matched-pair welfare decreases. There-
fore local decision quality, even if asymptotically no-regret, does not by itself imply monotonicity
or terminal optimality of the matched-pair welfare metric. Stability is likewise not implied because
the local regret benchmark contains no stability constraint.
M FULLDECENTRALIZEDMATCHINGPROCEDURE
Algorithm 1 expands the period-level procedure summarized in Section 3.4. It makes explicit the
order of local exposure, valuation, proposal, feedback, model updating, relationship revision, and
stochastic commitment.
The procedure preserves three distinct forms of locality. Candidate discovery is local through
Ct(i); LLM valuation is triggered only when a candidate becomes locally relevant; and reciprocal-
acceptance learning is agent-specific because only proposals made byienterH i,t. No global ac-
ceptance model, shared interaction history, or market-wide preference matrix is available to the
proposed agents.
N LIMITATIONS ANDFUTUREDIRECTIONS
N.1 LIMITATIONS
The empirical grounding of this study is intentionally specific to the Chinese marriage-market set-
ting represented by the 2015 population sample and the choice experiment of Zhou et al. (2023).
Accordingly, the validation establishes alignment with this empirical reference rather than univer-
sal behavioral validity across cultures, cohorts, or institutional settings. Extending the framework
to other populations would require corresponding domain-specific demographic construction and
behavioral validation.
The simulated market also remains deliberately stylized. The main experiments use a50×50pop-
ulation with random local exposure, a common reservation-utility specification, and probabilistic
commitment. Richer interaction structures—including social networks, endogenous meeting pro-
cesses, heterogeneous or adaptive reservation values, noisy or private attributes, and evolving out-
side options—may alter the resulting matching dynamics. These components can be incorporated
within the same decentralized framework, but are outside the scope of the present experiments.
The theoretical results in Appendix L characterize local proposal-level learning and bilateral re-
matching; they do not guarantee terminal welfare optimality or convergence to a stable matching.
34

Preprint. Under review.
Algorithm 1Decentralized LLM-Agent Matching with Local Logistic-UCB
Require:Agent setsM,W; horizonT; proposal budgetL; reservation utilities{r i}; regularization
{λi}; exploration coefficients{β i,t}; utility thresholdϵ U ; commitment probabilities{ρ t}.
1:Initialize all agents as single; set local histories empty and initialize local Logistic-UCB models.
2:fort= 1, . . . , Tdo
3:A act t ← {i∈ A:iis not permanently matched}
4:ifA act t =∅then
5:break
6:end if
7:fora= 1, . . . ,|A act t |do
8:Samplei∼Uniform(A act t )with replacement
9:Sample local exposure setC t(i)⊆ Pt(i)
10:ObtainU i(j)for allj∈ C t(i)and constructE t(i)using Equation 3
11:R t ← Et(i)
12:forq= 1, . . . , Ldo
13:ifR t =∅then
14:break
15:end if
16:For eachj∈ R t, constructx (i) j,t and computeI ij,t using Equations 7 and 8
17:j ∗ ←arg max j∈Rt Iij,t
18:ObtainU j∗ (i)and computey ∗ ←Y i→j∗,t using Equation 5
19:H i,t ← Hi,t ∪ {(x(i) j∗,t, y∗)}
20:Refit bθi,t by Equation 20 and updateV i,t by Equation 23
21:ify ∗ = 1then
22:Dissolve temporary matches involvingiorj ∗ and return displaced partners to
active search
23:Form(i, j ∗)as a new temporary pair
24:break
25:else
26:R t ← Rt \ {j∗}
27:end if
28:end for
29:end for
30:LetT t denote temporary pairs after all activations
31:for all(i, j)∈ T t in parallel do
32:SampleZ ij,t ∼Bernoulli(ρ t)
33:ifZ ij,t = 1then
34:Mark(i, j)as permanent
35:end if
36:end for
37:end for
38:returnfinal matchingµ
35

Preprint. Under review.
Establishing endogenous bounds on dynamic misspecification and conditions linking local learn-
ing to market-level outcomes remains an open direction. Moreover, learned acceptance coefficients
represent predictive associations rather than structural or causal preferences, because proposal ob-
servations are endogenously selected by the matching policy.
Finally, LLM-based behavioral modeling remains sensitive to persona construction, prompt design,
model choice, and demographic representation (Anthis et al., 2025; Zhou et al., 2026; Ludwig et al.,
2024). Our cross-backbone and empirical-reference validation reduces dependence on any single
model realization, but does not eliminate these broader sources of behavioral-model uncertainty.
N.2 FUTUREDIRECTIONS
The framework naturally extends to other decentralized economic settings in which agents evalu-
ate counterparties while learning whether interaction will be reciprocated, including labor-market
search, hiring, team formation, housing, platform matching, and repeated buyer–seller or lender–
borrower interactions. The same separation between domain-grounded behavioral valuation and
local reciprocal learning can be retained while replacing personas, actions, institutions, and valida-
tion targets with domain-specific counterparts.
A second direction is to enrich the interaction structure through social networks, geography, rec-
ommender systems, endogenous communication, longer memories, adaptive reservation values, or
information sharing. On the learning side, nonstationary bandits, hierarchical priors, and theoretical
conditions connecting local learning to welfare or stability are natural extensions. Beyond eco-
nomics, the architecture can support persistent multi-agent societies in games, where NPCs form
and revise friendships, rivalries, coalitions, or trading relationships through local interaction rather
than a globally scripted social graph.
36
