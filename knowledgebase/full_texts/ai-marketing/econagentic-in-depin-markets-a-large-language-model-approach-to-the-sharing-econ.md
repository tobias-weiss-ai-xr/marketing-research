---
title: 'EconAgentic in DePIN Markets: A Large Language Model Approach to the Sharing Economy of Decentralized
  Physical Infrastructure'
url: https://arxiv.org/abs/2508.21368
category: ai-marketing
subcategory: empirical
date: 2025-08
venue: ''
authors:
- Yulin Liu
- Mocca Schweitzer
source: arxiv
pdf_url: https://arxiv.org/pdf/2508.21368
pages: 11
chars: 48773
fetched_at: '2026-11-08T13:18:29+00:00'
kb_version: 1
---

# EconAgentic in DePIN Markets: A Large Language Model Approach to the Sharing Economy of Decentralized Physical Infrastructure

EconAgentic in DePIN Markets: A Large Language Model
Approach to the Sharing Economy of Decentralized Physical
Infrastructure
Yulin Liu∗
Quantum Economics
Zug, Switzerland
Mocca Schweitzer
Quantum Economics
Zug, Switzerland
ABSTRACT
The Decentralized Physical Infrastructure (DePIN) market is revo-
lutionizing the sharing economy through token-based economics
and smart contracts that govern decentralized operations. By 2024,
DePIN projects have exceeded $10 billion in market capitalization,
underscoring their rapid growth. However, the unregulated nature
of these markets, coupled with the autonomous deployment of
AI agents in smart contracts, introduces risks such as inefficien-
cies and potential misalignment with human values. To address
these concerns, we introduce EconAgentic, a Large Language Model
(LLM)-powered framework designed to mitigate these challenges.
Our research focuses on three key areas: 1) modeling the dynamic
evolution of DePIN markets, 2) evaluating stakeholders’ actions and
their economic impacts, and 3) analyzing macroeconomic indicators
to align market outcomes with societal goals. ThroughEconAgentic,
we simulate how AI agents respond to token incentives, invest
in infrastructure, and adapt to market conditions, comparing AI-
driven decisions with human heuristic benchmarks. Our results
show that EconAgentic provides valuable insights into the efficiency,
inclusion, and stability of DePIN markets, contributing to both aca-
demic understanding and practical improvements in the design and
governance of decentralized, tokenized economies.
KEYWORDS
Decentralized Physical Infrastructure, Autonomous AI Agents, Token-
based Economics, Multi-agent Systems, DePIN Market Simulation,
AI-driven Decision-making, Tokenomics, Smart Contracts, Large
Language Models, Economic Incentives
1 INTRODUCTION
The introduction of blockchain technology has been transformative
across various sectors [ 17], notably in finance, where it ensures
secure and transparent financial transactions [21], and in supply
chain management, where it facilitates greater traceability and
efficiency [3]. Diverging from these applications, the concept of
Decentralized Physical Infrastructure Networks (DePIN) emerges
as a particularly innovative use of blockchain in managing physical
infrastructures. DePIN employs blockchain technology to manage
crucial systems such as decentralized wireless networks, cloud com-
puting platforms, and distributed storage solutions, introducing
sector-specific innovations like Helium’s network1, Render’s plat-
form2, and Filecoin’s storage3 that disrupt traditional centralized
∗Corresponding author. Email: yulin@quantecon.ai.
1https://www.helium.com/
2https://render.com/
3https://filecoin.io/
models and improve infrastructure management across various sec-
tors [5]. Unlike traditional systems, where management often relies
on centralized hubs—such as control centers for electricity grids or
operational headquarters for public transportation—which can act
as bottlenecks or single points of failure, DePIN introduces a more
resilient and democratic approach to infrastructure management.
As of 2024, the traction for DePIN is evident, with market capital-
izations exceeding $10 billion and even over $30 billion in May 2024,
according to CoinMarketCap4 and DePINscan5. This substantial
growth reflects a significant shift toward decentralization, promis-
ing to address the inefficiencies and vulnerabilities inherent in
centralized systems and aligning with the foundational principles
of Web3.
The Decentralized Physical Infrastructure (DePIN) market is
transforming the sharing economy by decentralizing physical as-
sets and incentivizing node providers through token-based eco-
nomics. Central to the DePIN ecosystem are smart contracts that
autonomously govern market operations and interactions. Increas-
ingly, AI agents—referred to as Agentic [20]—are being deployed
within these smart contracts, enabling decision-making processes
and infrastructure management without human intervention. By
2024, the market capitalization of DePIN-related projects has sur-
passed $10 billion, reflecting significant popularity and investment.
As the DePIN market scales, the potential for widespread adoption
of these autonomous AI agents offers significant promise for effi-
ciency and innovation in resource allocation and decentralized in-
frastructure management. Despite the growing interest and invest-
ment in DePIN, academic research on this topic is limited. Existing
studies primarily concentrate on the technical aspects of blockchain
and decentralized systems [7], neglecting the distinct characteristics
and economic effects of DePIN [15]. Moreover, despite this growth,
there is a notable lack of academic research on DePIN’s founda-
tional aspects and economic impact. The unregulated nature of
decentralized markets and the autonomous operation of AI agents
within DePIN systems pose risks that could lead to unexpected neg-
ative consequences. Without proper analysis and governance, these
systems may inadvertently produce outcomes that conflict with
societal values, leading to inefficiencies or unintended harms [1, 2].
1.1 Unique Challenges in DePIN Research and
Development
The research and development of Decentralized Physical Infrastruc-
ture Networks (DePIN) face a number of critical challenges that
remain largely unexplored due to the lack of comprehensive models.
4https://coinmarketcap.com/view/DePIN/
5https://DePINscan.io/
arXiv:2508.21368v1  [econ.GN]  29 Aug 2025

Conference’17, July 2017, Washington, DC, USA Liu
Currently, no general model exists to capture the full complexity
of these decentralized markets and their evolving dynamics, which
makes it difficult to ensure that DePIN outcomes align with societal
goals and human values. The absence of such a model leaves a sig-
nificant gap between industry practices and the scientific inquiry
needed to rigorously analyze and design DePIN systems. Below, we
outline three major challenges:
a. Modeling Dynamic Market Evolution: Capturing DePIN’s
market evolution, from inception to large-scale adoption, re-
mains a challenge. Current models either isolate phases or lack
detail to account for feedback loops and nonlinear growth.
A comprehensive model for both micro and macro levels is
needed.
b. Identifying Stakeholders and Modeling Interactions: De-
PIN markets involve diverse stakeholders with unique incen-
tives. Modeling their interactions is key to understanding mar-
ket outcomes. A systematic approach is needed to reflect in-
dustry practices while providing theoretical abstraction for
stakeholder dynamics.
c. Macroeconomic Measurement and Value Alignment: Tra-
ditional metrics don’t capture the decentralized nature of DePIN
markets or their alignment with goals like efficiency, inclu-
sion, and stability. A new framework grounded in real-world
practices is needed to assess how market outcomes align with
societal values.
1.2 Our Contributions: The EconAgentic
Framework
Figure 1: Contributions.
To bridge these gaps, we introduceEconAgentic, a comprehensive
framework designed to empower both academic researchers and
industry practitioners to understand, analyze, and design DePIN
markets in ways that ensure their outcomes align with human
values. Our framework is both grounded in industry practices and
capable of abstracting scientific inquiry at the micro and macro
levels. As in Figure 1, the key contributions of EconAgentic are as
follows:
a. Dynamic Market Evolution Modeling: EconAgentic pro-
vides a novel methodology for modeling the dynamic evolution
of DePIN markets, from their inception to large-scale adop-
tion. Our approach accounts for market fluidity, stakeholder be-
haviors, technological advances, and regulatory changes. This
model is industry-informed but also designed to abstract core
principles that govern market growth and feedback loops, al-
lowing for both practical application and scientific exploration.
b. Stakeholder Modeling and Interaction Framework: We
propose a systematic approach to identifying and modeling the
key stakeholders in the DePIN market and their interactions.
EconAgentic allows us to analyze the actions of individual
stakeholders and the aggregated impact of their behaviors on
the overall market. Our framework balances industry realities
with the ability to abstract stakeholder dynamics into a form
suitable for scientific inquiry, facilitating better market design
and alignment with societal goals.
c. Macroeconomic Metrics for Human Value Alignment:
EconAgentic introduces new macroeconomic measurement
tools designed specifically for DePIN markets. These tools are
grounded in industry practice but abstracted to assess aggre-
gate market outcomes at a high level, ensuring alignment with
human values such as fairness, sustainability, and equity. This
novel measurement framework enables policymakers and in-
dustry practitioners to guide DePIN markets toward socially
beneficial outcomes.
In summary,EconAgentic provides a much-needed framework for
bridging the gap between industry practices and scientific research
in the context of DePIN markets, while addressing the unique chal-
lenges these markets present. Our framework is designed to enable
a rigorous analysis and design of DePIN systems that prioritize
alignment with human values at both micro and macro levels.
The rest of the paper is organized as follows: Section 2 provides
an overview of DePIN markets and models their dynamic evolution.
Section 3 introduces stakeholder dynamics and presents an LLM
agent-based framework for modeling interactions. Section 4 focuses
on the visualization and analysis of macroeconomic indicators in
DePIN markets. Section 5 discusses related work and suggests di-
rections for future research. The appendix details the data, with
an emphasis on geospatial heat maps for managing decentralized
infrastructure networks.
2 BACKGROUND AND MODELING OF DEPIN
MARKETS
In this section, we elaborate on how DePIN advances over central-
ized physical infrastructure (CePIN), the taxonomy of DePIN, and
the dynamic evaluation of DePIN markets through different growth
stages.
2.1 The DePIN Advances and Taxonomy
Decentralized Physical Infrastructure Networks (DePIN) offer a
transformative approach to managing real-world infrastructure
by leveraging blockchain technology and decentralization prin-
ciples [10]. This shift decentralizes not only service distribution
but also the underlying infrastructure layer that coordinates eco-
nomic activities. DePIN builds upon the success of the sharing

EconAgentic in DePIN Markets Conference’17, July 2017, Washington, DC, USA
Figure 2: CePIN vs. DePIN.
economy models, like Uber and Airbnb, by decentralizing the plat-
forms themselves. In DePIN ecosystems, networks of IoT-enabled
devices facilitate real-time data exchange and operational decisions,
making them smarter and more interconnected [9, 18].
As shown in Figure 2, the transition from centralized physi-
cal infrastructure (CePIN) to decentralized models (DePIN) intro-
duces significant advantages across various operational metrics.
For instance, DePIN reduces capital expenditure by utilizing crowd-
sourced, commoditized hardware instead of proprietary equipment.
Labor costs are lowered by enabling simplified, DIY installation of
hardware, which contrasts with the labor-intensive setups required
in traditional networks. Maintenance and operation costs are min-
imized through decentralized automation and warranty-backed
hardware, while real estate and operational expenses are reduced
by allowing participants to host hardware on their own premises.
Most notably, DePIN offers global market access and flexibility,
breaking free from the geographical constraints and monopolies
that often limit centralized networks.
This evolution in infrastructure management brings us to the
various types of DePIN projects. As outlined in Table 1, DePIN
projects can be classified based on the type of physical infrastructure
they decentralize. These categories include:
• Server: Networks that distribute and manage server re-
sources for hosting applications and services across decen-
tralized nodes (e.g., Render on Solana).
• Wireless: Networks that enhance wireless communication
coverage and resilience using decentralized nodes (e.g., He-
lium on Solana).
• Sensor: Networks that manage IoT and sensor data across
decentralized nodes for improved security and integrity (e.g.,
Hivemapper on Solana).
• Compute: Networks that distribute computational resources
for scalable data processing (e.g., Nosana on Ethereum).
• Energy: Networks that support localized energy manage-
ment and peer-to-peer trading (e.g., Arkreen).
Beyond individual projects, DePIN can be divided into two over-
arching types: Physical Resource Networks (PRN) and Digital
Resource Networks (DRN) [11]. PRNs, such as DIMO6, focus
on physical assets like vehicles, where participants earn tokens
6https://DePINhub.io/projects/dimo
Table 1: Categories of DePIN and their Representative Prod-
ucts
Name Definition Project (Blockchain)
✌ Server
Networks distribute and man-
age server resources for host-
ing applications and services
across decentralized nodes.
Render
(Solana)
▲ Wireless
Decentralized nodes improve
coverage and resilience, avoid-
ing central points of failure in
communications.
Helium
(Solana)
✎ Sensor
Networks enhance the man-
agement of IoT and sen-
sor data across decentralized
nodes for improved security
and integrity.
Hivemapper
(Solana)
■ Compute
Networks distribute computa-
tional resources for scalable
data processing across multi-
ple decentralized nodes.
Nosana
(Ethereum)
✳ Energy
Networks support localized
energy management and peer-
to-peer trading, promoting en-
ergy independence.
Arkreen
by contributing data. DRNs, like Akash7, allow users to rent out
unused digital resources such as cloud computing power.
This taxonomy underscores the versatility of DePIN in managing
both physical and digital resources, demonstrating the wide array
of applications and the potential for increased efficiency, resilience,
and security across various industries. As we analyze the evolution
of these projects, it is evident that DePIN’s scalability depends on
careful planning across different growth stages.
2.2 DePIN Market Evolution Dynamics
The evolution of a DePIN project follows distinct stages, from its
inception to widespread adoption. These stages can be characterized
as: Inception (Stage 0), Initial Launch and Scaling (Stage 1) ,
and Exponential Growth and Widespread Adoption (Stage∞)
as in Figure 3. Each stage introduces unique stakeholders, specific
actions, and measurable impacts on the project’s development and
network growth.
2.2.1 Stage 0: Inception – Conceptualization and Fundraising. At
the inception stage, the core stakeholders include:
i. Core Team/Developers: These individuals are responsible
for defining the technical vision and building the founda-
tional infrastructure of the DePIN project.
ii. Early Investors (VCs, Angels) : These investors provide
the initial capital needed to bootstrap the project.
The key action at this stage isfundraising. For example, Helium
raised $53 million in a Series C funding round led by Andreessen
7https://akash.network/

Conference’17, July 2017, Washington, DC, USA Liu
Figure 3: DePIN Market Evolution Dynamics
Horowitz in 20218, while Render Network raised $30 million from
Multicoin Capital9. For simplicity, we assume the project raises $10
million in a single venture capital round.
Half of the raised funds ($5 million) are allocated to development
and operations, while the other $5 million is used to deploy the
initial network nodes. Setup costs can vary significantly, ranging
from $500 to $1,000 for a Helium Hotspot miner 10 to $5,000 to
$20,000 for Render Network’s GPU-based nodes 11. Assuming a
cost of $100,000 per node, the project deploys 50 nodes with the
allocated budget.
From a theoretical standpoint, Metcalfe’s Law explains the ex-
ponential growth in network value. The value 𝑉 of the network
is proportional to the square of the number of connected nodes
𝑛 (𝑉 ∝ 𝑛2)12. With 50 nodes, the DePIN network offers baseline
services, establishing the first network effect, where the utility of
the network grows with the number of connected nodes.
2.2.2 Stage 1: Initial Launch and Scaling. As the project moves
from inception to launch, additional stakeholders emerge:
i. Core Team/Developers: Continue expanding and refining
the network infrastructure.
ii. Early Adopters and Node Operators : These participants
operate the network’s nodes, contributing to operations
while earning rewards.
iii. Growth Capitalists (GCs): New investors who enter the
market by purchasing tokens, supporting liquidity and ex-
pansion.
In this phase, tokenomics become critical for sustaining growth.
Real-world examples such as Helium and Filecoin typically allocate
between 15% and 25% of tokens to early investors, with vesting
schedules to prevent early sell-offs 13. Node operators also earn
revenue through network transaction fees. For example, Helium’s
IoT network charges usage-based fees, providing an additional rev-
enue stream14. As more nodes join, the network effect strengthens,
8https://techcrunch.com/2021/08/10/helium-raises-53m-series-c-led-by-andreessen-
horowitz/
9https://cryptoslate.com/render-network-raises-30-million/
10https://www.helium.com/
11https://rendertoken.com/
12https://infoworld.com/article/2973672/metcalfes-law.html
13https://docs.filecoin.io/
14https://www.helium.com/using-the-network
creating a positive feedback loop, where more participants increase
the utility and growth of the network.
2.2.3 Stage ∞: Exponential Growth and Widespread Adoption. At
this stage, the DePIN network reaches a critical mass, entering
a phase of self-sustaining, autonomous growth. The network’s
infrastructure and tokenomics, established in earlier stages, allow
it to operate with minimal external intervention. The following key
dynamics drive this stage:
i. Growth Capitalists (GCs) : These investors continue to
provide liquidity, which stabilizes the token’s market price
and ensures the availability of capital for future expansion.
ii. End Users: The general public and businesses begin using
the network at scale, significantly increasing transaction
volumes and enhancing the network’s utility.
At this stage, network autonomy becomes critical. Governance
mechanisms and smart contracts guide the ecosystem’s evolution,
while decentralized decision-making ensures the network can adapt
and grow without centralized control. This allows the network to
continue expanding through a self-sustaining feedback loop.
As predicted byMetcalfe’s Law, the network’s value grows quadrat-
ically with the number of nodes and users. For example, Helium
had expanded to over 800,000 hotspots globally by 2023, provid-
ing decentralized IoT services15. Similarly, Render connects global
users with GPU operators, enabling scalable compute power for
tasks such as 3D rendering and machine learning16.
In summary, ecosystem stability and autonomous growth
are key in Stage∞. The network reaches maturity, where stake-
holders, including node operators and token holders, interact seam-
lessly. The decentralized infrastructure now operates autonomously,
driven by the incentives and governance structures set in earlier
stages.
This autonomous growth necessitates strong stakeholder inter-
actions and efficient frameworks to manage complex operations
within a decentralized environment. In the next section, we delve
into Stakeholder Dynamics and the LLM Agent-Based Frame-
work, exploring how artificial intelligence and decentralized agents
facilitate these interactions.
3 STAKEHOLDER DYNAMICS AND LLM
AGENT-BASED FRAMEWORK
In this section, we introduce a general agent-based framework
for analyzing stakeholder behaviors within Decentralized Physical
Infrastructure Networks (DePIN). This framework allows for the
simulation of various stakeholder types, including node providers,
venture capitalists (VCs), growth capitalists (GCs), and end users.
The model evaluates stakeholders’ behaviors using either heuristic-
based or LLM-based agents and assesses their impact on network
growth, token economy dynamics, and market stability. The frame-
work is generalizable across different types of stakeholders, and by
comparing simple heuristic-based agents with more complex LLM-
based agents, we gain insights into how decision-making strategies
influence the overall ecosystem.
15https://explorer.helium.com/
16https://rendertoken.com/

EconAgentic in DePIN Markets Conference’17, July 2017, Washington, DC, USA
3.1 Token Distribution
The total token supply is fixed at𝑇total = 1, 000, 000, 000 tokens and
is allocated among three key stakeholders: the core team, venture
capitalists (VCs), and node providers. The allocation is governed by
vesting schedules that ensure long-term engagement and alignment
with network growth. The total supply is divided as follows:
𝑇total =𝑇team+𝑇vc+𝑇node
where:
𝑇team = 0.20×𝑇total, 𝑇 vc = 0.20×𝑇total, 𝑇 node = 0.60×𝑇total
The distribution follows specific vesting schedules for each group
of stakeholders:
• Core Team (20%) : The core team receives 20% of the to-
tal token supply. The team’s tokens are subject to a 4-year
vesting period with a 1-year cliff, meaning:
– No tokens are distributed in the first 11 months (cliff pe-
riod).
– At the end of Month 12 (end of the cliff), 25% of the allo-
cated tokens are distributed.
– The remaining 75% are vested monthly over the following
36 months.
• Venture Capitalists (VCs) (20%): VCs receive 20% of the
total supply, following a 2-year vesting period with a 1-year
cliff:
– No tokens are distributed in the first 11 months.
– At the end of Month 12, 50% of the VC allocation is dis-
tributed.
– The remaining 50% is distributed monthly over the second
year (Months 13–24).
• Node Providers (60%) : Node providers are allocated 60%
of the total token supply. Their tokens are distributed over
multiple periods, with a halving mechanism every 4 years:
– In the first 4 years (Months 1–48), 50% of the node provider
allocation is distributed equally every month.
– In the next 4 years (Months 49–96), 25% of the total alloca-
tion is distributed, with the monthly distribution halved
compared to the first period.
– So on and so forth.
The token vesting schedule ensures that incentives are aligned
with long-term participation in the network. The precise distri-
bution of tokens to each stakeholder group is illustrated in Fig-
ure 4, showing the vesting periods and halving mechanism for
node providers.
3.2 Simulation Model for Stakeholder Dynamics
The stakeholder simulation is based on an agent-based model that
evaluates the behavior of various participants in the DePIN ecosys-
tem. This model captures interactions between node providers,
venture capitalists, growth capitalists, and end users, using both
heuristic-based and LLM-based strategies.
3.2.1 Node Provider Behavior. The model simulates the entry and
exit of node providers based on profitability. The profitability at
time𝑡, denoted𝜋node(𝑡), is calculated as the difference between the
global estimated revenue𝑅global(𝑡) and the operating cost 𝐶node
Figure 4: Token distribution schedules for the core team, VCs,
and node providers.
for each active node. The formula is given by:
𝜋node(𝑡) =
𝑅global(𝑡)
𝑛(𝑡) −𝐶node
where𝑛(𝑡) is the number of active nodes at time 𝑡. If a node’s
profitability exceeds a certain threshold, it remains in the system;
otherwise, it exits.
3.2.2 Global Estimated Revenue. The total revenue generated by
the network,𝑅global(𝑡), is influenced by the number of users𝑈(𝑡),
the number of active nodes 𝑛(𝑡), and the token price 𝑃(𝑡). The
number of users𝑈(𝑡) is a function of the number of active nodes,
modeled as:
𝑈(𝑡) = 100×
√︂
𝑛(𝑡)·( 𝑛(𝑡)− 1)
2
The global estimated revenue𝑅global(𝑡) is then computed as:
𝑅global(𝑡) = 𝑃(𝑡− 1)· 𝑇node(𝑡) 𝑛(𝑡− 1) +𝑘·𝑈(𝑡)
where𝑇node(𝑡) is the number of tokens issued to node providers,
and𝑘 is a scaling factor for user-related revenue.
3.2.3 Growth Capital Dynamics. Growth capitalists receive endow-
ments𝐸gc, with lifespans𝐿gc drawn from a log-normal distribution.
The total endowment at time𝑡,𝐸total(𝑡), is the sum of the endow-
ments from active growth capitalists:
𝐸total(𝑡) =
∑︁
gc active at 𝑡
𝐸gc
Growth capitalists exit after their lifespan𝐿gc, and ther tokens are
sold to the market, influencing the number of tokens on sale.
3.2.4 Token Price and Market Capitalization. The token price𝑃(𝑡)
is determined by the ratio of the total growth capital endowment
to the tokens on sale at time𝑡:
𝑃(𝑡) = 𝐸total(𝑡) Tokens on Sale(𝑡)
Market capitalization𝑀(𝑡) is then calculated as the product of the
token price and the circulating supply:
𝑀(𝑡) =𝑃(𝑡)× Circulating Supply(𝑡)

Conference’17, July 2017, Washington, DC, USA Liu
The fully diluted market capitalization, which accounts for the
entire token supply, is given by:
𝑀diluted(𝑡) =𝑃(𝑡)× 𝑇total
3.2.5 Simulation Process. The simulation spans 96 months. At each
time step𝑡, the following updates are performed:
• Active nodes𝑛(𝑡) and users𝑈(𝑡) are updated based on node
participation.
• Node provider revenue𝑅global(𝑡), costs𝐶node(𝑡), and profits
𝜋node(𝑡) are calculated.
• Growth capitalists enter or exit based on𝐿gc.
• Token price𝑃(𝑡), market capitalization𝑀(𝑡), and stability
𝜎log-returns(𝑡) are adjusted.
The simulation outputs key metrics, including token price𝑃(𝑡),
market cap𝑀(𝑡), and network participation over time, providing
insight into system dynamics.
3.3 Heuristic and LLM-Based Agents
We compare two types of agents:
(1) Heuristic-Based Agents: These agents rely on predefined
rules to make decisions. For node providers, a node enters
the system if the global estimated revenue𝑅global(𝑡) exceeds
its cost𝐶node, and exits if the revenue falls below a tolerance
threshold.
(2) LLM-Based Agents: These agents use Large Language Mod-
els (LLMs) to make decisions based on contextual prompts.
LLM-based agents provide more nuanced decision-making
by considering broader market conditions and trends.
3.3.1 Heuristic Node Provider Agent. The heuristic node provider
agent follows a rule-based approach:
• Node Entry: A node enters if𝑅global(𝑡) >𝐶node.
• Node Exit: A node exits if𝑅global(𝑡) <𝜏node×𝐶node, where
𝜏node is the node’s risk tolerance.
The pseudocode for the heuristic-based node provider agent is
as follows:
For each month𝑡 :
a. For each node:
if𝑅global(𝑡) >𝐶node, add node.
if𝑅global(𝑡) <𝜏node×𝐶node, remove node.
Update node count and calculate new revenue.
3.3.2 LLM-Based Node Provider Agent. The LLM-based agent pro-
vides more context-aware decisions. It generates responses based
on natural language prompts to make entry or exit decisions. For
example, the decision to enter might depend on a prompt like:
"The global estimated revenue is𝑅global. A node has
a cost of 𝐶node. Should the node enter the system?
Please answer ’yes’ or ’no’. "
Similarly, the decision to exit might depend on a prompt such as:
"The global estimated revenue is𝑅global. A node has
a cost of𝐶node and a tolerance of 𝜏node. Should the
node exit the system? Please answer ’yes’ or ’no’. "
4 VISUALIZATION AND ANALYSIS OF
MACROECONOMIC INDICATORS IN DEPIN
MARKETS
In this section, we analyze key macroeconomic indicators to assess
the performance of Decentralized Physical Infrastructure Networks
(DePIN) markets. We focus on three critical dimensions:Efficiency,
Inclusion, and Stability. These measures offer valuable insights
into the economic value, decentralization, and resilience of De-
PIN markets. Table 2 presents the top 10 DePIN tokens by market
capitalization as of May 28, 2024, highlighting key data such as
token price, market capitalization, and 24-hour trading volume.
The metrics for efficiency, inclusion, and stability are derived from
industry-standard practices, providing a comprehensive framework
for evaluation.
Table 2: Top 10 DePIN Tokens by Market Cap. Data ex-
tracted on May 28, 2024, from CoinMarketCap (https://
coinmarketcap.com/view/depin/).
Name Price Market Cap Volume (24h)
Internet Com-
puter (ICP) $12.13 $5,631,971,226 $92,320,912
Render (RNDR) $10.24 $3,980,572,572 $236,206,486
Filecoin (FIL) $5.94 $3,310,041,671 $201,176,245
Bittensor (TAO) $416.51 $2,850,998,994 $30,304,854
Arweave (AR) $37.98 $2,486,050,282 $105,864,760
Theta Network
(THETA) $2.27 $2,274,255,874 $29,805,885
Akash Network
(AKT) $5.23 $1,247,039,844 $19,040,451
BitTorrent (BTT) $1.19 ×10−6 $1,152,552,225 $28,933,320
MultiversX
(EGLD) $39.96 $1,078,774,444 $30,160,556
AIOZ Network
(AIOZ) $0.7824 $858,001,031 $9,057,703
4.1 Measures
4.1.1 Efficiency. The Efficiency of a DePIN market is measured
by its market capitalization, representing the economic value gen-
erated by the network. Mathematically, we define efficiency as the
market capitalization𝐸eff, which is given by:
𝐸eff =𝑁circ×𝑃token
Where:
• 𝑁circ is the number of circulating tokens.
• 𝑃token is the current token price.
Efficiency, represented as𝐸eff, reflects the total economic value
of the network based on the available token data in Table 2. Higher
market capitalization implies a more economically efficient net-
work.

EconAgentic in DePIN Markets Conference’17, July 2017, Washington, DC, USA
4.1.2 Inclusion. The Inclusion of a DePIN market refers to the
degree of decentralization and the participation of external node
providers. It is critical to evaluate how much of the network’s
infrastructure is controlled by external participants versus the core
team. We represent inclusion using the symbol𝐼inc, defined as:
𝐼inc = 𝑁ext 𝑁total = 𝑁total−𝑁init 𝑁total
Where:
• 𝑁ext is the number of nodes operated by external providers.
• 𝑁total is the total number of nodes in the network.
• 𝑁init is the number of nodes initially set up by the core team.
The inclusion parameter𝐼inc measures the proportion of total
nodes operated by external participants. A higher value of 𝐼inc
indicates greater decentralization and participation by external
stakeholders. This parameter often requires more technical efforts
to measure, as node provider data may not be as publicly accessible
as token data.
4.1.3 Stability. Stability refers to the volatility of the token price
in the DePIN market. Stability is an essential metric for assessing
the resilience of the network, as highly volatile token prices may
signal instability and risk for investors. We calculate stability𝑆stab
based on the volatility of token price returns over a specific time
period, following the conventional approach of measuring price
volatility.
The stability𝑆stab is given by the standard deviation of the loga-
rithmic returns of the token price:
𝑆stab =𝜎log-returns =
vut
1
𝑁− 1
𝑁∑︁
𝑖=1

ln
 𝑃𝑖
𝑃𝑖−1

− ¯𝑟
2
Where:
• 𝑃𝑖 is the token price at time𝑖,
• ln
 𝑃𝑖
𝑃𝑖−1

represents the logarithmic return from time𝑖− 1
to time𝑖,
• ¯𝑟 is the average logarithmic return over the observed time
period,
• 𝑁 is the total number of observations.
Lower values of𝑆stab indicate less price volatility and thus greater
stability, which is desirable for long-term network growth and
sustainability.
4.2 Simulation and Results
In our simulation, we utilized the open-source EleutherAI/gpt-
neo-125M language model17 as the decision-making agent within
the DePIN economic environment. A key variable in this model is
the patience parameter, which governs the number of consecutive
signals required for a node to exit the system, thus representing
varying levels of risk tolerance. We evaluated LLM strategies with
different patience levels and compared them against a heuristic-
based benchmark.
Figure 5 illustrates the impact of patience on three critical mea-
sures: inclusion, stability, and efficiency. Inclusion increases with
17https://huggingface.co/EleutherAI/gpt-neo-125M
higher patience, as nodes are retained in the system longer, allow-
ing for more favorable market conditions to emerge. This results
in a more inclusive network with fewer premature exits. Similarly,
stability improves with greater patience, as nodes become less
sensitive to short-term market fluctuations, leading to reduced
volatility and smoother system behavior. Although higher patience
might theoretically reduce efficiency by keeping non-viable nodes
in the system longer, the results show that market capitalization
continues to grow across all strategies, indicating that enhanced
stability and inclusion do not significantly compromise overall
efficiency.
The observed outcomes suggest that LLMs with higher patience
are more effective at mitigating short-term volatility, promoting
decisions that align with long-term trends. This behavior enhances
both inclusion and stability without incurring substantial efficiency
losses. Additional visualizations are provided in the appendix.
5 RELATED WORK AND FUTURE RESEARCH
This paper makes significant contributions to the study of Decen-
tralized Physical Infrastructure Networks (DePIN) by developing a
comprehensive framework that integrates Large Language Model
(LLM) agents to evaluate societal goals such as efficiency, inclusion,
and stability. Our framework provides a foundation for understand-
ing how stakeholder behaviors influence DePIN market dynamics
and establishes benchmarks for assessing the performance of LLM
agents in decentralized systems. The following subsections elabo-
rate on our contributions to different strands of the literature, with
distinct directions for future research.
5.1 Token Economy in DePIN
Chiu et al.[4] introduced a foundational framework for DePIN’s
token economy, focusing on token issuance as rewards and multi-
token models that distinguish between value and utility tokens.
Their work highlights how staking mechanisms can align short-
term behaviors with long-term goals by incentivizing participants
to lock tokens into the system. Liu and Zhang[14] further analyzed
token-based incentives in blockchain governance, demonstrating
how staking rewards based on duration can foster long-term par-
ticipation and stabilize decentralized governance systems.
Our Contribution: Our contribution lies in setting up a frame-
work that can evaluate the impact of token economies in DePIN
markets, particularly in terms of efficiency, inclusion, and stability.
While we do not explore specific token design choices like reward
structures or staking mechanisms, our framework enables future re-
searchers to assess how these elements influence market outcomes.
By focusing on these societal metrics, we provide a foundation for
deeper analysis of token economies in decentralized ecosystems.
Future Research Directions: Future work should utilize this
framework to examine how specific token mechanisms—such as
reward structures, staking models, and multi-token systems—affect
both individual behaviors (microeconomic outcomes) and overall
market performance (macroeconomic outcomes). Moreover, there
is potential to explore how token designs can be optimized to sup-
port broader societal goals, such as equitable resource distribution,
environmental sustainability, and ethical governance. Researchers

Conference’17, July 2017, Washington, DC, USA Liu
(a) Efficiency: higher values indicate greater
efficiency.
(b) Inclusion: higher values indicate more in-
clusiveness.
(c) Stability: lower values indicate higher sta-
bility.
Figure 5: Comparison of Efficiency, Inclusion, and Stability Across Models.
could extend our framework to incorporate fairness and ethics in
future evaluations.
5.2 LLM Agents in Economic Decision-Making
LLM agents have increasingly been applied to economic and finan-
cial decision-making processes. Li et al.[12] proposed EconAgent,
which uses LLMs to simulate macroeconomic activities and under-
stand complex market dynamics. Other studies, such as ALYMPICS[16]
and Ding et al. [6], explored how LLM agents can support strategic
decision-making in financial trading by analyzing vast amounts of
unstructured data and simulating trading scenarios.
Our Contribution: We contribute to this line of research by
applying LLM agents to DePIN markets, allowing for the simulation
and optimization of stakeholder decisions. Our framework enables
researchers to analyze how LLM-driven decisions influence key
metrics such as efficiency, inclusion, and stability within decentral-
ized, token-based markets. This unique application of LLM agents
provides new insights into how AI can support the sustainable
development of DePIN systems.
Future Research Directions: Future research should focus on
refining LLM agents to balance short-term economic incentives
with long-term network sustainability. Analyzing how LLM agents
can assist different stakeholders, such as node operators, venture
capitalists, and governance participants, will be essential for im-
proving decision-making processes in DePIN systems. Additionally,
extending the application of LLM agents to evaluate broader soci-
etal objectives, such as fairness, ethics, and long-term sustainability,
represents a promising area for further exploration.
5.3 Data and Benchmark for LLM
Our work introduces new benchmarks for evaluating LLM agents
in decentralized economic systems, particularly within the context
of DePIN markets. These benchmarks allow researchers to assess
how LLM agents perform in complex decision-making scenarios,
focusing on metrics like efficiency, inclusion, and stability. This
effort is inspired by previous benchmarks such as BIG-Bench[19],
MMLU[8], and AgentBench [13], which evaluate LLM capabilities
in different domains.
Our Contribution: We provide a set of benchmarks specifically
tailored to DePIN, focusing on societal metrics like efficiency, in-
clusion, and stability. These benchmarks offer a novel approach to
evaluating LLM agents in decentralized, tokenized ecosystems, pro-
viding a foundation for future research to assess the sustainability
of LLM-driven decisions.
Future Research Directions: Future research should extend
these benchmarks to explore how different LLM architectures and
training methods impact decision-making in decentralized systems.
Additionally, incorporating metrics for fairness, ethics, and long-
term societal goals will provide a more comprehensive evaluation
framework. Researchers could also examine how LLM agents man-
age trade-offs between short-term market dynamics and long-term
sustainability, further advancing the application of AI in decen-
tralized economies. Future studies could also consider including
empirical data for the training process to enhance the realism and
applicability of the models. Moreover, more elaboration and cases
on decentralized platform data characteristics are provided in the
appendix, offering additional insights into the complexities and
nuances of such data.

EconAgentic in DePIN Markets Conference’17, July 2017, Washington, DC, USA
REFERENCES
[1] Daron Acemoglu. 2021. Harms of AI. Oxford Handbook of AI Governance (2021).
https://www.nber.org/papers/w29247 Forthcoming.
[2] Daron Acemoglu and Pascual Restrepo. 2018. The race between man and machine:
Implications of technology for growth, factor shares, and employment. American
Economic Review 108, 6 (2018), 1488–1542. https://doi.org/10.1257/aer.20170672
[3] Shuchih E Chang and Yichian Chen. 2020. When blockchain meets supply chain:
A systematic literature review on current development and potential applications.
Ieee Access 8 (2020), 62478–62494.
[4] Michael T. C. Chiu, Sachit Mahajan, Mark C. Ballandies, and Uroš V. Kal-
abić. 2024. DePIN: A Framework for Token-Incentivized Participatory Sensing.
arXiv:2405.16495 [cs.GT]
[5] Cointelegraph. 2023. Decentralized Physical Infrastructure Network (De-
PIN), explained. https://cointelegraph.com/explained/decentralized-physical-
infrastructure-network-depin-explained. https://cointelegraph.com/explained/
decentralized-physical-infrastructure-network-depin-explained Accessed: 2024-
05-28.
[6] Han Ding, Yinheng Li, Junhao Wang, and Hang Chen. 2024. Large Language
Model Agent in Financial Trading: A Survey. arXiv preprint arXiv:2408.06361
(2024).
[7] Xinxin Fan and Lei Xu. 2023. Towards a Rollup-Centric Scalable Architecture for
Decentralized Physical Infrastructure Networks: A Position Paper. In Proceedings
of the Fifth ACM International Workshop on Blockchain-enabled Networked Sensor
Systems. 9–12.
[8] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn
Song, and Jacob Steinhardt. 2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300 (2020).
[9] Steve Huckle, Rituparna Bhattacharya, Martin White, and Natalia Beloff. 2016. In-
ternet of things, blockchain and shared economy applications. Procedia computer
science 98 (2016), 461–466.
[10] IoTeX IoTeX. 2018. a Decentralized Network for Internet of Things Powered by a
Privacy-Centric Blockchain. White Paper 1 (2018).
[11] Tintin Land. 2021. Before Scaling to Mass Adoption: How does
DePin Break Through Technology, Data, and Market? https:
//medium.com/@tintin.land2021/before-scaling-to-mass-adoption-how-
does-depin-break-through-technology-data-and-market-72f79243f76c.
https://medium.com/@tintin.land2021/before-scaling-to-mass-adoption-
how-does-depin-break-through-technology-data-and-market-72f79243f76c
Accessed: 2024-05-28.
[12] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. 2024. Econagent: large
language model-empowered agents for simulating macroeconomic activities.
In Proceedings of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers) . 15523–15536.
[13] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu,
Hangliang Ding, Kaiwen Men, Kejuan Yang, et al. 2023. Agentbench: Evaluating
llms as agents. arXiv preprint arXiv:2308.03688 (2023).
[14] Yulin Liu and Luyao Zhang. 2024. The Economics of Blockchain Governance: Eval-
uate Liquid Democracy on the Internet Computer.arXiv preprint arXiv:2404.13768
(2024).
[15] Katya Malinova and Andreas Park. 2023. Tokenomics: when tokens beat equity.
Management Science 69, 11 (2023), 6568–6583.
[16] Shaoguang Mao, Yuzhe Cai, Yan Xia, Wenshan Wu, Xun Wang, Fengyi Wang,
Tao Ge, and Furu Wei. 2023. Alympics: Language agents meet game theory.arXiv
preprint arXiv:2311.03220 (2023).
[17] Ahmed Afif Monrat, Olov Schelén, and Karl Andersson. 2019. A survey of
blockchain from the perspectives of applications, challenges, and opportunities.
Ieee Access 7 (2019), 117134–117151.
[18] Rodrigo Roman, Jianying Zhou, and Javier Lopez. 2013. On the features and
challenges of security and privacy in distributed internet of things. Computer
networks 57, 10 (2013), 2266–2279.
[19] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb,
Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, et al. 2022. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models. arXiv preprint arXiv:2206.04615
(2022).
[20] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yiwen Ding, Boyang Hong, Ming
Zhang, Junzhe Wang, Senjie Jin, Enyu Zhou, et al. 2023. The rise and potential
of large language model based agents: A survey. arXiv preprint arXiv:2309.07864
(2023).
[21] Luyao Zhang. 2023. The Future of Finance: Synthesizing CeFi and DeFi for the
Benefit of All. In Financial Literacy in Today´s Global Market, Ireneusz Miciuła
(Ed.). IntechOpen, Rijeka, Chapter 13. https://doi.org/10.5772/intechopen.1003042
A THE DATA
DePIN projects exhibit distinct characteristics that set them apart
from traditional infrastructure models. A key feature is the use of
geospatial heat maps to visualize the distribution of devices within
the network. These heat maps provide a dynamic and intuitive rep-
resentation of the physical locations and density of decentralized
nodes, such as servers, sensors, and wireless devices. By displaying
this data spatially, stakeholders can quickly identify areas of high
and low device concentration, facilitating more effective resource
allocation, maintenance planning, and network optimization. This
geospatial approach enhances transparency and monitoring capabil-
ities, supports strategic decision-making, and reveals patterns and
trends in device deployment across different geographic regions.
Consequently, geospatial heat maps are essential tools in managing
and expanding DePIN networks, offering a clear and comprehen-
sive overview of the network’s physical footprint. Several DePIN
projects provide explorers that include heatmaps of the geospatial
distribution of physical infrastructure networks. For instance, He-
lium provides a hotspot map displaying the distribution of wireless
communication nodes, accessible at the Helium Explorer 18.
Figure 6: Datacenter Density Heatmap.
The Internet Computer protocol, developed by Dfinity Founda-
tion, offers the detailed geospatial data of data center locations,
along with the number of active nodes and node providers in each
data center, available at the Internet Computer Dashboard 19. Based
on this data, we produce visualizations to illustrate the distribution
and density of data centers and node machines across different
continents. Figure 6 shows a heatmap of datacenter density, illus-
trating the concentration of datacenters around the globe, with
colors indicating the number of node machines in each location.
Figure 7 presents the percentage distribution of data centers across
different continents, with Europe having the highest number fol-
lowed by North America. It provides insight into how data centers
are geographically distributed among continents. Figure 8 epicts
the number of node machines distributed across various continents,
with North America and Europe having the highest numbers. It
highlights the distribution of computational resources represented
by node machines on different continents. Figure 9 shows the node
machines and data centers by Coutnries
18https://explorer.helium.com/
19https://dashboard.internetcomputer.org/centers

Conference’17, July 2017, Washington, DC, USA Liu
Figure 7: Data Centers by Continent
Figure 8: Node Machines by Continent
Another notable platform is DePINscan, which aggregates data
from sources like the W3bstream Trusted Metrics API and third-
party APIs to provide a comprehensive overview of DePIN projects.
Developers can submit their projects for review, and approved
projects are featured on the DePINscan explorer. The platform’s
API supports data integration, allowing the upload of device iden-
tifiers and geospatial coordinates (longitude and latitude). This
data populates the DePINscan world map, illustrating network
device distribution and aiding in understanding deployment pat-
terns. Explore the geospatial distribution of DePIN infrastructure
on DePINscan20. The major unique contribution of DePIN data lies
in extending the application of blockchain technology as a data
ledger for digital infrastructure from the purely digital domain to
the physical world [11]. This transformative approach allows for a
secure and transparent recording of geospatial data, bridging the
gap between virtual and real-world applications.
However, blockchain technology alone cannot ensure the au-
thenticity of the geospatial data reported onto the blockchain for
DePIN projects. Therefore, it is crucial to implement economic
mechanisms or tokenomics designs to incentivize all stakehold-
ers, including small businesses and entrepreneurs, to participate.
These economic incentives help lower initial costs, enhance effi-
ciency, optimize resource allocation, and reduce waste. Additionally,
20https://DePINscan.io/map-view
they improve the integrity of network participants by encouraging
honest reporting and active engagement in the ecosystem, thus
fostering a more reliable and efficient data ledger system.
In conclusion, the unique characteristics of DePIN data, particu-
larly the use of geospatial heat maps and blockchain technology,
offer significant advantages in managing and optimizing decentral-
ized networks. By leveraging these tools, stakeholders can assess
and enhance the performance metrics of DePIN networks, ensur-
ing efficient and reliable operation. The integration of economic
incentives would further strengthens the network by promoting
active and honest participation, ultimately leading to a more robust
and effective decentralized infrastructure.
Figure 9: Node Machines and Data Cetners by Countries
B ADDITIONAL VISUALIZATIONS
Figure 10: The Diluted Market Cap

EconAgentic in DePIN Markets Conference’17, July 2017, Washington, DC, USA
Figure 11: The Number of Nodes
Figure 12: The Number of Users
