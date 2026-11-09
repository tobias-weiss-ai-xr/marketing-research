---
title: 'From Tokens to Ties: Network and Discourse Analysis of Web3 Ecosystems'
url: https://arxiv.org/abs/2604.18761
category: social-media
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Valentina Kuskova
- Dmitry Zaytsev
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.18761
pages: 7
chars: 32850
fetched_at: '2026-11-08T12:57:17+00:00'
kb_version: 1
---

# From Tokens to Ties: Network and Discourse Analysis of Web3 Ecosystems

From Tokens to Ties: Network and Discourse Analysis
of Web3 Ecosystems
Valentina Kuskova, Dmitry Zaytsev
Lucy Family Institute for Data & Society
University of Notre Dame
Notre Dame, IN, 46556
Abstract
This paper examines Web3 ecosystems not merely
as markets for digital assets, but as networked social
spaces where economic transactions give rise to endur-
ing social ties, shared narratives, and collective iden-
tities. Leveraging large-scale data mining of fused on-
chain blockchain transactions and off-chain social me-
dia activity, we analyze over one hundred NFT col-
lections to uncover how different forms of participa-
tion structure community formation in decentralized en-
vironments. Using network analysis, we identify dis-
tinct ecosystem roles, such as long-term holders, ac-
tive traders, and short-term speculators, and demon-
strate how each produces markedly different network
topologies, levels of cohesion, and pathways for influ-
ence. We complement this structural analysis with dis-
course analysis of social media engagement, revealing
how narrative production, visibility, and sustained in-
teraction persist even as transactional activity declines.
Our findings show that communities centered on hold-
ing behavior evolve from transactional networks into
socially embedded ecosystems characterized by dense
ties, decentralized influence, and ongoing cultural par-
ticipation, while trader- and speculator-dominated net-
works remain fragmented and transactional. By linking
network structure with discursive dynamics, this study
provides a sociotechnical framework for understanding
how value, identity, and inequality are negotiated in
Web3 spaces. The approach offers a scalable method
for detecting patterns of inclusion, exclusion, and rep-
resentational imbalance, advancing network-based re-
search on digital communities beyond purely economic
or technical accounts.
1 Introduction
Non-fungible tokens (NFTs) emerged into public awareness
following several highly publicized transactions, including
early record-setting sales of digital artworks (Kaczynski and
Kominers, 2021). While these events initially framed NFTs
as speculative digital assets, subsequent developments have
revealed a more complex ecosystem in which economic ex-
change, social interaction, and cultural production are tightly
Copyright © 2026 by the authors. Open access article published
under the Creative Commons Attribution-NonCommercial 4.0 In-
ternational License (CC BY-NC 4.0).
intertwined. Rather than functioning solely as isolated trans-
actions, NFT activity increasingly unfolds within persistent,
networked communities that extend across blockchain plat-
forms and social media.
Prior research has largely examined NFTs through a
technological or application-oriented lens, emphasizing use
cases such as copyright protection (C ¸ a ˘glayan Aksoy and
¨Ozkan ¨Uner, 2021), intellectual property commercializa-
tion (Okonkwo, 2021), healthcare systems (Musamih et al.,
2022), game development (Fowler and Pirker, 2021), mar-
keting (Chohan and Paschen, 2023), and fashion (Huggard
and S¨arm¨akari, 2023). While this work highlights the versa-
tility of NFT technology, it typically treats NFTs as discrete
technical artifacts or economic instruments, paying limited
attention to the social structures and interaction patterns that
emerge around them at scale.
The rapid rise and subsequent market contraction of NFTs
further underscores the need for such analysis. After an ini-
tial speculative boom, NFT markets experienced sharp de-
clines in asset valuations, leading to widespread narratives
of financial loss and market failure (Smith, 2023; Hategan,
2024). However, despite declining prices, NFT production
and participation have continued to grow. Estimates sug-
gest that the number of NFT collections increased substan-
tially between 2023 and 2024, even as average transaction
values fell (Minaev, 2023). This divergence between eco-
nomic valuation and participation indicates that NFTs are
being used for purposes beyond short-term speculation, mo-
tivating closer examination of their social and organizational
dynamics.
Importantly, NFT ecosystems are not limited to on-chain
transactions. They are accompanied by rich off-chain ac-
tivity, including community discussion, narrative formation,
and identity signaling across social media platforms. NFT
collections often function as focal points around which
participants coordinate, communicate, and establish shared
meanings that persist independently of ongoing trading ac-
tivity. These dynamics suggest that NFT ecosystems can be
understood as sociotechnical networks, where value is pro-
duced not only through exchange, but also through social
embedding and sustained interaction.
In this paper, we address this gap by analyzing NFT
ecosystems as networked social systems rather than solely
as markets. Leveraging large-scale data mining of fused on-
arXiv:2604.18761v1  [cs.SI]  20 Apr 2026

chain transaction records and off-chain social media dis-
course, we examine over one hundred NFT collections to
identify participation roles, network structures, and discur-
sive dynamics. By combining network analysis with dis-
course analysis, we provide a framework for understand-
ing how decentralized digital communities form, persist, and
differentiate, offering insight into the emergence of value,
identity, and inequality in Web3 environments.
2 Socio-Technical Framing of NFT
Ecosystems
Prior research suggests that NFTs encompass more than dig-
ital assets or technical artifacts. As illustrated in Figure 1,
NFT ecosystems consist of multiple interrelated layers, in-
cluding creators and buyers, on-chain transaction networks,
off-chain communities, and ongoing narrative and discursive
activity across social platforms. Together, these elements
form integrated socio-technical systems in which techni-
cal infrastructure, economic exchange, and social interaction
are mutually constitutive.
Figure 1: The many facets of NFTs.
Beyond their role as transferable digital objects, NFTs
have been used for cultural preservation and representation,
including the digitization of historical artifacts (Metablock,
2024a), religious objects (Constantino, 2022), and Indige-
nous art (Crypto Altruism, 2023). Following the contrac-
tion of speculative NFT markets, such applications have
gained increased prominence, suggesting a shift from purely
transactional use toward community-oriented and meaning-
driven engagement. These developments motivate analyti-
cal approaches that move beyond market behavior to exam-
ine how participation, identity, and interaction are structured
within NFT ecosystems.
Digital art remains the most visible and widely adopted
NFT application. Low production costs, global distribution,
and liquidity enabled by blockchain infrastructure, often
combined with creator anonymity, have been described as
lowering barriers to artistic participation (Watkins, 2021)
and, in some accounts, contributing to the democratization
of art markets (Gibson, 2021). While such claims are con-
tested, they underscore the extent to which NFTs intertwine
creative production with networked participation and collec-
tive visibility.
Despite the rapid growth of NFT-related scholarship,
work explicitly addressing their human-centered or socio-
cultural implications remains limited. A systematic review
of Scopus-indexed publications in late 2022 identified only
one Arts and Humanities article among 127 NFT-related
studies (Taherdoost, 2022), with the remainder concentrated
in computer science, engineering, economics, and social
sciences. Where human-centered considerations do appear,
they are typically operationalized through narrow fairness
metrics, such as demographic representation among NFT
holders (Young, 2020; Kumar, 2025), rather than through
analysis of participation dynamics, discourse, or community
structure.
More broadly, existing work rarely examines NFTs
through alternative analytical lenses that emphasize recog-
nition, participation, or communicative power, including
identitarian (Fraser and Honneth, 2003), capability-based
(Sen, 2001), discursive (Habermas, 1990), or meritocratic
(Sandel, 2020) frameworks. This gap persists despite in-
creasing recognition that AI-enabled and blockchain-based
systems function as socio-technical systems that actively
shape social relations rather than remaining neutral infras-
tructures (Dignum, 2022).
In this paper, we build on this perspective by analyzing
NFT collections as networked socio-technical ecosystems.
Rather than focusing on individual assets or price dynam-
ics, we examine how participation roles, interaction patterns,
and discursive practices co-evolve within NFT communities.
By integrating network analysis with social media discourse
analysis, we investigate how value, identity, and influence
are produced and negotiated across decentralized environ-
ments, positioning NFTs as empirically tractable sites for
studying community formation and inequality in Web3 sys-
tems.
3 NFT Ecosystems as Community-Forming
Technologies
NFT-native properties, such as verifiable ownership, pro-
grammable access rights, and persistent on-chain identity,
have enabled the rapid emergence of NFT-centered on-
line communities. Rather than existing as isolated digi-
tal artifacts, NFT collections often serve as focal points
around which participants organize social interaction, coor-
dinate events, and develop shared narratives (Kaczynski and
Kominers, 2021). These ecosystems extend beyond trading
activity to include conferences, collaborative projects, and
platform-specific social spaces, forming durable interaction
networks that persist independently of asset price dynamics.
Despite their scale and visibility, NFT communities re-
main underexamined from a systems perspective. Unlike
the traditional art world, where institutions and social roles
are relatively transparent, NFT ecosystems operate largely
through pseudonymous participation and decentralized co-
ordination. This limits external visibility while simulta-
neously producing rich, traceable interaction data across
blockchain and social platforms. As immersive online en-
vironments and metaverse-like systems continue to expand
(Belk et al., 2022), understanding how such communities
form, persist, and stratify has become an important empir-

ical problem rather than a purely cultural one.
4 Participation, Representation, and
Opportunity Structures
NFT ecosystems are frequently described as offering new
opportunities for participation by historically underrepre-
sented groups, due to lower barriers to entry, global reach,
and reduced reliance on traditional gatekeeping institutions
(Bastian, 2021). From a socio-technical perspective, this
raises empirical questions about who participates in NFT
ecosystems, how visibility and influence are distributed, and
whether new forms of inequality emerge alongside new op-
portunities.
Existing discussions of inclusion in NFTs are largely
anecdotal or project-specific, focusing on individual col-
lections or platforms associated with Indigenous creators,
Black artists, or women-led initiatives. While these cases il-
lustrate the potential for alternative participation pathways,
they do not provide systematic evidence about ecosystem-
wide patterns of representation, community formation, or
influence. Moreover, participation alone does not guarantee
visibility, valuation, or sustained engagement, underscoring
the need to distinguish between access, centrality, and long-
term network position.
Rather than evaluating inclusion through categorical pres-
ence alone, this study treats participation as a measurable
structural property of NFT ecosystems. By analyzing in-
teraction networks and discourse dynamics, we examine
whether communities associated with underrepresented cre-
ators occupy central or peripheral positions, whether influ-
ence is concentrated or distributed, and how narratives prop-
agate across collections. This reframing shifts attention from
individual success stories to population-level patterns that
can be empirically assessed.
5 Ethical and Equity Considerations in NFT
Ecosystems
Alongside their participatory potential, NFT ecosystems
raise well-documented ethical and equity concerns. These
include the circulation of harmful or exclusionary content,
fraud and consumer protection issues, and environmental
externalities associated with blockchain infrastructure (In-
gold, 2022; Dean, 2022; Flick, 2022). From a sociotech-
nical standpoint, such issues are not peripheral but struc-
turally embedded, reflecting how technical affordances in-
teract with social norms and incentives.
Empirical research has begun to examine inequality in
NFT markets, including evidence of racial and gender dis-
parities in pricing and representation (Nguyen, 2022; Zhang
et al., 2022). However, much of this work focuses on early
or iconic collections, such as CryptoPunks, which may not
be representative of the current NFT ecosystem. Given the
rapid expansion and diversification of NFT collections, it re-
mains unclear whether previously identified patterns gener-
alize to newer communities or whether alternative structures
have emerged.
More broadly, existing analyses of fairness and bias in AI-
driven and blockchain-enabled systems often rely on narrow
technical definitions that overlook contextual and discursive
dimensions of inequality (Blodgett et al., 2020). This lim-
its the ability to detect how exclusion, marginalization, or
unequal amplification arise through participation dynamics
rather than explicit design choices. In response, this study
adopts an interdisciplinary, data-driven approach that inte-
grates network structure and discourse analysis to examine
how ethical and equity-related outcomes emerge within NFT
ecosystems at scale.
6 Data and Methodology for NFT
Community Detection
Data Sources and Scope
Data for this study were provided by Web3Sense (2025), a
private analytics firm specializing in the integration of on-
chain blockchain data with off-chain Web2 and open-source
intelligence, including social media activity. The dataset
covers all recorded transactions for hundreds of NFT col-
lections, from the date of first mint through the date of data
retrieval.
Each transaction record includes the unique token iden-
tifier, buyer and seller wallet addresses, transaction times-
tamp, transaction value denominated in Ethereum (ETH),
gas fees, and, when available, Ethereum Name Service
(ENS) identifiers. Although wallet addresses are pseudony-
mous by default, ENS registrations provide a partial linkage
between on-chain behavior and publicly visible online iden-
tities, enabling richer contextual analysis.
Network Construction and Community Detection
Using transaction-level data, we constructed directed trans-
action networks in which nodes represent wallet addresses
and edges represent NFT transfers between buyers and sell-
ers. Edge weights capture transaction frequency and value,
allowing differentiation between sporadic and sustained in-
teractions. Specifically, edge weight is computed as a com-
posite of transfer count and cumulative ETH value between
a given wallet pair, enabling the network to reflect both ac-
tivity intensity and economic significance simultaneously.
Graph layouts for all visualizations were generated using
force-directed algorithms, specifically the ForceAtlas2 lay-
out as implemented in Gephi, which positions nodes based
on attraction along weighted edges and repulsion between
all node pairs. This approach causes highly interconnected
wallets to cluster together visually and isolated nodes to drift
to the periphery, making community structure directly legi-
ble in the spatial arrangement. Consequently, visual differ-
ences across the holder, trader, and speculator network fig-
ures reflect genuine structural differences in interaction pat-
terns, not arbitrary drawing choices.
To identify structurally coherent subgroups, we applied
community detection techniques including modularity-
based clustering (Louvain method) and label propagation.
These methods reveal clusters of wallets that interact more
frequently with one another than with the broader network,
signaling shared ownership patterns, coordinated behavior,
or collective engagement with specific collections. Such

clusters serve as the basis for identifying distinct commu-
nity types within NFT ecosystems. The numerical labels vis-
ible in Figure 5 correspond to community cluster identifiers
assigned by the detection algorithm, providing a basis for
cross-community comparison of size, density, and central-
ization.
Integration of On-Chain and Off-Chain Signals
To contextualize transactional behavior, we enriched the on-
chain networks with off-chain metadata using Web3Sense’s
identity-matching layer. This layer links wallet addresses to
public social media accounts through ENS identifiers, user-
declared wallet tags, and triangulated digital footprints.
This integration enables joint analysis of behavioral sig-
nals, such as minting frequency, resale patterns, and hold-
ing duration, with discursive indicators including posting
volume, engagement levels, and participation in community
spaces such as Twitter Spaces or Discord events. The dual-
layer approach allows us to examine how identity signal-
ing, social participation, and economic behavior co-evolve
within NFT communities, rather than treating transactions
as isolated events.
7 Behavioral Typologies in NFT Ecosystems
Analysis across dozens of NFT transaction networks re-
vealed three recurring behavioral community types: holders,
traders, and speculators. These types are not predefined cat-
egories but empirically emergent patterns derived from net-
work structure, transaction dynamics, and temporal behav-
ior.
Holder Communities
Holder communities (Figure 2) consist of wallets that ac-
quire NFTs and retain them over extended periods, exhibit-
ing limited resale activity. These networks are characterized
by dense cores of interconnected wallets surrounded by pe-
ripheral nodes that have purchased tokens but remain trans-
actionally inactive thereafter.
The structure suggests more than transactional engage-
ment; it reflects social cohesion and the emergence of digital
affinity groups. These holders may be bound by shared aes-
thetic preferences, collective narratives, or community val-
ues, forming the cultural backbone of the NFT ecosystem.
The network’s shape, consisting of dense center with radi-
ating tendrils, illustrates a vibrant and resilient social fab-
ric, with the potential for influence, governance, and story-
telling emerging from within. This is not merely a collection
of users but a digitally-native community bound by belief in
the symbolic and cultural value of the assets they hold.
Trader Communities
In contrast, trader communities (Figure3) display highly dy-
namic and interconnected structures driven by frequent buy-
ing and selling across multiple collections. These networks
feature dense transactional cores, extensive cross-cutting
ties, and long transactional chains indicative of liquidity-
driven behavior.
Figure 2: Communities of “Holders” – Veefriends (top) and
ArtBlocks (bottom).
Figure 3: Communities of “Traders” – Doodles (top) and
CoolCats (bottom).

The presence of loops, bridges, and extended paths sug-
gests arbitrage strategies, coordinated trading, or automated
activity. Unlike holder communities, traders exhibit weak
attachment to specific collections or narratives, operating
instead as connectors across disparate ecosystems. Struc-
turally, these networks function as high-throughput conduits
for value transfer rather than as sites of sustained social co-
hesion.
Speculator Communities
Speculator communities (Figure 4) occupy an intermediate
but distinct position. Characterized by short holding periods
and episodic engagement, these networks show looser clus-
tering, fragmented cores, and a high prevalence of transient
nodes.
Figure 4: Communities of “Speculators” – Finiliar (top) and
BudHeritage (bottom).
The structure reflects opportunistic participation driven
by hype cycles, influencer signals, or trending indicators.
Unlike traders, speculators exhibit limited strategic coordi-
nation, and unlike holders, they display minimal long-term
attachment to community norms or narratives. Their frag-
mented topology and detached subgroups suggest low com-
mitment and weak social integration, contributing to volatil-
ity and trust erosion within broader NFT ecosystems.
8 Comparative Cluster Structure and
Network Centralization
Cluster-level analysis further highlights structural differ-
ences across community types (Figure 5). The Art Blocks
holder network exhibits a decentralized, interwoven clus-
ter structure with multiple moderately sized hubs, indicat-
ing distributed influence and high mutual connectivity. This
pattern is consistent with participatory cultures where en-
gagement and authority are broadly shared.
In contrast, the Doodles trader network displays a hub-
and-spoke configuration dominated by a single central node,
with many peripheral wallets connected primarily through
that hub. Such centralization facilitates efficient trade but
limits redundancy, mutual visibility, and durable commu-
nity ties. These contrasts illustrate how different participa-
tion modes generate fundamentally different social architec-
tures within NFT ecosystems.
Figure 5: Clusters of Artblocks (top) and Doodles (bottom).
Together, these contrasting structures reinforce the cen-
tral argument: holder communities like Art Blocks foster de-
centralized, richly connected networks conducive to cultural
and social development, while trader communities such as
Doodles exhibit hub-and-spoke models that facilitate liquid-
ity but lack the structural complexity necessary for sustained
community building. This methodology can be extended to
assess whether vulnerable or underrepresented groups are
participating primarily at the center or periphery of these
networks, offering a new lens to evaluate not just inclusion,
but integration.
9 Temporal Dynamics of On-Chain and
Off-Chain Activity
To examine the relationship between economic and social
engagement, we analyzed temporal patterns of transaction
volume and social media activity. Figure 6 juxtaposes on-
chain transaction counts and Twitter activity for the Art
Blocks community throughout 2021.
Both series show initial surges following minting and dur-
ing peak market attention. However, while transaction vol-
ume declines after mid-2021, social media activity contin-
ues to rise and remains elevated. This decoupling indicates
a transition from speculative engagement to sustained com-
munity participation, where discourse, interpretation, and
identity-building persist independently of trading intensity.

This pattern is consistently observed across multiple
holder communities but is largely absent in trader- and
speculator-dominated networks, where social engagement
typically tracks transaction volume more closely. The diver-
gence highlights the role of holding behavior in catalyzing
durable cultural ecosystems rather than transient market ac-
tivity.
Figure 6: ArtBlocks community activity on-chain (top) and
on X (formerly Twitter) (bottom).
In the case of Art Blocks, social media activity became
the scaffolding for a vibrant, durable holder network rooted
in shared aesthetic appreciation and cultural participation.
These individuals remained invested not just in the asset, but
in the cultural and social life of the project, sharing interpre-
tations of the artwork, organizing virtual events, and rein-
forcing the community’s collective identity. The divergence
between economic and discursive behavior in this data rein-
forces the idea that NFT communities like Art Blocks thrive
not only through sales, but through storytelling, shared val-
ues, and lasting social bonds.
10 Discussion
Our analysis demonstrates that integrating network analysis
with off-chain discourse data provides a robust sociotech-
nical framework for examining bias, inequality, and repre-
sentation in NFT ecosystems. This approach enables simul-
taneous investigation of structural participation patterns and
discursive visibility - dimensions that are often treated sep-
arately or overlooked in technically oriented fairness analy-
ses.
From a structural standpoint, transaction networks reveal
how influence and access are distributed across NFT com-
munities. Network metrics such as centrality, modularity,
and connectivity make it possible to identify whether partic-
ipation is broadly distributed or concentrated among a small
number of actors, as well as whether certain groups occupy
peripheral or weakly connected positions. The presence of
isolated clusters or limited cross-community ties may indi-
cate systemic segmentation, even in ecosystems that appear
open at the level of entry.
Off-chain discourse analysis complements these findings
by capturing how communities are represented and engaged
with in public-facing spaces. Patterns in language use, senti-
ment, and engagement volume reveal whose narratives gain
traction and whose remain marginal. By linking transac-
tional roles to social visibility through ENS identifiers and
platform metadata, the framework distinguishes between
nominal participation and meaningful influence in shaping
community narratives.
Taken together, this socio-technical approach moves be-
yond surface-level demographic counts to examine how in-
equality emerges through interaction structure, discursive
amplification, and network position. It provides a scalable
and empirically grounded method for assessing fairness and
inclusion in decentralized digital ecosystems, where social
outcomes are produced through the interaction of technical
infrastructure and collective practice.
11 Conclusion and Research Implications
This study demonstrates that Web3 ecosystems, and NFT
collections in particular, can be systematically analyzed
as sociotechnical networks in which economic transactions
give rise to durable social structures and shared narratives.
By mining fused on-chain transaction data and off-chain
social media activity, we show that different participation
modes - holding, trading, and speculation - produce distinct
network topologies, levels of cohesion, and influence dy-
namics.
Our results indicate that holder-centered ecosystems tran-
sition from transactional interaction graphs into socially em-
bedded networks characterized by dense ties, decentralized
influence, and sustained discourse, even as trading activ-
ity declines. In contrast, trader- and speculator-dominated
ecosystems remain structurally fragmented and temporally
volatile, with limited persistence of social ties or narrative
continuity. These findings highlight the importance of inte-
grating behavioral roles and discourse signals into network-
based analyses of decentralized digital communities.
Methodologically, this work contributes a scalable frame-
work for linking network structure with discursive dynam-
ics in Web3 environments. By combining role-based net-
work analysis with social media discourse mining, the ap-
proach enables the detection of inclusion, exclusion, and
representational imbalance as emergent properties of inter-
action rather than as purely economic outcomes. This moves
beyond asset-centric or transaction-only analyses and pro-
vides a richer basis for studying value formation, identity
signaling, and inequality in decentralized systems.
Future work will extend this framework longitudinally
and across platforms, enabling causal and temporal analy-
sis of community evolution, narrative diffusion, and struc-
tural change. Among the promising directions is the ap-
plication of graph neural networks (GNNs), for example,
modeling transaction networks with wallets, collections, and

social accounts as heterogeneous node types, with transac-
tion, mention, and ownership relations as edge types, which
could support tasks such as community role prediction and
link prediction across Web3 ecosystems. More broadly, the
proposed approach offers a generalizable methodology for
studying how social organization and cultural participation
emerge from large-scale interaction data in decentralized on-
line ecosystems.
References
Bastian, R. 2021. The Diversity, Equity And Inclusion Po-
tential Of NFTs. https://www.forbes.com/sites/rebekahbastian/
2021/10/24/the-diversity-equity-and-inclusion-potential-of-nfts/
Belk, R., Humayun, M., and Brouard, M. 2022. Money, pos-
sessions, and ownership in the Metaverse: NFTs, cryptocur-
rencies, Web3 and Wild Markets.Journal of Business Re-
search153: 198–205.
Blodgett, S. L., Barocas, S., Daum´e III, H., and Wallach, H.
2020. Language (technology) is power: A critical survey of
“Bias” in NLP. arXiv preprint arXiv:2005.14050.
C ¸ a˘glayan Aksoy, P., and ¨Ozkan ¨Uner, Z. 2021. NFTs and
copyright: challenges and opportunities.Journal of Intellec-
tual Property Law and Practice16(10): 1115–1126.
Chohan, R., and Paschen, J. 2023. NFT marketing: How
marketers can use nonfungible tokens in their campaigns.
Business Horizons66(1): 43–50.
Constantino, T. 2022. NFTs Get Religion as Vatican
Creates a Digital Gallery. https://www.fool.com/the-
ascent/cryptocurrency/articles/nfts-get-religion-as-vatican-
creates-a-digital-gallery/
Crypto Altruism. 2023. Three Indigenous-led NFT
Projects elevating Indigenous art and culture.
https://www.cryptoaltruism.org/blog/three-nft-projects-elevating-
indigenous-art-and-culture
Dean, T. 2022. Hype and hypocrisy: The high ethical cost of
NFTs. https://ethics.org.au/hype-and-hypocrisy-the-high-ethical-
cost-of-nfts/
Dignum, V . 2022. Relational artificial intelligence. arXiv
preprint arXiv:2202.07446.
Flick, C. 2022. A critical professional ethical analysis of
Non-Fungible Tokens (NFTs).Journal of Responsible Tech-
nology12(100054): 1–16.
Fowler, A., and Pirker, J. 2021. Tokenfication — The po-
tential of non-fungible tokens (NFT) for game development.
InExtended Abstracts of the 2021 Annual Symposium on
Computer-Human Interaction in Play,152–157.
Fraser, N., and Honneth, A. 2003.Redistribution or Recog-
nition? A Political-Philosophy Exchange.Verso.
Gibson, J. 2021. The thousand-and-second tale of NFTs, as
foretold by Edgar Allan Poe.Queen Mary Journal of Intel-
lectual Property11(3): 249–269.
Habermas, J. 1990.Moral Consciousness and Communica-
tive Action.London: Polity Press.
Hategan, V . 2024. Dead NFTs: The Evolving Landscape of
the NFT Market. https://dappgambl.com/nfts/dead-nfts/
Huggard, E., and S ¨arm¨akari, N. 2023. How digital-only
fashion brands are creating more participatory models of
fashion co-design.Fashion, Style and Popular Culture
10(4): 583–600.
Ingold, L. 2022. NFTs: Risks, Rewards, Ethics. https://
sevenpillarsinstitute.org/nfts-risks-rewards-ethics/
Kaczynski, S., and Kominers, S. D. 2021. How NFTs create
value.Harvard Business Review. https://hbr.org/2021/11/how-
nfts-create-value
Kumar, N. 2025. 49 NFT Statistics 2025 — Worldwide
Data and Market Forecast. https://www.demandsage.com/nft-
statistics/
Metablock. 2024a. NFTs and Historical Artifacts. https://
blog.metablock.co/nfts-and-historical-artifacts-073de79caa19
Minaev, A. 2023. How Many NFTs Are There in 2024?https:
//cryptodose.net/learn/how-many-nfts-are-there/
Musamih, A., Salah, K., Jayaraman, R., Yaqoob, I., Puthal,
D., and Ellahham, S. 2022. NFTs in healthcare: vision,
opportunities, and challenges.IEEE Consumer Electronics
Magazine12(4): 21–32.
Nguyen, J. K. 2022. Racial discrimination in non-fungible
token (NFT) prices? CryptoPunk sales and skin tone.Eco-
nomics Letters218: 1–4.
Okonkwo, I. E. 2021. NFT, copyright and intellectual prop-
erty commercialization.International Journal of Law and
Information Technology29(4): 296–304.
Sandel, M. J. 2020.The Tyranny of Merit.Penguin Random
House.
Sen, A. 2001.Development as Freedom.Oxford University
Press.
Smith, S. V . 2023. Is it RIP for the NFT? https:
//www.marketplace.org/story/2023/12/22/nft-market-crashes-
value-worthless
Taherdoost, H. 2022. Non-fungible tokens (NFT): A system-
atic review.Information14(1): 1–12.
Watkins, I. 2021. Non-fungible tokens (NFT) and the evo-
lution of art. InThe Youth of the 21st Century: Education,
Science, Innovations. https://rep.vsu.by/bitstream/123456789/
30743/1/278-280.pdf
Web3Sense. 2025. Web3Sense.https://www.web3sense.ai/
Young, I. M. 2020. Justice and the Politics of Difference. In
The New Social Theory Reader ,261–269. Routledge.
Zhang, Y ., Chen, Z., Xu, C., Zhang, L., and Tong, X. 2022.
Are racial and gender inequalities emerging in the NFT art-
work? A visual exploration of CryptoPunks.
