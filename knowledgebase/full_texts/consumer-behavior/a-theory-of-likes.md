---
title: A Theory of Likes
url: https://arxiv.org/abs/2408.11362
category: consumer-behavior
subcategory: empirical
date: 2024-08
venue: ''
authors:
- Jean-Michel Benkert
- Armin Schmutzler
source: arxiv
pdf_url: https://arxiv.org/pdf/2408.11362
pages: 47
chars: 99373
fetched_at: '2026-11-08T13:07:55+00:00'
kb_version: 1
---

# A Theory of Likes

A Theory of Likes
Jean-Michel Benkert and Armin Schmutzler ∗
June 9, 2026
Abstract
We study binary, non-strategic ratings when consumer preferences reflect a com-
bination of objective quality differences between products and idiosyncratic taste. A
rating then decomposes into objective and subjective content. Rating systems that
are extremely strict or extremely lenient only convey objective content, maximizing
consumer welfare when the population is not biased toward a particular product.
With a biased population, less extreme rating systems that convey subjective con-
tent can be valuable. In many environments, a sales-maximizing platform prefers
lenient rating systems, creating a conflict with welfare maximization.
Keywords:recommendations, ratings, preference heterogeneity, information design,
platform design, value maximization
JEL Classification:D02, D47, D83
∗Benkert: Department of Economics, University of Bern, jean-michel.benkert@unibe.ch. Schmutzler:
Department of Economics, University of Zurich, and CEPR, armin.schmutzler@econ.uzh.ch. This paper
was previously circulated under the title “A Theory of Recommendations”. We are grateful for very helpful
discussionswithDirkBergemann, PiotrDworczak, JohannesJohnen, IgorLetina, SimonLoertscher, Matt
Mitchell, Marc Möller, Nick Netzer, Volker Nocke, Martin Peitz, Marcus Reisinger, Egor Starkov, Jakub
Steiner and seminar participants in Bamberg, Bern, Fribourg, Lausanne, Zurich, at MaCCI (2025), SAET
(2023), Swiss Society of Economics of Statistics (2024), Swiss IO Day (2024) and Verein für Socialpolitik
(2024).
1
arXiv:2408.11362v4  [econ.GN]  8 Jun 2026

1 Introduction
Simple peer-to-peer ratings play an essential role for the diffusion of economic information
in diverse domains, most notably in the digital economy. In some ways, this is surprising.
For example, consider a consumer deciding whether to “like” a restaurant after a meal.
Her experience may depend on at least two dimensions, such as food quality and service
quality, each of which can be good or bad. Consumers agree that good food is better than
bad food and good service is better than bad service, but they may differ in how much
weight they place on each dimension. The consumer leaving the rating has little incentive
to think hard about how her like will be interpreted, while the consumer receiving the
rating may rely on it to avoid a poor match. Moreover, even a thoughtful consumer cannot
convey all relevant nuances through a coarse binary signal. The example illustrates three
core features of peer-to-peer rating:Products and preferences are heterogeneous,stakes
are asymmetricfor those who leave ratings and those who read them, andratings are
inherently coarse.
In this paper, we study how such ratings can nonetheless provide value. We first show
how coarse rating systems can be designed in such a way that a like (dislike) conveys
objectively good (bad) news about a product. We then argue that, from a consumer
welfare perspective, it need not be optimal to make use of this option. The subjectivity of
ratings is not always a bug to be eliminated, but can be the feature that makes a rating
system valuable: If the population is known to be biased toward particular products,
it may be desirable to design the system in such a way that consumers disagree about
whether a like is good or bad news about a product. Consumers with majority taste
will then understand that they should buy such a product, those with minority tastes
understand that they should avoid it. Having identified the optimal design of the rating
system from a consumer perspective, we then find that a sales-maximizing platform will
oftendeviatefromthisprescription, relyingtoooftenonexcessivelylenientratingsystems.
Our model captures the three core features of the example in a parsimonious way. An
agent must decide between twoproducts, which can come in different variants. There are
objectively good (bad) variants, for which all consumers agree that they are better (worse)
than all alternatives. Moreover, there are two controversial variants with intermediate
values, which consumers rank differently. Ex ante, consumers merely have distributional
information on which variant they are facing. However, one of the products comes with
a rating from a previous consumer: Thissendermechanically gives a like for a product
that is objectively good or at least sufficiently good from her perspective (with payoffs at
least some exogenous rating standardR). Thereceiverof the signal knows the preference
distribution and therefore how likely it is that his preferences are aligned with those of
the sender. Finally, based on this information, he decides whether to be obedient, that
1

is, behave according to the prescription of the rating.
A transparent cut-off condition determines whether a receiver isobedientordisobedi-
ent. Importantly, the condition is the same for likes and dislikes. The key insight is that
ratings contain both objective and subjective content. From a (dis-)like, a receiver learns
that the product is not objectively bad (good), generating a payoff effect that pushes
every receiver toward obedience. A like usually also raises the probability that, if the
product is controversial, it is of the variant preferred by the majority. For consumers
with majority tastes, these two pieces of information are both good news, so that they
are obedient. Consumers with minority tastes face opposing effects and are obedient only
when the objective effect outweighs the subjective one, and disobedient otherwise.
Our main contributions concern the design of rating systems. Platforms often try to
influence how critical consumer ratings are, for example through guidelines or instruc-
tions.1 We capture this by assuming that the platform controls the rating standardR
above which a like is given. Our first contribution is that we characterize the value of
rating systems for consumers and identify the value-maximizing choice ofR. When the
population is not biased toward any of the controversial products on average, the sub-
jective effect of ratings cancels out in the aggregate, and extreme rating standards are
optimal: Likes should be reserved for objectively good products, or dislikes for bad ones.
When the population is biased, ratings that convey subjective content due to an interior
rating standard may be strictly preferable. Intuitively, ratings can provide value in two
ways. First, they can push consumers toward objectively good products and help them
avoid objectively bad ones. Second, they can help consumers obtain a product variant
that fits their tastes, even when it is not perfect. These two objectives need not be con-
flicting: Consumers with majority tastes will benefit in both ways from being obedient.
Instead, for consumers with minority tastes, being obedient reduces the chance of getting
the preferred controversial product variant. Being disobedient reduces the chance of get-
ting the objectively good rather than the objectively bad variant. Either way, the rating
system creates value for these consumers, even if they do the opposite of what they are
told.
Our second main contribution concerns the potential conflict between consumer wel-
fare and sales maximization by a platform that benefits from transactions of the rated
product, for instance through transaction fees or advertising revenue tied to traffic. We
find that a sales-maximizing platform usually favors a lowR, issuing likes for everything
butobjectivelybadproducts. Bycontrast, thevalue-maximizingRcanbehighorinterior.
We provide several further results. First, we introduce prices and show that the
1For example, Uber employs a five-star system but informs riders that “5 stars means the ride went
without issues,” while “4 stars or less” prompt requests for feedback (Uber, 2024). Similarly, Airbnb
communicates that a 5-star rating means “everything was as expected” (Hospitable, 2024).
2

firm’s pricing decision affects not only demand but also the informativeness of the rating.
Second, weanalyzethecasewherereceiversobservemultipleindependentratings. Perhaps
surprisingly, access to more signals does not necessarily increase value or sales. Third,
we allow the sender and receiver populations to differ, showing that our main results
remain robust while new design considerations arise regarding the composition of the
sender pool. We close by examining how polarization and the prevalence of controversial
products shape the value of the rating system.
1.1 Related Literature
Our paper relates most directly to work distinguishing vertical quality from horizontal
fit in online reviews. Sun (2012) argues that variance of ratings does not reflect pure
noise but conveys information about taste differences. Chen, Hitt, Hong, and Wu (2021)
theoretically and empirically separate uncertainty about quality from uncertainty about
fit, finding that online ratings resolve the former more effectively than the latter. Closest
in spirit is Lafky and Ng (2024), who show experimentally that raters evaluate prod-
ucts through their own preferences and consumers interpret ratings accordingly. Bohren,
Hakimov, and Santos-Pinto (2025) provide complementary experimental evidence, show-
ing that ratings raise welfare under vertical but not under horizontal differentiation, while
segmenting ratings by consumer type restores the welfare gains.2
In a broad sense, our static inference problem belongs to the literature on observational
learning.3 A more closely related literature deals specifically with learning from online
reviews. For instance, Acemoglu, Makhdoumi, Malekian, and Ozdaglar (2022) show that
consumers with strong prior preferences are more likely to purchase and review, so the
pool of recommenders is endogenously selected and receivers must account for this bias.
Che and Hörner (2018) study the tension between informativeness and exploration in
recommender systems. We study a single binary signal in isolation, which makes the
rating standard the sole design instrument, enabling us to characterize precisely how it
trades off objective against subjective content.
Our design problem is naturally framed as one of constrained information design: The
platform cannot choose an arbitrary signal structure (Kamenica and Gentzkow, 2011),
only the rating standard at which senders convert their experience into a like. This can
be justified using results on the optimality of coarse disclosure in certification and rat-
ing design, including partial information revelation (Rayo and Segal, 2010), monopolistic
pass/fail certification (Lizzeri, 1999), and optimal partition of quality into rating tiers
2Bohren et al. (2025) isolate the pure vertical and pure horizontal cases, while we study environments
in which both dimensions coexist within a single product space.
3However, this literature, e.g. Banerjee (1992) Bikhchandani, Hirshleifer, and Welch (1992) and Smith
and Sørensen (2000), focuses on dynamics, and it emphasizes learning from the decisions of others rather
than ratings.
3

(Hopenhayn and Saeedi, 2026). Unlike this prior work, our signal is generated mechani-
cally from the experiences of heterogeneous senders, and the central trade-off is not more
versus less information but objective versus subjective content.4
Our analysis of the tradeoff between value and sales maximization connects to the
literature on platform economics and rating bias, where platform incentives often diverge
from consumer welfare. The most closely related papers in this area also work with het-
erogeneous tastes. Shi and Raghu (2020) studywhichproduct a platform should feature,
whereas we studyhow demandingthe standard for a positive recommendation should be.
Peitz and Sobolev (2025) show that a profit-maximizing firm may optimally recommend
products even to poorly matched consumers. A literature on reputation and recommen-
dation bias (Bourreau and Gaudin, 2022; Tadelis, 2016) documents how feedback systems
can be distorted by strategic behavior.5 By contrast, the wedge between platforms and
consumers that we identify does not rest on fake reviews or inflated individual messages.
Ratings are mechanically truthful, and the distortion arises because a sales-maximizing
platform chooses a more permissive rating standard than a value-maximizing one.
Section 2 introduces the model. Section 3 characterizes receiver behavior. Section 4
studies the value of rating systems, first characterizing the sources of value and then
analyzing the optimal design of the rating standard. Section 5 turns to the parallel
question of sales maximization, where a platform seeks to maximize transaction volume
rather than consumer welfare. Section 6 presents further results. Section 7 concludes. All
proofs are relegated to the appendix.
2 Model
Products and PayoffsWe consider a consumer’s choice between two products. Each
product can be of one of four variants:g, b, c1 andc 2. The probability of each variant is
independently drawn from the same distributionq= (qg, q1, q2, qb)where
Pr(g) =q g >0,Pr(b) =q b >0,Pr(c 1) =q 1 >0,Pr(c 2) =q 2 >0.
Consumers cannot observe the product variant before consumption, but they know the
distribution. Consumer types are distributed on[−1/2,1/2]according toF, which is ab-
solutely continuous with full support. All consumers obtain a payoff of1from consuming
variantgand a payoff of0from consuming variantb. The payoff from consuming variant
4Strategic senders can produce coarse messages endogenously, see, e.g., Chakraborty and Harbaugh
(2010) and Smirnov and Starkov (2025). Our senders are non-strategic, so coarseness is imposed by the
binary rating rule rather than chosen.
5For instance, Bolton, Greiner, and Ockenfels (2013) show how the threat of retaliation in reciprocal
feedback systems leads buyers to withhold negative feedback.
4

c1 is1/2+i, the payoff from variantc2 is1/2−i. Therefore, consumers agree that product
variantsgandbare (objectively) good and bad, leading to the maximal (minimal) payoff.
By contrast, the payoff fromc1 andc 2 depends on typei, so that the assessment of these
variants is subjective. We thus refer to them ascontroversial. Typesi >0preferc 1 to
c2, and vice versa fori <0, while typei= 0is indifferent between the two variants.
We use the following self-explanatory terminology:
Definition 1Theprevalence of controversial productsis given asQ:= q1+q2 2 . The
odds of a good productareσ:=q g/qb.
A Motivating ExampleTo motivate the payoff structure, one might assume that a
product variant has two quality dimensionsd∈ {1,2}that are relevant to consumers.
The quality level in each dimensiondcan take valuesω d ∈ {0,1}. All consumers agree
that high quality in any dimension is desirable, but they put weight1 2 +ion dimension
1and weight 1 2 −ion dimension2. Definingc i as a product variant with quality1in
dimensioniand quality0in dimensionj̸=i, the above payoff structure obtains.
Ratings and UpdatingBefore choosing products, a consumer receives a rating for
one of the two products from a previous consumer. Thissender(she) and thereceiver
(he) are both drawn from the distributionF. Senders and receivers who consume the
same product face the same variant and differ only in their type-dependent evaluation of
controversial products. The receiver chooses between the product with a ratingr, which
can be a like (r=L) or a dislike (r=D), and the alternative without (r= 0).
To eliminate any scope for strategic sender behavior, we assume that a sender mechan-
ically gives a like if she obtained a payoff of at leastR∈(0,1)and a dislike otherwise.6
Intuitively, a like conveys the following information to the receiver: The probability of
the bad product variant falls to zero, the likelihood of the good variant relative to the
controversial variants rises, and the odds between the controversial variants change.
For the objectively good and bad variantsgandb, there issender agreement: All types
like the former and dislike the latter. For the controversial variants, sender behavior
is type-dependent: After consumingc 1, a sender of typeigives a like if and only if
i≥R−1/2, whereas typesi≤1/2−Rgive a like after consumingc 2; see Figure 1. A
rating hasobjective contenton which all senders agree, andsubjective contenton which
they do not. The rating standard determines the mix between objective and subjective
content: For interiorR, sender disagreement on controversial products is preserved and
ratings carry nontrivial subjective content. AsR→0orR→1, sender disagreement
vanishes and ratings become purely objective in content.
6We exclude the rating standardR= 0as this would render the rating uninformative. For symmetry,
we also excludeR= 1, but all results would essentially go through if we allowedR= 1.
5

Figure 1. Illustration of Sender Beha vior
−1/2 0 1/4 1/2
Product variantc 1
−1/2 −1/4 0 1/2
Product variantc 2
Notes:The figure illustrates what types send a like (green) and a dislike (red) for the two controversial
product variants whenR= 3/4.
Letϕ 1(R) := 1−F(R−1/2)andϕ 2(R) :=F(1/2−R)denote the probability of a
like conditional on the product variant beingc1 orc 2, respectively. The probability that
a randomly chosen sender gives a like or dislike, respectively, is
πL(R) :=q g +q 1ϕ1(R) +q 2ϕ2(R),
πD(R) := 1−π L(R) =q 1(1−ϕ 1(R)) +q 2(1−ϕ 2(R)) +q b.
In words, the probability of receiving a like from a randomly chosen sender is given
by the sum of the probability that a product is objectively good and the probability
that it is subjectively good enough from a randomly chosen sender’s perspective. We
assume that receivers are Bayesian. In Appendix A.1.1, we present the receiver’s posterior
pr(R) := (pr g(R), pr 1(R), pr 2(R), pr b(R))after a liker=Lor a disliker=D. 7
Finally, we use the following summary terminology:
Definition 2E:= (q, F)defines adecision environment. Arating systemRcon-
sists of a decision environmentEand a rating standardR∈(0,1).
Throughout, the decision environmentEand the rating standardRare common knowl-
edge among all agents.
3 Receiver Behavior
The receiver must decide whether to follow the prescription of the rating, that is, whether
to purchase the rated product after a like and avoid it after a dislike. We now characterize
the receiver’s optimal choice, depending on his typeiand the rating systemR.
The expected payoffs from buying the product with a rating and the alternative with-
7To simplify notation, we will often drop the dependence of these posteriors and other variables onR.
6

out are respectively given as
U r(i) :=p r g + (1/2 +i)p r 1 + (1/2−i)p r 2, r∈ {L, D};
U 0(i) :=q g + (1/2 +i)q 1 + (1/2−i)q 2.
Receiveribuys the product rated with a like if and only ifUL(i)≥U 0(i)or equivalently
pL g −q g
2 − pL b −q b 2 +i[(p L 1 −q 1)−(p L 2 −q 2)]≥0.(1)
The receiver follows the prescription of dislike ratings if and only ifU0(i)≥U D(i). A
rating’s informational impact on the receiver decomposes into an objective and a subjec-
tive payoff effect. To make this precise:
Definition 3For a ratingr∈ {D, L}, let∆r O and−i∆ r S denote its objective and subjec-
tive payoff effects, respectively, where
∆r O := pr g −q g 2 − pr b −q b 2 ,
∆r S := (pr 2 −q 2)−(p r 1 −q 1).
If∆ r O >0, the ratingrhas shifted probability from the objectively bad to the objectively
good variant, a payoff gain shared by all types.∆r S measures the analogous shift between
the controversial variants: fromc 1 toc 2 when positive, and conversely when negative.
Whether this shift is good news depends on the receiver: The sign of the subjective payoff
effect,−i∆ r S, depends on the signs ofiand∆ r S, so that a shift towardc2 is welcome only
for types who preferc2 toc 1. Applying this notation to condition (1), we obtain:
Proposition 1For a given rating systemR, a receiver of typeibuys the rated product
after a like and does not buy it after a dislike if and only if
∆L O ≥i∆ L S.(2)
Intuitively, a receiver follows a prescription only if he expects the rating to come from
a sender whose preferences are sufficiently aligned with his. Condition (2) formalizes
the resulting trade-off via the objective and subjective payoff effects. Importantly, this
condition is the same for likes and dislikes, which motivates the following terminology:
Definition 4
(i) A receiver isobedientif he buys the rated product after a like but not after a dislike,
disobedientif he buys it after a dislike but not after a like.
7

(ii) Receivers areuniversally obedientin decision environmentEif all receivers are
obedient for everyR∈(0,1).
Denoting the type who is indifferent between being obedient or disobedient as
˜i:= ∆L O
∆L S if∆ L S ̸= 0,
Proposition 1 immediately implies the following result:
Corollary 1Fix a rating systemR.
(i) If|∆ L S| ≤2∆L O, then alli∈[−1/2,1/2]are obedient.
(ii) If∆ L S <−2∆ L O, then alli≥ ˜iare obedient.
(iii) If∆ L S >2∆ L O, then alli≤ ˜iare obedient.
Intuitively, in case (i), the objective effect is so large that it dominates even the subjective
effect of the most extreme receivers. As∆ L S and hence the subjective effect increases,
receivers who are not sufficiently aligned with the population at large will be disobedient;
see cases (ii) and (iii). The interplay between objective and subjective effect leads to a
stark result for extreme rating standards:
Proposition 2SupposeR→1orR→0. Then, all types are obedient irrespective of
the decision environmentE.
In the limits, ratings have purely objective content. For instance, asR→1, a like
guarantees the product is objectively good, while a dislike implies it is not.
4 Value of Rating Systems
This section takes a welfare perspective, studying the value of rating systems for receivers
and deriving the value-maximizing choice of the rating standard.
4.1 Characterization of the Value
Without a rating system, all product variants are identical ex ante, with an expected
payoff based on the prior distribution of product variants:
V 0(i) :=U 0(i).(3)
8

If one of the products comes with a rating, an obedient receiverichooses this product
(rather than the alternative) only if it comes with a like. The expected payoff is thus
V +(i) :=π LU L(i) + (1−π L)U 0(i).(4)
The first term on the right-hand side comes from likes, the second one from dislikes.
A disobedient receiver will buy a product that comes with a dislike. Otherwise, he
will buy the alternative. Hence, his expected payoff is
V −(i) :=πLU 0(i) + (1−π L)U D(i).(5)
A like does not create value for disobedient receivers, who choose the alternative
without a rating. Instead, a dislike, which is given with probability(1−πL), influences
their behavior: Rather than buying an alternative based on priors, updating leads them
to choose the product for which they received the explicit recommendation not to buy.
We now define the value of a rating system.8
Definition 5V(R), thevalue of a rating systemR= (E, R), is the increase in
expected payoffs resulting from the existence of a rating standardRin a decision environ-
mentE, where the expectation is taken over all pairs of independently drawn senders and
receivers.
Using Definition 5 and Corollary 1, we can characterizeV(R)as follows:
(i)
R 1/2
−1/2(V +(i)−V 0(i))dF(i)if|∆ L S| ≤2∆L O;
(ii)
R ˜i
−1/2 V −(i)dF(i) + R 1/2 ˜i V +(i)dF(i)− R 1/2 −1/2 V 0(i)dF(i)if∆ L S <−2∆ L O;
(iii)
R ˜i
−1/2 V +(i)dF(i) + R 1/2 ˜i V −(i)dF(i)− R 1/2 −1/2 V 0(i)dF(i)if∆ L S >2∆ L O.
All receivers are obedient when|∆L S| ≤2∆L O, as the objective effect dominates (case (i)).
Hence, by equation (4), the rating system creates value only for a receiver who observes a
like, as a dislike leads to the same expected payoff as without a rating system. Parts (ii)
and (iii) refer to cases where the subjective effect of the messages matters more. Then, not
all receivers are obedient and, as argued above, the system can create value for receivers
that are obedient as well as those who are not.
We restate the valueV(R)to better understand how it reflects the role of the objective
and subjective payoff effects of ratings:9
Proposition 3The valueV(R)of the rating systemRis:
(i)π L[∆L O −∆ L S E[i]]if|∆ L S | ≤2∆L O;
(ii)(1−π L)F(˜i)  ∆D O −∆ D S E[i|i≤ ˜i]  +π L(1−F( ˜i))  ∆L O −∆ L S E[i|i≥ ˜i]  if∆ L S <−2∆ L O;
(iii)π LF(˜i)  ∆L O −∆ L S E[i|i≤ ˜i]  + (1−π L)(1−F( ˜i))  ∆D O −∆ D S E[i|i≥ ˜i]  if∆ L S >2∆ L O.
8This definition is in line with the definition of a valuable signal in Kamenica and Gentzkow (2011).
9As we focus onRas the design parameter, we often writeV(R)instead ofV(R).
9

The positive payoff effect of the rating system in case (i) consists of the type-independent
objective effect∆ L O and the expected subjective effect−∆ L SE[i]. As∆ L S increases in
absolute terms, some receivers become disobedient. For instance, when∆ L S >2∆ L O, a
like shifts beliefs toward the controversial product variant that is less preferred by types
i >0, who may thus become disobedient. Only the fractionF( ˜i)of the population
whose preferences are sufficiently aligned with the sender’s (i <˜i) still buy. For them,
the subjective effect is either positive or not sufficiently negative to dominate the positive
objectiveeffect. Theaveragesubjectivepayoffeffectamongtheobedienttypesis−∆ L SE[i|
i≤ ˜i]. As argued above, the fraction1−F( ˜i)of disobedient types may benefit from the
rating. They infer from a dislike that the product is likely to be of the controversial variant
they personally prefer and thus buy despite or rather because of the negative signal.10
4.2 Design
The design problem is to choose a rating standardR∈(0,1).11 Extreme standards yield
sender agreement and thus purely objective content, while interior standards preserve dis-
agreement and admit subjective content. We organize the analysis along this dichotomy.
We first show that, when the population is symmetric, the aggregate contribution of the
subjective effect cancels out, so design is governed by the objective effect alone and ex-
treme standards are generically optimal. We next show that, when the population is
asymmetric, the subjective effect no longer cancels out in the aggregate, and balancing
it against the objective effect yields an interior optimum under simple general conditions
on the decision environment. Finally, we present a tractable parametric example in which
both regimes appear and the optimal rating standard can be characterized in closed form.
4.2.1 Symmetric populations
We begin with symmetric populations, so that preference heterogeneity corresponds to
pure noise on average.
Assumption 1F(−i) = 1−F(i)for alli∈[−1/2,1/2].
Under symmetry, the share1−F(R−1/2)of senders who give a like after consumingc1
is the same as the shareF(1/2−R)who give a like after consumingc 2, and we define
β:=F(1/2−R) = 1−F(R−1/2). Symmetry implies that the subjective effect of ratings
cancels out in the aggregate. From Proposition 3, we thus obtain:
10This is reflected in the term(1−πL)(1−F( ˜i))  ∆D O −∆ D S E[i|i≥ ˜i]  in Proposition 3(iii).
11Throughout, we formulate the design problem on the open intervalR∈(0,1). Statements favoring
extreme standards should therefore be understood as boundary statements, i.e. as limits or maxima of
the continuous extension atR= 0orR= 1.
10

Lemma 1For any rating system satisfying Assumption 1, all types are obedient and
V(R) =π L∆L O.
The optimal rating standard then depends only onσ, the odds of a good product:
Proposition 4For any rating system satisfying Assumption 1,V(R)is
(i) decreasing inRifσ <1;
(ii) increasing inRifσ >1;
(iii) independent ofRifσ= 1.
Intuitively, since the subjective effect of ratings cancels out in the aggregate, the designer
can focus on the objective effect. To this end, he either chooses a very low rating standard
close to0that reveals whether a product is objectively bad or not, or a very high rating
standard close to1that reveals whether a product is objectively good or not. Which
choice is better depends on how important these two pieces of information are: When
objectively bad goods are common (σ <1), it is important to avoid them, so an extremely
low rating standard is appropriate; when objectively good products are common (σ >1),
it is important to identify them through extremely high rating standards.
4.2.2 Asymmetric populations
We now turn to asymmetric populations. To capture biased populations in a tractable
way, we introduce the following weak assumption.
Assumption 2Fhas meanµ:=E[i]̸= 0. Moreover, its densityfextends continuously
to[− 1 2 , 1 2 ]and satisfies0< f(± 1 2 )<∞.
We use a shorthand notation for the net payoff of the average receiver from consuming
each controversial variant rather than taking the outside option:
A1 :=
 1
2 +µ

−U 0(µ),
A2 :=
 1
2 −µ

−U 0(µ).
Here, 1 2 +µand 1 2 −µare the gross payoffs of typeµfrom variantsc1 andc 2, respectively,
whileU 0(µ)is her expected payoff from the unrated alternative. We obtain a sufficient
condition for an interior rating standard to be optimal:
Proposition 5For any rating system satisfying Assumption 2, if
q1A1f(− 1 2 ) +q 2A2f( 1 2 )<0< q 1A1f( 1 2 ) +q 2A2f(− 1 2 )(6)
then there exists an optimalR∗ ∈(0,1).
11

Condition (6) is clearly inconsistent with Assumption 1. Moreover, it requires thatA1
andA 2 have different signs. W.l.o.g., we assume thatA1 >0> A 2, meaning that variant
c1 is valuable for the average receiver relative to the outside option, whereas variantc2
is not. Under this interpretation, condition (6) has a transparent meaning. The first
inequality guarantees that rating standards nearR= 0are dominated by slightly more
stringent standards. Starting from an extremely lenient standard, a small increase inR
removes only likes from senders who have strong preferences for one of the controversial
products and thus hardly value the other one. For variantc1, these likes come from types
near−1/2; for variantc2, they come from types near1/2. The inequality states that these
weakest marginal likes have negative average value: They are too heavily tilted toward
recommendations for the controversial variant that is bad from a majority perspective.12
Hence, an extremely lenient standard is too permissive. By similar arguments, the second
inequality guarantees that extremely stringent rating standards are not desirable.
4.2.3 A tractable example
The general results of Sections 4.2.1 and 4.2.2 establish the qualitative dichotomy between
symmetric and asymmetric populations. To illustrate the general mechanism from above,
we now provide an explicit closed-form solution for a tractable parametric specification.13
Example 1(i)F(i) = (i+ 1/2) a fora >0; (ii)q 1 =q 2 =Q.
The casea= 1reflects a symmetric, unbiased population. By contrast, whena̸= 1, the
population is biased toward one product variant or the other.14
Our characterization focuses on decision environments where the prevalence of contro-
versial products is so low that receivers are universally obedient. In the Online Appendix
OA.1.1, we show that this holds ifQ≤ ¯Q(a, σ)for a cutoff ¯Q(a, σ)∈(0,1/2]that is
unique givenaandσ, the other features of the decision environment. The condition is
frequently satisfied.15 Moreover, in Lemma OA.2 of the Online Appendix, we show that
this condition is easiest to satisfy in the unbiased benchmarka= 1and becomes harder
12The fact that senders near1/2switch from like to dislike after observing variantc2 is desirable from
the perspective of the average receiver, the corresponding switch for senders near−1/2after observing
variantc 1 is not. The left inequality in (6) guarantees that the beneficial effect of eliminating undesirable
likes dominates the adverse effect of eliminating desirable likes.
13Example 1 is complementary to Assumption 2 rather than nested in it: the power distributions
F(i) = (i+ 1/2) a have boundary densities that vanish or diverge whena̸= 1. A tractable example of a
distribution that satisfies Assumption 2 is given by tilted-uniform distributions.
14The conditionq 1 =q 2 ensures that all subjective content in ratings is driven by the asymmetry of
the type distributionF, not by prior differences in how common the controversial variants are.
15Ifa= 1, ¯Q(1, σ) = 1/2, so universal obedience arises for every admissibleQ. Fora̸= 1, the cutoff is
still quite large (for example,¯Q(2,1) = 1/3). Atσ= 1anda >1the closed form ¯Q(a,1) = 1/[4(1−2 −a)]
obtains (Corollary OA.2 in the Online Appendix). For generalσ, ¯Q(a, σ)is also computable from the
primitives.
12

to satisfy as the population becomes more biased. We now describe the relation between
the rating standardRand the value, focusing on the asymmetric case.
Proposition 6Suppose the decision environmentEsatisfies the conditions in Example 1
as well asQ≤ ¯Q(a, σ)anda̸= 1.
(i) IfQ≥min
 a
a+1 , 1 a+1 	 , thenV(R)is maximized at a uniqueR ∗ ∈(0,1).
(ii) IfQ <min
 a
a+1 , 1 a+1 	 , then
(a)V(R)is decreasing inRif and only ifσ≤min
n
a−Q(a+1)
1−Q(a+1) , 1−Q(a+1) a−Q(a+1)
o
;
(b)V(R)is increasing inRif and only ifσ≥max
n
a−Q(a+1)
1−Q(a+1) , 1−Q(a+1) a−Q(a+1)
o
;
(c)V(R)is maximized at a uniqueR ∗ ∈(0,1)otherwise.
Proposition 6 first identifiesmin
 a
a+1 , 1 a+1 	 as a cutoff on the share of controversial
products, above which an interior optimum exists. Below that cutoff, extreme rating
standards are optimal only when the odds of a good product are sufficiently unbalanced.
Figure 2 illustrates how the occurrence of interior solutions depends on the parameters:
the furtherais away from1, the larger is the interval ofσvalues for which an interior
solution exists.
In some cases, the restrictionQ≤ ¯Q(a, σ)is not needed. In Example 1, ifσ= 1, so
thatq g =q b, the design role of the objective channel is shut down. The rating standard
matters only through the subjective content of the rating. One can show that this content
is maximized atR= 1/2, where senders like precisely the controversial variant they
personally prefer. Thus the midpoint standard makes ratings maximally informative
about the controversial dimension.16
5 Sales Maximization
We now consider a platform that maximizes sales of the product with a rating rather
than receiver welfare. It will turn out that there are parameter regions where the two
objectives are aligned and others where they are in stark conflict.
5.1 Characterization
Using Corollary 1, the sales for the rated productD(R)can be expressed analogously to
the value of the rating system in Proposition 3 as
16This remains true even whenQ >¯Q(a,1)and some receivers are disobedient, as disobedience does
not affect the amount of subjective content conveyed by the rating.
13

Figure 2. Illustration of Proposition 6
1 3 5 7 9
1
3
5
7
9
R∗
∈(0,1)
R∗ ∈(0,1)
R∗ →1
R∗ →0
a
σ
Notes:This figure illustrates the parameter regimes of Proposition 6 forQ= 0.05. The dotted and
dashed curves correspond toσ= (a−Q(a+ 1))/(1−Q(a+ 1))and its reciprocal, respectively. An
interior solution arises between the two curves. Otherwise, extreme rating standards are optimal.
(i)π L(R)if|∆ L S| ≤2∆L O;
(ii)π L(R)F(˜i(R)) + (1−π L(R))(1−F( ˜i(R)))if∆ L S >2∆ L O;
(iii)π L(R)(1−F( ˜i(R))) + (1−π L(R))F(˜i(R))if∆ L S <−2∆ L O,
where we have made explicit that the indifferent receiver˜iand the probability of a like
πL are functions of the rating standardR. Similar to the expression for the value in
Proposition 3, the relation between∆L S and∆ L O determines which types are obedient. In
case (i), all types are obedient so that sales are given byπL(R), the probability of a like.
In cases (ii) and (iii), sales come from both obedient and disobedient types. Importantly,
disobedient types buy a product rated with a dislike, thus contributing to sales.
The structural parallel betweenD(R)above and the value expression in Proposition 3
is instructive. The determinants of both expressions are the same (πL,∆ L O,∆ L S and ˜i).
The key difference lies in the aggregation across receivers. Value weights each rating by
the resulting payoff effect for the receiver, while demand simply counts purchases. When
all types are obedient, sales equalπL, the frequency of likes, regardless of their objective
effect on receivers. This difference drives the potential conflict between value and sales
maximization.
5.2 Design
Proceeding as in Section 4.2, we first show that, for symmetric populations, sales are
monotone in the rating standard. Then, we establish an analogous result that applies to
asymmetric populations as well.
14

Proposition 7For a decision environmentEsatisfying Assumption 1, demandD(R) =
πL(R)is decreasing inR.
ThesimpleformofD(R)isimpliedbyLemma1, whichstatesthatreceiversareuniversally
obedient under Assumption 1. This implies the result because the probability of likes is
decreasing inR. 17
Comparison with Proposition 4 highlights the potential for conflict between value and
sales maximization. Whenσ <1, value is also decreasing inR, so the two objectives are
aligned and both call for a low standard. Whenσ >1, however, value is increasing in
Rwhile sales remain decreasing, so that the objectives are diametrically opposed: Sales
maximization favors a low standard to make likes frequent, while value maximization
favors a high standard to make likes informative.
Like value maximization, sales maximization becomes more complex for asymmetric
population distributions. Nonetheless, we establish a sufficient condition for sales maxi-
mization to call for low rating standards, mirroring the result in the symmetric case.
Proposition 8Consider a decision environmentEwithq g ≥q b. Then, the continuous
extension ofD(R)to[0,1]is maximized atR= 0.
The result holds without assumptions on the distributionF, but requiresq g ≥q b.
Intuitively, sales come from obedient types who received a like and disobedient types who
received a dislike. LoweringRenlarges the like channel and shrinks the dislike channel
in any decision environment. The assumptionqg ≥q b ensures the first effect dominates,
makingR= 0optimal. This contrasts sharply with value maximization. In Example 1
withq g > qb, the condition for value to be decreasing inRin Proposition 6 is never
satisfied: Since good products are common, likes are frequently given for lowR, and the
emphasis shifts from frequency to informativeness. IncreasingRfilters out controversial
products, making likes more selective and thus more valuable.
Whenq g < qb, the analytical argument for Proposition 8 no longer extends. One
sufficient condition under which demand is nonetheless highest for low rating standards is
universal obedience: Then demand coincides with the probability of a like, so loweringR
weaklyincreasessalesregardlessofwhetherq g islargerorsmallerthanq b. Thus, thefailure
of Proposition 8 in the unrestricted model must rely on some receivers beingdisobedient.
This is not merely a limitation of the proof: without further restrictions onF, one can
construct absolutely continuous full-support type distributions for which the continuous
extension ofD(R)is not maximized atR= 0. The reason is that, when bad products are
sufficiently common, dislikes are frequent. If the type distribution is sufficiently biased,
the subjective effect may dominate the objective effect for many receivers. Demand can
then be driven by disobedient receivers rather than by the frequency of likes.
17See Lemma A.2 in the appendix.
15

This possibility appears not to arise in the tractable specification of Example 1, in
whichq g < qb corresponds toσ <1. An extensive numerical search found no violations
of monotonicity, so that sales remain decreasing inR. Thus, while Proposition 8 is false
in the unrestricted model withoutq g ≥q b, the low-standard conclusion appears robust
within Example 1.
6 Further Results
6.1 Optimal Pricing
We now introduce prices to highlight that, when ratings are based on net utility, the price
of a product affects not only its sales but also the value of a rating. This connects to a
literature on how prices and ratings interact.18 Our purpose is not to study full-fledged
pricing competition, but to isolate, in the simplest setup, how the firm’s pricing choice
feeds back into the value of the rating.
We consider a symmetric population and assume for simplicity that types are dis-
tributed uniformly.19 To simplify the exposition further, we assume that the controversial
variants are equally likely and setQ=q 1 =q 2. Receivers choose between buying the
product with a rating at priceP≥0and buying the product without a rating at a
price normalized to beP 0 = 0. The rating standardR∈(0,1)is fixed (e.g., by a
platform), and the firm selling the product with a rating choosesPto maximize profit
Π(P;R) =P D(P;R), whereD(P;R)denotes demand at pricePgiven standardR.
Ratings are based onnetutility. For instance, after consuming product variantc 1, a
sender gives a like if and only if1/2 +i−P≥R, resulting in an effective rating standard
T:=R+P. We work with the continuous extension of the rating rule toT= 1and can
therefore considerT∈(0,1], equivalently pricesP∈[0,1−R], without loss.
The receiver buys the product with a like if and only if
U L(R+P)−P≥U 0 ⇔P≤∆ L O(R+P).
Since∆ r S = 0, all types consider a like objectively good news and the dislike objectively
bad news. After a dislike rating, the product with a rating is dominated by the outside
option.20 Moreover, either all types buy the product with a like at pricePor none do.
18Johnen and Ng (2024) show that firms can strategically use pricing to harvest favorable ratings, Peitz
and Sobolev (2025) document rating inflation, and Carnehl, Stenzel, and Schmidt (2024) study dynamic
pricing when prices directly shape the distribution of reviews.
19Assuming the uniform distribution simplifies the analysis and admits closed-form solutions. Econom-
ically, the key assumption is symmetry as in Assumption 1 to ensure that the two controversial variants
generate likes with the same probability at a given rating standard.
20Formally,U D(R+P)≤U 0 andP≥0implyU D(R+P)−P≤U 0.
16

Therefore, sales at pricePtake the simple form
D(P;R) =π L(R+P)·1  P≤∆ L O(R+P) 	 ,(7)
and the firm’s profits areΠ(P;R) =P·D(P;R).Intuitively, at a price of zero, all
consumers who observe a like buy the rated product. By increasing the effective rating
standardT=R+Pand thus decreasingπ L(R+P), a higher price makes a like less likely.
However, conditional on observing a like, the rating becomes more valuable because it is
harder to obtain. This increases the receiver’s willingness to pay after a like, so that
∆L O(R+P)is increasing inP. 21 In regions where the latter effect dominates, sales are
increasing inP. They remain positive as long asP≤∆ L O(R+P).
DefineP u(R)as the unrestricted maximizer of the objectiveP πL(R+P), ignoring
the demand constraintP≤∆ L O(R+P). Denote the upper bound of the feasible price set
as ¯P(R) := max  P∈[0,1−R] :P≤∆ L O(R+P) 	 . We then obtain:
Proposition 9Consider a decision environmentEsuch that the type distributionFis
uniform,q 1 =q 2 andq g > Q.22 Then, for a fixed rating standardR∈(0,1), the firm’s
profit-maximizing price isP ∗(R) = min  P u(R), ¯P(R) 	 .
The above result also sheds light on the conflict between value and sales maximization.
A higher price raises the effective rating standardT=R+PaboveR. By Proposition 4,
when (objectively) good products are common, this upward shift movesTin a value-
enhancing direction: a higher positive price makes the rating more selective and thereby
more valuable. Conversely, when good products are scarce, a higher price pushesTaway
from the value-maximizing level. In this case, the firm’s profit motive undermines the
value of the rating system.
6.2 Multiple Ratings
We now show that additional ratings fail to add value when controversial variants are
equally likely, or when the outside option is so attractive or unattractive that the single-
rating optimum already induces the same decision. Formally, we consider a rating system
where the receiver observes an arbitrary large number of ratings (blikes andddislikes,
each independently drawn from a population of senders as in the benchmark model).23 To
21This mechanism is related to the rating inflation studied in Peitz and Sobolev (2025) and the price-
rating dynamics in Johnen and Ng (2024), where firms strategically manipulate the informativeness of
ratings through pricing.
22The assumptionq 1 =q 2 eliminates thesubjectivecontent of ratings and delivers the simple “all-
or-nothing” demand in (7). If insteadq 1 ̸=q 2, then a like typically also shifts beliefsbetweenthe two
controversial variants. Because receiver types value these two variants differently, the same rating is more
attractive for some types than for others. Demand afterLthen becomestype-dependent, and potentially
only a subset of consumers are obedient at a given price.
23We derive the posteriors for general(b, d)in Appendix A.4.2.
17

highlight the limits of informational gains from additional ratings, we focus on the case
ofinfinite learning,where the receiver observes an unbounded number of independent
ratings.
Proposition 10In the model with multiple ratings, suppose the decision environmentE
satisfies Assumption 1 holds. Letλ:=q 1/q2. Then, infinite learning does not increase
the value of the rating system relative to the optimally designed single-rating benchmark
if and only if one of the following holds:
(i)λ= 1;(ii)λ >1andσ /∈
 1
λ , λ

;(iii)λ <1andσ /∈

λ, 1 λ  .
Intuitively, a single like is sufficient to rule out the objectively bad variant, and a single
dislike rules out the objectively good variant. Hence, when the receiver obtains a mix of
both, he infers that the product must be one of the two controversial variants. With
infinitely many ratings, the receiver can perfectly infer whether the product is objectively
good, bad, or controversial. As in the case with only one rating, receivers buy objectively
good products and reject bad ones. Thus, any potential gain must come from improved
decisions about controversial products. However, controversial products always generate
mixed ratings. If the odds of good products are low, the outside option is unattractive,
and the receiver may prefer a controversial product even if it is only an imperfect match.
If the odds of good products are high, the receiver is more willing to choose the outside
option. In either extreme, the decision under infinite learning coincides with what could
be achieved by a single rating from an optimally designed rating system. Only when
the uncontroversial variants are similarly likely and the likelihoods of the controversial
variants are not too similar does additional information add value.
Finally, note that, under Assumption 1, providing more ratings does not help a sales-
maximizing platform either. To achieve this goal, it suffices to choose a single rating
standard close to0, which leads all senders to issue likes when the product is not bad.
Since mixed ratings can only reduce the likelihood of purchasing controversial products,
adding them weakly reduces sales.24
6.3 Distinct Sender and Receiver Distributions
Sender and receiver distributions may be distinct. For instance, as early adopters, senders
may differ systematically from the broader population.25 Our earlier results extend nat-
24The finding that additional ratings need not add value is related to Ifrach, Maglaras, Scarsini, and
Zseleva (2019), who develop a Bayesian model of sequential learning from binary like/dislike reviews and
show that a seller’s optimal dynamic pricing can cause learning to fail with positive probability. Both
findings illustrate that more signals need not raise welfare, though through different mechanisms.
25Acemoglu et al. (2022) study how such endogenous selection into reviewing shapes the speed of
Bayesianlearning. LiandHitt(2008)documenthowearlybuyerswithsystematicallydifferentpreferences
18

urally to such a setting. Let the sender be drawn fromFand the receiver fromG. If
Fsatisfies Assumption 1, the results from Sections 4 and 5 remain valid. For example,
generalizing Proposition 4, Proposition A.1 in the appendix shows that, whenFis sym-
metric, all receiver types are obedient,V(R)remains monotone inRandσcontinues to
play the same role as before in determining the sign of the slope. Similarly, the potential
conflict between value and sales objectives persists.
Beyond such robustness results, differing sender and receiver distributions give rise to
new design considerations. In many cases, platforms may have partial control over the
sender population or the information receivers have about it. For instance, Amazon’s
phrasing “customers who bought this item also bought...” implicitly informs the receiver
about who the senders are.
First, though it may seem that making the sender distribution more precise would raise
the value of the system, this is not always true. A more concentrated sender pool makes
ratings less dependent on idiosyncratic taste and therefore strengthens their objective
content while reducing subjective content. Whether this raises or lowers value depends
on which source of information is more important in the environment.26
Second, suppose that the sender and receiver distributions are fixed, but that the
designer can provide the receivers with a signal about the sender’s type. Assume for
simplicity that the signal fully reveals the type. If the sender is revealed to bei= 0, all
types are obedient, as her rating only contains objective content. In contrast, if the signal
reveals a sender of typei̸= 0, the receiver may learn about controversial products, too.27
Thus, having a biased sender is not necessarily a bad thing.
Third, suppose sender and receiver types are correlated, so that ratings are effectively
“tailored” to the receiver. Then the relevant sender distribution depends on the receiver’s
type. If these conditional sender distributions are symmetric, the subjective component
of a rating vanishes for every receiver. Hence all receivers are obedient, ratings are in-
terpreted purely through their objective content, and a sales-maximizing platform again
prefers a rating close toR= 0.
These three cases share a common thread: The sender’s characteristics shape not
only how often likes are issued but also what they reveal. A biased sender, for instance,
can be more informative about controversial products precisely because her ratings carry
subjective content. The design of the sender pool thus offers a complementary lever to the
rating standard for balancing objective and subjective content. Bohren et al. (2025) show
generate self-selection bias in reviews even when ratings are mechanically truthful, framed around the
same objective-quality versus subjective-fit decomposition we use.
26In particular, adapting the argument behind Proposition A.1 shows that the effect depends on the
prevalence of controversial products and on the extent to which receiver preferences are tilted toward one
controversial variant or the other.
27For instance, ifi= 1/2andR∈(0,1), a like reveals that the product is either of variantgorc 1.
19

experimentally that this lever can be relevant, where welfare in horizontally differentiated
markets is restored by segmenting the rating system by consumer type.28
6.4 Polarization and the Prevalence of Controversial Products
Invoking symmetry (Assumption 1), we now ask how the value of the rating system
responds to two features of the environment other than the rating standard: the degree
of preference polarization and the prevalence of controversial product variants.
First consider polarization (or preference heterogeneity). Recall thatβ=F(1/2−R)
is the fraction of the population willing to recommend a controversial product at stan-
dardR. Under Assumption 1,βsummarizes how often controversial products generate
positive ratings. A higherβraises the probability of likes, but weakens their objective
content, since more positive ratings stem from controversial rather than uncontroversially
good products. Whether greater preference heterogeneity raises or lowers the value of the
rating system depends onσ: When uncontroversially good products are common, highly
informative likes increase the value of the system, so a higherβis harmful; when un-
controversially bad products are common, the value comes from ruling out bad products
through more frequent likes, so a higherβis beneficial (see Appendix A.4.4).
Next, we turn to the prevalence of controversial product variants. A natural conjecture
is that a higher share of controversial products always reduces the value of the rating
system, because it dilutes the objective content of recommendations. This is indeed true
when good and bad products are similarly likely. More generally, however, the effect
ofQis non-monotone. Under Assumption 1, the value of the rating system can be
written asV(R) =π L∆L O, reflecting thatQhas two opposing effects: Likes become more
common but less likely to reflect uncontroversially good products. Whenσis far from
one, the frequency effect can dominate the loss in objective informativeness, so the value
of the rating system may be maximized at an interior share of controversial products
(Corollary A.1 in Appendix A.4.4).
7 Conclusion
We analyze the design of coarse rating systems, focusing on the binary case of likes and
dislikes.29 Our approach relies on the distinction between objective and subjective content
28Moreover, when the platform can influence the sender population, the choice of senders may itself
depend on the objective: A value-maximizing platform may prefer a different sender composition than a
sales-maximizing one, adding a new dimension to the value–sales conflict.
29One can show that the monotonicity result of Proposition 4 extends to richer rating structures.
With three rating levels—like, neutral, dislike—defined by two rating standardsR1 ≤R 2, value remains
monotone in the relevant standard under Assumption 1: decreasing inR1 ifσ <1and increasing inR 2
ifσ >1. Intuitively, the neutral rating reveals that the product is controversial but carries no subjective
20

of a rating. The payoff effect of a rating on a receiver has an objective part, shared by
all types, and a subjective part, with sign depending on how closely her preferences are
aligned with the sender’s. A receiver is obedient if the objective effect outweighs the sub-
jective one for her type. This decomposition shapes optimal design. When the population
is sufficiently biased toward one of the controversial variants, a value-maximizing system
preserves some subjective content at an interior standard, enabling inference about con-
troversial products; otherwise, an extreme standard that filters out all subjective content
is optimal.
The conflict between value and sales maximization is a central theme of our paper.
When good products are scarce, both objectives call for low standards. When good
products are common, this is usually still true for sales maximization but not for value
maximization. Our result on pricing reinforces this conflict. When good products are
common, the firm’s pricing enhances the value of the rating system by charging a high
price, but when they are low, pricing undermines the value of the system.
Although disobedient receivers play an important conceptual role in the model, they
appear only sparingly in the main design results. The reason is that optimal standards
often induce obedience by all receiver types. Under sales maximization, this is often the
case because the platform prefers extremely lenient standards, fostering obedience. Under
value maximization, universal obedience always obtains for symmetric populations, and it
can arise even under asymmetric populations when the subjective effect of ratings remains
sufficiently weak. Thus, disobedient receivers are central for understanding how ratings
can create value, but they are less often a feature of the optimally designed system itself.
There are several avenues for future research. For instance, the current model main-
tains classical assumptions such as risk neutrality and Bayesian updating. Relaxing these
assumptions could affect which receiver types are obedient, with potential implications for
the design of the system. On a related note, it would be interesting to use experimental
evidence to see whether our model captures key features of receiver behavior and in which
ways it fails to do so.
content under symmetry, so the design logic reduces to pushing one of the extreme standards to its
boundary.
21

A Formal Details and Proofs
A.1 Receiver Behavior
A.1.1 Posterior Distributions
The receiver’s posteriorpL(R) := (pL g (R), pL 1 (R), pL 2 (R), pL b (R))after a like is
pL g (R) := qg qg +q 1ϕ1(R) +q 2ϕ2(R) , p L 2 (R) := q2ϕ2(R) qg +q 1ϕ1(R) +q 2ϕ2(R) ,
pL 1 (R) := q1ϕ1(R) qg +q 1ϕ1(R) +q 2ϕ2(R) , p L b (R) := 0.
A dislike gives rise topD(R) := (pD g (R), pD 1 (R), pD 2 (R), pD b (R)), where
pD g (R) := 0, p D 2 (R) := q2(1−ϕ 2(R)) q1(1−ϕ 1(R)) +q 2(1−ϕ 2(R)) +q b ,
pD 1 (R) := q1(1−ϕ 1(R)) q1(1−ϕ 1(R)) +q 2(1−ϕ 2(R)) +q b , p D b (R) := qb q1(1−ϕ 1(R)) +q 2(1−ϕ 2(R)) +q b .
A.1.2 Proof of Proposition 1
Let∆ L(i)≡U L(i)−U 0(i)be the gain from buying after a like and∆D(i)≡U 0(i)−U D(i)
the gain from not buying after a dislike. The receiver buys after a like (does not buy after
a dislike) if and only if∆L(i)≥0(resp.∆ D(i)≥0).
We first show the equivalence of these conditions. For every states∈ {g,1,2, b},
Bayes’ rule impliesπ L(pL s −q s) +π D(pD s −q s) = 0.Multiplying by the state-contingent
payoffs{1,1/2 +i,1/2−i,0}and summing over the states yieldsπ L∆L(i) =π D∆D(i).
Becauseπ L, πD >0,∆ L(i)and∆ D(i)have the same sign, the desired equivalence holds.
It remains to show that this is equivalent to∆L O ≥i∆ L S. By condition (1), the receiver
buys after a like if and only if
(pL g −q g) + pL 1 −q 1 2 + pL 2 −q 2 2 ≥i  (pL 2 −q 2)−(p L 1 −q 1)  ,
which is exactly∆L O ≥i∆ L S by Definition 3.
A.1.3 Proof of Proposition 2
First, observe thatlim R→1 pL 1 = lim R→1 pL 2 = 0and thuslim R→1 pL g = 1. Hence, in the
caseR→1the obedience condition (1) simplifies to
1−q g − q1 +q 2
2 ≥i(q 1 −q 2).(8)
22

Equation (8) always holds fori≥0andq 1 ≥q 2. Further, forq 1 > q2 the condition is
most stringent fori= 1/2. In this case, it is equivalent to1≥q 1 +q g, which always
holds. The casei <0is analogous. In the caseR→0we getlim R→0 pL s =q s/(1−q b)for
s∈ {g,1,2}and thus the obedience condition simplifies to
qgqb
1−q b
+ q1qb
2(1−q b) + q2qb 2(1−q b) ≥i[ q2qb 1−q b − q1qb 1−q b ]
⇔2q g +q 1 +q 2 ≥2i[q 2 −q 1].
Fori≥0, the last condition always holds ifq 1 ≥q 2. Further, forq2 > q1 the condition is
most stringent fori= 1/2. In this case, it is equivalent toq g +q 1 ≥0, which is always
satisfied. The casei <0is analogous.
A.2 Value of Rating Systems
A.2.1 Proof of Proposition 3
(i) If|∆ L S| ≤2∆L O, inserting (3) and (4) yields
V(R) =
Z 1/2
−1/2
(V +(i)−V 0(i))dF(i)
=π L
Z 1/2
−1/2

pL g + (1/2 +i)p L 1 + (1/2−i)p L 2  −(q g + (1/2 +i)q 1 + (1/2−i)q 2)dF(i)
=π L
Z 1/2
−1/2
(pL g −q g) + pL 1 −q 1 2 + pL 2 −q 2 2 dF(i)−π L Z 1/2 −1/2 i([(pL 2 −q 2)−(p L 1 −q 1)])dF(i)
=π L
Z 1/2
−1/2
pL g −q g
2 − pL b −q b 2| {z }
=∆L O
dF(i)−π L
Z 1/2
−1/2
i([(pL 2 −q 2)−(p L 1 −q 1)]| {z }
=∆L S
)dF(i)
=π L[∆L O −∆ L S E[i]]
(ii) If∆ L S <−2∆ L O, inserting (3), (4) and (5) yields
V(R) =
Z ˜i
−1/2
V −(i)dF(i) +
Z 1/2
˜i
V +(i)dF(i)−
Z 1/2
−1/2
V 0(i)dF(i)
=
Z ˜i
−1/2
πL

qg +q 1( 1 2 +i) +q 2( 1 2 −i)  + (1−π L)  pD g +p D 1 ( 1 2 +i) +p D 2 ( 1 2 −i)  dF(i)
+
Z 1/2
˜i
πL

pL g +p L 1 ( 1 2 +i) +p L 2 ( 1 2 −i)  + (1−π L)  qg +q 1( 1 2 +i) +q 2( 1 2 −i)  dF(i)
−
Z ˜i
−1/2
qg +q 1( 1 2 +i) +q 2( 1 2 −i)dF(i)− Z 1/2 ˜i qg +q 1( 1 2 +i) +q 2( 1 2 −i)dF(i)
23

= (1−π L)
Z ˜i
−1/2
pD g −q g
2 − pD b −q b 2| {z }
=∆D O
−i([(pD 2 −q 2)−(p D 1 −q 1)]| {z }
=∆D S
)dF(i)
+π L
Z 1/2
˜i
pL g −q g
2 − pL b −q b 2| {z }
=∆L O
−i([(pL 2 −q 2)−(p L 1 −q 1)]| {z }
=∆L S
)dF(i)
= (1−π L)F(˜i)  ∆D O −∆ D S E[i|i≤ ˜i]  +π L(1−F( ˜i))  ∆L O −∆ L S E[i|i≥ ˜i]  .
(iii) If∆ L S >2∆ L O, thenV(R) = R ˜i −1/2 V +(i)dF(i) + R 1/2 ˜i V −(i)dF(i)− R 1/2 −1/2 V 0(i)dF(i).
Inserting (3), (4) and (5) and proceeding analogously as in case (ii) gives the expression.
A.2.2 Proof of Lemma 1
According to Corollary 1, all types are obedient if
min{∆L O + ∆L S 2 ,∆ L O − ∆L S 2 } ≥0.(9)
To see that this condition is fulfilled, first observe that
∆L O + ∆L S 2 =p L g −q g +p L 2 −q 2
= qg
qg +β(q 1 +q 2) −q g + βq2 qg +β(q 1 +q 2) −q 2
= β(q2 −(q g +q 2)(q1 +q 2)) +q g(1−q g −q 2) qg +β(q 1 +q 2)
This term is positive ifq2 −(q g +q 2)(q1 +q 2)≥0. Ifq 2 −(q g +q 2)(q1 +q 2)<0, then
β(q2 −(q g +q 2)(q1 +q 2)) +q g(1−q g −q 2)
≥(q 2 −(q g +q 2)(q1 +q 2)) +q g(1−q g −q 2) = (qg +q 2)(1−q 1 −q 2 −q g)≥0.
Thus,∆ L O + ∆L S 2 ≥0even in this case. Proceeding analogously, one obtains∆ L O − ∆L S 2 =
pL g −q g +p L 1 −q 1 ≥0.Corollary 1 thus implies that all types are obedient. Assumption 1
impliesE[i] = 0, so that the result follows from Proposition 3.
A.2.3 Proof of Proposition 4
We first restate the probabilities of likes, their objective effect and the value of the rating
system in terms ofσ,βandQ:
24

Lemma A.1Suppose Assumption 1 holds. Then,
πL = (1−2Q)σ 1 +σ + 2Qβ;
∆L O = βQ(σ+ 1)−2Qσ+σ 2βQ(σ+ 1)−2Qσ+σ − (1−2Q)σ 1 +σ −Q;
V(β) =π L∆L O = (1−2Q) σ+Q(β−σ+σ 2(1−β)) (σ+ 1) 2 .
Proof.The result onπ L follows from insertingqg = (1−2Q)σ/(1+σ),ϕ 1(R) =ϕ 2(R) =β
andq 1 +q 2 = 2Qintoπ L =q g +q 1ϕ1(R) +q 2ϕ2(R). Next, equation (3) gives
∆L O = βQ(σ+ 1)−2Qσ+σ 2βQ(σ+ 1)−2Qσ+σ − (1−2Q)σ 1 +σ −Q(10)
The result onV(β)then follows immediately from Proposition 3.
The following result shows that countervailing effects ofβon the probability of a like
and the objective value∆L O of accepting it result in a non-trivial effect onV(β) =πL∆L O.
Lemma A.2Suppose Assumption 1 holds. Then,
(i)π L is strictly increasing and∆L O strictly decreasing inβ;
(ii) ∂2V ∂β∂σ <0andV ′(β)has the same sign as1−σ.
Proof.(i) Note thatπ L = (1−2Q)σ/(1 +σ) + 2Qβ, so thatπ L is strictly increasing.
Moreover,
∂∆L O
∂β =− (Q(1−2Q)σ(1+σ)) (σ−2Qσ+2βQ(1+σ)) 2 <0.(ii) Lemma A.1 impliesV ′(β) = Q(1−2Q)(1−σ) 1+σ ,
and hence ∂2V ∂β∂σ =− 2Q(1−2Q) (1+σ)2 <0,so thatV ′(β)is negative forσ >1, positive forσ <1
and zero forσ= 1.
Then, usingβ=F(1/2−R), Lemma A.2 directly implies Proposition 4. 30
A.2.4 Proof of Proposition 5
The proof follows from Steps 1–6, which we now state and prove. We will repeatedly use
the formulation thata statement holds near the extremes, meaning that for any decision
environmentE, there existsδ(E)>0such that the statement holds forR < δ(E)and
R >1−δ(E).
Step 1:Near the extremes,V(R) =π L(R)  ∆L O(R)−µ∆ L S(R)  .
Proof of Step 1: ForR→0orR→1, all types have a strict preference for being
obedient. Since∆ L O(R)and∆ L S(R)are continuous inR, for any decision environmentE,
there existsδ(E)>0such that all types are obedient for allR∈(0, δ(E))∪(1−δ(E),1).
Hence, for suchRProposition 3(i) applies, and Step 1 follows.
30Result (iii) follows becauseV(β)is independent ofβin this case.
25

Step 2:Near the extremes,
V(R) =q 1

1
2 +µ

ϕ1(R) +q 2

1
2 −µ

ϕ2(R)−

qg + q1+q2 2 −µ(q 2 −q 1)  πL(R) +C,
where the termCis independent ofR.
Proof of Step 2: Recalling the posteriors after a like (see page 22) and applying
Definition 3, we obtain
πL∆L O =  qg −π Lqg  + q1ϕ1 −π Lq1 2 + q2ϕ2 −π Lq2 2 ,
πL∆L S =  q2ϕ2 −π Lq2  −  q1ϕ1 −π Lq1  = (q2ϕ2 −q 1ϕ1)−π L(q2 −q 1).
Inserting these terms into the expression from Step 1 and rearranging gives the claim.
Step 3:Near the extremes,V ′(R) =q 1A1 ϕ′ 1(R) +q 2A2 ϕ′ 2(R).
Proof of Step 3: Differentiating the expression obtained in Step 2 gives
V ′(R) =q 1

1
2 +µ

ϕ′ 1(R) +q 2

1
2 −µ

ϕ′ 2(R)
−

qg + q1 +q 2
2 −µ(q 2 −q 1)

q1ϕ′ 1(R) +q 2ϕ′ 2(R)  .
The claim follows from this expression using
1
2 +µ−

qg + q1 +q 2
2 −µ(q 2 −q 1)

= qb −q g
2 +µ(q 2 −q 1) +µ=A 1,
1
2 −µ−

qg + q1 +q 2
2 −µ(q 2 −q 1)

= qb −q g
2 +µ(q 2 −q 1)−µ=A 2.
Step 4:V ′(0+) =−q 1A1f− −q 2A2f+ andV ′(1−) =−q 1A1f+ −q 2A2f−.
Proof of Step 4: Sinceϕ′ 1(R) =−f(R− 1 2 )andϕ ′ 2(R) =−f( 1 2 −R),
V ′(R) =−q 1A1 f(R− 1 2 )−q 2A2 f( 1 2 −R)
near the extremes. Letf− :=f(− 1 2 )andf + :=f( 1 2 ). Taking limits in the expression for
V ′(R)gives the result.
Step 5:Condition(6)is equivalent toV ′(0+)>0andV ′(1−)<0.
Proof of Step 5: Since Assumption 2 impliesf(1 2 )>0, we have
V ′(0+)>0⇐ ⇒q 1A1f(− 1 2 ) +q 2A2f( 1 2 )<0,
and
V ′(1−)<0⇐ ⇒q 1A1f( 1 2 ) +q 2A2f(− 1 2 )>0.
Thus condition (6) is equivalent toV′(0+)>0andV ′(1−)<0.
Step 6:V(R)has an interior maximumR ∗ ∈(0,1).
Proof of Step 6: According to Step 5, condition (6) impliesV′(0+)>0andV ′(1−)<0.
26

Hence, for any decision environmentE, there existsδ(E)>0such thatVis strictly
increasing on(0, δ(E))and strictly decreasing on(1−δ(E),1). Thus the supremum ofV
over(0,1)equals the supremum ofVover some compact interval[δ(E),1−δ(E)]⊂(0,1).
SinceVis continuous inR, 31 the extreme value theorem implies thatV(R)attains its
maximum on[δ(E),1−δ(E)], and hence on(0,1), at someR ∗ ∈(0,1).
A.2.5 Proof of Proposition 6
Throughout this proof, we use the identitiesqg = (1−2Q)σ/(1+σ)andq b = (1−2Q)/(1+
σ). Since Proposition 6 assumesQ≤ ¯Q(a, σ), Lemma OA.1 implies that all receiver types
are obedient for everyR∈(0,1). Hence Proposition 3(i) applies throughout, yielding
V(R) =π L[∆L O −∆ L SE[i]].In Example 1,ϕ 1(R) = 1−R a,ϕ 2(R) = (1−R) a, and
E[i] = a−1 2(a+1), so that
V(R) = (1−2Q)σ(Q(σ−1) + 1) (σ+ 1) 2 + Q a+ 1 (1−R a)  a−(a+ 1)  (1−2Q)σ 1 +σ +Q 
+ Q a+ 1 (1−R) a

1−(a+ 1)
 (1−2Q)σ
1 +σ +Q

=c 0 + Q a+ 1 [c1(a)(1−R a) +c 2(a)(1−R) a]
withc 0 = (1−2Q)σ(Q(σ−1)+1) (σ+1)2 ,c 1(a) =a+ (a+ 1) Q(σ−1)−σ σ+1 andc 2(a) = 1 + (1 +a) Q(σ−1)−σ σ+1 .
We thus obtain
V ′(R) =− Qa a+ 1  Ra−1c1(a) + (1−R) a−1c2(a)  ,
V ′′(R) =− Qa(a−1) a+ 1  Ra−2c1(a)−(1−R) a−2c2(a)  ,
SinceR a−1 >0and(1−R) a−1 >0on(0,1)andQa/(a+ 1)>0, the sign ofV ′(R)is
determined by the signs ofc1(a)andc 2(a), which can be written as
c1(a) = σ[Q(a+ 1)−1] +a−Q(a+ 1) σ+ 1 ,
c2(a) = σ[Q(a+ 1)−a] + 1−Q(a+ 1) σ+ 1 .
Solvingc 1(a) = 0andc 2(a) = 0givesσ ∗ 1 := a−Q(a+1) 1−Q(a+1) andσ ∗ 2 := 1−Q(a+1) a−Q(a+1) .IfQ <
min{a,1}/(a+ 1), then the numerators ofc 1(a)andc 2(a)are strictly decreasing affine
functions ofσwith positive intercepts. Therefore
c1(a), c2(a)≥0⇐ ⇒σ≤min{σ ∗ 1, σ∗ 2},
31Since payoffs are bounded and, for every typei, the receiver’s ex ante payoff under standardRis a
continuous function ofR, the value functionV(R)is continuous by the dominated convergence theorem.
27

c1(a), c2(a)≤0⇐ ⇒σ≥max{σ ∗ 1, σ∗ 2}.
Hence, ifQ <min{a,1}/(a+1),Vis decreasing exactly ifσ≤min{σ ∗ 1, σ∗ 2}and increasing
exactly ifσ≥max{σ ∗ 1, σ∗ 2}.
If insteadQ≥min{a,1}/(a+ 1), these two monotone cases cannot occur. To see this,
first supposea >1, so that the cutoff equals1/(a+ 1). SinceQ <1/2< a/(a+ 1),
we haveQ(a+ 1)−1≥0anda−Q(a+ 1)>0,and hencec 1(a)>0for everyσ >0.
Moreover,Q(a+ 1)−a <0and1−Q(a+ 1)≤0,so thatc 2(a)<0for everyσ >0. Thus
c1(a)>0> c 2(a).
Now supposea <1, so that the cutoff equalsa/(a+ 1). SinceQ <1/2<1/(a+ 1),
we haveQ(a+ 1)−1<0anda−Q(a+ 1)≤0and hencec 1(a)<0for everyσ >0.
Moreover,Q(a+ 1)−a≥0,and1−Q(a+ 1)>0,soc 2(a)>0for everyσ >0. Thus
c1(a)<0< c 2(a). Therefore, at and above the cutoffmin{a,1}/(a+ 1), the coefficients
have opposite signs for everyσ >0. Together with the caseQ <min{a,1}/(a+ 1)and
min{σ∗ 1, σ∗ 2}< σ <max{σ∗ 1, σ∗ 2},
this is exactly the region wherec1(a)andc 2(a)have opposite signs. Since
c1(a)−c 2(a)



<0ifa <1,
>0ifa >1,
the mixed-sign case meansc1(a)>0> c 2(a)whena >1, andc 1(a)<0< c 2(a)when
a <1. In either case,
V ′′(R) =− Qa(a−1) a+ 1  Ra−2c1(a)−(1−R) a−2c2(a)  <0for allR∈(0,1),
soVis strictly concave on(0,1). To conclude that the maximum is interior, we also check
the derivatives atR= 0andR= 1. Ifa >1andc 1(a)>0> c 2(a), then
V ′(0+) =− Qa a+ 1 c2(a)>0, V ′(1−) =− Qa a+ 1 c1(a)<0.
Ifa <1andc 1(a)<0< c 2(a), thenR a−1c1(a)→ −∞asR↓0while(1−R) a−1c2(a)→
c2(a), soV ′(0+)>0; similarly,(1−R) a−1c2(a)→+∞asR↑1, soV ′(1−)<0. Hence
Vincreases near0and decreases near1, and strict concavity implies a unique interior
maximizerR ∗ ∈(0,1).
Combining the casesQ≥min{a,1}/(a+ 1)andQ <min{a,1}/(a+ 1)proves Propo-
sition 6.
28

A.3 Sales Maximization
A.3.1 Proof of Proposition 8
We showD(R)≤D(0)for allR >0. Let ˆF(R)∈[0,1]denote the fraction of receiver
types that buy a product with a like at standardR. Then the claim is equivalent to
πL(R) ˆF(R) + (1−π L(R))(1− ˆF(R))≤q g +q 1 +q 2.(11)
FixR >0. Then the left-hand side of (11) equals
πL(R) ˆF(R) + (1−π L(R))(1− ˆF(R)) = (1−π L(R)) + (2πL(R)−1) ˆF(R).
As a function of ˆF(R)∈[0,1]this expression is affine, hence it is bounded above by its
endpoint values:
πL(R) ˆF(R) + (1−π L(R))(1− ˆF(R))≤max{1−π L(R), πL(R)}.
Next, by definitionπL(R) =q g +q 1ϕ1(R) +q 2ϕ2(R)withϕ 1, ϕ2 ∈[0,1], so
πL(R)≤q g +q 1 +q 2 =D(0).
Moreover, sinceϕ 1, ϕ2 ≥0, we also haveπ L(R)≥q g. Under the assumptionqg ≥q b and
usingq g +q 1 +q 2 = 1−q b, it follows that
1−π L(R)≤1−q g ≤1−q b =q g +q 1 +q 2 =D(0).
Therefore bothπ L(R)and1−π L(R)are at mostD(0), implying
max{1−π L(R), πL(R)} ≤D(0).
Combining the inequalities yields (11), henceD(R)≤D(0)for allR >0. Consequently,
sales are maximized asR→0.
A.4 Further Results
A.4.1 Optimal Pricing
Proof of Proposition 9
The proof will follow from Steps 1-4 below.
Step 1.The unique unrestricted profit maximizer is
P u(R) = qg + 2Q(1−R) 4Q .
29

FixR∈(0,1)and consider pricesP∈[0,1−R]. For a uniform type distribution
andq 1 =q 2 =Q, a sender gives a like for each controversial variant with probability
1−T= 1−R−P. Hence
πL(R+P) =q g +q 1(1−R−P) +q 2(1−R−P) =q g + 2Q(1−R−P).
Ignoring the demand constraint in (7), the firm’s (unrestricted) profit is
Πu(P;R) :=P π L(R+P) =P  qg + 2Q(1−R−P)  .
This function is strictly concave inP(sinceQ >0), and its first-order condition is
∂Πu(P;R)
∂P =q g + 2Q(1−R−P)−2QP=q g + 2Q(1−R)−4QP= 0.
This first-order condition yields
P u(R) = qg + 2Q(1−R) 4Q .
This is the unconstrained maximizer of the quadratic objectiveΠu(P;R). It need not
lie in the admissible interval[0,1−R], so at this stage it is not yet the solution to the
constrained pricing problem.
Step 2.The objective content of the rating system satisfies
∆L O(R+P) = 1 2 −q g −Q+ qg 2  qg + 2Q(1−R−P)  .
Sales are positive if and only if the acceptance constraint in (7) holds, i.e. if and only
ifP≤∆ L O(R+P).Underq 1 =q 2 =Qand uniform types,∆ L S = 0, so∆ L O(R+P) =
U L(i)−U 0(i)is the common willingness to pay after a like for all typesi. Moreover, the
posterior probability of a good product afterLis
pL g (R+P) = qg qg + 2Q(1−R−P) ,
and the posterior probabilities of the two controversial variants are equal. Plugging these
posteriors into Definition 3(i) yields the result.
Step 3:The acceptance gapγ(P) := ∆L O(R+P)−Pis strictly decreasing on[0,1−R].
Differentiatingγgives
γ′(P) = qgQ
qg + 2Q(1−R−P)
2 −1.
For allP∈[0,1−R]we haveq g + 2Q(1−R−P)≥q g, hence
qgQ
qg + 2Q(1−R−P)
2 ≤ qgQ q2 g = Q qg <1,
where the strict inequality uses the assumptionqg > Q. Thereforeγ′(P)<0on[0,1−R].
30

Moreover,γ(0) = ∆ L O(R)>0. To see this, note that
∆L O(R) = pL g (R)−q g +q b 2 .
SinceR∈(0,1)andQ >0, we haveq g + 2Q(1−R)< q g + 2Q= 1−q b <1, so
pL g (R) =q g/(qg + 2Q(1−R))> q g. Hencep L g (R)−q g +q b >0, provingγ(0)>0.
Therefore the feasible setn
P∈[0,1−R] :P≤∆ L O(R+P) o = n P∈[0,1−R] :γ(P)≥0 o
Sinceγis continuous and strictly decreasing, this feasible set is a nonempty compact
interval of the form[0, ¯P(R)], where ¯P(R) := max{P∈[0,1−R] :γ(P)≥0}. If
γ(1−R)≤0, then ¯P(R)is the unique root ofγin[0,1−R], characterized byγ( ¯P(R)) = 0,
i.e. ¯P(R) = ∆ L O(R+ ¯P(R)). If insteadγ(1−R)>0, then ¯P(R) = 1−Rand every price
in[0,1−R]is feasible.
Step 4:The unique maximizer on[0, ¯P(R)]isP ∗(R) = min{P u(R), ¯P(R)}.
From Step 3, the original problem reduces to maximizing the strictly concave quadratic
Πu(P;R)over the interval[0, ¯P(R)]. SinceP u(R)is the unconstrained maximizer from
Step 1, the unique constrained maximizer is
P ∗(R) =



P u(R),ifP u(R)≤ ¯P(R),
¯P(R),ifP u(R)> ¯P(R).
Equivalently,
P ∗(R) = min{P u(R), ¯P(R)}.
Since ¯P(R)≤1−R, this formula automatically respects the admissible price restriction
P∈[0,1−R].
A.4.2 Multiple ratings
We now derive some auxiliary results for the case of multiple ratings, before we prove
Proposition 10.
Afterblikes andddislikes, whereb+d >0, the posterior reads
pg(b, d) =



qg
qg+q1(ϕ1(R))b+q2(ϕ2(R))b ifd= 0
0ifd >0
p1(b, d) = q1(ϕ1(R))b(1−ϕ 1(R))d
q1(ϕ1(R))b(1−ϕ 1(R))d +q 2(ϕ2(R))b(1−ϕ 2(R))d
p2(b, d) = q2(ϕ2(R))b(1−ϕ 2(R))d
q1(ϕ1(R))b(1−ϕ 1(R))d +q 2(ϕ2(R))b(1−ϕ 2(R))d
pb(b, d) =



qb
q1(1−ϕ1(R))d+q2(1−ϕ2(R))d+qb ifb= 0
0ifb >0
31

Theformulasforp 1 andp 2 arestatedforb, d >0, whereobjectivelygoodandbadproducts
are ruled out. Whend= 0orb= 0,p 1 andp 2 follow fromp g +p 1 +p 2 +p b = 1and the
ratiop 1/p2 =q 1ϕb 1(1−ϕ 1)d/[q2ϕb 2(1−ϕ 2)d].
Lemma A.3Consider the model with multiple ratings. Suppose Assumption 1 holds and
consider any standardR∈(0,1).
(i) If the receiver obtains only likes (dislikes), then, as the number of ratings increases,
her posterior belief converges topg = 1(p b = 1).
(ii) If the receiver obtains mixed ratings, thenp1(b, d)/p2(b, d) =q 1/q2 andp g(b, d) =
pb(b, d) = 0for anyb, d >0.
Proof.(i) Suppose the receiver gets only likes and thatb→ ∞. Then,ϕ1(R) =ϕ 2(R) =:
ϕ. SinceFhas full support andR∈(0,1),ϕ∈(0,1), so thatlim b→∞(ϕi(R))b = 0for
i= 1,2. Hence,lim b→∞ pg(b,0) = 1. The argument for dislikes is analogous.
(ii) For anyb, d >0,pg(b, d) =pb(b, d) = 0obviously holds. Further, becauseϕ1(R) =
ϕ2(R)by Assumption 1,p i(b, d) = qi q1+q2 fori= 1,2, yielding statement (ii).
Proof of Proposition 10
The proof will follow from Steps 1-4 below. We use the notationb(i) := q1 q1+q2

1
2 +i

+
q2
q1+q2

1
2 −i

−U 0(i)for the receiver’s gain from buying a controversial product after
infinitely many ratings, relative to the outside option.
Step 1:the value of the infinite-learning system is
V∞ =q g(1−q g −Q) + 2QE

b(i)+ , b(i) + := max{b(i),0}.
By Lemma A.3, infinite learning perfectly reveals objectively good and bad products,
while mixed ratings identify a controversial product but not its variant. Hence, (i) good
products are always bought, (ii) bad products are never bought, and (iii) controversial
products are bought exactly by those types withb(i)≥0. Thus, the result holds.32
Step 2:The optimally designed single-rating system gives the value
V ∗ 1 =q g(1−q g −Q) + 2Qmax{E[b(i)],0}.
Under Assumption 1, Proposition 4 implies that the optimal single-standard design is
extreme:
•ifσ <1, the designer choosesR→0, so all controversial products are bought;
32The first term is the gain from correctly identifying objectively good products: a good product yields
payoff 1, while the outside option yieldsE[U0(i)] =q g +Qunder symmetricF, so the gain isqg(1−q g −Q).
Objectively bad products contribute zero because they are identified and not bought.
32

•ifσ >1, the designer choosesR→1, so no controversial product is bought;
•ifσ= 1, all standards are optimal.
Hence the benchmark value isV∗ 1 =q g(1−q g −Q) + 2Qmax{E[b(i)],0}.
Step 3:V ∞ =V ∗ 1 ⇐ ⇒b(i)has a constant sign almost surely.
Sinceb=b + −b − withb − := max{−b,0}, we haveE[b +]≥max{E[b],0}.Moreover,
•ifE[b]≥0, thenE[b +]−E[b] =E[b −], so equality requiresb− = 0a.s.;
•ifE[b]≤0, thenE[b +] = 0requiresb + = 0a.s.
Thus the claim holds.
Step 4:b(i)has a constant sign almost surely if and only if one of the following holds:
(i)λ= 1;(ii)λ >1andσ /∈
 1
λ , λ

;(iii)λ <1andσ /∈

λ, 1 λ  .
Usingq 1 = 2Qλ λ+1,q 2 = 2Q λ+1, andq g = (1−2Q)σ 1+σ :
b(i) = (1−2Q)(λ−1) λ+ 1 (i− ˜i∞), ˜i∞ = σ−1 2(1 +σ) λ+ 1 λ−1 .
Case 1:λ= 1.Thenb(i)is constant ini, so it has a constant sign a.s. Hence
V∞ =V ∗ 1 .
Case 2:λ >1.Thenb(i)is strictly increasing ini. BecauseFhas full support on
[−1/2,1/2],b(i)has a constant sign a.s. iff ˜i∞ ≤ −1/2or˜i∞ ≥1/2. The first inequality
is equivalent toσ≤1/λ, and the second toσ≥λ. HenceV ∞ =V ∗ 1 ⇐ ⇒σ /∈(1/λ, λ).
Case 3:λ <1.Thenb(i)is strictly decreasing ini. By the same argument,b(i)
has a constant sign a.s. iff˜i∞ ≥1/2or ˜i∞ ≤ −1/2. Nowλ−1<0, so the direction of
the inequalities reverses: ˜i∞ ≥1/2givesσ≤λ, and ˜i∞ ≤ −1/2givesσ≥1/λ. Hence
V∞ =V ∗ 1 ⇐ ⇒σ /∈(λ,1/λ).
At the boundary values (e.g.,σ= 1/λwithλ >1), ˜i∞ =−1/2, sob(−1/2) = 0and
b(i)>0fori >−1/2. Under full support with continuousF, zero at a single point has
measure zero, sob≥0a.s. The boundary belongs to the equality region, yielding the
open intervals in the statement.
A.4.3 Distinct Sender and Receiver Distributions
We prove the following result:
Proposition A.1Consider the model with distinct preference distributions of senders
and receivers. Suppose the sender distributionFsatisfies Assumption 1. Then, all types
are obedient. Further,V(R) =π L F [∆L O,F −∆ L S,F EG[i]]is
33

(i) decreasing inRifσ < Q+(q1−q2)EG[i] Q−(q1−q2)EG[i];
(ii) increasing inRifσ > Q+(q1−q2)EG[i] Q−(q1−q2)EG[i];
(iii) constant inRifσ= Q+(q1−q2)EG[i] Q−(q1−q2)EG[i].
Proof.
The value of the rating system can be written as
V(R) =



R 1/2
−1/2(VA,F (i)−V 0,F (i))dG(i)if|∆ L S,F | ≤2∆L O,F
R ˜i
−1/2 VN,F (i)dG(i) +
R 1/2
˜i VA,F (i)dG(i)−
R 1/2
−1/2 V0,F (i)dG(i)if∆ L S,F <−2∆ L O,F
R ˜i
−1/2 VA,F (i)dG(i) +
R 1/2
˜i VN,F (i)dG(i)−
R 1/2
−1/2 V0,F (i)dG(i)if∆ L S,F >2∆ L O,F
and the result from Proposition 3 translates accordingly so that we can rewriteV(R)as
πL[∆L O,F −∆ L S,F EG[i]]if|∆ L S,F | ≤2∆L O,F
(1−π L)G(˜i)  ∆D O,F −∆ D S,F EG[i|i≤ ˜i]  +π L(1−G( ˜i))  ∆L O,F −∆ L S,F EG[i|i≥ ˜i]  if∆ L S,F <−2∆ L O,F
πLG(˜i)  ∆L O,F −∆ L S,F EG[i|i≤ ˜i]  + (1−π L)(1−G( ˜i))  ∆D O,F −∆ D S,F EG[i|i≥ ˜i]  if∆ L S,F >2∆ L O,F .
SinceFsatisfies Assumption 1, all receivers will be obedient so that we are in the case
|∆L S,F | ≤2∆L O,F. Thus, we have
V(β) =π L[∆L O,F −∆ L S,F EG[i]]
=q g +βQ−(q g + 2βQ)(qg +Q) + (q 2 −q 1)(qg −β(1−2Q))E G[i]
and thereforeV ′(β) =Q−2Q(q g +Q)−(q 2 −q 1)(1−2Q)E G[i]. Replacingq g = ((1−
2Q)σ)/(σ+ 1)and rearranging the inequalitiesV ′(β)>0andV ′(β)<0yields the
statement in the proposition.
A.4.4 Polarization and the Prevalence of Controversial Products
Polarization.Under Assumption 1, polarization affects the rating system through
β=F(1/2−R),the share of senders who recommend a controversial product at rat-
ing standardR. By Lemma A.2, the value of the rating system is strictly increasing inβ
whenσ <1, strictly decreasing inβwhenσ >1, and independent ofβwhenσ= 1.
Figure 3 illustrates such a change inβ. The intuition is that a higherβmakes likes
more frequent but less objectively informative. To see this, supposeσ <1andR >1/2.
As shown in Figure 1, whenR >1/2, only sufficiently extreme types issue likes for
controversial products. Hence a higherβmeans that likes are more likely to stem from
controversial rather than objectively good products. This raises the probability of likes
while lowering their objective value. When good products are rare, the frequency effect
dominates; when good products are common, the informativeness effect dominates.
34

Figure 3. Population polarization
i
-0.5 -0.25 0 0.25 0.5
β= 1 2
β= 0
1
1
2
Notes:We have fixedR= 3/4. The dotted and dashed lines both correspond to symmetric type
distributionsF, whereβ= 1/2for the dotted line andβ= 0for the dashed line. A move fromβ= 0to
β= 1/2illustrates a symmetric shift in the type distribution that increases the share of types willing to
recommend a controversial product at the fixed standardR= 3/4.
The impact of preference heterogeneity on sales is straightforward. Under Assump-
tion 1, all types are obedient so sales equal the probability of a like and are therefore
increasing inβ. Thus, shifts that increaseβalso increase sales.
Prevalence of Controversial Products.The following lemma gives the comparative
statics ofVinQ:
Lemma A.4Suppose Assumption 1 holds.
(i) If3σ−β−σ 2 +σ 2β >0, then the value of the rating system is decreasing inQ. In
particular, this is the case whenσ= 1.
(ii) If3σ−β−σ 2 +σ 2β <0, thenQ ∗ := 3σ−β−σ 2+σ2β 4σ−4β−4σ 2+4σ2β ∈(0, 1 2 )maximizesV(R).
Proof.
We first take the derivative ofVwith respect toQto obtain
∂V
∂Q = 1 (σ+ 1) 2  β−3σ+ 4Qσ−4Qβ+σ 2 −4Qσ 2 −σ 2β+ 4Qσ 2β 
Grouping theQ-terms, this can be written in affine form as
∂V
∂Q = −(3σ−β−σ 2 +σ 2β) + 4Q(σ−β−σ 2 +σ 2β) (σ+ 1) 2 ,
which is linear inQ.
Proof of (i).Suppose3σ−β−σ 2 +σ 2β >0. Straightforward calculations show that
∂V /∂Qis negative forQ= 0and negative forQ= 1/2. Because it is affine inQ, it is
thus negative throughout(0,1/2). HenceVis decreasing inQ, proving (i). In particular,
atσ= 1,3σ−β−σ 2 +σ 2β= 2for everyβ∈[0,1], so (i) applies.
35

Proof of (ii).Suppose3σ−β−σ 2 +σ 2β <0. Setting∂V /∂Qequal to zero and solving
for the candidate solution we obtain
Q∗ = 3σ−β−σ 2 +σ 2β 4σ−4β−4σ 2 + 4σ2β
Next, the SOC reads4σ−4β−4σ 2 + 4σ2β <0,where the l.h.s. of the SOC is the
denominator ofQ ∗. Using the identity4σ−4β−4σ 2 + 4σ2β= 4(3σ−β−σ 2 +σ 2β)−8σ,
the condition3σ−β−σ 2 +σ 2β <0(together withσ >0) implies the SOC holds. Hence,
the candidate solution is positive. It remains to show thatQ ∗ < 1 2. The requirement
3σ−β−σ 2+σ2β
4σ−4β−4σ 2+4σ2β <1/2becomes
2σ−2β−2σ 2 + 2σ2β <3σ−β−σ 2 +σ 2β,
becausethedenominatoroftheratioisnegative. Equivalently,(σ+ 1) (σ(1−β) +β)>0,
which always holds forβ≤1.
As an immediate consequence we obtain:
Corollary A.1Suppose Assumption 1 holds. Then for everyβ∈(0,1), there exist
σ(β)∈(0,1)and σ(β)>1such that
(i) the value of the rating system is decreasing inQon(σ(β), σ(β)).
(ii) Forσ < σandσ > σ, the value of the rating system is maximized for someQ∗ >0.
Figure 4. Illustration of Corollary A.1
Panel A
σ
β
1 3 5 7 9
0.2
0.4
0.6
0.8
1.0
Panel B
σ
β
1 3 5 7 9
0.2
0.4
0.6
0.8
1.0
Panel C
σ
β
1 3 5 7 9
0.2
0.4
0.6
0.8
1.0
Notes:In Panel A, the shaded area indicates the parameter space for which an interior solution forQ
arises by Corollary A.1. In Panel B, the shaded area indicates whereπL is increasing inQ. In Panel C,
the shaded area indicates where∆L O is increasing inQ, illustrated forQ= 0.1.
Figure 4 illustrates the result. In the white area in Panel A,V(Q)is decreasing inQ; in
the shaded area, an interior maximizer exists. When objectively good and bad products
are similarly likely (σis close to1), a higher prevalence of controversial products indeed
reducesV(Q). For very high or low values ofσ, however, this need not be true. This
36

surprising result reflects the multiplicative structure ofV(Q). Under Assumption 1,V(Q)
is the product of the buying probabilityπL and the objective value of the rating per buyer,
∆L O. TheeffectofQonπ L isnegativeonlyifσissufficientlylarge(seePanelB).Intuitively,
asQincreases, objectively good products are less likely, reducing the probability of likes.
However, there are now more likes stemming from controversial products, as these have
become more likely.βandσdetermine which of these effects dominates. Whenβis
high, the greater likelihood that controversial products receive likes increases the total
probability of likes, strengthening the positive effect. Whenσis high, the lower share
of objectively good products dominates, strengthening the negative effect. Similarly, one
can show that the effect ofQon∆ L O becomes negative only for smallσ(see Panel C),
reflecting the increased probability that a product with a like is controversial.33
33There is also a positive effect of higherQ, reflecting a change in the value of the outside option. The
values ofσandβdetermine which effect dominates.
37

References
Acemoglu, D., A. Makhdoumi, A. Malekian, and A. Ozdaglar(2022): “Learning
from reviews: The selection effect and the speed of learning,”Econometrica, 90, 2857–
2899.
Banerjee, A. V.(1992): “A Simple Model of Herd Behavior,”The Quarterly Journal
of Economics, 107, 797–817.
Bikhchandani, S., D. Hirshleifer, and I. Welch(1992): “A Theory of Fads, Fash-
ion, Custom, and Cultural Change as Informational Cascades,”Journal of Political
Economy, 100, 992–1026.
Bohren, N., R. Hakimov, and L. Santos-Pinto(2025): “Beyond the Stars: Explor-
ing the Welfare Effects of Ratings in Differentiated Markets,” Working paper, University
of Lausanne; AEA Registry AEARCTR-0011386.
Bolton, G., B. Greiner, and A. Ockenfels(2013): “Engineering trust: reciprocity
in the production of reputation information,”Management Science, 59, 265–285.
Bourreau, M. and G. Gaudin(2022): “Streaming Platform and Strategic Recommen-
dation Bias,”Journal of Economics and Management Strategy, 31, 25–47.
Carnehl, C., A. Stenzel, and P. Schmidt(2024): “Pricing for the Stars: Dynamic
Pricing in the Presence of Rating Systems,”Management Science, 70, 1755–1772.
Chakraborty, A. and R. Harbaugh(2010): “Persuasion by Cheap Talk,”American
Economic Review, 100, 2361–2382.
Che, Y.-K. and J. Hörner(2018): “Recommender systems as mechanisms for social
learning,”The Quarterly Journal of Economics, 133, 871–925.
Chen, P.-Y., L. M. Hitt, Y. Hong, and S. Wu(2021): “Measuring Product Type
and Purchase Uncertainty with Online Product Ratings: A Theoretical Model and
Empirical Application,”Information Systems Research, 32, 1470–1489.
Hopenhayn, H. and M. Saeedi(2026): “Optimal Simple Ratings,”The Journal of
Industrial Economics.
Hospitable(2024): “Understanding Airbnb Ratings: How They Work and How to Im-
prove Them,” Accessed: March 12, 2025.
Ifrach, B., C. Maglaras, M. Scarsini, and A. Zselev a(2019): “Bayesian Social
Learning from Consumer Reviews,”Operations Research, 67, 1209–1221.
38

Johnen, J. and R. Ng(2024): “Harvesting Ratings,” Working Paper, CORE/LIDAM,
UCLouvain and University of Mannheim.
Kamenica, E. and M. Gentzkow(2011): “Bayesian Persuasion,”American Economic
Review, 101, 2590–2615.
Lafky, J. and R. Ng(2024): “Ratings with Heterogeneous Preferences,” Discussion
Paper No. 594, CRC TR 224, University of Bonn and University of Mannheim.
Li, X. and L. M. Hitt(2008): “Self-Selection and Information Role of Online Product
Reviews,”Information Systems Research, 19, 456–474.
Lizzeri, A.(1999): “Information Revelation and Certification Intermediaries,”The
RAND Journal of Economics, 30, 214–231.
Peitz, M. and A. Sobolev(2025): “Inflated Recommendations,”The RAND Journal
of Economics.
Rayo, L. and I. Segal(2010): “Optimal Information Disclosure,”Journal of Political
Economy, 118, 906–948.
Shi, Z. M. and T. S. Raghu(2020): “An Economic Analysis of Product Recommenda-
tion in the Presence of Quality and Taste-Match Heterogeneity,”Information Systems
Research, 31, 399–411.
Smirnov, A. and E. Starkov(2025): “Designing Social Learning,”European Economic
Review, 178.
Smith, L. and P. Sørensen(2000): “Pathological Outcomes of Observational Learn-
ing,”Econometrica, 68, 371–398.
Sun, M.(2012): “How Does the Variance of Product Ratings Matter?”Management
Science, 58, 696–707.
Tadelis, S.(2016): “Reputation and feedback systems in online platform markets,”
Annual Review of Economics, 8, 321–340.
Uber(2024): “Understanding Driver Ratings,” Accessed: March 12, 2025.
39

OA Online Appendix
OA.1 Value of Rating Systems
OA.1.1 Universal Obedience in Example 1
Recall that, for the economic analysis, we maintain the assumptions thatR∈(0,1)and
qs >0fors, implyingQ <1/2. For continuity and convexity arguments, we occasionally
extend functions ofRandQto the closures[0,1]and[0,1/2].
The following two lemmas supply the exact cutoff¯Q(a, σ)invoked informally before
Proposition 6, clarifying under which conditions the requirement that all receivers are
obedient is satisfied.1 Lemma OA.1 establishes existence, uniqueness, and an explicit
characterization fora >1. Lemma OA.2 describes how the cutoff varies witha.
Lemma OA.1Suppose we are in Example 1. Then, for every(a, σ)∈ R+ × R+, there
exists a unique cutoff ¯Q(a, σ)∈(0,1/2]such that receivers are universally obedient for
(Q, a, σ)if and only ifQ≤ ¯Q(a, σ). Moreover:
(i) Fora= 1and every(Q, σ)∈(0,1/2)× R +, receivers are universally obedient for
(Q, a, σ).
(ii) Fora >1and(Q, σ)∈(0,1/2)× R +, receivers are universally obedient for(Q, a, σ)
if and only if
N(R;Q, a, σ) :=qgqb −Q 2 +Q(q b +Q)(1−R) a +Q(q g +Q)R a ≥0
for allR∈(0,1).
(iii) Fora <1, receivers are universally obedient if and only if
˜N(R;Q, a, σ) :=qgqb −Q 2 +Q(q b +Q)(1−R a) +Q(q g +Q)  1−(1−R) a ≥0
for allR∈(0,1).
Proof.In Steps 1-7, we establish the lemma fora≥1. Steps 1 and 2 hold for alla. In
Example 1,F(i) = (i+ 1/2) a andq 1 =q 2 =Q, soϕ 1(R) = 1−R a andϕ 2(R) = (1−R) a.
To simplify notation, we sets a(R) :=ϕ 1(R) +ϕ 2(R)andb a(R) :=ϕ 2(R)−ϕ 1(R) =
Ra + (1−R) a −1,
Step 1.We have
∆L S(R) = Q ba(R) πL(R) ,∆ L O(R) = qg + Q 2 sa(R) πL(R) −(q g +Q).
1Whenever we write ¯Q(a, σ) = 1/2, this should be understood as a boundary statement: universal
acceptance then holds for every admissibleQ <1/2.
1

Proof of Step 1:In Example 1, the probability of like isπL(R) =q g +Qs a(R)>0.
The posteriors after a like arePL g =q g/πL,p L 1 =Qϕ 1/πL, andp L 2 =Qϕ 2/πL, so Step 1
follows from by Definition 3.
Step 2.(i)Fora >1,∆ L S(R)<0. (ii)Fora= 1,∆ L S ≡0,so that all types are
universally obedient. (iii)Fora <1,∆ L S(R)>0.
Proof of Step 2: Fora >1, strict convexity ofx7→x a on[0,1]givesb a(R)<0
on(0,1), hence∆ L S(R)<0. Fora= 1,b a ≡0, so∆ L S ≡0and Lemma 1 implies that
receivers are universally obedient; in particular¯Q(1, σ) = 1/2, proving (ii). Fora <1,
strict concavity ofx7→x a givesb a(R)>0, hence∆ L S(R)>0.
Step 3.Fora >1, the objective rating effect∆ L O(R)>0is strictly positive for all
R∈[0,1].
Proof of Step 3:Multiplying∆ L O(R)byπ L(R), substitutingπ L =q g +Qs a and
rearranging yieldsπL(R)∆L O(R) =q gqb + Q 2  sa(R)qb +(2−s a(R))qg  .Since0≤s a(R)≤2
andq g, qb >0forQ <1/2, both summands are nonnegative and the first is strictly
positive. Hence∆ L O(R)>0for allR∈(0,1), and by continuity the same inequality
extends to the boundary pointsR= 0andR= 1.
Step 4.For(Q, a, σ)witha >1,receivers are universally obedient if and only if
N(R;Q, a, σ)≥0for allR∈(0,1).
Proof of Step 4:By Corollary 1, all receiver types are obedient for the standard
Rif and only if|∆ L S(R)| ≤2∆L O(R). Since∆ L S <0fora >1, this is equivalent to
∆L O(R) + 1 2 ∆L S(R)≥0. Multiplying byπ L(R)>0and substituting the closed forms from
Step 1 gives
πL(R)  ∆L O(R) + 1 2 ∆L S(R)  =q g + Q 2  sa(R) +b a(R)  −(q g +Q)π L(R)≥0
Usings a(R)+b a(R) = 2(1−R) a andπ L(R) =q g +Qsa(R) =q g +Q  1−R a +(1−R) a , this
rearranges toπ L(R)  ∆L O(R) + 1 2 ∆L S(R)  =N(R;Q, a, σ)≥0.Therefore, for(Q, a, σ)
receivers are universally obedient if and only ifN(R;Q, a, σ)≥0for allR∈(0,1).
BecauseNextends continuously to[0,1], this is equivalent toN(R;Q, a, σ)≥0for all
R∈[0,1].
Step 5.For all(a, σ)∈(1,∞)× R +,there existsε(a, σ)>0such that all receivers
are obedient for all(a, σ, Q)such thatQ≤ε(a, σ)and allR∈(0,1).
Proof of Step 5:Since|b a(R)|is continuous on the compact interval[0,1],C a :=
maxR∈[0,1] |ba(R)|<∞. Usingπ L(R)≥q g from Step 1,|∆ L S(R)| ≤QCa/qg for everyR.
From Step 3,πL∆L O ≥q gqb, andπ L(R)≤q g +2Qsinces a ≤2, so∆ L O(R)≥q gqb/(qg +2Q).
2

AsQ↓0,
QCa
qg
→0, 2qgqb
qg + 2Q → 2 1 +σ >0.
Hence there existsε(a, σ)>0such that|∆ L S(R)|<2∆ L O(R)uniformly inR∈[0,1]for
everyQ≤ε(a, σ). By Corollary 1, receivers are universally obedient for every suchQ, a, σ.
Step 6.DefineS(a, σ) :=

Q∈[0,1/2)|alliare universally obedient atQ(a, σ)

as the obedience set. Then, fora >1, eitherS(a, σ) = [0, ¯Q(a, σ)]for some ¯Q(a, σ)∈
(0,1/2)orS(a, σ) = [0,1/2).
Proof of Step 6
S(a, σ)is nonempty:More generally, by Step 5,[0, ε(a, σ)]⊆ S(a, σ).
S(a, σ)is downward closed.By Corollary 1, all receivers are obedient for the standard
Rif and only if˜i(R, Q)≤ −1/2. Writingδ:= (σ−1)/(σ+ 1)∈(−1,1), direct differentia-
tion at fixedσ(taking the dependence ofqg = (1−2Q)σ/(1 +σ)andq b = (1−2Q)/(1 +σ)
onQinto account) yields
∂˜i(R, Q)
∂Q =−
Q2 δ(Ra −(1−R) a +δ) + 1−δ 2
4
Q2 ba(R) .(OA.1)
Lettingx:=R a −(1−R) a ∈[−1,1], the boundδ(x+δ)≥ −|δ|(1− |δ|)gives
Q2 δ(x+δ) + 1−δ 2
4 ≥(1− |δ|)
 1 +|δ|
4 −Q 2|δ|

>0
forQ <1/2, so that the numerator in (OA.1) is strictly positive. Fora >1, Step 2
givesb a(R)<0on(0,1), so∂ ˜i(R, Q)/∂Q >0:˜i(R, Q)is strictly increasing inQ. Hence,
if ˜i(R, Q)≤ −1/2at someQ, the same inequality holds at everyQ′ ≤Q; equivalently,
S(a, σ)is downward closed.
S(a, σ)is relatively closed in[0,1/2): DefineG(R, Q) := 2∆L O(R, Q)− |∆L S(R, Q)|. As
Gis continuous on[0,1]×[0,1/2),m(Q) := min R∈[0,1] G(R, Q)exists for everyq∈[0,1/2)
by compactness and is continuous inQ. HenceS(a, σ) ={Q∈[0,1/2) :m(Q)≥0}is
relatively closed in[0,1/2).
Conclusion.Combining non-emptiness, downward closedness and relative closedness,
Step 6 follows. In both cases,¯Q(a, σ) := supS(a, σ)∈(0,1/2].
Step 7. ¯Q(a, σ)<1/2fora >1.
Proof of Step 7:To rule out the possibility that the cutoff reaches the boundary
1/2, we evaluate the continuous extension ofNat the boundary pointQ= 1/2. At
Q= 1/2,q g =q b = 0, soN(R; 1/2, a, σ) =−1 4 + 1 4  Ra + (1−R) a . By strict convexity of
x7→x a fora >1,R a + (1−R) a <1on(0,1), henceN(R; 1/2, a, σ)<0for allR∈(0,1).
3

Now fix anyR 0 ∈(0,1). SinceNis continuous in(R, Q), there existsδ >0such that
N(R 0;Q, a, σ)<0for everyQ∈(1/2−δ,1/2). By Step 4, universal obedience fails at
every suchQ, so ¯Q(a, σ)≤1/2−δ <1/2.
Putting together Steps 1-7 implies the result fora >1.
Step 8.The proposition also holds fora <1.
Sketch of proof:The casea <1is analogous: The main difference is that the
sign of∆ L S changes by Step 2. Therefore, the obedience condition|∆ L S(R)| ≤2∆L O(R)
becomes∆ L O − 1 2 ∆L S ≥0, and the resulting polynomial is again strictly convex on[0,1]
with strictly positive boundary values, so the same chain of arguments delivers a unique
cutoff ¯Q(a, σ)<1/2.
The universal obedience conditions in Lemma OA.1 are formulated as requirements
that, for allR∈(0,1),N(R;Q, a, σ)≥0and ˜N(R;Q, a, σ)≥0must hold, respectively.
We now show that it is sufficient that the requirements hold at specific values ofR.
Corollary OA.1Suppose Example 1 holds.
(i) Fora >1and(Q, σ)∈(0,1/2)× R +, receivers are universally obedient for(Q, a, σ)
if and only ifN(Rmin(Q, a, σ);Q, a, σ)≥0, where
Rmin(Q, a, σ) :=

(qb +Q)/(q g +Q)
1/(a−1)
1 +

(qb +Q)/(q g +Q)
1/(a−1) .
(ii) Fora <1and(Q, σ)∈(0,1/2)× R +, receivers are universally obedient for(Q, a, σ)
if and only if ˜N( ˜Rmin(Q, a, σ);Q, a, σ)≥0, where
˜Rmin(Q, a, σ) := 1
1 +

(qb +Q)/(q g +Q)
1/(a−1) .
Proof.(i) Simple calculations show that
N ′′(R) =a(a−1)Q  (qb +Q)(1−R) a−2 + (qg +Q)R a−2 >0forR∈(0,1).
Thus,N(·;Q, a, σ)is strictly convex on[0,1]. Direct evaluation givesN(0;Q, a, σ) =
qb(qg +Q)>0andN(1;Q, a, σ) =q g(qb +Q)>0.SettingN ′(R) = 0yields
(qg +Q)R a−1 min = (q b +Q)(1−R min)a−1, soR min is the expression in the statement.
SinceNis strictly convex with positive boundary values,N≥0on[0,1]if and only
ifN(R min;Q, a, σ)≥0. The result thus follows from Lemma OA.1.
(ii) Fora <1, direct differentiation gives
˜N ′′(R) =aQ(1−a)  (qb +Q)R a−2 + (qg +Q)(1−R) a−2 >0forR∈(0,1),
4

so ˜N(·;Q, a, σ)is strictly convex on[0,1]. Direct evaluation gives˜N(0;Q, a, σ) =qb(qg +
Q)>0and ˜N(1;Q, a, σ) =qg(qb +Q)>0. Setting ˜N ′(R) = 0yields(q g +Q)(1−
˜Rmin)a−1 = (qb +Q) ˜Ra−1 min, so ˜Rmin is the expression in the statement. Strict convexity with
positive boundary values again implies˜N≥0on[0,1]if and only if ˜N( ˜Rmin;Q, a, σ)≥0.
The result thus follows from Lemma OA.1.
A particularly simple case arises whenσ= 1.
Corollary OA.2Forσ= 1, receivers are universally obedient at(Q, a, σ)if and only if
Q≤ ¯Q(a,1), where
¯Q(a,1) =



2a−2,0< a <1,
1/2, a= 1,
1/[4(1−2 −a)], a >1.
Proof.The result follows from Corollary OA.1 after noting that atσ= 1we have
Rmin = ˜Rmin = 1/2.
To illustrate the result, note that¯Q(2,1) = 1/3, so that, ifa= 2, obedience arises for
quite high prevalence of controversial products.
Lemma OA.2In Example 1, the cutoff ¯Q(a, σ)from Lemma OA.1 is strictly increasing
inaon(0,1), attains its maximum ¯Q(1, σ) = 1/2ata= 1, and is strictly decreasing in
aon(1,∞).
Proof.The value ata= 1is Lemma OA.1(i). We first prove strict monotonicity on
(1,∞); we then give the corresponding argument on(0,1)using the polynomial ˜Nfrom
Lemma OA.1(iii). Throughout, we use the proof of Step 1 in Lemma OA.1 that, for each
a >1, the acceptance setS(a, σ)⊂[0,1/2)is nonempty, downward closed, and relatively
closed, and that ¯Q(a, σ)<1/2.
Step 1:N(R;Q, a, σ)is strictly decreasing inafor fixedR∈(0,1).
Proof of Step 1:By Lemma OA.1(ii), fora >1receivers are universally obedient at
(Q, a, σ)if and only ifN(R;Q, a, σ)≥0for allR∈(0,1); by continuity this is equivalent
to the same condition on[0,1]. Sinceqg andq b depend only on(Q, σ), only the termsRa
and(1−R) a inNdepend ona. Hence
∂N(R;Q, a, σ)
∂a =Q(q b +Q)(1−R) a ln(1−R) +Q(q g +Q)R a lnR <0forR∈(0,1),
because the prefactors are strictly positive whilelnR <0andln(1−R)<0.
Step 2:Supposea 2 > a1 >1.Then ¯Q(a2, σ)≤ ¯Q(a1, σ).
Proof of Step 2:Takea 2 > a1 >1and anyQ∈ S(a 2, σ); by Lemma OA.1,
equivalently any admissibleQ∈[0, ¯Q(a2, σ)]. ThenN(R;Q, a 2, σ)≥0for allR∈
5

(0,1). By Step 1,N(R;Q, a 1, σ)> N(R;Q, a2, σ)≥0for everyR∈(0,1). At the
auxiliary boundary pointsR= 0andR= 1, the valuesN(0;Q, a, σ) =q b(qg +Q)
andN(1;Q, a, σ) =q g(qb +Q)(computed in Step 6 of the proof of Lemma OA.1) are
independent ofaand strictly positive, soN(·;Q, a 1, σ)≥0on[0,1]. HenceQ∈ S(a 1, σ),
which gives ¯Q(a2, σ)≤ ¯Q(a1, σ).
Step 3:Supposea 2 > a1 >1.Then ¯Q(a2, σ)< ¯Q(a1, σ).
Proof of Step 3:Suppose, toward a contradiction, that ¯Q(a1, σ) = ¯Q(a2, σ) =:
¯Q. By Lemma OA.1(ii), ¯Q <1/2, and by the relative closedness ofS(a 2, σ)in the
admissibledomain[0,1/2)establishedinStep7ofthepreviousproof, ¯Q∈ S(a2, σ). Hence
N(R; ¯Q, a2, σ)≥0for allR∈[0,1]. By Step 1, for everyR∈(0,1),N(R; ¯Q, a1, σ)>
N(R; ¯Q, a2, σ)≥0. At the auxiliary boundary points,N(0; ¯Q, a1, σ) =q b(qg + ¯Q)and
N(1; ¯Q, a1, σ) =q g(qb + ¯Q), both of which are strictly positive since¯Q <1/2implies
qg, qb >0. Therefore,m:= min R∈[0,1] N(R; ¯Q, a1, σ)>0.Choose anyδ >0with
¯Q+δ <1/2. The functionNis uniformly continuous on the compact set[0,1]×[¯Q, ¯Q+δ]
(witha 1 andσfixed), so there existsε∈(0, δ]such that

N(R;Q, a1, σ)−N(R; ¯Q, a1, σ)

 < mfor allR∈[0,1]and allQ∈[ ¯Q, ¯Q+ε].
For suchQ,N(R;Q, a 1, σ)>0for allR∈[0,1], so receivers are universally obedient
at(Q, a1, σ). This contradicts the definition of ¯Q(a1, σ)assupS(a 1, σ). We conclude
¯Q(a2, σ)< ¯Q(a1, σ).
Step 4: ¯Q(a, σ)is strictly increasing inaon(0,1).
Proof of Step 4:By Lemma OA.1(iii), fora <1universal acceptance at(Q, a, σ)is
equivalent to ˜N(R;Q, a, σ)≥0for allR∈(0,1), where
˜N(R;Q, a, σ) :=q gqb −Q 2 +Q(q b +Q)(1−R a) +Q(q g +Q)  1−(1−R) a .
For fixedR∈(0,1), only the termsR a and(1−R) a depend ona, so
∂ ˜N(R;Q, a, σ)
∂a =−Q(q b +Q)R a lnR−Q(q g +Q)(1−R) a ln(1−R)>0,
sincelnR <0andln(1−R)<0. Hence, if0< a 1 < a2 <1andQ∈ S(a 1, σ), then
˜N(R;Q, a1, σ)≥0for allR∈(0,1), and Step 1’s strict inequality yields ˜N(R;Q, a2, σ)>
˜N(R;Q, a1, σ)≥0. The boundary values ˜N(0;Q, a, σ) =q b(qg +Q)and ˜N(1;Q, a, σ) =
qg(qb +Q)are independent ofaand strictly positive, so ˜N(·;Q, a 2, σ)≥0on[0,1], giving
Q∈ S(a2, σ). Thus ¯Q(a1, σ)≤ ¯Q(a2, σ). The strict-inequality argument from Step 3
carries over verbatim with˜Nin place ofN(using∂ ˜N/∂a >0instead of∂N/∂a <0, and
the relative closedness ofS(a1, σ)). From this, Step 4 follows.
6

Thus the permissible prevalence of controversial products is largest at the symmetric
benchmarka= 1andshrinksasthepopulationbecomesmorepolarizedineitherdirection.
7
