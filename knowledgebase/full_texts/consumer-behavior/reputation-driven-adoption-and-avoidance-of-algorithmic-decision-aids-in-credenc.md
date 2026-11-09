---
title: Reputation-Driven Adoption and Avoidance of Algorithmic Decision Aids in Credence Goods Markets
url: https://arxiv.org/abs/2401.17929
category: consumer-behavior
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Alexander Erlei
- Lukas Meub
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.17929
pages: 72
chars: 152256
fetched_at: '2026-11-08T13:12:23+00:00'
kb_version: 1
---

# Reputation-Driven Adoption and Avoidance of Algorithmic Decision Aids in Credence Goods Markets

Reputation-Driven Adoption and Avoidance
of Algorithmic Decision Aids in Credence
Goods Markets
Alexander Erlei* Lukas Meub
In credence goods markets such as health care or repair services, consumers rely on
experts with superior information to adequately diagnose and treat them. Experts, how-
ever, are constrained in their diagnostic abilities, which hurts market efficiency and
consumer welfare. Technological breakthroughs that substitute or complement expert
judgments have the potential to alleviate consumer mistreatment. This article studies how
competitive experts adopt novel diagnostic technologies when skills are heterogeneously
distributed and obfuscated to consumers. We differentiate between novel technologies
that increase expert abilities, and algorithmic decision aids that complement expert
judgments, but do not affect an expert’s personal diagnostic precision. When consumers
build up beliefs about an expert’s type through repeated interactions, we show that high-
ability experts may strategically forego the decision aid in order to escape a pooling
equilibrium by differentiating themselves from low-ability experts. Without future visits,
signaling concerns cause all experts to randomize their investment choice, leading to
under-utilization from low-ability experts and over-utilization from high-ability experts.
Results from two online experiments support our hypotheses. High-ability experts are
significantly less likely than low-ability experts to invests into an algorithmic decision
aid if reputation building is possible. Otherwise, there is no difference, and experts who
believe that consumers play a signaling game randomize their investment choice.
JEL codes. C91, C92, C72, D82
Keywords. Credence goods, expert ability, diagnostic uncertainty, technology, decision
aid, experiment
*Corresponding author. Chair for Economic Policy and SME Research, Georg-August-University Goettingen.
alexander.erlei@wiwi.uni-goettingen.de.
Lukas Meub: Institute for Small Business Economics (ifh), Georg-August-University Goettingen.
We gratefully acknowledge financial support by the Federal Ministry of Education and Research, project
"Handwerk mit Zukunft (HaMiZu)" , grant number 02K20D001.
For this article’s data, programming and screenshots, please refer to the online appendix https://osf.
io/shcmp/?view_only=e06a7d8315c14999a59c58754dfea809.
arXiv:2401.17929v3  [econ.GN]  25 Apr 2025

1. Introduction
Credence goods markets are characterized by severe information asymmetries between
experts and consumers. This often translates into market inefficiencies, with experts
resorting to insufficient treatments or using their information advantage to overcharge
consumers, e.g. for unnecessary services. Due to the ubiquity of expert services through-
out important economic decision domains such as medicine, law, financial advice or
accounting, these patterns are highly consequential, and very costly for both consumers
and the overall economy. The theoretical literature often attributes these adverse out-
comes to expert fraud. That is, given the right incentives, experts would behave “honestly”
and treat consumers perfectly. However, in reality, a second factor that can severely inhibit
the provision of high-quality services is the expert’s diagnostic ability. The information
asymmetry in credence goods markets generally precludes many consumers from ade-
quately judging the quality of a performed service ex post. This reduces their ability to
effectively discipline experts, who in turn have little incentive to invest into their abilities.
For example, Zhi et al. (2013) document an under-utilization rate of 44.8% for 46 of the
most commonly used diagnostic rests between 1997 and 2012. Simultaneously, around
30% of health expenditures in the US are used for non-beneficial interventions (Brody
2010). Several studies show the detrimental effect of insufficient skills on misdiagnoses as
well as faulty prescription of aggressive medication such as antibiotics (Chan, Gentzkow,
and Yu 2022; Xue et al. 2019; Currie and MacLeod 2017). Field experiments in the car
repair industry point to under-treatment rates of around 75% (Schneider 2012), as well as
a negative correlation between competency and low-quality services (Rasch and Waibel
2018). In auditing, heterogeneity in expert ability forces consumers to pay high premiums
for skilled service providers (Aobdia, Siddiqui, and Vinelli 2021).
Possibly the most promising solution to these entrenched quality issues are technological
breakthroughs, specifically in algorithmic decision systems. Even today, prediction mod-
els complement or substitute human judgments in many professional fields, including
legal search and bail decisions (Kleinberg et al. 2018), clinical diagnosis, medical scans
(Topol 2019) or financial advice (Brenner and Meyll 2020). Large language models such as
GPT are increasingly able to assist lawyers in discovering relevant information, generate
and check legal documents, or predict court outcomes (Alarie, Niblett, and Yoon 2018).
According to a study by the Michigan Legal Help Program, clients with access to a legal
advice software were equally successful as clients with an attorney when filing for divorce
(Sandefur 2020). Machine learning models have been shown to substantially exceed physi-
cians in predicting heart attacks by avoiding faulty human heuristics (Mullainathan and
Obermeyer 2022), and provide improved cancer screening (Daysal et al. 2022). However,
in order to actually realize these potentially large welfare gains, experts need to adopt
algorithmic decision systems at scale. If that happens, or how long it might take, is an
1

open, but very consequential question. Humans appear to have persistent biases against
algorithmic decisions, especially once they (inevitably) observe errors (Dietvorst, Sim-
mons, and Massey 2015). There are also reputational concerns. Relying on an algorithmic
decision system precludes the expert from sending a competence signal, and may well
indicate the opposite (Arkes, Shaffer, and Medow 2007; Dai and Singh 2020).
In this paper, we experimentally investigate the adoption of novel decision aids following
a technological shock on verifiable credence goods markets with diagnostic uncertainty
and obfuscated, heterogeneous (high vs. low) expert abilities. Our experimental setup
differentiates between two different phases. In a first phase, expert abilities are exogenous,
and cannot be improved through investment. Contrary to prior experiments on credence
goods, experts diagnose consumers problems by completing a short prediction task.
High-ability experts are able to utilize more input variables than low-ability experts. All
diagnoses are uncertain. Consumers can never observe an expert’s ability type. This
traps high-ability experts in a pooling equilibrium with low-ability experts, precluding
them from exploiting their skill advantage. The second phase simulates an external
technological shock. In Experiment 1, depending on treatment, experts receive the option
to increase their diagnostic precision by either (1) investing into their own abilities ( Skill)
or (2) investing into an algorithmic decision aid (Algorithm). This allows us to capture some
distinct features of algorithmic decision aids, and compare them with a baseline where
technological improvements are perfectly predictable and quantifiable. Technological
investments are always transferred onto consumers via prices, representing e.g. many
medical situations in which certain tests are not covered by insurance. We hypothesize that
high-ability experts may be incentivized to forego the algorithmic decision aid, but not the
skill investments, in order to signal consumers their personal ability type. The intuition
is that with decision aids, an expert’s personal ability type can still play a role in the
consumer’s choice process. Decision aids carry uncertainty, because consumers cannot
perfectly predict whether an expert is gonna (correctly) utilize the system’s information.
Consumers also know that high-ability experts derive relatively lower benefits from the
decision aid, and may therefore rather compete through lower prices. Low-ability experts,
on the other hand, cannot afford to imitate non-investing high-ability experts in the
presence of Bayesian consumers. This allows high-ability experts to escape the prior
equilibrium, and then exploit their skill advantage. In Experiment 2, we replicate the
Algorithm condition, and add a one-shot condition in which the second phase only lasts
one round. There is no future reputation building, leading to a coordination game in
which all experts with signaling concerns share the same best-response function and
should therefore randomize their investment choice. As a consequence, low-ability experts
under-utilize the decision aid, whereas high-ability experts over-utilize it.
Experimental results confirm the importance of obfuscated expert ability types for the
2

costly adoption of algorithmic decision aids. In line with our predictions for Experiment
1, there are no differences in investment behavior between ability types for Skill, whereas
high-ability experts are much less likely to purchase the algorithmic decision aid than
low-ability experts. Furthermore, high-ability experts who forego the algorithm exhibit
different price-setting patterns from those who decide to invest, suggesting signaling
behavior. Experts generally under-invest, which may be partially driven by consumer
choices. Investments tend to shift the expert’s price menus towards more self-serving
ones that reward fraudulent undertreatment.
Experiment 2 largely replicates the results from Experiment 1, and provides evidence from
incentivized beliefs elicitation that the separation between expert types is driven by high-
ability experts who think that consumers interpret investments as a signal for low-ability
type. Following theory, we find that these same experts tend to randomize their investment
choice in one-shot, irrespective of ability type. Overall, there are no differences between
expert types for algorithm adoption in theone-shot setup. Compared to a situation in which
reputation building through future interactions is possible, this leads to higher rates of
under-investment from low-ability experts and more over-investment from high-ability
experts, which hurts efficiency.
To the best of our knowledge, this is the first paper to analyze obfuscated expert abilities
and reputation concerns as a potential explanation for and barrier to technological adop-
tion in professional services. It is also the first paper to analyze the importance of future
reputation building in the presence of Bayesian consumers for experts’ technology adop-
tion behavior. Finally, our experiments offer empirical contributions about the efficiency
of credence goods markets when experts are heterogeneous and diagnosis is uncertain,
as well as the concurrent efficacy of expert investments after a technological shock.
Our paper relates to the literature on credence goods markets with diagnostic uncertainty.
Most articles are theoretical, showing how price competition may negatively affect di-
agnostic precision when experts need to exert effort (Pesendorfer and Wolinsky 2003),
that separating diagnosis and treatment can achieve first-best outcomes when consumer
evaluations are subjective (Bester and Dahm 2018), or that fraud-sensitive penalties can
discipline experts whose diagnoses require proper incentives (Chen, Li, and Zhang 2022).
In recent empirical work, Balafoutas et al. (2020) show in a laboratory experiment that
diagnostic uncertainty decreases efficient service provision and consumer market entry.
Insurances reduce investments into diagnostic precision, while pro-social experts invest
more. There is also evidence that diagnostic uncertainty does not affect expert dishonesty
or consumer trust, while reputation mechanisms remain beneficial for overall market
efficiency (Tracy, Schniter, and Zíka 2023).
A second relevant string is the literature on heterogeneous expert abilities on credence
goods markets. Prior theoretical work shows that efficient equilibria are always possi-
3

ble with heterogeneous, obfuscated expert abilities, but inefficient ones also exist (Liu
et al. 2020). Incentives to invest into expert abilities may break down in the presence of
discounters (Dulleck and Kerschbamer 2009), and heterogeneous cost functions gener-
ally prevent first-best solutions (Hilger 2016; Frankel and Schwarz 2014). Schneider and
Bizer (2017a) find that in the presence of low-ability experts who always misdiagnose
consumers without exerting effort, a sufficient number of high-ability experts allows for
a second-best equilibrium without policy intervention. Empirically, they show with a
laboratory experiment that high-ability experts invest less than theoretically predicted,
that the market is more efficient than predicted, and that price competition hurts overall
welfare (Schneider and Bizer 2017b).
Third and finally, this article contributes to the literature on decision aids in professional
contexts. Especially in the medical literature, it is a widespread sentiment that experts
who strongly rely on complementary decision expertise e.g., through laboratory test-
ing, tend to be less competent (Schroeder, Schliftman, and Piemme 1974; Daniels and
Schroeder 1977; Yeh 2014; Hall et al. 2019; Miyakis et al. 2006; Doi et al. 2021; Groopman
and Prichard 2007). There is evidence that both patients and peers derogate the diagnostic
ability of physicians who rely on diagnostic aids (Cruickshank 1985; Arkes, Shaffer, and
Medow 2007; Promberger and Baron 2006; Shaffer et al. 2013; Wolf 2014). Patients have
formulated preferences for physicians using intuition-based diagnoses versus statistical
models (Eastwood, Snook, and Luther 2012) and general aversions towards statistical
methods (Dawes, Faust, and Meehl 1989). While we do not measure consumers prefer-
ences or attitudes towards decision aids, we do study how experts may strategically avoid
algorithmic support systems in order to influence consumer beliefs about the expert’s
ability type. Rather than projecting a general distrust of technology, we thereby explore
another possibility why the adoption of algorithmic systems may lag behind the opti-
mal investment path. Skilled experts use the appearance of a novel diagnostic tool to
reduce consumer uncertainty about their ability and thereby differentiate themselves
from low-ability experts. Depending on the nature of consumer-expert interactions as
well as the possibility of reputation building, this may either lead to pooling equilibria
without technology adoption, separation between expert types, or a randomization of
adoption behavior.
2. The Market
We study a credence goods market with competing experts who are not liable for offering
insufficient treatments. Consumers know that they have a big problem with probability
h or a small problem with probability (1- h). Once consumers approach an expert, they
are committed to receive the recommended treatment under the offered price, meaning
there is no separation of diagnosis and treatment, and consumers cannot consult other
4

information sources. Afterwards, consumers can verify the treatment and observe their
payoff. If the problem is solved, consumers receive a payoff of v, if it is not solved, they
earn nothing. We assume that indifferent consumers choose to visit the expert. Similarly,
experts who are indifferent between cheating and treating the consumer honestly always
choose the correct treatment. There are two commonly known expert types, high-ability
(H, with probability γ) and low-ability (L, with probability 1 − γ) experts, who differ in
the probability to perform a costless correct diagnosis: z ∈ [0.75, 1] vs. q∈ [0.5, 0.75]. Let
i ∈ {H, L} and k ∈ {z, q}. Experts always charge for the implemented treatment (verifia-
bility), and a high quality treatment HQT (low quality treatment LQT) treatment induces
costs of ¯c (¯c), with ¯c > ¯c. The HQT solves both problems, the LQT only solves the small
problem. Expert type ability probabilities are common knowledge. Consumers therefore
consider two possible types of misdiagnosis: diagnosing a major problem when they actu-
ally have a minor problem, and diagnosing a minor problem in case of a major problem.
Consumers cannot observe an expert’s ability type. They can, however, identify each indi-
vidual expert, allowing for reputation. It is by assumption always profitable for the expert
to treat the consumer because v > ¯c. Experts choose a price menu P= (¯p,
¯
p) after learning
about their type, with ¯p (HQT)≥
¯
p. Consumers and experts are assumed to be risk-neutral.
Investments. After n rounds, experts can choose to increase their diagnostic precision k
for a fixed fee d. Investments automatically increase P by d. We assume that the low-ability
expert matches the high-ability expert’s skill by investing in the new technology. Thus, the
low-ability expert improves their diagnostic precision by an additional z− q for any chosen
precision level. There are two reasons for that. First, in many cases, low-ability experts
presumably make mistakes that are comparatively easy to eliminate. This also implies
low costs. Second, investing specifically in tangible new technology like an algorithmic
decision system does not only complement the expert’s diagnosis, but often serves as an
imperfect substitute for it (Doyle Jr, Ewer, and Wagner 2010; Dai and Singh 2020). Assuming
that the low-ability expert’s mistakes are relatively easy to fix, we’d expect algorithmic
decision aids to mostly eliminate them. 1
3. Experiment 1 – Experimental Design
We conduct two treatments of a pre-registered between-subject (Skill vs. Algorithm) online
group experiment where three experts compete over three clients. The experimental
parameters are fixed across treatments. Consumers have a big problem with probability
h = 0.4, receive v = 150 if their problem is solved, and earn σ = 15 when choosing the
1Even if the assumption that low-ability experts completely catch up to high-ability experts might be too
strong for many real-life cases, it is almost certainly true that the marginal benefits of algorithmic systems
will on average be larger for low-ability experts.
5

outside option. The cost of providing the LQT is ¯c = 20, the cost for the HQT is ¯c = 60.
Experts choose between three price vectors. The price for the HQT is ¯p= 100 and fixed.
For Pm, we set
¯
p= 40; for Pe, we set
¯
p= 60; and for Ps, we set
¯
p= 80. Experts always have a
markup of 40 for the HQT, and markups of 20/40/60 for the LQT when choosing Pm/Pe/Ps.
In each group, there are 2 low-ability experts and 1 high-ability expert. Low-ability (High-
ability) experts receive the correct signal with a probability of 50% (75%). Investing into
additional diagnostic precision costs d= 10 and increases an expert’s diagnostic precision
to k = 0.9. Importantly, investments also automatically increase
¯
p and ¯p by 10 Coins,
meaning that consumers pay for improved diagnoses. We apply the following conversion
rate: 100 Coins = 60 cents. Data from 300 participants (40% female) was collected on
Amazon Mechanical Turk (MTurk) using oTree (Chen, Schonger, and Wickens 2016) and
CloudResearch (Litman, Robinson, and Abberbock 2017). All participants are vetted for
quality by CloudResearch, completed at least 50 prior tasks on MTurk with a minimal
approval rating of 90%, and reside in the US. The base payment was $4.50.
3.1. Procedure
Subjects play 25 rounds in groups of six. The first 10 rounds are constant across treatments
and always follow the same sequence. Experts choose their price vector, and then diagnose
all three consumers by completing a short prediction task. Here, high-ability experts use
3 out of 5 possible input factors, and low-ability experts use 2 input factors to identify
the problem. Input numbers are pre-filled for each expert, who automatically make a
prediction by clicking on a "diagnose" button. Then, experts receive a diagnostic signal
that depends on their ability type. Finally, experts choose for each consumer whether
they want to implement the HQT or the LQT, and proceed to a summary screen that shows
how many consumers approached them and how much money they made that round.
Consumers first decide whether they want to leave the market, or choose one of the three
experts. Consumers do not observe an expert’s ability level, but they can identify each
expert, which allows for reputation building. After choosing an expert or leaving the
market, consumers wait to be treated and proceed to a summary screen that shows which
expert they approached in this round (as well as in all previous rounds), what prices the
expert chose, and how much money they earned.
After 10 rounds, all subjects are informed that experts now have the opportunity to invest
into their diagnostic precision (Figure 1). There are two treatments. In Skill, subjects learn
that experts can pay 10 Coins each round to increase their diagnostic precision to 90%. In
Algorithm, experts can pay 10 Coins each round to rent an algorithmic decision aid that
increases the expert’s maximum diagnostic precision to 90% if used correctly. For the al-
gorithmic decision aid, consumers also learn that experts are not forced to use the system,
but can choose to ignore it. All subjects know that consumers pay for the investment by
6

Nature draws
problem h
Experts make
investment decision
d
Experts set
prices P
Consumers observe
d and P
Consumers choose
Expert or σ
Experts receive
diagnostic signal k
Experts choose
HQT or LQT
Payoffs
are realized
FIGURE 1. Timing of events in each round forPhase 2. In Phase 1, experts skip the investment
decision.
automatically paying 10 Coins more per treatment if they choose to approach an investing
expert. Then, subjects complete another 15 rounds. Experts first decide whether they
want to invest, then choose their price vector, and proceed to diagnosis and treatment.
During the diagnosis, investments allow experts to utilize four input numbers, and those
in Algorithm can forego the decision aid with the click of a button. Consumers observe
each expert’s investment decision. Otherwise, nothing changes. Upon completing the
credence goods experiment, subjects proceed to a short post-experimental questionnaire
and answer a battery of demographic questions as well as a question about their risk
attitudes (Dohmen et al. 2011).
4. Predictions
4.1. Phase 1 Equilibria
To derive equilibria, we differentiate between the three possible markup scenarios: (i)
¯p− ¯c>
¯
p−¯c; (ii) ¯p− ¯c< ¯ p−¯c; (iii) ¯p− ¯c= ¯ p−¯c. First note that in any equilibrium where the expert chooses Ps or Pm and consequently always implements only the high quality or
low quality treatment, diagnostic precision does not matter and prices as well as profits
are the same as in the model with transparent expert abilities. That is because consumers
anticipate experts to follow their monetary self-interest. Under Pe, experts signal honesty,
because their markups for both treatments are the same. We first derive consumer profits
under Ps and Pm.
When (i) the profit margin for the HQT is larger than for the LQT, all expert types always
recommend the HQT. Therefore, consumer problems are always solved. Profits are
(1) πm = v− ¯p.
When (ii) the profit margin for the LQT is larger than for the HQT, experts always rec-
ommend the low quality treatment, irrespective of ability. Consumers infer the markups
7

from prices and anticipate undertreatment. Profits are
(2) πs = (1− h)v−
¯
p.
Finally, there are equal markup scenarios. Here, heterogeneous expert abilities affect
consumer payoffs, because lower diagnostic precision leads to more mistakes when treat-
ing consumers honestly. Under transparency, consumers anticipate different problems
depending on expert type:
(3) πe = (1− h+ hk)v− ¯p+(h+ k− 2hk)∆p
Which markup scenario do experts choose? With perfect diagnosis and full transparency,
Dulleck and Kerschbamer (2006) show that under verifiability, experts always efficiently
serve consumers by setting equal markups. With diagnostic uncertainty, that is no longer
viable, because credible commitment to honesty does not imply that a consumer is suffi-
ciently treated. Under competition, experts choose prices that maximize expected con-
sumer income. Hence, the boundaries determining experts price strategy are:
(4) πm ≥ πe when h≥ k∆p (1− k)v−(1− 2k)∆p := hm i .
and
(5) πs ≥ πe when h≤ (1− k)∆c kv+(1− 2k)∆p := hs i .
Under full obfuscation, however, consumers do not know whether to condition their
expected payoff on z or q. Therefore, they need to incorporate both possibilities, and
profits change to
(6) πe = (1− h+ hq(1− γ)+ γhz)v− ¯p+(h− 2hq(1− γ)− γ2hz+ q(1− γ)+ γz)∆p.
The boundaries determining experts price strategy are:
(7) πm ≤ πe when h≤ ∆p(q− γq+ γz) v(1− q(1− γ)− γz)− ∆p(1− 2q(1− γ)− γ2z) := hm o .
and
8

(8) πs ≤ πe when h≥ ∆p(q− γq+ γz− 1) v(q(γ− 1)− γz)− ∆p(1− 2q(1− γ)− γ2z) := hs o.
Note that in comparison to the transparent scenario, expected consumer profits from
approaching the high-ability expert decrease. This makes a straightforward argument
why high-ability experts are incentivized to signal their true ability type.
We now turn towards three possible equilibria. Without reputation or repeated interac-
tions, given full obfuscation, both expert types always charge the same prices and earn
the same profits in equilibrium (see also Liu et al. 2020). If the high-ability expert would
post a price vector that increases expected consumer profits, the low-ability expert could
simply copy it. This works as long as obfuscation is strong enough such that consumers are
sufficiently unlikely to believe that an expert following the high-ability expert’s optimal
pricing path is, in fact, a high-ability expert. Furthermore, in any equilibrium where
experts choose Ps or Pm and consequently always implement only the high quality or low
quality treatment, diagnostic precision never matters, irrespective of reputation. Hence,
from the expert’s perspective, their personal ability type is inconsequential.
In a first equilibrium, experts may always choose the HQT and charge Pm, irrespective of
type. This is the equilibrium we focus on in the experiment. Consumer beliefs µ(P) that
the expert is a high ability expert must be low enough. Otherwise, the high-ability expert
would be able to exploit their skill advantage by committing to treat consumers truthfully
and offer higher profits. Hence, the expected loss from inadvertently approaching the
low-ability expert who charges Pe (as compared to approaching an expert who chargesPm)
must be greater than or equal to the expected benefit from approaching the high-ability
expert who charges Pe.2 Then, consumer beliefs that the expert is a high-ability expert do
not exceed:
(9) ˜γm := vh(1− q)−(h− 2hq+ q)∆p (z− q)(vh− 2h∆p+ ∆p) .
Equilibrium 1. Both expert types charge Pm, always perform the major treatment, con-
sumers believe µ(P)∈ [0, ˜γm] if the expert chargesPe, meaning
¯
p−¯c= ¯p−¯c, and consumers
always visit the expert. Note that this also implies that the high-ability expert could attract
more consumers and thus increase profits in a scenario with only partial obfuscation by
increasing consumer beliefs such that ˜γ> ˜γm for h∈ [hmo , hm H].
Equilibrium 2. The analogous equilibrium for the case where experts always choose the
minor treatment implies:
2This only works for values of h and z under which the transparent high-ability expert would be able to
charge Pe. Otherwise, signalling better diagnostic precision has no impact on the expert’s price setting.
9

FIGURE 2. Left: Price setting under fully transparent and fully obfuscated expert abilities.
The shaded areas represents the high-ability expert’s loss. Due to consumer uncertainty,
the high-ability expert cannot choose the profit-maximizing price vector Pe as often as
they would want to. Variables for this figure: q= 0.5, γ= 1/3. Right: Variations for different
consumer beliefs ˜γ.
(10) ˜γs := −vhq−(h− 2hq+ q− 1)∆p (z− q)(vh− 2h∆p+ ∆p) .
Both expert types charge Ps, always perform the minor treatment, consumers believe
µ(P)∈ [0, ˜γs] if the expert charges Pe, meaning
¯
p−¯c= ¯p− ¯c, and consumers always visit
the expert. The high-ability expert could improve their profits in a scenario with only
partial obfuscation by changing consumer beliefs such that ˜γ> ˜γs for h∈ [hso, hs H].
Equilibrium 3. Finally, there are equal mark-up equilibria. We briefly describe them
for completeness, but do not analyze them empirically. Both expert types charge Pe and
without reputation or repeated interactions, consumers believe µ(P) ∈ [0, ˜γ] because
abilities are fully obfuscated and beliefs are fully determined by nature. Consumers
always visit the expert. Contrary to the other two equilibria, treatment behavior is not
obvious. We know that forh∈ [hs L, hm L ], both expert types always follow their own diagnosis.
However, within the gray area (see Figure 2) as well as at any point between hL and hH,
the incentives of the two expert types to follow their diagnosis differ. That is because
the high-ability expert may have options to deliver better treatments for the consumer,
whereas the low-ability expert, knowing about their small diagnostic precision, could
be incentivized to completely rely on one treatment and thereby minimize diagnostic
mistakes. For the consumer, treatment choices do not make a difference, because they
cannot infer anything from prices or experience.
If consumers repeatedly approach identifiable experts, their beliefs about their expert’s
type µ(P) change over time. That is because under Pe, consumers expect honest expert
behavior. On a verifiable credence goods market, this implies an outcome sequence with
10

three distinct observations: undertreatment (−
¯
p), efficient treatment of the small problem
(V −
¯
p), and overtreatment or the efficient treatment of the big problem ( V − ¯p). The
difference in diagnostic precision between expert types precludes low-ability experts
from offering the same sequence of outcomes as high-ability experts do. Therefore, in the
long run, consumers who use Bayes rule to update their beliefs will necessarily identify
their expert’s ability type. Low-ability experts cannot deviate from charging Pe because
consumers know that Pe is optimal and will always opt for such an expert. Hence, while
low-ability experts may be able to compete with high-ability experts for a limited number
of interactions, in the long run, expert type becomes transparent.
The consequences of consumer belief updating depend on the low-ability expert’s diag-
nostic precision, the market’s reputation mechanism, the number of competitors, and
consumer beliefs about competitor abilities. If there is a sufficiently accurate and com-
plete public reputation system, all consumers observe each expert’s ability type over
time and consequently opt for high-ability experts. Therefore, consumers always visit
an expert, consumer surplus increases compared to equilibria without reputation, and
low-ability experts cannot compete.
If reputation is the private information of the consumer, there are two different cases.
One, h ∈ [hs L, hm L ] and the low-ability expert maximizes expected consumer income by
choosing Pe and committing to honesty. Here, the consumer always switches away from
any expert i to another expert j as long as µi(Pe)< µ j(Pe). There are no opportunity costs
to switching, since all experts always follow the same strategy. Due to costless exploration,
consumers necessarily identify high-ability experts in the long run, and therefore achieve
the same surplus as in the public reputation case.
Second, h ∈ [hm L , hmo ]∨ h ∈ [hso, hs L], and the low-ability expert maximizes expected con-
sumer income by choosing Pm or Ps. Here, the low-ability expert imitates the high-ability
expert (Pe) at the expense of consumer welfare. If low-ability experts maximize consumer
surplus by always choosing the HQT or the LQT, consumers face no switching costs be-
cause all low-ability experts offer them the same expected value. Hence, consumers always
switch away from expert i when µi(Pe)< µ j(Pe) until they find a high-ability expert. This
incentivizes low-ability experts to (i) first imitate high-ability expert treatment behavior
and then (ii) switch towards their personal optimal treatment strategy once the Bayesian
consumer’s beliefs µ(P) are such that they would prefer the expert to always prescribe
the HQT or the LQT, because they are certain enough that the expert is not a high-ability
expert. In that situation, low-ability experts make switching costly by allowing consumers
to “discipline” them over time. Switching away from a disciplined low-ability expert is
costly because the consumer may switch towards an undisciplined low-ability expert who
imitates the high-ability expert’s treatment behavior by following their diagnostic signal,
and thereby reduces the consumer’s expected income. Therefore, it may be beneficial
11

for the consumer to stay with the disciplined low-ability expert, depending on (1) the
likelihood of switching to an undisciplined low-ability expert, (2) the number of future
interactions (and thus the value of exploration), and (3) consumer aversions towards being
lied to.
The three equilibria types show that high-ability experts are trapped in a pooling equilib-
rium for h∈ [hs H, hso]∨ h∈ [hmo , hm H]. When h∈ [hso, hmo ], identifiable high-ability experts
out-compete low-ability experts in the long-run. However, for h∈ [hm L , hmo ]∨ h∈ [hso, hs L],
low-ability experts may retain some consumers by making switching costly. Low-ability
experts always imitate high-ability expert prices, because they do not attract any consumer
otherwise. Regarding price setting, we propose:
Proposition 1. When expert abilities are fully obfuscated, the following scenarios arise:
(11)
⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩ Ps if h∈ [0, hso], Pe if h∈ [hso, hmo ], Pm if h∈ [hmo , 1] ⎫⎪⎪⎪⎪⎪⎬⎪⎪⎪⎪⎪⎭
4.2. Phase 1 Hypotheses
We can now insert the experimental parameters to derive our hypothesis. In Phase 1,
consumers believe that an expert is of high ability type with γ= 1/3. Expected consumer
income equals πm = 50 under Pm, πs = 10 under Ps, and πe = 45.67 under Pe. This follows
from consumers observing the mark-up incentives for experts and adjusting their expec-
tations accordingly. Therefore, experts always charge Pm in equilibrium irrespective of
type, with h = 0.4> hmo = 0.34 and γ = 1/3 < ˜γm = 0.59. There is no incentive to deviate
from implementing the high-quality treatment, meaning experts never under-treat clients,
who therefore always enter the market. Experts over-treat clients with a probability of
1− h= 0.6. High-ability experts cannot differentiate themselves from low-ability experts,
and price-setting therefore does not differ between types.
Hypothesis 1: Experts maximize expected consumer income by choosing Pm irrespective
of type.
Hypothesis 2: There is no difference between high-ability expert and low-ability expert
behavior.
Hypothesis 3: Consumers always enter the market.
12

4.3. Phase 2 Hypotheses: Skill
In Skill, experts can increase their diagnostic precision to k= 0.9 by paying d= 10 before
choosing prices. Consumers observe whether an expert invested. Hence, by investing,
an expert’s prior personal ability type becomes obsolete, and all investing experts are
the same type. Expected client income from approaching an expert who invested into
their diagnostic precision equals πe inv = 57. Comparing πe inv to πm, πs and πe reveals a
straightforward incentive for experts to invest. Under full transparency, the low ability
experts offers consumers an expected income of 40 under Pe, and the high-ability experts
offers an expected income of 57. Hence, even if consumers infer something about the
expert’s type when they invest, no expert type can out-compete an investing expert. At
most, consumers are indifferent between approaching the investing and the not-investing
transparent high-ability expert, when ˜γ = 1. Otherwise, they prefer any expert who in-
vested, regardless of their prior ability type. Assuming that high-ability experts cannot
signal their ability type with certainty by foregoing investments, consumer beliefs about
an expert’s type are inconsequential, and we propose:
Hypothesis 4: Low-ability experts in Skill always invest to improve their diagnostic ability.
Hypothesis 5: Low-ability experts in Skill maximize expected consumer income by choos-
ing Pe.
Hypothesis 6: High-ability experts in Skill always invest to improve their diagnostic ability.
Hypothesis 7: High-ability experts in Skill maximize expected consumer income by choos-
ing Pe.
4.4. Phase 2 Hypotheses: Algorithm
In Algorithm, experts can rent an algorithmic decision aid that increases their diagnostic
precision to k= 0.9 by paying d= 10 before choosing prices. Compared to Skill, this setup
exhibits some crucial differences. First, consumers know that experts can choose to
forego the decision aid’s information even after paying for the algorithm. Second, because
consumers do not have insight into the expert’s diagnostic process, they are uncertain
about the efficacy of the algorithm’s information. Hence, consumers still consider an
expert’s personal precision when anticipating their expected income. We argue that this
allows high-ability experts to differentiate themselves from low-ability experts, and escape
the pooling equilibrium derived earlier.
Looking at expert incentives, first note that once uncertainty is reduced and consumer
beliefs exceed certain thresholds ˜γ, pooling equilibria break down because high-ability
13

experts can, e.g., change their pricing strategy in return for their increased estimated
diagnostic precision. The same is true for the low-ability expert, but reversed. Lower
uncertainty decreases their potential profits. Thus, as long as there is uncertainty, high-
ability experts experience a penalty, whereas low-ability experts can charge more. Figure 2
illustrates how different levels of ˜γ change price setting. Without investments, high-ability
experts have obvious incentives to persuade consumers of their diagnostic type.
With investments, we have shown above that a transparent high-ability expert would be
indifferent between investing and not investing because in both cases, they offer con-
sumers an expected income of πe = 57 after choosing Pe. Introducing the aforementioned
uncertainty around decision aids changes that. Because consumers cannot be certain that
experts utilize the algorithmic decision aid (i) at all or (ii) effectively, expected consumer
income after investing changes toπe alg,inv ≤ 57. Then, depending on the level of uncertainty
as well as consumer beliefs about an expert’s type, it may be profitable for high-ability
experts to forego investments, if they can plausibly signal their type to consumers who
judge the benefits of the decision aid as uncertain. Yet, if that is the case, low-ability ex-
perts may also have incentives to once again imitate high-ability experts, which is initially
hidden to consumers because of obfuscated expert abilities. Note, however, that in order
to imitate high-ability experts, low-ability experts now also rely on Pe. In a one-shot game,
this is irrelevant, because there is no consumer belief formation. In Phase 1, it is irrelevant
because the pooling equilibrium implies Pm, which masks the low-ability expert’s abilities.
In Phase 2, however, imitating low-ability experts cannot hide their relative diagnostic im-
precision due to consumer expectations of being treated honestly (the high-ability expert’s
strategy). Therefore, we now have to ask whether it is profitable for low-ability experts to
imitate high-ability experts despite Bayesian consumers who update their beliefs.
First, to allow high-ability experts to try and differentiate themselves from low-ability
experts by foregoing the algorithm, and thereby to allow low-ability experts to imitate
them by foregoing the algorithm, consumers need to believe that an expert who does not
invest in round 11 is of high-ability type with µ(P)∈ [˜γm, 1] where ˜γm = 0.59. Consumers
then use Bayes’s rule to update their beliefs µ(P) each round. There are three possible
observations: (a) undertreatment (−
¯
p Coins), (b) overtreatment or efficient treatment of
big problem (50 Coins), and (c) efficient treatment of small problem (90 Coins). An honest
high-ability (low-ability) expert has respective observation probabilities of 0.1 (0.2), 0.45
(0.5) and 0.45 (0.3). Letn be the number of relevant a-signals, m be the number of relevant
b-signals, and o be the number of relevant c-signals. Approaching a low-ability expert is an
L-event, approaching a high-ability expert is a H-event. Given any sample of observations,
consumers calculate the posterior probability:
(12) Pr(L∣n, m, o)= Pr(n, m, o∣L)Pr(L) Pr(n, m, o∣L)Pr(L)+ Pr(n, m, o∣H)Pr(H) .
14

Pr(L) is the prior probability for event L that is determined by consumer beliefs at the
beginning of round 11 µ(P)∈ [˜γm, 1]. Using this, we can simulate a probability distribu-
tion of consumer beliefs. To demonstrate, let µ(P) = ˜γ ∈ {0.6, 0.8}. That is, consumers
believe that their expert has high abilities with a probability of 60% or 80%. At this point,
consumers would rather approach a not-investing expert with Pe under full obfuscation
than a Pm-expert who always successfully treats the problem because ˜γ> ˜γm. Figure 3
shows average consumer beliefs that a representative expert is of low-ability type over
time, using 10.000 simulations. Here, we assume that low-ability experts fully imitate
high-ability experts by choosing Pe and following their diagnosis.
2 4 6 8 10 12 14
Round
0.20
0.25
0.30
0.35
0.40
0.45
0.50
0.55
0.60Probability of Being Low-Ability Expert
Bayesian Consumer Beliefs (10.000 simulations)
FIGURE 3. Consumer Belief Updating with Pr(L)= 0.4 and Pr(L)= 0.2.
It is clear that consumer beliefs change substantially over time, which constraints the
imitation of high-ability experts.3 A second possibility is that low-ability experts imitate
high-ability experts in price setting and investment behavior, but always choose the HQT
in order to somewhat compensate their diagnostic disadvantage. As shown in Figure
A7 in the appendix, this strategy very quickly reveals the expert’s ability type. Having
demonstrated the limits for low-ability experts to imitate high-ability experts, we now turn
towards experts’ optimal strategies and the conditions under which high-ability experts
can escape the pooling equilibrium by signaling their type.
First, when does the high-ability expert deliberately forego the decision aid? Let w ∈
[0, 1] be the estimated probability from the consumer that an investing expert does not
3On the equilibrium path, consumers do not switch away from an expert in Phase 1 because there is no
undertreatment, and expect some undertreatment in Phase 2 as long as it is optimal to approach a Pe-expert.
Therefore, consumers gather repeated observations from an individual expert.
15

(correctly) utilize the decision aid after renting it. Then, expected consumer profit equals
πe alg,inv = (1− w)∗ πe inv+ w∗(˜γπe ninv,ha+(1− ˜γ)πninv,la− d)= (1− w)∗ 57+ w∗(30+ ˜γ∗ 17). In
the event of w, consumers pay an additional d without gaining diagnostic improvements.
Because experts invest, consumers receive an information signal about the expert’s type,
which is incorporated in˜γinv ∈ [0, 1 3]. If the expert does not invest, they influence consumer
beliefs ˜γninv ∈ [ 1 3 , 1]. Expected consumer profits are πe alg,ninv = 40+ 17∗ ˜γ. High-ability
experts forego the decision aid along:
(13) πe alg,ninv ≥ πe alg,inv when w ≥ 17(1− ˜γninv) 27+ 17˜γninv := wninv, or
(14) πe alg,ninv ≥ πe alg,inv when ˜γ≥ 17− 27w 17(1+ w) := ˜γninv
If ˜γninv ≥ ˜γninv after one of the three experts chose to forego the investment, then signaling
is a potential strategy for experts. The incentive is c.p. substantially larger for the high-
ability expert, because they do not profit from the investment under equilibrium prices
Pe, and do not have to worry about consumer learning as the latter’s confidence in their
beliefs only increases over time. In a one-shot setting, low-ability experts can imitate
high-ability experts, and there is no separation of expert types. We will come back to
that case in Section 6. With repeated interactions, imitation is limited, due to Bayesian
consumer updating.
To search for equilibria in which expert behavior is not pooled, we must first derive
what happens if one expert chooses to invest, while the other two choose to not invest.
Consumers believe with ˜γinv that either of the not-investing experts is the high-ability
expert. The expected income total income of approaching the sole investing expert is
πe alg,inv = R(57− 27w+ 17˜γinvw), where R is the total number of future expert–consumer
interactions (15 in our experiment). Consumers expected income from switching in round
11 to a non-investingPe expert is described by: πe alg,ninv = (1− ˜γinv)[0.5∗(riπe L+(R−ri)πe H)+
0.5∗(Rπe H)]+ ˜γinv(Rπe L), where ri is the number of rounds until the Bayesian consumer
i identifies the imitating low-ability expert’s j true type. 4 Consumers estimate a 50%
probability to accidentally approach the second low-ability expert, whose true type they
learn after ri. Note that πe alg,ninv is decreasing in ri, because better imitation increases the
cost of switching towards the imitating second low-ability expert. Consumers stay with the
investing expert if πe alg,inv ≥ πe alg,ninv holds, which gives ri ≥ 2R[πe alg,inv−((1−˜γinv)πe H+˜γinvπe L)] (1−˜γinv)(πe L−πe H)
4Here, we assume that means Pr(L) = 1− ˜γ j must be such that a Bayesian consumer’s belief ˜γl about
second not-investing expert l is high enough to prefer them over the investing expert, i.e., ˜γl ≥ 1− 27 17 w.
16

or ri ≥ 30[w(17˜γinv−27)+17˜γinv)] −17(1−˜γinv) := ¯ri in the current setup. Figure A1 in the Appendix illustrates
this condition.
If a consumer i realizes the expert’s type afterri < ¯ri rounds, they always leave the investing
expert in round 11 and search for the high-ability expert. If that holds for all consumers,
then no expert ever invests, and all low-ability experts maximize their income by imitating
the high-ability expert for r < ¯r rounds. Afterwards, consumers switch away because they
have been deceived, and switching cannot make them worse off. Hence, there are pooling
equilibria in which no expert invests if r < ¯r holds for all consumers.
Now, we go back to expert strategies under signaling concerns. Throughout, we assume
that not-investing is a sufficiently strong signal such that, if only one expert invests,
consumers think that this is the high-ability expert with enough certainty to always want
to approach them (see ˜yninv above). Otherwise, signaling is not a valid strategy. The
various payoffs associated with the investment choice in round 11 are illustrated in the
Appendix. Given that r ≥ ¯r may not hold for all consumers due to differences in belief
formation and priors, we define α∈ [0, 1] as the share of consumers for whom r ≥ ¯r holds.
Furthermore, because (1) subjects make decisions under high levels of uncertainty, (2)
signaling strategies may unravel quickly if only a minority of players follows them, and
(3) the experimental setup is quite complex, we use two methods to analyze whether
high-ability experts can escape the pooling equilibrium. One, we look for separating and
mixed Nash equilibria. Two, we assume bounded rationality where each expert deploys
Level-1 thinking and assumes that the other players are Level-0 (randomization) (Stahl
and Wilson 1995; Camerer, Ho, and Chong 2004). This approach has been shown in some
strategic settings to be a better predictor of behavior (Stahl II and Wilson 1994; Nagel
1995), particularly for initial play (Costa-Gomes, Crawford, and Broseta 2001; Crawford
and Iriberri 2007).
Non-Pooling Equilibria. There are two potential separating profiles. Either only the high-
ability expert invests, or only the two low-ability experts invest. In addition, there can
be mixed equilibria in which only one expert opts for the decision aid, thereby acting
as the “safe option” for consumers. Optimal strategies depend on how consumers are
distributed among experts, and whether experts can observe that. Here, we focus on
the case in which an expert cannot observe the distribution of consumers who did not
approach them. The results for each individual case are shown in the appendix, along
with a more detailed explanation of the results. Tables 1 and 2 illustrate the general payoff
idea for the simple case in which all experts ex ante coordinate on the high-ability expert.
If the high-ability expert foregoes the algorithm, they keep all consumers as long as
the two low-ability experts either both invest or do not invest, because consumers by
assumption do not switch when they are indifferent. If only one low-ability expert invests,
the high-ability expert loses all α consumers (ri ≥ ¯ri) who prefer the safe investing option.
17

TABLE 1. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on the
high-ability expert, i.e. xha = 3.
LA0
Invest Not Invest
LA0
Invest 1 (1− α)
Not Invest (1− α) 1
LA0
Invest Not Invest
LA0
Invest 1 0.5R−ri R
Not Invest 0.5R−ri R α+ (1− α) R−2ri R
HA3 Expert Chooses Not Invest HA3 Expert Chooses Invest
TABLE 2. Low-Ability Expert: Expected consumer attraction conditional on on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on the
high-ability expert, i.e. xha = 3.
HA3
Invest Not Invest
LA0
Invest ri R 0
Not Invest
(1− α)0.5ri R+
(1− α)0.5R−ri R 0
HA3
Invest Not Invest
LA0
Invest 0 0
Not Invest 0.5R−ri R α
LA0 Expert Chooses Not Invest LA0 Expert Chooses Invest
On the other hand, if the high-ability expert chooses to rent the decision aid, they only
keep all consumers if all experts do so. If both low-ability experts forego investments, the
high-ability expert keeps α, and may re-attract consumers when ri < 0.5R. Finally, any
expert who stands out as the only non-investing expert initially attracts all consumers.
The low-ability expert retains consumers for ri R rounds, i.e. until imitation is revealed.
Regarding strategic separation of experts, the only separating equilibrium in which the
high-ability expert foregoes the decision aid is an equilibrium by indifference if xha = 3.
Otherwise, separation is not stable, because the transparent pivotal high-ability expert
always monopolizes the market, which incentivizes low-ability experts to imitate.
In contrast, we find that strategic separation where only the high-ability expert invests –
which is very inefficient – can be a stable outcome under certain circumstances. Specifi-
cally, the high-ability expert must have attracted a small share of consumers at the time
of the technological shock (here xha ∈ {0, 1}) and the ratio r R has to be relatively large
(here, with one exception, r R > 0.5R), implying either a small number of expected future
interactions or a long imitation horizon. Figure 4 shows two illustrative cases for xha = 0
and xha = 1, and Figures A2, A3 in the Appendix illustrate all possibilities conditional on
the distribution of consumers. These confirm that even high-ability experts can profit
from acting as the sole safe option if ability differences are obfuscated, resulting in invest-
18

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha0, inv, noinf
la, 3, inv
la0, ninv, noinf
D

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 1, inv
la2, ninv, noinf
la0, ninv, noinf
E

FIGURE 4. Panels (a) and (b) show the separating equilibrium space in which only the
high-ability expert invests if (i) xha = 0, xla,i = 3, xla, j = 0 or (ii) xha = 1, xla,i = 2, xla, j = 0.
Panels (c) and (d) illustrate mixed equilibrium space where only one low-ability expert
invests for xha = 1, xla,i = 2, xla, j = 0. In Panel (d), LA0 invests. For all cases, experts do
not observe the distribution of “other” consumers who do not approach them.
ment paths that run opposite to the optimal ones. In the current experiment, we do not
expect them to be empirically relevant, if only because experts and consumers complete
15 interactions after the introduction of the decision aid, leaving ample room for learning
and experimentation. Nevertheless, this suggests that, while there is no clean separation
for the most desirable diagnostic path in which only the high-ability expert foregoes the
technology, expert separation can occur for the least desirable path. All thresholds and
respective hyperbolas are listed in Table A17.
Beyond clean separation, there may also be mixed equilibria which allow the high-ability
expert to escape the pooling equilibrium from Phase 1. In those, one low-ability expert
invests, while the other two experts do not invest. Tables A18 and A19 illustrate the respec-
tive conditions for different consumer distributions and expert information. In general,
as long as the high-ability expert does not attract all consumers in Phase 1, there are
parameter constellations in which one low-ability expert can find it profitable to act as
the safe option, while the second continues to forego the decision aid. Figure 4 shows
19

FIGURE 5. Strategic expert separation in which only the high-ability expert foregoes the
decision aid. Experts invest above their respective hyperbola, and do not invest below it.
Panel (b) shows the separating space when xha = 2, Panel (e)= for xha = 0, xla,i = 2 and
xla, j = 1.
an example for xha = 1 and xla = 2. The high-ability expert’s hyperbola across potential
scenarios always suggest a strong inclination to forego the decision aid, such that α must
consistently be very high to motivate high-ability investments. Both low-ability experts
can find it profitable to be the sole technology adopter, but the parameter space is much
larger for the low-ability expert with few (here 0) consumers. This is very intuitive, since
low-ability experts with a sizeable consumer stock can profit from imitation. For an il-
lustration of all hyperbolas under different conditions, refer to Figures A4 and A5 in the
Appendix. Overall, there are ample opportunities for high-ability experts to escape the
pooling equilibrium through signaling, depending on consumer preferences α, the speed
of learning ri and the number of total future interactions R. However, if consumers either
do not consider learning ( α= 1), heavily rely on safe alternatives, or learn very quickly
relative to the total number of interactions, there is less (or no) room for separation. More-
over, pure separation in expert strategies is only possible when the high-ability expert
(inefficiently) chooses to invest, not vice versa.
Bounded Rationality .We look at predicted expert behavior based on level-1 thinking
experts. This is primarily - but not only – to predict initial behavior once the novel tech-
nology arrives. Our focus lies on pure expert separation where the high-ability expert
is the only one to forego the decision aid. This is the most efficient diagnostic pathway,
and the one most in line with the idea of ability signaling to escape a pooling situation.
Tables A21 and A20 in the Appendix summarize all conditions for experts to strategically
separate. In contrast to the behavioral predictions from Nash equilibria, assuming that
experts simply maximize their expected payoff while being naive about the other experts
choices strongly predicts strategic ability-based separation for a large space of parameters.
In particular, the high-ability expert almost always chooses to forego the decision aid (see
Figure 5 for a selection and Figure A6 for a full overview). Low-ability experts’ inclination
20

to rent the algorithm increases in α, but decreases in ri R – resulting in a high likelihood for
pooling behavior without any technology adoption if ri R roughly≥ 0.5. Consumers being
relatively quick in identifying low-ability experts and switching between experts makes
investments more attractive for low-ability experts through (i) worsening imitation of
the expert themselves and (ii) worsening imitation of other low-ability experts, thereby
increasing the low-ability expert’s likelihood to poach other consumers.
Overall, if bounded rationality holds, high-ability experts almost always forego the decision
aid. Moreover, there is a large space for pure strategic expert separation in which the
high-ability expert escapes the previous pooling equilibrium through signaling. Hence,
we predict that, especially right after the appearance of the novel diagnostic technology,
high-ability experts will be less likely to invest into it. However, it is unclear how stable that
strategy is. While there are no Nash equilibria in which pure separation holds long-term,
there are stable mixed equilibria in which only one low-ability expert invests, and their
parameter spaces do intersect with the ones derived for bounded rationality. Hence, even
if bounded rationality does not explain behavior in equilibrium, high-ability experts may
still be able to exploit their skill advantage by foregoing the decision, albeit less effectively.
Finally, we should note that signaling still predicts pooling behavior for a wide arrange of
parameters. This would cause under-investments from low-ability experts. Moreover, if
signaling does not play any role, then theoretical predictions for Algorithm do not differ
from predictions for Skill, meaning all experts should invest (as long as w ≤ 0.48). Hence,
it is difficult to make fine-grained predictions. We hypothesize:
Hypothesis 8: Less high-ability experts than low-ability experts in Algorithm invest to rent
the algorithmic decision aid.
Hypothesis 9: Both expert types in Algorithm maximize expected consumer income by
choosing Pe.
5. Results
Table 3 provides summary statistics for the two periods. We first analyze subject behavior
and market efficiency in the first 10 rounds without diagnostic investments.
In contrast to the model’s prediction, experts do not generally maximize expected con-
sumer income by choosing Pm. The most popular price vector Ps has the highest prices
and lowest expected income for consumers (see also Figure A9 in the Appendix). This
replicates a common effect from prior credence goods experiments without diagnostic un-
certainty and obfuscated ability heterogeneity: under verifiability, experts rarely choose
equal mark-up price vectors, and instead opt for the price vector that splits the gains of
trade most equally if expert behave honestly (Dulleck, Kerschbamer, and Sutter 2011;
21

Phase 1 Phase 2 Skill Phase 2 Algorithm
Market Entry Rate 0.95 0.98 0.98
Efficiency (relative) 0.61 0.65 (0.75) 0.63 (0.74)
Undertreatment 0.29 0.23 0.25
Overtreatment 0.55 0.43 0.49
Efficient Treatment 0.52 0.64 0.60
Efficient Provision 0.40 0.59 0.53
Total Expert Surplus 132 133 133
Total Client Surplus 131 138 133
Price Vectors Pm 0.28 Pm 0.33 Pm 0.26
Ps 0.41 Ps 0.41 Ps 0.40
Pe 0.31 Pe 0.26 Pe 0.34
N 300 150 150
TABLE 3. Summary statistics by phase and treatment. Efficiency is calculated as (average
actual profit - outside option)/(maximum possible average profit - outside option). Relative
Efficiency refers to the market’s efficiency without correcting for the efficiency loss due to
investment costs. Undertreatment is the share of treatment choices where the consumer
has a big problem but receives the LQT. Overtreatment is the share of treatment choices
where the consumer has a small problem but receives the HQT. Efficient Treatment equals
1 when an expert makes the efficient treatment decision. Efficient Provision equals 1 when
the expert receives the correct diagnostic signal and consequently chooses the efficient
treatment.
Kerschbamer, Sutter, and Dulleck 2017). This leads to efficiency losses, as roughly 30% of
big problems are treated with the LQT.
Still, compared to other experiments with expert price setting, both Pm and Pe are rel-
atively common. In fact, experts shift towards the predicted price vector Pm over time
(logistic panel regression odds ratio: 1.08, p = 0.02, CI (95%): [1.01, 1.14]). Furthermore,
as predicted by the model, high-ability experts ( Pm/Ps/Pe = 0.29/0.39/0.31) set the same
prices as low-ability experts ( Pm/Ps/Pe = 0.28/0.41/0.31). There are no differences in the
number of consumers an expert can attract in round 10 on average between expert types
(t = 1.2, p= 0.214). High-ability experts cannot exploit their diagnostic advantage due to
ability obfuscation. Overall, inefficiencies from over- and undertreatment are relatively
common (see Figure A8), but do not deter consumers from entering the market. Only 5%
of consumers choices fall on the outside option. This makes the market much more effi-
22

FIGURE 6. Expert investment shares for Skill and Algorithm over the 15 rounds of Phase 2.
.2
.4
.6
.8
10 15 20 25 10 15 20 25
Skill Algorithm
Investment Shares High Ability Expert Investment Shares Low Ability Expert
cient than standard laboratory experiments with perfect diagnostic, suggesting a potential
upside of uncertainty for market outcomes (see e.g. Tracy, Schniter, and Zíka (2023)).
5.1. Phase 2 – Expert Investments
Round 11 introduces either skill investments or an algorithmic decision aid as an external
technological shock. Each round, experts can increase their maximum diagnostic preci-
sion to 90% by paying 10 Coins, which also automatically increases their prices by 10 Coins.
Figure 6 shows investment shares for the two treatments and expert types in Phase 2. As
predicted, there are no differences between expert types for skill investments. Over all 15
rounds, experts invest 64% of the time. Investments start at around 80%, but deteriorate
significantly (see Table 4). Thus, while popular, investment shares lie substantially below
the predicted (and optimal) 100%.
In Algorithm, investment shares clearly diverge between expert types. In round 11, 84% of
low-ability and 56% of high-ability experts rent the algorithm ( ˜χ2 = 6.91, p= 0.009). Across
all 15 rounds, 73% of low-ability expert choose to invest, whereas high-ability experts opt
for the decision aid with a probability of only 45%. Logit panel regression with subject-
level random effects and clustered standard errors at the matched group level confirm a
large and significant negative effect of being a high-ability expert on investment shares
(Table 4). This provides direct support for our main hypothesis. When an expert’s initial
ability type becomes inconsequential through skill investments, there are no differences
between high- and low-ability experts. With technological decision aids, however, some
high-ability experts try to signal their ability type by foregoing investments and offering
23

TABLE 4. Expert Investment Behavior in Phase 2
Skill Investment Skill Investment Algorithm Investment Algorithm Investment
High-Ability -0.022 -0.035 -0.257 ∗∗∗ -0.259∗∗∗
(0.081) (0.079) (0.067) (0.071)
Round -0.011 ∗∗ -0.001
(0.004) (0.004)
Risk 0.024 -0.003
(0.013) (0.016)
Female 0.005 -0.016
(0.083) (0.061)
Age -0.004 0.003
(0.004) (0.003)
N 1125 1125 1125 1125
This table reports marginal effects of panel logistic regressions using subject-level random effects and a
cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The dependent
variable is a binary variable that equals 1 if the expert invests into the new diagnostic technology. ∗
p< 0.05,∗∗ p< 0.01,∗∗∗ p< 0.001
lower prices. In line with that hypothesis, the algorithmic decision aid does not appear to
be less desirable overall. In both treatments, aggregated investment shares are 64%. That
is because, while high-ability experts exhibit a 19 percentage point drop in technology
adoption, low-ability experts are qualitatively more likely choose the decision aid – a
pattern likely generated by increased polarization through strategic expert separation.
Furthermore, investments into the algorithmic decision aid do not deteriorate over time.
This suggests that subjects’ do not predict consumers to be generally averse towards
algorithms.
Expert Price Setting. Figure A10 shows the share of experts choosing a specific price
vector depending on type, treatment and investment. We are primarily interested in
potential strategic differences between high-ability experts who invest and those who
forego investments. There are two potential effects. One, an expert may condition their
pricing strategy on their current investment choice (within-subject variance). For instance,
the standard model predicts a low-ability expert to change their pricing strategy from
Pm to Pe after investing. However, generating the necessary variance implies that an
expert switches between different investment and pricing strategies, which is largely
inconsistent with signaling behavior. Therefore, we would expect high-ability experts
in Algorithm to exhibit lower within-subject variance. Second, experts who invest a lot
may differ from expert who do not invest or only invest occasionally (between-subject
variance). This would, e.g., be consistent with some proportion of high-ability experts
foregoing the investment choice to signal their type. We first focus on the second case.
24

TABLE 5. Expert Price Setting Conditional on Investment Frequency
Low-Ability Expert High-Ability Expert
Skill Algorithm Skill Algorithm
Pm Ps Pe Pm Ps Pe Pm Ps Pe Pm Ps Pe
Investments 0.004 -0.002 -0.002 -0.009 0.001 0.013 0.001 0.006 -0.003 -0.004 0.045 ∗∗∗ -0.044∗∗∗
(0.065) (0.009) (0.008) (0.013) (0.011) (0.014) (0.013) (0.012) (0.012) (0.009) (0.006) (0.008)
N 750 750 750 750 750 750 375 375 375 375 375 375
This table reports marginal effects of panel logistic regressions using subject-level random effects
and a cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The
dependent variable is a binary variable that equals 1 if the expert chooses the respective price vector. ∗
p< 0.05,∗∗ p< 0.01,∗∗∗ p< 0.001
TABLE 6. Expert Price Setting Conditional on Investment Decision
Low-Ability Expert High-Ability Expert
Skill Algorithm Skill Algorithm
Pm Ps Pe Pm Ps Pe Pm Ps Pe Pm Ps Pe
Invested -0.134 ∗ 0.114 0.019 -0.173 ∗ 0.235∗∗∗ -0.175∗∗∗ -0.119 0.207 ∗∗ -0.172∗ 0.009 -0.012 0.008
(0.063) (0.064) (0.077) (0.057) (0.029) (0.049) (0.105) (0.070) (0.082) (0.103) (0.087) (0.098)
N 510 555 540 540 645 630 210 210 255 195 255 210
This table reports marginal effects of fixed effects panel logistic regressions. The dependent variable is
a binary variable that equals 1 if the expert chooses the respective price vector. Observations vary due
to the omission of groups where investment shares predict prices perfectly. ∗ p< 0.05,∗∗ p< 0.01,∗∗∗
p< 0.001
Table 5 shows random effects panel regression results for price setting conditional on the
number of rounds an expert chooses to invest. For low-ability experts, andSkill treatments,
there are no differences. The number of investment choices does not predict price setting
in either condition. For high-ability experts, there are large and significant effects of
investing frequency on Ps and Pe in the Algorithm treatment. Those who often rent the
algorithmic decision aid are more likely to choose Ps – the price menu that (1) has the
highest consumer prices, (2) exhibits the highest expected value for experts and (3) splits
the gains of trade relatively equally if experts behave honestly. On the other hand, high-
ability experts who never or rarely invest into the decision aid are more likely to choose
Pe – the price menu that can only be imitated for a short period of time and maximizes
expected consumer income if they approach a non-investing high ability expert.
These results are in line with our general proposition. In Algorithm, there appear to
be systematic differences between high-ability experts who invest into new diagnostic
technology and those who do not. Because high-ability experts can influence consumer
perceptions, some of them strategically choose a low-investment path with equal markup
prices. Those who invest a lot tend to opt for Ps, which is again inconsistent with the
standard model, but consistent with behavior in Phase 1 and prior empirical evidence
25

TABLE 7. Undertreatment Conditional on Expert Price Setting
Phase 1 Skill Algorithm
Undertreated (1) (2) (3) (1) (2) (3) (1) (2) (3)
Pm -0.084 -0.153 ∗∗ -0.08
(0.054) (0.054) (0.065)
Ps 0.221∗∗∗ 0.252∗∗∗ 0.121
(0.041) (0.043) (0.066)
Pe -0.152∗∗ -0.131∗∗ -0.048
(0.049) (0.047) (0.074)
N 574 574 574 450 450 450 434 434 434
This table reports marginal effects of panel logistic regressions using subject-level random effects
and a cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The
dependent variable is a binary variable that equals 1 if the consumers experiences undertreatment. ∗
p< 0.05,∗∗ p< 0.01,∗∗∗ p< 0.001
about the prevalence of selfish expert preferences (Kerschbamer, Sutter, and Dulleck
2017). In Skill, experts cannot differentiate themselves based on their original ability type.
Therefore, all experts face the same incentives, and we would not expect two different
“groups” that strategically choose either a low-investment or a high-investment strategy.
Instead, experts should condition their behavior on theircurrent price menu. To test this, we
opt for a fixed effects logistic panel regression with a binary variable measuring whether
an expert invested in a given round. This captures within-subject differences in price
setting conditional on the expert’s current investment choice. Results from a pooled
regression suggest that generally, investing reduces the share of experts choosing Pm
and Pe in favor of Ps (see Table A22). Separating regressions with regard to expert type
and treatment reveals that these trends are present in all conditions, except high-ability
experts in Algorithm (Table 6).
Thus, in our experiment, an investment into novel diagnostic technology that improves
accuracy and simultaneously increases prices shifts experts towards the most expensive
price menu with the lowest expected value for consumers. This tends to be true for both
expert types across the two conditions,except for high-ability experts after the introduction
of an algorithmic decision aid. In contrast, high-ability experts in Algorithm are the only
group whose choices are explained by the absolute number of investments, with non- or
low-investing experts opting forPe instead of Ps. Results therefore support the conjunction
that high-ability experts diverge into two groups with the introduction of technological
decision aids: one group that strategically under-invests to signal their ability type to
consumers, and one group that follows the standard model’s prediction by purchasing the
algorithm. As predicted, this pattern only exists in Algorithm, but not in Skill.
Expert Undertreatment and Overtreatment. The prevalence of Ps may be an indication
26

TABLE 8. Expert Intent-To-Undertreat Conditional on Price Setting
Phase 1 Skill Algorithm
Undertreated (1) (2) (3) (1) (2) (3) (1) (2) (3)
Pm -0.112∗∗∗ -0.128∗∗ -0.090∗
(0.028) (0.041) (0.039)
Ps 0.191∗∗∗ 0.213∗∗∗ 0.199∗∗∗
(0.031) (0.056) (0.066)
Pe -0.095∗∗ -0.097∗ -0.149∗∗∗
(0.049) (0.046) (0.038)
Invested -0.017 -0.026 -0.012 -0.039 -0.063 ∗ -0.047
(0.027) (0.026) (0.027) (0.028) (0.025) (0.028)
N 1312 1312 1312 928 928 928 910 910 910
This table reports panel regressions using subject-level random effects and a cluster–robust VCE estima-
tor at the matched group level (standard errors in parentheses). The dependent variable is the share of
choices where an expert chooses a LQT for a diagnosed big problem.∗ p< 0.05,∗∗ p< 0.01,∗∗∗ p< 0.001
that experts build a reputation of honesty and can therefore offer to split the gains of
trade equally. Table 7 shows that this is not generally the case. Consumers who approach
a Ps-expert are more likely to be undertreated, whereas Pe is – as theoretically predicted
– associated with lower rates of undertreatment. This is true for both Phase 1 and Skill.
Only in Algorithm, the chosen price menu has no significant predictive power. Therefore,
consumers cannot plausibly assume experts to treat them honestly irrespective of prices.
Investment choices do not predict undertreatment.
We now look at undertreatment from the expert’s perspective. Each round, experts receive
three diagnoses, and make three treatment choices. Because of diagnostic uncertainty,
an expert may intent to undertreat a consumer, but does not actually do so because of a
wrong diagnosis. Therefore, we define the intent-to-undertreat as experts who diagnose
a big problem, but prescribe the LQT, irrespective of the consumer’s actual underlying
condition. The results (Table 8) confirm that across all treatments, experts cheating
behavior is strongly influenced by their chosen price menu. Experts intend to undertreat
consumers significantly more often under Ps, and significantly less often under the two
other menus. Investment choices are largely irrelevant. There are no differences between
expert types.
For overtreatment, we document all relevant regression analyses in the Appendix. As
expected, consumers experience more overtreatment when approaching an expert with
Pm or Pe in Phase 1 (Table A24). For Phase 2, the results are similar, albeit less strong. In
Skill but not Algorithm, consumers who approach an investing expert are also significantly
less likely to be overtreated. Focusing on expert choices confirms the strong negative
effect of Ps on overtreatment compared to both Pm and Pe. Overall the results are in line
with theory such that consumers should expect Ps-experts to be much more likely to
27

TABLE 9. Consumer Switching Behavior
Switched Away – Phase 1 Switched Away – Phase 1 Switched Away – Skill Switched Away – Skill Switched Away – Algorithm Switched Away – Algorithm
Undertreated 0.377 ∗∗∗ 0.374∗∗∗ 0.256∗∗∗ 0.259∗∗∗ 0.208∗∗ 0.217∗∗
(0.051) (0.049) (0.067) (0.059) (0.068) (0.063)
Overtreated 0.046 0.049 0.042 0.048 0.042 0.049 ∗
(0.026) (0.026) (0.038) (0.041) (0.028) (0.024)
Pm 0.024 -0.268 -0.229
(0.092) (0.253) (0.195)
Ps -0.004 -0.156 -0.209
(0.095) (0.248) (0.212)
Pe 0.039 -0.364 -0.162
(0.093) (0.238) (0.204)
Round -0.008 -0.011 ∗ -0.016∗∗∗
(0.006) (0.005) (0.004)
Risk 0.037 ∗∗∗ 0.027∗ 0.039∗∗∗
(0.009) (0.012) (0.011)
Invested 0.073∗ -0.006
(0.034) (0.039)
Invested_LR 0.115∗ 0.021
(0.046) (0.036)
N 3600 3600 1050 1050 1050 1050
This table reports marginal effects of panel logistic regressions using subject-level random effects
and a cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The
dependent variable is a binary variable that equals 1 if the consumer switched to a new expert in the
current round. Undertreated, Overtreated and Invested_LR are lagged variables (one round).∗ p< 0.05,∗∗
p< 0.01,∗∗∗ p< 0.001
undertreat them. Across all rounds and conditions, intention-to-undertreat rates are 40%
under Ps, and only 12% and 11% for Pm and Pe respectively. On the other hand, intention-
to-overtreat rates are only 22% under Ps, and 48%/43% for Pe/Pm. Investment choices
generally do not affect cheating intentions.
Consumer Choices. How do consumers react to undertreatment with diagnostic un-
certainty? Table 9 shows that experiencing undertreatment strongly predicts consumer
switching in the following round. This holds for both phases and treatments. Overtreat-
ment appears to have no or only little effect on consumer choices. Furthermore, con-
sumers do not appear to condition their switching decision on the expert’s chosen price
menu. Yet, looking at the number of consumers an expert attracts confirms that the
former do exhibit strong preferences against Ps, and for Pm (Table A25 in the Appendix).
In line with consumer switching, undertreating consumers in the previous round also
significantly reduces an expert’s current number of consumers. Investments do not mean-
ingfully affect an expert’s ability to attract consumers. This may be one reason why we
find consistent under-investment by experts. Finally, a three-way interaction of expert
type, the expert’s investment choice, andPe suggests that high-ability experts in Algorithm
attract significantly more consumers when they choose Pe and simultaneously forego
the algorithmic decision aid. This result is in line with our theoretical prediction, and
does not hold for either Skill or low-ability experts, nor for any other price menu. Thus, it
provides supportive evidence for the hypothesis that high-ability experts may strategically
alter their utilization of costly decision aids under obfuscation to influence consumer
beliefs about their skill type.
28

6. Experiment 2: The Role of Repeated Interactions and Beliefs
We conduct a second experiment to replicate our findings for Algorithm, demonstrate
the importance of reputation building through repeated future interaction, and capture
incentivized consumer beliefs. The basic parameters of the game are the same as above,
except that we increase investment costs d from 10 to 12. This reduces the expected payoff
approaching an investing expert to πalg,inv ≤ 55 < πe ha,ninv = 57. The only difference is
that we do not strictly rely on uncertainty surrounding the decision aid when making
our predictions. Treatment-wise, we differentiate between a repeated (25 rounds) and a
one-shot (11 rounds) paradigm.
In a one-shot setting, where learning has no utility because consumers do not expect
their updated beliefs to affect future outcomes, there is no separation between expert
types. There are two possible scenarios. If consumers do not (sufficiently) interpret the
investment decision as an ability signal ( ˜γ < ˜γninv), then high-ability experts cannot
differentiate themselves and all experts should rent the decision aid as long as uncertainty
w≤ 0.48 to offer consumers the highest expected payoff.5 If consumers do interpret the
investment decision as a negative ability signal, then experts condition their investment
choice on their beliefs about other experts. To illustrate, we will assume here that the
signal is strong enough such that consumers find it profitable to approach the high-ability
expert after, ostensibly, identifying them.6 Table 10 shows a simple payoff matrix relating
to the share of consumers an expert can attract under these circumstances.
TABLE 10. Expert 1: Share of attracted consumers conditional on the choices of Expert 2
(E2) and Expert 3 (E3).
E3
Invest Not Invest
E2
Invest 1 3 0
Not Invest 0 1
E3
Invest Not Invest
E2
Invest 1 0
Not Invest 0 1 3
Expert 1 Chooses Invest Expert 1 Chooses Not Invest
The simple intuition behind these payoffs is the same as before: Consumers know that
high-ability experts can make a better offer without investments, while low-ability experts
cannot. Therefore, if two experts invest, and one expert does not invest, all consumers will
identify the not-investing expert as a high-ability expert and approach them (consumer
share = 1). Knowing that, low-ability experts are incentivized to not invest and create a
5Expert ability is fully obfuscated. Experts only forego the decision aid if γπe ninv,ha + (1− γ)πe ninv,la ≥
(1− w)πe inv+ w(πeo− 10) where γ= 1 3 because there is no signalling. 6 ˜γπe ninv,ha+(1− ˜γ)πe ninv,la ≥ (1− w)πe alg,inv+ w(˜γπe ninv,ha+(1− ˜γ)πe ninv,la)
29

pooling equilibrium in which consumers must choose randomly, which leads to experts
sharing consumers equally in expectation on average (consumer share = 1 3 ). Once both
other experts forego the investment, the third expert now maximizes their attraction
by investing – as long as the uncertainty surrounding the efficacy of the algorithmic
decision aid is not exorbitantly large. That is because consumers are uncertain if they
approach the not-investing high-ability or the not-investing low-ability expert. In that case,
πe alg,ninv = 0.5∗ πe ha+ 0.5∗ πe la = 48.5< πe alg,inv. Without learning, and under obfuscated
abilities, all experts face the same basic decision structure. Hence, there are only mixed
equilibria.
Participants first complete 10 rounds if a standard credence goods game with diagnostic
uncertainty. Due to ability obfuscation, there is a pooling equilibrium, and each experts
might have attracted x ∈ {0, 1, 2, 3} consumers in round 10. From any expert’s (e1) perspec-
tive, there are three cases. The other two do not invest: (1− pe2)(1− pe3); The other two
do invest: pe2 pe3; One other invests: pe2∗(1− pe3)+(1− pe2)∗ pe3. The expected payoff
for an expert to (not) invest is:
πinv = [(1− pe2)(1− pe3)](3− x)+[pe2 pe3]∗ 0+[pe2∗(1− pe3)+(1− pe2)∗ pe3](−x),
πninv = [(1− pe2)(1− pe3)]∗ 0+[pe2 pe3](3− x)+[pe2∗(1− pe3)+(1− pe2)∗ pe3](−x).
If all three experts choose the same strategy, no consumer has an incentive to switch.
The difference is πinv− πninv = (1− pe2− pe3)(3− x), which simplifies to 1 − (pe2+ pe3).
In the one-shot scenario, the number of current consumers x does not play a role. If
pe2+ pe3 > 1, the best response is to not invest. If pe2+ pe3 < 1, the best response is to
invest. If pe2+ pe3 = 1, then the expert is indifferent. In this case, all experts have the same
best response, thus giving 2 p= 1 and p= 0.5.7 The unique mixed equilibrium is p= 0.5.
Proposition 2. When expert abilities are fully obfuscated at the time of the technological shock,
neither consumers nor experts expect repeated future interactions, and experts believe that
foregoing the decision sufficiently affects consumer beliefs about expert type, then all experts
randomize their investment choice.
⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩ Invest if pe2+ pe3 < 1, Not Invest if pe2+ pe3 > 1, Indifferent if pe2+ pe3 = 1 ⎫⎪⎪⎪⎪⎪⎬⎪⎪⎪⎪⎪⎭
Whereas we predict high- and low-ability experts to separate in the repeated condition,
experts who predict a signaling game should randomize their investment choice in one-
7Note that this is different with repeated rounds, because consumers strategically approach experts to
learn about their type.
30

shot, causing under-investments from low-ability experts and over-investments from
high-ability experts.
6.1. Experimental Design
We implement a between-subject design with two treatments that are based on the Algo-
rithm condition from Experiment 1. In repeated, subjects complete the original Algorithm
procedure, except that investment costs increase by 2 such thatd= 12, and that we elicit in-
centivized consumer and expert beliefs at the end of the experiment. In one-shot, subjects
only complete 11 rounds, meaning there is only one round after the technological shock.
To ensure incentive-compatibility, participants learn that their payoff from the last round
will be multiplied by 4 when calculating their bonus. Other than that, nothing changes. For
belief elicitation, we follow an (incentivized) introspective approach (Charness, Gneezy,
and Rasocha 2021). We ask consumers (1) the likelihood that an expert who chooses to
rent the decision aid does not use it, (2) the likelihood that an expert who chooses to rent
the decision aid does not use it correctly and hence does not achieve the best-possible
prediction accuracy of 90%, and (3) the likelihood that an expert who chooses to rent the
decision aid is a high-ability expert. For each question, we ask (not incentivized) what
the consumer themselves thought in round 11, as well as (incentivized) the average likeli-
hoods across all observations. For the latter, we inform consumers that they earn $2 for a
perfect prediction. For each point that their prediction is off by, that $2 is reduced by $0.1.
Similarly, experts state two beliefs about consumer beliefs that an expert who chooses
to rent the decision aid is of high-ability, one non-incentivized about their own beliefs
in round 11, and one incentivized about average consumer beliefs. In addition, experts
indicate who they think is more likely to rent the algorithmic decision aid. We rely on
simple introspection, as opposed to, e.g., scoring rules, because they have been shown to
be effective even without incentives (Charness, Gneezy, and Rasocha 2021; Trautmann and
van de Kuilen 2015) and have the upside of being very simple. Complex rules can distort
subject beliefs (Danz, Vesterlund, and Wilson 2022), which may be especially likely after
a long and complex main game such as this one. Participants indicate their beliefs after
the main game to avoid influencing behavior. While experiences throughout the game
might affect subject belief measurement, it is more important to avoid distorting actual
behavior. We collected data from 312 participants via Cloud Research’s Connect platform
(Hartman et al. 2023). All participants completed at least 10 prior tasks with a minimal
approval rating of 90%, reside in the US, and successfully answered 4 comprehension
questions within three trials. The base payment is $7 .
31

6.2. Results – Beliefs
We first look at consumer and expert beliefs. Experts in repeated generally believe that low-
ability experts are most likely to rent the decision aid (59%), followed by “equally likely”
(35%), whereas only 6% opt for the high-ability expert. This is in line with our expectations.
Yet, when asked to indicate their incentivized beliefs about how consumer beliefs that
an expert is a high-ability expert would change after an expert invests, 80% indicate a
positive probability, suggesting that consumers would be more likely to identify an expert
as high-ability after renting the decision aid (Figure A12 in the Appendix). While there
may be some measurement error due to the involvement of negative probabilities, results
suggest that a majority of experts expects consumers to draw the wrong inference from
investments. For consumers, 17% believe that the investment choice is not an informative
signal about expert type (stated likelihood that an investing expert is a high-ability expert
= 33%), 32% believe that investing reduces the likelihood of an expert being of high
ability type, and 51% believe that investing increases the likelihood (Figure A12 in the
Appendix). Hence, there is substantial heterogeneity in consumer beliefs. Note again,
however, that these might be affected by participant experience during the experiment.
To approximate the extent to which consumers perceive uncertainty around the decision
aid (see Experiment 1), we also ask about the likelihood that experts choose to ignore the
decision aid, or do not use the corresponding information from the algorithm correctly.
While most consumers judge that to be unlikely, average incentivized consumer beliefs
that an expert does not use the system are around 30% (Figure A13 in the Appendix),
corroborating that uncertainty may play a substantial role. The belief results for one-shot
are similar, suggesting a limited effect of experimental exposure on belief formation. A
larger percentage of consumers beliefs that investments have no informative value for
ability type (28%), and the average incentivized indicated likelihood that an expert does
not use the decision aid is only 22%. On the expert side, roughly 36% (60%) believe that the
effect of investing on consumer high ability beliefs would be negative (positive). Overall,
despite some moderate changes, belief patterns between treatment remain comparable.
6.3. Results – Repeated vs. One-Shot
Figure 7 shows investment shares for repeated. In line with our prediction and Experiment
1, there is substantial expert type separation when learning through repeated future
interactions is possible. With the appearance of the technological shock in round 11, 52%
of high-ability experts and 90% of low-ability experts rent the decision aid ( ˜χ2 = 13.73, p<
0.001). Over time, that difference becomes significantly smaller, mostly because low-ability
experts invest less. This stands in contrast to our results above, where the gap did not
meaningfully change over time. Two potential reasons are the increased investment costs
32

FIGURE 7. Left: Expert investment shares for repeated in the Algorithm paradigm over
the 15 rounds of Phase 2. Right: High-ability expert investment shares dis-aggregated by
direction of incentivized beliefs.
.2
.4
.6
.8
10 15 20 25
Investment Shares High Ability Expert Investment Shares Low Ability Expert
0
.2
.4
.6
.8
10 15 20 25
HA Expert Negative Beliefs Investment Shares Low Ability Expert HA Expert Positive Beliefs
d and simple population effects, as we utilize a different subject pool from a different
platform, with an experiment that is quite sensitive to a number of individual parameters.
Still, a random effects panel logistic regression finds a significantly negative effect of
high-ability expert type on the likelihood to invest (Table A26).
Theoretically, this result should be driven by the sub-population of high-ability experts
who expect consumers to adjust their beliefs about an expert’s high-ability type downwards
after observing investments. Otherwise, foregoing the decision aid cannot function as
a competence signal. The right panel of Figure 7 shows high-ability expert investment
shares disaggregated by belief category. A negative belief indicates that experts expect
consumers to belief that an investing expert is less likely of high ability type, a positive
belief indicates the opposite. As predicted, the separation of experts appears almost
entirely driven by experts who believe that consumers read not-investing as a competence
signal. In contrast, there is almost no difference between high- and low-ability experts if
high-ability experts do not think that foregoing the algorithm can convince consumers
of their type. Hence, results suggest that expert beliefs about consumer beliefs drive the
separation between expert types. In line with our theory, high-ability experts engage in
a signaling game by exploiting the appearance of a novel technology if that strategy is
consistent with predicted consumer beliefs. Otherwise, investments remain on a similarly
high level.
Second, Figure 8 shows expert investments shares in round 11 for one-shot. In contrast
to repeated, there is no significant difference between high- and low-ability experts (67%
vs. 79%, ˜χ2 = 1.627 ,p= 0.202). Moreover, categorizing experts according to their beliefs
about consumer beliefs suggests that (1) both high- and low-ability experts tend to rent
the algorithm with a probability of around 50% when they believe that consumers take
not-investing as a competence signal, and (2) a large majority of both expert types invests if
they believe investing transports no information or suggests that an expert is of high ability
33

FIGURE 8. Left: Expert investment shares for one-shot in the Algorithm paradigm in Round
11. Right: Expert investment shares dis-aggregated by direction of incentivized beliefs.
0.67
0.80
0
.2
.4
.6
.8
1
Investment Shares High Ability Expert Investment Shares Low Ability Expert
0.76
0.91
0.50
0.58
0
.2
.4
.6
.8
1
HA Positive Beliefs LA Positive Beliefs HA Negative Beliefs LA Negative Beliefs
type. While sub-sample analyses should be interpret cautiously given the sample size,
these results align with expert behavior in repeated as well as our theoretical prediction.
In the absence of future learning opportunities, experts whose ability differences are
obfuscated and who believe that consumers enter a signaling game randomize their
investment decision. This generally leads to over-investments from high-ability experts,
and under-investments from low-ability experts. On the other hand, experts who do not
think that consumers interpret foregoing the algorithm as a competence signal are always
incentivized to invest, irrespective of type. In our data, this leads to higher investment
shares across the board, resulting in less under-investments from low-ability experts and
more over-investments from high-ability experts. On aggregate, high-ability experts invest
more than in repeated, while low-ability experts invest less – which, regarding efficiency, is
undesirable in both directions. Comparing expert behavior in round 11 between repeated
and one-shot by their beliefs (see Figure A14 in the Appendix) suggests that high-ability
experts, who belief that consumers take not-investing as a positive ability signal, generally
do not rent the decision aid (0%) with repeated future interactions, while those in one-shot
randomize (50%). Similarly, signaling low-ability experts always invest in repeated (100%),
but randomize in one-shot (58%). Overall, results from Experiment 2 corroborate all our
theoretical predictions and largely replicate Experiment 1.
7 . Concluding Remarks
Technological breakthroughs have the potential to significantly alleviate inefficiencies on
credence goods markets. While full automation of expert tasks is usually neither feasible,
nor desirable or legal, algorithmic decision aids offer huge potential in complementing or
sometimes even substituting human expertise. In this paper, we argue that two prevalent
characteristics of real-life credence goods markets can affect the effective adoption of
novel diagnostic technologies: diagnostic uncertainty and obfuscated heterogeneous
34

expert abilities. Consumers know that experts cannot perfectly identify their problem,
but also that some are better than others. Information asymmetries preclude consumers
from accessing that information, hurting both their welfare and the welfare of high-
ability experts. Technological shocks, like the invention of a new diagnostic medical
test or large language models, offer an opportunity for experts to influence consumer
perceptions of their abilities. That is because consumers know that high-ability experts
not only derive smaller benefits from decision aids, but are additionally hurt by the lack
of skill expression. Once novel technologies allow lower ability experts to costly catch
up to higher ability experts, we show that the presence of Bayesian consumers limits the
low-ability consumer’s capacity for imitation. Then, by strategically ignoring the decision
aid, a high-ability expert can signal consumers their ability type, and simultaneously
offer a more favorable price. In reality, the latter may represent (1) lower diagnostic costs
for experts or (2) less services for the consumer. In the medical domain, for instance, it
is common for patients to pay for additional or advanced tests that are not covered by
insurances but increase the chance of a correct diagnosis.
In combination, the obfuscation of heterogeneous abilities with the appearance of a
novel technology gives rise to a set of signaling games, many of which, as we show, can
lead to a separation of expert strategies, depending on the (1) the mechanism and (2) a
number of variables such as the imitation horizon and consumer preferences for a “safe”
option. These may result in very efficient diagnostic paths where low-ability experts are
much more likely to invest than high-ability experts. Yet, they can also imply widespread
rejection of novel technologies through low-ability experts’ imitation behavior. Under
certain conditions, like very noisy and slow consumer learning curves, a small number
of repeated future interactions, and a low market share for the high-ability expert, there
are even stable equilibria in which only the high-ability expert invests – maximizing
both over- and under-utilization of the decision aid. In addition, we show that without
repeated future interactions, all experts who enter a signaling game randomize their
investment choice, whereas without signaling, all experts would invest. As randomization
simultaneously implies over-utilization from high-ability experts and under-utilization
from low-ability experts, theory suggests very inefficient technology adoption paths in
domains with limited reputation building, such as highly specialized services which people
only very infrequently demand. This may, for example, be one reason why in medicine,
both under- overtesting are very common.
We test these ideas using two online credence goods experiments in which experts experi-
ence a technological shock after 10 rounds and thereby receive the option to costly increase
their diagnostic precision. The first experiment differentiates between skill investments,
and algorithmic decision aids. Skill investments over-ride an expert’s prior ability type,
representing for example advanced or specialized training. Algorithmic decision aids
35

complement the expert’s diagnosis, without affecting their personal ability type. There-
fore, experts who do not use or disregard the system may still rely on their own diagnostic
skill. Our results show no differences between high-ability and low-ability expert for skill
investments. With the algorithmic decision aid, however, high-ability experts are far less
likely to pay for increased diagnostic precision. Auxiliary results suggest that investing and
non-investing high-ability experts exhibit different pricing strategies, with those largely
foregoing the decision aid predominantly relying on price menus that signal honesty. On
the other hand, investing experts opt for prices that are more favourable to them. These re-
sults offer preliminary evidence that high-ability experts may strategically (under-)utilize
technology to differentiate themselves from low-ability experts. They also suggest that
the adoption of algorithmic decision aids could be conditional on the distribution of skills
within a profession, and that negative consumer attitudes towards professionals with
decision aids may be rooted in actual ability differences.
Overall, experts in our experiment substantially under-invest into new diagnostic tech-
nologies. This is one reason why efficiency gains are small to negligible. Investments do
not meaningfully affect expert fraud, which may be partially driven by very high consumer
participation rates. Throughout the experiment, 95%-98% of consumers enter the market,
which speaks to the potential efficiency of uncertain credence goods markets under verifi-
ability. Consumers react negatively towards undertreatment, but not overtreatment, and
generally do not reward expert investments. In contrast to the predictions of the standard
model, consumers also do not appear to reward expert prices that signal honesty. Instead,
they avoid high prices with expert-incentives to under-treat, but approach lower prices
with expert-incentives to over-treat. This strongly reduces investment incentives.
The second experiment provides evidence that there is indeed little to no expert separation
without the possibility of reputation building, which leads to strong over-investments from
high-ability experts. Furthermore, results suggest that separation is driven by experts who
think that foregoing the decision aid is a competence signal, and that this perception leads
to highly polarized – and therefore efficient – investment patterns. Hence, the inability of
consumers to observe expert abilities is very costly, and can, in the absence of reputation
building, cause randomized technology adoption. This highlights the constant need of
establishing a better information system for consumers, or to allow for de-centralized
mechanisms like prices to better internalize dispersed consumer knowledge. This holds
specifically of sectors in which (1) consumer demand is rare, e.g., highly specialized
services, or (2) sectors in which consumers interact with a mass of potential experts,
e.g., hospitals or large insurance firms. On the plus side, technological progress itself
can – under the right circumstances – endow experts with an information mechanism
that allows them to escape inefficient pooling equilibria while simultaneously motivating
large-scale algorithmic adoption by low-ability experts – where it has the largest marginal
36

benefit.
Our findings provide first evidence on the efficacy of algorithmic decision aids on credence
goods markets with obfuscated, heterogeneous expert abilities. We hope they provide
some useful orientation for future research. In particular, there is much to learn about
the relationship between expert investments, technology, and consumer learning/beliefs.
For example, identifying institutional or environmental factors that inhibit or promote
consumer learning could be highly valuable. It not only reduces information asymmetries
and thereby avoids exploitation, but also plays a crucial role in pushing experts towards
efficient technology adoption paths. More generally, the role of signalling for creating
efficient equilibria in the context of obfuscated information is highly important, with con-
crete implications for practical interventions that allow high-ability people to differentiate
themselves. Finally, carefully isolating and quantifying the mechanism behind (a) what
causes experts and consumers to engage in a signalling game, (b) consumer reactions
towards experts with decision aids, and (c) the role of ability distributions and market
conditions such as excess demand or monopoly actors, is crucial to better understand the
transformative impact of technology on credence goods markets. This generally necessi-
tates a better understanding of the beliefs and expectations of experts and consumers
alike.
37

References
Alarie, Benjamin, Anthony Niblett, and Albert H Yoon. 2018. “How artificial intelligence will affect
the practice of law. ”University of Toronto Law Journal 68 (supplement 1): 106–124.
Aobdia, Daniel, Saad Siddiqui, and Andres Vinelli. 2021. “Heterogeneity in expertise in a credence
goods setting: Evidence from audit partners. ”Review of Accounting Studies 26: 693–729 .
Arkes, Hal R, Victoria A Shaffer, and Mitchell A Medow. 2007 . “Patients derogate physicians who
use a computer-assisted diagnostic aid. ”Medical Decision Making 27 (2): 189–202.
Balafoutas, Loukas, Helena Fornwagner, Rudolf Kerschbamer, and Matthias Sutter. 2020. “Diag-
nostic uncertainty and insurance coverage in credence goods markets. ”
Bester, Helmut, and Matthias Dahm. 2018. “Credence goods, costly diagnosis and subjective evalu-
ation. ”The Economic Journal 128 (611): 1367–1394.
Brenner, Lukas, and Tobias Meyll. 2020. “Robo-advisors: a substitute for human financial advice?”
Journal of Behavioral and Experimental Finance 25: 100275.
Brody, Howard. 2010. “Medicine’s ethical responsibility for health care reform—the top five list. ”
New England Journal of Medicine 362 (4): 283–285.
Camerer, Colin F, Teck-Hua Ho, and Juin-Kuan Chong. 2004. “ A cognitive hierarchy model of games. ”
The Quarterly Journal of Economics 119 (3): 861–898.
Chan, David C, Matthew Gentzkow, and Chuan Yu. 2022. “Selection with variation in diagnostic
skill: Evidence from radiologists. ”The Quarterly Journal of Economics 137 (2): 729–783.
Charness, Gary, Uri Gneezy, and Vlastimil Rasocha. 2021. “Experimental methods: Eliciting beliefs. ”
Journal of Economic Behavior & Organization 189: 234–256.
Chen, Daniel L, Martin Schonger, and Chris Wickens. 2016. “oTree—An open-source platform for
laboratory, online, and field experiments. ”Journal of Behavioral and Experimental Finance 9:
88–97 .
Chen, Yongmin, Jianpei Li, and Jin Zhang. 2022. “Efficient liability in expert markets. ”International
Economic Review 63 (4): 1717–1744.
Costa-Gomes, Miguel, Vincent P Crawford, and Bruno Broseta. 2001. “Cognition and behavior in
normal-form games: An experimental study. ”Econometrica 69 (5): 1193–1235.
Crawford, Vincent P , and Nagore Iriberri. 2007 . “Level-k auctions: Can a nonequilibrium model
of strategic thinking explain the winner’s curse and overbidding in private-value auctions?”
Econometrica 75 (6): 1721–1770.
Cruickshank, PJ. 1985. “Patient rating of doctors using computers. ”Social Science & Medicine 21 (6):
615–622.
Currie, Janet, and W Bentley MacLeod. 2017 . “Diagnosing expertise: Human capital, decision
making, and performance among physicians. ”Journal of labor economics 35 (1): 1–43.
Dai, Tinglong, and Shubhranshu Singh. 2020. “Conspicuous by its absence: Diagnostic expert
testing under uncertainty. ”Marketing Science 39 (3): 540–563.
Daniels, Marcia, and Steven A Schroeder. 1977 . “Variation among physicians in use of laboratory
tests II. Relation to clinical productivity and outcomes of care. ”Medical care: 482–487 .
Danz, David, Lise Vesterlund, and Alistair J Wilson. 2022. “Belief elicitation and behavioral incen-
tive compatibility. ”American Economic Review 112 (9): 2851–2883.
Dawes, Robyn M, David Faust, and Paul E Meehl. 1989 . “Clinical versus actuarial judgment. ”Science
243 (4899): 1668–1674.
38

Daysal, N Meltem, Sendhil Mullainathan, Ziad Obermeyer, Suproteem K Sarkar, and Mircea
Trandafir. 2022. “ An Economic Approach to Machine Learning in Health Policy. ” Univ. of
Copenhagen Dept. of Economics Discussion, CEBI Working Paper (24).
Dietvorst, Berkeley J, Joseph P Simmons, and Cade Massey. 2015. “ Algorithm aversion: people
erroneously avoid algorithms after seeing them err.. ”Journal of Experimental Psychology: General
144 (1): 114.
Dohmen, Thomas, Armin Falk, David Huffman, Uwe Sunde, Jürgen Schupp, and Gert G Wagner.
2011. “Individual risk attitudes: Measurement, determinants, and behavioral consequences. ”
Journal of the european economic association 9 (3): 522–550.
Doi, Dimitria, Romulo Ribeiro do Vale, Jean Michell Correia Monteiro, Glauco Cabral Marinho
Plens, Mario Ferreira Junior, Luiz Augusto Marcondes Fonseca, Sandro Félix Perazzio, Bruno
Adler Maccagnan Pinheiro Besen, Arnaldo Lichtenstein, Leandro Utino Taniguchi et al. 2021.
“Perception of usefulness of laboratory tests ordering by internal medicine residents in ambu-
latory setting: A single-center prospective cohort study. ”Plos one 16 (5): e0250769 .
Doyle Jr, Joseph J, Steven M Ewer, and Todd H Wagner. 2010. “Returns to physician human capital:
Evidence from patients randomized to physician teams. ” Journal of health economics 29 (6):
866–882.
Dulleck, Uwe, and Rudolf Kerschbamer. 2006. “On doctors, mechanics, and computer specialists:
The economics of credence goods. ”Journal of Economic literature 44 (1): 5–42.
Dulleck, Uwe, and Rudolf Kerschbamer. 2009 . “Experts vs. discounters: Consumer free-riding and
experts withholding advice in markets for credence goods. ”International Journal of Industrial
Organization 27 (1): 15–23.
Dulleck, Uwe, Rudolf Kerschbamer, and Matthias Sutter. 2011. “The economics of credence goods:
An experiment on the role of liability, verifiability, reputation, and competition. ” American
Economic Review 101 (2): 526–555.
Eastwood, Joseph, Brent Snook, and Kirk Luther. 2012. “What people want from their professionals:
Attitudes toward decision-making strategies. ”Journal of Behavioral Decision Making 25 (5): 458–
468.
Frankel, Alexander, and Michael Schwarz. 2014. “Experts and their records. ”Economic Inquiry 52
(1): 56–71.
Groopman, Jerome E, and Michael Prichard. 2007 .How doctors think. vol. 82: Houghton Mifflin
Boston.
Hall, Stephen F, Colleen Webber, Patti A Groome, Christopher M Booth, Paul Nguyen, and Yvonne
DeWit. 2019 . “Do doctors who order more routine medical tests diagnose more cancers? A
population-based study from Ontario Canada. ”Cancer medicine 8 (2): 850–859 .
Hartman, Rachel, Aaron J Moss, Shalom Noach Jaffe, Cheskie Rosenzweig, Leib Litman, and
Jonathan Robinson. 2023. “Introducing connect by CloudResearch: Advancing online partici-
pant recruitment in the digital age. ”
Hilger, Nathaniel G. 2016. “Why don’t people trust experts?” The Journal of Law and Economics 59
(2): 293–311.
Kerschbamer, Rudolf, Matthias Sutter, and Uwe Dulleck. 2017 . “How social preferences shape
incentives in (experimental) markets for credence goods. ” The Economic Journal 127 (600):
393–416.
39

Kleinberg, Jon, Himabindu Lakkaraju, Jure Leskovec, Jens Ludwig, and Sendhil Mullainathan.
2018. “Human decisions and machine predictions. ”The quarterly journal of economics 133 (1):
237–293.
Litman, Leib, Jonathan Robinson, and Tzvi Abberbock. 2017 . “TurkPrime. com: A versatile crowd-
sourcing data acquisition platform for the behavioral sciences. ”Behavior research methods 49
(2): 433–442.
Liu, Fang, Alexander Rasch, Christian Waibel, and Marco A Schwarz. 2020. “The role of diagnostic
ability in markets for expert services. ”
Miyakis, Spiros, Georgios Karamanof, Michalis Liontos, and Theodore D Mountokalakis. 2006.
“Factors contributing to inappropriate ordering of tests in an academic medical department and
the effect of an educational feedback strategy. ”Postgraduate medical journal 82 (974): 823–829 .
Mullainathan, Sendhil, and Ziad Obermeyer. 2022. “Diagnosing physician error: A machine learn-
ing approach to low-value health care. ”The Quarterly Journal of Economics 137 (2): 679–727 .
Nagel, Rosemarie. 1995. “Unraveling in guessing games: An experimental study. ”The American
economic review 85 (5): 1313–1326.
Pesendorfer, Wolfgang, and Asher Wolinsky. 2003. “Second opinions and price competition: Ineffi-
ciency in the market for expert advice. ”The Review of Economic Studies 70 (2): 417–437 .
Promberger, Marianne, and Jonathan Baron. 2006. “Do patients trust computers?” Journal of
Behavioral Decision Making 19 (5): 455–468.
Rasch, Alexander, and Christian Waibel. 2018. “What drives fraud in a credence goods market?–
Evidence from a field study. ”Oxford Bulletin of Economics and Statistics 80 (3): 605–624.
Sandefur, Rebecca L. 2020. “Legal advice from nonlawyers: consumer demand, provider quality,
and public harms. ”Stan. JCR & CL 16: 283.
Schneider, Henry S. 2012. “ Agency problems and reputation in expert services: Evidence from
auto repair. ”The Journal of Industrial Economics 60 (3): 406–433.
Schneider, Tim, and Kilian Bizer. 2017a. “Effects of qualification in expert markets with price
competition and endogenous verifiability. ”CEGE Discussion Papers, Number.
Schneider, Tim, and Kilian Bizer. 2017b. “Expert qualification in markets for expert services: A
Sisyphean Task?” CEGE-Discussion Papers, Number.
Schroeder, Steven A, Alan Schliftman, and Thomas E Piemme. 1974. “Variation among physicians
in use of laboratory tests: relation to quality of care. ” Medical Care: 709–713.
Shaffer, Victoria A, C Adam Probst, Edgar C Merkle, Hal R Arkes, and Mitchell A Medow. 2013.
“Why do patients derogate physicians who use a computer-based diagnostic support system?”
Medical Decision Making 33 (1): 108–118.
Stahl, Dale O, and Paul W Wilson. 1995. “On players models of other players: Theory and experi-
mental evidence. ”Games and Economic Behavior 10 (1): 218–254.
Stahl II, Dale O, and Paul W Wilson. 1994. “Experimental evidence on players models of other
players. ”Journal of economic behavior & organization 25 (3): 309–327 .
Topol, Eric. 2019 .Deep medicine: how artificial intelligence can make healthcare human again.: Hachette
UK.
Tracy, Dustin, Eric Schniter, and Vojtěch Zíka. 2023. “Uncertainty and Reputation Effects in Cre-
dence Goods Markets. ”Available at SSRN 4513820.
Trautmann, Stefan T, and Gijs van de Kuilen. 2015. “Belief elicitation: A horse race among truth
40

serums. ”The Economic Journal 125 (589): 2116–2135.
Wolf, James R. 2014. “Do IT students prefer doctors who use IT?” Computers in Human Behavior 35:
287–294.
Xue, Hao, Yaojiang Shi, Lei Huang, Hongmei Yi, Huan Zhou, Chengchao Zhou, Sarah Kotb, Joseph D
Tucker, and Sean Y Sylvia. 2019 . “Diagnostic ability and inappropriate antibiotic prescriptions:
a quasi-experimental study of primary care providers in rural China. ” Journal of Antimicrobial
Chemotherapy 74 (1): 256–263.
Yeh, D Dante. 2014. “ A clinician’s perspective on laboratory utilization management. ”Clinica chimica
acta 427: 145–150.
Zhi, Ming, Eric L Ding, Jesse Theisen-Toupal, Julia Whelan, and Ramy Arnaout. 2013. “The land-
scape of inappropriate laboratory testing: a 15-year meta-analysis. ”PloS one 8 (11): e78962.
41

Appendix 8. Appendix
FIGURE A1. Threshold ¯ri condition on uncertainty and consumer beliefs.
42

8.1. Payoffs
TABLE A1. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on the
high-ability expert, i.e. xha = 3.
LA0
Invest Not Invest
LA0
Invest 1 (1− α)
Not Invest (1− α) 1
LA0
Invest Not Invest
LA0
Invest 1 0.5R−ri R
Not Invest 0.5R−ri R α+ (1− α) R−2ri R
HA3 Expert Chooses Not Invest HA3 Expert Chooses Invest
TABLE A2. Low-Ability Expert: Expected consumer attraction conditional on on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on the
high-ability expert, i.e. xha = 3.
HA3
Invest Not Invest
LA0
Invest ri R 0
Not Invest
(1− α)0.5ri R+
(1− α)0.5R−ri R 0
HA3
Invest Not Invest
LA0
Invest 0 0
Not Invest 0.5R−ri R α
LA0 Expert Chooses Not Invest LA0 Expert Chooses Invest
If all consumers coordinate on the high-ability expert (Table A1), then the high-ability
expert always chooses to forego the investment. If nobody invests, consumers do not
switch away. Otherwise, not-investing dominates investing. Note that we use α as the
share of consumers who prefer the “safe” option. The term ri R captures the payoff for an
imitating low-ability expert if they successfully attract a consumer. Here, ri describes the
number of rounds after a consumer switches away, i.e., after learning about the low-ability
expert’s true type. LAx denotes the low-ability expert with x consumers at the beginning
of round 11, HA x the equivalent high-ability expert. We use ri instead of ∑3 i=1 ri for ease of
presentation. The payoff term (1− α)∗ R−2ri R always depends on the assumption ri ≤ 0.5R.
If a low-ability expert attracts consumers by not investing after ri R rounds, then the payoff
term R−ri R becomes ri R if ri ≤ 0.5.
43

TABLE A3. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on one
low-ability expert, i.e. xla = 3, and α equals share of consumers for whom ri ≥ ¯ri. All cells
show the expected share of approached consumer rounds.
LA0
Invest Not Invest
LA3
Invest 1 0.5(1− α)+ 0.5(1− α) R−ri R
Not Invest (1− α) R−ri R 0.5R−ri R + 0.5R−2ri R
LA0
Invest Not Invest
LA3
Invest 0 0.5R−ri R
Not Invest 0.5R−ri R α+(1− α) R−2ri R
HA0 Expert Chooses Not Invest HA0 Expert Chooses Invest
TABLE A4. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on one
low-ability expert, i.e. xla = 3, and α equals share of consumers for whom ri ≥ ¯ri. All cells
show the expected share of approached consumer rounds.
HA0
Invest Not Invest
LA0
Invest ri R (1− α) ri R
Not Invest (1− α) ri R ri R
HA0
Invest Not Invest
LA0
Invest 1 0
Not Invest
α+(1− α)
0.5R−ri R α
LA3 Expert Chooses Not Invest LA3 Expert Chooses Invest
TABLE A5. Low-Ability Expert L0: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if all consumers coordinated on
one low-ability expert, i.e. xla = 3, and α equals share of consumers for whom ri ≥ ¯ri. All
cells show the expected share of approached consumer rounds. LA 3 does not invest, HA0
invests.
HA0
Invest Not Invest
LA3
Invest ri R (1− α)0.5ri R
Not Invest (1− α) R−ri R 0.5R−ri R
HA0
Invest Not Invest
LA3
Invest 0 0
Not Invest 0.5R−ri R α
LA0 Expert Chooses Not Invest LA0 Expert Chooses Invest
44

8.2. Mixed Distribution
TABLE A6. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xha = 2. The additional income for
attracting new consumers “x” has no implications for the dominant choice.
LA0
Invest Not Invest
LA1
Invest 1 (1− α) 2 3+ (1− α) 1 3 R−ri R
Not Invest (1− α) 2 3+ (1− α) 1 3 R−ri R 2 3+ 1 3 R−ri R
LA0
Invest Not Invest
LA1
Invest 2 3 0.5R−ri R
Not Invest 0.5R−ri R α+ (1− α) R−2ri R
HA2 Chooses Not Invest HA2 Chooses Invest
TABLE A7. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xla = 1 for this low-ability expert
and xha = 2. HA2
Invest Not Invest
LA0
Invest ri R (1− α) ri 3R
Not Invest
(1− α) 2 3 ri R+
(1− α) 1 3 R−ri R
ri
3R
HA2
Invest Not Invest
LA0
Invest 1 3 0
Not Invest 0.5R−ri R α
LA1 Expert Chooses Not Invest LA1 Expert Chooses Invest
TABLE A8. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xla = 0 for this low-ability expert
and xha = 2. HA2
Invest Not Invest
LA1
Invest ri R (1− α) ri 6R
Not Invest
(1− α) 1 3 ri R+
(1− α) 2 3 R−ri R
R−ri
6R
HA2
Invest Not Invest
LA1
Invest 0 0
Not Invest 0.5R−ri R α
LA0 Expert Chooses Not Invest LA0 Expert Chooses Invest
45

TABLE A9. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xha = 1, xi,la = 2, x j,la = 0.
LA0
Invest Not Invest
LA2
Invest 1 (1− α) 2 3+ (1− α) 1 3( R−ri R )
Not Invest (1− α) 1 3+ (1− α) 2 3( R−ri R ) 1 3 + 1 3( R−ri R )+ 1 3( R−2ri R )
LA0
Invest Not Invest
LA2
Invest 1 3 0.5R−ri R
Not Invest 0.5R−ri R α
HA1 Expert Chooses Not Invest HA1 Expert Chooses Invest
TABLE A10. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xla = 2 and xha = 1.
HA1
Invest Not Invest
LA0
Invest ri R (1− α) 2 3 ri R
Not Invest
(1− α) 2 3 ri R+
(1− α) ri 6R+
(1− α) R−ri 6R
2
3
ri
R
HA1
Invest Not Invest
LA0
Invest 2 3 0
Not Invest 0.5( R−ri R ) α
LA2 Expert Chooses Not Invest LA2 Expert Chooses Invest
TABLE A11. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xla = 0 for this expert and xha = 1.
HA1
Invest Not Invest
LA2
Invest ri R (1− α) 1 3 ri R
Not Invest
(1− α) 1 6 ri R+
(1− α) 5 6 R−ri R
1
3
ri
R
HA1
Invest Not Invest
LA2
Invest 0 0
Not Invest 0.5( R−ri R ) α
LA0 Expert Chooses Not Invest LA0 Expert Chooses Invest
46

TABLE A12. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xha = 0, xi,la = 2, x j,la = 1.
LA2
Invest Not Invest
LA1
Invest 1 (1− α) 1 6+ (1− α) 5 6 R−ri R
Not Invest (1− α) 1 3+ (1− α) 2 3 R−ri R 1 2 R−ri R + 1 2 R−2ri R
LA2
Invest Not Invest
LA1
Invest 0 0.5R−ri R
Not Invest 0.5R−ri R α+(1− α) R−2ri R
HA0 Expert Chooses Not Invest HA0 Expert Chooses Invest
TABLE A13. Low-Ability Expert: Expected consumer attraction of LA2 conditional on the
three experts’ investment choices in round 11 for Algorithm if xha = 0, xi,la = 2, x j,la = 1.
HA0
Invest Not Invest
LA1
Invest ri R (1− α) 5 6 ri R
Not Invest (1− α) 2 3 ri R+ (1− α) 1 3 R−ri R 2 3 ri R+ 1 6 R−ri R
HA0
Invest Not Invest
LA1
Invest 2 3 0
Not Invest 0.5R−ri R α
LA2 Expert Chooses Not Invest LA2 Expert Chooses Invest
TABLE A14. Low-Ability Expert: Expected consumer attraction of LA0 conditional on the
three experts’ investment choices in round 11 for Algorithm if xha = 0, xi,la = 2, x j,la = 1.
HA0
Invest Not Invest
LA2
Invest ri R (1− α) 1 3 ri R+ (1− α) 1 3 R−ri R
Not Invest (1− α) 1 3 ri R+ (1− α) 2 3 R−ri R 1 3 ri R+ 1 3 R−ri R
HA0
Invest Not Invest
LA2
Invest 1 3 0
Not Invest 0.5R−ri R α
LA1 Expert Chooses Not Invest LA1 Expert Chooses Invest
47

8.3. Equal Distribution
TABLE A15. High-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if xha = 1, xi,la = 1, x j,la = 1.
LA1
Invest Not Invest
LA1
Invest 1 (1− α) 1 3+ (1− α) 2 3( R−ri R )
Not Invest (1− α) 1 3+ (1− α) 2 3( R−ri R ) 1 3 + 1 3( R−ri R )+ 1 3( R−2ri R )
LA1
Invest Not Invest
LA1
Invest 1 3 0.5R−ri R
Not Invest 0.5R−ri R α
HA1 Expert Chooses Not Invest HA1 Expert Chooses Invest
TABLE A16. Low-Ability Expert: Expected consumer attraction conditional on the three
experts’ investment choices in round 11 for Algorithm if if xha = 1, xi,la = 1, x j,la = 1.
HA1
Invest Not Invest
LA1
Invest ri R (1− α) 1 2 ri R
Not Invest
(1− α) 1 2 ri R+
(1− α) 1 2 R−ri R
1
3
ri
R+
1
6
R−ri
R
HA1
Invest Not Invest
LA1
Invest 1 3 0
Not Invest 0.5( R−ri R ) α
LA1 Expert Chooses Not Invest LA1 Expert Chooses Invest
48

8.4. Calculations
8.4.1. Separating Equilibria – Only HA Invests
If xha = 3, then high-ability experts always forego the decision aid, and specifically never
opt for investments if the other two experts choose to not invest because 1≥ α+(1−α) R−2ri R .
Assuming that all consumers coordinated on one low-ability expert, if both low-ability
experts do not invest, the high-ability expert only invests if α ≥ 0.25 and ri < 0.5R or
α≥ 0.5− 0.5ri R := αha,0,inv and ri ≥ 0.5R. This can be straightforwardly calculated from the
payoff matrix (Table A3). The low-ability expert without consumers chooses to not invest,
given investments from the high-ability expert and no investments from the second low-
ability expert LA3, if α≤ 1.5− 0.5R ri := αla,0,ninv and ri < 0.5R or α≤ 0.5 and ri ≥ 0.5R. Finally,
the coordinated low-ability expert foregoes investments if ri > 1 3 R and α≤ 3ri−R R+3ri := αla,3,inv.
If ri < 0.5R, then experts can only separate when 0.25 ≤ αla,3,ninv ≤ αla,0,ninv. This implies
ri ≥ 5 9 R, which is ruled out by ri < 0.5R. There is no separation for ri < 0.5R. When
ri ≥ 0.5R, then expert types can only separate if αha,0,inv ≤ αla,3,ninv ≤ 0.5 which holds for
ri ≥ 0.535R. Figure A2 illustrates the separating space, given the conditions that ri ≥ 0.535R
and α ∈ [αha,0,inv, αla,3,inv]. For a small set of parameter values, there are equilibria in
which only the high-ability expert invests, if all consumers coordinate on one low-ability
expert.
What if consumers do not coordinate and xha = 2? Again, we look for the two candidate
equilibria in which either only the high-ability expert or only the low-ability experts invest
(Table A6). First, when ri ≥ 0.5R, the high-ability expert never invests. If ri < 0.5R, the
high-ability expert invests given non-investments from the two low-ability experts when
α> 3R−ri 5R−6ri := αha,2,inv. Then, for both low-ability experts to invest, α< 1.5− 0.5R ri := αla,1,inv
must hold. However αha,2,inv ≤ α ≤ αla,1,inv requires ri ≥ 5 6 R, which violates ri < 0.5R.
Hence, there is no separating equilibrium in which only the high-ability expert invests
for xha = 2. Similarly, while the high-ability expert never invests if they believe the other
two to forego investments, both low-ability experts are then incentivized to also forego
investments and imitate the high-ability expert, precluding any strategic separation.
For xha = 1 and xla = 2, the high-ability experts separates through investments if α> 1− ri R
and ri < 0.5R or α> 2R−ri 3R := αha,1,inv and ri ≥ 0.5R. The equivalent conditions for LA2 are
α< 1.5− 0.5R ri and ri < 0.5R or α< 7ri−2R 4ri+R := αla,20,ninv and ri ≥ 0.5R. For LA0, α< 1.5− 0.5R ri
or α< −0.5(R+ri) ri−2R := αla,02,ninv must hold. Comparing these conditions reveals no possible
separation through high-ability expert investments ifri < 0.5R. As before, when learning is
slow and ri ≥ 0.5R, then separation may arise. Panel (b) in Figure A2 shows the separation
space. When Bayesian consumers take a long time to figure out the imitating low-ability
expert’s true type, e.g., due to small performance differences or noisy feedback, and a
large share of consumers prefers a safe option because of the possibility to accidentally
49

approach an imitating low-ability expert, then high-ability experts may be the only ones
to invest.
After consumers coordinate only on the two low-ability experts with xha = 0, there are
separating equilibria in which only the high-ability expert invests for both ri < 0.5R and
ri ≥ 0.5R (Panels (c) and (d) in Figure A2). The high-ability expert invests if α> 1− 1.5ri R and
ri < 0.5R or α> 0.5(R−ri) R := αha,0,inv and ri ≥ 0.5R. For LA2, α< 1.5− 0.5R ri or α< 2.5ri−0.5R ri+R :=
αla,21,ninv must hold under ri < 0.5R and ri ≥ 0.5R respectively. ForLA1, the condition under
ri ≥ 0.5R changes to α< 0.5(R+ri) 2R−ri := αla,12,ninv. Then, expert types separate in equilibrium
if αha,0,inv < α< αla,12,ninv because αla,12,ninv ≤ αla,21,ninv.
Under an equal consumer distribution at the time of the technological shock, separation
requires again ri ≥ 0.5R. Here, the respective conditions are α> 2R−ri 3R for the high-ability
expert, and α< ri R for each low-ability expert (Panel (e) in Figure A2).
Finally, we look at separation behavior when experts are completely uninformed about
the distribution of the other consumers who did not approach them. Hence, if an expert
has attracted all consumers, they are fully informed. Otherwise, they must incorporate
all different possibilities. Here, we assume that experts assign equal probabilities to all
possible unobservable states. For the high-ability expert, considerations only change if
ri ≥ 0.5R. Then, the high-ability expert only separates through investments if α> R−ri R+2ri :=
αha0,inv,noin f . The low-ability expert’s condition when xla,i = 2 changes to α < 14ri−3R 8ri+3R :=
αla2,ninv,noin f if ri ≥ 0.5R. The low-ability expert’s condition when xla,i = 1 changes to
α< ri R αla1,ninv,noin f if ri ≥ 0.5R. Finally, if a low-ability expert attracts 0 consumers at the
time of the technological shock, separation with an investing high-ability expert requires
α< 8R−5ri 17R−14ri αla0,ninv,noin f ri ≥ 0.5R.
8.4.2. Mixed Equilibria – One LA Invests
If xha = 0, then the respective hyperbolas for the high-ability expert are α< 1.5R−0.5ri 3R−2ri :=
αha0,la21,ninv if LA2 invests, α< 3R−2ri 6R−5ri := αha0,la12,ninv if LA1 invests, α> 5 6 ri R := αla2,ha0,inv
and ri < 0.5R or α > 1.5ri+0.5R 3R := αla2,ha0,inv and ri ≥ 0.5R for LA 2 to invest, and α >
2
3
ri
R := αla1,ha0,inv if ri < 0.5R or α > 1 3 := αla1,ha0,inv if ri ≥ 0.5R when LA1 is the only one
to invest. If all consumers coordinate on one low-ability expert, then there are stable
mixed equilibria in which only LA 3 invests for α > ri R := αla3,ha0la0,inv and α < R 2R−ri :=
αha0,la3la0,ninv. The second low-ability expert always foregoes the decision aid. Similarly, if
only LA0 chooses to rent the decision aid, behavior is stable forα> 0.5R−ri R := αla0,ha0la3,inv
and α < 0.5 := αha0,la0la3,ninv, with LA 3 always ignoring the algorithm. If xha = 1 and
consumers are distributed equally, then the high-ability expert foregoes the decision aid
along α < 1.5R−0.5ri 3R−2ri := αha1,la1la1,ninv, and either low-ability expert invests, if the second
one does not invest, when α > R+ri 6R := αla1,ha1la1,inv. If consumers are not distributed
50

equally and xha = 1, the corresponding hyperbolas if LA 2 invests are α < 1.5R+0.5ri 3R−ri :=
αha,la2la0,ninv, and α > 2 3 ri R := αla2,ha1la0,inv. Once again, in the mixed equilibrium, the
second low-ability expert never switches because it would reveal the high-ability expert’s
type. If LA 0 invests, the hyperbolas are α < 1.5R−0.5ri 3R−2ri := αha,la0la2,ninv and α > 1 3 ri R :=
αla0,ha1la2,inv. If αla0,ha1la2,inv ≤ α < αla2,ha1la0,inv, then only LA 0 invests in equilibrium,
if α ≥ αla2,ha1la0,inv, either does. For xha = 2, the relevant hyperbola for the high-ability
expert is α < 1.5R+0.5ri 3R−ri := αha2,la1la0,ninv irrespective of which low-ability expert invests.
LA1 invests in equilibrium if α > 1 3 ri R := αla1,ha2la0,inv, LA0 if α > 1 6 R−ri R and ri ≥ 0.5R :=
αla0,ha2la1,inv or α> 1 6 ri R := αla0,ha2la1,inv and ri < 0.5R. Finally, if all consumers coordinate
on the high-ability expert, there is no satisfying equilibrium because both low-ability
experts can only poach consumers if they are the only investing expert, and never attract
any consumer by foregoing the decision aid. Hence, the investment decision is largely
inconsequential, and if anything, both should individually invest, revealing the high-ability
expert. Knowing all individual conditions, we can calculate how they change if experts do
not observe the choices of “other” consumers. All results are shown in Table A19.
8.4.3. Level-1-Thinking Experts Pure Separation
When consumers coordinate on the high-ability expert, they forego the decision aid along
α ≤ R+3ri 2(R+ri) for ri < 0.5R and α ≤ 2R+ri 3R := αha3,ninv for ri ≥ 0.5R. Each LA 0 invests along
α≥ 5ri−R 2(R+ri) for r < 0.5R and α≥ ri R αla0,inv for r ≥ 0.5R.
If xha = 2, high-ability experts forego the decision aid along α ≤ 2R+3ri 3R+2ri for r < 0.5R and
α ≤ 7R 9R−2ri := αha2,ninv for r ≥ 0.5R. The hyperbola for the low-ability expert with xla = 1
to switch from investing to not-investing is α ≥ 19ri−5R 2(3R+4ri) for ri < 0.5R and α ≥ 3(5ri−R) 4(2R+ri) :=
αla1,inv for ri ≥ 0.5R. For LA0, it is α≥ 17ri−3R 6R+7ri for ri < 0.5R and α≥ 7ri+2R 10R−ri := αla0,inv for ri ≥
0.5R. Hence, there are separating strategies for αla1,inv < αla0,inv < α≤ αha2,ninv.
For xha = 1 and xla = 2, the high-ability expert prefers no investment alongα≤ 8R−3ri 3(3R−ri) for ri <
0.5R and α≤ 7R−ri 3(3R−ri) := αha1,la2la0,ninv for ri ≥ 0.5R. LA2 invests if α≥ 23ri−7R 2(3R+5ri) for ri < 0.5R
and α ≥ 21ri−6R 7R+8ri := αla2,ha1la0,inv for ri ≥ 0.5R. Finally, LA0 invests if α ≥ 19ri−3R 2(3R+4ri) for ri <
0.5R and α ≥ 9ri+2R 11R−2ri := αla0,ha1la2,inv for ri ≥ 0.5R. Again, strategic separation occurs for
αla2,ha1la0,inv < αla0,ha1la2,inv < α≤ αha1,ninv.
Under equal consumer distribution, we get α ≤ 4(2R−ri) 9R−4ri for ri < 0.5R and α ≤ 7R−2ri 9R−4ri :=
αha1,la1,ninv for ri ≥ 0.5R for HA1 as the high-ability expert’s hyperbolas, and α≥ 13ri−R 9R+3ri :=
αla1,ha1,inv for the low-ability expert LA 1.
When all consumers coordinate on the low-ability expert LA 3, the high-ability expert fore-
goes the decision aid along α ≤ 4R 4R+ri for ri < 0.5R and α ≤ 5R−2ri 3(2R−ri) := αha0,la3,ninv for ri ≥
0.5R. LA0 invests if α≥ 2R+ri 4R−ri := αla0,la3,inv, and LA3 along α≥ 3(3ri−R) 3R+5ri := αla3,inv.
51

Finally, under xha = 0, xla,i = 1 and xla, j = 2, the high-ability expert does not use the
decision aid for α ≤ 4(2R−ri) 9R−4ri for r < 0.5R and α 7R−2ri 9R−4ri := αha0,la2la1,ninv for ri ≥ 0.5R. LA1
invests along α ≥ 3R+7ri 2(6R−ri) := αla1,ha0la2,inv, and LA 2 if α ≥ 19ri−4R 8R+7ri := αla2,ha0la1,inv. Table
A20 summarizes all conditions for separation depending on the distribution of consumers
at the time of the shock.
If experts cannot observe the distribution of other consumers, then the conditions change
for low-ability experts with x ≤ 2 and high-ability experts with x ≤ 1. This has implica-
tions for most distributions. If xha = 3, then the two low-ability experts invest along α≥
−144R4+1062R3ri+2786R2r2 i+1257Rr3 i−353r4 i
8(R+ri)( 3R+4ri)( 4R−ri)( 6R+7ri) for ri < 0.5R and LA0 and α≥ 194R4+545R3ri−257R2r2 i+32Rr3 i−r4 i 2R(10R−ri)(11R−2ri)(4R−ri) :=
αla0,inv,noin f for ri ≥ 0.5R and LA0. Ifxha = 2, then LA1 invests alongα≥ −225R3+1731R2ri+1091Rr2 i−77r3 i 18(3R+4ri)(3R+ri)(6R−ri) for r <
0.5R and α≥ −102R3+1733R2ri+584Rr2 i−55r3 i 36(2R+ri)(3R+ri)(6R−ri) := αla1,inv,noin f for r ≥ 0.5R. For LA0, the condition
is the same as above. Ifxha = 1, high-ability experts forego alongα≤ 144R2−119Rri+24r2 i 6(3R−ri)(9R−4ri) for ri <
0.5R and α≥ 63R2−38Rri+5r2 i 3(3R−ri)(9R−4ri) := αha1,ninv,nin f for ri ≥ 0.5R. LA2 considers the possibilities of
xha = 1 or xla = 1, resulting in α≥ −80R2+209Rri+351r2 i 4(3R+5ri)(8R+7ri) for ri < 0.5 andα≥ −76R2+227Rri+299r2 i 2(7R+8ri)(8R+7ri) :=
αla2,inv,nin f for ri ≥ 0.5R. For LA3, nothing changes because they know that they monopo-
lize the market. Finally, if the high-ability expert has not attracted any consumers, they
face α ≤ 2(17R2−6Rri−r2 i ) (9R−4ri)(4R+ri) for ri < 0.5R and α ≤ 87R2−71Rri+14r2 i 6(2R−ri)(9R−4ri) := αha0,ninv,nin f for ri ≥ 0.5R.
Table X summarizes these conditions.
52

8.5. Figures Expert Separation
53

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
ha, 0, inv
la, 3, inv
= 0.5
D

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 1, inv
la, 20, ninv
la, 02, ninv
E

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 0, inv
la, 21, ninv
la, 12, ninv
F

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 0, inv
la, 21, ninv
G

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 111, inv
la, 111, ninv
H

FIGURE A2. Expert type separating equilibria (PBE). Only the high-ability expert invests.
Panel (a) shows the separating space when xla = 3. Panel (b) shows the same for xha = 1
and xla = 2. Panels (c) and (d) show separation when xha = 0, xla,i = 2 and xla, j = 1 for
ri < 0.5R and ri ≥ 0.5R respectively. In panel (e), consumers are distributed equally.
54

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha0, inv, noinf
la, 3, inv
la0, ninv, noinf
D

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 1, inv
la2, ninv, noinf
la0, ninv, noinf
E

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP1R6HSDUDWLRQ
= 0.5
ha0, inv, noinf
la1, ninv, noinf
la2, ninv, noinf
F

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 0, inv
la, 21, ninv
G

     
ri
R






6HSDUDWLQJ
(TXLOLEULXP
1R6HSDUDWLRQ
= 0.5
ha, 1, inv
la1, ninv, noinf
H

FIGURE A3. Expert type separating equilibria (PBE) when the distribution of other con-
sumers is unknown. Only the high-ability expert invests. Panel (a) shows the separating
space when xla = 3. Panel (b) shows the same for xha = 1 and xla = 2. Panels (c) and (d)
show separation when xha = 0, xla,i = 2 and xla, j = 1 for ri < 0.5R and ri ≥ 0.5R respectively.
In panel (e), consumers are distributed equally.
55

FIGURE A4. Mixed equilibria in which only one low-ability expert invests when the
distribution of other consumers is unknown. Panel (a) shows the mixed space when
xha = 0, xla,i = 2, xla, j = 1, Panel (b) when xha = 0, xla,i = 2, xla, j = 1, Panel (c) when xha = 0,
xla,i = 3, xla, j = 0, (d) when xha = 0, xla,i = 0, xla, j = 3.
56

FIGURE A5. Mixed equilibria in which only one low-ability expert invests when the
distribution of other consumers is unknown. Panel (a) shows the mixed space when
xha = 1, xla,i = 1, xla, j = 1, Panel (b) when xha = 1, xla,i = 2, xla, j = 0, Panel (c) when xha = 1,
xla,i = 0, xla, j = 2, (d) when xha = 2, xla,i = 1, xla, j = 0, (e) when xha = 2, xla,i = 0, xla, j = 1.
57

FIGURE A6. Expert type strategic separation under level-1 thinking (bounded rationality)
when the distribution of other consumers is unknown. Only the high-ability expert does
not invests. Panel (a) shows the separating space when xha = 3. Panel (b) shows the same
for xha = 2 and xla = 1. Panel (c) shows separation for xha = 1 and xla = 2, (d) when xha = 1,
xla,i = 1 and xla, j = 1. Panel (e) illustrates separation under xha = 0, xla,i = 2, xla, j = 1 and
Panel (f ) under xla = 3.
58

8.6. Figures and Tables
TABLE A17. Separating Equilibria Conditions Only HA Invests
Equilibrium Description Conditions ( α) Threshold Definitions
Case: xla = 3 – separation possible for r i ≥ 0.5R where αha,0,inv ≤ α≤ αla,3,ninv
Only HA0 invests α≥ αha,0,inv αha,0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 0.25 if ri < 0.5R 0.5− 0.5ri R if ri ≥ 0.5R
LA0 does not invest α≤ αla,0,ninv αla,0,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 1.5− 0.5R ri if ri < 0.5R 0.5 if ri ≥ 0.5R
LA3 does not invest α≤ αla,3,ninv αla,3,ninv := 3ri−R R+3ri
Case: xha = 1, xla = 2 – separation possible only if r i ≥ 0.5R.
Only HA1 invests α> αha,1,inv αha,1,inv :=
⎧⎪⎪⎨⎪⎪⎩ 1− ri R if ri < 0.5R 2R−ri 3R if ri ≥ 0.5R
LA2 does not invest α< αla,20,ninv αla,20,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 1.5− 0.5R ri if ri < 0.5R 7ri−2R 4ri+R if ri ≥ 0.5R
LA0 does not invest α< αla,02,ninv αla,02,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 1.5− 0.5R ri if ri < 0.5R −0.5(R+ri) ri−2R if ri ≥ 0.5R
Case: xha = 0 – separation requires αha,0,inv < α< αla,12,ninv
Only HA0 invests α> αha,0,inv αha,0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 1− 1.5ri R if ri < 0.5R 0.5(R−ri) R if ri ≥ 0.5R
LA2 does not invest α< αla,21,ninv αla,21,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 1.5− 0.5R ri if ri < 0.5R 2.5ri−0.5R ri+R if ri ≥ 0.5R
LA2 does not invest α< αla,12,ninv αla,12,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 1.5− 0.5R ri if ri < 0.5R 0.5(R+ri) 2R−ri if ri ≥ 0.5R
Case: equal consumer distribution – separation possible only if r i ≥ 0.5R.
Only HA1 invests α> αha,1,inv see above for ri ≥ 0.5R
LA1 invests α< αla,eq,ninv αla,eq,ninv := ri R
59

TABLE A18. Mixed Equilibria Conditions
Equilibrium Description Conditions ( α) Threshold Definitions
Case: xha = 0
HA0 α< αha0,la21,ninv αha0,la21,ninv := 1.5R−0.5ri 3R−2ri
Only LA2 invests α> αla2,ha0,inv αla2,ha0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 5 6 ri R if ri < 0.5R 1.5ri+0.5R 3R if ri ≥ 0.5R
HA0 α< αha0,la12,ninv αha0,la12,ninv := 3R−2ri 6R−5ri
Only LA1 invests α> αla1,ha0,inv αla1,ha0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 2 3 ri R if ri < 0.5R 1 3 if ri ≥ 0.5R
Consumers coordinate on LA3
HA0 α< αha0,la3la0,ninv αha0,la3la0,ninv := R 2R−ri
Only LA3 invests α> αla3,ha0la0,inv αla3,ha0la0,inv := ri R
HA0 α< αha0,la0la3,ninv αha0,la0la3,ninv := 0.5
Only LA0 invests α> αla0,ha0la3,inv αla0,ha0la3,inv := 0.5R−ri R
Case: xha = 1
Equal consumer distribution:
HA1 α< αha1,la1la1,ninv αha1,la1la1,ninv := 1.5R−0.5ri 3R−2ri
Either LA1 invests α> αla1,ha1la1,inv αla1,ha1la1,inv := R+ri 6R
Unequal consumer distribution:
HA1 α< αha1,la2la0,ninv αha,la2la0,ninv := 1.5R+0.5ri 3R−ri
Only LA2 invests α> αla2,ha1la0,inv αla2,ha1la0,inv := 2 3 ri R
HA1 α< αha1,la0la2,ninv αha,la0la2,ninv := 1.5R−0.5ri 3R−2ri
Only LA0 investsa α> αla0,ha1la2,inv αla0,ha1la2,inv := 1 3 ri R
Case: xha = 2
HA2 α< αha2,la1la0,ninv αha2,la1la0,ninv := 1.5R+0.5ri 3R−ri
Only LA1 α> αla1,ha2la0,inv αla1,ha2la0,inv := 1 3 ri R
HA2 α< αha2,la1la0,ninv (same as above)
Only LA0 invests α> αla0,ha2la1,inv αla0,ha2la1,inv :=
⎧⎪⎪⎨⎪⎪⎩ 1 6 ri R if ri < 0.5R 1 6 R−ri R if ri ≥ 0.5R
Case: All consumers coordinate on high-ability expert b
a If α≥ αla2,ha1la0,inv, either LA can invest. If αla0,ha1la2,inv ≤ α< αla2,ha1la0,inv, only LA0 invests.
b No stable mixed equilibrium exists where only one LA invests. Both LAs investing would reveal
the HA type.
60

TABLE A19. Mixed Equilibria Conditions if Distribution and Investments Are Not Observ-
able
Equilibrium Description Conditions ( α) Threshold Definitions
Case: xha = 0
HA0 does not invest α< αha0,ninv,mixed αha0,ninv,mixed := 144R3−252R2ri+138Rr2 i −23r3 i 8(3R−2ri)(6R−5ri)(2R−ri)
Only LA2 invests α> αla2,inv,mixed αla2,inv,mixed :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 9R2+18Rri−5r2 i 12R(3R−ri) if ri < 0.5R 12R2+11Rri−3r2 i 12R(3R−ri) if ri ≥ 0.5R
Only LA1 invests α> αla1,inv,mixed αla1,inv,mixed :=
⎧⎪⎪⎨⎪⎪⎩ R+7ri 18R if ri < 0.5R R+ri 6R if ri ≥ 0.5R
Consumers coordinate on one LA
Only LA3 invests α> αla3,inv,mixed αla3,inv,mixed := ri R
Only LA0 invests α> αla0,inv,mixed αla0,inv,mixed :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 18R2−15Rri+4r2 i 18R(3R−2ri) if ri < 0.5R 21R2−23Rri+8r2 i 18R(3R−2ri) if ri ≥ 0.5R
Case: xha = 1
HA1 does not invest α< αha1,inv,mixed αha1,inv,mixed := 9R2−5Rri 2(3R−2ri)(3R−ri)
Equal consumer distribution:
Either LA1 invests α> αla1,inv,mixed αla1,inv,mixed :=
⎧⎪⎪⎨⎪⎪⎩ R+7ri 18R if ri < 0.5R R+ri 6R if ri ≥ 0.5R
Unequal consumer distribution:
Only LA2 invests α> αla2,inv,mixed αla2,inv,mixed :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 9R2+18Rri−5r2 i 12R(3R−ri) if ri < 0.5R 12R2+11Rri−3r2 i 12R(3R−ri) if ri ≥ 0.5R
Only LA0 invests α> αla0,inv,mixed αla0,inv,mixed :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 18R2−15Rri+4r2 i 18R(3R−2ri) if ri < 0.5R 21R2−23Rri+8r2 i 18R(3R−2ri) if ri ≥ 0.5R
Case: xha = 2
HA2 does not invest α< αha2,ninv,mixed αha2,la1la0,ninv := 1.5R+0.5ri 3R−ri
Only LA1 invests α> αla1,inv,mixed see above
Only LA0 invests α> αla0,inv,mixed see above
Case: All consumers coordinate on High-ability expert b
a If α≥ αla2,ha1la0,inv, either LA can invest. If αla0,ha1la2,inv ≤ α< αla2,ha1la0,inv, only LA0 invests.
b No stable mixed equilibrium exists where only one LA invests. Both LAs investing would reveal
the HA type.
61

TABLE A20. Conditions for Strategic Expert Separation under Expert Level-1 Thinking
Equilibrium Description Conditions ( α) Threshold Definitions
Case: xha = 3
HA No Investment α≤ αha3,ninv αha3,ninv :=
⎧⎪⎪⎨⎪⎪⎩ R+3ri 2(R+ri) if ri < 0.5R 2R+ri 3R if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv αla0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 5ri−R 2(R+ri) if ri < 0.5R ri R if ri ≥ 0.5R
Case: xha = 2
HA No Investment α≤ αha2,ninv αha2,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 2R+3ri 3R+2ri if ri < 0.5R 7R 9R−2ri if ri ≥ 0.5R
LA1 Investment α≥ αla1,inv αla1,inv :=
⎧⎪⎪⎨⎪⎪⎩ 19ri−5R 2(3R+4ri) if ri < 0.5R 3(5ri−R) 4(2R+ri) if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv αla0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 17ri−3R 6R+7ri if ri < 0.5R 7ri+2R 10R−ri if ri ≥ 0.5R
Case: xha = 1, xla = 2
HA No Investment α≤ αha1,la2la0,ninv αha1,la2la0,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 8R−3ri 3(3R−ri) if ri < 0.5R 7R−ri 3(3R−ri) if ri ≥ 0.5R
LA2 Investment α≥ αla2,ha1la0,inv αla2,ha1la0,inv :=
⎧⎪⎪⎨⎪⎪⎩ 23ri−7R 2(3R+5ri) if ri < 0.5R 21ri−6R 7R+8ri if ri ≥ 0.5R
LA0 Investment α≥ αla0,ha1la2,inv αla0,ha1la2,inv :=
⎧⎪⎪⎨⎪⎪⎩ 19ri−3R 2(3R+4ri) if ri < 0.5R 9ri+2R 11R−2ri if ri ≥ 0.5R
Case: Equal Consumer Distribution
HA1 No Investment α≤ αha1,la1,ninv αha1,la1,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 4(2R−ri) 9R−4ri if ri < 0.5R 7R−2ri 9R−4ri if ri ≥ 0.5R
LA1 Investment α≥ αla1,ha1,inv αla1,ha1,inv := 13ri−R 9R+3ri
Case: xla = 3
HA No Investment α≤ αha0,la3,ninv αha0,la3,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 4R 4R+ri if ri < 0.5R 5R−2ri 3(2R−ri) if ri ≥ 0.5R
LA0 Investment α≥ αla0,la3,inv αla0,la3,inv := 2R+ri 4R−ri
LA3 Investment α≥ αla3,inv αla3,inv := 3(3ri−R) 3R+5ri
Case: xha = 0, xla,1 = 1, xla,2 = 2
HA No Investment α≤ αha0,la2la1,ninv αha0,la2la1,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 4(2R−ri) 9R−4ri if ri < 0.5R 7R−2ri 9R−4ri if ri ≥ 0.5R
LA1 Investment α≥ αla1,ha0la2,inv αla1,ha0la2,inv := 3R+7ri 2(6R−ri)
LA2 Investment α≥ αla2,ha0la1,inv αla2,ha0la1,inv := 19ri−4R 8R+7ri
62

TABLE A21. Conditions for Strategic Expert Separation under Expert Level-1 Thinking if
Consumer Distribution Is Not Observable
Equilibrium Description Conditions ( α) Threshold Definitions
Case: xha = 3
HA3 No Investment α≤ αha3,ninv :=
⎧⎪⎪⎨⎪⎪⎩ R+3ri 2(R+ri) if ri < 0.5R 2R+ri 3R if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv,noin f :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ −144R4+1062R3ri+2786R2r2 i +1257Rr3 i −353r4 i 8(R+ri)(3R+4ri)(4R−ri)(6R+7ri) if ri < 0.5R 194R4+545R3ri−257R2r2 i +32Rr3 i −r4 i 2R(10R−ri)(11R−2ri)(4R−ri) if ri ≥ 0.5R
Case: xha = 2
HA2 No Investment α≤ αha2,ninv :=
⎧⎪⎪⎨⎪⎪⎩ 2R+3ri 3R+2ri if ri < 0.5R 7R 9R−2ri if ri ≥ 0.5R
LA1 Investment α≥ αla1,inv,noin f :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ −225R3+1731R2ri+1091Rr2 i −77r3 i 18(3R+4ri)(3R+ri)(6R−ri) if ri < 0.5R −102R3+1733R2ri+584Rr2 i −55r3 i 36(2R+ri)(3R+ri)(6R−ri) if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv,noin f see above
Case: xha = 1, xla = 2
HA1 No Investment α≤ αha1,ninv,noin f :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 144R2−119Rri+24r2 i 6(3R−ri)(9R−4ri) if ri < 0.5R 63R2−38Rri+5r2 i 3(3R−ri)(9R−4ri) if ri ≥ 0.5R
LA2 Investment α≥ αla2,inv,noin f :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ −80R2+209Rri+351r2 i 4(3R+5ri)(8R+7ri) if ri < 0.5R −76R2+227Rri+299r2 i 2(7R+8ri)(8R+7ri) if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv,noin f see above
Case: Equal Consumer Distribution
HA1 No Investment α≤ αha1,ninv,noin f see above
LA1 Investment α≥ αla1,inv,noin f see above
Case: xla = 3
HA0 No Investment α≤ αha0,ninv,noin f :=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ 2(17R2−6Rri−r2 i ) (9R−4ri)(4R+ri) if ri < 0.5R 87R2−71Rri+14r2 i 6(2R−ri)(9R−4ri) if ri ≥ 0.5R
LA0 Investment α≥ αla0,inv,noin f see above
LA3 Investment α≥ αla3,inv := 3(3ri−R) 3R+5ri
Case: xha = 0, xla,1 = 1, xla,2 = 2
HA0 No Investment α≤ αha0,ninv,noin f see above
LA1 Investment α≥ αla1,inv,noin f see above
LA2 Investment α≥ αla2,inv,noin f see above
63

2 4 6 8 10 12 14
Round
0.4
0.5
0.6
0.7
0.8
0.9
1.0Probability of Being Low-Ability Expert
Bayesian Consumer Beliefs (10.000 simulations)
2 4 6 8 10 12 14
Round
0.00
0.05
0.10
0.15
0.20
0.25
0.30Probability of Being Low-Ability Expert
Bayesian Consumer Beliefs (10.000 simulations)
FIGURE A7. Left: Consumer Belief Updating with Pr(L)= 0.4 (blue) andPr(L)= 0.2 (orange)
when Low-Ability Experts only choose the HQT. Right: Pr(L)∈ {0.1, 0.05, 0.01}.
0
.1
.2
.3
.4
.5
.6
.7
0 2 4 6 8 10
share undertreatment share overtreatment
Phase 1
0
.1
.2
.3
.4
.5
.6
.7
10 15 20 25
share undertreatment share overtreatment
Treatment: Skill Investments
0
.1
.2
.3
.4
.5
.6
.7
10 15 20 25
share undertreatment share overtreatment
Treatment: Algorithmic Decision Aid
FIGURE A8. Share of undertreatment and overtreatment in (left) the first 10 rounds (middle)
Phase 2 of Skill and (right) Phase 2 of Algorithm
.
0
.1
.2
.3
.4
.5
0 2 4 6 8 10
High Ability Expert Share P
big
Low Ability Expert Share P
big
0
.1
.2
.3
.4
.5
0 2 4 6 8 10
High Ability Expert Share P
small
Low Ability Expert Share P
small
0
.1
.2
.3
.4
.5
0 2 4 6 8 10
High Ability Expert Share P
equal
Low Ability Expert Share P
equal
FIGURE A9. Expert price setting Pm, Ps and Pe in Phase 1.
TABLE A22. Consumer Approaching Behavior
Pm Ps Pe
Invested -0.122 ∗∗ 0.159∗∗∗ -0.088∗
(0.039) (0.031) (0.040)
N 1,455 1,665 1,635
This table reports marginal effects of a pooled fixed effects panel logistic regression. The dependent
variable is a binary variable that equals 1 if the expert chooses the respective price vector. ∗ p< 0.05,∗∗
p< 0.01,∗∗∗ p< 0.001
64

FIGURE A10. Price setting depending on treatment, expert type and investment decision.
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
m
Not Invested HA Expert Share P
m
Invested LA Expert Share P
m
Not Invested LA Expert Share P
m
Algorithm
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
s
Not Invested HA Expert Share P
s
Invested LA Expert Share P
s
Not Invested LA Expert Share P
s
Algorithm
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
e
Not Invested HA Expert Share P
e
Invested LA Expert Share P
e
Not Invested LA Expert Share P
e
Algorithm
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
m
Not Invested HA Expert Share P
m
Invested LA Expert Share P
m
Not Invested LA Expert Share P
m
Skill
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
s
Not Invested HA Expert Share P
s
Invested LA Expert Share P
s
Not Invested LA Expert Share P
s
Skill
0
.1
.2
.3
.4
.5
.6
.7
.8
10 15 20 25
Invested HA Expert Share P
e
Not Invested HA Expert Share P
e
Invested LA Expert Share P
e
Not Invested LA Expert Share P
e
Skill
TABLE A23. Frequencies of expert prices in Phase 2.
Expert
HA Invested HA Not Invested LA Invested LA Not Invested
Algorithm
Pm: 18.6%
Ps: 61.1%
Pe: 20.4%
Pm: 20.2%
Ps: 31.2%
Pe: 48.6%
Pm: 26.3%
Ps: 40.3%
Pe: 33.3%
Pm: 39 .5%
Ps: 29%
Pe: 31.5%
Skill
Pm: 44.9%
Ps: 35.7%
Pe: 19 .3%
Pm: 50.4%
Ps: 24.1%
Pe: 25.5%
Pm: 25.9%
Ps: 46.2%
Pe: 27 .9%
Pm: 27 .1%
Ps: 44.9%
Pe: 27 .9%
65

TABLE A24. Overtreatment Conditional on Expert Price Setting
Phase 1 Skill Algorithm
Overtreated (1) (2) (3) (1) (2) (3) (1) (2) (3)
Pm 0.094∗ 0.120 0.111
(0.047) (0.054) (0.084)
Ps -0.228∗∗∗ -0.232∗∗ -0.199∗∗
(0.041) (0.054) (0.066)
Pe 0.119∗ 0.081 0.055
(0.046) (0.084) (0.082)
N 856 856 856 652 652 652 664 664 664
This table reports marginal effects of panel logistic regressions using subject-level random effects
and a cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The
dependent variable is a binary variable that equals 1 if the consumers experiences overtreatment. ∗
p< 0.05,∗∗ p< 0.01,∗∗∗ p< 0.001
66

TABLE A25. Consumer Approaching Behavior
Phase 1 Skill Algorithm Algorithm
Undertreated -0.519 ∗∗ -0.539∗∗∗ -0.465∗ -0.473∗
(0.169) (0.212) (0.220) (0.221)
Overtreated 0.089 0.047 0.075 0.088
(0.098) (0.097) (0.038) (0.095)
Pe Baseline Baseline Baseline Baseline
Pm 0.574∗∗ 0.620∗∗ 1.174∗∗∗ 1.297∗∗
(0.174) (0.225) (0.283) (0.402)
Ps -0.770∗∗∗ -0.803∗∗∗ -0.748∗∗∗ -0.661∗∗
(0.167) (0.215) (0.138) (0.229)
Not_Invested 0.059 -0.262 -0.386
(0.276) (0.166) (0.209)
High-Ability 0.905
(0.503)
Not_Invested× Pe 0.393
(0.375)
High-Ability× Pe -0.683
(0.363)
Not_Invested× High-Ability× Pe 0.849∗
(0.421)
N 1,350 1,125 1,125 1,125
This table reports results of a panel ordered logistic regressions using subject-level random effects
and a cluster–robust VCE estimator at the matched group level (standard errors in parentheses). The
dependent variable is an ordinal variable that captures the number of consumers (0 - 3) who approached
the expert in the current round. Undertreated and Overtreated are lagged variables (one round).∗ p< 0.05,
∗∗ p< 0.01,∗∗∗ p< 0.001
67

FIGURE A11. Left: High-Ability Expert Investment Behavior conditional on incentivized
beliefs that investments decrease consumer beliefs in high ability type (negative) or
increase beliefs in high ability type (positive). Right: Non-incentivized beliefs.
0
.2
.4
.6
.8
10 15 20 25
HA Expert Negative Beliefs Investment Shares Low Ability Expert HA Expert Positive Beliefs
.2
.4
.6
.8
10 15 20 25
HA Expert Negative Beliefs HA Expert Positive Beliefs Investment Shares Low Ability Expert
FIGURE A12. Left: Expert beliefs about how consumer beliefs about the expert’s ability
type change after the expert chooses to invest. Right: Consumer beliefs that an expert is
high-ability after investing.
0
.005
.01
.015
Change in Likelihood that Expert is Perceived as HA
-100 -50 0 50 100
0
.01
.02
.03
.04
Consumer Belief that Expert is HA after investing
0 20 40 60 80 100
68

FIGURE A13. Left: Consumer beliefs about the likelihood that an expert does not use the
decision aid after renting it. Right: Consumer beliefs that investing expert does not use
the decision aid correctly.
0
.01
.02
.03
Consumer Belief that Expert does not use Algorithm
0 20 40 60 80
0
.01
.02
.03
Consumer Belief that Expert does not use Algorithm correctly0 20 40 60 80
TABLE A26. Experiment 2: Expert Investment Behavior in Phase 2
Repeated Repeated One-Shot One-Shot
High-Ability -0.181 ∗ -0.179∗ -0.1222 -0.111
(0.082) (0.079) (0.092) (0.093)
Round -0.095 ∗
(0.037)
Risk 0.015 -0.000
(0.015) (0.017)
Female 0.008 -0.095
(0.074) (0.113)
Age -0.004 0.001
(0.004) (0.004)
N 1125 1125 150 150
This table reports marginal effects of panel logistic regressions using subject-level random effects and a
cluster–robust VCE estimator at the matched group level (for repeated, standard errors in parentheses)
and marginal effects of equivalent logistic regressions (one-shot). The dependent variable is a binary
variable that equals 1 if the expert invests into the new diagnostic technology. ∗ p< 0.05,∗∗ p< 0.01,∗∗∗
p< 0.001
69

FIGURE A14. Expert investment shares in repeated and one-shot by ability type and belief
type. A negative belief indicates that experts belief consumers will find an investing expert
less likely to be of high ability type.
0.65
0.88
0.00
1.00
0.76
0.91
0.50
0.58
0
.2
.4
.6
.8
1
Investment Share in Round 11
Repeated Repeated One-Shot One-Shot
HA_Positive LA_Positive HA_Negative LA_Negative
HA_Positive LA_Positive HA_Negative LA_Negative
FIGURE A15. One-Shot. Left: Expert beliefs about how consumer beliefs about the expert’s
ability type change after an expert chooses to invest. Right: Consumer beliefs that an
expert is high-ability after investing.
0
.002
.004
.006
.008
.01
Change in Likelihood that Expert is Perceived as HA
-50 0 50 100
0
.01
.02
.03
.04
Consumer Beliefs that Expert is HA after Investing
0 20 40 60 80 100
70

FIGURE A16. One-Shot. Left: Consumer beliefs about the likelihood that an expert does not
use the decision aid after renting it. Right: Consumer beliefs that investing expert does
not use the decision aid correctly.
0
.01
.02
.03
.04
.05
Consumer Beliefs that Expert does not use Algorithm
0 20 40 60 80
0
.01
.02
.03
Consumer Beliefs that Expert does not use Algorithm correctly0 20 40 60 80 100
71
