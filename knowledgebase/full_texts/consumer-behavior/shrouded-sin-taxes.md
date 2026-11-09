---
title: Shrouded Sin Taxes
url: https://arxiv.org/abs/2409.01493
category: consumer-behavior
subcategory: empirical
date: 2024-09
venue: ''
authors:
- Johannes Kasinger
source: arxiv
pdf_url: https://arxiv.org/pdf/2409.01493
pages: 61
chars: 167514
fetched_at: '2026-11-08T13:14:27+00:00'
kb_version: 1
---

# Shrouded Sin Taxes

Shrouded sin taxes∗
Johannes Kasinger†
November 2023
Latest version available here.
Abstract
Strategic shrouding of taxes by profit-maximizing firms can impair the effectiveness of cor-
rective taxes. This paper explores tax shrouding and its consequences after the introduction
of a digital sin tax designed to discourage harmful overconsumption of online sports bet-
ting in Germany. In response to the tax reform, most firms strategically shroud the tax,
i.e., exclude tax surcharges from posted prices. Using an extensive novel panel data set on
online betting odds, I causally estimate the effect of the tax on consumer betting prices.
Consumers bear, on average, 76% of the tax burden. There is considerable and long-lasting
heterogeneity in effects conditional on shrouding practices. Firms that shroud taxes can pass
90% of the tax onto consumers, while the pass-through rate is 16% for firms that directly
post tax-inclusive prices. To understand the results’ underlying mechanisms and policy im-
plications, I propose an optimal corrective taxation model where oligopolistic firms compete
on base prices and can shroud additive taxes. Tax shrouding is only attainable in equilib-
rium if (some) consumers underreact to shrouded attributes. According to the theoretical
predictions, the empirically identified heterogeneity suggests that strategic tax shrouding
significantly attenuates the positive corrective welfare effects of the tax. The results prompt
regulating shrouding practices in the context of corrective taxation.
JEL Classification: H22, H23, D43, D83, Z28
Keywords: shrouded attributes, optimal taxation, tax salience, digital taxes, partitioned
pricing, online gambling, sin taxes.
∗I am grateful for helpful comments and useful suggestions from Youssef Benzarti, Andreas Born, Fabrizio
Colella, Markus Dertwinkel-Kalt, Markus Eyting, Gyozo Gy¨ ongy¨ osi, Simon Heß, Aljoscha Janssen, Christine
Laudenbach, Alexander Ludwig, Vincenzo Pezone, James Reade, Emmanuel Saez, Patrick Schmidt, Lorenzo
Sch¨ onleber, Johannes Spinnewijn, Tomasz Sulko, Dmitry Taubinsky, Alfons Weichenrieder and seminar partici-
pants at the Goethe University Frankfurt, University of Reading, Leibniz Institute for Financial Research SAFE,
and the WHU Young Scholar Tax Conference. Financial support from the Leibniz Institute of Financial research
SAFE is gratefully acknowledged.
†Tilburg School of Economics & Management, Tilburg University & Leibniz Institute for Financial Research
SAFE, j.kasinger@tilburguniversity.edu
arXiv:2409.01493v1  [econ.GN]  2 Sep 2024

1 Introduction
Consumers often underreact to shrouded (i.e., non-salient or hidden) attributes of goods (DellaV-
igna, 2009). There are numerous examples where firms strategically shroud relevant price at-
tributes to exploit these underreactions. 1 When firms can choose how to present and collect
taxes, they may optimally shroud those taxes, e.g., by actively excluding tax surcharges from
posted prices as frequently observed in the aviation sector (Bradley and Feldman, 2020). Tax
shrouding decreases the salience of taxes, which attenuates the behavioral responses to those
taxes and thus influences their welfare effects (Chetty et al., 2009; Taubinsky and Rees-Jones,
2018). Various theoretical studies on add-on pricing and strategic price complexity (e.g. Gabaix
and Laibson, 2006; Carlin, 2009) further suggest that responses to shrouded attributes and equi-
librium outcomes can substantially differ when salience is not a passive but an active decision by
firms, depending on consumers’ attention to shrouded price information (and the implied firms’
motives).2
Consequently, strategic tax shrouding and the underlying market structure have important
welfare implications. These implications are essential for corrective taxation because its ef-
fectiveness in discouraging the harmful overconsumption of certain goods directly depends on
(perceived) tax-induced price changes (Bernheim and Taubinsky, 2018). 3 Nevertheless, strate-
gic tax shrouding and its consequences are understudied. The literature typically assumes that
consumers optimize fully with respect to tax-inclusive prices, which rules out the relevance of
tax shrouding. The tax salience literature, in contrast, relaxes this assumption but almost ex-
clusively focuses on settings where tax salience is exogenous and independent of firms’ strategic
decisions.
This article fills this gap by examining the prevalence, effects, and welfare implications
of strategic tax shrouding by firms in the context of a corrective sin tax on (online) sports
betting. I document that tax shrouding is a widespread response by firms to the introduction
of the 2012 German sports betting tax. The tax imposes a 5% duty on betting turnovers
generated by German customers and has to be remitted by all betting agencies that serve
German customers, irrespective of their jurisdictional location. 4 By exploiting the induced
quasi-experimental variation and a novel extensive panel data set on online betting prices, I
estimate the pass-through rates of the tax onto consumers. The paper employs a difference-in-
differences (DID) framework, comparing the changes in average consumer betting prices in the
German market with changes outside the German market. Firms can pass around 76% of the tax
1Examples of such practices include add-on pricing (e.g., Ellison, 2005; Gabaix and Laibson, 2006), hidden
shipping and handling costs (e.g., Hossain and Morgan, 2006; Brown et al., 2010), strategic price complexity
(Carlin, 2009) and complicated or confusing product descriptions (e.g., Ellison and Ellison, 2009; Chioveanu and
Zhou, 2013).
2For instance, Bayesian consumers who infer that products with strategically shrouded add-on prices are likely
to be less attractive offers may or may not lead to unshrouding in equilibrium depending on the market structure
(Gabaix and Laibson, 2006).
3From a social welfare perspective, goods can be overconsumed if individuals do not fully account for the
negative effects of their consumption on others in society—externalities—or on their (future) selves—internalities
(Allcott et al., 2019b). Typical examples of such goods include environmentally harmful goods or sin goods, such
as cigarettes, alcohol, or gambling. Corrective taxes are a central policy tool to limit their negative effects on
social welfare.
4Note that the average expected net return of a (random) 1 e bet from a bookmaker’s perspective is around
7%, implying a considerable levy on firms’ profits.
1

onto consumers, i.e., tax-inclusive consumer prices increased on average by about 3.8 percentage
points after the tax reform. Estimated pass-through rates are heterogeneous depending on
firms’ shrouding practices, which is inconsistent with predictions of standard taxation models
(Kotlikoff and Summers, 1987; Weyl and Fabinger, 2013). Firms that actively exclude taxes
from posted prices can pass 90% of the tax onto consumers, while the pass-through rate is 16%
for firms that directly post tax-inclusive prices. 5
To better understand the underlying mechanisms and policy implications, I propose a stylized
sin tax model based on O’Donoghue and Rabin (2006) and Varian (1980) that allows for strategic
tax shrouding and heterogeneously attentive consumers. According to the model, the empirical
results imply that several consumers underreact to shrouded taxes. The positive corrective
effects of the sin tax are undermined by the strategic shrouding behavior of profit-maximizing
firms. In addition, the employed homogeneous linear sin tax can only effectively implement the
first-best outcome when attention to shrouded attributes is homogeneous across consumers. To
ensure the effectiveness of the sin tax, policymakers should require firms to post tax-inclusive
prices. While the study focuses on a sin tax, the policy implications also extend to the optimal
design of externality correction policies, more generally.
The German sports betting tax provides a suitable quasi-experimental setting to study the
effectiveness and strategic shrouding of sin taxes in a digital context. Importantly, the vast
majority of betting agencies that target the German market followed the tax rules despite
a missing jurisdiction in Germany. The tax effectively generated considerable tax revenues,
which also has important implications for the functioning of digital service taxes. 6 The primary
rationale behind German sports betting regulation and taxation is to prevent betting addiction
and problem gambling (German interstate gaming treaty §1). The tax rules do not restrict
how and whether to present or collect the tax. In contrast to most other countries that deduct
betting taxes from gross betting revenues, i.e., the total wagered amount minus all winnings
by bettors (Haucap, 2021), Germany bases the sports betting tax on betting turnover. This
peculiarity implies that the German tax is independent of a bet’s price, analogous to a classical
per unit sin tax (see section 2.2). Moreover, there was no other effective taxation of gambling
services before and after the reform, and the regulatory landscape in Germany for online sports
betting remained essentially unchanged between 2009 and 2018 besides the tax reform.
The data set combines web-scraped information on betting odds from 68 international betting
agencies for more than 80,000 sports events between 2009 and 2018 with information from various
other sources. The data set allows to infer implicit betting prices and identify heterogeneity in
tax effects conditional on strategic tax shrouding by firms. I focus on the pass-through of the
tax, which is a central measure to evaluate the policy’s corrective and welfare effects (Weyl and
Fabinger, 2013). The estimated average effective pass-through rate is stable over time and shows
a slightly increasing trend. The betting prices before the tax reform develop very similar within
and outside the German market. Treatment timing is homogeneous and plausibly exogenous to
5Note that the pass-through rates refer to the effective consumer prices, i.e., posted prices plus shrouded tax
surcharges. Accordingly, a pass-through rate of 90% for shrouding agencies implies a decrease in posted prices of
10%, given that the average applied shrouded tax surcharge is equal to the size of the tax.
6Using data from a commercial provider that also serves the betting agencies and official bodies, I find that
around 80% and 90% of online sports betting revenue are taxed. Until 2020, the German sports betting tax
generated revenues of more than 2.6bn Euro according to administrative tax data, making it a significant source
of tax revenue.
2

betting prices. Accordingly, the identifying DID assumptions hold and effects are not biased
because of heterogeneous treatment timing (Goodman-Bacon, 2021; Sun and Abraham, 2021;
Borusyak et al., 2022), allowing for a causal interpretation of the average effects. The empirical
results are robust to different specifications and more restrictive categorizations of the control
and treatment groups.
In response to the tax, the majority, but not all, betting agencies employ a shrouding policy
that drives a wedge between posted and effective tax-inclusive betting prices. Shrouding agencies
advertise tax-exclusive prices but deduct taxes after a specific bet is selected—similar to hidden
shipping surcharges. Non-shrouding agencies post tax-inclusive prices directly. The agencies
introduced shrouding policies on different dates. All agencies that established a shrouding policy
kept that policy until the end of the observation period.7 I estimate heterogeneous pass-through
rates by two approaches using a DID design: i) subsample analyses where I only consider a
subset of German agencies depending on the established shrouding policy; ii) a framework where
I interact “treatment” with a dummy variable that indicates whether a shrouding policy was
in place for a given event and bookmaker. While shrouding policies are endogenous decisions
by firms, average prices and trends before the tax reform were similar for shrouding and non-
shrouding agencies, suggesting that non-German agencies still provide a valid counterfactual for
the subsample analyses. The estimated difference in pass-through rates using approach ii) is
around 80%. This difference is slightly higher than for the subsample analyses as average effects
are not diluted by “not yet shrouded” events. 8 The heterogeneity persists until the end of the
observation period, even if the gap decreases over time. Furthermore, the difference persistence
of this difference implies that firms cannot profitably “debias” competitors’ consumers (Gabaix
and Laibson, 2006).
The theoretical model I am proposing has two extensions to the standard optimal sin tax
model. First, the sin good is not supplied under perfect competition but under imperfect
Bertrand-Nash price competition in the spirit of Varian (1980). Firms set salient base prices
and can shroud additive taxes that apply to the sin good. Second, consumers can perfectly ob-
serve the base prices but are heterogeneous regarding their attention toward the shrouded tax. 9
Suppose all consumers are fully attentive to the tax surcharge. In that case, equilibrium prices
are symmetric and equal to firms’ marginal costs, implying a full pass-through of taxes onto
consumers. The implications of classical corrective taxation models (Pigou, 1920; O’Donoghue
and Rabin, 2006) carry over to the extended model: (i) the sin good is overconsumed compared
to the welfare-optimal solution because consumers do not fully internalize costs on their (future)
selves when making their decision due to self-control problems or other behavioral mistakes; ii)
a corrective per-unit sin tax equal to the average mistake of the marginal consumer restores the
welfare-optimal solution. iii) in the case of a homogeneous underreaction to taxes (Chetty et al.,
2009; DellaVigna, 2009), the optimal tax rate increases and equals the average marginal mistake
7Two out of ten agencies targeting the German market did not shroud taxes over the entire observation period.
Six agencies started with tax shrouding within six months after the reform.
8This result is confirmed by the assessment of one of the main competitors in their 2012 annual report,
Bwin.party digital entertainment (2013): “Following the introduction of a 5% turnover tax on sports betting in
Germany on 1 July 2012, along with the rest of the industry, we began to pass on the majority of the tax to
customers by requiring that winning customers pay a 5% withholding on their pay-out”.
9To keep the model tractable, I assume a static model where consumers are either fully attentive or completely
inattentive to shrouded taxes and homogeneous otherwise.
3

divided by tax salience or attention parameter θ (Farhi and Gabaix, 2020). 10
If (some) consumers are inattentive to shrouded taxes, (some) firms will optimally exploit
this inattention and shroud taxes. Consumers overconsume the sin good in equilibrium, and sin
taxes are less effective (or even completely ineffective) in restoring the welfare-optimal solution.
If attention to shrouded taxes is heterogeneous, a linear corrective tax-transfer scheme that
applies equivalently to all consumers is ineffective in restoring the first-best welfare-optimal
solution. The second-best sin tax rate depends on the distribution of consumers’ attention
to shrouded surcharges. The government faces a tradeoff between “overcorrecting” attentive
consumers and “undercorrecting” the consumption of inattentive consumers. However, banning
tax shrouding practices is one simple and effective policy that restores the effectiveness of sin
taxes in implementing the welfare-optimal solution independent of the fraction of attentive
consumers.
In the case where self-control problems are negatively correlated with attention (e.g. due to
impulsive gambling behavior), the adverse welfare effects of tax shrouding are more pronounced
as the individuals that would benefit from the sin tax the most react to it the least. Similarly,
a correlation between attention and income can affect the regressivity of the tax and, thus,
its welfare implication depending on the correlation’s sign (on the welfare implications of the
regressivity of sin taxes see Gruber and K˝ oszegi, 2004; Goldin and Homonoff, 2013; Allcott et al.,
2019a).11
Following the theoretical implications, the observed pricing strategies and pass-through
rates in the empirical part of the paper are only sustainable if (some) consumers underreact
to shrouded tax surcharges. Consequently, the empirical results indicate that the average expe-
rienced increase in consumer prices is substantially higher than the perceived increase in prices.
This implies that strategic tax shrouding considerably decreases the positive corrective welfare
effect of the German sports betting tax. While these results are indicative of consumption adap-
tions by bettors, the betting revenue data is not granular enough to make a conclusive statement
about the effect on actual consumption. However, overall betting revenues in Germany strongly
increased and developed very similarly to other European countries before and after the tax re-
form, which suggests a limited corrective effect of the betting tax. Requiring agencies to directly
post tax-inclusive odds can help restore the corrective effect. Bradley and Feldman (2020) pro-
vide evidence of the effectiveness of such a policy in the context of US air carriers. They find, in
line with my empirical results and theoretical predictions, that introducing full-fare advertising
rules, which required airlines and travel agents in the US to advertise tax-inclusive prices on
their website, led to a decrease in consumers’ tax incidence and demand.
My study contributes to different strands of economic literature. First, numerous behavioral
public finance studies provide compelling evidence on the importance of behavioral frictions for
markets and optimal economic policy (e.g. Chetty et al., 2009; Finkelstein, 2009; Sallee, 2011;
10Note that as consumers are still homogeneous, Bertrand competition will push firms’ profits to zero. However,
the corrective effect of the tax decreases.
11The theoretical results imply that strategic shrouding behavior by firms undermines the effectiveness of
(positive) corrective taxation. However, in the case of subsidies, say, on environmentally-friendly products, the
motives of the government and firms align. It is optimal for firms to boost the subsidy salience to make their
offers more attractive—amplifying the effectiveness of subsidy-based externality correction policies. Consequently,
corrective subsidies may be preferable to taxes in settings where strategic shrouding by firms is significant for
consumers’ behavioral responses.
4

Goldin and Homonoff, 2013; Allcott and Taubinsky, 2015; Feldman and Ruffle, 2015; Taubinsky
and Rees-Jones, 2018; Benzarti et al., 2020; Farhi and Gabaix, 2020; Bradley and Feldman,
2020; Kroft et al., 2020). In their seminal paper on tax salience, Chetty et al. (2009) note that
the tax incidence on consumers is lower when “producers must actively “shroud” a tax levied
on them in order to reduce its salience”. Yet, theoretical and empirical evidence on this channel
is scarce. My study closes this gap in the context of a digital sin tax, bridging the behavioral
public finance literature to a rich literature in industrial organization that examines the effect
of shrouded attributes and strategic price obfuscation in different market settings (e.g. Ellison,
2005; Gabaix and Laibson, 2006; Hossain and Morgan, 2006; Carlin, 2009; Ellison and Ellison,
2009; Brown et al., 2010; Ellison and Wolitzky, 2012; Piccione and Spiegler, 2012; Kosfeld and
Sch¨ uwer, 2017; Heidhues et al., 2016).
Second, there is a growing literature in public finance, industrial organization and marketing
that examines the pass-through and the effects of taxes on various traditional (physical) sin
goods, such as sugar-sweetened beverages (Allcott et al., 2019a,b; Seiler et al., 2021; Keller
et al., 2023), alcohol (Kenkel, 2005; Hindriks and Serse, 2019), cigarettes (Barnett et al., 1995;
Gruber and K˝ oszegi, 2004; Harding et al., 2012), and marijuana (Hollenbeck and Uetake, 2021).
Some of these studies show full pass-through of these taxes, or even over-shifting—one possible
outcome in models with imperfect competition (Anderson et al., 2001; Weyl and Fabinger,
2013).12 My findings align with DeCicca et al. (2013), who find that consumer price search
affects the pass-through of cigarette excise taxes. I contribute to this literature by showing that
firms can affect “experienced” and “perceived” pass-through rates and the corrective effect of
sin taxes by strategic tax shrouding. Moreover, to the best of my knowledge, this is the first
study that examines the pass-through of sin taxes on online sports betting prices. Sin taxes on
sports betting can be expected to become increasingly policy-relevant in the near future, given
the recent legalization of sports betting in the US (US Supreme Court, 2017) and the persistent
unprecedentedly growth in global sports betting revenues (Montone, 2021).
Third, my study builds on and contributes to the literature on taxation and imperfect com-
petition (Stern, 1987; Delipalla and Keen, 1992; Anderson et al., 2001; Weyl and Fabinger, 2013).
In a recent paper, Kroft et al. (2020) extend the standard tax salience model to imperfect compe-
tition. They find that tax salience and market structure interact so that higher tax salience can
increase tax incidence under certain conditions. My study adds to their comprehensive analysis
and related studies (Bradley and Feldman, 2020) by relaxing the assumption of exogenous tax
salience in a price competition model inspired by Varian (1980) with an application to corrective
taxation.
The remainder of the paper is organized as follows. Section 2 gives more background on
the tax reform, online sports betting markets, and how shrouding affects the difference between
posted and effective prices. Sections 3 and 4 discuss the data and empirical strategy. Section 5
presents the empirical results. Section 6 lays out the theoretical model and discusses its policy
implications. Section 7 concludes.
12There is also a renewed interest among industrial economists in studying tax pass-through to learn more
about consumer preferences, market power, and competition in different markets (e.g. Miravete et al., 2018; Pless
and van Benthem, 2019; Miravete et al., 2020; Hollenbeck and Uetake, 2021).
5

2 Background
2.1 Institutional background
This section gives an overview of the relevant institutional details of the German sports betting
tax reform and regulations of the European and German online sports betting market. It further
presents some descriptive statistics on the development of online betting revenues in Europe to
put the study into perspective. Appendix A describes the underlying regulatory framework in
detail.
The German sports betting tax and online sports betting regulation
In July 2012, Germany extended the geographical scope of its sports betting tax code, effectively
introducing a new 5% tax on online sports betting turnovers generated by German bettors. 13
Betting agencies must remit the tax on aggregated monthly turnovers, irrespective of their
jurisdictional location and whether the provider operates lawfully in Germany. There is no
regulation on how or whether to display or collect the tax from consumers. According to§1 of the
German interstate Gaming treaty (“Gl¨ ucksspielstaatsvertrag”), the main goal behind regulating
and taxing online sports betting is to prevent problem gambling and betting addiction.
Before the reform, online sports betting generated virtually no tax revenue because the
preceding Sports Bet Tax only applied to bets that were ”organized” in Germany. According
to German tax law, the organizer of a bet is defined as the entity that fixes the odds and not
the entity that brokers a bet. Consequently, betting agencies, even if established or with some
physical presence in Germany, avoided taxation and the national sports betting ban by simply
operating from liberal foreign EU entities, mostly from Gibraltar and Malta (Englisch, 2013).
The tax reform in 2012 extended the geographical scope of the tax code to bettors, making the
Sports Bet Tax applicable if the bettor or the organizer of a bet is domiciled in Germany. 14
Accordingly, all online betting agencies that provide their services to German customers became
liable for the tax (Englisch, 2013). So, while the statutory tax rate actually decreased from
16.7% to 5%, the effective tax rate for online sports betting increased from zero to 5%. In this
study, we thus refer to a newly introduced sports betting tax.
Before and after the reform, betting services are exempted from the German V AT if they
are subject to the Sports Bet Tax (Englisch, 2013). The Sports Bet Tax does further take
precedence over federal and state duties. Moreover, international betting agencies are usually
not liable to business taxation as they operate from low-tax foreign entities, implying that the
turnover tax was and is the only effective taxation of online sports betting before and after the
reform. On the consumer side, there are no additional taxes in Germany, as gambling winnings,
including profits from sports betting, are excluded from the personal income tax.
Except for the online sports betting tax, the regulatory landscape for online sports betting in
Germany was in abeyance between 2008 and 2018 (see Appendix A for details). 15 The German
13According to the Racing Bets and Lottery Tax Act (RBLTA, §17), the term turnover includes all expenses
incurred by the bettor to participate in the wager.
14Domiciled in Germany means that the bettor has a broadly defined residence or his habitual abode in Germany.
If a German resident has placed the wager on an occasional stay outside of Germany, the tax does not apply.
(Englisch, 2013).
15A statement in the 2009 annual report of the betting provider sporting betsummarizes the industry view (and
6

regulatory framework for online gambling and betting was characterized by a division of tax and
regulatory competencies between the federal and the state level. This division of competencies
led to opaque and ineffective legislation, which was at variance with European law (European
Court of Justice, 2010) and even German constitutional law. In this regulatory environment,
betting agencies, domiciled in liberal (primarily European) jurisdictions outside Germany where
their services were admissible, could serve the German demand for sports betting in a semi-legal
(due to the free movement of services in the EU) and more or less unrestricted grey market
tolerated by German authorities (Rebeggiani and Breuer, 2017). The regulatory framework
effectively changed only in 2021.
The German case provides an ideal (quasi-experimental) setup to study the incidence of
a sports betting sin tax. First, the tax was effective in raising considerable considerable tax
revenues and the vast majority of betting agencies that target the German market followed the
tax rules despite a missing jurisdiction in Germany (see Section 5.1). Second, Germany taxes
the betting turnover, which makes the tax analogous to a classical excise sin tax. In contrast, the
vast majority of countries levy taxes on gross betting revenues, i.e., the total wagered amount
minus all winnings by bettors, (Haucap, 2021). Note that a 5% tax on turnover constitutes and
considerable levy, given that the average expected gross betting revenue per e wagered on a
single game is around 0.07 Euro cents (see section 3). Third, there was no other effective taxation
of gambling services besides the turnover tax before and after the reform. So, the estimation of
the tax incidence is not diluted by other taxes, such as corporate taxation or V ATs.
The rise of sports betting in Europe and Germany
Thanks to the internet and deregulation, sports betting—and gambling in general—is now avail-
able to a broad audience, and the sector has grown unprecedentedly over the past years. The
European Commission (2012b) describes online gambling as ”one of the fastest growing service
activities in the EU”. European online gross betting revenues, i.e., the total wagered amount
minus all winnings by bettors, grew from around e2.4bn in 2008 to over e12.1bn in 2019 (H2
Gambling Capital 2021, see more details in section 5.1). 16
As can be seen in Figure 1, German online betting revenues exhibit a similar trend to other
European countries, growing from e206m in 2008 to e1,280m in 2019. European sports betting
revenues account for around 36.3% of global sports betting revenue in 2019, second to Asia with
a share of 47.2%. If only online sports betting services are considered, Europe had the largest
share with over 50% in revenues. In contrast, sports betting revenues in North America only
account for 6.7% of global sports betting revenues (International Betting Integrity Association,
2021). However, after the legalization of sports betting by the US Supreme Court in 2018, the
sports betting revenues in the US seem to start following a similar trend to those in Europe
strategy) on the German gambling regulation quite fittingly: ”Furthermore, enforcement action against operators
where they actively target German residents (including through local marketing) has been curbed due to the lack
of clarity in the legal position. In our view, therefore, legislation that was intended to almost comprehensively
block online gambling has had only limited effect and the general inability of the German government to block
online gambling websites, coupled with the questionable legality of the legislation, has led to a continued supply
of online gambling services, and an absence of extra-territorial enforcement against the activity.”
16Revenues include onshore (i.e., regulated/taxed activity) and offshore (i.e., the revenue of operators targeting
the market without holding a local license) revenues. Revenues on the completely unregulated black market are
not included. The total wagered amount includes bonuses.
7

(Forbes, 2022).
Figure 1: Total online gross betting revenues in different countries (in eM)
Notes: This figure illustrates the annual total online gross betting revenues between 2008 and 2020 in Germany,
Italy, and France (in eM). Gross betting revenues are equal to the total wagered amount (including bonuses)
minus all winnings by bettors. Revenues include onshore (i.e., regulated/taxed activity) and offshore (i.e. revenue
of operators targeting the market without holding a local license) revenues. Source: H2 Gambling Capital –
July 2021.
2.2 The price of a bet and tax shrouding
Bets constitute simple contingent claims on different outcomes of a game with a well-defined
asset and state price (the inverse of the decimal odds), which gives betting markets a direct
application to financial markets. For this reason, betting markets are well-suited to serve as a
natural asset pricing laboratory to test market efficiency and rationality (e.g. Figlewski, 1979;
Camerer, 1989; Brown and Sauer, 1993; Woodland and Woodland, 1994; Levitt, 2004; Snowberg
and Wolfers, 2010; Moskowitz, 2021). This paper does not consider these issues but focuses on
the pass-through of betting taxes on the event’s betting margin charged by the bookmakers.
In the context of this paper, bets can be best understood as recreational consumption goods
that come with a price equal to the expected net return of a (random) bet on a specific event
from a bookmaker’s perspective. Goods are very homogeneous across providers. A price of zero
implies an actuarial fair bet with an expected return of zero. Throughout this paper, we consider
fixed odds betting markets, where prices—in contrast to parimutuel markets—are fixed at the
time of “purchase”. For each event i, there are n mutually-exclusive outcomes ( s = 1, 2, ...n).
In this paper, the outcomes are defined by the game’s result: i) home team wins; ii) away team
wins; or iii) draw. 17 Bookmaker b promises bettors to pay risb for every $1 wagered if (in event
i) outcome s is realized and zero otherwise. risb are the effective odds, including all potential
17In Basketball, Hockey, and American Football, usually, games never end with a draw as teams play overtime(s)
until one team wins the game. For this reason, we concentrate on “two-way” markets for these sports that exclude
a draw as a potential outcome. In the infrequent event of a draw (only possible in American Football), bettors’
wagers are paid back.
8

tax surcharges (see section 2.2). 18 The odd risb for an arbitrary outcome s can be expressed as:
risb = 1 θibπis , (1)
where θib is bookmaker b’s markup for event i. πis represents the (objective) likelihood of state
s, which is unobserved. However, as we observe the odds for all outcomes of an event we can
derive θib and the implied probabilities of each outcome, which is defined as ¯πis = 1 θibrisb . To do
that, we rearrange Equation 1 and sum over all possible states: 19
θi,b
nX
s=1
πi,s
| {z }
=1
=
nX
s=1
1
ri,s,b
θi,b can be understood as the amount a bettor has to pay to receive a safe payout at the end
of the game. Note that a safe payout of 1 $ can be secured by betting 1 ri,s,b $ on outcome s
of each possible outcome of an event i. In the case of unbiased odds, i.e., the odds give an
unbiased prediction of the true probabilities, the expected and certain payouts equate. I define
the consumer price of a one-dollar bet on event i as:
pib = 1 − 1 θib , (2)
which gives the expected net return of a 1 $ bet from the bookmaker’s perspective. A lower
price makes a bet “cheaper” to the bettor and less profitable to the betting agency. This notion
has the advantage that it is directly applicable to standard microeconomic theory. A tax on
betting turnover is independent of the price and can be directly treated as a standard per unit
excise tax. For instance, a 5% tax on turnover decreases the expected net revenue of the betting
agency per $1 wagered (i.e., the price of a bet) by $0.05.
Note that betting agencies sometimes use different marketing tools to attract consumers
that may indirectly affect the overall attractiveness of different providers. Examples include
cash bonuses when a bettor deposits money on their account for the first time, loyalty bonuses
that are usually “paid” out as free bets, and “odds boost” that improve the effective odds
if bettors combine a large number of bets. Most of these bonuses do not affect the betting
prices of single events. Historical data on these programs are not available. Using data from
top100bookmaker that provide a snapshot of bonus programs for several agencies in the year
2021, bonus programs seem not to vary considerably between betting agencies, so I abstract
from differences in bonuses in this paper.
Posted and effective betting prices
On a website of a betting agency, the bettors can choose from numerous events in different
leagues and for varying sports. Figure 2 presents a typical example from a website of one of
18I use the decimal odds notation in this paper that directly refers to this definition. The other common
notations are fractional (or English) odds and moneyline (or American) odds. The odds can be easily converted
and contain the same information.
19Note that in this step I implicitly assume that the bookmaker chooses markups independently of the type of
state or its likelihood.
9

the main competitors. The list on the left-hand side represents different leagues the bettor
can choose. In the main panel, one can find different events—Premier League games in our
example—with respective odds for a home win , draw, or away win . There are other betting
types for the same game, such as the number of scored goals or spread bets appearing once a
bettor clicks on a particular game.
Figure 2: Example of odds presentation on a typical website
Notes: This figure presents an example of how tax-exclusive odds are displayed on a typical website of a betting
agency (browser version) before the bettor chooses one of the outcomes. The list on the left represents the
different Leagues a bettor can select. Outcome “1” represents a win of the home team, “X” a draw, and “2” a
win of the away team. Source: Bwin.com - September 2021.
Before bettors choose one particular bet, odds for different outcomes are always presented
exclusive of a potential additional tax surcharge. All agencies refer to the surcharge as a “tax”,
similar to a value-added tax, which gives the impression that agencies must pass the tax onto
consumers. In principle, there is, however, no direct link as the tax must be remitted by suppliers,
irrespective of whether agencies are applying a surcharge. The tax authority does not directly
receive the tax surcharge. In principle, the agencies can apply other surcharges common in other
markets, such as in the aviation industry or the e-commerce sector more generally (Dertwinkel-
Kalt et al., 2020; Bradley and Feldman, 2020). However, there is no example of a betting agency
10

applying additional surcharges.
Let denote the posted, advertised surcharge-exclusive odds as ˜ risb. ˜risb may differ from the
effective surcharge-inclusive odds ri,s,b, depending on endogenous shrouding practices set by the
betting agencies. Accordingly, the surcharge-inclusive betting prices, pib, may also differ from
the implied posted tax-exclusive betting prices ˜pib, which are equal to:
˜pib = 1 − 1 ˜θib
where ˜θib = Pn s=1 1 ˜risb is the implied surcharge-exclusive markup for bookmaker b and event
i. Prior to the tax reform, there was no difference between posted and effective betting prices,
implying that pib = ˜pib. Let’s denote τ as the shrouded tax surcharge, i.e., the difference between
the tax-inclusive and posted betting prices:
τ = pib − ˜pib = 1 ˜θib − 1 θib
As evident from agencies’ annual reports, shrouding policies are an active decision by betting
agencies to increase the effective betting prices after the introduction of the sports betting tax in
Germany. For instance, the 2012 annual report of Bwin, one of the leading international betting
agencies, makes the following statement: the “gross win margin [...] increased sharply in the
second half [...] also because from August 2012 we began to withhold 5% of players’ winning
bets to cover the gaming tax due” (Bwin.party digital entertainment, 2013).
The shrouding policies are irrelevant to the tax effect on consumer prices according to the
standard theory of taxation (Kotlikoff and Summers, 1987). In these models, the pass-through
rates depend on tax-inclusive price elasticities of demand and supply and, in the case of imperfect
competition, additionally on market power (Weyl and Fabinger, 2013). See section E in the
appendix for details.
In principle, three different policies betting agencies set that affect the difference between
posted surcharge-exclusive and effective surcharge-inclusive betting odds:
i) No further deductions : The posted odds are equivalent to the effective odds: ri,s,b =
˜risb. There is no difference between advertised and effective betting prices: τ = 0.
ii) Deducting tax surcharge from winnings : In the case of a successful bet, the bettors
receive only (1 − t) of the implied surcharge-exclusive payout. As a result, the effective
tax-inclusive odds are equal to: ri,s,b = ˜risb(1 − t). This implies: τ = t ˜θib (See Appendix B
on the derivation of τ for the different shrouding policies).
iii) Deducting tax surcharge from wager : The tax surcharge applies directly to the
effective wager, such that the effective wager multiplied by (1 + t) equals the amount the
bettor pays. This implies that the effective tax-inclusive odds are equal to: ri,s,b = ˜risb (1+t) .
This policy is slightly more favorable to the bettor than policy ii), given that surcharge-
exclusive odds equate (and t >0). In this case: τ = t (1+t)˜θib .
In principle, betting agencies could also set policies in which the deductions are larger or
smaller than t. However, there is no example of a betting agency that does that. To get a better
idea about the different shrouding policies, turn again to the example above (Figure 2).
11

Suppose a bettor wants to bet on a draw between Chelsea and Manchester City (marked by
the red box). The posted tax-exclusive odds are equal to 3.30, implying that without further
deductions, the bettor would receive e3.30 for each e1 wagered in the case the game ends with
a draw. If the bettor clicks on one of the outcomes, draw in our example, there is a new panel
popping up—the betting slip (“Wettschein”)—that has an input window for the amount a bettor
wants to wager. After the amount is entered, the potential net payout, i.e., tax-inclusive odds
multiplied by the wager, is calculated and presented to the bettor. This is the first time during
the interaction with the website when tax-inclusive odds are directly posted to the bettor.
Figure 3 illustrates examples of such a betting slip of three betting agencies using different
shrouding policies for the same bet (draw in the game Chelsea vs. Manchester City). Panel ii)
refers to the betting agency in our example above applying shrouding policy ii) (“deducting tax
from winnings”). A bet of e100 would not result in a potential net payout of e330 as implied by
the tax-exclusive odds of 3.30 but only ine313.50, which is equal to 330∗(1−0.05).20 In contrast,
the betting agency in panel i) does not impose further deductions on the posted odd, implying
that the potential net payout is equal to the wager times the posted odds, e330 in our example.
To advertise that there are no further tax surcharges (“Geb¨ uhr”) on this website, the bookmaker
additionally displays the surcharges a bettor would pay with a bookmaker that deducts 5% of
the winnings as in the previous example ( e16.50), see the crossed-out red number. Panel iii)
illustrates an example of an agency that employs the third policy (“deducting a surcharge from
the effective wager”).21 The tax-exclusive odd for this agency is only equal to 3.15. Compared to
the agency in Panel ii), the agency is more transparent about how the net payout (“M¨ oglicher
Gewinn”) is calculated, displaying the steps of the underlying calculation, including effective
wager (“Effektiver Einsatz”) and the “tax” (“Steuer”) directly. The presentation of the betting
slip for other agencies by shrouding policies is very similar.
3 Data
The main data set covers fixed sports betting odds from 68 online betting agencies between
2008 and 2018 for more than 80,000 events in 16 different leagues. The events in the data set
span leagues in six different countries and five different sports. The number of unique events
per league and corresponding fractions are displayed in Table 1. For each event, I observe the
pre-match closing odds by betting agencies on each potential outcome of the game, which allows
me to calculate the price of a bet as defined above. If not stated otherwise, betting prices pib
always refer to the effective surcharge-inclusive betting prices. For each event, the data set
further records the result, date, league, country of competition, and the sport of the event. The
68 agencies include agencies that share the same brand but operate from different domains. For
instance, Bwin operates from different domains in some countries, e.g. in Italy from .it; and
in Spain from .es. I include each domain as a single agency because, typically, the prices differ
across different domains for the same brand. In total, there are 55 unique bookmaker brands in
20The yellow button “Einzahlen” button translates to Deposit, as the bettor has no money in her account. If
the bettor has sufficient funds, clicking the yellow button will place the bet.
21Please note that the bookmaker in this example uses t = 0 .053, the new tax rate after the reform in July
2021. Before the reform, the agency used t = 0.05 as well.
12

Figure 3: Example of different shrouding policies
i) No further deductions
 ii) Deduction of winnings
 iii) Deduction of wager
Notes: This figure presents examples of different betting slips (browser version) after the bettor has chosen
one of the potential outcomes: a draw in the game between Chelsea FC and Manchester City in our example.
The gross odds on the top are presented, excluding the tax, for all three panels. All of the betting slips show
the potential net payouts on the bottom. The size of the net payouts depends on different shrouding policies:
i) No (additional) deduction of taxes, i.e., effective tax-inclusive odds are equal to posted tax-exclusive odds;
ii) deduction of 5% of the winning, i.e., effective tax-inclusive odds are equal to 95% of the posted odds; iii)
deduction of 5% of the wager, i.e., the effective tax-inclusive odds are equal to 1 /1.05 of the posted odds. Note
that example iii) already applies the new tax rate of 5.3%, which was introduced in Juli 2021. Source: i)
Tipico.com; ii) bwin.com; iii) Bet365.com - September 2021.
the sample.22
3.1 Data sources
This section gives an overview of the data sources used to construct the data set. More detailed
information are provided in appendix.
Betting prices
The raw odds data is obtained from oddsportal.com—a commercial website that provides odd
comparison tools and an odds archive for many events, betting types, and periods to their
users since 2008. 23 Oddsportal.com collects the odds data directly from online betting agencies’
websites—either via their Application Programming Interface (API) or xml (Extensible Markup
Language) odds feeds (as confirmed by email exchange). Thus, one limitation of the data set
is that agencies report only one set of odds for each event. However, betting agencies could, in
principle, use different odds for different regions or countries conditional on regional IP addresses.
22A list of all betting agencies, the number of included events and observations per year, and the average price
by betting agencies can be found in the online appendix.
23Data for the betting agency Tipico, one of the leading agencies in Germany, is scraped directly from the results
archive from their website. The Tipico archive was available until its relaunch in 2020 under the following URL:
https://www.tipico.com/de/ergebnisse/. Data were available from the start of 2012 onwards. All odds before
2012 refer to odds scraped from the website of their partner label Rivalo. Rivalo provides betting services for Swiss
customers only, using identical odds as Tipico before the tax reform, and still uses the old website with an active
scrapeable results archive that dates back to 2008. In line with this claim (motivated by personal observations),
the odds in 2012 before the introduction of the tax available on the Tipico and the Rivalo webpage are identical.
There is further no jump in betting prices between 2011 and 2012. All raw odds are surcharge-exclusive.
13

Historical archived odds may thus not necessarily refer to the actual odds displayed to bettors
in different countries. However, several points assures me that this is not a major concern for
this study. First, to the best of my knowledge, there is no evidence in the agencies’ annual
reports or on other websites that agencies have engaged in such behavior between 2009 and
2018. Second, while it is not possible to check which odds were displayed to German customers
in the past, I have manually compared the ”live” odds displayed on oddsportal.com with odds
on the agencies’ websites for a subsample of events in 2021. The comparisons were made from
a German IP address. I could not find any discrepancies between the odds on oddsportal.com
and the agencies’ websites. 24 Third, if the odds on oddsportal.com were considerably off from
the true odds in different countries, their services would provide no value to their consumers.
Fourth, there are several ”local” agencies that operate from country-specific domains that are
only accessible by domestic bettors.
Table 1: List of included competitions and number of unique matches
League Sport Country # Outcomes # Matches Percent
Bundesliga Soccer Germany 3-way 3,060 3.78
2. Bundesliga Soccer Germany 3-way 3,109 3.84
3. Liga Soccer Germany 3-way 3,802 4.70
Premier League Soccer England 3-way 3,801 4.70
Championship Soccer England 3-way 5,558 6.87
Primera Division Soccer Spain 3-way 3,807 4.71
Segunda Division Soccer Spain 3-way 4,691 5.80
Serie A Soccer Italy 3-way 3,819 4.72
Serie B Soccer Italy 3-way 4,668 5.77
Ligue 1 Soccer France 3-way 3,789 4.68
Ligue 2 Soccer France 3-way 3,818 4.72
Bundesliga Handball Germany 3-way 3,097 3.83
Bundesliga Basketball Germany 2-way 3,305 4.08
NBA Basketball USA 2-way 13,702 16.94
NFL Am. Football USA 2-way 3,323 4.11
NHL Hockey USA 2-way 13,560 16.76
Total 80,909 100.00
Notes: The table lists the leagues included in the data set together with the respective
sport, the country of the league, and the number of potential outcomes of the consid-
ered bet. The last two columns report the number of unique matches and respective
frequencies for each league.
Agency characteristics and shrouding policies
To determine the type and timing of the betting agency’s ”shrouding” policy, I match the odds
data with hand-collected data from different sources. The sources include annual reports of
the listed agencies, websites from betting agencies, web-scraped information from different com-
mercial betting websites and forums, including Top100bookmakers.com, as well as information
from bodies that represent the interest of betting agencies, such as the ”Deutsche Sportwetten-
verband” (DSWV, German sports betting association) and the European Gaming and Betting
24Exemplary screenshots can be provided upon request.
14

Association (EGBA). 25 I further use information from official regulatory bodies, including the
Malta Gaming Authority (MGA). The matched data set further allows me to infer whether a
betting agency targets the German market or not.
Online betting and tax revenues
Data on online betting revenues was provided by H2 Gambling Capital (website:https://h2gc.
com/). H2 Gambling Capital is a betting and gaming consultancy that is one of the leading
market data providers in the gambling industry. Their data is regularly used by the main listed
sports betting agencies in their annual reports (e.g. Bwin.party digital entertainment, 2013)
and by the International Betting Integrity Association – IBIA (International Betting Integrity
Association, 2021). The data is primarily taken from information by official gambling regulatory
bodies in different jurisdictions, governments, and tax authorities. It only includes revenues of
operators licensed in at least one jurisdiction. Entirely unlicensed activities (black market)
are not included. Collecting and disaggregating the data, H2 further uses information from
national monopoly operators (where available for land-based and onshore interactive activity)
and information derived from major operators and suppliers active in each market, including
publicly available reports. To determine whether an agency targets a particular market, H2
undertakes a biannual audit of all operators, examining whether agencies proactively target
domestic players, accept domestic players, or (not) prohibit domestic players from betting. 26
Tax revenues refer to administrative tax data of the German Federal Ministry of Finance.
3.2 Descriptive statistics
In total, there are around 3.3m observations in the data set. Each observation refers to a unique
event and betting agency combination. The increasing number of observations over time (Table
2) can be explained by an increasing number of betting agencies included in the data set. 27
Differences in observations across leagues are primarily due to a varying number of games per
season. Betting agencies offer a wide range of leagues that usually cover the major leagues and
sports considered in this paper, even at the start of their services.
Table 2 illustrates the mean and standard deviation of (tax-inclusive) betting prices. The
average betting price for all events is equal to 0.0706, which implies, as described above, that
a betting agency makes around 0.0706 e per wagered e.The mean of betting prices for soccer
games is equal to 0.0734, and the standard deviation slightly decreases from 0.0317 to 0.0315.
If we only consider agencies for which odds data is available for all years, the average betting
25I use snapshots from Top100bookmakers.com at two dates: September 2021, which I collected, and data that
was already used in Montone (2021). I am immensely thankful to Maurizio Montone, who provided me with the
data. Other websites include: www.wettforum.info, www.wettbuero.de, www.wettsteuer.com and others.
26According to email correspondence, H2 further considers any actual market information by companies and
feedback from their users (they currently have well over 1,000 users with access to different local operators and
suppliers) when allocating activity across markets. Furthermore, they also consider any restrictions in place, any
onshore supply, and several generic measures ranging from GDP to broadband and smartphone penetration to
check the size of each market. The author thanks H2 for providing the data on a pro-bono basis.
27Missing observation for some agencies in specific years or specific events can have three explanations: i) the
agencies were not operating in a given year; ii) the agencies were providing betting services for a specific event;
or iii) oddsportal.com was not collecting the odds for a betting agency for a specific year or event. According to
an email by oddsportal.com, the reasons are purely technical and primarily related to betting agencies’ APIs.
15

Table 2: Summary statistics - betting prices by league and year
League - Sport Mean Std.Dev. Observations
All agencies:
All events 0.0706 0.0317 3,289,135
Soccer events 0.0734 0.0315 2,067,137
Agencies with data for all years:
All events 0.0727 0.0273 2,259,449
Soccer events 0.0770 0.0271 1,407,215
All agencies by League:
Bundesliga - Soccer 0.0621 0.0280 147,894
2 Bundesliga - Soccer 0.0792 0.0302 147,501
3 Liga - Soccer 0.0887 0.0289 161,139
Premier League - Soccer 0.0576 0.0284 184,909
Championship - Soccer 0.0740 0.0325 264,213
Primera Division - Soc.. 0.0616 0.0284 183,514
Segunda Division - Soc.. 0.0847 0.0311 220,208
Serie A - Soccer 0.0627 0.0286 184,610
Serie B - Soccer 0.0848 0.0307 214,155
Ligue 1 - Soccer 0.0659 0.0276 179,113
Ligue 2 - Soccer 0.0819 0.0285 179,881
Bundesliga - Handball 0.0932 0.0321 115,624
Bundesliga - Basketball 0.0752 0.0282 110,088
NBA - Basketball 0.0615 0.0294 474,717
NFL - American Football 0.0585 0.0280 112,485
NHL - Hockey 0.0630 0.0314 409,084
All agencies by Y ear:
2009 0.0745 0.0275 199,885
2010 0.0725 0.0264 229,491
2011 0.0747 0.0301 255,470
2012 0.0752 0.0315 288,038
2013 0.0770 0.0327 325,451
2014 0.0748 0.0329 353,585
2015 0.0708 0.0320 377,322
2016 0.0678 0.0323 391,238
2017 0.0649 0.0322 437,352
2018 0.0622 0.0312 431,303
German agencies by shrouding policy:
No ”shrouding” (i) 0.0737 0.0199 24,351
Deduction from winnings (ii) 0.0726 0.0225 143,842
Deduction from wager (iii) 0.0745 0.0207 47,068
Notes: The first four rows of the table display the mean and standard deviation of
betting prices for all events and soccer events only, considering all agencies or only
agencies for which odds data is available in all years. The two middle panels show
the summary statistics for all agencies disaggregated by leagues and years. The
last rows illustrate the mean and standard deviation of pre-reform betting prices
of treated agencies grouped according to the respective implemented post-reform
”shrouding” policy. The last column reports the respective number of observations.
One observation refers to a price for a specific event and bookmaker.
16

prices slightly increase to 0.0727 and 0.0077, respectively. In contrast, the standard deviation
decreases to around 0.027.
In general, the betting prices vary across different leagues. Prices are smaller for ”higher”
leagues, where the number of bettors and competition among agencies is usually higher. A
larger standard deviation accompanies this difference. Furthermore, prices tend to be smaller
for sports with two possible outcomes (Basketball, American Football, Hockey).These findings
align with results by Montone (2021), who rationalizes the findings with risk-averse bookmakers.
The prices across different countries, controlling for the division, are very similar. Only English
leagues tend to exhibit a comparably smaller price, which may relate to the larger market size
and competition in the UK. Prices show a decreasing trend after 2013. Before 2013, betting
prices are relatively constant over time. 28
Figure 9 in the appendix illustrates the distribution of betting prices across all observations
for all sports and soccer games. The distribution is relatively symmetric around the mean of
betting prices. There is, however, some excess mass around a betting markup of around 0.1, a
standard assumption often made in the literature that studies relative betting prices (e.g. Levitt,
2004). A log transformation considerably skews the data to the right, as prices are smaller than
1, which is, besides the direct interpretability, one of the main reasons why I concentrate on
absolute betting prices in my empirical analyses.
4 Methodology
4.1 Empirical strategy
Average tax effect on consumer prices
To estimate the effect of the betting tax on consumer prices, I use a DID framework. I compare
changes in consumer betting prices (as defined above) around the 2012 tax reform between
German and Non-German agencies. DID frameworks are commonly used to causally estimate
the pass-through of taxes (e.g. Doyle and Samphantharak, 2008; Harding et al., 2012; Hindriks
and Serse, 2019; Harju et al., 2018, 2022). In the main specification, I estimate the following
equation:
pi,m(t,c) = β0 + β1Ti,t + αi + λt + ψc + ϵi,m, (3)
where pi,m(t,c) is the betting price of agency i for event m, taking place in week t and league
c. Ti,t is a dummy variable that equals one if agency i is in the treatment group, i.e., is active in
the German market, and the event takes place after the tax was in place. αi, λt, ψc are agency,
week and league fixed effects. I use robust standard errors clustered on the agency level.
The main identifying assumption is that the betting prices of treated and control agencies
would have followed a parallel time trend in the absence of the tax reform, controlling for
time, agency, and league fixed effects. If the parallel trend assumption holds, β1 identifies
the average causal effect of the betting tax on consumer betting prices with an equal weight
on each observation. Note that the tax is applied to all treated agencies at the same time.
28Please note that betting prices from 2012 onward can be affected by the sports betting tax.
17

Consequently, the issue of biased multi-period DID estimators (commonly referred to as ”two-
way fixed-effects” models) in settings with heterogenous treatment effects and timing does not
apply.29 In addition, the treatment can be expected to be exogenous to betting prices since
the tax reform is mainly determined by unrelated political processes and rulings by courts (see
section 2.1). Yet, changing regulation after the German tax reform in other European countries
may still confound our estimates. Note, however, that most European countries, including the
UK, Italy, and France, comprehensively regulated online sports betting already before 2012,
implying that effects of these regulation should already show up in the pre-trends. 30
As there was effectively no taxation on online betting services in Germany before the reform
and no additional taxes after the reform, the change in consumer prices can be directly translated
to the pass-through rate of the sports betting tax on consumer prices. The estimated pass-
through of the tax is equal to dp dt = β1 0.05 .31 Besides the Sports Bet Tax, producer prices q are
assumed to follow the same trend as consumer prices before and after the tax reform, such that
the incidence of producers is equal to dq dt = 1 − dp dt .
While it is not possible to test the parallel trends assumption directly, the assumption is
more plausible if betting prices in the control and treatment groups showed a common trend
prior to July 2012. Figure 4 show average quarterly and weekly betting prices over time for all
agencies in the sample. The circles signify average weekly betting prices in each group pooled
and aligned by the respective quarter. The solid line illustrates the average quarterly betting
prices. Prior to the introduction of the tax reform, which is illustrated by the vertical red line,
the average betting prices moved very similarly over time in both groups. We observe common
pre-trends if we consider all sports (Panel a), only soccer events are considered (Panel c) and if
exclude cross-leagues, i.e., Non-German Leagues in the Treatment group and German games in
the Control group, the trends prior to the tax introduction remain very similar (Panels b and d).
The same holds true if we only consider agencies for which odds data is available for all periods
(Figure 10). Betting prices are higher on average before July 2012 for agencies with a foreign
domain than in the treatment group (see Panels a and b of Figure 11). At the same time, the
pre-trends between these two groups are parallel, implying that the parallel trend assumption
also holds in this case.
The observed seasonality in betting prices, considering all sports, stems from the fact that
there are relatively more events with two potential outcomes in the winter, Basketball, Hockey,
and American Football, that tend to have lower prices. Given that more than 80% of all wagers
are made on Soccer matches in the European market (Tipico, 2019), and soccer games are not
affected by seasonality, I will mainly focus on soccer matches in the remainder of this paper.
To provide a more structured test of the parallel trend assumption and examine how the pass-
through to consumer prices evolve over time, I estimate the following multi-period event study
design:
29A detailed discussion of these issues can be found here: De Chaisemartin and d’Haultfoeuille (2020); Goodman-
Bacon (2021); Sun and Abraham (2021).
30Thomson Reuters and the Global Legal Group provide detailed overviews of online gambling law
in different European countries: https://uk.practicallaw.thomsonreuters.com/ and https://iclg.com/
practice-areas/gambling-laws-and-regulations .
31This notation implicitly assumes that the marginal (or local) pass-through rate is equal to the non-marginal
(or global) pass-through rate, which is only true for the linear case. The global pass-through rate is equal to the
average local pass-through rate over the respective tax change interval.
18

Figure 4: Avg. tax-inclusive consumer betting prices of all German and Non-German betting
agencies over time
(a) All sports
 (b) Soccer games
(c) All sports - excluding cross leagues
 (d) Soccer games - excluding cross leagues
Notes: This figure shows the average quarterly and weekly betting prices over time for agencies that target the
German market (Treatment) and for agencies that do not target the German market (Control). All agencies in
the Control and Treatment group are considered, N=65 (Treatment=10/Control=55). The circles signify average
weekly betting prices in each group, pooled and aligned by the respective quarter. The solid line illustrates the
average quarterly betting prices. The odds for the graphs are trimmed at the quarterly 1- and 99-percentiles,
considering all events and all agencies. Panel (a) and (c) consider all sports included in the data set, while
Panel (b) and (d) only consider soccer events. Panel (c) and (d) exclude German leagues for the control group
and Non-German leagues for the treatment group. The vertical red line illustrates the introduction of the tax
reform.
19

pi,m(t,c) = αi + λt + ψc +
25X
k=−13
βkDk i,t + ϵi,m, (4)
where Dk i,t is an indicator for event m being k quarters relative to the introduction of the
tax when the agencies i is in the treatment group. Dk i,t equals zero for all agencies in the control
group. For better results readability, t refers to a quarter instead of a week here. The results are
robust if I use week-fixed effects instead. Insignificant coefficients for leading quarters, k <0,
indicate that the parallel trend assumption is plausible.
Heterogeneity in tax incidence
I use two approaches to estimate heterogeneity in pass-through rates conditional on different
”shrouding” policies. First, I run specifications 3 and 4 for different agencies’ subsamples condi-
tional on the applied shrouding policy. This categorization is consistent over time, as I observe no
switching back to ”No shrouding” once one of the shrouding policies is implemented or between
different ”shrouding” policies.
Second, I use an interaction term that interacts treatment (Ti,m) with a noShroud i,m indica-
tor that equals one if the event took place after the tax reform and agency i had a NO shrouding
policy in place for event m. In detail, I estimate the following equations for the average tax
effects on betting prices:
pi,m(t,c) = β1Ti,t + β2Ti,t × noShroud i,m + αi + λt + ψc + ϵi,m, (5)
The coefficient on Ti,t can be interpreted as the effect of the tax on betting prices when a
shrouding policy was in place for a specific event and agency. In contrast, the coefficient of
the interaction term estimates the difference between the tax effect when no shrouding policy
was in place and the tax effect when a ”shrouding” policy was in place. Accordingly, the t-
statistics of the coefficient on the interaction term can directly serve as a test of a differential
tax effect conditional on whether a shrouding policy was in place or not. The interpretation of
the estimated effects between the subsample analyses and the regressions with the interaction
term differ because ”shrouding” policies, used for the subsample analyses, are defined on the
agency level, while the noShroud i,m dummy is defined on the agency-time dimension. This
implies that coefficients of the subsample analyses may be diluted because it includes treated
observations in ”shrouding samples”, in which agencies that switched to shrouding later have
not put the shrouding policy in place yet. In contrast, the estimation with an interaction term
compares prices for treated events not subject to an active shrouding policy with events for
which an active shrouding was in place.
Similarly, I also interact the leads and lags of periods relative to the tax ( Dk i,t) with the
noShroud i,m indicator to capture the dynamics in the differential tax effects over time:
pi,m(t,c) = αi + λt + ψc +
25X
k=−13
βkDk i,t +
25X
k=−13
βkDk i,t × noShroud i,m + ϵi,m, (6)
The heterogeneity analyses require somewhat stronger assumptions. The parallel trend as-
sumption remains crucial to estimating the causal effects of the tax on consumer prices in the
20

different subsamples. The difference is that the parallel trend assumption now applies to the
respective treatment group subsamples (and not to all agencies in the treatment group) and the
control group. For the heterogeneity analyses, we need to assume that the shrouding policies are
exogenous to changes in price setting behavior and firms’ characteristics that affect price setting
behavior, conditional on time and agency fixed effects. Agencies seem to not differ significantly
in price setting behavior before the reform (see Table 2), and pre-trends follow the same trends as
the control group for the shrouding and non-shrouding subsamples (see Figure 8, Panel a). Yet,
shrouding practices are endogenous by definition, and differences in pass-through rates should
thus not be interpreted as being caused by the shrouding practices alone. Other characteristics
correlated with the shrouding policies may also drive part of the observed heterogeneity.
4.2 Defining the control and treatment group
One of the critical issues for a clean identification of the tax incidence of the German sports
betting tax is to define a consistent and reliable treatment and control group. The treatment
group should consist of agencies that provide their services to German customers, i.e., who are
active in the German market. The control group should ideally consist of agencies whose services
are not available to German customers, i.e., that do not operate in the German online betting
market. This categorization is challenging due to the opacity and the cross-border dimension of
the online betting market.
I limit the potential set of treated bookmakers to agencies that are or were members of
the DSWV, the German sports betting association. The DSWV, founded in 2014, represents
the interest of leading German and European sports betting providers and describes itself on
its website as ”the public contact of their members to German politics, sports, and media”.
The members of the DSWV represented around 90 percent of the entire German sports betting
market in August 2018 (Deutscher Sportwettenverband, 2018). According to the information
from Top100bookmakers.com, used in Montone (2021), all of these agencies had a German
language version as of 2021. I further use the hand-collect data on this sub-set of agencies (see
above) to track their activities in the German betting market over time. Agencies only active
in Germany for a limited period between 2009 and 2018 are excluded from the sample. 32 This
approach leaves me with a subsample of ten agencies in the Treatment group, henceforth also
referred to as ”German” agencies, to ease readability.33 While I am confident that this approach
limits the treatment group to agencies that were active in the German market between 2009
and 2018, defining a stringent control group is more challenging, as this requires ruling out that
these agencies were never serving German customers at any point.
In the main specification, I include all other remaining agencies in the data set in the control
group. However, I cannot entirely rule out that some German bettors bet with one of the foreign
betting agencies that do not primarily target the German market. In this case, the estimated
32This approach excludes three betting agencies for the estimation: Expekt, Pinnacle, and Betclic. The empir-
ical results are robust if we include these agencies in our sample.
33The set of German agencies: Betfair Sportsbook, Betsson, Betway, Interwetten, Sportingbet, Tipico, Unibet,
Bet365, Bet-at-home, and Bwin. Betfair Sportsbook does not refer to the well-known betting exchange but to
a subsidiary that offered fixed odds betting services to German customers after the exchange left the German
market. Odds data for Betfair sportsbook are available from the third quarter of 2015. I included Betfair
sportsbook in the treatment group as the agency was active on the German market over all periods where data
is available. Data for all other treated agencies is available for the entire observation period.
21

pass-through rates are potentially biased.
I take two approaches to resolve these concerns. First, I restrict the control group to agencies
that are linked to a foreign country-specific domain. Agencies that operate from country-specific
domains are usually only available to customers in these countries. Furthermore, even if foreign
customers could, in principle, access the webpage, e.g., through a VPN client, they should have
no possibility to register with the respective agency. If I consider all agencies, there are 65
agencies in the sample. Ten are treated, and 55 are in the control group. If I exclude agencies
for which data is only available for a subset of years, the number of agencies decreases to 30,
with nine agencies in the treatment and 21 agencies in the control group. If I only consider
agencies in the control group with a foreign domain, the number of agencies in the control group
decreases to 22 and 6, respectively. According to the domain identifier, 12 out of 22 agencies
that use a country-specific domain are located in Eastern Europe (Slovakia, Czech Republic,
Poland, and Russia). Four agencies use an Italian, three a French, and three a Spanish domain.
Second, suppose that bettors prefer to bet on local games. In this case, potential concerns
can be alleviated by excluding ”cross” leagues, i.e., German Leagues for Non-German agencies
and Non-German games for German agencies. Without ”cross” league events, the control group
only includes betting markets on foreign events that are less likely to be populated with German
bettors— and thus less affected by potential confounders. Similarly, the treatment group then
only includes domestic markets that are primarily populated with German bettors and thus more
realistically represent (changes in) German consumer prices. Following the same argument, I
also run robustness checks only considering lower-level leagues that are assumingly even less
prone to cross-country bettors.
Heterogeneity in ”shrouding” policy implementation
As already discussed above, betting agencies mainly engage in three different ”shrouding”
policies that affect the difference between the advertised surcharge-exclusive and the effective
surcharge-inclusive odds: i) no further deductions; ii) deducting tax surcharge from winnings;
iii) deducting a surcharge from the wager. Six out of the ten treated agencies choose policy
ii), while two choose policy iii), and two do not apply additional tax surcharges for the entire
observation period. Most agencies that choose policy ii) or iii) implement ”shrouding” policies
within six months after the tax reform. There is one ”outlier” that switches from no ”shrouding”
to policy iii) only in March 2016. The type and timing of ”shrouding” policies for all treated
agencies can be found in the Appendix in Table 6. No agency switches back to policy i) or
between policies after one of the policies was established. The average pre-reform betting prices
conditional on post-reform policies do not differ considerably and range from 0.0726 to 0.0745
(Table 2).
5 Results
Before I show the estimated tax effects according to Section 4.1, I examine whether agencies
follow the tax rules, which is crucial for the validity of the estimation approach and has important
implications for digital taxation in general.
22

5.1 Sports betting tax revenues
As noted above, most betting agencies operate from offshore locations and usually have no
jurisdiction in Germany. Consequently, it is not straightforward to assume that agencies also
pay the German sports betting tax—an issue that is common for many highly digitalized business
models. In this section, I use administrative tax data and aggregated sports betting revenue
data provided by a commercial provider to examine whether agencies follow the tax rules.
Figure 5 shows the aggregated yearly sports betting tax revenues, according to administrative
tax data of the German Federal Ministry of Finance (2021). Tax revenues more than doubled
from around e200m in 2013 to over e450m in 2019. In total, the German sports betting tax
generated revenues of more than e2.6bn until 2020.
Figure 5: German sports betting tax revenue 2012-2020 in eM
Notes: This figure illustrates the aggregated annual tax revenue (ineM) generated by the German sports betting
tax between 2012 and 2020. The tax revenue in 2012 only covers a period of 6 months, as the tax was introduced
on 1 July 2012. Source: German Federal Ministry of Finance, own representation.
Figure 6 illustrates the annual total gross online betting revenues between 2008 and 2020
in Germany, disaggregated by onshore and offshore betting revenues. 34 Onshore revenues refer
to all online sports betting activities for which taxes were paid in Germany. Offshore revenues
include all sports betting revenues by agencies that target the German market but do not
pay the sports betting tax in Germany. Note that gross betting revenues are defined as the
total wagered amount minus all winnings by bettors. Consequently, gross betting revenues’ size
directly depends on the price adaptions by agencies, ceteris paribus. In contrast, the tax base
only indirectly depends on betting prices through behavioral responses by bettors.
As illustrated by the bars in Figure 6, the share of taxed betting revenues is constantly
over 80% after the tax reform in 2012. The share shows a slightly increasing trend. One can
conclude that the vast majority of betting agencies that target the German market also paid the
34For 2012, the onshore revenues refer to annual revenues by agencies that paid sports betting taxes after the
tax reform in 2012.
23

Figure 6: Onshore vs. offshore gross online betting revenues in Germany in eM
Notes: This figure illustrates the annual total gross online betting revenues between 2008 and 2020 in Germany
(in eM), disaggregated into onshore and offshore betting revenues. The bars illustrate the share of onshore
betting revenues. Onshore revenues refer to all sports betting activities for which taxes were paid in Germany.
For 2012, the onshore revenues refer to all revenues by agencies that paid sports betting taxes in 2012. Offshore
revenues include all sports betting revenues by agencies that target the German market but do not pay the sports
betting tax in Germany. Gross betting revenues are equal to the total wagered amount (including bonuses) minus
all winnings by bettors, disaggregated by onshore and offshore agencies. Data was provided by H2 Gambling
Capital (July 2021) and is primarily based on official data from official gambling regulatory bodies, governments,
and tax authorities. The data only includes revenues of operators licensed in at least one jurisdiction, and entirely
unlicensed activities are not included.
sports betting tax, despite a missing jurisdiction in Germany. Annual reports of listed betting
agencies regularly discuss the implications of the German sports betting tax for their business
(e.g. Bwin.party digital entertainment, 2013), confirming this conclusion.
While this finding seems rather trivial, it is noteworthy in the context of digital taxation.
The German sports betting tax shares several features with digital service taxes that aim to tax
domestic revenues of international digital businesses.35 Several countries introduced such digital
service taxes in recent years to protect their domestic tax base from extensive profit shifting
by digital firms that typically do not require a physical presence in a specific country to serve
domestic customers (OECD, 2014). 36
Operating from an offshore location implies that monitoring and prosecution by public au-
thorities are very difficult or even impossible. Thus, one objection to introducing digital taxes,
at least in some sectors, is that digital taxes are unlikely to raise significant tax revenues as most
firms that are not registered with the tax authorities will also not pay domestic taxes. In the
setting at hand, firms do not only operate from jurisdiction to avoid taxes but also to circum-
vent national bans, making the argument particularly applicable in our setting. In fact, many
observers of the debate questioned in the beginning whether 5% on stakes would be low enough
that private betting agencies would cooperate with the German tax authorities (Englisch, 2013).
35Online betting services are a good example of a highly digitalized business model. All three factors of
highly digitalized business models, as defined by the OECD (2014) apply to the online betting market: i) Cross-
jurisdictional scale without mass, ii) Reliance on intangible assets, including intellectual property (IP). iii) Data,
user participation, and their synergies with IP.
36For an overview of the current state of digital services taxes in different countries, see KPMG (2022).
24

My findings suggest that taxing online sports betting and digital services can generally work,
in the sense, that they can generate considerable tax revenues even if the taxed entity has no
jurisdiction within the respective country. Agencies seem not to evade the German sports betting
tax on a large scale. 37
5.2 Overall effect on consumer prices
The results for the average tax effects can be found in Table 3 and 7. The estimated average
pass-through ( dp dt ) in our main specification, which considers all agencies and leagues for soccer
games and includes week, league, and agency fixed effects (Column 2, Table 3), is equal to 76%
(β1=0.038 with a standard error (SE) of 0.004). The average pass-through increases to 82% if
we exclude ”cross” leagues. The estimated pass-through rates remain robust to only considering
agencies with odds data available for all years or using betting prices for all sports events (Table
7). Furthermore, the average pass-through rate remains unchanged if we consider a TWFE
model with only time and agency fixed effects (Columns 1 and 4, Table 3) or if we include
league-by-agency fixed effects instead (Columns 3 and 6, Table 3).
Table 3: Avg. effect of tax on consumer betting prices - soccer matches
All Leagues Excl. ”cross” leagues
(1) (2) (3) (4) (5) (6)
Panel A: All agencies
Tax effect on prices 0.038 ∗∗∗ 0.038∗∗∗ 0.038∗∗∗ 0.041∗∗∗ 0.041∗∗∗ 0.041∗∗∗
(0.004) (0.004) (0.004) (0.005) (0.005) (0.005)
Observations 1,936,322 1,936,322 1,936,322 1,290,843 1,290,843 1,290,843
R2 0.642 0.759 0.811 0.643 0.754 0.809
Panel B: Comp. agencies
Tax effect on prices 0.038 ∗∗∗ 0.038∗∗∗ 0.038∗∗∗ 0.041∗∗∗ 0.041∗∗∗ 0.041∗∗∗
(0.005) (0.005) (0.005) (0.005) (0.005) (0.005)
Observations 1,276,400 1,276,400 1,276,400 778,207 778,207 778,207
R2 0.521 0.699 0.747 0.467 0.660 0.711
Constant Yes Yes Yes Yes Yes Yes
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes No Yes Yes No
League FE No Yes No No Yes No
League-agency FE No No Yes No No Yes
Notes: This table reports the estimated average sports betting tax effects on consumer betting prices of
soccer events according to Eq. 3, comparing changes in prices before and after the tax reform between Ger-
man and Non-German agencies. Each agency-event combination (unique observation) is equally weighted.
Columns 1-3 consider all leagues, while Columns 4-6 exclude events in German leagues for the control
group and Non-German leagues for the treatment group. All estimations include time-fixed effects, and
the columns differ in the included agency and league fixed effects. Estimations in Panel A consider obser-
vations from all agencies, and Panel B considers agencies with observations from all years only. Robust
standard errors clustered at the agency level are reported in the brackets. * denotes significance at the
10-%, ** at the 5-%, and *** at the 1-% level.
Results for the dynamic tax effects of the tax reform, illustrated by the connected black
37Tax evasion has important implications for the relationship between statutory incidence and the economic
incidence of the tax (e.g. Kopczuk et al., 2016).
25

squares, can be found in Figure 7. The grey shaded area illustrates the respective 95% confidence
intervals. Coefficients for all periods before the tax reform are statistically insignificant. The
average quarterly pass-through rates steadily increase in the first four quarters after the tax
reform to around 0.035 (70%). This development is associated with the staggered introduction
of different shrouding policies that seem to help agencies pass a larger share of the tax onto
consumers. After one year, the pass-through rate stays at around 80% for several quarters with
a slightly increasing trend. At the end of the observation period, the estimated βk-coefficients
reach around 0.045. In general, the pass-through rate of the tax seems very persistent over
time. Similar to the average effects, the coefficients slightly increase if we exclude cross-leagues,
showing the same general pattern.
Figure 12 in the Appendix shows the estimated dynamic tax effects for samples that only
considers agencies with a complete set of odds data (Panels c-f), and events for all sports (Panel
a and b). In general, the pattern of the tax effect dynamics are similar to the main specification.
The estimated coefficients tend to be slightly smaller if we consider all sports. Pass-through rates
seem to be slightly higher for soccer games if we only consider ”complete” agencies, reaching
nearly a full-pass through ( β = 0 .05) in 2018. In general, not only the coefficients, but also
the confidence intervals are quite stable across different specifications and samples. To check
whether the results are driven by outliers, I also estimate equation (5) based on trimmed data
(1-99% percentiles). The results are robust and can be found in Figure 13 in the Appendix.
The estimated average and dynamic pass-through rates are higher for specifications with the
more restrictive control group that only includes agencies that operate from a foreign nation-
specific domain. The pass-through rates are close to a full-pass-through for these specifications
(see Table 8 in the Appendix). However, these slightly larger pass-through rates can be mainly
attributed to higher estimates in later periods (Panel c and d of Figure 11) that may be partly
driven by specific developments in these local (control) markets. According to the domain
identifier, 12 out of 22 agencies that use a country-specific domain are located in Eastern Europe
(slovakia, Czech Republic, Poland and Russia), four agencies use an Italian, three a French and
three a Spanish domain.
The estimated average and dynamic pass-through rates are higher for specifications with the
more restrictive control group that only includes agencies that operate from a foreign nation-
specific domain. The pass-through rates are close to a full pass-through for these specifications
(see Table 8 in the Appendix). However, these slightly larger pass-through rates can be mainly
attributed to higher estimates in later periods (Panel c and d of Figure 11) that may be partly
driven by specific developments in these local (control) markets.
5.3 Heterogeneity in tax effects
Table 4 shows the results of the subsample analyses. There is large heterogeneity in pass-through
rates depending on the agencies’ shrouding policy (see Section 2.2). The estimated average pass-
through in the subsample that only considers treated agencies that do not shroud taxes for the
entire observation period is about 16% (Column 3, Table 4). In contrast, agencies that shroud
taxes can pass most of the tax onto consumers. Excluding all ”transparent” agencies from
the sample, I estimate a pass-through of 82% (Column 2, Table 5. These differences get even
more pronounced when excluding ”cross” leagues or extending the data set to non-soccer events.
26

Figure 7: Pre-trends and tax effects on consumer betting prices over time - all agencies
(a) Soccer games
(b) Soccer games - excluding cross leagues
Notes: This figure shows the estimated effects (according to Eq. 4) and respective 95-% confidence intervals
of the German sports-betting tax on consumers’ betting prices for soccer events over time. All agencies are
considered, N=65 (Treatment=10/Control=55). In contrast to Panel (a), Panel (b) excludes German leagues
for the control group and Non-German leagues for the treatment group. The vertical dashed line illustrates the
introduction of the tax reform. The horizontal dotted line signifies a full pass-through of the tax on consumers.
27

For instance, the β1 coefficients for the ”No shrouding”-subsample is only slightly positive and
insignificant (see Panel B, Table 4) when all events are used in the estimations.
Interestingly, there is also heterogeneity in estimated pass-through rates along the two
shrouding policies (columns 2 and 3, Table 4). Agencies employing the shrouding policy that
deducts the tax from the winnings increase their betting prices most significantly in response to
the tax, with an estimated tax effect of 0.043. In contrast, the estimated tax effect for agencies
that deduct the surcharge directly from the wager only equals 0.036. This difference is consider-
ably larger than one would expect, given the policies’ different τ (see Section B). The difference
between the shrouding policies could be explained by a lower tax salience when the surcharge
is framed as being only due in the case of winning. While it does not make a big difference
for the effective betting prices, the framing may exploit a present bias where tax surcharges are
weighted less if they are deducted only in the case of winning.
Table 4: Avg. effect of tax on consumer betting prices - Subsamples different policies
All Leagues Excl. ”cross” leagues
”Shrouding” policy (ii) (iii) (i) (ii) (iii) (i)
(1) (2) (3) (4) (5) (6)
Panel A: Soccer
Tax effect on prices 0.043 ∗∗∗ 0.036∗∗∗ 0.008∗∗∗ 0.046∗∗∗ 0.043∗∗∗ 0.008∗∗
(0.003) (0.007) (0.002) (0.003) (0.005) (0.002)
Constant 0.085 ∗∗∗ 0.085∗∗∗ 0.085∗∗∗ 0.091∗∗∗ 0.091∗∗∗ 0.091∗∗∗
(0.003) (0.003) (0.003) (0.003) (0.003) (0.003)
Observations 1,793,974 1,619,606 1,587,090 1,257,582 1,217,911 1,211,548
R2 0.764 0.743 0.728 0.754 0.743 0.737
Panel B: All sports
Tax effect on prices 0.044 ∗∗∗ 0.034∗∗∗ 0.002 0.041 ∗∗∗ 0.037∗∗∗ 0.001
(0.002) (0.007) (0.002) (0.002) (0.007) (0.002)
Constant 0.079 ∗∗∗ 0.084∗∗∗ 0.084∗∗∗ 0.088∗∗∗ 0.088∗∗∗ 0.088∗∗∗
(0.003) (0.003) (0.003) (0.003) (0.003) (0.003)
Observations 2,815,902 2,512,623 2,466,796 1,974,102 1,912,848 1,901,791
R2 0.745 0.716 0.703 0.736 0.721 0.713
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes Yes Yes Yes Yes
League FE Yes Yes Yes Yes Yes Yes
Notes: This table reports the estimated average sports betting tax effects on consumer betting
prices according to Eq. 3, comparing changes in prices before and after the tax reform between
German and Non-German agencies. Columns 3 and 6 only consider German agencies that do
not shroud taxes. Likewise, columns 1 and 4 (2 and 5) only consider agencies that deduct a
5% tax surcharge from the advertised winnings (from the advertised wager). Each agency-event
combination (unique observation) is equally weighted. Columns 1-3 consider all leagues, while
Columns 4-6 exclude events in German leagues for the control group and Non-German leagues for
the treatment group. All estimations include time-, agency- and league-fixed effects. Estimations
in Panel A consider observations from soccer matches, and Panel B considers observations from
all sports. Robust standard errors clustered at the agency level are reported in the brackets. *
denotes significance at the 10-%, ** at the 5-%, and *** at the 1-% level.
The results from the subsample analyses are confirmed by estimating equation 5 (Columns
28

3 and 6, Table 5). The coefficient on Ti,m can be interpreted as the effect of the tax on betting
prices when a shrouding policy is in place for a specific event m and bookmaker i. In contrast,
the coefficient of the interaction term shows the difference between the coefficient on Ti,m and
the tax effect without shrouding. In line with previous findings that showed a strong positive
association between the effect on consumer betting prices and active shrouding policies, the
estimated tax effect is around 0.046 when a shrouding policy was in place for a specific event-
bookmaker observation. If we exclude cross-leagues, the estimated coefficients increase to 0.05,
implying a full pass-through of the tax onto consumers ( dp dt = 1). The estimated coefficients
on the interaction term are equal to -0.041 and -0.043, respectively, which implies a highly
statistically significant difference in pass-through rates of over 80%. The estimated effects are
robust to only considering agencies, for which odds data is available for all years (Table 9 in the
Appendix) or considering all sports (Table 10 in the Appendix).
Panel (a) of Figure 8 illustrates the estimation results of the event study design, considering
only treated agencies that never shroud tax surcharges (blue line) and shrouding agencies (red
line). The control group is the same for both subsample regressions. Importantly, in both
subsamples, the pre-trends show a similar pattern as the control group, suggesting that the
parallel trend assumption holds for both subsamples. Only after the tax reform estimated
treatment effects diverge between the two subsamples. While other explanations cannot be
entirely ruled out, this evidence highly suggests that shrouding policies cause differences in tax
effects.
Panel (b) shows the estimation results for specifications with leads and lags of treatment
interacted with the noShroud i,m dummy (equation 6). The coefficients are calculated such that
the red connected dots show the tax effects over time for a specific event and bookmaker with
an active shrouding policy. The blue connected dots show the dynamic tax effects for events
where agencies did not employ shrouding policy was employed. In contrast to the subsample
analysis, the estimated quarterly tax effects jump to around 0.045 directly after the tax reform
and stay pretty constant until the end of the observation period. This immediate increase
can be attributed to the fact that not all shrouding agencies immediately employ a shrouding
policy after the reform. The tax effects for “no shrouding”-events are insignificant in the first
quarterly periods after the tax reform and steadily increase until the end of the observation
period to around 0.02 in 2018, similar to the subsample analysis. The results are very similar if
we exclude cross leagues or consider all events (Figure 14 in the Appendix).
29

Table 5: Avg. effect of tax on consumer betting prices - soccer
All Leagues Excl. ”cross” leagues
Subsamples Interact. Subsamples Interact.
No shrouding Shrouding No shrouding Shrouding
(1) (2) (3) (4) (5) (6)
Tax effect on prices 0.008 ∗∗∗ 0.041∗∗∗ 0.008∗∗ 0.045∗∗∗
(0.002) (0.003) (0.002) (0.003)
Ti,m 0.046∗∗∗ 0.050∗∗∗
(0.003) (0.003)
Ti,m x noShroud i,m -0.041∗∗∗ -0.043∗∗∗
(0.002) (0.002)
Constant 0.085 ∗∗∗ 0.084∗∗∗ 0.084∗∗∗ 0.091∗∗∗ 0.091∗∗∗ 0.091∗∗∗
(0.003) (0.003) (0.003) (0.003) (0.003) (0.003)
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes Yes Yes Yes Yes
League FE Yes Yes Yes Yes Yes Yes
Observations 1,587,090 1,881,406 1,936,322 1,211,548 1,277,394 1,290,843
R2 0.728 0.767 0.779 0.737 0.757 0.761
Notes: Columns 1, 2, 4, and 5 of the table report the estimated average sports betting tax effects on
consumer betting prices for soccer events according to Eq. 3, comparing changes in prices before and
after the tax reform between German and Non-German agencies. Columns 1 and 4 only consider German
agencies that do not shroud taxes, while columns 2 and 5 only consider shrouding agencies (either policy ii
or iii). Columns 3 and 6 show the estimation results for Eq. 5. The coefficient on Ti,m can be interpreted
as the effect of the tax on betting prices when a shrouding policy is in place for a specific event m and
bookmaker i. In contrast, the coefficient of the interaction term shows the difference between the coefficient
on Ti,m and the tax effect without shrouding. Each agency-event combination (unique observation) is
equally weighted. Columns 1-3 consider all leagues, while Columns 4-6 exclude events in German leagues
for the control group and Non-German leagues for the treatment group. All estimations include time-,
agency- and league-fixed effects. Robust standard errors clustered at the agency level are reported in the
brackets. * denotes significance at the 10-%, ** at the 5-%, and *** at the 1-% level.
30

Figure 8: Pre-trends and tax effects on consumer betting prices over time for different ”shroud-
ing” policies- all agencies
(a) Subsample analysis (agency level)
(b) Interaction terms (event-agency level)
Notes: This figure shows the estimated effects and respective 95-% confidence intervals of the
German sports-betting tax on consumers’ betting prices over time. Panel (a) shows the estimates
for the event study design according to equation 4. The red estimates only consider German
agencies that employ a shrouding policy at some point, and the blue estimates only consider
German agencies that never employ a shrouding policy. The control group is the same for both
regressions. Panel (b) shows the coefficients estimating Eq 6 that interacts leads and lags of
treatment with a dummy that equals one if the event took place after the tax reform and agency
i had a NO shrouding policy in place for event m. Coefficients are transformed such that both
groups can be directly compared. All agencies are considered, N=65 (Treatment=10/Control=55).
The vertical dashed line illustrates the introduction of the tax reform. The horizontal dotted line
signifies a full pass-through of the tax on consumers.
31

6 Optimal sin taxation
The goal of this section is to derive the policy and welfare implications of the empirical results and
understand the underlying mechanism behind and effects of strategic tax shrouding. I use the
optimal sin taxation framework by O’Donoghue and Rabin (2006) and relax their assumptions
of perfect competition and fully attentive consumers to accommodate the main features of online
sports betting markets.
6.1 Optimal sin tax model with homogeneous consumers and perfect com-
petition
The main rationale behind sin taxes is that certain goods are “overconsumed” because (some)
consumers do not internalize negative externalities on one’s (future) self because of self-control
problems, e.g. due to time-inconsistent preferences (Laibson, 1997), or other frictions when
making a decision. In these cases, consumer do not optimize their own true ”experienced” utility
or welfare u with respect to this good’s consumption but base their decision on some “decision”
utility ˜u that differ from the true utility. Following the arguments for Pigouvian taxes (Pigou,
1920), taxing the consumption of sin goods can thus induce consumers to internalize negative
consumption effects and increase social welfare.
Consider a variant of the model by O’Donoghue and Rabin (2006). There is a unit mass of
consumers i ∈ [0, 1] that consume two goods: a sin good x, say sports betting, and a composite
good z. The composite good is produced with constant return to scale and supplied in a perfectly
competitive market. The price of the composite good is normalized to one. Sin good x gives
consumer i an (immediate) enjoyment from consumption vi(x) but come with (future) costs
due to potential issues related to problem gambling, ci(x). Assume following quasi-linear utility
function: ui = vi(xi) − ci(xi) + z. Here, ui refers to“long-run” utility of consumption, which
eliminates the time dimension. vi is increasing in x with decreasing marginal benefits. Potential
costs c are increasing in x with no constraints on the marginal costs beside that vxx − cxx < 0,
guaranteeing well-behaved behavior.
Suppose that consumers may not fully internalize the costs from consumption of the sin
good and discount the long-run costs of the sin good with 0 ≤ γi ≤ 1, implying that ˜ui =
vi(xi) − γici(xi) + z. Consumers are endowed with per period income W that is large relative
to the sin good consumption. The government can impose a per unit tax t on the consumption
of x remitted by firms that finances a lump sum transfer L to the consumers. The effective
tax-inclusive consumer price is p whereas the producers’ price is q = p − t. The sin good is
produced at constant marginal costs m. Assume for now that all consumers are homogeneous.
Accordingly, each consumer solves following maximization problem:
max
x,z
˜u = v(x) − γc(x) + z (7)
s.t. px + z ≤ W + L
If the market for the sin good is perfectly competitive, producer prices will equal marginal
costs (including t), such that p∗ = m+t. Accordingly, the tax will be fully passed onto consumers
32

( dp∗ dt = 1).38
Without taxes (t = 0) and no self-control problems (γ = 1) the optimal consumption bundle
(x∗, z∗) is determined by the first order conditions: vx(x∗) − cx(x∗) = m and z∗ = W − mx∗.39
This case provides the first-best solution that maximizes social welfare. Without taxes but
γ <1, consumers ignores 1 − γ of the costs. They set ˜ x∗(t) according to their decision utility,
such that: vx(˜x∗(t)) − γcx(˜x∗(t)) = m + t and z∗(t) = W + L − (m + t)˜x∗(t). This implies that
consumers overconsume the sin good if t = L = 0: ˜x∗(0) > x∗. Similar to a simple Pigouvian
tax-transfer scheme designed to correct for externalities, a tax t∗ = (1 − γ)cx(x∗) on sports
betting and a uniform transfer of the tax revenue to consumers would implement the first-best
solution, where all consumers choose ( x∗, z∗). The proof is straightforward and provided in
Appendix F.1, Lemma 1.
Suppose now that consumers underreact to taxes and misperceive the tax being equal to θt.
θ <1 can be interpreted as an exogeneous tax salience parameter similar to Chetty et al. (2009);
DellaVigna (2009). In this case consumers choose ˜x∗ θ(t) such that: vx(˜x∗ θ(t))−γcx(˜x∗ θ(t)) = m+θt
and ˜z∗ θ (t) = W +L−(m+t)˜x∗ θ(t).40 The corrective effect of the tax is attenuated and the optimal
tax rate increases. The optimal sin tax that reinstates the social optimal solution is equal to
(see Appendix F.1, Lemma 1):
t∗ θ = (1 − γ)cx(x∗) θ (8)
The sin tax is completely ineffective in correcting behavior if θ = 0. As tax revenues are
completely transferred back to consumers and profits are zero irrespective of the tax, the sin tax
is irrelevant from a social welfare perspective in this extreme case.
The optimal tax formula also applies if there is an overreaction to the tax θ > 1 and the
maximization problem of the social planner has an interior solution. In addition, all results
of the homogeneous case also hold if additional to—or instead of—internalities, sports betting
exhibits externalities to other consumers. The Pigou dollar principle still applies: A dollar of
internalities and/or externalities must be corrected with 1 θ tax dollars (Farhi and Gabaix, 2020).
The basic results hinge on the assumption that consumers are homogeneous. O’Donoghue and
Rabin (2006) study optimal sin taxation with perfectly attentive consumers that may vary in
their tastes and γ. I will focus on consumers that are heterogenous in terms of their attention
towards shrouded taxes in the next section.
6.2 Optimal sin tax model with heterogeneous consumers and tax shrouding
Now suppose that the sin good is not supplied under perfect competition but under imperfect
Bertrand-Nash price competition. The supply side of the model follows Varian’s model of sales
(1980) and shares several features with the model by Armstrong and Chen (2009) that study
38The full pass-through of the tax is the result of the constant marginal costs assumption, which implies a
perfectly elastic supply. In the standard partial equilibrium model of taxation under perfect competition, the
pass-through rate of the tax will be a function of demand and supply elasticities, where the relatively less elastic
side of the market will bear most of the tax burden (see Appendix E for details).
39Note that the optimal consumption bundle also depends on m, I simplify the notation in the interest of better
readability.
40Note that for ˜z∗ θ (t) there is no θ on the right-hand side of the equation, as consumers will spend the remaining
“true” income on the composite good. W is assumed to be large enough such that the consumers do not breach
the budget constraint for any θ and γ.
33

the optimal choice of binary product quality in the presence of inattentive consumers.
k = 1, 2, ..., Nfirms produce the sin good at the same constant marginal costs m. Firms set
a salient posted price ps k and a shrouded tax surcharge τk, which can be either zero or equal to
the unit tax t (τk ∈ {0, t}). Accordingly, the firm k’s consumer price is defined as pk = ps k + τk
and producers prices are pk − t. Supply is completely elastic.
On the demand side, suppose that only a fraction λ of consumers are attentive. They
perfectly observe all effective prices (including shrouded tax surcharges) and the shrouding
decision by firms. Buying from a shrouding firm may come with a fixed disutility s ≥ 0, which
may refer to attention or search costs, or behavioral costs related to the attempt of being ripped
off. The remaining fraction of consumers (1 − λ) are inattentive to shrouded taxes. They
perfectly observe posted prices but misperceive the shrouded tax surcharge being equal to θt
if τk = t. In the case where all consumers are entirely inattentive to shrouded taxes ( θ = 0),
consumers act on the posted price alone, i.e., they mistakenly believe that there are no tax
surcharges. Demand from inattentive consumers is split equally among firms with the lowest
posted price. Firms cannot discriminate between consumer types and set one pricing strategy
for all consumers. All demand function will further depend on competitors’ prices and shrouding
decisions.
Homogeneous (in)attention
As a benchmark consider following three boundary cases which results in some sort of marginal
cost pricing. First, without taxes both types of consumers have perfect information about
relevant prices and will simply buy from the firm with the lowest posted (i.e., effective) price.
Following a price undercutting argument ` a la Bertrand (1883), this implies a unique symmetric
equilibrium where all firms set prices equal to marginal costs m. Firm’s market shares are equal
to 1 N and profits are equal to zero independent of γ. With no self-control problems ( γ = 1), the
optimal consumption bundle ( x∗, z∗) is chosen. With self-control problems, the demand for the
sin good is higher, i.e., x will be overconsumed from a social welfare perspective.
Second, suppose all consumers are fully attentive to the tax surcharge ( λ = 1). In that case,
all firms set symmetric equilibrium prices equal to firms’ marginal costs p∗ = m+t. Sin taxes are
fully passed through onto consumer prices ( dp∗ dt = 1). All firms will split the market equally and
equlibrium profits are zero. If s >0, firms do not shroud taxes in equilibrium. The implications
of the classical corrective taxation model under perfect competition discussed above carry over
to the extended model in this case.
Third, if all consumers underreact to shrouded taxes, firms optimally shroud taxes (τk = t) in
equilibrium. As consumers are homogeneous, the Bertrand price undercutting argument applies,
and firms will set symmetric posted prices equal to m, implying zero equilibrium profits. Firms
effectively still fully pass through taxes onto consumers (through shrouded taxes); the corrective
effect of the tax is, however, attenuated by θ. The optimal sin tax results under a homogeneous
underreaction and perfectly competitive markets apply, and the optimal tax rate is given by Eq.
8.
34

Heterogeneous attention
With both types of consumers (0 < λ <1) and θ <1, there is no equilibrium in pure strategies
where all firms unshroud taxes. (Lemma 2 in Appendix F.2). This implies that tax shrouding
prevails in equilibrium with some inattentive consumers, and the sin tax is less effective, on
average, as in the base case. If s >0, there is further no symmetric pure strategy equilibrium
(Lemma 2 in Appendix F.2).
However, if N ≥ 4, a “segmented” market equilibrium exists (Lemma 3 in Appendix F.2). In
the first market segment, firms shroud taxes, set ps∗ k = m, and split the demand of all inattentive
consumers. In the second market segment, firms do not shroud taxes, ps∗ k = m + t, and sell their
products to all attentive consumers. The equilibrium profits are zero in both segments, as in the
boundary cases with homogeneous attention discussed above. 41 The tax will have a different
corrective effect in each market segment. In this case, a (consumer-)type-specific sin tax can
implement the first-best welfare optimal solution. However, type-specific tax-transfer schemes
are usually not feasible. In the remainder of this section, I thus investigate optimal sin taxation
when the government is restricted to a linear tax-transfer scheme that is homogeneous across
consumers.
Throughout the analysis, I assume equal welfare weights for all people. If t >0, θ <1 and
γ < 1, inattentive consumers consume more of the sin good than attentive consumers, even
if self-control problems are homogeneous. Thus, no linear tax-transfer scheme implements the
first-best solution from a social planner’s perspective. If the tax is set equal to t∗, attentive
consumers perfectly internalize the internalities and/or externalities but inattentive consumers
still overconsume the sin good: ˜ x∗ θ(t∗) > ˜x∗(t∗) = x∗. On the other hand, when the sin tax is
set to t∗ θ, the sin good consumption of the inattentive consumers will be optimal but attentive
consumers “underconsume” the sin good compared to the social optimum: ˜x∗ θ(t∗ θ) = x∗ > ˜x∗(t∗ θ).
These two considerations are optimally traded off by the government when setting the sin tax
rate. The optimal tax rate increases with the fraction of inattentive consumers. In the stylized
model, requiring firms to post tax-inclusive prices would eliminate differences in attention to
tax-induced price changes, implying that t∗ would effectively implement the social optimum.
I focus on the segmented market equilibrium when deriving the implications for the optimal
sin tax. In related models, there is usually also a symmetric mixed strategy equilibrium that
involves random pricing and implies positive profits for firms. Armstrong and Chen (2009) study
a similar setup where firms can “cheat” inattentive consumers by selling low-quality products.
Low quality can be interpreted as a product with shrouded attributes. While their setup assumes
uniform demand for the product and that the low-quality product is entirely worthless, the
implications of their model provide some important insights for the optimal corrective policy in
a mixed strategy equilibrium.
In the symmetric mixed strategy equilibrium, firms draw prices from a bounded probability
41Segmented market equilibria can also arise in differentiated consumer search models in the spirit of Wolinsky
(1986) where firms set prices and produce either high or low-quality products (Gamp and Kr¨ ahmer, 2022). Low
quality can be interpreted as a product with shrouded surcharges. While the equilibrium predictions are richer, the
main policy implications concerning optimal corrective taxation qualitatively still apply. In Gamp and Kr¨ ahmer
(2022), firms earn positive profits in both segments. Low-quality firms only serve inattentive consumers but earn
higher markups. High-quality firms serve both types of consumers, which implies higher market shares but lower
effective markups. The equilibrium outcomes will primarily depend on the share of inattentive consumers, the
search costs, and the degree of product heterogeneity.
35

distribution involving a cutoff price. Below the cutoff price, a firm targets inattentive consumers
by choosing a low quality and lower price. Above the price cutoff, the firm chooses high quality,
higher prices and sells to both types of consumers. In this equilibrium, firms make positive
profits, implying that the presence of inattentive consumers harms attentive consumers, in con-
trast to Gabaix and Laibson (2006). There is always a positive probability that firms choose
low quality in equilibrium as long as λ > 1. An education policy that increases the number
of attentive consumers tends to decrease the number of low-quality firms in equilibrium. How-
ever, the effects of such a policy are ambiguous as profits and aggregate consumer surplus is
non-monotonic in the share of attentive consumers. Increasing the number of firms drives firms’
profits to zero but does not prevent “cheating by firms” by firms. If low quality refers to a
product with shrouded tax surcharges, there is, thus, always a positive probability that firms
shroud taxes in equilibrium as long as λ > 1, attenuating the average corrective effect of a
sin tax. Again, requiring firms to reveal their quality, i.e., posting tax-inclusive prices, would
prevent “cheating” in equilibrium and increases total welfare.
7 Conclusion
One aspect often disregarded when designing tax policies is that firms cannot only change
prices but also decide whether to hide or shroud taxes levied on them from consumers. If
firms strategically shroud taxes, effective tax-inclusive prices may rise, but the welfare effect
of corrective taxes would be impaired as a part of the increase is not salient. In this paper,
I show that the strategic shrouding of sin taxes, which drives a wedge between posted and
effective tax-inclusive consumer prices, is widespread in online betting markets. According to
the theoretical model, the observed shrouding strategies and tax effects are only attainable if
(some) consumers misperceive and underreact to shrouded tax surcharges. Consequently, the
corrective effect of the tax is likely to be small because most of the high pass-through rates
are attributed to increases in shrouded tax surcharges. At the same time, bettors bear most
of the “true” tax burden due to higher effective prices. The best policy response depends on
the distribution of attention toward shrouded taxes, and homogeneous corrective tax-transfer
schemes are unsuccessful in restoring the welfare optimum if attention is heterogeneous. Banning
tax shrouding practices successfully restores the effectiveness of sin taxes independent of these
considerations (see section 6).
The theoretical and empirical results can be directly applied to externality correction policies,
such as carbon taxes or environmental subsidies. Similar to sin taxes, the effectiveness of these
policies depends on perceived rather than experienced changes in incentives. If consumers do not
internalize shrouded taxes or do not know about subsidies, they will underreact to those policy
incentives. However, a critical difference between taxes and subsidies is that firms have the
incentive to increase, instead of decrease, the salience of a subsidy because it makes their offers
more attractive. The motives of the government and firms align. Consequently, consumers’
limited attention to surcharges and firms’ strategic incentives to manipulate policy’s salience
provides a novel argument for why environmental subsidies can be socially preferable to taxes.
One common objection against sin taxes is their regressivity, i.e., low-income consumers tend
to bear most of their tax burden (Allcott et al., 2019a). Past studies suggest that regressivity
36

is not a major concern for (online) sports betting taxes as sports bettors, in contrast to other
forms of gambling, tend to be relatively wealthy, and income is not a predictor for excessive
gambling (Humphreys and Perez, 2012; Wicker and Soebbing, 2012; Hing et al., 2016). How-
ever, a correlation between attention and income can have significant implications depending on
the correlation’s sign. Goldin and Homonoff (2013) find that low-income consumers pay more
attention to less salient cigarette taxes. In our case, this attention gap would imply that the
negative effects of shrouding tend to fall disproportionately strong on high-income individuals,
making the sin taxes less regressive. Similarly, if attention and self-control problems are cor-
related, this can affect the policy implications. For instance, impulsive bettors are likely more
prone to self-control problems and, at the same time, less attentive to shrouded price attributes
(Hing et al., 2018). In this case, tax shrouding is even more harmful as the individuals that
would benefit from the corrective effect the most react to it the least. A thorough analysis of
these effects goes beyond the scope of this paper and provides a promising avenue for future
research.42
As predicted by the theoretical model, the tax reform has led to market segmentation between
non-shrouding and shrouding firms. I do not find significant differences between non-shrouding
and shrouding agencies before the reform. According to the model, the tax has introduced a new
dimension of product differentiation of an otherwise homogeneous good. In equilibrium, non-
shrouding firms target attentive consumers, while shrouding firms target inattentive consumers.
Following predictions from related models on binary quality choice (Armstrong and Chen, 2009;
Gamp and Kr¨ ahmer, 2022), profit-maximizing firms trade off higher market share with higher
markups. Anecdotal evidence from the annual reports of listed agencies is in line with this
conjecture. While the leading agency that did not shroud taxes was able to considerably increase
its market share in Germany to over 50% since the tax reform (Tipico, 2019), the market share,
implied by market size and revenues of the prior market leader (that chose to shroud taxes
in response to the reform) decreased over time (Bwin.party digital entertainment, 2013; GVC
Holdings, 2018).
Aggregated betting revenues in Germany strongly increased, analogous to other European
countries before and after the tax reform. Together with the observed equilibrium prices, this
development suggests a limited corrective effect of the betting tax on online sports betting
consumption. However, more granular betting revenue data within and outside the German
market is needed to make a conclusive empirical statement about the precise corrective effect on
consumption. Unfortunately, online betting markets remain very opaque, and granular revenue
data is not available. Future studies that conduct surveys with bettors about their betting
behavior and attention to the tax or structured interviews with industry experts may address
this limitation of the study.
The study examines the pass-through on the average betting prices across all outcomes of
an event. However, the setting also offers a promising natural laboratory to study the effects of
transaction taxes on asset prices and market efficiency. Betting markets on a single event can be
understood as small and complete financial markets with state-contingent claims (bets) that have
42The theoretical model assumes that self-control problems and income is homogeneous across consumers and
thus independent of attention toward shrouded taxes.O’Donoghue and Rabin (2006) provide an analysis of op-
timal sin taxes when consumers are heterogeneous in their tastes and self-control problems concerning sin good
consumption.
37

well-defined state prices (odds) and termination points (Thaler and Ziemba, 1988; Moskowitz
and Vissing-Jørgensen, 2002). Accordingly, the effect of the tax on relative betting prices in
single-event markets can have important implications for financial markets. For instance, one
may use the unique setting presented in this study to examine whether the sports betting tax
lead to less efficient betting markets.
38

References
Hunt Allcott and Dmitry Taubinsky. Evaluating behaviorally motivated policy: Experimental
evidence from the lightbulb market. American Economic Review, 105(8):2501–38, 2015.
Hunt Allcott, Benjamin B Lockwood, and Dmitry Taubinsky. Regressive sin taxes, with an
application to the optimal soda tax. The Quarterly Journal of Economics , 134(3):1557–1626,
2019a.
Hunt Allcott, Benjamin B Lockwood, and Dmitry Taubinsky. Should we tax sugar-sweetened
beverages? an overview of theory and evidence. Journal of Economic Perspectives , 33(3):
202–27, 2019b.
Simon P Anderson, Andre De Palma, and Brent Kreider. Tax incidence in differentiated product
oligopoly. Journal of Public Economics , 81(2):173–192, 2001.
Mark Armstrong and Yongmin Chen. Inattentive consumers and product quality. Journal of
the European Economic Association, 7(2-3):411–422, 2009.
Paul G Barnett, Theodore E Keeler, and Teh-Wei Hu. Oligopoly structure and the incidence of
cigarette excise taxes. Journal of Public Economics , 57(3):457–470, 1995.
Youssef Benzarti, Dorian Carloni, Jarkko Harju, and Tuomas Kosonen. What goes up may not
come down: asymmetric incidence of value-added taxes. Journal of Political Economy , 128
(12):4438–4474, 2020.
B Douglas Bernheim and Dmitry Taubinsky. Behavioral public economics. Handbook of behav-
ioral economics: Applications and Foundations 1 , 1:381–516, 2018.
Joseph Bertrand. Th´ eorie math´ ematique de la richesse sociale.Journal des Savants , 67(1883):
499–508, 1883.
Kirill Borusyak, Xavier Jaravel, and Jann Spiess. Revisiting event study designs: Robust and
efficient estimation. arXiv preprint arXiv:2108.12419 , 2022. doi: 10.48550/ARXIV.2108.
12419.
Sebastien Bradley and Naomi E Feldman. Hidden baggage: Behavioral responses to changes
in airline ticket tax disclosure. American Economic Journal: Economic Policy , 12(4):58–87,
2020.
Jennifer Brown, Tanjim Hossain, and John Morgan. Shrouded attributes and information sup-
pression: Evidence from the field. Quarterly Journal of Economics , 125(2):859–876, 05 2010.
William O Brown and Raymond D Sauer. Fundamentals or noise? evidence from the professional
basketball betting market. Journal of Finance , 48(4):1193–1209, 1993.
Jeremy I Bulow and Paul Pfleiderer. A note on the effect of cost changes on prices. Journal of
political Economy, 91(1):182–185, 1983.
39

Bundesverfassungsgericht. Urteil des ersten senats vom 28. m¨ arz 2006 - 1 bvr 1054/01 -, rn.
1-162,. 2006. https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/
DE/2006/03/rs20060328_1bvr105401.html. Last accessed August 28, 2022.
Bwin.party digital entertainment. Annual report & accounts 2012. 2013. https://
entaingroup.com/wp-content/uploads/2017/12/2012_Annual_Report.pdf. Last accessed
March 29, 2022.
Colin F Camerer. Does the basketball market believe in the hot hand? American Economic
Review, 79(5):1257–1261, 1989.
Bruce I Carlin. Strategic price complexity in retail financial markets. Journal of Financial
Economics, 91(3):278–287, 2009.
Raj Chetty, Adam Looney, and Kory Kroft. Salience and taxation: Theory and evidence.
American Economic Review, 99(4):1145–77, 2009.
Ioana Chioveanu and Jidong Zhou. Price competition with consumer confusion. Management
Science, 59(11):2450–2469, 2013.
Cl´ ement De Chaisemartin and Xavier d’Haultfoeuille. Two-way fixed effects estimators with
heterogeneous treatment effects. American Economic Review, 110(9):2964–96, 2020.
Philip DeCicca, Donald Kenkel, and Feng Liu. Who pays cigarette taxes? the impact of con-
sumer price search. Review of Economics and Statistics , 95(2):516–529, 2013.
Sofia Delipalla and Michael Keen. The comparison between ad valorem and specific taxation
under imperfect competition. Journal of Public Economics , 49(3):351–367, 1992.
Stefano DellaVigna. Psychology and economics: Evidence from the field. Journal of Economic
literature, 47(2):315–72, 2009.
Markus Dertwinkel-Kalt, Mats K¨ oster, and Matthias Sutter. To buy or not to buy? price salience
in an online shopping field experiment. European Economic Review, 130:103593, 2020.
Deutscher Sportwettenverband. Playtech und kindred verst¨ arken
deutschen sportwettenverband. 2018. https://dswv.de/
playtech-und-kindred-verstaerken-deutschen-sportwettenverband/ . Last accessed
August 28, 2022.
Joseph J Doyle and Krislert Samphantharak. $2.00 gas! studying the effects of a gas tax
moratorium. Journal of Public Economics , 92(3-4):869–884, 2008.
Glenn Ellison. A model of add-on pricing. Quarterly Journal of Economics , 120(2):585–637,
2005.
Glenn Ellison and Sara Fisher Ellison. Search, obfuscation, and price elasticities on the internet.
Econometrica, 77(2):427–452, 2009.
Glenn Ellison and Alexander Wolitzky. A search cost model of obfuscation. RAND Journal of
Economics, 43(3):417–441, 2012.
40

Joachim Englisch. Taxation of online gambling in Germany.Gaming Law Review and Economics,
17(1):20–32, 2013.
European Commission. Online gambling in the internal market - frequently asked questions.
2012a. https://ec.europa.eu/commission/presscorner/detail/en/MEMO_12_798. Last
accessed March 3, 2022.
European Commission. Commission sets out an action plan for online gambling. 2012b.
https://ec.europa.eu/commission/presscorner/detail/en/IP_12_1135. Last accessed
March 3, 2022.
European Commission. Online gambling: Commission recommends principles to ensure effective
protection of consumers. 2014. https://ec.europa.eu/commission/presscorner/detail/
en/IP_14_828. Last accessed March 3, 2022.
European Court of Justice. Judgement of the court (grand chamber) – 8 september 2010.
2010. https://curia.europa.eu/juris/liste.jsf?language=en&num=C-316/07. Last ac-
cessed August 28, 2022.
Emmanuel Farhi and Xavier Gabaix. Optimal taxation with behavioral agents. American
Economic Review, 110(1):298–336, 2020.
Naomi E. Feldman and Bradley J. Ruffle. The impact of including, adding, and subtracting a
tax on demand. American Economic Journal: Economic Policy , 7(1):95–118, 2015.
Stephen Figlewski. Subjective information and market efficiency in a betting market. Journal
of Political Economy , 87(1):75–88, 1979.
Amy Finkelstein. E-ztax: Tax salience and tax rates. The Quarterly Journal of Economics , 124
(3):969–1010, 2009.
Forbes. Where is sports betting legal? a guide to all 50 states. 2022. https://www.forbes.com/
sites/willyakowicz/2022/01/07/where-is-sports-betting-legal-america-2022/
?sh=462e796e2342. Last accessed August 28, 2022.
Xavier Gabaix and David Laibson. Shrouded attributes, consumer myopia, and information
suppression in competitive markets. Quarterly Journal of Economics , 121(2):505–540, 05
2006.
Tobias Gamp and Daniel Kr¨ ahmer. Competition in search markets with naive consumers. The
RAND Journal of Economics , 2022.
Gl¨ ucksspielaufsichtsbeh¨ orden der L¨ ander. Jahresreport 2020 der gl¨ ucksspielaufsichtsbeh¨ orden
der l¨ ander. 2021. https://innen.hessen.de/sites/innen.hessen.de/files/2021-12/
jahresreport_2020.pdf. Last accessed August 28, 2022.
Jacob Goldin and Tatiana Homonoff. Smoke gets in your eyes: Cigarette tax salience and
regressivity. American Economic Journal: Economic Policy , 5(1):302–336, 2013.
41

Andrew Goodman-Bacon. Difference-in-differences with variation in treatment timing. Journal
of Econometrics, 225(2):254–277, 2021.
Jonathan Gruber and Botond K˝ oszegi. Tax incidence when individuals are time-inconsistent:
the case of cigarette excise taxes. Journal of Public Economics , 88(9-10):1959–1987, 2004.
GVC Holdings. Annual report2017. 2018. https://entaingroup.com/wp-content/uploads/
2018/04/GVC_Annual-Report-2017.pdf. Last accessed March 29, 2022.
George H¨ aberling. Internet gambling policy in europe. In Routledge International Handbook of
Internet Gambling , pages 304–319. Routledge, 2012.
Matthew Harding, Ephraim Leibtag, and Michael F Lovenheim. The heterogeneous geographic
and socioeconomic incidence of cigarette taxes: evidence from nielsen homescan data. Amer-
ican Economic Journal: Economic Policy , 4(4):169–98, 2012.
Jarkko Harju, Tuomas Kosonen, and Oskar Nordstr¨ om Skans. Firm types, price-setting strate-
gies, and consumption-tax incidence. Journal of Public Economics , 165:48–72, 2018.
Jarkko Harju, Tuomas Kosonen, Marita Laukkanen, and Kimmo Palanne. The heterogeneous
incidence of fuel carbon taxes: Evidence from station-level data. Journal of Environmental
Economics and Management , page 102607, 2022.
Justus Haucap. Gl¨ ucksspielstaatsvertrag: Endlich reguliert.Wirtschaftsdienst, 101(8):583–583,
2021.
Paul Heidhues, Botond K˝ oszegi, and Takeshi Murooka. Inferior products and profitable decep-
tion. Review of Economic Studies , 84(1):323–356, 08 2016.
Jean Hindriks and Valerio Serse. Heterogeneity in the tax pass-through to spirit retail prices:
Evidence from belgium. Journal of Public Economics , 176:142–160, 2019.
Nerilee Hing, Alex MT Russell, Peter Vitartas, and Matthew Lamont. Demographic, behavioural
and normative risk factors for gambling problems amongst sports bettors. Journal of gambling
studies, 32(2):625–641, 2016.
Nerilee Hing, En Li, Peter Vitartas, and Alex MT Russell. On the spur of the moment: Intrinsic
predictors of impulse sports betting. Journal of Gambling Studies , 34(2):413–428, 2018.
Brett Hollenbeck and Kosuke Uetake. Taxation and market power in the legal marijuana indus-
try. The RAND Journal of Economics , 52(3):559–595, 2021.
Tanjim Hossain and John Morgan. ... plus shipping and handling: Revenue (non) equivalence
in field experiments on ebay. Advances in Economic Analysis & Policy , 5(2):1–27, 2006.
Brad R Humphreys and Levi Perez. Who bets on sports? characteristics of sports bettors and
the consequences of expanding sports betting opportunities. Studies of Applied Economics ,
30(2):579–598, 2012.
42

International Betting Integrity Association. An optimum betting market: A regulatory,
fiscal & integrity assessment. 2021. https://ibia.bet/wp-content/uploads/2021/08/
IBIA-An-Optimum-Betting-Market.pdf . Last accessed March 3, 2022.
Kristopher O Keller, Jonne Y Guyt, and Rajdeep Grewal. Soda taxes and marketing conduct.
Journal of Marketing Research , page 00222437231195551, 2023.
Donald S Kenkel. Are alcohol tax hikes fully passed through to prices? evidence from alaska.
American Economic Review, 95(2):273–277, 2005.
Wojciech Kopczuk, Justin Marion, Erich Muehlegger, and Joel Slemrod. Does tax-collection
invariance hold? evasion and the pass-through of state diesel taxes. American Economic
Journal: Economic Policy , 8(2):251–86, 2016.
Michael Kosfeld and Ulrich Sch¨ uwer. Add-on pricing in retail financial markets and the fallacies
of consumer education. Review of Finance , 21(3):1189–1216, 2017.
Laurence J Kotlikoff and Lawrence H Summers. Tax incidence. In Handbook of Public Eco-
nomics, volume 2, pages 1043–1092. Elsevier, 1987.
KPMG. Taxation of the digitalized economy. 2022. https://tax.kpmg.us/content/dam/
tax/en/pdfs/2022/digitalized-economy-taxation-developments-summary.pdf . Last
accessed March 10, 2022.
Kory Kroft, Jean-William Lalibert´ e, Ren´ e Leal Vizca ´ ıno, and Matthew Notowidigdo. Salience
and taxation with imperfect competition. NBER Working Paper , (27409), 2020.
Des Laffey, Vincent Della Sala, and Kathryn Laffey. Patriot games: The regulation of online
gambling in the european union. Journal of European Public Policy , 23(10):1425–1441, 2016.
David Laibson. Golden eggs and hyperbolic discounting. Quarterly Journal of Economics , 112:
443–477, 1997.
Steven D Levitt. Why are gambling markets organised so differently from financial markets?
Economic Journal, 114(495):223–246, 2004.
Eugenio J Miravete, Katja Seim, and Jeff Thurk. Market power and the laffer curve. Econo-
metrica, 86(5):1651–1687, 2018.
Eugenio J Miravete, Katja Seim, and Jeff Thurk. One markup to rule them all: Taxation by
liquor pricing regulation. American Economic Journal: Microeconomics, 12(1):1–41, 2020.
Maurizio Montone. Optimal pricing in the online betting market. Journal of Economic Behavior
& Organization, 186:344–363, 2021.
Tobias J Moskowitz. Asset pricing and sports betting. Journal of Finance , 76(6):3153–3209,
2021.
Tobias J Moskowitz and Annette Vissing-Jørgensen. The returns to entrepreneurial investment:
A private equity premium puzzle? American Economic Review, 92(4):745–778, 2002.
43

Ted O’Donoghue and Matthew Rabin. Optimal sin taxes. Journal of Public Economics , 90
(10-11):1825–1849, 2006.
OECD. Addressing the tax challenges of the digital economy, oecd/g20 base erosion and profit
shifting project. 2014. OECD Publishing, https://doi.org/10.1787/9789264218789-en.
Last accessed March 10, 2022.
David Paton, Donald S Siegel, and Leighton Vaughan Williams. A policy response to the e-
commerce revolution: The case of betting taxation in the uk. Economic Journal , 112(480):
296–314, 2002.
Michele Piccione and Ran Spiegler. Price competition under limited comparability. Quarterly
Journal of Economics , 127(1):97–135, 2012.
Arthur Pigou. The economics of welfare . Macmillan and Company, 1920.
Jacquelyn Pless and Arthur A van Benthem. Pass-through as a test for market power: An
application to solar subsidies. American Economic Journal: Applied Economics , 11(4):367–
401, 2019.
Luca Rebeggiani and Markus Breuer. Neue ordnung, neues gl¨ uck? Wirtschaftsdienst, 97(9):
655–663, 2017.
James M Sallee. The surprising incidence of tax credits for the toyota prius. American Economic
Journal: Economic Policy , 3(2):189–219, 2011.
Stephan Seiler, Anna Tuchman, and Song Yao. The impact of soda taxes: Pass-through, tax
avoidance, and nutritional effects. Journal of Marketing Research , 58(1):22–49, 2021.
Erik Snowberg and Justin Wolfers. Explaining the favorite–long shot bias: Is it risk-love or
misperceptions? Journal of Political Economy , 118(4):723–746, 2010.
Nicholas Stern. The effects of taxation, price control and government contracts in oligopoly and
monopolistic competition. Journal of Public Economics , 32(2):133–158, 1987.
Liyang Sun and Sarah Abraham. Estimating dynamic treatment effects in event studies with
heterogeneous treatment effects. Journal of Econometrics , 225(2):175–199, 2021.
Dmitry Taubinsky and Alex Rees-Jones. Attention variation and welfare: Theory and evidence
from a tax salience experiment. The Review of Economic Studies , 85(4):2462–2496, 2018.
Richard H Thaler and William T Ziemba. Anomalies: Parimutuel betting markets: Racetracks
and lotteries. Journal of Economic perspectives , 2(2):161–174, 1988.
Tipico. Corporate responsibility report 2018. Valetta, Malta, 2019. http://tipicolabs.de/
magazin_epaper/CR_Report_Sep2019/#6. Last accessed August 29, 2022.
US Supreme Court. Corporate responsibility report 2018. Washington, USA , 2017. https:
//www.supremecourt.gov/opinions/17pdf/16-476_dbfi.pdf. Last accessed September 29,
2022.
44

Hal R Varian. A model of sales. American Economic Review, 70(4):651–659, 1980.
E Glen Weyl and Michal Fabinger. Pass-through as an economic tool: Principles of incidence
under imperfect competition. Journal of Political Economy , 121(3):528–583, 2013.
Pamel Wicker and Brian P Soebbing. Examining participation in sports betting in germany.
The Journal of Gambling Business and Economics , 6(3):17–33, 2012.
Asher Wolinsky. True monopolistic competition as a result of imperfect information. The
Quarterly Journal of Economics , 101(3):493–511, 1986.
Linda M Woodland and Bill M Woodland. Market efficiency and the favorite-longshot bias: the
baseball betting market. Journal of Finance , 49(1):269–279, 1994.
N Zborowska, SF Kingma, and Ph Brear. Regulation and reputation: The gibraltar approach.
In The International Handbook of Internet Gambling , pages 84–100. Routledge, 2012.
45

A Institutional background - details
A.1 Regulation and of online sports betting in Europe
A coherent regulation of online sports betting has been a complicated task in nearly all European
countries. Competencies regarding taxes and regulation of online gambling activities are divided
between the European, federal, and state levels, sometimes even at the municipality level. This
diffusion of competencies further widened the existing time lag between the regulation of on-
line services and the development of (Internet) technology (Laffey et al., 2016). There is no
sector-specific EU regulation, and EU member states are, in principle, autonomous in regulat-
ing online betting services as long as they respect the fundamental freedoms established under
the Treaty on the Functioning of the European Union (TFEU) (H¨ aberling, 2012). In the early
2000s, the common response of European countries was either the prohibition of commercial
online gambling, including sports betting, or introducing very restrictive monopoly models that
only allowed one or few, primarily state-owned, operators to provide online betting services or
lotteries (H¨ aberling, 2012).43 However, these very restrictive regulatory models proved largely
unsuccessful in limiting the provision and substantial growth of commercial cross-border online
betting services in the EU (European Commission, 2012a).
The main reason behind the limited success of the sports betting bans was that most online
betting providers operate(d) in a grey market where they could meet national demands mostly
independent of national regulations. Most international agencies hold sports betting concessions
from and are domiciled in low-tax jurisdictions that are parts of the European Union, such as
Malta and Gibraltar. This offshore operation has several advantages from their perspective: i)
possibility to claim free movement of services in the EU to circumvent national and sub-federal
regulations (Article 56 - Treaty on the Functioning of the EU, TFEU); ii) prevent national
authorities to monitor and prosecute agencies; iii) minimizing the tax liability of their services,
both regarding direct and indirect taxation; iv) added credibility by holding a European license
(Zborowska et al., 2012).
The provision of cross-border online gambling services is an economic activity that falls
within the scope of the fundamental freedoms of the TFEU, which implies that the cross-border
provision of gambling services authorized in one member state is legal (European Commission,
2012b). Member states can, however, impose restrictions justified by public interest objectives,
such as consumer protection or fraud prevention. Importantly, these restrictions must be pro-
portionate, non-discriminatory, applied consistently and transparently, and suitable to achieve
the pursued objective (H¨ aberling, 2012). These strict principles triggered several judgments by
the Court of Justice of the European Union (CJEU) and actions by the European Commission
(e.g. 2014) that pushed several member states to update their national online sports betting
regulations.44 As a consequence of this pressure and the limited success of prohibition of on-
line gambling and resulting missed tax revenue from private sports betting providers, the vast
majority of European countries started to liberalize online sports betting. This process to a
practical regulatory framework often took several years, as the (admittedly special) example of
43The UK was an exception that updated its regulatory sports betting framework to the new digital era in 2001
(Paton et al., 2002).
44A list of relevant judgments can be found here: https://ec.europa.eu/growth/sectors/online-gambling/
gambling-case-law_en .
1

Germany shows, where an effective sports betting law was only passed in 2021.
A.2 Regulation in Germany
Like other European countries, Germany traditionally banned the private provision of sports
betting.45 However, the state monopoly on sports betting and gambling had already been
challenged in the course of German reunification by a debate on how to deal with four private
sports betting licenses granted under GDR law (Rebeggiani and Breuer, 2017). The new Gaming
Treaty in 2021 was the final step of unsuccessful attempts to adjust the German gambling
regulatory framework to European law and the digital era.
In 2006, the German constitutional court ruled that the state monopoly in its traditional
form was at variance with German constitutional law (Bundesverfassungsgericht, 2006), which
triggered the first Gl¨ ucksspielstaatsvertrag (interstate Gaming Treaty) in 2008 that imposed
an even stricter state monopoly (Rebeggiani and Breuer, 2017). This initial gaming treaty
was under immediate pressure from European authorities, legal scholars and the private sec-
tor. In September 2010, the European Court of Justice ruled that national monopolies are
incompatible with European law if they do not serve the pursued public interest objective, re-
quiring a more coherent gambling regulation in Germany. This ruling led to an intense debate
among German states and to the first amendment of the German interstate Gaming Treaty
(”Gl¨ ucksspiel¨ anderungsstaatsvertrag”) in July 2012. The first amendment of the interstate
Gaming Treaty was accompanied by the introduction of the new ”Federal Sports Bets Tax” (see
section 2.1).
The amendment stipulated that online sports betting remains prohibited but defined a 7-year
”experimental phase”, in which private operators could apply for a maximum of 20 state-issued
concessions.(Englisch, 2013). 46 However, several court rulings halted the process of granting
betting concessions because the process was not in compliance with the law, erroneous, and
non-transparent. (Rebeggiani and Breuer, 2017). The ratification of an additional amendment
of the Treaty failed due to resistance from Schleswig-Holstein and North Rhine-Westphalia in
March 2017. By the end of 2020, there was still no concession granted for legal sports betting in
Germany (for more details see: Gl¨ ucksspielaufsichtsbeh¨ orden der L¨ ander, 2021). The deadlock in
German online gaming regulation between 2006 and 2021 was further fueled by betting agencies
that actively challenged the Gaming treaties in court, leading to rulings that eventually delayed
an effective gambling regulation in Germany until 2021.
In sum, gambling regulation in Germany was in abeyance until the new ”Gl¨ ucksspielstaatsvertrag”
(interstate Gaming Treaty) was passed in 2021 (Haucap, 2021). The German regulatory frame-
work for online gambling and betting was characterized by a division of tax and regulatory
competencies between the federal and the state level. This division of competencies led to
opaque and ineffective legislation, which was at variance with European law (European Court
45Some exceptions existed for horse racing, where a selected group of private horse racing clubs and registered
bookmakers were allowed to organize events and provide parimutuel betting (Englisch, 2013).
46The northern state of Schleswig-Holstein (SH) initially opted out of the interstate Gaming Treaty and applied
a more liberal gambling regulation, particularly concerning online poker and casinos. By the end of December,
SH had granted more than 20 betting licenses. These liberalization efforts were only short-lasted, as in January
2013, the new government of SH reversed this decision and rejoined the interstate Gaming Treaty (Rebeggiani
and Breuer, 2017).
2

of Justice, 2010) and even German constitutional law. In this regulatory environment, betting
agencies, domiciled in liberal (primarily European) jurisdictions outside Germany where their
services were admissible, could serve the German demand for sports betting in a semi-legal and
more or less unrestricted grey market tolerated by German authorities(Rebeggiani and Breuer,
2017).47
B The difference between posted and effective betting prices
We defined τ as the difference between the tax-inclusive and posted betting prices (i.e., the
shrouded tax surcharge):
τ = pib − ˜pib = 1 ˜θib − 1 θib (9)
For the three different policies that betting agencies set, τ can be derived as follows:
i) No further deductions : τ = 0. The derivation of τ is trivial as: pib = ˜pib
ii) Deducting tax surcharge from winnings :
Using that θib = Pn s=1 1 ri,s,b and ri,s,b = ˜risb(1 − t) we can rewrite equation (4) to:
τ = 1 ˜θib − 1 Pn s=1 1 (1 − t)˜risb = 1 ˜θib − 1 − t ˜θib = t ˜θib
iii) Deducting tax surcharge from wager: Noting that ri,s,b = ˜risb (1 + t) and θib = Pn s=1 1 ri,s,b
we can rewrite equation (4) to:
τ = 1 ˜θib − 1 Pn
s=1
(1 + t)
˜risb
=

1 − 1 (1 + t)  1 ˜θib = t (1 + t)˜θib
47A statement in the 2009 annual report of the betting provider sporting betsummarizes the industry view (and
strategy) on the German gambling regulation quite fittingly: ”Furthermore, enforcement action against operators
where they actively target German residents (including through local marketing) has been curbed due to the lack
of clarity in the legal position. In our view, therefore, legislation that was intended to almost comprehensively
block online gambling has had only limited effect and the general inability of the German government to block
online gambling websites, coupled with the questionable legality of the legislation, has led to a continued supply
of online gambling services, and an absence of extra-territorial enforcement against the activity.”
3

C Appendix figures
Figure 9: Distribution of consumer betting prices
(a) All sports
 (b) Soccer games
Notes: This figures shows the distribution of betting prices and the corresponding normal distribu-
tion with the mean and standard deviation of the sample. Panel a) considers all sports, Panel (b)
only soccer games. The prices considered for the graphs are trimmed by quarter at the quarterly
1- and 99-percentiles, considering all events and all agencies. The number of bins is fixed to 40
and the first bin starts at 0.005, which includes also the smallest price. Width per bin is equal to
0.0040721.
4

Figure 10: Avg. tax-inclusive consumer betting prices of German and Non-German betting
agencies over time with data for all years
(a) All sports
 (b) Only soccer games
(c) All sports - excluding cross leagues
 (d) Only soccer games - excluding cross leagues
Notes: This figures shows the average quarterly and weekly betting prices over time for agencies that target the
German market (Treatment) and for agencies that do not target the German market (Control). Only agencies
for which odds data in all years is available are considered, N=30 (Treatment=9/Control=21). The circles
signify average weekly betting prices in each group pooled and aligned by the respective quarter. The solid line
illustrates the average quarterly betting prices. The odds considered for the graphs are trimmed by quarter at
the quarterly 1- and 99-percentiles, considering all events and all agencies. Panel (a) and (c) consider all sports
included in the data set, while Panel (b) and (d) only consider soccer events. Panel (c) and (d) excludes German
leagues for the control group and Non-German leagues for the treatment group.
5

Figure 11: Avg. tax-inclusive consumer betting prices and estimated tax effects over time -
treated agencies vs. agencies with a foreign domain
(a) Soccer games
 (b) Soccer games - excluding cross leagues
(c) Soccer games
 (d) Soccer games - excluding cross leagues
Notes: This figures shows the average quarterly and weekly betting prices for soccer events (Panel a and b)
and corresponding estimated treatment effects (Panel c and d) of the German sports-betting tax on consumers’
betting prices over time. Only agencies that target the German market (Treatment) and agencies that have a
foreign domain (Control) are considered. Unique agencies: N=32 (Treatment=10/Control=22). The vertical
lines illustrate the introduction of the tax reform. For Panel a and b, the circles signify average weekly betting
prices in each group, pooled and aligned by the respective quarter. The solid line illustrates the average quarterly
betting prices. The odds considered for the graphs in Panel a) and b) are trimmed by quarter at the quarterly
1- and 99-percentiles, considering all events and all agencies. For Panel c) and d), the shaded area shows the
95% confidence intervals of the estimated effects and the horizontal dotted line signifies a full-pass through of
the tax on consumers.
6

Figure 12: Effect of tax on consumer betting prices over time - for all sports/all agencies and
for agencies where data is available for all year
(a) All sports
 (b) All sports - excluding cross leagues
(c) Soccer games
 (d) Soccer games - excluding cross leagues
(e) All sports
 (f) All sports - excluding cross leagues
Notes: This figures shows the estimated effects and respective 95-% confidence intervals of the German sports-
betting tax on consumers’ betting prices over time. Only agencies for which odds data in all years is available are
considered, N=30 (Treatment=9/Control=21). Panel (a) and (b) consider all sports included in the data set,
while Panel (c) and (d) only consider soccer events. Panel (b) and (d) excludes German leagues for the control
group and Non-German leagues for the treatment group. The vertical dashed line illustrates the introduction of
the tax reform. The horizontal dotted line signifies a full-pass through of the tax on consumers.
7

Figure 13: Pre-trends and tax effects on consumer betting prices over time - all agencies -
trimmed sample
(a) Soccer games
 (b) Soccer games - excluding cross leagues
(c) All sports
 (d) All sports - excluding cross leagues
Notes: This figures shows the estimated effects and respective 95-% confidence intervals of the
German sports-betting tax on consumers’ betting prices over time. All agencies are considered,
N=65 (Treatment=10/Control=55). The odds considered for the graphs are trimmed by quarter
at the quarterly 1- and 99-percentiles, considering all events and all agencies. Panel (a) and (b)
consider soccer matches, while Panel (c) and (d) consider all sports events. Panel (b) and (d)
excludes German leagues for the control group and Non-German leagues for the treatment group.
The vertical dashed line illustrates the introduction of the tax reform. The horizontal dotted line
signifies a full-pass through of the tax on consumers.
8

Figure 14: Pre-trends and tax effects on consumer betting prices over time - agencies where
data is available for all year
(a) All sports
 (b) All sports - excluding cross leagues
(c) Soccer games
 (d) Soccer games - excluding cross leagues
(e) All sports
 (f) All sports - excluding cross leagues
Notes: This figures shows the estimated effects and respective 95-% confidence intervals of the German sports-
betting tax on consumers’ betting prices over time. Only agencies for which odds data in all years is available are
considered, N=30 (Treatment=9/Control=21). Panel (a) and (b) consider all sports included in the data set,
while Panel (c) and (d) only consider soccer events. Panel (b) and (d) excludes German leagues for the control
group and Non-German leagues for the treatment group. The vertical dashed line illustrates the introduction of
the tax reform. The horizontal dotted line signifies a full-pass through of the tax on consumers.
9

D Appendix tables
Table 6: List and of included competitions and number of unique matches
Betting agency Type of ”shrouding” policy Implementation month
Bet365 Deduction of winnings November 2012
Bet-at-home Deduction of wager August 2012
Betfair Sportsbook No shrouding Not applicable
Betsson Deduction of wager February 2016
Betway Deduction of winnings March 2013
Bwin Deduction of winnings August 2012
Interwetten Deduction of winnings July 2012
Sportingbet Deduction of winnings October 2012
Tipico No shrouding Not applicable
Unibet Deduction of winnings December 2012
Notes: The table lists all treated agencies and shows the respective shrouding
policy and its implementation date.
Table 7: Avg. effect of tax on consumer betting prices - all sports
All Leagues Excl. ”cross” leagues
(1) (2) (3) (4) (5) (6)
Panel A: All agencies
Tax effect on prices 0.037 ∗∗∗ 0.037∗∗∗ 0.038∗∗∗ 0.036∗∗∗ 0.035∗∗∗ 0.037∗∗∗
(0.005) (0.005) (0.005) (0.005) (0.005) (0.005)
Observations 3,057,547 3,057,547 3,057,547 2,027,511 2,027,511 2,027,511
R2 0.617 0.730 0.818 0.649 0.735 0.831
Panel B: Compl. agencies
Tax effect on prices 0.037 ∗∗∗ 0.036∗∗∗ 0.038∗∗∗ 0.036∗∗∗ 0.035∗∗∗ 0.036∗∗∗
(0.005) (0.005) (0.005) (0.005) (0.005) (0.005)
Observations 2,027,861 2,027,861 2,027,861 1,223,098 1,223,098 1,223,098
R2 0.468 0.656 0.760 0.445 0.614 0.742
Constant Yes Yes Yes Yes Yes Yes
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes No Yes Yes No
League FE No Yes No No Yes No
League-agency FE No No Yes No No Yes
Notes: This table reports the estimated average sports betting tax effects on consumer betting prices of
all sports events in the sample according to Eq. 3, comparing changes in prices before and after the tax
reform between German (treatment group) and Non-German agencies (control group). Each agency-event
combination (unique observation) is equally weighted. Columns 1-3 consider all leagues, while Columns 4-6
exclude events in German leagues for the control group and Non-German leagues for the treatment group.
All estimations include time-fixed effects, and the columns differ in the included agency and league fixed
effects. Estimations in Panel A consider observations from all agencies, and Panel B considers agencies
with observations from all years only. Robust standard errors clustered at the agency level are reported
in the brackets. * denotes significance at the 10-%, ** at the 5-% and *** at the 1-% level.
10

Table 8: Avg. effect of tax on consumer betting prices - control group with foreign country-
specific domain
All Leagues Excl. ”cross” leagues
(1) (2) (3) (4) (5) (6)
Panel A: All agencies
Tax effect on prices 0.047 ∗∗∗ 0.047∗∗∗ 0.047∗∗∗ 0.051∗∗∗ 0.051∗∗∗ 0.051∗∗∗
(0.005) (0.005) (0.005) (0.005) (0.005) (0.005)
Observations 983,713 983,713 983,713 550,380 550380 550380
R2 0.579 0.728 0.796 0.589 0.741 0.810
Panel B: Compl. agencies
Tax effect on prices 0.049 ∗∗∗ 0.050∗∗∗ 0.050∗∗∗ 0.054∗∗∗ 0.054∗∗∗ 0.054∗∗∗
(0.004) (0.004) (0.004) (0.005) (0.005) (0.005)
Observations 644,326 644,326 644,326 288,854 288,854 288,854
R2 0.554 0.711 0.746 0.582 0.743 0.761
Constant Yes Yes Yes Yes Yes Yes
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes No Yes Yes No
League FE No Yes No No Yes No
League-agency FE No No Yes No No Yes
Notes: This table reports the estimated average sports betting tax effects on consumer betting
prices of soccer events according to Eq. 3, comparing changes in prices before and after the tax
reform between German agencies (treatment group) and agencies with a foreign country-specific
domain (control group). Each agency-event combination (unique observation) is equally weighted.
Columns 1-3 consider all leagues, while Columns 4-6 exclude events in German leagues for the
control group and Non-German leagues for the treatment group. All estimations include time-
fixed effects, and the columns differ in the included agency and league fixed effects. Estimations in
Panel A consider observations from all agencies, and Panel B considers agencies with observations
from all years only. Robust standard errors clustered at the agency level are reported in the
brackets. * denotes significance at the 10-%, ** at the 5-% and *** at the 1-% level.
E Standard theory of tax pass-through and tax salience
This section presents a partial equilibrium model of taxation based on the textbook model by
Kotlikoff and Summers (1987) and the tax salience workhorse model by Chetty et al. (2009).
It derives the pass-through rates of an excise tax in this model and discusses the implications
when market competition becomes imperfect following Weyl and Fabinger (2013) and Kroft
et al. (2020).
T extbook model of taxation
Let q = p−t denote the suppliers’ price net of taxes. p is the effective tax-inclusive price faced by
consumers, and t is the per unit tax. The pass-through rate is defined as ρ = dp dt , i.e., the rate at
which consumer prices increase when the tax rises. In the standard model of taxation, based on
a simple partial equilibrium setting under perfect competition, the equilibrium condition is given
by: D(p) = S(p − t).48 In the textbook model (Kotlikoff and Summers, 1987), the economic
incidence of a tax is independent of who pays the tax (statutory incidence). Fully differentiating
the equilibrium condition with respect to t and solving for the pass-through rate gives us:
48Note that the partial equilibrium analysis presupposes that the market is small relative to the entire economy
(Kotlikoff and Summers, 1987), which applies to the market of sports betting.
11

Table 9: Avg. effect of tax on consumer betting prices - soccer - compl. agencies
All Leagues Excl. ”cross” leagues
Subsamples Interact. Subsamples Interact.
No shroud Shrouding No shroud Shrouding
(1) (2) (3) (4) (5) (6)
Tax effect on prices 0.008 ∗∗ 0.041∗∗∗ 0.008∗ 0.045∗∗∗
(0.003) (0.003) (0.003) (0.003)
Ti,m 0.046∗∗∗ 0.050∗∗∗
(0.003) (0.004)
Ti,m x noShroud i,m -0.041∗∗∗ -0.043∗∗∗
(0.002) (0.002)
Constant 0.085 ∗∗∗ 0.084∗∗∗ 0.084∗∗∗ 0.092∗∗∗ 0.092∗∗∗ 0.092∗∗∗
(0.004) (0.003) (0.003) (0.003) (0.003) (0.003)
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes Yes Yes Yes Yes
League FE Yes Yes Yes Yes Yes Yes
Observations 927,168 1,236,292 1,276,400 698,912 768,145 778,207
R2 0.577 0.713 0.741 0.579 0.668 0.681
Notes: This table reports the estimated average sports betting tax effects on consumer betting
prices for soccer events according to Eq. 3, comparing changes in prices before and after the
tax reform between German and Non-German agencies. Columns 3 and 6 only consider German
agencies that do not shroud taxes. Likewise, columns 1 and 4 (2 and 5) only consider agencies that
deduct a 5% tax surcharge from the advertised winnings (from the advertised wager). Each agency-
event combination (unique observation) is equally weighted. Columns 1-3 consider all leagues, while
Columns 4-6 exclude events in German leagues for the control group and Non-German leagues for
the treatment group. Only agencies for which odds data in all years is available are considered.
All estimations include time-, agency- and league-fixed effects. Estimations in Panel A consider
observations from soccer matches, and Panel B considers observations from all sports. Robust
standard errors clustered at the agency level are reported in the brackets. * denotes significance at
the 10-%, ** at the 5-%, and *** at the 1-% level.
ρ =
δS
δp δS
δp − δD δp  = 1 1 + ηD ηS  ,
where ηD = − δD δp p D(p) is the elasticity of demand and ηS = δS δp p S(p−t) is the elasticity of supply.
Accordingly, the pass-through rate ρ only depends on the supply and demand elasticities. The
pass-through is higher when demand is less elastic relative to supply. A full-pass through (ρ = 1),
i.e., the demand side of the market bears the entire burden of the tax, implies that either supply
is perfectly elastic or demand is perfectly inelastic. The total burden of the tax is shared between
consumers and suppliers (0 ≤ ρ ≤ 1), i.e., there is no ”over-shifting” of the tax onto consumers.
If competition is imperfect, ”over-shifting” of a tax is possible in equilibrium as the convexity
of the demand and supply curves becomes important for the pass-through of a tax. Suppose a
monopolist who chooses quantityw to maximize following profit function: Π = (p(w)−t)w−c(w),
where p(w) is the inverse demand and c(w) the monopolist’s cost function. In such a setting,
the pass-through of a tax is given by (Weyl and Fabinger, 2013):
ρ = 1
1 + ηD − 1 ηS + 1 ηms
 ,
12

Table 10: Avg. effect of tax on consumer betting prices - all sports
All Leagues Excl. ”cross” leagues
Subsamples Interact. Subsamples Interact.
No shroud Shrouding No shroud Shrouding
(1) (2) (3) (4) (5) (6)
Tax effect on prices 0.002 0.041 ∗∗∗ 0.001 0.040 ∗∗∗
(0.002) (0.003) (0.002) (0.003)
Ti,m 0.046∗∗∗ 0.044∗∗∗
(0.002) (0.002)
Ti,m x noShroud i,m -0.045∗∗∗ -0.042∗∗∗
(0.001) (0.001)
Constant 0.084 ∗∗∗ 0.079∗∗∗ 0.081∗∗∗ 0.088∗∗∗ 0.088∗∗∗ 0.088∗∗∗
(0.003) (0.003) (0.003) (0.003) (0.003) (0.003)
Time FE Yes Yes Yes Yes Yes Yes
Agency FE Yes Yes Yes Yes Yes Yes
League FE Yes Yes Yes Yes Yes Yes
Observations 2,466,796 2,959,638 3,057,547 1,901,791 2,006,335 2,027,511
R2 0.703 0.744 0.755 0.713 0.740 0.742
Notes: This table reports the estimated average sports betting tax effects on consumer betting prices
according to Eq. 3, comparing changes in prices before and after the tax reform between German
and Non-German agencies. Columns 3 and 6 only consider German agencies that do not shroud
taxes. Likewise, columns 1 and 4 (2 and 5) only consider agencies that deduct a 5% tax surcharge
from the advertised winnings (from the advertised wager). Each agency-event combination (unique
observation) is equally weighted. Columns 1-3 consider all leagues, while Columns 4-6 exclude
events in German leagues for the control group and Non-German leagues for the treatment group.
All estimations include time-, agency- and league-fixed effects. Estimations in Panel A consider
observations from soccer matches, and Panel B considers observations from all sports. Robust
standard errors clustered at the agency level are reported in the brackets. * denotes significance at
the 10-%, ** at the 5-%, and *** at the 1-% level.
where ms = − δp(w) δw w is the negative of the marginal consumer surplus and ηms = ms δms δw w is the elasticity of the inverse marginal surplus function. Consequently, the smaller ηms, which
can be understood as the curvature (of the logarithm) of demand (Weyl and Fabinger, 2013),
the higher the pass-through onto consumers ceteris paribus. Pass-through is larger than one
if and only if ηms is negative (Bulow and Pfleiderer, 1983), i.e. demand is very convex (Pless
and van Benthem, 2019). This result in monopolies carries over to oligopolistic competition
models, with the difference that the degree of market competition and market power becomes
an additional determining factor for pass-through rates (see Weyl and Fabinger, 2013, for a
thorough discussion). In general, the pass-through of taxes is higher when markets are less
competitive and vice versa. This connection to market competition and market power has
important implications not only for questions in public finance but also for various topics in
industrial organization (Pless and van Benthem, 2019; Miravete et al., 2020). For instance,
over-shifting of taxes can be used as a test for market power in different markets (Pless and van
Benthem, 2019).
T ax salience
The standard theory of taxation assumes that consumers are perfectly informed about taxes
and that they optimize fully with respect to tax-inclusive effective prices. The tax (surcharge)
elasticity is assumed to be equivalent to the elasticity with respect to the (posted) price. Thus,
the tax incidence in the standard model, both under perfect and imperfect competition, is
13

independent of whether consumer price changes are due to changes in the base price or the
tax surcharge. Numerous studies suggest that this assumption is often violated and that the
incidence also depends on the salience of a tax or the way taxes are presented (e.g. Chetty et al.,
2009). Suppose consumers are subject to limited attention and the tax surcharge is not fully
salient. In that case, consumers may react differently to changes in displayed prices compared to
changes in the tax surcharge. Consequently, the tax incidence and theoretical welfare implication
of the tax may change.
In relation to the ”shrouding” policies by betting agencies presented in section 2.2, one
can decompose effective consumer prices in a tax surcharge set by suppliers, τ , and advertised
consumer prices, ˜p: p = ˜p + τ . Accordingly, supplier prices can be rewritten to: q = ˜p − t + τ .
For the sake of simplicity, assume for now that the tax surcharge is always equal to the tax
(τ = t), implying q = ˜p and p = ˜p + t = q + t.
Following the tax salience literature (Chetty et al., 2009), I assume that the consumers only
perceive a fraction 0 ≤ ψ of the actual tax surcharge (τ = t). In contrast to the theoretical model
in Section 6, I follow the tax salience literature here and assume that the salience parameter
is exogenously given and not subject to strategic ”shrouding” considerations by firms. The
perceived price from the consumers’ perspective is thus given by: pψ = q + ψt. ψ defines the
extent of underreaction to the tax, which can be interpreted as the degree of tax salience or
inattention. As in the model of Chetty et al. (2009), ψ is determined the ratio of the tax (ηD,pψ|t)
and price elasticity ( ηD,pψ|q). The equilibrium condition is given by D(q + ψt) = S(q). By the
implicit function theorem, we can derive the following incidence on producers:
dq
dt =
δD
δpψ|t δS
δq − δD δpψ|q  =
ψ δD δpψ|q δS
δq − δD δpψ|q  = ψηD,pψ|q p q ηS,q + ηD,pψ|q 
Accordingly, the incidence on consumers is equal to:
dp
dt = 1 + dq dt =
 p
q ηS,q + (1 − ψ)ηD,pψ|q

 p
q ηS,q + ηD,pψ|q

Consequently, the pass-through of a tax is determined not only by the supply and demand
elasticities but also by the salience parameter ψ. The higher the salience of a tax, the lower
the incidence on consumers. If the consumers are entirely inattentive to the tax ( ψ = 0), the
incidence falls completely on consumers. We are back to the standard model if the tax is fully
salient (ψ = 1).
Bradley and Feldman (2020) derives the tax incidence under tax salience in a monopoly and
Kroft et al. (2020) generalizes the tax salience model to imperfect competition models along
the lines of Weyl and Fabinger (2013). Under imperfect competition, tax salience’s effect on
pass-through rates depends on the market structure and the curvature of demand. In special
cases, higher tax salience can even increase the incidence on consumers.
14

F Lemmas and Proofs
F.1 Perfect competition
Lemma 1. Suppose γ <1 and the homogeneous consumers optimally chooses ˜x∗(t) according
to her decision utility Eq. 7. Then t∗ = (1 − γ)cx(x∗) θ financing a uniform lump sum transfer
W ∗ back to the consumers would implement the first-best solution (x∗, z∗). θ = 1 represents the
standard case with no underreaction.
Proof. ˜x∗(t) satisfies vx(˜x∗(t)) − γcx(˜x∗(t)) = m + θt. t∗ = (1−γ)cx(x∗) θ implies, according to
the first-order condition, that vx(˜x∗(t)) − γcx(˜x∗(t)) = m + θ(1−γ)cx(x∗) θ , which can be rewritten
to vx(˜x∗(t)) − cx(x∗) − m = γ(cx(˜x∗(t))cx(x∗)) and is satisfied if and only if ˜ x∗(t) = x∗ and
consequently ˜z∗(t) = z∗
F.2 Imperfect competition
Lemma 2. In the case with both types of consumers ( 0 < λ < 1) and θ < 1, there is no
pure strategy equilibrium where no firm shrouds. If s >0, there is no symmetric pure strategy
equilibrium.
Proof. If all firms do not shroud taxes ( τk = 0), Bertrand competition implies p∗ k = ps k = m + t.
In this case, a firm can profitably deviate by shrouding taxes τk = t and setting a slightly lower
posted price, implying that the firm serves all inattentive consumers for a profit because of
underreaction to the tax ( θ <1). Suppose all firms shroud taxes τk = t and s >0. Bertrand
competition implies that posted prices will equal m and firms’ profits are again equal to zero.
In that case, a firm can make positive profits by unshrouding taxes and serving all attentive
consumers’ at higher than marginal cost prices if s >0.
Lemma 3. If N ≥ 4, there is an asymmetric equilibrium in pure strategies with two market
segments: i) at least two firms shroud taxes, choose {ps k = m, τk = t} and serve all inattentive
consumer; and ii) at least two firms do not shroud taxes, choose {ps k = m + t, τk = 0} and serve
all attentive consumers.
Proof. The equilibrium outcomes and prices in each market segment are equivalent to the bound-
ary cases discussed above. The shrouding segment will only be populated by inattentive con-
sumers and the non-shrouding segment will only be populated by attentive consumers. According
to Bertrand competition, we have marginal cost pricing in both segments and profits are equal
to zero in both segments, implying that no firm can profitably deviate.
15
