---
title: 'Adaptive Ad Load Design for Sponsored Search Markets: Evidence, Theory, and Deployment'
url: https://arxiv.org/abs/2607.14418
category: consumer-behavior
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Mohammad Rashid
- Hema Yoganarasimhan
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.14418
pages: 54
chars: 140492
fetched_at: '2026-11-08T12:58:33+00:00'
kb_version: 1
---

# Adaptive Ad Load Design for Sponsored Search Markets: Evidence, Theory, and Deployment

Adaptive Ad Load Design for Sponsored Search Markets: Evidence,
Theory, and Deployment
Mohammad Rashid ∗
University of Washington
Hema Yoganarasimhan∗
University of Washington
July 17, 2026
Abstract
Ad-load design is a central supply-side decision in sponsored search: more sponsored slots can
raise revenue, but may crowd out organic results and degrade user outcomes. We study this trade-off
using a large-scale randomized field experiment on an Android app store, where over five million users
are exposed to one through six sponsored slots. Increasing ad load raises revenue by up to 43%, but
reduces total search conversions by up to 5% and daily engagement by up to 2.2%. These average effects
mask substantial heterogeneity: additional slots generate large revenue gains for high-ad-conversion
queries, but little or negative marginal revenue for low-conversion queries. The trade-off also shifts
within query as advertiser composition changes, such as brand-advertiser presence. Motivated by these
findings, we design and deploy a novel adaptive algorithm –exploration-augmented Locally Adaptive
Ad Load (e-LAAL). e-LAAL combines LAAL, a model-free query-level decision rule that updates
ad-load recommendations using recent outcomes, with static exploration arms that maintain support and
provide fixed-policy counterfactual benchmarks. We provide a finite-time dynamic-regret guarantee for
the e-LAAL architecture. In a platform-level production deployment serving 22.3 million users and 77.6
million searches, e-LAAL improves the empirical revenue–conversion trade-off relative to deployed static
benchmarks and outperforms uniform and historical query-dependent static benchmarks.
Keywords:Digital advertising, Adaptive algorithms, Sponsored search, Ad load
∗We would like to thank the participants of the PhD workshop at the University of Washington and the 2026 UW-UBC conference
for their comments. We are also grateful to Simha Mummalaneni, Omid Rafieian, Ken Wilbur, Zikun Ye, and Dennis Zhang
for their detailed feedback, which has significantly improved the paper. Please address all correspondence to: rashid98@uw.edu,
hemay@uw.edu.
arXiv:2607.14418v1  [cs.LG]  15 Jul 2026

1 Introduction
1.1 Sponsored Search Advertising
Search advertising is one of the central monetization channels in the digital economy. In 2025, search
advertising revenue in the United States reached $114.2 billion, making it the largest format of online
advertising (Interactive Advertising Bureau 2026). The success of sponsored advertising stems from a unique
structural advantage: the precise alignment between user intent and advertiser offerings. Unlike display or
social media advertising, which often rely on interrupting a user’s consumption of content, search ads are
served at the moment a user reveals a specific need or interest through a query. This intent-driven architecture
reduces the friction between the user’s objective and the advertisement, making search ads more relevant, less
intrusive, and often more effective for direct-response objectives than other digital formats. This dynamic
is particularly critical in mobile app marketplaces, where the sheer volume of available products creates a
significant discovery bottleneck. With millions of applications available, search has become the primary
navigation tool for users; Apple reports that nearly 65% of all App Store downloads are initiated directly after
a search query (Apple Ads 2026). The search results page, therefore, becomes a natural advertising surface.
Within this environment, the platform faces an important design problem. While the auction format
determineswhichads are shown and at what price, a more fundamental supply-side decision remains under the
platform’s direct control:ad load design, or determining the number of sponsored slots to display. Increasing
ad load expands paid inventory and can increase short-run platform revenue, but sponsored results may
displace organic results that are more relevant to the user. Excessive ad exposure can therefore degrade search
quality, reduce conversions, and weaken engagement (Kohavi et al. 2012; Carri´on et al. 2023). Ad load design
is therefore a strategic platform-level allocation problem that governs the balance between monetization and
user experience. Yet despite the importance of this supply-side choice, there are no established paradigms for
how platforms should set ad load in sponsored search settings.
1.2 Research Agenda and Challenges
In this paper, we examine the platform’s ad load design problem through three interrelated research questions.
First, what is the causal effect of changing the number of sponsored slots on platform outcomes? We quantify
the marginal impact of additional ads on advertising revenue and conversion,1 which provides the baseline
trade-off underlying ad-load decisions. Second, how do ad-load effects vary across queries and market
conditions? We examine heterogeneity across queries, based on differences in baseline ad conversion potential,
and within queries over time, based on shifts in advertiser composition such as brand participation. Third,
given such heterogeneity, how can platforms design an ad-load policy that tailors sponsored inventory to
context and adapts as market conditions change?
Addressing these questions comes with three challenges. First, identifying the revenue–conversion
trade-off requires exogenous user-level variation in ad load, so outcome differences can be attributed to the
number of sponsored slots rather than selection or demand shocks. Second, heterogeneity analysis requires
1Our empirical setting is an app-store platform (introduced in§1.3), where the natural unit of conversion is an app install.
Throughout this paper, we define conversion as the number of apps installed through search, originating from both sponsored ads and
organic results. We focus on total search conversions as a main outcome because app installs are the platform’s primary matching
outcome and provide immediate search-level feedback on whether users find relevant apps.
1

moderators that are predetermined or independently measured; otherwise, query- or market-level variables may
be endogenous to the realized ad load. Third, policy design requires persistent support for multiple ad-load
levels within each context over time. Without such support, the platform cannot keep updating counterfactual
performance as advertiser entry and exit, budget depletion, bid changes, seasonality, and user intent shift.
Thus, the policy problem is not only to learn which ad load works on average, but to build a theoretically
grounded and deployable adaptive system that continues learning as the market evolves.
1.3 Our Approach and Findings
We study ad-load design on a large Android app-store platform in an Asian country. The platform is a major
mobile distribution channel, with over 70% market share, roughly 40 million monthly users, 5 million daily
active users, and nearly half a million apps. Search is a central discovery mechanism: users install about 2.5
million apps per day from search results pages, of which roughly 50,000 installs are attributed to sponsored
ads. When a user submits a query, the platform runs a real-time Generalized Second-Price auction among
eligible advertisers and displays sponsored results above organic results. The status quo before our intervention
was asingle-ad layout, in which one sponsored result appeared at the top of the page, followed by organic
results. This setting is ideal for studying ad-load design because increasing sponsored slots directly expands
monetizable inventory while displacing organic content.
We address the paper’s research questions in five steps. First, we run a 66-day user-level randomized field
experiment that exogenously varies the number of sponsored slots shown on the search results page. The
experiment covers 10% of the platform’s user base and includes over 5 million users, 26 million searches,
377K sponsored-ad installs, and 15 million organic installs. Users are assigned to six persistent regimes: a
control group, covering 5% of users, receives the status quo one-ad layout, while five treatment groups,𝑇2
through𝑇6, each covering 1% of users, receive fixed layouts with two through six sponsored slots. This design
identifies the causal effects of moving from the status quo to increasingly aggressive ad-load regimes at a scale
large enough to detect both monetization effects and user-side behavioral responses.
The experiment reveals a clear aggregate trade-off. Moving from one ad to six ads increases revenue per
user by 43%, but reduces total conversions per user by up to 5%. Higher ad loads also increase searches per
user by up to 3%, suggesting that users exposed to heavier ad loads may need to search more to find relevant
apps, while reducing daily engagement by up to 2.2% and generating a negative engagement trend among
users exposed to at least four ads per search. Taken together, these results show that additional sponsored
slots raise short-run monetization but degrade user-side outcomes, making ad-load design a multi-objective
optimization problem rather than a simple revenue-maximization problem.
Second, we use the experimental variation to show that the revenue–conversion trade-off is heterogeneous
across queries and over time. To study cross-query heterogeneity, we focus on the top 10,000 queries by
advertising conversion count and partition them into three equally sized segments (Low, Medium, High) based
on advertising conversion rate in the control condition, where the sponsored ad always appears in the first
position. Across all three segments, higher ad loads reduce conversions, but revenue effects differ sharply:
in the Low segment, additional slots do not generate incremental revenue, whereas in the High segment,
extra slots generate substantial incremental revenue. Thus, the value of an additional sponsored slot depends
critically on query-level advertiser quality: a uniform “always show 𝑖 ads” rule misallocates inventory by
2

showing too many ads on queries where ads convert poorly and too few ads where sponsored demand is
valuable. We then examine time variation using brand queries, i.e., branded phrases such as “WhatsApp,” and
find that periods with brand-advertiser presence are associated with higher revenue and conversions, with the
largest gains under high ad loads. This within-query variation shows that the same query can appear on a
different revenue–conversion frontier as advertiser composition changes. These results imply that effective
ad-load design must be both query-sensitive and time-adaptive.
Third, these empirical patterns motivate an adaptive ad-load allocation policy but also highlight why
standard parametric contextual bandits are not a good fit for this setting. Conventional contextual bandits
require a stable reward model over observed contexts, but many reward-relevant states in sponsored search are
partially observed, including advertiser entry and exit, budget depletion, bid changes, app availability, brand
participation, and shifts in user demand. The mapping from query, ad load, and market state to revenue and
conversions is also complex and non-stationary, and ad-load decisions may affect future search behavior, so
context arrivals are not fully policy-invariant. Moreover, per-search exploration schemes such as standard
𝜖-greedy or Thompson sampling do not preserve persistent user-level fixed-policy cohorts, which are needed
to evaluate counterfactual policies such as “always show three ads” when ad load can affect subsequent usage.
Fourth, we therefore design Locally Adaptive Ad Load (LAAL) and its exploration-augmented imple-
mentation, e-LAAL. LAAL is a model-free, query-level, sliding-window policy. For each query–ad-load
pair, it estimates recent mean revenue and total conversions, maps these estimates into a scalarized reward,
and chooses the ad load with the highest estimated value. This design makes the policy both query-adaptive
and time-adaptive: different queries can receive different ad loads, and the same query can receive different
ad loads as recent market conditions evolve. The policy does not require a parametric reward model or full
observability of latent market states; it can react to changes reflected in recent outcomes, even if the source of
the change is not explicitly labeled.
The deployed e-LAAL architecture adds a crucial exploration layer. Rather than randomizing exploration
within a single adaptive arm, e-LAAL runs LAAL on 90% of users while keeping static arms𝐶,𝑇 2,...,𝑇 6
active on the remaining 10%. These static arms provide persistent support for every ad-load level and
contemporaneous fixed-policy counterfactuals. We also provide a finite-time high-probability dynamic-regret
guarantee for e-LAAL. The proof adapts non-stationary bandit arguments to our deployment architecture
by accounting for the fact that exploration is assigned through persistent user-level cohorts, while realized
query-level support for each ad-load arm may deviate from the platform’s designed traffic shares.
As part of this design, we evaluate e-LAAL in a 22-day production deployment. The deployment serves
22.33 million users and 77.60 million searches, with the adaptive LAAL arm alone covering 20.10 million
users and 69.85 million searches. LAAL recommends 3.1 ads per search on average and produces a bimodal
recommendation distribution, often choosing either low ad loads when conversion losses dominate or high ad
loads when revenue gains justify additional sponsored slots. Further, we see that LAAL shifts the empirical
revenue–conversion frontier outward relative to the deployed static ad-load benchmarks. In the static arms,
the familiar trade-off persists: moving from the control condition to the highest ad-load condition increases
revenue per user by more than 40%, but reduces conversions per user by roughly 5%. LAAL preserves
the monetization benefits of high ad loads while substantially mitigating their conversion losses: it delivers
3

revenue essentially identical to the always-5-ads policy (𝑇5), while generating about 3% more conversions
and keeping conversions much closer to the low-ad-load benchmarks. The system-level e-LAAL mixture
remains close to the LAAL arm, indicating that the 10% static exploration layer preserves ongoing learning
and counterfactual support with limited performance cost.
We further unpack the mechanism behind the frontier improvement. Consistent with the heterogeneity
analysis, LAAL recommends fewer ads for low-CVR queries and more ads for high-CVR queries, without hard-
coding these segments into the policy. For non-stationary brand queries, LAAL changes its recommendations
within the same query: when the brand advertiser is absent, the policy shifts toward lower ad loads; when the
brand advertiser is present, it shifts toward higher ad loads.
Finally, we benchmark LAAL against both uniform and query-dependent static policies. Among uniform
policies, the best historical rule selected from the 66-day experiment is 𝑇3, whereas the best uniform rule
during deployment is𝑇5, showing that even the best platform-wide static ad load changes over time. LAAL
outperforms the historical uniform benchmark and weakly dominates the deployment-period uniform oracle
by matching its revenue while delivering significantly higher conversions. A historical query-dependent
benchmark improves over uniform static rules, confirming the value of query sensitivity, but remains below
LAAL during deployment. Relative to an ex post deployment query-dependent empirical oracle, LAAL ’s
empirical regret is close to zero for the highest-volume queries, where recent local estimates are most precise.
1.4 Contributions and Implications
The paper contributes to the literature on monetization in digital platforms, ad-load effects, and adaptive policy
design.
First, from a substantive perspective, we provide large-scale causal evidence on the effects of ad load
in sponsored search and show why the optimal ad load cannot be reduced to a single platform-wide or
time-invariant query-level rule. Our 66-day experiment exposes over five million users to an unusually wide
range of ad loads, from the status quo single-ad layout to a six-ad layout that covers most of the first page with
sponsored results. This design allows us to quantify the revenue–consumer-experience trade-off induced by
ad load, as reflected in conversions and engagement, over a scale and time horizon not previously studied in
sponsored search. We further show that this trade-off is highly heterogeneous: query-level advertiser quality
determines whether additional sponsored slots generate incremental revenue, while market-state shifts, such
as brand-advertiser presence, can move the same query to a different revenue–conversion frontier. To our
knowledge, this is the first study to provide causal evidence on sponsored-search ad-load effects over this
range of ad loads while also documenting that the optimal ad load varies both across queries and over time.
Second, from a methodological perspective, we provide a constructive and theoretically grounded solution
to the adaptive ad-load allocation problem. LAAL is a model-free, query-level decision rule that uses
sliding-window estimates of recent revenue and conversion outcomes to adapt ad load across queries and over
time. e-LAAL is the deployable architecture that augments LAAL with persistent static exploration arms; these
arms preserve support for each ad-load level and provide contemporaneous fixed-policy counterfactuals while
the adaptive arm exploits recent evidence. In other words, e-LAAL is the practical implementation framework
a platform can adopt directly: it implements LAAL in production, optimizes ad load at scale, and continues
to collect the experimental data needed for ongoing learning and evaluation. We also provide a finite-time
4

high-probability dynamic-regret bound for e-LAAL that explicitly accounts for the gap between designed
traffic shares and realized query-level support. Empirically, in a platform-level production deployment serving
over 22 million users and 77 million searches, LAAL improves the revenue–conversion frontier, delivers
revenue comparable to high-ad-load static policies while preserving conversions closer to low-ad-load policies,
and adapts in economically sensible ways by recommending fewer ads when advertiser quality is low and
more ads when sponsored demand is valuable.
Finally, from a managerial perspective, the results show that ad load decisions in sponsored search markets
should neither be set platform-wide nor governed by a time-invariant query-level rule. Effective ad-load
design must be both query-sensitive and time-adaptive: the query determines the baseline value of additional
sponsored slots, while current market conditions determine whether that value has shifted. The 22-day e-LAAL
deployment demonstrates that this principle is operationally feasible at a production scale. The approach is
also practical and portable because it does not require a platform-specific parametric reward model, complete
observability of advertiser states, or extensive engineering. Instead, it relies on recent local outcomes and a
small set of fixed exploration cohorts, making it adaptable to sponsored search and e-commerce platforms that
track query-level revenue and conversion outcomes. More broadly, the paper shows that platforms can ease
the revenue–consumer-experience trade-off not only through auction design, pricing, ranking, or targeting, but
also by dynamically controlling the supply of sponsored attention.
2 Related Literature
Our paper contributes to four complementary streams at the intersection of marketing, economics, and computer
science: (i) sponsored-search market design, (ii) empirical work on advertising and ad-load trade-offs, (iii)
ad-load allocation systems, and (iv) adaptive decision-making with contextual bandits.
First, our paper connects to the large literature on auction design in sponsored search and its implications
for platform revenue. Early work in this area examines how auction formats and allocation rules affect
outcomes and revenue (Edelman et al. 2007; Varian 2007; Lahaie and Pennock 2007; Athey and Ellison
2011). Building on Myerson (1981), a central line of research has studied how to set optimal reserve prices in
advertising auctions to improve platform revenues (Yuan et al. 2014; Leme et al. 2016; Ostrovsky and Schwarz
2023). This literature primarily focuses on optimizing pricing and ranking mechanisms for a given ad load.
Apart from auction design, more recent work has examined how real-time bidding, behavioral targeting, and
privacy regulation reshape allocation, pricing, and platform revenue in digital advertising markets (Sayedi
2018; Yao and Mela 2011; Rafieian and Yoganarasimhan 2021; Goldfarb and Tucker 2011). We complement
this literature by focusing on ad load as a supply-side design choice. We empirically quantify how ad load
affects platform revenues and user-side outcomes, propose an adaptive framework that the platform can use to
decide how many sponsored slots to display for any given search query at a given point in time, and evaluate
that choice using platform-level outcomes rather than advertising metrics alone. Our work thus extends this
research by endogenizing the amount of sponsored inventory shown to users for any given query, and by
characterizing how this operational lever can improve platform performance.
Second, our work contributes to the literature that measures the effects of advertising on consumer behavior.
Early work on TV ads finds that reducing advertising time increases audience size (Wilbur 2008; Wilbur et al.
2013). More recent work has focused on digital platforms. Goli et al. (2025a) document consumer sensitivity
5

to ad load in a music streaming platform and find that heavier ad loads reduce user engagement and increase
churn in the long run, with heterogeneous effects across age groups. In an e-commerce setting, Moshary
(2025) compares two conditions—no ads and a default ad load—and finds that the number of transactions and
commission revenue are higher in the no-ads condition, but that this increase in transactions does not offset
the loss of advertising revenue. Finally, in a search engine sponsored-search setting, Sahni and Zhang (2024)
find that reducing average ad load in the mainline above organic results from 1 to 0.83 reduces ad revenue but
does not significantly affect clicks.
In our setting, we vary ad load from one to six and find a clear revenue–conversion trade-off: higher ad loads
increase ad revenue but reduce overall app installs and engagement. Beyond the main effects, we document that
these effects are heterogeneous across queries and over time, implying that the revenue–conversion trade-off
can shift across queries and market states. Moreover, while the earlier papers mainly document ad-load effects,
we design and deploy an adaptive ad-load allocation policy that balances revenue and conversions, and present
results from this platform-level deployment. Thus, our main goal is not just to show that these trade-offs
exist or to quantify them; rather, we propose a methodological framework that decision-makers can use to
adaptively allocate ad load in sponsored search settings.2
Our work also relates to the literature that examines how to optimally allocate ad load in advertising
markets. In sponsored search, Broder et al. (2008) study when to show no ads based on predicted click-through
rates, while later supervised and whole-page optimization approaches use historical click patterns or predicted
page-level click and revenue outcomes to determine how many ads to display (Wang et al. 2011; Zhang et al.
2018). Relatedly, Kim et al. (2012) provide a theoretical analysis of how many sponsored slots a platform
should offer under GSP when the objective is advertising revenue. These papers are important precursors,
but they primarily rely on predicted user-response models based on observational data, historical logs, or
analytical models. In contrast, we first run a large-scale randomized field experiment that exogenously varies
ad load from one to six ads, allowing us to causally quantify the revenue–conversion trade-off and show that it
varies across queries and over time. We then use these findings to design and deploy a model-free adaptive
policy with persistent static exploration arms, contemporaneous fixed-policy counterfactuals, and a finite-time
dynamic-regret guarantee.
More recent work treats ad load as a platform-level decision, incorporating user-engagement proxies
through multi-objective rewards, constrained optimization, off-policy learning, or doubly robust estimation. In
feed allocation and social-media ad supply, related work optimizes ad exposure within an ongoing stream of
organic content, using signals such as feed position, session context, user ad tolerance, ad fatigue, and long-run
engagement (Liao et al. 2021; Sagtani et al. 2023; Yan et al. 2020; Shi et al. 2024). In audio streaming, Goli
et al. (2025b) studies ad load as a personalized exposure problem, using long-run experiments to balance
advertising revenue, subscription revenue, and user consumption. These studies establish ad load as an
important operational lever, but their settings differ from sponsored search in both the decision unit and the
main source of heterogeneity. In feeds and streaming, the platform manages ad exposure over a consumption
path, and heterogeneity is primarily user- or session-level. In sponsored search, by contrast, the query is the
central state variable: it reveals user intent, determines which organic results are displaced, and shapes the set
2Indeed, we show that these trade-offs can be brittle and change over time, and that choosing a fixed ad load based on a historical
experiment can lead to suboptimal outcomes; see§8.1.
6

and quality of eligible advertisers. Search platforms also observe immediate search-level outcomes, such as
conversions and revenue, that can be linked directly to the ad-load decision. Thus, ad-load methods designed
for feed or streaming environments do not directly translate to sponsored search, where the key problem is to
adapt the number of sponsored slots across queries and over time as advertiser composition changes.
Finally, our paper relates to and contributes to the literature on contextual bandits and adaptive experi-
mentation (Lattimore and Szepesv´ari 2020). In a standard contextual-bandit problem, the decision-maker
observes a context, chooses an action, and observes only the reward associated with the chosen action. A
large theoretical literature studies algorithms such as LinUCB and Thompson sampling, typically under stable
reward mappings and parametric or linear structures in the relationships among contexts, actions, and rewards
(Li et al. 2010; Chu et al. 2011; Abbasi-Yadkori et al. 2011; Agrawal and Goyal 2013). Related work extends
bandit methods to non-stationary environments using sliding windows, discounting, or variation-budget regret
criteria (Garivier and Moulines 2011; Cheung et al. 2019; Russac et al. 2019). Closer in application, Ye et al.
(2023) develop and field-test a deployable contextual-bandit policy for new-ad cold start that leverages an
incumbent CTR/CVR prediction and auction system. Our setting differs in how exploration must be engineered
for deployment. We maintain parallel static ad-load arms because they provide persistent, contemporaneous
counterfactuals for fixed policies of the form “always show𝑖 ads.” This design introduces a complication
absent from canonical bandit models: because ad load can affect users’ subsequent search behavior, the
realized query-level support in each arm need not match the platform’s designed traffic weights. We therefore
provide regret bounds for the parallel-static-cohort exploration scheme, explicitly allowing realized support
to deviate from intended allocation shares. We also evaluate the approach in a real production deployment,
connecting the theoretical exploration design to platform-scale implementation.
3 Setting and Field Experiment
3.1 Setting: Android App Store
Our data come from a leading Android app store in an Asian country that commands over 70% of the market
share. On the demand side, the app store attracts around 40 million monthly users and 5 million daily active
users, while on the supply side, it features nearly half a million applications developed by over eighty thousand
developers. The platform’s primary source of income is advertising within the store, with the most prominent
form beingsponsored search ads, which is the focus of this study. On average, users install about 2.5 million
apps daily from search results pages, with about 50,000 of those installs attributed to sponsored ads.
When a user submits a search query in the app store, the platform runs a real-time Generalized Second-
Price (GSP) auction (Edelman et al. 2007) among eligible ads, employing a cost-per-install payment model.
Under the platform’s standard setting – referred to as thesingle-ad layout– one ad slot is allocated to the
highest-ranked bidder. This sponsored ad is displayed at the top of the search results page, followed by a
rank-ordered list of organic results. Users can scroll down to view additional organic listings.
An example of the single-ad layout is illustrated in Figure 1a. On a typical smartphone with a 6.3–6.5
inch display (e.g., a Pixel 9), users can see eight listings (ads or organic) without scrolling if the search query
is non-brand. Abrand queryis a search query explicitly referring to a particular application or brand. An
example of a brand query isWhatsApp, while an example of a non-brand query isFlights. In the case of a
7

brand query, the brand result is displayed with additional details (e.g., application screenshots), occupying two
additional rows and thus reducing the number of visible items to approximately six (see Web Appendix§A for
examples of brand query layouts).
3.2 Field Experiment on Number of Ad Slots
Our analysis leverages data from a large-scale randomized field experiment conducted on the platform’s search
results page. The experiment aims to examine how varying the number of sponsored ads displayed impacts
user-, advertiser-, and platform-level outcomes. The experiment ran for 66 days starting from September 2023.
The experiment consisted of approximately 10% of the platform’s user-base. Users in the experiment were
randomly assigned to one of six conditions, as follows:
• Control Group (𝐶):Users in the control group experience thesingle-ad layout, displaying one sponsored
ad per search query. This group comprises 5% of the user base.
• Treatment Groups (𝑇𝑖):We have five distinct treatment groups, 𝑇2,𝑇 3,𝑇 4,𝑇 5,𝑇 6. Users assigned to
treatment group𝑇𝑖 are exposed to ani-ad layout, where the top 𝑖 slots are assigned to ads for each search
(based on the same GSP auction mechanism). An illustrative example of the three-ad layout, corresponding
to users in the𝑇3 treatment group, is shown in Figure 1b. Each treatment group comprised approximately
1% of the platform’s user base.
Users are assigned to experimental conditions by hashing each device’s unique Android identifier with a
deterministic, salt-aware function to prevent collisions with other experiments. This method yields a random
but reproducible treatment assignment. Throughout the experiment, user assignment to the experiment
condition remains fixed, ensuring consistent exposure to the treatments/control.3
(a) Single-Ad Layout
 (b) Three-Ad Layout
Figure 1: Comparison of single-ad versus three-ad sponsored search layouts.
3Although each treatment condition targets a specific number of sponsored ad positions, the actual number of ads shown per
search is contingent upon the availability of eligible bidders, meaning fewer ads could be displayed if bidder supply is insufficient (i.e.,
realized ad load could be lower than treatment condition). However, such discrepancies are rare across all treatments in our data
because the ad market is sufficiently thick.
8

Overall, the experiment contains observations from 5,057,952 unique users who performed 26,326,936
searches, installed 377,425 ads, and 15,514,923 organic apps, over the 66-day experiment period.
3.3 Data
Our data are at the impression-level. An impression is any search result displayed to a user in response to their
query. Thus, each organic link or ad shown on the first page counts as a separate impression, and if the user
scrolls to subsequent pages, every additional result shown is likewise recorded as its own impression.
For each impression in the data, we observe the following variables:
•Search ID (𝑠): The unique identifier of a search.
• Query (𝑞): The search term used by a user. We denote the query associated with Search ID 𝑠 by𝑞𝑠. Our
dataset contains 4,045,348 unique queries, with the top 2,000 accounting for 60% of all searches. This
concentration is consistent with prior work on search platforms, where a small share of keywords generates
most searches (e.g., Yoganarasimhan (2020)). Web Appendix§B.1 reports the full cumulative distribution
of query search counts. Most queries belong to the Social Media, Games, and Tools categories.
• Device ID (𝑢): The unique identifier of the user, associated with the Android device. We denote the user
associated with search ID𝑠by𝑢 𝑠.
•Experiment Condition (𝑒): The experiment condition assigned to a user, drawn from the set
E={𝐶,𝑇 2,𝑇 3,𝑇 4,𝑇 5,𝑇 6}. We denote the experimental condition associated with search𝑠 by𝑒𝑠 =𝑒(𝑢 𝑠).
• Timestamp (𝑡): Exact time when the result is shown to the user. We denote the time of a search request𝑠
by𝑡𝑠.4
• App ID: The unique identifier of the apps shown on the platform. We observe 141,716 distinct apps in our
data. The top 20% of ads receive 90% of ad impressions, while the top 20% of apps receive 99% of total
impressions of the search page. This reflects how relevance-based organic ranking algorithms amplify
popular items more strongly than auction-driven ad allocations do. The cumulative distribution of app
impressions is shown in Web Appendix§B.2.
•Position (𝑝): Rank position of the app in search results.
• Is Sponsored: A binary flag indicating whether the impression/app appears as an ad. We have ad
impressions for 664 unique advertisers; the most frequent categories among sponsored apps are Finance,
Shopping, and Entertainment.
• Conversion Indicator (Conv𝑠,𝑝 ): A binary indicator, defined at impression level, showing whether the user
installed the app in position𝑝for search ID𝑠.
We denote the sum of conversion outcomes (sum over all positions) of search ID𝑠by Conversion𝑠:
Conversion𝑠 =
∑︁
𝑝
Conv𝑠,𝑝 (1)
Please see Web Appendix§B.2 for the cumulative distribution of app conversions.
• Revenue (Rev𝑠,𝑝 ): Revenue from the advertiser upon sponsored app installation, in position𝑝 for search
4Following a search, all the results displayed on the first page of the results (both ads and organic listings) share the same timestamp
𝑡𝑠. If the user navigates to the next page in a few minutes, the time at which s/he sees the second page of results is denoted as the
timestamp for the impressions/listings in the second page, and so on.
9

ID𝑠. By definition, organic listings generate zero revenue; for ads, revenue is determined by the GSP
mechanism discussed earlier. To preserve the platform’s privacy, we multiply all revenue numbers by an
undisclosed multiplier. We denote the sum of revenue for search ID𝑠by Revenue 𝑠,
Revenue𝑠 =
∑︁
𝑝
Rev𝑠,𝑝 (2)
4 Effect of Number of Ad Slots on Conversion and Revenue
We first describe the main effect of the number of ad slots on various outcomes in§4.1 and then quantify the
heterogeneity in treatment effects across queries and time in§4.2.
4.1 Main Effects
Table 1 reports summary statistics of the various outcomes by experimental condition. The top panel shows
the realized ad load and the number of users in each condition. We see that the realized ad exposure closely
tracks the intended design (top row). Next, we focus on the two main outcomes of interest, shown in the
middle panel of Table 1.Revenue per Useris total advertising revenue from all the users in the experiment
bucket divided byUser Countin that bucket.Conversion per Useris the total number of conversions from ads
and organic listing divided byUser Count. We see thatRevenue per Userincreases monotonically with ad
load: from 35.72 under𝐶 to 51.18 under𝑇6 – a 43% improvement relative to control. In contrast,Conversions
per Userdeclines monotonically from 3.19 (𝐶) to 3.03 (𝑇 6), a 5% reduction.
Table 1: Summary Statistics of the Experiment
𝐶 𝑇 2 𝑇3 𝑇4 𝑇5 𝑇6
Avg. Ad Load 1.00 2.00 3.00 3.99 4.94 5.88
User Count 2,528,428 505,193 505,016 506,335 506,713 506,267
Revenue/Usera 35.72 41.61 44.54 46.39 49.47 51.18
Conversion/User 3.19 3.15 3.13 3.10 3.06 3.03
Daily Eng. (%) 4.95 4.92 4.89 4.87 4.85 4.84
Searches/User 5.14 5.16 5.30 5.31 5.28 5.31
Note: aScaled by an undisclosed multiplier.
To assess statistical significance, we estimate separate user-level regressions for outcomes
𝑌∈{Revenue, Conversion}:
𝑌𝑢 =𝛼 𝑌 𝐶 +
6∑︁
𝑖=2
𝛼𝑌 𝑇𝑖 1{𝑒(𝑢)=𝑇 𝑖} +𝜀𝑌 𝑢,(3)
where:
•𝑌 𝑢 is the outcome of user𝑢such that𝑌 𝑢= ˝ 𝑠:𝑢𝑠=𝑢𝑌𝑠
•𝛼 𝑌 𝐶 =E[𝑌 𝑢|𝑒(𝑢)=𝐶]is the control mean for outcome𝑌
10

•For treatment conditions𝑇 𝑖,𝛼𝑌 𝑇𝑖 measures the deviation from control as follows:
𝛼𝑌 𝑇𝑖 =E[𝑌 𝑢|𝑒(𝑢)=𝑇 𝑖]−E[𝑌 𝑢|𝑒(𝑢)=𝐶]=ATE 𝑌(𝑇𝑖).(4)
We present the estimation results from Equation (3) in Table 2. It confirms the previously observed pattern:
for revenue, treatment effects are positive, increasing in ad load, and highly significant; for conversion, effects
are negative, more pronounced at higher ad loads, and likewise highly significant. These findings suggest an
important trade-off for the platform: more ad slots raise revenue while reducing total conversions.
We now examine how ad load changes consumers’ behavior and whether consumers in our setting are
averse to advertising. To answer these questions, we consider two platform usage metrics, shown in the last
two rows of Table 1. For each day and experimental condition, we calculate the proportion of assigned users
who performed at least one search.Daily Engagement, defined as the mean of these daily proportions over
the duration of the experiment, declines from 4.95% in 𝐶 to 4.84% in𝑇6 (a 2.2% relative decrease), with
significant differences versus control across all treatment conditions. Within high-ad-load groups (𝑇4–𝑇6),
we also detect a modest but significant downward trend over time (See Web Appendix§C.1 for a detailed
analysis). This result shows that ad load harms platform usage, and consumers with higher ad loads are less
willing to use the search feature. This finding is similar to that of Goli et al. (2025a), who report a near-linear
decline in total hours spent on an audio streaming platform as ad load increases. At the same time,Searches
per Userrises from 5.14 (𝐶) to 5.31 (𝑇6), a 3.3% increase despite the fact that the unique number of active
users decreases with higher ad load. This is likely because high ad exposure degrades the quality of search
results; users cannot find the desired app at the top, prompting additional searches. A similar pattern of higher
search volume with a degraded search experience has also been observed in Bing search experiments (Kohavi
et al. 2012). We present a detailed analysis of this effect of ad load on search behavior (including regressions)
in Web Appendix§C.2.
Table 2: Effect of Ad Load on Revenue and Conversion
Revenue Conversion
𝐶35.722 ∗∗∗ (0.255) 3.192 ∗∗∗ (0.005)
𝑇2 5.890∗∗∗ (0.626) -0.046 ∗∗∗ (0.013)
𝑇3 8.818∗∗∗ (0.593) -0.063 ∗∗∗ (0.015)
𝑇4 10.669∗∗∗ (0.507) -0.096 ∗∗∗ (0.016)
𝑇5 13.746∗∗∗ (0.524) -0.133 ∗∗∗ (0.013)
𝑇6 15.455∗∗∗ (0.545) -0.165 ∗∗∗ (0.013)
Obs. 5,057,952 5,057,952
𝑅2 <0.001<0.001
Note:The 𝐶 row reports the mean outcome in the control condition. Rows𝑇2,...,𝑇 6 report differences relative to𝐶. Standard errors
in parentheses.∗∗∗𝑝 <0.001.
In sum, increasing the number of ad slots produces a monotonic increase in revenue and a monotonic
decrease in total conversions, which frames a tradeoff in the platform’s design problem. Meanwhile, ad load
hurts consumers’ experience and platform usage. In the remainder of the paper, we focus on conversion
as the main metric for consumer satisfaction for two reasons. First, app installations are the platform’s
11

primary matching outcome: conversions directly capture whether users find and adopt relevant apps. Second,
conversions are observed at the search level and therefore provide immediate feedback that can be directly
linked to search-level decisions.
4.2 Heterogeneity in the Revenue–Conversion Trade-off
So far, we have shown that more ad slots generally increase revenue and decrease conversions. We now
examine how the revenue-conversion trade-off varies across queries and over time.
4.2.1 Heterogeneity Across Queries
We now examine how treatment effects vary across queries. We first segment queries into three buckets based
on the quality of their ads. We select the top 10,000 queries based on advertising conversion count and rank
them by their control group ad conversion rate. Formally, for query𝑞 we define ads’ conversion rate based on
their performance in the control condition as follows:
AdsCVR𝑞 =E[Conv 𝑠,1|𝑒 𝑠 =𝐶,𝑞 𝑠 =𝑞],
where Conv𝑠,1 is the conversion indicator of the (single) sponsored position in the control group. We only use
the control condition for labeling ads because it keeps the position of the ad fixed to the first position.
We then partition queries based on AdsCVR into three equal-sized segments as follows:𝐾1=lowest 3,333 ,
𝐾2 =middle 3,334 , and 𝐾3 =highest 3,333 . 𝐾1 consists of the set of queries with the lowest advertising
conversion rate under the control condition, while𝐾3 consists of the highest ad conversion rate queries. We
use three segments to balance interpretability and statistical precision: each segment has sufficient search
volume for precise estimation while still capturing meaningful variation in ad load effects. See Web Appendix
§D for the summary statistics of these three segments of queries.
To estimate how ad load affects outcomes within each segment, we run the following query–fixed-effects
regression for𝑌∈{Revenue,Conversion}:
𝑌𝑠 =𝛼 𝑌 𝑞𝑠 +
3∑︁
𝑘=1
6∑︁
𝑖=2
𝛽𝑌 𝑘,𝑖 1{𝑞𝑠∈𝐾 𝑘}1{𝑒 𝑠 =𝑇𝑖} +𝜀𝑌 𝑠 (5)
𝑌𝑠 is the observed outcome for search𝑠. The query fixed effect 𝛼𝑌 𝑞𝑠 absorbs all baseline differences across
queries. Thus,𝛽 𝑌 𝑘,𝑖 isolates the incremental effect of treatment𝑇𝑖 relative to control within segment𝑘.
We report the estimation results from Equation (5) for all three segments of queries in Table A5 in Web
Appendix§D. To aid interpretation, we plot the estimated effects in Figure 2 after normalizing each segment’s
treatment effects by its own control mean (so a value of 1.10 corresponds to a 10% increase relative to the
segment’s control mean). 5 We observe two patterns. First, we find that conversion decreases significantly
as ad load increases in all three segments. Further, the magnitude and slope of this decline are broadly
similar across all three segments. However, revenue displays strong heterogeneity across segments. In the low
segment (𝐾1), additional ad slots do not raise revenue (on average), and in fact lead to significantly negative
5Points in Figure 2 show the treatment-effect estimates from Equation (5). Confidence intervals are reported separately for each
treatment effect. Although confidence intervals overlap across some ad-load conditions, pairwise tests confirm that revenue effects
increase significantly with ad load in the High-CVR segment.
12

effects for𝑇3 and𝑇4. In the medium segment (𝐾2), revenue becomes positive and significant at higher ad loads.
In the high segment (𝐾3), revenue rises sharply and monotonically with the number of ads. These patterns
reveal a sharp asymmetry in how the top advertiser’s conversion rate mediates the effect of additional ad slots.
For queries with low advertiser quality, additional ads fail to generate incremental paid installs. For such
queries, more ads displace relevant organic results, depressing both revenue and conversion.6 In contrast, for
queries with high-quality advertisers (who have high conversion rates), increasing ad load unlocks substantial
revenue gains, albeit with expected conversion losses.
This contrast implies an important takeaway for platform design. A “one-size-fits-all” ad load policy is
inefficient: showing many ads universally can backfire for queries with low-quality ads. As such, platforms
should adopt query-sensitive allocation rules that limit exposure when advertiser quality is poor and expand
ad supply when strong advertisers are present. Such query-specific or adaptive ad load allocation can improve
monetization efficiency while reducing user-side friction caused by irrelevant ad clutter.
(a) Normalized Conversion (Control=1)
 (b) Normalized Revenue (Control=1)
Figure 2: Treatment effects by Ad CVR segment.
4.2.2 Heterogeneity Over Time
We now examine how the revenue-conversion trade-off varies over time using the presence or absence of
brand advertising as a salient time-varying market-state. In this analysis, we focus onbrand queries– queries
which refer to a specific brand/app, e.g., WhatsApp. We first split the 8,561 brand queries in our data into two
groups:
• Brand-Active Queries, where the brand app advertises on at least one day during the experiment (709
queries).
•Brand-Inactive Queries, where the brand app never advertises (7,852 queries).
Figure 3 compares the revenue–conversion frontier across these two groups using the same axis scaling
in both panels.Brand-Active Queriesexhibit larger revenue gains and smaller conversion losses relative to
Brand-Inactive Queries, resulting in a noticeably steeper frontier.
6One reason revenue can decline rather than merely remain flat is that additional sponsored slots may dilute attention to the top
sponsored result: when low-quality ads occupy more of the visible page, users appear less likely to convert on the first sponsored
listing, and the additional lower-ranked ads do not generate enough paid installs to offset this loss.
13

However, query-specific differences could still confound the comparison above, i.e.,Brand-Active Queries
can be systematically different fromBrand-Inactive Queries. We therefore focus on the 709Brand-Active
Queriesand compare search-level outcomes when the brand ad is present (Brand-On) vs. absent (Brand-Off).
Let𝐵𝑠∈{0,1} indicate whether the brand ad at search ID𝑠 is shown. Figure 4 shows the distribution of the
share ofBrand-Onsearches by query among theBrand-Activeset. We see significantwithin-queryvariation
in the presence/absence of brand-ads for almost all queries. We use this variation to measure how outcomes
differ between Brand-On and Brand-Off states under each ad load condition. Specifically, we run the following
regressions for𝑌∈{Revenue,Conversion}controlling for query-condition fixed effect:
𝑌𝑠 =𝛼𝑌 𝑞𝑠,𝑒𝑠 +𝜃 𝑌 𝑒𝑠1{𝐵𝑠 =1} +𝜀 𝑌 𝑠 (6)
where𝛼𝑌 𝑞𝑠,𝑒𝑠 denote query-condition fixed effects. Thus,𝜃𝑌 𝑒𝑠 measures the within-query change in𝑌 when
the brand ad is displayed under condition𝑒𝑠. Table 3 reports ˆ𝜃𝑌 𝑒 estimates from this analysis. We see that
Brand-On searches have higher revenue and conversion than Brand-Off searches across all ad-load conditions,
and the revenue gap is larger at higher ad loads. In other words, brand-advertiser presence is associated with
a more favorable revenue–conversion frontier, particularly under higher ad loads.7 Figure 5 visualizes the
revenue and conversion gaps associated with brand presence. Revenue rises sharply underBrand-Onwhile
conversion declines only slightly, illustrating that brand activity meaningfully softens the tradeoff. This finding
parallels the cross-query heterogeneity documented in§4.2.1: brand participation raises the quality of the
sponsored slate for a query, effectively moving the query toward the high-advertiser-quality regime in which
additional sponsored slots are more valuable.
(a) Brand-Active Queries (709 Queries)
 (b) Brand-Inactive Queries (7,852 Queries)
Figure 3: Revenue-Conversion tradeoff based on brand activity. Each point corresponds to an experimental
condition. The Conversion axis measures total search conversions, i.e., app installs originating from both
sponsored ads and organic results; the Revenue axis measures total ad revenue.
Taken together, these results show that brand activity systematically affects the revenue–conversion frontier,
even within the same query. When the brand advertises, the marginal cost of showing additional ads is
7Previous studies have attributed these improvements to the brand ad cannibalizing the organic brand result (Simonov et al. 2017)
14

Figure 4: Distribution ofBrand-Onsearches withinBrand-Active Queries
Table 3: Brand effect by condition with Query×Condition fixed-effects
Revenue Conversion
C 93.05 ∗∗∗ (4.75) 0.104 ∗∗∗ (0.015)
T2 116.36 ∗∗∗ (8.11) 0.100 ∗∗∗ (0.018)
T3 128.70 ∗∗∗ (9.73) 0.111 ∗∗∗ (0.017)
T4 132.31 ∗∗∗ (8.82) 0.115 ∗∗∗ (0.013)
T5 139.49 ∗∗∗ (9.17) 0.127 ∗∗∗ (0.014)
T6 140.03 ∗∗∗ (7.95) 0.121 ∗∗∗ (0.013)
Query-Condition FE✓ ✓
Obs. 2,253,506 2,253,506
𝑅2 0.103 0.016
Notes:Each column reports ˆ𝜃𝑒 from specification 6. Standard errors in parentheses are clustered at the query level. ∗∗∗𝑝 <0.001,
∗∗𝑝 <0.01,∗𝑝 <0.05.
(a) Conversion per search:Brand Offvs.Brand On.
 (b) Revenue per search:Brand Offvs.Brand On.
Figure 5: The effect of brand advertising on left: conversion and right: revenue. The gaps equal to the brand
effect estimates from Table 3.
15

substantially lower: revenue gains grow while conversion losses shrink. For platforms, this highlights the
importance of incorporating time-varying market conditions into ad-load decisions. A static, time-invariant
allocation rule will systematically misallocate ad load (e.g., showing too few ads when brands are actively
advertising and too many when they are not). Effective ad-load design, therefore, requires adaptive mechanisms
that respond directly to shifts in advertiser presence and market composition.
Summary and implications for policy design.The heterogeneity results show that the revenue–conversion
frontier is neither uniform across queries nor stable over time. Across query segments, the marginal conversion
loss of adding sponsored slots is broadly similar, but the marginal revenue effect varies sharply with advertiser
quality. We find that additional slots generate little incremental sponsored installs—and can even reduce
revenue—for queries with low ad-conversion rates, whereas they deliver substantial incremental revenue for
queries with high ad-conversion rates. Furthermore, within a given query, the frontier shifts with market
composition: Brand-On states are associated with higher revenue and total conversions than Brand-Off states,
and these differences are largest at higher ad loads. In our reduced-form analysis above, we operationalized
non-stationarity along one salient dimension—the presence or absence of the brand advertiser on a given
query—because it is observable and generates substantial within-query variation. However, non-stationarity
can arise from many other forces, e.g., entry/exit of other advertisers, budget exhaustion, shifts in bids and
predicted relevance, seasonality, or changes in user intent. So a policy that conditions only on brand presence
would be incomplete; instead, the platform needs a general adaptive rule that updates from recent outcomes
rather than hard-coding a single market-state indicator. Taken together, these patterns imply that anystatic
ad-load rule—platform-wide or fixed per query—will systematically misallocate inventory, showing too many
ads when advertiser quality is low and too few when high-quality or brand demand is present. This motivates
anadaptive, query-level policy that updates ad load using recent outcomes to track changes in advertiser
quality and advertiser participation.
5 Problem Setup
5.1 Background
We now model ad load design as a sequential decision problem. For each incoming search request, the
platform observes a context and chooses how many sponsored slots to display, then observes noisy outcomes.
A useful policy should (i) customize ad load across queries, (ii) adapt to non-stationarity, and (iii) make the
revenue–conversion trade-off explicit. The setup below defines the context, actions, and outcomes; introduces
a scalar reward representing the platform’s objective; and provides a deployable adaptive policy.
Context, actions, outcomes.Consider a sequence of search requests indexed by 𝑠=1,2,... . Each request
arrives with an observable context𝑥𝑠 =(𝑡 𝑠,𝑞𝑠)∈X , where𝑡𝑠 is the time and𝑞𝑠 is the query.8 Given𝑥𝑠, the
platform chooses an action𝑎𝑠∈A={1,2,...,6} , where𝑎𝑠 is the number of sponsored slots displayed
above organic results. Conditional on𝑎𝑠, the platform runs a GSP auction and shows the top𝑎𝑠 sponsored
listings.
8The context can be expanded to include user/device attributes or advertiser-set features. We restrict attention to non-personalized
ad-load rules for two reasons: (i) the platform avoids user-level ad-load personalization due to privacy and fairness concerns; and (ii)
the main sources of heterogeneity in our setting (as documented above) operate at the query and time levels.
16

After the search results are shown, the platform observes a vector outcome𝑦𝑠 = Conversion𝑠,Revenue𝑠 ∈
Y⊆R 2 +, where Conversion𝑠 is the total number of installs from the search (sum of sponsored and organic
installs) and Revenue𝑠 is ad revenue generated by the search.9
History, policies, and objective.Let the information available at (calendar) time 𝑡 be the history of past
contexts, actions, and outcomes defined as𝐻𝑡 ={(𝑥 𝑠′,𝑎𝑠′,𝑦𝑠′):𝑡 𝑠′ <𝑡}∈H.
A policy maps the current context and available history to an action:
Definition 1(Policy).Apolicy 𝜋 is a mapping𝜋:H×X→Δ(A) , whereΔ(A) is the probability simplex
overA. Under𝜋, the action for search𝑠is drawn as𝑎 𝑠∼𝜋(𝐻 𝑡𝑠,𝑥𝑠).
Because ad load can affect user behavior (e.g., the number of subsequent searches), the realized sequence
of contexts{𝑥 𝑠}need not be policy-invariant.
Next, to make the revenue–conversion trade-off explicit, we use a scalarized reward:
Definition 2(Reward Function).For𝜆≥0, define
𝑟(𝑦𝑠,𝜆)=𝜆Revenue 𝑠 +Conversion 𝑠.(7)
The scalarization parameter𝜆 governs the relative weight on revenue versus conversions. Scalarization is
standard in multi-objective optimization (Deb et al. 2016), and varying𝜆 traces out a Pareto frontier. Recent
marketing studies also use this approach (Rafieian et al. 2025; Wang et al. 2024; Cheng et al. 2025). In
practice, firms calibrate𝜆 using the estimated monetary value of an incremental conversion, such as expected
downstream retention, future purchases, or user lifetime value. This maps both terms in𝑟(𝑦𝑠,𝜆) to a common
value scale, so policy comparisons reflect a transparent economic trade-off. Firms may also tune𝜆 to satisfy
business constraints, for example, meeting a minimum revenue target while limiting conversion losses. We
discuss the choice of𝜆in our setting in§6.5.
5.2 Problem Definition
Given𝜆, the firm’s objective is to maximize cumulative expected reward over a fixed time horizon𝑇:
𝜋★∈arg max
𝜋
E
" ∑︁
𝑠:𝑡𝑠≤𝑇
𝑟𝑦𝜋 𝑠,𝜆 
#
,(8)
where the expectation is taken over randomness in actions and outcomes (and, potentially, in the arrival process
of contexts induced by the policy).
The objective in Equation (8) is to choose, for each incoming search𝑠, an ad load that balances revenue
and conversions according to the scalarization parameter𝜆. For a given query𝑞and candidate ad load𝑖, the
relevant objects are the conditional mean outcomes
E[Revenue𝑠|𝑞 𝑠 =𝑞,𝑎 𝑠 =𝑖]andE[Conversion 𝑠|𝑞 𝑠 =𝑞,𝑎 𝑠 =𝑖].
9By definition, Revenue𝑠 =0 if no sponsored listing is installed. If a sponsored listing at position𝑖is installed, Revenue 𝑠 equals
the minimum bid required for the advertiser to retain position𝑖under the GSP rules.
17

If these quantities were known and stable, the platform could select the ad load that maximizes expected
reward. In practice, however, both these components are unknown; as such the platform must trade off learning
these components through sufficientexplorationwithexploitingthe information it has already gained.
Note that each search arrives with a context (in our case𝑥𝑠, as defined earlier). Thus, a natural starting
point for the adaptive ad-load design problem is contextual bandits, e.g., LinUCB (Li et al. 2010; Chu et al.
2011; Abbasi-Yadkori et al. 2011) or parametric Thompson sampling (Agrawal and Goyal 2013). These
methods are theoretically appealing when rewards are generated by a stable/stationary parametric model
over well-defined contexts and context arrivals are i.i.d. Unfortunately, our environment departs from these
assumptions in four important ways. First, ad-load decisions can affect subsequent user behavior, so context
arrivals in our setting are not strictly policy-invariant, i.e., the arrival of contexts can be non-i.i.d. and
policy-dependent. This is often referred to as adversarial contexts in bandit settings (Lattimore and Szepesv´ari
2020). Second, the platform may not be able to pre-define and track all the relevant contextual variables that
can affect the reward function, e.g., advertiser entry/exit, set of apps available, budget depletion, bid changes,
user-demand, and seasonality. Third, even if the firm could identify all the relevant contextual variables, it is
unclear what parametric form the reward function would take. Fourth, reward mappings are non-stationary
over time; as shown in§4.2.2, within-query shifts are empirically important.
Recent work relaxes some of these assumptions but not all. For example, Cheung et al. (2019); Russac et al.
(2019) model non-stationarity via discounting/sliding-window, but still assume that the platform knows all the
relevant contextual variables that affect the reward model and a linear (parametric) reward model.10 Jain et al.
(2024) allow for adversarial context arrivals and non-parametric reward models in contextual bandits setting.
However, their model still requires the platform to know and define all the relevant contextual variables that
affect the reward model, and assumes that rewards are stationary and stable.
Taken together, these gaps imply three design requirements for our setting: (i) model-free reward estimation
under partial observability of relevant contextual features, (ii) explicit adaptation to drifting rewards, and (iii)
persistent exploration that remains operationally stable. We address these requirements with our proposed
adaptive ad load algorithm introduced next.
6 Adaptive Ad Load Design
We propose and implementexploration-augmented Locally Adaptive Ad Load(e-LAAL). The notation is
intentional:LAALdenotes the adaptive query-level decision rule, while the prefix e denotes the exploration
layer in the deployed system. Throughout, “locally” refers to estimation that is local inqueryand intime:
LAAL estimates rewards separately for each query using only recent observations from a sliding window—i.e.,
it is a query-level, sliding-window greedy rule.
6.1 e-LAAL Architecture and Traffic Allocation
e-LAAL combines two components: (i) an adaptive arm that runsLAAL, and (ii) parallel static arms
{𝐶,𝑇 2,...,𝑇 6} inherited from the first experiment. Let 𝑤𝑒 denote arm-level traffic shares of the static arms
10They also introduce additional tuning and exploration-safety trade-offs that can be difficult to deploy in production.
18

and define
𝜖≡
∑︁
𝑒∈{𝐶,𝑇 2,...,𝑇 6}
𝑤𝑒.(9)
Thus,𝜖 is the fixed exploration budget, while 1−𝜖 is served by the adaptive LAAL arm. In our deployment,
𝜖=0.10, so 10% of users are permanently allocated to static exploration and 90% to LAAL (Table 4).
This architecture separates exploration from exploitation in a controlled way. Static arms ensure persistent
support for every ad-load level and LAAL exploits these continually refreshed observations to adapt ad load
across queries and over time. The static cohorts are also used to estimate contemporaneous fixed ad load
(always show𝑖ads) counterfactuals; see§8.1 for details.
Table 4: Traffic Allocation under e-LAAL
Condition Share of Users(𝑤 𝑒)
𝐶(1 ad) 5%
𝑇2 (2 ads) 1%
𝑇3 (3 ads) 1%
𝑇4 (4 ads) 1%
𝑇5 (5 ads) 1%
𝑇6 (6 ads) 1%
LAAL (adaptive) 90%
e-LAAL (all conditions combined) 100%
6.2LAALDecision Rule and Algorithm
We now describe the adaptiveLAALpolicy, which runs on 90% of the traffic.LAALis a deployable policy
for pursuing the cumulative-reward objective in Equation(8): it uses recent query-level outcomes to track the
contemporaneous reward-maximizing ad load as the reward frontier changes over time. It is adaptive along two
dimensions. First, it isquery-adaptive: different queries can receive different ad loads because {𝑟𝑖(𝑞,𝑡)} 6 𝑖=1
differs across queries. Second, it istime-adaptive: for a fixed query, the selected ad load can change as
recent outcomes update, allowing the policy to respond to shifts in market conditions (e.g., brand entry/exit,
bidder-quality changes). Operationally, for each incoming search, LAAL combines local recency-based
estimation with greedy action selection:
• Sliding-window reward estimation.For each query–ad-load pair(𝑞,𝑖) , LAAL estimates recent mean
conversion and revenue per search using a fixed-length sliding window.11
• Greedy ad-load selection.LAAL maps these estimates into a scalarized reward and selects the ad load
with the highest estimated reward.
In deployment, LAAL maximizes the per-search reward in Equation (7). For each query 𝑞, it forms
sliding-window estimates for each ad load𝑖∈{1,...,6} . Let ℎ denote window length, and define thesliding
window𝑊𝑡(𝑞)as:
𝑊𝑡(𝑞)={𝑠 ′ :𝑞 𝑠′ =𝑞, 𝑡−ℎ≤𝑡 𝑠′ <𝑡}.(10)
11Using fixed-length windows (or related forgetting schemes) to handle non-stationarity is common in online learning and bandits
(Tr`ov`o et al. 2020; Cavenaghi et al. 2021; Cheung et al. 2019).
19

calendar time
𝑡1−ℎ 𝑡1𝑡2−ℎ 𝑡2=𝑡 1+Δ
search𝑠 1 search𝑠 2
Δ𝑊𝑡1(𝑞)=[𝑡 1−ℎ,𝑡 1)
𝑊𝑡2(𝑞)=[𝑡 2−ℎ,𝑡 2)
Figure 6: Sliding-window update for two searches of the same query 𝑞, separated by Δ. LAAL uses
𝑊𝑡(𝑞)=[𝑡−ℎ,𝑡); as the window shifts from𝑡 1 to𝑡 2, old data are dropped and new data are added.
Figure 6 depicts how the sliding window 𝑊𝑡(𝑞) is used for two searches of the same query 𝑞, 𝑠1 and𝑠2,
separated by a time difference ofΔ. Notice that for the same query in the newer search (𝑠2), the older data is
dropped and only data from the most recent time-window of lengthℎis considered.
Next, for each ad-load𝑖, let𝑛𝑖(𝑞,𝑡) denote thenumber of observations in the recent windowfor query 𝑞
when ad load𝑖was shown:
𝑛𝑖(𝑞,𝑡)=
∑︁
𝑠′∈𝑊𝑡(𝑞)
1{𝑎𝑠′ =𝑖}.(11)
Using these observations, LAAL computes two local means (the two 𝜇-terms): b𝜇𝐶,𝑖(𝑞,𝑡) , thelocal mean
conversion per search, andb𝜇𝑅,𝑖(𝑞,𝑡), thelocal mean revenue per search, both for query𝑞under ad load𝑖:
b𝜇𝐶,𝑖(𝑞,𝑡)=
˝
𝑠′∈𝑊𝑡(𝑞) 1{𝑎𝑠′ =𝑖}Conversion 𝑠′
𝑛𝑖(𝑞,𝑡)+𝛿 ,b𝜇 𝑅,𝑖(𝑞,𝑡)=
˝
𝑠′∈𝑊𝑡(𝑞) 1{𝑎𝑠′ =𝑖}Revenue 𝑠′
𝑛𝑖(𝑞,𝑡)+𝛿 ,(12)
where 𝛿 >0 is a small stability constant. LAAL then computes b𝑟𝑖(𝑞,𝑡) , theestimated local rewardfor
choosing ad load𝑖on query𝑞at time𝑡:
b𝑟𝑖(𝑞,𝑡)=𝜆b𝜇 𝑅,𝑖(𝑞,𝑡)+b𝜇𝐶,𝑖(𝑞,𝑡)−𝜂𝑖,(13)
selects ad load:
𝑎𝑡(𝑞)∈arg max 𝑖∈{1,...,6} b𝑟𝑖(𝑞,𝑡).
We set𝜂 to a very small number; thus−𝜂×𝑖 is a small tie-break regularizer that breaks near ties in favor of
fewer ads. To stabilize sparse queries, LAAL applies greedy selection only when the query has at least 𝑚
observations in the window; otherwise, it returns the default ad load of 𝑖def. We discuss the choice of the
hyperparameters (ℎ,𝛿,𝜂,𝑚,𝑖 def) in§6.5.
Algorithm 1 presents the details of the deployed procedure.
Conditional Cohort-Invariance Assumption.LAAL pools recent observations from both the LAAL
and static cohorts to estimate query–ad-load rewards (i.e., to estimate Equations (11) and (12)). Pooling
improves support for each query–ad-load pair and, as such, improves precision. However, it requires immediate
per-search outcomes to be conditionally comparable across cohorts: after conditioning on query, time, and
displayed ad load, revenue and conversion responses are assumed to be independent of whether the observation
came from a static or adaptive cohort. This assumption is weaker than requiring search behavior to be
20

policy-invariant; it does not require identical future search behavior across cohorts, and the static cohorts
are maintained precisely because ad load may affect subsequent usage. Instead, it rules out unobserved
regime-specific differences in immediate search-level responses after conditioning on query, time, and realized
ad load. We formally test and establish the validity of this assumption in Web Appendix§E.
Further, note that while this assumption is relevant for the quality of LAAL ’s learned reward estimates, it
does not affect the direct evaluation of realized deployment outcomes in§7. If the assumption fails, the pooled
estimates used by LAAL may be noisier or biased for the LAAL cohort, potentially reducing the quality of the
policy’s recommendations. However, outcomes for the LAAL arm and the static arms are observed directly in
their respective randomized cohorts during deployment. Thus, the deployment results remain informative
about how the implemented policy performed in production.
Illustrative example.We now present a simple example using a single query and two adjacent windows
separated by one day to illustrate how LAAL works. Suppose LAAL uses only the lastℎ=3 days of data,
𝜆=0.01 , and the tie-breaking regularizer𝜂=0.001 . Then, for query 𝑞 at time𝑡, the window is𝑊𝑡(𝑞) , and
LAAL computes the estimated reward over this window as:
b𝑟𝑖(𝑞,𝑡)=0.01b𝜇 𝑅,𝑖(𝑞,𝑡)+b𝜇𝐶,𝑖(𝑞,𝑡)−0.001𝑖.
For illustration, we only consider a setting with three ad loads𝑖∈{2,4,6}and two consecutive windows, as
shown in Table 5. LAAL chooses𝑎𝑡(𝑞)=6 in Table 5a, when the brand is active, and the expected revenue
from a higher ad load outweighs the lower conversion rate. In contrast, 𝑎𝑡(𝑞)=2 in Table 5b. Here, the
brand has become inactive, and the expected revenue from a higher ad load does not compensate for the lower
conversion. See Figure 7 for a pictorial depiction.
Table 5: LAAL estimates in two consecutive windows.
(a) Window A (brand-active period)
𝑖 b𝜇𝐶,𝑖 b𝜇𝑅,𝑖 b𝑟𝑖
2 0.50 36 0.50+0.36−0.002=0.858
4 0.38 60 0.38+0.60−0.004=0.976
6 0.27 84 0.27+0.84−0.006=1.104
(b) Window B (one day later; window shifted, brand exits)
𝑖 b𝜇𝐶,𝑖 b𝜇𝑅,𝑖 b𝑟𝑖
2 0.48 32 0.48+0.32−0.002=0.798
4 0.33 40 0.33+0.40−0.004=0.726
6 0.18 36 0.18+0.36−0.006=0.534
This illustrates the sliding-window mechanism: as old observations leave and new ones enter the 3-day
window, the estimated reward ranking changes, and LAAL adapts the ad load for the same query over time. In
sum, LAAL maximizes estimated contemporaneous reward from local evidence, while parallel static cohorts
provide continual exploration by maintaining exposure to every ad-load level.
6.3 Why e-LAAL Fits This Setting
e-LAAL addresses the key deployment challenge in our setting: how to combine adaptive exploitation with
exploration that remains operationally stable and provides meaningful fixed-policy counterfactuals. Unlike
standard per-search exploration schemes in contextual bandits, e-LAAL separates exploration and exploitation
through persistent user-level cohorts. This distinction is important because ad load may affect not only
21

Algorithm 1e-LAAL Algorithm: Locally Adaptive Ad Load (LAAL) with Parallel Static Arms
Require: each search𝑠 arrives with context(𝑞𝑠,𝑡𝑠), and arm assignment𝑒𝑠 inherited from user assignment;
𝑒𝑠∈{𝐶,𝑇 2,...,𝑇 6,𝐿}, where𝐿denotes the LAAL arm
Require: window length ℎ (days), scalarization 𝜆≥0 , smoothing 𝛿 >0 , minimum window volume 𝑚,
regularization𝜂≥0, default ad load𝑖 def
Require:action setA={1,2,3,4,5,6}
1:foreach search request𝑠do
2:if𝑒 𝑠∈{𝐶,𝑇 2,...,𝑇 6}then⊲Static cohorts: fixed ad load
3:𝑎 𝑠←1·1{𝑒 𝑠 =𝐶}+ ˝6 𝑗=2 𝑗1{𝑒 𝑠 =𝑇 𝑗}
4:else⊲𝑒 𝑠 =𝐿: LAAL cohort
5:𝑊←{𝑠 ′ :𝑞 𝑠′ =𝑞 𝑠, 𝑡𝑠−ℎ≤𝑡 𝑠′ <𝑡 𝑠}⊲Local window for query𝑞 𝑠, using all cohorts
6:for𝑖∈Ado
7:𝑛 𝑖← ˝ 𝑠′∈𝑊 1{𝑎𝑠′ =𝑖}
8:𝐶 𝑖← ˝ 𝑠′∈𝑊 1{𝑎𝑠′ =𝑖}Conversion 𝑠′
9:𝑅 𝑖← ˝ 𝑠′∈𝑊 1{𝑎𝑠′ =𝑖}Revenue 𝑠′
10:b𝜇 𝐶,𝑖← 𝐶𝑖 𝑛𝑖+𝛿
11:b𝜇 𝑅,𝑖← 𝑅𝑖 𝑛𝑖+𝛿
12:b𝑟 𝑖←𝜆b𝜇𝑅,𝑖+b𝜇𝐶,𝑖−𝜂𝑖
13:end for
14:if ˝ 𝑖∈A 𝑛𝑖 <𝑚then
15:𝑎 𝑠←𝑖 def ⊲Fallback for sparse windows
16:else
17:𝑎 𝑠←arg max𝑖∈A b𝑟𝑖
18:end if
19:end if
20:Deploy𝑎 𝑠 sponsored slots; observe(Conversion 𝑠,Revenue𝑠)
21:end for
t-4 t-3 t-2 t-1 t t+1 t+2
Window A
Window B (shifted)
Window A scores
b𝑟2=0.858,b𝑟 4=0.976,b𝑟 6=1.104
⇒𝑎 𝑡(𝑞)=6
Window B scores
b𝑟2=0.798,b𝑟 4=0.726,b𝑟 6=0.534
⇒𝑎 𝑡(𝑞)=2
window slides
Figure 7: Illustration of LAAL ’s sliding-window adaptation. As the 3-day window shifts, estimated rewards
change, and the selected ad load for the same query can switch.
immediate revenue and conversion, but also subsequent search behavior and engagement. Evaluating fixed
ad-load policies therefore requires users to remain under persistent regimes such as “always show𝑖 ads,” which
the static cohorts preserve.
This architecture delivers four advantages for our deployment environment.
• User-level fixed-policy counterfactuals.Because ad load may affect future usage, fixed ad-load bench-
marks must be evaluated using persistent user-level regimes rather than isolated per-search randomization.
22

The static arms {𝐶,𝑇 2,...,𝑇 6} maintain users under fixed ad-load policies, allowing us to estimate
outcomes for policies of the form “always show𝑖 ads,” including their induced effects on search behavior
and engagement. A standard𝜖-greedy policy mixes ad loads within a single adaptive arm and therefore
does not provide these fixed-policy counterfactuals.
• Stable exploration support under changing context distributions.Exploration is supplied ex ante
through static arms with fixed traffic shares𝑤𝑒. Thus, every ad-load level continues to receive exposure
even if LAAL concentrates adaptive traffic on a subset of actions. This is particularly important when
ad-load decisions may influence future context arrivals: realized query-level support can differ from the
platform’s intended traffic allocation, but the static cohorts provide a persistent exploration floor.
• Model-free adaptation to a drifting reward frontier.LAAL estimates query-level rewards directly
from recent outcomes rather than relying on a prespecified reward model. This reduces dependence on
observing and encoding all drivers of rewards, such as advertiser entry and exit, budget depletion, bid
changes, relevance shifts, seasonality, and demand changes. Through sliding-window updates, the policy
adapts as these factors shift the revenue–conversion frontier over time.
• Production-friendly implementation.e-LAAL operates as a lightweight decision layer on top of the
platform’s existing prediction, auction, and ranking systems. It does not require rebuilding the underlying
advertising infrastructure or deploying a complex end-to-end learning system. Instead, it uses recent
query-level outcomes and a small set of persistent exploration cohorts to adapt ad load at scale.
Together, these features make e-LAAL suitable for sponsored-search environments where reward mappings
evolve over time and credible fixed-policy counterfactuals are essential for deployment evaluation.
6.4 Theoretical Guarantee for e-LAAL
In this section, we formalize the performance of e-LAAL in a non-stationary environment. The benchmark is
a dynamic query-level oracle that can choose the best ad load for a fixed query as its reward frontier changes
over time. The key complication, relative to standard non-stationary bandit analyses, is that exploration in
e-LAAL is supplied through persistent user-level static cohorts rather than direct per-search randomization.
As a result, the realized query-level support for each ad-load arm may differ from the platform’s designed
traffic shares. The theorem below reports the optimized-rate implication under regular query arrivals; Web
Appendix§F provides the corresponding finite-sample bound for arbitrary exploration mass and window
length. For simplicity, regret is stated in normalized reward units, with raw-unit regret obtained by rescaling
by the reward bound.
Theorem 1(Dynamic regret of e-LAAL).Fix query 𝑞. Assume the number of realized searches for query𝑞
during[0,𝑇] satisfies𝑁=Θ(𝑇) , and the query arrivals are regular enough that eachℎ-time window contains
on the order of𝑁ℎ/𝑇 searches. Under the assumptions stated in Web Appendix§F, after normalizing rewards
and optimizing over exploration mass and window length, the dynamic regret of Algorithm 1 is bounded, with
high probability, by
𝑅dyn 𝑞 (𝑇)= ˜𝑂  ¯𝑐1/4𝑐−1/4𝑇 3/4𝐾𝑉𝑞(𝑇)1/4 .
Here𝑉𝑞(𝑇) is the variation budget,𝐾 is the number of arms,𝑐 is the minimum-support coefficient, and ¯𝑐is
the total-static-traffic upper-bound coefficient.
23

Proof.See Web Appendix§F.
The query-level guarantee reflects the local nature of LAAL: each query evolves according to its own
reward frontier and support process. Platform-level performance aggregates these query-level decisions
weighted by search volume. The coefficients𝑐 and ¯𝑐account for the gap between the design exploration budget
and the realized query-level exploration traffic. The coefficient𝑐 lower bounds the observed traffic on each
static arm by its design weight. The coefficient ¯𝑐upper bounds the total realized traffic from static cohorts by
their total exploration weight. Thus, these parameters capture deviations between assigned user-level cohort
shares and realized query-level static traffic. If there is no such deviation and the realized exploration traffic
exactly matches the design exploration budget, then𝑐 =¯𝑐=1.
The regret bound combines the standard non-stationary bandit tradeoff between estimation noise and
temporal drift with the additional cost and support role of static exploration cohorts. The proof follows the
standard logic of non-stationary bandit analysis, where sliding-window estimators balance estimation noise
against temporal drift (Tr`ov`o et al. 2020; Cavenaghi et al. 2021; Cheung et al. 2019). The new feature in
our setting is the exploration architecture. In canonical bandit models, exploration probabilities are typically
controlled directly at the decision level. In e-LAAL, exploration is supplied by persistent user-level static
cohorts, but regret is evaluated on the realized search stream for a fixed query. Our analysis therefore
accounts for the fact that realized query-level support can differ from the assigned cohort shares. The support
coefficients in the theorem make this distinction explicit and adapt standard non-stationary regret arguments to
the parallel-static-cohort implementation used in our deployment.
6.5 Implementation Details
We now discuss the three main parameters that are used in the deployment below.
• Scalarization parameter in the objective function (𝜆):In principle, 𝜆 should reflect the platform’s
monetary value of an incremental conversion (e.g., downstream engagement, retention, or LTV). Because
these downstream outcomes are not observed in our data, we use𝜆 as a scale-normalization parameter to
convert short-run ad revenue into conversion-equivalent units, so that the two components in Equation(7)
are comparable. We calibrate𝜆 from the first experiment: the uniform policies{𝐶,𝑇 2,...,𝑇 6} trace an
empirical revenue–conversion frontier; over this feasible menu, the relationship is approximately linear,
implying a near-constant local exchange rate between conversion losses and revenue gains. We therefore
set
𝜆≈− ΔConversion ΔRevenue ,
which yields𝜆≈0.01 in our data (Table 2). This calibration is not a claim about long-run welfare weights;
rather it anchors LAAL to the platform’s revealed short-run rate of substitution across feasible uniform
ad-load policies.
• Exploration budget (𝜖):As discussed earlier, exploration is fixed ex ante through parallel static arms as
defined in Equation (9). In our deployment, 𝜖=0.10 : 10% of traffic is permanently allocated to static
arms (5% to𝐶, 1% to each𝑇 2,...,𝑇 6), while 90% is assigned to the adaptive LAAL arm.
• Algorithmic hyperparameters (ℎ,𝑚,𝜂,𝛿,𝑖 def):We set ℎ=3 days,𝑚=100 ,𝜂=10 −3,𝛿=10 −6, and
fallback load𝑖 def =4. The reasons for these choices are discussed briefly below:
24

•ℎ=3 days balances responsiveness and variance. Shorter windows react faster to market-state
changes (e.g., advertiser entry/exit) but are noisier; longer windows are more stable but slower to
adapt. A 3-day horizon provided sufficient sample support while preserving timely adaptation.
•𝑚=100 enforces a minimum evidence threshold before greedy selection. This guards against
unstable action flips on sparse queries where window estimates are high-variance.
•𝜂=10 −3 is a small tie-break regularizer that favors lower ad loads only when estimated rewards are
nearly equal.
•𝛿=10 −6 is a numerical smoothing constant to avoid division instability in very low-count cells; it is
intentionally negligible relative to observed counts and does not affect estimates when support is
adequate.
•𝑖 def =4 is the default ad load used when the query is sparse in the recent window. Using the historical
data on static-cohorts obtained from the last month of the first experiment, we set𝑖def to the uniform
ad load that maximizes expected reward on a low-volume search query. The definition of low volume
query follows the same definition as in deployment of LAAL. See Web Appendix§G for the detailed
analysis.
7 Empirical Performance of the Adaptive Ad Load Policy
The e-LAAL architecture was deployed at the platform level, and we now report the results from the deployment
for a 22-day steady-state window from December 8 to 29, 2023.12 During this period, user assignment is
fixed: 90% of traffic is routed to the adaptive LAAL arm and 10% remains in the static exploration arms
{𝐶,𝑇 2,...,𝑇 6}(as shown in Table 4).
In the rest of this section, we address three empirical questions on the performance of our adaptive ad load
policy in deployment. (1) Does e-LAAL improve the revenue–conversion trade-off relative to static ad-load
policies? (2) Does LAAL adapt ad load across query segments in economically sensible ways? (3) Does
LAAL adapt over time when market conditions shift (brand entry/exit)?
7.1 Main Results
Table 6: Summary Statistics of the Deployment
𝐶 𝑇 2 𝑇3 𝑇4 𝑇5 𝑇6 LAAL e-LAAL
User Count 1,121,219 223,690 222,024 222,586 221,871 221,961 20,097,353 22,330,704
Searches 3,859,143 776,181 776,749 779,883 776,194 781,223 69,851,684 77,601,057
Revenue/Usera 25.80 29.48 31.17 33.11 36.11 36.68 36.13 35.47
Conversion/User 2.152 2.104 2.101 2.091 2.064 2.054 2.127 2.126
Daily Eng. (%) 8.45 8.44 8.38 8.34 8.37 8.35 8.43 8.43
Searches/User 3.44 3.47 3.50 3.50 3.50 3.52 3.48 3.47
Note: aScaled by an undisclosed multiplier.
12The adaptive LAAL arm was launched soon after the first experiment ended (November 17, 2023), but the system required a
short ramp-up period before reaching steady state.
25

Summary statistics from platform-level deployment.Table 6 provides four immediate facts about the
deployment. First, the scale is large: e-LAAL serves 22.33 million users and 77.60 million searches in 22
days, with the adaptive LAAL arm alone covering 20.10 million users and 69.85 million searches (≈90% of
traffic). Second, the static arms remain large in absolute size (≈0.22 M–1.12M users each), so exploration and
benchmarking are statistically meaningful throughout deployment.
Third, the table reproduces the core economics from the first experiment (Table 1): as static ad load
increases from𝐶 to𝑇6, revenue per user rises monotonically (25.80→ 36.68), while conversion per user falls
(2.152→ 2.054), confirming a stable revenue–conversion trade-off. Fourth, LAAL improves on this frontier:
revenue per user is 36.13 (essentially𝑇5-level, 36.11), but conversion per user is 2.127 (higher than𝑇5: 2.064,
and𝑇6: 2.054, and close to 𝐶: 2.152). Note that the actual revenue and conversion numbers differ from those
in Table 1 because the first experiment lasted 66 days, while the deployment statistics come from a 22-day
period; as such, conversions and revenue are proportionally smaller here.13
The system-level e-LAAL outcome remains close to LAAL (35.47 revenue/user; 2.126 conversion/user),
indicating that the fixed 10% exploration layer preserves learning and benchmarking with limited performance
loss. Finally, daily engagement does not show notable differences across cohorts. LAAL has slightly lower
engagement than𝐶 and𝑇2, but these differences are not statistically significant; Web Appendix§C.3 reports
the corresponding tests. Searches per user are also tightly clustered across cohorts (3.44–3.52), suggesting that
outcome differences are not driven by large differences in search intensity across arms. Overall, Table 6 shows
that at production scale, e-LAAL preserves the monetization gains of high ad-load policies while recovering a
substantial share of the conversion losses they typically induce.
Evaluation objects and normalization.The summary statistics above are descriptive. To make policy
comparisons valid under unequal cohort traffic shares, we use inverse-propensity normalization (Horvitz
and Thompson 1952; Yoganarasimhan et al. 2023). Let𝑤𝑒 be the assignment probability to cohort𝑒. For
𝑌∈{Revenue,Conversion}, define
b𝑌𝑒 = 1 𝑤𝑒 ∑︁ 𝑠:𝑒𝑠=𝑒 𝑌𝑠.(14)
For static cohorts𝑒∈{𝐶,𝑇 2,...,𝑇 6}, b𝑌𝑒 is an unbiased estimate of the total outcome if the full population
were assigned to the corresponding fixed policy (“always show𝑖ads”).
Because LAAL is trained using data from all cohorts, the policy-relevant system estimand is the deployed
mixture:
b𝑌e-LAAL =
∑︁
𝑒∈{𝐶,𝑇 2,...,𝑇 6,𝐿}
𝑤𝑒 b𝑌𝑒 =
∑︁
𝑠
𝑌𝑠.(15)
Thus, e-LAAL is the correct “policy + exploration” benchmark for deployment comparisons.
Frontier shift under deployment.Figure 8a compares static cohorts, the LAAL cohort, and e-LAAL in the
empirical revenue–conversion space. Two patterns emerge. First, LAAL/e-LAAL improves the empirical
revenue–conversion trade-off relative to uniform static policies: it reaches revenue levels close to high-ad-load
static rules (e.g., always show five ads, i.e.,𝑇5) while maintaining conversions closer to low-ad-load rules (e.g.,
13𝑅𝑒𝑣𝑒𝑛𝑢𝑒/𝑈𝑠𝑒𝑟
𝑆𝑒𝑎𝑟𝑐ℎ/𝑈𝑠𝑒𝑟 is a more comparable metric that controls for the length of the experiment and this metric is similar across both
experiments.
26

(a) Revenue–conversion across fixed ad-load cohorts,
LAAL, and e-LAAL.
(b) Distribution of the number of ads recommended
by LAAL.
Figure 8: Performance of LAAL (and system-level e-LAAL).
always show two ads). This is an efficiency gain, not movement along a fixed frontier. Second, LAAL and
e-LAAL are numerically close, as expected given the90/10 LAAL/exploration split, so the exploration cost is
modest in practice.
How the policy behaves in practice.Figure 8b shows the distribution of ad counts selected by LAAL. On
average, LAAL recommends 3.1 ads per search. It uses sliding-window estimates to choose greedily in 79%
of searches (those with at least𝑚=100 observations in the recent window) and falls back to𝑖def =4 in the
remaining 21% (sparser queries). The recommendation distribution is bimodal: LAAL frequently chooses
either low ad loads (conversion-oriented) or high ad loads (revenue-oriented), with fewer intermediate choices.
This is consistent with the discrete nature of the decision problem: interior ad loads are optimal only under a
narrow knife-edge in incremental revenue versus conversion loss.
7.2 Heterogeneity in Policy Performance
Performance across query segments.We next evaluate LAAL across the query segments defined in §4.2
(bucketed by control-group advertising CVR). Figure 9 plots the empirical revenue–conversion trade-off
within each segment. LAAL improves upon fixed ad-load (or static) policies in all segments, with the most
pronounced gains in the high-CVR segment, where incremental ad slots are most likely to translate into
additional paid installs and revenue.
Figure 10 reports the distribution of LAAL ’s recommended ad loads by segment. The policy adapts in
the expected direction: it recommends fewer ads on low-CVR queries (where additional slots generate little
revenue and primarily displace relevant organic content) and more ads on high-CVR queries (where additional
slots generate revenue). This behavior mirrors the heterogeneity patterns in§4.2 and illustrates that LAAL
operationalizes those insights using only recent outcome data, without hard-coding segment membership.
Within-query heterogeneity over time: brand entry and exitFinally, we examine the performance of
LAAL in non-stationary settings, i.e., queries with explicit time variation in advertiser composition. We
27

(a) Low CVR segment
 (b) Mid CVR segment
 (c) High CVR segment
Figure 9: Revenue–conversion trade-offs across query segments.
(a) Low CVR segment
 (b) Mid CVR segment
 (c) High CVR segment
Figure 10: Distribution of ad loads recommended by LAAL across query segments.
Figure 11: Performance of LAAL and e-LAAL on non-stationary queries (brand entry/exit)
28

focus on brand queries whose focal brand app advertises on some days but not others during the 22-day
deployment window. Restricting attention to queries that experience bothBrand-OnandBrand-Offperiods
during deployment yields 315 such queries, which together account for 13% of revenue, 13% of conversions,
and 11% of searches in the control condition. We refer to these asnon-stationary queries.
Figure 11 reports the mean observed outcomes for non-stationary queries. We see that LAAL dominates
static cohorts on both revenue and conversions, consistent with a key mechanism of LAAL: time-adaptive
reallocation when the reward frontier shifts.
A direct test of adaptivity is whether LAAL recommends different ad loads for the same query depending
on brand presence. For the non-stationary queries, we compare LAAL ’s recommended ad-load distributions
duringBrand-OnandBrand-Offsearches, using within-query reweighting so that queries with different
Brand-On shares are comparable; details of the reweighting procedure are provided in Web Appendix§H.
Figure 12 plots the resulting recommendation histograms. When the brand is absent, LAAL concentrates
on lower ad loads; when the brand is present, the distribution shifts toward higher ad loads. This within-query
reallocation is precisely the behavior a time-adaptive ad-load policy should exhibit in response to changing
advertiser composition.
(a)Brand-Offstate
 (b)Brand-Onstate
Figure 12: Distribution of LAAL ad-load recommendations underBrand-OffandBrand-Onstates for
non-stationary queries. Histograms are reweighted within query to make Brand-On and Brand-Off states
comparable across queries with different Brand-On shares.
7.3 Managerial Implications
Three implications follow from the deployment evidence. First,fixed exploration with adaptive exploitationis
implementable at scale: the platform can pre-commit a small exploration budget (10% here) and still obtain
substantial frontier gains through local adaptive exploitation. Second,query-level ad-load personalization
matters: the platform can improve monetization without proportionate conversion losses by reallocating ad
load at the query level rather than committing to a single global ad count; this matters because monetization-
conversion trade-offs vary sharply across query types. Third,time adaptivity is economically material: when
29

advertiser composition shifts (e.g., brand entry/exit), adaptive ad-load reallocation can dominate static rules
on both objectives.
Taken together, the results indicate that e-LAAL is not only statistically and operationally feasible, but
also managerially actionable: it provides a practical mechanism to improve monetization while preserving
user outcomes in real large-scale non-stationary sponsored search platforms.
8 Comparisons with Benchmark Policies
The previous section compared LAAL and the deployed e-LAAL system to the contemporaneous static
cohorts{𝐶,𝑇 2,...,𝑇 6} using IPW-normalized outcomes from the deployment window. Those comparisons
evaluate LAAL against the fixed ad-load regimes that were actually deployed alongside the adaptive arm.
However, they benchmark LAAL only against the six individual “always show𝑖 ads” regimes; they do not ask
whether LAAL outperforms static rules that a platform might have selected using performance data, such as a
historically chosen uniform rule or a query-specific static mapping. In this section, we therefore provide a
broader benchmark analysis against static policies that are still time-invariant once chosen, but are selected
using either historical or deployment-period data.
We study two classes of static policies. The first class consists ofuniform static policies, which show the
same number of ads for every query. The second class consists ofquery-dependent static policies, which
allow the ad load to vary by query but keep each query’s assignment fixed over time. These benchmarks allow
us to separate the value of query sensitivity from the value of time adaptivity.
For each policy class, we distinguish two timing regimes. Ahistorical benchmarkis selected using the
66-day experiment window and is therefore feasible ex ante before the 22-day deployment. It answers: what
static policy would the platform have chosen if it had used the earlier experiment to set a rule for deployment?
Adeployment oracleis selected using the 22-day deployment window itself. It is not feasible ex ante; rather, it
is an ex post benchmark that asks how LAAL performs relative to the best static rule in the realized deployment
environment. Thus, historical benchmarks evaluate implementable static alternatives, while deployment
oracles provide stronger diagnostic comparisons.
Notation:For compactness, let 𝐻 denote the historical 66-day experiment window and 𝐷 denote the
22-day deployment window. LetS𝑊 andV𝑊 denote the sets of searches and users observed during window
𝑊∈{𝐻,𝐷} . For each ad load𝑖∈A , letS𝑊(𝑖) andV𝑊(𝑖) denote the sets of searches and users in window
𝑊 assigned to the static cohort that displays ad load𝑖. Let 𝑤𝑖 denote the traffic share of the corresponding
static cohort. For query-dependent benchmarks, let S𝑊(𝑞,𝑖) denote the sets of searches observed during
window𝑊for query𝑞and ad load𝑖.
8.1 Uniform Static Benchmarks
A uniform static policy chooses the same number of sponsored slots for all queries. These policies correspond
directly to the fixed experimental cohorts: policy𝑖implements “always show𝑖ads.”
Definition 3(Uniform Static Policy Class).For each 𝑖∈A , define the uniform static policy𝜋𝑈 𝑖 :Q→A by
𝜋𝑈 𝑖(𝑞)=𝑖∀𝑞∈Q. The class of uniform static policies isΠ 𝑈 ={𝜋 𝑈 𝑖 :𝑖∈A}.
30

For𝑊∈{𝐻,𝐷}and𝑖∈A, define the sample mean reward per user under uniform ad load𝑖as
b𝑅𝑈 𝑊(𝑖;𝜆):= 1 |V𝑊(𝑖)| ∑︁ 𝑠∈S𝑊(𝑖) 𝑟(𝑦𝑠,𝜆).
This user-level normalization preserves the interpretation of the static cohorts as persistent user-level regimes.
Definition 4(Historical Uniform Benchmark and Deployment Uniform Oracle).For𝑊∈{𝐻,𝐷}, define
𝑖𝑈,★ 𝑊 ∈arg max 𝑖∈A b𝑅𝑈 𝑊(𝑖;𝜆), 𝜋 𝑈,★ 𝑊 :=𝜋 𝑈 𝑖𝑈,★ 𝑊 .
We call𝜋𝑈,★ 𝐻 thehistorical uniform benchmarkand𝜋 𝑈,★ 𝐷 thedeployment uniform oracle.
The two benchmarks are selected by the same reward-maximization rule, but from different samples.
The historical uniform benchmark 𝜋𝑈,★ 𝐻 uses only the 66-day experiment and is therefore feasible before
deployment. The deployment uniform oracle𝜋𝑈,★ 𝐷 uses the deployment window itself and is therefore an ex
post benchmark. In our data,𝑖𝑈,★ 𝐻 =3 , corresponding to the 3-ad policy𝑇3, whereas𝑖𝑈,★ 𝐷 =5 , corresponding
to the 5-ad policy𝑇5. The shift from𝑇3 historically to𝑇5 in deployment shows that even the best platform-wide
static ad load changes over time. This instability is precisely the type of environment in which an adaptive
policy such as LAAL can improve on fixed rules.
We compare LAAL to the uniform benchmarks using user-level outcomes from the deployment window.
For each outcome𝑌∈{Revenue,Conversion,Reward} , where Reward=Conversion+0.01×Revenue , we
estimate the following equation:
𝑌𝑢=𝛼𝑌 𝐿+ ∑︁
𝑗∈{𝐶,𝑇 2,...,𝑇 6}
𝛽𝑌 𝑗 1{𝑒(𝑢)=𝑗}+𝜀 𝑌 𝑢.(16)
Here𝑌𝑢 is the total outcome for user𝑢 over the deployment window,𝛼𝑌 𝐿 is the mean outcome in the LAAL
arm, and𝛽 𝑌 𝑗 measures the difference between static cohort𝑗and LAAL.
Table 7 reports the estimates. LAAL strictly dominates the historical uniform benchmark 𝑇3: relative
to 𝑇3, LAAL delivers significantly higher revenue and conversions, and therefore significantly higher
scalarized reward. LAAL also weakly dominates the deployment uniform oracle𝑇5: revenue is statistically
indistinguishable between LAAL and𝑇5, while LAAL delivers significantly higher conversions. Thus, LAAL
outperforms both the feasible ex ante historical uniform benchmark as well as the ex post deployment uniform
oracle.
Next, we use an iso-reward line to visualize whether LAAL improves the scalarized objective relative to
the best uniform static rule in deployment. Recall that the platform’s scalarized reward is
Reward=Conversion+𝜆·Revenue.
The deployment uniform oracle𝜋𝑈,★ 𝐷 is the uniform static policy with the highest deployment-period reward;
in our data this corresponds to𝑇5. Let its total deployment-period reward be𝐵𝑈 𝐷 :=|V𝐷|· b𝑅𝑈 𝐷(𝑖𝑈,★ 𝐷 ;𝜆) , where
V𝐷 is the set of all users observed during the 22-day deployment period. Then, the associated iso-reward line
31

Table 7: User-level deployment regressions comparing LAAL to uniform static benchmarks.
Revenue Conversion Reward
LAAL 36.13 ∗∗∗ (0.08) 2.127 ∗∗∗ (0.000) 2.488 ∗∗∗ (0.001)
𝐶-10.33 ∗∗∗ (0.33) 0.025 ∗∗∗ (0.002) -0.078 ∗∗∗ (0.004)
𝑇2 -6.65∗∗∗ (0.72) -0.023 ∗∗∗ (0.004) -0.090 ∗∗∗ (0.009)
𝑇3 -4.96∗∗∗ (0.72) -0.026 ∗∗∗ (0.004) -0.075 ∗∗∗ (0.009)
𝑇4 -3.02∗∗∗ (0.72) -0.036 ∗∗∗ (0.004) -0.066 ∗∗∗ (0.009)
𝑇5 -0.02 (0.72) -0.063 ∗∗∗ (0.004) -0.064 ∗∗∗ (0.009)
𝑇6 0.55 (0.72) -0.073 ∗∗∗ (0.004) -0.067 ∗∗∗ (0.009)
Obs. 22,330,704 22,330,704 22,330,704
𝑅2 <0.001<0.001<0.001
Note:The LAAL row reports the mean outcome in the LAAL arm. Rows 𝐶,𝑇 2,...,𝑇 6 report differences relative to LAAL. Reward
is defined as Conversion+0.01·Revenue . Standard errors in parentheses. Significance levels: ∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
is
L𝑈 𝐷 :={(C,M)∈R 2 + :C+𝜆M=𝐵 𝑈 𝐷},(17)
whereC denotes total conversions andM denotes total revenue in the deployment window. This line contains
all revenue–conversion bundles that deliver exactly the same scalarized reward as the best uniform static
policy in deployment. Points above the line have a higher reward than the deployment uniform oracle, because
they deliver either more conversions for a given revenue level or more revenue for a given conversion level.
Points below the line have a lower reward. Thus, the iso-reward line provides a visual test of whether LAAL
improves the platform’s scalarized objective, not merely one of the two underlying outcomes. We plot this line
together with LAAL, and the static cohorts in Figure 13 (along with the historical query-dependent benchmark
discussed next). We see that LAAL clearly improves the reward compared to the best uniform fixed-ad load
policy.
8.2 Query-Dependent Benchmarks
Uniform static rules ignore the cross-query heterogeneity documented in§4.2. A stronger static benchmark
therefore allows the ad load to vary across queries, while still requiring the rule to remain fixed over time.
These benchmarks help separate two sources of improvement: the value ofquery sensitivityand the value of
time adaptivity. If a fixed query-level rule performs close to LAAL, then most of LAAL ’s gain comes from
choosing different ad loads for different queries. If LAAL outperforms such a rule, then its additional gain
comes from adapting within the same query as market conditions change.
Definition 5(Query-Dependent Static Policy Class).Let Π𝑄 denote the class of deterministic query-dependent
static policiesΠ 𝑄={𝜋:Q→A}, where𝜋(𝑞)is the fixed ad load assigned to query𝑞.
Since each uniform rule applies the same ad load to every query, uniform static policies are a special case
of query-dependent static policiesΠ𝑈⊆Π 𝑄.
For query-dependent benchmarks, whenever|S𝑊(𝑞,𝑖)|>0 , define the sample mean reward per search for
query𝑞under ad load𝑖as
b𝑟𝑊(𝑞,𝑖;𝜆):= 1 |S𝑊(𝑞,𝑖)| ∑︁ 𝑠∈S𝑊(𝑞,𝑖) 𝑟(𝑦𝑠,𝜆).(18)
32

Figure 13: Revenue–conversion comparison of LAAL with static benchmarks. The figure shows the static
cohorts, the iso-reward line induced by the deployment uniform oracle, and the historical query-dependent
benchmark.
Definition 6(Historical Query-Dependent Benchmark and Deployment Query-Dependent Empirical Oracle).
For𝑊∈{𝐻,𝐷}and any query𝑞with at least one observed query–ad-load cell in window𝑊, define
𝜋𝑄,★ 𝑊 (𝑞)∈arg max {𝑖∈A:|S 𝑊(𝑞,𝑖)|>0} b𝑟𝑊(𝑞,𝑖;𝜆).
For queries that do not appear in the historical window, set𝜋𝑄,★ 𝐻 (𝑞)=𝑖 def. We refer to𝜋𝑄,★ 𝐻 as the historical
query-dependent benchmark and to𝜋 𝑄,★ 𝐷 as the deployment query-dependent empirical oracle.
The historical query-dependent benchmark𝜋𝑄,★ 𝐻 is selected using the 66-day experiment window and is
therefore feasible ex ante before deployment. It represents the best fixed query-level rule the platform can
construct from historical experimental evidence. By contrast, the deployment query-dependent empirical
oracle𝜋𝑄,★ 𝐷 is selected using the 22-day deployment window itself. It is not a deployable policy; rather, it
is an ex post benchmark that asks how close LAAL comes to the best time-invariant query-level rule in the
realized deployment environment.
Historical query-dependent benchmark in deployment.We first evaluate the feasible ex ante benchmark
𝜋𝑄,★ 𝐻 using deployment-window outcomes. This comparison asks whether a query-sensitive static rule selected
from the earlier experiment would still perform well in the later deployment environment.
For each ad load𝑖∈A , define the set of queries assigned to𝑖 by the historical query-dependent benchmark,
𝑄𝐻 𝑖 :={𝑞∈Q:𝜋 𝑄,★ 𝐻 (𝑞)=𝑖} . Then, for any outcome𝑌∈{Revenue,Conversion} , define the IPW estimate
of the deployment-window total outcome under𝜋𝑄,★ 𝐻 as
bY𝑄 𝐻→𝐷(𝑌)= ∑︁
𝑖∈A
∑︁
𝑠∈S𝐷(𝑖)
1{𝑞𝑠∈𝑄 𝐻 𝑖}
𝑤𝑖
𝑌𝑠.(19)
33

The estimator uses deployment searches from static cohort𝑖 whenever the historical query-dependent rule
would have assigned the corresponding query to ad load𝑖, and rescales by the static cohort traffic share𝑤𝑖. Thus,
it evaluates a historically selected query-level rule in the deployment environment using contemporaneous
randomized support from the static arms.
Using𝑌=Revenue and𝑌=Conversion in Equation (19), we obtain the platform-level revenue and
conversion totals generated by the historical query-dependent benchmark during deployment and show it in
Figure 13. We see that the historical query-dependent benchmark improves the empirical revenue–conversion
trade-off relative to uniform static rules, confirming the value of query sensitivity. However, it remains
materially below LAAL. This gap shows that query sensitivity alone is not sufficient: a fixed query-level rule
selected from historical data can become stale when within-query market conditions shift during deployment.
Empirical regret relative to the deployment query-dependent empirical oracle.We next compare LAAL
to the deployment query-dependent empirical oracle𝜋𝑄,★ 𝐷 . This oracle is selected using deployment outcomes
themselves: for each query, it chooses the fixed ad load that performed best during the same 22-day deployment
window. It therefore could not have been implemented ex ante at the start of deployment. We use it instead as
an ex post diagnostic benchmark that measures how close LAAL comes to the best fixed query-level rule in
the realized deployment environment. LetS𝐷(𝑞,𝐿) denote the set of deployment-window searches for query
𝑞 served by the LAAL arm. Whenever|S𝐷(𝑞,𝐿)|>0 , define LAAL ’s deployment-window mean reward on
query𝑞as
b𝑟𝐿 𝐷(𝑞;𝜆)= 1 |S𝐷(𝑞,𝐿)| ∑︁ 𝑠∈S𝐷(𝑞,𝐿) 𝑟(𝑦𝑠,𝜆).(20)
For each query𝑞, we define LAAL ’s query-level empirical regret relative to the deployment query-dependent
empirical oracle as
EmpReg(𝑞)=b𝑟𝐷

𝑞,𝜋 𝑄,★ 𝐷 (𝑞);𝜆  −b𝑟𝐿 𝐷(𝑞;𝜆),(21)
This quantity is the per-search reward gap between LAAL and the best fixed ad load for query𝑞, where the
fixed ad load is chosen ex-post from deployment data. The deployment query-dependent empirical oracle,
b𝑟𝐷

𝑞,𝜋 𝑄,★ 𝐷 (𝑞);𝜆  , is an upper benchmark within the class of time-invariant query-level rules. It assigns
a single ad load to each query for the entire deployment window based on ex-post optimal ad load during
deployment. As such, it is an infeasible benchmark. LAAL, by contrast, can change the ad load for the same
query over time. Therefore, empirical regret can be negative for queries where within-query non-stationarity
allows LAAL to outperform any single fixed ad load over the evaluation window.
For the empirical analysis, we restrict our attention to the 2,451 queries that consistently maintained
sufficient support for LAAL ’s greedy selection, i.e., queries with at least 100 searches during every rolling
3-day window. We rank these queries by deployment search frequency from highest to lowest and report
mean empirical regret within bins of that ranking in Figure 14. We construct 95% confidence intervals
using bootstrap resampling at the query level. Mean empirical regret declines with query frequency: in the
highest-frequency bins, the confidence intervals include zero, indicating that LAAL performs nearly as well as
the best query-dependent static rule when local support is ample. Empirical regret is larger in lower-frequency
bins, where local estimation is noisier.
Taken together, the query-dependent benchmark comparisons deliver two takeaways. First, allowing ad
34

Figure 14: Average empirical regret per search of LAAL relative to the deployment query-dependent empirical
oracle, by query-volume bin. The sample is restricted to the 2,451 queries.
load to vary across queries improves over uniform static rules, confirming the importance of query sensitivity.
Second, LAAL continues to outperform the historical query-dependent benchmark and exhibits near-zero
empirical regret relative to the deployment query-dependent empirical oracle on the highest-volume queries.
Thus, LAAL ’s gains come not only from choosing different ad loads for different queries, but also from
adapting ad load within the same query as market conditions evolve.
9 Discussion and Robustness Checks
The benchmark results above show that LAAL improves the revenue–conversion frontier relative to both
uniform and query-dependent static policies. We now examine two additional concerns about the interpretation
of these gains. First, we ask whether LAAL ’s performance is stable throughout the deployment window, rather
than being driven by short-lived launch-period effects. Second, we ask whether the gains are driven solely
by brand-query mechanics, where the focal brand advertiser’s participation decision may interact with the
platform’s ad-load policy.
9.1 Performance Over Time
One potential concern with the deployment results is that they may not be stable over the evaluation window.
Launch-period effects could inflate early gains, and performance may erode as advertisers adjust their bids,
budgets, or participation. Such responses would appear as changes in observed query-level rewards, which
LAAL is designed to accommodate through its sliding-window updates and which are captured as reward drift
in Theorem 1. Nevertheless, whether LAAL ’s relative performance remains stable during deployment is an
empirical question.
We assess whether LAAL ’s improvement is stable over time by testing for a linear trend in daily outcomes
relative to the control group. For each outcome𝑌∈{Revenue,Conversion}and date𝑑, we estimate
𝑌𝐿,𝑑 =𝛼 𝑌𝑌𝐶,𝑑 +𝛽 𝑌𝑑+𝜀 𝑌,𝑑,(22)
where𝑌𝐿,𝑑 and𝑌𝐶,𝑑 denote the LAAL and control IPW-scaled totals on day 𝑑, respectively, and 𝑑 is
mean-centered within the 22-day window. In this specification,𝛼𝑌 captures the average multiplicative change
in LAAL relative to control, controlling for common day-to-day shocks through𝑌𝐶,𝑑 , while𝛽𝑌 tests whether
35

LAAL ’s relative performance drifts over time.
Table 8: LAAL vs. Control With Time Trend
Revenue Conversion
Relative change𝛼1.3685 ∗∗∗ (0.0421) 0.9891 ∗∗∗ (0.0016)
Trend𝛽487.04 (884.65) -5.05 (4.5351)
Observations 22 22
Standard errors in parentheses. Significance: ∗𝑝 <0.05,∗∗𝑝 <0.01,∗∗∗𝑝 <0.001.
Table 8 reports the estimates. Consistent with the results from§7.1, LAAL increases revenue by 36.8% and
decreases conversions by 1.1% relative to the control condition. Importantly, the estimated trend coefficients
𝛽𝑌 are statistically indistinguishable from zero for both outcomes, suggesting that LAAL ’s relative performance
did not erode over the 22-day evaluation window. Nevertheless, we caution that 22 days may be too short for
advertisers to fully re-optimize. The analysis therefore establishes stability over the observed deployment
window, but does not rule out slower or longer-run equilibrium responses.
9.2 Robustness Beyond Brand Queries
For brand queries, the platform often shows more ads, and the focal brand’s decision to advertise can affect
which layouts are observed and how profitable additional slots are. This creates the possibility that advertiser
behavior and the platform’s ad-allocation rule interact: if the brand’s propensity to advertise is itself affected
by the realized ad load, then LAAL ’s performance on brand queries may partially reflect this strategic response
rather than purely mechanical reallocation.
As a robustness check, we therefore repeat the main revenue–conversion comparison from §7.1 on
non-brandqueries only, where no single advertiser is sufficiently prominent to plausibly manipulate the overall
design. The results are reported in Figure 15. On non-brand queries, LAAL continues to outperform all
non-control static cohorts in conversions, and it dominates all alternatives in revenue except the highest ad-load
cohorts (𝑇5 and𝑇6). These results indicate that the gains from LAAL are not driven solely by brand-query
mechanics; substantial improvements persist in the broader set of non-brand queries.
10 Conclusion
Ad-load design is a central supply-side decision in sponsored search: increasing sponsored inventory can
raise short-run revenue, but may also crowd out relevant organic results and reduce user-side outcomes.
Using a 66-day user-level randomized field experiment, we document this revenue–conversion trade-off at
scale. Higher ad loads substantially increase advertising revenue, but reduce total search conversions and
engagement. We further show that these effects are neither homogeneous nor stable over time. Additional
slots generate large revenue gains on queries with high-conversion advertisers, but little or no incremental
revenue on queries where ads convert poorly. Within-query variation in brand-advertiser presence further
shows that the revenue–conversion frontier can shift as market conditions change.
Motivated by these findings, we design and deploy exploration-augmented Locally Adaptive Ad Load
(e-LAAL). The deployed architecture combines LAAL, a model-free query-level policy that uses recent
36

Figure 15: Revenue–conversion across fixed ad-load cohorts, LAAL, and e-LAAL onNon-BrandQueries.
outcomes to adapt the number of sponsored slots, with persistent static exploration arms that maintain support
and provide fixed-policy counterfactuals. In a 22-day production deployment serving over 22 million users
and 77 million searches, LAAL recommends 3.1 ads per search on average and improves the empirical
revenue–conversion frontier relative to deployed static benchmarks. It achieves revenue comparable to
high-ad-load static policies while preserving conversions closer to low-ad-load benchmarks. The policy’s
recommendations are economically interpretable: it shows fewer ads when advertiser quality is low or the
brand advertiser is absent, and more ads when sponsored demand is valuable or the brand advertiser is active.
The e-LAAL architecture also provides a practical and theoretically grounded way to implement adaptive
ad-load allocation. By maintaining parallel static exploration arms, the platform preserves support for every
ad-load level and obtains contemporaneous fixed-policy counterfactuals, while the adaptive arm exploits
recent local evidence. We provide a finite-time, high-probability dynamic-regret guarantee for e-LAAL that
accounts for non-stationarity, sliding-window estimation, and deviations between designed traffic shares and
realized query-level support. Empirically, LAAL outperforms both uniform static benchmarks and historical
query-dependent static benchmarks, and exhibits near-zero empirical regret on high-volume queries relative to
an ex post deployment oracle.
Together, the results show that ad load should not be treated as a fixed platform-wide parameter or as
a time-invariant query-level rule. Effective ad-load design must be both query-sensitive and time-adaptive.
More broadly, the paper shows that sponsored-search platforms can ease the revenue–consumer-experience
trade-off not only through auction design, pricing, ranking, or targeting, but also by dynamically controlling
the supply of sponsored attention. LAAL provides a lightweight, scalable, and portable blueprint for doing so
in large-scale, non-stationary sponsored-search markets.
Funding and Competing Interests
The first author was a paid intern at the company that provided the data when the experiments were conducted.
The company had no input or constraints on what is reported in the manuscript.
37

References
Y. Abbasi-Yadkori, D. P´al, and C. Szepesv´ari. Improved algorithms for linear stochastic bandits. InAdvances in Neural
Information Processing Systems 24, pages 2312–2320, 2011. URL https://proceedings.neurips.cc/paper/
2011/hash/e1d5be1c7f2f456670de3d53c7b54f4a-Abstract.html.
S. Agrawal and N. Goyal. Thompson sampling for contextual bandits with linear payoffs. InProceedings of the 30th
International Conference on Machine Learning, volume 28 ofProceedings of Machine Learning Research, pages
127–135. PMLR, 2013. URLhttps://proceedings.mlr.press/v28/agrawal13.html.
Apple Ads. Ads on the app store.https://ads.apple.com/app-store, 2026. Accessed: 2026-06-02.
S. Athey and G. Ellison. Position auctions with consumer search.Quarterly Journal of Economics, 126(3):1213–1270,
2011. doi: 10.1093/qje/qjr028.
A. Broder, M. Fontoura, V. Josifovski, and L. Riedel. To swing or not to swing: Learning when (not) to advertise. In
Proceedings of the 17th ACM Conference on Information and Knowledge Management (CIKM), pages 1003–1012.
ACM, 2008. doi: 10.1145/1458082.1458215. URLhttps://fontoura.org/papers/cikm2008-swing.pdf.
A. Carri ´on, J. Wang, H. S. Nair, W. Xu, and Y. Zhang. Blending advertising with organic content in e-commerce:
A virtual bids optimization approach. InProceedings of the AAAI Conference on Artificial Intelligence (AAAI),
volume 37, pages 4141–4149. AAAI Press, 2023. doi: 10.1609/aaai.v37i4.25629. Also available as arXiv preprint
arXiv:2105.13556.
E. Cavenaghi, G. Sottocornola, F. Stella, and M. Zanker. Non-stationary multi-armed bandit: Empirical evaluation of a
new concept drift-aware algorithm.Entropy, 23(3):380, 2021. doi: 10.3390/e23030380.
M. Cheng, E. Ofek, and H. Yoganarasimhan. Balancing engagement and polarization: Multi-objective alignment of
news content using llms.arXiv preprint arXiv:2504.13444, 2025.
W. C. Cheung, D. Simchi-Levi, and R. Zhu. Learning to optimize under non-stationarity. InProceedings of the
Twenty-Second International Conference on Artificial Intelligence and Statistics (AISTATS), volume 89 ofProceedings
of Machine Learning Research, pages 1079–1087. PMLR, 2019.
W. Chu, L. Li, L. Reyzin, and R. Schapire. Contextual bandits with linear payoff functions. InProceedings of the
Fourteenth International Conference on Artificial Intelligence and Statistics, volume 15 ofProceedings of Machine
Learning Research, pages 208–214. PMLR, 2011. URL https://proceedings.mlr.press/v15/chu11a.html.
K. Deb, K. Sindhya, and J. Hakanen. Multi-objective optimization. InDecision sciences, pages 161–200. CRC Press,
2016.
B. Edelman, M. Ostrovsky, and M. Schwarz. Internet advertising and the generalized second-price auction: Selling
billions of dollars worth of keywords.American Economic Review, 97(1):242–259, 2007. doi: 10.1257/aer.97.1.242.
URLhttps://doi.org/10.1257/aer.97.1.242.
A. Garivier and ´E. Moulines. On upper-confidence bound policies for switching bandit problems. InInternational
Conference on Algorithmic Learning Theory (ALT), pages 174–188, 2011. doi: 10.1007/978-3-642-24412-4 16.
URLhttps://doi.org/10.1007/978-3-642-24412-4_16.
A. Goldfarb and C. E. Tucker. Privacy regulation and online advertising.Management Science, 57(1):57–71, 2011. doi:
10.1287/mnsc.1100.1246.
A. Goli, J. Huang, D. Reiley, and N. M. Riabov. Measuring consumer sensitivity to audio advertising: a long-run field
experiment on pandora internet radio.Quantitative Marketing and Economics, pages 1–31, 2025a.
A. Goli, D. H. Reiley, and H. Zhang. Personalizing ad load to optimize subscription and ad revenues: Product strategies
constructed from experiments on pandora.Marketing Science, 44(2):327–352, 2025b. doi: 10.1287/mksc.2022.0357.
URLhttps://pubsonline.informs.org/doi/10.1287/mksc.2022.0357.
D. G. Horvitz and D. J. Thompson. A generalization of sampling without replacement from a finite universe.Journal of
the American Statistical Association, 47(260):663–685, 1952. doi: 10.1080/01621459.1952.10483446.
38

Interactive Advertising Bureau. Internet advertising revenue report: Full-year 2025 results. https:
//www.iab.com/wp-content/uploads/2026/04/IAB_PwC_Internet_Ad_Revenue_Report_Full_Year_
2025_April_2026.pdf, Apr. 2026. Accessed: 2026-06-01.
L. Jain, Z. Li, E. Loghmani, B. Mason, and H. Yoganarasimhan. Effective adaptive exploration of prices and promotions
in choice-based demand models.Marketing Science, 43(5):1002–1030, 2024.
A. Kim, S. Balachander, and K. Kannan. On the optimal number of advertising slots in a generalized second-price
auction.Marketing Letters, 23(3):851–868, Sept. 2012. doi: 10.1007/s11002-012-9193-2.
R. Kohavi, A. Deng, B. Frasca, R. Longbotham, T. Walker, and Y. Xu. Trustworthy online controlled experiments: Five
puzzling outcomes explained. InProceedings of the 18th ACM SIGKDD international conference on Knowledge
discovery and data mining, pages 786–794, 2012.
S. Lahaie and D. M. Pennock. Revenue analysis of a family of ranking rules for keyword auctions. InProceedings of the
8th ACM Conference on Electronic Commerce (EC), pages 50–56, 2007. doi: 10.1145/1250910.1250918.
T. Lattimore and C. Szepesv´ari.Bandit algorithms. Cambridge University Press, 2020.
R. P. Leme et al. A field guide to personalized reserve prices, 2016. arXiv preprint.
L. Li, W. Chu, J. Langford, and R. E. Schapire. A contextual-bandit approach to personalized news article recommendation.
InProceedings of the 19th international conference on World wide web, pages 661–670, 2010.
G. Liao, Z. Wang, X. Wu, X. Shi, C. Zhang, Y. Wang, X. Wang, and D. Wang. Cross DQN: Cross deep Q network for
ads allocation in feed, 2021. URLhttps://arxiv.org/abs/2109.04353. Accepted by WWW ’22.
S. Moshary. Does sponsored search advertising augment organic search? evidence from an e-commerce platform.
Management Science, mar 2025. doi: 10.1287/mnsc.2024.04792. URL https://doi.org/10.1287/mnsc.2024.
04792. Articles in Advance.
R. B. Myerson. Optimal auction design.Mathematics of Operations Research, 6(1):58–73, Feb. 1981. doi: 10.1287/
moor.6.1.58. URLhttps://pubsonline.informs.org/doi/10.1287/moor.6.1.58.
M. Ostrovsky and M. Schwarz. Reserve prices in internet advertising auctions: A field experiment.Journal of Political
Economy, 131(12), 2023. doi: 10.1086/725702.
O. Rafieian and H. Yoganarasimhan. Targeting and privacy in mobile advertising.Marketing Science, 40(2):193–218,
2021. doi: 10.1287/mksc.2020.1235.
O. Rafieian, A. Kapoor, and A. Sharma. Multiobjective personalization of marketing interventions.Marketing Science,
44(2):457–477, 2025.
Y. Russac, C. Vernade, and O. Capp ´e. Weighted linear bandits for non-stationary environments. InAdvances in
Neural Information Processing Systems 32, pages 12040–12049, 2019. URL https://papers.nips.cc/paper/
9372-weighted-linear-bandits-for-non-stationary-environments.
H. Sagtani, M. G. Jhawar, R. Mehrotra, and O. Jeunen. Ad-load balancing via off-policy learning in a content marketplace,
2023. URLhttps://arxiv.org/abs/2309.11518.
N. S. Sahni and C. Zhang. Are consumers averse to sponsored messages? the role of search advertising in information
discovery.Quantitative Marketing and Economics, 22(1):63–114, 2024. doi: 10.1007/s11129-023-09270-z.
A. Sayedi. Real-time bidding in online display advertising.Marketing Science, 37(4):553–568, 2018. doi: 10.1287/
mksc.2017.1083.
W. Shi, C. Fu, Q. Xu, S. Chen, J. Zhang, Q. Zhu, Z. Hua, and S. Yang. Ads supply personalization via doubly robust learning.
InProceedings of the 33rd ACM International Conference on Information and Knowledge Management (CIKM ’24),
Boise, ID, USA, Oct. 2024. ACM. doi: 10.1145/3627673.3680035. URL https://arxiv.org/abs/2410.12799.
A. Simonov, C. Nosko, and J. M. Rao. Competition and crowd-out for brand keywords in sponsored search.Marketing
Science eJournal, 2017. URLhttps://api.semanticscholar.org/CorpusID:947920.
F. Tr`ov`o, S. Paladino, M. Restelli, and N. Gatti. Sliding-window thompson sampling for non-stationary settings.Journal
of Artificial Intelligence Research, 68:311–364, 2020. doi: 10.1613/jair.1.11407.
39

H. R. Varian. Position auctions.International Journal of Industrial Organization, 25(6):1163–1178, 2007. doi:
10.1016/j.ijio.2006.10.006.
B. Wang, Z. Li, J. Tang, K. Zhang, S. Chen, and L. Ru. Learning to advertise: How many ads are enough? In J. Z.
Huang, L. Cao, and J. Srivastava, editors,Advances in Knowledge Discovery and Data Mining: 15th Pacific-Asia
Conference, PAKDD 2011, Shenzhen, China, May 24–27, 2011, Proceedings, Part II, volume 6635 ofLecture Notes
in Computer Science, pages 506–518. Springer, 2011. doi: 10.1007/978-3-642-20847-8 42.
Y. Wang, L. Tao, and X. X. Zhang. Recommending for a multi-sided marketplace: A multi-objective hierarchical
approach.Marketing Science, 2024.
K. C. Wilbur. A two-sided, empirical model of television advertising and viewing markets.Marketing Science, 27(3):
356–378, May 2008. doi: 10.1287/mksc.1070.0303. URL https://pubsonline.informs.org/doi/10.1287/
mksc.1070.0303.
K. C. Wilbur, L. Xu, and D. Kempe. Correcting audience externalities in television advertising.Marketing Science, 32
(6):892–912, 2013.
M. Yan, J. Xu, A. A. Tiwana, and M. Chatterjee. Ads allocation in feed via constrained optimization. InProceedings
of the 26th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), pages
3299–3307. ACM, 2020. doi: 10.1145/3394486.3403391.
S. Yao and C. F. Mela. A dynamic model of sponsored search advertising.Marketing Science, 30(3):447–468, 2011.
doi: 10.1287/mksc.1100.0626.
Z. Ye, D. J. Zhang, H. Zhang, R. Zhang, X. Chen, and Z. Xu. Cold start to improve market thickness on online advertising
platforms: Data-driven algorithms and field experiments.Management Science, 69(7):3838–3860, 2023.
H. Yoganarasimhan. Search personalization using machine learning.Management Science, 66(3):1045–1070, 2020.
H. Yoganarasimhan, E. Barzegary, and A. Pani. Design and evaluation of optimal free trials.Management Science, 69
(6):3220–3240, 2023.
S. Yuan, J. Wang, B. Chen, P. Mason, and S. Seljan. An empirical study of reserve price optimisation in real-time
bidding. InProceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data
Mining (KDD), pages 1897–1906. ACM, 2014. doi: 10.1145/2623330.2623357.
W. Zhang, C. Wei, X. Meng, Y. Hu, and H. Wang. The whole-page optimization via dynamic ad allocation. InCompanion
Proceedings of the The Web Conference 2018 (WWW ’18), pages 1407–1411, Lyon, France, 2018. ACM. ISBN
978-1-4503-5640-4. doi: 10.1145/3184558.3191584. URLhttps://doi.org/10.1145/3184558.3191584.
40

Appendices
A Brand Query Layouts
(a) Brand Query Single-Ad Layout
 (b) Brand Query Three-Ad Layout Example
Figure A1: Examples of brand query layouts: in (a), the brand appears as the sponsored Ad 1; in (b), it appears
as Organic 1.
B Data Distributions
B.1 CDF of Search Frequency
Figure A2: Cumulative distribution of search frequency of queries
B.2 CDF of Impressions and Conversions
The blue and green curves in Figure A3 show the cumulative distribution of conversions and impressions
respectively. Notice that “Conversion” CDFs lie above the corresponding “Impression” CDFs. This suggests
that conversions are more concentrated (across both apps and ads) than impressions.
i

(a) CDF of Apps (Organic and Ads).
 (b) CDF of Ads.
Figure A3: Cumulative distribution of Conversions and Impressions
C Platform Usage
C.1 Engagement
We evaluate whether daily engagement changes under higher ad loads. Let𝑑 be mean-centered time within
the experiment window (in days). We estimate a condition-specific levels-and-trends model with the control
group as baseline:
Engagement𝑒,𝑑 =(𝛽 𝐶 +𝛿 𝐶𝑑) +
6∑︁
𝑗=2
(𝛽𝑇𝑗+𝛿𝑇𝑗𝑑)1{𝑒=𝑇 𝑗} +𝜀𝑒,𝑑 (A1)
Engagement𝑒,𝑑 measures the daily engagement under experimental condition𝑒 on day𝑑. Here, 𝛽𝐶 and𝛿𝐶
estimate the mean engagement and time trend of the control group respectively. If engagement trends under
control are absent, we expect𝛿𝐶 to be statistically indistinguishable from zero. 𝛽𝑇𝑗 and𝛿𝑇𝑗 estimate the level
difference for condition𝑇𝑗 and the incremental trend difference for condition𝑇𝑗 relative to control respectively.
Table A1 reports the estimates: Engagement levels decline monotonically with ad load. The control trend
𝛿𝐶 is small and not statistically significant, indicating no intrinsic drift in engagement absent additional ads.
In contrast, we observe significantly negative incremental trends for𝑇4–𝑇6, implying that daily engagement
erodes over time under extreme ad loads. If the experiment were extended, this pattern suggests further
engagement losses in𝑇 4–𝑇6 relative to control.
C.2 Search per User
We now test whether higher ad loads induce additional search activity. Let SearchesPerUser𝑢 denote the total
number of search queries executed by user𝑢during the experiment:
SearchPerUser𝑢=
∑︁
𝑠
1{𝑢𝑠 =𝑢}
ii

Table A1: Daily Engagement: Condition Levels and Trends per Day
Daily Engagement Trend
𝐶4.95e-02 ∗∗∗ (1.00e-03) 5.82e-05 (3.16e-05)
𝑇2 -3e-04∗∗∗ (4.83e-05) 1.45e-06 (2.47e-06)
𝑇3 -6e-04∗∗∗ (4.63e-05) -1.11e-06 (3.08e-06)
𝑇4 -8e-04∗∗∗ (5.79e-05) -9.76e-06 ∗∗ (3.65e-06)
𝑇5 -10e-04∗∗∗ (4.96e-05) -6.38e-06 ∗ (3.01e-06)
𝑇6 -11e-04∗∗∗ (4.96e-05) -9.97e-06 ∗∗ (3.16e-06)
Observations 396 396
Standard errors in parentheses are clustered at the day level. Significance levels:∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
With control as the baseline, we estimate:
SearchesPerUser𝑢 =𝜁 𝐶 +
6∑︁
𝑗=2
𝜁𝑇𝑗 1{𝑒(𝑢)=𝑇 𝑗} +𝜀𝑢 (A2)
where𝜁𝐶 is the average under𝐶 and𝜁𝑇𝑗 estimates the deviation for condition𝑇𝑗 relative to𝐶. Table A2
presents the estimates. It shows that search intensity is higher under larger ad loads: coefficients for𝑇3–𝑇6 are
positive and highly significant, with the largest increase in𝑇6 (0.171 additional searches per user). Relative to
the control mean of𝜁 𝐶 =5.1389, this corresponds to approximately a 3.3% increase.
Table A2: Searches per User by Condition
Searches per User
𝐶5.1389 ∗∗∗ (0.0060)
𝑇2 0.0199 (0.0170)
𝑇3 0.1620∗∗∗ (0.0170)
𝑇4 0.1673∗∗∗ (0.0170)
𝑇5 0.1412∗∗∗ (0.0160)
𝑇6 0.1710∗∗∗ (0.0160)
Observations 5,057,952
Standard errors in parentheses. Significance levels: ∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
C.3 Engagement During Deployment
We also examine engagement during the deployment period. For each date and condition, engagement is
defined as the fraction of assigned users who performed at least one search. We estimate average differences
relative to LAAL while absorbing common date shocks:
Engagement𝑒,𝑑 =𝛼 𝐿 +𝛽 𝐶1{𝑒=𝐶} +
6∑︁
𝑗=2
𝛽𝑇𝑗 1{𝑒=𝑇 𝑗} +𝛾𝑑 +𝜀 𝑒,𝑑.(A3)
iii

Here, LAAL is the omitted condition and𝛾𝑑 denotes date fixed effects. Thus, 𝛽𝐶 and𝛽𝑇𝑗 measure average
engagement differences relative to LAAL after controlling for day-level shocks.
Table A3 reports the results.𝐶 and𝑇2 have higher engagement than LAAL, while the other static conditions
have lower engagement than LAAL. However, only the effects of𝑇4 and𝑇6 are statistically significant. This
limited significance is expected because the deployment period contains only 22 days of data.
Table A3: Deployment Engagement Relative to LAAL
Daily Engagement
LAAL 8.43e-02 ∗∗∗ (6.19e-04)
𝐶1.69e-04 (3.66e-04)
𝑇2 1.09e-04 (3.86e-04)
𝑇3 -4.72e-04 (3.71e-04)
𝑇4 -9.55e-04∗ (3.89e-04)
𝑇5 -6.44e-04 (4.13e-04)
𝑇6 -7.87e-04∗ (3.75e-04)
Observations 154
Standard errors in parentheses. The LAAL row reports the baseline engagement level. Other rows report differences relative to LAAL.
Estimates are from Equation (A3). Significance levels: ∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
D Query Segmentation Results
D.1 Query Segmentation Summary Statistics
Table A4 summarizes the distribution share of outcomes across query segments introduced in 4.2.1.14. Most
of revenue and advertising conversion come from the segment𝐾3. The segment 𝐾1 contributes the most to the
total search and conversion share while it has a small share to the advertising results.
Table A4: Query Segment Composition. Numbers show the shares under each variable.
Segment #Queries Search Revenue Ads Conversion Conversion
K1 3,333 0.468 0.188 0.091 0.450
K2 3,334 0.069 0.153 0.100 0.092
K3 3,333 0.059 0.553 0.733 0.081
D.2 Regression Estimates
Table A5 presents the regression estimates from Equation (5).
E Conditional Cohort-Invariance Assumption
LAAL uses observations from the adaptive cohort and the static cohorts to estimate query–ad-load outcomes.
This requires that, after conditioning on the same query, ad load, and time, the cohort label does not contain
14Queries outside this 10k set account for the remaining mass:40.41% of searches, 10.58% of revenue,37.67% of total conversions,
and 7.61% of ad conversions.
iv

Table A5: Effect of Ad Load on Revenue and Conversion Across Segments
Revenue Conversion
Low Medium High Low Medium High
𝐶3.368 16.212 62.741 0.547 0.763 0.781
𝑇2 -0.427 (0.218) -0.094 (0.536) 14.136 ∗∗∗ (3.327) -0.011∗∗∗ (0.003) -0.025∗∗∗ (0.003) -0.016∗∗∗ (0.003)
𝑇3 -0.621∗∗ (0.199) 2.047∗∗∗ (0.547) 20.701∗∗∗ (4.252) -0.009 ∗∗ (0.003) -0.023 ∗∗∗ (0.004) -0.030∗∗∗ (0.004)
𝑇4 -0.510∗∗ (0.189) 2.330∗∗∗ (0.524) 25.432∗∗∗ (5.027) -0.017∗∗∗ (0.003) -0.037∗∗∗ (0.004) -0.033∗∗∗ (0.005)
𝑇5 -0.177 (0.173) 3.526 ∗∗∗ (0.674) 28.927∗∗∗ (4.743) -0.024∗∗∗ (0.005) -0.036∗∗∗ (0.006) -0.049∗∗∗ (0.004)
𝑇6 -0.255 (0.180) 4.828 ∗∗∗ (0.665) 32.887∗∗∗ (5.018) -0.033∗∗∗ (0.006) -0.060∗∗∗ (0.005) -0.052∗∗∗ (0.005)
Obs. 12,313,120 1,825,671 1,548,914 12,313,120 1,825,671 1,548,914
𝑅2 0.001 0.010 0.072 0.176 0.048 0.029
Notes:Standard errors in parentheses are clustered at the query level. Significance levels: ∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
additional information about immediate search-level outcomes. We evaluate this condition by estimating two
regressions, one for revenue and one for conversion:
𝑌𝑠 =𝛼𝑌 𝑞𝑠,𝑎𝑠,ℎ𝑠+
6∑︁
𝑖=1
𝛽𝑌 𝑖 1{𝑒𝑠 =𝐿𝐴𝐴𝐿}1{𝑎 𝑠 =𝑖}+𝜀 𝑌 𝑠,(A4)
where𝑌𝑠∈{Revenue 𝑠,Conversion𝑠},𝑞𝑠 is the query,𝑎𝑠 is the realized ad load, andℎ𝑠 is the calendar-hour
of the search. The fixed effects𝛼𝑌 𝑞𝑠,𝑎𝑠,ℎ𝑠 absorb all query-by-ad-load-by-hour variation. Thus, each coefficient
𝛽𝑌 𝑖 measures whether the LAAL cohort has additional explanatory power for outcome 𝑌, relative to the
corresponding static cohort with the same realized ad load.
Table A6 reports the results. The conversion coefficients are small and statistically insignificant across all
ad loads. For revenue, only the LAAL-versus-𝐶 comparison at one ad is statistically significant. To assess its
economic magnitude, note that Table 6 implies a control reward per search of approximately
2.152+0.01×25.80
3.44 =0.701.
The significant revenue coefficient, 0.199, changes the policy reward by only0.01×0.199=0.002 , which is
0.002/0.701≈0.28% of the control reward per search. Thus, although statistically detectable, the effect is
economically negligible. Overall, the results do not provide economically meaningful evidence that cohort
identity explains remaining revenue or conversion variation after controlling for query-by-ad-load-by-hour
fixed effects.
F Regret Guarantee for e-LAAL
This appendix gives the finite-sample dynamic-regret guarantee for e-LAAL for a fixed query𝑞. It provides
the detailed definitions, support conditions, and tuning argument behind Theorem 1.
Query-level sequence and rewards.Fix a query 𝑞, and letS𝑞(𝑇)={𝑠 1,...,𝑠 𝑁} be the realized searches
containing 𝑞 during[0,𝑇] , ordered by time. Write 𝑡𝑗 :=𝑡 𝑠𝑗 , 𝑒𝑗 :=𝑒 𝑠𝑗 , and 𝑎𝑗 :=𝑎 𝑠𝑗 . We identify the
static cohort 𝐶 with arm 1, and the static cohort 𝑇𝑖 with arm 𝑖 for𝑖=2,...,𝐾 . Thus the action set is
v

Table A6: Testing Cohort Effects Conditional on Query–Ad-Load–Hour Fixed Effects
Revenue Conversion
LAAL vs.𝐶, 1 ad 0.199 ∗ (0.080) 0.008 (0.004)
LAAL vs.𝑇 2, 2 ads 0.305 (1.888) 0.003 (0.071)
LAAL vs.𝑇 3, 3 ads 6.592 (3.434) -0.005 (0.123)
LAAL vs.𝑇 4, 4 ads 15.971 (9.870) -0.023 (0.110)
LAAL vs.𝑇 5, 5 ads 0.290 (0.594) 0.009 (0.012)
LAAL vs.𝑇 6, 6 ads 4.011 (4.108) 0.008 (0.032)
Query×Ad Load×Hour FE✓ ✓
Obs. 77,601,057 77,601,057
𝑅2 0.141 0.024
Notes:Each column estimates Equation (A4) on the full deployment search sample. Each row reports the LAAL coefficient for
realized ad load𝑖, comparing LAAL searches with the corresponding static cohort after absorbing the fixed effects. Standard errors in
parentheses are clustered at the query level. Significance levels:∗∗∗𝑝 <0.001,∗∗𝑝 <0.01,∗𝑝 <0.05.
A={1,...,𝐾}, and the cohort set is{𝐿}∪A, where𝐿denotes the LAAL cohort.
Let the raw scalarized reward be
𝑟raw 𝑗 :=𝑟(𝑦 𝑠𝑗,𝜆)=𝜆Revenue 𝑠𝑗+Conversion𝑠𝑗,0≤𝑟 raw 𝑗 ≤𝐵 𝑟 <∞.
For the proof, normalize rewards by𝐵𝑟: ˜𝑟𝑗 :=𝑟 raw 𝑗 /𝐵𝑟∈[0,1] . All mean rewards, variation budgets, regret
quantities, and the tie-break parameter𝜂 in this appendix are expressed in normalized units. Bounds in raw
reward units are recovered by multiplying by𝐵𝑟.
For each arm𝑖∈A, define the possibly time-varying mean reward
𝜇𝑖,𝑗 :=E[˜𝑟𝑗|𝑎 𝑗 =𝑖,𝑞].
Let𝑖★ 𝑗∈arg max𝑖∈A 𝜇𝑖,𝑗 . The dynamic regret over[0,𝑇]is
𝑅dyn 𝑞 (𝑇):=
𝑁∑︁
𝑗=1
𝜇𝑖★ 𝑗,𝑗−𝜇 𝑎𝑗,𝑗 ,
and the query-level variation budget, with𝑉𝑞(𝑇)>0, is
𝑉𝑞(𝑇):=
𝑁∑︁
𝑗=2
max
𝑖∈A
|𝜇𝑖,𝑗−𝜇 𝑖,𝑗−1|.
Design weights and query-level support.Let 𝑤𝑒 denote the pre-assigned user-level cohort weights, with
𝑤𝐿+ ˝𝐾 𝑖=1𝑤𝑖 =1 . Define the total static design mass 𝜖:= ˝𝐾 𝑖=1𝑤𝑖 =1−𝑤 𝐿, and let 𝑤min :=min 𝑖∈A 𝑤𝑖.
User assignment is fixed by design, but for a fixed query 𝑞, realized query-level traffic may not match the
user-level design shares. Let𝜀𝑒,𝑗 :=Pr(𝑒 𝑗 =𝑒) denote the expected share of the 𝑗th query-𝑞 search coming
vi

from cohort𝑒. We assume that there exist constants𝑐 ∈(0,1]and ¯𝑐≥1 such that, for every search𝑗,
𝜀𝑖,𝑗 ≥𝑐 𝑤𝑖,∀𝑖∈A,(A5)
and
𝐾∑︁
𝑖=1
𝜀𝑖,𝑗 ≤¯𝑐𝜖.(A6)
The coefficient𝑐 is the minimum-support coefficient: it lower bounds realized query-level traffic on each static
arm by its design weight. The coefficient ¯𝑐is the total-static-traffic upper-bound coefficient: it upper bounds
total realized static-cohort traffic by the total design exploration mass. If realized query-level static traffic
exactly matches the design exploration shares, then𝑐 =¯𝑐=1.
Sliding-window estimation and fallback.At each search𝑠 𝑗, LAAL uses the most recentℎunits of time:
𝑊𝑗(ℎ):={ℓ< 𝑗:𝑡 𝑗−ℎ≤𝑡 ℓ <𝑡 𝑗}.
Because the searches are ordered by time, write𝑊𝑗(ℎ)={𝑏 𝑗,...,𝑗−1} , and let𝑀𝑗 :=|𝑊 𝑗(ℎ)|=𝑗−𝑏 𝑗.
Define the number of warm-up searches 𝑁ℎ :=|{𝑗≤𝑁:𝑡 𝑗−𝑡 𝑠1 < ℎ}|, and set 𝐽ℎ :=𝑁 ℎ+1 . Thus, for
𝑗≥𝐽 ℎ, the lookback window is not truncated by the start of the horizon.
Define the post-warm-up index sets
J𝐺(ℎ,𝑚):={𝑗∈{𝐽 ℎ,...,𝑁}:𝑀 𝑗≥𝑚},J 𝐹(ℎ,𝑚):={𝑗∈{𝐽 ℎ,...,𝑁}:𝑀 𝑗 <𝑚}.
The realized LAAL greedy and fallback rounds are 𝑆𝐺 𝐿 :={𝑗∈ J 𝐺(ℎ,𝑚):𝑒 𝑗 =𝐿} and 𝑆𝐹 𝐿 :={𝑗∈
J𝐹(ℎ,𝑚):𝑒 𝑗 =𝐿} . The post-warm-up static rounds are 𝑆+ 𝑆 :={𝑗∈{𝐽 ℎ,...,𝑁}:𝑒 𝑗∈A} , and the fallback
count is𝐹𝑞(𝑇;ℎ,𝑚):=|𝑆 𝐹 𝐿|. WhenJ 𝐺(ℎ,𝑚)≠∅, define
𝑀(𝑚) − :=min 𝑗∈J𝐺(ℎ,𝑚) 𝑀𝑗, 𝑀 (𝑚) + :=max 𝑗∈J𝐺(ℎ,𝑚) 𝑀𝑗.
For each arm𝑖∈A, let
𝑛𝑖,𝑗 :=
∑︁
ℓ∈𝑊𝑗(ℎ)
1{𝑎ℓ =𝑖}
be the number of action-𝑖observations in the window. The LAAL estimator is
b𝜇𝑖,𝑗 =
˝
ℓ∈𝑊𝑗(ℎ) ˜𝑟ℓ 1{𝑎ℓ =𝑖}
𝑛𝑖,𝑗+𝛿 sm
.
Here 𝛿sm >0 . On post-warm-up LAAL rounds, for tie-break penalty 𝜂 >0 , the algorithm plays 𝑎𝑗 ∈
arg max𝑖∈A{b𝜇𝑖,𝑗 −𝜂𝑖} for 𝑗∈𝑆 𝐺 𝐿 , and plays the default 𝑎𝑗 =𝑖 def for 𝑗∈𝑆 𝐹 𝐿 . On static rounds, cohort 𝑖
deterministically plays action𝑖.
Assumptions.(E1) ˜𝑟 𝑗∈[0,1]for all𝑗.
(E2) Conditional on the realized query-search sequence S𝑞(𝑇) , the cohort of each search is drawn
vii

independently across searches, with query-level cohort shares satisfying (A5) and (A6).
(E3) For each arm 𝑖, the noise ˜𝑟𝑗−𝜇 𝑖,𝑗 is conditionally mean-zero and bounded in[−1,1] on rounds
where𝑎 𝑗 =𝑖.
(E4) Conditional cohort invariance holds for immediate search-level rewards: after conditioning on
query𝑞, search time𝑡𝑗, and realized ad load𝑖, the conditional mean reward does not depend on whether the
observation comes from the LAAL cohort or the corresponding static cohort.
Lemma E.1 (Per-arm support from static cohorts).Assume J𝐺(ℎ,𝑚)≠∅ . For each 𝑖∈ A and
𝑗∈J 𝐺(ℎ,𝑚), define the number of static observations of arm𝑖inside the window:
𝑍𝑖,𝑗 :=
∑︁
ℓ∈𝑊𝑗(ℎ)
1{𝑒ℓ =𝑖}.
Then𝑛𝑖,𝑗 ≥𝑍 𝑖,𝑗 , because static cohort𝑖always plays action𝑖. The conditional mean of𝑍 𝑖,𝑗 is
𝑚𝑖,𝑗 :=
∑︁
ℓ∈𝑊𝑗(ℎ)
𝜀𝑖,ℓ≥𝑐 𝑤𝑖𝑀𝑗≥𝑐 𝑤min𝑀(𝑚) − .
By Assumption E2, for any𝛼∈(0,1),
Pr

𝑛𝑖,𝑗 <(1−𝛼)𝑐 𝑤min𝑀(𝑚) −

≤exp

−𝛼2
2 𝑐𝑤min𝑀(𝑚) −

.
A union bound over𝑖∈Aand𝑗∈J 𝐺(ℎ,𝑚)gives
Pr

∃𝑗∈J 𝐺(ℎ,𝑚),∃𝑖∈A:𝑛 𝑖,𝑗 <(1−𝛼)𝑐 𝑤min𝑀(𝑚) −

≤𝐾𝑁exp

−𝛼2
2 𝑐𝑤min𝑀(𝑚) −

.
Choice of𝛼and𝑛 min.AssumeJ 𝐺(ℎ,𝑚)≠∅. Fix𝜉∈(0,1), and choose
𝛼:=
√︄
2 log(3𝐾𝑁/𝜉)
𝑐𝑤min𝑀(𝑚) − , 𝑛 min :=(1−𝛼)𝑐 𝑤min𝑀(𝑚) − ,
assuming𝛼<1. Then Lemma E.1 implies that the support event
Esupp :={∀𝑗∈J 𝐺(ℎ,𝑚),∀𝑖∈A,𝑛 𝑖,𝑗 ≥𝑛 min}
satisfies Pr(E supp)≥1−𝜉/3.
Lemma E.2 (Total static traffic concentration).Let𝑌 𝑗 :=1{𝑒 𝑗∈A}for𝑗=𝐽 ℎ,...,𝑁. Then
E[𝑌𝑗]=
𝐾∑︁
𝑖=1
𝜀𝑖,𝑗 ≤¯𝑐𝜖.
viii

Therefore,E|𝑆+ 𝑆|≤¯𝑐𝜖𝑁. By Assumption E2, for any𝜁∈(0,1),
Pr'›
«
|𝑆+ 𝑆|>¯𝑐𝜖𝑁+
√︄
𝑁
2 log
 1
𝜁

“ﬁ
‹
≤𝜁.
Theorem E.1 (Finite-sample dynamic regret bound).Under Assumptions (E1)–(E4), assume J𝐺(ℎ,𝑚)≠
∅and𝛼<1. For any𝜉∈(0,1), with probability at least 1−𝜉,
𝑅dyn 𝑞 (𝑇)≤𝑁 ℎ+¯𝑐𝜖𝑁+
√︄
𝑁
2 log
 3
𝜉

+2|𝑆𝐺 𝐿|
√︄
log(6𝐾𝑁/𝜉)
2𝑛min
+2𝑀(𝑚) + 𝑉𝑞(𝑇)+𝜂(𝐾−1)|𝑆 𝐺 𝐿|+ 2𝛿sm 𝑛min |𝑆𝐺 𝐿|+𝐹𝑞(𝑇;ℎ,𝑚).
Proof.The first 𝑁ℎ searches do not yet have a fullℎ-time lookback window; since per-search regret is at
most one, their contribution is at most𝑁ℎ. On any post-warm-up static round, regret is also at most one, so
the total static-round regret is at most|𝑆+ 𝑆|. Lemma E.2 with𝜁=𝜉/3 gives the event
Estat :=
 
 |𝑆+ 𝑆|≤¯𝑐𝜖𝑁+
√︄
𝑁
2 log
 3
𝜉
 
 ,
with probability at least 1−𝜉/3.
Now fix a greedy LAAL round𝑗∈𝑆 𝐺 𝐿 . Define regularized means 𝑔𝑖,𝑗 :=𝜇 𝑖,𝑗−𝜂𝑖 and b𝑔𝑖,𝑗 :=b𝜇𝑖,𝑗−𝜂𝑖 .
Greedy selection implies
𝜇𝑖★ 𝑗,𝑗−𝜇 𝑎𝑗,𝑗 ≤2 max 𝑖∈A |b𝜇𝑖,𝑗−𝜇 𝑖,𝑗|+𝜂(𝐾−1).
To bound the estimation error, define
b𝜇0 𝑖,𝑗 := 1 𝑛𝑖,𝑗 ∑︁ ℓ∈𝑊𝑗(ℎ) ˜𝑟ℓ1{𝑎ℓ =𝑖},¯𝜇 𝑖,𝑗 := 1 𝑛𝑖,𝑗 ∑︁ ℓ∈𝑊𝑗(ℎ) 𝜇𝑖,ℓ 1{𝑎ℓ =𝑖}.
Then
|b𝜇𝑖,𝑗−𝜇 𝑖,𝑗|≤|b𝜇0 𝑖,𝑗−¯𝜇𝑖,𝑗|+|¯𝜇 𝑖,𝑗−𝜇 𝑖,𝑗|+|b𝜇𝑖,𝑗−b𝜇0 𝑖,𝑗|.
OnE supp,𝑛𝑖,𝑗 ≥𝑛 min. By (E3) and Hoeffding–Azuma, choosing
𝛽:=
√︄
log(6𝐾𝑁/𝜉)
2𝑛min
and applying a union bound over𝑖∈A and 𝑗∈J 𝐺(ℎ,𝑚) gives a noise eventEnoise, with probability at least
1−𝜉/3, on which
max
𝑖,𝑗
|b𝜇0 𝑖,𝑗−¯𝜇𝑖,𝑗|≤𝛽.
Since ˜𝑟𝑗∈[0,1], the smoothing term is bounded by
|b𝜇𝑖,𝑗−b𝜇0 𝑖,𝑗|≤ 𝛿sm 𝑛𝑖,𝑗 ≤ 𝛿sm 𝑛min .
ix

For the drift term, let𝑣 𝑟 :=max 𝑖∈A|𝜇𝑖,𝑟−𝜇 𝑖,𝑟−1|and𝐵 𝑗 := ˝𝑗 𝑟=𝑏𝑗+1𝑣𝑟. Then|¯𝜇𝑖,𝑗−𝜇 𝑖,𝑗|≤𝐵 𝑗, and
∑︁
𝑗∈𝑆𝐺 𝐿
𝐵𝑗≤𝑀 (𝑚) + 𝑉𝑞(𝑇),
because each variation increment appears in at most𝑀 (𝑚) + greedy-eligible windows.
OnE supp∩E noise∩E stat, which has probability at least 1−𝜉, every greedy LAAL round satisfies
𝜇𝑖★ 𝑗,𝑗−𝜇 𝑎𝑗,𝑗 ≤2𝛽+2𝐵 𝑗+ 2𝛿sm 𝑛min +𝜂(𝐾−1).
Summing over𝑗∈𝑆 𝐺 𝐿 gives
∑︁
𝑗∈𝑆𝐺 𝐿
(𝜇𝑖★ 𝑗,𝑗−𝜇 𝑎𝑗,𝑗)≤2|𝑆 𝐺 𝐿|𝛽+2𝑀 (𝑚) + 𝑉𝑞(𝑇)+𝜂(𝐾−1)|𝑆 𝐺 𝐿|+ 2𝛿sm 𝑛min |𝑆𝐺 𝐿|.
Fallback rounds contribute at most |𝑆𝐹 𝐿|=𝐹 𝑞(𝑇;ℎ,𝑚) . Adding the warm-up, static, greedy-LAAL, and
fallback contributions proves the theorem.□
Assumption E5 (Regular query rate).For the tuning results, assume there exist constants 0<𝜅 −≤𝜅+<∞
such that
𝜅−
𝑁ℎ
𝑇 ≤𝑀 𝑗≤𝜅+
𝑁ℎ
𝑇 ,∀𝑗∈{𝐽 ℎ,...,𝑁}, 𝑁 ℎ≤𝜅+
𝑁ℎ
𝑇 .
This formalizes the statement that anℎ-time window contains on the order of𝑁ℎ/𝑇searches of query𝑞.
Corollary E.1 (Fixed exploration mass).Under Assumption E5, ignoring logarithmic factors and lower-
order warm-up, smoothing, regularization, and fallback terms, and taking 𝑚=0 , Theorem E.1 gives the
dominant scaling
𝑅dyn 𝑞 (𝑇)≲¯𝑐𝜖𝑁+
√︄
𝑁𝑇
𝑐𝑤minℎ+ 𝑁ℎ 𝑇 𝑉𝑞(𝑇).
For fixed𝜖, choosing
ℎ★≍
 𝑇 3
𝑐𝑤min𝑁𝑉𝑞(𝑇) 2
1/3
yields
𝑅dyn 𝑞 (𝑇)=𝑂(¯𝑐𝜖𝑁)+ ˜𝑂  (𝑐𝑤min)−1/3𝑁2/3𝑉𝑞(𝑇) 1/3  .
If𝑁=Θ(𝑇), this becomes
𝑅dyn 𝑞 (𝑇)=𝑂(¯𝑐𝜖𝑇)+ ˜𝑂  (𝑐𝑤min)−1/3𝑉𝑞(𝑇) 1/3𝑇 2/3  .
Corollary E.2 (Joint tuning under equal static shares).Under the same simplifications as Corollary E.1,
suppose the 𝐾 static cohorts receive equal design mass, 𝑤𝑖 =𝜖/𝐾 for𝑖=1,...,𝐾 . The dominant terms
x

become
𝑅dyn 𝑞 (𝑇)≲¯𝑐𝜖𝑁+
√︄
𝐾𝑁𝑇
𝑐𝜖ℎ + 𝑁ℎ 𝑇 𝑉𝑞(𝑇).
For fixed𝜖, the optimal window length is
ℎ★(𝜖)≍
 𝐾𝑇 3
𝑐𝜖𝑁𝑉 𝑞(𝑇) 2
1/3
.
Substituting this back and optimizing over𝜖gives
𝜖★≍¯𝑐−3/4𝑐−1/4
𝐾𝑉𝑞(𝑇)
𝑁
1/4
,
and therefore
𝑅dyn 𝑞 (𝑇)= ˜𝑂  ¯𝑐1/4𝑐−1/4𝑁3/4𝐾𝑉𝑞(𝑇)1/4 .
If𝑁=Θ(𝑇), this becomes
𝑅dyn 𝑞 (𝑇)= ˜𝑂  ¯𝑐1/4𝑐−1/4𝑇 3/4𝐾𝑉𝑞(𝑇)1/4 ,
which is the bound stated in Theorem 1 after writing𝑉(𝑇)≡𝑉 𝑞(𝑇).
G Low Volume Queries
Default ad load for sparse queries (𝑖def):LAAL applies greedy selection only when a query has at least𝑚
recent observations in the sliding window; otherwise it falls back to a fixed default𝑖def. We choose𝑖def using
historical data from the static cohorts{𝐶,𝑇 2,...,𝑇 6}during the last month of the first experiment.
LetS𝐻 denote the historical sample of searches from the static cohorts (so each𝑠∈S 𝐻 has a fixed realized
ad load𝑎𝑠∈{1,...,6} determined by its cohort). Using the same window length ℎ as in deployment, define
the trailing-window volume for search𝑠 as the number of searches for the same query in the precedingℎ days:
𝑁𝑠 ≡
∑︁
𝑠′∈S𝐻
1{𝑞𝑠′ =𝑞 𝑠}1{𝑡 𝑠−ℎ≤𝑡 𝑠′ <𝑡 𝑠}.
Let𝜖 denote the aggregate traffic share assigned to these static cohorts. We label a search aslow-volumeif its
full-traffic-equivalent trailing-window volume is at most the greedy threshold𝑚:
SLow ≡ {𝑠∈S 𝐻 :𝑁 𝑠/𝜖≤𝑚}.
We then choose𝑖def as the best-performinguniformad-load policy on this low-volume subset, under the
deployed reward𝑟(𝑦𝑠,𝜆)=𝜆Revenue 𝑠+Conversion𝑠. Specifically, for each𝑖∈{1,...,6} define the mean
reward among low-volume searches that were served with ad load𝑖:
b𝑟Low(𝑖) ≡E[𝑟(𝑦𝑠,𝜆)|𝑠∈S Low, 𝑎𝑠 =𝑖] ≈
˝
𝑠∈S Low 1{𝑎𝑠 =𝑖}𝑟(𝑦 𝑠,𝜆)˝
𝑠∈S Low 1{𝑎𝑠 =𝑖} .
xi

Finally, we set
𝑖def∈arg max 𝑖∈{1,...,6} b𝑟Low(𝑖).
In our historical data, this maximizer is𝑖def =4 . Intuitively,𝑖def is the best uniform static policy when the
query is sparse in the recent window (i.e., when LAAL cannot reliably estimate per-query arm values).
Table A7: Low-Volume Queries: Outcomes by Conditions
𝐶 𝑇 2 𝑇3 𝑇4 𝑇5 𝑇6
Search Count 1,787,515 354,797 335,833 338,457 334,132 336,299
Conversion/Search 0.479 0.470 0.489 0.485 0.475 0.466
Revenue/Search 4.03 4.37 4.75 5.15 5.52 5.99
Reward/Search 0.519 0.514 0.536 0.537 0.531 0.526
H Reweighting Brand-On and Brand-Off Recommendation Histograms
For each non-stationary query𝑞, let𝑑𝑞 on,𝑖 and𝑑𝑞 off,𝑖 denote the number of LAAL searches in which ad load𝑖
was recommended duringBrand-OnandBrand-Offstates, respectively. Let 𝐷𝑞 on= ˝ 𝑖𝑑𝑞 on,𝑖,𝐷𝑞 off = ˝ 𝑖𝑑𝑞 off,𝑖 ,
and 𝑝𝑞 on =𝐷 𝑞 on/(𝐷𝑞 on+𝐷 𝑞 off). To compare Brand-On and Brand-Off recommendation distributions while
accounting for different Brand-On shares across queries, we reweight counts within query as ˜𝑑𝑞 on,𝑖 =𝑑 𝑞 on,𝑖/𝑝𝑞 on
and ˜𝑑𝑞 off,𝑖 =𝑑 𝑞 off,𝑖/(1−𝑝 𝑞 on). We then aggregate ˜𝑑on,𝑖 = ˝ 𝑞∈Q NS ˜𝑑𝑞 on,𝑖 and ˜𝑑off,𝑖 = ˝ 𝑞∈Q NS ˜𝑑𝑞 off,𝑖 , and normalize
each vector to sum to one.
xii

References
xiii
