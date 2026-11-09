---
title: 'The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed
  Tokens'
url: https://arxiv.org/abs/2606.26704
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- JJ Jia Jing Tan
- Eva Meng
- Josh Ng
- Zack Zhang
- September Liu
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.26704
pages: 12
chars: 40228
fetched_at: '2026-11-08T13:07:41+00:00'
kb_version: 1
---

# The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in Asset-Backed Tokens

THEFUNGIBLERESERVESTANDARD: A DETERMINISTIC
FRAMEWORK FORENCODINGCARRYINGCOSTS IN
ASSET-BACKEDTOKENS
A PREPRINT
JJ Jia Jing Tan, Eva Meng, Josh Ng, Zack Zhang,
September Liu, Teelet Wang, Ludwig Zhang, Seth Yan
Matrixdock
{jj.tan, eva.meng, josh.ng, zack.zhang,
september.liu, teelet.wang, ludwig.zhang, seth.yan}@bit.com
March 2026
ABSTRACT
The tokenization of real-world assets (RW As) has emerged as a transformative application of
blockchain technology, with market projections estimating trillions of dollars in tokenized assets
within the coming decade. However, a fundamental challenge remains unaddressed: physical as-
sets such as precious metals, stored commodities, and warehoused goods incur structural negative
carry—custody, insurance, and audit costs that accumulate over time. While existing tokeniza-
tion models have successfully established the market for digital gold and treasuries, they typically
manage operational costs at the issuer level. The FRS introduces a framework to bring these eco-
nomics directly on-chain, avoiding mechanisms such as token rebasing that compromise fungibility
and composability with decentralized finance (DeFi) protocols. This paper proposes the Fungible
Reserve Standard (FRS), a deterministic token design framework that encodes carrying costs trans-
parently into on-chain logic. The FRS introduces an asset-per-token variableq(t)that decreases
according to a predefined annualized carrying cost rate, coupled with a supply reconciliation mech-
anism that preserves holder balances and ERC-20 composability. While mathematically inspired
by the daily expense ratio accrual in traditional asset management—which often embed centralized
profit margins—the FRS design specifically encodes actual operational carrying costs to provide
pure institutional-grade accounting clarity without compromising DeFi compatibility. The frame-
work is asset-agnostic and applicable to any real-world asset with positive, predictable holding costs.
KeywordsReal-World Assets (RW A)·tokenization·Decentralized Finance (DeFi)·carrying costs·smart contracts·
blockchain economics·asset-backed tokens
1 Introduction
The tokenization of real-world assets represents one of the most consequential applications of distributed ledger tech-
nology, aiming to embed traditionally off-chain financial instruments within programmable blockchain infrastruc-
ture [1,2]. Industry projections reflect the scale of this opportunity: Boston Consulting Group estimated the tokenized
asset market at $16.1 trillion by 2030 [3], while McKinsey & Company projected a tokenized market capitalization
of approximately $2 trillion by 2030 (with an optimistic scenario reaching $4 trillion), excluding cryptocurrencies
and stablecoins [4]. Major institutional participants have entered this space, including the launch of tokenized money
market funds backed by U.S. Treasury securities on public blockchains [5].
While significant progress has been made in tokenizing financial instruments with positive carry characteristics—such
as yield-bearing tokens backed by government securities—the tokenization ofphysicalassets withnegative carry
presents a distinct and largely unaddressed challenge. Precious metals, stored commodities, warehouse receipts, and
arXiv:2606.26704v1  [cs.CR]  25 Jun 2026

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
other tangible goods require custody, insurance, audits, and operational oversight. These costs create structural nega-
tive carry: a persistent economic characteristic intrinsic to the physical asset itself.
In traditional finance, negative carry is embedded transparently into product structures. Exchange-traded commodity
vehicles reflect expense ratios through net asset value (NA V) adjustments [6], and custodial costs are deducted daily
from fund assets. This mechanism is well-understood by institutional participants and provides accounting clarity.
By contrast, existing real-world asset tokenization models often diverge from this discipline. Some rely on issuer sub-
sidies to offset custody costs, creating opacity regarding long-term sustainability. Others introduce yield overlays or
hybrid underlying asset compositions that transform the token into astructured productrather than a direct represen-
tation of the underlying asset. Still others employ mechanisms such as balance rebasing or wrapper tokens that, while
reflecting costs, compromise the token’s fungibility and compatibility with decentralized finance (DeFi) protocols.
This paper makes the following contributions:
1. We formalize theprinciple of economic purityfor tokenized physical assets, articulating a set of design
requirements that ensure the token faithfully represents the economic characteristics of its underlying asset,
including negative carry.
2. We propose theFungible Reserve Standard (FRS), a deterministic token design framework that encodes
carrying costs through a monotonically decreasing asset-per-token variableq(t), coupled with a supply rec-
onciliation mechanism that preserves ERC-20 fungibility.
3. We demonstrate how the FRS mechanism isinspired by the transparency of institutional accounting, ex-
plicitly contrasting the FRS’s focus on pure verifiable physical carrying costs against the centralized, margin-
based fee models of traditional asset management.
4. We provide acomparative analysisshowing that the FRS preserves DeFi composability where alternative
approaches (rebasing, wrapper tokens, issuer subsidization) do not.
The remainder of this paper is organized as follows. Section 2 surveys related work in traditional finance carrying-
cost mechanisms, token economics, and the RW A tokenization landscape. Section 3 formalizes the economic purity
principle. Section 4 presents the Fungible Reserve Standard. Section 5 provides comparative analysis. Section 6
discusses institutional and DeFi compatibility. Section 7 examines broad applicability across asset classes. Section 8
addresses limitations and future directions. Section 9 concludes.
2 Background and Related Work
2.1 Traditional Finance: Carrying Cost Mechanisms
2.1.1 ETF Expense Ratios vs. Pure Carrying Costs
Exchange-traded funds (ETFs) are open-end investment funds traded on stock exchanges. The ETF structure involves
a distinctive creation/redemption mechanism mediated by Authorized Participants (APs), which maintains alignment
between the fund’s market price and its net asset value (NA V) [6, 7].
Theexpense ratiois the annual fee charged by an ETF to cover operational costs and the fund provider’s profit margin,
expressed as a percentage of the fund’s total assets. Critically, this feeaccrues dailyand isdeducted from the fund’s
assetswhen daily NA V is calculated, reducing net returns over time without altering the number of shares held by
investors [8]. For physically-backed gold ETFs, this mechanism operates as follows: the trust gradually sells small
quantities of gold to cover expenses, causing the gold backing per share to decline monotonically. The holder’s share
count remains unchanged; only the asset content per share diminishes.
This mathematical decay structure provides a baseline, but the economic driver differs fundamentally. While tradi-
tional ETF expense ratios blend actual custody costs with centralized management fees and profit margins, the FRS
strictly isolates and encodes the pure, structuralcarrying costs(e.g., vaulting, insurance) of the physical asset. For
illustration, an asset-backed ETF with annual expense ratiorand initial asset-per-sharea 0 sees its physical backing
per share aftertdays decrease as:
a(t) =a 0 ·

1− r 365 t (1)
2

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
2.1.2 Commodity Carrying Costs
Physical commodities incur carrying costs including storage, insurance, and financing. In futures markets, these costs
are reflected in the term structure: when futures prices exceed spot prices (contango), the premium approximates
the cost of carry [9, 10]. Futures-based commodity ETFs incur additional “roll yield” costs when replacing expiring
contracts, which can produce significant negative carry [10].
2.1.3 REITs and Pass-Through Economics
Real Estate Investment Trusts (REITs) demonstrate an alternative mechanism for encoding asset economics into finan-
cial instruments. REITs are required to distribute at least 90% of taxable income to shareholders, effectively passing
through operating costs and income [11]. This regulatory structure ensures that the financial instrument reflects the
underlying asset’s economics rather than absorbing or masking them.
2.2 Token Economics and Mechanism Design
2.2.1 Bitcoin’s Deterministic Supply Schedule
Bitcoin introduced the concept of algorithmically enforced monetary policy [12]. Its fixed supply cap of 21 million
coins and predetermined halving schedule (block reward halves every 210,000 blocks) established the precedent that
economic parameters can be encoded deterministically in protocol logic, providing transparency and predictability that
contrasts with discretionary monetary policy. Carlsten et al. [13] analyzed the long-term implications of this design on
mining incentives as block rewards diminish.
2.2.2 Ethereum’s EIP-1559 Fee Mechanism
Ethereum’s EIP-1559 upgrade [14] reformed the network’s fee market by introducing an algorithmically determined
base fee that adjusts with network demand and is burned (destroyed), removing it from circulation. This demonstrated
that on-chain economic mechanisms can be governed algorithmically, providing formal guarantees on user experience
and economic properties. Liu et al. [15] empirically validated the mechanism’s effects on fee predictability and
consensus security.
2.2.3 Token Valuation and Design
Cong et al. [16] developed a formal framework for understanding token valuation dynamics, analyzing the interplay
between token utility, platform growth, and speculative demand. Their work demonstrates the importance of carefully
designed tokenomics in determining the economic sustainability of token-based systems. The nascent field of token
mechanism design draws from auction theory, monetary economics, and computer science to create systems with
desirable equilibrium properties.
2.3 RW A Tokenization Landscape
2.3.1 Tokenized Physical Assets
The most prominent tokenized physical assets are gold-backed tokens. Leading products provide robust 1:1 backing,
representing one troy ounce of physical gold stored in allocated vaults with regular third-party attestation reports
verifying reserve backing [17]. The FRS complements these existing standards by providing an alternative for users
requiring deterministic, on-chain cost visibility.
2.3.2 Tokenized Financial Instruments
Tokenized yield-bearing instruments—such as on-chain representations of U.S. Treasury securities—represent the
fastest-growing segment of RW A tokenization [4]. These products pass through the yield generated by the underlying
assets and have attracted billions of dollars in assets under management. They representpositive carryassets where
the underlying generates returns, in contrast to thenegative carryphysical assets that are the focus of this paper.
2.3.3 RW A-Specific Blockchain Infrastructure
A new generation of purpose-built blockchain infrastructure has emerged to address RW A-specific requirements.
Layer-2 solutions such as Plume Network provide integrated compliance (KYC/AML), identity management, and
DeFi infrastructure purpose-built for tokenized assets [18]. Specialized Layer-1 blockchains such as Polymesh embed
3

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
identity, compliance, and governance as native protocol features for regulated securities [19]. Decentralized networks
like Canton Network offer privacy and interoperability for institutional assets, enabling a ”network of networks”
approach to tokenization [20]. DeFi protocols such as Centrifuge enable the tokenization of illiquid assets as col-
lateral within decentralized lending markets [21]. Financial-services-oriented chains such as Provenance Blockchain
embed compliance metadata directly into token structures using the Cosmos SDK [22]. These platforms address
infrastructure-level challenges but do not define how theeconomic characteristicsof the underlying asset should be
reflected in token design—the problem this paper addresses.
2.3.4 Token Standards
The ERC-20 standard [23] provides a widely-adopted interface for fungible tokens on Ethereum but lacks built-in
compliance features. ERC-1400 [24] extends ERC-20 with partitioned balances and programmable transfer validation
for security tokens. ERC-3643 (T-REX) [25] adds decentralized identity and modular compliance for permissioned
tokens. The FRS builds upon ERC-20 to maximize composability and interoperability while encoding asset economics
within the standard interface.
2.4 DeFi Properties for Physical Asset Tokens
Decentralized finance (DeFi) offers several properties that are uniquely valuable for tokenized physical assets [26]:
•Transparency: All state variables, including reserve ratios and fee parameters, are publicly queryable on-
chain at any time—in contrast to periodic disclosures in traditional finance.
•Composability: Tokens adhering to standard interfaces (ERC-20) can be integrated into decentralized ex-
changes, lending protocols, and structured products without bespoke integrations.
•Continuous Operation: Unlike traditional exchanges with fixed trading hours, blockchain-based tokens are
tradable 24/7 across geographies.
•Traceability and Auditability: All minting, burning, and transfer events are recorded on an immutable
ledger, providing a comprehensive audit trail.
•Non-Custodial Access: Users maintain direct control over their tokens without reliance on intermediary
custodians for trading and transfer.
These properties have been systematized by Werner et al. [26] and Catalini and Gans [1], who identify reduced verifi-
cation costs and enhanced network effects as fundamental advantages of blockchain-based financial systems.
3 Design Philosophy: The Principle of Economic Purity
We formalize the design philosophy underlying the Fungible Reserve Standard through the following principle:
A tokenized representation of a real-world asset should accurately reflect the fundamental economic
properties of the underlying asset, including its structural carrying costs, without distortion, subsi-
dization, or obfuscation.
This principle, which we termeconomic purity, yields four formal design requirements:
R1 (Reserve Integrity):The underlying physical reserve must remain verifiable in its most fundamental form. The
asset held in custody must be the asset the token claims to represent, without blending or substitution.
R2 (Deterministic Accounting Identity):The relationship between token supply and physical reserve must be de-
terministic and continuously computable:
S(t)·q(t) =R(t)(2)
whereS(t)is the total token supply,q(t)is the asset quantity per token, andR(t)is the total physical reserve
at timet.
R3 (Economic Isolation):The token must not blend with off-chain downstream strategies—such as yield overlays,
lending programs, or structured products—to offset negative carry. The token’s economics must represent
theasset, not astrategybuilt around the asset.
4

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
R4 (On-Chain Cost Encoding):Carrying costs must be encoded on-chain with rule-based, transparent logic, en-
abling institutional-grade accounting clarity. Carrying cost parameters must be publicly visible and their
application algorithmically deterministic, stripping away arbitrary or centralized issuer fees.
These requirements distinguish the FRS from existing approaches. Issuer-subsidized models violateR3andR4by
absorbing costs off-chain and concealing the asset’s true economics. Rebasing tokens satisfyR4but violate fungibility
assumptions expected by DeFi protocols. Wrapper token approaches violateR3by introducing additional layers that
obscure the direct asset relationship.
4 The Fungible Reserve Standard
Table 1 summarizes the notation used throughout this section.
Table 1: Notation
Symbol Description
q(t)Quantity of physical asset per token at timet
S(t)Total token supply at timet
R(t)Total physical reserve in custody at timet
cAnnualized carrying cost rate
t0 Inception time
∆tCost application interval (e.g., 1 day)
4.1 Token Design
The Fungible Reserve Standard defines a token whose value representation is governed by the accounting identity:
q(t) = R(t) S(t) (3)
At inceptiont 0, the standard setsq(t 0) = 1, meaning each token corresponds to one unit of the underlying asset.
Consequently:
S(t0) =R(t 0)(4)
The value ofq(t)decreases monotonically over time to reflect the carrying costs of the underlying physical asset. This
design ensures that the token’s economic representation evolves consistently with the real-world cost of maintaining
the reserve.
4.2 Deterministic Carry Encoding
Rather than deducting tokens from holders, rebasing token balances, or reducing physical reserves, the FRS adjusts
the asset-per-token variableq(t)according to a predefined annualized carrying cost ratec. To optimize for smart
contract execution environments where exponential compounding is computationally expensive, the FRS employs a
linear deductionmodel. For an epoch starting att k with ratec k, the value afternintervals∆t(e.g., days) is:
q(tk +n∆t) =q(t k)·

1−c k · n N  (5)
whereNis the number of intervals per year (e.g.,N= 365for daily application).
This linear formulation provides a predictable reduction in asset representation with the following properties:
• The annual carrying cost ratecis definedex anteand publicly visible on-chain.
• The linear computation minimizes gas costs and execution complexity.
• The value ofq(t)can be deterministically calculated for any future timestamp within the same rate epoch.
5

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
4.2.1 Handling Cost Rate Changes
When the carrying cost rate must be updated (e.g., fromc k toc k+1), a strict state checkpointing mechanism is re-
quired. The protocol must comprehensively reconcile the state up to the boundary of the change—typically 12:00
AM (00:00:00 UTC) of the day immediately preceding the effective date of the new rate. At this checkpointt k+1, all
outstanding carry is applied usingc k to lock in the finalq(t k+1). Only after this reconciliation is the new mathematical
epoch initiated, such that all subsequent days strictly usec k+1 applied linearly against the newly locked baseq(t k+1).
Proposition 1.The mathematical structure of the linear FRS carry encoding (5) serves as a rigorous first-order
approximation to the daily compound accrual calculation in physically-backed commodity ETFs (1), bounded tightly
for smallc.
Proof.The cumulative daily decay of a traditional ETF isg(n) =g 0 ·(1− rETF 365 )n. Settingq(t 0) =g 0 = 1and cFRS =r ETF, the binomial expansion of the ETF decay yields:

1− cFRS
365
n
= 1−n
 cFRS
365

+ n(n−1) 2!  cFRS 365 2 − n(n−1)(n−2) 3!  cFRS 365 3 +. . .
The FRS linear model computes exactly the first two terms:
q(t0 +n) = 1−c FRS
n
365
Since typical real-world carrying costs are small (c≤0.02), the higher-order terms are mathematically negligible. The
linear formula perfectly optimizes on-chain gas execution while mirroring the pure economic depreciation of physical
custody over an annual horizon.
This structural alignment allows the FRS to implement a familiar accounting mechanism on-chain, while shifting from
centralized compounding to gas-optimized linear tracking of physical carrying costs.
4.3 Supply Reconciliation Mechanism
After each adjustment ofq(t), the token supply must be reconciled to preserve the accounting identity (2). SinceR(t)
remains constant during a cost application (no physical reserves are added or removed), andq(t)has decreased, the
supply must increase:
S(t+ ∆t) = R(t) q(t+ ∆t) =S(t)· q(t) q(t+ ∆t) (6)
The additional tokens minted are:
∆S=S(t+ ∆t)−S(t) =S(t)·
 q(t)
q(t+ ∆t) −1

(7)
Substituting the expected linear deductionδq=q(t+n∆t)−q(t), the required supply expansion is easily com-
puted on-chain. These newly minted tokens are assigned to a designatedCarryCollectoraddress. This mechanism
achieves:
1. Physical reserves remain unchanged during reconciliation.
2. All existing holder token balances remainnumerically intact, preserving fungibility and DeFi compatibility.
3. The dilution of asset-per-token value occurs proportionally across all holders.
4. Cost collection is fully transparent, verifiable, and recorded on-chain.
The explicit separation of physical custody costs via theCarryCollectorisolates pure asset carrying costs from
external operational margins, unlike bundled ETF fees.
6

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
4.4 Precision and Rounding Error Management
Because the EVM natively supports integer mathematics rather than floating-point numbers, calculating fractional
linear deductions over time inevitably introduces the risk of truncation and rounding errors. If unmanaged, these
rounding artifacts can accumulate across daily checkpoints, eventually diverging the on-chain representationR(t) =
S(t)·q(t)from the exact off-chain physical reality.
To counteract this, the FRS introduces extensive scalar precision. In optimal implementations, the underlying compu-
tations and token fractional mechanics operate using9 decimal places of precision(10 9 scaling).
•Minimized truncation gap: Operating at 9 decimal places ensures that daily fraction splits forc· n 365 retain extreme accuracy, pushing rounding truncation down to nominal fractions of a billionth of an asset unit.
•Reconciliation integrity: When performing supply reconciliation (minting∆Sto theCarryCollector),
high decimal resolution guarantees that the aggregate balances of standard token holders mathematically sum
to the exact non-diluted reserve ratio without leaving unassigned ”dust” behind.
•On-chain efficiency: While 18 decimals is standard for general ERC-20 tokens, 9 decimals offers a special-
ized equilibrium for physically vaulted assets (such as metric grams of gold or troy ounces), fully enclosing
the physically measurable reality of the asset while preserving computational bounds within EVM word sizes.
4.5 Reserves Addition and Reduction
When physical reserves are added or removed—corresponding to minting or burning of tokens—the prevailingq(t)
value determines the exact token quantity:
For reserve additions of quantity∆R +:
∆Smint = ∆R+ q(t) (8)
For reserve reductions of quantity∆R −:
∆Sburn = ∆R− q(t) (9)
The continuously evolvingq(t)ensures precise representation of any addition or removal at any point in time. After
the operation, the accounting identity (2) is maintained:
(S(t)±∆S)·q(t) =R(t)±∆R(10)
This mechanism preserves the integrity of the asset-token relationship while ensuring that all changes in the underlying
reserves are accurately reflected on-chain.
5 Analysis and Comparison
5.1 Comparison with Alternative Approaches
Table 2 provides a systematic comparison of the FRS with alternative approaches to encoding carrying costs in asset-
backed tokens.
5.1.1 Issuer-Subsidized Models
In issuer-subsidized models, the token issuer absorbs custody and storage costs, either from operational budgets or by
retaining yield generated from other activities. While this simplifies the user experience:
• The token’s price does not reflect the true cost of maintaining the underlying asset, violatingR3(Economic
Isolation) andR4(On-Chain Cost Encoding).
• Long-term sustainability depends on the issuer’s financial health and willingness to continue subsidization.
• Institutional participants cannot derive accurate cost bases from on-chain data alone.
7

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
Table 2: Comparison of Carrying Cost Mechanisms for Asset-Backed Tokens
Property FRS Issuer Subsidized Rebasing Wrapper Tokens
On-chain cost transparency✓×✓×
Holder balance stability✓ ✓×✓
ERC-20 DeFi composability✓ ✓×Partial
Economic fidelity to underlying✓×Partial×
Institutional accounting clarity✓Partial× ×
Deterministic cost schedule✓×✓Varies
Long-term sustainability✓×✓ ✓
Reserve integrity✓ ✓ ✓Partial
5.1.2 Rebasing Mechanisms
Rebasing tokens adjust all holder balances proportionally at regular intervals to reflect value changes. While this does
encode costs on-chain:
• Fluctuating balances break assumptions made by DeFi protocols. A lending protocol, for example, may
record a deposit of 100 tokens; if the balance subsequently decreases to 99.97 through rebasing, accounting
discrepancies arise.
• Portfolio tracking and tax accounting become significantly more complex.
• Integration with automated market makers (AMMs) and order book protocols requires custom handling [26].
5.1.3 Wrapper Token Approaches
Wrapper tokens encapsulate the underlying asset token within a secondary contract that introduces fee logic. This
approach:
• Introduces an additional layer of smart contract risk.
• Requires wrapping/unwrapping operations that add friction.
• Obscures the direct relationship between the token and the underlying asset, violatingR3.
• May fragment liquidity between wrapped and unwrapped versions.
5.2 Structural Analogs to TradFi Vehicles
The FRS mechanism provides a transparent on-chain analog to traditional finance expense structures, while removing
centralized fee extraction. Table 3 illustrates the structural mapping.
Table 3: Comparative Accounting Logic: Traditional vs. On-chain Models
Traditional Asset Management Logic FRS Mechanism
Asset per sharea(t)Asset per tokenq(t)
Expense ratior(includes profit margin) Annual carrying cost ratec(pure custody cost)
Daily NA V accrual Dailyq(t)update
Fund sells asset for feesreconcileSupplymints tokens for carry
Shares outstanding unchanged Holder balances unchanged
Published NA V On-chainq(t)query
Periodic audit On-chain verification + reserve audit
The key enhancement over the ETF model is the transition fromperiodic disclosure of centralized feestocontinuous
on-chain transparency of physical carrying costs. In a traditional ETF, NA V is published once daily, and detailed
audit reports are periodic. In the FRS,q(t),S(t), and the cost ratecare queryable at any time by any party, offering
real-time economic transparency.
8

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
6 Institutional and DeFi Compatibility
6.1 Accounting Clarity and Transparency
Institutional adoption of tokenized real-world assets requires accounting symmetry, transparency, and deterministic
behavior. The FRS aligns with established financial product structures:
•Mathematical inspiration from expense ratios: As demonstrated in Section 5, the FRS mechanism uses
mathematical structures familiar to institutional participants from daily expense ratio accruals, but cleanly
unbundles pure carrying costs from management fees.
•Continuous asset-backed value computation: The reserve identityR(t) =S(t)·q(t)can be computed
on-chain at any time, enabling independent auditors to verify that:
1. Reserves in custody reports match attested amounts on-chain.
2. On-chain token supplyS(t)is publicly viewable.
3. The asset-per-token variableq(t)follows deterministic logic with publicly visible parameters.
•Real-time auditability: The mechanism provides continuous, mathematically verifiable evidence of custody
costs on-chain, eliminating the opacity of centralized fee models.
6.2 DeFi Compatibility
A central design objective of the FRS is preserving full token composability with decentralized finance infrastructure.
Since holder token balances do not fluctuate numerically—unlike rebasing tokens—the FRS token is fully compatible
with:
•Decentralized exchanges (DEXs): AMM liquidity pools and order book protocols can integrate the token
using standard ERC-20 interfaces.
•Lending protocols: Deposit and collateral accounting remains consistent; no reconciliation logic is required
for balance changes.
•Price Oracles: On-chain price oracles can easily digest the asset-per-token variableq(t)into their reported
net price, enabling accurate valuation for DeFi integrations.
•Structured DeFi vaults: Yield strategies and composable primitives can incorporate the token without cus-
tom adapters.
•Cross-chain bridges: Standard bridge contracts designed for ERC-20 tokens require no modification.
The FRS thus occupies a unique position: it provides institutional-grade accounting clarity—typically associated with
centralized, regulated financial products—while maintaining full composability with permissionless DeFi infrastruc-
ture.
7 Applicability Across Asset Classes
The Fungible Reserve Standard is broadly applicable to real-world assets characterized bypositive, predictable holding
costs—where custody, storage, compliance, or preservation expenses accumulate over time and can be encoded as
deterministic value adjustments.
7.1 Directly Applicable Asset Classes
•Vaulted precious metals: Gold, silver, platinum, and palladium held in allocated custody incur well-defined
storage and insurance costs.
•Warehoused commodities: Industrial metals, agricultural products, and raw materials stored in regulated
warehouses have measurable custody costs.
•Carbon instruments: Regulated environmental assets (carbon credits, emissions allowances) incur registry,
verification, and audit costs that follow externally defined schedules.
•Fine art and collectibles: Insured, climate-controlled storage with periodic appraisal involves quantifiable
recurring costs.
9

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
7.2 Framework Properties
In general, any asset for which holding costs satisfy the following conditions is a candidate for FRS encoding:
1. Costs arestructurally positive(the asset incurs costs, not yields, from holding).
2. Costs aretime-dependent(they accrue predictably over time).
3. Costs areoperationally verifiable(they can be attested by independent parties).
The annualized carrying cost rateccan be set to reflect the specific cost structure of each asset class, making the FRS
anasset-agnosticmechanism parameterized by a single, transparent variable.
7.3 Integration with RW A Infrastructure
The FRS is designed to be deployable on any smart contract platform, including general-purpose chains (Ethereum,
Sui, etc.) and RW A-specific infrastructure (Plume, etc.). On RW A-focused chains, the FRS mechanism can integrate
with native compliance and identity layers while maintaining its economic logic independently. The separation of
economic design(FRS) frominfrastructure design(compliance, identity, governance) reflects a modular architecture
principle that allows each layer to evolve independently.
8 Discussion
8.1 Limitations
The FRS addresses the specific problem of encodingnegative carrying costsfor physical assets and does not address
several related challenges in RW A tokenization:
•Oracle design: The FRS assumes that reserve attestation is performed through external audits. The design
of trust-minimized reserve oracles remains an open research problem.
•Credit and counterparty risk: The standard does not address risks arising from custodian default or fraud.
•Dynamic cost rates: The current formulation assumes a fixed annualized carrying cost ratecthat can only
be adjusted on a discrete interval. Assets with variable or unpredictable cost structures may require more
flexible on-chain updates.
•Regulatory compliance: The FRS addresses economic design but does not incorporate jurisdiction-specific
compliance logic such as KYC/AML. Integration with standards like ERC-3643 [25] may be necessary for
regulated deployments.
8.2 Future Directions
Several extensions merit further investigation:
•Dynamic cost rates: Allowingcto be updated through governance mechanisms while maintaining trans-
parency guarantees and providing advance notice of changes.
•Continuous Carrying Costs: Investigating mathematical models for costs that need to be charged on a
continuous interval rather than discrete daily epochs.
•Multi-asset reserves: Extending the framework to tokens backed by baskets of physical assets with hetero-
geneous carrying costs.
•Formal verification: Applying formal methods to prove correctness properties of the smart contract imple-
mentation, including the invariant preservation of the accounting identity (2).
•Cross-chain deployment: Examining how the FRS accounting identity can be maintained consistently across
multiple blockchains via bridge protocols.
•Empirical analysis: Conducting simulations or deploying pilots to study the FRS’s behavior under varying
market conditions, carrying cost rates, and DeFi integration scenarios.
10

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
8.3 Broader Implications
The FRS contributes to a broader objective in the maturation of tokenized assets: the transition frommere on-chain
representationtoeconomically accurate representation. By establishing the principle of economic purity and pro-
viding a concrete mechanism for its implementation, the FRS offers a template for how other asset-specific economic
characteristics might be encoded into token design. By providing a deterministic on-chain mechanism for value adjust-
ment, the FRS offers a transparent framework that aligns with the reporting requirements of institutional participants,
regardless of the underlying jurisdiction.
9 Conclusion
The maturation of real-world asset tokenization requires a transition from simple on-chain representation to econom-
ically accurate representation that faithfully encodes the fundamental properties of the underlying asset. This paper
introduced the Fungible Reserve Standard (FRS), a deterministic, transparent, and institutionally aligned framework
for encoding carrying costs directly into token design.
The FRS addresses a gap in the existing literature and practice: while significant work has been done on token stan-
dards, DeFi composability, and RW A infrastructure, no prior framework has formally addressed how the structural
negative carry of physical assets should be encoded in fungible token design. Existing approaches—issuer subsidiza-
tion, balance rebasing, and wrapper tokens—each compromise on transparency, composability, or economic fidelity.
The FRS resolves these tradeoffs through a mechanism that is:
•Deterministic: Carrying costs follow a predefined, algorithmically enforced schedule.
•Transparent: All parameters (q(t),r,S(t)) are on-chain and publicly queryable.
•Composable: Holder balances remain numerically stable, preserving full ERC-20 compatibility with DeFi
infrastructure.
•Institutionally familiar: The mechanism is mathematically aligned with traditional cost-accrual logic used
in commodity management, ensuring that the token’s economic representation evolves consistently with the
real-world cost of maintaining the reserve.
•Asset-agnostic: Applicable to any real-world asset with positive, predictable holding costs.
The future of real-world asset tokenization depends not only on representing assets on-chain, but on ensuring that
the economic truthfulness of those assets is embedded in protocol logic. By prioritizing native DeFi composability
alongside accurate cost accounting, the Fungible Reserve Standard provides a robust foundation for this objective.
References
[1] C. Catalini and J. S. Gans, “Some simple economics of the blockchain,”Communications of the ACM, vol. 63,
no. 7, pp. 80–90, 2020.
[2] T. Lambert, D. Liebau, and P. Roosenboom, “Security token offerings,”Small Business Economics, vol. 59,
no. 1, pp. 299–325, 2022.
[3] Boston Consulting Group and ADDX, “Relevance of on-chain asset tokenization in ‘crypto winter’,”
2022. [Online]. Available:https://web-assets.bcg.com/1e/a2/5b5f2b7e42dfad2cb3113a291222/
on-chain-asset-tokenization.pdf
[4] McKinsey & Company, “From ripples to waves: The transformational power of tokenizing assets,” Jun. 2024.
[Online]. Available:https://www.mckinsey.com/industries/financial-services/our-insights/
from-ripples-to-waves-the-transformational-power-of-tokenizing-assets
[5] Boston Consulting Group and Ripple, “Approaching the tokenization tipping point,” 2025.
[6] M. Lettau and A. Madhavan, “Exchange-traded funds 101 for economists,”Journal of Economic Perspectives,
vol. 32, no. 1, pp. 135–154, 2018.
[7] A. N. Madhavan,Exchange-Traded Funds and the New Dynamics of Investing. Oxford University Press, 2016.
[8] A. Agapova, “Conventional mutual index funds versus exchange-traded funds,”Journal of Financial Markets,
vol. 14, no. 2, pp. 323–343, 2011.
11

The Fungible Reserve Standard: A Deterministic Framework for Encoding Carrying Costs in
Asset-Backed TokensA PREPRINT
[9] G. Gorton and K. G. Rouwenhorst, “Facts and fantasies about commodity futures,”Financial Analysts Journal,
vol. 62, no. 2, pp. 47–68, 2006.
[10] C. B. Erb and C. R. Harvey, “The strategic and tactical value of commodity futures,”Financial Analysts Journal,
vol. 62, no. 2, pp. 69–97, 2006.
[11] S. H. Chan, J. Erickson, and K. Wang,Real Estate Investment Trusts: Structure, Performance, and Investment
Opportunities. Oxford University Press, 2003.
[12] S. Nakamoto, “Bitcoin: A peer-to-peer electronic cash system,” 2008. [Online]. Available:https://bitcoin.
org/bitcoin.pdf
[13] M. Carlsten, H. Kalodner, S. M. Weinberg, and A. Narayanan, “On the instability of Bitcoin without the block
reward,” inProc. 2016 ACM SIGSAC Conf. Computer and Communications Security (CCS), pp. 154–167, 2016.
[14] T. Roughgarden, “Transaction fee mechanism design for the Ethereum blockchain: An economic analysis of
EIP-1559,” 2021. [Online]. Available:https://arxiv.org/abs/2012.00854
[15] Y . Liu, Y . Lu, K. Nayak, f. Zhang, L. Zhang, and Y . Zhao, “Empirical analysis of EIP-1559: Transaction fees,
waiting times, and consensus security,” inProc. 2022 ACM SIGSAC Conf. Computer and Communications Se-
curity (CCS), 2022.
[16] L. W. Cong, Y . Li, and N. Wang, “Tokenomics: Dynamic adoption and valuation,”The Review of Financial
Studies, vol. 34, no. 3, pp. 1105–1155, 2021.
[17] M. Ashfaq, M. Pfeifer, T. G ¨urpinar, and M. A. Gulum, “Tokenized gold in crypto markets: Tracking accuracy
and portfolio performance,”FinTech, vol. 5, no. 1, p. 19, 2026. [Online]. Available:https://www.mdpi.com/
2674-1032/5/1/19
[18] Plume Network, “Plume documentation,” 2024. [Online]. Available:https://plume.org
[19] Polymesh Labs Ltd., “Polymesh whitepaper (Version 3.0),” Jul. 2025. [Online]. Available:https://assets.
polymesh.network/whitepaper.pdf
[20] Canton Network, “Canton Network whitepaper,” 2023. [Online]. Available:https://www.canton.network/
whitepaper
[21] Centrifuge, “Centrifuge documentation,” 2024. [Online]. Available:https://centrifuge.io
[22] Provenance Blockchain Foundation, “Provenance documentation,” 2024. [Online]. Available:https://
provenance.io
[23] F. V ogelsteller and V . Buterin, “EIP-20: Token standard,” Ethereum Improvement Proposals, 2015. [Online].
Available:https://eips.ethereum.org/EIPS/eip-20
[24] Polymath et al., “ERC-1400: Security token standard,” Ethereum Improvement Proposals. [Online]. Available:
https://github.com/ethereum/eips/issues/1411
[25] Tokeny, “EIP-3643: T-REX – Token for Regulated EXchanges,” Ethereum Improvement Proposals. [Online].
Available:https://eips.ethereum.org/EIPS/eip-3643
[26] S. M. Werner, D. Perez, L. Gudgeon, A. Klages-Mundt, D. Harz, and W. Knottenbelt, “SoK: Decentralized
finance (DeFi),” inProc. ACM Conf. Advances in Financial Technologies (AFT), pp. 30–46, 2022.
12
