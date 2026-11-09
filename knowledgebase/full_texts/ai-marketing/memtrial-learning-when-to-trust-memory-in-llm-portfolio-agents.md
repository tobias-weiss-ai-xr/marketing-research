---
title: 'MemTrial: Learning When to Trust Memory in LLM Portfolio Agents'
url: https://arxiv.org/abs/2610.11732
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Guanghao Wu
- Zhuo Cai
- Shoujin Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.11732
pages: 33
chars: 180688
fetched_at: '2026-11-08T13:23:47+00:00'
kb_version: 1
---

# MemTrial: Learning When to Trust Memory in LLM Portfolio Agents

MemTrial: Learning When to Trust Memory
in LLM Portfolio Agents
Guanghao Wu∗, Zhuo Cai∗, Shoujin Wang†
University of Technology Sydney
Abstract
Large language model (LLM) agents for portfolio management learn
from experience: they credit each experience in their memory with
the outcome of the decisions that used it. In financial markets,
however, this outcome mostly reflects the market move shared by
all decisions on that date, so the credit tracks the market rather
than the experience, and these agents often do worse than simply
holding the equal-weight (1/𝑁 ) portfolio. We ask how an agent
can measure what an experience changes, and answer by putting
memory on trial: drafts of the same decision with and without an
experience face the same market, so the outcome they share can-
cels in their difference. Our agent, MemTrial, generates eight drafts
of each decision with subsets of its retrieved experiences chosen
by a fractional factorial design, and estimates each experience’s
contribution as its Banzhaf value, the average of these differences.
As each date occurs once and each draft is a noisy LLM sample,
these contributions are noisy and may not hold on unseen dates.
MemTrial therefore pools them into values across dates and sim-
ilar experiences with a hierarchical Bayesian model, acts on the
values only after they have predicted unseen dates, and otherwise
stays anchored at a conservative reference such as 1/𝑁 . On four
benchmarks, it not only benefits from experiences that matter (the
best of 15 methods on a semi-synthetic benchmark with known
experience quality) but also, through its anchor, limits its losses
when its values do not hold (at most 2.2% below 1/𝑁 on PortBench
and InvestorBench, against 15–38% for the best experience-learning
agent). Averaged over five benchmark settings, its utility is 21.2%
higher than that of the best experience-learning agent, and with
eight LLMs it beats every LLM-based baseline on InvestorBench.
Our code is available here.
Keywords
LLM agents; agent memory; experience learning; credit assignment;
counterfactual attribution; portfolio management
1 Introduction
LLM agents are increasingly used to manage investment portfo-
lios [34, 54, 57]. To improve with use, they learn from experience:
when the outcome of a decision is known, the agent writes an
experience, such as a short lesson, into its memory, and at later
dates it retrieves the most relevant experiences and conditions its
decision on them [45, 59]. Which experiences it comes to rely on is
decided byoutcome credit, in one of two ways: an experience used
in a decision that turned out well gains importance or value [54, 56],
or lessons are distilled from episodes judged by their outcomes to
be successes or failures [45, 59].
∗Both authors contributed equally to this research.
†Corresponding author.
(a) Existing agents: credit the whole outcome
Retrieve Outcome Credit all Always act
ƥ u
b Ƥ
market
mostly market
ƥ
+
u
+
b
+
Ƥ
+
values track the market
!
no check before use
(b) MemTrial: put memory on trial
P Same date Shared move cancels Trust test Act
ƥ
with h
without h − = Δ
Δ = what h changes
pool
dates Ǒ
do values
predict
unseen dates?
¬ yes: act on values
ň no: stay near 1/N
Figure 1:(a) Existing agents credit experiences with market-driven
outcomes and always use these credits. (b) MemTrial measures what
each experience changes on the same date and acts on its values only
after they have predicted unseen dates; otherwise it stays near 1/ 𝑁 .
In portfolio management, this rule has a blind spot. The outcome
of a decision is dominated by the market move over the holding
period, and every decision made on that date shares this move. An
experience retrieved before a rally is credited with the rally, and
one retrieved before a sell-off is blamed for it, much as a treatment
effect estimated without a control group mixes the treatment with
everything else that happened (Figure 1a). Table 1 measures this on
three real benchmarks (§4.1), using the utility of the equal-weight
(1/𝑁 ) portfolio over the same holding period as a proxy for the
market. On every date, we generate a draft with each subset of
the four retrieved experiences and compare two measures for each
experience: its outcome credit, the mean utility of the drafts that
used it, and its counterfactual contribution, the mean utility of
these drafts minus that of the drafts without it. Outcome credit
rises and falls with the market almost in lockstep, but is nearly
unrelated to the contribution of the experience, which itself is
unrelated to the market. As each experience is in half of the drafts,
its outcome credit is the date’s mean utility plus half its contribution,
and the first term dominates. Agents that accumulate outcome
credit therefore rank experiences by the markets in which they
were retrieved. Accordingly, every experience-learning agent we
test underperforms 1/𝑁 on PortBench and InvestorBench (Table 3).
Data valuation offers a remedy: it values a data point by its
marginal contribution to a utility, averaged over subsets of the
other points [18, 50]. Applying it to LLM portfolio agents raises
two challenges (CHs).
CH1: How can an agent measure what an experience
changes when every measurement is a costly, noisy LLM
call on a market date that never comes back?Data valuation
evaluates a utility many times on a fixed dataset. For an LLM agent,
1
arXiv:2610.11732v2  [cs.AI]  11 Oct 2026

Wu, Cai and Wang
every evaluation is a paid call whose output varies from sample
to sample, and every decision date is a single market episode. A
contribution measured on one date is therefore mostly noise: on
PortBench, the retrieved experiences change the agent’s utility
detectably on only 2–4 of 56 months, about as often as chance
alone would produce (Table 1).
Table 1:Outcome credit tracks the market, not the experience.
Spearman correlation (𝜌)
Benchmark Outcome credit vs. 1/𝑁 Contribution vs. 1/𝑁 Outcome credit vs. contribution Dates with a detectable effect
PortBench-Full+0.91±0.00+0.04±0.03+0.11±0.063–4 / 56
PortBench-Raw+0.92±0.00+0.03±0.04+0.04±0.032–4 / 56
InvestorBench+0.95±0.00−0.07±0.02−0.03±0.02126–127 / 149
ClassAlloc+0.97±0.00+0.02±0.07+0.02±0.0753–57 / 71
CH2: How can an agent tell whether a learned value will
hold on dates it has not seen?Even where experiences clearly
change the decision, as on about 85% of InvestorBench days, the
contributions learned from past days do not predict those of the
following days (§4.2), and selecting experiences by their average
past contribution still trails 1/𝑁 (Table 3). Existing agents always
act on their learned scores: they have no notion of insufficient
evidence and no fallback for when their scores do not hold.
To address these challenges, we presentMemTrial(memory
on trial), an experience-learning agent that learns when to trust
its memory through a closed loop of four steps (Figures 1b and 2).
(1)Counterfactual attribution: on every date, the agent generates
eight drafts of its decision with combinations of its four retrieved
experiences chosen by a fractional factorial design [6], and estimates
the contribution of each experience as its Banzhaf value [3, 50], the
average difference between the drafts with and without it. Because
all drafts face the same market, the outcome they share cancels.
(2)Value estimation: as in small-area estimation [ 15], a hierarchical
Bayesian model pools these noisy contributions into values across
dates and across experiences with similar content. (3)Trust test:
following prequential analysis [10], the agent scores its predicted
values against the contributions measured once the outcome is
known, and trusts its values only when these out-of-sample forward
scores are significantly positive. (4)Anchored action: if the values are
trusted, the agent deploys the draft with the highest predicted value;
otherwise it deploys a blend of its drafts anchored at a conservative
reference, such as 1/𝑁 , and learns online how far to move from it.
Steps (1)–(2) address CH1, and steps (3)–(4) address CH2.
We evaluate MemTrial on three real benchmarks, PortBench, In-
vestorBench and ClassAlloc, and on PlantedMem, a semi-synthetic
environment with real prices and real LLM drafts in which the qual-
ity of every experience is known.Our contributions are: (i)we
show that outcome credit, the credit rule of existing experience-
learning agents, tracks the market rather than what an experience
changes;(ii)we propose MemTrial, a closed learning loop that
learns what each experience is worth and when this knowledge
can be trusted;(iii)against 14 baselines on four benchmarks and
with eight LLMs, MemTrial is the best method when experiences
matter and stays close to 1/𝑁 when its values do not hold, where
existing experience-learning agents fall behind. Appendices A–H
follow the references.
2 Related Work
LLM agents for financial decision making.LLM agents now
trade single assets and allocate across many. FinMem [54] ranks
memories by recency, relevance and an importance that trading
feedback reinforces; FinCon [55] updates the investment beliefs of
a team of agents by verbal reinforcement from realized profit and
loss; FinAgent [57] and CryptoTrade [35] reflect on past trades; and
TradingAgents [52] simulates the roles of a trading firm. Investor-
Bench [34] and PortBench [ 60] evaluate such agents on stocks,
cryptocurrencies and multi-asset portfolios. These agents judge a
memory, reflection or strategy by the outcome of the trades that
used it, which the market move dominates, and none of them checks
whether what it has learned holds on later dates.
Experience learning and memory in LLM agents.Outside
finance, Reflexion [45] turns feedback on failed attempts into verbal
reflections, ExpeL [59] distils insights from successful and failed
trajectories, Voyager [49] keeps a library of skills that it reuses when
they succeed, and Generative Agents [41], MemoryBank [61] and
MemGPT [40] decide which memories to retrieve, keep or forget
by recency, importance and relevance. MemRL [56] learns a value
for each memory from the rewards of the episodes that used it, and
retrieval-augmented generation [32] retrieves by similarity alone.
These methods credit outcomes to the memories involved or distil
lessons from successes and failures, and never test whether what
they learn holds later. This works when outcomes reflect the agent’s
own choices, as in games, coding or multi-agent environments, but
not when a shock shared by all decisions dominates them.
Counterfactual credit and data valuation.Data Shapley [ 18,
23], Beta Shapley [29] and Data Banzhaf [50] value a training point
by its averaged marginal contributions to a model’s performance,
and Data Banzhaf is the most robust of them when the utility is
noisy. Influence functions [26] approximate the effect of removing a
point. Uplift modelling [21] and counterfactual learning from logged
decisions [5, 46] estimate the effect of an action from observational
data. These methods value data for a fixed model and test set, or
estimate effects from logs in which, in our setting, the market and
the choice of memory are confounded. None of them measures
what a memory changes in an LLM’s decisions, or asks whether
values learned on past dates predict future ones.
Safe deployment and portfolio choice under estimation er-
ror.Safe policy improvement deploys a learned policy only when it
beats a baseline with high confidence [30, 47], and prequential anal-
ysis [10] judges a model by its sequential out-of-sample predictions.
In portfolio choice, estimation error makes optimized portfolios
hard to trust: none of those evaluated by DeMiguel et al. [12] consis-
tently beats 1/𝑁 out of sample, which motivates shrinkage towards
conservative targets [24, 31, 48]. MemTrial brings these ideas to
the memory of LLM agents: a trust test on forward scores decides
whether its learned values are trusted, and until then an anchored
blend learns online how far to move from a conservative reference.
What is new in MemTrial is not the Banzhaf value [3] but how
it is measured and used: on LLM decisions through a designed
experiment on each date, pooled into a value model, and trusted
2

MemTrial: Learning When to Trust Memory
only after this model has predicted unseen dates. Please refer to
Appendix A for more related work.
3 MemTrial: Learning When to Trust Memory
3.1 Problem Formulation and Overview
Portfolio decisions under an investor mandate.An agent man-
ages a portfolio of𝑁assets and cash for an investor. At each deci-
sion date𝑡= 1,...,𝑇 , it observes the market state𝑠𝑡 and outputs
portfolio weights𝑥𝑡 , which are held over a holding period. A pro-
jection𝑃𝜃 enforces the investor’s mandate, a cap𝑀 on the share
of risky assets and a floor𝑚 on the share of defensive assets; the
investor profile𝜃=(𝑀,𝑚,𝛾) also contains the risk aversion𝛾. A
decision is scored by the investor utility of the executed portfolio,
a certainty-equivalent (CEQ) return [12],
𝑢𝑡(𝑥)=𝑟 𝑡
𝑃𝜃(𝑥)−𝛾 2𝑉𝑡 𝑃𝜃(𝑥),(1)
where𝑟𝑡 is the realized return over the holding period net of pro-
portional trading costs and𝑉𝑡 is the variance of daily returns times
the number of days in that period (for one day, the squared return).
An LLM agent with an experience memory.The agent is
an LLM policy𝜋 that maps the state and a set of experiences𝑆 to
weights,𝑥∼𝜋(·|𝑠 𝑡,𝑆) . Its memory holds experiences written once
the outcomes of earlier decisions were known: lessons, or records of
earlier decisions and their outcomes. At date𝑡, the retriever returns
the𝑘= 4experiences whose embeddings are most similar to that of
the current state,𝑅𝑡 =(ℎ 𝑡,1,...,ℎ 𝑡,𝑘). Because the LLM samples at a
positive temperature, the same prompt yields different weights; we
call each sample adraft. Experience learning selects which retrieved
experiences enter the prompt,𝑆𝑡⊆𝑅 𝑡 , based on scores learned from
earlier dates. Existing agents credit an experience used at date 𝑡
with𝑢𝑡(𝑥𝑡), the utility of the whole decision [54, 56], which Table 1
shows mostly measures the market.
Our goal and the MemTrial loop.We aim to maximize the
investor’s cumulative utility ˝ 𝑡𝑢𝑡(𝑥𝑡) by learning what each expe-
rience is worth, from what it changes in decisions, and when this
knowledge can be trusted. Figure 2 shows the loop (Algorithm F.1
in Appendix F gives its pseudocode). Before the outcome of date𝑡 is
known, MemTrial generates drafts with designed subsets of𝑅𝑡 and
acts (§3.5) according to the trust test (§3.4). After the outcome is
known, it attributes the change in utility to each experience (§3.2),
updates the values (§3.3) and scores their predictions (§3.4).
3.2 Counterfactual Attribution: What Does an
Experience Change?
Designed drafts.To know what an experience changes, MemTrial
compares decisions made on the same date with and without it,
as in a controlled experiment: both face the same market path,
so the outcome they share cancels in their difference. Comparing
every subset of𝑘 experiences would need2𝑘 drafts, 16 for𝑘= 4. A
fractional factorial design [6] measures the effect of each experience
with half as many drafts: the half fraction
D={𝑆⊆𝑅 𝑡 :|𝑆|is even},(2)
a2 4−1 design of resolution IV. Its eight subsets include the empty
and the full set, every experience appears in half of them and every
pair in two, so the effect of one experience is not aliased (mixed)
with any interaction between two others (Appendix C.1).
Contribution as an estimated Banzhaf value.Let 𝑈𝑡(𝑆)=
𝑢𝑡(𝑥𝑆 𝑡) be the utility that the draft made with subset𝑆 would have
earned at realized prices (the agent is a price taker). The counter-
factual contribution of the𝑗-th retrieved experience is
𝑐𝑡,𝑗 =mean{𝑈 𝑡(𝑆):𝑆∈D, 𝑗∈𝑆}
−mean{𝑈𝑡(𝑆):𝑆∈D, 𝑗∉𝑆}, (3)
the main effect of experience 𝑗 in the2 4−1 design. Over all 16
subsets, the main effect is the Banzhaf value [3] of 𝑗 in the game
𝑈𝑡 ; in the half fraction, it is aliased with the interaction of the
other three experiences, which adds 13–17% to its noise variance on
the benchmarks where all 16 subsets were drafted (Appendix C.1).
The Banzhaf value weights every context of the other experiences
equally, which makes it the most robust semivalue under noisy
utilities [50], as for sampled LLM outputs. Any utility shared by
all drafts of date 𝑡 cancels in𝑐𝑡,𝑗 , and the market move enters it
only through the weights that experience 𝑗 changes. Since𝑈𝑡 is
evaluated after the mandate projection, a change that the mandate
removes contributes nothing. On the design, the outcome credit
of 𝑗, the mean utility of the drafts that used it, equals ¯𝑈𝑡+𝑐𝑡,𝑗/2,
where ¯𝑈𝑡 , the mean utility of the eight drafts, follows the market
(Table 1). Finally, we centre the contributions within each date,
𝑦𝑡,𝑗 =𝑐𝑡,𝑗− 1 𝑘 𝑘∑︁ 𝑗′=1 𝑐𝑡,𝑗′,(4)
which removes what all retrieved experiences do in common on
that date and keeps what distinguishes them.
3.3 Value Estimation: Pooling Noisy Evidence
Hierarchical value model.A contribution measured on a single
date is mostly noise, and a new experience has no measurements at
all. Small-area estimation faces the same problem when it estimates
the income of a small town from a few survey responses, and solves
it by borrowing strength from similar towns [ 15]. Let 𝑛ℎ be the
number of dates with a realized outcome on which experience ℎ
was retrieved and𝑚ℎ the mean of its centred contributions. The
value model is
𝑚ℎ =𝑣ℎ+𝜀ℎ, 𝜀 ℎ∼N(0, 𝜎 2/𝑛ℎ),
𝑣ℎ =𝑧⊤ ℎ𝛽+𝑏 ℎ, 𝛽∼N(0, 𝜎 2 𝛽𝐼), 𝑏 ℎ∼N(0,𝜏 2), (5)
where𝑣ℎ is the value of experience ℎ,𝑧ℎ∈R 𝑑 a content feature
(the first𝑑= 8standardized principal components of its retrieval
embedding),𝛽 maps content to value, and 𝑏ℎ is the experience’s
own deviation. This is the Fay–Herriot model with content as the
covariate, or a Gaussian process with a kernel linear in content plus
an identity term [42]. The noise variance𝜎2 is estimated from the
spread of each experience’s contributions, and(𝜎 2 𝛽,𝜏 2) maximize
the marginal likelihood
log𝑝(𝑚|𝜎 2 𝛽,𝜏 2)=logN(𝑚; 0, 𝐾),
𝐾=𝜎 2 𝛽𝑍𝑍⊤+𝜏 2𝐼+𝜎 2 diag(1/𝑛ℎ), (6)
over a grid. The posterior means are
ˆ𝑣=(𝜎 2 𝛽𝑍𝑍⊤+𝜏 2𝐼)𝐾 −1𝑚, ˆ𝛽=𝜎 2 𝛽𝑍⊤𝐾−1𝑚,(7)
3

Wu, Cai and Wang
Act · before outcome
Learn · after outcome
State + memory
4 experiences
8 subsets → 8 drafts
Each in 4/8 drafts
Trust test
No
Best draft
Anchored blend
1/N + drafts
Execute
& holdYes
Forward scores
ρ
Earlier values
Bayesian values
…
Pool dates + content
− +
− −
− +
− −
Next date
Values
Past scores
Same date · shared move cancels
Predicted
unseen dates?
Outcome realized
Banzhaf contribution
New contributions
Figure 2:One decision date of MemTrial. Before the outcome, it acts on its learned values only if they have predicted unseen dates; after the
outcome, it updates the values and scores their predictions. Contributions compare drafts of one date, so their shared market move cancels.
so an experience with few measurements is shrunk towards the
value predicted from its content, and a new one receives ˆ𝑣ℎ =𝑧⊤ ℎ ˆ𝛽
before it is ever used.
Learner selection.Content may or may not predict value, so
MemTrial keeps two learners, the content-aware model (5) and a
per-experience model with 𝜎2 𝛽 = 0. It scores both forward (§3.4)
and uses the one with the higher mean forward score once both
have at least 10 scores (before that, the per-experience model).
3.4 Trust Test: Has the Learned Value Predicted
the Future?
Forward scores.A weather forecaster is judged by how well she
predicted tomorrow’s weather, not by how well her model fits
yesterday’s, and prequential analysis judges a statistical model in
the same way [ 10]. Before date 𝑡, each learner is fitted only on
dates whose outcomes are known and predicts the values ˆ𝑣𝑡,𝑗 of
the experiences retrieved at 𝑡. Once the outcome is known, the
prediction is scored against the measured centred contributions,
𝜌𝑡 =corr ( ˆ𝑣𝑡,1,..., ˆ𝑣𝑡,𝑘),(𝑦 𝑡,1,...,𝑦 𝑡,𝑘),(8)
the Pearson correlation across the retrieved experiences, which is
out of sample by construction.
Trust test.Let 𝜌1,...,𝜌 𝑛 be the forward scores of the selected
learner available at date𝑡, with mean ¯𝜌 and standard deviation𝑠𝜌.
As in safe policy improvement [47], MemTrial trusts its values only
on strong evidence: when𝑛≥10and
𝑝𝑡 =Pr

𝑇𝑛−1≥ ¯𝜌 𝑠𝜌/√𝑛
!
<𝛼,(9)
where𝑇𝑛−1 follows a Student 𝑡 distribution with 𝑛− 1degrees
of freedom and 𝛼= 0.05. Trust thus means that the values have
ranked the retrieved experiences better than chance on unseen
dates; used as a decision rule on every date, the test rarely passes
where experiences carry no signal (§4.5). When trusted, MemTrial
deploys the designed draft with the highest total predicted value,
𝑆∗ 𝑡 =arg max
𝑆∈D
∑︁
𝑗∈𝑆
ˆ𝑣𝑡,𝑗,(10)
with ties broken towards fewer experiences, provided that this total
is positive, i.e., that the subset’s experiences are predicted to beat
the average retrieved one; §4.5 measures whether trusted drafts beat
the anchored blend. This draft was already generated for Eq. (3), so
trusting costs no extra LLM call. The test asks whether the values
have predicted the future, not whether experiences differed in the
past (§4.3 compares the two).
3.5 Anchored Action: What to Do Until Memory
Can Be Trusted
Anchored blend.The 1/ 𝑁 portfolio is hard to beat out of
sample [12], and combining it with a more ambitious strategy,
weighted by how strongly the data support the latter, can improve
on both [48]. MemTrial applies this idea online. When its values are
not trusted, it deploys a blend of a conservative reference𝑥ref (on
the real benchmarks, the 1/𝑁 portfolio projected to the mandate)
and the average draft ¯𝑥𝑡 = 1 |D| ˝ 𝑆∈D 𝑥𝑆 𝑡 ,
𝑥𝑡(𝑞)=𝑞𝑥 ref 𝑡 +(1−𝑞) ¯𝑥𝑡,
𝑞𝑡 =arg max
𝑞∈[0,1]
1
𝑛
∑︁
𝑠<𝑡
𝑢𝑠
𝑥𝑠(𝑞)−𝜆𝑛 KL(𝑞∥𝛼 0), 𝜆 𝑛 = 𝜆0 ˆ𝜎𝑛√𝑛 ,
(11)
where KL(𝑞∥𝛼 0) is the Kullback–Leibler divergence between
Bernoulli distributions,𝛼0 = 0.9is the prior weight on the refer-
ence,𝜆0 = 4,𝑛 is the number of dates with a realized outcome,
and ˆ𝜎𝑛, half the mean absolute utility gap between the reference
and the average draft, makes the regularizer unit-free. This is
4

MemTrial: Learning When to Trust Memory
follow-the-regularized-leader [43] with a regularizer centred at
the prior: with little evidence, 𝑞𝑡 stays close to 𝛼0; as evidence
accumulates, the regularization weakens as1/√𝑛 and𝑞𝑡 follows
the blend that performed best on these dates.
3.6 The Closed Loop and Its Cost
The same eight drafts serve every step: they yield the contribu-
tions (3), the trusted action (10) and the average draft in (11). Mem-
Trial therefore makes|D|= 8drafts per decision, which run in
parallel; its LLM cost is eight times that of a single-draft agent.
Fitting the value model costs 𝑂(𝐺·𝐻 3) for𝐺 grid points and 𝐻
experiences, a few milliseconds per decision (Appendix D.3).
4 Experiments
4.1 Experimental Setup
Table 2:Three real benchmarks and one semi-synthetic benchmark
with planted experiences of known quality.
PortBench InvestorBench ClassAlloc PlantedMem
Assets 99 (6 classes) 4 stocks, cash 5 classes 4 classes
Decisions monthly daily monthly monthly
Development 2019–22 none none 15 worlds
Test dates 20 (2023–24) 149 (10/20–05/21) 71 (05/20–03/26) 120 / world
Experiences 338 decisions 63 lessons 58 lessons 12/48 planted
Seeds 3 3 3 100 worlds
Benchmarks.Table 2 summarizes the four benchmarks, and
Appendix D.3 gives their construction. OnPortBench[ 60], each
decision starts from the equal-weight portfolio, holds for 20 trading
days and pays 15 bp on the amount traded. PortBench’s native
prompt shows prices for only eight of its 99 assets: PortBench-Raw
keeps this prompt, and PortBench-Full shows every eligible asset;
the prompts of the other benchmarks show every asset. OnInvestor-
Bench[ 34], the agent also reads daily news and writes its lessons
during a warm-up from July to September 2020.ClassAlloctests
agents after the LLM’s knowledge cutoff: built from PortBench’s
prices, it ends 21 months after that of gpt-4.1-mini [38] (June 2024),
carries holdings from month to month, and gives every learner an
outcome only after its 20 trading days. Experiences are retrieved
by embedding similarity, with Qwen3-Embedding-0.6B [ 58] on
PortBench and text-embedding-3-small [37] on InvestorBench and
ClassAlloc.PlantedMemkeeps real prices and real LLM drafts but
plants twelve experiences of known quality: three useful, six neu-
tral and three misleading. A useful (misleading) experience moves
a share𝛽 of the draft to an asset class, with probability 0.7 the one
that does best (worst) next (Appendix D.3). Retrieval depends on
the market regime, which reproduces the market confound. Five
core regimes vary how strongly experiences move a draft (no in-
fluence, noise only, and𝛽∈{ 0.1, 0.25, 0.5}), and two more have 48
experiences whose content is uninformative (many experiences) or
informative (informative content) about their quality.
Investors and metric.We use PortBench’s conservative (𝑀=
0.40,𝑚= 0.40,𝛾= 10), balanced (𝑀= 0.65,𝑚= 0.20,𝛾= 5) and
aggressive (𝑀= 0.90,𝑚= 0.05,𝛾= 2) investors. We report the
utility (1) per decision period, averaged over dates and investors,
in % per month (bp per day on InvestorBench); higher is better.
Baselines(Appendix D.2). (i) Rule-based: 1/ 𝑁 projected to
the mandate [ 12] and Minimum variance [ 36]. (ii) LLM agents
without experience learning: Memory-free (zero-shot) [ 7], Self-
consistency [51] (the average of three memory-free drafts) and
Similarity retrieval [32] of the two or four most similar experiences.
(iii) Experience-learning agents: FinMem [54], MemRL [56], Reflex-
ion [45] and ExpeL [59]. (iv) Credit-based and ensemble learners:
Uplift credit [21], which regresses outcomes on experience usage
with a market control; Counterfactual selection, which selects
experiences by our contributions (3) without value estimation
or trust test; Draft averaging [ 4], which deploys the average of
MemTrial’s eight drafts; and Hedge [16] over 1/𝑁 and the memory
configurations. Where a baseline’s own module cannot run, we
re-implement its memory-scoring rule (marked†); on PortBench,
ExpeL†votes over the experiences, and the FinMem and MemRL
modules receive no feedback after July 2019 (Appendix D.2).
Implementation and statistics.All LLM agents use gpt-4.1-
mini (2025-04-14) at temperature 0.7, which gives the distinct drafts
that MemTrial, Self-consistency and Draft averaging need. Mem-
Trial uses𝑘= 4, the design (2),𝑑= 8,𝛼= 0.05with at least 10
forward scores, 𝛼0 = 0.9and 𝜆0 = 4. Its reference is 1/𝑁 on the
real benchmarks and the average of eight memory-free drafts in
PlantedMem, where 1/𝑁 ignores the risk aversion. It was frozen
before any InvestorBench decision, so InvestorBench, ClassAlloc
and the runs with other LLMs are held-out tests. On the real bench-
marks, each of three seeds is an independent deployment in which
every draft is sampled anew; PlantedMem uses 100 test seeds, each
a new world. Tables report the mean ± sd over seeds, with the
best result inboldand the second best underlined.Improv.is the
gain of MemTrial over the best experience-learning agent of each
setting, in percent of that agent’s utility, and * marks a significant
improvement (𝑝< 0.05, one-sided paired𝑡-test over test dates, or
over seeds in PlantedMem). Thetrust rateis the share of decisions
on which MemTrial acts on its learned values. Appendix D.3 gives
further implementation details and Appendix G the prompts.
4.2 Main Results
Overall performance.Table 3 (PlantedMem: mean of the five
core regimes) shows that MemTrial is the best of all 15 methods in
PlantedMem and the best LLM-based method on PortBench and
InvestorBench. Averaged over the five settings, its utility is 21.2%
higher than that of the best experience-learning agent. In Planted-
Mem, where experiences carry real signal, the gain is 0.10 pp per
month. On PortBench and InvestorBench, no LLM-based method
beats 1/𝑁 : the LLM’s drafts fail to outperform equal weighting, and
their frequent reallocation costs fees and adds risk (Appendix D.4).
MemTrial is the only LLM-based method that stays close to 1/𝑁
there, at most 2.2% below it, whereas the best existing experience-
learning agent falls 15–38% behind. On PortBench-Full, the lead
of 1/𝑁 and MemTrial depends on the last test month (November
2024), in which cryptocurrencies rose by 129%: without it, Simi-
larity retrieval (top-4) and Hedge come out slightly ahead of both
(Appendix D.6). On ClassAlloc, the memory-free LLM beats 1/𝑁 ,
but no form of memory improves on it (Appendix D.11); §4.5 shows
that this advantage lies in the months before the LLM’s knowledge
cutoff (June 2024).
5

Wu, Cai and Wang
Table 3:Main results: utility per decision period (higher is better). MemTrial is the best LLM-based method on PortBench and InvestorBench,
where it stays within 2.2% of 1/𝑁, and the best method in PlantedMem.
Method PortBench-Full PortBench-Raw InvestorBench ClassAlloc PlantedMem
%/month %/month bp/day %/month %/month
Rule-based 1/𝑁[12] 2.02±0.002.02±0.0010.45±0.000.623±0.0000.57±0.00 Minimum variance [36] 0.25±0.000.25±0.005.53±0.000.230±0.000−0.04±0.00
LLM w/o
experience
learning
Memory-free [7] 1.60±0.051.07±0.028.43±0.290.657±0.001 0.76±0.08
Self-consistency [51] 1.56±0.111.17±0.037.89±0.210.686±0.0070.79±0.03
Similarity retrieval (top-2) [32] 1.43±0.191.24±0.298.67±0.190.649±0.0330.72±0.07
Similarity retrieval (top-4) [32] 1.70±0.061.05±0.028.12±0.610.643±0.0390.72±0.06
Experience-
learning
agents
FinMem [54] 1.63±0.311.26±0.148.47±0.17 † 0.594±0.017 † 0.75±0.06 †
MemRL [56] 1.58±0.291.05±0.068.90±0.39 † 0.633±0.012 † 0.74±0.08 †
Reflexion [45] 1.40±0.181.26±0.037.29±0.660.590±0.0610.78±0.06 †
ExpeL [59] 1.53±0.05 † 1.10±0.06 † 8.93±0.320.609±0.0060.77±0.06 †
Credit-based
and ensemble
learners
Uplift credit [21] 1.38±0.09 † 1.20±0.10 † 8.44±0.25 † 0.645±0.022 † 0.78±0.09 †
Counterfactual selection [50] 1.49±0.291.30±0.348.54±0.260.650±0.0330.85±0.08
Draft averaging [4] 1.62±0.051.19±0.028.69±0.090.651±0.0080.75±0.03
Hedge [16] 1.73±0.091.59±0.048.97±0.230.634±0.0080.75±0.03 †
MemTrial (ours) 1.98±0.00 2.01±0.00 10.40±0.04 0.613±0.017 0.87±0.04 *
Improv.(%) +21.3±19.3+59.0±2.6+16.4±3.2−3.2±1.4+12.6±10.1
Trust rate of MemTrial (%) 0.0±0.00.6±1.00.3±0.514.6±21.733.7±9.2
1.00
1.25
1.50
wealth
(balanced)
PortBench-Full
−5
0
5
conservative
−10
0
10
balanced
2023 2024
−10
0
10
aggressive
1.0
1.1
1.2
InvestorBench
−2
0
−5
0
Nov ’20 Feb ’21 May ’21
−5
0
1.0
1.5
2.0 LLM cutoff
ClassAlloc
−5
0
−5
0
5
2022 2024 2026
−5
0
5
wealth vs. 1/𝑁 (%)
1/𝑁 Memory-free FinMem MemRL Reflexion ExpeL MemTrial falling market (decline ≥5%)
1
Figure 3:Wealth of the balanced investor (top, start = 1) and relative to 1/𝑁 for the conservative, balanced and aggressive investors (rows 2–4).
For every investor, MemTrial stays close to 1/𝑁, while the other LLM-based methods drift away, mostly below.
Wealth over time.Figure 3 follows the wealth of the three
investors on PortBench-Full, InvestorBench and ClassAlloc (red
shading marks falling markets and the dotted line the knowledge
cutoff); on PortBench, whose decisions each start from the equal-
weight portfolio, wealth compounds their net returns. For every
investor, MemTrial tracks 1/𝑁 through rising and falling markets,
while the other LLM-based methods drift away from it, mostly
below. In Table 4, MemTrial has the best Sharpe ratio and draw-
down of the LLM-based methods on every benchmark, and the
highest return on PortBench and InvestorBench, where no LLM-
based method has a higher return than 1/𝑁 . Across all 162 runs
(both PortBench variants and eight LLMs on InvestorBench and
ClassAlloc, each with three investors and three seeds), the wealth
of MemTrial never fell more than 5% behind that of 1/𝑁 , whereas
the memory-free LLM and the experience-learning agents did so in
22–44% of their runs (Appendix D.6).
Why does MemTrial help?Three components account for this.
First, counterfactual attribution removes the market from the con-
tribution. In PlantedMem, counterfactual selection beats selection
by outcome credit (MemRL†), whereas adjusting outcome credit
for the market by regression (Uplift credit) closes only a third of
this gap. Second, the trust test keeps MemTrial from acting on
6

MemTrial: Learning When to Trust Memory
Table 4:Return and risk of the balanced investor: cumulative net return (CR), annualized Sharpe ratio (SR) and maximum drawdown (MDD).
On PortBench and InvestorBench, MemTrial is the only LLM-based method close to 1/𝑁in both return and Sharpe ratio.
PortBench-Full InvestorBench ClassAlloc
Method CR %↑SR↑MDD %↓ CR %↑SR↑MDD %↓ CR %↑SR↑MDD %↓
Rule-based 1/𝑁[12] 61.2±0.01.77±0.005.6±0.0 19.1±0.02.87±0.005.7±0.0 82.0±0.01.22±0.00 12.0±0.0 Minimum variance [36] 5.4±0.01.19±0.001.5±0.0 9.9±0.01.47±0.006.4±0.0 19.1±0.04.19±0.000.2±0.0
LLM w/o
exp. learning Memory-free [7] 48.5±0.81.47±0.067.3±1.0 14.6±0.52.24±0.086.3±0.1 88.3±1.5 1.11±0.0013.9±0.3
Experience-
learning
agents
FinMem [54] 49.6±9.21.53±0.216.2±1.4 14.7±0.42.27±0.036.1±0.1 75.4±2.61.07±0.0315.4±0.5
MemRL [56] 47.7±11.11.45±0.196.9±1.1 15.4±0.72.33±0.096.1±0.3 84.0±1.21.06±0.0315.4±1.1
Reflexion [45] 41.8±6.11.41±0.147.2±1.4 12.9±1.01.97±0.146.3±0.1 80.6±8.31.10±0.0815.1±1.8
ExpeL [59] 54.6±3.31.61±0.216.8±1.1 15.5±0.52.43±0.075.8±0.1 83.2±0.41.04±0.0116.9±0.3
Credit /
ensemble
Counterfactual selection [50] 46.9±8.91.44±0.156.1±1.1 14.8±0.52.29±0.076.0±0.0 88.6±5.11.10±0.0414.0±1.2
Hedge [16] 51.3±3.21.64±0.07 5.6±0.3 15.8±0.32.43±0.056.0±0.0 83.9±1.61.10±0.0114.2±0.1
MemTrial (ours) 59.6±0.1 1.77±0.01 5.5±0.0 19.0±0.1 2.86±0.02 5.7±0.0 79.9±5.1 1.14±0.10 13.1±1.5
Full Raw
Investor-
Bench
Class-
Alloc
no
signal signal
inform.
content
per-experience learner
content-aware learner
in-sample F-test
none (always act)
never passes
draft average (𝑞=0)
uniform prior (𝛼0=0.5)
no online learning
= −0.01 = = +0.2 −0.3 −5.3
= −3.4 = = +0.1 −0.3 +0.5
= −0.01 −0.3 +2.6 +0.2 −0.8 −5.6
−4.2 −11.8 −4.7 −0.1 −2.3 +0.9 +2.4
= −0.01 −0.3 +2.6 +0.4 −15.4 −8.5
−18.3 −40.7 −16.4 +5.8 −4.8 −2.9 −2.9
−7.3 −4.6 −6.6 +3.2 −1.0 −0.8 −0.8
+0.9 −3.1 −0.1 +0.1 −0.1 −0.1 −0.05
valuestestanchor
PortBench PlantedMem
1
Figure 4:Ablation: change in utility when one step of MemTrial
is changed (%, mean over seeds; =: same actions; bold: 𝑝< 0.05). On
real markets, the anchor and the trust test matter most; with signal,
acting on the learned values does.
values that do not carry over to unseen dates. On PortBench and
InvestorBench, the values learned from past dates did not predict
the following dates, so the test almost never passed (on at most 0.6%
of decisions, Table 3). Counterfactual selection, which acts on past
contributions without such a test, trails 1/𝑁 as much as the other
agents. Third, the anchor protects MemTrial on these benchmarks.
The drafts alone do not: Draft averaging deploys the same eight
drafts and falls well behind 1/𝑁 . With the same anchor, however,
every LLM-based baseline also comes within 1% of MemTrial. With
signal in PlantedMem, MemTrial earns 11% more than the best
anchored baseline, as it acts fully on values that have predicted
unseen dates (Appendix D.5).
4.3 Ablation Study
Figure 4 changes one step of MemTrial at a time; PlantedMem is
split into the core regimes without signal (no influence, noise only),
those with signal (𝛽>0), and the regime with 48 experiences and
informative content. On real markets, the anchor and the trust test
matter: replacing the anchored blend by the draft average costs
16–41% on PortBench and InvestorBench, and acting on the values
without the trust test 4–12%, as these values do not hold on unseen
dates. The prior weight on the reference sets a trade-off: a uniform
prior loses 5–7% on PortBench and InvestorBench but gains 3.2%
on ClassAlloc, where the drafts beat 1/𝑁 , and the opposite extreme,
always keeping the reference, gains where 1/𝑁 cannot be beaten
but loses where the drafts are better (Appendix D.8). Learning the
blend online matters less: fixing it at the prior changes the utility
by−3% to+1%. On ClassAlloc, where the test passed most often,
never acting on values is 2.6% better (Appendices D.5 and E).
In PlantedMem, the learned values matter where experiences
carry signal: never acting on them costs 15% (8.5% with informative
content), and almost nothing without signal. The trust test costs
little there: removing it gains 0.9–2.4% with signal but loses 2.3%
without. Content-aware value estimation and the trust test matter
when each experience is retrieved too rarely for per-experience es-
timates or for an in-sample F-test (5–6% with informative content).
4.4 Robustness to the LLM
We repeat InvestorBench and ClassAlloc with seven other LLMs:
gpt-4.1-nano [38], gpt-5-mini [39], Gemini 2.5 Flash [ 8], Claude
Haiku 4.5 [1], and the open-weight Llama-3.3-70B [ 20], Qwen3-
235B [53] and DeepSeek-V3.1 [11]. We also run InvestorBench at
temperatures 0, 0.3 and 1.0. Appendix D.12 gives every LLM, temper-
ature and method. On InvestorBench, no LLM-based baseline beats
1/𝑁 in any of the eleven configurations, and MemTrial beats all of
them in every configuration, by 4–33% over the best experience-
learning agent. On ClassAlloc, MemTrial stays within 0.021 pp per
month of 1/𝑁 with every LLM; it beats the best experience-learning
agent with four of the eight LLMs and trails it with the other four.
Without its trust test, MemTrial does worse in most configurations.
4.5 Analysis
Does MemTrial learn what each experience is worth?In Plant-
edMem, the quality of every experience is known, so we can check
how well the learned values rank them (Figure 5; balanced investor).
Outcome credit hardly ranks them: after ten years of monthly de-
cisions, the correlation is 0.08 at 𝛽= 0.25and only 0.29 even at
𝛽= 0.5, because it follows the markets in which an experience was
retrieved. Counterfactual contributions rank them well, and the
pooled values of MemTrial reach the same level (0.81 at𝛽= 0.25);
with 48 experiences whose content is informative, pooling across
7

Wu, Cai and Wang
0 2 4 6 8 10
0.00
0.25
0.50
0.75
1.00
rank correlation with
planted quality
(a) 𝛽 = 0.25
0 2 4 6 8 10
(b) 48 exp., informative content
years of decisions
Outcome credit (MemRL †) Counterfactual sel. MemTrial
1
Figure 5:Outcome credit does not learn which experiences are
useful; counterfactual contributions do, and pooling them by content
helps when content is informative.
−0.1
0.0
0.1
0.2
0.3
gain over reference
(pp per month)
no
influence
noise
only
0.1 0.25 0.5 many
exp.
inform.
content
0
50
100
trust rate of
MemTrial (%)2 3
14
64
85
26
45
no signal with signal (𝛽) 48 experiences
Outcome credit (MemRL†) Counterfactual sel. MemTrial
1
Figure 6:PlantedMem by regime. MemTrial abstains when experi-
ences carry no signal and acts on its values when they matter.
similar experiences ranks them better than the raw contributions
(0.66 against 0.55). Early on, the shrunk values are less accurate and
MemTrial rarely acts on them; at𝛽= 0.25, its trust rate rises from
12% in the first year to 91% in the tenth as evidence accumulates.
When does MemTrial trust its values?Figure 6 shows Plant-
edMem by regime. When experiences carry no signal, the trust
test passes on only 2–3% of decisions and MemTrial stays at the
reference, whereas Counterfactual selection and outcome credit
fall below it. As experiences matter more, the test passes more
often, on up to 85% of decisions, and MemTrial gains up to 0.30 pp
per month over the reference. On the real benchmarks, the test
responds to whether learned values carry over to unseen dates,
not to whether experiences matter: on InvestorBench, experiences
change the decision on 85% of days, yet the test passed on only
0.3% of decisions. Where it passed most often (15% of ClassAlloc
decisions), the trusted drafts earned0.05pp less (s.e.0 .07) than the
anchored blend they replaced (Appendices D.11 and E).
What happens after the LLM’s knowledge cutoff?On Clas-
sAlloc, the memory-free LLM beats 1/ 𝑁 by 0.08 pp per month
before the knowledge cutoff of gpt-4.1-mini and trails it by as much
afterwards (𝑝= 0.36for the difference), and five of the six LLMs
whose cutoff is published trail 1/𝑁 after theirs. Given only a date,
each LLM recalls the asset-class returns of the following month
before its cutoff (a look-ahead bias) but hardly at all after it; yet
hiding every date from the agent does not remove the advantage
before the cutoff (Appendices D.13–D.14, Figure D.6). Anchored
at 1/𝑁 , MemTrial gives up most of the drafts’ advantage before
the cutoff but loses less than any other LLM-based method after
it (Appendix D.11). On PortBench extended to 2026, it is again the
best LLM-based method over the eleven months after the cutoff of
gpt-4.1-mini (Appendix D.15).
Hyperparameters and cost.Appendix D.7 varies the level 𝛼
of the trust test (Figure D.4). Up to the default𝛼= 0.05, the results
on the real benchmarks barely change. Looser levels let chance
forward scores pass, on up to 17% of PortBench-Full decisions, and
cost up to 4% of the utility, whereas in the informative regime of
PlantedMem they let MemTrial act earlier on values that do hold.
The anchor needs a strong prior on the reference (§4.3) but not a
precise strength, and more retrieved experiences help only when
experiences matter (Appendices D.7–D.9). A decision costs about
USD 0.05 on PortBench; at the same LLM spend, Draft averaging
does clearly worse.
5 Conclusion
When an LLM portfolio agent credits an experience with the out-
come of the decisions that used it, the credit tracks the market
rather than the experience. MemTrial instead measures what each
experience changes with a small designed experiment on every
date, pools these measurements into values across dates and similar
experiences, trusts the values only after they have predicted unseen
dates, and until then keeps an anchored blend near a conservative
reference. Where the quality of experiences is known, it achieves
the highest utility among 15 methods. On real markets, where the
learned values did not carry over to unseen dates, it stayed close to
1/𝑁, unlike existing experience-learning agents.
Limitations.On the real benchmarks, MemTrial’s values rarely
passed the trust test, and where they did (ClassAlloc), acting on
them did not beat the anchor. Its advantage there comes from the
anchor, which protects the baselines just as well, so gains from
memory on real markets remain to be shown. LLMs recall market
outcomes from before their knowledge cutoffs, a look-ahead bias
that can flatter any LLM-based method on earlier periods; Planted-
Mem and the months after the cutoff are free of it. When the LLM’s
drafts beat the reference, as on ClassAlloc before the cutoff, the
anchored action gives up most of their advantage (Appendix H).
References
[1] Anthropic. 2025. Claude Haiku 4.5 system card. https://www.anthropic.com/
system-cards.
[2] Susan Athey and Guido Imbens. 2016. Recursive partitioning for heterogeneous
causal effects.Proceedings of the National Academy of Sciences113, 27 (2016),
7353–7360.
[3] John F Banzhaf III. 1964. Weighted voting doesn’t work: A mathematical analysis.
Rutgers L. Rev.19 (1964), 317–343.
[4] John M Bates and Clive WJ Granger. 1969. The combination of forecasts.Journal
of the Operational Research Society20, 4 (1969), 451–468.
[5] Léon Bottou, Jonas Peters, Joaquin Quiñonero-Candela, Denis X Charles, D Max
Chickering, Elon Portugaly, Dipankar Ray, Patrice Simard, and Ed Snelson. 2013.
8

MemTrial: Learning When to Trust Memory
Counterfactual reasoning and learning systems: The example of computational
advertising.Journal of Machine Learning Research14, 11 (2013), 3207–3260.
[6] George EP Box, J Stuart Hunter, and William Gordon Hunter. 2005.Statistics for
Experimenters: Design, Innovation, and Discovery(2nd ed.). Wiley.
[7] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot learners.Advances in Neural
Information Processing Systems33 (2020), 1877–1901.
[8] Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, et al. 2025.
Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long
context, and next generation agentic capabilities.arXiv preprint arXiv:2507.06261
(2025).
[9] Thomas M Cover. 1991. Universal portfolios.Mathematical finance1, 1 (1991),
1–29.
[10] A Philip Dawid. 1984. Present position and potential developments: Some
personal views: Statistical theory: The prequential approach.Journal of the Royal
Statistical Society: Series A (General)147, 2 (1984), 278–290.
[11] DeepSeek-AI. 2024. DeepSeek-V3 technical report.arXiv preprint
arXiv:2412.19437(2024).
[12] Victor DeMiguel, Lorenzo Garlappi, and Raman Uppal. 2009. Optimal versus
naive diversification: How inefficient is the 1/N portfolio strategy?The Review
of Financial Studies22, 5 (2009), 1915–1953.
[13] Francis X Diebold and Robert S Mariano. 2002. Comparing predictive accuracy.
Journal of Business & economic statistics20, 1 (2002), 134–144.
[14] Bradley Efron and Carl Morris. 1975. Data analysis using Stein’s estimator and
its generalizations.J. Amer. Statist. Assoc.70, 350 (1975), 311–319.
[15] Robert E Fay III and Roger A Herriot. 1979. Estimates of income for small places:
an application of James-Stein procedures to census data.J. Amer. Statist. Assoc.
74, 366a (1979), 269–277.
[16] Yoav Freund and Robert E Schapire. 1997. A decision-theoretic generalization
of on-line learning and an application to boosting.J. Comput. System Sci.55, 1
(1997), 119–139.
[17] Lorenzo Garlappi, Raman Uppal, and Tan Wang. 2007. Portfolio selection with pa-
rameter and model uncertainty: A multi-prior approach.The Review of Financial
Studies20, 1 (2007), 41–81.
[18] Amirata Ghorbani and James Zou. 2019. Data Shapley: Equitable valuation
of data for machine learning. InInternational Conference on Machine Learning.
PMLR, 2242–2251.
[19] Tilmann Gneiting and Adrian E Raftery. 2007. Strictly proper scoring rules,
prediction, and estimation.Journal of the American statistical Association102,
477 (2007), 359–378.
[20] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Ab-
hishek Kadian, et al . 2024. The Llama 3 herd of models.arXiv preprint
arXiv:2407.21783(2024).
[21] Pierre Gutierrez and Jean-Yves Gérardy. 2017. Causal inference and uplift mod-
elling: A review of the literature. InInternational Conference on Predictive Appli-
cations and APIs. PMLR, 1–13.
[22] David P Helmbold, Robert E Schapire, Yoram Singer, and Manfred K Warmuth.
1998. On-line portfolio selection using multiplicative updates.Mathematical
finance8, 4 (1998), 325–347.
[23] Ruoxi Jia, David Dao, Boxin Wang, Frances Ann Hubis, Nick Hynes, Nezihe Merve
Gürel, Bo Li, Ce Zhang, Dawn Song, and Costas J Spanos. 2019. Towards efficient
data valuation based on the Shapley value. InThe 22nd International Conference
on Artificial Intelligence and Statistics. PMLR, 1167–1176.
[24] Philippe Jorion. 1986. Bayes-Stein estimation for portfolio analysis.Journal of
Financial and Quantitative Analysis21, 3 (1986), 279–292.
[25] Raymond Kan and Guofu Zhou. 2007. Optimal portfolio choice with parameter
uncertainty.Journal of Financial and Quantitative Analysis42, 3 (2007), 621–656.
[26] Pang Wei Koh and Percy Liang. 2017. Understanding black-box predictions
via influence functions. InInternational Conference on Machine Learning. PMLR,
1885–1894.
[27] Ron Kohavi, Roger Longbotham, Dan Sommerfield, and Randal M Henne. 2009.
Controlled experiments on the web: survey and practical guide.Data mining
and knowledge discovery18, 1 (2009), 140–181.
[28] Sören R Künzel, Jasjeet S Sekhon, Peter J Bickel, and Bin Yu. 2019. Metalearners
for estimating heterogeneous treatment effects using machine learning.Proceed-
ings of the national academy of sciences116, 10 (2019), 4156–4165.
[29] Yongchan Kwon and James Zou. 2022. Beta Shapley: A unified and noise-reduced
data valuation framework for machine learning. InInternational Conference on
Artificial Intelligence and Statistics. PMLR, 8780–8802.
[30] Romain Laroche, Paul Trichelair, and Remi Tachet Des Combes. 2019. Safe
policy improvement with baseline bootstrapping. InInternational Conference on
Machine Learning. PMLR, 3652–3661.
[31] Olivier Ledoit and Michael Wolf. 2004. Honey, I shrunk the sample covariance
matrix.The Journal of Portfolio Management30, 4 (2004), 110–119.
[32] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive NLP
tasks.Advances in Neural Information Processing Systems33 (2020), 9459–9474.
[33] Bin Li and Steven C. H. Hoi. 2014. Online Portfolio Selection: A Survey.Comput.
Surveys46, 3, Article 35 (2014).
[34] Haohang Li, Yupeng Cao, Yangyang Yu, Shashidhar Reddy Javaji, Zhiyang Deng,
Yueru He, Yuechen Jiang, Zining Zhu, K. P. Subbalakshmi, Jimin Huang, et al.
2025. InvestorBench: A benchmark for financial decision-making tasks with
LLM-based agent. InProceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers). 2509–2525.
[35] Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, and Bingsheng He. 2024.
CryptoTrade: A reflective LLM-based agent to guide zero-shot cryptocurrency
trading. InProceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing. 1094–1106.
[36] Harry M Markowitz. 1955.Portfolio selection. Ph. D. Dissertation. The University
of Chicago.
[37] OpenAI. 2024. New embedding models and API updates. https://openai.com/
index/new-embedding-models-and-api-updates/.
[38] OpenAI. 2025. Introducing GPT-4.1 in the API. https://openai.com/index/gpt-4-
1/.
[39] OpenAI. 2025. OpenAI GPT-5 system card.arXiv preprint arXiv:2601.03267
(2025).
[40] Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G Patil, Ion
Stoica, and Joseph E Gonzalez. 2023. MemGPT: Towards LLMs as operating
systems.arXiv preprint arXiv:2310.08560(2023).
[41] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy
Liang, and Michael S Bernstein. 2023. Generative agents: Interactive simulacra
of human behavior. InProceedings of the 36th Annual ACM Symposium on User
Interface Software and Technology. 1–22.
[42] Matthias Seeger. 2004. Gaussian processes for machine learning.International
Journal of Neural Systems14, 2 (2004), 69–106.
[43] Shai Shalev-Shwartz. 2012. Online learning and online convex optimization.
Foundations and Trends®in Machine Learning4, 2 (2012), 107–194.
[44] Lloyd S Shapley et al. 1953. A value for n-person games. (1953).
[45] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and
Shunyu Yao. 2023. Reflexion: Language agents with verbal reinforcement learn-
ing.Advances in Neural Information Processing Systems36 (2023), 8634–8652.
[46] Adith Swaminathan and Thorsten Joachims. 2015. Counterfactual risk mini-
mization: Learning from logged bandit feedback. InInternational Conference on
Machine Learning. PMLR, 814–823.
[47] Philip Thomas, Georgios Theocharous, and Mohammad Ghavamzadeh. 2015.
High confidence policy improvement. InInternational Conference on Machine
Learning. PMLR, 2380–2388.
[48] Jun Tu and Guofu Zhou. 2011. Markowitz meets Talmud: A combination of
sophisticated and naive diversification strategies.Journal of Financial Economics
99, 1 (2011), 204–215.
[49] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu,
Linxi Fan, and Anima Anandkumar. 2024. Voyager: An open-ended embodied
agent with large language models.Transactions on Machine Learning Research
(2024).
[50] Jiachen T Wang and Ruoxi Jia. 2023. Data Banzhaf: A robust data valuation frame-
work for machine learning. InInternational Conference on Artificial Intelligence
and Statistics. PMLR, 6388–6421.
[51] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang,
Aakanksha Chowdhery, and Denny Zhou. 2023. Self-consistency improves chain
of thought reasoning in language models. InInternational Conference on Learning
Representations.
[52] Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. 2024. TradingAgents: Multi-
agents LLM financial trading framework.arXiv preprint arXiv:2412.20138(2024).
[53] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, et al . 2025.
Qwen3 technical report.arXiv preprint arXiv:2505.09388(2025).
[54] Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang, Yang Li, Jordan W Suchow,
Denghui Zhang, and Khaldoun Khashanah. 2025. FinMem: A performance-
enhanced LLM trading agent with layered memory and character design.IEEE
Transactions on Big Data(2025).
[55] Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng
Cao, Zhi Chen, Jordan W Suchow, Zhenyu Cui, Rong Liu, et al. 2024. FinCon: A
synthesized LLM multi-agent system with conceptual verbal reinforcement for
enhanced financial decision making.Advances in Neural Information Processing
Systems37 (2024), 137010–137045.
[56] Shengtao Zhang, Jiaqian Wang, Ruiwen Zhou, Junwei Liao, Yuchen Feng, Zhuo
Li, Yujie Zheng, Weinan Zhang, Ying Wen, Zhiyu Li, et al. 2026. MemRL: Self-
evolving agents via runtime reinforcement learning on episodic memory.arXiv
preprint arXiv:2601.03192(2026).
[57] Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin,
Xinyi Li, Yuqing Zhao, Yilei Zhao, Xinyu Cai, et al. 2024. A multimodal foun-
dation agent for financial trading: Tool-augmented, diversified, and generalist.
InProceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining. 4314–4325.
9

Wu, Cai and Wang
[58] Yanzhao Zhang, Mingxin Li, Dingkun Long, Xin Zhang, Huan Lin, Baosong Yang,
Pengjun Xie, An Yang, Dayiheng Liu, Junyang Lin, et al. 2025. Qwen3 embedding:
Advancing text embedding and reranking through foundation models.arXiv
preprint arXiv:2506.05176(2025).
[59] Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao
Huang. 2024. ExpeL: LLM agents are experiential learners. InProceedings of the
AAAI Conference on Artificial Intelligence, Vol. 38. 19632–19642.
[60] Yuxuan Zhao, Sijia Chen, and Ningxin Su. 2026. PortBench: A correlation-aware,
full-pipeline benchmark for LLM-driven portfolio management.arXiv preprint
arXiv:2605.27887(2026).
[61] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. 2024. Mem-
oryBank: Enhancing large language models with long-term memory. InProceed-
ings of the AAAI Conference on Artificial Intelligence, Vol. 38. 19724–19731.
Appendices
Contents.A More Related Work (A.1 memory and experience in
LLM agents; A.2 valuation and causal effects; A.3 portfolio choice
under estimation error; A.4 forecast evaluation and safe deploy-
ment)· B Notation· C Derivations (C.1 the half-fraction design;
C.2 the value model; C.3 the trust test; C.4 the anchored action)·
D More Experiments (D.1 dataset statistics; D.2 baselines; D.3 im-
plementation details; D.4 why LLM agents trail 1/𝑁 ; D.5 ablation
details; D.6 wealth, market phases and survival; D.7 hyperparame-
ter analysis; D.8 strength of the anchor; D.9 number of retrieved
experiences by regime; D.10 PlantedMem by regime; D.11 ClassAl-
loc before and after the knowledge cutoff; D.12 other LLMs and
temperatures; D.13 ClassAlloc with other LLMs; D.14 look-ahead
checks; D.15 PortBench after the knowledge cutoff)· E Case Study·
F Algorithms· G LLM Prompts (G.1 InvestorBench; G.2 ClassAlloc;
G.3 PortBench)·H Limitations.
A More Related Work
A.1 Memory and experience in LLM agents
In more detail than §2: MemGPT [40] manages a hierarchy of mem-
ory tiers for long interactions, MemoryBank [61] stores memories
and lets them fade with a rule inspired by the forgetting curve, and
Voyager [49] builds a library of executable skills that it reuses when
they succeed; in finance, FinCon [55] updates the investment be-
liefs of a team of LLM agents by verbal reinforcement from realized
profit and loss. These methods decide what to store, keep or reuse
from the success of the episodes in which a memory took part, i.e.,
by outcome credit, and none of them tests whether its rule for using
memory predicts future gains before acting on it.
A.2 Valuation and causal effects
The Shapley value [44] and the Banzhaf value [3] are the two classic
ways to divide a joint payoff among players. Data valuation adapts
them to training data [18, 23, 29, 50]: Beta Shapley reweights subsets
by their size to reduce noise, and Data Banzhaf weights all subsets
equally, which makes it the most robust semivalue when the utility
is noisy. Our counterfactual contribution (3) is the main effect of a
factor in a24−1 fractional factorial experiment [6], the classic way to
estimate several effects at once with few runs; Appendix C.1 shows
that it equals the Banzhaf value when the three-way interaction
aliased with it is negligible. Estimating what an experience does to
a decision is also a problem of heterogeneous treatment effects [2,
28]. Uplift modelling [21] and counterfactual learning from logged
decisions [5, 46] estimate such effects from observational data, and
online controlled experiments [27] randomize users into groups.
MemTrial instead runs the whole designed experiment on every
date, so the market is held fixed within each comparison.
A.3 Portfolio choice under estimation error
Mean–variance optimization [36] is sensitive to errors in the es-
timated means and covariances, which has motivated shrinkage
estimators [24, 31], portfolios that account for parameter and model
uncertainty [17, 25], and combinations of an optimized portfolio
with 1/𝑁 [48]. DeMiguel et al. [12] find that none of the optimized
portfolios they evaluate consistently beats 1/𝑁 out of sample. On-
line portfolio selection [9, 22, 33] adapts the weights over time with
regret guarantees. The anchored action of MemTrial combines two
of these ideas: shrinkage towards a conservative reference, and an
online blend learned with a regularizer.
A.4 Forecast evaluation and safe deployment
Prequential analysis [10] judges a model by its sequential out-of-
sample predictions; tests of predictive accuracy [ 13] and proper
scoring rules [19] formalize such judgments. The trust test of Mem-
Trial applies this idea to the values of experiences, as a one-sided test
of whether their out-of-sample correlations with the measured con-
tributions are positive on average. Safe policy improvement [30, 47]
deploys a new policy only when it improves on a baseline with high
confidence; in MemTrial, the trust test plays the role of this confi-
dence check, and the anchored action that of the baseline policy.
Finally, shrinkage across units [14, 15] underlies our value model.
B Notation
C Derivations
C.1 The half-fraction design
Code the presence of the 𝑗-th retrieved experience in a subset𝑆 as
𝑥𝑗 =+ 1if 𝑗∈𝑆 and𝑥𝑗 =− 1otherwise, and write the utility of a
draft as a full factorial model,
𝑈𝑡(𝑆)=𝜇 𝑡+
∑︁
𝑗
𝑎𝑗
2 𝑥𝑗+
∑︁
𝑗<𝑙
𝑎𝑗𝑙
2 𝑥𝑗𝑥𝑙
+
∑︁
𝑗<𝑙<𝑚
𝑎𝑗𝑙𝑚
2 𝑥𝑗𝑥𝑙𝑥𝑚+ 𝑎1234 2 𝑥1𝑥2𝑥3𝑥4+𝜀𝑡,𝑆,(C.1)
where𝜇𝑡 collects everything the drafts of date𝑡 share, including
the market move,𝑎𝑗 is the main effect of experience 𝑗 (over the 16
subsets, the mean utility of those with it minus that of those without
it), the other𝑎’s are interactions, and𝜀𝑡,𝑆 is the sampling noise of
the draft. Over all 16 subsets, the main effect equals the Banzhaf
value of 𝑗, because both are the mean over subsets with 𝑗 minus
the mean over subsets without it. Since𝑘= 4is even, a subset has
an even number of experiences exactly when𝑥1𝑥2𝑥3𝑥4 =+ 1, so the
design (2) is the half fraction with defining relation𝐼=𝑥 1𝑥2𝑥3𝑥4.
Multiplying by𝑥𝑗 shows that on the design𝑥𝑗 equals the product of
the other three columns: each main effect is aliased with the three-
way interaction of the other three experiences, and each two-way
interaction with the complementary one (𝑥1𝑥2 =𝑥 3𝑥4), which is
resolution IV. The contribution(3) is the contrast of column𝑥𝑗 over
the design, so under (C.1)
𝑐𝑡,𝑗 =𝑎 𝑗+𝑎(−𝑗) + ¯𝜀+ 𝑡,𝑗− ¯𝜀− 𝑡,𝑗,(C.2)
10

MemTrial: Learning When to Trust Memory
Table B.1: Notation.
Symbol Meaning
𝑡,𝑇decision date, number of dates
𝑠𝑡 market state at date𝑡
𝑁number of assets (plus cash)
𝜃=(𝑀,𝑚,𝛾)investor profile: maximum share of risky assets,
minimum share of defensive assets, risk aversion
𝑃𝜃 projection of a portfolio onto the investor’s
mandate
𝑢𝑡(𝑥);𝑟 𝑡 ,𝑉𝑡 investor utility (certainty-equivalent return) of
portfolio𝑥, Eq. (1); net return and realized
variance over the holding period
𝜋;𝑥∼𝜋(·|𝑠 𝑡,𝑆) LLM policy; a draft made with the experiences in
𝑆
𝑘;
𝑅𝑡 =(ℎ 𝑡,1,...,ℎ 𝑡,𝑘)
number of retrieved experiences (4); experiences
retrieved at date𝑡
Ddesigned subsets, Eq. (2)
𝑈𝑡(𝑆) utility of the draft made with subset𝑆, at realized
prices
𝑐𝑡,𝑗 ;𝑦𝑡,𝑗 counterfactual contribution of the𝑗-th retrieved
experience, Eq. (3); centred contribution, Eq. (4)
𝑣ℎ; ˆ𝑣ℎ value of experienceℎ; its posterior mean, Eq. (7)
𝑧ℎ∈R 𝑑 content feature of experienceℎ(𝑑=8principal
components of its embedding)
𝛽;𝑏 ℎ map from content to value; experience-specific
deviation
𝜎2;𝜎 2 𝛽 ,𝜏 2 noise variance; prior variances, Eq. (5)
𝑛ℎ;𝑚ℎ number of dates with a realized outcome on
whichℎwas retrieved; mean of its centred
contributions
𝜌𝑡 ;𝑛;𝛼forward score at date𝑡, Eq. (8); number of
forward scores; level of the trust test, Eq. (9)
𝑆∗ 𝑡 trusted subset, Eq. (10)
𝑥 ref; ¯𝑥𝑡 conservative reference; average draft
𝑞𝑡 ;𝛼 0;𝜆 0 weight on the reference; its prior; regularization
strength, Eq. (11)
where𝑎(−𝑗) is the three-way interaction of the other three expe-
riences and ¯𝜀+, ¯𝜀− are the mean noise of the four drafts with and
the four without experience 𝑗. Three consequences follow. First,
𝜇𝑡 , everything the drafts of date𝑡 share, cancels; the market move
enters𝑐𝑡,𝑗 only through the weights that experience𝑗 changes. Sec-
ond,𝑐𝑡,𝑗 estimates the main effect without bias when three-way
interactions are negligible, and the four contrasts are orthogonal to
each other and to every two-way interaction, so the contribution
of one experience is not affected by two-way interactions. Third,
the noise term has variance𝜎2 𝜀/2for draft-level noise variance 𝜎2 𝜀 ,
against𝜎2 𝜀/4for the full factorial with twice as many drafts. On
ClassAlloc and InvestorBench, where all 16 subsets were drafted
on every date and seed, the difference between 𝑐𝑡,𝑗 and the full-
factorial value, half the contrast between the two half fractions, has
1.26–1.34 times the mean square that sampling noise alone gives
(𝜎2 𝜀/4, with𝜎 2 𝜀 estimated from the spread of a draft’s utility across
seeds): the three-way interaction aliased with the main effect adds
13–17% to the noise variance of a contribution, and𝑐𝑡,𝑗 correlates
with the full-factorial value at 0.76–0.86.
C.2 The value model
Stack the𝐻 experiences that have at least one measured contribu-
tion. Under Eq. (5), the values𝑣=𝑍𝛽+𝑏 and the observed means
𝑚are jointly Gaussian with
𝑣∼N(0,𝐾 𝑣), 𝐾 𝑣 =𝜎 2 𝛽𝑍𝑍⊤+𝜏 2𝐼,
𝑚∼N(0,𝐾), 𝐾=𝐾 𝑣+𝜎 2 diag(1/𝑛ℎ), (C.3)
which gives the marginal likelihood(6). Gaussian conditioning gives
E[𝑣|𝑚]=𝐾 𝑣𝐾−1𝑚 and E[𝛽|𝑚]=𝜎 2 𝛽𝑍⊤𝐾−1𝑚, i.e., Eq. (7). For a
new experienceℎ′ without measurements, cov(𝑣ℎ′,𝑚)=𝜎 2 𝛽𝑧⊤ ℎ′𝑍⊤,
so E[𝑣ℎ′|𝑚]=𝑧 ⊤ ℎ′ ˆ𝛽: its value is predicted from its content alone.
Without content (𝜎2 𝛽 =0),𝐾is diagonal and
ˆ𝑣ℎ = 𝜏2 𝜏2+𝜎 2/𝑛ℎ 𝑚ℎ,(C.4)
the James–Stein-type shrinkage of the Fay–Herriot model [15]: an
experience measured on few dates is shrunk towards zero, which
after the centring (4) is the value of an average experience. The
noise variance𝜎2 is the pooled within-experience variance of the
centred contributions, and(𝜎 2 𝛽,𝜏 2)maximize (6) over a grid.
C.3 The trust test
Suppose that the learned values carry no information about future
contributions, so that every forward score has mean zero. If the
scores were independent and approximately normal, the statistic in
Eq. (9) would follow a Student𝑡 distribution with𝑛− 1degrees of
freedom, and a single test at a fixed𝑛 would pass with probability at
most𝛼. MemTrial uses the test as a decision rule: it applies the test
on every date with𝑛≥ 10, to the scores of the learner whose mean
score is higher. Scores of nearby dates are also dependent when the
same experiences recur. The level𝛼 is therefore the level of one
test, not the rate at which the rule passes over a run. That rate is
measured where every pass is a false one: in the two PlantedMem
regimes in which experiences carry no signal, the rule passed on
2.3% and 3.0% of decisions (Table D.13). The minimum of 10 scores
and the level𝛼= 0.05were fixed on the development seeds, and
Table D.9 varies both.
C.4 The anchored action
Both the reference and the average draft satisfy the mandate, which
is a convex set, so every blend𝑥𝑡(𝑞) does too. Because𝑞 is a single
number, Eq. (11) is solved by evaluating the objective on a grid of
201 values, which finds its maximizer up to the grid spacing without
any assumption on its shape; the utility of every blend is computed
exactly on the realized price path, including trading costs. Before
any outcome is realized,𝑞𝑡 =𝛼 0. As𝑛 grows,𝜆𝑛 =𝜆 0 ˆ𝜎𝑛/√𝑛 tends
to zero, so the weight of the prior fades and𝑞𝑡 approaches the blend
with the highest mean utility over the past dates, as in follow-the-
regularized-leader [43]. Scaling by ˆ𝜎𝑛 makes𝜆0 independent of the
units of utility, so the same𝜆 0 =4is used on all benchmarks.
D More Experiments
Improv.is the gain of MemTrial over the best experience-learning
agent of each setting, in percent of that agent’s utility.
11

Wu, Cai and Wang
D.1 Dataset statistics
Table D.1 gives the size of each benchmark and the cost of our
runs. The smallest sample is the PortBench test period (20 months):
with significance tested across test dates, none of the PortBench
differences in Table 3 is significant. The ten further InvestorBench
runs of §4.4 make 8,940 executions each (the 16 subsets, ExpeL and
the three sequential agents, over 149 days and three seeds) and cost
USD 1.21–16.90 each; the seven further ClassAlloc runs make 4,318
executions each and cost USD 0.38–6.01 each, and the two extra
memory-free draws per date and seed of Self-consistency cost USD
6.76 in all. Replaying the sequential agents of all ten ClassAlloc
runs (eight LLMs and two with dates hidden, Appendix D.14) with
the feedback timing of Appendix D.3 cost USD 1.26.
D.2 Baselines
Several methods are evaluated on the same logged drafts, so that
they differ only in how they use memory.1/ 𝑁 [12] holds equal
weights in all assets and cash, projected to the mandate.Minimum
variance[ 36] is the long-only minimum-variance portfolio esti-
mated from the past 60 daily returns, projected to the mandate.
Memory-free(zero-shot) [ 7] deploys the draft made without expe-
riences.Self-consistency[ 51] averages memory-free drafts of the
same decision: on the real benchmarks, three per seed (the seed’s
own draft and two further draws, made after the main runs with
the same prompt, LLM and temperature); in PlantedMem, eight.
Similarity retrieval[ 32] deploys the draft made with the two most
similar or with all four retrieved experiences.FinMem[ 54] ranks
memories by similarity, recency and an importance score that is
reinforced when the decision that used them earns a positive return.
MemRL[ 56] learns a value for each memory from the rewards of
the decisions that used it and selects among the most similar can-
didates, with𝜀-greedy exploration.Reflexion[ 45] writes a verbal
reflection after each outcome and conditions later decisions on the
most recent reflections.ExpeL[59] distils insights from successful
and failed decisions; on InvestorBench and ClassAlloc the LLM
writes them, and on PortBench and in PlantedMem we use its in-
sight votes (†): an experience gains a vote when the decision it
took part in beats 1/𝑁 and loses one otherwise, and the two experi-
ences with the most votes are used.Uplift credit[ 21] regresses the
utility of the deployed decision on indicators of which experiences
were used, with the utility of 1/𝑁 as a market control and a small
ridge penalty, and uses the two experiences with the highest coef-
ficients, exploring a random pair on 10% of dates.Counterfactual
selection[ 50] measures the Banzhaf contribution of each retrieved
experience on every date with a realized outcome and deploys the
draft with the two experiences of highest mean past contribution,
without value estimation, trust test or anchor.Draft averaging[ 4]
deploys the average of MemTrial’s eight designed drafts.Hedge[16]
mixes 1/𝑁 and the portfolios of the memory configurations avail-
able on each benchmark (memory-free, top-4 retrieval, FinMem and
MemRL, plus the benchmark’s native memory on PortBench) with
exponential weights, whose learning rate is scaled as in Eq. (11).
On PortBench, FinMem and MemRL select experiences from the
same pool with their own memory modules; where a baseline’s own
module cannot run (†in Table 3), we re-implement its memory-
scoring rule over the same experience pool. The baselines learn as
follows. On PortBench, the FinMem and MemRL modules receive
no feedback after July 2019, before the first decision date, and score
the pool by the outcomes recorded up to then; ExpeL†is the vote
rule above (ExpeL-style voting), and Reflexion writes a reflection
once the outcome of each decision is known. On InvestorBench
and ClassAlloc, FinMem†and MemRL†update their importance
and values, and Reflexion its reflections, once the outcome of each
decision is known; FinMem†and MemRL†learn from the return
of their own draft over the holding period, before the mandate and
fees. ExpeL’s insights are written once from the warm-up lessons.
In PlantedMem, every adapted agent updates after every period.
Uplift credit, Counterfactual selection, Hedge and MemTrial learn
from every realized outcome on all benchmarks.
D.3 Implementation details
• Agents.All LLM agents use gpt-4.1-mini (2025-04-14) [ 38]
at temperature 0.7. On PortBench, a draft is one run of the
benchmark’s staged agent (market interpretation, signal
generation and weight optimization), which makes three
LLM calls with JSON output; the retrieved experiences en-
ter the prompt as a memory block of at most 4,096 tokens.
PortBench-Raw uses the benchmark’s native prompt, which
shows a price table of eight assets, and PortBench-Full ex-
tends the table to all eligible assets. On InvestorBench, a
draft is one chat completion that returns a JSON object with
the weights of the four stocks and cash; the prompt gives,
for each stock, the close, the 1-, 5- and 20-day returns, the
20-day volatility and up to three news headlines of the day,
and an invalid reply is retried once. The runs with other
LLMs (§4.4) also use gpt-4.1-nano (2025-04-14) [38], gpt-5-
mini (2025-08-07; minimal reasoning effort, temperature
fixed by the API) [39], and, through OpenRouter, Llama-3.3-
70B-Instruct [20], Qwen3-235B-A22B-Instruct-2507 [ 53],
DeepSeek-V3.1 (non-thinking mode) [11], Gemini 2.5 Flash
(thinking budget 0) [8] and Claude Haiku 4.5 [1], all with
unchanged prompts; on InvestorBench the lessons and their
embeddings are those of the main run, and on ClassAlloc
each LLM writes its own lessons; the ExpeL insights and
Reflexion notes are always written by the LLM under test.
• ClassAlloc.Each class index averages, every day, the daily
returns of PortBench’s assets in that class that have prices
on both days (44 equities, 15 bond, 16 commodity, 10 real-
estate and 4 cash assets); an asset listed after January 2015
enters its index only after 20 sessions of prices, because
the first quotes of new listings can be wrong (one coin
gains 10,200% on its third day). Decisions are made on the
first session of each month from July 2015 (on 6 July, the
first session with six months of history) to March 2026,
the last month with 20 sessions of outcome in the data.
Each decision is scored over the 20 sessions after it, and the
holdings are carried to the next decision date. Every learner
uses an outcome only after its 20 sessions have passed: in
9 of the 70 test months the next decision comes after 19
sessions, and that outcome is first used at the decision after
next. The sequential agents of our runs (FinMem, MemRL
and Reflexion) were replayed under this timing from the
12

MemTrial: Learning When to Trust Memory
Table D.1: Benchmark statistics and cost.
PortBench (Full / Raw) InvestorBench ClassAlloc PlantedMem
Decision dates 59 monthly, Aug 2019 – Dec 2024 (a
month whose 20-day window would
overlap the previous one is skipped); 56
usable per configuration
63 warm-up and 149 test trading
days, Jul 2020 – May 2021
129 monthly, Jul 2015 – Mar 2026:
58 warm-up and 71 test
132 monthly, Apr 2015 – Mar
2026, per episode; the first 12
are a warm-up
Development / test 36 / 20 months none (fully held out) / 149 days none (fully held out) / 71 months seeds 0–14 / 15–114
Assets 99 in 6 classes, including cash HON, JNJ, MSFT, UVV and cash equities, bonds, commodities, real
estate and cash: equal-weighted
indices of 89 assets
equities, bonds, cash,
commodities
Experiences 338 records of earlier decisions (Apr 2015
– Jul 2019); 29 retrieved
63 lessons written in the
warm-up
58 lessons written in the warm-up 12 or 48 planted per episode
Drafts per date and
seed
19: the 16 subsets of the 4 retrieved
experiences, FinMem, MemRL and the
benchmark’s native memory; Reflexion
runs separately
20: the 16 subsets, ExpeL,
FinMem, MemRL and Reflexion
20: the 16 subsets, ExpeL, FinMem,
MemRL and Reflexion
resampled from 2,828 logged
LLM allocations
LLM executions 6,612 (6,518 valid) and 354 Reflexion
decisions
9,003 4,318 (58 in the warm-up), and 210
redrawn (Appendix D.3)
none
API cost about USD 43.6 USD 5.09 USD 1.61, and USD 0.12 to redraw none
Retrieval (𝑘=4) Qwen3 embeddings text-embedding-3-small text-embedding-3-small regime match with noise
Trading costs (15 bp) on the distance from equal weights on the amount traded on the amount traded on the distance from equal
weights
Seeds 3 3 3 100 (and 15 for development)
Evaluated test
decisions per method
360 (20 months× 3 investors× 3 seeds×
2 configurations)
1,341 (149 days×3 investors×
3 seeds)
639 (71 months×3 investors×3
seeds)
252,000 (100 seeds× 120 months
×7 regimes×3 investors)
logged runs: a logged decision whose prompt is unchanged
is kept, and any other decision, with the reflection written
after it, is drawn anew (210 of 639 in the main run). The
mandate treats equities and real estate as risky and bonds
and cash as defensive, as PortBench does. Each lesson is
written after the agent sees the returns of the five classes
over the 20 holding sessions, its own portfolio return and
that of the equal-weight portfolio, and is retrieved by text-
embedding-3-small [37] as on InvestorBench. FinMem’s
recency decays over 4.5 months (about 90 trading days); all
other settings are as on InvestorBench.
•PlantedMem.An episode runs over 132 monthly dates (Ta-
ble D.1) with four asset classes, the equal-weighted indices
of PortBench’s equities, bonds, cash and commodities, and
20-session outcomes; every decision starts from the equal-
weight portfolio, and its outcome is known before the next
one. Of the 12 (or 48) planted experiences, a quarter are
useful, half neutral and a quarter misleading, in random
order. Each experience has a home regime, drawn indepen-
dently of its type; on date𝑡 it receives the retrieval score
⊮[home=𝑔 𝑡]+𝜖 with𝜖∼N( 0, 0.52), where 𝑔𝑡 = 1if
the equities rose on average over the previous 60 sessions,
and the four highest scores are retrieved. On each date,
a retrieved experience points to an asset class 𝑐𝑡,ℎ: a use-
ful (misleading) experience points with probability 0.7 to
the class with the highest (lowest) return over the coming
20 sessions, and otherwise, like a neutral one, to a class
drawn uniformly. A draft made with the experiences𝑆 is
𝑥𝑆 =( 1−𝛽)𝑏+𝛽 1 |𝑆| ˝ ℎ∈𝑆 𝑒𝑐𝑡,ℎ , where𝑏 is an allocation
drawn for each draft from 2,828 logged gpt-4.1-mini allo-
cations of PortBench (aggregated to the four classes) and
𝑒𝑐 is the indicator of class 𝑐; the memory-free draft is 𝑏.
The regimes set𝛽∈{ 0, 0.1, 0.25, 0.5}, andnoise onlyuses
𝛽= 0.5with every experience neutral. The content feature
is𝑧ℎ =𝜅𝑞 ℎ𝑒1+𝜉ℎ, with type𝑞ℎ∈{+ 1, 0,− 1},𝜉ℎ∼N( 0,𝐼 8),
𝜅= 1.5in the regime with informative content and 0 other-
wise. Usefulness is thus defined by the direction in which an
experience moves the draft, and its gain in utility depends
on the date and the investor. The adapted baselines act
on the same retrieved experiences: FinMem†adds an im-
portance that rises when the decision beats 1/𝑁 , MemRL†
learns values from the utilities of the decisions that used the
experiences, ExpeL†votes, and Reflexion†tilts the draft
towards the classes that did best in the last three periods.
• Retrieval.On PortBench, the query is a short JSON text with
the task description, the date, the public market features, the
number of assets and the risk profile of the benchmark task.
Each experience is the JSON record of an earlier decision:
its allocation by asset class, the public market features at
the time and the realized 20-day outcome. Both are embed-
ded with Qwen3-Embedding-0.6B [58] (1,024 dimensions,
run locally), and the four records with the highest cosine
similarity are retrieved. All 338 records became available
between April 2015 and July 2019, before the first deci-
sion date. On InvestorBench, the query is the day’s market
context described above, each experience is a lesson of at
most 700 characters that the agent wrote after seeing the
outcome of a warm-up decision, and both are embedded
with text-embedding-3-small. Ties are broken by experi-
ence identifier.
• Mandate.On PortBench, 𝑃𝜃 is the Euclidean projection onto
the long-only portfolios whose risky share (equities, real es-
tate and cryptocurrency) is at most𝑀 and whose defensive
share (bonds and cash) is at least𝑚, computed by alternat-
ing projections. On InvestorBench, negative weights are
set to zero and, if the stock share exceeds min(𝑀, 1−𝑚) ,
the stock weights are scaled down to this cap and the rest
goes to cash.
13

Wu, Cai and Wang
• Trading costs and utility.Costs are 15 bp of the L1 distance
moved. Each PortBench decision is an episode that starts
from the equal-weight portfolio, as in the benchmark, so the
distance is measured from it; PlantedMem does the same.
On InvestorBench, holdings drift with prices overnight and
the distance is measured from the drifted holdings, so every
method pays for what it actually trades. The variance term
of Eq. (1) is the variance of daily portfolio returns times the
number of days held (20); on InvestorBench, with one day
held, it is the squared daily return.
• MemTrial.Content features 𝑧ℎ are the first𝑑= 8principal
components of the retrieval embeddings of all experiences,
standardized; in PlantedMem, the first coordinate carries𝜅
times the experience’s quality plus standard normal noise
and the others are noise.(𝜎 2 𝛽,𝜏 2) maximize the marginal
likelihood (6) over a small grid; Eq. (11) is solved over 201
values of𝑞. All learning uses only outcomes realized before
the decision date.
• Seeds.A seed means different things on the two kinds of
benchmark. On the real benchmarks, a seed is an indepen-
dent deployment in which every LLM draft is sampled anew.
There is only one market history, so additional seeds mea-
sure only the randomness of the LLM, and each one costs a
full set of paid calls (about USD 14.5 per seed on PortBench,
USD 43.6 for all methods and seeds); we use three seeds and
test significance across test dates, where the randomness of
the market lies. In PlantedMem, a seed is a newly generated
world (which experiences are useful, the retrieval noise and
the resampled drafts), which costs no LLM call, so we use
100 test seeds to make the estimates precise. A standard
deviation shown as 0.00 is below 0.005; this happens when
MemTrial stays anchored at the reference, which does not
depend on the seed.
• LLM cost and learning overhead.MemTrial makes eight
drafts per decision. The drafts are independent and run in
parallel, so the latency of a decision is that of a single draft.
With gpt-4.1-mini, one draft costs about USD 0.006 on Port-
Bench and USD 0.0006 on InvestorBench, whose prompts
are shorter, so a MemTrial decision costs about USD 0.05
and USD 0.005, respectively; the complete InvestorBench
run, covering all 15 methods with three seeds, cost USD 5.09,
and the ClassAlloc run USD 1.61 (Appendix D.1). At equal
LLM spend, the relevant comparison is Draft averaging,
which uses the same eight drafts and is 0.36 and 0.81 pp per
month worse than MemTrial on PortBench, 1.70 bp per day
worse on InvestorBench and 0.12 pp worse in PlantedMem
(Table 3). Fitting both value models, scoring the trust test
and solving Eq. (11) takes 3.6 ms per decision on average
with 12 experiences and 6.9 ms with 48 experiences (95th
percentiles 6.2 and 10.4 ms, one CPU core), and recording a
realized outcome takes 0.1 ms, which is negligible next to a
single LLM call.
• Statistics.Mean ± sd over seeds; one-sided paired 𝑡-tests
over test dates on the real benchmarks (after averaging over
seeds and investors) and over seeds in PlantedMem. Every
number in the paper is computed from the logged drafts;
after MemTrial was frozen, only the names in its source
file were changed (the sha256 of the file before and after is
recorded with the code).
D.4 Why do LLM agents trail 1/𝑁?
Table D.2 splits the test-period utility into gross return, trading cost
and risk penalty (utility = gross return− cost− risk penalty, up to
rounding; mean± sd over seeds, each averaged over the investors,
in % per month on PortBench and bp per day on InvestorBench).
L1 is the mean distance from the equal-weight portfolio, on which
PortBench charges costs. On PortBench-Full, the memory-free draft,
the top-4 retrieval draft and the average of the eight designed drafts
trail 1/𝑁 by 0.33–0.42 pp per month, and the gap has three parts
of similar size: 0.06–0.16 pp less gross return, 0.13–0.15 pp more
trading cost and a 0.11–0.14 pp larger risk penalty. Each month, the
LLM moves about half of the capital away from the equal-weight
portfolio (an L1 distance of 1.0–1.2, against 0.17 for 1/𝑁 projected
to the mandate), which costs money and adds risk without earning
more. On PortBench-Raw, whose prompt shows only eight assets,
the drafts are also more defensive than 1/𝑁 : they earn 0.72–0.85 pp
less gross return at a slightly smaller risk penalty. On InvestorBench,
the other LLM-based methods earn about the same gross return
as 1/𝑁 (10.7–11.7 against 11.4 bp per day), but they change their
portfolios substantially every day and pay 1.0–2.5 bp per day in
trading costs, against 0.1 bp for 1/𝑁 and 0.2 bp for MemTrial. With
trading costs set to zero for all methods, MemTrial included, every
LLM draft still trails 1/𝑁 on PortBench, by 0.17–0.27 pp per month
on Full and 0.68–0.81 pp on Raw, while MemTrial stays within
0.04 pp of it. In short, the drafts do not pick better assets than equal
weighting, and their frequent reallocation costs money. Experience
learning would have to close this gap to beat 1/𝑁 . Outcome credit
does not close it, and MemTrial’s trust test finds that its learned
values do not hold on unseen dates, so it stays near the reference.
D.5 Ablation details
This appendix completes §4.3 (Figure 4). Table D.3 gives the trust
rate of every variant, the share of test decisions on which it acted
on its learned values (mean± sd over seeds: three seeds on the real
benchmarks, each pooling the configurations and investors; 100 test
seeds in PlantedMem and 50 for the𝑘 designs). PlantedMem (core)
averages the five core regimes, and PlantedMem (informative) is
the regime with 48 experiences and informative content; – marks
settings that were not evaluated. A large sd on the real benchmarks
means that the test passed mostly in one seed. Table D.4 gives
the utilities behind Figure 4. The variant whose test never passes
always takes the anchored action: it is identical to MemTrial on
PortBench-Full, where the test of MemTrial never passed either, and
in PlantedMem it stays at the reference in every regime (Table D.14).
On ClassAlloc it earns 0.629% per month against 0.613% for Mem-
Trial: acting on the trusted values cost 0.016 pp per month there
(𝑝= 0.28; Appendix E). Fixing the blend of the anchored action at
its prior (𝑞=𝛼 0 = 0.9, no online learning) and always keeping the
reference (𝑞= 1) are two fixed alternatives to the learned blend:
the first differs from MemTrial by−3.1% to+0.9%, and the second
is the extreme𝛼 0 =1of the prior (Appendix D.8).
14

MemTrial: Learning When to Trust Memory
Table D.2: Decomposition of the test-period utility. The LLM drafts trail 1/ 𝑁 in all three parts on PortBench-Full, mostly in
gross return on PortBench-Raw and mostly in trading costs on InvestorBench.
Benchmark Method Utility Gross return Trading cost Risk penalty L1
PortBench-Full
1/𝑁2.02±0.002.25±0.000.03±0.000.21±0.000.17±0.00
Memory-free 1.60±0.052.12±0.050.17±0.020.34±0.031.13±0.11
Sim. retrieval (top-4) 1.70±0.062.19±0.040.18±0.020.31±0.021.17±0.14
Draft averaging 1.62±0.052.09±0.060.16±0.000.32±0.021.02±0.01
PortBench-Raw
1/𝑁2.02±0.002.25±0.000.03±0.000.21±0.000.17±0.00
Memory-free 1.07±0.021.43±0.030.18±0.010.17±0.001.19±0.08
Sim. retrieval (top-4) 1.05±0.021.40±0.020.19±0.010.17±0.001.22±0.05
Draft averaging 1.19±0.021.53±0.020.17±0.000.17±0.001.13±0.03
InvestorBench
1/𝑁10.45±0.0011.44±0.000.11±0.000.88±0.00–
Memory-free 8.43±0.2911.53±0.312.16±0.070.94±0.01–
Sim. retrieval (top-4) 8.12±0.6110.74±0.581.72±0.050.90±0.01–
Draft averaging 8.69±0.0911.23±0.111.62±0.030.91±0.00–
ExpeL 8.93±0.3210.78±0.340.96±0.020.89±0.00–
MemTrial (ours)10.40±0.0411.44±0.060.16±0.010.88±0.00–
Table D.3: Trust rate (%) of every variant. With the trust test, MemTrial acts on its values on at most 0.3% of PortBench and
InvestorBench decisions (0.6% on PortBench-Raw alone); without it, on 25–35%.
Variant PortBench InvestorBench ClassAlloc PlantedMem (core) PlantedMem (informative)
Ablation (Figure 4)
MemTrial (ours)0.3±0.50.3±0.514.6±21.733.7±9.244.9±22.5
per-experience only (no content) 0.0±0.00.3±0.514.6±21.731.8±8.922.0±20.7
content-aware only (no learner selection) 1.1±1.30.3±0.514.6±21.732.6±9.044.5±23.1
in-sample F-test 0.0±0.00.0±0.02.3±4.129.3±8.415.1±17.8
no trust test 24.7±21.434.5±18.853.8±24.754.3±12.664.9±18.6
test never passes (always anchored action) 0.0±0.00.0±0.00.0±0.00.0±0.00.0±0.0
draft average (𝑞=0) 0.3±0.50.0±0.014.9±20.533.7±9.244.9±22.5
always the reference (𝑞=1) 0.3±0.50.3±0.514.4±21.833.7±9.244.9±22.5
uniform prior (𝛼0 =0.5) 0.3±0.50.0±0.014.7±20.633.7±9.244.9±22.5
no online learning (𝑞fixed at𝛼 0) 0.3±0.50.3±0.514.4±21.833.7±9.244.9±22.5
Trust test (Table D.9); default𝛼=0.05, at least 10 forward scores
𝛼=0.010.0±0.00.0±0.0– 28.2±8.132.9±22.3
𝛼=0.020.0±0.00.0±0.0– 30.3±8.537.8±22.7
𝛼=0.15.3±5.00.5±0.9– 36.9±10.050.6±21.4
𝛼=0.212.2±13.01.6±2.3– 40.7±11.056.3±20.4
at least 5 forward scores 0.3±0.50.3±0.5– 33.9±9.244.6±22.2
at least 20 forward scores 0.0±0.00.0±0.0– 32.0±8.543.4±21.6
Number of retrieved experiences and design (Table D.10); PlantedMem on seeds 15–64
𝑘=2, full factorial (4 drafts) 0.0±0.02.0±2.0– 8.5±7.77.2±12.3
𝑘=3, half fraction (4 drafts) 0.8±1.44.5±5.2– 18.5±9.49.5±13.7
𝑘=3, full factorial (8 drafts) 0.0±0.010.8±10.7– 29.4±11.043.4±25.6
𝑘=4, half fraction (8 drafts; seeds 15–64) 0.3±0.50.3±0.5– 35.4±11.049.6±24.3
𝑘=4, full factorial (16 drafts) 1.1±1.98.5±7.4– 42.0±8.169.9±20.1
𝑘=5, half fraction (16 drafts) – – – 43.4±10.374.7±17.0
𝑘=6, half fraction (32 drafts) – – – 49.1±9.886.4±10.6
Why do some values coincide?On PortBench and Investor-
Bench, the three variants that change how values are learned or
tested give the same numbers as MemTrial in all but two cells.
Such a change can affect a decision only when the values are acted
upon, and on these two benchmarks the test (or the F-test) passes
on at most 1.1% of decisions (Table D.3), so on all other decisions
the four methods take the same anchored action. The two excep-
tions come from the few decisions on which the tests disagree:
the content-aware learner alone passes its test by chance on a few
PortBench-Raw decisions (1.94± 0.12; observation 3), and the F-test
never passes on InvestorBench, whereas MemTrial’s test passes
on 0.3% of decisions (10.37 against 10.40). On ClassAlloc, the value
model estimates the content term at zero on every date, so the
content-aware learner coincides with the per-experience learner,
and the two value-estimation variants give the same numbers as
MemTrial although the test passes on 15% of decisions. Where no
test passes, the anchored action stays close to the reference, which
does not depend on the seed, so the sd is below 0.005; a test that
passes on a few decisions of one seed raises it (0.04 for MemTrial on
InvestorBench). The same steps make a difference in PlantedMem,
where these variants trust their values on 15–45% of decisions and
the columns differ. The anchored-action variants change what the
15

Wu, Cai and Wang
Table D.4: Utilities behind Figure 4, with the variant that always keeps the reference ( 𝑞= 1; Appendix D.8) (% per month, bp per
day on InvestorBench; mean± sd over seeds). Without signal, the variants differ little in PlantedMem; with signal, never acting
on the learned values stays at the reference.
PlantedMem
Step changed Variant PortBench-Full PortBench-Raw InvestorBench ClassAlloc no signal signal informative content core
–MemTrial (ours)1.98±0.002.01±0.00 10.40±0.04 0.613±0.0170.784±0.0310.932±0.0700.862±0.0680.873±0.045
Value
estimation
per-experience learner only 1.98±0.002.01±0.00 10.40±0.04 0.613±0.0170.786±0.030 0.929±0.0690.817±0.0480.872±0.045
content-aware learner only 1.98±0.001.94±0.1210.40±0.04 0.613±0.0170.785±0.0310.929±0.0720.866±0.072 0.871±0.046
Trust test
in-sample F-test 1.98±0.002.01±0.00 10.37±0.000.628±0.0010.786±0.029 0.924±0.0640.814±0.0450.869±0.043
none (always act on values) 1.89±0.111.77±0.419.91±0.450.612±0.0050.767±0.0380.940±0.0800.882±0.0680.871±0.052
never passes (always anchored
action)
1.98±0.002.01±0.00 10.37±0.000.629±0.0010.787±0.0290.788±0.0290.789±0.0290.788±0.028
Anchored
action
draft average (𝑞=0) 1.62±0.051.19±0.028.69±0.090.648±0.0070.747±0.0320.905±0.0800.837±0.0730.842±0.049
uniform prior (𝛼0 =0.5) 1.83±0.021.92±0.019.71±0.020.632±0.008 0.777±0.0240.924±0.0720.855±0.0660.865±0.044
no online learning (𝑞fixed at𝛼 0) 1.99±0.01 1.94±0.0010.39±0.040.613±0.0180.784±0.0310.931±0.0700.862±0.0680.872±0.045
always the reference (𝑞=1)2.02±0.002.02±0.0010.48±0.050.605±0.0180.785±0.0340.933±0.070 0.864±0.0680.874±0.045
agent does when its values are not trusted, so they matter most on
PortBench and InvestorBench, where the values are rarely trusted.
We make the following observations. (1)The trust test matters
most on real markets.Without it, MemTrial acts on its learned values
whenever they favour a designed subset, on 25% of PortBench and
34.5% of InvestorBench test decisions, and loses 0.08 pp per month
on PortBench-Full, 0.24 pp on PortBench-Raw and 0.49 bp per day
on InvestorBench, with a much larger spread across seeds. In Plant-
edMem, removing the test leaves the core average unchanged and
gains 0.02 pp in the informative regime, where acting early pays off;
§4.5 shows that the test trades this small delay for protection when
experiences carry no signal. On ClassAlloc, where the test passes
on 15% of decisions, acting on the values does not pay either way:
without the test, MemTrial loses 0.001 pp, and the F-test, which
passes on 2% of decisions, gains 0.016 pp. (2)The test must look at
future dates, not past ones.An in-sample F-test of whether experi-
ences differed in the past leaves PortBench and the core regimes
nearly unchanged and never passes on InvestorBench (−0.03bp
per day), but it loses 0.05 pp in the informative regime: with 48 ex-
periences, each retrieved only occasionally, the F-test, which needs
repeated measurements of the same experience, passes on only
15% of decisions there, against 45% for the trust test. (3)Content-
aware value estimation helps when content is informative and costs
nothing otherwise.Without it, MemTrial trusts its values on only
22% of decisions in the informative regime and loses 0.05 pp. Us-
ing the content-aware learner alone, without learner selection, is
as good there but costs 0.07 pp on PortBench-Raw, with a larger
spread across seeds, because its chance forward scores pass the test
more often (1.1% against 0.3% of PortBench decisions); selecting the
learner by its forward score keeps the benefit and avoids the cost.
(4)When the values are not trusted, the agent must stay anchored to
the reference.Replacing the anchored blend by the draft average
costs 0.36 pp (Full), 0.82 pp (Raw), 1.70 bp per day (InvestorBench)
and 0.03 pp (PlantedMem, core), and learning the blend from a uni-
form prior (𝛼0 = 0.5) costs 0.14 pp (Full), 0.09 pp (Raw) and 0.68 bp
per day (InvestorBench). Always keeping the reference (𝑞= 1) is as
good as MemTrial in PlantedMem and slightly better on PortBench
and InvestorBench (by up to 0.04 pp per month and 0.08 bp per day),
because there the average draft never beats the reference; online
learning matters when the reference is weak (Appendix D.8). Clas-
sAlloc is such a case: there the drafts beat 1/𝑁 , so the draft average
would gain 0.035 pp per month and the uniform prior 0.019 pp,
whereas always keeping the reference loses 0.008 pp.
Baselines with the same anchor.Table D.5 gives every LLM-
based baseline the anchored action of MemTrial: on every date,
it deploys𝑞𝑡𝑥ref 𝑡 +( 1−𝑞𝑡)𝑥𝑡 , where𝑥𝑡 is the portfolio that the
baseline would deploy and𝑞𝑡 follows Eq. (11) on the baseline’s own
realized outcomes (𝛼0 = 0.9,𝜆0 = 4); holdings, fees and the timing
of outcomes are those of each benchmark. For Draft averaging, this
is exactly the variant whose test never passes. On PortBench and In-
vestorBench, the anchor helps every baseline, and all of them come
within 1% of MemTrial; on ClassAlloc, where the trusted decisions
of MemTrial lost to the anchored blend, all of them are ahead of it
(0.621–0.635% against 0.613% per month). No difference between
MemTrial and the best anchored baseline on a real benchmark is
significant (𝑝≥ 0.13, two-sided paired𝑡-test over test dates), and
Hedge with a prior weight of 0.9 on the reference does as well. In
PlantedMem, the anchor keeps the baselines close to the reference:
with signal, they earn 0.787–0.838% per month against 0.788% for
the reference, whereas MemTrial, which acts fully on its values
once they have predicted unseen dates, earns 0.932% per month,
11% more than the best of them (Counterfactual selection;𝑝< 0.001
over seeds), and 7.5% more with informative content. Without sig-
nal, the anchored baselines stay at the reference and MemTrial is
0.6% below them, the cost of its false passes.
D.6 Wealth over time, market phases and
survival
Wealth.For every method, seed and setting, the wealth path starts
at 1 and follows the net returns after the 15 bp trading fee, before
the risk penalty of the utility; we divide it by the wealth path of
1/𝑁 in the same setting. On InvestorBench and ClassAlloc, which
carry the holdings from one decision to the next, it is the value
of the account from each decision date to the next (on ClassAl-
loc, a decision is scored over the 20 sessions after it and held until
the next decision date). On PortBench, whose decisions each start
16

MemTrial: Learning When to Trust Memory
Table D.5: Every LLM-based baseline with the anchored action of MemTrial (Eq. (11); % per month, bp per day on InvestorBench;
mean± sd over seeds). With the same anchor, the baselines do as well as MemTrial on the real benchmarks; with signal in
PlantedMem, MemTrial earns 11% more than the best of them.
PlantedMem
Method PortBench-Full PortBench-Raw InvestorBench ClassAlloc no signal signal informative content
1/𝑁2.021±0.0002.021±0.00010.45±0.000.623±0.0000.575±0.0000.575±0.0000.575±0.000
MemTrial (ours)1.976±0.0052.007±0.00210.40±0.040.613±0.0170.784±0.0310.932±0.0700.862±0.068
Hedge, prior 0.9 on the reference 1.992±0.009 2.003±0.00310.41±0.01 0.627±0.0010.786±0.0290.787±0.0290.787±0.030
With the anchored action of MemTrial
Memory-free 1.985±0.0081.998±0.00410.34±0.020.630±0.001 0.789±0.0300.789±0.0320.788±0.030
Self-consistency 1.980±0.0222.000±0.00510.32±0.010.635±0.0020.788±0.032 0.788±0.0320.788±0.032
Similarity retrieval (top-2) 1.961±0.0212.003±0.01010.36±0.010.629±0.0060.787±0.0290.788±0.0300.790±0.031
Similarity retrieval (top-4) 1.984±0.0112.006±0.00310.34±0.030.627±0.0060.787±0.0290.787±0.0280.789±0.031
FinMem 1.981±0.0412.005±0.00110.35±0.000.621±0.0020.787±0.0300.796±0.0300.789±0.031
MemRL 1.963±0.0441.998±0.00710.36±0.030.625±0.0020.787±0.0300.792±0.0310.790±0.030
Reflexion 1.964±0.0421.999±0.00110.30±0.010.621±0.0060.789±0.0290.790±0.0290.790±0.029
ExpeL 1.971±0.0152.007±0.00310.34±0.010.622±0.0010.787±0.0290.803±0.0320.791±0.029
Uplift credit 1.969±0.0122.004±0.00310.35±0.010.628±0.0030.787±0.0300.804±0.0340.792±0.031
Counterfactual selection 1.970±0.0262.006±0.00910.34±0.010.629±0.0050.788±0.031 0.838±0.040 0.802±0.032
Draft averaging (= test never passes) 1.976±0.0052.007±0.00110.37±0.000.629±0.0010.787±0.0290.788±0.0290.789±0.029
Hedge 1.984±0.0062.013±0.000 10.39±0.010.626±0.0010.787±0.0300.788±0.0300.788±0.030
from the equal-weight portfolio, it compounds the net returns of
the 20-day decision periods. The net returns are those of the port-
folios deployed in the reported runs: evaluating these portfolios
reproduces every reported utility exactly, so the wealth paths need
no new LLM calls.Market phases.For each benchmark we form
the equal-weighted index of its equities (PortBench: the equities
in the date’s universe; InvestorBench: the four stocks; ClassAlloc:
the equities class) and callfallingevery phase from a peak of this
index to the following trough in which the index lost at least 5%; all
other periods arerising. This gives one falling phase on PortBench
(August to October 2023,−8.7%), one on InvestorBench (October
2020,−8.7%) and four on ClassAlloc, the largest of which is the
2022 bear market (−20.6%).Survival.A run survives at a given
shortfall if its wealth never fell further behind the wealth of 1/𝑁
than this shortfall at any time in the test period.
Figure D.1 shows the wealth relative to 1/ 𝑁 in every setting,
Figure D.2 the wealth itself, Figure D.3 InvestorBench with the
other LLMs and temperatures, and Figure D.5 ClassAlloc with the
other LLMs. All use gpt-4.1-mini unless stated and show the mean
over three seeds, with a band of± sd for MemTrial; shading marks
the falling phases and the dotted line the LLM’s knowledge cutoff,
as in Figure 3. Figures D.3 and D.5 show the balanced investor;
on InvestorBench, the experience pool, retrieval and test days are
those of the main run. Table D.6 gives the relative wealth at the end
of the test period and accumulated over the falling and the rising
phases, Table D.7 the share of runs whose wealth never fell further
behind that of 1/𝑁 than a given shortfall, with the median over runs
of the largest shortfall, and Table D.8 the cumulative net return,
annualized Sharpe ratio and maximum drawdown over the test
period, computed from the wealth paths of Figure D.2. In Tables D.6
and D.8, each seed averages the settings of a benchmark (PortBench:
two configurations and three investors; InvestorBench and ClassAl-
loc: eight LLMs and three investors); Table D.7 pools the 54 runs
of each seed over the three benchmarks. All three report the mean
± sd over the three seeds. On PortBench, the experience-learning
agents were ahead of 1/𝑁 in mid-2024 in the Full configuration; the
last test month (November 2024) reverses this: the equal-weighted
cryptocurrency class of the universe gained 129%, and 1/𝑁 , which
holds 10% in it for the balanced investor, gained 15%, whereas the
agents’ drafts held 0–7%. Without this month, Similarity retrieval
(top-4) (1.50% per month) and Hedge (1.49%) come out ahead of 1/𝑁
and MemTrial (1.46% each) on PortBench-Full; dropping any other
single test month leaves MemTrial the best LLM-based method on
both PortBench variants. On ClassAlloc, the memory-free LLM and
most memory-based methods end above 1/𝑁 for the balanced and
aggressive investors, with their gains made before the knowledge
cutoff of gpt-4.1-mini; after it, every LLM-based method trails 1/𝑁 ,
MemTrial the least for every investor.
Summary over all settings.Every method gains over the test
periods (for the balanced investor, 1/𝑁 ends at 1.61, 1.19 and 1.82
times its initial wealth on PortBench-Full, InvestorBench and Clas-
sAlloc), so we compare the methods by their wealth relative to 1/𝑁 .
Averaged over all settings, including every LLM, the experience-
learning agents fall behind 1/𝑁 on PortBench and InvestorBench
mostly while markets rise (by 9.8–11.5% and 2.0–4.1% over the ris-
ing phases), and on ClassAlloc they lose 1.5–3.5% against 1/𝑁 over
the falling phases, which include the 2022 bear market (Table D.6).
Over the falling phases of InvestorBench and ClassAlloc, MemTrial
loses less than the memory-free LLM and every experience-learning
agent (0.06% and 0.9%, against 0.38–0.65% and 1.5–3.5%). Its termi-
nal wealth is the highest of all LLM-based methods in 38 of the 39
PortBench and InvestorBench settings and within 1.4% of 1/𝑁 , and
its Sharpe ratio and maximum drawdown are the closest to those
of 1/𝑁 (Table D.8). On ClassAlloc, the memory-free LLM ends 0.3%
above 1/𝑁.
D.7 Hyperparameter analysis
We vary one hyperparameter at a time around the frozen setting:
the trust test (Figure D.4 and Table D.9), the number of retrieved
experiences𝑘 and the design (Table D.10), and the strength of the
17

Wu, Cai and Wang
2023 2024
−5
0
5
wealth vs. 1/𝑁 (%)
PortBench-Full, conservative
2023 2024
−10
0
10
PortBench-Full, balanced
2023 2024
−10
0
10
PortBench-Full, aggressive
2023 2024
−15
−10
−5
0
wealth vs. 1/𝑁 (%)
PortBench-Raw, conservative
2023 2024
−20
−10
0
PortBench-Raw, balanced
2023 2024
−15
−10
−5
0
PortBench-Raw, aggressive
Nov ’20 Feb ’21 May ’21
−3
−2
−1
0
wealth vs. 1/𝑁 (%)
InvestorBench, conservative
Nov ’20 Feb ’21 May ’21
−4
−2
0
InvestorBench, balanced
Nov ’20 Feb ’21 May ’21
−4
−2
0
InvestorBench, aggressive
2022 2024 2026
−5.0
−2.5
0.0
wealth vs. 1/𝑁 (%)
LLM cutoff
ClassAlloc, conservative
2022 2024 2026
−5
0
5
LLM cutoff
ClassAlloc, balanced
2022 2024 2026
−5
0
5
LLM cutoff
ClassAlloc, aggressive
1/𝑁 Memory-free FinMem MemRL Reflexion ExpeL MemTrial falling market (decline ≥5%)
1
Figure D.1: Wealth relative to 1/𝑁 in every setting. MemTrial stays within 2% of 1/ 𝑁 throughout, whereas the other agents fall
up to 21% behind.
Table D.6: Wealth relative to 1/𝑁 (%) at the end and by market phase. MemTrial stays within 1% of 1/ 𝑁 in every phase; the other
agents lose most in the rising phases of PortBench and InvestorBench.
Method PortBench InvestorBench ClassAlloc
End Falling Rising End Falling Rising End Falling Rising
Memory-free−11.10±0.46−0.65±0.58−10.50±0.61−3.15±0.36−0.65±0.06−2.52±0.39+0.31±0.97−1.59±0.25+2.08±0.89
FinMem−9.05±1.93 +0.75±1.48−9.80±0.96 −2.54±0.20−0.41±0.03−2.14±0.22−4.62±0.25−3.17±0.10−1.33±0.35
MemRL−11.44±2.82−0.93±0.38−10.59±2.64−2.46±0.10 −0.50±0.11−1.97±0.11 −2.50±0.22−3.53±0.20+1.35±0.07
Reflexion−11.42±1.16+0.11±1.31 −11.50±1.78−4.60±0.10−0.52±0.06−4.09±0.11−2.53±0.87−1.45±0.67 −0.98±0.71
ExpeL−11.29±0.88−0.05±1.03−11.27±0.83−2.75±0.16−0.38±0.03 −2.37±0.18−3.88±0.39−3.44±0.26+0.17±0.33
MemTrial (ours)−0.53±0.04+0.03±0.03−0.55±0.03−0.21±0.06−0.06±0.02−0.15±0.04−0.33±0.30 −0.94±0.15+0.64±0.18
Falling / rising periods 3 / 17 months 12 / 137 days 17 / 54 months
anchor (Appendix D.8, Table D.11). Tables report the mean± sd over
seeds, in % per month (bp per day on InvestorBench). In Table D.10,
Draftsis the number of drafts per decision; a draft is one LLM call on
InvestorBench and one run of the three-call agent on PortBench, so
the LLM cost grows in proportion. On the real benchmarks, drafts
were generated for all 16 subsets of the four retrieved experiences,
so every design with𝑘≤ 4is evaluated offline from these drafts,
without new LLM calls. In PlantedMem, drafts are resampled, which
also allows𝑘= 5and 6; these results come from a separate run on
50 test seeds (15–64) with common random numbers across designs,
in which the default scores 0.868% per month (0.87 on 100 seeds in
Table 3); they are shown with three decimals. Trust rates, with sd,
are in Table D.3.
18

MemTrial: Learning When to Trust Memory
2023 2024
1.0
1.2wealth (start = 1)
PortBench-Full, conservative
2023 2024
1.0
1.2
1.4
1.6
PortBench-Full, balanced
2023 2024
1.0
1.2
1.4
1.6
PortBench-Full, aggressive
2023 2024
1.0
1.2wealth (start = 1)
PortBench-Raw, conservative
2023 2024
1.0
1.2
1.4
1.6
PortBench-Raw, balanced
2023 2024
1.0
1.2
1.4
1.6
PortBench-Raw, aggressive
Nov ’20 Feb ’21 May ’21
1.00
1.05
1.10wealth (start = 1)
InvestorBench, conservative
Nov ’20 Feb ’21 May ’21
1.0
1.1
1.2
InvestorBench, balanced
Nov ’20 Feb ’21 May ’21
1.0
1.1
1.2
InvestorBench, aggressive
2022 2024 2026
1.00
1.25
1.50
1.75wealth (start = 1) LLM cutoff
ClassAlloc, conservative
2022 2024 2026
1.00
1.25
1.50
1.75
LLM cutoff
ClassAlloc, balanced
2022 2024 2026
1.00
1.25
1.50
1.75
LLM cutoff
ClassAlloc, aggressive
1/𝑁 Memory-free FinMem MemRL Reflexion ExpeL MemTrial falling market (decline ≥5%)
1
Figure D.2: Wealth in every setting (start = 1). MemTrial tracks 1/𝑁 ; on PortBench and InvestorBench, the others end below it.
Table D.7: Survival against 1/𝑁 (% of runs). MemTrial never
falls 5% behind 1/𝑁; the others do in 22–44% of runs.
Method Shortfall <2% Shortfall <5% Shortfall <10% Median largest shortfall (%)
Memory-free 27.8±3.777.8±3.7 94.4±0.0 3.15±0.19
FinMem 19.1±3.967.9±3.990.7±3.23.59±0.12
MemRL 31.5±4.9 74.7±1.193.2±1.13.04±0.26
Reflexion 14.2±4.355.6±1.988.9±3.74.60±0.24
ExpeL 26.5±2.169.8±3.983.3±3.23.01±0.36
MemTrial (ours) 93.2±1.1100.0±0.0100.0±0.00.20±0.01
We make the following observations. (1)The test level trades
protection against speed.Levels up to 0.05 give identical results on
PortBench, because at these levels the test passes on at most 0.3%
of PortBench decisions. At𝛼= 0.1and 0.2, chance forward scores
pass the test on 5% and 12% of PortBench decisions;𝛼= 0.1gains
0.03 pp on PortBench-Full but costs 0.03 pp on PortBench-Raw,
and𝛼= 0.2costs 0.03 and 0.08 pp, with a larger spread across
seeds. In PlantedMem, a looser test trusts the values earlier and
more often (on 28% of core decisions at 𝛼= 0.01against 41% at
𝛼= 0.2), which helps in the informative regime (0.84% against
0.88%). On InvestorBench, all levels stay within 0.05 bp per day of
each other. The frozen level𝛼= 0.05sits between these regimes.
(2)The minimum number of forward scores(5, 10 or 20) changes the
InvestorBench result by at most 0.03 bp per day and no other result
at two decimals. (3)More retrieved experiences help when experiences
matter, with diminishing returns per draft.In PlantedMem, the core
utility rises from 0.812% per month with𝑘= 2(4 drafts) to 0.868
with𝑘= 4(8 drafts), 0.896 with 𝑘= 5(16 drafts) and 0.909 with
𝑘= 6(32 drafts): going from 8 to 16 drafts adds 0.03 pp, and doubling
again to 32 drafts adds 0.01 pp. (4)At equal cost, the half fraction is
the better design, because it measures one more experience with the
same number of drafts. With 4 drafts,𝑘= 3in a half fraction beats
𝑘= 2in a full factorial (0.829% against 0.812%); with 8 drafts, 𝑘= 4
in a half fraction matches𝑘= 3in a full factorial (0.868% against
0.865%) and trusts its values more often (35% against 29%); with 16
drafts,𝑘= 5in a half fraction beats 𝑘= 4in a full factorial (0.896%
against 0.889%). (5)On the real benchmarks, where the values are
rarely trusted,𝑘 and the design barely matter on PortBench (1.95–
2.01% per month). On InvestorBench, every other design passes
the test more often (on 2–11% of decisions), on values that do not
carry over to the next day, and loses 0.13–0.44 bp per day against
19

Wu, Cai and Wang
Nov ’20 Feb ’21 May ’21
−6
−4
−2
0
2
wealth vs. 1/𝑁 (%)
gpt-4.1-mini
Nov ’20 Feb ’21 May ’21
gpt-4.1-nano
Nov ’20 Feb ’21 May ’21
gpt-5-mini (default T)
Nov ’20 Feb ’21 May ’21
Llama-3.3-70B
Nov ’20 Feb ’21 May ’21
−6
−4
−2
0
2
wealth vs. 1/𝑁 (%)
gpt-4.1-mini (T = 0.0)
Nov ’20 Feb ’21 May ’21
gpt-4.1-mini (T = 0.3)
Nov ’20 Feb ’21 May ’21
gpt-4.1-mini (T = 1.0)
Nov ’20 Feb ’21 May ’21
Gemini 2.5 Flash
Nov ’20 Feb ’21 May ’21
−6
−4
−2
0
2
wealth vs. 1/𝑁 (%)
Qwen3-235B
Nov ’20 Feb ’21 May ’21
DeepSeek-V3.1
Nov ’20 Feb ’21 May ’21
Claude Haiku 4.5
1/𝑁 Memory-free FinMem MemRL Reflexion ExpeL MemTrial falling market (decline ≥5%)
1
Figure D.3: InvestorBench with other LLMs and temperatures: wealth relative to 1/ 𝑁 . MemTrial stays within 1.2% of 1/𝑁 in
every configuration; the other agents end 1.5–6.7% behind.
Table D.8: Cumulative net return (CR, %), annualized Sharpe ratio (SR) and maximum drawdown (MDD, %). On every benchmark,
MemTrial has the highest Sharpe ratio and the smallest drawdown of the LLM-based agents.
Method PortBench InvestorBench ClassAlloc
CR SR MDD CR SR MDD CR SR MDD
1/𝑁53.1±0.01.72±0.005.7±0.018.1±0.02.87±0.005.4±0.082.0±0.0 1.22±0.0012.0±0.0
Memory-free 36.0±0.81.43±0.046.8±0.814.4±0.42.26±0.066.0±0.182.5±1.81.14±0.0212.7±0.3
FinMem 39.1±3.01.53±0.08 6.2±0.6 15.1±0.22.42±0.035.8±0.073.5±0.51.12±0.0013.4±0.0
MemRL 35.4±4.41.39±0.056.5±0.415.2±0.12.39±0.035.9±0.177.4±0.41.11±0.0013.5±0.3
Reflexion 35.4±1.81.43±0.096.8±0.812.6±0.12.02±0.015.9±0.077.4±1.61.14±0.0113.0±0.4
ExpeL 35.5±1.21.47±0.116.7±0.714.8±0.22.41±0.035.8±0.074.9±0.71.11±0.0113.4±0.3
MemTrial (ours)52.3±0.1 1.72±0.015.7±0.017.9±0.1 2.84±0.01 5.5±0.0 81.4±0.51.19±0.01 12.3±0.2
the default; the full factorial at 𝑘= 4, for example, doubles the
drafts and loses 0.41 bp per day. We therefore keep 𝑘= 4with
eight drafts: in PlantedMem its gain over the reference per draft
(0.011 pp) is close to the largest (0.012 pp, for𝑘= 3in a half fraction),
and on InvestorBench it is the best design. A larger𝑘 is worth its
cost only when experiences are known to matter. (6)The anchor
matters more than its exact strength(Table D.11). A uniform prior
(𝛼0 = 0.5) costs up to 0.18 pp on PortBench-Full, up to 0.29 pp
on PortBench-Raw and 0.40–0.74 bp per day on InvestorBench,
whereas with 𝛼0∈{ 0.9, 0.95} every𝜆0 stays within 0.06 pp per
month and 0.06 bp per day of the default; in PlantedMem, all twelve
settings give 0.86–0.87% per month on the core regimes.
D.8 Strength of the anchor
Table D.11 varies the prior weight 𝛼0 on the reference and the
regularization strength𝜆0 of Eq. (11) (mean± sd over seeds; % per
month, bp per day on InvestorBench; default𝛼0 = 0.9and 𝜆0 = 4).
Its last row is the extreme𝛼0 = 1, which always keeps the reference
when the values are not trusted. It is the best choice where 1/ 𝑁
cannot be beaten, 2.2%, 0.7% and 0.8% better than MemTrial on
PortBench-Full, PortBench-Raw and InvestorBench, but it cannot
move towards better drafts: it is 1.2% worse on ClassAlloc and 4.4%
worse in PlantedMem when 1/𝑁 is the reference (Table D.15). The
20

MemTrial: Learning When to Trust Memory
Table D.9: Sensitivity to the trust test. Test levels up to 0.05 give identical PortBench results; looser levels help consistently only
in the informative PlantedMem regime.
Hyperparameter Value PortBench-Full PortBench-Raw InvestorBench PlantedMem (core) PlantedMem (informative)
Test level𝛼
0.01 1.98±0.00 2.01±0.0010.37±0.000.87±0.040.84±0.07
0.02 1.98±0.00 2.01±0.0010.37±0.000.87±0.040.85±0.07
0.05 (default) 1.98±0.00 2.01±0.0010.40±0.04 0.87±0.040.86±0.07
0.12.01±0.051.98±0.04 10.42±0.090.87±0.050.87±0.07
0.2 1.94±0.051.93±0.1310.39±0.070.87±0.050.88±0.07
Minimum forward scores
51.98±0.002.01±0.0010.40±0.040.87±0.050.86±0.07
10 (default)1.98±0.002.01±0.0010.40±0.040.87±0.040.86±0.07
201.98±0.002.01±0.0010.37±0.000.87±0.040.86±0.06
Table D.10: Number of retrieved experiences𝑘 and the design. More experiences help when experiences matter, with diminishing
returns per draft; at equal cost, the half fraction is the better design.
𝑘Design Drafts PortBench-Full PortBench-Raw InvestorBench PlantedMem (core) PlantedMem (informative)
2 full factorial 41.98±0.012.01±0.0010.27±0.11 0.812±0.0430.798±0.042
3 half fraction 4 1.97±0.022.01±0.0010.14±0.210.829±0.0410.799±0.047
3 full factorial 81.98±0.012.01±0.009.96±0.360.865±0.0510.850±0.070
4 half fraction (default) 81.98±0.002.01±0.0010.40±0.040.868±0.0450.862±0.072
4 full factorial 16 1.97±0.001.95±0.119.99±0.340.889±0.0470.903±0.085
5 half fraction 16 – – – 0.896±0.044 0.914±0.078
6 half fraction 32 – – –0.909±0.0480.932±0.070
1.9
2.0utility
Full
Raw
PortBench
10.0
10.5
InvestorBench
0.82
0.86
PlantedMem (inform.)
0.01 .02 .05 0.1 0.2
0
10trust (%)
Full
Raw
0.01 .02 .05 0.1 0.2
0
1
2
0.01 .02 .05 0.1 0.2
40
60
trust-test level 𝛼 (dotted: default)
1
Figure D.4: Effect of the trust-test level𝛼 (top: utility; bottom:
trust rate). On real markets, a looser test acts on chance and
loses; in PlantedMem, it acts earlier on values that hold.
default𝛼0 = 0.9gives up at most 2.2% where the reference is strong
and keeps the ability to follow better drafts.
The best𝜆0 differs between the two PortBench configurations
(16 on Full, 1 on Raw), and the default is within 0.03 pp of the best
setting on both. A higher prior (𝛼0 = 0.95) would have done slightly
better on the real benchmarks, where the reference is strong, but
by the trade-off shown in §4.3 it would adapt more slowly when
the reference is weak.
Table D.11: Strength of the anchor (𝛼0 = 1: always the refer-
ence). A uniform prior (𝛼0 = 0.5) costs the most; with 𝛼0≥ 0.9,
every𝜆 0 stays close to the default.
𝛼0 𝜆0 PortBench- Full PortBench- Raw InvestorBench PlantedMem (core)
0.5 1 1.80±0.022.02±0.009.99±0.030.87±0.04
0.5 4 1.83±0.021.92±0.019.71±0.020.87±0.04
0.5 16 1.85±0.021.72±0.019.65±0.040.86±0.04
0.75 1 1.86±0.032.02±0.0010.29±0.050.87±0.04
0.75 4 1.92±0.011.98±0.0010.16±0.020.87±0.04
0.75 16 1.94±0.011.89±0.0010.12±0.010.87±0.04
0.9 1 1.92±0.032.02±0.0010.42±0.050.87±0.04
0.9 4 (default) 1.98±0.002.01±0.00 10.40±0.040.87±0.04
0.9 16 1.99±0.011.97±0.0010.39±0.040.87±0.04
0.95 1 1.95±0.022.02±0.0010.45±0.050.87±0.04
0.95 4 2.00±0.002.01±0.00 10.45±0.040.87±0.05
0.95 16 2.01±0.00 2.00±0.0010.46±0.04 0.87±0.05
1 –2.02±0.002.02±0.0010.48±0.050.87±0.05
D.9 Number of retrieved experiences by regime
Table D.12 breaks the PlantedMem part of Table D.10 down by
regime (% per month; mean± sd over test seeds 15–64, each av-
eraged over the three investors; trust rates in Table D.3). When
experiences carry no signal (first two columns), every design stays
within 0.01 pp of the reference, so a larger𝑘 adds no risk there; its
gains come entirely from the regimes in which experiences matter.
21

Wu, Cai and Wang
Table D.12: PlantedMem utility by regime for each 𝑘 and design (% per month). A larger 𝑘 gains only where experiences matter.
Design Drafts No influence Noise only𝛽=0.1𝛽=0.25𝛽=0.5Many exp. Informative Core avg.
Reference 8 0.782±0.0310.782±0.031 0.782±0.0310.782±0.0310.782±0.0310.782±0.0310.782±0.0310.782±0.031
𝑘=2, full factorial 40.784±0.0290.782±0.038 0.785±0.0290.804±0.0480.904±0.1300.782±0.0290.798±0.0420.812±0.043
𝑘=3, half fraction 40.784±0.0320.784±0.0420.787±0.0380.821±0.0610.970±0.1230.789±0.0360.799±0.0470.829±0.041
𝑘=3, full factorial 8 0.782±0.0280.778±0.0320.784±0.0310.904±0.0891.078±0.1540.812±0.0480.850±0.0700.865±0.051
𝑘=4, half fraction (default) 8 0.783±0.028 0.777±0.0370.794±0.0450.901±0.0841.085±0.1140.836±0.0790.862±0.0720.868±0.045
𝑘=4, full factorial 16 0.780±0.0300.778±0.0290.792±0.0490.950±0.0801.143±0.1340.869±0.0940.903±0.0850.889±0.047
𝑘=5, half fraction 16 0.780±0.0320.775±0.0340.800±0.054 0.956±0.081 1.170±0.110 0.873±0.075 0.914±0.078 0.896±0.044
𝑘=6, half fraction 32 0.783±0.029 0.776±0.0340.822±0.0730.981±0.0821.184±0.1260.921±0.0660.932±0.0700.909±0.048
D.10 PlantedMem by regime
Tables D.13–D.15 break the PlantedMem results down by regime
(mean± sd over the 100 test seeds, each averaged over the three
investors). The trust rate is the share of decisions on which a method
acts on its learned values, and the reference is the average of eight
memory-free drafts, except in Table D.15, where it is 1/𝑁.
When does MemTrial trust its values?Table D.13 shows how
often the trust test passes in each regime of PlantedMem. When
experiences carry no signal, MemTrial acts on its values on only
2–3% of decisions, below the nominal 5% level of a single test. The
trust rate rises with the influence of experiences, from 14% at𝛽= 0.1
to 64.5% at𝛽= 0.25and 85% at 𝛽= 0.5, and with 48 experiences it
rises from 26% to 45% when content becomes informative, because
the content-aware learner then predicts the contributions of rarely
seen experiences. On PortBench, the test passed on 1 of 360 test
decisions and on 14 of 1,008 decisions over all months, consistent
with Table 1, where the effect of experiences on PortBench decisions
is rarely detectable. On InvestorBench, it passed on only 0.3% of
decisions, even though experiences change most daily decisions
detectably: the values learned from past days do not carry over
to the following days, and the mean forward score of the learned
values, averaged over investors and seeds, is−0.07. The test thus
responds to whether learned values transfer to unseen dates, not
to whether experiences matter on a given date.
Where does MemTrial gain and where does it lose?Ta-
ble D.14 breaks the PlantedMem results down by regime. When
experiences carry no signal, acting on learned values is costly: with-
out its trust test, MemTrial falls 0.01–0.03 pp below the reference,
and Counterfactual selection falls up to 0.13 pp below it, whereas
the full MemTrial stays at the reference. When experiences matter,
MemTrial gains up to 0.30 pp over the reference, but it gives up 0.01–
0.03 pp to Counterfactual selection, because it waits for forward
evidence before acting; the exception is the informative regime,
where content-aware value estimation puts it 0.01 pp ahead. Aver-
aged over the core regimes, protection outweighs delay (+0.02pp,
𝑝= 0.001; Table 3). Outcome credit (MemRL†) never gains from
experiences, even at𝛽= 0.5, because its credit follows the market.
What if the reference is weak?On PortBench, InvestorBench
and PlantedMem, the reference is never beaten by the average
draft, so always keeping it (𝑞= 1) is at least as good as MemTrial;
on ClassAlloc, where the average draft beats 1/𝑁 by 0.03 pp per
month, it is 0.008 pp worse (Table D.4). To test the online learning
of the anchored action, we replace the reference in PlantedMem
with the 1/𝑁 portfolio, which ignores the investor’s risk aversion
and is about 0.18 pp per month worse than the average draft there.
Table D.15 shows that, if MemTrial always kept 1/𝑁 when its values
are not trusted, it would earn 0.71% per month on the core regimes.
The anchored action instead learns to move towards the drafts
(0.75%), and a uniform prior moves faster (0.81%). In every regime,
the learned blend is at least as good as always keeping 1/𝑁 . Never
acting on its values, MemTrial would earn only 0.62%, so with a
weak reference the learned values matter even more. The prior
weight𝛼0 therefore sets a trade-off: a high prior protects when the
reference is strong (Table D.11), and a low prior adapts faster when
it is weak.
D.11 ClassAlloc before and after the knowledge
cutoff
Table D.16 splits the ClassAlloc results at the knowledge cutoff
of gpt-4.1-mini (June 2024; % per month, mean ± sd over seeds,
averaged over the three investors). Before the cutoff, every LLM-
based method except FinMem and Reflexion beats 1/𝑁 , by up to
0.12 pp per month (Self-consistency); after it, every LLM-based
method trails 1/𝑁 , MemTrial the least (0.746% against 0.787%) and
the memory-free draft by 0.08 pp. As on the other benchmarks, out-
come credit tracks the market (Spearman correlation 0.97, Table 1),
and the retrieved experiences change the decision detectably in
53–57 of the 71 months. Over all 71 months, the memory-free draft
beats 1/𝑁 by 0.03 pp per month, but no form of memory improves
on it: retrieval, the experience-learning agents and the credit-based
learners earn 0.59–0.65%, against 0.66% for the memory-free draft
and 0.69% for Self-consistency (Table 3). For the memory-free draft,
the difference between the periods before and after the cutoff is
not significant (𝑝=0.36, Welch𝑡-test). The trust test of MemTrial
passed on none of the decisions of 2020, on 3% of those of 2021 and
on 13–33% of those of each later year, and on 0%, 39% and 4% of the
decisions of the three seeds. On the 93 decisions on which it passed,
the trusted draft earned0.05pp less (s.e.0 .07) than the anchored
blend it replaced, and more on 48% of them.
D.12 Other LLMs and temperatures
Table D.17 summarizes every configuration of §4.4: on Investor-
Bench, in bp per day (1/𝑁 earns 10.45 in every configuration), with
the experience pool, retrieval and test days of the main run; on Clas-
sAlloc, in % per month (1/𝑁 earns 0.623), where each LLM writes
its own warm-up lessons. The temperature is 0.7 unless stated, and
gpt-5-mini runs at the temperature fixed by its API.Best other LLM-
based methodis the best of the 12 LLM-based baselines; Improv. and
the trust rate are defined as in Table 3, and𝑝 is the𝑝-value of the
one-sided paired𝑡-test over test dates. Tables D.18 and D.19 give
22

MemTrial: Learning When to Trust Memory
Table D.13: Trust rate (%) by PlantedMem regime. MemTrial rarely trusts its values when experiences carry no signal and trusts
them more often the more experiences matter.
Trust rule No influence Noise only𝛽=0.1𝛽=0.25𝛽=0.5Many exp. Informative
MemTrial (trust test) 2.3±6.63.0±10.113.7±20.764.5±23.384.8±8.926.1±22.644.9±22.5
Per-experience learner only 1.5±5.12.0±8.310.5±18.061.4±24.083.5±10.122.0±20.722.0±20.7
In-sample F-test 2.4±6.72.1±7.18.1±13.752.4±22.981.7±10.514.8±17.715.1±17.8
Table D.14: Utility by PlantedMem regime (% per month). MemTrial stays at the reference when experiences carry no signal
and gains when they matter.
Method No influence Noise only𝛽=0.1𝛽=0.25𝛽=0.5Many exp. Informative
Reference (memory-free average)0.788±0.0320.788±0.0320.788±0.0320.788±0.0320.788±0.0320.788±0.0320.788±0.032
Outcome credit (MemRL†) 0.759±0.0970.658±0.0890.758±0.0900.755±0.0980.749±0.1440.760±0.0850.760±0.085
Counterfactual selection 0.768±0.0970.659±0.0870.805±0.0930.926±0.1001.101±0.1380.852±0.0780.852±0.078
MemTrial w/o trust test 0.776±0.0470.758±0.0560.803±0.059 0.924±0.092 1.094±0.131 0.843±0.061 0.882±0.068
MemTrial, never acting on its values0.788±0.0280.787±0.029 0.788±0.0280.788±0.0290.788±0.0290.789±0.0290.789±0.029
MemTrial (ours)0.787±0.030 0.782±0.0350.793±0.0430.912±0.0881.090±0.1240.821±0.0500.862±0.068
Table D.15: PlantedMem with 1/𝑁as the reference (% per month). The anchored blend learns to leave a weak reference.
Method No influence Noise only𝛽=0.1𝛽=0.25𝛽=0.5Many exp. Informative Core avg.
1/𝑁0.575±0.0000.575±0.0000.575±0.0000.575±0.0000.575±0.0000.575±0.0000.575±0.0000.57±0.00
Draft averaging0.782±0.0320.715±0.0520.777±0.0310.764±0.0440.719±0.0800.775±0.0410.775±0.041 0.75±0.03
MemTrial, always 1/𝑁when not trusted (𝑞=1) 0.578±0.0160.580±0.0210.596±0.0550.783±0.1241.030±0.1360.626±0.0730.700±0.0960.71±0.05
MemTrial, never acting on its values 0.633±0.0090.608±0.0170.630±0.0090.624±0.0140.611±0.0260.626±0.0130.626±0.0130.62±0.01
MemTrial, anchored (𝛼0 =0.9) 0.635±0.0150.612±0.0240.646±0.0470.805±0.114 1.033±0.133 0.669±0.0630.733±0.0850.75±0.05
MemTrial, uniform prior (𝛼0 =0.5) 0.735±0.022 0.675±0.041 0.736±0.039 0.852±0.1001.043±0.1300.751±0.055 0.797±0.0730.81±0.05
Table D.16: ClassAlloc before and after the knowledge cutoff
of gpt-4.1-mini (% per month). Most LLM-based methods beat
1/𝑁 before the cutoff; after it, all trail it, MemTrial the least.
Method All 71 months 50 months before cutoff 21 months after cutoff
1/𝑁0.623±0.0000.554±0.0000.787±0.000
Minimum variance 0.230±0.0000.178±0.0000.353±0.000
Memory-free 0.657±0.001 0.636±0.008 0.705±0.017
Self-consistency0.686±0.0070.672±0.0100.721±0.013
Similarity retr. (top-2) 0.649±0.0330.616±0.0430.728±0.008
Similarity retr. (top-4) 0.643±0.0390.621±0.0470.696±0.027
FinMem† 0.594±0.0170.538±0.0210.725±0.026
MemRL† 0.633±0.0120.612±0.0300.683±0.033
Reflexion 0.590±0.0610.545±0.0720.697±0.064
ExpeL 0.609±0.0060.593±0.0050.648±0.012
Uplift credit† 0.645±0.0220.617±0.0310.711±0.001
Counterfactual sel. 0.650±0.0330.632±0.0390.691±0.047
Draft averaging 0.651±0.0080.632±0.0070.696±0.012
Hedge 0.634±0.0080.601±0.0090.714±0.012
MemTrial (ours)0.613±0.0170.557±0.0090.746±0.050
MemTrial w/o trust test 0.612±0.0050.572±0.0300.707±0.061
every method on InvestorBench (the column for temperature 0.7
is the main run), and Table D.20 every method on ClassAlloc; all
report the mean± sd over seeds, averaged over the three investors.
In every InvestorBench configuration, the best LLM-based base-
line earns 8.97–9.71 bp per day, 1/𝑁 10.45 and MemTrial 9.84–10.54.
D.13 ClassAlloc with other LLMs
Table D.20 gives every method of Table D.17b on ClassAlloc, Fig-
ure D.5 the wealth relative to 1/𝑁 , and Table D.21 the results before
and after each LLM’s own knowledge cutoff (utility minus that
of 1/𝑁 , mean over seeds;Monthscounts the test months before
and after the cutoff). For Claude Haiku 4.5 we use the end of its
training data, July 2025 (its reliable-knowledge cutoff is February
2025); Qwen3-235B and DeepSeek-V3.1 have no published knowl-
edge cutoff. Each LLM writes its own warm-up lessons, which are
embedded and retrieved as in the main run. The memory-free draft
beats 1/𝑁 over the whole test period with four of the eight LLMs
(gpt-4.1-mini, gpt-5-mini, Qwen3-235B and Claude Haiku 4.5). Of
the six LLMs whose knowledge cutoff is published, it trails 1/ 𝑁
after the cutoff with five (by 0.06–0.09 pp per month), which is
what one would expect if the LLMs had seen the earlier outcomes
during pretraining; with Claude Haiku 4.5, it beats 1/𝑁 also in the
eight months after the cutoff (by 0.08 pp). MemTrial stays within
0.021 pp per month of 1/𝑁 with every LLM; with gpt-5-mini and
Qwen3-235B, whose memory-free drafts beat 1/𝑁 by the widest
margins, its anchor gives up most of their advantage.
D.14 Look-ahead checks
The LLMs were trained on text that may describe the test periods,
a source of look-ahead bias. We ran two checks on ClassAlloc, at a
total cost of USD 3.87.
Memorization probe.For each of the 129 ClassAlloc decision
dates (58 warm-up and 71 test months, July 2015 to March 2026),
we gave each LLM only the date and asked for the return of each
asset class over the 20 trading days for which a decision is held,
with no market data and no memory (prompt in Appendix G.2);
three draws per date, at the temperature of the runs. We compare
the answers with the realized returns before and after each LLM’s
23

Wu, Cai and Wang
Table D.17: Robustness to the LLM and its temperature, all configurations. MemTrial beats every LLM-based baseline in all
eleven InvestorBench configurations and stays within 0.021 pp of 1/𝑁with all eight LLMs on ClassAlloc.
LLM, temperature Memory-free Best experience- learning agent Best other LLM-based method MemTrial (ours) MemTrial w/o trust test Improv. (%,𝑝) Trust rate (%)
(a) InvestorBench (bp per day)
gpt-4.1-mini, 0 7.74±0.35ExpeL 9.46±0.09ExpeL 9.46±0.099.84±0.519.69±0.22 +4.0±6.0(0.32) 23.2±7.9
gpt-4.1-mini, 0.3 7.63±0.25ExpeL 9.40±0.15 ExpeL 9.40±0.15 10.54±0.329.33±0.28+12.1±4.0(0.09) 7.0±12.1
gpt-4.1-mini, 0.7 (main) 8.43±0.29ExpeL 8.93±0.32Hedge 8.97±0.2310.40±0.049.91±0.45 +16.4±3.2(0.12) 0.3±0.5
gpt-4.1-mini, 1.0 7.83±0.47ExpeL 9.51±0.45ExpeL 9.51±0.4510.36±0.0110.10±0.54 +9.0±4.8(0.15) 0.0±0.0
gpt-4.1-nano, 0.7 8.45±0.74MemRL 7.75±0.55Self-consistency 9.07±0.3910.30±0.06 * 9.22±1.25 +33.0±7.4(0.02) 2.1±3.6
gpt-5-mini, default 8.36±0.54MemRL 8.98±0.07Hedge 9.19±0.1110.29±0.129.48±0.79 +14.7±2.1(0.14) 2.3±0.9
Llama-3.3-70B, 0.7 8.34±0.39FinMem 9.18±0.37Counterfactual sel. 9.39±0.4410.38±0.04 10.41±0.16+13.1±4.0(0.10) 0.8±1.1
Qwen3-235B, 0.7 8.31±0.21MemRL 8.86±0.64Hedge 8.97±0.21 10.07±0.258.94±0.20+13.6±8.6(0.12) 9.2±10.3
DeepSeek-V3.1, 0.7 8.37±0.55ExpeL 9.71±0.14 ExpeL 9.71±0.14 10.33±0.129.57±0.27+6.4±2.3(0.13) 1.1±1.0
Gemini 2.5 Flash, 0.7 7.66±0.23FinMem 8.97±0.27FinMem 8.97±0.2710.36±0.009.53±0.47 +15.5±3.0(0.09) 0.0±0.0
Claude Haiku 4.5, 0.7 8.42±0.10FinMem 9.40±0.11FinMem 9.40±0.1110.35±0.039.48±0.69 +10.1±1.6(0.14) 1.3±1.8
(b) ClassAlloc (% per month)
gpt-4.1-mini (main) 0.657±0.001 MemRL 0.633±0.012Self-consistency0.686±0.0070.613±0.0170.612±0.005−3.2±1.4(0.65) 14.6±21.7
gpt-4.1-nano 0.587±0.007Reflexion 0.575±0.040Counterfactual sel.0.617±0.0160.609±0.0050.616±0.007 +5.9±7.8(0.26) 8.5±6.0
gpt-5-mini 0.713±0.013 ExpeL 0.690±0.013Self-consistency0.719±0.0120.643±0.0170.642±0.015−6.7±0.7(0.76) 16.3±27.8
Llama-3.3-70B 0.619±0.059 FinMem 0.589±0.015Memory-free 0.619±0.059 0.622±0.0000.622±0.013+5.6±2.5(0.26) 0.9±1.6
Qwen3-235B 0.688±0.022 MemRL 0.609±0.016Self-consistency0.698±0.0210.626±0.0010.640±0.015+2.8±2.7(0.38) 3.4±2.4
DeepSeek-V3.1 0.597±0.018Reflexion 0.624±0.049 Sim. retrieval (top-4)0.625±0.0160.607±0.0130.604±0.014−2.7±10.0(0.65) 12.8±11.7
Gemini 2.5 Flash 0.616±0.012ExpeL 0.613±0.010Sim. retrieval (top-2)0.656±0.0260.621±0.0100.625±0.039 +1.3±0.7(0.44) 21.9±26.4
Claude Haiku 4.50.668±0.020MemRL 0.637±0.006 Memory-free0.668±0.0200.629±0.0000.618±0.004−1.2±0.9(0.56) 0.0±0.0
Table D.18: InvestorBench with gpt-4.1-mini at four temperatures, all methods (bp per day). At every temperature, no LLM-based
baseline beats 1/𝑁and MemTrial is the best LLM-based method.
gpt-4.1-mini, temperature
Method 0 0.3 0.7 (main) 1.0
1/𝑁10.45±0.0010.45±0.00 10.45±0.0010.45±0.00
Minimum variance 5.53±0.005.53±0.005.53±0.005.53±0.00
Memory-free 7.74±0.357.63±0.258.43±0.297.83±0.47
Self-consistency 7.86±0.177.81±0.087.89±0.217.83±0.24
Similarity retrieval (top-2) 8.36±0.148.73±0.288.67±0.198.60±0.45
Similarity retrieval (top-4) 8.06±0.107.91±0.278.12±0.618.65±0.40
FinMem† 8.45±0.178.66±0.378.47±0.178.36±0.14
MemRL† 8.46±0.258.32±0.398.90±0.398.77±0.25
Reflexion 6.87±0.157.59±0.547.29±0.667.93±0.36
ExpeL 9.46±0.099.40±0.158.93±0.329.51±0.45
Uplift credit† 8.52±0.288.35±0.248.44±0.258.44±0.20
Counterfactual selection 8.50±0.078.39±0.128.54±0.268.60±0.65
Draft averaging 8.55±0.068.51±0.068.69±0.098.69±0.16
Hedge 8.70±0.078.69±0.128.97±0.238.96±0.10
MemTrial (ours)9.84±0.51 10.54±0.3210.40±0.04 10.36±0.01
MemTrial w/o trust test 9.69±0.229.33±0.289.91±0.4510.10±0.54
knowledge cutoff in two ways.Absolute recallis the correlation
over months between recalled and realized returns, averaged over
the four non-cash classes.Relative recallis the correlation after
removing each class’s mean and each month’s mean, that is, the
recall of which class did better than usual in which month, which
is what matters for beating 1/𝑁 . Table D.22 gives the mean± sd
over the three draws; each LLM has 102–121 dates before its cutoff,
warm-up months included, and 8–27 after it. Every LLM whose
cutoff is published recalls the outcomes before its cutoff (absolute
recall 0.10–0.63, relative recall 0.06–0.50) and hardly at all after it
(−0.16to +0.09and −0.10to +0.01). Gemini 2.5 Flash recalls the
most, and Qwen3-235B and DeepSeek-V3.1, whose cutoffs are not
published, have an absolute recall of 0.27 and 0.22 over all months.
The advantage of the memory-free draft before the cutoff does not
grow with recall: with Gemini 2.5 Flash, which recalls the most,
it beats 1/𝑁 by only 0.008 pp per month before the cutoff, against
0.157 pp with gpt-5-mini (Table D.21).
Dates hidden.We evaluated gpt-4.1-mini and gpt-5-mini on
ClassAlloc (three seeds each, with the two extra draws of Self-
consistency) with no calendar date shown to the LLM: the market
context omits its date line, the warm-up lessons are stored and
retrieved without their dates, and the ExpeL insight prompt lists
the lessons without their dates. Everything else is unchanged. The
lessons and reflections are written by the LLM from the dateless
context, and none of the 58 warm-up lessons of either run mentions
a year or a month. Table D.23 compares these runs with those that
show the dates (mean ± sd over seeds, averaged over the three
investors). Hiding the dates leaves the pattern of the memory-free
24

MemTrial: Learning When to Trust Memory
Table D.19: InvestorBench with eight LLMs, all methods (bp per day). With every LLM, no LLM-based baseline beats 1/ 𝑁 and
MemTrial beats every LLM-based baseline.
Method gpt-4.1-mini gpt-4.1-nano gpt-5-mini Llama-3.3-70B Qwen3-235B DeepSeek-V3.1 Gemini 2.5 Flash Claude Haiku 4.5
1/𝑁10.45±0.0010.45±0.0010.45±0.0010.45±0.0010.45±0.0010.45±0.0010.45±0.0010.45±0.00
Minimum variance 5.53±0.005.53±0.005.53±0.005.53±0.005.53±0.005.53±0.005.53±0.005.53±0.00
Memory-free 8.43±0.298.45±0.748.36±0.548.34±0.398.31±0.218.37±0.557.66±0.238.42±0.10
Self-consistency 7.89±0.219.07±0.398.31±0.318.26±0.228.37±0.178.63±0.517.92±0.238.48±0.07
Similarity retrieval (top-2) 8.67±0.196.89±0.928.41±0.178.90±0.288.15±0.448.66±0.478.50±0.418.98±0.12
Similarity retrieval (top-4) 8.12±0.617.71±0.668.46±0.248.51±0.148.00±0.328.55±0.458.22±0.088.83±0.15
FinMem† 8.47±0.177.47±0.728.87±0.229.18±0.378.59±0.488.94±0.358.97±0.279.40±0.11
MemRL† 8.90±0.397.75±0.558.98±0.079.10±0.348.86±0.648.84±0.558.35±0.229.38±0.31
Reflexion 7.29±0.666.58±0.945.91±1.458.33±0.616.10±1.138.24±0.226.57±0.829.05±0.68
ExpeL 8.93±0.327.38±0.418.82±0.517.79±0.198.29±0.279.71±0.148.72±0.219.11±0.14
Uplift credit† 8.44±0.256.62±0.558.37±0.339.04±0.298.38±0.328.82±0.308.44±0.188.71±0.20
Counterfactual selection 8.54±0.266.79±0.449.01±0.099.39±0.448.68±0.539.25±0.318.61±0.378.80±0.26
Draft averaging 8.69±0.098.42±0.108.80±0.119.25±0.048.56±0.099.14±0.138.57±0.078.93±0.04
Hedge 8.97±0.238.98±0.219.19±0.119.29±0.168.97±0.219.33±0.238.96±0.079.39±0.05
MemTrial (ours)10.40±0.04 10.30±0.06 10.29±0.12 10.38±0.0410.07±0.25 10.33±0.12 10.36±0.00 10.35±0.03
MemTrial w/o trust test 9.91±0.459.22±1.259.48±0.7910.41±0.16 8.94±0.209.57±0.279.53±0.479.48±0.69
Table D.20: ClassAlloc with eight LLMs, all methods (% per month). MemTrial stays within 0.021 pp of 1/ 𝑁 with every LLM; the
memory-free LLM beats 1/𝑁with four of them.
Method gpt-4.1-mini gpt-4.1-nano gpt-5-mini Llama-3.3-70B Qwen3-235B DeepSeek-V3.1 Gemini 2.5 Flash Claude Haiku 4.5
1/𝑁0.623±0.0000.623±0.0000.623±0.0000.623±0.0000.623±0.0000.623±0.0000.623±0.0000.623±0.000
Minimum variance 0.230±0.0000.230±0.0000.230±0.0000.230±0.0000.230±0.0000.230±0.0000.230±0.0000.230±0.000
Memory-free 0.657±0.001 0.587±0.0070.713±0.013 0.619±0.0590.688±0.022 0.597±0.0180.616±0.0120.668±0.020
Self-consistency0.686±0.0070.588±0.0140.719±0.0120.614±0.0170.698±0.0210.615±0.0240.618±0.0030.656±0.004
Similarity retrieval (top-2) 0.649±0.0330.557±0.0000.701±0.0190.602±0.0090.599±0.0060.603±0.0090.656±0.0260.640±0.006
Similarity retrieval (top-4) 0.643±0.0390.554±0.0190.655±0.0060.598±0.0050.631±0.0190.625±0.0160.586±0.0160.641±0.009
FinMem† 0.594±0.0170.532±0.0170.632±0.0250.589±0.0150.564±0.0060.570±0.0080.567±0.0260.608±0.008
MemRL† 0.633±0.0120.569±0.0300.661±0.0220.579±0.0240.609±0.0160.553±0.0150.598±0.0530.637±0.006
Reflexion 0.590±0.0610.575±0.0400.659±0.0130.560±0.0030.550±0.0690.624±0.049 0.585±0.0520.633±0.031
ExpeL 0.609±0.0060.475±0.0250.690±0.0130.565±0.0210.606±0.0120.597±0.0070.613±0.0100.524±0.017
Uplift credit† 0.645±0.0220.558±0.0020.677±0.0280.582±0.0070.640±0.0050.620±0.0220.617±0.0230.638±0.011
Counterfactual selection 0.650±0.0330.617±0.016 0.685±0.0040.604±0.0130.646±0.0070.622±0.0200.640±0.011 0.624±0.004
Draft averaging 0.651±0.0080.587±0.0030.677±0.0050.604±0.0110.652±0.0090.620±0.0110.622±0.0030.650±0.002
Hedge 0.634±0.0080.583±0.0020.665±0.0110.602±0.0100.632±0.0090.602±0.0070.604±0.0120.640±0.008
MemTrial (ours)0.613±0.0170.609±0.0050.643±0.0170.622±0.000 0.626±0.0010.607±0.0130.621±0.0100.629±0.000
MemTrial w/o trust test 0.612±0.0050.616±0.0070.642±0.0150.622±0.013 0.640±0.0150.604±0.0140.625±0.0390.618±0.004
Table D.21: ClassAlloc before and after each LLM’s knowledge
cutoff (utility minus that of 1/ 𝑁 , pp per month). With five
of the six LLMs whose cutoff is published, the memory-free
draft trails 1/𝑁after the cutoff.
Memory-freeMemTrial (ours)
LLM Cutoff Months before after before after
gpt-4.1-mini Jun 2024 50/21+0.082−0.082+0.003−0.041
gpt-4.1-nano Jun 2024 50/21−0.018−0.078−0.018−0.007
gpt-5-mini May 2024 49/22+0.157−0.059+0.040−0.024
Llama-3.3-70B Dec 2023 44/27+0.047−0.087+0.005−0.009
Qwen3-235B –
DeepSeek-V3.1 –
Gemini 2.5 Flash Jan 2025 57/14+0.008−0.069+0.001−0.014
Claude Haiku 4.5 Jul 2025 63/8+0.040+0.079+0.005+0.013
draft intact: with gpt-4.1-mini, it beats 1/𝑁 by 0.13 pp per month
before the cutoff and trails it by 0.10 pp after (0.08 and 0.08 with
the dates shown); with gpt-5-mini, by 0.14 and 0.07 pp (0.16 and
Table D.22: Memorization probe: correlation of the asset-class
returns that each LLM recalls from a date alone with the
realized ClassAlloc returns. Every LLM recalls the outcomes
before its knowledge cutoff, and hardly any after it.
Absolute recall Relative recall
LLM Cutoff before after before after
gpt-4.1-mini Jun 2024+0.21±0.02−0.05±0.12+0.19±0.01−0.02±0.03
gpt-4.1-nano Jun 2024+0.10±0.040.00±0.04+0.06±0.06−0.10±0.09
gpt-5-mini May 2024+0.22±0.06−0.04±0.09+0.20±0.04−0.10±0.13
Llama-3.3-70B Dec 2023+0.40±0.09+0.09±0.15+0.36±0.08+0.01±0.12
Qwen3-235B –+0.27±0.03–+0.21±0.05–
DeepSeek-V3.1 –+0.22±0.09–+0.19±0.05–
Gemini 2.5 Flash Jan 2025+0.63±0.03−0.07±0.02+0.50±0.02−0.09±0.06
Claude Haiku 4.5 Jul 2025+0.27±0.01−0.16±0.07+0.27±0.01−0.07±0.10
0.06). Over all 71 test months, it beats 1/𝑁 by 0.06 and 0.07 pp (0.03
and 0.09 with the dates shown). MemTrial stays within 0.02 pp per
25

Wu, Cai and Wang
2022 2024 2026
−10
0
10
wealth vs. 1/𝑁 (%)
LLM cutoff
gpt-4.1-mini
2022 2024 2026
LLM cutoff
gpt-4.1-nano
2022 2024 2026
LLM cutoff
gpt-5-mini
2022 2024 2026
LLM cutoff
Llama-3.3-70B
2022 2024 2026
−10
0
10
wealth vs. 1/𝑁 (%)
Qwen3-235B
2022 2024 2026
DeepSeek-V3.1
2022 2024 2026
LLM cutoff
Gemini 2.5 Flash
2022 2024 2026
LLM cutoff
Claude Haiku 4.5
1/𝑁 Memory-free FinMem MemRL Reflexion ExpeL MemTrial falling market (decline ≥5%)
1
Figure D.5: ClassAlloc with other LLMs: wealth relative to 1/ 𝑁 . MemTrial stays within 3% of 1/𝑁 with every LLM, whereas the
memory-free LLM and the other agents move up to 14% away.
0.0
0.5
recall of dated
outcomes (corr.)
before the LLM’s cutoff after dates hidden
gpt-4.1-
mini
gpt-4.1-
nano
gpt-5-
mini
Llama-
3.3-70B
Gemini
2.5 Flash
Claude
Haiku 4.5
−0.1
0.0
0.1
memory-free draft
minus 1/𝑁 (pp/month)
1
Figure D.6: ClassAlloc at each LLM’s knowledge cutoff. The
LLMs recall dated outcomes from before their cutoffs, but
hiding the dates does not remove the memory-free draft’s
advantage before the cutoff.
month of 1/𝑁 (+0.006with gpt-4.1-mini and −0.017with gpt-5-
mini; trust rates 0.0% and 6.6%) and, after the cutoff, trails it by 0.02
and 0.03 pp, against 0.10 and 0.07 pp for the memory-free draft.
Figure D.6 brings these checks together with Table D.21. The
LLMs thus recall dated market outcomes, but the advantage of the
memory-free draft before the cutoff does not depend on being told
the date. It may come from recognizing a period from the returns
shown, or from allocations that happened to suit the markets of
2020–2024. Either way, this effect applies to all LLM-based methods
alike, and PlantedMem is free of it.
D.15 PortBench after the knowledge cutoff
To test on months that gpt-4.1-mini, the LLM of the PortBench runs,
cannot have seen, we extended the monthly PortBench stream with
the decision dates that follow 2024-12-02 under the same calendar
rule (the first trading day of each month; a month is skipped when
its 20-day holding window would overlap the previous one). This
gives twelve dates from 2025-01-02 to 2026-02-02; March 2025,
December 2025 and March 2026 are skipped by the overlap rule,
and April 2026 has no complete holding window before the data end
on 2026-04-16. Everything else is identical to the original months:
the experience pool and the FinMem and MemRL modules (which
receive no feedback after July 2019), the 19 drafts per date, both
configurations, gpt-4.1-mini at temperature 0.7, three seeds, and the
code that builds the inputs and runs the agents, which was reused
unchanged. Before any new month was run, the inputs of all 59
original months were rebuilt with the same code and compared
byte by byte with the frozen inputs, including the hash of every
first LLM request; they were identical. The six Reflexion chains
continue from their state after 2024-12-02. The evaluation reuses
the code of the main results, run forward over all 71 dates without
re-tuning, and reproduces the 2019–2024 results exactly.
The publisher’s price files have gaps in this period: 18 large eq-
uities (including AAPL, MSFT and NVDA) have no prices from
10 December 2024 to 24 January 2025 and after 19 February 2026,
MATIC-USD ends on 24 March 2025 but remains in the agent’s
market view until June 2025, and INDS has no price on 24 October
2025. As for December 2024 in the original months, a month in
which any execution held an asset without a price is dropped for
that configuration. This removes six of the twelve months (Janu-
ary, April, May, June and October 2025, and February 2026) and
26

MemTrial: Learning When to Trust Memory
Table D.23: ClassAlloc with every calendar date hidden from the LLM (utility minus that of 1/ 𝑁 , pp per month). Hiding the
dates does not remove the memory-free draft’s advantage before the knowledge cutoff.
gpt-4.1-mini gpt-5-mini
dates shown dates hidden dates shown dates hidden
Method before after before after before after before after
Memory-free+0.082±0.008 −0.082±0.017+0.127±0.017−0.099±0.027+0.157±0.020 −0.059±0.025+0.136±0.038 −0.066±0.006
Self-consistency+0.118±0.010−0.066±0.013+0.125±0.030 −0.104±0.012+0.160±0.013−0.048±0.016+0.118±0.028−0.068±0.015
FinMem† −0.016±0.021−0.062±0.026 −0.047±0.029−0.076±0.003+0.019±0.025−0.013±0.045 −0.024±0.016−0.088±0.035
MemRL† +0.058±0.030−0.104±0.033+0.088±0.032−0.093±0.050+0.077±0.046−0.048±0.034+0.077±0.049−0.012±0.041
Reflexion−0.009±0.072−0.090±0.064−0.001±0.095−0.049±0.036+0.066±0.026−0.032±0.096+0.051±0.014−0.093±0.019
ExpeL+0.039±0.005−0.140±0.012+0.009±0.041−0.015±0.009+0.089±0.018+0.017±0.004+0.033±0.032−0.134±0.025
Draft averaging+0.077±0.007−0.091±0.012+0.087±0.003−0.100±0.006+0.100±0.006−0.049±0.007+0.107±0.004−0.020±0.014
Counterfactual selection+0.078±0.039−0.096±0.047+0.063±0.034−0.083±0.016+0.118±0.005−0.064±0.003+0.140±0.014+0.008±0.037
MemTrial (ours)+0.003±0.009−0.041±0.050+0.016±0.000−0.017±0.001 +0.040±0.038−0.024±0.029−0.010±0.047−0.033±0.015
leaves 2025-02-03, 2025-07-01, 2025-08-01, 2025-09-02, 2025-11-03
and 2026-01-02 for both configurations. The new runs cost USD
9.29 for 1,368 executions and USD 0.48 for the Reflexion chains.
Table D.24 reports the six new months and all eleven test months
after the knowledge cutoff of gpt-4.1-mini (June 2024), averaged
over the three investors. Over the eleven months, MemTrial is the
best LLM-based method on both configurations and stays close to
1/𝑁 (0.14 and 0.01 pp per month below it), while the other LLM-
based methods trail 1/𝑁 by 0.36–1.57 pp; its values never passed the
trust test after the cutoff. In the six new months alone, the memory-
free draft of PortBench-Full beats 1/𝑁 by 0.80 pp per month, and
MemTrial, still anchored at 1/𝑁 , gains only 0.06 pp; on PortBench-
Raw, every LLM-based method is within 0.17 pp of 1/𝑁 . With six
months, no difference involving MemTrial is significant.
E Case Study: Two Decisions in the 2022 Bear
Market
This appendix follows MemTrial through two monthly decisions
on ClassAlloc (balanced investor), on 1 April and 1 September
2022. Both lie in the largest falling phase of the test period, in
which the equal-weight equity index lost 21% between January and
the end of September 2022 (Appendix D.6). The retrieved lessons
depend only on the date, so all seeds see the same four lessons; the
drafts, contributions and learned values differ by seed. In seed 1
the trust test passed on 1 April and narrowly failed on 1 September
(𝑝= 0.058); in seeds 0 and 2 it passed on neither date. The two dates
thus show one decision that acted on the learned values and one
that kept the anchored action. Table E.1a lists the eight designed
drafts of seed 1 on each date: the lessons each draft was given, its
weights in % (Eq. equities, Bd. bonds, Cm. commodities, RE real
estate) and its utility in % over the following 20 trading days, with
the deployed draft in bold (on 1 September, seed 1 deployed the
anchored blend) and, in the last row, the realized return of each class
over these 20 days. Table E.1b gives the contributions (Contr.) and
learned values of the retrieved lessons in seed 1, in pp. Table E.1c
gives the trust test and the action in each seed: the number 𝑛 of
forward scores, their mean ¯𝜌, the𝑝-value of the test, the action and
its utility in %, with trusted decisions in bold; the column 1/𝑁 gives
the utility of moving to 1/𝑁 from the seed’s holdings, which differs
slightly across seeds because of trading costs.
Retrieved lessons.Each lesson was written by the agent after
one of its warm-up decisions, and its label gives the month of that
decision. On 1 April 2022 the agent retrieved L18/04, L16/08, L17/05
and L15/12, and on 1 September L18/04, L16/08, L19/10 and L17/05.
L15/12 In December 2015, equities and real estate showed strong
recent gains with moderate volatility, while commodities declined
sharply. I overweighted equities and real estate, avoided commodi-
ties, and held cash. Despite this, bonds and real estate declined
significantly, hurting returns. In similar scenarios, diversify more
cautiously, temper bond exposure during rising volatility, and avoid
complacency from recent positive trends.
L16/08 In August 2016, equities and bonds showed steady gains with
low volatility, while commodities declined sharply and real estate
dipped despite strong prior returns. I overweighted equities and
real estate, underweighted commodities and cash. The portfolio
outperformed due to equities and bonds. In similar conditions,
maintain exposure to stable asset classes and reduce commodities
when short-term momentum weakens.
L17/05 In May 2017, equities and real estate showed strong recent
gains and moderate volatility, while commodities lagged with neg-
ative returns and high volatility. I overweighted equities and real
estate, underweighted commodities, and outperformed the equal-
weight portfolio. In similar conditions, favor assets with positive
momentum and manageable volatility, reducing exposure to weak,
volatile sectors like commodities.
L18/04 In April 2018, equities showed recent weakness but strong
6-month gains; bonds were stable with low volatility; commodi-
ties mildly positive; real estate mixed signals. I favored equities
and bonds over cash, yielding a slightly better return than equal
weights. In similar conditions, maintain diversified exposure but
overweight assets with solid medium-term momentum and man-
ageable volatility for balanced growth.
L19/10 In October 2019, real estate and equities showed strong recent
returns with moderate volatility, while bonds declined. Allocating
higher weights to real estate (35%) and equities (30%) capitalized on
momentum, delivering a portfolio return above the equal-weight
benchmark. In similar cases, emphasize assets with strong momen-
tum and moderate risk, but maintain diversification to manage
downside risks.
1 April 2022.Equities had fallen 5.4% over three months but
risen 3.2% in the last month, and commodities had risen 21.6% over
three months. Three of the lessons (L18/04, L16/08 and L17/05)
describe months in which overweighting assets with positive mo-
mentum paid off; L15/12 describes one in which it did not and
27

Wu, Cai and Wang
Table D.24: PortBench after the knowledge cutoff (% per month). Over the eleven months after the cutoff, MemTrial is the best
LLM-based method and stays close to 1/𝑁; in the six new months, the memory-free draft beats 1/𝑁on PortBench-Full.
New months (2025–2026) All months after the cutoff
Method Full Raw Full Raw
Rule-based portfolios
1/𝑁1.025±0.0001.025±0.0002.075±0.0002.075±0.000
Minimum variance 0.029±0.0000.029±0.0000.078±0.0000.078±0.000
LLM agents without experience learning
Memory-free 1.825±0.228 1.055±0.1031.290±0.2771.363±0.053
Self-consistency1.867±0.0001.058±0.0001.328±0.0001.367±0.000
Similarity retrieval (top-2) 1.131±0.3511.059±0.1410.883±0.2991.265±0.229
Similarity retrieval (top-4) 1.350±0.3531.002±0.0691.007±0.2831.211±0.044
Experience-learning agents
FinMem 1.071±0.2930.874±0.2030.691±0.3471.183±0.104
MemRL 1.358±0.6761.191±0.1470.916±0.3431.365±0.050
Reflexion 0.869±0.0921.091±0.066 0.502±0.1851.404±0.153
ExpeL† 1.197±0.1030.920±0.1551.033±0.1741.270±0.152
Credit-based and ensemble learners
Uplift credit† 1.034±0.5281.051±0.0420.598±0.2321.425±0.237
Counterfactual selection 1.794±0.3671.024±0.1821.217±0.2421.542±0.423
Draft averaging 1.437±0.1091.004±0.0331.039±0.0471.413±0.115
Hedge 1.499±0.1301.029±0.0231.234±0.0901.711±0.032
MemTrial (ours)1.086±0.0141.027±0.0001.939±0.011 2.064±0.002
Improv. (%,𝑝)−20.1±49.7(0.61)−13.8±12.3(0.64)+87.8±17.9(0.12)+47.0±10.9(0.24)
MemTrial−1/𝑁+0.061±0.014+0.001±0.000−0.135±0.011−0.011±0.002
Trust rate of MemTrial (%) 0.0 0.0 0.0 0.0
Table E.1: Case study on ClassAlloc (balanced investor). The contributions separate the lessons although every draft lost money;
in seed 1, acting on the values cost 1.66 pp in April, and keeping the anchored action gave up 2.02 pp in September.
(a)
1 April 2022 1 September 2022
Lessons in the draft Eq. Bd. Cm. RE Cash Utility Lessons in the draft Eq. Bd. Cm. RE Cash Utility
none 35 10 25 20 10−4.63 none 15 35 15 15 20−5.43
L18/04, L16/08 35 10 20 25 10−5.14 L18/04, L16/08 15 30 10 15 30−5.05
L18/04, L17/05 35 10 15 30 10−5.67 L18/04, L19/10 10 30 10 10 40−3.89
L16/08, L17/05 35 15 10 30 10−6.02 L16/08, L19/10 15 25 10 15 35−4.81
L18/04, L15/12 35 15 15 25 10−5.48L18/04, L17/05 15 35 10 15 25−5.29
L16/08, L15/12 35 15 10 25 15−5.58 L16/08, L17/05 15 35 10 15 25−5.29
L17/05, L15/12 35 10 15 30 10−5.67 L19/10, L17/05 15 15 20 15 35−4.64
all four 35 10 20 25 10−5.14 all four 15 25 10 15 35−4.81
anchored blend 19 21 19 19 21−5.91
1/𝑁20 20 20 20 20−3.83 1/𝑁20 20 20 20 20−6.06
Class return (%)−8.1−4.8 2.2−7.5 0.0 Class return (%)−9.5−4.3−1.8−12.3 0.1
(b)
1 Apr. 1 Sep.
Lesson Contr. Value Contr. Value
L15/12−0.11 +0.004 – –
L16/08−0.11−0.015−0.18−0.016
L17/05−0.42−0.002−0.21−0.002
L18/04 +0.12 +0.004 +0.28 +0.003
L19/10 – – +0.73 +0.005
(c)
Date Seed𝑛 ¯𝜌 𝑝Action Utility 1/𝑁
1 Apr. 0 18 0.17 0.123 anchored,𝑞=0.835−4.08−3.82
111 0.24 0.045 draft L18/04, L15/12−5.48−3.83
2 15 0.13 0.163 anchored,𝑞=0.835−4.10−3.83
1 Sep. 0 22 0.07 0.286 anchored,𝑞=0.885−5.84−5.99
1 16 0.17 0.058 anchored,𝑞=0.875−5.91−6.06
2 18 0.03 0.421 anchored,𝑞=0.875−5.79−5.99
warns against complacency after recent gains. All eight drafts of
seed 1, including the one without lessons, put 35% in equities (1/𝑁 :
20%) and 20–30% in real estate (Table E.1a), so this tilt comes from
the LLM’s reading of the market rather than from the lessons. The
lessons changed the drafts only slightly, and mostly for the worse:
three of the four contributions are negative, and the drafts that used
L17/05 earned 0.42 pp less on average than those that did not. The
11 forward scores of seed 1 so far had a mean of 0.24 and passed
the trust test (𝑝= 0.045), so MemTrial deployed the draft with the
highest total learned value (L18/04 and L15/12). Equities then fell
8.1% and real estate 7.5%, and the decision earned−5.48%, against
−3.83% for 1/𝑁 . In seeds 0 and 2 the test did not pass ( 𝑝= 0.12
and 0.16), and the anchored action, with a weight of 0.835 on 1/𝑁 ,
earned−4.08% and−4.10%.
28

MemTrial: Learning When to Trust Memory
1 September 2022.Every risky class had lost money over the
past one, three and six months, and all eight drafts of seed 1 were
defensive, with 10–15% in equities and 20–40% in cash. The drafts
that used L19/10 held 35–40% in cash, against 20–30% for those
that did not, and L19/10 had the largest contribution (+0.73pp). In
seed 1 the test narrowly failed (𝑝= 0.058; 16 forward scores, mean
0.17), so MemTrial kept the anchored action, which put a weight of
0.875 on 1/𝑁 and earned−5.91%, against−6.06% for 1/𝑁 ; the draft
it would have deployed (L18/04 and L19/10: 40% cash, 30% bonds,
10% equities) earned−3.89%. In seeds 0 and 2 (𝑝= 0.29and 0.42),
the anchored action earned−5.84% and−5.79%.
What the case shows.First, contributions are measured on the
same date, so the part of the outcome that all drafts share cancels:
on both dates every draft had a utility between−6.1% and−3.8%,
which outcome credit would charge to every lesson used, yet the
contributions separate the lessons by tenths of a pp. Second, the
contributions are noisy, so the learned values are small: L18/04
helped on both dates (+0.12and+0.28pp) and L17/05 hurt on both
(−0.42and −0.21pp), but after shrinkage all values in seed 1 are
below 0.02 pp in absolute value, so the deployed draft is decided by
small differences. Third, the trust test decides whether MemTrial
takes on the drafts’ market exposure: in April, when every draft
overweighted equities before a fall, acting on the values cost 1.66 pp
against 1/𝑁 ; in September, when every draft was defensive, the test
narrowly failed and the anchored action gave up the 2.02 pp by
which the selected draft beat it. Over all 71 months, acting on the
values did not pay on ClassAlloc: on the 93 decisions (all investors
and seeds) on which the test passed, the trusted draft earned0.05pp
less (s.e.0.07) than the anchored blend it replaced, and the variant
whose test never passes is 0.016 pp per month better (Figure 4).
Keeping part of the anchor even on trusted decisions is a natural
extension (Appendix H).
F Algorithms
Algorithm F.1 gives the steps of MemTrial on one decision date
(§3.6). Algorithm F.2 expands its value estimation, and Algorithm F.3
its trust test and anchored action.
G LLM Prompts
This appendix gives the prompts used on the three real benchmarks,
copied from the logged requests. Text in angle brackets is filled in
at run time, and [...] marks lines omitted here. On each benchmark,
all LLM-based methods use the same prompts and differ only in
the memory block that follows the market context (Table G.1); the
other LLMs of §4.4 receive the same prompts unchanged. The drafts
of all 16 subsets of the four retrieved lessons are logged on every
date and seed, so the methods in the second row of Table G.1 differ
only in which draft they deploy or how they combine the drafts.
On InvestorBench and ClassAlloc, a draft is one chat completion
with a system and a user message, and an invalid reply is answered
once with a retry message; on PortBench, a draft is one run of the
benchmark’s three-stage agent, without retries.
Algorithm F.1MemTrial at decision date𝑡
Input:state𝑠 𝑡 ; retrieved experiences𝑅𝑡 =(ℎ 1,...,ℎ 𝑘); designD(8
subsets of𝑅𝑡 ); reference𝑥 ref; contributions of past dates; forward
scores; FTRL statistics
Act, before the outcome
1:foreach𝑆∈Ddo
2:draft𝑥 𝑆∼𝜋(·|𝑠 𝑡,𝑆)⊲8 drafts in parallel
3:fit the content-aware and the per-experience value models on past
dates⊲Eqs. (5)–(7)
4:predict ˆ𝑣𝑗 for everyℎ 𝑗∈𝑅 𝑡 with both models; keep both predictions
for scoring
5:𝑆 ∗ =arg max𝑆∈D ˝ 𝑗∈𝑆 ˆ𝑣𝑗 for the selected model⊲Eq. (10)
6:ifthe trust test passes (𝑛≥10and𝑝 𝑡 <𝛼, Eq. (9)) and ˝ 𝑗∈𝑆∗ ˆ𝑣𝑗 >0
then
7:deploy𝑥 𝑡 =𝑥𝑆∗ ⊲trusted
8:else
9:deploy𝑥 𝑡 =𝑞𝑡𝑥 ref 𝑡 +(1−𝑞 𝑡) ¯𝑥𝑡 , with𝑞𝑡 from Eq. (11)⊲anchored
Learn, once the outcome is realized
10:𝑈(𝑆)=𝑢 𝑡(𝑥𝑆)for𝑆∈D; contributions𝑐 𝑗 (Eq. (3)); centred𝑦 𝑗
(Eq. (4))
11:forward score𝜌 𝑡 of each model (Eq. (8)); update the FTRL statistics of
Eq. (11)
Algorithm F.2Value estimation (line 3 of Algorithm F.1)
Input:centred contributions𝑦 𝑠,𝑗 of past dates, each with the experience
it belongs to; content features𝑧ℎ; grid𝐺of(𝜎 2 𝛽,𝜏 2)
1:foreach experienceℎmeasured on𝑛 ℎ≥1past datesdo
2:𝑚 ℎ←mean of its centred contributions
3:𝜎 2←pooled within-experience variance of the centred contributions
4:per-experience model:𝜎 2 𝛽 =0,𝜏 2 =arg max𝐺 of the marginal
likelihood⊲Eq. (6)
5:content-aware model:(𝜎 2 𝛽,𝜏 2)=arg max 𝐺 of Eq. (6)
6:foreach modeldo
7: ˆ𝑣←(𝜎 2 𝛽𝑍𝑍⊤+𝜏 2𝐼)𝐾−1𝑚; ˆ𝛽←𝜎 2 𝛽𝑍⊤𝐾−1𝑚⊲Eq. (7)
8:prediction for a retrieved experienceℎ: ˆ𝑣ℎ if𝑛ℎ≥1, else𝑧 ⊤ ℎ ˆ𝛽(0 for
the per-experience model)
Output:the predictions of both models
Algorithm F.3Trust test and anchored action (Algorithm F.1)
Input:forward scores of both models; utilities of the blends of earlier
dates
1:selected model←per-experience model until both models have≥10
forward scores, then the model with the higher mean forward score
2:𝑛, ¯𝜌,𝑠𝜌← number, mean and sd of the selected model’s forward scores
3:𝑝←Pr 𝑇𝑛−1≥ ¯𝜌/(𝑠𝜌/√𝑛) ⊲Eq. (9)
4:𝑆 ∗←arg max𝑆∈D ˝ 𝑗∈𝑆 ˆ𝑣𝑗 , ties towards fewer experiences⊲Eq. (10)
5:trusted←(𝑛≥10)∧(𝑝<𝛼)∧ ˝ 𝑗∈𝑆∗ ˆ𝑣𝑗 >0 
6:ifnot trustedthen
7:𝑞 𝑡←arg max𝑞 mean𝑠<𝑡𝑢𝑠
𝑞𝑥 ref 𝑠 +(1−𝑞) ¯𝑥𝑠 −𝜆𝑛KL(𝑞∥𝛼 0)
over𝑞∈{0,0.005,...,1}⊲Eq. (11)
8:after the outcome of date𝑡: for each model,𝜌 𝑡←corr( ˆ𝑣𝑡,·,𝑦𝑡,·)
(Eq. (8)), appended to its forward scores; store𝑢𝑡 of every blend
G.1 InvestorBench
System message(all calls).
You are a portfolio manager. You allocate a long-only portfolio across
four U.S. stocks (HON, JNJ, MSFT, UVV) and cash. Each trading day you set
target weights that are held until the next trading day's close.
29

Wu, Cai and Wang
Table G.1: Memory block of each LLM-based method in the
decision prompt on InvestorBench and ClassAlloc.
Method Memory block
Memory-free, Self-consistency none
MemTrial, Similarity retrieval,
Counterfactual selection,
Uplift credit, Draft averaging
experiences block with a subset of the four retrieved
lessons
FinMem experiences block with four lessons ranked by
similarity, recency and importance
MemRL experiences block with four of the ten most similar
lessons, ranked by learned value (𝜀-greedy)
Reflexion reflections block with its three most recent
reflections
ExpeL insights block with at most eight insights distilled
from all warm-up lessons
Decision prompt(user message), here for 25 February 2021 and
the draft with all four retrieved lessons.
Date: 2021-02-25
Market data (returns in %; volatility = standard deviation of daily
returns over 20 days, in %):
HON: close 190.74; 1-day -2.53; 5-day +1.07; 20-day +3.17; volatility
1.48
JNJ: close 148.73; 1-day +0.10; 5-day -1.19; 20-day -2.45; volatility
1.14
MSFT: close 222.30; 1-day -2.37; 5-day -6.07; 20-day -1.45; volatility
1.53
UVV: close 41.36; 1-day -1.53; 5-day -1.16; 20-day +7.24; volatility 2.02
News today:
- JNJ: The global Cold Pain Therapy Market is projected to grow from USD
1.6 billion in 2020 to USD 2.0 billion by 2025, at a CAGR of 4.4%, driven
by the increasing prevalence of arthritis and musculoskeletal disorders
and growing awareness of col
- JNJ: Lucid has announced the integration of its virtual whiteboard,
Lucidspark, with Microsoft Teams, enhancing real-time collaboration and
innovation for Teams users. This integration allows seamless movement
between Lucidchart and Lucidspark d
[... 7 more headlines: at most three per stock, each cut at 240
characters]
Experiences from your past decisions (use them only where relevant):
[1] (2020-09-14) In a mixed market with positive news for JNJ and MSFT
but recent negative 5-day returns for MSFT, I overweighted JNJ and MSFT,
underweighted UVV and HON, and held some cash. The portfolio outperformed
slightly. In similar cases, balance recent momentum with positive news,
maintain diversification, and keep modest cash to manage uncertainty.
[2] (2020-08-18) In a mixed market with modest gains and losses,
overweighting MSFT and JNJ aligned with positive trends but UVV’s rebound
was underestimated. Diversifying more evenly and maintaining a slightly
higher cash position could reduce downside risk. In similar conditions,
balance growth potential with volatility by avoiding concentration in
fewer stocks despite recent strong performance.
[3] (2020-07-17) In a mixed market with strong news for JNJ and MSFT but
recent declines in MSFT and UVV, I overweighted HON and JNJ for stability
and growth potential. Despite a dip in HON, MSFT’s rebound boosted
returns. In similar cases, balance stable leaders with growth stocks
showing recovery signs, maintaining some cash to manage volatility.
[4] (2020-07-16) In a mixed market with strong recent gains in HON and
JNJ but weakness in MSFT and UVV, overweighting HON and JNJ while
underweighting MSFT and UVV led to outperformance. For similar conditions,
favor stocks with positive momentum and stable news, maintain some cash
for flexibility, and cautiously reduce exposure to recent laggards to
improve returns.
Decide the target weights for the next trading day. Respond with a JSON
object only, for example {"HON": 0.2, "JNJ": 0.2, "MSFT": 0.2, "UVV": 0.2,
"CASH": 0.2, "reason": "one short sentence"}. Weights must be non-
negative and sum to 1.
Replyof gpt-4.1-mini (seed 0), as parsed.
{"HON": 0.25, "JNJ": 0.35, "MSFT": 0.2, "UVV": 0.1, "CASH": 0.1, "reason":
"Overweight JNJ for positive news and stability; moderate HON for steady
gains; reduce MSFT and UVV due to recent declines and higher volatility;
keep cash for risk management."}
Retry message, sent once after an invalid reply.
Your reply was not a valid JSON weight object. Reply again with the JSON
object only, weights non-negative and summing to 1.
Lesson prompt.After each warm-up decision, the agent sees the
outcome and writes a lesson. The prompt for 2 July 2020:
<market context of the warm-up day, in the format of the decision prompt>
Your decision: HON 15%, JNJ 30%, MSFT 40%, UVV 5%, CASH 10%
Next trading day returns (%): HON +1.52, JNJ +1.43, MSFT +2.15, UVV +1.45
Your portfolio return: +1.59%; equal-weight portfolio (four stocks and
cash): +1.31%.
Write one reusable lesson for future allocation decisions in at most 60
words: describe the market situation, what you did, what happened, and
what you would do in a similar situation. Plain text only.
The written lesson, stored with its date as experience E000:
(2020-07-02) In a mixed market with strong MSFT momentum and positive JNJ
news, overweighting MSFT and JNJ while maintaining modest exposure to
HON and UVV outperformed an equal-weight approach. Future allocations
should emphasize stocks with positive catalysts and momentum, balancing
risk with cash to capture upside while managing volatility.
Reflection prompt(Reflexion): the lesson prompt with its last
paragraph replaced by
Reflect on this decision in at most 60 words: what worked, what did not,
and what you will do differently next time. Plain text only.
Insight prompt(ExpeL), run once on all 63 warm-up lessons:
Below are lessons you wrote after past daily decisions, each with the
outcome of that decision.
- [2020-07-02; portfolio +1.59% vs equal weight +1.31%] In a mixed market
with strong MSFT momentum and positive JNJ news, overweighting MSFT and
JNJ while maintaining modest exposure to HON and UVV outperformed an
equal-weight approach. Future allocations should emphasize stocks with
positive catalysts and momentum, balancing risk with cash to capture
upside while managing volatility.
[... 62 more lessons, one per warm-up day]
Compare the successful and unsuccessful decisions and extract at most 8
general insights for future daily allocation across HON, JNJ, MSFT, UVV
and cash. Return a numbered list; each insight at most 30 words.
Insights and reflections blocks, which take the place of the
experiences block for ExpeL and Reflexion:
Insights distilled from your past decisions:
1. Balance growth momentum with recent price trends and volatility to
avoid overexposure to short-term weakness or reversals in high-volatility
stocks like MSFT and UVV.
2. Emphasize stocks with strong fundamentals and positive catalysts (e.g.,
HON, JNJ, MSFT) while maintaining modest cash to manage downside risk
and market uncertainty.
3. Maintain diversification across all stocks to capture unexpected
rebounds, especially in volatile or uncertain markets, avoiding
concentrated bets in recent winners.
[... at most 8 insights]
Your reflections on your most recent decisions (oldest first):
- <reflection on the third most recent decision>
- <reflection on the second most recent decision>
- <reflection on the most recent decision>
30

MemTrial: Learning When to Trust Memory
G.2 ClassAlloc
System message(all calls).
You are a portfolio manager. You allocate a long-only portfolio across
four asset classes (equities, bonds, commodities, real estate) and cash.
At the start of each month you set target weights that are held for the
next 20 trading days.
Decision prompt, here for 1 April 2022 (Appendix E) and the draft
with all four retrieved lessons.
Date: 2022-04-01
Market data (each asset class and cash is an equal-weighted index of
exchange-traded assets; returns in %; volatility = standard deviation of
daily returns over the last 20 trading days, in %):
equities: 1-month +3.20; 3-month -5.35; 6-month +5.93; volatility 1.62
bonds: 1-month -2.06; 3-month -5.59; 6-month -5.23; volatility 0.45
commodities: 1-month -1.35; 3-month +21.55; 6-month +22.05; volatility
2.03
real estate: 1-month +2.17; 3-month -8.63; 6-month +2.81; volatility 1.38
cash: 1-month -0.05; 3-month -0.12; 6-month -0.16; volatility 0.01
Experiences from your past decisions (use them only where relevant):
[1] (2018-04-02) In April 2018, equities showed recent weakness but
strong 6-month gains; bonds were stable with low volatility; commodities
mildly positive; real estate mixed signals. I favored equities and bonds
over cash, yielding a slightly better return than equal weights. In
similar conditions, maintain diversified exposure but overweight assets
with solid medium-term momentum and manageable volatility for balanced
growth.
[2]-[4] <the lessons of August 2016, May 2017 and December 2015; Appendix
E>
Decide the target weights for the next 20 trading days. Respond with a
JSON object only, for example {"equities": 0.2, "bonds": 0.2, "
commodities": 0.2, "real_estate": 0.2, "cash": 0.2, "reason": "one short
sentence"}. Weights must be non-negative and sum to 1.
The retry message, the reflection prompt and the memory blocks
are those of InvestorBench. In the lesson and reflection prompts,
the outcome lines become
Your decision: equities <x>%, bonds <x>%, commodities <x>%, real estate <
x>%, cash <x>%
Returns over the next 20 trading days (%): equities <+x.xx>, bonds <+x.xx
>, commodities <+x.xx>, real estate <+x.xx>, cash <+x.xx>
Your portfolio return: <+x.xx>%; equal-weight portfolio (the five asset
classes): <+x.xx>%.
and the insight prompt (ExpeL) becomes
Below are lessons you wrote after past monthly decisions, each with the
outcome of that decision.
- [<date>; portfolio <+x.xx>% vs equal weight <+x.xx>%] <lesson>
[... one line per warm-up month, 58 in all]
Compare the successful and unsuccessful decisions and extract at most 8
general insights for future monthly allocation across equities, bonds,
commodities, real estate and cash. Return a numbered list; each insight
at most 30 words.
Memorization probe(Appendix D.14), here for 1 April 2022; the
system message is “You answer questions about financial markets. ”
Date: 2022-04-01
Consider five asset classes, each an equal-weighted index of exchange-
traded assets: equities, bonds, commodities, real estate and cash. From
what you know about the markets, give the return in % of each asset class
over the 20 trading days starting on this date. If you are not sure,
give your best estimate. Respond with a JSON object only, for example {"
equities": 1.5, "bonds": -0.3, "commodities": 2.0, "real_estate": 0.4, "
cash": 0.1, "reason": "one short sentence"}.
G.3 PortBench
A draft is one run of the benchmark’s native agent in three stages:
market interpretation, signal generation and weight optimization.
Each stage is one chat completion that returns a JSON object (JSON
mode, at most 8,192 output tokens) and, from stage 2 on, receives the
output of the previous stage; the memory enters all three stages as
the benchmark’s experience block, which holds the records selected
by the method. The prompts below are those of PortBench-Raw for
the balanced investor on 1 April 2022, for the draft with all four
retrieved records; PortBench-Full extends the market-data table of
stage 1 from eight assets to all eligible assets.
System message(all stages).
You are the investment agent in a simulated research benchmark. Follow
the native stage instruction and return its JSON object; historical
experiences are observations, not guarantees.
Stage 1: market interpretation.
You are a portfolio manager analyzing market conditions on 2022-04-01.
MARKET DATA (trailing 60 trading days):
QQQ: price=352.83, trailing_return=-5.72%, ann_vol=31.03%
IWM: price=197.08, trailing_return=-4.32%, ann_vol=26.82%
VTI: price=215.83, trailing_return=-3.35%, ann_vol=22.60%
IVV: price=429.40, trailing_return=-2.98%, ann_vol=21.48%
EEM: price=41.63, trailing_return=-4.83%, ann_vol=28.28%
EFA: price=65.73, trailing_return=-5.89%, ann_vol=22.76%
VEA: price=42.58, trailing_return=-5.04%, ann_vol=21.35%
FXI: price=30.07, trailing_return=-5.79%, ann_vol=58.06%
Macro: fed_funds_rate=0.330, cpi_yoy=0.000, unemployment=3.900,
gdp_growth_qoq=0.000, t10y2y_spread=0.040
MACRO INDICATORS:
Fed Funds Rate (%): 0.33
Unemployment (%): 3.90
10Y-2Y spread (pp): 0.04
[... 12 more indicators]
[... pairwise, intra-class and inter-class return correlations]
Current market regime context: unknown
RECENT NEWS / FILINGS:
[INVESTOR PROFILE] This investor is BALANCED: allocate at most 65% to
equities and cryptocurrency combined; allocate at least 20% to bonds and
cash; the portfolio may accept up to a 20% maximum drawdown.
[Kaggle 2022-03-31] ["Apple now allows Netflix, Spotify and other'reader
'apps to link to their sites for payment It's part of the tech giant's
settlement with the Japan Fair Trade Commission.", [... further headlines
of the previous day]
TASK: Interpret the market data and provide structured asset views.
Return a sparse set of material asset views. Any visible asset omitted
from
"asset_views" is deterministically interpreted as neutral (0.0). Only use
visible asset identifiers and do not invent assets. You may include an
explicit neutral 0.0 view, but do not need to list every neutral asset.
For each reported asset, assign a sentiment score in [-1.0, +1.0]:
+1.0 = strongly bullish (expect strong outperformance)
0.0 = neutral
-1.0 = strongly bearish (expect significant underperformance)
Identify the overall market regime: one of "bull", "bear", "sideways", "
high-volatility".
JSON SCHEMA:
{
"asset_views": { "ASSET": <float in [-1, 1]> },
"detected_regime": "<bull|bear|sideways|high-volatility>",
"confidence": <float in [0, 1]>,
"macro_summary": "<one sentence>"
}
31

Wu, Cai and Wang
OUTPUT FORMAT — STRICT:
1. Reply with EXACTLY ONE JSON object and nothing else.
2. The very first character of your reply MUST be`{`and the very last
character MUST be`}`. No leading whitespace, no trailing newline
text.
3. Do NOT wrap the object in markdown code fences (no```json, no```).
4. Do NOT add any explanation, preamble, or commentary before/after.
5. Use double quotes for all keys and string values; numbers must be
raw
JSON numbers (no quotes, no`%`, no commas).
6. Every key listed in the schema below MUST appear exactly once.
FROZEN HISTORICAL EXPERIENCE (observations, not proof of causal advantage
):
{"text":"[{\"id\":\"ec8700d3d7c4...\",\"source_ids\":[...],\"text\":\"<
the record below, JSON-encoded>\"}, <3 more records>]","unique_source_ids
":[]}
One record of the experience block, decoded. Each record de-
scribes an earlier decision of the benchmark’s agent (2015–2019):
its allocation by asset class, a readout of its execution (net return
𝐽 , fee, turnover, concentration HHI, largest weight and fraction of
assets held), public market features at the time, and the realized
20-day net return.
{
"actual_target_weights_by_asset_class": {"bonds": 0.111, "cash": 0.011,
"commodities": 0.1184, "cryptocurrency": 0.0074, "equities": 0.6856, "
real_estate": 0.0666},
"benchmark": "PortBench-Dynamic-99asset-native-shared-memory-raw-price-
adaptation",
"decision_date": "2016-05-02",
"execution_readout_J_fee_turnover_HHI_maxweight_nonzero_fraction":
[0.010039484803091359, 0.0010229302, 0.682, 0.029007079999999998, 0.0735,
0.9883720930232558],
"experience_id": "portbench/ec8700d3d7c4...:portbench:2016-05-02:r0",
"feedback_scope": "actual20sessiontradeoutcome;
unexecutedalternativesunknown; notcausalsuperiority",
"public_state_features": [0.0, 0.86, 0.00153055, 0.01327625, 0.61627907,
0.19767442],
"realized_net_interval_return": 0.010039484803091359,
"settled_date": "2016-05-31"
}
Stage 2: signal generation.
You are a portfolio manager on 2022-04-01.
Stage 1 market interpretation produced these asset views (scale: -1=
bearish, +1=bullish):
QQQ: view=-0.400
IWM: view=+0.000
VTI: view=+0.000
[... the other assets]
Detected market regime: high-volatility
Macro summary: Market shows elevated volatility with flat CPI, low Fed
funds rate, narrow yield curve, and moderate unemployment, indicating
uncertain economic conditions and cautious sentiment.
Recent news / filings:
[investor profile and news, as in stage 1]
TASK: Convert each asset view into an actionable trading signal.
Rules:
- view > 0.15: consider "buy"
- view < -0.15: consider "sell"
- otherwise: consider "hold"
Use your judgement to refine signals based on regime and macro context.
Signal strength should reflect conviction (0.0 = low, 1.0 = high).
Return only non-hold signals. Omitted visible assets are interpreted as
hold with strength 0.5.
The signals and strengths objects must contain exactly the same selected
assets.
JSON SCHEMA:
{
"signals": {"SELECTED_ASSET": "<buy|sell>", ...},
"strengths": {"SELECTED_ASSET": <float in [0, 1]>, ...},
"reasoning": "<one sentence>"
}
OUTPUT FORMAT — STRICT:
[the six rules of stage 1]
[experience block, as in stage 1]
Stage 3: weight optimization.
You are a portfolio manager on 2022-04-01.
Stage 2 signals:
QQQ: signal=sell, strength=0.60
IWM: signal=hold, strength=0.50
VTI: signal=hold, strength=0.50
[... the other assets]
Current portfolio weights: QQQ=0.0103, IWM=0.0103, VTI=0.0103, [...] (
equal weights)
Portfolio NAV: $1,000,000
Market regime: unknown
[return correlations, as in stage 1]
TASK: Select a sparse portfolio allocation based on the signals above.
Constraints:
- allocation_scores must be finite, non-negative decimal numbers, with
at least one strictly positive score
- Do not normalize allocation_scores; the deterministic environment
normalizes their relative magnitudes into target weights
- Omitted visible assets receive a target weight of 0.0; a listed 0.0
explicitly excludes that asset
- Prefer a concise allocation, while retaining any material existing
holdings
- "sell" signals should receive reduced weight (ideally 0.0)
- "buy" signals should receive increased weight
- Minimize unnecessary turnover from current weights
JSON SCHEMA:
{
"allocation_scores": {"SELECTED_ASSET": <non-negative decimal>, ...},
"expected_return": <annualized decimal, e.g. 0.08>,
"expected_vol": <annualized decimal, e.g. 0.12>,
"sharpe_estimate": <decimal>
}
OUTPUT FORMAT — STRICT:
[the six rules of stage 1]
[experience block, as in stage 1]
Repliesof gpt-4.1-mini in this draft (seed 1). The environment turns
the stage-3 scores into target weights, which are then projected
to the investor’s mandate (Appendix D.3). Here, stage 3 gives the
same score to the 93 assets without a sell signal and none to the
four with one.
Stage 1: {"asset_views": {"FXI": -0.7, "QQQ": -0.4, "EFA": -0.5, "EEM":
-0.4}, "detected_regime": "high-volatility", "confidence": 0.8, "
macro_summary": "Market shows elevated volatility with flat CPI, low Fed
funds rate, narrow yield curve, and moderate unemployment, indicating
uncertain economic conditions and cautious sentiment."}
Stage 2: {"signals": {"QQQ": "sell", "EEM": "sell", "EFA": "sell", "FXI":
"sell"}, "strengths": {"QQQ": 0.6, "EEM": 0.6, "EFA": 0.7, "FXI": 0.9},
"reasoning": "In a high-volatility regime with cautious sentiment and
bearish views on QQQ, EEM, EFA, and FXI, moderate to high conviction sell
signals are warranted to reduce risk exposure in these assets."}
Stage 3: {"allocation_scores": {"IWM": 0.5, "VTI": 0.5, "IVV": 0.5, "VEA":
0.5, ... (89 more assets)}, "expected_return": 0.07, "expected_vol":
0.14, "sharpe_estimate": 0.5}
32

MemTrial: Learning When to Trust Memory
H Limitations
• Gains from memory on real markets remain to be shown.
On PortBench and InvestorBench, MemTrial’s advantage
over the experience-learning agents comes from abstain-
ing: its values passed the trust test on fewer than 1% of
the test decisions, and with the same anchor the baselines
do as well (Appendix D.5). On ClassAlloc they passed on
15%, and the trusted drafts did not beat the anchored blend
they replaced. These results show that MemTrial avoids
the losses of acting on untested memory, not that memory
improves real decisions; showing the latter may need more
decisions, more informative experiences or tasks in which
experiences matter more. When its values are trusted, Mem-
Trial deploys the selected draft in full and so takes on its
market exposure (Appendix E); keeping part of the anchor
even then is a natural extension.
• Pretraining exposure (look-ahead bias).The knowledge cut-
off of gpt-4.1-mini (June 2024) is later than the whole In-
vestorBench test period and than 15 of the 20 PortBench test
months, so the LLM may have seen these market outcomes
during pretraining; the same holds for 50 of the 71 Clas-
sAlloc test months. On ClassAlloc, the memory-free LLM
beats 1/𝑁 by 0.08 pp per month before the cutoff and trails
it by 0.08 pp after it (Appendix D.11), although 21 months
are too few for this difference to be significant. Every LLM
recalls dated outcomes from before its cutoff, and hiding
the dates on ClassAlloc did not remove the memory-free
draft’s advantage before the cutoff (Appendix D.14), but
the LLM may still recognize a period from the returns it
is shown; we did not hide the dates on PortBench and In-
vestorBench. This exposure affects all LLM-based methods
alike but may change how much any LLM agent gains from
memory; PlantedMem, whose drafts do not depend on the
date, is free of it.
• The anchor also holds back good drafts.When the LLM’s
drafts beat the reference, as on ClassAlloc before the knowl-
edge cutoff, the anchored action keeps MemTrial close to
1/𝑁 and gives up most of their advantage (Appendices D.11
and D.13). Its online blend moves towards better drafts,
but slowly under a prior of 0.9 on the reference (Appen-
dix D.10); a lower prior adapts faster but protects less when
the reference is strong.
• Error rate of the trust test.The trust test is applied on ev-
ery date to dependent scores of a selected learner (Appen-
dix C.3), so its false-pass rate has no formal bound; we
measure it instead (2–3% of PlantedMem decisions without
signal). A sequential test with time-uniform error control
on block or permutation scores would bound it.
• Cost.MemTrial needs eight drafts per decision instead of
one. The drafts run in parallel, so latency does not grow, but
the LLM cost does; adaptive designs that spend more drafts
only on dates where contributions are uncertain could re-
duce it.
• Benchmark protocols.PortBench scores each monthly deci-
sion as a separate episode that starts from the equal-weight
portfolio, so its costs are charged on the distance from that
portfolio rather than on actual turnover, and its experience
pool is fixed before the first decision date, so learning hap-
pens in the credit rather than in the content of memory. Our
InvestorBench task is a multi-asset adaptation of the bench-
mark’s single-stock task, with four stocks and cash. Clas-
sAlloc’s class indices are equal-weighted and rebalanced
daily, and its cryptocurrency class is left out. PlantedMem is
semi-synthetic: its experiences act on the drafts through a
simple tilt model (Appendix D.3), which is cleaner than the
way real lessons act on an LLM, and each period’s outcome
is known before the next decision.
33
