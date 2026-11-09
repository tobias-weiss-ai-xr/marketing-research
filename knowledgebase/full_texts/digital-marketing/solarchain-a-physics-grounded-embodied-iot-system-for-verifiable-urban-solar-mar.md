---
title: 'SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design'
url: https://arxiv.org/abs/2605.23162
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Shilin Ou
- Yifan Xu
- Zhenshan Zhang
- Luyao Zhang
- Ming-Chun Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.23162
pages: 10
chars: 53044
fetched_at: '2026-11-08T13:06:16+00:00'
kb_version: 1
---

# SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design

SolarChain: A Physics-Grounded Embodied IoT System for
Verifiable Urban Solar Market Design
Shilin Ou†
Duke Kunshan University
Suzhou, China
Yifan Xu†
Duke Kunshan University
Suzhou, China
Zhenshan Zhang†§
Duke Kunshan University
Suzhou, China
Luyao Zhang∗
Duke Kunshan University
Suzhou, China
Ming-Chun Huang∗
Duke Kunshan University
Suzhou, China
Figure 1: System architecture ofSolarChain. The three-layer implementation connects an off-chain physics engine, a decentral-
ized frontend, and on-chain contracts. Market allocation is configurable, with a 20/80 producer-reward/liquidity default in this
prototype.
Abstract
Distributed solar markets must coordinate physical reports, eco-
nomic allocation, and public settlement even when IoT data can
be manipulated. We presentSolarChain, a controlled Embodied
Intelligence of Things (EIoT) prototype that integrates four func-
tions: physics-bounded screening of photovoltaic reports, persistent
agent and planner coordination, configurable allocation between
producer rewards and market liquidity, and replayable hash-linked
auditing of settlement decisions. The benchmark combines city-
level historical weather inputs with physics-modeled generation
†Equal contribution.
§Z.Z. completed this work while at DKU and is now at Johns Hopkins University.
∗Joint corresponding authors.
Email: Zhang: lz183@duke.edu; Huang: mh596@duke.edu. Address: 8 Duke Ave, Kun-
shan, Suzhou, Jiangsu 215316, China.
bounds and synthetic nodes, demand, trades, and scripted attacks.
On 36,000 monthly records, an IQR/MAD baseline attains F1=1.000,
while the rule-based adaptive verifier attains F1=0.988 and provides
physically interpretable decision evidence; it is not uniformly su-
perior across attack classes. A sensitivity sweep selects a 20/80
reward/liquidity default under the stated simulation assumptions,
while showing the incentive–liquidity trade-off. These results pro-
vide reproducible evidence from a controlled prototype, not proof of
deployment readiness. We release the code, data, and audit artifacts
in the spirit of open science.
CCS Concepts
•Human-centered computing→ Ubiquitous and mobile com-
puting systems and tools;•Computer systems organization
arXiv:2605.23162v2  [cs.CY]  12 Aug 2026

UbiComp Companion ’26, October 11–15, 2026, Shanghai, China Ou et al.
→ Sensor networks;•Security and privacy → Distributed
systems security;•Computing methodologies → Multi-agent
systems;•Software and its engineering → Software infras-
tructure.
Keywords
embodied Internet of Things, physics-grounded verification, multi-
agent coordination, urban solar energy, decentralized energy mar-
kets
1 Introduction
Urban photovoltaic (PV) systems increasingly participate in local
energy coordination rather than operating as passive generators,
adding flexibility and management complexity to distributed grids
[5, 11]. Peer-to-peer markets can reward prosumers and aggregate
distributed flexibility [1, 17], but they also couple physical mea-
surements to digital incentives. A ledger can preserve a submitted
record without establishing that the underlying generation report
was physically plausible. False-data injection can therefore create
fictitious supply, rewards, or settlement events [ 13, 18]. Market
design introduces a second dependency: assigning more accepted
value to individual rewards leaves less value for shared liquidity.
Prior studies address grid anomaly detection, on-chain energy
markets, and decentralized physical infrastructure as distinct prob-
lems. Their combination leaves a systems question:Can a controlled
Embodied Intelligence of Things (EIoT) prototype connect physics-
bounded PV reports to coordinated market settlement with traceable
evidence, and what limitations become visible when that chain is eval-
uated end to end?This question concerns integration and evidence,
not the novelty of each component in isolation.
We answer this question withSolarChain. City-level historical
weather and solar geometry first bound each simulated PV report.
Persistent Solar, Planner, Factory, and Market agents then coordi-
nate verification and participation. A configurable contract divides
accepted value between producer rewards and market liquidity,
while hash-linked events make each decision replayable. In EIoT
terms [14], the simulated PV body, weather context, and physical
constraints constituteenactment. Cross-role coordination provides
engagement, and accumulated residuals with updates to calibration,
trust, and participation state representevolution. This evolution
is rule-based rather than learned continual adaptation. Because
no physical agents are deployed, the study evaluates a simulated
decision path rather than a field system.
This paper makes three system-level contributions:
• a cross-layer workflow linking bounded PV reports, per-
sistent coordination, configurable allocation, and contract
settlement;
• a replayable evaluation spanning statistical and physics-
grounded verifiers, 11 scripted attack classes, allocation sen-
sitivity, runtime, and audit-chain integrity; and
• an open benchmark separating sourced weather, physics-
modeled variables, and synthetic system behavior so the
evidence can be reproduced without overstating field valid-
ity.
The results are deliberately scoped to a simulated prototype. The
attacks are scripted rather than adaptive, and the inputs contain
Table 1: Mapping Between EIoT dimensions and the con-
trolled prototype.
Dimension Prototype summary (realization; evidence; boundary)
Enacted PV nodes + city weather + physics-bounded reports; 50 nodes and
36,000 node-hours with modeled𝑃 max; no inverter/meter telemetry.
Engaged Solar/Planner/Factory/Market roles coordinate via reports, demand,
and settlement events; decision + market traces, local-EVM, hash-linked
log; rule-based trust.
Evolutionary Residual, trust, calibration, and participation state persists across steps;
state histories and attack-wise verifier results; stateful but not learned
adaptation.
neither inverter nor smart-meter telemetry. Code, data, and audit
artifacts are available online.1
2 Background and Design Requirements
2.1 EIoT and Decentralized Infrastructure
EIoT characterizes embodied systems through enacted grounding,
engaged interaction, and evolutionary adaptation [14]. Urban com-
puting supplies the broader spatial and infrastructural setting [25],
while DePIN research studies how distributed contributors can pro-
vide physical resources under digital coordination and incentives
[6, 12]. These perspectives motivate a stateful, cross-layer system,
but they do not by themselves authenticate a PV measurement.
We therefore treat EIoT as an organizing framework and explicitly
distinguish simulated embodiment from deployment.
2.2 Physical Plausibility and False Data
Conventional residual tests can miss attacks constructed to pre-
serve a grid estimator’s expected residual [13]; spatiotemporal and
learned detectors add contextual evidence [ 15, 18, 19]. Physics-
informed methods encode domain constraints into inference [20],
while secure-control frameworks protect distributed operation against
false-data injection [7]. For PV systems, established models connect
irradiance, solar position, temperature, and hardware parameters to
expected output [3, 9, 22]. Such an envelope can reject impossible
reports without training data, but a plausible within-bound value
may still be false. A useful verifier should thus retain multiple forms
of evidence and expose rather than conceal its attack-class failures.
2.3 Energy Markets, Ledgers, and Oracles
Peer-to-peer energy markets coordinate prosumer exchange and
flexibility [1, 17]; blockchain implementations make market state
and rules inspectable [ 10, 16, 21]. However, blockchain energy-
trading systems still depend on off-chain measurements, and vali-
dation and oracle mechanisms manage rather than eliminate that
trust boundary [23, 24]. Liquidity mechanisms also rest on explicit
price and allocation assumptions [4]. Renewable ledgers must addi-
tionally address participant identity and double counting [8]. Ac-
cordingly, a hash-linked settlement trace proves what the software
processed, not the truth of the originating sensor or the environ-
mental meaning of a token event.
1https://github.com/Global-Nomad-Nexus/SolarSave

SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design UbiComp Companion ’26, October 11–15, 2026, Shanghai, China
(a) Planner console for reviewing candidate reports and bounds.
 (b) Market dashboard for comparing allocation policies.
Figure 2: Demonstration interfaces in theSolarChainprototype.
Together, these strands motivate a decision chain in which phys-
ical evidence informs coordination, accepted supply enters a con-
figurable market, and settlement remains replayable.SolarChain
exposes how failures propagate across this chain.
3 Integrated System Design
3.1 Physical Evidence and Stateful Coordination
The off-chain engine combines a node’s area𝐴, efficiency𝜂, effective
irradiance𝐺, temperature coefficient𝛽, and reference temperature
𝑇𝑟𝑒 𝑓 to compute
𝑃max =𝐴𝜂𝐺[1−𝛽(𝑇−𝑇 𝑟𝑒 𝑓)].(1)
A report above𝜏𝑃 max is physically inconsistent. Reports inside this
envelope may still be flagged by temporal, neighbor, or residual-
memory rules. A persistent SolarAgent retains residual history, cal-
ibration, trust, and participation state; the PlannerAgent approves,
rejects, or escalates; and Factory and Market agents return demand
and slippage feedback. The resulting coordination is inspectable,
but it is neither a learned policy nor cryptographic proof of source
authenticity.
State evolves only through declared transitions. The SolarAgent
keeps the most recent 48 residuals, updates calibration after at least
six observations, and revises trust after planner and market feed-
back. Threshold rules map trust to active, probation, or suspended
participation. The PlannerAgent combines verifier outcome and
trust to approve, reject, or escalate a report rather than silently
overwriting it. This makes “evolutionary” testable as accumulated
state without claiming online learning.
All calculations use one-hour intervals:𝐸𝑡 =𝑃 𝑡 Δ𝑡 with Δ𝑡= 1 h.
Consequently, summed kW (MW) samples are reported as kWh
(MWh). Legacy implementation fields ending in W or MW, includ-
ing contract inputs, represent power-derived one-hour step values
rather than separately calibrated energy-meter readings.
3.2 Allocation, Settlement, and Replay
Accepted supply enters the market contract, where reward share𝜌
is configurable:
𝑅𝑟𝑒𝑤𝑎𝑟𝑑 =𝜌𝐸 𝑣𝑒𝑟𝑖 𝑓 𝑖𝑒𝑑, 𝑅 𝑙𝑖𝑞 =(1−𝜌)𝐸 𝑣𝑒𝑟𝑖 𝑓 𝑖𝑒𝑑.(2)
The owner-set default is 2,000 basis points (20/80 reward/liquidity),
an experimental policy parameter evaluated rather than assumed
optimal. Wallet-signed contracts register assets, update supply and
demand, burn SOLR for simulated factory purchases, and emit
settlement events.
The event bus serializes each report, verification result, planner
action, market update, feedback update, and settlement with the pre-
vious event hash. Replaying the chain reveals whether the recorded
path has changed. The frontend in Figure 2 presents this evidence
before registration or purchase; physical calculations remain off-
chain, and contracts record approved shared-state transitions.
This separation also exposes the trust boundary. Weather and
node metadata feed the model, the planner approves its evidence,
the contract enforces access and allocation bounds, and the ledger
preserves accepted transitions. A later layer cannot repair a com-
promised input, although the combined record allows an auditor to
identify the evidence used.
4 Controlled Prototype Evaluation
The evaluation examines three linked properties: detector accuracy
and failure modes, sensitivity to the reward–liquidity allocation,
and consistency from accepted reports through settlement and
replay.
4.1 Benchmark, Provenance, and Protocol
The canonical benchmark covers April 1–May 1, 2026: 50 simulated
PV nodes in five cities, 720 hourly observations per node, and 36,000
records in total. A fixed seed injects 1,800 labeled records into the
original monthly FDIA set. The broader taxonomy contains this
original category and ten additional scripted attack scenarios (11
categories in total); it does not model an adversary that observes
the detector and adapts to evade it.
We distinguish three provenance classes. Externally sourced in-
puts are city-level historical temperature and shortwave-radiation
series retrieved from Open-Meteo, not panel telemetry. Solar po-
sition, the clear-sky envelope, temperature correction, and 𝑃max
are physics-modeled. PV nodes and hardware parameters, reported
power, demand, trades, planner/agent behavior, and attacks are

UbiComp Companion ’26, October 11–15, 2026, Shanghai, China Ou et al.
synthetic. Dataset hashes, the weather cache, seed, scripts, and
software versions accompany the release.
All detectors receive the same ordered records and labels. Preci-
sion, recall, and F1 use attacks as the positive class; FAR denotes
the fraction of attacks accepted and FRR the fraction of normal
reports rejected. Runtime uses 30 warmed full-batch runs on the en-
vironment named in Table 2. Because the benchmark is fixed-seed
and deterministic, we report descriptive results rather than inferen-
tial significance. The taxonomy is a stress test, not a substitute for
naturally occurring fault or adversarial data.
4.2 Verifier Accuracy, Attack Classes, and Cost
Table 2 reports the monthly comparison. IQR/MAD achieves the
highest aggregate F1 (1.000); the adaptive verifier reaches 0.988 and
is therefore not uniformly superior. Its physics, temporal, neighbor,
and residual/trust rules provide inspectable evidence and replayable
state at the cost of higher runtime and occasional false positives.
Category results expose the boundary: nighttime, above-bound,
and neighbor-inconsistent attacks are strongly covered; sensor
drift, replay, and intermittent bursts are partially covered; and near-
bound fraud, weather spoofing, and coordinated near-bound attacks
remain failures. The released attack_taxonomy_results.csv re-
ports seven detectors across all 11 categories. The 24-hour result
(F1=1.000 on 60 obvious violations) is only a boundary-violation
sanity check.
IQR/MAD is preferable when aggregate classification on the in-
jected distribution is the sole objective. The adaptive verifier instead
supplies a physical residual, temporal context, and recorded state
transition at a median 52.159 ms per batch (1.449 𝜇s per record).
These explanations do not compensate for uncovered attack classes,
which require authenticated context or additional detection mecha-
nisms.
Separately, all 144,721 generated events reproduced their stored
hash linkage. This establishes trace integrity for that run, not source
truth or better detection.
4.3 Allocation Sensitivity
The reward share𝜌 is configurable, with liquidity receiving1−𝜌 .
The sweep evaluates 41 ratios in 2.5-percentage-point increments
across seven common scenarios. Each ratio passes through the same
demand-response and market-update path before averaging and
scoring. This controls the simulated scenarios but cannot identify
causal participant response because supply, demand, and behavior
are model-generated. Table 3 reports representative endpoints, the
selected neighborhood, and the 50/50 reference; the released CSV
contains every ratio. The default𝜌= 0.20is conditional on these
assumptions rather than a universal optimum.
Table 3: Allocation sensitivity averaged across the simulated
market scenarios. “Reward/liquidity” gives producer and
market shares; score is unitless.
Allocation
Fulfill
(ratio)
Reward
(kWh)
Slip.
(%)
Unmet
(MWh) Score
0/100 0.961 0 32.356 1.869 0.617
10/90 0.964 4,174 32.165 1.686 0.640
20/80 0.956 8,976 32.569 2.111 0.651
25/75 0.939 11,220 33.032 2.858 0.646
50/50 0.782 22,441 33.297 9.520 0.592
The score uses declared weights (0.50 fulfillment, 0.20 reward,
0.15 slippage, 0.10 unmet demand, and 0.05 drawdown). Different
weights or dynamics can select another ratio; the contract therefore
exposes a bounds-checked basis-point parameter.
4.4 End-to-End Spatial and Settlement Trace
The May 1, 2026 interface trace contains 1,200 node-hour records
and 60 deliberately obvious anomalies. Unlike the monthly detector
benchmark, it follows accepted reports through city aggregates,
allocation, purchases, and the event log.
Table 4: Simulated city-level generation in the 24-hour com-
panion trace.
City Capacity (kW) Verified (kWh) Peak (kW) Cap. factor
Beijing 84.58 427.72 63.34 21.07%
Chengdu 92.62 220.95 51.23 9.94%
Hangzhou 79.14 539.39 72.12 28.40%
Shanghai 84.12 554.34 76.32 27.46%
Shenzhen 72.77 285.73 46.26 16.36%
The five synthetic city clusters produce 2,028.13 kWh of ac-
cepted generation. Chengdu has the largest simulated capacity but
the lowest verified output, whereas Shanghai and Hangzhou have
smaller capacities and higher output. This difference follows city-
level weather and synthetic hardware; it is not a field comparison
of municipal PV fleets.
The market applies the 20/80 split after aggregating accepted
supply, so rejected records cannot directly create reward or liquidity
in this trace. Factory purchases consume simulated supply and
emit the settlements in Table 5; legacy 50/50 fields serve only as a
reference policy.
Table 5: Simulated P2P settlement outcomes in the 24-hour
companion trace.
City Trades Volume (MWh) SOLR burned Exergy (MJ)
Beijing 7 0.0994 96.74 10.84
Chengdu 8 0.0883 89.13 7.45
Hangzhou 6 0.0855 85.21 7.05
Shanghai 14 0.2161 219.75 23.26
Shenzhen 7 0.1159 118.93 11.02
Across 42 synthetic purchases, the trace records 0.6052 MWh,
609.77 SOLR-equivalent units burned, and 59.63 MJ in the model’s
exergy field. Volume sums per-purchase MW values over one-hour
steps. These values demonstrate software linkage, not real transac-
tions, emissions, or carbon abatement.

SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design UbiComp Companion ’26, October 11–15, 2026, Shanghai, China
Figure 3: Spatial benchmark illustration for one 24-hour slice across five Chinese cities. Markers locate the 50 simulated PV
nodes; the right panel summarizes the slice’s 1,200 records and 60 scripted anomalies. The canonical evaluation extends the
same pipeline to 36,000 April records.
Table 2: Verifier results on 36,000 monthly records with 1,800 original FDIA labels. FAR is false-acceptance rate and FRR is
false-rejection rate. Runtime columns report the median and p95 of 30 warmed batch runs on the released macOS/Apple-arm64
environment.
Detector Precision Recall F1 FAR FRR Median (ms) p95 (ms)𝜇s/record
3-sigma 1.000 0.766 0.868 0.234 0.000 6.378 7.605 0.177
IQR/MAD 1.000 1.0001.0000.000 0.000 7.859 9.195 0.218
Physics bound 1.000 0.862 0.926 0.138 0.000 0.132 0.205 0.004
Adaptive SolarAgent 0.976 1.000 0.988 0.000 0.001 52.159 53.769 1.449
Market-state comparison.Under common accepted generation,
demand, reserve, and slippage assumptions, Table 6 compares the
20/80 policy with a simulated 50/50 reference (not a no-split market).
More liquidity increases modeled depth and decreases the slippage
proxy while assigning 0.4056 MWh-equivalent value to rewards.
Table 6: Market-state metrics for the 24-hour companion
trace.
Metric 20/80 default 50/50 ref. Change
Average liquidity (MW) 0.0856 0.0503 +70.3%
Peak liquidity (MW) 0.2376 0.1453 +63.6%
Liquidity area (MW-hours) 2.0545 1.2061 +70.3%
Average slippage proxy 34.33% 57.18% -40.0%
Daylight slippage proxy 49.79% 82.15% -39.4%
These simulator outputs are neither exchange observations nor
welfare estimates; the slippage proxy responds mechanically to
synthetic demand and liquidity. Plausible attacks that evade verifi-
cation could still alter market state, so field validation must jointly
measure detection error and economic impact.
The trace checks that rejected generation is excluded, reward
and liquidity sum to the accepted one-hour value, and every event
names its preceding hash. Regenerated city and purchase totals
satisfy these invariants, while local-EVM tests cover registration,
access control, ratio bounds, token burning, and settlement fields.
Full replay reconstructs the recorded inputs and decisions but re-
mains a consistency test, not proof of contract security or source
authenticity.
5 Discussion and Limitations
5.1 Integrated Evidence
The controlled evidence shows that an EIoT-oriented prototype
can connect physical screening to coordinated settlement and re-
playable evidence. Enacted grounding rejects clearly impossible PV
reports; engaged roles propagate approval and demand into market
state; and evolutionary state retains residual, trust, calibration, and
participation history. The result is an inspectable decision chain,
not evidence that physics bounds, agents, contracts, or hash chains
are individually novel.
The evidence also exposes a clear boundary. Physical plausi-
bility is not authenticity: near-bound manipulation, coordinated
reports, or spoofed weather can remain inside the rules. The adap-
tive verifier is therefore a reason-producing planner checkpoint,
not a uniformly better detector; IQR/MAD has stronger aggregate
F1 in the monthly benchmark. These results favor a layered compar-
ison rather than a single winner. IQR/MAD can screen batch-level
deviations, whereas the adaptive agent preserves residuals and
state changes that explain a planner decision. Their outputs should
remain distinct because agreement among rules derived from the
same modeled envelope is not independent corroboration. Likewise,
the 20/80 default is the highest-scoring point under this simulator’s
demand, participation, normalization, and declared weights, not a
general welfare optimum.
A detector can classify well without supplying physical evidence
for a settlement dispute; a market setting can improve a simulated
score while relying on unverified supply; and perfect replay can

UbiComp Companion ’26, October 11–15, 2026, Shanghai, China Ou et al.
preserve a false input. Linking the stages makes these dependencies
visible and traces downstream effects to their assumptions. This dis-
tinction also changes what should be measured. Detection metrics
quantify classification, whereas planner escalations, decision rever-
sals, and excluded settlements quantify operational consequences.
Reporting both avoids treating an explanatory trace as an accuracy
gain or a high F1 score as sufficient market protection, and it allows
each error to be followed into the allocation and settlement records
it affects.
5.2 Market, Audit, and Governance Implications
A larger reward share strengthens direct producer incentives but
removes value from shared liquidity; a larger liquidity share can
support fulfillment while weakening individual reward. Exposing
the split in basis points permits a deployment study to substitute
observed behavior and an explicit governance process. Selecting
𝜌 should therefore be treated as a governance decision with pub-
lished score weights, scenario ranges, and update intervals. A pilot
should report the full trade-off among producer reward, fulfilled de-
mand, unmet demand, slippage, and drawdown rather than only the
highest composite score. Formal market and participant-response
analysis would still be required before interpreting any selected
ratio as policy.
The hash-linked log supplies a different kind of evidence from
detector accuracy: it connects report, rule outputs, planner action,
market update, and settlement so an auditor can reproduce a state
change. It cannot prove sensor calibration, asset control, or envi-
ronmental additionality. This distinction matters because digital
incentives can become detached from physical activity [2], while
renewable accounting still faces identity and double-counting risks
[8]. The off-chain process and planner remain trusted, and the con-
tract owner can change the reward ratio; the prototype records
these actions but implements neither decentralized oracle consen-
sus nor stakeholder voting and dispute resolution.
Operational governance would therefore need accountable roles
for meter attestation, model maintenance, approval and appeal,
and allocation-policy control. Concentrating them in one operator
preserves replayability but not institutional independence; decen-
tralizing them without assigning responsibility may make failures
harder to resolve. At minimum, model and ratio changes should
have separate permissions and versioned justifications, while an
appeal record should retain the parameters active when a report
was judged. The prototype exposes these decisions but does not
select a governance model.
5.3 Threats to Validity and Validation Agenda
Construct validity is limited by modeled rather than metered gener-
ation and by a slippage proxy rather than observed prices. Internal
validity is constrained by synthetic hardware, demand, trades, agent
behavior, and fixed-seed attacks. External validity is limited by one
month of city-level weather and the absence of communication loss,
clock drift, shading, clipping, outages, strategic bidding, privacy
costs, chain congestion, and adaptive adversaries. Hash replay es-
tablishes event integrity but cannot authenticate an input at origin.
The perfect IQR/MAD result is distribution-specific: scripted
anomalies can be unusually separable, and synthetic labels contain
no field-data uncertainty. The adaptive verifier also depends on
observation order and early feedback, so attack timing and cold-
start behavior may change its result. Field labels should distinguish
manipulation from shading, sensor drift, outages, and data loss;
otherwise a single F1 score conflates adversarial behavior with
operational faults. Category-level reporting reduces but does not
remove these threats.
The release mitigates reproducibility concerns by recording the
April window, seed, cached weather, file hashes, detector settings,
scripts, and software versions. Runtime results also include the
input hash and machine environment. Repeating the benchmark
therefore does not require a live weather API, although it reproduces
only the stated controlled conditions. An independent replication
should reconstruct weather-derived bounds from the cache, repro-
duce event hashes, and compare regenerated metric tables with the
released CSVs. Any divergence could then be localized to source
data, software environment, or policy parameters.
Validation should next replay synchronized inverter and smart-
meter traces through the same interface, then progress to shadow
operation and a governed microgrid pilot. It should test seasonal
faults, missing data, adaptive attacks, end-to-end latency, privacy
and communication overhead, and the economic consequences of
false acceptance and rejection. Chronological evaluation should
separate cold-start from steady-state periods and propagate each
false decision through settlement to quantify downstream value
at risk. A field protocol must also define meter calibration, ratio
governance, appeal procedures, and behavior during unavailable
weather or network data before any claim of deployment readiness.
6 Conclusion
This study asked whether a controlled EIoT prototype could carry
physics-bounded PV reports through coordinated settlement while
retaining traceable evidence.SolarChainimplements this path, but
the results set clear limits. IQR/MAD achieved the best aggregate
F1, while the interpretable adaptive verifier retained attack-class
failures. The 20/80 allocation remained assumption-dependent, and
hash replay established trace consistency rather than source au-
thenticity.
SolarChaintherefore serves as an experimental testbed for trac-
ing how verification errors and allocation choices affect digital
incentives. Field claims require synchronized telemetry, adaptive-
attack evaluation, and governed trials.
Acknowledgments
Ming-Chun Huang and Luyao Zhang received research support
from the Duke Kunshan University Education Development Foun-
dation and the Kunshan Municipal Government. Shilin Ou was
additionally supported by the Summer Research Scholar Program
at Duke Kunshan University under the mentorship of Luyao Zhang.
References
[1] Juhar Abdella and Khaled Shuaib. 2018. Peer to peer distributed energy trading
in smart grids: A survey.Energies11, 6 (2018), 1560. doi:10.3390/en11061560
[2] Muneer Maher Alshater. 2026. Decentralized physical infrastructure networks
(DePIN) tokenomics.Frontiers in Blockchain8 (2026), 1644115. doi:10.3389/fbloc.
2025.1644115

SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design UbiComp Companion ’26, October 11–15, 2026, Shanghai, China
[3] Kevin S Anderson, Clifford W Hansen, William F Holmgren, Adam R Jensen,
Mark A Mikofski, and Anton Driesse. 2023. pvlib python: 2023 project update.
Journal of Open Source Software8, 92 (2023), 5994. doi:10.21105/joss.05994
[4] Guillermo Angeris and Tarun Chitra. 2020. Improved price oracles: Constant
function market makers. InProceedings of the 2nd ACM Conference on Advances
in Financial Technologies. 80–91. doi:10.1145/3419614.3423251
[5] Alain Aoun, Mehdi Adda, Adrian Ilinca, Mazen Ghandour, and Hussein Ibrahim.
2024. Centralized vs. decentralized electric grid resilience analysis using Leon-
tief’s input–output model.Energies17, 6 (2024), 1321. doi:10.3390/en17061321
[6] Mark C. Ballandies, Hongyang Wang, Andrew Chung Chee Law, Joshua C. Yang,
Christophe Gösken, and Michael Andrew. 2023. A taxonomy for blockchain-
based decentralized physical infrastructure networks (DePIN).arXiv preprint
arXiv:2309.16707(2023). doi:10.48550/arXiv.2309.16707
[7] Jiahong Dai, Jiawei Yang, Yu Wang, and Yan Xu. 2024. Blockchain-enabled cyber-
resilience enhancement framework of microgrid distributed secondary control
against false data injection attacks.IEEE Transactions on Smart Grid15, 2 (2024),
2226–2236. doi:10.1109/TSG.2023.3328383
[8] Md Sadek Ferdous, Umit Cali, Ugur Halden, and Wolfgang Prinz. 2023. Leveraging
self-sovereign identity and distributed ledger technology in renewable energy
certificate ecosystems.Journal of Cleaner Production422 (2023), 138355. doi:10.
1016/j.jclepro.2023.138355
[9] William F. Holmgren, Clifford W. Hansen, and Mark A. Mikofski. 2018. pvlib
python: a python package for modeling solar energy systems.Journal of Open
Source Software3, 29 (2018), 884. doi:10.21105/joss.00884
[10] Chung-Ting Huang and Ian J. Scott. 2024. Peer-to-peer multi-period energy mar-
ket with flexible scheduling on a scalable and cost-effective blockchain.Applied
Energy367 (2024), 123331. doi:10.1016/j.apenergy.2024.123331
[11] Zipeng Liang, Xin Yin, Chi Yung Chung, Safwat Khair Rayeem, Xinquan
Chen, and Haosen Yang. 2025. Managing massive RES integration in hybrid
microgrids: A data-driven quad-level approach with adjustable conservative-
ness.IEEE Transactions on Industrial Informatics21, 10 (2025), 7698–7709.
doi:10.1109/TII.2025.3575133
[12] Zhibin Lin, Taotao Wang, Long Shi, Shengli Zhang, and Bin Cao. 2024. Decen-
tralized physical infrastructure network (DePIN): Challenges and opportunities.
arXiv preprint arXiv:2406.02239(2024). doi:10.48550/arXiv.2406.02239
[13] Yao Liu, Peng Ning, and Michael K Reiter. 2011. False data injection attacks
against state estimation in electric power grids.ACM Transactions on Information
and System Security (TISSEC)14, 1 (2011), 1–33. doi:10.1145/1952982.1952995
[14] Yunhao Liu, Xu Wang, Yunhuai Liu, Kebin Liu, Shuai Tong, Jinliang Yuan, and Li
Liu. 2026. EIoT: Embodied Intelligence of Things.Tsinghua Science and Technology
31, 1 (2026), 1–15. doi:10.26599/TST.2025.9010127
[15] Sara Mohammadi, Frank Eliassen, Yan Zhang, and Hans-Arno Jacobsen. 2022.
Detecting false data injection attacks in peer to peer energy trading using machine
learning.IEEE Transactions on Dependable and Secure Computing19, 5 (2022),
3417–3431. doi:10.1109/TDSC.2021.3096213
[16] Muhammad Baqer Mollah, Jun Zhao, Dusit Niyato, Kwok-Yan Lam, Xin Zhang,
Amer M. Y. M. Ghias, Leong Hai Koh, and Lei Yang. 2021. Blockchain for future
smart grid: A comprehensive survey.IEEE Internet of Things Journal8, 1 (2021),
18–43. doi:10.1109/JIOT.2020.2993601
[17] Thomas Morstyn, Niall Farrell, Sarah J Darby, and Malcolm D McCulloch. 2018.
Using peer-to-peer energy-trading platforms to incentivize prosumers to form
federated power plants.Nature Energy3, 2 (2018), 94–101. doi:10.1038/s41560-
017-0075-y
[18] Ahmed S Musleh, Guo Chen, Zhao Yang Dong, Chen Wang, and Shiping Chen.
2023. Spatio-temporal data-driven detection of false data injection attacks in
power distribution systems.International Journal of Electrical Power & Energy
Systems145 (2023), 108612. doi:10.1016/j.ijepes.2022.108612
[19] Imtiaz Parvez and Aditya Sundararajan. 2025. A Graph-Net with Node Embed-
dings to Detect False Data Injection Attacks in Photovoltaic Systems. In2025 IEEE
International Conference on Electro Information Technology (eIT). IEEE, 085–090.
doi:10.1109/eIT64391.2025.11103667
[20] Maziar Raissi, Paris Perdikaris, and George E Karniadakis. 2019. Physics-informed
neural networks: A deep learning framework for solving forward and inverse
problems involving nonlinear partial differential equations.Journal of Computa-
tional physics378 (2019), 686–707. doi:10.1016/j.jcp.2018.10.045
[21] Amin Zakhirehkar Sahih, Alireza Abbasi, and Milad Ghasri. 2024. Blockchain-
enabled solutions for fair and efficient peer-to-peer renewable energy trading:
An experimental comparison.Journal of Cleaner Production455 (2024), 142301.
doi:10.1016/j.jclepro.2024.142301
[22] Elisa Skoplaki and John A Palyvos. 2009. On the temperature dependence of
photovoltaic module electrical performance: A review of efficiency/power corre-
lations.Solar energy83, 5 (2009), 614–624. doi:10.1016/j.solener.2008.10.008
[23] Johann Westphall and Jean Everson Martina. 2022. Blockchain privacy and
scalability in a decentralized validated energy trading context with hyperledger
fabric.Sensors22, 12 (2022), 4585. doi:10.3390/s22124585
[24] Youquan Xian, Lianghaojie Zhou, Jianyong Jiang, Boyi Wang, Hao Huo, and
Peng Liu. 2024. A distributed efficient blockchain oracle scheme for internet
of things.IEICE Transactions on CommunicationsE107-B, 9 (2024), 573–582.
doi:10.23919/transcom.2023EBP3156
[25] Yu Zheng, Licia Capra, Ouri Wolfson, and Hai Yang. 2014. Urban computing:
concepts, methodologies, and applications.ACM Transactions on Intelligent
Systems and Technology5, 3 (2014), 1–55. doi:10.1145/2629592
Appendix
A Benchmark and Verifier Specification
This appendix specifies the controlled benchmark and its evaluation
artifacts.
Table 7: Canonical benchmark specification.
Item Specification
Window 2026-04-01 to 2026-05-01; 720 hourly steps
(Asia/Shanghai).
Scale Five cities; 50 simulated nodes; 36,000 node-hours.
Labels 1,800 original FDIA rows (5%).
Seeds Dataset20260511; taxonomy20260617.
Sourced Open-Meteo city temperature and shortwave radiation.
Modeled Solar position, clear-sky envelope, temperature correc-
tion,𝑃 max.
Synthetic Nodes, reports, labels, demand, trades, agents, and at-
tacks.
SHA-256caa0d95656e618e7d54c98bfed507128a
94edac454b8b964ac06f3541f9b190e.
Table 8: Released benchmark artifacts.
Artifact Rows Role
Nodes 50 Registry and PV parameters.
Generation 36,000 Bounds, reports, and labels.
Market 720 Demand, allocation, and slippage.
Trades 1,185 Simulated energy trades.
Event log 144,721 Ordered agent and settlement events.
Files:urban_energy_nodes.csv.
market_liquidity.csv;p2p_trades.csv.
spatiotemporal_generation.csv.
eiot_event_log.csv.gz.
For the offline verifier, let 𝑑𝑖,𝑡 =max(𝑃 max 𝑖,𝑡 , 1),𝑟𝑖,𝑡 =(𝑃 rep 𝑖,𝑡 −
0.978𝑃 max 𝑖,𝑡 )/𝑑𝑖,𝑡 , and𝑞 𝑖,𝑡 =𝑃 rep 𝑖,𝑡/𝑑𝑖,𝑡 . Its physical flag is
𝐵𝑖,𝑡 =[𝑃 rep 𝑖,𝑡 >1.03𝑃 max 𝑖,𝑡 +25]∨[𝑃 max 𝑖,𝑡 ≤1∧𝑃 rep 𝑖,𝑡 >50].(3)
The temporal rule𝑇 compares𝑟𝑖,𝑡 with up to 12 prior node residu-
als (minimum four; difference > 0.24). In daylight, neighbor rule
𝑁 flags𝑞𝑖,𝑡 more than 0.32 from the simultaneous city median.
Memory rule𝑀 uses 24 prior steps (minimum eight, non-daylight
residuals zeroed): positive mean > 0.035with 𝑟> 0.030; negative
mean <− 0.075with 𝑟<− 0.060; or mean|𝑟|> 0.10with current
|𝑟|>0.090. The composite is
𝐶𝑖,𝑡 =𝐵 𝑖,𝑡∨𝑀 𝑖,𝑡∨(𝑇 𝑖,𝑡∧𝑁 𝑖,𝑡)∨(|𝑟 𝑖,𝑡|>0.20∧𝑁 𝑖,𝑡).(4)
This batch classifier produces Appendix B’s metrics. The stateful
SolarAgent/PlannerAgent trace instead updates trust, calibration,
participation, and market decisions; the two share physical evidence
but are not the same evaluation object.

UbiComp Companion ’26, October 11–15, 2026, Shanghai, China Ou et al.
B Attack-Class Capability and Threshold
Sensitivity
Table 9 reports all eleven scripted classes. Labels mean strong (S),
partial (P), or outside the current claim (O), and do not guarantee
resistance to adaptive attacks.
Table 9: Offline verifier results by attack class. Capability:
S=strong, P=partial, O=outside current claim.
Attack Rows P R F1 Cap.
Original FDIA 1,800 .976 1.000 .988 S
Night impossible 1,440 1.000 1.000 1.000 S
Above bound 1,800 .960 .984 .972 S
Near bound 1,800 .000 .000 .000 O
Within-bound fraud 1,800 .000 .000 .000 O
Sensor drift 3,068 .999 .864 .927 P
Weather spoofing 1,800 .000 .000 .000 O
Replay 2,160 .992 .654 .788 P
Neighbor incons. 1,800 1.000 1.000 1.000 S
Coordinated near bound 1,945 .000 .000 .000 O
Intermittent burst 436 .990 .897 .941 P
Strong coverage is obtained for original FDIA, nighttime, above-
bound, and neighbor-inconsistent attacks. Drift, replay, and in-
termittent bursts are partial; near-bound, within-bound, weather-
spoofing, and coordinated near-bound attacks remain outside the
defense claim.
Table 10: Physics-tolerance sensitivity;𝜏= 1.03is the imple-
mented point, not a global optimum.
𝜏Mac. P Mac. R Mac. F1 FRR Near R Above R
1.000 .643 .574 .586 .008 .572 .956
1.005 .713 .548 .592 .003 .420 .955
1.030 .545 .443 .479 .000 .000 .954
1.080 .545 .426 .466 .000 .000 .945
Raising𝜏 removes normal false rejections but sacrifices near-
bound recall; above-bound recall is comparatively stable. All points
reuse the same fixed-seed records and scripted attacks.
C Allocation Robustness and Audit Evidence
The 41-point ratio sweep uses 0.025 increments and seven per-
turbations: low, normal, and high demand (0 .5/1.0/1.5); cloudy
generation (0.6); 10% and 20% FDIA loss (0.9/0.8accepted supply);
and high volatility (1+0.25 sin(0.31𝑡)demand).
Within each scenario, 𝑆= 0.50𝐹+ 0.20𝑅+ 0.15𝐿+ 0.10𝑈+
0.05𝐷, with adverse terms reverse-scaled; the robust score is0.75𝑆+
0.25 min(𝑆) . Feasibility requires average fulfillment≥ 0.90, worst
fulfillment≥ 0.80, average slippage≤ 40%, and average producer
reward≥5,000kWh.
Table 11: Selected 20/80 result across seven scenarios.
Metric Value
Robust score .628
Average/worst scenario score .651/.556
Average/worst fulfillment .956/.836
Average reward; slippage 8,976 kWh; 32.569%
Average unmet demand 2.111 MWh
The feasible reward-share interval is 12.5%–22.5%; 20% has the
highest robust score within that set but remains conditional on the
simulator, normalization, scenarios, and weights.
Table 12: End-to-end audit evidence and its boundary.
Layer Evidence Boundary
Inspect Weather, registry Modeled input, not panel
telemetry.
Verify Report, result Replays decisions, not sen-
sor truth.
Coordinate Planner, feedback Ordered state, not policy
optimality.
Allocate Market, ratio sweep Declared scenarios and
weights.
Settle Settlement; 5/5 EVM Consistency, not a secu-
rity audit.
To verify the audit trail, the replay procedure canonicalized each
JSON payload, blanked its record_hash field, recomputed the SHA-
256 digest, and checked the resulting predecessor link. All 144,721
events across six event types passed this verification. The local EVM
suite then evaluated the allocation workflow under five cases, cov-
ering the 20/80 initialization, authorized and unauthorized updates,
enforcement of the 10,000-basis-point bound, and settlement after
a ratio change. These results support the internal consistency and
replayability of the implementation, but they do not validate sensor
inputs, establish economic optimality, or constitute a security audit
of the contract. Reproduction begins by identifying the benchmark
through its provenance record and generation digest. The released
capability, tolerance, and ratio files can then be evaluated before
replaying the event log and running the EVM tests. Values reported
in the paper are rounded for readability, whereas all verification
procedures use the unrounded records.
D User Experience Workflow
SolarChainis designed as a human-in-the-loop energy planning
workflow. The user experience begins from a map-centered dash-
board and then moves through verification, registration, settlement,
and audit. Each stage exposes both the user action and the evidence
produced by the system, so that planners can trace how a PV record
becomes an on-chain market state.
Step 1: Wallet and city-state initialization.The planner, PV
owner, or factory owner first connects a Web3 wallet. After the
signature identity is available, the frontend loads the deployed con-
tract addresses, ABIs, city layers, PV nodes, factory nodes, and local

SolarChain: A Physics-Grounded Embodied IoT System for Verifiable Urban Solar Market Design UbiComp Companion ’26, October 11–15, 2026, Shanghai, China
dashboard state. This step binds later approvals and transactions to
a cryptographic account.
Step 2: Spatial inspection of candidate assets.The planner
opens the map workspace and inspects distributed energy resources
across the demonstration cities. For each candidate PV node, the
interface shows location, panel specifications, battery tempera-
ture, DC power, AC power, and predicted generation. This spatial
view is important becauseSolarChaintreats energy generation as a
location-dependent urban process rather than as a generic token
balance.
Step 3: Physics-bounded verification.Before a PV record is
allowed to affect the market, the planner reviews the off-chain
verification evidence. The physics engine combines geospatial coor-
dinates, irradiance, temperature, panel area, efficiency, and tempera-
ture coefficient to compute𝑃max. If the reported generation satisfies
𝑃reported≤𝜏𝑃 max, the record is marked verified; otherwise it is
labeled rejected. This step blocks FDIA records before they can
create false market supply or invalid token rewards.
Step 4: PV digital-twin registration.After a panel passes veri-
fication, the PV owner submits the asset to the chain. The panel-
registration function records the owner address, location, battery
temperature, DC power, AC power, and creation timestamp. The
resulting panel event provides an audit trail from the planner-
approved physical record to the on-chain digital twin. The con-
firmation view in Figure 4 is the final human checkpoint before
the wallet signature: the user verifies the selected location and
predicted outputs instead of signing a transaction from an abstract
contract call alone.
Figure 4: Solar panel confirmation. User verifies the selected
location and predicted outputs before submitting a Web3
wallet signature.
Step 5: Hourly market-state update.At each simulation step,
verified generation is aggregated together with factory demand.
The market operator calls the market-update function, which ap-
pliesSolarChain’s forced distribution rule: 80% of verified value is
added to global market liquidity, while 20% is assigned to personal
producer rewards. This prevents the marketplace from depending
only on voluntary liquidity provision.
Step 6: Reward preview and claiming.PV owners can preview
their pending reward balance before claiming. If the cooldown
interval has passed, the reward contract transfers SOLR to the
owner and updates the last-claim timestamp. This gives owners
a visible maintenance incentive while preventing repeated claims
within the same simulator interval.
Step 7: Factory registration and energy purchase.Factory users
register demand nodes with location and power-consumption meta-
data. When buying verified energy, the factory owner approves
SOLR spending and calls the purchase function. The exchange burns
the corresponding SOLR, decreases global supply, increases the fac-
tory energy balance, and emits an EnergyPurchased event. This
ties digital token deflation to energy consumption. Figure 5 shows
the purchase interface where the user selects a factory, previews
the energy amount, and prepares the SOLR burn transaction before
wallet approval.
Figure 5: Energy exchange interface. The user selects a fac-
tory, previews the energy amount, and prepares the SOLR
burn transaction.
Step 8: P2P panel marketplace.SolarChainalso supports sec-
ondary ownership transfer. A PV owner can list a panel in Shop;
buyers place offers after approving token spending; the seller ap-
proves one buyer. The shop transfers SOLR from buyer to seller and
calls the panel ownership-transfer function, so the asset registry
and payment record remain synchronized.
Step 9: Planner audit and analytics.Finally, planners review
charts for verified generation, rejected anomalies, market liquidity,
baseline slippage, token burn, and exergy dissipation. Then dash-
board therefore connects meteorological input, physical verifica-
tion, contract events, and economic settlement into one inspectable
evidence chain.
E Dataset Data Dictionary
The released datasets form a linked physical-to-digital benchmark.
The node registry defines each PV asset’s location and hardware
parameters; the hourly generation file expands those nodes into
weather-bounded verification records with FDIA labels. The market-
liquidity file aggregates verified generation into liquidity and slip-
page variables. Additionally, the P2P trade file records factory pur-
chases, SOLR burn, and exergy dissipation. All timestamps use ISO
8601 format in the Asia/Shanghai timezone. To provide a compre-
hensive overview, Table 13 presents the complete data dictionary,
detailing the specific role of each dataset alongside its variable units,
numerical ranges or categorical domains, temporal frequencies, and
sample observations.

UbiComp Companion ’26, October 11–15, 2026, Shanghai, China Ou et al.
Table 13: Detailed data dictionary for releasedSolarChaindatasets.
Dataset Dataset role Variables: unit; range/domain; frequency; sample observations
urban_energy_nodes Static PV asset registry. This file defines
the physical nodes that later appear in the
generation and verification records. It is
used to reproduce geospatial placement,
panel capacity, efficiency assumptions, and
temperature response.
node_id: id; 50 unique nodes; static node-level;BEI-001. city: name; Beijing/Shanghai/Chengdu/Shenzhen/Hangzhou; static;
Beijing. latitude: deg.; 22.465945–39.982854; static; 39.887642. longitude: deg.; 104.022990–121.522048; static; 116.380950.
panel_area_m2: m2; 18.43–63.57; static; 43.39. efficiency: ratio; 0.1768–0.2234; static; 0.2055. temp_coefficient: per◦C;
-0.00460 to -0.00326; static; -0.00379.install_date: date; 2020-01-09–2024-05-10; static; 2022-03-29.
spatiotemporal_generation Hourly physics-verification dataset. This
file is the main FDIA benchmark: each
row pairs weather input and panel loca-
tion with 𝑃max, reported power, anomaly
status, and the final verification decision.
timestamp: time; 2026-05-01 hourly; node-hour;2026-05-01T00:00:00+08:00. hour: hour; 0–23; node-hour; 0.node_id: id;
50 nodes; node-hour;BEI-001. city: name; five cities; node-hour; Beijing.latitude/longitude: deg.; node coordinate ranges
above; repeated node-hour; 39.887642/116.380950. irradiance_Wm2: W/m2; 0.00–929.00; node-hour; 15.00. air_temp_C:
◦C; 9.10–27.00; node-hour; 20.00. P_max_W: W; 0.00–12325.98; node-hour; 138.51. P_reported_W: W; 0.00–13700.91; node-
hour; 963.02. fdia_detected: bool; True/False, 60 injected FDIA rows; node-hour; False. verification_status: label;
verified/rejected; node-hour; verified.
market_liquidity Hourly market-state dataset. This file eval-
uates whether verified generation im-
proves market depth by comparingSolar-
Chainliquidity against a no-split baseline
and reporting the corresponding slippage.
timestamp: time; 24 hourly records; market-hour; 2026-05-01T00:00:00+08:00. hour: hour; 0–23; market-
hour; 0. total_verified_MW: MW; 0.000000–0.274561; market-hour; 0.004729. SolarChain _liquidity_MW : MW;
0.018000–0.270596; market-hour; 0.022350. baseline_liquidity_MW: MW; 0.008000–0.175482; market-hour; 0.010885.
slippage_SolarChain _pct : percent; 0.5703–2.8571; market-hour; 2.6726. slippage_baseline_pct: percent; 1.5235–
8.6111; market-hour; 7.9723.
p2p_trades Event-level settlement dataset. This file
records simulated factory purchases dur-
ing daylight hours and links each trade
to energy volume, SOLR burn, and exergy
dissipation for carbon-accounting analy-
sis.
trade_id: id; 42 unique trades; event-level; TRD-0001. timestamp: time; 06:00–19:00 daylight records; event;
2026-05-01T06:00:00+08:00. hour: hour; 6–19; event; 6. factory_id: id; six factories; event; FAC-BJ-01. city: name;
five cities; event; Beijing. energy_purchased_MW: MW; 0.000326–0.037502; event; 0.000970. tokens_burned: SOLR; 0.3164–
38.8174; event; 0.9507.exergy_dissipated_MJ: MJ; 0.0321–4.5783; event; 0.1199.
F Smart Contracts inSolarChain
The on-chain layer uses a modular design.SolarChainkeeps the
physics model off-chain. An off-chain engine verifies energy gener-
ation records, while smart contracts manage state transitions that
require public auditing. These transitions include token issuance,
asset registration, market allocation, and asset transfers. This de-
sign separates expensive physical computations from transparent
market settlements.
Table 14: Smart contracts inSolarChain
Contract Name Object Main Function
SolarToken SOLR token Token minting, transfer, approval, and burning
SolarPanels PV asset Panel registration, query, and ownership transfer
FactoryRegistry Demand node Factory registration and demand recording
EnergyExchange Energy market Supply update, demand tracking, rewards, and purchase
PowerReward Reward pool Power-based reward preview and claiming
Shop Asset market Panel listing, offer, sale approval, and transfer
Table 14 summarizes the six core contracts. How do they work
together to connect physical data with digital records? As shown
in Code box 2, the panel and factory contracts form the registry
layer. They do not handle energy trading directly. Instead, they
assign stable identities to supply-side solar panels and demand-side
factories. This is important because urban energy generation and
consumption vary by location. The registry ensures every market
event traces back to a specific owner and physical location.
SolarToken and EnergyExchange form the settlement layer. In
our system, the SOLR token is an accounting tool, not a speculative
asset. Code box 1 outlines its logic, which manages token issuance
and verifiable burns. The exchange contract receives verified energy
data from the off-chain engine. Code box 3 demonstrates how the
system divides this energy into two parts: market liquidity and
owner rewards. When a factory buys energy, it does not simply pay
another user. Instead, the contract burns the spent SOLR tokens.
This reduces the global token supply and increases the factory’s
energy balance. This mechanism directly connects digital token
deflation to physical energy consumption.
Finally, the reward and shop contracts encourage long-term
participation. The reward contract distributes tokens based on panel
capacity. It uses a cooldown timer to prevent multiple claims in the
same simulation step. The shop contract manages the secondary
market for solar panels. It verifies ownership, handles payments,
and updates the registry (Code box 2). Together, these contracts tie
economic incentives to physical infrastructure rather than short-
term token trading.
Code box 1: token issuance and burn.
mint(to, amount): require supply + amount <= cap;
_mint(to, amount).
burn(amount): _burn(msg.sender, amount).
burnFrom(account, amount): spend allowance;
_burn(account, amount).
Code box 2: registry and ownership evidence.
createPanel(lat, lon, temp, dcPower, acPower):
panelCount++; save owner, location, power.
createFactory(lat, lon, powerConsumption):
factoryCount++; save owner, location, demand.
approveSale(itemId, buyer): transfer SOLR;
transferPanelOwnership(panelId, buyer).
Code box 3: forced liquidity, rewards, and consumption burn.
updateMarketStep(users, userEnergy, totalEnergy, demand):
reward = userEnergy[i] * 20 / 100;
personalRewardWei[user] += reward * 1e18 / 100000;
globalSupplyEnergy += totalEnergy * 80 / 100;
totalDemandEnergy = demand.
buyEnergyForFactory(factoryId, energyAmount):
require supply >= energyAmount;
costWei = energyAmount * 1e18 / 100000;
burnFrom(msg.sender, costWei);
supply -= energyAmount; factory balance += energy.
