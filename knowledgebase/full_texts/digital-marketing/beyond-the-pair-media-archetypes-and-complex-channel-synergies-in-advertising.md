---
title: 'Beyond the Pair: Media Archetypes and Complex Channel Synergies in Advertising'
url: https://doi.org/10.1177/00222429241302808
category: digital-marketing
subcategory: measurement
date: 2024-11
venue: Journal of Marketing
authors:
- J. Jason Bell
- Felipe Thomaz
- Andrew T. Stephen
source: openalex-oa
pdf_url: https://ora.ox.ac.uk/objects/uuid:5e5051e2-1e94-4a19-a7ce-187e4eeeefdd/files/s00000257t
pages: 71
chars: 126794
fetched_at: '2026-11-08T17:04:07+00:00'
kb_version: 1
---

# Beyond the Pair: Media Archetypes and Complex Channel Synergies in Advertising

The E↵ects of Advertising Media
Channel Combinations on Brand
Performance
J. Jason Bell
Sa ¨ ıd Business School
University of Oxford
jason.bell@sbs.ox.ac.uk
Felipe Thomaz
Sa ¨ ıd Business School
University of Oxford
felipe.thomaz@sbs.ox.ac.uk
Andrew T. Stephen
Sa ¨ ıd Business School
University of Oxford
andrew.stephen@sbs.ox.ac.uk

The E↵ects of Advertising Media Channel Combinations
on Brand Performance
October 9, 2024
Abstract
Prior research on advertising media mixes has mostly focused on single channels
(e.g., television), pairwise cross-elasticities, or budget optimization within single cam-
paigns. This is starkly detached from advertising practice where (i) there is an in-
creasingly large number of media channels available to marketers, (ii) media plans
employ complex combinations of channels, and (iii) marketers manage complementar-
ities among many (i.e., more than pairs) channels. This research empirically learns
complex channel complementaries using Latent Class analysis. Latent classes have
three useful properties: (i) they account for non-random selection of channels into
campaigns, (ii) they capture pairwise and higher-order interactions between channels,
and (iii) they allow for meaningful interpretation. We empirically describe the most
common media channel archetypes and estimate their e↵ectiveness on a set of com-
mon brand-related campaign performance metrics using a dataset of 1,083 advertising
campaigns from around the world run between 2008 and 2019. We ﬁnd that there is
not a systematically “best” media mix that generates dominant performance across
metrics. However, for each metric, clear recommendations can be made. We ﬁnd that
traditional channels (TV, outdoor) pair quite well with digital channels (Facebook,
YouTube), current marketing practice appears far from optimal, and simple strategies
are predicted to increase brand mindset metric lifts by 50% or more.
Keywords:
advertising, media planning, media complementarity, budget allocation, leading indicators

INTRODUCTION
As global advertising spend exceeded $1T ( Statista 2024)i n2 0 2 3 ,m a r k e t i n ga c a d e m i c s
and practitioners need to understand e↵ective media budget allocation approaches. Media
selection is also important for recipients of media budgets in the vast and complex market
for advertising. For instance Google reported $224.47B in revenue from advertising sales
in 2022 ( Inc. 2022), while the entire global print publisher ad revenue was $37.3B, just
behind Amazon’s advertising sales of $37.7B for that period ( Tobitt 2023). Despite an often
discussed shift to digital channels, traditional advertising products are hardly abandoned,
with $46.9B ﬂowing to outdoor ( MarketWatch 2023)a n d$ 3 7 . 2 Bt or a d i oa d v e r t i s i n gg l o b a l l y
in 2022 ( IMARC 2023).
Unsurprisingly, a $1T market attracts entrants, competition, and innovation. As a result,
marketers are met with a proliferation of media channels (e.g. the rise of retailer owned ad
channels like sponsored listings on Amazon or Walmart), as well as an increase in channel-
speciﬁc options to consider when developing media mixes. Marketers buying ads and media
planners are faced with a complex resource allocation problem that is seemingly intractable
with a vast number of possible media combinations from an expanding menu. The task is
made more dicult by the fact that media planners cannot immediately evaluate the results
of their choices, as “feedback” in the form of market results comes with both statistical noise
and often a long delay. In addition, media planners must often decide on budget allocations
in advance, and adapt to changing market conditions later. Practically, marketers must
simplify media allocation. This simpliﬁcation comes in the form of using heuristics, repeating
previous patterns, imitating competitors, following industry trends, or outsourcing to the
large support industry that o↵ers help with media planning (e.g. marketing mix modeling)
or validation (e.g. attribution).
Simpliﬁcation introduces errors that, from the perspective of a manager, are hard to
detect due to limited data relative to the high dimensionality of the problem. Unlike adjust-
1

ments to individual ads, A/B testing budget allocations on entire campaigns carries a high
ratio of cost to information yield. It’s worth recognizing that large ﬁrms are not in the habit
of running experiments with multi-million campaign investments against their major brands,
and tend to avoid risky experimentation. Furthermore, information about channel-speciﬁc
return on ad spend usually comes from channel owners, and is often analyzed in isolation
from concurrent channel spend decisions, which reduces its value for questions of channel
interaction. In some ways, the overwhelming uncertainty provides “cover” for managers to
justify approaches that are favorable to them for reasons other than performance. If two
strategies plausibly produce similar results, managers are likely to prefer the one that is
simpler to execute and explain. For example, buying ads based primarily on reach is one
strategy which may appeal to managers facing very high uncertainty, particularly as it aligns
with industry lay beliefs on reach-suciency (all results ﬂow from achieving high reach) and
the ease of measuring reach. Regardless of the criteria used, managers are likely to view the
media allocation task holistically and intuitively. This contrasts with the notion of managers
methodically simulating all possible channel combinations for every campaign and goal. The
combinatorial nature of the problem makes such exhaustive testing time and cost prohibitive.
From the p ersp ective of a researcher, di↵ering budget allo cation approaches taken by
managers creates variation across ﬁrms and industries in media mix tendencies, which could
potentially be exploited to uncover patterns in channel allocations and outcomes. W e take
advantage of the variation in campaign construction (channel usage and spend shares) using
au n i q u ed a t a s e tt h a ti n c l u d e s1 , 0 8 3l a r g em u l t i - c h a n n e lc a m p a i g n st h a tr a nb e t w e e n2 0 0 8
to 2019. These campaigns were undertaken by 557 global brands, and covered 23 major
industries in 51 countries. The dataset is broad enough that it could be used, in principle, to
detect patterns in campaign construction, and to estimate the relationship between di↵erent
patterns and advertising outcomes. However, the data alone are insucient because patterns
do not make themselves readily available in the raw data. To see this, consider two campaigns
with similar spend from similar brands. The ﬁrst allocates 60% to TV and 40% to Youtube,
2

the second allocates 60% to TV, 30% to Youtube, and 10% to cinema ads. These campaigns
are very similar to one another, but not exactly the same. To succeed in extracting patterns
from the data, we need a model that can represent these two campaigns as “close” but not
identical. We should avoid any model that would treat the two as totally distinct entities.
At the same time, we should also avoid a model which reduces them to simply the sum of
their parts, because that would fail to capture complementarities between the channels.
Our model relies on the concept of archetypes. An archetype is like the Platonic ideal of
ac a m p a i g ns t y l e . F o re x a m p l e ,am a n a g e rm i g h ti m a g i n eac a m p a i g nu s i n gd i g i t a lc h a n n e l s
with algorithmic targeting (e.g., Youtube). However, in practice, the manager might deviate
slightly from the envisioned approach and include some spend on radio (neither digital
nor algorithmically targeted). We could say the campaign turned out to be close to the
“algorithmic digital” archetype, though not a perfect realization of it. From this perspective,
archetypes are landmarks on a map of media allocation styles, and individual campaigns are
characterized by their coordinates on the map, and thus their relative distances to di↵erent
archetypes. Campaigns can be concisely described by projecting them into archetype space,
and “close” campaigns can be treated as similar but not identical. Past research on media
complementarity has been limited to main e↵ects of channels plus pairwise interactions.
This ignores interactions between more than two channels, and lacks parsimony. The lack
of parsimony is a serious concern when there are more than three or four channels. For
example, if there are eleven, there are 2047 possible channel combinations. Representing
each of these combinations as an additional term in a regression is hopelessly infeasible.
To apply this approach we must b e able to estimate archetyp es from data, which requires
that patterns in media allocation actually exist, and that we have a feasible estimation
procedure for recovering them. Whether the patterns exist is an empirical question which
we address in this work, using Bayesian latent class analysis as an estimation procedure.
We combine the archetyp es from the latent class analysis with a mo del predicting brand
lifts to understand the relationship between archetypes and outcomes. The breadth of our
3

dataset is critical for estimating archetypes with high external validity. To make archetypes
interpretable, we build an empirical Archetype Map, similar to the conceptual one described
above, and display it in two dimensions. A given campaign on this map can be thought of
as a mixture of the di↵erent more “pure” archetypes, and the empirical archetypes are given
as landmarks.
We make three contributions. First, our dataset and archetype model allow us to come
closer than prior research to addressing the critical practical question of how to best combine
media channels for high-performance against di↵erent advertising goals. By going beyond
simple pairwise combinations of media channels we are able to see how more complex com-
binations of channels perform, which is new to the marketing literature.
Second, our empirical study is, to the best of our knowledge, the largest academic study
of advertising performance and media mixes. Our unique dataset includes 1,083 large multi-
channel campaigns that took place during the period 2008 to 2019. These campaigns were
undertaken by 557 global brands, covered 23 major industries, and ran in 51 countries.
Finally, unlike prior research that has focused extensively on how advertising a↵ects short-
term sales outcomes, our dataset allows us to consider several brand-related outcomes that
are of strategic interest to marketers (e.g., brand awareness, associations, purchase intent).
While the existing literature has been able to examine the implications of few media channels
on short-term results, we focus on the consequences of many simultaneous media channels
on long-term marketing metrics.
Third, we produce several descriptive ﬁndings that strongly suggest the existence of me-
dia allocation tendencies among mangers. We ﬁnd that reach, which is relatively easy to
understand and measure, is optimized to a greater degree than lift (i.e., improvement on
brand metrics). We ﬁnd seven media allocation archetypes that each relate di↵erently to
brand outcomes, implying that managers cannot simply apply a single archetype without
respect to campaign goals. The archetypes have di↵erent risk proﬁles, with some archetypes
producing high expected outcome lifts but with high variation, while others produce lower
4

expected lifts but have much better worst-case outcomes. We also ﬁnd that budget concen-
tration (how unevenly managers allocate) relates favorably to lifts in Aided Awareness but
unfavorably to Association lifts. All of our substantive results are new to the literature.
LITERATURE REVIEW AND CONCEPTUALIZATION
Deighton (1996, p.243) ponders “Why would one not integrate a communications cam-
paign? Integration is surely the natural condition, the simple and obvious way of doing
things. Most marketing problems are solved with a combination of tools, even if the blend-
ing is no more complex than synchronizing advertising with trade promotion schedules.
Unintegrated communication campaigns are aberrations.” This perspective highlights that
the combination of marketing tools is a longstanding part of marketing thinking, captured in
both the concept of the marketing mix ( Culliton et al. 1948; Borden 1964)a sw e l la st h eM a r -
keting Concept itself ( Houston 1986). Therefore, it is unsurprising that the combinatorial
aspect of integration is connected to critical facets of marketing, such as budget allocation
(Venkatesan and Kumar 2004; Fischer, Albers, Wagner, and Frie 2011), marketing mix and
media planning ( Wedel and Kannan 2016), attribution ( Berman 2018), as well as advertising
e↵ectiveness (Danaher, Danaher, Smith, and Loaiza-Maya 2020)a n dt h eﬁ n a n c i a li m p a c t so f
marketing (McAlister et al. 2016). Since marketing in practice has combinatorial or “mixing”
principles at its core, it is also unsurprising that much of the literature on media e↵ectiveness
and related decisions has considered how di↵erent combinations of activities work. The IMC
literature has focused extensively on this; see reviews by Naik and Peters (2009), and Batra
and Keller (2016). These works lay out a framework of components for successful marketing
communication integration: (i) consistency, (ii) cross-e↵ects, and (iii) complementarity.
Interestingly, the concept of consistency of communication across media channels is
deemed a “solved problem” on the basis of numerous studies supporting its advantage ( Dun-
can and Moriarty 1998; Batra and Keller 2016), or placing it as a tactical part of integration
(Naik and Peters 2009), thus requiring no further investigation. However, these perspec-
5

tives also mark a signiﬁcant distinction between the three components of IMC. While the
complementarity and cross-e↵ects of channels relate to their inclusion in a media plan, the
consistency of communications relates to content development and management that occurs
alongside media channel selection and planning. Therefore, it is in the interplay of comple-
mentarity and cross-channel e↵ects, or what Naik and Peters (2009)t e r ms t r a t e g i cs y n e r g y ,
where combinatorial aspects of media planning are most relevant.
The questions in this type of research are relatively straightforward, such as seeking to
understand how di↵erent media channels operate together in order to see if and when they
“play nicely together” (i.e., are synergistic). However, conﬂating cross-e↵ects and comple-
mentarity of media channels, or collapsing both into a single construct (synergy) is not
always ideal. Indeed, we argue that in doing so prior research on media selection and inte-
gration has been overly concerned with simple media channel combinations (e.g., pairwise
combinations that can be captured with cross-e↵ects) at the expense of considering more
realistic mixtures of media channels that go beyond what can be empirically speciﬁed with
pairwise cross-e↵ects in advertising response models.
The importance of this distinction comes from Batra and Keller’s (2016) observation that,
while the literature has provided a signiﬁcant amount of empirical evidence on the existence
and importance of media interactions and cross-e↵ects, “it has not yet clearly explicated
the relative strengths and weaknesses of di↵erent media in inﬂuencing di↵erent communica-
tion outcomes” (p.123). The reason for this gap might be more apparent from the body of
literature on media complementarity and cross-e↵ects, a selection of which is shown in Ta-
ble W.F.1 (in Web Appendix F). It highlights a strong dedication to explaining advertising
impact on sales ( Gopalakrishna and Chatterjee 1992; Naik and Raman 2003; Danaher and
Dagger 2013; Srinivasan, Rutz, and Pauwels 2016; Kolsarici and Vakratsas 2018), or analo-
gous metrics like conversion and recruitment ( Gatignon and Hanssens 1987). However, not
all media campaigns are designed for activation or sales. Brand-related outcomes are often
important to practitioners. Yet the number of studies on brand outcomes is much smaller
6

than those on sales outcomes ( Edell and Keller 1989; Chang and Thorson 2004; Dijkstra,
Buijtels, and Van Raaij 2005; Fischer 2019).
This focus reduces the question of media selection and combinatorial channel e↵ects down
to a single advertising outcome. This concentration on one outcome creates a potentially
false equivalence between channels, as they are all measured as better or worse delivery
mechanisms for one metric; e↵ectively creating a literature-level environment where it is
dicult to identify complementarity (hence the reasonable simpliﬁcation to synergy). If
the construct requires “di↵erence” and “di↵erentially useful” as Batra and Keller (2016)
suggested, then the second component is only observable when conditions vary (outcomes).
Much of this equivalence is observed in studies concerned with within media plan budget
allocation and re-allocation toward an optimal position ( Fischer 2019), where the trade-
o↵ towards one speciﬁc goal is justiﬁed. However, it translates into a concerning industry
practice where media planning and purchase is similarly simpliﬁed to the bases of reach and
frequency (GRPs), rather than a combination of GRPs and the functionality or purpose of
the channel. Practitioner guidance encourages this behavior by focusing on campaign reach
measures ( Binet and Field 2013). In a way, it is similar to treating an ad exposure as equal
across channels, or perfectly fungible, such that an ad exposure on Facebook is identical
to an ad view on television or in a newspaper. This assumption goes against the notion
of di↵erentiation of media channel exposures ( Batra and Keller 2016), as well as ﬁndings
showing di↵erential consumer behaviors and the resulting importance in respecting resulting
channel di↵erences ( Schweidel and Moe 2014).
Further, prior literature has tended to leverage fairly limited datasets in terms of scale
and scope. The majority of prior studies rely on case studies, focusing on a single brand and
single campaign. Notable exceptions to this are Joo et al. (2014)a n dw o r kb yKolsarici and
Vakratsas (2018). Similarly, studies have strongly focused on simple dyadic relationships
between channels, such as the interaction between sales force and advertising ( Gatignon and
Hanssens 1987), television and radio ( Edell and Keller 1989), television and print ( Naik and
7

Raman 2003), television and search ( Joo et al. 2014), or television and social ( Fossen and
Schweidel 2019). Even those fewer studies that consider more than two channels simulta-
neously are restricted to the pairwise interactions ( Danaher and Dagger 2013; Srinivasan,
Rutz, and Pauwels 2016; Kolsarici and Vakratsas 2018; Fischer 2019)o rh a v ea g g r e g a t e d
data on multiple channels of the same category (e.g., traditional media and social media)
to allow for pairwise cross-e↵ects estimations ( Stephen and Galak 2012). In fact, Danaher
and Dagger ( 2013,p . 5 3 0 )s p e c i ﬁ c a l l yd e s c r i b et h ei n a b i l i t yt od e m o n s t r a t es y n e r g i e sa m o n g
the channels in their study, as the pairwise interactions among all ten channels became an
econometric problem. And in that vein, Batra and Keller ’s (2016) observed lack in guidance
on the appropriate selection and complementarity in media channels for a diverse set of out-
comes is not necessarily due to a lack of interest, or motivation; but rather from a simple
lack of opportunity to observe a sucient amount of brands, campaigns, and outcomes in
order to make meaningful statements.
DATA
Our dataset was provided by Kantar. All campaigns in our dataset were generated
by Kantar’s Insights Division in their CrossMedia Research practice, which is dedicated to
global market research on media campaign performance, advertising e↵ectiveness, and brand
impact. The dataset includes measures captured in brand lift and advertising e↵ectiveness
studies for 1,083 large multimedia advertising campaigns. The earliest campaign in the
dataset ran in 2008, and the most recent was in 2019. A total of 557 global brands are rep-
resented in these campaigns, with 23 di↵erent industries covered (e.g. automotive, ﬁnancial
services, retail). Campaigns come from 51 di↵erent countries, capturing all major markets
and regions (e.g. North America, Latin America, Europe, Asia Paciﬁc). A noteworthy fea-
ture of this dataset is that all campaigns are signiﬁcant in their budgets and size, meaning
that our sample is focused on large, professional advertising campaigns. For instance, the
average media-only spend (i.e. ignoring production, management, and ancillary costs) of
8

the U.S. campaigns in our dataset is USD 12 Million. 1 Kantar, on behalf of their global
brand clients, measured media budget allocation for each campaign across eleven types of
advertising channels: (i) Cinema, (ii) Facebook, (iii) Magazines, (iv) Newspapers, (v) On-
line Display (banners), (vi) Online Video, (vii) Outdoor, (viii) Point of Sale, (ix) Radio, (x)
Television, and (xi) YouTub e.
Table 1: Data Overview
Total number of campaigns 1,083
Mean Number of campaigns per year 92.1 (60.8)
Average Spend (U.S. campaigns only): $12M
Total number of brands: 557
Mean Lift (di↵erence between percentages)
Motivation 2% (2%)
Association 3% (3%)
Unaided Awareness 2% (3%)
Aided Awareness 1% (4%)
Number of Channels Used: Distribution
1 channel 6%
2 channels 13%
3 channels 26%
4 channels 25%
5 channels 19%
6+ channels 12%
Maximum Number of Channels Used 9 (of 11)
Notes: Standard deviations in parentheses.
Each observation in the dataset is an advertising campaign and an associated Kantar
study. As the studies were conducted in real-time against live campaigns across a varied
number of media channels, true random-assigned control was impossible. The approach
Kantar used is standard industry practice for multi-channel campaigns across digital and
non-digital channels. In this situation true exposure (or non-exposure) to a given campaign
cannot be fully controlled in channels such as television and outdoor like it can be in digital
channels such as YouTube and Facebook. In each campaign Kantar controlled for background
1The dataset does not have comparable ﬁgures across countries.
9

variation by surveying non-exposed people both before the campaign begins and throughout
the campaign. Non-exposure during the time of a campaign is estimated by Kantar using
media consumption self-reports from survey respondents. This is a typical “opportunity to
see” approach in the industry. For example, if a respondent reports that she does not use
Faceb o ok, she is eligible to b e in the control group for a Faceb o ok advertising campaign.
Kantar also directly asked respondents about seeing each campaign. Kantar additionally
accounted for the “predisposition” of a respondent towards each brand with information
about exposure to previous campaigns, use or awareness of the brand by family members,
brand equity in the survey region, and similar measures to determine a lift attributable to
the speciﬁc campaign alone.
In terms of campaign performance metrics, all of these campaigns had brand-related
objectives and therefore the studies that Kantar ran for their clients were all “brand lift”
studies. Four di↵erent brand-related outcomes were measured for each campaign: (i) Un-
aided Awareness, (ii) Aided Awareness, (iii) Association, and (iv) Motivation. The dataset
does not include sales performance data, since the measurement work Kantar did on behalf
of their clients focused solely on brand outcomes. Of course, it is entirely possible that
advertisers had a desire to impact sales as well as brand outcomes. Sales data, however,
is not part of this proprietary Kantar dataset and therefore is not available. We have four
dependent variables, which are all lifts (di↵erences between proportions). Each question
used to measure the dependent variables is coded so that a value of 1 indicates a desirable
response for the brand. Lift is then a proportion, and lies between 0 and 1. A lift of 1, the
maximum, means that every respondent in the exposed group answered armatively and
all control respondents answered negatively. Table 1 summarizes key features of the dataset.
Figure 1 shows histograms of our four outcomes. Note that each is greater than or equal
to zero, with the exception of one observation, which we drop. The histograms make clear
two modeling challenges. First, there is a large mass of observations at zero, for three of the
four outcomes. We must account for this zero-inﬂation. Second, the data distributions have
10

0
50
100
0.000.050.100.150.200.25
Motivation
Count
0
20
40
60
0.000.050.100.150.200.25
Association
Count
0
200
400
0.000.050.100.150.200.25
Unaided Awareness
Count
0
200
400
600
800
0.000.050.100.150.200.25
Aided Awareness
Count
Figure 1: Outcomes are Positive and Right Skewed
relatively long right tails.
Figure 2 shows that after a mild decrease in the number of channels per campaign from
2008 to 2013, the number of channels began increasing to reach a high in 2019. As more
new media channels and formats appear, complexity is likely to continue increasing.
Finally, we provide some model-free evidence that brands have idiosyncratic tendencies in
media selection, which suggests we should be able to identify archetypes in the dataset. For
0
1
2
3
4
200820092010201120122013201420152016201720182019
Year
Avg. No. Channels per Campaign
Figure 2: Channel Consolidation then Expansion
11

0.0
0.2
0.4
0.6
TV Onl. Disp. Onl. Vid. Radio POS Cinema
Outdoor Facebook YoutubeNewspapersMagazines
Avg. Share
Figure 3: Patterns in Share
0.00
0.25
0.50
0.75
1.00
TV Onl. Disp. Onl. Vid. Radio POS Cinema
Outdoor Facebook YoutubeNewspapersMagazines
Percent Usage
Figure 4: Patterns in Usage
eleven brands most commonly appearing in our dataset, we plot the average share allocated
to each channel, as well as the usage probability of each channel, in Figures 3 and 4.I t i s
evident that whereas brands exhibit some idiosyncrasies in share of spend across channels,
there is much more variation when looking at campaigns in terms of usage (a binary indicator
of zero vs. non-zero spend). This supports our choice of usage as the input into the archetype
model, as discussed below.
Measures
Keller (1993)s u g g e s t st h a tm a r k e t e r ss h o u l dt r a c kc h a n g e st od i ↵ e r e n td i m e n s i o n so f
brand knowledge over time, and importantly, how these changes might be related to dif-
ferent marketing mix choices. The dependent variables in our study follow this pattern,
and in a structure consistent with Keller’s brand equity framework. Each of the following
four outcome measures is described in terms of its campaign lift, or the (Kantar-estimated)
campaign-only attributable change in the metric as measured by the di↵erences between the
response of pre-campaign and during-campaign consumers in exposed versus non-exposed
matched control groups. These campaign lifts can theoretically take values between -1 and
1, but in practice are almost exclusively non-negative. Lastly, as all brand outcomes are
measured for all campaigns, regardless of goal, and then passed through a signiﬁcance ﬁlter,
the resulting data include a number of exact zeros (i.e. non-signiﬁcant quasi-experimental
lifts). We must appropriately handle these exact zeros in the modeling, and we do so with
12

a hurdle model. The four outcome measures we use are deﬁned below.
Unaided awareness measures knowledge and memory of the brand without direct cues or
prompts. While we are not permitted to list the exact questions used on the Kantar survey,
we can say that the question used by Kantar is very similar to many used across the industry.
The question usually takes the form “which brands in [category] are you familiar with?”
Aided awareness measures recognition of the brand with the aid of a prompt or a direct
cue. Like the question used to measure unaided awareness, Kantar follows typical industry
practices. Most questions in the industry are of the form “which of the following brands
in [category] are you familiar with?”, followed by a list of brands to select from, where
respondents are allowed to indicate multiple brands.
Association is related to the second dimension of the Keller (1993) brand knowledge
framework, the brand image. Association captures the presence and strength of associative
connections to the brand, regardless of favorability. Explicitly, it considers whether respon-
dents can connect a particular message, positioning statement, slogan or other stimuli used
in advertisements to the focal brand. The questions used to measure this are often dependent
on the category or even the speciﬁc brand. Some very general associations such as “high
quality” or “trustworthiness” can be measured for a wide variety of brands and categories.
Two examples of this type of question have the form “which of these brands is the most
[association]” or “which of these brands has the slogan: [slogan]”
Motivation is an index of brand metrics meant to proxy for near-term sales. The con-
struction of the exact metric is proprietary, but it is highly correlated with Purchase Intent
(which is one of its constituent metrics), so we interpret ﬁndings as if Motivation is essentially
Purchase Intent. Of the four metrics, Motivation is the most like a sales measure, thus pro-
viding the closest (or at times identical) measure to the existing body of work on cross-media
e↵ects described in Table 1. We then make use of both the subset of the eleven channels
selected (binary indicators of positive spend) as well as the share of campaign budget spent
on each channel as the focal point of our analysis, and in the empirical study of Archetypes
13

(or clusters) that we describe next. We also control for time (year) and spend concentration
(deﬁned below), and we use the brand and category (industry) as control variables in a
random intercepts speciﬁcation.
METHODS
Descriptive Stochastic Frontier Analysis
In our initial discussion, we highlighted that practitioners are concerned with mindset
metrics, beyond immediate activation ( Binet and Field 2013), consistent with theory and
empirics ( Vakratsas and Ambler 1999; Srinivasan, Vanhuele, and Pauwels 2010). As such,
it would be logical to assume that managers are therefore optimizing their media selection
towards this declared goal. However, we also described a practitioner focus and guidance
on “reach maximization and suciency,” which carries with it the implication that channel
complementarities are inconsequential, and ad exposure are at least somewhat fungible across
media channels in the construction of an e↵ective media campaign seeking to achieve these
declared intermediate brand goals (e.g. awareness, associations, etc).
Conversely, we put forward that ﬁrms (and academics) are missing the complementarity
aspect of planning and focusing on coarse audience maximization strategies, rather than
goal and outcome-oriented approaches. So, in order to interrogate these assumptions, we
will rely on a “model-light” description of our data via Stochastic Frontier Analysis (SF A).
This approach is used to describe the eciency of resource allocation for the creation of
a given output. It estimates an ecient frontier, and ranks the ineciency of observed
resource allocation decisions according to their proximity to this estimated theoretical line
(see Krasnikov, Jayachandran, and Kumar 2009 for a detailed description of the approach).
In our case, we consider channels as inputs and lifts in any of the above mentioned brand
mindset metrics as the outcome. And if the assumption holds that managers’ strategic
choices are correct and aligned with their stated and demonstrated intent, then campaigns
should be ecient in delivering brand outcomes, with an expected large mass of campaigns
14

relatively close to the most ecient observed campaigns. Columns two and three of Table 2
shows the distribution of campaigns under the ecient frontier by distance, along with their
associated mean observed lifts (outcome).
Table 2: SF A Mindset Metric Lift
Lift SF A Reach SF A
Decile to Ecient Frontier % of Campaigns Mean Lift % of Campaigns Mean Reach
0.0 3.72% 0.13% – –
0.1 8.81% 0.42% – –
0.2 11.89% 0.74% 0.62% 24.64%
0.3 13.89% 1.18% 0.62% 33.07%
0.4 17.69% 1.75% 2.07% 45.14%
0.5 18.23% 2.61% 1.65% 55.50%
0.6 17.08% 4.16% 5.99% 65.65%
0.7 7.60% 7.97% 8.88% 74.77%
0.8 1.08% 18.46% 20.66% 85.42%
0.9 – – 59.50% 95.23%
@ Frontier – – – –
Notes: Reach is stated as % of available audience exposed to the ad.
First, we must recognize that there is no ex ante expectation that campaigns would reach
the ecient frontier, but the best performers do highlight what is practically achievable.
However, it is rather surprising that so few campaigns exist at the top of the e↵ectiveness
ladder, and that the disparity of average outcomes is so large. Furthermore, eciency/in-
eciency with respect to brand metrics appears to be approximately normally distributed
around the mid-eciency point. This result provides some evidence against the assumption
that managers and media planners are already making optimal choices, despite the practical
guidance that 60% of their advertising should move these metrics. 2
Next, we consider a di↵erent construction of the stochastic frontier where the intended
outcome is campaign reach. As noted previously, practitioners are also given the guidance
2At the request of an anonymous reviewer, we reconsider the SF A with the 10 largest campaign lifts removed to
examine the inﬂuence of extreme outlier performances. The resulting SF A from this restricted set maintains the same
distribution of results, again peaking at the 80% proximity to the ecient frontier, but o↵ering an average 15.23%
lift in outcomes at this level.
15

to maximize reach, which carries the risk of downgrading or entirely dismissing complemen-
tarities, as planners can opt for channels with larger audiences, and continuously pay more
to reach increasingly greater proportions of them, with no consideration for any mechanical
or functional di↵erences between channels and their consequences for the campaign goal.
Columns four and ﬁve of Table 2 show these results.
This second frontier shows a markedly di↵erent pattern. With respect to reach, 80% of
campaigns fall near the two highest reach-eciency scores. Compared to 8% of campaigns
on the two highest eciency bands for brand metrics (again, metrics that are important
enough for brands to pay an agency to measure their shift as a result of multi-million dollar
campaigns). It is clear that optimization is happening against reach, but not campaign
goal. Managers are indeed following industry practice and guidance by organizing campaigns
around achieving highest reach. Yet, the disconnect between both frontiers suggests that
managers’ belief of reach suciency is incorrect, otherwise brand metrics would similarly
improve with reach. Lastly, as the reach suciency (and channel/impression fungibility)
argument stood in direct opposition to the concept of complementarities, we take this as
some initial evidence supporting our argument that complementarity is a crucial component
of planning media mixes. We next we turn to the main analysis of complementarity e↵ects.
Main Analysis
Our modeling approach must account for several important features of the dataset. These
features are: (i) complex interactions between channels through campaign types, (ii) the
skewed and bounded shape of the outcome distributions, and (iii) the presence of a group of
exact zeros on each of the outcome variables. We handle the ﬁrst using a Bayesian Latent
Class approach, and the second two with a Gamma hurdle regression model.
16

Campaign Types and Channel Interactions
Including higher-order interactions comes with a combinatorial challenge. With eleven
media channels in our data, specifying every possible pair of channels, triple of channels, and
so on, up to all eleven, would require 2 11  1=2 0 4 7i n t e r a c t i o nt e r m s . I nt h ec r o s s - e ↵ e c t s
research tradition, a typical solution to this combinatorial explosion is to limit the analysis
to pairwise interactions between media channels. Limiting interactions to pairs would reduce
the number of combinations to 55. However, even this number of combinations is intractable
for modeling and interpretation, and would result in the same issues previously documented
by Danaher and Dagger (2013). For the sake of illustration, we report our attempt at
this approach using a regression approach similar to what is found in much of the media
cross-e↵ects literature in Web Appendix D.
Instead of blindly or exhaustively including interaction terms, which is doomed to fail,
we took a practical approach. We are interested in how di↵erent campaign types compare
across the outcome measures. This means that we should only be concerned with the com-
binations of channels that actually appear in data (i.e., a vast number of the theoretically
possible combinations in fact are never observed). Further, we are interested in comparing
the e↵ectiveness among “typical” media plans. This type of comparison is distinct from try-
ing to statistically estimate interactions between individual channels to ascertain the extent
to which they operate in synergy.
Taking this logic into account, our mo deling approach empirically ﬁnds common me-
dia plan “archetypes” across all of the campaigns in our data. These archetypes embody
di↵erent media channel combinations. We used Bayesian Latent Class analysis to ﬁnd the
archetypes, which allows us to determine the most typical and therefore practically relevant
combinations. Latent Class analysis ﬁnds campaign archetypes, and each individual cam-
paign is assumed to be some mixture of the archetypes. The degree of each archetype is
given by membership probabilities which are estimated for each campaign. Latent Classes
can then be used for clustering by assigning each campaign to the archetype for which it has
17

the highest membership probability. Using Latent Classes, we limit the number of combi-
nations to consider, and the archetypes are interpretable and relate to theory. Finally, by
estimating the archetypes from actual campaign spends, we ensure that the combinations we
study are substantially present in the data. At the same time Latent Classes exhibit channel
combinations of more than two, so that we are not conﬁned to dyadic relationships.
One alternative to Latent Class analysis is a neural network. This would allow us to
handle a high degree of complexity and determine combinations empirically, but neural
networks are notoriously dicult to interpret. Latent classes or archetypes, on the other
hand, are easily interpretable and not only do they aid in the main task of understanding
e↵ectiveness, the patterns of channel usage they uncover are ﬁndings in their own right.
Bayesian Latent Class Model
We estimate the latent class model twice, once as an exploratory exercise to determine
the best number of latent classes, and a second time in a joint estimation with the regression.
The outcomes or dependent variables in the latent class model are indicators of which chan-
nels were used on a given campaign, which will later become independent variables in the
Gamma hurdle model. In the exploratory latent class model — estimated by itself — mem-
bership probabilities and class parameters are estimated. In the second latent class model
—i n t e g r a t e dw i t ht h er e g r e s s i o n—t h em e m b e r s h i pp r o b a b i l i t i e sa n dc l a s sp a r a m e t e r sa r e
estimated, just as before. However, in the integrated version, the membership probabilities
for each campaign are included as covariates in the regression. These parameters will reﬂect
the di↵erential performance associated with each archetype.
To explain the Latent Class mo del, we start with the likeliho o d contribution for a single
observation. A single observation is a vector of channel usage indicators. Let n 2{ 1,. . . ,N}
be the campaign index, and c 2{ 1,. . . ,C} be the channel index, and snc is the share of
spend allocated to channel c in campaign n.T h e n t h e v e c t o r o f c h a n n e l u s a g e i n d i c a t o r s ,
18

un =( un1,. . . ,unC )i sd e ﬁ n e da s :
unc =
8
>><
>>:
1i f snc > 0
0o t h e r w i s e .
(1)
Index classes with d 2{ 1,. . . ,D},a n dd e ﬁ n ezn as the class label for observation (cam-
paign) n.T h e l i k e l i h o o d c o n t r i b u t i o n f o r o b s e r v a t i o nn is:
Pr (un)=
DX
d
⌫d
CY
c
Pr (unc|zn = d)( 2 )
Since unc is binary, we use a Bernoulli distribution to model the usage probability, with
parameters wcd = Pr (unc =1 |zn = d). Collect unc into a matrix U .I f ⌫ =( ⌫1,. . . ,⌫D)a n d
W is a K ⇥ D matrix containing the set of parameters {wcd} with rows corresponding to
channels and columns to classes, then the Latent Class likelihood for the full dataset is:
`lc(U |⌫, W )=
NY
n
" DX
d
⌫d
CY
c
wcd
#
(3)
EXPLORATORY LATENT CLASS ANALYSIS
To determine the numb er of classes, we estimated an exploratory Latent Class mo del 7
di↵erent times, with the number of classes varying from 2 to 8. Each time we computed the
PSIS-LOO CV, the approximate leave-one-out cross-validation for Bayesian models using
Pareto smoothed importance sampling ( Vehtari, Gelman, and Gabry 2017, Vehtari et al.
2022). This allows for model comparisons using the pointwise expected log predictive density
(ELPD). The best ELPD is reached at 7 classes. The ELPD values are in Web Appendix C.
The likelihood function in Equation ( 3)i si n v a r i a n tt op e r m u t a t i o n so ft h ec l a s sl a b e l s .
When running separate chains, convergence for class-speciﬁc parameters can fail because
of this, since separate chains often explore relative to di↵erent orderings, which has the
19

e↵ect of reordering the columns of W and the elements of ⌫.T h i s p r o b l e m i s k n o w n a s
label switching. Label switching does not a↵ect model outputs for which the discrete class
probabilities have been marginalized out (such as the PSIS-LOO CV values used to determine
the number of classes). However, to estimate class-speciﬁc parameters, label switching must
be prevented. In practice, di↵erent approaches are used to solve this problem, but one of
them is to use a “non-exchangeable prior”, meaning a prior which di↵ers across classes,
thus keeping each chain on the same relative ordering ( Betancourt 2017)b yp e n a l i z i n gt h e
sampler if it moves toward di↵erent orderings. We use a non-exchangeable prior by ﬁrst
getting point estimates via the EM algorithm, a standard approach for Latent Class. We
use the R package poLCA (Linzer and Lewis 2011)t og e tt h e s ep a r a m e t e rp o i n te s t i m a t e s .
Then we put priors on W and ⌫ centered around the EM point estimates. This solves the
label switching problem for our dataset. We provide details of the prior speciﬁcations and
code in Web Appendices A and B.
Outcome Model: Bayesian Gamma Hurdle Regression
We have four dep endent variables, which are all lifts expressed as decimals (di↵erences
between proportions). The outcome (lift) distributions are positively skewed. In principle a
lift could be negative, but we observe this only once in the entire dataset. 3 Thus, in practical
terms, lifts are bounded at 0. The lifts are also bounded above by 1, as noted above. There
are some exact zeros, however, which represent campaigns that had no detectable lift for a
given outcome. To appropriately model each of these aspects, we use a hurdle model with a
Gamma density for the response distribution.
We selected a Gamma regression by visual p osterior predictive checks using only shares as
variables. Candidate distributions were: Normal, Log-Normal, Exponential, Exponentially
Modiﬁed Gaussian, Laplace, and Gamma. The Gamma best ﬁt the lift distributions above
zero. We then add the hurdle component to account for the mass at zero. 4
3We drop this observation.
4The Gamma distribution can in principle produce values above 1, which is impossible for a lift. In practice this
20

Gamma regression is a generalized linear model (GLM) that assumes a Gamma distribu-
tion for the conditional distribution of the response. GLMs use a link function to transform
the conditional mean of the response, which in our case can only take non-negative values,
to the same space as the linear predictor ( xn). We pair this with a hurdle component
paramaterized by 0n.I f yn is an observation of an outcome, and xn contains covariates,
then the generative model for yn is
yn =
8
>><
>>:
0w i t h p r o b a b i l i t y l o g i s t i c ( 0n)
⇠ (exp(0n + 1xn), )o t h e r w i s e.
(4)
The variable  is the shape parameter of the Gamma distribution. The expectation of
the Gamma distribution in Equation ( 4)i s[ e x p (0n + 1xn)] / =e x p (0n + 1xn). The
link function g(·)f o raG L Ms a t i s ﬁ e sE[yn|xnn]= µ = g1(xnn), our link function is log( ·).
Intuitively, the outcome model has two components. The ﬁrst component accounts for
whether a lift value is exactly zero or positive. The second component models the magnitude
of the outcome conditional on the outcome being positive. The ﬁrst component, the hurdle,
has a simple speciﬁcation with random intercepts that vary according to category. Letting
a index categories and letting an stand for the category of campaign n:
0n =0 + an
an
iid
⇠N (0, ,a)
(5)
In words, each category has a constant e↵ect that shifts the probability of exact zeroes.
The category constants share a common distribution.
The second component, the Gamma GLM, models the values of the outcomes conditional
on those values being positive. The intercept 0n has a random intercepts speciﬁcation.
happens extremely rarely, perhaps 1 time per 1,000 draws. In all simulations from the model, we drop any draws
above 1.
21

Recalling that a indexes categories and letting j index brands:
0n =0 + an + jn
an
iid
⇠ N (0, ,a ), jn
iid
⇠ N (0, ,j )
(6)
Deﬁne ⌘0n =l o g i s t i c (0n)a n d n =( 0n, 1). Then conditional on the observation-
speciﬁc parameters, the likelihood contribution for observation n is
Pr(yn|⌘0n, n, )= ⌘0nI{yn =0 } +( 1  ⌘0n)I{yn > 0}(yn|exp(0n + 1xn), )( 7 )
Collect yn into a vector y,a n ds i m i l a r l yf o rxn into a matrix X,a n df o r ⌘ and .T h e n
the Gamma hurdle likelihood is:
`gh(y, X|⌘, , )=
NY
n
Pr (yn|⌘0n, n, ). (8)
The full likelihood for the joint model is the product of the Latent Class likelihood and
the Gamma hurdle likelihood:
`(y, X, U |⌘, , , ⌫, W )= `lc(U |⌫, W )`gh(y, X|⌘, , ). (9)
We estimate the standalone Gamma hurdle regression using the NUTS algorithm ( Ho↵-
man and Gelman 2014)f r o mt h eStan probabilistic programming language ( Carpenter et al.
2017). We also estimate the joint Gamma hurdle and Latent Class model with NUTS.
Variables
The Gamma hurdle regression includes a random intercept by category for the hurdle
as shown in Equation ( 5), and a random intercept for the outcome regression by category
and brand as shown in Equation ( 6). In addition, the Gamma regression includes Archetype
membership probabilities for each campaign, the concentration of spend for the campaign,
22

at i m et r e n d ,a n dt h es p e n ds h a r e sf o re a c hc h a n n e l .
The membership probabilities link the Latent Class model to the Gamma hurdle model.
At each iteration of the sampler, membership probabilities for each campaign are calculated
conditional on the current Latent Class parameter draws and included in the Gamma hurdle
as covariates. We leave Archetype 2 out as the reference class. 5
We deﬁne
concentrationnc =
X
c
s2 nc.
This is a version of the Herﬁndahl-Hirschman Index used as a metric for market concentration
in economics ( Tuckman and Chang 1991). Here we use the shares as decimals rather than
whole numbers to keep consistent scales across variables. A concentration value of 1 means all
budget is allocated to a single channel. For 11 channels, the minimum value of concentration
is achieved when a campaign spends equally on all 11 channels: (1 /11)2 + ... +( 1/11)2 =
11 ⇥ (1/11)2 =1 /11 ⇡ 0.09.
We include a time trend, ranging from 2008 to 2019. Finally we include the shares {snc}
for each campaign and channel. We leave Online Video out as the reference channel. 6 Table
3 summarizes the variables used and which models they enter.
Table 3: Variable Deﬁnitions
Variable Deﬁnition Enters which model
Channel Binary values: 1 means Latent Class
indicators positive spend
Membership Campaign membership probability Gamma hurdle
Probabilities for each Archetype
Concentration Sum of squared spend shares Gamma hurdle
Time trend The campaign year (centered) Gamma hurdle
Channel shares Share of spend on each channel Gamma hurdle
5Since the membership probabilities sum to one, the design matrix is not full rank if all are included.
6Since the shares sum to one, the design matrix is not full rank if all shares are included.
23

RESULTS
There are two sets of results to explore. The ﬁrst are descriptive and detail di↵erent
campaign archetypes. These results show which groups of media channels are commonly
used together, and typical spend concentrations. These descriptive results are shown next.
The second set of results show the estimates of the regression coecients relating archetypes,
campaign concentrations, and allocation shares to the four outcomes. These results show
which clusters and individual channels are associated with better advertising performance
on each of the outcomes. We call this the outcome model and the results are shown below.
Descriptive Results
Table 4 gives the archetype proﬁles numerically, and the same results are plotted in Figure
5.T h e a r c h e t y p e p r e v a l e n c e i s t h e p a r a m e t e r e s t i m a t e o f (⌫c), which empirically is almost
the same as the percent of campaigns assigned to each archetype. 7 For each archetyp e, we
also include in Table 4 the probability of usage for each channel, as well as the average
concentration of spend among campaigns assigned to each archetype.
Table 4: Achetype Proﬁles
Archetype ! 1234567
Prevalence: .18 .23 .18 .13 .10 .08 .10
Usage Prob: Cinema .02 .13 .08 .06 .25 .39 .15
Usage Prob: Magazines .27 .03 .10 .20 .19 .31 .05
Usage Prob: POS .10 .11 .16 .35 .03 .06 .24
Usage Prob: Newspapers .11 .02 .13 .06 .56 .36 .09
Usage Prob: Radio .16 .13 .24 .16 .50 .30 .19
Usage Prob: Youtube .20 .05 .94 .04 .04 .09 .31
Usage Prob: Online Video .13 .67 .03 .31 .31 .04 .78
Usage Prob: Facebook .52 .23 .72 .56 .35 .78 .93
Usage Prob: Online Display .15 .64 .64 .47 .76 .06 .26
Usage Prob: Outdoor .06 .35 .49 .86 .66 .94 .73
Usage Prob: TV .84 .93 .94 .74 .84 .97 .97
Avg. Concentration .76 .59 .52 .48 .43 .44 .42
7The di↵erence exists because assignment to classes is stochastic.
24

Figure 5: Achetype Proﬁles
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 1
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 2
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 3
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 4
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 5
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 6
Avg. Concentration TV Outdoor Online Display Facebook Online Video Youtube Radio Newspapers POS Magazines CinemaPct. of Campaigns:
0.00 0.25 0.50 0.75 1.00
 Archetype 7
25

TV is the most commonly used channel, and cinema the least. Three channels see usage
less than half the time for any archetype: cinema, magazines, and point of sale. Archetype
2 is the most prevalent (23%). To ease interpretation, we also provide Figure 6.
The map was created by multidimensional scaling with the L1 norm for measuring dis-
tance (also known as city block or Manhattan distance). The campaigns are plotted by
weighting the Archetype coordinates by the campaign membership probabilities. An impor-
tant takeaway from the archetype map is that campaigns are not easy to organize in terms
of a few dimensions such as legacy vs. digital or broad vs. narrow. Archetype 5 is mostly
legacy channels, but with a high tendency to use online display. Archetype 6 is similarly
reliant on legacy channels but with a heavy use of Facebook.
The map is drawn and labeled according to what best discriminates archetypes. This
does not mean that archetypes toward the extremes are “pure-play” but rather that they
are distinctive for using some channels more or less. For example, Archetypes 7, 3, and 1
make high use of channels with algorithmic targeting (e.g., YouTube), but vary in degree
of legacy channel usage. Archetype 7 uses outdoor 73% of the time while Archetype 1 uses
outdoor 6% of the time. Despite this, they are still close because of the high tendency to
include algorithmic digital channels.
Integrated Model Results
In Table 5,w ep r e s e n tt h er e s u l t so ft h ei n t e g r a t e dL a t e n tC l a s sa n dB a y e s i a nr e g r e s s i o n .
As a reminder, the link between the two models is that the archetype membership proba-
bilities for each campaign are included as covariates in the regression. Also recall that the
regression incorporates a hurdle for zero vs. non-zero response, and ﬁts a Gamma density to
the positive portion of the response distribution. The results in the table are conditional on
clearing the hurdle. Each coecient should be viewed as the estimated e↵ect on a campaign
outcome given that the campaign has any detectable impact at all. Since we use a Bayesian
approach, the results take the form of probability distributions for each parameter. For the
26

Figure 6: Archetype Map
Notes: Light, ﬁlled dots are individual campaigns. Open dots are archetypes and size
indicates prevalence. “Legacy” refers to cinema, point-of-sale, outdoor, magazines,
radio. “Generic digital” refers to non-YouTube online video and non-Facebook online
display. “Algorithmic” refers to algorithmic targeting (e.g., Youtube and Facebook)
27

coecient tables in Table 5, we report the posterior means and 95% credible intervals.
Interpreting the coecients here is not as straightforward as in conventional linear re-
gression. As explained above, in order to model an outcome with a Gamma distribution, a
link function is necessary to bridge between the right-hand-side variables and the responses.
This is because the right-hand-side variables can often take negative values, which are not in
the support of the Gamma density. The link function we use is the natural logarithm. The
inverse link — the exponential in our case — is applied to the linear predictor ( xnn)t o
transform values into R+. For interpretation, we pass the coecients through the exponen-
tial function, which allows them to be interpreted as factors. Explicitly, a coecient x for
ar i g h t - h a n ds i d ev a r i a b l ex is interpreted as the factor by which the response is multiplied
given a 1 unit increase in x.I n s o m e c a s e s , t h i s w i l l c r e a t e a n i m p r e s s i o n o f u n r e a l i s t i c a l l y
large e↵ect sizes, but in interpretation it is important to note the intercept term, which
always applies. As will be evident, in each model the intercept balances out large coecients
on the covariates. With a typical regression coecient, where e↵ects are additive, zero (the
additive identity) indicates a null e↵ect. Here, e↵ects are multiplicative, so a null e↵ect is
one (the multiplicative identity). In Table 5 coecients have been exponentiated already, so
each number can be interpreted directly as a scaling factor.
Archetype membership probability coecients are relative to Archetype 2, the reference
level (which therefore has no coecient). Each coecient shown is the factor of improvement
over Archetype 2. Similarly, spend share coecients are relative to Online Video.
Starting in block (a) of Table 5, we have the results for Motivation. Archetype 4 has the
largest signiﬁcant coecient. However, the share of spend on cinema has a larger coecient,
and share spent on YouTube has a coecient nearly as large, on average. Also note that the
lower bound of the credible interval for Archetype 3 is higher than for 4. This suggests the
possibility that di↵erent channel selections come with di↵erent risk proﬁles, which highlights
ar e a l i t yw h e r et h ec o n c e p to f“ b e s ts t r a t e g y ”i sm o r en u a n c e d ,w i t ht h ep o t e n t i a lt oa tl e a s t
consider the risk appetite of brands. In fact, scanning across the four dependent variables in
28

Table 5, this relationship between Archetypes 3 and 4 holds in all but one case. Note that
concentration is not signiﬁcantly di↵erent from 1 (multiplicative identity) for Motivation.
Coecients for Association are in block (b). We see that again Archetype 4 has the largest
coecient among the archetypes, but four main e↵ects (spend shares) are at least as large:
cinema, YouTube, Newspapers, and point of sale (POS). Concentration has a signiﬁcant
coecient below 1, meaning more concentrated spend reduces lifts for Association. This
may be due to the fact that higher concentrations tend to be common among campaigns
which spend more on TV, outdoor, or other “legacy” media, whereas lower concentration
reﬂects experimentation and adoption of new channels. Heavy use of TV and other legacy
media may in turn constrain or dampen the ability for brands to create changes in association,
while on the other hand, more diverse and newer channels may a↵ord more variability in
exposure, new means of communication, as well as new signaling mechanisms. All conditions
and consequences that are consistent with Keller’s ( 1993)t h e o r ya n dp r a c t i c a li m p l i c a t i o n s ,
as well as some early empirical evidence on advertising variance ( Haugtvedt et al. 1994).
See coecients for Unaided Awareness in block (c). The largest archetype coecient is
for 4, but by a very small margin. If the reference class were changed from 2 to 5, it is likely
that Archetypes 3, 4, 5, and 7 would not be signiﬁcantly di↵erent from one another. For
Unaided Awareness, the coecients on Archetypes are generally larger than the coecients
on spend shares (with the exception of cinema). In fact, several of the share coecients are
below 1, with magazines having an especially low coecient.
Block (d) shows coecients for Aided Awareness. As shown in Table 1, Aided Awareness
has a lower average lift and a higher standard deviation than the others. Aided Awareness
also has more zeroes, consistent with a ceiling e↵ect for large brands ( Srinivasan, Vanhuele,
and Pauwels 2010). The larger variation and reduced signal in the Aided Awareness lift data
manifests in much larger credible intervals for the coecients. However, relative e↵ects still
reveal interpretable results, such as the fact that Archetype 4 and share of spend on cinema
have distinctly larger impacts on Aided Awareness than the other variables.
29

While the raw coecients are very informative, model simulations can show the e↵ects
of holistic changes to campaign structure, encompassing channel selection, spend shares,
and concentration. We show these holistic impacts in Figures 7 and 8.T h e x - a x i s o f e a c h
ﬁgure starts on the left with the posterior predictive median for a campaign of Archetype
2: membership probability of 1 for Archetype 2, and the average channel selection, spend,
and concentration of Archetype 2 campaigns in the data. Then we move the membership
probability, average spends, and average concentration values progressively toward di↵erent
clusters, and plot the predicted outcome. In Figure 7 we plot the median value of the pos-
terior predictive distribution, and for Figure 8 we plot the 2.75th percentile. The di↵erences
indicate that sometimes an approach optimized for a median result would not be the same
as more risk averse ‘maximin’ approach. For example, Archetype 4 delivers by far the best
median result on Aided Awareness, but by far the worst 2.75th percentile result — it is a
high risk, high reward campaign structure for Aided Awareness.
30

Figure 7: Archetype Outcome Proﬁles: Median
Figure 8: Archetype Outcome Proﬁles: 2.75th Percentiles
31

Table 5: Outcome Model Results
(a) Motivation (b) Association
Mean CI:L CI:U Mean CI:L CI:U
Intercept 0.01 0.01 0.02 0.01 0.01 0.02
Archetype 1 1.22 0.91 1.65 1.38 1.04 1.85
Archetype 3 1.99 1.56 2.60 1.83 1.45 2.34
Archetype 4 2.25 1.51 3.51 2.02 1.41 2.94
Archetype 5 1.74 1.25 2.49 1.68 1.22 2.31
Archetype 6 1.66 1.18 2.45 1.59 1.12 2.32
Archetype 7 1.65 1.05 2.60 1.45 0.99 2.14
Concentraton 0.95 0.80 1.13 0.68 0.58 0.81
Time Trend 1.02 1.00 1.05 1.00 0.98 1.03
Share: Cinema 3.34 2.78 4.04 6.05 4.98 7.33
Share: Facebook 1.33 1.12 1.58 1.68 1.42 2.01
Share: Magazines 0.69 0.57 0.83 0.60 0.49 0.72
Share: Newspapers 1.98 1.66 2.37 3.34 2.77 4.03
Share: Online Display 1.09 0.91 1.32 1.77 1.50 2.10
Share: Outdoor 0.65 0.55 0.78 0.77 0.64 0.92
Share: POS 1.09 0.90 1.32 2.02 1.68 2.43
Share: Radio 0.89 0.74 1.07 1.54 1.28 1.86
Share: TV 1.17 1.01 1.36 1.73 1.49 2.00
Share: Youtube 2.08 1.74 2.48 3.55 2.97 4.27
(c) Unaided Awareness (d) Aided Awareness
Mean CI:L CI:U Mean CI:L CI:U
Intercept 0.01 0.01 0.02 0.01 0.00 0.01
Archetype 1 1.12 0.67 1.82 0.68 0.39 1.20
Archetype 3 2.03 1.38 3.02 1.83 1.10 3.11
Archetype 4 2.10 1.19 3.77 10.30 4.51 27.22
Archetype 5 1.90 1.13 3.28 2.89 1.37 6.10
Archetype 6 1.76 0.97 3.33 1.23 0.65 2.38
Archetype 7 2.06 1.18 3.74 1.35 0.49 3.58
Concentraton 1.20 1.00 1.43 1.76 1.47 2.11
Time Trend 1.06 1.02 1.10 1.04 0.98 1.10
Share: Cinema 6.69 5.54 8.14 26.11 21.44 31.48
Share: Facebook 1.40 1.16 1.69 4.26 3.54 5.18
Share: Magazines 0.07 0.06 0.08 1.20 0.99 1.46
Share: Newspapers 1.74 1.44 2.12 2.59 2.14 3.14
Share: Online Display 0.79 0.66 0.96 0.88 0.73 1.06
Share: Outdoor 0.74 0.62 0.90 0.45 0.38 0.55
Share: POS 0.39 0.32 0.47 2.79 2.31 3.39
Share: Radio 0.81 0.66 0.98 1.81 1.50 2.20
Share: TV 1.07 0.90 1.26 1.74 1.47 2.07
Share: Youtube 1.59 1.31 1.93 6.98 5.78 8.41
Notes: CI:L is the 2.75th percentile and CI:U is the 97.5th percentile,
which together form the 95% credible interval.
32

To give a sense for how the b est archetyp e di↵ers by industry or category, we show in
Table 6 the best Archetype coecient when the model is estimated on subsamples of the data.
While some aggregation is necessary to maintain reasonably large sample sizes, we are able
to provide results for three mega-category subsamples: consumer packages goods (CPG),
services, as well as technology & durables. Notably, di↵erent categories have distinctly
di↵erent proﬁles. Archetype 6 is best for all four outcomes in CPG, but for none of the
outcomes in the other categories. Archetype 4, though best in the overall dataset, is only
best in one case (Unaided Awareness in the Services category) for the subsamples. Archetype
6 is notable for having a very high probability of combining TV, outdoor, and Facebook.
That this triple performs extremely well for CPG calls into question the common conceptual
division between traditional vs. digital media. It appears traditional and digital media can
be highly complementary .
Technology and Durables shows a clear division between awareness (“top of funnel”) and
motivation and association (“lower funnel”). Archetype 7, notably high in Facebook and
YouTube, unsurprisingly is associated with lower funnel metrics, while Archetype 5, which
is distinctly lower in YouTube and Facebook, associates with upper funnel awareness metrics.
Table 6: Archetypes with Highest Coecient by Industry
CPG Services Technology
&D u r a b l e s
Motivation 6 5 7
Association 6 5 7
Unaided Awareness 6 4 5
Aided Awareness 6 7 5
Notes. CPG: personal care, food and drink, household.
Services: ﬁnancial services, airlines, utilities, telecoms, leisure.
Technology & durables: automobiles, consumer electronics,
apparel, search, social media, ecommerce.
33

PRESCRIPTIVE RESULTS
The model can be used to simulate the impact of possible changes to marketing me-
dia planning. For each of the four dependent variables (Motivation, Association, Unaided
Awareness, and Aided Awareness) we consider the predicted impact of a change in the plan-
ning mix. The possible changes we consider all take the form of “acting like” a particular
archetype. In concrete terms, “acting like” an archetype means selecting channels with the
same probabilities as that archetype (i.e. to act like Archetype d,c h o o s ec h a n n e lc with
probability wcd), and then conditional on channels selected, allocate spend like the average
member of that archetype in the dataset.
To implement the simulation, we ﬁrst use the mo del estimates for channel usage proba-
bilities by archetype (shown in Table 4). We next compute the average spend in the dataset
by archetype, after each campaign is assigned to the likelihood for which it has highest
membership probability. The spend shares by archetype are shown in Table 7.
Table 7: Average Spend Shares by Archetype
Archetype ! 1234567
Share: Cinema .01 .01 .01 .03 .04 .01
Share: Magazines .06 .01 .02 .01 .03
Share: POS .02 .02 .02 .06 .04
Share: Newspapers .02 .01 .02 .13 .04 .01
Share: Radio .04 .02 .03 .02 .06 .03 .01
Share: Youtube .04 .10 .02
Share: Online Video .11 .03 .02 .08
Share: Facebook .11 .03 .06 .05 .02 .11 .07
Share: Online Display .01 .13 .08 .08 .06 .01
Share: Outdoor .05 .08 .35 .17 .23 .26
Share: TV .69 .62 .59 .38 .49 .53 .49
Notes: shares below 0.01 have been rounded to zero.
To generate a campaign proﬁle that approximates an archetyp e, we follow the steps
below. W e use S to stand for simulated quantities. Consider Archetype d:
34

1. Draw channel usage indicators. For each c,d r a wuS c from a Bernoulli distribution with
parameter ˆwcd, which is Archetype d’s estimated usage probability of channel c.
2. From mean sp end shares shown in Table 7 select values s⇤ c for channels where uS c =1 .
3. To ensure that the shares sum to one, normalize: sS c = s⇤ c / P c s⇤ c .
We then simulate from the posterior predictive distribution of the model to obtain ex-
pected lifts. We run the above steps for each archetype. Finally, we compare the expected
lifts to average observed lifts. Table 8 shows the expected lift, in absolute terms and as a
percentage improvement, for the best archetype for each outcome.
Table 8: Model Recommendations
Improvement
Outcome Best Archetype Channel to Upweight Absolute Percentage
Motivation 4 POS +.018 +83%
Association 3 YouTube +.025 +96%
Unaided Awareness 7 Online Video +.009 +52%
Aided Awareness 4 POS +.095 +750%
Notes: Absolute improvement is the mean simulated lift minus the mean observed lift in the dataset.
Percentage improvement is absolute improvement divided by mean observed lift in the dataset.
Channel to upweight is the channel which had the largest increase in probability of usage, as a
percent of average observed usage probabilities.
Given the large amounts of money to achieve lifts, these results appear to be extremely
economically meaningful. One note is in order about the improvement in Aided Awareness:
Figures 7 and 8 show that while Archetype 4 performs much better on average,i ta l s oc o m e s
with very large risk. There is also a very high likelihood of zero lifts in the data (see the
hurdle intercept in Table 5), which suggests a relatively lower amount of informative data
and thus noisier estimates, but also suggests a very low baseline level of Aided Awareness in
the dataset upon which to improve. Together these factors suggest that the improvement is
credible but should be interpreted with some caution and with proper context.
35

Rough Financial Impact Figures
Ad a t a s e tc o m p a r a b l et oo u r si nr i c h n e s sa n ds c o p e ,b u tw h i c ha l s oi n c l u d e sm e a s u r e m e n t s
of sales outcomes, is very unlikely to exist. Given the ability of this dataset to allow us to
answer questions on media usage and brand metric impact, the lack of ﬁnancial outcomes
seems a more-than-acceptable trade-o↵. However, despite lacking sales data linked to each
campaign, we can still produce some rough back-of-the-envelope estimates of ﬁnancial impact
from the prescriptions in Table 8 by relying on previous research. The best match for this
purpose is Srinivasan, Vanhuele, and Pauwels (2010), wherein the authors produce sales
elasticities with respect to mindset metrics similar to those in our data.
The metric from our dataset which best matches the metrics from Srinivasan, Vanhuele,
and Pauwels (2010)i sM o t i v a t i o n ,w h i c hi sac o m b i n a t i o no fc o n s i d e r a t i o n ,p u r c h a s ei n t e n t ,
and brand liking. The corresponding metrics reported in Srinivasan, Vanhuele, and Pauwels
(2010) are brand liking and consideration. We note that purchase intent was also in the
dataset in Srinivasan, Vanhuele, and Pauwels (2010)b u tw a sn o tu s e da c c o r d i n gt ot h a t
paper because it was so highly correlated with consideration. Our approach for the purposes
of this thought experiment are to use the elasticity of sales with respect to consideration
as a lower estimate and the the elasticity with respect to liking as a higher estimate. The
rationale is that our metric is some combination of the two things, and so the elasticity
would naturally fall somewhere between them. The reference unit we use is millions of
dollars, meaning our goal is to calculate the incremental revenue per $1M dollars of revenue
that could be expected by increasing Motivation by .018 (ﬁrst row of Table 8). Because the
results form Srinivasan, Vanhuele, and Pauwels (2010)a r ee l a s t i c i t i e s ,w en e e dt oa s s u m ea
starting level of Motivation. In our dataset, Motivation is measured on a scale between 0 and
1, as discussed, where 1 represents 100% of respondents giving answers indicating favorable
attitudes toward the brand. To produce rough ﬁgures for ﬁnancial impact then, we use
as e to fe q u a l l ys p a c e dg r i dp o i n t sb e t w e e n0 . 1a n d0 . 9 ,w h i c hr e p r e s e n td i ↵ e r e n ts t a r t i n g
levels of Motivation. For each grid point, we use the following formula to get estimates for
36

25000
50000
75000
100000
0.25 0.50 0.75
Base Value
Incremental Revenue per $1M
Lower
Upper
Figure 9: Financial Impact through Motivation
incremental revenue on $1M ( R):
R = " ⇥ 0.018 ⇥ 1,000,000 grid point , (10)
where " is a cumulative elasticity ﬁgure from Srinivasan, Vanhuele, and Pauwels (2010)
(either 0.374 if associated with consideration for the lower estimate, or 0.59 if associated
with liking, for the upper estimate). Figure 9 shows the results. Elasticity naturally cap-
tures diminishing returns: if Motivation levels are very low, the incremental impact is much
larger than if Motivation levels are already very high. The highest estimated impact is
approximately $100,000 additional dollars per $1M in current revenue, and the lowest is
approximately $7,500. Adopting a particular media selection archetype does not require
changing spend levels but only re-allocating spend, which means that even if realized incre-
mental revenue were on the very low end of this range, the intervention would be worthwhile.
Pairwise Interaction Models
To help see why modeling channel complementarity is useful, as well as to understand
the beneﬁt of using Latent Class as a ﬁrst stage, we can compare our results to the most
common alternative: pairwise e↵ects, without applying Latent Class ﬁrst.The results for our
37

data are shown in Web Appendix D.
Pairwise interaction models for planning ten channels show 56 rows of data, including
estimates of interaction terms. However, this output has severe limitations. First, the
coecients are mostly untrustworthy due to the number of parameters relative to the number
of data points. Second, there is no principled way to determine which, if any, coecients to
focus attention on for managerial insights. Third, even accepting the complications arising
from this model, it still only captures pairwise interactions. Lastly, by construction, this
model collapses the channel selection problem into either a narrower cross-e↵ects individual
eciency construct, or a coarser and less informative ”synergy” construct (and all channels in
the ’on’ position); risking an analysis that optimizes to individual channel e↵ectiveness rather
than campaign level outcome. Altogether, this comparison demonstrates why our approach
is more statistically and practically tractable and valid. More signiﬁcantly, the comparisons
show that our approach is both uniquely able to address the conceptual question of channel
selection and complementarity, while also being more insightful to managers.
MOVING IMC FROM CONCEPT TO THEORY
While not testing a speciﬁc theory, our results are very useful in context of the general
propositions we introduced earlier, and in protecting the original constructs inside of the IMC
concept. Furthermore we see our results as a motivation for a more comprehensive theory of
marketing integrated communications that provides testable hypotheses, predictive power,
and valuable mechanic explanation for the behavior and interplay of media.
First, we were able to identify and demonstrate the existence of a signiﬁcant and prob-
lematic managerial lay theory. Consistent with broad managerial guidance, we ﬁnd that
managers seek to optimize the reach of their campaigns, or in other words, they seek to
maximize the size and exposure of the audience (given their brand targeting parameters).
Furthermore, the argument arising from this theory is that audience reach, and this signiﬁ-
cant exposure is sucient, such that all other outcomes for the brand should naturally arise
38

(reach eciency leading to awareness, consideration and ultimately purchase). To be clear,
by construction, this lay theory posits that all channels are undi↵erentiated outside of their
audience composition and ability to deliver against this audience.
However, we ﬁnd the opposite outcome with regards to brand consequences, and this
optimization in reach does not at all translate into optimized brand outcomes. Therefore,
we can point to a (at minimum) 2-dimensional heterogeneity of channels: (1) audience
composition, and the channel’s ability to deliver messages to this audience, and (2) a channel
speciﬁc functional advantage, e↵ect, or impact it has on its audience that arises from the
channel itself and not from creative or content choices.
Secondly, we ﬁnd that di↵erent brand outcome goals (Aided Awareness, Unaided Aware-
ness, Association, and Motivation) yield di↵erent best archetypes, or combinations of se-
lected channels. This highlights that not only does the functional-level heterogeneity exist,
but that channel function carries di↵erent relevance or value for di↵erent goals. And, as this
di↵erential combinatorial value of channels by outcome is the suggested required element of
complementarity, we ﬁnd that our results are a strong indication that complementarity is
an important and separate construct, which should be maintained as separate component
inside of the IMC concept.
What is complementarity, and how might it arise? For exposition, let’s consider a stylized
construction of a single objective, such as brand salience. We can then imagine that building
salience requires two sub-processes. We can leave them unnamed and assume they are latent,
but maintain that they are distinct and necessary components of creating salience. In this
stylized discrete world, let’s assume that radio advertising acts on sub-process 1 exclusively,
while television and outdoor advertising both act on sub-process 2 alone. If this were the
case, radio and television would be complementary investments. This tiny campaign with
two channels would address each sub-process of salience, and together they would perfectly
make up for each others’ deﬁciency (no channel handles all sub-processes alone). Similarly,
and alternatively, radio and outdoor would also form complementary investments, with radio
39

handling sub-process 1 and outdoor handling sub-process 2. However, television and outdoor
are not complementary channels with respect to salience, as each would be acting on sub-
process 2, and this campaign construction would leave sub-process 1 devoid of activity.
Complementarity deals directly with the question of which channels should be used, based
on their function with respect to an objective.
What then of cross-e↵ects? Still in our stylized world described above, both radio+television
and radio+outdoor represent complementary selections. However, we might imagine that
—f o rw h a t e v e rr e a s o n—t h ej o i n tp r e s e n c eo ft e l e v i s i o na d sa c t u a l l yi m p r o v e st h ee ↵ e c -
tiveness with which radio acts on sub-process 1. Alternatively, we might imagine that the
combination with outdoor actually harms the e↵ectiveness of radio acting on its own sepa-
rate sub-process. These positive or negative e↵ectiveness gains are the channel cross-e↵ect.
They do not alter where the channel is active, but the strength with which it acts. As such,
cross-e↵ects will impact spend, inasmuch as we can reduce spend given gains in e↵ectiveness
and eciency due to a supporting channel, or we can compensate from loss of eciency from
a negative cross-e↵ect by pumping ever more money into a channel. But, there is not any
amount of investment that will cause a channel to switch functionality and create comple-
mentarity. These are likely an emergent characteristic from channel design interacting with
consumer utilization behaviors and patterns.
Therefore, complementarity addresses the channel selection problem, while cross-e↵ects,
on its own, provides an understanding of the e↵ectiveness of a channel in the context of
a group of channels working together. This is not to undermine the value of cross-e↵ects
within the IMC concept, but rather to ﬂag the importance for all constructs, and the need
to understand where and how they act.
Further towards our understanding of marketing integration, we identify a fascinating
boundary condition in product category. As noted before, of the three IMC constructs, one
(consistency) exists at a content level, while the other two (complementarity and cross e↵ects)
exist at the channel level. However, we were able to identify one product category (CPG)
40

where complementarity —- a channel level e↵ect –– collapses and a singular combinatorial
archetype becomes a dominant strategy (archetype 6), regardless of brand advertising goal.
Critically, this points towards important and nuanced considerations when explaining the
interaction of media strategies, brand contexts, and brand goals, particularly given desires
to simplify the IMC concept. Whereas, given the explosion of media options and the crit-
ical dynamic multi-dimensionality of media value (audience, function and interactions), we
might instead beneﬁt from an opposite move towards a homegrown IMC theory, providing a
complete set and deﬁned constructs, their compositions, relational structure and applicable
boundary conditions. Ultimately, this shift would yield us much great explanatory and pre-
dictive power for the complex media environment, as well as a course-correction and better
guidance for practice.
DISCUSSION
Our study demonstrates that there is a signiﬁcant value in considering the complementar-
ity of media channels in campaigns, beyond pairwise interactions. The analysis takes some
initial steps in safeguarding the necessity of complementarity inside IMC theory and litera-
ture and in answering the call by Batra and Keller (2016)f o rb e t t e rm a n a g e r i a lg u i d a n c eo n
the usage and combination of media channels.
One major implication is that there is no universal silver-bullet campaign strategy. Across
all campaign archetypes identiﬁed and possible outcomes, no single combination of channels
o↵ers the best possible result. We show that the concept of “best” can even di↵er by risk
appetite, such that some might aim for highest average outcome lifts, while others might
prefer a more conservative lower downside risk option. Di↵erent campaign goals and industry
contexts require di↵erent media combinations.
That does not mean all channel combinations have a ‘best’ purpose. While we ﬁnd no
dominant strategies, we do ﬁnd dominated ones. Archetype 2 (i.e., “Generic Digital”) might
serve as the best example. As a reminder, this archetype combines TV with online video
41

and display, likely pointing to a common practice of replicating the TV asset on online video
and banners/display. Despite being the observed format of 23% of campaigns, it essentially
never o↵ers best performance, regardless of campaign goal, outperforming only Archetype 1
for Aided Awareness (but losing to 3, 4 and 5).
The complementarity of channels in this study raises another important consideration.
Channels do in fact have channel-speciﬁc strengths and weaknesses that are mostly invisible
if we are restricted to the consideration of a singular outcome or dimension of channel
performance. This means there are reasons to use (or not use) a channel beyond reach,
impressions, or frequency. The coverage of a target market (audience composition) is not the
only contribution of a channel. One might excel in awareness, while others drive motivation.
Channels are not perfectly fungible, and mangers should consider the unique individual
functionality of channels relative to other available channels, along with the potential for
complementarity in the media plan. The implication is that the value of a media channel is
not a function of simple supply constraints (i.e., “how many views can I buy?”), but also of
the channel’s positioning and di↵erentiation (i.e., “what do I accomplish with a view?”)
We demonstrate the imp ortance of considering higher-order (i.e., more than pairwise)
relationships in media planning and in research. Archetype 6 (Television + Facebook +
Outdoor) provides a good example, as the performance of any sub-component dyad su↵ers
by the removal of the third component. Despite comprising only 8% of our observed cam-
paigns, this archetype is the closest to a silver-bullet, o↵ering the best outcomes regardless
of campaign goal, provided the brand was in the CPG category. However, for all other
categories, archetype 6 was never ideal. These results highlight that the division between
traditional and digital channels may be a false dichotomy. While practice and academia
might usually consider these to be in opposition, or two separate but internally cohesive
groups ( Naik and Peters 2009), the reality appears to be more nuanced and consideration
should be given to the functional complementarity of channels regardless of their catego-
rization. Again, the triad of TV, Facebook, and outdoor as a high performance strategy
42

necessitates the use of billboards; hardly ﬁtting with the narrative that advertising might be
strictly a digital focus in the future.
Table 8 highlights goal speciﬁc characteristics. Across awareness (aided or unaided),
association, and motivation, there are a variety of archetypes to follow, channels to invest in,
and a range of resulting improvements. This indicates that there are natural di↵erences in
our ability to inﬂuence di↵erent aspects of the brand, or to comparatively call the customer
to action successfully, which further reinforces the need to respect channel heterogeneity.
Implications for Practice
The present study provides new insights for practitioners who are concerned with mul-
timedia campaign construction, demonstrable advertising e↵ectiveness, and the balance be-
tween long-term brand building versus short term consumer activation ( Binet and Field
2013). We begin by showing common patterns in campaign structures via the Latent Class
approach, as shown in Table 4.C u r r e n t i n d u s t r y d i s c u s s i o n o n m e d i a s e l e c t i o n c e n t e r s o n
the immediate and growing investment in digital channels, which carries the risk of inﬂat-
ing expectations of digital channel performance and applicability. This increases the risk of
over-indexing on these channels as Adidas claims to have done in late 2019 ( Vizzard 2019).
We then provide a view on how some of the largest global brands have executed their cam-
paigns, providing a counterweight to that discussion and a reference based in recent historical
evidence where traditional channels are still very much an important feature of integrated
campaign design.
We show that the GRP-only paradigm of media selection and purchase is problematic in
that it reduces media plan construction down to a too-simple market coverage problem. If the
GRP-only hypothesis were true, we would be able to identify one single campaign structure
to dominate all others (i.e. the combination of channels providing the single largest possible
market coverage). This practice is unfortunately an increasingly dominant unspoken strategy
for media planners and reinforced by the pricing structure of channels, as they are presented
43

on the basis of GRPs, impressions, or opportunities to view, depending on the context. This
is a supply dominant logic for platforms and channels that ignores the needs and motivations
of brand owners. One might ask, for example, why buy into cinema advertising when I can
have more impressions on Facebook? The answer is: because they are functionally di↵erent,
and a cinema exposure will elicit a di↵erent response when compared to a Facebook exposure.
The reality of the dominance of reach-buying is clear from Table 2,a si st h ee x t e n to fp o t e n t i a l
for improvement on lifts.
The ease of falling into this framing of advertising is fairly straightforward to show if
we consider the discussion around the health of channels. For example, in popular and
industry press, Facebook has historically been evaluated primarily by the number of users and
their demographics. As another example, the US bill to ban TikTok elicited an immediate
advertiser discussion on diversifying media portfolios in order to reach heavy TikTok users
(Barnett 2024). In these and most other instances, the question of media allocation is
reduced to audience construction and eciency of reach, but the functional beneﬁt of a
channel-speciﬁc exposure is never addressed. As we have shown, there is a signiﬁcant amount
of additional advertising power available to brands if they consider channel function as well
as audience.
Furthermore, we provide speciﬁc guidance on channel performance and channel comple-
mentarity for four possible brand campaign goals: Unaided Awareness, Aided Awareness,
brand Association, and Motivation. This is particularly important, as our data shows that
even among the largest ﬁrms and brands present in our dataset, a number of campaigns
are deploying strictly worse-performing combinations of channels. Instead, by following the
goal-speciﬁc structures shown in our study, brands should be able to realize both greater
and more consistent campaign lifts across the whole range of the purchasing funnel.
44

Implications for Research
This work provides a number of contributions to the literature on advertising and in-
tegrated marketing communications. First, by leveraging the largest and broadest view to
date on campaign e↵ectiveness, we produce evidence of channel-speciﬁc, as well as structure
and goal dependent campaign e↵ectiveness. We provide an initial empirical response to Ba-
tra and Keller (2016), based on the meta-analytic view of over one thousand campaign lift
studies.
Our approach can also serve as a foundation for researchers to operationalize high level
constructs in IMC. Simultaneously, via better measurement and utilization of all high-level
IMC constructs, we were able to generate predictions on advertising campaign construction
and outcomes. However, this opportunity opens a set of valid questions around the nature
of channel complementarity itself, designed-for versus emergent characteristics, dynamic as
well as competitive contexts, and beyond. There is a need to connect micro (consumer level,
processing) e↵ects to macro (channel and ﬁrm level, econometric) e↵ects ( Batra and Keller
2016). As such, this study might be an impetus and the ﬁrst step in transitioning IMC from
a concept towards a formalized and structured theory, which would enable an increasingly
cogent set of future analyses on the nature of media evolution and utilization, including
cross-country variation and deeper competitive analysis.
Our results point to functional heterogeneity in channels, beyond audience composition
and size. Not only does this bring to question the strict digital versus traditional media
split we’ve already discussed, but also highlights a signiﬁcant risk by researchers assuming
that all channels within a single domain are equivalent. For example, collapsing a variety
of channels into a collective “Social Media” label should be done cautiously, as it would
imply that Facebook, Twitter, Instagram, Snapchat, TikTok, and beyond are functionally
equivalent. In broadest terms, our results suggest that assumption is wrong.
Relatedly, by showing that media channels are indeed functionally heterogeneous, an
immediate set of questions arise around the identiﬁcation of divergent functions, as well as the
45

causes for these di↵erences. And while we cannot exhaustively provide channel functionality
categorization here, we do propose that these di↵erences should arise from an interplay of
channel design (e.g. feed construction, velocity of content delivery, aspect ratio, etc.) and
user behavior (e.g. navigation, rationale for use, usage occasion). Future research should be
able to address precise channel function attribution, sharpening advice to advertisers as well
as channel owners.
Lastly, we shed light on the under-researched area of brand-building (Unaided Awareness,
Aided Awareness, Brand Association, and Motivation). While the call for sales as a critical
outcome variable ( Sethuraman, Tellis, and Briesch 2011)h a sb e e nt h o r o u g h l ya c c e p t e d( s e e
Table W.F.1 in Web Appendix F for sales focused studies), the exclusive dedication to sales
leaves a signiﬁcant gap in understanding brand building. This work helps to ﬁll this gap,
and supports the view that campaign e↵ectiveness is best served by considering both the
short and long-term horizon.
Note that while our analysis covers many channels, it is not exhaustive. Due to lack of
data, we are missing search advertising and some new and popular additions (e.g. TikTok).
This means caution is warranted when it comes to making precise recommendations sug-
gested from this study. Instead, we focus on the larger, more general ﬁndings, such as the
fact that no single plan is best for all outcomes and contexts. These insights will almost
certainly remain relevant with the addition of more channels, since the answers will grow
more complex, not simpler. Furthermore, businesses can likely improve ROI at a broader
level by examining their historical media mix data and moving toward archetypes that are
better for their contexts and goals.
46

REFERENCES
Barnett, Kendra “Advertisers on alert as bill to ban TikTok or force divestment advances in
US House,” https://www.thedrum.com/news/2024/03/07/advertisers-alert-bill-ban-
tiktok-or-force-divestment-advances-us-house (2024).
Batra, Rajeev and Kevin Lane Keller (2016), “Integrating marketing communications: New ﬁnd-
ings, new lessons, and new ideas,” Journal of Marketing , 80 (6), 122–145.
Berman, Ron (2018), “Beyond the last touch: Attribution in online advertising,” Marketing
Science, 37 (5), 771–792.
Betancourt, Michael “Identifying Bayesian Mixture Models,” (2017) https://mc-stan.org/
users/documentation/case-studies/identifying mixture models.html.
Binet, Les and Peter Field (2013), The Long and the Short of It: Balancing Short and Long-Term
Marketing Strategies Institute of Practitioners in Advertising.
Borden, Neil H (1964), “The concept of the marketing mix,” Journal of advertising research , 4 (2),
2–7.
Carpenter, Bob, Andrew Gelman, Matthew D Ho↵man, Daniel Lee, Ben Goodrich, Michael Be-
tancourt, Marcus Brubaker, Jiqiang Guo, Peter Li, and Allen Riddell (2017), “Stan: A
probabilistic programming language,” Journal of statistical software , 76 (1).
Chang, Yuhmiin and Esther Thorson (2004), “Television and web advertising synergies,” Journal
of advertising , 33 (2), 75–84.
Culliton, James William et al. (1948), Management of marketing costs Division of Research,
Graduate School of Business Administration, Harvard Univ.
Danaher, Peter J and Tracey S Dagger (2013), “Comparing the relative e↵ectiveness of advertising
channels: A case study of a multimedia blitz campaign,” Journal of Marketing Research ,
50 (4), 517–534.
Danaher, Peter J, Tracey S Danaher, Michael Stanley Smith, and Ruben Loaiza-Maya (2020),
“Advertising e↵ectiveness for multiple retailer-brands in a multimedia and multichannel envi-
ronment,” Journal of Marketing Research , 57 (3), 445–467.
Deighton, John (1996), Features of good integration: two cases and some generalizations Hillsdale,
NJ: Erlbaum.
Dijkstra, Majorie, Heidi EJJM Buijtels, and W Fred Van Raaij (2005), “Separate and joint e↵ects
of medium type on consumer responses: a comparison of television, print, and the Internet,”
Journal of Business Research , 58 (3), 377–386.
Duncan, Tom and Sandra E Moriarty (1998), “A communication-based marketing model for man-
aging relationships,” Journal of marketing , 62 (2), 1–13.
Edell, Julie A and Kevin Lane Keller (1989), “The information processing of coordinated media
campaigns,” Journal of Marketing Research , 26 (2), 149–163.
Fischer, Marc (2019), “Practice Prize Paper–Managing Advertising Campaigns for New Product
Launches: An Application at Mercedes-Benz,” Marketing Science , 38 (2), 343–359.
Fischer, Marc, S¨ onke Albers, Nils Wagner, and Monika Frie (2011), “Practice prize win-
ner—dynamic marketing budget allocation across countries, products, and marketing activi-
ties,” Marketing Science , 30 (4), 568–585.
Fossen, Beth L and David A Schweidel (2019), “Social TV, advertising, and sales: Are social shows
good for advertisers?,” Marketing science , 38 (2), 274–295.
47

Gatignon, Hubert and Dominique M Hanssens (1987), “Modeling marketing interactions with
application to salesforce e↵ectiveness,” Journal of Marketing Research , 24 (3), 247–257.
Gopalakrishna, Srinath and Rabikar Chatterjee (1992), “A communications response model for a
mature industrial product: Application and implications,” Journal of Marketing Research ,
29 (2), 189–200.
Haugtvedt, Curtis P., David W. Schumann, Wendy L. Schneier, and Wendy L. Warren (1994),
“Advertising Repetition and Variation Strategies: Implications for Understanding Attitude
Strength,” Journal of Consumer Research , 21 (1), 176–189.
Ho↵man, Matthew D and Andrew Gelman (2014), “The No-U-Turn sampler: adaptively setting
path lengths in Hamiltonian Monte Carlo.,” J. Mach. Learn. Res. , 15 (1), 1593–1623.
Houston, Franklin S (1986), “The marketing concept: what it is and what it is not,” Journal of
marketing, 50 (2), 81–87.
IMARC “Radio Advertising Market: Global Industry Trends, Share, Size, Growth, Opportu-
nity and Forecast 2023-2028,” (2023) https://www.imarcgroup.com/radio-advertising-
market.
Inc., Alphabet “Form 10-k 2022,” (2022) https://www.sec.gov/Archives/edgar/data/1652044/
000165204423000016/goog-20221231.htm.
Joo, Mingyu, Kenneth C Wilbur, Bo Cowgill, and Yi Zhu (2014), “Television advertising and
online search,” Management Science , 60 (1), 56–73.
Keller, Kevin Lane (1993), “Conceptualizing, measuring, and managing customer-based brand
equity,” Journal of marketing , 57 (1), 1–22.
Kolsarici, Ceren and Demetrios Vakratsas (2018), “Synergistic, antagonistic, and asymmetric media
interactions,” Journal of Advertising , 47 (3), 282–300.
Krasnikov, Alexander, Satish Jayachandran, and V. Kumar (2009), “The Impact of Customer
Relationship Management Implementation on Cost and Proﬁt Eciencies: Evidence from the
U.S. Commercial Banking Industry,” Journal of Marketing , 73, 61–76.
Linzer, Drew A. and Je↵rey B. Lewis (2011), “poLCA: An R Package for Polytomous Vari-
able Latent Class Analysis,” Journal of Statistical Software , 42 (10), 1–29 https://
www.jstatsoft.org/v42/i10/.
MarketWatch “Outdoor Advertising Market Size 2023 with Regional Scope, Report Coverage,
Historic Data and Outlook 2030,” (2023) https://www.marketwatch.com/press-release/
outdoor-advertising-market-size-2023-with-regional-scope-report-coverage-
historic-data-and-outlook-2030-2023-06-06 .
McAlister, Leigh, Raji Srinivasan, Niket Jindal, and Albert A Cannella (2016), “Advertising
e↵ectiveness: the moderating e↵ect of ﬁrm strategy,” Journal of Marketing Research , 53 (2),
207–224.
Naik, Prasad A and Kay Peters (2009), “A hierarchical marketing communications model of online
and o✏ine media synergies,” Journal of Interactive Marketing , 23 (4), 288–299.
Naik, Prasad A and Kalyan Raman (2003), “Understanding the impact of synergy in multimedia
communications,” Journal of marketing research , 40 (4), 375–388.
Schweidel, David A and Wendy W Moe (2014), “Listening in on social media: A joint model of
sentiment and venue format choice,” Journal of marketing research , 51 (4), 387–402.
Sethuraman, Raj, Gerard J Tellis, and Richard A Briesch (2011), “How well does advertising work?
Generalizations from meta-analysis of brand advertising elasticities,” Journal of Marketing
Research, 48 (3), 457–471.
48

Srinivasan, Shuba, Oliver J Rutz, and Koen Pauwels (2016), “Paths to and o↵ purchase: quantifying
the impact of traditional marketing and online consumer activity,” Journal of the Academy
of Marketing Science , 44 (4), 440–453.
Srinivasan, Shuba, Marc Vanhuele, and Koen Pauwels (2010), “Mind-set metrics in market response
models: An integrative approach,” Journal of Marketing Research , 47 (4), 672–684.
Statista “Advertising - Worldwide,” (2024) https://www.statista.com/outlook/amo/
advertising/worldwide.
Stephen, Andrew T and Je↵ Galak (2012), “The e↵ects of traditional and social earned media on
sales: A study of a microlending marketplace,” Journal of marketing research , 49 (5), 624–639.
Tobitt, Charlotte “Print ad revenue halves in six years as three tech giants make USD400bn
annually,” (2023) https://pressgazette.co.uk/marketing/global-print-advertising-
market-halves-in-six-years-but-publishers-struggling-to-compete-with-online-
oligopoly/.
Tuckman, Howard P and Cyril F Chang (1991), “A methodology for measuring the ﬁnancial
vulnerability of charitable nonproﬁt organizations,” Nonproﬁt and voluntary sector quarterly ,
20 (4), 445–460.
Vakratsas, Demetrios and Tim Ambler (1999), “How Advertising Works: What Do We Really
Know?,” Journal of Marketing , 63, 26–43.
Vehtari, Aki, Andrew Gelman, and Jonah Gabry (2017), “Practical Bayesian model evaluation
using leave-one-out cross-validation and W AIC,” Statistics and computing , 27, 1413–1432.
Vehtari, Aki, Daniel Simpson, Andrew Gelman, Yuling Yao, and Jonah Gabry (2022), “Pareto
smoothed importance sampling,” arXiv preprint arXiv:1507.02646 .
Venkatesan, Rajkumar and Vita Kumar (2004), “A customer lifetime value framework for customer
selection and resource allocation strategy,” Journal of marketing , 68 (4), 106–125.
Vizzard, Sarah “Adidas: We over-invested in digital advertising,” https://
www.marketingweek.com/adidas-marketing-effectiveness (2019).
Wedel, Michel and PK Kannan (2016), “Marketing analytics for data-rich environments,” Journal
of Marketing , 80 (6), 97–121.
49

The E↵ects of Advertising Media Channel Combinations
on Brand Performance
WEB APPENDIX TABLE OF CONTENTS
Web Appendix A: Priors 2
Web Appendix B: Estimation Code 4
Web Appendix C: Selecting the Number of Archetypes 10
Web Appendix D: Pairwise Interaction Results 11
Web Appendix E: Variations and Additional Results 15
Web Appendix F: Literature Review Table 18

WEB APPENDIX A: PRIORS
Latent Class Priors
As discussed, to avoid label switching, we use non-exchangeable priors by centering pa-
rameter prior distributions around point estimates from poLCA (Linzer and Lewis 2011). For
⌫ and W ,w i t hp o i n te s t i m a t e sf r o mpoLCA denoted by ⌫EM and W EM we use the following
priors:
⌫c ⇠N (⌫c,EM , 0.1)
wcd ⇠N (wcd,EM , 0.1) (W.A.1)
Trial and error (approximately 30 separate mo del runs) revealed that a standard deviation
of 0.1 is needed to avoid the prior being overwhelmed by label switching and failing to
converge. Recall that each ⌫c and wcd is a probability, so 0.1 is not as tight a prior as it
may appear. With this prior speciﬁcation, chains converge, with most ˆR values ( Vehtari
et al. 2021)a to rb e l o w1 . 0 1 . T h e s ep r i o r sa r eu s e di nt h es t a n d a l o n eL a t e n tC l a s sa n dt h e
integrated model.
Gamma Hurdle Priors
The priors for the hierarchical intercepts are given in the main text. The remaining
prior speciﬁcations are given here. In the integrated model, the 6 archetype membership
probability coecients {1,. . . ,6} have Normal priors centered at the posterior medians of
the standalone Gamma regression.
k ⇠ N (k,BRM , 5),k 2{ 1,. . . ,6} (W.A.2)
In the joint model the 12 slope coecients on control variables have similar priors but
they are much tighter since they do not relate to the Latent Class model:
i ⇠ N (i,BRM , 0.1),i 2{ 1,. . . ,12} (W.A.3)
In the standalone regression, rather than 0.1, for the standard deviation, 5 is used. The
priors on the brand and category constant distribution standard deviations have half Student
tp r i o r s
,a ⇠ t+(3, 0, 2.5)
,a ⇠ t+(3, 0, 2.5)
,j ⇠ t+(3, 0, 2.5)
(W.A.4)
2

The base intercept 0 has a Student t prior:
0 ⇠ t(3, 4, 2.5) (W.A.5)
In the standalone regression the shape parameter  for the Gamma distribution has itself
aG a m m ap r i o r
 ⇠ (0.1, 0.1) (W.A.6)
In the joint model the prior is changed to (10 ⇥ BRM , 10). Finally, in both the stan-
dalone and joint models the base intercept for the hurlde component has a standard Logistic
(see Stockute, Veaux, and Johnson 2013)p r i o r :
0 ⇠ Logistic(0, 1) (W.A.7)
3

WEB APPENDIX B: ESTIMATION CODE
We include here the Stan code for the Latent Class model and the Gamma hurdle regres-
sion, as well as the joint model. We do not include the R code used to compile and run the
Stan code since it is system-speciﬁc and will be of no value to knowledgeable Stan users.
Latent Class Stan Code
The following Stan code estimates the Latent Class model.
data {
int <lower=1> K;
int <lower=1> N;
matrix[N, K] X;
int <lower=1> D;
vector[D] nu_EM; // from poLCA , to avoid label switching
matrix[K, D] probs_EM; // from poLCA , to avoid label switching
}
parameters {
simplex[D] nu;
real <lower=0, upper=1> probs[K, D];
}
transformed parameters {
matrix[K, D] log_prob;
for (d in 1:D) {
log_prob[, d] = log(to_vector(probs[ , d]));
}
}
model{
// Priors
for (d in 1:D) {
nu[d] ~ normal(nu_EM[d], 0.1);
for (k in 1:K) {
probs[k, d] ~ normal(probs_EM[k, d], 0.1);
}
}
{
for (n in 1:N) {
row_vector[D] ps = log(nu’) + X[n] * log_prob +
(1 - X[n]) * log1m_exp(log_prob) ;
target += log_sum_exp(ps);
}
}
}
generated quantities {
vector[N] log_lik;
matrix[N, D] pred_class;
vector[N] pred_class_dis;
4

for (n in 1:N) {
row_vector[D] ps = log(nu’) + X[n] * log_prob +
(1 - X[n]) * log1m_exp(log_prob);
log_lik[n] = log_sum_exp(ps);
pred_class[n, ] = exp(ps - log_lik[n]);
pred_class_dis[n] = categorical_rng(pred_class[n, ]’);
}
}
Gamma hurdle
The code for running the Gamma hurdle with random e↵ects by category and brand is
below. The ﬁrst and third sets of grouping variables ( N 1, M 1, J 1, N 3, M 3, J 3)r e l a t e
to the category, and the second set ( N 2, M 2, J 2)r e l a t e st ob r a n d .
functions {
real hurdle_gamma_logit_lpdf(real y, real alpha , real beta , real hu) {
if (y == 0) {
return bernoulli_logit_lpmf(1 | hu);
}e l s e{
return bernoulli_logit_lpmf(0 | hu) + gamma_lpdf(y | alpha , beta);
}
}
}
data {
int <lower=1> N;
vector[N] Y;
int <lower=1> K;
matrix[N, K] X;
int <lower=1> N_1;
int <lower=1> M_1;
array[N] int<lower=1> J_1;
int <lower=1> N_2;
int <lower=1> M_2;
array[N] int<lower=1> J_2;
int <lower=1> N_3;
int <lower=1> M_3;
array[N] int<lower=1> J_3;
}
transformed data {
int Kc = K - 1;
matrix[N, Kc] Xc;
vector[Kc] means_X;
for (i in 2 : K) {
means_X[i - 1] = mean(X[ : , i]);
Xc[ : , i - 1] = X[ : , i] - means_X[i - 1];
}
}
5

parameters {
vector[Kc] b;
real Intercept;
real <lower=0> shape;
real Intercept_hu;
vector <lower=0>[M_1] sd_1;
array[M_1] vector[N_1] z_1;
vector <lower=0>[M_2] sd_2;
array[M_2] vector[N_2] z_2;
vector <lower=0>[M_3] sd_3;
array[M_3] vector[N_3] z_3;
}
transformed parameters {
vector[N_1] r_1_1;
vector[N_2] r_2_1;
vector[N_3] r_3_hu_1;
real lprior = 0;
r_1_1 = sd_1[1] * z_1[1];
r_2_1 = sd_2[1] * z_2[1];
r_3_hu_1 = sd_3[1] * z_3[1];
lprior += normal_lpdf(b | 0, 5);
lprior += normal_lpdf(b_controls | 0, 5);
lprior += student_t_lpdf(Intercept | 3, -3.9, 2.5);
lprior += gamma_lpdf(shape | 0.01, 0.01);
lprior += logistic_lpdf(Intercept_hu | 0, 1);
lprior += student_t_lpdf(sd_1 | 3, 0, 2.5)
-1*s t u d e n t _ t _ l c c d f ( 0|3 ,0 ,2 . 5 ) ;
lprior += student_t_lpdf(sd_2 | 3, 0, 2.5)
-1*s t u d e n t _ t _ l c c d f ( 0|3 ,0 ,2 . 5 ) ;
lprior += student_t_lpdf(sd_3 | 3, 0, 2.5)
-1*s t u d e n t _ t _ l c c d f ( 0|3 ,0 ,2 . 5 ) ;
}
model {
vector[N] mu = rep_vector(0.0, N);
vector[N] hu = rep_vector(0.0, N);
mu += Intercept + Xc * b;
hu += Intercept_hu;
for (n in 1 : N) {
mu[n] += r_1_1[J_1[n]] + r_2_1[J_2[n]];
}
for (n in 1 : N) {
// add more terms to the linear predictor
hu[n] += r_3_hu_1[J_3[n]];
}
mu = exp(mu);
for (n in 1 : N) {
target += hurdle_gamma_logit_lpdf(Y[n] | shape , shape / mu[n], hu[n]);
6

}
target += lprior;
target += std_normal_lpdf(z_1[1]);
target += std_normal_lpdf(z_2[1]);
target += std_normal_lpdf(z_3[1]);
}
generated quantities {
real b_Intercept = Intercept - dot_product(means_X , b);
real b_hu_Intercept = Intercept_hu;
}
Joint Latent Class and Gamma Hurdle Model
The Stan code below uses nu EM, probs EM to avoid label switching, and b BRM, b controls BRM,
shape BRM as informative priors on the coecients, where b BRM is weakly informative and
b controls BRM and shape BRM are more strongly informative, as they are unrelated to the
Latent Class model and so should be very close to the standalone Gamma hurdle regression
results.
functions {
real hurdle_gamma_logit_lpdf(real y, real alpha , real beta , real hu) {
if (y == 0) {
return bernoulli_logit_lpmf(1 | hu);
}e l s e{
return bernoulli_logit_lpmf(0 | hu) +
gamma_lpdf(y | alpha , beta);
}
}
}
data {
int <lower=1> N;
vector[N] Y;
int <lower=1> D;
int <lower=1> K;
int <lower=1> Kc;
vector[D] nu_EM;
matrix[K, D] probs_EM;
vector[D - 1] b_BRM;
vector[Kc] b_controls_BRM;
real shape_BRM;
matrix[N, K] X_bin;
matrix[N, Kc] X_controls;
int <lower=1> N_1;
int <lower=1> M_1;
int <lower=1> J_1[N];
int <lower=1> N_2;
int <lower=1> M_2;
int <lower=1> J_2[N];
7

int <lower=1> N_3;
int <lower=1> M_3;
int <lower=1> J_3[N];
}
transformed data {
matrix[N, Kc] Xc_controls;
vector[Kc] means_X_controls;
for (k in 1:Kc) {
means_X_controls[k] = mean(X_controls[, k]);
Xc_controls[, k] = X_controls[, k] - means_X_controls[k];
}
}
parameters {
simplex[D] nu;
real <lower=0, upper=1> probs[K, D];
vector[D - 1] b;
vector[Kc] b_controls;
real Intercept;
real <lower=0> shape;
real Intercept_hu;
vector <lower=0>[M_1] sd_1;
vector[N_1] z_1[M_1];
vector <lower=0>[M_2] sd_2;
vector[N_2] z_2[M_2];
vector <lower=0>[M_3] sd_3;
vector[N_3] z_3[M_3];
}
transformed parameters {
matrix[K, D] log_prob;
matrix[K, D] log_prob;
vector[N_1] r_1_1;
vector[N_2] r_2_1;
vector[N_3] r_3_hu_1;
real lprior = 0;
r_1_1 = (sd_1[1] * (z_1[1]));
r_2_1 = (sd_2[1] * (z_2[1]));
r_3_hu_1 = (sd_3[1] * (z_3[1]));
lprior += normal_lpdf(b | b_BRM , 5);
lprior += normal_lpdf(b_controls | b_controls_BRM , 0.1);
lprior += student_t_lpdf(Intercept | 3, -4, 2.5);
lprior += gamma_lpdf(shape | shape_BRM * 10, 10);
lprior += logistic_lpdf(Intercept_hu | 0, 1);
lprior += student_t_lpdf(sd_1 | 3, 0, 2.5)
-1*s t u d e n t _ t _ l c c d f ( 0|3 ,0 ,2 . 5 ) ;
lprior += student_t_lpdf(sd_2 | 3, 0, 2.5)
-1*s t u d e n t _ t _ l c c d f ( 0|3 ,0 ,2 . 5 ) ;
for (d in 1:D) {
8

log_prob[, d] = log(to_vector(probs[ , d]));
}
}
model {
for (d in 1:D) {
nu[d] ~ normal(nu_EM[d], 0.1);
for (k in 1:K) {
probs[k, d] ~ normal(probs_EM[k, d], 0.1);
}
}
{
vector[N] mu = rep_vector(0.0, N);
vector[N] hu = rep_vector(0.0, N);
real mu_nd = 0.0;
row_vector[D] ps;
mu += Xc_controls * b_controls;
hu += Intercept_hu;
for (n in 1:N) {
row_vector[D] pred_class_n;
row_vector[D - 1] class_X;
mu[n] += r_1_1[J_1[n]] + r_2_1[J_2[n]];
hu[n] += r_3_hu_1[J_3[n]];
ps = log(nu ’) + X_bin[n] * log_prob +
(1 - X_bin[n]) * log1m_exp(log_prob);
pred_class_n = exp(ps - log_sum_exp(ps));
for (d in 1:D) {
if (d < 2) {
class_X[d] = pred_class_n[d];
}
if (d > 2) {
class_X[d - 1] = pred_class_n[d];
}
}
mu[n] += Intercept + dot_product(class_X , b);
mu[n]= exp(mu[n]);
target += hurdle_gamma_logit_lpdf(Y[n] | shape , shape / mu[n], hu[n]);
target += log_sum_exp(ps);
}
}
target += lprior;
target += std_normal_lpdf(z_1[1]);
target += std_normal_lpdf(z_2[1]);
target += std_normal_lpdf(z_3[1]);
}
generated quantities {
real b_Intercept = Intercept - dot_product(means_X_controls , b_controls);}
9

WEB APPENDIX C: SELECTING THE NUMBER OF ARCHETYPES
Table W.C.1: ELPD Values for Archetype Numbers
Number of Archetypes ELPD (higher is better)
2- 6 1 9 5 . 5
3- 6 1 7 0 . 3
4- 6 1 4 7 . 2
5- 6 1 4 1 . 8
6- 6 1 4 1 . 1
7 -6138.5
8- 6 1 4 2 . 8
10

WEB APPENDIX D: PAIR WISE INTERACTION RESULTS
Here we present the pairwise interaction model results for each outcome.
Table W.D.1: Unaided Awareness (All Pairwise E↵ects)
Est. CI:L CI:U
Intercept 0.03 0.01 0.12
Share:Cinema 2.11 0.03 143.40
Share:F acebook 2.75 0.31 26.80
Share:Magazines 0.25 0.02 2.95
Share:Newspapers 2.06 0.14 30.13
Share:Online Display 1.27 0.20 7.70
Share:Outdoor 0.76 0.08 6.85
Share:Point of sale 0.36 0.01 26.66
Share:Radio 0.90 0.01 85.03
Share:TV 0.97 0.19 4.60
Share:Y outube 2.22 0.04 103.37
Share:Cinema ⇥ Share:F acebook 0.47 < 0.01 8918.14
Share:Cinema ⇥ Share:Magazines 0.61 < 0.01 8717.09
Share:Cinema ⇥ Share:Newspapers 2.13 < 0.01 5742.64
Share:Cinema ⇥ Share:Online Display 0.76 < 0.01 12176.73
Share:Cinema ⇥ Share:Outdoor 8.84 < 0.01 115353.32
Share:Cinema ⇥ Share:Point of sale 0.71 < 0.01 10970.43
Share:Cinema ⇥ Share:Radio 1.56 < 0.01 26742.80
Share:Cinema ⇥ Share:TV 0.19 < 0.01 268.19
Share:Cinema ⇥ Share:Y outube 0.75 < 0.01 10383.02
Share:F acebook ⇥ Share:Magazines 0.19 < 0.01 694.41
Share:F acebook ⇥ Share:Newspapers 0.86 < 0.01 11449.47
Share:F acebook ⇥ Share:Online Display 0.75 < 0.01 5809.82
Share:F acebook ⇥ Share:Outdoor 0.03 < 0.01 29.01
Share:F acebook ⇥ Share:Point of sale 0.48 < 0.01 6133.01
Share:F acebook ⇥ Share:Radio 1.39 < 0.01 20943.13
Share:F acebook ⇥ Share:TV 0.05 < 0.01 5.19
Share:F acebook ⇥ Share:Y outube 2.46 < 0.01 24583.10
Share:Magazines ⇥ Share:Newspapers 1.38 < 0.01 20527.05
Share:Magazines ⇥ Share:Online Display 0.24 < 0.01 1253.72
Share:Magazines ⇥ Share:Outdoor 5.62 < 0.01 42424.71
Share:Magazines ⇥ Share:Point of sale 0.43 < 0.01 5859.46
Share:Magazines ⇥ Share:Radio 0.83 < 0.01 19637.84
Share:Magazines ⇥ Share:TV 0.34 < 0.01 81.71
Share:Magazines ⇥ Share:Y outube 2.61 < 0.01 40286.95
Share:Newspapers ⇥ Share:Online Display 7.81 < 0.01 130685.54
Share:Newspapers ⇥ Share:Outdoor 0.21 < 0.01 581.65
Share:Newspapers ⇥ Share:Point of sale 0.98 < 0.01 18467.99
Share:Newspapers ⇥ Share:Radio 0.61 < 0.01 7633.47
Share:Newspapers ⇥ Share:TV 26.86 0.12 6325.19
Share:Newspapers ⇥ Share:Y outube 1.29 < 0.01 8071.30
Share:Online Display ⇥ Share:Outdoor 119.34 0.14 95223.00
Share:Online Display ⇥ Share:Point of sale 1.30 < 0.01 7219.61
Share:Online Display ⇥ Share:Radio 2.68 < 0.01 39133.47
Share:Online Display ⇥ Share:TV 0.21 0.01 8.22
Share:Online Display ⇥ Share:Y outube 0.20 < 0.01 219.84
Share:Outdoor ⇥ Share:Point of sale 9.88 < 0.01 90003.06
Share:Outdoor ⇥ Share:Radio 0.16 < 0.01 1770.38
Share:Outdoor ⇥ Share:TV 2.23 0.07 69.62
Share:Outdoor ⇥ Share:Y outube 9.06 < 0.01 61643.22
Share:Point of sale ⇥ Share:Radio 1.11 < 0.01 14522.07
Share:Point of sale ⇥ Share:TV 68.55 0.07 55028.20
Share:Point of sale ⇥ Share:Y outube 0.18 < 0.01 1797.32
Share:Radio ⇥ Share:TV 1.62 < 0.01 2967.30
Share:Radio ⇥ Share:Y outube 0.87 < 0.01 10142.83
Share:TV ⇥ Share:Y outube 4.74 0.01 3014.85
11

Table W.D.2: Aided Awareness (All Pairwise E↵ects)
Est. CI:L CI:U
Intercept 0.02 < 0.01 0.06
Share:Cinema 17.79 0.86 447.99
Share:F acebook 5.45 1.22 23.45
Share:Magazines 1.31 0.21 8.31
Share:Newspapers 3.84 0.50 31.45
Share:Online Display 1.93 0.36 10.02
Share:Outdoor 1.64 0.28 9.22
Share:Point of sale 3.04 0.13 78.02
Share:Radio 3.95 0.07 223.56
Share:TV 1.74 0.45 6.77
Share:Y outube 0.85 0.03 23.17
Share:Cinema ⇥ Share:F acebook 0.91 < 0.01 1421.48
Share:Cinema ⇥ Share:Magazines 0.64 < 0.01 9148.26
Share:Cinema ⇥ Share:Newspapers 0.09 < 0.01 304.65
Share:Cinema ⇥ Share:Online Display 22.11 < 0.01 128759.85
Share:Cinema ⇥ Share:Outdoor 0.63 < 0.01 4061.77
Share:Cinema ⇥ Share:Point of sale 0.64 < 0.01 9693.98
Share:Cinema ⇥ Share:Radio 14.75 < 0.01 169678.87
Share:Cinema ⇥ Share:TV 2.35 0.01 1365.37
Share:Cinema ⇥ Share:Y outube 0.42 < 0.01 5574.87
Share:F acebook ⇥ Share:Magazines 0.03 < 0.01 56.46
Share:F acebook ⇥ Share:Newspapers 0.68 < 0.01 11857.52
Share:F acebook ⇥ Share:Online Display 0.56 < 0.01 1401.11
Share:F acebook ⇥ Share:Outdoor 0.72 < 0.01 174.28
Share:F acebook ⇥ Share:Point of sale 0.93 < 0.01 8087.89
Share:F acebook ⇥ Share:Radio 0.65 < 0.01 6671.80
Share:F acebook ⇥ Share:TV 0.28 0.01 6.82
Share:F acebook ⇥ Share:Y outube 1.03 < 0.01 1456.94
Share:Magazines ⇥ Share:Newspapers 0.27 < 0.01 326.83
Share:Magazines ⇥ Share:Online Display 4.14 < 0.01 10783.76
Share:Magazines ⇥ Share:Outdoor 24.68 0.01 74077.94
Share:Magazines ⇥ Share:Point of sale 0.16 < 0.01 328.81
Share:Magazines ⇥ Share:Radio 1.62 < 0.01 26117.25
Share:Magazines ⇥ Share:TV 0.16 < 0.01 8.71
Share:Magazines ⇥ Share:Y outube 12.19 0.01 21376.71
Share:Newspapers ⇥ Share:Online Display 6.67 < 0.01 49802.05
Share:Newspapers ⇥ Share:Outdoor 0.23 < 0.01 437.28
Share:Newspapers ⇥ Share:Point of sale 2.03 < 0.01 36744.14
Share:Newspapers ⇥ Share:Radio 0.11 < 0.01 1627.44
Share:Newspapers ⇥ Share:TV 1.98 0.02 201.25
Share:Newspapers ⇥ Share:Y outube 0.39 < 0.01 2061.32
Share:Online Display ⇥ Share:Outdoor 0.84 0.01 146.11
Share:Online Display ⇥ Share:Point of sale 3.74 < 0.01 16238.99
Share:Online Display ⇥ Share:Radio 21.62 < 0.01 235963.98
Share:Online Display ⇥ Share:TV 2.17 0.08 62.94
Share:Online Display ⇥ Share:Y outube 1.72 < 0.01 1167.15
Share:Outdoor ⇥ Share:Point of sale 32.44 0.01 168546.99
Share:Outdoor ⇥ Share:Radio 12.43 < 0.01 54959.81
Share:Outdoor ⇥ Share:TV 5.97 0.41 80.12
Share:Outdoor ⇥ Share:Y outube 0.24 < 0.01 2171.96
Share:Point of sale ⇥ Share:Radio 0.80 < 0.01 9910.60
Share:Point of sale ⇥ Share:TV 38.16 0.12 11861.38
Share:Point of sale ⇥ Share:Y outube 0.06 < 0.01 773.50
Share:Radio ⇥ Share:TV 0.30 < 0.01 347.48
Share:Radio ⇥ Share:Y outube 0.41 < 0.01 5619.09
Share:TV ⇥ Share:Y outube 127.32 0.63 24656.96
12

Table W.D.3: Association (All Pairwise E↵ects)
Est. CI:L CI:U
Intercept 0.01 0.01 0.02
Share:Cinema 18.86 1.51 250.28
Share:F acebook 2.47 1.19 5.29
Share:Magazines 0.99 0.32 3.35
Share:Newspapers 3.46 1.03 11.61
Share:Online Display 2.59 1.19 5.85
Share:Outdoor 0.95 0.45 2.04
Share:Point of sale 1.16 0.29 5.17
Share:Radio 0.84 0.27 3.05
Share:TV 1.88 1.05 3.35
Share:Y outube 5.22 2.06 14.21
Share:Cinema ⇥ Share:F acebook 16.01 0.02 14193.03
Share:Cinema ⇥ Share:Magazines 0.53 < 0.01 4170.20
Share:Cinema ⇥ Share:Newspapers 3.07 < 0.01 3556.64
Share:Cinema ⇥ Share:Online Display 1.92 < 0.01 4030.28
Share:Cinema ⇥ Share:Outdoor 0.42 < 0.01 379.68
Share:Cinema ⇥ Share:Point of sale 0.28 < 0.01 4207.95
Share:Cinema ⇥ Share:Radio 1.13 < 0.01 9774.41
Share:Cinema ⇥ Share:TV 0.06 < 0.01 3.91
Share:Cinema ⇥ Share:Y outube 6.21 < 0.01 44443.18
Share:F acebook ⇥ Share:Magazines 1.77 0.01 337.07
Share:F acebook ⇥ Share:Newspapers 6.96 0.02 4288.99
Share:F acebook ⇥ Share:Online Display 15.65 0.17 1677.04
Share:F acebook ⇥ Share:Outdoor 0.31 0.01 7.55
Share:F acebook ⇥ Share:Point of sale 2.91 < 0.01 3222.62
Share:F acebook ⇥ Share:Radio 0.05 < 0.01 31.72
Share:F acebook ⇥ Share:TV 1.29 0.25 6.25
Share:F acebook ⇥ Share:Y outube 0.64 0.01 55.83
Share:Magazines ⇥ Share:Newspapers 0.54 < 0.01 150.24
Share:Magazines ⇥ Share:Online Display 0.02 < 0.01 6.07
Share:Magazines ⇥ Share:Outdoor 3.12 0.04 327.02
Share:Magazines ⇥ Share:Point of sale 0.46 < 0.01 356.48
Share:Magazines ⇥ Share:Radio 3.64 < 0.01 43441.54
Share:Magazines ⇥ Share:TV 3.15 0.28 38.59
Share:Magazines ⇥ Share:Y outube 5.62 0.02 2058.23
Share:Newspapers ⇥ Share:Online Display 3.62 < 0.01 2583.14
Share:Newspapers ⇥ Share:Outdoor 1.71 0.02 159.51
Share:Newspapers ⇥ Share:Point of sale 0.35 < 0.01 4985.90
Share:Newspapers ⇥ Share:Radio 0.77 < 0.01 1292.29
Share:Newspapers ⇥ Share:TV 10.49 0.85 117.02
Share:Newspapers ⇥ Share:Y outube 5.10 0.01 4378.15
Share:Online Display ⇥ Share:Outdoor 1.58 0.13 21.43
Share:Online Display ⇥ Share:Point of sale 3.31 0.02 937.78
Share:Online Display ⇥ Share:Radio 62.78 0.09 39014.10
Share:Online Display ⇥ Share:TV 0.91 0.22 3.59
Share:Online Display ⇥ Share:Y outube 0.14 < 0.01 7.33
Share:Outdoor ⇥ Share:Point of sale 9.27 0.11 893.48
Share:Outdoor ⇥ Share:Radio 13.67 0.10 2580.72
Share:Outdoor ⇥ Share:TV 5.19 1.64 15.39
Share:Outdoor ⇥ Share:Y outube 102.47 0.95 11271.17
Share:Point of sale ⇥ Share:Radio 2.77 < 0.01 16213.17
Share:Point of sale ⇥ Share:TV 46.31 2.98 708.13
Share:Point of sale ⇥ Share:Y outube 1.13 < 0.01 4928.32
Share:Radio ⇥ Share:TV 26.71 2.39 279.74
Share:Radio ⇥ Share:Y outube 0.41 < 0.01 3649.24
Share:TV ⇥ Share:Y outube 2.82 0.32 22.57
13

Table W.D.4: Motivation (All Pairwise E↵ects)
Est. CI:L CI:U
Intercept 0.01 0.01 0.03
Share:Cinema 10.32 0.76 141.23
Share:F acebook 2.65 1.18 6.11
Share:Magazines 1.17 0.39 3.95
Share:Newspapers 1.77 0.51 6.46
Share:Online Display 1.62 0.71 3.78
Share:Outdoor 0.86 0.36 2.01
Share:Point of sale 0.36 0.10 1.51
Share:Radio 0.69 0.18 3.16
Share:TV 1.52 0.79 2.91
Share:Y outube 3.15 1.15 9.45
Share:Cinema ⇥ Share:F acebook 0.16 < 0.01 169.32
Share:Cinema ⇥ Share:Magazines 0.41 < 0.01 4322.89
Share:Cinema ⇥ Share:Newspapers 0.80 < 0.01 1013.96
Share:Cinema ⇥ Share:Online Display 6.72 < 0.01 15398.41
Share:Cinema ⇥ Share:Outdoor 0.30 < 0.01 282.44
Share:Cinema ⇥ Share:Point of sale 0.25 < 0.01 5802.72
Share:Cinema ⇥ Share:Radio 3.04 < 0.01 25254.44
Share:Cinema ⇥ Share:TV 0.47 < 0.01 43.93
Share:Cinema ⇥ Share:Y outube 3.54 < 0.01 21560.37
Share:F acebook ⇥ Share:Magazines 5.29 0.02 1291.33
Share:F acebook ⇥ Share:Newspapers 9.54 0.02 5721.46
Share:F acebook ⇥ Share:Online Display 2.93 0.02 472.15
Share:F acebook ⇥ Share:Outdoor 0.44 0.02 11.06
Share:F acebook ⇥ Share:Point of sale 3.22 < 0.01 4394.62
Share:F acebook ⇥ Share:Radio 0.11 < 0.01 97.97
Share:F acebook ⇥ Share:TV 0.32 0.06 1.63
Share:F acebook ⇥ Share:Y outube 0.09 < 0.01 10.60
Share:Magazines ⇥ Share:Newspapers 0.14 < 0.01 54.62
Share:Magazines ⇥ Share:Online Display 0.07 < 0.01 24.21
Share:Magazines ⇥ Share:Outdoor 0.43 < 0.01 95.99
Share:Magazines ⇥ Share:Point of sale 1.28 < 0.01 676.92
Share:Magazines ⇥ Share:Radio 6.85 < 0.01 52103.49
Share:Magazines ⇥ Share:TV 1.10 0.09 13.46
Share:Magazines ⇥ Share:Y outube 0.92 < 0.01 574.32
Share:Newspapers ⇥ Share:Online Display 18.83 0.02 15879.14
Share:Newspapers ⇥ Share:Outdoor 4.89 0.04 616.77
Share:Newspapers ⇥ Share:Point of sale 1.00 < 0.01 17509.63
Share:Newspapers ⇥ Share:Radio 3.35 < 0.01 5751.61
Share:Newspapers ⇥ Share:TV 4.71 0.33 70.51
Share:Newspapers ⇥ Share:Y outube 28.64 0.03 53369.10
Share:Online Display ⇥ Share:Outdoor 2.29 0.13 48.24
Share:Online Display ⇥ Share:Point of sale 0.02 < 0.01 15.87
Share:Online Display ⇥ Share:Radio 0.01 < 0.01 12.57
Share:Online Display ⇥ Share:TV 1.06 0.23 5.37
Share:Online Display ⇥ Share:Y outube 0.97 0.02 54.48
Share:Outdoor ⇥ Share:Point of sale 129.33 1.50 12448.01
Share:Outdoor ⇥ Share:Radio 11.05 0.05 2784.74
Share:Outdoor ⇥ Share:TV 3.93 1.17 13.74
Share:Outdoor ⇥ Share:Y outube 150.37 1.38 19399.21
Share:Point of sale ⇥ Share:Radio 25.59 0.01 109059.55
Share:Point of sale ⇥ Share:TV 156.07 11.03 2225.72
Share:Point of sale ⇥ Share:Y outube 1.56 < 0.01 5919.09
Share:Radio ⇥ Share:TV 11.27 0.73 151.09
Share:Radio ⇥ Share:Y outube 0.40 < 0.01 4262.54
Share:TV ⇥ Share:Y outube 4.14 0.46 37.11
14

WEB APPENDIX E: V ARIATIONS AND ADDITIONAL RESULTS
Several variations and minor additional results are collected here.
Combining Unaided and Aided Awareness
Table W.E.1 (below) shows the same results as Table 5 but with Unaided and Aided
Awareness outcomes combined by averaging them at the campaign level. The results are
similar to when the variables are used separately.
Archetype Prevalance by Category
Table W.E.2 (below) shows prevalance by category. Archetype 2 is the most common in
all categories. Archetype 1 is second most common in Services and Technology & Durables,
while Archetype 3 is most common in CPG.
15

Table W.E.1: Outcome Model Results with Combined Awareness
(a) Motivation (b) Association
Mean CI:L CI:U Mean CI:L CI:U
Intercept 0.01 0.01 0.02 0.01 0.01 0.02
Archetype 1 1.22 0.91 1.65 1.38 1.04 1.85
Archetype 3 1.99 1.56 2.60 1.83 1.45 2.34
Archetype 4 2.25 1.51 3.51 2.02 1.41 2.94
Archetype 5 1.74 1.25 2.49 1.68 1.22 2.31
Archetype 6 1.66 1.18 2.45 1.59 1.12 2.32
Archetype 7 1.65 1.05 2.60 1.45 0.99 2.14
Concentraton 0.95 0.80 1.13 0.68 0.58 0.81
Time Trend 1.02 1.00 1.05 1.00 0.98 1.03
Share: Cinema 3.34 2.78 4.04 6.05 4.98 7.33
Share: Facebook 1.33 1.12 1.58 1.68 1.42 2.01
Share: Magazines 0.69 0.57 0.83 0.60 0.49 0.72
Share: Newspapers 1.98 1.66 2.37 3.34 2.77 4.03
Share: Online Display 1.09 0.91 1.32 1.77 1.50 2.10
Share: Outdoor 0.65 0.55 0.78 0.77 0.64 0.92
Share: POS 1.09 0.90 1.32 2.02 1.68 2.43
Share: Radio 0.89 0.74 1.07 1.54 1.28 1.86
Share: TV 1.17 1.01 1.36 1.73 1.49 2.00
Share: Youtube 2.08 1.74 2.48 3.55 2.97 4.27
(c) Awareness
Mean CI:L CI:U
Intercept 0.01 0.00 0.01
Archetype 1 0.90 0.59 1.38
Archetype 3 2.20 1.55 3.22
Archetype 4 3.50 2.05 6.37
Archetype 5 1.87 1.16 3.14
Archetype 6 1.34 0.78 2.33
Archetype 7 1.92 1.07 3.41
Concentraton 1.27 1.06 1.51
Time Trend 1.02 0.99 1.06
Share:Cinema 21.73 17.92 26.49
Share:Facebook 2.56 2.13 3.08
Share:Magazines 0.53 0.44 0.64
Share:Newspapers 2.95 2.46 3.56
Share:Online Display 1.37 1.14 1.66
Share:Outdoor 0.77 0.65 0.93
Share:POS 0.82 0.68 1.00
Share:Radio 1.42 1.17 1.74
Share:TV 1.51 1.29 1.80
Share:Youtube 2.86 2.36 3.48
Notes: CI:L is the 2.75th percentile and CI:U is the 97.5th percentile,
which together form the 95% credible interval.
16

Table W.E.2: Archetype Prevalence by Category
Tech &
CPG Services Durables
Archetype 1 0.19 0.16 0.23
Archetype 2 0.25 0.25 0.28
Archetype 3 0.20 0.11 0.13
Archetype 4 0.13 0.08 0.13
Archetype 5 0.06 0.14 0.17
Archetype 6 0.09 0.15 0.03
Archetype 7 0.08 0.11 0.04
17

WEB APPENDIX F: LITERATURE REVIEW TABLE
Table W.F.1:Selected Studies in Media Complementarity and Cross-E↵ects
Authors Media Channel Interactions DVs Scale/Scope
Gatignon and Hanssens (1987) Sales force by Advertising Sales Single Brand
Edell and Keller (1989) Television by Radio Recall and Motivation Experiments
Gopalakrishna and Chatterjee (1992) Sales force by Advertising Sales Single Brand
Naik and Raman (2003) Television by Print Advertising Sales Single Brand Campaign
Gopalakrishna and Chatterjee (1992) Sales force by Advertising Sales Single Brand
Naik and Raman (2003) Television by Print Advertising Sales Single Brand Campaign
Chang and Thorson (2004) Television by Online Banner Ads Attention and Motivation Experiments
Dijkstra, Buijtels, and van Raaij (2005) Television by Print by Online
Banner Ads
Recall and Motivation Experiments
Dijkstra, Buijtels, and van Raaij (2005) Television by Print by Online
Banner Ads
Recall and Motivation Experiments
Naik and Peters (2009) o✏ine (television, print, and ra-
dio) by online (banners and
search)
Consideration Single Brand
Danaher and Dagger (2013) television, newspapers, radio,
magazines, online display, search,
social media, catalogs, postal
mail, and e-mail
Sales Single Brand Campaign
Lin, Venkataraman, and Jap (2013) Television, Radio, Print, and
Computer
Satiation Consumer diaries
Joo, Wilbur, Cowgill, and Zhu (2014) Television by Paid Search Consumer Search 22 Brands, single industry
Srinivasan, Rutz, and Pauwels (2015) Television, Search, Consumer
Online Activity
Sales Single Brand
Continued on next page
18

T able W.F.1 – continued from previous page
Authors Media Channel Interactions DVs Scale/Scope
Kolsarici and Vakratsas (2018) National TV, Regional TV, Mag-
azine, Internet, Outdoor, News-
paper, and Radio
Sales 8 Brands (2 Auto, 6 CPG)
Fischer (2019) Television, Newspaper, Maga-
zines, Online Banner Ads
Awareness, Purchase in-
tent
Single Brand, 4 Campaigns
Fossen and Schweidel (2019) Television by Social Online trac and Sales 5 Brands, single industry
This Study Television, Magazines, News-
papers, Radio, Outdoor, Cin-
ema, Point of Sale, Online Dis-
play, Online Video, Facebook,
YouTube
Awareness (Aided and Un-
aided), Brand Association,
and Motivation
1105 campaigns, 557
brands, 6 Industries, 51
countries
19

WEB APPENDIX REFERENCES
Stockute, Raminta, Andrea Veaux, and Paul Johnson “Logistic Distribution,” (2013).
Vehtari, Aki, Andrew Gelman, Daniel Simpson, Bob Carpenter, and Paul-Christian B¨ urkner (2021),
“Rank-normalization, folding, and localization: An improved ˆR for assessing convergence of
MCMC (with discussion),” Bayesian analysis , 16 (2), 667–718.
20
