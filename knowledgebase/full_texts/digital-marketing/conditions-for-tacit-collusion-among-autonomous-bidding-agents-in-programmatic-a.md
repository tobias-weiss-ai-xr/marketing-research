---
title: CONDITIONS FOR TACIT COLLUSION AMONG AUTONOMOUS BIDDING AGENTS IN PROGRAMMATIC ADVERTISING MARKETS
url: https://doi.org/10.62731/mcnd-17.04.2026.001
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Igor Ivitskiy
source: openalex-oa
pdf_url: https://archives.mcnd.org.ua/index.php/conference-proceeding/article/download/1547/1684
pages: 3
chars: 5833
fetched_at: '2026-11-08T17:20:18+00:00'
kb_version: 1
---

# CONDITIONS FOR TACIT COLLUSION AMONG AUTONOMOUS BIDDING AGENTS IN PROGRAMMATIC ADVERTISING MARKETS

17 квітня 2026 рік ♦ м. Житомир, Україна ♦ МЦНД
.

23
СЕКЦІЯ III.
МАРКЕТИНГОВА ТА
ЛОГІСТИЧНА ДІЯЛЬНІСТЬ

DOI 10.62731/mcnd-17.04.2026.001

CONDITIONS FOR T ACIT COLLUSION AMONG
AUTONOMOUS BIDDING AGENTS IN PROGRAMMATIC
ADVERTISING MARKETS

Ivitskiy Igor
ORCID ID: 0000-0002-9749-6414
PhD, Associate Professor, Founder
London

The allocation of programmatic advertising budget has migrated, over the
past five years, from human -managed campaigns to au tonomous
reinforcement learning agents embedded in demand -side and supply -side
platforms [1]. This migration introduces a threat class that classical ad fraud
taxonomies do not capture: the possibility that bidding agents, through
repeated interaction alon e, converge on strategies that sustain
supracompetitive prices without any explicit communication, shared code, or
human intent to coordinate. The theoretical foundation is well established.
Calvano, Calzolari, Denicolo  , and Pastorello demonstrated that Q -learning
agents in a repeated Bertrand oligopoly reliably learn collusive pricing
equilibria supported by implicit punishment strategies, a result robust across
cost asymmetries and demand shocks [2]. Klein extended the finding to
sequential pricing environments and obtained qualitatively identical dynamics
[3].
The update rule driving this behavior is standard:

𝑄𝑡+1(𝑠, 𝑎) = (1 − α)𝑄𝑡(𝑠, 𝑎) + α [𝑟𝑡 + γ max 𝑎′ 𝑄𝑡(𝑠′, 𝑎′)]

where 𝑠 encodes the observable market state (recent clearing prices, win rates,
competitor bid distributions), 𝑎 is the agent's bid or reserve price, 𝑟𝑡 is realized

Наукові відкриття та фундаментальні наукові дослідження: світовий досвід

24
profit, α is the learning rate, and γ is the discount factor. Collusive equilibria
emerge when four conditions hold jointly: a high discount factor, a stable roster
of market participants, a compact action space that permits rapid convergence,
and a sufficiently long interaction horizon. Each of these conditions is
increasingly satisfied in real -time bidding. Programmatic spending is
approximately 60% automated and rising [1]. The market is concentrated
around a small number of major DSPs and SSPs, producing the stable structure
that learning theory requires. Real -time auctions run continuously at
frequencies that render the effective horizon unbounded.
A second, related failure mode operates on the buy side and requires no
coordination at all. A buying agent optimizing reported return on ad spend
solves

max
π
𝔼 [∑ 𝑣𝑡𝑐𝑡
𝑝𝑡𝑡
]

where 𝑣𝑡 is the platform-imputed conversion value, 𝑐𝑡 the conversion indicator,
and 𝑝𝑡 the price paid. When fraudulent inventory supplies cheap conversions
with 𝑐𝑡 = 1 but true commercial value near zero, the agent discovers and
exploits these sources as a matter of policy, not pathol ogy [1]. The reported
metric improves while realized margin compresses, a divergence consistent
with the data integrity literature on corrupted feedback loops [1, 4].
A third vector compounds the first two. Motwani and colleagues showed
that large language model agents can embed hidden information in ostensibly
routine communication, opening covert channels undetectable to external
monitors [5]. Applied to auction telemetry, bid timing, or creative metadata,
such channels could transmit coordination signals through traffic that appears
fully competitive to regulators and auditors [6].
The implications for competition policy are acute. Existing antitrust
frameworks presuppose human decision -makers who can form intent and
exchange information. Emergent algorit hmic collusion satisfies neither
predicate, yet produces equivalent welfare losses. Detection requires a shift
from intent -based analysis to game -theoretic measurement of market
equilibria, combined with counterfactual testing of agent behavior under
perturbed conditions [ 7]. Until such measurement infrastructure exists, the
preconditions identified by Calvano et al. will continue to accumulate in
programmatic markets without a corresponding defensive apparatus.

17 квітня 2026 рік ♦ м. Житомир, Україна ♦ МЦНД
.

25
References:
1. Ivitskiy I., Savchenko D., Sydore nko D. Data Integrity as the Terminal Constraint in AI -Driven
Advertising: An Information -Theoretic Analysis of Conversion Fraud and Agentic Threat
Evolution. Zenodo. 2026. DOI: https://doi.org/10.5281/zenodo.18675362.
2. Calvano E., Calzolari G., Denicolo   V., Pastorello S. Artificial intelligence, algorithmic pricing, and
collusion. American Economic Review . 2020. Vol. 110, no. 10. P . 3267–3297. DOI:
https://doi.org/10.1257/aer.20190623.
3. Klein T. Autonomous algorithmic collusion: Q -learning under sequential pricing. RAND Journal
of Economics. 2021. Vol. 52, no. 3. P . 538–558. DOI: https://doi.org/10.1111/1756-2171.12383.
4. Ivitskiy I. The M.A.T .H. Framework: A First-Principles Approach to Quant Marketing in  High-
Uncertainty Environments. Zenodo. 2026. DOI: https://doi.org/10.5281/zenodo.18552246.
5. Motwani A., Barber M., McDuff J., Jain L. Secret collusion among generative AI agents. arXiv
preprint. 2024. arXiv:2402.07510.
6. Ivitskiy I. API -native marketing operations: a reference architecture for automated decision
loops. Global Trends in Economics, Finance and Management: Proceedings of the III International
Scientific and Practical Conference  (Kyiv, September 30, 2025). Kyiv: Research Europe, 2025.
P . 101–104. URL: https://researcheurope.org/wp-content/uploads/2025/10/re-30.09.2025-
101-104.pdf.
7. Ivitskiy I. From playbooks to code: translating bidding strategy into rigorous objective functions
and constraints. Global Trends in Science and Education: Proceedings of the IX International
Scientific and Practical Conference (Kyiv, October 5, 2025). Kyiv: Research Europe, 2025. P . 30–
33. URL: https://researcheurope.org/wp-content/uploads/2025/10/re-05.10.2025-30-33.pdf.
