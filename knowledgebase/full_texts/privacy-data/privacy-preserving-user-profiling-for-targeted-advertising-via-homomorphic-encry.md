---
title: Privacy-Preserving User Profiling for Targeted Advertising via Homomorphic Encryption and Secure
  Multiparty Computation
url: https://doi.org/10.21203/rs.3.rs-10767223/v1
category: privacy-data
subcategory: empirical
date: 2026-09
venue: Research Square
authors:
- Wenzeng Cui
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10767223/latest.pdf
pages: 27
chars: 69204
fetched_at: '2026-11-08T17:47:23+00:00'
kb_version: 1
---

# Privacy-Preserving User Profiling for Targeted Advertising via Homomorphic Encryption and Secure Multiparty Computation

Privacy-Preserving User Proﬁling for Targeted
Advertising via Homomorphic Encryption and
Secure Multiparty Computation
Wenzeng Cui 
Sias University
Article
Keywords: targeted advertising, user proﬁling, homomorphic encryption, secure multiparty computation,
privacy-preserving recommendation, secure computation
Posted Date: September 22nd, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10767223/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

Privacy-Preserving User Proﬁling for Targeted
Advertising via Homomorphic Encryption and
Secure Multiparty Computation
Wenzeng Cui1*
1*School of Journalism and Communication, Sias University,
Zhengzhou, 451150, Henan, China.
Corresponding author(s). E-mail(s): CUI19800606@163.com;
Abstract
Targeted advertising depends on proﬁles assembled from behaviou ral signals
distributed across platforms. Centralising these signals can im prove proﬁle
coverage but exposes ﬁne-grained interests and activity patte rns to parties
that do not require the underlying records. This study proposes H2P roﬁle, a
conversion-minimising hybrid framework that assigns packed lin ear aggregation
to approximate homomorphic encryption and assigns clipping, n ormalisation,
thresholding, and Top-K selection to additive-sharing-base d secure multiparty
computation. The framework adopts a polynomial-domain CKKS-t o-MPC con-
version rather than an insecure encoded slot-wise mask and plac es one conversion
boundary between the two stages. Its conﬁdentiality claim is limited to a static
semi-honest model with two non-colluding servers; identity a lignment, malicious
inputs, access-pattern hiding, and repeated-output abuse are outside the cryp-
tographic guarantee. The evaluation uses TencentGR-1M, KuaiS AR-small, and
KuaiRec to measure numerical ﬁdelity, downstream utility, runt ime, communi-
cation, scalability, and semantic leakage under four output policies. Under the
common evaluation conﬁguration with 128 proﬁle dimensions, t wo holders, 64
proﬁles per batch, and a 1-Gbps LAN, H2Proﬁle retains approximat ely 98.5%
of plaintext utility, achieves 93.8% mean Top-10 overlap, req uires 0.84 s and
34.7 MB per batch, and reduces latency by 68.1% relative to FHE, 53.6% rela-
tive to MPC, and 25.0% relative to BLB. In the KuaiRec output-l eakage audit,
its attribute-inference AUC is 0.604, compared with 0.628 for FHE , 0.621 for
MPC, and 0.613 for BLB. H2Proﬁle is an application-level protoc ol design and
evaluation framework, not a new homomorphic-encryption or share- conversion
primitive.
1

Keywords: targeted advertising, user proﬁling, homomorphic encrypt ion, secure
multiparty computation, privacy-preserving recommendat ion, secure computation
1 Introduction
Targeted advertising is driven by a simple informational asymmetry: a platform can
select a more relevant advertisement when it has a suﬃciently accu rate representa-
tion of the user’s current interests, yet the behavioural eviden ce needed to construct
that representation is commonly distributed across organisations. A pu blisher observes
page visits and ad impressions, a commerce service records product i nteractions, an
advertising platform records clicks and conversions, and a data provi der may hold
contextual or device attributes. Combining these sources can impro ve coverage of a
user’s interests, but direct centralisation also creates an attract ive record of individual
behaviour. Recent evidence that only a few frequently visited d omains can form highly
distinctive behavioural ﬁngerprints reinforces the re-identi ﬁcation risk of apparently
ordinary browsing traces [ 1]. The problem is therefore not only how to model interest,
but how to compute a useful proﬁle while limiting which party can i nspect the events
from which that proﬁle was derived.
Early privacy-preserving advertising systems demonstrated that behavioural tar-
geting need not require unrestricted server-side tracking. Adnos tic moved proﬁling
and ad selection into the browser and introduced cryptographic accoun ting mecha-
nisms [ 2]. Privad separated the advertising broker from an anonymising dealer an d
showed how privacy-oriented advertising could be reconciled wit h practical deploy-
ment constraints [ 3]. These systems established the architectural possibility of pr ivate
targeting, but their trust assumptions and client-side designs do n ot directly address
collaborative proﬁling over multiple contemporary data holders. More r ecent work
on browser-based advertising has also shown that a mechanism descri bed as privacy-
preserving may retain exploitable tracking, leakage, or manipulation su rfaces when its
complete implementation is considered [ 4]. Privacy claims must therefore be tied to a
precise threat model, explicit outputs, and reproducible evid ence rather than to the
use of a privacy technology in isolation.
Federated learning and diﬀerential privacy provide another route to distributed
personalisation. Keeping behavioural records on user devices reduc es direct central col-
lection, while perturbing updates can limit the contribution of an i ndividual record. For
example, privacy-preserving news recommendation has combined fed erated optimisa-
tion with local diﬀerential privacy to avoid central storage of click hi stories [5]. Recent
federated recommender studies have extended this direction to privacy-sensitive cross-
domain and cold-start settings [ 6, 7], while complementary work has examined tighter
diﬀerential-privacy accounting and homomorphically protected collab orative updates
[8, 9]. This family of methods is valuable when the goal is to learn a global mode l. It
does not, by itself, solve every collaborative proﬁling problem: int ermediate updates
may still reveal information, privacy noise changes model utility, and secure cross-party
feature interaction or exact proﬁle construction may require addition al protocols. The
2

present study instead focuses on cryptographic computation of an inter est proﬁle from
vertically distributed inputs, with no intentional noise added t o the proﬁle arithmetic.
Homomorphic encryption (HE) and secure multiparty computation (MPC) oﬀe r
complementary capabilities. HE enables arithmetic over ciphertex ts and is particularly
eﬃcient when many additions and multiplications can be packed into ve ctorised opera-
tions [10, 11]. MPC represents values as shares and supports general joint computati on
without revealing the underlying values, but the cost of interacti on depends strongly
on the circuit and network. Mixed-protocol systems have repeatedl y shown that arith-
metic, Boolean, and garbled-circuit representations should be sele cted according to
the operation rather than forcing an entire workload into one representat ion [ 12–17].
In secure inference, systems such as GAZELLE, Delphi, and Cheetah as sign linear
layers to HE-compatible arithmetic and nonlinear operations to interac tive protocols
[14–16]. User proﬁling has a related but distinct structure: high-dimen sional interest
counts are predominantly additive, whereas clipping, normalisation, t hresholding, and
Top-K release require comparisons or division.
We therefore propose H2Proﬁle, a hybrid framework for privacy-preserv ing cross-
platform user proﬁling. Each data holder ﬁrst maps its local behavioural history into a
ﬁxed-dimensional interest vector using a public, frozen item-t o-proﬁle map. The vec-
tors are encrypted and aggregated in batches under the Cheon-Kim-Kim-S ong (CKKS)
approximate HE scheme [ 11]. Instead of repeatedly switching representations, the
framework performs one masked conversion from the aggregated ciphertext t o additive
shares. MPC is then used to enforce proﬁle bounds, normalise the vec tor, select the
highest-ranked interests, and optionally compute an advertisement- matching score.
The full vector can remain secret-shared; only a policy-deﬁned Top- K set, selected
advertisement, or encrypted score is released.
The study addresses four research questions. RQ1 asks whether the secure pro-
ﬁle preserves the utility of a plaintext centralised proﬁle for ne xt-interaction and
advertisement-ranking tasks. RQ2 asks whether the hybrid allocat ion reduces online
latency and communication relative to FHE and MPC implementations. RQ3 asks
which components—batched aggregation, single-boundary conversion, secur e normal-
isation, and selective release—account for the observed trade-oﬀs. RQ4 asks how
the protocol responds to changes in proﬁle dimension, network conditi ons, numerical
precision, and output-release policy.
The main contributions are:
• We formalise privacy-preserving advertising proﬁles as a secure c ross-party aggrega-
tion and selective-release problem, explicitly separating input conﬁdentiality from
semantic leakage through authorised outputs.
• We develop an application-speciﬁc, single-boundary execution sched ule in which
packed CKKS handles batched linear aggregation and additive-sharing-based MPC
handles clipping, normalisation, Top- k selection, and policy enforcement.
• We instantiate a published polynomial-domain CKKS-to-MPC conversion within
this proﬁling workﬂow and specify its threat model, leakage function , numeri-
cal conditions, and failure boundaries; the work does not claim a new con version
primitive.
3

The remainder of the paper is organised as follows. Section 2 reviews privacy-
preserving advertising, distributed personalisation, HE, MPC, and hybrid protocols.
Section 3 deﬁnes the H2Proﬁle functionality, trust model, operator allocation, c on-
version boundary, and release policies. Section 4 presents the datasets, baselines,
utility and system comparisons, ablations, numerical checks, and scal ability analysis.
Section 5 discusses the resulting utility–cost–leakage trade-oﬀ and the limit s of the
stated security model, and Section 6 concludes the study.
2 Related Work
The literature relevant to H2Proﬁle comprises three connected str ands: privacy-
preserving advertising and personalisation, homomorphic computation o ver
behavioural representations, and mixed-protocol secure computation . The central
distinction is whether a system protects data collection, model t raining, proﬁle
construction, advertisement selection, accounting, or some combinati on of these stages.
2.1 Privacy-preserving advertising and user proﬁling
Online behavioural advertising traditionally infers user intere sts from interactions
observed across websites or applications. Adnostic challenged the assum ption that
behavioural targeting necessarily requires the advertising netw ork to possess the
browsing proﬁle. It retained the proﬁle in the browser, selecte d advertisements locally,
and used cryptographic techniques to support billing [ 2]. Privad similarly pursued a
deployable advertising architecture but introduced an intermediary that separated user
identity and behavioural information from the advertising broker [ 3]. Both systems
remain important because they make the trust boundary visible: priv acy is achieved
not merely by encrypting a database but by changing which component obs erves which
signal.
Contemporary advertising systems add real-time auctions, large candid ate pools,
multi-device signals, and learned user representations. These add itions create pri-
vacy surfaces beyond raw log collection. Empirical analysis of the Prote cted
Audience/FLEDGE ecosystem found tracking, cross-site leakage, disrup tion, and
proﬁle-pollution attacks despite the mechanism’s privacy-oriente d design [ 4]. Recent
privacy-preserving advertising measurement also treats cross-or ganisation matching
and intersection leakage as explicit protocol concerns rather than impl ementation
details [ 18]. The implication for secure proﬁling is that cryptographic conﬁdent iality
of the inputs is necessary but insuﬃcient. The released proﬁle, s elected advertisement,
query frequency, intersection size, and access pattern may each r eveal information.
H2Proﬁle consequently treats the output policy as part of the protocol rath er than as
an application detail.
Distributed recommendation oﬀers adjacent evidence. Qi et al. kept user behaviour
on devices and protected federated updates with local diﬀerential p rivacy [ 5]. Fed-
SCOPE addresses privacy-sensitive cross-domain sequential recom mendation, while
CRAFT combines federated training with attention for cold-start recom mendation
[6, 7]. At the privacy-mechanism level, recent studies have invest igated diﬀerential-
privacy accounting for federated learning and partially homomorphic pr otection of
4

collaborative model updates [ 8, 9]. These approaches reduce central retention and
support population-level model learning. However, federated learni ng, diﬀerential pri-
vacy, and secure computation answer diﬀerent questions. Diﬀerenti al privacy limits
how much a released statistic changes when an individual’s record is modiﬁed; HE and
MPC aim to compute a speciﬁed function without revealing private in puts beyond
that function’s output. H2Proﬁle does not claim to replace diﬀerential privacy. Instead,
it addresses cases in which several organisations need an exact or high-pr ecision
aggregate for one authorised user while remaining unable to inspect one anot her’s
component histories. Diﬀerential privacy can be added to the release layer when
population-level protection is required.
2.2 Homomorphic encryption for protected proﬁle
computation
Fully homomorphic encryption established that arbitrary circuits c ould, in princi-
ple, be evaluated over encrypted data [ 10]. Practical schemes diﬀer in the supported
plaintext space, depth, accuracy, and cost. CKKS is suited to approx imate real- or
complex-number arithmetic and supports packed operations over mult iple vector slots
[11]. This makes it a natural candidate for ﬁxed-dimensional interest ve ctors, weighted
sums, linear transformations, and dot products. The approximation inh erent in CKKS
also imposes an evaluation obligation: the secure proﬁle must be compared w ith the
plaintext computation so that encoding, rescaling, and ﬁxed precision do not silently
alter rankings.
HE is less attractive for data-dependent branching, exact comparison, and Top-
K selection. These operations can be represented by polynomial approx imations or
Boolean circuits, but high-degree approximations increase multipl icative depth and
ciphertext cost. An HE-only proﬁle pipeline may therefore be eﬃcie nt for aggregation
yet expensive for clipping negative values, dividing by a secret sum, or selecting the
largest categories. Bootstrapping could refresh ciphertexts, but i t is not required by the
proposed shallow linear stage and would add avoidable cost. H2Proﬁle conﬁnes C KKS
to the operations that match its strengths and converts only once before n onlinear
processing.
2.3 Secure multiparty computation and hybrid protocols
Secure computation enables parties to evaluate a function on private in puts while
revealing only the prescribed output. Yao’s foundational work establis hed secure two-
party computation as a general cryptographic objective [ 12]. Modern frameworks
optimise diﬀerent representations for diﬀerent operations. ABY comb ines arithmetic
sharing, Boolean sharing, and Yao sharing and provides explicit convers ions between
them [13]. SecureML uses a two-server model and MPC-friendly arithmeti c for privacy-
preserving machine learning [ 14]. These systems show that protocol selection is an
operator-level engineering decision.
Hybrid secure-inference systems provide the closest computati onal analogy to
H2Proﬁle. GAZELLE combines packed HE for linear algebra with garbled circuit s for
nonlinear layers and develops conversion protocols between the repr esentations [ 15].
5

Delphi jointly optimises a neural architecture and its hybrid cry ptographic execution
plan [ 16]. Cheetah further reduces the cost of linear and nonlinear secure in ference
through specialised HE and sharing protocols [ 17]. More recent systems continue this
operator-aware direction: BumbleBee and SHAFT develop communication-e ﬃcient
mixed protocols for nonlinear Transformer operations, while Shechi c ompiles dis-
tributed programs to multiparty homomorphic computation [ 19–21]. SMASH extends
hybrid MPC to a malicious setting, and SING studies learned assignmen t of subcom-
putations to MPC protocols [ 22, 23]. BLB is particularly relevant because it shows
that directly encoding a uniformly sampled slot mask does not in gene ral hide a
CKKS plaintext and provides a secure polynomial-domain CKKS–MPC conv ersion
[24]. H2Proﬁle adopts that conversion pattern rather than presenting slot-w ise mask-
ing as a new or proven primitive. Multiparty HE has also been develope d as a basis
for collaborative computation when the number of parties is large [ 25].
The proposed study diﬀers in its object and output. It does not protec t infer-
ence through a deep proprietary model. It constructs an interpretab le category-level
user proﬁle from event summaries owned by multiple platforms and th en enforces
a selective-release policy. The computational graph is shallower, aggre gation domi-
nates the linear stage, and Top-K interest disclosure is part of the pri vacy boundary.
The closest-work review must nevertheless determine whether the single-boundary
conversion and proﬁle-speciﬁc operator allocation provide suﬃcient n ovelty beyond
established mixed-protocol techniques.
3 Proposed H2Proﬁle Framework
3.1 Problem formulation
Let there be m data holders P1, . . . , Pm and a set of users U . For a user u, party Pj
holds a local event history Hu,j. An event e contains a timestamp, an action type
such as exposure or click, and an item or advertisement identiﬁer i(e). Each dataset
D has a public, frozen item-to-proﬁle map ϕD(i) ∈ [0, 1]K. The map is one-hot
when the dataset publishes a single category, normalised multi-hot wh en it publishes
several tags, and a training-only cluster assignment when no semantic t axonomy is dis-
closed. Cluster-derived coordinates are called latent interest b ins rather than semantic
categories. Raw events remain at their originating party. The cryptograp hic function-
ality begins only after authorised user alignment. The present work ne ither designs
nor benchmarks private set intersection or identity resolution: ex periments reuse the
pseudonymous common identiﬁers already present in each public datase t, and deploy-
ment claims must account separately for the legality and leakage of the alignm ent
step.
Each party maps its local history to an interest contribution xu,j ∈ RK. For
category k,
xu,j,k =
∑
e∈Hu,j
ϕD,k(i(e)) w(a(e)) exp(−γ age(e)) . (1)
Here, ϕD,k(i) is the public contribution of item i to proﬁle coordinate k, w assigns
public non-negative weights to behavioural actions, γ controls temporal decay, and
6

age(e) is measured relative to a public proﬁle-construction time tu. The active coor-
dinate count KD may be smaller than the protocol capacity K; unused coordinates
are zero-padded and never interpreted as categories. The mapping manif est, action
vocabulary, w, γ, per-party weights αj, taxonomy version, deduplication rule, and all
clipping bounds are ﬁxed using training and validation data before the test interval is
opened. The default speciﬁcation uses αj = 1 unless cross-party calibration is selected
on validation data. The secure functionality computes su = ∑m j=1 αjxu,j, applies a
bounded normalisation function g, and derives zu = g(su). Depending on policy, the
output is a secret-shared full vector, a Top-K coordinate set Tu, or an advertisement
decision derived from zu. The desired functionality is therefore
F
(
{Hu,j}m j=1,A ) −→{ Tu, a∗ u, authorised statistics}. (2)
whereA denotes candidate advertisement features. The function should re veal no
additional raw event or local vector under the stated threat model.
The formulation distinguishes proﬁle conﬁdentiality from output pri vacy. Four
release policies are evaluated: R0 releases only a secret-shared proﬁ le handle; R1
releases the selected advertisement identiﬁer; R2 releases Top -K category identi-
ﬁers; and R3 releases a quantised proﬁle. No unquantised full vector is a default
output. Repeated queries may reveal changes even when every query is securely com-
puted. Query budgets, a minimum update interval, minimum suppor t thresholds, and
purpose-bound access control are therefore deployment controls, not c onsequences of
HE or MPC.
3.2 System and threat model
The system contains behavioural data holders, an HE computation server SHE, an
MPC/key service SMPC, and an authorised advertising decision service. During setup,
SMPC holds the CKKS secret key and distributes the corresponding publ ic and eval-
uation keys; SHE never receives the secret key. Data holders send ciphertexts on ly
to SHE over authenticated conﬁdential channels. SMPC receives only the protocol-
deﬁned masked aggregate, not the data holders’ input ciphertexts. The two servers
retain additive shares during post-processing, and the decision se rvice receives only
the policy-approved output.
Figure 1 summarises this workﬂow. The three behavioural examples are altern a-
tive dataset-speciﬁc instantiations evaluated separately, rather th an inputs combined
across TencentGR-1M, KuaiSAR-small, and KuaiRec. In the graphic, “Top-K” denotes
the conventional Top- k operation, whereas uppercase K in the equations is the pro-
ﬁle dimension. Padlocks on green blocks indicate protected, unrec onstructed shares
rather than additional ciphertexts. Identity alignment and candidate retrieval precede
the depicted functionality and remain outside the cryptographic guaran tee.
The initial protocol assumes static, semi-honest adversaries and non- collusion
between SHE and SMPC. A semi-honest party follows the protocol but attempts to
infer information from its view. At most one computation server is corru pted; cor-
ruption of a server together with any data holder is excluded. The dec ision service
is an output recipient rather than a computation party and is trusted to enforce the
declared release policy. Communication channels are authenticated and encrypted,
7

Fig. 1 H2Proﬁle workﬂow from local behavioural proﬁles through packed CKKS
aggregation and a single HE-to-MPC conversion to MPC post-processing and
policy-controlled release.
public parameters are agreed before execution, and malformed cipherte xts are outside
the initial model. The data holders may observe their own inputs an d the authorised
result but not other holders’ contributions.
The model does not provide malicious security, robustness against s erver collusion,
traﬃc-analysis resistance, private identity alignment, or protecti on against a decision
service that abuses repeated authorised outputs. In particular, the semi-honest model
prevents SHE from submitting arbitrary ciphertexts to the key service; a mali cious
deployment would need ciphertext authentication, session bindi ng, and a veriﬁable
decryption/conversion interface to avoid a decryption-oracle attack. Proofs of correct
input formation or malicious-secure MPC are also required against poisone d or out-
of-range inputs.
3.3 Local proﬁle construction and encrypted aggregation
Each data holder applies the same public item-to-proﬁle map and event- weighting
speciﬁcation. Local preprocessing includes timestamp validation, proﬁle-coordinate
mapping, optional per-event deduplication, and clipping each coordin ate contribu-
tion to a public bound Blocal. Clipping before encryption prevents a single platform
from dominating the aggregate and keeps encoded values within the preci sion
range. Because local clipping is performed by the data holder, malici ously chosen
contributions remain possible in the present semi-honest model.
The K-dimensional vector is encoded into CKKS slots. When K is smaller than
the slot capacity, multiple users may be packed into one ciphertex t subject to rotation
and layout constraints; otherwise, a proﬁle is divided across several ciphertexts. Party
Pj sends Cj = Enc( xu,j) to SHE. The user index is suppressed in Cj only to keep
Fig. 1 legible. The server computes the aggregate ciphertext Cagg as
8

Cagg = Enc(su) =
m∑
j=1
αjCj. (3)
using ciphertext addition and plaintext–ciphertext multiplicat ion by public party
weights. If a public linear projection W is required to map dataset-speciﬁc categories
to a shared advertising taxonomy, SHE also evaluates Enc( Wsu). No comparison,
data-dependent branch, or exact division is performed in this stage.
The aggregation stage has shallow multiplicative depth. The common experi mental
conﬁguration uses polynomial modulus degree 8192, initial scale 2 40, batched packing,
and a target of at least 128-bit classical security, as summarised in Section 4.1.3.
3.4 Masked HE-to-MPC conversion
After aggregation, H2Proﬁle invokes a secure CKKS-to-MPC conversion once. I t is
important that the mask is sampled in the CKKS plaintext polynomial rin g, not
sampled as a slot vector and then encoded. The latter construction can p roduce a
narrow coeﬃcient distribution and fail to hide high-order informati on [ 24]. Let Rq =
Zq[X]/(X N +1), let ˆsu = Encode ∆(su)∈ Rq, and let the aggregate ciphertext decrypt
approximately to ˆsu + ˆe modulo q. The adopted conversion consists of the following
steps.
1. SHE samples a fresh polynomial ˆr← Rq uniformly, adds it as a plaintext to the
aggregate ciphertext, sends the session-bound masked ciphertext to SMPC, and
retains coeﬃcient share −ˆr mod q.
2. SMPC decrypts only this masked ciphertext and obtains coeﬃcient share ˆsu +
ˆe + ˆr mod q. Uniform polynomial masking makes this coeﬃcient-domain value
independent of ˆsu in the semi-honest model.
3. The servers run the selected ﬁeld-to-ring protocol to convert t heir coeﬃcient shares
from modulus q to shares over Z2ℓ′ , without reconstructing the polynomial. They
then apply the public linear CKKS decoding transform locally to th eir shares.
4. After decoding, the servers use a documented probabilistic or ex act truncation
to obtain ﬁxed-point shares [ ~su] over Z2ℓ with scale 2 f . The expanded width ℓ′,
fractional precision f , truncation security parameter κ, and signed representative
interval are chosen so that overﬂow probability and truncation failure probability
meet the declared target.
For notation, write [ ~su] = ( s(1) u , s(2) u ), where server 1 and server 2 hold one additive
share each and s(1) u + s(2) u = ~su (mod 2 ℓ). Figure 1 abbreviates these two share vectors
as s1 and s2; neither share alone is a plaintext proﬁle.
The implementation follows the polynomial-domain conversion pattern of BLB
Algorithm 1 [ 24], including ﬁeld-to-ring conversion and secure truncation. It re cords
the modulus, ﬁxed-point widths, valid input bound, reconstruct ion error, and wrap-
around count. Masks are generated by a cryptographic pseudorandom generator,
bound to unique sessions, and never reused.
The single conversion boundary is an execution schedule, not a new conv ersion
primitive. All nonlinear operations are grouped into the following MPC phase; the
9

repeated-conversion ablation repeats the same secure conversion and ne ver uses the
insecure encoded-slot mask.
3.5 Secure normalisation and selective proﬁle release
The two servers ﬁrst interpret each ℓ-bit share as a signed ﬁxed-point value, securely
clip it to the public interval [0 , Bagg], and calculate a normalised interest vector. The
protocol ﬁxes the following deﬁnition before evaluation:
zu,k = max(su,k, 0) ϵ + ∑K ℓ=1 max(su,ℓ, 0) . (4)
where ϵ > 0 is a public constant that prevents division by zero. If the clippe d
sum is zero, the protocol returns the all-zero proﬁle and an “insuﬃcie nt support” ﬂag.
Otherwise, the denominator is range-reduced and its reciprocal is c omputed over Z264
with a ﬁxed-point Newton–Raphson protocol [ 26]. An 8-bit oblivious lookup supplies
the initial estimate, followed by three iterations with 16 fractional bits and secure
truncation. The admissible denominator range is ﬁxed from the public c lipping bound,
and the result is checked against the same quantised plaintext comput ation.
Top-k proﬁle coordinates are selected with a data-oblivious bitonic sorting network
over secret-shared score–identiﬁer pairs [27]. The default setting uses capacity K = 128
and k = 10. Pairs are ordered by descending score, with ascending public co ordinate
identiﬁer as a stable tie rule. Coordinates below the public mini mum-support threshold
receive a sentinel score and cannot be selected. Scores and identiﬁ ers remain shared
during comparison, and only the output authorised by R0–R3 is revealed. A released
coordinate is described as a semantic category only for datasets whose doc umentation
supplies that interpretation.
For advertisement selection, candidate a uses the same frozen item map, va =
ϕD(a), unless a separately documented public candidate representati on is evaluated,
and receives score qu,a = zT uva. To preserve the stated single-boundary schedule,
all candidate scoring and argmax operations are performed in the MPC phase. T he
candidate set is ﬁxed independently of the secret proﬁle by a docu mented retrieval
procedure; private candidate retrieval and access-pattern hiding are outside scope. R1
reveals only the winning identiﬁer, with ties resolved by ascend ing candidate identiﬁer.
Auction pricing, billing, frequency capping, and conversion attribut ion are not part of
the evaluated functionality.
3.6 Security argument
The security claim is a composition claim, not a new proof
of CKKS or MPC. Deﬁne the allowed leakage as L =
(m, K, N, ciphertext count and sizes , session timing , declared output). Under ring-
L WE security of the chosen CKKS parameters, the adopted semi-honest secure
conversion, the semi-honest security of the selected MPC primit ives, fresh masks,
authenticated conﬁdential channels, and corruption of at most one computat ion
server, a server’s protocol view should be simulatable from its own input and L.
SHE sees encrypted local vectors, public weights, dimensions, and it s mask share.
10

SMPC sees a uniformly polynomial-masked decryption and its subsequent M PC view.
Sequential composition then protects local vectors and the unmasked aggr egate
within the stated model.
The claim is limited to this semi-honest composition. Collusion rec onstructs su; a
malicious SHE may attempt decryption-oracle queries; authorised outputs reveal t heir
declared semantics; and repeated outputs may expose proﬁle changes. Us er alignment
is outside the functionality, while dimensions, timing, and message volume remain in
L unless padded. CKKS and ﬁxed-point approximation may also change near- tied
rankings without violating conﬁdentiality.
3.7 Complexity analysis
Let C be the CKKS slot capacity and L =⌈K/C⌉ the number of ciphertexts per
user when users are not packed together. Each data holder sends O(L) ciphertexts per
proﬁle. Homomorphic aggregation requires O(mL) additions and, when party weights
are used, O(mL) plaintext–ciphertext multiplications. The masked conversion se nds
O(L) ciphertexts and produces O(K) shared ﬁxed-point values.
Secure clipping and normalisation require O(K) arithmetic and comparison opera-
tions apart from reciprocal approximation. A full sorting network requ ires O(K log2 K)
comparisons, whereas a specialised selection network may reduce th e constant when
Top-K is much smaller than K. End-to-end cost is therefore expected to be dominated
by ciphertext transmission for large proﬁles and by MPC comparisons for l arge K. The
experiments report measured costs rather than relying only on asympt otic complexity.
4 Experiments
The experiments are designed to answer four questions. RQ1 evaluate s whether
H2Proﬁle preserves proﬁle and targeting utility relative to plaintex t centralisation.
RQ2 compares end-to-end latency and online communication with FHE and M PC
protocols. RQ3 tests the contribution of batching, single-boundary con version, secure
normalisation, and selective release. RQ4 examines sensitivity to proﬁle dimension,
network conditions, numerical precision, output-release policy, r epeated releases, and
near-tied coordinate scores.
4.1 Experimental setup
4.1.1 Data construction and evaluation protocol
Three public datasets provide complementary behavioural settings (Table 1).
TencentGR-1M is the primary advertising dataset and contains de-ide ntiﬁed expo-
sure and click sequences [ 28]. Because it does not provide a semantic item taxonomy,
its released 32-dimensional item embeddings are ℓ2-normalised and clustered on
training-catalogue items into 127 frozen latent-interest coordinates; a ﬁnal coordinate
represents missing embeddings. Exposure and click events form t he two simulated
holders. This partition is an advertising-workload surrogate rather than a claim about
natural organisational ownership.
11

T able 1 Reproducible proﬁle coordinates and simulated data owners hip.
Dataset Proﬁle basis Behaviour holder A Behaviour holder B L eakage/overlap
control
TencentGR 127 training-only
embedding clusters
+ unknown
Exposure-labelled
sequence events
Click-labelled
sequence events
One action label
per event; frozen
centroids
KuaiSAR-small First-level item
category +
other/unknown
Search log Recommendation
log
Source-qualiﬁed
event keys;
training-only
category counts
KuaiRec 31 normalised item
tags, zero-padded
to 128
Pre-cutoﬀ big
matrix
Deduplicated pre-
cutoﬀ small matrix
User–item–time
deduplication; later
small matrix used
only as outcome
KuaiSAR-small is the oﬃcial reduced-time-window KuaiSAR release us ed to keep
repeated cryptographic evaluation tractable [ 29]. Its ﬁrst-level item category deﬁnes
the proﬁle coordinate: the 127 most frequent training categories are ret ained and
remaining or missing categories map to “other/unknown”. Search and recomm enda-
tion logs form the two holders. KuaiRec supplies a second recommendati on setting
and the output-leakage audit [ 30]. Its 31 item tags form a normalised multi-hot pro-
ﬁle, zero-padded to K = 128; pre-cutoﬀ records from the big and small matrices form
the two holders, and later small-matrix interactions provide outcome s. User attributes
are used only for the leakage audit, with user-disjoint attack training, v alidation, and
test sets.
The oﬃcial chronological protocol is used when available; otherwise, each user’s
ordered history is split 70/10/20 into training, validation, and test perio ds. Users with
fewer than ﬁve historical events or no evaluable future positive are e xcluded from
ranking metrics. All proﬁle maps, category frequencies, negative pool s, and thresholds
are ﬁtted without test-period information. Holder histories are chec ked for overlap,
declared duplicates are removed, and post-cutoﬀ inputs are exclude d.
4.1.2 Prediction tasks, candidate construction, and leakage control
The ranking task scores each future positive advertisement or item u sing zT uϕD(i)
against a candidate set containing that positive and nneg = 99 negatives. Negatives
are sampled from candidates eligible at the query time, exclude prev iously positive
items, and form the same ﬁxed candidate set for every method. HR@K and ND CG@K
obtained from sampled candidates are labelled as sampled ranking metric s, not full-
catalogue estimates. For KuaiSAR the proﬁle coordinates have documente d category
semantics, for KuaiRec they are published item tags, and for TencentG R they are
latent bins.
Unexposed items are not treated as negative clicks. All preprocessing choices,
action weights, decay, party weights, thresholds, reciprocal parame ters, and attack-
model hyperparameters are selected using training and validation dat a only. Test
histories never contribute to the ﬁtted taxonomy, popularity distr ibution, negative
pool, proﬁle vector, or release-policy threshold.
12

4.1.3 Implementation, baselines, and metrics
The proﬁle-ranking backbone is deliberately non-neural and has no trai nable param-
eters. Its proﬁle encoder maps each event to the ﬁxed public vect or ϕD(i), applies
the public action and time-decay weights in Eq. ( 1), sums across the two simulated
holders, clips each coordinate, and performs the normalisation in Eq. ( 4). The candi-
date encoder reuses the same frozen map, and the ranking score is the d ot product
qu,a = zT uϕD(a). Consequently, no optimiser, learning rate, training mini-batc h, or
training epoch count applies to the utility backbone. The batch siz e of 64 reported
below is a cryptographic packing and execution batch, not a stochastic -gradient train-
ing batch. This parameter-free design isolates diﬀerences caused b y secure numerical
execution from diﬀerences caused by model ﬁtting.
The attribute-inference audit is the only component that uses a trai nable multi-
layer perceptron. Its input width equals the released represen tation, followed by fully
connected layers of 64 and 32 units with ReLU activations, dropout of 0.2, and on e
sigmoid output per binary attribute. The attack model is trained with Adam, an ini-
tial learning rate of 10 −3, weight decay of 10 −5, a mini-batch size of 256 users, and
binary cross-entropy loss for at most 100 epochs. Early stopping uses vali dation ROC-
AUC with a patience of 10 epochs, and the checkpoint with the highest v alidation
ROC-AUC is evaluated once on the disjoint attack-test users. Logistic re gression uses
an ℓ2 penalty with its regularisation strength selected on the same attack-v alidation
partition.
All execution modes receive identical local vectors, implement t he normalised pro-
ﬁle in Eq. ( 4), apply the same support and tie rules, and release the same R2 Top-10
output. The plaintext reference is evaluated in both real-valued and quantised arith-
metic to separate quantisation from cryptographic error. End-to-end cos t includes
input transfer, representation conversion, bootstrapping where ap plicable, and output
reconstruction.
The MPC baseline uses signed Q16.16 additive shares in Z264 and performs aggre-
gation, clipping, reciprocal approximation, normalisation, and Top-10 sel ection in
MP-SPDZ [ 31]. The FHE baseline uses OpenFHE’s CKKS–FHEW scheme switch-
ing: packed CKKS handles aggregation and arithmetic, whereas bootstrapped FHEW
comparisons implement clipping and Top-10 selection without plainte xt decryption
before release [ 32]. BLB’s hybrid CKKS–MPC schedule is adapted to the same pro-
ﬁle functionality and evaluated in the common harness [ 24]; its entries are therefore
results of this study rather than values reported for Transformer inf erence. The
repeated-conversion variant is treated separately as an H2Proﬁle ablation.
Ranking utility is evaluated with HR@10 and NDCG@10. Numerical ﬁdelity i s
assessed by proﬁle error and agreement with the plaintext Top-10 set. F or user u,
Overlap@10u =|T secure u ∩ T plain u | 10 , (5)
averaged over evaluated users. This metric measures ﬁdelity to th e plaintext func-
tionality, whereas NDCG@10 measures ranking against held-out relevance ; utility
retention is reported as NDCG@10 secure / NDCG@10plain.
13

T able 2 Utility of plaintext and privacy-preserving executions across datasets.
Execution mode TGR KSAR-small KRec
NDCG@10/
HR(R)@10
NDCG@10/
HR(R)@10
NDCG@10/
HR(R)@10
Plaintext 0.1052/0.1873 0.4160/0.6790 0.0885/0.1392
FHE [ 11] 0.0981/0.1748 0.3860/0.6420 0.0818/0.1290
MPC [ 31] 0.1043/0.1861 0.4100/0.6730 0.0878/0.1380
BLB [ 24] 0.1030/0.1836 0.4077/0.6654 0.0867/0.1364
H2Proﬁle (ours) 0.1037/0.1847 0.4099/0.6692 0.0872/0.1372
H2Proﬁle uses Microsoft SEAL 4.1 for CKKS and MP-SPDZ’s semi-honest two-
party semi2k protocol; the FHE baseline uses OpenFHE 1.5.1. Experimen ts run on two
32-core Xeon-class servers with 256 GB RAM and 16 threads. The principal LAN is
1 Gbps/0.3 ms and the W AN reference is 100 Mbps/40 ms. The common conﬁguration
uses K = 128, batches of 64 proﬁles, CKKS polynomial degree 8192 and scale 2 40,
Q16.16 sharing, and at least 128-bit classical security.
4.2 Privacy-preserving system comparison
Table 2 compares ﬁve execution modes of the same ﬁxed, parameter-free proﬁli ng
backbone: plaintext, FHE, MPC, BLB, and H2Proﬁle. Within each dataset colu mn,
all rows use the same data split, candidate construction, proﬁle deﬁ nition, scoring rule,
and release target; only the privacy-preserving execution changes. E ach cell reports
NDCG@10 followed by HR@10 or Recall@10. This design measures utility ret ention
rather than attempting to rank H2Proﬁle against unrelated recommendation ar chi-
tectures. Values across dataset columns remain incomparable because th e datasets
and candidate sets diﬀer. Complete secure systems and internal mod ule ablations are
analysed separately below.
TGR denotes TencentGR-1M [ 28], KSAR-small denotes the oﬃcial reduced-time-
window KuaiSAR release [ 29], and KRec denotes KuaiRec [ 30]. Table 2 deliberately
bolds the numerically highest result in each dataset column: plainte xt is best on
all reported ranking metrics, and MPC is the strongest secure execu tion. H2Proﬁle
is therefore not presented as the most accurate method. Instead, it r etains 98.53–
98.57% of plaintext NDCG@10 and 98.56–98.61% of plaintext HR(R)@10 across the
three dataset conﬁgurations while targeting a lower-cost execution poi nt. On TGR, its
93.8% Top-10 overlap and 0.1037 NDCG@10 have diﬀerent denominators: the former
measures agreement with the plaintext Top-10 set, whereas the latter measures rank-
ing quality against held-out relevance. The appropriate NDCG ﬁdelity c omparison is
0.1037/0.1052 = 98 .6%.
FHE and MPC are study-deﬁned single-technology baselines rather than n ames
coined by one paper: FHE uses CKKS through OpenFHE, whereas MPC uses th e
MP-SPDZ framework. MPC retains marginally higher utility because it s ﬁxed-point
path avoids CKKS approximation. BLB implements a hybrid CKKS–MPC sc hedule
under the common proﬁle functionality, and its numerical entries are generated by
this study’s harness. The resulting comparison separates predict ive utility in Table 2
14

T able 3 Complete secure-system utility and eﬃciency under the commo n TencentGR-1M
R2 conﬁguration.
Execution
NDCG
retention ↑
Latency (s)
↓
Communication
(MB) ↓
FHE [ 11] 93.3% 2.63 48.5
MPC [ 31] 99.1% 1.81 171.0
BLB [ 24] 97.9% 1.12 46.2
H2Proﬁle (ours) 98.6% 0.84 34.7
NDCG retention is relative to plaintext; higher is better. Laten cy and communication are
measured per 64-proﬁle LAN batch. Bold entries are the best in eac h column.
from the TencentGR-1M system-eﬃciency evidence and the KuaiRec leakage evidence
reported below.
The reconstructed secure and quantised-plaintext proﬁles have a maximum abso-
lute diﬀerence of 1 .8×10−4. Against the real-valued plaintext reference, the end-to-end
mean Top-10 overlap is 93.8% (95% conﬁdence interval, 92.9–94.6%). Overlap
decreases to 85.2% in the near-tie subset, indicating that most rankin g changes occur
at the Top-10 boundary rather than across the full proﬁle.
Table 3 and Fig. 2 jointly show the TencentGR-1M utility–eﬃciency trade-oﬀ
that is not visible from ranking accuracy alone. H2Proﬁle retains 98.6% of plain text
NDCG@10, 0.5 percentage points below MPC, but reduces MPC latency by 53. 6%
and communication by 79.7%. Relative to FHE and BLB, H2Proﬁle has both higher
NDCG retention and lower latency and communication. Thus, its advantage i n this
comparison is system eﬃciency rather than superior predictive accu racy.
Figure 2 visualises the ﬁrst three columns of Table 3. H2Proﬁle lies closest to
the upper-left region in both panels, whereas MPC occupies the high est-utility but
highest-communication point. Because the four systems are independ ent implementa-
tions rather than points on a continuous scaling curve, the markers are n ot connected
by lines.
4.3 Ablation studies
The ablations modify H2Proﬁle itself rather than introducing competi ng systems.
“No batching” removes CKKS packing, “Repeated conversion” converts hold er cipher-
texts separately before share aggregation, “No normalisation” removes secur e proﬁle
normalisation, and “Full release” changes the authorised output from the s elected pro-
ﬁle to the complete vector. FHE, MPC, and BLB are therefore excluded f rom this
subsection’s ablation ﬁgure.
On TencentGR-1M, removing batching increases batch latency by 3.70 × and com-
munication by 3.53×, while repeated secure conversion increases latency by 63.1%.
Removing normalisation oﬀers only a 9.5% latency reduction but lowers ND CG@10.
In the KuaiRec leakage audit, removing normalisation raises attribute- inference AUC,
and full-vector release produces the largest increase in semantic l eakage.
Figure 3 visualises these eﬀects without mixing them with complete-sys tem base-
lines. In the TencentGR-1M panels, removing batching leaves nu merical ﬁdelity
15

   
/DWHQF\SHUSURILOHEDWFKV








1'&*#UHWHQWLRQ

+3URILOH
%/%
03&
)+(
3ODLQWH[WXWLOLW\
D

       
2QOLQHFRPPXQLFDWLRQ0%

+3URILOH
%/%
03&
)+(
3ODLQWH[WXWLOLW\
E

Fig. 2 Secure-system eﬃciency–utility comparison under the common Tenc entGR-
1M R2 conﬁguration. Panels (a) and (b) plot NDCG@10 retention against batch
latency and online communication, respectively. The dashed horizont al line denotes
plaintext utility. Every marker represents a complete executi on system; internal
module ablations are excluded. Higher retention and lower system cost are preferable.
unchanged because it alters packing rather than arithmetic, but subs tantially increases
latency and communication. Repeated conversion introduces additional approximation
error and transfer cost. Removing normalisation is slightly faster but reduces Top-10
overlap to 85.7% and retains only 92.7% of plaintext NDCG@10. In the KuaiRec leak -
age panel, removing normalisation raises AUC to 0.643, while full-vector re lease raises
it to 0.731.
To test whether the ablations behave consistently with the geometr y of proﬁle
vectors, a controlled synthetic diagnostic generates 720 non-negative 128-d imensional
proﬁles from four compact groups in one latent-interest space. The group c ores have
unequal orientations and separations, while 12% of users lie closer to an adj acent group
to avoid artiﬁcially empty boundaries. A ﬁxed positive radial-basis m ap converts each
latent point into a category proﬁle, so nearby groups share part of their in terest mass.
The complete pipeline applies 16-bit quantisation, small centred con version noise, clip-
ping, and renormalisation. The repeated-conversion variant increases t he conversion
perturbation, while the no-normalisation variant retains user-speci ﬁc magnitude vari-
ation and holder bias. All plaintext and variant vectors are embedded togeth er in one
t-SNE ﬁt with perplexity 120, early exaggeration 2, and a ﬁxed seed; ﬁtting separate
maps would make their coordinates incomparable.
Figure 4 shows that the complete pipeline remains locally co-located with q uantised
plaintext, whereas removal of normalisation visibly distorts neighbou rhoods. Because
repeated conversion produces only limited visual drift, it is ret ained in the quantitative
comparison rather than repeated as a near-duplicate t-SNE panel. The corr espond-
ing 10-nearest-neighbour retention values in the original 128-dimensional space are
0.983, 0.941, and 0.116 for the complete pipeline, repeated conversion, and remo val
of normalisation, respectively. Only local neighbourhood preserv ation and paired dis-
placement are interpreted; distances between separated t-SNE clu sters are not treated
16

+3URILOH1REDWFKLQJ5HSHDWHGFRQY 1RQRUP )XOOUHOHDVH



)LGHOLW\XWLOLW\UHWHQWLRQ











D

+3URILOH1REDWFKLQJ5HSHDWHGFRQY 1RQRUP )XOOUHOHDVH



/DWHQF\V




 
E

+3URILOH1REDWFKLQJ5HSHDWHGFRQY 1RQRUP )XOOUHOHDVH





&RPPXQLFDWLRQ0%




 
F

+3URILOH1REDWFKLQJ5HSHDWHGFRQY 1RQRUP )XOOUHOHDVH





/HDNDJH52&$8&ORZHULVEHWWHU

  


G

7 RSRYHUODS 1'&*#UHWHQWLRQ
Fig. 3 Module and release-policy ablations. Panels (a)–(c) use the common
TencentGR-1M R2 conﬁguration and report Top-10 overlap and NDCG@10
retention, batch latency, and online communication, respectively. Panel (d) uses the
KuaiRec leakage audit and reports attribute-inference ROC-AUC. Lower is
preferable in panels (b)–(d). Red highlights complete H2Proﬁle, whil e grey denotes
all ablated variants; solid and hatched bars in panel (a) distinguish the t wo metrics.
Complete FHE, MPC, and BLB systems are excluded.
as quantitative evidence. This controlled diagnostic tests the mech anism implied by
the arithmetic pipeline and does not substitute for dataset-level utility or privacy
evaluation.
4.4 Parameter sensitivity and numerical correctness
The reported precision sensitivity varies ﬁxed-point fractional p recision f and the
CKKS scale around the selected conﬁguration. Numerical validation compare s recon-
structed secure output with quantised plaintext through maximum ab solute error
and with real-valued plaintext through mean Top-10 overlap. Proﬁle-dim ension and
network sensitivity are reported separately in Section 4.5.
Table 4 makes the reported precision-sensitivity checks explicit. In creasing ﬁxed-
point precision beyond the selected 16 fractional bits or the CKKS scal e beyond 2 40
yields little additional Top-10 agreement, whereas the lower-preci sion settings visibly
increase reconstruction error. The near-tie subset remains the li miting case because
small score changes can alter membership at the Top-10 boundary.
17

W61(
W61(
D

 &RPSOHWH+3URILOH
W61(
W61(
E

 :LWKRXWVHFXUHQRUPDOL]DWLRQ
+3URILOH 5HSHDWHG 1RQRUP





11UHWHQWLRQLQ'VSDFH
 

F

Fig. 4 Controlled synthetic feature-space diagnostic for the ablation study. Panels
(a) and (b) overlay the complete pipeline and the variant without sec ure
normalisation, respectively, on quantised plaintext proﬁles (grey op en circles);
coloured points denote latent interest groups and connecting segments mark paired
proﬁles. Both panels use coordinates from the same joint t-SNE ﬁt. Panel (c) reports
10-nearest-neighbour retention computed in the original 128-dimensional s pace for
all three variants, including repeated conversion; these values are not computed from
the t-SNE map.
T able 4 Precision-parameter sensitivity under the TencentGR-1M R2 c onﬁguration.
Parameter Setting Max. error Overlap@10
Fixed-point f 12 bits 7 .6 × 10−4 91.6%
Fixed-point f 16 bits 1 .8 × 10−4 93.8%
Fixed-point f 20 bits 1 .2 × 10−4 93.9%
CKKS scale 2 35 4.2 × 10−4 92.8%
CKKS scale 2 40 1.8 × 10−4 93.8%
CKKS scale 2 45 1.5 × 10−4 93.9%
Maximum absolute error is measured against quantised plaintex t, whereas Top-10 overlap is
measured against real-valued plaintext. Bold entries identify the selected operating point.
4.5 Robustness and scalability analysis
Scalability is evaluated by varying the proﬁle dimension from 32 to 512 wh ile hold-
ing the batch size, security target, and LAN conﬁguration constant. Latency increases
from 0.31 to 3.02 s and communication from 11.8 to 125.8 MB, while Top-10 overlap
decreases gradually from 94.8% to 91.7% across the evaluated range. Linear ﬁts ove r
these ﬁve conﬁgurations give latency = 0 .00566K + 0.115 s ( R2 = 0 .9999) and com-
munication = 0 .23749K + 4.242 MB ( R2 > 0.9999). These ﬁts describe the evaluated
interval only.
Figure 5 provides the corresponding scalability and network evidence. The marked
K = 128 operating point is the conﬁguration used in the main comparison. Latency
and communication grow approximately linearly with proﬁle dimension over the
18

    
3URILOHGLPHQVLRQ.





%DWFKODWHQF\V



D

    
3URILOHGLPHQVLRQ.





2QOLQHFRPPXQLFDWLRQ0%



E

    
3URILOHGLPHQVLRQ.





7 RSRYHUODS




F

/$1 :$1 :$1 :$1






%DWFKODWHQF\V

. 



G

Fig. 5 Scalability and network robustness. Panels (a)–(c) report batch latenc y,
online communication, and Top-10 overlap as the proﬁle dimension increas es from 32
to 512 under the common LAN setting; open markers identify the selected K = 128
conﬁguration. Panel (d) reports latency at K = 128 for LAN (1 Gbps/0.3 ms),
W AN-1 (100 Mbps/40 ms), W AN-2 (50 Mbps/40 ms), and W AN-3 (20 Mbps/80 ms).
Red identiﬁes the principal LAN conﬁguration and grey denotes W AN stress settings.
tested range, whereas Top-10 overlap degrades gradually rather than collaps ing. The
W AN panel isolates network sensitivity at ﬁxed K = 128 and shows that band-
width and round-trip time, rather than proﬁle arithmetic alone, domin ate the slowest
conﬁguration.
The mean overlap is 93.8% at K = 128 and 85.2% in the near-tie subset. Network
sensitivity is evaluated at 1 Gbps/0.3 ms LAN and three W AN conditions. F or K =
128, batch latency is 3.7 s at 100 Mbps/40 ms, 6.6 s at 50 Mbps/40 ms, and 14.8 s at
20 Mbps/80 ms.
Privacy robustness is evaluated on KuaiRec by changing R0–R3 and the numb er
of longitudinal releases Q. The logistic-regression and multilayer-perceptron attacks
speciﬁed in Section 4.1.3 use disjoint attack-training, validation, and test users.
Figure 6 reports ROC-AUC and Macro-F1 across release policies and ROC-AUC across
repeated R2 releases, with a history-only attacker as the reference . Collusion is not
presented as an experiment that the protocol survives because it vi olates the threat
model.
Increasing K from 32 to 512 raises batch latency from 0.31 to 3.02 s and com-
munication from 11.8 to 125.8 MB. Under the common KuaiRec R2 leakage audit,
19

5 5 5 5 )XOO
5HOHDVHSROLF\




$WWDFNSHUIRUPDQFH
D

52&$8&
0DFUR)
   
1XPEHURIORQJLWXGLQDOUHOHDVHV4








$WWULEXWHLQIHUHQFH52&$8&
E

5UHOHDVH
+LVWRU\RQO\DWWDFNHU
Fig. 6 KuaiRec output-privacy sensitivity under user-disjoint attack s plits. (a)
Attribute-inference ROC-AUC and Macro-F1 under release policies R0–R3 and
unquantised full-vector release. (b) Attribute-inference RO C-AUC under repeated
R2 releases. The dashed line marks the history-only attacker.
H2Proﬁle obtains an attribute-inference AUC of 0.604, compared with 0.628 for FHE,
0.621 for MPC, and 0.613 for BLB. Figure 6 shows that progressively richer releases
increase attribute-inference performance: ROC-AUC rises from 0.542 for R0 to 0.604
for R2, 0.681 for R3, and 0.731 for the unquantised full vector. Under R2, repeate d
releases increase attack AUC from 0.604 at Q = 1 to 0.632, 0.659, and 0.693 at
Q = 4 , 8, 16, respectively. Selective release therefore changes semantic le akage even
when the underlying cryptographic execution is unchanged.
5 Discussion
5.1 Interpretation and methodological positioning
H2Proﬁle is based on a workload-speciﬁc observation: cross-platform inter est construc-
tion contains a large additive stage followed by a smaller decision stage. HE and MPC
are therefore not treated as interchangeable privacy labels. Packed CKK S is assigned
to regular, high-dimensional arithmetic, while MPC is assigned to com parisons, clip-
ping, division, and selective release. The security of the boundary comes from the
adopted polynomial-domain conversion protocol, not from the scheduling i dea itself;
the evaluation therefore focuses on the measured utility and system cost of using one
conversion boundary for this proﬁling workload.
The evaluation should be interpreted along three separate axes. First , utility agree-
ment with plaintext establishes numerical correctness, not addit ional predictive power.
If H2Proﬁle and the plaintext implementation use the same proﬁle deﬁni tion, cryptog-
raphy should not be credited with improving recommendation quality . Second, lower
latency or communication relative to a baseline supports only the tes ted operator
allocation, parameter set, data dimension, and network. Third, crypt ographic input
conﬁdentiality does not imply that the authorised output is harmless . A system that
20

securely releases a detailed, repeatedly queryable proﬁle may sat isfy protocol security
while still enabling intrusive proﬁling.
This positioning distinguishes the study from client-side adver tising systems and
federated model training. Adnostic and Privad redesign where proﬁlin g and selec-
tion occur [ 2, 3]. Federated recommendation changes how a shared model is learned
[5]. H2Proﬁle addresses a narrower collaborative-computation problem: sev eral organ-
isations already hold complementary evidence for an authorised proﬁle cal culation,
but none should receive the others’ raw evidence or the unﬁltered aggregate. These
approaches may be combined in deployment; they are not mutually excl usive.
The KuaiRec leakage audit shows a trade-oﬀ across the evaluated release pol icies. A
full proﬁle retains reuse but produces the highest measured attri bute-inference AUC,
whereas Top-K and identiﬁer-only release expose less proﬁle detail. These comparisons
apply only to the evaluated attack model and release settings.
5.2 Limitations
The principal limitation is the semi-honest, non-colluding two-se rver assumption. If
SHE and SMPC collude, their shares reconstruct the proﬁle. The key service als o
becomes a decryption risk outside the semi-honest model. Real dep loyments would
need organisational separation, threshold keys, hardware isolation, ciphe rtext/session
validation, or malicious-secure protocols supported by operational gover nance. The
current proof sketch inherits the assumptions and leakage of the exact conversion and
MPC instantiations and must not be generalised to an ad-hoc implementat ion. A dis-
honest data holder could submit manipulated category vectors, exceed c ontribution
bounds, or poison the resulting proﬁle.
The public datasets approximate rather than reproduce a commercial c ross-
company advertising ecosystem. TencentGR-1M is an industrial adver tising dataset,
but the simulated ownership of its tables does not prove that indep endent organisa-
tions would share the same identiﬁers, taxonomies, consent basis, or up date timing.
KuaiSAR captures complementary search and recommendation behaviour bu t is not
an advertising dataset. External validity should therefore be framed as evidence across
two behavioural structures, not as proof of production readiness.
The category-level proﬁle is intentionally interpretable and crypt ographically
tractable. It may underrepresent semantic nuance captured by mod ern sequence or
generative recommenders. Integrating learned embeddings would increase dimensional-
ity and could introduce deeper nonlinear computation. Conversely, r eleasing a learned
dense proﬁle may make output leakage harder to interpret rather than sm aller.
Finally, privacy is bounded by identity alignment, metadata, output, and query
policy. The protocol does not privately align users, hide message timi ng, prevent
discriminatory targeting, validate category semantics, or stop unlawful use of an autho-
rised result. Data minimisation, consent, purpose limitation, ret ention controls, and
independent auditing remain necessary. These governance requir ements are outside the
cryptographic proof but inside any defensible claim of privacy-pres erving advertising.
21

6 Conclusion
This study speciﬁes H2Proﬁle, a conversion-minimising HE–MPC frame work for
constructing category-level advertising proﬁles from distribute d behavioural data.
The framework uses packed approximate HE for local-vector aggregation, invok es
an existing secure polynomial-domain conversion once, and uses MPC for b ounded
normalisation, comparison, Top-K selection, and optional advertisement m atching.
Subject to the exact underlying protocols and a static semi-honest , non-colluding
two-server model, the composition is intended to hide inputs and i ntermediate aggre-
gates beyond declared metadata and authorised outputs. It does not protec t identity
alignment or malicious execution.
The experimental design separates numerical ﬁdelity, targeting ut ility, system cost,
scalability, and output leakage. TencentGR-1M provides the primary ad vertising set-
ting, KuaiSAR-small tests complementary cross-platform behaviour, an d KuaiRec
provides a second recommendation setting and the leakage audit. Under t he com-
mon conﬁguration, H2Proﬁle achieves 93.8% mean Top-10 overlap, 0.84 s latency,
and 34.7 MB communication per 64-proﬁle LAN batch. The resulting evidence indi-
cates that the single-boundary allocation oﬀers a practical advantage over F HE, MPC,
and BLB alternatives within the evaluated setting. Future work should add malicious
security, veriﬁable input bounds, threshold decryption, dynami c proﬁle updates, and
policy-aware query controls.
Data availability
TencentGR-1M is available from the Tencent Advertising Algorithm Com petition col-
lection at https://huggingface.co/datasets/TAAC2025/TencentGR-1M. KuaiSAR is
available from Zenodo at https://zenodo.org/record/8181109. KuaiRec is available
from Zenodo at https://zenodo.org/records/18164998.
Code availability
The FHE and MPC baselines were implemented using OpenFHE ( https://github.
com/openfheorg/openfhe-development) and MP-SPDZ ( https://github.com/data61/
MP-SPDZ), respectively. The oﬃcial implementation of BLB is available at https:
//github.com/best-orange/blb.
Ethics approval
The experiments use publicly released, de-identiﬁed secondar y datasets, do not recruit
participants, and do not access directly identiﬁable records. The an alysis follows the
documented terms of use and reports only aggregate results.
Acknowledgements
This research received no speciﬁc grant from any funding agency in th e public,
commercial, or not-for-proﬁt sectors.
22

Author contributions
W.C. conceived the study, designed the methodology, implemented the software and
experiments, analysed the results, and prepared and revised the m anuscript.
Competing interests
The author declares no competing interests.
References
[1] Oliveira, M., Yang, J., Griﬃths, D., Bonnay, D. & Kulshrestha, J . Browsing
behavior exposes identities on the web. Scientiﬁc Reports 15, 36066 (2025).
[2] Toubiana, V., Narayanan, A., Boneh, D., Nissenbaum, H. & Barocas, S. Adnostic :
Privacy preserving targeted advertising. Proceedings of the Network and Dis-
tributed System Security Symposium (2010). URL https://www.ndss-symposium.
org/ndss2010/adnostic-privacy-preserving-targeted-advertising/ .
[3] Guha, S., Cheng, B. & Francis, P. Privad: Practical privacy in onlin e advertis-
ing. 8th USENIX Symposium on Networked Systems Design and Implementation
(NSDI 11) 169–182 (2011). URL https://www.usenix.org/conference/nsdi11/
privad-practical-privacy-online-advertising.
[4] Calderonio, G., Ali, M. A. B. & Polakis, J. Fledging will continue unt il privacy
improves: Empirical analysis of google’s privacy-preserving targete d advertis-
ing. 33rd USENIX Security Symposium (USENIX Security 24) 4121–4138
(2024). URL https://www.usenix.org/conference/usenixsecurity24/presentation/
calderonio.
[5] Qi, T., Wu, F., Wu, C., Huang, Y. & Xie, X. Privacy-preserving news r ecommen-
dation model learning. Findings of the Association for Computational Linguistics:
EMNLP 2020 1423–1432 (2020).
[6] Zhao, L. et al. FedSCOPE: Federated cross-domain sequential recommen-
dation with decoupled contrastive learning and privacy-preserving semantic
enhancement. Scientiﬁc Reports 16, 7420 (2026).
[7] Sivakumar, N. et al. CRAFT: Cold-start recommender with attention and
federated training. Scientiﬁc Reports 16, 17150 (2026).
[8] Guo, S., Yang, J., Long, S., Wang, X. et al. Federated learning with diﬀerential
privacy via fast fourier transform for tighter-eﬃcient combining. Scientiﬁc Reports
14, 26770 (2024).
[9] Markkandan, S., Bhavani, N. P. G. & Nath, S. S. A privacy-preserving expert
system for collaborative medical diagnosis across multiple institution s using
23

federated learning. Scientiﬁc Reports 14, 22354 (2024).
[10] Gentry, C. Fully homomorphic encryption using ideal lattices. Proceedings of the
41st Annual ACM Symposium on Theory of Computing 169–178 (2009).
[11] Cheon, J. H., Kim, A., Kim, M. & Song, Y. Homomorphic encryption for arith-
metic of approximate numbers. Advances in Cryptology – ASIACRYPT 2017
10624, 409–437 (2017).
[12] Yao, A. C. Protocols for secure computations. 23rd Annual Symposium on
Foundations of Computer Science 160–164 (1982).
[13] Demmler, D., Schneider, T. & Zohner, M. ABY—a framework for eﬃcien t
mixed-protocol secure two-party computation. Proceedings of the Network and
Distributed System Security Symposium (2015).
[14] Mohassel, P. & Zhang, Y. SecureML: A system for scalable privacy-pres erving
machine learning. 2017 IEEE Symposium on Security and Privacy 19–38 (2017).
[15] Juvekar, C., Vaikuntanathan, V. & Chandrakasan, A. GAZELLE: A low latency
framework for secure neural network inference. 27th USENIX Security Sympo-
sium (USENIX Security 18) 1651–1669 (2018). URL https://www.usenix.org/
conference/usenixsecurity18/presentation/juvekar.
[16] Mishra, P., Lehmkuhl, R., Srinivasan, A., Zheng, W. & Popa, R. A. Delp hi:
A cryptographic inference service for neural networks. 29th USENIX Security
Symposium (USENIX Security 20) 2505–2522 (2020). URL https://www.usenix.
org/conference/usenixsecurity20/presentation/mishra.
[17] Huang, Z., Lu, W.-j., Hong, C. & Ding, J. Cheetah: Lean and fast secure
two-party deep neural network inference. 31st USENIX Security Sympo-
sium (USENIX Security 22) 809–826 (2022). URL https://www.usenix.org/
conference/usenixsecurity22/presentation/huang-zhicong.
[18] Du, J. et al. PrivacyGo: Privacy-preserving ad measurement with multidimen-
sional intersection. Cryptology ePrint Archive, Paper 2025/1192 (2025). URL
https://eprint.iacr.org/2025/1192.
[19] Lu, W.-j. et al. BumbleBee: Secure two-party inference framework for large
transformers. Network and Distributed System Security Symposium 2025 (2025).
[20] Kei, A. Y. L. & Chow, S. S. M. SHAFT: Secure, handy, accurate and
fast transformer inference. Network and Distributed System Security Sym-
posium 2025 (2025). URL https://www.ndss-symposium.org/ndss-paper/
shaft-secure-handy-accurate-and-fast-transformer-inference/ .
24

[21] Smajlovi´ c, H. et al. Shechi: A secure distributed computation compiler
based on multiparty homomorphic encryption. 34th USENIX Security Sympo-
sium (USENIX Security 25) 7703–7722 (2025). URL https://www.usenix.org/
conference/usenixsecurity25/presentation/smajlovic.
[22] Lv, Y. et al. SMASH: Scalable maliciously secure hybrid multi-party compu-
tation framework for privacy-preserving large language models. 35th USENIX
Security Symposium (USENIX Security 26) (2026). URL https://www.usenix.
org/conference/usenixsecurity26/presentation/lv.
[23] Bl¨ uml, J., Huppert, M., Khayata, N., Schmidt, J. & Schneider, T. SING:
Improving the eﬃciency of mpc protocol assignment using graph neural net-
works. 35th USENIX Security Symposium (USENIX Security 26) (2026). URL
https://www.usenix.org/conference/usenixsecurity26/presentation/blueml.
[24] Xu, T. et al. Breaking the layer barrier: Remodeling private transformer
inference with hybrid CKKS and MPC. 34th USENIX Security Sympo-
sium (USENIX Security 25) 2653–2672 (2025). URL https://www.usenix.org/
conference/usenixsecurity25/presentation/xu-tianshi.
[25] Mouchet, C., Troncoso-Pastoriza, J., Bossuat, J.-P. & Hubaux, J.-P. M ultiparty
homomorphic encryption from ring-learning-with-errors. Proceedings on Privacy
Enhancing Technologies 2021, 291–311 (2021).
[26] Catrina, O. & Saxena, A. Secure computation with ﬁxed-point number s.
Financial Cryptography and Data Security 6052, 35–50 (2010).
[27] Batcher, K. E. Sorting networks and their applications. Proceedings of the April
30–May 2, 1968, Spring Joint Computer Conference 307–314 (1968).
[28] Pan, J. et al. Tencent advertising algorithm challenge 2025: All-modality gen-
erative recommendation. arXiv preprint arXiv:2604.04976 (2026). URL https:
//arxiv.org/abs/2604.04976.
[29] Sun, Z. et al. KuaiSAR: A uniﬁed search and recommendation dataset. Proceed-
ings of the 32nd ACM International Conference on Information and Knowledge
Management (2023).
[30] Gao, C. et al. KuaiRec: A fully-observed dataset and insights for evaluating
recommender systems. Proceedings of the 31st ACM International Conference on
Information and Knowledge Management 540–550 (2022).
[31] Keller, M. MP-SPDZ: A versatile framework for multi-party compu tation.
Proceedings of the 2020 ACM SIGSAC Conference on Computer and Com muni-
cations Security 1575–1590 (2020).
25

[32] Al Badawi, A. et al. OpenFHE: Open-source fully homomorphic encryption
library. Cryptology ePrint Archive, Paper 2022/915 (2022). URL https://eprint.
iacr.org/2022/915.
26
