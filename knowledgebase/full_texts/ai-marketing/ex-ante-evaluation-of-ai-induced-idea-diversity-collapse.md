---
title: Ex Ante Evaluation of AI-Induced Idea Diversity Collapse
url: https://arxiv.org/abs/2605.06540
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Nafis Saami Azad
- Raiyan Abdul Baten
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.06540
pages: 29
chars: 81851
fetched_at: '2026-11-08T13:10:04+00:00'
kb_version: 1
---

# Ex Ante Evaluation of AI-Induced Idea Diversity Collapse

Ex AnteEvaluation of AI-Induced Idea Diversity
Collapse
Nafis Saami Azad
Bellini College of Artificial Intelligence, Cybersecurity, and Computing
University of South Florida
Tampa, FL–33620, USA
nafisazad@usf.edu
Raiyan Abdul Baten
Bellini College of Artificial Intelligence, Cybersecurity, and Computing
University of South Florida
Tampa, FL–33620, USA
rbaten@usf.edu
Abstract
Creative AI systems are typically evaluated at the level of individual utility, yet
creative outputs are consumed in populations: an idea loses value when many others
produce similar ones. This creates an evaluation blind spot, as AI can improve
individual outputs while increasing population-level crowding. We introduce a
human-relative framework for benchmarking AI-induced human diversity collapse
without requiring human–AI interaction data, providing anex anteprotocol to
estimate crowding risk from model-only generations and matched unaided human
baselines. By modeling ideas as congestible resources, we show that source-level
crowding is identifiable from within-distribution comparisons, yielding an excess-
crowding coefficient ∆ and a human-relative diversity ratio ρ. We show that ρ≥1
is the no-excess-crowding parity condition and connect∆ to an adoption game with
exposure-dependent redundancy costs. Across short stories, marketing slogans,
and alternative-uses tasks, three frontier LLMs fall below parity across crowding
kernels. Estimates stabilize with feasible model-only sample sizes. Importantly,
generation-protocol variants show that crowding can be reduced through targeted
design, making diversity collapse an actionable, development-time evaluation target
for population-aware creative AI.
1 Introduction
Generative AI systems are increasingly used to support human creativity, from writing and design
to scientific ideation. Their effectiveness is typically evaluated at the level ofindividualutility: a
model is deemed successful if it helps a person write better stories, generate more ideas, or produce
more compelling artifacts. However, in creative domains, outputs are evaluated and consumed in
populations, and the value of a creative product depends not only on its intrinsic quality, but also on
its uniqueness relative to other products in the population [3, 1, 6]. When many users rely on the same
generative model for inspiration, their final outputs can become correlated, leading toAI-induced
human diversity collapse: a reduction in the collective diversity of human-generated ideas [18, 4, 29].
This creates an evaluation blind spot that individual-level approaches do not capture: a system can
improve each user’s expected output while making the population of human outputs more redundant.
Preprint.
arXiv:2605.06540v1  [cs.AI]  7 May 2026

Current empirical evidence on AI-induced diversity collapse relies onpost hoc evaluation: researchers
collect human–AI co-created outputs and measure idea diversity after the fact [18, 4, 29]. Such studies
are essential for documenting deployed effects, but this evaluation paradigm is poorly suited as a
development-time, population-aware benchmark. It requires expensive, time-intensive human-subject
experiments for each model, task, and interface condition; it does not provide a model-side quantity
that can be monitored, compared, or optimized before deployment; and it leaves users without a clear
way to reason about whether one model may help their final ideas stand out more than another.
To close this gap, we introduce a human-relative evaluation framework for benchmarking AI-induced
human diversity collapse without requiring human–AI interaction data. The framework formalizes
the population-level claim being evaluated, the proper counterfactual to contextualize it, and the
evidence needed to estimate it. It uses two observable ingredients: model-only generations from a
fixed model-condition and matched unaided human baselines from the same task condition.
Our approach is based on two key observations.First, ideas are not ordinary goods when they
function assources of inspiration. Inspiration sources behave like shared, congestible resources:
many individuals cannot draw from the same idea without diminishing its value, because repeated
use increases overlap in downstream idea-space [ 9, 10, 8, 27, 2]. This perspective gives rise to a
population game in which generative models act as shared source distributions that shape the human
outputs users ultimately produce.Second, crowding in idea-space must be contextualized to be
meaningful. Even without AI, independently generated human ideas exhibit a task-specific level of
overlap [1, 22, 6]. We therefore use human crowding as the baseline and measure the extent to which
model-only generations introduceexcess crowdingbeyond ordinary human convergence.
A central consequence is that population-level crowding effects can be estimated fromwithin-
distributioncomparisons at the source: human–human crowding estimates the baseline level of task-
specific convergence, while model-only crowding estimates the concentration induced by repeated
draws from the same model-condition. Their comparison yields an excess-crowding coefficient
that links source-level crowding to the population-level adoption game, while the human-relative
ratio defines a parity condition: a model-condition introduces no excess crowding exactly when its
outputs are no more crowded than the matched human baseline. Since this coefficient drives the
population-level redundancy cost, it can be estimated before human–AI outputs are collected. This
enablesex anteevaluation of AI-induced human diversity collapse: before running a new human–AI
study, developers can use model-only sampling to estimate a model-condition’s population-level
crowding risk. The resulting quantities also admit a decision-theoretic interpretation, characterizing
when AI adoption is individually rational as a function of expected crowding, value of distinctiveness,
and beliefs about others’ behavior.
We instantiate the framework on three creative task families—short stories, marketing slogans,
and alternative uses of common objects—and evaluate three frontier LLMs under matched task
instructions. Across the primary crowding kernel, all evaluated neutral model-conditions fall below
human-relative parity, indicating positive excess crowding relative to matched unaided human
baselines. We then stress-test the framework along three dimensions. First, rarefaction diagnostics
show that the estimated pairwise crowding coefficients stabilize with feasible model-only sample
sizes, supporting the practicality of development-time evaluation. Second, task-specific crowding
kernels show that the results are not artifacts of a single representation: story crowding persists under
plot-synopsis similarity, slogan crowding persists under lexical-template overlap, and alternative-uses
crowding persists under concept-bucket co-membership. Third, generation-protocol variants show
that crowding is not fixed by the base model alone: interventions such as temperature scaling and
persona-mixture prompting can move model-conditions toward human-relative parity. Together, these
results reframe diversity collapse from a post hoc diagnosis into an actionable evaluation target. For
AI developers, the framework provides a way to audit and reduce population-level crowding before
deployment; for users and downstream evaluators, it clarifies why the value of AI assistance depends
not only on private quality gains, but also on how many others draw from the same generative source.
2 Related Work
2.1 Post Hoc Evaluation of AI-Assisted Human Creativity
The most direct evidence for AI-induced human diversity collapse comes from studies of AI-assisted
creativity. In these experiments, participants generate stories, ideas, designs, or other artifacts with
2

or without AI assistance, and researchers evaluate the resulting human outputs. This paradigm has
shown that AI assistance can improve individual-level outcomes while narrowing the distribution of
outputs across users [4, 18]. Similar human–AI co-creation studies evaluate whether AI-generated
suggestions, feedback, or writing support change the novelty or usefulness of human creative
products [16, 29, 5, 47]. Methodologically, these studies use combinations of human ratings, expert
judgments, semantic similarity, clustering, lexical overlap, and idea-level diversity measures to
compare human-only and AI-assisted output distributions [4, 18, 16, 29]. This paradigm is essential
because it observes the realized human outputs in a particular task, model, interface, and interaction
protocol. Its limitation is that it is expensive, system-specific, and retrospective: each new model-
condition requires new human–AI interaction data before its population-level effect can be assessed.
The measurement tools used in these studies draw on a long tradition of human creativity assessment
in psychology. Human responses to common divergent-thinking tasks, such as the Alternative Uses
Task (AUT), are typically evaluated using three complementary approaches [12, 41, 19, 42].Idea-
intrinsicmeasures assess properties of a response or response set, such as semantic distance from
a prompt, within-person semantic diversity, or elaboration [ 23, 49, 41, 11, 45, 14].Social-rarity
measures score an idea by its infrequency in a reference population, often requiring rephrasings of the
same underlying concept to be grouped into shared buckets [1, 22, 40, 14, 7, 36, 17].Subjective-rating
approaches, including the Consensual Assessment Technique, ask human judges to rate novelty,
usefulness, or quality directly [9, 3]. Recent computational work has scaled these traditions using
embeddings, clustering, supervised scoring, and retrieval-assisted LLM bucketing [11, 37, 38, 6, 45,
13, 20, 48]. This literature provides mature ways to measure creative quality and population-relative
distinctiveness once outputs are observed; the open challenge is how to convert such measurements
into development-time benchmarks for AI systems before the corresponding human–AI outputs exist.
2.2 From Model-Output Diversity to Human-Relative Evaluation
A parallel literature evaluates the creative outputs of generative models themselves [44, 51]. Work on
story generation, divergent-thinking tasks, and model-based creative ideation commonly measures
model outputs using n-gram diversity, pairwise semantic distance, novelty, surprise, lexical or
syntactic complexity, association-based metrics, and human or LLM judgments [ 54, 26, 33, 31,
15, 34]. Recent benchmark and survey work emphasizes that LLM creativity evaluation remains
fragmented across tasks and metrics, with separate measures for quality, novelty, diversity, and
domain-specific creative behavior [39, 25, 32]. These evaluations often show that model outputs can
be fluent, coherent, and high quality while still converging on repeated themes, templates, or semantic
regions [52, 26, 25, 32, 54, 43]. Such convergence is expected from a generation perspective: LLMs
sample from prompt-conditioned distributions shaped by shared training data, post-training objectives,
decoding parameters, and prompting protocols [ 43, 24, 28, 35, 53]. When many generations are
elicited from similar prompts under similar settings, repeated tropes, phrasings, and high-probability
continuations are natural unless the generation process is explicitly diversified [30, 50]. However,
ordinary AI-output diversity metrics do not provide the human counterfactual needed to contextualize
AI-induced human diversity collapse. They can say whether model outputs are more or less diverse,
but not whether shared model use adds excess crowding beyond ordinary human convergence, or
whether that excess crowding implies an adoption-dependent, population-level redundancy cost. Our
framework addresses this gap directly.
3 A Human-Relative Theory of Idea-Space Crowding
3.1 Human-Relative Crowding
Consider a creative task condition k with output space Yk. Let Hk denote the distribution of unaided
human outputs over Yk. Likewise, let Am,k denote the distribution induced by model m under a fixed
generation protocol. We usemodel-only samplingto refer to repeated independent generations from
this same model-condition, without human interaction. Let Kk :Y k × Yk →[0,1] be a crowding
kernel, where larger values indicate that two outputs occupy a more similar region of idea-space. The
kernel is task-dependent: it may encode semantic similarity, shared plot structure, lexical-template
overlap, or co-membership in the same concept bucket, as appropriate. The formal theory requires
only that the same Kk be applied to both human and model-only data, be bounded in [0,1] , and be
interpretable as pairwise crowding.
3

We define unaided human crowding and model-only crowding for task conditionkas
κH k =E h,h′∼Hk [Kk(h, h′)], κ A m,k =E a,a′∼Am,k [Kk(a, a′)],(1)
where both expectations are over independent draws. The excess crowding coefficient is
∆m,k = max{0, κA m,k −κ H k }.(2)
This coefficient measures the excess concentration of the model-conditioned source distribution
relative to the unaided human counterfactual. We also define the human-relative diversity ratio
ρm,k =
1−κ A m,k
1−κ H k , κ H k <1.(3)
The ratio normalizes model-only diversity by the matched human baseline for the given task condition
k. This normalization is necessary because creative tasks differ in their baseline level of convergence:
humans also reuse tropes, affordances, and templates. A human-relative counterfactual therefore
prevents intrinsically constrained tasks from being mistaken for model-specific concentration.
Importantly, both quantities are identifiable from within-distribution samples: pairs of unaided
human outputs estimate κH k , and pairs of model-only generations estimate κA m,k. These matched
human-only and model-only samples are therefore sufficient to estimate excess crowding at the
source-distribution level, without observing realized human–AI interactions. The next subsection
shows how this source-level quantity enters a population adoption game.
Proposition 1(Human-relative parity is the no-externality condition).Ifκ H k <1, then
∆m,k = 0⇐ ⇒ρ m,k ≥1.(4)
This proposition makes ρ= 1 a benchmark threshold: it is exactly the point at which the model-
conditioned source distribution introduces no excess crowding beyond ordinary human convergence
under the same task constraints. Proofs of all propositions are provided in Appendix A.
3.2 Mean-field Approximation of a Congestion Game: From Crowding to Adoption
The coefficient ∆m,k is a pairwise property of a model-task distribution, representing the per-pair
excess-crowding hazard. Population cost depends on how many other creators draw from that same
distribution. Let X−i denote the number of other creators using model m in task condition k. Each
additional adopter creates another opportunity for the focal creator’s output to overlap with others.
Under an independent-exposure approximation, the probability of no excess redundancy encounter
is approximately exp{−X−i∆m,k}. The probability of at least one excess encounter is therefore
1−exp{−X −i∆m,k}. Multiplying by the value of distinctiveness in task k, γk ≥0 , we get the
redundancy cost
Cm,k(X−i) =γ k (1−exp{−X −i∆m,k}).(5)
The cost saturates because once an output is already non-distinct, additional overlaps add less marginal
damage. This is not the only possible choice for the redundancy cost function; we use the exponential
form as a monotone saturating exposure model that cleanly separates the pairwise excess crowding
∆m,k from population exposureX −i.
Let Ri,k be creator i’s expected payoff from unaided production, and letQi,m,k be creator i’s expected
payoff from using modelmbefore redundancy costs. The private AI advantage is
Bi,m,k =Q i,m,k −R i,k.(6)
A rational creator adopts AI when
Bi,m,k > Cm,k(X−i).(7)
The human-relative diversity ratio ρm,k affects this decision through the excess-crowding coefficient
∆m,k, which determines the redundancy cost. Combining Eqs. 2 and 3 gives
∆m,k = max{0,(1−ρ m,k)(1−κ H k )}.(8)
Thus, ρm,k ≥1 implies ∆m,k = 0, while lower values of ρm,k <1 imply larger excess crowding.
Therefore, lower human-relative diversity raises the redundancy cost Cm,k(X−i) and increases the
private benefitB i,m,k required for rational adoption.
4

Proposition 2(Critical benefit threshold).For exposure levelX −i, using modelmis rational iff
Bi,m,k > Bcrit m,k(X−i) =γ k (1−exp{−X −i∆m,k}).(9)
Forρ m,k <1, this threshold is decreasing inρ m,k and increasing inX −i,γ k, and∆ m,k.
The implication is intuitive: a below-parity model can still be rational to use when exposure is low,
distinctiveness is unimportant, or private benefit is large. But in a high-adoption creative market, low
ρimposes a larger distinctiveness discount.
3.3 Population Exposure
Now consider a population of N creators facing the same task condition k. For a focal creator
i, suppose each of the other N−1 creators independently adopts the same model-condition with
probability p. Then the number of other adopters is X−i ∼Binomial(N−1, p) . Taking the
expectation of Eq. 5 over this adoption process gives
E[Cm,k] =γ k
h
1−(1−p+pexp{−∆ m,k})N−1
i
.(10)
The derivation follows by taking the binomial expectation overX−i; see Appendix A. This expression
separates the empirically benchmarked model property, ∆m,k, from the population context, p and
N, and the task value of distinctiveness, γk. Thus, the same model can impose different expected
redundancy costs depending on adoption prevalence and market size.
The limiting case of mass adoption clarifies why the human-parity boundary matters.
Proposition 3(Mass-adoption limit).For the realized-exposure cost in Eq. 5,
lim
X−i→∞
Cm,k(X−i) =
0, ρ m,k ≥1,
γk, ρ m,k <1. (11)
If ρm,k ≥1 , shared model use adds no excess crowding cost at any exposure level. If ρm,k <1 ,
source-level excess crowding compounds with adoption, reaching the full distinctiveness penalty γk
in the mass-adoption limit. Thus, although ρ is estimated from matched human-only and model-only
data, it has a population-level interpretation: it determines whether shared model use creates an excess
crowding externality in human outputs, making human-relative parity a meaningful benchmark target.
4 Benchmark Design
The theory identifies ∆m,k as the pairwise excess-crowding coefficient that enters the adoption
game. Empirically, the benchmark estimates κH k , κA m,k, ∆m,k, and ρm,k from matched human and
model-generated samples. Rather than construct a general-purpose model leaderboard, we instantiate
atask-relativeevaluation procedure using a human baseline, a model-conditioned sample, and a
task-appropriate crowding kernel. Accordingly, we evaluate three task families that differ in output
structure, data source, and relevant notions of crowding: short stories, alternative uses of common
objects, and smartphone marketing slogans. These tasks serve three purposes: (i) to test whether
the benchmark recovers idea-space narrowing relative to humans, (ii) to assess whether pairwise
crowding coefficients are stable with feasible model-only sample sizes, and (iii) to examine whether
human-relative crowding is sensitive to the model-conditioned generation process, using temperature
and persona-mixture prompting as illustrative deployment variants.
Tasks and human baselines.For short, prompted creative writing, we sample three compact-
fiction prompts from the WritingPrompts corpus [21]: a short horror story, a 100-word parachute-
failure story, and a microfiction prompt contrasting a character’s life history with their final seconds.
These prompts provide 87 human-contributed stories, one per author. For the alternative uses task
(AUT) [23], we use the socialmuse dataset [10], with 109 human contributors generating 3,047
unaided ideas across five common objects while excluding each object’s primary use. For slogans, we
conducted an IRB-approved study with 95 human contributors who generated 659 creative marketing
slogans for a new smartphone, of which 650 are unique. Each story prompt, AUT object, or product
slogan context is treated as a task condition k; human-relative diversity is estimated within condition
before equal-weight aggregation. Dataset details and human instructions are provided in Appendix B.
5

(A) Story (B) AUT (C) Slogan
Human-relative diversity, ρ0.0
0.2
0.4
0.6
0.8
1.0
GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
Figure 1:Human-relative diversity under the primary semantic kernel.Points show task-family
estimates of bρfor each model; bars show 95% bootstrap intervals. The dashed line marks ρ= 1 , the
no-excess-crowding condition from Proposition 1. Full numeric estimates are reported in Appendix E.
Models and protocols.Model generations are collected from GPT-5.4, Claude Sonnet 4.5, and
Gemini 2.5 Flash under matched task instructions. The main benchmark uses neutral prompting
at temperature T= 1.0 with 50 model-only generations per task condition. Deployment variants
include temperature sweeps and a persona-mixture protocol crossing a 25 grid of Big Five binary
personality dimensions [46]. The persona mixture induces heterogeneous generation contexts while
holding the task fixed. Exact prompts and implementation details are provided in Appendix C.
Crowding kernels.Our primary kernel is semantic crowding. Let f(x) be a normalized sentence
embedding of outputx. We define
K sem k (x, y) =1 + cos(f(x), f(y)) 2 .(12)
This maps embedding similarity to [0,1] and is applied across all task families. Because crowding
can occur at different representational levels, we also evaluate task-specific kernels: plot-synopsis
crowding for narrative convergence in stories, concept-bucket crowding for repeated underlying uses
in AUT responses, and lexical-template overlap for repeated wording or phrase structure in slogans.
These kernels test whether the benchmark conclusions persist under domain-sensitive definitions of
idea-space overlap; implementation details are provided in Appendix D.
Matched estimation.For each model m, task condition k, and kernel Kk, we estimate human
and model-only crowding using matched-sample bootstrapping. Let nH k be the number of human
sampling units (authors for stories, participants for AUT, and slogans) and nA m,k the number of
model-only generations. Each bootstrap replicate samples bm,k = min{nH k , nA m,k} human units and
model generations with replacement, then computes the mean off-diagonal pairwise crowding:
bκH k = 1 bm,k(bm,k −1) X i̸=j Kk(hi, hj),bκ A m,k = 1 bm,k(bm,k −1) X i̸=j Kk(ai, aj).(13)
Within each task condition, we compute b∆m,k and bρm,k using Eqs. 2 and 3; task-family estimates
are then obtained by equal-weight aggregation across conditions. Confidence intervals are percentile
bootstrap intervals. For AUT and slogans, where human participants may contribute multiple
responses, we use participant-aware sampling: sample participants first, then sample one response
per selected participant. This prevents high-fluency participants from dominating the human baseline.
Aggregation and diagnostics.All quantities are estimated within a task-condition and then averaged
equally across conditions within a task family, so no prompt dominates because it has more human
responses. We assess finite-sample stability using rarefaction curves over model-only sample size.
5 Results
5.1 Neutral model-conditions fall below human-relative diversity parity
Figure 1 reports the main semantic benchmark under neutral prompting and the primary semantic
kernel. The dashed line marks ρ= 1 , the no-excess-crowding boundary from Proposition 1. All nine
neutral model-task combinations fall below this boundary, and in every case, the upper 95% bootstrap
6

Human
GPT-5.4
Claude Sonn 4.5
Gemini 2.5 Flash
(A) Story (B) AUT (C) Slogan
Mean semantic crowding, κ(n)
Sample size, n
0.60
0 10 20 30 40 50 0 10 20 30 40 50 0 10 20 30 40 50
0.5 0.5
0.6
0.7
0.8
0.9
1.0
0.6
0.7
0.8
0.9
1.0
0.70
0.80
0.90
Figure 2:Finite-sample stability of semantic crowding estimates.Curves show bκ(n)as a function
of sampled responses n, averaged across conditions within each task family. Shaded bands show 95%
intervals from repeated rarefaction samples.
confidence bound is also below one. Thus, under the primary semantic kernel, all evaluated neutral
model-conditioned source distributions introduce positive excess crowding relative to the matched
human baseline.
The estimates are interpretable as human-relative deficits rather than model-only diversity scores.
Their magnitudes vary across task and model conditions, consistent with the task-relative design of the
benchmark. For example, the slogan condition shows a large deficit for GPT-5.4, with bρ= 0.179and
b∆ = 0.331, while AUT shows a large deficit for Claude Sonnet 4.5, with bρ= 0.309and b∆ = 0.275.
These examples illustrate that excess crowding is not a single global property of a base model; it is
estimated for a specific model-condition, task condition, and crowding kernel. Full numeric estimates
are reported in Appendix E.
5.2 Crowding estimates stabilize with feasible model-only sample sizes
A development-time benchmark is useful only if its estimates stabilize with feasible model-only
sample sizes. We therefore use rarefaction to assess whether the pairwise crowding estimates
underlying b∆m,k are sensitive to the number of model generations sampled. This diagnostic concerns
estimation rather than deployment scale: n is the number of model-only samples used to estimate the
source-level crowding coefficient, whereas X−i in the adoption game is the number of other creators
using the same model-condition. Stability in n therefore supports reliable estimation of b∆m,k; it does
not imply that population-level redundancy stops growing with adoption.
Figure 2 shows that semantic crowding estimates stabilize within the sampled range. Betweenn= 40
and n= 50 , the largest relative change in task-level bκA is only 0.104%, observed for Gemini 2.5
Flash on slogans; all other model-task combinations change by less than 0.06% (see Appendix F).
The narrow intervals near n= 50 indicate that the chosen model-only sample size is sufficient for
stable estimation in this benchmark. This supports the practicality ofex anteevaluation: pairwise
crowding tendencies can be estimated with modest model-only samples, while the adoption game
separately describes how those tendencies compound with population exposure.
5.3 Excess crowding implies adoption-dependent benefit thresholds
Proposition 2 gives the benchmarked coefficient a decision-theoretic interpretation. The empirical
b∆m,k estimates do not measure user preferences directly; rather, they imply how large the private AI
advantage would need to be to offset redundancy costs at a given exposure level. Normalizing by the
task’s distinctiveness value gives
Bcrit m,k(X)
γk
= 1−exp{−X b∆m,k}.(14)
This quantity is the fraction of the task’s distinctiveness value that AI use must compensate for when
Xother creators use the same model-condition.
Even moderate pairwise excess crowding becomes strategically meaningful as exposure grows.
With only one other adopter, the implied critical benefit ranges from 12.4% to 28.2% of the full
7

GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
GPT
5.4
Claude
Sonnet 4.5
Gemini
2.5 Flash
(A) Story (B) AUT (C) Slogan
Human-relative diversity, ρ
Neutral prompt
Persona mixing
0.0
0.2
0.4
0.6
0.8
1.0
Figure 3:Persona-mixture prompting improves human-relative diversity.Bars compare the
neutral main protocol atT= 1.0with a persona-mixture protocol atT= 1.0. Error bars show 95%
bootstrap intervals. The dashed line marksρ= 1, the no-excess-crowding condition.
distinctiveness value γk. At X= 10 , the threshold ranges from 73.3% to 96.4% of γk; by X= 25 ,
every model-task curve exceeds 96% (see Appendix G). In the adoption game, this means that once
25 other creators draw from the same below-parity source, the private benefit of AI must offset
nearly the entire distinctiveness value in each evaluated model-task setting. This is the empirical
counterpart of Proposition 3: below-parity models may be rational in private or low-exposure settings,
but widespread adoption pushes users toward the full distinctiveness penalty.
5.4 Robustness across narrative, lexical, and concept-level kernels
We next test whether the below-parity conclusion persists under task-specific crowding kernels. For
stories, all models remain below parity under a plot-synopsis kernel: GPT-5.4 moves from bρ= 0.372
to 0.509, Claude Sonnet 4.5 from 0.485 to 0.594, and Gemini 2.5 Flash from 0.446 to 0.519. Thus,
story crowding persists when similarity is computed over plot synopses rather than full prose.
For slogans, all three models remain below parity under both lexical-template kernels. GPT-5.4 shows
substantial lexical crowding, with bρ= 0.368 under non-stopword Jaccard and bρ= 0.305 under
character-trigram Jaccard. Claude Sonnet 4.5 and Gemini 2.5 Flash are less lexically crowded, but
their lexical bρvalues remain below one. Thus, slogan crowding persists when overlap is defined by
reused words and phrase templates rather than semantic embedding similarity alone (see Appendix H).
For AUT, crowding also persists under concept-bucket co-membership. All three models remain
below parity: GPT-5.4 has bρ= 0.866, Claude Sonnet 4.5 has bρ= 0.715, and Gemini 2.5 Flash has
bρ= 0.938. Under this kernel, bκA is the probability that two model-only generations express the same
underlying use concept, so below-parity bρindicates that model generations repeat use concepts more
often than the matched human baseline. Together, these results illustrate the task-relative evaluation
logic: developers should specify a crowding kernel that matches the form of overlap relevant to their
creative domain. In our benchmark, human-relative excess crowding persists under narrative-level
overlap for stories, lexical-template overlap for slogans, and concept-level overlap for AUT, showing
how the same framework can be instantiated with domain-appropriate kernels.
5.5 Generation protocols can improve human-relative diversity
Finally, we test whether human-relative crowding changes under generation-protocol variants. We
use two illustrative levers—persona-mixture prompting and temperature tuning—to vary the model-
conditioned source distribution while holding the task fixed.
Figure 3 shows that persona-mixture prompting increases bρin eight of nine model-task combinations.
The only exception is GPT-5.4 on AUT, where the confidence interval includes zero (95% CI
[−0.053,0.017] ). The largest improvement occurs for GPT-5.4 on slogans: bρincreases by 0.749 and
b∆ decreases by 0.301. Claude Sonnet 4.5 nearly reaches parity on slogans, moving from bρ= 0.673
to 0.960, with a confidence interval crossing one. Thus, crowding is not fixed by the base model
8

alone; it can change substantially with the generation protocol. Notably, by Proposition 2, reducing b∆
also lowers the implied critical-benefit threshold. At X= 10 , persona-mixture prompting lowers the
normalized critical-benefit threshold in eight of nine model-task settings, with the largest reductions
for slogan generation (see Appendix I).
Temperature tuning provides a second protocol variant. Across the tested temperature grids, bρ
increases and b∆ decreases from the lowest to the highest temperature in all nine model-task com-
binations, with strict monotonic ordering in six (see Appendix I). Together, these results show that
human-relative crowding is an estimable property of a model-condition, not only a descriptive prop-
erty of a base model. This makes bρand b∆ actionable evaluation targets: they can be used to test
whether generation protocols reduce population-level crowding before deployment.
6 Discussion
This work reframes AI-induced diversity collapse as a development-time evaluation problem. Prior
human–AI studies show that AI assistance can improve individual creative outputs while making
the population of outputs more homogeneous [ 4, 18, 29]. Related model-side work shows that
LLMs themselves can produce unusually homogeneous creative responses, suggesting that source-
level similarity is a plausible mechanism behind downstream human–AI convergence [51, 52]. Our
framework formalizes this source-to-population link. If many users draw inspiration from the same
model-conditioned source distribution, then excess concentration in that source distribution becomes
a population-level crowding risk. Comparing model-only generations to matched unaided human
baselines therefore yields an excess-crowding coefficient and a human-relative parity condition before
new human–AI data are collected. This does not displace human–AI experiments; it gives developers
a principled way to evaluate model-conditions, prompts, decoding settings, and other interventions
before selecting which ones warrant costly human-subject testing.
Our empirical results suggest that this evaluation logic remains tractable across disparate creative
tasks. Across three task families, we find that neutral model conditions consistently fall below
human-relative parity, that crowding estimates stabilize with feasible sample sizes, and that protocol
variants (such as temperature and persona-mixture prompting) can significantly shift bρand b∆. We
view these variants as proof-of-concept explorations rather than final prescriptions. The broader
implication is that human-relative crowding is a measurable, estimable property of a model condition,
rendering diversity collapse an actionable target for optimization prior to deployment.
Crucially, the framework is designed as a generalizable procedure rather than a rigid task suite.
The three task families analyzed here were selected to capture varied output lengths, response
structures, and dimensions of crowding: compact stories for narrative convergence, slogans for
highly constrained creative spaces, and the AUT for classic divergent thinking. The newly collected
slogan baseline is particularly instructive, providing a fresh human reference for a task unlikely to be
contaminated by model training exposure. Any application of this framework requires a matched
human reference and a domain-appropriate crowding kernel. This task-relative structure is a deliberate
feature: it avoids evaluating model diversity in a vacuum and instead asks whether shared model use
introduces excess redundancy relative to the human counterfactual for a specific creative setting.
This perspective also clarifies the relationship between population-level diversity and established
metrics of individual creativity. Creativity research has long used complementary lenses: idea-intrinsic
quality measures, social-rarity measures, and subjective ratings [3, 41, 11, 6]. Our framework extends
the logic of social rarity to the generative era by quantifying how shared access to a model-conditioned
source reduces the distinctiveness of the population-level output. It is intended to complement, rather
than replace, intrinsic quality measures. A model condition may produce high-quality outputs while
suffering from severe crowding, or conversely, achieve high diversity at the expense of quality.
Developers must therefore evaluate population-level crowding alongside other dimensions relevant to
their creativity task.
Finally, the adoption game provides a theoretical foundation for why human-relative parity is a critical
benchmark. The critical-benefit curves translate b∆ into the marginal private benefit required to offset
redundancy costs under specific exposure models. While the exponential cost function serves as
a convenient monotone specification, the central insight is robust: any redundancy-cost function
that increases with crowding and exposure ensures that below-parity source distributions become
9

increasingly costly as adoption expands. At the limit of mass adoption, below-parity conditions
expose users to a maximum distinctiveness penalty. Human-relative parity thus represents the
fundamental condition under which shared model use introduces no excess crowding costs compared
to the baseline of human convergence.
7 Limitations
The empirical demonstration is limited to text-based creative tasks. Extending the framework to
images, music, code, scientific hypotheses, and multimodal design will require domain-specific
human baselines and kernels. The benchmark also estimates source-level crowding rather than the
full realized interaction process: interfaces, user expertise, selective uptake, and editing behavior can
mediate how model suggestions shape final human outputs.
10

A Proofs of Theoretical Results
A.1 Proof of Proposition 1
Proof.By definition,
∆m,k = max{0, κA m,k −κ H k }.
Therefore, ∆m,k = 0 if and only if κA m,k ≤κ H k . Since κH k <1 , the denominator of ρm,k is positive.
Hence,
κA m,k ≤κ H k ⇐ ⇒1−κ A m,k ≥1−κ H k ⇐ ⇒ 1−κ A m,k 1−κ H k ≥1.
By Eq. 3, this is equivalent toρ m,k ≥1. Thus,
∆m,k = 0⇐ ⇒ρ m,k ≥1.
A.2 Proof of Proposition 2
Proof.A rational creator adopts AI when
Bi,m,k > Cm,k(X−i).
Substituting the redundancy cost from Eq. 5 gives
Bi,m,k > γk (1−exp{−X −i∆m,k}).
Therefore adoption is rational if and only if
Bi,m,k > Bcrit m,k(X−i),
where
Bcrit m,k(X−i) =γ k (1−exp{−X −i∆m,k}).
It remains to show the monotonicity claims. The threshold is increasing in γk directly. For X−i ≥0
and∆ m,k ≥0,
∂B crit m,k
∂∆m,k
=γ kX−i exp{−X−i∆m,k} ≥0,
and
∂B crit m,k
∂X−i
=γ k∆m,k exp{−X−i∆m,k} ≥0.
Thus,B crit m,k is increasing in∆ m,k andX −i.
Forρ m,k <1, Eq. 8 gives
∆m,k = (1−ρ m,k)(1−κ H k ),
so
∂∆m,k
∂ρm,k
=−(1−κ H k )<0.
By the chain rule,
∂B crit m,k
∂ρm,k
=
∂B crit m,k
∂∆m,k
∂∆m,k
∂ρm,k
≤0.
Hence, forρ m,k <1, the critical benefit threshold is decreasing inρ m,k.
11

A.3 Proof of Eq. 10
Proof. Suppose each of the other N−1 creators independently adopts the same model-condition
with probabilityp. Then
X−i ∼Binomial(N−1, p).
From Eq. 5,
Cm,k(X−i) =γ k (1−exp{−X −i∆m,k}).
Taking expectations,
E[Cm,k] =γ k (1−E[exp{−X −i∆m,k}]).
For a binomial random variable X∼Binomial(N−1, p) , the probability generating function gives
E[tX ] = (1−p+pt) N−1 .
Settingt= exp{−∆ m,k}yields
E[exp{−X −i∆m,k}] = (1−p+pexp{−∆ m,k})N−1 .
Therefore,
E[Cm,k] =γ k
h
1−(1−p+pexp{−∆ m,k})N−1
i
.
A.4 Proof of Proposition 3
Proof.Ifρ m,k ≥1, then Proposition 1 implies∆ m,k = 0. Substituting into Eq. 5,
Cm,k(X−i) =γ k(1−exp{0}) = 0
for allX −i.
Ifρ m,k <1, then Eq. 8 implies
∆m,k = (1−ρ m,k)(1−κ H k )>0.
Therefore,
exp{−X−i∆m,k} →0asX −i → ∞.
Substituting into Eq. 5,
lim
X−i→∞
Cm,k(X−i) =γ k(1−0) =γ k.
Thus,
lim
X−i→∞
Cm,k(X−i) =
0, ρ m,k ≥1,
γk, ρ m,k <1.
B Human Baseline Datasets and Task Conditions
This appendix describes the human baselines used to instantiate the task-relative benchmark. All
duplicate human outputs are retained because duplicate or near-duplicate responses are part of the
crowding signal.
B.1 Short, prompted creative writing
The story baseline is drawn from theWritingPrompts corpus [21], a Reddit-based dataset of human-
written stories paired with writing prompts. The original corpus contains 303,358 prompt–story pairs,
split into 272,600 training, 15,620 validation, and 15,138 test stories. The corpus was collected from
Reddit’s r/WritingPrompts, where users submit story premises and other users write responses;
each prompt can therefore have multiple human-written stories. The dataset is distributed through the
fairseq story-generation example page; we report the prompt IDs and processing details needed to
reproduce our filtering from the original release.
We selected three high-response prompts that asked participants to produce compact narrative fiction
under shared constraints (see Table 1). Compact prompts were useful for the benchmark because they
reduce uncontrolled variation in response length while preserving narrative choice. Each prompt is
treated as a separate conditionk.
12

Table 1: WritingPrompts story conditions.Here, nH k denotes the number of available human
sampling units for condition k. Because each retained WritingPrompts response is one story from
one human author, nH k equals the number of human stories for each prompt. Word and sentence
counts are computed over these retained human stories.
Prompt ID Promptn H k Median words Median sentences
10491 A short horror story. Something to chill the
bones in one hundred words or less.
35 104 10.0
93742 100 Words or Less — The parachute isn’t open-
ing up
32 107 14.0
93855 Describe 100 years of a character’s life in 10
words. Then describe the last 10 seconds of their
life in 100 words.
20 112 10.5
B.2 Alternative Uses Task
The Alternative Uses Task (AUT) baseline comes from thesocialmuse dataset [10]. Participants
completed a divergent thinking task in which they generated alternative uses for common objects
while excluding the object’s primary use. The retained human baseline contains 109 participants, 5
object conditions, and 3,047 unaided ideas (see Table 2). Participants contributed up to six ideas per
object; the median participant produced 30 ideas across the five objects. Responses range from short
phrases to full sentences. For example, for the object “shoe,” human responses include “We can use
a shoe as a hamster bed” and “As a doorstop.” In participant-aware bootstrapping, participants are
sampled first, and then one response is sampled per selected participant within each object condition.
The original authors provided the dataset and granted permission for research use.
Table 2:Alternative Uses Task conditions.Only unaided human ideas are retained. Here, nH k
denotes the number of available human sampling units for condition k; because participant-aware
sampling is used,n H k equals the number of participants.
Object Common usen H k Ideas Unique ideas Median words
Shoe used as footwear 109 604 532 3
Button used to fasten things 109 603 583 4
Key used to open a lock 109 612 574 4
Wooden pencil used for writing 109 613 583 4
Automobile tire used on the wheel of an automobile 109 615 575 5
B.3 Smartphone marketing slogans
We collected unaided slogan baseline data through an IRB-approved online study with U.S.-based
participants recruited from Prolific (see Table 3). All participants provided informed consent before
beginning the study and were paid at the local minimum hourly rate at the end of the task. Participants
were asked to generate creative marketing slogans for a hypothetical new smartphone. The retained
dataset contains 659 slogans from 95 participants, of which 650 are unique strings (see Table 4). The
median slogan length is 4 words; only one slogan exceeds the requested six-word maximum. Exact
duplicate slogans are retained because repeated slogans are part of the human crowding baseline.
Participants saw the following instruction:
You are part of the marketing team at a tech company preparing to launch a new
smartphone. You are tasked with coming up with creative new marketing slogans
for this brand-new smartphone. Your task is to:
• Come up with as many creative marketing slogans as you can for this brand
new smartphone. The slogans need to be novel and appropriate.
• You must create at least 3 slogans, but please try to generate as many slogans
as possible.
• Each slogan should not exceed 6 words.
• You can assume any detail about the smartphone – be as creative as you want!
13

• You will have 3 minutes for this task.
Table 3:Demographic composition of the smartphone slogan study.Counts are reported for the
participants who completed the slogan task and demographic questionnaire. Race categories are not
mutually exclusive if participants selected multiple categories.
Category Group Number of participants
Age 18–24 12
Age 25–34 31
Age 35–44 30
Age 45–54 10
Age 55–64 9
Age 65+ 3
Gender Male 46
Gender Female 48
Gender Non-binary 1
Education High school graduate 12
Education Some college 16
Education Associate degree 6
Education Bachelor’s degree 39
Education Master’s degree 17
Education Professional degree 3
Education Doctorate degree 2
Hispanic Origin Yes 14
Hispanic Origin No 81
Race American Indian or Alaska Native 1
Race Asian 20
Race Black or African American 14
Race Native Hawaiian or Other Pacific Islander 1
Race Other 5
Race White 58
Table 4:Smartphone slogan condition. nH k denotes the number of available human sampling units
for conditionk; because participant-aware sampling is used,n H k equals the number of participants.
Condition Slogans Unique slogansn H k Mean slogans / participant Median words
Smartphone 659 650 95 6.94 4
As with the AUT baseline, participant-aware bootstrapping samples participants first and then samples
one slogan per selected participant. This prevents high-fluency participants from dominating the
human baseline.
C Model Prompts and Generation Protocols
This appendix documents the model-only generation protocols used in the benchmark. For every task
condition, models were prompted to generate exactly one creative product per request. This makes
the model sampling unit parallel to the human sampling unit used in the matched benchmark.
C.1 Models and generation scenarios
We generated outputs from GPT-5.4, Claude Sonnet 4.5, and Gemini 2.5 Flash. For each model-
task pair, the main benchmark used neutral prompting at temperature T= 1.0 with 50 model-
only generations per task condition. We also collected deployment-variant samples using neutral
temperature changes and persona-mixture prompting (Table 5).
14

Table 5:Model generation scenarios.The main benchmark uses neutral prompting at T= 1.0 .
Temperature and persona-mixture generations are used for deployment-variant analyses.
Scenario Description Generations / condition Personas
Neutral main Neutral prompt atT= 1.050 1
Temperature robustness Neutral prompt at non-default
temperatures
10 per temperature 1
Persona mixture 32 persona profiles crossed with
temperature
10 per persona-temperature pair 32
For the neutral temperature-robustness scenario, the non-default temperatures were {0.7,1.3} for
GPT-5.4 and Gemini 2.5 Flash, and {0.3,0.7} for Claude Sonnet 4.5. The T= 1.0 neutral condition
is supplied by the main benchmark.
C.2 Neutral system instructions
For stories, the neutral system instruction was:
You are participating in a creative writing task. Respond to the prompt as a human
participant would. Follow the prompt’s constraints exactly. Do not explain your
answer. Do not include commentary before or after the creative response.
For AUT and slogans, the neutral system instruction was:
You are participating in a creativity test. Follow the task instructions exactly. Do
not explain your reasoning. Do not include commentary before or after the answer.
Task-specific user prompts.Stories.For each selected WritingPrompts condition, the user
prompt was:
Prompt:
<story prompt>
where<story prompt>was replaced with the corresponding prompt text in Table 1.
Alternative Uses Task.For each AUT object, the user prompt was:
Object:<object>
Common use to avoid:<common use>
Generate exactly one unusual, creative, and plausible alternative use for the object
or one of its parts. Do not use the common use. Do not list multiple uses. Return
only the alternative use as a short phrase or one sentence.
The object and common-use pairs are listed in Table 2.
Smartphone slogans.For the slogan task, the user prompt was:
You are part of the marketing team at a tech company preparing to launch a new
smartphone.
Generate exactly one creative marketing slogan for this brand new smartphone.
Requirements:
• The slogan must be novel and appropriate.
• The slogan must not exceed 6 words.
• You may assume any detail about the smartphone.
• Do not list multiple slogans.
• Return only the slogan text.
15

C.3 Persona-mixture prompting
The persona-mixture protocol crossed five binary personality dimensions, yielding 25 = 32 profiles:
{extroverted,introverted} × {agreeable,antagonistic}
× {conscientious,unconscientious} × {neurotic,emotionally stable}
× {open to experience,closed to experience}.
For stories, the following instruction was appended to the neutral system instruction:
Write as if you are a person with the following personality profile: <traits>. Let
this personality influence the creative choices, tone, voice, imagery, pacing, and
emotional framing of the story, while still following the user’s writing prompt
exactly.
For AUT, the following instruction was appended:
Write as if you are a person with the following personality profile: <traits>. Let
this personality influence the creative choice, style, and framing of the idea, while
still following the task exactly.
For slogans, the following instruction was appended:
Write as if you are a person with the following personality profile: <traits>. Let
this personality influence the creative choice, style, tone, and framing of the slogan,
while still following the task exactly.
In each case, <traits> was replaced by the comma-separated traits in one of the 32 personality
profiles.
C.4 Output limits
Maximum output lengths were set by task family: 800 tokens for stories, 120 tokens for AUT
responses, and 40 tokens for slogans. These limits were ceilings rather than target lengths; all prompts
instructed models to return only the requested creative product.
D Crowding Kernels
The benchmark is task-relative: each kernel defines what it means for two outputs to occupy
nearby regions of idea-space in a given task. The primary semantic kernel in Eq. 12 pro-
vides a common measure across all task families. For all primary semantic analyses, we use
sentence-transformers/all-mpnet-base-v2 to compute sentence embeddings and normalize
embeddings before computing cosine similarity. The same embedding model is also used for the
plot-synopsis story kernel and for nearest-neighbor retrieval in the AUT concept-bucketing pipeline.
D.1 Story plot-synopsis kernel
Full-story semantic similarity can reflect plot, style, setting, tone, and surface phrasing. To isolate
narrative-content crowding, we generate a one-sentence plot synopsiss(x) for each story and compute
semantic crowding over synopsis embeddings. Synopses were generated with GPT-5.4 at temperature
T= 0 and a maximum output length of 80 tokens. Duplicate story texts were summarized once and
then mapped back to all corresponding story rows, preserving duplicates for the crowding analysis.
The system instruction for synopsis generation was:
You convert creative stories into concise plot synopses for research analysis. Follow
the instructions exactly. Do not add commentary.
For each story, the user prompt was:
16

Summarize the following story as exactly one sentence.
Focus on the plot: the protagonist or central entity, the main situation, the central
conflict or change, and the outcome if it is present.
Do not evaluate the writing quality. Do not mention the author. Do not quote the
story. Do not include labels such as ‘Synopsis:’. Return only the one-sentence plot
synopsis.
STORY:
<story text>
We manually checked a random 10% of all story synopses generated by this method, and found all of
those synopses to be appropriate.
Let s(x) denote the generated synopsis for story x. We embed synopses using
sentence-transformers/all-mpnet-base-v2and compute
K plot k (x, y) =1 + cos(f(s(x)), f(s(y))) 2 .(15)
This kernel measures whether stories converge on similar plot content rather than only on similar
full-prose representations.
D.2 AUT concept-bucket kernel
For alternative uses, semantic similarity may obscure whether two responses express the same
underlying use concept. We therefore construct object-specific concept codebooks using a retrieval-
assisted LLM bucketing pipeline psychometrically validated in MuseScorer [6]. Human and model
responses are pooled within each object condition, and each object receives its own codebook because
bucket IDs are meaningful only within object condition.
For each AUT object, the pooled file includes human responses and model responses from
the main and deployment-variant generation scenarios. Exact duplicate responses are re-
tained because repeated responses are part of the crowding signal. Each pooled response
is assigned to a concept bucket using the original annotation utility with the following
configuration: LLM judge llama3.3:70b-Instruct through Ollama, embedding model
sentence-transformers/all-mpnet-base-v2, Kc = 10 nearest comparison candidates, and
CoT prompt method, based on the exact LLM settings validated to be the best-performing by the
original authors. This bucketing was conducted using an Intel Core i7-based computer with 64GB
RAM and an RTX3070Ti graphics card. The final result generation took roughly5GPU days.
The bucketing procedure proceeds sequentially within each object. For a new response, the pipeline
retrieves the Kc = 10 nearest existing bucket exemplars under the embedding model, then asks the
LLM judge whether the response is an obvious rephrasing of an existing concept or should form a new
bucket. The common use of each object is supplied as a forbidden idea and inserted as comparison
idea ID 0 in the original pipeline.
Let bk(x) denote the assigned bucket for response x within object condition k. The concept-bucket
kernel is
K bucket k (x, y) =1{bk(x) =b k(y)}.(16)
Under this kernel, κH k is the probability that two human responses express the same underlying use
concept, andκ A m,k is the corresponding probability for model-only generations.
D.3 Slogan lexical-template kernels
For slogans, short length makes lexical reuse especially important. We therefore compute two
lexical-template kernels in addition to the primary semantic kernel. Before computing lexical overlap,
slogans are lowercased and normalized by stripping punctuation and collapsing whitespace.
The first lexical kernel is non-stopword token Jaccard similarity:
K word k (x, y) =|T(x)∩T(y)| |T(x)∪T(y)| ,(17)
17

where T(x) is the set of non-stopword tokens in slogan x. The second is character-trigram Jaccard
similarity:
K tri k (x, y) =|G3(x)∩G 3(y)| |G3(x)∪G 3(y)| ,(18)
where G3(x) is the set of character trigrams after lowercasing and normalizing punctuation and
whitespace. The word-level kernel captures repeated content words, while the trigram kernel captures
more fine-grained phrase-template overlap.
E Additional Main Semantic Crowding Results
E.1 Task-family semantic benchmark
Table 6 reports the full numeric estimates for the main semantic benchmark shown visually in Fig. 1.
Table 6:Semantic crowding benchmark.Each row reports equal-weight task-family estimates
under the primary semantic kernel. Confidence intervals are percentile bootstrap intervals forbρ.
Model Taskbκ H bκA b∆bρ95% CI forbρ
GPT-5.4 Stories 0.706 0.892 0.186 0.372 [0.338, 0.408]
Claude Sonnet 4.5 Stories 0.706 0.857 0.151 0.485 [0.441, 0.533]
Gemini 2.5 Flash Stories 0.705 0.869 0.164 0.446 [0.406, 0.490]
GPT-5.4 AUT 0.601 0.791 0.190 0.525 [0.499, 0.548]
Claude Sonnet 4.5 AUT 0.601 0.877 0.275 0.309 [0.277, 0.340]
Gemini 2.5 Flash AUT 0.601 0.743 0.142 0.645 [0.612, 0.677]
GPT-5.4 Slogans 0.597 0.928 0.331 0.179 [0.096, 0.275]
Claude Sonnet 4.5 Slogans 0.597 0.729 0.132 0.672 [0.596, 0.734]
Gemini 2.5 Flash Slogans 0.597 0.733 0.136 0.662 [0.562, 0.746]
E.2 Human versus AI crowding
Figure 4 plots bκH against bκA at the task-family level. All model-task points lie above the diagonal,
indicating that AI outputs are more semantically crowded than the matched human baseline in every
main benchmark comparison.
0.60 0.65 0.70 0.75 0.80 0.85 0.90 0.95
Human crowding,
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95AI crowding,
Claude Sonnet 4.5 / aut
GPT-5.4 / aut
Gemini 2.5 Flash / aut
Claude Sonnet 4.5 / slogan
GPT-5.4 / slogan
Gemini 2.5 Flash / slogan
Claude Sonnet 4.5 / story
GPT-5.4 / story
Gemini 2.5 Flash / story
Semantic crowding: humans vs AI
Figure 4:Human versus AI semantic crowding.Each point is a model-task comparison. Points
above the diagonal havebκA >bκH, corresponding to positive excess crowding.
18

F Finite-Sample Stability Diagnostics
F.1 Task-level rarefaction drift
Table 7 reports the task-level change in mean semantic crowding from n= 40 to n= 50 for the
rarefaction curves. Relative drift is computed as |bκ(50)−bκ(40)|/|bκ(50)|. For human stories, the
maximum available rarefaction size differs because the story prompts have fewer human responses;
the reported human story drift usesn= 25ton= 35.
Table 7:Task-level recent drift in semantic crowding estimates.All values are computed from
task-level rarefaction curves under the primary semantic kernel.
Source Model Taskn low nhigh bκ(nlow)bκ(n high)Relative drift
AI Claude Sonnet 4.5 AUT 40 50 0.874064 0.874004 0.0069%
AI GPT-5.4 AUT 40 50 0.786562 0.786407 0.0196%
AI Gemini 2.5 Flash AUT 40 50 0.737719 0.737773 0.0073%
Human Human AUT 40 50 0.600302 0.600237 0.0109%
AI Claude Sonnet 4.5 Slogans 40 50 0.723630 0.723616 0.0019%
AI GPT-5.4 Slogans 40 50 0.926871 0.926327 0.0587%
AI Gemini 2.5 Flash Slogans 40 50 0.728476 0.727721 0.1038%
Human Human Slogans 40 50 0.596146 0.596149 0.0005%
AI Claude Sonnet 4.5 Stories 40 50 0.853920 0.854035 0.0135%
AI GPT-5.4 Stories 40 50 0.889544 0.889512 0.0036%
AI Gemini 2.5 Flash Stories 40 50 0.866477 0.866443 0.0039%
Human Human Stories 25 35 0.701182 0.687392 2.0061%
G Critical-Benefit Thresholds
Figure 5 plots the normalized critical-benefit curves implied by the main semantic excess-crowding
estimates. Table 8 reports the same thresholds at selected exposure levels. Values are computed as
Bcrit(X)/γ= 1−exp(−X b∆).
0 5 10 15 20 25 30
Other adopters, X
0.0
0.2
0.4
0.6
0.8
1.0Critical benefit, Bcrit/
Stories
0 5 10 15 20 25 30
Other adopters, X
AUT
0 5 10 15 20 25 30
Other adopters, X
Slogans
Model
Claude Sonnet 4.5
GPT-5.4
Gemini 2.5 Flash
Figure 5:Critical private benefit required for rational adoption.Each curve shows Bcrit(X)/γ=
1−exp(−X b∆), using the main semantic excess-crowding estimate for one model-task pair. Lower
human-relative diversity raises the private AI benefit required to justify adoption in crowded settings.
H Kernel Robustness
H.1 Story plot-synopsis kernel
The story robustness analysis evaluates whether below-parity crowding persists when stories are
represented by one-sentence plot synopses rather than full prose. This kernel reduces the influence of
style, wording, and surface phrasing, and instead measures convergence in narrative content.
Figure 6 shows that the plot-synopsis kernel reduces the magnitude of the story deficit but does not
remove it. GPT-5.4 moves from bρ= 0.372under full-text similarity to 0.509 under plot-synopsis
19

Table 8:Normalized critical benefit thresholds.Each entry is the fraction of the task’s distinctive-
ness valueγthat AI must compensate for at exposure levelX.
Model Task b∆X= 1X= 5X= 10X= 25
GPT-5.4 Stories 0.186 0.170 0.605 0.844 0.990
Claude Sonnet 4.5 Stories 0.151 0.140 0.530 0.779 0.977
Gemini 2.5 Flash Stories 0.164 0.151 0.560 0.806 0.983
GPT-5.4 AUT 0.190 0.173 0.613 0.850 0.991
Claude Sonnet 4.5 AUT 0.275 0.240 0.747 0.936 0.999
Gemini 2.5 Flash AUT 0.142 0.132 0.508 0.758 0.971
GPT-5.4 Slogans 0.331 0.282 0.809 0.964 1.000
Claude Sonnet 4.5 Slogans 0.132 0.124 0.483 0.733 0.963
Gemini 2.5 Flash Slogans 0.136 0.127 0.493 0.743 0.967
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
0.0
0.2
0.4
0.6
0.8
1.0Human-relative diversity,
full_text_semantic_embedding
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
Human-relative diversity,
story_plot_synopsis_embedding
Story crowding by full-text and plot-synopsis kernels
Figure 6:Story crowding under full-text and plot-synopsis kernels.Points show task-family
estimates of bρfor each model; bars show 95% bootstrap intervals. The dashed line marks ρ= 1 ,
the no-excess-crowding condition. All models remain below parity under the plot-synopsis kernel,
indicating that story crowding persists when similarity is computed over narrative content rather than
full prose.
similarity, Claude Sonnet 4.5 moves from 0.485 to 0.594, and Gemini 2.5 Flash moves from 0.446 to
0.519. Thus, part of the full-text story effect reflects prose-level convergence, but the below-parity
pattern remains after reducing stories to narrative synopses.
To assess finite-sample stability under this robustness kernel, Figure 7 reports the task-level rarefaction
curves for plot-synopsis crowding. The model curves stabilize within the sampled range, indicating
that the narrative-level crowding estimates are not driven by the final few model-only generations.
H.2 Slogan lexical-template kernels
Figure 8 shows the human relative diversity of slogans under lexical template kernels. All models
remain below human parity.
Figures 9 and 10 show rarefaction curves for the slogan lexical-template kernels. The curves stabilize
by n= 50 , indicating that the lexical-template estimates are not driven by finite model-only sample
size.
H.3 AUT concept-bucket kernel
The AUT concept-bucket kernel evaluates whether two responses express the same underlying use
concept. Human and model responses are assigned to object-specific buckets, and the kernel equals
one when two responses fall in the same bucket and zero otherwise. Thus, under this kernel, bκis the
probability that two sampled responses reuse the same concept.
Figure 11 compares the primary semantic kernel with the concept-bucket kernel. Under concept-
bucket co-membership, all three models remain below parity: GPT-5.4 has bρ= 0.866with 95% CI
20

0 10 20 30 40 50
Sampled responses, n
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95Plot-synopsis crowding, (n)
Story plot-synopsis rarefaction
Source / model
Human
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 7:Rarefaction curve for story plot-synopsis crowding.Curves show mean plot-synopsis
crowding bκ(n)as a function of sampled responses n, aggregated across story prompts. The dashed
vertical line marks n= 50 . The curves assess whether the narrative-level crowding estimates are
stable with the available model-only sample size.
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
0.0
0.2
0.4
0.6
0.8
1.0Human-relative diversity,
semantic_embedding
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
Human-relative diversity,
word_jaccard_nonstop
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
Human-relative diversity,
char_trigram_jaccard
Slogan crowding by semantic and lexical-template kernels
Figure 8:Slogan crowding under semantic and lexical-template kernels.Points show bρfor each
model; bars show 95% bootstrap intervals. The dashed line marks ρ= 1 , the no-excess-crowding
condition. All models remain below parity under semantic, word-overlap, and character-trigram
kernels.
[0.833,0.894] , Claude Sonnet 4.5 has bρ= 0.715with 95% CI [0.665,0.759] , and Gemini 2.5 Flash
hasbρ= 0.938with 95% CI[0.920,0.953]. Figure 12 shows the rarefaction curves.
I Protocol Diagnostics
I.1 Persona-mixture protocol comparison
Table 9 reports the direct comparison between the neutral main protocol and persona-mixture
prompting atT= 1.0. Difference intervals are bootstrap intervals forbρ persona −bρmain.
Figure 13 shows how persona-mixture prompting lowers the critical private benefit required for
rational adoption.
I.2 Temperature-grid monotonicity
Figure 14 reports human-relative diversity over the tested temperature grid. The neutral T= 1.0
point is downsampled to match the robustness sample size, making it comparable to the non-main
temperature settings.
Figure 15 reports the corresponding effect on excess crowding.
21

0 10 20 30 40 50
Sample size n
0.0
0.2
0.4
0.6
0.8
1.0Mean lexical crowding (n)
Slogan lexical-template saturation: word_jaccard_nonstop
Source/model
Human
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 9:Rarefaction curve for slogan non-stopword Jaccard crowding.Curves show mean
lexical crowdingbκ(n)as a function of sampled slogansn. The dashed vertical line marksn= 50.
0 10 20 30 40 50
Sample size n
0.0
0.2
0.4
0.6
0.8
1.0Mean lexical crowding (n)
Slogan lexical-template saturation: char_trigram_jaccard
Source/model
Human
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 10:Rarefaction curve for slogan character-trigram crowding.Curves show mean lexical
crowdingbκ(n)as a function of sampled slogansn. The dashed vertical line marksn= 50.
Table 10 reports monotonic associations between temperature and crowding metrics. Because each
model-task pair has only three temperature points, these tests are descriptive diagnostics rather than
large-sample trend tests.
I.3 Best observed protocol and critical-benefit curves
The main protocol analysis isolates persona-mixture prompting at fixed T= 1.0 . As an additional
diagnostic, we identify the best observed protocol among the tested temperature and persona-mixture
settings for each model-task pair. Figure 16 compares the neutral main critical-benefit curve with the
best observed protocol curve.
22

GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
0.0
0.2
0.4
0.6
0.8
1.0Human-relative diversity,
Semantic
GPT-5.4
Claude Sonnet 4.5 Gemini 2.5 Flash
Human-relative diversity,
Concept Bucket
AUT crowding by semantic and concept-bucket kernels
Figure 11:AUT crowding under semantic and concept-bucket kernels.Points show task-family
estimates of bρfor each model; bars show 95% bootstrap intervals. The dashed line marks ρ= 1 ,
the no-excess-crowding condition. All models remain below parity under the concept-bucket kernel,
indicating excess concept reuse relative to the matched human baseline.
10 20 30 40 50
Sample size, n
0.0
0.1
0.2
0.3
0.4
0.5
0.6Concept-bucket crowding, (n)
AUT concept-bucket rarefaction
Source / model
Human
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 12:Rarefaction curve for AUT concept-bucket crowding.Curves show mean concept-
bucket crowding bκ(n)as a function of sampled responses n, aggregated across AUT objects. The
dashed vertical line marks n= 50 . The curves assess whether the concept-level crowding estimates
are stable with the available model-only sample size.
Table 9:Persona mixture versus neutral main prompting at fixed temperature.Both protocols
useT= 1.0. Positive∆bρindicates improved human-relative diversity under persona mixture.
Task Model MainbρPersonabρ∆bρ95% CI for∆bρ
AUT Claude Sonnet 4.5 0.309 0.739 0.430 [0.388, 0.474]
AUT GPT-5.4 0.526 0.507 -0.018 [-0.053, 0.017]
AUT Gemini 2.5 Flash 0.645 0.766 0.121 [0.080, 0.164]
Slogans Claude Sonnet 4.5 0.673 0.960 0.287 [0.201, 0.382]
Slogans GPT-5.4 0.179 0.927 0.749 [0.650, 0.846]
Slogans Gemini 2.5 Flash 0.660 0.926 0.265 [0.153, 0.391]
Stories Claude Sonnet 4.5 0.486 0.699 0.213 [0.145, 0.284]
Stories GPT-5.4 0.372 0.616 0.244 [0.189, 0.300]
Stories Gemini 2.5 Flash 0.446 0.724 0.278 [0.212, 0.345]
23

0 10 20 30 40 50
Population exposure, X
0.0
0.2
0.4
0.6
0.8
1.0Critical benefit threshold, Bcrit(X)/
Xmax = 50
STORY
0 5 10 15 20 25 30 35 40
Population exposure, X
Xmax = 40
AUT
0 25 50 75 100 125 150 175 200
Population exposure, X
Xmax = 220
SLOGAN
Model
GPT-5.4 Claude Sonnet 4.5 Gemini 2.5 Flash
Protocol
Neutral main, T = 1.0 Persona mixture, T = 1.0
Figure 13:Persona-mixture prompting lowers the critical private benefit required for rational
adoption.Solid curves show the neutral main protocol at T= 1.0 ; dashed curves show the persona-
mixture protocol at T= 1.0 . Curves plot Bcrit(X)/γ= 1−exp(−X b∆). Lower curves indicate
weaker congestion externalities.
0.4 0.6 0.8 1.0 1.2
T emperature
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0Human-relative diversity,
STORY
0.4 0.6 0.8 1.0 1.2
T emperature
0.2
0.4
0.6
0.8
1.0Human-relative diversity,
AUT
0.4 0.6 0.8 1.0 1.2
T emperature
0.0
0.2
0.4
0.6
0.8
1.0Human-relative diversity,
SLOGAN
Model
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 14:Temperature-grid effects on human-relative diversity.Points show task-level bρunder
the primary semantic kernel across available temperatures. Error bars show 95% bootstrap intervals.
Higher temperature increases bρfrom the lowest to highest tested temperature in all nine model-task
combinations, although strict monotonicity holds in six of nine.
0.4 0.6 0.8 1.0 1.2
T emperature
0.12
0.14
0.16
0.18
0.20
0.22
0.24Excess crowding,
STORY
0.4 0.6 0.8 1.0 1.2
T emperature
0.10
0.15
0.20
0.25
0.30
0.35Excess crowding,
AUT
0.4 0.6 0.8 1.0 1.2
T emperature
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40Excess crowding,
SLOGAN
Model
GPT-5.4
Claude Sonnet 4.5
Gemini 2.5 Flash
Figure 15:Temperature-grid effects on excess crowding.Points show task-level b∆ under the
primary semantic kernel across available temperatures. Error bars show 95% bootstrap intervals.
Higher temperature decreases b∆ from the lowest to highest tested temperature in all nine model-task
combinations.
24

Table 10:Temperature-grid monotonicity diagnostics.Positive ρs(T,bρ)indicates that higher
temperature is associated with higher human-relative diversity. Negative ρs(T, b∆) indicates that
higher temperature is associated with lower excess crowding.
Task Model∆bρ ρ s(T,bρ) ∆ b∆ρ s(T, b∆)
AUT Claude Sonnet 4.5 0.143 1.0 -0.057 -1.0
AUT GPT-5.4 0.014 0.5 -0.005 -0.5
AUT Gemini 2.5 Flash 0.146 1.0 -0.058 -1.0
Slogans Claude Sonnet 4.5 0.254 1.0 -0.102 -1.0
Slogans GPT-5.4 0.163 1.0 -0.065 -1.0
Slogans Gemini 2.5 Flash 0.141 1.0 -0.056 -1.0
Stories Claude Sonnet 4.5 0.198 1.0 -0.058 -1.0
Stories GPT-5.4 0.048 0.5 -0.015 -0.5
Stories Gemini 2.5 Flash 0.023 0.5 -0.007 -0.5
0 10 20 30 40 50
Population exposure, X
0.0
0.2
0.4
0.6
0.8
1.0Critical benefit threshold, Bcrit(X)/
STORY
0 10 20 30 40 50
Population exposure, X
AUT
0 25 50 75 100 125 150 175 200
Population exposure, X
SLOGAN
Model
GPT-5.4 Claude Sonnet 4.5 Gemini 2.5 Flash
Protocol
Neutral main Best observed protocol
Figure 16:Critical benefit curves under neutral main and best observed protocols.For each
model-task pair, the solid curve shows the neutral main protocol and the dashed curve shows the
best observed protocol among the tested temperature and persona-mixture settings. Curves plot
Bcrit(X)/γ= 1−exp(−X b∆). This figure is descriptive: it shows the best protocol found in the
tested grid, not an optimized global protocol.
25

References
[1] Selcuk Acar and Mark A Runco. Assessing associative distance among ideas elicited by tests of
divergent thinking.Creativity Research Journal, 26(2):229–238, 2014.
[2] Mirza Nayeem Ahmed and Raiyan Abdul Baten. From semantic memory to collective creativity:
A generative cognitive foundation for social creativity models. InProceedings of the Annual
Meeting of the Cognitive Science Society, volume 48, 2026.
[3] Teresa M Amabile. Social psychology of creativity: A consensual assessment technique.
Journal of Personality and Social Psychology, 43(5):997, 1982.
[4] Barrett R Anderson, Jash Hemant Shah, and Max Kreminski. Homogenization effects of Large
Language Models on human creative ideation. InProceedings of the 16th Conference on
Creativity & Cognition, pages 413–425, 2024.
[5] Joshua Ashkinaze, Julia Mendelsohn, Li Qiwei, Ceren Budak, and Eric Gilbert. How AI ideas
affect the creativity, diversity, and evolution of human ideas: evidence from a large, dynamic
experiment. InProceedings of the ACM Collective Intelligence Conference, pages 198–213,
2025.
[6] Ali Sarosh Bangash, Krish Veera, Ishfat Abrar Islam, and Raiyan Abdul Baten. MuseScorer:
Idea originality scoring at scale. InProceedings of the 2025 Conference on Empirical Methods
in Natural Language Processing, pages 19947–19965, 2025.
[7] Raiyan Abdul Baten, Richard N Aslin, Gourab Ghoshal, and Ehsan Hoque. Cues to gender
and racial identity reduce creativity in diverse social networks.Scientific Reports, 11(1):10261,
2021.
[8] Raiyan Abdul Baten, Richard N Aslin, Gourab Ghoshal, and Ehsan Hoque. Novel idea
generation in social networks is optimized by exposure to a “Goldilocks” level of idea-variability.
PNAS Nexus, 1(5):pgac255, 2022.
[9] Raiyan Abdul Baten, Daryl Bagley, Ashely Tenesaca, Famous Clark, James P Bagrow, Gourab
Ghoshal, and Ehsan Hoque. Creativity in temporal social networks: How divergent thinking is
impacted by one’s choice of peers.Journal of the Royal Society Interface, 17(171):20200667,
2020.
[10] Raiyan Abdul Baten, Ali Sarosh Bangash, Krish Veera, Gourab Ghoshal, and Ehsan Hoque. AI
can enhance creativity in social networks.arXiv preprint arXiv:2410.15264, 2024.
[11] Roger E Beaty and Dan R Johnson. Automating creativity assessment with SemDis: An open
platform for computing semantic distance.Behavior Research Methods, 53(2):757–780, 2021.
[12] Kenes Beketayev and Mark A Runco. Scoring divergent thinking tests by computer with a
semantics-based algorithm.Europe’s Journal of Psychology, 12(2):210, 2016.
[13] Terry Bossomaier, Mike Harré, Anthony Knittel, and Allan Snyder. A semantic network
approach to the Creativity Quotient (CQ).Creativity Research Journal, 21(1):64–71, 2009.
[14] Philip Buczak, He Huang, Boris Forthmann, and Philipp Doebler. The machines take over:
A comparison of various supervised learning approaches for automated scoring of divergent
thinking tasks.The Journal of Creative Behavior, 57(1):17–36, 2023.
[15] Tuhin Chakrabarty and Paramveer S Dhillon. Can good writing be generative? expert-level AI
writing emerges through fine-tuning on high quality books. InProceedings of the 2026 CHI
Conference on Human Factors in Computing Systems, pages 1–27, 2026.
[16] Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, and Chien-Sheng
Wu. Art or artifice? Large Language Models and the false promise of creativity. InProceedings
of the 2024 CHI Conference on Human Factors in Computing Systems, pages 1–34, 2024.
[17] Colin G DeYoung, Joseph L Flanders, and Jordan B Peterson. Cognitive abilities involved
in insight problem solving: An individual differences model.Creativity Research Journal,
20(3):278–290, 2008.
26

[18] Anil R Doshi and Oliver P Hauser. Generative AI enhances individual creativity but reduces the
collective diversity of novel content.Science Advances, 10(28):eadn5290, 2024.
[19] Denis Dumas and Kevin N Dunbar. Understanding fluency and originality: A latent variable
perspective.Thinking Skills and Creativity, 14:56–67, 2014.
[20] Denis Dumas, Peter Organisciak, and Michael Doherty. Measuring divergent thinking originality
with human raters and text-mining models: A psychometric comparison of methods.Psychology
of Aesthetics, Creativity, and the Arts, 15(4):645, 2021.
[21] Angela Fan, Mike Lewis, and Yann Dauphin. Hierarchical neural story generation. InProceed-
ings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pages 889–898, 2018.
[22] Boris Forthmann, Sue Hyeon Paek, Denis Dumas, Baptiste Barbot, and Heinz Holling. Scru-
tinizing the basis of originality in divergent thinking tests: On the measurement precision of
response propensity estimates.British Journal of Educational Psychology, 90(3):683–699,
2020.
[23] Joy Paul Guilford.The Nature of Human Intelligence. McGraw-Hill, 1967.
[24] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural
text degeneration.arXiv preprint arXiv:1904.09751, 2019.
[25] Zhaoyi Joey Hou, Bowei Alvin Zhang, Yining Lu, Bhiman Kumar Baghel, Anneliese Brei,
Ximing Lu, Meng Jiang, Faeze Brahman, Snigdha Chaturvedi, Haw-Shiuan Chang, Daniel
Khashabi, and Xiang Lorraine Li. CreativityPrism: A holistic benchmark for Large Language
Model creativity.arXiv preprint arXiv:2510.20091, 2025.
[26] Mete Ismayilzada, Claire Stevenson, and Lonneke van der Plas. Evaluating creative short story
generation in humans and Large Language Models.arXiv preprint arXiv:2411.02316, 2024.
[27] Sean Kelty, Raiyan Abdul Baten, Adiba Mahbub Proma, Ehsan Hoque, Johan Bollen, and
Gourab Ghoshal. The innovation trade-off: how following superstars shapes academic novelty.
Humanities and Social Sciences Communications, 12(1):1–13, 2025.
[28] Robert Kirk, Ishita Mediratta, Christoforos Nalmpantis, Jelena Luketina, Eric Hambro, Edward
Grefenstette, and Roberta Raileanu. Understanding the effects of RLHF on LLM generalisation
and diversity.arXiv preprint arXiv:2310.06452, 2023.
[29] Harsh Kumar, Jonathan Vincentius, Ewan Jordan, and Ashton Anderson. Human creativity in the
age of LLMs: Randomized experiments on divergent and convergent thinking. InProceedings
of the 2025 CHI Conference on Human Factors in Computing Systems, pages 1–18, 2025.
[30] Tianjian Li, Yiming Zhang, Ping Yu, Swarnadeep Saha, Daniel Khashabi, Jason Weston, Jack
Lanchantin, and Tianlu Wang. Jointly reinforcing diversity and quality in language model
generations.arXiv preprint arXiv:2509.02534, 2025.
[31] Yen-Ting Lin and Yun-Nung Chen. LLM-Eval: Unified multi-dimensional automatic evaluation
for open-domain conversations with Large Language Models. InProceedings of the 5th
Workshop on NLP for Conversational AI (NLP4ConvAI 2023), pages 47–58, 2023.
[32] Yi-Cheng Lin, Kang-Chieh Chen, Zhe-Yan Li, Tzu-Heng Wu, Tzu-Hsuan Wu, Kuan-Yu Chen,
Hung-yi Lee, and Yun-Nung Chen. Creativity in LLM-based multi-agent systems: A survey. In
Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pages 27572–27595, 2025.
[33] Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide Xia, Graham Neubig, Pengchuan Zhang,
and Deva Ramanan. Evaluating text-to-visual generation with image-to-text generation. In
European Conference on Computer Vision, pages 366–384. Springer, 2024.
[34] Ximing Lu, Melanie Sclar, Skyler Hallinan, Niloofar Mireshghallah, Jiacheng Liu, Seungju Han,
Allyson Ettinger, Liwei Jiang, Khyathi Chandu, Nouha Dziri, et al. AI as humanity’s Salieri:
Quantifying linguistic creativity of language models via systematic attribution of machine text
against web text.arXiv preprint arXiv:2410.04265, 2024.
27

[35] Minh Nhat Nguyen, Andrew Baker, Clement Neo, Allen Roush, Andreas Kirsch, and Ravid
Shwartz-Ziv. Turning up the heat: Min-p sampling for creative and coherent LLM outputs.
arXiv preprint arXiv:2407.01082, 2024.
[36] Jay A Olson, Johnny Nahas, Denis Chmoulevitch, Simon J Cropper, and Margaret E Webb.
Naming unrelated words predicts creativity.Proceedings of the National Academy of Sciences,
118(25):e2022340118, 2021.
[37] Peter Organisciak, Selcuk Acar, Denis Dumas, and Kelly Berthiaume. Beyond semantic
distance: Automated scoring of divergent thinking greatly improves with Large Language
Models.Thinking Skills and Creativity, 49:101356, 2023.
[38] Peter Organisciak and Denis Dumas. Open creativity scoring. https://openscoring.du.
edu, 2020. [Computer software].
[39] Ziliang Qiu and Renfen Hu. Deep associations, high creativity: A simple yet effective metric
for evaluating Large Language Models. InProceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing, pages 10870–10883, 2025.
[40] Roni Reiter-Palmon, Boris Forthmann, and Baptiste Barbot. Scoring divergent thinking tests: A
review and systematic framework.Psychology of Aesthetics, Creativity, and the Arts, 13(2):144,
2019.
[41] Mark A Runco and Garrett J Jaeger. The standard definition of creativity.Creativity Research
Journal, 24(1):92–96, 2012.
[42] Mark A Runco and Wayne Mraz. Scoring divergent thinking tests using total ideational output
and a creativity index.Educational and Psychological Measurement, 52(1):213–221, 1992.
[43] Alexander Shypula, Shuo Li, Botong Zhang, Vishakh Padmakumar, Kayo Yin, and Osbert
Bastani. Evaluating the diversity and quality of LLM generated content.arXiv preprint
arXiv:2504.12522, 2025.
[44] Brandon Smith, Mohamed Reda Bouadjenek, Tahsin Alamgir Kheya, Phillip Dawson, and Sunil
Aryal. A comprehensive analysis of Large Language Model outputs: Similarity, diversity, and
bias.arXiv preprint arXiv:2505.09056, 2025.
[45] Allan Snyder, John Mitchell, Terry Bossomaier, and Gerry Pallier. The Creativity Quotient: An
objective scoring of ideational fluency.Creativity Research Journal, 16(4):415–419, 2004.
[46] Christopher J Soto and Oliver P John. Short and extra-short forms of the Big Five Inventory–2:
The BFI-2-S and BFI-2-XS.Journal of Research in Personality, 68:69–81, 2017.
[47] Zhivar Sourati, Alireza S Ziabari, and Morteza Dehghani. The homogenizing effect of Large
Language Models on human expression and thought.Trends in Cognitive Sciences, 2026.
[48] C. Stevenson, I. Smal, M. Baas, M. Dahrendorf, R. Grasman, C. Tanis, E. Scheurs, D. Sleiffer,
and H. van der Maas. Automated AUT scoring using a big data variant of the consensual
assessment technique. Report Final Technical Report, Modeling Creativity Project, Universiteit
van Amsterdam, Amsterdam, July 2020. Faculty of Social and Behavioural Sciences (FMG),
Psychology Research Institute (PsyRes).
[49] E Paul Torrance. Nurture of creative talents.Theory Into Practice, 5(4):167–173, 1966.
[50] Yun Wan and Yoram M Kalman. Diverse AI personas can mitigate the homogenization effect
in human-AI collaborative ideation.Computers in Human Behavior: Artificial Humans, page
100289, 2026.
[51] Emily Wenger and Yoed Kenett. We’re different, we’re the same: Creative homogeneity across
LLMs.arXiv preprint arXiv:2501.19361, 2025.
[52] Weijia Xu, Nebojsa Jojic, Sudha Rao, Chris Brockett, and Bill Dolan. Echoes in AI: Quantifying
lack of plot diversity in LLM outputs.Proceedings of the National Academy of Sciences,
122(35):e2504966122, 2025.
28

[53] Longfei Yun, Chenyang An, Zilong Wang, Letian Peng, and Jingbo Shang. The price of format:
Diversity collapse in LLMs.arXiv preprint arXiv:2505.18949, 2025.
[54] Yiming Zhang, Harshita Diddee, Susan Holm, Hanchen Liu, Xinyue Liu, Vinay Samuel, Barry
Wang, and Daphne Ippolito. NoveltyBench: Evaluating language models for humanlike diversity.
arXiv preprint arXiv:2504.05228, 2025.
29
