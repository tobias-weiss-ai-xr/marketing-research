---
title: 'Design Information Disclosure under Bidder Heterogeneity in Online Advertising Auctions: Implications
  of Bid-Adherence Behavior'
url: https://arxiv.org/abs/2410.05535
category: consumer-behavior
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Zhu Mingxi
- Song Michelle
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.05535
pages: 47
chars: 90915
fetched_at: '2026-11-08T13:05:51+00:00'
kb_version: 1
---

# Design Information Disclosure under Bidder Heterogeneity in Online Advertising Auctions: Implications of Bid-Adherence Behavior

Design Information Disclosure under Bidder
Heterogeneity in Online Advertising Auctions:
Implications of Bid-Adherence Behavior
Mingxi Zhu
Scheller College of Business, Georgia Institute of Technology, Atlanta, GA 30332, mingxi.zhu@scheller.gatech.edu
Michelle Song
Google, 1600 Amphitheatre Parkway, Mountain View, California 94043, yingze@stanford.edu
Bidding is a fundamental aspect of search advertising today. It is less commonly recognized that bidders
in online advertising differ both in their valuations and in their bidding strategies. Fortunately, disclosing
bid information not only uncovers the heterogeneity in valuations and strategies among bidders, but also
allows the platform to customize its information disclosure policies to achieve various objectives, such as
enhancing consumer surplus, or increasing platform revenue. We analyzed data from a platform that imple-
mented a system for bid recommendations based on disclosing historical bids. Our findings highlight the
diversity in bidding strategies among advertisers: some directly adhere to the platform’s disclosed historical
bid information, while others construct their own unique bids that diverge from the platform’s revealed data.
This underscores the importance of designing information disclosure in online ad marketplaces in response
to bidder diversity. We developed an equilibrium model for the Generalized Second Price (GSP) auction
and demonstrated that adhering to any bid recommendations with a positive probability is theoretically
suboptimal. We then distinguished advertisers into categories of bid-adhering and bid-constructing bidders.
We developed a novel structural model for self-bidding in GSP auctions to identify the private valuations of
heterogeneous advertisers. This model facilitates a counterfactual analysis to assess the impact of varying
levels of information disclosure on the market. Both theoretical and empirical evidence indicate that a mod-
erate increase in information disclosure significantly enhances platform revenue and overall market efficiency.
Identifying the diversity in bidder valuations and strategies is essential for online advertising platforms. By
carefully designing information disclosure policies, platforms can not only identify heterogeneity among bid-
ders to better address diverse bidder needs, but also efficiently achieve their managerial objectives through
costless information disclosure.
Key words: Online Auctions; Structural Models; Information Disclosure; Valuation Identification
1
arXiv:2410.05535v1  [econ.GN]  7 Oct 2024

2 Zhu and Song:Information Disclosure in Auctions
1. Introduction
Search advertising is a significant component of online advertising, with its revenue in the United
States being projected to reach US $ 132 billion dollars in 2024 (Statista (2024)). Major platforms
such as Google and Yahoo utilize the complicated Generalized Second Price (GSP) auction system.
This system demands expertise in quality scores, bid distributions, and click-through rates at
various positions – knowledge often inaccessible to small business owners with limited resources.
Such complexity not only highlights the challenges faced by advertisers, but also underscores the
need for platforms to provide information and strategies that are more accessible to less experienced
bidders.
To address the challenges faced by individual advertisers in the bidding process, advertising
platforms have introduced several strategies to enhance understanding of GSP bidding system
for bidders. One widely adopted strategy is auto-bidding. Auto-bidding allows advertisers to set
their budgets, maximum bid limits, and targets for impressions, with the platform serving as a
consumer agent. While this mechanism supports less experienced advertisers, as bidders do not
have control over their own bids under auto-bidding system, it raises issues related to fairness and
transparency (Akbarpour and Li (2018), Southern (2023)). This paper, on the other hand, shifts
focus to another important aspect of digital advertising strategy: the role of information disclosure
in self-bidding environments, a practice once adopted by Google and Yahoo, and currently in used
by the platform we collaborated in this study. Self-bidding, empowered by information disclosure,
allows advertisers to make informed decision and manually set their own bids, which enhances the
overall transparency of system. Although analytical models suggest that platform can enhance its
revenue through information disclosure (Amaldoss et al. (2015)), empirical evidence supporting
the efficacy of these strategies is scant, primarily due to the lack of quasi-experimental data in
self-bidding environments.
This paper examines how information disclosure affects advertiser behavior and market equilib-
rium. We address key questions: How does information release impact market outcomes? How do

Zhu and Song:Information Disclosure in Auctions 3
advertisers respond differently to disclosed information? How can disclosure strategies be improved
on advertising platforms? To study these issues, we collaborate with a Yelp-like lifestyle service
platform in China, which provides bid recommendations to wedding service advertisers in one city
but not others. This quasi-experimental setup enables us to analyze the effects of information
disclosure on advertising auctions, market outcomes, and advertiser behaviors.
In our paper, we identify a subset of bidders in GSP auctions who deviate from equilibrium
bids by following the platform’s recommendations, which we show to be suboptimal. Detecting
such behavior in real-world settings has been difficult due to the lack of quasi-experimental data.
We classify these bidders as bid-adhering and those who create their own bids as bid-constructing.
To analyze the impact on market welfare, we develop a novel structural model that identifies the
private values of bid-constructing bidders and estimates value bounds for bid-adhering bidders.
Finally, our counterfactual analysis shows that the platform can influence surplus outcomes by
adjusting the level of information disclosure.
This article contributes to the literature on information disclosure by providing empirical, theo-
retical, methodological, and policy insights.
Empirically, we document varied advertiser responses to bid recommendations in the GSP auc-
tion, providing the first empirical evidence that some advertisers follow these recommendations
even when it is suboptimal to do so. This underscores the critical impact of information disclosure
policy on market dynamics through affecting heterogeneous groups of advertisers.
Theoretically, we prove that bid-adhering bidders do not maximize their expected surplus by
following bid recommendations. This suggests that the bid-adhering bidders are adopting different
strategies from the bid-constructing ones, highlighting the bidder diversity in bidding strategies
under information disclosure.
Methodologically, we develop a novel approach for valuation identification for GSP auctions,
expanding on methods previously limited to first-price auctions (Guerre et al. (2000)). Our method-
ology differs from other studies by not relying heavily on assumptions about the specific bidding

4 Zhu and Song:Information Disclosure in Auctions
strategies of different bidder groups in equilibrium. This distinguishes it from approaches focused
on valuation identification for asymmetric bidding strategies in auctions (e.g., Krasnokutskaya
(2011), Horta¸ csu and Puller (2008), Gayle and Richard (2008)). Such methodology could be readily
adopted in other GSP auctions.
On a policy level, this paper evaluates the impact of information disclosure on advertising plat-
forms with diverse advertisers. The findings highlight the need to consider the varied responses of
bidders when designing information-disclosure policies for online advertising. We demonstrate that
through designing information disclosure, the platform can significantly enhance both ads revenue
and market efficiency.
The paper is organized as follows: Section 2 reviews the related literature. Section 3 provides
the empirical background and details the information disclosure event. Section 4 presents evidence
of advertisers’ varied responses to information disclosure and discusses the suboptimality of bid-
adhering strategies. Section 5 introduces our empirical model for GSP auctions, including valuation
identification and estimation results. Section 6 conducts a counterfactual analysis on how changes in
information disclosure affect market outcomes. Section 7 concludes with a summary and suggestions
for future research.
2. Literature Review
Our work relates to several streams of literature: the impact of information disclosure on market
outcomes, GSP auctions for online advertising, empirical and theoretical studies of online advertis-
ing, the interaction between human behavior and platform policies, and methodologies for valuation
estimation. We review each of these areas separately below.
Impact of Information Disclosure on Market Outcomes : This study contributes to the
literature on the impact of information disclosure on market outcomes. In the supply chain context,
the effects of information sharing vary: Chu et al. (2017) and Cui and Shin (2018) find that, under
certain conditions, carefully managed information sharing can benefit supply chain participants,
while Shamir and Shin (2018) and Lu and Tomlin (2023) show that accurate information sharing

Zhu and Song:Information Disclosure in Auctions 5
is not always beneficial and may even harm participants. In crowdfunding platforms, Chakraborty
and Swinney (2021) demonstrates through a game-theoretic model that well-designed information
signals can enhance platform performance. In online matching platforms, Chen et al. (2024) finds
that information signaling improves matchmaking by dynamically balancing supply and demand.
In auctions, Tadelis and Zettelmeyer (2015) shows that in wholesale automobile auctions, providing
quality information enhances the match between dealers and cars boosts auction revenue. In our
study, we find that information disclosure enhances both platform revenue and overall surplus in
online advertising markets by encouraging bid-adhering bidders to bid more effectively.
GSP Auctions: Since Google introduced the GSP auction in 2002, it has been widely studied
in the context of search advertising. Edelman et al. (2007) and Varian (2007) develop the envy-
free equilibrium model, which minimizes platform revenue but maximizes advertiser surplus under
complete information. Athey and Nekipelov (2010) further extends this model by incorporating
dynamics more representative of real-world GSP auctions. While these studies assume rational,
Bayesian utility-maximizing bidders, our work identifies bid-adhering behavior in a subgroup of
bidders that cannot be explained under this assumption. This highlights the need for a new empir-
ical model for valuation identification in online search advertising with heterogeneous bidders.
Empirical and Theoretical Studies of Online Advertising:, Choi et al. (2020) and Agrawal
et al. (2020) provide comprehensive literature reviews and commentaries on online and digital
advertising markets. Empirically, Jerath et al. (2011) shows that under a pay-per-click mecha-
nism in GSP auctions, less reputable firms have strong incentives to bid aggressively. Similarly,
Narayanan and Kalyanam (2015) finds that position effects are more pronounced for smaller adver-
tisers and when consumers are unfamiliar with the advertiser’s keyword. Other studies, such as
Ghose and Yang (2009), Zhang and Feng (2011), Yao and Mela (2011), and Agarwal et al. (2011),
focus on consumer behavior and its impact on advertisers’ strategies. Theoretically, a stream of
work focuses on providing theories for auto-bidding environment (Balseiro and Gur (2019)). In
platform display decisions, Najafi-Asadolahi and Fridgeirsdottir (2014) and Fridgeirsdottir and

6 Zhu and Song:Information Disclosure in Auctions
Najafi-Asadolahi (2018) formulate the platform display problem in online advertising as a queueing
system and design the optimal pricing schemes on both cost-per-click and cost-per-impression. Our
work extends this stream of literature by incorporating information disclosure into the analysis,
where we explore heterogeneous responses from bidders under such information disclosure.
Interaction between Human Behavior and Platform Policies: This paper contributes to
the literature on the interaction between market participants’ behaviors and platform mechanisms.
In auction platforms, participant behaviors such as ”sniping” in eBay auctions (Ockenfels and Roth
(2006), Roth and Ockenfels (2002), Bajari and Horta¸ csu (2003), Barbaro and Bracht (2004)) and
inefficient bidding in electricity auctions (Horta¸ csu and Puller (2008)) have been well-documented.
Horta¸ csu et al. (2019) studies how heterogeneity in firms sophistication level impact electricity
market outcomes. Caro and de Tejada Cuenca (2023) focuses on price-adhering behavior in deci-
sion support systems and identifies factors contributing to non-adherence. In the online real estate
market, Fu et al. (2022) examines how information disclosure, such as platform home value esti-
mates, influences human decisions and market outcomes. Our study identifies a new non-strategic
behavior—adherence to bid recommendations—based on empirical evidence from real-world set-
tings. We analyze the impact of this behavior on market outcomes and propose policy designs to
improve revenue and social surplus.
Methodology for V aluation Estimation: This paper also contributes to the methodologi-
cal literature on valuation estimation in online platforms. Early works on online auctions, such
as Donald and Paarsch (1993), Donald and Paarsch (1996), and Laffont et al. (1995), focus on
parametric identification of bidders’ private values in first-price auctions with symmetric bidders.
Guerre et al. (2000) (GPV hereafter) introduces a computationally feasible method for first-price
auctions under the symmetric independent private value paradigm. Campo et al. (2003) extends
this to asymmetric bidders with affiliated private values. In procurement auctions, Kim et al. (2014)
develops a structural estimation approach to estimate bidders’ private costs using bidding data
from combinatorial auctions, building on the methods in Cantillon et al. (2006) based on GPV.

Zhu and Song:Information Disclosure in Auctions 7
Our paper extends GPV methods for online Generalized Second Price (GSP) auctions, assum-
ing a subset of bidders follows equilibrium strategies. Similar to GPV, our model infers bidder
values from empirical bid distributions by calculating a positive markup term in GSP auctions.
Additionally, many empirical studies test the Linkage Principle (Milgrom and Weber (1982)) in
auctions, such as De Silva et al. (2008), Cho et al. (2014), and Gupta et al. (2019). However, in
our case, there is no common value component in the information structure. In online retailing,
Jiang et al. (2024) provides a nonparametric estimation method to detect consumer heterogeneity
through transaction data. In our work, we use bid data to confirm heterogeneity in both bidder
valuations and bidding strategies.
3. Data and Background
3.1. The Ad Platform and the Generalized Second Price Auction
We partnered with a leading online platform for discovering lifestyle services in China. The plat-
form is similar to Yelp and Groupon in North America. As of 2023, it has 677 million annual
transacting users and 9.3 million annual active merchants. The advertising platform manages spon-
sored search ads for various lifestyle services such as restaurants, takeouts, travel, and wedding
services. Our research focuses on the wedding service category, where the platform has introduced
bid recommendations as a means of disclosing information to advertisers. Figure 1 displays the
search result for wedding service providers on its mobile App. The top five slots on the search
results page display advertisements marked with an “ad” logo on the merchant’s picture, which
may be easily overlooked unless consumers closely inspect the page. Alongside these ads, the search
results page also provides additional information about each merchant, including their title, review
stars, number of reviews, average price per person, and location.
On this platform, the first five positions are reserved for search advertisements. Subsequent
advertising results are mixed with organic search results, appearing every four spots starting from
the ninth position (e.g., the sixth ad appears in the ninth slot). Advertisers bid for desired time slots
to display their ads at the top of the page or interspersed with organic search results. Advertisers
bid on their targeted time periods to display their ads for sponsored search. They submit a single

8 Zhu and Song:Information Disclosure in Auctions
Figure 1 Wedding Service Category Search Result App Layout
bid that applies to all positions, and the ad platform then ranks them for each search query based
on a combination of their bids and quality scores. Specifically, when a consumer searches for a
relevant keyword, the platform calculates the advertiser’s quality score for that specific consumer
query, and ranks the advertisement based on a rank score, which is the product of the quality score
and the submitted bid.
Like other sponsored search platforms, this ad platform operates using the GSP auction model
(Edelman et al. (2007)). Each consumer search initiates an auction, where the platform identifies
matching advertisers, retrieves their current bids b, and assigns a quality score q for that specific
consumer search query. Advertisers are ranked by a rank score r = q × b. If advertiser i has the kth
highest rank score, she occupies slot k. The pay-per-click price for ad slot k to advertiser i, pi,k is
determined by dividing the k + 1th highest rank score rk+1 by the advertiser i ’s quality score qi,
pi,k =
rk+1
qi . If the number of clicks (or in other words, the Click Through Rate, CTR) for position
k is αk, the advertiser i’s total payment for ad slot k is αk × pi,k =
αkrk+1
qi .
3.2. Information Disclosure in Online Advertising Auctions
The ad platform initially launched bid recommendations as a means of information disclosure
for wedding service advertisers in Xi’an, China, on August 13 th, 2019, without extending this to

Zhu and Song:Information Disclosure in Auctions 9
other cities. Subsequently, on October 10 th, 2019, it expanded these recommendations nationwide.
For our analysis, we selected Chengdu as a control city to assess the impact of these information
disclosures in Xi’an using the difference-in-differences method. Chengdu was selected based on a
weighted comparison of average bid, cost-per-click (CPC), number of ads, and advertising revenue
during July 2019, a month before the policy change. Among 145 cities, Chengdu was the most
similar city to Xi’an in these metrics. A robustness check with Nanjing, the second-best match,
confirms that our findings are consistently valid.
The advertising platform updates bid recommendations daily, based on yesterday’s second to
fourth highest rank scores adjusted by each advertiser’s simulated quality score, following a method-
ology similar to Google’s first page bid estimates strategy. For instance, the bid recommendation
for the first slot for advertiser i, denoted as si,1, is calculated by dividing yesterday’s second-highest
rank score r2 by the quality score qi of advertiser i (si,1 = r2 qi ). Intuitively, si,1 represents the min-
imum bid required for advertiser i to secure slot 1, assuming all other bids remain as yesterday,
and quality scores remain as simulated.
Regarding the quality score, since the actual score is computed for each consumer query, the
platform needs to simulate the quality score qi for each advertiser i when constructing bid recom-
mendations. Specifically, the platform simulates a few consumers from various locations in the city,
predicts the quality scores qi using a machine learning algorithm, and averages all the predicted
quality scores to obtain an estimate of advertiser j’s quality score used in the bid recommendation.
Advertisers receive only the bid recommendations, not the detailed historical bid or quality score
data.
Considering that bid recommendations utilize all ex-ante information, they cannot guarantee
100% success in securing the top three positions when the advertiser chooses to adhere to the
recommendations. This is because the bidding environment, including bids from other advertisers,
consumer search queries, and quality scores, is constantly changing. It is important to note that
the platform publicly discloses this mechanism, and all advertisers are fully aware of how the bid

10 Zhu and Song:Information Disclosure in Auctions
recommendations are constructed. This transparency makes it common knowledge that following
the bid recommendations for a specific position does not guarantee securing that position in the
actual auction.
Figure 2 displays the advertiser’s bidding interface. “RP” stands for the reserved price. Below
the bid submission area, advertisers can view the current day’s bid recommendations for the first,
second, and third positions. Beneath these recommendations, there is a button labeled “Use This
Price”. When clicked, this button automatically sets the advertiser’s bid to the selected recom-
mendation.
Figure 2 Advertiser’s Bidding Interface
3.3. Data
The dataset spans from July 13th to October 10th, 2019. We analyze data from 30 days prior to the
introduction of bid recommendations on August 13th, 2019, and 59 days following the introduction.
There are two primary datasets. The first dataset includes advertisers’ performance level data, such
as average daily Cost Per Click (CPC, in RMB), total daily number of clicks or Click Through Rate
(CTR), the average quality score (Avg qs), and the average displayed position (Avg pos, indexed
from 1). The second dataset focuses on bid-change event, and contains fewer observations as it
only includes the treated city post-intervention data. It records advertisers’ activities when they
log into their personal ad accounts, including any bid changes during the login, the original bid,
the new bid, and the current displayed bid recommendations for the top three positions. Table 1
provides summary statistics for these datasets, which will be used in our analysis. The CPC, bids
and recommendations are in unit of RMB. Additionally, we have access to the advertiser review
characteristics, including total number of reviews, and the good review ratio.

Zhu and Song:Information Disclosure in Auctions 11
Advertiser’s Performance Level Data Bid-change Event Level Data
N Mean St. dev. Min. Max. N Mean St. dev. Min. Max.
CPC 73271 3.97 5.29 0.03 116.63 Bids 3532 22.62 21.16 1.00 99.00
CTR 73271 75.88 10.33 54.17 102.69 s1 3532 54.62 32.46 2.79 99.00
Avg qs 73271 0.12 0.05 0.02 0.47 s2 3532 41.87 26.21 2.11 99.00
Avg pos 73271 35.67 28.29 1.04 455.48 s3 3532 33.50 22.15 1.00 99.00
Table 1 Summary Statistics Table
4. Descriptive Evidence
4.1. Documentation of Theoretically Sub-Optimal Bidding Pattern
On August 13 th, 2019, the ad platform introduced bid recommendations for the top three ad
positions to advertisers in the wedding service category in Xi’an. Figure 3 illustrates the distribution
of bi,t − si,k,t, where i indexes the advertiser, t indexes the bid change occasion, and k indexes ad
positions. Here, bi,t represents the bid submitted by advertiseri at time t, and si,k,t is the current kth
position bid recommendation for advertiser i at time t. Figure 3 illustrates the difference between
each advertiser’s submitted bid bi,t and the three personalized bid recommendations si,k,t for the
top 3 positions, adjusted by quality scores, at each bid change occasion. The clustering around zero
in Figure 3 shows that advertisers frequently place bids exactly as recommended. In contrast, no
similar pattern is observed in Chengdu, where we constructed pseudo-bid recommendations and
compared them with advertisers’ bids.
From Figure 3, we observe bid-adherence behavior under information disclosure, where some
bidders directly follow the platform’s recommended bids instead of constructing their own. The
following theorem demonstrates that under mild assumptions, the strategy of following bid recom-
mendation for any fixed position k with strictly positive probability can not be rationalized.
Theorem 1. Under Assumption 4 (as detailed in Online Appendix 8.1), if other bidders adhere
to the bid recommendation for any fixed position k, then any strategy that involves bidder i following
the bid recommendation si,k for position k with strictly positive probability is not a best-response
strategy.

12 Zhu and Song:Information Disclosure in Auctions
Figure 3 Bidding Pattern Under Information Disclosure
The proof of Theorem 1 is provided in Online Appendix 8.1. And the intuition behind Theorem
1 is that if the bidder is a Bayesian utility maximizer, she must submit a unique bid that optimizes
her expected payoff, taking into account the bid distributions and quality score distributions of
other bidders. Hence, the probability that this unique bid precisely matches the bid suggestion
provided by the platform under the described mechanism is zero. Consequently, if a bidder adopts a
strategy involving a positive probability of following the bid recommendation, such a strategy is not
a best-response strategy. The bidder could benefit from reducing the probability of bid-adherence
and submitting an optimally constructed bid instead. Hence, even a one-time adherence to the
bid recommendation for any position k cannot be rationalized. This allows us to further identify
and distinguish bid-adhering bidders in our dataset as those who have placed bids matching the
bid recommendations at least once.
Figure 3 illustrates that bid-adhering behavior persists, even though it is theoretically sub-
optimal. While some bidders follow bid recommendations with positive probability, others never
bid at the cut-off and instead construct their own bids. In the next section, we categorize the
bidders into two groups: bid-adhering and bid-constructing bidders, and delve into the descriptive
patterns of bid-adhering bidders.

Zhu and Song:Information Disclosure in Auctions 13
4.2. Descriptive Patterns and Explanations for Bid-adhering Bidders
If adhering precisely to the bid recommendation is not theoretically optimal, why do advertisers still
follow it? In this subsection, we provide descriptive patterns of bid-adhering bidders, and propose
several mechanisms that could explain these theoretically sub-optimal bid-adhering behaviors.
Firstly, we define the elite bid-adhering bidders as those who have followed one of the three bid
recommendations at least once. According to Theorem 1, adhering to the bid recommendation
with any positive probability is not rational. The recommendations in our dataset are relatively
high, indicating that these elite bidders have high valuations for online advertising. Although the
group of potential bid-adhering bidders may be larger, we focus on elite bidders due to their direct
observable behavior in our dataset and significant impact on platform revenue. In contrast, bid-
constructing bidders are those who have bid above the lowest recommendation at least once but
have never exactly followed any of the recommendations. By requiring bid-constructing bidders to
place bids above the lowest recommendation, we ensure that they have similar private valuations
to the elite bid-adhering bidders.
In our data set, among the bid-adhering bidders, there are 88 individuals with a total of 1494 bid
change event observations post-information release, where they bid at the cutoffs approximately
13.5% of the time. The group of bid-constructing bidders comprises 99 advertisers, with 1101 total
bid change occasion observations post-intervention. The table below shows frequency statistics for
bid-adhering bidders in online advertising, focusing on 18 active participants. Bidders with fewer
than 10 bid changes are excluded to accurately represent frequent bidders.
Metric N Mean St. dev Min Max
Bid-Adherence Occurrences 18 2.87 2.20 1 9
Total Bid Change Events 18 28.80 22.43 11 103
Bid-Adherence Rate (%) 18 12 .11% 10 .02% 3 .23% 41 .67%
Table 2 Bid-adhering Frequency Summary Statistics
Table 2 suggests that bid-adherence is a significant and substantive component of bidding behav-
ior on the online-advertising platform, influencing not only the individual bidders outcomes but

14 Zhu and Song:Information Disclosure in Auctions
also the overall market equilibrium and efficiency. While the table underscores the prevalence of
bid-adherence, it invites further exploration into the reasons why some bidders follow recommen-
dations, whereas others, like bid-constructing bidders, adopt a different bidding strategy of crafting
their own bids after information disclosure. Next, we analyze the differences between these two
groups based on their bids, and propose several underlying mechanisms to explain why bid-adhering
bidders follow the bid recommendations.
Figure 4 shows the average daily bid before and after the intervention. Initially, bid-adhering
bidders submitted bids at levels similar to bid-constructing bidders. After the intervention, there
was a significant increase in bids among the bid-adhering group, reflecting their adherence to higher
recommendations for the top 3 slots. Conversely, bid levels among the bid-constructing group in
the treated city and the top bidders in the control city remained constant. Figure 4 highlights the
heterogeneity in bidding strategies between the groups after information disclosure intervention.
Notably, there is a decrease in daily bids around early October. This is because early October is the
peak season for wedding services in Xi’an, which necessitates advertising several days in advance,
making late September a peak, and early October a trough for wedding service advertising with
a significant drop on bids across groups. In Online Appendix 8.2, we also show that bid-adhering
bidders differ from bid-constructing bidders in multiple characteristics according to our dataset,
including their reviews and review stars.
Lastly, we present several potential mechanisms to explain bid-adherence and discuss the likeli-
hood of these mechanisms. Due to the absence of laboratory data, we cannot precisely determine
the exact reason for bid-adherence. However, from the support of descriptive patterns, we find that
some explanatory mechanisms are more prevalent than others.
Cognitive Ease : People often prefer to exert less cognitive effort, which makes them more
likely to follow straightforward recommendations (Sweller (1988), Jin et al. (2017)). Our data
indicates that bid-adhering bidders have a relatively high number of reviews but lower review
stars (Online Appendix 8.2), suggesting they favor a straightforward volume-first strategy. This

Zhu and Song:Information Disclosure in Auctions 15
Figure 4 Average Daily Bid across Bidders
* Figure 4 displays the average daily bid for bid-constructing bidders (shown in blue), bid-adhering bidders (shown
in red), and bidders in the control city among top 25 th-position advertisers (shown in green). The vertical line
reflects the intervention date.
predisposition also makes them more likely to adopt straightforward recommendations for cognitive
ease. Moreover, as the options of “Use this Price” for bid recommendations are presented as default
(Figure 2), they are more likely to be chosen as changing from a default option requires additional
cognitive effort.
Anchoring Effect : The anchoring effect describes how individuals may depend excessively on
an initial piece of information (the “anchor”) for subsequent decision-making. Unlike the cognitive
ease effect where bidders simply follow recommendations, the anchoring effect leads bidders to ini-
tially try to determine their optimal bid but eventually revert to recommended bids. Our descriptive
evidences on reviews and review stars (provided in Online Appendix 8.2) suggest that bid-adhering
bidders generally employ traditional marketing strategies aimed at increasing transaction volumes,
reflecting a lower proficiency with advanced digital marketing and keyword search strategies. And
those with less experience or knowledge in a domain are more susceptible to anchoring (Wilson
et al. (1996)), offering a likely explanation for the observed bid-adherence.
Learning Effect : Bidders might follow the bid recommendation to learn quality scores or
top slot rank distributions, but we conjecture this effect to be limited since recommendations are
observed prior to bidding. If the goal is to learn the bid or quality score distributions, advertisers
can initially observe the recommendations and bid optimally without strictly adhering to these

16 Zhu and Song:Information Disclosure in Auctions
recommendations, then monitor outcomes to validate their beliefs, since the information disclosure
occurs prior to their bidding. While learning effect is possible in auctions, such learning requires
a stable environment and a relatively long-run play in a stable environment (Doraszelski et al.
(2018)). As there is no clear and direct evidence of learning effects in our dataset, we decide to
focus on short-term interactions under platform-driven changes in information disclosure policy,
without considering learning dynamics.
4.3. Impact of Information Disclosure On Market Outcomes
In this section, we explore the impact of bid recommendation information disclosure on market
outcomes. We first demonstrate the effects of bid recommendations on bids and cost per click
(CPC) for the top five positions, as shown in Figure 5a and 5b. The left graph presents the average
daily bids for the top five ad positions in Xi’an (red line) and Chengdu (blue line) before and after
the bid recommendation was introduced. The right graph displays the average CPC for the top five
ad positions in both cities. Additional effects on lower positions are detailed in Online Appendix
8.3.
(a) Average Bid of Top 5 Ad positions
* Figure 5a displays the average daily bid level in Xi’an
(red line) and Chengdu (blue line).
(b) Average CPC of Top 5 Ad positions
* Figure 5b displays the average daily CPC level in Xi’an
(red line) and Chengdu (blue line).
Figure 5 Pre-and-Post Changes in Bid and CPC of Top 5 Ad positions
Before the policy change, average bids and CPC for top positions were similar in Xi’an and
Chengdu. Following the implementation of bid recommendations on August 13, 2019, there was no
immediate increase in the average bids and CPC in Xi’an compared to Chengdu. The divergence

Zhu and Song:Information Disclosure in Auctions 17
in bid levels became noticeable three days later, likely because advertisers may require time to
adapt to this new information disclosure. Specifically, the bid levels for the top five ad positions
in Xi’an significantly increased three days post-implementation. This disparity between the two
cities persisted until the end of September, coinciding with the conclusion of the peak wedding
advertising season. For mid and lower-position ad groups, no substantial difference in bid levels
was observed following the bid recommendation release (see Appendix 8.3). This analysis suggests
that the primary impact of bid recommendations is on the top ad positions, leading to increased
bid levels and CPC in Xi’an.
In the next subsection, we present Difference-in-Differences regression results to quantify the
impact of information disclosure to bid and CPC.
4.3.1. Difference-in-Differences Regression on the Impact of Information Disclo-
sure
To assess the impact of introducing bid recommendations, we utilize a difference-in-differences
approach comparing changes in bids and CPCs between Xi’an and Chengdu. Chengdu was chosen
as the control city due to its closely matched average bid, CPC, number of ads, and advertising
revenue with Xi’an, one month prior to the policy change. Formally, we analyze the effects of bid
recommendations on bids and CPC using the following regression model:
Yit = α0 ∗ (Ti ∗ P ostt) +P3 g=1 αggroup g + P3 g=1 βg ∗ group g ∗ (Ti ∗ P ostt) +f ea i + f ed t + ϵit.
In our regression model, the unit of observation is ad-per-day, where i denotes an ad and t a
date. Yit includes two outcome measures: bid and CPC. P ostt is an indicator variable for dates
after the information release on August 13, 2019. Ti indicates whether ad i is in the treatment
city, Xi’an. group g indexes ad categories by position, divided into three groups: top, middle, and
low positions. Specifically, group 1 is an indicator variable set to one for ads in the top 5 positions,
excluding those reserved for organic search. group 2 covers ads in positions 6 to 25, and group 3
includes ads below position 25. f ea i and f ed t control for ad-specific and day-specific effects that are
constant over time, respectively. The coefficient α0 captures the difference-in-differences effect of

18 Zhu and Song:Information Disclosure in Auctions
information disclosure, while βg explores the heterogeneous effects of the treatment across different
ad positions. Standard errors are clustered at the ad level across all regressions to account for
repeated panel data, consistent with Bertrand et al. (2004).
(1) (2) (3) (4)
bid bid cpc cpc
T*Post 2.193 ∗∗∗ (0.394) 0.633 ∗∗∗ (0.207) 0.669 ∗∗∗ (0.152) 0.168 ∗ (0.0906)
group1 0.256 (0.243) -0.0695 (0.601)
group2 0.217 ∗ (0.130) 0.129 ∗∗∗ (0.0487)
T*Post*group1 5.372 ∗∗∗(1.203) 1.902 ∗∗∗(0.478)
T*Post*group2 1.705 ∗∗∗(0.289) 0.436 ∗∗∗(0.0991)
N 73044 73044 73044 73044
adj. R2 0.903 0.908 0.866 0.868
Standard errors in parentheses; Ad and day fixed effects, cluster at advertiser level
∗ p <0.10, ∗∗ p <0.05, ∗∗∗ p <0.01
Table 3 Difference-In-Differences Regression Table
To assess the impact of bid recommendation releases on market dynamics, we use daily bids
averaged across bid changes within a day; if no changes occur, the average remains constant as the
previous day. The difference-in-differences analysis shows an average bid increase of 2.19 RMB (0.3
USD) post-release, a 35% rise from pre-policy levels. We further explore variations in response by
ad position as detailed in column (2) of Table 3, which includes interactions between post-disclosure
and Xi’an dummies with a group id dummy. Ads in the top five positions experience a significant
5.37 RMB (0.74 USD) increase, about twice the overall effect. In contrast, ads in positions 6
to 25 see a more modest increase of 1.71 RMB (0.24 USD). The effects are less pronounced for
lower-position ads despite all receiving identical bid recommendations.
We then examine the impact on Cost Per Click (CPC), reported in column (3) of Table 3, which
shows a 0.67 RMB (0.09 USD) increase in CPC, a 19% lift from the pre-period level. Column (4)

Zhu and Song:Information Disclosure in Auctions 19
details the heterogeneous impact on CPC across ad groups, with top-position ads seeing the largest
increase of 1.9 RMB (0.26 USD), or 28%. Mid-position ads have a smaller, 11% increase in CPC.
These results suggest a smaller relative increase in ad prices compared to bids, which is consistent
to the GSP auction mechanism where the second-highest bid sets prices.
In this section, we examine the descriptive evidence on how information disclosure affects market
outcomes, specifically bids and CPC. We observe that the presence of bid-adhering bidders leads
to an increase in market ad prices, potentially enhancing revenue for the ad platform. However,
without known bidder valuations, the direct impact on bidder and social surplus remains unex-
plored. In the following section, we introduce a novel empirical model to identify heterogeneous
valuations for both bid-adhering and bid-constructing bidders.
5. V aluation Identification
To better understand how sub-optimal bidding behaviors influence market equilibrium, specifically
regarding bidder surplus and social surplus, it is crucial to identify advertisers’ private values. The
complexity of the GSP auction complicates empirical modeling of equilibrium bidding behavior.
Additionally, the asymmetry in behaviors between bid-adhering and bid-constructing bidders adds
to the challenge. To tackle these issues, we utilize distinct empirical approaches for identifying
private values. For bid-constructing bidders, we characterize an equilibrium model of bidding in
the GSP auction in Section 5.1 and provide valuation identification methodology. For bid-adhering
bidders, we describe the model on identifying bounds on their valuations in Section 5.2.
5.1. V aluation Identification of Bid-constructing Bidders
Here, we present a computationally feasible and practical framework for modeling the bidding
strategy of bid-constructing advertisers in the GSP auction. The primary assumption for bid-
constructing bidders is that they are fully rational, submitting bids that optimize their expected
payoffs in equilibrium.
Specifically, we adopt a symmetric independent private valuation model within bid-constructing
bidders, where bid-constructing bidders adhere to a Bayesian Nash Equilibrium bidding strategy.

20 Zhu and Song:Information Disclosure in Auctions
In our model, we analyze the daily bidding behavior of bid-constructing advertisers, indexed by t.
We assume that the distributions are stationary across each day. Despite advertisers having the
flexibility to change bids at any time, the observed frequency of bid changes averages 4.3 times per
week, aligning well with our assumption of daily modeling.
Bidding Process : In our daily bidding model, each bid-constructing advertiser i at period
t is assumed to realize a private value per click vi,t, independently and identically drawn from a
distribution V , i.e., vi,t ∼ V . The distribution V is our primary target for estimation, representing
the valuation distribution for the bid-constructing bidders. Upon realizing their private valuation,
advertiser i submits a bid bi,t within the same day to maximize her expected daily payoff. The
platform calculates daily quality scores for each advertiser and ranks them by the rank scores,
computed as the product of the advertiser i’s submitted bid bi,t and her quality score qi,t. The
platform then orders the advertisers according to these rank scores. Let rk,t be the rank score for
position k at period t. If advertiser i occupies the kth position, her daily CTR (number of clicks)
is αk, and the realized utility is αk(vi,t −
rk+1,t
qi,t ).
Quality Scores and Rank Scores: Although each consumer query generates a quality score,
potentially numbering in the hundreds daily, our dataset includes only the average daily quality
score for each bidder. In our model, each bid-constructing advertiser i believes her daily quality
scores qi,t at period t are independently and identically drawn from a distribution with cumulative
distribution function (c.d.f) Qi(q), which has continuous positive support on [0 , ∞). We assume
that the distributions of quality scores and bidder valuations are independent. The rank score rk
for the kth position is the kth order statistic from the sorted product of quality scores and bids.
We denote gk(·) as the probability density function of rk and gk−1,k(·, ·) as the joint density of rk−1
and rk.
Bidder Beliefs : We assume that the beliefs of bid-constructing bidders are consistent with
actual distributions in equilibrium, aligning with the assumptions of a Bayesian Nash Equilibrium.
Bid-constructing advertisers develop beliefs about the quality score distributions, rank score dis-
tributions, and CTRs, without access to the actual realizations of these metrics or others’ private

Zhu and Song:Information Disclosure in Auctions 21
values. During the identification process, we use empirical data on quality score distributions, rank
score distributions, and CTRs as proxies for the formed beliefs of advertiser i.
Estimation Process: Each day, the bid-constructing bidder i submits a bid that maximizes
her daily expected payoff, based on her realized valuation vi,t. The expected payoff function for
bidder i at time t with valuation vi,t, π(b|vi,t) is thus given by:
π(b|vi,t) =
Z " KX
k=1
αk
Z Z
I (rk < qb < rk−1)

vi,t − rk
q

gk−1,k (rk−1, rk) drkdrk−1
#
dQi(q), (1)
where I(rk < qb < rk−1) is an indicator function that equals 1 if the condition rk < qb < rk−1 is
satisfied, and 0 otherwise. A bid bi,t that maximizes the expected payoff π(b|vi,t) should satisfies
the following first-order condition, which is equivalent as
π(b|vi,t)
d bi,t = 0:
vi,t = bi,t +
R
[P k αkgk−1 (qbi,t) E (qbi,t − rk|rk < qbi,t)] dQi(q)R
[P k qgk (qbi,t) (αk − αk+1)] dQi(q) . (2)
Details on deriving Equation (2) are provided in Online Appendix 8.4. Equation (2) employs a
GPV-like formulation as outlined in Guerre et al. (2000). It models the advertiser’s private value
vi,t as a function of their equilibrium daily bid bi,t, the number of clicks αk at each position, and
the density functions of the k − 1th and kth position rank scores, gk−1(·) and gk(·), respectively,
along with the distribution of the daily quality score Qi(·). The identification of estimation on
verifying the uniqueness of bid-value mapping is provided in Online Appendix 8.5. Notably, as
both the numerator and denominator of the markdown term are positive, the resultant markup is
also positive, indicating that advertisers submit bids below their actual value in equilibrium. This
finding aligns with the theoretical predictions of shading behaviors in GSP (Edelman et al. (2007)).
The basic concept of value identification is then straightforward. With the density gk−1 and gk,
we can estimate bid-constructing bidders values from the Equation (2). The density gk−1 and gk
can be approximated non-parametrically from the observed bid data. We assume that the observed
pre-intervention data is generated from bidders’ equilibrium bidding strategies. We employ Guerre
et al. (2000)’s two-step estimator approach. First, we construct a sample of pseudo values from
Equation (2) using non-parametric recommendations of the density functions for the observed

22 Zhu and Song:Information Disclosure in Auctions
bids. We then use the pseudo values generated in the previous step to estimate the density of the
valuation density.
To clarify, we first simulate 100 auctions daily (30 days in total) for bid-constructing bidders.
In each auction, we simulate a daily quality score qi,t for advertiser i from a normal distribution
Qi ∼ N (¯qi, ϵ), where ¯qi represents the mean of observed quality scores for advertiser i, averaged
over all her observations. The standard deviation ϵ, consistent across all advertisers, is derived
from the observed residual across all advertisers. This uniform variance assumption is based on
the fact that the platform applies the same machine learning algorithmic treatment to compute
the quality score for each advertiser, thereby standardizing the variance while allowing individual
mean differences. In Online Appendix 8.6, we present histogram of quality scores, supporting that
normal distribution is a good approximation for quality score distribution.
We then calculate each advertiser i’s rank score at auction t, ri,t = bi,t ∗ qi,t, where qi,t are
simulated from our estimated quality score distributions. After obtaining the auction-level empirical
distribution at auction t, we sort the observations and obtain samples of rank scores. We then
estimate the density for the 1st to 24th ad position, gk, using kernel density estimation. The
estimated density is given by: gk(x) = 1 Nkhg PNk t=1 Kg  x−rk,t hg  , where rk,t is the t-th sample of the
k-th rank score, Nk is the number of observations for the k-th rank score, and hg = 1.06σkN −1/5 k is
the bandwidth, with σk being the standard deviation of the samples for the k-th rank score. The
function Kg(·) represents the normal kernel.
Using Equation (2), we estimate the pseudo values and compute the private value density, where
the bid-constructing bidder’s valuation distribution V has density f (x):
f (x) = 1 Nf hf
NfX
i=1
K
 x − vi
hf

. (3)
Here, vi represents the i-th pseudo value sample of bid-constructing bidders from Equation (2),
Nf is the number of observations, and hf = 1.06σf N −1/5 f is the bandwidth, with σf denoting the
standard deviation of the bid samples.

Zhu and Song:Information Disclosure in Auctions 23
We use pre-information disclosure data to estimate the valuations of bid-constructing bidders,
isolating the effect of information disclosure. This is crucial as information disclosure influences
the strategy of bid-adhering bidders and, consequently, the equilibrium rank scores. And the equi-
librium rank score distribution becomes a function of bid recommendations, complicating the
estimation process.
We define bid-constructing bidders as those who have bid higher than the lowest bid recom-
mendation at least once but have never adhered to any bid recommendations. Before the platform
released its bid recommendations, we observed 1 , 090 out of 8 , 151 total daily bid observations for
62 bid-constructing bidders. Firstly, we estimate gk. Then we compute pseudo valuation, using
Equation (2), applying it only to bids from bid-constructing bidders that meet the condition
I(rk < qb < rk−1), as in Equation (1). Using this pseudo data, we then estimate the private values
density function with Equation (3). The empirical estimation on bid-constructing bidder valuation
distribution and corresponding bid distribution are provided in Online Appendix 8.7.
5.2. V aluation Bounds for Bid-adhering Bidders
In Section 4, we observed the sub-optimal behaviors of bid-adhering bidders, indicating that the
equilibrium bidding strategies previously discussed might not be applicable for this group. While
it is possible to develop a specific stylized model for bid-adhering bidders, the primary focus of this
paper is to document such behaviors and propose policy interventions, rather than to elaborate
on the underlying behavioral models. Therefore, the comprehensive exploration of reasons why
some bidders adhere to bid recommendations and the creation of specific models for bid-adhering
bidders are left for future research, possibly involving laboratory experiments, with preliminary
explanations in Section 4.2.
Given this focus, instead of developing specific stylized models, we propose an incomplete model
based on two foundational assumptions: bidders never bid more than their valuations (Li (2017)),
and they do not allow an opponent to win at a price they are willing to match. We assume that
bid-adhering bidders share the same valuation distribution. Although we cannot precisely estimate

24 Zhu and Song:Information Disclosure in Auctions
this distribution, two foundational assumptions enable us to establish bounds on their valuations.
The first assumption on no overbidding provides lower bounds on bid-adhering bidders’ private
valuations, as their submitted bids. The second assumption suggests that whenever a bid-adhering
bidder submits a bid that is lower than one specific recommended bid, it implies that the bidder
has a private valuation lower that recommendation. Otherwise, knowing that some bid-adhering
bidder would bid at the recommended price that they are willing to match, the bidder would have
bid at that price instead. Hence, bid recommendations that exceed submitted bids act as upper
bounds for the valuation of bid-adhering bidders.
Specifically, when a bid-adhering bidder submit a bid bi,t, the lower bound of valuation vi,t =
bi,t, and the upper bound vi,t equals to the smallest bid recommendation above bi,t, vi,t =
mink{si,k,t, si,k,t > bi,t}. We further non-parametrically estimate the lower bounds and upper
bounds from vi,t and vi,t. The empirical estimation on bid-constructing bidder valuation distribu-
tion is provided in Online Appendix (8.8).
6. Design Information Disclosure : Counterfactual Analysis
6.1. Preliminaries
In Section 5, we provide the methodology for identifying valuations of heterogeneous bidders under
generalized second price (GSP) auction. With these valuations identified, we are able to exam-
ine both bidder surplus and social surplus under the effects of the information disclosure policy.
Furthermore, we conduct counterfactual analyses to guide enhancements in information disclo-
sure design, allowing the platform to pursue various objectives such as revenue maximization or
social/bidder surplus improvement.
To facilitate counterfactual analysis, we first assume that bid-constructing bidders are rational,
and bid in best response to the opponents strategies. As there are multiple equilibria in GSP
auctions, the following assumption assumes that bid-constructing bidders adopt a locally envy-free
equilibrium bidding strategy (Edelman et al. (2007)) which is in favor to the bidder. This implies
that our counterfactual analysis provides a conservative estimate on platform revenue. And the
platform revenue in any other locally envy-free equilibrium would be at least as high as what we
have reported.

Zhu and Song:Information Disclosure in Auctions 25
Assumption 1. Envy-Free Equilibrium Strategy : Bid-constructing bidders bid under a
locally envy-free equilibrium strategy.
For bid-adhering bidders, the assumptions are more complex. We first establish the following
assumption regarding the behavior of bid-adhering bidders when the platform varies the number
of slots for providing bid recommendations while maintaining the same mechanism for generating
these recommendations.
Assumption 2. Stability of Bid-Adherence Under Fixed Mechanism : The bidding strat-
egy of bid-adhering bidders remains unchanged, if the platform only varies the number of slots for
providing bid recommendations, under the same recommendation generation algorithm.
Assumption 2 is crucial. As outlined in Section 3.2, we documented the bid recommendation gen-
eration algorithm, which the platform fully discloses. While it may seem presumptuous to assume
that bid-adhering bidders will consistently follow (with positive probability) all platform-provided
bid recommendations under any bid recommendation generation algorithm, it is reasonable to
expect that as long as the recommendation generation algorithms remain unchanged, the same
group of bidders will continue to occasionally adhere to these recommendations. Conversely, bid-
constructing bidders will continue to submit their own bids. A mild assumption like Assumption 2
facilitates the conduct of counterfactual analysis by varying the amount of information provision,
through varying the number of slots with bid recommendations. Altering the bid recommenda-
tion generation algorithm could potentially increase profits or enhance surplus, assuming that the
strategies of bid-adhering bidders remain unchanged. However, as we cannot verify whether bid-
adhering bidders would continue to adhere to bid recommendations under a different algorithm, we
conduct our counterfactual analysis under Assumption 2, maintaining the current recommendation
generation algorithm.
With Assumption 2, we further explore different bidding models of bid-adhering bidders. As
discussed in Section 4.2, the overall bid-adherence rate among the 88 identified bid-adhering indi-
viduals is 13 .5%. Among those actively participating in auctions with more than 10 bid-change

26 Zhu and Song:Information Disclosure in Auctions
event, the bid-adherence rate is 12 .1%. With the descriptive data on bid-adhering bidders, we
assume a probabilistic bid-adhering strategy: when a bid-adhering bidder observes a suggestive
bid, and if his valuation exceeds any of the suggestive bids, the bidder follows the suggestive bid
closest to his valuation with a fixed probability.
Assumption 3. Probabilistic Bid-Adherence: When observing a set of bid recommendations
{si,k,t}, a bid-adhering bidder i with valuation vi adheres to the bid recommendation si,k∗(i),t =
maxk{si,k,t | si,k,t < vi} with a constant probability p.
Assumption 3 is relatively restrictive. Firstly, it assumes that all bid-adhering bidders follow the
bid recommendation with a fixed probability p. Adjusting the model to fit an individual probability
of adherence for each bidder may result in high variance in the estimation due to the limited number
of bid-changing events per bidder. Therefore, we treat bid-adhering bidders as a homogeneous
group with a constant probability p. Secondly, it assumes that the bid-adhering probability is
an exogenous parameter, not influenced by the level of bid recommendation. This precludes the
likelihood that bid-adhering bidders are biased towards following higher or lower recommendations.
In our data, we did not find such biased tendency among bid-adhering bidders. Online Appendix
8.9 provides data on the bids submitted and the bid recommendations observed for several bid-
adhering bidders, supporting our assumption of probabilistic bid-adherence. In the counterfactual
analysis, we use a grid search to find the probability p∗ to match the overall bid-adherence rate in
table 2 under current information provision mechanism .
Lastly, we still need to propose bidding model on how the bid-adhering bidder bids, when they
are not following bid-recommendations. We propose two models for the bid-adhering bidders. The
polynomial bidding model and the random shading model. It is important to note that due to the
lack of comprehensive survey data from bid-adhering bidders, and controlled laboratory experi-
ments, we are unable to fully characterize a bidding model for bid-adhering bidders. Nonetheless,
the results presented in this counterfactual analysis section remain robust across the different
bidding models we have proposed.

Zhu and Song:Information Disclosure in Auctions 27
For the polynomial bidding model, we assume that when bid-adhering bidders do not adhere
to the bid recommendations, they utilize the same bidding strategy, modeled by a polynomial
function of their valuation. Specifically, if bidder i values an item at vi,t on day t and chooses
not to adhere to the bid recommendation, bidder i submits a bid bi,t calculated as: bi,t = p(vi,t),
where p(·) is a polynomial function. We fit the polynomial function p(·) following a data-driven
approach, where we utilize both lower and upper bounds of bid-adhering bidder valuations (detailed
in Online Appendix 8.10). Specifically, we simulate 1001 valuations from each estimated valuation
distribution bound for bid-adhering bidders, sorting the valuations to map observed bids in a
monotonic increasing relationship. This process is repeated 10,000 times, with aggregation over
all samples to determine the polynomial parameters. Under the polynomial bidding model, the
fitted bidding functions of the bid-adhering bidders are : for the lower-bound valuation, p(v) =
1.11 × 10−5 ∗ v3 − 5.54 × 10−3 ∗ v2 + 0.83 ∗ v − 1.68, and for the upper-bound valuation, p(v) =
−1.50 × 10−3 ∗ v2 + 0.57 ∗ v − 3.11.
For the random shading model, we assume that when bid-adhering bidders deviate from bid
recommendations, they randomly shade their valuations by bidding b(vi) = αi,tvi, where αi,t is
drawn from a standard uniform distribution, αi,t ∼ Unif[0, 1]. This model is supported by empirical
evidence: the ratio of the expected bid to the expected lower-bound of valuation is 0 .5284, and the
ratio of the expected bid to the expected upper-bound of valuation is 0 .4071. These ratios, both
close to 0 .5, to some extent, provide justification for the uniformly random shading model.
Lastly, we generate quality scores from the estimated distributions, accounting for group hetero-
geneity by estimating these distributions separately for bid-constructing and bid-adhering groups.
We use simulated quality scores instead of mapping actual quality scores in our dataset to each
bidder mainly for confidentiality reasons. We further utilize the empirical average click-through
rate (CTR) to simulate the market for the top 20 slots in sponsored search (slots beyond the top
20 exhibited less than 0.1 daily CTR). We simulate the market with 99 bid-constructing bidders
and 88 bid-adhering bidders, matching our empirical data.

28 Zhu and Song:Information Disclosure in Auctions
6.2. Counterfactual Analysis
In the counterfactual analysis, we keep the same recommendation generation algorithm and explore
how variations in the amount of information provided on online advertising platforms influence
market outcomes. Specifically, we explore how altering the top number of slots with bid recom-
mendations will change the ad prices, the platform profits, and the bidder and social surplus.
Table 4 and 5 provide the counterfactual analysis, we present a range of of market outcomes,
with the range corresponding to using the lower bound valuation to the upper bound valuation
for bid-adhering bidders. For each scenario, we simulate with 10 , 000 periods, and average across
the observations. The numbers in brackets correspond to using the upper bound of bid-adhering
bidders valuation.
In terms of platform revenue, as expected, increasing the amount of information provided, under
the bid-adhering mechanism, leads to an increase in ad prices and platform revenue. This is intu-
itive: under our probabilistic bid-adherence assumption, bid-adhering bidders now have a higher
probability of accepting a recommended bid instead of shading their bids, directly affecting the
rise in ad prices and revenue. Additionally, bid-constructing bidders, knowing that bid-adhering
bidders are bidding at recommended prices, also increase their bids in response, which further
elevates ad prices and revenue.
We define the surplus for bidder i who occupies position k at period t with quality score qi,t as
αk(vi,t −
rk+1,t
qi,t ). The increase in platform revenue comes at a cost, with a decrease in bidder surplus.
This is because, when bid-adhering bidders do not adhere to recommendations, they tend to shade
their bids excessively, leading to a form of semi-collusion in the generalized second price auction.
Although they do not secure the most desirable positions warranted by their high valuations, they
manage to obtain reasonably lower spots at significantly reduced prices. However, when they follow
the bid recommendation, they secure top sponsored search positions at the cost of increased bids.
This decrease in bidder surplus does not account for the indirect benefits of occupying a higher
spot, such as enhanced brand awareness and increased reviews, which are consistent with our

Zhu and Song:Information Disclosure in Auctions 29
descriptive findings on reviews (provided in Online Appendix 8.2). These effects, while not directly
quantifiable in bidder surplus calculations, could potentially benefit the bid-adhering bidders.
The impact on social surplus is more complex, and there exists a trade-off between increased
platform revenue and reduced bidder surplus. Both the polynomial and random bidding models
suggest that releasing bid recommendations for all top 20 positions could be overly aggressive, as the
decrease in bidder surplus begins to outweigh the increase in platform revenue. Our counterfactual
analysis suggests that releasing a moderate level of bid recommendations for the top 10 slots results
in the highest social surplus.
Number of Slots Avg. Ads Price Revenue Bidder Surplus Social Surplus
Pre-intervention 28.23 (28.07) 3.81 × 104 (3.83) 3.39 × 104 (4.03) 7.20 × 104 (7.86)
Top 1 34.84 (37.76) 5.93 × 104 (6.41) 2.87 × 104 (3.04) 8.80 × 104 (9.45)
Top 3 (current) 38.56 (42.48) 6.75 × 104 (7.30) 2.40 × 104 (2.50) 9.14 × 104 (9.80)
Top 5 41.45 (46.17) 7.24 × 104 (7.90) 2.07 × 104 (2.12) 9.31 × 104 (10.02)
Top 10 46.78 (53.16) 7.86 × 104 (8.66) 1.62 × 104 (1.61) 9.48 × 104 (10.27)
All Positions 51.40 (60.58) 8.10 × 104 (9.02) 1.35 × 104 (1.25) 9.44 × 104 (10.26)
Table 4 Counterfactual Analysis of Varying Number of Slots on Market Outcomes
Polynomial Bidding Model, Ads price and Revenue in unit of RMB
Number of Slots Avg. Ads Price Revenue Bidder Surplus Social Surplus
Pre-intervention 34.73 (30.60) 5.96 × 104 (6.79) 2.38 × 104 (2.53) 8.33 × 104 (9.32)
Top 1 38.28 (43.90) 6.68 × 104 (7.51) 2.33 × 104 (2.36) 9.01 × 104 (9.87)
Top 3 (current) 41.34 (47.64) 7.22 × 104 (8.05) 2.05 × 104 (2.06) 9.27 × 104 (10.01)
Top 5 43.70 (50.57) 7.53 × 104 (8.37) 1.86 × 104 (1.84) 9.39 × 104 (10.21)
Top 10 47.99 (55.80) 7.92 × 104 (8.79) 1.55 × 104 (1.50) 9.47 × 104 (10.29)
All Positions 51.67 (60.84) 8.09 × 104 (9.01) 1.34 × 104 (1.24) 9.44 × 104 (10.25)
Table 5 Counterfactual Analysis of Varying Number of Slots on Market Outcomes
Random Bidding Model, Ads price and Revenue in unit of RMB

30 Zhu and Song:Information Disclosure in Auctions
7. Conclusion
Identifying the heterogeneity in bidder valuations and strategies is essential for optimizing out-
comes on online advertising platforms under information disclosure. This study explores the design
of information disclosure policies and their impact on market dynamics within a Yelp-like plat-
form that introduced a bid recommendation system. Our analysis identifies a subset of advertisers
(termed bid-adhering advisors), who, characterized by lower review ratings and initial ad place-
ments, tend to follow the platform’s bid recommendations – a theoretically sub-optimal practice.
In contrast, bid-constructing bidders consistently craft their own bids without following released
recommendations.
Empirical evidence from a difference-in-differences (DID) analysis indicates that bid recommen-
dations elevate ad prices and platform revenue. To thoroughly assess the impact of these recom-
mendations on participant surplus, it is necessary to identify bidder valuations within this intricate
system featuring heterogeneous reaction to information disclosure. Our empirical model is the
first to identify private values for bid-constructing advertisers in the online Generalized Second
Price (GSP) auction, and establishes valuation bounds for bid-adhering bidders. Utilizing these
valuations, we conduct counterfactual analysis to explore how varying the number of disclosed
bid recommendations affects platform revenue, bidder surplus, and total surplus. Our findings
suggest that while platform profits increase with increased information disclosure, social surplus
peaks under a carefully designed information provision scheme, highlighting that more extensive
disclosure is not always socially optimal.
This paper underscores the importance of recognizing and accounting for heterogeneous responses
to information disclosure. By pinpointing a subgroup of market participants more likely to adhere to
recommendations, platforms can improve their information disclosure strategies. The implications
of our findings extend beyond search advertising to other online marketplaces, such as Amazon
and Airbnb, which provide price recommendations to suppliers based on demand and competitive
dynamics.

Zhu and Song:Information Disclosure in Auctions 31
There are many promising directions for future research. First, behavioral economics could pro-
vide significant insights into the psychological drivers of bid adherence through controlled lab
experiments, which were not covered in this paper due to resource constraints. Additionally, inves-
tigating the effects of changes in the recommendation algorithm on bidder behavior could enhance
our understanding of bidder sensitivity and adaptability. Another fruitful area of study is the
interaction between optimal auction design and bid-adherence behavior. For instance, while the
platform currently maintains a reserve price of 2.5 RMB in the bid recommendation system, future
research could explore how to optimally set reserve prices to maximize platform objectives in envi-
ronments characterized by information disclosure and bid-adhering behaviors. Another interesting
direction for future theory research is to formally analyze the impact of increasing the number of
bid recommendation slots on revenue and social surplus with analytical models. Although quality
score interventions complicate the definition of social surplus — since quality scores reflect poten-
tial consumer satisfaction and primarily benefit the consumer side—there remains an opportunity
to develop theoretical models that explore the effects of information disclosure levels on ad revenue
and bidder surplus without the influence of quality scores. Such an extension could provide valuable
theory-guided insights into optimizing platform information disclosure strategies for advertisers.

32 Zhu and Song:Information Disclosure in Auctions
References
Agarwal, A., Hosanagar, K., and Smith, M. D. (2011). Location, location, location: An analysis of profitability
of position in online advertising markets. Journal of marketing research , 48(6):1057–1073.
Agrawal, N., Najafi-Asadolahi, S., and Smith, S. A. (2020). Optimization of operational decisions in digital
advertising: A literature review . Springer.
Akbarpour, M. and Li, S. (2018). Credible mechanisms. In EC, page 371.
Amaldoss, W., Desai, P. S., and Shin, W. (2015). Keyword search advertising and first-page bid estimates:
A strategic analysis. Management Science, 61(3):507–519.
Athey, S. and Nekipelov, D. (2010). A structural model of sponsored search advertising auctions. In Sixth
ad auctions workshop , volume 15.
Bajari, P. and Horta¸ csu, A. (2003). The winner’s curse, reserve prices, and endogenous entry: Empirical
insights from ebay auctions. RAND Journal of Economics , pages 329–355.
Balseiro, S. R. and Gur, Y. (2019). Learning in repeated auctions with budgets: Regret minimization and
equilibrium. Management Science, 65(9):3952–3968.
Barbaro, S. and Bracht, B. (2004). Shilling, squeezing, sniping: Explaining late bidding in online second-price
auctions. Working article. University of Mainz, Mainz, Germany .
Bertrand, M., Duflo, E., and Mullainathan, S. (2004). How much should we trust differences-in-differences
estimates? The Quarterly journal of economics , 119(1):249–275.
Campo, S., Perrigne, I., and Vuong, Q. (2003). Asymmetry in first-price auctions with affiliated private
values. Journal of Applied Econometrics , 18(2):179–207.
Cantillon, E., Pesendorfer, M., et al. (2006). Auctioning bus routes: The london experience. Combinatorial
auctions, 22:573–592.
Caro, F. and de Tejada Cuenca, A. S. (2023). Believing in analytics: Managers’ adherence to price recom-
mendations from a dss. Manufacturing & Service Operations Management , 25(2):524–542.
Chakraborty, S. and Swinney, R. (2021). Signaling to the crowd: Private quality information and rewards-
based crowdfunding. Manufacturing & Service Operations Management , 23(1):155–169.

Zhu and Song:Information Disclosure in Auctions 33
Chen, L., Rai, A., Chen, W., and Guo, X. (2024). Signaling effects under dynamic capacity in online matching
platforms: Evidence from online health consultation communities. Information Systems Research.
Cho, S.-J., Paarsch, H. J., and Rust, J. (2014). Is the ‘linkage principle’valid? evidence from the field. The
Journal of Industrial Economics , 62(2):346–375.
Choi, H., Mela, C. F., Balseiro, S. R., and Leary, A. (2020). Online display advertising markets: A literature
review and future directions. Information Systems Research, 31(2):556–575.
Chu, L. Y., Shamir, N., and Shin, H. (2017). Strategic communication for capacity alignment with pricing
in a supply chain. Management Science, 63(12):4366–4388.
Cui, R. and Shin, H. (2018). Sharing aggregate inventory information with customers: Strategic cross-selling
and shortage reduction. Management Science, 64(1):381–400.
De Silva, D. G., Dunne, T., Kankanamge, A., and Kosmopoulou, G. (2008). The impact of public information
on bidding in highway procurement auctions. European Economic Review, 52(1):150–181.
Donald, S. G. and Paarsch, H. J. (1993). Piecewise pseudo-maximum likelihood estimation in empirical
models of auctions. International Economic Review , pages 121–148.
Donald, S. G. and Paarsch, H. J. (1996). Identification, estimation, and testing in parametric empirical
models of auctions within the independent private values paradigm. Econometric Theory, pages 517–
567.
Doraszelski, U., Lewis, G., and Pakes, A. (2018). Just starting out: Learning and equilibrium in a new
market. American Economic Review, 108(3):565–615.
Edelman, B., Ostrovsky, M., and Schwarz, M. (2007). Internet advertising and the generalized second-price
auction: Selling billions of dollars worth of keywords. American economic review, 97(1):242–259.
Fridgeirsdottir, K. and Najafi-Asadolahi, S. (2018). Cost-per-impression pricing for display advertising.
Operations Research, 66(3):653–672.
Fu, R., Jin, G. Z., and Liu, M. (2022). Does human-algorithm feedback loop lead to error propagation?
evidence from zillow’s zestimate. Technical report, National Bureau of Economic Research.
Gayle, W.-R. and Richard, J. F. (2008). Numerical solutions of asymmetric, first-price, independent private
values auctions. Computational Economics, 32(3):245–278.

34 Zhu and Song:Information Disclosure in Auctions
Ghose, A. and Yang, S. (2009). An empirical analysis of search engine advertising: Sponsored search in
electronic markets. Management science, 55(10):1605–1622.
Guerre, E., Perrigne, I., and Vuong, Q. (2000). Optimal nonparametric estimation of first-price auctions.
Econometrica, 68(3):525–574.
Gupta, D., Schmitt, M., and Stamatopoulos, I. (2019). Local cost synergies in reverse auctions: An application
to road salt procurement. Available at SSRN 3435185 .
Hern´ andez, C., Quint, D., and Turansick, C. (2020). Estimation in english auctions with unobserved hetero-
geneity. The RAND Journal of Economics , 51(3):868–904.
Horta¸ csu, A., Luco, F., Puller, S. L., and Zhu, D. (2019). Does strategic ability affect efficiency? evidence
from electricity markets. American Economic Review, 109(12):4302–4342.
Horta¸ csu, A. and Puller, S. L. (2008). Understanding strategic bidding in multi-unit auctions: a case study
of the texas electricity spot market. The RAND Journal of Economics , 39(1):86–114.
Jerath, K., Ma, L., Park, Y.-H., and Srinivasan, K. (2011). A “position paradox” in sponsored search
auctions. Marketing Science, 30(4):612–627.
Jiang, H., Cao, J., and Shen, Z.-J. M. (2024). Intertemporal pricing via nonparametric estimation: Integrat-
ing reference effects and consumer heterogeneity. Manufacturing & Service Operations Management ,
26(1):28–46.
Jin, Y., Cardoso, B. D. L. R. P., and Verbert, K. (2017). How do different levels of user control affect
cognitive load and acceptance of recommendations? In IntRS@ RecSys, pages 35–42.
Kim, S. W., Olivares, M., and Weintraub, G. Y. (2014). Measuring the performance of large-scale combina-
torial auctions: A structural estimation approach. Management Science, 60(5):1180–1201.
Krasnokutskaya, E. (2011). Identification and estimation of auction models with unobserved heterogeneity.
The Review of Economic Studies , 78(1):293–327.
Laffont, J.-J., Ossard, H., and Vuong, Q. (1995). Econometrics of first-price auctions. Econometrica: Journal
of the Econometric Society , pages 953–980.
Li, S. (2017). Obviously strategy-proof mechanisms. American Economic Review, 107(11):3257–87.

Zhu and Song:Information Disclosure in Auctions 35
Lu, T. and Tomlin, B. (2023). Forewarned is forearmed? contingent sourcing, shipment information, and
supplier competition. Manufacturing & Service Operations Management , 25(5):1796–1813.
Milgrom, P. and Shannon, C. (1994). Monotone comparative statics. Econometrica: Journal of the Econo-
metric Society, pages 157–180.
Milgrom, P. R. and Weber, R. J. (1982). A theory of auctions and competitive bidding. Econometrica:
Journal of the Econometric Society , pages 1089–1122.
Najafi-Asadolahi, S. and Fridgeirsdottir, K. (2014). Cost-per-click pricing for display advertising. Manufac-
turing & Service Operations Management , 16(4):482–497.
Narayanan, S. and Kalyanam, K. (2015). Position effects in search advertising and their moderators: A
regression discontinuity approach. Marketing Science, 34(3):388–407.
Ockenfels, A. and Roth, A. E. (2006). Late and multiple bidding in second price internet auctions: Theory and
evidence concerning different rules for ending an auction. Games and Economic behavior , 55(2):297–
320.
Roth, A. E. and Ockenfels, A. (2002). Last-minute bidding and the rules for ending second-price auctions:
Evidence from ebay and amazon auctions on the internet. American economic review, 92(4):1093–1103.
Shamir, N. and Shin, H. (2018). The perils of sharing information in a trade association under a strategic
wholesale price. Production and Operations Management , 27(11):1978–1995.
Southern, M. G. (2023). Google allegedly adjusts ad auctions to meet revenue goals. Accessed: May 6, 2024.
Statista (2024). Search advertising - united states. Accessed: May 6, 2024.
Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive science, 12(2):257–
285.
Tadelis, S. and Zettelmeyer, F. (2015). Information disclosure as a matching mechanism: Theory and evidence
from a field experiment. American Economic Review, 105(2):886–905.
Varian, H. R. (2007). Position auctions. international Journal of industrial Organization , 25(6):1163–1178.
Wilson, T. D., Houston, C. E., Etling, K. M., and Brekke, N. (1996). A new look at anchoring effects: basic
anchoring and its antecedents. Journal of Experimental Psychology: General , 125(4):387.

36 Zhu and Song:Information Disclosure in Auctions
Yao, S. and Mela, C. F. (2011). A dynamic model of sponsored search advertising. Marketing Science ,
30(3):447–468.
Zhang, X. and Feng, J. (2011). Cyclical bid adjustments in search-engine advertising. Management Science,
57(9):1703–1719.

Zhu and Song:Information Disclosure in Auctions 37
8. Online Appendix
8.1. Proof of Theorem 1
We first introduce the following assumptions for Theorem 1.
Assumption 4. 1. Bidder i is a Bayesian utility maximizer who optimizes her expected utility
based on her beliefs about quality score distributions, aware of her own valuation at period t, denoted
as vi,t.
2. Bidder i understands the bid recommendation generation process. Specifically, for the kth
position at period t, bidder i receives a bid recommendation si,k,t =
rk+1,t−1
ˆqi,t , where rk+1,t−1 is the
rank score of position k + 1 from period t − 1, and ˆqi,t is the simulated quality score for bidder i at
period t.
3. Bidder i’s belief about the actual quality score distribution for each bidder j at period t is
independently drawn from distributions Qj,t, which have continuous positive support on the interval
[0, ∞). Similarly, the belief regarding the platform-simulated quality score distribution for calculating
bidder j’s bid recommendation at period t, ˆqj,t, follows distribution of ˆQj,t with continuous positive
support on the interval [0, ∞).
With Assumption 4, we are ready to prove Theorem 1. As a Bayesian expected utility maximizer
observing the quality score adjusted bid recommendation at period t for position k, si,k,t, bidder i
updates the belief on the distribution of the k + 1th position’s rank score from period t − 1, denoted
rk+1,t−1 which is distributed as si,k,t ˆQi,t. Given that other bidders follow the bid recommendation,
the bidding strategy for bidder j is bj =
rk+1,t−1
ˆQj,t , and the rank score associated with bj follows the
distribution si,k,t
ˆQi,tQj,t
ˆQj,t . Under Assumption 4, as long as the bid recommendation si,k,t is non-zero,
the rank score distributions at period t have continuous positive support on [0 , ∞). And bidder i
can update the belief on the rank score distribution rk,t, and the joint rank score distribution with
associated probability density function (pdf) gk−1,k,t(·, ·) with support on [0 , ∞) × [0, ∞) at period
t.

38 Zhu and Song:Information Disclosure in Auctions
Bidder i then solves the following optimization problem to maximize her expected profit, given
her valuation vi,t. Let Qi,t(q) denote the cumulative distribution function (cdf) of the distribution
Qi,t,
π(b|vi,t) =
Z ∞
0
"X
k
αk
Z ∞
qb
Z qb
0

vi,t − rk,t
q

gk−1,k,t (rk−1,t, rk,t) drk,t

drk−1,t
#
dQi,t(q)
Taking the first-order derivative and setting it to zero (for details please refer to Appendix 8.4),
let gk(·) be the marginal probability density function of the joint rank score pdf gk−1,k,t(·, ·),
vi,t = b +
R ∞
0 [P k αkgk−1 (qb) E (qb − rk,t|rk,t < qb)] dQi,t(q)R ∞
0 [P k qgk (qb) (αk − αk+1)] dQi,t(q) (4)
Given the valuation vi,t, the best response on bid b of a Bayesian expected utility maximizer
should satisfy Equation (4). As si,k,t =
rk+1,t−1
ˆqi,t , where ˆqi,t is a sample of bidder i’s simulated quality
score at period t from an atomless distribution ˆQi,t, P (si,k,t = b) = 0. The bid recommendationsi,k,t
coincides with bidder i’s optimal bid b is a probability zero event. Hence, any strategy that involves
a positive probability on adhering to bid recommendation si,k,t is not a best response strategy.

Zhu and Song:Information Disclosure in Auctions 39
8.2. Descriptive Patterns on Reviews and Review Stars
We explore differences in reviews metrics between groups as shown in Figure 6. Bid-adhering
bidders have lower review stars but a higher number of reviews, suggesting they are likely to adopt
a straightforward marketing strategy focused mostly on increasing transaction volumes. Following
the release of bid recommendations, the review stars among the bid-adhering group have slightly
increased. Additionally, as depicted in Figure 6, the number of reviews for the bid-adhering group
has also improved, likely due to new consumers (Narayanan and Kalyanam (2015)). In general,
we observe improvements in advertising performance in terms of review numbers for bid-adhering
bidders, who also incur higher costs per click after information disclosure.
Figure 6 Reviews
* Figure 6 displays the review star and review number for bid-constructing bidders (shown in blue) and
bid-adhering bidders (shown in red). The green line represents the daily average level in the control city among top
25th-position advertisers. The vertical line reflects the intervention date.

40 Zhu and Song:Information Disclosure in Auctions
8.3. Pre-Post Changes in Bid and CPC in Lower Ad Positions
(a) Average Bid of Top 5 Ad positions
* Figure 7a displays the average daily bid level in Xi’an
(red line) and Chengdu (blue line) of Mid (6-25th) Ad
slots.
(b) Average CPC of Top 5 Ad positions
* Figure 7b displays the average daily bid level in Xi’an
(red line) and Chengdu (blue line) of Mid (6-25th) Ad
slots.
Figure 7 Pre-and-Post Changes in Bid and CPC of Mid (6-25th) Ad Slots
(a) Average Bid of Top 5 Ad positions
* Figure 8a displays the average daily bid level in Xi’an
(red line) and Chengdu (blue line) of lower ( >25th) Ad
slots.
(b) Average CPC of Top 5 Ad positions
* Figure 8b displays the average daily bid level in Xi’an
(red line) and Chengdu (blue line) of of lower ( >25th) Ad
slots.
Figure 8 Pre-and-Post Changes in Bid and CPC of Lower ( >25th) Ad Slots

Zhu and Song:Information Disclosure in Auctions 41
8.4. Estimation Process
The bidder i’s expected payoff when submitting bid equals to b, with valuation vi,t, is given by
π(b|vi,t) =
Z " KX
k=1
αk
Z Z
1 (rk < qb < rk−1)

vi,t − rk
q

gk−1,k (rk−1, rk) drkdrk−1
#
dQi(q)
=
Z "X
k
αk
Z ∞
qb
Z qb
0

vi,t − rk
q

gk−1,k (rk−1, rk) drk

drk−1
#
dQi(q).
Taking the first order derivative with respect to b gives us:
dπ(b|vi,t)
db = −
Z "X
k
αk
Z qb
0
q

vi,t − rk
q

gk−1,k (qb, rk) drk − q (vi,t − b)
Z ∞
qb
gk−1,k (rk−1, qb) drk−1
#
dQi(q)
= −
Z "X
k
αk

gk−1 (qb)
Z qb
0
q

vi,t − rk
q

gk−1,k (rk|qb) drk − q (vi,t − b)
Z ∞
qb
gk−1,k (rk−1, qb) drk−1
#
dQi(q)
= −
Z "X
k
αk

gk−1 (qb) q

vi,t − 1 q E (rk|rk < qb)  − q (vi,t − b) gk (qb) # dQi(q).
Solving for v with the first order condition π′(b|vi,t) = 0, we have
vi,t =
R
[P k αk (gk−1 (qb) E (rk|rk < qb) − qbgk (qb))] dQi(q)R
[P k qαk (gk−1 (qb) − gk (qb))] dQi(q)
= b +
R
[P k αkgk−1 (qb) E (rk − qb|rk < qb)] dQi(q)R
[P k qαk (gk−1 (qb) − gk (qb))] dQi(q) .
Rearrange the above equation and let b = bi,t, which represents the bid submitted by bidder i at
period t,
vi,t = bi,t +
R
[P k αkgk−1 (qbi,t) E (qbi,t − rk|rk < qbi,t)] dQi(q)R
[P k qgk (qbi,t) (αk − αk+1)] dQi(q),
which is Equation (2).
We further show that any bid maximizing the expected payoff function must satisfy Equation
(2), establishing that the first-order condition is necessary. In Appendix 8.5, we also confirm that
this condition is sufficient. For the necessity of the first-order condition, we show that a bid b that
optimizes the expected payoff π(b|vi,t) must lie within the interior of [0 , ∞). The feasible bid set
is [0, ∞). And π(b = 0|vi,t) = 0. Given that the valuation vi,t is bounded, overbidding beyond this
valuation is also not optimal (Edelman et al. (2007)). Therefore, the optimal bid b ∈ (0, vi,t) is
within the interior of feasible bid set. Hence, the first-order condition outlined in Equation (2) is
a necessary condition for b being an optimal bid that maximizes the expected payoff.

42 Zhu and Song:Information Disclosure in Auctions
8.5. Identification for Estimation
Firstly, we propose the following lemma on showing that the bidding strategy is increasing in
valuation – with a higher valuation, the optimal bid derived in Equation (2) is higher.
Lemma 1. Let b(vi,t) be the bidding strategy that maximizes the expected payoff function π(b|vi,t).
b(vi,t) is monotone increasing in vi,t.
We prove this by showing that the expected payoff of bidding b given vi,t, π(b|vi,t) has an
increasing difference.
∂π(b|vi,t)
∂b = −
Z "X
k
αk

gk−1 (qb) q

vi,t − 1 q E (rk|rk < qb)  − q (vi,t − b) gk (qb) # dQi(q)
And
∂2π(b|vi,t)
∂bdvi,t
=
Z X
k
αkq(gk(qb) − gk−1(qb))dQi(q) =
Z X
k
(αk − αk+1)gk(qb)dQi(q) > 0
Hence π(b|vi,t) has increasing difference in (b, vi,t), and b(vi,t) is monotone increasing in v (Milgrom
and Shannon (1994)).
We then demonstrate that all pairs ( bi,t, vi,t) satisfying Equation (2) imply that bi,t maximizes
the function π(b|vi,t). Consider a pair (bi,t, vi,t) that meets the first-order condition. Let b < bi,t < ¯b,
and ( v, b) and (¯v, ¯b) are pairs such that b and ¯b maximize π(b|v) and π(b|¯v) respectively, each
satisfying the first-order condition under the same rank score and quality score distributions. From
Lemma 1, v < ¯v.
Moreover, from Appendix 8.4, we have
dπ(b|vi,t)
db

b=b
=
 Z "X
k
qgk (qb) (αk − αk+1)
#
dQi(q)
! 
−vi,t + b +
R
[P k αkgk−1 (qb) E (qb − rk|rk < qb)] dQi(q)R
[P k qgk (qb) (αk − αk+1)] dQi(q)

.
And from Equation (2), as ( v, b) satisfies the first order condition,
v = b +
R
[P k αkgk−1 (qb) E (qb − rk|rk < qb)] dQi(q)R
[P k qgk (qb) (αk − αk+1)] dQi(q) .
Hence
dπ(b|vi,t)
db

b=b
=
 Z "X
k
qgk (qb) (αk − αk+1)
#
dQi(q)
!
(v − vi,t) < 0

Zhu and Song:Information Disclosure in Auctions 43
Similarly,
dπ(b|vi)
db

b=b
=
 Z "X
k
qgk

qb

(αk − αk+1)
#
dQi(q)
!
(v − vi,t) > 0
Therefore,
dπ(b|vi,t)
db

b=b
< 0 <
dπ(b|vi,t)
db

b=¯b
for b < bi < ¯b. Thus, fixing valuation vi,t, let π′(b|vi,t) =
dπ(b|vi,t)
db . As π′(b|vi,t) is a continuous function in b, and when b∗ satisfies π′(b∗|vi,t) = 0, for all
b < b∗ < b, π′(b|vi,t) < 0, π′(v|vi,t) > 0. The derivative π′(b|vi,t) exhibits a single crossing property
to x-axis in ( b, π′(b)) plane.
Given that the function π′(b|vi,t) is continuous and crosses the x-axis only once, the first-order
condition is sufficient. This implies, the bid bi,t which satisfies the first order condition described
in Equation (2) is the unique maximizer of the expected payoff function π(b|vi,t).
8.6. Estimation Details of Quality Score Distributions
Figure 9 shows the histogram of the mean-centered individual quality scores, demonstrating that
a normal approximation for these scores is appropriate.
Figure 9 Histogram of Daily Quality Score Variations

44 Zhu and Song:Information Disclosure in Auctions
8.7. Empirical Bid Distribution and Estimated V aluation Distribution for
Bid-constructing Bidders
Figure 10 displays the estimated value density for the bid-constructing bidders. The estimated
valuation distribution approximates a bimodal distribution. This aligns with the bimodal bid dis-
tribution, detailed in Figure 11. The bimodal distribution suggests that there might be further
segmentation of bidders within the bid-constructing bidders (e.g. high types and low types), a
phenomenon similarly documented in Hern´ andez et al. (2020).
Figure 10 Valuation Density of Bid-constructing Bidders
Figure 11 Bid-constructing Bidders’s Empirical Bid Density

Zhu and Song:Information Disclosure in Auctions 45
8.8. Estimated V aluation Bounds for Bid-adhering Bidders
Figure 12 displays the estimated bounds for bid-adhering bidders. The blue line represents the
lower bound of the value CDF, and the red line represents the upper bound of the value CDF.
Figure 12 CDF of Lower and Upper Bounds for Bid-adhering Bidders Valuation

46 Zhu and Song:Information Disclosure in Auctions
8.9. Bid-adhering Bidders Bidding Pattern
Figure 13a presents two bidding pattern from bid-adhering bidders, supporting a probabilistic
bidding model.
(a) Bidding Pattern of Bidder A
* Figure 13a displays the bidding pattern of a
bid-adhering bidder, referred to as bidder A. Among 37
bid-changing events, bidder A adhered to the bid
recommendation 9 times, with a bid-adhering rate of
24.32%.
(b) Bidding Pattern of Bidder B
* Figure 13b displays the bidding pattern of a
bid-adhering bidder, referred to as bidder B. Among 103
bid-changing events, bidder B adhered to the bid
recommendation 4 times, with a bid-adhering rate of
3.88%.
Figure 13 Submitted Bids and Observed Bid Recommendations for Bid-adhering Bidders

Zhu and Song:Information Disclosure in Auctions 47
8.10. Data-driven Polynomial Strategy under Polynomial Bidding Model for
Bid-adhering Bidders
Figure 14 presents the fitted polynomial bidding strategy using both the lower- and upper-bound
valuation distributions, along with observed bids from bid-adhering bidders. To estimate this strat-
egy, we generate 10,000 valuation samples from the estimated bounds and match them to bid
samples in increasing order, assuming that bidders with higher valuations place higher bids. The
polynomial model is fitted separately for both lower- and upper-bound valuations.
Figure 14 Fitted polynomial bidding model for bid-adhering bidders
