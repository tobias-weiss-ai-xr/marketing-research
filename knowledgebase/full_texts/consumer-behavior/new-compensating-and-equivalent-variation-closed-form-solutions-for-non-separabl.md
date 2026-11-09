---
title: New Compensating and Equivalent Variation Closed-form Solutions for Non-Separable Public Goods
url: https://arxiv.org/abs/2401.15493
category: consumer-behavior
subcategory: empirical
date: 2024-01
venue: ''
authors:
- Daniel H. Karney
- Khyati Malik
source: arxiv
pdf_url: https://arxiv.org/pdf/2401.15493
pages: 50
chars: 81906
fetched_at: '2026-11-08T13:14:18+00:00'
kb_version: 1
---

# New Compensating and Equivalent Variation Closed-form Solutions for Non-Separable Public Goods

New Compensating and Equivalent Variation Closed-form Solutions for Non-
Separable Public Goods

Daniel H. Karney, Department of Economics, Ohio University

Khyati Malik, National Bureau of Economic Research (NBER)

January 2026

Abstract. This study finds exact closed-form solutions for compensating variation (CV)
and equivalent variation (EV) for both marginal and non-marginal changes in public
goods given homothetic, but non-separable, utility where a single sufficient statistic
summarizes consumer preferences. The closed-form CV and EV expressions identify
three economic mechanisms that determine magnitudes. One of these mechanisms, the
relative preference effect, helps explain the disparity between willingness to pay (WTP)
and willingness to accept (WTA) for public goods. We also show how our closed-form
solutions can be employed to calculate WTP and WTA across income groups using
estimates from existing empirical studies.
KEYWORDS: Public goods; Compensating variation; Equivalent variation; Willingness-
to-pay; Willingness-to-accept; Non-separable utility

Contacts: Daniel H. Karney: karney@ohio.edu; Khyati Malik: malikk@nber.org
We are grateful for comments from Marcel Arbex, Spencer Banzhaf, Peter Caradonna, Nathan Chan, Sathya
Gopalakrishnan, Anna Klis, Bethany Lemont, Vahe Lskavyan, James Price, and from participants at 2024
AERE@MEA and 2024 AERE Summer Conference. This manuscript was previously circulated under the title “Public
Good Provision and Compensating Variation”. All mistakes are our own.

 1
1 Introduction
Public goods provision by governments is a prominent feature of modern economies. In 2019, U.S.
local municipalities and states spent $425.7 billion on gross investments in fixed assets including
streets, highways, and water and sewer systems (U.S. BEA, 2022). The U.S. federal government
spends hundreds of billions of dollars on public goods like national defense (U.S. GAO, 2021) as
well as provides other public goods via policies that incur costs without direct expenditures such
as mandates to reduce pollution.1 Projected costs of climate change mitigation may be one of the
largest future public goods expenditure as worldwide total costs are expected to range from one to
seven percent of global GDP (Fujimori et al., 2023). How much are consumers willing to pay for
these public goods? Compensating variation (CV) and equivalent variation (EV) measure the value
of public good provision (Hanemann, 1991; Weber, 1992).
 This study contributes to the literature by finding closed-form solutions for CV and EV for
changes in public good provision. We also find a single sufficient statistic for the preference
parameters and show how to estimate this sufficient statistic in empirical applications. Previous
studies to uncover willingness to pay (WTP) and willingness to accept (WTA) of public goods
often impose separability to generate tractable results such as strongly or weakly separable utility
(Freeman et al., 2014). Here, we study a utility model with non-separable private and public goods
with homothetic preferences where public good provision may affect private consumption choices
on the margin. For instance, the provision of clean municipal water allows consumers to substitute
 1 Present government expenditures towards public goods may not change current public good provision. For example,
an under-construction municipal water system may entail significant upfront costs to the government but will not
contribute to an individual’s current-period direct utility in our model until it starts supplying clean water.

 2
away from private adaptation goods such as water filtration devices. Meanwhile, the building of
public highways complements private vehicle purchases. Hence, the private and public goods may
be complements or substitutes for each other in our model.
Other assumptions in the literature to enable tractability in the context of valuing public
goods include weak complementarity (Mäler, 1974), the Willig condition (Willig, 1978; Smith and
Banzhaf, 2004; Palmquist, 2005), and weak substitution (Feenberg and Mills, 1980). In general,
this study adds to the extensive theoretical (e.g., Larson, 1992; Neill, 1998) and empirical (e.g., Ito
and Zhang, 2020; Banzhaf, 2021) literature on willingness to pay for public goods and local
amenities. Our results also relate to the theory of non-traded goods (Neary and Roberts, 1980;
Bockstael and McConnell, 1993). Finally, this analysis extends the work on homogeneous utility
functions but without public goods (Espinosa and Prada, 2012).
We derive conditions for recovering closed-form expressions of compensating variation
and equivalent variation for utility functions with homothetic preferences for a change in public
good provision. The family of homothetic utility functions that we consider allow private and
public goods to be independently homogeneous in the underlying function without restrictions on
the monotonic transformation. We define “independently homogeneous” to mean that a function
is homogeneous in the private goods and separately in the public goods of (potentially) different
degrees.2
Homothetic utility functions are widely used in economic theory and applied applications,
and common forms include the constant elasticity of substitution (CES) and constant relative risk
aversion (CRRA) utility functions. As a result, homothetic utility functions are employed in
 2 In contrast, a “jointly homogeneous” function is homogeneous in both private and public goods simultaneously to
the same degree across both arguments.

 3
virtually all fields of economics including, but not limited to, consumer theory (Caselli and
Ventura, 2000), international trade (Kucheryavyy, 2012), and political economy (Collie, 2022). In
the context of environmental economics per our numerical application, homothetic functions have
been employed in numerical work (e.g., Pindyck, 2012), applied theory exercises (e.g., Fullerton
and Chi, 2019), as well as computational general equilibrium studies (e.g., Goulder and Hafstead,
2017).
The assumption of homotheticity with underlying independent homogeneity is crucial in
our approach because it leads to exact closed-form expressions for welfare measures—specifically,
compensating and equivalent variation—without resorting to consumer surplus approximations.
By exploiting these closed-form expressions, we can systematically link changes in public goods
provision to income in a way that remains analytically tractable. This is significant not just from a
theoretical standpoint; in practice, it allows researchers and policy analysts to directly compute
welfare measures, sidestepping the limitations that can arise from relying on approximate measures
of consumer surplus.
The single sufficient statistic in our CV and EV closed-form solutions is the ratio of the
degrees of homogeneity of the public and private goods from the independently homogeneous
function. This ratio is a sufficient statistic because it reduces the degree of complexity in our CV
and EV expressions from two parameters to one parameter (Reid, 2015), and the statistic indicates
the sign and relative size of CV and EV, all else equal (Chetty, 2009). Also, the sufficient statistic
can be estimated using either individual- or aggregate-level data of consumer expenditure (or
equivalently income), or private goods purchases given variation in public good provision. Our
utility function may also include an auxiliary set of public goods that are not subject to
homogeneity assumptions, and therefore not all public goods must have the same homothetic

 4
relationship to the private goods. Only a few studies explore willingness to pay for public goods
given homothetic utility (e.g., Quigley, 1982; Chattopadhyay, 1999) and ours is the first study to
derive these specific closed-form CV and EV expressions.
Our closed-form expressions allow us to cleanly identify economic mechanisms driving
CV and EV. We identify three different effects and relate them to WTP (the intuition is similar for
WTA). First, larger initial income leads to a larger WTP, all else equal, and this is the income
effect. Second, the absolute preference effect finds a positive correlation between the preference
parameter governing the impact of public good provision in utility and WTP. Third, the relative
preference effect leads to a larger WTP if the ratio of the degrees of homogeneity of the public
goods and the private goods is large. Conversely, the relative preference effect can result in a small
WTP if the ratio is small, and this relative effect is independent of the level of the public good
preference parameter. Thus, the relative preference effect demonstrates how WTP for public goods
can be small, regardless of income level and absolute effect of public goods in utility.
Our relative preference effect is related to the substitution effect discussed in Hanemann
(1991), but we show that the independent homogeneity assumption requires the private and public
goods to be imperfect substitutes. While Hanemann (1991)’s main objective is to show how
substitution could generate a large gap between WTP and WTA even in a traditional framework,
much of the experimental and survey literature has emphasized behavioral explanations, such as
loss aversion (Kahneman, Knetsch, and Thaler, 1990). We demonstrate that in a neoclassical
model with homothetic (non-separable) preferences without any behavioral biases, a gap can arise
via the relative preference effect. This effect is consistent with a substitution elasticity that drives
a wedge between WTP and WTA for public goods and helps clarify that WTP–WTA differences
need not rely solely on behavioral departures from the neoclassical assumptions. We prove that

 5
the relative preference effect partially drives the WTP-WTA gap for public goods in our model,
and this can help explain the Tunçel and Hammitt (2014) finding of a consistently larger gap
between WTP and WTA for public goods compared to private goods. Furthermore, our closed-
form CV and EV expressions are asymmetric, and this matches the asymmetry between WTP and
WTA found in the empirical literature (Horowitz and McConnell, 2002).
Also, while many WTP and WTA results hold for only marginal changes, our CV and EV
closed-form solutions hold for both marginal and non-marginal changes in public good provision.
Non-marginal changes in public good provision occur with large-scale public investments, such
as the construction of the U.S. interstate highways (Duranton and Turner, 2012) or implementation
of a paradigm-changing public policy, such as the Clean Air Act (Aldy et al., 2022). Therefore,
our study also contributes to the literature by providing an exact measure of WTP and WTA for
non-marginal public good provision changes. Again, our CV and EV expressions do not rely on
consumer surplus to approximate welfare as occurs with other WTP/WTA measures including
those employing the Willig condition.3 Slesnick (1998) discusses a general set of issues related to
using consumer surplus as an approximation for individual welfare in a variety of settings.
As an illustration of our results, we draw on existing studies—such as Ito and Zhang’s
(2020) analysis of air purifier markets in China to demonstrate that observed WTP for pollution
reductions can be readily translated into the sufficient statistic from our CV and EV closed-form
 3 With regards to the welfare effects of public goods and valuing public goods, Bockstael and McConnell (1993,
p.1254) note, “The Willig condition describes what must be true for the incremental consumer surplus to equal the
marginal value of quality measured from the expenditure function. When the Willig condition holds, the value of a
change in quality measured by a change in consumer surpluses for the associate good will be bounded by the equivalent
and compensating variation from a quality change.”

 6
expression. We then show how to use our closed-form expressions to easily calculate WTP (or
WTA) across income groups using standard empirical estimates.
This paper serves as a bridge between theory and empirical application by offering an
analytically precise method to calculate welfare metrics—such as compensating and equivalent
variation—for public goods under homothetic, non-separable preferences. In doing so, it departs
from purely theoretical modeling in two keyways. First, the closed-form CV and EV expressions
make it straightforward to connect the degree of homotheticity to observed WTP or WTA in
applied contexts. Second, because our expressions hold for non-marginal as well as small changes
in public goods, this framework is immediately usable by environmental economists, public
finance analysts, and others engaged in cost –benefit evaluations that often extend beyond
incremental changes. By eliminating the need for consumer-surplus approximations, our approach
offers a direct, exact mapping from measurable changes in public-goods provision to underlying
welfare gains or losses. This provides a practical tool for researchers and policymakers who require
valuations of large-scale public investments.
 The next section details the theoretical framework and accompanying assumptions. Section
3 provides our main results including CV and EV closed-form solutions via the expenditure
function. Next, Section 4 calculates values of the sufficient statistic from empirical WTP estimates
in the literature and then shows how to find WTP estimates for different income groups using the
derived sufficient statistic. Finally, Section 5 compares our results to the common assumption of
additively separable utility, and Section 6 concludes.

 7
2 Model
Given (potentially) many non-separable public goods, let the representative consumer's utility
maximization problem (UMP) be defined as max𝒙{ℎ(𝒙;𝒛,𝒘):𝒑∙𝒙	≤𝑚}, where 𝒙∈ℝ"# is a row
vector of private goods indexed 𝑛=1,…,𝑁 with associated prices 𝒑∈ℝ"" # and exogenous
income 𝑚>0. Let 𝒚=(𝒛,𝒘)∈ℝ"$ be a row vector of public goods indexed as 𝑘=1,…,𝐾 with
𝒛∈ℝ" $! and 𝒘∈ℝ" $" where 𝐾=𝐾%+𝐾&. The function ℎ(⋅) is a homothetic utility function
defined as ℎ(𝒙;𝒛,𝒘)≡𝑔D𝑢(𝒙;𝒛,𝒘)F where 𝑔(⋅) is a monotonic transformation and 𝑢(⋅) is the
so-called “underlying” function that is either jointly or independently homogeneous in 𝒙 and 𝒛.
Assume 𝑢(⋅) is strictly increasing, continuous, and quasiconcave.
Private goods are purchased via marginal pricing. Public goods such as clean municipal
water or a highway network, provide utility to the consumer but are not purchased.4 The level of
public good provision is exogenous from the consumer’s perspective so 𝒚 is not included in the
consumer’s budget constraint. For notational purposes, 𝒚 is offset by a semicolon in the relevant
functions to denote exogeneity. A change in the level of public good provision may occur through
quantity change and/or quality change but what matters to the consumer is the flow of utility-
generating public goods. That is, the public goods vector represents the flow of value in utility and
not the physical stock of public good infrastructure.
 4 The goods in vector 𝒚=(𝒛	𝒘) do not necessarily need to be non-rival and non-excludable and could be rival or
excludable, but goods provided freely to consumers by governments are understood to be public goods in many cases.
Public good provision may be voluntarily provided such as vaccine uptake, but our model does not allow for impure
public goods whereby purchasing 𝒙 affects public good provision 𝒚 (Chan and Kotchen, 2014; Chan, 2024). Also, the
model does not allow the representative consumer to select the level or composition of public good provision via
Tiebout (1956) sorting.

 8
 The model does not require optimal public good provision because the consumer optimizes
utility and private consumption regardless of the level of public goods provided. The UMP leads
to Marshallian demand 𝒙(𝑚,𝒑;𝒛,𝒘) and the subsequent indirect utility function 𝑣(𝑚,𝒑;𝒛,𝒘).
The dual expenditure minimization problem (EMP), formally given by min𝒙{𝒑⋅𝒙:ℎ(𝒙;𝒛,𝒘)≥
𝑢}, yields Hicksian demand, 𝒙𝒉(𝑢,𝒑;𝒛,𝒘), and the expenditure function, 𝑒(𝑢,𝒑;𝒛,𝒘), where 𝑢
is a scalar, fixed utility level.
We define three general characteristics of the utility function. First, the utility function is
strictly increasing in the public and private goods. Second, the utility function is continuous and
quasi-concave. Third, the utility function is homothetic and the underlying function, 𝑢(⋅), is
homogeneous. For the special case of homogeneous utility, one would employ 𝑢(𝒙;𝒛,𝒘) directly
as the utility function in the consumer's optimization problem. However, our main results for CV
and EV employ a homothetic utility function given by ℎ(𝒙;𝒛,𝒘)≡𝑔D𝑢(𝒙;𝒛,𝒘)F so that the CV
and EV results only use the ordinal properties of the underlying 𝑢(⋅) function.
For our main results, we define 𝑢(⋅) to be “independently homogeneous”, or exhibits
“independent homogeneity”, across the vectors 𝒙 and 𝒛 where the function is homogeneous of
degree 𝜂∈ℝ in 𝒙 and homogeneous of degree 𝜃∈ℝ in 𝒛; that is, 𝑡(𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝒛,𝒘) for
all 𝑡>0 and 𝑡)𝑢(𝒙;𝒛,𝒘)=𝑢(𝒙;𝑡𝒛,𝒘) for all 𝑡>0. It follows that 𝑡(")𝑢(𝒙;𝒛,𝒘)=
𝑢(𝑡𝒙;𝑡𝒛,𝒘) such that an independently homogeneous function is also “jointly homogeneous” of
degree 𝜂+𝜃. The standard homogeneity and homotheticity results then apply in the cone (𝒙	𝒛)∈
ℝ" #"$! as well as the cones defined by the clauses of the independent homogeneity assumption
(Simon and Blume, 1994). As a result, there always exists an interior solution with positive prices
for the private goods since the income expansion rays are linear from the origin.

 9
In contrast, one could define 𝑢(⋅) to be a jointly homogeneous function of degree 𝛾 in 𝒙
and 𝒛; that is, 𝑡*𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝑡𝒛,𝒘) for all 𝑡>0 where 𝛾∈ℝ denotes the degree of
homogeneity. In such cases, we would say the function exhibits “joint homogeneity”, since it is
homogeneous in the private goods and the public goods to the same degree and each argument
must be scaled by the same 𝑡>0.
The second public goods vector (𝒘) need not be included in any of the homogeneity
conditions and thus represents an auxiliary public goods vector. We include this auxiliary vector
in our model to highlight that not all public goods need to be subject to a homogeneity assumption
to yield results. Also, the first vector of public goods (𝒛) covers the special cases of a single, scalar
public good (𝑧) as well as an aggregator function that translates a vector of public goods into a
single-valued measure (e.g., 𝑧=𝑓(𝒛)).
We highlight that our utility model allows for a flexible relationship between private and
public goods without assuming strongly or weakly separable utility. Freeman et al. (2014) defines
a strongly separable utility function where the marginal rate of substitution (MRS) of any two
goods, regardless of the subset, is independent of the quantity of any other good. Weakly separable
utility function means that the MRS for any pair of goods within a subset of goods is independent
of the quantities in other subsets. We make no such assumptions. Our modeling assumptions also
imply that there are no choke prices for any of the private goods meaning that weak
complementarity does not hold (Smith and Banzhaf, 2004). Relatedly, but independently, the
Willig condition is not implicit in our model either as Palmquist (2005)'s path-independence
condition does not hold.

 10
3 Compensating and Equivalent Variation
Using the indirect utility function, CV and EV are implicitly defined in Hanemann (1991) as
𝑣(𝑚−CV,𝒑;𝒛%,𝐰)=𝑣(𝑚,𝒑;𝒛+,𝐰)=𝑢+ and 𝑣(𝑚,𝒑;𝒛%,𝐰)=𝑣(𝑚+EV,𝒑;𝒛+,𝒘)=𝑢%,
respectively, with 𝒛+,𝒛%∈𝒛 where 𝒛%≡𝑡𝒛+ such that 𝒛+ is the initial value of 𝒛, while 𝒛% is the
new, scaled value. CV and EV are both positive (negative) when 𝑡>1 (0<𝑡<1). Theorem 1 is
our main result.5,6

Theorem 1. Let 𝑔(∙) be a monotonic transformation such that utility function ℎ(𝒙;𝒛,𝒘)≡
𝑔D𝑢(𝒙;𝒛,𝒘)F is homothetic. If the function 𝑢(𝒙;𝒛,𝒘) is independently homogeneous, such that
𝑡(𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝒛,𝒘) with 𝜂≠0 for all 𝑡>0	and 𝑡)𝑢(𝒙;𝒛,𝒘)=𝑢(𝒙;𝑡𝒛,𝒘) for all 𝑡>0,
then:
(a) Expenditure function 𝑒(𝑢,𝒑;𝒛,𝒘) related to the utility function ℎ(𝒙;𝒛,𝒘) has the property
𝑡,)(⁄𝑒(𝑢,𝒑;𝒛,𝒘)=𝑒(𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑡>0, that is, the expenditure function is
homogeneous of degree 𝜙≡(−𝜃𝜂⁄) in the 𝒛 vector of public goods;
(b) Hicksian demand for the utility function ℎ(𝒙;𝒛,𝒘) is homogenous of degree 𝜙 in public goods
(𝒛); that is, 𝑡.𝑥/ 0(𝑢,𝒑;𝒛,𝒘)=𝑥/ 0(𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑡>0 for all 𝑛=1,…,𝑁, when
𝑢(𝒙;𝒛,𝒘) is strictly quasiconcave; and,
 5 Theorem 1 requires 𝜂≠0 because 𝜂=0 means the degree of homogeneity for the expenditure function is undefined.
6 Since any rational number can be written as a fraction, then 𝜙 as a rational number implies the existence of integer
values for 𝜃 and 𝜂. The ratio 𝜃𝜂⁄ is independent of scale since multiplying the numerator and denominator by 1𝜁⁄,
where 𝜁 is a non-zero integer, yields the same 𝜙. Therefore, Theorem 1 parts (a)-(b) provide a family of utility
functions necessary for a homogeneous expenditure and Hicksian demand function, respectively.

 11
(c) Compensating variation (CV) and equivalent variation (EV) related to the utility function
ℎ(𝒙;𝒛,𝒘) are given by the expressions	CV(𝒛𝟎,𝑡)=𝑒(𝑢+,𝒑;𝒛𝟎,𝒘)−𝑒(𝑢+,𝒑;𝑡𝒛𝟎,𝒘)	and
EV(𝒛𝟎,𝑡)=𝑒(𝑢%,𝒑,𝒛𝟎,𝒘)−𝑒(𝑢%,𝒑;𝑡𝒛𝟎,𝒘). These expressions are equivalent to
CV(𝑚,𝑡)=D1−𝑡.F𝑚 and EV(𝑚,𝑡)=D𝑡,.−1F𝑚, respectively, where 𝑚 is income.
Proof of Theorem 1. All main text proofs appear in Appendix A.

Theorem 1 part (a) proves that a homothetic utility function with an independently
homogeneous underlying function leads to a homogeneous expenditure function in public goods
(𝒛). The expenditure function is homogeneous of degree (−𝜃𝜂⁄)≡𝜙 and thus equal to the
negative ratio of the degrees of homogeneity for the public and private goods. Theorem 1 part (b)
immediately follows from the expenditure function result and shows that Hicksian demand is
homogeneous of degree (−𝜃𝜂⁄)≡𝜙 in the public goods (𝒛%) when 𝑢(⋅) is strictly quasiconcave.
Then, Theorem 1 part (c) provides the closed-form CV and EV expressions given by
CV(𝑚,𝑡)=D1−𝑡,)(⁄F𝑚 and EV(𝑚,𝑡)=D𝑡)(⁄−1F𝑚. For an increase in public good
provision (𝑡>1), the closed-form CV and EV expressions demonstrate three effects that impact
WTP and WTA, respectively, where 𝜙≡(−𝜃𝜂⁄)<0 is a sufficient statistic summarizing
preferences. First, the income effect shows that CV and EV increase with income. Second, the
absolute preference effect occurs when CV and EV increase in the public good preference
parameter 𝜃, holding income and 𝜂 constant. Third, the relative preference effect identifies that
CV and EV increase in the ratio 𝜃𝜂⁄ and this trade-off in utility is independent of proportionally
scaling 𝜃 and 𝜂 whereby CV and EV can be small even if 𝜃 is “large” (noting 𝜃𝜂⁄ is not generally
equal to the marginal rate of substitution between 𝒙 and 𝒛).

 12
For a decrease in public good provision (0<𝑡<1) such that CV and EV are negative
(with CV=EV=0 when 𝑡=1), the resulting welfare losses imply that CV is equivalent to WTA
while EV is equivalent to WTP. However, relevant to our numerical application below, when 𝒛
represents public “bads” then 𝜃<0 (and 𝜙>0), the condition 0<𝑡<1 leads to an increase in
utility and thus CV (EV) is equivalent to WTP (WTA) again.
 The results in Theorem 1 arise when the underlying function 𝑢(⋅) is independently
homogeneous. Appendix B provides results under joint homogeneity, and these additional results
help provide theoretical guidance for the independent homogeneity assumption in our main results.
Also, Appendix B provides results under the restrictive case where 𝑔(⋅) is the identity function
leading to homogeneous utility and help provide intuition for the EV and CV closed-form solutions
that we find under homotheticity in Theorem 1.
By inspection, Theorem 1 shows that CV and EV are asymmetric. Theorem 2 proves EV
is greater than CV always for the same proportional change in public good provision, regardless
of whether public good provision is increasing or decreasing.

Theorem 2. For all 𝑡>0 (𝑡≠1), EV(𝑚,𝑡)>CV(𝑚,𝑡). Also, the ratio EV(𝑚,𝑡)CV(𝑚,𝑡)⁄
increases in 𝜃𝜂⁄ when 𝑡>1, and EV(𝑚,𝑡)CV(𝑚,𝑡)⁄  decreases in 𝜃𝜂⁄ when 0<𝑡<1.

Hanemann (1991) shows that EV equals CV when a public and a private good are perfect
substitutes. Our assumption of independent homogeneity of the utility function in private and
public good(s) rules out the possibility of perfect substitutability (see Appendix A for further
discussion). Consequently, in our framework, EV always exceeds CV, but our results remain
consistent with Hanemann (1991) otherwise. Regardless, in our neoclassical model, the difference

 13
between WTP and WTA for public good provision arises through two mechanisms.7 The first
mechanism comes from the budget constraint leading to a bounded WTP but an unbounded WTA.
The second mechanism is the relative preference effect where the disparity between WTP and
WTA is mediated by 𝜃𝜂⁄	(as shown by Theorem 2). Therefore, a large relative preference effect
can help explain the Tunçel and Hammitt (2014) finding that the WTA-WTP gap is larger for
public goods than private goods.8
One key advantage of our framework is that it identifies the relative preference effect that
drives a systematic wedge between WTP and WTA—beyond the conventional explanations like
behavioral biases (e.g., loss aversion). Thus, the relative preference effect highlights that even in
a fully neoclassical setting, a large discrepancy between WTP and WTA can arise if public goods
are sufficiently “important” relative to the private good. When 𝜃 is large relative to 𝜂, households
will display a substantial difference between what they are willing to pay for a small (or even non-
marginal) increase versus what they would demand in compensation for a comparable decrease.
Empirically, researchers can estimate this ratio 𝜃𝜂⁄ from observed data and upon finding that it
exceeds one, for example, indicates that WTA could be expected to surpass WTP by more than
what standard consumer-surplus approximations (or purely behavioral models) might predict. This
interpretation helps connect seemingly abstract parameters in our model to real -world policy
scenarios—showing why certain public goods trigger unusually large WTA–WTP gaps and how
 7 In a dynamic model, Zhao and Kling (2004) finds a disparity between WTA and WTP due to uncertainty,
irreversibility, and learning.
8 Vossler et al. (2023) explores behavioral explanations for the gap between WTP and WTA for public goods and
shows that implementing incentive-compatible mechanism to control for behavioral effects significantly closes the
gap and provides valid welfare estimates.

 14
one might quantify those gaps without resorting to approximate surplus measures or behavioral
assumptions.
Suppose an empirical study finds that a representative sample of households with an
average annual income of 𝑚=$1000 has a $50 average willingness to pay (WTP) for a 20 percent
improvement in a public good (𝒛). In our model, compensating variation is given by CV(𝑚,𝑡)=
D1−1.2.F1000=50. Solving for (−𝜃𝜂⁄)≡𝜙 finds −0.28≈ln(0.95)ln(1.2)⁄  and thus
implies 𝜃𝜂⁄≈0.28. Interpreting this economically: a smaller 𝜃𝜂⁄ means the public good has less
impact on utility as compared to private goods, all else equal, yielding a smaller WTP for the same
proportional improvement. Researchers could replicate this simple calibration approach across
different sub-samples (e.g., varying incomes or demographic groups) or for different observed
WTP estimates (including those from stated-preference surveys) to estimate how 𝜃𝜂⁄ varies across
the population. This showcases how one can take the theoretical closed-form solutions straight to
real-world data and empirical results.
One practical application arises in urban environmental policy—for example, introduction
of a new municipal water-treatment facility or a large-scale pollution-control program. Typically,
local or national agencies rely on stated preference or hedonic estimates to infer how residents
value cleaner water or improved air quality. Our model can be deployed in such a scenario by (i)
employing existing willingness-to-pay figures from either revealed-preference (e.g., housing price
differentials) or stated-preference surveys, (ii) calibrating the ratio of degrees of homotheticity
(𝜃𝜂⁄) to capture the public good’s weight in utility relative to private goods, and  then (iii)
predicting how WTP or WTA scales with income or other demographic variables. This approach
ensures that even non-marginal policy shifts—like a 50% reduction in air pollution such as
particulate matter concentrations—can be analyzed with exact compensating or equivalent

 15
variation, rather than relying on approximate consumer-surplus measures. Local officials and
researchers could thus compare policy options (e.g., partial vs. full clean-up) in terms of precise
welfare benefits across different income strata and demographic characteristics, thereby linking
sound theoretical underpinnings to concrete policy evaluation.
Finally, because our approach applies to non-marginal changes, it can be deployed in cases
where the policy change involves a major infrastructure investment, a significant environmental
improvement, or a sweeping regulatory shift. The resulting closed-form WTP and WTA formulas
facilitate transparent cost–benefit analyses, especially if policymakers want to gauge winners and
losers in different income brackets. By mapping real -world empirical estimates into these
formulas, agencies can simulate counterfactual policies, compare expected welfare outcomes
across subgroups, and design redistributive mechanisms (e.g., tiered pricing schemes or targeted
transfers) to align policy with equity objectives. Thus, our framework ultimately serves as a
practical toolkit that will help public agencies and researchers to translate utility-based concepts
into actionable, data-driven guidance for large-scale policy decisions.
We conclude this section with Corollary 1 as it makes additional connections between the
CV and EV expressions in Theorem 1 and the representative consumer's budget constraint. Then,
Figure 1 provides a visual representation of Theorem 1 and Corollary 1. To start, we specify the
model to have two private goods (𝑥%,𝑥&), a single public good (𝑧), and let 𝑔(∙) to be the identity
function. Without loss of generality, Figure 1 identifies CV>0 in the 𝑥%-𝑥& space with 𝑡>1 and
𝜙<0. Point A is the horizontal intercept of the budget constraint and equals 𝑚𝑝%⁄ at the original
level of public good provision and income. Similarly, point B is the horizontal intercept of the
budget constraint at the new level of public good provision and income, and equals 𝑡.𝑚𝑝%⁄. The
difference between points B to A equals D1−𝑡.F𝑚𝑝%⁄ =CV𝑝%⁄ >0 since CV=D1−𝑡.F𝑚.

 16
Analogously, CV can be measured on the vertical 𝑥& axis too by observing the difference from
points D to C equals D1−𝑡.F𝑚𝑝&⁄ =CV𝑝&⁄ >0. Therefore, CV can be determined by 𝑝% times
the distance between the points B and A, or, equivalently, 𝑝& times the distance between the points
D and C. Thus, CV is implicitly measured twice in Figure 2, and a similar figure can be constructed
to measure EV.

Corollary 1. Let 𝑔(∙) be a monotonic transformation such that utility function ℎ(𝒙;𝒛,𝒘)≡
𝑔D𝑢(𝒙;𝒛,𝒘)F is homothetic. If the function 𝑢(∙) is independently homogeneous (with 𝜂≠0) and
𝑢(∙) is strictly quasiconcave, then CV can be expressed as follows: CV=∑ CV/ # /2%  , where CV/≡
𝑝/(𝑥/ ∗−𝑥/ 4) for all 𝑛=1,…,𝑁 for the optimal demand vectors 𝒙∗=𝒙𝒉(𝑢+,𝒑;𝒛𝟎,𝒘) and 𝒙4=
𝒙𝒉(𝑢+,𝒑;𝑡𝒛𝟎,𝒘), and, similarly, EV=∑ EV/ # /2% , where EV/≡𝑝/(𝑥/44−𝑥/∗∗) with 𝒙∗∗=
𝒙𝒉(𝑢%,𝒑;𝒛𝟎,𝒘)	and	𝒙44=𝒙𝒉(𝑢%,𝒑;𝑡𝒛𝟎,𝒘).

Figure 1. Compensating Variation

 17
4 Sufficient Statistic
4.A Sufficient Statistic: Calculation and Applications
In this section, we calculate 𝜙≡(−𝜃𝜂⁄) values using actual WTP estimates from the literature.
Analogous calculations can be conducted with the EV closed-form solution and WTA estimates.
Our primary aim in this section is to provide one clear, concrete example of how the closed-form
formulas can be calibrated using a real-world estimate. Although we focus on Ito and Zhang
(2020)’s estimate for this demonstration, we wish to emphasize that the theoretical result itself is
not tied to a single setting like health or environmental economics. As explained above, the
homothetic, non-separable framework can be applied to any context—public finance, industrial
organization, trade, or regional economics —where researchers assume (or approximate)
homothetic preferences for analytical tractability and wish to evaluate non-marginal changes.
Thus, we do not regard this section as an exhaustive survey of all possible uses; rather, it illustrates
how one might implement our approach in practice. Indeed, numerous other studies that rely on
homothetic specifications (e.g., CES preference) could adopt our formulas with relatively minimal
adaptation. Therefore, our example, although drawn from environmental valuation, is sufficiently
indicative of how the framework could be applied broadly.
We begin by selecting two revealed preference studies looking at particulate matter (PM)
pollution in China and compare outcomes. In the first study, Ito and Zhang (2020) find s that
households in China are willing to pay $32.7 annually to reduce PM10 concentrations from 120
micrograms per cubic meter (𝜇g/m5) to 96 𝜇g/m5, or 24 𝜇g/m5 reduction, and in our notation
this means 𝑡=0.80 for a reduction in a public “bad”. As Section 3 discusses, applying our results
to public “bad” requires 𝜃<0 meaning 𝜙>0. The compensating variation formula remains

 18
CV=D1−𝑡.F𝑚, but CV>0 if 0<𝑡<1. Also, rearranging the compensating variation formula
from Theorem 1 yields 𝜙=lni1−67 8jln(𝑡)k . The average annual income of the affected
households in Ito and Zhang (2020)’s study is $527.5/year and thus 𝜙=0.29. In the second study,
Freeman et al. (2019) finds a WTP of $316.4 annually for a one standard deviation decrease in
PM2.5, equal to 14.6 𝜇g/m5 from a baseline of 41.4 𝜇g/m5, and implying 𝑡=0.65.
Freeman et al. (2019) also studies Chinese households, but the sample population is richer
with a median income of $1481.2/year. Again, using the formula in Theorem 1 and solving then
yields 𝜙=0.55.
 Next, we use our CV formula to provide plausible estimates of WTP for similar populations
in the same setting; specifically, we show how to find WTP estimates for different income groups.
Then, we compare our estimates to those in the literature that estimate WTP heterogeneity by
income. Our case study to demonstrate these methods uses the results from Ito and Zhang (2020).
Their study employs a rich dataset and a computationally challenging, random-coefficient logit
model to uncover WTP heterogeneity across household income. Ito and Zhang (2020) reports that
the 95-percent confidence interval for WTP is approximately $12 to $36 annually for households
with income of $1000/year using their random-coefficient estimates, where $1000/year is more
the two standard deviations above the average household income in their sample.9 Importantly, Ito
and Zhang (2020) finds an approximately linear relationship between income and WTP for the
vast majority of the income distribution, only deviating slightly at the upper tail of the distribution,
and this linearity matches the linear relationship in the Theorem 1’s closed-form solutions.
 9 The average income in their sample is $527.5/year with a standard deviation of $153, and the WTP for PM10
reductions overall is $32.7/year. This suggests a skewed income distribution in their sample as WTP estimates by
income in Ito and Zhang (2020) go up to $10,000/year (or more than 68 standard deviations above the mean). See Ito
and Zhang (2020)’s Figure 4.

 19
We use Theorem 1’s CV expression along with Ito and Zhang (2020)’s simpler standard
logit WTP estimate to calculate WTP values for other income groups without needing to deploy a
random-coefficient model. Specifically, the Ito and Zhang (2020) standard logit estimate for the
marginal WTP (MWTP) is approximately $1.25 per 𝜇g/m5 across all income groups. Thus, a 24
𝜇g/m5 reduction yields an approximate total WTP of $30 annually. This implies 𝜙=0.26 at the
average income for 𝑡=0.80. Then, applying the CV expression with the new 𝜙, but with an
income of $1000/year, finds a WTP of $56.0 annually. This WTP approximation is slightly larger
than the upper bound of Ito and Zhang (2020)’s random-coefficient model confidence interval that
is centered on $36/year. Regardless, the estimate of $56/year could feasibly be used in policy
analysis despite $1000/year being far from the average household income. Finally, we have not
yet considered errors in the estimation of pollution reduction (or any other estimate parameters).
Indeed, only a slight change in the pollution reduction ratio to 𝑡=0.87 recovers a WTP of
$36/year, and 𝑡=0.87 is with is within the range implied by Ito and Zhang (2020)’s 95-percent
confidence interval for pollution reduction.10

4.B Sufficient Statistic: Identification and Estimation
If an empirical study is unavailable, then the below methodology shows how to identify and
estimate the sufficient statistic from data directly. Again, the analysis and discussion below in this
section addresses CV and WTP directly, but the methods can be easily adapted for our closed-
 10 Ito and Zhang (2020)’s main estimate for pollution reduction is 24.54 𝜇g/m# with a standard error of 6.97 𝜇g/m#.
From a baseline of 120 𝜇g/m#, this implies calculated value of 𝑡 then ranges from 0.68 to 0.91 such that 0.87 falls
within that range.

 20
form EV expression and thus WTA. Theorem 1 provides the equality 𝑡,)(⁄𝑒(𝑢,𝒑;𝒛,𝒘)=
𝑒(𝑢,𝒑;𝑡𝒛,𝒘), so taking the logarithm of both sides and rearranging yields:
lnn𝑚%
𝑚+
o=(−𝜃𝜂⁄)ln[𝑡] (1)
with 𝒛𝟏=𝑡𝒛+ and 𝑚+=𝑒(𝑢,𝒑;𝒛𝟎,𝒘), and also let 𝑚%=𝑒(𝑢,𝒑;𝑡𝒛𝟎,𝒘)=𝑒(𝑢,𝒑;𝒛𝟏,𝒘) be the
income after the change in the public good provision that maintains a constant level of utility.
Then, define the change public good provision as Δ𝑧≡‖𝒛%‖‖𝒛+‖⁄ =𝑡, and similarly define
Δ𝑚≡𝑚%𝑚+⁄ .
 Next, we translate equation (1) to an estimating equation and start by defining the following
variables: 𝑌 = log of the change in expenditure or income = ln[Δ𝑚]; and, 𝑋% = log of the change
in public good provision = ln[Δ𝑧]. Then, using equation (1), we specify an estimating equation:
𝑌=𝛽++𝛽%𝑋%+𝜀 (2)
where 𝜀 is the error term.11 The parameter of interest is 𝛽% equal to 𝜙≡(−𝜃𝜂⁄), and 𝜙 can be
estimated using quasi-experiment techniques such as instrumental variables or regression
discontinuity. The data needed to estimate equation (2) can be individual-level observations or
aggregate-level data depending on the setting. For example, equation (2) allows the use of
aggregate data such as national income to account for 𝑚 since the structural assumption of
homogeneity enable aggregation over individuals.  However, income data subject to the
requirements of quasi-experimental causal identification may be unavailable, so we next turn to
identifying and estimating 𝜙 using consumption data.
 11 The upper-case 𝑋$ variables in the estimating equation should not be confused with the lower-case 𝑥$ values for
private goods in our utility model.

 21
 Alternatively, although under the stronger assumption of strictly quasiconcave utility,
Theorem 1 finds 𝑡,)(⁄𝑥/ 0(𝑢,𝒑;𝒛,𝒘)=𝑥/ 0(𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑛=1,…,𝑁 meaning that the
equality holds for all private goods. Again, taking the logarithm of both sides and rearranging
yields:
lnn𝑥/%
𝑥/+
o=(−𝜃𝜂⁄)ln[𝑡]	∀	𝑛=1,…,𝑁 (3)
where 𝑥/+=𝑥/ 0(𝑢,𝒑;𝒛+,𝒘) and 𝑥/%=𝑥/ 0(𝑢,𝒑;𝑡𝒛+,𝒘)=𝑥/ 0(𝑢,𝒑;𝒛%,𝒘) are the private
consumption quantities related to the level of public good provision. Then, define the change in
private good consumption as Δ𝑥/≡𝑥/%𝑥/+⁄ , and redefine the dependent variable as	𝑌4 = log of
the change in private consumption of the 𝑛:; good = ln[Δ𝑥/]. Thus, we can specify an alternative
estimating equation:
𝑌/4=𝛽+/+𝛽%/𝑋%+𝜀/4		∀	𝑛=1,…,𝑁 (4)
where 𝜀/4 is the error term for each good and noting 𝑋%=ln[𝑡] is common across private goods.
Then, to identify 𝛽%/, equation (4) can be estimated for a single good using quasi-experimental
methods in a similar manner to equation (2). However, if data on multiple private goods is available
at the individual- or aggregate-level, then (4) becomes a system of seemingly unrelated regression
equations to estimate the parameter of interest. Furthermore, ex-post inference can check if 𝛽%/ is
the same across all equations or the researcher can constrain 𝛽%/ to be the same across equations.
As we discuss above, Ito and Zhang (2020) provides a good example where data could be used to
calculate 𝜙 directly as that study employs a regression discontinuity method to find the change in
private air filter purchases (𝑥/) for a change in particulate matter pollution (𝑡).
 The goal when estimating equation (2) or (4) is to identify and estimate the parameter 𝛽%=
𝜙≡(−𝜃𝜂⁄) noting that the same 𝑋% appears in both equations. Importantly, it is not necessary to

 22
separately identify and estimate the parameters 𝜂 and 𝜃. Rather, it is only necessary to identify and
estimate the ratio −𝜃𝜂⁄ as this ratio appears in the CV expression (and similarly for EV). That is,
𝜙 is a sufficient statistic in the statistical meaning (Reid, 2015) , and, relatedly, infinite
combinations of the primitives 𝜂 and 𝜃 generate the same 𝜙. Also, the sign of 𝜙 determines the
sign of CV, so 𝜙 is a sufficient statistic in the economic meaning as well (Chetty, 2009). The level
values of the preference parameters 𝜂 and 𝜃, all else equal, do not affect the CV expression because
the underlying result in Theorem 1 only uses the ordinal properties of the homogeneous function
𝑢(𝒙;𝒛,𝒘) that translate to the homothetic utility function ℎ(𝒙;𝒛,𝒘). It is the relative importance
of the public goods to the private goods as expressed by the ratio 𝜃𝜂⁄ that matters.
 We note that ln[𝑡] is needed in both estimating equations where 𝑡>0 is the scaling of
public good provision in either quality and/or the quantity of the public goods. The vector 𝒛 can
be a single, scalar public good, a vector of public goods summarized by a single statistic ( 𝑧=
𝑔(𝒛)), or a vector of public goods that all change by the same quantity and/or quality. The variable
definitions prior to equation (4) in this section say "expenditure or income" due to the single-period
utility maximization model of the representative consumer.12

5 Additively Separable Utility
In this last section, we address the special case of additively separable utility since this assumption
often explicitly or implicitly arises in many theoretical and empirical contexts. We will focus on
utility functions with only 𝒛. That is, we drop 𝒘 from the model. Under additivity, the utility
 12 Diewart (2012) provides necessary and sufficient conditions using Afriat's Theorem to check whether finite price
and quantity data are consistent with homothetic utility maximization.

 23
function can be written as 𝑢(𝒙;𝒛)=	𝑢%(𝒙)+𝑢&(𝒛) where 𝑢&(∙) is an additive utility term
containing the public goods. That is, public goods influence only the level of utility but not
consumer choices on the margin; for instance, if more public parks make a consumer better off but
do not change the marginal incentive to buy hiking boots. However, Example 1 shows that a utility
function with additively separable public goods does not necessarily lead to a homogeneous
expenditure function in public goods and thus Theorem 1 does not hold. Rather, Example 1
suggests that the expenditure function under additive separability includes the term "𝑢−𝑢&(𝒛)"
and Proposition 1 proves that this is true for all additively separable utility functions, and vice
versa.

Example 1: Let 𝑢(𝒙;𝒛)=𝑢%(𝒙)+𝑢&(𝒛)=(𝑥%𝑥&)%<=+(𝑧%%𝑧%&)%>= with 𝒛=(𝑧%%	𝑧%&) where
𝑢(𝒙;𝒛) is jointly homogeneous of degree 𝛾=2𝛿⁄ when 𝛿=𝛼=𝛽. Assume the function is
jointly homogeneous and then expenditure function is found to be 𝑒(𝑢,𝒑;𝒛)=2i𝑢−
(𝑧%%𝑧%&)% ?=j ?&= (𝑝%𝑝&)%&=. However, the expenditure function is not homogeneous in the public
goods as shown by 𝑒(𝑢,𝒑;𝑡𝒛)=2i𝑢−(𝑧%%𝑧%&)% ?=(𝑡)& ?=j ?&= (𝑝%𝑝&)%&=.

Proposition 1. The utility function is additively separable in the public good, such that 𝑢(𝒙;𝒛)=
	𝑢%(𝒙)+𝑢&(𝒛), if and only if the expenditure function can be expressed  as 𝑒(𝑢,𝒑;𝒛)=
𝑒(𝑢−𝑢&(𝒛),𝒑).

Finally, Proposition 2 finds an expression for the expenditure function in terms of indirect
utility and the degree of homogeneity of 𝑢%(𝒙). This result explicitly relates private expenditure

 24
to public goods despite additive separability. However, as Example 1 demonstrates, it does not
allow for the compensating or equivalent variation expressions for public goods considered by our
main theorem in Section 3.

Proposition 2. If a utility function is additively separable in public good and 𝑢%(𝒙) is
homogeneous of degree 𝛾≠0, then the expenditure function has the form 𝑒(𝑢,𝒑;𝒛)=
{@,@"(𝒛) D!(%,𝒑)| %*⁄ .

6 Conclusion
Governments incur billions of dollars in costs to provide public goods but the willingness to pay
(WTP) and willingness to accept (WTA) for changes in public goods are not directly observable
by policymakers. This study derives exact closed-form compensating variation (CV) and
equivalent variation (EV) expressions for a change in public good provision, where the change can
be in the quantity and/or quality of the public good(s). These closed-form expressions provide a
concrete bridge between the theorems in this study and a wide range of real-world applications
across fields and settings that employ WTP and WTA for public goods.
The CV and EV expressions we find are linear in initial income but mediated by preference
parameters from a homothetic utility function with an independently homogeneous underlying
function. We also show two different ways to estimate a single sufficient statistic for the two
preference parameters in our expressions. Furthermore, we identify three mechanisms – that we
call the income effect, absolute preference effect, and relative preference effect – that drive CV
and EV in our model and help explain the gap between WTP and WTA for public goods. Our

 25
results contribute to the literature by providing exact CV and EV expressions for both marginal
and non-marginal changes in public good provision for a family of homothetic utility functions. In
addition, we show how to derive the sufficient statistic from WTP (WTA) estimates in the literature
and then how those estimates can be used to calculate WTP (WTA) across income groups.
 The model generating our CV and EV expressions are for homothetic utility functions that
encompass a wide spectrum of functions that have been employed in contemporary theoretical and
empirical economic studies. The CV and EV expressions derived here remain valid when an
auxiliary public goods vector is included in the utility function but not subject to the homogeneity
condition; rather, only the public good of interest must manifest independent homogeneity.
Furthermore, the much-employed Willig condition also has a restriction with respect to income
(Smith and Banzhaf, 2004) and employs consumer surplus as an approximate welfare measure
because demand is not directly observed for public goods (Bockstael and McConnell, 1993). This
limits the conventional willingness-to-pay analysis to marginal changes in public goods, but our
closed-form solutions are not limited to marginal changes. In addition, our CV and EV expressions
do not use consumer surplus as a welfare approximation and thus provides exact WTP and WTA
measures for both marginal and non-marginal changes in public good provision.

References
Aldy, Joseph E., Maximilian Auffhammer, Maureen Cropper, Arthur Fraas, and Richard
Morgenstern. 2022. “Looking Back at 50 Years of the Clean Air Act.” Journal of Economic
Literature, 60(1): 179-232.
Amiran, Edoh, Y., and Daniel A. Hagen. 2003. “Willingness To Pay and Willingness to Accept:
How Much Can They Differ? Comment.” American Economic Review, 93(1): 458-463.
Chan, Nathan W., and Matthew J. Kotchen. 2014. “A general impure public good and linear
characteristics of green consumptions.” Resource and Energy Economics, 37: 1-16.

 26
Chan, Nathan W. 2024. “A Unifying Algebra of Green Consumption Technologies.” Journal of
the Association of Environmental and Resource Economists, 11(4): 797-825.
Banzhaf, H. Spencer. 2021. “Differences-in-Difference Hedonics.” Journal of Political Economy:
129(8): 2385-2414.
Barbier, Edward B., Mikołaj Czajkowski, and Nick Hanley. “Is the income elasticity of the
willingness to pay for pollution control constant?” Environmental and Resource Economics,
68(3): 663-682.
Bockstael, Nancy E., and Kenneth E. McConnell. 1993. “Public goods as characteristics of non-
market commodities.” The Economic Journal, 103(420): 1244-1257.
Caselli, Francesco, and Jaume Ventura. 2000. “A representative consumer theory of distribution.”
American Economic Review, 90(4): 909-926.
Chattopadhyay, Sudip. 1999. “Estimating the Demand for Air Quality: New Evidence Based on
the Chicago Housing Market.” Land Economics: 75(1): 22-38.
Chetty, Raj. 2009. “Sufficient Statistics for Welfare Analysis: A Bridge Between Structural and
Reduced-Form Methods.” Annual Review of Economics, 1(1): 451-488.
Collie, David R. 2022. “CRRA utility and the sustainability of cooperation in infinitely-repeated
games.” Economics Letters, 221: 110897.
Deaton, Angus, and John Muellbauer. 1980. Economics and consumer behavior: Cambridge
university press.
Diewert, W. Erwin. 2012. “Afriat's Theorem and Some Extensions to Choice Under Uncertainty.”
The Economic Journal, 122(560): 305-331.
Duranton, Gilles, and Matthew A. Turner. 2012. “Urban Growth and Transportation.” Review of
Economic Studies, 79(4): 1407-1440.
Epstein, Larry G, and Stanley E. Zin. 1989. “Substitution, Risk Aversion, and the Temporal
Behavior of Consumption and Asset Returns: A Theoretical Framework.” Econometrica,
57(4): 937-969.
Espinosa, Miguel A., and Juan D. Prada. 2012. “Identities for Homogeneous Utility Functions.”
Economics Bulletin, 32(3): 2026-2034.
Feenberg, Daniel, and Edwin S. Mills. 1980. Measuring the Benefits of Water Pollution
Abatement: Academic Press.

 27
Fujimori, Shinichiro, Ken Oshiro, Tomoko Haesgawa, Junya Takakura, and Kayo Ueda. 2023.
“Climate change mitigation costs reductions caused by socioeconomic -technological
transitions.” NPJ Climate Action 2, 9: https://doi.org/10.1038/s44168-023-00041-w
Freeman, A. Myrick, Joseph A. Herriges, and Catherine L. Kling. 2014. The Measurement of
environmental and resources values: theory and methods (3rd edition). New York: RFF Press.
Freeman, Richard, Wenquan Liang, Ran Song, and Christopher Timmins. 2019. “Willingness to
pay for clean air in China.” Journal of Environmental Economics and Management, 94(1):
188-216.
Fullerton, Don, and Chi L. Ta. 2019. “Environmental policy on the back of an envelope: A Cobb-
Douglas model is not just a teaching tool.” Energy Economics, 84: 104447.
Goulder, Lawrence, and Marc Hafstead. 2017. Confronting the climate challenge: US policy
options. New York: Columbia University Press.
Hanemann, W. Michael. 1991. “Willingness to Pay and Willingness to Accept: How Much Can
They Differ?” The American Economic Review, 81(3): 635-647.
Horowitz, John K., and Kenneth E. McConnell. 2002. “A Review of WTA/WTP Studies.” Journal
of Environmental Economics and Management, 44(3): 426-447.
Ito, Koichiro, and Shuang Zhang. 2020. “Willingness to Pay for Clean Air: Evidence from Air
Purifier Markets in China.” Journal of Political Economy, 128(5): 1627-1672.
Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. 1990. “Experimental tests of the
endowment effect and the Coase theorem.” Journal of Political Economy 98(6): 1325-1348.
Kucheryavyy, Konstantin. 2012. “Continuity of a model with a nested CES utility function and
Bertrand competition.” Economics Letters 117(2): 473-476.
Larson, Douglas M. 1992. “Further results on willingness to pay for nonmarket goods.” Journal
of Environmental Economics and Management, 23(2): 101-122.
Mäler, Karl-Göran. 1974. Environmental Economics: A Theoretical Inquiry: Resources for the
Future.
Neary, J. Peter, and Kevin W.S. Roberts. 1980. “The theory of household behavior under
rationing.” European Economic Review, 13(1): 25-42.
Neill, Jon R. 1988. “Another theorem on using market demands to determine willingness to pay
for non-traded goods.” Journal of Environmental Economics and Management, 15(2): 224-
232.

 28
Palmquist, Raymond B. 2005. “Weak complementarity, path independence, and the intuition of
the Willig condition.” Journal of Environmental Economics and Management, 49(1): 103-
115.
Pindyck, Robert S. 2012. “Uncertain outcomes and climate change policy.” Journal of
Environmental Economics and management, 63(3): 289-303.
Quigley, John M. 1982. “Nonlinear budget constraints and consumer demand: An application to
public programs for residential housing.” Journal of Urban Economics, 12(2): 177-201.
Reid, Nancy. 2015. “Statistical Sufficiency.” (in) International Encyclopedia of the Social &
Behavioral Sciences (2nd Ed., Oxford: Elsevier), Vol. 23: 418-422.
Slesnick, Daniel T. 1998. “Empirical Approaches to the Measurement of Welfare.” Journal of
Economic Literature, 36(4): 2108-2165.
Smith, V. Kerry, and H. Spencer Banzhaf. 2004. “A Diagrammatic Exposition of Weak
Complementarity and the Willig Condition.” American Journal of Agricultural Economics,
86(2), 455-466.
Smith, V. Kerry, and H. Spencer Banzhaf. 2007. “Quality adjusted price indexes and the Willig
condition.” Economics Letters, 94(1): 43-48.
Smith, V. Kerry, Mary F. Evans, H. Spencer Banzhaf, and Christine Poulos. 2010. “Can weak
substitution be rehabilitated?” Environmental and Resource Economics, 45(2): 203-221.
Simon, Carl P., and Lawrence Blume. 1994. Mathematics for Economists. New York: W.W.
Norton & Company.
Tiebout, Charles. 1956. “A Pure Theory of Local Expenditures.” Journal of Political Economy,
64(5): 416-24.
Tunçel, Tuba, and James K. Hammitt. “A new meta-analysis of the WTP/WTA disparity.” Journal
of Environmental Economics and Management, 68(1): 175-187.
U.S. Bureau of Economic Analysis (BEA). 2022. State and Local Government Gross Investment
[SLINV], retrieved from FRED, Federal Reserve Bank of St. Louis;
https://fred.stlouisfed.org/series/SLINV, March 7, 2022.
U.S. Government Accountability Office (GAO). 2021. “Opportunities Exist to Improve DOD's
Management of Defense Spending.” Washington, DC: GAO-21-415T.
Varian, Hal R. 2002. Microeconomic Analysis (Third Edition). New York: W.W. Norton &
Company.

 29
Vossler, Christian A., Stéphanie Bergeron, Maurice Doyon, and Daniel Rondeau. 2023. Journal
of the Association of Environmental and Resource Economists, 10(2): 413-445.
Weber, William L. 1992. “Exact Aggregation and the Demand for Public Goods.” Journal of
Economic Studies, 19(4): 3-16.
Willig, Robert D. 1978. “Incremental consumer's surplus and hedonic price adjustment.” Journal
of Economic Theory, 17(2): 227-253.
Zhao, Jinhua, and Catherine L. Kling. 2004. “Willingness to Pay, Compensating Variation, and
the Cost of Commitment.” Economic Inquiry, 43(3): 503-517.

 30
Appendix A
Proof of Theorem 1. Part (a): Begin with the EMP definition:
𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙{𝒑⋅𝒙:ℎ(𝒙;𝒛,𝒘)≥𝑢}
⇔𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙~𝒑⋅𝒙:𝑔D𝑢(𝒙;𝒛,𝒘)F≥𝑢 [Definition]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙~𝒑⋅𝒙:𝑔D𝑢(𝒙;𝑡𝒛,𝒘)F≥𝑢
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑔i𝑡)𝑢(𝒙;𝒛,𝒘)j≥𝑢 [Assumption: Homogeneity of 𝑢(∙) in 𝒛]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑔𝑡)𝑢iG(&’(⁄) G(&’(⁄)𝒙;𝒛,𝒘j≥𝑢
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑔𝑡)𝑡H(,)(⁄)(I𝑢i% G(&’(⁄)𝒙;𝒛,𝒘j≥𝑢 [Assumption:
Homogeneity of 𝑢(∙) in 𝒙]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑔𝑢i% G(&’(⁄)𝒙;𝒛,𝒘j≥𝑢
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙J~𝒑⋅𝑡(,)(⁄)𝒙:𝑔(𝑢(𝒙;𝒛,𝒘)≥𝑢) [Unit conversion: 𝒙= % G(&’(⁄)𝒙]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=𝑡(,)(⁄)min𝒙J~𝒑⋅𝒙:𝑔D𝑢(𝒙;𝒛,𝒘)F≥𝑢 [Min operator property]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=𝑡(,)(⁄)min𝒙J{𝒑⋅𝒙:ℎ(𝒙;𝒛,𝒘)≥𝑢} [Definition]
⇔𝑒(𝑢,𝒑;𝑡𝒛,𝒘)=𝑡(,)(⁄)𝑒(𝑢,𝒑;𝒛,𝒘) [Definition].

Part (b): When 𝑢(𝒙;𝒛,𝒘) is independently homogeneous then from part (a) we know
𝑡,)(⁄𝑒(𝑢,𝒑;𝒛,𝒘)=𝑒(𝑢,𝒑;𝑡𝒛,𝒘). Let the Hicksian demands in vector form be defined as
𝒙∗≡𝒙𝒉(𝑢,𝒑;𝒛,𝒘) and 𝒙4≡𝒙𝒉(𝑢,𝒑;𝑡𝒛,𝒘). Since the utility level is fixed, then it follows:
ℎ(𝒙∗;𝒛,𝒘)=ℎ(𝒙4;𝑡𝒛,𝒘)
⇔𝑔D𝑢(𝒙∗;𝒛,𝒘)F=𝑔D𝑢(𝒙4;𝑡𝒛,𝒘)F

 31
⇔𝑢(𝒙∗;𝒛,𝒘)=𝑢(𝒙4;𝑡𝒛,𝒘) [Apply 𝑔,%(∙) to both sides]
⇔𝑢(𝒙∗;𝒛,𝒘)=𝑡)𝑢(𝒙4;𝒛,𝒘) [Assumption: Homogeneity of 𝑢(∙) in 𝒛]
⇔𝑡,)𝑢(𝒙∗;𝒛,𝒘)=𝑢(𝒙4;𝒛,𝒘)
⇔𝑢D𝑡,)(⁄𝒙∗;𝒛,𝒘F=𝑢(𝒙4;𝒛,𝒘) [Assumption: Homogeneity of 𝑢(∙) in 𝒙]
and therefore 𝑡,)(⁄𝒙∗=𝒙4 by strict quasi-concavity leading to uniqueness. Alternatively,
assuming a differentiable expenditure function, this part of the corollary can be proven by
differentiating the expenditure function and applying Shepard's Lemma.

Part (c): To start, define the utility levels given different levels of public goods provision as
follows:
𝑢+≡𝑣(𝑚,𝒑;𝒛+,𝐰)
𝑢%≡𝑣(𝑚,𝒑;𝒛%,𝐰)
with 𝒛%≡𝑡𝒛+ (for 𝑡>0) where 𝒛+,𝒛%∈𝒛. We call 𝒛+ the “initial” of “original” level of public
good provision and 𝒛% the “new” or “scaled” level of public good provision. Recall that Mäler’s
indirect utility definition for CV found in Hanemann (1991) is given as:
𝑣(m−CV,𝒑;𝒛%,𝐰)=𝑣(𝑚,𝒑;𝒛+,𝐰)=𝑢+
where 𝑚 is the fixed income level from the utility maximization problem (UMP). For the CV
expression, 𝑚 and 𝑚−CV are the levels of expenditure needed to reach utility level 𝑢+ with public
good levels 𝒛+ and 𝒛%, respectively. In turn, this means:
𝑚=𝑒(𝑢+,𝒑;𝒛+,𝐰)
𝑚−CV=𝑒(𝑢+,𝒑;𝒛%,𝐰)
and subtracting the equations finds:
CV=𝑒(𝑢+,𝒑;𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝒛%,𝐰)⇔CV=𝑒(𝑢+,𝒑;𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝑡𝒛+,𝐰).

 32
If 𝑡>1, then 𝒛%>𝒛+ meaning 𝑒(𝑢+,𝒑;𝒛+,𝒘)>𝑒(𝑢+,𝒑;𝒛%,𝒘), implying CV>0, since a higher
level of public good provision requires a lower level of expenditure to achieve utility 𝑢+. For this
increase in public good provision, CV>0 is an individual’s willingness to pay (WTP) to go from
an initial, lower (𝒛+) to a new, higher (𝒛%) level of public good provision.
In contrast, if 0<𝑡<1, then 𝒛+>𝒛% and CV<0. Here, compensating variation measures
the willingness to accept (WTA) a decrease in public good provision from the initial to the new
level. As such, the absolute value of CV is the amount that an individual must be paid to return to
the initial utility 𝑢+.
 Similarly, Mäler’s indirect utility definition for EV found in Hanemann (1991) is given as:
𝑣(𝑚,𝒑;𝒛%,𝐰)=𝑣(𝑚+EV,𝒑;𝒛+,𝐰)=𝑢%.
For the EV expression, 𝑚 and 𝑚+EV are the levels of expenditure needed to reach utility level
𝑢% with public good levels 𝒛% and 𝒛+, respectively. In turn, this means:
𝑚=𝑒(𝑢%,𝒑;𝒛%,𝐰)
𝑚+EV=𝑒(𝑢%,𝒑;𝒛+,𝐰)
and subtracting the equations finds:
−EV=𝑒(𝑢%,𝒑;𝒛%,𝐰)−𝑒(𝑢%,𝒑;𝒛+,𝐰)
⇔EV=𝑒(𝑢%,𝒑;𝒛+,𝐰)−𝑒(𝑢%,𝒑;𝒛%,𝐰)⇔EV=	𝑒(𝑢%,𝒑;𝒛𝟎,𝐰)−	𝑒(𝑢%,𝒑;𝒕𝒛+,𝐰).
If 𝑡>1, then 𝒛%>𝒛+ meaning 𝑒(𝑢%,𝒑;𝒛+,𝐰)−𝑒(𝑢%,𝒑;𝒛%,𝐰), implying EV>0, since EV is
the amount that an individual must be paid (i.e., willingness to accept) when returning to the
original level of public good provision 𝒛+ but still maintaining the new level of utility 𝑢%. In other
words, EV is the amount an individual would accept to forgo the higher level of public good
provision while keeping to the same level of utility. If 0<𝑡<1, then EV<0 represents the

 33
amount an individual would be willing to pay to return to 𝑢% since the new level of public good
provision 𝒛% is less than the original level 𝒛+.

We continue part (c) of the proof as follows. For CV,
CV(𝒛+,𝑡)=𝑒(𝑢+,𝒑;𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝑡𝒛+,𝐰) [Definition]
⇔CV(𝒛+,𝑡)=𝑒(𝑢+,𝒑;𝒛𝟎,𝒘)−𝑡.𝑒(𝑢+,𝒑;𝒛𝟎,𝒘) [Theorem 1 part (a)]
⇔CV(𝒛+,𝑡)=D1−𝑡.F𝑒(𝑢+,𝒑;𝒛𝟎,𝒘)
⇔CV(𝑚,𝑡)=D1−𝑡.F𝑚.
Alternatively,
CV(𝒛+,𝑡)=𝑒(𝑢+,𝒑;𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝑡𝒛+,𝐰) [Definition]
⇔CV(𝒛+,𝑡)=𝑒(𝑢+,𝒑;𝑡,%𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝒛%,𝐰) [since 𝒛%≡𝑡𝒛+]
⇔CV(𝒛+,𝑡)=𝑡,.𝑒(𝑢+,𝒑;𝒛+,𝐰)−𝑒(𝑢+,𝒑;𝒛%,𝐰) [Theorem 1 part (a)]
⇔CV(𝒛+,𝑡)=D𝑡,.−1F𝑒(𝑢+,𝒑;𝒛%,𝐰)
⇔CV=D𝑡,.−1F(𝑚−CV) [Definition]
⇔CV=𝑡,.(𝑚−CV)−(𝑚−CV)⇔CV=𝑡,.(𝑚−CV)−𝑚+CV
⇔0=𝑡,.(𝑚−CV)−𝑚⇔0=𝑚−CV−𝑡.𝑚⇔CV=𝑚−𝑡.𝑚
⇔CV(𝑚,𝑡)=D1−𝑡.F𝑚.
Similarly, for EV, we have:
EV(𝒛+,𝑡)=	𝑒(𝑢%,𝒑;𝒛𝟎,𝒘)−	𝑒(𝑢%,𝒑;𝑡𝒛+,𝒘) [Definition]
⇔EV(𝒛%,𝑡)=	𝑒(𝑢%,𝒑;𝑡,%𝒛𝟏,𝒘)−	𝑒(𝑢%,𝒑;𝒛%,𝒘) [since 𝒛%≡𝑡𝒛+]
⇔EV(𝒛%,𝑡)=𝑡,.𝑒(𝑢%,𝒑;𝒛𝟏,𝒘)−	𝑒(𝑢%,𝒑;𝒛%,𝒘) [Theorem 1 part (a)]
⇔EV(𝒛%,𝑡)=	𝑡,.	𝑒(𝑢%,𝒑;𝒛%,𝒘)−𝑒(𝑢%,𝒑;𝒛𝟏,𝒘)

 34
⇔EV(𝒛%,𝑡)=	D𝑡,.−1F𝑒(𝑢%,𝒑;𝒛%,𝒘)
⇔EV(𝑚,𝑡)=D𝑡,.−1F𝑚.
Alternatively,
EV(𝒛+,𝑡)=	𝑒(𝑢%,𝒑;𝒛𝟎,𝒘)−	𝑒(𝑢%,𝒑;𝑡𝒛+,𝒘) [Definition]
⇔EV(𝒛+,𝑡)=	𝑒(𝑢%,𝒑;𝒛𝟎,𝒘)−𝑡.𝑒(𝑢%,𝒑;𝑡𝒛+,𝒘) [Theorem 1 part (a)]
⇔EV(𝒛+,𝑡)=	D1−𝑡.F𝑒(𝑢%,𝒑;𝒛+,𝒘)
⇔EV=	D1−𝑡.F(𝑚+EV) [Definition]
⇔EV=	(𝑚+EV)−𝑡.(𝑚+EV)⇔0=	𝑚−𝑡.(𝑚+EV)⇔0=𝑡,.𝑚−(𝑚+EV)
⇔0=𝑡,.𝑚−(𝑚+EV)⇔0=𝑡,.𝑚−𝑚−EV⇔EV=𝑡,.𝑚−𝑚
⇔EV(𝑚,𝑡)=D𝑡,.	−1F𝑚.  Q.E.D.

Proof of Theorem 2.
Define 𝜌≡𝜃𝜂⁄. Begin with EV(𝑚,𝑡)>CV(𝑚,𝑡) for a fixed 𝑡>0, and proceed as follows:
D𝑡)(⁄−1F𝑚>D1−𝑡,)(⁄F𝑚 [Theorem 1]
⇔(𝑡K−1)𝑚=EV(𝜌)>CV(𝜌)=(1−𝑡,K)𝑚 [Define EV and CV as functions of 𝜌]
⇔𝑡K+𝑡,K−2>0
⇔D𝑡K&⁄−𝑡,K&⁄F& >0 and this last statement is true for all 𝜌 and 𝑡, thus EV>CV, always.

Next, calculate the derivative of EV(𝜌)CV(𝜌)⁄ . To start, LM7 LK=𝑚𝑡Kln𝑡 and  L67 LK=𝑚𝑡,Kln𝑡.
Applying the quotient rule finds:
𝑑
𝑑𝜌EV(𝜌) CV(𝜌)=𝑑EV(𝜌)CV(𝜌)−EV(𝜌)dCV(𝜌) [CV(𝜌)]&

 35
⇔
(𝑚𝑡Kln𝑡)(1−𝑡,K)𝑚−(𝑡K−1)𝑚(𝑚𝑡,Kln𝑡)
[(1−𝑡,K)𝑚]&
⇔
(𝑡Kln𝑡)(1−𝑡,K)−(𝑡K−1)(𝑡,Kln𝑡)
(1−𝑡,K)&
⇔ln𝑡∙(𝑡K)(1−𝑡,K)−(𝑡K−1)(𝑡,K) (1−𝑡,K)&
⇔ln𝑡∙
(𝑡K)(1−𝑡,K)−(1−𝑡,K)
(1−𝑡,K)&
⇔ln𝑡∙𝑡K−1 1−𝑡,K=ln𝑡∙ (𝑡K−1)𝑚 (1−𝑡,K)𝑚=ln𝑡∙EV CV.
For public goods, 𝜃>0 and 𝜌>0, and increasing a public good implies 𝑡>1. As shown above,
EV>CV>0 and ln𝑡>0 for 𝑡>1, so the ratio increases. For 0<𝑡<1, then CV<EV<0,
but the ratio NO PO>0 and ln𝑡<0, so the ratio decreases.  Q.E.D.

The inequality EV>CV is a consequence of private and the public goods being (imperfect)
substitutes under the independent homogeneity assumption. To begin, the inequality EV>CV is
equivalent to:
𝑒(𝑢%,𝑝,𝑧+,𝑤)−𝑒(𝑢%,𝑝,𝑡𝑧+,𝑤)>	𝑒(𝑢+,𝑝,𝑧+,𝑤)−	𝑒(𝑢+,𝑝,𝑡𝑧+,𝑤)
and this can be rewritten as:
𝑒(𝑢%,𝑝,𝑧+,𝑤)−	𝑒(𝑢+,𝑝,𝑧+,𝑤)>𝑒(𝑢%,𝑝,𝑡𝑧+,𝑤)−	𝑒(𝑢+,𝑝,𝑡𝑧+,𝑤). (A1)

Consider a small increase in the utility around 𝑢+ to 𝑢%. Then, the first-order Taylor expansions of
the expenditure function in utility are given:
𝑒(𝑢%,𝑝,𝑧+,𝑤)≈𝑒(𝑢+,𝑝,𝑧+,𝑤)+	QR(@+,S,T+,U) Q@ (𝑢%−𝑢+)

 36
𝑒(𝑢%,𝑝,𝑡𝑧+,𝑤)≈𝑒(𝑢+,𝑝,𝑡𝑧+,𝑤)+	QR(@+,S,GT+,U) Q@ (𝑢%−𝑢+)
Substituting the above expansions into (A1) and canceling then implies:
𝜕𝑒(𝑢+,𝑝,𝑧+,𝑤)
𝜕𝑢 >𝜕𝑒(𝑢+,𝑝,𝑡𝑧+,𝑤) 𝜕𝑢 . (A2)
The relationship in (A2) is a direct consequence of EV>CV. This derivative of the expenditure
function with respect to utility is the incremental expenditure required to raise utility by one unit at
a given level of the public good. Therefore, the inequality in (A2) means that it costs more money
to achieve a one unit increase in utility when the public good is at the lower level 𝑧+ than when it
is at the higher level 𝑡𝑧+ (when 𝑡>1). The economic intuition is as follows. Utility levels increase
due to the increase in private as well as public goods. However, since public goods are exogeneous,
they cannot be directly increased through an increase in the expenditure. When public good
provision is low, individuals spend additional income on private substitutes to maintain the same
level of utility (𝑢+). This additional expenditure makes up for the low level of the public good and
means that improving utility by one unit also requires additional marginal spending relative to a
higher level of public good provision. In other words, when the public good provision is higher,
less spending on substitute private goods is needed, so raising utility costs less.

Next, we show that the private and the public goods that satisfy the independent homogeneity
assumption are (imperfect) substitutes. Recall that:
𝑡)𝑢(𝒙;𝒛,𝒘)=𝑢(𝒙;𝑡𝒛,𝒘) (A3)

𝑡(𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝒛,𝒘). (A4)

 37
Then, starting with (A3): 𝑡)𝑢(𝒙;𝒛,𝒘)=𝑢(𝒙;𝑡𝒛,𝒘)⇔𝑡()(⁄)(𝑢(𝒙;𝒛,𝒘)=𝑢(𝒙;𝑡𝒛,𝒘). Next,
using (A4), we get 𝑢D𝑡)(⁄𝒙;𝒛,𝒘F=𝑢(𝒙;𝑡𝒛,𝒘). This last relationship shows that an increase in
public goods (that satisfies the independent homogeneity condition) can be substituted by an
increase in the private good and implies that these are (imperfect) substitutes.

Proof: Independent homogeneity excludes perfect substitutes.
For two goods to be perfect substitutes, their marginal rate of substitution (MRS) must be constant.
Consider the special case of an independently homogenous utility function with a single public
good 𝑧 such that 𝑡(𝑢(𝒙;𝑧)=𝑢(𝑡𝒙;𝑧) and 𝑡)𝑢(𝒙;𝑧)=𝑢(𝒙;𝑡𝑧). Also, let 𝒙=𝑡𝒙 and 𝑧̃=𝑡𝑧
(with 𝑡≠1). Then, differentiating finds with respect to some private good 𝑥V:
𝑡,𝜕𝑢 𝜕𝑥$ =𝜕𝑢 𝜕𝑥:$ 𝜕𝑥:$ 𝜕𝑥$ ⇔𝑡,𝜕𝑢 𝜕𝑥$ =𝜕𝑢 𝜕𝑥:$ 𝑡⇔𝑡,-.𝜕𝑢 𝜕𝑥$ =𝜕𝑢 𝜕𝑥:$ ⇔𝑡,-.
/0
/1!
/0
/2
=
/0
/13!
/0
/2
⇔
/0
/1!
/0
/2
=𝑡.-,
/0
/13!
/0
/2

and, similarly, for 𝑧,
𝑡4𝜕𝑢 𝜕𝑧=𝜕𝑢 𝜕𝑧̃ 𝜕𝑧̃ 𝜕𝑧⇔𝑡4𝜕𝑢 𝜕𝑧=𝜕𝑢 𝜕𝑧̃𝑡⇔𝑡4-.𝜕𝑢 𝜕𝑧=𝜕𝑢 𝜕𝑧̃⇔𝑡.-4
/0
/1!
/0
/2
=
/0
/1!
/0
/23
⇔
/0
/1!
/0
/2
=𝑡4-.
/0
/1!
/0
/23
.
Then, the MRS at (𝑥V,𝑧) equals Q@ QW5 Q@ QTk, and setting equal from both expressions above finds:
Q@
QW5
Q@
QT
=𝑡%,(
Q@
QWX5
Q@
QT
=𝑡),%
Q@
QW5
Q@
QTX
⟹𝑀𝑅𝑆(W5,T)=𝑡%,(𝑀𝑅𝑆(WX5,T)=𝑡),%𝑀𝑅𝑆(W5,TX)			[A]
and thus, the MRS at (𝑥V,𝑧) is different from the MRS at (𝑥V,𝑧) and (𝑥V,𝑧̃) since there does not
exist a real constant 𝑐=𝑀𝑅𝑆(W5,T)=𝑀𝑅𝑆(WX5,T)=𝑀𝑅𝑆(W5,TX) that satisfies expression [A] when 𝜂≠
1 or 𝜃≠1. Now, consider now the special case of 𝜂=1 and 𝜃=1, and it follows that:
𝑢(𝑡𝒙;𝑡,%𝑧)=(𝑡%𝑡,%)𝑢(𝒙;𝑧)=𝑢(𝒙;𝑧)
Next, let 𝒙=𝑡𝒙 and 𝑧̃=𝑡,%𝑧, and differentiating by 𝑥V finds:

 38
𝜕𝑢(𝑡𝒙;𝑡,%𝑧)
𝜕𝑥V
𝜕𝑥V
𝜕𝑥V
=𝜕𝑢(𝒙;𝑧) 𝜕𝑥V ⇒𝑡𝜕𝑢(𝒙;𝑡,%𝑧) 𝜕𝑥V =𝜕𝑢(𝒙;𝑧) 𝜕𝑥V .
Similarly, differentiating by 𝑧 finds:
𝜕𝑢(𝑡𝒙;𝑡,%𝑧)
𝜕𝑧̃
𝜕𝑧̃%
𝜕𝑧=𝜕𝑢(𝒙;𝑧) 𝜕𝑧 ⇒𝑡,%𝜕𝑢(𝑡𝒙;𝑡,%𝑧) 𝜕𝑧̃ =𝜕𝑢(𝒙;𝑧) 𝜕𝑧 .
Taking the ratios, we get 𝑡&𝑀𝑅𝑆(WX5,TX)=𝑀𝑅𝑆(W5,T). Q.E.D.

Proof of Corollary 1. A binding budget constraint can be rewritten as 𝑚=∑ 𝑝/𝑥/ # /2% . At the
initial public good provision 𝑚=∑ 𝑝/𝑥/∗# /2%   at 𝑢+ and, similarly, 𝑚=∑ 𝑝/𝑥/∗∗# /2%   at 𝑢%. By
Theorem 1, 𝑡.𝑚=∑ 𝑝/𝑥/ 4# /2%  and 𝑡,.𝑚=∑ 𝑝/𝑥/ 44# /2%  (with 𝜙≡−𝜃𝜂⁄). For compensating
variation, it follows that: 𝐶𝑉=D1−𝑡.F𝑚=𝑚−𝑡.𝑚=∑ 𝑝/𝑥/ ∗# /2% −∑ 𝑝/𝑥/ 4# /2% =
∑ (𝑝/𝑥/ ∗−𝑝/𝑥/ 4)# /2% =∑ 𝑝/(𝑥/ ∗−𝑥/ 4)# /2% =∑ CV/ # /2% .
For equivalent variation, it follows that: 𝐸𝑉=D𝑡,.−1F𝑚=𝑡,.𝑚−𝑚=∑ 𝑝/𝑥/44# /2% −
∑ 𝑝/𝑥/∗∗# /2% =∑ (𝑝/𝑥/44−𝑝/𝑥/∗∗)# /2% =∑ 𝑝/(𝑥/44−𝑥/∗∗)# /2% =∑ EV/ # /2% . Q.E.D.

Proof of Proposition 1. Begin by assuming separability of the utility function and then prove the
property of the expenditure function. To start,
𝑒(𝑢,𝒑;𝒛)=	min{𝒙}	{𝒑∙𝒙∶𝑢(𝒙;𝒛)≥𝑢} [Definition]
⇔𝑒(𝑢,𝒑;𝒛)=	min{𝒙}	{𝒑∙𝒙∶𝑢%(𝒙)+𝑢&(𝒛)≥𝑢	} [Separability assumption]
⇔𝑒(𝑢,𝒑;𝒛)=	min{𝒙}	{𝒑∙𝒙∶𝑢%(𝒙)≥𝑢−𝑢&(𝒛)	}
⇔𝑒(𝑢,𝒑;𝒛)=𝑒(𝑢−𝑢&(𝒛),𝒑) [Definition].
Then, assume that the expenditure function can be expressed as 𝑒(𝑢,𝒑;𝒛)=𝑒(𝑢−𝑢&(𝒛),𝒑) and
show that the utility function is additively separable in public goods. To start,
𝑒(𝑢−𝑢&(𝒛),𝒑)=	min{𝒙}	{𝒑∙𝒙∶𝑢%(𝒙)≥𝑢−𝑢&(𝒛)	} [Definition]

 39
⇔𝑒(𝑢−𝑢&(𝒛),𝒑)=	min{𝒙}	{𝒑∙𝒙∶𝑢%(𝒙)+𝑢&(𝒛)≥𝑢	}
⇔𝑒(𝑢−𝑢&(𝒛),𝒑)=	min{𝒙}	{𝒑∙𝒙∶𝑢(𝒙;𝒛)≥𝑢	} [Separability definition]. Q.E.D.

Proof of Proposition 2. By Espinosa and Prada (2012)’s Corollary 1 and 2, respectively,
𝑣%(𝑚,𝒑)=𝑚*𝑒(1,𝒑),* and 𝑣%(𝑚,𝒑)=𝑚*𝑣%(1,𝒑), when 𝑢%(𝒙) is homogeneous of degree
𝛾≠0. Then, it follows 𝑣%(1,𝒑)=𝑒(1,𝒑),* and 𝑣%(1,𝒑),%*==𝑒(1,𝒑). Next,
𝑒(𝑢,𝒑;𝒛)=𝑒(𝑢−𝑢&(𝒛),𝒑) [Proposition 1]
⇔𝑒(𝑢,𝒑;𝒛)=𝑒(𝑢,𝒑) [Definition 𝑢=𝑢−𝑢&(𝒛)]
⇔𝑒(𝑢,𝒑;𝒛)=𝑢%*=𝑒(1,𝒑) [Espinosa and Prada (2012)'s Corollary 1]
⇔𝑒(𝑢,𝒑;𝒛)=𝑢%*=𝑣%(1,𝒑),%*= ⇔𝑒(𝑢,𝒑;𝒛)={@,@"(𝒛) D!(𝟏,𝐩)| %*=  [Definition]. Q.E.D.

Appendix B
We assume a homogeneous utility function by letting 𝑔(⋅) be the identity function and provide
results related to indirect utility function and the expenditure function. We also derive the certainty
equivalence of lotteries over public goods.
To start, Proposition B1 shows the relationship between direct and indirect utility under
continuity in our public goods model. Proposition B1 is the only result in this study that does not
utilize a homogeneity assumption and thus applies to both jointly and independently homogeneous
functions.

Proposition B1.  If the utility function is strictly increasing, continuous, and quasiconcave, then
𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑∙𝒙=𝑚}.

 40
Proof of Proposition B1. All proofs for Appendix B appear at the end of this appendix.

 Example B1 below provides closed-form Marshallian demands and an indirect utility
function for a homogeneous utility function. For our examples, let 𝒛=(𝑧%	𝑧&) where the first
subscript indicates that these public goods are subject to the homogeneity assumption and let the
𝒘 vector be empty. Example B1 is not weakly separable (and thus not strongly separable) because
the MRS between the two private goods (𝑥%,𝑥&) is given by MRSW!,W"=T! T" iW! W" j <,% . Example B1
illustrates the “if” statements of Propositions B2a and B2b that follow, since the utility function in
the example is both jointly and independently homogeneous, while the “only if” parts are left for
the reader. Specifically, Propositions B2a and B2b relate the degree of homogeneity of a jointly
and independently homogeneous utility function, respectively, to the indirect utility function.
These if-and-only-if-style propositions demonstrate how maximized utility scales with respect to
exogenous income and the provision of public goods.
Then, Propositions B2c and B2d separately apply each of the necessary condition clauses
of independent homogeneity and doing so leads to Corollary B1 regarding Marshallian demand
with respect to public goods under homogeneity. Specifically, Corollary B1 shows that if a strictly
quasiconcave utility function is homogeneous in only the public goods (𝒛) then Marshallian
demand is homogeneous of degree zero in the public goods, and Example B1 also demonstrates
this property. The utility scaling in Propositions B2a through B2d requires the cardinal properties
of a homogeneous utility function.

Example B1:  Let 𝑢(𝒙;𝒛)=𝑥% <𝑧%+𝑥& <𝑧& and thus 𝑡<"%𝑢(𝒙;𝒛)=𝑢(𝑡𝒙;𝑡𝒛); that is, 𝑢(𝒙;𝒛) is
jointly homogeneous of degree 𝛼+1. This utility function is also independently homogeneous of

 41
degrees 1 and 𝛼 in the vectors 𝒙 and 𝒛, respectively. The first-order conditions of the UMP lead to
W!
W"
={\!T"
\"T!
|
%/(<,%)
≡𝑘(𝒑;𝒛)=𝑘 and restrict 𝛼≠0,1. Note that 𝑘(𝒑;𝑡𝒛)=𝑘(𝒑;𝒛). Next, the
Marshallian demands are 𝑥%(𝑚,𝒑;𝒛)=8^ \!^"\"  and 𝑥&(𝑚,𝒑;𝒛)=8 \!^"\" , and have the properties
𝑡𝑥/(𝑚,𝒑;𝒛)=𝑥/(𝑡𝑚,𝒑;𝑡𝒛) as well as 𝑥/(𝑚,𝒑;𝒛)=𝑥/(𝑚,𝒑;𝑡𝒛) for 𝑛=1,2. Thus, the
indirect utility function has the closed-form solution 𝑣(𝑚,𝒑;𝒛)=(𝑘<𝑧%+𝑧&)i8 \!^"\" j <  and has
the property that 𝑡<"%𝑣(𝑚,𝒑;𝒛)=𝑣(𝑡𝑚,𝒑;𝑡𝒛).

Proposition B2a. The utility function 𝑢(𝒙;𝒛,𝒘) is jointly homogeneous of degree 𝛾 (see
definition in Section 2) if and only if the indirect utility function 𝑣(𝑚,𝒑;𝒛,𝒘) is homogeneous of
degree 𝛾 in income (𝑚) and public goods (𝒛%); that is, 𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘) for all
𝑡>0.

Proposition B2b. The utility function 𝑢(𝒙;𝒛,𝒘) is independently homogeneous (see definition in
Section 2) if and only if the indirect utility function 𝑣(𝑚,𝒑;𝒛,𝒘) is homogeneous of degree 𝜂+𝜃
in income and public goods (𝒛); that is, 𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘) for all 𝑡>0.

Proposition B2c. The utility function 𝑢(𝒙;𝒛,𝒘) is homogeneous in the private goods such that
𝑡(𝑢(𝒙,𝒛,𝒘)=𝑢(𝑡𝒙,𝒛,𝒘) for all 𝑡>0 if and only if 𝑡(𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑡𝑚,𝒑;𝒛,𝒘).

Proposition B2d. The utility function 𝑢(𝒙;𝒛,𝒘) is homogeneous in the public goods (𝒛) such that
𝑡)𝑢(𝒙,𝒛,𝒘)=𝑢(𝒙,𝑡𝒛,𝒘) for all 𝑡>0 if and only if 𝑡)𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑚,𝒑;𝑡𝒛,𝒘).

 42
Corollary B1. If the utility function is homogeneous in the public goods (𝒛), such that
𝑡)𝑢(𝒙,𝒛,𝒘)=𝑢(𝒙,𝑡𝒛,𝒘) for all 𝑡>0 and 𝑢(∙) is strictly quasiconcave, then Marshallian
demands are homogeneous of degree zero in public goods where 𝑥/(𝑚,𝒑;𝒛,𝒘)=𝑥/(𝑚,𝒑;𝑡𝒛,𝒘)
for all 𝑡>0 for all 𝑛=1,…,𝑁.

Next, we explore properties of the expenditure function given a jointly homogeneous utility
function. With an if-and-only-if structure proof, Proposition B3 formalizes Example B1's finding
that relates the utility function's joint degree of homogeneity to scaling utility and the public goods.
Corollary B2 follows directly from Proposition B3 by setting 𝛾=1. Corollary B2 is easy to
interpret: the utility function is jointly homogeneous of degree one, equivalent to assuming
homothetic preferences (Varian, 2002), if and only if the expenditure function is jointly
homogeneous of degree one in utility and public goods. Corollary B2 also proves that Hicksian
demand is homogeneous of degree zero in utility and public goods when the utility function is
strictly quasiconcave. The CES utility function is an important example of a utility function with
homogeneity of degree 1 while noting that CES functions are additively separable in a monotonic
transformation and thus are strongly separable (Deaton and Muellbauer, 1980). In some contexts,
the degree of homogeneity of utility function dictates whether an agent is a risk-taker, risk-neutral,
or risk-averse. Homogeneous utility is also employed in asset pricing models with atemporal, non-
expected utility theories (Epstein and Zin, 1989).

Example B1 (concluded): The utility function 𝑢(𝒙;𝒛)=𝑥% <𝑧%+𝑥& <𝑧& is jointly homogeneous of
degree 𝛼+1 and the expenditure function is 𝑒(𝑢,𝒑;𝒛)=(𝑘𝑝%+𝑝&){ @ ^6T!"T" | %/<  with the
property 𝑡𝑒(𝑢,𝒑;𝒛)=𝑒(𝑡<"%𝑢,𝒑;𝑡𝒛).

 43
Proposition B3. The utility function 𝑢(𝒙;𝒛,𝒘) is jointly homogeneous of degree 𝛾 if and only if
the expenditure function 𝑒(𝑢,𝒑;𝒛,𝒘) satisfies the following property: 𝑡𝑒(𝑢,𝒑;𝒛,𝒘)=
𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑡>0.

Corollary B2. The utility function 𝑢(𝒙;𝒛,𝒘) is jointly homogeneous of degree 1 in 𝒙 and 𝒛 if and
only if the expenditure function 𝑒(𝑢,𝒑;𝒛,𝒘) is homogeneous of degree 1 in utility and public
goods; that is, 𝑡𝑒(𝑢,𝒑;𝒛,𝒘)=𝑒(𝑡𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑡>0. Furthermore, if the utility function is
jointly homogeneous of degree 1 and 𝑢(∙) is strictly quasiconcave, then the Hicksian demand is
homogeneous of degree 0 such that 𝑥/ 0(𝑢,𝒑;𝒛,𝒘)=𝑥/ 0(𝑡𝑢,𝒑;𝑡𝒛,𝒘) for all 𝑡>0 for all 𝑛=
1,…,𝑁.

We conclude the analysis of homogeneous utility by deriving the certainty equivalence
(𝐶𝐸) of lotteries over public goods and thus provide a measure of the curvature of 𝑢(∙) related to
the preferences parameters 𝜃 and 𝜂.
To begin, we express the certainty equivalence as 𝐶𝐸=(1−𝑟)𝑚, where 𝑟>0 is the risk
premium expressed as a percentage of income. Let 𝒛 be the amount of the public goods that the
consumer has with certainty. The lottery occurs over two possible outcomes 𝒛_ and 𝒛‘. Let the
“low” outcome be given by 𝒛_≡ 𝛿_𝒛 with 𝛿_∈[0,1) and the “high” outcome be given by 𝒛‘≡
𝛿‘𝒛 with 𝛿‘∈(1,∞) such that 𝒛_<𝒛<𝒛‘. Also, let the probabilities assigned to 𝒛_ and 𝒛‘ be
denoted 𝑤 and 1−𝑤, respectively, with 𝑤∈[0,1].
The goal is then to find 𝑟>0 associated with 𝒛 and thus the 𝐶𝐸 expression written in terms
of the indirect utility function is as follows:

 44
𝑣D(1−𝑟)𝑚,𝒑;𝒛,𝒘F=𝑤𝑣(𝑚,𝒑;𝒛_,𝒘)+(1−𝑤)𝑣(𝑚,𝒑;𝒛‘,𝒘) (B1)
and we proceed by applying the definitions and then Propositions B2c and B2d to the left-hand
and right-hand sides, respectively, of equation ( B1) under the assumption of independent
homogeneity. After cancelling 𝑣(𝑚,𝒑;𝒛,𝒘) from both sides and rearranging, we find an
expression for 𝑟 that is then substituted into the certainty equivalence definition to yield:
𝐶𝐸=£𝑤𝛿_ )+(1−𝑤)𝛿‘ )⁄%(⁄ 𝑚 (B2)
where 𝐶𝐸 is positive.
Regarding the comparative statics in equation (B2) assuming 𝜃>0 and 𝜂>0, we find
that 𝐶𝐸 is increasing in income (𝑚), the probability of the low outcome (𝑤), the value of the low
outcome (𝛿_), the value of the high outcome (𝛿‘), and the public good preference parameter (𝜃).
The 𝐶𝐸 is increasing in 𝜃 since a high value for public goods means the consumer place a premium
on securing their provision of public goods. Meanwhile, 𝐶𝐸 is decreasing in private good
preference parameter (𝜂) and this occurs because the more a consumer values the utility from
private goods then the less the consumer is willing to pay to avoid the lottery for the public goods.
That is, we find opposite effects of 𝜃 and 𝜂 on the certainty equivalence and this finding
foreshadows results in subsequent sections under homothetic utility. However, the 𝐶𝐸 expression
in equation (B2) does not extend to homothetic utility since Propositions B2c and B2d only hold
for homogeneous utility functions.

Proof of Proposition B1. Fix 𝒛  and 𝒘, then let 𝑢(𝒙)=𝑢(𝒙;𝒛,𝒘). Then, the function 𝑢(⋅) is
strictly increasing in 𝒙 and it follows that the upper contour level sets of 𝑢	are convex (since 𝑢(⋅)

 45
is continuous and quasiconcave function). Then, 𝑢(⋅) satisfies conditions C.2 and C.3 from
Espinosa and Prada (2012) and thus,
𝑢(𝒙)=min𝑝{𝑣	(𝑚,𝒑):𝒑∙𝒙=𝑚} [Definition, Proposition 2: Espinosa and Prada (2012)]
where 	𝑣	(𝑚,𝒑)=max𝒙{𝑢(𝒙):𝒑∙𝒙=𝑚} [Definition]
⇔𝑣	&(𝑚,𝒑)=max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑∙𝒙=𝑚} [Since	𝑢(𝒙)=𝑢(𝒙;𝒛)]
⇔𝑣	&(𝑚,𝒑)=𝑣(𝑚,𝒑;𝒛,𝒘) [Definition]
⇔	𝑢(𝒙;𝒛,𝒘)=min#{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑∙𝒙=𝑚} [Definition]. Q.E.D.

Proof of Proposition B2a. Begin by assuming that the utility function is homogeneous of degree
𝛾 and show that the indirect utility function is homogeneous of degree 𝛾 in income and public
goods. To start, 𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Definition]
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=𝑡*max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚}
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑡*𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚}
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑢(𝑡𝒙;𝑡𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Assumption]
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙J𝑢(𝒙;𝑡𝒛,𝒘):𝒑⋅i% G𝒙j≤𝑚 [Unit conversion : 𝒙=𝑡𝒙]
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙J{𝑢(𝒙;𝑡𝒛,𝒘):𝒑⋅𝒙≤𝑡𝑚}
⇔𝑡*𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘) [Definition].
Next, assume that the indirect utility function is homogeneous of degree 𝛾 in income and
public goods and show that the utility function is homogeneous of degree 𝛾. Start with the result
from Proposition B1 and proceed as follows:
𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚} [Proposition B1]
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=𝑡*min𝒑{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚}
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑡*𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚}

 46
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘):𝒑⋅𝒙=𝑚} [Assumption]
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=min𝒑𝑡+𝑣i𝑚,% G𝒑;𝑡𝒛,𝒘j:𝒑⋅𝒙=𝑚 [Indirect utility homogeneous of
degree zero in prices and income]
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=min𝒑J{𝑣(𝑚,𝒑;𝑡𝒛,𝒘):𝑡𝒑⋅𝒙=𝑚} [Unit conversion such that 𝒑=% G𝒑]
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=min𝒑J{𝑣(𝑚,𝒑;𝑡𝒛,𝒘):𝒑⋅𝑡𝒙=𝑚}
⇔𝑡*𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝑡𝒛,𝒘) [Proposition A1]. Q.E.D.

Proof of Proposition B2b. Begin by assuming that the utility function is independently
homogeneous and show that the indirect utility function is homogeneous of degree 𝜃 in income
and public goods. To start, 𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Definition]
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=𝑡(")max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚}
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=𝑡(𝑡)max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚}
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙~𝑡(𝑡)𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑢(𝑡𝒙;𝑡𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Assumption]
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙J𝑢(𝒙;𝑡𝒛,𝒘):𝒑⋅i% G𝒙j≤𝑚 [Unit conversion : 𝒙=𝑡𝒙]
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙J{𝑢(𝒙;𝑡𝒛,𝒘):𝒑⋅𝒙≤𝑡𝑚}
⇔𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘)=𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘) [Definition].
Next, assume that the indirect utility function is homogeneous of degree 𝜂+𝜃 in income
and public goods vector 𝒛 and show that the utility function is homogeneous of degree 𝜂+𝜃. Start
with the result from Proposition B1 and proceed as follows:
𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚} [Proposition B1]
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=𝑡(")min𝒑{𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚}

 47
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=min𝒑~𝑡(")𝑣(𝑚,𝒑;𝒛,𝒘):𝒑⋅𝒙=𝑚
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=min𝒑{𝑣(𝑡𝑚,𝒑;𝑡𝒛,𝒘):𝒑⋅𝒙=𝑚} [Assumption]
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=min𝒑𝑡+𝑣i𝑚,% G𝒑;𝑡𝒛,𝒘j:𝒑⋅𝒙=𝑚 [Indirect utility homogeneous of
degree zero in prices and income]
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=min𝒑J{𝑣(𝑚,𝒑;𝑡𝒛,𝒘):𝑡𝒑⋅𝒙=𝑚} [Unit conversion such that 𝒑=% G𝒑]
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=min𝒑J{𝑣(𝑚,𝒑;𝑡𝒛,𝒘):𝒑⋅𝑡𝒙=𝑚}
⇔𝑡(")𝑢(𝒙;𝒛,𝒘)=𝑢(𝑡𝒙;𝑡𝒛,𝒘) [Proposition B1]. Q.E.D.

Proof of Proposition B2c. Follow Proof of Proposition B2b and simplify.

Proof of Proposition B2d. Follow Proof of Proposition B2b and simplify.

Proof of Corollary B1. Defined 𝒙∗ to be the maximizer of max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑∙𝒙	≤𝑚}, and
similarly, define 𝒙4 to be the maximizer of max𝒙{𝑢(𝒙;𝑡𝒛,𝒘):𝒑∙𝒙	≤𝑚}. Then,
𝑣(𝑚,𝒑;𝒛,𝒘)=max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Definition]
⇔𝑣(𝑚,𝒑;𝑡𝒛,𝒘)=max𝒙{𝑢(𝒙;𝑡𝒛,𝒘):𝒑⋅𝒙≤𝑚}
⇔𝑣(𝑚,𝒑;𝑡𝒛,𝒘)=max𝒙~𝑡)𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚 [Assumption]
⇔𝑣(𝑚,𝒑;𝑡𝒛,𝒘)=𝑡)max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Max operator property]
⇔max𝒙{𝑢(𝒙;𝑡𝒛,𝒘):𝒑∙𝒙	≤𝑚}=𝑡)max𝒙{𝑢(𝒙;𝒛,𝒘):𝒑⋅𝒙≤𝑚} [Definition]
and therefore 𝒙4=𝒙∗ since scaling an objective function by 𝑡) does not affect the maximizer and
the maximizers are unique by strict quasiconcavity. Alternatively, assuming a differentiable

 48
indirect utility function, this corollary can be proven by differentiating the indirect utility function
and applying Roy's Identity. Q.E.D.

Proof of Proposition B3. Begin by assuming homogeneity of the utility function and then prove
the scaling property of the expenditure function.  Then,
𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙{𝒑⋅𝒙:𝑢(𝒙;𝑡𝒛,𝒘)≥𝑡*𝑢} [Definition]
⇔𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑡*𝑢i% G𝒙;𝒛,𝒘j≥𝑡*𝑢 [Homogeneity of 𝑢(∙)]
⇔𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙𝒑⋅𝒙:𝑢i% G𝒙;𝒛,𝒘j≥𝑢 [Divide constraint by 𝑡*>0]
⇔𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=min𝒙J{𝒑⋅𝑡𝒙:𝑢(𝒙;𝒛,𝒘)≥𝑢} [Unit conversion: 𝒙=% G𝒙]
⇔𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=𝑡min𝒙J{𝒑⋅𝒙:𝑢(𝒙;𝒛,𝒘)≥𝑢}
⇔𝑒(𝑡*𝑢,𝒑;𝑡𝒛,𝒘)=𝑡𝑒(𝑢,𝒑;𝒛%,𝒛&) [Definition].
Next, assume the scaling property of the expenditure function and show the utility function
property. Neary and Roberts (1980) show 𝑢=𝑣(𝑒(𝑢,𝒑;𝒛),𝒑;𝒛), we omit 𝒑 for notational
simplicity; that is, 𝑢=𝑣(𝑒(𝑢;𝒛);𝒛). In our model,
𝑣(𝑚;𝒛,𝒘)=	𝑣(𝑒(𝑢;𝒛,𝒘);𝒛,𝒘) [Identity: 𝑚=𝑒(𝑢;𝒛,𝒘)]
⇔𝑣(𝑡𝑚;𝑡𝒛,𝒘)=𝑣(𝑡𝑒(𝑢;𝒛,𝒘);𝑡𝒛,𝒘)
⇔𝑣(𝑡𝑚;𝑡𝒛,𝒘)=𝑣(𝑒(𝑡*𝑢;𝑡𝒛,𝒘);𝑡𝒛,𝒘) [By assumption 𝑡𝑒(𝑢;𝒛,𝒘)=𝑒(𝑡*𝑢;𝑡𝒛,𝒘)]
⇔𝑣(𝑡𝑚;𝑡𝒛,𝒘)=𝑡*𝑢 [Identity:	𝑢=𝑣(𝑒(𝑢;𝒛,𝒘);𝒛,𝒘), so 𝑣(𝑒(𝑡*𝑢;𝑡𝒛,𝒘);𝑡𝒛,𝒘)= 𝑡*𝑢 by
Proposition B2a.]
⇔𝑣(𝑡𝑚;𝑡𝒛,𝒘)=𝑡*𝑣(𝑚;𝒛,𝒘) [Identity: 𝑢=𝑣(𝑚;𝒛,𝒘)].
Thus, 𝑣(∙) is homogeneous of degree 𝛾 in income and public goods and therefore by Proposition
B2a, 𝑢(∙) is homogeneous of degree 𝛾. Q.E.D.

 49
Proof of Corollary B2. Start with Proposition B3 and set 𝛾=1. Define 𝒙∗ to be the minimizer of
min𝒙{𝒑⋅𝒙:𝑢(𝒙;𝒛,𝒘)≥𝑢}, and similarly, define 𝒙4 to be the minimizer of min𝒙{𝒑⋅
𝒙:𝑢(𝒙;𝑡𝒛,𝒘)≥𝑡𝑢}. Then,
𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙{𝒑⋅𝒙:𝑢(𝒙;𝒛,𝒘)≥𝑢} [Definition]
⇔𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙{𝒑⋅𝒙:𝑡𝑢(𝒙;𝒛,𝒘)≥𝑡𝑢}
⇔𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙{𝒑⋅𝒙:𝑢(𝑡𝒙;𝑡𝒛,𝒘)≥𝑡𝑢}	 [Assumption: Joint Homogeneity of degree 1
in 𝑢(∙)]
⇔𝑒(𝑢,𝒑;𝒛,𝒘)=min𝒙J{𝒑⋅𝑡,%𝒙:𝑢(𝒙;𝑡𝒛,𝒘)≥𝑡𝑢} [Unit conversion: 𝒙=𝑡𝒙]
⇔𝑒(𝑢,𝒑;𝒛,𝒘)=𝑡,%min𝒙J{𝒑⋅𝒙:𝑢(𝒙;𝑡𝒛,𝒘)≥𝑡𝑢} [Min Operator Property]
⇔min𝒙{𝒑⋅𝒙:𝑢(𝒙;𝒛,𝒘)≥𝑢}=𝑡,%min𝒙J{𝒑⋅𝒙:𝑢(𝒙;𝑡𝒛,𝒘)≥𝑡𝑢} [Definition]
and therefore 𝒙∗=𝒙4 since scaling an objective function by 𝑡,% does not affect the minimizer and
the minimizers are unique by strict quasiconcavity. Alternatively, assuming a differentiable
expenditure function, this corollary can be proven by differentiating the expenditure function and
applying Shepard's Lemma. Q.E.D.
