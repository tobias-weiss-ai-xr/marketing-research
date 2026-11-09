---
title: Influencer Cartels
url: https://arxiv.org/abs/2405.10231
category: digital-marketing
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Marit Hinnosaar
- Toomas Hinnosaar
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.10231
pages: 70
chars: 149306
fetched_at: '2026-11-08T13:11:35+00:00'
kb_version: 1
---

# Influencer Cartels

Influencer Cartels∗
Marit Hinnosaar† Toomas Hinnosaar‡
May 27, 2026
Abstract
Social media influencers account for a growing share of marketing worldwide. We
demonstrate the existence of a novel form of market failure in the advertising mar-
ket: influencer cartels, where groups of influencers collude to increase their advertising
revenue by inflating their engagement. Our theoretical model shows that influencer
cartels can improve consumer welfare if they expand social media engagement to the
target audience, or reduce welfare if they divert engagement to less relevant audiences.
Drawing on the model’s insights, we empirically examine influencer cartels using novel
datasets and machine learning tools, and derive policy implications.
JEL: L82, M31, D26, L14
Keywords: influencers, marketing, collusion, Natural Language Processing, Large Lan-
guage Models, Latent Dirichlet Allocation
∗We are grateful to the editor Pierre Dubois and anonymous referees for guidance in revising the paper.
We thank the data editor Maia G¨ uell and the anonymous replicator for verifying the replication package. We
also thank Daniel Ershov, Carl-Christian Groh, John Horton, Dina Mayzlin, Matt Mitchell, Devesh Raval,
Johanna Rickne, Stephen P. Ryan, Stephan Seiler, Egor Starkov, and seminar participants at University of
East Anglia, University of Leicester, University of Nottingham, Collegio Carlo Alberto, Mannheim Virtual
IO Seminar, UK Competition and Markets Authority (CMA), 12th Paris Conference on Digital Economics,
IIOC, Munich Summer Institute, Baltic Economics Conference, Australasian Meeting of the Econometric
Society, NBER Summer Institute on IT and Digitization, Econometric Society European Meeting, EARIE,
NIE Annual Conference, 13th Workshop on the Economics of Advertising and Marketing, Bristol-Warwick
Empirical IO Workshop, Berlin IO Day, 6th Monash-Warwick-Zurich Text-as-Data Workshop, CESifo Eco-
nomics of Digitization Conference, Text-as-Data in Economics Workshop in Liverpool, City/CMA Work-
shop on Economics of Competition and Regulation, Theory and Policy in the Digital Economy Workshop
in Durham, Workshop on Collusion in Markets in Tinbergen Institute Amsterdam, SAET, CEPR Virtual
IO Seminar, and CEPR Paris Symposium for helpful comments and suggestions. Refine.ink was used to
proofread the paper for consistency and clarity. First draft: February 12, 2021.
†University of Nottingham and CEPR,marit.hinnosaar@gmail.com
‡University of Nottingham and CEPR,toomas@hinnosaar.net
1
arXiv:2405.10231v3  [econ.GN]  21 Jun 2026

1 Introduction
Collusion between a group of market participants to improve their market outcomes is typ-
ically considered anticompetitive behavior. While some forms of collusion, such as price-
fixing, are illegal in most countries, new industries provide new collusion opportunities for
which regulation is not yet well developed. In this paper, we study one such industry—
influencer marketing. Influencer marketing combines paid endorsements and product place-
ments by influencers. It allows advertisers to fine-target based on consumer interests by
choosing a good product-influencer-consumer match. Influencer marketing is a large and
growing industry; with 31 billion U.S. dollars in ad spending in 2023, it is almost as large as
the print newspaper advertising. 1
Many non-celebrity influencers are not paid based on the success of their marketing cam-
paigns; instead, their compensation depends on past engagement. 2 This gives incentives
for fraudulent behavior—for inflating their influence. Inflating one’s influence is a form of
advertising fraud that leads to market inefficiencies by directing ads to the wrong eyeballs.
An estimated 15% of influencer marketing spending was misused due to exaggerated influ-
ence.3 To address this problem, the U.S. Federal Trade Commission in 2024 introduced a
new rule that prohibits selling and buying fake indicators of social media influence, such as
fake followers or views. 4 In this paper, we study a way of obtaining fake engagement that
does not directly fall under the proposed rule, but is in the same spirit. We study influencer
cartels where groups of influencers collude to increase each other’s indicators of social me-
dia influence. 5 While there is substantial literature in economics on fake consumer reviews
(Mayzlin et al., 2014; Luca and Zervas, 2016; He et al., 2022; Glazer et al., 2021; Smirnov and
Starkov, 2022) and other forms of advertising fraud (Zinman and Zitzewitz, 2016; Rhodes
and Wilson, 2018), the economics of this fraudulent behavior has not been studied.
We study how influencers collude to inflate engagement, and the conditions under which
1Source:https://www.statista.com/outlook/amo/advertising/worldwide, accessed March 17,
2024.
2While influencers with large followings are typically paid based on campaign performance (tracked
through sales from personalized links or discount codes), only 19% of firms employing influencer marketing
reported tracking sales during the period covered by our sample (ANA, 2020). More recent industry data
suggest that this share has increased to about 29% (CreatorIQ, 2024).
3Source:https://en.wikipedia.org/wiki/Influencer_marketing, accessed April 6, 2024.
4Source: Federal Trade Commission, August 14, 2024, “Federal Trade Commission Announces Final Rule
Banning Fake Reviews and Testimonials”,https://www.ftc.gov/news-events/news/press-releases/
2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials,
accessed November 21, 2025.
5 On various platforms, these groups are called different names, such as “pods” on Instagram and “ex-
changes” on SoundCloud. We use the term “cartels” instead of a neutral term like “club” to highlight
that their primary objective is to manipulate the marketplace to obtain higher prices through prohibited
practices, which mirror the traditional concept of cartels.
2

influencer cartels can be welfare-improving. Our research makes three key contributions.
First, we develop a new theoretical framework for influencer cartels, a setting that has not
been studied before. Second, we use a novel dataset of influencer cartels and machine learning
tools to generate engagement quality measures from text and photos. Third, for each type
of cartel, we estimate whether it is likely to be welfare-improving or not. We document
that general cartels generate lower-quality engagement than topic cartels, which are closer
to natural engagement. This suggests that narrow, topic cartels could improve welfare, while
general cartels are detrimental to all involved.
In an influencer cartel, a group of influencers colludes to inflate their engagement, in
order to increase the prices they can get from advertisers. As in traditional industries,
influencer cartels involve a formal agreement to manipulate the market for members’ benefit.
In traditional industries, the agreement typically involves price fixing or allocating markets.6
Influencer cartels involve a formal agreement to inflate the engagement measures to increase
their prices. Instead of smoky backroom deals, influencer cartels operate in online chat
rooms or discussion boards, where members submit links to their content for additional
engagement. In return, they must engage with other members’ content by providing likes
and meaningful comments. An algorithm enforces the cartel rules.
Our theoretical model focuses on the key market failure in this setting—the free-rider
problem. Engaging with other influencers’ content brings attention to someone else’s content,
creating a positive externality. Without cartels, influencers do not engage with each other’s
content enough, because they do not internalize the externality. A cartel could lessen the
free-rider problem by internalizing the externality. By joining the cartel, influencers agree
to engage more than the equilibrium engagement. They are compensated for this additional
engagement by receiving similar engagement from other cartel members. If the cartel only
brings new engagement from influencers with closely related interests, this could benefit cartel
members but also consumers and advertisers. However, the influencer cartel can also create
new distortions. The cartel may overshoot and create too much low-quality engagement. The
low-quality engagement may hurt all involved parties, consumers, advertisers, and indirectly,
even the influencers themselves.
The dimension that separates socially beneficial cooperation from welfare-reducing cartels
is the quality of engagement. By high quality we mean engagement coming from influencers
with similar interests. The idea is that influencers provide value to advertisers by promoting
the product among people with similar interests, e.g., vegan burgers to vegans. If a cartel
generates engagement from influencers with other interests (e.g., meat-lovers), this hurts
consumers and advertisers. Consumers are hurt because the platform shows them irrelevant
6Collusion in cartels does not always occur via fixing prices or output (Genesove and Mullin, 2001).
3

content, and advertisers are hurt because their ads are shown to the wrong consumers.
Whether or not a particular cartel is welfare-reducing or welfare-improving is an empirical
question.
In our empirical analysis, we combine data from two sources: cartel interactions from
Telegram and data from Instagram. Our cartel data allows us to directly observe cartel
activity (not predict or estimate it). We observe which Instagram posts are included in the
cartel and which engagement originates from the cartel. 7 Our dataset includes two types of
cartels differentiated by cartel entry rules: three topic cartels that only accept influencers
posting on specific topics and six general cartels with unrestricted topics. 8
We use machine learning to analyze text and photos from Instagram to measure engage-
ment (match) quality. Our goal is to compare the quality of natural engagement to that
originating from the cartel. We measure quality by the topic match between cartel members
and users who engage with their content. To quantify the similarity of Instagram users we
use Large Language Models to convert text and photos to numeric vectors (embeddings)
and calculate cosine similarity between users based on these vectors. We then estimate a
panel data fixed effects regression with cosine similarity as the outcome. We complement the
analysis using the Latent Dirichlet Allocation to map each user’s content into a distribution
over topics.
We find that engagement from general cartels is significantly lower in quality compared
to natural engagement. Specifically, the quality of engagement from these cartels is nearly as
low as that from a counterfactual engagement from a random Instagram user. In contrast,
engagement from topic cartels is much closer to the quality of natural engagement. Our
back-of-the-envelope calculations show that if an advertiser pays for cartel engagement as
if it is natural engagement, they only get 3–18% of the value in the case of general cartels
and 60–85% in the case of topic cartels. Our results are robust to alternative ways to con-
struct outcome variables and alternative samples. Our estimates also validate our outcome
measures: advertisers are known to pay higher fees for more engagement, and we show that
users with higher similarity are more likely to engage. This implies our similarity measures
capture what advertisers value.
The trade-offs studied in this paper can arise in other settings. Lampe (2012) shows that
7The ability to directly observe cartel activity is rather unique. Most studies of cartels in traditional
industries have to rely on either historical data of known cartels from the time cartels were legal (Porter,
1983; Genesove and Mullin, 2001; R¨ oller and Steen, 2006; Hyytinen et al., 2018, 2019) or data from the court
cases (Igami and Sugaya, 2022), including bidding rings in auctions (for example, Porter and Zona (1993);
Pesendorfer (2000); Asker (2010); Kawai et al. (2026)), for an overview see Marshall and Marx (2012).
8To make the results comparable, we only study cartels by the same cartel organizer; they all run on the
same platform and have the same engagement requirements. The cartels differ only in entry requirements:
some cartels have topic restrictions, while others have minimal follower requirements.
4

patent applications strategically withhold citations. To overcome the free-rider problem,
firms have formed patent pools—agreements to cross-license their patents (Lerner and Tirole,
2004; Moser, 2013). 9 There is also evidence of citation agreements in academic publishing
(Franck, 1999; Van Noorden, 2013; Wilhite and Fong, 2012). Due to anomalous citation
patterns, Clarivate (formerly Thomson Reuters) regularly excludes journals from Impact
Factor listings.10 There are differences between these settings and influencer cartels. First,
in citation cartels, explicit agreements are unobservable, whereas collusion and outcomes are
directly observable in influencer cartels. Second, patent and academic citations have rather
objectively defined relevance.
Our paper adds to the literature on social media and attention (for an overview, see Aridor
et al. (2024)). While the literature on social media has extensively studied the consumption
and production of social media content, there is less work on strategic engagement, which is
the strategic choice of which content to engage with. Our paper is most closely related to
Filippas et al. (2025), who use Twitter data to study attention bartering. Similarly to our
paper, they model social media users’ decision to engage (in their setting, whether to follow
other users) as a partially reciprocal process. Unlike us, they study pairwise agreements and
they focus on vertically differentiated social media users (i.e., whether social media stars
engage with users who have a smaller number of followers), whereas we focus on horizontal
differentiation (topics and topic similarities). Another key difference is that in Filippas
et al. (2025), users know each other’s characteristics before deciding to barter, whereas in
our setting, cartel members commit to engagement without knowing whose content they
will engage with. Finally, Filippas et al. (2025) don’t model advertising, which plays a key
role in our analysis. Our theoretical model of influencer engagement and advertisement
builds on classic models of product differentiation (Salop, 1979) and models of attention and
advertising (Anderson and Coate, 2005; Anderson and de Palma, 2012; Anderson and Peitz,
2023). Unlike all these papers, we study the groups of users who agree to collude in order
to increase engagement.
Our paper adds to a small but growing literature in economics on influencer marketing.
The empirical literature has analyzed advertising disclosure (Ershov and Mitchell, 2025; Er-
shov et al., 2025), while the theoretical literature has studied the benefits of mandatory
disclosure (Pei and Mayzlin, 2022; Mitchell, 2021; Fainmesser and Galeotti, 2021), the prior-
itization of content (Szydlowski, 2023), and social learning with influence-motivated agents
(Song, 2025). In contrast to these papers, we study collusion between influencers. Influencer
9Patent pools are also formed for reasons beyond internalizing externalities, including reducing transaction
costs and addressing blocking patents.
10Source:https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351398819089-
Title-Suppressions, accessed December 16, 2025.
5

cartels have been studied qualitatively in marketing and media studies: O’Meara (2019) ex-
amined them through the lens of organized labor, Cotter (2019) analyzed discussions among
influencers in closed Facebook groups, including those on Instagram cartels, and Miguel
et al. (2022) conducted in-depth interviews with 20 food influencers on Instagram cartels.
Influencer cartels have been studied quantitatively in computer science. Weerasinghe et al.
(2020) analyzed approximately two million Instagram posts included in cartels and built a
classifier to predict whether a post is part of a cartel. None of these studies analyze the
welfare effects or the type of engagement that is generated by influencer cartels.
Our paper also contributes to the literature on welfare-improving cartels. The literature
has shown that with negative externalities, such as environmental damage, collusion can
improve welfare (Buchanan, 1969; Schinkel and Spiegel, 2017; Schinkel et al., 2022; Asker
et al., 2024). Fershtman and Pakes (2000) showed that the positive effect of collusion on
product variety may make collusion welfare-improving. Deltas et al. (2012) showed that
collusion may be welfare-improving due to reduced trade costs. In contrast, in our paper the
beneficial aspect of collusion arises from a positive externality to other influencers, which
can be internalized through reciprocal engagement.
In our empirical analysis, we build on the recent literature in economics that uses text and
photos as data. 11 In particular, we use Large Language Models and large neural networks
to generate embeddings from text and photos. Large Language Models with social media
data have been used in economics before, for example, by Ershov et al. (2025). We also
use the Latent Dirichlet Allocation model (Blei et al., 2003), which has been recently used
in economics, for example, to extract information from Federal Open Market Committee
meeting minutes (Hansen et al., 2018). We combine these tools with the use of the cosine
similarity index. This and other similarity indexes have been used as quality measures
in economics, for example, by Chen et al. (2024) and Hinnosaar et al. (2022). While many
studies have made use of text as data, using photos is still rare in economics (examples include
Adukia et al. (2023); Ash et al. (2021); Caprini (2023)). 12 As Instagram as a platform is
primarily used to share photos, extracting information from photos is particularly important
in our setting.
The rest of the paper is organized as follows. In the next section, we provide some
institutional details of influencer cartels. Section 3 introduces the theoretical model and
discusses the welfare implications of influencer cartels. Section 4 describes the dataset used
in our analysis. Section 5 presents the empirical results. Section 6 concludes.
11For surveys of the uses of text as data in economics, see Gentzkow et al. (2019); Ash and Hansen (2023).
12One exception is the use of satellite images mostly in development economics, and typically, to measure
electricity use, air pollution, land use, or natural resources (Donaldson and Storeygard, 2016).
6

2 Background: Influencer Cartels
In influencer marketing, firms pay influencers for product placements and endorsements.
Many non-celebrity influencers are compensated based on engagement metrics, which gives
incentives to inflate the engagement. In an influencer cartel, a group of influencers collude to
inflate each other’s engagement in order to increase the prices they can get from advertisers.
Instagram considers these groups to be violating Instagram’s policies 13 and has closed down
influencer cartels with hundreds of thousands of members. 14
Influencer cartels operate in an online chat room or a discussion board, typically on Tele-
gram or Reddit. 15 The cartels in our sample operate in Telegram chat rooms and advertise
themselves as a way to “attract lucrative brand partnerships” (see screenshots in Figure A1.1
in the Online Appendix). In the chat room, members of the cartels submit links to their
Instagram content for which they would like to receive additional engagement. In order to
receive that engagement, they themselves must engage with a fixed set of links submitted by
other users. Specifically, the cartels have the requirement that before submitting a post, the
member must like and write meaningful comments to previousN(in our sample, at least the
last five) posts submitted by other members. Figures A1.2 and A1.3 in the Online Appendix
show an example of a post submitted to the cartel receiving the required comments. The
rules of the cartel are enforced automatically by an algorithm. The cartels in our sample
have entry requirements: either thresholds for the minimum number of followers (ranging
from 1,000 to 100,000 followers) or restrictions on the topics of the posts.
The cartel increases engagement via both direct effect and indirect effects. The direct
effect is the cartel members engaging with each other’s posts. This additional engagement
generates two types of indirect effects. First, the Instagram algorithm gives higher exposure
to posts with higher engagement, leading to even more engagement. Second, an influencer
engaging with another user’s post increases the likelihood of the post being shown to the
influencer’s followers. This happens as the Instagram algorithm is more likely to show posts
that the user’s social network has engaged with, that is, posts that the users who the user
follows have commented on or liked. 16
13Source: Devin Coldewey, Apr 29, 2020, “Instagram ‘pods’ game the algorithm by coordinating likes
and comments on millions of posts”, TechCrunch.https://techcrunch.com/2020/04/29/instagram-pods-game-the-
algorithm-by-coordinating-likes-and-comments-on-millions-of-posts/.
14Source:https://www.buzzfeednews.com/article/alexkantrowitz/facebook-removes-ten-
instagram-algorithm-gaming-groups-with, accessed August 19, 2024.
15For more details, see a computer science overview of Instagram cartels operating on Telegram (Weeras-
inghe et al., 2020) or for example: Apr 9, 2019 “Instagram Pods: What Joining One Could Do For Your
Brand”, Influencer Marketing Hub.https://influencermarketinghub.com/instagram-pods/.
16Figure A1.4 in Online Appendix A1 presents a screenshot of an Instagram post that was recommended
to the user because their friend liked it.
7

How widespread are influencer cartels? This question is inherently difficult to answer, as
the goal of influencers joining such cartels is to generate engagement that is indistinguishable
from natural engagement. The challenge is similar to other forms of hidden misconduct, such
as accounting fraud or corruption, where most behavior goes unreported or undetected. For
example, Dyck et al. (2010) document that detected cases of corporate fraud represent only
a small fraction of the true incidence. Likewise, Leuz et al. (2003) show how measurement
problems arise when misreporting is endogenous to detection and enforcement. To provide
some background context, Online Appendix A2 presents suggestive evidence from Google
Trends on the widespread interest in influencer cartels (Google LLC, 2024).
Our data does not allow us to estimate a causal impact of cartel participation on en-
gagement beyond the direct effect. However, we provide correlational evidence (discussed in
Section 4.4) showing that, after joining the cartels, influencers’ posts receive more engage-
ment and influencers are more likely to have disclosed sponsored content. Furthermore, the
screenshot in Figure A1.1b (Online Appendix A1) shows that the main arguments the cartel
organizer uses to convince influencers to join are related to growth in profile prominence and
earnings. The fact that these cartels attract many long-term members indicates that at least
some influencers expect and perceive cartels to have a positive impact on both engagement
and earnings.
3 Theoretical Model
We start with a simple model that captures the main trade-offs behind influencer engagement
and later extend it to more general settings. The analysis focuses onengagement, the activity
that influencer cartels directly coordinate. All other aspects of influencer marketing, such as
content creation or audience growth, are assumed to be independent of engagement choices.
3.1 Model Setup
The model consists of three types of agents: influencers, their followers, and advertisers.
There is a continuum of influencers, each having some content. Influencers differ by topic:
each influencer is characterized by a typeα∈[0,2π], denoting a location on the Salop (1979)
circle.17 The distribution of topics is uniform around the circle.
Each influencerαis randomly matched with another influencerα ′, whose content influ-
encerαmay engage with. 18 Ifαengages withα ′, we denote this bye(α ′|α) = 1; otherwise,
17Topicαis measured in radians, corresponding to 360◦ 2π α∈[0 ◦,360 ◦]. 18We thank an anonymous referee for the suggestion to model engagement through pairwise matches. The
results would not change if each influencerαwere matched with two random influencers,α ′ andα ′′, so that
8

e(α′|α) = 0.
Influencerαhas a continuum of followers with total measureR. If influencerαengages
with the content of influencerα ′, then all followers ofαare exposed to the content created
byα ′. The utility to each follower ofαfrom such engagement is 19
U F =e(α ′|α)  cos(∆)−C(∆)  ,(1)
where ∆ =d(α, α ′) denotes the distance between topicsα ′ andα. The first term, cos(∆),
represents the informational or entertainment value of engagement, whileC(∆) captures the
cost of attention. 20
The cost function is assumed to be
C(∆) =



sin(∆),if ∆≤ π 2 ,
1,if ∆> π 2 . (2)
Each influencer is matched with an advertiser promoting a product related to that topic.
Hence, when influencerαengages with the content ofα ′, the followers ofαare also exposed
to the advertisement associated withα ′. The probability that a follower purchases the
product is increasing in the topic match cos(∆). Letv≥0 denote the surplus generated per
successful purchase. We assume that the total value created by engagement isRvcos(∆).
The payoff for an advertiser is
U A =e(α ′|α)  Rvcos(∆)−p  ,(3)
wherepis theprice of engagement, i.e., the payment from the advertiser to influencerα ′.
Advertisers, however, observe only thequantityof engagement rather than its source
orquality. We assume that the advertising market is competitive,E[U A] = 0, hence the
expected payment from the advertiser to the influencerα ′ is21
p=RvE[cos(∆)|e(α ′|α) = 1].(4)
We assume that influencers care about advertising revenue as well as the value they
αcan engage withα ′′, andα ′ can engage withα.
19Our modeling assumptions regarding the costs and benefits of attention are similar to models of attention
and advertising (Anderson and Coate, 2005; Anderson and de Palma, 2012; Anderson and Peitz, 2023), who
also model the cost of attention as a difference between consumers’ preferences and the content they consume.
This literature does not consider the externality that is our main focus.
20d(α, α′) = min{ |α′ −α|,2π− |α′ −α| } ∈[0, π] denotes the shortest angular distance on the circle.
21Later we relax this assumption. The results remain qualitatively the same whenpis determined by Nash
bargaining between the influencer and the advertiser.
9

provide to their followers. The payoff of influencerαwho is matched withα ′ consists of
four parts. Ifαengages withα ′, she bears the attention costC(∆) of her followers and
internalizes only a fractionγ∈(0,1) of the benefit created. The remaining share, 1−γ, is
an external benefit to influencerα ′, who receives this engagement. In addition, the recipient
of engagement receives the advertising incomep. Formally,
U I =e(α ′|α)  γcos(∆)−C(∆)  +e(α|α ′)  (1−γ) cos(∆) +p  .(5)
The influencer’s payoff captures the idea that the current value provided to followers has
a persistent impact, with asymmetric costs and benefits. The more different the content
is, the greater the attention cost for followers. We assume that the influencer internalizes
followers’ attention costs, which in reduced form captures the idea that the more different
the content is, the more likely followers are to stop following. Conversely, if followers find
the content interesting, both the content creator and the engaging influencer benefit, which
in reduced form captures that they gain followers. Importantly, when the influencer engages
with dissimilar content, the content creator’s followers and therefore the content creator are
not affected. Thus, the costs of engaging are borne only by the influencer who engages, while
high-quality engagement benefits both parties.
The total welfare from all engagements is
W=E

U I +RU F +U A ,(6)
where the expectation is taken over all interacting pairs of influencers (α, α ′).
We consider two types of engagement behavior. Undernatural engagement, influencers
decide independently whether to engage each time they have an opportunity to do so. Under
cartel engagement, the decision is determined by algorithmic rules imposed by the cartel,
conditional on membership. We first consider each type of engagement in isolation, and then
their interaction.
3.2 Only Natural Engagement
We assume first that each influencer independently chooses whether or not to engage with
the influencer they are matched with. Taking the difference inU I between engagement and
no engagement, we get that the net value of engagement isγcos(∆)−C(∆). This expression
is positive if and only ifγ≥tan(∆), which gives the natural engagement function
eN (α′|α) =1[∆≤Λ N ],(7)
10

where ΛN = arctan(γ)<arctan(1) = π 4 is the natural engagement threshold. 22
Importantly, influencerαdoes not internalize the positive externality that her engage-
ment creates forα ′. In contrast, socially optimal engagement would account for this exter-
nality. The socially optimal engagement function ise S(α′|α) =1[∆≤Λ] for some Λ∈[0, π].
The corresponding social welfare function can be written as 23
W(Λ) = 1 π Z Λ 0  (R+ 1 +Rv) cos(∆)−(R+ 1)C(∆)  d∆.(8)
The welfare-maximizing cutoff is Λ S(v) = arctan  1 + Rv R+1  , which is strictly increasing
inv, satisfies Λ S(0) = π 4 , and converges to π 2 asv→ ∞.24
The following proposition summarizes the equilibrium and the social optimum.
Proposition 1.There exists a unique equilibrium. There is more engagement in the social
optimum than in equilibrium (natural engagement), but the additional engagement is of lower
quality. In particular:
1. In equilibrium,e N (α′|α) =1[∆≤Λ N ], whereΛ N = arctan(γ)< π 4 .
2. In social optimum,e S(α′|α) =1[∆≤Λ S(v)], whereΛ S(v)is a strictly increasing
function ofv, satisfyingΛ S(0) = π 4 andlim v→∞ ΛS(v) = π 2 .
Hence, socially optimal engagement involves more engagement than natural engagement,
but the additional engagement has lower topic similarity (lower quality). Moreover, for all
v, Λ N < π 4 ≤Λ S(v)< π 2 .
3.3 Only Cartel Engagement
Suppose that, instead of natural engagement, engagement arises through a cartel. Specifi-
cally, the cartel rules define an engagement requirement Λ∈[0, π], such that the engagement
function is given bye C(α′|α) =1[∆≤Λ]. All cartel members are assumed to follow this
rule.25 Influencers therefore choose only whether to join the cartel, making this decision
before learning the identity of their match. Advertisers are aware of the cartel’s existence
and the price of engagement reflects the specific value of Λ. The objective of the cartel is to
maximize the expected payoff of its members.
22The angle π 4 corresponds to 45 ◦. 23We define social welfare as the sum of all agents’ payoffs. We use this specification for tractability, and
our qualitative results would be unchanged if welfare were evaluated separately for different groups of agents.
24Proofs and derivations are in Online Appendix A3.1.
25In practice, the rules are enforced by an algorithm that automatically detects and penalizes deviations.
11

The expected payoff from joining a cartel with engagement threshold Λ is
E[U C] = 1 π Z Λ 0  (1 +Rv) cos(∆)−C(∆)  d∆.(9)
Before studying the optimal cartel, it is useful to describe which values of Λ are feasible,
that is, for which values of Λ influencers are willing to join the cartel. There exists a maximal
threshold Λ max ∈[0, π] such that influencers are willing to join the cartel only if Λ≤Λ max.
Moreover, π 2 ≤Λ max < π.26
The optimal Λ that maximizes (9) is ΛC(v) = arctan(1 +Rv). This leads to the following
proposition.
Proposition 2.Feasible cartel engagement levels belong to[0,Λ max], where π 2 ≤Λ max < π.
The optimal cartel engagement levelΛ C(v)is a strictly increasing function ofv, with
ΛC(0) = Λ S(0) = arctan(1) = π 4 andlim v→∞ ΛC(v) = π 2 . Moreover, for allv >0,Λ C(v)>
ΛS(v).
To interpret this result, note that the optimal cartel internalizes the externality among
influencers by making engagement reciprocal. Thus, it can achieve higher welfare than
natural engagement. However, as long as there is some advertising revenue, i.e.,v >0,
the cartel engagement goes even further than socially optimal engagement, because the
optimal cartel does not internalize the impact on followers beyond what is already reflected
in influencers’ payoffs and therefore places relatively greater weight on advertising revenue.
3.4 Both Natural and Cartel Engagement
We now combine natural and cartel engagement by assuming that a mass 1−εof influencers
choose their engagement freely, that is, they follow natural engagement. The remaining mass
ε >0 of influencers is divided into a large number of cartels, where each carteli∈ {1, . . . , m}
independently chooses its engagement level ΛC i . The allocation of influencers into cartels and
natural engagement is independent of their topic. We assume thatεis small but positive.
Importantly, advertisers knowε, but are unable to distinguish between different types of
engagement (natural or cartel), and thus the advertising pricepis determined by the expected
engagement across all types. We focus on the limiting case asm→ ∞. In that limit, the
choice of Λ C i does not affect the price of engagement. 27
First, consider influencers who do not belong to cartels, that is, those who choose en-
gagement naturally. For them, the optimal engagement has not changed, because the only
26Proofs and derivations are in Online Appendix A3.2.
27Proofs and derivations are in Online Appendix A3.3.
12

difference with the analysis above is the changed advertising price, and their advertising
revenue does not depend on their own engagement decision. Therefore, their engagement
function remainse N (α′|α) =1[∆≤Λ N ], where Λ N = arctan(γ).
For a member of carteli, the analysis is different, as the price of advertising is
p(ε) =RvE[cos(∆)|e(α ′|α) = 1] =Rv (1−ε) sin(Λ N ) +εsin(Λ C) (1−ε)Λ N +εΛ C ≥vRρ(ε, γ),(10)
where Λ C is the engagement requirement of other cartels, which is equal for all cartels in
equilibrium, andρ(ε, γ) is strictly positive for anyε, γ∈(0,1). The payoff to a member of
carteliis
E[U C i ] = 1 π Z ΛC i 0  cos(∆)−C(∆) +p(ε)  d∆.(11)
Because each individual cartel is small,p(ε) is taken as given.
We refer to cartels with ΛC i =πasgeneral cartels, since they place no restrictions on the
topic similarity.28 We show that general cartels are feasible and optimal for sufficiently large
v. Due to the existence of natural engagement, the price of engagement is bounded below
by a constant multiplied byv. Therefore, whenvis large, the advertising revenue dominates
any other incentives.
Proposition 3.For anyε <1andR >0, there existsbv >0such that ifv≥bv, then all
cartels are general cartels, i.e., they set the required engagement level toΛ C i =π.
Intuitively, these optimal cartels generate pure noise in terms of topic match. More
precisely, general cartels with ΛC i =πhaveE[cos(∆)|∆≤Λ C i ] = 0, so there is no benefit to
followers or surplus to advertisers, while the costs to followers (attention) and to influencers
are strictly positive. Moreover, the cartels lower the price of engagement and therefore reduce
the payoff of non-cartel members as well.
Corollary 1.If cartels are general cartels withΛ C i =π, then
1. Cartels strictly reduce social welfare.
2. Non-cartel influencers would strictly prefer a lower share of cartels.
3. Cartel members would strictly prefer a lower share of cartels.
28In our data, there are two types of cartels: general cartels, with no restrictions on topics, and topic
cartels, which restrict entry to specific topics. In our theoretical model, the case where Λ C i ≪πcaptures
the essence of topic cartels, as only engagement with relatively closely related content is required.
13

3.5 Interpretation of the Model
The model presented above can be extended in many directions without changing the main
conclusions. The key elements are: (1) the free-rider problem under natural engagement—as
influencers’ engagement choices create positive externalities for others, there is insufficient
engagement in equilibrium relative to the socially optimal level; (2) the cartel can internalize
this externality through reciprocal engagement; and (3) the distortion from the advertising
market—because advertisers cannot distinguish high-quality engagement from low-quality
engagement, and realistic cartels are too small to have a substantial impact on market prices,
it may be optimal to organize a cartel that maximizes engagement quantity by generating
what is essentially low-value engagement. Before discussing possible extensions, we briefly
outline the motivation behind our modeling choices.
Our model captures the manipulation of followers’ attention. Engagement by influencerα
with contentα ′ signals to the platform algorithm that this content may be relevant for users
with similar interests toα, which includesα’s followers. Consequently, this content is shown
to these followers with higher probability. The follower’s payoff function, cos(∆)−C(∆), is
strictly decreasing in ∆: it is high and positive for small ∆ (followers enjoy consuming such
content), but negative for large ∆, where the cost of attention exceeds the value of being
shown irrelevant content.
3.6 Extensions
3.6.1 Sequential Engagement Choices
For simplicity, we have so far presented engagement choices as simultaneous. In practice,
such interactions are inherently dynamic: influencers post content over time and can only
engage with content that has already been created.
The presented model can be reinterpreted as a model of a dynamic process. Consider an
infinite sequence of influencers, where influencerthas typeα t. Influencertcan choose to
engage with the content of influencert−1, at distance ∆ t =|α t −α t−1|. The only difference
from our baseline model is that we previously assumed engagement choices were matched,
i.e.,tcould engage witht−1 and vice versa, but since types are independently drawn, this
assumption does not affect the analysis.
Again, it is both important and natural to assume that when influencers join the cartel,
they do not yet know the characteristics of the content they may be required to engage with.
14

3.6.2 Advertisers with Bargaining Power
We have so far assumed that advertisers are competitive, so that the price of engagementp
equals the expected surplus generated for advertisers. This assumption can be relaxed by
allowingpto be determined through Nash bargaining, with bargaining powerβ >0 for the
influencer and 1−β >0 for the advertiser. In this case, the price of engagement is multiplied
byβthroughout, and advertisers obtain a strictly positive expected payoff proportional to
1−β. All conclusions remain unchanged, because from the influencer’s perspective, this is
equivalent to replacing the parametervwithβv. The only difference is that advertisers, too,
would now be strictly worse off in the presence of general cartels.
3.6.3 Advertisers Observing Engagement Quality
The key distortion in the model is that advertisers observe only whether engagement occurs,
but not its source or quality. This assumption reflects real-world influencer marketing,
where payments typically depend only on observable metrics such as the number of views,
comments, or likes. However, it is possible (although more costly) for advertisers to employ
more sophisticated tracking technologies and either (1) evaluate engagement quality as we do
in the empirical analysis, or (2) track sales generated by specific influencers and engagements.
In this case, the payment from the advertiser to the influencer would depend on the true
match quality rather than its expectation, that is,p=Rvmax{0,cos(∆)}, or a fractionβ
of it if the advertiser has bargaining power.
If we substituted this expression into the analysis above, cartels would never require
engagement above π 2 , because at this range the marginal advertising revenue is zero, and
even a fully internalized marginal benefit of engagement is strictly less than the cost. In
other words, general cartels can only exist because of imperfect observability.
3.6.4 Alternative Objectives of Cartels
In the main model, we assumed that the goal of the cartel is to maximize its members’
expected payoffs. This is a natural objective in a typical setting where a group of influencers
agree to cooperate: they want the cartel organizer to choose Λ that maximizes their payoffs.
However, the model also allows us to consider alternative objectives for the cartel organizer:
1.Socially optimal cartel:As we showed, the socially optimal cartel is always feasible
(ΛS(v)≤Λ max), so a cartel organizer seeking to maximize social welfare could imple-
ment it.
15

2.Engagement-maximizing cartel:The maximal feasible engagement level Λ max clearly
maximizes the amount of engagement among all feasible cartels.
3.Revenue-maximizing cartel:If a cartel could charge an entry feeϕ >0, the effective
value of joining the cartel would beE[U C]−ϕ, so all influencers would join as long as
ϕ≤E[U C]. The revenue-maximizing cartel would therefore setϕ=E[U C] and choose
Λ = ΛC as above, extracting the entire surplus created for influencers.
4.Advertising-revenue-maximizing cartel:Advertising revenue conditional on engage-
ment isp, which decreases in market-wide Λ, while the likelihood of engagement in-
creases in cartel’s own ΛC i . If the cartel is small enough not to have a significant impact
on the market price of engagement, it would choose Λ C i to maximize engagement.
Ifvis very large and each cartel is small, as discussed above, then all cases except the socially
optimal cartel lead to the same conclusion: all cartels are general cartels with Λ C i =π. This
is becauseπis the largest feasible reach (maximizing engagement), and with sufficiently high
v, maximizing engagement dominates all other considerations.
3.6.5 Heterogeneous Reach
So far, we have assumed that all influencers have the same number of followers,R. In Online
Appendix A4, we relax this assumption by allowing each influencertto be characterized by
a two-dimensional type (α t, Rt), whereα t is the topic, still distributed uniformly, andR t
denotes their reach (attention). We assume influencers’ payoffs depend on reach.
We show that all qualitative results remain unchanged: natural engagement remains
below the socially optimal level, while cartel engagement can exceed it. In particular, when
there are many small cartels and the advertising revenue is very important for influencers,
all cartels are general cartels.
The heterogeneous-reach extension provides additional insights. Cartels can now generate
two distinct distortions. Not only can they require excessively broad engagement (i.e., low-
quality topic matching), but high-reach influencers may also choose not to join, leading to
low-quality engagement in terms of reach.
High-reach influencers may abstain from joining because of the asymmetry between what
they contribute to the cartel (the attention of their own followers) and what they receive
in return (the attention of the followers of an average member). To address this, real-world
cartels often impose a minimum reach requirement. We show that cartels would indeed
sometimes find it optimal to impose a high entry requirement in terms of reach.
16

4 Data and Measures of Engagement Quality
4.1 Data Sources
We combine data from two sources: first, the detailed cartel communications from Telegram,
and second, Instagram posts and engagement data. A detailed description of our data
collection is in Online Appendix A5.
Telegram cartel history.From Telegram, we collected the communication history of nine
cartels: six general cartels and three topic cartels: fitness & health, fashion & beauty, travel
& food (Telegram FZ-LLC, 2020; Hinnosaar and Hinnosaar, 2020). This history provided
us with three relevant pieces of information for each submission: the Telegram username,
Instagram post shortcode, and the time of submission. According to the rules of these
cartels, a user must comment on and like at least five posts preceding their own submission
before submitting a post to the cartel for engagement.29 This rule allows us to clearly identify
which cartel members were bound to engage with which Instagram posts. In other words, we
directly observe, instead of having to infer, which posts are included in the cartel. Similarly,
we observe, instead of having to infer, which engagement originates from the cartel according
to the cartel rules. The Telegram cartels include 220,893 unique Instagram posts that we
were able to map to 21,068 Instagram users.
Instagram data.Our goal is to compare natural engagement to that acquired via cartels.
In engagement, we focus on comments instead of likes or views because information on who
views the post is not available, and data on who likes the post is more difficult to collect
than comments. We already know which cartel members have to comment according to the
cartel rules. For comparison, we needed to collect information on natural engagement.
We definenatural engagementas comments from users who don’t belong to any of the
cartels in our data. 30 To obtain information on natural engagement, we focus on each cartel
member’s first post in any of the nine cartels. For each cartel member’s first post in cartels,
29While most of the cartels in our dataset require engagement with the last five posts, one topic cartel
(fashion & beauty) required engagement with last seven posts and a general cartel started out requiring
seven but changed to five. In our analysis, to make it comparable, we focus on the first five comments in all
cartels.
30In practice, the engagement that we call natural could come from followers, users seeing the influencer’s
post for the first time, or users in other cartels unobservable to us. If a substantial part of the natural
engagement comes from other cartels or viewers induced by the cartel engagement, then our measure of
natural engagement match quality is a lower bound, which would make our results even stronger. To avoid
potential misclassification, we exclude all cartel commenters from natural engagement, including the ones
who, according to the cartel rules, were not required to comment. Our results remain qualitatively the same
when we include cartel commenters who were not required to comment in natural engagement.
17

we collected information on who commented on the post (Apify Technologies s.r.o., 2024).
Then, we used a random number generator and picked a random non-cartel user who had
commented on the post. The randomly chosen commenting Instagram users who don’t
belong to any of our cartels form our control group (natural engagement). Since these are
from the earliest post in the cartel, they are less likely to be indirectly affected by the cartel
activity.
We collected the text of all public Instagram posts and a photo for cartel members and
for the randomly picked non-cartel users (CrowdTangle Team, 2021, 2024; Hinnosaar and
Hinnosaar, 2024). We were unable to collect the content if the initial post had been deleted
or made private. We were also unable to collect information on the non-cartel commenters
if the initial post had no non-cartel commenters, or if the commenting user’s account was
private. We also didn’t collect information on non-cartel commenting users if they had fewer
than ten Instagram posts. Additionally, we excluded about 5% of the non-cartel commenting
users who had associated posts with cartel members. 31
4.2 Measuring Engagement Quality
Our goal is to compare engagement that originates from cartels to that of natural engage-
ment. As demonstrated above, the relevant quality measure in this context is the similarity
between the interests of the post author and the commenting user. 32 In our analysis, we
therefore consider engagement to be of high quality if it comes from Instagram users whose
own Instagram content has similar topics. Therefore, we measure the similarity of the posts
of commenting users to those of the post author. To analyze similarity, we use text and/or
photos in Instagram posts and three alternative methods.
4.2.1 Text Embeddings and Cosine Similarity of Users
First, we use a large language model named Language-agnostic BERT Sentence Embedding
(LaBSE) to construct embeddings of text in Instagram posts (Feng et al., 2022). An embed-
ding represents text as a numerical vector in a multidimensional vector space. The vector
representation of text is useful, allowing quantitative similarity comparison of texts via cosine
similarity. Cosine similarity is a standard measure of text similarity. This measure is defined
31The association can happen as Instagram allows posts to be associated with multiple users (this is
different from tagging a user), or it can happen when the user changes usernames.
32We focus on similarity based on users’ posts and do not use the text of comments, because comments in
this setting are not reliable indicators of engagement quality. Negative comments are rare, and while cartel
comments are on average slightly longer (Table A6.1 in the Online Appendix), this is by construction, as
cartel rules require members to leave longer meaningful comments, making them artificially substantial and
not reflective of genuine user interest.
18

as the cosine of the angle between two vectors, providing a similarity score between -1 and 1,
where close to 1 means that the texts (vectors) are highly similar. LaBSE builds upon one
of the first large language models, Bidirectional Encoder Representations from Transformers
(BERT), which was developed by Google researchers (Devlin et al., 2019). While BERT
was originally implemented for the English language, LaBSE extends it to more than 100
languages. The multilingual effectiveness is necessary for us because our sample is multilin-
gual. The LaBSE model transforms each post into a vector of length 768. It does so using
a large neural network with approximately 470 million parameters. This enables the model
to capture a large range of semantic features in multiple languages.
To create the input for the embedding, we restrict the sample in the following way.
First, we restrict the sample to users who have at least ten posts. In the main analysis,
we focus on 100 posts per user closest in the symmetric time window to the first post for
the cartel member and to the post they commented on for the non-cartel users. Results are
qualitatively similar when using a random sample or all posts from 2017 to 2020 (presented
in Online Appendix A7). In our main analysis, we create an embedding of each post using
hashtags in the post. We focus on hashtags because they typically informatively capture the
essence of Instagram posts. Online Appendix A7 presents results where the embeddings are
created using the whole text of the posts.
To create the input for the embedding, we pre-process the text: (i) transform to lower
case; (ii) replace all characters that are not letters, numbers, underscores, or hashtags with a
space (these are the only characters allowed in Instagram hashtags); (iii) add a space before
each hashtag; (iv) keep only words that start with a hashtag; (v) keep only the first 30
hashtags in each post because Instagram allows only up to 30 hashtags per post; (vi) drop
all hashtags that have only a single character because these tend to be uninformative; (vii)
drop all hashtags that don’t include any letters because these tend to be uninformative.
Before creating embeddings, we replace the hashtag and underscore symbols with a space.
Using the embeddings, we calculate the cosine similarity of users. To do that, first, we
create an embedding for each Instagram post separately. After obtaining embeddings of
each separate post, we generate a single measure for each user by taking the average of the
post embeddings for each user. Online Appendix A7 presents results where instead of post
embeddings, we first combine all users’ posts for each month, and obtain one embedding per
user and month pair, and then take the average over the months for each user. Using the
average embeddings, we calculate the cosine similarity of user pairs.
19

4.2.2 Photo and Text Embeddings and Cosine Similarity of Posts
We also construct embeddings of photos and text. As the above LaBSE model can encode
only text, we have to use a different model for processing photos alongside text. We use the
Contrastive Language Image Pre-training (CLIP) model, developed by OpenAI (Radford
et al., 2021). CLIP maps the contents of photos and text into a shared embedding space.
Because CLIP generates embeddings for photos and text that are directly comparable, it
allows us to calculate similarity by combining both forms of information. The CLIP model
transforms the text and photos into a vector of length 512. It does so using a neural network
with approximately 86 million parameters. The advantage of the CLIP model is that it
allows combining photos and text. On the other hand, the LaBSE model more precisely
captures text.
We use a photo and the text from a single Instagram post for each user. For cartel
members, we use the first post each cartel member posted to the cartels. For non-cartel
members, we select their closest post within a symmetric time window to the cartel member’s
post they commented on. To create the text input for the CLIP embedding, we first pre-
process the text, keeping the entire text, not just the hashtags: (i) transform it to lower
case; (ii) replace question marks, exclamation marks, and new line breaks with a full stop;
(iii) replace all characters that are not letters, numbers, full stops, underscores, hashtags,
at symbols, or apostrophes with a space; (iv) drop separate groups of characters that don’t
include any letters or numbers; (v) add a space before each hashtag; (vi) discard posts
that are shorter than three characters. Since the CLIP model has a binding limit of 77
for the number of tokens (text units such as words or subwords), we have to split the text.
Specifically, we split the text into sentences. In a small share of cases where the sentence
is longer than 77 tokens, we further split it at the 77-token mark. Then, we generate the
embedding for each sentence and take the average over all sentences in that post. We
also generate an embedding for each photo. Then we take the average of text and photo
embeddings of each post. Finally, using the average embeddings, we calculate the cosine
similarity for each author and commenter pair.
4.2.3 Determining Users’ Topics Using Latent Dirichlet Allocation
The models that generate embeddings allow us to measure similarity, but they are somewhat
black boxes. To shed some light on the comparison of users’ topics, we use a Latent Dirichlet
Allocation (LDA) model. The LDA algorithm estimates a probability distribution of topics
for each user based on the words used in their posts, and a probability distribution over the
words for each topic.
20

We train the LDA model using hashtags from the same sample of posts with the same
text pre-processing as in the LaBSE model used above. To improve learning from the
underlying content, we reduce the set of hashtags using standard thresholds following a
common approach in text analysis. Specifically, we exclude hashtags that fewer than 50
users use or more than 33% of the sample uses. This reduces the number of unique hashtags
from about 1.5 million to 19,032, giving us a typical medium-sized dictionary suitable for
LDA models. To improve the model’s performance and avoid giving more weight to users
with longer content, we homogenize the length of content over the users. To do that, for
each user, we cap the length of content at 1000 hashtags, which is about the 75th percentile
and slightly less than three times the median length. Finally, we exclude users with fewer
than 15 unique hashtags because there is not enough information to learn their topics. This
reduces the number of users by 17 percent. We fix the number of topics to six based on
interpretability and the coherence score (Figure A6.1). We assign each topic a label based
on the most representative hashtags in each topic, that is, the hashtags with the highest
probability (Table A6.2). The labels are fitness, beauty, fashion, food, entrepreneur, and
travel.
4.3 Sample
Our analysis is within subject. That is, for the same author, we compare his similarity
to cartel commenters versus his similarity to non-cartel commenters. For this comparison,
we need to be able to evaluate both similarities for each author. As described above, for
some authors, we were not able to collect information on their non-cartel commenters. Fur-
thermore, not all users had enough posts with text to calculate the outcome measures (the
embeddings, cosine similarity, LDA topics). The main sample includes only the authors for
whom: (A) we were able to find commenters both from cartels and not from cartels; and
(B) we had sufficient data to calculate the similarity measures for both types of commenters.
Table A6.3 in the Online Appendix describes how each restriction reduces the sample and
Online Appendix A5 provides further details.
The main regression analysis focuses on 8507 cartel members as authors of content.
For those authors, we were able to calculate both the LaBSE and CLIP embeddings, as
well as the same embeddings for at least one cartel and non-cartel commenter. The topic
analysis focuses on an analogous sample of 6654 authors with LDA topic measures for both
cartel and non-cartel commenters. 33 The authors excluded from the main samples due to
data limitations are similar to included authors in terms of their LDA topics (Figures A6.2
33The sample is smaller because the LDA topic estimation has stricter data requirements as it uses only
hashtags that are sufficiently common in the sample.
21

and A6.3), but, as expected, have fewer posts (Table A6.4).
4.4 Summary Statistics
Summary statistics of the main sample are presented in the Online Appendix. Table A6.5
compares members of general cartels to members of topic cartels, and Table A6.6 compares
cartel members to users not in the cartel. Note that the non-cartel users in the sample are not
representative of Instagram users, instead these are active users with enough public content.
That is, first, since we are analyzing engagement, we have to focus on active Instagram
users who comment on others’ content. Second, when calculating users’ interests based on
their content, we have to focus on Instagram users with enough public content. This avoids
potential measurement issues, such as having more detailed information on cartel members
than on users not in cartels. Table A6.6 shows that indeed, users not in cartels are rather
similar to cartel members. One might worry that perhaps those users belong to other cartels
not in our sample. In that case, our estimate of the natural engagement match quality is a
lower bound, which would make our results even stronger.
Table A6.7 provides suggestive evidence that cartels are effective in generating engage-
ment. It compares cartel members before and after joining the cartels. It shows that influ-
encers’ posts after joining the cartels have more likes and comments, have higher engagement
performance, and after joining the cartels, influencers are more likely to have disclosed spon-
sored posts.
The distribution of topics in the cartels is as expected (Figure 1). In the fashion & beauty
cartel, authors are posting more about fashion and beauty; in the fitness & health cartel,
about fitness; in the travel & food cartel, about travel and food. In the general cartels, the
topic distribution is rather uniform, with slightly more concentration on the topics of fashion
and travel.
5 Empirical Results
5.1 Empirical Strategy
Our empirical question is whether engagement from cartels is of lower quality than natural
engagement. To answer the question, we estimate a panel data fixed effects regression where
the outcome variable is the cosine similarity between an author and their commenter. An
observation is an author and their commenter pair. For each author, we focus on the first
post in the cartel. Thus, we have only one post for each author. For each post, we have
three types of commenters. Type one are the cartel members required to comment under
22

0 .2 .4 .6
Topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
(a) General cartels
0 .2 .4 .6
Topic share
FitnessBeautyFashion Food
Entrepreneur
Travel (b) Fashion & beauty cartel
0 .2 .4 .6
Topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
(c) Fitness & health cartel
0 .2 .4 .6
Topic share
FitnessBeautyFashion Food
Entrepreneur
Travel (d) Travel & food cartel
Figure 1: Authors’ LDA topic distributions
Notes: The bars correspond to the average topic shares across authors and capped spikes describe the 95%
confidence intervals.
cartel rules. 34 Here we separate general and topic cartel commenters. Type two is what we
call natural engagement: the non-cartel user who actually commented on the post. This
serves as a benchmark to test whether cartel commenters have lower similarity (to authors)
than non-cartel commenters. Type three are what we call the counterfactual random users:
these are randomly chosen non-cartel users. 35 This third group gives us another benchmark.
It allows us to measure whether cartel commenters have higher similarity (to authors) than
random users. Our sample is a balanced panel, in the sense that we have all three types of
34In the main analysis, we focus on cartel members required to comment instead of those actually com-
menting. We do this because we don’t observe all comments. The robustness analysis shows that the results
are similar when looking at who actually commented (Online Appendix A7).
35The counterfactual random users are sampled from all the users in our dataset that are not members of
any of the cartels. For each post, we first exclude the non-cartel commenter used to estimate the natural
engagement, and then draw five random users from the remaining set.
23

users for each author: cartel commenters, non-cartel commenters, and random users. 36
For the first post in cartels of authori, the similarity to their commenterjis:
Similarity ij =β GenGeneralCartelCommenter ij +β T opT opicCartelCommenterij
+β RanRandomU serij +InstagramAuthorF Ei +ε ij,(12)
whereSimilarity ij refers to the cosine similarity between authoriand commenterj;General
CartelCommenter ij is an indicator for a general cartel memberjwho is required to com-
ment;T opicCartelCommenterij is an indicator for a topic cartel memberjwho is required
to comment;RandomU serij is an indicator for a counterfactual random Instagram user not
in the cartel;InstagramAuthorF E i is the fixed effect for each author. Since we only have
one post per author, this is equivalent to the post fixed effect. The base category is natural
engagement, that is, a commenter who is not in the cartel.
In the main analysis, we use two alternative similarity measures as outcomes: cosine
similarity of users from LaBSE text embeddings and cosine similarity of their posts from
CLIP photo and text embeddings. 37 We look at three mutually exclusive samples, each
defined by the type of cartel containing the author’s first cartel post: (1) authors whose first
post is only in general cartels; (2) those whose first post is only in topic cartels; and (3)
those whose first post is in both. 38
To preview our main results, let us look at raw distributions of outcome variables (Fig-
ure 2). Non-cartel commenters have the highest similarity with the author, and random users
have the lowest. Commenters from general cartels have almost as low similarity as random
users (Figure 2a), while commenters from topic cartels have higher similarity (Figure 2b).
5.2 Quality of Engagement Measured by Cosine Similarity
We find that in general cartels (columns 1 and 4 in Table 1), authors’ similarity to cartel
commenters is significantly lower than their similarity to non-cartel commenters, who form
the base category. 39 Furthermore, similarity to general cartel members is almost as low as
36For each post, we have one non-cartel commenter, five random users, and one to five cartel commenters.
As described in Section 4.3, for some posts, there are fewer than five cartel commenters in the sample because
some cartel commenters didn’t have enough publicly available content.
37The details of the outcome variables are described in Section 4.2.
38With some abuse of terminology, we say that a post is only in general (or topic) cartel even if it was
posted in both but we have information on the commenters from only one of these. This affects only a small
number of posts.
39We define non-cartel commenters as those who don’t belong to any of the cartels in our sample, but they
might belong to cartels outside the sample. If some non-cartel commenters are members of cartels outside
our sample, then we underestimate the difference between authors’ similarity to cartel versus non-cartel
commenters.
24

0 .5 1 1.5 2 2.5
Density
0 .2 .4 .6 .8 1
Similarity of users, text embeddings
Non-cartel commenters
General cartel commenters
Random users
(a) General cartels, users’ similarity
0 .5 1 1.5 2 2.5
Density
0 .2 .4 .6 .8 1
Similarity of users, text embeddings
Non-cartel commenters
Topic cartel commenters
Random users (b) Topic cartels, users’ similarity
Figure 2: Probability density of authors’ similarity to commenters and random users
Notes: The figures present kernel density estimates using the Epanechnikov kernel function of authors’ cosine
similarity to non-cartel commenters (grey line with solid circle markers), to random users (red dotted line),
to general cartel commenters (blue dashed line on Figure 2a), and to topic cartel commenters (green dashed
and dotted line on Figure 2b). The cosine similarity is calculated as the similarity of users using the text
embeddings from the LaBSE model. Figure A6.4 presents the probability density estimates for the similarity
of posts using the photo and text embeddings from the CLIP model.
to random users. In contrast, in topic cartels (columns 2 and 5), authors’ similarity to cartel
commenters is only slightly lower than to non-cartel commenters. Similar results hold for
posts that are in both general and topic cartels (columns 3 and 6). The regression results are
robust to alternative ways to construct outcome variables and alternative samples, described
in detail in Online Appendix A7.
To interpret these estimates, we use natural engagement and random match quality as
benchmarks. When we rescale cartel cosine similarity to the natural-random difference,
an advertiser paying for general cartel engagement, while expecting natural engagement,
captures only 3–18% of the value. In contrast, with topic cartels, the advertiser still overpays
but gets 60–85% of the value.
Overall, our goal is to measure whether the additional attention that the cartel engage-
ment brings is from users who are likely to be interested in the content. Above, we proxied
the interests of the cartel-induced attention by the interests of the engaging cartel influencer.
This is a good proxy because cartel members’ natural commenters are likely to be interested
in the same topics as cartel members, irrespective of whether it is a topic or general cartel
(as shown in Section 5.3). However, in Online Appendix A7 (Tables A7.7 to A7.9), we use an
alternative approach based on topic match between the author and the commenting cartel
members’ commenters. The results remain qualitatively similar, but adding this additional
layer of distance increases noise, and therefore, similarity measures are smaller.
25

Table 1: Panel data fixed effects estimates of authors’ similarity to cartel commenters and
random users versus non-cartel commenters
(1) (2) (3) (4) (5) (6)
Dependent variable: Cosine similarity
Posts in general or topic cartels
General Topic Both General Topic Both
Similarity of users Similarity of posts
Text embeddings Photo+text embeddings
General cartel commenter -0.058*** -0.060*** -0.033*** -0.034***
(0.003) (0.008) (0.001) (0.003)
Topic cartel commenter -0.023*** -0.009 -0.016*** -0.012***
(0.003) (0.008) (0.001) (0.003)
Random user -0.071*** -0.076*** -0.062*** -0.040*** -0.040*** -0.037***
(0.003) (0.003) (0.008) (0.001) (0.001) (0.003)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.574 0.585 0.577 0.657 0.657 0.659
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4756 3263 488 4756 3263 488
Observations 44900 30569 6665 44900 30569 6665
Notes: Each column presents estimates from a separate panel data fixed effects regression. Unit of observation
is an author and another user pair. Outcome variable is the cosine similarity of the author to his commenter
or to a random user. In columns 1–3, the cosine similarity of users is calculated using the text embeddings
from the LaBSE model; in columns 4–6, the cosine similarity of the corresponding users’ posts is calculated
using the photo and text embeddings from the CLIP model. Each regression includes author fixed effects
(equivalent to the post fixed effects because only one post per author). In all the regressions, the base
category is the author’s similarity to a non-cartel commenter; andBase (non-cartel) meanpresents their
average cosine similarity.General cartel commenteris an indicator variable whether the commenter to whom
the author’s cosine similarity is calculated, is in the general cartel, andTopic cartel commenterwhether he
is in the topic cartel.Random userindicates that the author’s similarity is calculated to a counterfactual
random non-cartel user. The sample consists of authors whose first cartel post is either: only in general
cartels (columns 1 and 4); only in topic cartels (columns 2 and 5; or in both general and topic cartels
(columns 3 and 6). Standard errors in parentheses are clustered at the author level.
5.3 Quality of Engagement Measured by LDA Topic Match
To further study engagement quality, we compare the LDA topic distributions of cartel
versus non-cartel commenters, separately for general and topic cartels. For each author,
we define the main topic as the one with the largest LDA probability. Then, within each
group of authors sharing the same main topic, we compare the same topic share of the post’s
cartel versus non-cartel commenters. First, Figure 3 illustrates that general and topic cartels
are similar in terms of how often non-cartel commenters post on authors’ main topic (grey
bars). Second, Figure 3a shows that topic match from general cartels is worse than natural
(non-cartel): non-cartel commenters post on the author’s main topic about 42% of the time,
while cartel commenters do so only 22% of the time. This comparison is different for topic
cartels. Figure 3b focuses on the topics most prevalent in each topic cartel. It shows that
26

the topic match from topic cartels is not worse than natural (non-cartel).
0 .2 .4 .6
Topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Non-cartel commenters
General cartel commenters
(a) General cartel versus non-cartel commenters
0 .2 .4 .6
Topic share
Fashion Fitness Travel
Non-cartel commenters
Topic cartel commenters (b) Topic cartel versus non-cartel commenters
Figure 3: LDA topic shares of commenters from cartels versus non-cartels (natural)
Notes: The bars correspond to the average topic shares across commenters and capped spikes describe
the 95% confidence intervals. The grey bars capture the non-cartel commenters and blue bars the cartel
commenters. The sample is restricted to general cartel commenters on Figure 3a and topic cartel commenters
on Figure 3b. Each set of bars uses a sample of commenters that is further restricted by the main topic
of the author of the post they comment on, where the main topic is defined as the topic with the highest
LDA probability. For example, on Figure 3a, for the first grey and blue bar, the sample is restricted to
commenters on the posts in general cartels of the authors whose main topic is fitness.
6 Discussion
Collusion can take many forms, especially in new and evolving industries. In this paper, we
have documented and studied influencer cartels, a form of collusion in the rapidly growing
influencer marketing industry, which has stayed under regulators’ radar. Our empirical re-
sults indicate that engagement from general cartels is significantly lower in quality compared
to natural engagement, while engagement from topic cartels is closer to natural engagement.
Our theoretical model sheds light on the trade-offs involved and explores the associated wel-
fare implications. The key distortion is the free-rider problem, which cartels could help mit-
igate through enforced commitment. However, cartels also introduce new distortions, such
as over-engagement. These issues become particularly severe when the advertising market
heavily rewards the quantity of engagement, encouraging the creation of fake engagement.
Our empirical and theoretical results have three policy and managerial implications.
First, as general cartels are likely to be welfare-reducing, shutting these cartels down would
be socially beneficial. Second, regulatory rules that prohibit buying and selling fake social
media indicators should also prohibit obtaining these fake indicators via in-kind transfers,
27

i.e., paying for engagement with engagement. Third, the current practice of advertisers
to reward past engagement encourages harmful collusion. A better approach would be to
compensate influencers based on the actual value they add. Alternatively, platforms could
improve the outcomes by reporting match-quality-weighted engagement.
While our focus in this paper is to study specifically the distortions that influencer car-
tels create, the market structure and available data are rich enough to study other related
questions. Future research could analyze whether joining a cartel really brings the desired
growth in real followers and better advertising deals. While the cartel organizers claim this
is the case and correlational evidence (provided in this paper and by Weerasinghe et al.
(2020)) supports it, the causal impact is difficult to measure because influencers might join
a cartel at the same time they engage in other activities to induce growth.
Other potential extensions require additional data collection. To compare general and
topic cartels that are similar in other dimensions, we focused only on Instagram influencer
cartels that were organized by the same cartel organizer, had similar engagement rules, and
were all relatively large. Future research could study heterogeneity in other dimensions:
platforms, engagement requirements, and cartel sizes.
References
Adukia, A., A. Eble, E. Harrison, H. B. Runesha, and T. Szasz(2023): “What We
Teach About Race and Gender: Representation in Images and Text of Children’s Books,”
Quarterly Journal of Economics, 138, 2225–2285.
ANA(2020): “The State of Influence: Challenges and Opportunities in Influencer Market-
ing,” Tech. rep., Association of National Advertisers.
Anderson, S. P. and S. Coate(2005): “Market Provision of Broadcasting: A Welfare
Analysis,”Review of Economic Studies, 72, 947–972.
Anderson, S. P. and A. de Palma(2012): “Competition for Attention in the Informa-
tion (Overload) Age,”RAND Journal of Economics, 43, 1–25.
Anderson, S. P. and M. Peitz(2023): “Ad Clutter, Time Use, and Media Diversity,”
American Economic Journal: Microeconomics, 15, 227–270.
Apify Technologies s.r.o.(2024): “Instagram Comments and Public-Profile Informa-
tion for Cartel and Non-Cartel Users,” [data set, snapshot of January 2024]. Original
data produced by Meta Platforms, Inc., Menlo Park, CA, and made publicly avail-
able on Instagram; extracted by the authors using the Instagram Comment Scraper
28

actor. Prague, Czech Republic: Apify Technologies s.r.o. [extraction provider].https:
//apify.com/apify/instagram-comment-scraper.
Aridor, G., R. Jim ´enez-Dur´an, R. Levy, and L. Song(2024): “The Economics of
Social Media,”Journal of Economic Literature, 62, 1422–1474.
Ash, E., R. Durante, M. Grebenshchikova, and C. Schwarz(2021): “Visual Rep-
resentation and Stereotypes in News Media,” SSRN 3934858.
Ash, E. and S. Hansen(2023): “Text Algorithms in Economics,”Annual Review of
Economics, 15, 659–688.
Asker, J.(2010): “A Study of the Internal Organization of a Bidding Cartel,”American
Economic Review, 100, 724–762.
Asker, J., A. Collard-Wexler, C. D. Canniere, J. D. Loecker, and C. R. Knit-
tel(2024): “Two Wrongs Can Sometimes Make a Right: The Environmental Benefits of
Market Power in Oil,” NBER 28666.
Blei, D. M., A. Y. Ng, and M. I. Jordan(2003): “Latent Dirichlet Allocation,”Journal
of Machine Learning Research, 3, 993–1022.
Buchanan, J. M.(1969): “External Diseconomies, Corrective Taxes, and Market Struc-
ture,”American Economic Review, 59, 174–177.
Caprini, G.(2023): “Visual bias,”Manuscript.
Chen, Y., R. F arzan, R. Kraut, I. YeckehZaare, and A. F. Zhang(2024): “Mo-
tivating Experts to Contribute to Digital Public Goods: A Personalized Field Experiment
on Wikipedia,”Management Science, 70, 3264–3280.
Cotter, K.(2019): “Playing the Visibility Game: How Digital Influencers and Algorithms
Negotiate Influence on Instagram,”New Media & Society, 21, 895–913.
CreatorIQ(2024): “2024 Influencer Marketing Trends Report,” Tech. rep., CreatorIQ.
CrowdTangle Team(2021): “Instagram Post History of Cartel Users via Crowdtangle,”
[data set, snapshot of August 19–September 16, 2021]. Menlo Park, CA: Meta Platforms,
Inc. [producer and distributor].https://web.archive.org/web/2024*/https://www.
crowdtangle.com/. CrowdTangle was retired by Meta on August 14, 2024 and replaced
by the Meta Content Library (https://transparency.meta.com/researchtools/meta-
29

content-library); access at the time of collection was provided under Meta’s CrowdTan-
gle research-access program.
——— (2024): “Instagram Post History of Non-Cartel Commenters via Crowdtan-
gle,” [data set, snapshot of January 2024]. Menlo Park, CA: Meta Platforms,
Inc. [producer and distributor].https://web.archive.org/web/2024*/https://www.
crowdtangle.com/. CrowdTangle was retired by Meta on August 14, 2024 and replaced
by the Meta Content Library (https://transparency.meta.com/researchtools/meta-
content-library); access at the time of collection was provided under Meta’s CrowdTan-
gle research-access program.
Deltas, G., A. Salvo, and H. V asconcelos(2012): “Consumer-Surplus-Enhancing
Collusion and Trade,”RAND Journal of Economics, 43, 315–328.
Devlin, J., M.-W. Chang, K. Lee, and K. Toutanova(2019): “BERT: Pre-training
of Deep Bidirectional Transformers for Language Understanding,” ArXiv 1810.04805.
Donaldson, D. and A. Storeygard(2016): “The View from Above: Applications of
Satellite Data in Economics,”Journal of Economic Perspectives, 30, 171–198.
Dyck, A., A. Morse, and L. Zingales(2010): “Who Blows the Whistle on Corporate
Fraud?”Journal of Finance, 65, 2213–2253.
Ershov, D., Y. He, and S. Seiler(2025): “How Much Influencer Marketing is Undis-
closed? Evidence from Twitter,”Marketing Science, 44, 505–515.
Ershov, D. and M. Mitchell(2025): “The Effects of Influencer Advertising Disclosure
Regulations: Evidence From Instagram,”RAND Journal of Economics, 56, 74–90.
F ainmesser, I. P. and A. Galeotti(2021): “The Market for Online Influence,”Amer-
ican Economic Journal: Microeconomics, 13, 332–72.
Feng, F., Y. Yang, D. Cer, N. Arivazhagan, and W. W ang(2022): “Language-
agnostic BERT Sentence Embedding,” ArXiv 2007.01852.
Fershtman, C. and A. Pakes(2000): “A Dynamic Oligopoly with Collusion and Price
Wars,”RAND Journal of Economics, 31, 207–236.
Filippas, A., J. J. Horton, E. Lipnowski, and P. Parasurama(2025): “The Pro-
duction and Consumption of Social Media,”Management Science, Forthcoming.
Franck, G.(1999): “Scientific Communication–A Vanity Fair?”Science, 286, 53–55.
30

Genesove, D. and W. P. Mullin(2001): “Rules, Communication, and Collusion: Nar-
rative Evidence from the Sugar Institute Case,”American Economic Review, 91, 379–398.
Gentzkow, M., B. Kelly, and M. Taddy(2019): “Text as Data,”Journal of Economic
Literature, 57, 535–574.
Glazer, J., H. Herrera, and M. Perry(2021): “Fake Reviews,”Economic Journal,
131, 1772–1787.
Google LLC(2024): “Google Trends Search-Volume Series for Four Terms,” [data set,
snapshot of November 2024]. Mountain View, CA: Google LLC [producer and distributor].
https://trends.google.com/.
Hansen, S., M. McMahon, and A. Prat(2018): “Transparency and Deliberation
Within the FOMC: A Computational Linguistics Approach,”Quarterly Journal of Eco-
nomics, 133, 801–870.
He, S., B. Hollenbeck, and D. Proserpio(2022): “The Market for Fake Reviews,”
Marketing Science, 41, 896–921.
Hinnosaar, M. and T. Hinnosaar(2020): “Telegram Cartel Interaction History, Nine
Channels,” [restricted-access data set, snapshot of July 2020]. Nottingham, UK: University
of Nottingham [distributor].doi:10.17639/nott.23546. Compiled by the authors from
nine Instagram engagement cartels operating on Telegram (six general and three topic
cartels: fitness & health, fashion & beauty, travel & food). Original data produced and
distributed by Telegram FZ-LLC [producer], Dubai, United Arab Emirates, and collected
via the Telegram desktop client in July 2020. Restricted-access; available subject to a
data-use agreement.
——— (2024): “Instagram Post Photos From Public Accounts of Cartel and Non-Cartel
Users,” [data set, snapshot of February–March 2024]. Compiled by the authors. Original
data produced by Meta Platforms, Inc. [producer], Menlo Park, CA, and downloaded
directly from Instagram between February and March 2024.
Hinnosaar, M., T. Hinnosaar, M. Kummer, and O. Slivko(2022): “Externalities
in Knowledge Production: Evidence from a Randomized Field Experiment,”Experimental
Economics, 25, 706–733.
Hutto, C. and E. Gilbert(2014): “V ADER: A Parsimonious Rule-Based Model for Sen-
timent Analysis of Social Media Text,”Proceedings of the International AAAI Conference
on Web and Social Media, 8, 216–225.
31

Hyytinen, A., F. Steen, and O. Toivanen(2018): “Cartels Uncovered,”American
Economic Journal: Microeconomics, 10, 190–222.
——— (2019): “An Anatomy of Cartel Contracts,”Economic Journal, 129, 2155–2191.
Igami, M. and T. Sugaya(2022): “Measuring the Incentive to Collude: The Vitamin
Cartels, 1990–99,”Review of Economic Studies, 89, 1460–1494.
Kawai, K., J. Nakabayashi, and J. M. Ortner(2026): “The Value of Privacy in
Cartels: An Analysis of the Inner Workings of a Bidding Ring,”Review of Economic
Studies, 93, 600–628.
Lampe, R.(2012): “Strategic Citation,”Review of Economics and Statistics, 94, 320–333.
Lerner, J. and J. Tirole(2004): “Efficient Patent Pools,”American Economic Review,
94, 691–711.
Leuz, C., D. Nanda, and P. D. Wysocki(2003): “Earnings Management and Investor
Protection: An International Comparison,”Journal of Financial Economics, 69, 505–527.
Luca, M. and G. Zervas(2016): “Fake It Till You Make It: Reputation, Competition,
and Yelp Review Fraud,”Management Science, 62, 3412–3427.
Marshall, R. C. and L. M. Marx(2012):The Economics of Collusion: Cartels and
Bidding Rings, MIT Press.
Mayzlin, D., Y. Dover, and J. Chevalier(2014): “Promotional Reviews: An Em-
pirical Investigation of Online Review Manipulation,”American Economic Review, 104,
2421–2455.
Miguel, C., C. Clare, C. J. Ashworth, and D. Hoang(2022): “With a Little
Help From My Friends: Exploring Mutual Engagement and Authenticity Within Foodie
Influencers’ Communities of Practice,”Journal of Marketing Management, 38, 1561–1586.
Mitchell, M.(2021): “Free Ad(vice): Internet Influencers and Disclosure Regulation,”
RAND Journal of Economics, 52, 3–21.
Moser, P.(2013): “Patents and Innovation: Evidence from Economic History,”Journal
of Economic Perspectives, 27, 23–44.
O’Meara, V.(2019): “Weapons of the Chic: Instagram Influencer Engagement Pods as
Practices of Resistance to Instagram Platform Labor,”Social Media + Society, 5, 1–11.
32

Pei, A. and D. Mayzlin(2022): “Influencing Social Media Influencers Through Affilia-
tion,”Marketing Science, 41, 593–615.
Pesendorfer, M.(2000): “A Study of Collusion in First-Price Auctions,”Review of
Economic Studies, 67, 381–411.
Porter, R. H.(1983): “A Study of Cartel Stability: The Joint Executive Committee,
1880-1886,”Bell Journal of Economics, 14, 301–314.
Porter, R. H. and J. D. Zona(1993): “Detection of Bid Rigging in Procurement
Auctions,”Journal of Political Economy, 101, 518–538.
Radford, A., J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal,
G. Sastry, A. Askell, P. Mishkin, J. Clark, G. Krueger, and I. Sutskever
(2021): “Learning Transferable Visual Models From Natural Language Supervision,”
ArXiv 2103.00020.
Rhodes, A. and C. M. Wilson(2018): “False advertising,”RAND Journal of Economics,
49, 348–369.
R¨oller, L.-H. and F. Steen(2006): “On the Workings of a Cartel: Evidence from the
Norwegian Cement Industry,”American Economic Review, 96, 321–338.
Salop, S. C.(1979): “Monopolistic Competition with Outside Goods,”Bell Journal of
Economics, 10, 141–156.
Schinkel, M. P. and Y. Spiegel(2017): “Can Collusion Promote Sustainable Consump-
tion and Production?”International Journal of Industrial Organization, 53, 371–398.
Schinkel, M. P., Y. Spiegel, and L. Treuren(2022): “Production Agreements, Sus-
tainability Investments, and Consumer Welfare,”Economics Letters, 216, 110564.
Smirnov, A. and E. Starkov(2022): “Bad News Turned Good: Reversal under Censor-
ship,”American Economic Journal: Microeconomics, 14, 506–560.
Song, Y.(2025): “Social Learning Among Opinion Leaders,”Games and Economic Behav-
ior, 153, 451–473.
Szydlowski, M.(2023): “Deprioritizing Content,” SSRN 4398140.
33

Telegram FZ-LLC(2020): “Telegram Desktop Client,” [computer software, version cur-
rent as of July 2020]. Dubai, United Arab Emirates: Telegram FZ-LLC [producer and dis-
tributor].https://telegram.org/. Telegram desktop client used to download the cartel-
channel communication history.
V an Noorden, R.(2013): “Brazilian Citation Scheme Outed,”Nature, 500, 510–511.
Weerasinghe, J., B. Flanigan, A. Stein, D. McCoy, and R. Greenstadt(2020):
“The Pod People: Understanding Manipulation of Social Media Popularity via Reciprocity
Abuse,” inProceedings of The Web Conference 2020, WWW ’20, 1874–1884.
Wilhite, A. W. and E. A. Fong(2012): “Coercive Citation in Academic Publishing,”
Science, 335, 542–543.
Zinman, J. and E. Zitzewitz(2016): “Wintertime for Deceptive Advertising?”American
Economic Journal: Applied Economics, 8, 177–192.
34

Influencer Cartels
Online Appendix
Marit Hinnosaar∗ Toomas Hinnosaar†
May 27, 2026
∗University of Nottingham and CEPR,marit.hinnosaar@gmail.com
†University of Nottingham and CEPR,toomas@hinnosaar.net
35

Contents of Online Appendix
A1 Screenshots of Instagram and Engagement Pods . . . . . . . . . . . . . . . . . . . A3
A2 Google Trends . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A6
A3 Proofs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A7
A4 Extension with Heterogeneous Reach . . . . . . . . . . . . . . . . . . . . . . . . . A11
A5 Data Collection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A17
A6 Additional Empirical Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A20
A7 Robustness Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A27
List of Online Appendix Tables
A6.1 Summary statistics of cartel versus non-cartel comments . . . . . . . . . . . . A20
A6.2 Most representative hashtags for each LDA topic . . . . . . . . . . . . . . . . . A20
A6.3 Sample construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A21
A6.4 Summary statistics of authors in cartel included/excluded from the sample . . A21
A6.5 Summary statistics of authors in different types of cartel . . . . . . . . . . . . A22
A6.6 Summary statistics of users in cartels versus not in cartels . . . . . . . . . . . A22
A6.7 Summary statistics of cartel members before and after joining the cartel . . . . A23
A7.1 Alternative outcome variables: random posts; all posts in 2017–2020 . . . . . . A28
A7.2 Alternative outcome variable: whole text instead of hashtags . . . . . . . . . . A29
A7.3 Alternative outcome variables: photo embeddings, text embeddings . . . . . . A30
A7.4 Alternative outcome variables: similarity above 75th, 90th percentile . . . . . A31
A7.5 Alternative sample: commenters who actually commented . . . . . . . . . . . A32
A7.6 Heterogeneity by topic cartel . . . . . . . . . . . . . . . . . . . . . . . . . . . . A33
A7.7 Cartel commenters’ non-cartel commenters . . . . . . . . . . . . . . . . . . . . A34
A7.8 Cartel commenters’ non-cartel commenters: posts in both cartels . . . . . . . . A35
A7.9 Cartel commenters’ non-cartel commenters: heterogeneity . . . . . . . . . . . . A35
List of Online Appendix Figures
A1.1 Screenshots of Wolf Global Instagram Engagement Pods . . . . . . . . . . . . A3
A1.2 Wolf Onyx Comments on Telegram app mapped to Instagram users . . . . . . A4
A1.3 Instagram comments coming from Wolf Onyx Comments . . . . . . . . . . . . A4
A1.4 Suggested Instagram post and a user who liked it . . . . . . . . . . . . . . . . A5
A2.1 Google Trends . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . A6
A4.1 Welfare as a function of engagement requirement . . . . . . . . . . . . . . . . A14
A1

A6.1 LDA model coherence scores by the number of topics . . . . . . . . . . . . . . A24
A6.2 Authors’ topics: regression sample versus excluded . . . . . . . . . . . . . . . . A24
A6.3 Authors’ topics: LDA sample versus excluded . . . . . . . . . . . . . . . . . . A25
A6.4 Probability density of authors’ similarity to commenters and random users . . A26
A2

A1 Online Appendix: Screenshots of Instagram and
Engagement Pods
(a) Main page
(b) Description of how influencers can amplify their earnings
Figure A1.1: Screenshots of Wolf Global Instagram Engagement Pods
Notes: Screenshots ofhttps://www.wolfglobal.org/, taken on March 4, 2024.
A3

Figure A1.2: Wolf Onyx Comments on Telegram app mapped to Instagram users
Notes: Screenshot of Telegram Wolf Onyx Comments, taken on March 4, 2024.
Figure A1.3: Instagram comments coming from Wolf Onyx Comments
Notes: Screenshot of Instagram, taken on March 4, 2024. To preserve anonymity, the Instagram account
names are blurred and the photo is replaced with a analogous photo generated by AI image generator.
A4

Figure A1.4: Suggested Instagram post and a user who liked it
Notes: Screenshot of Instagram, taken on May 9, 2024. Upper red oval shows that the post was suggested
to the viewer (who was not follower for this Instagram account) and lower red oval shows a specific user
that the viewer does follow liked the post, indicating that one reason the post was suggested to the viewer
was because of this engagement. To preserve anonymity, the Instagram account names are blurred and the
photo is replaced with a analogous photo generated by AI image generator.
A5

A2 Online Appendix: Google Trends
One way to estimate the prevalence of these cartels is through search activity. Figure A2.1
presents Google Trends data for four relevant search terms: “Instagram algorithm”, “Insta-
gram pod”, “Instagram bot”, and “patent pool”. 3 The graph for “Instagram algorithm”
provides a useful baseline, as influencers are likely to be interested in understanding the
platform’s mechanics. The upward trend in searches aligns with the platform’s growth, with
notable spikes following changes to the algorithm. Searches for “Instagram pods” (i.e., car-
tels) follow a similar pattern but with lower magnitude, averaging 53% of algorithm-related
searches. This suggests a significant portion of Instagram users are aware of and interested
in cartels. Searches for “Instagram bot”, representing the most basic form of engagement
fraud (paid computer-generated clicks, likes, and comments), are more common, averaging
260% of algorithm-related searches. In contrast, “patent pools” serve as a control benchmark
and show relatively flat search activity, with lower volume compared to all Instagram-related
terms.
0
20
40
60
80
100
Google Trends
2010 2014 2018 2022
Years
Instagram pod
Instagram algorithm
Instagram bot
patent pool
Figure A2.1: Google Trends
Notes: The figure uses data from Google Trends. The lines measure worldwide Google search volume for
search terms ”Instagram pod”, ”Instagram algorithm”, ”Instagram bot”, and ”patent pool” in 2010-2024.
Influencer cartels are commonly called “Instagram pods”.
3The influencer cartels are commonly called “Instagram pods”, sometimes also “influencer pods” or
“engagement pods”.
A6

A3 Online Appendix: Proofs
A3.1 Proof of Proposition 1
Taking the difference inU I between engagement and no engagement yields net private gain
γcos(∆)−C(∆). This expression is nonnegative if and only ifγ≥tan(∆), which holds
if and only if ∆≤Λ N with Λ N = arctan(γ). Hence the equilibrium engagement rule is
eN (α′|α) =1[∆≤Λ N ]. Because the engagement decision is independent and determined
pointwise by the sign ofγcos(∆)−C(∆), the equilibrium is unique. Finally, sinceγ <1, we
have ΛN = arctan(γ)<arctan(1) =π/4. Consider cutoff rulese S(α′|α) =1[∆≤Λ]. Social
welfare is
W(Λ) = 1 π Z Λ 0  (R+ 1 +Rv) cos(∆)−(R+ 1)C(∆)  d∆.
The welfare-maximizing cutoff Λ S(v) satisfies the first-order condition
(R+ 1 +Rv) cos(Λ)−(R+ 1)C(Λ) = 0.
This condition is equivalent to
tan(Λ) = 1 + Rv R+ 1 ,
and therefore Λ S(v) = arctan  1 + Rv R+1  . This expression is strictly increasing inv, and
satisfies Λ S(0) = arctan(1) =π/4 and lim v→∞ ΛS(v) =π/2. As Λ S(v)≥π/4>Λ N , the
social optimum prescribes engagement for all matches that engage in equilibrium and for
additional matches with ∆∈(Λ N ,Λ S(v)]. These additional engagements occur at larger
topic distances and therefore have lower similarity.
A3.2 Proof of Proposition 2
The expected payoff from joining a cartel with engagement threshold Λ is
E[U C] = 1 π Z Λ 0  γcos(∆)−C(∆) + (1−γ) cos(∆) + Rv Λ Z Λ 0 cos(∆′)d∆ ′ | {z }
=p

d∆
= 1 π Z Λ 0  (1 +Rv) cos(∆)−C(∆)  d∆.
A7

Define Λ max ∈[0, π] as the maximal feasible threshold, that is, the largest Λ such that
E[U C]≥0. We first show that Λ max ≥π/2. For all Λ≤π/2,
E[U C] = 1 π Z Λ 0  (1 +Rv) cos(∆)−sin(∆)  d∆ = 1 π  (1 +Rv) sin(Λ)−(1−cos(Λ))  .
This expression is non-negative because 4
(1 +Rv) 2 sin Λ 2 cos Λ 2 ≥2 sin 2 Λ 2 ⇐ ⇒1 +Rv≥tan Λ 2 ,
which holds for all Λ≤π/2 because then Λ/2≤π/4 and tan(Λ/2)≤1≤1 +Rv. Next, we
show that Λ max < π. With Λ =πwe get
E[U C] = 1 π Z π 0  (1 +Rv) cos(∆)−C(∆)  d∆ =− 1 π − 1 2 <0.
Hence there exists a maximal feasible threshold Λ max ∈(π/2, π) such that influencers are
willing to join the cartel if and only if Λ≤Λ max. We now characterize the optimal cartel
engagement. Differentiating (9) with respect to Λ yields
dE[U C]
dΛ = 1 π  (1 +Rv) cos(Λ)−C(Λ)  .
The optimal Λ therefore satisfies
(1 +Rv) cos(Λ)−C(Λ) = 0⇐ ⇒tan(Λ) = 1 +Rv,
and hence Λ C(v) = arctan(1 +Rv). This expression is strictly increasing inv, satisfies
ΛC(0) = arctan(1) =π/4, and converges toπ/2 asv→ ∞. Finally, for allv >0,
ΛC(v) = arctan(1 +Rv)>arctan

1 + Rv R+ 1  = ΛS(v),
becauseR/(R+ 1)<1.
4We are using the half-angle identities sin(Λ) = 2 sin( Λ 2 ) cos(Λ 2 ) and 1−cos(Λ) = 2 sin 2( Λ 2 ).
A8

A3.3 Proofs for Section 3.4
A3.3.1 Proof of Proposition 3
We focus on the limit asm→ ∞, so a single cartel takes the pricep(ε) as given. In
equilibrium all cartels choose the same engagement requirement, denoted Λ C. By definition,
p(ε) =Rv (1−ε) sin(Λ N ) +εsin(Λ C) (1−ε)Λ N +εΛ C .
Since sin(ΛC)≥0 and Λ C ≤π, we have
p(ε)≥Rv (1−ε) sin(Λ N ) (1−ε)Λ N +επ .
With ΛN = arctan(γ), we have sin(Λ N ) =γ/ p 1 +γ 2, hence
p(ε)≥Rv
(1−ε) γp
1 +γ 2
(1−ε) arctan(γ) +επ =:Rv ρ(ε, γ),
whereρ(ε, γ)>0 for allε, γ∈(0,1). A cartel with Λ C i =πis feasible if and only if its
members obtain a nonnegative expected payoff,
E[U C i ](π) = 1 π Z π 0  cos(∆)−C(∆) +p(ε)  d∆ =p(ε)− 1 π − 1 2 ≥0,
that is, ifp(ε)≥ 1 π + 1 2 . Sincep(ε)≥Rv ρ(ε, γ), there exists v >0 such that for allv≥ v
this feasibility condition holds. For carteli,
E[U C i ](ΛC i ) = 1 π Z ΛC i 0  cos(∆)−C(∆) +p(ε)  d∆.
Differentiating with respect to Λ C i gives
dE[U C i ]
dΛC i = cos(ΛC i )−C(Λ C i ) +p(ε) π .
Evaluating at ΛC i =πyields
dE[U C i ]
dΛC i

ΛC i =π
= cos(π)−C(π) +p(ε) π = p(ε)−2 π .
A9

Using the lower boundp(ε)≥Rv ρ(ε, γ), there existsbv≥ vsuch that for allv≥bv,
dE[U C i ]
dΛC i

ΛC i =π
≥ Rv ρ(ε, γ)−2 π >0.
Hence, forv≥bv, cartelistrictly prefers Λ C i =πto any smaller engagement requirement.
Since cartels are symmetric, in equilibrium all cartels choose Λ C i =π.
A3.3.2 Proof of Corollary 1
Assume cartels are general cartels, so Λ C =π. Then
p(ε) =Rv (1−ε) sin(Λ N ) (1−ε)Λ N +επ .
Differentiating gives
p′(ε) =− Rv πsin(ΛN )
(1−ε)Λ N +επ 2 <0.
A cartel member’s expected payoff satisfies
dE[U C i ]
dε =p ′(ε)<0,
becauseεaffectsE[U C i ] only throughp(ε). A non-cartel influencer engages with probability
ΛN /π, hence her expected payoff depends onεthrough advertising revenue with the same
factor, which implies
dE[U I]
dε = ΛN π p′(ε)<0.
This proves parts (ii) and (iii). General cartels implyE[cos(∆)|∆≤π] = 0, while attention
costs and engagement costs remain strictly positive. Moreover,p ′(ε)<0 reduces the payoffs
of both cartel members and non-members. Therefore, increasingεstrictly reduces social
welfare, proving part (i).
A10

A4 Online Appendix: Extension with Heterogeneous
Reach
Here we extend the analysis to the case of heterogeneous reach. Specifically, we assume that
every influencertis characterized by a two-dimensional type (α t, Rt), whereα t ∈[0,2π]
denotes the topic andR t the reach. We assume thatα t is uniformly distributed, while
Rt follows a power-law distribution with mean 2. 5 As in the main text, each influencer
is randomly matched with another influencert ′ (equivalently, this can be interpreted as a
dynamic model), where the distance isd(α t, αt′) = ∆. Each influencer can engage either
naturally or according to cartel rules. To keep the analysis tractable, we make two addi-
tional simplifying assumptions relative to the main text. First, instead of modeling followers
explicitly, we assume that influencers fully internalize the costs and benefits experienced
by their followers. Specifically, the payoff of influencertdepends only on the engagement
choices,a t =e(α t′ |α t) anda t′ =e(α t |α t′), and is given by
U I =a tRt[γcos(∆)−C(∆)] +a t′  (1−γ)R t′ cos(∆) +p t  ,(13)
where the price of engagement is given byp t =R t′vE[cos(∆)|a t′ = 1]. Because influencers
jointly internalize the surplus generated for both consumers and advertisers, social welfare
is simply the sum of all influencers’ payoffs:
W=E[U I].(14)
The second simplifying assumption is that we focus on two extremes with respect to the ad-
vertising market: eitherv= 0, i.e., there is no advertising, orvis very large, i.e., advertising
revenue dominates all other considerations. 6
A4.1 Only Natural Engagement
As in our main model, the positive externality of engagement creates a free-riding problem.
Therefore, in equilibrium there is less engagement than is socially optimal, i.e., the conclu-
sions from Proposition 1 still hold. The level of natural engagement is Λ N = arctan(γ)< π 4 ,
5That is, the probability density function isf(R) = 2R −3 forR≥1.
6To avoid dealing with infinities, we study limits of normalized payoffs, i.e., lim v→∞(U/v), whereU
denotes the relevant payoff or welfare function.
A11

whereas the socially optimal engagement level Λ S maximizes
W= 2 π Z Λ 0  (1 +v) cos(∆)−sin(∆)  d∆,(15)
where we have used the facts that the optimal Λ≤ π 2 and thatE[R t] =E[R t′] = 2. Without
an advertising market, the socially optimal engagement level satisfies cos(Λ) = sin(Λ), so
that Λ S(0) = arctan(1) = π 4 . On the other hand, if the advertising market is extremely
important, then, in the limit, the advertising surplus dominates all other components of
social welfare, and therefore
lim
v→∞
W
v = 2 π Z Λ 0 cos(∆)d∆,(16)
and the socially optimal engagement level converges to lim v→∞ ΛS(v) = arccos(0) = π 2 . The
following proposition formalizes these observations.
Proposition 4.There is a unique equilibrium. There is more engagement in the social
optimum than in equilibrium, although the additional engagement is of lower quality. In
particular:
1. The natural engagement level isΛ N = arctan(γ)< π 4 .
2. The socially optimal engagement level isΛ S = π 4 ifv= 0, andΛ S → π 2 asv→ ∞.
A4.2 Only Cartel Engagement
Suppose that the cartel requires an engagement level Λ. An influencertwho considers joining
the cartel knows his type (α t, Rt) but does not yet know the characteristics of the matched
influencert ′. The expected payoff from joining the cartel is
EU C(Rt) = 1 π Z Λ 0 h γRt cos(∆)−R tC(∆) + (1−γ)E[R t′ |a t′ = 1] cos(∆) +p t i d∆.(17)
A4.2.1 No Advertising
Let us again start with the case whenv= 0, so thatp t = 0. It is straightforward to see that
there exists a possibly infinite threshold R≥1, such that an influencer with reachR t joins
the cartel if and only ifR t ≤ R. Suppose first that Λ≤ π 2 , so thatC(∆) = sin(∆). Using a
A12

monotonic transformationλ= tan
 Λ
2

, the expression forEU C(Rt) simplifies to 7
EU C(Rt) = 2λ(1−γ) π(1 +λ 2)  E[Rt′|Rt′ ≤ R]− λ−γ 1−γ Rt  .(18)
Now, ifλ≤γ, then the expression is positive for allR t, and all influencers join the cartel.
On the other hand, ifλ > γ, then the marginal influencer type Rmust satisfy 8
EU C(R) = 2λ(1−γ) π(1 +λ 2)  2R 1 + R − λ−γ 1−γ R  = 0⇐ ⇒ R= 2−λ−γ λ−γ .(19)
This analysis assumed that Λ≤ π 2 and thereforeλ= tan  Λ 2  ≤tan  π 4  = 1. Specifically,
when Λ = π 2 , we haveλ= 1 and therefore R= 1, i.e., in this extreme case only the lowest-
reach influencers withR t = 1 join the cartel. It is easy to see that when Λ> π 2 , even the
lowest type would not want to join the cartel. Combining these observations, we get the
following proposition.
Proposition 5.Ifv= 0, then, depending on the cartel agreement, there can be three types
of equilibria in the cartel entry game:
1. Ifλ≤γ, all influencers join the cartel.
2. Ifγ < λ <1, all influencers withR t ≤ R= 2−γ−λ λ−γ join the cartel.
3. Ifλ≥1, no influencer joins the cartel.
The proposition implies that only cartels with engagement requirement Λ≤ π 2 are feasi-
ble. Compared to the case with homogeneous influencers, high engagement requirement Λ
introduces an additional distortion: influencers with high reach may choose not to join the
cartel. This is because, for sufficiently high engagement requirements Λ, influencers face a
trade-off when deciding whether to join: on the one hand, they are asked to engage more
than they would prefer in isolation (i.e.,γcos(∆)−C(∆)<0), but on the other hand
they receive additional engagement from other cartel members in return. The key insight
is that the first component (cost) is proportional to the influencer’s own reachR t, whereas
the second (benefit) is proportional to the average reach of a cartel member. Hence, influ-
encers with the highest reach are the first to stay out of the cartel. Next, let us consider
an optimal cartel. Using Proposition 5, we know that the optimal cartel must haveλ <1
(or equivalently, Λ< π 2 ). Therefore, depending on the level of the externality parameterγ,
7Note that 1+cos(Λ) sin(Λ) = 1/tan  Λ 2  = 1 λ , and sin(Λ) = sin(2 tan−1(λ)) = 2λ λ2+1 .
8Note thatE[R t′|Rt′ ≤ R] = 2R 1+R .
A13

λ
EU C(R), W
0 1 λS 1 2λN 1 2 3 8λN 3 8 1 10λN 1 10
λC 1
2
λC 3
8
λC 1
10
Figure A4.1: Welfare as a function of engagement requirement
Notes:λ S denotes the socially optimal engagement level,λ N γ , the natural engagement, andλ C γ the optimal
cartel engagement corresponding toγ. The solid lines with markers represent expected payoffs for cartel
members, and the dashed line is social welfare function if all influencers would join.
there are three cases to consider. First, suppose that the socially optimal engagement level
is such thatλ C < γ, i.e., all influencers would join such cartel. It is straightforward to see
that, in this case, the expected payoff of a cartel member,EU C(Rt), coincides with the social
welfare functionW. Hence, the optimal engagement coincides with the socially optimal one,
which is such that Λ C = Λ S = π 4 , or equivalentlyλ C =λ S = tan  π 8  = √ 2−1≈0.414.
For illustration, see Figure A4.1 (the green line, corresponding toγ= 1 2 ). This argument
fails whenγis small, i.e.,γ < λ S. In this case, the socially optimal cartel is not feasible,
because the highest-reach influencers would not join the cartel. We then need to augment
the objective of the cartel, i.e., the mean payoff for a cartel member by taking expectation
conditional onR t ≤ Rdefined in Proposition 5, and the expression becomes
E[EU C(Rt)|R t ≤ R] = 2λ(1−λ) π(λ2 + 1) 2−γ−λ 1−γ ,(20)
This expression has a unique maximizerλ ∗(γ) in (0,1). Ifλ ∗(γ)> γ, then the optimal
cartel engagement isλ C =λ ∗(γ). This is illustrated by the blue line in Figure A4.1 (the
caseγ= 1 10 ). The final case is when the externality parameterγis intermediate, i.e.,
λ∗(γ)< γ < λS. In this case, the optimal engagement lies at the boundary between the two
regions, i.e.,λ C =γ. This case is illustrated by the red line in Figure A4.1 (the caseγ= 3 8 ).
The following corollary summarizes the observations above.
A14

Corollary 2.Depending onγ, we have one of three cases: 9
1. Ifγ≥λ S, then the optimal cartel is the socially optimal cartel withλ C =λ S.
2. Ifγ inc ≤γ < λS, then the social optimum is not feasible as a cartel outcome. The
optimal cartel is the one with the largest engagement level such that all influencers join
the cartel, which isλ C =γ.
3. Ifγ < γ inc, then the social optimum is not feasible as a cartel outcome. The optimal
cartel,λ C =λ ∗(γ), involves some influencers staying out of the cartel.
This version of our model can also shed light on why influencer cartels often impose entry
requirements in practice. A typical requirement is to have at least some minimum number of
followers, ranging from 1,000 to 100,000 in our sample. We saw that the cost of joining the
cartel depends on the influencer’s own reach, while the benefit depends on the average reach
of a cartel member. By imposing a minimum reach requirement, the cartel increases the
average reach, making it more appealing to influencers with higher reach. The combination
of these effects raises the average reach and benefits all cartel members. Therefore, we would
expect the entry requirement to increase the average benefits for cartel members. On the
other hand, excluding influencers with low reach means that fewer can join the cartel, which
may reduce overall social welfare. The following proposition confirms this intuition.
Proposition 6.Suppose that, in addition to an engagement requirementΛ>0, the cartel
imposes an entry requirementR >1, so that only influencers withR t ≥R are eligible to
join. The expected payoff of a cartel member,E[U C(Rt)|R ≤R t], is proportional toR , and
social welfare is proportional toR −1.
The cartel may, therefore, choose to restrict eligibility, because such a restriction raises
cartel members’ welfare. However, there is a downside—the restriction reduces the number
of cartel members, and this effect can be large enough to reduce overall welfare. In our
model, the optimal minimum reach is infinitely large, but in practice, a very high reach
requirement would be impractical. 10
A4.2.2 Advertising Dominates Other Incentives
Let us now consider the other extreme, where advertising revenue dominates all other in-
centives. Specifically, in this case, the normalized value of joining a cartel with engagement
9The critical values areγ inc ≈0.344 andλ S = √ 2−1≈0.414.
10Nevertheless, in our sample there is a cartel that requires at least 100,000 followers, and this cartel has
a large number of members.
A15

requirement Λ becomes
lim
v→∞
EU C(Rt)
v = Λ π E[Rt′ cos(∆)|a t′ = 1] = sin(Λ) π E[Rt′ |a t′ = 1].(21)
This expression is non-negative for all Λ, so any cartel is feasible and all influencers join,
implyingE[R t′ |a t′ = 1] = 2. The expression is maximized when sin(Λ) = 1, hence
ΛC = π 2 , which also corresponds to the socially optimal cartel in this case. Compared
to the no-advertising case above, we do not have the secondary distortion of high-reach
influencers staying out of the cartel. The reason is that, since advertising revenue dominates
all other incentives, all influencers become primarily interested in the attention they receive
from the cartel, i.e., they care much more about the average reach than about their own
reach. Note that a minimum entry requirement would still increase the expected payoff of
a cartel member, asE[R t′ |R t′ ≥R ] = 2R , so it would be optimal to introduce a high
entry requirement. However, since the share of influencers satisfying this requirement is
P r(Rt′ ≥R ) = 1 R2 , social welfare would in fact decrease withR .
A4.3 Both Natural and Cartel Engagement
Again, we combine natural engagement and cartel engagement, assuming that mass 1−εof
influencers choose natural engagement, whereas massεbelong to an infinite number of small
cartels, which choose their engagement requirements independently. We now focus only on
the casev→ ∞. As implied by the discussion above, in this case there is no substantial
difference from the homogeneous-reach model, as payoffs depend only on the average reach
rather than the influencer’s own reach. Therefore, the results from Proposition 3 and Corol-
lary 1 apply here as well: general cartels with maximal engagement level ΛC i =πare not only
feasible but also optimal, maximizing cartel members’ payoffs. These cartels are harmful to
everyone, as they reduce welfare, and all influencers would be better off if there were fewer
such cartels.
A16

A5 Online Appendix: Data Collection
A5.1 Telegram Cartel History
We collected Telegram cartel interaction history for 9 cartels: 6 general cartels (1K, 5K,
10K, 30K, 50K, 100K) and 3 topic cartels (fashion & beauty, health & fitness, travel &
food). The 9 cartels were formed the earliest in August 2017 (10K and 50K) and the latest
in February 2018 (5K). We downloaded the data in July 2020. In June 2020 all cartels had
new posts. The Telegram cartel interaction history consists of three pieces of information:
Telegram username, Instagram post shortcode, and time. The interaction history tells us
which Telegram user, added when, and which Instagram post to the cartel. According to
the cartel rules, this information allows to determine which cartel member has to comment
and like which post. This is because one has to comment and like at least five posts by other
users directly preceding one’s own.
A5.2 Mapping Telegram Posts to Instagram Users
The Telegram cartels included 220,893 unique Instagram posts that we were able to map to
21,068 Instagram users. Specifically, the Telegram cartels included 316,462 unique Instagram
posts altogether. Some posts are posted multiple times and/or multiple cartels, the 316,462
unique Instagram posts were posted in total 527,498 times. The cartel interaction files
don’t include the Instagram username of the author of the Instagram post. We mapped
the Instagram posts included in cartels to Instagram users using the following interactive
procedure. For the first Instagram post in the cartel of each Telegram user, we searched
for the post on Instagram to learn the Instagram username of the post’s author. Then we
obtained from CrowdTangle the full list of all the Instagram posts of that Instagram username
and matched those to the posts in the cartel. We checked the remaining unmatched posts
in the cartel one by one until we either found a match for it on Instagram or determined
that the post had been deleted on Instagram or made private. In this way, we were able
to determine the Instagram usernames of 70% of the posts in the cartels, altogether 21,068
Instagram usernames. Of the 21,068 Instagram users, 22% of users had posted in both topic
and general cartels. Altogether, 11,158 users had posted in topic cartels and 14,566 users in
general. This includes 4,656 users who had posted in both. Hence, the total number of users
equals 11,158 + 14,566 - 4,656 = 21,068. From CrowdTangle, for all the 21,068 Instagram
users, we obtained the history of all their Instagram posts. This data included the time of
the post, and the text of the post including the hashtags. The data was downloaded from
August 19 to September 16, 2021.
A17

A5.3 Instagram Comments
For each Instagram user, for their first post in cartels (no matter which cartel), we collected
information on who commented on the post. Our goal was to learn who engaged with the
post and compare natural (non-cartel) engagement to that obtained via cartels. Therefore,
we did not focus on the comment but instead only on the username that posted the comment.
We restricted attention to the commenters on the post itself, and excluded commenters who
commented on a comment. We focused on each user’s first post in cartels to minimize the
possibility that involvement in cartels had affected engagement. However, when the first
post did not have enough information for the analysis, that is, when for the first post none
of the cartel members who were required to comment existed anymore, then we focused
on the second (if the second post existed) and so on. We did not require that the cartel
members actually commented, only that the users still existed. For 18 users no post existed
that satisfied the requirement reducing the sample to 21,050 users. Among the remaining
21,050 users, for 99.8% (20,999), it was of their actual first posts. To simplify the exposition,
in going forward, we call all the first posts satisfying the requirement, simply the first posts.
We used Apify to collect the comments. It allows access to the comments that are available
without logging in to Instagram and provides only up to 50 comments for each post. The
data included the username of the commenter and the text of the comment. While we don’t
use the text of the comment in our main analysis, we do analyze it in Section A6. The
comments were downloaded in January 2024. We were able to collect comments only for
16,630 posts, which is 79.0% of the 21,050 first posts. We could not collect comments for all
the first posts, because these posts either did not have any comments but mostly because we
attempted to collect these comments more than two years after collecting posts itself, and
in two years these users or their posts were either deleted or made private. Of the posts for
which we were able to collect comments, some had no non-cartel comments, leaving us with
16,386 posts. Hence, we were able to find non-cartel comments for 77.8% of the total 21,050
first posts. For both topic and general cartels the percentage of first posts for which we got
non-cartel comments was similar, 78%.
A5.4 Random Non-Cartel Commenter on Each Cartel Member’s
First Cartel Post
For each cartel member’s first post in cartels, we used a random number generator and
picked a random non-cartel user who had commented on the post. We picked these random
non-cartel users for 16,386 posts. Some of the randomly picked non-cartel commenting users
were the same across posts. Hence, we were left with 14,490 unique non-cartel commenting
A18

users. For these 14,490 non-cartel users, we collected their information about their number
of public posts. We collected this information using Apify in January 2024. Of these users,
24 didn’t exist anymore. So that we were left with 14,466 non-cartel users. Of those, 3,049
(21.0%) had no public posts. We had to exclude those user because they had no information
we could analyze. So that we were left with 11,417 public non-cartel users. We further limited
the sample to non-cartel users who had at least 10 public posts and this restriction reduced
the sample to 10,394 non-cartel users. For these random non-cartel users, we obtained the
history of all their Instagram posts from CrowdTangle. We did this to calculate authors’
similarity to the non-cartel users who commented on the post. For these non-cartel users,
the data was downloaded from CrowdTangle in January 2024. We were able to get the
history only for 10,280 non-cartel users (99%). For the remaining 114 usernames either they
had changed the username, made the account private or deleted it. Furthermore, we learned
that 551 (5%) of the 10,280 non-cartel users were associated with cartel members as they
had posted at least one post associated with a cartel member. The association can happen
as Instagram allows posts to be associated with multiple users (this is different from tagging
a user) or it can happen when users change usernames. We excluded those 551 non-cartel
users from our sample, while keeping the corresponding cartel members. That reduced the
sample of non-cartel users to 9,729. These 9,729 non-cartel users mapped to 10,683 first
posts because, as said above, some of these non-cartel users were commenting on multiple
posts.
A5.5 Photos from First Posts
We collected a photo from a single Instagram post for each user. For cartel members, we
use the first post each cartel member posted to the cartels. For non-cartel members, we
select their closest post within a symmetric time window to the cartel member’s post they
commented on. The photos were downloaded in February and March in 2024. We were able
to get the photos for only 16,693 (79%) cartel members and 9,269 (95%) non-cartel users.
The reason why we did not get photos for 21% of the cartel members is the same as for the
comments, that in the two years the posts were either deleted or made private. Similarly,
due the delay, we did not get photos for 5% of the non-cartel users. In the end, we were
left with 5244 authors whose first post was in general cartels and 3751 authors whose first
post was in topic cartels (including 488 authors that appear in both categories). Therefore,
the percentage reduction due to data limitations was similar for general cartels and topic
cartels. Thus we have no reason to expect that the data collection affected different cartel
types differently.
A19

A6 Online Appendix: Additional Empirical Results
Table A6.1: Summary statistics of cartel versus non-cartel comments
(1) (2)
Commenter not in cartel Commenter in cartel
Panel A: General cartels
Comment’s length (in words) 4.574 4.803
Share of negative comments 0.011 0.008
Comment’s similarity to the post’s photo 0.221 0.227
Observations (comments) 4432 10490
Panel B: Topic cartels
Comment’s length (in words) 4.942 5.274
Share of negative comments 0.010 0.006
Comment’s similarity to the post’s photo 0.220 0.228
Observations (comments) 3399 8463
Notes: Negative comments are classified using V ADER sentiment analysis model (Hutto and Gilbert, 2014).
While only about 1% of comments are classified as negative, most of these are misclassified as negative due
to the use of slang (for example: “hell of a view”, “killing this look”, “sick style keep it up”) or don’t criticize
the post (for example: “this is so scary” “I hate when it happens” “that looks so brutal”). Comments
similarity to the photo in the post is calculated using the CLIP model (see Section 4.2). Panel A includes
posts submitted only to general cartels, and panel B, only to topic cartels. According to the t-test, all
differences between columns 1 and 2, except for the share of negative comments are statistically significant
at 1 percent level.
Table A6.2: Most representative hashtags for each LDA topic
Topic number Topic label Most representative hashtags
Topic 1 Fitness #fitness #gym #workout #motivation #fitnessmotivation #fitfam #fit
#bodybuilding #health #training
Topic 2 Beauty #art #music #makeup #artist #photography #beauty #makeupartist
#design #mua #yoga
Topic 3 Fashion #fashion #ootd #instagood #style #photooftheday #fashionblogger
#picoftheday #beautiful #photography #beauty
Topic 4 Food #foodie #foodporn #food #instafood #liketkit #foodphotography
#foodstagram #foodblogger #yummy #delicious
Topic 5 Entrepreneur #motivation #entrepreneur #success #business #inspiration #luxury
#quotes #motivationalquotes #mindset #entrepreneurship
Topic 6 Travel #travel #travelgram #travelphotography #wanderlust #travelblogger
#nature #photography #instatravel #photooftheday #beautifuldesti-
nations
A20

Table A6.3: Sample construction
Number of authors
Panel A: Number of authors in the regression sample
Total number of authors in the cartel 21068
.. with cartel commenters 21050
.. and with non-cartel commenters 10683
.. and author has embeddings 10171
.. and cartel commenter has embeddings 10022
.. and non-cartel commenter has embeddings 8507
Panel B: Number of authors in the LDA sample
Total number of authors in the cartel 21068
.. with cartel commenters 21050
.. and with non-cartel commenters 10683
.. and author has LDA 8936
.. and cartel commenter has LDA 8835
.. and non-cartel commenter has LDA 6654
Table A6.4: Summary statistics of authors in cartel included/excluded from the sample
(1) (2)
Authors included vs excluded from the sample
Excluded Included
Panel A: Regression sample
Number of posts per user 583.0 735.7
Number of posts in cartel per user 9.5 12.0
Number of likes per post 777.9 699.8
Number of comments per post 28.8 29.5
Overperforming score -5.7 -4.6
% of disclosed sponsored posts 0.8 1.0
% of users with disclosed sponsored posts 25.9 34.4
Observations (authors) 12561 8507
Panel B: LDA sample
Number of posts per user 615.0 709.0
Number of posts in cartel per user 10.0 11.6
Number of likes per post 790.3 651.1
Number of comments per post 29.0 29.2
Overperforming score -5.6 -4.5
% of disclosed sponsored posts 0.7 1.1
% of users with disclosed sponsored posts 26.8 34.7
Observations (authors) 14414 6654
Notes: Average statistics per post are calculated by first taking averages across the posts for each user, and
then calculating averages across users.Overperforming scoreis calculated by CrowdTangle and measures the
number of comments and likes relative to the user’s previous 100 posts conditional on posts’ type and age.
Disclosed sponsored posts are identified following Ershov et al. (2025) based on disclosure hashtags (#ad,
#sponsored, #paidpartnership, #brandedcontent, #gifted, #paid, #partnership, #promotion, #branded,
#sponsoredby, #paidby). According to the t-test, all differences between columns 1 and 2, except forNumber
of likes per postin Panel A,Number of comments per postandOverperforming scorein Panels A and B,
are statistically significant at 1 percent level.
A21

Table A6.5: Summary statistics of authors in different types of cartel
(1) (2) (3)
Authors in cartels
General Topic Both
Number of posts per user 860.8 570.1 624.3
Number of posts in cartel per user 13.3 10.0 12.7
Number of words per post 51.4 59.3 58.9
Number of hashtags per post 14.0 15.0 14.4
Number of likes per post 829.1 501.2 768.2
Number of comments per post 32.1 25.4 31.0
Overperforming score -6.6 -1.8 -3.7
% of disclosed sponsored posts 1.2 0.8 0.6
% of users with disclosed sponsored posts 38.2 29.3 30.9
Observations (authors) 4756 3263 488
Notes: The table includes authors in the main regression sample. Average statistics per post are calculated by
first taking averages across the posts for each user, and then calculating averages across users.Overperforming
scoreis calculated by CrowdTangle and measures the number of comments and likes relative to the user’s
previous 100 posts conditional on posts’ type and age. Disclosed sponsored posts are identified following
Ershov et al. (2025) based on disclosure hashtags (#ad, #sponsored, #paidpartnership, #brandedcontent,
#gifted, #paid, #partnership, #promotion, #branded, #sponsoredby, #paidby). The sample includes all
posts for each user, except for word and hashtag counts, which are calculated using the data for the main
regression analysis (as described in Section 4.2): word counts use a single post per user, and hashtag counts
use 100 posts per user. According to the t-test, all differences between columns 1 and 2 are statistically
significant at 1 percent level.
Table A6.6: Summary statistics of users in cartels versus not in cartels
(1) (2)
User not in cartel User in cartel
Number of posts per user 769.1 730.9
Number of words per post 48.9 53.8
Number of hashtags per post 13.7 14.4
Number of likes per post 537.3 730.8
Number of comments per post 31.1 29.2
Overperforming score -10.3 -6.1
% of disclosed sponsored posts 0.8 1.0
% of users with disclosed sponsored posts 28.6 33.7
Observations (users) 7847 12088
Notes: The table includes users (authors and commenters) in the main regression sample. Average statistics
per post are calculated by first taking averages across the posts for each user, and then calculating averages
across users.Overperforming scoreis calculated by CrowdTangle and measures the number of comments and
likes relative to the user’s previous 100 posts conditional on posts’ type and age. Disclosed sponsored posts are
identified following Ershov et al. (2025) based on disclosure hashtags (#ad, #sponsored, #paidpartnership,
#brandedcontent, #gifted, #paid, #partnership, #promotion, #branded, #sponsoredby, #paidby). The
sample includes all posts for each user, except for word and hashtag counts, which are calculated using the
data for the main regression analysis (as described in Section 4.2): word counts use a single post per user,
and hashtag counts use 100 posts per user. According to the t-test, all differences, except forNumber of
comments per post, are statistically significant at 5 percent level.
A22

Table A6.7: Summary statistics of cartel members before and after joining the cartel
(1) (2)
Before After
first joining a cartel
Number of likes per post 501.6 960.2
Number of comments per post 21.0 43.0
Overperforming score -8.4 0.5
% of disclosed sponsored posts 0.6 1.7
% of users with disclosed sponsored posts 21.9 28.0
Observations (number of cartel members) 8447 8447
Notes: The table includes authors in the main regression sample who have posts both before and after
joining the cartel. Average statistics per post are calculated by first taking averages across the posts for
each user before and after joining the cartel, and then calculating averages across users.Overperforming
scoreis calculated by CrowdTangle and measures the number of comments and likes relative to the user’s
previous 100 posts conditional on posts’ type and age. Disclosed sponsored posts are identified following
Ershov et al. (2025) based on disclosure hashtags (#ad, #sponsored, #paidpartnership, #brandedcontent,
#gifted, #paid, #partnership, #promotion, #branded, #sponsoredby, #paidby). According to the t-test,
all differences are statistically significant at 1 percent level.
A23

0 .05 .1 .15 .2
Coherence score
2 5 8 11 14 17 20
Number of topics
Figure A6.1: LDA model coherence scores by the number of topics
Notes: The figure presents the Normalized Pointwise Mutual Information (NPMI) coherence score (y-axes)
for each LDA model, comparing models with the number of topics (x-axes) ranging from two to twenty. The
score is calculated for the top ten words in each topic with a window size of five words.
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample
(a) General cartels
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample (b) Fashion & beauty cartel
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample
(c) Fitness & health cartel
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample (d) Travel & food cartel
Figure A6.2: Authors’ topics: regression sample versus excluded
A24

0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample
(a) General cartels
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample (b) Fashion & beauty cartel
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample
(c) Fitness & health cartel
0 .2 .4 .6
Average topic share
FitnessBeautyFashion Food
Entrepreneur
Travel
Excluded Sample (d) Travel & food cartel
Figure A6.3: Authors’ topics: LDA sample versus excluded
A25

0 1 2 3 4 5
Density
.2 .4 .6 .8 1
Similarity of posts, photo+text embeddings
Non-cartel commenters
General cartel commenters
Random users
(a) General cartels, posts’ similarity
0 1 2 3 4 5
Density
.2 .4 .6 .8 1
Similarity of posts, photo+text embeddings
Non-cartel commenters
Topic cartel commenters
Random users (b) Topic cartels, posts’ similarity
Figure A6.4: Probability density of authors’ similarity to commenters and random users
Notes: The figures present kernel density estimates using the Epanechnikov kernel function of authors’ cosine
similarity to non-cartel commenters (grey line with solid circle markers), to random users (red dotted line),
to general cartel commenters (blue dashed line on Figure A6.4a), and to topic cartel commenters (green
dashed and dotted line on Figure A6.4b). The cosine similarity is calculated as the similarity of posts using
the photo and text embeddings from the CLIP model.
A26

A7 Online Appendix: Robustness Analysis
This Online Appendix describes that the regression results are robust to alternative ways to
construct outcome variables and alternative samples. Tables A7.1 to A7.3 presents results
where first, text embeddings (outcome variables in columns 1–3 in Table 1) are constructed
based on (A) random sample of posts; (B) all posts in 2017–2020; (C) the whole text instead
of hashtags; second, embeddings from the CLIP model (outcome variables in columns 4–6
of Table 1) are constructed based on (A) only the photos, (B) only the text. To alleviate
the concern that, instead of the average match quality, advertisers care about sufficiently
high matches, in Table A7.4, outcome variables are indicators for whether cosine similarity is
above the 75th or 90th percentile. It also presents the results where the sample includes only
the cartel commenters for whom we observe that they actually commented (Table A7.5). In
all these specifications, the estimates remain similar to the main results. When looking at
each of the topic cartels separately, we find that cartel commenters from the fitness & health
cartel are the most similar to natural engagement (Table A7.6). In our main analysis, the
quality of the additional engagement that cartels bring is proxied by the similarity between
the author and the cartel commenter. This is good proxy as for example, the topic analysis
shows (Figure 3) that cartel members natural commenters are interested in the same topic
as the cartel member irrespective of whether it is a topic or general cartel. However, as a
robustness check, in Tables A7.7 to A7.9, the outcome variable is the similarity of the author
and the commenting cartel member’s non-cartel commenter. Adding this one additional layer
of distance increases noise, and therefore, similarity measures are smaller, but results remain
qualitatively similar.
A27

Table A7.1: Alternative outcome variables: random posts; all posts in 2017–2020
(1) (2) (3) (4) (5) (6)
Dependent variable: Cosine similarity from text embeddings
Posts in general or topic cartels
General Topic Both General Topic Both
Random 100 posts All posts 2017-2020
General cartel commenter -0.044*** -0.044*** -0.028*** -0.038***
(0.002) (0.007) (0.002) (0.007)
Topic cartel commenter -0.012*** 0.006 -0.000 0.010
(0.003) (0.007) (0.003) (0.007)
Random user -0.073*** -0.075*** -0.062*** -0.066*** -0.068*** -0.062***
(0.002) (0.003) (0.007) (0.002) (0.003) (0.007)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.626 0.630 0.623 0.651 0.656 0.647
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4749 3261 487 4750 3261 488
Observations 44752 30459 6630 43650 29745 6546
Notes: Each column presents estimates from a separate panel data fixed effects regression. Unit of observation
is an author and another user pair. Outcome variable is the cosine similarity of the author to his commenter
or to a random user. In columns 1–3, the outcome variable is calculated based on the hashtags in user’s
100 randomly chosen posts; in columns 4–6, it is calculated based on hashtags in all posts in 2017–2020 (for
further details see Section 4.2.1). Each regression includes author fixed effects (equivalent to the post fixed
effects because only one post per author). In all the regressions, the base category is the author’s similarity
to a non-cartel commenter; andBase (non-cartel) meanpresents their average cosine similarity.General
cartel commenteris an indicator variable whether the commenter to whom the author’s cosine similarity is
calculated, is in the general cartel, andTopic cartel commenterwhether he is in the topic cartel.Random
userindicates that the author’s similarity is calculated to a counterfactual random non-cartel user. Standard
errors in parentheses are clustered at the author level.
A28

Table A7.2: Alternative outcome variable: whole text instead of hashtags
(1) (2) (3)
Dependent variable: Cosine similarity from text embeddings of full text
Posts in general or topic cartels
General Topic Both
General cartel commenter -0.043*** -0.042***
(0.002) (0.006)
Topic cartel commenter -0.014*** -0.003
(0.003) (0.006)
Random user -0.073*** -0.079*** -0.063***
(0.002) (0.003) (0.006)
Wald test,β Gen =β T op, p-value 0.000
Base (non-cartel) mean 0.659 0.665 0.662
Author fixed effects Yes Yes Yes
Authors 4756 3263 488
Observations 44900 30569 6665
Notes: Each column presents estimates from a separate panel data fixed effects regression. Unit of observation
is an author and another user pair. Outcome variable is the cosine similarity of the author to his commenter
or to a random user. It is calculated using the whole text instead of only hashtags (for further details see
Section 4.2.1). Each regression includes author fixed effects (equivalent to the post fixed effects because
only one post per author). In all the regressions, the base category is the author’s similarity to a non-cartel
commenter; andBase (non-cartel) meanpresents their average cosine similarity.General cartel commenter
is an indicator variable whether the commenter to whom the author’s cosine similarity is calculated, is in the
general cartel, andTopic cartel commenterwhether he is in the topic cartel.Random userindicates that the
author’s similarity is calculated to a counterfactual random non-cartel user. Standard errors in parentheses
are clustered at the author level.
A29

Table A7.3: Alternative outcome variables: photo embeddings, text embeddings
(1) (2) (3) (4) (5) (6)
Dependent variable: Cosine similarity of posts
Posts in general or topic cartels
General Topic Both General Topic Both
Photos embeddings Text embeddings
General cartel commenter -0.033*** -0.037*** -0.019*** -0.021***
(0.002) (0.005) (0.001) (0.004)
Topic cartel commenter -0.008*** -0.004 -0.009*** -0.008**
(0.002) (0.005) (0.002) (0.004)
Random user -0.051*** -0.053*** -0.044*** -0.016*** -0.018*** -0.022***
(0.002) (0.002) (0.005) (0.001) (0.002) (0.004)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.487 0.493 0.491 0.777 0.780 0.784
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4756 3263 488 4756 3263 488
Observations 44900 30569 6665 44900 30569 6665
Notes: Each column presents estimates from a separate panel data fixed effects regression. Unit of observation
is an author and another user pair. Outcome variable is the cosine similarity of the author to his commenter
or to a random user. It is calculated using embeddings from the CLIP model of either only photos (columns
1–3), or only text (columns 4–6). Each regression includes author fixed effects (equivalent to the post fixed
effects because only one post per author). In all the regressions, the base category is the author’s similarity
to a non-cartel commenter; andBase (non-cartel) meanpresents their average cosine similarity.General
cartel commenteris an indicator variable whether the commenter to whom the author’s cosine similarity is
calculated, is in the general cartel, andTopic cartel commenterwhether he is in the topic cartel.Random
userindicates that the author’s similarity is calculated to a counterfactual random non-cartel user. Standard
errors in parentheses are clustered at the author level.
A30

Table A7.4: Alternative outcome variables: indicator for cosine similarity above the 75th or
90th percentile
(1) (2) (3) (4) (5) (6)
Posts in general or topic cartels
General Topic Both General Topic Both
Similarity of users Similarity of posts
Text embeddings Photo+text embeddings
Panel A: Dep. var: Cosine similarity above the 75th percentile
General cartel commenter -0.168*** -0.151*** -0.157*** -0.154***
(0.008) (0.021) (0.007) (0.019)
Topic cartel commenter -0.062*** 0.003 -0.087*** -0.062***
(0.009) (0.021) (0.009) (0.020)
Random user -0.201*** -0.214*** -0.156*** -0.180*** -0.185*** -0.177***
(0.007) (0.009) (0.021) (0.007) (0.008) (0.019)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.393 0.419 0.383 0.391 0.396 0.389
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4756 3263 488 4756 3263 488
Observations 44900 30569 6665 44900 30569 6665
Panel B: Dep. var: Cosine similarity above the 90th percentile
General cartel commenter -0.136*** -0.146*** -0.131*** -0.124***
(0.006) (0.018) (0.006) (0.017)
Topic cartel commenter -0.071*** -0.058*** -0.061*** -0.059***
(0.008) (0.018) (0.007) (0.017)
Random user -0.158*** -0.176*** -0.149*** -0.142*** -0.122*** -0.126***
(0.006) (0.008) (0.018) (0.006) (0.007) (0.017)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.216 0.243 0.236 0.214 0.198 0.223
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4756 3263 488 4756 3263 488
Observations 44900 30569 6665 44900 30569 6665
Notes: Each column presents estimates from a separate panel data fixed effects regression. Unit of observation
is an author and another user pair. Outcome variable is an indicator whether cosine similarity of the author
to his commenter or to a random user is above the 75th or the 90th percentile. The percentiles are calculated
using all author and user pairs (cartel, non-cartel, and random users) and all cartels. In columns 1–3, the
cosine similarity of users is calculated using the text embeddings from the LaBSE model; in columns 4–6, the
cosine similarity of the corresponding users’ posts is calculated using the photo and text embeddings from
the CLIP model. Each regression includes author fixed effects (equivalent to the post fixed effects because
only one post per author). In all the regressions, the base category is the author’s similarity to a non-cartel
commenter; andBase (non-cartel) meanpresents their average cosine similarity.General cartel commenter
is an indicator variable whether the commenter to whom the author’s cosine similarity is calculated, is in the
general cartel, andTopic cartel commenterwhether he is in the topic cartel.Random userindicates that the
author’s similarity is calculated to a counterfactual random non-cartel user. Standard errors in parentheses
are clustered at the author level.
A31

Table A7.5: Alternative sample: commenters who actually commented
(1) (2) (3) (4) (5) (6)
Dependent variable: Cosine similarity
Posts in general or topic cartels
General Topic Both General Topic Both
Similarity of users Similarity of posts
Text embeddings Photo+text embeddings
General cartel commenter -0.055*** -0.062*** -0.033*** -0.032***
(0.003) (0.011) (0.002) (0.005)
Topic cartel commenter -0.020*** 0.005 -0.014*** -0.011**
(0.004) (0.011) (0.002) (0.005)
Random user -0.067*** -0.074*** -0.056*** -0.037*** -0.040*** -0.035***
(0.003) (0.003) (0.010) (0.001) (0.002) (0.004)
Wald test,β Gen =β T op, p-value 0.000 0.000
Base (non-cartel) mean 0.566 0.581 0.573 0.652 0.655 0.656
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 3361 2635 281 3361 2635 281
Observations 27379 21797 2961 27379 21797 2961
Notes: The table presents estimates from the same regressions as in Table 1 except the sample includes only
these cartel commenters who actually commented. Each column presents estimates from a separate panel
data fixed effects regression. Unit of observation is an author and another user pair. Outcome variable is the
cosine similarity of the author to his commenter or to a random user. Each regression includes author fixed
effects (equivalent to the post fixed effects because only one post per author). In all the regressions, the base
category is the author’s similarity to a non-cartel commenter; andBase (non-cartel) meanpresents their
average cosine similarity.General cartel commenteris an indicator variable whether the commenter to whom
the author’s cosine similarity is calculated, is in the general cartel, andTopic cartel commenterwhether he
is in the topic cartel.Random userindicates that the author’s similarity is calculated to a counterfactual
random non-cartel user. Standard errors in parentheses are clustered at the author level.
A32

Table A7.6: Heterogeneity by topic cartel
Posts in topic cartels, by the topic
Fashion Fitness Travel Fashion Fitness Travel
& beauty & health & food & beauty & health & food
Similarity of users Similarity of posts
Text embeddings Text+photo embeddings
Topic cartel commenter -0.014** 0.005 -0.033*** -0.011*** -0.006 -0.018***
(0.007) (0.008) (0.004) (0.003) (0.004) (0.002)
Random user -0.059*** -0.081*** -0.081*** -0.038*** -0.050*** -0.038***
(0.006) (0.008) (0.004) (0.003) (0.004) (0.002)
Base (non-cartel) mean 0.572 0.569 0.596 0.662 0.666 0.652
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 728 573 1881 728 573 1881
Observations 6386 4953 18184 6386 4953 18184
Notes: The table presents estimates from the same regressions as in Table 1 except the sample is a subset of
the sample in columns 2 and 5 of Table 1. Specifically, the sample consists of authors whose first cartel post
is either: only in Fashion and beauty cartel (columns 1 and 4), only in Fitness and health cartel (columns 2
and 5), or only in Travel and food cartel (columns 3 and 6). Note that those authors whose post is in multiple
cartels are excluded. Each column presents estimates from a separate panel data fixed effects regression. Unit
of observation is an author and another user pair. Outcome variable is the cosine similarity of the author to
his commenter or to a random user. In columns 1–3, the cosine similarity of users is calculated using the text
embeddings from the LaBSE model; in columns 4–6, the cosine similarity of the corresponding users’ posts
is calculated using the photo and text embeddings from the CLIP model. Each regression includes author
fixed effects (equivalent to the post fixed effects because only one post per author). In all the regressions,
the base category is the author’s similarity to a non-cartel commenter; andBase (non-cartel) meanpresents
their average cosine similarity.Topic cartel commenteris an indicator variable whether the commenter to
whom the author’s cosine similarity is calculated, is in the topic cartel.Random userindicates that the
author’s similarity is calculated to a counterfactual random non-cartel user. Standard errors in parentheses
are clustered at the author level.
A33

Table A7.7: Cartel commenters’ non-cartel commenters
(1) (2) (3) (4) (5) (6)
Dependent variable: Cosine similarity
Posts in general or topic cartels
General Topic Both General Topic Both
Similarity of users Similarity of posts
Text embeddings Photo+text embeddings
General cartel commenter (CC) -0.058*** -0.051*** -0.033*** -0.029***
(0.003) (0.008) (0.001) (0.003)
Topic cartel commenter (CC) -0.023*** -0.005 -0.016*** -0.008**
(0.003) (0.008) (0.002) (0.004)
αGen: General CC’s non-cartel commenter -0.061*** -0.054*** -0.034*** -0.024***
(0.003) (0.009) (0.001) (0.004)
αT op: Topic CC’s non-cartel commenter -0.054*** -0.024*** -0.028*** -0.022***
(0.004) (0.009) (0.002) (0.004)
βRan: Random user -0.070*** -0.075*** -0.055*** -0.039*** -0.041*** -0.031***
(0.003) (0.003) (0.009) (0.001) (0.002) (0.003)
Wald test,α Gen =β Ran 0.000 0.772 0.000 0.006
Wald test,α T op=β Ran 0.000 0.000 0.000 0.001
Wald test,α Gen =α T op 0.000 0.562
Base (non-cartel) mean 0.574 0.585 0.573 0.656 0.657 0.659
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 4236 2882 392 4236 2882 392
Observations 50660 34002 7573 50660 34002 7573
% value via general cartel 13.8 2.9 15.0 23.1
% value via topic cartel 27.9 56.3 30.9 29.2
Notes: The table presents estimates from the same regressions as in Table 1 (Equation (12)) where in
addition to indicators for the similarity between the author and the general cartel commenter (General car-
tel commenter (CC)), topic cartel commenter (Topic cartel commenter (CC)) and random user (Random
user), the regression also includes an indicator for the similarity between the author and the general cartel
commenters’ non-cartel commenter (General CC’s non-cartel commenter) and the topic cartel commenters’
non-cartel commenter (Topic CC’s non-cartel commenter). The last two rows present the similarity between
the author and cartel commenters’ non-cartel commenter rescaled to the natural-random difference, calcu-
lated as: 100×(1−α t/βRan), t∈ {Gen, T op}. This proxies the percentage of value of natural engagement
that advertisers get via cartels. Standard errors in parentheses are clustered at the author level.
A34

Table A7.8: Cartel commenters’ non-cartel commenters: posts in both cartels
(1) (2)
Dependent variable: Cosine similarity
Posts in both cartels
Similarity of users Similarity of posts
Text embeddings Text+photo embeddings
Topic cartel commenter’s non-cartel commenter 0.025*** 0.005*
(0.005) (0.002)
Base (general cartel commenter’s non-cartel commenter) mean 0.515 0.624
Author fixed effects Yes Yes
Authors 722 722
Observations 3730 3730
Notes: The table presents estimates from similar regressions as in columns 3 and 6 in Table A7.7. The
outcome variable is the similarity between the author and the cartel commenters’ non-cartel commenter. The
regression includes an indicator for the similarity between the author and the topic cartel commenters’ non-
cartel commenter. The base category is the similarity between the author and the general cartel commenters’
non-cartel commenter. The sample is larger than in Table A7.7 because it includes also the authors for
whom we were not able to calculate the similarity with non-cartel commenters which is the base category in
Table A7.7. Standard errors in parentheses are clustered at the author level.
Table A7.9: Cartel commenters’ non-cartel commenters: heterogeneity by cartel topic
Posts in topic cartels, by the topic
Fashion Fitness Travel Fashion Fitness Travel
& beauty & health & food & beauty & health & food
Similarity of users Similarity of posts
Text embeddings Text+photo embeddings
Topic cartel commenter (CC) -0.015** 0.009 -0.032*** -0.012*** -0.006 -0.018***
(0.007) (0.009) (0.004) (0.003) (0.004) (0.002)
αT op: Topic CC’s non-cartel commenter -0.048*** -0.039*** -0.061*** -0.024*** -0.034*** -0.028***
(0.007) (0.010) (0.005) (0.004) (0.005) (0.002)
βRan: Random user -0.061*** -0.077*** -0.080*** -0.040*** -0.051*** -0.038***
(0.007) (0.009) (0.004) (0.003) (0.004) (0.002)
Wald test,α T op=β Ran 0.008 0.000 0.000 0.000 0.000 0.000
Base (non-cartel) mean 0.576 0.561 0.596 0.664 0.666 0.652
Author fixed effects Yes Yes Yes Yes Yes Yes
Authors 596 443 1764 596 443 1764
Observations 6443 4673 21547 6443 4673 21547
% value via topic cartel 21.8 49.4 23.6 41.1 33.4 27.5
Notes: The table presents estimates from the same regressions as in Table A7.6 where in addition to indicators
for the similarity between the author and the topic cartel commenter (Topic cartel commenter (CC)) and
random user (Random user), the regression also includes an indicator for the similarity between the author
and the topic cartel commenters’ non-cartel commenter (Topic CC’s non-cartel commenter). The last row
presents the similarity between the author and cartel commenters’ non-cartel commenter rescaled to the
natural-random difference (100×(1−α T op/βRan)). This proxies the percentage of the value of natural
engagement that advertisers get via cartels. Standard errors in parentheses are clustered at the author
level.
A35
