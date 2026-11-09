---
title: The Optimal Ranking Tradeoffs Between Two Ranking Scores in Two-Class Classification
url: https://arxiv.org/abs/2610.23294
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Sébastien Piérard
- Adrien Deliège
- Marc Van Droogenbroeck
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.23294
pages: 14
chars: 54465
fetched_at: '2026-11-08T13:30:29+00:00'
kb_version: 1
---

# The Optimal Ranking Tradeoffs Between Two Ranking Scores in Two-Class Classification

THEOPTIMALRANKINGTRADEOFFS
BETWEENTWORANKINGSCORES
INTWO-CLASSCLASSIFICATION
Sébastien Piérard, Adrien Deliège & Marc Van Droogenbroeck
Montefiore Institute, University of Liège, Liège, Belgium
{S.Pierard, Adrien.Deliege, M.VanDroogenbroeck}@uliege.be
ABSTRACT
The accuracy, true negative rate (negative class recall), true positive rate (positive
class recall), negative predictive value (negative class precision), positive predic-
tive value (positive class precision), class-specific intersections over unions, class-
specific F-scores, Cohen’s kappa, and balanced accuracy are scores that one intu-
itively wants to maximize when developing machine learning methods. However,
they lead to different rankings of such methods. So, how can we establish a rank-
ing that is an optimal tradeoff between any pair of these scores? It turns out that all
these scores are special cases of ranking scores: a continuum of scores parameter-
ized by the relative importance values assigned to the true negative, false positive,
false negative, and true positive outcomes. Since all these scores are known to
induce meaningful rankings, we seek the optimal tradeoffs among them. We con-
sider the tradeoff between two scores to be optimal when it minimizes the Fréchet
variance regarding the Kendall distance (also known as the bubble-sort distance)
between rankings. For any given set of classifiers to rank, the optimal tradeoff lies
at the center of the shortest (geodesic) path on the manifold of all rankings induced
by the ranking scores. However, in the parameter space of the ranking scores, it
is rarely achieved by averaging the importance values corresponding to the initial
scores. In this paper, we present an exact analytical solution for determining a
ranking score that is an optimal tradeoff for any given pair of initial scores, in the
common case where the class priors are the same for all compared performances.
We also experimentally investigate what happens when performance follows some
distributions with fixed priors.
1 INTRODUCTION
Benchmarks aim at sorting some compared methods from best (first rank) to worst (largest rank). A
common way to do this is to choose a score and consider that a method isworse than or equivalent
toanother one if and only if the value taken by the score for the first method isless than or equal to
the value taken for the second method. In other words, using a score is nothing more than a trick to
induce a preorder on the methods based on the well-known natural order on real numbers.
Obviously, not just any score or any preorder on performances can be used if the ranking is to be
meaningful. When the performances have a probabilistic meaning, the conditions that must be satis-
fied have been formalized in Piérard et al. (2025c) (which presentsgeneric axioms of performance-
based ranking) without assuming any particular task. Moreover, in the ubiquitous setting in which
the evaluation behaves linearly regarding the evaluated method (i.e., a hybrid method obtained by
blindly and non-deterministically combining some base methods has a performance that is a mixture
of the performances of the base methods), it has been shown that a wide family of scores leads to
meaningful rankings. These are calledranking scoresand defined as the ratio of the expected value
of the importance-satisfaction product to the expected value of the importance, thesatisfactionbeing
a random variable modeling the task and theimportancebeing another random variable specifying
the relative importance given to the various evaluation outcomes (Piérard et al., 2025c).
1
arXiv:2610.23294v1  [cs.PF]  16 Oct 2026

In other words, the ranking scoresRI form an infinite and continuous family of scores parameterized
by importance values. This offers great flexibility in freely choosing the relative weights that best
align with the preferences associated with the target application or its users. However, we argue
that choosing the score (i.e., the importance values in the case of ranking scores) remains a delicate
matter for a challenge organizer or a benchmarker (Halin et al., 2024), for example, who is unaware
of the applications that the people consulting the proposed ranking are targeting. Consequently,
further theoretical advances to guide this choice are still needed. This paper aims to contribute
to that effort for two-class classification, with a special focus on the particular case in which all
compared performances share the same class priors. This is a very common setting as good practice
suggests to compare only performances determined by evaluating the methods on the same dataset,
hence fixing the class priors.
In two-class classification, one usually considers a class asnegativeand the other one aspositive. It
should be stressed that this is just a convention. The choice of which class is positive is always arbi-
trary. Four evaluation outcomes are usually considered: true negative (tn), false positive (f p), false
negative (f n), and true positive (tp). All of us will certainly agree that the outcomestnandtpare
fully satisfying, and that the outcomesf pandf nare not satisfying at all. In this setting, the ranking
scores include well-known scores such as the accuracyA, the true negative rateT N R=Re− =Sp
(a.k.a.inverse recall and specificity), the true positive rateT P R=Re+ =Se(a.k.a.recall and sen-
sitivity), the negative predictive valueN P V=P r− (a.k.a.inverse precision), the positive predictive
valueP P V=P r+ (a.k.a.precision), as well as the F-scoresF β and the intersection over union
IoU(a.k.a.Jaccard coefficient) that can be defined for both classes. When the class priors are fixed,
the balanced accuracyBA, the skew-insensitive version ofF 1 SIV F(Flach, 2003), and the stan-
dardized predictive valuesSN P VandSP P V(Heston, 2011) also belong to the family of ranking
scores (the importance values are constants expressed in terms of the class priors). Moreover, Co-
hen’s kappaκ(Cohen, 1960) (a.k.a.Heidke Skill Score) is linearly increasing with a ranking score
(Piérard et al., 2024). All these classical scores are therefore associated with well-defined impor-
tance values. For any ranking score, its inverse (i.e., the function composition of the score with the
operation on performances that swaps the negative and positive classes (Powers, 2020)) is also a
ranking score (Piérard et al., 2024). For example, the true negative and positive rates are inverses of
each other, and the negative and positive predictive values are also inverses of each other.
The main objective of this paper is to provide all the theoretical and algorithmic tools to determine
optimal tradeoffs between two scores. This indeed includes the determination of the tradeoff be-
tween a class-specific score (e.g., the precision, recall, F-score, or intersection over union) and its
inverse. But this also includes the determination of the tradeoff between two scores for the same
class (e.g.between precision and recall).
There are mainly two reasons why one cannot just use any arbitrarily chosen mean (e.g., arithmetic,
geometric, harmonic, or quadratic) to establish a tradeoff between scores. First, the performance or-
dering induced by a mean of two base scores does not necessarily satisfy the axioms of performance-
based ranking, even if the orderings induced by these two base scores do. Second, even if this were
the case, the resulting ranking would not necessarily be intermediate between the rankings induced
by the two base scores. For example, it has been shown in Piérard et al. (2026) that even though
the F-scoreF 1 is the harmonic mean of the precision and recall and thatF 1 is known to lead to
meaningful rankings (it is a ranking score), the F-score sometimes mimics perfectly the precision
or recall in terms of rankings, totally ignoring the other. It is very likely that this problem is not
specific to the tradeoff between precision and recall. For this reason, it is far preferable to establish
an optimal tradeoff from the perspective of ranking. We aim at providing all the theoretical and
algorithmic tools to answer the following question.
Question.In two-class classification, for any given set of performances and for any pair of scores
perfectly rank-correlated with ranking scores (e.g.,A,T N R,T P R,N P V,P P V,F− β ,F + β ,IoU −,
IoU+,BA,SIV F,κ), what ranking scores are optimal tradeoffs from a ranking point of view?
To the best of our knowledge, only the very particular case of the optimal tradeoff between the
precision and recall of the positive class has been extensively studied. This was done in Piérard
et al. (2026). In this paper, we keep the same methodology and reasoning, generalizing it to any pair
of ranking scores. Let us summarize the methodology in four points.
2

(1) The search space.How one interprets a ranking depends on how one interprets the score that
induces it. For this reason, the use of rank aggregation methods, such as those developed by Ke-
meny (Kemeny, 1959), are inappropriate as they operate on the rankings only, ignoring their origins,
and lead to a ranking that is not related to any score. Instead, we explicitly determine the tradeoff
score that leads to the optimal tradeoff ranking. Moreover, as we want to be sure that the tradeoff
corresponds to one of the possible meaningful rankings, we seek for the optimal tradeoff within the
family of ranking scores. More information about the search space can be found in section 3.1.
(2) The means.The main challenge facing us is that the reasoning of Piérard et al. (2026) was
heavily based on the observation that there exists a weighted mean (the weighted harmonic mean)
such that, if applied to precision and recall, one obtains ranking scores. To be able to generalize it,
for any pair of ranking scores we need to find a weighted mean such that, if applied to them, one
also obtains a ranking score. This is done in section 3.2.
(3) The shortest paths.If there is a mean between the scoresR IA andR IB, then it is possible to
determine scoresR I such thatd τ(RIA ;R I)+d τ(RI ;R IB)=d τ(RIA ;R IB)whered τ = 1−τ 2 is Kendall distance (Kendall, 1938) (also known as the bubble-sort distance) between rankings. We
say that these scores form a shortest path betweenR IA andR IB. This is done in section 3.3.
(4) The optimal tradeoffs.The optimal tradeoff is the midpoint on the shortest path. It is given by
the ranking scoreR I such thatd τ(RIA ;R I)=d τ(RI ;R IB). It is a Karcher mean (Karcher, 1977)
as it minimizes the Fréchet variance regarding the Kendall distance between rankings:
RI∗ =arg min
RI
σ2(I)withσ 2(I)=d 2 τ(RIA ;R I)+d 2 τ(RI ;R IB).(1)
Establishing solutions for this equation is done in section 3.4.
Our theoretical contributions are threefold.
1. From the point of view ofvalues, we introduce scores that are homographic transformations
of ranking scores. We show that, when the class priors are fixed, for any pair of ranking
scores(R IA , RIB)there exist ranking scores that are weightedf-means of some ranking
scoresR ′ IA andR ′ IB monotonically increasing with respect toR IA andR IB, respectively, and that are generated by homographiesf. This stands in contrast to the unjustifiable
practice of considering only the arithmetic, geometric, and harmonic means.
2. From the point of view ofrankings, we provide the equation for a shortest path between
any pair of ranking scores(R IA , RIB), assuming the priors are fixed. Furthermore, we
present a method for determining the optimal tradeoff when the set of performances to be
ranked is known. This optimal tradeoff lies on the shortest path.
3. We show that, among all the ways to parameterize the two-dimensional manifold of per-
formance orderings induced by ranking scores, there is one that has properties particularly
interesting for finding optimal tradeoffs. We call thisthe parameterization adapted to the
priors. Its usefulness should not be viewed as limited to simplifying equations, since a
well-designed parameterization is key to obtaining ranking visualization tools that are well-
suited to specific needs. Readers curious to discover such a tool, calledthe Tile, are invited
to consult Piérard et al. (2024; 2025b) for the theory, Piérard et al. (2025d) for an open-
source implementation, and Halin et al. (2024); Piérard et al. (2025a); Bouwmans et al.
(2026); Zakharova et al. (2026) for some uses of it.
2 RELATEDWORK: THERISKYMEANS
We dedicate this section to the tradeoffs betweentwoscores that have been defined in the literature,
in the case of two-class classification. As this list shows, these tradeoffs are all established using
an arbitrarily chosen mean. The so-called “Pythagorean” means (i.e., the arithmetic meanµ A, the
geometric meanµ G, and the harmonic meanµ H) are systematically used, although there is no good
reason to limit ourselves to the means that were known and studied by the ancient Greeks, some two
and a half millennia ago. The base scores on which these tradeoffs are based are primarily the follow-
ing:T N R,T P R,N P V, andP P V. Hereafter, we list not only the means but also their monotonous
transformations as they induce the same ranking or its inverse. Scores related toµ A(T N R;T P R).
3

score classic formula Itn If p If n Itp a(π)(I)b (π)(I)
T N R=Re− P(Y= ˆY∣Y=c −) 1 1 0 0 0 0
T P R=Re+ P(Y= ˆY∣Y=c +) 0 0 1 1 1 1
N P V=P r− P(Y= ˆY∣ ˆY=c −) 1 0 1 0 0 1
P P V=P r+ P(Y= ˆY∣ ˆY=c +) 0 1 0 1 1 0
SN P V T N R T N R+F N R= N P V π+ N P V(π+−π− )+π− π+ 0π − 0 0 1
SP P V T P R F P R+T P R= P P V π− P P V(π−−π+ )+π+ 0π + 0π − 1 0
SIV F 2T P R T P R+F P R+1=µ H(SP P V;T P R) 0π + π− 2π− 1 1/2
F− β 1 F− β = 1 1+β2 1 P r− + β2 1+β2 1 Re− 1 β2 1+β2 1 1+β2 0 0 1 1+ℓ ,ℓ=β 2 π− π+
F+ β 1 F+ β = 1 1+β2 1 P r+ + β2 1+β2 1 Re+ 0 1 1+β2 β2 1+β2 1 1 ℓ 1+ℓ ,ℓ=β 2 π+ π−
IoU− P(Y= ˆY∣Y=c −∪ ˆY=c −) 1 1 1 0 0π +
IoU+ P(Y= ˆY∣Y=c +∪ ˆY=c +) 0 1 1 1 1π +
BA 1/2T N R+1/2T P R π+ π+ π− π− 1/2 1/2
A P(Y= ˆY)=E P[S] 1 1 1 1 π+ π+
Linear ofκ(π 2 −+π 2 +)κ+2π −π+ π2 + π2−+π2+ 1 2 1 2 π2 − π2−+π2+ π− π+
Table 1: Some ranking scores, when the class priors(π −, π+)are fixed, with corresponding impor-
tance values, and the coordinates of the induced performance ordering in the(a (π), b(π))space.
Many authors combineT N RandT P R. Their weighted arithmetic mean is the weighted accu-
racyW A. When the weights are0.5, we obtain the balanced accuracyBA(Brodersen et al.,
2010), and when the weights correspond to the priors, we get the accuracyA. Youden’s index
(Youden, 1950; Fluss et al., 2005) or Youden’sJ Y statistic isJ Y =2BA−1. It is also called
informedness (Powers, 2020) and Peirce Skill Score (Peirce, 1884). The determinant of the (nor-
malized) confusion matrix (Foulle, 2025) is∣C∣=π −π+JY . Scores related toµ G(T N R;T P R).
Instead of taking an arithmetic mean, it has been proposed to take the geometric mean (Kubat,
1997; Barandela et al., 2003; Guo et al., 2008), which leads to the G-measure (Canbek et al., 2017).
Scores related toµ H(P P V;T P R).This is the F-one score (van Rijsbergen, 1979; Christen et al.,
2023), also called Dice-Sørensen coefficient (Dice, 1945). It is well known that that Jaccard co-
efficient (Jaccard, 1908) leads to the same performance ordering asF 1, due to a strict increas-
ing monotonic relationship between the two scores.µ G(P P V;T P R)is Fowlkes-Mallows index
(Fowlkes & Mallows, 1983).µ A(P P V;T P R)is Kulczynski index (Kulczy ´nski, 1927). The In-
dividual Classification Success Index (ICSI) is a monotonous transformation of Kulczynski index.
Scores related toµ A(N P V;P P V).The markedness (Powers, 2020) is defined asN P V+P P V−1
and is also known as the Clayton Skill Score (Clayton, 1934; Canbek et al., 2017; Wilks, 2020).
3 THEORY
Probabilistic grounding and notations (following Piérard et al. (2025c)).Let us consider a
measurable space(Ω,Σ)with a sample space (a.k.a.universe) made of four evaluation outcomes
Ω={tn, f p, f n, tp}and the event spaceΣ=2Ω. By definition, performances are probability mea-
sures onΩ, and scores are real functions whose domains are subsets of all possible performances.
We denote byE P[⋅]the expected value of random variables for the performanceP. In order to es-
tablish a connection with two-class classification, we introduce a setC={c−, c+}that we interpret as
the set of classes,c− being called thenegative classandc + being called thepositive class. Moreover,
since it is common to refer to ground-truth and predicted classes, we introduce symbolic variables
for them. The ground-truth class isY∶Ω→CwithY(tn)=Y(f p)=c − andY(f n)=Y(tp)=c +.
The predicted class is ˆY∶Ω→Cwith ˆY(tn)= ˆY(f n)=c − and ˆY(f p)= ˆY(tp)=c +. The sym-
bolstn,f p,f n, andtpcan thus be interpreted, respectively, as atrue negative,false positive,false
negative, andtrue positive. For a performanceP, the class priors are given byπ − =P(Y=c −)and
π+ =P(Y=c +). The classification task is modeled by a binary random variable calledsatisfaction
S∶Ω→R∶ω↦1 {tn,tp}(ω). In other wordsS=1if and only ifY= ˆYandS=0if and only
ifY≠ ˆY. We also introduce another random variable, positive but non-zero, calledimportance
I∶Ω→[0,∞[. To shorten the notations, we poseI ω =I(ω)andP ω =P({ω})for allω∈Ω.
4

𝑡𝑛
𝑓𝑝
𝑓𝑛
t𝑝
𝑡𝑛
𝑓𝑝
𝑓𝑛
t𝑝
𝑡𝑛
𝑓𝑝
𝑓𝑛
t𝑝
𝐴
𝑇𝑁𝑅
𝑁𝑃𝑉
𝑇𝑃𝑅
𝑃𝑃𝑉
𝐹!
𝐼𝑜𝑈
We denote by (𝑎,𝑏) the
Cartesian coordinates in this
square. It is one possible
parameterization of the
performance orderings.
The scores in this square
are called “canonical
ranking scores”.
𝑎
1−
𝑎
𝐹! and 𝐼𝑜𝑈
induce the same
 performance ordering.
𝐹!  is canonical, but  𝐼𝑜𝑈 is not.
All scores along such a
line induce the same
performance ordering.
𝑏
1−𝑏
𝑡𝑛
𝑓𝑝
𝑓𝑛
t𝑝
𝑎
1−
𝑎
𝑏
1−𝑏0.5
0.5
0.5
0.5
𝜋"
𝜋#
𝜋# 𝜋"
The parameterization
(𝑎$,𝑏$), adapted to
the class priors, is a
homography of this
cutting plane.
𝑇𝑁𝑅
𝑇𝑃𝑅
𝑆𝑃𝑃𝑉 𝑆𝑁𝑃𝑉
𝐴
𝐵𝐴
𝑆𝐼𝑉𝐹
Figure 1: The tetrahedron of ranking scores, or the simplex of importance values in two-class clas-
sification. Be careful not to confuse this with the tetrahedron of performances or confusion sim-
plex (Chicco et al., 2021; Chicco & Jurman, 2023; Lovell et al., 2023; Brzezinski et al., 2017; 2020;
2018). In this one, each point corresponds to a score, not a performance.
3.1 THEPERFORMANCEORDERINGSINDUCED BYRANKINGSCORES
A space of scores.To ensure meaningful ranking tradeoffs, we seek for optimal tradeoffs within
the family of ranking scores. These scores are generic, but we are only interested in their particular-
ization to two-class classification. They have been defined in Piérard et al. (2025c) as
RI(P)= EP[SI] EP[I] = Itn Ptn+I tp Ptp Itn Ptn+I f pPf p+I f nPf n+I tp Ptp .(2)
A few examples of ranking scores or of scores strictly increasing with them (i.e., perfectly rank-
correlated with them) are given in table 1. The ranking scores are insensitive to the scaling of
the importanceI, so we can limit ourselves to considering thatI tn+I f p+I f n+I tp =1. As the
importance values must be positive, the ranking scores form a three-dimensional simplex (see fig. 1).
In the tetrahedron(I tn, If p, If n, Itp), all scores on the line between(1−a,0,0, a)and(0,1−b, b,0)
induce the same performance ordering. We call themiso-ranking lines.
A space of performance orderings.The performance orderings can be parameterized in different
ways. A quite intuitive choice is with the pair(a, b)∈[0,1] 2. These are Cartesian coordinates in
the squareI tn +I tp =I f p+I f ncutting the tetrahedron in the middle and intersecting each iso-
ranking line in one point. But we discovered that there is a much more interesting cutting plane to
consider for our purpose:I tn π−+I tp π+ =I f pπ−+I f nπ+. Its advantages will become clear in
the next subsections. This plane form a convex kite that can be mapped to the square[0,1] 2 with a
homography (thus a collineation; this will be important for us a little bit further)(a (π), b(π)):
a(π)(I)= Itp π+
Itn π−+I tp π+
∈[0,1]b (π)(I)= If nπ+
If pπ−+I f nπ+
∈[0,1].(3)
Note thata (π) andb (π) are strictly increasing withaandb, respectively.
3.2 MEANS OFRANKINGSCORES
Let us remind that for real numbers (the co-domain of scores), a large class of means is known as
the generalizedf-means, quasi-arithmetic means, or Kolmogorov-Nagumo-de Finetti means (Kol-
mogorov, 1930). The generalizedf-mean X, on an interval[l, u], betweenX1 andX 2 is defined as
f( X)= 1 2 f(X 1)+ 1 2 f(X 2), wherefis monotonic over[l, u]. These means include the arithmetic, geometric, harmonic, and quadratic means, to cite only a few examples. In the case of a binary
satisfaction, in which we are, it has been shown in Piérard et al. (2025c) that, for the generators
f∶x↦x −1 andf∶x↦(1−x) −1, some ranking scores are means of others. When the priors are
fixed, we discovered that the means to consider are more generally thef-means generated by some
5

homographiesf. 1 For this reason, we introduce the homographic transformations of ranking scores:
f○R I = A RI +B C RI +D = (A+B)I tn Ptn+B If pPf p+B If nPf n+(A+B)I tp Ptp (C+D)I tn Ptn+D If pPf p+D If nPf n+(C+D)I tp Ptp ,(4)
withAD>BC. This constraint on the transformation parameters ensures that the transformation is
strictly increasing and therefore that the scoref○R I induces the same performance ordering asR I.
From now, we leave aside the unnecessary constraint ∑ω I(ω)=1. To ensureI tn π− +I tp π+ =
If pπ−+I f nπ+, for the performance ordering(a (π), b(π)), we consider only
Itn =π +(1−a (π))I f p=π +(1−b (π))I f n=π − b(π) Itp =π − a(π) .(5)
We now take a look at the conditions on(A, B, C, D)to obtain a scoreRI with thef-mean of some
given scoresR IA andR IB. The equationf○R I = 1/2f○R IA+ 1/2f○R IB has solutions whenIis the
arithmetic mean ofI A andI B and the denominator of eq. (4) is the same forf○R IA andf○R IB, for
any given performance. Thus,(C+D)∆ tn Ptn+D∆ f pPf p+D∆ f nPf n+(C+D)∆ tp Ptp =0,
with∆ ω =I A(ω)−I B(ω)∀ω∈Ω. AsP tn+P f pandP f n+P tp are constant when the priors are
fixed, the coefficients in front ofP tn andP f pshould be equal, as well as those ofP f nandP tp:
(C+D)∆ tn =D∆ f p D∆ f n=(C+D)∆ tp (6)
Let us pose∆ a(π) =a (π)(IB)−a (π)(IA)and∆ b(π) =b (π)(IB)−b (π)(IA). We have∆ tn =
−π+ ∆a(π),∆ f p=−π + ∆b(π),∆ f n=π − ∆b(π), and∆ tp =π − ∆a(π). So, the two constraints given
in eq. (6) are equivalent to(C+D)∆ a(π) =D∆ b(π). We choose the solution
A=∆ a(π) B=∆ a(π) −∆ b(π) C=∆ b(π) −∆ a(π) D=∆ a(π) .(7)
This homographyfis an involution (i.e.,f −1 =f). Its polez=− D/Ccan be in the[0,1]range (i.e.,
the image of ranking scores). So,fis monotonously increasing on]−∞, z[and on]z,∞[, but not
on[0,1]. However, this is not a problem for us because it can be shown that
RIA(P)<z⇔R IB(P)<z R IA(P)=z⇔R IB(P)=z R IA(P)>z⇔R IB(P)>z .(8)
3.3 UNIVERSALSHORTESTPATHSBETWEENRANKINGS
We have just seen that, when the class priors are fixed, for any pair of ranking scores(R IA , RIB)
there exist ranking scoresR I that are weighted means of some ranking scoresR ′ IA andR ′ IB mono- tonically increasing with respect toRIA andR IB, respectively. The reasoning of Piérard et al. (2026)
can be applied as is: it follows immediately thatd τ(RIA ;R I)+d τ(RI ;R IB)=d τ(RIA ;R IB)for
all these meansR I. This shortest path is obtained with a weighted linear interpolation of impor-
tance values when they satisfy eq. (5). However, takingI= 1 2 IA+ 1 2 IB does not necessarily lead to optimal tradeoff (this will be the topic of the next subsection). It is interesting to note that the
passage from the plane of eq. (5) to the cutting plane shown on the right hand side tetrahedron of
fig. 1 is a homography. As the mapping from this cutting plane to the space(a (π), b(π))is also
a homography, it follows that the shortest paths are line segments in(a (π), b(π)). Aside from the
ease of graphical representation this provides (see section 5), it also sheds light on the manifolds of
performance orderings induced by the ranking scores when the class priors are fixed. According to
Beltrami’s theorem (Beltrami, 1868), this implies that these manifolds have a constant curvature.
3.4 OPTIMALTRADEOFFSBETWEENTWORANKINGSCORES
Again, the reasoning that was proposed in Piérard et al. (2026) to determine the optimal tradeoff
betweenP randRecan be easily generalized to the determine the optimal tradeoff between any
pair of ranking scores thanks to the fact that we found means. If there is a scoreR I such that
dτ(RIA ;R I)=d τ(RI ;R IB), then it is a solution to eq. (1).
Let us consider any scoreXthat is a weightedf-mean of some scoresX 1 andX 2, that isf○X=
(1−w)f○X 1+w f○X 2 withw∈[0,1]. The performancesP i andP j are put on an equal footing
1If two weighted means are equal, their generators are related by homographies (Grünwald & Páles, 2019).
Also, the composition of two homographies is also a homography. That is why we consider all homographies.
6

byXwhen
X(P i)=X(P j)⇔ w w−1 = (f○X 1)(Pi)−(f○X 1)(Pj) (f○X 2)(Pi)−(f○X 2)(Pj) =ψ(P i;P j).(9)
The weightwdepends on the pair of performances(P i;P j). We havew(P i;P j)= ψ(Pi;Pj ) ψ(Pi;Pj )−1. If
bothX 1 andX 2 agree on the order betweenP i andP j, thenw(P i;P j) /∈[0,1].
The optimal tradeoffs betweenX 1 andX 2, from a ranking perspective, are the scores on the shortest
path such that there is the same amount of swaps on both sides. Denoting multisets by{⋅}, a weight
leading to an optimal tradeoff is given by
w∗ =median({w(P i, Pj)∣i≠j∧w(P i, Pj)∈[0,1]}∪{0,1}).(10)
4 ALGORITHM
We present now an algorithm in nine steps to determine a ranking score that is one of the optimal
tradeoffs between two base scores, namelyXA andX B, perfectly rank-correlated with some ranking
scores, for a finite set of performancesΠsharing the same class priors.
Step 1.Determine the priors(π −, π+)such thatP(Y=c −)=π − andP(Y=c +)=π +,∀P∈Π.
Step 2.Determine some importance valuesI A andI B that correspond to the base scores. To do this,
one can, for example, consult table 1. This gives us the scoresR IA andR IB, which are perfectly
rank-correlated withX A andX B for the class priors(π −, π+).
Step 3.Move the importance points along their iso-ranking line to place them on the planeI tn π−+
Itp π+ =I f pπ− +I f nπ+ (see fig. 1, right). For an importanceI(whetherI A orI B), calculate
a(π)(I)andb (π)(I)using eq. (3), then apply eq. (5) to obtainI ′. So we replaceR IA andR IB
respectively byR I′ A andR I′ B without changing the rankings. The optimal tradeoff betweenX A and XB is therefore the same as that betweenR I′ A andR I′ B .
Step 4.Consider the universal shortest path betweenR I′ A andR I′ B , which is obtained by linearly
interpolating the importances:I=(1−w)I ′ A+w I′ B withw∈[0,1]. In the planeI tn π−+I tp π+ =
If pπ−+I f nπ+, this is a line segment. In the(a (π), b(π))space, this is also a line segment.
Step 5.Determine the mean generatorf. Any scoreR I on the shortest path is af-mean ofR I′ A
andR I′ B generated by an homographic functionf∶[0,1]→R∶x↦ Ax+B Cx+D , whose coefficients are
given by eq. (7) and depend only on∆a(π) =a (π)(I′ B)−a (π)(I′ A)and∆ b(π) =b (π)(I′ B)−b (π)(I′ A).
We haveR I =f −1[(1−w)f○R I′ A +w f○R I′ B ].
Step 6.For each performanceP∈Π, precompute(f○R I′ A )(P)and(f○R I′ B )(P). These values will be used when eq. (9) will be applied in the next step.
Step 7.Determine all the values ofwsuch that the universal shortest path crosses a boundary
between neighboring rankings. To do this, apply eq. (9) for each pairPi, Pj ∈Π. Indeed, forn=∣Π∣
performances, this step requiresO(n 2)uses of eq. (9) (this the same time complexity as one has
with a naive implementation of Kendall’sτ). In practice, however, this is not a big deal: even for
n=1000(hardly met in practice), this takes less than a second on a modern laptop.
Step 8.On the universal shortest path, choose a scoreR I∗ that is equidistant from the two start-
ing scores. To do this, determinew ∗ using eq. (10). Note thatd τ(RI∗ ;R I′ A )=d τ(RI∗ ;R IA)=
dτ(RI∗ ;X A)andd τ(RI∗ ;R I′ B )=d τ(RI∗ ;R IB)=d τ(RI∗ ;X B). So, one hasd τ(RI∗ ;R I′ A )=
dτ(RI∗ ;R I′ B )iifd τ(RI∗ ;X A)=d τ(RI∗ ;X B). When this equality is achieved,R I∗ is a solution to eq. (1). It minimizes Fréchet variance and is thus a Karcher mean betweenX A andX B,w.r.t.d τ .
Step 9.Determine the parameters of the scoreR I∗ that lies at this midpoint. This is an optimal
tradeoff given byI ∗ =(1−w ∗)I′ A +w ∗ I′ B. Any score that increases strictly withR I∗ is also
suitable. In particular, any ranking scoreR I such thata (π)(I)=a (π)(I∗)andb (π)(I)=b (π)(I∗)
or, equivalently,a(I)=a(I ∗)andb(I)=b(I ∗)is an optimal tradeoff betweenX A andX B.
7

A
 G
 H
 ours
PPV  TPR
NPV  TNR
NPV  PPV
TNR  TPR
IoU   IoU +
PPV  TNR
NPV  TPR
0.614 0.831 0.519 1.000
0.538 0.513 0.507 1.000
0.994 0.528 0.500 1.000
0.994 0.998 0.998 1.000
0.535 0.915 0.543 1.000
0.536 0.915 0.543 1.000
0.594 0.545 0.529 1.000
(a) WithΠ A.
A
 G
 H
 ours
PPV  TPR
NPV  TNR
NPV  PPV
TNR  TPR
IoU   IoU +
PPV  TNR
NPV  TPR
0.610 0.851 0.528 1.000
0.509 0.507 0.505 1.000
0.680 0.504 0.500 1.000
0.983 0.981 0.980 1.000
0.592 0.921 0.541 1.000
0.596 0.916 0.539 1.000
0.513 0.510 0.508 1.000 (b) WithΠ B.
A
 G
 H
 ours
PPV  TPR
NPV  TNR
NPV  PPV
TNR  TPR
IoU   IoU +
PPV  TNR
NPV  TPR
0.938 0.900 0.875 1.000
0.991 0.992 0.991 1.000
0.511 0.506 0.503 1.000
0.507 0.503 0.502 1.000
0.518 0.505 0.502 1.000
0.511 0.505 0.502 1.000
0.514 0.507 0.501 0.999 (c) WithΠ C.
Figure 2: OptimalityOobtained with each of the three Pythagorean means (µ A: arithmetic,µ G:
geometric,µ H: harmonic) and with our method, for seven pairs of scores and three sets of1000
performances corresponding toπ + =0.01. Our method always yields an optimal result (O=1, in
blue), but arbitrarily chosen means are only approximately optimal in a few specific cases. In fact,
the optimality value is often barely above 0.5 (the worst, in red). The meaningful rankings (i.e., the
tradeoffs satisfying the axioms of performance-based ranking (Piérard et al., 2025c)) are in bold.
5 EXPERIMENTS
5.1 ARBITRARILY CHOSEN MEANS:A RECIPE FOR TROUBLE
The purpose of our 1 st experiment is to highlight the problems that arise when a tradeoff is made
between two scores(R IA , RIB)using an arbitrarily chosen meanµ. We illustrate this using three
common means (the arithmetic, the geometric, and the harmonic) for seven tradeoffs (three of them
are tradeoffs between a score and its inverse), based on three large sets of performances. These
sets consist of performances drawn at random,i.i.d., following three performance distributions that
have been studied theoretically in Piérard et al. (2026) in the specific case of theP r-Retradeoff.
In the case of the setΠ A, the distribution is uniform for fixed priors; this corresponds to a uniform
distribution inROC=(F P R, T P R)∈[0,1]2. ForΠ B, the distribution remains uniform with fixed
priors but is restricted to performances above the no-skills (i.e.,T P R≥F P R). Finally, forΠC, we
restrict even further and consider a uniform distribution over(F P R, T P R)∈[0, π+]×[π +,1].
For each pair of scores for which a compromise must be determined, we calculate the values taken
by these two scores as well as their means, across all performances. Then, we calculate three Kendall
correlations: between the two base scores, between the first score and the mean, and between the
mean and the second score. From these values, we derive the optimality. It is defined in Piérard
et al. (2026) and can be generalized as:O(X)=1− ∣dτ (RIA ;X)−d τ (X;R IB )∣/2dτ (RIA ;RIB ), whereX
is the proposed tradeoff. For a meanµ,X=µ(R IA ;R IB). On any shortest path, the optimality
increases linearly with Kendall’s distance from both base scores (where it takes the minimal value
O= 1/2) towards the optimal tradeoff (where it takes the maximal valueO=1). The optimality can
be interpreted as the proportion of pairs of performances for whichXand the optimal tradeoff do
not agree, among those for which the ordering is not trivial (i.e.,RIA andR IB do not agree). Indeed,
the optimality can also be computed for any ranking score that our theory recommends.
The results of this first experiment are given in fig. 2. One can see that the ranking score recom-
mended by our theory has an optimality of1, as expected, no matter the set of performances and the
pair of scores that are considered. This is never the case with arbitrarily chosen means. With a prior
π+ =0.01, the optimality is often close to0.5(the worst scenario) with arbitrarily chosen means.
In this figure, we have written in bold the values for the cases in which the tradeoff score satisfies
the axioms of performance-based ranking. It is always the case with the tradeoffs we recommend
as they are ranking scores. However, it is rarely the case with the classic means (for the readers
interested to dive deeper into this topic, this is because the third axiom is not satisfied).
8

0.00 0.25 0.50 0.75 1.00
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
TNR
TPRNPV
PPV
IoU +IoU
 A
BA
(a)Π A: uniform
0.00 0.25 0.50 0.75 1.00
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
TNR
TPRNPV
PPV
IoU +IoU
 A
BA
 (b)Π B: uniform, above no-skills
0.00 0.25 0.50 0.75 1.00
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
TNR
TPRNPV
PPV
IoU +IoU
 A
BA
 (c)Π C: uniform , close to oracle
Figure 3: Case studies with large performances sets randomly drawn from reference distributions
with fixed priors (π+ =0.2). The colored markers indicate, in the(a (π), b(π))space, the performance
orderings that are optimal tradeoffs for the pairsP P V⋅T P R(▸),N P V⋅T N R(◂),N P V⋅P P V(∎),
T N R⋅T P R(◆),IoU−⋅IoU + (✖),P P V⋅T N R(▼), andN P V⋅T P R(▲).
5.2 CASE STUDIES:WITH REFERENCE DISTRIBUTIONS
The goal of our 2 nd experiment is to illustrate, within the(a (π), b(π))space, where the optimal
tradeoffs lie for the seven pairs of base scores and for the three distributions of performances of the
previous experiment. For each, we draw1000performances to have large sets. Considering refer-
ence distributions is interesting because the organizer of a challenge is often required to announce
the score that will be used to rank participants before receiving their actual performance results. For
the organizer, one option is to choose a reference distribution and use it to select a score.
In fig. 3, the rankings induced by the base scores,A,BA, andκare shown with labeled black dots.
Their locations can depend on the priors, but never on the set of performances. In the(a (π), b(π))
space, the shortest path is the line segment connecting the base scores. The position of the optimal
tradeoff on it depends on the set of performances. Along the seven studied segments, we draw gradu-
ated rulers such that the (not uniform) spacing between the marks is proportional todτ . The optimal
tradeoff (colored point) is thus at the median mark. The marks on the rulers allow to visualize how
the optimal tradeoff would move if one weighted non-uniformly the two base scores inσ 2(I)(see
eq. (1)). In this case, one needs to replace the median by a quantile in eq. (10).
We can see that the optimal tradeoff between precision (P P V) and recall (T P R) is notF1 (same
ranking asIoU +), but always corresponds to one of theF β scores (a(π) =1line). This confirms
the results of Piérard et al. (2026). We also see that the behavior is, broadly speaking, quite similar
betweenΠ A andΠ B, but quite different withΠ C, particularly for the optimal tradeoff between
T N RandT P R(close to the balanced accuracyBAfor the first two sets; close to the accuracyA
for the third) and for the optimal tradeoff betweenN P VandP P V(close to the balanced accuracy
BAfor the first two datasets; in the lower right quadrant of Cohen’sκfor the third). There is
generally no universal optimal tradeoff for a given pair of scores.
5.3 CASE STUDIES:WITH REAL-WORLD RANKINGS
The goal of our 3 rd experiment is to show what happens with real-world performance sets whose
size is significantly smaller than those we studied in the previous experiment. We considered four
published or publicly available performance sets related to computer vision problems. The results
are shown in fig. 4. There, we have plotted in the(a (π), b(π))space the frontiers between rank-
ings. They correspond to the scores for which any two performances are considered equivalent. It
turns out that, in the case of our parameterization adapted to the priors,R I(Pi)=R I(Pj)holds
if and only if the performance orderings lie on the lineζ a a(π)(I)+ζ b b(π)(I)+ζ=0withζ a =
F P R(Pi)F N R(Pj)−F P R(Pj)F N R(Pi),ζ b =T P R(Pi)T N R(Pj)−T P R(Pj)T N R(Pi),
andζ=T N R(P i)F P R(Pj)−T N R(Pj)F P R(Pi). On any given shorter path, the number of
times the path crosses one of these lines on either side of the optimal tradeoffs is equal.
9

0.0 0.2 0.4 0.6 0.8 1.0
FPR(P)
0.0
0.2
0.4
0.6
0.8
1.0TPR(P)
ROC space for + = 0.5
no-skill: P(Y, Y) = P(Y)P(Y)
unbiased: P(Y) = P(Y)
10 performances P
0.0 0.2 0.4 0.6 0.8 1.0
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
 PPV  PPV
NPV  NPV
NPV  NPV
TNR  TNR
IoU   IoU
PPV  PPV
NPV  NPV
Tile for + = 0.5
(a) With the10performances reported in Bouwmans
et al. (2026) for theIllegal Waste Dumping Detection
challenge, when the evaluation is done on the LS.
0.0 0.2 0.4 0.6 0.8 1.0
FPR(P)
0.0
0.2
0.4
0.6
0.8
1.0TPR(P)
ROC space for + = 0.5
no-skill: P(Y, Y) = P(Y)P(Y)
unbiased: P(Y) = P(Y)
10 performances P
0.0 0.2 0.4 0.6 0.8 1.0
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
PPV  PPV
NPV  NPV
NPV  NPV
TNR  TNR
IoU   IoU
PPV  PPV
NPV  NPV
Tile for + = 0.5
(b) With the10performances reported in Bouwmans
et al. (2026) for theIllegal Waste Dumping Detection
challenge, when the evaluation is done on the TS.
0.0 0.2 0.4 0.6 0.8 1.0
FPR(P)
0.0
0.2
0.4
0.6
0.8
1.0TPR(P)
ROC space for + = 0.124227
no-skill: P(Y, Y) = P(Y)P(Y)
unbiased: P(Y) = P(Y)
74 performances P
0.0 0.2 0.4 0.6 0.8 1.0
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
PPV  PPV
NPV  NPV
 NPV  NPV
TNR  TNR
 IoU   IoU
PPV  PPV
NPV  NPV
Tile for + = 0.124227
(c) With the performances given in Halin et al. (2024)
for74semantic segmentation models fromMMSeg-
mentation(MMSegmentation Contributors, 2020).
0.0 0.2 0.4 0.6 0.8 1.0
FPR(P)
0.0
0.2
0.4
0.6
0.8
1.0TPR(P)
ROC space for + = 0.0115291
no-skill: P(Y, Y) = P(Y)P(Y)
unbiased: P(Y) = P(Y)
57 performances P
0.0 0.2 0.4 0.6 0.8 1.0
a (I)
0.0
0.2
0.4
0.6
0.8
1.0b (I)
PPV  PPV
NPV  NPV
 NPV  NPV
TNR  TNR
 IoU   IoU
PPV  PPV
NPV  NPV
Tile for + = 0.0115291
(d) With the performances of57background subtrac-
tion methods reported on changedetection.net (CDnet
2014 (Wang et al., 2014)) for theblizzardvideo.
Figure 4: Case studies with 4 real-world performance sets. For each of them, the performances are
shown in the ROC space, and the optimal tradeoffs for 7 pairs of scores are shown in(a (π), b(π)).
The two first cases are based on the10performances reported in Bouwmans et al. (2026) regarding
the results of the Illegal Waste Dumping Detection (IWDD) challenge 2026. The authors reported
the performances measured on the learning set (LS) and on the test set (TS) to highlight the dis-
crepancy between the two (overfitting). Both LS and TS are balanced (π − =π +).We examine the
LS case in fig. 4a and the TS case in fig. 4b. In the latter case, all performances are close to the
no-skills (rising diagonal of ROC,i.e.Y⊥ ⊥P ˆY), and the optimal tradeoffs approach the descending
diagonal of(a (π), b(π))where the no-skill performances are put on an equal footing. In the extreme
case where all compared performances were no-skill, all the boundaries between the rankings would
coincide with the descending diagonal, and consequently, all optimal tradeoffs would lie on it.
The last two cases are for the performances reported by Halin et al. (2024) for74semantic seg-
mentation models fromMMSegmentation(MMSegmentation Contributors, 2020), evaluated on
BDD100K (Yu et al., 2020) after grouping the semantic labels into two classes, and the performances
of57background subtraction methods (classifying pixels as backgroundc − or foregroundc +; for
more information, see Bouwmans et al. (2019); Bouwmans & Garcia-Garcia (2019a;b)) measured
on the video “blizzard” (Goyette et al., 2012; Wang et al., 2014). They correspond, respectively, to
π+ ≃0.124andπ + ≃0.012. The comparison with fig. 3c shows that the optimal tradeoffs are close
to those predicted by the uniform distribution of performances, close to the oracle (ΠC).
6 CONCLUSION
Two-class classification is, conceptually, a simple task. However, the evaluation of the classifiers, as
well as the analysis and comparison of their performances, remains relatively poorly understood. We
have presented theoretical contributions that address the question: “Which scores correspond to the
optimal tradeoff between the rankings induced by two arbitrarily chosen scores?” We did so in the
specific but very common case of two-class classification with fixed priors, deliberately restricting
ourselves to the family of ranking scores known to yield meaningful rankings (i.e., rankings inter-
pretable from a performance perspective). We first presented the theory, then presented the results
of three experiments demonstrating the practical applicability of the proposed technique.
10

ACKNOWLEDGMENTS
S. Piérard is funded by grant 2010235 (ARIAC by DigitalWallonia4.ai) of the SPW EER, Wallonia,
Belgium; A. Deliège is a F.R.S.-FNRS postdoc researcher.
REFERENCES
Ricardo Barandela, Josep Salvador Sánchez, Vicente García, and Erick Rangel. Strategies for learn-
ing in class imbalance problems.Pattern Recognition, 36(3):849–851, March 2003. doi: 10.
1016/S0031-3203(02)00257-1. URLhttps://doi.org/10.1016/S0031-3203(02)
00257-1.
Eugenio Beltrami. Teoria fondamentale degli spazii di curvatura costante.Annali di Matematica
Pura ed Applicata, 2(1):232–255, August 1868. doi: 10.1007/bf02419615. URLhttps://
doi.org/10.1007/BF02419615.
Thierry Bouwmans and Belmar Garcia-Garcia. Visual surveillance of human activities: Background
subtraction challenges and methods. InFrom Visual Surveillance to Internet of Things: Tech-
nology and Applications, pp. 1–24. Taylor & Francis Group, October 2019a. doi: 10.1201/
9780429297922-4. URLhttps://doi.org/10.1201/9780429297922-4.
Thierry Bouwmans and Belmar Garcia-Garcia. Visual surveillance of natural environments:
Background subtraction challenges and methods. InFrom Visual Surveillance to Internet
of Things: Technology and Applications, pp. 1–20. Taylor & Francis, October 2019b. doi:
10.1201/9780429297922-5. URLhttps://doi.org/10.1201/9780429297922-5.
Thierry Bouwmans, Sajid Javed, Maryam Sultana, and Soon Ki Jung. Deep neural network concepts
for background subtraction: A systematic review and comparative evaluation.Neural Networks,
117:8–66, September 2019. doi: 10.1016/j.neunet.2019.04.024. URLhttps://doi.org/
10.1016/j.neunet.2019.04.024.
Thierry Bouwmans, Antonio Greco, Sébastien Piérard, Andrea Vincenzo Ricciardi, Carlo Sansone,
Marc Van Droogenbroeck, and Bruno Vento. Illegal waste dumping detection. InIEEE/CVF Win-
ter Conference on Applications of Computer Vision Workshops (WACVW), pp. 539–548, Tucson,
Arizona, USA, March 2026.
Kay Henning Brodersen, Cheng Soon Ong, Klaas Enno Stephan, and Joachim M. Buhmann. The
balanced accuracy and its posterior distribution. InIEEE International Conference on Pattern
Recognition (ICPR), pp. 3121–3124, Istanbul, Turkey, August 2010. Institute of Electrical and
Electronics Engineers (IEEE). doi: 10.1109/icpr.2010.764. URLhttps://doi.org/10.
1109/ICPR.2010.764.
Dariusz Brzezinski, Jerzy Stefanowski, Robert Susmaga, and Izabela Szcz˛ ech. Tetrahedron:
Barycentric measure visualizer. InMachine Learning and Knowledge Discovery in Databases,
volume 10536 ofLecture Notes in Computer Science, pp. 419–422. Springer International Pub-
lishing, 2017. doi: 10.1007/978-3-319-71273-4_43. URLhttps://doi.org/10.1007/
978-3-319-71273-4_43.
Dariusz Brzezinski, Jerzy Stefanowski, Robert Susmaga, and Izabela Szcz˛ ech. Visual-based anal-
ysis of classification measures and their properties for class imbalanced problems.Informa-
tion Sciences, 462:242–261, September 2018. doi: 10.1016/j.ins.2018.06.020. URLhttps:
//doi.org/10.1016/j.ins.2018.06.020.
Dariusz Brzezinski, Jerzy Stefanowski, Robert Susmaga, and Izabela Szcz˛ ech. On the dynamics of
classification measures for imbalanced and streaming data.IEEE Transactions on Neural Net-
works and Learning Systems, 31(8):2868–2878, August 2020. doi: 10.1109/tnnls.2019.2899061.
URLhttps://doi.org/10.1109/TNNLS.2019.2899061.
Gürol Canbek, Seref Sagiroglu, Tugba Taskaya Temizel, and Nazife Baykal. Binary classification
performance measures/metrics: A comprehensive visualized roadmap to gain new insights. In
International Conference on Computer Science and Engineering (UBMK), pp. 821–826, Antalya,
Turkey, October 2017. IEEE. doi: 10.1109/UBMK.2017.8093539. URLhttps://doi.org/
10.1109/UBMK.2017.8093539.
11

Davide Chicco and Giuseppe Jurman. The Matthews correlation coefficient (MCC) should replace
the ROC AUC as the standard metric for assessing binary classification.BioData Mining, 16(1),
February 2023. doi: 10.1186/s13040-023-00322-4. URLhttps://doi.org/10.1186/
s13040-023-00322-4.
Davide Chicco, Valery Starovoitov, and Giuseppe Jurman. The benefits of the Matthews correlation
coefficient (MCC) over the diagnostic odds ratio (DOR) in binary classification assessment.IEEE
Access, 9:47112–47124, 2021. doi: 10.1109/access.2021.3068614. URLhttps://doi.org/
10.1109/ACCESS.2021.3068614.
Peter Christen, David J. Hand, and Nishadi Kirielle. A review of the F-measure: Its history, prop-
erties, criticism, and alternatives.ACM Computing Surveys, 56(3):1–24, October 2023. doi:
10.1145/3606367. URLhttps://doi.org/10.1145/3606367.
H. Helm Clayton. Rating weather forecasts.Bulletin of the American Meteorological Society, 15
(12):279–283, December 1934. doi: 10.1175/1520-0477-15.12.279. URLhttps://doi.
org/10.1175/1520-0477-15.12.279.
Jacob Cohen. A coefficient of agreement for nominal scales.Educational and Psychological
Measurement, 20(1):37–46, April 1960. doi: 10.1177/001316446002000104. URLhttps:
//doi.org/10.1177/001316446002000104.
Lee R. Dice. Measures of the amount of ecologic association between species.Ecology, 26:297–
302, 1945. doi: 10.2307/1932409. URLhttps://doi.org/10.2307/1932409.
Peter A. Flach. The geometry of ROC space: Understanding machine learning metrics through
ROC isometrics. InInternational Conference on Machine Learning (ICML), pp. 194–201, Wash-
ington, District of Columbia, USA, August 2003. Association for the Advancement of Artificial
Intelligence (AAAI).
Ronen Fluss, David Faraggi, and Benjamin Reiser. Estimation of the Youden index and its associated
cutoff point.Biometrical Journal, 47(4):458–472, August 2005. doi: 10.1002/bimj.200410135.
URLhttps://doi.org/10.1002/bimj.200410135.
Sébastien Foulle. Mathematical characterization of better-than-random multiclass models.Trans-
actions on Machine Learning Research, pp. 1–17, June 2025. URLhttps://openreview.
net/forum?id=VdW9SkALSd.
Edward B. Fowlkes and Colin L. Mallows. A method for comparing two hierarchical clusterings.
Journal of the American Statistical Association, 78(383):553–569, September 1983. doi: 10.
1080/01621459.1983.10478008. URLhttps://doi.org/10.1080/01621459.1983.
10478008.
Nil Goyette, Pierre-Marc Jodoin, Fatih Porikli, Janusz Konrad, and Prakash Ishwar. Changedetec-
tion.net: A new change detection benchmark dataset. InIEEE International Conference on Com-
puter Vision and Pattern Recognition Workshops (CVPRW), pp. 1–8, Providence, Rhode Island,
USA, June 2012. IEEE. doi: 10.1109/CVPRW.2012.6238919. URLhttps://doi.org/10.
1109/CVPRW.2012.6238919.
Richárd Grünwald and Zsolt Páles. On the equality problem of generalized Bajraktarevi ´c means.
Aequationes Mathematicae, 94(4):651–677, August 2019. doi: 10.1007/s00010-019-00670-9.
URLhttps://doi.org/10.1007/s00010-019-00670-9.
Xinjian Guo, Yilong Yin, Cailing Dong, Gongping Yang, and Guangtong Zhou. On the class
imbalance problem. InInternational Conference on Natural Computation, pp. 192–201, Ji-
nan, China, October 2008. Institute of Electrical and Electronics Engineers (IEEE). doi:
10.1109/icnc.2008.871. URLhttps://doi.org/10.1109/ICNC.2008.871.
Anaïs Halin, Sébastien Piérard, Anthony Cioppa, and Marc Van Droogenbroeck. A hitchhiker’s
guide to understanding performances of two-class classifiers.arXiv, abs/2412.04377, 2024. doi:
10.48550/arXiv.2412.04377. URLhttps://doi.org/10.48550/arXiv.2412.04377.
12

Thomas F. Heston. Standardizing predictive values in diagnostic imaging research.Journal of
Magnetic Resonance Imaging, 33(2):505–505, January 2011. doi: 10.1002/jmri.22466. URL
https://doi.org/10.1002/jmri.22466.
Paul Jaccard. Nouvelles recherches sur la distribution florale.Bulletin de la Société Vaudoise des
Sciences Naturelles, 44(163):223–270, 1908.
Hermann Karcher. Riemannian center of mass and mollifier smoothing.Communications on Pure
and Applied Mathematics, 30(5):509–541, September 1977. doi: 10.1002/cpa.3160300502. URL
https://doi.org/10.1002/cpa.3160300502.
John G. Kemeny. Mathematics without numbers.Daedalus, 88(4):577–591, 1959. URLhttp:
//www.jstor.org/stable/20026529.
Maurice George Kendall. A new measure of rank correlation.Biometrika, 30(1/2):81, June 1938.
doi: 10.2307/2332226. URLhttps://doi.org/10.2307/2332226.
Andrey Nikolaevich Kolmogorov. Sur la notion de la moyenne.Atti della Academia Nazionale dei
Lincei, 12(9):388–391, 1930.
Miroslav Kubat. Addressing the curse of imbalanced training sets: one-sided selection. InInterna-
tional Conference on Machine Learning (ICML), pp. 179–186. Morgan Kaufmann, 1997.
Stanisław Kulczy´nski. Die pflanzenassoziationen der pieninen.Bulletin International de l’Académie
Polonaise des Sciences et des Lettres, Classe des Sciences Mathématiques et Naturelles, Série B:
Sciences Naturelles, II:57–203, 1927.
David Lovell, Dimity Miller, Jaiden Capra, and Andrew P. Bradley. Never mind the metrics –
what about the uncertainty? visualising binary confusion matrix metric distributions to put per-
formance in perspective. InInternational Conference on Machine Learning (ICML), volume
202 ofProceedings of Machine Learning Research, pp. 22702–22757, 2023. URLhttps:
//proceedings.mlr.press/v202/lovell23a.html.
MMSegmentation Contributors. MMSegmentation: OpenMMLab semantic segmentation toolbox
and benchmark.https://github.com/open-mmlab/mmsegmentation, 2020.
Charles S. Peirce. The numerical measure of the success of predictions.Science, 4(93):453–
454, November 1884. doi: 10.1126/science.ns-4.93.453.b. URLhttp://www.jstor.org/
stable/1760565.
Sébastien Piérard, Anaïs Halin, Anthony Cioppa, Adrien Deliège, and Marc Van Droogenbroeck.
The Tile: A 2D map of ranking scores for two-class classification.arXiv, abs/2412.04309,
2024. doi: 10.48550/arXiv.2412.04309. URLhttps://doi.org/10.48550/arXiv.
2412.04309.
Sébastien Piérard, Adrien Deliège, Anaïs Halin, and Marc Van Droogenbroeck. A methodology to
evaluate strategies predicting rankings on unseen domains. InIEEE International Conference on
Multimedia and Expo Workshops (ICMEW), Workshop on Big Surveillance Data Analysis and
Processing (BIG-Surv), pp. 1–6, Nantes, France, June 2025a. IEEE. doi: 10.1109/icmew68306.
2025.11152102. URLhttps://doi.org/10.1109/ICMEW68306.2025.11152102.
Sébastien Piérard, Adrien Deliège, and Marc Van Droogenbroeck. Multi-domain performance anal-
ysis with scores tailored to user preferences.arXiv, abs/2512.08715, 2025b. doi: 10.48550/arXiv.
2512.08715. URLhttps://doi.org/10.48550/arXiv.2512.08715.
Sébastien Piérard, Anaïs Halin, Anthony Cioppa, Adrien Deliège, and Marc Van Droogenbroeck.
Foundations of the theory of performance-based ranking. InIEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), pp. 14293–14302, Nashville, Tennessee, USA, June
2025c. IEEE. doi: 10.1109/cvpr52734.2025.01333. URLhttps://doi.org/10.1109/
CVPR52734.2025.01333.
13

Sébastien Piérard, Anaïs Halin, François Marelli, Simon Pernas, and Jérôme Pierre. Sorbetto: a
Python library for producing classification tiles with different flavors to visualize, analyze, and
compare performances in two-class classification problems.Zenodo, September 2025d. doi:
10.5281/zenodo.17591788. URLhttps://doi.org/10.5281/zenodo.17591788.
Sébastien Piérard, Adrien Deliège, and Marc Van Droogenbroeck. What is the optimal ranking score
between precision and recall? we can always find it and it is rarelyF 1. InIEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR), Denver, Colorado, USA, June 2026. IEEE.
David M. W. Powers. Evaluation: from precision, recall and F-measure to ROC, informedness,
markedness and correlation.arXiv, abs/2010.16061, 2020. doi: 10.48550/arXiv.2010.16061.
URLhttps://doi.org/10.48550/arXiv.2010.16061.
Cornelis Joost van Rijsbergen.Information Retrieval. Butterworths, London, England, second
edition, 1979.
Yi Wang, Pierre-Marc Jodoin, Fatih Porikli, Janusz Konrad, Yannick Benezeth, and Prakash Ishwar.
CDnet 2014: An expanded change detection benchmark dataset. InIEEE/CVF Conference on
Computer Vision and Pattern Recognition Workshops (CVPRW), pp. 393–400, Columbus, Ohio,
USA, June 2014. Institute of Electrical and Electronics Engineers (IEEE). doi: 10.1109/cvprw.
2014.126. URLhttps://doi.org/10.1109/CVPRW.2014.126.
Daniel S. Wilks.Statistical methods in the atmospheric sciences. Elsevier, fourth edition, 2020. doi:
10.1016/C2017-0-03921-6. URLhttp://dx.doi.org/10.1016/C2017-0-03921-6.
William John Youden. Index for rating diagnostic tests.Cancer, 3(1):32–35, January 1950. doi: 10.
1002/1097-0142(1950)3:1<32::aid-cncr2820030106>3.0.co;2-3. URLhttps://doi.org/
10.1002/1097-0142(1950)3:1<32::AID-CNCR2820030106>3.0.CO;2-3.
Fisher Yu, Haofeng Chen, Xin Wang, Wenqi Xian, Yingying Chen, Fangchen Liu, Vashisht Madha-
van, and Trevor Darrell. BDD100K: A diverse driving dataset for heterogeneous multitask learn-
ing. InIEEE International Conference on Computer Vision and Pattern Recognition (CVPR), pp.
2633–2642, Seattle, Washington, USA, June 2020. IEEE. doi: 10.1109/cvpr42600.2020.00271.
URLhttps://doi.org/10.1109/CVPR42600.2020.00271.
Anastasia Zakharova, Thierry Bouwmans, Anthony Cioppa, Adrien Deliège, Antonio Greco, Anaïs
Halin, Kamil Jeziorek, Meghna Kapoor, Tomasz Kryjak, Islam Osman, Sébastien Piérard, Carlo
Sansone, Mohamed S. Shehata, Renaud Vandeghen, Marc Van Droogenbroeck, and Bruno
Vento. Event detection in videos: A framework for the development of new methods.arXiv,
abs/2607.04372, 2026. doi: 10.48550/arXiv.2607.04372. URLhttps://doi.org/10.
48550/arXiv.2607.04372.
14
