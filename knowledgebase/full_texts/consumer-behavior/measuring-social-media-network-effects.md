---
title: Measuring Social Media Network Effects
url: https://arxiv.org/abs/2507.04545
category: consumer-behavior
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Sinan Aral
- Seth G Benzell
- Avinash Collis
- Christos Nicolaides
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.04545
pages: 201
chars: 374304
fetched_at: '2026-11-08T13:13:39+00:00'
kb_version: 1
---

# Measuring Social Media Network Effects

Measuring Social Media Network Effects
Sinan Aral,1∗ Seth G. Benzell,2 Avinash Collis,3 Christos Nicolaides4
1Massachusetts Institute of Technology, 2Chapman University,
3Carnegie Mellon University, 4University of Cyprus
∗To whom correspondence should be addressed; E-mail: sinan@mit.edu.
Authors listed in alphabetical order.
June 1, 2026
Network effects, which dictate that the utility from consuming a good increases with
the total number of other consumers consuming it, are widely regarded as critical to the
digital economy. But recent theory and evidence suggest thatlocalnetwork effects—the
economic value created by specific social network connections—are what drive value in
networked online platforms. Here, we use representative, incentive-compatible online
choice experiments involving 19,923 Facebook, Instagram, LinkedIn, and X users in the
United States to provide the first large-scale, empirical measurement of local network ef-
fects in the digital economy and to measure heterogeneity in the value of network connec-
tions across social media platforms. Our analysis reveals that social media platform value
ranges from $78 to $101 per consumer, per month, on average, and that 8.1-23.7% of that
value is explained by local network effects. We also find that 1) stronger ties are more
valuable on Facebook and Instagram, while weaker ties are more valuable on LinkedIn
and X; 2) connections known through work are most valuable on LinkedIn and least valu-
able on Facebook, and people who are looking for work value LinkedIn significantly more
1
arXiv:2507.04545v2  [econ.GN]  29 May 2026

and Facebook significantly less than people who are not looking for work; 3) men value
connections to women on social media significantly more than they value connections to
other men, particularly on Instagram, Facebook and X, while women value connections
to men and women equally across platforms; 4) consumers value network connections on
any platform more if they are also connected with them on other platforms, suggesting
that social media platforms are complements, not substitutes; 5) white consumers value
relationships with other white consumers significantly more than they value relationships
with non-white consumers on Facebook while, on Instagram, connections to alters eigh-
teen years old or younger are valued significantly more than any other age group—two
patterns not seen on any other platforms. The social media platforms we studied each
individually generate between $53B and $215B in consumer surplus per year in the US
alone. These results suggest that social media generates significant value, that local net-
work effects drive a substantial fraction of that value and that the sources and contours of
these effects vary across platforms, consumers, and connections.
Numerous economic models explain how network effects operate (1–4) and affect market
competition (5–7), product design (4), platform strategy (8), systems compatibility (9, 10), an-
titrust regulation (11), market failure (12), prices (13), and lock-in to potentially adverse or
sub-optimal technologies (14). Some empirical work measures economic network effects in the
aggregate, estimating the effect of the total size of a product or platform’s user base on eco-
nomic value creation, using observational data (15, 16), field experiments (17, 18), and natural
experiments (19). But, for decades, most scientific literature only considered network effects in
the aggregate, modeling and measuring the effect of thetotalnumber of consumers of a prod-
uct or platform on that product or platform’s economic value and treating each consumer, and
therefore each connection between consumers in the network, interchangeably.
Recently, however, as the economy became more networked, the concept of economic net-
2

work effects expanded to consider how social networks affect economic value. Tucker (2008)
is an early example of an empirical paper which allowed a network effect to depend on the
identity of technology adopters (20). A new theory of “local network effects,” which evolved
from consideration of networks of geographically proximate consumers (21–23), now considers
how social network connections and structures create network effects through socially proxi-
mate consumers (24). Rather than asking how the total number of consumers of a product
affects a product’s value, these new local network effects theories posit that a product’s value
is created, at least in part, through subsets of consumers connected by the product in social
networks. These new theories also seek to explain how different types of network connections
and structures determine a product’s value.
Sociological studies of the value of network connections have examined self reports of con-
nection value (25–28), measured the strength of ties (17,29–33), examined the social capital and
social support implications of network ties (34–39), measured the importance of digital network
connections (40–49) and valued ties based on strategic outcomes related to information advan-
tage and power (50–54). But sociologists have not examined economic valuations of network
ties or measured tie value in the context of economic network effects. On the other hand, eco-
nomic studies have estimated total platform valuations in the context of network effects in the
aggregate (15, 16, 18–20, 55–57), investigated the role of heterogeneity in network formation
(58, 59), and studied the implications of specific types of network ties for economic outcomes
such as income mobility (60, 61). But economists have not measured consumers’ economic
valuations of network connections or measured tie value in the context of economic network
effects. As a result, a large and important gap exists, between the sociology of networks and the
economics of network effects, in our understanding of local network effects.1
In today’s digital economy, which is increasingly characterized by products consumed by
1See SI subsection 2.1 for a more complete discussion.
3

networks of consumers together, this lack of understanding of local network effects is critical
for several reasons. First, local network effects are essential to understanding the welfare im-
plications of social media platforms and their regulation. As social media platforms expand
internationally and as governments attempt to regulate them across geographies, precise mea-
surement of the value created by social network connections is essential to guiding policies that
maximize welfare. Effective antitrust regulation, merger oversight, national bans on foreign
social media platforms, and interoperability and network portability legislation all depend on
understanding the value created by social network connections and how that value is shaped by
the nature of the connections and the social network structures in which they are embedded. For
example, when governments seek to break up networked monopolies, unwind anti-competitive
acquisitions, or ban foreign social media, understanding the welfare implications of breaking
the networked ties enabled by these platforms is a first-order consideration. Similarly, the wel-
fare implications of legislation that forces networked platforms to be interoperable or that allows
consumers to take their networks with them when they leave one platform for another, can only
be understood in the context of precise measurement of the network value created by enabling
such interoperability or network portability.
Our study addresses this challenge by being the first to obtain valuations, at the connection
and platform level, for multiple major social media platforms simultaneously using a common
methodology. This enables direct cross-platform comparisons that reveal how platforms differ
in the nature of the value they create. Our results show, for example, that job seekers value
LinkedIn significantly more and Facebook significantly less than non-job-seekers, providing
direct evidence that these platforms serve distinct economic functions. The finding that con-
nections to people consumers see frequently in person are valued far more than connections to
people they never meet offline raises important questions about whether social media primarily
complements or substitutes for offline social life. An additional policy-relevant finding is that
4

consumers value connections to the same person more when they are connected on multiple
platforms. This is a result with direct implications for competition policy and one that can only
be observed in a study that measures valuations across platforms simultaneously.
Second, local network effects are critical to platform strategy. How network connections
create economic value directly implicates the most important strategic decisions faced by net-
worked platforms. The first ever model of network effects theorized that how different network
connections create value, for example if consumers have “communities of interest” or “a few
principal contacts,” dramatically changes platforms’ optimal go-to-market strategies and pric-
ing (1). If consumers are socially clustered, as we know they are in human social networks (62),
recruiting communities of connected consumers will create greater consumer welfare and total
platform value than recruiting disjoint sets of unconnected consumers. Local network effects
also implicate platform monetization, user acquisition, and algorithmic connection recommen-
dation strategies for the same reason (17). As different connections and network structures may
create dramatically different value for consumers and platforms, how platforms recruit users,
recommend connections, monetize their services, and how these decisions affect welfare all
depend on the contours of the value created by local network effects.
Finally, local network effects determine, in part, why some platforms succeed while others
fail. Analysis of the early platform battle between Facebook and MySpace suggests that Face-
book’s go-to-market strategy, which focused on cultivating connections among college friends,
created stronger local network effects than MySpace’s recruitment strategy, which yielded neg-
ative assortativity, loose connections and, thus, weak local network effects (63). The evidence
suggests that Facebook overcame MySpace’s significant installed base advantage by creating
stronger local network effects (64).
Despite the importance of local network effects for regulation, competition, platform strat-
egy, and the measurement of economic welfare, we currently lack methods for measuring local
5

network effects in the digital economy. To address this challenge we adapt the framework
of massive, incentive compatible online choice experiments to measure local network effects
among 19,923 representative users of Facebook, Instagram, LinkedIn and X across the United
States. The incentive compatible choice experiment framework is well understood and has pre-
viously been used to measure total welfare gains from the consumption of a variety of digital
goods and services (55–57). Choice experiments illicit truthful and accurate valuations of prod-
ucts by offering consumers a series of choices in exchange for monetary compensation equal to
their willingness to accept deactivation of a product if and only if they cease using the product
for specified periods. The experiments are made consequential by informing participants that
some fraction of the study pool will be randomly selected to receive payments based on their
valuations after the survey concludes. In incentive compatible online choice experiments, com-
pliance with deactivation is monitored by requiring subjects to provide access to their online
accounts so researchers can verify that they deactivated the products before payments are made.
While previous incentive compatible choice experiments have measured the total value of
social media platforms by offering consumers payments equal to their expressed platform valu-
ations upon platform deactivation, we offer consumers payments for deactivating the platforms
and, separately, solicit incentive compatible estimates of specific connections. By randomly
varying payment offers and the types of connections selected for valuation, our approach allows
us to precisely measure total platform value, platform value arising from local network effects
and the heterogeneity of local network effects across consumers, connections and platforms.
We conducted two waves of surveys containing incentive compatible online choice experi-
ments including Becker-DeGroot-Marschak (BDM) lotteries (65), multiple-price lists (66), and
a ranked choice method (67) adapted to measure the value of networked connections and lo-
cal network effects, which we call Connection Rank Choice (CRC), across four social media
platforms over three years. The first wave, conducted between February 2021 and May 2022,
6

recruited 10,528 respondents representative of the U.S. internet population from Lucid—a high
quality online survey platform (68) widely used in academic research (69–71). The second
wave, conducted between November and December 2023, recruited 9,395 respondents rep-
resentative of the U.S. internet population, again from Lucid. Every survey respondent was
verified by Lucid to be a monthly active user of the platforms for which we were conducting
incentive-compatible choice experiments.
During the first wave, after respondents were recruited, they were immediately asked to
connect with our research accounts on the four platforms. When connecting to those accounts,
respondents were informed that they would provide account information to the research team
including their connection counts, connection lists and demographic profile information. This
gave us access to rich data about respondents’ profiles and social networks, which we describe
below. After connecting with our research accounts, respondents were asked a series of survey
questions about their age, gender, ethnicity, household income, political leaning and time spent
using each of the platforms. Following the survey, respondents were asked to list their top four
closest connections and “any four connections excluding the four closest connections”, which
created a list of eight connections for every respondent totaling 84,224 network connections.
Then, following Brynjolffson et al (55) and Allcott et al (56), we provided respondents a Becker-
DeGroot-Marschak (BDM) lottery to illicit their total platform valuation for each platform—
asking them to provide a valuation they were willing to accept to deactivate the platform for
a month. After the platform valuation question, we asked respondents to rank how valuable
they find their eight connections using Connection Rank Choice (CRC), a rank order question
adapted to measure the value of networked connections and local network effects.
Once the connections, the BDM platform valuations and connection rankings were pro-
vided, the research team manually verified all of the responses by navigating to the respondents’
accounts and checking each response against each platform’s data to ensure survey accuracy.
7

For each connection named in the survey to whom the respondent is connected on the platform,
we checked whether that connection appears in the list of the respondent’s connections on the
platform. We also collected information about the respondents, their eight ranked connections
and their relationship to each connection. On Facebook, for example, we collected respondents’
connection lists and matched the names with U.S. Census data from the U.S. Social Security
Administration to estimate the race and gender of each of the respondents’ connections. 2 For
LinkedIn, we collected respondents’ profile information, including their educational attainment
and career history. For X, we collected respondents’ post history and lists of followers and fol-
lowees using the X API. Instagram was the only platform from which we were unable to gather
additional information due to restrictions imposed by the platform.
During the second wave survey, in addition to the demographic and platform usage ques-
tions listed above, we also asked respondents if they were currently looking for work and vali-
dated our total platform valuation measurement using a multiple price list valuation elicitation
instrument equivalent to a series of single binary discrete choice experiments across a range
of valuations (55, 66). This method is also well understood and has been validated across a
number of different product and platform valuation studies (55). We randomly varied the upper
limit of the price range to be $100, $150, or $200 to account for anchoring effects. One out of
every hundred respondents were randomly selected and offered to follow up on their choices
with incentive compatible payments (see SI more details about incentive-compatibility in both
waves). The research protocol in each Wave was separately evaluated and approved by the
Massachusetts Institute of Technology’s (MIT’s) Institutional Review Board and the analysis in
Wave two was preregistered with the Open Science Foundation (OSF).3
To evaluate the results of these surveys, we developed a model of local network effects
based on a latent topics/redundant signal framework. The model allows for rich patterns of
2https://www.ssa.gov/oact/babynames/limits.html
3https://osf.io/qs4kn/?view only=5cee408999b5484dafcc9626e88c953b
8

complementarity and substitution across types of connections and information transmitted. The
model is described in detail in SI section 3.2.3. It motivates our two main sets of analyses:
First, an analysis of the total value created by the platform and the share of the value created by
local network effects; Second, an analysis of the relative value of different types of connection,
which are interpreted as the product of the value of the information transmitted and likelihood
the connection yields that information.
Figure 1 presents estimates of total platform value, the share of platform value explained
by direct connections, and how platform value varies with time spent on the platforms, polit-
ical leaning, relationship status and job seeking behavior. 4 Results of our choice experiment
measurements show that social media platform value ranges from $78 to $101 per consumer,
per month, on average with Facebook having the highest estimated platform value of $101 per
month, Instagram $91 per month, LinkedIn $87 per month and X $78 per month (Fig. 1A). Us-
ing equation [1], we estimate that between 8.1-23.7% of total platform value is created by local
network effects or the value consumers receive from their network connections (Fig. 1B). Face-
book displayed the strongest local network effects as it had the highest share of platform value
associated with direct connections. X displayed the weakest local network effects as it had the
lowest share of platform value associated with direct connections. TheR 2 of the regressions in-
forming these estimates are low, consistent with strong individual heterogeneity in the share of
platform value derived from local network effects. However, all local network effect estimates
were significantly different from zero, indicating that a substantial fraction of platform value is
derived from direct connections above and beyond aggregate network effects derived from the
total installed base of the platforms for the average user.
There is a positive relationship between time spent on the platforms and platform valuations
(Fig. 1C), but no clear relationship between a platform’s valuation and consumers’ political
4For full statistical reporting of estimated differences between conditional averages and associated p-values for
Figures 1 through 4, see SI section 6.
9

Figure 1: Total Platform Value and Local Network Effects.This figure summarizes results on
total monthly platform valuations from study 2. Panel A plots the empirical CDF of monthly valuations
of retaining access to the platform for one month in contemporaneous US Dollars. Panel B plots the
average of these values by platform, as well as the estimated share of that value created by local network
effects. Panels C reports average valuations and 95% confidence intervals conditional on platform and
time spent on that platform. Panel D reports average valuations and 95% confidence intervals conditional
on platform and political ideology. Panel E reports average valuations and 95% confidence intervals
conditional on platform and relationship status. Panel F reports differences between job seekers and
non-job seekers of average valuations and 95% confidence intervals conditional on platform.
10

ideology (Fig. 1D). Married and partnered individuals have significantly higher valuations for
Facebook and LinkedIn than individuals who are currently in or are looking for serious rela-
tionships (Fig. 1E), perhaps because married or partnered individuals are more focused on their
careers and socializing with their families online. Along similar lines, people who are actively
looking for work value LinkedIn significantly more, and Facebook significantly less, than peo-
ple who are not looking for work (Fig. 1F).
Figure 2: Tie Strength and Connection Value.This figure summarizes results on the relative value
of social media connections from study 1. Outcome is Connection Value Percentile (CVP) as defined
in equation [2], with higher values indicating a stronger preference. Panel A reports average CVP and
95% confidence interval conditional on platform and how the ego (survey taker) reports knowing the
alter. Panel B reports average CVP and 95% confidence interval conditional on platform and how often
the ego reports seeing the alter. Panel C reports average CVP and 95% confidence interval conditional
on platform and whether the ego and alter are connected on at least one other platform. Panel D reports
average CVP and 95% confidence interval by platform of the ego-alter pair being connected on one of
three other studied platforms.
11

We refer to the value of a single connection, as distinct from the total value of local network
effects, as connection value. Consumers value closer, stronger ties more than weaker, arms
length ties across all platforms (Fig 2.). Specifically, digital connections to family members and
family friends are more valuable than contacts known only online (Fig. 2A). Value from net-
work connections is increasing in interaction intensity, with a sharp increase in value from dig-
ital connections to people we live with and a sharp drop in value for people who we never meet
in person, especially for connections made through Facebook (Fig. 2B). For every platform,
connections made on more than one platform are valued significantly more than connections
made on only a single platform (Fig. 2C). This strongly suggests that connections to the same
people across platforms are either imperfect substitutes or even complements, perhaps due to a
desire for redundancy (if one platform were to be interrupted) or because different information
is more usefully transmitted on different channels. There is heterogeneity in the extent to which
connection on an alternate platform reduces CVP on the focal platform, suggesting varying de-
grees of complementarity across pairs of platforms (Fig. 2D). 5 Being connected with someone
on Facebook, Instagram or LinkedIn is associated with higher valuations for that same person
on every other platform. However, being connected with someone on X is associated with
higher valuations for that person on LinkedIn, but not on Instagram and Facebook, suggesting
lower relative complementarity.
Men value connections to women on social media significantly more than they value con-
nections to other men, particularly on Instagram, Facebook and X, while women value connec-
tions to men and women equally across all platforms (Fig. 3A). The relationship valuations
we estimated also reveal preferences for race homophily, as same race relationships are valued
more highly than mixed race relationships, on average, across social media (Fig. 3B). Interest-
5Of course, purely correlational evidence is not conclusive. The ideal test of this hypothesis would use ex-
ogenous changes to network connections to identify their elasticity of substitution. For a complete discussion of
measurement of complementarity and substitution, see SI section S.2.6
12

ingly, the higher average valuations for race homophily are driven by a single platform. White
consumers value relationships with other white consumers significantly more than they value
relationships with non-white consumers on Facebook, while same race relationships are not val-
ued significantly more than mixed race relationships on any other platform. The data also reveal
value disassortativity by age on one platform—Instagram. Valuations for connections younger
than oneself are significantly higher on Instagram than valuations for connections that are older
or of the same age (Fig. 3C). Furthermore, on Instagram, connections to alters eighteen years
old or younger are valued significantly more than any other age group, which are patterns not
seen on any other platform (Fig. 3D).
These individual characteristic gradients are jointly confirmed in a rank-ordered, exploded,
logit estimated on the pooled Wave 1 rankings. Nearly every positive correlate of CVP retains
an independent, statistically significant coefficient when entered together in a pooled regres-
sion. This suggests that contact frequency, relational source, cross-platform connection, and
demographic homophily each capture distinct sources of value. In a pooled regression, contact
frequency is the most important predictor, then relationship-type and cross-platform connection
status, with relative and absolute demographics being the least important. By anchoring the es-
timated marginal utilities from connection characteristics to average connection value, we also
estimate monthly monetary valuations for different characteristics. The largest value is for ‘I
live with this person’ which raises connection value by 4.6 cents a month on Facebook. From
a policy perspective, the most important takeaway is that being connected on another platform
remains a positive predictor of connection value after controlling for other dyadic characteris-
tics, further supporting the theory that connections on different platforms are complementary.
See SI section 3.1.2 for full results and details.
Analysis of the value of platform features is also instructive (Fig. 4). First, posting content
on one’s Facebook feed, posting new photos and reels to Instagram and posting profile up-
13

Figure 3: Relational Demographics and Connection Value.This figure summarizes results on the
relative value of social media connections from study 1. Outcome is Connection Value Percentile (CVP)
as defined in the text, with higher values indicating a stronger preference. Panel A reports CVP and
95% CIs conditional on platform and ego (survey taker) and alter gender (an ‘other’ category, with wide
confidence intervals, is omitted). Panel B reports CVP and 95% CIs conditional on platform, and ego
and alter race. Panel C reports CVP and 95% CIs conditional on platform, and ego and alter’s relative
age, where same age indicates being in the same age bin. Panel D reports CVP and 95% CIs conditional
on platform and alter’s age bin, and includes an insert where age-bins are split alternatively: under age
18 and otherwise.
dates, like new educational credentials or achievements, job transitions or work promotions to
LinkedIn, all add significantly to higher platform valuations (Fig. 4A). These results are in line
with the higher valuations for followers than for followees on Instagram and X reported earlier.
The ability to express ourselves to our networks and to update the world about ourselves and
our thoughts provides significant value to consumers. This is in line with research like Filippas
et. al. (72) who argue that we desire attention online and that follower-followee relationships
in part reflect the bartering of attention. Second, group interactions add significant value be-
14

Figure 4: Relational Demographics and Connection Value.This figure summarizes results on how
TPV varies with platform feature use from study 2. Panel A reports, for each platform, the increase in
TPV associated with feature use. Coefficients and 95% confidence intervals are derived from a regression
of total platform value on egos’ usage of each platform feature. Panel B reports how platform value varies
with feature use and ego income. Plotted are conditional average platform values for users and non-users
of the feature, for egos of different income groups. The split for high vs. low income is at one hundred
thousand dollars. SI Table S11 reports the point estimate and p-values for two differences: The difference
between conditional average total platform value for high and low income egos who use the feature, and
the difference in differences between conditional average total platform value for high income feature
users and non-users less the difference between low-income feature users and non-users.
yond dyadic network connections. For example, the use of LinkedIn Groups and X Spaces both
significantly increase consumers’ valuations of LinkedIn and X on average (Fig. 4A). Results
on the value of group interactions lend support to recent work documenting the importance of
higher order group relationships, characterized by simplicial complexes in networks, expanding
our theoretical conceptualization of networked value beyond dyadic interactions (73,74). Third,
the use of messaging features that enable direct, often synchronous, real-time communication
with others increase consumers’ valuations. For example, use of Facebook Messenger, on aver-
15

age, increases a consumer’s valuation of Facebook by approximately $12 per month (Fig. 4A).
Results on direct communications features, which add value beyond our estimates of the value
of networked connections, suggest that our estimates of the importance of local network effects
may be conservative as these features capture the value of not just having network connections,
but being able to communicate with them directly in real-time. Fourth, features that allow users
to organize and curate content add significantly to platform valuations. For example, the ability
to bookmark X posts adds approximately $5 per month, on average, to consumers’ valuations
of X. These results are in line with prior evidence of the value of content curation and organiza-
tion features demonstrating, for example, that the ability to curate playlists on music streaming
services increases consumers’ willingness to pay for those services (75).
Perhaps even more instructive, however, is how different consumers value the same features
differently. Figure 4B reports conditional average platform values for four features — Face-
book Messenger, Instagram Reels, LinkedIn Groups, and X Lists — stratified by income, with
the high/low cutoff drawn at $100,000 annually. Two patterns emerge. First, low-income users
who adopt these features value them significantly more than high-income users who adopt them.
Second, the gap between feature users and non-users is significantly larger for low-income than
for high-income consumers (SI Table S11). Together, these results indicate that social me-
dia networks deliver value to lower-income consumers in fundamentally different ways than
to higher-income consumers, and that this divergence is concentrated precisely in features de-
signed to extend reach beyond one’s existing network.
When the purposes of these features are considered, we believe the results support the use of
social media networks by lower income consumers to achieve social mobility, echoing research
demonstrating that social media network connections to higher socio-economic status (SES)
peers is “among the strongest predictors of upward income mobility identified to date” (60, 61).
For example, LinkedIn’s official description of the Groups feature notes that it is intended to
16

enable consumers to “build relationships... that can enhance your skills and knowledge... seek
feedback... [and to] learn from others’ experiences through group discussions.” Similarly, a key
element of Facebook Messenger is that it allows consumers to speak to people they are not con-
nected to on Facebook, which potentially enables them to break through to new social networks
with higher SES, value and resources that don’t exist in their own social networks. X Lists en-
able consumers to “manage and guide conversations... monitor competitors... highlight local or
small businesses... [and] track leads passing through their sales funnels.” These three features
are designed to enable consumers to reach beyond their own social networks, to enhance skills
and knowledge through interactions with those not yet in their own social networks and to seek
feedback, collaboration and professional development opportunities in networks not accessible
through direct connections. Such use cases are the precise enablers of social mobility described
by Chetty et al (60, 61) in their large-scale analysis of Facebook.
Access to the creator economy may be another driver of value for low income consumers.
Instagram describes Reels as enabling consumers to “create multi-clip videos... select from a
variety of effects created by Instagram and creators around the world... share your reels with
your followers on Feed, or make them available to the wider Instagram community... [and]
recommend your Reel on Facebook.” Thus, Reels not only enables participation in the creator
economy, but also content sharing beyond one’s direct network. As the creator economy attracts
aspiring, amateur creators seeking to participate in influencer marketing, platform payouts and
the monetization of short-form video, it is perhaps not surprising that lower income consumers
value Instagram Reels more than higher income consumers.
Combining our total platform valuation estimates with up-to-date counts of monthly active
users (MAUs) reported by each platform, we can estimate the total consumer surplus generated
by each platform in the US, monthly and annually. Using similar methods, Allcott et. al. (56)
estimated Facebook generates $31 Billion of consumer surplus per month and $372 Billion
17

annually. We estimate that Facebook generates $17.9 Billion per month and $214.9 Billion
annually, Instagram generates $12.6 Billion per month and $151.7 Billion annually, LinkedIn
generates $8.7 Billion per month and $104.9 Billion annually, and X generates $4.4 Billion per
month and $52.6 Billion annually. Given that 97% of total welfare gains from technological
innovations are captured by consumers, these estimates seem reasonable (76). The similarity
and consistency of our estimates compared to Allcott et. al. (56) also give us confidence in our
shared approach to estimating the total consumer welfare gains generated by these four social
media platforms in the United States. It is not surprising that our estimates are slightly lower
than Allcott et al. (56) given they only focus on highly active Facebook users (consumers who
use Facebook more than 15 minutes per day).
Although our work is the first to quantify the value and structure of local network effects
in the digital economy and to describe a systematic and rigorous method for doing so, it is not
without its limitations. First, in our setting, we do not have access to exogenous variation in
the number or types of respondents’ social network connections. As such, causal estimates of
the marginal value of adding or losing specific types of connections are elusive and omitted
variables could bias our estimates of connection value. We took several steps to estimate and
counteract our vulnerability to the lack of experimental variation in connections in our analysis.
Our pre-registered ordinary least squares (OLS) and LASSO specifications, which include nu-
merous controls and interactions, go a long was toward controlling for omitted variables. These
results show that, while controlling for many other factors, the number of connections (or alter-
natively, followers and followees) are highly significant predictors of platform valuations. Our
pre-registered analyses demonstrate that between 14%-25% of the variation in platform value
is explained by our predictors lending support to our post hoc control of omitted variables. Fur-
thermore, interactions between connection counts and platform engagement are also predictive
of platform value, suggesting that, as respondents engage more with the platforms, increases
18

in their platform valuations increase with their connection counts. Taken together, these results
suggest that local network effects are a consistent, significant and economically meaningful
driver of platform value and consumer surplus.
We encourage future work to measure local network effects using exogenous variation in the
number and types of respondents’ connections to causally identify the contributions of direct
connections to platform value. We know such analyses are possible given prior large scale
experiments that randomly varied the number and types of connections on social platforms
to measure, for example, the strength of weak ties (17). Experiments varying the connection
network could also provide insight into the value of alters’ connections to an ego’s valuation of
the connection. Understanding the value of these second and higher-order connections to user
value is another promising direction for future work.
Second, all incentive compatible choice experiments are potentially vulnerable to anchoring
effects in the solicitation of valuations. When presenting potential valuations to respondents, the
maximum values presented could anchor their perceptions of typical or acceptable valuations.
We directly addressed potential anchoring effects using a number of preregistered designs. First,
in Wave 1, we provided respondents a slider of valuations and an open-ended free response value
solicitation that exceeded the slider range. Second, we randomly assigned different maximum
offer values in Wave 2 to experimentally vary distinct anchors enabling a systematic examina-
tion of our vulnerability to anchoring effects. Controlling for random assignment to anchors
has a minimal impact on point estimates of connection valuations, which remain positive and
significant on all platforms, suggesting that our results are robust to anchoring effects.
Third, platform and connection value solicitation in our context is self reported and in-
herently subjective, making efforts to generalize findings such as ours more challenging. Our
approach to this problem goes to the core of our research design. We present a rigorous attempt
to quantify inherently subjective valuations by constructing an incentive compatible value so-
19

licitation mechanism that provides real monetary incentives for the revelation of truthful and
accurate valuations of platforms and connections. Yet, incentive compatibility itself has weak-
nesses applicable to this entire literature. Most importantly, it depends on participants having
a reasonable expectation of payments upon deactivation, which may be especially problematic
for people with higher true valuations. Prior incentive compatible valuations have approached
this problem in different ways. Allcott et. al. (56) allow for a free response in the BDM value
solicitation, but winsorize maximum replies at $170, as this is the maximum payment they allow
in their randomized BDM offer, though this cutoff is not made known to participants. Burztyn
et. al. (77) provide a multiple price list with a $200 maximum and fit a thin tailed curve through
their results, allowing for imputted values above $200, and conclude this does not change their
findings.
We analyze different winsorization cutoffs for maximum value and learn several things.
First, pooling all platforms, less than 1% of respondents have valuations greater than $1000.
This seems reasonable given some creators earn tens of millions of dollars a year from their
social media presences and could not earn this revenue without social media. Second, this in-
terpretation is supported by the fact that X and Instragram are the platforms most impacted by
winsorization, suggesting the long tail of high valuers is most important on those platforms
where creator economies are most prevalent, compared to Facebook and LinkedIn. These facts
suggest a need for some caution when interpreting the aggregate welfare implications of our
estimates if a substantial fraction of value is driven by a small number of high valuers who are
imprecisely measured. However, the fact that less than 1% of our sample are high valuers makes
us more confident in our total platform valuations. Furthermore, winsorization and maximum
values do not effect our relative connection value estimates or platform or connection valuations
for typical platform users, giving us confidence in our results. In addition, our approach is at
or beyond the current state of the art, which has extensively solicited valuations with incentive
20

compatible designs even when such solicitations promise to enforce BDM contracts under cir-
cumstances known to experimenters ex-ante to be impossible (9). It has been shown, even in
these situations, that the promise of payments themselves incentivize participants to respond to
value solicitation questions truthfully and accurately. Furthermore, our extensive real platform
data collection mitigates vulnerabilities associated with self reporting of platform network and
use variables.
Fourth, network sampling and tie valuation are inherently challenging. Since we cannot
ask respondents to value all connections, we must sample their networks in a way that is both
representative and likely to choose connections respondents know well. Soliciting connection
value may also be unfamiliar for and inconsistent across respondents. We therefore sampled the
top four connections and any other four connections and asked respondents for relative rankings
rather than numeric valuations, which allows us to ensure consistency across comparisons while
estimating numeric valuations by combining total connection values with relative rankings to
understand how valuations vary by tie type and network structure. While prior connection value
research uses name generators, typically soliciting between three and fifteen connections, and
solicits tie closeness using self reported Likert scales, binary indicators of whether someone is
a “connection,” or observations of time spent together, no prior work applies incentive compat-
ibility to connection value solicitations.
Our solicitation of top and other connections ensures sampling from the entire connection
distribution and those whom respondents know well. But it may be that respondents are better
able to value close connections than other connections. To understand the reliability of our con-
nection value estimates, we reanalyzed our CVP results using only the four closest connections
given these are the connections over which consumers are likely to have the strongest and most
consistent preferences. If these results differed from results based on all eight connections, we
might be concerned that respondents are not able to value the four other connections as accu-
21

rately or consistently as top connections. Our analysis shows, however, that the relative rankings
are robust to the acquaintance generation process and return similar and consistent results (see
S4.1 in the SI).
Fifth, we may be concerned that an online sample is biased or not representative. However,
Lucid is a highly reliable online survey platform (68) widely used in academic research (69–
71) to solicit representative samples of US respondents, and the size of our study population,
which approaches 20K respondents, makes us less vulnerable to the idiosyncrasies of a small
online sample. By comparison, our sample is over six times larger than that of Allcott et. al.
(56), which offered the “the largest-scale experimental evidence available to date” when it was
published in 2020. Moreover, we required Lucid to verify that every survey respondent was
a monthly active user of the platforms for which we were conducting incentive compatible
choice experiments, performed multiple attention checks during the experiments filtering out
inattentive respondents, required respondents to connect with our research accounts to verify
their reporting of platform usage, verified each of their 84K network connections by examining
connection lists on their profiles, and collected substantial additional information, by survey and
by downloading observational data, to control for observable differences between respondents
and to ensure the reliability and representativeness of our analysis. We then used the additional
information we collected to analyze pre-registered robustness checks that showed the strong
and consistent contributions of connection value to total platform value holding observable
factors constant (see SI Tables S12-S21). We believe these measures support the robustness
and validity of our data collection from our large representative sample and mitigate against
inattentive responses and missing variables.
Finally, asking respondents to value platforms and connections on a monthly basis may
either over- or under-estimate the long term value of connections. For example, it could be that
giving up a social platform and your connections on it for a month imposes a low cost because
22

you know you will be back online and in touch in a month. If respondents had been asked to give
up platforms and connections for six months or a year, they might have assigned higher values,
making our one-month-based value solicitation undervalue platforms and connections. On the
other hand, short term connection value may be high if respondents want to communicate with
their connections immediately. When confronted with a more permanent, year long obstacle
to connection, they might seek alternative modes of communication, substituting away from
social media based connections entirely, lessening their value. We follow the literature and
solicit values based on deactivation for four weeks. However, we encourage future work in
this domain to examine different time horizons, like six months and a year, to understand how
valuations depend on elasticities of substitution.
Despite these limitations, our work presents the first large-scale, empirical measurement of
local network effects in the digital economy and the largest-scale experimental evidence on the
consumer surplus generated by social media to date. Our incentive compatible online choice
experiments revealed that between 8.1-23.7% of social media’s total value emanates from the
value consumers receive from their direct connections and that the social media platforms we
studied each generate between $53 billion and $215 billion a year in consumer surplus in the
United States alone. Our analysis also showed that stronger ties are more valuable on Facebook
and Instagram, while weaker ties are more valuable on LinkedIn and X, that men value connec-
tions to women on social media significantly more than they value connections to other men,
while women value connections to men and women equally across all platforms, that white
consumers value relationships with other white consumers significantly more than they value
relationships with non-white consumers on Facebook while, on Instagram, connections to alters
eighteen years old or younger are valued significantly more than any other age group (patterns
not seen on any other platform) and, as Chetty et al (60, 61) predicted, low income consumers
value social media features that enable them to reach across networks to higher socio-economic
23

status connections more than high income consumers. These results are essential to under-
standing the welfare implications of social media platforms and inform policymakers seeking
to regulate social media and managers setting platform monetization, user acquisition, and al-
gorithmic connection recommendation strategies. We hope the methods developed here provide
a foundation for future analyses of local network effects and the welfare effects of social media.
Materials and Methods
We analyzed three main measurements, derived from our choice experiments, to quantify net-
work effects in the social media economy: total platform valuation (TPV), the share of platform
value explained by connections (SPV) and connection value percentile (CVP). Total platform
valuation is the average total monthly value of a platform implied by our choice experiments
measured in U.S. dollars. The value of social media platforms derives, in part, from direct net-
work connections and, in part, from other platform features like news feeds, job search features,
marketplaces, groups, reels, lists and short form videos. The share of platform value explained
by connections (SPV) is the fraction of total platform value (TPV) derived from consumers’
direct connections. We estimate SPV by first evaluating the following regression:
T P Vp,i =δ p +λ p

1−e −zp Cp,i

+ε i,(1)
zp ≡ −log(1−π p),
This functional form is motivated by a redundant signal model where receiving the benefit
of connection on a platform requires successfully transmitting a message at least once, but
transmitting the message additional times is redundant. For example, the message may represent
an important social event or job opportunity. For a longer discussion, see section S3.2.3 in
the SI.π p is the probability that a single connection provides the signal,λ p is the value of
24

receiving the signal, andδ p is the value of platform participation in the absence of receiving the
signal.T P Vp,i is consumeri’s total monthly valuation for platformp, andC p,i is the number of
users consumeriis directly connected to on platformp. On Facebook and LinkedIn these are
friends and direct connections. On Twitter and Instagram, two separate terms forπandλ, the
probability of receiving the benefit of connection and the value of that signal being delivered,
for followers and followees were estimated. The results of these regressions are reported in the
SI (Table S22). If we defineT P Vp as the average ofT P Vfor all users (P i T P Vp,i/I, whereIis
the total number of respondents), then the share of platform value not explained by connections
is the platform’s intercept term ( δp T P Vp ) and the share of platform value explained by connections
SP Vp is1− δp T P Vp .
Finally, Connection Value Percentile (CV P) measures the relative value of a particular net-
work connection. Egos in our study named and described up to eight alters they are connected
to on the focal platform. On a subsequent survey page, we solicited the relative importance
of these contacts using a rank-order question (connection Ranked Choice (CRC)). 6 Using the
ranking provided, we calculatedCV Pfor each ego-alter pair as
CV Pi,j,p = 100(1− CR i,j,p −1 T CRi,p )(2)
whereCR i,j,p is the ranking given to connectionjby egoion platformpon our relative
ranking scale andCF R i,p is the total number of connections ranked by consumerion plat-
formp. We then estimated the relative value of different types of connections by analyzing
conditional averageCV P sfor egos and connections of different types.7
6The text of the relevant question is “Please rank the following connections from most valued on [PLATFORM]
(top) by you to least valued on [PLATFORM] (bottom) by you.” Note that we do not give detailed instructions to
survey takers about what is meant by “most valued.” Interpreting these results as informative about the nature of
connection complementarity across platforms requires interpreting importance as marginal value and the evidence
suggests such an interpretation was employed by participants (see Section S2.6 in the SI for more discussion).
7Our results are very similar when restricting attention to only top four connections, indicating the correlates
of CVP we find are not solely driven by small cardinal differences in value between e.g. 5th and 8th ranked
connections, but rather likely reflect substantive cardinal differences in value between these connections.
25

Acknowledgments
We thank D. Eckles, E. Brynjolfsson and participants of the MIT Conference on Digital Exper-
imentation, the Networks, Markets and the State conference at NYU Abu Dhabi, the Workshop
on Information Systems Economics, the MIT Social Analytics Lab and the IDE Research Sem-
inar for their helpful comments on earlier drafts of this manuscript. We also thank members
of the MIT Initiative on the Digital Economy for their intellectual support. The study was
approved by the MIT Institutional Review Board (IRB Protocols E-3229 and E-5633).
References
1. Jeffrey Rohlfs. A theory of interdependent demand for a communications service.The Bell
journal of economics and management science, pages 16–37, 1974.
2. Michael L Katz and Carl Shapiro. Network externalities, competition, and compatibility.
The American economic review, 75(3):424–440, 1985.
3. Jean-Charles Rochet and Jean Tirole. Platform competition in two-sided markets.Journal
of the european economic association, 1(4):990–1029, 2003.
4. Geoffrey G Parker and Marshall W Van Alstyne. Two-sided network effects: A theory of
information product design.Management science, 51(10):1494–1504, 2005.
5. Michael L Katz and Carl Shapiro. Systems competition and network effects.Journal of
economic perspectives, 8(2):93–115, 1994.
6. Carl Shapiro and Hal R Varian.Information rules: A strategic guide to the network econ-
omy. Harvard Business Press, 1999.
26

7. Geoffrey G Parker, Marshall W Van Alstyne, and Sangeet Paul Choudary.Platform revo-
lution: How networked markets are transforming the economy and how to make them work
for you. WW Norton & Company, 2016.
8. Paul Belleflamme and Martin Peitz.Platforms and network effects. Edward Elgar Publish-
ing, 2018.
9. Qi Wang, Yubo Chen, and Jinhong Xie. Survival in markets with network effects: Product
compatibility and order-of-entry effects.Journal of Marketing, 74(4):1–14, 2010.
10. Charles Zhechao Liu, Esther Gal-Or, Chris F Kemerer, and Michael D Smith. Compati-
bility and proprietary standards: The impact of conversion technologies in it markets with
network effects.Information Systems Research, 22(1):188–207, 2011.
11. Seth G Benzell and Avinash Collis. Multi-sided platform strategy, taxation, and reg-
ulation: A quantitative model and application to facebook.Benzell, Seth and Collis,
Avinash, Multisided Platform Strategy, Taxation and Regulation: Model and Application
to Facebook (February 22, 2022). Available at SSRN: https://ssrn.com/abstract=3619535
or http://dx.doi.org/10.2139/ssrn.3619535, 2022.
12. Stan J Liebowitz and Stephen E Margolis. Network externality: An uncommon tragedy.
Journal of economic perspectives, 8(2):133–150, 1994.
13. E Glen Weyl. A price theory of multi-sided platforms.American Economic Review,
100(4):1642–72, 2010.
14. Joseph Farrell and Paul Klemperer. Coordination and lock-in: Competition with switching
costs and network effects.Handbook of industrial organization, 3:1967–2072, 2007.
27

15. Erik Brynjolfsson and Chris F Kemerer. Network externalities in microcomputer software:
An econometric analysis of the spreadsheet market.Management science, 42(12):1627–
1647, 1996.
16. Yann Bramoull ´e, Habiba Djebbari, and Bernard Fortin. Identification of peer effects
through social networks.Journal of econometrics, 150(1):41–55, 2009.
17. Karthik Rajkumar, Guillaume Saint-Jacques, Iavor Bojinov, Erik Brynjolfsson, and Sinan
Aral. A causal test of the strength of weak ties.Science, 377(6612):1304–1310, 2022.
18. Kevin J Boudreau. Promoting platform takeoff and self-fulfilling expectations: Field ex-
perimental evidence.Management Science, 67(9):5953–5967, 2021.
19. Chiara Farronato, Jessica Fong, and Andrey Fradkin. Dog eat dog: Balancing network
effects and differentiation in a digital platform merger.Management Science, 70(1):464–
483, 2024.
20. Catherine Tucker. Identifying formal and informal influence in technology adoption with
network externalities.Management science, 54(12):2024–2038, 2008.
21. Austan Goolsbee and Peter J Klenow. Evidence on learning and network externalities in the
diffusion of home computers.The Journal of Law and Economics, 45(2):317–343, 2002.
22. Nicoletta Corrocher and Lorenzo Zirulia. Me and you and everyone we know: An empirical
analysis of local network effects in mobile communications.Telecommunications Policy,
33(1-2):68–79, 2009.
23. Jin-Hyuk Kim, Peter Newberry, Liad Wagman, and Ran Wolff. Local network effects in
the adoption of a digital platform.The Journal of Industrial Economics, 70(3):493–524,
2022.
28

24. Arun Sundararajan. Local network effects and complex network structure.The BE Journal
of Theoretical Economics, 7(1):0000102202193517041319, 2008.
25. Peter V Marsden and Karen E Campbell. Measuring tie strength.Social forces, 63(2):482–
501, 1984.
26. Claude S Fischer. What do we mean by ‘friend’? an inductive study.Social networks,
3(4):287–306, 1982.
27. Barry Wellman and Scot Wortley. Different strokes from different folks: Community ties
and social support.American journal of Sociology, 96(3):558–588, 1990.
28. Ray Reagans. Preferences, identity, and competition: Predicting tie strength from demo-
graphic data.Management Science, 51(9):1374–1383, 2005.
29. Mark S Granovetter. The strength of weak ties.American journal of sociology, 78(6):1360–
1380, 1973.
30. Mark Granovetter. Economic action and social structure: The problem of embeddedness.
American journal of sociology, 91(3):481–510, 1985.
31. Nan Lin, Walter M Ensel, and John C Vaughn. Social resources and strength of ties: Struc-
tural factors in occupational status attainment.American sociological review, pages 393–
405, 1981.
32. Jeroen Bruggeman. The strength of varying tie strength: comment on aral and van alstyne.
American Journal of Sociology, 121(6):1919–1930, 2016.
33. Sinan Aral. The future of weak ties.American Journal of Sociology, 121(6):1931–1939,
2016.
29

34. Robert D Putnam. Bowling alone: The collapse and revival of american community.Simon
Schuster, 2000.
35. Nan Lin.Social capital: A theory of social structure and action, volume 19. Cambridge
university press, 2002.
36. Ronald S Burt. The network structure of social capital.Research in organizational behav-
ior, 22:345–423, 2000.
37. Ronald S Burt.Brokerage and closure: An introduction to social capital. Oxford university
press, 2005.
38. Alan Hall and Barry Wellman. Social networks and social support. 1985.
39. James S Coleman. Social capital in the creation of human capital.American journal of
sociology, 94:S95–S120, 1988.
40. Barry Wellman, Anabel Quan Haase, James Witte, and Keith Hampton. Does the inter-
net increase, decrease, or supplement social capital? social networks, participation, and
community commitment.American behavioral scientist, 45(3):436–455, 2001.
41. J-P Onnela, Jari Saram ¨aki, Jorkki Hyv ¨onen, Gy ¨orgy Szab ´o, David Lazer, Kimmo Kaski,
J´anos Kert ´esz, and A-L Barab ´asi. Structure and tie strengths in mobile communication
networks.Proceedings of the national academy of sciences, 104(18):7332–7336, 2007.
42. Andrea Petr ´oczi, Tam´as Nepusz, and F¨ul¨op Bazs´o. Measuring tie-strength in virtual social
networks.Connections, 27(2):39–52, 2007.
43. Eric Gilbert and Karrie Karahalios. Predicting tie strength with social media. InProceed-
ings of the SIGCHI conference on human factors in computing systems, pages 211–220,
2009.
30

44. Jason J Jones, Jaime E Settle, Robert M Bond, Christopher J Fariss, Cameron Marlow,
and James H Fowler. Inferring tie strength from online directed behavior.PloS one,
8(1):e52168, 2013.
45. Moira Burke, Robert Kraut, and Cameron Marlow. Social capital on facebook: Differ-
entiating uses and users. InProceedings of the SIGCHI conference on human factors in
computing systems, pages 571–580, 2011.
46. Barry Wellman and Keith Hampton. Living networked on and offline.Contemporary
Sociology, 28(6):648–654, 1999.
47. Nicole B. Ellison, Charles Steinfield, and Cliff Lampe. The benefits of facebook “friends”:
Social capital and college students’ use of online social network sites.Journal of Computer-
Mediated Communication, 12(4):1143–1168, 2007.
48. Nicole B. Ellison, Cliff Lampe, Charles Steinfield, and Jessica Vitak. With a little help from
my friends: How social network sites affect social capital processes. In Zizi Papacharissi,
editor,A Networked Self: Identity, Community, and Culture on Social Network Sites, pages
124–145. Routledge, New York, 2010.
49. Nicole B. Ellison, Jessica Vitak, Rebecca Gray, and Cliff Lampe. Cultivating social re-
sources on social network sites: Facebook relationship maintenance behaviors and their role
in social capital processes.Journal of Computer-Mediated Communication, 19(4):855–
870, 2014.
50. Ronald S Burt. The social structure of competition.Networks in the knowledge economy,
13(2):57–91, 2003.
51. Ronald S Burt. Structural holes and good ideas.American journal of sociology,
110(2):349–399, 2004.
31

52. Minjae Kim and Roberto M Fernandez. Strength matters: tie strength as a causal driver of
networks’ information benefits.Social science research, 65:268–281, 2017.
53. Sinan Aral and Marshall Van Alstyne. The diversity-bandwidth trade-off.American journal
of sociology, 117(1):90–171, 2011.
54. Katja Rost. The strength of strong ties in the creation of innovation.Research policy,
40(4):588–604, 2011.
55. Erik Brynjolfsson, Avinash Collis, and Felix Eggers. Using massive online choice experi-
ments to measure changes in well-being.Proceedings of the National Academy of Sciences,
116(15):7250–7255, 2019.
56. Hunt Allcott, Luca Braghieri, Sarah Eichmeyer, and Matthew Gentzkow. The welfare ef-
fects of social media.American Economic Review, 110(3):629–676, 2020.
57. Roberto Mosquera, Mofioluwasademi Odunowo, Trent McNamara, Xiongfei Guo, and Ra-
gan Petrie. The economic effects of facebook.Experimental Economics, 23:575–602,
2020.
58. Angelo Mele. A structural model of dense network formation.Econometrica, 85(3):825–
850, 2017.
59. Anton Badev. Discrete games in endogenous networks: Theory and policy.Econometrica,
89(6):2569–2597, 2021.
60. Raj Chetty, Matthew O Jackson, Theresa Kuchler, Johannes Stroebel, Nathaniel Hendren,
Robert B Fluegge, Sara Gong, Federico Gonzalez, Armelle Grondin, Matthew Jacob,
et al. Social capital i: measurement and associations with economic mobility.Nature,
608(7921):108–121, 2022.
32

61. Raj Chetty, Matthew O Jackson, Theresa Kuchler, Johannes Stroebel, Nathaniel Hendren,
Robert B Fluegge, Sara Gong, Federico Gonzalez, Armelle Grondin, Matthew Jacob, et al.
Social capital ii: determinants of economic connectedness.Nature, 608(7921):122–134,
2022.
62. Duncan J Watts and Steven H Strogatz. Collective dynamics of ‘small-world’networks.
nature, 393(6684):440–442, 1998.
63. Yong-Yeol Ahn, Seungyeop Han, Haewoon Kwak, Sue Moon, and Hawoong Jeong. Analy-
sis of topological characteristics of huge online social networking services. InProceedings
of the 16th international conference on World Wide Web, pages 835–844, 2007.
64. Sinan Aral.The Hype Machine: How Social Media Disrupts Our Elections, Our Economy,
and Our Health–and How We Must Adapt. Currency, 2021.
65. Gordon M Becker, Morris H DeGroot, and Jacob Marschak. Measuring utility by a single-
response sequential method.Behavioral science, 9(3):226–232, 1964.
66. Steffen Andersen, Glenn W Harrison, Morten Igel Lau, and E Elisabet Rutstr¨om. Elicitation
using multiple price list formats.Experimental Economics, 9:383–405, 2006.
67. Jon A Krosnick and Duane F Alwin. A test of the form-resistant correlation hypothesis:
Ratings, rankings, and the measurement of values.Public Opinion Quarterly, 52(4):526–
538, 1988.
68. Alexander Coppock and Oliver A McClellan. Validating the demographic, political, psy-
chological, and experimental results obtained from a new source of online survey respon-
dents.Research & Politics, 6(1):2053168018822174, 2019.
33

69. Gordon Pennycook, Ziv Epstein, Mohsen Mosleh, Antonio A Arechar, Dean Eckles, and
David G Rand. Shifting attention to accuracy can reduce misinformation online.Nature,
592(7855):590–595, 2021.
70. Seth G Benzell, Avinash Collis, and Christos Nicolaides. Rationing social contact during
the covid-19 pandemic: Transmission risk and social benefits of us locations.Proceedings
of the National Academy of Sciences, 117(26):14642–14644, 2020.
71. Julio S Sol ´ıs Arce, Shana S Warren, Niccol`o F Meriggi, Alexandra Scacco, Nina McMurry,
Maarten V oors, Georgiy Syunyaev, Amyn Abdul Malik, Samya Aboutajdine, Opeyemi
Adeojo, et al. Covid-19 vaccine acceptance and hesitancy in low-and middle-income coun-
tries.Nature medicine, 27(8):1385–1394, 2021.
72. Apostolos Filippas, John Horton, and Elliot Lipnowski. The production and consumption of
social media. InProceedings of the 23rd ACM Conference on Economics and Computation,
EC ’22, page 287–288, New York, NY , USA, 2022. Association for Computing Machinery.
73. Arnab Sarker, Natalie Northrup, and Ali Jadbabaie. Higher-order homophily on simpli-
cial complexes.Proceedings of the National Academy of Sciences, 121(12):e2315931121,
2024.
74. Arnab Sarker, Ali Jadbabaie, and Sinan Aral. Differentiating novelty on networks with
hodge decomposition.MIT Initiative on the Digital Economy Working Paper, 2024.
75. Gal Oestreicher-Singer and Lior Zalmanson. Content or community? a digital business
strategy for content providers in the social age.MIS quarterly, pages 591–616, 2013.
76. William D Nordhaus. Schumpeterian profits in the american economy: Theory and mea-
surement, 2004.
34

77. Leonardo Bursztyn, Benjamin R Handel, Rafael Jimenez, and Christopher Roth. When
product markets become collective traps: The case of social media. Technical report, Na-
tional Bureau of Economic Research, 2023.
35

Supporting Information:
Measuring Social Media Network Effects
Sinan Aral,1∗ Seth G. Benzell,2 Avinash Collis,3 Christos Nicolaides4
1Massachusetts Institute of Technology, 2Chapman University,
3Carnegie Mellon University, 4University of Cyprus
∗To whom correspondence should be addressed; E-mail: sinan@mit.edu.
This PDF file includes:
Description of Data Collection
Results
Robustness Analyses
References
1

Contents
S1 Supplemental Materials and IRB Approval 7
S2 Research Design and Data Collection 7
S2.1 A Gap Between the Sociology of Networks and the Economics of Network Effects 7
S2.1.1 Measuring Connections and Their Value . . . . . . . . . . . . . . . . . 8
S2.1.2 Networks as Social Capital and Social Support . . . . . . . . . . . . . 10
S2.1.3 Strategic Implications of Network Ties . . . . . . . . . . . . . . . . . 11
S2.1.4 Digital Network Connection Research . . . . . . . . . . . . . . . . . . 12
S2.1.5 Economic Measurement of Network Effects and the Research Gap . . . 14
S2.2 Data Collection Through Lucid Survey Platform . . . . . . . . . . . . . . . . . 16
S2.3 Wave 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
S2.3.1 Wave 1 Instrument Summary . . . . . . . . . . . . . . . . . . . . . . . 17
S2.3.2 Dependent Variable: Connection Value Percentile (CVP) . . . . . . . . 19
S2.3.3 Explanatory Variables: Ego Demographics, Dyadic Characteristics, and
Platform Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
S2.4 Wave 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
S2.4.1 Wave 2 Instrument Summary . . . . . . . . . . . . . . . . . . . . . . . 21
S2.4.2 Dependent Variable: Total Platform Value (TPV) . . . . . . . . . . . . 23
S2.4.3 Explanatory Variables: Number of Connections, Ego Demographics,
and Platform Usage . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
S2.5 Ordinal Versus Cardinal Connection Value Solicitation Designs . . . . . . . . . 25
S2.6 Measuring Complementarity in Connections . . . . . . . . . . . . . . . . . . . 29
S3 Results 33
2

S3.1 Wave 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
S3.1.1 Connection Value Percentile by Dyadic Characteristics . . . . . . . . . 35
S3.1.2 Imputing Monetary Value for Connection Characteristics . . . . . . . . 37
S3.2 Wave 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
S3.2.1 Predictors of Total Platform Valuation . . . . . . . . . . . . . . . . . . 41
S3.2.2 Pre-registered Models Total Platform Value . . . . . . . . . . . . . . . 46
S3.2.3 The Redundant Signal Model of Local Network Effect Share of Plat-
form Value . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
S4 Robustness 71
S4.1 Robustness of Predictors of Connection Value Percentile . . . . . . . . . . . . 72
S4.2 Robustness of Predictors of Total Platform Value . . . . . . . . . . . . . . . . 74
S4.2.1 Measuring the Value of Connections with Wave 1 Data . . . . . . . . . 74
S4.2.2 Other Predictors of Total Platform Value from Wave 1 . . . . . . . . . 78
S4.2.3 Sensitivity to Alternate Maximum Platform Value . . . . . . . . . . . . 79
S5 Additional Data Collection Tables 83
S6 Full Statistical Reporting of the Findings 87
S6.1 Grouped Comparisons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
S6.1.1 Figure 1C: Total Platform Valuation by Platform & Usage, Aggregated
to Two Usage Levels . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
S6.1.2 Figure 1C: Total Platform Valuation by Platform & Usage, Aggregated
over all platforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
S6.1.3 Figure 1D: Total Platform Valuation by Platform & Political Orienta-
tion, Aggregated to Three Orientations . . . . . . . . . . . . . . . . . 89
3

S6.1.4 Figure 1D: Total Platform Valuation by Platform & Political Orienta-
tion, Aggregated over all platforms . . . . . . . . . . . . . . . . . . . 90
S6.1.5 Figure 1E: Total Platform Valuation by Platform & Relationship Status,
Aggregated to Married and Unmarried . . . . . . . . . . . . . . . . . . 91
S6.1.6 Figure 1E: Total Platform Valuation by Platform & Relationship Status,
Aggregated over all platforms . . . . . . . . . . . . . . . . . . . . . . 91
S6.1.7 Figure 2A: Connection Value Percentile by Platform & How Ego Knows
Alter, Aggregated to Three Relationship Types . . . . . . . . . . . . . 93
S6.1.8 Figure 2A: Connection Value Percentile by Platform & How Ego Knows
Alter, Aggregated over all platforms . . . . . . . . . . . . . . . . . . . 94
S6.1.9 Figure 2B: Connection Value Percentile by Platform & Frequency of
Meeting Alter, Aggregated to Three Meeting Frequencies . . . . . . . 95
S6.1.10 Figure 2B: Connection Value Percentile by Platform & Frequency of
Meeting Alter, Aggregated Across All Platforms . . . . . . . . . . . . 96
S6.1.11 Figure 2C: Connection Value Percentile by Whether You Are Con-
nected with Alter on Another Platform, Aggregated Across All Platforms 96
S6.1.12 Figure 3A: Connection Value Percentile by Platform & Gender, Aggre-
gated by Alter Gender . . . . . . . . . . . . . . . . . . . . . . . . . . 97
S6.1.13 Figure 3A: Connection Value Percentile by Whether You relative Ego
and Alter Gender, Aggregated Across All Platforms . . . . . . . . . . . 97
S6.1.14 Figure 3B: Connection Value Percentile by Platform & Race, Aggre-
gated to Alter Race . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
S6.1.15 Figure 3B: Connection Value Percentile by Whether You relative Race
of Ego and Alter, Aggregated Across All Platforms . . . . . . . . . . . 99
4

S6.1.16 Figure 3C: Connection Value Percentile by Whether You relative Age
of Ego and Alter, Aggregated Across All Platforms . . . . . . . . . . . 99
S6.1.17 Figure 3D: Connection Value Percentile by Platform & Alter Age, Ag-
gregated to Alter Over or Under Age 18 . . . . . . . . . . . . . . . . . 100
S6.1.18 Figure 3D: Connection Value Percentile by Platform & Alter Age, Ag-
gregated Across All Platforms . . . . . . . . . . . . . . . . . . . . . . 101
S6.2 All Statistical Comparisons . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
S6.2.1 Figure 1B: Average Total Platform Valuation by Platform and Average
Total Platform Valuation that is attributed to the local network effects
by Platform . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
S6.2.2 Figure 1C: Total Platform Valuation by Platform & Usage Levels . . . 103
S6.2.3 Figure 1D: Total Platform Valuation by Platform & Political Orientation 106
S6.2.4 Figure 1E: Total Platform Valuation by Platform & Relationship Status 110
S6.2.5 Figure 1F: Total Platform Valuation by Platform & Job Seeking . . . . 111
S6.2.6 Figure 2A: Connection Value Percentile by Platform & How You Know
Alter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
S6.2.7 Figure 2B: Connection Value Percentile by Platform & Frequency of
Meeting Alter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
S6.2.8 Figure 2C: Connection Value Percentile by Platform & Whether Ego is
Connected with Alter on Other Platform. . . . . . . . . . . . . . . . . 117
S6.2.9 Figure 2D: Connection Value Percentile by Platform & Whether Ego is
Connected with Alter on Each other Platform . . . . . . . . . . . . . . 117
S6.2.10 Figure 3A: Connection Value Percentile by Platform & Ego and Alter
Gender . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
5

S6.2.11 Figure 3B: Connection Value Percentile by Platform & Ego and Alter
Race . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
S6.2.12 Figure 3C: Connection Value Percentile by Platform & Relative Age of
Ego and Alter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
S6.2.13 Figure 3D: Connection Value Percentile by Platform & Absolute Age
of Alter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
S6.2.14 Figure 4A: Total Platform Valuation by Platform Feature Use . . . . . 127
S6.2.15 Figure 4B: Total Platform Valuation by Platform Feature Use and Income130
References 135
6

S1 Supplemental Materials and IRB Approval
This document contains supplemental materials for “Measuring Social Media Network Effects.”
Our research was approved by the Massachusetts Institute of Technology’s (MIT’s) Institutional
Review Board1 and analyses were pre-registered at the Open Science Foundation (OSF). 2 For
Wave 1, we ask respondents to follow our research accounts on social media platforms. For
Wave 2, we collect email addresses of respondents for following up with them for additional
rewards. For both waves of the surveys, we permanently deleted all personally identifying
information (social media handles, email addresses, and names of their connections) as soon as
the data collection was completed. As noted, the MIT IRB reviewed and approved all of these
protocols. The survey instruments for Instagram for both waves are appended at the end of this
document. The survey instruments for other platforms are identical.
S2 Research Design and Data Collection
S2.1 A Gap Between the Sociology of Networks and the Economics of
Network Effects
Our research speaks to literature from sociology on the nature and role of networks, and from
economics on the value of network effects. While both fields have established the importance
of relationships, including online relationships, ours is the first paper to measure local network
effects, to assign economic value to relationships in an incentive compatible way and to distin-
guish heterogeneity in the value of network effects across social media platforms.
1IRB protocol ID for Wave 1: E-3229, IRB protocol ID for Wave 2: E-5633
2https://osf.io/qs4kn/?view only=5cee408999b5484dafcc9626e88c953b
7

S2.1.1 Measuring Connections and Their Value
While we are unaware of other papers valuing connections on social media, there have been
sociological studies of the value of ties and the predictors of high-value relationships. Many
studies have measured the strength of ties (1–3). For example, in Marsden and Campbell (2),
which measured predictors of tie importance, dependent variables included self-reported close-
ness on a scale of 1-3 3 and a composite set of objective measures of closeness (e.g. time spent
together). The study conducted surveys of individuals in three cities (1,013 native-born white
males in the Detroit metropolitan area, 496 non-institutionalized adults in Aurora, Illinois, and
820 drawn from the eligible voters in an unnamed West German city). The study began with
each participant self-reporting the names of their three closest friends. Then, many features of
their relationship were coded, including both measures that were thought to predict closeness
(such as whether the two were related) and measures of closeness. The study found that kin-
ship was a relatively strong predictor of closeness, but that the explanatory variables had low
predictive power overall.
A second classic study, with elements similar to our own by Fischer (3), asked “What do
we mean by friend?” In this study the dependent closeness variable was binary—whether a
person was classified by the individual as a friend. The study was conducted on 1050 adults
living in northern California and began with the interviewer asking open-ended questions about
the subject’s relationships, to generate a list of 2-26 acquaintances per subject. The subject
then reported several facts about the individual and their relationship. 59% of acquaintances
qualified as friends, while 41% did not. The study found no strong patterns in which types of
contacts were considered friends, as an overwhelming majority of non-relative acquaintances
were classified this way.
Other studies have looked into how different friendships provide different types of value,
3Namely: ‘acquaintance (coded 1), a good friend (2), or a very close friend (3)’
8

without trying to construct a measure of overall value (e.g. Wellman and Wortley (4)) as well as
which relationships tend to be emotionally intense over the long term (e.g. Roberts et al. (5)). In
the first study, different measures of social support (e.g. home health visits, financial assistance)
are associated with different types of acquaintances. In the latter study, 25 students were asked,
over an 18-month period, who they felt emotionally intimate with. Features of these relation-
ships were solicited and the study found kinship ties positively predicted enduring, emotionally
close relationships.
Our dependent variable (CVP) has advantages over these and other approaches. First, and
perhaps most importantly, it quantifies value in an incentive compatible choice framework.
Such measurement enables economic analyses relevant to social, industrial and judicial pol-
icy by standardizing value measurement in a quantitative framework that is comparable across
consumers and likely to solicit high fidelity measures of economic value due to incentive com-
patibility. Second, soliciting CVP over eight options also provides more information than a
binary classification or a 1-3 scale. Rigorous quantification of subjective value is important be-
cause objective measures, like time spent, may not be sufficient to capture the subjective value
provided by social media platforms as we may communicate less frequently with some very
high value relationships. Third, a rank-ordered list may be easier for subjects to reason over
than a binary classification or scale, when these use vaguely defined terms (6). Finally, in this
setting, the rank-ordering task is conceptually easier than soliciting cardinal connection pref-
erences through BDM or a similar mechanism. While BDM may work well for soliciting the
overall value of a platform, it would be cognitively hard to estimate the value of a particular
connection in monetary amounts.
Our approach shares some weaknesses with previous approaches. We rely on self-reported
acquaintance names and evaluate relative value over this set of names. However, in section
S4.1 we provide robustness analyses related to the concern that our results are driven by our
9

acquaintance generation process by analyzing data restricted to just the four closest contacts
(omitting the four other top-of-mind contacts). This restricts attention to the subset of names
that the subject is likely to have the strongest and most reliable feelings about. Our analyses
indicate our relative ranking is robust to the acquaintance generation process. Moreover, if two
connections are similarly ranked, forcing respondents to select one over the other may increase
cognitive load and result in random responses (7). However, relative ranking is still a much
easier question framing compared to separately soliciting connection valuations (7).
S2.1.2 Networks as Social Capital and Social Support
Seminal work by Granovetter (8) proposed the importance of weak ties for accessing informa-
tion and opportunities, including job opportunities. Rajkumar et al. (9) conducted a large-scale
randomized experiment on LinkedIn to causally test the impact of weak ties on employment
outcomes. They found evidence supporting Granovetter’s thesis that weak ties have the greatest
impact on job mobility while strong ties have minimal impact, with the caveat that the relation-
ship is non-linear, meaning moderately weak ties provide greater employment opportunities
than strong ties or very weak ties.
Coleman (10) posits that social capital—comprising relationships, trust, and norms within
social structures—plays a crucial role in developing human capital, such as skills and knowl-
edge. He identifies three primary forms of social capital: obligations and expectations within
relationships, information channels that facilitate knowledge exchange, and social norms that
guide behavior. Coleman emphasizes the significance of “closure” in social networks, where
tightly-knit communities effectively enforce norms and trust. He illustrates this with exam-
ples like family dynamics and community involvement, highlighting that the presence of social
capital can enhance educational outcomes and individual development. Unlike physical or hu-
man capital, social capital is embedded in social relationships and is often a collective asset,
10

benefiting not just individuals but the broader community. Coleman’s work underscores the
importance of social structures in shaping individual actions and outcomes.
Recently, Chetty et al. (11, 12) conducted one of the largest studies examining the impact
of social capital on economic mobility in the United States. Utilizing data from 21 billion
Facebook friendships, they introduced the concept of “economic connectedness,” which mea-
sures the degree of interaction between individuals from different socioeconomic backgrounds.
Their research revealed that communities with higher economic connectedness exhibit greater
upward income mobility for children from low-income families. The studies identified two
primary factors influencing economic connectedness: “exposure,” referring to the presence of
individuals from diverse socioeconomic backgrounds within shared environments, and “friend-
ing bias,” the tendency to form friendships within one’s own socioeconomic group. Both limited
exposure and high friending bias were found to equally impede cross-class friendships. These
findings suggest that policies aimed at increasing socioeconomic diversity in communal settings
and encouraging cross-class interactions can enhance economic mobility.
S2.1.3 Strategic Implications of Network Ties
There is also a sociological literature on the strategic value of networks. Like this manuscript,
research of this type emphasizes that not all ties are created equal. In particular, the value and
impact of a tie may depend on overall network structure.
One prominent theory of how networked social structure drives value was proposed by
Burt (13). Burt distinguishes between connections that broker across ‘structural holes’ and
connections that simply increase the density of connections between nodes that are already
closely connected. He argues that the sociological evidence is consistent with the former being
most valuable, but with both playing important roles. Burt finds evidence consistent with this
theory in data on the networks of managers employed in a large corporation (14). Managers
11

who bridged structural holes of disparate business entities were paid more and were noted to
have better ideas. Building on the theory of structural holes, (15) argues that those that bridge
holes should have disproportionate value in settings with high practical uncertainty but low so-
cial uncertainty. Similarly, (16) emphasizes that real economies are not pure markets conducted
by a Walrassian auctioneer, but rather embedded in social networks that can inspire managerial
strategies or retard innovation.
Another theory of how network connection topology relates to value was developed in (17).
This model, relevant for political and social as well as economic settings, suggests that when
individuals self-interestedly form or disconnect links, there are typically multiple equilibria, and
none are guaranteed to be efficient. Papers have considered strategic action in the context of
political networks as well. One foundational paper in this domain is (18). This paper evaluates
the rise of the Medici banking family to dominate renaissance Florence. The authors, Padgett
and Ansell, document how Cosimo de Medici made a series of marriages and business deals that
placed him at the center of the political, social and economic world. They theorize his foresight
set up his dynasty for centuries of success. Relatedly, (19) found royal marriage networks play
a major causal role in preventing wars in Early Modern Europe.
S2.1.4 Digital Network Connection Research
Several papers have also looked at the importance of connections on digital platforms. Wellman
et al. (20) analyzed data from one of the largest-scale web surveys in 1998 to study whether
internet use affects social capital. The key finding of their work is that online interactions
supplement face-to-face communication. Online network connections maintain and enhance
offline face-to-face connections, particularly connections which are socially and geographically
dispersed. Moreover, internet use increases involvement in offline organizational and political
activity. Similarly, Burke et al. (21) studied the impact of using Facebook on social capital.
12

They find that receiving messages from friends on Facebook is linked with increases in bridging
social capital. Wellman and Hampton (22) also find that the internet strengthens real-life local
links within neighborhoods and households.
From a network science perspective, Onnela et al. (23) analyze communication patterns of
millions of mobile phone users to construct a population-level social network and explore the
relationship between network topology and tie strength. They find that there is a correlation
between tie strength and the local network structure around the tie. They further explore how
removing ties impacts network integrity. Removing weak ties results in network collapse, while
removing strong ties has little impact on network integrity while still playing an important role
in maintaining local communities.
Another literature investigates the role of social media connections in creating and main-
taining self-reported social capital. In this literature, social capital may be “bridging” i.e. in-
creasing a user’s access to novel or socially distant information, or “bonding” i.e. deepening
existing ties (24,25). The concept of bridging ties is connected to Burt’s structural holes (13), as
these holes are why these bridges are valuable. It is also connected to the concept of ‘weak ties’
or the more distant relations who in aggregate provide many important opportunities (8). One
early survey of 800 MSU undergraduates users found more intense Facebook users had more
perceived social capital (26), especially “bridging” social capital as measured through questions
like “Interacting with people at MSU makes me feel like a part of a larger community”. A 2011
survey of 614 Midwestern US university nonfaculty staff also found that those with more in-
tense Facebook friends and who performed more Facebook relationship maintenance activities
had stronger perceived bridging capital both online and offline (27). Research suggests that this
is due to Facebook lowering the cost of maintaining social ties (28).
Several studies have also measured tie strength quantitatively using surveys and digital trace
data. Petr ´oczi et al. (29) developed an 11-question survey scale to provide a continuous measure
13

of tie strength in online communities. Gilbert and Karahalios (30) instead measured tie strength
using a prediction model based on social media data. Jones et al. (31) focused on inferring real-
world tie strength using Facebook data. Facebook users were asked to name their closest friends
in real life. In this study, interaction frequency on Facebook successfully predicted real-world
strong ties. This provides confidence in our methods, as we also ask people to name their close
ties.
S2.1.5 Economic Measurement of Network Effects and the Research Gap
In addition to the previous literature, several economic studies have estimated total platform
valuations in the context of network effects in the aggregate. Brynjolfsson and Kemerer (32)
studied the spreadsheet market in the 80s and 90s to measure aggregate network effects in this
market and its impact on pricing. Using a hedonic model to estimate the impact of network
externalities and other software features on pricing, they find that a 1% increase in the installed
base is associated with a 0.75% increase in price.
Tucker (33) explores how formal and informal social influences affect technology adoption
in the presence of network externalities. Analyzing the rollout of a video-messaging tool within
a firm, she finds that adoption by managers and employees in key network positions signifi-
cantly boosts uptake among others, whereas adoption by ordinary workers has minimal impact.
Boudreau (34) investigates how subjective expectations influence the early adoption of plat-
forms with network effects. Using a field experiment, he finds that optimistic statements about
future user base size significantly boost adoption rates more than disclosures of the current user
base. The findings underscore the importance of managing market expectations to overcome
the initial “chicken-and-egg” problem in platform adoption.
On the methodological side, Bramoulle et al. (35) introduce a method to identify peer ef-
fects within social networks. By leveraging the structure of these networks, they distinguish
14

between endogenous peer influences and contextual factors, providing conditions under which
peer effects can be empirically identified.
Recent literature has also looked at quantifying the total platform value of various social
media platforms. Brynjolfsson et al. (36) introduced the method of incentivized choice exper-
iments, similar to the ones we use in this paper, to quantify the total value of various popular
digital apps. Allcott et al. (37) build upon this work and estimate the causal impact of Facebook
on subjective well-being in addition to quantifying Facebook’s total platform value. We com-
pare our total platform valuations in this paper with those of these papers in the SOM. What is
missing from this literature on economic measurement of network effects is that these studies
have not measured consumers’ economic valuations of network connections, measured tie value
in the context of economic network effects in an incentive-compatible way or distinguished het-
erogeneity in the value of network effects across social media platforms—all elements of what
we do in this paper.
To summarize, sociological research has extensively explored the value of social network
connections, focusing on aspects like tie strength, social capital, and digital interactions. How-
ever, sociologists have not directly measured how individuals economically value these ties,
particularly within the framework of economic network effects. Conversely, economic studies
have assessed the overall value of platforms and the impact of specific network connections on
economic outcomes such as income mobility, but they have not measured consumers’ economic
valuations of network connections or measured tie value in the context of economic network ef-
fects. As a result, a large and important gap exists, between the sociology of networks and the
economics of network effects, in our understanding of local network effects. This highlights
a significant gap between sociology and economics in measuring local network effects, some-
thing we aim to fill in this paper. In this paper, we assign economic value to relationships in an
incentive-compatible way and distinguish heterogeneity in the value of network effects across
15

social media platforms. These specific questions and measurement frameworks are essential to
the primary policy and strategy questions facing lawmakers and platform managers today.
S2.2 Data Collection Through Lucid Survey Platform
We conducted online surveys of US users regarding their use of four major social media plat-
forms: Facebook, X (formerly known as Twitter), Instagram, and LinkedIn. Subjects were
recruited through Lucid, a market research firm. Lucid provides high-quality responses for
online surveys and is one of the largest marketplaces for online sampling in the US (38). Ap-
proximately 375,000 respondents take part in studies every day on Lucid and over 30 million
respondents pass through the exchange every year (38). Coppock and McClellan (38) ran sev-
eral classic experiments and compared results on Lucid to other traditionally well-regarded
polling and survey platforms like the American National Election Studies (ANES). While these
platforms differ in that Lucid participation is ‘opt-in’ and standard polling uses probability sam-
pling, they found that the demographics and experimental results of the Lucid samples were
comparable to those obtained from standard US probability samples.
Many academic studies have used Lucid. For example, Pennycook et al. (39) conducted
survey experiments on Lucid to test interventions that can reduce misinformation sharing online.
Sol´ıs Arce et al. (40) studied factors that explain COVID-19 vaccine acceptance by conducting
a large-scale survey on Lucid. Benzell et al. (41) conducted a survey on Lucid to understand
people’s preferences for keeping businesses and other locations open during the COVID-19
pandemic.
Lucid provides us with users of the four social media platforms that we study—Facebook,
X, Instagram, and LinkedIn—and verifies that participants are monthly active users of the plat-
form under consideration. Subjects are paid directly by Lucid (the exact amount is determined
based on their demographic profile), and we pay Lucid for the participant fee and survey ad-
16

ministration costs. Lucid provides additional responses at no cost for responses that are rejected
for failing to pass an attention check.
We conduct two Waves of surveys. Wave 1 was conducted from 2/24/2021 to 5/10/2022
and collected 10,528 valid responses. Wave 2 was conducted from 11/1/2023 to 12/19/2023
and collected 9,395 valid responses.
S2.3 Wave 1
In the Wave 1 survey, our goal was to understand how the characteristics of consumers’ con-
nections relate to how they value those connections on social media. We refer to the subjects of
these surveys as “egos,” and the network connections they are asked to characterize and evaluate
as “alters.” For this wave, consumers on each of the four platforms that we study were recruited
and asked to report on their use of one platform.
S2.3.1 Wave 1 Instrument Summary
Before launching Wave 1, we created a research account on each of the four platforms studied.
In the first step of the Wave 1 study, we asked respondents to connect with our research account.
This step ensures data quality and allows collection of additional data of interest. At this stage,
respondents could choose to exit the survey. After connecting to our research account, ego
respondents were asked about their demographics (age, gender, ethnicity, income and political
ideology) and usage of social media platforms, including the amount of time they spend on
these platforms. These questions were asked with responses provided as dropdown lists with
options.
In the next part of the survey, egos were asked to identify eight individuals (alters). The
first four were their four closest connections (who they may or may not be connected to on
the platform).4 The second four were “any four connections excluding the four closest connec-
4The question text is: “Name your most important contacts (first name and last initial) ranked in order from
17

tions” that they were “connected to on [platform].” We then asked the egos to characterize their
relationships with these alters. More specifically, for each of these connections, we asked for
their age, gender, ethnicity, how the ego knows them, how often the ego sees this person face to
face, and if they are connected to them on other social media platforms.
In the next section of the survey, (following Brynjolfsson et al. (36) and Allcott et al. (37)),
we solicited egos’ total overall valuations of social media platforms using the Becker DeGroot
Marschak (BDM) method (42), by asking them for the minimum dollar amount they were will-
ing to accept (WTA) to give up access to the platform for one month. Consumers provided
answers by moving a slider to enter a value between $0 and $100, with an option to enter values
greater than $100 in an open-ended text box.
We informed the respondents that we would select 1 in 200 respondents and follow up with
them to receive rewards of at least $200. Once we verified that they entered all the details of
their connections accurately, they would be eligible to receive $200. In addition to this, they
would be eligible to receive additional rewards based on the outcome of their BDM lottery.
The procedure for the additional rewards was as follows. We drew a random amount of money
from a distribution. If the random offer was greater than the valuation the respondent entered,
they would receive the random offer as an additional reward if and only if they deactivated
their account for one month. If the random offer was less than their valuation, they would not
have to do anything, and they would not receive any additional reward. This mechanism is
incentive-compatible and is widely used in experimental economics to solicit valuations (43).
We followed up with respondents selected for additional rewards through Lucid. As per
our agreement with Lucid, we did not have direct contact with the respondents in Wave 1 and
Lucid reached out to the selected respondents through their portal, but no respondents replied.
To increase the chances of response, in Wave 2 we acquired respondents’ emails and reached
most important to 4th most important. These contacts could include friends, family, and colleagues or any other
type of relationships.”
18

out to them directly. Still, respondents answered their valuation solicitation question under the
impression that responses were incentive-compatible. This is in line with other recent incentive
compatible implementations of BDM in the social media context, such as Bursztyn et al. (44)
who, in the context of TikTok and Instagram, promised to enforce BDM contracts only un-
der circumstances known to the experimenters ex-ante to be impossible, preserving incentive
compatibility without enforcement.
After the platform valuation question, we asked respondents to rank how valuable they find
their eight connections using a rank order question adapted to measure the value of networked
connections and local network effects, which we call Connection Ranked Choice (CRC).
Consumers of all four platforms received the same survey instrument with a slight modifi-
cation for Facebook and LinkedIn, where we only asked egos if they are connected to alters,
unlike Instagram and X, where we asked egos if they follow alters and if alters follow them.
A key aspect of Wave 1 is that egos are required to follow/friend our research account on the
platform to qualify for the study. When egos follow/friend our research account, we can see
their entire set of public profile information for that platform, as well as their list of contacts, if
it is public. We reject observations which do not choose to follow our account. We collected
valid responses from 4,149 Facebook users, 2,899 X users, 1,981 Instagram users, and 1,499
LinkedIn users.
S2.3.2 Dependent Variable: Connection Value Percentile (CVP)
To understand what characteristics lead to highly valued connections on digital platforms, we
constructed a measure of the relative value of connections, called “Connection Value Percentile”
(CVP). This measure is derived from our Wave 1 questionnaire about individual connections.
The egos in our study name and describe up to eight alters they are connected to on the focal
platform. On a subsequent survey page, we solicit the relative importance of these contacts
19

using a rank-order question (Connection Ranked Choice (CRC)). The exact text of the relevant
question is “Please rank the following connections from most valued on [PLATFORM] (top) by
you to least valued on [PLATFORM] (bottom) by you.”
Using the provided ranking we calculate CVP as
CV Pi,j,p = 100(1− CR i,j,p −1 T CRi,p )(S1)
whereCR i,j,p is the ranking given to connectionjby egoion platformpon our relative
ranking scale andT CRi,p is the total number of connections ranked by consumerion platform
p. This measure evaluates which relationships are more valued on the platform. To summarize
these relationships, we calculate average CVPs conditional on a given dyadic characteristic.
Larger CVPs for one dyadic characteristic versus another indicate that those types of relation-
ships are valued more highly, on average.
S2.3.3 Explanatory Variables: Ego Demographics, Dyadic Characteristics, and Platform
Usage
For our Wave 1 analysis, the first set of data collected is the information from the ego’s public
social media profiles. For Facebook, we downloaded respondents’ entire connection list and
matched these names with census data from the US Social Security Administration to estimate
the race and gender of alters. 5 For LinkedIn, we downloaded respondents’ profiles and their
education and career history. For X, we used the X API to download rich information about
respondents’ profile information and posting activity, as well as the number of followers and
followees. Instagram was the only platform from which we were unable to gather complemen-
tary information due to restrictions imposed by the platform. Table S1 summarizes the data we
were able to collect by platforms.
Our main set of explanatory variables are alter characteristics as reported in the survey.
5https://www.ssa.gov/oact/babynames/limits.html
20

Platform Additional Information Collected
Facebook Ego’s public friend list
LinkedIn Ego’s profile (e.g. resume information)
X Ego’s Timeline history, list of followers and followees
Instagram N/A
Table S1: Summary of additional information collected by survey platform. Section S5 provides
additional information on data collected from LinkedIn and X participants.
The alter characteristics solicited were: age, gender, ethnicity, how ego knows them (school/
college/ shared interest/ family member/ only know them online), how often ego sees this person
face to face (or lives with them), and if they are connected to them on any of the other social
media platforms. Other explanatory variables are the ego characteristics (gender, age, ethnicity,
income, political affiliation) and platform usage characteristics (time spent on each of the four
platforms) self-reported in the survey.
S2.4 Wave 2
Wave 2 is focused on determining the predictors of ego’s overall platform valuation and the role
of social network connections as a predictor. Wave 2 follows the design of Wave 1. However,
there is a focus on ascertaining total platform value in an incentive-compatible manner as well
as directly soliciting the count of the ego’s connections.
S2.4.1 Wave 2 Instrument Summary
We first recruited users of one of the four social media platforms from Lucid to participate in
our study. Respondents were asked for their email addresses at the beginning of the study so
that we could follow up with them if they were selected for additional rewards. If they choose
not to share their email address, they exited the survey. At this stage 1195 or 30% of Facebook
recruited respondents exited the survey; 644 or 19% of Instagram recruited respondents exited
the survey; 648 or 17.7% of LinkedIn recruited respondents exited the survey; and 691 or
21

18.8% of X recruited respondents exited the survey. Given that 70-82% of recruited users were
retained after being asked to give their email address and agreeing to the terms of service, we
feel retention is not a significant issue for our study although we cannot compare respondents
who opted out of the experiments to those who were retained since those who exited did not
answer survey questions or provide permission for other data collection. Users (egos) were then
asked about their demographics (age, gender, ethnicity, income, and political ideology), usage
of the platform, and their total number of connections on the platform. For users of Facebook
and LinkedIn, we collected their total number of connections on these platforms directly. For
users of Instagram and X, we collected both the number of followers and followees.
Unlike Wave 1, we also collected information about which features consumers used on
each of the platforms. On Facebook, respondents were given the option to select one or more
features from posting on the news feed, to engaging with content from connections, follow-
ing pages, playing games, joining groups, organizing and attending events, buying and selling
on Marketplace, messaging on Messenger, and using Facebook Live. On Instagram, respon-
dents were asked to select one or more options from posting photos/ reels/ stories, liking and
commenting on photos/ reels/ stories, streaming on Instagram Live, and direct messaging other
users. On LinkedIn, respondents were asked to select one or more options from updating their
profile, using groups, liking, commenting, and sharing content, and searching and applying for
jobs. On X, respondents were asked to select one or more options from posting posts, liking/
replying to/ reposting posts, direct messaging other users, bookmarking posts, using X Lists,
using X Spaces, and subscribing to X Premium.
In the next section of the survey, we solicited egos’ valuations of social media platforms
by asking them for the minimum dollar value they were willing to accept (WTA) to give up
access to a platform for one month using a variation of incentive-compatible BDM, following
Brynjolfsson et al. (36). Valuations were solicited using a multiple price list (45), and the upper
22

limit of the price range was randomly selected to be either $100, $150, or $200 to account
for anchoring effects. The multiple price list is analogous to a discrete choice experiment as
described in Brynjolfsson et al. (36) and de Bekker-Grob et al. (46).
All platforms used the same survey instrument except for the question related to the usage
of platform-specific features, which had different feature options. Respondents who selected a
fake social media platform (“Mystro”) as one of the platforms that they use were also filtered out
of the survey for failing an attention check. The platform valuation experiments were incentive
compatible and provided consumers an opportunity to be paid when the incentive compatibility
constraint became binding—when they were verified to have given up the platform and were
paid to do so. For participants who received the upper limit of $100 in the multiple price list
question, 1 in 100 respondents were randomly selected and offered to follow up on their choices
(1 in 150 for those with upper limit of $150 and 1 in 200 for those with upper limit of $200). We
made cash offers of a randomly selected value if and only if they deactivated the platform. 70%
of those who were made cash offers to deactivate a platform complied with their offers. We
received valid responses from 2470 Facebook users, 2237 X users, 2488 Instagram users, and
2200 LinkedIn users. Summary statistics for the second Wave data are presented in Table S10.
All pre-registered results for Wave 2 of the study not included in the main text are included in
the sections below.
S2.4.2 Dependent Variable: Total Platform Value (TPV)
As mentioned previously, we solicited the minimum dollar value respondents’ were willing to
accept (WTA) to give up a platform for one month using a BDM and a multiple price list.
Respondents made a series of choices between keeping access to the platform or giving it up
for one month in exchange for a certain monetary compensation. The price list was offered in
increments of $5, ranging from a minimum of $5 to a maximum of either $100, $150, or $200,
23

assigned randomly, to ensure our results are robust to anchoring effects (47).
Prices were listed in multiple rows on a single page, ranging from the lowest price to the
highest price. For each row, respondents made a choice between keeping access to the platform
or giving it up for one month in exchange for the price listed in that row. We followed up
with randomly selected respondents and selected one of their rows from the multiple price list
question. Whatever choice was made by the respondent was offered to them. For example, if
they chose to give up access to a platform for $45 in a particular row, we offered them the chance
to actually give up that platform and get paid $45 at the end of the month after we verified that
they complied with their choice. Therefore, our valuations are incentive-compatible.
Since prices were listed in increasing order, respondents made a switch at some point from
keeping access to the platform to giving it up in exchange for a certain price. Our dependent
variable, total platform value, is measured by looking at the lowest price at which respondents
made this switch. For example, if a particular respondent didn’t accept prices until $80 but
switched and started accepting prices from $85 and above to give up access to a platform for
one month, their total platform value for that platform was assessed as $85.
S2.4.3 Explanatory Variables: Number of Connections, Ego Demographics, and Plat-
form Usage
For our Wave 2 analysis, our explanatory variables included the ego demographics and platform
usage characteristics previously listed. In addition, a key explanatory variable that we measured
in this study was the total number of connections a respondent has on a given platform. Previous
literature has documented the impact of network effects on platform value (48). Based on
this, we hypothesized that platform value is increasing in the number of connections. While
we focused on the characteristics of connections in Wave 1, we analyzed the total number of
connections and their association with total platform value in Wave 2.
24

S2.5 Ordinal Versus Cardinal Connection Value Solicitation Designs
When soliciting connection value through incentive compatible designs, a natural choice arises
in whether to solicit connection values ordinally or cardinally. For example, one option is
to solicit connection values by randomly selecting some connections from an ego’s network
and soliciting their willingness to accept payments for disconnecting from that connection for
a specified period of time. We considered this research design in depth and even conducted
exploratory studies to evaluate its reliability, robustness and appropriateness. In the end, several
factors made clear that this design is likely unreliable in soliciting connection value.
First, implementing plausible, connection specific, incentive compatible designs at scale in
a fully remote, online setting is technically challenging. The study participant’s full contact list
needs to be collected, parsed, and then a random subset selected, all within the initial survey
time-frame. In a lab setting, for Instagram, we achieved this by assisting participants in carefully
copy-pasting their contacts into a specially designed desktop application.
Putting aside these concerns, we conducted a laboratory study to test the practicality of the
cardinal, incentive compatible connection value solicitation design.6 We recruited 316 students
to participate in a one-hour session with optional online follow up. Study participants were
asked to report on their entire list of Instagram contacts, directly copied and pasted from their
main Instagram account. Using the standard BDM mechanism, we asked subjects their willing-
ness to accept (WTA) offers to disconnect, on Instagram, from 1, 5, or 10 randomly selected
followers or followees for one semester (about 3.5 months), as well as for giving up Instagram
altogether. The randomly selected contacts’ handles were displayed for the subjects to see as
they made their decisions. Of the 316 study participants, 119 were made follow up offers larger
than their stated willingness to accept. Of these, 80 remained in compliance with the restric-
6Experiment approved by Chapman University IRB: IRB-22-304 Measuring Digital Network Effects Using
Incentivized Choice Experiments
25

tions for the entire semester and were made compliance payments averaging $87.17. Figure S1
below summarizes our findings on the WTA of subjects to give up randomly selected connec-
tions. There are a few surprising things about the results that led us to reject using this design
to measure connection value.
Figure S1: Scatterplot and quadratic line of best fit of study participants’ minimum required
payments (i.e. WTA) to block 1, 5, or 10 randomly selected Instagram contacts. In the left panel,
A, the random names were selected from those followed by the study participant (followees). In
the right panel, B, the random names were selected from those following the study participant
(followers).
First, subjects requested an average of almost $30 to disconnect from a single randomly
selected follower or followee—an implausibly high valuation for a single connection for a pe-
riod of 3.5 months. Exit interviews suggested that bias in connection valuation may have arisen
from a) a fixed cost of monitoring, b) loss aversion or c) a high cost of the social signal of
disconnection. The fixed cost of monitoring arises from subjects’ distaste of being digitally
monitored. The problem with this fixed cost of monitoring is that it biases connection value es-
timates disproportionally and extremely compared to platform value estimates. To understand
why, consider this toy example: Suppose for a specific person the actual value of a random con-
nection is 1 penny, and the actual total platform value is $20. Suppose the cost of monitoring is
$10. The WTA an offer to disconnect from that connection would be $10.01, a 1000x bias. In
26

estimating the platform value, we’d estimate $30, a 1.5x bias. Loss aversion would arise from
the psychological cost from losing a monetarily low value resource (a single connection), that
is not matched symmetrically by as large a gain from acquiring the resource (or connection).
Finally, the negative social signal of disconnecting from a connection may be an additional cost
that biases connection value estimates in this design upward, which is itself unrelated to the ac-
tual value of the connection. If we perceive a significant social cost to slighting our connection,
the incentive compatible disconnection design would not produce a reliable connection value
solicitation because it would bias connection value estimates upward significantly and unnec-
essarily as the concept of disconnection is merely an artifact of the value solicitation method
rather than an intrinsic element of the value of the connection.
Second, the relationship between the number of connections to be removed and the WTA
is non-linear (see Figure S1), suggesting a strongly increasing marginal value of connections,
which is also itself implausible. To understand why, consider Figure S2 below. The figure
depicts the number of social media contacts on the X-axis, and platform value on the Y-axis. The
utility function is upward sloping, indicating an increasing marginal value of contacts or that, for
example, the marginal value of 100th connection is significantly higher than the first connection.
As the figure illustrates, the immediate corollary of this is that the WTA disconnections has
decreasing marginal costs.
It is not surprising that total platform value, across all users of a platform, would be in-
creasing in the number of connections. If all connections have the same, constant value, then
the total value of the entire platform to all users grows with the square of the number of users.
This observation is known as ‘Metcalfe’s Law.’ However, mature networks in long-term equi-
libria likely have constant or decreasing network effects in the number of users. Otherwise, a
very small increase or decrease in the number of participants would have dramatic effects on
the value from, and future participation in, the network. We think it implausible from a net-
27

Figure S2: This figure is a stylized illustration of a utility function with increasing returns to
the number of connections. In this example, the platform user would require at least $20 to
disconnect from a single connection, and would require $30 to disconnect from 5 users - a
cost of only $6 per user. This figure shows how increasing returns to connections generates a
decreasing cost of disconnection per-connection as in our lab experiment. The dashed lines on
the y-axis and curve indicate the figure is not to scale.
28

work stability perspective that losing a single connection is so impactful, and so much more
impactful, per-connection, than disconnecting from 5 or 10 contacts.
We also feel this is an important area of future work. If we can devise reliable strategies for
measuring local network effects, an important next step in the work is to empirically validate
the shape of the utility function that captures network effects and local network effects, and to
understand whether network effects are non-linear, marginally increasing or decreasing in the
number of contacts, and how the shape of the network or the type of contacts considered affects
the shape of the utility function.
Ultimately we eschewed using the BDM mechanism to solicit connection value for three
reasons: (1) the difficulty in having plausible IC at scale in a fully remote online setting in-
cluding the cognitive difficulty in evaluating the ‘dollar value of a connection’, a much more
unusual, alien or distasteful task relative to simply ranking their importance, (2) the theoreti-
cally small value of individual connections would be dwarfed by the variance of such estimates
making estimation extremely challenging, (3) experimental biases arising from loss aversion,
the fixed costs of monitoring and the costs of negative social signals from disconnection, all of
which were plausibly displayed in our laboratory study.
For these reasons, we believe the way forward for connection value solicitation and local
network effects estimation is the combination of incentive compatible platform value solicita-
tion designs and connection rank choice, which describe and implement in this study.
S2.6 Measuring Complementarity in Connections
The elasticity of substitution between a pair of inputs refers to how much the ratio of marginal
values of the two inputs changes as a result of an increase in the use of one of the inputs. In the
context of social media connections, one might be interested in how the value of a connection
on a focal platform changes as a result of a connection being formed on an alternate platform.
29

This elasticity has practical implications for policymakers. For antitrust enforcers, for example,
complementarity and substitution patterns across different platforms are relevant to judging
the consumer welfare effects of mergers. When communications across a pair of services are
substitutes, combinations of social media firms will necessarily have more market power – a
“market” being defined as a set of products which are close substitutes (49).
In the context of discrete inputs, complementarity is defined as when the value of both inputs
together is greater than the sum of the value of each input alone, i.e.:
V(1,1)–V(0,0)≥V(1,0)–V(0,0) +V(0,1)–V(0,0).
Where V(X,Y) total outcome value as a function of two binary input choices. (50)
We can use this definition to determine whether connections to the same person across
different platforms are complements in our data. To do so, we interpret CVP as a measure of
the marginal value of a connection. Rearranging the complementarity criteria yields:
V(1,1)–V(0,0)≥V(1,0)–V(0,0) +V(0,1)–V(0,0)
V(1,1)−V(1,0)−(V(1,0) +V(0,0))≥V(1,0)–V(0,0) +V(0,1)–V(0,0)
CV P(1,1)−CV P(1,0)≥CV P(1,0)−CV P(0,1)
CV P(1,1)≥CV P(0,1)
This condition implies that the criterion for connections on different platforms to be comple-
mentary in our data is for CVP for the combination of connections to be higher than for a single
connection alone. As is seen in Figure 2C (and Table S62) this is the case for the connections
of each platform and being connected on at least one other platform (all differences significant
atα=.00001level).
However, this analysis faces a major limitation. Connections are not randomly assigned
but rather endogenously chosen by users. Therefore, omitted variables may bias our findings.
30

Table S2: Rank concentration by relationship type.
How ego knows alter Relative age Other platform
Online None K–12 Work Interest College Family Same Younger Older Yes No
P(R2/∈c|R1∈c)0.580 0.793 0.667 0.644 0.716 0.678 0.450 0.457 0.586 0.528 0.120 0.487
P(top2⊆c)0.0357 0.0064 0.0357 0.0668 0.0380 0.0423 0.2277 0.2514 0.0986 0.1449 0.7480 0.0963
P(top4⊆c)0.0204 0.0020 0.0122 0.0191 0.0093 0.0130 0.1189 0.1065 0.0291 0.0510 0.6253 0.0597
P(top8⊆c)0.0018 0.0002 0.0020 0.0061 0.0012 0.0033 0.0369 0.0292 0.0045 0.0145 0.7019 0.0049
Correlational analysis can only be suggestive, although controlling for observable covariates
may help (50).
Another barrier to this interpretation arises from ambiguity in how we solicited connection
valuations. Note that we do not give detailed instructions to survey takers about what is meant
by “most valued.” Interpreting these results as informative about the nature of connection com-
plementarity across platforms requires interpreting importance as marginal value. However,
some respondents may have taken a portfolio approach to ranking connections, with their top
4 ranks, for example, corresponding to their preferred team of four connections rather than
indicating individual preferences.
To investigate this point further, we examined the extent to which certain connection types
co-occur in rankings. If participants tend to list many friends of the same type at the top of
their rankings, this is in tension with the portfolio hypothesis. On the other hand, if participants
always have a diverse mix of connections in their top 4, this would suggest a portfolio strategy.
The table below lists 4 ranking co-occurrence measures for 12 focal characteristics. The first
row reports the probability of having a different category 2nd ranked connection conditional on
a given first ranked connection. The remaining rows give the probability of all top N friends
being in the same category.7
On balance, the table should move us substantially away from the view that a portfolio
7The top 8 ranking restricts attention to only participants who ranked all 8 possible friends, creating a slightly
different denominator.
31

motive governs the rankings. A community-following logic implies that respondents diversify
across groups after only a slot or two, so that concentration at the top of the ranking should de-
cay quickly and, crucially, should do so without regard to how valuable a category is. Instead,
attributes that earn the highest Connection Value Percentile—cross-platform ties, family, and
same-age peers—accumulate at the very top (e.g., over half of people who rank a family con-
nection as their top connection list another family connection as their second most valued, and
88% of egos whose top connection is cross-platform also rank a second cross-platform connec-
tion next). Summing across the ‘How ego knows alter’ columns, over 19% of respondents list
their top 4 connections as all being from the same connection type. Portfolio behavior cannot
easily generate this pattern. We therefore regard a portfolio motive as, at most, a second-order
influence on the rankings rather than their organizing principle—though, because observable
attributes are imperfect proxies for the latent communities a respondent might have in mind, we
treat this as suggestive rather than decisive evidence.
To our knowledge, no previous paper has attempted to estimate whether connections across
platforms are complementary. However, a pair of papers have been able to harness experiments
to measure the complementarity of different digital messaging systems. Collis and Eggers (51)
conducted an RCT of university students in which half were randomly assigned to a large
restriction on their use of Facebook, Instagram and Snapchat. Those in the treatment group
dramatically increased their usage of WhatsApp. The authors take this as evidence of strong
substitutability between WhatsApp and the bundle of social media platforms. Aridor (52) exper-
imentally varied participant’s phone access to Instagram and YouTube. The author found that
participants’ increased their usage of several other digital products as well as their time spent in
non-digital activities. Neither of these papers speaks to the question of complementarity of spe-
cific connections across platforms. While identifying complementarity or substitution across
platforms is not our primary objective, our work nonetheless provides suggestive evidence that
32

these platforms are complements not substitutes.
S3 Results
S3.1 Wave 1
In Table S4, we present summary statistics on age, gender, ethnicity, income, and political ori-
entation for our Wave 1 sample. At the bottom of Table S4, we report the average, median
and standard deviation of the self-reported share of connection value that comes from the top-
four connections on each platform. Consistent with later results, these results suggest strong
heterogeneity in connection value, with the top four connections being valued disproportion-
ately. Also interesting is that the share of value coming from the top four platforms is lowest
for LinkedIn. This is consistent with LinkedIn being valued for introducing a large number of
weak-ties for job searching.
None of the platforms we studied release official statistics on the demographics of its US
users. This makes comparison of our summary statistics to the platforms’ true user bases chal-
lenging. However, there are two general surveys of social media usage that allow us to construct
comparable estimates of the shares of platform users by demographic.
The first social media survey we compare to our sample is the 2020-2022 ANES Social
Media Study (53). This is a three-wave panel survey conducted online. Data collection was
carried out by NORC at the University of Chicago, supported by funding from Facebook and
the National Science Foundation. The sample included U.S. citizens aged 18 and older and
achieved a 3.2% response rate in the initial wave. In the third wave of their survey, conducted
from November 9, 2022, to January 2, 2023, the instrument asked whether respondents were
current users of three of the social media platforms we studied. ANES makes the micro-data
of the survey responses available, which we used to calculate platform participation rates by
demographic. We combined these usage rates from US Census (54) data on the demographics of
33

US persons to estimate shares of users by demographic for each platform. We estimated a 95%
confidence interval for each platform’s demographics by using the total number of respondents
for questions regarding platform usage as the sample size.
The second general survey to which we compare our sample is a 2023 survey conducted by
Pew on social media usage (55). The survey was conducted between May 19 and September
5, 2023, with a total of 5,733 respondents (2,217 online and 3,516 via paper). Participants
were recruited through mailed invitations, employing address-based sampling, with materials
provided in English and Spanish. To encourage participation, households received an initial
incentive and respondents who completed the survey were later sent a $10 post-completion
incentive. The microdata on responses is not made available by Pew, but they do provide cross-
tabulation results on the share of individuals of each demographic who use each of the platforms
we studied. We combined these estimates with the same US Census data described above to
create platform-level demographic share estimates. In calculating confidence intervals for this
estimate, we used the Pew provided 95% confidence interval for the full sample.
The resulting estimates of platform demographic shares from ANES, Pew, and our sample
are reported in Table S3. ANES did not ask about LinkedIn usage, so those columns are empty.
Table S3: Percent of Users by Demographic Characteristic on Each Platform: PEW 2023 Esti-
mated, ANES 2022 Estimated, and this Study Sample.
Facebook Instagram LinkedIn X
Pew* ANES* Our Sample Pew* ANES* Our Sample Pew* ANES* Our Sample Pew* ANES* Our Sample
Val CI† Val CI** Val CI** Val CI† Val CI** Val CI** Val CI† Val CI** Val CI** Val CI† Val CI** Val CI**
Men (%) 43±1.846±1.647±1.241±1.841±1.639±1.451±1.8– – 46±1.657±1.859±1.653±1.4
White (%) 76±1.874±1.471±1.169±1.867±1.561±1.475±1.8– – 68±1.568±1.872±1.564±1.3
65+ (%) 15±1.814±1.17±0.66±1.87±0.86±0.77±1.8– – 10±1.05±1.89±0.95±0.6
Note:*Estimated US User Demographics based on Pew data or American National Election Studies (ANES) data.
Note:**95% confidence interval
Note:†95% confidence interval for full sample as reported by Pew.
As can be seen, there is broad agreement between the different samples in the demographic
breakdown of platforms. For example, Facebook is the whitest platform in both the survey
estimates and in our surveys, and LinkedIn is whiter than Instagram and X. Across the sources,
34

there is agreement on X being relatively male, and Facebook having more older users than X.
However, the sources are not in perfect agreement. Comparing Pew to ANES, four of nine
estimates are significantly different at the 95% level. Comparing our sample to ANES, seven of
nine estimates are significantly different at the 95% level. Comparing our sample to Pew, eight
of twelve estimates are significantly different at the 95% level.
We think these small but significantly detectable differences arise for several reasons. First,
our studies were conducted in different time periods, and participation rates by demographic
groups are known to change over time. Second, the ANES study is focused on US citizens,
while Pew and our estimates are based on US persons and are not restricted to US citizens.
Third, Pew made a special effort to include Spanish language materials, while ANES and our
study did not. Fourth, there are differences in the wordings of the survey questions used, in
how they solicit both demographics and current platform usage, across the studies. Finally,
our confidence intervals for the Pew and ANES studies may be overly narrow, as we naively
use the Pew stated confidence intervals, and for both ANES and Pew do not make additional
adjustments for the fact that estimating user shares involves combining the survey data with
estimates of US population shares. Overall, the broad agreement of our sample with available
surveys, despite differences in their sampling methods and time periods, gives us confidence in
the generalizability of our findings.
S3.1.1 Connection Value Percentile by Dyadic Characteristics
We measured the effect of dyadic attributes on the connection value percentage (CVP) by esti-
mating the conditional average CVP for different subpopulations to identify significant differ-
ences. Formally, we evaluated the conditional expectation and 95% confidence intervals for
E[CV Pi,j,p|Ai,j,p =A](S2)
35

Table S4: Summary Statistics for Wave 1.
FACEBOOK INSTAGRAM LINKEDIN X
N % N % N % N %
4149 1981 1499 2899
Gender
– Female 2181 53% 1424 72% 853 57% 1236 43%
– Male 1951 47% 543 27% 637 42% 1641 57%
– Other 17 0% 14 1% 8 1% 22 1%
Age Bin
– 18-24 years old 646 16% 587 30% 239 16% 520 18%
– 25-34 years old 1396 34% 713 36% 489 33% 1048 36%
– 35-44 years old 1310 32% 388 20% 436 29% 1050 36%
– 45 years or older 790 18% 278 14% 333 22% 277 10%
Ethnicity
– White 2952 71% 1189 60% 1014 68% 1873 65%
– Black or African American 573 14% 354 18% 227 15% 534 18%
– Hispanic or Latino 387 9% 278 14% 150 10% 317 11%
– Asian / Pacific Islander 159 4% 100 5% 66 4% 106 4%
– Nat. American or Am. Indian 36 1% 19 1% 14 1% 33 1%
– Other 42 1% 41 2% 27 2% 36 1%
Income
– Less than $100,000 2859 69% 1673 84% 1119 75% 1655 57%
– $100,000 or more 1290 31% 308 16% 379 25% 1244 43%
Political Orientation
– Liberal 1403 34% 541 28% 435 29% 1140 39%
– Moderate 2000 48% 1150 59% 846 56% 1290 44%
– Conservative 746 18% 270 14% 217 14% 469 16%
Top 4 Connection Value (Self-reported %)
– Mean 53.2 44.9 43.4 55.7
– Median 53 44 40 59
– SD 31.1 31.7 32.1 30.7
36

whereAis some dyadic attribute that an ego-alter pair could have (for example, the ego and
alter are both male), where the indexesi, j, krefer to the connectioni, jon platformp.
In the main text of the paper we present the most important findings of this analysis in Fig-
ures 2 and 3. Across types of connections, one strong and consistent result is that connections
between individuals that are “closer” tend to create more platform value. Across all platforms,
connections seen more frequently and in more intimate relationships (e.g. family and school
friends) are more valued than connections seen infrequently and in less intimate relationships
(e.g. shared interest groups and those only known online). Those who are connected to the
ego on multiple platforms also have higher CVP, suggesting that the negative effect of having
alternative modes of communication on focal platform CVP is small, relative to the effect of
closer contacts being more valued on all platforms. This result is consistent with the hypothe-
sis that Myspace was eventually surpassed by Facebook because the latter focused on creating
higher-value college friend connections, while the former fostered looser shared-interest con-
nections (56). Close contacts and family members are especially highly valued on Facebook,
and there is a preference for same-race contacts on average.
S3.1.2 Imputing Monetary Value for Connection Characteristics
The Connection Value Percentile (CVP) analysis in the previous section documents which
dyadic attributes are associated with higher within-ego ranks, but it does so attribute-by-attribute
and on an ordinal scale. To complement that evidence, this subsection imputes a marginal
monthly dollar value for each connection characteristic, jointly estimated, by combining the
Wave 1 ranking task with the platform-level estimates of total platform value (TPV) and the
share of platform value attributable to local network effects (SPV) developed in the main text.
The procedure has two steps.
37

Step 1: Rank-ordered (exploded) logit on the pooled Wave 1 sample.We treat each ego’s
eight-alter ranking as the source of a sequence of choice events—the top alter chosen from
eight, the second from the remaining seven, and so on—and estimate a rank-ordered (exploded)
logit8 on the resulting data, pooling across the four platforms (57). Lettinguija denote the latent
value to egoion platformpof an alterawith characteristicsX ija, we model
uija =X ija β+η ip +ε ija,(S3)
whereη ip is an ego×ranking-stage stratum effect andε ija is i.i.d. Type-I extreme value, so
that the probability of observing a given complete ranking is the product of conditional logit
probabilities over successive choice sets. The covariates inXare the dyadic attributes solicited
in Wave 1: how the ego knows the alter, face-to-face contact frequency, whether the pair is also
connected on a second platform, and three same/different indicators (same race, same age, same
gender). Also included as covariates in the regression are alter gender and race directly. For
each characteristic category, the omitted baseline is the lowest-ranked level in the dyadic CVP
analysis. The results of this logit regression are reported in Table S5 in the form of odds ratios
on being ranked above an alternative connection.
Step 2: Anchoring rank utilities to monthly dollars.Step 1 identifiesβonly up to scale.
To convert utility into dollars, we anchor the average value of a random alter on platformpto
its implied per-connection contribution to local network value. Writing ¯Np for the platform-p
average count of connections, the per-connection anchor is
¯Vp = SPVp ·TPV p ¯Np ,(S4)
i.e., the share of mean monthly platform value attributable to local network effects, divided
across the typical user’s connections. Our identifying assumption is that ¯Vp equals the average
8“Exploded” following Beggs et al. (57) means a complete ranking ofKalternatives is rewritten asK−1
stacked conditional-logit choices, with successively smaller choice sets at each stage.
38

monthly dollar value, on platformp, of arandomconnection in our Wave 1 design—specifically,
the four alters that each ego reported after the four closest connections (the four top-of-mind
connections). We exclude the closest-four alters from this anchoring because they are by con-
struction atypically valuable. Combined with the additional normalization that an alter in the
omitted baseline category of every block is worth $0 per month, equation (4) pins down the
dollars-per-utile conversion on each platform. We compute the sample mean ofX ija ˆβacross
the four random alters per ego on platformp, set this equal to ¯Vp, and rescale ˆβaccordingly. Ap-
plying the resulting platform-specific scaling to each element of ˆβyields the marginal monthly
dollar values reported in Table S6.
Results.Table S6 reports the imputed monthly dollar value of each characteristic, by platform.
Before going in to the details of these results, it’s important to highlight an important advantage
of these results over the pure dyadic rankings.
The combined rank-ordered logit speaks to a question that the attribute-by-attribute CVP
analysis cannot resolve. Several of the dyadic attributes we measure are correlated in the data:
family members are seen more often, are more likely to be connected on a second platform,
and are more often of the same race or age as the ego. In principle, the dyadic CVP gradients
documented in Figures 2 and 3 of the main text could have been driven by a single latent
factor—say, relational closeness with family—with the other variables loading on that factor
as proxies. The rank-ordered logit in Table S5 provides evidence against that single-factor
interpretation. Nearly every attribute that entered the CVP gradients positively retains a positive
and statistically significant coefficient when entered jointly. Contact frequency is monotone in
its odds ratio across all five tiers; “family member or family friend,” college connections, and
shared-interest connections retain independent positive coefficients in the “how known” block;
cross-platform connection retains an independent positive coefficient even after conditioning on
39

contact frequency and relational category; and the homophily margins (same race, same age)
survive at conventional significance. It is therefore likely that each of these dimensions identifies
a distinct source of value to the ego, rather than a common latent driver. The exception is that
some of the “how do you know” connection characteristics, namely, “school (K–12),” “work,”
and “none of these” are not statistically distinguishable from the online-only baseline.
Two additional patterns are worth highlighting. First, contact frequency is the strongest pre-
dictor of platform value. An alter the ego lives with is worth roughly four times as much per
month as a non-cohabiting alter seen multiple times per week, and an order of magnitude more
than an alter seen less than four times per year. Among the “how known” categories, family
members and family friends carry a substantially larger premium than college, shared-interest,
work, or K–12 connections. Cross-platform connection contributes a premium comparable
in magnitude to that of a family-or-family-friend connection. Demographic and homophily
characteristics—alter gender and race, same race, same age, same gender—contribute small
but non-zero premia. Second, taking the table as a whole, the premia fall into a clear three-
tier hierarchy by relative importance: contact frequency at the top (with the live-with category
alone exceeding the largest premium in any other block), relational source and cross-platform
connection at an intermediate tier (with family-or-family-friend status and being connected on
a second platform contributing premia of comparable magnitude), and demographic and ho-
mophily characteristics roughly an order of magnitude smaller than the intermediate tier. The
marginal monthly value of a connection on these platforms appears to derive primarily from
the intensity and structural depth of the relationship rather than from demographic matching
between ego and alter.
The dollar values reported in Table S6 are marginal monthly contributions of each attribute
to the value of one additional connection of a given type, conditional on the platform’s per-
connection anchor. Because the typical user has hundreds of connections, the value of adding a
40

characteristic to a single connection is necessarily small in absolute terms. The largest estimates
are on the order of 4 cents a month.
S3.2 Wave 2
In Table S7 we present summary statistics of network characteristics and platform valuation in
each of the platforms used in Wave 2. The average monthly valuation of Facebook is com-
parable to the valuation found in previous research (see Table S8). 9 A calculation estimating
monthly and yearly measures of consumer surplus generated by the four platforms is presented
in Table S9. For monthly consumer surplus estimates, we take the average willingness to accept
valuations to give up these platforms for 1 month and multiply them by their user base in the
US (monthly active users).10 For yearly consumer surplus estimates, we multiply the monthly
estimates by 12. Assuming that platform surplus is linear in the number of months may be an
overestimate however. This is because hyperbolic discounting, rational addiction, or switching
costs could make the willingness-to-pay for a year of Facebook smaller than this calculation
would imply. Indeed, Allcott et al. (37) find some evidence of this. Individuals in their exper-
iment who were paid to deactivate Facebook for a month valued future months of Facebook
usage less.
In Table S10 we present summary statistics on age, gender, ethnicity, income and political
orientation of the sample in Wave 2.
S3.2.1 Predictors of Total Platform Valuation
We implement two sets of models that predict Total Platform Value. The first set predicts
this value with connection counts being included as linear or log-linear predictive terms. This
9We couldn’t find studies estimating valuations for Instagram, LinkedIn, and X on a national scale.
10The sources for monthly active users arehttps://backlinko.com/social-media-users,
https://sproutsocial.com/insights/linkedin-statistics/andhttps://news.
linkedin.com/about-us#Statistics. For linkedIn, we multiply the number of registered users
(230 million) with an estimate of the percentage of users who are active monthly (48.5%).
41

Table S5: First-Stage Rank-Ordered Logit Estimates of Connection Value
Odds Ratio
How known (base: I only know them online)
None of these 1.029
School (K–12) 1.013
Work 1.029
Through shared interest in real life 1.069 ∗∗
College or University 1.068 ∗∗
Family member or family friend 1.298 ∗∗∗
Meeting frequency (base: Never)
Less than 4 times/year 1.325 ∗∗∗
About once a month 1.560 ∗∗∗
About once a week 1.647 ∗∗∗
Multiple times per week 1.850 ∗∗∗
I live with this person 2.719 ∗∗∗
Cross-platform connection (base: Not connected on another platform)
Also connected on another platform 1.262 ∗∗∗
Gender
Alter female (base: alter male) 1.067 ∗∗∗
Ego and alter different gender (base: same gender) 1.024 ∗∗
Age mix (base: ego younger than alter)
Same age as alter 1.054 ∗∗∗
Ego older than alter 1.044 ∗∗
Race
Alter non-white (base: alter white) 1.011
Same race (base: different race) 1.061 ∗∗∗
Observations 230,669
Notes:Rank-ordered exploded logit estimates of a regression of rank on all connection characteristics, pooling
all platforms. The coefficients are exponentiated and reported as odds ratios. An odds ratio greater than one
indicates a higher likelihood of being ranked above an alternative connection within the same stratum, holding
other characteristics constant. Significance: ∗ p <0.10, ∗∗ p <0.05, ∗∗∗ p <0.01.
42

Table S6: Imputed Marginal Dollar Value per Month of an Additional Connection, by Charac-
teristic and Platform
Characteristic Facebook Instagram LinkedIn Twitter
Contact frequency (base: Never)
Live with this person0.0455 0.004 34 0.0345 0.003 89
Multiple times per week0.0280 0.002 67 0.0212 0.002 40
About once a week0.0227 0.002 16 0.0172 0.001 94
About once a month0.0202 0.001 93 0.0153 0.001 73
Less than 4 times/year0.0128 0.001 22 0.009 71 0.001 10
How known (base: I only know them online)
Family member or family friend0.0119 0.001 13 0.009 00 0.001 02
Through shared interest IRL0.003 05 0.000 290 0.002 31 0.000 261
College or University0.002 99 0.000 285 0.002 27 0.000 256
Work0.001 32 0.000 126 0.001 00 0.000 113
None of these0.001 29 0.000 123 0.000 978 0.000 110
School (K–12)0.000 597 0.000 056 8 0.000 452 0.000 051 0
Cross-platform connection (base: Not connected on another platform)
Also connected on another platform0.0106 0.001 01 0.008 03 0.000 906
Alter demographics
Female (base: alter male)0.002 96 0.000 282 0.002 24 0.000 253
Non-white (base: alter white)0.000 486 0.000 046 3 0.000 369 0.000 041 6
Dyadic characteristics
Same race (base: different race)0.002 71 0.000 258 0.002 05 0.000 232
Same age as alter (base: ego younger)0.002 39 0.000 228 0.001 81 0.000 204
Older than alter (base: ego younger)0.001 97 0.000 188 0.001 50 0.000 169
Different gender (base: same gender)0.001 08 0.000 103 0.000 822 0.000 092 7
Notes:Each cell reports the imputed monthly dollar value of a connection to an alter possessing the row charac-
teristic, on the column platform.
43

Table S7: Additional Summary Statistics for Wave 2
FB X IN LK
Average Number of Connections 604.7 302.2
Average Number of Followers 1384 2861.4
Average Number of Followees 648.2 599.4
Average Monthly Valuation 100.9 78.35 91.25 86.85
N2,470 2,238 2,488 2,200
Paper Sample Mean WTA/month Median WTA/month
Allcott et al. (2020) Active Facebook users (>15 mins/ per day) $180 $100
Brynjolfsson et al. (2024) Representative sample of Facebook users N/A $48.53
This paper Facebook users recruited on Lucid $100.90 $100
Table S8: Comparison of Willingness to Accept (WTA) estimates for giving up Facebook for
one month
Platform Mean WTA/month US user base Monthly consumer surplus Yearly consumer surplus
Facebook $100.90 177.5 million $17.9 Billion $214.9 Billion
Instagram $91.25 138.5 million $12.6 Billion $151.7 Billion
X $86.85 50.5 million $4.4 Billion $52.6 Billion
LinkedIn $78.35 111.5 million $8.7 Billion $104.9 Billion
Table S9: Monthly and annual estimates of consumer surplus generated by the platforms
44

Table S10: Summary Statistics for Wave 2
Facebook Instagram LinkedIn X
N % N % N % N %
2470 2488 2200 2237
gender
– Female 1301 53% 1259 51% 1128 51% 1132 51%
– Male 1158 47% 1222 49% 1065 48% 1097 49%
– Other 11 0% 7 0% 7 0% 8 0%
Age
– 18-24 years old 406 16% 399 16% 312 14% 331 15%
– 25-34 years old 538 22% 429 17% 299 14% 388 17%
– 35-44 years old 412 17% 504 20% 443 20% 466 21%
– 45 years or older 1111 45% 1153 46% 1145 52% 1050 47%
Ethnicity
– White 1762 71% 1534 62% 1497 68% 1432 64%
– Black or African American 421 17% 417 17% 352 16% 438 20%
– Hispanic or Latino 180 7% 318 13% 173 8% 235 11%
– Asian or Pacific Islander 72 3% 119 5% 114 5% 84 4%
– Nat. American or Am. Indian 18 1% 28 1% 26 1% 21 1%
– Other 17 1% 72 3% 38 2% 27 1%
Income
– Less than $100,000 925 37% 1111 45% 935 43% 895 40%
– $100,000 or more 1545 63% 1377 55% 1265 57% 1342 60%
Political Orientation
– Liberal 568 23% 519 21% 523 24% 515 23%
– Moderate 1479 60% 1512 61% 1243 56% 1306 58%
– Conservative 423 17% 457 18% 434 20% 416 19%
Total Platform Valuation
Median 100 100 90 70
Mean 101 91.3 86.8 78.4
SD 60.5 58.5 59.4 58.7
45

approach is atheoretical, and the specifications were pre-registered.
After describing these specifications and results, we discuss a theoretically motivated model
of Total Platform Value used to estimate the Share of Platform Value created by local network
effects, which is reported in the manuscript Figure 1b.
S3.2.2 Pre-registered Models Total Platform Value
For Wave 2 we report all pre-registered analysis as published at:
https://www.socialscienceregistry.org/trials/12300.
The first set of results are on the predictors of Total Platform Valuation. In Tables S12 to S17
we present OLS results where monthly Total Platform Valuation is explained by the number of
connections on the platform. They are estimated using variations on the following equation:
Vi =β 1Ci +β 2χ+α(S5)
WhereVis Total Platform Valuation,C i is some measure of the number of connections the ego
has on the platform, andαis an intercept term.χcorresponds to a vector of controls, which
varies by specification. Regressions are run separately for each platform. We are primarily
interested in the coefficientβ 1, which estimates the relationship between platform value and
connection count. We are also interested in the predictors ofV i, as well as the predictability of
Vi overall.
The main econometric challenge in interpreting these results is the possibility of omitted
variables bias. As we do not have experimental variation in the number of contacts for each
consumer, these correlations should not necessarily be interpreted as causal. Popularity in the
real world is one example of a problematic omitted variable. Plausibly, individuals who are
more popular in the real world will find it easier to accumulate contacts online. But it may also
be that these popular people have a higher opportunity cost of their time, and therefore value
46

social media less. This omitted variable could bias the magnitude of the effect of contacts on
platform value downwards.
The interpretation of these results also faces two other econometric challenges. First, we do
not know the exact functional form of the relationship between connection count and platform
value—whether it is linear, log-linear, or something else. Second is the role that anchoring may
play in setting ego’s Total Platform Valuations. Our pre-registration therefore calls for estimat-
ing several different functional forms, as well as possible interaction terms and controlling for
different potential confounders.
Our baseline preregistered specification is reported in Table S13. In this specification, Total
Platform Valuation is explained by the log of the number of connections, for each platform. For
platforms where connections are split by followers and followees, we have three specifications:
one with each type of connection included individually, and ones where both types of connec-
tion are included. This table shows significant positive relationships between overall contacts
and the log of follower count on all platforms. The effects are largest for Facebook connections,
with a doubling of connection count associated with a $5.04 increase in total valuation. For plat-
forms where followers and followees are split, including either predictor alone leads to a strong
and significant correlation between the logged connection count and Total Platform Valuation.
However, for both X and Instagram, when both connection types are included, followers is the
predictor that has a larger and more significant positive point estimate.
Next, S12 estimates the effect of the count of connections rather than their logarithm. The
effect of total connections on monthly platform value remains positive and significant, except
on X. In Tables S14 through S17, we report the estimated effect of log connection counts
on platform value with a variety of additional controls. For Facebook and LinkedIn, the first
specification adds controls for ego characteristics. The second column includes controls for the
maximum platform value users were allowed to report—this is meant to investigate and account
47

for possible anchoring effects. The final column includes both previous sets of controls, as well
as controls for platform usage. Arguably this last set of controls is over-controlling, as platform
value and platform usage intensity may both be positively caused by the number of platform
contacts.
Even with this wide battery of controls, we continue to find positive and highly significant
relationships between the number of platform connections and platform value. While adding
platform usage controls does attenuate the size of the effect, adding ego characteristic con-
trols does so only marginally, ameliorating the concern that omitted variables are biasing the
estimates. For X and Instagram we conduct the same exercise, but with six specifications as
we split followers and followees. Similarly, the estimated effect of log connections on Total
Platform Valuation remains significant and positive, regardless of which controls are added,
although platform usage controls attenuate the effect more. The robustness of the correlation
leads us to strongly suspect a positive causal role of connections on platform value, increasing
valuation by between one to six dollars a month for a doubling in connections.
We are also interested in other ego characteristics that are correlated with platform value.
Even if we cannot make causal claims about these relationships, because of omitted variables
concerns, they are suggestive for future research. Figures S3 to S12 report conditional average
Total Platform Valuations for Wave 2 survey respondents in different groups, following the
preregistration. Figure 1 in the main text reports four variations on conditional average total
platform value: by platform time use, political orientation, relationship status, and job seeking
status. These show a positive relationship between time use and platform value. They also show
significantly higher valuations reported by those looking for a job for LinkedIn users, but not
for users of other platforms. Figure 1 also reports the empirical CDF of platform valuations
for all four platforms (panel A) as well as the share of value on each platform imputed to be
due to connections (panel B). Panel B is generated by dividing average platform value by the
48

constant term estimated in a regression of platform value on the number of connections (and an
intercept) in a redundant signal model as reported in Table S22 to calculate the contribution of
other factors, while the remainder is attributed to connections.
In the main text, Figure 4 reports how total platform value varies as a function of feature
use. Panel A reports, for each platform, the coefficients on feature use from a regression of
total platform value as a function of using different platform features. Features found to have a
significant positive effect on platform value on Facebook are using Messenger, positing on the
news feed, and engaging with others’ content on the news feed; on Instagram posting Reels and
posting photos; on LinkedIn using Groups and updating one’s profile; and on X using Spaces
and bookmarking tweets. No feature was associated with a significant negative effect on value.
Figure 4 Panel B reports how platform value varies with feature use and ego income. The
conditional average platform values, for users and non-users of the feature, are plotted for egos
of different income groups. The split for high vs. low income is drawn at one hundred thousand
dollars. S11, Column 1 reports the difference between conditional average total platform value
for high and low income egos who use the feature. P-values for this difference being different
than zero are also reported. Column 2 reports the difference in differences between conditional
average total platform value for high income feature users and non-users minus the difference
between low-income feature users and non-users. This quantity measures the difference in
marginal contributions to total platform value of feature use for high vs. low income egos.
P-values for this difference of differences being different from zero are also reported. These
p-values were calculated by first determining the standard error of this difference using the
standard errors of the individual groups. The t-statistic was obtained by dividing the difference
in differences by its standard error. Finally, the p-value was calculated, conservatively, by using
the t-distribution with degrees of freedom equal to the minimum of the two groups.
All pre-registered figures not appearing in the main text appear here. A few highlight re-
49

Table S11: Summary of total platform value by feature use and ego income group for selected
features.
∆1 =Value (High income & uses feature)−Value (Low income & uses feature)
∆2 = [Value (High income & uses feature)−Value (High income & doesn’t use feature)]−
[Value (Low income & uses feature)−Value (Low income & doesn’t use feature)]
Feature ∆1 (p-value) ∆2 (p-value)
FB Messenger ∆1 =−6.3157(p = 0.02143) ∆2 =−12.23003(p = 0.06125)
Instagram Reels ∆1 =−10.69087(p = 0.00556) ∆2 =−7.48214(p = 0.12209)
LinkedIn Groups ∆1 =−8.70992(p = 0.03359) ∆2 =−11.54328(p = 0.02670)
X Lists ∆1 =−21.05425(p =2.621×10 −5) ∆2 =−27.34639(p =6.176×10 −6)
sults from these figures include that white respondents and women have the strongest relative
preference for Facebook versus the other platforms ( S3 and S4) and that older people have
a higher valuation for all platforms overall, which may be confounded by income ( S5). We
found no significant relationship between introversion, family size, or number of recent moves
and social media willingness-to-pay ( S7, S8, S12). On the other hand, we were able to detect
some significant differences across platforms by relationship status, income, and years on the
platform. Facebook was more valued by married people than single people ( S9); LinkedIn
was more valued by our highest income group than our lowest ( S6); and platform value was
increasing in the number of years spent on the platform, especially for Facebook ( S11).
Tables S18 to S21 report the results of our pre-registered LASSO analysis of the predictors
of monthly platform value for each platform. The purpose of this analysis is to understand how
predictable platform value is overall, and to estimate the most robust predictors of platform
value. We used LASSO, with a lambda penalty selected through cross-fold validation, to select
the most robust predictors. All ego-level characteristics, as well as their two- and three-way
interactions were included as potential predictors. An OLS regression was then run regressing
platform value on all the selected regressors.
For each platform, two to three variations on this analysis were conducted, differing in the
number of candidate predictors and their interactions. In run 1, for LinkedIn and Facebook, pre-
50

dictors from the following five categories were included: connection count, log of connection
count, maximum platform value random group assignment (100, 150 or 200), ego character-
istics11 and digital platform use characteristics 12. This means that up to a five-way interaction
of the above factors was explored. For Instagram and X, this regression was split into two
versions: Run 1 measured connections through number of followers, and run 2 measured con-
nections through the number of followees. Run 2 for LinkedIn and Facebook was parallel to run
3 for X and Instagram. In these runs we excluded platform usage characteristics, including the
number of connections and platform feature use variables because these are more endogenous
than demographic characteristics. The specific predictors and their interactions included maxi-
mum value assignment and ego characteristics (the same list of these as run 1). This means in
run 2 (for Facebook and LinkedIn) and run 3 (for X and Instagram) up to two-way interactions
were explored.
The first thing to note about these results is that a significant portion of the variation in
platform value was explained by our predictors. In the normal OLS regressions (Tables S14
through S17), the specifications with the most predictors explained between .138 (for X) and
.218 (for Facebook) of the variation, based on adjustedR 2s. The LASSO models ( S18 to S21),
for the procedure with the greatest number of predictors, had adjustedR 2 of between .133 (X)
and .254 (Facebook). This predictable heterogeneity provides opportunities for platforms to
third-degree price discriminate and extract a larger share of the surplus from their platforms.
For X, the predictive power of the model using follower count was much greater than the other
two specifications, while for Instagram, the model using the count of followees was slightly
more predictive than the one using followers.
11specifically, the response to any of the following: gender, age, ethnicity, urban/rural status, marital status, num-
ber in household, income, number of moves, looked.for.job, political orientation, and two introversion measuring
questions
12specifically, the response to any of the following: years on platform, platform time use, [list of platform
specific feature use] and use of one of the other main platforms or TikTok or Snapchat
51

The second thing to note about the LASSO models is in the second half of each Table. In
this section, coefficients for several of the selected predictors is reported. Across all platforms,
many interactions of connections/followers with ego and platform use were found to positively
predict platform value. This suggests that connection count is indeed a robust predictor of
platform value. On Facebook, terms that were found, in combination with log of number of
connections, to positively predict platform value included age, assignment to a high valuation
group, and engaging on the news feed. For X it was high value group assignment, age, and
using X for many hours and use of bookmarking. For Instagram and LinkedIn, age and feature
use combined with the log of the number of connections strongly predicted platform value. One
interesting result for Instagram is a large positive estimate of the interaction between log of
followees and Urban status. This is consistent with an Instagram following being more useful
for urban users. Across all platforms, the linear measure of connection count was never included
as a predictor, suggesting our focus on the log of connection count in our main regression is
appropriate. In the final specifications (runs 2 and 3), which do not include platform use, one
robust predictor that appeared across two platforms was the interaction between the maximum
value assignment and Asian ethnicity, suggesting that this group may be particularly sensitive
to anchoring.
52

Table S12: Preregistered OLS regressions of total valuation on number of social media contacts,
Wave 2
Monthly Total Platform Valuation
FB X(1) X(2) IN(1) IN(2) LK
Connections 0.004 ∗∗∗ 0.004∗∗∗
(0.001) (0.001)
Followers−0.00004 0.0002 ∗∗∗
(0.0001) (0.0001)
Followees 0.00000 0.005 ∗∗∗
(0.0002) (0.001)
Constant 98.405 ∗∗∗ 78.401∗∗∗ 78.339∗∗∗ 90.753∗∗∗ 88.335∗∗∗ 85.719∗∗∗
(1.420) (1.245) (1.249) (1.178) (1.353) (1.304)
N2,470 2,238 2,238 2,488 2,488 2,200
R2 0.004 0.0002 0.000 0.005 0.007 0.005
Adj. R2 0.004−0.0002−0.0004 0.004 0.007 0.005
Res. SE 60.349 58.720 58.726 58.320 58.249 59.245
F Statistic 11.061 ∗∗∗ 0.460 0.00003 12.123 ∗∗∗ 18.222∗∗∗ 12.089∗∗∗
Notes: ∗∗∗Significant at the 1 percent level.
∗∗Significant at the 5 percent level.
∗Significant at the 10 percent level.
53

Table S13: Preregistered OLS regressions of total valuation on the log of the number of social
media contacts, Wave 2
Monthly Total Platform Valuation
FB X 1 X 2 X 3 IN 1 IN 2 IN 3 LK
Connection (log) 5.037 ∗∗∗ 4.044∗∗∗
(0.664) (0.584)
Followers (log) 2.707 ∗∗∗ 2.019∗∗∗ 5.077∗∗∗ 4.365∗∗∗
(0.558) (0.764) (0.593) (0.728)
Followees (log) 2.919 ∗∗∗ 1.230 4.355 ∗∗∗ 1.418∗
(0.683) (0.934) (0.691) (0.843)
Constant 74.637 ∗∗∗ 65.993∗∗∗ 63.835∗∗∗ 63.014∗∗∗ 64.138∗∗∗ 68.101∗∗∗ 60.402∗∗∗ 71.590∗∗∗
(3.659) (2.830) (3.614) (3.622) (3.371) (3.853) (4.036) (2.533)
N2,470 2,237 2,237 2,237 2,488 2,488 2,488 2,200
R2 0.023 0.010 0.008 0.011 0.029 0.016 0.030 0.021
Adjusted R2 0.022 0.010 0.008 0.010 0.028 0.015 0.029 0.021
Res. Std. Error 59.791 58.429 58.498 58.419 57.618 58.000 57.597 58.769
F Statistic 57.551 ∗∗∗ 23.573∗∗∗ 18.280∗∗∗ 12.658∗∗∗ 73.317∗∗∗ 39.730∗∗∗ 38.100∗∗∗ 48.027∗∗∗
Notes: ∗∗∗Significant at the 1 percent level.
∗∗Significant at the 5 percent level.
∗Significant at the 10 percent level.
54

Table S14:Facebook: Preregistered OLS regressions of total valuation on the number of
social media contacts and other controls, Wave 2
Monthly Facebook Valuation
1b(i) 1b(ii) 1b(iii)
Facebook connection count (log) 5.520 ∗∗∗ 5.340∗∗∗ 3.620∗∗∗
group assignment 100usd – –
group assignment 150usd 28.329 ∗∗∗ 28.842∗∗∗
group assignment 200usd 54.161 ∗∗∗ 54.037∗∗∗
Female – –
Male−6.266 ∗∗ −5.048∗∗
Other−15.338−4.835
Age 0.621 ∗∗∗ 0.573∗∗∗
White – –
Asian or Pacific Islander 4.082 5.351
Black or African American 1.898 2.449
Hispanic or Latino 0.418 0.911
Native American or American Indian 15.086 13.759
Other 27.861 ∗ 24.923∗
Rural – –
Urban−1.214 2.332
Single, not looking for a relationship – –
In a serious relationship−0.293−3.871
Married or domestic partnership 5.134 2.116
Prefer not to say 5.168 7.863
Single, looking for a relationship 4.848 2.153
household of 1 – –
household of 2 2.032 3.673
household of 3 0.502 0.674
household of 4 4.036 4.570
household of 5 10.059 ∗ 8.502∗
household of 6 3.605 5.952
household of 7 or more 0.489 0.814
less than 25K dollars – –
25K to 50K dollars−1.240 2.631
50K to 100K dollars−2.549−0.733
100K to 150K dollars−3.578−2.356
150K dollars or more−6.546 ∗ −4.134
moved 1 or less times – –
moved 2 times−1.194 1.209
moved 3 times−1.108 0.470
moved 4 times−2.900 1.714
moved 5 times or more 1.402 1.267
looked for job: No, and I have not looked in the past year – –
looked for job: No, but I looked for a job in the past year−1.070−2.678
looked for job: Yes−4.331−4.966 ∗
Extremely Liberal – –
Liberal 1.381 2.836
Slightly liberal 2.615 1.327
Moderate−2.439−1.662
Slightly conservative 6.579 7.263 ∗
Conservative−6.214−3.720
Extremely conservative−5.234 1.464
introvert 1: Strongly agree – –
introvert 1: Neither agree nor disagree−4.331−3.911
introvert 1: Somewhat agree−2.068−2.863
introvert 1: Somewhat disagree−3.639−4.746
introvert 1: Strongly disagree 2.658 1.941
introvert 2: Strongly disagree – –
introvert 2: Neither agree nor disagree 2.547 2.285
introvert 2: Somewhat agree 0.178 0.215
introvert 2: Somewhat disagree−3.708−0.695
introvert 2: Strongly agree−4.901−4.727
Years on the platform 0.211
FB usage: less than 10 minutes per day –
FB usage: 10–30 minutes per day 27.343 ∗∗∗
FB usage: 31–60 minutes per day 12.078 ∗∗∗
FB usage: 1–2 hours per day 27.752 ∗∗∗
FB usage: 2–3 hours per day 15.122 ∗∗∗
FB usage: More than 3 hours per day 30.343 ∗∗∗
Playing games −1.730
Marketplace −0.700
Organize attend events 0.806
Engaging with content from your connections on news feed 4.107
Joining groups 1.022
Messenger 7.492∗∗
Facebook Live 3.041
Posting content on your news feed 2.213
Instagram −1.219
X −1.873
LinkedIn −5.149∗
TikTok −1.558
Snapchat −1.832
Constant 50.324 ∗∗∗ 45.487∗∗∗ 2.244
N2,428 2,470 2,428
R2 0.072 0.157 0.239
Adj. R2 0.055 0.156 0.218
Res. SE 58.907 55.570 53.573
F Statistic 4.205 ∗∗∗ 152.575∗∗∗ 11.429∗∗∗
* (p<0.10), ** (p<0.05), *** (p<0.01)
55

Table S15:X: Preregistered OLS regressions of total valuation on the number of social
media contacts and other controls, Wave 2
Monthly X Valuation
1b(i) 1b(i) 1b(ii) 1b(ii) 1b(iii) 1b(iii)
X Followers count (log) 2.814 ∗∗∗ 2.771∗∗∗ 1.597∗∗∗
X Followees count (log) 3.132 ∗∗∗ 2.857∗∗∗ 1.509∗∗
group assignment 100usd – – – –
group assignment 150usd 18.798 ∗∗∗ 18.272∗∗∗ 18.478∗∗∗ 18.267∗∗∗
group assignment 200usd 36.802 ∗∗∗ 36.575∗∗∗ 37.910∗∗∗ 37.762∗∗∗
Female – – – –
Male 2.159 2.455 0.197 0.239
Other−16.620−17.015−17.595−18.025
Age 0.474 ∗∗∗ 0.454∗∗∗ 0.620∗∗∗ 0.618∗∗∗
White – – – –
Asian or Pacific Islander 7.076 6.888 3.736 3.580
Black or African American 2.837 4.065 0.984 1.542
Hispanic or Latino 14.878 ∗∗∗ 14.781∗∗∗ 13.060∗∗∗ 13.045∗∗∗
Native American or American Indian 31.015 ∗∗ 30.779∗∗ 27.957∗∗ 27.934∗∗
Other 7.643 7.027 3.401 3.089
Rural – – – –
Urban 3.070 3.954 1.401 1.864
Single, not looking for a relationship – – – –
In a serious relationship−5.350−5.016−2.844−2.719
Married or domestic partnership−0.521 0.152 0.438 0.649
Prefer not to say 10.988 11.731 9.828 10.267
Single, looking for a relationship−3.064−2.701−3.132−3.046
household of 1 or less – – – –
household of 2−2.783−3.233−3.717−3.995
household of 3 5.211 5.265 4.683 4.625
household of 4 2.434 2.355 0.782 0.573
household of 5−0.895−1.098−4.455−4.681
household of 6−0.373−0.412−3.483−3.589
household of 7 or more−12.837−14.271−17.933 ∗∗ −18.786∗∗
less than 25K dollars – – – –
25K to 50K dollars−5.378−5.057−6.390−6.342
50K to 100K dollars−5.202−4.447−4.747−4.388
100K to 150K dollars−3.758−2.851−4.658−4.212
150K dollars or more−2.325−1.638−3.716−3.378
moved 1 or less times – – – –
moved 2 times−1.533−1.676−2.484−2.642
moved 3 times 0.691 0.412−1.564−1.852
moved 4 times−8.535 ∗ −8.538∗ −5.377−5.366
moved 5 times or more 3.923 4.465 3.823 4.049
looked for job: No, and I have not looked in the p. year – – – –
looked for job: No, but I looked for a job in the p. year−1.361−0.955−0.981−0.816
looked for job: Yes 0.016 0.371 1.306 1.415
Extremely Liberal – – – –
Liberal 10.282 ∗ 9.681∗ 10.321∗∗ 10.085∗
Slightly liberal 16.424 ∗∗∗ 16.692∗∗∗ 16.847∗∗∗ 17.044∗∗∗
Moderate 6.008 5.626 3.560 3.479
Slightly conservative 11.074 ∗∗ 11.470∗∗ 10.238∗∗ 10.532∗∗
Conservative 2.038 1.794 0.217 0.137
Extremely conservative−0.470−0.847−2.920−2.927
introvert 1: Strongly agree – – – –
introvert 1: Neither agree nor disagree−1.240−0.847 1.358 1.651
introvert 1: Somewhat agree−6.879−7.425 ∗ −2.511−2.680
introvert 1: Somewhat disagree−5.581−6.186−2.284−2.521
introvert 1: Strongly disagree−3.463−3.792 1.182 1.074
introvert 2: Strongly disagree – – – –
introvert 2: Neither agree nor disagree−8.278 ∗ −7.400−7.167−6.669
introvert 2: Somewhat agree−8.284 ∗ −7.317−8.804 ∗∗ −8.385∗
introvert 2: Somewhat disagree−9.212 ∗ −8.835∗ −8.724∗ −8.508∗
introvert 2: Strongly agree 3.321 5.202−0.692 0.022
Years on the platform 0.263 0.274
X usage: less than 10 minutes per day – –
X usage: 10–30 minutes per day 21.653 ∗∗∗ 22.129∗∗∗
X usage: 31–60 minutes per day 8.203 ∗∗ 8.366∗∗
X usage: 1–2 hours per day 25.595∗∗∗ 26.063∗∗∗
X usage: 2–3 hours per day 19.986∗∗∗ 20.043∗∗∗
X usage: More than 3 hours per day 34.628 ∗∗∗ 35.155∗∗∗
Post tweets −1.344−0.752
Like reply retweet tweets 6.281∗∗ 5.732∗
Direct messages 4.161 4.256
Bookmark tweets 7.449∗∗∗ 7.524∗∗∗
X lists −3.201−2.949
X Blue Premium −0.336 0.841
Spaces 3.981 4.382
Facebook −7.430∗∗ −7.448∗∗
Instagram 0.457 0.516
LinkedIn −5.024∗ −4.962∗
TikTok 0.207 0.314
Snapchat −3.872−3.602
Constant 46.123 ∗∗∗ 41.483∗∗∗ 47.278∗∗∗ 45.965∗∗∗ 14.271 12.263
N2,187 2,187 2,237 2,237 2,187 2,187
R2 0.059 0.057 0.076 0.073 0.164 0.163
Adj. R2 0.039 0.038 0.075 0.072 0.138 0.138
Res. SE 57.560 57.601 56.483 56.579 54.507 54.536
F Statistic 3.028 ∗∗∗ 2.954∗∗∗ 61.307∗∗∗ 58.569∗∗∗ 6.488∗∗∗ 6.446∗∗∗
* (p<0.10), ** (p<0.05), *** (p<0.01)
56

Table S16:Instagram: Preregistered OLS regressions of total valuation on the number of
social media contacts and other controls, Wave 2
Monthly Instagram Valuation
1b(i) 1b(i) 1b(ii) 1b(ii) 1b(iii) 1b(iii)
Insta Followers count (log) 4.909 ∗∗∗ 5.091∗∗∗ 3.194∗∗∗
Insta Followees count (log) 4.814 ∗∗∗ 4.525∗∗∗ 2.980∗∗∗
group assignment: 100usd – – – –
group assignment: 150usd 26.657 ∗∗∗ 26.906∗∗∗ 25.235∗∗∗ 25.367∗∗∗
group assignment: 200usd 42.664 ∗∗∗ 42.910∗∗∗ 42.154∗∗∗ 42.398∗∗∗
Female – – – –
Male−0.804 0.472 0.231 0.921
Other−27.079−29.132−22.461−23.606
Age 0.345 ∗∗∗ 0.327∗∗∗ 0.446∗∗∗ 0.448∗∗∗
White – – – –
Asian or Pacific Islander 15.464 ∗∗∗ 15.762∗∗∗ 12.807∗∗ 12.770∗∗
Black or African American 17.519 ∗∗∗ 18.711∗∗∗ 12.950∗∗∗ 13.434∗∗∗
Hispanic or Latino 12.938 ∗∗∗ 13.767∗∗∗ 7.799∗∗ 8.078∗∗
Native American or American Indian 15.374 14.478 14.632 14.265
Other 7.333 21.084 ∗∗∗ 5.844 13.448 ∗
Rural – – – –
Urban 10.055 ∗∗ 10.190∗∗ 6.831 6.831
Single, not looking for a relationship – – – –
In a serious relationship 1.052 2.176 0.432 1.080
Married or domestic partnership 0.042 1.335−1.070−0.358
Prefer not to say−3.997−4.567−4.570−4.547
Single, looking for a relationship−2.424−1.852−2.976−2.635
household of 1 or less – – – –
household of 2−2.625−3.713−2.249−2.960
household of 3−7.436 ∗ −8.139∗ −8.292∗∗ −8.804∗∗
household of 4−4.356−4.463−4.779−5.036
household of 5−0.681 1.141−1.356−0.622
household of 6 3.864 1.105 2.216 0.466
household of 7 or more 1.956 2.377−2.629−2.572
less than 25K dollars – – – –
25K to 50K dollars−7.944−7.372−8.802 ∗ −8.370∗
50K to 100K dollars 5.016 7.176 1.387 2.620
100K to 150K dollars−5.988−5.614−7.384 ∗ −7.094∗
150K dollars or more−7.843 ∗ −8.031∗ −8.484∗∗ −8.512∗∗
moved 1 or less times – – – –
moved 2 times 1.226 1.398 0.079 0.191
moved 3 times−0.106 0.982−0.318 0.229
moved 4 times−4.367−3.664−6.582−6.147
moved 5 times or more 4.909 4.615 0.529 0.382
looked for job: No, and I have not looked in the p, year – – – –
looked for job: No, but I looked for a job in the p, year−0.056 0.556−0.032 0.120
looked for job: Yes−3.113−1.473−4.662−3.977
Extremely Liberal – – – –
Liberal 5.408 3.875 6.087 5.377
Slightly liberal 3.521 3.205 2.630 2.379
Moderate 3.750 2.762 2.522 2.096
Slightly conservative 6.733 6.285 4.935 4.836
Conservative 7.117 5.750 6.765 6.220
Extremely conservative−1.067−2.322−0.920−1.403
introvert 1: Strongly agree – – – –
introvert 1: Neither agree nor disagree 0.880 0.560 0.156 0.134
introvert 1: Somewhat agree−0.192−0.178−0.220 0.012
introvert 1: Somewhat disagree 0.117−0.779−0.576−0.915
introvert 1: Strongly disagree−1.200−0.377−1.235−0.564
introvert 2: Strongly disagree – – – –
introvert 2: Neither agree nor disagree−0.928 0.708−2.681−1.728
introvert 2: Somewhat agree−1.246 1.136−3.478−2.140
introvert 2: Somewhat disagree−0.394 1.158−1.782−0.820
introvert 2: Strongly agree 2.740 5.235−0.214 1.043
Years on the platform 0.927∗∗∗ 0.891∗∗∗
Insta usage: less than 10 minutes per day – –
Insta usage: 10–30 minutes per day 29.321 ∗∗∗ 28.639∗∗∗
Insta usage: 31–60 minutes per day 16.881 ∗∗∗ 16.727∗∗∗
Insta usage: 1–2 hours per day 27.682∗∗∗ 27.114∗∗∗
Insta usage: 2–3 hours per day 23.629∗∗∗ 23.085∗∗∗
Insta usage: More than 3 hours per day 41.358 ∗∗∗ 42.072∗∗∗
Post photos as a post 4.971∗ 5.170∗
Like and comment on posts −2.607−3.043
Post Instagram reels 8.417∗∗∗ 8.973∗∗∗
Like and comment on reels −0.581−0.768
Post Instagram stories 1.127 1.891
Like and comment on stories −0.159−0.595
Direct messages 1.420 1.229
Instagram live −7.306∗∗ −5.896∗∗
Facebook 1.153 0.141
X 0.163−0.018
LinkedIn −2.914−2.647
TikTok −1.944−1.153
Snapchat −1.196−0.639
Constant 40.033 ∗∗∗ 37.115∗∗∗ 41.096∗∗∗ 44.066∗∗∗ 3.782 2.807
N2,440 2,440 2,488 2,488 2,440 2,440
R2 0.065 0.061 0.119 0.107 0.195 0.194
Adj. R2 0.048 0.044 0.118 0.106 0.173 0.172
Res. SE 57.127 57.238 54.896 55.263 53.229 53.288
F Statistic 3.785 ∗∗∗ 3.559∗∗∗ 111.822∗∗∗ 99.375∗∗∗ 8.868∗∗∗ 8.768∗∗∗
* (p<0.10), ** (p<0.05), *** (p<0.01)
57

Table S17:LinkedIn: Preregistered OLS regressions of total valuation on the number of
social media contacts and other controls, Wave 2
Monthly LinkedIn Valuation
1b(i) 1b(ii) 1b(iii)
LinkedIn connections count (log) 3.740 ∗∗∗ 4.160∗∗∗ 3.254∗∗∗
group assignment 100usd – –
group assignment: 150usd 19.642 ∗∗∗ 20.184∗∗∗
group assignment: 200usd 46.731 ∗∗∗ 46.366∗∗∗
Female – –
Male−2.981−4.962 ∗∗
Other 35.005 45.208 ∗
Age 0.226 ∗∗ 0.212∗
White – –
Asian or Pacific Islander 21.057 ∗∗∗ 18.401∗∗∗
Black or African American 8.679 ∗∗ 6.392∗
Hispanic or Latino 15.015 ∗∗∗ 11.394∗∗
Native American or American Indian 10.446 6.008
Other 7.901 8.710
(9.800) (9.188)
Rural – –
Urban 6.900 6.520
Single, not looking for a relationship – –
In a serious relationship−11.012 ∗∗ −11.416∗∗∗
Married or domestic partnership−3.354−3.880
Prefer not to say−5.997−1.127
Single, looking for a relationship−10.340 ∗∗ −10.217∗∗∗
household of 1 – –
household of 2−4.260−2.043
household of 3−6.832−3.925
household of 4 0.065 1.171
household of 5−1.261 3.104
household of 6 6.847 7.192
household of 7 or more−4.197 2.063
less than 25K dollars – –
25K to 50K dollars 19.423 ∗∗∗ 15.210∗∗∗
50K to 100K dollars 12.091 ∗∗ 8.922∗
100K to 150K dollars 10.279 ∗∗ 7.049
150K dollars or more 12.204 ∗∗∗ 7.309∗
moved 1 or less times – –
moved 2 times−5.478 ∗ −5.810∗
moved 3 times 1.708 1.399
moved 4 times−4.403−6.269
moved 5 times or more−7.591−7.693 ∗
looked for job: No, and I have not looked in the past year – –
looked for job: No, but I looked for a job in the past year−1.029−3.344
looked for job: Yes 10.337 ∗∗∗ 4.869
Extremely Liberal – –
Liberal 3.288 5.240
Slightly liberal 3.721 5.729
Moderate 2.937 4.302
Slightly conservative 7.673 ∗ 7.344∗
Conservative−2.079 1.293
Extremely conservative−1.805 0.441
introvert 1: Strongly agree – –
introvert 1: Neither agree nor disagree 2.839 3.708
introvert 1: Somewhat agree−3.693−0.903
introvert 1: Somewhat disagree 3.375 5.009
introvert 1: Strongly disagree−0.351−2.667
introvert 2: Strongly disagree – –
introvert 2: Neither agree nor disagree−0.821−0.915
introvert 2: Somewhat agree 2.159 1.089
introvert 2: Somewhat disagree 0.852 1.698
introvert 2: Strongly agree 1.427−0.513
Years on the platform−0.361
LinkedIn usage: 10–30 minutes per day 21.576 ∗∗∗
LinkedIn usage: 31–60 minutes per day 12.172 ∗∗∗
LinkedIn usage: 1–2 hours per day 20.192 ∗∗∗
LinkedIn usage: usage2–3 hours per day 17.978 ∗∗∗
LinkedIn usage: More than 3 hours per day 4.858
Search and apply for jobs−0.031
comment and share content−0.440
Keep profile up to date 6.092 ∗∗
LinkedIn groups 6.172 ∗∗
Facebook 4.201
Instagram −2.070
X 1.431
TikTok −5.362∗
Snapchat −5.556∗
Constant 43.799 ∗∗∗ 49.032∗∗∗ 19.091∗
N2,159 2,200 2,159
R2 0.069 0.125 0.196
Adj. R2 0.049 0.124 0.172
Res. SE 57.948 55.588 54.077
F Statistic 3.553 ∗∗∗ 104.832∗∗∗ 8.360∗∗∗
* (p<0.10), ** (p<0.05), *** (p<0.01)
58

Characteristic Run 1 Run 2
Observations 2,428 2,428
R-squared 0.262 0.167
Adjusted R-squared 0.254 0.166
F Statistic 30.473*** 162.106***
Number of Coefficients 28 3
log(connections):age 0.011 –
(0.015)
log(connections):group assignment150usd:age 0.082*** –
(0.021)
log(connections):group assignment200usd:age 0.038 –
(0.037)
log(connections):group assignment200usd:Messenger -1.922* –
(1.117)
log(connections):age:Engaging on your news feed 0.022** –
(0.010)
log(connections):Urban RuralUrban:FB.10–30 minutes per day 1.306* –
(0.667)
log(connections):group assignment200usd:Slightly conservative – 0.299**
(0.135)
Note: *p<0.1; **p<0.05; ***p<0.01
Table S18: Summarized Facebook OLS Regression Results: Facebook Value on LASSO
Covariates
59

Characteristic Run 1 Run 2 Run 3
Observations 2,187 2,187 2,187
R-squared 0.141 0.094 0.070
Adjusted R-squared 0.133 0.091 0.068
F Statistic 18.724*** 32.263*** 54.435***
Number of Coefficients 19 7 3
log(followers):group assignment150usd:age 0.057*** – –
(0.017)
log(followers):group assignment200usd:age 0.0004 – –
(0.046)
log(followers):group assignment200usd:Bookmark tweets 3.013*** – –
(0.790)
log(followers):group assignment200usd:age:X.2-3 hours per day 0.072*** – –
(0.022)
log(followers):group assignment200usd:age:Like reply retweet tweets 0.030 – –
(0.050)
log(followers):group assignment150usd:age:Direct messages 0.033* – –
(0.019)
log(followings):group assignment200usd:age – 0.063* –
(0.020)
group assignment200usd:Married or domestic partnership – – 10.161**
(4.416)
Table S19: Summarized X OLS Regression Results: X Value on LASSO Covariates
Note: *p<0.1; **p<0.05; ***p<0.01
Characteristic Run 1 Run 2 Run 3
Observations 2,440 2,440 2,440
R-squared 0.204 0.207 0.141
Adjusted R-squared 0.194 0.197 0.135
F Statistic 20.551*** 21.639*** 22.062***
Number of Coefficients 30 29 18
log(followers):group assignment150usd:age 0.066*** – –
(0.020)
log(followers):group assignment200usd:age -0.003 – –
(0.025)
log(followers):group assignment150usd:Urban RuralUrban 0.796 – –
(1.063)
log(followers):age:Post Instagram reels 0.011 – –
(0.013)
log(followers):Urban RuralUrban:Post photos as a post 0.462 – –
(0.520)
log(followers):group assignment200usd:age:Like and comment on stories 0.018 – –
(0.030)
log(followings):Urban Rural-Urban – 1.357** –
(0.608)
group assignment200usd:ethnicity - Asian or Pacific Islander – – 38.307***
(8.968)
Table S20: Summarized Instagram OLS Regression Results: Instagram Value on LASSO
Covariates
Note: *p<0.1; **p<0.05; ***p<0.01
60

Characteristic Run 1 Run 2
Observations 2,159 2,159
R-squared 0.216 0.141
Adjusted R-squared 0.200 0.137
F Statistic 13.255*** 32.036***
Number of Coefficients 44 11
log(connections):group assignment150usd:age 0.050* –
(0.026)
log(connections):group assignment200usd:age -0.023 –
(0.035)
log(connections):group assignment200usd:Facebook -2.090 –
(2.330)
log(connections):age:LinkedIn 2-3 hours per day 0.039* –
(0.020)
log(connections):age:LinkedIn groups 0.028** –
(0.013)
log(connections):group assignment150usd:age:Keep profile up to date 0.299** –
(0.135)
group assignment200usd:ethnicity - Asian or Pacific Islander – 36.604***
(8.698)
Table S21: Summarized LinkedIn OLS Regression Results: LinkedIn Value on LASSO
Covariates
Note: *p<0.1; **p<0.05; ***p<0.01
Figure S3: Conditional average valuations by ethnicity. Preregistered analysis for Wave 2.
61

Figure S4: Conditional average valuations by gender. Preregistered analysis for Wave 2.
Figure S5: Conditional average valuations by age group. Preregistered analysis for Wave 2.
62

Figure S6: Conditional average valuations by income. Preregistered analysis for Wave 2.
Figure S7: Conditional average valuations by number in household. Preregistered analysis
for Wave 2.
63

Figure S8: Conditional average valuations by number of moves. Preregistered analysis for
Wave 2.
Figure S9: Conditional average valuations by relationship status. Preregistered analysis for
Wave 2.
64

Figure S10: Conditional average valuations by urban vs. rural location. Preregistered anal-
ysis for Wave 2.
Figure S11: Conditional average valuations by years using platform. Preregistered analysis
for Wave 2.
65

Figure S12: Conditional average valuations by self-reported introversion. The index is the
average of the two introversion likert questions in the instrument. Preregistered analysis for
Wave 2.
66

S3.2.3 The Redundant Signal Model of Local Network Effect Share of Platform Value
In the manuscript, we use a different, theoretically motivated model for relating the number of
connections to platform value. This model is used for calculating the estimates of the Share of
Total Platform Value caused by network effects reported in Figure 1b. The equation is reported
in equation 6. We now briefly motivate the use of this model.
Previous papers have studied the value of two types of network effects, which are similar,
but not identical, to the phenomena of our primary interest. First are studies of undifferenti-
ated network effects, such as Metcalfe’s Law, examined theoretically (58) or empirically (35).
These studies are not of the value of specific connections to specific users, but rather of how a
large user base leads to high platform valuations, on average, through a variety of mechanisms.
A second set of studies is sociological, looking into how the value of different sorts of imme-
diate connections, in person or online, creates value for users. See, for example, the seminal
work by Granovetter (8) proposing the importance of weak ties for accessing information and
opportunities, and recent work by Rajkumar et al. (9) testing these theories on LinkedIn.
In this paper, we are interested in how individual-level platform value varies with the num-
ber and type of connections. To do so, we conceive of a model of platform value where
connections are formed to transmit information, both to the focal user and to the platform, to
improve the service for the focal user, for example, through more useful news feeds, direct
messages, or other personalized content.
In this framework, platform users make connections because they believe it will lead to
them either receiving or communicating data that is useful to them.
For example, consider someone on social media who wants to hear important information.
This could be personal information, like the birth of a colleague’s son, or professional infor-
mation, like a job opening in an industry important to the user. The connection could also
create value from being able to communicate the same information outwards. For example,
the information that the individual is newly single and looking for a date. The value gained
from these communications are examples of local network effects. This is because our user
67

would be highly unlikely to gain these benefits from the platform if he or she had not made the
connection.
This framework has several conceptual and practical advantages. First, it motivates the fact
that value from information conveyance on the platform faces decreasing returns, rather than
simply assuming it. Second, due to incentive compatibility constraints (we cannot credibly
commit to payments in the thousands of dollars), our measure of platform value has a maxi-
mum, so it makes sense to have a model of platform value where value saturates as the number
of connection increases. Finally, it is plausible that the value of information received on a
platform has a heavy tail, with most value being conveyed by a small minority of information,
making a model where one or a few signals create most of connection value plausible.
In this framework, the value of a particular connection may differ for several reasons.
First, certain connections may be more likely to send signals of different types. Second, certain
connections may be more redundant, giving information that the user is likely to know. Finally,
the value of a type of signal may be complementary to whether a signal of another type has
arisen: for example, the information that a job is available in a certain city is complementary
to information that the city has certain amenities.
Our vision of the value of local network effects – as connections that increase the likeli-
hood of me receiving valuable communications – leads us to model platform value through a
redundant signal or latent topics communication model. Messages across topics can be com-
plementary, because knowing one piece of information increases the value of another. More
commonly, messages are redundant, and not useful once a message has been received. This
leads to the following model of the total value to the user from all platforms:
T P Vi =
PX
p=1
δp +
KX
k=1
λk

1−e −Xik

+
KX
k=1
KX
ℓ=k+1
θkℓ

1−e −Xik
 
1−e −Xiℓ

+ε i,(S6)
68

and
Xik =
PX
p=1
TX
t=1
zitkp nitp, z itkp ≡ −log(1−πitkp).
WhereT P Vi represents total platform value for useriacross all platformsp;λ k represents
the value thatigets from hearing messagek, assuming they receive no other messages;1−
e−Xik corresponds to the probability that the user receives messagek. It is a function ofn itp –
the number of connections the user has of typeton platformp, as well asπ itkp, which is the
probability a contact of typetprovides the information of typekon platformp;θ k,ℓ represents
the level of complementarity (or redundancy) between information of typekandℓ.
This framework suggests several directions for analysis: understanding the share of value
that comes from the platform without connections (δ) vs. local network effects (the share of
platform value from local network effects, or SPV) is one. Another direction is to understand
the relative value of different sorts of connections, both at the margin and on average. We are
also interested in how different sorts of information might complement each other. Finally, we
might imagine that the types of information shared on different networks (the topicsk) might
be different even for the same user. We focus in particular on heterogeneity in the value of
connections of different types in the rest of the paper.
Figure 1b in the manuscript uses the model for the first question. Unfortunately, we do not
observe the share of connections by type at the individual level in our WTA analysis. We also
do not observe multiple platforms or data streams per user. However, we can still estimateδin
a simplified specification with homogeneous connection types and messages. This yields:
T P Vp,i =δ p +λ p

1−e −zp Cp,i  +ε i,
zp ≡ −log(1−π p), z≥0, λ≥0.
In the context of platforms with both followers and followees, we allow for these to have
twoλ k,p and twoπ k,p terms, representing a separate value (and cumulative probability) for an
69

Table S22: Estimate of the value of local network effects following the redundant signal model,
underlying Figure 1b
Facebook X Instagram LinkediN
alpha77.006 ∗∗∗ 72.007∗∗∗ 79.043∗∗∗ 79.119∗∗∗
(4.074) (1.837) (2.639) (1.760)
lambda (connection count)30.499 ∗∗∗ 36.926∗∗∗
(4.163) (7.217)
p (connection count)−0.015 ∗∗ −0.002∗
(0.005) (0.001)
lambda1 (followees)22.647 19.658 ∗∗∗
(12.664) (3.563)
p1 (followees)−0.000−0.003 ∗
(0.000) (0.001)
lambda2 (followers)13.026 ∗ 71.256∗∗∗
(6.205) (21.477)
p2 (followers)−0.001−0.000
(0.001) (0.000)
Sigma59.736 58.281 57.531 58.619
Convergence1 1 1 1
Tolerance0.000 0.000 0.000 0.000
Log Likelihood−13605.422−12265.680−13609.988−12076.511
AIC27218.844 24543.360 27231.977 24161.021
BIC27242.092 24577.637 27266.892 24183.806
Deviance8803257.076 7581341.312 8218205.717 7549421.848
DF Resid.2467 2232 2483 2197
nobs2470 2237 2488 2200
∗∗∗p <0.001; ∗∗p <0.01; ∗p <0.05
outgoing and incoming signal – essentially treating these as different topics.θ k,ℓ is set so these
values are perfect substitutes.
70

S4 Robustness
This section reports the results of several robustness checks on the validity of our results. Sec-
tion S4.1 focuses on the predictors of connection value percentile after restricting attention to
only the top four connections. Section S4.2 reports analysis of the predictors of total platform
value. Our main results on total platform value are derived from Wave 2. Here, where pos-
sible, we look to see whether the same patterns held in Wave 1 data. Section S4.2.1 reports
regressions of total platform value on the number of platform connections and other scraped
platform data from Wave 1. Section S4.2.2 reports whether predictors of platform value inves-
tigated in Wave 2 also held in Wave 1, focusing on platform time use and political orientation.
The Wave 1 sample retains the strong relationship between hours of use and total platform
value observed in Wave 2.
A final possible concern about our analyses may be the sensitivity of our findings to the
maximum value egos are allowed to report for total platform value using the BDM mechanism.
In Wave 1, respondents could enter a free-response answer if their monthly total platform value
was greater than $100. In Wave 2, users are randomly assigned to a maximum value of $100,
$150 or $200. We investigated the robustness of our main results to additional controls for the
Wave 2 maximum value assignment and found these controls do not attenuate our large and
significant estimates of the relationship of log connection count and total monthly platform
value (see Tables S14 through S17). As a second investigation of the importance of the long-
tail of high-value platform valuers, we report the empirical CDF of total platform value by
ego respondents along two variations: with the Wave 1 sample and a winsorization at $100,
vs using the free response valuations. We found that less than 1% of respondents value the
platform at more than $1000 in Wave 1. One implication of this finding is that, given the small
fraction of high valuations, our total platform value results from Wave 1 and Wave 2 should be
interpreted as representative of typical valuations rather than fully describing the distribution
of valuations.
71

S4.1 Robustness of Predictors of Connection Value Percentile
Previous studies investigating the determinants of relationship importance have used a variety
of methods for soliciting the list of contacts to be investigated. In Marsden and Campbell
(2), interviewers solicited the names of the subjects’ three closest friends. In Fischer (3),
interviewers asked open-ended questions about the subject’s life, generating a list of 2-26
acquaintances per subject. Our approach in the main data was a hybrid of these approaches.
We asked the egos to report their four closest connections (who may or may not be on the
platform) as well as four other top-of-mind contacts on the platform.
There are advantages and disadvantages to different approaches for soliciting connections.
A focus on the closest connections helps ensure that the subject will have good knowledge of
and strong preferences over the relationships. On the other hand, the relationships we have
with close connections are distinctive. The things that endear us to our closest connections
may repel us in more distant relations. To cover a more complete range of relationships, it is
important to include less close relations in the sample.
For robustness, we re-analyzed our CVP results for just the ego’s closest connections.
These are the connections that consumers are likely to have the strongest and most consistent
preferences over, making these robustness results most closely comparable to the results re-
ported by Marsden and Campbell (2). Figures S13, S14 and S15 report conditional average
CVPs, restricting attention to the four closest contacts. Figure S13 shows that our first main re-
sult, that people seen more often had higher CVPs, was replicated in the top four connections.
Just like in the main analysis Figure 2B, for Facebook the CVP of alters who live with egos
was significantly higher than on X. Figure S14 broadly replicates the main analysis of family
and college friends having the highest CVP. Unlike in the main analysis here, for Facebook,
the point estimate for the CVP for ‘none of these describe how I know this person’ was larger
than the CVPs for school and work, which is suggestive of the value of top connections. S15 is
also very similar to the main result in Figure 2C, with the closest four connections having sig-
nificantly higher CVP when connected to the ego on a second platform, for all focal platforms,
72

replicating the suggestive evidence of a lack of substitution between platforms.
50%
60%
70%
80%Connection Value Percentile (fited)
Never Less than
4 times/year
About once
a month
About once
a week
Multiple times
per week
I live with this
person
How often do you meet Alter?
Figure S13: Connection value percentile as a function of how often seen. Wave 1, four closest
connections only.
55%
60%
65%Connection Value Percentile (fited)
WorkI only know them online School (K−12) None of these describe how I know this person College or University Family member or family friend Through a shared interest in real life
How do you know Alter?
Figure S14: Connection value percentile as a function of connection source. Wave 1, four
closest connections only.
73

55%
57.5%
60%
62.5%
65%
No Yes
Connection Value Percentile (fited)
Are you connected with Alter on other platform?
Figure S15: Connection value percentile as a function of connection source. Wave 1, four
closest connections only.
S4.2 Robustness of Predictors of Total Platform Value
While Wave 2 focused on Total Platform Valuation, we examine whether similar patterns hold
in Wave 1 data.
S4.2.1 Measuring the Value of Connections with Wave 1 Data
We used Wave 1 data to establish the robustness of our results on the value of connections
across platforms. For X, Facebook, and LinkedIn, we were able to collect additional data
on platform use from a subset of survey participants. We were unable to collect additional
information from Instagram users because of platform scraping restrictions. We were able to
collect additional data from about∼25% of respondents overall. For each of these respondents,
we were able to collect connection count information directly from the platform.
Table S23 reports the results of a regression of total platform valuation, winsorized at
$1,000, on the log of connection counts scraped from Wave 1 survey participants. While not
74

significant, the point estimates are consistent with those from Wave 2 focused on whether
platform value is increasing in log(connections) for Facebook and LinkedIn. For X, where
followers and followees are distinguished, log(followers) entered the analysis positively and
log(followees) negatively. The lack of significance in these estimates is almost certainly due
to the small sample size of our scraped data.
Total Monthly Platform Valuation
Facebook X LinkedIn
log(Connections)2.108
(2.716)
log(Followers)3.874
(5.111)
log(Followees)−3.030
(6.649)
log(Connections)4.913
(5.311)
Constant 114.980 ∗∗∗ 106.880∗∗∗ 73.120∗∗∗
(14.534) (22.839) (26.182)
Observations 944 599 344
R2 0.001 0.001 0.002
AdjustedR 2 −0.0004−0.002−0.0004
Residual SE 165.870 155.840 130.790
FStatistic 0.602 0.318 0.856
Table S23: OLS Regression for the Total Monthly Valuation on Log-Connection Count (Wave
1 Main Text Filtering)
Standard Errors in parenthesis. Note: *p<0.1; **p<0.05; ***p<0.01
Interestingly, the result that log follower count positively predicts total platform value while
log followee count negatively predicts value is sensitive to the level at which platform valua-
tions were winsorized (the positive relationship between total connection count and platform
value for Facebook and LinkedIn was not sensitive to this decision). This finding is reported
in Table S24.
This result is consistent with the ‘attention bartering’ theory of X value in Filippas et.
al. (59). According to this theory, intensive users of X get positive value from being followed,
but negative value from following all but a small subset of accounts. However, a close corre-
75

lation between the count of followers and followees emerges because users trade following a
third party that they would not follow otherwise in return for that party following their own
accounts. They document this correlation in their study population of economists. In our data,
log followers and log followees were also highly correlated—for example, on X the correlation
was over 80%.
Under the attention bartering theory, a change in the relative importance of followers and
followees as total platform value winsorization increases would emerge if there are two types
of users. We’ll call these ‘lurkers’ and ‘broadcasters’. The lurkers do not care about being
followed (or may even dislike it) and follow only accounts they directly value. This group has
a low total platform value, but their platform value is increasing in the number of accounts
followed (followees). Broadcasters have high total platform value, which is increasing in the
number of accounts that follow them (followers). In order to increase their number of followers
they barter following uninteresting accounts that they do not directly value. Broadcasters may
also value following some accounts, but most of their followees actually give them negative
value directly. When platform values are winsorized at low levels, it is the preferences of
lurkers which dominate the correlation between connection count and platform value. When
platform values are winsorized at high levels, the preferences of the broadcasters are more
influential in determining the correlations.
In addition to connection count, for LinkedIn users we were able to collect information on
labor force participation. Table S25 shows a positive point estimate for connection count on
LinkedIn platform value. Furthermore, individuals with a long tenure at their current work-
place valued LinkedIn less, which is consistent with LinkedIn being used for job search. This
finding is also consistent with our finding from Wave 2 that people who are searching for a job
value LinkedIn more.
Table S26 looks at other aspects of X use and platform value. This information was down-
loaded from the X API for a subset of Wave 1 participants. We found that the number of
reposts the account has had in its history is a significant positive predictor of Total Platform
76

Total Monthly Platform Valuation (X)
Win. = 100 Win. = 200 Win. = 300 Win. = 400 Win. = 500 Win. = 1000
log(Followers)−0.504−0.444 0.042 0.691 1.343 3.874
(1.129) (1.689) (2.247) (2.721) (3.139) (5.111)
log(Followees) 2.414 1.783 1.192 0.522−0.089−3.030
(1.468) (2.197) (2.922) (3.539) (4.083) (6.649)
Constant59.655 ∗∗∗ 73.253∗∗∗ 80.609∗∗∗ 85.751∗∗∗ 89.578∗∗∗ 106.880∗∗∗
(5.044) (7.548) (10.038) (12.157) (14.024) (22.839)
Observations 599 599 599 599 599 599
R2 0.008 0.002 0.001 0.001 0.001 0.001
AdjustedR 2 0.005−0.002−0.003−0.003−0.003−0.002
Residual SE34.417 51.501 68.496 82.951 95.691 155.840
FStatistic2.387 ∗ 0.534 0.247 0.202 0.233 0.318
Table S24: OLS Regression of the Total Monthly Valuation for X on Log Followers and Fol-
lowees (Different Winsorizations of Total Platform Value)
Notes: Standard Errors in parenthesis. *p<0.1; **p<0.05; ***p<0.01
LinkedIn Monthly Valuation
(1) (2) (3)
log(Connections) 4.913 7.447
(5.311) (5.821)
Currently working>1year−14.460−16.458
(15.475) (15.538)
Constant73.120 ∗∗∗ 103.820∗∗∗ 68.913∗∗
(26.182) (10.037) (29.070)
Observations 344 309 309
R2 0.002 0.003 0.008
AdjustedR 2 −0.0004−0.0004 0.002
Residual SE130.790 134.290(df = 307)134.150
FStatistic0.856 0.873 1.256
Table S25: OLS Regression for Total Monthly Valuation on Connections Count and Tenure of
Current Employment
Notes: Standard Errors in parenthesis. *p<0.1; **p<0.05; ***p<0.01
77

Valuation, with every repost raising the monthly value of the platform by 5.1 cents, and quotes
by 29.8 cents. On the other hand, receiving replies is predictive of lower platform value, by
2.3 cents each. This result is again consistent with that idea that broadcasting information is
of higher value than consuming it.
X Monthly Valuation
(1) (2)
log(Followers) 3.874
(5.111)
log(Followees)−3.030
(6.649)
Total retweets0.051 ∗∗∗
(0.013)
Total quotes0.298 ∗∗∗
(0.065)
Total replies−0.023 ∗∗∗
(0.009)
Favorite count0.005 ∗∗
(0.003)
Constant106.880 ∗∗∗ 87.902∗∗∗
(22.839) (7.738)
Observations599 571
R2 0.001 0.093
AdjustedR 2 −0.002 0.087
Residual SE155.840 142.450
FStatistic0.318 14.523 ∗∗∗
Table S26: OLS Regression of Total Monthly Valuation on Social Metrics (Platform Value
Winsorized at $1,000)
Notes: Standard Errors in parenthesis. *p<0.1; **p<0.05; ***p<0.01
S4.2.2 Other Predictors of Total Platform Value from Wave 1
Table S16 reports conditional average Total Platform Valuations by self-reported political ori-
entation from Wave 1. The figure confirms the Wave 2 result that individuals who use a plat-
form more value it more highly.
78

60
70
80Platform Valuation
Extremely
Conservative Conservative Slightly Conservative Moderate Slightly Liberal Liberal Extremely Liberal
60
70
80Platform Valuation
Less than 10
minutes per day
10 to 30 minutes
 per day
31 to 60 minutes
per day
1 to 2 hours
per day
2 to 3 hours
per day
More than 3
hours per day
a.
b.
Figure S16: Conditional average valuations by self-reported political orientation and platform
usage. Wave 1 main analysis data.
S4.2.3 Sensitivity to Alternate Maximum Platform Value
For our total platform value results, we gathered data using the BDM method. A potential
weakness of the BDM method for soliciting willingness-to-pay is that results may be less
reliable for those with very large valuations. There are a few reasons for this. First, a low-
attention survey taker may select a very large willingness to pay out of carelessness. To control
for this possibility we executed attention checks, described earlier, and filtered out respondents
found to display carelessness. Second, all BDM mechanisms rely on the subject having a
positive expectation that they will be offered a follow up contract. As true valuations get larger,
users may find it increasingly unlikely that the BDM mechanism will actually be enforced, and
therefore be more careless in reporting their true valuation if it is large. These challenges are
common and apply to all incentive compatible valuations and BDM mechanisms. Here we
describe their implications for our results and our work to ensure robustness in the face of
these challenges.
79

The inability to precisely probe valuations for users who have very high WTPs for social
media has important consequences, especially for studies trying to make aggregate claims
about the contribution of social media to total welfare. This is because there plausibly exists
a thick-tail of platform users with extremely high valuations – which would be consistent
with the large count of users who use social media for a large share of their waking hours.
For example, one nationally representative Gallup survey found that 29% of teens used social
media for 6 hours or more a day on average (60). Therefore it poses a specific challenge for
work like that of Bursztyn et al. (44) who focus on the question of aggregate welfare.
Other BDM studies of the value of social media have approached this problem in different
ways. Allcott et al. (37) allow for a free response in their BDM value solicitation, but winsorize
maximum replies at $170. This value is selected as the maximum because it is the maximum
payment that they allow in their randomized BDM offer, though this cutoff was not made
known to participants. Bursztyn et al. (44) have a multiple price list soliciting their BDM,
with a maximum set at $200. In a robustness section, they fit a thin-tailed curve through their
results, allowing for imputed values above $200 and argue this does not change their findings.
Brynjolfsson et al. (36) focus on median valuations to avoid this issue entirely.
In our context, we are primarily interested in determinants of CVP, which are not impacted
by this issue, as well as how connections predict total platform value. Estimation of total
platform value is impacted by BDM measurement challenges, but less so as the results can
simply be interpreted as predictors of platform value for typical users rather than all users.
Regardless, in our two study Waves, we took different approaches to this challenge. In Wave
1, we used a slider up to $100 and then a free-response box for values larger than $100. Our
main results were winsorized at the $100 dollar level. In Wave 2 we used a multiple price list,
with users randomly assigned to $100, $150 and $200 maximum values. We used this Wave 2
data for our main total platform value results and showed the sensitivity of results to controls
for these maximum values in Tables S14 thorough S17. The point estimates of the effect of
log(connections) on total platform value were not sensitive to these controls, indicating the
80

robustness of our main results.
In this section we report further robustness checks using Wave 1 data to understand what
percentage of responses were impacted by the presence of a maximum value. Figure S17 A re-
ports the empirical CDF of Total Platform Valuations in our Wave 1 study with a winsorization
of $100. Figure S17B reports the same, but increases the $100 winsorization to $1,000,000.
In Panel B, log total platform values are reported on the x-axis.
In the Wave 1 data, pooling all platforms, less than 1% of respondents reported valuations
above $1,000. X and Instagram were the platforms most impacted by winsorization in the
filtered data, suggesting that the long tail of high valuers may be particularly important for
these platforms. These facts suggest a need for some caution when interpreting the aggregate
welfare implications of the results derived from our valuation methods, if a large share of
value is driven by a small number of high valuers who are imprecisely measured. However,
the fact that less than 1% of our sample are high valuers makes us retain confidence in our total
platform valuation estimates. Furthermore, winsorization and maximum values do not impact
our CVP results or connection valuations for typical platform users, giving us more confidence
in our results and interpretations.
81

Figure S17: Empirical CDFs of total platform value from Wave 1. A. Responses capped at
$100. B. Responses capped at $1,000,000.
82

S5 Additional Data Collection Tables
Description Details
User’s id by number Unique numerical identifier for a user
Tweet id by number Unique numerical identifier for a tweet
Tweet creation date Timestamp when the tweet was posted
User’s id by screen name User’s handle on X
Tweet content Text of the tweet
App used for writing the tweet Source application (e.g., Android, iPhone, Web App)
Number of characters used in the tweet Displayed tweet width in characters
Tweet’s id to which the user responded ID of the tweet being replied to (NA if not a reply)
User’s id to which the user responded Numerical ID of the user being replied to (NA if not a reply)
User’s id by screen name to which the user
responded
Screen name of the user being replied to (NA if not a reply)
TRUE if quoting another tweet Indicates if the tweet is a quote
TRUE if retweeting another tweet Indicates if the tweet is a retweet
Number of “favorite” reactions Count of likes/favorites on the tweet
Number of retweets Count of retweets for the tweet
Number of quotes Count of quotes for the tweet
Number of responses Count of replies to the tweet
Words after the hashtag symbol Hashtags used in the tweet
Symbols used in the tweet
URLs in the tweet List of URLs used
Media used in the tweet Links and types of media (e.g., photos, videos)
Mentions in the tweet Users mentioned by screen name or ID
Language of the tweet Detected language of the content
Information about quoted tweets Includes ID, content, creation date, and engagement metrics
Information about retweeted tweets Includes ID, content, creation date, and engagement metrics
Location data Place name, coordinates, and country if available
User’s profile data Includes name, location, description, URLs, and account status
Account statistics Followers, friends, statuses, and favorites counts
Verification and protection Whether the account is verified or protected
83

User’s media links Profile images, banner URLs, and background themes
Table S27: Twitter/X Additional Ego Timeline Data Collection: This data is available for a
subset of Twitter/X study participants through November 2021. For regressions in Table S26
some variables were aggregated to the account level.
84

Account ID UTC datetime of account creation
whether ‘contributor mode’ enabled user description
User display name number of Tweets user has liked
User follower count Authenticating user has issued follow re-
quest
User followee count Geotagging Enabled
Participant in Twitter translator commu-
nity
User language
Number of public lists user is on User defined location
Indicator for protected tweets User handle
Count of Tweets and retweets User Timezone
User URL User UTC offset
User verified indicator Countries user is witheld from
Table S28: Twitter/X Account level data collected for a subset of Wave 1 study participants
and their non-private followers and followees.
85

Field Name Description
linkedinProfile URL of the LinkedIn profile
email Email address
headline User’s professional headline
location User’s location
imgUrl URL of the user’s profile picture
firstName, lastName, fullName User’s first name, last name, and full name
subscribers Number of followers or subscribers
connectionsCount Total number of connections
company, company2 Names of current and previous company
companyUrl, companyUrl2 URLs of current and previous company LinkedIn pages
jobTitle, jobTitle2 Titles of current and previous job
jobDescription, jobDescription2 Descriptions of current and previous job
jobLocation, jobLocation2 Locations of current and previous job
jobDateRange, jobDateRange2 Date ranges of current and previous job
school, school2 Names of attended schools
schoolUrl, schoolUrl2 URLs of attended schools’ LinkedIn pages
schoolDegree, schoolDegree2 Degrees obtained from schools
schoolDateRange, schoolDat-
eRange2
Date ranges of attendance at schools
schoolDescription, schoolDe-
scription2
Descriptions of attended schools
skill1 - skill6; endorsement1-
endorsement6
Up to 6 listed skills count of ‘endorsements’ by third parties for each
allskills any self-reported skills including beyond the first 6
timestamp Timestamp of data scraping
website, twitter, facebookUrl User’s website, Twitter handle, and Facebook URL
birthday User’s birthday
Table S29: Resume information collected from a subset of Wave 1 LinkedIn Study Participants
from their profile page.
86

S6 Full Statistical Reporting of the Findings
For completeness and in the interest of maximum clarity, this section presents estimated dif-
ferences, and associated p-values, for the results in Figures 1 through 4 of the main text. In
section S6.1, we report estimates for selected groups which are aggregated at a higher level
than in the main text figures. In section S6.2 we report all estimated differences between pairs
of estimates in the main text figures.
S6.1 Grouped Comparisons
In this section we present estimated differences, and associated p-values, for selected aggrega-
tions of respondents.
For example, Figure 1C reports estimates of platform valuations, conditional on platform
type and six bins indicating the amount of time spent on the platform. Table S30 reports corre-
sponding estimates based on this figure. In particular, here we report the estimated difference
in platform value between pairs of conditions but aggregating to only two participation levels:
above and below one hour a day. The first row of the table indicates that users who use Face-
book less than 1 hour a day value it$8.848a month less than those who use it 1 hour a day
or more. The row is bolded, indicating the difference is significantly different from zero at the
99% confidence level, having an associated p-value of .006.
87

contrast estimate SE t-stat p-value1 Less than 1 hour per day Facebook - More than 1 hour per day Facebook -8.848 2.401 -3.685 0.006
2 Less than 1 hour per day Facebook - Less than 1 hour per day Instagram 11.193 2.173 5.152 0.00001
3 Less than 1 hour per day Facebook - More than 1 hour per day Instagram -2.837 2.473 -1.147 0.946
4 Less than 1 hour per day Facebook - Less than 1 hour per day LinkedIn 11.906 2.097 5.678 0.00000
5 Less than 1 hour per day Facebook - More than 1 hour per day LinkedIn 2.872 3.321 0.865 0.989
6 Less than 1 hour per day Facebook - Less than 1 hour per day X 24.199 2.207 10.966 0
7 Less than 1 hour per day Facebook - More than 1 hour per day X 8.813 2.614 3.371 0.017
8 More than 1 hour per day Facebook - Less than 1 hour per day Instagram 20.040 2.361 8.488 0
9 More than 1 hour per day Facebook - More than 1 hour per day Instagram 6.010 2.640 2.277 0.307
10 More than 1 hour per day Facebook - Less than 1 hour per day LinkedIn 20.753 2.291 9.057 0
11 More than 1 hour per day Facebook - More than 1 hour per day LinkedIn 11.720 3.447 3.400 0.016
12 More than 1 hour per day Facebook - Less than 1 hour per day X 33.047 2.392 13.813 0
13 More than 1 hour per day Facebook - More than 1 hour per day X 17.661 2.773 6.369 0
14 Less than 1 hour per day Instagram - More than 1 hour per day Instagram -14.030 2.434 -5.763 0.00000
15 Less than 1 hour per day Instagram - Less than 1 hour per day LinkedIn 0.713 2.051 0.348 1.000
16 Less than 1 hour per day Instagram - More than 1 hour per day LinkedIn -8.320 3.293 -2.527 0.184
17 Less than 1 hour per day Instagram - Less than 1 hour per day X 13.006 2.163 6.012 0.00000
18 Less than 1 hour per day Instagram - More than 1 hour per day X -2.379 2.578 -0.923 0.984
19 More than 1 hour per day Instagram - Less than 1 hour per day LinkedIn 14.743 2.367 6.229 0
20 More than 1 hour per day Instagram - More than 1 hour per day LinkedIn 5.709 3.498 1.632 0.731
21 More than 1 hour per day Instagram - Less than 1 hour per day X 27.036 2.465 10.969 0
22 More than 1 hour per day Instagram - More than 1 hour per day X 11.651 2.836 4.109 0.001
23 Less than 1 hour per day LinkedIn - More than 1 hour per day LinkedIn -9.033 3.243 -2.786 0.099
24 Less than 1 hour per day LinkedIn - Less than 1 hour per day X 12.293 2.087 5.891 0.00000
25 Less than 1 hour per day LinkedIn - More than 1 hour per day X -3.092 2.514 -1.230 0.923
26 More than 1 hour per day LinkedIn - Less than 1 hour per day X 21.327 3.315 6.433 0
27 More than 1 hour per day LinkedIn - More than 1 hour per day X 5.941 3.599 1.651 0.719
28 Less than 1 hour per day X - More than 1 hour per day X -15.386 2.607 -5.903 0.00000
Table S30: Full reporting of the comparative statistics of Figure 1C in the main text where we
group usage levels to More or Less than 1 hour.Highlighted contrastsare significant at the
1% level. DF = 9387.
S6.1.1 Figure 1C: Total Platform Valuation by Platform & Usage, Aggregated to Two
Usage Levels
S6.1.2 Figure 1C: Total Platform Valuation by Platform & Usage, Aggregated over all
platforms
contrast estimate ($) SE t-stat p-value
1 Less than 10 minutes per day - 10–30 minutes per day -27.546 2.067 -13.329 0
2 Less than 10 minutes per day - 31–60 minutes per day -11.478 1.739 -6.602 0
3 Less than 10 minutes per day - 1–2 hours per day -27.037 2.609 -10.361 0
4 Less than 10 minutes per day - 2–3 hours per day -18.408 1.925 -9.565 0
5 Less than 10 minutes per day - More than 3 hours per day -39.561 2.641 -14.982 0
6 10–30 minutes per day - 31–60 minutes per day 16.068 1.907 8.424 0
7 10–30 minutes per day - 1–2 hours per day 0.508 2.725 0.187 1.000
8 10–30 minutes per day - 2–3 hours per day 9.138 2.078 4.397 0.0002
9 10–30 minutes per day - More than 3 hours per day -12.015 2.755 -4.362 0.0002
10 31–60 minutes per day - 1–2 hours per day -15.560 2.485 -6.261 0
11 31–60 minutes per day - 2–3 hours per day -6.930 1.753 -3.954 0.001
12 31–60 minutes per day - More than 3 hours per day -28.083 2.518 -11.153 0
13 1–2 hours per day - 2–3 hours per day 8.630 2.619 3.295 0.013
14 1–2 hours per day - More than 3 hours per day -12.524 3.182 -3.936 0.001
15 2–3 hours per day - More than 3 hours per day -21.153 2.650 -7.983 0
Table S31: Full reporting of the comparative statistics of Figure 1C in the main text: Pairwise
Comparisons of the average over all platforms TPV for the different Usage Levels.High-
lighted contrastsare significant at the 1% level. DF=9389.
88

S6.1.3 Figure 1D: Total Platform Valuation by Platform & Political Orientation, Ag-
gregated to Three Orientations
contrast estimate ($) SE t-stat p-value
1 Liberal Facebook - Moderate Facebook -2.910 2.923 -0.995 0.998
2 Liberal Facebook - Conservative Facebook 6.328 3.803 1.664 0.885
3 Liberal Facebook - Liberal Instagram 11.417 3.596 3.175 0.066
4 Liberal Facebook - Moderate Instagram 7.452 2.914 2.557 0.305
5 Liberal Facebook - Conservative Instagram 11.047 3.721 2.969 0.118
6 Liberal Facebook - Liberal LinkedIn 15.251 3.589 4.250 0.001
7 Liberal Facebook - Moderate LinkedIn 10.978 2.999 3.660 0.013
8 Liberal Facebook - Conservative LinkedIn 17.843 3.776 4.726 0.0001
9 Liberal Facebook - Liberal X 21.019 3.603 5.833 0.00000
10 Liberal Facebook - Moderate X 19.669 2.977 6.608 0
11 Liberal Facebook - Conservative X 29.677 3.822 7.766 0
12 Moderate Facebook - Conservative Facebook 9.238 3.265 2.829 0.168
13 Moderate Facebook - Liberal Instagram 14.327 3.021 4.742 0.0001
14 Moderate Facebook - Moderate Instagram 10.362 2.166 4.784 0.0001
15 Moderate Facebook - Conservative Instagram 13.957 3.169 4.404 0.001
16 Moderate Facebook - Liberal LinkedIn 18.161 3.013 6.028 0.00000
17 Moderate Facebook - Moderate LinkedIn 13.888 2.279 6.095 0.00000
18 Moderate Facebook - Conservative LinkedIn 20.753 3.233 6.419 0
19 Moderate Facebook - Liberal X 23.929 3.030 7.897 0
20 Moderate Facebook - Moderate X 22.579 2.249 10.041 0
21 Moderate Facebook - Conservative X 32.587 3.287 9.915 0
22 Conservative Facebook - Liberal Instagram 5.089 3.879 1.312 0.978
23 Conservative Facebook - Moderate Instagram 1.124 3.257 0.345 1.000
24 Conservative Facebook - Conservative Instagram 4.719 3.996 1.181 0.990
25 Conservative Facebook - Liberal LinkedIn 8.923 3.873 2.304 0.474
26 Conservative Facebook - Moderate LinkedIn 4.650 3.334 1.395 0.965
27 Conservative Facebook - Conservative LinkedIn 11.515 4.046 2.846 0.161
28 Conservative Facebook - Liberal X 14.690 3.886 3.780 0.009
29 Conservative Facebook - Moderate X 13.341 3.313 4.027 0.003
30 Conservative Facebook - Conservative X 23.348 4.089 5.710 0.00000
31 Liberal Instagram - Moderate Instagram -3.965 3.013 -1.316 0.977
32 Liberal Instagram - Conservative Instagram -0.370 3.799 -0.097 1
33 Liberal Instagram - Liberal LinkedIn 3.834 3.669 1.045 0.997
34 Liberal Instagram - Moderate LinkedIn -0.439 3.095 -0.142 1
35 Liberal Instagram - Conservative LinkedIn 6.426 3.852 1.668 0.883
36 Liberal Instagram - Liberal X 9.602 3.683 2.607 0.276
37 Liberal Instagram - Moderate X 8.252 3.073 2.685 0.234
38 Liberal Instagram - Conservative X 18.260 3.897 4.685 0.0002
39 Moderate Instagram - Conservative Instagram 3.595 3.161 1.137 0.993
40 Moderate Instagram - Liberal LinkedIn 7.799 3.004 2.596 0.282
41 Moderate Instagram - Moderate LinkedIn 3.526 2.267 1.555 0.925
42 Moderate Instagram - Conservative LinkedIn 10.391 3.225 3.222 0.058
43 Moderate Instagram - Liberal X 13.567 3.021 4.490 0.0004
44 Moderate Instagram - Moderate X 12.217 2.237 5.461 0.00000
45 Moderate Instagram - Conservative X 22.225 3.279 6.778 0
46 Conservative Instagram - Liberal LinkedIn 4.204 3.792 1.109 0.994
47 Conservative Instagram - Moderate LinkedIn -0.069 3.240 -0.021 1
48 Conservative Instagram - Conservative LinkedIn 6.796 3.969 1.712 0.863
49 Conservative Instagram - Liberal X 9.972 3.806 2.620 0.268
50 Conservative Instagram - Moderate X 8.622 3.219 2.679 0.237
51 Conservative Instagram - Conservative X 18.630 4.013 4.642 0.0002
52 Liberal LinkedIn - Moderate LinkedIn -4.273 3.087 -1.384 0.967
53 Liberal LinkedIn - Conservative LinkedIn 2.592 3.845 0.674 1.000
54 Liberal LinkedIn - Liberal X 5.768 3.676 1.569 0.920
55 Liberal LinkedIn - Moderate X 4.418 3.064 1.442 0.955
56 Liberal LinkedIn - Conservative X 14.426 3.891 3.708 0.011
57 Moderate LinkedIn - Conservative LinkedIn 6.865 3.302 2.079 0.638
58 Moderate LinkedIn - Liberal X 10.041 3.103 3.235 0.055
59 Moderate LinkedIn - Moderate X 8.691 2.347 3.704 0.012
60 Moderate LinkedIn - Conservative X 18.699 3.354 5.574 0.00000
61 Conservative LinkedIn - Liberal X 3.175 3.859 0.823 1.000
62 Conservative LinkedIn - Moderate X 1.826 3.281 0.556 1.000
63 Conservative LinkedIn - Conservative X 11.833 4.063 2.912 0.137
64 Liberal X - Moderate X -1.350 3.081 -0.438 1.000
65 Liberal X - Conservative X 8.658 3.904 2.218 0.537
66 Moderate X - Conservative X 10.008 3.334 3.002 0.108
89

Table S32: Full reporting of the comparative statistics of Figure 1D in the main text where
extremely conservative and conservatives are grouped as conservative and extremely Liberals
are groups with Liberals. Everything else is grouped as moderates.Highlighted contrastsare
significant at the 1% level. DF=9383.
S6.1.4 Figure 1D: Total Platform Valuation by Platform & Political Orientation, Ag-
gregated over all platforms
contrast estimate ($) SE t-stat p-value
1 Extremely liberal - Liberal -3.727 2.621-1.422 0.790
2 Extremely liberal - Slightly liberal -7.983 3.147-2.537 0.146
3 Extremely liberal - Moderate -1.395 2.511-0.556 0.998
4 Extremely liberal - Slightly conservative -6.748 2.233-3.022 0.040
5 Extremely liberal - Conservative1.450 2.822 0.514 0.999
6 Extremely liberal - Extremely conservative3.197 2.860 1.118 0.923
7 Liberal - Slightly liberal -4.256 2.979-1.428 0.787
8 Liberal - Moderate2.332 2.298 1.015 0.951
9 Liberal - Slightly conservative -3.021 1.990-1.518 0.734
10 Liberal - Conservative5.177 2.634 1.965 0.437
11 Liberal - Extremely conservative6.925 2.675 2.588 0.130
12 Slightly liberal - Moderate6.588 2.883 2.285 0.251
13 Slightly liberal - Slightly conservative1.235 2.645 0.467 0.999
14 Slightly liberal - Conservative9.433 3.158 2.987 0.045
15 Slightly liberal - Extremely conservative 11.180 3.192 3.502 0.008
16 Moderate - Slightly conservative -5.353 1.844 -2.904 0.057
17 Moderate - Conservative 2.845 2.525 1.127 0.920
18 Moderate - Extremely conservative 4.592 2.568 1.788 0.556
19 Slightly conservative - Conservative 8.198 2.249 3.645 0.005
20 Slightly conservative - Extremely conservative 9.946 2.297 4.330 0.0003
21 Conservative - Extremely conservative1.748 2.873 0.608 0.997
Table S33: Full reporting of the comparative statistics of Figure 1D in the main text: Pairwise
Comparisons of average over the four platforms TPV for the different Political Groups.High-
lighted contrastsare significant at the 1% level. DF=9388.
90

S6.1.5 Figure 1E: Total Platform Valuation by Platform & Relationship Status, Aggre-
gated to Married and Unmarried
contrast estimate ($) SE t-stat p-value
1 Married or domestic partnership Facebook - Not Married Facebook 8.166 2.435 3.354 0.018
2 Married or domestic partnership Facebook - Married or domestic partnership Instagram 13.997 2.564 5.458 0.00000
3 Married or domestic partnership Facebook - Not Married Instagram 14.984 2.495 6.005 0.00000
4 Married or domestic partnership Facebook - Married or domestic partnership LinkedIn 14.923 2.650 5.631 0.00000
5 Married or domestic partnership Facebook - Not Married LinkedIn 22.367 2.556 8.750 0
6 Married or domestic partnership Facebook - Married or domestic partnership X 24.076 2.666 9.031 0
7 Married or domestic partnership Facebook - Not Married X 30.088 2.528 11.904 0
8 Not Married Facebook - Married or domestic partnership Instagram 5.831 2.315 2.519 0.187
9 Not Married Facebook - Not Married Instagram 6.818 2.238 3.047 0.048
10 Not Married Facebook - Married or domestic partnership LinkedIn 6.758 2.409 2.805 0.094
11 Not Married Facebook - Not Married LinkedIn 14.201 2.305 6.160 0.00000
12 Not Married Facebook - Married or domestic partnership X 15.911 2.426 6.557 0
13 Not Married Facebook - Not Married X 21.922 2.274 9.642 0
14 Married or domestic partnership Instagram - Not Married Instagram 0.987 2.378 0.415 1.000
15 Married or domestic partnership Instagram - Married or domestic partnership LinkedIn 0.927 2.540 0.365 1.000
16 Married or domestic partnership Instagram - Not Married LinkedIn 8.370 2.442 3.427 0.014
17 Married or domestic partnership Instagram - Married or domestic partnership X 10.079 2.557 3.942 0.002
18 Married or domestic partnership Instagram - Not Married X 16.091 2.412 6.671 0
19 Not Married Instagram - Married or domestic partnership LinkedIn -0.060 2.471 -0.024 1
20 Not Married Instagram - Not Married LinkedIn 7.383 2.369 3.116 0.039
21 Not Married Instagram - Married or domestic partnership X 9.092 2.487 3.656 0.006
22 Not Married Instagram - Not Married X 15.104 2.339 6.459 0
23 Married or domestic partnership LinkedIn - Not Married LinkedIn 7.443 2.532 2.940 0.065
24 Married or domestic partnership LinkedIn - Married or domestic partnership X 9.153 2.643 3.464 0.013
25 Married or domestic partnership LinkedIn - Not Married X 15.165 2.503 6.058 0.00000
26 Not Married LinkedIn - Married or domestic partnership X 1.709 2.548 0.671 0.998
27 Not Married LinkedIn - Not Married X 7.721 2.403 3.213 0.029
28 Married or domestic partnership X - Not Married X 6.012 2.520 2.386 0.248
Table S34: Full reporting of the comparative statistics of Figure 1E in the main text: Pairwise
Comparisons of TPV for the different Platforms and different Relationship Status. Relation-
ship statuses are grouped into Married or Not Married.Highlighted contrastsare significant
at the 1% level. DF=9387.
S6.1.6 Figure 1E: Total Platform Valuation by Platform & Relationship Status, Aggre-
gated over all platforms
contrast estimate ($) SE t-stat p-value
1 Single, not looking for a relationship - Single, looking for a relationship 4.913 1.956 2.512 0.058
2 Single, not looking for a relationship - In a serious relationship 6.659 2.102 3.168 0.008
3 Single, not looking for a relationship - Married or domestic partnership -1.491 1.661 -0.897 0.806
4 Single, looking for a relationship - In a serious relationship 1.746 2.107 0.828 0.841
5 Single, looking for a relationship - Married or domestic partnership -6.404 1.668 -3.840 0.001
6 In a serious relationship - Married or domestic partnership -8.149 1.837 -4.437 0.0001
91

Table S35: Full reporting of the comparative statistics of Figure 1E in the main text: Pairwise
Comparisons of the average over all platforms TPV for the different Relationship Statuses.
Highlighted contrastsare significant at the 1% level. DF=9289.
92

S6.1.7 Figure 2A: Connection Value Percentile by Platform & How Ego Knows Alter,
Aggregated to Three Relationship Types
contrast estimate SE t.ratio p.value
1 Family member or family friend Facebook - Work, school or university Facebook 5.428 0.362 14.995 0
2 Family member or family friend Facebook - Online or shared interest Facebook 7.392 0.427 17.331 0
3 Family member or family friend Facebook - Family member or family friend Instagram -2.701 0.554 -4.878 0.0001
4 Family member or family friend Facebook - Work, school or university Instagram 2.154 0.537 4.009 0.004
5 Family member or family friend Facebook - Online or shared interest Instagram 1.644 0.584 2.814 0.174
6 Family member or family friend Facebook - Family member or family friend LinkedIn -0.918 0.650 -1.412 0.961
7 Family member or family friend Facebook - Work, school or university LinkedIn 2.445 0.480 5.090 0.00002
8 Family member or family friend Facebook - Online or shared interest LinkedIn 6.041 0.626 9.650 0
9 Family member or family friend Facebook - Family member or family friend X -0.047 0.527 -0.090 1
10 Family member or family friend Facebook - Work, school or university X 3.492 0.394 8.854 0
11 Family member or family friend Facebook - Online or shared interest X 3.579 0.438 8.165 0
12 Work, school or university Facebook - Online or shared interest Facebook 1.964 0.425 4.626 0.0002
13 Work, school or university Facebook - Family member or family friend Instagram -8.129 0.552 -14.720 0
14 Work, school or university Facebook - Work, school or university Instagram -3.274 0.536 -6.111 0.00000
15 Work, school or university Facebook - Online or shared interest Instagram -3.784 0.583 -6.491 0
16 Work, school or university Facebook - Family member or family friend LinkedIn -6.346 0.649 -9.780 0
17 Work, school or university Facebook - Work, school or university LinkedIn -2.983 0.479 -6.232 0.00000
18 Work, school or university Facebook - Online or shared interest LinkedIn 0.613 0.625 0.982 0.998
19 Work, school or university Facebook - Family member or family friend X -5.475 0.525 -10.422 0
20 Work, school or university Facebook - Work, school or university X -1.936 0.392 -4.934 0.0001
21 Work, school or university Facebook - Online or shared interest X -1.849 0.436 -4.236 0.001
22 Online or shared interest Facebook - Family member or family friend Instagram -10.093 0.597 -16.919 0
23 Online or shared interest Facebook - Work, school or university Instagram -5.238 0.581 -9.010 0
24 Online or shared interest Facebook - Online or shared interest Instagram -5.748 0.625 -9.196 0
25 Online or shared interest Facebook - Family member or family friend LinkedIn -8.310 0.687 -12.097 0
26 Online or shared interest Facebook - Work, school or university LinkedIn -4.947 0.529 -9.349 0
27 Online or shared interest Facebook - Online or shared interest LinkedIn -1.350 0.664 -2.033 0.671
28 Online or shared interest Facebook - Family member or family friend X -7.439 0.572 -13.012 0
29 Online or shared interest Facebook - Work, school or university X -3.900 0.453 -8.617 0
30 Online or shared interest Facebook - Online or shared interest X -3.813 0.491 -7.760 0
31 Family member or family friend Instagram - Work, school or university Instagram 4.855 0.680 7.138 0
32 Family member or family friend Instagram - Online or shared interest Instagram 4.346 0.718 6.053 0.00000
33 Family member or family friend Instagram - Family member or family friend LinkedIn 1.783 0.772 2.309 0.470
34 Family member or family friend Instagram - Work, school or university LinkedIn 5.146 0.636 8.090 0
35 Family member or family friend Instagram - Online or shared interest LinkedIn 8.743 0.752 11.622 0
36 Family member or family friend Instagram - Family member or family friend X 2.654 0.672 3.950 0.004
37 Family member or family friend Instagram - Work, school or university X 6.194 0.574 10.790 0
38 Family member or family friend Instagram - Online or shared interest X 6.281 0.605 10.380 0
39 Work, school or university Instagram - Online or shared interest Instagram -0.510 0.705 -0.723 1.000
40 Work, school or university Instagram - Family member or family friend LinkedIn -3.072 0.761 -4.038 0.003
41 Work, school or university Instagram - Work, school or university LinkedIn 0.291 0.622 0.468 1.000
42 Work, school or university Instagram - Online or shared interest LinkedIn 3.888 0.740 5.252 0.00001
43 Work, school or university Instagram - Family member or family friend X -2.201 0.659 -3.342 0.040
44 Work, school or university Instagram - Work, school or university X 1.338 0.558 2.398 0.407
45 Work, school or university Instagram - Online or shared interest X 1.425 0.590 2.416 0.395
46 Online or shared interest Instagram - Family member or family friend LinkedIn -2.562 0.795 -3.225 0.057
47 Online or shared interest Instagram - Work, school or university LinkedIn 0.801 0.663 1.208 0.988
48 Online or shared interest Instagram - Online or shared interest LinkedIn 4.397 0.775 5.674 0.00000
49 Online or shared interest Instagram - Family member or family friend X -1.692 0.697 -2.425 0.388
50 Online or shared interest Instagram - Work, school or university X 1.848 0.604 3.062 0.092
51 Online or shared interest Instagram - Online or shared interest X 1.935 0.633 3.056 0.093
52 Family member or family friend LinkedIn - Work, school or university LinkedIn 3.363 0.722 4.660 0.0002
53 Family member or family friend LinkedIn - Online or shared interest LinkedIn 6.960 0.826 8.428 0
54 Family member or family friend LinkedIn - Family member or family friend X 0.871 0.753 1.156 0.992
55 Family member or family friend LinkedIn - Work, school or university X 4.410 0.668 6.607 0
56 Family member or family friend LinkedIn - Online or shared interest X 4.497 0.694 6.477 0
57 Work, school or university LinkedIn - Online or shared interest LinkedIn 3.596 0.700 5.138 0.00002
58 Work, school or university LinkedIn - Family member or family friend X -2.492 0.613 -4.066 0.003
59 Work, school or university LinkedIn - Work, school or university X 1.047 0.504 2.080 0.638
60 Work, school or university LinkedIn - Online or shared interest X 1.134 0.539 2.106 0.619
61 Online or shared interest LinkedIn - Family member or family friend X -6.089 0.733 -8.310 0
62 Online or shared interest LinkedIn - Work, school or university X -2.549 0.644 -3.958 0.004
63 Online or shared interest LinkedIn - Online or shared interest X -2.462 0.672 -3.665 0.013
64 Family member or family friend X - Work, school or university X 3.540 0.548 6.457 0
65 Family member or family friend X - Online or shared interest X 3.627 0.581 6.246 0.00000
66 Work, school or university X - Online or shared interest X 0.087 0.464 0.188 1
93

Table S36: Full reporting of the comparative statistics of Figure 2A in the main text where we
group the way Ego knows Alter into 3 bins: A. Online or shared interest, B. Work, school or
university and C. Family member or family friend.Highlighted contrastsare significant at
the 1% level. DF = 70755.
S6.1.8 Figure 2A: Connection Value Percentile by Platform & How Ego Knows Alter,
Aggregated over all platforms
contrast estimate(%) SE t-stat p-value
1 I only know them online - None of these describe how I know this person -1.279 0.615 -2.081 0.364
2 I only know them online - School (K-12) -2.317 0.484 -4.782 0.00004
3 I only know them online - Work -2.412 0.421 -5.726 0.00000
4 I only know them online - Through a shared interest in real life -2.904 0.459 -6.332 0
5 I only know them online - College or University -3.260 0.458 -7.126 0
6 I only know them online - Family member or family friend -7.132 0.396 -17.991 0
7 None of these describe how I know this person - School (K-12) -1.038 0.611 -1.699 0.617
8 None of these describe how I know this person - Work -1.134 0.562 -2.017 0.404
9 None of these describe how I know this person - Through a shared interest in real life -1.625 0.590 -2.752 0.086
10 None of these describe how I know this person - College or University -1.982 0.590 -3.361 0.014
11 None of these describe how I know this person - Family member or family friend -5.853 0.544 -10.768 0
12 School (K-12) - Work -0.096 0.416 -0.231 1.000
13 School (K-12) - Through a shared interest in real life -0.587 0.453 -1.296 0.854
14 School (K-12) - College or University -0.944 0.452 -2.087 0.360
15 School (K-12) - Family member or family friend -4.816 0.390 -12.337 0
16 Work - Through a shared interest in real life -0.492 0.385 -1.276 0.863
17 Work - College or University -0.848 0.384 -2.209 0.290
18 Work - Family member or family friend -4.720 0.309 -15.298 0
19 Through a shared interest in real life - College or University -0.356 0.425 -0.839 0.981
20 Through a shared interest in real life - Family member or family friend -4.228 0.358 -11.814 0
21 College or University - Family member or family friend -3.872 0.356 -10.861 0
Table S37: Full reporting of the comparative statistics of Figure 2A in the main text: Pairwise
Comparisons of the average over all platforms CVP for the different ways Ego know Alter.
Highlighted contrastsare significant at the 1% level. DF = 70760.
94

S6.1.9 Figure 2B: Connection Value Percentile by Platform & Frequency of Meeting
Alter, Aggregated to Three Meeting Frequencies
contrast estimate(%) SE df t-stat p-value
1 Never Facebook - I live with this person Facebook -22.322 0.688 70,755 -32.463 0
2 Never Facebook - Sometimes Facebook -8.080 0.455 70,755 -17.775 0
3 Never Facebook - Never Instagram -8.448 0.716 70,755 -11.805 0
4 Never Facebook - I live with this person Instagram -21.667 1.136 70,755 -19.080 0
5 Never Facebook - Sometimes Instagram -11.524 0.539 70,755 -21.385 0
6 Never Facebook - Never LinkedIn -5.832 0.705 70,755 -8.267 0
7 Never Facebook - I live with this person LinkedIn -16.898 1.368 70,755 -12.353 0
8 Never Facebook - Sometimes LinkedIn -10.046 0.541 70,755 -18.572 0
9 Never Facebook - Never X -7.017 0.619 70,755 -11.335 0
10 Never Facebook - I live with this person X -17.738 0.951 70,755 -18.647 0
11 Never Facebook - Sometimes X -8.948 0.479 70,755 -18.683 0
12 I live with this person Facebook - Sometimes Facebook 14.242 0.576 70,755 24.730 0
13 I live with this person Facebook - Never Instagram 13.874 0.798 70,755 17.380 0
14 I live with this person Facebook - I live with this person Instagram 0.655 1.189 70,755 0.551 1.000
15 I live with this person Facebook - Sometimes Instagram 10.798 0.645 70,755 16.753 0
16 I live with this person Facebook - Never LinkedIn 16.490 0.789 70,755 20.897 0
17 I live with this person Facebook - I live with this person LinkedIn 5.424 1.413 70,755 3.839 0.007
18 I live with this person Facebook - Sometimes LinkedIn 12.276 0.646 70,755 18.995 0
19 I live with this person Facebook - Never X 15.305 0.713 70,755 21.468 0
20 I live with this person Facebook - I live with this person X 4.584 1.015 70,755 4.517 0.0004
21 I live with this person Facebook - Sometimes X 13.374 0.595 70,755 22.465 0
22 Sometimes Facebook - Never Instagram -0.368 0.609 70,755 -0.605 1.000
23 Sometimes Facebook - I live with this person Instagram -13.587 1.072 70,755 -12.679 0
24 Sometimes Facebook - Sometimes Instagram -3.444 0.386 70,755 -8.915 0
25 Sometimes Facebook - Never LinkedIn 2.248 0.597 70,755 3.765 0.009
26 Sometimes Facebook - I live with this person LinkedIn -8.818 1.315 70,755 -6.704 0
27 Sometimes Facebook - Sometimes LinkedIn -1.966 0.389 70,755 -5.052 0.00003
28 Sometimes Facebook - Never X 1.063 0.492 70,755 2.161 0.579
29 Sometimes Facebook - I live with this person X -9.658 0.874 70,755 -11.051 0
30 Sometimes Facebook - Sometimes X -0.868 0.297 70,755 -2.922 0.133
31 Never Instagram - I live with this person Instagram -13.219 1.206 70,755 -10.962 0
32 Never Instagram - Sometimes Instagram -3.076 0.674 70,755 -4.561 0.0003
33 Never Instagram - Never LinkedIn 2.616 0.814 70,755 3.215 0.059
34 Never Instagram - I live with this person LinkedIn -8.449 1.427 70,755 -5.922 0.00000
35 Never Instagram - Sometimes LinkedIn -1.598 0.676 70,755 -2.364 0.431
36 Never Instagram - Never X 1.431 0.740 70,755 1.934 0.738
37 Never Instagram - I live with this person X -9.289 1.034 70,755 -8.983 0
38 Never Instagram - Sometimes X -0.499 0.628 70,755 -0.796 1.000
39 I live with this person Instagram - Sometimes Instagram 10.143 1.110 70,755 9.137 0
40 I live with this person Instagram - Never LinkedIn 15.835 1.200 70,755 13.198 0
41 I live with this person Instagram - I live with this person LinkedIn 4.769 1.677 70,755 2.844 0.162
42 I live with this person Instagram - Sometimes LinkedIn 11.621 1.111 70,755 10.459 0
43 I live with this person Instagram - Never X 14.650 1.151 70,755 12.727 0
44 I live with this person Instagram - I live with this person X 3.929 1.359 70,755 2.892 0.144
45 I live with this person Instagram - Sometimes X 12.719 1.082 70,755 11.753 0
46 Sometimes Instagram - Never LinkedIn 5.692 0.664 70,755 8.578 0
47 Sometimes Instagram - I live with this person LinkedIn -5.374 1.347 70,755 -3.990 0.004
48 Sometimes Instagram - Sometimes LinkedIn 1.478 0.485 70,755 3.047 0.095
49 Sometimes Instagram - Never X 4.507 0.571 70,755 7.896 0
50 Sometimes Instagram - I live with this person X -6.213 0.921 70,755 -6.750 0
51 Sometimes Instagram - Sometimes X 2.576 0.415 70,755 6.212 0.00000
52 Never LinkedIn - I live with this person LinkedIn -11.066 1.422 70,755 -7.784 0
53 Never LinkedIn - Sometimes LinkedIn -4.214 0.665 70,755 -6.335 0.00000
54 Never LinkedIn - Never X -1.185 0.730 70,755 -1.623 0.901
55 Never LinkedIn - I live with this person X -11.906 1.027 70,755 -11.593 0
56 Never LinkedIn - Sometimes X -3.116 0.616 70,755 -5.059 0.00003
57 I live with this person LinkedIn - Sometimes LinkedIn 6.851 1.348 70,755 5.084 0.00002
58 I live with this person LinkedIn - Never X 9.881 1.381 70,755 7.156 0
59 I live with this person LinkedIn - I live with this person X -0.840 1.558 70,755 -0.539 1.000
60 I live with this person LinkedIn - Sometimes X 7.950 1.324 70,755 6.005 0.00000
61 Sometimes LinkedIn - Never X 3.029 0.573 70,755 5.289 0.00001
62 Sometimes LinkedIn - I live with this person X -7.691 0.922 70,755 -8.344 0
63 Sometimes LinkedIn - Sometimes X 1.099 0.417 70,755 2.632 0.262
64 Never X - I live with this person X -10.721 0.970 70,755 -11.056 0
65 Never X - Sometimes X -1.931 0.515 70,755 -3.752 0.010
66 I live with this person X - Sometimes X 8.790 0.887 70,755 9.912 0
95

Table S38: Full reporting of the comparative statistics of Figure 2B in the main text where we
group frequency of meets with alter to Never or Sometimes or I Live with Alter.Highlighted
contrastsare significant at the 1% level. DF = 70755.
S6.1.10 Figure 2B: Connection Value Percentile by Platform & Frequency of Meeting
Alter, Aggregated Across All Platforms
contrast estimate(%) SE t-stat p-value
1 Never - Less than 4 times/year -2.468 0.347 -7.105 0
2 Never - About once a month -4.027 0.358 -11.253 0
3 Never - About once a week -4.531 0.369 -12.273 0
4 Never - Multiple times per week -6.145 0.330 -18.645 0
5 Never - I live with this person -16.084 0.471 -34.118 0
6 Less than 4 times/year - About once a month -1.559 0.357 -4.363 0.0002
7 Less than 4 times/year - About once a week -2.063 0.369 -5.595 0.00000
8 Less than 4 times/year - Multiple times per week -3.677 0.329 -11.174 0
9 Less than 4 times/year - I live with this person -13.616 0.471 -28.904 0
10 About once a month - About once a week -0.504 0.379 -1.330 0.768
11 About once a month - Multiple times per week -2.118 0.340 -6.227 0
12 About once a month - I live with this person -12.056 0.479 -25.178 0
13 About once a week - Multiple times per week -1.614 0.352 -4.586 0.0001
14 About once a week - I live with this person -11.553 0.487 -23.704 0
15 Multiple times per week - I live with this person -9.939 0.458 -21.696 0
Table S39: Full reporting of the comparative statistics of Figure 2B in the main text: Pairwise
Comparisons of the average over all platforms CVP for the different frequencies of meeting
with Alter.Highlighted contrastsare significant at the 1% level. DF = 70761.
S6.1.11 Figure 2C: Connection Value Percentile by Whether You Are Connected with
Alter on Another Platform, Aggregated Across All Platforms
contrast estimate SE t-stat p-value
1 No - Yes -2.392 0.272 -8.798 0
Table S40: Full reporting of the comparative statistics of Figure 2C in the main text: Pairwise
Comparisons of the average over all platforms CVP for whether Ego is connected to Alter on
other platform or Not.Highlighted contrastsare significant at the 1% level. DF = 70765.
96

S6.1.12 Figure 3A: Connection Value Percentile by Platform & Gender, Aggregated by
Alter Gender
contrast estimate (%) SE t-stat p-value
1 Alter Female Facebook - Alter Male Facebook 1.009 0.325 3.101 0.041
2 Alter Female Facebook - Alter Female Instagram -3.389 0.449 -7.548 0
3 Alter Female Facebook - Alter Male Instagram -2.081 0.507 -4.104 0.001
4 Alter Female Facebook - Alter Female LinkedIn -1.905 0.503 -3.791 0.004
5 Alter Female Facebook - Alter Male LinkedIn 0.104 0.467 0.223 1.000
6 Alter Female Facebook - Alter Female X -1.304 0.397 -3.282 0.023
7 Alter Female Facebook - Alter Male X 0.297 0.360 0.826 0.992
8 Alter Male Facebook - Alter Female Instagram -4.398 0.451 -9.748 0
9 Alter Male Facebook - Alter Male Instagram -3.089 0.509 -6.071 0.00000
10 Alter Male Facebook - Alter Female LinkedIn -2.914 0.504 -5.776 0.00000
11 Alter Male Facebook - Alter Male LinkedIn -0.905 0.469 -1.930 0.530
12 Alter Male Facebook - Alter Female X -2.312 0.400 -5.786 0.00000
13 Alter Male Facebook - Alter Male X -0.711 0.363 -1.960 0.509
14 Alter Female Instagram - Alter Male Instagram 1.309 0.596 2.197 0.353
15 Alter Female Instagram - Alter Female LinkedIn 1.484 0.592 2.507 0.192
16 Alter Female Instagram - Alter Male LinkedIn 3.493 0.562 6.219 0
17 Alter Female Instagram - Alter Female X 2.086 0.506 4.126 0.001
18 Alter Female Instagram - Alter Male X 3.687 0.477 7.731 0
19 Alter Male Instagram - Alter Female LinkedIn 0.175 0.637 0.275 1.000
20 Alter Male Instagram - Alter Male LinkedIn 2.184 0.609 3.587 0.008
21 Alter Male Instagram - Alter Female X 0.777 0.558 1.393 0.861
22 Alter Male Instagram - Alter Male X 2.378 0.532 4.472 0.0002
23 Alter Female LinkedIn - Alter Male LinkedIn 2.009 0.605 3.319 0.020
24 Alter Female LinkedIn - Alter Female X 0.602 0.554 1.087 0.960
25 Alter Female LinkedIn - Alter Male X 2.203 0.528 4.175 0.001
26 Alter Male LinkedIn - Alter Female X -1.408 0.521 -2.701 0.122
27 Alter Male LinkedIn - Alter Male X 0.194 0.493 0.392 1.000
28 Alter Female X - Alter Male X 1.601 0.428 3.737 0.005
Table S41: Full reporting of the comparative statistics of Figure 3A in the main text where
we group gender mix into 2 bins: A. Alter Female, B. Alter Male.Highlighted contrastsare
significant at the 1% level. DF = 67575.
S6.1.13 Figure 3A: Connection Value Percentile by Whether You relative Ego and Alter
Gender, Aggregated Across All Platforms
97

contrast estimate (%) SE t-stat p-value
1 (Ego Male / Alter Male) - (Ego Female / Alter Female) -1.719 0.274 -6.266 0
2 (Ego Male / Alter Male) - (Ego Female / Alter Male) -1.873 0.318 -5.892 0.00000
3 (Ego Male / Alter Male) - (Ego Male / Alter Female) -2.863 0.333 -8.608 0
4 (Ego Female / Alter Female) - (Ego Female / Alter Male) -0.154 0.318 -0.485 0.962
5 (Ego Female / Alter Female) - (Ego Male / Alter Female) -1.145 0.332 -3.443 0.003
6 (Ego Female / Alter Male) - (Ego Male / Alter Female) -0.990 0.369 -2.682 0.037
Table S42: Full reporting of the comparative statistics of Figure 3A in the main text: Pairwise
Comparisons of the average over all platforms CVP for the different Gender mix of Ego and
Alter.Highlighted contrastsare significant at the 1% level. DF = 67579.
S6.1.14 Figure 3B: Connection Value Percentile by Platform & Race, Aggregated to
Alter Race
contrast estimate (%) SE t-stat p-value
1 Alter White Facebook - (Alter non-White Facebook) 0.447 0.342 1.307 0.897
2 Alter White Facebook - Alter White Instagram -3.472 0.441 -7.880 0
3 Alter White Facebook - (Alter non-White Instagram) -2.923 0.500 -5.847 0.00000
4 Alter White Facebook - Alter White LinkedIn -0.813 0.426 -1.907 0.546
5 Alter White Facebook - (Alter non-White LinkedIn) -1.957 0.568 -3.445 0.013
6 Alter White Facebook - Alter White X -0.647 0.345 -1.878 0.566
7 Alter White Facebook - (Alter non-White X) -0.913 0.386 -2.367 0.258
8 (Alter non-White Facebook) - Alter White Instagram -3.919 0.479 -8.185 0
9 (Alter non-White Facebook) - (Alter non-White Instagram) -3.370 0.534 -6.311 0
10 (Alter non-White Facebook) - Alter White LinkedIn -1.260 0.466 -2.706 0.121
11 (Alter non-White Facebook) - (Alter non-White LinkedIn) -2.404 0.598 -4.018 0.002
12 (Alter non-White Facebook) - Alter White X -1.094 0.392 -2.789 0.098
13 (Alter non-White Facebook) - (Alter non-White X) -1.360 0.429 -3.171 0.033
14 Alter White Instagram - (Alter non-White Instagram) 0.549 0.602 0.912 0.985
15 Alter White Instagram - Alter White LinkedIn 2.659 0.542 4.906 0.00003
16 Alter White Instagram - (Alter non-White LinkedIn) 1.514 0.660 2.296 0.296
17 Alter White Instagram - Alter White X 2.824 0.481 5.875 0.00000
18 Alter White Instagram - (Alter non-White X) 2.559 0.511 5.008 0.00002
19 (Alter non-White Instagram) - Alter White LinkedIn 2.111 0.591 3.569 0.009
20 (Alter non-White Instagram) - (Alter non-White LinkedIn) 0.966 0.701 1.378 0.867
21 (Alter non-White Instagram) - Alter White X 2.276 0.536 4.248 0.001
22 (Alter non-White Instagram) - (Alter non-White X) 2.010 0.563 3.571 0.009
23 Alter White LinkedIn - (Alter non-White LinkedIn) -1.145 0.650 -1.761 0.647
24 Alter White LinkedIn - Alter White X 0.165 0.467 0.353 1.000
25 Alter White LinkedIn - (Alter non-White X) -0.100 0.498 -0.201 1.000
26 (Alter non-White LinkedIn) - Alter White X 1.310 0.600 2.184 0.362
27 (Alter non-White LinkedIn) - (Alter non-White X) 1.044 0.624 1.673 0.705
28 Alter White X - (Alter non-White X) -0.266 0.431 -0.616 0.999
98

Table S43: Full reporting of the comparative statistics of Figure 3B in the main text where we
group gender mix into 2 bins: A. Alter White, B. Alter non-WhiteHighlighted contrastsare
significant at the 1% level. DF = 66770
S6.1.15 Figure 3B: Connection Value Percentile by Whether You relative Race of Ego
and Alter, Aggregated Across All Platforms
contrast estimate (%) SE t-stat p-value
1 Ego&Alter both Whites - (Ego White - Alter Non-White) 1.354 0.330 4.105 0.0002
2 Ego & Alter both Whites - (Ego Non-White - Alter White) 1.203 0.445 2.702 0.035
3 Ego & Alter both Whites - (Both Ego and Alter Non-Whites) -0.669 0.273 -2.453 0.067
4 (Ego White - Alter Non-White) - (Ego Non-White - Alter White) -0.151 0.512 -0.295 0.991
5 (Ego White - Alter Non-White) - (Both Ego and Alter Non-Whites) -2.023 0.373 -5.429 0.00000
6 (Ego Non-White - Alter White) - (Both Ego and Alter Non-Whites) -1.871 0.478 -3.918 0.001
Table S44: Full reporting of the comparative statistics of Figure 3B in the main text: Pairwise
Comparisons of the average over all platforms CVP for the different Race mix between Alter
and Ego groups.Highlighted contrastsare significant at the 1% level. DF = 66774.
S6.1.16 Figure 3C: Connection Value Percentile by Whether You relative Age of Ego
and Alter, Aggregated Across All Platforms
contrast estimate (%) SE t-stat p-value
1 ego younger than alter - ego same age as alter -0.241 0.270 -0.893 0.645
2 ego younger than alter - ego older than alter -0.176 0.293 -0.600 0.820
3 ego same age as alter - ego older than alter 0.065 0.261 0.251 0.966
Table S45: Full reporting of the comparative statistics of Figure 3C in the main text: Pairwise
Comparisons of Connection Value Percentile between different Age mix of Ego and Alter for
the different platforms.Highlighted contrastsare significant at the 1% level. DF = 67965.
99

S6.1.17 Figure 3D: Connection Value Percentile by Platform & Alter Age, Aggregated
to Alter Over or Under Age 18
contrast estimate (%) SE t-stat p-value
1 Alter under 18 years old Facebook- Alter over 18 years old Facebook 0.724 0.935 0.775 0.994
2 Alter under 18 years old Facebook- Alter under 18 years old Instagram -6.907 1.590 -4.345 0.0004
3 Alter under 18 years old Facebook- Alter over 18 years old Instagram -2.497 0.966 -2.585 0.161
4 Alter under 18 years old Facebook- Alter under 18 years old LinkedIn -1.105 2.576 -0.429 1.000
5 Alter under 18 years old Facebook- Alter over 18 years old LinkedIn -0.483 0.966 -0.500 1.000
6 Alter under 18 years old Facebook- Alter under 18 years old X -3.539 1.561 -2.266 0.312
7 Alter under 18 years old Facebook- Alter over 18 years old X -0.162 0.943 -0.172 1.000
8 Alter over 18 years old Facebook- Alter under 18 years old Instagram -7.632 1.306 -5.842 0.00000
9 Alter over 18 years old Facebook- Alter over 18 years old Instagram -3.221 0.336 -9.597 0
10 Alter over 18 years old Facebook- Alter under 18 years old LinkedIn -1.829 2.412 -0.759 0.995
11 Alter over 18 years old Facebook- Alter over 18 years old LinkedIn -1.208 0.335 -3.608 0.007
12 Alter over 18 years old Facebook- Alter under 18 years old X -4.263 1.272 -3.352 0.018
13 Alter over 18 years old Facebook- Alter over 18 years old X -0.887 0.264 -3.355 0.018
14 Alter under 18 years old Instagram - Alter over 18 years old Instagram 4.411 1.329 3.319 0.020
15 Alter under 18 years old Instagram - Alter under 18 years old LinkedIn 5.802 2.733 2.123 0.400
16 Alter under 18 years old Instagram - Alter over 18 years old LinkedIn 6.424 1.329 4.835 0.00004
17 Alter under 18 years old Instagram - Alter under 18 years old X 3.369 1.809 1.862 0.577
18 Alter under 18 years old Instagram - Alter over 18 years old X 6.745 1.313 5.138 0.00001
19 Alter over 18 years old Instagram - Alter under 18 years old LinkedIn 1.392 2.424 0.574 0.999
20 Alter over 18 years old Instagram - Alter over 18 years old LinkedIn 2.014 0.414 4.861 0.00003
21 Alter over 18 years old Instagram - Alter under 18 years old X -1.042 1.295 -0.805 0.993
22 Alter over 18 years old Instagram - Alter over 18 years old X 2.335 0.360 6.488 0
23 Alter under 18 years old LinkedIn - Alter over 18 years old LinkedIn 0.622 2.424 0.257 1.000
24 Alter under 18 years old LinkedIn - Alter under 18 years old X -2.434 2.717 -0.896 0.987
25 Alter under 18 years old LinkedIn - Alter over 18 years old X 0.943 2.415 0.390 1.000
26 Alter over 18 years old LinkedIn - Alter under 18 years old X -3.056 1.295 -2.360 0.261
27 Alter over 18 years old LinkedIn - Alter over 18 years old X 0.321 0.359 0.894 0.987
28 Alter under 18 years old X - Alter over 18 years old X 3.377 1.279 2.641 0.141
Table S46: Full reporting of the comparative statistics of Figure 3D in the main text where we
group Alter Age into 2 bins: A. Below 18 yo, B. Alter over 18 yo.Highlighted contrastsare
significant at the 1% level. DF = 70759
100

S6.1.18 Figure 3D: Connection Value Percentile by Platform & Alter Age, Aggregated
Across All Platforms
contrast estimate (%) SE t-stat p-value
1 Under 18 years old - (18-24 years old) 1.644 0.669 2.459 0.137
2 Under 18 years old - (25-34 years old) 2.214 0.653 3.393 0.009
3 Under 18 years old - (35-44 years old) 2.353 0.664 3.545 0.005
4 Under 18 years old - (45-54 years old) 3.135 0.705 4.445 0.0001
5 Under 18 years old - 55 years or older 1.466 0.724 2.025 0.328
6 (18-24 years old) - (25-34 years old) 0.570 0.308 1.854 0.431
7 (18-24 years old) - (35-44 years old) 0.710 0.331 2.144 0.265
8 (18-24 years old) - (45-54 years old) 1.491 0.408 3.658 0.003
9 (18-24 years old) - 55 years or older -0.178 0.440 -0.404 0.999
10 (25-34 years old) - (35-44 years old) 0.139 0.297 0.468 0.997
11 (25-34 years old) - (45-54 years old) 0.921 0.381 2.418 0.150
12 (25-34 years old) - 55 years or older -0.748 0.415 -1.803 0.463
13 (35-44 years old) - (45-54 years old) 0.781 0.400 1.954 0.369
14 (35-44 years old) - 55 years or older -0.887 0.432 -2.052 0.313
15 (45-54 years old) - 55 years or older -1.669 0.493 -3.381 0.009
Table S47: Full reporting of the comparative statistics of Figure 3D in the main text: Pairwise
Comparisons of the average over all platforms CVP for the different Alter Age groups.High-
lighted contrastsare significant at the 1% level. DF = 67971
101

S6.2 All Statistical Comparisons
In this section we present estimated differences, and associated p-values, for every pair of
respondent types in Figures 1 through 4.
S6.2.1 Figure 1B: Average Total Platform Valuation by Platform and Average Total
Platform Valuation that is attributed to the local network effects by Platform
contrast estimate ($) SE t-test p-value
1 Facebook - Instagram 9.598 1.684 5.701 0.00000
2 Facebook - LinkedIn 14.007 1.738 8.061 0
3 Facebook - X 22.500 1.730 13.005 0
4 Instagram - LinkedIn 4.409 1.735 2.541 0.054
5 Instagram - X 12.901 1.727 7.470 0
6 LinkedIn - X 8.493 1.780 4.772 0.00001
Table S48: Full comparative statistics of Figure 1B in the main text: Pairwise Comparisons of
the average TPVfor the different platforms.Highlighted contrastsare significant at the 1%
level. DF = 9391.
contrast estimate ($) SE t-stat p-value
1 Facebook - Instagram -4.637 3.175 -1.460 0.144
2 Facebook-LinkedIn 10.960 2.945 3.721 0.0002
3 Facebook-X 10.877 3.121 3.485 0.0005
4 Instagram-LinkedIn 15.597 3.001 5.197 0.00000
5 Instagram-X 15.513 3.174 4.888 0.00000
6 LinkedIn - X 0.083 2.943 0.028 0.977
Table S49: Full comparative statistics of Figure 1B in the main text: Pairwise Comparisons
of theaverage TPV that is attributed to local network effectsfor the different platforms.
Highlighted contrastsare significant at the 1% level. DF = 9391.
contrast estimate (%) SE t-stat p-value
1 Facebook - Instagram -7.815 3.367 -2.321 0.020
2 Facebook-LinkedIn 8.427 3.161 2.666 0.008
3 Facebook - X 6.417 3.593 1.786 0.074
4 Instagram-LinkedIn 16.243 3.398 4.780 0.00000
5 Instagram-X 14.232 3.803 3.743 0.0002
6 LinkedIn - X -2.010 3.622 -0.555 0.579
Table S50: Full comparative statistics of Figure 1B in the main text: Pairwise Comparisons
of the% of TPV attributed to the local network effectsfor the different platforms.High-
lighted contrastsare significant at the 1% level. DF = 9391.
102

S6.2.2 Figure 1C: Total Platform Valuation by Platform & Usage Levels
contrast usage estimate ($) SE t-stat p-value
1 Facebook - Instagram Less than 10 minutes per day 11.745 4.519 2.599 0.046
2 Facebook - LinkedIn Less than 10 minutes per day 3.889 3.760 1.034 0.729
3 Facebook - X Less than 10 minutes per day 14.676 4.317 3.399 0.004
4 Instagram - LinkedIn Less than 10 minutes per day -7.857 3.805 -2.065 0.165
5 Instagram - X Less than 10 minutes per day 2.930 4.356 0.673 0.907
6 LinkedIn - X Less than 10 minutes per day 10.787 3.562 3.028 0.013
7 Facebook - Instagram 10–30 minutes per day 13.881 3.962 3.503 0.003
8 Facebook - LinkedIn 10–30 minutes per day 12.528 5.016 2.497 0.060
9 Facebook - X 10–30 minutes per day 29.675 4.196 7.073 0
10 Instagram - LinkedIn 10–30 minutes per day -1.353 5.000 -0.271 0.993
11 Instagram - X 10–30 minutes per day 15.795 4.176 3.782 0.001
12 LinkedIn - X 10–30 minutes per day 17.148 5.187 3.306 0.005
13 Facebook - Instagram 31–60 minutes per day 9.442 3.098 3.048 0.012
14 Facebook - LinkedIn 31–60 minutes per day 4.052 3.103 1.306 0.559
15 Facebook - X 31–60 minutes per day 23.367 3.176 7.359 0
16 Instagram - LinkedIn 31–60 minutes per day -5.390 2.968 -1.816 0.266
17 Instagram - X 31–60 minutes per day 13.925 3.044 4.574 0.00003
18 LinkedIn - X 31–60 minutes per day 19.315 3.049 6.334 0
19 Facebook - Instagram 1–2 hours per day 12.850 5.486 2.342 0.089
20 Facebook - LinkedIn 1–2 hours per day 16.183 8.339 1.941 0.211
21 Facebook - X 1–2 hours per day 22.021 5.708 3.858 0.001
22 Instagram - LinkedIn 1–2 hours per day 3.333 8.586 0.388 0.980
23 Instagram - X 1–2 hours per day 9.171 6.064 1.513 0.430
24 LinkedIn - X 1–2 hours per day 5.838 8.729 0.669 0.909
25 Facebook - Instagram 2–3 hours per day 4.854 3.629 1.338 0.539
26 Facebook - LinkedIn 2–3 hours per day 1.542 4.217 0.366 0.983
27 Facebook - X 2–3 hours per day 12.592 3.681 3.421 0.004
28 Instagram - LinkedIn 2–3 hours per day -3.312 4.174 -0.793 0.857
29 Instagram - X 2–3 hours per day 7.738 3.632 2.130 0.144
30 LinkedIn - X 2–3 hours per day 11.049 4.220 2.618 0.044
31 Facebook - Instagram More than 3 hours per day -3.049 5.197 -0.587 0.936
32 Facebook - LinkedIn More than 3 hours per day 34.246 10.056 3.406 0.004
33 Facebook - X More than 3 hours per day 14.033 6.294 2.230 0.115
34 Instagram - LinkedIn More than 3 hours per day 37.295 10.225 3.647 0.002
35 Instagram - X More than 3 hours per day 17.082 6.561 2.604 0.046
36 LinkedIn - X More than 3 hours per day -20.214 10.824 -1.867 0.242
Table S51: Full reporting of the comparative statistics of Figure 1C in the main text: Pairwise
Comparisons of TPV for the different Platforms within Usage Levels.Highlighted contrasts
are significant at the 1% level. DF=9371.
103

contrast platform estimate ($) SE t-stat p-value
1 Less than 10 minutes per day - 10–30 minutes per day Facebook -34.148 4.240 -8.054 0
2 Less than 10 minutes per day - 31–60 minutes per day Facebook -13.902 3.905 -3.560 0.005
3 Less than 10 minutes per day - 1–2 hours per day Facebook -30.799 4.796 -6.422 0
4 Less than 10 minutes per day - 2–3 hours per day Facebook -16.677 4.099 -4.068 0.001
5 Less than 10 minutes per day - More than 3 hours per day Facebook -36.230 4.672 -7.754 0
6 10–30 minutes per day - 31–60 minutes per day Facebook 20.246 3.625 5.586 0.00000
7 10–30 minutes per day - 1–2 hours per day Facebook 3.350 4.570 0.733 0.978
8 10–30 minutes per day - 2–3 hours per day Facebook 17.471 3.833 4.558 0.0001
9 10–30 minutes per day - More than 3 hours per day Facebook -2.082 4.441 -0.469 0.997
10 31–60 minutes per day - 1–2 hours per day Facebook -16.896 4.262 -3.965 0.001
11 31–60 minutes per day - 2–3 hours per day Facebook -2.775 3.460 -0.802 0.967
12 31–60 minutes per day - More than 3 hours per day Facebook -22.328 4.122 -5.416 0.00000
13 1–2 hours per day - 2–3 hours per day Facebook 14.121 4.441 3.180 0.018
14 1–2 hours per day - More than 3 hours per day Facebook -5.431 4.974 -1.092 0.885
15 2–3 hours per day - More than 3 hours per day Facebook -19.553 4.307 -4.540 0.0001
16 Less than 10 minutes per day - 10–30 minutes per day Instagram -32.013 4.260 -7.514 0
17 Less than 10 minutes per day - 31–60 minutes per day Instagram -16.206 3.844 -4.216 0.0004
18 Less than 10 minutes per day - 1–2 hours per day Instagram -29.694 5.246 -5.660 0.00000
19 Less than 10 minutes per day - 2–3 hours per day Instagram -23.568 4.097 -5.752 0.00000
20 Less than 10 minutes per day - More than 3 hours per day Instagram -51.025 5.060 -10.084 0
21 10–30 minutes per day - 31–60 minutes per day Instagram 15.807 3.487 4.533 0.0001
22 10–30 minutes per day - 1–2 hours per day Instagram 2.319 4.991 0.465 0.997
23 10–30 minutes per day - 2–3 hours per day Instagram 8.445 3.765 2.243 0.218
24 10–30 minutes per day - More than 3 hours per day Instagram -19.012 4.795 -3.965 0.001
25 31–60 minutes per day - 1–2 hours per day Instagram -13.489 4.641 -2.907 0.043
26 31–60 minutes per day - 2–3 hours per day Instagram -7.363 3.286 -2.241 0.219
27 31–60 minutes per day - More than 3 hours per day Instagram -34.819 4.429 -7.862 0
28 1–2 hours per day - 2–3 hours per day Instagram 6.126 4.853 1.262 0.806
29 1–2 hours per day - More than 3 hours per day Instagram -21.330 5.689 -3.749 0.002
30 2–3 hours per day - More than 3 hours per day Instagram -27.456 4.651 -5.904 0.00000
31 Less than 10 minutes per day - 10–30 minutes per day LinkedIn -25.509 4.618 -5.524 0.00000
32 Less than 10 minutes per day - 31–60 minutes per day LinkedIn -13.739 2.918 -4.708 0.00004
33 Less than 10 minutes per day - 1–2 hours per day LinkedIn -18.504 7.789 -2.376 0.165
34 Less than 10 minutes per day - 2–3 hours per day LinkedIn -19.024 3.888 -4.893 0.00001
35 Less than 10 minutes per day - More than 3 hours per day LinkedIn -5.873 9.666 -0.608 0.991
36 10–30 minutes per day - 31–60 minutes per day LinkedIn 11.771 4.653 2.530 0.116
37 10–30 minutes per day - 1–2 hours per day LinkedIn 7.005 8.591 0.815 0.965
38 10–30 minutes per day - 2–3 hours per day LinkedIn 6.486 5.315 1.220 0.827
39 10–30 minutes per day - More than 3 hours per day LinkedIn 19.637 10.323 1.902 0.401
40 31–60 minutes per day - 1–2 hours per day LinkedIn -4.766 7.810 -0.610 0.990
41 31–60 minutes per day - 2–3 hours per day LinkedIn -5.285 3.930 -1.345 0.760
42 31–60 minutes per day - More than 3 hours per day LinkedIn 7.866 9.683 0.812 0.965
43 1–2 hours per day - 2–3 hours per day LinkedIn -0.519 8.222 -0.063 1.000
44 1–2 hours per day - More than 3 hours per day LinkedIn 12.632 12.079 1.046 0.902
45 2–3 hours per day - More than 3 hours per day LinkedIn 13.151 10.018 1.313 0.778
46 Less than 10 minutes per day - 10–30 minutes per day X -19.149 4.274 -4.480 0.0001
47 Less than 10 minutes per day - 31–60 minutes per day X -5.211 3.670 -1.420 0.715
48 Less than 10 minutes per day - 1–2 hours per day X -23.453 5.312 -4.415 0.0001
49 Less than 10 minutes per day - 2–3 hours per day X -18.761 3.922 -4.783 0.00003
50 Less than 10 minutes per day - More than 3 hours per day X -36.873 6.035 -6.110 0.00000
51 10–30 minutes per day - 31–60 minutes per day X 13.938 3.814 3.654 0.004
52 10–30 minutes per day - 1–2 hours per day X -4.304 5.412 -0.795 0.968
53 10–30 minutes per day - 2–3 hours per day X 0.388 4.057 0.096 1.000
54 10–30 minutes per day - More than 3 hours per day X -17.724 6.123 -2.895 0.044
55 31–60 minutes per day - 1–2 hours per day X -18.242 4.950 -3.686 0.003
56 31–60 minutes per day - 2–3 hours per day X -13.550 3.416 -3.967 0.001
57 31–60 minutes per day - More than 3 hours per day X -31.662 5.719 -5.537 0.00000
58 1–2 hours per day - 2–3 hours per day X 4.692 5.139 0.913 0.943
59 1–2 hours per day - More than 3 hours per day X -13.420 6.888 -1.948 0.373
60 2–3 hours per day - More than 3 hours per day X -18.112 5.883 -3.079 0.025
104

Table S52: Full reporting of the comparative statistics of Figure 1C in the main text: Pair- wise
Comparisons of TPV for the different Usage Levels within Platforms.Highlighted contrasts
are significant at the 1% level. DF= 9371.
105

S6.2.3 Figure 1D: Total Platform Valuation by Platform & Political Orientation
contrast political estimate ($) SE t-stat p-value
1 Facebook - Instagram Extremely liberal 6.435 5.423 1.187 0.635
2 Facebook - LinkedIn Extremely liberal 10.433 5.410 1.929 0.216
3 Facebook - X Extremely liberal 20.973 5.552 3.777 0.001
4 Instagram - LinkedIn Extremely liberal 3.998 5.632 0.710 0.893
5 Instagram - X Extremely liberal 14.538 5.769 2.520 0.057
6 LinkedIn - X Extremely liberal 10.540 5.756 1.831 0.259
7 Facebook - Instagram Liberal 15.621 4.806 3.250 0.006
8 Facebook - LinkedIn Liberal 19.333 4.798 4.029 0.0003
9 Facebook - X Liberal 22.035 4.751 4.638 0.00002
10 Instagram - LinkedIn Liberal 3.713 4.834 0.768 0.869
11 Instagram - X Liberal 6.414 4.787 1.340 0.537
12 LinkedIn - X Liberal 2.702 4.779 0.565 0.942
13 Facebook - Instagram Slightly liberal 16.459 6.566 2.507 0.059
14 Facebook - LinkedIn Slightly liberal 19.371 7.059 2.744 0.031
15 Facebook - X Slightly liberal 12.827 6.392 2.007 0.186
16 Instagram - LinkedIn Slightly liberal 2.913 7.512 0.388 0.980
17 Instagram - X Slightly liberal -3.631 6.889 -0.527 0.953
18 LinkedIn - X Slightly liberal -6.544 7.361 -0.889 0.811
19 Facebook - Instagram Moderate 5.993 4.341 1.381 0.512
20 Facebook - LinkedIn Moderate 7.063 4.485 1.575 0.393
21 Facebook - X Moderate 20.380 4.436 4.595 0.00003
22 Instagram - LinkedIn Moderate 1.069 4.210 0.254 0.994
23 Instagram - X Moderate 14.387 4.157 3.4610.003
24 LinkedIn - X Moderate 13.317 4.307 3.092 0.011
25 Facebook - Instagram Slightly conservative 10.609 2.715 3.908 0.001
26 Facebook - LinkedIn Slightly conservative 15.351 2.873 5.343 0.00000
27 Facebook - X Slightly conservative 24.598 2.872 8.564 0
28 Instagram - LinkedIn Slightly conservative 4.743 2.881 1.646 0.353
29 Instagram - X Slightly conservative 13.990 2.880 4.857 0.00001
30 LinkedIn - X Slightly conservative 9.247 3.030 3.052 0.012
31 Facebook - Instagram Conservative 2.518 5.540 0.455 0.969
32 Facebook - LinkedIn Conservative 12.376 5.546 2.231 0.115
33 Facebook - X Conservative 22.350 5.634 3.967 0.0004
34 Instagram - LinkedIn Conservative 9.858 5.613 1.756 0.295
35 Instagram - X Conservative 19.832 5.699 3.480 0.003
36 LinkedIn - X Conservative 9.974 5.706 1.748 0.299
37 Facebook - Instagram Extremely conservative 6.791 5.790 1.173 0.644
38 Facebook - LinkedIn Extremely conservative 10.596 5.922 1.789 0.279
39 Facebook - X Extremely conservative 24.336 5.956 4.086 0.0003
40 Instagram - LinkedIn Extremely conservative 3.805 5.613 0.678 0.905
41 Instagram - X Extremely conservative 17.546 5.649 3.106 0.010
42 LinkedIn - X Extremely conservative 13.740 5.785 2.375 0.082
106

Table S53: Full reporting of the comparative statistics of Figure 1D in the main text: Pairwise
Comparisons of TPV for the different Platforms Within Political Groups.Highlighted con-
trastsare significant at the 1% level. DF=9367.
107

contrast platform estimate ($) SE t-stat p-value
1 Extremely liberal - Liberal Facebook -9.152 4.986-1.836 0.524
2 Extremely liberal - Slightly liberal Facebook -9.952 5.633-1.767 0.571
3 Extremely liberal - Moderate Facebook -1.209 4.909-0.246 1.000
4 Extremely liberal - Slightly conservative Facebook -9.754 4.140-2.356 0.218
5 Extremely liberal - Conservative Facebook1.278 5.334 0.240 1.000
6 Extremely liberal - Extremely conservative Facebook1.474 5.659 0.261 1.000
7 Liberal - Slightly liberal Facebook -0.799 5.443-0.147 1.000
8 Liberal - Moderate Facebook7.944 4.690 1.694 0.620
9 Liberal - Slightly conservative Facebook -0.601 3.878-0.155 1.000
10 Liberal - Conservative Facebook10.430 5.134 2.032 0.395
11 Liberal - Extremely conservative Facebook10.627 5.470 1.943 0.452
12 Slightly liberal - Moderate Facebook8.743 5.373 1.627 0.665
13 Slightly liberal - Slightly conservative Facebook0.198 4.681 0.042 1
14 Slightly liberal - Conservative Facebook11.229 5.764 1.948 0.448
15 Slightly liberal - Extremely conservative Facebook11.426 6.066 1.884 0.491
16 Moderate - Slightly conservative Facebook -8.545 3.779-2.261 0.263
17 Moderate - Conservative Facebook2.486 5.059 0.491 0.999
18 Moderate - Extremely conservative Facebook2.683 5.400 0.497 0.999
19 Slightly conservative - Conservative Facebook11.031 4.317 2.555 0.140
20 Slightly conservative - Extremely conservative Facebook11.228 4.712 2.383 0.206
21 Conservative - Extremely conservative Facebook0.196 5.790 0.034 1
22 Extremely liberal - Liberal Instagram0.033 5.258 0.006 1
23 Extremely liberal - Slightly liberal Instagram0.072 6.386 0.011 1
24 Extremely liberal - Moderate Instagram -1.651 4.915-0.336 1.000
25 Extremely liberal - Slightly conservative Instagram -5.580 4.432-1.259 0.870
26 Extremely liberal - Conservative Instagram -2.640 5.625-0.469 0.999
27 Extremely liberal - Extremely conservative Instagram1.830 5.559 0.329 1.000
28 Liberal - Slightly liberal Instagram0.039 6.048 0.006 1
29 Liberal - Moderate Instagram -1.683 4.466-0.377 1.000
30 Liberal - Slightly conservative Instagram -5.613 3.928-1.429 0.786
31 Liberal - Conservative Instagram -2.672 5.238-0.510 0.999
32 Liberal - Extremely conservative Instagram1.797 5.167 0.348 1.000
33 Slightly liberal - Moderate Instagram -1.723 5.752-0.299 1.000
34 Slightly liberal - Slightly conservative Instagram -5.652 5.344-1.058 0.940
35 Slightly liberal - Conservative Instagram -2.712 6.369-0.426 1.000
36 Slightly liberal - Extremely conservative Instagram1.758 6.311 0.278 1.000
37 Moderate - Slightly conservative Instagram -3.930 3.455-1.137 0.917
38 Moderate - Conservative Instagram -0.989 4.893-0.202 1.000
39 Moderate - Extremely conservative Instagram3.480 4.817 0.722 0.991
40 Slightly conservative - Conservative Instagram2.941 4.407 0.667 0.994
41 Slightly conservative - Extremely conservative Instagram7.410 4.323 1.714 0.606
42 Conservative - Extremely conservative Instagram4.469 5.540 0.807 0.984
43 Extremely liberal - Liberal LinkedIn -0.253 5.237-0.048 1
44 Extremely liberal - Slightly liberal LinkedIn -1.014 6.882-0.147 1.000
45 Extremely liberal - Moderate LinkedIn -4.579 5.028-0.911 0.971
46 Extremely liberal - Slightly conservative LinkedIn -4.836 4.514-1.071 0.937
47 Extremely liberal - Conservative LinkedIn3.221 5.619 0.573 0.998
48 Extremely liberal - Extremely conservative LinkedIn1.637 5.685 0.288 1.000
49 Liberal - Slightly liberal LinkedIn -0.761 6.574-0.116 1.000
50 Liberal - Moderate LinkedIn -4.327 4.598-0.941 0.966
51 Liberal - Slightly conservative LinkedIn -4.583 4.029-1.137 0.917
52 Liberal - Conservative LinkedIn3.473 5.237 0.663 0.995
53 Liberal - Extremely conservative LinkedIn1.889 5.308 0.356 1.000
54 Slightly liberal - Moderate LinkedIn -3.566 6.409-0.556 0.998
55 Slightly liberal - Slightly conservative LinkedIn -3.822 6.014-0.636 0.996
56 Slightly liberal - Conservative LinkedIn4.234 6.882 0.615 0.996
57 Slightly liberal - Extremely conservative LinkedIn2.650 6.936 0.382 1.000
58 Moderate - Slightly conservative LinkedIn -0.256 3.754-0.068 1
59 Moderate - Conservative LinkedIn7.800 5.028 1.551 0.713
60 Moderate - Extremely conservative LinkedIn6.216 5.102 1.218 0.887
61 Slightly conservative - Conservative LinkedIn8.056 4.514 1.785 0.559
62 Slightly conservative - Extremely conservative LinkedIn6.473 4.596 1.408 0.798
63 Conservative - Extremely conservative LinkedIn -1.584 5.685-0.279 1.000
64 Extremely liberal - Liberal X -8.091 5.343-1.514 0.736
65 Extremely liberal - Slightly liberal X -18.097 6.321-2.863 0.064
66 Extremely liberal - Moderate X -1.802 5.139-0.351 1.000
67 Extremely liberal - Slightly conservative X -6.129 4.684-1.309 0.848
68 Extremely liberal - Conservative X2.655 5.841 0.454 0.999
69 Extremely liberal - Extremely conservative X4.837 5.855 0.826 0.982
70 Liberal - Slightly liberal X -10.007 5.814-1.721 0.602
71 Liberal - Moderate X6.289 4.500 1.397 0.803
72 Liberal - Slightly conservative X1.962 3.973 0.494 0.999
73 Liberal - Conservative X10.745 5.288 2.032 0.394
74 Liberal - Extremely conservative X12.928 5.303 2.438 0.183
75 Slightly liberal - Moderate X16.295 5.627 2.896 0.058
76 Slightly liberal - Slightly conservative X11.969 5.215 2.295 0.246
77 Slightly liberal - Conservative X20.752 6.275 3.307 0.016
78 Slightly liberal - Extremely conservative X 22.935 6.288 3.647 0.005
79 Moderate - Slightly conservative X -4.327 3.694-1.171 0.905
80 Moderate - Conservative X4.457 5.082 0.877 0.976
81 Moderate - Extremely conservative X6.639 5.098 1.302 0.851
82 Slightly conservative - Conservative X8.783 4.621 1.901 0.480
83 Slightly conservative - Extremely conservative X10.966 4.639 2.364 0.214
84 Conservative - Extremely conservative X2.183 5.805 0.376 1.000
108

Table S54: Full reporting of the comparative statistics of Figure 1D in the main text: Pairwise
Comparisons of TPV for the different Political Groups within Platforms.Highlighted con-
trastsare significant at the 1% level. DF=9367.
109

S6.2.4 Figure 1E: Total Platform Valuation by Platform & Relationship Status
contrast Relationship Status estimate ($) SE t-stat p-value
1 Facebook - Instagram Single, not looking for a relationship 7.701 3.799 2.027 0.178
2 Facebook - LinkedIn Single, not looking for a relationship 10.237 3.793 2.699 0.035
3 Facebook - X Single, not looking for a relationship 21.463 3.717 5.774 0.00000
4 Instagram - LinkedIn Single, not looking for a relationship 2.536 4.054 0.625 0.924
5 Instagram - X Single, not looking for a relationship 13.762 3.983 3.455 0.003
6 LinkedIn - X Single, not looking for a relationship 11.226 3.978 2.822 0.025
7 Facebook - Instagram Single, looking for a relationship 7.496 3.804 1.970 0.199
8 Facebook - LinkedIn Single, looking for a relationship 16.315 3.880 4.205 0.0002
9 Facebook - X Single, looking for a relationship 19.894 3.852 5.165 0.00000
10 Instagram - LinkedIn Single, looking for a relationship 8.819 3.929 2.244 0.112
11 Instagram - X Single, looking for a relationship 12.398 3.902 3.177 0.008
12 LinkedIn - X Single, looking for a relationship 3.579 3.976 0.900 0.805
13 Facebook - Instagram In a serious relationship 3.898 4.182 0.932 0.788
14 Facebook - LinkedIn In a serious relationship 16.657 4.552 3.659 0.001
15 Facebook - X In a serious relationship 26.086 4.446 5.868 0.00000
16 Instagram - LinkedIn In a serious relationship 12.759 4.521 2.822 0.025
17 Instagram - X In a serious relationship 22.189 4.414 5.027 0.00000
18 LinkedIn - X In a serious relationship 9.430 4.766 1.978 0.196
19 Facebook - Instagram Married or domestic partnership 13.997 2.560 5.468 0.00000
20 Facebook - LinkedIn Married or domestic partnership 14.923 2.645 5.642 0.00000
21 Facebook - X Married or domestic partnership 24.076 2.661 9.048 0
22 Instagram - LinkedIn Married or domestic partnership 0.927 2.536 0.365 0.983
23 Instagram - X Married or domestic partnership 10.079 2.552 3.950 0.0005
24 LinkedIn - X Married or domestic partnership 9.153 2.638 3.470 0.003
Table S55: Full reporting of the comparative statistics of Figure 1E in the main text: Pairwise
Comparisons of TPV for the different Platforms within Relationship Status.Highlighted con-
trastsare significant at the 1% level. DF = 9277.
110

contrast Platform estimate ($) SE t-stat p-value
1 Single, not looking for a relationship - Single, looking for a relationship Facebook3.671 3.638 1.009 0.744
2 Single, not looking for a relationship - In a serious relationship Facebook5.475 3.883 1.410 0.493
3 Single, not looking for a relationship - Married or domestic partnership Facebook -5.491 3.123-1.758 0.294
4 Single, looking for a relationship - In a serious relationship Facebook1.804 3.991 0.452 0.969
5 Single, looking for a relationship - Married or domestic partnership Facebook -9.162 3.256-2.814 0.025
6 In a serious relationship - Married or domestic partnership Facebook -10.966 3.528-3.108 0.010
7 Single, not looking for a relationship - Single, looking for a relationship Instagram3.466 3.958 0.876 0.818
8 Single, not looking for a relationship - In a serious relationship Instagram1.671 4.103 0.407 0.977
9 Single, not looking for a relationship - Married or domestic partnership Instagram0.804 3.351 0.240 0.995
10 Single, looking for a relationship - In a serious relationship Instagram -1.794 4.004-0.448 0.970
11 Single, looking for a relationship - Married or domestic partnership Instagram -2.661 3.228-0.824 0.843
12 In a serious relationship - Married or domestic partnership Instagram -0.867 3.405-0.255 0.994
13 Single, not looking for a relationship - Single, looking for a relationship LinkedIn9.749 4.026 2.422 0.073
14 Single, not looking for a relationship - In a serious relationship LinkedIn11.894 4.476 2.657 0.039
15 Single, not looking for a relationship - Married or domestic partnership LinkedIn -0.804 3.411-0.236 0.995
16 Single, looking for a relationship - In a serious relationship LinkedIn2.146 4.455 0.482 0.963
17 Single, looking for a relationship - Married or domestic partnership LinkedIn -10.553 3.383 -3.119 0.010
18 In a serious relationship - Married or domestic partnership LinkedIn -12.699 3.908 -3.249 0.006
19 Single, not looking for a relationship - Single, looking for a relationship X 2.102 3.927 0.535 0.950
20 Single, not looking for a relationship - In a serious relationship X 10.098 4.302 2.347 0.088
21 Single, not looking for a relationship - Married or domestic partnership X -2.878 3.339 -0.862 0.824
22 Single, looking for a relationship - In a serious relationship X 7.996 4.321 1.850 0.250
23 Single, looking for a relationship - Married or domestic partnership X -4.980 3.364 -1.480 0.449
24 In a serious relationship - Married or domestic partnership X -12.976 3.795 -3.419 0.004
Table S56: Full reporting of the comparative statistics of Figure 1E in the main text: Pairwise
Comparisons of TPV for the different Relationship Statuses within Platforms.Highlighted
contrastsare significant at the 1% level. DF=9277.
S6.2.5 Figure 1F: Total Platform Valuation by Platform & Job Seeking
contrast platform estimate ($) SE t-stat p-value
1 Job Seekers - Non Job Seekers Facebook -9.472 2.623 -3.612 0.0003
2 Job Seekers - Non Job Seekers Instagram 0.052 2.542 0.020 0.984
3 Job Seekers - Non Job Seekers LinkedIn 8.330 2.612 3.189 0.001
4 Job Seekers - Non Job Seekers X -2.528 2.735 -0.924 0.355
Table S57: Full reporting of the comparative statistics of Figure 1F in the main text: Pairwise
Comparisons of the TPV between job seekers and non job seekers for the different platforms.
Highlighted contrastsare significant at the 1% level. DF=9387.
111

S6.2.6 Figure 2A: Connection Value Percentile by Platform & How You Know Alter
contrast Platform estimate(%) SE t-stat p-value
1 I only know them online - None of these describe how I know this person Facebook -3.937 1.061 -3.712 0.004
2 I only know them online - School (K-12) Facebook -4.109 0.814 -5.048 0.00001
3 I only know them online - Work Facebook -4.826 0.748 -6.453 0
4 I only know them online - Through a shared interest in real life Facebook -4.419 0.789 -5.603 0.00000
5 I only know them online - College or University Facebook -6.339 0.799 -7.931 0
6 I only know them online - Family member or family friend Facebook -10.505 0.694 -15.134 0
7 None of these describe how I know this person - School (K-12) Facebook -0.172 0.978 -0.176 1.000
8 None of these describe how I know this person - Work Facebook -0.889 0.924 -0.963 0.962
9 None of these describe how I know this person - Through a shared interest in real life Facebook -0.482 0.957 -0.503 0.999
10 None of these describe how I know this person - College or University Facebook -2.402 0.966 -2.487 0.164
11 None of these describe how I know this person - Family member or family friend Facebook -6.568 0.881 -7.457 0
12 School (K-12) - Work Facebook -0.717 0.625 -1.147 0.913
13 School (K-12) - Through a shared interest in real life Facebook -0.310 0.673 -0.460 0.999
14 School (K-12) - College or University Facebook -2.230 0.686 -3.251 0.020
15 School (K-12) - Family member or family friend Facebook -6.396 0.560 -11.423 0
16 Work - Through a shared interest in real life Facebook 0.408 0.592 0.689 0.993
17 Work - College or University Facebook -1.513 0.606 -2.497 0.160
18 Work - Family member or family friend Facebook -5.678 0.458 -12.389 0
19 Through a shared interest in real life - College or University Facebook -1.920 0.655 -2.930 0.053
20 Through a shared interest in real life - Family member or family friend Facebook -6.086 0.522 -11.656 0
21 College or University - Family member or family friend Facebook -4.166 0.538 -7.742 0
22 I only know them online - None of these describe how I know this person Instagram -2.272 1.535 -1.480 0.757
23 I only know them online - School (K-12) Instagram -2.224 1.105 -2.012 0.407
24 I only know them online - Work Instagram -0.405 1.147 -0.353 1.000
25 I only know them online - Through a shared interest in real life Instagram -4.600 1.146 -4.015 0.001
26 I only know them online - College or University Instagram -3.045 1.235 -2.466 0.172
27 I only know them online - Family member or family friend Instagram -6.670 0.952 -7.006 0
28 None of these describe how I know this person - School (K-12) Instagram 0.048 1.498 0.032 1
29 None of these describe how I know this person - Work Instagram 1.867 1.530 1.220 0.886
30 None of these describe how I know this person - Through a shared interest in real life Instagram -2.328 1.529 -1.523 0.731
31 None of these describe how I know this person - College or University Instagram -0.773 1.597 -0.484 0.999
32 None of these describe how I know this person - Family member or family friend Instagram -4.398 1.389 -3.166 0.026
33 School (K-12) - Work Instagram 1.818 1.098 1.656 0.646
34 School (K-12) - Through a shared interest in real life Instagram -2.376 1.096 -2.167 0.313
35 School (K-12) - College or University Instagram -0.822 1.189 -0.691 0.993
36 School (K-12) - Family member or family friend Instagram -4.446 0.892 -4.985 0.00001
37 Work - Through a shared interest in real life Instagram -4.195 1.139 -3.684 0.004
38 Work - College or University Instagram -2.640 1.229 -2.149 0.324
39 Work - Family member or family friend Instagram -6.265 0.944 -6.640 0
40 Through a shared interest in real life - College or University Instagram 1.555 1.227 1.267 0.867
41 Through a shared interest in real life - Family member or family friend Instagram -2.070 0.942 -2.198 0.296
42 College or University - Family member or family friend Instagram -3.625 1.049 -3.457 0.010
43 I only know them online - None of these describe how I know this person LinkedIn -0.581 1.494 -0.389 1.000
44 I only know them online - School (K-12) LinkedIn -2.927 1.512 -1.936 0.456
45 I only know them online - Work LinkedIn -5.292 1.153 -4.590 0.0001
46 I only know them online - Through a shared interest in real life LinkedIn -2.907 1.356 -2.143 0.327
47 I only know them online - College or University LinkedIn -5.252 1.296 -4.051 0.001
48 I only know them online - Family member or family friend LinkedIn -8.328 1.189 -7.007 0
49 None of these describe how I know this person - School (K-12) LinkedIn -2.345 1.550 -1.513 0.737
50 None of these describe how I know this person - Work LinkedIn -4.710 1.203 -3.916 0.002
51 None of these describe how I know this person - Through a shared interest in real life LinkedIn -2.325 1.399 -1.662 0.642
52 None of these describe how I know this person - College or University LinkedIn -4.670 1.341 -3.482 0.009
53 None of these describe how I know this person - Family member or family friend LinkedIn -7.747 1.237 -6.261 0
54 School (K-12) - Work LinkedIn -2.365 1.225 -1.931 0.460
55 School (K-12) - Through a shared interest in real life LinkedIn 0.020 1.418 0.014 1
56 School (K-12) - College or University LinkedIn -2.325 1.361 -1.708 0.610
57 School (K-12) - Family member or family friend LinkedIn -5.402 1.259 -4.291 0.0004
58 Work - Through a shared interest in real life LinkedIn 2.385 1.027 2.322 0.233
59 Work - College or University LinkedIn 0.040 0.947 0.042 1
60 Work - Family member or family friend LinkedIn -3.036 0.793 -3.831 0.002
61 Through a shared interest in real life - College or University LinkedIn -2.345 1.186 -1.977 0.429
62 Through a shared interest in real life - Family member or family friend LinkedIn -5.421 1.067 -5.080 0.00001
63 College or University - Family member or family friend LinkedIn -3.076 0.990 -3.107 0.031
64 I only know them online - None of these describe how I know this person X -0.371 1.118 -0.332 1.000
65 I only know them online - School (K-12) X -2.540 0.876 -2.901 0.057
66 I only know them online - Work X -0.990 0.690 -1.435 0.783
67 I only know them online - Through a shared interest in real life X -2.878 0.760 -3.786 0.003
68 I only know them online - College or University X -1.240 0.733 -1.692 0.621
69 I only know them online - Family member or family friend X -4.903 0.703 -6.971 0
70 None of these describe how I know this person - School (K-12) X -2.170 1.204 -1.802 0.546
71 None of these describe how I know this person - Work X -0.619 1.076 -0.575 0.997
72 None of these describe how I know this person - Through a shared interest in real life X -2.507 1.123 -2.233 0.277
73 None of these describe how I know this person - College or University X -0.869 1.104 -0.787 0.986
74 None of these describe how I know this person - Family member or family friend X -4.532 1.085 -4.178 0.001
75 School (K-12) - Work X 1.551 0.822 1.887 0.489
76 School (K-12) - Through a shared interest in real life X -0.338 0.882 -0.383 1.000
77 School (K-12) - College or University X 1.300 0.858 1.515 0.736
78 School (K-12) - Family member or family friend X -2.363 0.833 -2.836 0.069
79 Work - Through a shared interest in real life X -1.889 0.698 -2.708 0.096
80 Work - College or University X -0.250 0.667 -0.375 1.000
81 Work - Family member or family friend X -3.914 0.635 -6.164 0.00000
82 Through a shared interest in real life - College or University X 1.638 0.740 2.213 0.288
83 Through a shared interest in real life - Family member or family friend X -2.025 0.711 -2.848 0.066
84 College or University - Family member or family friend X -3.663 0.682 -5.375 0.00000
112

Table S58: Full reporting of the comparative statistics of Figure 2A in the main text: Pairwise
Comparisons of Connection Value Percentile between different ways that Ego knows Alter for
the different platforms.Highlighted contrastsare significant at the 1% level. DF = 70739
contrast How do you know Alter? estimate(%) SE t-stat p-value
1 Facebook - Instagram I only know them online -6.54 1.04 -6.28 0.00
2 Facebook - LinkedIn I only know them online -3.09 1.21 -2.55 0.05
3 Facebook - X I only know them online -5.65 0.84 -6.76 0.00
4 Instagram - LinkedIn I only know them online 3.44 1.31 2.62 0.04
5 Instagram - X I only know them online 0.89 0.97 0.91 0.80
6 LinkedIn - X I only know them online -2.55 1.16 -2.21 0.12
7 Facebook - Instagram None of these describe how I know this person -4.87 1.55 -3.14 0.01
8 Facebook - LinkedIn None of these describe how I know this person 0.26 1.37 0.19 1.00
9 Facebook - X None of these describe how I know this person -2.08 1.29 -1.61 0.37
10 Instagram - LinkedIn None of these describe how I know this person 5.13 1.69 3.03 0.01
11 Instagram - X None of these describe how I know this person 2.79 1.63 1.71 0.32
12 LinkedIn - X None of these describe how I know this person -2.34 1.46 -1.60 0.38
13 Facebook - Instagram School (K-12) -4.65 0.90 -5.19 0.00
14 Facebook - LinkedIn School (K-12) -1.91 1.21 -1.57 0.39
15 Facebook - X School (K-12) -4.08 0.85 -4.77 0.00
16 Instagram - LinkedIn School (K-12) 2.74 1.34 2.05 0.17
17 Instagram - X School (K-12) 0.57 1.02 0.56 0.94
18 LinkedIn - X School (K-12) -2.17 1.31 -1.66 0.35
19 Facebook - Instagram Work -2.11 0.89 -2.37 0.08
20 Facebook - LinkedIn Work -3.56 0.65 -5.52 0.00
21 Facebook - X Work -1.81 0.58 -3.13 0.01
22 Instagram - LinkedIn Work -1.45 0.96 -1.50 0.43
23 Instagram - X Work 0.30 0.92 0.33 0.99
24 LinkedIn - X Work 1.75 0.68 2.57 0.05
25 Facebook - Instagram Through a shared interest in real life -6.72 0.92 -7.27 0.00
26 Facebook - LinkedIn Through a shared interest in real life -1.58 0.99 -1.59 0.38
27 Facebook - X Through a shared interest in real life -4.11 0.71 -5.81 0.00
28 Instagram - LinkedIn Through a shared interest in real life 5.13 1.20 4.29 0.00
29 Instagram - X Through a shared interest in real life 2.61 0.97 2.69 0.04
30 LinkedIn - X Through a shared interest in real life -2.53 1.04 -2.43 0.07
31 Facebook - Instagram College or University -3.24 1.04 -3.12 0.01
32 Facebook - LinkedIn College or University -2.01 0.92 -2.18 0.13
33 Facebook - X College or University -0.55 0.69 -0.80 0.86
34 Instagram - LinkedIn College or University 1.23 1.22 1.01 0.74
35 Instagram - X College or University 2.69 1.05 2.55 0.05
36 LinkedIn - X College or University 1.46 0.94 1.56 0.40
37 Facebook - Instagram Family member or family friend -2.70 0.55 -4.88 0.00
38 Facebook - LinkedIn Family member or family friend -0.92 0.65 -1.41 0.49
39 Facebook - X Family member or family friend -0.05 0.53 -0.09 1.00
40 Instagram - LinkedIn Family member or family friend 1.78 0.77 2.31 0.10
41 Instagram - X Family member or family friend 2.65 0.67 3.95 0.00
42 LinkedIn - X Family member or family friend 0.87 0.75 1.16 0.65
113

Table S59: Full reporting of the comparative statistics of Figure 2A in the main text: Pairwise
Comparisons of Connection Value Percentile for the different Platforms for different ways that
Ego knows Alter.Highlighted contrastsare significant at the 1% level. DF = 70739.
114

S6.2.7 Figure 2B: Connection Value Percentile by Platform & Frequency of Meeting
Alter
contrast Platform estimate(%) SE t-stat p-value
1 Never - Less than 4 times/year) Facebook -5.12 0.54 -9.41 0.00
2 Never - About once a month Facebook -7.25 0.56 -12.84 0.00
3 Never - About once a week Facebook -9.02 0.58 -15.50 0.00
4 Never - Multiple times per week Facebook -10.61 0.53 -20.11 0.00
5 Never - I live with this person Facebook -22.32 0.69 -32.50 0.00
6 Less than 4 times/year) - About once a month Facebook -2.13 0.52 -4.11 0.00
7 Less than 4 times/year) - About once a week Facebook -3.89 0.54 -7.26 0.00
8 Less than 4 times/year) - Multiple times per week Facebook -5.49 0.48 -11.49 0.00
9 Less than 4 times/year) - I live with this person Facebook -17.20 0.65 -26.50 0.00
10 About once a month - About once a week Facebook -1.77 0.56 -3.17 0.02
11 About once a month - Multiple times per week Facebook -3.36 0.50 -6.72 0.00
12 About once a month - I live with this person Facebook -15.07 0.67 -22.63 0.00
13 About once a week - Multiple times per week Facebook -1.59 0.52 -3.06 0.03
14 About once a week - I live with this person Facebook -13.30 0.68 -19.55 0.00
15 Multiple times per week - I live with this person Facebook -11.71 0.63 -18.45 0.00
16 Never - Less than 4 times/year) Instagram -1.33 0.87 -1.54 0.64
17 Never - About once a month Instagram -3.78 0.90 -4.19 0.00
18 Never - About once a week Instagram -1.78 0.98 -1.82 0.45
19 Never - Multiple times per week Instagram -5.02 0.86 -5.84 0.00
20 Never - I live with this person Instagram -13.22 1.20 -10.98 0.00
21 Less than 4 times/year) - About once a month Instagram -2.45 0.94 -2.60 0.10
22 Less than 4 times/year) - About once a week Instagram -0.45 1.02 -0.44 1.00
23 Less than 4 times/year) - Multiple times per week Instagram -3.69 0.90 -4.09 0.00
24 Less than 4 times/year) - I live with this person Instagram -11.89 1.23 -9.63 0.00
25 About once a month - About once a week Instagram 2.00 1.05 1.90 0.40
26 About once a month - Multiple times per week Instagram -1.24 0.94 -1.32 0.77
27 About once a month - I live with this person Instagram -9.44 1.26 -7.48 0.00
28 About once a week - Multiple times per week Instagram -3.24 1.01 -3.19 0.02
29 About once a week - I live with this person Instagram -11.44 1.32 -8.67 0.00
30 Multiple times per week - I live with this person Instagram -8.20 1.23 -6.66 0.00
31 Never - Less than 4 times/year) LinkedIn -3.37 0.86 -3.90 0.00
32 Never - About once a month LinkedIn -3.57 0.93 -3.85 0.00
33 Never - About once a week LinkedIn -3.61 1.00 -3.62 0.00
34 Never - Multiple times per week LinkedIn -5.74 0.83 -6.90 0.00
35 Never - I live with this person LinkedIn -11.07 1.42 -7.79 0.00
36 Less than 4 times/year) - About once a month LinkedIn -0.20 0.98 -0.21 1.00
37 Less than 4 times/year) - About once a week LinkedIn -0.24 1.05 -0.23 1.00
38 Less than 4 times/year) - Multiple times per week LinkedIn -2.37 0.89 -2.66 0.08
39 Less than 4 times/year) - I live with this person LinkedIn -7.70 1.45 -5.29 0.00
40 About once a month - About once a week LinkedIn -0.04 1.10 -0.03 1.00
41 About once a month - Multiple times per week LinkedIn -2.17 0.95 -2.28 0.20
42 About once a month - I live with this person LinkedIn -7.50 1.49 -5.02 0.00
43 About once a week - Multiple times per week LinkedIn -2.13 1.02 -2.09 0.29
44 About once a week - I live with this person LinkedIn -7.46 1.54 -4.85 0.00
45 Multiple times per week - I live with this person LinkedIn -5.33 1.44 -3.71 0.00
46 Never - Less than 4 times/year) X -1.24 0.69 -1.79 0.47
47 Never - About once a month X -1.79 0.68 -2.65 0.09
48 Never - About once a week X -1.79 0.67 -2.67 0.08
49 Never - Multiple times per week X -2.54 0.61 -4.16 0.00
50 Never - I live with this person X -10.72 0.97 -11.07 0.00
51 Less than 4 times/year) - About once a month X -0.56 0.72 -0.78 0.97
52 Less than 4 times/year) - About once a week X -0.56 0.71 -0.78 0.97
53 Less than 4 times/year) - Multiple times per week X -1.30 0.65 -1.99 0.35
54 Less than 4 times/year - I live with this person X -9.48 1.00 -9.51 0.00
55 About once a month - About once a week X -0.00 0.70 -0.00 1.00
56 About once a month - Multiple times per week X -0.74 0.64 -1.16 0.86
57 About once a month - I live with this person X -8.93 0.99 -9.03 0.00
58 About once a week - Multiple times per week X -0.74 0.64 -1.16 0.85
59 About once a week - I live with this person X -8.93 0.99 -9.05 0.00
60 Multiple times per week - I live with this person X -8.18 0.94 -8.67 0.00
115

Table S60: Full reporting of the comparative statistics of Figure 2B in the main text: Pairwise
Comparisons of Connection Value Percentile for different Platforms within different bins for
the frequency in which ego meets alter.Highlighted contrastsare significant at the 1% level.
DF = 70743.
contrast How Freq. you meet Alter estimate(%) SE t-stat p-value
1 Facebook - Instagram Never -8.45 0.71 -11.82 0.00
2 Facebook - LinkedIn Never -5.83 0.70 -8.28 0.00
3 Facebook - X Never -7.02 0.62 -11.35 0.00
4 Instagram - LinkedIn Never 2.62 0.81 3.22 0.01
5 Instagram - X Never 1.43 0.74 1.94 0.21
6 LinkedIn - X Never -1.18 0.73 -1.62 0.36
7 Facebook - Instagram Less than 4 times/year -4.66 0.73 -6.37 0.00
8 Facebook - LinkedIn Less than 4 times/year -4.08 0.74 -5.52 0.00
9 Facebook - X Less than 4 times/year -3.13 0.62 -5.02 0.00
10 Instagram - LinkedIn Less than 4 times/year 0.58 0.91 0.64 0.92
11 Instagram - X Less than 4 times/year 1.53 0.82 1.86 0.25
12 LinkedIn - X Less than 4 times/year 0.95 0.83 1.14 0.66
13 Facebook - Instagram About once a month -4.98 0.79 -6.31 0.00
14 Facebook - LinkedIn About once a month -2.15 0.82 -2.61 0.05
15 Facebook - X About once a month -1.56 0.63 -2.48 0.06
16 Instagram - LinkedIn About once a month 2.83 1.01 2.81 0.03
17 Instagram - X About once a month 3.42 0.85 4.01 0.00
18 LinkedIn - X About once a month 0.59 0.89 0.67 0.91
19 Facebook - Instagram About once a week -1.21 0.89 -1.37 0.52
20 Facebook - LinkedIn About once a week -0.42 0.91 -0.46 0.97
21 Facebook - X About once a week 0.21 0.64 0.32 0.99
22 Instagram - LinkedIn About once a week 0.79 1.14 0.70 0.90
23 Instagram - X About once a week 1.42 0.93 1.52 0.42
24 LinkedIn - X About once a week 0.63 0.96 0.65 0.91
25 Facebook - Instagram Multiple times per week -2.86 0.71 -4.01 0.00
26 Facebook - LinkedIn Multiple times per week -0.96 0.69 -1.39 0.50
27 Facebook - X Multiple times per week 1.06 0.52 2.04 0.17
28 Instagram - LinkedIn Multiple times per week 1.90 0.88 2.16 0.13
29 Instagram - X Multiple times per week 3.92 0.75 5.21 0.00
30 LinkedIn - X Multiple times per week 2.02 0.73 2.77 0.03
31 Facebook - Instagram I live with this person 0.65 1.19 0.55 0.95
32 Facebook - LinkedIn I live with this person 5.42 1.41 3.84 0.00
33 Facebook - X I live with this person 4.58 1.01 4.52 0.00
34 Instagram - LinkedIn I live with this person 4.77 1.68 2.85 0.02
35 Instagram - X I live with this person 3.93 1.36 2.89 0.02
36 LinkedIn - X I live with this person -0.84 1.56 -0.54 0.95
116

Table S61: Full reporting of the comparative statistics of Figure 2B in the main text: Pairwise
Comparisons of Connection Value Percentile for different Platforms within different bins for
the frequency in which ego meets alter.Highlighted contrastsare significant at the 1% level.
DF = 70743.
S6.2.8 Figure 2C: Connection Value Percentile by Platform & Whether Ego is Con-
nected with Alter on Other Platform.
contrast Platform estimate(%) SE t.ratio p.value
1 No - Yes Facebook -6.917 0.722 -9.583 0
2 No - Yes Instagram -2.928 0.620 -4.722 0.00000
3 No - Yes LinkedIn -3.515 0.605 -5.813 0
4 No - Yes X -2.287 0.454 -5.038 0.00000
Table S62: Full reporting of the comparative statistics of Figure 2C in the main text: Pairwise
Comparisons of Connection Value Percentile between yes and no response to the question
whether ego is connected with alter in other platform for the different platforms.Highlighted
contrastsare significant at the 1% level. DF = 70759.
contrast Are you con. with Alter on other Platform? estimate(%) SE t.ratio p.value
1 Facebook- Instagram No -7.94 0.87 -9.11 0.00
2 Facebook- LinkedIn No -5.50 0.85 -6.44 0.00
3 Facebook- X No -5.88 0.80 -7.34 0.00
4 Instagram - LinkedIn No 2.45 0.71 3.46 0.00
5 Instagram - X No 2.06 0.64 3.21 0.01
6 LinkedIn - X No -0.38 0.62 -0.62 0.93
7 Facebook- Instagram Yes -3.95 0.38 -10.38 0.00
8 Facebook- LinkedIn Yes -2.09 0.40 -5.27 0.00
9 Facebook- X Yes -1.25 0.29 -4.26 0.00
10 Instagram - LinkedIn Yes 1.86 0.50 3.73 0.00
11 Instagram - X Yes 2.70 0.42 6.43 0.00
12 LinkedIn - X Yes 0.84 0.44 1.94 0.21
Table S63: Full reporting of the comparative statistics of Figure 2C in the main text: Pairwise
Comparisons of Connection Value Percentile for the different Platforms for whether ego is
connected with alter in other platform.Highlighted contrastsare significant at the 1% level.
DF = 70759.
S6.2.9 Figure 2D: Connection Value Percentile by Platform & Whether Ego is Con-
nected with Alter on Each other Platform
117

contrast Are you connected with Alter also in Facebook? estimate (%) SE t-stat p-value
1 Instagram - LinkedIn No 2.09 0.79 2.64 0.02
2 Instagram - X No 1.96 0.71 2.77 0.02
3 LinkedIn- X No -0.13 0.70 -0.19 0.98
4 Instagram - LinkedIn Yes 1.90 0.51 3.76 0.00
5 Instagram - X Yes 2.73 0.43 6.40 0.00
6 LinkedIn- X Yes 0.83 0.44 1.87 0.15
Table S64: Full reporting of the comparative statistics of Figure 2D (top left) in the main
text: Pairwise Comparisons of Connection Value Percentile between different platforms for
the case that Ego and Alter are connected also in Facebook or not.Highlighted contrastsare
significant at the 1% level. DF = 36045.
contrast Platform estimate (%) SE t-stat p-value
1 No - Yes Instagram -2.610 0.666 -3.919 0.0001
2 No - Yes LinkedIn -2.796 0.663 -4.217 0.00002
3 No - Yes X -1.838 0.489 -3.761 0.0002
Table S65: Full reporting of the comparative statistics of Figure 2D (top left) in the main text:
Pairwise Comparisons of Connection Value Percentile between whether Alter is also connected
with Ego in Facebook or not for the different platforms.Highlighted contrastsare significant
at the 1% level. DF = 36045
contrast Are you connected with Alter also on Instagram? estimate (%) SE t-stat p-value
1 Facebook - LinkedIn No -2.02 0.47 -4.28 0.00
2 Facebook - X No -0.91 0.45 -2.01 0.11
3 LinkedIn - X No 1.11 0.56 1.98 0.12
4 Facebook - LinkedIn Yes -0.61 0.47 -1.31 0.39
5 Facebook - X Yes -0.08 0.33 -0.26 0.96
6 LinkedIn - X Yes 0.53 0.48 1.10 0.51
Table S66: Full reporting of the comparative statistics of Figure 2D (top right) in the main
text: Pairwise Comparisons of Connection Value Percentile between different platforms for
the case that Ego and Alter are connected also on Instagram or not.Highlighted contrastsare
significant at the 1% level. DF = 60799.
contrast Platform estimate (%) SE t-stat p-value
1 No - Yes Facebook -3.518 0.321 -10.944 0
2 No - Yes LinkedIn -2.104 0.580 -3.625 0.0003
3 No - Yes X -2.694 0.455 -5.919 0
Table S67: Full reporting of the comparative statistics of Figure 2D (top right) in the main
text: Pairwise Comparisons of Connection Value Percentile between whether Alter is also
connected with Ego on Instagram or not for the different platforms.Highlighted contrasts
are significant at the 1% level. DF = 60799.
118

contrast Are you connected with Alter also in LinkedIn? estimate SE t-value p-value
1 Facebook - Instagram No -0.04 0.00 -10.30 0.00
2 Facebook - X No -0.01 0.00 -3.88 0.00
3 Instagram - X No 0.03 0.00 6.07 0.00
4 Facebook - Instagram Yes -0.02 0.01 -2.92 0.01
5 Facebook - X Yes -0.00 0.00 -0.57 0.83
6 Instagram - X Yes 0.02 0.01 2.55 0.03
Table S68: Full reporting of the comparative statistics of Figure 2D (bottom left) in the main
text: Pairwise Comparisons of Connection Value Percentile between different platforms for
the case that Ego and Alter are also connected on LinkedIn or not.Highlighted contrastsare
significant at the 1% level. DF = 61069
contrast Platform estimate (%) SE t-value p-value
1 No - Yes Facebook -0.008 0.004-2.164 0.030
2 No - Yes Instagram0.010 0.007 1.395 0.163
3 No - Yes X0.003 0.004 0.628 0.530
Table S69: Full reporting of the comparative statistics of Figure 2D (bottom left) in the main
text: Pairwise Comparisons of Connection Value Percentile between whether Alter is also
connected with Ego on LinkedIn or not for the different platforms.Highlighted contrastsare
significant at the 1% level. DF = 61069.
contrast Are you connected with Alter also on X? estimate (%) SE t-stat p-value
1 Facebook - Instagram No -3.05 0.42 -7.25 0.00
2 Facebook - LinkedIn No -1.52 0.41 -3.73 0.00
3 Instagram - LinkedIn No 1.53 0.51 2.97 0.01
4 Facebook - Instagram Yes -3.77 0.53 -7.16 0.00
5 Facebook - LinkedIn Yes -0.62 0.57 -1.08 0.53
6 Instagram - LinkedIn Yes 3.15 0.68 4.67 0.00
Table S70: Full reporting of the comparative statistics of Figure 2D (bottom right) in the main
text: Pairwise Comparisons of Connection Value Percentile between different platforms for the
case that Ego and Alter are also connected on X or not.Highlighted contrastsare significant
at the 1% level. DF = 51402.
contrast Platform estimate (%) SE t-stat p-value
1 No - Yes Facebook -1.495 0.336 -4.448 0.00001
2 No - Yes Instagram -2.217 0.584 -3.799 0.0001
3 No - Yes LinkedIn -0.591 0.615 -0.961 0.336
Table S71: Full reporting of the comparative statistics of Figure 2D (bottom right) in the
main text: Pairwise Comparisons of Connection Value Percentile between whether Alter is
also connected with Ego on X or not for the different platforms.Highlighted contrastsare
significant at the 1% level. DF = 51402.
119

S6.2.10 Figure 3A: Connection Value Percentile by Platform & Ego and Alter Gender
contrast Platform estimate (%) SE t-stat p-value
1 (Ego Male / Alter Male) - (Ego Female / Alter Female) Facebook -0.893 0.408 -2.188 0.126
2 (Ego Male / Alter Male) - (Ego Female / Alter Male) Facebook -1.932 0.476 -4.060 0.0003
3 (Ego Male / Alter Male) - (Ego Male / Alter Female) Facebook -3.439 0.490 -7.012 0
4 (Ego Female / Alter Female) - (Ego Female / Alter Male) Facebook -1.039 0.466 -2.229 0.115
5 (Ego Female / Alter Female) - (Ego Male / Alter Female) Facebook -2.546 0.481 -5.294 0.00000
6 (Ego Female / Alter Male) - (Ego Male / Alter Female) Facebook -1.507 0.539 -2.794 0.027
7 (Ego Male / Alter Male) - (Ego Female / Alter Female) Instagram -2.740 0.791 -3.465 0.003
8 (Ego Male / Alter Male) - (Ego Female / Alter Male) Instagram -3.011 0.907 -3.318 0.005
9 (Ego Male / Alter Male) - (Ego Male / Alter Female) Instagram -3.631 1.096 -3.315 0.005
10 (Ego Female / Alter Female) - (Ego Female / Alter Male) Instagram -0.270 0.755 -0.358 0.984
11 (Ego Female / Alter Female) - (Ego Male / Alter Female) Instagram -0.891 0.973 -0.916 0.797
12 (Ego Female / Alter Male) - (Ego Male / Alter Female) Instagram -0.621 1.070 -0.580 0.938
13 (Ego Male / Alter Male) - (Ego Female / Alter Female) LinkedIn -2.351 0.756 -3.112 0.010
14 (Ego Male / Alter Male) - (Ego Female / Alter Male) LinkedIn -0.322 0.831 -0.388 0.980
15 (Ego Male / Alter Male) - (Ego Male / Alter Female) LinkedIn -1.685 0.950 -1.773 0.287
16 (Ego Female / Alter Female) - (Ego Female / Alter Male) LinkedIn 2.029 0.842 2.411 0.075
17 (Ego Female / Alter Female) - (Ego Male / Alter Female) LinkedIn 0.666 0.960 0.694 0.899
18 (Ego Female / Alter Male) - (Ego Male / Alter Female) LinkedIn -1.363 1.020 -1.336 0.540
19 (Ego Male / Alter Male) - (Ego Female / Alter Female) X -1.820 0.548 -3.323 0.005
20 (Ego Male / Alter Male) - (Ego Female / Alter Male) X -1.637 0.623 -2.627 0.043
21 (Ego Male / Alter Male) - (Ego Male / Alter Female) X -2.338 0.585 -3.998 0.0004
22 (Ego Female / Alter Female) - (Ego Female / Alter Male) X 0.183 0.688 0.266 0.993
23 (Ego Female / Alter Female) - (Ego Male / Alter Female) X -0.518 0.654 -0.793 0.858
24 (Ego Female / Alter Male) - (Ego Male / Alter Female) X -0.701 0.718 -0.976 0.763
Table S72: Full reporting of the comparative statistics of Figure 3A in the main text: Pairwise
Comparisons of Connection Value Percentile between different Gender mix of Ego and Alter
for the different platforms.Highlighted contrastsare significant at the 1% level. DF = 67567
contrast gender mix estimate (%) SE t-stat p-value
1 Facebook - Instagram Ego Male / Alter Male -2.233 0.726 -3.075 0.011
2 Facebook - LinkedIn Ego Male / Alter Male -1.527 0.603 -2.530 0.055
3 Facebook - X Ego Male / Alter Male -1.009 0.442 -2.284 0.102
4 Instagram - LinkedIn Ego Male / Alter Male 0.706 0.846 0.835 0.838
5 Instagram - X Ego Male / Alter Male 1.224 0.739 1.655 0.348
6 LinkedIn - X Ego Male / Alter Male 0.517 0.619 0.835 0.838
7 Facebook - Instagram Ego Female / Alter Female -4.080 0.515 -7.929 0
8 Facebook - LinkedIn Ego Female / Alter Female -2.984 0.611 -4.885 0.00001
9 Facebook - X Ego Female / Alter Female -1.936 0.521 -3.718 0.001
10 Instagram - LinkedIn Ego Female / Alter Female 1.096 0.693 1.580 0.390
11 Instagram - X Ego Female / Alter Female 2.144 0.615 3.484 0.003
12 LinkedIn - X Ego Female / Alter Female 1.048 0.698 1.502 0.436
13 Facebook - Instagram Ego Female / Alter Male -3.312 0.723 -4.583 0.00003
14 Facebook - LinkedIn Ego Female / Alter Male 0.083 0.743 0.112 0.999
15 Facebook - X Ego Female / Alter Male -0.715 0.648 -1.103 0.687
16 Instagram - LinkedIn Ego Female / Alter Male 3.395 0.893 3.801 0.001
17 Instagram - X Ego Female / Alter Male 2.597 0.815 3.185 0.008
18 LinkedIn - X Ego Female / Alter Male -0.798 0.834 -0.957 0.774
19 Facebook - Instagram Ego Male / Alter Female -2.426 0.956 -2.538 0.054
20 Facebook - LinkedIn Ego Male / Alter Female 0.228 0.883 0.258 0.994
21 Facebook - X Ego Male / Alter Female 0.091 0.622 0.147 0.999
22 Instagram - LinkedIn Ego Male / Alter Female 2.653 1.178 2.252 0.110
23 Instagram - X Ego Male / Alter Female 2.517 0.998 2.522 0.057
24 LinkedIn - X Ego Male / Alter Female -0.136 0.928 -0.147 0.999
120

Table S73: Full reporting of the comparative statistics of Figure 3A in the main text: Pairwise
Comparisons of Connection Value Percentile between different platforms for different gender
contrast between Ego and Alter.Highlighted contrastsare significant at the 1% level. DF =
70739
121

S6.2.11 Figure 3B: Connection Value Percentile by Platform & Ego and Alter Race
contrast Platform estimate (%) SE t-stat p-value
1 Ego&Alter both Whites - (Ego White - Alter Non-White) Facebook 1.991 0.494 4.029 0.0003
2 Ego & Alter both Whites - (Ego Non-White - Alter White) Facebook 1.692 0.712 2.377 0.082
3 Ego & Alter both Whites - (Both Ego and Alter Non-Whites) Facebook -0.263 0.410 -0.642 0.918
4 (Ego White - Alter Non-White) - (Ego Non-White - Alter White) Facebook -0.300 0.813 -0.368 0.983
5 (Ego White - Alter Non-White) - (Both Ego and Alter Non-Whites) Facebook -2.255 0.568 -3.971 0.0004
6 (Ego Non-White - Alter White) - (Both Ego and Alter Non-Whites) Facebook -1.955 0.765 -2.556 0.052
7 Ego & Alter both Whites - (Ego White - Alter Non-White) Instagram 2.380 0.968 2.458 0.067
8 Ego & Alter both Whites - (Ego Non-White - Alter White) Instagram 1.557 1.175 1.325 0.547
9 Ego & Alter both Whites - (Both Ego and Alter Non-Whites) Instagram 0.130 0.680 0.191 0.998
10 (Ego White - Alter Non-White) - (Ego Non-White - Alter White) Instagram -0.823 1.403 -0.587 0.936
11 (Ego White - Alter Non-White) - (Both Ego and Alter Non-Whites) Instagram -2.251 1.025 -2.196 0.124
12 (Ego Non-White - Alter White) - (Both Ego and Alter Non-Whites) Instagram -1.428 1.222 -1.168 0.647
13 Ego & Alter both Whites - (Ego White - Alter Non-White) LinkedIn -0.959 0.941 -1.019 0.738
14 Ego & Alter both Whites - (Ego Non-White - Alter White) LinkedIn 0.587 1.117 0.525 0.953
15 Ego & Alter both Whites - (Both Ego and Alter Non-Whites) LinkedIn -1.139 0.789 -1.443 0.472
16 (Ego White - Alter Non-White) - (Ego Non-White - Alter White) LinkedIn 1.546 1.346 1.149 0.659
17 (Ego White - Alter Non-White) - (Both Ego and Alter Non-Whites) LinkedIn -0.180 1.089 -0.165 0.998
18 (Ego Non-White - Alter White) - (Both Ego and Alter Non-Whites) LinkedIn -1.725 1.244 -1.387 0.507
19 Ego & Alter both Whites - (Ego White - Alter Non-White) X 1.007 0.592 1.702 0.323
20 Ego & Alter both Whites - (Ego Non-White - Alter White) X 1.183 0.808 1.464 0.460
21 Ego & Alter both Whites - (Both Ego and Alter Non-Whites) X -0.890 0.524 -1.697 0.325
22 (Ego White - Alter Non-White) - (Ego Non-White - Alter White) X 0.177 0.907 0.195 0.997
23 (Ego White - Alter Non-White) - (Both Ego and Alter Non-Whites) X -1.896 0.666 -2.846 0.023
24 (Ego Non-White - Alter White) - (Both Ego and Alter Non-Whites) X -2.073 0.865 -2.397 0.078—
Table S74: Full reporting of the comparative statistics of Figure 3B in the main text: Pairwise
Comparisons of Connection Value Percentile between different Race mix for Ego and Alter
for the different platforms.Highlighted contrastsare significant at the 1% level. DF = 66762.
contrast Relative Ego and Alter Race estimate (%) SE t-stat p-value
1 Facebook - Instagram Ego&Alter both Whites -3.519 0.469 -7.500 0
2 Facebook - LinkedIn Ego & Alter both Whites -0.739 0.454 -1.626 0.364
3 Facebook - X Ego & Alter both Whites -0.661 0.368 -1.798 0.274
4 Instagram - LinkedIn Ego&Alter both Whites 2.781 0.580 4.792 0.00001
5 Instagram - X Ego&Alter both Whites 2.858 0.515 5.545 0.00000
6 LinkedIn - X Ego & Alter both Whites 0.077 0.502 0.154 0.999
7 Facebook - Instagram Ego White - Alter Non-White -3.131 0.981 -3.192 0.008
8 Facebook - LinkedIn Ego White - Alter Non-White -3.689 0.961 -3.837 0.001
9 Facebook - X Ego White - Alter Non-White -1.646 0.677 -2.430 0.072
10 Instagram - LinkedIn Ego White - Alter Non-White -0.558 1.220 -0.458 0.968
11 Instagram - X Ego White - Alter Non-White 1.485 1.011 1.468 0.457
12 LinkedIn - X Ego White - Alter Non-White 2.043 0.992 2.059 0.167
13 Facebook - Instagram Ego Non-White - Alter White -3.654 1.291 -2.829 0.024
14 Facebook - LinkedIn Ego Non-White - Alter White -1.844 1.244 -1.482 0.448
15 Facebook - X Ego Non-White - Alter White -1.170 1.012 -1.156 0.655
16 Instagram - LinkedIn Ego Non-White - Alter White 1.810 1.514 1.196 0.629
17 Instagram - X Ego Non-White - Alter White 2.484 1.330 1.868 0.242
18 LinkedIn - X Ego Non-White - Alter White 0.674 1.284 0.525 0.953
19 Facebook - Instagram Both Ego and Alter Non-Whites -3.127 0.641 -4.878 0.00001
20 Facebook - LinkedIn Both Ego and Alter Non-Whites -1.614 0.764 -2.112 0.149
21 Facebook - X Both Ego and Alter Non-Whites -1.287 0.554 -2.322 0.093
22 Instagram - LinkedIn Both Ego and Alter Non-Whites 1.512 0.865 1.748 0.299
23 Instagram - X Both Ego and Alter Non-Whites 1.839 0.687 2.676 0.037
24 LinkedIn - X Both Ego and Alter Non-Whites 0.327 0.803 0.407 0.977
122

Table S75: Full reporting of the comparative statistics of Figure 3B in the main text: Pairwise
Comparisons of Connection Value Percentile between different platforms for different Race
mix of Ego and Alter.Highlighted contrastsare significant at the 1% level. DF = 66762.
S6.2.12 Figure 3C: Connection Value Percentile by Platform & Relative Age of Ego and
Alter.
contrast Platform estimate (%) SE t-stat p-value
1 ego younger than alter - ego same age as alter Facebook 0.272 0.398 0.683 0.773
2 ego younger than alter - ego older than alter Facebook -0.022 0.422 -0.053 0.998
3 ego same age as alter - ego older than alter Facebook -0.294 0.384 -0.766 0.724
4 ego younger than alter - ego same age as alter Instagram -2.623 0.712 -3.685 0.001
5 ego younger than alter - ego older than alter Instagram -3.124 0.821 -3.804 0.0004
6 ego same age as alter - ego older than alter Instagram -0.501 0.722 -0.694 0.767
7 ego younger than alter - ego same age as alter LinkedIn 1.501 0.692 2.168 0.077
8 ego younger than alter - ego older than alter LinkedIn 0.779 0.804 0.970 0.596
9 ego same age as alter - ego older than alter LinkedIn -0.721 0.789 -0.914 0.632
10 ego younger than alter - ego same age as alter X -0.671 0.566 -1.186 0.462
11 ego younger than alter - ego older than alter X -0.103 0.603 -0.171 0.984
12 ego same age as alter - ego older than alter X 0.568 0.479 1.187 0.461
Table S76: Full reporting of the comparative statistics of Figure 3C in the main text: Pairwise
Comparisons of Connection Value Percentile between different Age mix of Ego and Alter for
the different platforms.Highlighted contrastsare significant at the 1% level. DF = 67965.
contrast Ego Age estimate (%) SE t-stat p-value
1 Facebook - Instagram younger than alter -1.231 0.651 -1.890 0.232
2 Facebook - LinkedIn younger than alter -2.091 0.588 -3.559 0.002
3 Facebook - X younger than alter -0.410 0.567 -0.723 0.888
4 Instagram - LinkedIn younger than alter -0.860 0.762 -1.129 0.671
5 Instagram - X younger than alter 0.821 0.746 1.100 0.690
6 LinkedIn - X younger than alter 1.681 0.691 2.431 0.071
7 Facebook - Instagram same age as alter -4.126 0.491 -8.404 0
8 Facebook - LinkedIn same age as alter -0.863 0.541 -1.596 0.381
9 Facebook - X same age as alter -1.353 0.396 -3.416 0.004
10 Instagram - LinkedIn same age as alter 3.263 0.636 5.127 0.00000
11 Instagram - X same age as alter 2.773 0.520 5.337 0.00000
12 LinkedIn - X same age as alter -0.491 0.567 -0.866 0.822
13 Facebook - Instagram older than alter -4.333 0.654 -6.621 0
14 Facebook - LinkedIn older than alter -1.290 0.692 -1.865 0.243
15 Facebook - X older than alter -0.491 0.469 -1.049 0.721
16 Instagram - LinkedIn older than alter 3.043 0.860 3.538 0.002
17 Instagram - X older than alter 3.842 0.693 5.539 0.00000
18 LinkedIn - X older than alter 0.798 0.729 1.096 0.692
123

Table S77: Full reporting of the comparative statistics of Figure 3C in the main text: Pairwise
Comparisons of Connection Value Percentile between different platforms for different relative
age between Ego and Alter.Highlighted contrastsare significant at the 1% level. DF =
67965.
124

S6.2.13 Figure 3D: Connection Value Percentile by Platform & Absolute Age of Alter.
contrast Platform estimate (%) SE t-stat p-value
1 Under 18 years old - (18-24 years old) Facebook 0.035 0.993 0.035 1
2 Under 18 years old - (25-34 years old) Facebook 0.723 0.964 0.750 0.976
3 Under 18 years old - (35-44 years old) Facebook 0.672 0.981 0.685 0.984
4 Under 18 years old - (45-54 years old) Facebook 1.381 1.033 1.337 0.764
5 Under 18 years old - 55 years or older Facebook -0.872 1.038 -0.840 0.960
6 (18-24 years old) - (25-34 years old) Facebook 0.688 0.469 1.466 0.686
7 (18-24 years old) - (35-44 years old) Facebook 0.637 0.503 1.267 0.803
8 (18-24 years old) - (45-54 years old) Facebook 1.346 0.597 2.254 0.213
9 (18-24 years old) - 55 years or older Facebook -0.907 0.607 -1.494 0.668
10 (25-34 years old) - (35-44 years old) Facebook -0.051 0.444 -0.114 1.000
11 (25-34 years old) - (45-54 years old) Facebook 0.658 0.549 1.199 0.837
12 (25-34 years old) - 55 years or older Facebook -1.595 0.560 -2.849 0.050
13 (35-44 years old) - (45-54 years old) Facebook 0.708 0.578 1.227 0.824
14 (35-44 years old) - 55 years or older Facebook -1.544 0.588 -2.626 0.091
15 (45-54 years old) - 55 years or older Facebook -2.253 0.670 -3.360 0.010
16 Under 18 years old - (18-24 years old) Instagram 3.292 1.409 2.336 0.179
17 Under 18 years old - (25-34 years old) Instagram 3.625 1.397 2.595 0.098
18 Under 18 years old - (35-44 years old) Instagram 4.423 1.458 3.033 0.029
19 Under 18 years old - (45-54 years old) Instagram 6.110 1.619 3.774 0.002
20 Under 18 years old - 55 years or older Instagram 7.543 1.759 4.288 0.0003
21 (18-24 years old) - (25-34 years old) Instagram 0.333 0.759 0.439 0.998
22 (18-24 years old) - (35-44 years old) Instagram 1.131 0.866 1.306 0.782
23 (18-24 years old) - (45-54 years old) Instagram 2.818 1.116 2.526 0.116
24 (18-24 years old) - 55 years or older Instagram 4.251 1.311 3.243 0.015
25 (25-34 years old) - (35-44 years old) Instagram 0.797 0.846 0.942 0.935
26 (25-34 years old) - (45-54 years old) Instagram 2.485 1.101 2.258 0.212
27 (25-34 years old) - 55 years or older Instagram 3.918 1.298 3.019 0.031
28 (35-44 years old) - (45-54 years old) Instagram 1.687 1.177 1.434 0.706
29 (35-44 years old) - 55 years or older Instagram 3.120 1.363 2.289 0.198
30 (45-54 years old) - 55 years or older Instagram 1.433 1.534 0.934 0.938
31 Under 18 years old - (18-24 years old) LinkedIn 1.715 2.551 0.672 0.985
32 Under 18 years old - (25-34 years old) LinkedIn -0.872 2.477 -0.352 0.999
33 Under 18 years old - (35-44 years old) LinkedIn 1.104 2.478 0.446 0.998
34 Under 18 years old - (45-54 years old) LinkedIn 0.355 2.513 0.141 1.000
35 Under 18 years old - 55 years or older LinkedIn -1.325 2.536 -0.523 0.995
36 (18-24 years old) - (25-34 years old) LinkedIn -2.587 1.027 -2.519 0.118
37 (18-24 years old) - (35-44 years old) LinkedIn -0.611 1.030 -0.593 0.992
38 (18-24 years old) - (45-54 years old) LinkedIn -1.360 1.111 -1.225 0.825
39 (18-24 years old) - 55 years or older LinkedIn -3.040 1.163 -2.614 0.094
40 (25-34 years old) - (35-44 years old) LinkedIn 1.976 0.827 2.388 0.160
41 (25-34 years old) - (45-54 years old) LinkedIn 1.226 0.926 1.324 0.772
42 (25-34 years old) - 55 years or older LinkedIn -0.454 0.989 -0.459 0.997
43 (35-44 years old) - (45-54 years old) LinkedIn -0.750 0.930 -0.806 0.966
44 (35-44 years old) - 55 years or older LinkedIn -2.430 0.992 -2.450 0.139
45 (45-54 years old) - 55 years or older LinkedIn -1.680 1.076 -1.562 0.624
46 Under 18 years old - (18-24 years old) X 2.681 1.334 2.010 0.337
47 Under 18 years old - (25-34 years old) X 3.594 1.308 2.748 0.066
48 Under 18 years old - (35-44 years old) X 2.865 1.331 2.152 0.261
49 Under 18 years old - (45-54 years old) X 4.457 1.477 3.016 0.031
50 Under 18 years old - 55 years or older X 2.585 1.687 1.533 0.643
51 (18-24 years old) - (25-34 years old) X 0.914 0.552 1.656 0.561
52 (18-24 years old) - (35-44 years old) X 0.184 0.606 0.305 1.000
53 (18-24 years old) - (45-54 years old) X 1.776 0.881 2.015 0.334
54 (18-24 years old) - 55 years or older X -0.095 1.200 -0.080 1.000
55 (25-34 years old) - (35-44 years old) X -0.729 0.546 -1.336 0.765
56 (25-34 years old) - (45-54 years old) X 0.862 0.842 1.025 0.910
57 (25-34 years old) - 55 years or older X -1.009 1.171 -0.862 0.955
58 (35-44 years old) - (45-54 years old) X 1.592 0.878 1.813 0.457
59 (35-44 years old) - 55 years or older X -0.280 1.197 -0.234 1.000
60 (45-54 years old) - 55 years or older X -1.871 1.358 -1.378 0.740
125

Table S78: Full reporting of the comparative statistics of Figure 3D in the main text: Pairwise
Comparisons of Connection Value Percentile between different Age bins of Alter for the dif-
ferent platforms.Highlighted contrastsare significant at the 1% level. DF = 67953.
contrast Alter Age estimate (%) SE t-stat p-value
1 Facebook - Instagram Under 18 years old -6.91 1.59 -4.34 0.00
2 Facebook - LinkedIn Under 18 years old -1.11 2.58 -0.43 0.97
3 Facebook - X Under 18 years old -3.54 1.56 -2.27 0.11
4 Instagram - LinkedIn Under 18 years old 5.80 2.73 2.12 0.15
5 Instagram - X Under 18 years old 3.37 1.81 1.86 0.24
6 LinkedIn - X Under 18 years old -2.43 2.72 -0.90 0.81
7 Facebook - Instagram 18-24 years old -3.65 0.66 -5.49 0.00
8 Facebook - LinkedIn 18-24 years old 0.57 0.92 0.62 0.92
9 Facebook - X 18-24 years old -0.89 0.57 -1.57 0.40
10 Instagram - LinkedIn 18-24 years old 4.23 1.01 4.19 0.00
11 Instagram - X 18-24 years old 2.76 0.70 3.94 0.00
12 LinkedIn - X 18-24 years old -1.47 0.95 -1.55 0.41
13 Facebook - Instagram 25-34 years old -4.00 0.59 -6.74 0.00
14 Facebook - LinkedIn 25-34 years old -2.70 0.65 -4.16 0.00
15 Facebook - X 25-34 years old -0.67 0.45 -1.49 0.44
16 Instagram - LinkedIn 25-34 years old 1.31 0.78 1.67 0.34
17 Instagram - X 25-34 years old 3.34 0.62 5.35 0.00
18 LinkedIn - X 25-34 years old 2.03 0.68 3.01 0.01
19 Facebook - Instagram 35-44 years old -3.16 0.75 -4.22 0.00
20 Facebook - LinkedIn 35-44 years old -0.67 0.68 -0.99 0.75
21 Facebook - X 35-44 years old -1.35 0.54 -2.48 0.06
22 Instagram - LinkedIn 35-44 years old 2.48 0.89 2.79 0.03
23 Instagram - X 35-44 years old 1.81 0.79 2.29 0.10
24 LinkedIn - X 35-44 years old -0.67 0.72 -0.93 0.79
25 Facebook - Instagram 45-54 years old -2.18 1.08 -2.02 0.18
26 Facebook - LinkedIn 45-54 years old -2.13 0.86 -2.48 0.06
27 Facebook - X 45-54 years old -0.46 0.90 -0.51 0.96
28 Instagram - LinkedIn 45-54 years old 0.05 1.21 0.04 1.00
29 Instagram - X 45-54 years old 1.72 1.24 1.39 0.51
30 LinkedIn - X 45-54 years old 1.67 1.05 1.58 0.39
31 Facebook - Instagram 55 years or older 1.51 1.28 1.18 0.64
32 Facebook - LinkedIn 55 years or older -1.56 0.93 -1.67 0.34
33 Facebook - X 55 years or older -0.08 1.22 -0.07 1.00
34 Instagram - LinkedIn 55 years or older -3.07 1.43 -2.14 0.14
35 Instagram - X 55 years or older -1.59 1.63 -0.97 0.76
36 LinkedIn - X 55 years or older 1.48 1.38 1.07 0.71
126

Table S79: Full reporting of the comparative statistics of Figure 3D in the main text: Pairwise
Comparisons of Connection Value Percentile between different platforms for different Age bin
of Alter.Highlighted contrastsare significant at the 1% level. DF = 67953.
S6.2.14 Figure 4A: Total Platform Valuation by Platform Feature Use
Contrast estimate ($) p-value
Messenger - Posting content on your news feed 5.361 0.326
Messenger - Engaging with content from your friends on your news feed 9.135 0.090
Messenger - Facebook Live 10.334 0.058
Messenger - Joining groups 13.468 0.011
Messenger - Playing games 15.781 0.002
Messenger - Organize attend events 16.241 0.004
Messenger - Marketplace 19.520 0.000
Posting content on your news feed - Engaging with content from your friends on your news feed 3.773 0.435
Posting content on your news feed - Facebook Live 4.973 0.326
Posting content on your news feed - Joining groups 8.106 0.090
Posting content on your news feed - Playing games 10.420 0.028
Posting content on your news feed - Organize attend events 10.880 0.037
Posting content on your news feed - Marketplace 14.159 0.002
Engaging with content from your friends on your news feed - Facebook Live 1.199 0.796
Engaging with content from your friends on your news feed - Joining groups 4.333 0.377
Engaging with content from your friends on your news feed - Playing games 6.646 0.190
Engaging with content from your friends on your news feed - Organize attend events 7.106 0.195
Engaging with content from your friends on your news feed - Marketplace 10.385 0.028
Facebook Live - Joining groups 3.134 0.504
Facebook Live - Playing games 5.447 0.287
Facebook Live - Organize attend events 5.907 0.287
Facebook Live - Marketplace 9.186 0.056
Joining groups - Playing games 2.314 0.586
Joining groups - Organize attend events 2.773 0.571
Joining groups - Marketplace 6.053 0.196
Playing games - Organize attend events 0.460 0.913
Playing games - Marketplace 3.739 0.417
Organize attend events - Marketplace 3.279 0.504
Table S80: Full reporting of the comparative statistics of Figure 4A (Facebook) in the main
text: Pairwise Comparisons of the increase in TPV associated with feature use.Highlighted
contrastsare significant at the 1% level.
127

Comparison Estimate p-value
Post Instagram reels vs Post photos as a post 6.293 0.237
Post Instagram reels vs Direct messages 7.632 0.158
Post Instagram reels vs Like and comment on stories 7.950 0.158
Post Instagram reels vs Post Instagram stories 9.596 0.080
Post Instagram reels vs Like and comment on reels 9.815 0.077
Post Instagram reels vs Instagram live 12.999 0.016
Post Instagram reels vs Like and comment on posts 17.487 0.001
Post photos as a post vs Direct messages 1.339 0.789
Post photos as a post vs Like and comment on stories 1.656 0.760
Post photos as a post vs Post Instagram stories 3.303 0.585
Post photos as a post vs Like and comment on reels 3.521 0.585
Post photos as a post vs Instagram live 6.705 0.220
Post photos as a post vs Like and comment on posts 11.194 0.077
Direct messages vs Like and comment on stories 0.318 0.955
Direct messages vs Post Instagram stories 1.964 0.760
Direct messages vs Like and comment on reels 2.183 0.759
Direct messages vs Instagram live 5.366 0.355
Direct messages vs Like and comment on posts 9.855 0.094
Like and comment on stories vs Post Instagram stories 1.646 0.760
Like and comment on stories vs Like and comment on reels 1.865 0.760
Like and comment on stories vs Instagram live 5.049 0.399
Like and comment on stories vs Like and comment on posts 9.538 0.109
Post Instagram stories vs Like and comment on reels 0.219 0.955
Post Instagram stories vs Instagram live 3.403 0.585
Post Instagram stories vs Like and comment on posts 7.891 0.172
Like and comment on reels vs Instagram live 3.184 0.585
Like and comment on reels vs Like and comment on posts 7.673 0.172
Instagram live vs Like and comment on posts 4.489 0.524
Table S81: Full reporting of the comparative statistics of Figure 4A (Instagram) in the main
text: Pairwise Comparisons of the increase in TPV associated with feature use.Highlighted
contrastsare significant at the 1% level.
128

Comparison Estimate p-value
Spaces vs Bookmark tweets 2.449 0.908
Spaces vs X Blue Premium 3.018 0.908
Spaces vs Like reply retweet tweets 4.670 0.832
Spaces vs Direct messages 4.748 0.816
Spaces vs Post tweets 4.990 0.816
Spaces vs X lists 9.482 0.816
Bookmark tweets vs X Blue Premium 0.568 0.985
Bookmark tweets vs Like reply retweet tweets 2.220 0.908
Bookmark tweets vs Direct messages 2.299 0.908
Bookmark tweets vs Post tweets 2.540 0.908
Bookmark tweets vs X lists 7.032 0.816
X Blue Premium vs Like reply retweet tweets 1.652 0.938
X Blue Premium vs Direct messages 1.731 0.938
X Blue Premium vs Post tweets 1.972 0.938
X Blue Premium vs X lists 6.464 0.816
Like reply retweet tweets vs Direct messages 0.078 0.985
Like reply retweet tweets vs Post tweets 0.320 0.985
Like reply retweet tweets vs X lists 4.812 0.816
Direct messages vs Post tweets 0.241 0.985
Direct messages vs X lists 4.733 0.816
Post tweets vs X lists 4.492 0.816
Table S82: Full reporting of the comparative statistics of Figure 4A (X) in the main text: Pair-
wise Comparisons of the increase in TPV associated with feature use.Highlighted contrasts
are significant at the 1% level.
Comparison Estimate p-value
LinkedIn groups vs Keep profile up to date 1.402 0.719
LinkedIn groups vs like comment and share content 6.756 0.148
LinkedIn groups vs Search and apply for jobs 8.402 0.148
Keep profile up to date vs like comment and share content 5.353 0.254
Keep profile up to date vs Search and apply for jobs 7.000 0.148
like comment and share content vs Search and apply for jobs 1.646 0.719
Table S83: Full reporting of the comparative statistics of Figure 4A (LinkedIn) in the main
text: Pairwise Comparisons of the increase in TPV associated with feature use.Highlighted
contrastsare significant at the 1% level.
129

S6.2.15 Figure 4B: Total Platform Valuation by Platform Feature Use and Income
contrast income level estimate ($) SE t-stat p-value
1 Messenger(FALSE) - Messenger(TRUE) High Income -14.719 4.086 -3.602 0.0003
2 Messenger(FALSE) - Messenger(TRUE) Low Income -26.949 5.229 -5.154 0.00000
Table S84: Full reporting of the comparative statistics ofFigure 4B (top left)in the main text:
Pairwise Comparisons of TPV for differential use of Facebook Messenger for different Income
levels.Highlighted contrastsare significant at the 1% level. DF=2466.
contrast Messenger User estimate ($) SE t-stat p-value
1 High Income - Low Income FALSE 5.914 6.045 0.978 0.328
2 High Income - Low Income TRUE -6.316 2.738 -2.306 0.021
Table S85: Full reporting of the comparative statistics ofFigure 4B (top left)in the main text:
Pairwise Comparisons of TPV for different Income level for Messenger Users and Non Users
.Highlighted contrastsare significant at the 1% level. DF = 2466.
contrast income level estimate ($) SE t-stat p-value
1 Insta Reels(FALSE) - Insta Reels(TRUE) High Income -13.551 3.233 -4.192 0.00003
2 Insta Reels(FALSE) - Insta Reels(TRUE) Low Income -21.033 3.604 -5.836 0
Table S86: Full reporting of the comparative statistics ofFigure 4B (top right)in the main
text: Pairwise Comparisons of TPV for differential use of Reels and by different Income level.
Highlighted contrastsare significant at the 1% level. DF = 2484.
contrast Posting Instagram reels estimate ($) SE t-stat p-value
1 High Income - Low Income FALSE -3.209 2.927 -1.096 0.273
2 High Income - Low Income TRUE -10.691 3.856 -2.772 0.006
Table S87: Full reporting of the comparative statistics ofFigure 4B (top right)in the main text:
Pair- wise Comparisons of TPV for different Income level for Users that either post Instagram
Reels or not.Highlighted contrastsare significant at the 1% level. DF = 2484.
contrast LowHighIncome estimate SE t.ratio p.value
1 XLists(FALSE) - XLists(TRUE) High Income 8.277 3.882 2.132 0.033
2 XLists(FALSE) - XLists(TRUE) Low Income -19.070 4.371 -4.363 0.00001
130

Table S88: Full reporting of the comparative statistics ofFigure 4B (bottom right)in the main
text: Pairwise Comparisons of TPV for differential use of X Lists and by different Income
level.Highlighted contrastsare significant at the 1% level. DF = 2233.
contrast X lists estimate ($) SE t-stat p-value
1 High Income - Low Income FALSE 6.292 2.919 2.156 0.031
2 High Income - Low Income TRUE -21.054 5.065 -4.157 0.00003
Table S89: Full reporting of the comparative statistics ofFigure 4B (bottom right)in the main
text: Pairwise Comparisons of TPV for different Income level for users and non-users of X
Lists.Highlighted contrastsare significant at the 1% level. DF = 2233.
contrast LowHighIncome estimate SE t.ratio p.value
1 LK Groups(FALSE) - LK Groups(TRUE) High Income -7.115 3.427 -2.076 0.038
2 LK Groups(FALSE) - LK Groups(TRUE) Low Income -18.658 3.962 -4.709 0.00000
Table S90: Full reporting of the comparative statistics of Figure 4B (bottom left) in the main
text: Pair- wise Comparisons of TPV for differential use of LinkedIn groups for different
Income levels.Highlighted contrastsare significant at the 1% level. DF = 2196.
contrast LinkedIn Groups estimate SE t.ratio p.value
1 High Income - Low Income FALSE 2.833 3.247 0.873 0.383
2 High Income - Low Income TRUE -8.710 4.111 -2.119 0.034
Table S91: Full reporting of the comparative statistics ofFigure 4B (bottom left)in the main
text: Pairwise Comparisons of TPV for different Income level for users and non-users of
LinkedIn groups.Highlighted contrastsare significant at the 1% level. DF = 2196.
131

(1)
How you know: I only know them online
How you know: Family member or family friend1.304***
How you know: None of these1.027
How you know: School (K-12)1.014
How you know: Work1.028
How you know: Shared interest in real life1.071**
How you know: College or University1.068**
Meeting frequency: Never
Meeting frequency: I live with this person2.738***
Meeting frequency: Less than 4 times/year1.326***
Meeting frequency: About once a month1.563***
Meeting frequency: About once a week1.651***
Meeting frequency: Multiple times per week1.855***
Connected on other platform: Yes1.263***
Alter gender: Male
Alter gender: Female1.066***
Alter age: Over 65 years old
Alter age: Under 18 years old1.121**
Alter age: 18-24 years old1.108**
Alter age: 25-34 years old1.100**
Alter age: 35-44 years old1.078**
Alter age: 45-54 years old1.015
Alter age: 55-64 years old1.058
Alter race: Asian / Pacific Islander
Alter race: White1.042
Alter race: Black or African American1.018
Alter race: Hispanic or Latino1.037
Alter race: Native American or American Indian1.022
Num.Obs.230 669
* p<0.1, ** p<0.05, *** p<0.01
Odds ratios reported. Strata by ego $\times$ ranking stage.
132

(1)
How you know: I only know them online
How you know: Family member or family friend1.299***
How you know: None of these1.029
How you know: School (K-12)1.013
How you know: Work1.030
How you know: Shared interest in real life1.070**
How you know: College or University1.068**
Meeting frequency: Never
Meeting frequency: I live with this person2.722***
fq 5 friendnum Less than 4 times/year1.325***
Meeting frequency: About once a month1.560***
Meeting frequency: About once a week1.647***
Meeting frequency: Multiple times per week1.851***
Connected on other platform: No
Connected on other platform: Yes1.262***
Gender Mix: Ego Male - Alter Male
Gender Mix: Ego Female - Alter Female1.042**
Gender Mix: Ego Male - Alter Female1.092***
Age Mix: younger than alter
Age Mix: same age as alter1.054***
Age Mix: older than alter1.044**
Race Mix: Ego Non-White - Alter White
Race Mix: Ego & Alter both Whites1.052**
Race Mix: Both Ego and Alter Non-Whites1.057*
Num.Obs.230 669
* p<0.1, ** p<0.05, *** p<0.01
Odds ratios reported. Strata by ego $\times$ ranking stage.
133

(1)
How you know: I only know them online
How you know: None of these1.029
How you know: School (K-12)1.013
How you know: Work1.029
How you know: Shared interest in real life1.069**
How you know: College or University1.068**
How you know: Family member or family friend1.298***
Meeting frequency: Never
Meeting frequency: Less than 4 times/year1.325***
Meeting frequency: About once a month1.560***
Meeting frequency: About once a week1.647***
Meeting frequency: Multiple times per week1.850***
Meeting frequency: I live with this person2.719***
Connected on other platform: No
Connected on other platform: Yes1.262***
Gender: Alter Female1.067***
Gender: Ego and Alter Different Gender1.024**
Age Mix: younger than alter
Age Mix: same age as alter1.054***
Age Mix: ego older than alter1.044**
Race: alter nonwhite1.011
Race: same race1.061***
Num.Obs.230 669
* p<0.1, ** p<0.05, *** p<0.01
Odds ratios reported. Strata by ego $\times$ ranking stage.
134

References
1. Aral, S. The future of weak ties.American Journal of Sociology121, 1931–1939 (2016).
2. Marsden, P. V . & Campbell, K. E. Measuring tie strength.Social forces63, 482–501
(1984).
3. Fischer, C. S. What do we mean by ‘friend’? an inductive study.Social Networks3,
287–306 (1982).
4. Wellman, B. & Wortley, S. Different strokes from different folks: Community ties and
social support.American journal of Sociology96, 558–588 (1990).
5. Roberts, S. C., Dunbar, R. I. M., Pollet, T. V . & Kuppens, T. The costs of family and
friends: An 18-month longitudinal study of relationship maintenance and decay.Evolution
and Human Behavior32, 186–197 (2011).
6. Krosnick, J. A. & Alwin, D. F. A test of the form-resistant correlation hypothesis: Ratings,
rankings, and the measurement of values.Public Opinion Quarterly52, 526–538 (1988).
7. DeScioli, P. & Kurzban, R. The alliance hypothesis for human friendship.PloS one4,
e5802 (2009).
8. Granovetter, M. S. The strength of weak ties.American journal of sociology78, 1360–
1380 (1973).
9. Rajkumar, K., Saint-Jacques, G., Bojinov, I., Brynjolfsson, E. & Aral, S. A causal test of
the strength of weak ties.Science377, 1304–1310 (2022).
10. Coleman, J. S. Social capital in the creation of human capital.American journal of
sociology94, S95–S120 (1988).
11. Chetty, R.et al.Social capital i: measurement and associations with economic mobility.
Nature608, 108–121 (2022).
135

12. Chetty, R.et al.Social capital ii: determinants of economic connectedness.Nature608,
122–134 (2022).
13. Burt, R. S. The network structure of social capital.Research in organizational behavior
22, 345–423 (2000).
14. Burt, R. S. Structural holes and good ideas.American journal of sociology110, 349–399
(2004).
15. Podolny, J. M. Networks as the pipes and prisms of the market.American journal of
sociology107, 33–60 (2001).
16. White, H. C.Markets from networks: Socioeconomic models of production(Princeton
University Press, 2001).
17. Jackson, M. O. & Wolinsky, A.A strategic model of social and economic networks
(Springer, 2003).
18. Padgett, J. F. & Ansell, C. K. Robust action and the rise of the medici, 1400-1434.Amer-
ican journal of sociology98, 1259–1319 (1993).
19. Benzell, S. G. & Cooke, K. A network of thrones: Kinship and conflict in europe, 1495–
1918.American Economic Journal: Applied Economics13, 102–133 (2021).
20. Wellman, B., Haase, A. Q., Witte, J. & Hampton, K. Does the internet increase, decrease,
or supplement social capital? social networks, participation, and community commitment.
American behavioral scientist45, 436–455 (2001).
21. Burke, M., Kraut, R. & Marlow, C. Social capital on facebook: Differentiating uses and
users. InProceedings of the SIGCHI conference on human factors in computing systems,
571–580 (2011).
22. Wellman, B. & Hampton, K. Living networked on and offline.Contemporary Sociology
28, 648–654 (1999).
136

23. Onnela, J.-P.et al.Structure and tie strengths in mobile communication networks.Pro-
ceedings of the national academy of sciences104, 7332–7336 (2007).
24. Putnam, R. D.Bowling Alone: The Collapse and Revival of American Community(Simon
& Schuster, New York, 2000).
25. Williams, D. On and off the ’net: Scales for social capital in an online era.Journal of
Computer-Mediated Communication11, 593–628 (2006).
26. Ellison, N. B., Steinfield, C. & Lampe, C. The benefits of facebook “friends”: Social
capital and college students’ use of online social network sites.Journal of Computer-
Mediated Communication12, 1143–1168 (2007).
27. Ellison, N. B., Vitak, J., Gray, R. & Lampe, C. Cultivating social resources on social
network sites: Facebook relationship maintenance behaviors and their role in social capital
processes.Journal of Computer-Mediated Communication19, 855–870 (2014).
28. Ellison, N. B., Lampe, C., Steinfield, C. & Vitak, J. With a little help from my friends:
How social network sites affect social capital processes. In Papacharissi, Z. (ed.)A Net-
worked Self: Identity, Community, and Culture on Social Network Sites, 124–145 (Rout-
ledge, New York, 2010).
29. Petr ´oczi, A., Nepusz, T. & Bazs ´o, F. Measuring tie-strength in virtual social networks.
Connections27, 39–52 (2007).
30. Gilbert, E. & Karahalios, K. Predicting tie strength with social media. InProceedings of
the SIGCHI conference on human factors in computing systems, 211–220 (2009).
31. Jones, J. J.et al.Inferring tie strength from online directed behavior.PloS one8, e52168
(2013).
137

32. Brynjolfsson, E. & Kemerer, C. F. Network externalities in microcomputer software: An
econometric analysis of the spreadsheet market.Management science42, 1627–1647
(1996).
33. Tucker, C. Identifying formal and informal influence in technology adoption with network
externalities.Management science54, 2024–2038 (2008).
34. Boudreau, K. J. Promoting platform takeoff and self-fulfilling expectations: Field experi-
mental evidence.Management Science67, 5953–5967 (2021).
35. Bramoull ´e, Y ., Djebbari, H. & Fortin, B. Identification of peer effects through social
networks.Journal of econometrics150, 41–55 (2009).
36. Brynjolfsson, E., Collis, A. & Eggers, F. Using massive online choice experiments to
measure changes in well-being.Proceedings of the National Academy of Sciences116,
7250–7255 (2019).
37. Allcott, H., Braghieri, L., Eichmeyer, S. & Gentzkow, M. The welfare effects of social
media.American Economic Review110, 629–676 (2020).
38. Coppock, A. & McClellan, O. A. Validating the demographic, political, psychological,
and experimental results obtained from a new source of online survey respondents.Re-
search & Politics6, 2053168018822174 (2019).
39. Pennycook, G.et al.Shifting attention to accuracy can reduce misinformation online.
Nature592, 590–595 (2021).
40. Sol ´ıs Arce, J. S.et al.Covid-19 vaccine acceptance and hesitancy in low-and middle-
income countries.Nature medicine27, 1385–1394 (2021).
41. Benzell, S. G., Collis, A. & Nicolaides, C. Rationing social contact during the covid-
19 pandemic: Transmission risk and social benefits of us locations.Proceedings of the
National Academy of Sciences117, 14642–14644 (2020).
138

42. Becker, G. M., DeGroot, M. H. & Marschak, J. Measuring utility by a single-response
sequential method.Behavioral science9, 226–232 (1964).
43. Burchardi, K. B., De Quidt, J., Gulesci, S., Lerva, B. & Tripodi, S. Testing willingness to
pay elicitation mechanisms in the field: Evidence from uganda.Journal of Development
Economics152, 102701 (2021).
44. Bursztyn, L., Handel, B. R., Jimenez, R. & Roth, C. When product markets become
collective traps: The case of social media. Tech. Rep., National Bureau of Economic
Research (2023).
45. Andersen, S., Harrison, G. W., Lau, M. I. & Rutstr ¨om, E. E. Elicitation using multiple
price list formats.Experimental Economics9, 383–405 (2006).
46. de Bekker-Grob, E. W., Ryan, M. & Gerard, K. Discrete choice experiments in health
economics: a review of the literature.Health economics21, 145–172 (2012).
47. Jack, B. K., McDermott, K. & Sautmann, A. Multiple price lists for willingness to pay
elicitation.Journal of Development Economics159, 102977 (2022).
48. Parker, G. G. & Van Alstyne, M. W. Two-sided network effects: A theory of information
product design.Management science51, 1494–1504 (2005).
49. Hovenkamp, H. Antitrust and platform monopoly.Yale LJ130, 1952 (2020).
50. Brynjolfsson, E. & Milgrom, P. Complementarity in organizations.The handbook of
organizational economics11–55 (2013).
51. Collis, A. & Eggers, F. Effects of restricting social media usage on wellbeing and perfor-
mance: A randomized control trial among students.PloS one17, e0272416 (2022).
52. Aridor, G. Forthcoming.“measuring substitution patterns in the attention economy: An
experimental approach.”.RAND Journal of Economics.
139

53. American National Election Studies. Anes 2020-2022 social media study release
[dataset and documentation] (2023). URLhttps://electionstudies.org/
wp-content/uploads/2023/07/anes_specialstudy_2020-2022_
socialmedia_userguidecodebook_20230705.pdf. Accessed 12-28-24.
54. U.S. Census Bureau. U.S. Census Bureau QuickFacts: United States (2024). URL
https://www.census.gov/quickfacts/fact/table/US/PST045219.
Accessed December 1, 2024.
55. Gottfried, J. Americans’ social media use (2024). URL
https://www.pewresearch.org/internet/2024/01/31/
americans-social-media-use/. Accessed 9-29-24.
56. Aral, S.The Hype Machine: How Social Media Disrupts Our Elections, Our Economy,
and Our Health–and How We Must Adapt(Currency, 2021).
57. Beggs, S., Cardell, S. & Hausman, J. Assessing the potential demand for electric cars.
Journal of Econometrics17, 1–19 (1981).
58. Rohlfs, J. A theory of interdependent demand for a communications service.The Bell
journal of economics and management science16–37 (1974).
59. Filippas, A., Horton, J. & Lipnowski, E. The production and consumption of social me-
dia. InProceedings of the 23rd ACM Conference on Economics and Computation, EC
’22, 287–288 (Association for Computing Machinery, New York, NY , USA, 2022). URL
https://doi.org/10.1145/3490486.3538372.
60. Rothwell, J. How parenting and self-control mediate the link between social media use
and youth mental health (2023). URLhttps://www.ifstudies.org/.
140

Wave 1 Instrument
141

Intro page
Welcome!
 
The purpose of this research study is to investigate how much
you value online platforms. Answering this survey will take less
than 10 minutes. 
 
You need to have a Instagram account in order to take this
survey and follow our research account on Instagram. We
will ask you about your Instagram proﬁle and usage. We will
permanently delete all of your personal information as soon
as the study is complete. We want to reward you for thinking
carefully about these questions. Therefore, we will randomly
select at least 1 in 200 respondents and give them cash
rewards of over $200.
 
The study is being conducted by researchers Seth Benzell and
Avi Collis who are research associates at MIT. For any
questions, please contact us at:
socialmedia_research@mit.edu
 
Participation in this study is voluntary and you can quit at any
time. You have to be more than 18 years old to participate in
this study. You can only participate once. All the information
you provide will be treated conﬁdentially and kept
anonymous.
 
If you agree and wish to participate in this study, please check
the 'I AGREE' box.
I AGREE
I DO NOT AGREE
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 1/11

follow Instagram account
We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select at least 1 in 200
respondents and give them cash rewards of over $200.
To be eligible for the reward, please follow our research
account on
Instagram: https://www.instagram.com/mit_research_project/
We will only contact you if you are selected for the reward,
and we will permanently delete your information after the
study is complete.
 
If you do not want to proceed, please exit the study. Note that
your response will be rejected if you select that you have
followed us on Instagram but you haven't actually done so.
Demographics
What gender do you most identify with?
What is your year of birth?
I followed your account on Instagram, my Instagram handle (@username) is:
I do not want to follow your account on Instagram, I will exit the study
Male
Female
Other
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 2/11

Please indicate your ethnicity
How much total combined money did all members of your
HOUSEHOLD earn in the year 2019?
Here is a scale on which the political views that people might
hold are arranged from extremely liberal to extremely
conservative. Where would you place yourself on this
scale?
Screener
Which of these online platforms do you use? Select all that
apply.
White
Hispanic or Latino
Black or African American
Native American or American Indian
Asian / Paciﬁc Islander
Other
Less than $25,000
$25,000 - $49,999
$50,000 - $99,999
$100,000 - $149,999
$150,000 or more
Extremely liberal
Liberal
Slightly liberal
Moderate
Slightly conservative
Conservative
Extremely conservative
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 3/11

Platforms usage 1
Please rank the following online platforms from most used
(top) by you to least used (bottom) by you in terms of time
spent on them.
Platforms usage 2
In the past week, on average, approximately how much time
PER DAY have you spent actively using Facebook?
In the past week, on average, approximately how much time
PER DAY have you spent actively using Instagram?
Instagram
Twitter
Facebook
LinkedIn
None of the above
LinkedIn
Twitter
Instagram
Facebook
Less than 10 minutes per day
10–30 minutes per day
31–60 minutes per day
1–2 hours per day
2–3 hours per day
More than 3 hours per day
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 4/11

In the past week, on average, approximately how much time
PER DAY have you spent actively using LinkedIn?
In the past week, on average, approximately how much time
PER DAY have you spent actively using Twitter?
Friends
In the following questions, we will ask you for names (ﬁrst
name and last initial) of your four overall most important
contacts as well as four other proﬁles you are connected to
on Instagram. We will also ask you some general details
about these friends/ proﬁles.
 
Less than 10 minutes per day
10–30 minutes per day
31–60 minutes per day
1–2 hours per day
2–3 hours per day
More than 3 hours per day
Less than 10 minutes per day
10–30 minutes per day
31–60 minutes per day
1–2 hours per day
2–3 hours per day
More than 3 hours per day
Less than 10 minutes per day
10–30 minutes per day
31–60 minutes per day
1–2 hours per day
2–3 hours per day
More than 3 hours per day
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 5/11

We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select at least 1 in 200
respondents and give them $200 or more after we verify that
you have entered valid names and details of your friends/
proﬁles.
Name your most important contacts (ﬁrst name and last
initial) ranked in order from most important to 4th most
important. These contacts could include friends, family, and
colleagues or any other type of relationships.
Give some details about your contacts.
Friend 1
Friend 2
Friend 3
Friend 4
Gender Age
${q://QID310/ChoiceTextEntryValue/1}
${q://QID310/ChoiceTextEntryValue/2}
${q://QID310/ChoiceTextEntryValue/3}
${q://QID310/ChoiceTextEntryValue/6}
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 6/11

Name any four people excluding the four closest friends
mentioned before and excluding organizations, that you are
connected to on Instagram. You can enter their Instagram
@username/ handle OR their ﬁrst name and last initial.
Give some details about these Instagram connections.
WTA
In the following questions, we will ask you for the minimum
amount of money (in US $) you would require to either
deactivate Instagram for 1 month. We will also ask you some
questions about how much you value your connections on
Instagram.
 
Friend 1
Friend 2
Friend 3
Friend 4
Gender Age
${q://QID311/ChoiceTextEntryValue/1}
${q://QID311/ChoiceTextEntryValue/2}
${q://QID311/ChoiceTextEntryValue/3}
${q://QID311/ChoiceTextEntryValue/6}
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 7/11

We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select 1 in 200
respondents and give them a chance to get $200 or more if
they follow up on their choices.
 
The procedure to get the reward works as follows:
We will randomly generate an amount of money to offer
you to deactivate Instagram for 1 month.
If the randomly generated offer is greater than the
minimum amount of money you enter, then you will be
asked to not use Instagram  for 1 month and you will get
the payment at the end of the month. We will also pay you
a bonus payment of $200 for your trouble. Note that we
will verify that you deactivated it for 1 month before getting
the payment.
If the randomly generated offer is less than the minimum
amount of money you enter, then you will only receive the
bonus payment of $200 and no additional payment.
 
Therefore, it is in your best interest to think carefully and
truthfully report the minimum amount of money you would
require to either not use Instagram or block a particular
proﬁle on Instagram for 1 month.
What is the minimum amount of money (in US $) you would
require to deactivate Instagram for 1 month?
If >$100, what is the minimum amount of money (in US $)
you would require to deactivate Instagram for 1 month?
                     
  >100
 0 10 20 30 40 50 60 70 80 90 100
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 8/11

What percent of the total value that you get from Instagram
is due to these four
connections ${q://QID311/ChoiceTextEntryValue/1}, ${q://QID
and ${q://QID311/ChoiceTextEntryValue/6}, using the
platform?
Please rank the following connections from most valued on
Instagram (top) by you to least valued on Instagram
(bottom) by you.
On Instagram, you may have connections whom you met in
many different ways.
                   
 
 0 10 20 30 40 50 60 70 80 90 100
${q://QID311/ChoiceTextEntryValue/2}
${q://QID311/ChoiceTextEntryValue/3}
${q://QID311/ChoiceTextEntryValue/6}
${q://QID310/ChoiceTextEntryValue/1}
${q://QID310/ChoiceTextEntryValue/3}
${q://QID310/ChoiceTextEntryValue/2}
${q://QID310/ChoiceTextEntryValue/6}
${q://QID311/ChoiceTextEntryValue/1}
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0Y… 9/11

Please rank the following categories from most common
source of connections on Instagram to least common.
Covid question
Which best describes how you have changed in your
interaction with friends during the COVID-19 pandemic?
Insta follow reminder
As mentioned previously, your response will be rejected if you
haven't followed our research account on
Instagram: https://www.instagram.com/mit_research_project/
Did you follow our research account on Instagram?
Through a shared interest in real life
Family member or family friend
School (K-12)
Work
College or University
Connections you only know online
I have completely stopped meeting in person with friends
I have reduced my amount of in person meetings with friends a lot
I have reduced my amount of in person meetings with friends somewhat
I have not changed my amount of in person meetings with friends
I followed your account on Instagram, my Instagram handle (@username) is:
I do not want to follow your account on Instagram, my response will be
rejected
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0… 10/11

Powered by Qualtrics
Thank you
Thank you for participating in our study. We will contact you if
you are selected for the additional rewards.
7/16/25, 10:53 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_4Gv8MOvyub9EUdg&ContextLibraryID=UR_9ZTpo8t0… 11/11

Wave 2 Instrument
153

Intro page
Welcome!
 
The purpose of this research study is to investigate how much
you value online platforms. Answering this survey will take less
than 5 minutes. 
 
You need to have a Instagram account and be located in
the US in order to take this survey. We will ask you about your
Instagram proﬁle and usage. We will permanently delete all of
your personal information as soon as the study is complete.
We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select some
respondents and give them bonus cash rewards of up
to $200.
 
The study is being conducted by researchers at MIT. For any
questions, please contact us at:
socialmedia_research@mit.edu
 
Participation in this study is voluntary and you can quit at any
time. You have to be more than 18 years old to participate in
this study. You can only participate once. All the information
you provide will be treated conﬁdentially and kept
anonymous.
 
If you agree and wish to participate in this study, please check
the 'I AGREE' box.
email
I AGREE
I DO NOT AGREE
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 1/13

We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select some
respondents and give them bonus cash rewards of up
to $200.
If you are selected for the reward, we will contact you via
email. Please enter your email address below.
 
We will only contact you if you are selected for the reward,
and we will permanently delete your email after the study is
complete.
If you do not want to proceed, please exit the study.
Demographics
What gender do you most identify with?
What is your year of birth?
What is your zipcode?
I want to participate in the study, my email is:
I do not want to share my email, I will exit the study
Male
Female
Other
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 2/13

Please indicate your ethnicity.
What is your relationship status?
How many people are in your household?
How much total combined money did all members of your
HOUSEHOLD earn last year (2022)?
White
Hispanic or Latino
Black or African American
Native American or American Indian
Asian or Paciﬁc Islander
Other
Single, looking for a relationship
Single, not looking for a relationship
In a serious relationship
Married or domestic partnership
Prefer not to say
1 (just yourself)
2
3
4
5
6
7 or more
Less than $25,000
$25,000 - $49,999
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 3/13

How many different places have you lived in the past 10
years?
Are you currently looking for a job? Please select the situation
that best applies to you.
Here is a scale on which the political views that people might
hold are arranged from extremely liberal to extremely
conservative. Where would you place yourself on this
scale?
$50,000 - $99,999
$100,000 - $149,999
$150,000 or more
1 (I never moved)
2
3
4
5 or more
Yes
No, but I looked for a job in the past year
No, and I have not looked in the past year
Extremely liberal
Liberal
Slightly liberal
Moderate
Slightly conservative
Conservative
Extremely conservative
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 4/13

Please select how much you agree or disagree with the
following statements:
Insta usage
Which of these platforms have you used in the past month?
Please select all that apply.
In the past week, on average, approximately how much time
PER DAY have you spent actively using Instagram?
In which year did you ﬁrst create your Instagram account?
    
Strongly
disagree
Somewhat
disagree
Neither
agree nor
disagree
Somewhat
agree
Strongly
agree
I keep in the
background.   
I talk to a lot of
different people at
parties.
  
Facebook
TikTok
Mystro
Snapchat
Instagram
LinkedIn
X/Twitter
Less than 10 minutes per day
10–30 minutes per day
31–60 minutes per day
1–2 hours per day
2–3 hours per day
More than 3 hours per day
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 5/13

friend count
How many follower and following connections do you have on
Instagram? Please open your Instagram proﬁle and check
and report the exact number. You can log into your Instagram
proﬁle to check the number of
connections: https://www.instagram.com/
If you are selected for the bonus payment, we will verify that
you entered the correct numbers. You will get the bonus
payment if and only if you enter the correct numbers below
(the exact follower counts may change slightly between now
and when we verify it, we will take that into consideration).
On Instagram, which of these features do you use? Select all
that apply.
      
Number of followers   
Number of
connections you are
following
  
Instagram live
Post Instagram reels
Direct messages
Like and comment on posts
Post photos as a post
Like and comment on reels
None of the above
Like and comment on stories
Post Instagram stories
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 6/13

WTA 100
In the following question, we will ask you to think about the
minimum amount of money (in US $) you would require to
deactivate Instagram for 1 month.
 
We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select 1 in 100
respondents and give them a chance to get up to $100 if they
follow up on their choices.
 
The procedure to get the reward works as follows:
We will randomly select 1 in 100 respondents.
For this respondent, we will randomly select one of the
rows below.
If you choose to deactivate Instagram in exchange for the
amount mentioned in that row, we will email you and ask
you to deactivate Instagram for 1 month starting from that
date.
At the end of the month, if you kept your account
deactivated throughout the month, we will pay you the
amount mentioned in that row.
If you choose to not deactivate Instagram in exchange for
the amount mentioned in that row, you don't have to do
anything and you will not get any bonus payment.
Therefore, it is in your best interest to think carefully and
truthfully report which of the following amounts of money
you would accept to deactivate Instagram for 1 month.
 
Note that if your answers are not consistent (for example, if
you choose to accept a lower cash offer but reject a higher
cash offer), your response will be rejected.
For each of the possible cash offers below, please choose
whether you prefer to accept the cash and deactivate
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 7/13

Instagram for 1 month OR reject the cash offer and keep using
Instagram.
It is in your best interest to answer honestly because any of
these cash offers may be randomly selected as the real offer
you will get in exchange for deactivating Instagram.
WTA 150
In the following question, we will ask you to think about the
minimum amount of money (in US $) you would require to
    
Keep using Instagram and turn
down cash offer
Accept cash offer and deactivate
Instagram for 1 month
$5   
$10   
$15   
$20   
$25   
$30   
$35   
$40   
$45   
$50   
$55   
$60   
$65   
$70   
$75   
$80   
$85   
$90   
$95   
$100   
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 8/13

deactivate Instagram for 1 month.
 
We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select 1 in150
respondents and give them a chance to get up to $150 if they
follow up on their choices.
 
The procedure to get the reward works as follows:
We will randomly select 1 in 150 respondents.
For this respondent, we will randomly select one of the
rows below.
If you choose to deactivate Instagram in exchange for the
amount mentioned in that row, we will email you and ask
you to deactivate Instagram for 1 month starting from that
date.
At the end of the month, if you kept your account
deactivated throughout the month, we will pay you the
amount mentioned in that row.
If you choose to not deactivate Instagram in exchange for
the amount mentioned in that row, you don't have to do
anything and you will not get any bonus payment.
Therefore, it is in your best interest to think carefully and
truthfully report which of the following amounts of money
you would accept to deactivate Instagram for 1 month.
 
Note that if your answers are not consistent (for example, if
you choose to accept a lower cash offer but reject a higher
cash offer), your response will be rejected.
For each of the possible cash offers below, please choose
whether you prefer to accept the cash and deactivate
Instagram for 1 month OR reject the cash offer and keep using
Instagram.
    
Keep using Instagram and turn
down cash offer
Accept cash offer and deactivate
Instagram for 1 month
$5   
$10   
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0Y… 9/13

It is in your best interest to answer honestly because any of
these cash offers may be randomly selected as the real offer
you will get in exchange for deactivating Instagram.
    
Keep using Instagram and turn
down cash offer
Accept cash offer and deactivate
Instagram for 1 month
$15   
$20   
$25   
$30   
$35   
$40   
$45   
$50   
$55   
$60   
$65   
$70   
$75   
$80   
$85   
$90   
$95   
$100   
$105   
$110   
$115   
$120   
$125   
$130   
$135   
$140   
$145   
$150   
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0… 10/13

WTA 200
In the following question, we will ask you to think about the
minimum amount of money (in US $) you would require to
deactivate Instagram for 1 month.
 
We want to reward you for thinking carefully about these
questions. Therefore, we will randomly select 1 in 200
respondents and give them a chance to get up to $200 if
they follow up on their choices.
 
The procedure to get the reward works as follows:
We will randomly select 1 in 200 respondents.
For this respondent, we will randomly select one of the
rows below.
If you choose to deactivate Instagram in exchange for the
amount mentioned in that row, we will email you and ask
you to deactivate Instagram for 1 month starting from that
date.
At the end of the month, if you kept your account
deactivated throughout the month, we will pay you the
amount mentioned in that row.
If you choose to not deactivate Instagram in exchange for
the amount mentioned in that row, you don't have to do
anything and you will not get any bonus payment.
Therefore, it is in your best interest to think carefully and
truthfully report which of the following amounts of money
you would accept to deactivate Instagram for 1 month.
 
Note that if your answers are not consistent (for example, if
you choose to accept a lower cash offer but reject a higher
cash offer), your response will be rejected.
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0… 11/13

For each of the possible cash offers below, please choose
whether you prefer to accept the cash and deactivate
Instagram for 1 month OR reject the cash offer and keep using
Instagram.
    
Keep using Instagram and turn
down cash offer
Accept cash offer and deactivate
Instagram for 1 month
$5   
$10   
$15   
$20   
$25   
$30   
$35   
$40   
$45   
$50   
$55   
$60   
$65   
$70   
$75   
$80   
$85   
$90   
$95   
$100   
$105   
$110   
$115   
$120   
$125   
$130   
$135   
$140   
$145   
$150   
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0… 12/13

Powered by Qualtrics
It is in your best interest to answer honestly because any of
these cash offers may be randomly selected as the real offer
you will get in exchange for deactivating Instagram.
Thank you
Thank you for participating in our study. We will email you if
you are selected for the additional rewards.
    
Keep using Instagram and turn
down cash offer
Accept cash offer and deactivate
Instagram for 1 month
$155   
$160   
$165   
$170   
$175   
$180   
$185   
$190   
$195   
$200   
7/16/25, 10:08 AM Qualtrics Survey Software
https://mit.co1.qualtrics.com/Q/EditSection/Blocks/Ajax/GetSurveyPrintPreview?ContextSurveyID=SV_3WXT6UmrKppo2fI&ContextLibraryID=UR_9ZTpo8t0… 13/13
