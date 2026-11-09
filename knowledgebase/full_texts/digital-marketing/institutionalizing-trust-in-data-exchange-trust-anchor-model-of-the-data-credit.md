---
title: 'Institutionalizing Trust in Data Exchange: Trust-Anchor Model of the Data Credit Guarantee Organization
  and Its Simulation-Based Comparison'
url: https://arxiv.org/abs/2610.18400
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Hiroshi Mano
- Chie Sugiyama
- Teruaki Hayashi
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.18400
pages: 10
chars: 55169
fetched_at: '2026-11-08T13:22:56+00:00'
kb_version: 1
---

# Institutionalizing Trust in Data Exchange: Trust-Anchor Model of the Data Credit Guarantee Organization and Its Simulation-Based Comparison

Institutionalizing Trust in Data Exchange:
Trust-Anchor Model of the Data Credit Guarantee
Organization and Its Simulation-Based Comparison
Hiroshi Mano
EverySense Japan Inc.
Tokyo, Japan
h.mano@every-sense.com
Chie Sugiyama
Data Society Alliance
Tokyo, Japan
c.sugiyama@data-society-alliance.org
Teruaki Hayashi
Hitotsubashi University
Tokyo, Japan
teruaki.hayashi@r.hit-u.ac.jp
Abstract—Data trading markets that span industries and
regions are expanding, but the implicit trust that supports data
use within an organization does not carry over to cross-domain
exchange. This paper examines the Data Credit Guarantee Or-
ganization (DCGO), a proposal to institutionalize trust through
third-party verification and certification, and asks what it means
to trust data, what such certification can support, and under
what conditions DCGO outperforms existing trading models.
We decompose trust in data into four layers: authenticity of
entity, authenticity and integrity of data, rights and conditions
of use, and history and auditability. A third party can certify
authenticity but not the correctness of content, and DCGO is
positioned as a trust anchor spanning existing marketplaces and
data spaces. We then extend the Law Merchant model with
three data-specific properties, namely imperfect ex-post detection,
cheap pseudonyms, and non-rivalry of harm, and compare bilat-
eral trading with DCGO by agent-based simulation. DCGO keeps
the buyer’s payoff near its theoretical upper bound regardless
of the market environment, whereas bilateral trading loses even
when fraud is always detected. Identity verification proves to be
a prerequisite for record sharing, and pre-verification is the only
function that limits the spread of harm. On the seller side, honest
sellers join voluntarily whenever the price premium exceeds the
fee. Lock-in and a critical mass for diffusion, however, call for
fee governance and support for entry.
Index Terms—data trust, data market, third-party certifica-
tion, data credit guarantee, agent-based simulation
I. INTRODUCTION
A. Data Trading Markets and the Fragmentation of Trust
With the development of AI and big data, data have come
to be regarded as a strategic asset that determines the perfor-
mance of AI, decision making, and service delivery. Global
private investment in generative AI reached USD 33.9 billion
in 2024 [1], and the market for data marketplaces is projected
to grow from about USD 1.5 billion in 2024 to about USD 5.7
billion by 2030 [2]. This trend is pushing up the demand for
data whose quality, rights clearance, and provenance have been
verified, and data trading markets for discovering, acquiring,
and reusing data across industries and regions are expanding.
They take two broad forms: data marketplaces, in which
providers list “data products” in a catalog and users search,
contract, and use them in the cloud, and data spaces, federated
ecosystems in which participants keep data under their own
control and share them on the basis of common identifiers,
connection methods, usage policies, and governance rules.
What these markets have in common is that they combine
third-party trust functions, such as identity verification of
organizations, electronic signatures and certificates issued by
trusted third parties (TTPs), access control, contracts and terms
of use, and audit logs, with the operational governance of each
operator. A signature or certificate, however, shows only that
a specific entity issued specific information or that alteration
can be detected. It does not guarantee that the data represent
real-world facts, that the provider holds sufficient rights, or
that the intended use is permitted. Which evidence is verified,
how certificates are revoked and corrected, and who bears
responsibility in a dispute are determined by the governance
of each marketplace or data space operator.
This operator-specific governance allows flexible design
according to the business characteristics of each market, but
it fragments the evidence of trust when it must be carried
between markets. A certification, evaluation, or audit result ob-
tained in one market is not necessarily recognized in another,
so identity verification, rights verification, quality verification,
and audit preparation are repeated for the same provider or
the same data at every connection point. This raises the cost
of participation for providers and the time and uncertainty
from discovery to use for users. The growth of data trading
markets therefore requires, beyond more capable individual
markets, evidence of trust that can be used across markets and
a common mechanism for verification and the demarcation of
responsibility.
B. Positioning of DCGO and Research Questions
The Data Society Alliance (DSA) in Japan has advocated a
mechanism that secures trust through third-party verification
and certification in order to realize Data Free Flow with Trust
(DFFT) [3]. In fiscal year 2026, the construction of a highly
trusted data collaboration infrastructure centered on the Data
Credit Guarantee Organization (DCGO) was adopted under
the Cabinet Office’s BRIDGE program [4], and efforts toward
its social implementation are under way.
arXiv:2610.18400v1  [cs.CY]  13 Oct 2026

DCGO is not intended to replace existing data marketplaces
or data spaces. Rather, as a trust anchor that spans them, it
provides common evidence formats, verification procedures,
assurance levels, and rules for revocation, correction, and
audit, so that evidence of trust can be carried between markets
and data spaces in a verifiable form while preserving the
expertise and flexibility of each operator. DCGO thus does not
substitute for the internal governance of individual markets; by
resolving the cross-market information asymmetry and frag-
mentation of trust that are hard to solve within a single market,
it complements existing governance and may accelerate the
growth of data trading through the expansion of data supply,
demand, reuse, and the scope of trading.
The focus of this paper therefore shifts from whether trust
exists in existing markets to a question of institutional design:
which trust functions should be shared across markets so as to
complement existing governance while lowering the barriers to
participation and the information asymmetry in data trading?
We address it through three research questions.
•RQ1:What does it mean to trust data?
•RQ2:What, and to what extent, can a mechanism of
verification and certification such as DCGO support?
•RQ3:Under what conditions does DCGO work effec-
tively compared with existing trading models?
Our contributions are threefold. First, we decompose trust
in data into four layers, namely the authenticity of entity, the
authenticity and integrity of data, rights and conditions of use,
and history and auditability, and define what trustworthy data
are (RQ1). Second, we map the architecture of DCGO onto
the four layers and clarify the scope and boundary of what
third-party certification can support (RQ2). Third, we model
a data market with information asymmetry as an agent-based
simulation and compare bilateral trading with DCGO, showing
the conditions under which DCGO benefits both buyers and
sellers and which layer is responsible for which effect (RQ3).
II. RELATEDINITIATIVES ANDRESEARCH
A. Data Marketplaces and Data Spaces
Existing data trading markets fall into three design axes. The
first is the market platform type, which catalogs data products
and brokers search, purchase, delivery, and settlement. AWS
Data Exchange [5] and Snowflake Marketplace [6] are com-
mercial examples in which users subscribe to data products
from within the provider’s cloud environment, and EverySense
Pro in Japan offers catalog search, negotiation, delivery, and
settlement for inter-company trading while the operator con-
fines itself to brokerage [9]. The second is the data space type,
in which participants retain control over their data and use
them across organizations on the basis of common connection
methods, access rights, and usage rules. Catena-X, an industry-
led data space of the automotive industry, exchanges data
directly between participants through connectors based on the
IDS reference architecture, with conditions of use negotiated
and enforced as policies between connectors [7], [8]. The third
is the rights certificate type, which expresses the scope of
permitted actions on data as rights and trades those rights. In
the data usage rights trading market that DSA is testing, the
conditions of use defined by the provider (access, method of
use, redistribution, and period of use) are embodied as a “data
usage rights certificate” bound to the data and traded [11]. Real
services combine these axes; the Kyoto Data Marketplace, a
catalog site for public and private data [10], can connect a
catalog with a data space and incorporate usage rights and
contract terms into it.
B. Standardization of Data Trading Systems and Data Spaces
For data spaces, the International Data Spaces Associa-
tion (IDSA) maintains the IDS reference architecture and
is standardizing the Dataspace Protocol for communication
between connectors [12], Gaia-X provides a trust framework
for evaluating the trustworthiness of participants and ser-
vices [13], and industrial data spaces such as Catena-X build
on these. In Japan, the Digital Architecture Design Center of
the Information-technology Promotion Agency (IPA) is devel-
oping ODS-RAM (Open Data Spaces Reference Architecture
Model) [14], and DSA promotes DATA-EX, an initiative
that provides domain-independent common technologies and
standards for building data spaces, in alignment with the ODS
specifications [15].
IEEE 3800-2024, “IEEE Standard for a Data-Trading Sys-
tem: Overview, Terminology, and Reference Model,” defines
the terminology, overview, and reference model of a data
trading system and describes the relationships among data
providers, data users, trading systems, and data space operators
with common concepts, thereby providing a reference frame
for interoperability between different trading systems [16]. It
does not, however, guarantee that individual data are correct
as real-world facts, that the provider holds all rights, or that
no violation of conditions of use occurs after the trade. We
therefore position DCGO on top of this reference frame as a
trust anchor that provides, as a third party, evidence of trust,
verification procedures, and assurance levels shared across
trading systems and data spaces built on it.
C. Provenance, Description, and Authenticity of Data
Individual technologies that support trust in data have also
accumulated. W3C PROV provides a standard model for
describing the generation, transformation, and attribution of
data [17], documentation frameworks such as Datasheets for
Datasets make explicit the purpose of collection, composition,
and constraints of machine learning data [18], and, in ad-
dition to electronic signatures, timestamps, and hash chains,
watermarking techniques verify after the fact the origin and
unauthorized use of data and trained models [19], [20]. These
technologies mainly support the authenticity and integrity
of data and history and auditability among the four layers
in Section III, but none of them answers the institutional
questions of who verifies, who guarantees, and who bears
responsibility upon revocation or dispute. This paper takes
them as given and positions DCGO as a mechanism that
bundles them and provides assurance across markets.

Data seller Data  buyer
Register data,
attest identity
Certification/
verification result
Data Credit Guarantee Organization (DCGO)
Trust anchor: third-party verification and certification
L1: Authenticity of entity
Is the data seller/buyera real, authorized party?
L2: Authenticity and integrity of data
Identical to the original, unaltered
L3: Rights and conditions of use
Which uses are permitted, to what extent
Notary-like function Supporting
functions
Catalog
(register/
search) Custody
Settlement
L4: History and auditability
Audit log and ledger record all functions; events are verifiable afterward
Query, verify,
report misuse
Data marketplace Data spaces Bilateral exchange
⋯
Fig. 1. Architecture of the Data Credit Guarantee Organization (DCGO). DCGO acts as a trust anchor between data sellers and buyers: a notary-like function
certifies the authenticity of entity (L1), the authenticity and integrity of data (L2), and rights and conditions of use (L3), and the audit log and ledger (L4)
record all functions. Data and payments flow through existing marketplaces, data spaces, or bilateral exchange, not through DCGO.
D. Economic Analysis and Simulation Studies
Information asymmetry in data markets is a market-for-
lemons problem [21]: if buyers cannot tell quality before
purchase, high-quality sellers leave and overall quality de-
clines. Classical institutional remedies are the Law Merchant
model, in which a third party that keeps records of cheating
sustains honest trade [22], and the certification intermediary
that inspects and discloses quality [23]. Online, however,
cheap pseudonyms undermine record-based institutions [24],
and data are a credence good whose quality is unknown until
use [25] and whose easy copying lets a single fraud harm
many users at once.
Beyond work on data pricing and mechanism design [26],
[27], agent-based studies of data markets are advancing.
Yamamoto and Hayashi compared reputation systems in a
manufacturing data market with agents whose utilities were
estimated by Q-learning and inverse reinforcement learning,
showing that the reputation design affects the alignment of
price and quality [28]. Sashihara et al. proposed a multi-
agent framework with large language models as buyer and
seller agents [29] and used it to analyze how institutional
designs such as transaction prohibitions affect the growth
and decline of data markets [30]. None of these studies,
however, incorporates third-party verification and certification
as a market function.
In summary, standardization provides interoperability,
provenance and authenticity technologies provide individual
pieces of evidence, and economic analysis and simulation
provide means to understand market dynamics, but no study
has cut across these fields to decompose what it means to trust
data or to ask, from the viewpoint of institutional design, under
what conditions a third-party verification and certification
mechanism works compared with existing trading models.
This paper fills that gap by decomposing trust into four layers,
mapping DCGO onto them, and testing the conditions under
which DCGO works by an agent-based simulation that extends
the Law Merchant model with data-specific properties.
III. TRUSTFRAMEWORK ANDDCGO ARCHITECTURE
A. Four Layers Supporting Trust in Data
Unlike a paper certificate or a physical product, data are
intangible: copying them does not consume the original, and
identical copies can be made in large numbers in a short time.
Whether the data in front of us are “genuine” is therefore
hard to judge by looking at them. A file name that claims to
be the original does not guarantee that it is the first record,
and even if the figures are transcribed accurately, judgment
may be wrong if the measuring instrument was not calibrated.
Moreover, even when authenticity can be verified, if the data
were redistributed beyond the scope of the license, the user
runs the risk of unexpected liability. Trust in data thus has
several faces, and a single certificate cannot cover all of them.
In this paper we define trust in data as a state in which the
following four questions, each concerning a different object
of verification, can be answered.
Authenticity of entity (L1):Do the provider and the user
exist, and are they entities with legitimate authority to provide
and use the data?
Authenticity and integrity of data (L2):Are the delivered
data identical to the presented original and free from tamper-
ing?
Rights and conditions of use (L3):Which of the actions such
as viewing, copying, processing, AI training, redistribution,
overseas provision, storage, and deletion are permitted, and to
what extent?
History and auditability (L4):Are events such as acquisition,
registration, viewing, processing, transfer, redistribution, and
deletion recorded so that they can be traced and verified
afterward?
The four layers verify different objects, namely the parties
(L1), the data themselves (L2), the permitted actions (L3),
and the events over time (L4), and cannot substitute for one
another. Data that have not been tampered with cannot be used
with confidence if they are sold by an unauthorized entity
(L2 holds but L1 does not). Data received from a legitimate

provider and verified as untampered may still not be usable for
AI training if the license does not permit it (L1 and L2 hold but
L3 does not), or cannot be relied upon for quality judgment
if the method of acquisition and the processing history are
unknown (L1 and L2 hold but L4 does not).
A point to emphasize is the existence of a boundary of
what can be certified. The certification of L2 by hash values,
electronic signatures, e-seals, and timestamps gives evidence
that a given piece of data was issued by a specific entity and
has not been altered since. It does not, however, guarantee that
the content of the data agrees with real-world facts. Evaluating
the correctness of content requires combining evidence that
belongs to the other layers, such as the managing entity (L1),
the declared purpose and scope of use (L3), and calibration
records, installation conditions, and measurement methods
(L4), and judging it against the intended use.
What the four-layer framework aims at is therefore not a
“guarantee of correctness” but assembling the evidence needed
for judgment and making previously invisible risks assessable.
Trustworthy data are not data that contain no errors; they are
data whose origin and limitations can be verified and which
can be reasonably evaluated against their intended use. This
is our answer to RQ1.
B. DCGO as a Trust Anchor
Of the four layers, L1 and L2 have been realized individu-
ally by existing technologies such as corporate identifiers and
electronic signatures, and L3 and L4 have been handled par-
tially by contracts and operations. As described in Section I-A,
however, these are established separately by each operator,
and in collaboration across domains and borders it is difficult
for the trading parties alone to establish them every time:
providers fear use beyond the intended purpose and leakage,
and users doubt authenticity, quality, and rights. Under this
two-sided information asymmetry, the higher the quality of
data, the less likely they are to reach the market, and the
market turns into a market for lemons.
DCGO is a proposal in which a third party independent of
the trading parties verifies and certifies the four layers against
common criteria. We call it atrust anchorin the sense that
evidence verified once by DCGO is recognized, in the same
form and at the same assurance level, across the markets and
data spaces that refer to DCGO; the certification of the four
layers is thereby bundled into “portable trust” that accom-
panies a transaction wherever it takes place. Although the
name “credit guarantee” may evoke monetary compensation
for losses, the core of the proposal is to neutrally verify the
evidence and rules required for data trading and thereby raise
the trustworthiness of transactions.
Figure 1 shows the architecture at the present stage. DCGO
is placed between data providers and users, and at its core
is a notary-like function that certifies (i) the authenticity of
entity (L1), (ii) the authenticity and integrity of data (L2),
and (iii) the unity of the data and the contractual conditions
of their use (L3). Combined with this core are supporting
functions: (iv) a data catalog (registration and search), (v)
custody, (vi) settlement, and (vii) support by AI agents for
discovery, comparison of conditions, negotiation, and receipt.
The audit log and ledger (L4) record the operations of all
these functions, so that any certification can be traced back
to the evidence on which it was based. Data and payments
themselves flow through existing marketplaces, data spaces,
or bilateral exchange, not through DCGO. “Notary” here does
not refer to the notary public system under current law but to
a notary-like function that technically and neutrally certifies
authenticity and related properties.
Three distinctions are important for understanding DCGO.
First, DCGO is not a data repository. Rather than aggregating
all data centrally, a federated design is assumed in which each
participant keeps its data and only certification information and
metadata are linked; for highly confidential data, conditions
can be confirmed without disclosing the content. Second,
DCGO is not a trading site. Before a market function that
attaches a price and sells, a notary-like function that verifies
who can provide what under which conditions is needed.
Without this foundation of trust, high-quality data will not
gather even with market functions in place. Third, DCGO
does not replace existing data infrastructures. It is a layer that
superimposes a cross-cutting trust verification function on the
collaborations established in each industry and use case and
on the mechanisms that connect them.
In summary, what DCGO can support is the verification and
certification of evidence for L1 to L4 and its portability across
markets; guaranteeing the correctness of content, storing data,
and brokering sales are outside its scope, as is judging whether
the data fit a particular purpose, which requires the user’s
context. This is our answer to RQ2. Section V examines the
validity of this positioning by showing which layers play roles
that cannot be substituted by the others (RQ3).
IV. MODELS OFDCGOFORSIMULATION
A. Objective
To answer RQ3, that is, under what conditions DCGO
works effectively compared with existing trading models, we
ask whether using DCGO is beneficial in the long run for
both buyers and sellers even after paying its fees, and we
identify the parameter region in which this holds. “Beneficial”
has two meanings. For buyers, it means that the net payoff
exceeds that under the existing trading model on average
over a sufficiently long period. For sellers, it means that an
honest seller obtains more profit by joining DCGO than by
not joining, so that joining is chosen voluntarily. We verify
the former with a buyer-side simulation and the latter with
a seller-side simulation, and define the region in which both
hold as thecondition under which DCGO works. By removing
the functions of DCGO one at a time, we also identify which
of the four layers is responsible for which effect.
We use agent-based simulation rather than equilibrium
analysis because the market considered here has dynamic
properties that are difficult to treat analytically: participants
turn over, buyers learn from finite experience, and a single
fraud harms many buyers at once. The simulation is not

calibrated with real data; what it provides is a qualitative
condition, namely which parameters matter and in which
direction, rather than a quantitative prediction.
B. The Law Merchant Model and Data-Specific Extensions
We model the market after the Law Merchant model [22],
which explains why honest trade was sustained at medieval
fairs where trading partners changed frequently. A third party
without enforcement power keeps records of past cheating and
answers queries before a trade. If the cycle ofquery, record,
and excludeis individually rational, honest trade is sustained
even in a large market of one-shot encounters where bilateral
reputation does not work. The ledger of DCGO plays this role
in data trading.
To this model, we add three properties specific to data as
a good. First, fraudulent data cannot be recognized until they
are used: tampering, forged provenance, and defective rights
clearance surface only later and only partially, as malfunctions
of analysis results or trained models. We represent this as
imperfect ex-post detection, in which fraud is discovered after
the trade only with probabilityδ. The smallerδ, the fewer
frauds are recorded and the weaker record-based exclusion
becomes. This corresponds to a credence good [25].
Second, an excluded fraudulent seller can return with a new
account. Unlike a medieval merchant, whose identity is fixed,
a new ID is cheap to obtain in digital trading. We represent
this as the social cost ofcheap pseudonyms[24]: an excluded
fraudulent seller returns as a new ID with probabilityρ. This
property separates trading models without identity verification
from DCGO, which blocks re-entry.
The third is thenon-rivalry of harm. Because data are easy
to copy, a single undetected fraudulent seller can harm many
buyers in the same period. We place no upper limit on the
quantity a seller can supply, so that multiple buyers can choose
the same seller at once, and measure this byvictims per fraud.
This property raises the social cost of delayed detection and
hence the value of verification before the trade.
Finally, DCGO verifies the authenticity of data before the
trade, a function absent from the Law Merchant model that
corresponds to acertification intermediary[23], a third party
that inspects sellers’ quality and discloses it to buyers. In
our model, pre-verification detects and excludes fraudulent
data before the trade with probabilityp det. DCGO is thus
the composition of two classical third-party mechanisms,
the law merchant (records and queries) and the certification
intermediary (inspection before the trade), with querying and
recording automated through its catalog and ledger rather than
left to the voluntary action of merchants. The ablation study
separates what each mechanism contributes and what happens
when either is missing.
C. Trading Models
We represent each trading model by the presence or absence
of three functions of DCGO: sharing of fraud records among
buyers (L4), identity verification that binds records to a seller
and blocks re-entry under a new ID (L1), and pre-verification
TABLE I
TRADING MODELS COMPARED AND THE FUNCTIONS EACH ONE HAS
Trading model
Sharing of fraud
records (L4)
Identity
verification (L1)
Pre-verification
(L2)
Bilateral× × ×
DCGO✓ ✓ ✓
DCGO−ID✓×✓
DCGO−Check✓ ✓×
of data before the trade (L2). The trading model with none
of the three is calledBilateral, in which there is no third
party and a buyer judges its counterpart only from its own
experience, and the one with all three is calledDCGO. For
the ablation study we also setDCGO−ID, which removes
only identity verification, andDCGO−Check, which removes
only pre-verification (Table I). Because the four trading models
differ only in these functions within the same model, the effect
of each function can be isolated.
Rights and conditions of use (L3) is not handled, because
L1, L2, and L4 all matter for whether a buyer can trust a
seller at the time of the trade, whereas L3 concerns the buyer’s
behavior after the trade, such as use beyond the intended
purpose, and requires a different model that includes post-
purchase behavior, which we leave as a future extension.
Who bears the usage fee is a design variable: a fee borne by
buyers raises their participation threshold directly, whereas a
fee borne by sellers may reduce the incentive of honest sellers
to join. Buyers bear the fee in the buyer-side simulation, and
sellers bear it in the seller-side simulation, where buyers pay
only a small feec b for certified data.
D. Agent Model
The market hasNsellers andMbuyers. Sellerjhas a
fixed typeθ j ∈ {0,1}: afraudulent seller(θ j = 1) always
sells fraudulent data and anhonest seller(θ j = 0) always
sells correct data, and the share of fraudulent sellers isϕ. A
buyer obtains valuevfrom good data and suffers lossLfrom
fraudulent data. The pricepis fixed, andL,p, and the DCGO
feecare expressed as ratios tov= 1.
In every round, each seller leaves the market with prob-
abilityµ s and each buyer with probabilityµ b, and they are
replaced by the same number of new entrants: a new seller
is fraudulent with probabilityϕ, a new buyer starts with no
trading experience, and the records concerning a departed
seller (blacklist entries and detection) leave with it. This
turnover represents the Law Merchant situation in which the
chance of meeting the same partner again is small.
A trading model is represented by a tuple(s, ι, π, c): three
binaryswitchescorresponding to the three functions in Sec-
tion IV-C, namely sharing of fraud recordss(L4), identity
verificationι(L1), and pre-verificationπ(L2), each equal to
1if the trading model has the function and0otherwise, and the
usage feec≥0that a buyer pays for each trade. If a buyer
never receives fraudulent data, its payoff from one trade is
v−p−c, which we call thetheoretical upper boundof the

buyer’s net payoff (0.60for Bilateral withc= 0and0.55for
DCGO withc= 0.05).
E. A Simulation Round
Each roundtconsists of the following seven steps.
(Step 1) Turnover.Sellers and buyers are replaced with the
probabilities described above.
(Step 2) Participation decision.Each buyeriholds asubjec-
tive fraud rate˜r t i , its estimate of the share of fraudulent data
in the market, formed from the frequency of fraud detected
in its own past trades and, when records are shared, in those
of other buyers. The buyer participates if the expected payoff
from a single trade is positive:
(1−˜r)v−˜rL−p−c >0⇐ ⇒˜r < τ≡ v−p−c v+L ,(1)
whereτis the threshold fraud rate above which a buyer stops
participating; the higher the feec, the lower the threshold. A
non-participating buyer re-enters on a trial basis with a small
probabilityε, so that a buyer that once left can notice that the
market has improved.
(Step 3) Seller choice.A participating buyer chooses one
seller uniformly at random among the sellers not on the
blacklistB t ij it can refer to. There is no upper limit on the
quantity a seller can supply, so several buyers may choose the
same seller in the same round and, if it is fraudulent, all of
them suffer the loss (non-rivalry of harm).
(Step 4) Pre-verification (DCGO only).If the chosen seller
is fraudulent, the fraud is detected before the trade with
probabilityp det and the seller is immediately blacklisted.
Because verification is performed regardless of whether the
trade is completed, the buyer pays the feeceven when fraud
is detected.
(Step 5) Payoff.A buyer that completes a trade receivesv−
p−cfor good data and−L−p−cfor fraudulent data; a
buyer blocked by pre-verification receives−c.
(Step 6) Ex-post detection and memory update.If the
trade is completed and the seller is fraudulent, the fraud is
discovered with probabilityδ; the seller is blacklisted and
the buyer’s subjective fraud rate is updated. The switchs
determines whether these records are shared among all buyers
or remain private to the buyer that detected it. With the shared
blacklist and fraud rate written asb t j andr t, and the private
ones of buyeriasb t ij andr t i, buyerirefers to
Bt ij =s bt j + (1−s)b t ij,˜r t i =s rt + (1−s)r t i.(2)
Withs= 0, a buyer can avoid only the sellers by which it
was itself harmed.
(Step 7) Pseudonym reset.A blacklisted fraudulent seller re-
enters the market as a new ID with probabilityρin trading
models without identity verification (ι= 0); with identity
verification (ι= 1), it is permanently excluded.
F . Metrics
Thebuyer’s net payoffis the payoff per buyer per round,
that is, the value of good data minus the loss from fraudulent
data, the price, and the usage fee. Theparticipation rateis
the share of buyers that participated in that round. Thecon-
tamination rateis the share of fraudulent data among the data
purchased in that round.Victims per fraudis the number of
buyers harmed per seller that sold fraudulent data in that round,
which captures the spread of harm due to the copyability of
data. In the seller-side simulation we additionally observe the
share of honest sellers that are certified (theadoption rate)
and the profit per honest seller per round.
G. Buyer-Side and Seller-Side Simulations (Sim 1 and Sim 2)
To make the results easier to interpret, we run two simu-
lations in which one side is fixed. InSim 1, the buyer-side
simulation, the types and behavior of sellers are fixed, only
buyers learn and decide following Section IV-E, the trading
model is applied uniformly to the whole market, and the usage
fee is paid by buyers.
InSim 2, the seller-side simulation, buyers are fixed and a
voluntary DCGO certification is installed on top of a Bilateral
base market, in which a buyer avoids only the sellers whose
fraud it has itself noticed, records are not shared, pseudonym
resets are not prevented, and buyers are replaced at rateµ b
with empty blacklists. A seller that joins DCGO undergoes
identity verification (and cannot re-join once revoked) and pre-
verification at every sale, pays a feec s per unit sold, and in
exchange sells certified data at a price premiumη. Buyers
choose among certified sellers whenever they exist and payc b
for certified data. An honest seller with production costkearns
p−kper unit if uncertified andp+η−c s−kif certified. Sellers
do not optimize the decision to join; each seller compares its
average profit over the last 10 rounds with that of a randomly
chosen seller and imitates the membership status of the more
profitable one. A fraudulent seller may also imitate joining,
but it is stopped by pre-verification at its first sale and loses
its certification. Newly entering sellers start uncertified.
H. Experimental Settings
Table II lists the definitions and default values of the
parameters used in the simulations. One run consists of 300
rounds, and 30 runs are performed with different random
seeds. Reported values are averages over the last 100 rounds,
excluding the initial transient, across the 30 runs.
V. RESULTS ANDDISCUSSION
A. Buyer-Side Simulation (Sim 1)
Under Bilateral, buyers lose from the early rounds on
(Table III, Fig. 2(a)). The contamination rate stays at about
30%, nearly equal to the share of fraudulent sellersϕ= 0.3
(Fig. 2(c)): because of seller turnover and pseudonym resets,
the market as a whole cannot accumulate the knowledge of
which sellers are fraudulent, even though each buyer builds its
own blacklist. Under DCGO, in contrast, the buyer’s payoff
almost reaches the theoretical upper bound of0.55. Even after
paying the usage fee, it is0.75higher than under Bilateral,
and the contamination rate is kept down to0.1%. Notably,
the participation rate under Bilateral stops falling at 74%

TABLE II
PARAMETERS AND THEIR DEFAULT VALUES
Symbol Meaning Default
N,MNumber of sellers, number of buyers 100, 200
ϕShare of fraudulent sellers among sellers 0.3
δProbability that a buyer notices fraud after buying fraudulent data 0.3
ρProbability that a blacklisted fraudulent seller re-enters via a pseudonym reset 0.2
µs,µ b Share of sellers / buyers replaced by new participants per round 0.02, 0.02
v,L,pValue of good data, loss from fraudulent data, price (v= 1as the unit) 1, 2, 0.4
pdet Probability that pre-verification blocks fraudulent data 0.9
cUsage fee of the trading model, paid by the buyer per trade (Sim 1 only) Bilateral: 0, DCGO: 0.05
εProbability that a non-participating buyer participates on a trial basis (Sim 1 only) 0.05
kCost for an honest seller to produce one unit of good data; 0 for fraudulent sellers (Sim 2 only) 0.2
ηPrice premium of certified data (Sim 2) 0.10
cs,c b DCGO fees:c s is paid by the seller,c b by the buyer per unit of certified data (Sim 2 only) 0.05, 0.05
0 100 200 300
Round
−0.50
−0.25
0.00
0.25
0.50
Buyer payoff
(a) Buyer payoff
0 100 200 300
Round
60
70
80
90
100Participation [%]
(b) Participation
0 100 200 300
Round
0
10
20
30Bad data bought [%]
(c) Contamination
0 100 200 300
Round
2
4
6Victims per fraud
(d) Victims per fraud
Bilateral
DCGO
DCGO-ID
DCGO-Check
Fig. 2. Time series by trading model: (a) buyer’s net payoff, (b) participation rate, (c) contamination rate, and (d) victims per fraud. Solid lines are the means
over 30 seeds; bands are mean±standard deviation.
0.05 0.1 0.2 0.3 0.4 0.5 0.6
Share of fraudulent sellers ϕ
0.0
0.05
0.1
0.15
0.2
0.3
DCGO fee c (÷ v)
+0.16 +0.28 +0.58 +0.80 +0.97 +1.03 +1.07
+0.11 +0.23 +0.53 +0.75 +0.92 +0.98 +1.02
+0.06 +0.18 +0.48 +0.70 +0.87 +0.93 +0.97
+0.01 +0.13 +0.43 +0.65 +0.82 +0.88 +0.92
-0.04 +0.08 +0.38 +0.60 +0.77 +0.83 +0.87
-0.14 -0.02 +0.28 +0.50 +0.67 +0.73 +0.77
−1.00
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
1.00
Buyer payoff: DCGO − Bilateral
Fig. 3. Difference in the buyer’s net payoff. Darker blue means DCGO is
more favorable; darker red means Bilateral is more favorable.
(Fig. 2(b)): buyers notice only 30% of fraudulent data after
the fact and cannot realize that they are losing. In a market
for data in which fraud is hard to notice, a high participation
rate is therefore not evidence that the market is sound; the
market must be assessed by both participation and payoff.
Figure 3 shows the difference in the buyer’s net payoff
between DCGO and Bilateral for each combination ofϕ
and the usage feec. DCGO is inferior only when there are
almost no fraudulent sellers (ϕ≤0.1)andthe fee is high
(c≥0.2). In almost the entire remaining region DCGO yields
the higher payoff, by+0.50atϕ= 0.3even whenc= 0.3.
The difference increases almost linearly inϕand decreases
almost linearly inc. In the sensitivity analysis (Fig. 4), the
DCGO payoff stays within0.53–0.55whichever ofϕ, the
seller turnoverµ s, the ex-post detection probabilityδ,ρ, and
the pre-verification accuracyp det is varied; the only parameter
that moves it is the feec. The Bilateral payoff, in contrast,
turns negative at aroundϕ≈0.2and remains negative even
when fraud is always noticed (Fig. 4(b)) or pseudonym resets
are absent, and it falls as the buyer turnoverµ b rises (Fig. 4(c)),
because new buyers do not know who is fraudulent.
In summary, the Bilateral payoff declines as the market en-
vironment deteriorates, whereas the DCGO payoff is constant
regardless of the environment, with its upper bound lowered
only by the fee. The conditions under which DCGO works are
thus governed by two quantities, the strength of the incentive
to cheatϕand the cost of certificationc. This is the buyer-side
answer to RQ3.
The ablation study (Fig. 4(e)–(g)) compares DCGO,
DCGO−ID, and DCGO−Check asρis varied. Atρ= 0,

0.0 0.1 0.2
Seller turnover μs
0.0
0.5Buyer payoff
(a)
0.5 1.0
Ex-post detection δ
(b)
0.0 0.1 0.2
Buyer turnover μb
(c)
0.6 0.8 1.0
Pre-check accuracy pdet
(d)
0.0 0.5 1.0
Pseudonym reset ρ
0.0
0.2
0.4Buyer payoff
(e)
0.0 0.5 1.0
Pseudonym reset ρ
0
2
4Bad data bought [%]
(f)
0.0 0.5 1.0
Pseudonym reset ρ
1
2
3Victims per fraud
(g)
Bilateral
DCGO
DCGO-ID
DCGO-Check
Fig. 4. Sensitivity analysis of Sim 1. Buyer’s net payoff under Bilateral and DCGO when (a) the seller turnoverµ s, (b) the ex-post detection probabilityδ,
and (c) the buyer turnoverµ b are varied one at a time from their default values, and (d) under DCGO and DCGO−ID when the pre-verification accuracy
pdet is varied. (e) Buyer’s net payoff, (f) contamination rate, and (g) victims per fraud as functions of the pseudonym-reset probabilityρ.
0.0 0.05 0.1 0.15 0.2 0.3
Price premium η
0.0
0.02
0.05
0.1
0.15
0.2
Seller fee cs
+0.15 +0.29 +0.42 +0.55 +0.68 +0.95
+0.10 +0.23 +0.37 +0.50 +0.63 +0.89
+0.02 +0.15 +0.29 +0.42 +0.55 +0.81
-0.11 +0.02 +0.15 +0.29 +0.42 +0.68
-0.24 -0.11 +0.02 +0.15 +0.29 +0.55
+0.00 -0.24 -0.11 +0.02 +0.15 +0.42
(a) Honest-seller profit gain
0.0 0.05 0.1 0.15 0.2 0.3
Price premium η
0.0
0.02
0.05
0.1
0.15
0.2
Seller fee cs
+0.77 +0.72 +0.68 +0.63 +0.59 +0.49
+0.77 +0.72 +0.68 +0.63 +0.59 +0.49
+0.77 +0.72 +0.68 +0.63 +0.59 +0.49
+0.77 +0.72 +0.68 +0.63 +0.59 +0.49
+0.77 +0.72 +0.68 +0.63 +0.59 +0.49
-0.01 +0.72 +0.68 +0.63 +0.59 +0.49
(b) Buyer payoff gain
0.0 0.05 0.1 0.15 0.2 0.3
Price premium η
0.0
0.02
0.05
0.1
0.15
0.2
Seller fee cs
(c) Both sides better off
−0.75
−0.50
−0.25
0.00
0.25
0.50
0.75
DCGO − none
−0.6
−0.4
−0.2
0.0
0.2
0.4
0.6
DCGO − none
Fig. 5. For each combination of the price premiumη(horizontal axis) and the seller-side feec s (vertical axis): (a) gain in the profit of honest sellers, (b)
gain in the buyer’s net payoff, and (c) combinations in which both are positive. Gains are differences from the market without DCGO.
when the identity of sellers is completely fixed, DCGO−ID
achieves the same outcome as DCGO: this is the world of the
Law Merchant model, in which fixed identity was an implicit
premise and record sharing alone sustains honest trade. As
ρincreases, however, the payoff of DCGO−ID decreases
monotonically, from0.48atρ= 0.2to0.39atρ= 0.5
and0.30atρ= 1, and the contamination rate rises from
0.1%to4.1%: under cheap pseudonyms [24], the exclusion
of fraudulent sellers remains incomplete without identity ver-
ification, even with record sharing and pre-verification. Under
DCGO and DCGO−Check, which have identity verification,
none of the payoff, the contamination rate, and the number of
victims changes withρ. Identity verification is the function that
effectively setsρto0. Without it the history-and-auditability
layer cannot keep functioning. Among the four layers, L1 is
therefore a prerequisite for L4.
A further result concerns the number of victims per fraud
(Table III, Fig. 2(d)), which is larger in trading models that
have fewer undetected fraudulent sellers:1.9under Bilateral
versus3.0under DCGO−Check. The more record sharing
shrinks the set of fraudulent sellers not yet blacklisted, the
more buyers concentrate on the few that remain, and because
data can be copied without limit, one fraudulent seller sells to
TABLE III
COMPARISON OF TRADING MODELS WITH THE DEFAULT PARAMETERS
(±IS THE STANDARD DEVIATION ACROSS SEEDS)
Trading model Buyer’s net
payoff
Contamination
rate
Victims per
fraud
Bilateral−0.21±0.0529.7% 1.9
DCGO+0.54±0.000.1% 1.2
DCGO−ID+0.48±0.011.0% 1.1
DCGO−Check+0.51±0.011.4% 3.0
all of them in the same round. This is the non-rivalry of harm
added to our model, captured by the victims-per-fraud metric.
Only DCGO and DCGO−ID, which have pre-verification,
keep the number of victims at around one by stopping fraud
before the trade. The pre-verification accuracyp det has almost
no effect on the buyer’s payoff (Fig. 4(d)) but does affect the
number of victims.
Therefore, reducing the number of fraudulent sellers and
reducing the harm caused by a single fraud are distinct
goals: the former is achieved by record sharing and identity
verification, and the latter only by pre-verification. This is why
L2 is necessary among the four layers.

0.2 0.4 0.6
Share of fraudulent sellers ϕ
0
50
100DCGO adoption [%]
(a)
0.00 0.05 0.10 0.15 0.20
Seller fee cs
0
50
100DCGO adoption [%]
(b)
0.00 0.05 0.10 0.15 0.20
Seller turnover μs
0
50
100DCGO adoption [%]
(c)
0.2 0.4 0.6
Share of fraudulent sellers ϕ
2
4
6Honest-seller profit
(d)
honest, certified
honest, all
w/o DCGO
0.00 0.05 0.10 0.15 0.20
Seller fee cs
0.5
1.0Honest-seller profit
(e)
0.2 0.4 0.6
Share of fraudulent sellers ϕ
−1
0
Buyer payoff
(f)
w/ DCGO
w/o DCGO
Fig. 6. Sensitivity analysis of Sim 2: DCGO adoption rate of honest sellers when (a) the share of fraudulent sellersϕ, (b) the seller-side feec s, and (c) the
seller turnoverµ s are varied. Profit of honest sellers as a function of (d)ϕand (e)c s, and (f) buyer’s net payoff as a function ofϕ.
B. Seller-Side Simulation (Sim 2)
Table IV shows that the profit of honest sellers rises from
0.40to0.69(about1.7times), and to0.99(about2.5times)
for certified sellers alone. Adoption spreads through imitation
and settles at 68% of honest sellers. Fraudulent sellers that join
are stopped by pre-verification at their first sale and lose their
certification, so the contamination rate falls from29.5%to
2.1%, and the buyer’s net payoff turns from−0.29to+0.39.
The sellers’ gain is not carved out of the buyers’ share: the
loss caused by fraudulent data disappears from the market as
a whole, and that amount is divided between the two sides
through the premiumη.
As the share of fraudulent sellersϕincreases
(Fig. 6(a)(d)(f)), the profit of certified honest sellers
reaches2.0atϕ= 0.5, five times the level without DCGO,
whereas the adoption rate declines and stays at 23% at
ϕ= 0.6: the more fraudulent sellers there are, the greater
the value of joining, but the fewer the opportunities to meet
a profitable member to imitate. This dilemma, that the more
valuable the market, the harder it is for DCGO to spread
naturally, rebounds on buyers: atϕ= 0.6a contamination
rate of 26% remains and the buyer’s payoff is−0.28even
with DCGO (Fig. 6(f)), a large improvement over−1.18
without DCGO but still a loss. Buyers benefit only once
adoption on the seller side has spread sufficiently.
The condition under which both sides benefit is simple: the
premiumηroughly exceeds the feec s (Fig. 5(c)). The sellers’
gain is almost proportional toη−c s (Fig. 5(a)), and the buyers’
gain, although it decreases withη, is positive wherever DCGO
has spread and still+0.49atη= 0.3(Fig. 5(b)). The boundary
of the region is therefore set by the seller-side condition: as
long as the fee can be passed on to the price, buyers accept
a premium of up to aboutη= 0.3, which is funded by the
payoff difference of about0.75measured in Sim 1.
There are, however, two side effects and a diffusion con-
dition. First, because buyers prefer certified sellers, uncerti-
fied honest sellers (mainly new entrants) sell almost nothing
(Table IV), so the gap between members and non-members
becomes extremely large. Second, once DCGO has spread,
TABLE IV
MARKETS WITHOUTDCGO (BILATERAL)VERSUS VOLUNTARYDCGO
DCGO
Adoption
rate
Honest-seller profit
(all / certified / uncertified)
Contamination
rate
Buyer’s
net payoff
w/o n/a 0.40 / n/a / 0.40 29.5%−0.29
w/ 68% 0.69 / 0.99 / 0.03 2.1%+0.39
the adoption rate stays at 68% even whenc s is raised to0.2
(Fig. 6(b)), although the profit of certified sellers (0.39) then
falls below the level without DCGO (0.40) (Fig. 6(e)); sellers
are locked in because uncertified sellers cannot sell, which
implies that the fee must be restrained by governance rather
than by market competition. Third, diffusion has a critical
mass: even under the default setting, in 2 of the 30 seeds
the initial members (5%) were lost through turnover before
imitation could multiply them, and with fast seller turnover
(µs ≥0.05) this becomes the norm (Fig. 6(c)), so that prior
registration of large providers or support at entry is likely to
be necessary in markets with intense entry. This is the seller-
side answer to RQ3; together with the buyer-side answer, it
gives the conditions under which DCGO works.
VI. CONCLUSION
A. Summary
This paper took up the Data Credit Guarantee Organization
(DCGO), which performs third-party verification and certifi-
cation, as a mechanism that makes trust, previously closed
within each operator, portable across markets, and addressed
three research questions. For RQ1, trust in data is a state in
which four mutually non-substitutable layers can be answered:
the authenticity of entity (L1), the authenticity and integrity
of data (L2), rights and conditions of use (L3), and history
and auditability (L4); trustworthy data are not error-free data
but data whose origin and limitations can be verified against
their intended use. For RQ2, DCGO is a trust anchor in
which a third party verifies and certifies the evidence of the
four layers and makes it portable across markets and data
spaces; guaranteeing the correctness of content, storing data,
and brokering sales are outside its scope. For RQ3, the DCGO

payoff on the buyer side stays close to the theoretical upper
bound regardless of the market environment and falls below
bilateral trading only when fraudulent sellers are almost absent
and the fee is high; on the seller side, honest sellers join
voluntarily and both sides gain whenever the price premium
exceeds the fee, with lock-in and a critical mass for diffusion
as side effects.
The conditions under which DCGO works are thus de-
scribed by two axes, the strength of the incentive to cheat
and the cost of certification, and among the four layers the
authenticity of entity and pre-verification play roles that record
sharing alone cannot substitute. The priority in introducing
DCGO is therefore not to upgrade market functions but to
establish a foundation of trust that includes identity verification
and pre-verification, and to keep its cost, through governance,
at a level that providers and users can accept.
B. Limitations and Future Work
We kept the data price fixed, because endogenous pricing
would mix price formation with the formation and collapse
of trust and make it harder to read which function of which
trading model is at work. Our model also limits fraud to
a single kind, namely data that cause a loss to the buyer;
distinguishing fraud in authenticity, which DCGO targets, from
errors in content, and modeling the propagation of contami-
nation to secondary data, remain future work. In addition, we
fixed either buyers or sellers; moving both sides at the same
time and examining buyers’ voluntary choice of certification
are left for the future.
Among the four layers, rights and conditions of use (L3)
was not handled. Violations of L3 appear as the buyer’s
behavior after the trade, such as use beyond the intended
purpose or redistribution, so buyers must be modeled as agents
that keep acting after purchase, and the effect of usage rights
certificates and of the detection and revocation of violations
must be evaluated. The support by AI agents for discovery,
comparison of conditions, and negotiation (Section III-B)
corresponds to the part of the trading procedure that we
fixed; incorporating it would show how DCGO certification
is referred to in agreements between agents. Modeling L3 and
introducing AI agents are the next steps toward covering all
four layers.
Our simulation also targets a single market and does not
model the cross-market portability of trust itself; a model with
multiple markets in which DCGO certifications are or are not
mutually recognized is future work. Finally, the parameters
are not calibrated with real data, so our findings are limited to
qualitative conditions. The next step is to obtain the fraud rate,
the time to detection, and certification costs from the planned
demonstrations and to evaluate the applicability of DCGO to
specific industries and regions quantitatively.
ACKNOWLEDGMENT
This study was supported by the Japan CSTI BRIDGE
Program with MIC, METI, and Digital Agency, and by JST
PRESTO Grant Number JPMJPR2369.
REFERENCES
[1] Stanford Institute for Human-Centered Artificial Intelligence, “Artificial
Intelligence Index Report 2025,” Stanford University, 2025.
[2] Grand View Research, “Data Marketplace Platform Market Size, Share
& Trends Analysis Report, 2025–2030,” https://www.grandviewresearch.
com/industry-analysis/data-marketplace-market-report, Nov. 2024.
[3] Digital Agency, Japan, “Data Free Flow with Trust (DFFT),” https://
www.digital.go.jp/en/policies/dfft.
[4] Cabinet Office, “Programs for Bridging the gap between R&D and
the IDeal society (society 5.0) and Generating Economic and social
value (BRIDGE): FY2026 adopted projects,” https://www8.cao.go.jp/
cstp/bridge/saitaku r8.html (in Japanese).
[5] Amazon Web Services, “AWS Data Exchange,” https://aws.amazon.com/
data-exchange/.
[6] Snowflake Inc., “Snowflake Marketplace,” https://www.snowflake.com/
en/product/features/marketplace/.
[7] Catena-X Automotive Network e.V ., “Catena-X: The automotive net-
work,” https://catena-x.net/.
[8] Catena-X Automotive Network e.V ., “Catena-X Operating Model,”
2023.
[9] EverySense Japan, Inc., “EverySense Pro,” https://data-ex.every-sense.
com/ (in Japanese).
[10] Kyoto Smart City Promotion Council, “Kyoto Data Marketplace,” https:
//data-market.smart-kyoto.or.jp/ (in Japanese).
[11] Data Society Alliance, “DSA starts a demonstration experiment of
data trading using data usage rights,” https://prtimes.jp/main/html/rd/p/
000000005.000039966.html (in Japanese).
[12] International Data Spaces Association, “Dataspace Protocol,” https://
docs.internationaldataspaces.org/ids-knowledgebase/dataspace-protocol.
[13] Gaia-X European Association for Data and Cloud AISBL, “Gaia-X Trust
Framework,” 2024. https://docs.gaia-x.eu/.
[14] Information-technology Promotion Agency, Japan, “Open Data Spaces,”
https://www.ipa.go.jp/en/digital/opendataspaces/.
[15] Data Society Alliance, “Agreement to jointly promote
the dataspace technical concept as ‘Open Data Spaces’,”
https://en.data-society-alliance.org/press-release/12533/.
[16] “IEEE Standard for a Data-Trading System: Overview, Terminology, and
Reference Model,” IEEE Std 3800-2024, Dec. 2024.
[17] L. Moreau and P. Missier, Eds., “PROV-DM: The PROV Data Model,”
W3C Recommendation, Apr. 2013.
[18] T. Gebru et al., “Datasheets for datasets,”Commun. ACM, vol. 64, no.
12, pp. 86–92, 2021.
[19] R. Agrawal and J. Kiernan, “Watermarking relational databases,”28th
Int. Conf. Very Large Data Bases, 2002, pp. 155–166.
[20] Y . Uchida, Y . Nagai, S. Sakazawa, and S. Satoh, “Embedding water-
marks into deep neural networks,”ACM Int. Conf. Multimedia Retrieval,
2017, pp. 269–277.
[21] G. A. Akerlof, “The market for ‘lemons’: Quality uncertainty and the
market mechanism,”Quarterly Journal of Economics, vol. 84, no. 3, pp.
488–500, 1970.
[22] P. R. Milgrom, D. C. North, and B. R. Weingast, “The role of institutions
in the revival of trade: The law merchant, private judges, and the
champagne fairs,”Economics and Politics, vol. 2, no. 1, pp. 1–23, 1990.
[23] A. Lizzeri, “Information revelation and certification intermediaries,”
RAND Journal of Economics, vol. 30, no. 2, pp. 214–231, 1999.
[24] E. J. Friedman and P. Resnick, “The social cost of cheap pseudonyms,”J.
Economics & Management Strategy, vol. 10, no. 2, pp. 173–199, 2001.
[25] M. R. Darby and E. Karni, “Free competition and the optimal amount
of fraud,”J. Law and Economics, vol. 16, no. 1, pp. 67–88, 1973.
[26] J. Pei, “A survey on data pricing: From economics to data science,”
IEEE Trans. Knowl. Data Eng., vol. 34, no. 10, pp. 4586–4608, 2022.
[27] A. Agarwal, M. Dahleh, and T. Sarkar, “A marketplace for data: An
algorithmic solution,”ACM Conf. Economics and Computation, 2019.
[28] K. Yamamoto and T. Hayashi, “Designing reputation systems for manu-
facturing data trading markets: A multi-agent evaluation with Q-learning
and IRL-estimated utilities,”IEEE Int. Conf. Big Data, 2025.
[29] J. Sashihara, Y . Fujita, K. Nakamura, M. Kuwahara, and T. Hayashi,
“LLM-based multi-agent system for simulating strategic and goal-
oriented data marketplaces,”IEEE Int. Conf. Big Data, 2025.
[30] J. Sashihara, Y . Fujita, K. Nakamura, M. Kuwahara, and T. Hayashi, “Do
data markets grow or decline? Institutional dynamics explored through
LLM-based multi-agent simulation,”12th Int. Conf. Computational
Social Science, 2026.
