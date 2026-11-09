---
title: Misinformation Regulation in the Presence of Competition between Social Media Platforms (Extended
  Version)
url: https://arxiv.org/abs/2402.09639
category: social-media
subcategory: empirical
date: 2024-02
venue: ''
authors:
- So Sasaki
- Cédric Langbort
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.09639
pages: 13
chars: 64468
fetched_at: '2026-11-08T13:08:54+00:00'
kb_version: 1
---

# Misinformation Regulation in the Presence of Competition between Social Media Platforms (Extended Version)

1
Misinformation Regulation in the Presence of
Competition between Social Media Platforms
(Extended Version)
So Sasaki, C ´edric Langbort
Abstract—Social media platforms have diverse content moder-
ation policies, with many prominent actors hesitant to impose
strict regulations. A key reason for this reluctance could be
the competitive advantage that comes with lax regulation. A
popular platform that starts enforcing content moderation rules
may fear that it could lose users to less-regulated alternative
platforms. Moreover, if users continue harmful activities on other
platforms, regulation ends up being futile. This article examines
the competitive aspect of content moderation by considering the
motivations of all involved players (platformer, news source, and
social media users), identifying the regulation policies sustained in
equilibrium, and evaluating the information quality available on
each platform. Applied to simple yet relevant social networks such
as stochastic block models, our model reveals the conditions for a
popular platform to enforce strict regulation without losing users.
Effectiveness of regulation depends on the diffusive property of
news posts, friend interaction qualities in social media, the sizes
and cohesiveness of communities, and how much sympathizers
appreciate surprising news from influencers.
Index Terms —Content moderation, Network game theory,
Platform competition, Social media
I. I NTRODUCTION
In recent years, social media platforms have significantly
changed their content moderation policies. For instance, Jhaver
et al. [1] reported that Pinterest recently started actively
blocking some search results for controversial or debunked
queries, while Reddit has taken action against certain toxic
communities by banning or quarantining them. Meta/Facebook
has also identified and flagged groups that engage in hate
speech on its platform. Different platforms have implemented
widely varying policies, resulting in different standards for
what is considered acceptable speech. One of the most visible
examples of this was the different treatment of President
Trump’s May 2020 messages by Twitter and Facebook, as
reported by [2] and [3].
The difference in content moderation policies between so-
cial media platforms is likely influenced by a combination
of factors, including each company’s interpretation of §230
of the US Communications Decency Act and the founders’
views on freedom of speech. However, it is also probable that
economic incentives play a role in shaping these policies. In
fact, a platform’s regulation, or lack thereof, can be perceived
as a competitive advantage, as users may choose to switch
to a competitor if they feel that the moderation rules in
place amount to censorship and limit their access to the
Manuscript received January 1, 2023; revised January 2, 2023; accepted
January 3, 2023. This work was supported by an ARO MURI award, under
agreement W911NF-20-1-0252.
S. Sasaki and C. Langbort are with Coordinated Science Laboratory,
University of Illinois at Urbana-Champaign, Urbana, IL 61801 USA (e-mail:
ssasaki2@illinois.edu, langbort@illinois.edu).
news and content they value. This effect can be amplified
in social networking markets, where the positive externalities
of network economics are typically present. As more users
join a particular platform, it becomes even more socially
advantageous for others to join as well, resulting in a winner-
takes-all effect, as has been well documented in the literature,
such as [4]. Such a threat of seeing its users leave en masse
may play a role in reducing a platformer’s interest in policing
misinformation on its network. At the same time, other actors,
such as companies advertising on the network, may value
regulation (e.g., as a form of so-called ’brand safety’ [5],
[6]) and introduce incentives that, in contrast, may push the
platformer towards more oversight.
The aim of this article is to investigate the competitive
nature of content moderation on simplified platform models
by considering the motivations of different players such as
the platform owner, news sources, and social media users.
We purposefully omit the kind of pro-regulation stakehold-
ers mentioned above in this first study. This is because, in
the context of our model, they only make it easier for the
platform to implement strict regulation, and we are interested
in characterizing the most restrictive such policy that can be
sustained in equilibrium.
More precisely, in our model, we examine the effect of reg-
ulation when multiple users and a news source (also referred to
as an influencer or sender) choose platforms to maximize their
individual utility. A user’s utility is determined by their social
interaction payoff and news consumption payoff. Platform
owners have the option to deplatform a deceptive news source
based on their policies. As a result, the news source must
decide whether to comply with the strict regulation of a
popular platform or relocate to an alternative platform to
spread more biased information to a smaller audience.
This study is part of a larger body of research on plat-
form governance, as discussed in reviews [7] and [8]. We
specifically examine how platforms can prevent the spread of
misinformation, such as through the preclusion of accounts.
Twitter account suspension following the 2020 U.S. presiden-
tial election is examined in [9]. Our model also takes into
account how users and news sources react to the regulations.
The way users perceive and interpret content moderation is
studied closely in [10]. Meanwhile, Horta Ribeiro et al. [11]
investigate how moderation policies affect harmful activity in
the wider web ecosystem, and whether this activity becomes
more radicalized on alternative platforms. Additionally, Innes
and Innes [12] examine the intended and unintended conse-
quences of deplatforming interventions, such as the emergence
of “minion accounts” of a banned account.
arXiv:2402.09639v1  [cs.GT]  15 Feb 2024

2
Other recent works concerned with regulation in information
diffusion include [13]–[15], all of which place a heavier em-
phasis on the process underlying dynamic propagation and/or
the formation of opinions. Little research has been conducted,
however, in regard to the intensity of effective regulation that
mainstream platforms can implement without losing users.
Understanding this fundamental aspect can advance our con-
versation on the social responsibilities of tech companies.
This article improves our previous work [16] in that 1)
we give tighter sufficient conditions in the propositions for
simple social network structures and 2) more realistic net-
work structures (finite networks and random networks with
community structures) are investigated. In addition, 3) our
analysis is extended to networks consisting of heterogeneous
users (sympathizers and non-sympathizers). These improve-
ments allow our model to analyze e.g., how regulation should
be adjusted depending on community sizes, in-community
cohesiveness, inter-community structures, and sympathizers
near an influencer.
The rest of the paper proceeds as follows. First, we intro-
duce our model of information diffusion and regulation on a
single platform. Next, we describe the competitive process of
platform migration among the sender and users, and character-
ize the strictest regulation that can be imposed in equilibrium.
We then relate its properties to various network structures.
Lastly, the analysis scope is extended to heterogeneous users.
II. M ODEL
A. News information from sender
The game players are multiple users and a sender, who
choose platform P ∈ {A, B}. The sender’s (respectively user
i’s) choice of platform A or B is denoted as PS (Pi).
The sender’s goal is to persuade as many users as possible
to adopt a specific belief about the state of the world, while
accounting for users’ platform choices and updates of beliefs
in response to its signaling policy. The sender thus acts as a
propagandist, whose decision-making process is best described
using the framework of Bayesian persuasion [17], as is done
in [18].
The world state is represented by a random variable w ∈
{0, 1} with µ = P rob(w = 1) < 1/2. User i estimates the
world state as ai ∈ {0, 1} and gets payoff c if ai = w =
0, payoff 1 − c if ai = w = 1 , or no payoff if ai ̸= w.
The assumption is made that µ < c <1/2, implying that
the user’s optimal estimation is ai = 0 in absence of any
news information. The sender is the only one who can observe
the state of the world, and their objective is to have the user
estimate ai = 1 regardless of the world state. To persuade
users, the sender sends signal s ∈ {0, 1}. However, the choice
of signal is not entirely arbitrary, and the sender selects a
level of deceitfulness, denoted as β ∈ [0, 1]. The signal s is
generated probabilistically, such that P rob(s = 1 |w = 0) =
β, P rob(s = 1|w = 1) = 1. This means that the sender reports
the true news when the state of the world is w = 1 , but
occasionally lies when the world state is unfavorable. User i
in platform P receives the signal with probability of piP, and
then makes their estimation ai based on the sender’s strategy
β and the realized signal s.
Now let us examine the optimal strategy for user i with
respect to their estimation ai. If the user does not receive any
signal, they should choose the default optimal estimation of
ai = 0 . If they receive signal s = 0 , the biased sender is
reporting unfavorable news and the world state is without a
doubt w = 0. However, if they receive signal s = 1, which
could potentially be misleading, a more careful analysis is
needed. In this case, the expected payoff for the user when
choosing ai = 1 is given by
P rob(w = 1|s = 1)(1 − c) = µ µ + (1 − µ)β (1 − c), (1)
while for ai = 0, it is given by
P rob(w = 0|s = 1)c = (1 − µ)β µ + (1 − µ)β c. (2)
Therefore, the user should trust signal s = 1 and select ai =
1 if the sender’s deceitfulness satisfies β ≤ µ(1 − c) (1 − µ)c =: β′.
Otherwise, they should distrust signal s = 1 and select ai = 0.
Overall, the user’s optimal strategy when receiving a signal
is to trust any signal ( ai = s) if β ≤ β′, and to ignore any
signal (ai = 0) otherwise. Therefore, their expected payoff (for
estimating the world state correctly) in platform P is given by
ΨiP =
(
µpiP(1 − c) + (1 − µ)(1 − βpiP)c ifβ ≤ β′
(1 − µ)c ifβ > β′ (3)
We call ΨiP news consumption payoff. The sender’s expected
utility U is the total number of users who choose ai = 1 ,
which can be expressed as
U = E
 P
i ai

= P i(µ + (1 − µ)β)piPi , (4)
if β ≤ β′. Otherwise, the sender fails to persuade the users,
and therefore U = 0.
Before introducing social-network aspects of our model, let
us consider a scenario with only one user and one platform,
A = Pi = PS, and see the implications of the setting so far. If
the sender chooses β ≤ β′, their utility will be U = (µ + (1−
µ)β)piA. Since the utility function increases monotonically
for β ∈ [0, β′], the sender’s optimal strategy is β∗ = β′. They
prefer a deceitful strategy as long as the user trusts them.
Suppose the platform sets a regulation ρA that prohibits
the sender from using a β value greater than ρA. This, for
example, could be done by setting a content moderation guide-
line to de-platform a news source that reports misinformation
often. In the absence of an alternative platform, the sender
must comply with the regulation and restrict their deceitfulness
to the range β ∈ [0, ρA] instead of β ∈ [0, 1], because
a de-platformed sender’s utility would be zero. A relatively
strict regulation ρA < β′ works effectively in reducing the
sender’s optimal strategy β∗ from β′ to ρA, thus improving
the quality of news information on the platform. Conversely, a
loose regulation with ρA ≥ β′ is meaningless, as the sender’s
optimal strategy remains at β∗ = β′.

3
Fig. 1. Illustration of our model. Blue (red) nodes are in platform A (B).
Values below nodes present piPi . Note that user 6 is assumed to receive the
source’s signal with probability p2 (because it is two edges away from it) even
though there are two paths connecting these vertices. See text for details.
B. Social Interaction and Platform Adoption
Users and the sender are connected via an undirected graph,
where edges represent friend relationships. Given choices Pi’s
and PS, this graph induces two subgraphs containing actors
that are on the same platform. We assume that the signal
originating from the sender travels along the edges of the
subgraph corresponding to the sender’s platfom choice and
that user i receives that message with probability piPi = pk
if and only if Pi = PS, and i is k edges away from S in
that subgraph. We call parameter p information diffusiveness.
Works such as [19] have shown that news dissemination
follows tree-like broadcast patterns. To account for this, we
assume that the receiving probability depends on the shortest
path length in the subgraph.
Note that the probability piPi depends on other users’
choices of platforms, and a user in platform Pi ̸= PS does
not receive the signal. See Figure 1 for an illustrated example.
The number of user i’s friends in platform P (i.e., the size of
their neighborhood in the corresponding subgraph) is denoted
by NiP. The payoff derived from social interactions with
these friends is ΦiPi = NiPi bPi, where bP is a parameter,
controlled by P, which determines the reward obtained for
each social interaction in platform P. The value of bP should
be thought of as increasing with every service or feature (e.g.,
Story/Fleet feature, birthday notification...) introduced by the
platform to enhance a user’s experience interacting with peers.
We call bP the quality of social interaction. In real life, some
friends may be more important than others, but the uniform
bP for all neighbors is a typical assumption in the literature
on networked agents’ adoption of a new option with positive
externality (e.g., [20]). All in all, user i’s utility in platform
P is given by
ViP = ΦiP + ΨiP. (5)
Given the sender’s decision on PS and β ∈ [0, β′], user i
should choose Pi such that ViPi ≥ ViP for all P ∈ {A, B}.
We say the users’ choices of platforms are in equilibrium if
this condition is satisfied for all users. A trivial equilibrium is
Pi = PS for all i, but there can be other equilibria.
Since we are interested in situations where a pre-existing,
originally “dominant”, platform (A) imposes regulations in the
presence of a competing one (B), it makes sense to specifically
look for equilibria that occur as the limit of an “adoption
process” carried out by the users. The process is described as
follows. First, the sender chooses PS. Then, from the initial
state with all users in A, users repeatedly update their choices.
In each iteration, users choose Pi = argmax P ViP simul-
taneously, based on other users’ previous choices. Iterations
continue until an equilibrium is reached, if any. We will discuss
the convergence of this process next, noting for now that it is
essentially a fictitious play-iteration (see, e.g., [20]) for the
non-cooperative game played by the users with utilities ViP,
once the sender’s choice is enacted.
Proposition 1. If 1) the social network is acyclic and platform
A provides higher social interaction quality than platform B,
i.e., bA > bB, or 2) the social network is a finite graph, then
the adoption process converges to an equilibrium in a finite
number of iterations.
This is the sole equilibrium we will consider going forward,
when saying that a property holds “at (the) equilibrium.”
Proof. We will prove the result for Condition 1) only, as the
proof for 2) is similar. If PS = A, the initial state is the
equilibrium. So we only need to consider PS = B.
As shown in the Appendix, users can switch from platform
A to B but not from B to A. It is also shown that for an
acyclic graph, user i that switches to platform B at iteration t
is t edges away from the sender and has p(t) iB = pt, where x(t)
denotes the value of x at iteration t. (This implies that such
user i’s neighbor who is t − 1 edges away from the sender has
to switch to B at iteration t − 1. It also implies that if a user k
edges away does not switch to B at iteration k, then the user
and its downstream users do not switch to B forever.)
Suppose user i switches to B at an iteration of sufficiently
large t. Since p(t) iA = 0, p(t) iB = pt, we have Ψ(t) iB < Ψ(t) iA + ϵ for
small ϵ >0. Since user i’s neighbors farther from the sender
are still in platform A and the neighbor closer to the sender
is in B, N (t) iB = 1. Since bB < bA, we have Φ(t) iB < Φ(t) iA if
N (t) iA ≥ 1. Therefore, V (t) iB < V(t) iA if N (t) iA ≥ 1. Since user i
adopts B at iteration t (i.e., V (t) iB ≥ V (t) iA ), this means N (t) iA = 0.
Therefore, user i is a leaf node. Hence, no user switches to B
at iteration τ ≥ t + 1.
III. S TRICTEST EFFECTIVE REGULATION
We now focus on the scenario where platforms have the
ability to regulate the level of deceitfulness of the sender.
Specifically, we assume that platform A enforces a restriction
ρA ∈ [0, 1] on the sender’s choice of β, limiting the range to
[0, ρA]. In contrast, B has no such restriction, i.e., ρB = 1,
and the sender can choose any β ∈ [0, 1] if they choose B.
In practice, such regulation can be implemented if the source
has been present on the platform long enough to enable it to
fact-check its messages over a period of time, thus obtaining
an empirical estimate of β.
Definition 1. Platform A’s regulation ρA is said to be effec-
tive if it decreases the sender’s deceitfulness in platform A

4
at equilibrium. The strictest effective regulation ρSE is the
minimum of effective regulation ρA.
In other words, Definition 1 states that ρA is effective if in
the presence of the constraint β ∈ [0, ρA], (1) the sender stays
in A and (2) the chosen value β∗ is less than if ρA were equal
to 1 (i.e., β∗ < β′). Our primary interest lies in identifying
the strictest effective regulation ρSE . With this regulation, all
users remain in platform A.
Assuming that either condition 1) or 2) in Proposition 1
holds, we let UP be the sender’s expected utility in platform
P. When users take the optimal strategies, the sender considers
UP as a function of β. We denote U ∗ P as the maximum value
of UP for β ∈ [0, ρP].
If the sender chooses platform A, all users should choose
A at the equilibrium. If P i piA < ∞, according to (4),
UA increases linearly with β ∈ [0, min{ρA, β′}]. Thus, the
sender’s optimal level of deceitfulness is β∗ = min{ρA, β′}.
On the other hand, if P i piA = ∞, then U ∗ A = ∞ for any
β ∈ [0, min{ρA, β′}].
This observation allows us to characterize an effective
regulation. Firstly, if ρA ≥ β′, then the regulation has no
impact on the sender’s behavior as the sender would have
chosen a lower level of deceitfulness. In other words, the
regulation is too lenient to be effective. Secondly, if regulation
ρA < β′ satisfies UA(ρA) ≥ U ∗ B, then the sender should
remain in platform A since it would not gain more utility in
platform B. Note that when ρA takes the lowest value that
satisfies the inequality, we have
(µ + (1 − µ)ρA)
X
i
piA = U ∗ B, (6)
where piA corresponds to PS = A. Lastly, if regulation ρA <
β′ satisfies UA(ρA) < U∗ B, then the sender should switch to
B for higher utility. The regulation is too strict, and the sender
would prefer to move to the alternative platform with some of
its followers.
Rearranging these cases from the viewpoint of designing
the strictest effective regulation ρSE in platform A, we have
the following proposition.
Proposition 2. If UA(β′) ≤ U ∗ B, effective regulation does not
exist. If UA(0) > U∗ B, platform A can enforce any strict reg-
ulation effectively, i.e., ρSE = 0. If UA(0) ≤ U ∗ B < UA(β′),
regulation should be moderate and
ρSE = 1 1 − µ  U ∗ BP i piA − µ  , (7)
where piA is for PS = A.
IV. D ISCUSSION OF MODEL ASSUMPTIONS
Having now presented the main features of our model,
and before particularizing its high-level predictions to specific
networks, we are in a good position to discuss its central
assumptions and simplifications in more details.
A. Multiple platforms
The main insights of our model remain relevant in situations
where more than two platforms are competing, with one of
them being initially dominant. In fact, the two-platform model
can be considered as the worst case for this dominant platform
because the key factor of platform competition is the positive
externality. If users can disperse to many alternative platforms,
it is difficult for each one to become competitive against the
dominant one. Therefore, the dominant platform might be able
to enforce stricter regulation.
B. Multihoming
In its current form, our model assumes that users adopt one
platform at a time. In reality, users do not necessarily have to
leave one platform to join another and can, a priori, consume
news and interact with peers on multiple sites contemporane-
ously. If such multihoming occurs, the sender’s departure to
another platform may not necessarily cause users to leave the
dominant one, and the latter can in turn enforce any regulation
without any risk of losing its user base.
However, if user i has a finite time and/or attention budget
to allocate between the various sites they join, and if they do
not explicitly value diversity of platforms, they will de facto
spend all that budget on the platform bringing them highest
utility, i.e., move to P such that ViP ≥ ViP′ for all P′, as we
have assumed in Section III.
C. Sender strategy and multiple senders
Using a similar argument as the one we described for
multihoming, one can contend that users do not have to
get their news from a single source. In turn, if a specific
source leaves the dominant platform, a user can just either
continue relying on other sources or decide to adopt a new
one. For this reasoning to hold, however, it is necessary
that all news sources be seen as substitutable by the users.
Assuming otherwise (as we do) and, in particular, that the news
consumption payoff enters a user’s utility according to (5) thus
implicitly posits that (a) they have already committed to a
specific sender of interest, to the exclusion of all others and,
(b) that this commitment is independent from the messages
sent by the source.
These two points are consistent with the behavior of at least
some categories of social media users, whose main motivations
for following an influencer are “entertainment” and “out of
habit”, as uncovered by recent research in the field of social
media studies [21]. Conditions (a) and (b) are also likely to
hold more generally if the news source has unique features
that make it especially appealing or salient to users, even
before receiving any message from it (e.g., if the source
is a particularly visible public figure or media outlet, or a
charismatic influencers). Another way in which the users’ ex-
ante devotion to the source (encapsulated by (a) and (b))
manifests itself in our model is in the assumption that they
know the parameter β. This could be the result of users having
interacted with the source for a long enough time, and hence
“knowing what to expect” from it, and/or β being one of the
salient features of the source that make it attractive to the
users. This is also consistent with the literature on Bayesian
Persuasion, which has been used before to model interactions
between platforms and news consumers [17], [18], [22]. Note,
however, that users do not necessarily heed the source’s signal
but, rather, use their knowledge of β to interpret the signals

5
they receive.
V. A PPLICATIONS TO PROTOTYPICAL NETWORKS
In this section, we apply the main result of Section sec3
to prototypical network structures. To maintain analytical
tractability and be able to interpret results qualitatively, we
focus on simple network structures with some relevance to
actual social media platforms. In particular, we study linear
networks, star-chain networks, regular trees, and stochastic
block models for the following reasons.
We analyze a linear network as it presents an intuitive
analytical representation of our model. In many social me-
dia settings, news dissemination takes place with a tree-like
hub-spoke structure, often embedded within a larger social
interaction network [19], [23]. A star-chain network is built
on this structure and possesses cohesive blocking clusters, a
crucial element for platform adoption as defined below.
Definition 2. A cluster, or a set of users, has cohesion x if
each member has at least fraction x of their neighbors within
the set. The cohesion of a cluster is the maximum of such x.
Without news consumption payoffs, platform adoption pro-
cess would be governed by cluster cohesion. As shown in [20],
a “blocking cluster,” that has the highest cohesion in a graph
would determine whether the adoption to the whole population
occurs or not. A regular tree network exhibits, in addition
to cohesive blocking clusters, the exponentially spreading
communication feature, making it a good benchmark to gauge
the relative importance of both characteristics (especially when
compared to the star chain).
Large literature (e.g., [24], [25]) has demonstrated that
homophily is encoded in common social networks. Stochastic
block model is a random network suited to express such net-
works with community structures. Analysis of this parameter-
ized random network is useful because players may not know
the exact structure of a large network, and even if they do,
computing exact solutions is prohibitively expensive. Instead,
an approximate solution based on a few primary factors may
be more practical. Coordination games on stochastic block
model have been explored in prior works (e.g., [26], [27]).
A. Linear Network
An infinite linear network has users i = 0 , 1, 2, . . .with
edges between i and i + 1. The news source can send a signal
to user 0. If the sender and user 0, . . . , kare in the same
platform, user k receives a signal with probability pk. We will
use index k instead of i to imply the user is k edges away from
the sender, although k coincides with i in the linear network.
If the sender opts for platform A, all users remain in A
since VkA > VkB. The sender’s utility function is
UA(β) =
∞X
k=0
(µ + (1 − µ)β)pk = µ + (1 − µ)β 1 − p . (8)
If PS = B, some users may switch platforms. Let user K
be the last user who switches to B. We have VkA ≤ VkB for
k ≤ K, and VkA > VkB for k > K, where
VkA = bA + (1 − µ)c,
VkB = bB + µpk(1 − c) + (1 − µ)(1 − βpk)c (9)
for k = K, K+ 1. The sender thus maximizes
UB(β) = PK(β) k=0 (µ + (1 − µ)β)pk (10)
with K satisfying the condition
VK+1,B < bA + (1 − µ)c ≤ VK,B. (11)
It is worth noting that if bA ≤ bB, then K = ∞.
Condition (11) can be rewritten equivalently in two ways,
F (K + 1) < β≤ F (K), (12)
G(β) − 1 < K≤ G(β), (13)
where
F (K) = 1 (1−µ)c

µ(1 − c) − bA−bB pK

,
G(β) = 1 log p log

bA−bB
µ(1−c)−(1−µ)βc

.
(14)
Note that F (K), G(β) are decreasing functions, and the equal-
ities in the conditions hold at the equilibrium. We thus have
U ∗ B = maxK∈N(µ + (1 − µ)F (K)) 1−pK+1 1−p
= maxβ:G(β)∈N(µ + (1 − µ)β) 1−pG(β)+1 1−p . (15)
Using these UA(β) and U ∗ B, the strictest effective regulation
can be designed. In particular, (7) becomes
ρSE = (1 − p)U ∗ B − µ 1 − µ . (16)
The application of Proposition 2 to this situation is illus-
trated in Figure 2. For all subsequent numerical experiments,
we use the following parameter values unless otherwise spec-
ified: µ = 0.2, c= 0.3, p= 0.9, bA − bB = 0.01. (The value
of µ does not affect the claims of this article qualitatively,
and we will study different values of the other parameters in
the following sections.) When the sender chooses platform B,
the utility attains maximum U ∗ B at β = β∗ B. If the sender
selects β > β∗ B, the signal is biased towards the sender’s
preference, but few users move to B due to the poor news
quality. If β < β∗ B, many users switch to B to follow the
sender, but the signal is not biased in favor of the sender.
On the other hand, when the sender chooses A, all users
remain in the platform. The sender’s utility, UA, increases
for β ≤ min{ρA, β′}, and therefore achieves the maximum
value at β = min{ρA, β′}. Proposition 2 indicates, with these
parameters, the strictest effective regulation is ρSE such that
UA(ρSE ) = U ∗ B. If platform A enforces a stricter regulation
ρA < ρSE , then the sender’s utility becomes lower than in
B. In other words, the sender would rather send more biased
information to fewer people in the alternative platform than
comply with the regulation to gain more potential receivers,
and thus platform A would lose some users. On the other
hand, regulation ρA ∈ [ρSE , β′] works effectively, making the
sender less deceptive, and the platform does not lose any users.
We will now inspect for what bA, bB, p, platform A can
enforce the strict regulation ρA = 0. Our previous work [16]
proved a sufficient condition for ρSE = 0:
Proposition 3. [16] For an infinite linear network, if bA −
bB > µ(1 − c) or bA − bB > µ(1 − c)2/p, then the strictest
effective regulation is ρSE = 0.

6
Fig. 2. The sender’s expected utility in a linear network
We will improve this proposition with a tighter bound.
Let bA ≥ bB ≥ 0. Suppose that the sender chooses B.
At the equilibrium, the sender’s best strategy satisfies β∗ B =
F (K). The strictest effective regulation ρSE takes the value
of zero if and only if UA(β = 0) ≥ UB(β∗ B), i.e.,
∞X
k=0
µpk ≥
KX
k=0
(µ + (1 − µ)β∗ B)pk, (17)
or
bA − bB ≥ µpK − µcpK 1 − pK+1 =: fK(p). (18)
Therefore, using fK(p) defined here, we have the following.
Proposition 4. For an infinite linear network, the strictest
effective regulation is ρSE = 0 if bA − bB ≥ maxK fK(p).
In Figure 3(a), the strictest effective regulation is calculated
for different p and bA, fixing bB = 0. The white curve presents
bA = maxK fK(p)+ bB as in Proposition 4. Above this curve,
platformer A can enforce any regulation without losing users.
We now consider a finite linear network with users
0, 1, . . . , n− 1. Note that K does not take the value of n − 2
since user n − 1 always chooses the same platform as user
n − 2. Following the argument in Appendix, we let
fn,K (p) := µpK − (1 − pn) µcpK 1−pK+1 for K < n− 2
fn,n−2(p) := µ(1 − c)pn−2 for K = n − 1.
Then Proposition 4 becomes
Proposition 5. For a finite linear network, the strictest
effective regulation is ρSE = 0 if bA − bB ≥
maxK=0,1,...,n−2 fn,K (p).
Panel (d) in Figure 3 shows the strictest effective regulation
for a finite linear network. As a rule, and as is evident from the
figure, in the case of linear networks, platform A can impose
any regulation on the sender as long as its quality of social
interaction is sufficiently larger than that of platform B.
B. Star-chain Network
In this section, we consider a star-chain network, where hub
user k has r − 1 leaf nodes and two hub users k − 1, k+ 1
as their neighbors. The news source sends the signal to hub
user 0. The cohesion of blocking clusters is r r+1. If hub users
0, 1, . . . , kare in the same platform as the sender, hub user k
receives the signal with probability pk (and their leaf nodes
receive with probability pk+1).
The news source’s utility in platform A is
UA(β) =
∞X
k=0
(µ + (1 − µ)β)(pk + (r − 1)pk+1). (19)
Suppose the sender chooses platform B. Let K be defined
as an integer such that at the equilibrium, hub user k ≤ K
chooses platform B and hub user k > Kchooses A. Note that
a peripheral user must always follow their hub user’s choice
of platform. The sender in B maximizes their expected utility
UB(β) = PK(β) k=0 (µ + (1 − µ)β)(pk + (r − 1)pk+1) (20)
subject to 1
VK+1,B < rbA + (1 − µ)c ≤ VK,B. (21)
Unlike linear network cases, even if the social interaction
quality in platform A is lower than B, users may prefer the
former as it enables them to communicate with many friends.
Indeed, Proposition 4 becomes
Proposition 6. For an infinite star chain, the strictest effective
regulation is ρSE = 0 if rbA − bB ≥ maxK fK(p).
The proof follows the same argument as the linear network.
The proposition indicates that platform A needs relatively low
quality of social interactions to enforce strict regulations when
hub users have many peripheral users. This is because users
with many friends have high inertia to switch platforms. Since
users have more friends in platform A and higher incentive
to stay there, the dominant platform has more power to
affect players’ behaviors. The higher the cohesion of blocking
clusters is, the easier it becomes to enforce strict regulations.
Panel (b) in Figure 3 presents numerical results for r =
2, bB = 0 . Compared to panel (a), the white curve is lower
in the (p, bA)-plane, and the dark area is larger in this panel.
This means that platform A is more capable of enforcing the
strict regulation ρA = 0 than in the linear network case.
For a finite star-chain with n hub users, the counterpart of
Proposition 5 also holds with some modification. 2 Letting
gn,K (p) := µpK − (1 − pn) µcpK 1 − pK+1 (22)
for K ≤ n − 1, Proposition 5 becomes
Proposition 7. For a finite star chain, the strictest ef-
fective regulation is ρSE = 0 if rbA − bB ≥
maxK=0,1,...,n−1 gn,K (p).
Panel (e) in the figure presents the result for n = 5.
C. Regular Tree Network
In an r-regular tree network, each user is connected to r
child nodes. The news source sends the signal to the root node
(user 0). The blocking cluster cohesion is r r+1 like for the star-
chain network, but as the distance from the sender increases,
the number of users grows exponentially. If users 0, 1, . . . , k
1For hub user k = K, K+ 1, consider
VkA = rbA + (1− µ)c,
VkB = bB + µpk(1 − c) + (1− µ)(1 − βpk)c.
2The farthest hub user can stay at platform A even when the other hub users
are in B, while in a finite linear network, the farthest user always chooses
the same platform as the second farthest user.

7
Fig. 3. The strictest effective regulation ρSE in (a) linear network, (b) star-chain network, and (c) regular-tree network. Respectively, (d), (e), (f) are the
finite cases. In panel (a), the white curve is computed using the formula of Proposition 4. From this proposition, the strictest effective regulation is guaranteed
to be ρSE = 0 above this curve in the (p, bA)-plane. The orange curve plays the same role, but based on the results of Proposition 3. The color map is
computed by (15) and Proposition 2. The white/orange curves and color maps in other panels are computed similarly.
along a path are in the same platform as the sender, then the
probability that user k receives the signal is pkPk = pk.
In platform A, the sender’s expected utility is
UA(β) = P∞ k=0(µ + (1 − µ)β)pkrk. (23)
The sender in platform B maximizes the utility
UB(β) = PK(β) k=0 (µ + (1 − µ)β)pkrk (24)
subject to condition (21). Proposition 6 holds when replacing
function fK by hK,
hK(p) := µpK − µcpK 1 − (pr)K+1 . (25)
In addition, we can show the following.
Proposition 8. For an infinite regular tree, if rbA > bB and
pr >1, then ρSE = 0.
Proof. When pr > 1, the expected number of users who
receive the sender’s signal is infinite. On the other hand, with
rbA > bB, at most finite users move to platform B. Therefore,
the sender’s utility is infinity in platform A and finite in
B. By Proposition 2, since UA(0) > U∗ B, the sender should
always choose platform A. Any strict regulation thus works
effectively, i.e., ρSE = 0.
When a signal is diffusive, even lower quality of social
interaction is sufficient for strict regulation because of expo-
nentially many potential receivers. Distant users are relatively
important to the sender, and the dominant platform becomes
powerful. As long as the social interaction quality satisfies
rbA > bB, platform A can enforce any regulation if the
signal’s reproduction rate rp is greater than one. Lower degree
trees require higher p for strict regulation.
Panel (c) in Figure 3 shows the strictest effective regulation
for r = 2, bB = 0. In the regular tree (c) and the star chain (b),
platform A is more capable of enforcing strict regulation than
in the linear network (a), due to cohesive blocking clusters. In
the regular tree (c), platform A is even more capable than in
the star chain (b) due to the number of the potential receivers.
If p >1/r, a regular tree has ρSE = 0 for any bA ≥ 0.
The finite case follows the same argument as Proposition 5.
Let
hn,K (p) := µpK − (1 − (pr)n) µcpK 1−(pr)K+1 for K < n− 2,
hn,n−2(p) := µ(1 − c)pn−2 for K = n − 1.
Proposition 9. For a finite regular tree, the strictest ef-
fective regulation is ρSE = 0 if rbA − bB ≥
maxK=0,1,...,n−2 hn,K (p).
Note that Proposition 8 does not hold since the signal does
not spread to infinitely many users. Panel (f) shows the result
for a finite tree truncated at the fifth generation.
D. Stochastic Block Model
A stochastic block model is a random graph with M
communities. Community J ∈ {1, . . . , M} has nJ users, and a
pair of users in communities J, J′ are friends with probability
θJJ ′ ∈ [0, 1].
To provide analytical expressions, we restrict our study to
stochastic block models on which the platform reallocation
process satisfies the few assumptions mentioned below.
Assumption 1. If a user moves to platform B, then the other
users in the same community do so too.
While this assumption may appear restrictive, we show
through numerical simulations in Appendix that it is satisfied
for some stochastic block models when θJJ is close to one.
Assumption 2. Communities move to platform B in the order
of community 1, 2, . . . , M(if they relocate).
We restrict our attention to network structures such that
we can estimate the order of migration. Such network class

8
Fig. 4. The strictest effective regulation ρSE for (a1, a2) community chains and (b1, b2) complete graphs of communities. The community chain has a
middle community of (a1) low or (a2) high intra-community tightness. Parameter values are as described in the main text. The color map is the simulation
results of 50 random graphs. The white curves calculated by Proposition 10 fit the results of the simulation, which does not use Assumptions 1–3 for the
proposition. The dashed curves represent the base case with medium intra-community tightness (see Figure 6 panel (b)). With high p, platform A can enforce
strict regulation more easily (i.e., the white curve is lower) in (a2) than (a1). For the complete graphs of communities, the sender is in a (b1) small or (b2)
large community. The white curves calculated by Proposition 10 again fit the color maps (the simulation results for 50 random graphs), which are computed
without Assumptions 1–3 for the proposition. With low p, platform A can enforce strict regulation more easily in (b2) than (b1).
includes various community structures, for instance a chain, a
star graph, and a complete graph of communities as we will
see in the following subsections.
Assumption 3. Friendship across communities is rare (i.e.,
θJJ ′ ≈ 0, J ̸= J ′), and the first-relocating user in a
community has a single friend in the precedingly-relocated
communities.
The argument can be naturally extended to more connected
first-relocating users, provided that the number of such exter-
nal friends, not necessarily one, is known to us. Define user
ϕ(J) as the first (potentially) relocating user in community J.
The following proposition is derived in the Appendix.
Proposition 10. Under Assumptions 1–3, the strictest effective
regulation is ρSE = 0 if
nJ θJJ bA − bB ≥ µ(1 − c)pϕ(J)B −
PM
L=J+1 RL
PJ
L=1 RL
µcpϕ(J)B.
for all J = 1, . . . , M, where RJ denotes the expected number
of signal receivers in community J when the community is in
the same platform as the sender.
Proposition 10 emphasizes the role played by pϕ(J)B and
RJ in enabling the platformer to apply regulation ρSE = 0.
These aggregate numbers can further be related to the basic
structure and characteristics of the network if, e.g., they satisfy
particular scaling laws. In that case, Proposition 10 can be used
to gauge the effect of such parameters as well.
1) Community-chain-type Scaling
Our first example is pϕ(J)B and RJ decaying with J
according to
pϕ(J)B =
(
p J = 1
p2J−2 2 ≤ J ≤ M,
RJ = nJ p2J−1.
(26)
As explained heuristically in the Appendix, such a scal-
ing can be achieved in a so-called “chain of communities”
network. Numerical simulations also presented in Appendix
seem to indicate that Assumptions 1–3 hold for these networks
when the intra-community tightness (i.e., probability θJJ ) is
high, which makes them good representatives of the class
of networks for which (26) holds and Proposition 10 is
applicable. Note that this is all that is needed of the network
to perform our analysis.
For example, consider a base model with n1 = n2 = n3 =
30 and θJJ ′ given by
θ =


3
4
4
900 0 4
900
3
4
4
900
0 4 900 3 4

 . (27)
We utilize Proposition 10 to analyze how the regulation de-
pends on the in-between community’s “tightness.” For variants
of the basic parameter sets, instead of θ22 = 3/4 for the second
community, we consider θ22 = 1/2 (case (a1)) and θ22 = 1
(case (a2)).
Figure 4 shows the strictest regulation ρSE for these
networks. The simulation does not use Assumptions 1-3 a
priori, which Proposition 10 is based on. The white curves
indicate that our mathematical analysis of Proposition 10 fits
the simulation results (the color map) of the corresponding
physical model. In particular, with high p, platform A can
enforce strict regulation more easily for (a2), featuring a tightly
connected intermediate community, than for (a1), which con-
tains a loosely connected one. This is in agreement with
our qualitative understanding. When p is high, the sender’s
influence on distant users becomes relatively important. Since
a tightly connected intermediate community blocks their plat-
form migration, it helps platform A hold more power to
impose regulation.
2) Community-star-type Scaling
Another example is given by pϕ(J)B and RJ that, in
contrast, do not decay with J:
pϕ(J)B =
(
p J = 1
p2 2 ≤ J ≤ M,
RJ =
(
n1p J = 1
nJ p3 2 ≤ J ≤ M.
(28)
As explained again in the Appendix, such scalings can be
obtained for a star and a complete graph of communities (while
satisfying Assumptions 1–3), when the sender is in community

9
1 and θ1J > 0 for all J = 2 , . . . , M. We assume, without
loss of generality, n2θ22 ≤ n3θ33 ≤ . . .≤ nM θM M. This
implies that the sender can attract the first users in community
2, . . . , J− 1 more easily than community J since they have
less friends within community. Assumption 2 is thus satisfied.
Simulations are conducted for complete graphs of commu-
nities with the sender at different communities. The model has
four communities. In one simulation setting, the sender is in
a small community, and n1 = 20, n2 = 30, n3 = 40, n4 = 50.
In another, the sender is in a large community, and n1 =
50, n2 = 20, n3 = 30, n4 = 40. The other parameters are
θ =


3
4
4
n1n2
4
n1n3
4
n1n4
4
n2n1
3
4
4
n2n3
4
n2n4
4
n3n1
4
n3n2
3
4
4
n3n4
4
n4n1
4
n4n2
4
n4n3
3
4

 (29)
so that the network structure itself remains identical in the two
settings.
In Figure 4 (b1, b2), the white curves indicate that our math-
ematical analysis of Proposition 10 is again consistent with the
simulation results, which do not presume the Assumptions 1–
3. With low p, platform A can enforce strict regulation more
easily if the sender is in a large community (panel (b2)) than
if it is in a small one (panel (b1)). This goes along with our
qualitative intuition. When p is low, the sender’s influence on
nearby agents becomes relatively important. Since it is difficult
for the sender to persuade a large community into platform B,
platform A can take advantage of this to impose regulation.
VI. I NFLUENCER AND NEIGHBORING SYMPATHIZERS
The previous section demonstrated how the strictest effec-
tive regulation is affected by network structure. In particular,
we saw how the presence of cohesive clusters can preclude
new platform adoption (and hence help the platformer impose
stricter regulation), and how the location of pivotal users
(who determine the power balance between the sender and the
platformer) changes depending on information diffusiveness.
In this section, we consider yet another effect, namely
heterogeneity in the users’ preference for their received signal.
More precisely, from now on, we assume users differ in how
much they appreciate the news information received from the
sender and in how biased they are toward unorthodox views.
This is captured by the payoff ci of user i (replacing the
common value c used up to now). A user with low ci gets
high utility when they correctly estimate the surprising world
state, i.e., ai = w = 1. User i with high ci gets high utility
when they correctly estimate the unsurprising world state, i.e.,
ai = w = 0. Therefore users with low ci, having high β′, tend
to trust a deceitful sender and bet on the unlikely world state.
Note that with the standing assumption of 0 < µ < ci < 1/2,
their default estimation is still ai = 0. We call users with low
ci sympathizers, and high ci non-sympathizers.
A. Sympathizers in Linear Network
For an infinite linear network, our previous arguments can
be reused with minor modifications. with c replaced by ck.
Therefore, a counterpart of Proposition 4 holds, replacing
function fK in (18) with
˜fK(p) := µpK − µcKpK 1 − pK+1 . (30)
In the simulation for an infinite linear network, three users
close to the sender are sympathizers with ci = 0.21, i= 0, 1, 2,
and the rest are non-sympathizers with ci = 0.4, i≥ 3. For the
purpose of comparison, simulation is conducted also for the
opposite pattern, ci = 0.4, i= 0, 1, 2, and ci = 0.21, i≥ 3. As
can be seen in Figure 5 (a), it is more difficult (compared to
the homogeneous case) for the platformer to impose strict reg-
ulation when the users closest to the sender are sympathizers
and p is low. This can be understood intuitively by noting that,
when information is not diffusive, nearby users are relatively
important for the sender to decide its strategy, and therefore
the nearby sympathizers give it greater power.
When the information is diffusive, on the other hand, users
far from the sender are relatively important, and therefore the
sender needs to be more truthful to please the distant non-
sympathizers (and, hence, the solid curves dips below the
dashed on for large p in Figure 5 (a)).
The pattern observed in panel (a) is reversed in (c), as
sympathizers become helpful to the sender when p is high.
B. Community of Sympathizers
For stochastic block models, we consider that users in the
same community have the same payoff, but that different
communities have different payoffs. With a slight abuse of
notation, let cJ denote the payoff parameter for community
J. Then, the counterpart of Proposition 10 holds as follows.
Proposition 11. Under Assumptions 1–3, the strictest effective
regulation is ρSE = 0 if
nJ θJJ bA − bB ≥ µ(1 − cJ )pϕ(J)B −
PM
L=J+1 RL
PJ
L=1 RL
µcJ pϕ(J)B
for all J = 1, . . . , M.
Simulation is conducted for the previous model of commu-
nity chain, n1 = n2 = n3 = 30 and (27). The basic model
has cJ = 0.3 for all J = 1, 2, 3. Keeping all other parameters
fixed, a variant model has c1 = 0.21, meaning that the sender
is in a community of sympathizers. For comparison, another
variant has c1 = 0.4, corresponding to non-sympathizers in the
sender’s community. Figure 6 indicates that in the case that
the sender has sympathizers nearby, it is difficult for platform
A to enforce strict regulation when p is low. In the case
that non-sympathizers are nearby, on the other hand, platform
A can enforce strict regulation easily when p is low. Like
linear network cases, when the information is not diffusive,
the nearby users are relatively important for the sender to
decide its strategy, and therefore the nearby sympathizers (non-
sympathizers) bring advantage (disadvantage) to the sender.
VII. D ISCUSSION AND CONCLUSION
This article provided a novel perspective on the design
of regulation policies that a dominant platform can enforce
without reducing its user base, thus shedding light on the the-
oretical efficacy of such misinformation-mitigation measures,
and the responsibility of mainstream platforms.
More precisely, we identified the strictest level of regulation
a platform can enforce on an information source without

10
Fig. 5. The strictest effective regulation ρSE for infinite linear networks. Panel (b) is the basic case with ci = 0.3 for all i. For panel (a), users close to
the sender are sympathizers ( ci = 0.21 for i = 0, 1, 2) and distant users are non-sympathizers ( ci = 0.4 for i ≥ 3). Panel (c) is the opposite ( ci = 0.4 for
i = 0, 1, 2 and ci = 0.21 for i ≥ 3). The white curves are the parameter threshold for ρSE = 0 as in Proposition 4, and the dashed curves represent that in
the base case (b) for reference. In case (a), it is difficult for platform A to enforce strict regulation (i.e., the color map is bright and the white curve is high)
when p is low. The color map is computed similarly to Figure 3, not using any random procedure.
Fig. 6. The strictest effective regulation ρSE for a community chain. Panel (b) is the basic case with cJ = 0.3 for all J = 1, 2, 3. For panel (a), users in
the sender’s community are sympathizers ( c1 = 0.21) and distant users are the same as the basic case ( c2 = c3 = 0.3). Panel (c) has non-sympathizers
nearby ( c1 = 0.4 and c2 = c3 = 0.3). The color map shows the simulation result for 50 samples of the random graph. The white curves are the parameter
threshold for ρSE = 0 as in Proposition 10, and the dashed curves represent that in the base case (b) for reference. In case (a), it is difficult for platform A
to enforce strict regulation (i.e., the color map is bright and the white curve is high) when p is low.
losing users to a non-regulated competitor. We focused on
simple yet relevant network structures, such as stochastic block
models, and used the model to make predictions in a variety
of scenarios. In particular, we showed that a tightly connected
community prevents new platform adoption thereby helping
the currently dominant platform impose strict regulation, es-
pecially if the information is diffusive. We also showed that
a news source in a large community tends to comply with
strict regulation in the popular platform if the information is
not diffusive, while a news source in a small community is
more likely to relocate to an alternative platform. Finally, a
news source surrounded by sympathizers who appreciate the
information it emits exerts a greater indirect influence over
the platform’s content moderation policy than one surrounded
by non-sympathizers. However, when information is diffusive,
this effect diminishes, allowing the platform to enforce stricter
regulations.
APPENDICES
A. Lemmata for Proposition 1
Lemma 1. Suppose PS = B. In the adoption process, users
can switch from platform A to B but not from B to A.
Proof. We show by induction. Suppose this statement is true
at iteration t. Then, for each user i, the number of neighbors
in platform A (resp. B) decreases (increases) or stays the
same. This means Φ(t) iA ≥ Φ(t+1) iA , Φ(t) iB ≤ Φ(t+1) iB . Also, p(t) iB ≤
p(t+1) iB because the shortest path in the subgraph for platform
B does not become longer. This means Ψ(t) iB ≤ Ψ(t+1) iB . Note
that p(t) iA = p(t+1) iA = 0 and therefore Ψ(t) iA = Ψ (t+1) iA . Hence,
V (t) iA ≥ V (t+1) iA and V (t) iB ≤ V (t+1) iB . Therefore, if V (t) iB ≥ V (t) iA ,
then V (t+1) iB ≥ V (t+1) iA . This means if a user chooses B at
iteration t, then chooses B at iteration t + 1 too. By induction,
the statement is true at any iteration.
Lemma 2. Suppose PS = B and the network is acyclic. User
i that switches to platform B at iteration t is t edges away
from the sender and has p(t) iB = pt.
Proof. We show by induction. Suppose the statement is true
for 1, 2, . . . , t.
Let St be the set of users who switched to B at iteration
t. Since the graph is acyclic, each user has only one neigh-
bor upstream (closer to the sender) and the other neighbors
downstream (farther from the sender). Therefore, the upstream
neighbors of St is already in B at iteration t (otherwise,
p(t) iB = 0 for i ∈ St, which contradicts the assumption).
Therefore, the platform adoption of St affects NjP only if
user j is a downstream neighbor of St or is already in B.
By assumption, all users more than t edges away from the
sender are in A at iteration t. Therefore, the platform adoption
of St affects pjB only if user j is a downstream neighbor of
St.
Therefore, the platform adoption of St affects VjP only if
user j is a downstream neighbor of St or is already in B.
Therefore, if a user switches to B at iteration t + 1, then it is

11
a downstream neighbor of St. A downstream neighbor of St
is t + 1 edges away from the sender and has p(t+1) iB = pt+1.
By induction, the statement holds for any t.
B. Finite Linear Network
We have
UA(β) =
n−1X
k=0
(µ + (1 − µ)β)pk,
UB(β) =
KX
k=0
(µ + (1 − µ)β)pk
(31)
with K < n− 2 satisfying
VK+1,B < bA + (1 − µ)c ≤ VK,B (32)
or K = n − 1 if bA + (1− µ)c ≤ Vn−2,B. For the best strategy
in platform B, the sender takes β∗ B = F (K) for K < n− 2
and β∗ B = F (n − 2) for K = n − 1.
The strictest effective regulation ρSE takes the value of zero
if and only if UA(β = 0) ≥ UB(β∗ B), i.e.,
n−1X
k=0
µpk ≥
KX
k=0
(µ + (1 − µ)F (K))pk for K < n− 2
n−1X
k=0
µpk ≥
n−1X
k=0
(µ + (1 − µ)F (n − 2))pk for K = n − 1.
This leads to Proposition 5.
C. Derivation of Proposition 10
Suppose the sender chooses platform B. The critical situ-
ation for community J’s platform adoption is that the first-
adopting user ϕ(J) chooses a platform when a friend from
community 1, . . . , J− 1 is in platform B and other friends in
community J are in A. This user compares
Vϕ(J)A = nJ θJJ bA + (1 − µ)c and
Vϕ(J)B = bB + µpϕ(J)B(1 − c) + (1 − µ)(1 − βpϕ(J)B)c.
Hence, users in community J chooses B if β ≤ βJ where
βJ := 1 (1 − µ)c  µ(1 − c) − nJ θJJ bA − bB pϕ(J)B  . (33)
This βJ is the sender’s best strategy assuming that commu-
nities 1, . . . , Jare in platform B and J + 1, . . . , Mare in
A at equilibrium. Then, the strictest effective regulation ρSE
satisfies UA(ρSE ) ≥ UB(βJ ), i.e.,
(µ + (1 − µ)ρSE )
MX
L=1
RL ≥ (µ + (1 − µ)βJ )
JX
L=1
RL. (34)
Plugging in ρSE = 0 and the value of βJ, we obtain the
following necessary and sufficient condition forρSE = 0 at the
equilibrium where communities 1, . . . , J− 1 are in Platform
B and the rest are in A:
nJ θJJ bA − bB ≥ µ(1 − c)pϕ(J)B −
PM
L=J+1 RL
PJ
L=1 RL
µcpϕ(J)B.
Considering all possible assignments of communities to
platforms at equilibrium, we achieve Proposition 10.
D. Numerical Validation of Assumption 1
To justify Assumption 1 for Proposition 10, we conduct
simulations, taking community chains and complete graphs of
communities for example.
For variants of the base model of community chain ( n1 =
n2 = n3 = 30 and (27)), instead of θJJ = 3/4, we consider
θJJ = 1 /4, 1/8, 1/16. Figure 7 shows the number of users
who choose platform B when platform A sets too strict
regulation ρA < ρSE . For a large θJJ , the number of users in
platform B is 0, 30, 60, or 90, indicating that all users in a
community choose the same platform. On the other hand, for
a small θJJ , users in a community do not necessarily choose
the same platform. The simulation result is for a single sample
for the random networks.
Similar results are achieved in simulation for the complete
graph of communities.
To discuss this property of community migration, we in-
troduce new metrics. Let N (J, P) be the number of users
in community J who choose platform P. Then, define the
number of users’ irregular choices as
MX
J=1
min{N (J, A), N(J, B)}. (35)
This takes the value of zero when all users in each community
choose the same platform, and the maximum value P J nJ /2
when half users in each community choose a platform different
from the other half.
Figure 8 presents the number of users’ irregular choices. The
simulation is conducted for 50 samples, fixing p = 0 .7 and
bA = 0.002. As in Figures 7, the results consistently indicate
that when users are tightly connected within community (i.e.,
θJJ is high), all users in a community choose the same
platform. This simulation result supports Assumption 1 for
Proposition 10.
E. Community Structures Applicable to Proposition 10
1) Community Chain
The chain of communities is introduced as a physical model
that satisfies (26).
Heuristically, a possible way to obtain such a scaling is by
considering a community chain with
θJJ ≈ 1, (36)
nJ θJJ ′ < 1 < nJ nJ ′θJJ ′ for J ′ = J − 1, J+ 1, (37)
nJ nJ−1θJJ −1nJ+1θJJ +1 < 1. (38)
Roughly speaking, (36) means that most user pairs in the same
community are friends; (37) means that although communities
are connected, most users do not have friends in other com-
munities; (38) means that in most cases, no user in community
J has friends both in community J − 1 and community J + 1.
Under these conditions, it should be intuitive that most users
are two edges away from the nearest neighbor in an adjacent
community, thus leading to (26).
Assumption 1 is validated for (36) in simulation in Ap-
pendix D. The chain structure of the network guarantees
Assumption 2, and Assumption 3 is satisfied due to (37).

12
Fig. 7. The number of users who choose platform B when platform A imposes too strict regulation ρA < ρSE . The network is a community chain. For a
large θJ J, the number of users in platform B is 0, 30, 60, or 90, indicating that all users in a community choose the same platform. On the other hand, for
a small θJ J, users in a community do not necessarily choose the same platform.
Fig. 8. The number of users’ irregular choices. The value of 0 means that
all users in a community choose the same platform.
2) Star/Complete Graph of Communities
In order to obtain (28), consider a stochastic block model
with the sender in community 1 and θ1J > 0 for all J =
2, . . . , M. In addition to (36), we assume
n1θ1J < 1, nJ θ1J < 1, n1nJ θ1J > 1, (39)
θJJ ′ ≈ 0 for J ̸= 1, J′ ̸= 1, J̸= J ′. (40)
Equation (39) means that in most cases, a user in community
J (resp. 1) does not have friends in community 1 (resp.
J), but there are some inter-community links between 1
and J. Equation (40) means that edges between peripheral
communities do not exist or are negligible. These assumptions
indicate that the first-adopting user ϕ(J) in community J ≥ 2
is two-edges away from the sender and most others are three-
edges away; hence (28).
Assumption 1 is validated for (36) in simulation in Ap-
pendix D. Assumption 2 is satisfied because n2θ22 < n3θ33 <
n4θ44. The combination of (39) and (40) satisfies Assumption
3.
REFERENCES
[1] S. Jhaver, C. Boylston, D. Yang, and A. Bruckman, “Evaluating the
effectiveness of deplatforming as a moderation strategy on twitter,”Proc.
of the ACM on Human-Computer Interaction , vol. 5, no. CSCW2, pp.
1–30, 2021.
[2] T. Romm and E. Dwoskin, “Twitter adds labels for tweets that break its
rules - a move with potentially stark implications for trump’s account,”
Washington Post, 2019.
[3] S. Vaidhyanathan, “Facebook and the folly of self-regulation,” WIRED,
2020.
[4] C. Shapiro and H. R. Varian, Information Rules: A Strategic Guide to
the Network Economy . Boston: Harvard Business School Press, 1999.
[5] R. Devaux, “Should i stay or should i go? platform advertising
in times of boycott,” Preprint, 02 2023. [Online]. Available:
https://www.researchgate.net/publication/368386572 Should I Stay
or Should I Go Platform Advertising in Times of Boycott
[6] L. Madio and M. Quinn, “User-generated content, strategic moderation,
and advertising,” Preprint, vol. 2, 2020.
[7] J. Rietveld and M. A. Schilling, “Platform competition: A systematic
and interdisciplinary review of the literature,” Journal of Management ,
vol. 47, no. 6, pp. 1528–1563, 2021.
[8] R. Gorwa, “What is platform governance?” Information, Communication
& Society, vol. 22, no. 6, pp. 854–871, 2019.
[9] F. A. Chowdhury, D. Saha, M. R. Hasan, K. Saha, and A. Mueen,
“Examining factors associated with twitter account suspension following
the 2020 us presidential election,” in Proc. of the 2021 IEEE/ACM
International Conference on Advances in Social Networks Analysis and
Mining, 2021, pp. 607–612.
[10] S. Myers West, “Censored, suspended, shadowbanned: User interpreta-
tions of content moderation on social media platforms,” New Media &
Society, vol. 20, no. 11, pp. 4366–4383, 2018.
[11] M. Horta Ribeiro, S. Jhaver, S. Zannettou, J. Blackburn, G. Stringhini,
E. De Cristofaro, and R. West, “Do platform migrations compromise
content moderation? evidence from r/the donald and r/incels,” Proc. of
the ACM on Human-Computer Interaction , vol. 5, no. CSCW2, pp. 1–
24, 2021.
[12] H. Innes and M. Innes, “De-platforming disinformation: conspiracy
theories and their control,” Information, Communication & Society , pp.
1–19, 2021.
[13] V . Tzoumas, C. Amanatidis, and E. Markakis, “A game-theoretic analy-
sis of a competitive diffusion process over social networks,” in Internet
and Network Economics: 8th International Workshop, WINE 2012,
Liverpool, UK, December 10-12, 2012. Proceedings 8 . Springer, 2012,
pp. 1–14.
[14] Y . E. Bayiz and U. Topcu, “Countering misinformation on social
networks using graph alterations,” arXiv preprint arXiv:2211.04617 ,
2022.
[15] L. Damonte, G. Como, and F. Fagnani, “Targeting interventions for
displacement minimization in opinion dynamics,” in 2022 IEEE 61st
Conference on Decision and Control (CDC) . IEEE, 2022, pp. 7023–
7028.
[16] S. Sasaki and C. Langbort, “A model of information regulation in
the presence of competition between social media platforms,” IFAC-
PapersOnLine, vol. 55, no. 13, pp. 186–191, 2022.
[17] E. Kamenica and M. Gentzkow, “Bayesian persuasion,” American Eco-
nomic Review, vol. 11, no. 6, pp. 2590–2615, 2011.
[18] G. Egorov and K. Sonin, “Persuasion on networks,” National Bureau of
Economic Research, Tech. Rep., 2020.
[19] D. Ediger, K. Jiang, J. Riedy, D. A. Bader, C. Corley, R. Farber,
and W. N. Reynolds, “Massive social network analysis: Mining twitter
for social good,” in 2010 39th International Conference on Parallel
Processing, 2010, pp. 583–593.
[20] S. Morris, “Contagion,” The Review of Economic Studies, vol. 67, no. 1,
pp. 57–78, 01 2000.
[21] E. Croes and J. Bartels, “Young adults’ motivations for following social
influencers and their relationship to identification and buying behavior,”
Computers in Human Behavior , vol. 124, 2021.

13
[22] B. Hebert and W. Zhong, “Engagement maximization,” 2022. [Online].
Available: https://arxiv.org/pdf/2207.00685.pdf
[23] I. Himelboim, M. A. Smith, L. Rainie, B. Shneiderman, and C. Espina,
“Classifying twitter topic-networks using social network analysis,” So-
cial media+ society , vol. 3, no. 1, 2017.
[24] M. McPherson, L. Smith-Lovin, and J. M. Cook, “Birds of a feather:
Homophily in social networks,” Annual review of sociology , vol. 27,
no. 1, pp. 415–444, 2001.
[25] S. Currarini, M. O. Jackson, and P. Pin, “An economic model of friend-
ship: Homophily, minorities, and segregation,” Econometrica, vol. 77,
no. 4, pp. 1003–1045, 2009.
[26] M. O. Jackson and E. C. Storms, “Behavioral communities and
the atomic structure of networks,” 2017. [Online]. Available: https:
//arxiv.org/abs/1710.04656
[27] F. Parise and A. Ozdaglar, “Graphon games,” in Proceedings of the
2019 ACM Conference on Economics and Computation , ser. EC ’19.
New York, NY , USA: Association for Computing Machinery, 2019, p.
457–458.
So Sasaki is working toward the Ph.D. degree with
the University of Illinois at Urbana–Champaign, Ur-
bana, IL, USA. He is currently with the Decision and
Control Group, Coordinated Science Lab, Univer-
sity of Illinois at Urbana–Champaign. His research
interests include game, optimization, control, graph
theory, and machine learning, with application to
social media.
C´edric Langbort received the Ph.D. degree in
Theoretical and Applied Mechanics from Cornell
University, Ithaca, NY , USA, in 2005. He is cur-
rently a Professor of Aerospace Engineering with
the University of Illinois at Urbana–Champaign,
Champaign, IL, USA. He is also with the Decision
and Control Group, Coordinated Science Lab (CSL),
where he works on the applications of control, game,
and optimization theory to a variety of fields.
