---
title: 'PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection'
url: https://arxiv.org/abs/2506.20981
category: privacy-data
subcategory: measurement
date: 2025-06
venue: arXiv (Cornell University)
authors:
- Jian Du
- Qian, Haohao
- Shikun Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.20981
pages: 17
chars: 82261
fetched_at: '2026-11-08T12:57:50+00:00'
kb_version: 1
---

# PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection

arXiv:2506.20981v1  [cs.CR]  26 Jun 2025
PrivacyGo: Privacy-Preserving Ad Measurement with
Multidimensional Intersection
Jian Du, Haohao Qian, Shikun Zhang, Wen-jie Lu, Donghang Lu,
Yongchuan Niu, Bo Jiang, Yongjun Zhao, and Qiang Yan
TikTok Inc.
ABSTRACT
In digital advertising, accurate measurement is essential for optimiz-
ing ad performance, requiring collaboration between advertisers
and publishers to compute aggregate statistics—such as total conver-
sions—while preserving user privacy. Traditional secure two-party
computation methods allow joint computation on single-identifier
data without revealing raw inputs, but they fall short when mul-
tidimensional matching is needed and leak the intersection size,
exposing sensitive information to privacy attacks.
This paper tackles the challenging and practical problem of multi-
identifier private user profile matching for privacy-preserving ad
measurement, a cornerstone of modern advertising analytics. We
introduce a comprehensive cryptographic framework leveraging re-
versed Oblivious Pseudorandom Functions (OPRF) and novel blind
key rotation techniques to support secure matching across multiple
identifiers. Our design prevents cross-identifier linkages and in-
cludes a differentially private mechanism to obfuscate intersection
sizes, mitigating risks such as membership inference attacks.
We present a concrete construction of our protocol that achieves
both strong privacy guarantees and high efficiency. It scales to
large datasets, offering a practical and scalable solution for privacy-
centric applications like secure ad conversion tracking. By combin-
ing rigorous cryptographic principles with differential privacy, our
work addresses a critical need in the advertising industry, setting a
new standard for privacy-preserving ad measurement frameworks.
1 INTRODUCTION
Private Ad in Practice: Digital advertising relies on cross-site
and cross-app user tracking to link ad impressions stored by ad
providers with user conversions recorded by advertisers, using
third-party cookies or mobile device identifiers. This connection
provides insights into ad performance and audience reach, enabling
measurement of key metrics such as click-through rates, conver-
sions, and return on ad spend (ROAS). By analyzing user behavior
across platforms, marketers can further refine campaign strategies.
However, growing privacy concerns over tracking consumer
behavior across ad providers and advertisers—driven by regulations
such as GDPR and CCPA, along with industry changes such as
third-party cookie deprecation and mobile identifier restrictions—
are transforming the digital advertising landscape. In response,
privacy-preserving technologies are becoming essential to balance
effective ad measurement with robust data protection.
Ideally, if a unique identifier is used consistently across both the
ad provider and the advertiser sides, cryptographic techniques that
enable privacy-preserving set intersection can compute shared sta-
tistics without revealing sensitive data from either party, effectively
preventing cross-platform tracking. However, in practice, matching
*Corresponding author: Jian Du. Email: jian.du@tiktok.com.
user identities across platforms is complex because users often have
different identifiers, such as varying registration emails or phone
numbers. To improve accuracy, multiple identifiers must be aligned
based on specific rules. Techniques like the waterfall matching
approach (also known as advanced matching [1]), widely used in
the advertising industry, prioritize identifier hierarchy to reduce
false positives and enhance reliability. This method systematically
resolves identity discrepancies by sequentially matching identifiers
from the most reliable to the least reliable, ensuring more precise
attribution. The underlying mathematics extends beyond the sim-
ple set intersection and is known as multidimensional intersection,
where multiple attributes are matched simultaneously to achieve
context-aware identity resolution with higher accuracy.
1.1 Problem Characteristics and Requirements
In Figure 1, we provide a formal description of the functionality that
we aim to compute privately. This figure illustrates the process by
which one party, P𝐵, learns the aggregated sum𝑐 according to the
logic of the waterfall matching1 for a multidimensional intersection.
At first glance, the target problem illustrated in Figure 1 may appear
similar to the private-match-for-compute protocols such as [2–7].
However, we highlight two key differences that distinguish our
target problem from theirs:
1) Multidimensional Intersection. For the case of a single ID,
two databases are joined using exact matching on the common
identifier, which is handled by most existing private set intersec-
tion protocols. However, when it comes to multiple IDs, it often
results in many-to-many connections. For instance, some records in
the databases may be matched by one identifier, e.g., email address,
while other records are matched by a different identifier, e.g., phone
number. The waterfall matching converts the many-to-many con-
nections to one-to-one connections in a hierarchically iterative way.
Specifically, the waterfall matching approach ranks identifiers in a
predefined order. A record is considered matched if one of its iden-
tifiers matches. To avoid many-to-many connections, the matched
rows are removed before the matching procedure advances to the
next identifier. Waterfall matching for multidimensional intersec-
tions is effective because:
(1) Each record is matched only once, preventing many-to-
many connections.
(2) Higher-priority identifiers take precedence, reducing false
positives and enhancing matching reliability.
2) Hiding Cross-ID Leakages. Leveraging multiple identifiers
improves match rates, which is critical for the advertising business.
However, a simple approach that runs a single-ID matching protocol
1Indeed, the waterfall matching can work for more than two identifiers. To simplify
the presentation, we only consider two identifiers here.

FunctionalityFwfm
On receiving identifiers ID1 𝐴, ID2 𝐴 from P𝐴, ID1 𝐵, ID2 𝐵 and payloads 𝑇
from P𝐵, this functionality do:
(1) Match on the 1st identifier
𝐽 1 𝐴 ={𝑖 : ID1 𝐴[𝑖]∈ ID1 𝐵}, 𝐽 1 𝐵 ={𝑗 : ID1 𝐵[𝑗]∈ ID1 𝐴}
(2) Unmatched records on the 2nd identifier
rID2 𝐴 ={ID2 𝐴[𝑖]}𝑖∉𝐽 1 𝐴 , rID2 𝐵 ={ID2 𝐵[𝑗]}𝑗 ∉𝐽 1 𝐵
(3) Match on the 2nd identifier
𝐽 2 𝐴 =  𝑖 : ID2 𝐴[𝑖]∈ rID2 𝐵 	 \𝐽 1 𝐴
𝐽 2 𝐵 =  𝑗 : ID2 𝐵[𝑗]∈ rID2 𝐴 	 \𝐽 2 𝐵
(4) Give P𝐴 the sizes𝑠1 =|𝐽 1 𝐴| and𝑠2 =|𝐽 2 𝐵|.
(5) Give P𝐵 the sum𝑐 = ˝ 𝑖∈𝐽 1 𝐵∪𝐽 2 𝐵 𝑇[𝑖] and𝑠1,𝑠 2.
Figure 1: The waterfall matching and sum functionality. Note
that the matches on the 2nd ID column can also be given as
{𝑖 : rID2 𝐴[𝑖]∈ rID2 𝐵} and{𝑗 : rID2 𝐵[𝑗]∈ rID2 𝐴}, which needs an
extra mapping to a global index in the payload column.
ID1 𝐴 ID2 𝐴
d !
a #
f &
g @
ID1 𝐵 ID2 𝐵
b ˆ
a #
c &
g NA
NA @
type-E
type-X
Figure 2: Example of the type-E cross-ID leakage and the
type-X cross-ID leakage. ‘NA’ indicates a missing value.
separately for each identifier can unintentionally reveal additional
information.
Figure 1 defines two types of cross-ID leakages: type-E and
type-X (see Figure 2 for an example). Type-E leakages occur when
parties learn that a record is matched by multiple IDs, while type-
X leakages occur when one party (say, P𝐴) learns that a record
from P𝐵 matches multiple records on P𝐴’s side. For example, in
Figure 2, the fourth row of the left table matches both the fourth
and fifth rows of the right table. Type-X leakages are common
in ad applications, where users may have multiple accounts on a
publisher’s platform registered with different identifiers, such as
phone numbers and email addresses.
Both type-E and type-X leakages increase the risk of member-
ship leakage, as demonstrated by membership inference attacks
described in the literature [8, 9]. From a business perspective, these
leakages allow either party to track user behaviour on the other side.
For instance, the ad provider could learn if a user has converted
on the advertiser’s side, which could be particularly sensitive for
industries like healthcare and finance. Addressing these leakages is
crucial to ensure privacy while enabling effective matching.
2 TECHNICAL OVERVIEW
2.1 Distributed Evaluation of Reversed and
Blindly Updatable Pseudorandom Function
We first recap the recipe for building a private set intersection
protocol. Suppose P𝐴 inputs set𝑋 and P𝐵 inputs set𝑌 . They invoke
an Oblivious Pseudorandom Function (OPRF) protocol, which gives
the PRF evaluations{𝐹𝑘(𝑥)| 𝑥∈𝑋} to P𝐴 and gives the key𝑘 to
P𝐵. This directly allows obtaining the intersection𝑋∩𝑌 by having
P𝐵 send{𝐹𝑘(𝑦)| 𝑦∈𝑌} to P𝐴. Since the interest is in evaluating a
function𝑓 over the intersection, rather than the intersection itself,
it is natural to perform the OPRF in a reversed manner. For example,
P𝐵 obtains{𝐹𝑘(𝑥)| 𝑥∈𝑋}, the PRF evaluations on P𝐴’s input. By
performing the reversed OPRF twice and exchanging the PRFs, P𝐴
and P𝐵 can obtain the set cardinality𝑓(𝑋∩𝑌) =|𝑋∩𝑌| without
revealing the intersection. This reversed OPRF implicitly demands
a distributed OPRF evaluation, i.e., the corresponding PRF key is
secretly shared between the two parties.
We demonstrate that the reversed OPRF already enables efficient
row deletion required by the waterfall matching logic. Specifically,
P𝐴 can locally remove matched rows from𝐹𝑘(𝑦)| 𝑦∈𝑌 before ex-
changing PRF evaluations with P𝐵. Since the key remains unknown
to both parties, P𝐵 is oblivious to which rows have been deleted.
This private row deletion inherently mitigates type-E leakages.
To address type-X leakages, we introduce a novel mechanism
for blind PRF key updates. Given an evaluation 𝐹𝑘(𝑥), P𝐵 inter-
acts with P𝐴 to obtain𝐹𝑘′(𝑥)—an evaluation under a new shared
key—without revealing the linkage between𝐹𝑘(𝑥) and𝑥. Impor-
tantly, this ensures that even if P𝐴 knows the input𝑥, it remains
unaware of the key transition, thus preserving input privacy across
key updates. Our method represents a significant advancement
in leakage resilience by seamlessly integrating key blinding into
private matching protocols.
Finally, we formalize the desired OPRF functionality in Figure 3,
defining it as a Distributed, Blindly Updatable, and Reversed Pseudo-
random Function (𝑑𝑢𝑟𝑃𝑅𝐹 ). This newFdurPRF construction enables
a privacy-preserving multidimensional intersection for implement-
ing a waterfall matching protocol with robust leakage resistance.
Our blind key update mechanism addresses type-X leakages by
fully decoupling key transitions from input knowledge. This en-
sures that even if an input is partially known to P𝐴, the linkage
between evaluations under different keys remains hidden, preserv-
ing privacy across updates. Additionally, the reversed OPRF design
allows P𝐴 to efficiently delete matched rows from 𝐹𝑘(𝑦)| 𝑦∈𝑌
without exposing deletion patterns to P𝐵, inherently mitigating
type-E leakages. By integrating these capabilities, our protocol de-
livers privacy guarantees against adversaries seeking to exploit
linkage or key-correlated information, providing a comprehensive
defense against both type-E and type-X leakages.
2.2 Enhancing Privacy via Differential Privacy
Recent research highlights that size-revealing (single-ID) private
set intersection (PSI) protocols are susceptible to membership in-
ference attacks, posing significant privacy risks in advertising con-
texts [8, 9]. In these attacks, an ad publisher can infer which users
on its platform viewed an ad but did not complete a purchase

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
FunctionalityFdurPRF
There are two parties P𝐴 and P𝐵.
Initialization: Upon receiving Init.(sid,𝑘𝐴) from P𝐴, and Init.(sid,𝑘𝐵)
from P𝐵, initialize an empty table𝑇sid, and record(sid,𝑘𝐴⊕𝑘𝐵). Ignore
all subsequent init queries for the session ID sid.
Evaluation: On Send.(sid,𝑥 1,··· ,𝑥𝑛) from P𝐴 (sender), and
Recv.(sid,𝑛) from P𝐵 (receiver) do:
• Set𝑇sid[𝑥𝑖]
$
← −{0, 1}𝜆 if any empty entry.
• Give𝑇sid[𝑥1],··· ,𝑇sid[𝑥𝑛] to P𝐵.
The roles can be flipped, i.e., P𝐵 acts as the sender and P𝐴 acts as the
receiver.
Update: Upon receiving Update.(sid, sid′,𝑧 1,··· ,𝑧𝑚) from P𝐵, and
Update.(sid, sid′,𝑚) from P𝐴 do:
• Set𝑧′ 𝑗 $ ← −{0, 1}𝜆 for𝑗 = 1, 2,··· ,𝑚 .
• For each𝑧𝑗 , find an entry𝑥𝑗 in𝑇sid such that𝑇sid[𝑥𝑗] =𝑧𝑗 . If
not any then set𝑥𝑗 =⊥.
• If𝑥𝑗 ≠⊥ and the entry𝑇sid′[𝑥𝑗] is not empty, then overwrite
𝑧′ 𝑗←𝑇sid′[𝑥𝑗]. Otherwise if𝑥𝑗 ≠⊥ and the entry𝑇sid′[𝑥𝑗] is
empty, then set the entry𝑇sid′[𝑥𝑗]← 𝑧′ 𝑗 .
• Finally return𝑧′ 1,··· ,𝑧′𝑚 to P𝐵.
The roles can be flipped too, i.e., P𝐵 acts as the assistant and P𝐴 acts as
the updater.
Figure 3: The functionality of 𝑑𝑢𝑟𝑃𝑅𝐹 .
with the advertiser. This compromises sensitive business data, as
the advertiser may not wish to disclose granular user conversion
behavior. Such leakages not only undermine the advertiser’s com-
petitive edge but also raise potential compliance concerns under
privacy regulations such as the GDPR, which mandates strict limits
on personal data processing and requires minimizing data expo-
sure between parties. Addressing these vulnerabilities is critical to
ensuring privacy-preserving advertising practices that align with
regulatory obligations and protect proprietary business insights.
Multidimensional intersections are more vulnerable to member-
ship inference attacks. Particularly, we conduct the membership
inference attacks [8, 9] against the size-revealing and multi-ID pro-
tocol [10]. The results show that the success rates doubled ( e.g.,
from 2.5% to 6.6%) when the same attacks were carried out over a
dataset with 4 IDs. See Figure 7(a) in §6.
To mitigate intersection size leakages, we adopt a strategy based
on differentially private (DP) mechanisms. Specifically, we intro-
duce a novel dual-sided DP mechanism that enables both parties
to independently sample and inject dummy identifiers into their
datasets, ID𝐴 and ID𝐵, creating two augmented sets, fID𝐴 and fID𝐵,
respectively.
Input privacy is preserved by the private waterfall matching pro-
tocol, while the intersection size privacy is guaranteed by ensuring
that the distribution of|fID𝐴∩ fID𝐵| is differentially private with
respect to the true size|ID𝐴∩ ID𝐵|. This mechanism obfuscates
the intersection size, making it indistinguishable within a carefully
controlled privacy budget.
The number of dummy identifiers added depends on the size
of the original data set and the desired privacy parameters. By
leveraging our𝑑𝑢𝑟𝑃𝑅𝐹 construction, which enables independent
processing of dimensions, we achieve a tighter DP analysis. This de-
sign allows us to apply parallel composition across multiple dimen-
sions, significantly reducing the exponential overhead of dummy
identifiers required under a sequential composition approach. Con-
sequently, our method scales more efficiently while maintaining
rigorous privacy guarantees, offering a substantial improvement in
the practicality of privacy-preserving multi-dimensional set opera-
tions.
On DP to Multi-Dimension PSI . A naive approach of applying
DP to PSI protocols dimension-by-dimension may appear feasible
at first glance. However, while DP mechanisms can theoretically
mitigate privacy risks posed by type-E and type-X leakages, this
approach incurs exponentially increasing overheads. This stems
from the fact that the intersection size can vary by up to the full
dataset size, as demonstrated by the scenario where all records of
one party could potentially match different identifiers under type-
E/X leakage conditions. In contrast, our waterfall matching protocol
eliminates these leakage vectors entirely, enabling a significantly
reduced overhead when integrated with DP mechanisms.
On the Input Validations. The intersection sizes are effectively
randomized by our dual-sided DP mechanism, provided both parties
correctly sample and add dummies to their input sets. However,
an adversary could bypass this protection and reveal the exact in-
tersection size by simply skipping the sampling step. To prevent
this “simple attack, ” we employ secure hardware, such as Intel SGX,
for code attestation. Each party uses its own secure hardware to
verify that the (encrypted) messages they send are generated by
the intended code, including the correct dummy sampling. Since
the dummy set is common information, it can be hardcoded within
the attested code. Notably, confidentiality of the hardware is unnec-
essary in this setting, as it is managed and executed by the same
party.
2.3 Our Contributions
Our contributions are summarized as follows:
• A general framework for private waterfall matching
without cross-ID leakage.
We propose a novel framework to achieve the waterfall
matching functionality while eliminating cross-ID leakages.
Central to our approach is a functionality we define as the
Distributed, Updatable, and Reversed Pseudorandom Function
(FdurPRF), described in Figure 3. We present two construc-
tions forFdurPRF using hashed Diffie-Hellman (DH) and
Yao’s Garbled Circuit [11].
Preventing cross-ID leakage is critical because it allows
the use of lighter, more efficient differential privacy (DP)
mechanisms to enhance privacy. Applying DP to protocols
with cross-ID leakage would result in significantly higher
overhead, as privacy loss grows exponentially with the
number of IDs. Our solution effectively decouples privacy
loss from cross-ID matches, leading to more scalable and
practical implementations.
• A tightly bounded DP mechanism for protecting inter-
section sizes. We design a differentially private mechanism
where both parties independently sample and add dummy

identifiers to their input sets. This protects the intersection
size with minimal overhead.
We present two analyses to reduce dummy size, improving
efficiency. The first uses FdurPRF to decompose cross-ID
leakage, allowing parallel composition with linear dummy
growth relative to the number of identifiers, compared to
the exponential growth in sequential composition. The sec-
ond uses convolution techniques from [ 12] to minimize
dummies across multiple waterfall matching executions,
such as aggregating conversion data from two ad cam-
paigns.
• Two variants and an optimized implementation. We
extend our protocol to support both P𝐴 and P𝐵 provid-
ing payloads for aggregation and enable general functions
beyond summation by sharing matched homomorphic en-
cryption (HE) ciphertexts for secret sharing.
We implement the protocol using DH-based𝑑𝑢𝑟𝑃𝑅𝐹 and a
lattice-based HE scheme, with HE optimizations that handle
two million records across three ID columns in about 2
minutes (8 threads) over a 100Mbps connection. Our DP-
enhanced protocol achieves practical performance, and we
plan to release our implementation publicly.
2.4 Related Works
In Private Set Intersection (PSI) two parties, P𝐴 with a set𝑋 and
P𝐵 with a set𝑌 , securely compute the intersection𝑋∩𝑌 , without
leaking the information of the items that are not in the intersection
has been studied extensively in a long sequence of works [2, 4, 5, 5,
6, 10, 13–21].
In many settings, the goal is to compute some function𝑓 over the
intersection set, i.e.,𝑓(𝑋∩𝑌), rather than knowing the intersection
itself [2, 22–24]. PSI-cardinality is one example of such an the two
parties are limited to learning only the cardinality (or size) of the
intersection [23, 24]. The private intersection-sum functionality
introduced by Ion et al. [2] is another example where one of the
input sets has integer values associated with the elements in the set
and the two parties aggregate of the integer values associated with
the intersection set. The circuit-based PSI protocols such as [5, 6, 25]
enable the computation of arbitrary symmetric functions securely
over the intersection. To the best of our knowledge, most of the
existing PSI protocols are designed for the single identifier.
Private-ID [10] is the only publicly available solution for multi-ID
matching that comes with membership leakage. More precisely, the
participants in [10] can know the intersection size of any subset of
IDs, leading to an exponential leakage of membership information.
Kacsmar et al. [26] employ DP mechanisms for the cardinality
function𝑓(𝑋∩𝑌) =|𝑋∩𝑌| in a client-server scenario in where
only the client can know the result. Consequently, only central DP
is necessary for their setting. However, in our context, where each
party is inquisitive about membership and there is a potential for
membership attacks, the application of central DP is not suitable.
Instead, a distributed DP approach is required.
Oblivious PRF. In the literature, the oblivious evaluation of a PRF
is commonly defined as a two-party protocol where P𝐴 provides a
key𝑘 and the other party P𝐵 provides an input𝑥. At the end of the
protocol execution, P𝐵 obtains𝐹𝑘(𝑥). There are many constructions
for oblivious PRF protocols, such as [ 27–29]. Moreover, we can
modify an OPRF protocol to a key-distributed and output-reversed
counterpart, i.e., the key is distributed between the two parties
and P𝐴 obtains the evaluation, using homomorphic encryption as
described by [2]. The double-hash approach from [23] is a reversed
OPRF but does not provide key rotation capability.
Many OPRF protocols based on the Dodis-Yampolskiy (DY) PRF
can support key rotation (i.e., updating the PRF key). However, it
seems to require nontrivial efforts to support blind key rotation
when the DY-PRF key is distributed between two parties. We refer
to the survey by Casacuberta et al. [30] for more details on recent
oblivious PRF constructions.
Circuit-based Solutions. One can also leverage the technique
called circuit-based PSI (CPSI), such as [5, 6, 25], which can elimi-
nate the leakage of the intersection sizes. However, the modification
of the current single-ID CPSI protocols to the multi-ID setting in-
volves non-trivial work. A CPSI protocol is basically an asymmetric
set membership testing. That is it allows P𝐵 to query whether its
ID match the ones own by P𝐴. At the end of the protocol execution,
P𝐵 obtains a secretly shared testing bits 𝑏𝑖 = 1 if id1 𝐵,𝑖∈ ID1 𝐴, or
𝑏𝑖 = 0 otherwise. One of the difficulties of adopting the CPSI to
the multi-ID setting is to obliviously delete records that already
matched from the previous IDs. That is because the position of each
ID is computed using a hash function. For instance, the position
of the identifier “a@123” is computed via𝑖 = Hash("a@123"), and
then it is assigned to the𝑖-th position in the query vector. It renders
an inconsistent order of result bits when performing the queries on
a record of different IDs. Communication extensive cryptographic
protocols (e.g., oblivious permutation) are needed to align the order
of the of testing bits (and the payloads).
In the ad applications, the intersection size can be significantly
smaller than the input sets, i.e.,|𝑋∩𝑌|≪ min(|𝑋|,|𝑌|). For in-
stance, a typical ratio is less than 1%. In other words, to evaluate
a downstream function over the intersection using fully private
techniques might introduce a large overhead on the downstream
computation.
3 PRELIMINARIES
3.1 Definitions
Definition 1. (Pseudorandom Functions [31]) Let 𝐹 :{0, 1}∗×
{0, 1}∗ ↦→ {0, 1}∗ be an efficient, length-preserving, keyed func-
tion. We say 𝐹 is a pseudorandom function if for all probabilistic
polynomial-time distinguishersD, there exists a negligible function
negl such that: Pr[D𝐹𝑘(·)(1𝑛) = 1]− Pr[D𝑓𝑛(·)(1𝑛) = 1]≤ negl(𝑛),
where𝑘
$
← −{0, 1}𝑛 is chosen uniformly at random and 𝑓𝑛 is chosen
uniformly at random from the set of functions mapping 𝑛-bit strings
to𝑛-bit strings.
Honest-but-Curious Privacy. We recap the privacy definition
from [32, 33]. Let𝐹 :{0, 1}∗×{ 0, 1}∗↦→{ 0, 1}∗ be a deterministic
functionality where𝐹0(𝑥0,𝑥 1) (resp.𝐹1(𝑥0,𝑥 1)) denotes the 1st ele-
ment (resp. the 2nd) of𝐹(𝑥0,𝑥 1), and let Π be a two-party protocol
for computing𝐹. The view of P𝐴 (resp. P𝐵) during an execution of
Π on(𝑥0,𝑥 1) is denoted ViewΠ 𝐴(𝑥0,𝑥 1) (resp. ViewΠ 𝐵(𝑥0,𝑥 1)).
Definition 2. (Honest-but-Curious Privacy) For a function 𝐹 , we
say that Π privately computes𝐹 if there exist probabilistic polynomial

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
time algorithms, denoted Sim0 and Sim1, such that
{Sim0(𝑥0,𝐹 0(𝑥0,𝑥 1))}𝑥0,𝑥1
𝑐
≡{ ViewΠ 𝐴(𝑥0,𝑥 1)}𝑥0,𝑥1
{Sim1(𝑥1,𝐹 1(𝑥0,𝑥 1))}𝑥0,𝑥1
𝑐
≡{ ViewΠ 𝐵(𝑥0,𝑥 1)}𝑥0,𝑥1,
where
𝑐
≡ denotes computational indistinguishability. This definition
states that the views of the parties can be properly constructed by a
polynomial time algorithm given the party’s input and output solely.
Also, the parties here are semi-honest and the view is therefore exactly
according to the protocol specification.
Differential Privacy. We recall a definition of approximate differ-
ential privacy for interactive two-party protocols, following [34].
Let Σ be a finite alphabet and for strings 𝑥,𝑦 ∈ Σ𝑛, let|𝑥−𝑦|𝐻
denote the Hamming distance between𝑥 and𝑦.
Definition 3. ((𝜖,𝛿)-Differential Privacy) A mechanism M on
Σ𝑛 is a family of probability distributions {𝜇𝑥 :𝑥∈ Σ𝑛} onR. The
mechanism is(𝜖,𝛿)-differentially private if for every 𝑥 and𝑥′ such
that|𝑥−𝑥′|𝐻 = 1 and every measurable subset 𝑆⊂R we have
𝜇𝑥(𝑆)≤ exp(𝜖)𝜇𝑥′(𝑆)+ 𝛿.
The definition of differential privacy naturally extends to in-
teractive protocols, by requiring that the views of all parties be
differentially private in respect to other parties’ inputs. More specif-
ically, let View𝐴 Π(𝑥,𝑦) be the joint probability distribution over𝑥,
the transcript of the protocol Π, private randomness of P𝐴, where
the probability space is private randomness of both parties. For
each𝑥, View𝐴 Π(𝑥,𝑦) is a mechanism over the𝑦’s. Let View𝐵 Π(𝑥,𝑦)
be similarly defined view of P𝐵 whose input is𝑦.
Definition 4. (Differential privacy for two-party protocols) We
say that a protocol Π enables(𝜖,𝛿)-differential privacy if the mech-
anism View𝐴 Π(𝑥,𝑦) is(𝜖,𝛿)-differentially private for all values of 𝑥,
and same holds for View𝐵 Π(𝑥,𝑦) for all values𝑦.
3.2 Security Model
We chose to target the security against honest-but-curious,i.e. semi-
honest adversaries, due to the strong efficiency and monetary re-
quirements of ad conversion applications. The semi-honest model
provides strong privacy protections against data breaches on either
side since semi-honest protocols leak nothing beyond the prescribed
protocol output.
We protect the intersection size by having each party indepen-
dently sample and add dummy identifiers from a common set of
dummies. Even under the semi-honest setting, all parties should
follow the protocol descriptions, e.g., sampling dummy identifiers
from the proper set. However, there is a prisoner’s dilemma where
an adversary can learn the exact intersection size if he/she sim-
ply skips the sampling step, and the honest party cannot detect
this behavior. To guarantee that each party correctly performs the
DP mechanism, we rely on secure hardware such as Intel SGX to
provide code attestation. In brief, the outputs generated by the
hardware are indeed from the code that it attested to. Note that we
do not assume confidentiality for the secure hardware since, in
our case, a party uses his/her own hardware to convince the other
party that he/she has executed a public piece of code properly. This
practice of using secure hardware to achieve code attestation is also
employed by other works such as [35].
3.3 Additively Homomorphic Encryption (AHE)
An AHE schemeHE =(Gen, Enc, Dec, Sum, Refresh) consists of 5
algorithms. Gen outputs a public-private key pair(pk, sk), and spec-
ifies a message spaceM. Given the public key pk and a plaintext
message𝑚∈M , one can compute a ciphertextHE.Encpk(𝑚), an
encryption of𝑚 under pk. Given the secret key sk and a ciphertext
𝐶 = Enc(𝑚), one can run Dec(𝐶) to recover the plaintext𝑚.
Given the public key pk and a set of ciphertexts{𝐶𝑖} encrypt-
ing messages{𝑚𝑖}, one can homomorphically compute a cipher-
text encrypting the sum of the underlying messages, which we
denote for ease of exposition as: Enc(˝ 𝑖𝑚𝑖) = Sum({𝐶𝑖}𝑖). We
will also use the property that one can randomize ciphertexts using
a randomized procedure denoted as Refresh. The two distributions
Refresh(Sum({Enc(𝑚𝑖)}𝑖)) and Refresh(Enc(˝ 𝑖𝑚𝑖)) are statisti-
cally close, even against an adversary that holds the decryption key
sk.
We can instantiate the AHE scheme by the Brakerski/Fan-Vercauteren
scheme (BFV) scheme [36, 37] or the Paillier scheme [38]. Particu-
larly, the current work [2] used the Paillier scheme while we present
some optimizations for the BFV scheme.
4 PROPOSED PROTOCOL FOR W ATERFALL
MATCHING
4.1 Private Waterfall Matching with Sum
Protocol fromFdurPRF
The concrete construction of our private waterfall matching proto-
col is given in Figure 4. Our protocol operates in five stages.
(1) In the first stage, P𝐵 sends homomorphic encryption of
P𝐵’s payloads to P𝐴 along with his public key.
(2) The two parties first send the “random tags” of their IDs
using multiple 𝑑𝑢𝑟𝑃𝑅𝐹 . For instance, on the 𝑏-th ID col-
umn, P𝐵 sendsF𝑑𝑢𝑟𝑃𝑅𝐹 .Send(sid𝑏, ID𝑏 𝐵) and P𝐴 receives
Tag𝑏 𝐵←F𝑑𝑢𝑟𝑃𝑅𝐹 .Recv(sid𝑏). That is P𝐴 obtains the PRF
evaluations on P𝐵’s𝑏-th ID column under a shared key𝑘𝑏.
On the other hand, P𝐵 receives the PRF evaluations onP𝐴’s
IDs under the corresponding key, denoted as Tag𝑏 𝐴.
(3) By exchanging the tags on the 1st ID column, P𝐴 and P𝐵
can obtain the intersection in a reversed way. For instance,
after receiving gTag1 𝐴 in a shuffled order from P𝐵, P𝐴 knows
the matching positions 𝐽 1 𝐵 ={𝑖 : Tag1 𝐵[𝑖]∈ gTag1 𝐴} on the
1st ID column, but P𝐴 does not learn the exact matched
row index in P𝐴’s dataset due to the shuffling. Similarly P𝐵
knows𝐽 1 𝐴 ={𝑖 : Tag1 𝐴[𝑖]∈ gTag1 𝐵}.
(4) Moreover, to avoid the type-E cross-ID leakage, P𝐴 and P𝐵
can first remove the matched rows from the received tags
of the 2nd ID column. Particularly, P𝐴 prepares rTag2 𝐵 =
{Tag2 𝐵[𝑖] = 𝐹𝑘2(ID𝐵[𝑖])}𝑖∉𝐽 1 𝐵 and P𝐵 prepares rTag2 𝐴 =
{Tag2 𝐴[𝑖] =𝐹𝑘2(ID2 𝐴[𝑖])}𝑖∉𝐽 1 𝐴 . Then they perform the match-
ing on the remaining tags. For instance, on receiving grTag2 𝐴
from P𝐵, P𝐴 can know the matching positions due to the
2nd ID column: 𝐽 2 𝐵 ={𝜎(𝑖) : rTag2 𝐵[𝑖]∈ grTag2 𝐴} where𝜎
is an index mapping from|rTag2 𝐴|↦→| ID1 𝐴| that maps the
matching positions in rTag2 𝐴 to their global positions in

Figure 4: Our private waterfall matching protocol under FdurPRF-hybrid model.HE is an AHE scheme.
ID1 𝐴. The type-E cross-ID leakage is avoided from the
sense that 𝐽 1 𝐵∩𝐽 2 𝐵 =∅.
However, it might introduce the type-X cross-ID leakage.
For instance, when∃𝑖∈ 𝐽 1 𝐵⇒ Tag2 𝐵[𝑖]∈ grTag2 𝐴, it reveals
to P𝐴 that a record𝑖 of P𝐵 is matched by two records of P𝐴,
one due to the 1st ID, and the other is due to the 2nd ID. To
mitigate the type-X cross-ID leakage, we further leverage
the blind-update command as follows
P𝐵 : rTag2 𝐴←F𝑑𝑢𝑟𝑃𝑅𝐹 .Update(sid2, sid′ 2, rTag2 𝐴)
P𝐴 : rTag2 𝐵←F𝑑𝑢𝑟𝑃𝑅𝐹 .Update(sid2, sid′ 2, rTag2 𝐵)
so that Tag2 𝐵∩ rTag2 𝐴 =∅ and Tag2 𝐴∩ rTag2 𝐵 =∅ due to
the distinct PRF keys. Thus the type-X leakage is also
avoided.
(5) P𝐴 can then aggregate the HE ciphertexts using the match-
ing lists𝐽 1 𝐵 and𝐽 2 𝐵.
Theorem 1. If the AHE schemeHE is semantic secure then the
protocol Πwmf in Figure 4 securely realizes the Fwmf functionality of
Figure 1 against semi-honest adversaries underFdurPRF-hybrid.
Proof. LetA be a polynomial-time adversary that may corrupt
P𝐴 and P𝐵. We construct a simulator Sim with access to functional-
ityFdurPRF that runsA as a subroutine. Moreover the Sim is also
given the intersection sizes 𝑠1 and𝑠2. We writeO to denote the

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
domain of the PRF, and write 𝑛𝐴 and𝑛𝐵 to denote the database
sizes of P𝐴 and P𝐵, respectively.
Corrupted P𝐴 with a honest P𝐵.
(1) Let(𝑘1 𝐴,𝑘 2 𝐴,𝑘 3 𝐴) be the keysA sends toFdurPRF.Init. Sim
sends an AHE public key, and𝑛𝐵 AHE ciphertexts of zero
toA on behalf of P𝐵.
(2) Let sid𝑏 (𝑏 = 1, 2, 3) be the session idA sends toFdurPRF.Recv.
Sim sends𝑛𝐵 random elements of O toA on behalf of
FdurPRF.
(3) Sim sends𝑛𝐴 random elements fromO toA on behalf of
P𝐵.
(4) Let sid2, sid3 be the session idsA sends toFdurPRF.Update.
Sim samples𝑛𝐵−𝑠1 random elements (designated by 𝑅)
fromO toA on behalf ofFdurPRF.
(5) Sim samples𝑛𝐴−𝑠1 random elements ofO and randomly
replaces𝑠2 of them by a subset of𝑅. Then Sim sends them
toA on behalf of P𝐵.
It is not hard to see that the simulation is computationally close
to an execution of Πwfm in theFdurPRF-hybrid world. In particular,
the simulation relies on the fact that messages sent byP𝐵 are either
AHE ciphertexts or PRF outputs, and the matching positions (e.g.
𝐽 1 𝐵,𝐽 2 𝐵) are randomly shuffled.
The simulation for P𝐵’s view is similar except that we addition-
ally simulate an AHE of aggregation result in Step 18 where the
privacy is guaranteed by theHE.Refresh function. □
4.1.1 AHE Instantiation from (R)LWE. Learning-With-Errors (LWE)-
based encryption schemes are usually quite computationally effi-
cient compared to schemes like Paillier and DGK, since they do not
involve expensive modular-exponentiation operations to encrypt
and decrypt. However, the batch of LWE ciphertexts of the payloads
can be large in volume. To further reduce the communication over-
head, we can first transfer a batch of𝑁 (e.g.,𝑁 = 4096) payloads
inside a Ring LWE ciphertext instead of a batch of LWE ciphertexts.
This reduces the communication by a factor of 𝑂(𝑁). Then, the
ciphertext receiver (e.g., P𝐴 in our case) can unpack the encrypted
payloads from the received Ring LWE ciphertext, i.e., one LWE
ciphertext for each payload value, by performing some inexpensive
local operations. The aggregation is then performed over the LWE
ciphertexts.
We explicitly export the Ring LWE as an encapsulation layer of
the LWE ciphertexts to be more efficient and to offer more flexibility.
Particularly, for the efficiency, the sum step over LWE ciphertexts
is about 2× faster than the corresponding homomorphic additions
over the Ring LWE ciphertexts. For the flexibility, when comes
to the secret sharing variant described in the following section,
P𝐴 can return a "packed" version of the matched LWE ciphertexts
{𝐶[𝑗]}𝑗∈𝐽 1 𝐵∪𝐽 2 𝐵 to P𝐵 using the technique from [39].
4.2 Variants
We considered variants of the waterfall matching protocol that
modify the functionality and offer important flexibility.
4.2.1 Multiple Payloads. Our protocol generalizes easily to cases
where each row in P𝐵’s dataset has multiple types of payloads
(e.g. amount spent, and label of conversion), and parties wish to
learn the sum of each type of payload. This is handled by simply
encrypting each column separately using the AHE, and creating
one sum for each type of payload.
4.2.2 Secret Sharing the Matched Payloads. One variant is to let
P𝐴 reshare the matched HE payloads to P𝐵 in an additively secret
shared form, rather than computing the aggregated sum. This vari-
ant allows more complicated functions beyond the aggregated sum
to be evaluated on the intersection set. To achieve this, P𝐴 now
sendsHE.Refresh

HE.Encpk(𝐶[𝑗]+ 𝑟𝑗)

a batch of AHE cipher-
texts to P𝐵 in Step 17. for 𝑗∈ 𝐽 1 𝐵∪𝐽 2 𝐵. The masking values{𝑟𝑗}
are sampled uniformly from the message space ofHE . Then, the
matched payloads{𝑇[𝑗]} are now additively shared between the
two parties, with P𝐵 holding𝑇[𝑗]+ 𝑟𝑗 and P𝐴 holding−𝑟𝑗 , while
P𝐵 is unaware of the matching positions 𝑗∈ 𝐽 1 𝐵∪𝐽 2 𝐵.
4.2.3 Payloads from Both Parties. Some ad conversion computa-
tions involve payloads from both the publisher and the advertiser.
Our protocol also generalizes easily to support payloads from both
sides. Particularly, we make the following modifications over Fig-
ure 4 to support payloads from both sides:
(1) P𝐴 now generates the AHE key-pair and sends the public
key to P𝐵 in Step 4.
(2) P𝐴 also encrypts its payloads using its public key and at-
taches the AHE ciphertexts in Step 4.
(3) P𝐴 now needs to send the tags rTag2 𝐵 to P𝐵 in Step 15 in
a shuffled order. This enables P𝐵 to obtain the matching
positions on the second identifier 𝐽 2 𝐴. By this point, P𝐵 is
already able to pick up P𝐴’s (encrypted) payloads in the
intersection, i.e.,𝐽 1 𝐴∪𝐽 2 𝐴.
4.3 Concrete Constructions of FdurPRF
We present two constructions ofFdurPRF using Hashed Diffie-Hellman
(HashDH) and Yao’s Garbled circuit [11], respectively. Particularly,
we leverage a functionalityFGC which takes inputs𝑥 and𝑦 from a
circuit generator and a circuit evaluator, respectively, and returns
the evaluation𝐵𝐶(𝑥,𝑦) to the circuit evaluator for a Boolean circuit
𝐵𝐶 :{0, 1}∗×{ 0, 1}∗↦→{ 0, 1}∗ that is agreed upon by both the
generator and the evaluator.
Specifically, in the HashDH-based construction, we leverage a
PRF function defined as𝐹𝑘(𝑥) = H(𝑥)𝑘 where H is a function that
maps bit strings to elements of G.
Theorem 2. If H is modeled as a random oracle, and DDH as-
sumption holds for the group G, the protocol ΠDDH durPRF in Figure 5
securely realizes the functionality FdurPRF with the PRF defined as
𝐹𝑘(𝑥) = H(𝑥)𝑘 .
We give a sketch proof here, and defer the formalized proof to
Appendix.
Proof. (Sketch.) The proof follows the arguments in [ 40, 41].
w.l.o.g, we assume P𝐴 acts as the Sender with input𝑋 and P𝐵 acts
as the Receiver who will invoke the Update command.
Correctness. For the evaluation part, P𝐵 obtains𝑎𝑖 = H(𝑥𝑖)𝑘 𝐴
which is then lifted to 𝑎𝑘𝐵 𝑖 and forms H(𝑥𝑖)𝑘𝐴𝑘𝐵 mod𝑞. For the
update part,

(H(𝑥𝑗)𝑘)𝑘′ 𝐵/𝑘𝐵 𝑘′ 𝐴/𝑘𝐴 =(H(𝑥𝑗)𝑘′ 𝐵𝑘𝐴)𝑘′ 𝐴/𝑘𝐴 = H(𝑥𝑗)𝑘′ 𝐵𝑘′ 𝐴,

Protocol ΠDDH durPRF from HashDH
Initialization:
P𝐴 samples𝑘𝐴,𝑘′ 𝐴 $ ← −Z𝑞. P𝐵 samples𝑘𝐵,𝑘′ 𝐵 $ ← −Z𝑞.
Evaluation: [40] 𝑃𝐴 inputs𝑋 ={𝑥𝑖}𝑚 𝑖=1.
(1) P𝐴:𝑎𝑖← H(𝑥𝑖)𝑘𝐴 for𝑥𝑖∈𝑋 .
(2) P𝐴→ P𝐵 :{𝑎𝑖∈ G}𝑖.
(3) P𝐵 outputs𝑍 ={𝑎𝑘𝐵 𝑖 }.
Update: [41] 𝑃𝐵 selects a subset𝑍′⊂𝑍.
(4) P𝐵 :𝑏𝑗∈ G←𝑧
𝑘′ 𝐵/𝑘𝐵
𝑗 for𝑧𝑗∈𝑍′.
(5) P𝐴← P𝐵 :{𝑏𝑗}𝑗 in a shuffled order.
(6) P𝐴 :𝑏′ 𝑗 =𝑏 𝑘′ 𝐴/𝑘𝐴 𝑗 .
(7) P𝐴→ P𝐵 : e𝑍 ={𝑏′ 𝑗}𝑗 .
(8) P𝐵 outputs e𝑍 by undoing the shuffle in Step 2.
Figure 5: The 𝑑𝑢𝑟𝑃𝑅𝐹 protocol from HashDH. Both parties
agree upon a group G of a prime order𝑞 that the DH assump-
tion holds, and a hash function H :{0, 1}∗→ G that maps bit
strings to elements of G. The corresponding PRF is defined
as𝐹𝑘(𝑥) = H(𝑥)𝑘 .
which is the PRF evaluation𝐹𝑘′(𝑥𝑗) under the new key𝑘′ =𝑘′ 𝐴·𝑘′ 𝐵.
Sender’s (P𝐴) Privacy. For the evaluation part, we claim that the
views of the receiver (i.e., P𝐵) - i.e.,𝑎𝑖 = H(𝑥𝑖)𝑘𝐴 for𝑖 = 1,··· ,𝑚 ,
where H is modeled as a random oracle - is indistinguishable from
𝑟1,··· ,𝑟𝑚 with𝑟𝑖
$
← −G. For the update part, P𝐵 knows{𝑏𝑗} but
P𝐵 can not distinguish{(𝑏𝑗)𝑘′ 𝐴/𝑘𝐴}𝑗 from random elements from
G under the DDH assumption and random oracle model.
Receiver’s (P𝐵) Privacy. For the evaluation part, P𝐵’s privacy is
achieved directly from the CDH assumption. That is,P𝐴 who knows
𝑎𝑖 can not deriveP𝐵’s secret𝑘𝐵 after seeing𝑎𝑘𝐵 𝑖 . For the update part,
the views of the sender (P𝐴), i.e.,(H(𝑥𝑗)𝑘𝐴)𝑘′ 𝐵 , is indistinguishable
from random group elements from G. □
For the GC-based construction in Figure 6, we use the standard
AES encryption AES𝑘(H(𝑥)) as a PRF function, where H maps the
input to an AES block. The circuit generator/evaluator paradigm
of GC naturally allows an oblivious evaluation of the PRF in a
reversed manner by having the PRF receiver act as the circuit eval-
uator. For the update part, we do not perform the key-switching
from AES𝑘(𝑥) to AES𝑘′(𝑥), which might require a circuit twice the
size of the evaluation part. Instead, we define the PRF after the
update by double AES encryption𝐹𝑘′(𝑥) = AES𝑘′(AES𝑘(H′(𝑥))),
which also follows our interface by treating the inner evaluation
AES𝑘(H′(𝑥)) as a hash from{0, 1}∗↦→{ 0, 1}𝜆, given that the inner
AES encryption acts as a pseudorandom permutation.
Theorem 3. If H′ is modeled as a random oracle, the protocol
ΠGC durPRF in Figure 6 securely realizes the functionality FdurPRF under
theFGC hybrid. The PRF is defined as 𝐹𝑘(𝑥) = AES𝑘(H′(𝑥)).
The correctness and security simply reduce to the correctness
and security ofFGC.
4.3.1 Complexities. Let𝑛 = |𝑋|,𝑛′ = |𝑍| and𝐶 be the size of
the AES encryption circuit. In total ΠDDH durPRF requires computing
Protocol ΠGC durPRF fromFGC
Initialization:
P𝐴 samples𝑘𝐴,𝑘′ 𝐴 $ ← − {0, 1}𝜆. P𝐵 samples𝑘𝐵,𝑘′ 𝐵 $ ← − {0, 1}𝜆. Both
parties aggree on a hash function H′ :{0, 1}∗→{ 0, 1}𝜆.
Evaluation: 𝑃𝐴 inputs𝑋 ={𝑥𝑖}𝑚 𝑖=1.
(1) P𝐴:𝑎𝑖← H′(𝑥𝑖) for𝑥𝑖∈𝑋 .
(2) P𝐴 and P𝐵 invokesFGC to evaluate the standard AES encryp-
tions AES𝑘(·) . Particularly, P𝐴 is the circuit generator with
inputs(𝑘𝐴,{𝑎𝑖}) , and P𝐵 is the circuit evaluator with inputs
𝑘𝐵. After the GC execution, P𝐵 obtains𝑍 = {AES𝑘(𝑎𝑖)}𝑚 𝑖=1
where the key is defined as𝑘 =𝑘𝐴⊕𝑘𝐵.
Update: 𝑃𝐵 inputs𝑍′⊂𝑍.
P𝐴 and P𝐵 invokesFGC to evaluate the standard AES encryption. Par-
ticularly, P𝐴 is the circuit generator with inputs𝑘′ 𝐴, and P𝐵 is the cir-
cuit evaluator with inputs(𝑘′ 𝐵,𝑍′). After the GC execution, P𝐵 obtains
{AES𝑘′(𝑧𝑗)}𝑧𝑗∈𝑍′ with the key𝑘′ =𝑘′ 𝐴⊕𝑘′ 𝐵.
Figure 6: The𝑑𝑢𝑟𝑃𝑅𝐹 protocol from Garbled Circuit (GC). The
corresponding PRF is defined as 𝐹𝑘(𝑥) = AES𝑘(H(𝑥)) where
H :{0, 1}∗→{ 0, 1}𝜆 that maps bit strings to an AES block.
2(𝑛+𝑛′) exponentiations. ΠDDH durPRF exchanges𝑂(𝑛(| G|+ 1)) bits for
the PRF evaluation, and𝑂(𝑛′(| G|+ 1)) bits for the update step. On
the other hand, ΠGC durPRF exchanges𝑂(2𝑛𝐶𝜆+𝜆2) bits for the PRF
evaluation, and𝑂(𝑛′𝐶𝜆+𝜆2) bits for the update step.
5 DP MECHANISM FOR W ATERFALL
MATCHING
5.1 DP Mechanism Design
We first consider a mechanism to protect the intersection-size for
the single identifier setting, and then we extend it to the waterfall
matching setting. Randomness is introduced by padding dummy
entries to both input sets𝐴 and𝐵 to create e𝐴 and e𝐵, respectively.
This is done by randomly selecting and adding𝜏 dummy entries
from a common set𝐷 with 2𝜏 rows, which is disjoint from both𝐴
and𝐵. The specific steps are outlined in Algorithm 1.
The following Theorem 4 provides a simple way to enhance the
privacy of any private matching protocol that leaks the intersection
size. For a given target privacy profile(𝜖,𝛿), one can calculate the
parameter𝜏 from (1), which defines the size of the dummy set𝐷.
Theorem 4. Let Π be a semi-honest secure two-party protocol that
takes private input sets 𝐴 and𝐵 from P𝐴 and P𝐵, respectively, and
computes the intersection size, i.e.|𝐴∩𝐵|. Also, let 𝐷 be a common
set of dummies of 2𝜏 entries such that𝐷∩𝐴 =∅ and𝐷∩𝐵 =∅. Then
the composited protocol Π′(𝐴,𝐵) := Π(M𝜏one(𝐴,𝐷),M𝜏one(𝐵,𝐷)) is
a semi-honest secure two-party protocol offering (𝜖,𝛿)-differential
privacy, where DP profile is given by
𝛿(𝜖) = 1 2𝜏 C𝜏 '›››
«
1+
𝜏−1∑︁
𝑧=
l
𝜏·𝑒𝜖/2−1
𝑒𝜖/2+1
m
(𝜏 C𝑧)2−𝑒𝜖·( 𝜏 C𝑧+1)2
“ﬁﬁﬁ
‹
. (1)
To prove Theorem 4, we utilize the following. We writeM(𝐴,𝐵)
to denote a variable of the intersection size between two (single-ID)

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
Algorithm 1:M𝜏one Mechanism for single ID
Input : Set𝑆 of𝑛 entries. Set𝐷 of𝜏′ >𝜏 entries such that
𝐷∩𝑆 =∅.
Output :A new set ˜𝑆 of ˜𝑛 =𝑛+𝜏 entries.
1: 𝐷′⊂𝐷 by randomly selecting a subset of𝜏 entries.
2: Output ˜𝑆 =𝑆+𝐷′ by appending𝐷′ to𝑆.
sets. Note that, up to this point, M(𝐴,𝐵) is independent of the
specific private matching protocol.
Lemma 5. The size of the intersection between two padded sets in
Algorithm 1 can be represented as
M(𝐴,𝐵) =|M𝜏 one(𝐴,𝐷)∩M 𝜏 one(𝐵,𝐷)| =|𝐴∩𝐵|+ 𝑧, (2)
where𝑧 with axisymmetrially Probability Mass Function (PMF):
Pr(𝑧 =𝑧′) =
( (𝜏 C𝑧′) 2
2𝜏 C𝜏 0 <𝑧′≤𝜏,
0 others.
(3)
where𝑛C𝑟 is the combinations out of a group of 𝑛.
In cases where we concentrate on one side, say𝐴, the inclusion
of𝐵 is omitted fromM(𝐴,𝐵) for simplicity, i.e., onlyM(𝐴).
Proof. (Theorem 4) We introduce the privacy loss random vari-
able [42] for a tight DP analysis.
Definition 5. The privacy loss random variable ofM(𝐴) over
M(𝐴′) for any pair of neighboring inputs 𝐴 ∼ 𝐴′ is defined as
follows:
(i) If both Pr(M(𝐴) =𝑜) ≠ 0 and Pr(M(𝐴′) =𝑜) ≠ 0, then
𝜸𝐴𝐴′ = ln
 Pr(M(𝐴) =𝑜)
Pr(M(𝐴′) =𝑜)

. (4)
(ii) If Pr(M(𝐴′) =𝑜) = 0 and Pr(M(𝐴′) =𝑜) ≠ 0, then 𝜸𝐴𝐴′ =∞.
The quantity 𝜸𝐴𝐴′ is the logarithmic ratio between the prob-
ability of observing outcome 𝑜 on input 𝐴,𝐵 compared to input
𝐴′,𝐵 , which is referred to as the privacy loss variable. From Defini-
tion 5, it is apparent that the privacy analysis involves both 𝜸𝐴𝐴′
and 𝜸𝐴′𝐴 by considering the order of𝐴 and𝐴′. According to Defi-
nition 3,M assures tightly(𝜖,𝛿)-DP with𝛿 computed as follows:
𝛿(𝜖) = max(𝛿𝐴𝐴′(𝜖),𝛿𝐴′𝐴(𝜖)) where
𝛿𝐴𝐴′(𝜖) = (5) ∑︁
𝑜∈𝑂
max Pr(M(𝐴) =𝑜)− 𝑒𝜖 Pr(M(𝐴′) =𝑜), 0,
𝛿𝐴′𝐴(𝜖) = (6) ∑︁
𝑜∈𝑂
max Pr(M(𝐴′) =𝑜)− 𝑒𝜖 Pr(M(𝐴) =𝑜), 0.
To streamline the analysis, we demonstrate the property that
when employing a DP mechanism with axisymmetrially distributed
additive noise such as that proposed in Algorithm 1, the order of
neighboring data sets can be disregarded in the privacy analysis.
Property 1. If and only if the PMF of M(𝐴) is axisymmetrically
distributed, as exemplified by Pr(𝑧) in (3), the following relationship
holds for any non-negative 𝜖:𝛿𝐴′𝐴(𝜖) =𝛿𝐴𝐴′(𝜖).
Algorithm 2:Mmult Mechanism for multiple IDs
Input : Sets{𝑆ℓ}𝑚 ℓ =1,{𝐷ℓ}𝑚 ℓ =1, and{ ˆ𝐷ℓ}𝑚 ℓ =1.𝑆ℓ is a set of𝑛
entries.𝐷ℓ, ˆ𝐷ℓ are sets of 2𝜏 and 2𝜏𝑚 entries, respectively.
Output :New sets{ ˜𝑆ℓ}𝑚 ℓ =1 of𝑛+𝑚𝜏 entries each.
1: for 1≤𝑘≤𝑚 do
2: Initialize ˜𝑆𝑘 =𝑆𝑘 .
3: for 1≤ℓ <𝑘 do
4: Update the set ˜𝑆𝑘←M 𝜏one( ˜𝑆𝑘, ˆ𝐷ℓ)
5: end for
6: Update the set ˜𝑆𝑘←M 𝜏one( ˜𝑆𝑘,𝐷𝑘)
7: for𝑘 <ℓ≤𝑚 do
8: Update the set ˜𝑆𝑘←M 𝜏one( ˜𝑆𝑘, ˆ𝐷ℓ)
9: end for
10: end for
Property 1 simplifies the DP analysis by allowing the privacy
accountant with either (5) or (6). Therefore, simplify 𝜸𝐴𝐴′ as 𝜸.
Substituting (3) into (4), we have
Pr𝜸(𝜸 = ln(𝜏 C𝑧/𝜏 C𝑧+1)) =(𝜏 C𝑧)2 2𝜏 C𝜏 , ∀𝑧∈[ 0,...,𝜏 ]. (7)
Meanwhile, (5) can be reformulated as
𝛿(𝜖)≥ E𝜸[max{0, 1− exp(𝜖−𝛾)}]
=𝛿(+∞)+
∫ ∞
𝜖
(1− exp(𝜖−𝛾)) Pr𝜸(𝛾)𝑑𝛾. (8)
In this context,𝛿(+∞) addresses failures resulting from the support
discrepancy betweenM(𝐴) andM(𝐴′), where a single occurrence
leads to infinite leakage, i.e.,
𝛿(+∞) = Pr(M(𝐴) =|𝐴∩𝐵|). (9)
By further substituting (9) into the second term in the right-hand-
side of (8), we acquire the intersection size’s DP profile using Algo-
rithm 1, as outlined in Theorem 4 below. □
5.2 DP Mechanism for the Multi-ID Matching
DP protection in multi-ID scenarios can be accomplished by ap-
plying the single-ID DP mechanism to each ID column. It is well-
known that the composition of DP mechanisms compromises the
privacy of DP protection. SupposeM𝜏one (i.e., Algorithm 1) achieves
(𝜖ℓ,𝛿ℓ)-DP for its intersection size for theℓ-th ID column. The basic
composition reveals that DP protection, considering the observation
of each intersection size of each ID column from the two parties,
is(𝜖,𝛿)-DP, where𝜖 = ˝𝑚 ℓ=1𝜖ℓ and𝛿 = ˝𝑚 ℓ=1𝛿ℓ. Consequently, the
protective capacity of DP diminishes linearly with an increase in
the number of IDs.
The linear rate of diminishing DP is attributed to the fact that
different IDs matched for each column could correspond to the same
record. If there is a way to ensure that the cross-ID dummies cover
disjoint subsets of the data records, the sequential composition is
no longer a tight DP analysis. Instead, the combined privacy loss is
the maximum of𝜖ℓ for allℓ∈[ 1,𝑚] from the parallel composition
theorem. To ensure that cross-ID dummies cover disjoint subsets of
the dummy records, we propose Algorithm 2 to construct dummy
variables. The sufficient condition for parallel composition is that

the dummies padded for different ID columns come from disjoint
spaces and cannot match.
Property 2. (DP profile for Waterfall Matching.) In Algorithm 2,
if the mechanism M𝜏one provides achieving (𝜖,𝛿)-DP for each ID
column, then theMmult mechanism also achieves(𝜖,𝛿)-DP for the
waterfall matching.
5.3 DP-enhanced Waterfall Matching Protocol
The DP-enhanced waterfall matching Πdp-wmf operates as follows.
(1) P𝐴 and P𝐵 compute the dummies size 𝜏 according to (1)
under the DP profile(𝜖,𝛿).
(2) P𝐴 and P𝐵 agree on dummy sets Dmy =(𝐷1, ˆ𝐷1,𝐷 2, ˆ𝐷2).
Particularly,|𝐷1| =|𝐷2| = 2𝜏 and| ˆ𝐷1| =| ˆ𝐷2| = 4𝜏, and
there are disjoint to each other,i.e.,𝐷1∩𝐷2 =∅, ˆ𝐷1∩ ˆ𝐷2 =∅,
𝐷1∩ ˆ𝐷2 =∅, and ˆ𝐷1∩𝐷2 =∅.
(3) P𝐴 samples{fID𝑏 𝐴}𝑏←M mult({ID𝑏 𝐴}𝑏,{𝐷𝑏}𝑏,{ ˆ𝐷𝑏}𝑏) ac-
cording to Algorithm 2.
(4) P𝐵 samples{fID𝑏 𝐵}𝑏←M mult({ID𝑏 𝐵}𝑏,{𝐷𝑏}𝑏,{ ˆ𝐷𝑏}𝑏) ac-
cording to Algorithm 2.
(5) P𝐵 appends e𝑇←𝑇∥0 with zeros to|e𝑇| =|fID1 𝐵|.
(6) P𝐴 and P𝐵 jointly run Πwmf on the modified inputs, i.e.,
(fID1 𝐴,fID2 𝐴) and(fID1 𝐵,fID2 𝐵, e𝑇).
This DP-enhanced protocol Πdp-wmf is clearly a secure two-party
protocol as long as the base protocol Πwmf is secure. Note that
P𝐴 and P𝐵’s views in Πdp-wmf differ from their views in the base
protocol Πwmf only with respect to the intersection size. Thus, the
Πdp-wmf protocol ensures(𝜖,𝛿)-differential privacy (Definition 4)
for the intersection sizes by a similar composition argument in
Theorem 4.
Discussions. P𝐴 and P𝐵 can generate a common set of randomness
by sharing a random seed. Moreover, to make sure the disjoint
requirements (i.e.,𝐷∩𝐴 =∅ and𝐷∩𝐵 =∅), they can leverage
the specific type of the identifier. For instance, suppose the target
identifier is the "phone numbers", then P𝐴 and P𝐵 can generate the
dummies from the alphabet set, or they can generate the dummies
with longer digits than a valid phone number.
5.4 A Tighter Privacy Profile for Multiple
Executions of Waterfall Matching
There are real needs to perform matching over the same ID sets
multiple times. For instance:
• The ad publisher and the advertiser may perform the match-
ing twice to aggregate ad conversion data across two ad
campaigns launched in close proximity.
• The advertiser may want to change the payload and perform
one more matching after having seen the aggregated value
from the first matching.
From the privacy perspective, the notion of combining multiple
DP intersection results while preserving the overall privacy guar-
antee is referred to as the sequential DP composition problem. One
widely adopted analysis is the sequential composition, revealing a
linear increasing rate of𝜖. Given the inversely proportional rela-
tionship between the dummy size𝜏 and𝜖, it is natural to explore
a tight DP composition that decreases𝜏 the number of dummies
Algorithm 3: Find the minimal𝜏 for multiple executions.
Input : Total DP budget(𝜖,𝛿); Total numbers of
executions:𝑘;
Output :The number of dummies added for DP:𝜏.
procedure Estimate-𝛿(𝜏,𝑘,𝜖,𝑛 𝑥 )
2: FFT window: 𝑊 =(4𝑘− 2) ln𝜏.
FFT resolution: Δ𝑥 = 2𝑊/𝑛𝑥 .
4: Initialize PLD vector as an all zeros vector 𝑃Γ∈ R𝑛𝑥 .
for𝑜∈[ 0,...,𝜏 − 1]: do
6: Update: 𝑃Γ[⌈(𝑊+ 2 ln𝜏 C𝑜− 2 ln𝜏 C𝑜+1)/Δ𝑥⌉] =(𝜏 C𝑜) 2/2𝜏 C𝜏
end for
8: Compute the convolutions via FFT: 𝑏 =𝐷F−1 F(𝐷·𝑃Γ)𝑘, where
𝐷 =

0 𝐼𝑛𝑥/2
𝐼𝑛𝑥/2 0

.
Compute the starting point:𝛾𝜖 =
l
𝜖+𝑊
Δ𝑥
m
.
10: Return 𝛿′ = 1−  1− 1 2𝜏 C𝜏 𝑘 + ˝𝑛𝑥𝛾 =𝛾𝜖(1−𝑒𝜖+𝑊−𝛾 Δ𝑥)𝑏[𝛾].
end procedure
1: Set𝜏lo = 0
2: Increase𝜏hi = 0, 1,··· , until𝛿≤ Estimate-𝛿(𝜏hi,𝑘,𝜖,𝑛 𝑥).
3: while𝜏lo <𝜏hi do
4: Set𝜏′ =⌈(𝜏lo+𝜏hi)/2⌉.
5: 𝛿′← Estimate-𝛿(𝜏′,𝑚,𝜖,𝑊,𝑛 𝑥).
6: Set𝜏lo←𝜏′ if𝛿′≥𝛿. Otherwise set𝜏hi←𝜏′ if𝛿′ <𝛿.
7: end while
8: Output𝜏hi.
under the same privacy budget𝜖. We adapt the composition results
shown in [12] to our multiple execution cases. Given Pr𝜸 in (7),
after𝑘 times of execution of our waterfall matching protocol, the
composition is tightly(𝜖,𝛿)-DP for𝛿𝑚(𝜖) given by
𝛿𝑘(𝜖) = 1−(1−𝛿(+∞))𝑘+
∫ ∞
𝜖
1− e𝜖−𝛾  Pr𝜸∗𝑘 Pr𝜸  (𝛾)d𝛾,
(10)
where𝛿𝑘(𝜖) denotes the post-composition privacy profile, and∗𝑘
denotes the𝑘 times convolution. According to (9), it is straightfor-
ward that,
𝛿𝑘(𝜖) = 1−

1− 1 2𝜏 C𝜏
𝑘
+
∑︁
𝛾 :𝜖<𝛾 <∞
(1−𝑒𝜖−𝛾) Pr𝜸(𝛾)⊛𝑘, (11)
where(·)⊛𝑘 denotes the𝑘-fold convolution. Note that directly solv-
ing Pr𝜸(𝛾)⊛𝑘 exhibits exponentially computation complexity w.r.t.
𝑘. Following similar steps as presented in [ 12], we present the
two-party DP composition accounting algorithm based on FFT in
Algorithm 3, subsequently, we outline steps to numerically derive𝜏
that guarantees(𝜖,𝛿)-DP after𝑘-fold composition in Algorithm 3.
FFT-based composition for privacy loss involves representing the
distribution as a sparse vector, marking specific locations indicating
data leakage and their probabilities. This vector is transformed into
the frequency domain using FFT, followed by multiplication op-
erations to handle convolution. Matrix expressions simplify these
complex operations into linear transformations and power compu-
tations. The processed sequence is then reverted to the time domain
using the inverse FFT transformation.
FFT significantly improves the computation cost from O(𝑛2)
toO(𝑛 log(𝑛)), where𝑛 denotes the length of Pr𝜸(𝛾)⊛𝑘. However,
FFT requires the input sequence to be periodic. Further, the input

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
Table 1: The minimum dummies size 𝜏 is a function 𝜏 =
𝜏(𝑛,𝑚,𝜖,𝛿,𝑘 ) of𝑛 the input size 𝑛,𝑚 the number of IDs,(𝜖,𝛿)
the DP profile, and𝑘 the maximum sequential matching. The
below are fixed by 𝑚 = 3.
𝑘 = 1,𝜖 = 1,𝛿 = 1/(10𝑛) 𝑘 = 6,𝜖 = 1,𝛿 = 1/(10𝑛)
𝑛 104 105 106 107 𝑛 104 105 106 107
𝜏 114 141 170 201 𝜏 285 353 425 503
𝑘 = 1,𝜖 = 2,𝛿 = 1/(10𝑛) 𝑘 = 6,𝜖 = 2,𝛿 = 1/(10𝑛)
𝑛 104 105 106 107 𝑛 104 105 106 107
𝜏 77 96 116 137 𝜏 191 239 289 340
sequence should be cast to a periodical window with size, say𝑊 ,
no less than the length of FFT result to avoid information loss due
to spectrum overlap. To this end, we proved the following property
with details in Appendix, and it is used to set the parameter 𝑊
required in our waterfall matching protocol.
Property 3. (Minimal FFT window) The minimal window size
for FFT to guarantee no spectrum overlap is 𝑊≥( 4𝐾− 2) ln𝜏.
Further, casting continuously-valued leakages to discrete vector
locations incurs information loss. The discretization is handled
by the resolution factor 𝑛𝑥 that represents the total number of
entries on the input sequence vector. Intuitively, larger 𝑛𝑥 leads
to high input resolution, and thereby reduces information loss.
However, large𝑛𝑥 inevitably increases the computation complexity.
By examining line 6 of the Estimate-𝛿 procedure in Algorithm 3,
this line projects the continuously valued leakage onto the closest
discretized location to its right. In essence, this means that the
leakage is consistently amplified or increased, thereby ensuring
that the calculated𝛿′ is always greater than or equal to the true𝛿
that accurately reflects the exact leakage.
In summary, for a given target(𝜖,𝛿), one can calculate the pa-
rameter𝜏 using Algorithm 3.
6 EXPERIMENTS
Testbed. All computational cost measurements for our protocols
are in terms of total wall-clock runtime for both parties, running
on cloud instances with an Intel(R) Xeon(R) Platinum 8336C CPU
(2.30GHz) and 64GB of RAM. Communication cost includes the
inbound and out-bound traffice of the two parties. We consider
three network conditions, including LAN (10Gbps, 0.2ms ping),
MAN (1Gbps, 2ms ping), and WAN (100Mbps, 20ms ping).
Synthetic Data. We consider balanced databases|𝑋| =|𝑌| = 𝑛
for 103 ≤ 𝑛 ≤ 107 with the number of IDs 𝑚 = 2, 3. The total
intersection size is set as|𝑋∩𝑌| = 0.02𝑛. The payloads are at most
32 bits long.
Implementations of𝑑𝑢𝑟𝑃𝑅𝐹 . For the DDH-based construction,
we use OpenSSL’s implementation “prime256v1”, a NIST elliptic
curve with 256-bit group elements, as the group G. For the random
oracle, we use SHA-256 and apply the “try-and-increment” method
to map bit-string to group elements [43]. We mention a common
trick for the DDH-based construction. For the update command,
we can truncate the updated group element ( i.e.,𝑏′ 𝑗 in Step 4 in
Figure 5) to save some communication. For instance, we only send
1 ID 4 IDs
0
1
2
3
4
5
6Percent (%) of Success
2.52%
6.64%
0.22%
1.57%
0.00% 0.00%
Jiang et al.'s attack
Guo et al.'s attack
Jiang et al.'s attack after DP
(a) Revealing the intersection sizes in the
multi-ID setting are more susceptible to
membership inference attacks.
1 2 3 4 5 6 7
#IDs
0
100
200
300
400
500
#dummies(parallel comp.)
#dummies (sequential comp.)
(b) The parallel composition introduces
less dummies than the sequential com-
position under the profile (𝜖 = 1.0,𝛿 =
10−6).
Figure 7: (a) The robustness of the DP-enhanced protocol
against the two membership inference attacks. (b) The paral-
lel composition introduces less dummies.
the least significant𝛾 bits of𝑏′ 𝑗 . This is suffice for the private match-
ing function given that the the least significant bits of a random
element of G are indistinguishable from a uniform bit-string [44].
Particularly, we set 𝛾 = 96. For the GC-based construction, we
use the EMP-toolkit [45] and set the AES block size 𝜆 = 128. For
the random oracle, we use the BLAKE2b hash function to produce
128-bit digests. For the AHE, we use the SEAL library [46] for the
BFV scheme with the AVX512 acceleration [47]. Specifically, we
use BFV with an 118-bit ciphertext modulus and a 64-bit plaintext
modulus, with 8192 coefficients per ciphertext. Each ciphertext is
236 KB2 and can hold up to 8192 payloads of 64-bit each.
6.1 Enhancing Privacy via DP
Table 1 shows the corresponding dummy sizes under different in-
put settings according to Algorithm 3. Briefly, the dummy size
is significantly smaller than the input size by virtue of the paral-
lel decomposition and FFT technique applied. In Figure 7(a), we
demonstrate the robustness of the DP-enhanced protocol against
two membership inference attacks. Specifically, it illustrates that the
membership leakage after𝑘 = 20 executions of a size-revealing pri-
vate matching protocol can be up to 6% using recent attacks [8, 48].
However, after applying our DP protection for the intersection size,
we do not observe any successful inferences using these attacks.
Figure 7(b) depicts the effectiveness of the parallel decomposition
for introducing less number of dummies. This also translates to the
FFT-based composition technique used for multiple executions of
the waterfall matching.
6.2 Micro-benchmarks
Table 2 depicts the micro-benchmarks for the two constructions of
𝑑𝑢𝑟𝑃𝑅𝐹 . Specifically, the DDH-based construction is more compu-
tation intensive but has significantly less communication overhead.
On the other hand, the GC-based construction introduces a signifi-
cantly larger communication overhead.
A Note on PSI Based on Symmetric Primitives It is often per-
ceived that the DDH-based approach may be less efficient than
conventional symmetric-primitive-based PSI protocols. However,
existing experimental results challenge this misconception. For
instance, Peter et al. reported a circuit-based PSI implementation
2We can leverage the symmetric version of BFV to reduce the size to 118KB.

Table 2: Benchmarks of 𝑑𝑢𝑟𝑃𝑅𝐹 . Single threaded. The time
was measured under the LAN setting.
Send Command
DDH GC
Input𝑛 Time Commu. Time Comm.
103 0.19s 32.23KB 0.52s 209.74MB
104 1.88s 322.26KB 5.21s 2.05GB
105 18.56s 3.15MB 51.23s 20.46GB
106 185.61s 31.52MB 512.49s 204.56GB
Update Command
DDH GC
Input𝑛 Time Commu. Time Comm.
103 0.16s 43.95KB 0.52s 209.74MB
104 1.62s 439.45KB 5.21s 2.05GB
105 16.48s 4.29MB 51.23s 20.46GB
106 163.06s 41.92MB 512.49s 204.56GB
† 1GB = 210 MB = 220 KB = 230 bytes
Table 3: Benchmarks the proposed waterfall matching proto-
col using ΠDDH durPRF. 8 threads were used for each party.
Matching for Sum (#IDs𝑚 = 2)
𝑛 Commu. LAN MAN WAN
104 2.91MB 1.89s 2.03s 3.51s
105 26.61MB 6.93s 7.22s 10.54s
106 263.1MB 68.01s 69.86s 88.18s
107 2631MB 697s 719s 911s
Matching for Share (#IDs𝑚 = 3)
𝑛 Comm. LAN MAN WAN
104 4.14MB 1.42s 1.48s 3.58s
105 41.36MB 11.29s 11.41s 15.44s
106 410.64MB 106.68s 109.71s 139.35s
107 4102MB 1095s 1121s 1430s
Matching for Share (#IDs𝑚 = 2)
𝑛 Comm. LAN MAN WAN
104 3.16MB 0.95s 1.18s 2.63s
105 26.85MB 6.93s 7.73s 10.98s
106 237.19MB 72.46s 74.17s 94.09s
107 2637MB 732s 742s 940s
Matching for Share (#IDs𝑚 = 3)
𝑛 Comm. LAN MAN WAN
104 4.64MB 2.36s 2.16s 3.76s
105 41.59MB 11.99s 12.34s 16.69s
106 411.36MB 110.02s 114.28s 145.79s
107 4109MB 1125s 1153s 1456s
(single identifier) requiring 8 CPU cores and 103 seconds (277 MB
memory) for a dataset of𝑛 = 106 records [49, Table 4]. This demon-
strates 2× higher CPU workloads and 3.7× greater communication
overhead compared to our DDH-based method.
6.3 Benchmark the Private Waterfall Matching
Table 3 shows the performance of our waterfall matching protocol
under different network conditions. From the results, we see that
the Matching-for-Sum and the Matching-for-Share variant do not
change much. That is because the 𝑑𝑢𝑟𝑃𝑅𝐹 part (i.e., DDH-based
𝑑𝑢𝑟𝑃𝑅𝐹 ) dominates the computation and communication. The AHE
part only takes a very small portion of the whole protocol for two
reasons. First, the BFV is very efficient for encrypting a long vector,
i.e., million records per second. Second, the intersection size is
significantly smaller than the input size, leading a relatively smaller
workload for the AHE, e.g., addition and decryption. Overall, our
waterfall matching protocol is practical to handle large-scale input
sets.
6.4 Comparison with Existing Solutions
Figure 8 shows a comparison with two existing approaches. To the
best of our knowledge, none of the existing approaches fully realize
waterfall matching without cross-ID leakages. This is because most
of them are designed for the single ID setting.
6.4.1 Private-Join-then-Sum (PJS) [ 2]. Ion et al. present a matching-
for-sum protocol using hashed DDH and the Paillier AHE scheme.
Their approach works for a single ID and reveals the exact inter-
section size. We re-ran their implementation3 in our environment.
Due to the superiority of the BFV scheme over the Paillier scheme,
our approach is about 20× faster, with approximately one-tenth the
communication overhead compared to their approach.
6.4.2 P S3I [17], a matching-for-share protocol with payloads from
both sides. We also perform the benchmark under the single-ID set-
ting with two payload columns, and we compare the performance
using their implementation4. In general, our protocol is about 2
order of magnitude faster than PS3I with 85% less communication.
This improvement is a result of multiple factors. PS3I [17] utilizes
the Paillier scheme which is less efficient than the BFV scheme we
used. Also, PS3I [17] transfer all encrypted payloads while our ap-
proach only transfer the encrypted payload within the intersection.
CONCLUSIONS
In this paper, we propose a practical and privacy-preserving solu-
tion to the multidimensional matching problem. By integrating a
novel two-party distributed differential privacy mechanism with
a specially tailored matching protocol, our approach effectively
mitigates membership inference leakage. Our design satisfies the
practical requirements for handling multiple identifiers while mini-
mizing the overhead of additional dummy elements needed for pri-
vacy protection. This combination of robust privacy guarantees and
computational efficiency represents a significant advancement in
privacy-preserving data matching, offering both theoretical rigour
and practical applicability for real-world deployment.
REFERENCES
[1] “Advanced Matching, ” https://developers.facebook.com/docs/meta-pixel/adva
nced/advanced-matching, 2025.
3 https://github.com/google/private-join-and-compute
4 https://github.com/facebookresearch/Private-ID

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
103 104 105
#Samples n
100
101
102
Time (s)
19X
21X
20X
Matching for Sum
PJS Time
Ours Time
103 104 105
#Samples n
100
101
102
103
104
Time (s)
148X
271X
341X
Matching for Share
PS3I Time
Ours Time
0
10
20
30
40
50
60
Comm. (MB)
PJS Comm.
Ours Comm.
0
25
50
75
100
125
150
175
Comm. (MB)
PS3I Comm.
Ours Comm.
Figure 8: Comparison with the PJS [ 2] protocol and the
PS3I [17] protocol. For our DDH-based protocol, we configure
the DP profile with the parameters (𝑘 = 6,𝑚 = 3,𝜖 = 2,𝛿 =
1/(10𝑛)). The experiments were conducted under the LAN
network setting, utilizing one single thread per party.
[2] M. Ion, B. Kreuter, A. E. Nergiz, S. Patel, S. Saxena, K. Seth, M. Raykova, D. Shana-
han, and M. Yung, “On deploying secure computing: Private intersection-sum-
with-cardinality, ” in2020 IEEE European Symposium on Security and Privacy
(EuroS&P). IEEE, 2020, pp. 370–389.
[3] P. Buddhavarapu, A. Knox, P. Mohassel, S. Sengupta, E. Taubeneck, and V. Vlaskin,
“Private matching for compute. ”IACR Cryptol. ePrint Arch., vol. 2020, p. 599, 2020.
[4] M. Ion, B. Kreuter, A. E. Nergiz, S. Patel, S. Saxena, K. Seth, M. Raykova,
D. Shanahan, and M. Yung, “On deploying secure computing: Private
intersection-sum-with-cardinality, ” inIEEE European Symposium on Security
and Privacy, EuroS&P, 2020. [Online]. Available: https://doi.org/10.1109/EuroSP
48549.2020.00031
[5] B. Pinkas, T. Schneider, O. Tkachenko, and A. Yanai, “Efficient circuit-based
PSI with linear communication, ” inAdvances in Cryptology - EUROCRYPT 2019 ,
Y. Ishai and V. Rijmen, Eds., 2019.
[6] N. Chandran, D. Gupta, and A. Shah, “Circuit-psi with linear complexity via
relaxed batch OPPRF, ”Proc. Priv. Enhancing Technol., vol. 2022, no. 1, pp. 353–372,
2022. [Online]. Available: https://doi.org/10.2478/popets-2022-0018
[7] G. Garimella, P. Mohassel, M. Rosulek, S. Sadeghian, and J. Singh, “Private set
operations from oblivious switching. ” inPublic Key Cryptography (2) , 2021, pp.
591–617.
[8] X. Guo, Y. Han, Z. Liu, D. Wang, Y. Jia, and J. Li, “Birds of a feather flock
together: How set bias helps to deanonymize you via revealed intersection sizes, ”
in 31st USENIX Security Symposium (USENIX Security 22) . USENIX Association,
Aug. 2022. [Online]. Available: https://www.usenix.org/conference/usenixsecuri
ty22/presentation/guo
[9] B. Jiang, J. Du, and Q. Yan, “Anonpsi: An anonymity assessment framework for
psi, ” inThe Network and Distributed System Security Symposium (NDSS) 2024 ,
Boston, MA, Feb. 2024.
[10] P. Buddhavarapu, B. M. Case, L. Gore, A. Knox, P. Mohassel, S. Sengupta, E. Taube-
neck, and M. Xue, “Multi-key private matching for compute, ”Cryptology ePrint
Archive, 2021.
[11] A. C.-C. Yao, “How to generate and exchange secrets, ” in27th annual symposium
on foundations of computer science (Sfcs 1986) . IEEE, 1986, pp. 162–167.
[12] A. Koskela, J. Jälkö, L. Prediger, and A. Honkela, “Tight approximate differential
privacy for discrete-valued mechanisms using fft, ”arXiv preprint arXiv:2006.07134,
2020.
[13] H. Chen, K. Laine, and P. Rindal, “Fast private set intersection from homomorphic
encryption, ” inProceedings of the 2017 ACM SIGSAC Conference on Computer and
Communications Security, 2017, pp. 1243–1255.
[14] B. Pinkas, T. Schneider, and M. Zohner, “Faster private set intersection based on
OT extension, ” in23rd USENIX Security Symposium (USENIX Security 14) , 2014,
pp. 797–812.
[15] V. Kolesnikov, R. Kumaresan, M. Rosulek, and N. Trieu, “Efficient batched oblivi-
ous prf with applications to private set intersection, ” inProceedings of the 2016
ACM SIGSAC Conference on Computer and Communications Security , 2016, pp.
818–829.
[16] M. J. Freedman, K. Nissim, and B. Pinkas, “Efficient private matching and set inter-
section, ” inInternational conference on the theory and applications of cryptographic
techniques. Springer, 2004, pp. 1–19.
[17] P. Buddhavarapu, A. Knox, P. Mohassel, S. Sengupta, E. Taubeneck, and V. Vlaskin,
“Private matching for compute, ”Cryptology ePrint Archive, 2020.
[18] F. Karakoç and A. Küpçü, “Linear complexity private set intersection for secure
two-party protocols, ” inInternational Conference on Cryptology and Network
Security. Springer, 2020, pp. 409–429.
[19] P. Branco, N. Döttling, and S. Pu, “Multiparty cardinality testing for threshold
private intersection, ” in PKC 2021 , ser. Lecture Notes in Computer Science,
J. A. Garay, Ed., vol. 12711. Springer, 2021, pp. 32–60. [Online]. Available:
https://doi.org/10.1007/978-3-030-75248-4_2
[20] S. Ghosh and M. Simkin, “The communication complexity of threshold
private set intersection, ” in CRYPTO 2019 , ser. Lecture Notes in Computer
Science, vol. 11693. Springer, 2019, pp. 3–29. [Online]. Available:
https://doi.org/10.1007/978-3-030-26951-7_1
[21] E. Zhang, J. Chang, and Y. Li, “Efficient threshold private set intersection, ”
IEEE Access , vol. 9, pp. 6560–6570, 2021. [Online]. Available: https:
//doi.org/10.1109/ACCESS.2020.3048743
[22] M. Ciampi and C. Orlandi, “Combining Private Set-Intersection with Secure
Two-Party Computation, ” inSCN, 2018, pp. 464–482.
[23] E. D. Cristofaro, P. Gasti, and G. Tsudik, “Fast and Private Computation of
Cardinality of Set Intersection and Union, ” inCANS, 2012, pp. 218–231.
[24] S. K. Debnath and R. Dutta, “Secure and Efficient Private Set Intersection Cardi-
nality Using Bloom Filter, ” inISC, 2015, pp. 209–226.
[25] Y. Huang, D. Evans, and J. Katz, “Private Set Intersection: Are Garbled Circuits
Better than Custom Protocols?” in NDSS, 2012.
[26] B. Kacsmar, B. Khurram, N. Lukas, A. Norton, M. Shafieinejad, Z. Shang, Y. Baseri,
M. Sepehri, S. Oya, and F. Kerschbaum, “Differentially private two-party set
operations, ” in2020 IEEE European Symposium on Security and Privacy (EuroS&P) .
IEEE, 2020, pp. 390–404.
[27] M. Naor and O. Reingold, “Number-theoretic Constructions of Efficient Pseudo-
random Functions, ” inFOCS, 1997, pp. 458–467.
[28] Y. Dodis and A. Yampolskiy, “A verifiable random function with short proofs
and keys, ” inPKC, 2005, pp. 416–431.
[29] V. Kolesnikov, R. Kumaresan, M. Rosulek, and N. Trieu, “Efficient Batched Oblivi-
ous PRF with Applications to Private Set Intersection, ” inCCS, 2016, pp. 818–829.
[30] S. Casacuberta, J. Hesse, and A. Lehmann, “Sok: Oblivious pseudorandom func-
tions, ” inEuroS&P, 2022, pp. 625–646.
[31] J. Katz and Y. Lindell,Introduction to Modern Cryptography, Second Edition. CRC
Press, 2014.
[32] O. Goldreich, The Foundations of Cryptography - Volume 2: Basic Applications .
Cambridge University Press, 2004. [Online]. Available: http://www.wisdom.wei
zmann.ac.il/%7Eoded/foc-vol2.html
[33] R. Canetti, “Security and Composition of Multiparty Cryptographic Protocols, ”J.
Cryptol., vol. 13, no. 1, pp. 143–202, 2000.
[34] A. McGregor, I. Mironov, T. Pitassi, O. Reingold, K. Talwar, and S. Vadhan, “The
limits of two-party differential privacy, ” in2010 IEEE 51st Annual Symposium on
Foundations of Computer Science . IEEE, 2010, pp. 81–90.
[35] N. Kumar, M. Rathee, N. Chandran, D. Gupta, A. Rastogi, and R. Sharma, “Crypt-
flow: Secure tensorflow inference, ” inSymposium on Security and Privacy , 2020,
pp. 336–353.
[36] Z. Brakerski, “Fully Homomorphic Encryption without Modulus Switching from
Classical GapSVP, ” inCRYPTO, 2012, pp. 868–886.
[37] J. Fan and F. Vercauteren, “Somewhat Practical Fully Homomorphic Encryption, ”
IACR Cryptol. ePrint Arch., 2012.
[38] P. Paillier, “Public-Key Cryptosystems Based on Composite Degree Residuosity
Classes, ” inEUROCRYPT, 1999, pp. 223–238.
[39] H. Chen, W. Dai, M. Kim, and Y. Song, “Efficient homomorphic conversion
between (ring) LWE ciphertexts, ” inACNS, 2021, pp. 460–479.
[40] S. Jarecki and X. Liu, “Fast secure computation of set intersection, ” inSCN, 2010,
pp. 418–435.

[41] A. Everspaugh, R. Chatterjee, S. Scott, A. Juels, and T. Ristenpart, “The pythia
PRF service, ” inUSENIX Security, 2015, pp. 547–562.
[42] C. Dwork and G. N. Rothblum, “Concentrated differential privacy, ”arXiv preprint
arXiv:1603.01887, 2016.
[43] D. Boneh and M. K. Franklin, “Identity-Based Encryption from the Weil Pairing, ”
in CRYPTO, 2001, pp. 213–229.
[44] C. Chevalier, P. Fouque, D. Pointcheval, and S. Zimmer, “Optimal Randomness
Extraction from a Diffie-Hellman Element, ” inEUROCRYPT, 2009, pp. 572–589.
[45] X. Wang, A. J. Malozemoff, and J. Katz, “EMP-toolkit: Efficient MultiParty com-
putation toolkit, ” https://github.com/emp-toolkit, 2016.
[46] “Microsoft SEAL (release 4.1), ” https://github.com/Microsoft/SEAL, Jan. 2023,
microsoft Research, Redmond, WA.
[47] F. Boemer, S. Kim, G. Seifu, F. D. de Souza, V. Gopalet al., “Intel HEXL (release
1.2), ” https://github.com/intel/hexl, 2021.
[48] X. Jiang, X. Zhou, and J. Grossklags, “Comprehensive analysis of privacy leakage
in vertical federated learning during prediction. ”Proc. Priv. Enhancing Technol.,
vol. 2022, no. 2, pp. 263–281, 2022.
[49] P. Rindal and P. Schoppmann, “Vole-psi: Fast oprf and circuit-psi from vector-ole, ”
in Annual International Conference on the Theory and Applications of Crypto-
graphic Techniques. Springer, 2021, pp. 901–930.
A APPENDIX
A.1 Proofs
A.1.1 Proof of Lemma 5.
Proof. We denote𝐷′ 𝐴 and𝐷′ 𝐵 the sampled set in Algorithm 1
by P𝐴 and P𝐵, respectively. According to Algorithm 1, it is es-
tablished that both𝐷′ 𝐴 and𝐷′ 𝐵 are independent of both𝐴 and𝐵.
Consequently, it becomes evident that|e𝐴∩ e𝐵| =|𝐴∩𝐵|+ 𝑧 where
𝑧 =|𝐷′ 𝐴∩𝐷′ 𝐵|. To calculate Pr(𝑧 =𝑧′), we need to determine the
number of outcomes where the intersection size of𝐷′ 𝐴∩𝐷′ 𝐵 is𝑧
and then divide by the total number of possible outcomes. There
are 2𝜏 C𝜏 possible outcomes for both 𝐷′ 𝐴 and𝐷′ 𝐵 since there are
random subsets of a dummy set with 2𝜏 elements. Therefore, the
total number of outcomes is 2𝜏 C𝜏· 2𝜏 C𝜏 .
The number of outcomes for 𝐷′ 𝐵 alone is 2𝜏 C𝜏 . For any|𝐷′ 𝐴∩
𝐷′ 𝐵| =𝑧, it implies that there are𝑧 elements in𝐷′ 𝐵 belonging to𝐷′ 𝐴,
with𝜏 C𝑧 possible outcomes. Simultaneously, the remaining𝜏−𝑧
elements in𝐷′ 𝐵 must be randomly selected from𝐷\𝐷′ 𝐴, offering 𝜏 C𝜏−𝑧 possibilities. Consequently, we can compute the PMF of
𝑧 =|𝐷′ 𝐴∩𝐷′ 𝐵| as follows:
Pr(𝑧 =𝑧′) = 2𝜏 C𝜏·𝜏 C𝑧′·𝜏 C𝜏−𝑧′ 2𝜏 C𝜏· 2𝜏 C𝜏 =(𝜏 C𝑧′)2 2𝜏 C𝜏 .
□
A.1.2 Proof of Property 1.
Proof. Denote{0,...,𝜏 } as the support of 𝑧, the support of
M(𝐴) becomes:{|𝐴∩𝐵|,...,|𝐴∩𝐵|+ 𝜏}. Given the asymmetri-
cally distributed property, we have Pr(𝑧 = 𝜏−𝑜) = Pr(𝑧 = 𝑜),
∀𝑜𝑖𝑛[0, 1,...,𝜏 ]. Given the sensitivity of the operation of|𝐴∩𝐵|
is 1, The worst-case neighboring datasetM(𝐴′) has the support of
{|𝐴∩𝐵|+ 1,..., |𝐴∩𝐵|+𝜏+1}, and the mapping relationships of the
two neighboring datasets become Pr(M(𝐴) =𝑜) = Pr(M(𝐴′) =
𝑜+ 1) . Define𝑂 as the support of the output of the mechanism,𝑂+
as the subset of𝑂 corresponds to the criterion:
𝑂+ ={𝑜 : Pr(M(𝐴) =𝑜)− 𝑒𝜀 Pr(M(𝐴′) =𝑜)≥ 0}.
Simulator Sim𝐴
Evaluation: P𝐴 does not receive message in this stage, and thus
Sim𝐴 does nothing.
Update:
• Sim𝐴 samples ˜𝑏𝑗← G for 𝑗 = 1, 2,··· ,𝑛′.
• P𝐴← Sim𝐴 :{ ˜𝑏𝑗}𝑛′ 𝑗=1 as P𝐴’s received message in Step
(5) in ΠDH durPRF.
Figure 9: The simulator for P𝐴 in the ΠDH durPRF protocol .
Then, according to the definition of DP, the failure probability 𝛿
can be expressed as:
𝛿 =
∑︁
𝑜∈𝑂
max Pr(M(𝐴) =𝑜)− 𝑒𝜀 Pr(M(𝐴′) =𝑜), 0
=
∑︁
𝑜∈𝑂+
Pr(M(𝐴) =𝑜)− 𝑒𝜀 Pr(M(𝐴′) =𝑜
=
∑︁
𝑜∈𝑂+

1−𝑒𝜀 Pr(M(𝐴′) =𝑜) Pr(M(𝐴) =𝑜)  Pr(M(𝐴) =𝑜),
This shows how (8) is derived. For the first term in (8)
𝛿𝐴𝐴′(∞) =
∑︁
{𝑜| Pr(M(𝐴)=𝑜) >0,
Pr(M(𝐴′)=𝑜)=0}
Pr(M(𝐴) =𝑜)
=
|𝐴∩𝐵|∑︁
𝑜=|𝐴∩𝐵|
Pr(M(𝐴) =𝑜)
= Pr(M(𝐴) =|𝐴∩𝐵|)
(12)
For the other direction,
𝛿𝐴′𝐴(∞) =
∑︁
{𝑜| Pr(M(𝐴′)=𝑜) >0,
Pr(M(𝐴)=𝑜)=0}
Pr(M(𝐴′) =𝑜)
=
|𝐴∩𝐵|+𝜏∑︁
𝑜=|𝐴∩𝐵|+𝜏
Pr(M(𝐴) =𝑜)
= Pr(M(𝐴) =|𝐴∩𝐵|+ 𝜏)
= Pr(M(𝐴) =|𝐴∩𝐵|)
(13)
which means𝛿𝐴𝐴′(∞) =𝛿𝐴′𝐴(∞).
For the second part of (8), first, let 𝜸𝐴𝐴′(𝑜) and 𝜸𝐴′𝐴(𝑜) be:
𝜸𝐴𝐴′(𝑜) = ln
 Pr(M(𝐴) =𝑜)
Pr(M(𝐴′) =𝑜)

,
𝜸𝐴′𝐴(𝑜) = ln
 Pr(M(𝐴′) =𝑜)
Pr(M(𝐴) =𝑜)

Then, 𝜸𝐴𝐴′(𝑜) =−𝜸𝐴′𝐴(𝑜), and by the symmetric property,𝜸𝐴𝐴′(𝑜) =
𝜸𝐴′𝐴(𝜏+ 1−𝑜). Then, the second part𝛿(𝜸 >𝜖) for each term can
be expressed as:
𝛿(𝜸𝐴𝐴′ >𝜖) =
𝜸−1 𝐴𝐴′(𝜖)∑︁
𝑜=1
(1−𝑒𝜖−𝜸𝐴𝐴′(𝑜)) Pr(M(𝐴) =𝑜)

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
Simulator Sim𝐵
Evaluation:
• Sim𝐵 samples ˜𝑎𝑖← G for𝑖 = 1, 2,··· ,𝑛 .
• Sim𝐵→ P𝐵 :{ ˜𝑎𝑖}𝑛 𝑖=1 as P𝐵’s received messages in Step
(2).
Update:
• Sim𝐵← P𝐵 :{𝑏𝑗∈ G}𝑛′ 𝑗=1 where𝑏𝑗 s are chosen by P𝐵.
• Sim𝐵 → P𝐵 :{𝑏𝑟 𝑗}𝑛′ 𝑗=1 using random 𝑟 ← Z𝑞 as P𝐵’s
received messages in Step (7).
Figure 10: The simulator for P𝐵 in the ΠDH durPRF protocol.
and
𝛿(𝜸𝐴′𝐴 >𝜖)
=
𝜏∑︁
𝑜=𝜸−1 𝐴′𝐴(𝜖)
(1−𝑒𝜖−𝜸𝐴′𝐴(𝑜)) Pr(M(𝐴′) =𝑜)
=
𝜸−1 𝐴𝐴′(𝜖)∑︁
𝑜=1
(1−𝑒𝜖−𝜸𝐴𝐴′(𝑜)) Pr(M(𝐴) =𝑜).
Therefore,𝛿(𝜸𝐴𝐴′ >𝜖) =𝛿(𝜸𝐴′𝐴 >𝜖). □
A.1.3 Proof of Property 3.
Proof. 𝑊 is lower bounded by the maximum leakage after𝑘-
fold convolution. From(7), the maximum leakage of the mechanism
can be expressed as
2 ln

max
𝑧∈[ 0,𝜏−1]
𝑧+ 1
𝜏−𝑧

= 2 ln(𝜏)
The length of the PLD is:
2 ln

max
𝑧∈[ 0,𝜏−1]
𝑧+ 1
𝜏−𝑧

− 2 ln

min
𝑧∈[ 0,𝜏−1]
𝑧+ 1
𝜏−𝑧

= 4 ln𝜏
Then, the maximum leakage after𝑘-fold composition becomes:
2 ln(𝜏)+ 4(𝑘− 1) ln(𝜏) =(4𝑘− 2) ln(𝜏)
This completes the proof. □
A.1.4 Security Proof for ΠDDH durPRF. This section contains the full
version of the security proof of ΠDDH durPRF.
Let View
ΠDDH durPRF
𝜎,𝜆 ({𝑥𝑖}𝑛 𝑖=1,∅) be a random variable representing
the view of 𝑃𝜎 (𝜎 = 𝐴,𝐵 ) in real protocol execution, where the
random variable ranges over the internal randomness of all parties,
and the randomness in the setup phase (including that of the Ran-
dom Oracle). The the view of a party consists of its internal state
(including its input and randomness) and all messages this party
received from the other party. The messages sent by this party do
not need to be part of the view because they can be determined
using the other elements of its view.
View
ΠDH durPRF
𝐴,𝜆 ({𝑥𝑖}𝑛 𝑖=1) =(∅,{H(𝑥𝑗)𝑘′ 𝐵}𝑗∈𝑍)
View
ΠDH durPRF
𝐵,𝜆 ({𝑥𝑖}𝑛 𝑖=1) =({H(𝑥𝑖)𝑘𝐴}𝑛 𝑖=1,{H(𝑥𝑗)𝑘′ 𝐴}𝑗∈𝑍)
We now show that P𝐴’s view can be simulated given only P𝐴’s
input but notP𝐵’s input. The simulatorSim𝐴 is given in Figure 9. We
argue that{H(𝑥𝑗)𝑘′ 𝐵}𝑗∈𝑍 is indistinguishable from random group
elements in G assuming the hardness of DDH under the random
oracle model. Specifically, the existence of an efficient distinguisher
D that outputs 0 when presented with ˜𝑏1,··· , ˜𝑏𝑛′ and outputs 1
when it observes{H(𝑥𝑗)𝑘′ 𝐵}𝑗∈𝑍 allows us to construct a simulator
Sim that violates the DDH assumption, as follows.
Upon receiving a DDH challenge (𝑔,𝑔𝑥,𝑔𝑦,𝑔𝑧), Sim does the
following:
• Selects random values𝑑1,··· ,𝑑𝑛′−2 from Z𝑞.
• Answers queries for H as follows: H(𝑥𝑗1) =𝑔, H(𝑥𝑗2) =𝑔𝑥 ,
and H(𝑥𝑗𝑘) =𝑔𝑑𝑘−2 for𝑘 > 2 for consistency.
• Sends{𝑔𝑦,𝑔𝑧,(𝑔𝑦)𝑑1,··· ,(𝑔𝑦)𝑑𝑛′−2} toD.
If(𝑔,𝑔𝑥,𝑔𝑦,𝑔𝑧) is a Diffie-Hellman tuple, i.e.,𝑧 =𝑥𝑦, then
{𝑔𝑦,𝑔𝑧,(𝑔𝑦)𝑑1,··· ,(𝑔𝑦)𝑑𝑛′−2}
={𝑔𝑦,(𝑔𝑥)𝑦,(𝑔𝑑1)𝑦,··· ,(𝑔𝑑𝑛′−2)𝑦},
which is distributed like{H(𝑥𝑗1)𝑘′ 𝐵,··· , H(𝑥𝑗𝑛′)𝑘′ 𝐵}. Thus,D must
return 1. On the other hand, when𝑧 ≠𝑥𝑦, the term𝑔𝑧 ≠ H(𝑥𝑗2)𝑦.
As a result,Sim can useD’s output to respond to the DDH challenge
correctly.
The simulator Sim𝐵 is given in Figure 10. For the evaluation part,
the values in{H(𝑥𝑖)𝑘𝐴} are indistinguishable from random group
elements under the DDH assumption. Similarly, for the update part,
the values in{H(𝑥𝑗)𝑘′ 𝐴} are also indistinguishable from random
group elements in G.
B FULL PROTOCOL WITH MORE
IDENTIFIERS
Figure 12 depicts the full version of our waterfall matching protocol
that handles𝑚≥ 2 identifiers.
Complexities. Let the databases sizes being𝑛𝐴 =|ID𝑏 𝐴| and𝑛𝐵 =
|ID𝑏 𝐵|, and|𝐽𝑏| being the intersection size on the 𝑏-th identifier.
When instantiatingFdurPRF as the DDH-based construction, the
computation of Figure 12 includes𝑂(2𝑚(𝑛𝐴+𝑛𝐴)− 2˝𝑚−1 𝑏=1 |𝐽𝑏|)
group operations, and 𝑂(𝑛𝐵+ ˝𝑚 𝑏=1|𝐽𝑏|) AHE operations. The
communication includes𝑂(𝑚(𝑛𝐴+𝑛𝐵)+ 𝑛𝐵− ˝𝑚−1 𝑏=1 |𝐽𝑏|) group
elements, and𝑂(𝑛𝐵) AHE ciphertexts.

Figure 11: An illustration of the DDH-based Waterfall Matching.

PrivacyGo: Privacy-Preserving Ad Measurement with Multidimensional Intersection
Private Waterfall Matching and Sum Protocol Πwfm
1 : P𝐴 : identifiers ID1 𝐴, ID2 𝐴,··· , ID𝑚 𝐴 P𝐵 : identifiers ID1 𝐵, ID2 𝐵, ID𝑚 𝐵, and payloads𝑇
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Stage-1: Setups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2 : 𝑘 1 𝐴,𝑘𝑏 𝐴, ˆ𝑘𝑏 𝐴 $ ← −Z𝑞 for𝑏 = 2, 3,··· ,𝑚 𝑘 1 𝐵,𝑘𝑏 𝐵, ˆ𝑘𝑏 𝐵 $ ← −Z𝑞 for𝑏 = 2, 3,··· ,𝑚
3 : FdurPRF.init(sid𝑏,𝑘𝑏 𝐴) for𝑏 = 1,··· ,𝑚 FdurPRF.init(sid𝑏,𝑘𝑏 𝐵) for𝑏 = 1,··· ,𝑚
4 : FdurPRF.init( ˆsid𝑏, ˆ𝑘𝑏 𝐴) for𝑏 = 2,··· ,𝑚 FdurPRF.init( ˆsid𝑏, ˆ𝑘𝑏 𝐵) for𝑏 = 2,··· ,𝑚
5 : (sk, pk)←HE .Gen(1𝜆)
6 : pk,𝐶 𝐶 ={HE.Encpk(𝑇[𝑗])}|𝑇| 𝑗 =1
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Stage-2: PRF on all identifiers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7 : FdurPRF.Send(sid𝑏, ID𝑏 𝐴) for𝑏 = 1,··· ,𝑚 Tag𝑏 𝐴←F durPRF.Recv(sid𝑏) for𝑏 = 1,··· ,𝑚
8 : Tag𝑏 𝐵←F durPRF.Recv(sid𝑏) for𝑏 = 1,··· ,𝑚 FdurPRF.Send(sid𝑏, ID𝑏 𝐵) for𝑏 = 1,··· ,𝑚
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Stage-3: Matching on the first identifier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
9 : gTag 1 𝐴 in shuffled order
10 : gTag 1 𝐵 in shuffled order
11 : Matches:𝐽 1 𝐵←{ 𝑗 : Tag1 𝐵[𝑗]∈ gTag 1 𝐴} 𝐽 1 𝐴←{ 𝑗 : Tag1 𝐴[𝑗]∈ gTag 1 𝐵}
12 : Mismatches:𝐷 1 𝐵←{ 1, 2,··· ,|Tag1 𝐵|}\ 𝐽 1 𝐵 𝐷 1 𝐴←{ 1, 2,··· ,|Tag1 𝐴|}\ 𝐽 1 𝐴
13 : Book-keep:𝜎 1 𝐵[𝑗]← 𝐷 1 𝐵[𝑗] for 1≤ 𝑗≤| 𝐷 1 𝐵| 𝜎 1 𝐴[𝑗]← 𝐷 1 𝐴[𝑗] for 1≤ 𝑗≤| 𝐷 1 𝐴|
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Stage-4: Key-update then matching on the𝑏-th identifier (𝑏 = 2,··· ,𝑚) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14 : Keep the unmatched records rTag𝑏 𝐵←{ Tag𝑏 𝐵[𝑖]}𝑖∈𝐷𝑏−1 𝐵 rTag𝑏 𝐴←{ Tag𝑏 𝐴[𝑖]}𝑖∈𝐷𝑏−1 𝐴
15 : (Skip this if𝑏 =𝑚) rTag𝑏 𝐵←F durPRF.Update(sid𝑏, ˆsid𝑏, rTag𝑏 𝐵) (Skip this if𝑏 =𝑚)FdurPRF.Assit(sid𝑏, ˆsid𝑏)
16 : FdurPRF.Assit(sid𝑏, ˆsid𝑏) rTag𝑏 𝐴←F durPRF.Update(sid𝑏, ˆsid𝑏, rTag𝑏 𝐴)
17 : grTag 𝑏 𝐴 in shuffled order
18 : (Skip this line if𝑏 =𝑚) grTag 𝑏 𝐵 in shuffled order
19 : Matches:𝐽𝑏 𝐵←{ 𝜎𝑏−1 𝐵 [𝑗] : rTag𝑏 𝐵[𝑗]∈ grTag 𝑏 𝐴} 𝐽𝑏 𝐴←{ 𝜎𝑏−1 𝐴 [𝑗] : rTag𝑏 𝐴[𝑗]∈ grTag 𝑏 𝐵}
20 : Mismatches:𝐷𝑏 𝐵←𝐷𝑏−1 𝐵 \𝐽𝑏 𝐵 𝐷𝑏 𝐴←𝐷𝑏−1 𝐴 \𝐽𝑏 𝐴
21 : Book-keep:𝜎𝑏 𝐵[𝑗]← 𝐷𝑏 𝐵[𝑗] for 1≤ 𝑗≤| 𝐷𝑏 𝐵| 𝜎𝑏 𝐴[𝑗]← 𝐷𝑏 𝐴[𝑗] for 1≤ 𝑗≤| 𝐷𝑏 𝐴|
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Final stage: aggregation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22 : Sum ct←HE .Sum({ e𝐶[𝑗]}𝑗∈𝐽 1 𝐵∪···∪𝐽𝑏 𝐵 ) ct′←HE .Refresh(ct) OutputHE.Decsk(ct′).
Figure 12: (Full version) Our private waterfall matching protocol under FdurPRF-hybrid model.HE is an AHE scheme.
