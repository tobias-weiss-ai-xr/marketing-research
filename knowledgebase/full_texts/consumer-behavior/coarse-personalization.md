---
title: Coarse Personalization
url: https://doi.org/10.1145/3670865.3673540
category: consumer-behavior
subcategory: empirical
date: 2024-07
venue: ''
authors:
- Walter W. Zhang
- Sanjog Misra
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2204.05793
pages: 58
chars: 142984
fetched_at: '2026-11-08T17:08:23+00:00'
kb_version: 1
---

# Coarse Personalization

arXiv:2204.05793v4  [econ.EM]  30 Jun 2025
Coarse Personalization∗
Walter W. Zhang
The Wharton School, University of Pennsylvania
Sanjog Misra
University of Chicago Booth School of Business
June 30, 2025
Abstract
With advances in estimating heterogeneous treatment effects, firms can personalize and
target individuals at a granular level. However, feasibility constraints limit full personal-
ization. In practice, firms choose segments of individuals and assign a treatment to each
segment to maximize profits: We call this the coarse personalization problem. We propose a
two-step solution that simultaneously makes segmentation and targeting decisions. First, the
firm personalizes by estimating conditional average treatment effects. Second, the firm dis-
cretizes using treatment effects to choose which treatments to offer and their segments. We
show that a combination of available machine learning tools for estimating heterogeneous
treatment effects and a novel application of optimal transport methods provides a viable and
efficient solution. With data from a large-scale field experiment in promotions management,
we find our methodology outperforms extant approaches that segment on consumer char-
acteristics, consumer preferences, or those that only search over a prespecified grid. Using
our procedure, the firm recoups over 99.5% of its expected incremental profits under full
personalization while offering only five segments. We conclude by discussing how coarse
personalization arises in other domains.
Keywords: Personalization, Targeting, Segmentation, Optimal Transport, Machine Learning
∗Zhang: wwz@wharton.upenn.edu, Misra: sanjog.misra@chicagobooth.edu; We thank the data science and an-
alytics team at the company that is the source of our data for their help and numerous insights. We are grateful
for the discussions, comments, and suggestions of conference participants at Marketing Science 2021, TADC 2021,
MLESI 2022, QME 2022, ICSDS 2023, and EC 2024.

1 Introduction
Improvements in estimating heterogeneous treatment effects enable firms to target customers on
an almost individual level. Leveraging state-of-the-art machine learning techniques, firms can
fully personalize; individual customers with a unique set of covariates can form their own seg-
ment.1 Full personalization involves both tailoring the marketing mix for each customer and tar-
geting only customers who generate positive incremental profits for the firm. Consequently, full
personalization is profit-maximizing because individuals are targeted only when their marginal
benefit of targeting outweighs their marginal cost.
However, in practice, firms face barriers implementing these personalization and targeting
procedures. First, firms are concerned about the cost: As an example, if a small firm sends
an identical email to 25,000 customers using an email marketing platform (e.g., MailChimp), it
would need to spend tens of dollars. If that same firm were to send fully personalized mes-
sages, it would need to spend a few thousand dollars—that is, two orders of magnitude more.
Second, firms face the potential for unstable estimates: Firms using complex machine learning
methods may be concerned that estimated treatment effects are noisy and their personalization
models could be hindered by variance. Finally, firms are concerned about downstream fairness
or inequity complaints: As another consequence of noisy estimates, two similar customers may
receive significantly different sets of marketing mix variables.
More generally, full personalization is limited when there are menu costs (Sheshinski and
Weiss, 1977), concerns about the personalization model’s stability (Hitsch et al., 2024), and issues
pertaining to inequity or fairness (Kahneman et al., 1986). The trade press often points to the
complexities of implementing personalized policies with particular focus on the high costs of
setting up the infrastructure to conduct such personalization.2
With these constraints, it is not surprising that firms restrict the set of unique marketing
mix variables, or treatments, to offer. Consequently, firms must decide to which customers they
will assign these treatments. In essence, firms create smaller sets, or segments, of customers and
optimally choose treatments for each set with the aim of maximizing profits. We call this problem
the coarse personalization problem.
The coarse personalization problem is not entirely new. The marketing literature has long
1In one-to-one marketing, a firm’s marketing mix is tailored to each individual (Arora et al., 2008). Personal-
ization based on heterogeneous treatment effects provides a modern implementation that approximates one-to-one
marketing using a high-dimensional vector of individual characteristics. If the set of covariates is relevant and large
enough, the two approaches will coincide.
2Harvard Business Review Analytic Services (2018) notes that firms are rapidly trying to fully personalize their
content, but continue to face implementation costs in doing so. Managers are selectively choosing which products
to personalize, as firms compete with one another to provide the best personalized experiences for their customers.
Gilmore and Pine (1997) observe that it is infeasible for many firms to offer mass customization because of imple-
mentation costs and suggest that managers should selectively choose which options to offer.
1

understood the need to segment consumers with the idea of personalizing the marketing mix for
each segment while keeping costs within bounds. The typical process is sequential: Marketers
first group customers into segments and then personalize marketing mix treatments for the tar-
geted segments. Indeed, the textbook approach is to implement a “discretize then personalize”
framework where they form customer segments based on some predefined source of customer
heterogeneity, identify which segments they wish to target, and then tailor marketing mix vari-
ables for those segments (Kotler and Keller, 2014). Over time, the sources of customer hetero-
geneity that underpin the segmentation procedure have evolved. Initially, marketing researchers
proposed forming segments on demographic and psychographic variables (Smith, 1956; Wind,
1978; Gupta and Chintagunta, 1994). More recently, researchers have formed segments based on
estimated consumer preferences and responses (Kamakura and Russell, 1989; Bucklin and Gupta,
1992; Krieger and Green, 1996; Bucklin et al., 1998) via either continuous or discrete mixtures
(Grover and Srinivasan, 1987; Jain et al., 1990).
In practice, the “discretize then personalize” framework is broadly used in marketing, espe-
cially in customer relationship management (CRM), database marketing, and direct marketing,
where marketers first form segments before making targeting decisions. While the literature has
evolved considerably in terms of the information it uses, the structure of the framework and the
sequence of steps have essentially remained the same.
In this paper, we show that implementing these steps sequentially is not necessarily profit
maximizing: The initial segmentation procedure is based on a distance metric that is statistical
(e.g., Euclidean) rather than economic in nature (e.g., based on profit maximization). To address
this problem, we recharacterize the coarse personalization problem as an optimal transport prob-
lem and derive a theoretically rigorous yet practically implementable solution. In doing so, we
draw on modern techniques from both the incrementality-based targeting literature and the op-
timal transport literature. In particular, we advocate for a “personalize then discretize” approach
where we first construct personalized policies based on heterogeneous treatment effects obtained
using now widely available machine learning tools, and in asecond step, we use these policies to
construct segments of consumers by minimizing profit regret. Crucially, in the second step we
simultaneously determine each segment’s optimal treatment and customer assignment to maxi-
mize profits. Put simply, this approach inverts the “discretize then personalize” approach by first
searching for what works for each customer and then deciding on a coarsened marketing mix
offering that would not significantly degrade profits relative to full personalization.
Our two-step framework solves the coarse personalization problem precisely because it is able
to segment consumers based on a profit-relevant distance metric. As such, we view our key con-
tribution to be the design of the second step that allows for the construction and implementation
of this solution. The first step’s machine learning-based personalization, done by exploiting het-
2

erogeneous treatment effects, is now relatively straightforward from the literature. On the other
hand, the issue of coarsening these to satisfy the problem is novel and poses challenges on mul-
tiple fronts. The combinatorial nature of the assignment problem coupled with the optimization
of the treatment policy makes the problem especially difficult.
Our proposed solution coarsens the personalization policy to account for the constraint that
policy space is limited to a finite number of segments. We use optimal transport methods that
minimize the regret between the profits that accrue from the full personalization solution to
those from any proposed coarsened solution. The regret minimizing solution guarantees that we
attain the highest possible profits while incorporating the additional constraint on the number of
segments available.
To be clear, while one might be able to solve the coarse personalization problem by brute
force, the complexity of the problem is exponential in the number of people and suffers from
the curse of dimensionality. Instead, we propose a computational solution that adapts Lloyd’s
Algorithm (Lloyd, 1982) and leverages the convexity of the problem. Our algorithm is scalable
and provides a transparent visualization of the solution’s procedure.
In our empirical application, we use data from a food delivery platform experimenting with its
promotions management. We find that our solution significantly outperforms traditional market-
ing procedures that sequentially segment on demographics, RFM variables, and consumer pref-
erences in generating profits. Further, we find that if the firm issues only five unique optimized
treatments, our solution recovers over 99.5% of the full personalization’s expected incremental
profits. These results illustrate the extent to which our “personalize then discretize” approach
outperforms the traditional “discretize then personalize” approach.
Substantively, our solution lets us interpolate between no personalization to full personal-
ization and evaluate the surplus at each level of personalization. While full personalization is
well-studied in the literature, the gap between full personalization and blanket targeting is not.3
Using our framework, we empirically document the impact personalization has on consumer and
producer surplus. Coarser personalization reduces producer surplus due to the extra constraint
on the firm’s optimization, but it can boost consumer surplus for some individuals by assigning
them treatment levels that differ from those under full personalization. We document that the
impact of personalization on consumer welfare is ambiguous in our application.
Lastly, we discuss how the coarse personalization problem naturally arises in other marketing
settings. In salesforce contract design, managers need to determine which geographic blocks for
salespeople to exert effort in, how much time to allocate, and whether to call or visit in person.
3The literature is divided on how personalization affects surplus. Bergemann and Bonatti (2011) theoretically
show as firms personalize more granularly, both producer surplus and total surplus increase. Dubé and Misra (2022)
empirically find that consumer surplus changes nonmonotonically as firms personalize more granularly in their
application.
3

Advertising designers need to choose which set of advertisements to send out to their customer
base. Pricing managers can choose to use nudges or price subsidies to influence consumer be-
havior. All of these marketing problems can be tackled with our framework.
Our application contributes to the promotions management literature. Traditionally, price
promotions are personalized based on customer heterogeneity (Rossi et al., 1996; Shaffer and
Zhang, 1995). With the advent of online marketplaces, promotions are more readily personal-
ized, customized, and distributed to customers (Ansari and Mela, 2003; Zhang and Krishnamurthi,
2004). The optimization angle to promotions management has been explored in the literature
(Duvvuri et al., 2007; Zhang and Wedel, 2009), but promotions are only optimized after first form-
ing segments. Most recently, marketers have used tools from causal machine learning to target
and personalize promotions based on customers’ heterogeneous treatment effects (Ascarza, 2018;
Simester et al., 2020; Rafieian and Yoganarasimhan, 2021; Ellickson et al., 2022; Yoganarasimhan
et al., 2022; Zhang, 2023; Hitsch et al., 2024). The operations management literature has looked
at optimal segmentation strategies without fully considering the causal impact of the marketing
mix (Cui and Hamilton, 2022; Aouad et al., 2023). Our framework integrates the classical opti-
mization approach with modern techniques leveraging heterogeneous treatment effects. We also
provide a framework for incrementality-based personalization for vector treatments, which, to
our knowledge, has not been explored in the marketing literature. To summarize the contribu-
tions of this paper, we have (1) highlighted the problem of optimal coarsening and (2) examined
this problem for multiple interconnected treatments that create methodological challenges, and
(3) provided a solution via optimal transport.
Our paper additionally provides a novel application of the optimal transport literature to the
marketing literature. Optimal transport problems have been applied to discrete choice models
under the mass transport framework (Chiong et al., 2016; Bonnet et al., 2017), matching markets
(Galichon and Salanie, 2012), quantile regression (Carlier et al., 2016), and bounding regression
discontinuity design estimates (Daljord et al., 2019); its general applications to economics are
surveyed in (Galichon, 2016). Computational methods for evaluating optimal transport problems
are detailed in (Peyré and Cuturi, 2019), and a survey of recent mathematical developments in
the field can be found in Villani (2009).
Section 2 overviews the proposed methodology. Section 3 formally presents our coarse per-
sonalization solution: the personalization in the first step is described in Section 3.1 and the dis-
cretization in the second step is detailed in Section 3.2. Our computational solution that adapts
Lloyd’s Algorithm is described in Section 4 and its comparison to standard brute-force grid search
is provided in Section 4.2. We then discuss why using optimal transport is effective for coarse
personalization in Section 5. We apply our methodology to an empirical application for promo-
tions management for a large food delivery firm in Section 6. The surplus analysis is discussed
4

in Section 7. We discuss how our framework can be adapted to address other classic marketing
problems in Section 8.
2 Methodological overview
Simply put, marketers maximize profits by simultaneously forming segments and choosing the
segments’ marketing mix. We first demonstrate that our “personalize then discretize” approach
yields higher profits compared to the classical approaches that “discretize then personalize, ” where
segments and their assigned marketing mix, or treatments, are selected sequentially rather than
simultaneously. Then, we demonstrate that solving the two components simultaneously is diffi-
cult in practice, which motivates our recasting of the problem in an optimal transport framework.
Intuitively, the simultaneous approach yields higher profits than the sequential one because
both segmentation and targeting rules are chosen jointly. To demonstrate this idea, we work
through the following stylized example.
We first denote individuals’ covariates as 𝒙𝑖, the segmentation rule that assigns individu-
als to segments as 𝑆(𝒙𝑖), and the function that maps segments to their assigned treatment as
𝑇(𝑆(𝒙𝑖), 𝒙𝑖).
The classical sequential approach forms segments a priori based on consumer characteristics
and preferences (Kotler and Keller, 2014). We denote a priori segmentation rule as 𝑆0(𝒙𝑖). After
segments are formed, the marketer then solves for the optimal treatment values𝑇(𝑆0(𝒙𝑖), 𝒙𝑖) by
taking the a priori segmentation as given.
In contrast, our approach solves the two problems simultaneously. We define profits as
Π(𝑆(𝒙𝑖),𝑇(𝒙𝑖,𝑆)). Our solution simultaneously solves for the segmentation rule𝑆(x𝑖) and chooses
treatments by𝑇(𝑆(𝒙𝑖), 𝒙𝑖) to maximize profits. We now show the simultaneous approach yields
higher profits,
max
𝑆,𝑇
Π(𝑆,𝑇(𝑆))
|             {z             }
Simultaneous approach profits
≥ max
𝑇
Π(𝑆0,𝑇(𝑆0))
|                {z                }
Sequential approach profits
(1)
where we suppressed the dependence on 𝒙𝑖 in our notation. The left-hand side in Equation 1
represents profits from the simultaneous approach where the profits are maximized to both ar-
guments. The right-hand side represents the sequential approach where treatments are chosen
only after segments𝑆0 are formed.
The inequality holds by the property of the maximization operator over 𝑆, and it will bind
if and only if the a priori segmentation is ex post optimal for profit maximization. 4 Hence, the
simultaneous approach will be an upper bound in profits for any sequential segmentation pro-
4Specifically, only if𝑆0(x𝑖)∈ argmax𝑆′ max𝑇 Π(𝑆′(x𝑖),𝑇(𝑆′(x𝑖))) .
5

cedure. In our empirical application, we validate this intuition by evaluating our simultaneous
approach to different sequential benchmarks.
While our simultaneous approach is analytically more profitable, in practice solving it is quite
difficult. As an example, forming three segments for fifteen individuals, each segment receiv-
ing a promotion from ten possible dollar-off or percentage-off values, yields a total of 10×2 3 315
combinations, which is over 16 billion combinations. Even in this stylized example, we see that
the search space is combinatorially large. For modern digital marketing applications with many
treatment arms that are issued to millions of customers, it only gets more complex.
Modern approaches attempt to solve the problem by testing each discrete treatment arm in
an A/B test, evaluating its heterogeneous treatment effects, and forming segments among the
extant treatment arms to maximize profits (Hitsch et al., 2024). Policy learning methods can di-
rectly learn the most profitable treatment to offer from the experiment. In our running example,
we have ten different promotional values tested by the firm for both dollar and percentage off
promotions. Effectively, we have twenty treatment arms for heterogeneous treatment effects
estimation or policy learning. Segments are then formed by assigning individuals to their best
profit-maximizing treatment arm by either using heterogeneous treatment effects or policy learn-
ing.
However, in both of these approaches, the continuity of the treatment variables is ignored. In
our application, this means the dollar off and percentage off promotions are treated as discrete
instead of as continuous. Ignoring the continuity of the treatments has two implications: First,
the choice of which segments to offer is still combinatorially large and suffers from the curse of
dimensionality. In our running example, to offer three segments, the marketer needs to search
over 10×2 3  = 1, 140 combinations. Second, many marketing mix variables, such as price, promo-
tional value, and product attributes, are fundamentally continuous. When a firm only looks at
discrete values, it forgoes possible profits by ignoring values between those from the experiment.
We benchmark these approaches in our empirical application and document the loss in profits by
ignoring the continuity of the treatment effects.
To mitigate the complexity of the problem, we leverage tools from optimal transport and
convex analysis to provide a scalable solution with continuous treatments. We show that (1)
the segmentation problem can be written as a semidiscrete optimal transport problem, where we
map individuals to segments, and (2) the problem is convex in the treatment values. These results
ensures our computational solution adequately solves the problem.
However, we make two conventional assumptions to ensure the problem is tractable. First,
we assume that individuals have diminishing sensitivity in each type of treatment—i.e., people
are less sensitive to changes at higher promotional values. Second, we assume the firm’s cost
function for issuing larger promotions has no economies of scale—i.e., the firm does not have
6

lower marginal cost at higher promotional values. These two assumptions afford us the convexity
of the problem and ensure each individual is deterministically assigned to a segment. In the next
section, we provide details of our methodology.
3 Model
We solve the coarse personalization problem in two steps. The first estimates treatment effects
from a randomized controlled trial (RCT). The second chooses which treatments to offer and their
segmentation rule using an optimal transport framework. The first step is described in Section
3.1 and the second step is detailed in Section 3.2. We emphasize that the second step is a novel
application of optimal transport, and the first step is presently used for full personalization. We
provide an overview of the mathematics behind the second step in Appendix Section A.
At a high level, the firm chooses to offer𝐿 segments that are each assigned to a unique treat-
ment. The assigned treatments represent a marketing mix variable and are non-zero in only one
dimension𝑑∈{ 1,...,𝐷 } (e.g., only one type of promotion is given to a segment). The coarse per-
sonalization solution solves for profit-maximizing segments by simultaneously finding (1) which
treatments to offer and (2) which individuals𝑖∈{ 1,...,𝑁 } to assign to each treatment.
We now define the notation for our setup. For individual𝑖, we denote the individual charac-
teristics as 𝒙𝑖 and the firm’s outcome measure as𝑌𝑖. Treatments are finite𝐷-dimensional and can
be thought of as marketing mix variables. The treatment vector, for individual𝑖, is denoted as,
𝒕𝑖 =(𝑡𝑖,1,...,𝑡 𝑖,𝑑,...,𝑡 𝑖,𝐷), (2)
where𝑡𝑖,𝑑 is the treatment level in dimension𝑑. If the firm only sends one type of marketing mix
variable, treatments are nonzero in only one dimension and have the format (0,...,𝑡 𝑖,𝑑,..., 0)
where𝑡𝑖,𝑑 ≠ 0. We denote these treatments as feasible.5 A vector of zeros for 𝒕𝑖 represents the no
treatment case. In our empirical application, there are two treatment dimensions—dollar off and
percentage off coupons.
The cost of issuing treatment𝒕𝑖 is𝑐(𝒕𝑖). We define the cost of issuing feasible treatment𝒕𝑖 that
is nonzero in dimension𝑑, or𝑡𝑖,𝑑, as
𝑐𝑑(𝑡𝑖,𝑑)≜𝑐(𝑇1,1 = 0,...,𝑇 𝑖,𝑑 =𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0), (3)
5In our application, feasible treatments implies that each segment receives either a dollar-off coupon (e.g., $2 off)
or a percentage-off coupon (e.g., 5% off), but not both. However, our theoretical results continue to hold if treatments
simultaneously vary across multiple dimensions. Section 8 discusses applications with this generalization.
7

and the cost of not targeting is normalized to be zero, 𝑐𝑑(0) = 𝑐(0) = 0.6 Then, the firm’s
expected return from assigning treatment 𝑡𝑖 to individual 𝑖 is the expected outcome minus the
cost of treatment,
𝐸[R𝑖|𝒙𝑖,𝑡𝑖,1,...,𝑡 𝑖,𝑑,...,𝑡 𝑖,𝐷] =𝐸[𝑌𝑖|𝒙𝑖,𝑡𝑖,1,...,𝑡 𝑖,𝑑,...,𝑡 𝑖,𝐷]− 𝑐(𝒙𝑖,𝑡𝑖,1,...,𝑡 𝑖,𝑑,...,𝑡 𝑖,𝐷). (4)
In the case forfeasible treatment 𝒕𝑖 that is nonzero in dimension𝑑, we have𝐸[R𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 =
𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0] =𝐸[𝑌𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 =𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0]− 𝑐𝑑(𝑡𝑖,𝑑).
3.1 Step 1: Personalize with heterogenous treatment effects
We first estimate continuous, conditional average treatment effect (CATE) functions from the
experiment. This gives us a continuous response surface that we will coarsen in the second step.
The continuous CATEs represent the heterogeneous treatment effects and allow us to construct
the full personalization benchmark.
We consider an RCT setting where the randomization is over the treatment values and di-
mensions. For example, in our empirical application, the RCT in our study has two dimensions of
treatments (dollar off and percentage off promotions), different levels over which the promotions
are randomized, and only one dimension of promotion assigned to each customer in the exper-
iment.7 Formally, we assume that each treatment is randomized between [0, ¯𝑡𝑑], where ¯𝑡𝑑∈ R+
represents the upper bound of the treatment value in each dimension𝑑, and the treatment vector
𝒕𝑖 has domain over[0, ¯𝑡1]×···×[ 0, ¯𝑡𝑑]×···×[ 0, ¯𝑡𝐷].
We can compute the CATEs for each of the treatments relative to the control (or no treatment)
arm under standard assumptions (Imbens and Rubin, 2015). Since our treatments are feasible,
we can compute the continuous CATE separately for each dimension given 𝒙𝑖. We define the
continuous CATE in dimension𝑑 as𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑) for an individual with covariates𝒙𝑖 given treatment
𝑡𝑖,𝑑. Individuals are proxied by their set of covariates 𝒙𝑖.
For each treatment dimension 𝑑 and set of covariates 𝒙𝑖, firms will choose the treatment
level that yields the highest expected profits. We can solve the firm’s problem separately in
each dimension because we prohibit treatments of different dimensions to be simultaneously
administered (feasible treatments).
Without loss of generality, we consider a continuous treatment that is nonzero in dimension
𝑑 or𝑡𝑖,𝑑. The firm will target the customer 𝑖 with treatment𝑡𝑖,𝑑 > 0 if and only if the treatment
6We use capital letters to denote random variables,𝑇𝑖,𝑑, and lowercase letters to denote their realizations,𝑡𝑖,𝑑.
7Each customer in the experiment received a dollar off promotion, a percentage off promotion, or was in the
control group and did not receive a promotion.
8

yields positive incremental expected returns over the no treatment case (𝑡𝑖,𝑑 = 0),
𝐸[R𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 =𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0] >𝐸[R𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 = 0,...,𝑇 𝑖,𝐷 = 0]
𝐸[𝑌𝑖|𝒙𝑖, 0,...,𝑡 𝑖,𝑑,..., 0]− 𝑐𝑑(𝑡𝑖,𝑑) >𝐸[𝑌𝑖|𝒙𝑖, 0,..., 0]
𝐸[𝑌𝑖|𝒙𝑖, 0,...,𝑡 𝑖,𝑑,..., 0]− 𝐸[𝑌𝑖|𝒙𝑖, 0,..., 0] >𝑐𝑑(𝑡𝑖,𝑑)
𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑) >𝑐𝑑(𝑡𝑖,𝑑), (5)
where𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)≜ 𝐸[𝑌𝑖|𝒙𝑖, 0,...,𝑡 𝑖,𝑑,..., 0]− 𝐸[𝑌𝑖|𝒙𝑖, 0,..., 0] is the expected incremental out-
come from issuing treatment 𝑡𝑖,𝑑. The treatment will be administered to an individual with co-
variates 𝒙𝑖 if𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑) >𝑐𝑑(𝑡𝑖,𝑑), or, equivalently, if the continuous CATE is greater than the cost
of treatment.
In each dimension 𝑑 of treatment, the firm chooses the optimal treatment level 𝑡∗ 𝑖,𝑑 for indi-
vidual𝑖 by solving the program,
𝑡∗ 𝑖,𝑑∈ argmax
𝑡𝑖,𝑑∈[0,¯𝑡𝑑]
𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)− 𝑐𝑑(𝑡𝑖,𝑑), (6)
which optimizes the firm’s expected returns over treatment 𝑡𝑖,𝑑 by maximizing the difference
between marginal revenue (𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)) and marginal cost (𝑐𝑑(𝑡𝑖,𝑑)).
The results from the first step provide the firm enough information to fully personalize: For
individual𝑖, the firm assigns treatment𝑡∗ 𝑖,𝑑 that yields the highest return across possible treatments
dimensions ({𝑡∗ 𝑖,𝑑}𝐷 𝑑=1) to do so. We can use off-the-shelf machine learning algorithms to estimate
the continuous CATEs (Athey and Imbens, 2016; Wager and Athey, 2018; Farrell et al., 2020, 2021).
Full personalization represents an upper bound on profits by the principle of maximization
in Equation 6. In our empirical application, we benchmark our coarse personalization solution to
full personalization to quantify lost profits due to coarsening.
3.2 Step 2: Discretize via optimal transport
In the coarse personalization problem, the firm can form at most 𝐿 segments to personalize its
marketing mix for its customers. To effectively account for this constraint, we use tools from
transport theory. In our solution, we need to determine (1) the treatments to offer and (2) the
assignment rule of individuals to their treatment to form segments.
We first introduce some notation to formally define the problem. We denote L as the set of
treatments the firm offers and the cardinality of this set is the number of segments ( |L| = 𝐿).8
8The firm will generally not choose less than 𝐿 unique treatments because it would weakly hinder the firm’s
ability to target more granularly.
9

We assume the number of customers (𝑁 ) is greater than the number of segments (𝐿), i.e.,𝐿 <𝑁 .
Naturally, as𝐿→𝑁 the firm recovers full personalization and when𝐿 = 1 the same treatment is
offered, or blanketed, to all individuals.
The firm then chooses which treatments to offer and which consumers the treatment is as-
signed to. Under the feasible treatment constraint, segment𝑙∈ L is assigned a treatment vector
with structure 𝒕𝑙 =(0,...,𝑡 𝑑,..., 0) that is nonzero in dimension 𝑑∈{ 1,...,𝐷 }. From our first
step in Section 3.1, the firm has already estimated the continuous CATEs, {{𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)}𝐷 𝑑=1}𝑁 𝑖=1,
and optimal treatment levels{{𝑡∗ 𝑖,𝑑}𝐷 𝑑=1}𝑁 𝑖=1 for each individual and dimension of treatment.
We now formulate the firm’s coarse personalization problem as an optimal transport problem
that simultaneously selects customer segments and their corresponding assigned treatments. Ap-
pendix Section A provides an overview of the mathematics behind our optimal transport frame-
work.
We first lay the groundwork for the problem. We define𝑃 as the distribution over the domain
X =[0, ¯𝑡1]×···×[ 0, ¯𝑡𝑑]×···×[ 0, ¯𝑡𝐷]⊂ R𝐷. Individuals are sufficiently represented by their
continuous CATE function, and𝑃 represents the distribution of these continuous CATEs.
We then define ˜t = {˜𝒕1, ˜𝒕2,..., ˜𝒕𝐿} as the 𝐿 assigned treatments for the 𝐿 segments. Each
component of ˜t, denoted as ˜𝒕𝑙, represents the treatment vector assigned to segment 𝑙 and has𝐷
elements. Specifically, ˜t consists of𝐿 points within the domain[0, ¯𝒕1]×···×[ 0, ¯𝒕𝑙]×···×[ 0, ¯𝒕𝐿]⊂
R𝐿𝐷.9
We further define𝑄 ˜t,q as the discrete distribution representing the𝐿 segments. The segments
are assigned treatments˜t and have segment sizes given by the vectorq. Specifically,𝑄 ˜t,q is defined
over the set of𝐿 points that assigns probability mass𝑞𝑙 to each treatment ˜𝑡𝑙 and ˝𝐿 𝑙=1𝑞𝑙 = 1. Here,
𝑞𝑙 represents the relative size of the segment𝑙, and 𝒒 is a vector of segment sizes𝑞𝑙 and has length
𝐿.
Lastly, we define𝜋∈M( 𝑃,𝑄 ˜t,q) to be the assignment rule of individuals to their segment or
the optimal transport plan. Specifically,𝜋 represents the allowable couplings between𝑃 and𝑄 ˜t,q
whereM(𝑃,𝑄 ˜t,q) is the set of possible joint probability distributions. These couplings represent
the mapping between the distributions of treatment effects 𝑃 and segments𝑄 ˜t,q. Substantively,
the couplings are the assignment rule of individuals to their segment.
Figure 1 provides a stylized overview of this problem. To recap the notation, ˜t are the treat-
ments that the firm needs to choose and 𝜋 represents the segmentation rule of individuals of 𝒙𝑖
to their segment. For segment𝑙, it is assigned treatment ˜𝒕𝑙 and has size𝑞𝑙.
9We define ¯𝑡𝑑,∀𝑑 ∈ 𝐷 as the upper bound that a treatment can take in that dimension. We also define ¯𝒕𝑙 =
[¯𝑡1··· ¯𝑡𝐷] to be a vector of dimension𝐷 that represents treatment𝑙’s upper bound in each dimension of treatment.
10

The optimal transport problem is
W( ˜t, q)≜ min
𝜋∈M(𝑃,𝑄 ˜t,q) 𝐸𝜋[𝐶(𝑋,𝑇)] = min 𝜋∈M(𝑃,𝑄 ˜t,q)
𝐿∑︁
𝑙=1
𝑞𝑙𝐸𝜋[𝐶(𝑋,𝑇)|𝑇 = ˜𝒕𝑙], (7)
whereW( ˜t, q) is the objective function at the solution to the optimal transport problem and
𝐶(𝑋,𝑇) is a cost function that will represent profit regret to full personalization.10 This problem
takes as inputs the treatment values ˜t and segment sizes q, and outputs an optimal assignment
rule𝜋 that forms the segments.
The coarse personalization problem is
min
˜𝒕∈R𝐿𝐷,𝒒∈R𝐿
W( ˜t, q)
s.t. 𝒒≥ 0 (non-negative weights)
𝐿∑︁
𝑙=1
𝑞𝑙 = 1 (adding up) (8)
˜𝒕𝑙 takes form(0,..., ˜𝑡𝑑,..., 0) ( feasible treatment)
where the decision variables are the segments’ treatment values ˜t and their sizes q.11
In our framework, the inner problem (Equation 7) is a semidiscrete optimal transport problem
that solves for the optimal assignment rule of individuals, described by their CATEs, to their
segment. The outer minimization problem (Equation 8) chooses the segments’ treatment values
and sizes, specifically the𝐿 unique𝐷-dimensional treatments ˜𝒕 and corresponding segment sizes
𝒒.
To link the optimal transport problem to profit maximization, we choose the cost function,
𝐶(𝑋,𝑇), to represent profit loss from coarse to full personalization. We first define R𝑖(𝒙𝑖, ˜𝒕𝑙) to
be the expected profits from assigning treatment ˜t𝑙 to an individual with covariates 𝒙𝑖,
R𝑖(𝒙𝑖, ˜𝒕𝑙)≜𝐸𝜋[R𝑖|𝒙𝑖,𝑇𝑖,1 = ˜𝑡𝑙,1, 0,..., 0]+···+ 𝐸𝜋[R𝑖|𝒙𝑖, 0,...,𝑇 𝑖,𝑑 = ˜𝑡𝑙,𝑑,..., 0]+···
+𝐸𝜋[R𝑖|𝒙𝑖, 0,...,𝑇 𝑖,𝐷 = ˜𝑡𝑙,𝐷]. (9)
10Equation 7 is also known as the Monge-Kantorovich problem in the optimal transport literature. A more formal
discussion is in Appendix Section A.
11The nonnegative constraint ensures the segments have one or more individuals assigned to them. The adding-up
constraint ensures that everyone is assigned to a segment. The feasible treatment constraint implies the segment’s
assigned treatment can take values in only one treatment dimension.
11

We then define ¯𝑅𝑖 to be the profits for an individual with𝑥𝑖 if firm fully personalizes,
¯𝑅𝑖≜ max  𝐸𝜋[R𝑖|𝒙𝑖,𝑡∗ 𝑖,1,... 0],...,𝐸 𝜋[R𝑖|𝒙𝑖, 0,...,𝑡 ∗ 𝑖,𝑑,... ],...,𝐸 𝜋[R𝑖|𝒙𝑖, 0,...,𝑡 ∗ 𝑖,𝐷] 	 . (10)
We further define R(𝒙, ˜𝒕𝑙) as the vector ofR𝑖(𝒙𝑖, ˜𝒕𝑙) across individuals𝑖∈{ 1,...,𝑁 }, ¯𝑹 as the
vector of ¯𝑅𝑖 across individuals, and 𝒙 as the stacked covariate matrix across individuals.
The cost function is
𝐸𝜋[𝐶(𝑋,𝑌)|𝑡 = ˜𝒕𝑙] =

R(𝒙, ˜𝒕𝑙)− ¯𝑹

2 (11)
in the optimal transport problem (Equation 7). The cost function in Equation 11 represents profit
regret: It is the square of the difference of coarse personalization profits ( R(𝒙, ˜𝒕𝑙)) to full per-
sonalization profits ( ¯𝑹).12 Because full personalization is profit maximizing, the firm will receive
weakly lower profits from coarse personalization as it can only form 𝐿 segments to personal-
ize. Thus, minimizing profit regret to an upper bound corresponds to profit maximization in the
coarse personalization solution.
As we will detail in Section 5, the problem, as it stands, is computationally burdensome. To
alleviate this concern, we impose two assumptions: The first is a strict concavity assumption on
the continuous CATE function, 𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑). The second is a weak convexity assumption on the
cost function,𝑐𝑑(𝑡𝑖,𝑑).
Assumption 1. (Strict Concavity of the Continuous Conditional A verage Treatment Effects)
The continuous conditional average treatment effect 𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑) is strictly concave in 𝑡𝑖,𝑑. For
𝑡,𝑡′∈[ 0, ¯𝑡𝑑]⊂ R+ and𝛼∈[ 0, 1],𝜏𝑑(𝒙𝑖,𝛼𝑡 +( 1−𝛼)𝑡′) >𝛼𝜏𝑑(𝒙𝑖,𝑡)+( 1−𝛼)𝜏𝑑(𝒙𝑖,𝑡′).
Assumption 2. (Convexity of the Cost Function)
The cost function 𝑐𝑑(𝑡𝑖,𝑑) is convex in 𝑡𝑖,𝑑. For 𝑡,𝑡′∈[ 0, ¯𝑡𝑑]⊂ R+ and𝛼∈[ 0, 1],𝑐𝑑(𝛼𝑡+( 1−
𝛼)𝑡′)≤ 𝛼𝑐𝑑(𝑡)+( 1−𝛼)𝑐𝑑(𝑡′).
Assumption 1 imposes a strict concavity requirement on the estimated continuous CATEs.
It captures the notion of diminishing sensitivity of the treatment level—that is, how at higher
treatment levels, further changes in the treatment level do not increase the treatment effect as
much. Assumption 2 rules out economies of scale in the cost of issuing the treatment as the
treatment level increases.
Because the difference between a strictly concave function and a convex function is strictly
concave, the firm’s program in the first step (Equation 6) now has a unique solution 𝑡∗ 𝑖,𝑑 that
is either an interior solution or on the boundary. After the firm solves 𝐷 programs for each
12We can extend the cost function to account for the number of segments in Online Appendix Section C.
12

individual𝑖 to fully personalize, it would have constructed optimal treatment levels{{𝑡∗ 𝑖,𝑑}𝐷 𝑑=1}𝑁 𝑖=1
and have estimated continuous CATE functions{{𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)}𝐷 𝑑=1}𝑁 𝑖=1.
Proposition 3 demonstrates that the optimal transport problem in Equation 8 is a convex
program in treatment values under Assumptions 1 and 2. We stress that any strictly concave
function of CATEs will satisfy Assumption 1, and any convex function will satisfy Assumption
2.
Corollary 4 shows that the convex program ensures that the assignment rule (optimal trans-
port plan) deterministically maps individuals to segments. Having a deterministic segmentation
rule is beneficial because it ensures the segments are easily implementable, and we further discuss
its downstream practical implications in Section 5. The proofs are in Appendix Section B.
Proposition 3. Under Assumptions 1 and 2, 𝐸𝜋[𝐶(𝑋,𝑇)] is strictly convex in ˜𝒕.
Corollary 4. Under Assumptions 1 and 2, the optimal transport plan 𝜋 that solves Equation 8
deterministically maps individuals to their segment.
Discussion
The coarse personalization solution maximizes profits by simultaneously choosing (1) the seg-
mentation rule of individuals and (2) the assigned treatment for each segment. At the solution,
the assigned treatment level is chosen such that its average marginal effect is equal to its aver-
age marginal cost in each segment. With full personalization, the marginal effect of treatment
equals the marginal cost of treatment at the individual level. Intuitively, our solution shifts the
profit-maximizing personalization principle from equating marginal effect and marginal cost in-
dividually to equating them at the segment level. Online Appendix Section D provides a formal
derivation of this intuition using the first order condition of Equation 8.
Coarse personalization can be interpreted as a more regularized version of full personaliza-
tion. Heterogeneous treatment effect estimates and CATEs are known to be noisy (Wager and
Athey, 2018; Rafieian and Yoganarasimhan, 2021; Hitsch et al., 2024), and by coarsely assigning
segments or groups of customers, firms are able to explicitly choose the level of regularization
when using heterogeneous treatment effects to personalize. At one extreme, full regularization
implies everyone receives the same treatment (𝐿 = 1) and at the other, full personalization implies
everyone gets their own fully personalized treatment (𝐿 =𝑁 ). The coarse personalization frame-
work enables navigation between two extremes while ensuring the profit maximizing groups and
treatments are formed at each level of regularization.
We also highlight that nonparametric approaches to estimate continuous CATEs have been
developed in the machine learning literature (Swaminathan and Joachims, 2015; Kallus and Zhou,
13

2018) and operations literature (Zhou et al., 2022). However, these methods either cannot incor-
porate the concavity condition from Assumption 1 or they require that treatment values for each
segment be specified ex ante for computational tractability. Thus, without additional adaptions
and theoretical adjustments, these methods cannot be directly applied to our setting.
4 Computational solution
To computationally solve our coarse personalization problem, we adapt a version of Lloyd’s Al-
gorithm (Algorithm 1), from Lloyd (1982) to maximize profits while accounting for all the con-
straints. Our algorithm provides an iterative method to efficiently solve the problem. Various
versions of Lloyd’s Algorithm have been used in the literature to solve optimal transport prob-
lems (Pollard, 1982; Canas and Rosasco, 2012).
Figure 2 illustrates the algorithm’s optimization procedure for two-dimensional treatments.
Our formulation of the optimal transport problem falls under the class of mixed-integer linear
programs; other methods to solve semidiscrete optimal transport problems can be found in Peyré
and Cuturi (2019). We discuss the benefits of Algorithm 1 over the brute force solution via grid
search in Section 4.2. Using the promotions-management setting from our empirical example, we
outline the procedure in Online Appendix Section E.
Given continuous CATE estimates{{𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑)}𝐷 𝑑=1}𝑁 𝑖=1 and{{𝑡∗ 𝑖,𝑑}𝐷 𝑑=1}𝑁 𝑖=1 from the first step,
the firm can solve the coarse personalization problem by using Algorithm 1. The firm chooses the
number of segments (𝐿) to offer and our algorithm will supply the profit-maximizing segments
and their assigned treatments.
As Figure 2 demonstrates, in each iteration, our algorithm cycles through updating the seg-
ments and their assigned treatment values. The feasible treatment constraint is enforced by
choosing the dimension of the treatment that yields the highest expected return to the firm for
each cell. The algorithm terminates when the change to the treatment values after each iteration
is smaller than a prespecified tolerance value. The final profits for the firm is the sum of the
expected profits from the terminal step’s segmentation rule.
4.1 Discussion of the Lloyd’s Algorithm’s adaptation
In Algorithm 1, we make two adaptations to Lloyd’s Algorithm to directly maximize profits.
First, the optimization metric is different. Rather than forming segments (Voronoi Cells) and
their assigned treatments (Barycenters) to maximize Euclidean distance between treatments, we
construct both simultaneously to maximize profits. Second, since each feasible treatment is only
14

Algorithm 1 Adapted Lloyd’s Algorithm
Notation: There are 𝐿 segments that need to each be assigned a treatment and 𝐷 treatment
dimensions. The candidate treatment for 𝒕𝑙 in step 𝑘 of the algorithm is denoted 𝒕𝑘 𝑙 . The set
of individuals assigned to treatment 𝑙 is denoted ℓ. The candidate treatments have form 𝒕𝑙 =
(0,...,𝑡 𝑙,𝑑,..., 0) and are nonzero only in dimension𝑑 with value𝑡𝑙,𝑑.𝛿 represents a prespecified
tolerance value.
Step 0: Guess the initial set of𝐿 treatment vectors ˜𝒕0 ={˜𝒕0 1,..., ˜𝒕0 𝑙,..., ˜𝒕0 𝐿}.
Step 𝒌:
• (Form segments) Compute the Voronoi Cells for each proposed treatment˜𝒕𝑘 𝑙,∀𝑙∈{ 1,...,𝐿 }
𝑣𝑘 𝑙 ={𝑥∈𝑋 :|𝐶(𝑋, ˜𝒕𝑘 𝑙)|≤| 𝐶(𝑋, ˜𝒕𝑗)|,∀𝑗 ≠𝑙}.
• (Choose new candidate treatments for each segment ) Compute the Barycenter values in each
dimension𝑑∈{ 1,...,𝐷 } and for each Voronoi Cell𝑣𝑘 𝑙,∀𝑙∈{ 1,...,𝐿 }
˜𝒕′ 𝑙 =(˜𝑡′ 𝑙,1,..., ˜𝑡′ 𝑙,𝐷) = 1 𝑃(𝑣𝑘 𝑙) ∫ 𝑣𝑘 𝑙 𝑤𝑑𝑃(𝑤).
• (Evaluate profits for candidate treatments for each segment) Compute profits for each feasible
treatment generated from ˜𝒕′ 𝑙 , which are of form {(0,..., ˜𝑡𝑙,𝑑,... 0)}𝐿 𝑙=1, and have expected
profits
∑︁
𝑖∈ℓ
𝐸[R𝑙,𝑑|𝑥𝑖,𝑡𝑖,1 = 0,...,𝑡 𝑖,𝑑 = ˜𝑡𝑙,𝑑,...,𝑡 𝑖,𝐷 = 0] =
∑︁
𝑖∈ℓ
𝜏𝑑(𝒙𝑖, ˜𝑡𝑙,𝑑)− 𝑐𝑑(˜𝑡𝑙,𝑑).
• (Update candidate treatments to ensure feasibility ) Update ˜𝒕 by forcing the feasibility con-
straint. We choose the feasible treatment that yields highest profits across each dimension
𝑑∈𝐷
˜𝒕𝑡+1 𝑙 =
 

(˜𝑡′ 𝑙,1,..., 0) if ˝ 𝑖∈ℓ𝐸[R𝑙,1|𝒙𝑖, ˜𝑡𝑖,1,..., 0] > ˝ 𝑖∈ℓ𝐸[R𝑙,𝑑′|𝒙𝑖, 0,..., ˜𝑡𝑖,𝑑′,..., 0],∀𝑑′ ≠ 1 ... ...
(0,..., ˜𝑡′ 𝑙,𝑑,... 0) if ˝ 𝑖∈ℓ𝐸[R𝑙,𝑑|𝒙𝑖, 0,..., ˜𝑡𝑖,𝑑,..., 0] > ˝ 𝑖∈ℓ𝐸[R𝑙,𝑑′|𝒙𝑖, 0,..., ˜𝑡𝑖,𝑑′,..., 0],∀𝑑′ ≠𝑑 ... ...
(0,..., ˜𝑡′ 𝑙,𝐷) otherwise.
Terminate the algorithm when ˜𝒕𝑘+1 is close enough to ˜𝒕𝑘, or|| ˜𝒕𝑘+1− ˜𝒕𝑘|| <𝛿.
15

nonzero in one dimension, we include a dimension-reduction step where the Barycenter of the
Voronoi cell is projected down to a treatment value in one dimension. 13 For each segment, we
choose the treatment dimension that maximizes profits.
Even though the coarse personalization problem is strictly convex in the treatment values
by Proposition 3, the requirement that treatments are feasible, or are nonzero in one dimension,
adds a combinatorial constraint to the problem.14 As a result, the optimization problem becomes
NP-hard and a global optimum is not guaranteed to be found with our algorithm or even with an
exhaustive grid search.
To mitigate this concern, we (1) run Algorithm 1 five times with different starting values and
choose the best performing run and (2) compare our results from our adapted Lloyd’s Algorithm
with a more exhaustive search using BFGS. We find that the best performing run of our algorithm
is effectively identical to that of the exhaustive search. We discuss the difference between our
algorithm and the grid search in the next subsection.
If we relax the treatment feasibility constraint in our coarse personalization problem, or let
the assigned treatments take values in each dimension of the treatment, then we can avoid the
combinatorial constraint. In our application, we require treatment feasibility because individuals
are only sent one type of promotion. However, this constraint can be relaxed in a product design
application when we optimize all attributes of the product simultaneously.15
Lastly, our results in Section 3.2 show that the solution under our assumptions leads to a
deterministic transport map: Individuals are assigned to one segment and not probabilistically
assigned to different segments. This allows us to form discrete segments that are more practically
implementable than probabilistic segments.
4.2 Grid search comparison
A common alternative approach to solving the optimal transport problem is using a brute-force
grid search, and we now discuss why our solution is advantageous over a grid search. To imple-
ment a grid search, the firm can discretize over the treatment domainX ex ante, thereby convert-
ing the semidiscrete optimal transport problem into a fully discrete optimal transport problem.16
13These are in the last two substeps in Step𝑘 of Algorithm 1.
14The dimension-reduction step in Algorithm 1 leads to discontinuities and possible sudden jumps in the assigned
treatment values when the assigned treatment dimension changes. These discontinuous updates arise due to the
combinatorial constraint.
15In Algorithm 1, we would then omit the dimension-reduction step and only run the first two substeps under step
𝑘. The coarse personalization problem then collapses to a standard convex optimization problem over a compact set.
Since Lloyd’s Algorithm is a greedy algorithm, it converges to a local optimum (Lu and Zhou, 2016), which is the
global optimum by the convexity of the problem.
16The use of discretization to approximate a continuous domain underlies the mass transport approach to solving
continuous-continuous optimal transport problems in Chiong et al. (2016).
16

Then, over the finite grid of possible assignments and treatment levels, the firm can combinatori-
ally search for segments and their assigned treatments. While we can relax Assumptions 1 and 2
in the grid search, the combinatorial space will grow exponentially in the number of individuals
and as it suffers from the curse of dimensionality. Specifically, for 𝑁 individuals,𝐿 treatments,
and𝐷 dimensions with𝐺 discrete points in each dimension, the combinatorial space for the grid
search is 𝐺𝐷 𝐿 𝐿𝑁 .17
The grid search algorithm’s run time isO((𝐺𝐷)𝐺𝐷/2𝐿𝑁). In contrast, the run time of𝐼 itera-
tions of our adapted Lloyd’s Algorithm isO(𝐼𝐷𝐿𝑁) and will be substantially faster as it removes
the exponential factor. For many high-dimensional treatments, the standard grid search approach
is computationally infeasible. Instead, using adapted Lloyd’s Algorithm or any convex optimizer
that leverages Assumptions 1 and 2 is recommended.
Algorithm 1 and the brute force approach yield similar profits. In Online Appendix Section
F, we describe our grid search implementation and discuss why Algorithm 1 runs37 times faster
than the grid search using an example from our empirical application. We also provide intuition
why our approach is faster. In short, our algorithm uses a more computationally efficient update
rule and avoids the curse of dimensionality.
5 Why optimal transport?
Given the constraint that only 𝐿 segments can be offered, our coarse personalization solution
solves which segments to offer and their corresponding treatment to maximize profits. In essence,
the distribution of CATEs estimated in the first step is mapped to a discrete distribution of as-
signed treatments. Figure 1 visualizes this procedure in a stylized example.
In essence, full personalization is profit maximizing for the firm because it optimally chooses
profit maximizing treatments at the individual level. Coarse personalization accounts for the
extra constraint on the number of segments and uses optimal transport to solve the segmentation
problem. Our coarse personalization solution generates the maximum possible expected profits
given the limitation on the number of segments.
Unlike the traditional marketing segmentation framework, we have solved both segmenta-
tion and targeting steps simultaneously. The former are the assignment of individuals to each
segment and the latter are the unique treatment values chosen for each segment. Because we are
discretizing full personalization’s estimates into a few segments in the second step, our “person-
alize then discretize” approach inverts the “discretize then personalize” approach used in classical
17For example, if the firm chooses to assign three different promotions ( 𝐿 = 3) across dollar off and percentage
off promotion types (𝐷 = 2) that take on ten possible values(𝐺 = 10) for fifteen people(𝑁 = 15), there are over 16
billion combinations to search over.
17

marketing. The optimal transport problem minimizes profit regret relative to full personalization,
so its segmentation and targeting rules should yield higher profits than those sequentially con-
structed by first segmenting on covariates or preferences and then forming targeting rules. We
additionally recover full personalization profits when we let the number of segments equal to the
number of individuals (𝐿 = 𝑁 ). The final choice of the number of segments 𝐿 to offer is a free
parameter for the firm to tune.
More generally, we espouse the optimal transport approach because it (1) allows us to in-
terpret the coarse personalization problem in an economic manner, (2) suggests a simple com-
putational solution in Algorithm 1, and (3) links the problem to the broader transport theory
literature. Naturally, marketing researchers can use black-box optimizers to solve the optimiza-
tion program via brute-force instead of using our optimal transport framework. However, this
approach forgoes the benefits from the optimal transport approach and can be computationally
slower as discussed in Section 4.2 and in Appendix Section F. Economically, the optimal transport
solution finds segmentation plans such that the average marginal benefit is equal to the marginal
cost of treatment across assigned segments (Appendix Section D). Algorithm 1 provides a compu-
tationally simple and scalable solution, and its link would not be made clear without viewing the
problem through an optimal transport lens. Our algorithm is especially efficient in higher dimen-
sions as it searches over treatments that are close to the individual optimal values: Compared to
a black-box optimizer, our algorithm embeds a “warm start” in the optimization process. Lastly,
recasting our coarse personalization problem as a semidiscrete optimal transport problem allows
us to connect our marketing problem to the broader transportation theory literature. Exploring
additional links between the two may prove fruitful for future research.
We emphasize that the link to the optimal transport framework is still beneficial even if As-
sumptions 1 and/or 2 are relaxed. In that case, the segmentation rule shifts from deterministically
assigning each individual to a single segment to probabilistically assigning each individual to mul-
tiple segments.18 This probabilistic assignment to segments also appears in the latent class and
finite mixture models in the marketing literature (Kamakura and Russell, 1989).
Thus, our recasting of the classical marketing segmentation problem as an optimal transport
framework is beneficial because (1) the correct target metric of profit is used when forming seg-
ments, (2) it lends a link to Lloyd’s Algorithm for a computationally efficient implementation,
and (3) under Assumptions 1 and 2 we show the solution’s optimal segments and their assigned
treatments are unique and each individual is deterministically assigned to a segment.
18In the optimal transport literature, the solution would then be the Kantorovich relaxation to our Monge-
Kantorovich problem and a pure Monge mapping is not guaranteed to exist. Additional details can be found in
Appendix Section A.
18

6 Empirical application
In this section, we illustrate our methodology with data from a large-scale field experiment
conducted by a food delivery platform. Marketing mix treatments are two dimensional: dol-
lar amount off and percentage off promotions. Customers will be assigned to a promotion of one
of the two treatment dimensions.
We show that with our coarse personalization framework, the company can achieve prof-
its close to full personalization while using only a handful of optimized segments. Further, we
demonstrate that the coarse personalization solution significantly outperforms classic sequential
segmentation procedures in generating expected profits.
6.1 Setting
We use a large-scale RCT dataset for a food delivery platform across three core-based statistical
areas in the United States. There are over 1.2 million unique customers in the data with around
100 pretreatment variables that describe customers’ recency, frequency, and monetary (RFM)
characteristics. Across these customers, the following promotional treatments were randomly
assigned: dollar amount off ( $2, $3, $4, $5), percentage off ( 5%, 10%, 15%, 20%), and no treatment.
The assigned promotion can only be used on the next order by the customer, the promotions are
issued by email, and the no treatment group will act as a control group. We assume customers
do not engage in coupon gaming or stockpiling.. Following Section 3’s framework, we have a
two-dimensional treatment vector that consists of dollar off and percentage off promotions. We
set the dollar off promotion to be the first dimension and the percentage off promotion as the
second dimension. We conduct randomization checks in Online Appendix Section G.
The firm aims to maximize profits by personalizing its dollar-off and percentage-off promo-
tions for its customer base. The outcome variable is the total profits generated from the customer
28 days after the promotion was sent. This represents the firm’s net profits per order, after sub-
tracting payments to delivery drivers and restaurants. The firm’s profits from consumer 𝑖 after
28 days is defined as
Profits after 28 days𝑖 = Spending after 28 days𝑖− Promotion cost𝑖 (12)
where the promotion cost depends on the type of promotion issued. Figure 3 plots the profits
by treatment value for dollar off and percentage off promotions. In both treatment dimensions,
profits generally increase with higher promotion values and have a concave shape which suggests
diminishing sensitivities at higher levels of treatment.
The ATE estimates for the firm’s profits are presented in Table 1. They represent the difference
19

in profits of comparing the treatment arms in Figure 3 to the control group of no treatment. Using
a two-sided𝑡-test, we find that the ATE estimates for four dollar off, fifteen percentage off, and
the twenty percentage off promotions are statistically significant from zero at the𝛼 = 0.05 level.
Further, the point estimates of the ATEs are all positive, which suggests the promotions have a
positive effect on profits.
Following Section 3’s notation, profits are R𝑖, spending levels are𝑌𝑖, and promotion costs are
𝑐𝑑(𝑡𝑖,𝑑), where𝑡𝑖,𝑑 is the treatment issued to consumer𝑖 that is nonzero in dimension𝑑. We only
observe profits after 28 days for each consumer but we can recover spending levels by imposing
structure on the firm’s costs. The firm’s expected returns, or expected profits, for individual 𝑖
assigned treatment𝑡𝑖,𝑑 that is nonzero in dimension𝑑 is
𝐸[𝑅𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 =𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0] =𝐸[𝑌𝑖|𝒙𝑖,𝑇𝑖,1 = 0,...,𝑇 𝑖,𝑑 =𝑡𝑖,𝑑,...,𝑇 𝑖,𝐷 = 0]− 𝑐𝑑(𝑡𝑖,𝑑).
(13)
We define the cost of the dollar off promotion as the dollar amount itself. For the percent-
age off promotion, the costs for consumer 𝑖 are the percentage off times the customer’s average
promotional spending on an order over the last year. The cost of the promotions are
𝑐𝑑(𝑡𝑖,1) =𝑡𝑖,1 (14)
𝑐𝑑(𝑡𝑖,2) =𝑡𝑖,2× average past promo spend𝑖 (15)
for dollar off promotion𝑡𝑖,1 and for percentage off promotion𝑡𝑖,2. For customers who have never
received a promotion before the field experiment, their past promotional spend for an order was
median imputed. The treatment vector (𝑡𝑖,1,𝑡𝑖,2) =(0, 0) represents the no promotion case; the
firm incurs no cost for withholding a promotion.
We also assume that the continuous CATEs,𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑), are strictly concave in the treatment
value,𝑡𝑖,𝑑, to satisfy Assumption 1. The strict concavity assumption then implies that customers
have diminishing sensitivities to promotion levels. By construction, the promotions’ costs are
weakly convex in𝑡𝑖,1 and𝑡𝑖,2 satisfying Assumption 2.
We interpret the continuous CATEs, 𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑), as a behavioral sensitivity to dollar off or
percentage off treatments (Briesch, 1997). We find that even when the two yield the same expected
value to the customers, the continuous treatment effect is different; customers have differing
sensitivity when presented with two promotions that yield the same expected monetary value.
Otherwise, if consumers had the same sensitivity to the expected value of both promotions, then
we would be able to collapse the two dimensions of treatments to a one-dimensional, expected
value of the promotion for each customer.
20

6.2 Estimation procedure
To estimate the continuous CATEs, ˆ𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑), we first implement the Causal Forest from Wager
and Athey (2018) in each of the two treatment dimensions. To adjust for randomization concerns
in the field experiment (see Appendix Section G), we use generalized regression forests that use
propensity score estimates to adjust for possible stratification between the treatment and holdout
samples (Athey et al., 2019).19
To force strict concavity of the continuous CATEs, we then impose a logarithmic functional
form that is parameterized by𝛼𝑖,𝑑 and𝛽𝑖,𝑑,
ˆ𝜏𝑑(𝒙𝑖,𝑡𝑖,𝑑) =𝛼𝑖,𝑑+𝛽𝑖,𝑑 log(1+𝑡𝑖,𝑑)+ 𝜖𝑖,𝑑, (16)
along with a shape restriction that 𝛽𝑖,𝑑 > 0 and we let 𝜖𝑖,𝑑 represent the approximation error.20
The individual continuous CATEs are parameterized by the estimates{{ ˆ𝛼𝑖,𝑑, ˆ𝛽𝑖,𝑑}2 𝑑=1}𝑁 𝑖=1, and we
use these to solve for the optimal treatment levels {𝑡∗ 𝑖,1,𝑡∗ 𝑖,2}𝑁 𝑖=1 following Equation 6. We then
choose the number of segments (𝐿) and run Algorithm 1 to attain the segments and their assigned
treatments.
We bootstrap to produce standard errors for our estimates. In our estimation results, we
focus on the implementation uncertainty of the second step, the optimal transport step, which
is of main practical interest to the firm. 21 In practice, firms treat the first step CATE estimates
as given and focus on the implementation uncertainty of the different methods in generating
profits. Our focus on implementation uncertainty reflects situations where the firm is concerned
with how the procedure performs across different markets, as well as uncertainty around the roll
out of the personalization policy.
To do so, we take the first stage treatments as the ground truth and bootstrap only the second
step of our procedure.22 More specifically, we only bootstrap the segmentation and treatment as-
signment steps from Section 3.2 to quantify the implementation error. For our other segmentation
benchmarks, we similarly only bootstrap the segmentation and treatment assignment steps.
As a result, the comparisons of interest are (1) how close coarse personalization can get to
19We also estimate the continuous CATEs directly using Deep Neural Networks (Farrell et al., 2020, 2021). We find
similar results which suggest that deviations from perfect randomization do not heavily influence our results. To
account for imperfect randomization in this approach, we can implement the DR-Learner procedure from Kennedy
(2020) while using DNNs for the propensity score and regression function estimators.
20Any strictly concave functions can be used in this procedure. The stylized logarithmic functional form of the
marketing treatment response to capture diminishing sensitivity has also been used in the CRM literature (Rust and
Verhoef, 2005).
21See Hitsch et al. (2024) for a discussion around uncertainty in decision-making for personalization strategies.
22To fully account for both model uncertainty in the first step and the implementation uncertainty in the second
step, we can use the confidence intervals from the Causal Forest’s CATE estimates. We then can sample from the
CATE confidence intervals and then implement the optimal transport step.
21

the full personalization in generating profits and (2) how our coarse personalization solution
compares to sequential segmentation procedures.
6.3 Results
In our application, we find that coarse personalization both (1) outperforms sequential segmen-
tation procedures and (2) almost recovers full personalization profits after using five segments.
Figure 5 summarizes the main results. We now discuss these results in more detail.
The first step’s CATE estimates were estimated using the entire set of 126 covariates and
the entire dataset of 1,213,390 individuals. 23 The continuous CATE parameterization produced
an average 𝑅2 of 0.925 and 0.770 respectively for the dollar off and percentage off dimensions.
We implement the honest validation procedure (Misra, 2021) to compare the continuous CATE
parameterization in Equation 16 to the nonparametric estimates in a holdout treatment and find
that our parameterization performs well out of sample (Online Appendix Section H).
To visualize the continuous CATEs, we can turn to Figure 4 to see the estimates across indi-
viduals evaluated at the treatment arms. We see that the treatment effects generally rise as the
promotion value increases in each dimension. On average, customers are more receptive to the
dollar off promotions than to the percentage off promotions since the CATE levels are higher for
the former. The treatment effect of the percentage off promotion has more variance than that of
the dollar off promotion.
We now examine the performance of our coarse personalization solution by quantifying prof-
its across different numbers of available segments. Table 3 shows the percentage of expected in-
cremental profits recouped by coarse personalization compared to full personalization. 24 Figure
5 plots the coarse personalization’s expected incremental profits across a hundred bootstrap iter-
ations. The lines represent the bootstrap means and the bands represent one bootstrap standard
deviation. Full personalization corresponds to issuing 2, 206 unique treatments in our scenario
when rounding to three significant figures.
We find that with three unique treatments, we recoup around99% of the full personalization’s
expected profits and with five unique treatments, we recoup over 99.5% of the full personaliza-
tion’s expected profits. These results suggest the firm is able to match almost all of the full
personalization’s expected profits by using only a handful of unique segments with our coarse
23We preprocess the CATE estimates. From our CATE parameterization, individuals whose ˆ𝛽𝑖,𝑑 are close to 0
are not responsive to promotions. After accounting for the promotions’ cost, these individuals would not receive
a promotion. Thus, dropping these individuals does not have an effect on incremental profits. Consequently, we
exclude individuals with values less than or equal to 10−6. The second step was run on the remaining 1, 203, 379
individuals.
24Expected incremental profits are defined as additional expected profits over the expected baseline profits of not
targeting anyone.
22

personalization solution.
To visualize our solution, we can turn to Figure 6, which plots the optimal treatment values,
{𝑡∗ 𝑖,1,𝑡∗ 𝑖,2}𝑁 𝑖=1, across individuals and segment assignments for ten segments (𝐿 = 10). The optimal
treatment values represent the treatment values in each treatment dimension for the individuals
under full personalization. 25 Table 2 provides the treatment values for the segments’ assigned
treatments and their segment sizes. The expected incremental profits for each individual under
the assigned treatment is provided on the vertical axis and a plane at zero expected profits is
provided for reference. The points represent the optimal treatment values {𝑡∗ 𝑖,1,𝑡∗ 𝑖,2}𝑁 𝑖=1 across
individuals and the colors represent their assigned treatment. The shape of the points represents
whether the assigned treatment is a dollar off (circle) or a percentage off (triangle) promotion.
The takeaways from Figure 6 are threefold. First, across the two dimensions of treatment,
the dollar and percentage off, we see explicit quantization of the assignments in each dimension
and individual assignment to only one segment. The quantization structure is an artifact from
our optimal transport problem which ensures individuals that generate similar profits within a
treatment dimension are grouped together.
Second, we see substantial heterogeneity in individual-level expected incremental profits.
Most of the individual expected profits are close to zero and profits are generally larger for those
with higher optimal treatment levels; the most receptive customers to the promotions produce
the largest profits. On the flip side, a handful of individuals assigned the lowest dollar off and
percentage off promotions generate negative profits. If the firm could use more segments, these
individuals would be given no promotion or an even smaller promotional value.
Third, there is significant bunching of individuals at the upper bound in Figure 6 for the per-
centage off treatment. This implies that we are leaving profits on the table by enforcing this upper
bound. While we can expand the upper bound of allowed treatments using our parameterization
of the continuous CATE estimates, we retain the upper bound at$5 and 20% in the optimal trans-
port problem because this was the largest promotion from RCT. In future experiments, the firm
may consider testing higher promotional values.
Breaking down the segments, we see from Table 2 that most of the customers are assigned to
the second, seventh, and tenth treatments and these are all dollar off promotions. Many of the
offered treatments are tightly packed between the one to two dollar off promotion in Figure 6
which suggests that a majority of individuals are most receptive to the firm using one dollar off
to two dollars off promotions.
25For example, the rightmost yellow circular point represents an individual whose optimal treatment values,
(𝑡∗ 𝑖,1,𝑡∗ 𝑖,2), are close to five dollars off and twenty percent off. That individual is in segment six and is assigned a
2.79 dollar off promotion. This assignment generates around five dollars in expected incremental profits for the firm.
23

6.3.1 Comparison to sequential segmentation procedures
We now compare our coarse personalization solution to sequential segmentation procedures that
first segment on covariates, individual preferences, and optimal treatment levels and then form
targeting rules. These comparisons (1) shed light on why our coarse personalization procedure
performs better by targeting profits when forming segments and (2) quantify how much our
proposed procedure outperforms these sequential techniques. Figure 5 and Table 3 summarize
our key results.
We find that our coarse personalization solution (“personalize then discretize”) significantly
outperforms the sequential segmentation methods (“discretize then personalize”). From our method-
ology, coarse personalization generates the maximum expected profits possible given the limits
on the number of segments. We now document how we implemented each sequential segmenta-
tion procedure and then discuss how they compare to our coarse personalization solution.
Sequential benchmark procedures
Covariate segmentation. We segment on customer covariates, which contain customers’ platform
behavior and RFM variables. We reduce the covariate size to 59 covariates by retaining vari-
ables that are relevant either for predicting subsequent purchase incidence or purchase amount
with the Lasso.26 For this reduced set of covariates, we implement𝑘-means to segment the data.
We then select the best treatment value in generating profits for each segment as the assigned
treatment. This segmentation procedure represents classical ex ante segmentation since neither
the outcome nor treatment variables from the data are used in forming the segments themselves
after the variable reduction step.
Preference segmentation . To segment on consumer preferences, we form segments on the
individuals’ treatment sensitivity. We implement 𝑘-means on{ ˆ𝛽𝑖,1, ˆ𝛽𝑖,2}𝑁 𝑖=1 estimates from our
parameterization of the CATEs (Equation 16) to form segments. The ˆ𝛽𝑖,1, ˆ𝛽𝑖,2 parameters capture
the sensitivity of the individuals to the dollar and percentage off promotions, which in turn are
proxies for the individuals’ price sensitivity. After running 𝑘-means to form segments, we then
find the profit-maximizing treatment for each segment.
Optimal treatment levels segmentation. We can segment on the optimal treatment levels across
individuals by running𝑘-means directly on{𝑡∗ 𝑖,1,𝑡∗ 𝑖,2}𝑁 𝑖=1. The optimal treatment levels are the indi-
vidually optimal promotion values for each individual under full personalization. Here, forming
segments using𝑘-means allocates individuals with the same optimal treatments (for both dollar
off and percentage off) in the same segment. After segments are constructed, we find the optimal
26The 59 RFM covariates include variables that capture customers’ past spending, tipping, delivery vs. pickup,
and order cancellation behavior, promotional spending, their location, and the device they use to order.
24

treatment level and treatment dimension that maximizes profits.
Discussion
From Figure 5 and Table 3, we see that segmenting on covariates barely helps the firm in max-
imizing profits. Segments formed only using consumer characteristics do not correspond to the
optimal segments for maximizing profits; profits barely increase as we increase the number of
segments. Segmenting on consumer preferences and optimal treatment levels does better than
segmenting on covariates. These results corroborate the conclusions found in the segmentation
literature: Segmenting on consumer preferences performs better than segmenting on demograph-
ics in generating profits (Gupta and Chintagunta, 1994; Rossi et al., 1996).
Since optimal treatment levels combine information on preferences with treatment costs, seg-
mentation on preferences and segmentation on optimal treatment levels embed similar informa-
tion and thus should perform similarly. However, segmenting on optimal treatment levels is less
noisy because it accounts for additional information in the treatments’ costs as we see in Figure
5.
Coarse personalization outperforms segmenting on optimal treatment levels because coarse
personalization uses the correct distance metric of expected profits for segmentation instead of Eu-
clidean distance between the optimal treatment levels (𝑡∗ 𝑖,1,𝑡∗ 𝑖,2). This specific difference is exempli-
fied when comparing the quantization of the segments in each treatment dimension. Appendix
Figure 12 provides a top-down view of Figure 6 and shows the segmentation structure of the
coarse personalization solution. Appendix Figure 13 shows segmentation structure when form-
ing segments by optimal treatment levels.
In the coarse personalization solution, the nearest treatment in Appendix Figure 12 is not
necessarily assigned to each individual because the distance metric used for segmentation is in
expected profits (Equation 11); it could be more profitable to give the individual a treatment in an-
other treatment dimension. However, within each dimension of treatment, the nearest treatment
will be assigned to the individual. In contrast, when segmenting on optimal treatment levels,
the nearest treatment is always assigned to the individual as seen in Appendix Figure 13. As a
result, the constructed segments from coarse personalization will outperform those constructed
from using the optimal treatment level when the firm’s goal is to maximize profits because the
objective function directly targets profits.
The lack of convexity guarantees for the three sequential benchmark procedures implies run-
ning the 𝑘-means solution is unstable; running it again will yield very different segments. In
contrast, rerunning Algorithm 1 yields almost identical results and the solution is quite stable.
Finally, we note that capturing 99.5% of the fully personalized profit with only five segments
is unique to this empirical application. In other contexts, the gap between coarse and full per-
25

sonalization could be wider or narrower.
6.3.2 Discrete treatments benchmark
In this section, we evaluate the cost of restricting the treatment variables (dollar off and per-
centage off) to the discrete levels used in the experiment. First, we examine the optimal blanket
promotion obtained when treatments are constrained. Next, we focus on policy-learning ap-
proaches that only assign the discrete treatments observed in the experimental data, thus ignoring
treatment continuity.27 Through both exercises, we demonstrate that neglecting the continuous
nature of treatments results in substantial unrealized profits.
First, we calculate the difference in profits between the firm’s historical blanket promotion of
ten percent off and an optimized blanket promotion. For the blanket promotion optimization, we
consider the cases where (1) the firm only uses the experiment’s discrete treatment values and
(2) the firm leverages the continuity of the treatment values. This comparison demonstrates how
much money the firm leaves on the table by not completely optimizing the blanket promotion.
If the firm chose the best treatment arm from the RCT to blanket target, the firm would blanket
a two dollar off promotion and attain expected profits of789, 868 dollars. Allowing for continuous
treatments, the firm would blanket 1.70 dollars off, which generates 808, 920 dollars in expected
profit (Table 3).
Before running the experiment, the firm historically used a blanketed10% off promotion. This
yields only 330, 278 in profits which is 39.21% of the full personalization benchmark. Thus, opti-
mizing the blanket treatment itself does a sizable amount of work of getting to full personalization
profits. Further allowing for continuous treatments rather than discrete treatments additionally
increases profits.
Second, we then consider the case where the firm offers up to all eight treatments used in the
experiment as possible assigned treatments for segments, and we report it as the discrete treat-
ments benchmark in Figure 5. This benchmark with one segment is just the optimized blanket
treatment among the discrete treatment arms at two dollars off. Substantively, this benchmark
represents the best we can do with policy learning with discrete treatment values because policy
learning only leverages extant treatment arms from the RCT.
For example, to implement this procedure for three segments, we combinatorially search
through the 8 3  = 56 possible combinations of treatments. For each of these treatment combina-
tions, we form segments by assigning the individual to the treatment that produces the highest
expected profits. We calculate total expected profits by summing the profits across the segments.
27Kallus and Zhou (2018) adapt policy learning for continuous treatments, but their reliance on kernel estimation
makes it computationally prohibitive for high-dimensional treatments and large datasets.
26

We then choose the most profitable combination of treatments as the discrete treatments bench-
mark.
From Figure 5, we find that the discrete treatments benchmark does better than segmenting on
covariates, but performs significantly worse than segmenting on consumers’ preferences, optimal
treatment levels, and our coarse personalization solution. These differences demonstrate the
benefit of allowing the treatments to be continuous instead of preselecting the discrete treatment
values. Our coarse personalization solution allows for optimization over the treatment values
themselves; this generates additional profits for the firm and demonstrates the advantage of our
solution over standard policy learning techniques.
6.3.3 Rounded treatment levels
Decimal treatment levels may be impractical in certain domains. To address this, we examine
our coarse personalization solution with rounded treatments. We round at the end of each step
in Algorithm 1 so it only considers rounded treatments when updating. This procedure ensures
that constructed segments are still geared towards profit maximization.
We find that our coarse personalization solution still does well with rounded treatments. Table
4 demonstrates the percentage of expected incremental profits with coarse personalization with
the two rounding procedures (at the integer level). Full personalization with integer treatments
only allows for 26 unique treatments in this setting. Comparing Table 3 to Table 4, we see that
we leave some profits on the table with the rounding procedure.
Figure 7 demonstrates the performance of Algorithm 1 and provides the profit comparisons
for the coarse personalization solution with rounded treatments at the 0.25, 0.5, and 1 (integer
rounding) levels. Our algorithm continues to perform well despite treatment rounding, with
profits rising as more segments are included.
The optimal rounding level of the treatments will ultimately depend on the firm’s application
and how much it is willing to leave profit on the table for more rounded treatments. Thus, even if
the firm only commits to offering rounded treatments, our solution still performs well in forming
segments.
7 Surplus analysis
We now use our coarse personalization methodology to study how the personalization level af-
fects consumer and producer surplus. While it is clear that producer surplus will monotonically
increase as the firm improves its personalization, its effect on consumer surplus is not clear. De-
pending on whether their assigned treatment is above or below their fully personalized treatment,
27

some consumers may experience higher or lower surplus compared to that of full personaliza-
tion. Due to the uncertain effect on consumer surplus, the total surplus may be higher or lower
under coarse personalization than under full personalization. This section provides an empirical
surplus analysis for our application.
To complete the surplus calculation, we need to impose assumptions on the individual val-
uation of the treatments 𝑣𝑖(𝑡𝑖,𝑑). We assume that the consumer values the dollar off coupon at
face value (𝑣𝑖(𝑡𝑖,1) =𝑡𝑖,1) and values the percentage off coupon at the percentage off rate times the
average past promotion spend for an order ( 𝑣𝑖(𝑡𝑖,2) = 𝑡𝑖,2× average past promo spend𝑖). These
valuations match the cost of issuing the promotion for the firm and we can treat the promotion as
a transfer from the firm to the consumer that further stimulates consumer demand. We can now
compute the total surplus (Equation 27) and estimate the change in surplus for each individual
under different levels of coarse personalization compared to the full personalization benchmark.
We defer the complete surplus calculation to Online Appendix Section I.
From Figure 8, we observe that there is a nonmonotonic relationship of consumer surplus
to the number of segments. Figure 8 plots the change in surplus from coarse personalization to
full personalization and Online Appendix Table 5 provides the decomposition. The figure’s lines
represent the bootstrap means and the bands represent one bootstrap standard deviation. Not
surprisingly, producer surplus is always reduced under coarse personalization when compared
to full personalization.
However, consumer surplus is highest when there is one unique treatment ( 𝐿 = 1) and de-
creases as the firm can use more treatments. Consumer surplus drops significantly after four
segments and then drops significantly again after eight segments. The nonmonotonic shifts in
consumer surplus arise because the firm optimizes its segments without explicitly considering
consumer surplus. Given the firm’s control over these assignments, consumers typically cannot
gain substantially at the firm’s expense.
Online Appendix Table 6 demonstrates the surplus decomposition of the change in total sur-
plus into the change in producer surplus and consumer surplus in ten segments (𝐿 = 10) setting.
Each row in the table represents the respective unique treatment in Table 2.
From Tables 2 and 6, we see that most of the customers are assigned to three unique treatments
or segments. In turn, the three segments capture a sizable portion of the expected profit gain
from coarse personalization. As a result, when the firm moves from three to four segments,
it can assign individuals previously unprofitable under the three-segment scenario to the new,
fourth segment. These individuals likely benefited under the three-segment arrangement, which
explains the substantial decline in consumer surplus observed in Figure 8 upon transitioning from
three to four segments.
Our empirical findings corroborate the nonmonotonic relationship between the level person-
28

alization and consumer surplus in Dubé and Misra (2022). We further see that from Figure 8
and Table 5, the consumer surplus gain when assigned a suboptimal treatment dwarfs the loss in
producer surplus. As a result, we see that total surplus is higher with coarser targeting. These
findings differ from the theoretical equilibrium results in Bergemann and Bonatti (2011), which
finds that total surplus increases as advertisers are better able to personalize and meet the needs
of the consumers. Even though our surplus calculation uses a simplified model of the consumer
valuation, our results still recover a complicated nonmonotonic relationship between consumer
surplus and the level of personalization. Future research should utilize panel data for a more rig-
orous surplus calculation as well as examine the long-term effect of personalized promotions on
societal surplus.
Lastly, our surplus framework offers a convenient rule for choosing the number of segments
from a societal perspective. From Figure 8 we see that offering three segments maximizes the total
societal surplus while allowing the firm to recover 99% of full personalization profits. Thus, the
firm may be inclined to offer only three unique treatments and leave1% of the full personalization
profits on the table.
8 Discussion
Beyond our empirical application, where we revisited the traditional segmentation for promo-
tions management, our coarse personalization procedure can be adapted to various other mar-
keting applications. In this section, we provide a handful of settings where our framework can
be used. In some of the examples, the assumption that the treatment vector is nonzero in one
treatment dimension can be relaxed and interactions across treatments can be allowed. However,
in practice, this requires significantly more data to estimate interactions.
In the context of salesforce compensation, managers need to decide which geographic blocks
salespeople should focus on, how much time the salespeople should spend on each visit, and
whether the visits should be in person or over the phone (Misra, 2019). The dimensions of treat-
ment are the salespeople’s time spent and the type of visit. Further, often only a handful of
geographic blocks are assigned to each salesperson (Zoltners and Sinha, 1983). Managers can use
the coarse personalization procedure to design the optimal geographic blocks and visits types to
maximize expected sales profits.
In the “contract externality” setting of Daljord et al. (2016), salesforce managers select a uni-
form commission rate and assign salespeople with heterogeneous performance levels to the con-
tract. “Contract externalities” arise because the composition of the salespeoples will affect the
optimal contract commission rate. Daljord et al. (2016) focus on a one-dimensional contract rate
while our framework allows for a finite dimensional number of contract components.
29

We can also apply our methodology to advertising content design. For instance, Bertrand
et al. (2010) find that modifying advertising elements such as imagery and content significantly
increases loan demand, comparable in effect to changing the loan’s interest rate. If the firm
chooses a few optimized advertisements to coarsely personalize and send out, then the findings
from Bertrand et al. (2010) provide the first step’s results in our procedure. The firm can then use
our coarse personalization solution to determine which optimal advertisements to offer and to
whom they should be sent to.
Our framework can also be used to guide pricing decisions. Chandar et al. (2019) find that
across 40 million Uber rides, riders have heterogeneous preferences over private tipping behav-
ior. If firm managers aim to maximize tip and overall spending from customers but cannot fully
personalize due to fairness concerns, they can assign different geographic blocks of riders going
to the same location the same baseline price and suggested default tip rate. By coarsely person-
alizing, the managers can both increase profits and address fairness concerns: two people in the
same area searching for a ride to the nearest airport will face the same optimized price.
9 Conclusion
Recent advances in estimating heterogeneous treatment effects have made granular, incrementality-
based targeting and personalization feasible. However, firms rarely deploy full personalization in
practice. Implementation costs, fairness considerations, and other operational constraints restrict
personalization to a limited number of segments. We refer to this as the coarse personalization
problem, where firms need to choose what marketing mix to offer and which segments of cus-
tomers to offer it to.
In this paper, we utilize methods from the optimal transport literature to effectively solve the
coarse personalization problem. We propose a two-step approach where the first step estimates
the conditional average treatment effects and the second step solves the constrained assignment
problem. The first step itself is already used in the literature for full personalization. The second
step is a novel application of optimal transport and maps the distribution of conditional average
treatment effects to a set of discrete segments. We advocate for a “personalize then discretize” ap-
proach that forms segments and chooses their assigned marketing mix variables simultaneously,
instead of the traditional “discretize then personalize” approach that sequentially forms segments
and then chooses their assigned marketing mix variables.
To illustrate the practical relevance of our methodology, we present an empirical applica-
tion for promotions management using field experiment data from a food delivery platform. We
find that after forming five optimized segments, the company is able to recoup over 99.5% of its
expected profits under full personalization. Our approach outperforms classical sequential pro-
30

cedures that first segment on covariates or preferences and then form targeting rules. We show
our algorithmic solution is both scalable and easily implementable. These results have direct
managerial implications: We offer a practical way for firms and marketers to optimally segment
and coarsely personalize their marketing mix.
Our methodology is quite general and can be applied for constrained assignment problems
in many settings even outside marketing. With clinical trial data, pharmaceutical companies can
coarsely personalize medicine by finding the best drug and dosage combination. The optimal
transport solution can be adapted to address problems such as teacher assignments with peer
effects or worker allocations to collaborative projects.
Our paper bridges optimal transport theory to practical problems in the social sciences. Opti-
mal transport methods have been utilized in economics for many applications and are surveyed in
Galichon (2016). In computer science, optimal transport has been used for a variety of problems
ranging from training high-dimensional GANs to computer vision (Peyré and Cuturi, 2019). We
use optimal transport as a novel way to solve a practical problem and future research in applying
optimal transport to other problems in social science is already underway.
31

References
Ansari, A. and C. F. Mela (2003): “E-Customization, ”Journal of Marketing Research , 40, 131–145.
Aouad, A., A. N. Elmachtoub, K. J. Ferreira, and R. McNellis(2023): “Market Segmentation Trees, ”Manufacturing
& Service Operations Management , 25, 648–667.
Arora, N., X. Dreze, A. Ghose, J. D. Hess, R. Iyengar, B. Jing, Y. Joshi, V. Kumar, N. Lurie, S. Neslin, S. Sajeesh,
M. Su, N. Syam, J. Thomas, and Z. J. Zhang (2008): “Putting one-to-one marketing to work: Personalization,
customization, and choice, ”Marketing Letters, 19, 305–321.
Ascarza, E. (2018): “Retention Futility: Targeting High-Risk Customers Might be Ineffective, ”Journal of Marketing
Research, 55, 80–98.
Athey, S. and G. Imbens(2016): “Recursive partitioning for heterogeneous causal effects, ”Proceedings of the National
Academy of Sciences of the United States of America , 113, 7353–7360.
Athey, S., J. Tibshirani, and S. W ager (2019): “Generalized random forests, ”Annals of Statistics, 47, 1179–1203.
Bergemann, D. and A. Bonatti (2011): “Targeting in advertising markets: Implications for offline versus online
media, ”RAND Journal of Economics , 42, 417–443.
Bertrand, M., D. Karlan, S. Mullainathan, E. Shafir, and J. Zinman (2010): “What’s Advertising Content
Worth? Evidence from a Consumer Credit Marketing Field Experiment, ” Quarterly Journal of Economics , 125,
263–305.
Bonnet, O., A. Galichon, and M. Shum (2017): “Yogurts Choose Consumers? Identification of Random Utility
Models via Two-Sided Matching, ”SSRN Electronic Journal.
Briesch, R. A. (1997): “Does it matter how price promotions are operationalized?” Marketing Letters, 8, 167–181.
Bucklin, R. E. and S. Gupta (1992): “Brand Choice, Purchase Incidence, and Segmentation: An Integrated Modeling
Approach, ”Journal of Marketing Research , 29, 201.
Bucklin, R. E., S. Gupta, and S. Siddarth (1998): “Determining Segmentation in Sales Response across Consumer
Purchase Behaviors, ”Journal of Marketing Research , 35, 189–197.
Canas, G. and L. Rosasco (2012): “Learning Probability Measures with respect to Optimal Transport Metrics, ” in
Advances in Neural Information Processing Systems, ed. by F. Pereira, C. J. Burges, L. Bottou, and K. Q. Weinberger,
Curran Associates, Inc., vol. 25.
Carlier, G., V. Chernozhukov, and A. Galichon (2016): “Vector quantile regression: An optimal transport ap-
proach, ”Annals of Statistics, 44, 1165–1192.
Chandar, B., U. Gneezy, J. A. List, and I. Muir (2019): “The Drivers of Social Preferences: Evidence from a Nation-
wide Tipping Field Experiment, ”SSRN Electronic Journal.
Chiong, K. X., A. Galichon, and M. Shum (2016): “Duality in dynamic discrete-choice models, ” Quantitative Eco-
nomics, 7, 83–115.
Cui, T. and M. Hamilton(2022): “Optimal Feature-Based Market Segmentation and Pricing, ”SSRN Electronic Journal.
Daljord, Ø., M. Hu, G. Pouliot, and J. Xiao (2019): “The Black Market for Beijing License Plates, ”SSRN Electronic
Journal.
Daljord, Ø., S. Misra, and H. S. Nair (2016): “Homogeneous contracts for heterogeneous agents: Aligning sales
force composition and compensation, ”Journal of Marketing Research , 53, 161–182.
32

Dubé, J.-P. and S. Misra (2022): “Personalized Pricing and Consumer Welfare, ”Journal of Political Economy .
Duvvuri, S. D., A. Ansari, and S. Gupta(2007): “Consumers’ Price Sensitivities Across Complementary Categories, ”
Management Science, 53, 1933–1945.
Ellickson, P. B., W. Kar, and J. C. Reeder (2022): “Estimating Marketing Component Effects: Double Machine
Learning from Targeted Digital Promotions, ”Marketing Science.
Farrell, M. H., T. Liang, and S. Misra (2020): “Deep Learning for Individual Heterogeneity, ” .
——— (2021): “Deep Neural Networks for Estimation and Inference, ”Econometrica, 89, 181–213.
Galichon, A. (2016): Optimal Transport Methods in Economics .
Galichon, A. and B. Salanie(2012): “Cupid’s Invisible Hand: Social Surplus and Identification in Matching Models, ”
SSRN Electronic Journal.
Gilmore, J. H. and B. J. I. Pine (1997): “The Four Faces of Mass Customization, ”Harvard Business Review.
Grover, R. and V. Srinivasan(1987): “A Simultaneous Approach to Market Segmentation and Market Structuring, ”
Journal of Marketing Research , 24, 139.
Gupta, S. and P. K. Chintagunta (1994): “On Using Demographic Variables to Determine Segment Membership in
Logit Mixture Models, ”Journal of Marketing Research , 31, 128.
Harvard Business Review Analytic Services (2018): “The Age of Personalization, ”Harvard Business Review.
Hitsch, G. J., S. Misra, and W. W. Zhang (2024): “Heterogeneous treatment effects and optimal targeting policy
evaluation, ”Quantitative Marketing and Economics .
Imbens, G. W. and D. B. Rubin (2015): Causal Inference for Statistics, Social, and Biomedical Sciences , Cambridge
University Press.
Jain, D., F. M. Bass, and Y.-M. Chen (1990): “Estimation of Latent Class Models with Heterogeneous Choice Proba-
bilities: An Application to Market Structuring, ”Journal of Marketing Research , 27, 94.
Kahneman, D., J. L. Knetsch, and R. Thaler (1986): “Fairness as a Constraint on Profit Seeking: Entitlements in
the Market, ”The American Economic Review, 76, 728–741.
Kallus, N. and A. Zhou (2018): “Policy Evaluation and Optimization with Continuous Treatments, ” inProceedings
of the Twenty-First International Conference on Artificial Intelligence and Statistics , ed. by A. Storkey and F. Perez-
Cruz, PMLR, vol. 84 of Proceedings of Machine Learning Research , 1243–1251.
Kamakura, W. A. and G. J. Russell (1989): “A Probabilistic Choice Model for Market Segmentation and Elasticity
Structure, ”Journal of Marketing Research , 26, 379.
Kennedy, E. H. (2020): “Optimal doubly robust estimation of heterogeneous causal effects, ” .
Kotler, P. and K. L. Keller (2014): Marketing Management, Pearson, 15 ed.
Krieger, A. M. and P. E. Green (1996): “Modifying Cluster-Based Segments to Enhance Agreement with an Exoge-
nous Response Variable, ”Journal of Marketing Research , 33, 351.
Lloyd, S. P. (1982): “Least Squares Quantization in PCM, ”IEEE Transactions on Information Theory , 28, 129–137.
Lu, Y. and H. H. Zhou (2016): “Statistical and Computational Guarantees of Lloyd’s Algorithm and its Variants, ” .
Misra, S. (2019): “Selling and sales management, ” inHandbook of the Economics of Marketing , Elsevier B.V., 441–496.
33

——— (2021): “Algorithmic Nudges, ” .
Paszke, A., S. Gross, F. Massa, A. Lerer, J. Bradbury, G. Chanan, T. Killeen, Z. Lin, N. Gimelshein, L. Antiga,
A. Desmaison, A. Köpf, E. Y ang, Z. DeVito, M. Raison, A. Tejani, S. Chilamkurthy, B. Steiner, L. Fang, J. Bai,
and S. Chintala (2019): “PyTorch: An imperative style, high-performance deep learning library, ” Advances in
Neural Information Processing Systems , 32.
Peyré, G. and M. Cuturi (2019): “Computational Optimal Transport, ”Computational Optimal Transport.
Pollard, D.(1982): “Quantization and the Method of k-Means, ”IEEE Transactions on Information Theory, 28, 199–205.
Rafieian, O. and H. Yoganarasimhan (2021): “Targeting and Privacy in Mobile Advertising, ” Marketing Science,
40, 193–218.
Rossi, P. E., R. E. McCulloch, and G. M. Allenby (1996): “The value of purchase history data in target marketing, ”
Marketing Science, 15, 321–340.
Rust, R. T. and P. C. Verhoef (2005): “Optimizing the Marketing Interventions Mix in Intermediate-Term CRM, ”
Marketing Science, 24, 477–489.
Santambrogio, F. (2015): Optimal Transport for Applied Mathematicians , vol. 87.
Shaffer, G. and Z. J. Zhang (1995): “Competitive Coupon Targeting, ”Marketing Science, 14, 395–416.
Sheshinski, E. and Y. Weiss(1977): “Inflation and costs of price adjustment, ”Review of Economic Studies, 44, 287–303.
Simester, D., A. Timoshenko, and S. I. Zoumpoulis (2020): “Efficiently evaluating targeting policies: Improving on
champion vs. Challenger experiments, ”Management Science, 66, 3412–3424.
Smith, W. R. (1956): “Product Differentiation and Market Segmentation as Alternative Marketing Strategies, ”Journal
of Marketing, 21, 3.
Swaminathan, A. and T. Joachims (2015): “Batch Learning from Logged Bandit Feedback through Counterfactual
Risk Minimization, ”Journal of Machine Learning Research , 1731–1755.
Villani, C. (2009): Optimal Transport, vol. 338 ofGrundlehren der mathematischen Wissenschaften, Berlin, Heidelberg:
Springer Berlin Heidelberg.
W ager, S. and S. Athey (2018): “Estimation and Inference of Heterogeneous Treatment Effects using Random
Forests, ”Journal of the American Statistical Association , 113, 1228–1242.
Wind, Y. (1978): “Issues and Advances in Segmentation Research, ”Journal of Marketing Research , 15, 317–337.
Yoganarasimhan, H., E. Barzegary, and A. Pani (2022): “Design and Evaluation of Optimal Free Trials, ”Manage-
ment Science.
Zhang, J. and L. Krishnamurthi(2004): “Customizing Promotions in Online Stores, ”Marketing Science, 23, 561–578.
Zhang, J. and M. Wedel (2009): “The Effectiveness of Customized Promotions in Online and Offline Stores, ”Journal
of Marketing Research, 46, 190–206.
Zhang, W. W. (2023): “Optimal Comprehensible Targeting, ” .
Zhou, Z., S. Athey, and S. W ager(2022): “Offline Multi-Action Policy Learning: Generalization and Optimization, ”
Operations Research.
Zoltners, A. A. and P. Sinha (1983): “Sales Territory Alignment: A Review and Model, ” Management Science, 29,
1237–1256.
34

Figures
Distribution of treatment effects Discrete treatments
(Segments)(Individuals)
Assigned treatment Segment size
Figure 1: Semidiscrete optimal transport
Note: This figure provides a stylized visualization of the semidiscrete optimal transport problem introduced in Sec-
tion 3.2 (Equation 7). In our setup, the allowable couplings 𝜋 are the assignment rule from the distribution of treat-
ment effects (𝑃) to the discrete distribution of segments (𝑄 ˜t,q) with assigned treatments ˜t ={t1,..., t5}. This figure
represents the one-dimensional case where the distribution of treatment effects is discretized into five different seg-
ments (𝐿 = 5), and the discrete distribution represents a coarsened version of the continuous distribution. The
optimal transport solution (𝜋) “pushes forward” the treatment effect distribution to their assigned segments. The
mathematics behind optimal transport are detailed in Appendix Section A.
ti,2
Start with ˜tk
ti,1
ti,2
ti,1
ti,2
ti,1
Expansion:
- Compute Voronoi Cells
- Compute Barycenters {(t′ l,1,t′ l,2)}L l=1
Reduction:
- Force feasibility constraint
E[Ri|xi,t′ l,1,0]
E[Ri|xi,0,t′ l,2]
(t′ l,1,t′ l,2)
Update:
- Update to  ˜tk+1
- Recompute Voronoi Cells
T erminate when  is close enough to ˜tk+1 ˜tk
Figure 2: Adapted Lloyd’s Algorithm (𝐷 = 2)
Note: This figure provides a stylized visualization of Algorithm 1 with two-dimensional treatments(𝐷 = 2) and three
segments (𝐿 = 3). The horizontal axis represents the treatment values for the first dimension and the vertical axis
represents that of the second dimension. The points on the axes represent the three segments’ assigned treatment
values 𝒕𝑙 ={t1, t2, t3}. The interior points represent the individuals’ optimal treatment values (𝑡∗ 𝑖,𝑑,𝑡∗ 𝑖,𝑑). The lines
represent the Voronoi Cells’ (or segments’) boundaries. The square points represent the Barycenter (or offered
treatment) of each cell. An outline of the algorithm is provided in Appendix Section E.
35

4.75
5.00
5.25
5.50
5.75
6.00
0 2 3 4 5
Treatment value (dollar off)
Profits (28 Days)
4.75
5.00
5.25
5.50
5.75
6.00
0 5 10 15 20
Treatment value (percentage off)
Profits (28 Days)
Note: The bars represent one standard deviation. Profits (28 days) are the average profits per customer 28 days after
the promotion was issued. The profits are defined as sales minus promotional costs in Equation 12.
Figure 3: Profits by treatment
0
2
4
6
8
2 3 4 5
Treatment value (dollar off)
CATE (post 28 days sales)
−2
0
2
4
5 10 15 20
Treatment value (percentage off)
CATE (post 28 days sales)
Figure 4: Continuous CATE densities for sales
36

790
800
810
820
830
840
1 2 3 4 5 6 7 8 9 10
Number of segments
Expected Incremental Profits (Thousands of USD)
Segmentation Procedure
Discrete Treatments
Covariates xi
Preferences β(xi)
Opt. Treatment Levels t ∗ (xi)
Coarse Personalization t~(t ∗ (xi))
Full Personalization
Note: Lines show bootstrap means and shaded bands show one bootstrap standard deviation. The full personalization
profits band reflects the sampling variation across the 100 bootstrap iterations. The full personalization benchmark
represents issuing 2, 206 unique treatments when rounded to three significant figures.
Figure 5: Profit comparisons
Note: The optimal treatment values (𝑡∗ 𝑖,1,𝑡∗ 𝑖,2) for each individual is plotted for the dollar off and percentage off
promotions. The colors represent each individual’s assigned treatment. The triangular points indicate those
individuals who are assigned a percentage off treatment and the circular points represents the those who are
assigned a dollar off promotion. The assigned treatments’ values are in the legend and in Table 2. The incremental
expected profits generated from the treatment assignments for each individual is plotted on the vertical axis. A
horizontal plane plotted at zero expected profits is provided as guide.
Figure 6: Treatment assignments (𝐿 = 10 treatments)
37

790
800
810
820
830
840
1 2 3 4 5 6 7 8 9 10
Number of segments
Expected Incremental Profits (Thousands of USD)
Rounding
0.25
0.5
1
Coarse Personalization
Full Personalization
Note: Lines show bootstrap means and shaded bands show one bootstrap standard deviation. The full personalization
profits band reflects the sampling variation across the100 bootstrap iterations. The 0.25, 0.5, 1 benchmarks represent
the coarse personalization solution with treatments rounded at those respective levels. The coarse personalization
benchmark is rounded to three significant figures. The full personalization benchmark represents issuing 2, 206
unique treatments when rounded to three significant figures.
Figure 7: Profit comparisons for coarse personalization with rounded treatments
−20
0
20
40
1 2 3 4 5 6 7 8 9 10
Number of segments
Change in surplus from full personalization (Thousands of USD)
Surplus
∆Consumer Surplus
∆Producer Surplus
∆Total Surplus
Note: Lines show bootstrap means and shaded bands show one bootstrap standard deviation.
Figure 8: Surplus decomposition across treatments
38

Tables
Table 1: Average treatment effects on profits
Treatment value ATE ($) SE 𝑡-stat 𝑝-value
Dollar off
2 0.034 0.046 0.730 0.465
3 0.061 0.046 1.326 0.185
4 0.122 0.047 2.605 0.009
5 0.085 0.049 1.722 0.085
Percentage off
5 0.056 0.045 1.225 0.220
10 0.078 0.047 1.659 0.097
15 0.153 0.047 3.220 0.001
20 0.096 0.045 2.101 0.036
Note: The outcome variable is profits 28 days after sending out the treatment. The average treatment effects (ATEs)
are estimated from the Causal Forest comparing each treatment arm to the holdout set of issuing no promotion and
represents the treatment effect on profits. The reported𝑡-statistic and the𝑝-value are for a two-sided Welch’s𝑡-test
against the null hypothesis that the ATE for each promotion is 0.
Table 2: Treatment assignments (𝐿 = 10)
Treatment (𝑙) Dimension (𝑑) Value ( 𝑡𝑖,𝑑) 𝑁
1 Percentage 12.45 7,090
2 Dollar 1.67 556,544
3 Percentage 20.00 7,375
4 Dollar 2.15 54,253
5 Percentage 8.42 12,816
6 Dollar 2.79 15,532
7 Dollar 1.83 214,631
8 Dollar 1.24 30,425
9 Percentage 5.17 9,234
10 Dollar 1.54 295,479
Note: The table lists the ten segments in Figure 6. The segments’ assigned treatment and size are provided.
39

Table 3: Expected incremental profits by segmentation method
Profits by segmentation method ($)
Number of segments (𝐿) Covariates Preferences Optimal treatment levels Coarse personalization
1 808,920 808,920 808,920 808,920
2 808,940 814,377 812,609 829,300
3 808,969 815,851 824,710 834,085
4 809,021 826,215 826,581 836,669
5 809,114 827,432 828,205 838,450
6 809,156 828,159 828,766 839,417
7 809,190 828,568 828,970 839,954
8 809,226 828,817 829,159 840,412
9 809,247 828,929 829,243 840,761
10 809,277 829,429 829,315 840,985
(a) Profit by segmentation method and number of segments
Benchmark Profits ($)
Firm’s blanket promotion (10% off) 330,278
Optimal experimented blanket promotion ($2) 789,868
Optimal blanket promotion ($1.70) 808,920
Full personalization 842,366
(b) Benchmark profit comparisons
Note: The firm’s most recent blanket promotion was 10% off. The optimal experimented blanket promotion is a $2
off promotion. The optimal blanket promotion allowing for continuous treatments is a $1.70 promotion. When
rounded to three significant figures, full personalization issues 2,206 unique promotions.
Table 4: Expected incremental profits by the number of segments (rounded integer treatments)
Number of segments (𝐿) Profits ($) Percent to integer-rounded
full personalization(%)
1 789,868 96.50
2 809,849 98.95
3 812,964 99.33
4 814,335 99.49
5 816,677 99.78
6 817,753 99.91
7 818,116 99.96
8 818,265 99.97
9 818,394 99.99
10 818,471 100.0
Full personalization (26) 818,481 –
Note: Full personalization with rounded integer treatments involves issuing 26 unique treatments.
40

Appendix
A Mathematics of Coarse Personalization
In this section, we present a mathematical overview of coarse personalization, including the op-
timal transport techniques underlying our solution. We provide a canonical example used in the
optimal transport literature to introduce the general framework. Then we link it to our promo-
tions management setting from our empirical application. We direct readers to Galichon (2016),
Santambrogio (2015), and Villani (2009) for a more formal introduction to optimal transport.
In essence, optimal transport is the study of moving mass from one distribution to another
while minimizing an established cost function. These two distributions can be continuous or
discrete. The solution to the optimal transport problem provides an optimal transport plan that
describes how the mass is moved. The optimal transport plan pushes forward the mass from one
distribution to the other distribution.
For a concrete example, we can first consider the canonical example of physically moving
earth. This optimal transport problem determines the best way to move ore from mines to facto-
ries. The optimal transport plan then details both how much ore is moved from each mine and
where the ore is sent. An optimal transport mapping is a subset of possible optimal transport
plans where all the mass from one mine is sent to a factory. In other words, under the map-
ping, the mines cannot split mass by sending half of their ore to one factory and the other half
to another factory. The optimal transport plan allows for probabilistic assignment of mines to
factories, while the optimal transport mapping allows only deterministic assignment from mines
to factories.
In practice, the number of mines and factories are discrete, but theoretically the results for the
earth moving example can be extended to continuous distributions of mines and/or factories. In
the continuous distribution to continuous distribution case, the optimal transport plan matches
segments of one distribution’s cumulative distribution function onto that of the other.
In our promotions management setting, we replace mines with a continuous distribution of
the heterogeneous treatment effects across the individuals in our data that we had estimated from
the field experiment (Section 3.1). We replace factories with discrete segments (or number of treat-
ments) that the firm decides to assign. Thus, we have a continuous-discrete (or a semidiscrete)
optimal transport problem. Since the treatments, or promotions, can be dollar off or percentage
off, we are mapping a two-dimensional continuous distribution to discrete segments.
Our coarse personalization problem in Equation 8 has two nested problems. The inner prob-
lem is the optimal transport problem where the segment assignments are formed. The outer
problem chooses the treatment levels to assign for each segments as well as their size.
41

We focus on the inner problem that is the optimal transport problem (Equation 7). We define
𝑃 as the distribution of heterogeneous treatment effects, ˜t = {˜𝒕1, ˜𝒕2,..., ˜𝒕𝐿} as the 𝐿 points or
assigned treatments for the segments, and q ={𝑞𝑙}𝐿 𝑙=1 as the normalized segment size. More
formally, the assigned treatments for the segments are distributed by𝑄 ˜𝑡,𝑞 where each treatment
˜𝒕𝑙 has probability mass 𝑞𝑙 such that ˝𝐿 𝑙=1𝑞𝑙 = 1. Both distributions are over the space of real
numbers.
In this setup, we want to map the continuous distribution of heterogeneous treatment effects
to the discrete distribution of𝐿 treatments (or segments). The probability mass 𝑞𝑙 for treatment
˜𝒕𝑙 represents the normalized number of individuals assigned to treatment𝑙∈𝐿. In the marketing
framework, we let the 𝐿 different treatments form 𝐿 different segments where each segment is
assigned treatment 𝒕𝑙 and𝑞𝑙 describes the size of segment𝑙∈𝐿. The distribution of heterogeneous
treatment effects is estimated using a field experiment or observational data.
We define acoupling as a mapping that, given an individual’s level of heterogeneous treatment
effect, assigns that person to a specific treatment. These couplings form the optimal transport
plan between two distributions and inform how the mass is moved across the two. In our setup,
the coupling is the assignment rule of individuals to segments.
More formally, following Galichon (2016), we letX∼ 𝑃 andY∼ 𝑄 ˜t,q where𝑃 and𝑄 ˜t,q are
the underlying distributions. Then the set of couplings over the probability distributions 𝑃 and
𝑄 ˜t,q is the set of probability distributionsX×Y with first and second marginal distributions as𝑃
and𝑄 ˜t,q. The set of couplings is defined asM(𝑃,𝑄 ˜t,q). Thus, a probability measure𝜋 overX×Y
is inM(𝑃,𝑄 ˜t,q) if and only if𝜋(𝐴×Y) =𝑃(𝐴) and𝜋(X× 𝐵) =𝑄 ˜t,q(𝐵) for every subset𝐴⊆X
and𝐵⊆Y . Then a random pair(𝑋,𝑌)∼ 𝜋 where𝜋∈M( 𝑃,𝑄 ˜t,q) is a coupling of𝑃 and𝑄 ˜t,q.
For a coupling(𝑋,𝑌) where𝑌 =𝑇(𝑋) is a deterministic function of𝑋, the transport plan𝑇(·)
will be a transport map. This is also known as pure assignment or a Monge coupling or mapping.
The map implies that for individuals with specific values of𝑥∈𝑋 , they will be assigned to only
one segment and not be probabilistically assigned to many segments.
The Monge problem finds the optimal pure assignments to minimize a cost function,
min
𝑇(·)
𝐸𝑃[𝐶(𝑋,𝑇(𝑋))] (17)
s.t.𝑇 #𝑃 =𝑄 ˜𝑡,𝑞, (18)
where 𝐶(𝑋,𝑌) is the cost function and 𝑇 #𝑃 is the push-forward of probability 𝑃 by map 𝑇 .
𝑇 #𝑃 = 𝑄 ˜𝑡,𝑞 is defined such that if 𝑋 ∼ 𝑃, then 𝑇(𝑋) ∼𝑄 ˜𝑡,𝑞. The cost function specifies the
cost of transporting mass from𝑋 to𝑌 . In our setting, it represents the lost profits from to coarse
personalization compared to full personalization (Equation 11).
In general, the Monge problem may not have a solution. Instead we can relax the problem to
42

attain the Monge-Kantorovich problem. The Monge-Kantorovich problem is
min
𝜋∈M(𝑃,𝑄 ˜𝑡,𝑞) 𝐸𝜋[𝐶(𝑋,𝑌)], (19)
where the couplings𝜋 are optimized over instead of the pure assignments𝑇(·) from the Monge
problem. The relaxation to the Monge problem implies that the optimal couplings may require
that some individuals are probabilistically assigned to, or to split mass across, different segments.
Under some conditions, the Monge-Kantorovich problem produces the same solution as the
Monge problem and the optimal transport plan is the same as the optimal transport map. In our
setting, this implies that segment assignments of individuals to treatments are deterministic. In
our semidiscrete optimal transport problem, we show in Proposition 3 that the coarse person-
alization problem is strictly convex in the treatment values. The strict convexity implies that
a solution to the optimal transport problem will exist and that we will have a pure assignment
of individuals to segments (Corollary 4). The former is provided from Theorem 2.2 in Galichon
(2016). The latter is a result from convex analysis using Rademacher’s Theorem. Thus, this result
implies that we attain a deterministic mapping of individuals to their assigned segments: Each
individual will only be mapped to one segment.
B Proofs for Section 3.2
We provide proofs for Proposition 3 and Corollary 4 in Section 3.2.
Proposition. Under Assumptions 1 and 2, 𝐸𝜋[𝐶(𝑋,𝑇)] is strictly convex in ˜𝒕.
Proof. From Assumptions 1 and 2, the firm’s program in Equation 6 is strictly concave. Because
𝐸[𝑌𝑖|𝒙𝑖, 0,..., 0,..., 0] is a constant with regards to ˜𝒕 and 𝒒, 𝐸[𝑅𝑖|𝒙𝑖, ˜𝑡𝑖,1,..., ˜𝑡𝑖,𝑑,..., ˜𝑡𝑖𝐷] is then
strictly concave and so isR𝑖(𝒙𝑖, ˜𝒕𝑙) by construction. Since ¯𝑅𝑖 is a constant with regards to ˜𝒕 and
𝒒, we have that( ¯𝑅𝑖−R 𝑖(𝒙𝑖, ˜𝒕𝑙)) is strictly convex.
We choose𝜙(·) to be a convex and strictly increasing function for all 𝑡,𝑡′∈ R+ and let𝛼∈
[0, 1]. Then, for some strictly convex function 𝑓 : R+→ R+,
𝜙𝑓(𝛼𝑡+( 1−𝛼)𝑡′) <𝜙𝛼𝑓(𝑡)+( 1−𝛼)𝑓(𝑡′)≤𝛼𝜙 𝑓(𝑡)+( 1−𝛼)𝜙𝑓(𝑡′) (20)
where we used that𝜙(·) is strictly increasing in the first inequality and then used that𝜙(·) is con-
vex in the second inequality. Choosing𝜙(𝑥) =𝑥2, we see that(R𝑖(𝒙 𝒊, ˜𝒕𝑙)− ¯𝑅𝑖)2 =( ¯𝑅𝑖−R𝑖(𝒙𝑖, ˜𝒕𝑙)) 2
is strictly convex and so is˝𝑁 𝑖 ( ¯𝑅𝑖−R𝑖(𝒙𝑖, ˜𝒕𝑙)) 2 =|R(𝒙, ˜𝒕𝑙)− ¯𝑹|2. Lastly,˝𝐿 𝑙=1𝑞𝑙𝐸𝜋[𝐶(𝑋,𝑇)|𝑇 = ˜𝒕𝑙]
is a convex combination of strictly convex functions with convex weights 𝒒. Thus, 𝐸𝜋[𝐶(𝑋,𝑇)]
is strictly convex in ˜𝒕. □
43

Corollary. Under Assumptions 1 and 2, the optimal transport plan 𝜋 that solves Equation 8 deter-
ministically maps individuals to their segment.
Proof. Our coarse personalization problem collapses to a convex optimization problem by Propo-
sition 3. Since we are solving a convex program over a closed interval, our cost function is
bounded from below. Theorem 2.2 from Galichon (2016) establishes that the solution to the
Monge-Kantorovich problem in Equation 7 exists. Further, Rademacher’s Theorem implies that
the set of non-differentiable points of the convex function will be Lebesgue measure zero, and
thus can be ignored under a continuous 𝑃. In our framework, the non-differentiable points are
those that split mass between two segments. Thus, Rademacher’s Theorem guarantees that we
have a pure assignment of individuals to segments and achieve a Monge mapping as a part of our
solution. Equivalently, individuals are only mapped to one segment. □
44

Online Appendix
C Incorporating the cost of additional segments
In our setup, the number of segments𝐿 is a free parameters that the firm can tailor to its setting.
Alternatively, we can explicitly account for the cost of forming more segments by adapting our
cost function to include a term that depends on the number of segments.28 By doing so, our coarse
personalization solution can outperform full personalization due to extra cost from forming too
many segments. We can define
𝐸𝜋[𝐶(𝑋,𝑌)|𝑡 = ˜𝒕𝑙] =

R( 𝒙, ˜𝒕𝑙)− ¯𝑹

2+𝜓(𝐿), (21)
where𝜓(𝐿) represents the cost of issuing 𝐿 different segments. To ensure there is a solution to
the problem when optimizing to𝐿, we assume that𝜓(𝐿) is weakly convex in𝐿. This encompasses
a wide class of functions, which include constant, linear 𝜓(𝐿) = 𝛿𝐿, and quadratic 𝜓(𝐿) = 𝛿𝐿 2
cost formulations with𝛿≥ 0.
In our analysis, we consider the case where𝜓(𝐿) = 0 or there is no additional cost of forming
additional segments. This is the most conservative case for evaluating our coarse personalization
solution because full personalization will be an upper bound of our solution.
D Coarse personalization problem’s first order condition
At the coarse personalization solution, the marginal effect of promotional treatment is equated
to the marginal cost of treatment across for each segment. We now derive this result from the
first order condition of the coarse personalization problem (Equation 8).
We define(˜𝒕∗, 𝒒∗) be the solution to the optimal transport problem. Treatments are feasible
so ˜𝒕∗ is a𝑑-dimensional treatment that is only nonzero in one dimension. From Equation 8, the
objective function at the optimum is
W( ˜𝒕∗, 𝒒∗) =
𝐿∑︁
𝑙=1
𝑞∗ 𝑙𝐸𝜋[𝐶(𝑋,𝑇)|𝑇 = ˜𝒕∗ 𝑙], (22)
and optimality to ˜𝒕 implies that the first order condition is
𝜕W( ˜𝒕, 𝒒)
𝜕˜𝒕𝑙

(˜𝒕∗,𝒒∗)
= 0 = 𝜕(R( 𝒙, ˜𝒕𝑙)) 𝜕˜𝒕𝑙

(˜𝒕∗,𝒒∗)
. (23)
28We thank an anonymous reviewer for this suggestion.
45

Without loss of generality, we let treatment ˜𝒕𝑙 be nonzero in dimension 𝑑. Then, R( 𝒙, ˜𝒕𝑙) =
𝐸𝜋[R|𝒙,𝑇1 = 0,...,𝑇 𝑑 = ˜𝑡𝑖,𝑑,...,𝑇 𝐷 = 0] and we define R, 𝒀, and 𝒄𝑑(˜𝑡𝑑) to be the vectors of 𝑅𝑖,𝑌𝑖
and𝑐𝑑( ˜𝑡𝑑) across individuals𝑖∈{ 1,...,𝑁 } respectively. We then attain
0 = 𝜕(𝐸𝜋[R|𝒙,𝑇1 = 0,...,𝑇 𝑑 = ˜𝑡𝑑,...,𝑇 𝐷 = 0]) 𝜕˜𝑡𝑙,𝑑
= 𝜕(𝐸𝜋[𝒀|𝒙, 0,..., ˜𝑡𝑑,..., 0]) 𝜕˜𝑡𝑙,𝑑 − 𝜕𝐸𝜋[𝒄𝑑(˜𝑡𝑑)] 𝜕˜𝑡𝑙,𝑑
𝜕(𝐸𝜋[𝒀|𝒙, 0,..., ˜𝑡𝑖,𝑑,..., 0])
𝜕˜𝑡𝑙,𝑑
|                              {z                              }
Average marginal effect
= 𝜕𝐸𝜋[𝒄𝑑(˜𝑡𝑑)] 𝜕˜𝑡𝑙,𝑑
|         {z         }
Average marginal cost
. (24)
The first order condition implies that the optimal treatment should be chosen such that for all
individuals assigned to a segment, the average marginal effect of the segment’s assigned treat-
ment is equal to the average marginal cost of issuing that treatment. For example, if treatments
were prices, this would be equating the marginal revenue to marginal cost across each assigned
group. Under full personalization, at the individual level, the marginal effect of treatment is set
to its marginal cost. Thus, our coarse personalization solution generalizes the individual-level
equivalence of marginal effects to marginal cost to an average-level equivalence within a seg-
ment. Our results generalize the economic intuition for a one-dimensional continuous treatment
to𝐷-dimensional continuous treatments.
E Outline of Algorithm 1
Initially (Step 0), we guesses the initial treatment values as well as their dimension of treatment.
For an example in promotions management, we can consider three segments to assign where
the two-dimensional treatments are dollar off and percentage off promotions. We further ini-
tially guess treatment values with one dollar off, two dollars off and five percent off for the three
segments.
For each iteration of the algorithm (Step k), we first compute the costs from Equation 9 for
assigning individuals to each offered treatment to form the segments. In our running example,
this would mean computing the expected profits loss to full personalization for each person if
they were assigned to each of the three treatment values of one dollar off, two dollars off and five
percent off. We then assign each individual the treatment that leads to the lowest lost (profits or
cost), and these form the Voronoi Cell (or segment) for each assigned treatment.29 In our running
29In the standard setting where there are less treatments than individuals ( 𝐿≪ 𝑁 ), Algorithm 1 will not assign
duplicate treatments that are the same in treatment value and dimension unless the initial treatments are the same.
46

example, those who are more profitable when given a one dollar off promotion than with the other
two promotions will form the Voronoi Cell (or segment) for the treatment of one dollar off. Thus,
the computation of the Voronoi Cells establishes the assignments for each offered promotions
and these cells themselves are the segments of the customer base.
After the Voronoi Cells are formed, we then compute the cells’ mean of the optimal treatment
values(𝑡∗ 𝑖,𝑑) for each dimension and across the assigned individuals. For the individuals in the
Voronoi Cell formed for the one dollar off treatment, we compute the average of the individual
optimal treatments for both the dollar off and percentage off dimensions. These average values
are the Barycenter of each of the Voronoi Cells and represent the candidate treatment values for
each segment.
Treatments must be feasible, or they can only be nonzero in one dimension. Thus, we need
a dimension-reduction step where we determine which treatment dimension in each Barycenter
to offer. We choose the treatment dimension that produces a higher profit across each dimension
and then set that value as the candidate treatment value for the next iteration of the algorithm. In
our running example, for the one dollar off promotion’s Voronoi Cell, suppose we have that the
Barycenter’s value is 1.5 dollars off and two percentage off. We then evaluate the expected total
profits for those in the cell for the two separate treatments of 1.5 dollars off and two percentage
off and choose the one that yields higher expected profits. This treatment, say 1.5 dollars off, is
the new candidate treatment value for this cell.
We iterate the steps of the algorithm until the treatment values update steps are minuscule
and the treatment dimensions do not change in successive iterations. In our application, we set
the tolerance for changes in the treatment values to 10−6 as the termination criterion for the
algorithm.
F Grid search details
F.1 Grid search implementation
We first describe how we implemented the grid search. To begin, we create the set of possible
feasible treatments. The encompasses looking across possible treatment values and treatment
dimensions for these treatments. We then choose 𝐿 different feasible treatments from this set,
t ={𝒕1, 𝒕2,..., 𝒕𝐿}. For each of the proposed treatments in the set ( 𝒕𝑙), we compute the coun-
terfactual profits for assigning the treatment to each individual. We assign individuals to their
However, If two identical treatments are initially supplied, then one iteration of the algorithm will lead to the dupli-
cate treatments to form an empty Voronoi Cell since those individuals are already assigned to the first instance of
the treatment. If the initial treatments are different, then the algorithm will not update such that two treatments are
assigned to the same treatment value and dimension because doing so will not be profit maximizing.
47

profit-maximizing treatment to form segments. We then compute total profits from this person-
alization strategy.
To speed this process up, we use the Broyden-Fletcher-Goldfarb-Shanno Algorithm (BFGS) to
select the treatment values instead of iterating through all possible values in the grid. However,
we still need to iterate through possible dimensions of treatment. To give a concrete example, we
can consider the following example for forming five segments with two dimensional treatments.
We define placeholder treatment values𝑡𝑑1 or𝑡𝑑2 for each dimension𝑑1,𝑑 2. These represent
the nonzero treatment value in dimension 𝑑1,𝑑 2 for their respective treatment vector. For five
segments there are six combinations across the two treatment dimensions when forming the
feasible treatment set t ={𝒕1, 𝒕2,..., 𝒕𝐿}:{𝑡𝑑1,𝑡𝑑1,𝑡𝑑1,𝑡𝑑1,𝑡𝑑1},{𝑡𝑑1,𝑡𝑑1,𝑡𝑑1,𝑡𝑑1,𝑡𝑑2},{𝑡𝑑1,𝑡𝑑1,𝑡𝑑1,𝑡𝑑2,𝑡𝑑2},
{𝑡𝑑1,𝑡𝑑1,𝑡𝑑2,𝑡𝑑2,𝑡𝑑2}, and{𝑡𝑑1,𝑡𝑑2,𝑡𝑑2,𝑡𝑑2,𝑡𝑑2}.30 For each combination, the treatment values (𝑡𝑑1,𝑡𝑑2)
are then searched for via BFGS and we iterate over these six combinations to find the profit-
maximizing set of treatments and their segments.
F.2 Why Algorithm 1 is computationally efficient
To quantify the difference between the brute-force approach and Algorithm 1, we benchmark
runtimes for the grid search and Algorithm 1 using our empirical application in Section 6. We
use personal desktop with an Intel i5-8259U CPU @ 2.30GHz processor that has four cores/eight
threads and implement the back end of the calculations in R’s torch CPU wrapper package of
PyTorch (Paszke et al., 2019). To speed up the grid search, we use the standard BFGS optimizer
to select the offered treatments levels (t𝑙) in each dimension of treatment and assign individuals
to the segment that optimizes expected profits for that individual. We then cycle through all the
possible treatment dimensions and choose the most profitable segments.
For over 1.2 million individuals, two dimensional promotions (dollar and percentage off), and
for five unique promotions issued, we find that our proposed Algorithm 1 solves the coarse per-
sonalization problem in 14 seconds. In contrast, the brute force approach takes 515 seconds and
we see around a 37 times improvement in computational speed. From our prior analysis of the
run time of the two procedures in Section 4.2, we anticipate this gap in performance between the
two to only increase in higher dimensions and when more segments are required.
The reasons for the dramatic difference in speed are twofold. First, the brute-force approach’s
long runtime is due to the curse of dimensionality. Even with a handful of treatment dimensions
this is evident: In the case of issuing five unique treatments with two dimensions of treatment,
the brute-force approach needs to search over six sets of possible treatments offered. Similarly,
for issuing three unique treatments with three dimensions of treatment, the brute-force approach
30The first set represents a set of only treatments offered in the first dimension, the second set represents a set
with four treatments offered in the first dimension and one in the second dimension, etc.
48

needs to search over nine different sets of possible treatments offered. Algorithm 1 avoids this
issue because the treatment dimensions are chosen along with treatment values in each iteration
of the algorithm.
Second, the treatment values’ update rule in Algorithm 1 is computationally more efficient
than that of the brute-force approach. The treatment values are updated by taking average of
the optimal treatment values across individuals assigned to each segment, which ensures the
candidate treatments for each iteration of the algorithm are close to the individually optimal
treatments. This update rule is derivative-free and computationally cheap as it is the mean vector
across treatment dimensions. In contrast, BFGS updates in a computationally expensive quasi-
newton procedure that requires explicit gradient evaluations. In our computational example,
Algorithm 1 converges in less than 50 iterations, whereas each BFGS optimizer takes around 250
function calls and 40 calls to the gradient.
G Randomization checks for the experiment
To examine if the randomization in the experiment was correctly implemented by the firm, we
compare propensity scores of each treatment arm to the holdout set. The propensity score com-
parison checks for overlap and covariate balance which should be satisfied by the randomization
in the field experiment (Imbens and Rubin, 2015). We assume SUTVA holds because the coupons
are linked to each customer’s account on the platform and we assume that sharing of coupons
among customers is unlikely.
We estimate a logistic regression for the propensity score of each treatment arm on our co-
variates using the Lasso. We then plot the distribution of the predicted propensity score in Figure
9 separately for treated and not treated individuals. We find that there is a sizable difference in
the propensity scores across the two types of individuals which suggests the data might not be
balanced. We then examine each treatment arm separately and estimate a logistic regression for
the propensity score of each treatment arm to the no treatment arm using the Lasso and plot the
predicted propensity score for only the treated individuals for each treatment arm in Figure 10.
We find that there is virtually no difference in predicted propensity scores for the treated indi-
viduals in each treatment arm. These results suggests that the randomization was correctly done
across treatment arms, but may be incorrectly performed for the control group or no treatment
sample. The company has not indicated that the randomization was incorrectly implemented, but
we will adjust our CATE estimations with the propensity score to account for possible mistakes
or stratification procedures during the firm’s randomization procedure.
49

H Honest validation for CATE estimation
We use the honest validation procedure introduced in Misra (2021) to provide an out-of-sample
performance evaluation for the parametric form for the continuous CATEs (Equation 16) to the
non-parametric CATE estimates for each treatment arm. The honest validation procedure lever-
ages the fact that the treatment arms are discrete while the treatment variables are themselves
continuous to provide a comparison of the parameterized estimate to the nonparametric esti-
mates in a holdout set. We detail the procedure and describe the evaluation in the remainder of
this section.
The honest validation procedure is implemented in four steps. First, we use the Causal Forest
to nonparametrically estimate the CATEs for each of the eight treatment arms ( 2, 3, 4, 5 dollars
off and 5, 10, 15, 20 percentage off).
Second, for each individual, we hold out the individual’s actual treatment assignment and use
the predicted CATEs to estimate the individual’s parameterized CATE function (Equation 16). 31
The estimation is only done in the dimension of treatment that the individual was assigned. For
example, if the individual was assigned to a two dollar off promotion in the field experiment, we
would use the customer’s predicted CATEs for the other dollar off treatment arms (0, 3, 4, 5 dollars
off) to estimate the individual’s parameterized CATE function. The two dollar off promotion is
held out in this step and consists of the hold-out set for the parameterized estimate.
Third, we use the parameterized CATE function to predict the CATE estimate for the held out
treatment. In our running example, we would predict the individual’s CATE using the parameter-
ized CATE function for two dollars off. The two dollar off promotion was the individual’s assigned
treatment from the field experiment so we have the nonparametric Causal Forest estimate for the
individual at that treatment.
Lastly, we compare the predicted CATE in the held out treatment to the nonparametric Causal
Forest estimate for the individual. In our running example, we would compare the non-parametric
estimate of the individual’s CATE at two dollars off to her predicted CATE estimate at two dollars
off from the parameterized CATE function.
If we treat the nonparametric estimate as the “ground truth”, then this honest validation pro-
cedure will inform us how close our chosen parameterization of the CATE function is to the
nonparametric ground truth. We perform this procedure separately for each dimension of treat-
ment—dollar off and percentage off promotions.
Figure 11 plots the parametric estimates against the non-parametric estimate for each indi-
vidual. The horizontal axis represents the parametric estimates in the holdout set and the vertical
31The average𝑅2 of the restricted parameterized CATEs is0.948 for the dollar off and 0.840 for the percentage off
promotions which suggests the parameterization fits the restricted set of data well in sample.
50

axis represents the non-parametric estimates. The shapes and colors of the points represent the
assigned treatment arm in the field experiment. We see that most of the points lie scattered
around the 45 degree line which suggests the two types of estimates overlap. Further, the corre-
lation between the parametric estimates in the hold-out sample to the non-parametric estimates
is 0.821 for the dollar off and 0.604 for the percentage off promotions. These results suggest that
the parameterized CATEs perform well in the hold out set.
We see generally that the non-parametric estimates are noisier than the parametric estimates
as there is more dispersion on the vertical axis in Figure 11. The parametric form imposes more
structure on the CATEs which reduces the variance of the estimates. The variance of the points
is higher for the percentage off promotions for both the parametric and nonparametric estimates
which explains why the parameterization fits the dollar off promotion’s response better than the
percentage off promotion’s response.
I Surplus calculation details
With our coarse personalization framework, we can empirically visualize how surplus changes
with the level of personalization. Since the firm can only choose𝐿 segments to assign, individuals
can be assigned a treatment that is either above or below their optimal level or even in a different
treatment dimension. Compared to full personalization, the consumer surplus may increase or
decrease under coarse personalization. In contrast, the producer surplus will always diminish
when the firm more coarsely personalizes by the optimality of full personalization. Due to the
ambiguous effect on consumer surplus, the total surplus generated for each individual𝑖 can either
increase or decrease compared to the full personalization.
Intuitively, we expect that some individuals benefit from coarse personalization because they
may receive a treatment that is better for them than what they would get under full personal-
ization. The distortion in the firm’s ability to fully granularly personalize creates this benefit to
individuals. For the segmentation strategy, when determining the optimal assignments and the
optimal treatments to offer, the firm maximizes profits without considering consumer surplus. An
individual generally cannot benefit too much, otherwise the firm would reassign the individual
to another treatment. These non-monotonic changes to the individual-level consumer surplus
as the personalization ability of the firm increases directly parallels to the non-monotonicity in
the consumer surplus as firms are able to use more features of the data to personalize prices in
Dubé and Misra (2022). Total surplus can increase or decrease with coarse personalization de-
pending on the changes in consumer surplus relative to the producer surplus; if the consumer
surplus gain from coarser personalization dwarfs the loss in producer surplus, then total surplus
increases with coarser personalization.
51

We formulate a simple surplus analysis to empirically examine the results from Bergemann
and Bonatti (2011) and Dubé and Misra (2022) in our framework. Without loss of generality, at
full personalization, individual 𝑖 is offered treatment value 𝑡∗ 𝑖,𝑑 that is non-zero in dimension 𝑑.
The expected outcome from giving individual𝑖 this optimal treatment is𝐸[𝑌𝑖|𝒙𝑖,...,𝑡 ∗ 𝑖,𝑑,... ] and
the firm makes expected profits 𝐸[𝑌𝑖|𝒙𝑖,...,𝑡 ∗ 𝑖,𝑑,... ]− 𝑐𝑑(𝑡∗ 𝑖,𝑑). If individual 𝑖 is instead assigned
treatment value ˜𝑡𝑖,𝑑′ that is non-zero in dimension𝑑′ under coarse personalization, the expected
outcome from giving individual𝑖 this optimal treatment is𝐸[𝑌𝑖|𝒙𝑖,..., ˜𝑡𝑖,𝑑′,... ] and the firm makes
expected profits 𝐸[𝑌𝑖|𝒙𝑖,..., ˜𝑡𝑖,𝑑′,... ]− 𝑐𝑑′(˜𝑡𝑖,𝑑′). Lastly, we assume the individual has valuation
function𝑣𝑖(·) and values the two types of treatments monetarily at𝑣𝑖(𝑡∗ 𝑖,𝑑),𝑣𝑖(˜𝑡𝑖,𝑑′).
At the individual level, the change in consumer surplus from coarse personalization to the
full personalization is
Δ𝐶𝑆𝑖(˜𝑡𝑖,𝑑′) =𝑣𝑖(˜𝑡𝑖,𝑑′)− 𝑣𝑖(𝑡∗ 𝑖,𝑑) (25)
and the change in producer surplus is
Δ𝑃𝑆𝑖(˜𝑡𝑖,𝑑′) =

𝐸[𝑌𝑖|𝒙𝑖,..., ˜𝑡𝑖,𝑑′,... ]− 𝑐𝑑′(˜𝑡𝑖,𝑑′)

−

𝐸[𝑌𝑖|𝒙𝑖,...,𝑡 ∗ 𝑖,𝑑,... ]− 𝑐𝑑(𝑡∗ 𝑖,𝑑)

. (26)
Then, the change in total surplus from coarse personalization to the full personalization for indi-
vidual𝑖 is
Δ𝑇𝑆𝑖(˜𝑡𝑖,𝑑′) = Δ𝐶𝑆𝑖(˜𝑡𝑖,𝑑′)+ Δ𝑃𝑆𝑖(˜𝑡𝑖,𝑑′)
=𝑣𝑖(˜𝑡𝑖,𝑑′)− 𝑣𝑖(𝑡∗ 𝑖,𝑑)+

𝐸[𝑌𝑖|𝒙𝑖,..., ˜𝑡𝑖,𝑑′,... ]− 𝑐𝑑′(˜𝑡𝑖,𝑑′)

−

𝐸[𝑌𝑖|𝒙𝑖,...,𝑡 ∗ 𝑖,𝑑,... ]− 𝑐𝑑(𝑡∗ 𝑖,𝑑)

.
(27)
Since the distortion in the firm’s optimal targeting strategy leads some individuals being given
a better promotion than that under full personalization, total surplus can increase under coarse
personalization. However, because the firm decides the treatment levels offered as well as their
assignments, individuals that receive overly beneficial treatments at the expense of the firm will
be reassigned if the firm is able to do so. The reassignment occurs because the firm focuses solely
on maximizing profits or producer surplus when personalizing. Depending on the sizes of the
consumer valuations and the generated profits, coarse personalization can either increase societal
deadweight loss or total surplus.
52

Example
To build intuition for the total surplus decomposition in Equation 27, we can consider the case
where there is only one dimension of treatment and the treatment𝑡𝑖,1 represents a dollar amount
off coupon that the consumer can redeem on her next purchase. We assume that the individual
values the coupon at face value so𝑣𝑖(𝑡∗ 𝑖,1) =𝑡∗ 𝑖,1 and𝑣𝑖(˜𝑡𝑖,1) = ˜𝑡𝑖,1 and the cost for the firm to issue
the coupon is also the face value of the coupon (𝑐1(𝑡∗ 𝑖,1) =𝑡∗ 𝑖,1 and𝑐1(˜𝑡𝑖,1) = ˜𝑡𝑖,1).32 Then, the change
of the total surplus from assigning coupon˜𝑡𝑖,1 to individual𝑖 compared to full personalization with
𝑡∗ 𝑖,1 is
Δ𝑇𝑆𝑖(˜𝑡𝑖,1) = ˜𝑡𝑖,1−𝑡∗ 𝑖,1+

𝐸[𝑌𝑖|𝒙𝑖, ˜𝑡𝑖,1]− ˜𝑡𝑖,1

−

𝐸[𝑌𝑖|𝒙𝑖,𝑡∗ 𝑖,1]− 𝑡∗ 𝑖,1

=𝐸[𝑌𝑖|𝒙𝑖, ˜𝑡𝑖,1]− 𝐸[𝑌𝑖|𝒙𝑖,𝑡∗ 𝑖,1]
=𝜏1(𝒙𝑖, ˜𝑡𝑖,1)− 𝜏1(𝒙𝑖,𝑡∗ 𝑖,1), (28)
where added and subtracted 𝐸[𝑌𝑖|𝒙𝑖, 0], or the expected outcome under no treatment, to get to
the last line. Thus, the change in total surplus for individual 𝑖 from coarse personalization over
the full personalization is just the difference in the continuous CATE evaluated at ˜𝑡𝑖,1 and𝑡∗ 𝑖,1.
If𝜏1(𝒙𝑖,𝑡) is increasing in 𝑡, then the total surplus for individual 𝑖 will increase if ˜𝑡𝑖,1 > 𝑡𝑖,1 or
her assigned treatment level is higher than the individual’s full personalization level. Similarly,
if𝜏1(𝒙𝑖,𝑡) is decreasing in 𝑡, then the total surplus for individual 𝑖 will increase if ˜𝑡𝑖,1 < 𝑡𝑖,1 or
the individual’s assigned treatment level is lower than the individual’s full personalization level.
Thus, total surplus can either increase or decrease for individuals under coarse personalization
when compared to full personalization.
32For a coupon that is for five dollars off, the individual would value the coupon at five dollars and the firm would
incur a five dollar cost of issuing the coupon to the consumer.
53

Figures
0
5
10
15
0.25 0.50 0.75 1.00
Propensity Score
Density
Treatment
Treated
Not treated
Note: Propensity scores are obtained using the Lasso with ten-fold cross-validation.
Figure 9: Estimated propensity score (any treated vs. not treated)
0
1
2
3
0.25 0.50 0.75 1.00
Propensity Score
Density
Treatment Name
2 dollars off
3 dollars off
4 dollars off
5 dollars off
5 percent off
10 percent off
15 percent off
20 percent off
Note: Propensity scores are obtained using the Lasso with ten-fold cross-validation.
Figure 10: Estimated propensity score across treated arms
54

Figure 11: Honest validation of the parametric CATE estimates on sales
(a) Dollar off promotion
(b) Percentage off promotion
Note: These figures provide comparisons of the predicted treatment effect from the CATE parameterization (Equation
16) in the holdout treatment to its non-parametric estimate. The dollar off and percentage off promotions are plotted
separately in the two panels. Each point represents an individual assigned a dollar off or percentage off promotion
in the field experiment. The shape and color of the points represents which treatment arm was assigned to the
individual. A 45 degree line is provided as a visual reference.
55

Note: This figure provides a top-down view of Figure 6 and visualizes the coarse personalization solution with
𝐿 = 10 segments. The optimal treatment levels (𝑡∗ 𝑖,1,𝑡∗ 𝑖,2) for each individual are plotted for the dollar off and the
percentage off promotions in the scatterplot. The segments’ membership are labeled by color and the segments’
assigned treatment is represented by the diamond point. These assigned treatments are in Table 2.
Figure 12: Treatment assignments for the coarse personalization solution (𝐿 = 10 treatments)
Note: This figure visualizes the results from forming𝐿 = 10 segments based on optimal treatment levels. The
construction of segments uses Euclidean distance between the optimal treatment levels. The optimal treatment
levels (𝑡∗ 𝑖,1,𝑡∗ 𝑖,2) for each individual is plotted for the dollar off and the percentage off promotions in the scatterplot.
The segments’ membership are labeled by color and the segments’ assigned treatment is represented by the
diamond point.
Figure 13: Treatment assignments for segmenting on optimal treatment levels (𝐿 = 10 treatments)
56

Tables
Table 5: Surplus decomposition by number of segments
Number of segments (𝐿) Δ𝑇𝑆 ($) Δ𝑇𝑆 𝑖 > 0 (%) Δ𝐶𝑆 ($) Δ𝐶𝑆𝑖 > 0 (%) Δ𝑃𝑆 ($) Δ𝑃𝑆 𝑖 > 0 (%)
1 10,613 64.16 44,029 64.54 -33,416 0
2 14,348 62.38 27,387 62.38 -13,040 0
3 21,248 50.29 29,483 50.29 -8,234 0
4 -123 49.71 5,546 49.71 -5,668 0
5 2,469 46.05 6,358 46.05 -3,889 0
6 3,807 51.16 6,724 51.17 -2,917 0
7 4,622 49.32 7,002 49.32 -2,380 0
8 737 49.18 2,664 49.18 -1,927 0
9 1,236 50.42 2,813 50.42 -1,577 0
10 1,543 49.98 2,883 49.98 -1,340 0
Note: Δ𝑇𝑆, Δ𝐶𝑆, and Δ𝑃𝑆 respectively represent the total change in total surplus, consumer surplus, and producer
surplus to the full personalization benchmark across individuals. Δ𝑇𝑆𝑖 > 0 represents the percentage of individuals
who have a positive change in total surplus to the full personalization benchmark and the other two columns (Δ𝐶𝑆𝑖 >
0 and Δ𝑃𝑆𝑖 > 0) are defined similarly.
Table 6: Surplus decomposition across individuals for𝐿 = 10
Treatment (𝑙) Average Δ𝑇𝑆 𝑖 Δ𝑇𝑆 𝑖 > 0 (%) Average Δ𝐶𝑆𝑖 Δ𝐶𝑆𝑖 > 0 (%) Average Δ𝑃𝑆 𝑖 Δ𝑃𝑆 𝑖 > 0 (%) 𝑁
1 -57.70 56 -15.65 56 -42.04 0 7,090
2 138.73 53 299.50 53 -160.77 0 556,544
3 136.14 25 152.81 25 -16.67 0 7,375
4 22.33 58 164.97 58 -142.64 0 54,253
5 -59.35 51 -7.84 51 -51.51 0 12,816
6 -170.45 64 78.62 64 -249.07 0 15,532
7 176.26 58 332.54 58 -156.27 0 214,631
8 -8.92 33 312.48 33 -321.41 0 30,425
9 -253.45 35 -122.20 36 -131.25 0 9,234
10 133.11 40 300.28 40 -167.17 0 295,479
Note: Δ𝑇𝑆𝑖, Δ𝐶𝑆𝑖, and Δ𝑃𝑆𝑖 respectively represent the change in total surplus, consumer surplus, and producer
surplus to the full personalization benchmark for individual 𝑖. Δ𝑇𝑆𝑖 > 0 represents the percentage of individuals
assigned that treatment who have a positive change in total surplus to the full personalization benchmark and the
other two columns (Δ𝐶𝑆𝑖 > 0 and Δ𝑃𝑆𝑖 > 0) are defined similarly.
57
