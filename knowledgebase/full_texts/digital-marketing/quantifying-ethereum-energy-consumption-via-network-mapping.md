---
title: Quantifying Ethereum Energy Consumption via Network Mapping
url: https://arxiv.org/abs/2610.03440
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yahn Costa Hackspacher
- Cornelius Ihle
- Vasundhara Shaw
- Dennis Trautwein
- Geerd-Dietger Hoffmann
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.03440
pages: 12
chars: 62276
fetched_at: '2026-11-08T13:22:03+00:00'
kb_version: 1
---

# Quantifying Ethereum Energy Consumption via Network Mapping

Quantifying Ethereum Energy Consumption via Network
Mapping
A Node-Level Estimate from Crawlable Attributes
Yahn Costa Hackspacher
FIZ Karlsruhe – Leibniz Institute for
Information Infrastructure
Karlsruhe, Germany
Yahn.Costa-Hackspacher@fiz-
Karlsruhe.de
Cornelius Ihle
University of Göttingen
Göttingen, Germany
ihle@gipplab.org
Vasundhara Shaw
FIZ Karlsruhe – Leibniz Institute for
Information Infrastructure
Karlsruhe, Germany
Vasundhar.Shaw@fiz-karlsruhe.de
Dennis Trautwein
ProbeLab Analytics OÜ
Talinn, Estonia
dennis@probelab.io
Geerd-Dietger Hoffmann
Department of Computer Science
University of Potsdam
Potsdam, Germany
didi@green-coding.io
Bela Gipp
University of Göttingen
Göttingen, Germany
gipp@uni-goettingen.de
Moritz Schubotz
FIZ Karlsruhe – Leibniz Institute for
Information Infrastructure
Karlsruhe, Germany
moritz.schubotz@fiz-karlsruhe.de
Abstract
Ethereum’s electricity use fell by about 99.95% after the network
moved from proof of work to proof of stake. Service providers still
need to report how much energy their operations use, e.g. under
the EU Markets in Crypto-Assets Regulation (MiCAR). Existing es-
timates either apply one typical wattage to every node or start from
aggregated monitoring counts. Both approaches ignore information
that nodes already advertise on the peer-to-peer network: which
client software they run, whether they use ARM or x86 hardware,
where they are hosted, and whether they act as validators.
We combine crawls of the consensus and execution layers, as-
sign a wattage to each peer from those attributes using published
measurements, and estimate the remaining incomplete peers with
a Random Forest. On 6,934 peers from two Nebula crawls (19 and
22 June 2026), the nodes that the crawler can reach sum to 415 kW,
or 3.63 GWh if that draw were held for a year. Applying the same
Lighthouse+Nethermind x86 wattage to every one of those peers
instead yields 431 kW. Using the observed attributes therefore low-
ers the total by 3.9%, mainly because nodes at Hetzner and other
non-AWS clouds draw less than that home-desktop figure. AWS
then accounts for 15.6% of watts from 12.2% of peers, and validator-
flagged nodes account for 31.4% of watts from 25.7% of peers.
Our snapshot of 415 kW is about 46% of the Cambridge Centre
for Alternative Finance (CCAF) estimate of about 0.90 MW. Both
approaches use about 60 W per node, so the gap is mostly how many
nodes each estimate includes. The assignment rules cover 3,110
peers and the forest estimates the other 3,824. On held-out labeled
peers with client, architecture, and OS hidden, the forest’s mean
absolute error against the rule wattage is 4.3 W. Twenty-four-hour
measurements on a gaming desktop differ from the predictions.
After subtracting a 33 W idle graphics card that Ethereum clients
do not need, both differences fall to about 19%.
CCS Concepts
•Networks→ Network measurement;•Computer systems
organization→ Peer-to-peer architectures;•Hardware → Power
and energy.
Keywords
Ethereum, proof of stake, energy estimation, network crawling,
Random Forest, MiCAR
1 Introduction
Ethereum’s Merge in September 2022 replaced proof of work (PoW),
long criticised for its energy use [ 67], with proof of stake (PoS)
and cut network electricity use by about 99.95% [ 30]. Pre-Merge
annualised estimates reached about 94 TWh [ 11, 24]. After the
Merge, security comes from staked ETH and the remaining energy
cost is the wall power of machines that run consensus-layer (CL)
and execution-layer (EL) clients. The Cambridge Centre for Alter-
native Finance (CCAF) places current demand near 0.90 MW, or
7.87 GWh/year [11].
Dialable nodes run different client pairs on ARM boards [20] and
on high-memory cloud instances. Regulation (EU) 2023/1114 on
Markets in Crypto-Assets (MiCAR) requires energy information in
white papers (Articles 6(1), 19(1), 51(1)) and updated figures from
service providers (Article 66(5)) [39]. The delegated sustainability
standards make annual energy, in kilowatt-hours, the mandatory
indicator. Greenhouse-gas and renewable-share fields apply only
1
arXiv:2610.03440v1  [cs.CY]  2 Oct 2026

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
once that energy exceeds 500,000 kWh/year, and claiming renew-
able electricity or offsets does not reduce the energy figure itself
[38].
Existing post-Merge models either apply one weighted wattage
to every participant [21] or start from aggregated headcounts [10,
82]. Neither uses metadata that the peer-to-peer protocols already
expose. The libp2p AgentVersion string encodes the client, proces-
sor architecture, and operating system [44, 69, 96]. The Ethereum
Node Record (ENR) carries subnet bitvectors that indicate whether
a node is acting as a validator [34, 61, 100]. Without attributing each
peer’s IP address to a hosting provider, the virtualisation-aware
cloud model of Pankovska et al. [82] also cannot be applied instance
by instance [66, 82].
The reachable-set total used below is the sum of estimated wall
power over peers that Nebula can dial on mainnet, that appear on
both CL and EL crawls, and that receive a rule label or a forest
imputation. NAT-only DHT clients, one-layer rows, and churn
between crawl sessions sit outside that set [59, 87]. It is a snapshot
lower bound, not a fleet count.
We address the following two questions:
(1) RQ1.How much do per-peer client, architecture, hosting,
and validator attributes change estimated node and network
power compared with one wattage applied to every peer?
(2) RQ2.How do the model’s predictions compare with wall-
power traces from a reference machine?
RQ1 needs a map from crawlable attributes to wattage, and a
check that a model trained on complete peers can fill the rest. RQ2
needs wall-power traces that were not used to build those wattages
[66, 91]. The pipeline assigns a wattage to each peer in a two-layer
mainnet crawl [48]. Cloud attribution, previously limited to Amazon
Web Services (AWS) [82], covers fourteen providers through the
Cloud Carbon Footprint (CCF) per-vCPU wattages [15]. ARM and
x86 hosts receive separate profiles. Validator activity is read per
peer from attestation subnets, sync-committee bits, and live gossip
topics [33, 34, 61]. Section 4 reports how well the forest recovers
the rule table, the snapshot total against a baseline that applies the
same wattage to every peer and against the CCAF index, the split
of watts by hosting and validator duty, and two 24-hour traces on
a reference machine.
2 Related Work
After the Merge, energy studies follow one of two paths. Some scale
a few measured wattages by a single network-wide headcount.
Others start from measured client and hardware pairs and then
guess how those pairs are distributed across the network. Hash rate
is gone, so the remaining draw is the wall power of the machines
that stay online [21, 82]. Table 1 places the main models next to the
pipeline used here.
The Crypto Carbon Ratings Institute (CCRI) merge report [21]
is the main measurement source. It reports idle baselines and the
extra watts each major consensus and execution client adds on a
few consumer machines, with both clients synchronised to mainnet.
Almost every later estimate, including this one and the 2024 CCRI
methods note [22], reuses those numbers. They are also the only
public set that covers all five then-common consensus clients under
one protocol. The cost of that reuse is inherited bias: the same two
Table 1: Post-Merge Ethereum energy models.
CCRI / Platt CCAF CBNSI Pankovska et al. This work
Input assumed global
mix
crawl counts +
mix
monitoring
counts
per-peer crawl
Cloud scope none / home
split
none AWS EC2 only 14 providers
ARM vs. x86 lumped or fixed lumped separate paths separate rules
Validator
signal
fleet average none at peer
level
fleet average ENR +
gossipsub
Validation CCRI lab — — wall-power
traces
or three chassis, and the same missing clients, appear in every later
model.
Platt et al. [86] published an earlier multi-chain estimate. They
assume one machine per validator, which pushes totals up relative
to models that allow several validators on one host [ 82]. Ibáñez
and Rua [55] put the CCRI figures into that framework, confirm
the post-Merge drop, and shrink the uncertainty interval. Both still
pick a global hardware mix instead of reading the attributes of a
named peer.
Cambridge’s Blockchain Network Sustainability Index (CBNSI)
[10] is the closest running estimate. It pairs CCRI wattages with
crawling: Armiarma from MigaLabs characterises beacon nodes
[19], and MonitorEth supplies counts for the hardware mix. That
already joins a crawl to a measurement table. ARM is still lumped
with x86, hosting is not read from a current IP-prefix list, and the
attestation and sync-committee bitvectors (attnets and syncnets)
are unused at the level of individual peers. Those three fields are
what move per-node watts [20, 100]. Cortes-Goicoechea et al. [20]
show that a large share of the network can run at home, including on
small boards. One weighted wattage cannot cover that low-power
tail and a high-memory cloud instance at the same time.
Pankovska et al . [82] add the cloud-versus-home split and a
power-usage-effectiveness (PUE) factor that accounts for data-
centre overhead. Their model is the first to apply instance-level
Amazon Web Services (AWS) Elastic Compute Cloud (EC2) fig-
ures to cloud nodes, with a 5 W solid-state-drive (SSD) overhead
and a cloud PUE of 1.2. We keep those two constants. Their cloud
path stops at AWS and still starts from monitoring counts, so the
virtualisation-aware formula is never applied instance by instance.
We map fourteen providers through Cloud Carbon Footprint (CCF)
per-vCPU wattages [15], keep ARM and x86 separate, and mark
validators from ENR bitvectors and live gossip topics instead of a
fleet average [34, 61].
Lei et al. [66] ask for measured hardware and an observed ma-
chine mix, not nameplate watts or an assumed validator-to-host
ratio. Sai and Vranken[91] treat a watt-meter check as required. The
node-level gaps above motivate RQ1; the call for a meter check mo-
tivates RQ2. Kiffer et al. [59] and Cortes-Goicoechea and Bautista-
Gomez [19] already show who is online at peer granularity, and
libp2p DHT crawls attribute peers to cloud providers by IP range
[103]. The energy models above still replace those peers with a
mix. Outside blockchains, Hoffmann and Majuntke [54] follow the
pattern we adopt: benchmark under controlled conditions once,
then evaluate compact models on attributes observable at run time,
without production power telemetry. Research infrastructures face
2

Quantifying Ethereum Energy Consumption via Network Mapping
the same question, from the MaRDI mathematical data portal [42]
to the data centres behind next-generation observatories [41]; both
propose efficiency measures but still lack per-component measure-
ments.
3 Method
The pipeline has four steps [40]: collect a two-layer crawl; extract
client, architecture, OS, hosting, and subnet features; assign wattage
from published measurements when those fields are complete; im-
pute the rest with a forest trained on the rule labels. Section 3.4
covers the wall-power setup for RQ2. Code and datasets are public
[48].
3.1 Crawl and features
We use two Nebula sessions [101] on mainnet, the crawler behind
the IPFS DHT measurements of Trautwein et al. [103]. The CL crawl
ran on 19 June 2026, 10:01–10:26 UTC (232,831 visits). The EL crawl
ran on 22 June 2026, 02:45–03:14 UTC (127,911 visits). Each visit is
a JSONL record with libp2p Identify fields [69], the ENR [61], and
Nebula metadata. The visit dumps are out_consensus.json and
out_execution.json.
IPv4 is taken from connect_maddr [88]; records without it are
dropped. Nebula only keeps peers that answer, so DHT clients be-
hind NAT that never accept inbound connections are outside the set
[87]; in libp2p networks, direct connections to such peers depend
on relay-assisted hole punching [102]. Layers are inner-joined on
(address, occurrence-index) so the 𝑘-th CL record at an address
matches the 𝑘-th EL record. We do not collapse several records
behind one public address into a single node: one address can front
several machines. Of 6,369 addresses seen on both layers, 3,440
(54%) have a different number of consensus and execution records,
so the𝑘-th pairing is an assumption rather than a guaranteed match.
Section 4.2 reports the subset of addresses that appear exactly once
on each layer as a sensitivity check. We keep the pairing rather
than drop unmatched rows [13]. Rows with a null consensus-layer
fork_digest are removed. That field marks mainnet membership
on the consensus layer and drops Optimism OP-Stack peers that
reuse the same networking stack [ 34, 77]. Table 2 lists the nor-
malised columns.
3.2 Power assignment
A peer receives a rule-based wattage only if both clients, the pro-
cessor architecture, and the operating system can be identified.
Incomplete rows are passed to the Random Forest (Section 3.3).
Caplin without Erigon is dropped because that pairing is not a valid
production configuration [29]. An empty hosting-provider field is
unclassified: the wattage rules treat it as a physical host without a
hypervisor. That choice overstates the home and bare-metal share
whenever a smaller cloud is missing from the fourteen prefix lists.
3.2.1 Bare-metal nodes.Unclassified prefixes are treated as physi-
cal hosts without a hypervisor [8, 20]. We use the CCRI idle base-
lines and the extra watts each client adds on synchronised mainnet
nodes [10, 21, 22, 82]. When both clients share a host, the combined
extra draw is scaled by 𝑓adj = 0.91[ 21]. Only CCRI configura-
tions 5 (Intel Core i5-10400, 64 GB, 25.04 W idle) and 6 (AMD Ryzen
Threadripper 3970X, 256 GB, 78.17 W idle) remain plausible: current
Table 2: Normalised crawl features used for wattage assign-
ment and modelling.
Feature Source and handling
consensus_clientConsensus-layerAgentVersionmatched
against Lighthouse, Prysm, Teku, Nimbus,
Lodestar, Grandine, Caplin.
execution_clientExecution-layer match against Geth,
Nethermind, Besu, Erigon, Reth, Nimbus-EL
[99], Ethrex.
hw_arch aarch64/arm64versusx86_64/amd64.
Conflicting tokens are left unresolved.
os_token linux,macos, orwindows. Conflicts are left
unresolved.
cloud_providerIPv4 prefix match on AWS, GCP, Azure,
Oracle, Hetzner, OVH, Contabo, Netcup,
Latitude, DigitalOcean, Vultr, Linode,
Leaseweb, Clouvider [90]. No match is
unclassified, not proven bare metal.
syncnets_numNumber of set bits in the Altairsyncnets
mask [33].
attnets_numNumber of set bits in the 64-bitattnets
mask [34].
gossipsub_att_countLivebeacon_attestation_{N}topics; used
with the bitvectors to flag validators.
production guidance asks for 32 GB for a non-validator and 64 GB
for a validator [95]. Table 3 records those two tiers.
Table 3: CCRI hardware configurations retained for unclassi-
fied x86 hosts [21].
Cfg. CPU RAM Idle (W)
5 Intel Core i5-10400 64 GB 25.04
6 AMD Ryzen TR 3970X 256 GB 78.17
Six clients seen in the crawl have no CCRI measurement. Gran-
dine and Caplin take the Nimbus consensus-layer extra draw (the
lowest measured value, which is conservative for designs that aim
at low resource use). Nethermind, Nimbus-EL, and Ethrex take the
Geth figure; Reth takes Erigon [20, 28, 45, 60, 76, 83, 85]. The mea-
sured extra watts on configurations 5 and 6 follow Crypto Carbon
Ratings Institute [21]: Lighthouse 3.14/18.84 W, Prysm 2.87/24.33 W,
Teku 3.32/27.46 W, Nimbus 2.08/17.11 W, Lodestar 3.89/33.55 W;
Geth 9.70/47.70 W, Erigon 17.59/44.62 W, Besu 31.02/75.04 W.
For x86 Linux and Windows,
𝑃node =
∑︁
𝑡∈{5,6}
𝑤𝑡·

(𝑃CL,𝑡+𝑃 EL,𝑡)×𝑓 adj+𝑃 idle,𝑡

,(1)
with 𝑓adj = 0.91, 𝑤5 = 0.75, and𝑤6 = 0.25. CCRI originally weighted
configurations 4, 5, and 6 as 0.25, 0.50, and 0.25. After dropping
the under-specified tier 4, the 0.75/0.25 split matches the EthStaker
survey in which 80% of home stakers run 64 GB or less [37]. Table 4
lists the other platforms. ARM Windows is dropped: no RAPL or
DCMI dataset exists for that pair [72, 81].
The ARM Linux token names the instruction-set architecture, not
a specific system-on-chip. We apply the 10 W figure only because
it is the long-run public mainnet measurement on a Raspberry Pi 5;
other ARM Linux boards are not treated as a separate class.
3

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
Table 4: Bare-metal wattage rules by architecture and operat-
ing system.
Arch. OS Assignment
x86 Linux, Windows Eq. (1); CCRI idle (Table 3).
x86 macOS Same extra watts; idle19.9W (2018 Intel
Mac mini) [5].
ARM macOS Same extra watts; idle6.9W (M1/M2 Mac
mini mean) [5].
ARM Linux Fixed10W [106, 107].
ARM Windows Dropped.
3.2.2 Cloud nodes.Cloud wattage depends on role (Table 5). The
ENR attnets field is a 64-bit mask of persistent attestation-subnet
subscriptions [34, 61]. Before consensus-specs pull request 3312,
any non-zero mask marked a validator. Since May 2023 every bea-
con node keeps two long-lived attestation subnets derived from
its node identity, so two set bits are the non-validator baseline
[71, 97]. Extra bits still cost CPU. Sutton [100] saw load rise with
each added attestation topic, because the node validates unaggre-
gated attestations on that subnet. The crawler also reports live
beacon_attestation_{N} gossip topics. Only validator clients call
the beacon committee_subscriptions API, so a topic count above
two is not explained by the backbone mandate [31]. Any set bit in
syncnets is restricted to active validators [32, 33]. A peer is flagged
as a validator if attnets_num> 2, gossipsub_att_count> 2, or
syncnets_num> 0. The two-subnet baseline applies only to attes-
tation subscriptions; any set sync-committee bit already marks an
active validator. The flag selects the hardware minima in Table 5
for cloud nodes. Unclassified x86 hosts still use the 0.75/0.25 mix
of configurations 5 and 6 regardless of duty; applying configura-
tion 6 only to validator-flagged unclassified nodes is a sensitivity
in Table 11.
Table 5: Minimum hardware assumed for a cloud node, by
role [43, 95].
Resource Non-validator Validator
RAM (GB) 32 64
vCPU 4 8
SSD (TB) 2 4
For AWS we follow Pankovska et al. [82]:
𝑃 AWS node = 𝑃pkg+𝑃 RAM+𝛿+𝑃 SSD ×𝜙 AWS,(2)
with 𝑃SSD = 5W and a data-centre overhead 𝜙AWS = 1.2. 𝑃pkg+
𝑃RAM+𝛿 is the Teads 100%-utilisation figure [23], the closest discrete
level given typical node load above 50%. We keep m6i/r6i for x86
[4, 23]; r6g uses Teads Graviton2 numbers and m7g a Graviton3
package term of100 ×𝑛/ 64W [ 84]. Candidates are filtered by
architecture and Table 5; we pick the smallest qualifying instance
[3].
Other providers use the CCF component model [15]:
𝑃 non-AWS node = 𝑊avg 𝑛vCPU+𝛽 RAM𝑛RAM+𝛽 SSD𝑛SSD ×𝜙 non-AWS,(3)
where 𝑊avg =|𝑀| −1 ˝ 𝑚∈𝑀 𝑊𝑚, with 𝛽RAM = 0.6W GB−1, 𝛽SSD =
1.2W TB−1, and 𝜙non-AWS = 1.185. 𝑊𝑚 is the per-vCPU maxi-
mum of microarchitecture 𝑚; 𝑀 is the provider fleet mix (CCF and
SPECpower coefficients and prefix lists are in the public repository
[48, 98]). Hardware counts again follow Table 5.
3.3 Random Forest for incomplete peers
Many peers advertise a hosting provider and subnet counts but omit
the client, architecture, or operating system. A provider-only aver-
age would discard the validator bits, so we fill incomplete rows with
a Random Forest [9, 12, 92]. The model is a standard regressor and is
not heavily tuned [94]. Inputs are the five categorical columns plus
the numeric subnet and gossip-topic counts. Empty provider values
become the unclassified token bare_metal. An OrdinalEncoder
uses sentinels−1and−2; encoder and forest form one Pipeline
fitted only on the training split [58]. The labeled set is split 80/20;
the forest has 500 trees. We also record the out-of-bag 𝑅2 and a
five-fold cross-validated𝑅 2 on all labeled rows.
A hold-out 𝑅2 against the rules, with client, architecture, and
operating system still visible, only shows that the trees can re-
build a deterministic table. When the forest is applied we hide
consensus_client, execution_client, hw_arch, and os_token
on the hold-out rows, which matches the information available
for incomplete peers. Unresolved categoricals stay as their own
encoded value [29, 68]. Caplin-without-Erigon rows are invalid (six
dropped).
3.4 Empirical power measurement
We recorded 24-hour wall-power traces on a Windows 11 x86 ma-
chine for two synchronised mainnet full-node pairs and an idle
baseline (no validator keys). Pairing each load scenario with an
idle baseline on the same machine follows established software
energy measurement models [47, 52]. Table 6 lists the chassis: a
Dell Alienware Aurora R16 gaming desktop. Home stakers usu-
ally run headless boxes [ 20, 37]. The GPU idles near 33 W in a
published review of this card [93]; that figure was not measured
on this PSU. Clients do not require a discrete GPU [ 21, 43]. We
report raw and GPU-adjusted figures. A myStrom WiFi Switch sat
inline with error margin under 1% [73]. Published windows [48]:
Nimbus+Geth (11 July 2026), Prysm+Nethermind (20–21 July 2026),
idle (16–17 July 2026). Measured idle is 71.1 W; after the 33 W GPU
that is 38.1 W against the pipeline’s 38.3 W CCRI x86 idle [10, 21].
Idle matches. The traces test client load.
Table 6: Gaming desktop used for the wall-power traces [ 25,
57].
Component Specification
System Dell Alienware Aurora R16
CPU i9-14900F (8P+16E / 32 threads; 65 W base, 219 W turbo)
Memory 64 GB DDR5-5600
GPU RTX 4090, 24 GB
PSU 1000 W Platinum
OS / plan Windows 11 Home; High Performance
Additionally, we explored the minimum hardware requirements
required to interact with the Ethereum Blockchain. The appen-
dix C reports a six-hour Helios light-client trace on a Raspberry Pi
Zero 2W. That measurement bounds the draw of a remote-RPC light
4

Quantifying Ethereum Energy Consumption via Network Mapping
client. It is not meant to validate the 10 W ARM Linux full-node
assignment [107].
4 Results
4.1 Crawl coverage
Of 6,940 matched peers, 3,110 (44.8%) receive a rule-based label and
3,824 get a forest wattage (99.9% coverage; Table 7). Six Caplin/non-
Erigon rows are invalid.
Table 7: Peer coverage for the 19/22 June 2026 crawl.
Category Count
Total CL+EL inner-joined peers 6,940
Rule-based labeled 3,110
Forest wattage 3,824
Invalid 6
4.2 Network-level estimate
Summing the rule labels and the forest estimates on the 6,934 valid
matched peers gives a reachable-set total of 415 kW, or 3.63 GWh if
that draw were held for a year (Table 8). Peers with a complete rule
label contribute 195 kW (mean 62.6 W); peers filled by the forest
contribute 220 kW (mean 57.5 W).
A uniform Lighthouse+Nethermind x86 assignment (the most
common labeled pair, with Nethermind on the Geth proxy) on the
same 6,934 peers is 431 kW (3.78 GWh/year). Per-peer mapping
lowers the total by 3.9%. Client choice moves the network sum only
a little on this crawl; the weights on the two hardware tiers move
it more (Section 4.4).
The snapshot is about 46% of the CCAF/CBNSI figure of about
0.90 MW (7.87 GWh/year) [ 10, 11]. At 59.8 W per peer, CCAF’s
demand implies on the order of 15,000 nodes. Mean watts are close:
59.8 W here versus about 60 W if CCAF’s 0.90 MW is spread over
15,000 nodes. Most of the gap is coverage. Peers seen on only one
layer, peers a crawl cannot dial, and churn between the consensus-
layer and execution-layer sessions, which are three days apart, are
all missing from our sum. If unseen peers look like the observed
mix, a straight scale-up would sit near 0.85–0.90 MW. We do not
apply that factor: there is no passive count of nodes that never
accept incoming connections [87].
Table 8: Estimated power of the reachable peers, compared
with applying one wattage to every peer and with the
CCAF/CBNSI index.
Estimate Power Annual energy
This work (6,934 matched peers) 415 kW 3.63 GWh
Same peers, one Lighthouse and
Nethermind x86 wattage
431 kW 3.78 GWh
CCAF/CBNSI (their census)∼0.90 MW 7.87 GWh
Restricting the join to addresses that appear once on the scored
table leaves 4,898 peers and 297 kW. The 54% of shared addresses
with a different number of consensus and execution records there-
fore account for much of the snapshot uncertainty.
4.3 Wattage shares
On the scored set, unclassified prefixes are 52.6% of peers and 54.3%
of watts; AWS is 12.2% of peers and 15.6% of watts; Hetzner averages
42.9 W and accounts for 11.9% of watts; and validator-flagged peers
are 25.7% of the set and 31.4% of watts (Tables 9 and 10). AWS and
validator-flagged nodes use a larger share of watts than of peers;
Hetzner uses a smaller share.
Table 9: Share of peers and of estimated watts by hosting
provider on the 6,934 scored peers.
Hosting Nodes Mean (W) Share
Unclassified (no listed prefix) 3,645 61.7 54.3%
AWS 849 76.4 15.6%
Hetzner 1,149 42.9 11.9%
OVH 768 58.3 10.8%
Other listed cloud 523 58.7 7.4%
Table 10: Share of peers and of estimated watts by validator
flag on the 6,934 scored peers.
Role Nodes Mean (W) Share
Non-validator 5,152 55.2 68.6%
Validator-flagged 1,782 73.1 31.4%
Figure 1 shows the mix among peers that received a rule-based la-
bel. On the consensus layer, Lighthouse leads at 47.8% [14, 36], then
Teku (19%), Nimbus (13.3%), Prysm (11.7%), and Lodestar (6.3%);
Caplin and Grandine stay below 2%. On the execution layer, Nether-
mind is 53%, Besu 18%, Geth 11.8%, Erigon 11.5%, and Reth 4.4%,
with Nimbus-EL at 1.1% and Ethrex at 0.2%. Besu carries the high-
est CCRI execution extra draw; almost one in five labeled nodes
can therefore draw up to three times the Geth/Nethermind proxy
wattage. A majority of labeled nodes (57.9%) match no listed cloud
prefix. Among listed-cloud nodes, Hetzner is 18.6% of the labeled
set, OVH 11.8%, and AWS 4.4%; Hetzner and OVH together are
30.4%. Part of that European-cloud share is a vantage effect: the
crawler ran from Germany and can over-represent nearby hosts
[59].
Persistent attestation-subnet subscriptions spike at 2 (83.7% of
labeled nodes); 6.1% sit at 4 and 9.0% subscribe to all 64 subnets
(Table 22). The all-64 tail validates unaggregated attestations on
every subnet [ 100]. The wattage rules use those extra bits only
as a validator flag and to raise the cloud hardware minima, so
the extra CPU cycles are not in the wattage table. Sync-committee
subscriptions are mostly zero (79.0%; Table 21). The remaining 13.3%
with four set bits match nodes that hold, or are about to hold, a
sync-committee seat: the committee has 512 validators and rotates
about every 27 hours [32]. Labeled power concentrates between
60 W and 70 W (mean 62.6 W, median 62.2 W), with clusters at
32–48 W and 80–88 W and a tail to 106.9 W from AWS validator-
tier instances (Figure 1c). The minimum is the 10 W ARM Linux
assignment.
Hosting provider dominates both importance measures (mean
decrease in impurity 0.456; permutation Δ𝑅2 = 1.312), then the live
attestation-topic count (0.215 and 0.580). Execution client is third by
5

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
(a) Client software.
 (b) Hosting provider.
(c) Estimated per-node power.
 (d) Forest importances (MDI and permutation).
Figure 1: Rule-based labeled mix (𝑛=3,110): clients, hosting, power, and forest importances.
impurity decrease (0.144) but fifth by permutation (0.254), because
four of the seven execution labels share the 9.70 W Geth proxy.
syncnets_num and hw_arch each contribute 0.088 of impurity de-
crease and rank third and fourth by permutation (0.323 and 0.273).
Consensus client, operating system, and the attestation-bit count
together contribute under 1% of impurity decrease (Figure 1d).
4.4 Sensitivity
Changing one assumption at a time on the labeled 195 kW (Table 11)
shows that the 0.75/0.25 hardware mix dominates: flattening it to
0.50/0.50 raises the labeled total by 24%. Cloud PUE, AWS utilisation,
and a validator-aware mix for unclassified hosts move the labeled
total by a few percent. The ARM Linux 10 W point is negligible on
this snapshot.
Table 11: Labeled-set power under one-at-a-time assumption
changes. Base is 195 kW.
Changed assumptionΔ𝑃
ARM Linux 8 W / 15 W−0.01% /+0.03%
Equal 0.50/0.50 weights on configs 5 and 6+24.1%
Cloud PUE1.1/1.4−2.8% /+6.8%
AWS utilisation50%−2.3%
Config 6 only for validator-flagged unclassified hosts+3.3%
4.5 Imputation
On 622 held-out labeled nodes, with client, architecture, and oper-
ating system still visible, the forest reaches a hold-out root-mean-
square error of 1.60 W, a mean absolute error (MAE) of 0.28 W
(0.44% of the test-set mean), and 𝑅2 = 0.9909(Table 12). Out-of-bag
𝑅2 is 0.9831; five-fold 𝑅2 on all 3,110 labels is0 .9890± 0.0074. Those
scores measure agreement with the rules, not with a watt-meter
[94]. Hiding exactly the fields that define a rule label, which is the
setting used for incomplete peers, drops hold-out 𝑅2 to 0.77 and
raises MAE to 4.3 W. Hiding the hosting provider instead leaves
𝑅2 = 0.48and MAE 9.3 W, which matches the importance ranking:
without a provider the imputer is weak. Figure 3 in the appendix is
the visible-field scatter.
Table 12: Random Forest evaluation against the rule wattages.
The imputation row hides the fields that are required to
create a rule label.
Evaluation𝑅 2 MAE (W)
Hold-out vs. rules (fields visible) 0.9909 0.28
Five-fold CV vs. rules0.9890±0.0074—
Out-of-bag vs. rules 0.9831 —
Hide client, arch, OS (imputation) 0.77 4.34
Hide hosting provider 0.48 9.32
4.6 Empirical comparison
The gaming desktop is encoded as in Table 13: unclassified x86
Windows, the two-subnet backbone, and the two client pairs. Traces
use a 20-sample centred rolling average [66]. Raw traces sit above
the model’s point prediction all day. System idle is 71.1 W; most
of that is platform background. Subtracting the 33 W RTX 4090
idle [7, 93] leaves 38.1 W idle and cuts the deviations from 43.7%
and 26.8% to 19.0% and 18.5% (Figure 2, Table 14). The leftovers
have opposite signs (−14.26W for Nimbus+Geth, +9.93W for
Prysm+Nethermind). We do not add that residual to 415 kW as a
constant offset.
5 Discussion
Assigning a wattage from each peer’s advertised attributes changes
the snapshot by−3.9% compared with applying one Lighthouse and
Nethermind x86 wattage to every peer. AWS and validator-flagged
nodes use a larger share of watts than of peers; Hetzner uses a
smaller share. The 415 kW (3.63 GWh/year) figure is the sum over
peers that this crawl can reach and match across both layers. It is a
lower bound, not a fleet count. It is about 46% of CCAF’s∼0.90 MW
6

Quantifying Ethereum Energy Consumption via Network Mapping
(a) Raw traces.
 (b) Traces after subtracting idle GPU power.
Figure 2: 24-hour wall-power traces compared with the model point predictions and the idle baseline.
Table 13: Feature rows submitted to the trained pipeline for
the gaming desktop. Unclassified hosting is the pipeline to-
kenbare_metal.
Feature Nimbus+Geth Prysm+Neth.
hw_arch/os_tokenx86 / windows x86 / windows
cloud_providerunclassified unclassified
attnets_num2 2
gossipsub_att_count2 2
syncnets_num0 0
Table 14: Measured 24-hour mean power versus the model
prediction on the bare-metal x86 Windows gaming desktop.
Client pair GPU off ∗ Meas. [W] Pred. [W] Err. [%]
Nimbus + Geth No 108.36 61.1 43.7
Prysm + Nethermind No 86.37 63.3 26.8
Nimbus + Geth Yes 75.36 61.1 19.0
Prysm + Nethermind Yes 53.37 63.3 18.5
∗Subtract the RTX 4090 idle of 33 W [93] from the 24-hour mean.
because this crawl sees fewer nodes; mean watts stay near 60 W in
both estimates. The hardware-tier weights move the labeled total
more than client choice does (+24.1% if the 0.75/0.25 mix is flattened
to 0.50/0.50).
That 3.63 GWh already exceeds the 0.5 GWh MiCAR threshold
at which a reporting entity must also fill in greenhouse-gas and
renewable-share fields [38]. Those fields apply to a reporting entity,
not to the network as a whole, and they need a location and a
grid mix that this paper does not estimate. A host that claims 100%
renewable electricity still counts in the energy total.
Besu, the highest-power CCRI execution client, is second at 18%
of the labeled execution-layer mix, so almost one in five labeled
nodes can draw up to three times the Geth/Nethermind extra watts
(Figure 1c). Validator-flagged peers average 73.1 W against 55.2 W
for the rest. The full consensus-client range on configuration 5 is
only 1.81 W [21], which is why the consensus client contributes
almost nothing to forest importance. Hosting still moves the labeled
histogram: Hetzner and OVH sit in the lower half and pull the
mode into 60–70 W, while AWS accounts for the tail above 100 W
through Equation (2). Validator signals describe mostly non-staking
full nodes (83.7% at two attestation subnets), a moderate cluster
at three or four subnets, and a 9% all-subnet tail that pays the full
attestation-validation cost [100]; 13.3% with four sync-committee
bits match sync-committee seats [32]. The forest barely uses the
attestation-bit count because the rules do not add watts for extra
topics beyond the validator hardware step.
For RQ1, the visible-field forest scores agree because the target
is a deterministic rule table. Hold-out 𝑅2 = 0.9909, out-of-bag
𝑅2 = 0.9831, and five-fold 𝑅2 = 0.9890± 0.0074all sit within 0.008 of
one another. Residuals concentrate at tier boundaries (Figure 3) [6].
Those metrics are agreement with the assignment rules, not with a
meter. The scores that matter for incomplete peers are the masked
ones: hosting recovers most of the label (MAE 4.3 W); without a
provider the imputer is weak.
For RQ2, raw idle on the test machine is 71.1 W. After removing
the RTX 4090, non-GPU idle is about 38.1 W against the pipeline’s
38.3 W x86 idle [21]. More than half of each raw deviation is that
GPU offset, which no CCRI box and no typical Ethereum node
has [43]. Remaining residuals have opposite signs (−14.26W for
Nimbus+Geth,+9.93W for Prysm+Nethermind), so they come
from the clients. Nethermind is treated as lighter than Geth in other
comparisons [85]; the traces also ran on Windows 11 while CCRI
measured Linux [21, 74]. We do not add that residual to 415 kW as
a constant. The validation chassis is a 219 W-turbo gaming desktop
with a 1000 W power supply; home stakers report headless low-
power boxes [20, 37]. The Helios 0.84 W mean is light-client draw
on a board that never stored the chain. It is not an ARM full-node
wattage.
5.1 Limitations
The rule wattages are published measurements and proxies, not a
meter on each peer. Forest scores against those rules are not empir-
ical accuracy. The consensus-layer and execution-layer crawls are
three days apart [46, 56, 59], and 54% of shared addresses have a
different number of records on the two layers [49, 70]. The 33 W
GPU correction is a published idle figure for the card, not a measure-
ment on this power supply. Six clients inherit proxy wattages; on
Windows, Nethermind drew less than its Geth proxy. Process-level
power attribution on Linux [53] could replace these proxies with
per-client measurements on a shared host.
The two CCRI boxes set the unclassified x86 wattages [21]. The
0.75/0.25 mix moves the labeled total by 24% if flattened to 0.50/0.50.
Hence, this distribution causes high sensitivity on the final en-
ergy consumption estimation. Unclassified prefixes include unlisted
clouds. The crawl vantage is Germany. The wall-power check cov-
ers one gaming desktop and two non-validator pairs, with no cloud
or ARM full node. The 33 W GPU offset belongs to this chassis only.
7

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
Active crawls miss nodes that never accept inbound connections.
A passive keyspace listener such as Ants-Watch, run with the same
Nebula snapshot, can bound that hidden population from incoming
routing-table traffic [87]. We do not scale 415 kW by an unseen
factor. There is no count of how many such peers exist. The 9%
all-attestation-subnet tail is extra CPU on peers already in the table.
6 Conclusion
RQ1 holds for the assignment table. Client identity, architecture,
operating system, hosting, and subnet activity are enough to rebuild
the wattages used here. A 500-tree forest trained on 3,110 labels
reaches hold-out 𝑅2 = 0.9909, five-fold 𝑅2 = 0.9890± 0.0074, and
a normalised MAE of 0.44%, and covers 99.9% of matched peers.
Those scores are agreement with the rules, not with a watt-meter.
When the fields that define a rule label are hidden, hold-out MAE
is 4.3 W.
On the same 6,934 matched peers, estimated draw is 415 kW,
or 3.63 GWh if held for a year. That is 3.9% below applying the
same Lighthouse and Nethermind x86 wattage to every peer, and
about 46% of the CCAF index, mainly because this snapshot sees
fewer nodes. AWS and validator-flagged peers take a larger share
of watts than of headcount. Flattening the CCRI 0.75/0.25 hardware
mix moves the labeled total by 24%.
RQ2 is only partly closed. The traces come from one gaming
desktop. Raw idle is 71.1 W. After subtracting a 33 W discrete-GPU
idle, 24-hour means sit about 19% from the predictions and non-
GPU idle matches the CCRI x86 baseline. The leftover error is a
proxied client and a Windows-versus-Linux difference. Still missing
are headless Linux traces, watts for the all-attestation-subnet tail,
and a same-day crawl with a passive listener for nodes that never
accept incoming connections [87].
From our measurements, we estimated that the Ethereum net-
work, with measured 3.63 GWh/year is well above the 0.5 GWh/year
threshold of the MiCAR regulation. Therefore, service providers
using Ethereum Tokens must provide full sustainability disclosures.
To comply, our results must be extended using grid mix data [38, 39].
Our whole estimation model is available at the Github repository:
https://github.com/yahncosta/ethereum-energy-code; crawls, ta-
bles, and traces are at https://huggingface.co/datasets/yhackspacher/
ethereum-energy-data [48].
References
[1] a16z crypto. 2022. Helios: A fast, secure, and portable multichain light client
for Ethereum. https://github.com/a16z/helios.
[2] Akamai Technologies (Linode). 2024. Linode Plans and Pricing. https://www.
linode.com/pricing/.
[3] Amazon Web Services. 2020.Right Sizing: Provisioning Instances to Match
Workloads. Technical Report. Amazon Web Services. https://d1.awsstatic.com/
whitepapers/cost-optimization-right-sizing.pdf
[4] Amazon Web Services. 2024. Amazon RDS for Db2 expands support for M6i
and R6i in additional AWS Regions. https://aws.amazon.com/about-aws/whats-
new/2024/03/amazon-rds-db2-m6i-r6i-additional-aws-regions/.
[5] Apple Inc. 2024. Mac mini power consumption and thermal output information.
https://support.apple.com/en-us/103253.
[6] Susan Athey and Guido W. Imbens. 2019. Machine Learning Methods That
Economists Should Know About.Annual Review of Economics11, 1 (2019),
685–725. doi:10.1146/annurev-economics-080217-053433
[7] Sara Bergman. 2021. How to Measure the Energy Consumption of Your Back-
end Service. https://greensoftware.foundation/articles/how-to-measure-the-
energy-consumption-of-your-backend-service/.
[8] Blockdaemon. 2023. What is Bare Metal Blockchain Infrastructure? https://
www.blockdaemon.com/blog/what-is-bare-metal-blockchain-infrastructure.
[9] Leo Breiman. 2001. Random Forests.Machine Learning45, 1 (2001), 5–32.
doi:10.1023/A:1010933404324
[10] Cambridge Centre for Alternative Finance. 2023. Cambridge Blockchain
Network Sustainability Index: Ethereum Methodology. https://ccaf.io/cbnsi/
ethereum/methodology.
[11] Cambridge Centre for Alternative Finance. 2026. Ethereum After the Merge:
A Change in Power. https://www.jbs.cam.ac.uk/2026/new-report-maps-
ethereums-climate-footprint-with-new-precision/.
[12] Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien (Eds.). 2006.Semi-
Supervised Learning. MIT Press, Cambridge, MA. doi:10.7551/mitpress/
9780262033589.001.0001
[13] Peter Christen. 2012.Data Matching: Concepts and Techniques for Record Linkage,
Entity Resolution, and Duplicate Detection. Springer, Berlin, Heidelberg. doi:10.
1007/978-3-642-31164-2
[14] Client Diversity Org. 2025. Client Diversity. https://clientdiversity.org/.
[15] Cloud Carbon Footprint contributors. 2024. Cloud Carbon Footprint Methodol-
ogy. https://www.cloudcarbonfootprint.org/docs/methodology.
[16] Clouvider Ltd. 2024. VPS Hosting Plans. https://www.clouvider.com/vps-
hosting/.
[17] Contabo GmbH. 2024. Introducing the New AMD Genoa 24 Bare Metal
Server. https://contabo.com/blog/our-dedicated-servers-just-got-more-epyc-
introducing-the-new-amd-genoa-24-bare-metal-server/.
[18] Contabo GmbH. 2025. AMD Turin CPUs Join the Contabo Virtualization
Hosts. https://contabo.com/blog/always-improving-amd-turin-cpus-join-the-
contabo-virtualization-hosts-inventory/.
[19] Mikel Cortes-Goicoechea and Leonardo Bautista-Gomez. 2021. Discovering the
Ethereum2 P2P Network. In2021 Third International Conference on Blockchain
Computing and Applications (BCCA). IEEE, Tartu, Estonia, 81–88. doi:10.1109/
BCCA53669.2021.9657041
[20] Mikel Cortes-Goicoechea, Tarun Mohandas-Daryanani, José Luis Muñoz-Tapia,
and Leonardo Bautista-Gomez. 2024. Can We Run Our Ethereum Nodes at
Home?IEEE Access12 (2024), 44401–44423. doi:10.1109/ACCESS.2024.3381782
[21] Crypto Carbon Ratings Institute. 2022. The Merge – Implications on the
Electricity Consumption and Carbon Footprint of the Ethereum Network.
https://carbon-ratings.com/eth-report-2022.
[22] Crypto Carbon Ratings Institute. 2024. Determining the Electricity Con-
sumption and Carbon Footprint of Proof of Stake Networks. https://carbon-
ratings.com/dl/whitepaper-pos-methods-2024.
[23] Benjamin Davy. 2021. Estimating AWS EC2 Instances Power Consump-
tion. https://medium.com/teads-engineering/estimating-aws-ec2-instances-
power-consumption-c9745e347959.
[24] Alex de Vries. 2022. Ethereum Energy Consumption Index. https://digiconomist.
net/ethereum-energy-consumption.
[25] Dell Inc. 2024. Alienware Aurora R16 Gaming Desktop: Product
Page. https://www.dell.com/en-us/shop/desktop-computers/alienware-aurora-
r16-gaming-desktop/spd/alienware-aurora-r16-desktop/useahctor16i16.
[26] DigitalOcean, LLC. 2021. Introducing Premium Droplets with Faster Intel and
AMD CPUs and NVMe SSD. https://www.digitalocean.com/blog/premium-
droplets-intel-cascade-lake-amd-epyc-rome.
[27] DigitalOcean, LLC. 2024. Choosing the Right CPU Droplet Plan. https://docs.
digitalocean.com/products/droplets/concepts/choosing-a-plan/.
[28] Erigon contributors. 2023. Announcing Caplin: Erigon Full Consensus Layer is
Now Live. https://erigon.tech/announcing-caplin-erigon-full-consensus-layer-
is-now-live/.
[29] Erigon contributors. 2024. Caplin: Embedded Consensus Layer Client in Erigon.
https://github.com/erigontech/erigon/tree/main/cl.
[30] Ethereum Foundation. 2022. The Merge: Ethereum Roadmap. https://ethereum.
org/roadmap/merge/.
[31] Ethereum Foundation. 2024. Ethereum Beacon Node API: Validator Flow. https:
//github.com/ethereum/beacon-APIs/blob/master/validator-flow.md.
[32] Ethereum Foundation. 2024. Ethereum Consensus Layer Altair Beacon Chain
Specification. https://github.com/ethereum/consensus-specs/blob/master/
specs/altair/beacon-chain.md.
[33] Ethereum Foundation. 2024. Ethereum Consensus Layer Altair P2P Interface
Specification. https://github.com/ethereum/consensus-specs/blob/dev/specs/
altair/p2p-interface.md.
[34] Ethereum Foundation. 2024. Ethereum Consensus Layer Phase 0 P2P Inter-
face Specification. https://github.com/ethereum/consensus-specs/blob/master/
specs/phase0/p2p-interface.md.
[35] Ethereum Foundation. 2024. Light clients. https://ethereum.org/en/developers/
docs/nodes-and-clients/light-clients/.
[36] Ethereum Foundation. 2025. Client Diversity: Ethereum Documentation. https:
//ethereum.org/developers/docs/nodes-and-clients/client-diversity/.
[37] EthStaker. 2025. 2025 Staking Survey Results. https://paragraph.com/
@ethstaker/staking-survey-2025.
8

Quantifying Ethereum Energy Consumption via Network Mapping
[38] European Commission. 2025. Commission Delegated Regulation (EU) 2025/422
supplementing Regulation (EU) 2023/1114 with regard to regulatory technical
standards specifying the content, methodologies and presentation of informa-
tion in respect of sustainability indicators. https://eur-lex.europa.eu/eli/reg_
del/2025/422/oj.
[39] European Parliament and Council of the European Union. 2023. Regulation
(EU) 2023/1114 on Markets in Crypto-Assets, and amending Regulations (EU)
No 1093/2010 and (EU) No 1095/2010 and Directives 2013/36/EU and (EU)
2019/1937. https://eur-lex.europa.eu/eli/reg/2023/1114/oj.
[40] Usama Fayyad, Gregory Piatetsky-Shapiro, and Padhraic Smyth. 1996. From
Data Mining to Knowledge Discovery in Databases.AI Magazine17, 3 (1996),
37–54. doi:10.1609/aimag.v17i3.1230
[41] Laurane Fréour, Mathilde Bouvier, Tony Mroczkowski, Callie Clontz, Fate-
meh Zahra Majidi, Vasundhara Shaw, Olivier Absil, Anna Cabré, Olivier Lai,
Dylan Magill, and Jake D. Turner. 2025. A vision for ground-based astron-
omy beyond the 2030s: How to build ESO’s next big telescope sustainably.
arXiv:2512.10902 https://arxiv.org/abs/2512.10902
[42] Noah Gießing, Madhurima Deb, Ankit Satpute, Moritz Schubotz, and Olaf
Teschke. 2024. Reducing the climate impact of data portals: a case study.
arXiv:2406.03858 https://arxiv.org/abs/2406.03858
[43] go-ethereum contributors. 2023. Hardware Requirements: go-ethereum
Documentation. https://geth.ethereum.org/docs/getting-started/hardware-
requirements.
[44] go-ethereum contributors. 2024. node/config.go: Go Ethereum source code.
https://github.com/ethereum/go-ethereum/blob/master/node/config.go.
[45] Grandine Core Team. 2024. Grandine: High Performance Ethereum Consensus
Client. https://github.com/grandinetech/grandine.
[46] Dominic Grandjean, Lioba Heimbach, and Roger Wattenhofer. 2025. Ethereum
Proof-of-Stake Consensus Layer: Participation and Decentralization. InFinan-
cial Cryptography and Data Security. FC 2024 International Workshops (Lecture
Notes in Computer Science, Vol. 14746). Springer, Cham, Switzerland, 253–280.
doi:10.1007/978-3-031-69231-4_17
[47] Achim Guldner, Rabea Bender, Coral Calero, Giovanni S. Fernando, Markus
Funke, Jens Gröger, Lorenz M. Hilty, Julian Hörnschemeyer, Geerd-Dietger
Hoffmann, Dennis Junger, Tom Kennes, Sandro Kreten, Patricia Lago, Franziska
Mai, Ivano Malavolta, Julien Murach, Kira Obergöker, Benno Schmidt, Arne
Tarara, Joseph P. De Veaugh-Geiss, Sebastian Weber, Max Westing, Volker
Wohlgemuth, and Stefan Naumann. 2024. Development and evaluation of a
reference measurement model for assessing the resource and energy efficiency
of software products and components—Green Software Measurement Model
(GSMM).Future Generation Computer Systems155 (2024), 402–418. doi:10.1016/
j.future.2024.01.033
[48] Yahn Costa Hackspacher. 2026. Github Repository and Hugging Face Dataset for
Ethereum Energy Consumption Analysis. Code: https://github.com/yahncosta/
ethereum-energy-code; Dataset: https://huggingface.co/datasets/yhackspacher/
ethereum-energy-data.
[49] Lioba Heimbach, Yann Vonlanthen, Juan Villacis, Lucianna Kiffer, and Roger
Wattenhofer. 2025. Deanonymizing Ethereum Validators: The P2P Network
Has a Privacy Issue. In34th USENIX Security Symposium (USENIX Security
25). USENIX Association, Seattle, WA, 1319–1338. https://www.usenix.org/
conference/usenixsecurity25/presentation/heimbach
[50] Hetzner Online GmbH. 2023. New CCX Cloud Server Plans: Dedicated vCPUs
from AMD EPYC Genoa and Milan. https://www.hetzner.com/pressroom/new-
dedicated-vcpu-cloud-servers/.
[51] Hetzner Online GmbH. 2024. New AX162 Dedicated Server with AMD EPYC
Genoa 9454P. https://www.hetzner.com/news/new-ax162/.
[52] Geerd-Dietger Hoffmann and Verena Majuntke. 2024. Green Metrics Tool:
Measuring for fun and profit. InProceedings of the 1st International Workshop
on Low Carbon Computing (LOCO 2024). Glasgow, United Kingdom, 1–3. https:
//www.sicsa.ac.uk/wp-content/uploads/2024/11/LOCO2024_paper_24.pdf
[53] Geerd-Dietger Hoffmann and Verena Majuntke. 2025. PowerLetrics: An Open-
Source Framework for Power and Energy Metrics for Linux. In2025 IEEE/ACM
9th International Workshop on Green and Sustainable Software (GREENS). IEEE,
Ottawa, ON, Canada, 28–30. doi:10.1109/GREENS66463.2025.00009
[54] Geerd-Dietger Hoffmann and Verena Majuntke. 2026. Measure Once, Model
Everywhere: Model-Based Per-Request Resource Consumption for HTTP. In
Proceedings of the 12th Workshop on Computing within Limits (LIMITS 2026).
Online. arXiv:2607.01246 https://arxiv.org/abs/2607.01246
[55] Juan Ignacio Ibáñez and Francisco Rua. 2023. The energy consumption of
Proof-of-Stake systems: Replication and expansion. arXiv:2302.00627 https:
//arxiv.org/abs/2302.00627
[56] Muhammad Anas Imtiaz, David Starobinski, Ari Trachtenberg, and Nabeel
Younis. 2019. Churn in the Bitcoin Network: Characterization and Impact. In
2019 IEEE International Conference on Blockchain and Cryptocurrency (ICBC).
IEEE, Seoul, South Korea, 431–439. doi:10.1109/BLOC.2019.8751297
[57] Intel Corporation. 2024. Intel®Core™i9 processor 14900F (36M Cache, up to
5.80 GHz): Product Specifications. https://www.intel.com/content/www/us/en/
products/sku/236853/intel-core-i9-processor-14900f-36m-cache-up-to-5-80-
ghz/specifications.html.
[58] Shachar Kaufman, Saharon Rosset, Claudia Perlich, and Ori Stitelman. 2012.
Leakage in Data Mining: Formulation, Detection, and Avoidance.ACM Transac-
tions on Knowledge Discovery from Data6, 4 (2012), 1–21. doi:10.1145/2382577.
2382579
[59] Lucianna Kiffer, Lioba Heimbach, Dennis Trautwein, Yann Vonlanthen, and
Oliver Gasser. 2025. Multiple Sides of 36 Coins: Measuring Peer-to-Peer Infras-
tructure Across Cryptocurrencies.Proceedings of the ACM on Measurement and
Analysis of Computing Systems9, 3 (2025), 1–32. doi:10.1145/3771572
[60] LambdaClass. 2026. ethrex: Minimalist, Stable, Modular and Fast Implementa-
tion of the Ethereum Protocol. https://github.com/lambdaclass/ethrex.
[61] Felix Lange. 2017. EIP-778: Ethereum Node Records (ENR). https://eips.
ethereum.org/EIPS/eip-778.
[62] Latitude.sh. 2024. Bare Metal Server Plans. https://www.latitude.sh/pricing.
[63] Latitude.sh. 2025. Pricing Overview: Latitude.sh. https://www.latitude.sh/
pricing.
[64] LeaseWeb Netherlands B.V. 2020. Leaseweb Brings 2nd Gen AMD
EPYC Processor Powered Servers to Their Customers. https:
//vmblog.com/archive/2020/03/11/leaseweb-brings-2nd-gen-amd-epyc-
processor-powered-servers-to-their-customers.aspx.
[65] LeaseWeb Netherlands B.V. 2024. Virtual Servers. https://www.leaseweb.com/
virtual-servers.
[66] Nuoa Lei, Eric Masanet, and Jonathan Koomey. 2021. Best practices for analyzing
the direct energy use of blockchain technology systems: Review and policy
recommendations.Energy Policy156 (2021), 112422. doi:10.1016/j.enpol.2021.
112422
[67] Stephan Leible, Steffen Schlager, Moritz Schubotz, and Bela Gipp. 2019. A
Review on Blockchain Technology and Blockchain Projects Fostering Open
Science.Frontiers in Blockchain2 (2019), 16. doi:10.3389/fbloc.2019.00016
[68] Oliver Urs Lenz, Daniel Peralta, and Chris Cornelis. 2025. No Imputation
Without Representation. InArtificial Intelligence and Machine Learning. Com-
munications in Computer and Information Science, Vol. 2187. Springer, Cham,
1–21. doi:10.1007/978-3-031-74650-5_1
[69] libp2p contributors. 2024. libp2p Identify Protocol Specification. https://github.
com/libp2p/specs/blob/master/identify/README.md.
[70] Jiahao Luo. 2025. Unveiling Ethereum’s P2P Network: The Role of Chain and
Client Diversity. arXiv:2501.16236 https://arxiv.org/abs/2501.16236
[71] Age Manning. 2023. Attnet revamp: Subnet backbone structure based on beacon
nodes. https://github.com/ethereum/consensus-specs/pull/3312.
[72] Microsoft. 2025. Hardware Requirements for Windows Server. https://learn.
microsoft.com/en-us/windows-server/get-started/hardware-requirements.
[73] myStrom AG. 2024. myStrom WiFi Switch: Product Page. https://mystrom.
com/wifi-switch/.
[74] Sayed Najmuddin, Zabihullah Atal, and Riaz Ahmad Ziar. 2021. Comparative
Analysis of Power Consumption of the Linux and its Distribution Operating
Systems vs Windows and Mac Operating Systems.Kardan Journal of Engineering
and Technology3, 1 (2021), 96–109. doi:10.31841/KJET.2022.21
[75] netcup GmbH. 2024. VPS Product Overview. https://www.netcup.eu/vserver/
vps.php.
[76] Nethermind contributors. 2024. Nethermind: Ethereum Execution Client. https:
//github.com/NethermindEth/nethermind.
[77] OP Labs. 2024. OP Stack Overview. https://docs.optimism.io/stack/getting-
started.
[78] Oracle Corporation. 2024. Oracle Cloud Infrastructure Compute
Shapes. https://docs.oracle.com/en-us/iaas/Content/Compute/References/
computeshapes.htm.
[79] OVHcloud. 2024. Public Cloud Instances. https://www.ovhcloud.com/en/public-
cloud/compute/.
[80] OVHcloud US. 2024. OVHcloud US Announces New Advance Bare Metal
Servers with AMD EPYC 4004 Series CPUs. https://us.ovhcloud.com/press/
press-releases/2024/ovhcloud-us-announces-new-advance-bare-metal-
servers-with-best-of-breed-amd-epyc-4004-series-cpus/.
[81] Deepak Panigrahy and Aakash Tyagi. 2026. The Energy Blind Spot: NVIDIA’s
Flagship Edge AI Hardware Cannot Support Process-Level Energy Attribution.
InProceedings of the 2nd International Workshop on Low Carbon Computing
(LOCO 2026). Lancaster, United Kingdom. arXiv:2605.27599 https://arxiv.org/
abs/2605.27599
[82] Elitsa Pankovska, Ashish Rajendra Sai, Harald Vranken, and Alan Ransil. 2024.
Electricity Consumption of Ethereum and Filecoin: Advances in Models and
Estimates. InProceedings of the 39th ACM/SIGAPP Symposium on Applied Com-
puting (SAC ’24). ACM, Ávila, Spain, 269–277. doi:10.1145/3605098.3635952
[83] Paradigm. 2024. Reth: Ethereum Protocol in Rust. https://github.com/
paradigmxyz/reth.
[84] Dylan Patel. 2021. Amazon Graviton 3 Uses Chiplets & Advanced Packaging to
Commoditize High Performance CPUs. https://newsletter.semianalysis.com/p/
amazon-graviton-3-uses-chiplets-and.
9

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
[85] Priyavanshi Pathania, Nikhil Bamby, Rohit Mehra, Samarth Sikand, Vibhu Sau-
janya Sharma, Vikrant Kaulgud, Sanjay Podder, and Adam P. Burden. 2025.
Calculating Software’s Energy Use and Carbon Emissions: A Survey of the
State of Art, Challenges, and the Way Ahead. In2025 IEEE/ACM 9th Interna-
tional Workshop on Green and Sustainable Software (GREENS). IEEE, Ottawa,
ON, Canada, 92–99. doi:10.1109/GREENS66463.2025.00018
[86] Moritz Platt, Johannes Sedlmeir, Daniel Platt, Jiahua Xu, Paolo Tasca, Nikhil
Vadgama, and Juan Ignacio Ibáñez. 2021. The Energy Footprint of Blockchain
Consensus Mechanisms Beyond Proof-of-Work. In2021 IEEE 21st International
Conference on Software Quality, Reliability and Security Companion (QRS-C).
IEEE, Hainan, China, 1135–1144. doi:10.1109/QRS-C55045.2021.00168
[87] ProbeLab. 2024. ants-watch: DHT Client Monitoring. https://github.com/probe-
lab/ants-watch.
[88] Protocol Labs. 2024. Addressing: libp2p Documentation. https://docs.libp2p.io/
concepts/fundamentals/addressing/.
[89] Raspberry Pi Ltd. 2021. Raspberry Pi Zero 2 W. https://www.raspberrypi.com/
products/raspberry-pi-zero-2-w/.
[90] RIPE NCC. 2024. RIPEstat Data API: Announced Prefixes Endpoint. https:
//stat.ripe.net/docs/data-api/api-endpoints/announced-prefixes.
[91] Ashish Rajendra Sai and Harald Vranken. 2024. Promoting rigor in blockchain
energy and environmental footprint research: A systematic literature review.
Blockchain: Research and Applications5, 1 (2024), 100169. doi:10.1016/j.bcra.
2023.100169
[92] scikit-learn developers. 2024. Model Persistence: scikit-learn Documentation.
https://scikit-learn.org/stable/model_persistence.html.
[93] ServeTheHome. 2022. NVIDIA GeForce RTX 4090 Founders Edition Re-
view. https://www.servethehome.com/nvidia-geforce-rtx-4090-founders-
edition-review-the-gpu/.
[94] Ravid Shwartz-Ziv and Amitai Armon. 2022. Tabular Data: Deep Learning Is
Not All You Need.Information Fusion81 (2022), 84–90. doi:10.1016/j.inffus.2021.
11.011
[95] Sigma Prime. 2023. Installation: Lighthouse Book. https://lighthouse-book.
sigmaprime.io/installation.html.
[96] Sigma Prime. 2025. Lighthouse Releases. https://github.com/sigp/lighthouse/
releases.
[97] Santiago Somoza, Tarun Mohandas-Daryanani, and Leonardo Bautista-Gomez.
2025. Blockprint Accuracy Study. In2025 7th International Conference on
Blockchain Computing and Applications (BCCA). IEEE, 249–256. doi:10.1109/
BCCA66705.2025.11229786
[98] Standard Performance Evaluation Corporation. 2008. SPECpower_ssj2008
Benchmark. https://www.spec.org/power_ssj2008/.
[99] Status Research & Development. 2025. Execution Client: The Nimbus Guide.
https://nimbus.guide/execution-client.html.
[100] Adrian Sutton. 2022. Exploring Eth2: Cost of Adding Validators. https://www.
symphonious.net/2022/04/06/exploring-eth2-cost-of-adding-validators/.
[101] Dennis Trautwein. 2023. Nebula: A Network-Agnostic DHT Crawler and
Monitor. https://github.com/dennis-tra/nebula.
[102] Dennis Trautwein, Cornelius Ihle, Moritz Schubotz, Corinna Breitinger, and Bela
Gipp. 2026. Large-Scale Measurement of NAT Traversal for the Decentralized
Web: A Case Study of DCUtR in IPFS. InProceedings of the 2026 ACM Internet
Measurement Conference (IMC ’26). ACM, Karlsruhe, Germany, 779–794. doi:10.
1145/3777912.3809138
[103] Dennis Trautwein, Aravindh Raman, Gareth Tyson, Ignacio Castro, Will Scott,
Moritz Schubotz, Bela Gipp, and Yiannis Psaras. 2022. Design and Evaluation
of IPFS: A Storage Layer for the Decentralized Web. InProceedings of the ACM
SIGCOMM 2022 Conference (SIGCOMM ’22). ACM, Amsterdam, Netherlands,
739–752. doi:10.1145/3544216.3544232
[104] Vultr Holdings LLC. 2022. High Performance and Truly EPYC: Vultr’s New
VMs. https://blogs.vultr.com/high-performance-and-truly-epyc-vultrs-new-
vms-are-ready-for-anything.
[105] Vultr Holdings LLC. 2024. Cloud Compute Instance Types. https://www.vultr.
com/products/cloud-compute/.
[106] Web3 Pi. 2024. About Web3 Pi. https://docs.web3pi.io/introduction/web3-pi-
project/.
[107] Web3 Pi and Golem Network. 2024. 200 Validators on a Single Raspberry Pi 5.
https://www.web3pi.io/blog/200-ethereum-validators-on-rpi5.
10

Quantifying Ethereum Energy Consumption via Network Mapping
A Cloud assignment tables
Tables 15 and 16 define the symbols in Equation (2). Tables 17–20
supply the CCF coefficients used in Equation (3).
Table 15: Variables in the A WS node-power equation (Equa-
tion(2)).
Symbol Definition Value
𝑃pkg CPU package power Table 16
𝑃RAM DRAM power Table 16
𝛿Residual overhead Table 16
𝑃SSD Fixed SSD draw 5 W
𝜙AWS Cloud PUE 1.2
Table 16: EC2 instances retained for A WS node power esti-
mation.
Instance Arch vCPU RAM [GB]𝑃 pkg [W]𝑃 RAM [W]𝛿[W]𝑃 pct100 [W]
m6i.2xlarge x86 8 32 38.20 19.20 7.50 64.90
m6i.4xlarge x86 16 64 76.39 38.40 15.00 129.79
r6i.2xlarge x86 8 64 38.20 38.40 7.50 84.10
r6i.4xlarge x86 16 128 76.39 76.80 15.00 168.19
r6g.2xlarge ARM 8 64 19.10 38.40 3.75 61.20
r6g.4xlarge ARM 16 128 38.20 76.80 7.50 122.50
m7g.2xlarge ARM 8 32 12.50 19.20 3.80 35.50
m7g.4xlarge ARM 16 64 25.00 38.40 7.50 70.90
Table 17: Variables in the non-A WS cloud equation (Equa-
tion(3)).
Symbol Definition Value
𝑊𝑚 Per-vCPU max wattage Tables 18, 19
𝑀Provider microarchitectures Table 20
𝑛vCPU,𝑛 RAM,𝑛 SSD Role-based minima Table 5
𝛽RAM RAM coefficient 0.6 W GB −1
𝛽SSD SSD coefficient 1.2 W TB −1
𝜙non-AWS Cloud PUE 1.185
Table 18: Hyperscaler per-vCPU wattage.
Provider𝑊 𝑚 [W/vCPU]
GCP 4.26
Azure 3.76
Table 19: SPECpower-derived microarchitecture wattage [98].
Microarchitecture𝑊 𝑚 [W/vCPU]
EPYC 1st Gen 2.6042
EPYC 2nd Gen 1.6930
EPYC 3rd Gen 1.9573
EPYC 4th Gen 2.2822
EPYC 5th Gen 8.9614
Cascade Lake 4.0632
Ice Lake 3.7582
Sapphire Rapids 4.1605
Skylake 4.1042
Table 20: CPU microarchitectures per hosting provider (set
𝑀in Equation(3)).
Provider CPU Microarchitectures Sources
Hetzner EPYC 2nd, 3rd, 4th Gen Hetzner Online GmbH [50, 51]
OVH EPYC 3rd, 4th Gen; Cascade
Lake; Sapphire Rapids
OVHcloud [79], OVHcloud US
[80]
Contabo EPYC 2nd, 4th, 5th Gen Contabo GmbH [17, 18]
Netcup EPYC 2nd, 4th, 5th Gen netcup GmbH [75]
DigitalOcean Skylake; Cascade Lake; Ice Lake;
Sapphire Rapids; EPYC 2nd, 3rd
Gen
DigitalOcean, LLC [26, 27]
Vultr Cascade Lake; EPYC 2nd, 3rd
Gen
Vultr Holdings LLC [104, 105]
Linode EPYC 1st, 2nd, 3rd Gen Akamai Technologies (Linode)
[2]
Leaseweb Cascade Lake; Sapphire Rapids;
EPYC 2nd, 3rd Gen
LeaseWeb Netherlands B.V.
[64, 65]
Clouvider Cascade Lake; EPYC 3rd Gen Clouvider Ltd [16]
Latitude EPYC 3rd, 4th, 5th Gen Latitude.sh [62, 63]
Oracle EPYC 3rd, 4th, 5th Gen Oracle Corporation [78]
11

Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, and Moritz Schubotz
B Hold-out scatter
Figure 3: Predicted versus rule-based power on 622 held-out
nodes when the fields that define a rule label are visible.
C Light-client bound
A Raspberry Pi Zero 2W [89] was metered idle (27 July) and under
Helios (30 July), six hours each. Helios is a light client: it checks
headers against remote consensus signatures and queries execu-
tion over RPC, and it does not store local chain state [1, 35]. The
board could not compile Helios; the binary was cross-compiled for
aarch64. Idle mean power is 0.83 W and Helios is 0.84 W (Figure 4).
The 0.01 W extra draw is the cost of a remote-RPC light client, not
of an ARM full node, and sits an order of magnitude below the 10 W
ARM Linux full-node assignment [1, 35, 107].
Figure 4: Raspberry Pi Zero 2W power over two six-hour
windows: (a) idle and (b) Helios.
D Subnet subscription counts
Table 21: Sync-committee subnet subscriptions.
syncnets_numNodes Share [%]
0 2,457 79.0%
1 139 4.5%
2 67 2.2%
3 34 1.1%
4 413 13.3%
Total 3,110 100.0%
Table 22: Attestation subnet subscriptions.
attnets_numNodes Share [%]
0 32 1.0%
2 2,602 83.7%
3 5 0.2%
4 190 6.1%
64 281 9.0%
Total 3,110 100.0%
12
