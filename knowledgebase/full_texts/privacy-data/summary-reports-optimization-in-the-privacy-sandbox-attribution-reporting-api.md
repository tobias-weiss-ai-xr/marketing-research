---
title: Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API
url: https://dx.doi.org/10.56553/popets-2024-0132
category: privacy-data
subcategory: measurement
date: 2024-07
venue: Proceedings on Privacy Enhancing Technologies
authors:
- Hidayet Aksu
- Badih Ghazi
- Pritish Kamath
source: openalex-oa
pdf_url: https://petsymposium.org/popets/2024/popets-2024-0132.pdf
pages: 17
chars: 79362
fetched_at: '2026-11-08T17:32:02+00:00'
kb_version: 1
---

# Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API

Summary Reports Optimization in the Privacy Sandbox
Attribution Reporting API
Hidayet Aksu
Google
aksu@google.com
Badih Ghazi
Google
badihghazi@gmail.com
Pritish Kamath
Google
pritishk@google.com
Ravi Kumar
Google
ravi.k53@gmail.com
Pasin Manurangsi
Google
pasin@google.com
Adam Sealfon
Google
adamsealfon@google.com
Avinash V Varadarajan
Google
avaradar@google.com
ABSTRACT
The Privacy Sandbox Attribution Reporting API has been recently
deployed by Google Chrome to support the basic advertising func-
tionality of attribution reporting (aka conversion measurement)
after deprecation of third-party cookies. The API implements a
collection of privacy-enhancing guardrails including contribution
bounding and noise injection. It also offers flexibility for the analyst
to allocate the contribution budget.
In this work, we present algorithms for optimizing the allocation
of the contribution budget for summary reports from the Attribu-
tion Reporting API. We develop a synthetic data model that we find
to accurately capture real-world conversion data, and extensively
evaluate our method on two real-world datasets and two synthetic
datasets. We show that optimizing the parameters that can be set
by the analyst can significantly improve the utility achieved by
querying the API while satisfying the same privacy bounds.
KEYWORDS
Attribution Reporting, Conversion Measurement, Contribution
Bounding, Contribution Budgeting, Discrete Laplace Mechanism,
Differential Privacy, Bias-Variance Trade-off
1 INTRODUCTION
In recent years, growing concerns around user privacy have led to
new efforts by web browsers and mobile platforms to limit perva-
sive tracking of users by websites, apps, and ad technology (aka,
ad-tech) providers. In particular, this led to the decision by several
browsers and platforms, including Safari [25], Mozilla Firefox [27],
and Google Chrome [22], to deprecate third-party cookies. How-
ever, third-party cookies had been widely used to support some
of the most critical functionalities powering digital advertising,
notably ad conversion measurement (aka attribution reporting),
where an ad-tech seeks to determine the volume of conversions
This work is licensed under the Creative Commons Attribu-
tion 4.0 International License. To view a copy of this license
visit https://creativecommons.org/licenses/by/4.0/ or send a
letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
Proceedings on Privacy Enhancing Technologies 2024(4), 605–621
© 2024 Copyright held by the owner/author(s).
https://doi.org/10.56553/popets-2024-0132
attributed to ads shown on different publishers and as part of differ-
ent campaigns. Example conversion measurement queries include
the number of conversions attributed to ad impressions shown on
a given publisher, or the total conversion value for sales occurring
during a weekend and attributed to a particular ad campaign. This
made several platforms and browsers provide privacy-preserving
APIs that can support ad conversion measurement functionalities
after the deprecation of third-party cookies, including Private Click
Measurement (PCM) on Safari [26], SKAdNetwork on iOS [8], the
Interoperable Private Attribution (IPA) developed by Mozilla and
Meta [23], Masked LARK from Microsoft [6, 21], and Privacy Sand-
box Attribution Reporting API (ARA) from Google [2, 20].
The Attribution Reporting API, available on both the Chrome
browser [20] and the Android operating system [ 2], offers sum-
mary reports that could be used to estimate counts and values of
conversions attributed to ad campaigns (and broken down by other
impression and conversion features). The privacy guardrails in the
API [3] include contribution bounding as well as discrete Laplace
noise injection, which can be used to provide a differential privacy
(DP) [13] guarantee on the output summary reports. More precisely,
for each impression, the API enforces a fixed bound on the contri-
butions of all conversions attributed to it. Moreover, each of these
contributions is required to be discrete. The contributions from
different impressions (from possibly many users) are aggregated.
Discrete Laplace noise is then added to the vector of contributions,
and the result is the summary report.
While ARA provides a formal DP guarantee, the noise addition
and contribution bounding procedure represents a paradigm shift in
conversion measurement compared to third-party cookies; straight-
forward use of ARA might result in large amount of noise. Concerns
have been raised that the degradation in accuracy after deprecation
of third-party cookies can in turn impact the downstream business
decisions made based on the measurements [15, 18].
This brings us to the main question of the paper: How can an
ad-tech obtain desired measurements via ARA that are as accurate
as possible? The flexibility of ARA allows the ad-tech to choose
their own encoding of the attributed information. (See Section 3.1
for formal descriptions.) By adjusting such an encoding, the ad-
tech can (implicitly) decide on several parameters, such as how
the contribution budget is allocated across different conversions
605

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
that are attributed to the same impression. These choices by the
ad-tech can significantly impact the utility of the summary reports
for any fixed privacy bar. The focus of this work is to optimize
these summary reports to maximize utility for a given level of
(differential) privacy.
1.1 Summary of Contributions
We make the following contributions to the problem of optimizing
summary reports from the Attribution Reporting API (ARA):
⊲ We formally define the problem of optimizing the utility of con-
version aggregates based on summary reports from the ARA.
In the process, we flesh out subtle but important details regard-
ing how the constraints in the API (e.g., contribution bounding,
discretization requirements, encoding of multiple conversions
attributed to the same impression, noise injection) can shape the
optimization problem.
⊲ Given access to historical data that has not been contribution-
bounded and is noise-free, we provide an optimization problem
that yields the optimal choice of parameters to use the ARA on
future data. Such historical data could be available to ad-techs
who have thus far relied on third-party cookies for ad conversion
measurement (prior to the deprecation of third-party cookies).
⊲ We evaluate our algorithm on real-world conversion data, demon-
strating that it significantly improves utility compared to baseline
non-optimized summary reports. We also evaluate our algorithm
on synthetic datasets (for attributed conversion counts and val-
ues), which are sampled using generative models that we fit to
real conversion data. These data generation models might be of
independent interest for future research on (privacy-preserving)
ad conversion measurement. 1
⊲ While our algorithm can be used to optimize for a variety of error
measures, we discuss several qualitative advantages of using a
thresholded version of the root mean square relative error in ad
conversion measurement.
⊲ As our algorithm uses past (historical) data in order to set the
parameters used to measure conversions on future data, we com-
plement our empirical findings by proving generalization bounds
showing that parameters optimized using historical bounds yield
good results on similar future data.
We remark that, due to the rather specific nature of the At-
tribution Reporting API (and, to a lesser extent, DP conversion
measurements), we are not aware of any previous work that studies
the same setting as ours. Nonetheless, we discuss some related work
in Section 7.
1.2 Overview of the Rest of the Paper
In Section 2, we provide some basic definitions related to ad con-
version measurement, and to DP. In Section 3, we provide further
background on the problem setup; ARA is formalized in more detail
in Section 3.1, the problem of estimating conversion aggregates
(the focus of our work) is defined in Section 3.2, and we briefly
discuss the error metric in Section 3.3. In Section 4, we present our
optimization algorithm for contribution budgeting. We describe
our experimental evaluation and findings in Section 5. In Section 6,
1Code from our evaluation can be found at https://github.com/google-research/google-
research/tree/master/ara_optimization
we prove generalization bounds that explain why our algorithm
does not overfit to the historical data. We discuss some related work
in Section 7. We discuss limitations and interesting directions for
future research in Section 8, and provide concluding remarks in
Section 9.
2 PRELIMINARIES
We now define the main terminology used in this paper. LetX be the
set of impression features, including a unique impression identifier
for each impression, letY be the set of conversion features, and
letZ =X×Y . We denote a dataset as 𝐷 =(𝑧1,...,𝑧 𝑛) ∈Z∗
where each record𝑧𝑖 is of the form(𝑥𝑖,𝑦𝑖), consisting of impression
features𝑥𝑖∈X and conversion features𝑦𝑖∈Y . The impression
features are assumed to beknown to the ad-tech, and can correspond
to an a priori unbounded number of conversions, which are assumed
to be unknown to the ad-tech.2 We say that two datasets𝐷,𝐷′ are
adjacent, denoted as 𝐷∼ 𝐷′ if we can get one dataset from the
other by removing all records corresponding to a single impression.
We use the following running example to illustrate our notation.
Imagine a fictional gift shop called Du & Penc that uses digital
advertising to reach its customers. Their holiday sales are captured
in the dataset in Table 1, where each record contains impression
features of (i) an impression ID, (ii) the campaign, and (iii) the city
in which the ad was shown, as well as the conversion features of the
(i) number of items bought and (ii) total dollar value of items bought
as part of the conversion.Du & Penc, as an advertiser, want to know
if their ads are working, so they track conversions to see how many
people click on their ads and then take the desired action, such
as buying a product. Therefore, they track conversions and run
queries like ‘total sales per advertising campaign’ to ensure their
ads are effective and generating revenue. This helps them identify
which ads are performing well and which ones need improvement.
2.1 Differential Privacy
Definition 2.1 (DP [13]). For𝜀≥ 0, a randomized algorithmA
is𝜀-DP if for all adjacent datasets𝐷∼𝐷′, and for every possible
output𝑜, it holds that Pr[A(𝐷) =𝑜]≤ 𝑒𝜀· Pr[A(𝐷′) =𝑜].
For an extensive overview of DP, we refer the reader to the mono-
graph [14]. A commonly used method in DP is the discrete Laplace
mechanism. To define it, we recall the notion ofℓ1-sensitivity, where
for any vector𝑣∈ R𝑑, we denote itsℓ1-norm as∥𝑣∥1 := ˝𝑑 𝑖=1|𝑣𝑖|.
Definition 2.2 (ℓ1-sensitivity). LetZ be any set, and𝑓 :Z𝑛→ R𝑑
be a𝑑-dimensional function. Itsℓ1-sensitivity is defined as Δ1𝑓 :=
max𝐷∼𝐷′∥𝑓(𝐷)− 𝑓(𝐷′)∥ 1.
Definition 2.3 (Discrete Laplace Mechanism). The discrete Laplace
distribution centered at 0 and with parameter 𝑎 > 0, denoted by
DLap(𝑎), is the distribution whose probability mass function at
integer𝑘 is 𝑒𝑎−1 𝑒𝑎+1·𝑒−𝑎|𝑘|. The𝑑-dimensional discrete Laplace mecha-
nism with parameter𝑎 applied to a function𝑓 :Z𝑛→ Z𝑑, on input
a dataset 𝐷∈Z 𝑛, returns 𝑓(𝐷)+ 𝜉 where𝜉 is a𝑑-dimensional
noise random variable whose coordinates are sampled i.i.d. from
DLap(𝑎) (abbreviated as𝜉∼ DLap(𝑎)⊗𝑑).
2Note that for the historical data both impression and conversion features are assumed
to be known.
606

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
Impression features 𝒙 Conversion features 𝒚
Impression ID Campaign City #items value ($)
𝑧1→ 123 Thanksgiving New York 3 21
𝑧2→ 123 Thanksgiving New York 1 5
𝑧3→ 456 Thanksgiving Boston 1 99
𝑧4→ 123 Thanksgiving New York 2 23
𝑧5→ 101 Christmas Boston 2 50
𝑧6→ 789 Christmas New York 3 15
𝑧7→ 101 Christmas Boston 1 5
. . . . . . . . . . . . . . . . . .
Table 1: Running example showing the impression and conversion logs for Du & Penc , an online gift shop.
𝑥∈X impression features
𝑦∈Y conversion features
𝑧∈Z all features(𝑥,𝑦) of an input record
Z𝑗 one slice of the input domainZ =Z1⊔···⊔Z 𝑚
𝜀 privacy parameter
𝐷∼𝐷′ adjacent datasets
𝑉𝐷(𝑞)𝑗 aggregate value of query𝑞 on slice 𝑗 of dataset𝐷
Γ ARA-defined contribution budget, set to 65,536
A,R pre/post-processing algorithms specified by ad-tech
C,S fixed algorithms performed by ARA
𝐾 set of aggregation keys{𝑘1,...,𝑘 𝑇}
𝑤𝑧 histogram contributionA(𝑧)
𝑤𝑧 𝑘 aggregatable value corresponding to𝑤𝑧 and key𝑘
Z𝑥 records corresponding to impression𝑥
W𝑥 histogram contributions corresponding to𝑥
Z
𝑥
records corresponding to aggregatable reports for𝑥
W
𝑥
aggregatable reports for impression𝑥
𝑤𝑥 sum of aggregatable reports for impression𝑥
𝑊 summary report produced by algorithmS
𝑈 final estimate by after post-processing byR
𝑑 number of queries, excluding the count query
𝑚 number of slices of the data domain
𝐶 count limit
𝐶ℓ clipping threshold for queryℓ∈[ 𝑑]
𝛼ℓ contribution budget fraction forℓ∈[ 𝑑]
𝜏 parameter of the RMSRE𝜏 error metric
Table 2: Summary of notation.
Lemma 2.4. For all 𝜀 > 0, the 𝑑-dimensional discrete Laplace
mechanism with parameter 𝑎≤𝜀/Δ1𝑓 is𝜀-DP.
Lemma 2.5. For all𝑎 > 0, it holds that
E[DLap(𝑎)] = 0 and Var(DLap(𝑎)) = 2𝑒𝑎
(𝑒𝑎− 1)2 .
The following is a well-known property of DP.
Lemma 2.6 (Post-processing). IfA is𝜀-DP, then for any (ran-
domized) algorithmA′, it holds thatA′(A(·)) is also𝜀-DP.
3 BACKGROUND AND SETUP
3.1 ARA Summary Reports
We now describe Summary Reports, which is a pre-defined frame-
work for ad measurement fixed in the ARA [24]. At a high-level,
ARA allows the ad-tech to specify the encoding algorithm from
each record to a vector. A contribution bounding procedure is then
applied to ensure that the total contribution corresponding to each
impression is bounded. Once this is done, they are sent to the aggre-
gation service who sums these vectors and adds a discrete Laplace
noise to the result. This (noisy) summary report is then returned to
the ad-tech.
More formally, a mechanism 𝑀 using ARA summary reports
operates as follows. To begin with, the ARA has a parameter called
contribution budget, which at this time of writing, is fixed to Γ :=
216 = 65, 536 (see [5]). To use the API, the ad-tech needs to specify
the following information beforehand:
⊲ a set𝐾 ={𝑘1,...,𝑘 𝑇} of aggregation keys, and
⊲ an encoding algorithmA that maps any record𝑧 to a histogram
contribution𝑤𝑧∈ Z𝐾 ≥0, where𝑤𝑧 𝑘 is called the aggregatable value
corresponding to the aggregation key𝑘∈𝐾.
Having specified the algorithmA, the summary report is generated
as follows:
(1) Each record is mapped to a histogram contribution usingA. For
each impression𝑥, letZ𝑥 :=(𝑧𝑖1,...,𝑧 𝑖𝑐) be the sequence of
records corresponding to the same impression 𝑥, i.e., 𝑧𝑖𝑗 =
(𝑥,𝑦𝑖𝑗), and let W𝑥 be the sequence of corresponding his-
togram contributions(𝑤𝑧𝑖1,...,𝑤 𝑧𝑖𝑐) obtained as𝑤𝑧𝑖𝑗 =A(𝑧𝑖𝑗).
(2) The histogram contributions for each impression𝑥 are filtered3
byC (Algorithm 1), such that theℓ1-norm of the sum of the re-
turned vectors, called aggregatable reports, is at most Γ. For ease
of notation, we useW
𝑥
to denote the sequence of aggregatable
reports for impression𝑥, and let𝑤𝑥 := ˝ 𝑤∈W 𝑥𝑤. Similarly,
we useZ
𝑥
to denote the sequence of records corresponding to
aggregatable reports for impression𝑥.
(3) The aggregatable reports are passed on byC to the ARA aggre-
gation serviceS that adds all the aggregatable reports and adds
discrete Laplace noise, as given in Algorithm 2, and returns a
summary report𝑊∈ Z𝐾 back to the ad-tech.
3Algorithm 1 as written requires all the inputs to be provided at once. But in practice,
it runs in an online manner, namely, the 𝑤𝑖 s arrive sequentially and the decision
of whether to include𝑤𝑖 or not, is made without knowing the future𝑤𝑖′s, and the
algorithm only needs to remember a single 16-bit value𝑏 for each impression𝑥.
607

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
Algorithm 1 ContributionBoundingC.
Params: Contribution budget Γ := 216 = 65, 536.
Input: Sequence of histogram contributions 𝑤1,...,𝑤 𝑐 ∈ Z𝐾 ≥0
corresponding to a single impression.
Output: Sequence of aggregatable reports𝑤1,...,𝑤 ˆ𝑐∈ Z𝐾 ≥0 such
that∥ ˝ ˆ𝑐 𝑗=1𝑤𝑗∥1≤ Γ and ˆ𝑐≤𝑐.
𝑆←∅ and𝑏← 0
for𝑖∈{ 1,...,𝑐 } do
if𝑏+∥𝑤𝑖∥1≤ Γ then
𝑆←𝑆∪{𝑖} and𝑏←𝑏+∥𝑤𝑖∥1
return (𝑤𝑖)𝑖∈𝑆
Algorithm 2 SummaryReportS.
Params: ⊲ Contribution budget Γ := 216 = 65, 536,
⊲ Privacy parameter𝜀 > 0.
Input: Aggregatable reports𝑤1,...,𝑤 𝑟∈ Z𝐾 ≥0
Output: Summary report𝑊∈ Z𝐾
return 𝑊← ˝ 𝑗𝑤𝑗+ DLap(𝜀/Γ)⊗𝐾
(4) Finally, the ad-tech can post-process the summary report 𝑊
using any algorithmR to obtain the final estimate𝑈∈ R𝑑×𝑚.
Note that algorithmA andC are executed on the browser/device
on which the impression occurred, and only the aggregatable re-
ports are passed on toS to produce the summary report, which
is executed in a trusted execution environment [1], andR is run
locally by the ad-tech as illustrated in Figure 1.
An important point to note is that algorithmsC andS are fixed in
ARA, and the only parts that the ad-tech can control are algorithms
A andR. The design of ARA summary reports ensures that, no
matter what algorithmsA andR are provided, it is guaranteed
that the end-to-end algorithm generating the final result received
by the ad-tech is𝜀-DP. We include a short proof of this statement.
Theorem 3.1. For allA andR, the end-to-end algorithm combin-
ing Items 1 to 4 above satisfies 𝜀-DP.
Proof. We show that for any per-record input preprocessing
A performed in step 1, steps 2–3 are an instantiation of the Dis-
crete Laplace mechanism and thus satisfy DP by Lemma 2.4. The
conclusion then follows from the robustness of DP to arbitrary
postprocessing (Lemma 2.6).
The condition checked in the loop of AlgorithmC (step 2) ensures
that regardless of how algorithm A transforms each individual
record, the total contribution 𝑤𝑥 of each impression 𝑥 satisfies
∥𝑤𝑥∥1≤ Γ. AlgorithmS then adds Discrete Laplace noise scaled
to this maximum sensitivity Γ, so the algorithm combining steps
1–3 instantiates the Discrete Laplace mechanism and is guaranteed
to be𝜀-DP under adding or removing all conversions attributed to
a single impression,4 by Lemma 2.4. Finally, in Item 4, algorithmR
4Note that this is a simpler setting compared to adding or removing an impression,
which may create a “cascading effect” that leads to modifications in the conversions
attributed to multiple impressions at once. However, since the current version of the
ARA does not touch upon this issue, we will do the same in this paper.
post-processes the summary report𝑊 to obtain the final estimate
𝑈∈ R𝑑×𝑚; by Lemma 2.6, this remains𝜀-DP. □
Recall that the goal of our paper is to design a mechanism in this
framework that minimizes a desired error metric. In order to design
a mechanism, we need to specify: (i) the set𝐾 of aggregation keys,
(ii) algorithmA mapping records to histogram contributions𝑤𝑧,
and (iii) the reconstruction algorithmR for recovering estimates
of interest. As we will demonstrate through the rest of this paper,
careful selection of these can lead to significant utility improvement.
3.2 Estimating Conversion Aggregates
As mentioned earlier, we are interested in computing aggregate
statistics on attributed conversion where they can be “sliced” based
on certain attributes. This problem is formalized below.
Consider a fixed partition ofZ given asZ1⊔···⊔Z 𝑚, where the
Z𝑗 ’s are pairwise disjoint (where⊔ denotes a disjoint union). This
partition naturally induces a partition of𝐷 given as𝐷1⊔···⊔ 𝐷𝑚
where 𝐷𝑗 = 𝐷∩Z 𝑗 ; we refer to each 𝐷𝑗 as a slice of 𝐷.5 We
use 𝑋 := {𝑥 :∃𝑦 ∈ Ys.t.(𝑥,𝑦) ∈𝐷} and 𝑋𝑗 := {𝑥 :∃𝑦 ∈
Y s.t.(𝑥,𝑦)∈ 𝐷𝑗}, whenever𝐷 is clear from context.
A statistical query, denoted query in the rest of the article, is an
aggregatable value defined by a function𝑞 :Z→ R.6 The aggregate
value7 associated with a query𝑞 on dataset𝐷 is𝑉𝐷(𝑞)∈ R𝑚, given
as𝑉𝐷(𝑞)𝑗 := ˝ 𝑧∈𝐷𝑗𝑞(𝑧), namely one aggregate for each slice of
𝐷. Given queries𝑞1,...,𝑞 𝑑 of interest, the goal is to construct an
𝜀-DP mechanism that estimates the corresponding aggregate values
𝑉𝐷(𝑞1),...,𝑉 𝐷(𝑞𝑑) as “accurately” as possible.
In the Du & Penc example, one could consider a partition of the
records, e.g., by Campaign or by City or by the pair (Campaign,
City). We could consider the following two queries:𝑞1(𝑧), which
returns #items and 𝑞2(𝑧), which returns the dollar value in any
record𝑧. In addition, we always consider another query of interest,
given as𝑞0(𝑧) = 1 for all𝑧∈Z ; that is,𝑉𝐷(𝑞0)𝑗 is precisely the
number of records in the 𝑗th slice.
3.3 Error Metrics for Experiment Evaluation
Since the values estimated using Summary Reports API are noisy,
API users should evaluate the impact of noise in reports carefully to
ensure that they are useful. For example, when Du & Penc executes
queries such as ‘total sales per advertising campaign’ to determine
the effectiveness of individual campaigns, the presence of added
noise may introduce slight or significant variations in the results.
Consequently, the utility of summary reports is called into question
when noise is present. A variety of utility metrics can be used to
evaluate the impact of noise. We provide a list of all metrics that
we have considered in Table 5 (Appendix A). There are several
desirable criteria for metrics. As listed in Table 6 (Appendix A),
we find out that only RMSRE𝝉 metric (defined below) satisfies all
desired properties. Therefore, we focus on this metric for our main
5Slices may be any partition of the data domain. For example, slices might be specified
by a GROUP BY statement in SQL.
6We emphasize that a query here is a function of a single data record, not a function
of the whole dataset. This usage is similar to the statistical query model in learning
theory, but here we allow queries to be real-valued, not just[0, 1]-valued.
7The aggregation here is specifically summation; we use the term aggregate for con-
sistency with the API documentation [24]
608

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
Attribution Reporting API
Trusted
Execution
Environment Ad-tech
HistogramContribution
(Algorithm 3)
ContributionBounding
(Algorithm 1)
SummaryReport
(Algorithm 2)
ReconstructValues
(Algorithm 4)
𝑈RS
C
C
C
A
A
A
A
A
A
(𝑥1,𝑦 1,1) =𝑧1,1
(𝑥1,𝑦 1,2) =𝑧1,2
(𝑥1,𝑦 1,3) =𝑧1,3
(𝑥2,𝑦 2,1) =𝑧2,1
(𝑥3,𝑦 3,1) =𝑧3,1
(𝑥3,𝑦 3,2) =𝑧3,2
Figure 1: Illustrative usage of ARA summary reports. Algorithms C andS are fixed in the API. The ad-tech designs A andR.
experimental evaluation. However, our approach can be applied
just as well to other error metrics, as discussed in Appendix B.
Definition 3.2 ([19]). For a dataset𝐷∈Z∗, a query𝑞 :Z→ R,
and a random vector𝑢∈ R𝑚, the root mean squared relative error
with parameter𝜏∈ R>0 is defined as
RMSRE𝜏(𝑢,𝑞 ;𝐷) :=
vut 1
𝑚
∑︁
𝑗∈[𝑚]
E
 𝑢𝑗−𝑉𝐷(𝑞)𝑗
max{𝜏,𝑉𝐷(𝑞)𝑗}
2
,
where the expectation is over the randomness of𝑢. Similarly, for
parameters𝝉 =(𝜏0,...,𝜏 𝑑), queries(𝑞0,...,𝑞 𝑑), and a randomized
report𝑈∈ R(𝑑+1)×𝑚, we define
RMSRE𝝉(𝑈,(𝑞ℓ)𝑑 ℓ=0;𝐷) :=
vut
1
𝑑+ 1
𝑑∑︁
ℓ=0
RMSRE𝜏ℓ(𝑈ℓ,𝑞ℓ ;𝐷)2,
where𝑈ℓ is theℓth row of𝑈 .
4 CONTRIBUTION BUDGETING ALGORITHM
In this section, we present our algorithm for contribution budgeting.
Suppose we have 𝑑 queries𝑞1,...,𝑞 𝑑 :Z→ R≥0 for which an
ad-tech desires to estimate the aggregate values. We now describe
our approach for defining the aggregation keys 𝐾, the encoding
algorithmA mapping records to histogram contributions, and the
methodR for reconstructing the values.
4.1 Aggregation Keys & Histogram
Contributions
We take the set of aggregation keys to be𝐾 =([𝑑]∪{⊥})×[ 𝑚], i.e.,
we define𝑑+1 aggregation keys corresponding to each slice𝑗∈[ 𝑚].
We choose a count limit𝐶, and additionally, corresponding to each
query𝑞ℓ, we choose aclipping threshold𝐶ℓ and a contribution budget
fraction𝛼ℓ, subject to ˝𝑑 ℓ=1𝛼ℓ = 1. We discuss how to choose the
parameters𝐶 and(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] shortly.
For any record𝑧, suppose𝑣1,...,𝑣 𝑑 are given as𝑣ℓ =𝑞ℓ(𝑧). We
first clip each 𝑣ℓ to be at most 𝐶ℓ, namely, let𝑣′ ℓ = clip𝐶ℓ(𝑣ℓ) :=
min(𝑣ℓ,𝐶ℓ). Next, we scale 𝑣′ ℓ to lie in [0, 1], by dividing by 𝐶ℓ,
namely, let𝑣′′ ℓ =𝑣′ ℓ/𝐶ℓ. We will choose a histogram contribution
𝑤𝑧 that uses exactly⌊Γ/𝐶⌋ of the total contribution budget, so that
at most𝐶 conversions can be accounted for per impression. To this
end, we rescale𝑣′′ ℓ by⌊𝛼ℓ Γ/𝐶⌋ so that the sum of contributions is
at most Γ/𝐶, and moreover, we assign the remaining contribution
mass to⊥. Finally, we apply a randomized rounding on the real
values to make them integer-valued, as required by the API.
These steps are formalized in Algorithm 3, where CRR is a ran-
domized method that clips and performs randomized rounding, de-
fined as follows:
CRR(𝑣;𝐶,𝐶ℓ,𝛼ℓ) := RR
j𝛼ℓ Γ
𝐶
k
·
clip𝐶ℓ(𝑣)
𝐶ℓ

, (1)
where RR(𝜔) :=
(
⌈𝜔⌉ w.p.𝜔−⌊𝜔⌋
⌊𝜔⌋ w.p. 1−𝜔+⌊𝜔⌋. (2)
We use RR instead of deterministic rounding because E[RR(𝜔)] =
𝜔, which allows recovery of unbiased estimates from summary
reports.
Lemma 4.1. For any 𝑧, the vector 𝑤𝑧 returned by Algorithm 3
satisfies𝑤𝑧≥ 0 and∥𝑤𝑧∥1 =⌊Γ/𝐶⌋.
Proof. It is immediate to see that ˝ ℓ,𝑗 𝑤𝑧 ℓ,𝑗+ ˝ 𝑗𝑤𝑧 ⊥,𝑗 =⌊Γ/𝐶⌋.
Let 𝑗 be such that 𝑧 ∈ Z𝑗 . To show that indeed all the values
are non-negative, we observe that 𝑤𝑧 ℓ,𝑗′ = 0 for all 𝑗′ ≠ 𝑗, and
0≤ CRR(𝑣;𝐶,𝐶ℓ,𝛼ℓ)≤ ⌊𝛼ℓ Γ/𝐶⌋ and hence, we have
˝𝑑
ℓ=1𝑤𝑧 ℓ,𝑗 ≤ ˝𝑑 ℓ=1 j𝛼ℓ Γ 𝐶 k ≤ j Γ 𝐶 ˝𝑑 ℓ=1𝛼ℓ k =  Γ 𝐶  ,
and hence𝑤𝑧 ⊥,𝑗 =⌊Γ/𝐶⌋− ˝ ℓ𝑤𝑧 ℓ,𝑗 ≥ 0. □
Thus, we have that for any impression𝑥, at most the first𝐶 con-
versions result in valid aggregatable reports.
609

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
Algorithm 3 HistogramContributionA (ℓ∞ version).
Params: ⊲ Queries𝑞1,...,𝑞 𝑑 :Z→ R≥0,
⊲ Partition ofZ =Z1⊔···⊔Z 𝑚,
⊲ Parameters𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] with ˝𝑑 ℓ=1𝛼ℓ = 1,
⊲ Aggregatable Keys𝐾 =([𝑑]∪{⊥})×[ 𝑚].
Input: Record𝑧∈Z
Output: Histogram contribution𝑤𝑧∈ Z𝐾 ≥0
for slice 𝑗∈[ 𝑚] do
for ℓ∈[ 𝑑] do
𝑤𝑧 ℓ,𝑗 ←
(
0 if𝑧 ∉Z𝑗
CRR(𝑞ℓ(𝑧);𝐶,𝐶ℓ,𝛼ℓ) if𝑧∈Z 𝑗
𝑤𝑧 ⊥,𝑗 ←
(
0 if𝑧 ∉Z𝑗 Γ
𝐶

− ˝𝑑 ℓ=1𝑤𝑧 ℓ,𝑗 if𝑧∈Z 𝑗
return 𝑤𝑧
Figure 2 illustrates how this histogram contribution gets pre-
pared at the browser/device, using the example of the Du & Penc
dataset in Table 1. Consider queries 𝑞1(𝑧) being the number of
items purchased and𝑞2(𝑧) being the corresponding dollar value,
and the slices corresponding to the “Campaign”. In this case, the set
of aggregatable keys𝐾 is{1, 2,⊥}×{ Thanksgiving, Christmas},
corresponding to all possible combinations of query and campaign,
as well as the remaining contribution⊥ for each campaign.
Suppose we use count limit𝐶 = 2, clipping thresholds𝐶1 = 2,
𝐶2 = $30 and contribution budget fractions𝛼1 =𝛼2 = 0.5. Consider
the record𝑧1 corresponding to Impression ID 123, corresponding
to the Thanksgiving campaign. The conversion consists of𝑣1 = 3
items and value𝑣2 = $21, which get clipped as𝑣′ 1 = clip𝐶1(𝑣1) = 2
and𝑣′ 2 = clip𝐶2(𝑣2) = $21. These get rescaled as 𝑣′′ 1 = 𝑣′ 1/𝐶1 = 1
and 𝑣′′ 2 = 𝑣′ 2/𝐶2 = 0.7. Finally, 𝑣′′ 1 and 𝑣′′ 2 are further rescaled
by⌊𝛼1Γ/𝐶⌋ and⌊𝛼2Γ/𝐶⌋, respectively, which are both equal to
Γ/4 = 16384. Thus,𝑧1 gets mapped to the following aggregatable
values𝑤𝑧1 𝑘 :
𝑤1,Thanksgiving = RR(16384·𝑣′′ 1) = RR(16384) = 16384
𝑤2,Thanksgiving = RR(16384·𝑣′′ 2) = RR(11468.8) e.g., = 11469
𝑤⊥,Thanksgiving = 32768− 16384− 11469 = 4915
𝑤1,Christmas = 𝑤2,Christmas = 𝑤⊥,Christmas = 0
The histogram contribution𝑤𝑧1 consists of these aggregatable val-
ues.
We have∥𝑤𝑧1∥1 = 32768 = Γ/𝐶; this holds for all records 𝑧,
not just𝑧1. Since records𝑧1,𝑧2, and𝑧4 in Table 1 all correspond to
the same impression𝑥, the histogram contribution𝑤𝑧4 will end up
being ignored in the aggregate, since∥𝑤𝑧1+𝑤𝑧2+𝑤𝑧4∥ > Γ. That
is,Z
𝑥
=(𝑧1,𝑧 2), and the aggregatable reports corresponding to
records𝑧1 and𝑧2 will simply be the histogram contributions𝑤𝑧1
and𝑤𝑧2, while no aggregatable report will be produced for𝑧4.
4.2 Reconstruction of Values
Given the summary report 𝑊 (from Algorithm 2), we can post-
process to obtain estimates of𝑉𝐷(𝑞ℓ); see Algorithm 4. We useZ
𝑥
𝑗
to denoteZ
𝑥
∩Z𝑗 .
Impression
(Campaign = Thanksgiving)
aggregation_keys:
“Items, Campaign”: “ Items, Thanksgiving ”
“Value, Campaign”: “Value, Thanksgiving ”
“⊥, Campaign”: “⊥, Thanksgiving ”
Ad-tech
Publisher
Conversion
(#items = 3, value = $21)
aggregatable_trigger_data:
key_piece: “”, source_key: “Items, Campaign”
key_piece: “”, source_key: “Value, Campaign”
key_piece: “”, source_key: “⊥, Campaign”
aggregatable_values:
“Items, Campaign”: 16384
“Value, Campaign”: 11469
“⊥, Campaign”: 4915 Ad-tech Advertiser
Histogram Contributions
key: “Items, Thanksgiving ”, value: 16384
key: “Value, Thanksgiving ”, value: 11469
key: “⊥, Thanksgiving ”, value: 4915
Browser
Figure 2: Histogram contributions generation.
Algorithm 4 ReconstructValuesR
Params: ⊲ Queries𝑞1,...,𝑞 𝑑 :Z→ R≥0,
⊲ Partition ofZ =Z1⊔···⊔Z 𝑚,
⊲ Parameter𝐶 and scale parameters𝛽1,...,𝛽 𝑑.
ForA as in Algorithm 3,𝛽ℓ =𝐶ℓ
. j𝛼ℓ Γ
𝐶
k
.
Input: Summary report𝑊∈ Z𝐾 for𝐾 =[𝑚]×([ 𝑑]∪{⊥})
Output:𝑈∈ R(𝑑+1)×𝑚 with𝑈𝑘,𝑗 corresponding to slice𝑗, query
𝑞ℓ.
for slice 𝑗∈[ 𝑚] do
for ℓ∈[ 𝑑] do
𝑈ℓ,𝑗 ← 𝑊ℓ,𝑗·𝛽ℓ
𝑈0,𝑗 ← (𝑊⊥,𝑗+ ˝ ℓ∈[𝑑]𝑊ℓ,𝑗) .  Γ 𝐶 
return 𝑈
Theorem 4.2. For𝑈 returned by conjunction of Algorithms 1, 2, 4
and 6 as in Figure 1, it holds for all ℓ∈[ 𝑑], that
E[𝑈ℓ,𝑗] = ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z 𝑥 𝑗 clip𝐶ℓ(𝑞ℓ(𝑧)),
and E[𝑈0,𝑗] = ˝ 𝑥∈𝑋𝑗|Z 𝑥 𝑗|.
Moreover, the variances are given as,
Var(𝑈ℓ,𝑗) ≤
 ˝
𝑥∈𝑋𝑗|Z
𝑥
𝑗|
4 + Var(DLap(𝜀/Γ))
!
·𝐶2 ℓ
. j𝛼ℓ Γ
𝐶
k 2
,
and Var(𝑈0,𝑗) = Var(DLap(𝜀/Γ))·( 𝑑+ 1)
.  Γ
𝐶
 2 .
Proof. It is easy to see that
𝑊ℓ,𝑗 = ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z 𝑥 𝑗 RR j𝛼ℓ Γ 𝐶 k · clip𝐶ℓ(𝑞ℓ(𝑧)) 𝐶ℓ  + DLap 𝜀 Γ .
Using the fact that E[RR(𝜔)] =𝜔 and Var(RR(𝜔))≤ 1 4 , we get
E[𝑊ℓ,𝑗] = ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z 𝑥 𝑗 j𝛼ℓ Γ 𝐶 k · clip𝐶ℓ(𝑞ℓ(𝑧)) 𝐶ℓ ,
Var(𝑊ℓ,𝑗) ≤˝ 𝑥∈𝑋𝑗 |Z
𝑥
𝑗|
4 + VarDLap 𝜀 Γ  .
610

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
Imp. features𝒙 Conv. features𝒚 Histogram Contributions𝒘𝒛
Imp. ID Camp. City #items value ($) 𝑤1,Th 𝑤2,Th 𝑤⊥,Th 𝑤1,Ch 𝑤2,Ch 𝑤⊥,Ch
𝑧1→ 123 Th N.Y. 3 21
A
−−→ 16384 11469 4915 0 0 0
C
−→✓
𝑧2→ 123 Th N.Y. 1 5
A
−−→ 8192 2731 21845 0 0 0
C
−→✓
𝑧3→ 456 Th Boston 1 99
A
−−→ 8192 16384 8192 0 0 0
C
−→✓
𝑧4→ 123 Th N.Y. 2 23
A
−−→ 16384 12561 3823 0 0 0
C
−→×
𝑧5→ 101 Ch Boston 2 50
A
−−→ 0 0 0 16384 16384 0
C
−→✓
𝑧6→ 789 Ch N.Y. 3 15
A
−−→ 0 0 0 16384 8192 8192
C
−→✓
𝑧7→ 101 Ch Boston 1 5
A
−−→ 0 0 0 8192 2731 21845
C
−→✓
↓
S
32768 30584 34952 40960 27307 30037
Sum of aggregatable reports
+
-2472 -993 -392 178 904 668
DLap(𝜀/Γ)⊗𝐾
⇐=30296 29591 34560 41138 28211 30705
Summary report
↓
Final estimate
R
Camp. #items value ($) count
Th 3.70 54.18 2.88
Ch 5.02 51.66 3.05
True values for comparison
Camp. #items value ($) count
Th 7 148 4
Ch 6 70 3
Figure 3: Summary report generation on dataset in Table 1 using 𝑪 = 2,𝑪1 = 2,𝑪2 = $30 and𝜶1 =𝜶2 = 0.5, with slices defined
for each campaign.
Similarly, we have that
˝𝑑
ℓ=1𝑊ℓ,𝑗+𝑊⊥,𝑗 = ˝ 𝑥∈𝑋𝑗  Γ 𝐶  ·|Z 𝑥 𝑗|+ ˝𝑑 ℓ=0 DLap(𝜀/Γ),
and hence
E
h˝𝑑
ℓ=1𝑊ℓ,𝑗+𝑊⊥,𝑗
i
= ˝ 𝑥∈𝑋𝑗  Γ 𝐶  ·|Z 𝑥 𝑗|,
Var
˝𝑑
ℓ=1𝑊ℓ,𝑗+𝑊⊥,𝑗

= (𝑑+ 1)· Var(DLap(𝜀/Γ)).
The proof is now complete by observing that 𝑈ℓ,𝑗 and𝑈0,𝑗 are
simply scaled versions of𝑊ℓ,𝑗 and𝑊⊥,𝑗+˝𝑑 ℓ=1𝑊ℓ,𝑗 respectively. □
In Figure 3, we provide a complete walk-through of how each
of the algorithms A,C,S, andR (in Figure 1) operate on the
dataset in Table 1. We start with the input records𝑧1,...,𝑧 7 in the
top left. AlgorithmA is then applied to each record, clipping the
number of items to𝐶1 = 2, rescaling by⌊𝛼1Γ/𝐶⌋/𝐶1 = 8192 and
applying randomized rounding, and similarly clipping the price to
$30, rescaling by⌊𝛼2Γ/𝐶⌋/𝐶2 = 8192 and applying randomized
rounding, as described in Section 4.1. Algorithm C then applies
contribution bounding, producing aggregatable reports using the
histrogram contributions for six of the records but not for𝑧4, since
theℓ1 contribution budget Γ for impression 123 has already been
used up by records𝑧1 and𝑧2. For each query{1, 2,⊥} and campaign
{Th, Ch}, AlgorithmS then sums the aggregatable reports for that
aggregation key and adds Discrete Laplace noise, producing the
summary report in the middle left of the figure. Finally, algorithm
R takes this summary report and rescales the values to obtain the
final estimate in the lower left. This entails multiplying the first
and fourth values in the summary report by 𝛽1 = 𝐶1/
j𝛼1Γ
𝐶
k
=
1/8192 to get the estimated number of items for the two campaigns,
and the second and fifth values by 𝛽2 = 𝐶2/
j𝛼2Γ
𝐶
k
= 15/8192
to get the estimated values for the two campaigns. The estimated
counts for each campaign are obtained by adding all three summary
report values corresponding to the campaign (the first three values
for campaign Th, the last three for campaign Ch) and scaling by
1/⌊Γ/𝐶⌋ = 1/32768.
We can compare the estimates obtained to the true total values
for each campaign in the lower right of the figure. The estimated
values in this walk-through are far from the true values for two
reasons: the dataset is too small to provide good accuracy, and the
value of𝐶2 = $30 means that large values such as $99 and $50 get
clipped to $30.
4.3 Optimization of Parameters
Having understood the variance in the estimates, we turn to
the question of understanding the optimal choice of parameters𝐶,
(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑], with the goal of minimizing RMSRE𝝉(𝑈,(𝑞ℓ)𝑑 ℓ=0;𝐷).
In this section, we optimize the choice of parameters, using knowl-
edge of the dataset 𝐷. This is admittedly circular, as we are using
an𝜀-DP mechanism to learn information about a dataset we do not
know. However, the eventual goal is that we will optimize the pa-
rameters using a historical dataset𝐷′, which is “similarly behaved”
611

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
Algorithm 5 ParameterOptimization
Params: ⊲ Queries𝑞1,...,𝑞 𝑑 :Z→ R≥0
⊲ Partition ofZ =Z1⊔···⊔Z 𝑚.
Input: Dataset𝐷∈Z∗
Output: Parameters𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] with ˝𝑑 ℓ=1𝛼ℓ = 1.
𝑅current←∞
𝐶max← max𝑥∈𝑋|Z𝑥| (max conversions for an impression)
for b𝐶 = 1, 2,...,𝐶 max do
(b𝐶ℓ, b𝛼ℓ)ℓ∈[𝑑]← argmin(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]𝑅(b𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑])
if𝑅(b𝐶,(b𝐶ℓ, b𝛼ℓ)ℓ∈[𝑑]) <𝑅current then
(𝐶∗ ℓ,𝛼∗ ℓ)ℓ∈[𝑑]←( b𝐶ℓ, b𝛼ℓ)ℓ∈[𝑑]
𝐶∗←𝐶
𝑅current←𝑅(b𝐶,(b𝐶ℓ, b𝛼ℓ)ℓ∈[𝑑])
return 𝐶∗,(𝐶∗ ℓ,𝛼∗ ℓ)ℓ∈[𝑑]
to𝐷 and as we show in Section 6, this is a reasonable choice as
long as the two datasets are drawn from the same distribution.
We stress that, since our optimization procedure is performed
using the dataset𝐷′ that is assumed to be public, this has no effect
on the DP guarantee of the sensitive dataset𝐷.
We focus on minimizing RMSRE𝝉(𝑈,(𝑞ℓ)𝑑 ℓ=0;𝐷)2 as a function
of𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]. The optimization problem we solve is as follows.
Problem 1. Given a fixed dataset 𝐷, a partition of the data uni-
verse into𝑚 slicesZ1,··· ,Z𝑚, and 𝑑+ 1 queries𝑞0,...,𝑞 𝑑, let
𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] be decision variables. For each𝑗∈[ 𝑚],𝑞∈{𝑞0,...,𝑞 𝑑},
let𝑉𝐷(𝑞)𝑗 := ˝ 𝑧∈𝐷∩Z𝑗𝑞(𝑧) and𝑈 =R◦S◦C 𝑘◦A|𝐷|, where
𝑘 denotes the number of impressions in𝐷 and the algorithms are
called on dataset 𝐷 with the parameters specified by the other
variables. Minimize the objective function
𝑅(𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]) :=
√︄
1
(𝑑+1)𝑚
𝑑˝
ℓ=0
˝
𝑗∈[𝑚]
E
 𝑈ℓ,𝑗−𝑉𝐷(𝑞ℓ)𝑗
max{𝜏ℓ,𝑉𝐷(𝑞ℓ)𝑗}
2
,
subject to the constraints𝐶 > 0,𝐶ℓ > 0, and𝛼ℓ > 0 for allℓ∈[ 𝑑],
and ˝𝑑 ℓ=1𝛼ℓ = 1.
As discussed in Appendix B, we can also apply our approach with
other error metrics by replacing RMSRE𝜏 in the objective function
with the desired error metric.
Denoting𝜋ℓ,𝑗 := 1/max{𝜏ℓ,𝑉𝐷(𝑞ℓ)𝑗}2, we can rewrite the objec-
tive as
𝑅(𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑])2 := 1 (𝑑+1)𝑚 𝑑˝ ℓ=0 ˝ 𝑗∈[𝑚] 𝜋ℓ,𝑗· E(𝑈ℓ,𝑗−𝑉𝐷(𝑞ℓ)𝑗)2.
(3)
That is,𝑅 is a linear combination of the following terms for ℓ∈
{0,...,𝑑 } and 𝑗 ∈ [𝑚], for which we can use the bias-variance
decomposition, namely
E(𝑈ℓ,𝑗−𝑉𝐷(𝑞ℓ)𝑗)2 = (𝑉𝐷(𝑞ℓ)𝑗− E𝑈ℓ,𝑗)2 + Var(𝑈ℓ,𝑗).
Thus, we can choose the optimal parameters using a procedure as de-
scribed in Algorithm 5. Namely, we enumerate over various values
of𝐶, and fixing𝐶 = ˆ𝐶, we optimize over the choice of(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑],
and finally choose the value of𝐶 and(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] that minimizes
𝑅(𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]). The challenging step is the one computing
argmin(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]𝑅(b𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]). In our experiments, we use
the method scipy.optimize.minimize [7], but in general any off-
the-shelf optimizer could be used. In the worst-case, even if we do
not minimize the objective exactly, it is still better than choosing
the parameters in an ad hoc manner.
We show below that in fact𝑅(b𝐶,(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑]) is a non-convex
objective in the parameters (𝐶ℓ,𝛼ℓ)ℓ∈[𝑑], which can be hard to
optimize in general. Nevertheless, we show that the objective is
convex in(𝐶ℓ)ℓ∈[𝑑] and(𝛼ℓ)ℓ∈[𝑑] separately. To recall,
Definition 4.3. A function𝑓 : R𝑡→ R is convex if for all𝑥,𝑦 ∈ R𝑡
and𝜆∈[ 0, 1], it holds that𝑓(𝜆𝑥+( 1−𝜆)𝑦) ≤𝜆𝑓(𝑥)+( 1−𝜆)𝑓(𝑦).
Bias term. To simplify notation, let rem𝐶ℓ(𝑣) :=𝑣− clip𝐶ℓ(𝑣) =
max{0,𝑣−𝐶ℓ}. Forℓ∈[ 𝑑], we have
𝑉𝐷(𝑞ℓ)𝑗− E𝑈ℓ,𝑗
= ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z𝑥 𝑗 𝑞ℓ(𝑧)− ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z 𝑥 𝑗 clip𝐶ℓ(𝑞ℓ(𝑧))
= ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z𝑥 𝑗 ∖Z 𝑥 𝑗 𝑞ℓ(𝑧)+ ˝ 𝑥∈𝑋𝑗 ˝ 𝑧∈Z 𝑥 𝑗 rem𝐶ℓ(𝑞ℓ(𝑧))
=: 𝐵ℓ,𝑗(𝐶)+ 𝐴ℓ,𝑗(𝐶ℓ,𝐶) (4)
We observe thatrem𝐶ℓ(𝑞ℓ(𝑧)) is convex in𝐶ℓ, and hence𝐴ℓ,𝑗(𝐶ℓ)
is a convex function in 𝐶ℓ. Moreover, since(𝑉𝐷(𝑞ℓ)𝑗− E𝑈ℓ,𝑗) is
non-negative, we have the following, where we use the fact that
the square of a non-negative convex function is convex.
Observation 4.4.(𝑉𝐷(𝑞ℓ)𝑗− E𝑈ℓ,𝑗)2 is convex in𝐶ℓ .
Variance term. To simplify the optimization, we use the following
relaxations in our calculations, that are obtained by (i) approximat-
ing Var(DLap(𝑎)) ≈2/𝑎2 for𝑎≪ 1, since we consider 𝜀 ≪ Γ,
(ii) ignoring the variance due to randomized rounding, 8 and (iii)
approximating⌊𝛼ℓ Γ/𝐶⌋ and⌊Γ/𝐶⌋ as𝛼ℓ Γ/𝐶 and Γ/𝐶 respectively.
Relaxation 4.5. We use the following approximations.
Var(𝑈ℓ,𝑗) ≈ 2𝐶2𝐶2 ℓ 𝛼 2 ℓ𝜀2 and Var(𝑈0,𝑗) ≈ 2(𝑑+1)𝐶2 𝜀2 .
Finally, we note that the function𝑎2/𝑏2 is non-convex in(𝑎,𝑏).
Observation 4.6. Under Relaxation 4.5, for fixed 𝐶∈ Z≥0 and
ℓ∈[ 𝑑], Var(𝑈ℓ,𝑗) is
⊲ convex in𝐶ℓ for a fixed 𝛼ℓ .
⊲ convex in𝛼ℓ for a fixed𝐶ℓ .
⊲ non-convex in joint variables(𝐶ℓ,𝛼ℓ).
Putting it together. Thus, combining Observation 4.4 and Obser-
vation 4.6, we have the following.
Theorem 4.7. For fixed𝐶∈ Z≥0, RMSRE𝝉(𝑈,(𝑞ℓ)𝑑 ℓ=0;𝐷)2 is
⊲ convex in(𝐶ℓ)ℓ∈[𝑑] for fixed(𝛼ℓ)ℓ∈[𝑑] , and
⊲ convex in(𝛼ℓ)ℓ∈[𝑑] for fixed(𝐶ℓ)ℓ∈[𝑑] ,
⊲ non-convex in joint variables(𝐶ℓ,𝛼ℓ)ℓ∈[𝑑] .
5 EXPERIMENTAL EV ALUATION
5.1 Datasets
5.1.1 Real-World Datasets.
8The variance due to rounding in𝑊ℓ,𝑗 is at most|𝑋𝑗|· 𝐶/4, which we view as much
smaller than Var(DLap(𝜀/Γ))≈( Γ/𝜀) 2. This is reasonable because, e.g., if 𝜀 = 1,
then(Γ/𝜀) 2 = 232, which is typically order of magnitude larger than|𝑋𝑗|· 𝐶/4 in
practice.
612

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
Ad-tech Real Estate Dataset. This dataset consists of approxi-
mately 100,000 real estate conversions from a 30-day period. We
consider the following attributes: three known impression level
features F1, F2, F3, and two unknown conversion features Price
and Quantity.
Ad-tech Travel Dataset. This dataset consists of approximately
30,000 travel conversions from a 30-day period. We consider the
following attributes: three known impression level features F1, F2,
F3, and two unknown conversion features Price and Quantity.
These proprietary datasets were provided to us by an ad-tech that
wished to remain anonymous. The datasets were collected and used
consistently with local regulations and terms of use.
5.1.2 Synthetic Data. The impact of various options to use the ARA
can be evaluated by testing different configurations. However, such
empirical evaluation would require access to a conversion dataset.
Access to conversion datasets can be restricted and slow due to
privacy concerns, or such data may not be available to practitioners.
One way to address these difficulties is to use synthetic data that
replicates the characteristics of real data that is bucketed by the
summary reports in ARA.
In this context, we present a method for generating synthetic
data through statistical modeling of actual conversion datasets. Ini-
tially, we performed an empirical analysis of these real conversion
datasets to uncover relevant characteristics for ARA. Specifically,
we examined the count and value distributions within these real
conversion datasets. Subsequently, we designed a pipeline that
employs the acquired distribution knowledge to create a realistic
synthetic dataset, customizable by provided input parameters. In
the following sections, we elaborate on the distributions as well as
the process of generating data using this pipeline.
Name Feature type Side
campaignId Categorical(16)
Impressiongeography Categorical(8)
productCategory Categorical(2)
conversionType Categorical(5) Conversionvalue ∈ R≥0
Table 3: Impression and conversion side features.
5.1.3 Dataset Generation. Let us assume Du & Penc runs various
Ad campaigns with the features shown in Table 3. Records relevant
to the ARA are outlined below:
(1) Impressions: For every display of an advertisement, an impres-
sion record is generated on the client side. For a specific key,
e.g., ‘campaignId=1 & geography=3 & productCategory=2’,
there could be a few or numerous impressions. Modeling the
distribution of these impressions is the initial aspect to address.
(2) Conversions: An impression might lead to zero, one, or mul-
tiple conversion events. These conversion events are defined
within the ad-tech context and encompass various activities,
such asclick, add-to-cart, purchase, spend-30-seconds, andachieved-
level-2 to provide a few examples. So the next aspect to model
is the count of conversions per impression, as well as the con-
version features associated to it, such as conversionType.
(3) Value Contributions: Not every conversion yields the same
return for advertisers. For instance, a purchase of $25 might
be more desirable than one of $5. Beyond simply considering
the number of conversions, it is crucial to take into account
the value that these conversions generate. This leads us to the
distribution of conversion values, which captures this aspect.
We propose a pipeline that generates both counts and values as
shown in Figure 4. Here, the data is not aggregated so that event
level processing such as count bounding and contribution budgeted
could be performed. First, we define the distributions that are used
in the pipeline.
Definition 5.1 (Power Law Distributions). The Power Law distribu-
tion with parameter𝑏 > 0 is the distribution supported on positive
integers, whose probability mass function at integer𝑘 is
Pr[𝑋 =𝑘] =
 

𝑘−𝑏 ˝𝑘max
𝑘=𝑘min 𝑘−𝑏 𝑘min≤𝑘≤𝑘max
0 otherwise,
where𝑏 is the shape parameter,𝑘min > 0 is the lower bound and
𝑘max is the upper bound.
A well-behaved distribution typically exhibits parameters of
1 <𝑏 < 3,𝑘min = 1 and𝑘max =∞. However, when working with
real datasets, it is common to observe power-law behavior within a
specific range and arbitrary𝑏 parameter.
Definition 5.2 (Poisson Distribution). The Poisson distribution
with parameter𝜆 > 0 is a discrete probability distribution whose
probability mass function at integer𝑘 is
𝑃(𝑋 =𝑘) = 𝜆𝑘𝑒−𝜆
𝑘! ,
where the parameter𝜆 is the average rate of events.
Definition 5.3 (Log-Normal Distribution). The Log-Normal distri-
bution with parameters𝜇 and𝜎 is a continuous probability distri-
bution whose probability density function is
𝑓(𝑥) = 1
𝜎𝑥
√
2𝜋
exp

−(log𝑥−𝜇)2
2𝜎2

.
Having defined the relevant distributions, we now describe the
data generation in more detail. For convenience of the theoretical
analysis in the next section, we will describe the data generation
for a general choice of distributions:
⊲Dimp count: the distribution of number of impressions per slice. In
our experiments, this is set to the power-law distribution (with
pre-specified parameter𝑏).
⊲Dconv count: the distribution of the number of conversions per im-
pression. In our experiments, this is set to the Poisson distri-
bution (with pre-specified parameter 𝜆). The conversions are
subsequently divided uniformly among the different values of
attributed keys.
⊲Dconv value: the distribution of conversion values. In our experiments,
this is set to the Log-normal distribution (with pre-specified pa-
rameter𝜇,𝜎 ). Figure 5 displays conversion values extracted from
two datasets alongside the corresponding Log-Normal distribu-
tion fit.
613

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
impression
features
1,2,1 3
0,0,0 1
15,7,1 12
impressions (1)
Step 1:
Generate impressions per slice
6
Imp. 1
12
5
Step 2:
Generate conversions for each key
Imp. 3
Imp. 2
conversions (2)
(1) Impressions drawn from power-law distribution.
(2) Conversions drawn from Poisson distribution.
(3) Conversion value drawn from log-normal distribution.
Step 3:
Generate conversion value
15.01,2,1,0Imp 1
12.01,2,1,1Imp 1
9.91,2,1,3Imp 1
8.51,2,1,1Imp 2
6.61,2,1,4Imp 2
value (3)attributed keyimp ID
8.21,2,1,0Imp 2
Figure 4: Overall dataset generation steps with features in
Table 3 used for illustration.
Our data generation pipeline works in the following stages:
Step 1 For each combination of impression features, sample #im-
pressions is independently sampled from the distribution
Dimp count 9. There will be
𝑇 =
Ö
X𝑖∈X
|X𝑖|
attributed slices, whereX represents the set of dimensions
within the impression side. To illustrate, in the sample case
shown in Table 3, there will be𝑇 = 16× 8× 2 slices.
Step 2 For each impression, independently sample #conversion
from the distributionDconv count, and distribute each one uni-
formly at random between the various conversion features.
In the case of Table 3, there are5 values of conversionType.
Step 3 For each conversion, independently sample the conversion
value from the distributionDconv value.
Name Step 1 Step 2 Step 3
𝑏 𝜆 𝜇 𝜎
synth-real-estate 1.03 10 0.87 0 .43
synth-travel 1.14 10 1.95 1 .14
Table 4: Synthetic datasets utilized in evaluations with pa-
rameters that mimic the corresponding real datasets.
Table 4 presents two synthetic datasets that were employed in
evaluations with parameters. It is possible to generate numerous
9Sampling from discrete power-law distributions with arbitrary parameters𝑏 is not
a straightforward process. To address this challenge, we adopted the approximation
method outlined in Appendix D of the work by Clauset et al. in [10]
datasets with specific parameters that closely mimicking the char-
acteristics of a target dataset. This could be particularly useful for
emulating privacy-restricted proprietary ad datasets.
5.2 Setup
We evaluate our algorithms on two real-world datasets and two
synthetic datasets, which are described in more detail in Section 5.1.
Each dataset is partitioned into a training set and a test set. For
the real-world datasets, the partition is based on timestamps; for
the synthetic data, separate training and test sets are generated
independently from the data distribution. The training set is used
to choose contribution budgets and clipping threshold parameters,
and the error is evaluated on the test set. For the synthetic datasets,
the training set is also used to choose a count limit𝐶; for the real-
world datasets only click-level or conversion-level data is available,
so the count limit is set to 1.
We optimize using the Sequential Least-SQuares Programming
(SLSQP) optimizer provided in scipy.optimize.minimize [7], which
is a quasi-Newton method. This optimizer runs in time cubic in the
number of variables of the optimization problem, which is twice the
number of queries𝑑. In our setting, for each dataset and parameter
choice, we have𝑑∈{ 1, 2} and optimization took between 1–75
seconds. Our experiments are based on 15 days of data, but ad-
techs may choose to perform optimization more or less frequently
depending on their data distribution’s temporal stability.
We compare our optimization-based algorithm to severalbaseline
approaches that use fixed contribution budgets 𝛼ℓ and clipping
thresholds𝐶ℓ set to a fixed quantile of the training data. For the
first baselines, we use equal contribution budgets for each query,
including the count query, so that𝛼0 =··· =𝛼𝑑 = 1 𝑑+1 . This is the
approach outlined in the API documentation [20], and represents
the only previously published approach that we are aware of for
using the API. The clipping threshold quantiles used are 95% and
99% for the real-world datasets, and 90% and 95% for the synthetic
datasets. Note that to choose these thresholds, the baselines also
require access to training data.
We also compare against some more tailored baselines that take
into account domain-specific knowledge that an ad-tech using the
API may possess. In particular, the count query tends to be easier
to answer accurately (i.e. incurs lower error for a fixed contribution
budget) than the other queries, due to the fact that all values have
the same scale and no signal is lost due to clipping. Consequently, it
may be desirable to allocate a lower contribution budget to the count
query and a higher contribution budget to the remaining query or
queries. For each dataset we consider two additional contribution
budgeting strategies, setting the contribution budgets to be in a
2:2:1 or 10:10:1 ratio for the real-world datasets and a 2:1 or 5:1 ratio
for the synthetic datasets. For each contribution budget strategy,
we again choose clipping thresholds determined by the 95% and
99% quantiles of the training data for the real-world datasets and
the 90% and 95% quantiles for the synthetic datasets.
For each dataset, we partition it into slices based on one or more
impression features, and estimate multiple queries corresponding to
each slice. For the real-world datasets we consider three queries for
each slice, corresponding to the count and two additional conver-
sion features depending on the dataset. For the synthetic datasets
614

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
Figure 5: Scatter plots of real-world datasets illustrating the probability of observing a conversion value. The fitted curves
represent best log-normal distribution models that effectively capture the underlying patterns in the data.
0 10 20 30 40 50 60
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
0.200RMSRE
AdT ech real estate dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization
(a) Ad-tech real estate
0 10 20 30 40 50 60
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35RMSRE
AdT ech travel dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization (b) Ad-tech travel
0 10 20 30 40 50 60
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35RMSRE
synth-real-estate
Baseline (90%)
Baseline (95%)
Linf optimization (c) synth-real-estate
0 10 20 30 40 50 60
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7RMSRE
synth-travel
Baseline (90%)
Baseline (95%)
Linf optimization (d) synth-travel
Figure 6: RMSRE𝝉 for privacy budgets{1, 2, 4, 8, 16, 32, 64} for our algorithms and baselines on two real-world and two synthetic
datasets. Our optimization-based approach consistently achieves lower error than baselines that use a fixed quantile for the
clipping threshold and split the contribution budget equally among the queries.
we consider two queries for each slice, corresponding to the count
and a single conversion feature.
For the error metric RMSRE𝝉 , for each query𝑞ℓ we choose𝜏ℓ
to be five times the median value of the query on the records of
the training dataset. This ensures invariance of the error metric
to rescaling the data, and allows us to combine the errors from
features of different scales by taking𝝉 =(𝜏0,...,𝜏 𝑑).
5.3 Results
We see in Figure 6 that the estimates produced by our algorithms
have substantially lower error than the baselines, on both the real-
world and synthetic datasets. Moreover, the excess error incurred
by each baseline depends on the data and overall privacy budget,
with different baselines performing better or worse in different
parameter regimes. In contrast, our optimization-based approach
is able to adapt to the privacy budget and data, and consistently
outperforms the baselines, often by a large margin. For the two
real-world datasets the improvements range from 2–36% to 14–66%,
respectively, depending on the value of the privacy parameter𝜀. For
the two synthetic datasets the improvements range from 36–60%
to 18–83%, respectively, again depending on the value of𝜀.10
In Appendix B and Figures 7–8 we show that our algorithmic
approach can also be applied to other error metrics such as RMSE
and ARE, and provides accuracy improvements for these as well.
In fact, for most datasets and parameter choices our algorithm
achieves an even larger improvement over the baselines, as large
as a 96% improvement for RMSE and a 85% improvement for ARE
on the real-world datasets. This underscores the flexibility of our
approach: in contrast to the baselines, which perform inconsistently
depending on the dataset, error metric, and choice of the privacy
parameter, our adaptive approach achieves strong performance in
each setting.
In Appendix C and Figure 9 we show that an ℓ1-based variant
of our optimization-based algorithm in Figure 9 provides modest
additional accuracy improvements on some datasets.
10These improvements are calculated by comparing our algorithm to the best of six
baselines for each dataset and each value of𝜀. Since we run multiple baselines on the
test data and only compare to the best, this may allow the baselines to overfit to the
test data. Consequently, this evaluation may actually understate our improvement on
some inputs.
615

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
6 GENERALIZATION BOUNDS
Since we optimize the parameters on the historical dataset, it is
important to ensure that we are not overfitting to this training
dataset in such a way that it performs badly on the actual (i.e.,
test) dataset. To support our empirical findings, in this section, we
formally prove—in a simplified setting—a generalization bound
showing that the expected RMSRE on the actual dataset is close to
optimal even with this procedure.
We work in the data generation model as in the previous section.
For the purpose of theoretical analysis, we consider a simplified
setting where: (i) there is only one conversion per impression (i.e.,
Dconv count is the point-mass distribution that is always equal to one)
and (ii) that there is only a single query (i.e.,𝑑 = 1).
Recall the notations from Section 4. Due to (i), we always set the
per-impression count capping to𝐶 = 1; this also givesZ𝑥 =Z 𝑥
for all impression𝑥. For convenience, we also define the following
notations:
bi𝐶1(𝐷𝑗) :=
∑︁
𝑥∈𝑋𝑗
∑︁
𝑧∈Z𝑥
rem𝐶1(𝑞1(𝑧)𝑗),
nc𝐶1(𝐷𝑗) :=
∑︁
𝑥∈𝑋𝑗
∑︁
𝑧∈Z𝑥
1[𝑞1(𝑧)𝑗 >𝐶1],
𝜋(𝐷𝑗) := max{𝜏1,𝑉𝐷(𝑞1)𝑗},
𝑅𝐷𝑗(𝐶1) := 1 𝜋(𝐷𝑗)2

bi𝐶1(𝐷𝑗)2+ 2𝐶2 1 𝜀2 ! ,
where recall that 𝑋𝑗 is the set of all 𝑥 such that(𝑥,𝑦) ∈𝐷𝑗 for
some𝑦, and𝑅 is similar to Equation (3), but here, we only have
one argument, namely𝐶1. bi𝐶1(𝐷𝑗) is the bias incurred in the es-
timate due to clipping; this is similar to the term in Equation (4),
and nc𝐶1(𝐷𝑗) counts the number of conversion values that were
clipped by the threshold at𝐶1. As stated earlier, we assume that
the number of impressions in the𝑗th slice is generated byDimp count
(with one conversion per impression) and the value of each conver-
sion is generated independently byDconv value. We denote this entire
compound distribution byDcomp.
Finally, we let
˜𝑅Dcomp(𝐶1) := E𝐷∼D comp[𝑅𝐷(𝐶1)],
denote the expected loss𝑅𝐷(𝐶1), where𝐷 is drawn from the dis-
tributionDcomp.
In this simplified setting, the optimization objective reduces to
just minimizing
𝑅𝐷1,...,𝐷𝑚(𝐶1) := 1 𝑚 𝑅𝐷1(𝐶1)+···+ 𝑅𝐷𝑚(𝐶1)
= 1 𝑚 ∑︁ 𝑗∈[𝑚] 1 𝜋(𝐷𝑗)2

bi𝐶1(𝐷𝑗)2+ 2𝐶2 1 𝜀2 ! .
Differentiating this (w.r.t.𝐶1), we get
𝜕
𝜕𝐶1
𝑅𝐷1,...,𝐷𝑚(𝐶1)
= 1 𝑚 ∑︁ 𝑗∈[𝑚] 1 𝜋(𝐷𝑗)2  4𝐶1 𝜀2 − 2bi𝐶1(𝐷𝑗)· nc𝐶1(𝐷𝑗)  .
In other words, the optimum contribution bounding threshold𝐶∗ 1 =
𝐶∗ 1(𝐷1,...,𝐷 𝑗) is such that
∑︁
𝑗∈[𝑚]
1
𝜋(𝐷𝑗)2
 4𝐶∗ 1
𝜀2 − 2bi𝐶∗ 1(𝐷𝑗)· nc𝐶1(𝐷𝑗)

= 0.
Let𝜇𝑛(D) denote the𝑛th moment of the distributionD over
R, namely,𝜇𝑛(D) = E𝑥∼D|𝑥|𝑛. We can get the following general-
ization bound. Note that the LHS is the expected error of the fresh
(independent) slice if we optimize based on the 𝐷1,...,𝐷 𝑚 (i.e.,
historical data) drawn from the same distributionDcomp, while the
RHS is the expected error with respect to the optimal threshold for
the distribution.
Theorem 6.1. For any distributionsDimp count,Dconv value such that the
moments 𝜇4(D imp count) and 𝜇2(D conv value) are finite. For any 𝜁,𝜃 > 0,
there exists𝑚∈ N such that, with probability 1−𝜁 over𝐷1,...,𝐷 𝑚∼
Dcomp, and using𝐶∗ 1 =𝐶∗ 1(𝐷1,...,𝐷 𝑚), we have
˜𝑅Dcomp(𝐶∗ 1) ≤ min ˜𝐶1≥0 ˜𝑅Dcomp( ˜𝐶1)+ 𝜃.
Proof. Let ˜𝐶∗ 1 = argmin ˜𝐶1≥0 ˜𝑅Dcomp( ˜𝐶1) denote the optimal
clipping threshold of the distribution. Since ˜𝑅Dcomp( ˜𝐶1) is a contin-
uous function, there exists𝜆 > 0 such that
˜𝑅Dcomp(𝐶1)− ˜𝑅Dcomp( ˜𝐶∗ 1)≤ 𝜃. ∀𝐶1∈[ ˜𝐶∗ 1−𝜆, ˜𝐶∗ 1+𝜆]. (5)
Furthermore, let𝜈 := E[ 1 𝜋(𝑋) 2] > 0.
Recall that
𝜕
𝜕𝐶1
˜𝑅𝑋( ˜𝐶∗ 1) = 1 𝜋(𝑋)2

4 ˜𝐶∗ 1
𝜀2 − 2bi ˜𝐶∗ 1 (𝑋)· nc ˜𝐶∗ 1 (𝑋)
!
.
Note that E𝑋∼D comp
h
𝜕
𝜕𝐶1
˜𝑅𝑋( ˜𝐶∗ 1) i = 0 (due to ˜𝐶∗ 1 being the mini-
mizer). Furthermore, we have
E𝑋∼D comp
" 𝜕
𝜕𝐶1
˜𝑅𝑋( ˜𝐶∗ 1)
2#
≤𝑂

1
𝜋 2

( ˜𝐶∗ 1)2
𝜀4 + bi ˜𝐶∗ 1 (𝑋)2· nc ˜𝐶∗ 1 (𝑋)2
!!
≤𝑂

1
𝜋 2

( ˜𝐶∗ 1)2
𝜀4 + bi0(𝑋)2· nc0(𝑋)2
!!
=𝑂

1
𝜋 2

( ˜𝐶∗ 1)2
𝜀4 +𝜇2(D conv value)𝜇4(D imp count)
!!
,
which is finite under the assumption in the theorem statement.
Thus, 𝜕 𝜕𝐶1 ˜𝑅𝑋( ˜𝐶∗ 1) when𝑋∼D comp, ˜𝑅′ 𝑋( ˜𝐶∗ 1) has a finite variance.
Similarly, the term 1 𝜋(𝑋) 2 has a finite variance, simply because
its maximum value is at most 1/𝜏 2 1. Thus, for any 𝜁,𝜃 > 0, there
exists𝑚0 such that for any 𝑚≥ 𝑚0, with probability 1−𝜃 over
𝐷1,...,𝐷 𝑚∼D comp, both of the following hold:

 𝜕 𝜕𝐶1 𝑅𝐷1,...,𝐷𝑚(𝐶1)

 =

 1 𝑚 ∑︁ 𝑗∈[𝑚] 𝜕 𝜕𝐶1 𝑅𝐷𝑗(𝐶∗ 1)

 ≤ 4𝜆𝜈/𝜀2,
616

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
and
1
𝑚
∑︁
𝑗∈[𝑚]
1
𝜋(𝐷𝑗)2≥𝜈/2.
Now, notice that the objective𝑅𝐷1,...,𝐷𝑚(𝐶1) is

4
𝑚𝜀 2
˝
𝑗∈[𝑚] 1 𝜋(𝐷𝑗) 2

-
strongly convex. As a result, when the above two inequalities hold
we have
| ˜𝐶∗ 1−𝐶∗ 1|≤

 𝜕 𝜕𝐶1𝑅𝐷1,...,𝐷𝑚(𝐶1)

 
4
𝑚𝜀 2
˝
𝑗∈[𝑚] 1 𝜋(𝐷𝑗) 2
 ≤𝜆.
From (5), this implies ˜𝑅Dcomp(𝐶∗ 1)− ˜𝑅Dcomp(𝐶∗ 1). □
We remark that, due to the use of continuity argument of˜𝑅Dcomp
(at ˜𝐶∗ 1), we do not achieve any explicit bound in the rate of conver-
gence. It remains an interesting question to extend this argument
to get a specific rate. Similarly, it remains interesting to incorporate
the privacy budgets (i.e.,𝛼ℓ’s) in the presence of multiple queries
to the bounds as well.
7 RELATED WORK
The work closest to ours is that on optimizing hierarchical queries
when using the Attribution Reporting API [12]. In our terminology,
this corresponds to aggregating with respect to multiple partitions
ofZ that are refinements of each other; our work is complementary
in that we focused on a single partition. In addition, our setting in-
volves aggregating different conversion values for each slice. Thus,
while [12] optimized for contribution budget allocation across dif-
ferent slices, our work optimizes the contribution budget allocation
across the different queries for each slice. Furthermore, [12] also
involved post-processing the estimates that ensured consistency of
estimates and reduced the overall noise; this was done by generaliz-
ing the methods in [11, 16]. Such post-processing is not relevant in
our context as we do not have any consistency constraints that are
satisfied by the noiseless data. Hence, it is possible to combine the
techniques in our work with the techniques in [12] to consider a set-
ting where we have hierarchical queries with multiple conversion
values to aggregate.
Private aggregation by contribution bounding and adding noise
is a common technique in DP. It was shown in [9] that in order to
minimize theℓ1-error, the optimal threshold is to set the contribu-
tion bound to be the(1−1/𝜀𝑛)th percentile of the data. On the other
hand, in order to minimize theℓ2 2 -error, it was shown in [17] that
bounding the range and adding Laplace noise achieves the smallest
error, thereby establishing a bias-variance-privacy trilemma; this is
precisely what we get in our approach as well, where we clip the
value range and add (discrete) Laplace noise, by optimizing the clip
threshold using historical data.
8 LIMITATIONS AND FUTURE DIRECTIONS
One limitation of our approach is that it relies on access to noise-
less historical data in order to optimize the contribution bounding
parameters for querying future data. While such non-contribution
bounded noiseless data might still be available for long-running
campaigns, new campaigns launched well after the deprecation of
third-party cookies would benefit from methods for continuously
updating the contribution bounding parameters based solely on the
outputs of privacy-preserving APIs.
A very interesting direction for future work is to develop al-
gorithms that rely on noisy privatized historical data or privately
generated aggregate statistics for historical data instead of noiseless
historical data. An approach based on this work would be to learn
the parameter(s) of the synthetic data distribution using past data,
and then sample repeatedly from this distribution to construct a
synthetic dataset that can be used for privacy budgeting for queries
on future data.
Another limitation is that the optimization problem is discrete,
since the contribution budgets must be positive integers. To avoid
the computational challenges of discrete optimization, we instead
work with a continuous approximation of the optimization problem.
Our results show that working with this continuous approximation
is sufficient for obtaining a high-accuracy solution to the original
discrete problem.
In addition to summary reports, ARA offersevent-level reports [4]
which are also subject to (a different type of) contribution bounding
and noising; our method does not take these reports into account
when setting the contribution bounds for summary reports. It would
be interesting to explore whether event-level reports can be lever-
aged to optimize the summary reports in ARA.
As described in Section 3.1, summary reports in ARA are cur-
rently restricted by on-client attribution and by the separate com-
putation of the contributions of different attributed conversions.
It would be interesting to determine the utility improvement that
could be achieved if the contributions of different attributed con-
versions can be computed jointly, e.g., if attribution were to be done
off-client either in a trusted execution environment or via a secure
multi-party computation protocol, or alternatively if the contri-
butions of an attributed conversion can simply take into account
the contributions of previously attributed conversions on the same
client.
9 CONCLUSION
In this work, we studied the optimization of summary reports in
the ARA, which is currently deployed on hundreds of millions of
Chrome browsers. To the best of our knowledge, there has been no
prior work formulating the contribution budgeting optimization
problem for ARA. We hope that our rigorous formulation will equip
researchers with the right abstraction of the problem as well as the
API to develop DP algorithms for ad conversion measurement with
better privacy-utility trade-offs.
Our recipe, which leverages past data that is noiseless and that
has not been bounded, in order to bound the contributions in future
data when querying it with DP, is quite general and applicable to set-
tings (beyond advertising) where a system is queried continuously
over time, and a DP constraint is being continuously enforced.
ACKNOWLEDGMENTS
This research received no specific grant from any funding agency
in the public, commercial, or not-for-profit sectors.
REFERENCES
[1] Aggregation service for the attribution reporting api. https://github.com/WICG/
attribution-reporting-api/blob/main/AGGREGATION_SERVICE_TEE.md.
617

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
[2] Attribution reporting: Aggregatable reports api. https://developer.android.com/
design-for-safety/privacy-sandbox/attribution#aggregatable-reports-api.
[3] Attribution Reporting API with Aggregatable Reports: Privacy Considerations.
https://github.com/WICG/attribution-reporting-api/blob/main/AGGREGATE.
md#privacy-considerations.
[4] Attribution Reporting: Event-level Reports. https://developer.android.com/
design-for-safety/privacy-sandbox/attribution#event-level-reports.
[5] Contribution budget for summary reports. https://developer.chrome.com/docs/
privacy-sandbox/attribution-reporting/contribution-budget/.
[6] MaskedLARk. https://github.com/microsoft/maskedlark.
[7] scipy.optimize.minimize.
[8] SKAdNetwork. https://developer.apple.com/documentation/storekit/
skadnetwork/.
[9] Amin, K., Kulesza, A., Munoz, A., and V assilvtiskii, S. Bounding user con-
tributions: A bias-variance trade-off in differential privacy. In ICML (2019),
pp. 263–271.
[10] Clauset, A., Shalizi, C. R., and Newman, M. E. Power-law distributions in
empirical data. SIAM Review 51, 4 (2009), 661–703.
[11] Cormode, G., Procopiuc, C., Srivastava, D., Shen, E., and Yu, T. Differentially
private spatial decompositions. In ICDE (2012), pp. 20–31.
[12] Dawson, M., Ghazi, B., Kamath, P., Kumar, K., Kumar, R., Luan, B., Manu-
rangsi, P., Mundru, N., Nair, H., Sealfon, A., and Zhu, S. Optimizing Hierar-
chical Queries for the Attribution Reporting API. In AdKDD (2023).
[13] Dwork, C., McSherry, F., Nissim, K., and Smith, A. D. Calibrating noise to
sensitivity in private data analysis. In TCC (2006), pp. 265–284.
[14] Dwork, C., and Roth, A. The algorithmic foundations of differential privacy.
Foundations and Trends® in Theoretical Computer Science 9 , 3–4 (2014), 211–407.
[15] Gozman, V. The slow death of third-party cookies. Forbes, September
2022. https://www.forbes.com/sites/theyec/2022/09/12/the-slow-death-of-third-
party-cookies/amp/.
[16] Hay, M., Rastogi, V., Miklau, G., and Suciu, D. Boosting the accuracy of
differentially-private histograms through consistency. VLDB (2010).
[17] Kamath, G., Mouzakis, A., Regehr, M., Singhal, V., Steinke, T., and Ullman,
J. A bias-variance-privacy trilemma for statistical estimation. In TPDP (2023).
[18] Kruppa, M., and Haggin, P. Google is finally killing cookies. Advertisers still
aren’t ready. Wall Street Journal, January 2024. https://www.wsj.com/tech/
google-is-finally-killing-cookies-advertisers-still-arent-ready-7582fcac.
[19] Nadan, A., White, A., Cucu, A., Nalpas, M., and Mastromatto, Z. Experiment
with summary report design decisions, November 2022. https://developer.chrome.
com/docs/privacy-sandbox/summary-reports/design-decisions/.
[20] Nalpas, M., and White, A. Attribution Reporting, May 2021. https://developer.
chrome.com/en/docs/privacy-sandbox/attribution-reporting/.
[21] Pfeiffer III, J. J., Charles, D., Gilton, D., Jung, Y. H., Parsana, M., and Ander-
son, E. Masked LARk: Masked learning, aggregation and reporting workflow.
arXiv preprint arXiv:2110.14794 (2021).
[22] Schuh, J. Building a more private web: A path towards making third party
cookies obsolete, January 2020. https://blog.chromium.org/2020/01/building-
more-private-web-path-towards.html.
[23] Thomson, M. Privacy Preserving Attribution for Advertising, February
2022. https://blog.mozilla.org/en/mozilla/privacy-preserving-attribution-for-
advertising/.
[24] White, A. Summary reports, November 2022. https://developer.chrome.com/
docs/privacy-sandbox/summary-reports/.
[25] Wilander, J. Full Third-Party Cookie Blocking and More, March 2020. https:
//webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/.
[26] Wilander, J. Introducing Private Click Measurement, PCM, February 2021.
https://webkit.org/blog/11529/introducing-private-click-measurement-pcm/.
[27] Wood, M. Today’s Firefox Blocks Third-Party Tracking Cookies and Cryptomin-
ing by Default, 2019. https://blog.mozilla.org/en/products/firefox/todays-firefox-
blocks-third-party-tracking-cookies-and-cryptomining-by-default/.
618

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
A ERROR METRICS FOR EV ALUATING
REPORTS
In Table 5 above, we specify all metrics considered for utility evalu-
ation.
To choose a particular metric, we considered the desirable prop-
erties of an error metric that further can be used as an objective
function. Ideally, a good error metric should have the following
properties:
(1) Decision Stability: Some of our metrics are parameterized.
(E.g., RMSRE𝝉 is parameterized by𝝉; see Definition 3.2.) For a
good metric, the decision from our optimization procedure (e.g,
count bound, contribution budgeting, etc.) should not be too
sensitive to the choice of parameters.
(2) Utility Stability: The utility measured by the metric is robust
to perturbations in the input (e.g., true conversion count). For
instance, the metric’s output should not change too much if
the true conversion count is slightly changed. This is important
because the true conversion count is often difficult to measure
accurately.
(3) Ease of Optimization: The metric is easy to calculate, and the
objective function based on it is easy to be optimized.
(4) Ease of Extension : The metric should be easy to extend to
aggregates after keyspace aggregation. The metric is for a slice
in aggregate API, which is any possible combination of keys
(keyspace value). For example, a slice for an advertiser may look
like: impression_date=‘8/1’, biddability=‘True’ . To get
the total number of biddable conversions, one needs to sum up
all noised counts from slices with biddability=‘True’. This
accumulates a bunch of Laplace noise random variables, which
is no longer Laplace. It is desirable that the slice error metric
can be easily adapted to aggregates after keyspace aggregation.
(5) Defined at Zero : The metric should be well-defined when
conversion query value is zero. This is important since the
conversion data can be sparse.
(6) Differentiates Small/Large Values: The metric should differ-
entiate between large and small query values. Intuitively, this is
because noise added to large values will usually have less effect
on downstream tasks compared to the same amount of noise
added to small values.
Table 6 provides the list of criteria that each metric satisfies.
Intuition for RMSRE𝜏 . RMSRE𝜏 can be seen as a hybrid between
additive and multiplicative error. When the query values are smaller
than the threshold𝜏, it becomes (a scaled version of) the root mean
squared error RMSE. Recall that
RMSE(𝑢,𝑞 ;𝐷) :=
vt 1
𝑚
∑︁
𝑗∈[𝑚]
E 𝑢𝑗−𝑉𝐷(𝑞)𝑗 2.
Meanwhile, if the query values are larger than𝜏, then it becomes
the root mean square relative error, defined as
RMSRE(𝑢,𝑞 ;𝐷) :=
vut 1
𝑚
∑︁
𝑗∈[𝑚]
E
𝑢𝑗−𝑉𝐷(𝑞)𝑗
𝑉𝐷(𝑞)𝑗
2
.
To give an intuition as to why RMSRE𝜏 is a good metric, we can
compare them with RMSE and RMSRE. The main advantage of
RMSRE𝜏 over RMSE is that RMSRE𝜏 can distinguish between the
small and large values (criteria (6) above). Meanwhile, RMSRE𝜏 is
defined even when the query values are zero, whereas RMSRE is
undefined (criteria (5) above).
B OPTIMIZATION FOR DIFFERENT ERROR
METRICS
We now show that our optimization algorithm also works well for
alternate error metrics besides RMSRE𝜏 . In particular, we show
experimental results optimizing for the error metrics RMSE in
Figure 7 and for ARE0.1 in Figure 8. In each plot we see that our
algorithm outperforms the baselines, often substantially.
Our method can also be applied to a variety of other error metrics,
including those described in Table 5. For each of these metrics, we
can compute or estimate the expected error or expected squared
error for a given setting of hyperparameters, and optimize over
these hyperparameters. For RMSE, like RMSRE𝜏 , we can represent
the error as a combination of the variance from noise addition
and the bias from clipping; for ARE we can compute the error by
evaluating the cumulative density function of the error distribution
at inputs that depend on the bias from clipping. Many of the other
error metrics in Table 5 can be computed similarly.
In some of the experiments, particularly for RMSE on the real-
world datasets (the first two panels of Figure 7), the baselines per-
form quite poorly, and it is likely that using a different quantile
would improve performance somewhat. Unlike the baselines, which
have varied performance depending on the dataset, the error met-
ric, and the privacy parameter𝜖, our optimization-based algorithm
consistently has the lowest error in each setting.
In a few of these experiments, the optimizer was unsuccessful
at finding the minimum-error parameters. This is most visible in
the small-𝜖 values of Figure 7(a), where the reported errors for
our algorithm are not quite monotonically decreasing in𝜖 as we’d
expect. It is likely that tweaking to the optimizer parameters or
using a different optimization library would improve the accuracy
on these inputs. Despite not necessarily achieving the true optimum
and exiting with a failure status on a few inputs, the optimizer
still obtained hyperparameters with error much smaller than the
baseline error.
C ℓ1 VERSION OF ALGORITHM 3
We present a variant of HistogramContribution in Algorithm 6,
which usesℓ1-clipping instead ofℓ∞-clipping that is employed in
Algorithm 3. We show in Figure 9 that this variant can achieve a
modest improvement to performance on some inputs. The main
intuition for this algorithm is thatℓ1-clipping results in less loss of
signal, especially when the different query values are negatively
correlated or only weakly correlated with each other. Below, we
show that the histogram contributions generated this way respect
the sameℓ1-norm constraint as Algorithm 3.
Figure 9 shows the improvement achieved by this variant on the
ad-tech real estate and travel datasets. For the synthetic datasets
theℓ1-optimization is equivalent toℓ∞-optimization, since there is
only a single non-count query on these datasets.
Lemma C.1. For any 𝑧, the vector 𝑤𝑧 returned by Algorithm 6
satisfies𝑤𝑧≥ 0 and∥𝑤𝑧∥1 =⌊Γ/𝐶⌋.
619

Proceedings on Privacy Enhancing Technologies 2024(4) Aksu et al.
Short Name Error Metric (slice 𝑗) Sample Parameters Interpretation
ARE𝛼 Pr
h|𝑈𝑗−𝑉(𝑞)𝑗|
𝑉(𝑞)𝑗 >𝛼
i
𝛼∈{ 0.1, 0.2} Probability of seeing large relative error.
AME𝜏 Pr

|𝑈𝑗−𝑉(𝑞)𝑗| >𝜏

𝜏∈{ 1, 5} Probability of seeing large magnitude errors.
APME𝛼,𝜏 Pr
h|𝑈𝑗−𝑉(𝑞)𝑗|
𝑉(𝑞)𝑗 >𝛼∩|𝑈𝑗−𝑉(𝑞)𝑗| >𝜏
i
𝛼∈{ 0.2},𝜏 ∈{ 1, 5} Probability of seeing large magnitude and relative errors.
EARE E
h|𝑈𝑗−𝑉(𝑞)𝑗|
𝑉(𝑞)𝑗
i
Expected absolute relative error (to true value).
RMSE
√︂
E
h𝑈𝑗−𝑉(𝑞)𝑗 2i Root mean squared error.
RMSRE
√︄
E
𝑈𝑗−𝑉(𝑞)𝑗
𝑉(𝑞)𝑗
2
Root mean squared relative error.
EARE𝜏 E
h |𝑈𝑗−𝑉(𝑞)𝑗|
max(𝜏,𝑉(𝑞)𝑗)
i
𝜏∈{ 3, 5, 10} Mean absolute relative error at threshold𝜏.
EAREO E
h|𝑈𝑗−𝑉(𝑞)𝑗|
𝑈𝑗
i
Expected absolute relative error (to observation).
RMSRE𝜏
√︄
E
 |𝑈𝑗−𝑉(𝑞)𝑗|
max(𝜏,𝑉(𝑞)𝑗)
2
𝜏∈{ 3, 5, 10} Root mean squared relative error at threshold𝜏.
Table 5: Error metrics considered for noise impact measurement. 𝑼𝒋 is observed and 𝑽(𝒒)𝒋 true value.
Metric−→ ARE𝛼 AME𝜏 APME𝛼,𝜏 EARE RMSE RMSRE EARE 𝜏 EAREO RMSRE 𝜏
Decision Stability × ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
Utility Stability ✓ ✓ ✓ ✓ ✓ ✓ ✓ × ✓
Ease of Optimization ✓ ✓ × ✓ ✓ ✓ ✓ × ✓
Ease of Agg. Extension × × ✓ × ✓ ✓ × × ✓
Defined at Zero × × ✓ × ✓ × ✓ ✓ ✓
Differentiates Small / Large ✓ × ✓ ✓ × ✓ ✓ ✓ ✓
Table 6: Desirable properties for different metrics.
0 10 20 30 40 50 60
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0RMSE
1e6 Ad tech real estate dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization
(a) Ad-tech real estate
0 10 20 30 40 50 60
0.0
0.5
1.0
1.5
2.0
2.5
3.0RMSE
1e6 Ad tech travel dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization (b) Ad-tech travel
0 10 20 30 40 50 60
0
100000
200000
300000
400000
500000RMSE
synth-real-estate
Baseline (90%)
Baseline (95%)
Our optimization (c) synth-real-estate
0 10 20 30 40 50 60
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0RMSE
1e6 synth-travel
Baseline (90%)
Baseline (95%)
Our optimization (d) synth-travel
Figure 7: RMSE for privacy budgets{1, 2, 4, 8, 16, 32, 64} for our algorithms and baselines on two real-world and two synthetic
datasets.
Proof. It is immediate to see that ˝ ℓ,𝑗 𝑤𝑧 ℓ,𝑗+ ˝ 𝑗𝑤𝑧 ⊥,𝑗 =⌊Γ/𝐶⌋.
Let 𝑗 be such that𝑧∈Z 𝑗 . Clearly𝑤𝑧 ℓ,𝑗′ = 0 for all 𝑗′ ≠ 𝑗. We have
˝𝑑
ℓ=1𝑤𝑧 ℓ,𝑗 ≤ ˝𝑑 ℓ=1⌊𝑢𝑖⌋ ≤ j˝𝑑 ℓ=1𝑢𝑖 k =  Γ 𝐶  ,
and hence𝑤𝑧 ⊥,𝑗 =⌊Γ/𝐶⌋− ˝ ℓ𝑤𝑧 ℓ,𝑗 ≥ 0. □
We can use the same algorithm for reconstructing the estimates (Al-
gorithm 4), with scales𝛽ℓ =𝐶ℓ/⌊Γ/𝐶⌋.
In Figure 9 we show that this variant withℓ1-clipping has slightly
lower error on the real-world datasets.
The synthetic datasets have only a single non-count query, and
in this settingℓ1-clipping is equivalent to theℓ∞-clipping used in
the other experiments.
620

Summary Reports Optimization in the Privacy Sandbox Attribution Reporting API Proceedings on Privacy Enhancing Technologies 2024(4)
0 10 20 30 40 50 60
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35ARE
Ad tech real estate dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization
(a) Ad-tech real estate
0 10 20 30 40 50 60
0.0
0.1
0.2
0.3
0.4
0.5
0.6ARE
Ad tech travel dataset
Baseline (95%)
Baseline (95%, 2:2:1)
Baseline (95%, 10:10:1)
Baseline (99%)
Baseline (99%, 2:2:1)
Baseline (99%, 10:10:1)
Our optimization (b) Ad-tech travel
0 10 20 30 40 50 60
0.00
0.05
0.10
0.15
0.20
0.25
0.30ARE
synth-real-estate
Baseline (90%)
Baseline (95%)
Our optimization (c) synth-real-estate
0 10 20 30 40 50 60
0.0
0.2
0.4
0.6
0.8
1.0ARE
synth-travel
Baseline (90%)
Baseline (95%)
Our optimization (d) synth-travel
Figure 8: ARE𝜶 for𝜶 = 0.1 and privacy budgets{1, 2, 4, 8, 16, 32, 64} for our algorithms and baselines on two real-world and two
synthetic datasets.
0 10 20 30 40 50 60
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
0.200RMSRE
Ad-tech real estate dataset
Baseline (95%)
Baseline (99%)
Our optimization (L_inf)
Our optimization (L_1)
(a) Ad-tech real estate
0 10 20 30 40 50 60
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40RMSRE
Adttech travel dataset
Baseline (95%)
Baseline (99%)
Our optimization (L_inf)
Our optimization (L_1) (b) Ad-tech travel
Figure 9: RMSRE𝝉 for privacy budgets{1, 2, 4, 8, 16, 32, 64} for ourℓ∞-based andℓ1-based optimization algorithms as well as
baselines on two real-world datasets.
Algorithm 6 HistogramContribution (ℓ1 version)
Params: ⊲ Queries𝑞1,...,𝑞 𝑑 :Z→ R≥0
⊲ Partition ofZ =Z1⊔···⊔Z 𝑚
⊲ Parameters𝐶,(𝐶ℓ)ℓ∈[𝑑]
Input: Record𝑧∈Z
Output: Histogram contribution𝑤𝑧∈ Z𝐾 ≥0 for𝐾 =([𝑑]∪{⊥})×
[𝑚]
for slice 𝑗∈[ 𝑚] do
if𝑧 ∉Z𝑗 then
(𝑤𝑧 1,𝑗,...,𝑤 𝑧 𝑑,𝑗,𝑤𝑧 ⊥,𝑗)← 0
else
𝒗←
𝑞1(𝑧)
𝐶1 ,..., 𝑞𝑑(𝑧) 𝐶𝑑

∈ R𝑑
𝒖← 𝒗 max{1,∥𝒗∥1}· Γ 𝐶
(𝑤𝑧 1,𝑗,...,𝑤 𝑧 𝑑,𝑗)←( ⌊𝑢1⌋,..., ⌊𝑢𝑑⌋)
𝑤𝑧 ⊥,𝑗 =  Γ 𝐶  − ˝𝑑 ℓ=1𝑤𝑧 ℓ,𝑗
return 𝑤𝑧
621
