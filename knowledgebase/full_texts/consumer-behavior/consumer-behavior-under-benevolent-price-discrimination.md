---
title: Consumer Behavior under Benevolent Price Discrimination
url: https://arxiv.org/abs/2404.03581
category: consumer-behavior
subcategory: empirical
date: 2024-04
venue: ''
authors:
- Alexander Erlei
- Mattheus Brenig
- Nils Engelbrecht
source: arxiv
pdf_url: https://arxiv.org/pdf/2404.03581
pages: 31
chars: 78467
fetched_at: '2026-11-08T13:07:04+00:00'
kb_version: 1
---

# Consumer Behavior under Benevolent Price Discrimination

Consumer Behavior under Benevolent Price
Discrimination
Alexander Erlei, Mattheus Brenig, Nils Engelbrecht
April 2024
Extensive research shows that consumers are generally averse to price discrimination.
However, instruments of differential pricing can benefit consumer surplus and alleviate
inequity through targeted price discounts. This paper examines how these outcome
considerations influence consumer reactions to price discrimination. Six studies with
3951 participants show that a large share of consumers is willing to costly switch away from
a store that introduces a discount for low-income consumers. This happens irrespective
of whether income differences are due to luck or merit. While the price-discriminating
store does attract some new high-income consumers, it cannot compensate the loss of
existing consumers. Allowing for altruistic preferences by simulating a market mechanism
increases costly support for price discounts, but does not alleviate consumer aversions.
Finally, we provide evidence that warm glow drives costly support for price discounts.
Keywords: price discrimination, pricing, altruism, inequity aversion, warm glow, con-
sumer behavior
JEL Codes: D12, C91, C99 , D30, D90
Corresponding author: Alexander Erlei, alexander.erlei@wiwi.uni-goettingen.de, ORCiD: 0000-0001-7322-2761.
Chair for Economic Policy and SME Research, Georg-August-University Goettingen.
We gratefully acknowledge financial support by the Lower Saxony Ministry of Science and Culture under
grant number ZN3492 within the Lower Saxony “Vorab“ of the Volkswagen Foundation and the Center for
Digital Innovations (ZDIN)
arXiv:2404.03581v1  [econ.GN]  4 Apr 2024

1. Introduction
Technological progress, especially the advent of big data, has reduced the technological
and informational constraints on sellers to differentiate prices among consumers (Calvano
et al. 2020; Musolff 2022). This development holds great economic potential for firms, as
uniform prices prevent them from fully leveraging consumer valuations above the market
price, while simultaneously pricing-out consumers with a lower willingness-to-pay (WTP).
Importantly, it also implies potential benefits to consumer welfare and inequality. Those
who are otherwise excluded from the market – often due to lower financial means – may
be able to access previously closed markets under more personalized pricing, i.e. third-
degree price discrimination. For example, Dubé and Misra (2023) present data from two
field experiments showing that personalized pricing benefits the majority of consumers
while also increasing seller profits. In turn, high-WTP consumers pay a substantially
higher fee. Aryal, Murry, and Williams (2023) analyze data from international airline
markets and find that using private information about passengers benefits overall welfare
by increasing seller and leisure passenger surplus at the expense of business passengers
(see also Williams (2022)).
Despite these straightforward incentives, most sellers still hesitate to deviate from
uniform pricing strategies (Fudenberg and Villas-Boas 2012; Della Vigna and Gentzkow
2019). In a striking example, Dubé and Misra (2023) estimate that, in 2015, personalized
pricing could have increased ZipRecruiter’s expected profits by 86% compared to their
uniform price (and by 19% compared to the theoretically optimal uniform price). One
commonly evoked explanation for the lack of realized price discrimination is that sellers
anticipate the risk of antagonizing consumers by violating their fairness perceptions (Xia,
Monroe, and Cox 2004; Cox 2004; Fabiani et al. 2006; Haws and Bearden 2006; Bolton,
Keh, and Alba 2010; Ferguson, Ellen, and Bearden 2014). Indeed, research has shown
that profit-seeking through price discrimination is often inhibited by negative consumer
reactions (Kahneman, Knetsch, and Thaler 1986; Leibbrandt 2020; Allender et al. 2021).
Recently, these sentiments have been echoed throughout many media outlets as well as
reports from e.g. the US-American Council of Economic Advisors (CEA, 2015), the German
Federal Data Ethics Committee (DEC, 2019) or the European Union (EU). 1 The latter even
codified a right to complete price transparency into law, highlighting the consumer’s
crucial role for the adoption of price discrimination. Thus, in addition to technological
constraints, firms also face “behavioral constraints” when deciding on their price setting
strategy.
1CEA: https://obamawhitehouse.archives.gov/sites/default/files/whitehouse_
files/docs/Big_Data_Report_Nonembargo_v2.pdf; DEC: https://www.bmi.bund.de/
SharedDocs/downloads/DE/publikationen/themen/it-digitalpolitik/gutachten-
datenethikkommission.html; EU: https://gdpr.eu/
1

These observations open up an intriguing puzzle. On the one hand, third-degree price
discrimination can increase overall economic welfare and simultaneously decrease in-
equity through reduced prices for low-income consumers. On the other hand, consumers
social preferences appear to enforce uniform pricing and thereby prevent firms from
opening up the market. This makes a straightforward argument for the need of an im-
proved understanding about which factors determine consumer behavior under price
discrimination, and the conditions that might alleviate seller constraints.
In this paper, we experimentally explore the behavioral mechanisms behind consumer
reactions to differential pricing that favors low-income consumers who cannot afford the
uniform price. We focus on benevolent price discrimination (BPD), defined as a policy of
differential pricing that is downward-bound and always benefits financially disadvantaged
groups or individuals, thereby leading to a convergence of outcomes. Because sellers
cannot increase prices, BPD improves joint welfare, while also creating a more equitable
distribution of consumer gains. High-income consumers do not experience any absolute
economic losses, but are relatively disadvantaged by price discrimination. Thus, our main
focus lies on situations where targeted price discounts allow previously excluded low-
income consumers to participate in a market, without (negatively) affecting the welfare of
other consumers.
One prominent real-life example is the Supplemental Nutrition Assistance Program
(SNAP) administered administered by the U.S. Department of Agriculture (USDA). In 2019 ,
the department started a pilot program whereby consumers eligible for SNAP where
allowed to use food stamps to buy groceries at participating online retailers, among them
Walmart and Amazon. In addition to food-related items, Amazon offers some further
benefits to SNAP-customers, such as an over 50% discount for their subscription service
Amazon Prime. They also do not try to obfuscate their participation, as eligible items are
marked with an "SNAP EBT eligible" label. Hence, while there is a lot of evidence that
consumers are generally averse to price discrimination, there appear to be exceptions.
Indeed, there is a long history of sellers offering specific discounts to certain groups of the
population, like students or the elderly. What it is exactly that drives the acceptance of such
programs is not yet known, although several researchers have speculated that inequality
concerns are likely to play an important role (Rotemberg 2011; Wu et al. 2012). Identifying
the specific mechanisms behind consumer choices from real-world data is complicated by
the fact that consumers operate in a highly endogenous environment that usually allows
for several distinct explanations. Even for a program like SNAP , eligibility hinges on several
criteria such as income, work requirements, resource requirements, constrained housing
expenditure, or immigrant status. Moreover, SNAP is publicly financed, participants only
have access to a specific selection of products or services, and must exert personal effort
during the application process. This makes it virtually impossible to parse which specific
2

elements determine the programs apparent widespread acceptance. We therefore use an
experimental approach to abstract from various cultural and context-dependent factors,
thereby avoiding behavioral distortions induced by residual variables and isolating the
effects of specific economic factors on consumer behavior.
Our conceptualization differentiates between (1) process-related fairness concerns
and (2) social preferences over the outcome of an transaction, i.e. the realized economic
gains and their distribution. There is unanimity in the pricing literature that consumers
are generally averse towards the process of price discrimination, and thus often oppose
different prices for the same good – particularly if they are disadvantaged (Campbell
1999; Haws and Bearden 2006; Maxwell 2007; Leibbrandt 2020). Here, prices paid by other
consumers, i.e. the consumer’s peers, serve as an external reference point, whereby the
consumer assesses if an offered price is fair (Thaler 1985; Janiszewski and Lichtenstein
1999; Jin, He, and Zhang 2014).2 Deviations from the reference point usually lead to averse
reactions, including lower purchase satisfaction (Shor and Oliver 2006), intentions to
spread negative word-of-mouth (Ferguson, Ellen, and Bearden 2014) and, most importantly,
switching to a different seller or terminating the trade relationship (Ho and Su 2009; Ho,
Su, and Wu 2014; Anderson and Simester 2008; Leibbrandt 2020; Allender et al. 2021).
However, price discrimination that benefits low-income consumers, and especially
BPD, also aligns positively with a number of pro-social concerns that have been thoroughly
documented in the economic literature. One, there is ample evidence that people care
about the equal distribution of economic outcomes (Fehr, Kirchsteiger, and Riedl 1993;
Harrington Jr, Gonzalez, and Kujal 2016), particularly if existing income inequalities are
seen as arbitrary (Rutström and Williams 2000; Alesina and Angeletos 2005; Durante,
Putterman, and van der Weele 2014). People tend to be inequity averse, and experience
disutility when their outcome is different from other people’s outcomes, or when they
receive an unequal share of the total surplus (Fehr and Schmidt 1999; Bolton and Ockenfels
2000). This effect is stronger for disadvantaged individuals, but has also been extensively
documented for those with distributional advantages. Thus, as long as differential pricing
leads to a convergence of consumer outcomes, and nobody incurs any additional losses,
it may not only by accepted by consumers, but even be desirable.
Second, we argue that support for BPD is consistent with impure altruism (Andreoni
1990). Altruistic people care about the economic outcomes of others, and will therefore
incur utility losses if their actions harm others. In a competitive market environment,
punishing sellers for introducing targeted price discounts discourages future BPD, which
hurts low-income consumers in the long run by pricing them out of the market. Thus,
altruistic preferences may alleviate negative consumer reactions towards BPD. In addition
2Next to peer-induced fairness concerns, there are also distributional fairness concerns that relate to the
seller’s profit. Usually, these appear to be substantially less important as long as peer prices are not being
obfuscated (Ho and Su 2009; Allender et al. 2021).
3

to that, research on impure altruism shows that many people derive non-monetary utility
through "warm glow" when helping others. For example, when donating to a charity,
people experience private benefits that are not motivated by the gains of the recipients,
but the contribution as such. People feel good about donating to charities, even if they
provide no tangible benefits. Beyond the economics of giving (see also Ottoni-Wilhelm,
Vesterlund, and Xie 2017; Korenok, Millner, and Razzolini 2013), private provision of
public goods through altruism or warm-glow has also been documented in cooperative
(Andreoni 1995; Palfrey and Prisbrey 1997; Goeree, Holt, and Laury 2002) and labor-market
like gift-exchange environments (Cox 2004; Charness and Haruvy 2002). We argue that
switching towards a price-discriminating store that offers goods to low-income consumers
at reduced prices might evoke similar non-monetary rewards, thereby increasing the
private provision of attainable prices for low-income individuals. This implies costly
consumer support for sellers who introduce BPD.
To the best of our knowledge, we are the first to systematically analyze consumer
reactions towards price discounts that are exclusively targeted at low-income consumers
who were previously excluded from the market. We are also the first ones to quantify
the effects of consumer altruism and warm glow preferences on sellers price setting
constraints.
Study Overview
We conduct a series of pre-registered, incentivized, context-neutral and controlled experi-
mental studies using Amazon Mechanical Turk (MTurk) and CloudResearch. Sellers can
offer a price discount for previously excluded low-income consumers, enabling them to
purchase in their store and thereby leading to a convergence in consumer outcomes. Price
discrimination is transparent, and high-income consumers can either costly switch to a
second seller who does (not) offer the discount, choose not to buy at all, or maximize their
income by staying with the same seller across all rounds. By quantifying both, behavioral
shifts away and towards the price discriminating seller, we capture bidirectional consumer
migration patterns that have so far been largely neglected by the experimental literature.
This allows us to make qualitative judgments about the net-effect of BPD, rather than
focusing solely on the behavioral constraints elicited by current consumers.
The first three studies establish consumer’s baseline behavior under BPD and analyze
the impact of inequity concerns. Our results show widespread aversions towards BPD.
Across the three experiments, 30% – 40% of consumers exhibited strictly BPD-averse
purchasing patterns, with little to no effect evidence that an equalization of outcomes
mitigates negative reactions. Controlling for reciprocity concerns by keeping sellers out of
the price-setting process does not change the results, and high-income consumers appear
indifferent to the cause of income inequality. That is, irrespective of whether the initial
4

consumer incomes are allocated randomly or via a subject’s performance in a real-effort
task, aversion remains high. Costly support for the BPD-seller is virtually non-existent.
Study 4 introduces a market mechanism that gives high-income consumers some
agency over future prices, i.e. future low-income consumer outcomes. This allows for
altruism, and possibly induces feelings of warm glow. We find marginal evidence that
altruism may slightly alleviate consumer constraints towards BPD when income differ-
ences are generated randomly. Generally, aversions persists. Contrary to studies 1 – 3,
a sizeable number of consumers is willing to costly support targeted price discounts by
switching towards the price-discriminating seller when their purchases influence the
store’s future pricing strategy. Allowing for altruism doubles the share of consumers who
exhibit strictly pro-pd behavior, and more than triples the number of goods sold by the
seller. However, consumer aversions still substantially outweigh consumer support.
Study 5 systematically varies switching costs for both paradigms. In line with warm
glow effects, we expect higher switching costs to increase costly consumer support for
BPD, and reduce the share of consumers switching away from the price discriminating
seller. The experimental data confirms these predictions.
Finally, we provide two robustness checks that are detailed in the online appendix. 3
First, using qualitative data, we confirm the validity of our behavioral interpretations,
showing that a large share of consumers reports to costly switch away from the price
discriminating store due to being unfairly passed over for the price discount. Second, we
conduct a sixth large study that varies low-income consumers willingness-to-pay for the
product, showing that consumer aversions and support are independent of purchase-level
inequity attitudes.
2. Experimental Design and Theory
Because the basic experimental setup was the same across all studies, we will describe it
here in more detail and refer to this description in the remainder of the paper.
Experimental Design
We ran purchasing experiments where consumers had the option to buy a homogeneous
good at one of two stores, each run by another participant acting as store manager. We
measure preferences for or against price discrimination by a consumer’s store choice. We
included a post-experimental questionnaire measuring participants’ fairness perceptions,
attitudes towards price discrimination as well as a questionnaire on social comparison
(Gibbons and Buunk 1999). Summary statistics can be found in the online appendix. All
3The complete data set, additional information and this project’s code can be accessed under the following
repository: https://osf.io/sztnh/?view_only=fc170dcbfeda431e994b23ed095d8b4b
5

experiments in this paper were conducted online using MTurk, CloudResearch and oTree
(Chen, Schonger, and Wickens 2016). Participants enrolled on their own accord and were
randomly assigned to one treatment and one role. After the instructions, participants had
two attempts to answer five comprehension questions correctly. Those who failed both
attempts were excluded from participating. We used “Coins” as our experimental currency.
Coins were later converted into dollars, where 10 coins equaled 3 cents. Additionally,
subjects playing the role of “consumer” received a fixed payment of $1.20 for completing
the survey. There were two main experimental paradigms to analyze consumer behavior:
One-Shot and Repeated.
One-Shot
Upon arrival, participants were randomly assigned the role of either a high-income or a
low-income consumer. High-income (low-income) consumers learned that they would
receive an endowment of 100 (50) Coins. Coins could be used to buy a good at one of two
stores (A, B). In both stores, the good returned a value of 150 Coins to a consumer’s final
payoff. Thus, consumers were incentivized to always buy the good. The two stores sold the
same good and were identical except for one thing: one store offered all consumers the
good for a price of 100 Coins. The other store offered low-income consumers the good for a
discounted price of 50 Coins and charged high-income consumers the regular price of 100
Coins. Consumers learned that each store was run by a manager, who had decided on the
pricing strategy of the store beforehand, and that managers earned money for each good
sold in their store. This ensured that consumer purchasing choices were meaningful.
Participants decided at which of the two stores they wanted to purchase the good.
High-income consumers could observe that one store offered the good at a price of 50
Coins and learned with a click that they were not eligible for that discount. However, in
Studies 1 and 2, no explanation for the different prices was given. We randomized the
position (left, right) and name (A, B) of the store introducing price discrimination. Thus, if
price discrimination had no impact, we would expect consumers to be equally distributed
across both stores.
Repeated
Compared to the one-shot design, consumers completed four purchasing rounds. We did
not change the basic parameters of the experiment. High-income consumers received
100 Coins each round and could use them to purchase the good in either store A or store B.
Low-income consumers were not able to purchase a good in the first two rounds and had
to rely on an outside option that was a simple multiplier of one and always available to
all consumers. Endowments could not be transferred from one round to another. Thus,
6

we can rule out that consumers may respond to a switch in sellers pricing strategies by
delaying their purchases in anticipation of future discounts (Coase 1972).
To make switching meaningful, we introduced monetary costs for switching between
stores in two consecutive rounds. Consumers always started a round in the store they
chose the previous round. For example, if a consumer purchased the good in store A in
the first round, they started the second round in store A. If the consumer then decided
to switch and purchase the good in store B, they had to pay a fee of 10 Coins, i.e. 10 %
of their endowment per round, after the purchase. Thus, consumers were monetarily
disincentivized to switch.
In the first two purchasing rounds, both stores offered the good for the same price.
After the second round, consumers learned that one of the two store managers changed
their pricing strategy and would offer low-income consumers the good for a price of
50 Coins in the remaining two rounds. Depending on treatment, this was either (i) the
manager of the store consumers had purchased in during the second round ( Avoid) or
(ii) the manager of the store consumers had not purchased in during the second round
(Approach). Price discrimination was transparent to all consumers.
This setup imposes stricter conditions on observing consumer preferences against
price discounts. Subjects who switch away from (or towards) the price discriminating
store are willing to substantially reduce their own payoff. Second, it allows us to analyze
benevolent price discrimination, where consumers who already participate in the market
do not experience a price increase and only low-income consumers who priorly could
not purchase any goods benefit from lower prices. Whereas in the one-shot design, con-
sumers might perceive the lower price to be at their own costs, the within-subject design
establishes the reference price of 100 Coins over two rounds. Importantly, low-income
consumers miss out on substantial payoff over the first two rounds, and the price discount
in rounds three and four serves to mitigate, but not fully eliminate unequal outcomes.
Manager
In each treatment, two participants were assigned the role of a store manager. Before
consumers made their choices, managers were free to decide whether they wanted to
implement a discount for low-income consumers in their store. In theRepeated treatments,
price discounts could only be introduced after the second round. Managers had full
information about the experimental setup. We gathered observations until we had one
manager who decided for and one who decided against price discrimination for each
experimental treatment. Hence, no deception was involved. Managers were rewarded
with a base reward of $0.50 and earned 1 Cent for each good sold in their store.
7

Theory
To illustrate how the different variables described above might affect purchasing behavior
under BPD, we introduce a short stylized theoretical section. The model concentrates
on high-income consumer’s switching decision in the Repeated paradigm after the intro-
duction of price discounts for low-income consumers. High income consumers can use
their endowment ehc to buy a good at their current store ( s= 0) that returns w for price
phc = ehc. Alternatively, the high-income consumer can switch to a second store ( s = 1)
and buy the same good for the same price, but pay additional switching costs c. In Avoid,
the current store introduces price discrimination, in Approach, the second store reduces
prices for low-income consumers ( plc). Thus, s = 1 measures preferences against price
discrimination in Avoid, and preferences for price discrimination in Approach. For the
very basic case where high-income consumers receive no contextual information and
observe price discounts, switching behavior for Avoid might be described by a simple
reference point model (see Leibbrandt 2020):
(1) Uavoid i (w, phc, plc)=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w− γi(phc− plc) if s= 0 w− c if s= 1
Here, γi ≥ 0 captures an individual’s aversion towards paying a higher price than other
consumers, i.e. disutility induced by procedural price unfairness (phc > plc).4 For Approach,
utility-maximizing high-income consumers (almost) never switch because they cannot
meaningfully evaluate the price changes beyond the reference point effect. In that case,
not switching is clearly the dominant choice:
(2) Ua p proach i (w, phc, plc)=
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w if s= 0 w− c− γi(phc− plc) if s= 1
Inequity Aversion and (Impure) Altruism
When high-income consumers learn about the benevolent nature of price discrimina-
tion, switching away becomes less attractive. First, the existence of low-income con-
sumers induces inequity considerations. Specifically, high-income consumers in Avoid
who change stores might experience disutility due to advantageous inequity concerns
4We do not explicitly analyze social preferences over seller surplus. Our experimental setup minimizes
seller information, and focuses on peer-comparison between consumers. The reference point model also
does not exclude disutility due to perceived seller gains. In prior work on bargaining where people negotiate
with a seller in the presence of peers, fairness concerns towards peers were substantially stronger than
towards the seller (Ho and Su 2009).
8

(Fehr and Schmidt 1999)5:
(3) Uavoid i =
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w− γi(phc− plc) if s= 0 w− c− βi max {0, w− elc} if s= 1
The degree of aversion from being distributionally ahead is captured by βi ≥ 0. For
example, a consumer who perceives their high-income status to be a result of random
luck might exhibit a higher β compared to those who earned larger endowments through
hard or productive work. Staying in the price-discriminating store alleviates inequity
considerations, as both consumer types earn the same amount of money by purchasing
the same good.
Conversely, BPD in Approach causes new opportunity costs for staying in the store
without price discounts because high-income consumers receive the option to decrease
inequities by switching towards the BPD-store:
(4) Ua p proach i =
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w− βi max {0, w− elc} if s= 0 w− c− γi(phc− plc) if s= 1
Second, in addition to the alleviation of inequity concerns, high-income consumers
who purchase at the BPD-store and thereby support higher economic returns for low-
income consumers might derive warm glow and altruism utility (Andreoni 1990). Warm
glow refers to the satisfaction an individual experiences through the act of giving to others.
It might be the primary explanation for giving behavior – such as charitable donations
– in large-scale economies (Ribar and Wilhelm 2002; Luccasen and Grossman 2017). In
our setup, warm glow only functions in the Approach paradigm. That is because high-
income consumers who approach the BPD-store essentially pay a cost, c, to support
a purchasing option that increases low-income consumer income. 6 It is thus closely
analogous to the private provision of a re-distributive, charitable mechanism. High-income
consumers choose between consuming w or w− c, where the switching costs determine
(and constrain) the amount of quasi-giving. In return, they receive additional utility ki(c).
Furthermore, consumers in both paradigms might exhibit altruistic preferences towards
low-income consumers and therefore derive utility from BPD because it increases the
latter’s consumption from elc to w. We define π= w− elc. Following impure altruism, the
5High-income consumers can never earn less than low-income consumers. Hence, there are no disadvan-
tageous inequity concerns.
6Since warm glow functions independent of the recipient’s output, it is not even necessary to assume
that purchasing behavior by high-income consumers actually influences market supply. However, because
consumers in the current setup are second movers, the effect might still depend on the existence of some
future impact that allows consumers to frame their switching decision as a "good deed" .
9

TABLE 1. High-income consumer utility functions by study and switching paradigm.
Uavoid i Ua p proach i
Stay Switch Stay Switch
Study 1 & 2 w− γi(phc− plc) w− c w w − c− γi(phc− plc)
Study 3 w− γi(phc− plc) w− c− βi max {0, w− elc} w− βi max {0, w− elc} w− c− γi(phc− plc)+ ki(c)
Study 4, 5 & 6 w− γi(phc− plc) w− c− βi max {0, w− elc}− ki(π) w− βi max {0, w− elc} w− c− γi(phc− plc)+ ki(c, π)
additional utility from switching towards the BPD-store ki(c, w− elc) then depends on both
warm glow and altruism:
(5) Ua p proach i =
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w− βi max {0, w− elc} if s= 0 w− c− γi(phc− plc)+ ki(c, π) if s= 1
Here, ki(c, π) is a quasi-concave, strictly increasing utility function for individual i.
Note that ki(c, π) only holds if consumers’ switching behavior influences the pricing
strategy of the BPD-store (Study 4 & 5). Otherwise (Study 3), additional utility only depends
on giving (ki(c)). Finally, altruistic preferences can increase the utility costs of avoidance
behavior when consumer choices influence future price-setting. Switching away from
the seller with price discounts reduces the probability of lower prices for low-income
consumers in the future and thereby decreases their potential consumption level:
(6) Uavoid i =
⎧⎪⎪⎪⎨⎪⎪⎪⎩ w− γi(phc− plc) if s= 0 w− c− βi max {0, w− elc}− ki(π) if s= 1
As Table 1 shows, our studies gradually build on these stylized intuitions, allowing for
increasingly more social preferences to determine switching behavior.
3. Studies 1 – 3: Reference Prices and Inequity Aversion
We first present three studies that quantify baseline consumer behavior under benevolent
price discrimination and introduce the possibility of inequity concerns. In the first two,
subjects do not receive information about the beneficiaries of BPD, and cannot infer that
the discounts lead to more equal outcomes. This precludes social considerations or prefer-
ences from affecting purchasing choices and provides a baseline for consumer behavior
towards relatively disadvantageous price discounts. It is also a relevant approximation of
many real-world contexts, where it is virtually impossible or too costly for consumers to
10

verify the specific circumstances behind differential pricing.
The third study extends that design by two crucial features. First, consumers observe
income as the variable of discrimination. Second, we introduce different causes of in-
come inequality. Endowments are either allocated randomly (Random) or based on the
performance (Effort) in a real-effort slider task (Gill and Prowse 2012). 7 Consumers in
Effort know that their performance influences their endowment, but are not informed
about the exact functional relationship, and thus do not know the specific endowment
levels of other consumers.
Compared to studies 1 – 2, high-income consumers know that (i) low-income con-
sumers exist, (ii) low-income consumers cannot afford to buy a good for the initial uniform
price, (iii) only low-income consumers benefit from price discrimination and (iv) high-
and low-income consumers can afford the same amount of goods under price discrimi-
nation. Hence, Study 3 reveals the benevolent nature of price discounts to high-income
consumers. Importantly, this also implies that low-income consumers can never earn
more than, or even the same as high-income consumers. This rules out disadvantageous
inequity as a motivation for high-income consumers.
If consumer behavior towards BPD is determined by inequity considerations, we would
expect fewer subjects to costly switch away from the BPD-seller in Study 3. Furthermore,
high-income consumers in Effort may exhibit stronger behavioral aversions than those in
Random because BPD undermines a merit-based advantage, which decreases the inequity
parameter β. For Approach, we expected some consumers to costly support the price
discriminating store due to warm glow effects. However, such an effect depends on the
consumers ability to frame their purchasing choice as a "good deed" , which may require
the possibility of having some tangible impact on other peoples utility. In that case, costly
support would not differ between studies.
Experimental Design
Studies 1 and 2 follow the basic procedure outlined above. In Study 1, participants are
randomly assigned to One-Shot, Repeated-Avoid or Repeated-Approach. We gathered data
until we had 100 high-income consumers in each treatment and set a fixed probability of
10% to become a low-income consumer.
Study 2 focuses on Repeated-Avoid to control for reciprocity towards the seller as
a main driver of consumer behavior. Without any information about either the goal,
reasons or beneficiaries of price discrimination, consumers are free to interpret the
manager’s actions in a variety of manners. Following attribution theory, people exhibit
7Consumers receive either the high or the low endowment based on a fixed performance threshold of 31
sliders over three rounds of 60 seconds each. Here, we follow a pretest with 100 participants and select the
cut-off at the 10th percentile.
11

TABLE 2. Study Overview – Repeated Paradigm
Study 1 Study 2 Study 3 Study 4 Study 5 Study 6 (OA)
Avoid Approach Avoid Approach Avoid Approach Avoid Approach Avoid Approach Avoid Approach
Transparent BPD X X X – ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
No Intention X X ✓ – X X X X X X X X
Effort X X X – ✓ ✓ ✓ ✓ ✓ X ✓ ✓
Random X X X – ✓ ✓ ✓ ✓ X ✓ ✓ ✓
No Agency ✓ ✓ ✓ – ✓ ✓ ✓ ✓ X X X X
Agency X X X - X X ✓ ✓ ✓ ✓ ✓ ✓
Switching Costs 10 10 10 – 10 10 10 10 5, 15, 30 5, 15, 30 10 10
wlow_income 150 150 150 150 150 150 150 150 150 150 70, 100, 130 70, 100, 130
N 96 97 391 – 197 200 586 589 367 444 479 505
Female % 47 47 52 – 47 45 49 50 54 43 45 48
strong tendencies to infer causes and assign responsibilities or intentions when they
perceive some outcome to be unfair (Heider 1982; Blount 1995; Falk, Fehr, and Fischbacher
2008). This may induce high-income consumers to punish managers because they want
to negatively reciprocate the act of being intentionally passed over for a discount. To
address this, we eliminate any intentionality behind price discrimination by keeping
managers out of the price-setting process. Instead, consumers learn that each manager
decided to install a pricing algorithm, without the ability to predict changes. For a detailed
description of the study, please refer to the online appendix. Here, we only focus on the
results, to substantiate the importance of peer-comparison for consumer behavior. We
run two treatments (Intention vs. No Intention) with 200 observations each.
Finally, Study 3 consists of six treatments within a 2 (Random vs. Effort) x 3 (One-Shot vs.
Repeated-Avoid vs. Repeated-Approach) between-subject design. We gathered observations
until we had 100 high-income consumers in each treatment with a fixed probability of 10%
to become a low-income consumer. The basic procedure mirrors Study 1. In Random, we
add one page where participants learn about the random endowment mechanism. InEffort,
participants first complete three rounds of a slider-based effort task. After being informed
about their endowment, we ask whether it would be fair if every consumer received the
same endowment, and whether it is fair that (1) endowments are allocated randomly or (2)
better performances in the slider task are rewarded with a higher endowment. Consumers
then proceeded with the original instructions. Those who completed the effort task but
failed to answer the comprehension questions were paid the base reward of $1.20.
Study 1 & 2
We always exclude all observations where a subject chose the outside option in the second
round. This leaves us with 96 independent observations in Avoid, 97 independent observa-
tions in Approach and 100 in One-Shot. See Table 2 for an overview of participant-samples
and treatments across all studies in this article.
12

One-Shot
From now on, we will refer to high-income consumers as “consumers” . Low-income con-
sumers are irrelevant for our analysis and only serve to avoid deception. As hypothesized,
a large majority of consumers prefers the non-price-discriminating store. Without any
explanation for the observed price discrimination, 86 % of consumers purchase the good
in the store that charged all consumers the same price, 9 % purchase in the store with
price discounts and 5 % choose the outside option. A one sample t-test also confirms
consumers to significantly prefer the non-price-discriminating store ( t = 14.25, p< 0.001).
The name (˜χ2 = 1.33, p= 0.25) and position (˜χ2 = 1.66, p= 0.20) of the store introducing
price discrimination do not have a significant effect on store choice.
Repeated-Avoid
In the first two rounds, both stores offer the good for the same price. After the second
round, consumers learn that the store they chose in the second round offers some con-
sumers lower prices. Figure 1 illustrates the two most common behavioral patterns in the
Avoid treatment.
1 2 3 4
0
1
Round
Bought in PD-Store
self-interested: 47 %
1 2 3 4
0
1
Round
anti-pd 40 %
FIGURE 1. The two most common behavioral patterns in Avoid
The two most common purchase patterns were “self-interested” and “anti-pd” . Consumers classified
as self-interested never switched to the other store. Consumers classified as anti-pd stayed within
the same store for the first two rounds and then switched after their store introduced price
discrimination.
We find that 47 % of consumers never switch and maximize their payoff. We classify
those consumer as “self-interested” . Surprisingly, almost as many consumers decide to
costly switch away from a benevolently price-discriminating store. We classify those
consumers who stay in the same store for the first two rounds, switch after the second
round, and stay in the other store for the third and fourth round as “anti-pd” . Note that we
13

can largely rule out distributional motives towards the managers’ income as a reason for
consumer switching for two reasons. One, we did not tell participants how many rounds
they would play. Thus, consumers who wanted both managers to earn the same would
have already switched in the second round. A few consumers exhibited these egalitarian
preferences. Two, we asked subjects after the experiment Who do you think made more
profit throughout this task? Here, the majority of “anti-pd” (79%) and “self-interested” (86%)
subjects stated that the manager they switched towards (or stayed in) made more or equal
profits. This result replicates throughout the studies of this article. Subjects do not choose
the manager they think to be worse off. 8
40 % of consumers exhibit the conservative “anti-pd” pattern. We run a paired t-test to
test whether consumers are less likely to purchase in the price discriminating store after it
has introduced price discrimination, i.e. in round three and four. On average, consumers
purchase 1.91 out of 2 goods in round one and two in the price-discriminating store, and
only 1.04 out of 2 in rounds three and four (t =−8.64, p< 0.001).
Throughout this paper, we will use a random effects panel logistic regression model
with clustered standard errors to confirm and expand on our findings. In accordance with
the results above, we report a significant and large negative effect of the BPD-dummy on a
subject’s probability to purchase in the price-discriminating store (see Tables A1 and A2
in the appendix).
Study 2: Intentions
We replicate our results from Study 1 when controlling for manager intentions by keeping
them out of the price-setting process. In Intention (No Intention), 37 % (30 %) of consumers
are willing to costly switch away from a benevolently price-discriminating store, while
45 % (49 %) act monetarily self-interested. The average number of goods sold by the
price-discriminating store decreases significantly with the introduction of price discrimi-
nation in round three and forth in both Intention (t =−13.23, p< 0.001) and No Intention
(t =−11.02, p< 0.001). There is moderate evidence that controlling for manager intentions
slightly alleviates consumer aversions, as the regression model reveals a significant in-
teraction between the introduction of BPD and Intention (see Table A1), suggesting that
subjects are less likely to purchase in the price-discriminating store after the introduction
of BPD when the decision is made by a store manager instead of a pricing algorithm.
However, at-test comparing the average number of goods sold by the price-discriminating
store during rounds three and four in Intention (0.98) and No Intention (1.09) shows no
significant difference (t = 1.1, p= 0.270). We take these results as evidence that consumer
8Generally, the most popular answer was that the manager subjects purchased in after the second round
also made the largest profits. Additionally, text data from an open-ended question in the questionnaire of
later studies also strongly confirms the validity of our interpretation. Almost no consumer ever refers to
either manager’s income.
14

aversion towards downward price-discrimination is not primarily driven by negatively
reciprocal actions following an ascription of manager intentions.
Repeated-Approach
In Approach, the store not chosen by the consumer in the second round introduces price
discrimination. This setup was designed to capture positive reactions towards BPD. As
predicted, 80 % of consumers follow the self-interested pattern, whereas only 4 % switch
to the price-discriminating store. A paired t-test shows no significant differences in the
likelihood that a consumer purchased the good in the price-discriminating store between
rounds 1 and 2 versus 3 and 4. On average, consumers purchase 0.07 out of 2 goods in round
one and two in the price-discriminating store, and 0.12 out of 2 after the introduction of
price discrimination in rounds three and four (t = 0.96, p= 0.339).
Study 3
One-Shot
In Effort, consumers find a hypothetically equal distribution of endowments significantly
more unfair than in Random (Effort: 2.52, Random: 6.42; t = 18.31, p p< 0.001). They also
find the mechanism by which differences in endowments are achieved significantly fairer
(Effort: 6.37 ,Random: 4.22; t =−9 .34,p< 0.001). This affirms that subjects in Effort perceive
differences in income and thereby different purchasing abilities as more fair, presumably
because they are rooted in merit. Regarding store choices, consumers in the one-shot
experiment still exhibit strong aversions against price discrimination, albeit weaker than
in Study 1. In Random, almost 67 % of consumers choose to purchase in the non-price-
discriminating store. In Effort, the share is around 72 %. The difference is not significant
(t = 1.46, p= 0.146).
Repeated-Avoid
Results for the manipulation check are in line with the ones from One-Shot and confirm
the success of our intervention. In Avoid, we largely replicate the results from Study 1 for
both Effort and Random (see Figure 2).
Surprisingly, we find no differences between price discrimination over merit-based
compared to arbitrary income inequality. In both treatments, one third of consumers
is willing to costly switch to a non-price-discriminating store. Note that this is with the
information that only low-income consumers who are otherwise not able to participate in
the market benefit from price discrimination, while nobody incurs any income losses.
Consumers purchase significantly less goods in the price discriminating store after the
introduction of price discrimination (Effort: 1.11 vs. 1.86,t =−7 .61,p< 0.001;Random: 1.11 vs.
15

0 10 20 30 40 50 60 70 80 90
Avoid, Random
Avoid, Eﬀort
Approach, Random
Approach, Eﬀort
0 100%
17
18.56
14
17
33
31.96
5
4
50
49.48
81
79
Self-interested anti-pd (Avoid) pro-pd (Approach) Other behavioral patterns
FIGURE 2. Behavioral patterns across the four conditions from Study 3.
1.88, t =−8.22, p< 0.001). There is no significant treatment difference (t =−0.10, p= 0.923)
and a random effects logistic regression reveals no significant interaction between Effort
and the introduction of BPD over the whole sample (see Table A1).
Repeated-Approach
In accordance with Study 1, almost no consumer is willing to costly support a benevolently
price discriminating store. Instead, the majority of consumers exhibits self-interested
behavior patterns (Effort: 79 %, Random: 81 %). Only four and five percent respectively
follow the pro-pd pattern. Pairedt-tests suggest that consumers do not significantly change
their behavior once the other store introduces price discrimination ( Effort: 0.17 vs. 0.11,
t = 1.10, p= 0.275; Random: 0.15 vs. 0.11,t = 0.68, p= 0.495).
Discussion
A large share of consumers rejects relatively disadvantageous price-discrimination and is
willing to pay money in order to switch towards a seller with uniform pricing. This pattern
holds for BPD where consumers are aware that price discounts only benefit low-income
consumers who are otherwise excluded from the market. Hence, the equalization of
consumer outcomes does not appear to be a sufficient condition for sellers to introduce
targeted price discounts. In contrast to many other documented scenarios in the context
of economic inequality and re-distributive preferences, consumers appear to disregard
the cause of income inequality. One possible explanation might simply be that procedural
fairness judgments, i.e. charging different prices for the same good, are much more
important in determining consumer behavior than outcome-related reasoning. This would
16

also be in line with research showing that negative reciprocity is both more common and
more intense than positive reciprocity, at least in one-shot settings (Baumeister et al. 2001;
Offerman 2002; Al-Ubaydli and Lee 2009).
An alternative explanation is that the top-down approach by which sellers impose
differential pricing reduces both the moral responsibility and agency of consumers in
causing more equal outcomes. Because in our setup the “future market” is unaffected
by consumer decisions, and consumers do not decide whether low-income consumers
receive discounts, they might exhibit patterns that are different from e.g. voting for re-
distributive policies. In the economics literature, this has been referred to as responsibility-
alleviation (Charness 2000). Put another way, decoupling high-income consumer choices
from low-income consumer outcomes isolates for warm-glow-altruism. Altruists who care
about the outcome of the “public good” have no reason to switch toward the BPD-store,
or incur the personal costs of staying in a store that advantages others. To test these
explanations, Study 4 extends our design by a second period that simulates consumer
agency through a market environment.
4. Study 4: Altruism
We examine whether consumer aversions towards BPD generalize to a market-analogous
situation where consumers’ purchasing decisions affect a store’s future pricing strategy.
By endowing current consumers with agency over the price-setting process for a later
period, we induce externalities on their purchasing decisions and thus agency regarding
future consumer outcomes. Consumers are responsible for future overall welfare as well
as the potential equalization of outcomes induced by BPD. In so far as our subjects exhibit
altruistic preferences, we would expect less switching in the Avoid paradigm and more
switching in Approach. Those who still switch away from the price discriminating store
essentially pay to decrease seller and future low-income consumer profits as well as to
prevent a more equal outcome distribution.
Experimental Design
We implemented two (Avoid vs. Approach) 2x2 mixed factorial designs manipulating the
source of income inequality (Random vs. Effort) as well as the agency of consumers regard-
ing the price-discriminating store’s pricing strategy in a future task ( Agency vs. No agency).
The No Agency treatments are equivalent to the corresponding Avoid conditions in Study
3. For the agency treatments, we add one screen after the store’s introduction of price
discrimination. On this screen, subjects are informed that the discriminating store’s sales
in the remaining two rounds will determine its price-setting in a future HIT on MTurk.
If sales exceeded a certain threshold, a rule would automatically implement the lower
17

0 10 20 30 40 50 60 70 80 90
NoAgency, Random
Agency, Random
NoAgency, Eﬀort
Agency, Eﬀort
0 100%
15.44
17.93
10.88
14.48
28.86
22.76
31.29
31.72
55.7
59.31
57.82
53.79
Self-interested anti-pd Other behavioral patterns
FIGURE 3. Behavioral patterns across the four conditions from Study 4, Avoid
prices for new low-income consumers in the last two rounds of a future setup-equivalent
task. Otherwise, future low-income consumers would face the uniform price, and thus be
unable to purchase the good at all. We thereby foreclose any considerations regarding
differing manager income levels or reverse outcome inequalities in the future task. 9
Results Avoid
Manipulation Check. To affirm that subjects understand our manipulation, we asked
them to choose the correct statement about the future impact of their purchase decisions
out of four options. In total, 76 % of subjects answered the questions correctly. Since there
could be multiple reasons why participants might answer the question incorrectly, we do
not drop observations based on the manipulation check. Instead, we will use the results
from the sub-sample of subjects who correctly answered the question as a robustness
check.
Switching Behavior .In line with Study 3, 58 % (56 %) of subjects in the No Agency treat-
ments of Effort (Random) decide to stay in the same store for the whole experiment.
Similarly, 31 % and 29 % respectively exhibit strictly anti price-discrimination behavioral
patterns by switching after the introduction of discounted prices. Endowing subjects
with agency regarding future consumer welfare does not appear to fundamentally shift
behavior (see Figure 3).
In Agency-Effort, 32 % are categorized as anti-pd. In Random, that share drops to 23 %.
Contrary to the No Agency treatments, we document a difference in the drop of sales
conditional on the source of endowment differences. InRandom, the store introducing BPD
experiences a smaller decline in demand ( Effort: -0.72, Random: -0.54; t =−1.56, p= 0.06),
9Specifying that low-income consumers would receive the discount only for two rounds ensures that it is
impossible for them to earn more money in total than regular consumers.
18

0 10 20 30 40 50 60 70 80 90
NoAgency, Random
Agency, Random
NoAgency, Eﬀort
Agency, Eﬀort
0 100%
19.18
12.33
14.19
18.12
5.48
11.64
4.73
10.07
75.34
76.03
81.08
71.81
Self-interested pro-pd Other behavioral patterns
FIGURE 4. Behavioral patterns across the four conditions from Study 4, Approach
which is accentuated when restricting the sample to subjects who correctly answered the
control question (t =−1.89 ,p= 0.03). The regression model replicates this effect across the
whole sample through a significant interaction between the Effort-Indicator and the BPD-
Indicator. Hence, there is moderate evidence that under agency, the source of endowment
differences becomes more meaningful and consumers who randomly receive a higher
income tend to switch less. However, differences are small and only marginally significant,
depending on the sample. The overall behavioral patterns remain largely unchanged.
Results Approach
The No Agency treatments closely replicate our results from Study 3 (see Figure 4). The
majority of consumers maximizes their income by staying in the same store for all four
rounds and the price-discriminating store sells roughly the same amount before and
after the introduction of discounts for low-income consumers ( Effort: t = 0.29 ,p= 0.769;
Random: t = 0.27 ,p= 0.787).
Once consumers are endowed with some agency regarding future store prices, their
purchasing behavior changes significantly. The share of subjects classified as pro-pd
roughly doubles with 10 % in Effort-Agency and 12 % in Random-Agency. In Effort-Agency,
the price discriminating store sells 0.09 goods on average over the first two rounds, and
0.30 goods over rounds three and four – a significant increase ( t = 3.89 ,p < 0.001). The
results for Random-Agency are similar (0.08 vs. 0.32; t = 4.04, p < 0.001) and there are
no significant treatment differences between the two ( t = 0.25, p = 0.802). The seller
introducing BPD after the second round sells significantly more in Effort-Agency than in
Effort-No Agency (t = −2.94, p = 0.013) and more in Random-Agency than in Random-No
Agency (t = −2.21, p = 0.028). Concurrently, the regression model reveals a significant
19

interaction between BPD and the Agency treatment dummy on store choice. The source of
endowment does not predict switching.
Discussion
The results show that a salient market mechanism, which endows consumers with agency
over future prices for low-income consumers, more than doubles costly support of BPD,
while aversions persist. This is consistent with altruistic preferences influencing switching
towards the price discriminating store. Given that consumers are uncertain about the
importance of their purchase in determining future prices – as is the case for many real-
life market contexts –, the effect is surprisingly large. On the other hand, high-income
subjects confronted with relatively disadvantageous price discounts appear unfazed by
the detrimental effects of their choices on inequality and economic welfare. This suggests
that a consumer’s role in the pricing environment mediates the influence of altruism
on sellers’ behavioral constraints. Those who can express altruism through voluntary,
costly action are more amenable to support benevolent price discounts, whereas those
deciding between inaction and disapproval largely disregard the outcome of low-income
consumers.
5. Study 5: Switching Costs and Warm Glow
People often derive utility from “giving” to others, irrespective of the generated output.
These warm glow effects are one main explanation why government transfers often only
imperfectly crowd-out private contributions to public goods or charitable organizations.
We argue that supporting benevolent price discrimination by giving up part of one’s in-
come is a manifestation of warm glow. Sellers depend on the reactions of other consumers
when implementing price discounts for people with lower income. However, changing
one’s purchasing habits can be costly. For example, consumers might have to break certain
routines, sustain longer distances, learn about and try new brands and products, create
new accounts, or incur additional search costs. Depending on the consumer’s preferences
as well as different market factors like the purchase environment (analog vs. digital),
competition or the availability of substitutes, these costs will differ substantially in the
real world. For consumer constraints, such higher expenses should have either no, or a
negative effect on switching – depending on the severity of aversions (see utility function
6). For consumers with the option to support BPD, however, this might change. That is
because, in addition to the negative effect of losing money, consumers can “feel good”
about themselves and their decision to give up, i.e. donate, money in order to assist the
seller introducing price discounts that allow low-income consumers to access the market
(see utility function 5). Consequently, the higher the switching costs, the better they may
20

feel about their good deed. To test this theory, Study 5 varies switching costs for both
Approach and Avoid. Following warm glow, we expect higher switching costs in Approach
to correlate with stronger support for BPD. For Avoid, varying switching costs serves as a
robustness check. Finally, we also provide a quick overview of two additional robustness
checks that (1) vary the willingness to pay of low-income consumers and (2) use qualitative
data to confirm the validity of our behavioral interpretations.
Experimental Design
Since consumers in the prior Approach studies did not condition their behavior on the
origin of endowment differences, we choose to allocate incomes randomly. Furthermore,
consumers have agency over future prices. We implement three treatments with switching
costs of either 5, 15 or 30 Coins.
Results
Figure 5 (right side) shows consumer “pro-pd” patterns for the three switching costs
treatments. Compared to 5 Coins (10.7%), the share of subjects classified as pro-pd in-
crease under 15 (16.9%) and 30 (16.3%) Coins. BPD-stores in both conditions experience
a significantly larger jump in sold goods after introducing price discounts ( 15: 0.21 vs.
0.43,t = 2.33, p = 0.02; 30: 0.21 vs. 0.38, t = 1.82, p = 0.07), which is further supported by
significant interaction effects in the panel regression (see Table A2).
5 15 30
0
0.1
0.2
0.3
0.4
0.5
Switching Costs
Share anti-pd/pro-pd
Avoid
5 15 30
0
0.1
0.2
0.3
0.4
0.5
Switching Costs
Approach
FIGURE 5. Share of “anti-pd” and “pro-pd” subjects for different switching costs
in Avoid and Approach.
Like before, the majority of subjects follow a self-interested strategy and never switch
stores (72%/68%/70%) for switching costs of 5/15/30. Restricting the sample to participants
who answered the control question correctly (76%) does not change anything. Overall,
21

these results support our conjunction that warm glow motivates costly support of BPD.
While there are no differences between 15 and 30 Coins, switching towards the store with
price discounts increases significantly compared to the baseline. Since costs “c” cause
both positive and negative utility, it is not surprising that the effect levels off for larger
amounts.
5b: Switching Costs Avoid
To assess the influence of switching costs on consumer aversions, we opt for the Avoid
paradigm where subjects earn their endowment through the effort task and have agency
over the store’s future prices.
Results
Results reveal moderate evidence for downward elasticity of consumer BPD aversions
(see Figure 5 and Table A1). For switching costs of 5 Coins, the drop in average goods sold
after the introduction of price discounts was significantly higher than for switching costs
of 15 (−0.91 vs.−0.70; t =−1.71, p= 0.045) and qualitatively higher than for switching costs
of 30 Coins (−0.91 vs.−0.74;t =−1.40, p= 0.082). There was no difference between 15 and
30 Coins (t = 0.30, p= 0.619).10 Finally, the regression analysis reveals no significant treat-
ment dummy (Table A1), confirming that consumer aversions towards BPD are relatively
inelastic to changes in switching costs.
Robustness Checks: Low-Income Consumer WTP and Consumer Reasoning
We ensure the validity of our findings with two additional robustness checks that are
detailed in the online appendix. 11 First, qualitative data from a post-experimental open-
ended question in studies 2, 4 and 5 confirms (1) the validity of our behavioral labels and
(2) high data quality. Consumer subjects consistently refer to unfair price discounts as
their reason for switching away from the price-discriminating store, while transaction
costs discipline many other consumers to act in their monetary self-interest. Second, we
conduct a sixth large study (see Table 2) that varies low-income consumers’ willingness
to pay (wlc ∈ {70, 100, 130}) such that high-income either experience (1) disadvantageous
purchase-level inequity, (2) no purchase-level inequity or (3) advantageous purchase-
level inequity. The data confirms the robustness of both Avoid and Approach towards
relatively lower product valuations from low-income consumers, and thereby controls for
high-income consumer disadvantageous inequity aversions as a behavioral explanation.
10Restricting the sample to subjects who correctly answered the control question about consumer purchases
affecting store prices in a future HIT (75 %) amplifies these results for switching costs of 15 (5: −0.82 vs. 15:
−0.51; t = −2.30, p= 0.011), but not for switching costs of 30 (5: −0.82 vs. 30: −0.65; t = −1.23, p= 0.110).
11https://osf.io/sztnh/?view_only=fc170dcbfeda431e994b23ed095d8b4b
22

6. General Discussion
This paper is the first to analyze consumer reactions towards benevolent price discounts
that favor low-income consumers who otherwise cannot participate in the market. We
show that a large share of consumers is willing to costly switch away from the price-
discriminating store, despite experiencing no price increases themselves. Qualitative
data confirms that this behavior is mainly driven by feeling unfairly passed over after the
introduction of discounts. Simply observing that other people pay less for the same good is
enough to motivate large consumer movements. In contrast to previous theories about the
existence of price discounts, there is no evidence that inequity attitudes can adequately
explain or mitigate consumer reactions. Even when consumers know that everybody is
priced according to the same rule, and that differences in endowment are purely due to
random chance, the main results hold. Furthermore, allowing for altruism by tying current
purchasing choices to future prices does not meaningfully change consumer aversions.
Our results therefore suggest that distributive fairness concerns do not play an important
role in determining consumer fairness perceptions of relatively disadvantageous prices.
This interesting results partially contrasts well-established findings from other economic
contexts such as bargaining or redistribution through e.g. taxation (Alesina and Angeletos
2005; Alesina and Giuliano 2011; Camerer 2011; Engelmann and Strobel 2004; Dimick,
Rueda, and Stegmueller 2016; Klor and Shayo 2010).
Second, we find that costly support for benevolent price discounts can be partially
explained by consumers being impure altruists (Andreoni 1990). As hypothesized, costly
switching towards a seller who introduces price discounts for excluded low-income con-
sumers is behaviorally similar to the private provision of a public good, such as charitable
giving (Ottoni-Wilhelm, Vesterlund, and Xie 2017). Without any information about price
discrimination, or when purchases have no future consequences, almost no consumer
is willing to costly switch away from their current store. However, once we allow for
altruism, support more than doubles. What is more, increasing the costs of switching
further increases costly support of the price discriminating seller, providing evidence
for warm glow effects. Like before, inequity attitudes do not appear to have meaningful
explanatory power.
Overall, consumer aversions consistently exceed consumer support, and the seller
introducing price discounts loses a sizeable share of high-income consumers. While the
most prominent purchasing strategy is always a monetary self-interested one, qualitative
and experimental data suggests that the existence of transaction costs prohibits many
averse consumers from switching. Thus, the easier it is for consumers to find another
seller, the higher the risk of potentially losing a disproportionate number of current
consumers.
23

Implications
The results highlight the importance of clearly distinguishing between different types of
consumers. For a firm, there are marked differences between attracting novel customers
who need to make an affirmative decision towards the seller, and not alienating or keeping
current customers who, at best, express their contentment by foregoing a switching choice.
The latter do not appear to judge top-down price discounts as a desirable public good, and
therefore also do not exhibit sensitivity to relevant pro-social peer preferences. This is
even true in situations where discounts are explicitly and exclusively targeted at people
who, through sheer luck, are not able to participate in the market at all, suggesting very
strong initial aversions towards price discrimination. Hence, while some researchers
have suggested overt transparency as a firm’s strategy to signal benevolence if price
discrimination is based on consumer income (Rotemberg 2011), our results indicate that
this is, by and large, not necessarily a good strategy for sellers. Rather, and similar to
situations where consumers react to disadvantageous price discrimination (e.g. Allender
et al. 2021; Leibbrandt 2020), firms should generally expect a substantial drop in demand
by current customers. Examples such as student discounts or the SNAP program are are
outliers, and can probably not be explained by consumer inequity aversion or altruism.
Our results are also in line with Li and Jain (2016), whereby firms that are expecting
consumer fairness concerns reduce differential pricing, e.g., low poaching prices. This
reduces inefficient switching and consumer dis-utility from perceived price unfairness,
but hurts overall consumer surplus. Consumer reactions constrain price setting that
increases market participation, consumer welfare, joint welfare, and equity. One particular
implication is that seller monitoring through price transparency regulations and consumer
agency does not necessarily imply utilitarian improvements. In fact, it may even have the
opposite effect, by preventing many consumers from receiving better deals.
Finally, there are reasons to believe that price discrimination can function as a re-
distributive mechanism that increases market participation for low-income consumers
while also increasing joint welfare. Consumers do exhibit impurely altruistic preferences
when differential pricing is not a top-down decision by their current seller. Leveraging
these social preferences may reveal hitherto under-explored mechanisms to attract new
customers and simultaneously improve consumer surplus, e.g., through marketing, CSR
communication or establishing a direct relationship between customer purchases and
targeted price discounts. These instruments, however, will often require the utilization
of either targeted information or obfuscation, in order to circumvent the behavioral
constraints exerted by a seller’s current customer base.
24

References
Al-Ubaydli, Omar, and Min Sok Lee. 2009 . “ An experimental study of asymmetric reci-
procity. ”Journal of Economic Behavior & Organization 72 (2): 738–749 .
Alesina, Alberto, and George-Marios Angeletos. 2005. “Fairness and Redistribution. ”Amer-
ican Economic Review 95 (4): 960–980.
Alesina, Alberto, and Paola Giuliano. 2011. “Preferences for redistribution. ” InHandbook
of social economics, vol. 1, 93–131: Elsevier.
Allender, William J, Jura Liaukonyte, Sherif Nasser, and Timothy J Richards. 2021. “Price
fairness and strategic obfuscation. ”Marketing Science 40 (1): 122–146.
Anderson, Eric T, and Duncan I Simester. 2008. “Research note—does demand fall when
customers perceive that prices are unfair? The case of premium pricing for large sizes. ”
Marketing Science 27 (3): 492–500.
Andreoni, James. 1990. “Impure altruism and donations to public goods: A theory of
warm-glow giving. ”The economic journal 100 (401): 464–477 .
Andreoni, James. 1995. “Cooperation in public-goods experiments: kindness or confusion?”
The American Economic Review: 891–904.
Aryal, Gaurab, Charles Murry, and Jonathan W Williams. 2023. “Price Discrimination in
International Airline Markets. ”The Review of Economic Studies.
Baumeister, Roy F, Ellen Bratslavsky, Catrin Finkenauer, and Kathleen D Vohs. 2001. “Bad
is stronger than good. ”Review of general psychology 5 (4): 323–370.
Blount, Sally. 1995. “When social outcomes aren’ t fair: The effect of causal attributions on
preferences. ”Organizational behavior and human decision processes 63 (2): 131–144.
Bolton, Gary E, and Axel Ockenfels. 2000. “ERC: A theory of equity, reciprocity, and com-
petition. ”American economic review 90 (1): 166–193.
Bolton, Lisa E., Hean Tat Keh, and Joseph W . Alba. 2010. “How Do Price Fairness Percep-
tions Differ across Culture?” Journal of Marketing Research 47 (3): 564–576.
Calvano, Emilio, Giacomo Calzolari, Vincenzo Denicolo, and Sergio Pastorello. 2020. “ Arti-
ficial intelligence, algorithmic pricing, and collusion. ”American Economic Review 110
(10): 3267–97 .
Camerer, Colin F. 2011. Behavioral game theory: Experiments in strategic interaction.: Prince-
ton University Press.
Campbell, Margaret C. 1999 . “Perceptions of Price Unfairness: Antecedents and Conse-
quences. ”Journal of Marketing Research 36 (2): 187–199 .
Charness, Gary. 2000. “Responsibility and effort in an experimental labor market. ”Journal
of Economic Behavior & Organization 42 (3): 375–384.
Charness, Gary, and Ernan Haruvy. 2002. “ Altruism, equity, and reciprocity in a gift-
exchange experiment: an encompassing approach. ”Games and Economic Behavior 40
(2): 203–231.
25

Chen, Daniel L., Martin Schonger, and Chris Wickens. 2016. “oTree—An open-source
platform for laboratory, online, and field experiments. ”Journal of Behavioral and Ex-
perimental Finance 9: 88–97 .
Coase, Ronald H. 1972. “Durability and monopoly. ”The Journal of Law and Economics 15 (1):
143–149 .
Cox, James C. 2004. “How to identify trust and reciprocity. ”Games and economic behavior
46 (2): 260–281.
Della Vigna, Stefano, and Matthew Gentzkow. 2019 . “Uniform pricing in us retail chains. ”
The Quarterly Journal of Economics 134 (4): 2011–2084.
Dimick, Matthew, David Rueda, and Daniel Stegmueller. 2016. “The altruistic rich? Inequal-
ity and other-regarding preferences for redistribution. ”Quarterly Journal of Political
Science 11 (4): 385–439 .
Dubé, Jean-Pierre, and Sanjog Misra. 2023. “Personalized pricing and consumer welfare. ”
Journal of Political Economy 131 (1): 131–189 .
Durante, Ruben, Louis Putterman, and Joël van der Weele. 2014. “Preferences for Redistri-
bution and Perception of Fairness: An Experimental Study. ”Journal of the European
Economic Association 12 (4): 1059–1086.
Engelmann, Dirk, and Martin Strobel. 2004. “Inequality aversion, efficiency, and maximin
preferences in simple distribution experiments. ” American economic review 94 (4):
857–869 .
Fabiani, Silvia, Martine Druant, Ignacio Hernando, Claudia Kwapil, Bettina Landau, Claire
Loupias, Fernando Martins, Thomas Mathä, Roberto Sabbatini, Harald Stahl et al.
2006. “What Firms’ Surveys Tell Us about Price-Setting Behavior in the Euro Area. ”
International Journal of Central Banking.
Falk, Armin, Ernst Fehr, and Urs Fischbacher. 2008. “Testing theories of fairness—
Intentions matter. ”Games and Economic Behavior 62 (1): 287–303.
Fehr, E., and K. M. Schmidt. 1999 . “ A Theory of Fairness, Competition, and Cooperation. ”
The Quarterly Journal of Economics 114 (3): 817–868.
Fehr, Ernst, Georg Kirchsteiger, and Arno Riedl. 1993. “Does fairness prevent market
clearing? An experimental investigation. ” The quarterly journal of economics 108 (2):
437–459 .
Ferguson, Jodie L., Pam Scholder Ellen, and William O. Bearden. 2014. “Procedural and
Distributive Fairness: Determinants of Overall Price Fairness. ”Journal of Business Ethics
121 (2): 217–231.
Fudenberg, Drew, and J. Miguel Villas-Boas. 2012. “Price discrimination in the digital
economy.. ”The Oxford handbook of the digital economy : 254.
Gibbons, Frederick X., and Bram P . Buunk. 1999 . “Individual differences in social compar-
ison: Development of a scale of social comparison orientation.. ” Journal of Personality
26

and Social Psychology 76 (1): 129–142.
Gill, David, and Victoria Prowse. 2012. “ A Structural Analysis of Disappointment Aversion
in a Real Effort Competition. ”American Economic Review 102 (1): 469–503.
Goeree, Jacob K, Charles A Holt, and Susan K Laury. 2002. “Private costs and public benefits:
unraveling the effects of altruism and noisy behavior. ”Journal of public Economics 83
(2): 255–276.
Harrington Jr, Joseph E, Roberto Hernan Gonzalez, and Praveen Kujal. 2016. “The relative
efficacy of price announcements and express communication for collusion: Experi-
mental findings. ”Journal of Economic Behavior & Organization 128: 251–264.
Haws, Kelly L., and William O. Bearden. 2006. “Dynamic Pricing and Consumer Fairness
Perceptions. ”Journal of Consumer Research 33 (3): 304–311.
Heider, Fritz. 1982. The psychology of interpersonal relations.: Psychology Press.
Ho, Teck-Hua, and Xuanming Su. 2009 . “Peer-Induced Fairness in Games. ” American
Economic Review 99 (5): 2022–2049 .
Ho, Teck-Hua, Xuanming Su, and Yaozhong Wu. 2014. “Distributional and Peer-Induced
Fairness in Supply Chain Contract Design. ”Production and Operations Management 23
(2): 161–175.
Janiszewski, Chris, and Donald R Lichtenstein. 1999 . “ A range theory account of price
perception. ”Journal of Consumer Research 25 (4): 353–368.
Jin, Liyin, Yanqun He, and Ying Zhang. 2014. “How Power States Influence Consumers’
Perceptions of Price Unfairness. ”Journal of Consumer Research 40 (5): 818–833.
Kahneman, Daniel, Jack L Knetsch, and Richard Thaler. 1986. “Fairness as a constraint on
profit seeking: Entitlements in the market. ”The American economic review: 728–741.
Klor, Esteban F, and Moses Shayo. 2010. “Social identity and preferences over redistribu-
tion. ”Journal of Public Economics 94 (3-4): 269–278.
Korenok, Oleg, Edward L Millner, and Laura Razzolini. 2013. “Impure altruism in dictators’
giving. ”Journal of Public Economics 97: 1–8.
Leibbrandt, Andreas. 2020. “Behavioral constraints on price discrimination: Experimental
evidence on pricing and customer antagonism. ”European Economic Review 121: 103303.
Li, Krista J, and Sanjay Jain. 2016. “Behavior-based pricing: An analysis of the impact of
peer-induced fairness. ”Management Science 62 (9): 2705–2721.
Luccasen, Andrew, and Philip J Grossman. 2017 . “Warm-glow giving: Earned money and
the option to take. ”Economic Inquiry 55 (2): 996–1006.
Maxwell, Sarah. 2007 .The price is wrong: Understanding what makes a price seem fair and the
true cost of unfair pricing .: John Wiley & Sons.
Musolff, Leon. 2022. “ Algorithmic Pricing Facilitates Tacit Collusion: Evidence from E-
Commerce. ” InProceedings of the 23rd ACM Conference on Economics and Computation,:
32–33.
27

Offerman, Theo. 2002. “Hurting hurts more than helping helps. ”European Economic Review
46 (8): 1423–1437 .
Ottoni-Wilhelm, Mark, Lise Vesterlund, and Huan Xie. 2017 . “Why do people give? Testing
pure and impure altruism. ”American Economic Review 107 (11): 3617–33.
Palfrey, Thomas R, and Jeffrey E Prisbrey. 1997 . “ Anomalous behavior in public goods
experiments: How much and why?” The American Economic Review: 829–846.
Ribar, David C, and Mark O Wilhelm. 2002. “ Altruistic and joy-of-giving motivations in
charitable behavior. ”Journal of political Economy 110 (2): 425–457 .
Rotemberg, Julio J. 2011. “Fair Pricing. ”Journal of the European Economic Association 9 (5):
952–981.
Rutström, E.Elisabet, and Melonie B Williams. 2000. “Entitlements and fairness: an exper-
imental study of distributive preferences. ”Journal of Economic Behavior & Organization
43 (1): 75–89 .
Shor, Mikhael, and Richard L Oliver. 2006. “Price discrimination through online couponing:
Impact on likelihood of purchase and profitability. ”Journal of Economic Psychology 27
(3): 423–440.
Thaler, Richard. 1985. “Mental accounting and consumer choice. ”Marketing science 4 (3):
199–214.
Williams, Kevin R. 2022. “The welfare effects of dynamic pricing: Evidence from airline
markets. ”Econometrica 90 (2): 831–858.
Wu, Chi-Cheng, Yi-Fen Liu, Ying-Ju Chen, and Chih-Jen Wang. 2012. “Consumer responses
to price discrimination: Discriminating bases, inequality status, and information
disclosure timing influences. ”Journal of Business Research 65 (1): 106–116.
Xia, Lan, Kent B. Monroe, and Jennifer L. Cox. 2004. “The Price is Unfair! A Conceptual
Framework of Price Fairness Perceptions. ”Journal of Marketing 68 (4): 1–15.
28

TABLE A1. Panel logistic regression using random effects for Avoid
Study 1 Study 2 Study 3 Study 4a Study 5b
Coef.
(se)
Coef.
(se)
Coef.
(se)
Coef.
(se)
Coef.
(se)
PD -5.353*** -3.935*** -4.700*** -3.994*** -5.273***
(1.206) (0.459) (0.806) (0.587) (0.726)
PD× Intention -1.543**
(0.617)
PD× Effort 0.507 -1.300*
(0.852) (0.754)
PD× Agency 0.380
(0.739)
PD× Effort× Agency 0.351
(1.075)
PD× 15 Coins 0.598
(0.849)
PD× 30 Coins 0.732
(0.812)
Intention 0.969*
(0.520)
Effort -0.412 1.119
(0.731) (0.683)
Agency 0.270
(0.646)
Effort× Agency -1.050
(0.951)
15 Coins 0.504
(0.731)
30 Coins 0.096
(0.683)
SCO 0.513* -0.237 -0.086 -0.375*** -0.117
(0.304) (0.172) (0.199) (0.144) (0.165)
Constant 3.383** 5.582*** 5.647*** 6.907*** 5.758***
(1.584) (0.965) (1.263) (0.958) (0.992)
N 384 1564 788 2344 1468
AIC 292.194 1267 .133 634.181 1734.051 1129 .807
BIC 307 .996 1299 .263 662.198 1791.647 1172.140
Table reports results of panel logistic regressions using random effects and a cluster–robust VCE estimator.
Dependent variable is a dummy variable that equals 1 if participant bought a good in the price discriminating
store, 0 otherwise. Independent variables: "PD" equals 1 in Round 2 and 3, 0 otherwise; Intention, Effort,
Agency, 15 ECU and 30 ECU are dummy variables for the experimental conditions; Reference groups are
omitted from the table; "SCO" is mean of Social comparison orientation scale by Gibbons and Buunk (1999). —
* p< 0.1, ** p< 0.05, *** p< 0.01.
29

TABLE A2. Panel logistic regression using random effects for Approach
Study 1 Study 3 Study 4b Study 5a
Coef.
(se)
Coef.
(se)
Coef.
(se)
Coef.
(se)
PD 0.636 0.409 0.120 1.667***
(0.666) (0.586) (0.437) (0.476)
PD× Effort 0.184 0.026
(0.774) (0.654)
PD× Agency 1.923***
(0.650)
PD× Effort× Agency -0.258
(0.913)
PD× 15 Coins 1.694**
(0.665)
PD× 30 Coins 1.500**
(0.726)
Effort -0.012 -0.384
(0.568) (0.448)
Agency -0.992**
(0.503)
Effort× Agency 0.527
(0.709)
15 Coins
(0.590)
30 Coins -0.955
(0.637)
SCO -0.308 -0.076 -0.064 -0.093
(0.239) (0.193) (0.121) (0.133)
Constant -2.731** -3.709*** -3.420*** -4.399***
(1.229) (1.037) (0.675) (0.721)
N 388 800 2356 1776
AIC 153.150 381.708 1246.513 1132.023
BIC 168.994 409 .816 1304.160 1175.880
Table reports results of panel logistic regressions using random effects and a cluster–robust VCE estimator.
Dependent variable is a dummy variable that equals 1 if participant bought a good in the price discriminating
store, 0 otherwise — Independent variables: “PD” equals 1 in Round 2 and 3, 0 otherwise; Effort and Agency
are dummy variables for the experimental conditions; Reference groups are omitted from the table; “SCO” is
mean of Social comparison orientation scale by Gibbons and Buunk (1999) — * p< 0.1, ** p< 0.05, *** p< 0.01.
30
