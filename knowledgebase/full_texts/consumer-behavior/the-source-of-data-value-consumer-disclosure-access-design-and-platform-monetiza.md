---
title: 'The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization'
url: https://arxiv.org/abs/2610.22864
category: consumer-behavior
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Hexiao Liu
- Lijian Lu
- Mingzheng Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.22864
pages: 47
chars: 145289
fetched_at: '2026-11-08T13:18:03+00:00'
kb_version: 1
---

# The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization

The Source of Data Value: Consumer Disclosure, Access
Design, and Platform Monetization
Hexiao Liu
School of Management, Zhejiang University, liuhexiao123@163.com
Lijian Lu
HKUST Business School, Hong Kong University of Science and Technology, lijianlu@ust.hk
Mingzheng Wang
School of Management, Zhejiang University, wangmzh@zju.edu.cn
Digital marketplaces increasingly generate revenue from two interrelated activities: transaction commis-
sions and seller-facing data services. A seller may purchase data to boost revenue or to avoid competing
with an informed rival. This study investigates how consumer disclosure rights influence these motives and
the platform’s incentive to provide data. We develop a game-theoretic model of a commissioned platform,
two differentiated sellers, and privacy-sensitive consumers. The platform’s data value arises from asales-
revenue effectdue to bilateral data use and acompetition-threat effectstemming from asymmetric access.
Under mandatory collection, the platform can monetize defensive adoption, even if bilateral personalization
decreases seller revenue. Under voluntary disclosure, anonymous purchasing and strictly positive privacy costs
make unilateral disclosure unattractive in the baseline. Exclusive access then yields no usable information,
restoring sellers’ no-data rejection payoffs and eliminating defensive fees. Profitable provision consequently
requires nonnegative bilateral revenue gains. Under full fee extraction, sellers retain their no-data net profits.
This revenue alignment does not ensure welfare improvement: additional transactions can benefit consumers,
whereas segmentation in an already covered market can raise anonymous prices and reduce welfare. A cap
on anonymous offers at their no-data benchmark protects individual consumers and confines positive-mass
provision to the transaction-creation region. Extensions examine access choice, privacy-cost heterogeneity,
imperfect identification, and limited contractual credibility. Platforms should evaluate data services against
both bilateral-use and seller-rejection outcomes. Sellers need to differentiate between revenue improvement
and defensive investments. Regulators should distinguish equal-access rules from effective consumer control
and monitor pricing in anonymous channels. Changes in privacy governance not only affect data availability
but also alter the sources and distribution of its commercial value.
Key words: marketplace operations; personalized pricing; data monetization; consumer disclosure; privacy
governance
History:
1. Introduction
Digital marketplaces intermediate product sales and control information that helps sell-
ers target consumers. Amazon’s Brand Tailored Promotions, for example, enables eligible
1
arXiv:2610.22864v1  [cs.GT]  16 Oct 2026

2Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
brands to offer discounts of 10%–50% to selected audiences, including repeat purchasers,
high-spending customers, and shoppers who have abandoned their carts (Toogood 2026).
Amazon also earns transaction-linked referral fees; its US schedule lists 15% for Home
and Kitchen, Office Products, and Toys and Games (Amazon 2026). These practices place
targeting capabilities and transaction intermediation within the same business. These prac-
tices motivate an operational question:how does consumers’ ability to withhold information
change what competing sellers will pay for a marketplace’s data service?
These considerations are crucial for platform investment, seller profitability, and the
assessment of personalization. Sellers adoption can reflect two motives: improving pricing
to increase revenue, or avoiding the loss they would face if a rival alone obtained access.
A service can therefore attract paying subscribers even when widespread use reduces their
product revenues. For a commissioned marketplace, this creates a potential conflict between
transaction revenue and access fees. A seller can pay to escape an unfavorable continuation
even if universal adoption leaves the industry worse off. Evaluating the service requires
two counterfactuals: bilateral use versus no data, and the outcome a seller faces after
rejecting access. Adoption, conversion, and fee receipts alone cannot distinguish revenue
improvement from defensive expenditure.
Consumer data rights make this distinction consequential beyond the seller’s procure-
ment decision. The GDPR’s consent provisions and California’s rights to opt out of specified
data sales and sharing place different constraints on the use of personal information (Euro-
pean Parliament and Council 2016, California Department of Justice 2026). A common
operational issue is whether consumers can decline a particular use while continuing to
purchase. Effective anonymous purchasing can preserve participation while denying a sole
subscriber usable pricing information, thereby changing the outside option against which
sellers evaluate a data contract. Privacy governance can thus affect not only information
availability but also the contractual basis of data monetization. We isolate this mechanism
where sellers depend on marketplace-provided information, and our governance regimes
are economic benchmarks rather than complete representations of either statute.
1.1. Our Approach and Contributions
We develop a game-theoretic model of a platform that intermediates between two horizon-
tally differentiated sellers, earns an exogenous commission share of product revenue, and
chooses whether to offer a fee-based data service. Subscribers can personalize prices using

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization3
available information; otherwise, they charge uniform prices. Consumers choose entry, dis-
closure, and purchases, accounting for privacy costs. We compare no data collection (NDC),
mandatory data collection (MDC), and voluntary data disclosure (VDD), which preserves
anonymous purchasing. The platform commits to sequential access offers and rejection
continuations, whereas sellers cannot commit to personalized offers before disclosure. Con-
sumers choose entry and disclosure before observing realized uniform prices. The reported
provision regions and welfare comparisons use this timing and the stated equilibrium selec-
tion. Amazon’s promotion tool motivates platform-controlled targeting rather than these
precise contractual and informational assumptions.
Our first contribution is to delineate a platform-specific breakdown of data’s commercial
value. We distinguish thesales-revenue effect—the change in sellers’ product revenue when
both use the data service rather than neither—from thecompetition-threat effect—the
revenue loss in the exclusive-access continuation after rejection, whether due to competition
from an informed rival or reduced consumer participation. This decomposition clarifies
how downstream outcomes determine access fees and commission income. Under MDC,
sufficiently large and enforceable rejection losses can make provision profitable even when
bilateral personalization reduces sellers’ revenue. The commitment analysis separates the
existence of these losses from their extractability: when exclusive access requires a subsidy,
weaker subsidy credibility reduces defensive fee extraction without altering the underlying
revenue states.
Our second contribution establishes when consumer disclosure rights can mitigate the
competition-threat component by altering the informational dynamics associated with uni-
lateral adoption. Under VDD, disclosing to a sole subscriber yields no additional purchasing
surplus but incurs a strictly positive privacy cost. Consumers therefore withhold informa-
tion while retaining anonymous purchasing, restoring the rejecting seller’s no-data revenue.
VDD eliminates the threat effect, so provision requires nonnegative bilateral seller-revenue
gains. Allowing the platform to choose its access structure also leaves exclusive access
with zero incremental monetization value. The substantive contribution is this upstream
consequence of disclosure: consumer control changes the disagreement payoffs supporting
platform contracts, rather than merely reducing the volume of data sold.
Third, we distinguishrevenue alignment from consumer protection. VDD can expand cov-
erage and benefit the platform and consumers in aggregate, while full fee extraction leaves

4Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
each seller at its no-data net profit. In an already covered market, however, the selected seg-
mentation equilibrium can raise anonymous prices and gross seller revenue without creating
transactions, reducing consumer surplus and welfare. An enforceable cap on anonymous
prices at the no-data benchmark addresses this remaining channel by preserving every
consumer’s no-data purchasing option. With the platform free to withhold the service, the
cap protects consumers and leaves the platform and sellers weakly better off than under
no data, although it can reduce platform profit relative to uncapped VDD. Disclosure
rights and anonymous-price protection therefore address distinct concerns: defensive access
payments and revenue extraction through the anonymous channel.
Extensions examine endogenous access, contractual credibility, strictly positive hetero-
geneous privacy costs, and reveal-or-no-signal identification. A conditional appendix bound
relates threat value to the quantity and quality of usable unilateral information under
explicit regularity assumptions, including restoration of the no-data continuation when
that information disappears. Numerical counterfactuals illustrate provision incentives and
distributional trade-offs; they are model-based scenarios, not estimates of service-specific
demand or causal effects.
1.2. Literature Review
Our analysis connects research on data monetization, personalized-price competition, and
consumer privacy through the role of disclosure in the outside options supporting platform
data contracts.
Data value and platform monetization.A growing body of literature examines how
information changes decisions and competition, making its commercial value depend on
how it is allocated and used (e.g., Bimpikis et al. 2019, Montes et al. 2019, Drakopoulos
and Makhdoumi 2023, Wernerfelt et al. 2025, Guo 2025, Cong and Matsushima 2026, Ray
et al. 2026). For instance, Bimpikis et al. (2019) study information sales to competing firms,
Galperti and Perego (2023) show that privacy constraints can redistribute the marginal
values of data records in an information-design problem, while Sun et al. (2024) empirically
quantify the value of tracking data and data-informed decisions. Concurrently, related
platform studies examine information provision and monetization alongside downstream
operations (e.g., Cosguner et al. 2017, Choe et al. 2024, Liu and Long 2026, Yao 2025,
Bhargava et al. 2026, Yan et al. 2026, Markovich and Yehezkel 2026, Zheng et al. 2026).

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization5
Montes et al. (2019) provide a close contracting antecedent: information prices depend
on the payoff difference between acquiring data and facing an informed rival, and the
supplier compares exclusive with nonexclusive sales. Their consumers incur costs to conceal
information, whereas ours incur costs when information is disclosed and becomes usable.
Combined with anonymous purchasing and noncommitment to personalized offers, this
difference can make unilateral access uninformative and restore the rejecting seller’s no-
data payoff. We use this change in the disagreement outcome to characterize the fees and
provision incentives of a marketplace that also earns transaction commissions.
Hu et al. (2025) already combine commission and information revenue on a platform
that competes with a third-party seller. Choe et al. (2025) study privacy management in
a digital business with usage-based revenue and an exogenous return per unit of shared
data, showing how anonymous purchasing and the revenue structure affect welfare. Our
platform solely intermediates between two independent sellers, and its data-service revenue
is determined by their adoption decisions and disagreement payoffs. The distinguishing
issue is how consumer control changes the returns supporting data provision, rather than
the presence of two revenue sources itself.
Personalized pricing and competition.A classic result is that personalized pricing
intensifies competition and can create a prisoner’s dilemma: each firm prefers to personal-
ize unilaterally, although both would benefit from uniform pricing (e.g., Thisse and Vives
1988, Chen et al. 2001, Choe et al. 2018). Subsequent work shows how coverage, differ-
entiation, targeting accuracy, and consumer heterogeneity change its profitability (Pazgal
and Soberman 2008, Shin and Sudhir 2010, Rhee and Thomadsen 2017, Amaldoss and He
2019, Rhodes and Zhou 2024, Li et al. 2024, 2025a, Du and Ning 2026). Our contribution
is complementary: holding product positions fixed, we study how an information-supplying
platform prices access to the resulting competitive environment. The threat effect is an
explicit disagreement-payoff component of platform monetization, not a claim that defen-
sive personalization is novel. The commissioned intermediary also differs from a stand-alone
data broker because data use affects its operating revenue from product transactions.
A closely related literature examines how consumer data control shapes personalized
pricing. Strategic privacy choices can benefit sellers by segmenting demand and softening
competition (Chen et al. 2020, Kim et al. 2025), but may also intensify competition, induce
price concessions, or degrade information quality (Ali et al. 2023, Bimpikis et al. 2024, Li

6Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
and Li 2023, Cong and Matsushima 2026). Existing studies generally assume that sellers
directly obtain consumer information or acquire it from an external data holder (Montes
et al. 2019, Argenziano and Bonatti 2026). We instead study sellers that depend on the
marketplace for both customer access and the data capability needed to personalize. This
platform dependence is precisely what makes seller-side data provision and monetization
operational decisions rather than simply seller-side pricing choices.
Consumer privacy, disclosure, and anonymity.Recently, a substantial literature
examines how consumers respond strategically to personalized pricing by hiding, eras-
ing, manipulating, or voluntarily disclosing information (Dinev and Hart 2006, Montes
et al. 2019, Ichihashi 2020, Fu et al. 2026, Ke and Sudhir 2023, Kim et al. 2025, Li et al.
2025b, Lin and Strulov-Shlain 2025, Wu 2025). Chen and Zhang (2026) provide the clos-
est unilateral-disclosure mechanism: a sole tracking firm cannot attract privacy-sensitive
consumers through personalized offers because it cannot commit to compensating them
for sunk privacy costs. We build on this mechanism to determine platform access fees and
provision. Their inclusion of privacy-insensitive consumers also clarifies the scope of our
complete threat-elimination result, which maintains strictly positive privacy costs through-
out the population.
Ali et al. (2023) show how verifiable disclosure can amplify competition: relatively flex-
ible consumers reveal information, while those with stronger preferences pool. Their firm-
specific disclosure technology permits selective revelation to different sellers; our consumers
authorize a platform-controlled pricing capability and incur intrinsic privacy costs. We
connect the resulting disclosure choices to upstream access contracts. Li and Li (2023)
instead study data manipulation and its implications for informativeness, collection scope,
and transparency. In our baseline, consumers withhold verifiable information rather than
contaminate it, so the relevant margin is whether a usable pricing signal becomes available.
Two further comparisons distinguish the welfare and operational contributions. Cong
and Matsushima (2026) analyze data management across collection and application mar-
kets, including pricing externalities and price commitments that protect firm profitability.
Our anonymous-price benchmark instead preserves consumers’ no-data purchasing options
within a platform access-contracting environment. Wang et al. (2026) examine a platform
that competes as a first-party seller and designs fuzzy segments in response to anonymous
users. Here, the platform does not sell products, disclosure is endogenous, and the central

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization7
decisions concern data-service provision and access fees. These distinctions explain why
protecting sellers’ rejection payoffs can eliminate defensive monetization without eliminat-
ing consumer harm from segmentation.
Roadmap.The remainder of the paper is organized as follows. Section 2 presents the
marketplace model and data-value framework. Section 3 derives equilibria and stakeholder
outcomes across governance regimes. Section 4 examines extensions and model-based coun-
terfactuals, and Section 5 concludes with managerial and policy implications. Technical
details and proofs appear in the appendix.
2. Model and The General Value of Platform Data
Operational setting and data-governance regimes.A platform connects a unit mass
of consumers with two horizontally differentiated sellers, indexed byi∈ {1,2}. It earns an
exogenous commission rateγ∈[0,1) on product sales. Throughout,sales revenuemeans
gross product revenue before commissions and access fees. A seller’s net profit is its retained
share (1−γ) of this revenue minus its data-service payment. The platform’s profit combines
commissions and access fees; data-service operating costs are normalized to zero in the
baseline. Keeping these quantities distinct is essential: an increase in seller revenue need
not increase the seller’s net profit or social welfare.
The platform controls consumer information that sellers cannot independently reproduce
in the baseline. It can provide a data service that enables subscribing sellers to infer
individual preferences and personalize prices. Nonsubscribers can offer only uniform prices.
The service is a platform-controlled capability, not necessarily a sale of raw records: an
audience interface, permissioned analytics environment, API, or platform-executed offer
could implement the required information access. The maintained economic restriction is
that sellers lack a comparable independent source of the price signal. This is most relevant
to sellers dependent on the marketplace for both customers and targeting information.
The data-governance regime is exogenous; the platform optimizes provision and contracts
within that regime. Underno data collection (NDC), consumer information cannot be used
for the seller-facing service, so sellers rely on anonymous uniform pricing. Undermanda-
tory data collection (MDC), data from entering consumers are available for the service and
consumers cannot preserve a meaningful anonymous purchasing channel. This regime also
represents take-it-or-leave-it data collection in which continued marketplace participation

8Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
effectively requires data use. Undervoluntary data disclosure (VDD), consumers can autho-
rize this use or decline it while continuing to purchase through the uniform-price channel.
“Anonymous” means unidentifiable for the modeled personalized-price decision; it does
not mean that a marketplace can process payment or fulfill orders without any operational
information. When the data service is withheld or neither seller adopts, no pricing-related
privacy cost is incurred and the NDC outcome applies.
Research objectives.We examine three linked decisions: when a platform should provide
a seller-facing data service; how access fees and commissions translate downstream data
use into platform profit; and how consumer disclosure rights change seller adoption, market
coverage, and the distribution of surplus. The first objective distinguishes seller-revenue
improvement from defensive willingness to pay, helping managers assess whether demand
for a data product indicates better marketplace performance. The second identifies when
the platform’s data business supports or undermines its transaction business. The third
evaluates anonymous purchasing as an operational design choice, separating protection
against an informed rival from changes in trade and privacy losses. These objectives require
joint analysis of platform contracts, seller pricing, and consumer choices rather than a fixed
per-record return or an exogenous disclosure rate.
Sequence of events and information.The game separates marketplace access rules
from subsequent pricing and consumer decisions. The platform first chooses whether to
offer the service. If offered under regimeg∈ {MDC,VDD}, it publicly commits to an
offer order, a history-dependent fee schedule, and the access configuration following each
acceptance or rejection. Each seller is first with probability one-half. Labeling the realized
offerees 1 and 2, the schedule isF g = (F g 1 , Fg 2|AC, Fg 2|RE), where seller 1 decides first, and
seller 2 observes that decision and receives the applicable offer. All fees may be real-valued.
In particular, a negative rejection-contingent fee subsidizes activation of exclusive access.
Bilateral adoption is the baseline equilibrium-path configuration; Section 4.1 also allows
exclusive provision on the equilibrium path. Figure 1 summarizes the subsequent decisions.
Consumers do not observe realized uniform prices before entry and disclosure. Informed
sellers subsequently observe the rival’s realized uniform price when choosing personalized
offers, as in the Appendix’s best-response calculations. A hidden uniform-price devia-
tion therefore leaves entry and disclosure fixed, while personalized offers can respond in
asymmetric-access continuations. Rational expectations require anticipated and realized

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization9
Figure 1 Sequence of Events under VDD
Time
Stage 1:
Platform commits to
offer order, contingent
fee scheduleF g, and
fallback access
Stage 2.1:
Seller 1 accepts
or rejects
Stage 2.2:
Seller 2 observes
the first decision,
and accepts or
rejects
Stage 3:
Sellers
simultaneously set
uniform pricesp i,∅
Stage 4:
Consumers choose
entry and disclosure,
anticipating
equilibrium prices
Stage 5:
Informed sellers
observe competing
uniform prices and
choose personalized
offersp i(x)
Stage 6:
Consumers observe
applicable prices and
decide whether to
purchase
equilibrium prices to coincide. Sellers cannot commit to personalized offers before informa-
tion becomes usable. Consent after observing posted anonymous prices requires a different
analysis. Sequential uniform and personalized pricing is related to Chen and Zhang (2026),
Montes et al. (2019), Hu et al. (2025); the precise information sets above are maintained
assumptions, not claims about universal marketplace practice.
Full implementation requires honoring fees and access rights after every history, including
subsidized rejection continuations. Sellers accept when indifferent, and consumers observe
active access. Backward induction solves contracting; pricing and consumer choices satisfy
sequential optimality and rational-expectations consistency. The resulting fees exhaust par-
ticipation constraints under this protocol, providing an extraction benchmark rather than
an unrestricted optimal mechanism or a description of observed marketplace contracts.
Two sources of data value.Summarize the selected downstream continuation under
regimegby four gross-revenue states:R g N when neither seller adopts the service;R g B when
both adopt;R g I for the sole adopter under exclusive access; andRg U for its nonadopting rival.
These states incorporate entry, disclosure, and pricing responses and exclude commissions
and fees. Define
sales-revenue effectG g :=R g B −R g N ,andcompetition-threat effectT g :=R g N −R g U .(1)
Thesales-revenue effectG g measures whether bilateral data use increases or lowers each
seller’s product revenue relative to the no-data outcome. It captures productive gains
from better targeting or transaction creation, but it may be negative when personalization
intensifies price competition or discourages participation. Thecompetition-threat effectT g
measures the seller’s revenue loss in the exclusive access continuation following rejection.
This loss may arise from being the uninformed seller when the rival alone has usable data
(competitive channel), or from reduced consumer participation (participation channel). If
T g >0, rejecting access can be costly even when bilateral use lowers both sellers’ revenues.

10Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
It is therefore a disagreement-payoff effect: a seller may value access not because bilateral
data use is profitable, but because refusing access is worse.
This distinction is operationally important. Seller adoption is not, by itself, evidence
that a data product creates downstream revenue. A marketplace may observe strong will-
ingness to pay even when bilateral personalization reduces seller sales, provided that asym-
metric access would reduce the rejecting seller’s revenue even further. Conversely, data
may improve seller revenue but be difficult for the platform to monetize if sellers can
obtain equivalent information elsewhere or if governance prevents asymmetric informa-
tional advantage. The four-state representation makes these possibilities explicit without
relying on the Hotelling pricing environment used later.
2.1. Seller Adoption and Platform Data V alue
We first retain the full-implementation benchmark of the specified contracting protocol. It
identifies the fees consistent with bilateral adoption given the selected revenue states and
promised rejection continuations.
Lemma 1(Seller adoption under full implementation).If the platform can commit
to the announced rejection continuation, it can induce both sellers to adopt by charging:
F g 1 =F g 2|AC = (1−γ)(G g +T g), F g 2|RE = (1−γ)(R g I −R g N ).
Lemma 1 clarifies why seller willingness to pay can exceed the direct revenue improve-
ment from bilateral data use. The on-path fee includes both the bilateral revenue change
and the rejection loss. The off-path fee makes the second seller willing to activate exclusive
access after the first rejects. When this requires a subsidy, commitment to pay it is part
of implementation, even if the continuation generates little trade.
Proposition 1(Platform data value).Under full implementation, the platform’s
incremental profit from providing the data service rather than withholding it is:
V g data = 2γG g | {z }
commission-based value
+ [2(1−γ)G g + 2(1−γ)T g]| {z }
data monetization value
= 2G g + 2(1−γ)T g. (2)
The decomposition provides a practical diagnostic for identifying the source of data
monetization. The sales-revenue effect enters through commissions and fees, while the
threat effect supports fees through sellers’ retained revenue. A platform may profitably
offer a data service even when bilateral data use reduces seller revenue (G g <0), provided

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization11
sellers are sufficiently willing to pay to avoid an asymmetric informational disadvantage
((1−γ)T g >−G g). Adoption does not establish improved revenue, andG g >0 need not
imply higher welfare if it comes from repricing existing trade. Under Lemma 1, each seller
retains (1−γ)R g U . WhenT g = 0, the platform extracts the bilateral revenue gain and seller
net profit equals the no-data benchmark.
We next relax commitment only when the announced rejection continuation requires
F g 2|RE <0. In that event, the platform may revise the continuation to no access; all other
offers and access rights remain enforceable. Letη g ∈[0,1] be seller 1’s ex ante perceived
probability that the platform honors the subsidy. Defineξg(ηg) = 1 ifRg I ≥R g N , andξ g(ηg) =
ηg otherwise. Thus, a continuation requiring no subsidy remains enforceable. Here credi-
bility is a reduced-form primitive and service costs remain zero. Appendix EC.2.1 provides
the implementation-cost microfoundation.
Proposition 2(Data value under limited commitment).With limited implemen-
tation credibility:(A)The platform can induce bilateral adoption withF g 1 = (1−γ)[G g +
ξg(ηg)T g],F g 2|AC = (1−γ)(G g +T g), andF g 2|RE = (1−γ)(R g I −R g N ).(B)The platform’s data
value isV g data(ηg) = 2Gg + [1 +ξg(ηg)](1−γ)T g.(C)When a subsidy is required (R g I < Rg N ),
the data value weakly increases with the credibility ifT g ≥0and decreases otherwise.
Limited commitment operates through seller 1’s rejection payoff, which becomes (1−
γ)[Rg N −ξ g(ηg)T g]. Once seller 1 accepts, seller 2 faces an informed rival upon rejection
regardless of subsidy credibility. WhenT g >0, the first offeree pays weakly less and retains
weakly more profit. The randomized offer order preserves ex ante symmetry. Credibility
affects extraction from the given revenue states, separating theexistenceof competitive
vulnerability from the platform’sability to monetizeit. In the subsidy region, greater
credibility increases data value whenT g >0. Hence, a platform seeking to monetize the
threat effect has an incentive to strengthen commitment through enforceable arrangements,
such as escrow payments, third-party audits, or verifiable access records. Appendix EC.2.2
further provides a conditional bound on competition-threat value, clarifying when privacy
or access governance can eliminate it.
2.2. Hotelling Microfoundation
The remainder of the paper leverages a Hotelling microfoundation to endogenize revenue
states, consumer disclosure, prices, and market coverage, thereby establishing a tractable

12Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
link between the general data-value framework and observable marketplace outcomes. Con-
sumers have unit demand and preferencesx∼U[0,1]. Sellers 1 and 2 are located at 0 and
1. Purchasing from them incurs mismatch coststxandt(1−x), respectively. All consumers
have product valuationv >0, and marginal production costs are zero. Dividing all mone-
tary variables byt >0 normalizes the mismatch parameter to one;vand the privacy cost
below are therefore normalized monetary quantities. Letδ(x) indicate whether consumer
x’s information is used in the pricing subgame. The baseline privacy cost isc >0, incurred
once when that information becomes usable, regardless of which seller is eventually cho-
sen. A seller with usable data chargesp i(x); otherwise it chargesp i,∅. Writingp i for the
applicable price, the consumer’s ex ante net utilities from purchases are
U1(x) =v−p 1 −x−cδ(x), U 2(x) =v−p 2 −(1−x)−cδ(x).
Staying outside the gives zero. Once information has been used, privacy cost is sunk: not
purchasing gives−cδ(x) at the purchase stage. Consumers therefore compare expected
net entry utility with zero initially and applicable offers with the sunk-cost no-purchase
alternative subsequently. Positive privacy cost and the absence of advance personalized-
price commitment are central to the unilateral-disclosure incentive.
Consumers enter and purchase when indifferent. Under VDD they opt in when indiffer-
ent between disclosure and nondisclosure. When both products yield the same maximal
purchase utility and exactly one seller has usable information about that consumer, she
chooses that seller. Otherwise, she chooses the lower-mismatch seller, with the midpoint
tie assigned to seller 1. We study pure-strategy rational-expectations equilibria, impos-
ing symmetry for symmetric access. If multiple such pricing equilibria exist, we apply the
appendix’s selection: maximal gross revenue for each seller under bilateral access and max-
imal gross revenue for the uninformed seller under exclusive access. Access fees are sunk,
so this also maximizes the corresponding continuation profit. The selected equilibrium
determines reported revenues and provision regions. The alternatives in Appendix EC.1.1
and Appendix EC.1.2 preserveT M DC>0 andT V DD= 0, while revenues and some provi-
sion decisions can change. In particular, the high-valuation segmentation outcome below
depends on selection.
Market coverage is the mass of consumers who purchase, not the mass who enter or
disclose. Consumer surplus integrates realized utility net of prices and any incurred pri-
vacy costs. In the zero-cost baseline, social welfare equals consumer surplus plus platform

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization13
profit and both sellers’ net profits; commissions and access fees cancel as transfers. These
definitions separate transaction creation from changes in revenue or its distribution.
2.3. Scope, Extensions, and Limitations
The Hotelling analysis below uses a deliberately parsimonious baseline to isolate the
link between consumer disclosure, asymmetric data access, and platform monetization. It
assumes homogeneous privacy costs, perfect identification, bilateral access on the equilib-
rium path and full implementation of announced access continuations. Section 4 relaxs
the first three assumptions by introducing two types of privacy costs, a reveal-or-no-signal
information structure and endogenous exclusive data provision. The reveal-or-no-signal
information structure keeps consumers anonymous after failed identification and charges
the privacy cost only upon successful identification; it does not serve as a general model for
noisy or biased predictions. Appendix EC.2.1 endogenizes the limited-commitment friction
introduced above through implementation costs and the cost of reneging on a promised
continuation. These extensions differentiate changes in downstream revenue states from the
platform’s capacity to extract defensive payments. However, the qualitative results do not
suggest that all baseline thresholds or welfare rankings withstand arbitrary heterogeneity,
information structures, or commitment frictions.
Several constraints remain. The platform remains an intermediary, with symmetric fixed-
position sellers, exogenous commission, and no independent signals or direct nonprice bene-
fits from disclosure. The introduction of first-party information, inference about anonymous
buyers, costly opt-outs, service improvements, and advance price commitments may alter
unilateral disclosure or segmentation and require separate downstream analysis.
3. Product-Market Equilibrium
This section characterizes and compares equilibrium outcomes across three data-
governance regimes, revealing their impact on seller adoption, platform monetization, mar-
ket participation, and welfare. All proofs are in Online Appendix EC.3.
3.1. No Data Collection: Benchmark
Under NDC, both sellers choose uniform prices simultaneouslyp 1,∅, p2,∅. Seller 1 serves
consumers satisfying 0≤x≤min{v−p 1,∅, 1+p2,∅−p1,∅ 2 }, with a symmetric condition for
seller 2. Letr NDC i denote gross sales revenue,D NDC market coverage, ΠNDC p platform profit,
CS NDC consumer surplus, andSW NDC social welfare.

14Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Proposition 3(NDC benchmark).Under NDC, all consumers enter the platform:
(pNDC i,∅ , rNDC i ,Π NDC p , CSNDC, SWNDC) =




v
2 , v2 4 , γv 2 2 , v2 4 , 3v2 4  ,ifv <1

v− 1 2 , 1 2 v− 1 4 , γ(v−1 2 ), 1 4 , v−1 4  ,if 1≤v < 3 2

1, 1 2 , γ, v−5 4 , v−1 4  ,ifv≥ 3 2
.
Seller profit isπ NDC i = (1−γ)r NDC i and market coverage isD NDC = min{v,1}.
Entry is not purchase: free anonymous entry is weakly optimal even for consumers who
eventually do not buy. Whenv <1, uniform pricing leaves central consumers unserved,
so data-enabled offers may create additional transactions. For 1≤v <3/2, the market is
covered but marginal participation constrains prices. Forv≥3/2, competition pins the
uniform price at one. These cases distinguish the possibility of trade creation from repricing
an already covered market.
3.2. Mandatory Data Collection: Monetizing Competitive V ulnerability
The adoption subgames are NN (neither adopts), PP (both adopt), PN (only seller 1
adopts), and NP (only seller 2 adopts). Letr P P Mdenote each seller’s revenue under PP and
rP N M 2 the uninformed seller’s revenue under PN. By symmetry and (1), the sales-revenue
effect isG MDC =r P P M−r NDC, and the threat effect isT MDC =r NDC −r P N M 2 .
Proposition 4(MDC equilibrium).Under MDC:
(A)If the platform provides the data service, both sellers adopt and the equilibrium-path fees
areF MDC 1 =F MDC 2|AC = (1−γ)(r P P M−r P N M 2 );
(B)G MDC <0andT MDC >0, the platform provides the data service if and only ifγ≤
1 +GMDC/T MDC;
(C)Conditional on monetization, consumer entry occurs forx∈Ω MDC, whereΩ MDC =
[max{0,1−v+c},min{1, v−c}]and personalized prices arep MDC 1 (x) = max{1−2x,0}
andp MDC 2 (x) = max{2x−1,0}.
Mandatory data use lowers bilateral seller revenue, but the revenue lost after reject-
ing access can be larger still. Under the selected exclusive-access continuation, Appendix
EC.1.1 shows that the rejection loss is participation-driven whenv−c <3/4, while it
arises from personalized poaching forv−c≥3/4. In the former case, exclusive access
need not benefit either seller: the platform sells avoidance of an unfavorable continuation.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization15
Lower commissions increase the retained revenue at stake and strengthen the defensive fee
component. Data provision can consequently benefit the platform even as it reduces the
commission base.
Proposition 5(MDC stakeholder effects).Whenever the platform monetizes data
under MDC, platform profit weakly increases relative to NDC, while market coverage weakly
decreases. Consequently, seller profit and social welfare are weakly reduced. The consumer
surplus can rise only in the regions in which stronger personalized-price competition domi-
nates privacy and participation losses:1< v < 3 2 andv−c >1, orv≥ 3 2 andc < 1 2 .
Proposition 5 reveals a tension between platform monetization and marketplace perfor-
mance. MDC cannot expand coverage relative to NDC in this model. Low personalized
prices can attract central consumers, but mandatory privacy losses can drive other con-
sumers out. The platform benefits only because it provides the service when doing so is
profitable. Neither this platform gain nor bilateral adoption establishes improved mar-
ketplace performance. Prices and access fees redistribute surplus; privacy losses and lost
transactions are real welfare costs.
3.3. V oluntary Disclosure: Eliminating Threat-Based Adoption
Under VDD, consumers retain anonymous purchasing. Definer P P Vas bilateral seller rev-
enue andr P N V 2 as the uninformed seller’s revenue under unilateral adoption. Then, anal-
ogous to MDC, the sales-revenue effect isG VDD =r P P V−r NDC and the threat effect is
T VDD =r NDC −r P N V 2 . We use the following provision convention: the platform withholds
the service when the opt-in set is empty and otherwise provides it when incremental profit
is nonnegative. The boundary cases with only a singleton opt-in set are therefore retained,
although they generate no positive mass of data or strictly positive data value.
Proposition 6(VDD equilibrium and threat elimination).Under VDD:
(A)If the platform provides the service, both sellers adopt and the equilibrium-path fees are
F VDD 1 =F VDD 2|AC = (1−γ)(r P P V−r NDC);
(B)The threat effectT VDD = 0, the platform provides the service if and only if the opt-in
set is nonempty and the sales-revenue effect is non-negative(G VDD ≥0), which occurs
when(v, c)∈ P1 ∪ P2 ∪ P3, where the regionsP i are defined in the proof;

16Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
(C)Conditional on provision, for alli= 1,2, the uniform prices are
pVDD i,∅ =



max{ v 2 ,2v−c−1},if (v, c)∈ P 1 ∪ P3,
pNDC i,∅ ,if (v, c)∈ P 2,
and the opt-in set is
ΩVDD =



[max{0,1−v+c},min{1, v−c}],if (v, c)∈ P 1 ∪ P3
{ 1 2 },if (v, c)∈ P 2
.
The opt-in consumers receivep VDD 1 (x) = max{1−2x,0}andp VDD 2 (x) = max{2x−1,0}.
All other consumers opt-out and face the uniform prices above. Forx∈Ω VDD,p VDD i (x)<
pVDD i,∅ .
The central mechanism operates in the unilateral-adoption subgame, not just on the
bilateral-adoption path. With only one informed seller, disclosure does not improve avail-
able purchase surplus: after information becomes usable, that seller can price against the
uninformed alternative. Disclosure also incurs the strictly positive privacy cost. No con-
sumer therefore discloses, anonymous purchasing preserves participation, and both sellers
face the no-data revenue state. This restores the rejecting seller’s payoff and eliminates
both channels ofT VDD. The platform’s data value becomesV VDD data = 2GVDD, independent
ofγin the zero-cost, fixed-commission benchmark. Provision is aligned with seller gross
revenue, full fee extraction and the separate welfare accounting remain essential.
Under bilateral access, consumers near the midpoint may obtain enough personalized
competition to disclose, while more strongly matched consumers prefer anonymity. The
provision regions in Figure 2 have distinct economic meanings. In the interior ofP1, person-
alization reaches consumers unserved under NDC and anonymity retains endpoint demand.
At its zero-mass boundary and throughoutP 2, only the midpoint consumer discloses at a
zero personalized price, leaving aggregates at their NDC values. InP 3, NNDC already cov-
ers the market, so higher revenue comes from segmentation and higher anonymous prices.
This last outcome depends on the maintained revenue-maximizing selection: Remark 2 in
Appendix EC.1.2 describes a coexisting nondisclosure equilibrium that restores NDC out-
comes. Threat elimination survives this multiplicity, and positive-revenue segmentation is
not common to every equilibrium.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization17
Figure 2 Regimes of Data Monetization (γ= 0.15)
Notes.The “Pareto-improvement region” compares the platform, each seller, and consumers in aggregate.
3.3.1. Prices, Coverage, Profits, and W elfareWe now examine the effects of voluntary
data disclosure regulations, including the impact on prices and market coverage, profits
of platform and sellers, consumer surplus, and social welfare. Withholding the service
reproduces NDC. The following comparisons state explicitly when provision is required
under one or both regimes.
Proposition 7(Impacts on Price and Market Coverage).Conditional on data
provision under VDD and MDC:
(A)VDD opt-in consumers receive the same personalized prices under both regimes
(pVDD i (x) =p MDC i (x), i∈ {1,2}). If(v, c)/∈ {(v, c)|v >3/2, c= 1}, VDD opt-out con-
sumers would not enter under MDC. Ifv >3/2, c= 1, only the consumer atx= 1 2 opts
in under VDD, whereas the MDC entry set isΩ MDC = [max{0,2−v},min{1, v−1}].
(B)Relative to NDC,p VDD i,∅ ≥p NDC i,∅ , strictly on{(v, c) : 2/3< v≤1, c <3v/2−1} ∪ P3. For
opt-in consumers,p VDD i (x)≤p NDC i,∅ except when2/3< v≤1and0< c <3v/4−1/2. In
that case, seller 1’s personalized price exceeds its NDC price forx∈[1−(v−c),(2−
v)/4), and seller 2’s exceeds its NDC price forx∈((2 +v)/4, v−c]; all other opt-in
consumers face weakly lower prices.
(C)Market coverage satisfiesD VDD = min  DNDC +D MDC,1 	 .
Voluntary disclosure changes who remains available for uniform pricing. The anonymous
group is more concentrated among strongly matched consumers, which can raise its uniform
price. Some consumers may then disclose their purchase because personalization is cheaper
than thenewanonymous price, even though it is more expensive than theNDCprice.

18Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Figure 3 illustrates this distinction. Individual optimality within the VDD therefore does
not establish a gain relative to a different governance regime.
Figure 3 Equilibrium Prices (v= 0.8, c= 0.06, γ= 0.15)
Notes.MDC and VDD prices are conditional on provision, and consumers outside the MDC entry set receive no
MDC offer.
The coverage identity integrates complementary demand sources. Forv <1, NDC sus-
tains anonymous endpoint purchases but leaves central consumers unserved. MDC can
serve central consumers, by offering personalized competition, but loses others due to pri-
vacy costs. VDD accommodates both groups, as Figure 4 illustrates. In the high-valuation
region, full coverage instead means preserving the number of transactions while changing
prices and privacy losses.
Figure 4 Market Coverages under Alternative Governance Regimes whenv <1
Notes.Conditional on provision, solid segments represent purchases; dashed segments represent no purchase.
Proposition 8(Impacts on Profits).Conditional on data provision under VDD:(A)
πVDD i =π NDC i ≥π MDC i fori∈ {1,2};(B) Π VDD p ≥Π NDC p ;(C) Π VDD p ≥Π MDC p if and only if
γ≥γ V M(v, c) := max{0,1−rP P V−rP P M T MDC }.
VDD protects the seller’s disagreement payoff. Because the platform extracts the entire
bilateral revenue gain through the fee, seller net profits equal NDC profits; they do not gen-
erally increase above that benchmark. The platform’s comparison with MDC depends on

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization19
the revenue gains retained under VDD relative to the defensive fees available under MDC. A
higher commission reduces the latter advantage, producing the threshold in Proposition 8.
The platform need not voluntarily prefer effective consumer control at a low commission,
so a privately profitable commitment to honor opt-out is not automatic.
Consumer surplus and welfare require separate comparisons with NDC and MDC. The
former asks whether data use itself improves outcomes; the latter isolates the consequences
of disclosure rights when both regimes use data.
Proposition 9(Impacts on Consumer Surplus and Social Welfare).
Conditional on data provision under VDD:
(A)Consumer surplus satisfiesCS VDD ≥CS NDC on(v, c)∈ {(v, c) :1 2 < v≤
√
2
2 , c≤v− 1 2 } ∪
{(v, c) :
√
2
2 < v≤1, v− 3 4 +
√
2v2−1
4 ≤c≤v− 1 2 } ∪ P2, andCS VDD < CSNDC otherwise.
Similarly, social welfare satisfiesSW VDD ≥SW NDC on(v, c)∈ {(v, c) :1 2 < v≤ 6+
√
6
10 , c≤
v− 1 2 } ∪ {(v, c) :6+
√
6
10 < v≤1, c∈(0, 2v−1−
√
10v2−12v+3
4 ]∪[ 2v−1+
√
10v2−12v+3
4 , v−1 2 ]} ∪ P2,
andSW VDD < SWNDC otherwise.
(B)If the service is also provided under MDC,CS VDD > CSMDC andSW VDD > SWMDC.
Additional trade is the main source of welfare gains over NDC. When baseline coverage
is sufficiently low, serving central consumers can outweigh privacy losses. Asvapproaches
one, fewer incremental transactions remain available, and the higher anonymous price can
reduce consumer surplus. The welfare effect can be nonmonotone inc: low privacy costs
make disclosure inexpensive, while sufficiently high costs discourage disclosure and limit
aggregate privacy losses; intermediate costs can be most problematic when the remaining
coverage gain is small.
The high-valuation segmentation region provides a useful boundary to the main mech-
anism. InP 3, the market was already covered under NDC, so higher seller revenue does
not reflect additional trade. Anonymous-price increases redistribute surplus and disclo-
sure creates real privacy losses. Consumer surplus and welfare are therefore below NDC,
notwithstandingG VDD ≥0. The zero-mass cases inP 2 leave aggregates unchanged. This is
why eliminating defensive monetization cannot by itself establish welfare improvement.
When both regimes provide the service, VDD preserves the personalized offers of dis-
closers while allowing other consumers to purchase anonymously instead of exiting. This
explains the improvement over MDC. Provision remains endogenous: if only VDD pro-
vides, MDC equals NDC and part (A) applies; if only MDC provides, VDD equals NDC
and Proposition 5 applies; if neither provides, all outcomes coincide.

20Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Proposition 10(Pareto Improvement).VDD yields a Pareto improvement over
both NDC and MDC, evaluated for the platform, each seller, and consumers in aggregate, if
and only if(v, c)∈ {(v, c) :1 2 < v≤
√
2
2 , c < v−1 2 } ∪ {(v, c) :
√
2
2 < v <1, v−3 4 +
√
2v2−1
4 ≤c <
v− 1 2 }andγ≥γ win(v, c), where
γwin(v, c) =



(3v−2c−2)2
v2 ,if 2 3 < v <1, c≤3v 2 −1,
0,otherwise.
These gains occur in the transaction-creating region, as illustrated in Figure 2. Sellers
retain their NDC net profits, the platform captures additional revenue, and the aggregate
consumer surplus is not decreasing. The statement does not claim that all individual buyers
are better off: Proposition 7 identifies possible price increases for some consumers. The
policy implication is consequently conditional, not a universal recommendation for data
collection or a blanket preference for VDD over NDC.
3.3.2. Protecting the Anonymous Purchase OptionThe distinction between volun-
tary disclosure and protection of the anonymous channel motivates a separate design
benchmark. Impose an enforceable capp i,∅ ≤p NDC i,∅ ,i∈ {1,2}, under VDD. The platform
announces the benchmark before seller adoption and enforces it on anonymous offers. All
other baseline assumptions remain unchanged. We refer to this rule as ‘UP’ and letU g(x)
denote consumerx’s utility.
Proposition 11(Anonymous-Price Protection).When VDD is implemented with
an enforceable price cap (p i,∅ ≤p NDC i,∅ ,i= 1,2):
(A)The platform provides the data service if and only if(v, c)∈ {(v, c)| 1 2 < v≤1, c≤v−
1
2 ,4c 2 ≥5v 2 −4v} ∪ P2.
(B)U UP(x)≥U NDC(x)forx∈[0,1]andSW UP ≥SW NDC.
(C)Conditional on service provision under both UP and MDC,CS UP ≥
max{CS NDC, CSMDC}andπ UP i =π NDC i ≥π MDC i fori= 1,2. Moreover, UP yields
a Pareto improvement over both NDC and MDC, evaluated for the platform, each
seller, and consumers in aggregate, if and only if service provision under UP induces
positive-mass disclosure andγ≥γ U M(v, c) := max{0,1−(rUP −r MDC)/T MDC}.
The cap preserves every consumer’s NDC anonymous-purchase option. Disclosure
must compensate for privacy cost relative to that protected alternative. This rules out

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization21
segmentation-based monetization and confines positive-mass provision to transaction cre-
ation, while preserving seller benchmark profits under full extraction. Unlike the aggregate
consumer comparison for uncapped VDD, part (B) protects each consumer relative to
NDC. UP is an enforceable policy benchmark, not the platform’s privately optimal rule:
uncapped VDD can support greater extraction. Applying the cap would require specifying
and enforcing a defensible no-data price. That counterfactual benchmark is determined
inside the model, and the analysis does not estimate it from marketplace observations or
resolve its practical implementation.
4. Extensions and Counterfactuals
In this section, we first validate the robustness of our key findings by examining three
extensions that test specific restrictions of the baseline model, and then conduct model-
based counterfactual analyses to further illustrate these results.
4.1. Platform Choice of Access Structure
The baseline commits to bilateral access on the equilibrium path, with exclusivity only
after rejection. Broad access serves as a design benchmark motivated by concerns about
discriminatory access to platform resources (European Commission 2022, European Par-
liament and Council of the European Union 2023). We allow bilateral, exclusive, or no
access through fees, retaining sellers’ acceptance and rejection rights. Full commitment,
zero provision costs, and baseline equilibrium selection keep the revenue states unchanged.
Alternative continuation selections affect access boundaries through revenues.
Proposition 12(Optimal Access Structure).If the platform can choose whether to
induce bilateral or exclusive data access:
(A)Forg∈ {M DC, V DD}, bilateral data access is optimal ifGg + (1−γ)T g ≥0and2R g B ≥
Rg I +R g U . Exclusive data access is optimal ifR g I −R g U ≥2γT g andR g I +R g U >2R g B. The
platform can induce exclusive access by committing to
F g 1 = (1−γ)(R g I −R g U ), F g 2|RE = (1−γ)(R g I −R g N ), F g 2|AC >(1−γ)(G g +T g).
(B)Under MDC,R M DC I +R M DC U <2R M DC N . Hence, neither bilateral nor exclusive data
access increases total seller sales revenue relative to NDC. When the platform imple-
ments exclusive data access,π M DC i < πN DC i , i∈ {1,2}andSW M DC< SWN DC. More-
over, conditional on exclusive data access under MDC,CS M DC> CSN DConly if(v, c)∈

(v, c)|1< v <3 2 	 ∪ {(v, c)|3 2 ≤v≤ 7 4 , c < v−1 2 − p 2v−5/2} ∪  (v, c)

 v >7 4 , c <1 4 	 .

22Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
(C)Under VDD, the platform never offers exclusive data access.
Proposition 12 shows that platform endogenous access allocation preserves the source of
value distinction and the incentive of platform data monetization. Under MDC, the plat-
form may prefer exclusive access when it generates more total sales revenue than bilateral
personalization. Nevertheless, total sales revenue under either arrangement remains below
NDC. Profitable monetization under MDC therefore still relies on the threat effect. Under
endogenous data access, seller profit and social welfare are still reduced, and the consumer
surplus rise only under large valuation and low privacy cost. Under VDD, consumers refuse
disclosure when only one seller has access, making both the rejection-contingent threat and
deliberate exclusivity economically ineffective. Thus, the platform can profitably provide
the service only through bilateral sales-revenue gains under VDD.
4.2. Heterogeneous Privacy Cost
In the baseline model, we assume that all consumers have a homogeneous privacy cost.
Here, we extend the model to consider consumers with heterogeneous privacy concerns. Let
privacy cost bec ′ ∈ {cH, cL}, wherec H ≥c L >0. The high-cost group has massρand the
low-cost group mass 1−ρ. Raisingρraises average privacy cost, holding the two costs fixed.
Locations remain uniformly distributed within each group. The extension retains strictly
positive privacy costs and does not encompass arbitrary multidimensional or correlated
preferences.
Proposition 13(Robustness to heterogeneous privacy costs).Under heteroge-
neous privacy costs, whenever the pure-strategy rational-expectations continuation equilibria
exist:
(A)Under MDC,G MDC−h <0andT MDC−h >0, and the platform provides the data service
if and only ifG MDC−h + (1−γ)T MDC−h ≥0. Conditional on provision,D MDC−h ≤D NDC
andSW MDC−h < SWNDC. Moreover,CS MDC−h ≥CS NDC if and only ifCS MDC−h L ≥
CS NDC andρ≤ρ ′, whereCS MDC−h L is consumer surplus per unit mass of low-cost con-
sumers andρ ′ is defined in the proof.
(B)Under VDD,T VDD−h = 0andV VDD−h data = 2GVDD−h. The platform provides the service if
and only ifG VDD−h ≥0and the opt-in set is nonempty. Every symmetric bilateral VDD
equilibrium satisfiesp P P V−h i,∅ ≥p NDC i fori∈ {1,2}.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization23
(C)If both regimes provide the service,D VDD−h ≥D MDC−h,CS VDD−h ≥CS MDC−h, and
SW VDD−h ≥SW MDC−h. Moreover,π VDD−h i =π NDC i ≥π MDC−h i , whileΠ VDD−h p ≥Π MDC−h p
if and only if
γ≥max

0,1−(G VDD−h −G MDC−h)/T MDC−h	 .
Privacy-cost heterogeneity changes the distribution of consumer gains and losses without
altering the source of data value. Under MDC, aggregate consumer surplus depends on
the shares of low- and high-cost consumers, while social welfare remains below NDC.
Under VDD, neither privacy type discloses to a single informed seller, soT VDD−h = 0.
When provision under both MDC and VDD, VDD weakly increases coverage, consumer
surplus, and welfare relative to MDC, with the platform comparison governed by the
extension’s commission threshold. The unilateral nondisclosure result under VDD holds for
all strictly positive privacy costs, whereas the bilateral pricing and stakeholder comparisons
are conditional on the existence of the selected continuation equilibria.
4.3. Imperfect Identifiation
The baseline model assumes that the platform’s data perfectly reveals consumer preference
x. We now relax this assumption and replace certain identification with a reveal-or-no-
signal technology. Letq∈(0,1] be the probability that the service reveals a disclosing
consumer’s exact location to both sellers. Otherwise, it produces no usable signal and the
consumer remains in the uniform-price channel. Privacy cost is incurred only following suc-
cessful identification. This common-knowledge specification is denoted “VDD-IQ”. Thus,
qmeasures the frequency of exact identification, and the extension does not model the
precision of a noisy location estimate.
Proposition 14(Robustness to imperfect identification).For anyq∈(0,1]:
(A)Under MDC, exclusive access may remain informative. The platform provides the data
service if and only ifG MDC(q) + (1−γ)T MDC(q)≥0.
(B)Under VDD, no consumer discloses under exclusive access andT VDD(q) = 0. Thus,
V VDD data (q) = 2G VDD(q), and the platform provides the data service if and only if
GVDD(q)≥0and the equilibrium opt-in set is nonempty.
Under MDC, imperfect identification can leave exclusive access informative because con-
sumers cannot refuse the modeled data use while purchasing anonymously. Under VDD,
successful unilateral identification creates a privacy cost without improving the consumer’s

24Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
purchasing opportunity; failed identification preserves the anonymous option. Consumers
therefore withhold disclosure from a single informed seller for every positive identifica-
tion probability. This preserves threat elimination under the specified technology, without
implying that all imperfect information structures have the same effect.
4.4. Model-Based Counterfactuals
Amazon Brand Tailored Promotions motivates platform control of audience eligibility and
targeted discounts, while its US referral-fee schedule motivatesγ= 0.15 (Toogood 2026,
Amazon 2026). We setv= 0.73 andc= 0.08 to illustrate a partially covered NDC market,
threat-supported MDC provision, and transaction-creating VDD. These are normalized
scenario parameters,not estimatesof Amazon demand or privacy preferences. No pro-
prietary observations, treatment effects, access fees, or disclosure rates are inferred from
the public program description. In particular, it does not document the model’s sequen-
tial fee schedule or establish that consumers can transact on Amazon under the precise
anonymous-consent arrangement assumed here.
Table 1 Baseline Model-Based Counterfactuals
Outcome NDC MDC VDD MEA VDD-IQ
Service provided No Yes Yes No Yes
Disclosure mass 0.0000 0.3000 0.3000 0.0000 0.3000
Market coverage 0.7300 0.3000 1.0000 0.7300 0.8500
Seller revenue (r) 0.1332 0.0225 0.1555 0.1332 0.1443
Seller net profit 0.1132 0.0000 0.1132 0.1132 0.1132
Platform profit 0.0400 0.0450 0.0845 0.0400 0.0620
Consumer surplus (CS) 0.1332 0.0225 0.1450 0.1332 0.1338
Social welfare (SW) 0.3997 0.0675 0.4560 0.3997 0.4223
Sales-revenue effect (G) 0.0000−0.1107 0.0223 0.0000 0.0110
Competition-threat effect (T) 0.0000 0.1332 0.0000 0.0000 0.0000
Notes.Values are reported to four decimal places. Seller revenue and net profit are per seller; platform profit,
consumer surplus, and welfare are marketplace totals. Disclosure denotes opt-in/disclosure mass, not successfully
identified mass. VDD-IQ usesq= 0.5. According to Proposition 1, commission-based values for NDC, MDC, VDD,
MEA, and VDD-IQ are, respectively, 0.0000,−0.0332, 0.0067, 0.0000, and 0.0033; data-monetization values are
0.0000, 0.0383, 0.0379, 0.0000, and 0.0187.
Table 1 includes mandatory equal access (MEA), under which data access is activated
only if both sellers adopt, and VDD-IQ with imperfect identification. The matched 30%
disclosure proportions under MDC and VDD highlight the importance of purchasing alter-
natives. Under MDC, disclosers constitute the entire purchasing population. At these
parameters, the selected exclusive-access continuation has no entry, so the reported threat is

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization25
participation-driven. Under VDD, nondisclosers continue purchasing and coverage reaches
one. Seller net profit remains at NDC, while platform profit rises from 0.0400 to 0.0845.
MEA also eliminates the exclusive-access threat but creates no positive bilateral revenue
gain in this scenario, so the platform withholds the service. Equal access and voluntary
disclosure therefore address different margins.
Conversion versus revenue lift.The first diagnostic examines whether higher conver-
sion implies positive sales-revenue value. Letτ∈[0,1) be the targeted discount andℓ≥0
the proportional purchase-rate lift. Given baseline revenueR full =pD, promotional revenue
and its proportional change are
Rdisc(τ, ℓ) = (1−τ)p(1 +ℓ)D,∆R(τ, ℓ) = (1 +ℓ)(1−τ)−1.
The zero revenue change boundary isℓ ∗(τ) =τ /(1−τ). For example, a 20% lift with
a 20% discount reduces revenue by 4%. Conversion lift alone is therefore insufficient to
measure the sales-revenue value of data and may overstate the value created by targeting.
Data value should instead be evaluated by the resulting revenue change, captured in our
framework byG. Moreover, if the platform charges a high data-service fee despiteG <0,
monetization may reflect the threat effectTrather than revenue created by the data.
Threat availability and commission rate.We now examine the sensitivity of data
monetization to the threat effect and platform commission. Letψ∈[0,1] denote the share
of the baseline MDC threat available for monetization, soT(ψ) =ψT MDC. Holding the
sales-revenue effect fixed, full-commitment data value is
V MDC data (ψ, γ) = 2GMDC + 2(1−γ)ψT MDC.
ForG MDC <0< T MDC, provision requiresψ≥ −G MDC/[(1−γ)T MDC]. This is a reduced-
form stress test of threat availability. Its parameterψis distinct from the subsidy-credibility
parameterηin Proposition 2: a concrete change in governance may also alter pricing,
participation, and the revenue effect.
Using Table 1’sG MDC =−0.1107 andT MDC = 0.1332, Figure 5 shows that positive data
value requires a threat share above approximately 0.978 at the baseline commission. Thus,
a roughly 2.2% reduction in the available threat eliminates the provision incentive. Even
with the full threat, data value becomes negative whenγ >0.169. Higher commissions
increase the platform’s exposure to lost product revenue while reducing sellers’ retained

26Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
revenue available for defensive fees. Threat-supported provision therefore requires both
substantial rejection-payoff leverage and a sufficiently low commission rate.
Figure 5 Sensitivity of Platform Data Value to Threat Availability and Commission Rate
Identification probability under VDD.Finally, we examine the identification require-
ments for profitable data provision and the market outcomes under VDD. Figures 6–7 use
the reveal-or-no-signal extension, with privacy cost incurred only upon successful iden-
tification. Figure 6 shows that higher privacy costs need not increase the identification
probability required for positive data value, and higher valuation need not facilitate mon-
etization. The bilateral analysis supporting Proposition 14 establishes a symmetric equi-
librium for 1 2 < v <1, 0< c < v−1 2 . Higher privacy costs can discourage consumers from
replacing existing anonymous purchases with cheaper personalized offers, limiting revenue
losses from personalization. Higher valuation expands NDC coverage and leaves fewer addi-
tional transactions to create. Figure 7, atv= 0.73,c= 0.08, andγ= 0.15, also illustrates
that platform and consumer outcomes can move differently as exact identification becomes
more likely. Eliminating defensive monetization does not by itself align those outcomes.
Figure 6 Identification Thresholds for Positive
VDD-IQ Data Value (γ= 0.15)
Figure 7 Market Outcomes as Exact Identification
Improves (v= 0.73, c= 0.08, γ= 0.15)

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization27
5. Conclusion and Managerial Implications
This paper shows how consumer disclosure rights reshape the disagreement payoffs support-
ing data contracts in a commission-based marketplace. The commercial value of platform-
controlled information reflects both changes in bilateral seller revenue and losses sellers
avoid by purchasing access. Mandatory collection can support defensive fees through asym-
metric competition or reduced participation following rejection, even when bilateral per-
sonalization lowers seller revenue. Under baseline voluntary disclosure, consumers withhold
information from a sole subscriber while retaining anonymous purchasing, restoring sell-
ers’ no-data rejection payoffs. The platform can then monetize bilateral revenue gains, but
not an exclusive-access threat. This connects consumer control to upstream contracting
and service provision: privacy governance changeswhy sellers pay for data, not merely how
much information is available.
The analysis yields several managerial implications.First, evaluate data services
against both no-data and rejection counterfactuals.Managers should distinguish the
revenue change under bilateral use from the loss a seller faces when its rival alone sub-
scribes. Adoption and conversion should be assessed alongside gross product revenue and
retained profit after commissions and access fees; deeper discounts can increase purchases
while reducing revenue. Sellers should likewise evaluate the contractual consequences of
refusal rather than equate rejecting a subscription with restoring a no-data market. Where
exclusive access requires a subsidy, its credibility affects the defensive payments the plat-
form can extract. Under full fee extraction, VDD protects sellers’ no-data net profits but
does not allow them to retain their gross revenue gains.
Second, evaluate access fees together with commission exposure.Holding down-
stream revenue states fixed, lower commissions increase sellers’ retained revenue at risk
after rejection and strengthen extractable defensive payments. Higher commissions reduce
this fee component and increase the platform’s exposure to lost product revenue. A data
service can therefore generate access fees while shrinking the commission base. Once VDD
eliminates the threat, however, full fee extraction makes the platform’s incremental provi-
sion value independent of the commission rate. Because commissions are exogenous in our
model, these results guide the evaluation of service provision and pricing at a given rate;
they do not identify an optimal commission policy.

28Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Third, preserve anonymous purchasing and protect its price.VDD can preserve
or expand coverage because consumers need not disclose to purchase. This protection
requires effective refusal of pricing-related data use, not merely a nominal opt-out. Yet
anonymity alone does not preserve no-data prices: in the selected high-valuation segmen-
tation equilibrium, anonymous prices rise without additional trade. An enforceable cap at
the no-data benchmark addresses this remaining channel by preserving every consumer’s
no-data purchasing option. In the model, the cap protects individual consumer utility and
welfare while preserving sellers’ no-data net profits. The platform remains weakly better
off than under no data because it can withhold the service, although its profit can fall
relative to uncapped VDD. Implementation requires a defensible benchmark announced
before seller adoption and enforcement of the cap on anonymous offers. Disclosure rights
and price protection thus address distinct sources of harm.
Fourth, distinguish equal-access commitments from consumer disclosure rights.
Offering the service to both sellers does not eliminate defensive demand if rejection leaves
the rival exclusively informed. A meaningful equal-access commitment must also prohibit
exclusive access after rejection. Although such a rule removes the threat, it does not pro-
vide an anonymous purchasing option or ensure that bilateral data use raises revenue. In
the reported counterfactual, mandatory equal access leads the platform to withhold the
service, whereas VDD supports provision and full coverage. Access rules determine who
may use information; disclosure rights also affect whether usable information is generated
and whether consumers remain willing to purchase. Platforms and regulators should there-
fore evaluate these instruments separately, using seller revenue, retained profit, market
coverage, consumer surplus, and privacy losses—not adoption or disclosure volume alone.
The results offer a key lesson for marketplace practitioners: the return on a platform’s
data service should be evaluated against relevant competitive alternatives, rather than
solely based on seller revenue without the service. A seller may rationally opt to pur-
chase data even if personalization lowers overall revenue, as refusing access could heighten
its disadvantage against an informed rival. Therefore, sellers should distinguish between
productive returns and defensive expenditures when evaluating data-service contracts and
negotiating terms. Similarly, policymakers should be cautious in interpreting strong seller
demand for data as evidence of efficiency, as it may reflect competitive vulnerability rather
than productive information use.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization29
The model deliberately isolates the interaction among platform-controlled information,
personalized pricing, seller adoption, and consumer disclosure. Future research could incor-
porate heterogeneous sellers, independent first-party data, direct non-price benefits from
disclosure, richer bargaining arrangements, and alternative uses of consumer information
such as recommendations, advertising, ranking, and demand forecasting. These extensions
may restore some value to unilateral data access under consumer control. More generally,
our analysis suggests that the economically relevant measure of privacy governance is not
disclosure volume alone, but the amount and quality of information that can be used to
create an asymmetric competitive advantage.
References
Ali SN, Lewis G, Vasserman S (2023) Voluntary disclosure and personalized pricing.The Review
of Economic Studies90(2):538–571.
Amaldoss W, He C (2019) The charm of behavior-based pricing: When consumers’ taste is diverse
and the consideration set is limited.Journal of Marketing Research56(5):767–790.
Amazon (2026) How much does it cost to sell on Amazon? URLhttps://sell.amazon.com/
pricing, accessed September 15, 2026.
Argenziano R, Bonatti A (2026) Data linkages and privacy regulation.American Economic Journal:
Microeconomics18(3):317–360.
Bhargava H, Dubus A, Ronayne D, Shekhar S (2026) The strategic value of data sharing in inter-
dependent markets.Management Science72(2):1472–1488.
Bimpikis K, Crapis D, Tahbaz-Salehi A (2019) Information sale and competition.Management
Science65(6):2646–2664.
Bimpikis K, Morgenstern I, Saban D (2024) Data tracking under competition.Operations Research
72(2):514–532.
California Department of Justice (2026) California Consumer Privacy Act (CCPA). URLhttps:
//oag.ca.gov/privacy/ccpa, updated August 28, 2026, accessed September 15, 2026.
Chen Y, Narasimhan C, Zhang ZJ (2001) Individual marketing with imperfect targetability.Mar-
keting Science20(1):23–41.
Chen Z, Choe C, Matsushima N (2020) Competitive personalized pricing.Management Science
66(9):4003–4023.
Chen Z, Zhang M (2026) Personalized pricing in the presence of privacy concerns.Management
ScienceArticles in Advance.
Choe C, Cong J, Wang C (2024) Softening competition through unilateral sharing of customer
data.Management Science70(1):526–543.
Choe C, King S, Matsushima N (2018) Pricing with cookies: Behavior-based price discrimination
and spatial competition.Management Science64(12):5669–5687.
Choe C, Matsushima N, Shekhar S (2025) The bright side of the GDPR: Welfare-improving privacy
management.Management Science71(8):6836–6858.
Cong J, Matsushima N (2026) The effects of personal data management on competition and welfare.
Management ScienceArticles in Advance.
Cosguner K, Chan TY, Seetharaman PB (2017) Behavioral price discrimination in the presence of
switching costs.Marketing Science36(3):426–435.

30Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Dinev T, Hart P (2006) An extended privacy calculus model for e-commerce transactions.Infor-
mation Systems Research17(1):61–80.
Drakopoulos K, Makhdoumi A (2023) Providing data samples for free.Management Science
69(6):3536–3560.
Du J, Ning ZE (2026) To each their own: Personalized product offerings in competition.Manage-
ment Science72(6):4737–4759.
European Commission (2022) Case M.10262: Meta (formerly Facebook)/Kustomer. Commission
Decision of 27 January 2022.
European Parliament and Council (2016) Regulation (EU) 2016/679 on the protection of natu-
ral persons with regard to the processing of personal data. Official Journal of the European
Union, L 119, URLhttps://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:
32016R0679, accessed August 26, 2026.
European Parliament and Council of the European Union (2023) Regulation (EU) 2023/2854 on
harmonised rules on fair access to and use of data (Data Act). Official Journal of the European
Union, 22 December 2023.
Fu X, Chen N, Gao P, Li Y (2026) Privacy-preserving personalized recommender systems.Manu-
facturing & Service Operations Management28(1):271–289.
Galperti S, Perego J (2023) Privacy and the value of data.AEA Papers and Proceedings113:197–
203.
Guo L (2025) Selling data to marketers.Management Science71(10):8823–8841.
Hu Y, Li G, Liu M, Qu S (2025) Information sharing and personalized pricing in online platforms.
Production and Operations Management34(12):3958–3977.
Ichihashi S (2020) Online privacy and information disclosure by consumers.American Economic
Review110(2):569–595.
Ke TT, Sudhir K (2023) Privacy rights and data security: GDPR and personal data markets.
Management Science69(8):4389–4412.
Kim Y, Cui H, Zhu Y (2025) Behavior-based pricing under informed privacy consent: Unraveling
autonomy paradox.Marketing Science44(6):1362–1380.
Li G, Tao Y, Zheng H (2025a) Endogenous information acquisition in a competitive market with
personalized pricing.Transportation Research Part E: Logistics and Transportation Review
202:104330.
Li X, Li B, Yang Z (2025b) The dark side of voluntary data sharing.MIS Quarterly49(1):155–178.
Li X, Li KJ (2023) Beating the algorithm: Consumer manipulation, personalized pricing, and big
data management.Manufacturing & Service Operations Management25(1):36–49.
Li X, Wang X, Nault BR (2024) Is personalized pricing profitable when firms can differentiate?
Management Science70(7):4184–4199.
Lin T, Strulov-Shlain A (2025) Choice architecture, privacy valuations, and selection bias in con-
sumer data.Marketing Science44(6):1321–1338.
Liu Y, Long F (2026) Data and algorithms: Strategic disclosure of competitiveness on platforms
through marketplace analytics.Marketing Science45(3):653–674.
Markovich S, Yehezkel Y (2026) Competing for cookies: Platforms’ business models in data markets
with network effects.Management Science72(2):915–931.
Montes R, Sand-Zantman W, Valletti T (2019) The value of personal information in online markets
with endogenous privacy.Management Science65(3):1342–1362.
Pazgal A, Soberman D (2008) Behavior-based discrimination: Is it a winning play, and if so, when?
Marketing Science27(6):977–994.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization31
Ray J, Menon S, Mookerjee V (2026) Bargaining over data and analytics: Sellers, buyers and
consultants.Information Systems Research37(3):2031–2048.
Rhee KE, Thomadsen R (2017) Behavior-based pricing in vertically differentiated industries.Man-
agement Science63(8):2729–2740.
Rhodes A, Zhou J (2024) Personalized pricing and competition.American Economic Review
114(7):2141–2170.
Shin J, Sudhir K (2010) A customer management dilemma: When is it profitable to reward one’s
own customers?Marketing Science29(4):671–689.
Sun T, Yuan Z, Li C, Zhang K, Xu J (2024) The value of personal data in internet commerce: A
high-stakes field experiment on data regulation policy.Management Science70(4):2645–2660.
Thisse JF, Vives X (1988) On the strategic choice of spatial price policy.American Economic
Review78(1):122–137.
Toogood M (2026) What are Amazon Brand Tailored Promotions? Amazon Selling Partner Blog,
URLhttps://sell.amazon.com/blog/brand-tailored-promotions, accessed August 26,
2026.
Wang J, Jiang Z, Singh PV (2026) Impact of the invisibles: Personalized pricing on platform with
privacy-preserving users.Information Systems ResearchArticles in Advance.
Wernerfelt N, Tuchman A, Shapiro BT, Moakler R (2025) Estimating the value of offsite tracking
data to advertisers: Evidence from Meta.Marketing Science44(2):268–286.
Wu J (2025) Secondary market monetization and willingness to share personal data.Management
Science71(10):8471–8490.
Yan P, Pei J, Kumar S (2026) To collect or to purchase? Collaboration between manufacturer and
e-commerce platform on customization.Information Systems Research37(3):1944–1965.
Yao Y (2025) Reputation for privacy.Marketing Science44(5):1145–1162.
Zheng H, Tian L, Li G (2026) Data evaluation: Mechanisms and implications.Management Science
Articles in Advance.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization1
Online Appendix to
The Source of Data Value: Consumer Disclosure, Access Design,
and Platform Monetization
This Appendix presents the pricing-subgame equilibria of the baseline model in Appendix EC.1, supple-
mentary Analysis of Platform Data Value in Appendix EC.2, proofs of the main results in Appendix EC.3,
and proofs of additional results and tables in Appendix EC.4.
Appendix EC.1: Pricing Subgame Equilibria in Baseline Model
EC.1.1. MDC Pricing Subgame Equilibria
1. The “NN” Subgame.When neither seller purchases the data service, both use uniform pricing and
consumers incur no privacy cost. The equilibrium is identical to the NDC benchmark in Proposition 3.
2. The “PP” Subgame.Both sellers offer personalized pricesp i(x) to consumers atx∈[0,1]. Let Ω P P M
denote the equilibrium entry set andp P P M i (x),i∈ {1,2}, the equilibrium pricing strategies.
Lemma EC.1.1.Under mandatory data collection, when both sellers purchase the data service, consumers
located inx∈Ω P P Menter the platform, where
ΩP P M=



∅,ifv≤ 1 2 or ifc > v−1 2
[max{0,1−(v−c)},min{1, v−c}],ifv > 1 2 , c≤v− 1 2
,
while others stay out. WheneverΩ P P M̸=∅, the equilibrium personalized prices for eachx∈Ω P P Mare
pP P M 1 (x) = max{1−2x,0}andp P P M 2 (x) = max{2x−1,0}.
Lemma EC.1.1 shows that consumers closer to the market center are more likely to enter under MDC,
while those near the endpoints may stay out. Personalized pricing allows the better-matched seller to charge
its location advantage over the rival, which is largest at the endpoints and decreases toward the center.
Personalized prices therefore fall toward the center, and then consumers enter only when this surplus covers
the privacy costc. Hence, no consumer enters whenv−cis low; asvincreases orcdecreases, entry begins
around the center and expands toward the endpoints until the entire market is covered.
3. The “PN” and “NP” Subgames.In the “PN” subgame, seller 1 sets the personalized pricep 1(x)
and seller 2 the uniform pricep 2,∅. Let Ω P N Mdenote the equilibrium entry set andp P N M 1 (x) andp P N M 2,∅
the equilibrium prices. If multiple rational-expectations equilibria exist, we select the one maximizing the
uninformed seller’s sales revenue, capturing optimistic common expectations about its pricing response.
Lemma EC.1.2.Under MDC, when only seller 1 purchases the data service, consumers inx∈Ω P N M
enter the platform, where
ΩP N M=



∅,ifv−c < 3 4

max{0, 3 2 −(v−c)},1  ,ifv−c≥ 3 4 ,
and others stay out. WheneverΩ P N M̸=∅, equilibrium prices arep P N M 1 (x) = max{3 2 −2x,0}andp P N M 2,∅ = 1 2 .
Remark 1.When 3 4 < v−c≤1, the “PN” subgame admits an alternative rational-expectations equilib-
rium with a smaller entry set: consumers in [v−c,1] enter, and the uninformed seller charges 2(v−c)−1. The
threat effect remains strictly positive and is weakly larger than under the maximal-participation equilibrium.
Thus, selecting the latter gives a conservative measure of the threat generated by a rival’s data access.
By symmetry, in the “NP” subgame, seller 2 sets the personalized pricep 2(x) and seller 1 the uniform
pricep 1,∅. Let Ω N P M,p N P M 2 (x), andp N P M 1,∅ denote the corresponding equilibrium entry set and prices.

2Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Lemma EC.1.3.Under MDC, when seller 2 adopts the exclusive data access, consumers located inx∈
ΩN P Menter the platform while others stay out, where
ΩN P M=



∅,ifv−c < 3 4

0,min{v−c− 1 2 ,1}  ,ifv−c≥ 3 4 .
WheneverΩ N P M̸=∅, equilibrium prices arep N P M 2 (x) = max{2x− 1 2 ,0}andp N P M 1,∅ = 1 2 .
Lemma EC.1.2 and Lemma EC.1.3 show that, when only one seller purchases the data service, partial
coverage is concentrated on the side of the uninformed seller, and the entry region expands toward the
informed seller asv−cincreases. Seller 2, the uninformed seller, charges the uniform price 1 2 , which serves
as an outside option to seller 1’s personalized offer. Near seller 1, this alternative is relatively unattractive,
allowing seller 1 to charge a high personalized price and leave little consumer surplus, so consumers may stay
out. Toward seller 2, the uniform offer becomes more attractive, constraining seller 1’s price and increasing
consumer surplus and entry. Thus, the uninformed seller promotes participation by limiting the informed
seller’s surplus extraction. Seller 1’s personalized price falls withxas its location advantage declines, and
sufficiently close to seller 2, it cannot profitably match the uniform offer even at zero price, so consumers buy
from seller 2. Asv−cincreases, more consumers can cover the privacy cost, and the entry region expands
until the market is fully covered.
EC.1.2. VDD Pricing Subgame Equilibria
1. The “NN” Subgame.If neither seller adopts the data service, consumer disclosure does not affect the
outcome because both sellers can only charge uniform prices.
2. The “PP” Subgame.For selleri∈ {1,2}, denote the equilibrium personalized prices and the uni-
form prices asp P P V i (x) andp P P V i,∅ , respectively. We focus on symmetric pure-strategy rational-expectations
equilibria. Consumers enter and opt in when indifferent. When multiple such equilibria exist, we select an
equilibrium that maximizes each seller’s sales revenue. Remark 2 describes the possible alternative equilibria
and their implications for bilateral revenue and service provision.
Lemma EC.1.4.Under voluntary regulation, when both sellers purchase the data service, all con-
sumers enter the platform. Furthermore, the following results hold:(A)If(v, c)∈

(v, c)

 v≤ 1 2 	 ∪
(v, c)

 v >1 2 , c≥min  v− 1 2 ,1 	 ,(v, c)/∈ P3 	 , thenp P P V i,∅ =p N DC i,∅ and
ΩP P V=



{1/2},ifv > 1 2 , c= min  v− 1 2 ,1 	 ,
∅,otherwise.
The consumers located at 1 2 face personalized price atp P P V 1 (1/2) =p P P V 2 (1/2) = 0.(B)If(v, c)∈
(v, c)

 v >1 2 , c <min  v− 1 2 ,1 		 ∪ P3, thenΩ P P V= [max{0,1−v+c},min{1, v−c}], opt-in consumers
facep P P V 1 (x) = max{1−2x,0}andp P P V 2 (x) = max{2x−1,0}, and all other consumers opt-out. If(v, c)∈
{(v, c)|v−c <1}, thenp P P V i,∅ = max  v 2 ,2v−c−1 	 , i= 1,2. If(v, c)∈ {(v, c)|v >1, c≤v−1, c <1}, then all
consumers disclose, and the uniform price satisfyingp P P V 1,∅ =p P P V 2,∅ ≥1 +csupports the selected outcome;
1 +cis a representative price.
Lemma EC.1.4 shows that all consumers enter under VDD, while disclosure depends on product valuation
and privacy cost. Whenvis very low orcvery high, all consumers opt out because personalized pricing cannot
offset the privacy cost. For intermediate values, central consumers opt in while those near the endpoints opt
out. Because central consumers are similarly matched with both sellers, disclosure intensifies personalized-
price competition and lowers prices enough to offset the privacy cost; near the endpoints, the better-matched
seller can extract more surplus, making disclosure less attractive. Asvincreases orcdecreases, the opt-in
region expands toward the endpoints until all consumers opt in. Consistently, personalized prices fall toward

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization3
the market center as competition intensifies. Thus, VDD preserves full participation while inducing disclosure
only when its competitive benefit exceeds the privacy cost.
Remark 2.The “PP” subgame admits the following alternative equilibria: (i) If (v, c)∈ {(v, c)|v≥2,1≤
c≤v−1}, there is a full-disclosure equilibrium with Ω P P V= [0,1] andp P P V 1,∅ =p P P V 2,∅ ≥1 +c. (ii) If (v, c)∈ P3,
there is an empty-disclosure equilibrium with ΩP P V=∅andp P P V 1,∅ =p P P V 2,∅ = 1. (iii) If (v, c)∈ {(v, c)|3 2 < v <
3+
√
2
2 , c≥max{1,2v−3}, v−1< c < v−1 + 1 4(v−1) }, there is a partial-disclosure equilibrium with Ω P P V=
[1−v+c, v−c] andp P P V 1,∅ =p P P V 2,∅ = 2v−c−1.
Anticipating any of these equilibria, the platform does not provide the data service. Relative to the selected
equilibria, provision changes only onP 3 and whenv > 3 2 andc= 1. OnP 3, the alternative equilibrium
weakly lowers platform profit and seller sales revenues, leaves seller profits unchanged, and strictly increases
consumer surplus. All alternative equilibria yield weakly lower seller sales revenues in the PP subgame. Since
data-service fees are sunk, the equilibrium in Lemma EC.1.4 weakly maximizes both sellers’ continuation
profits and is therefore seller-preferred among symmetric pure-strategy rational-expectations equilibria. The
threat effect remains zero under VDD in all alternative equilibria. The two equilibria onP 3 imply Π V DD p ∈
[ΠN DC p ,Π N DC p + 2GV DD],CS V DD∈[CS N DC−2G V DD−c(2v−2c−1), CS N DC], andSW V DD∈[SW N DC−
c(2v−2c−1), SW N DC], with seller net profits unchanged at NDC.
3. The “PN” and “NP” Subgames.In both subgames, only one seller adopts data service.
Lemma EC.1.5.With voluntary data disclosure regulations, if only one seller purchases the data service,
all consumers enter the platform and opt-out of data disclosure.
Lemma EC.1.5 implies that if only one seller purchases the data service, the data market has no data and
thus the equilibrium prices are identical to those under NDC.
Appendix EC.2: Supplementary Analysis of Platform Data V alue
EC.2.1. Credibility Microfoundation
Section 2.1 treats commitment credibilityη g as a reduced-form primitive. We now endogenize this credibility
from the platform’s continuation payoff and the cost of reneging on a subsidy-backed access commitment.
We focus on the subsidy region,R g I < Rg N . Suppose that providing the data service entails a per-seller
operating costa≥0 and a fixed implementation costK≥0, incurred upon activation. Exclusive access
costsa+K, bilateral access costs 2a+K, and no access incurs neither cost. If the announced exclusive-
access continuation is implemented after seller 1’s rejection, seller 2 obtains (1−γ)R g I −F g 2|RE, while the
platform obtainsγ(R g I +R g U ) +F g 2|RE −a−K. If the platform instead revises the continuation to no data
access, seller 2 obtains (1−γ)R g N , while the platform earns 2γR g N before any reneging penalty. At the
committed feeF g 2|RE = (1−γ)(R g I −R g N ), seller 2 is indifferent between accepting exclusive access and
receiving its no-data payoff. The platform’s continuation-profit loss from honoring the subsidy is therefore
∆Lg ≡R g N −R g I +γT g +a+K. Letκ≥0 denote the contractual, legal, or reputational loss from reneging
on the announced subsidy. Its realization occurs after seller 1’s adoption decision and is privately observed
by the platform, while seller 1 knows only its distribution. We assume thatκhas a continuous cumulative
distribution function Φκ(·) with densityϕ κ(·). The platform honors the subsidy wheneverκ≥∆L g, thus the
credibility is given byη g = Pr(κ≥∆L g) = 1−Φ κ(∆Lg). WhenR g I ≥R g N , no subsidy is required and the
rejection-contingent continuation remains fully credible.
Proposition EC.2.1(Comparative statics of data value).In the subsidy region:(A)IfT g >0, the
platform’s data value decreases withγ,aandK, and weakly increases under an upward shift in the distri-
bution of the reneging penaltyκ.(B)IfT g <0, data value weakly increases withaif and only ifϕ κ(∆Lg)≥
2
(1−γ)|T g | , withKif and only ifϕ κ(∆Lg)≥ 1 (1−γ)|T g | , and withγif and only ifϕ κ(∆Lg)≤ 1+ηg (1−γ)|T g | . An
upward shift in the distribution ofκweakly decreases data value.

4Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Proposition EC.2.1 endogenizes continuation credibility by linking it to the platform’s incentive to honor
the subsidy. WhenT g >0, exclusive access disciplines the rejecting seller, so higher implementation costs or
commission weaken credibility and threat-based fee extraction, while a larger reneging penalty strengthens
them. Hence, escrow arrangements, third-party verification, and auditable access commitments can reinforce
subsidy-backed threats when implementation costs are sufficiently small. WhenT g <0, exclusive access
instead improves the rejecting seller’s outside option, so weaker credibility can benefit the platform. Higher
aorKmay then raise data value if the resulting fee-extraction gain exceeds their direct cost, while the effect
ofγdepends on its direct and credibility effects. The thresholds in part (B) identify when these indirect
effects dominate. This case is included for generality and does not arise in an active data-service equilibrium
under the focal MDC and VDD regimes.
EC.2.2. Conditional Bound on Threat V alue
The baseline model studies how contractual credibility affects the extraction of an existing threat. We now
examine when the threat could be eliminated. Consider a general consumer type space Θ endowed with an
atomless probability measureµ. For any regimeg, let bΩg ⊆Θ denote the set of consumers whose information
can become usable when only one seller has data access, and letq(θ)∈[0,1] denote the quality of the
corresponding signal. Define the quality-weighted usable unilateral information asβ bΩg ,q =
R
bΩg q(θ)dµ(θ),
denotedβ g for simplicity. LetR g U (bΩg, q) denote the equilibrium sales revenue of the uninformed seller when
only its rival can use these signals. Without usable unilateral information, the continuation coincides with
the no-data benchmark andR g U (∅,0) =R g N . We assume that unilateral information weakly disadvantages
the uninformed seller,R g U (bΩg, q)≤R g N , and that its equilibrium revenue is Lipschitz continuous in the
usable-signal profile:
|Rg U (Ω, q)−Rg U (Ω′, q′)| ≤L
Z
Θ
|q(θ)1 Ω(θ)−q ′(θ)1Ω′(θ)|dµ(θ),forL≥0.
Proposition EC.2.2(Threat bound and elimination).Under the preceding assumptions, the threat
effect satisfies0≤T g ≤Lβ g. Hence,β g = 0is sufficient to eliminate the threat effect. If, in addition,
Rg U (bΩg, q)< Rg N wheneverβ g >0, thenβ g = 0is also necessary for threat elimination.
Proposition EC.2.2 shows that eliminating threat-based monetization depends not on disclosure volume per
se, but onusable information under unilateral access. The condition that eliminating the usable information
also restores the no-data participation outcome is essential: zero realized records alone need not eliminate a
participation-driven threat.
Appendix EC.3: Proofs of Main Results
Proof of Lemma 1.Fixg∈ {MDC,VDD}. If seller 1 accepts, seller 2 obtains (1−γ)R g B −F g 2|AC from
accepting and (1−γ)R g U from rejecting. Hence, the maximal fee inducing acceptance isF g 2|AC = (1−γ)(R g B −
Rg U ) = (1−γ)(G g +T g). If seller 1 rejects, seller 2 obtains (1−γ)R g I −F g 2|RE from accepting and (1−γ)R g N
from rejecting. Thus,F g 2|RE = (1−γ)(R g I −R g N ). Anticipating these continuation decisions, seller 1 obtains
(1−γ)R g B −F g 1 from accepting and (1−γ)R g U from rejecting. Therefore, the maximum first-stage fee that
induces acceptance isF g 1 = (1−γ)(R g B −R g U ) = (1−γ)(G g +T g). Thus, both sellers adopt, and each earns
(1−γ)R g U on the equilibrium path.□
Proof of Proposition 1.If the platform withholds the data service, its profit is Π g p,no = 2γRg N . Under
provision, Lemma 1 gives total data-service fees 2(1−γ)(G g +T g), so Πg p = 2γRg B + 2(1−γ)(G g +T g). Hence,
V g data = Πg p −Π g p,no = 2γGg + 2(1−γ)(G g +T g) = 2Gg + 2(1−γ)T g. Therefore, the platform provides the
data service if and only ifV g data ≥0, equivalently,G g + (1−γ)T g ≥0.□
Proof of Proposition 2.After seller 1 accepts, seller 2’s binding participation constraint givesF g 2|AC =
(1−γ)(R g B −R g U ) = (1−γ)(G g +T g). Following seller 1’s rejection, seller 2 accepts exclusive access when

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization5
F g 2|RE = (1−γ)(R g I −R g N ). IfR g I ≥R g N , this continuation requires no subsidy and is implemented with
probability one; ifR g I < Rg N , it is implemented with probabilityη g. Hence, seller 1’s expected rejection
payoff is (1−γ)[ξ g(ηg)Rg U + (1−ξ g(ηg))Rg N ]. Equating this with its acceptance payoff (1−γ)R g B −F g 1
yieldsF g 1 = (1−γ)[G g +ξ g(ηg)T g], proving part (A). On the equilibrium path, fee revenue isF g 1 +F g 2|AC =
2(1−γ)G g + [1 +ξ g(ηg)](1−γ)T g, while commission revenue increases by 2γG g. Therefore,V g data(ηg) =
2Gg + [1 +ξg(ηg)](1−γ)T g, proving part (B). WhenR g I < Rg N ,ξ g(ηg) =η g, so∂V g data(ηg)/∂η g = (1−γ)T g.
Thus, data value weakly increases with credibility whenT g ≥0 and decreases whenT g <0.□
Proof of Proposition 3.Since entering and subsequently not purchasing yields zero utility, all consumers
enter. Givenp 1, p2 ≥0, seller 1’s demand is determined by the participation boundaryv−p 1 and the indif-
ferent consumer (1−p 1 +p 2)/2; seller 2 is symmetric.
(1) Ifp 1 +p 2 ≥2v−1, the participation constraints bind before the two demands meet, so each seller
locally solves max pi≥0 pi(v−p i) subject top i +p j ≥2v−1. The symmetric candidate isp i =v/2 whenv <1
and the boundary pricep i =v− 1 2 whenv≥1.
(2) Ifp 1 +p 2 ≤2v−1, the market is covered and seller 1 solves max p1≥0 p1(1−p 1 +p 2)/2 subject to
p1 +p 2 ≤2v−1, with the symmetric problem for seller 2. The symmetric candidate is the boundary price
pi =v− 1 2 whenv < 3 2 and the unconstrained pricep i = 1 whenv≥ 3 2 . Comparing the feasible candidates
across the two regions givesp NDC i,∅ =v/2 forv <1,p NDC i,∅ =v− 1 2 for 1≤v < 3 2 , andp NDC i,∅ = 1 forv≥ 3 2 .
Letp NDC ∅ denote this common equilibrium price andd NDC = min{v−p NDC ∅ , 1 2 }each seller’s demand.
Thenr NDC i =p NDC ∅ dNDC,π NDC i = (1−γ)r NDC i , Π NDC p = 2γrNDC i ,CS NDC = 2 R dNDC 0 (v−p NDC ∅ −x)dx, and
SW NDC =CS NDC + 2rNDC i . Moreover,D NDC = 2dNDC = min{v,1}.□
Proof of Proposition 4.The MDC subgame equilibria in Online Appendix EC.1.1 giveR MDC B =r P P M,
RMDC I =r P N M 1 ,R MDC U =r P N M 2 , andR MDC N =r NDC. Substituting the corresponding subgame revenues yields
Table EC.3.1.
Table EC.3.1F MDC 1 and Its Components in Different Market Conditions
Conditionsv−c≤ 1 2 1 2 < v−c <3 4 3 4 ≤v−c≤1v−c >1
GMDC −rNDC (2v−2c−1)2 4 −r NDC (2v−2c−1)2 4 −r NDC 1 4 −r NDC
T MDC rNDC rNDC rNDC − 1 8 rNDC − 1 8
F MDC 1 = (1−γ)(G MDC +T MDC) 0 (1−γ) (2v−2c−1)2 4 (1−γ) h (2v−2c−1)2 4 − 1 8 i 1−γ 8
Notes:Seller revenue under NDC isr NDC = v2 4 ifv≤1,r NDC = 2v−1 4 if 1< v <3 2 , andr NDC = 1 2 ifv≥ 3 2 .
Hence,G MDC =r P P M−r NDC <0 andT MDC =r NDC −r P N M 2 >0. By Lemma 1, bilateral adoption is
implemented withF MDC 1 =F MDC 2|AC = (1−γ)(r P P M−r P N M 2 ) = (1−γ)(G MDC +T MDC) andF MDC 2|RE = (1−
γ)(r P N M 1 −r NDC), proving part (A). By Proposition 1, the platform’s incremental profit from provision is
2[GMDC + (1−γ)T MDC]. SinceT MDC >0, provision occurs if and only ifγ≤1 +G MDC/T MDC, proving part
(B). Conditional on provision, both sellers adopt and the “PP” subgame applies. Lemma EC.1.1 then gives
the equilibrium entry set and the personalized prices.□
Proof of Proposition 5.Based on Proposition 4, when the platform does not monetize data, the equilibrium
coincides with NDC. When it monetizes data, the resulting market outcomes are reported in Table EC.3.2.
•Market coverage.Under NDC,D NDC = min{v,1}. Conditional on data monetization under MDC, Lemma
EC.1.1 givesD MDC = [min{2(v−c)−1,1}] +. Ifv <1, thenD MDC < v=DNDC. Ifv≥1, thenD NDC = 1 and
DMDC ≤1, with equality if and only ifv−c≥1. Hence,D MDC ≤D NDC, with equality if and only ifv−c≥1.
•Profits of the sellers and the platform.For selleri∈ {1,2}, under MDC with data monetization,
we haveπ NDC i −π MDC i = (1−γ)(r NDC −r P N M 2 ) = (1−γ)T MDC ≥0. Hence,π NDC i > πMDC i . The platform
monetizes data only if Π MDC p ≥Π NDC p . Therefore, Π MDC p ≥Π NDC p holds.

6Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Table EC.3.2 Equilibrium Outcomes when the Platform Provides Data Service under MDC
Conditionsπ MDC 1 =π MDC 2 ΠMDC p CS MDC SW MDC
1
2 < v≤ 3 4 , c < v−1 2 , γ≤(2v−2c−1)2 v2 0 (2v−2c−1)2 2 (2v−2c−1)2 4 3(2v−2c−1)2 4
2+
√
2
4 < v≤1, c≤v− 2+
√
2
4 , γ≤2(2v−2c−1)2−1 2v2−1 1−γ 8 (2v−2c−1)2 2 − 1−γ 4 (2v−2c−1)2 4 3(2v−2c−1)2 4
3
4 < v≤1, v−3 4 < c < v−1 2 , γ≤(2v−2c−1)2 v2 0 (2v−2c−1)2 2 (2v−2c−1)2 4 3(2v−2c−1)2 4
1< v <3 2 ,0< c < v−1, γ≤ 1 4v−3 1−γ 8 1+γ 4 v−c− 3 4 v−c− 1 4
1< v <3 2 , v−3 4 < c < v−1 2 , γ≤(2v−2c−1)2 2v−1 0 (2v−2c−1)2 2 (2v−2c−1)2 4 3(2v−2c−1)2 4
1< v <3 2 , v−1≤c≤v− 2+
√
2
4 , γ≤2(2v−2c−1)2−1 4v−3 1−γ 8 (2v−2c−1)2 2 − 1−γ 4 (2v−2c−1)2 4 3(2v−2c−1)2 4
v≥ 3 2 ,0< c < v−1, γ≤1 3 1−γ 8 1+γ 4 v−c− 3 4 v−c− 1 4
v≥ 3 2 , v−1≤c≤v− 2+
√
2
4 , γ≤2(2v−2c−1)2−1 3 1−γ 8 (2v−2c−1)2 2 − 1−γ 4 (2v−2c−1)2 4 3(2v−2c−1)2 4
v≥ 3 2 , v−3 4 < c < v−1 2 , γ≤(2v−2c−1)2 2 0 (2v−2c−1)2 2 (2v−2c−1)2 4 3(2v−2c−1)2 4
•Consumer surplus and social welfare.Ifv≤1,CS MDC −CS NDC = [(2v−2c−1) 2 −v 2]/4<0 and
SW MDC −SW NDC = 3[(2v−2c−1) 2 −v 2]/4<0. If 1< v < 3 2 andc < v−1, thenCS MDC −CS NDC =
v−c−1>0 andSW MDC −SW NDC =−c <0; ifv−1≤c < v− 1 2 , then 2v−2c−1≤1, soCS MDC ≤CS NDC
andSW MDC −SW NDC ≤1−v <0. Finally, ifv≥ 3 2 andc < v−1, thenCS MDC −CS NDC = 1 2 −c, while
SW MDC −SW NDC =−c <0; ifv−1≤c < v− 1 2 , thenCS MDC −CS NDC ≤ 3 2 −v≤0 andSW MDC −SW NDC ≤
1−v <0. Therefore,CS MDC > CSNDC exactly when 1< v < 3 2 andv−c >1, orv≥ 3 2 andc < 1 2 , while
SW MDC < SWNDC throughout the monetization regions.□
Proof of Proposition 6.Online Appendix EC.1.2 givesR VDD B =r P P VandR VDD I =R VDD U =R VDD N =
rNDC because unilateral access induces no disclosure. Hence,T VDD = 0. By Lemma 1,F VDD 1 =F VDD 2|AC =
(1−γ)(r P P V−r NDC) = (1−γ)G VDD andF VDD 2|RE = 0, proving part (A). The platform’s incremental profit is
therefore 2GVDD, so it provides the service if and only ifG VDD ≥0 and the selected opt-in set is nonempty.
DefineP 1 ={(v, c) : 1 2 < v≤1, c≤v− 1 2 }andP 2 ={(v, c) :v >1, c= min{v− 1 2 ,1}}. Leth ±(v) =
[v+ 3±
√
−16v2 + 40v−8]/17, ¯v1 = (3 + √ 2)/2, and ¯v2 = (5 + √ 17)/4, and define
P3 =
n
(v, c) :3 2 < v≤¯v1, v−1 + 1 4(v−1) ≤c≤v−1 +h +(v) o
∪

(v, c) : ¯v1 < v≤ 9 4 ,2v−3≤c≤v−1 +h +(v)
∪

(v, c) :9 4 < v≤¯v2, v−1 +h −(v)≤c≤v−1 +h +(v) 	 .
(1) For 1 2 < v≤1 and 0< c≤v− 1 2 ,G VDD = (v−c− 1 2 )2 ≥0 whenc≥ 3v 2 −1, andG VDD = (5v−4c−
3)(1−v)/4≥0 otherwise. The opt-in set is nonempty, including{1/2}atc=v− 1 2 , givingP 1.
(2) For 1< v≤ 3 2 ,G VDD = (1−v)/2<0 whenc≤v−1 andG VDD = (v−1)(1−2v+ 2c)/2<0 when
v−1< c < v−1 2 . Atc=v− 1 2 ,G VDD = 0 and ΩP P V={1/2}, giving the corresponding part ofP 2.
(3) Forv > 3 2 andc <1, Lemma EC.1.4 givesG VDD =−1/4<0 under full disclosure. Ifv−1< c <1, then
GVDD =−1/4 + (v−1)(1−v+c)<−(v− 3 2 )2 <0. Hence, provision does not occur forc <1. OnP 3, instead,
ΩP P V= [1−v+c, v−c] andr P P V= 1/4 + (v−1)(1−v+c); the defining bounds implyc≥v−1 + 1/[4(v−1)],
soG VDD =−1/4 + (v−1)(1−v+c)≥0. Finally, whenc≥1 and (v, c)/∈ P 3, the selected PP equilibrium
hasG VDD = 0, with Ω P P V={1/2}atc= 1 and Ω P P V=∅forc >1. Thus, provision occurs exactly on
P1 ∪ P2 ∪ P3, proving part (B).
Conditional on provision, Lemma EC.1.4 gives, for (v, c)∈ P 1 ∪ P3,p VDD i,∅ = max{v/2,2v−c−1}and
ΩVDD = [max{0,1−v+c},min{1, v−c}]; for (v, c)∈ P2,p VDD i,∅ =p NDC i,∅ and ΩVDD ={1/2}. Opt-in consumers
facep VDD 1 (x) = max{1−2x,0}andp VDD 2 (x) = max{2x−1,0}, while all others opt out.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization7
It remains to compare personalized and uniform prices. For (v, c)∈ P1 ∪ P3, the largest personalized price
charged by seller 1 to an opt-in consumer is 2v−2c−1, whilep VDD 1,∅ ≥2v−c−1>2v−2c−1 because
c >0; the argument for seller 2 is symmetric. For (v, c)∈ P2, the only opt-in consumer is atx= 1/2, where
pVDD 1 (1/2) =p VDD 2 (1/2) = 0< pNDC i,∅ . Hence,p VDD i (x)< pVDD i,∅ for everyx∈Ω VDD andi= 1,2.□
Proof of Proposition 7.Based on Proposition 6, when the platform does not monetize data, the equilibrium
coincides with NDC. When it monetizes data, the resulting market outcomes are reported in Table EC.3.3.
Table EC.3.3 Equilibrium Outcomes when the Platform Provides Data Service under VDD
Conditionπ V DD 1 =π V DD 2 ΠV DD p CS V DD SW V DD
(v, c)∈ P1, c≥3v 2 −1 (1−γ) v2 4 γv 2+(2v−2c−1)2 2 v2+(2v−2c−1)2 4 3v2+3(2v−2c−1)2 4
(v, c)∈ P1, c <3v 2 −1 (1−γ) v2 4 γv 2+(1−v)(5v−4c−3) 2 4(1−v+c)2+(2v−2c−1)2 4 4v2+12c2−(2v−1+2c)2 4
(v, c)∈ P3 (1−γ) 1 2 γ− 1 2 + 2(v−1)(1−v+c) 4(1−v+c)2+(2v−2c−1)2 4 4v2+12c2−(2v−1+2c)2 4
(v, c)∈ P2 (1−γ)r N DC 2γr N DC CS N DC SW N DC
1. Impact on prices.•VDD vs. MDC.By Propositions 4 and 6, onP 1 ∪ P3, Ω VDD = ΩMDC =
[max 0,1−v+c,min 1, v−c], and opt-in consumers face the same personalized pricesp 1(x) = max 1−2x,0
andp 2(x) = max 2x−1,0. OnP 2 withv≤ 3 2 ,c=v− 1 2 and both entry sets equal 1/2. Ifv > 3 2 , thenc= 1,
ΩVDD = 1/2, and ΩMDC = [max 0,2−v,min 1, v−1].
•VDD vs. NDC.consider seller 1; seller 2 follows symmetrically. OnP 1,p NDC 1,∅ =v/2 andp VDD 1,∅ =
maxv/2,2v−c−1, so the inequality is strict if and only ifc <3v/2−1, which requiresv >2/3. OnP 2, the two
uniform prices coincide. OnP 3,p VDD 1,∅ = 2v−c−1>1 =p NDC 1,∅ . Hence, the stated uniform-price comparison
follows. For an opt-in consumer withx≤1/2,p VDD 1 (x) = 1−2x. OnP 1, this exceedsp NDC 1,∅ =v/2 if and only
ifx <(2−v)/4. Since the left disclosure boundary is 1−v+c, such consumers exist if and only if 1−v+c <
(2−v)/4, orc <3v/4−1/2, which requiresv >2/3. Thus, the relevant interval is [1−(v−c),(2−v)/4). On
P2, the only opt-in consumer is atx= 1/2 and pays zero, while onP 3,p VDD 1 (x)≤1 =p NDC 1,∅ . Symmetry gives
seller 2’s interval ((2 +v)/4, v−c].
2. Impact on market coverages.The comparisons of the market coverage across alternative privacy
regulations are summarized in Table EC.3.4. It follows that when the platform monetizes data under both
MDC and VDD,D VDD = min{DMDC +D NDC,1}is satisfied.□
Table EC.3.4 Market Coverage Across Alternative Privacy Regulations
Regime and condition Market coverage
NDCD N DC= min{v,1}
MDC, service providedD M DC= [min{2v−2c−1,1}] +
MDC, service withheldD M DC= min{v,1}
VDD, service providedD V DD= min{1, v+ [2v−2c−1] +}
Proof of Proposition 8.Conditional on provision under VDD, Lemma 1 givesπ VDD i = (1−γ)r NDC =π NDC i .
Under MDC, if the service is withheld,π MDC i =π NDC i ; if it is provided,π MDC i = (1−γ)r P N M 2 ≤(1−γ)r NDC
becauseT MDC =r NDC −r P N M 2 >0. Hence,π VDD i =π NDC i ≥π MDC i .
Since VDD provision requiresG VDD ≥0, Π VDD p = ΠNDC p + 2GVDD ≥Π NDC p . Under MDC, ΠMDC p = ΠNDC p +
2 max{GMDC + (1−γ)T MDC,0}. BecauseG VDD ≥0, Π VDD p ≥Π MDC p if and only ifG VDD ≥G MDC + (1−
γ)T MDC. UsingG VDD −G MDC =r P P V−r P P MandT MDC >0, this is equivalent toγ≥1− rP P V−rP P M T MDC .
Sinceγ≥0, the condition can be written asγ≥γ V M(v, c) := max{0,1−rP P V−rP P M T MDC }.□

8Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Proof of Proposition 9.
•VDD vs. NDC.Define ∆ CS V N=CS VDD −CS NDC and ∆SW V N=SW VDD −SW NDC. We consider the regions
where the platform provides the service under VDD.
(1) If (v, c)∈ P1 andc≥ 3v 2 −1, then ∆ CS V N= (2v−2c−1)2 4 ≥0,∆ SW V N= 3(2v−2c−1)2 4 ≥0.
(2) If (v, c)∈ P1 andc < 3v 2 −1, then ∆ CS V N= h2(c) 4 , whereh 2(c) = 8c2 + (12−16v)c+ 5−12v+ 7v 2. For
2
3 < v≤
√
2
2 ,h 2(c)≥0 throughout this region. For
√
2
2 < v≤1,h 2(c)≥0 if and only ifc≥
4v−3+
√
2v2−1
4 .
Likewise, ∆SW V N= h3(c) 4 , whereh 3(c) = 8c2 + (4−8v)c−1 + 4v−3v 2. For 2 3 < v≤ 6+ √ 6 10 ,h 3(c)≥0 throughout
this region. For 6+
√
6
10 < v≤1,h 3(c)≥0 ifc≤
2v−1−
√
10v2−12v+3
4 or ifc≥
2v−1+
√
10v2−12v+3
4 .Atv= 1, both
differences equal−c(1−2c)<0 forc < 1 2 .
(3) If (v, c)∈ P3, then ∆CS V N=−c(2v−2c−1)−2G VDD <0 and ∆ SW V N=c(2c+ 1−2v) =−c(2v−2c−1)<0.
(4) If (v, c)∈ P2, only the midpoint discloses and aggregate outcomes equal those under NDC.
•VDD vs. MDC.Suppose the platform provides the service under both regimes. Define ∆ CS V M=CS VDD −
CS MDC and ∆SW V M=SW VDD −SW MDC.
(1) If (v, c)∈ P1 andc≥ 3v 2 −1, then ∆ CS V M= v2 4 >0 and ∆ SW V M= 3v2 4 >0.
(2) If (v, c)∈ P1 andc < 3v 2 −1, or if (v, c)∈ P3, lety= 1−v+c, theny >0 and 2v−y >0. Thus,
∆CS V M=y 2 >0 and ∆ SW V M=y(2v−y)>0.
(3) If (v, c)∈ P2, the outcomes under VDD equal those under NDC. Proposition 5 implies that consumer
surplus and social welfare under MDC are strictly below their NDC levels whenever MDC data provision.
Therefore, whenever both regimes provide the service,CS VDD > CSMDC andSW VDD > SWMDC.□
Proof of Proposition 10.A Pareto improvement over both NDC and MDC requiresπ VDD i ≥
max{πNDC i , πMDC i }fori= 1,2, Π VDD p ≥max{Π NDC p ,Π MDC p }, andCS VDD ≥max{CS NDC, CSMDC}. Under
VDD,π VDD i =π NDC i . Proposition 8 further givesπ VDD i ≥π MDC i . Hence, the seller condition always holds
whenever VDD monetizes data. By Proposition 9, apart from the zero-measure disclosure cases treated
below,CS VDD ≥CS NDC under VDD provision if and only if 1 2 < v≤
√
2
2 andc < v−1 2 , or
√
2
2 < v <1 and
4v−3+
√
2v2−1
4 ≤c < v−1 2 . The remaining weak-comparison cases are the upper boundaryc=v− 1 2 ofP 1 and
P2. In these cases only the midpoint discloses and all aggregate VDD outcomes equal NDC, so VDD does not
yield a Pareto improvement over NDC. Moreover,CS VDD > CSMDC whenever MDC also monetizes data,
whileCS MDC =CS NDC otherwise. Therefore, the consumer condition is exactly the set of conditions above
(v, c). The Proposition 8 shows that ΠVDD p ≥Π NDC p . Comparing with MDC, if MDC does not monetize data,
ΠMDC p = ΠNDC p and the platform condition holds automatically. If MDC also monetizes data, Proposition 8
implies that, within the consumer conditions above, Π VDD p ≥Π MDC p if and only ifγ≥γ win(v, c), where
γwin(v, c) =



(3v−2c−2)2
v2 , 2 3 < v <1, c <3v 2 −1,
0,otherwise within the aboveCS VDD ≥max{CS NDC, CSMDC}regions.
Therefore, VDD yields a Pareto improvement over both NDC and MDC if 1 2 < v≤
√
2
2 andc < v−1 2 , or √
2
2 < v <1 and
4v−3+
√
2v2−1
4 ≤c < v−1 2 , withγ≥γ win(v, c).□
Proof of Proposition 11.Atp i,∅ =p NDC i,∅ , the disclosure conditions in Lemma EC.1.4 give positive-mass
disclosure ifc <min{v− 1 2 ,1}, with Ω UP = [ˆxUP,1−ˆxUP], where ˆxUP = max{1−v+c,(1 +c−p NDC ∅ )/2}. For
simplicity, denotep NDC ∅ =p NDC i,∅ , i∈ {1,2}. These prices are optimal under the cap. If ˆxUP ≥min{v−p NDC ∅ , 1 2 },
thenp NDC ∅ =v/2, and any feasible pricepyields anonymous revenue at mostp(v−p)≤v 2/4. Otherwise,
ˆxUP = (1 +c−p NDC ∅ )/2≥c/2. A deviation withp≥cyields at mostpˆx UP ≤p NDC ∅ ˆxUP, while one withp < c
yields at mostp[ˆxUP + (c−p)/2]≤cˆx UP < pNDC ∅ ˆxUP. Any symmetric price belowp NDC ∅ admits a profitable
small increase. Hence,p UP i,∅ =p NDC i,∅ . Each seller then earnsr UP =p NDC ∅ min{ˆxUP, v−pNDC ∅ , 1 2 }+ ( 1 2 −ˆxUP)2.
For 1 2 < v <1 and 0< c < v−1 2 , this givesG UP = (v−c− 1 2 )2 ifc≥ 3v 2 −1, andG UP = (4v−5v 2 + 4c2)/16

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization9
otherwise. Thus,G UP ≥0 exactly when 4c 2 ≥5v 2 −4v. Forv≥1, positive-mass disclosure givesG UP =
[c2 −(p NDC ∅ )2]/4<0. Atv > 1 2 andc= min{v− 1 2 ,1}, onlyx= 1 2 discloses andG UP = 0; otherwise the
disclosure set is empty. Since exclusive access still induces no disclosure, the threat effect is zero. The
maintained provision rule gives part (A).
The cap preserves every consumer’s NDC anonymous-purchase option, while disclosure is voluntary. Hence,
U UP(x)≥U NDC(x) for allxandCS UP ≥CS NDC. Under provision,SW UP −SW NDC =CS UP −CS NDC +
2GUP ≥0; without provision, UP coincides with NDC. This proves part (B).
If MDC also provides, its personalized offers remain available through disclosure under UP, while UP
additionally permits anonymous purchasing without privacy cost. Thus,U UP(x)≥U MDC(x) andCS UP ≥
CS MDC. Moreover, Lemma 1 givesπ UP i =π NDC i andπ MDC i = (1−γ)(r NDC −T MDC)≤π NDC i , proving the first
statement in part (C). For platform profit, endogenous MDC provision gives ΠMDC p = ΠNDC p + 2 max{GMDC +
(1−γ)T MDC,0}, whereas UP provision gives Π UP p = ΠNDC p + 2GUP. SinceG UP ≥0, Π UP p ≥Π MDC p if and
only ifr UP −r MDC ≥(1−γ)T MDC, equivalently,γ≥γ U M(v, c). Positive-mass UP provision requiresv <1
andc < v−1 2 . A positive measure of central consumers then obtains positive utility under UP while being
unserved under NDC, soCS UP > CSNDC. If MDC provides,π UP i > πMDC i becauseT MDC >0; otherwise MDC
coincides with NDC. Thus, positive-mass disclosure together withγ≥γ U M(v, c) yields a Pareto improvement
over both benchmarks. Conversely, without positive-mass disclosure, UP reproduces NDC aggregate payoffs,
while ifγ < γU M(v, c) the platform is worse off than under MDC. The conditions are necessary and sufficient.
□
Proof of Proposition 12.(1) Optimal data access. Under no access, platform profit is Π g N = 2γR g N .
Under bilateral access, Lemma 1 gives Π g B = 2Rg B −2(1−γ)R g U , so Π g B −Π g N = 2[Gg + (1−γ)T g]. To
implement exclusive access for seller 1, setF g 2|AC >(1−γ)(R g B −R g U ),F g 1 = (1−γ)(R g I −R g U ), andF g 2|RE =
(1−γ)(R g I −R g N ). The resulting profit is Π g E =R g I + (2γ−1)R g U , so Π g E −Π g N =R g I −R g U −2γT g. Exclusive
access for seller 2 yields weakly less, since the profit difference is (1−γ)(R g N −R g U ) = (1−γ)T g ≥0. Finally,
Πg B −Π g E = 2Rg B −R g I −R g U . Comparing Π g N ,Π g B,Π g E proves part (A).
(2) MDC. Under unilateral MDC,R M DC I +R M DC U = 0 ifv−c < 3 4 , (v−c− 3 4 )2 + 1 8 if 3 4 ≤v−c <
3
2 , and 11 16 ifv−c≥ 3 2 . Ifv≤1, positive unilateral revenue requiresv > 3 4 , andR M DC I +R M DC U < 3 16 <
v2
2 = 2RM DC N . If 1< v < 3 2 , thenv−c < vand 2R M DC N −R M DC I −R M DC U > 3 8 −(v− 5 4 )2 >0. Ifv≥ 3 2 ,
RM DC I +R M DC U ≤ 11 16 <1 = 2R M DC N . Hence,R M DC I +R M DC U <2R M DC N . Together withG M DC<0, neither
bilateral nor exclusive access increases total seller sales revenue relative to NDC. Direct substitution gives
2RM DC B ≥R M DC I +R M DC U if and only ifv−c≤(3 + √ 6)/4. Thus, exclusive access can be optimal only
ifv−c >(3 +
√
6)/4>1. Under exclusive access,F M DC 1 = (1−γ)(R M DC I −R M DC U ), so both sellers earn
πM DC i = (1−γ)R M DC U <(1−γ)R M DC N =π N DC i becauseT M DC>0. Whenv−c >1, NDC covers the entire
market and assigns each consumer to the closer seller. Exclusive MDC introduces privacy costs and allocates
a positive measure of consumers to the more distant seller, while possibly also reducing coverage. Hence,
SW M DC< SWN DC. Under exclusive MDC, the entry set is [max{0, 3 2 −v+c},1], and each entrant obtains
utilityv−c− 3 2 +x. Therefore,CS M DC= 1 2 (v−c− 1 2 )2 ifv−c < 3 2 , andCS M DC=v−c−1 otherwise. For
1< v <3 2 , the exclusive-access conditionv−c >(3 + √ 6)/4 impliesCS M DC> 1 4 =CS N DC. Forv≥ 3 2 and
v−c < 3 2 ,CS M DC> CSN DCis equivalent toc < v− 1 2 − q 2v− 5 2 ; forv−c≥ 3 2 , it is equivalent toc < 1 4 .
Combining these cases gives the regions in part (B).
(3) VDD. Under exclusive VDD, no consumer discloses, soRVDD I =R VDD U =R VDD N andT VDD = 0. Exclusive
access therefore yields Π VDD E = 2γRVDD N , identical to NDC, while generating no usable information. Under
the maintained provision convention, the platform therefore does not implement exclusive access.□
Proof of Proposition 13.When neither seller adopts, consumers incur no privacy cost, soR g−h N =r NDC
forg∈ {MDC,VDD}. The contracting argument in Lemma 1 is unchanged and givesF g−h 1 =F g−h 2|AC =

10Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
(1−γ)(R g−h B −R g−h U ). Hence, conditional on bilateral provision,π g−h i = (1−γ)R g−h U and Π g−h p −Π NDC p =
V g−h data = 2Gg−h + 2(1−γ)T g−h. Write [z] + ≜max{z,0}and [z] b a ≜min{max{z, a}, b}
(1) MDC. The bilateral MDC argument in Proposition 4 and Lemma EC.1.1 applies separately to each
privacy type after replacingcwithc k. Privacy costs are sunk at the pricing stage, so personalized prices do
not depend on the distribution of privacy types. Because each type is uniformly distributed over locations,
aggregate bilateral outcomes are the weighted averages of the corresponding homogeneous-cost outcomes.
This aggregation holds conditional on bilateral access, not after the platform’s endogenous provision decision.
In particular,R MDC−h B =ρ rP P M

 c=cH + (1−ρ)r P P M

 c=cL . Proposition 4 establishesr P P M< rNDC for
everyc >0, soR MDC−h B < rNDC andG MDC−h <0. The same weighting applies to coverage and welfare. For
v≤1, the baseline bilateral entry intervals give coverage 2[v−c k − 1 2 ]+ < vand welfare 3[v−c k − 1 2 ]2 + <3v 2/4
per unit mass of type-kconsumers. Forv >1, NDC serves every consumer through the closer seller without
privacy costs. Bilateral MDC either preserves a transaction while adding a positive privacy cost or eliminates
a transaction with positive social surplus. Thus, each type has weakly lower coverage and strictly lower welfare
than NDC. Weighting these comparisons yieldsD MDC−h ≤D NDC andSW MDC−h < SWNDC whenever the
service is provided.
The unilateral revenue comparison requires a separate argument because the uninformed seller charges a
common uniform price. Suppose only seller 1 has access, and letp=p P N M−h 2,∅ . A type-kconsumer purchasing
from seller 2 must satisfyv−p−(1−x)−c k ≥0 by voluntary entry and rational expectations. Sincec k ≥c L,
seller 2’s demand is at most [v−c L −p] +. Thus, forv≤1,R MDC−h U ≤max p≥0 p[v−c L −p] + = [v−c L]2 +/4<
v2/4 =r NDC. Forv >1, a consumer purchasing from seller 2 must also satisfyx≥(1 +p)/2; otherwise, seller
1 can profitably attract her with a nonnegative personalized price. Hence,R MDC−h U ≤max p≥0 p[(1−p)/2] + =
1/8< rNDC. Therefore,T MDC−h >0, and the data-value identity gives the stated MDC provision condition.
For consumer surplus, letCS MDC−h k denote surplus per unit mass of type-kconsumers under bilateral
provision. Applying the baseline entry utilities type by type givesCS MDC−h k = R 1 0 [v−max{x,1−x} −ck]+ dx.
Consequently,CS MDC−h H ≤CS MDC−h L andCS MDC−h =ρCS MDC−h H + (1−ρ)CS MDC−h L . Defineρ ′ = 1 if
CS MDC−h H ≥CS NDC,ρ ′ = 0 ifCS MDC−h L < CSNDC, andρ ′ = (CSMDC−h L −CS NDC)/(CS MDC−h L −CS MDC−h H )
otherwise. The last case satisfiesCS MDC−h H < CSNDC ≤CS MDC−h L , so its denominator is strictly positive.
Rearranging the weighted-average inequality proves the stated condition, including cases with equal type-
specific surplus.
(2) VDD. The nondisclosure argument in Lemma EC.1.5 applies separately to each privacy type because it
holds for any anticipated uniform prices and requires onlyc >0. Replacingcwithc k, anonymity improves each
consumer’s utility over disclosure by at leastc k >0. Hence, both types opt out under unilateral access, and
all consumers enter because anonymous entry allows nonpurchase at zero utility. The continuation therefore
coincides with NDC, givingR VDD−h I =R VDD−h U =R VDD−h N =r NDC andT VDD−h = 0. By Proposition 1,
V VDD−h data = 2GVDD−h. Thus, the platform provides the service if and only ifG VDD−h ≥0 and the opt-in set is
nonempty. It remains to establish the uniform-price comparison. Suppose a symmetric bilateral equilibrium
satisfiesp P P V−h i,∅ < pNDC i,∅ . For a type-kconsumer atx≤ 1 2 , disclosure yields [v−1 +x] + −c k, whereas
anonymity yields [v−p P P V−h i,∅ −x] +. The disclosure gain is nondecreasing inx, so anonymous consumers
form intervals adjacent to the endpoints. Sincep P P V−h i,∅ < pNDC i,∅ ≤1 andc k >0, these intervals have positive
length. A small upward deviation in the uniform price leaves disclosure and personalized-price revenue
unchanged. For a type whose anonymous interval ends strictly before min{v−pP P V−h i,∅ , 1 2 }, a sufficiently small
increase preserves demand and raises revenue. Otherwise, the local demand response coincides with NDC.
The corresponding revenue derivative isv−2p P P V−h i,∅ ifv−p P P V−h i,∅ < 1 2 , (1−p P P V−h i,∅ )/2 ifv−p P P V−h i,∅ > 1 2 ,
and 1 2 −p P P V−h i,∅ at equality, using the right derivative. By Proposition 3, each derivative is strictly positive
whenp P P V−h i,∅ < pNDC i,∅ . Thus, a small price increase raises revenue for both types, contradicting equilibrium.
Therefore,p P P V−h i,∅ ≥p NDC i,∅ . This proves part (B).

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization11
The personalized-pricing argument underlying Proposition 7 applies separately to each privacy type.
Under bilateral access, disclosure offers the same personalized prices under MDC and VDD, yielding utility
[v−max{x,1−x}] + −c k. VDD preserves this purchasing opportunity while allowing consumers to remain
anonymous. Thus, every consumer obtains weakly higher utility under VDD, and every consumer purchasing
under MDC continues purchasing under VDD, apart from measure-zero indifference boundaries. Aggregating
across types givesCS VDD−h ≥CS MDC−h andD VDD−h ≥D MDC−h.
For social welfare, consumers purchase from the closer seller under either bilateral regime. A consumer
purchasing under MDC who continues disclosing under VDD retains the same allocation and privacy cost,
whereas one who switches to anonymity avoids the privacy cost without changing the allocation. Any addi-
tional VDD buyer purchases anonymously and generates nonnegative social surplus, since voluntary purchase
at a nonnegative price impliesv−min{x,1−x} ≥0. Therefore,SW VDD−h ≥SW MDC−h. Finally, the con-
tracting argument in Proposition 8 applies unchanged to the heterogeneous revenue states. By Lemma 1 and
parts (A)–(B),π VDD−h i = (1−γ)r NDC =π NDC i andπ MDC−h i = (1−γ)(r NDC −T MDC−h)≤π NDC i . When both
regimes provide the service, ΠVDD−h p −Π MDC−h p = 2[GVDD−h −G MDC−h −(1−γ)T MDC−h]. SinceT MDC−h >0
andγ≥0, the difference is nonnegative if and only ifγ≥max{0,1−(G VDD−h −G MDC−h)/T MDC−h}.□
Proof of Proposition 14.(1) MDC. Under MDC, an exclusive adopter can identify consumers with
positive probability and exclusive access may remain informative. By Lemma 1,F MDC 1 (q) =F MDC 2|AC (q) =
(1−γ)[G MDC(q) +T MDC(q)]. Hence, the platform’s profit gain from bilateral provision is 2[G MDC(q) + (1−
γ)T MDC(q)], so it provides the service if and only ifG MDC(q) + (1−γ)T MDC(q)≥0.
(2) VDD. Under VDD, we first characterize the bilateral VDD-IQ pricing equilibrium, which characterizes
the bilateral revenueG VDD(q) and also supports the counterfactual results in Figures 6–7.
Lemma EC.3.1(Bilateral VDD equilibrium under imperfect identification).Under VDD-IQ
with both sellers purchase data service, all consumers enter, and the following results hold:
(A)For a candidate common uniform pricep, letˆx= max{0,1−v+c,(1 +c−p)/2}andd= min{ˆx,1/2}.
The opt-in set is[ˆx,1−ˆx]ifˆx≤1/2, and is empty otherwise. Identified consumers facep P P V 1 (x) = [1−2x] +
andp P P V 2 (x) = [2x−1] +.
(B)Definey(z, p) = [min{v−z,(1 +p−z)/2}] 1 0,A(y;d) = min{y, d}+ [y−(1−d)] +, andH(z;p, d, q) =
z[(1−q)y(z, p) +qA(y(z, p);d)]. Thenpis a symmetric pure-strategy rational-expectations equilibrium price
if and only ifp∈arg max z≥0 H(z;p, d, q), holdingdfixed. Global optimality can be checked at the breakpoints
and interior stationary points of the quadratic branches.
(C)If 1 2 < v <1and0< c < v−1 2 , a symmetric equilibrium exists with a unique common uniform price and
disclosure set. Leta= 1−v+candb q =v(1−q)/(2−q). Ifa < b q, thend= (1−q)(2 + 2c−v)/(4−3q)and
p=v/2 +q(2 + 2c−v)/[2(4−3q)]. Ifb q ≤a < v/2, then(d, p) = (a, v−a). Ifa≥v/2, then(d, p) = (a, v/2).
When multiple symmetric equilibria satisfy part (B), we apply the maintained selection rule, maximizing
each seller’s sales revenue and breaking ties in favor of greater disclosure. Next, we suppose only seller
1 has data access. If a consumer opts in, she is identified with probabilityq, in which case her utility is
U in(x) = max{0, v−p2,∅ −(1−x)} −c; with probability 1−q, identification fails and she obtainsU out(x),
whereU out(x) = max{0, v−p1,∅ −x, v−p2,∅ −(1−x)}. At the anticipated equilibrium prices, opting in yields
expected utilityq[max{0, v−p 2,∅ −(1−x)} −c] + (1−q)U out(x)≤U out(x)−qc < Uout(x) for everyq >0.
Hence, no consumer discloses under unilateral access. Therefore,R VDD I (q) =R VDD U (q) =R VDD N (q) =r NDC
andT VDD(q) = 0 forq∈(0,1]. Atq= 0, no usable information is generated, soT VDD(0) = 0 as well. By
Lemma 1,F VDD 1 (q) =F VDD 2|AC (q) = (1−γ)G VDD(q) andF VDD 2|RE (q) = 0. Hence,V VDD data (q) = 2GVDD(q). Under
the maintained convention that the service is not activated when the equilibrium opt-in set is empty, the
platform provides the service if and only ifG VDD(q)≥0 and the opt-in set is nonempty.□

12Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Appendix EC.4: Proofs of Results in Appendix
Proof of Lemma EC.1.1.We solve the subgame by backward induction. Conditional on entry, the privacy
costcis sunk, so not purchasing yields utility−c. Considerx≤ 1 2 . Seller 1 has mismatch-cost advantage
1−2x. If seller 2 can generate positive gross surplus at zero price, Bertrand competition yieldsp 2(x) = 0 and
p1(x) = 1−2x, leaving gross surplusv−(1−x); otherwise, seller 1 extracts the full gross surplusv−x. Thus,
continuation utility from entry is maxv−(1−x),0−c. Sincec >0, entry occurs if and only ifx≥1−(v−c).
Symmetrically, forx≥ 1 2 , entry requiresx≤v−c. Hence, the entry set is empty ifv−c < 1 2 , [1−(v−c), v−c]
if 1 2 ≤v−c <1, and [0,1] ifv−c≥1, equivalent to the regions in the lemma. For every entering consumer
withx≤ 1 2 ,v−(1−x)≥c >0, so both sellers can profitably serve the consumer and Bertrand competition
givesp P P M 1 (x) = 1−2xandp P P M 2 (x) = 0. Symmetrically, forx≥ 1 2 ,p P P M 1 (x) = 0 andp P P M 2 (x) = 2x−1.
Therefore, for allx∈Ω P P M,p P P M 1 (x) = max{1−2x,0}andp P P M 2 (x) = max{2x−1,0}.□
Proof of Lemma EC.1.2.Fix an anticipated entry set [ˆx P N M,1]. Under the maintained tie-breaking
rule, the informed seller can attain the highest personalized price that leaves the consumer weakly preferring
its offer to the uninformed alternative. Given seller 2’s uniform pricep2,∅, seller 1’s optimal personalized price
is ˆp1(x, p2,∅) = max{0,min{v−x,1 +p 2,∅ −2x}}. Hence, a consumer enters if and only ifx≥1−(v−c−p 2,∅).
For an interior REE, rational expectations therefore requirep 2,∅ = ˆxP N M+v−c−1.
Conditional on ˆxP N M, seller 2’s demand at pricepisD 2(p,ˆxP N M) = [1−max ˆxP N M,(1 +p)/2,1−v+p] +.
At an interior fixed point, 1−v+p= ˆx P N M−c <ˆxP N M, so the participation constraint is locally slack. If
ˆxP N M< v−c, seller 2’s local revenue isp(1−p)/2, which requiresp= 1 2 and hence ˆxP N M= 3 2 −(v−c). This
fixed point exists if and only ifv−c≥ 3 4 . Moreover, when ˆxP N M≤ 3 4 ,pD 2(p,ˆxP N M)≤p(1−p)/2≤ 1 8 , and
p= 1 2 attains the bound, so it is globally optimal. If ˆxP N M> v−c, seller 2’s revenue is locally increasing in
p, so no fixed point exists. If ˆx P N M=v−c, the fixed-point price isp= 2(v−c)−1, which is optimal only
whenv−c≥ 3 4 . Thus, for 3 4 < v−c≤1, there is also an equilibrium with entry set [v−c,1]; the largest-entry
selection chooses ˆxP N M= 3 2 −(v−c). Ifv−c≥ 3 2 , this threshold is nonpositive and all consumers enter.
Therefore, ΩP N M= [max 0,3 2 −(v−c),1] wheneverv−c≥ 3 4 , and is empty otherwise.
Finally, substitutingp P N M 2,∅ = 1 2 into seller 1’s best response givesp P N M 1 (x) = max{0,min{v−x, 3 2 −2x}}.
For every entrant withx≤ 3 4 ,x≥max{0, 3 2 −(v−c)}> 3 2 −v, so 3 2 −2x < v−x; forx≥ 3 4 , the optimal price
is zero. Hence,p P N M 1 (x) = max{3 2 −2x,0}.□
Proof of Remark 1.Consider the candidate entry threshold ˆx P N M=v−c. Sincev−c > 3 4 , seller 2’s
best response isep P N M 2,∅ = 2(v−c)−1. Substituting this price into the entry threshold 1−(v−c−p 2,∅)
returnsv−c, establishing rational-expectations consistency. Seller 2 then serves consumers in (v−c,1]
and earnserP N M 2 = [2(v−c)−1][1−(v−c)]. Under the maximal-participation equilibrium,p P N M 2,∅ = 1 2 and
rP N M 2 = 1 8 . Hence,r P N M 2 −erP N M 2 = 2(v−c− 3 4 )2 >0. Moreover,c >0 andv−c > 3 4 implyv > 3 4 . Thus,
rNDC > 1 8 ≥erP N M 2 : ifv≤1,r NDC =v 2/4>9/64>1/8; if 1< v < 3 2 ,r NDC = (2v−1)/4>1/4; and ifv≥ 3 2 ,
rNDC = 1/2. Therefore, eT MDC =r NDC −erP N M 2 >0 and eT MDC −T MDC =r P N M 2 −erP N M 2 = 2(v−c− 3 4 )2 >0.
Since provision requiresG MDC + (1−γ)T MDC ≥0, the maximal-participation equilibrium yields the more
demanding monetization condition.□
Proof of Lemma EC.1.3.This subgame is symmetric to the “PN” subgame in Lemma EC.1.2 after
interchanging the two sellers and replacingxby 1−x. Hence, Ω N P M=∅ifv−c < 3 4 and ΩN P M= [0,min{v−
c− 1 2 ,1}] otherwise, withp N P M 2 (x) = max{2x− 1 2 ,0}andp N P M 1,∅ = 1 2 .□
Proof of Lemma EC.1.4.We restrict attention to symmetric pure-strategy rational-expectations equilibria
and select the equilibrium maximizing each seller’s sales revenue, breaking ties in favor of more disclosure.
Since entry yields at least zero utility, all consumers enter.

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization13
Letp e i,∅ be selleri’s anticipated uniform price. Consider an opt-in consumer withx≤ 1 2 . Once she discloses,
cis sunk. Forx≤ 1 2 , ifv≥1−x, seller 2 can serve her at price zero, so Bertrand competition givesp 1(x) =
1−2xandp 2(x) = 0, yielding utilityv−(1−x)−c. Ifv <1−x, seller 2 cannot profitably serve her, so
seller 1 chargesv−xwhenever a purchase occurs, yielding utility−c. Thus,U opt−in,e(x) = [v−(1−x)] + −c.
Symmetrically,U opt−in,e(x) = [v−x] + −cforx≥ 1 2 , soU opt−in,e(x) = [v−max{x,1−x}] + −c. Opting out
yieldsU opt−out,e(x) = max{0, v−pe 1,∅ −x, v−pe 2,∅ −(1−x)}. Forx≤ 1 2 , comparing these utilities shows that
disclosure is optimal if and only ifx≥1−v+c,x≥(1 +c−p e 1,∅)/2, andp e 2,∅ ≥c. The conditions forx≥ 1 2
are symmetric. Hence, whenp e 1,∅, pe 2,∅ ≥c, define ˆxP P V,e i = max{0,1−v+c,(1 +c−p e i,∅)/2}. The anticipated
disclosure set is [ˆxP P V,e 1 ,1−ˆxP P V,e 2 ] if ˆxP P V,e 1 + ˆxP P V,e 2 ≤1, and is empty otherwise.
Fix an interior disclosure set [ˆxP P V 1 ,1−ˆxP P V 2 ]. Since realized uniform prices are unobserved when disclo-
sure is chosen, a uniform-price deviation leaves this set and personalized-price revenue fixed. Letq i ≤ˆxP P V i
be selleri’s anonymous demand adjacent to its endpoint. Its price cannot exceedv−q i or 1 +p −i,∅ −2q i,
so anonymous revenue is at mostq i min{v−q i,1 +p −i,∅ −2q i}. The competition constraint cannot bind
in equilibrium. If it bound for both sellers, their two equalities would implyq 1 +q 2 = 1; if it bound only
for selleriwhile the rival’s valuation constraint bound,p i,∅ = 1 +v−q −i −2q i ≤v−q i would again imply
qi +q −i ≥1. Both contradict a positive disclosure interval. Thus, sellerimaximizesq i(v−q i) overq i ≤ˆxP P V i ,
givingq i = min{ˆxP P V i , v/2}andp P P V i,∅ = max{v/2, v−ˆxP P V i }.
Rational expectations requirep e i,∅ =p P P V i,∅ . Substituting the preceding price into ˆxP P V i = max{0,1−v+
c,(1 +c−p P P V i,∅ )/2}yields ˆx P P V i = 1−v+c. To see this, if ˆx P P V i ≥v/2, thenp P P V i,∅ =v/2; if the price-
dependent boundary exceeded 1−v+c, it would requirec <3v/2−1, whereas ˆx P P V i ≥v/2 would require
c≥3v/2−1, a contradiction. If ˆx P P V i < v/2, thenp P P V i,∅ =v−ˆx P P V i and consistency becomes ˆx P P V i =
max{1−v+c,(1−v+c+ ˆx P P V i )/2}, whose only solution is ˆxP P V i = 1−v+c. Therefore, ˆx P P V 1 = ˆxP P V 2 =
1−v+candp P P V i,∅ = max{v/2,2v−c−1}.
For an opt-in consumer withx≤ 1 2 ,x≥1−v+cimpliesv−x−(1−2x) =v−1 +x≥c >0, so the
competition constraint binds andp P P V 1 (x) = 1−2x; symmetrically,p P P V 2 (x) = 2x−1 forx≥ 1 2 . Hence,
pP P V 1 (x) = max{1−2x,0}andp P P V 2 (x) = max{2x−1,0}.
Let ˆxP P V= 1−v+c. It remains to rule out price reductions attracting anonymous consumers from the
opposite side. If ˆx P P V≥v/2, any deviation yields anonymous revenue at most max p≥0 p(v−p) =v 2/4,
which is attained in equilibrium. If 0<ˆx P P V<min{v/2,1/2}, thenp P P V ∅ =v−ˆx P P Vand revenue from
consumers on the seller’s own side cannot increase becauseq(v−q) is increasing forq≤ˆx P P V. A deviation
crossing the disclosure interval and servingq∈[ˆx P P V,2ˆxP P V] yields at mostq[p P P V ∅ + 4ˆxP P V−1−2q].
Maximizing this quadratic and comparing it withp P P V ∅ ˆxP P Vgivesp P P V ∅ ≤2 if ˆx P P V≤ 1 4 , andp P P V ∅ ≤
1 +
p
8ˆxP P V(1−2ˆxP P V) if ˆxP P V> 1 4 . These conditions always hold forv≤ 3 2 : the first follows fromp P P V ∅ <
2, while for ˆx P P V> 1 4 andp P P V ∅ >1,p P P V ∅ −1≤ 1 2 −ˆxP P Vand 8ˆxP P V(1−2ˆxP P V)−( 1 2 −ˆxP P V)2 =
( 1 2 −ˆxP P V)(17ˆxP P V− 1 2 )≥0. They also hold forv > 3 2 andc <1, becausep P P V ∅ = 1 +c−2ˆxP P V<2 and,
when ˆxP P V> 1 4 andp P P V ∅ >1,p P P V ∅ −1 =c−2ˆx P P V<1−2ˆxP P V≤ p 8ˆxP P V(1−2ˆxP P V).
If ˆxP P V 1 = ˆxP P V 2 = 0, the disclosure conditions requirec≤v−1 andp P P V i,∅ ≥1 +c. Conversely, these
conditions induce full disclosure. Since a realized uniform-price deviation cannot create anonymous demand
once all consumers have disclosed, any symmetric price weakly above 1 +csupports the outcome; we take
1 +cas a representative price.
If the disclosure set is empty or has zero measure, the uniform-price game coincides with NDC, with
pN DC ∅ =v/2 forv≤1,p N DC ∅ =v− 1 2 for 1< v≤ 3 2 , andp N DC ∅ = 1 forv > 3 2 . At these prices, the maximal
gain from disclosure is attained atx= 1 2 and equals min{v− 1 2 ,1} −c. Hence, no consumer discloses ifv≤ 1 2 ;
forv > 1 2 , the disclosure set is{1/2}whenc= min{v− 1 2 ,1}and is empty whenc >min{v− 1 2 ,1}. Atx= 1 2 ,
pP P V 1 (1/2) =p P P V 2 (1/2) = 0.

14Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
Forv≤ 3 2 , these conditions yield full disclosure whenv >1 andc≤v−1, interval disclosure [max{0,1−
v+c},min{1, v−c}] whenv > 1 2 and max{v−1,0}< c < v− 1 2 , singleton disclosure atc=v− 1 2 , and no
disclosure otherwise. Forv > 3 2 andc <1, full disclosure occurs whenc≤v−1, while the same interval
disclosure occurs whenv−1< c <1.
Finally, letv >3 2 andc≥1. The NDC-like equilibrium gives each seller revenue 1/2, while any full-disclosure
equilibrium gives 1/4 and is not selected. An interior-disclosure equilibrium has ˆx P P V= 1−v+c∈(0,1/2)
and revenue ( 1 2 −ˆxP P V)2 + (v−ˆxP P V)ˆxP P V= 1 4 + (v−1)ˆxP P V, so it is selected if and only if ˆx P P V≥
1/[4(v−1)], with equality selected because it induces more disclosure. The no-deviation condition additionally
requires ˆxP P V≥v−2 when ˆx P P V≤ 1 4 , and 17(ˆxP P V)2 −2(v+ 3)ˆxP P V+ (v−1) 2 ≤0 when ˆxP P V> 1 4 . The
latter has roots (v+ 3±
√
−16v2 + 40v−8)/17. Since 1/[4(v−1)] =v−2 atv= (3 + √ 2)/2, the smaller root
equals 1/4 atv= 9/4, and the roots are real up tov= (5 +
√
17)/4, substituting ˆxP P V= 1−v+cgives
exactlyP 3. Thus, onP 3, ΩP P V= [1−v+c, v−c] andp P P V i,∅ = 2v−c−1; otherwise the selected outcome is
that in part (A). □
Proof of Remark 2.All three regions satisfyv > 3 2 , sop N DC ∅ = 1 andr N DC= 1/2.
For (i),v≥2, 1≤c≤v−1, andp P P V i,∅ ≥1 +cimply 1−v+c≤0 and (1 +c−p P P V i,∅ )/2≤0, so the disclosure
boundaries are zero and Ω P P V= [0,1]. A realized uniform-price deviation cannot change disclosure and
hence cannot generate anonymous demand. Thus, each seller earnsr P P V= R 1/2 0 (1−2x)dx= 1/4< r N DC,
soG VDD <0 and the platform does not provide the service.
For (ii), let (v, c)∈ P3, wherec >1. Atp P P V 1,∅ =p P P V 2,∅ = 1, forx≤ 1 2 the gain from disclosure is 2x−c≤
1−c <0; the casex > 1 2 follows symmetrically. Hence, Ω P P V=∅. The uniform-price game then coincides
with NDC, sop P P V i,∅ = 1 andr P P V= 1/2. Thus,G VDD = 0, but the platform does not provide because the
opt-in set is empty.
For (iii), the stated restrictions imply 0<1−v+c <1/2. Letting ˆxP P V= 1−v+c, the interior-equilibrium
conditions established in Lemma EC.1.4 givep P P V i,∅ =v−ˆx P P V= 2v−c−1. The no-deviation condition is
ˆxP P V≥v−2 when ˆx P P V≤1/4, which follows fromc≥2v−3; when ˆx P P V>1/4, the stated parameter
bounds place ˆxP P Vbetween the roots of 17(ˆxP P V)2 −2(v+ 3)ˆxP P V+ (v−1) 2 ≤0. Hence, Ω P P V= [1−v+
c, v−c] is a rational-expectations equilibrium. Each seller earnsr P P V= 1/4 + (v−1)(1−v+c)<1/2, where
the inequality follows fromc < v−1 + 1/[4(v−1)]. Thus,GVDD <0 and the platform again does not provide.
Relative to the selected equilibrium, cases (i) and (iii) change provision only whenc= 1: the selected
equilibrium then has Ω P P V={1/2}andG VDD = 0, so provision changes but all payoffs remain unchanged.
Forc >1, both selections induce non-provision.
OnP 3, the selected equilibrium hasr P P V= 1/4 + (v−1)(1−v+c)≥1/2, so the platform provides and
earns Π V DD P =γ+ 2G VDD ≥γ. Under the alternative empty-disclosure equilibrium it does not provide and
earnsγ, so platform profit and seller sales revenues are weakly lower. Seller profits are unchanged because
the selected-equilibrium fee leaves each seller with (1−γ)r P P V−(1−γ)(r P P V−r N DC) = (1−γ)r N DC.
Moreover, the selected equilibrium givesCS P P V= (1−v+c) 2 + (v−c− 1 2 )2 <1/4, whereas non-provision
givesCS N DC=v− 5 4 >1/4; hence consumer surplus is strictly higher under the alternative equilibrium.
In the PP subgame, the equilibria in (i) and (iii) yield sales revenues 1/4 and 1/4 + (v−1)(1−v+c)<1/2,
respectively, while (ii) yields 1/2≤r P P Vunder the selected equilibrium. Since the preceding characterization
exhausts the symmetric pure-strategy rational-expectations equilibria and data-service fees are sunk in this
subgame, the equilibrium selected in Lemma EC.1.4 weakly maximizes both sellers’ continuation profits.
Finally, these alternative PP equilibria do not affect the exclusive access subgames, soT VDD = 0 holds.□
Proof of Lemma EC.1.5.By symmetry, we assume without loss of generality that seller 1 makes the
purchase. Letp e i,∅ denote the anticipated uniform price of selleri. If a consumer atxopts in, seller 1 observes
xand can extract any surplus above the consumer’s outside option from seller 2 or no purchase. Hence,

Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization15
under rational expectations, her utility from opting in isU in,e(x) = max{v−p e 2,∅ −(1−x),0} −c. If she opts
out, both sellers charge uniform prices, givingU out,e(x) = max{v−p e 1,∅ −x, v−pe 2,∅ −(1−x),0}. Therefore,
U out,e(x)≥U in,e(x) +c > Uin,e(x) for everyx, so no consumer discloses. Since entering, opting out, and not
purchasing yields zero utility, all consumers enter.□
Proof of Proposition EC.2.1.In the subsidy region, the platform’s net data value is ∆Π g P = 2Gg + (1 +
ηg)(1−γ)T g −2a−K. Thus, ∂∆Πg P ∂η g = (1−γ)T g. Sinceη g = 1−Φ κ(∆Lg) and ∆Lg =R g N −R g I +γT g +a+K,
∂η g
∂a = ∂η g ∂K =−ϕ κ(∆Lg) and ∂η g ∂γ =−T gϕκ(∆Lg). IfT g >0, higheraorKlowers credibility and data value,
while
∂∆Πg P
∂γ =−(1 +η g)T g −(1−γ)(T g)2ϕκ(∆Lg)<0. An upward shift in the distribution ofκraisesη g and
thus weakly increases data value. IfT g <0, ∂∆Πg P ∂a = (1−γ)|T g|ϕκ(∆Lg)−2, ∂∆Πg P ∂K = (1−γ)|T g|ϕκ(∆Lg)−1,
and
∂∆Πg P
∂γ = (1 +η g)|T g| −(1−γ)|T g|2ϕκ(∆Lg). Hence, these derivatives are nonnegative if and only if
ϕκ(∆Lg)≥ 2 (1−γ)|T g | ,ϕ κ(∆Lg)≥ 1 (1−γ)|T g | , andϕ κ(∆Lg)≤ 1+ηg (1−γ)|T g | , respectively. An upward shift inκ
raisesη g and therefore weakly decreases data value whenT g <0.□
Proof of Proposition EC.2.2.By definition,T g =R g N −R g U (bΩg, q) andRg N =R g U (∅,0). Since unilateral
information weakly disadvantages the uninformed seller,T g ≥0 holds. TheL-Lipschitz continuity assumption
further impliesT g =

Rg U (∅,0)− Rg U (bΩg, q)

 ≤L R Θ q(θ)1 bΩg (θ)dµ(θ) =Lβ g. Hence, 0≤T g ≤Lβ g. Therefore,
βg = 0 impliesT g = 0, establishing sufficiency. For necessity, supposeT g = 0 andR g U (bΩg, q)< Rg N whenever
βg >0. Thenβ g >0 would implyT g =R g N −R g U (bΩg, q)>0, a contradiction. Hence, under the additional
condition, threat elimination requiresβ g = 0.□
Proof of T able EC.3.2.Conditional on data provision,F MDC 1 =F MDC 2|AC = (1−γ)(r P P M−r P N M 2 ). Hence,
each seller earnsπ MDC i = (1−γ)r P P M−F MDC 1 = (1−γ)r P N M 2 , which equals 0 ifr P N M 2 = 0 and (1−γ)/8
ifr P N M 2 = 1/8. The platform earns Π MDC p = 2γrP P M+ 2F MDC 1 = 2rP P M−2(1−γ)r P N M 2 , which reduces
to 2r P P Mand 2r P P M−(1−γ)/4, respectively. If entry is partial,CS MDC = 2 R 1/2 1−(v−c)(v−1 +x−c)dx=
(2v−2c−1) 2/4; if all consumers enter,CS MDC = 2 R 1/2 0 (v−1 +x−c)dx=v−c− 3 4 . Since prices and
platform payments are transfers,SW MDC =CS MDC + 2rP P M. Substituting the correspondingr P P Mand
rP N M 2 gives the outcomes in all provision regions. Whenever the platform does not provide the data service,
the equilibrium coincides with NDC. This yields Table EC.3.2.□
Proof of T able EC.3.3.Conditional on provision,F VDD =F VDD 1 =F VDD 2|AC = (1−γ)(r P P V−r NDC).
Hence,π VDD i = (1−γ)r NDC, ΠVDD p = 2rP P V−2(1−γ)r NDC, andSW VDD =CS VDD + 2rP P V.
When 1 2 < v≤ 2 3 andc < v− 1 2 , or 2 3 < v≤1 and 3v 2 −1≤c < v− 1 2 ,r NDC =v 2/4. Substitution gives
πVDD i = (1−γ)v 2/4 and Π VDD p = [γv 2 + (2v−2c−1) 2]/2. Moreover,CS VDD = 2 R v/2 0 (v−v/2−x)dx+
2
R 1/2
1−(v−c)(v−1 +x−c)dx= [v 2 + (2v−2c−1) 2]/4, soSW VDD = 3[v2 + (2v−2c−1) 2]/4.
When 2 3 < v≤1 andc < 3v 2 −1,p P P V i,∅ = 2v−c−1,r NDC =v 2/4, and the market is fully covered.
Hence,π VDD i = (1−γ)v 2/4 and Π VDD p = [−(5−γ)v 2 + 4vc+ 8v−4c−3]/2. Consumer surplus isCS VDD =
2
R 1−(v−c)
0 [v−(2v−c−1)−x]dx+ 2
R 1/2
1−(v−c)(v−1 +x−c)dx= [4(1−v+c) 2 + (2v−2c−1) 2]/4, and therefore
SW VDD = (4v−1−8vc+ 8c 2 + 4c)/4.
For (v, c)∈ P3,r NDC = 1/2 andr P P V= [−4v2 + 4vc+ 8v−4c−3]/4. Thus,π VDD i = (1−γ)/2 and Π VDD p =
[−4v2 + 4vc+ 8v−4c−(5−2γ)]/2. Since the uniform price, disclosure allocation, and full coverage coincide
with the preceding case,CS VDD andSW VDD are given by the same expressions.
Whenever the platform does not provide the data service, the equilibrium coincides with NDC. Substituting
these outcomes gives Table EC.3.3.□
Proof of Lemma EC.3.1.Letp e i,∅ denote selleri’s anticipated uniform price. All consumers enter because
they can remain anonymous and decline to purchase. Forx≤1/2, successful identification gives gross utility

16Liu, Lu, and W ang:The Source of Data Value: Consumer Disclosure, Access Design, and Platform Monetization
uI (x) = [v−1 +x] +, whereas anonymity givesu A(x) = [v−p e −x] + under symmetric anticipated uniform
prices. Since opting in yieldsq[u I (x)−c] + (1−q)u A(x) and opting out yieldsu A(x), disclosure is optimal
if and only ifu I (x)−c≥u A(x) forq >0. This requiresx≥1−v+candx≥(1 +c−p e)/2. The right
half-market is symmetric. Conditional on identification, the privacy cost is sunk and both sellers observex,
giving the personalized prices in part (A).
Fix the symmetric anticipated disclosure set, but allow actual uniform prices to differ. If sellericharges
zagainst the rival’s pricep j, its potential anonymous demand has massy(z, p j). Opt-out consumers remain
anonymous with probability one, whereas opt-in consumers remain anonymous with probability 1−q. Thus,
anonymous demand is (1−q)y(z, pj)+qA(y(z, pj);d). Personalized revenue is unaffected by this uniform-price
deviation because the anticipated disclosure set remains fixed. Each seller therefore maximizesH(z;p j, d, q)
holdingp j anddfixed. Imposingp 1 =p 2 =pand rational-expectations consistency gives the necessary and
sufficient condition in part (B).
For completeness, this global maximization requires only finitely many evaluations. Pricesz≥vgenerate
zero anonymous revenue. On [0, v], form the breakpoint setZ 0 = ({0, v,2v−1−p} ∪ {v−t,1 +p−2t:t∈
{0, d,1−d,1}})∩[0, v]. Between consecutive breakpoints, anonymous demand is affine, sayα−βzwithβ≥0,
and revenue isz(α−βz). Its maximum occurs at an endpoint or atz=α/(2β) whenβ >0 and this point lies
inside the interval. Comparing these values establishes global optimality without assuming global concavity.
Now suppose 1 2 < v <1 and 0< c < v−1 2 . Every symmetric equilibrium hasv/2≤p < v. Indeed, a price
belowv/2 admits a profitable small increase. On the participation-constrained branch, the right derivative
is eitherv−2por (1−q)(v−2p) +qd, both positive. On the competition-constrained branch, it is either
(1−p)/2 or (1−q)(1−p)/2 +qd, also positive. A price at leastvgenerates zero anonymous revenue and is
dominated by a positive price belowv, sinced≥a >0. Consequently, anonymous demand at symmetry is
participation-constrained, andp≥v/2> censures 0< d <1/2.
For fixedd, define ¯H(z;d) =z{(v−z) + −q[(v−z) + −d] +}. Near a symmetric candidate, this equals
the actual anonymous revenue. Forq <1, its derivatives on the branchesz < v−dandz > v−dare
(1−q)(v−2z) +qdandv−2z, respectively. The derivatives immediately below and above the kink are
(2−q)d−(1−q)vand 2d−v. Hence, a symmetric candidate must satisfyp=v/2 +qd/[2(1−q)] whend < b q,
p=v−dwhenb q ≤d < v/2, andp=v/2 whend≥v/2. Atq= 1, the first branch is absent. Combining these
conditions withd= max{a,(1 +c−p)/2}gives exactly the three cases in part (C).
It remains to verify global deviations. Ifd≥v/2, the candidatep=v/2 earns anonymous revenuev 2/4,
whileH(z;p, d, q)≤z(v−z) + ≤v 2/4 for everyz≥0. Suppose instead thatd < v/2. The candidate satisfies
p+d≤v <1 and globally maximizes ¯H, whose derivative decreases on each branch and drops at the kink.
For any deviation withy(z, p)≤1−d, monotonicity oft−q[t−d] + givesH(z;p, d, q)≤ ¯H(z;d)≤ ¯H(p;d) =
H(p;p, d, q). For a deviation reaching the opposite anonymous tail,y(z, p)>1−drequires 0≤z < t:=
p+ 2d−1< d. Sincet <1/2<(1 +p)/2, we haveH(z;p, d, q)≤z(1 +p−z)/2≤t(1−d)< pd≤H(p;p, d, q).
The strict inequality follows frompd−t(1−d) = (1−2d)(1−p−d)>0. Thus, no deviation is profitable.
The preceding local conditions exhaust symmetric candidates, establishing existence and uniqueness of the
common uniform price and disclosure set in part (C).□
