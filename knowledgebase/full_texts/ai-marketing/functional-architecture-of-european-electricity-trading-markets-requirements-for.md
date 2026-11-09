---
title: 'Functional Architecture of European Electricity Trading Markets: Requirements for AI Supported
  Trading Systems under Regulatory Constraints'
url: https://arxiv.org/abs/2609.29108
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Walter Kurz
- Wojtek Stricker
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.29108
pages: 12
chars: 51917
fetched_at: '2026-11-08T13:20:32+00:00'
kb_version: 1
---

# Functional Architecture of European Electricity Trading Markets: Requirements for AI Supported Trading Systems under Regulatory Constraints

SWISSI AI JOURNAL
Functional Architecture of European Electricity Trading Markets
Requirements for AI Supported Trading Systems under Regulatory Constraints
Walter Kurz1Wojtek Stricker1
1Swissi Institute for AI, kurz@swissi-ai.institute; stricker@swissi-ai.institute
ISSN 3043–1921 | Volume 2026 | https://journal.swissi-ai.institute | journal@swissi-ai.institute | CC BY 4.0
Article SAIJ-cwo7xrcdsaut | DOI: 10.5281/zenodo.21901249 | https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Submitted 01/26; Revised 02/26; Published 03/26
Abstract
European electricity trading in the EU operates as a constrained multi-layer system in which legal design, exchange
microstructure, and network physics are executed jointly across forward, day-ahead, intraday, and balancing horizons.
This paper develops a functional architecture for AI-supported trading that is aligned with market-coupling
mechanics, cross-zonal transfer constraints, and compliance obligations under REMIT, MiFID II, MiFIR, and
EMIR. The contribution is a formal system specification composed of a decision-state vector, residual-exposure
accounting, constrained optimization objective, executable-action permission gate, and fail-closed AI control logic
with auditable records. The analysis maps major Nominated Electricity Market Operator (NEMO) venues and
related exchange operators into an operational venue topology and identifies where cross-border coordination fails in
practice: interface-level timing, permission heterogeneity, and balancing-layer coupling. The resulting framework
proposes how AI can be deployed as a bounded decision component inside regulated market operation with explicit
governance, rather than as an unconstrained prediction layer.
Keywords:EU electricity market, market coupling, NEMO topology, electricity balancing, AI trading systems,
compliance-by-design
In simple terms, energy trading starts long before physical delivery: developers, utilities, and investors decide which
assets to build (for example wind, solar, flexible thermal units, and batteries) by estimating future revenue across
wholesale markets and system services. Once assets are online, producers and retailers hedge part of their expected
volume ahead of delivery, then set the main hourly position in the day-ahead auction, where clearing reflects both bids
and available cross-border transmission capacity. After day-ahead results are published, forecast errors from weather,
demand, or outages create position gaps, and market participants rebalance in intraday trading where prices can move
quickly as new information arrives. Arbitrage appears when the same megawatt-hour has different prices across hours
or bidding zones, so traders buy in lower-priced contexts and sell in higher-priced contexts, limited by transfer capacity
and timing constraints. Batteries are important in this chain because they move energy through time: charge in low
or negative price periods, discharge in high-price periods, and monetize short-cycle volatility that inflexible assets
cannot capture. Close to real time, TSOs activate balancing energy to keep system frequency stable, and remaining
deviations are settled financially as imbalance cost. From an investor viewpoint, the full business case is an end-to-end
stack in which project development quality determines optionality, trading quality determines spread capture, and
governance quality determines how much gross margin survives collateral, penalties, and settlement friction.Agency for
the Cooperation of Energy Regulators, 2026b; European Commission, 2017, 2026a; Nord Pool, 2026b, 2026c
1 Introduction
European electricity trading is a constrained coordination problem in which legal rules and system physics are executed
jointly. Orders clear under cross-zonal transfer limits, bidding-zone definitions, and balancing responsibility assignments,
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 1 / 12
arXiv:2609.29108v2  [cs.AI]  30 Sep 2026

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
so dispatch-feasible outcomes depend on both network conditions and market design parameters.Agency for the
Cooperation of Energy Regulators, 2026b; European Parliament and Council of the European Union, 2019
EU operation is distributed across linked horizons: forward capacity rights, day-ahead coupling, intraday re-dispatch,
and balancing activation close to delivery. These horizons are not independent layers; positions transferred from one
horizon constrain feasible actions in the next, and coupling algorithms apply common cross-zonal capacity inputs at
gate closure.Agency for the Cooperation of Energy Regulators, 2026b; European Commission, 2016
Exchange plurality creates a second constraint class. Member States designate one or more Nominated Electricity
Market Operators, and designated operators can provide services across borders under passporting conditions while
market coupling operator functions are executed jointly.Agency for the Cooperation of Energy Regulators, 2026b Trading
systems that operate across regions must align venue-specific access rules, order handling, and fallback procedures with
synchronized coupling timelines, which creates implementation friction even when legal harmonization exists.Agency
for the Cooperation of Energy Regulators, 2022b
The policy baseline shifted after the 2021–2022 crisis period. The reform package that entered into force on 16 July
2024 kept marginal pricing and strengthened long-term contracting and consumer-risk protection tools.European
Commission, 2026a ACER assessments report substantial welfare gains from integrated market operation and identify
unresolved constraints in cross-border capacity availability and implementation quality.Agency for the Cooperation of
Energy Regulators, 2022b
The current AI literature base in electricity markets is still concentrated on sub-task classes. Reviews synthesize
forecasting-model performance for day-ahead, intraday, and balancing price prediction, while reinforcement-learning
studies optimize bid construction mainly for day-ahead auction settings.Di Persio et al., 2025; Lago et al., 2021;
O’Connor et al., 2025 These strands improve local components but do not provide an integrated architecture that jointly
binds cross-zonal coupling constraints, multi-venue permissions, and compliance-by-design controls across end-to-end
execution.
The missing element is an operational architecture that maps legal obligations, market-coupling mechanics, and
actor permissions into implementable system requirements for AI-supported trading. This paper proposes such an
architecture through five research questions: how horizon layers interact as one functional system, which actors control
binding decisions, which governance constraints define executable permissions, which state variables are required for
decision-ready operation, and how AI support can improve decisions while preserving auditability and compliance.
2 Market design
European electricity market design is a synchronized multi-horizon control system rather than a sequence of independent
auctions. Legal design in Regulation (EU) 2019/943 and the network-code stack couples long-term allocation, day-ahead
clearing, intraday correction, and balancing settlement through common consistency requirements on cross-zonal
capacity use and balancing responsibility.European Commission, 2016, 2026b; European Parliament and Council of the
European Union, 2019
The forward layer allocates transmission rights and hedge structures before delivery, mainly through long-term rights
governed by the Forward Capacity Allocation guideline (FCA). This layer transfers future price and congestion risk
across zones but does not remove physical constraints; it defines admissible hedge translation and in turn constrains
feasible spot decisions in later horizons.European Commission, 2016, 2026b
Day-ahead operation is executed in the Single Day-Ahead Coupling (SDAC) under shared coupling functions where
order books from designated NEMOs are matched jointly with cross-zonal capacities. Clearing solves one coupled
optimization problem across participating bidding zones, with algorithmic outcomes determined by both bid structure
and transfer limits, not by local merit orders in isolation.Agency for the Cooperation of Energy Regulators, 2026a,
2026b; Nord Pool, 2026b
Intraday and balancing layers absorb forecast error and outage shocks under progressively tighter timing constraints.
Intraday continuous trading updates the commercial position close to delivery, while balancing activation and settlement
resolve the residual physical deviation that remains after market close. In system terms, balancing is the terminal
correction stage of the same control process.European Commission, 2026b; European Parliament and Council of the
European Union, 2019; Nord Pool, 2026c
Balancing design in the EU is structurally product- and platform-specific. The Electricity Balancing Guideline (EB
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 2 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
GL) defines harmonization requirements for reserve products and activation processes, while cross-border activation is
organized through dedicated platforms for automatic frequency restoration reserve (aFRR, via PICASSO), manual
frequency restoration reserve (mFRR, via MARI), and replacement reserve processes linked to TERRE implementation
history. These platform mechanics directly affect residual-risk transfer between intraday correction and post-delivery
imbalance settlement.ENTSO-E, 2026a, 2026b, 2026c; European Commission, 2017
The design problem is not only algorithmic coupling but institutional heterogeneity under cross-border execution.
ACER documents strong welfare gains from integration and, at the same time, persistent bottlenecks in capacity
availability and implementation quality across jurisdictions. Combined with a multi-exchange topology under NEMO
passporting, this produces real interface friction in data synchronization, gate-timing coordination, and compliance
encoding for pan-European strategies.Agency for the Cooperation of Energy Regulators, 2022a, 2022b, 2026d
3 Actors and rules
The rule hierarchy combines sector regulation, market-coupling codes, and exchange-level rulebooks. Regulation (EU)
2019/943 sets internal-market principles and cross-border participation logic, while the code stack links allocation
horizons and balancing obligations through the Capacity Allocation and Congestion Management regulation (CACM),
FCA, and EB GL. The 2024 reform package kept marginal pricing and tightened long-term risk-allocation and consumer-
protection instruments, which changes portfolio governance without removing the coupling architecture.European
Commission, 2016, 2026a, 2026b; European Parliament and Council of the European Union, 2019
Integrity and surveillance obligations run in parallel to market-design obligations. REMIT governs wholesale market
integrity and transparency, and operationally this means that trading organizations must separate strategy logic from
prohibited-information use and manipulation patterns while preserving auditable decision records. Derivatives activity
in financial venues adds conduct, transparency, clearing, and reporting constraints under MiFID II, MiFIR, and EMIR,
so compliance control is not a post-trade layer; it is part of executable strategy design.European Parliament and
Council of the European Union, 2011, 2012, 2014a, 2014b
The spot exchange landscape is structurally plural. Under CACM designation rules, each Member State designates at
least one NEMO and designated operators can passport services across borders under defined conditions. ACER’s
January 2026 list shows a multi-operator topology with major designated venues including EPEX Spot, Nord Pool,
OMIE, GME, HEnEx, HUPX, OTE, IBEX, CROPEX, EXAA, TGE, OKTE, OPCOM, BRM, BSP SouthPool,
SEMOpx, and ETPA across day-ahead and intraday service areas.Agency for the Cooperation of Energy Regulators,
2026a, 2026d
For implementation, exchange topology should be encoded as a structured venue matrix with operator and ownership
context. table 1 extends coverage to all major exchanges listed in the current NEMO landscape.Agency for the
Cooperation of Energy Regulators, 2026d
This venue map matters because cross-border strategies fail operationally at interface boundaries, not at conceptual
market level. Distinct operator governance, product eligibility, and procedural timetables require explicit per-venue rule
encoding even under harmonized coupling frameworks.Agency for the Cooperation of Energy Regulators, 2022b, 2026b
Cross-border execution is coordinated through coupled algorithms and synchronized gate windows, not by independent
local clearing. In day-ahead coupling, matching incorporates cross-zonal network constraints and common algorithmic
procedures; in intraday coupling and local continuous books, execution follows stricter timing and order-priority
mechanics close to delivery. Nord Pool documents these mechanics explicitly through SDAC/Euphemia-based day-ahead
matching and first-come first-served intraday execution with 15-minute, 30-minute, hourly, and block products.Agency
for the Cooperation of Energy Regulators, 2026b; Nord Pool, 2026b, 2026c
The derivatives layer is institutionally distinct from the NEMO spot layer and remains critical for hedge transfer,
collateral planning, and basis-risk management. EEX positions itself as the central European power derivatives venue
with integrated spot affiliation through EPEX Spot, ICE Endex provides a large continental energy derivatives venue
across gas, emissions, and power, and Euronext runs Nordic and Baltic power futures and EPAD contracts with the
current post-migration structure launched in 2026.Euronext, 2026; European Energy Exchange, 2026a; Intercontinental
Exchange, 2026
For system architecture, the consequence is a permission matrix rather than a single market-access flag. Venue
membership, product eligibility, gate-closure timing, balancing responsibility, clearing route, and surveillance obligations
jointly determine whether an action is executable. The trading stack must encode those constraints at order-construction
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 3 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Table 1:Major EU short-term electricity exchanges and operator context compiled from ACER and operator disclosures.
Exchange Segment Operator / ownership context Link
EPEX Spot DA, ID EPEX SPOT SE; part of EEX Group.EPEX SPOT, 2026 epexspot.com
Nord Pool DA, ID Nord Pool operator; acquired by Euronext.Nord Pool, 2026a nordpoolgroup.com
OMIE DA, ID Iberian operator under OMI Group structure.OMI Group, 2026; OMIE, 2026 omie.es
GME DA, ID Italian operator GME; wholly owned by GSE.Gestore dei Mercati Energetici, 2026mercatoelettrico.org
HEnEx DA, ID Hellenic Energy Exchange market operator.HEnEx Group, 2026 enexgroup.gr
HUPX DA, ID Hungarian exchange operator; ADEX group context.ADEX Group, 2026; HUPX,
2026
hupx.hu
OTE DA, ID Czech electricity and gas market operator.OTE, a.s., 2026 ote-cr.cz
IBEX DA, ID Bulgarian exchange; sole owner is BSE.Independent Bulgarian Energy Exchange,
2026
ibex.bg
CROPEX DA, ID Croatian exchange operator with system-institution ownership context.CROPEX,
2026
cropex.hr
EXAA DA Austrian exchange with published shareholder structure.EXAA, 2026 exaa.at
TGE DA, ID Towarowa Gielda Energii in GPW Group perimeter.Gielda Papierow Wartosciowych
w Warszawie, 2025
GPW report
OKTE DA, ID Slovak short-term market operator (OKTE, a.s.).OKTE, a.s., 2026 okte.sk
OPCOM DA, ID Romanian operator in Transelectrica group structure.Transelectrica, 2026 transelectrica.ro
BRM DA, ID Romanian Commodities Exchange electricity-market operator.Bursa Romana de
Marfuri, 2026
brm.ro
BSP South-
Pool
DA, ID Slovenian operator; majority stake held by ADEX Group.ADEX Group, 2024; BSP
SouthPool, 2026
bsp-southpool.com
SEMOpx DA, ID NEMO operator in Ireland and Northern Ireland; EirGrid/SONI joint struc-
ture.SEMOpx, 2026
semopx.com
ETPA ID Dutch operator with NEMO license and XBID linkage.ETPA, 2024, 2026 etpa.nl
time, since infeasible or non-compliant actions cannot be repaired downstream without economic loss or regulatory
exposure.Agency for the Cooperation of Energy Regulators, 2026a; European Parliament and Council of the European
Union, 2011, 2012, 2014a, 2014b
4 Trading workflow
Execution starts with rolling portfolio-state construction rather than order placement. Forecast updates for load,
generation, and asset availability are mapped against open forward and derivatives positions to compute residual
volume risk by delivery period and bidding zone. Long-term transmission-right positions from the FCA layer constrain
feasible hedge translation across zones and must be represented before day-ahead order construction.Euronext, 2026;
European Commission, 2016; European Energy Exchange, 2026a; Intercontinental Exchange, 2026
Day-ahead positioning is submitted through designated NEMOs under coupled market operation. Matching in SDAC
is executed with common coupling functions that combine order books and cross-zonal network capacities at gate
closure, so local bid quality and interzonal transfer limits determine clearing jointly. The resulting schedule is a coupled
allocation outcome, not an exchange-isolated merit-order result.Agency for the Cooperation of Energy Regulators,
2026a, 2026b; Nord Pool, 2026b
After day-ahead publication, intraday trading absorbs forecast error and operational events through repeated re-
optimization. Continuous order matching close to delivery follows strict time-priority mechanics, and cross-border
capacity updates propagate directly into executable opportunities. In this phase, execution latency and order-book
depth become binding decision variables because correction windows narrow as delivery approaches.Agency for the
Cooperation of Energy Regulators, 2026b; Nord Pool, 2026c
Residual deviations are resolved through balancing processes administered by TSOs under the balancing-guideline
framework. Balance-responsible parties remain exposed to imbalance outcomes when commercial positions and physical
delivery diverge, and settlement is performed after delivery on measured imbalance quantities and applicable pricing
rules. Cross-border activation pathways now depend on reserve-product and platform allocation, especially for aFRR
and mFRR activation through PICASSO and MARI structures, while replacement-reserve design remains under active
transition pressure.ENTSO-E, 2026a, 2026b, 2026c; European Commission, 2017, 2026b; European Parliament and
Council of the European Union, 2019
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 4 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Post-trade processing closes the loop through confirmation, clearing, reporting, and surveillance controls across venue
types. Spot and cross-border wholesale activity remains subject to REMIT integrity and transparency obligations,
while derivatives legs are shaped by MiFID II and MiFIR market-structure requirements together with EMIR clearing
and reporting duties. A production system must reconcile these layers into one timestamped audit trail linking forecast
state, order intent, execution outcome, and settlement exposure.European Parliament and Council of the European
Union, 2011, 2012, 2014a, 2014b
5 Licensing and permissions
Market entry in European power trading requires two permission stacks that cannot be merged into one checklist. The
first stack defines whether an entity is legally allowed to operate in the relevant regulatory perimeter. The second stack
defines whether that same entity can technically and contractually execute orders in specific markets. Treating these
stacks as one item creates recurrent onboarding failures and compliance gaps at go-live.
5.1 Legal and regulatory prerequisites
At wholesale level, REMIT registration is a pre-trade condition for reportable wholesale energy transactions: the
market participant must register with the competent national regulatory authority and receive an ACER code through
CEREMP before entering into transactions.Agency for the Cooperation of Energy Regulators, 2026c; European
Parliament and Council of the European Union, 2011 Where automated execution is used, the revised REMIT
framework adds a specific algorithmic-trading perimeter with notification and identifier obligations under Article 5a
implementation practice.Agency for the Cooperation of Energy Regulators, 2024; European Parliament and Council of
the European Union, 2024a If the business model extends into power derivatives as financial instruments, the legal
perimeter expands to MiFID II and MiFIR conduct and market-structure obligations together with EMIR clearing and
reporting duties.European Parliament and Council of the European Union, 2012, 2014a, 2014b In parallel, physical
delivery exposure remains tied to balancing responsibility under EU electricity-market rules, either via own BRP setup
or a contracted balance-responsibility arrangement.European Commission, 2017; European Parliament and Council of
the European Union, 2019
5.2 System and venue permissions
Legal status does not grant executable market access. Venue access is governed by exchange and clearing documentation,
participant agreements, admission checks, and technical onboarding processes. Nord Pool documents this explicitly
through rulebook and participant-agreement scope plus member-approval conditions that include authorization and
fit-and-proper requirements.Nord Pool, 2024, 2026d In the derivatives layer, EEX access documentation states the
same separation structurally: exchange participation and clearing admission at ECC are distinct permissions that must
both be in place before production trading.European Energy Exchange, 2026b
From a system-design perspective, this separation means a trading platform must encode two independent gates
for every action candidate: a legal-regulatory gate and a venue-execution gate. The first gate validates entity-level
regulatory admissibility; the second gate validates market-, product-, and counterparty-level execution permissions.
Only their intersection defines executable actions in production.
6 System requirements
A decision-ready trading system requires a compact state representation that merges market microstructure, physical
position, and regulatory feasibility. The minimum operational state is defined in Equation(1) as a tuple of market
descriptors, portfolio state, transfer limits, executable prices, risk state, and compliance state at decision timet.
st = (µt, νt, κt, πt, ρt, σt)(1)
In this notation,µt denotes market-status variables such as gate state and venue mode,νt the physical and contractual
portfolio state, κt cross-zonal capacity state,πt executable price and depth state,ρt risk state, andσt compliance state
under market-integrity and venue rules.Agency for the Cooperation of Energy Regulators, 2026a, 2026b; European
Commission, 2026b; European Parliament and Council of the European Union, 2011
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 5 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Residual delivery exposure must be computed per interval and bidding zone before any order is submitted. Equation(2)
defines the signed residual quantity that propagates from forecasting and hedge translation into day-ahead, intraday,
and balancing decisions.
ξt,z =d t,z −g t,z −h t,z −x DA t,z −x ID t,z −b t,z (2)
Here dt,z is forecast demand,gt,z controllable generation, ht,z forward and derivatives hedge volume translated to zone
z, xDA t,z and xID t,z cleared day-ahead and intraday positions, andbt,z activated balancing volume. The residualξt,z is the
direct driver of imbalance exposure.European Commission, 2016; European Parliament and Council of the European
Union, 2019; Nord Pool, 2026b, 2026c
A production objective must combine execution cost, imbalance risk, and regulatory cost in one optimization problem.
Equation (3) formalizes this as a constrained objective over market actionsx.
min
x
J=
X
t,z

πDA t,z xDA t,z +π ID t,zxID t,z +λ t,z|ξt,z|  +αCVaR β(L) +γC reg (3)
s.t.−κ t,ℓ ≤ϕ t,ℓ ≤κ t,ℓ, τ≤τ GC t,m
In Equation(3), λt,z prices imbalance risk,CVaRβ(L)is the tail-risk term at confidence levelβ, α and γ are policy
weights, ϕt,ℓ is scheduled flow on interconnectorℓ, κt,ℓ is available transfer capacity, andτ GC t,m is the gate-closure time
for market m. These constraints encode coupling and timing rules directly in the optimizer.Agency for the Cooperation
of Energy Regulators, 2026b; European Commission, 2026b; Nord Pool, 2026b
Execution feasibility cannot be inferred from price signals alone; it must be checked against venue permissions and
regulatory predicates at order granularity. The executable-action indicator in Equation (4) represents this gate.
Ωi =1
h
τi ≤τ GC m(i)
i
1

ui ∈ Um(i)

1

pi ∈ Pm(i)

1

ri ∈ Rm(i)

(4)
For order candidatei,Ω i = 1is required for release to the venue;Um(i) is the authorized participant set,Pm(i) the
permitted product set, andRm(i) the active regulatory predicate set. This structure links exchange access, product
scope, and surveillance obligations to the same control decision.Agency for the Cooperation of Energy Regulators,
2026a; European Parliament and Council of the European Union, 2011, 2012, 2014a, 2014b
7 Battery storage and temporal arbitrage
Merit-order pricing in markets with high renewable penetration produces structural temporal spreads. When wind or
solar output exceeds demand, zero-marginal-cost generation depresses clearing prices; when output drops or demand
peaks, scarcity pricing takes over. These are not transient anomalies but persistent features of the energy transition: as
renewable capacity grows, both the frequency and magnitude of intra-day price swings increase. European intraday
markets regularly exhibit spreads exceeding100EUR/MWh between off-peak surplus hours and peak scarcity hours
within the same delivery day.Nord Pool, 2026b, 2026c
Battery storage is the physical instrument that captures temporal spreads. The operating principle is direct: charge
when the clearing price is low, discharge when it is high, and retain the difference minus round-trip efficiency losses and
degradation cost. A storage operator with a100 MW/200 MW hsystem charging at20EUR/MWh and discharging
at140 EUR/MWh captures a gross margin of24 000EUR per cycle before efficiency, grid fees, and wear adjustments.
Multiple cycles per day are feasible in markets with strong solar midday troughs and evening demand peaks, which
compounds daily revenue.
The business case strengthens when a battery participates across multiple market layers simultaneously. Day-ahead
arbitrage captures the base spread from overnight positioning. Intraday re-optimization captures additional value
from forecast errors: when wind or solar output deviates from the day-ahead forecast, intraday prices shift and the
battery adjusts its schedule. Balancing and frequency response services add a third revenue layer, where the battery
earns activation payments for fast power injection or withdrawal under TSO procurement.ENTSO-E, 2026a, 2026b;
European Commission, 2017 This combination of revenue streams across horizons is the core of what practitioners call
value stacking, and it is the reason that battery returns can exceed single-market projections by a wide margin.
From an architecture perspective, batteries represent the canonical multi-horizon optimization problem. Optimal
dispatch requires joint consideration of day-ahead price expectations, intraday correction opportunities, balancing
activation probabilities, state-of-charge constraints, and degradation cost across overlapping delivery windows. Each
decision changes the feasible set for subsequent decisions: a battery that commits capacity to frequency response cannot
simultaneously use that capacity for intraday arbitrage. This coupling between horizons and markets is precisely the
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 6 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
problem that the state vector in Equation(1) and the constrained objective in Equation(3) are designed to represent,
making battery dispatch a primary validation case for the proposed architecture.
8 AI architecture
The architecture is modeled as a constrained policy system that maps operational statest to executable actions while
preserving risk and regulatory bounds. Equation(5) defines the optimization target as expected utility with explicit
tail-risk and governance penalties.
max
θ
J(θ) =E
" TX
t=1

rt(at,s t)−αCVaR β(Lt)−γ C gov t
#
(5)
s.t.Ω t(at) = 1, a t ∈ A(st)
In Equation(5), θ parameterizes the decision policy,rt is realized economic reward,CVaRβ(Lt)is the tail-loss term at
confidence level β, and C gov t represents governance and control cost. The executable-action constraintΩt(at) = 1links
the policy directly to venue and rule feasibility.European Parliament and Council of the European Union, 2011, 2012,
2014a, 2014b; Rockafellar and Uryasev, 2000
Forecasting and opportunity ranking use calibrated predictive distributions rather than point forecasts. Equation(6)
specifies a distribution-free coverage requirement for the predictive setΓ1−δ(st), which is consumed by downstream
decision and risk modules.
P(yt+h ∈Γ 1−δ(st))≥1−δ(6)
The confidence parameterδ controls interval width and directly influences aggressiveness in intraday repositioning;
lower δ increases protection against forecast misspecification at the cost of reduced expected capture.Angelopoulos and
Bates, 2021; Nord Pool, 2026c
Execution control is fail-closed by construction. Equation (7) enforces release only when profitability, risk, and
compliance predicates are simultaneously satisfied.
at =



arg max
a∈A(st)
Ut(a),Ω t(a) = 1∧R t(a)≤¯ρ∧M t(a)≥µ
∅,otherwise
(7)
Here Ut(a)is utility, Rt(a)predicted risk, ¯ρthe risk budget,Mt(a)a market-quality predicate combining depth and
latency conditions, and µ its acceptance threshold. The null action∅ is a valid output and preserves safety when
constraints are violated.Agency for the Cooperation of Energy Regulators, 2026b; European Parliament and Council of
the European Union, 2011
Operational robustness requires explicit model-risk supervision and automatic strategy downgrades. Equation(8)
defines the override controller that switches to a conservative policy when either distribution drift or calibration error
exceeds control limits.
πt =
(
πθ,∆ t ≤η ∆ ∧ε t ≤η ε
πsafe,otherwise
(8)
The drift statistic∆t tracks state-distribution shift,εt measures uncertainty-calibration error, andη∆, ηε are supervisory
thresholds tuned to tolerated operational risk.European Commission, 2026b; Tabassi, 2023
Auditability is treated as a first-class output variable. Equation(9) defines the minimal immutable record tuple stored
for each decision.
ℓt = (st,ˆyt,Γ 1−δ(st), at,Ω t, πt, ξt)(9)
The record ℓt captures state, forecast, uncertainty set, executed action, feasibility gate result, active policy, and
residual exposure ξt, which allows line-by-line reconstruction from forecast input to settlement consequence. This
structure supports surveillance expectations under REMIT and documentation discipline aligned with EU AI governance
requirements.European Parliament and Council of the European Union, 2011, 2024b
A reproducible validation protocol requires a fixed metric vector spanning economic, risk, compliance, and latency
dimensions. Equation (10) defines the minimal validation tuple for model and policy comparison.
v=

E[Π],CVaR β(L), Cimb,FPR comp,FNR comp,Λ 95

(10)
Here E[Π]is expected trading result, CVaRβ(L)tail-loss risk, C imb imbalance settlement cost,FPRcomp and FNRcomp
compliance false-positive and false-negative rates, andΛ95 the 95th-percentile decision-to-order latency.
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 7 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Backtesting should be executed over an explicit stress set rather than a single historical regime. Equation(11) defines
a compact scenario basis for evaluation across normal operation, congestion stress, forecast shock, outage regimes, and
decoupling fallback events.
S=
n
sbase, scong, sforecast, soutage, sdecouple
o
(11)
For eachs∈ S, the policy is accepted only if performance improves on baseline while preserving feasibility-gate integrity
and governance thresholds. This design aligns risk validation with AI lifecycle supervision and platform-level market
constraints.Agency for the Cooperation of Energy Regulators, 2026b; Rockafellar and Uryasev, 2000; Tabassi, 2023
9 Discussion
Forecasting reviews benchmark model accuracy for day-ahead, intraday, and balancing prices, while reinforcement-
learning studies optimize bid construction for single-venue auction settings.Di Persio et al., 2025; Lago et al., 2021;
O’Connor et al., 2025 These contributions improve local component performance but treat market layers as independent
optimization contexts. The architecture proposed here differs by modeling horizon coupling, cross-zonal capacity
constraints, and multi-venue permission rules as joint inputs to a single decision process.Agency for the Cooperation
of Energy Regulators, 2026b; European Parliament and Council of the European Union, 2019 Under this framing, a
day-ahead bid is not an isolated optimization output; it is a coupled decision whose feasibility depends on forward
hedge state, intraday correction capacity, and balancing-layer exposure.
The permission gate formalized in Equation(4) shifts compliance enforcement from post-trade monitoring to pre-trade
construction. In conventional system design, regulatory checks are applied as filters after an optimizer produces
candidate orders. The architecture inverts this relationship: venue membership, product eligibility, gate-closure timing,
and regulatory predicates enter the optimization as hard constraints, so infeasible or non-compliant actions cannot be
generated.Agency for the Cooperation of Energy Regulators, 2026a; European Parliament and Council of the European
Union, 2011 The fail-closed logic in Equation(7) extends this principle to the AI decision layer, where the system
defaults to inaction when any constraint is violated rather than requiring explicit exception handling for each failure
mode.
The EU AI Act and the NIST AI Risk Management Framework define lifecycle governance structures for AI systems
but do not specify how these structures map to sector-specific market mechanics.European Parliament and Council of
the European Union, 2024b; Tabassi, 2023 The architecture proposed here operationalizes governance for electricity
trading by embedding auditability, uncertainty calibration, and override controls as system components rather than
documentation requirements. The audit record tuple in Equation (9) and the drift-triggered policy override in
Equation (8) translate abstract governance expectations into executable logic that can be tested, monitored, and
verified against regulatory thresholds.
10 Conclusion
The paper proposes a unified interpretation of European electricity trading as a coupled control problem across
forward, day-ahead, intraday, and balancing horizons. Market outcomes are shown as joint products of capacity-
constrained coupling, venue timing rules, and actor-specific obligations rather than isolated auction results.Agency for
the Cooperation of Energy Regulators, 2026b; European Commission, 2026b; European Parliament and Council of the
European Union, 2019
The governance analysis indicates that executable trading logic is defined by an interaction of sector and financial
regulation with exchange-level permissions. REMIT, MiFID II, MiFIR, and EMIR map directly into pre-trade
admissibility checks and post-trade accountability requirements, while NEMO designation and passporting rules explain
the persistent multi-venue topology of EU spot markets.Agency for the Cooperation of Energy Regulators, 2026a,
2026d; European Parliament and Council of the European Union, 2011, 2012, 2014a, 2014b
The system contribution is a minimal decision architecture that links state representation, residual exposure accounting,
constrained optimization, uncertainty calibration, and fail-closed execution control. This framework proposes how
AI support can be integrated without separating economic optimization from regulatory feasibility or auditabil-
ity.Angelopoulos and Bates, 2021; European Parliament and Council of the European Union, 2024b; Rockafellar and
Uryasev, 2000; Tabassi, 2023
The resulting position is methodological and operational: model the market as one constrained system, encode
permissions before execution, and treat uncertainty and governance as first-class state variables. Under this framing,
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 8 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
AI is proposed as a bounded decision component inside regulated market operation, not as an autonomous layer outside
institutional control.
11 Limitations
The framework is scoped to EU wholesale electricity trading and does not claim completeness for all national
implementation detail. Code-level harmonization coexists with local market design differences, and the practical burden
of rule interpretation remains jurisdiction-sensitive at delivery-zone and venue levels.Agency for the Cooperation of
Energy Regulators, 2026d; European Commission, 2026b
The operational model abstracts from data-path fragility that materially affects live performance: feed latency, revision
frequency asymmetry, and outage behavior across venues and operators. These factors can dominate theoretical edge
in intraday correction windows and can degrade any policy calibrated on clean historical snapshots.Agency for the
Cooperation of Energy Regulators, 2026b; Nord Pool, 2026c
The legal environment is dynamic. Regulatory obligations in AI governance, market integrity, and financial-market
supervision continue to evolve, which limits the temporal stability of any fixed compliance encoding. Production deploy-
ment requires continuous legal versioning and rule-to-control trace updates, not one-time policy certification.European
Parliament and Council of the European Union, 2011, 2014a, 2014b, 2024b
The quantitative formulation still requires empirical validation on synchronized multi-venue event streams with realistic
transaction-cost, latency, and imbalance-penalty models. The next research stage is out-of-sample evaluation under
stress regimes and controlled ablations of risk, calibration, and governance gates to estimate the marginal value of each
architectural constraint.Angelopoulos and Bates, 2021; Rockafellar and Uryasev, 2000; Tabassi, 2023
References
ADEX Group. (2024).Adex group closes acquisition of majority stake in bsp southpool. Retrieved March 4, 2026, from
https://adexgroup.com/adex-group-closes-acquisition-of-majority-stake-in-bsp-southpool/
ADEX Group. (2026).About us. Retrieved March 4, 2026, from https://adexgroup.com/about-us/
Agency for the Cooperation of Energy Regulators. (2022a, April).Acer’s final assessment of the eu wholesale electricity
market design. Retrieved March 4, 2026, from https://acer.europa.eu/news-and-events/news/acers-final-
assessment-eu-wholesale-electricity-market-design
Agency for the Cooperation of Energy Regulators. (2022b, April).Final assessment of the eu wholesale electricity
market design. Retrieved March 4, 2026, from https://www.acer.europa.eu/Publications/Final_Assessment_
EU_Wholesale_Electricity_Market_Design.pdf
Agency for the Cooperation of Energy Regulators. (2024, July).Revised remit brings new obligations market participants
acer addresses algorithmic trading notifications. Retrieved March 4, 2026, from https://www.acer.europa.eu/
news-and-events/news/revised-remit-brings-new-obligations-market-participants-acer-addresses-algorithmic-
trading-notifications
Agency for the Cooperation of Energy Regulators. (2026a).Designation of nemos. Retrieved March 4, 2026, from
https://www.acer.europa.eu/electricity/market-rules/capacity-allocation-and-congestion-management/
implementation/designation-of-nemos
Agency for the Cooperation of Energy Regulators. (2026b).Market coupling development under cacm. Retrieved March
4, 2026, from https://www.acer.europa.eu/electricity/market-rules/capacity-allocation-and-congestion-
management-cacm/market-coupling-development
Agency for the Cooperation of Energy Regulators. (2026c).Registration of market participants. Retrieved March 4,
2026, from https://www.acer.europa.eu/remit/remit-portal/registration-market-participants
Agency for the Cooperation of Energy Regulators. (2026d, January).List of currently designated nemos and the
information in which member states they provide services. Retrieved March 4, 2026, from https://www.acer.
europa.eu/sites/default/files/documents/en/Electricity/MARKET-CODES/CAPACITY-ALLOCATION-
AND-CONGESTION-MANAGEMENT/Documents/NEMOs-list-January-2026.pdf
Angelopoulos, A. N., & Bates, S. (2021). A gentle introduction to conformal prediction and distribution-free uncertainty
quantification.CoRR,abs/2107.07511. Retrieved March 4, 2026, from https://arxiv.org/abs/2107.07511
BSP SouthPool. (2026).About us. Retrieved March 4, 2026, from https://www.bsp-southpool.com/about-us/
Bursa Romana de Marfuri. (2026).Markets managed by the romanian commodities exchange. Retrieved March 4, 2026,
from https://brm.ro/en/markets/
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 9 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
CROPEX. (2026).About us. Retrieved March 4, 2026, from https://www.cropex.hr/en/about-us
Di Persio, L., Garbelli, M., & Giordano, L. M. (2025). Reinforcement learning for bidding strategy optimization in
day-ahead energy market.Energy Economics,149, 108673. https://doi.org/10.1016/j.eneco.2025.108673
ENTSO-E. (2026a).Mari platform. Retrieved March 4, 2026, from https://www.entsoe.eu/network_codes/eb/mari/
ENTSO-E. (2026b).Picasso platform. Retrieved March 4, 2026, from https://www.entsoe.eu/network_codes/eb/
picasso/
ENTSO-E. (2026c).Terre platform. Retrieved March 4, 2026, from https://www.entsoe.eu/network_codes/eb/terre/
EPEX SPOT. (2026).Company information. Retrieved March 4, 2026, from https://www.epexspot.com/en/company-
information
ETPA. (2024).Etpa acquires european trading license and growth capital from set ventures and abn amro. Retrieved
March 4, 2026, from https://www.etpa.nl/en/news/etpa-acquires-european-trading-license-and-growth-
capital-from-set-ventures-and-abn-amro
ETPA. (2026).About. Retrieved March 4, 2026, from https://www.etpa.nl/en/about
Euronext. (2026).Power derivatives - euronext nord pool power futures. Retrieved March 4, 2026, from https:
//live.euronext.com/en/products/commodities/power-derivatives
European Commission. (2016).Commission regulation (eu) 2016/1719 of 26 september 2016 establishing a guideline on
forward capacity allocation. Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-content/EN/TXT/
?uri=uriserv:OJ.L_.2016.259.01.0042.01.ENG&toc=OJ:L:2016:259:TOC
European Commission. (2017).Commission regulation (eu) 2017/2195 of 23 november 2017 establishing a guideline on
electricity balancing. Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
CELEX:32017R2195
European Commission. (2026a).Electricity market design. Retrieved March 4, 2026, from https://energy.ec.europa.eu/
topics/markets-and-consumers/electricity-market-design_en
European Commission. (2026b).Electricity network codes and guidelines. Retrieved March 4, 2026, from https:
//energy.ec.europa.eu/topics/markets-and-consumers/wholesale-energy-market/electricity-network-codes-
and-guidelines_en
European Energy Exchange. (2026a).Power. Retrieved March 4, 2026, from https://www.eex.com/en/markets/power
European Energy Exchange. (2026b).Power derivatives access and trading. Retrieved March 4, 2026, from https:
//www.eex.com/en/markets/power/power-derivatives/access-and-trading
European Parliament and Council of the European Union. (2011).Regulation (eu) no 1227/2011 on wholesale energy
market integrity and transparency (remit). Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-
content/EN/TXT/?uri=CELEX:32011R1227
European Parliament and Council of the European Union. (2012).Regulation (eu) no 648/2012 on otc derivatives, central
counterparties and trade repositories (emir). Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-
content/EN/TXT/?uri=CELEX:32012R0648
European Parliament and Council of the European Union. (2014a).Directive 2014/65/eu on markets in financial
instruments (mifid ii). Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
celex%3A32014L0065
European Parliament and Council of the European Union. (2014b).Regulation (eu) no 600/2014 on markets in financial
instruments (mifir). Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=
celex%3A32014R0600
European Parliament and Council of the European Union. (2019).Regulation (eu) 2019/943 of 5 june 2019 on the
internal market for electricity. Retrieved March 4, 2026, from https://eur-lex.europa.eu/legal-content/EN/
TXT/?uri=uriserv:OJ.L_.2019.158.01.0054.01.ENG&toc=OJ:L:2019:158:TOC
European Parliament and Council of the European Union. (2024a).Regulation (eu) 2024/1106 of 29 april 2024
amending regulations (eu) no 1227/2011 and (eu) 2019/942 as regards improving the union’s protection
against market manipulation in the wholesale energy market. Retrieved March 4, 2026, from https://eur-
lex.europa.eu/eli/reg/2024/1106/oj
European Parliament and Council of the European Union. (2024b, July).Regulation (eu) 2024/1689 laying down
harmonised rules on artificial intelligence. Retrieved March 4, 2026, from https://op.europa.eu/en/publication-
detail/-/publication/dc8116a1-3fe6-11ef-865a-01aa75ed71a1/language-en
EXAA. (2026).About exaa. Retrieved March 4, 2026, from https://www.exaa.at/en/about-exaa/
Gestore dei Mercati Energetici. (2026).Organization. Retrieved March 4, 2026, from https://www.mercatoelettrico.
org/en-us/Home/Aboutus/Organization
Gielda Papierow Wartosciowych w Warszawie. (2025).Gpw group h1 2025 consolidated financial report. Retrieved
March 4, 2026, from https://pap-mediaroom.pl/sites/default/files/2025-09/GPW_Group_H1_2025_
Consolidated_Financial_Report.pdf
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 10 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
HEnEx Group. (2026).Company profile. Retrieved March 4, 2026, from https://www.enexgroup.gr/web/guest/company-
profile
HUPX. (2026).About. Retrieved March 4, 2026, from https://hupx.hu/about
Independent Bulgarian Energy Exchange. (2026).Profile. Retrieved March 4, 2026, from https://ibex.bg/en/profile.html
Intercontinental Exchange. (2026).Ice endex energy exchange for gas and power. Retrieved March 4, 2026, from
https://www.ice.com/ENDEX
Lago, J., Marcjasz, G., De Schutter, B., & Weron, R. (2021). Forecasting day-ahead electricity prices: A review
of state-of-the-art algorithms, best practices and an open-access benchmark.Applied Energy,293, 116983.
https://doi.org/10.1016/j.apenergy.2021.116983
Nord Pool. (2024).General terms and conditions. Retrieved March 4, 2026, from https://www.nordpoolgroup.com/en/
trading/Rule-and-regulations/General-terms-and-conditions/
Nord Pool. (2026a).About us. Retrieved March 4, 2026, from https://www.nordpoolgroup.com/en/about-us/
Nord Pool. (2026b).Day-ahead market. Retrieved March 4, 2026, from https://www.nordpoolgroup.com/en/the-power-
market/Day-ahead-market/
Nord Pool. (2026c).Intraday market. Retrieved March 4, 2026, from https://www.nordpoolgroup.com/en/the-power-
market/Intraday-market/
Nord Pool. (2026d).Rules and regulations. Retrieved March 4, 2026, from https://www.nordpoolgroup.com/en/trading/
Rule-and-regulations/
O’Connor, C., Bahloul, M., Prestwich, S., & Visentin, A. (2025). A review of electricity price forecasting models in the
day-ahead, intra-day, and balancing markets.Energies,18(12), 3097. https://doi.org/10.3390/en18123097
OKTE, a.s. (2026).Day-ahead detailed overview. Retrieved March 4, 2026, from https://www.okte.sk/en/short-term-
market/published-information-of-dam/day-ahead-detailed-overview/
OMI Group. (2026).Faqs. Retrieved March 4, 2026, from https://www.grupoomi.eu/en/faqs/
OMIE. (2026).About us. Retrieved March 4, 2026, from https://www.omie.es/en/about-us
OTE, a.s. (2026).Basic facts. Retrieved March 4, 2026, from https://www.ote-cr.cz/en/basic-facts
Rockafellar, R. T., & Uryasev, S. (2000). Optimization of conditional value-at-risk.Journal of Risk,2(3), 21–42.
https://doi.org/10.21314/JOR.2000.038
SEMOpx. (2026).About semopx. Retrieved March 4, 2026, from https://www.semopx.com/about/
Tabassi, E. (2023).Artificial intelligence risk management framework (ai rmf 1.0)(tech. rep. No. NIST AI 100-1).
National Institute of Standards and Technology. https://doi.org/10.6028/NIST.AI.100-1
Transelectrica. (2026).Opcom. Retrieved March 4, 2026, from https://www.transelectrica.ro/web/tel/opcom
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 11 / 12

DOI: 10.5281/zenodo.21901249 | Machine-readable record: https://journal.swissi-ai.institute/doi/cwo7xrcdsaut
Declarations
CITE THIS ARTICLE (BIBTEX)
@article{saijcwo7xrcdsaut,
author = {Kurz, W. and Stricker, W.},
title = {Functional Architecture of European Electricity Trading Markets: Requirements for AI Supported Trading
Systems under Regulatory Constraints},
journal = {Swissi AI Journal},
year = {2026},
volume = {2026},
note = {Article SAIJ-cwo7xrcdsaut},
issn = {3043-1921},
doi = {10.5281/zenodo.21901249},
url = {https://journal.swissi-ai.institute/doi/cwo7xrcdsaut}
}
PAPER INFORMATION
AFFILIATIONS 1Swissi Institute for AI, kurz@swissi-ai.institute; stricker@swissi-ai.institute
CORRESPONDING AUTHORWalter Kurz, kurz@swissi-ai.institute, ORCID 0009-0006-8045-4775
ARTICLE TYPEResearch Article
SWISSI ADDRESSSw2:academic01:obj:p1:cwo7xrcdsautxpkgbbkyzdopwojp6sgpfi2txhmyopeatkm3dypa:d741c563
PAPER DECLARATIONS
AUTHOR CONTRIBUTIONSAll authors contributed equally to this article.
FUNDINGThis research received no external funding.
CONFLICTS OF INTERESTThe authors declare no conflicts of interest.
DATA AND CODE
AVAILABILITY
The data and code supporting this article are available from the corresponding author on reasonable
request.
USE OF AI TOOLSGenerative AI tools were used for editorial work only, such as language editing and formatting, in
accordance with international scientific standards. The authors verified the content and remain fully
responsible for the article.
JOURNAL INFORMATION
PUBLISHERSwissi AI Journal
EDITORIAL DATESSubmitted 01/26; Revised 02/26; Published 03/26
LICENCECC BY 4.0
OPEN ACCESShttps://journal.swissi-ai.institute/authors#open-access
CREDIT TAXONOMYhttps://journal.swissi-ai.institute/authors#credit-taxonomy
JOURNAL CONTACThttps://journal.swissi-ai.institute | journal@swissi-ai.institute
Swissi AI Journal | ISSN 3043–1921 | Volume 2026 Page 12 / 12
