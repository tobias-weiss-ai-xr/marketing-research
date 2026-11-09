---
title: 'Click Without Compromise: Online Advertising Measurement via Per User Differential Privacy'
url: https://doi.org/10.1109/sp61157.2025.00187
category: privacy-data
subcategory: measurement
date: 2025-05
venue: ''
authors:
- Yingtai Xiao
- Jian Du
- Shikun Zhang
source: openalex-oa
pdf_url: https://arxiv.org/pdf/2406.02463
pages: 19
chars: 96707
fetched_at: '2026-11-08T17:31:27+00:00'
kb_version: 1
---

# Click Without Compromise: Online Advertising Measurement via Per User Differential Privacy

Click Without Compromise: Online Advertising Measurement
via Per User Differential Privacy
Yingtai Xiao∗, Jian Du ∗, Shikun Zhang ∗, Wanrong Zhang ∗, Qiang Yan ∗, Danfeng Zhang †, Daniel Kifer ‡
∗TikTok Inc. †Duke University ‡Penn State University
∗{yingtai.xiao1, jian.du, shikun.zhang, wanrong.zhang, yanqiang.mr}@tiktok.com
†danfeng.zhang@duke.edu ‡duk17@psu.edu
Abstract—Online advertising is a cornerstone of the Internet
ecosystem, with advertising measurement playing a crucial role
in optimizing efficiency. Ad measurement entails attributing
desired behaviors, such as purchases, to ad exposures across
various platforms, necessitating the collection of user activities
across these platforms. As this practice faces increasing restric-
tions due to rising privacy concerns, safeguarding user privacy
in this context is imperative. Our work is the first to formulate
the real-world challenge of advertising measurement systems
with real-time reporting of streaming data in advertising cam-
paigns. We introduce AdsBPC, a novel user-level differential
privacy protection scheme for online advertising measurement
results. This approach optimizes global noise power and re-
sults in a non-identically distributed noise distribution that
preserves differential privacy while enhancing measurement
accuracy. Through experiments on both real-world advertising
campaigns and synthetic datasets, AdsBPC achieves a 33% to
95% increase in accuracy over existing streaming DP mecha-
nisms applied to advertising measurement. This highlights our
method’s effectiveness in achieving superior accuracy alongside
a formal privacy guarantee, thereby advancing the state-of-the-
art in privacy-preserving advertising measurement.
1. Introduction
Online advertising is essential in the Internet ecosystem
as it fuels the economy of the web and enables businesses
to connect with their target audience effectively. Advertising
measurement systems [8], [25], [56], [57] are pivotal in
the online advertising landscape. They aim to assess the
effectiveness of advertising campaigns by determining the
total number of conversions—such as purchases, sign-ups,
downloads, or other desired actions—that occur as a result of
ad exposure. To reach a more diverse audience, advertisers
often set up ad campaigns across various platforms, includ-
ing Google Ads, Facebook Ads, and other digital advertising
networks. To effectively gauge the impact of these ads on
each platform, tracking mechanisms are in place to monitor
advertising campaigns across the selected channels.
The ad measurement process encompasses two major
steps: attribution and computation. The attribution step in-
volves analyzing the customer’s online journey, starting from
initial ad exposure to the ultimate conversion. Attribution
aims to identify which exposures (touchpoints) contributed
to conversions. The method that allocates credit to various
advertising channels or touchpoints throughout the customer
journey is referred to as multi-touch attribution (MTA).
MTA recognizes the multiple interactions a customer may
have with different advertising channels before making a
conversion. By distributing credit among these touchpoints
based on their influence on the conversion, MTA models
offer a more nuanced understanding of each channel’s ef-
fectiveness within the advertising mix. The computation
step is to calculate the total conversion value based on the
attribution results to gain insights into the effectiveness of
different advertising channels. Based on the such insights,
advertisers can improve their advertising campaigns by real-
locating budget, adjusting targeting parameters, refining ad
designs, or tweaking other campaign elements to improve
their return on investment and users’ advertising experience.
Ad measurement requires collecting a variety of user
data, including the ads users have viewed, clicks registered
by the ad platform, and conversion data from the advertiser’s
end. Traditionally, this involves automatically tracking user
behavior across both ad publishers’ platforms and adver-
tisers’ platforms, utilizing tools such as pixels, tags, or
software development kits (SDKs). However,the tracking
and collection of user data across sites have raised increasing
privacy concerns regarding user consent, data security, and
the potential misuse of personal information [27], [48], [49],
[57]. These privacy concerns have led to legislative actions,
such as the General Data Protection Regulation (GDPR) in
Europe [50] and industry initiatives such as Apple’s App
Tracking Transparency [6], which impose varying degrees of
restrictions on cross-site tracking. Recent studies have devel-
oped privacy-preserving mechanisms to support advertising
measurement [7], [39], [41]. However, these approaches lack
formal privacy guarantees. Our work addresses this gap
by introducing a formal differential privacy guarantee for
advertising measurement outcomes.
Differential privacy [9], [22] provides a mathematical
framework for adding carefully calibrated noise to query re-
sults or datasets to protect individual data record while still
allowing for meaningful data analysis. The calibrated noise
makes it nearly impossible to discern whether the dataset
contains a specific data record or not, thereby safeguarding
the privacy of individual data record. Differential privacy
arXiv:2406.02463v4  [cs.CR]  8 Sep 2025

has become a key component in modern privacy protection
efforts in research areas such as database systems [38],
machine learning model training data protection [3], and
census statistics [4].
Employing a differentially private mechanism to protect
individual user privacy in a practical MTA ad measurement
setting presents two challenges. First, maintaining a contin-
uous data stream poses significant hurdles for the effective
implementation of differential privacy. In advertising cam-
paigns, measurement results must be continuously disclosed
to both advertisers and ad providers in real-time, per time
slot (e.g., daily or hourly). This is crucial as it allows adver-
tisers to observe the outcomes of their campaigns and adjust
their strategies accordingly. Unlike one-time data releases in
database queries, continuous streams gradually consume the
differential privacy budget, leading to significant accuracy
deterioration and making the analysis results less valuable
from a business standpoint. Existing differentially private
streaming algorithms [12], [20], [23] primarily focus on
protecting prefix-sum queries (i.e., releasing the cumulative
sum up to the current day) and minimizing the root mean
squared error. These algorithms are limited in the types of
supported queries and objective functions.
Second, MTA involves records from various platforms,
making traditional event-level differential privacy insuffi-
cient. In differential privacy, the granularity of privacy refers
to the level at which DP guarantees are provided, indi-
cating the unit of data protected by DP. Event-level DP
protects whether a specific user action (such as clicking
an ad or making a purchase) is included in the dataset,
whereas user-level DP provides privacy protection at the
level of individual users, covering all event-level records
such as views, clicks, and conversions of a particular user.
Consequently, user-level DP protects whether a user engaged
with the ad campaign at any point, offering a stronger and
more meaningful level of privacy protection than event-
level DP. For instance, protecting whether a user has ever
engaged with an ad campaign for diabetic medication is
more meaningful than merely protecting whether a user has
clicked on an Instagram ad for diabetic medication.
To address the two challenges above, we propose the
AdsBPC algorithm, which offers greater flexibility by sup-
porting various types of online queries and objective func-
tions. This is achieved without significant modifications to
the algorithm’s structure—only the initialization of the noise
scale parameters needs to be adjusted. The algorithm can
then adaptively produce the desired results based on the
provided data. Our AdsBPC algorithm is also designed to
provide a formal user-level differential privacy. The primary
contributions of this paper are as follows:
1) We are the first to introduce and formalize the problem
regarding online MTA advertising measurement sys-
tems, including both attribution and computation steps,
which require the release of measurement results on a
streaming basis.
2) We devised a user-level streaming differentially private
algorithm, AdsBPC, tailored to address the challenges
in MTA advertising measurement. Mathematically, we
formulate the noise calibration process as a noise vari-
ance minimization problem with privacy budget con-
straints.
3) We developed a differentially private algorithm de-
signed to accurately bound per-day user contributions.
This approach reduces the sensitivity of AdsBPC,
thereby enhancing accuracy while maintaining a fixed
privacy budget.
4) Through comprehensive experiments with both syn-
thetic and real-world datasets, our algorithm achieves
notable improvements in accuracy, ranging from 33%
to 95%, compared to previous works. Our results in-
dicate that our algorithm can provide more accurate
and meaningful insights for advertisers while ensuring
users’ privacy.
This paper is structured as follows: Section 2 illustrates
how advertising measurement operates through concrete ex-
amples and discuss related concepts in differential privacy.
Section 3 explores previous work in the differential privacy
area. Section 4 formally defines our user-level differentially
private advertising measurement system and presents an ef-
ficient algorithm to address it. Section 5 presents discussions
on the proposed method. Finally, Section 6 presents the
results of comprehensive experiments conducted on both
synthetic and real-world datasets using our algorithm.
2. Ad Measurement and Differential Privacy
In this section, we elucidate advertising measurement
with multi-touch attribution as well as differential privacy
definitions in the advertising measurement context. Mathe-
matical notations used throughout this paper are summarized
in Table 1.
TABLE 1: Table of Notation
n: Number of days.
x: Data vector representation of a stream.
N : All pairs of neighboring streams. x
D: All possible deltas between neighboring. x, ˜x.
d: The difference between two neighboring dataset.
iu,j: j-th impression of user u.
cu,j: j-th conversion of user u.
w: Attribution weight.
qj: The j-th query vector.
Q: Query workload matrix.
L: Linear transformation matrix.
B: Basis matrix (strategy matrix).
z: Random variable.
ρ: Privacy budget.
ri: User contribution bound on day i.
σi: Noise scale on day i.
l: Number of days using DP-quantile.
p: The quantile percentage used in the DP-quantile.
s↑, s↓: Scaling parameters.
T ↑, T↓: Thresholds used in the sparse vector technique.

2.1. An Example of Advertising Measurement
At the core of advertising measurement lies the concept
of impression and conversion.
Impression Events. An impression event encompasses sev-
eral key elements that define the context of an ad being
served to a user. These elements include: 1) User ID, 2)
Publisher ID, 3) Advertiser ID, 4) Timestamp, and 5) Meta-
data (supplementary information related to the impression,
such as the type of user interaction (click or view) and ad
format, providing the context for further analysis). We use
the notation iu,j to express the j-th impression of user u,
and use ϕ(iu,j) to express the metadata of the impression
iu,j. In the case where an advertiser has multiple products,
we use different Advertiser IDs for different products. Table
2 shows an example of the impression table, where each row
represents an impression event of users interacting (viewing
or clicking) with ads on various publishers.
TABLE 2: Impression Table I on Day 1
User-ID Pub-ID Ad-ID Imp. Time Metadata
u1 P-1 Ad-1 iu1,1 1 ϕ(iu1,1)
u1 P-1 Ad-1 iu1,2 11 ϕ(iu1,2)
u2 P-1 Ad-1 iu2,1 15 ϕ(iu2,1)
u2 P-2 Ad-1 iu2,2 25 ϕ(iu2,2)
TABLE 3: Conversion Table C on Day 1
User-ID Ad-ID Conversion Time Metadata
u1 Ad-1 cu1,1 10 ϕ(cu1,1)
u2 Ad-1 cu2,1 20 ϕ(cu2,1)
u2 Ad-1 cu2,2 30 ϕ(cu2,2)
Conversion Events Conversion events represent pivotal mo-
ments in the advertising pipeline when users generate value
for advertisers after interacting with ads on the publishers’
platforms. These events encompass 1) User ID, 2) Advertiser
ID, 3) Timestamp, and 4) Metadata: Additional data that
characterize the conversion, including its type (e.g., purchase
or sign-up) and value (e.g., purchase amount). We use the
notation cu,j to express the j-th conversion of user u, and
use ϕ(cu,j) to express the metadata of the conversion cu,j.
Table 3 shows an example of the conversion table, where
each row represents a conversion, such as a purchase of Nike
shoes.
Advertising Measurement Process The gist of ad measure-
ment can be distilled into a two-step process. In the first step,
conversions are attributed to one or more impressions using
predefined logic or attribution models. This step is referred
to as “attribution,” determining which impressions played a
role in driving the eventual conversion event. Section 2.1.1
gives more details about attribution logic. Subsequently,
in the second step, queries are executed on the resulting
attributed dataset to derive valuable aggregate statistics.
These queries may involve counting the total number of
conversions attributed to a subset of impressions, calculating
the corresponding conversion rate, or assessing the total
return on an ad.
TABLE 4: Table after Joining Impression Table I and Con-
version Table C for Day 1 based on User-ID and Ad-ID
User-ID Pub-ID Ad-ID Imp. Conv. I.Time C.Time
u1 P-1 Ad-1 iu1,1 cu1,1 1 10
u2 P-1 Ad-1 iu2,1 cu2,1 15 20
u2 P-1 Ad-1 iu2,1 cu2,2 15 30
u2 P-2 Ad-1 iu2,2 cu2,2 25 30
TABLE 5: Attribution on Day 1 in Table 4
Conversion cu1,1 cu2,1 cu2,2
Pub-ID P-1 P-2 P-1 P-2 P-1 P-2
LTA 1 0 1 0 0 1
FTA 1 0 1 0 1 0
UNI 1 0 1 0 0.5 0.5
2.1.1. Attribution Logic. For attribution, we assume there
is a trusted third party that joins the impression table and the
conversion table. Listing 1 shows a simplified SQL query
that joins these two tables. Table 4 shows the result of
joining Tables 2 and 3. Then the third party assigns the
attribution weight of a conversion to each relevant impres-
sion. The following are several commonly used attribution
logic. Last-Touch Attribution ( LTA), also known as Last-
Click Attribution, assigns full credit for a conversion to the
last interaction or touchpoint that directly led to the conver-
sion. First-Touch Attribution ( FTA), as the name suggests,
attributes full credit for a conversion to the first interaction
or touchpoint that introduced the customer to the brand
or campaign. Uniform Attribution ( UNI) is an attribution
model in advertising measurement that evenly distributes
credit for conversions across all touchpoints in a customer’s
journey, providing equal weight to each interaction.
1 SELECT User-ID, Pub-ID, Ad-ID,
2 Impression, Conversion
3 FROM I JOIN C
4 ON I.User-ID = C.User-ID
5 AND I.Ad-ID = C.Ad-ID
6 And I.Time < C.Time
Listing 1: SQL Query to Join Impression Table and
Conversion Table on Day 1
Table 5 shows an example of the above attribution logics,
given the joined Table 4. Since onlyiu2,1 is relevant to cu2,1,
both LTA, FTA, and UNI will assign a weight of 1 to iu2,1
(similarly for cu1,1). In the case of cu2,2, where both iu2,1
and iu2,2 are relevant, LTA attributes a weight of 1 to iu2,2
as it occurs last. FTA assigns a weight of 1 to iu2,1 since
it happens first. UNI, on the other hand, evenly distributes
the weight, assigning 0.5 to both iu2,1 and iu2,2.
There are other more sophisticated attribution algo-
rithms. For example, Incremental Value Heuristics ( IVH)
[43] measures the impact of an impression by comparing re-
sults between a group exposed to the ads and a control group
that was not exposed. Shapley Value methods ( SV) [43],
[59] originate from game theory and allocate credit to each
impression based on its marginal contribution. Data-Driven
Attribution (DDA) [28], [42] uses machine learning models

TABLE 6: Streaming Measurement of Attributed Conver-
sions across Publishers via Queries
Pub-ID Day 1 Day 2 Day 3 · · ·
P-1 q1(xP1[1]) q2(xP1[1 : 2]) q3(xP1[1 : 3]) · · ·
P-2 q1(xP2[1]) q2(xP2[1 : 2]) q3(xP2[1 : 3]) · · ·
to analyze historical data and assign attribution weights by
comparing counterfactual impression patterns to reveal how
different touchpoints work together to drive conversions.
Our Ads-BPC algorithm is compatible with these advanced
attribution models, provided that the normalized total weight
assigned to each publisher for any given conversion c does
not exceed 1.
2.1.2. Measuring Attributed Conversions. In order to
effectively evaluate the advertisement’s performance across
multiple publishers, it is crucial to aggregate the total attri-
bution weights, i.e., total conversions, for each publisher. A
large cumulative sum of weights for a publisher signifies that
advertisements on that platform have a substantial likelihood
of resulting in product conversions. This metric becomes
instrumental in assessing the effectiveness of ad campaigns
and optimizing advertising strategies.
For a specific publisher and conversion event c, the
attribution process operates as follows: If c is attributed to
an impression i from this publisher, the publisher is assigned
an attribution weight of w. Then we will compute, for all
conversions, the total attribution weights received by each
publisher. A large sum of attribution weights for a publisher
signifies that advertisements on that platform are more likely
to be profitable and convert into actual conversions.
2.1.3. Streaming Measurement. In practical applications,
it is essential to adopt a continuous approach for releasing
queries on attribution weights. For instance, an advertiser
might want to obtain the cumulative sum of attribution up
to the current day and report this sum daily. Alternatively,
they might be interested in reporting the sum of attributions
for the past week, using a sliding window approach. This
approach facilitates the ongoing monitoring of trends over
time, allowing for the evaluation of changes in advertising
performance.
Before presenting an example, let’s define some key
notations. We assume the ad campaign will run for n days,
and we represent the data vector as xP ∈ Rn, where xP[i]
denotes the sum of attribution weights for publisher P on
day i (1 ≤ i ≤ n). For simplicity, we use x to represent
the data vector when the publisher P is clear from the
context. On day i, the advertiser is interested in obtaining an
answer to the query qi(x[1 : i]). The function qi depends
on x[1 : i] and has access only to the first i entries of x, as
the remaining entries are yet to be determined.
Table 6 provides an example of streaming measure-
ment for attributed conversions using online queries. In
this scenario, the advertiser Nike is interested in obtaining
answers to online queries q1, q2, . . . ,qn across two major
publishers, Publisher 1 and Publisher 2. This dataset allows
Nike to evaluate the performance of their advertisements
in real-time, enabling Nike to make timely and informed
decisions that can significantly impact their business.
Our primary concern is to ensure that the released infor-
mation will be privacy-preserving. Specifically, we require
that the released information satisfies differential privacy,
a formal privacy guarantee that will be discussed next in
Section 2.2. In Section 4, we will introduce the methodology
for achieving this privacy-preserving release of the dataset.
2.2. Differential Privacy
Differential Privacy [9], [22] establishes a set of con-
straints governing the operation of a mechanism M. It has
emerged as the de facto standard for safeguarding data pri-
vacy when publicly accessible data are released. Differential
privacy offers a robust guarantee of plausible deniability by
constraining an adversary’s ability to ascertain whether a
specific individual data record was included in the dataset
or not.
One of the key features of differential privacy is its
robust privacy guarantee, which remains effective regardless
of an adversary’s knowledge or actions when attempting to
attack the data. In this context, an adversary refers to any
person or entity trying to extract sensitive information about
an individual record from the analysis results of the data.
This privacy guarantee is maintained even if the adversary
possesses unlimited computing power and has full knowl-
edge of the algorithm and system used for data collection
and analysis.
A fundamental concept in differential privacy is the
notion of a neighboring dataset. Let N represent the set of
all possible pairs of neighboring datasets, denoted as (x, ˜x).
We define the vector d as the difference between these
neighboring datasets, expressed as d = x − ˜x. The diffset
of N is defined as the collection of all possible d values,
which we denote as D = {d : d = x − ˜x, ∀(x, ˜x) ∈ N }.
The most prevalent variant of differential privacy is given
below.
DEFINITION 2.1 (Differential Privacy [22]). Given privacy
parameters ϵ > 0 and δ ∈ (0, 1), and the set of all pairs
of neighboring datasets N , a randomized algorithm M
satisfies (ϵ, δ)-differential privacy if for all (x, ˜x) ∈ Nand
all sets S, the following equations hold:
P (M(x) ∈ S) ≤ eϵP (M(˜x) ∈ S) + δ.
When δ = 0, we say M satisfies ϵ-differential privacy.
We introduce an alternative notion of differential privacy,
zero-concentrated differential privacy for analysis.
DEFINITION 2.2 (Zero-Concentrated Differential Privacy
(zCDP) [9]). Given a privacy parameter ρ >0 and the set
of all pairs of neighboring datasets N , a mechanism M sat-
isfies ρ-zCDP if for all (x, ˜x) ∈ Nand for all α ∈ (1, ∞), it
holds that DIV α(M(x)||M(˜x)) ≤ ρα, where DIV α is the
α-Renyi divergence between distributions M(x) and M(˜x).

The following two theorems show the conversion between
zCDP and (ϵ, δ)-DP, ϵ-DP.
THEOREM 2.3 (zCDP to DP Conversion [10]). If mechanism
M satisfies ρ-zCDP , then it satisfies(ϵ, δ)-DP for any ϵ >0
and
δ = min
α>1
exp((α − 1)(αρ − ϵ))
α − 1 (1 − 1 α )α.
THEOREM 2.4 (Pure DP to zCDP Conversion [45]). If
mechanism M satisfies ϵ-DP , then it satisfies ρ-zCDP with
ρ = eϵ−1 eϵ+1 ϵ. Furthermore, the bound is tight.
In this paper, our primary emphasis is on zCDP due to
its implementation simplicity. Nevertheless, it’s important to
highlight that our proposed method seamlessly extends to
other variants of differential privacy. To analyze the privacy
of a given mechanism, an important quantity is sensitivity,
which measures the maximum change in function value on
neighboring datasets.
DEFINITION 2.5. The Lp (p = 1, 2) sensitivity of a function
f : Rn → Rn is given by ∆p(f ) = max (x,˜x)∈N ∥f (x) −
f (˜x)∥p, where ∥v∥p is the Lp norm of the vector v.
THEOREM 2.6 (Gaussian Mechanism of zCDP [9]). Let f :
Rn → Rn be a function of the dataset x, the Gaussian
mechanism M adds i.i.d. Gaussian noise to f (x) with scale
parameter σ2, M(x) = f (x) +N (0, σ2In), where In is the
n × n identity matrix. The Gaussian mechanism satisfies
∆2(f )2
2σ2 -zCDP .
A classical approach is to apply this Gaussian mecha-
nism to the vector of measurement results. However, we later
demonstrate that such an i.i.d. distribution is not optimal.
2.2.1. Neighboring Dataset. We first introduce the event-
level adjacency N Event. x and ˜x are called event-level
neighboring datasets, denoted as (x, ˜x) ∈ NEvent, if ˜x can
be obtained from x by substituting a single record in
x. We assume a fixed number of users, and therefore use
the replacement notion for defining neighboring datasets.
However, with minor adjustments to the sensitivity calcula-
tion, our method can also be adapted to the add-or-remove
notion. In this context, the diffset of N Event is defined as
DEvent = {d : ∥d∥1 ≤ 2}. This is because when a single
record is substituted, ˜x can deviate from x by 2 entries, with
each entry differing by 1, resulting in ∥˜x − x∥1 ≤ 2.
However, it is important to recognize that users may not
be content with protecting only individual actions taken on
the internet. Instead, they often seek comprehensive protec-
tion for all of their personal information. Consequently, there
arises a need for user-level neighboring datasets. To move
from event-level neighboring datasets to user-level neigh-
boring datasets, we replace the concept of “the change of
one record” with “the change of all records associated with
one user.” However, it’s important to note that since a user
can potentially contribute an infinite number of records, and
differential privacy aims to provide worst-case guarantees;
introducing excessive noise can significantly impact utility
performance. To address this challenge, a common practice
is to constrain user contributions, as discussed in prior works
such as [20], [35], [51]. This constraint limits each user to
having at most k records in the dataset. In cases where a user
exceeds this limit and contributes more than k records, only
the first k records are retained, while the surplus records are
discarded.
The user-level neighboring dataset with a global contri-
bution constraint of at most GS, denoted as N Global, defines
a pair of datasets (x, ˜x) as belonging to N Global if ˜x can
be obtained from x by substituting all records (up to a
maximum of GS records) of one user from x. Because each
user can contribute a maximum of GS records, the diffset
of N Global can be characterized as DGlobal = {d : ∥d∥1 ≤
2GS}. This is because when GS records are substituted, in
the extreme case, ˜x can deviate from x by 2 entries, with
each entry differing by GS, resulting in ∥˜x − x∥1 ≤ 2GS.
2.2.2. Differential Privacy Properties.
THEOREM 2.7 (Post-processing [9]). Let M be a mecha-
nism, f be an arbitrary function that takes the output of M
as the input. If the mechanism M satisfies ρ-zCDP , then the
post-processing f (M) satisfies ρ-zCDP .
THEOREM 2.8 (Sequential composition [9]). Let M1, · · ·,
Mk be a sequence of mechanisms. If the mechanism Mi in
the sequence satisfies ρi-zCDP , then the composition of the
sequence M = (M1, · · ·, Mk) satisfies (Pk i=1 ρi)-zCDP .
THEOREM 2.9 (Group privacy for zCDP [9]). Let M be a
mechanism that satisfies ρ-zCDP for any event-level neigh-
boring datasets (x, ˜x) ∈ NEvent. Then for any user-level
neighboring datasets with a global contribution constraint
of at most k, (x, ˜x) ∈ NGlobal, M satisfies k2ρ-zCDP .
Group privacy facilitates the transition from event-level
differential privacy to user-level differential privacy. Nev-
ertheless, in the context of online advertising measurement
systems, applying group privacy overlooks the likelihood
that a user’s contributions are more evenly distributed across
each day, rather than being concentrated in a single day. By
harnessing the patterns of user contributions across days, it
becomes feasible to enhance utility. This is the motivation
behind our proposal for a user-level differentially private
advertising measurement system with bounded per-day con-
tributions, affording greater control on a day-to-day basis.
3. Related Work
A lack of formal privacy guarantee in industry prac-
tices. To address growing consumer concerns over privacy,
many advertising networks and platforms have introduced a
range of privacy-preserving advertising measurement tools.
Notable among these initiatives are Apple’s Private Click
Measurement (PCM) framework and Google’s Attribution
Reporting API, which is part of the Privacy Sandbox. PCM
mostly relies on reducing data granularity—for example,
by allowing only limited user identifiers or implementing
delayed reporting—to decrease the amount of information

websites can gather about user activities on other sites.
Similarly, the Attribution Reporting API delivers event-
level reports that share many of PCM’s techniques, such
as delayed reporting and coarse data granularity. In addi-
tion, the Attribution Reporting API also generates summary
reports, or aggregated reports, by utilizing encryption and a
trusted execution environment (TEE). Neither PCM nor the
Attribution Reporting API can provide any formal privacy
guarantee for the advertising measurement output with a
mathematically rigorous definition. It is unclear whether
such approaches are indeed useful in safeguarding user
privacy since any aggregated report could potentially be
subject to privacy risks in a way similar to the US census
data attack in a series of works by Dwork and others [18],
[32]. Recently, Google [16] discussed releasing differentially
private conversions in a one-shot setting, whereas our fo-
cus is on releasing data in an online setting. Alistair [47]
scheduled the on-device privacy budget efficiently to achieve
individual differential privacy (IDP), with a special focus on
secure multiparty computation (MPC) and TEE.
Secure computation is not sufficient. The advertising in-
dustry has recently proposed secure multi-party computation
(MPC) based solutions. These solutions ensure the input
data is encrypted during advertising measurement compu-
tations. Examples include PSI-Sum [30] by Google and
Private Join and Compute [2] by Meta, as well as the
Interoperable Private Attribution (IPA) [11], a collaborative
effort by Mozilla and Meta. Despite the encryption of input
data, the reports—output from the MPC computation—are
plaintext results without formal privacy guarantees. Recent
studies have shown that in the case of advertising mea-
surement, membership inference attacks can exploit this
vulnerability, potentially risking user privacy and business
confidentiality [26], [31].
Ensuring privacy guarantees for online reporting poses
challenges. An advertising campaign can extend even
months. Applying differential privacy to the cumulative ad
measurement results ensure the privacy of the final data.
However, it is also crucial to report daily measurement
results online. Simply applying a differential privacy mecha-
nism by adding independent noise for each day severely de-
grades measurement accuracy and usability, as demonstrated
by the experiments in Section 6. One possible research
direction to improve the accuracy without sacrificing privacy
is to use tree-based mechanisms to address the online release
problem under event-level differential privacy. This direction
was initially introduced by Chan and Dwork [12], [23].
Subsequent studies by Denisov et al. [17] leveraged the
matrix mechanism [34], [52], [54] to enhance the accuracy
of these tree-based approaches by improving the constant
factors in their error rates. However, these methods have
limited flexibility, as they primarily focus on minimizing the
root mean squared error for prefix-sum queries. In contrast,
Ads-BPC can optimize a variety of queries with different
objective functions.
User-level privacy guarantee is preferred. Two defini-
tions of differential privacy exist in the advertising setting:
event-level and user-level. The former safeguards individual
events, while the latter conceals all events associated with a
particular user across the entire ads measurement campaign.
For instance, event-level privacy protects a single user’s
click or purchase activity (i.e., conversion), whereas user-
level privacy shields all user clicks or conversions. The cho-
sen privacy level impacts the degree of perturbation applied.
Choquette-Choo et al. introduced the matrix mechanism as
a solution for user-level differential privacy in their work
[14], [15]. Their primary application is differentially private
stochastic gradient descent. Nevertheless,these methods ne-
cessitate a minimum time gap of at least b days between
two records belonging to the same user. This requirement
presents a challenge in the context of online advertising
measurement systems, where a user can potentially have
multiple conversions within a single day. Investigating user-
level differential privacy in the context of continual ob-
servation, [20], [58] used tree-based mechanisms to tackle
the problem. Although effective for addressing the general
streaming problem, these approaches do not leverage the
specific structures inherent in advertising measurement sys-
tems. For example, in a general streaming process, a single
user may contribute most of the records, leading to a large
sensitivity (cropping the data related to this user will lead
to a high bias). However, in an advertising system involving
millions of users, most users generate only a small number
of conversions in practice . The removal of data associated
with a few users is unlikely to have a significant impact on
the overall dataset. In this paper, we focus on the challenge
of achieving the more stringent user-level differential pri-
vacy while satisfying the constraints and properties of an
online ad measurement system.
4. Differentially Private Measurement Design
We design our system to satisfies the following proper-
ties. Flexibility. The goals vary across different types of ad
campaigns, and we want to avoid redesigning the system
for each specific case. Ideally, the system should accom-
modate various objectives with only minor modifications.
Simplicity. The system should be easy to deploy and should
introduce minimal changes to the existing non-private ver-
sion. Adaptability. The system should automatically adjust
to different datasets, ensuring the algorithm performs well
across various types of data. Given these requirements, we
propose the following mechanism design:
1) Each day i, we add random Gaussian noise zi to
obtain the noisy result ˜xi = xi + zi, where zi ∼
N (0, σ2 i ) is a Gaussian random variable with mean
zero and variance σ2 i . While simple, adding indepen-
dent noise—combined with per-day contribution lim-
its—proves more effective in our experiments than
more complex methods like the matrix mechanism.
2) Depending on the specific objective function, we ini-
tialize the scale parameters ¯σ2 i , providing flexibility for
different ad campaign goals.
3) Each day, we privately estimate the user contribution
limit ri. A user can contribute up to ri conversions on
day i, with any additional conversions removed.

4) We then adjust the actual noise scale as σi = ri ∗
¯σi, based on the contribution limit ri for day i. This
data-dependent noise scaling makes the system more
adaptive.
Algorithm 1: Ads Measurement with Bounded Per
Day Contributions (Ads-BPC)
1: Input: Target workload query matrix Q; Objective
function OBJ.
2: Output: Noisy query answer.
3: ¯r1, · · ·, ¯rn = 1.
4: ¯σ1, · · ·, ¯σn = InitScales( Q, OBJ, {¯ri}n i=1).
5: bound_list = [].
6: for i in range( n) do
7: if i < lthen
8: ri= PrivateQuantile(Di, percent).
9: else
10: ri = UpdateBoundSVT( Di).
11: end if
12: Store the bound: bound_list.append( ri).
13: Clip data: x[i] = Clip( Di, ri).
14: Update scale: σi = ¯σi/¯ri ∗ ri.
15: Add noise to data: ˜x[i] = x[i] + N (0, σ2 i ).
16: Get query answer: yj = qT j ˜x.
17: end for
18: Return.
In the following sections, we describe each of the above
components in detail. Algorithm 1 provides an overview of
the AdsBPC mechanism. We begin by initializing the scale
parameters based on the given query workload and objec-
tive function, with Section 4.3 covering the initialization
process in detail. For the first l days, we estimate the user
contribution limit ri using a differentially private quantile
algorithm, as explained in Section 4.4. For the remaining
days, we apply the Sparse Vector Technique (SVT) to
determine whether an adjustment to the user contribution
limit is needed. Section 4.5 provides the implementation
details for the SVT algorithm. We will begin by addressing
the scenario involving a single publisher. In cases where
multiple publishers are involved, we show how to extend
the mechanism in Section 4.6. Before we introduce details
of our algorithm, we show how to measure the utility of
the proposed mechanism in Section 4.1, and give privacy
properties of the mechanism in Section 4.2
4.1. Mechanism Utility
Recall that there are n days in total, and we represent
the data vector as x ∈ Rn, where x[i] represents the sum
of attribution weights for a specific publisher on day i
(1 ≤ i ≤ n). In order to analyze our mechanism using
Theorem 2.6, we rewrite the noise addition step as ˜x[i] =
x[i] + N (0, σ2 i ) = σi( 1 σi x[i] + N (0, 1)). That is, we add a Gaussian random variable with zero mean and variance of
one to a scaled version of x[i]. Let B = diag( 1 σ1 , · · ·, 1 σn ), the private mechanism is defined as,
M(x) = Bx + N (0, I). (1)
We represent the j-th query vector as qj =
(qj[1], qj[2], · · ·, qj[n]), the true answer to this query
is qT j x = qj[1]x[1] + qj[2]x[2] + · · ·+ qj[n]x[n]. Be-
cause we perturb the ground truth data with indepen-
dent Gaussian noise, ˜x[i] = x[i] + N (0, σ2 i ), the noisy
answer to the query qj is qT j ˜x = Pn i=1 qj[i](x[i] +
N (0, σ2 i )) = Pn i=1 qj[i]x[i]+Pn i=1 qj[i]N (0, σ2 i ) = qT j x+
N (0, Pn i=1 qj[i]2σ2 i ). We can see that the variance of the
query qj is
Var(qj; M) :=
nX
i=1
qj[i]2σ2 i . (2)
The variance function of the mechanism M is defined
as L(Var(q1; M), . . . ,Var(qm; M)), here L is a function
of Var(qj; M). For example, L can be the sum function,
then it represents the sum of variances for all queries.
4.2. Mechanism Privacy Budget
As stated in Theorem 2.6, the privacy budget is pro-
portional to the L2 sensitivity of the mechanism. Since we
are adding independent noise to the data xi each day, a
natural way to reduce sensitivity is to limit the number of
contributions a user can make daily. To achieve this, we
introduce the concept of bounded per-day contributions.
DEFINITION 4.1 (User-Level Neighboring Dataset with
Bounded Per-day Contributions). Given the constraint that
each user can contribute at most ri conversions on day
i (1 ≤ i ≤ n), the user-level neighboring dataset with
bounded per-day contributions, denoted as N User, defines
a pair of datasets (x, x′) as belonging to N User if x′ can be
obtained from x by substituting all records (with a maximum
of ri records on day i) of one user from x. The diffset of
N User can be expressed as DUser = {d ∈ Rn : −ri ≤ di ≤
ri, 1 ≤ i ≤ n}.
The privacy budget is determined by the sensitivity of the
function f (x) = Bx, or more precisely, how much the
outputs of this mapping can deviate (in terms of L2 norm)
when transitioning from the input data vector x to a neigh-
boring data vector x′, under the definition of N User. The
following theorem shows how to calculate the sensitivity of
the function f.
THEOREM 4.2 (Sensitivity of Mechanism 1). The sensitivity
of the mechanism 1 under the definition of N User is
∆2(f ) = max (x,x′)∈N User ∥Bx − Bx′∥2 = max d∈DUser ∥Bd∥2
=
s
r2 1
σ2 1 + · · ·+ r2n σ2n . (3)

We define the privacy budget of the mechanism as
budget(M) := ∆2 2(f ) 2 = ρ. (4)
4.3. Initialize the Scales
With the expressions for utility and budget of our mech-
anism M established in previous sections, we can now
optimize the parameters σi for various queries and objective
functions. Before running the ads measurement system, ad-
vertisers need to provide: 1) The specific queries of interest,
such as the number of conversions each day or the number of
conversions from day 10 to day 20. 2) The objective function
of interest, such as minimizing the root mean squared error
or minimizing the maximum variance of the queries.
Depending on the provided queries and objective func-
tion, the advertiser may aim to minimize the objective
function within the constraints of a given privacy budget.
arg min
M
L(Var(q1; M), . . . ,Var(qm; M))
s.t. budget(M) ≤ ρ (Privacy constrained) (5)
Alternatively, the advertiser might have accuracy con-
straints for the queries and seek to minimize the total privacy
budget. We use a constant vector v to specify variance
constraints for queries.
arg min
M
budget(M) (Utility constrained)
s.t. L(Var(q1; M), . . . ,Var(qm; M)) ≤ v (6)
Then we can solve for σ1, σ2, · · ·, σn as the initial solu-
tion. The following theorem shows that using initial scales
derived above, Mechanism 1 satisfies zCDP.
THEOREM 4.3. Let Q = [ q1; q2; · · ·; qm] ∈ Rm×n be
the input Query Workload matrix. For Mechanism 1, let
ρ1 = budget(M), σ1, σ2, · · ·σn be the noise scales,
B = diag( 1 σ1 , 1 σ2 · · ·, 1 σn ), L = QB−1 and z ∼ N (0, In), then LM(x) = L(Bx + z) = Qx + Lz satisfies ρ1-zCDP .
We next show an example of calculating the initial
scales. Suppose on each day, the advertiser wants to get
the total number of conversions up to today, the query qi
on day i indicates a prefix sum function on x, qi[t] = 1 ,
when 1 ≤ t ≤ i, otherwise qi[t] = 0.
The advertiser wants to minimize the weighted sum of
variances given a fixed privacy budget. The loss function
is the weighted sum of variances, γi is the weight for qi.
L(Var(q1; M), . . . ,Var(qn; M)) =
nX
i=1
γ2 i Var(qi; M)
=
nX
i=1

γ2 i
iX
t=1
σ2 t
!
=
nX
i=1
 nX
j=i
γ2 j
!
σ2 i .
The constraint on privacy budget is budget (M) ≤ ρ, or
equivalently, ∆2 2(f ) ≤ 2ρ. Because we want to achieve
ρ-zCDP while minimizing the total variance, the problem
becomes,
min
σ2 1 ,··· ,σ2n
 nX
j=1
γ2 j
!
σ2 1 +
 nX
j=2
γ2 j
!
σ2 2 + · · ·+ γ2 nσ2 n
s.t. r2 1
σ2 1 + r2 2 σ2 2 + · · ·+ r2 n σ2n ≤ 2ρ. (7)
Problem (7) can be solved analytically using Cauchy in-
equality [53].
We give another example in the form of Problem 6.
In this example, the advertiser has requirements for the
accuracy of each query qj, the goal is to find a mechanism
that has minimal privacy cost.
min
σ2 1 ,··· ,σ2n
r2 1
σ2 1 + r2 2 σ2 2 + · · ·+ r2 n σ2n (8)
s.t. Var(qj; M) ≤ vj j = 1, · · ·, m.
As shown in Equation 2, the variance function is a linear
combination of σ2 i . Consequently, Problem 8 is a convex
optimization problem that can be efficiently solved using
any standard solver.
By selecting the initial scales, we maintain flexibility
for different types of queries and objective functions. The
key decision lies in determining these initial scales. We
initialize the user contribution bound as ¯ri = 1 to compute
the initial noise scale ¯σi. Once the actual user contribution
bound ri is determined, we update the noise scales using
σi = ¯σi/¯ri ∗ ri, as shown in Line 14 of Algorithm 1. This
adjustment ensures that the privacy budget of the mechanism
budget(M) remains unchanged. In the following sections,
we describe how to adjust the noise scales based on the
actual dataset to achieve more accurate measurements.
4.4. Estimate User Contribution Bound
Selecting an appropriate user contribution bound r in-
volves a trade-off between bias and variance. A small r
leads to the removal of numerous records, introducing sub-
stantial bias. Conversely, a large r retains most records in
the dataset but introduces significant noise into the results,
resulting in high variance. To achieve a balance between bias
and variance, we employ the differentially private quantile
algorithm [24], [44] to estimate the contribution bound. Each
day, we count the number of contributions per individual and
select an appropriate private quantile as the user contribution
bound for that day. The differentially private quantile is
based on the exponential mechanism [37].
THEOREM 4.4 (Exponential Mechanism [37], [40]).
Given utility function u mapping (dataset, output) pairs
to real valued scores with L1 sensitivity ∆1(u) =
maxX∼X ′ |u(X, o) − u(X ′, o)|, the Exponential Mecha-
nism M has output distribution PM [M (X) = o] ∝
exp

ϵu(X,o)
2∆1(u)

. Here ∝ ignores the normalization factor.
Then the mechanism M is ϵ-DP , and it satisfies 1 8 ϵ2-zCDP .

The utility function for the quantile is defined as
u(X, o) = −||{x ∈ X|x ≤ o}| −p ∗ k|. (9)
For a given output o, |{x ∈ X|x ≤ o}| is the count of
records with values less than or equal to o. Here, p denotes
the quantile percentage, and k is the total number of records.
As demonstrated in [24], [44], the sensitivity of the utility
function described above is 1. Algorithm 4 gives a detailed
description of of PrivateQuantile. We can prove that the
algorithm satisfies zCDP.
THEOREM 4.5. Algorithm PrivateQuantile 4 satisfies ρ2-
zCDP with privacy paramter ρ2 = min( 1 8 ϵ2, eϵ−1 eϵ+1 ϵ).
4.5. Track the Change of Contribution Bound
If we run the private quantile algorithm every day, the
privacy cost will be significant. We observe that the user
contribution bound is stable most of the time, which means
that the everyday estimate for the quantile is not necessary.
If we keep the bound as a constant and only update it when
there’s a significant change, it’s possible to save a large
amount of privacy budget. In case when the contribution
bound changes a lot in one day, we use Sparse Vector
Technique (SVT) [19], [36], [60] to track such a change.
We only need to report the user contribution bound when
such a change is detected.
Algorithm 2: CheckUpdate
1: Input: Query qi; Privacy budget ϵ; Number of reports
count; Maximum number of reports k; Noisy threshold
˜T ; True threshold T .
2: Output:
3: update = False.
4: if count < kthen
5: {Stop if maximum reports reached.}
6: Get noisy query: ˜qi = qi + Lap(4k/ϵ).
7: if ˜qi > ˜T then
8: update = True.
9: count = count + 1.
10: ˜T = T + Lap(2/ϵ).
11: end if
12: end if
13: Return (update, count, eT )
Define NumAbove(Di, τi) as the number of people who
has more than τi contributions on day i. We can run two
parallel SVT to check if there’s a need for updating the
contribution bound. One SVT checks if it’s necessary to
increase the bound, while the other one checks if it’s better
to decrease the bound. Algorithm 2 and Algorithm 3 outline
the details of the SVT. The three primary components are
discussed below.
Check if the Bound Increases In the first SVT, we use
the query function q↑ i = NumAbove(Di, τi), here τi is the
default contribution bound. We want to check if τi ∗ s↑
is a better contribution bound, here s↑ > 1 is a scaling
Algorithm 3: UpdateBoundSVT
1: Input: Dataset Di.
2: Parameter: Privacy budget ϵ; Maximum number of
reports k; Threshold T ↑, T↓; Scales s↑, s↓
3: Output: The user contribution bound ri.
4: Global Variable: Noisy threshold eT ↑, eT ↓; The number
of reports count ↑, count↓; Previous bounds: bound_list;
5: Split ϵ into ϵ↑ = ϵ↓ = ϵ 2.
6: τi = mean(bound_list[- l:]).
7: q↑ i = NumAbove(Di, τi).
8: (is_up, count ↑, eT ↑)
= CheckUpdate( q↑ i , ϵ↑, count ↑, k, eT ↑, T ↑).
9: q↓ i = NumAbove(Di, τi) − NumAbove(Di, τi ∗ s↓).
10: (is_down, count ↓, − eT ↓)
= CheckUpdate( q↓ i , ϵ↓, count ↓, k, − eT ↓, −T ↓).
11: if is_up == is_down then
12: ri = τi.
13: else if is_up then
14: ri = τi ∗ s↑.
15: else if is_down then
16: ri = τi ∗ s↓.
17: end if
18: bound_list.append(ri).
19: Return ri.
parameter. If q↑ i is larger than a predefined threshold T ↑,
it means that updating τ ∗ s↑ as the contribution bound
can reduce the bias. Therefore we use τi ∗ s↑ as the new
contribution bound on day i. Otherwise, we use τi as the
contribution bound.
Check if the Bound Decreases In the second SVT,
we use the query function q↓ i = NumAbove(Di, τi) −
NumAbove(Di, τi ∗ s↓), here τi is the default contribution
bound, and s↓ < 1. We want to check if τi ∗ s↓ is a better
contribution bound. If qi is greater than the threshold −T ↓
(or equivalent, −qi ≤ T ↓), it means that updating τ ∗ s↓
as the contribution bound can reduce the variance, without
introducing too much bias. Therefore we use τi ∗ s↓ as the
new contribution bound on day i. Otherwise, we use τi as
the contribution bound.
Update the Bound For the first l days, we use differentially
private quantile algorithm to calculate the private contribu-
tion bound as τi. On i > lwe update the default bound as
the average of previous l bounds τi = 1 l Pi−1 j=i−l τj. If both SVTs attempt to update the bound simultaneously, with one
trying to increase it and the other trying to decrease it, we
consider this an invalid attempt. In that case, we will use
the default bound.
The detailed description of UpdatedBoundSVT is shown
in Algorithm 3, we can prove that it satisfies zCDP.
THEOREM 4.6. Algorithm UpdateBoundSVT 3 satisfies ρ3-
zCDP with ρ3 = eϵ−1 eϵ+1 ϵ.
An Example for SVT To illustrate how SVT can detect
changes in user contribution bounds, we use an example

τ 1 2 5 8 10 13 20
Hist[D, τ] 1512 208 53 50 25 12 3
NumAbove(D, τ) 351 143 90 40 15 3 0
TABLE 7: Statistics of an example dataset D. τ is the
contribution bound. Hist [D, τ] counts the number of people
with τ contributions. NumAbove(D, τ) counts the number
of people with more than τ contributions
dataset D. For simplicity and clarity, noise is not added
to the queries or thresholds in this demonstration. Table 7
shows the statistics of the example dataset D. Suppose the
default contribution bound is τ = 10, the gap parameter is
s↑ = 1.5 and the threshold for SVT is T ↑ = 100. We want
to check if τ ∗ s↑ = 15 is a better bound. The query value
is q↑ = NumAbove(D, τ) = NumAbove(D, 10) = 15 .
Because the number of people with contributions above 10 is
small (15 is smaller than the threshold T ↑ = 100), increas-
ing the default contribution bound can’t reduce enough bias,
we don’t want to increase the bound.
Now let’s check if decreasing the default bound is better.
The default contribution bound is τ = 10, suppose the gap
parameter is s↓ = 0.5 and the threshold for SVT is T ↓ =
100. We want to check if τ ∗ s↓ = 5 is a better bound. The
query value is q↓ = NumAbove(D, τ) − NumAbove(D, τ∗
s↓) = NumAbove(D, 10) − NumAbove(D, 5) = −75.
Because the number of people with contributions between
[5, 10] is small (75 is smaller than the threshold T ↓ = 100),
decreasing the default contribution bound can reduce enough
variance, we can decrease the bound.
4.6. Extension for Multiple Publishers
The previous sections assume that only one publisher is
involved. In practice, multiple publishers often run the ad
campaign. In this section, we demonstrate that it is straight-
forward to extend the previous algorithm to accommodate
the multi-publisher case.
Suppose there are k publishers, the data vector for pub-
lisher i is xi ∈ Rn×1. Let X ∈ Rn×k be the concatenation
of these k data vectors xi. Similar to Section 4.3, the goal
is to find a private answer to QX. We factorize the work-
load matrix Q = LB, where B = diag( 1 σ1 , 1 σ2 · · ·, 1 σn )
and L = QB−1. Let Z ∼ M V Gn,k(0, In, Ik), where
M V Gn,k(0, In, Ik) is a Matrix Gaussian Distribution [13],
[55] (which generates N (0, 1) noise in each entry of Z),
then the mechanism is
LM(X) = L(BX + Z) = QX + LZ. (10)
Given the constraint that each user can contribute at most
ri records on day i (1 ≤ i ≤ n), the user-level neighbor-
ing dataset with bounded per-day contributions, denoted as
N User, defines a pair of datasets (X, ˜X) as belonging to
N User if ˜X can be obtained from X by substituting all
records (with a maximum of ri records on day i) of one
user from X. The diffset of N User can be expressed as
DUser = {D ∈ Rn×k : 0 ≤ ∥D[i, :]∥1 ≤ ri, 1 ≤ i ≤ n}.
The sensitivity calculation is similar, given that the user
contribution for each day is at most ri (across all publishers),
THEOREM 4.7 (Sensitivity of Mechanism 10). The sensitiv-
ity of the mechanism 10 under the definition of N User is
∆2(f ) = max
(X, ˜X)∈N User
∥BX − B ˜X∥F =
s
r2 1
σ2 1 + · · ·+ r2n σ2n .
(11)
Then similar to Theorem 4.3, we can show that the
mechanism 10 also satisfies zCDP,
THEOREM 4.8. Let Q ∈ Rm×n be the input Query
Workload matrix. For Mechanism defined in 10, let
ρ1 = budget(M), σ1, σ2, · · ·σn be the noise scales,
B = diag( 1 σ1 , 1 σ2 · · ·, 1 σn ), L = QB−1 and Z ∼ M V Gn,k(0, In, Ik), then LM(X) = L(BX + Z) = QX +
LZ satisfies ρ1-zCDP .
4.7. Combining Together
For Algorithm 4 and Algorithm 3, we convert them
from ϵ-DP to ρ-zCDP using Theorem 2.4. We prove in the
Theorem 4.9 that AdsBPC satisfies ρ-zCDP.
THEOREM 4.9. Algorithm AdsBPC 1 satisfies ρ-zCDP , with
parameter ρ = ρ1 + l ∗ ρ2 + ρ3.
5. Discussion
In AdsBPC, we add independent noise to the data vec-
tor with different noise scales. A natural question arises:
why not use the matrix mechanism to optimize these noise
scales? Our reasons are three-fold. Complexity: Solving the
exact matrix mechanism under user-level differential privacy
is NP-hard [15]. We compare AdsBPC with two variants
of the matrix mechanism that approximate the user-level
constraint in our experiments. AdsBPC consistently per-
forms better, while also being simpler—eliminating the need
for matrix optimization. Optimality for Small n: When
the number of days n is small and the objective function
is the root mean squared error, we calculated the optimal
matrix factorization using the code in [15]. Surprisingly,
the resulting strategy matrix is diagonal, yielding the same
objective value as AdsBPC. See the Appendix B for detailed
numerical results. Whether AdsBPC achieves optimal noise
scales in general remains a question for future research.
Flexibility: The matrix mechanism is designed to minimize
the sum of variances, limiting it to a single objective func-
tion. AdsBPC, on the other hand, offers greater flexibility
to tailor to various objectives.
Next, we discuss the differences in DP-quantile usage
between DP-SGD [3] and advertising systems. While DP-
quantile has been applied to ML training [5], the advertising
scenario presents distinct challenges. In ML training, DP-
quantile primarily determines the gradient norm, and [5]
shows that even a minimal privacy budget can yield benefits.
However, in advertising, conversion measurement accuracy

is highly sensitive to the user contribution bound. A low
privacy budget for estimating this bound introduces signifi-
cant noise. If the bound is too small, excessive data cutoff
causes high bias; if too large, increased noise leads to higher
variance. Thus, allocating a sufficient privacy budget for DP-
quantile is crucial. However, daily application depletes the
budget. To mitigate this, we exploit the stability of user
contribution quantiles, updating them only when significant
changes occur. Our novel SVT-based approach tracks users
exceeding a threshold, reducing budget consumption com-
pared to daily DP-quantile updates.
Lastly, we distinguish prior work on DP-SGD using
matrix mechanisms [14], [15], [17], emphasizing the funda-
mental differences between ML training and ads measure-
ment, particularly in how user-level privacy and neighboring
datasets are defined. In [14], a neighboring dataset is defined
such that two samples from the same user must be separated
by at least b steps. This constraint is valid in ML training,
where sample order can be controlled. However, in ads
measurement, this constraint does not hold, as users may
have consecutive conversions, and the order of their data
cannot be controlled. As noted in [15], solving a user-level
DP problem without specific ordering constraints—such as
in our case—is NP-hard. Both [14] and [15] introduce
ordering constraints to make the matrix mechanism feasible.
It is also important to note that [17] does not implement
a user-level DP mechanism. The key intuition behind our
approach comes from the unique characteristics of ads
measurement. Unlike ML training, where updates depend
on previous iterations, user contributions on different days
can be independent—i.e., for a random user, the proba-
bility of contributing each day is equal. Furthermore, the
sensitivity in our setting differs from that in ML training
due to the distinct definitions of neighboring datasets. In
our setting, a neighboring dataset is defined by replacing
a user’s conversions, with a maximum of r conversions
allowed per day. This difference in sensitivity makes our
approach specifically tailored to ads measurement.
6. Experiments
Throughout the experiments, we denote the length of
the data vector as n = len(x). We repeat our experiments
10 times and report the average results. All experiments are
conducted on a desktop with an 8-core 16-thread 3.6GHz
Intel i9-9900K CPU and 32 GB memory.
6.1. Query and Objective Function
We would like to test the performance of each method
under two scenario.
Scenario 1. The advertiser aims to track the trend of con-
versions over time. Each day, they seek a privacy-preserving
estimate of the cumulative conversions up to that day, which
corresponds to a prefix-sum query. Additionally, they prior-
itize accuracy in the final day’s estimate, so the error metric
used is the weighted root mean square error (WRMSE),
with a higher weight assigned to the last day’s query. In
this setting, the initialization of AdsBPC follows Problem
7, we set γ1 = · · ·= γn−1 = 1 and γn = 7.
Scenario 2. The advertiser is interested in the total number
of conversions over the past K days, represented by a sliding
window query. Each query is treated as equally important,
and the error metric used is the maximum variance. To
initialize AdsBPC in this context, we follow Problem 8 and
set v1 = · · ·= vn = 1. For comparison with other methods,
we scale the noise parameters to ensure that the total privacy
budget ρ is consistent across all methods. We then compare
the maximum variances across all queries for each method.
6.2. Baseline Methods
We compare our algorithm (named AdsBPC) with other
baselines. Unless otherwise specified, we allocate a total
privacy budget of ρtotal = 1. Some baseline methods require
bounding the global sensitivity. For each dataset, we assume
the global sensitivity is given as GS. If the global sensitivity
is unknown, we can set a reasonably largeGS as a threshold.
For any user with more than GS records in the dataset, only
the first GS records are retained, and any additional records
are removed. It is important to note that our algorithm
AdsBPC does not require knowledge of GS.
IPA [11]: The Interoperable Private Attribution (IPA) pro-
tocol leverages a combination of multi-party computation
and differential privacy to facilitate the processing of indi-
viduals’ data while ensuring that only aggregated measure-
ments are disclosed. In this paper, our primary focus is on
comparing how IPA achieves differential privacy, assuming
the presence of a trusted third party that provides the joined
table. IPA adds independent and identically distributed (IID)
noise to the data vector x, we use the group privacy property
2.9 to make sure it satisfies user-level neighboring datasets
with a global contribution constraint of at most GS.
BIN: BIN adds IID noise to a binary tree structure, we
use the group privacy property 2.9 to make sure it satisfies
user-level neighboring datasets with a global contribution
constraint of at most GS.
Stream [20]: Similar to BIN, Stream adds IID noise to
a binary tree structure. Rather than using a noise scale
proportional to the global sensitivity GS, Stream employs
the Sparse Vector Technique (SVT) to privately estimate the
maximum number of contributions τ that a user can make
in the dataset. Specifically, if a user exceeds τ contributions,
Stream doubles the bound, updating τ ← 2 × τ.
UMM (user-level matrix mechanism): It’s adapted from the
event-level matrix mechanism [29], we use the group privacy
property 2.9 to make sure it satisfies user-level neighboring
datasets with a global contribution constraint of at most GS.
MMBPC (matrix mechanism with bounded per-day contri-
bution): Similar to AdsBPC, we set a maximum contribution
limit ri for each user on day i. If any user contributes
more than ri conversions on a given day, only the first ri
conversions are retained in the dataset. We first compute the
event-level matrix mechanism and then scale the columns of
the matrix based on the contribution limit ri, ensuring that
the sensitivity remains unchanged.

Time 1 2 3 4 · · ·
User Alice Bob Alice Bob · · ·
Publisher 1 0 1 0 0 · · ·
Publisher 2 1 0 0 0 · · ·
· · · · · · · · · · · · · · ·· · ·
Publisher 1000 0 0 0 1 · · ·
TABLE 8: Attribution weight for each publisher
6.3. Datasets
We use three synthetic datasets and two real world
datasets to test the performance of our algorithm. For syn-
thetic datasets, we assume last-touch attribution (LTA) is
used. For real datasets, last-touch attribution (LTA), first-
touch attribution (FTA) and uniform atribution (UNI) are
used to create different data vectors x. Table 8 shows an
example of the dataset. At each time (we assume each
conversion happens in a non-overlapped timestamp), there
is one conversion, that’s attributed to one of the publishers.
Synthetic Datasets For synthetic datasets, we assume there
are 1 million users, |U | = 10 6. There are 1000 pub-
lishers. For each user, we use 3 different distributions to
generate the number of total conversions in the dataset
(the distributions are similar to the settings in [20]). For
example, if the distribution generates a number 5 for the
user Alice, it means that Alice has 5 conversions in the
dataset. We use the following three syntehtic datasets in the
experiment. Zipf Dataset In the Zipf dataset, the number of
conversions for each user is generated from the distribution:
Zipf(3)+10. Here the global sensitivity is GS = 50 (A user
has at most 50 conversions for each publisher). The total
number of conversions in the dataset is T = 11 , 361, 742.
Normal Dataset The number of conversions for each user
is generated from the distribution: Normal(50, 30). Here the
global sensitivity is GS = 150. The total number of conver-
sions in the dataset is T = 50 , 193, 976. Uniform Dataset
The number of conversions for each user is generated from
the distribution: Uniform(1, 256). Here the global sensitivity
is GS = 256, The total number of conversions in the dataset
is T = 51, 180, 247.
Criteo Dataset The Criteo Sponsored Search Conversion
Log Dataset [46] contains logs obtained from Criteo Pre-
dictive Search (CPS). Each row in the dataset represents
a user action, such as a click, performed on a product-
related advertisement, it includes information about product
characteristics (age, brand, gender, price), the timing of the
click, user characteristics, and device information.
For simplicity, we assume that the dataset pertains to a single
product. The columns of interest are as follows: ⟨sale⟩: This
column takes the value 1 if a conversion occurred and 0 if
it did not. We aim to attribute the conversion to a specific
publisher. ⟨partner_id⟩: This is a unique identifier associated
with the publisher. There are a total of 287 publishers.
⟨user_id⟩: This unique identifier is associated with each
user and is used to track the number of user contributions
in the dataset. Key dataset statistics include GS = 44 ,
T = 1, 732, 721, and |U | = 1, 608, 081.
Facebook Sales Conversion Dataset Facebook Sales Con-
version Dataset [1] is a dataset used for Facebook ad
campaign analysis and sales prediction. Each row of the
raw dataset contains information about age, gender, interest,
and number of conversions from a unique user group. We
treat each unique user group as a single user and distribute
the conversions across n days. Because Facebook is the
only publisher, both FTA, LTA and UNI will give the same
attribution weight. Key dataset statistics include GS = 60,
T = 3264, and |U | = 1143.
6.4. Experiments on Different Queries and Objec-
tive Functions
In this section, we compare AdsBPC with baseline
methods across various datasets. For the Zipf, Normal, and
Uniform datasets, we use LTA to generate the data vector
x. For the Criteo and Facebook datasets, we generate three
versions of the data vector x using different attribution
methods: LTA, FTA, and UNI. We set the number of days
to n = 31 and the privacy budget to ρ = 1.
In AdsBPC and MMBPC, we use the differentially
private quantile algorithm for the first l = 7 days, the
quantile percentage is p = 99% . In the SVT algorithm,
the scale parameters are s↑ = 1 .3 and s↓ = 0 .8, the
thresholds are T ↑ = T ↓ = 50 , the maximum number of
reports is k = 7. For the allocation of privacy budget, we set
ρ1 = 0.7ρ, ρ2 = 0.15ρ/l and ρ3 = 0.15ρ. The experiment
for time complexity is in Appendix A.1. The experiment for
parameter tuning is in Appendix A.3. The ablation study is
in Appendix A.4
Prefix Sum Query with Weighted Root Mean Squared
Error. Under Scenario 1 in Section 6.1, table 9 presents
the weighted root mean squared error (WRMSE) of vari-
ous methods across different datasets. AdsBPC consistently
outperforms other baseline methods. The final column dis-
plays the relative improvement over the second-best method;
AdsBPC achieves 33% to 63% lower error.
Sliding Window Sum Query with Max Var Error. Under
Scenario 2 in Section 6.1, table 10 presents the max variance
error of various methods across different datasets. AdsBPC
consistently outperforms other baseline methods. The final
column displays the relative improvement over the second-
best method; AdsBPC achieves 66% to 95% lower error.
We can see that AdsBPC outperforms the global
sensitivity-based methods IPA, BIN, and UMM. The reason
for this is that global sensitivity relies on the maximum
number of contributions a user makes within the dataset,
which is often significantly higher than the average con-
tribution per user. As a result, these methods introduce
an excessive amount of noise, leading to higher errors. In
contrast, AdsBPC clips user contributions on a daily basis,
effectively reducing the sensitivity and minimizing the added
noise. Stream performs poorly as it is primarily designed
for continuous releases exceeding 105 events. In contrast,
AdsBPC is better suited for advertising measurement, where
the number of online releases is comparatively small. While

Dataset IPA BIN Stream UMM MMBPC AdsBPC Improvement
Zipf 42.54 43.79 129.69 37.89 45.63 21.09 44.33%
Normal 189.73 142.53 427.82 123.41 116.12 77.28 33.45%
Uniform 294.17 153.13 760.19 316.65 161.71 56.69 62.98%
Criteo (LTA) 42.86 36.70 68.97 38.29 30.84 18.23 40.88%
Criteo (FTA) 81.14 37.47 68.02 43.08 50.01 21.78 41.87%
Criteo (UNI) 58.27 35.27 63.98 34.92 41.85 17.02 51.26%
Facebook 46.93 34.30 74.25 37.52 20.99 9.78 53.41%
TABLE 9: The query is the prefix sum, the objective (error metric) is the weighted root mean squared error. The total
privacy budget is ρ = 1. The number of days is n = 31.
Dataset IPA BIN Stream UMM MMBPC AdsBPC Improvement
Zipf 0.89 1.13 31.41 0.72 6.62 0.24 66.67%
Normal 29.72 19.19 266.40 16.65 111.83 1.35 91.89%
Uniform 32.66 171.18 1634.14 22.00 533.23 1.16 94.72%
Criteo (LTA) 0.90 2.86 15.01 1.44 23.95 0.13 85.56%
Criteo (FTA) 1.41 2.12 13.95 0.76 25.39 0.11 85.53%
Criteo (UNI) 1.00 2.32 7.02 0.69 7.52 0.12 82.61%
Facebook 0.89 4.40 10.86 1.12 0.26 0.06 76.92%
TABLE 10: The query is the sliding window sum, the objective (error metric) is the max variance (divided by 104). The
total privacy budget is ρ = 1. The number of days is n = 31.
=0.25
 =0.5
 =1
 =2
 =4
 =8
Privacy Budget ( )
101
102
Error (Weighted RMSE)
Prefix Sum
IPA
Bin
Stream
UMM
MMBPC
AdsBPC
=0.25
 =0.5
 =1
 =2
 =4
 =8
Privacy Budget ( )
10 2
10 1
100
101
102
Error (Max Variance)
Sliding Window Sum
IPA
Bin
Stream
UMM
MMBPC
AdsBPC
Figure 1: Comparison of different privacy budgets ρ on Criteo Dataset. The number of days is n = 31.
n=7 n=15 n=31 n=63 n=127
Number of Days (n)
101
102
Error (Weighted RMSE)
Prefix Sum
IPA
Bin
Stream
UMM
MMBPC
AdsBPC
n=7 n=15 n=31 n=63 n=127
Number of Days (n)
10 1
100
101
Error (Max Variance)
Sliding Window Sum
IPA
Bin
Stream
UMM
MMBPC
AdsBPC
Figure 2: Comparison of different number of days n on Criteo Dataset. The total privacy budget is ρ = 1.

MMBPC employs the same approach to calculate the per-
day user contribution bound and utilizes a complex matrix
factorization technique, its performance still falls short of
AdsBPC. This highlights that AdsBPC is effective despite
its simple design.
6.5. Experiments on Different Parameters
In this section, we demonstrate how different parameters
influence the errors. We use the Criteo dataset with LTA for
illustration.
Experiment on Different Privacy Budgets. In this section,
we study the performance of different algorithms with re-
spect to the privacy budget ρ, ρ is chosen from [0.25, 0.5,
1, 2, 4, 8]. The dataset we use is the Criteo dataset with
LTA as described in section 6.3. The number of days is
n = 31. As shown in Figure 1, the errors associated with
various algorithms decrease as ρ increases. This is because
the amount of noise added to the dataset decreases with a
larger privacy budget, leading to lower errors.
Experiments on Different Ad Campaign Durations. In
this section, we study the performance of different algo-
rithms with respect to the number of days n, n is chosen
from [7, 15, 31, 63, 127]. The dataset we use is the Criteo
dataset with LTA. The total privacy budget is set as ρ = 1.
Figure 2 illustrates the performance of various algorithms.
AdsBPC outperforms others consistently. The experiment
for n = 365 is in Appendix A.2.
7. Limitations and Future Work
Our approach currently assumes the presence of a trusted
third party, similar to existing multi-touch attribution (MTA)
systems where entities like advertising service providers
(e.g., Criteo) or mobile measurement partners fulfill this
role. However, reliance on a centralized third party intro-
duces privacy risks, as some have faced regulatory scrutiny
for mishandling user data. While our proposed algorithm
with differential privacy (DP) mitigates inference attacks and
cross-tracking risks, it does not fully eliminate concerns if
a third party acts maliciously. As future work, we plan to
explore decentralized alternatives to reduce or eliminate this
dependency. Techniques such as Trusted Execution Environ-
ments (TEE) can shift trust from third parties to secure hard-
ware providers, ensuring that only approved computations
are executed. Alternatively, Multi-Party Computation (MPC)
offers mathematically proven security without requiring a
trusted intermediary. However, practical challenges remain
in designing efficient protocols and ensuring DP guarantees
within an MPC framework. Addressing these challenges will
be a key direction for future research.
8. Conclusions
Our work is the first to formulate the real-world problem
of MTA advertising measurement systems with real-time
reporting of streaming data in advertising campaigns. We
introduced AdsBPC, a novel differentially private solution
for streaming advertising measurement results. Extensive
experiments confirm that AdsBPC significantly enhances
measurement accuracy by 33% to 95% compared to ex-
isting streaming differential privacy mechanisms applied in
advertising measurement. This improvement underscores the
effectiveness of our approach in achieving superior accuracy
while maintaining a formal privacy guarantee, thus ad-
vancing the state-of-the-art in privacy-preserving advertising
measurement.
References
[1] Facebook sales conversion dataset. https://www.kaggle.com/code/
mansimeena/facebook-ad-campaigns-analysis-sales-prediction.
[2] Private matching for compute. https://engineering.fb.com/2020/07/10/
open-source/private-matching/. Accessed: 2024-02-07.
[3] A BADI , M., C HU, A., G OODFELLOW , I., M CMAHAN , H. B.,
MIRONOV, I., T ALWAR, K., AND ZHANG , L. Deep learning with
differential privacy. In Proceedings of the 2016 ACM SIGSAC confer-
ence on computer and communications security (2016), pp. 308–318.
[4] A BOWD , J. M. The us census bureau adopts differential privacy. In
Proceedings of the 24th ACM SIGKDD international conference on
knowledge discovery & data mining (2018), pp. 2867–2867.
[5] A NDREW , G., T HAKKAR , O., M CMAHAN , B., AND RAMASWAMY ,
S. Differentially private learning with adaptive clipping. Advances
in Neural Information Processing Systems 34 (2021), 17455–17466.
[6] A PPLE . App tracking transparency. https://developer.apple.com/
documentation/apptrackingtransparency.
[7] A YALA-G ÓMEZ , F., H ORPPU , I., G ÜLBENKO ˘GLU , E., S IIVOLA ,
V., AND PEJÓ , B. Show me the money: Measuring marketing
performance in f2p games using apple’s app tracking transparency
framework.
[8] B RIGGS , R., AND HOLLIS , N. Advertising on the web: Is there
response before click-through? Journal of Advertising research 37, 2
(1997), 33–46.
[9] B UN, M., AND STEINKE , T. Concentrated differential privacy:
Simplifications, extensions, and lower bounds. In Proceedings, Part
I, of the 14th International Conference on Theory of Cryptography -
Volume 9985 (2016).
[10] C ANONNE , C. L., K AMATH , G., AND STEINKE , T. The discrete
gaussian for differential privacy. Advances in Neural Information
Processing Systems 33 (2020), 15676–15688.
[11] C ASE , B., J AIN , R., K OSHELEV , A., L EISERSON , A., M ASNY, D.,
SANDBERG , T., S AVAGE, B., T AUBENECK , E., T HOMSON , M., AND
YAMAGUCHI , T. Interoperable private attribution: A distributed attri-
bution and aggregation protocol. Cryptology ePrint Archive (2023).
[12] C HAN , T.-H. H., S HI, E., AND SONG , D. Private and continual
release of statistics. ACM Transactions on Information and System
Security (TISSEC) 14 , 3 (2011), 1–24.
[13] C HANYASWAD , T., D YTSO , A., P OOR , H. V., AND MITTAL , P.
Mvg mechanism: Differential privacy under matrix-valued query. In
Proceedings of the 2018 ACM SIGSAC Conference on Computer and
Communications Security (2018), pp. 230–246.
[14] C HOQUETTE -C HOO , C. A., G ANESH , A., M CKENNA , R., M CMA-
HAN , H. B., R USH , J., G UHA THAKURTA , A., AND XU, Z. (am-
plified) banded matrix factorization: A unified approach to private
training. Advances in Neural Information Processing Systems 36
(2024).
[15] C HOQUETTE -C HOO , C. A., M CMAHAN , H. B., R USH , K., AND
THAKURTA , A. Multi-epoch matrix factorization mechanisms for
private machine learning. arXiv preprint arXiv:2211.06530 (2022).

[16] D ELANEY , J., G HAZI , B., H ARRISON , C., I LVENTO , C., K UMAR ,
R., M ANURANGSI , P., P ÁL, M., P RABHAKAR , K., AND RAYKOVA,
M. Differentially private ad conversion measurement. Proceedings
on Privacy Enhancing Technologies (2024).
[17] D ENISOV , S., M CMAHAN , H. B., R USH , J., S MITH , A., AND
GUHA THAKURTA , A. Improved differential privacy for sgd via
optimal private linear operators on adaptive streams. Advances in
Neural Information Processing Systems 35 (2022), 5910–5924.
[18] D ICK , T., D WORK , C., K EARNS , M., L IU, T., R OTH, A., V IETRI ,
G., AND WU, Z. S. Confidence-ranked reconstruction of census
microdata from published statistics. Proceedings of the National
Academy of Sciences 120 , 8 (2023), e2218605120.
[19] D ING , Z., W ANG , Y., X IAO, Y., W ANG , G., Z HANG , D., AND
KIFER , D. Free gap estimates from the exponential mechanism,
sparse vector, noisy max and related algorithms. The VLDB Journal
32, 1 (2023), 23–48.
[20] D ONG , W., L UO, Q., AND YI, K. Continual observation under user-
level differential privacy. In 2023 IEEE Symposium on Security and
Privacy (SP) (2023), IEEE Computer Society, pp. 2190–2207.
[21] D URFEE , D. Unbounded differentially private quantile and maximum
estimation. Advances in Neural Information Processing Systems 36
(2023), 77691–77712.
[22] D WORK , C., M CSHERRY, F., N ISSIM , K., AND SMITH , A. Calibrat-
ing noise to sensitivity in private data analysis. In TCC (2006).
[23] D WORK , C., N AOR, M., P ITASSI , T., AND ROTHBLUM , G. N. Dif-
ferential privacy under continual observation. In Proceedings of
the forty-second ACM symposium on Theory of computing (2010),
pp. 715–724.
[24] G ILLENWATER , J., J OSEPH , M., AND KULESZA , A. Differentially
private quantiles. In International Conference on Machine Learning
(2021), PMLR, pp. 3713–3722.
[25] G UHA , S., C HENG , B., AND FRANCIS , P. Challenges in measuring
online advertising systems. In Proceedings of the 10th ACM SIG-
COMM conference on Internet measurement (2010), pp. 81–87.
[26] G UO, X., H AN, Y., L IU, Z., W ANG , D., J IA, Y., AND LI, J. Birds
of a feather flock together: How set bias helps to deanonymize you
via revealed intersection sizes. In 31st USENIX Security Symposium
(USENIX Security 22) (2022), pp. 1487–1504.
[27] H ADDADI , H., H UI, P., H ENDERSON , T., AND BROWN , I. Targeted
advertising on the handset: Privacy and security challenges. Pervasive
advertising (2011), 119–137.
[28] H ELP, G. A. Advertising and attribution. https://support.google.com/
analytics/answer/10596866?hl=en.
[29] H ENZINGER , M., AND UPADHYAY, J. Constant matters: Fine-grained
complexity of differentially private continual observation using com-
pletely bounded norms. Cryptology ePrint Archive (2022).
[30] I ON, M., K REUTER , B., N ERGIZ , A. E., P ATEL, S., S AXENA , S.,
SETH , K., R AYKOVA, M., S HANAHAN , D., AND YUNG , M. On de-
ploying secure computing: Private intersection-sum-with-cardinality.
In 2020 IEEE European Symposium on Security and Privacy (Eu-
roS&P) (2020), IEEE, pp. 370–389.
[31] J IANG , B., D U, J., AND YAN, Q. AnonPSI: An anonymity assess-
ment framework for PSI. In The Network and Distributed System
Security Symposium (NDSS) 2024 (Feb. 2024).
[32] K ELLER , S. A., AND ABOWD , J. M. Database reconstruction does
compromise confidentiality. Proceedings of the National Academy of
Sciences 120, 12 (2023), e2300976120.
[33] K RUŽÍK , M. Bauer’s maximum principle and hulls of sets. Calculus
of Variations and Partial Differential Equations 11 , 3 (2000), 321–
332.
[34] L I, C., M IKLAU , G., H AY, M., M CGREGOR , A., AND RASTOGI ,
V. The matrix mechanism: Optimizing linear counting queries under
differential privacy. The VLDB Journal 24 , 6 (Dec. 2015), 757–781.
[35] L IU, Y., S URESH , A. T., Z HU, W., K AIROUZ , P., AND GRUTESER ,
M. Algorithms for bounding contribution for histogram estimation
under user-level privacy. In International Conference on Machine
Learning (2023), PMLR, pp. 21969–21996.
[36] L YU, M., S U, D., AND LI, N. Understanding the sparse vector
technique for differential privacy. PVLDB 10, 6 (2017), 637–648.
[37] M CSHERRY, F., AND TALWAR, K. Mechanism design via differential
privacy. In Proceedings of the 48th Annual IEEE Symposium on
Foundations of Computer Science (Washington, DC, USA, 2007),
FOCS ’07, IEEE Computer Society, pp. 94–103.
[38] N EAR , J. P., H E, X., ET AL . Differential privacy for databases.
Foundations and Trends® in Databases 11 , 2 (2021), 109–225.
[39] P FEIFFER III, J. J., C HARLES , D., G ILTON , D., J UNG , Y. H.,
PARSANA , M., AND ANDERSON , E. Masked lark: Masked learning,
aggregation and reporting workflow. arXiv preprint arXiv:2110.14794
(2021).
[40] R OGERS , R., AND STEINKE , T. A better privacy analysis of the
exponential mechanism. DifferentialPrivacy.org, 07 2021. https://
differentialprivacy.org/exponential-mechanism-bounded-range/.
[41] R OSALES , R., C HENG , H., AND MANAVOGLU , E. Post-click con-
version modeling and analysis for non-guaranteed delivery display
advertising. In Proceedings of the fifth ACM international conference
on Web search and data mining (2012), pp. 293–302.
[42] S HAO, X., AND LI, L. Data-driven multi-touch attribution models.
In Proceedings of the 17th ACM SIGKDD international conference
on Knowledge discovery and data mining (2011), pp. 258–264.
[43] S INGAL , R., B ESBES , O., D ESIR , A., G OYAL, V., AND IYENGAR ,
G. Shapley meets uniform: An axiomatic framework for attribution
in online advertising. In The world wide web conference (2019),
pp. 1713–1723.
[44] S MITH , A. Privacy-preserving statistical estimation with optimal
convergence rates. In Proceedings of the forty-third annual ACM
symposium on Theory of computing (2011), pp. 813–822.
[45] S TEINKE , T. Tight rdp and zcdp bounds from pure dp. Differential-
Privacy.org, 05 2024. https://differentialprivacy.org/pdp-to-zcdp/.
[46] T ALLIS , M., AND YADAV, P. Reacting to variations in product de-
mand: An application for conversion rate (cr) prediction in sponsored
search. arXiv preprint arXiv:1806.08211 (2018).
[47] T HOLONIAT , P., K OSTOPOULOU , K., M CNEELY, P., S ODHI ,
P. S., V ARANASI , A., C ASE , B., C IDON , A., G EAMBASU , R.,
AND LÉCUYER , M. Alistair: Efficient on-device budgeting for
differentially-private ad-measurement systems. arXiv preprint
arXiv:2405.16719 (2024).
[48] T OUBIANA , V., N ARAYANAN , A., B ONEH , D., N ISSENBAUM , H.,
AND BAROCAS , S. Adnostic: Privacy preserving targeted advertising.
In Proceedings Network and Distributed System Symposium (2010).
[49] U LLAH , I., B ORELI , R., AND KANHERE , S. S. Privacy in targeted
advertising: A survey. arXiv preprint arXiv:2009.06861 (2020).
[50] V OIGT , P., AND VON DEM BUSSCHE , A. The eu general data
protection regulation (gdpr). A Practical Guide, 1st Ed., Cham:
Springer International Publishing 10 , 3152676 (2017), 10–5555.
[51] W ILSON , R., Z HANG , C. Y., L AM, W., D ESFONTAINES , D.,
SIMMONS -MARENGO , D., AND GIPSON , B. Differentially private
sql with bounded user contribution. In Proceedings on Privacy
Enhancing Technologies Symposium (2020).
[52] X IAO, Y., D ING , Z., W ANG , Y., Z HANG , D., AND KIFER , D. Opti-
mizing fitness-for-use of differentially private linear queries. In VLDB
(2021).
[53] X IAO, Y., H E, G., Z HANG , D., AND KIFER , D. An optimal and
scalable matrix mechanism for noisy marginals under convex loss
functions. Advances in Neural Information Processing Systems 36
(2024).

[54] X IAO, Y., W ANG , G., Z HANG , D., AND KIFER , D. Answering
private linear queries adaptively using the common mechanism. Pro-
ceedings of the VLDB Endowment 16 , 8 (2023), 1883–1896.
[55] Y ANG , J., X IANG , L., L I, W., L IU, W., AND WANG , X. Improved
matrix gaussian mechanism for differential privacy. arXiv preprint
arXiv:2104.14808 (2021).
[56] Y UAN, S., W ANG , J., AND ZHAO, X. Real-time bidding for online
advertising: measurement and analysis. In Proceedings of the seventh
international workshop on data mining for online advertising (2013),
pp. 1–8.
[57] Y UN, J. T., S EGIJN , C. M., P EARSON , S., M ALTHOUSE , E. C.,
KONSTAN , J. A., AND SHANKAR , V. Challenges and future direc-
tions of computational advertising measurement systems. Journal of
Advertising 49, 4 (2020), 446–458.
[58] Z HANG , B., D OROSHENKO , V., K AIROUZ , P., S TEINKE , T.,
THAKURTA , A., M A, Z., A PTE , H., AND SPACEK , J. Differentially
private stream processing at scale. arXiv preprint arXiv:2303.18086
(2023).
[59] Z HAO, K., M AHBOOBI , S. H., AND BAGHERI , S. R. Shapley value
methods for attribution modeling in online advertising. arXiv preprint
arXiv:1804.05327 (2018).
[60] Z HU, Y., AND WANG , Y.-X. Improving sparse vector technique with
renyi differential privacy. Advances in neural information processing
systems 33 (2020), 20249–20258.
Appendix A.
Additional Experiments
In this section, we present additional experiments to fur-
ther demonstrate the efficiency and practicality of AdsBPC.
All experiments follow the same settings as in Table 9. We
use Criteo (with LTA) and Facebook (FB) datasets.
A.1. Scalability
AdsBPC can be applied as a post-processing step after
the original data has been processed. Specifically, we re-
quire the accumulated data—namely, the total number of
conversions for a given user, advertiser, and publisher on
a particular day. This statistic can be efficiently retrieved
using an SQL query in large databases with limited over-
head. Regarding the computational cost of our algorithm,
Table 11 shows the running time (in seconds) for different
algorithm. The primary computational overhead of AdsBPC
arises from tracking and truncating user contributions across
different publishers. As future work, we will explore poten-
tial approaches to mitigate this overhead, as we believe an
efficient implementation can significantly improve runtime
performance. The running time on Facebook (FB) dataset is
small because it contains only 1 publisher.
Dataset IPA BIN Stream UMM MMBPC AdsBPC
Criteo 27 33 208 91 155 112
FB 0.001 0.08 0.03 0.21 0.43 0.004
TABLE 11: The running time (in seconds) comparison.
A.2. n=365 Experiment
We evaluate the performance of AdsBPC for long-
duration campaigns with n=365. The Criteo dataset is de-
rived from real-world data collected over a 30-day window.
If we simply divide it into 365 days, the data distribution
changes significantly—for instance, the number of conver-
sions per user per day would be diluted to approximately
1/10 of the original, leading to a lower signal-to-noise ratio
and increased sparsity. To maintain a distribution similar
to real-world data, we replicate the dataset five times to
generate a new dataset with a higher signal strength that
better reflects real-world conditions. We apply the same
approach to the FB dataset. As shown in Table 12, AdsBPC
consistently outperforms baseline methods, demonstrating
its capability to handle long-duration campaigns effectively.
Dataset IPA BIN Stream UMM MMBPC AdsBPC
Criteo 966 353 605 249 500 128
FB 1206 548 784 278 257 98
TABLE 12: Error comparison when n = 365.
A.3. Parameter Tuning
In the experiment, we set the privacy budget allocation as
ρ1 = 0.7ρ, ρ2 = 0.15ρ/l, and ρ3 = 0.15ρ. We examine how
different privacy budget allocations affect the performance
of AdsBPC. Specifically, we allocate ρ1 = (1 − λ)ρ for
measurement, ρ2 = λ 2l ρ for DP-quantile, and ρ3 = λ 2 ρ for SVT. Table 13 presents the performance of AdsBPC for
different values of λ. From the results, we observe that when
λ = 0.5, an insufficient budget is allocated for measurement,
leading to higher variance. Conversely, when λ = 0.1, the
bound selection becomes less accurate, resulting in increased
bias.
λ 0.5 0.4 0.3 0.2 0.1
Criteo 24.73 18.55 18.23 22.97 24.18
FB 29.67 11.17 9.78 10.25 18.40
TABLE 13: Different budget allocations.
Next, we examine the effect of the scaling factors s↑, s↓
used in SVT. We vary s↑ and set s↓ = 1 /s↑ accordingly.
Table 14 shows that the performance remains relatively
robust against different selections of s↑.
s↑ 1.1 1.2 1.3 1.4 1.5
Criteo 21.89 22.39 18.23 20.45 18.89
FB 12.23 11.73 9.78 10.70 12.05
TABLE 14: Different scaling factors.
Lastly, we examine the impact of the thresholds T ↑, T↓
used in SVT. We vary T ↑ and set T ↓ = T ↑. Table 15 shows
that a smaller threshold T ↑ causes SVT to update more
frequently, leading to faster budget consumption and leaving
the contribution bound unchanged in later days. This results
in higher errors due to inaccurate estimates of contribution
bounds in later days.

TABLE 18: Check the Absolute Value of the Off-Diagonal
Elements.
n maxi̸=j |B⋆[i, j]| mini̸=j |B⋆[i, j]| meani̸=j |B⋆[i, j]|
2 6.67 ∗ 10−5 6.67 ∗ 10−5 6.67 ∗ 10−5
4 1.59 ∗ 10−4 1.14 ∗ 10−5 5.38 ∗ 10−5
6 7.26 ∗ 10−5 8.03 ∗ 10−7 1.82 ∗ 10−5
8 4.81 ∗ 10−5 4.70 ∗ 10−8 5.58 ∗ 10−6
10 4.39 ∗ 10−5 1.69 ∗ 10−8 3.03 ∗ 10−6
12 4.36 ∗ 10−5 9.20 ∗ 10−9 2.14 ∗ 10−6
14 4.48 ∗ 10−5 2.79 ∗ 10−10 1.71 ∗ 10−6
TABLE 19: Comparison between the optimal objective func-
tion value of different methods.
n Solver AdsBPC
2 108.46 108.46
4 950.55 950.56
6 2400.11 2400.12
8 5193.02 5193.03
n Solver AdsBPC
10 11365.32 11365.32
12 19441.07 19441.07
14 32607.31 32607.32
T ↑ 10 25 50 75 100
Criteo 23.37 21.50 18.23 20.89 21.45
FB 17.79 16.90 9.78 8.71 10.13
TABLE 15: Different SVT thresholds.
A.4. Ablation Study
We aim to investigate the following questions:
1. Constant Bound : What if we use a fixed bound
instead of DP-quantile and SVT? How would this impact
accuracy? We use the same setting as in Table 9 ( ρ = 1) but
exclude dp-quantile and SVT, relying solely on a predefined
user contribution bound for all 31 days. The results in Table
16 indicate that WRMSE is highly sensitive to this bound:
a small bound ( r = 1) introduces high bias, while a larger
bound ( r = 6 ) increases variance. Although choosing an
intermediate bound ( r = 3) can mitigate error, the optimal
bound for a given dataset is itself private information and
unknown in advance. This highlights the necessity of a
private estimation method for the user contribution bound.
Bound r=1 r=2 r=3 r=4 r= 5 r = 6
Criteo 1512.25 24.52 18.18 22.29 23.15 40.63
FB 230.48 53.25 9.99 16.35 26.16 30.68
TABLE 16: Ablation Study 1: Constant Contribution Bound
2. Daily DP-Quantile Updates : What if we apply DP-
quantile every day without SVT? How would this affect
accuracy? We use the same setting as in Table 9 but with a
different privacy budget. Instead of SVT, we use dp-quantile
to estimate user contributions over all 31 days. Table 17
shows the errors. The performance deteriorates due to a
lower privacy budget allocated per day, leading to a less
accurate estimation of the user contribution bound. How-
ever, as the privacy budget increases, performance improves,
highlighting the importance of accurately estimating the user
contribution bound.
Budget ρ = 1 ρ = 2 ρ = 4 ρ = 6 ρ = 8 ρ = 10
Criteo 79.08 72.02 55.83 42.41 33.45 32.68
FB 137.55 100.82 65.64 33.24 29.34 29.11
TABLE 17: Ablation Study 2: DP-Quantile Only, No SVT
Appendix B.
Possibly Optimality of AdsBPC
To get the optimal strategy matrix under user level
differential privacy with bounded per-day contribution, we
use the numerical solver in [15] under its default parameters.
For each n, we randomly generate the per-day constraint
ri ∈ [1, 10] and set ρ = 1 . Surprisingly, we find that
the optimal strategy matrix B⋆ tends to be a diagonal
matrix. Table 18 shows the absolute value of the off-diagonal
elements in P⋆, the maximum absolute value of B⋆ is close
to 0. We also compare the optimal objective function values
of the solver and AdsBPC. Table 19 shows that our method
achieves optimality up to a difference of 10−2, which may
come from numerical error.
Appendix C.
Proofs
C.1. Proof for Theorem 4.2
Proof. From the definition of sensitivity 2.5, the function
f (x) = Bx has the sensitivity maxd∈DUser ∥Bd∥2. Notice
that ∥Bd∥2 is a convex and continuous function with respect
to d, and the constraint set DUser is convex and compact with
respect to d. So according to Bauer’s maximum principle
[33], the function ∥Bd∥2 attains its maximum at some
extreme point of the set DUser. Recall that DUser = {d ∈
Rn : −ri ≤ di ≤ ri, 1 ≤ i ≤ n}, so the set of extreme
points of DUser is
DUser ex = {d ∈ Rn : di ∈ {−ri, ri}, 1 ≤ i ≤ n}. (12)
Then the square of sensitivity of B is,
max
d∈DUser
dT BT Bd = max
d∈DUserex
dT BT Bd = r2 1
σ2 1 + · · ·+ r2 n σ2n .
C.2. Proof for Theorem 4.3
Proof. Let f (x) = Bx, from theorem 4.2 the sensitivity of
f is ∆2(f ) =
q
r2 1
σ2 1 + · · ·+ r2n σ2n . The constraint in problem
7 makes sure that ∆2 2(f ) ≤ 2ρ. From theorem 2.6 we get
f (x)+ N (0, In) = Bx+z satisfies ρ-zCDP. Using the post-
processing property 2.7, we know that M(x) = L(Bx+z) =
Wx + Lz satisfies ρ-zCDP.
C.3. Proof for Theorem 4.5
Proof. From Theorem 4.4, the Exponential Mechanism sat-
isfies ϵ-DP and 1 8 ϵ2-zCDP. From Theorem 2.4, any ϵ-DP
mechanism is also eϵ−1 eϵ+1 ϵ-DP. As a special case of Expo- nential Mechanism, the PrivateQuantile algorithm satisfies
ρ2-zCDP, with ρ2 = min( 1 8 ϵ2, eϵ−1 eϵ+1 ϵ).

C.4. Proof for Theorem 4.6
LEMMA C.1. The L1 sensitivity of the following is 1.
q(D, τ, s) = NumAbove(D, τ) − NumAbove(D, τ∗ s).
Here s <1.
Proof. Let D and D′ be two adjacent datasets. D′ can be
obtained from D by replacing one user u in D with another
user u′. q(D, τ, s) counts the number of people in D with
contributions between (τ ∗s, τ]. If both u and u′ have number
of contributions smaller or equal to τ ∗ s, then q(D, τ, s) =
q(D′, τ, s). If both u and u′ have number of contributions
between (τ + s, τ], then q(D, τ, s) = q(D′, τ, s). If both
u and u′ have number of contributions larger than τ, then
q(D, τ, s) = q(D′, τ, s). If one of them (suppose it’s u) has
number of contributions smaller or equal to τ, and another
one (suppose it’s u′) has number of contributions larger than
τ, then
q(D′, τ, s)
=NumAbove(D′, τ) − NumAbove(D′, τ∗ s)
=NumAbove(D, τ) + 1 − (NumAbove(D, τ∗ s) + 1)
=NumAbove(D, τ) − NumAbove(D, τ∗ s) = q(D, τ, s).
If one of them has number of contributions between
(τ, τ+s], and another one doesn’t have number of contribu-
tions between (τ, τ+s], then ∥q(D, τ, s)−q(D′, τ, s)∥1 = 1.
We see that the L1 difference is at most 1. This is true for
the same reason when s <0. Therefore, the L1 sensitivity
is 1.
With Lemma C.1, we are ready to prove Theorem 4.6.
Proof. The sensitivity of q↑ = NumAbove(D, τ) is 1 be-
cause if we replace a user in D, the total number of users
who have contributions greater than τ can change by at most
1. From Lemma C.1 we know that the sensitivity of q↓ is 1.
Therefore, each SVT satisfies ϵ/2-DP, so UpdateBoundSVT
satisfies ϵ-DP. From Theorem 2.4, UpdateBoundSVT satis-
fies ρ3 = eϵ−1 eϵ+1 ϵ-zCDP.
C.5. Proof for Theorem 4.9
Proof. In Algorithm 1, we allocate a privacy budget of ρ2
for each call to PrivateQuantile. Since there are l calls in to-
tal, the overall budget for PrivateQuantile is l ∗ρ2. Addition-
ally, we use a privacy budget of ρ3 for UpdateBoundSVT.
From Theorem 4.9, recall that the sensitivity of the noise
addition mechanism is determined by ri σi . Since we update the user contribution bound ri by scaling σi proportionally,
the sensitivity remains unchanged. Therefore, the noise ad-
dition mechanism uses a privacy budget of ρ1. In total, the
combined privacy budget used is ρ = ρ1 + l · ρ2 + ρ3.
C.6. Proof for Theorem 4.7
Proof. According to the matrix value mechanism
[13], the function f (X) = BX has the sensitivity
maxD∈DUser ∥BD∥F . Recall that DUser = {D ∈ Rn×k : 0 ≤
∥D[i, :]∥1 ≤ ri, 1 ≤ i ≤ n}, then the square of sensitivity
of B is,
max
D∈DUser
X
1≤i≤n
∥D[i, :]∥2 2
σ2 i ≤
X
1≤i≤n
∥D[i, :]∥2 1
σ2 i ≤
X
1≤i≤n
r2 i
σ2 i .
C.7. Proof for Theorem 4.8
Proof. Let f (X) = BX, from theorem 4.7 the sensitivity of
f is ∆2(f ) =
q
r2 1
σ2 1 + · · ·+ r2n σ2n . The constraint in problem
7 makes sure that ∆2 2(f ) ≤ 2ρ. We can flatten f (X) and
Z ∼ M V Gn,k(0, In, Ik) as vectors of length n × k. From
Theorem 2.6, we get f (X) +Z = BX+Z satisfies ρ-zCDP.
Using the post-processing property, we know that M(X) =
L(BX + Z) = WX + LZ satisfies ρ-zCDP.
Appendix D.
PrivateQuantile Algorithm
Algorithm 4 shows the pseudo-code for the DP-Quantile
algorithm [24], [44]. Note that PrivateQuantile requires an
additional parameter, Λ, which serves as an upper bound. In
our experiments, we set Λ = 10 for the Crieto, Facebook,
and Zipf datasets, and Λ = 20 for the Normal and Uniform
datasets. [21] proposed an algorithm that does not require
such a bound. Notably, their algorithm can be integrated into
our system with minimal modifications.
Algorithm 4: PrivateQuantile
1: Input: Dataset D; Quantile percentage p; privacy
parameter ϵ, bounding parameter Λ.
2: Output: The selected user contribution bound based
on p quantile.
3: X = [].
4: for Each user ui in D do
5: ci ← the number of records from ui.
6: X.append(ci).
7: end for
8: Sort X in ascending order. X = [c1, c2, · · ·, ck].
9: Replace ci > Λ with Λ. Define c0 = 0 and ck+1.
10: for i = 1 to k do
11: Set yi = (ci+1 − ci) exp(−ϵ|i − p ∗ k|/2).
12: end for
13: Sample an integer i ∈ {0, · · ·, k} with probability
yi/(Pk i=0 yi).
14: c ← uniformly sampled from [ci, ci+1].
15: Return c.

Appendix E.
Meta-Review
The following meta-review was prepared by the program
committee for the 2025 IEEE Symposium on Security and
Privacy (S&P) as part of the review process as detailed in
the call for papers.
E.1. Summary
This paper presents AdsBPC, a system to measure ad
campaign exposure and attribution with differential privacy
guarantees. This system allows publishers to measure multi-
touch attribution (MTA) while providing user-level differen-
tial privacy (DP). The authors claim a significant improve-
ment in accuracy when compared to prior work.
E.2. Scientific Contributions
• Provides a Valuable Step Forward in an Established
Field
• Creates a New Tool to Enable Future Science
E.3. Reasons for Acceptance
1) The paper provides a valuable step forward in an es-
tablished field. AdsBPC novel approach has been eval-
uated on five datasets, both synthetic and real-world,
and achieves improvements over baselines such as IPA,
BIN, Stream and UMM. Furthermore, the feasibility
and performance of the system was tested across ad
campaigns with different duration of up to 365 days.
2) The reviewers were positive about the presentation of
the paper, agreeing that it does a really good job of
presenting the methodology behind AdsBPC and the
thorough comparison with existing technologies. The
reviewers also agreed that, while some of the under-
lying techniques and notions of the paper might not
be novel, the way that these are applied to the specific
use case of advertisements and measuring conversions
provides enough of a step forward on the field to justify
accepting this paper.
