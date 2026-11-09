---
title: Decoding Political Polarization in Social Media Interactions
url: https://arxiv.org/abs/2407.03773
category: social-media
subcategory: empirical
date: 2024-07
venue: ''
authors:
- Giulio Pecile
- Niccolò Di Marco
- Matteo Cinelli
- Walter Quattrociocchi
source: arxiv
pdf_url: https://arxiv.org/pdf/2407.03773
pages: 7
chars: 40460
fetched_at: '2026-11-08T13:06:18+00:00'
kb_version: 1
---

# Decoding Political Polarization in Social Media Interactions

1
Decoding Political Polarization in Social Media Interactions
Giulio Pecile 1, Niccol `o Di Marco 1, Matteo Cinelli 1, Walter Quattrociocchi 1
1Sapienza University of Rome, Italy
Social media platforms significantly influence ideological divisions by enabling users to select information that aligns with their
beliefs and avoid opposing viewpoints. Analyzing approximately 47 million Facebook posts, this study investigates the interactions
of around 170 million users with news pages, revealing distinct patterns based on political orientations. While users generally
prefer content that reflects their political biases, the extent of engagement varies even among individuals with similar ideological
leanings. Specifically, political biases heavily influence commenting behaviors, particularly among users leaning towards the center-
left and the right. Conversely, the ’likes’ from center-left and centrist users are more indicative of their political affiliations. This
research illuminates the complex relationship between social media behavior and political polarization, offering new insights into
the manifestation of ideological divisions online.
Index Terms—Social Media, Polarization, Selective Exposure, News Consumption.
I. I NTRODUCTION
T
He World Wide Web has vastly increased information
accessibility, transforming how information is distributed
and consumed globally. This evolution has revolutionized
communication methods, erasing geographical and temporal
constraints. Over recent decades, expanding social networks
and shifting public discourse to digital platforms have led
scholars to explore how users interact with information and
form behavioral clusters, often challenging traditional expec-
tations. It is well-documented that online users tend to engage
with information that confirms their pre-existing beliefs, typi-
cally ignoring conflicting viewpoints [1], [2]. Such behaviors
create echo chambers, where like-minded individuals reinforce
each other’s views [3], [4], [5]. Such configurations, alongside
growing polarization, manifest with varying intensity across
different social media platforms [6], suggesting that the users’
base as well as platform designs and algorithms, which aim to
maximize engagement, play a significant role in shaping these
social dynamics.
Existing literature [7] suggests that although individuals
generally prefer political news that aligns with their pre-
existing beliefs, they do not entirely ignore opposing view-
points. Conversely, Guess [8] finds that most users gravitate
towards centrist news outlets despite a small, highly engaged
group favoring partisan sources. These patterns indicate a
notable convergence in the information available to the broader
public. However, the ability of individuals to completely shield
themselves from conflicting information is limited due to
the minimal control they have over the content presented
to them and the dynamics of information spread on social
media platforms. Notably, ’weak ties’—connections between
loosely affiliated individuals like acquaintances or distant
relatives—are crucial in spreading new information across
social networks [9].
Notably, most content users interact with on social media
is not actively sought but is delivered through a network
algorithm tailored to maximize user engagement. This char-
Corresponding author: W. Quattrociocchi (email: wal-
ter.quattrociocchi@uniroma1.it).
acteristic is pivotal as it may foster unrecognized behavioral
patterns, complicating efforts to measure such effects. Due
to concerns over potential manipulation by malicious actors,
social networks often refrain from disclosing the specifics
of these algorithms. Sunstein, in his book Republic: Divided
Democracy in the Age of Social Media [10], discusses the Age
of the Algorithm , where users lack control over their news
consumption, inadvertently contributing to the formation of
echo chambers.
Not all users exhibit polarization similarly. However, their
behaviors show significant nuances. Zaller observes that polit-
ically engaged citizens are particularly receptive to messages
that align with their beliefs [11]. Similarly, Taber and Lodge
find that highly partisan users are more likely to embrace
supporting arguments while dismissing contrary ones with-
out question [12]. This suggests that increasing polarization
complicates efforts to mitigate it, and using counterfactuals
might even be counterproductive [2]. The debate over which
political group is more prone to selective exposure and biased
information processing remains unresolved. Some studies in-
dicate that conservatives are more likely to engage in such
behaviors [13], [14], [15], while others present contradictory
findings [16], [17], [18]. Furthermore, there is no consensus
on cross-party discussions; Barber ´a suggests that liberals are
more involved in cross-party interactions [19], whereas Wu
argues that conservatives are more likely to engage in such
discussions [20].
In this study, we explore the phenomenon of selective
exposure by analyzing how about 170 million Facebook users
interact with approximately 47 million posts from news agen-
cies with varying political leanings. We specifically measure
the intensity of selective exposure and assess whether users
prefer specific ideologies or news agencies. The analysis is
structured around several distinct scenarios of user selectivity:
• users who are not selective at all;
• users who are selective both in terms of pages viewed
and the political leaning of the pages;
• users who are selective only in terms of political leaning;
• users who are selective in terms of pages viewed.
arXiv:2407.03773v1  [cs.SI]  4 Jul 2024

2
By categorizing user behavior into these scenarios, we
aim to uncover the extent and nature of selective exposure,
identifying whether it is more pronounced towards particular
ideologies or news providers.
We find that all users exhibit strong selectivity in terms
of political leaning, a phenomenon explained mainly by a
marked preference for specific pages [21], [22]. However,
this preference does not fully account for the leaning-based
selective exposure observed in specific user groups. These
results are crucial for understanding the primary drivers of
selective exposure and the resultant polarization within online
communities. Our framework enables an examination of the
role political affiliation plays in the selectivity exhibited by
users. The structure of this paper is organized as follows:
Initially, we discuss related works that explore the concepts
of polarization, the echo chamber hypothesis, and their in-
teractions with social media. We then describe the theoretical
methods used in our analysis, including entropy as a proxy for
measuring selective exposure and two randomization strategies
to evaluate the robustness of our findings. Following this,
we detail the patterns of user activity concentration and
demonstrate how this concentration aligns predominantly with
ideological page biases. The paper concludes by presenting
evidence of leaning-driven selectivity, predominantly among
users who follow pages with right and center-left biases.
II. R ELATED WORKS
A. Polarization and Echo Chambers
The prevailing hypothesis suggests that echo chambers
on social media significantly influence social dynamics by
amplifying similar opinions and minimizing opposing ones,
fostering homophily and polarization [5]. This effect is of-
ten exacerbated by the emergence of intolerance in online
discussions [23], [24], which further polarizes interactions
[25], [26], [27], [28]. Numerous studies employing diverse
algorithms and methodologies substantiate these observations
[29], [30], [31], [32], including Garimella’s work [4], which
uses the Walktrap Controversy metric to measure segregation
in discussion networks on polarizing topics. Additionally,
Salloum [33] investigates how network size, edge count, and
degree distribution influence polarization scores, proposing
methods to mitigate these biases. Global events such as Brexit
[34], vaccine debates [35], and climate change discussions
[36] frequently act as catalysts for the formation of echo
chambers. The political bias of news agencies covering these
events significantly contributes to these dynamics, as studies
indicate that highly polarized user clusters often form around
specific news pages [37], [21], distinguished by their narrative
and selective biases [38]. It is crucial to differentiate between
affective and ideological polarization. Affective polarization,
or psychological polarization [39], occurs when opposing
groups harbor feelings of dislike and distrust towards each
other. In contrast, ideological polarization involves differing
views that do not necessarily include moral judgments of the
opposing group. Affective polarization is particularly noted
in the partisan divide between Democrats and Republicans
in the United States [40] and is increasingly prevalent on
social media. This rise is attributed to the ease of identifying
a user’s political leanings, which complicates civil cross-
party dialogue, reinforces social and political identities, and
promotes negative stereotyping of opposing groups.
B. The interplay between social media and polarization
While there is broad consensus that social networks often
serve as arenas for polarization and echo chambers, the precise
mechanisms through which these platforms influence these
phenomena are still being explored [6]. Concerns about the
role of social media and search engines in filtering news,
potentially exacerbating polarization, remain significant [10],
[41]. Although highly polarized users tend to form homoge-
neous clusters, such filtering effects might be mitigated by
systems like those proposed by Garimella [42]. Conversely,
studies indicate that exposure to contrarian news sources
may actually increase political polarization [43], [44], and
introducing users who believe in conspiracy theories to fact-
checkers could be ineffective or even counterproductive [2],
[45]. The impact of algorithmically tailored feeds on polar-
ization has also been critically examined [46], [47], [48],
[49]. These studies assess the interactions between algorithmic
recommendations and societal forces, comparing their effects
to those produced by non-tailored feeds. The findings suggest
that personalized feeds may not significantly increase polar-
ization, pointing to other factors as potential drivers behind
the observed polarization on these platforms.
III. M ATERIALS AND METHODS
A. Entropy and selective exposure
To fully measure the phenomenon of selective exposure
defined as a tendency for people both consciously and un-
consciously to seek out material that supports their existing
attitudes and opinions and to actively avoid material that
challenges their views [50], one would need the full digital
trace of a user and the reasons that motivated the user to
interact with one page instead of another. In its absence, we
use the entropy of the interactions as a proxy. We recall that
Shannon Entropy is commonly used in information theory to
measure the concentration of a distribution. In our framework,
users with low entropy are the most selective, while those
interacting with different bias levels uniformly have high
entropy.
In particular, here we also employ some of its properties
that arise when considering sub-partitions.
Consider a set universe U and a partition σ = {s1, . . . , sn}
of it. We denote |si| ≡ci. Suppose that ρ is a partition of σ,
i.e. if for each r ∈ ρ, r⊆ si ∈ σ for exactly one i. Then, each
set of ρ can be written as:
ρ = {s1 1, . . . , s1 c1 , . . . , si 1, . . . , si ci , sn 1 , . . . , sn cn },
i.e. si j its the j−th subset of si.
Now, consider a random variable Xρ having image in ρ.
Obviously, Xρ can be naturally extended to Xσ having image
in σ. We define p(Xρ ∈ si j) ≡ pi j. It follows, p(Xρ ∈ si) =
p(Xσ ∈ si) = Pci j=1 pi j ≡ pi. We have that:

3
H(Xρ) = −
X
i
X
j
pi j log pi j =
= −
X
i
X
j

pi j log(pi) + pi j log pi j pi
!
=
= −
X
i
pilog(pi) − X
i
pi X
j
¯pi j log ¯pi j,
where ¯pi j = pi j pi . In a more compact form, we have obtained:
H(Xρ) = H(Xσ) +
X
i
piH(Xρ|Xσ ∈ si). (1)
In this work, we consider interactions over pages having
a certain political leaning. Therefore, given the general set
of spaces, σ will be the partition induced by their political
leaning, while ρ will be simply the partition in which each
page is considered alone.
Having reached Equation (1), it is immediate to find the
theoretical minimum and maximum entropy of the finer par-
tition ρ (i.e. the pages) given the interaction over partition σ
(i.e. the leanings).
This follows from the observation that the H(Xσ) and
pi terms are fixed, and the terms H(Xρ|Xσ ∈ si) are
all independent of one another and thus can be minimized
(maximized) independently. The minimum is clearly found
when H(Xρ|Xσ ∈ si) = 0 ∀i i.e. when the activity of the
user is concentrated in at most one page for every si (i.e.
leaning).
On the other hand, we recall that the maximum entropy is
reached by a uniform distribution. Since we consider interac-
tions, which are discrete and often not large, it is not always
possible to obtain an exact uniform distribution. Therefore,
we compute the maximum possible value of entropy with the
below criteria.
Consider a user u with n interactions in ci pages from si.
The maximum entropy is found when r pages receive q + 1
interactions and ci − r pages receive q interactions, where q
and r are the quotient and remainder of the integer division
of n ci . Note that, if n ≤ ci, the maximum entropy is simply log n.
Finally, we note that in everysi the minimum and maximum
entropies are the same only when there is only one interaction,
in which case H(Xρ|Xσ ∈ si) = 0.
B. Strong and weak randomization
In our analysis, we compare the actual interaction patterns to
those resulting from two randomization processes: a stronger
one, where each interaction between users and pages is ran-
domized, and a weaker one, where the Bias labels of the pages
are randomized. In both cases, the number of interactions made
by each user and received by each page remains the same, and
the number of pages for each bias label remains unchanged.
Furthermore, we notice that in the strong randomization pro-
cess, the users distribute their activity uniformly across pages
as the original multiple interactions between the same user and
the same page are now spread between multiple pages. This
uniformity of interactions implies that the result of a strong
randomization process would be unaffected by a further weak
randomization. Thus, the strong randomization process implies
the weaker one. In Figure 1, the details of the randomization
processes are visually explained. Note that, in the bipartite
representation, each edge indicate an interaction between a
user and a page and multiple edges are allowed.
• • •
• • •
• • •
• •
Users Pages Bias labels
•
• • •
• • •
• • •
• •
Users Pages Bias labels
•
• • •
• • •
• • •
• •
Users Pages Bias labels
•
Original dataset
Strong Randomization
Weak Randomization
Fig. 1. In the tripartite representation of the interactions, the strong random-
ization process affects the user-pages interactions, while the weak one affects
the page-bias affiliations.
IV. R ESULTS
In our analysis, we use the same dataset as two previous
papers [21], [6], which comprise roughly 266 million com-
ments and 1.5 billion likes from about 170 million users on
47 million Facebook posts by 222 pages of news agencies.
Those news agencies have a Bias score, provided by Media
Bias/Fact Check [51], with five possible leanings ranging from
left to right. We infer the political bias of users using the mode
of the leanings of their interactions. The distribution of pages
and users by political leaning is shown in Figure 2, where we
see that while most pages and users are identified as center-left
leaning, there are in proportion many more right-wing users
than pages.
0.0 × 10+0
2.5 × 10+7
5.0 × 10+7
7.5 × 10+7
1.0 × 10+8
Left
Center−Left
Center
Center−Right
Right
Bias
Count
Users by bias
0.0 × 10+0
2.5 × 10+1
5.0 × 10+1
7.5 × 10+1
1.0 × 10+2
Left
Center−Left
Center
Center−Right
Right
Bias
Count
Pages by bias
Fig. 2. Number of Facebook pages and users grouped by political affiliation.
A. Measuring Selective exposure
We first explore patterns of activity concentration by group-
ing users by the number of their likes and comments. We

4
create 12 logarithmic bins and, for each bin, we compute the
average number of pages they interact with. We then replicate
this analysis on the strongly randomized dataset (see Materials
and Methods for further details). Figure 3 compares the two
scenarios.
Comments Likes
101 103 105 101 103 105
0
50
100
150
Number of interactions
Number of pages visited
Users per bin
100
102
104
106
Random
FALSE
TRUE
Fig. 3. Number of pages among which users divide their attention.
The results show that the real behavior of users is much
more concentrated than the randomized case. Note that, in this
latter case, the probability that a user interacts with a page is
solely based on the page’s popularity i.e. the number of users
interacting with it. While this on itself does not imply that
there is a specific tendency for users to prefer content that
is congruent with their specific view, it already suggests that
users’ activity is strongly dependent on factors that transcend
the simple popularity of the page, as in the randomization case.
To understand if political leaning could be one of these
factors, we group pages by their bias level and, for each
user, we evaluate the Shannon entropy of their distribution
of interactions left in each political class. We use this metric
because it clearly indicates how concentrated or spread out
each user’s activity is. We scale the entropy values to a [0, 1]
interval by dividing by log 5, the theoretical maximum entropy
value for 5 classes. To ensure that the observed selectivity is
not due to low activity, we consider only users who have made
more than 5 comments (likes) in this and all further analyses.
The empirical cumulative distribution function (eCDF) of the
values of Shannon’s entropy for all groups of users is presented
in Figure 4. Additionally, we highlight the entropy levels
corresponding to a user interacting evenly with two, three,
and four different leanings using grey lines.
Clearly, the leaning classification of users is most reliable
for those with entropy at the left of the first line, since they
comment very heterogeneously. All groups of users display a
strong level of selectivity, with center-leaning users being the
most selective. We observe that, in all groups, at least 50% of
the users concentrated their commenting activity on pages of
the same political leaning. This trend is also present, albeit less
prominent, with likes, with center-right-leaning users being
less selective than other groups of users. We compare this
situation with the strong randomization process, that describes
users interacting with pages based solely on popularity.
Interestingly, we observe a substantial difference with the
randomized scenario, suggesting again that even the least
selective users choose content according to a criterion com-
patible with political leaning.
Comments Likes
Original DatasetStrong randomization
0.00 0.25 0.50 0.75 1.000.00 0.25 0.50 0.75 1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Entropy (scaled)
P(e < x)
Left
Center−Left
Center
Center−Right
Right
Total
Fig. 4. Distributions of bias entropy of users compared with the strongly
randomized scenario.
B. Page and Bias Selectivity
In the previous section we have shown that users display
a strong level of selectivity compatible with an ideological
classification of the pages. However, this can only partially
capture users’ preferences in their activity. If users base their
interactions solely on the political leaning of a page, they
will treat all pages with the same leaning similarly. On the
other hand, if users are selective about specific pages, their
interactions within each bias level will reflect that page-driven
selectivity. We observe that since pages can be thought of
as a sub-partition of the bias levels, the values of the two
entropies (the one calculated by considering the interaction on
pages and bias levels) are actually dependent, as explained in
Materials and Methods. In particular, we find that the entropy
calculated on pages is equal to the entropy calculated on the
bias levels summed with a weighted average of the entropies
of the pages inside each bias level. Since each term of this
average is independent, they can be trivially minimized and
maximized. As explained in Materials and Methods, for each
user, we find the theoretical interval I(u) = [m(u), M(u)] in
which the actual page entropy Hp(u) can be found and scale
the result using
x(u) = Hp − m M − m .
Doing that, users who make at most one interaction per bias
level are removed as the theoretical minimum and maximum
coincide. This phenomenon is desirable, as it is impossible to
decide if further selectivity is motivated by a preference for
specific pages. We also recall that the analysis is performed
only on users who have made at least five comments (likes) to
ensure that the selectivity measured cannot be attributed to low
activity. Table I reports the summary characteristics of thex(u)
values distribution. Interestingly, we can observe that users
tend to be very selective regarding pages, often concentrating
their activity on one page per bias level.

5
TABLE I
QUARTILES OF THE x STATISTICS DESCRIBING INTER -BIAS SELECTIVITY .
Min 1st Quartile Median 3rd Quantile Max
Likes 0 0 0 0.2108 1
Comments 0 0 0 0.09045 1
C. Bias and Page Selectivity
In the previous sections, we have observed that, although
users exhibit a selective behavior that is compatible with
political segregation, it is not the only explaining driver of user
activity. As users interact with -relatively- few pages, many
alternative divisions could be compatible with the observed
phenomenon, and thus, it is necessary to assess the divergence
between the real selective exposure expressed by the users
and a benchmark value found by grouping pages randomly.
To accomplish this, we perform the weak randomization
process described in Materials and Methods to account for
measurements of bias selectivity that may arise from the
simple page selectivity or other sorts of selective behaviors
(for instance, locality-driven selectivity). We notice that the
users interacting with only one page will naturally interact with
only one bias class, regardless of the randomization. For those
users, deciding if a preference in political leaning, locality,
or any arbitrary classification of pages drives their choice of
activity is impossible. For this reason, we set those users aside
and only compute the distributions of users who interact with
at least two pages and have a minimum of five interactions.
Upon performing the weak randomization process, we note
that since the user-page relations are unchanged, the page
entropy of each user remains unaffected by this particular
randomization process. This allows us to measure the bias
selectivity while accounting for the strong patterns of page
selectivity measured previously.
We perform a Monte Carlo experiment where each sim-
ulation is obtained using the weak randomization process.
To ensure the manageability of the procedure, we used a
random sample of the dataset (slightly over 2% of the users).
By averaging over multiple groupings of pages, we obtain a
benchmark value for the bias entropy of the users, which we
can then compare to the actual bias entropy. If the political
leaning determines a further selectivity, the distribution of
the original dataset will have higher entropy values, and,
especially at the left of the first line, the entropy eCDF will
have higher values. If, on the contrary, the two distributions
are similar or the weak randomization process produces higher
entropy values, it means that the political leaning of the pages
does not drive the selectivity of the users.
Figure 5 compares the real and randomized eCDF distribu-
tions and Table II summarizes the Kullback-Leibler divergence
between the distributions.
We observe that users primarily commenting on center and
center-right-leaning pages align closely with the randomized
distribution, suggesting that the political leaning of these pages
aligns with their usual consumption patterns. In contrast, users
interacting with center-left-leaning pages show the most signif-
icant divergence from the randomized model, indicating that
political leanings heavily influence their news consumption
habits. This is evident when comparing these findings with
those illustrated in Figure 4, where users engaging with only
one page are included. Notably, the exclusion of such users
significantly reduces the number of those with zero entropy.
Center-leaning users, who are the most selective, are most
impacted by this exclusion. This suggests that less politically
engaged users, who typically follow only one page, tend
to prefer center-leaning pages. Conversely, users with more
explicit political preferences display greater selectivity in their
interactions. For likes, the patterns slightly differ. Center-
leaning users clearly exhibit bias-driven engagement, a trend
that is less pronounced among right-leaning users and even
less so among center-right-leaning ones.
In particular, center-right-leaning users are less selective
than their randomized counterparts. Left- and center-left-
leaning users display prominent levels of divergence.
V. C ONCLUSION
In this paper, we conduct a comprehensive analysis of the
phenomenon of selective exposure on social media platforms.
Initially, we observe that user activity predominantly concen-
trates on a limited number of pages. As user engagement
increases, these pages quickly become saturated, suggesting
that user interactions are focused despite the availability of
vast content. Employing Shannon Entropy to explore the
homogeneity of user behavior, we identify a strong prefer-
ence for content that aligns with users’ pre-existing political
views. This finding supports the hypothesis that social media
serves as an echo chamber, amplifying and reinforcing similar
viewpoints. Further analysis reveals that user engagement
is not uniform across pages with similar political leanings.
Users prefer specific news sources within political categories,
indicating a more nuanced approach to selective exposure that
includes specific sources resonating deeply with individual
users. This observation prompted developing and applying
a novel methodology designed to dissect and analyze the
reasons behind such selective behaviors. Our findings indi-
cate that political congruence is a more significant driver of
user behavior than random selection, with effects particularly
pronounced among users leaning towards the center-left. Our
work establishes a robust framework for analyzing and com-
paring the mechanisms of selective exposure across various
user groups on social media. This framework enhances our
understanding of why users gravitate towards certain content
and improves our ability to predict page-level selectivity based
on political bias. Additionally, it helps identify which user
groups are most susceptible to selective exposure, shedding
light on how echo chambers form and persist. However, this
study has limitations. It does not account for the tone or nature
of interactions—whether users support, criticize, or comment
on content in a neutral or hostile manner. Despite this, we
are confident in the robustness of our findings. We observe
that negative or hostile interactions, though present, do not
significantly alter the overall patterns of selective exposure.
REFERENCES
[1] E. Bakshy, S. Messing, and L. A. Adamic, “Exposure to ideologically
diverse news and opinion on facebook,” Science, vol. 348, no. 6239,

6
Left Right Total
Center Center−Left Center−Right
0.00 0.25 0.50 0.75 1.000.00 0.25 0.50 0.75 1.000.00 0.25 0.50 0.75 1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Entropy (scaled)
P(e < x)
Comments
Left Right Total
Center Center−Left Center−Right
0.00 0.25 0.50 0.75 1.000.00 0.25 0.50 0.75 1.000.00 0.25 0.50 0.75 1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Entropy (scaled)
P(e < x)
Likes
Dataset Original Weak randomization
Fig. 5. Distribution of users’ bias entropy compared with the benchmark values obtained via weak randomization.
TABLE II
THE KULLBACK -L EIBLER DIVERGENCE BETWEEN THE DISTRIBUTION OF BIAS -ENTROPIES AND THE BENCHMARK OBTAINED VIA THE WEAK
RANDOMIZATION .
Left Center-Left Center Center-Right Right Total
Likes 1.029326 1.110854 0.948667 0.8790362 0.6452442 1.002449
Comments 0.5204064 1.317479 0.4297106 0.480125 0.6581254 1.014246
pp. 1130–1132, 2015. [Online]. Available: https://www.science.org/doi/
abs/10.1126/science.aaa1160
[2] F. Zollo, A. Bessi, M. Del Vicario, A. Scala, G. Caldarelli,
L. Shekhtman, S. Havlin, and W. Quattrociocchi, “Debunking in a
world of tribes,” PLOS ONE , vol. 12, no. 7, pp. 1–27, 07 2017.
[Online]. Available: https://doi.org/10.1371/journal.pone.0181821
[3] F. Zollo, P. K. Novak, M. Del Vicario, A. Bessi, I. Mozeti ˇc, A. Scala,
G. Caldarelli, and W. Quattrociocchi, “Emotional dynamics in the age
of misinformation,” PLOS ONE , vol. 10, no. 9, pp. 1–22, 09 2015.
[Online]. Available: https://doi.org/10.1371/journal.pone.0138740
[4] K. Garimella, G. D. F. Morales, A. Gionis, and M. Mathioudakis,
“Quantifying controversy on social media,” Trans. Soc. Comput., vol. 1,
no. 1, 1 2018. [Online]. Available: https://doi.org/10.1145/3140565
[5] M. Del Vicario, A. Bessi, F. Zollo, F. Petroni, A. Scala, G. Caldarelli,
H. Stanley, and W. Quattrociocchi, “The spreading of misinformation
online,” Proceedings of the National Academy of Sciences , vol. 113, 01
2016.
[6] M. Cinelli, G. D. F. Morales, A. Galeazzi, W. Quattrociocchi, and
M. Starnini, “The echo chamber effect on social media,” Proceedings
of the National Academy of Sciences , vol. 118, no. 9, p. e2023301118,
2021. [Online]. Available: https://www.pnas.org/doi/abs/10.1073/pnas.
2023301118
[7] R. K. Garrett, “Echo chambers online?: Politically motivated selective
exposure among internet news users,” Journal of computer-mediated
communication, vol. 14, no. 2, pp. 265–285, 2009.
[8] A. Guess, Media Choice and Moderation: Evidence from Online Track-
ing Data. Unpublished Manuscript, 2016.
[9] E. Bakshy, I. Rosenn, C. Marlow, and L. Adamic, “The role of social
networks in information diffusion,” WWW’12 - Proceedings of the 21st
Annual Conference on World Wide Web , 01 2012.
[10] C. R. SUNSTEIN, # Republic: Divided Democracy in the Age of
Social Media, ned - new edition ed. Princeton University Press, 2018.
[Online]. Available: http://www.jstor.org/stable/j.ctv8xnhtd
[11] J. R. Zaller, The Nature and Origins of Mass Opinion , ser. Cambridge
Studies in Public Opinion and Political Psychology. Cambridge
University Press, 1992.
[12] C. Taber and M. Lodge, “Motivated skepticism in the evaluation of
political beliefs,” American Journal of Political Science - AMER J
POLIT SCI, vol. 50, pp. 755–769, 07 2006.
[13] R. R. Lau and D. P. Redlawsk, How Voters Decide: Information
Processing in Election Campaigns , ser. Cambridge Studies in Public
Opinion and Political Psychology. Cambridge University Press, 2006.
[14] B. Nyhan and J. Reifler, “When corrections fail: The persistence of
political misperceptions,” Political Behavior, vol. 32, no. 2, pp. 303–
330, 2010.
[15] H. H. Nam, J. T. Jost, and J. J. Van Bavel, ““not for all the tea in
china!” political ideology and the avoidance of dissonance-arousing
situations,” PLOS ONE , vol. 8, no. 4, pp. 1–8, 04 2013. [Online].
Available: https://doi.org/10.1371/journal.pone.0059837
[16] G. D. Munro, P. H. Ditto, L. K. Lockhart, A. Fagerlin, M. Gready, and
E. Peterson, “Biased assimilation of sociopolitical arguments: Evaluating
the 1996 us presidential debate,” Basic and Applied Social Psychology ,
vol. 24, no. 1, pp. 15–26, 2002.
[17] S. Iyengar, G. Sood, and Y . Lelkes, “Affect, not ideology: A social
identity perspective on polarization,” Public opinion quarterly , vol. 76,
no. 3, pp. 405–431, 2012.
[18] E. Nisbet, K. Cooper, and R. K. Garrett, “The partisan brain,” The
ANNALS of the American Academy of Political and Social Science , vol.
658, pp. 36–66, 02 2015.
[19] P. Barber ´a, J. Jost, J. Nagler, J. Tucker, and R. Bonneau, “Tweeting
from left to right: Is online political communication more than an echo
chamber?” Psychological science, vol. 26, 08 2015.
[20] S. Wu and P. Resnick, “Cross-partisan discussions on youtube: Con-
servatives talk to liberals but liberals don’t talk to conservatives,”
Proceedings of the International AAAI Conference on Web and Social
Media, vol. 15, pp. 808–819, 05 2021.
[21] M. Cinelli, E. Brugnoli, A. L. Schmidt, F. Zollo, W. Quattrociocchi,
and A. Scala, “Selective exposure shapes the facebook news diet,”
PLOS ONE , vol. 15, no. 3, pp. 1–17, 03 2020. [Online]. Available:
https://doi.org/10.1371/journal.pone.0229129
[22] A. Schmidt, F. Zollo, M. Del Vicario, A. Bessi, A. Scala, G. Caldarelli,
H. Stanley, and W. Quattrociocchi, “Anatomy of news consumption on
facebook,” Proceedings of the National Academy of Sciences , vol. 114,
03 2017.
[23] M. Del Vicario, G. Vivaldo, A. Bessi, F. Zollo, A. Scala, G. Caldarelli,
and W. Quattrociocchi, “Echo chambers: Emotional contagion and group
polarization on facebook,” Scientific reports , vol. 6, no. 1, p. 37825,
2016.
[24] A. Bessi, F. Petroni, M. Del Vicario, F. Zollo, A. Anagnostopoulos,
A. Scala, G. Caldarelli, and W. Quattrociocchi, “Homophily and polar-
ization in the age of misinformation,” The European Physical Journal
Special Topics, vol. 225, 10 2016.
[25] ——, “Viral misinformation: The role of homophily and polarization,”

7
in Proceedings of the 24th international conference on World Wide Web,
2015, pp. 355–356.
[26] M. Del Vicario, A. Scala, G. Caldarelli, H. E. Stanley, and W. Quat-
trociocchi, “Modeling confirmation bias and polarization,” Scientific
reports, vol. 7, no. 1, p. 40391, 2017.
[27] J. Cheng, M. Bernstein, C. Danescu-Niculescu-Mizil, and J. Leskovec,
“Anyone can become a troll: Causes of trolling behavior in online
discussions,” in Proceedings of the 2017 ACM Conference on Computer
Supported Cooperative Work and Social Computing , ser. CSCW ’17.
New York, NY , USA: Association for Computing Machinery, 2017,
p. 1217–1230. [Online]. Available: https://doi.org/10.1145/2998181.
2998213
[28] M. Saveski, B. Roy, and D. Roy, “The structure of toxic
conversations on twitter,” in Proceedings of the Web Conference
2021, ser. WWW ’21. New York, NY , USA: Association for
Computing Machinery, 2021, p. 1086–1097. [Online]. Available:
https://doi.org/10.1145/3442381.3449861
[29] C. M. Valensise, M. Cinelli, and W. Quattrociocchi, “The drivers of
online polarization: Fitting models to data,” Information Sciences , vol.
642, p. 119152, 2023.
[30] F. Baumann, P. Lorenz-Spreen, I. M. Sokolov, and M. Starnini, “Mod-
eling echo chambers and polarization dynamics in social networks,”
Physical Review Letters , vol. 124, no. 4, p. 048301, 2020.
[31] F. Cinus, M. Minici, C. Monti, and F. Bonchi, “The effect of people
recommenders on echo chambers and polarization,” in Proceedings of
the International AAAI Conference on Web and Social Media , vol. 16,
2022, pp. 90–101.
[32] L. T. L. Terren and R. B.-B. R. Borge-Bravo, “Echo chambers on social
media: A systematic review of the literature,” Review of Communication
Research, vol. 9, 2021.
[33] A. Salloum, T. H. Y . Chen, and M. Kivel ¨a, “Separating polarization
from noise: Comparison and normalization of structural polarization
measures,” Proc. ACM Hum.-Comput. Interact. , vol. 6, no. CSCW1, 4
2022. [Online]. Available: https://doi.org/10.1145/3512962
[34] M. Del Vicario, F. Zollo, G. Caldarelli, A. Scala, and W. Quattrociocchi,
“Mapping social dynamics on facebook: The brexit debate,” Social
Networks, vol. 50, pp. 6–16, 2017. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0378873316304166
[35] A. L. Schmidt, F. Zollo, A. Scala, C. Betsch, and W. Quattrociocchi,
“Polarization of the vaccination debate on facebook,” Vaccine, vol. 36,
no. 25, pp. 3606–3612, 2018.
[36] M. Falkenberg, A. Galeazzi, M. Torricelli, N. Di Marco, F. Larosa,
M. Sas, A. Mekacher, W. Pearce, F. Zollo, W. Quattrociocchi, and
A. Baronchelli, “Growing climate polarisation on social media,” 12
2021.
[37] A. Schmidt, F. Zollo, A. Scala, and W. Quattrociocchi, “Polarization
rank: A study on european news consumption on facebook,” 05 2018.
[38] A. Galeazzi, A. Peruzzi, E. Brugnoli, M. Delmastro, and F. Zollo, “Un-
veiling the hidden agenda: Biases in news reporting and consumption,”
01 2023.
[39] J. E. Settle, Frenemies: How Social Media Polarizes America . Cam-
bridge University Press, 2018.
[40] L. Mason, Uncivil Agreement: How Politics Became Our Identity .
Chicago: University of Chicago Press.
[41] E. Pariser, The Filter Bubble . Penguin, 2012.
[42] K. Garimella, G. Morales, A. Gionis, and M. Mathioudakis, “Exposing
twitter users to contrarian news,” 03 2017.
[43] S. Rathje, J. J. Van Bavel, and S. Van Der Linden, “Out-group animosity
drives engagement on social media,” Proceedings of the National
Academy of Sciences , vol. 118, no. 26, p. e2024292118, 2021.
[44] C. Bail, L. Argyle, T. Brown, J. Bumpus, H. Chen, M. Hunzaker, J. Lee,
M. Mann, F. Merhout, and A. V olfovsky, “Exposure to opposing views
on social media can increase political polarization,” Proceedings of the
National Academy of Sciences , vol. 115, p. 201804840, 08 2018.
[45] M. Cinelli, G. Etta, M. Avalle, A. Quattrociocchi, N. Di Marco,
C. Valensise, A. Galeazzi, and W. Quattrociocchi, “Conspiracy theories
and social media platforms,” Current Opinion in Psychology, vol. 47, p.
101407, 2022.
[46] S. Gonz ´alez-Bail´on, D. Lazer, P. Barber ´a, M. Zhang, H. Allcott,
T. Brown, A. Crespo-Tenorio, D. Freelon, M. Gentzkow, A. M. Guess,
S. Iyengar, Y . M. Kim, N. Malhotra, D. Moehler, B. Nyhan, J. Pan, C. V .
Rivera, J. Settle, E. Thorson, R. Tromble, A. Wilkins, M. Wojcieszak,
C. K. de Jonge, A. Franco, W. Mason, N. J. Stroud, and J. A. Tucker,
“Asymmetric ideological segregation in exposure to political news on
facebook,” Science, vol. 381, no. 6656, pp. 392–398, 2023. [Online].
Available: https://www.science.org/doi/abs/10.1126/science.ade7138
[47] A. M. Guess, N. Malhotra, J. Pan, P. Barber ´a, H. Allcott,
T. Brown, A. Crespo-Tenorio, D. Dimmery, D. Freelon, M. Gentzkow,
S. Gonz ´alez-Bail´on, E. Kennedy, Y . M. Kim, D. Lazer, D. Moehler,
B. Nyhan, C. V . Rivera, J. Settle, D. R. Thomas, E. Thorson,
R. Tromble, A. Wilkins, M. Wojcieszak, B. Xiong, C. K. de Jonge,
A. Franco, W. Mason, N. J. Stroud, and J. A. Tucker, “Reshares on
social media amplify political news but do not detectably affect beliefs
or opinions,” Science, vol. 381, no. 6656, pp. 404–408, 2023. [Online].
Available: https://www.science.org/doi/abs/10.1126/science.add8424
[48] ——, “How do social media feed algorithms affect attitudes and
behavior in an election campaign?” Science, vol. 381, no. 6656, pp.
398–404, 2023. [Online]. Available: https://www.science.org/doi/abs/
10.1126/science.abp9364
[49] B. Nyhan, J. Settle, E. Thorson, M. Wojcieszak, P. Barber ´a, A. Chen,
H. Allcott, T. Brown, A. Crespo-Tenorio, D. Dimmery, D. Freelon,
M. Gentzkow, S. Gonz ´alez-Bail´on, A. Guess, E. Kennedy, Y . Kim,
D. Lazer, N. Malhotra, D. Moehler, and J. Tucker, “Like-minded sources
on facebook are prevalent but not polarizing,” Nature, vol. 620, pp. 1–8,
07 2023.
[50] “selective exposure.” [Online]. Available: https://www.oxfordreference.
com/view/10.1093/oi/authority.20110803100452931
[51] “Media bias/fact check,” https://mediabiasfactcheck.com.
ACKNOWLEDGMENT
The work is supported by IRIS Infodemic Coalition
(UK government, grant no. SCH-00001-3391), SERICS
(PE00000014) under the NRRP MUR program funded by
the European Union - NextGenerationEU, project CRESP
from the Italian Ministry of Health under the program CCM
2022, PON project “Ricerca e Innovazione” 2014-2020, and
PRIN Project MUSMA for Italian Ministry of University and
Research (MUR) through the PRIN 2022.
