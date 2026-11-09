---
title: 'When the customer is a machine: a systematic literature review and integrative framework of agentic
  commerce'
url: https://doi.org/10.21203/rs.3.rs-11222729/v1
category: ai-marketing
subcategory: framework
date: 2026-10
venue: Research Square
authors:
- Mahyar Tourchi Moghaddam
- Mina Alipour
- Klaus G. Grunert
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-11222729/latest.pdf
pages: 55
chars: 152240
fetched_at: '2026-11-08T20:01:01+00:00'
kb_version: 1
---

# When the customer is a machine: a systematic literature review and integrative framework of agentic commerce

When the customer is a machine: a systematic
literature review and integrative framework of
agentic commerce
Mahyar Tourchi Moghaddam 
University of Southern Denmark
Mina Alipour 
University of Southern Denmark
Klaus G Grunert 
Aarhus University
Systematic Review
Keywords: agentic commerce, AI agents, delegation, customer journey, generative engine optimization,
systematic literature review
Posted Date: October 22nd, 2026
DOI: https://doi.org/10.21203/rs.3.rs-11222729/v2
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

1
When the customer is a machine: a systematic literature
review and integrative framework of agentic commerce
Anonymous author(s)
Details withheld for double-blind review
Abstract
Artificial intelligence agents now search, evaluate, negotiate, and pa y on behalf of consumers,
while firms deploy agents that create content, personalize offers, and comple te transactions.
Agentic commerce therefore weakens a foundational assumption of marketing thought and
marketing measurement: that the recipient of marketing activity is a human being. The evidence
is scattered across marketing, information systems, computer science, ec onomics, and law, and it
has a largely forgotten first act in the shopbot research of the late 1990s . Following the SPAR-4-
SLR protocol with PRISMA 2020 reporting, we screen 5,157 records from Scopus, Web of
Science, and EBSCO Business Source and add verified snowballing to assemble 140 primary
studies spanning 1994 to 2026. Each study is coded on influence direction, customer journey
stage, delegation depth, method, and research wave. The synthesis yields an act or taxonomy with
a five-level delegation ladder, an influence triad that separates ma rketing to, through, and by
agents, an integrated account of trust and governance infrastructure, and a market-level analysis
connecting both research waves. The Agentic Commerce Reference Fra mework consolidates this
evidence into four auditable layers with explicit cross-layer dynamics, a ten-proposition research
agenda, and five measurement instruments for analytics practice. A complete  replication package
accompanies the article.
Keywords: agentic commerce; AI agents; delegation; customer journey; generative engine
optimization; systematic literature review
1 Introduction
For three decades, digital commerce has been designed around a human actor. A  person sees
the advertisement, reacts to the warning that only two items are lef t, compares offers across
browser tabs, clicks the button, and types the card number. That design assumption is now
weakening from both sides of the market at once. On the demand side, consumers de legate
shopping tasks to conversational assistants and increasingly autonomous agents, from product
discovery and comparison to checkout itself (Allouah et al., 2026; De Bellis and J ohar, 2020;
Frank et al., 2026). On the supply side, firms deploy generative agents that wr ite product content,
design advertising, personalize offers, negotiate, and transact (Wang et al ., 2025; Puri et al.,
2026; Aslam et al., 2026). The institutional infrastructure has followed quickly. Within roughly
eighteen months, Google’s Agent Payments Protocol, the OpenAI and Stripe Agent ic Commerce
Protocol, Visa’s Trusted Agent Protocol, and Mastercard’s Agent Pay were al l announced
(Google, 2025; OpenAI and Stripe, 2025; Visa, 2025; Mastercard, 2025). They share a singl e
purpose: letting software buy things in a way that merchants, card-issuing banks,  and regulators

2
can verify. Consultancies size the delegated purchasing opportunity in the tr illions of dollars by
2030 (Schumacher et al., 2025), and interface data make the projection concre te. The assistant
platforms now intermediating discovery sit atop a search market in which a single firm controlled
about 80 percent of desktop and 90 percent of mobile queries as of 2025 (Ortiz -Freuler and
Castells, 2025). Even partial migration of that traffic into agent-gener ated answers therefore
reroutes the primary demand channel of the digital economy. Marketing schol arship has
registered the shift. A recent research note argues that AI custome rs require a dedicated
subdiscipline of machine marketing (Sarstedt et al., 2026), and journals have begun publishing
empirical work on the value consumers derive from conversational commer ce, the established
term for shopping conducted through chat and voice interfaces (Schultz and K aiser, 2025). What
that emerging subdiscipline lacks is a systematic evidence base, and supply ing one is the purpose
of this article.
Why does the machine customer matter for theory rather than only for opera tions? Because it
breaks the mechanisms marketing has spent a century learning to use, and it breaks them in three
distinct places. First, visibility shifts from capturing human attention to being retrieved by a
machine. One can read retrieval as attention under different rules, but the practical levers change:
whether an offer exists for an agent depends on structured data, verifiable  claims, and third-party
signals. In one controlled experiment, restructuring content alone raised a source ’s presence in
generated answers by up to 40 percent (Aggarwal et al., 2024), and audit studies point in the
same direction (Li et al., 2026a; Kumar and Lakkaraju, 2024). Second, persuasion acquires a
second, non-human target with its own sensitivities. Audits of commercially deployed shoppi ng
agents document position biases that differ across providers and even reverse  between model
versions, penalties for sponsored tags alongside rewards for platform endorsement s, and demand
that concentrates on a few modal products and reshuffles when the underlying m odel updates
(Allouah et al., 2026). A field experiment adds the human-side counterpart: a single disclosure of
machine identity before the conversation can reduce a channel’s purchase rate by more than three
quarters (Luo et al., 2019). Third, the subject of measurement changes. Clic k paths, session logs,
and last-touch attribution presume a person navigating pages. None of them describes an agent
that, holding a consumer’s mandate, the authority the consumer has granted it to  act, reads ten
catalogs, queries three merchants, and buys once. A discipline whose analytics apparatus is built
on observing humans must now decide how to observe delegation.
The scholarly response is substantial but scattered, and it does not yet know itself as one
literature. Consumer researchers examine when people grant purchasing authority to machines
and how they respond to machine persuasion (Wang et al., 2026a; Farmer and Hardi ng, 2026;
Shamim et al., 2026). Computer scientists audit what shopping agents buy (Allouah et al., 2026),
benchmark them (Ling et al., 2026; Wang et al., 2026b), and demonstrate how easily their
recommendations can be manipulated (Li et al., 2026a; Kumar and Lakkaraju, 2024). Economists
design advertising auctions for generated answers (Duetting et al., 2024; Dubey et  al., 2024;
Hajiaghayi et al., 2024) and document pricing algorithms that reach supra-competi tive prices
without communicating (Schlechtinger et al., 2023). Legal scholars ask who is liable when a
delegated agent transacts and whether platform regulation anticipated ma chine gatekeepers
(Busch, 2025; Bostoen and Krämer, 2026; Zhang and He, 2026). Design researchers build t he
payment, identity, and authorization layer that makes any of this transactable  (Chua et al., 2026;
South et al., 2025), and taxonomies of marketing agents together with strategy c hapters have
begun to map the toolset and its firm-performance stakes (Puvvadi et al., 2025; FOLT EAN and

3
HERA, 2026). These communities rarely cite one another, and almost none of the m cite the
field’s first act: the agent-mediated electronic commerce program of the late 1990s. That program
built shopbots and negotiation agents, documented sellers gaming comparison engines, a nd
produced field evidence that brand premia survive machine-mediated choice (G uttman et al.,
1998; Maes et al., 1999; Smith and Brynjolfsson, 2001). That first program stalled for r easons its
field-defining survey named at the time: personalization (adapting offers to an individual), shared
semantics (agents and merchants describing products in compatible terms), service  discovery
(agents finding relevant sellers at all), and interaction protocols (standa rd messages agents can
exchange). Above all, it named trust in delegation (He et al., 2003). Each i tem on that list names
something the current protocol build-out exists to supply, which makes the fi rst wave the field’s
only long baseline and its natural control condition rather than a historical curiosity.
No existing review integrates these strands. Prior secondary studies (re views and other
syntheses) map consumer-side effects of agentic recommendation and dele gation (Balaskas,
2026), conversational commerce (Lim et al., 2022), adoption of conversational agents (Ling et
al., 2021), customer-level outcomes of deployed AI agents (Raja et al., 2026), and the first-wave
comparison shopping systems (Pathak, 2010). Each covers one region of the phenomenon; none
spans both research waves, treats the direction of marketing influence as an explicit coding
dimension, connects consumer evidence to the governance and payment infrastr ucture now being
built, or draws consequences for measurement. This review does all four, guided by four research
questions. RQ1: How has research on commerce-capable AI agents developed across its t wo
waves, the agent-systems wave of roughly 1994 to 2010 and the wave that follows the di ffusion
of large language models from late 2022, and which actors and levels of delegated autonomy
does it describe? RQ2: Through which mechanisms is marketing influence exerted on, through,
and by AI agents along the customer journey? RQ3: Which factors shape consumer trust in and
acceptance of delegated shopping, and which governance and infrastructure c onditions does the
literature identify? RQ4: What are the market-level consequences of agentic commerce, and what
do they imply for measurement and management?
We answer these questions through a systematic review of 140 primary studies published
between 1994 and 2026, assembled from database searches of Scopus, Web of Sci ence, and
EBSCO Business Source and extended through verified backward and forward snowballi ng. The
review follows the SPAR-4-SLR protocol (Paul et al., 2021) with PRISMA 2020 r eporting (Page
et al., 2021). The review makes four contributions, and each moves beyond mapping the sta te of
the art. First, it connects two research waves that have so far developed with little mutual citation,
and it shows result by result that several central second-wave market findings replicate first-wave
findings across a twenty-five-year technology shift. We read such replic ation as unusually strong
evidence for a domain this young. Second, it introduces two shared constructs the l iterature
currently lacks: a five-level delegation ladder that makes studies of as sistants, advisors, and
autonomous buyers commensurable, and an influence triad that separates marketing t o agents,
through agents, and by agents. Third, it consolidates the synthesis in the Agentic C ommerce
Reference Framework, a four-layer architecture with sub-components, cross-layer dynamics, and
explicit usage guidance for the marketing, consumer research, human-compute r interaction,
information systems, software engineering, economics, and legal communitie s, in which every
element is traceable to coded primary studies. Fourth, it converts the  framework’s exposed gaps
into a ten-proposition research agenda and five measurement instruments, fr om share of model
voice to mandate-based attribution, that operationalize the agenda fo r analytics practice. All

4
screening decisions, codes, and counts are released in a replication pack age from which every
number and data figure in the article can be recomputed. The anonymous pac kage is available at
this link: https://figshare.com/s/af06b7238fc45bed37fb.
The article proceeds as follows. Section 2 develops the conceptual back ground: the field’s
temporal structure, the construct space, the theoretical apparatus, a nd a positioning against prior
reviews. Section 3 reports the method in full. Section 4 profiles the corpus. S ections 5 to 8
answer the research questions. Section 9 builds the integrative framework,  its dynamics, and its
use across research communities. Section 10 develops the theoretical impli cations, the research
agenda, and the implications for analytics, management, and policy. Sections 11 and 12 state the
limitations and conclude.
2 Conceptual background
2.1 Two waves and a bridge decade
Commerce-capable software agents predate large language models by a quarter century, and
the first wave was not a footnote but a complete research program wit h theory, systems,
experiments, and field data. Its theoretical core was a consumer buying be havior model that
mapped software agents onto need identification, product brokering, merchant broke ring,
negotiation, purchase, and evaluation (Guttman et al., 1998), together with depl oyed systems that
occupied those stages: comparison shopbots, negotiation marketplaces, and re commendation
agents (Maes et al., 1999). Around the systems grew an empirical literatur e whose questions map
directly onto today’s: how decision aids change choice, how agent recommendations ar e
evaluated, and how sellers respond strategically. Interactive decision aids were shown to
restructure rather than merely shorten choice. In a controlled shopping experi ment, a
recommendation agent reduced the size but raised the quality of consideration sets, and it
increased the share of participants choosing objectively better options whil e lowering search
effort (Häubl and Trifts, 2000). The machine changed what consumers considere d, not only how
fast they considered it. Agent recommendations for unfamiliar products depended on context, and
the direction of that dependence reversed with detail. With little information, an attractive
familiar context lifted the unfamiliar item by association; once item-specific detail was added, the
same attractive context invited comparison and lowered the item’s evaluation (Cooke  et al.,
2002). Buyers adjusted their search behavior around the new intermediaries: in one early survey,
mere awareness of shopping agents made buyers about 35 percent more likely t o combine agent-
based and manual search rather than rely on a single channel (Sen et al., 2006). Comparison-
agent research documented paradoxical effects of decision aids on comparison sh opping (Wan et
al., 2009), price frames that moderated search behavior at shopping agents ( Grewal and Lindsey-
Mullikin, 2006), and differences between search and experience goods in perceive d agent
effectiveness (Aggarwal and Vaidyanathan, 2003). Later in the wave, it ad ded persona effects for
older users of virtual shopping agents (Chattaraman et al., 2014).
The first wave also produced the market-level results that anchor  this review’s continuity
thesis. Price dispersion persisted under comparison agents, contrary to fric tionless-market
predictions, and search-cost mechanisms explained why (Pathak, 2012; Snaith, 2003). Se llers
learned to game the machine gatekeeper through selective price disclosure a nd strategic ordering
(Hajaj et al., 2015; Hajaj et al., 2017), an adversarial dynamic that antici pates today’s generative

5
engine optimization. Price-setting agents produced cyclical price wars in sim ulation (Greenwald
and Kephart, 1999; Leloup, 2003). Game-theoretic analysis showed that shopping agents, by
putting every seller one click apart, change equilibrium pricing as if compe titors were physically
co-located (Iyer and Pazgal, 2003), and early assessments projected the market i mpact of
artificial shopping agents (Redmond, 2002; Ma et al., 2010). Above all, the wave’s signature field
study showed that at a shopbot, where price comparison is nearly costless, the  most heavily
branded retailers still commanded price premia: brand still matter ed when a machine ranked the
offers (Smith and Brynjolfsson, 2001). Design research meanwhile prototyped the t ransactional
machinery, from secure agent negotiation protocols (Wang et al., 1999) and bid-for ecasting
mechanisms for autonomous bidding agents (Kehagias et al., 2005) to personalized compar ison
engines (Yuan, 2003) and decision-analytic marketplaces (Karacapilidis and Moraıtis, 2001). The
program then stalled, and its field-defining survey closed by naming the open problems precisely,
and none of them was intelligence. They were personalization (agents knowi ng enough about a
person to act for them), semantic interaction (systems sharing enough meaning to t ransact),
discovery (finding trustworthy counterparties), and interaction protocols (shared standards for
negotiation and payment). The fifth and hardest was trust, with both a social fa cet, whether
people would let software decide for them, and a technological facet, w hether the infrastructure
could make such delegation safe (He et al., 2003). Nothing on that list concerns i ntelligence;
everything on it concerns interoperation and institutions.
What followed was not silence but a change in what researchers studied, and the corpus makes
the change visible. Between 2011 and 2021 the coded studies shift from buildi ng agents to
studying the human and institutional preconditions of delegation. The psychology of algorithm
reliance matured in this bridge decade. Its landmarks are aversion to a lgorithms after seeing them
err (Dietvorst et al., 2015), appreciation of algorithmic advice in many j udgment tasks (Logg et
al., 2019), task-dependent resistance concentrated in subjective domains (Castel o et al., 2019),
and the word-of-machine effect separating utilitarian from hedonic contexts (Longoni and Cian,
2022). Consumer-experience accounts of living with autonomous systems and connected obj ects
followed (Puntoni et al., 2021; Hoffman and Novak, 2018), capped by an analysis of the adoption
barriers specific to autonomous shopping systems (De Bellis and Johar, 2020). Legal scholarship
coined the algorithmic consumer as a market-structure category and anti cipated the competition
and advertising consequences of purchase decisions executing in code (Gal and Elkin-K oren,
2016). A small continuing stream of first-wave work still tracked shopbot m arkets and seller
gaming (Pathak, 2012; Hajaj et al., 2015; Hajaj et al., 2017; Pil ı́k et al., 2016). The decade closed
with the field’s largest field experiment on machine selling: undisclosed chatbots sold as
effectively as proficient human workers, while disclosure of machine i dentity before the
conversation reduced purchase rates by 79.7 percent (Luo et al., 2019). The bridge de cade thus
supplied the delegation psychology and the legal vocabulary that the second wave now r uns on,
while agent systems themselves lay dormant.
The second wave, dating from the diffusion of large language models in late 2022, changes
three parameters at once. Agents are general purpose, so one assistant spans the journey instead
of one shopbot per function (Patil et al., 2026; Potluri and Chittimalla, 2026; I shida et al., 2025).
Agents are linguistic, so they read the same persuasive content humans read, which helps explain
why persuasion, manipulation, and disclosure findings transfer to them (Friest ad and Wright,
1994; Farmer and Harding, 2026; Guo et al., 2025). And agents are being wired into payment-
grade infrastructure with cryptographic mandates, verified identity, and m erchant endpoints

6
(Chua et al., 2026; South et al., 2025; Google, 2025), which addresses the first wave’ s
institutional bottleneck directly. Whether that is sufficient is an empirica l question this review
keeps open; that it differs from 1999 rests, so far, on the new infrastruc ture and is an argument
rather than a measured result.
2.2 Construct space: what agentic commerce is
We define agentic commerce as commercial exchange in which an A I agent, acting under a
mandate from a consumer, a firm, or a platform, materially shapes at lea st one stage of the
customer journey (Lemon and Verhoef, 2016). The definition has four component s that carry the
analysis, and the corpus operationalizes each. The principal is the party whose interests the agent
nominally serves. Misalignment between principal and agent is a recurring empi rical object, from
inferences about a firm agent’s motives (Farmer and Harding, 2026) to seller age nts inferring a
buyer’s willingness to pay from dialogue (Alavi and Nozari, 2026). The mandate is the scope of
authority granted, which the infrastructure layer is converting from a va gue expectation into a
verifiable artifact (Chua et al., 2026; South et al., 2025). The capability is what the agent can
execute, which we formalize as delegation depth in Section 5. The journey locus  is where in
search, evaluation, transaction, or post-purchase the agent acts, which the evide nce map of
Section 9 shows is highly uneven.
Three boundary decisions follow. Purely informational customer-service chat bots without
transactional or delegation capability fall outside scope; their large liter ature is already
synthesized (Lim et al., 2022; Ling et al., 2021), and including it would dilute the de legation
construct that defines the phenomenon. Agents from all three actor groups, cons umer-side, firm-
side, and platform-side, are in scope, because the influence relations among them are exactly
what a marketing analysis must capture. We speak of actor groups rather tha n market sides, since
the underlying exchange remains one between consumers and firms. And both waves are in
scope, because excluding the first would discard the only field-tested market evidence the domain
possesses and would sever the current cycle from its own control condition.
2.3 Theoretical apparatus
Five theoretical traditions recur across the corpus, and each is trans formed rather than merely
applied when the customer is a machine. The persuasion knowledge model describe s how targets
learn to recognize and cope with influence attempts (Friestad and Wright, 1994). The corpus
displaces it twice. Consumers deploy different persuasion knowledge against machine
persuaders. Perceived benevolence, the belief that the agent wants to ac t in the customer’s
interest rather than the company’s, becomes a decisive inference (Far mer and Harding, 2026).
Time pressure moderates whether machine appeals outperform human ones (Sha mim et al.,
2026), and persuasion intensity sets the boundary at which human and AI streamer s diverge in
live commerce (Lu and Li, 2026). Meanwhile agents themselves possess almost no per suasion
knowledge, as the manipulation results of Section 6 demonstrate, so the model a cquires a second,
machine-side referent that theory has not yet named.
Choice architecture research explains how the arrangement of options stee rs decisions (Thaler
et al., 2009). In agentic commerce the architecture doubles: designers ar range context for the
agent, and the agent arranges options for the person. Both stages are empirica lly active. Agents
inherit position and framing sensitivities (Allouah et al., 2026), execute nudging on consumers at

7
scale with an accompanying autonomy paradox (Choubey and Chakraborty, 2026), and constrain
the option sets consumers ever see, with product expertise and purchase habits dampe ning the
perceived risk of the constraint (Rabassa et al., 2022). Agency and information e conomics supply
the third lens. Delegation creates a classic principal-agent struct ure, but with a twist the corpus
documents: the agent’s conversational interface leaks the principal’s private information,
allowing seller-side inference of willingness to pay nearly one for one from dialogue alone (Alavi
and Nozari, 2026). Verified product information itself becomes a priced int ermediation layer
(Ventirozos and Shardlow, 2026), and Hayekian analysis asks whether delegated ag ents can
transmit the dispersed knowledge markets depend on (McDavid et al., 2026). The c ustomer
journey perspective (Lemon and Verhoef, 2016) supplies the framework’s horizonta l axis,
because delegation depth and evidence density vary sharply by stage, and recent w ork already
rereads the whole journey through the lens of agent intervention (Vasileva, 2025). Finally, the
psychology of algorithm reliance introduced above (De Bellis and Johar, 2020; Longoni and
Cian, 2022; Castelo et al., 2019; Dietvorst et al., 2015; Logg et al., 2019) explai ns the ceiling that
separates what agents can do from what consumers let them do. Strategic t reatments of AI in
marketing frame the managerial stakes (Davenport et al., 2020; Huang and Rust, 2021)  but stop
short of agent-native transactions, which is the territory this review maps  and the territory the
machine-marketing agenda now names (Sarstedt et al., 2026).
2.4 Positioning against prior reviews
Because five secondary studies border this one, positioning deserves more than a table. Pathak
(2010) synthesized the first-wave comparison shopping literature as decision suppor t systems
research; it remains the best guide to that system class but predates language models, covers only
the advisor level of delegation, and contains no marketing-influence or governance analysis. Ling
et al. (2021) systematically reviewed adoption of conversational agents and conso lidated the
technology-acceptance antecedents on which our Section 7 builds; its scope is the interface, not
the transaction, and agent autonomy is outside its frame. Lim et al. (2022) mapped conversational
commerce and flagged the commercial turn of conversational interfaces; written at the cusp of the
LLM diffusion, it could not yet observe autonomous purchasing, machine-directed marke ting, or
the payment layer. Raja et al. (2026) meta-analyzed 468 effect sizes on customer-level outcomes
of AI agent implementation. It provides the quantitative anchor for what Sec tion 6 defines as the
through-direction of our triad, marketing that reaches the human through an agent. As an effect-
size synthesis, it deliberately abstracts from mechanisms, journey stages, and market structure.
Balaskas (2026) is the nearest neighbor: a systematic review mapping agent ic AI in e-commerce
and its consumer effects. It confirms the momentum of the delegation l iterature but stops at the
consumer boundary. Influence on agents, agents as marketing producers, transaction
infrastructure, law, and market outcomes remain outside it, and the first wave appears only in
passing. Finally, Sarstedt et al. (2026) is an agenda-setting research note r ather than a review; it
argues that machine marketing should exist, and the present article suppl ies the systematic
evidence base, the shared constructs, and the measurement program that t he proposed
subdiscipline requires.
The comparison identifies precisely what remained undone and this review su pplies. It
contributes a two-wave corpus with verified lineage between the waves,  and the influence-
direction construct, without which marketing to agents, through agents, and by agents blur into
one undifferentiated AI literature. It integrates the consumer evi dence with the governance and

8
payment infrastructure that determines which delegation depths are reacha ble at all, adds market-
level synthesis, and releases a recomputable evidence base. Table 1 summari zes the coverage
comparison.
Table 1: Positioning against related secondary studies. Filled circle: full coverage; open circle:
partial coverage; blank cell: no coverage.
Secondary
study
Two
waves
Influence
direction
Governance and
infrastructure
Market
outcomes
Replication
package
Pathak
(2010)
  ○ ○
Ling et al.
(2021)

Lim et al.
(2022)
 ○
Raja et al.
(2026)
 ○
Balaskas
(2026)
 ○
This review ● ● ● ● ●
3 Methodology
3.1 Review design and rationale
The review follows the three stages of the SPAR-4-SLR protocol, assembl ing, arranging, and
assessing (Paul et al., 2021), is reported in line with PRISMA 2020 (Page et  al., 2021), and
adopts concept-centric synthesis so that findings are organized by construct rathe r than by paper
(Webster and Watson, 2002). We chose a domain-based systematic review over a bibliometric or
purely narrative design for two reasons grounded in the phenomenon (Snyder, 2019). Fir st, the
literature crosses disciplinary boundaries with incompatible vocabularies, so replica ble retrieval
and explicit criteria matter more than in a settled field. Sec ond, the research questions require
synthesis of findings and mechanisms, not only mapping of publication patterns, whic h rules out
a purely bibliometric design. The unit of analysis is the primary study: a journal article,
conference or workshop paper, book chapter, or working paper making an empiric al, formal,
design, or substantive conceptual contribution about AI agents shaping commercial ex change.
Working papers are eligible because the second wave is young enough that excluding them
would erase a large share of the frontier; each is labeled by type in the corpus register so that any
analysis can be repeated on the peer-reviewed subset. Figure 1 reports the com plete flow by
SPAR-4-SLR stage with PRISMA counts.

9

Figure 1: Review protocol and flow. The spine reports the PRISMA counts at each stage ; side
boxes report removals and additions with their criterion codes; brackets on the left map the
stages onto the SPAR-4-SLR protocol of assembling, arranging, and assessing.
3.2 Databases
Three databases were searched. Scopus and Web of Science provide the two broadest curated
indexes of peer-reviewed business, information systems, economics, and computer science
research, with complementary coverage of conference proceedings. EBSCO Business Source
adds business-school journals and practitioner-adjacent scholarly outlets that t he citation indexes
cover unevenly. Its cost is that it also indexes trade press, which we handl e explicitly at
screening. Together the three cover the disciplinary spread the phenomenon dem ands. Preprint
servers were not searched directly; recent unindexed work enters through forwa rd snowballing,
which retrieves it selectively through its connection to included studies rather than in bulk.

10
3.3 Search string development
The search string pairs two concept groups, the agent and the commercial exchange:
("agentic commerce" OR "agentic shopping" OR "agentic AI" OR "AI  agent*" OR
"LLM agent*" OR "LLM-based agent*" OR "language model agent*" OR
"autonomous agent*" OR "shopping agent*" OR "buying agent*" OR "machine
customer*" OR "algorithmic consumer*" OR "conversational commerce" OR
"generative engine optimi*" OR "answer engine optimi*") AND (commerce  OR "e-
commerce" OR retail* OR shopping OR shopper* OR marketing OR advertis*  OR
consumer* OR purchas* OR checkout OR payment* OR pricing OR brand*)
Concept group one was harvested from three sources: the terminology of known landmark
studies, industry protocol vocabulary, and the keyword lists of the candidate reviews in
Section 2.4. It deliberately mixes established phrases with quoted compound ter ms so that
precision comes from phrase structure rather than from narrowing the domain. Concept group
two enumerates the commercial exchange broadly, because agent studies signal commerce in
many different words. Two design decisions control precision. The string is appli ed to titles,
abstracts, and keywords in Scopus and Web of Science, which keeps the searc hed concepts
central to the retrieved work and is established practice in marke ting reviews. In EBSCO
Business Source it runs on full text, which trades precision for recall a nd explains that database’s
larger and noisier return. No publication-date restriction was applied, so both waves enter through
the database track. Snowballing additionally secures the first-wave ca non: it is densely cited by
included studies and is therefore reached reliably through reference list s, even where legacy
vocabulary such as software agent is too ambiguous for precise retrieval across three decades. A
validation set of three known relevant studies spanning the corpus’s breadth, the c onsumer-side
systematic review (Balaskas, 2026), the generative engine optimization experiments (Aggarwal et
al., 2024), and a consumer trust study (Zhao et al., 2025), was fixed before execution as a recall
check; all three were retrieved. The searches were executed i n July 2026 and returned 5,157
records: 1,465 from Scopus, 1,098 from Web of Science, and 2,594 from EBSCO Business
Source. Per-database syntax, execution notes, and raw exports are in the replication package.
3.4 Screening procedure
Table 2 states the criteria in unified form: six paired dimensions apply at  every stage, and
three additional exclusion screens apply at full text, where the inform ation to judge them first
becomes available. De-duplication by DOI and guarded normalized-title matchi ng removed 686
records, leaving 4,471 unique records. Because EBSCO Business Source indexes tra de press
alongside scholarship, source-type separation preceded screening: 1,859 news a nd trade items
were set aside as context material, leaving 2,612 scholarly records. Titles and abstracts were then
screened against the paired criteria. Before full application, all thr ee authors independently
screened an initial calibration batch against the criteria; agreement across the three raters was
substantial (Fleiss’ κ = 0.76), and disagreements were resolved by dis cussion before the
remaining records were screened. Every decision was recorded with a criterion code; the coded
decisions and the marked export sheets in the replication package preserve the full trail. Judgment
calls concentrated at two boundaries, and we state how they were resol ved. Studies of service
chatbots were included only when the agent held transactional or delegatio n capability (EC7); for
example, chatbot studies measuring purchase outcomes of conversational selli ng were retained,

11
while studies of complaint-handling dialogue quality were not. Studies of autonomous a gents
outside commerce, in energy markets, network operations, and robotics, were e xcluded under
EC1 even when auction or pricing language appeared, unless the contribution address ed
consumer-facing commerce. The review’s scope is accordingly consumer commer ce: business-
to-business settings enter only where an included study examines them directly, as with delegated
B2B data curation (Adam et al., 2025) and cross-border seller-side agents (Xia o et al., 2025), and
all other findings should be read as claims about consumer markets. This pass advanced 150
records to full-text assessment; the 2,462 records not advanced carry per-r ecord exclusion codes
in the export sheets, and two of them later entered the corpus through backward snowballing.
Table 2: Screening criteria in unified form. Dimensions one to six pair an inclusion and an
exclusion criterion and apply at all stages; dimensions seven to nine are exclusion scre ens
applied at full text.
Dimension Inclusion criterion Exclusion criterion
Subject IC1: an AI agent materially shapes a
commercial exchange or its marketing, on the
consumer, firm, platform, or market side
EC1: agent not commerce
relevant (robotics, games,
network or energy operations)
Contribution IC2: empirical, formal or analytical, design or
system, or substantive conceptual
contribution
EC2: no extractable commerce
or marketing contribution
Scope IC3: commerce or marketing constructs
present (visibility, choice, persuasion,
delegation, trust, transaction, pricing,
advertising, market outcomes)
EC3: physical or robotic agents
only
Type IC4: journal article, conference, workshop, or
chapter; working papers eligible and labeled
EC4: secondary studies and
editorials (used for positioning,
not coded as primary studies)
Language IC5: full text in English EC5: non-English full text
Access IC6: full text obtainable for assessment EC6: full text not accessible
Interaction
scope
- EC7: service chatbots with no
transactional or delegation
capability
Reporting
depth
- EC8: extended abstract or
abstract-only publication with
insufficient detail for data
extraction
Outlet
credibility
- EC9: outlet fails peer-review
credibility screening
3.5 Full-text assessment
All 150 retrieved documents were read at full text against the same  criteria plus the three full-
text screens. Thirty-eight were excluded, each with a coded reason in the  replication package.
Thirteen were secondary studies and editorials, which inform Sections 2 and 4 but are not

12
primary evidence (EC4). Eighteen were extended abstracts or abstract-only publi cations whose
reporting could not support extraction (EC8), a category dominated by conference  abstract
volumes. Three were practitioner magazine pieces outside the primary-st udy definition, two were
descriptive chapters without an extractable contribution (EC2), and one outlet  failed credibility
screening (EC9). One article’s full text is not in English (EC5): an observational  study of brand
visibility in AI-generated tourism recommendations, published with an English abstract only,
which language verification at full text moved from the provisional set to the  exclusion log. The
database track therefore contributed 112 primary studies. Two further full-text decisions illustrate
the standard applied under EC8, which excludes on insufficient reporting rather than on length. A
one-page research note reporting an eleven-month price panel collected through a shopping agent
was retained because its data and design are fully reported (Snaith, 2003). A two-page simulation
report on algorithmic pricing was retained because its market design, learning setup, and
outcomes are extractable (Schlechtinger et al., 2023). A longer conference  abstract on agent
effects on norm compliance was excluded because its design could not be extrac ted, despite a
promising question.
3.6 Snowballing
Backward snowballing examined the reference lists of all included studie s. A candidate was
admitted only when three conditions held: it is verifiably cited by included studies, with the citing
identifiers logged; it satisfies the inclusion criteria; and it contributes evidenc e or theory not
already represented. Twenty-three studies entered this way, spanning the fi rst-wave canon
(Guttman et al., 1998; Maes et al., 1999; He et al., 2003; Häubl and Trifts, 2000; S mith and
Brynjolfsson, 2001; Gal and Elkin-Koren, 2016), the delegation and algorithm-reliance li terature
of the bridge decade (De Bellis and Johar, 2020; Longoni and Cian, 2022; Castel o et al., 2019;
Dietvorst et al., 2015; Logg et al., 2019; Puntoni et al., 2021; Hoffman and Novak, 2018),
persuasion knowledge theory (Friestad and Wright, 1994), and recent computational work on
generative visibility, silicon samples, and advertising mechanisms (Aggarwal et al., 2024; Kumar
and Lakkaraju, 2024; Sarstedt et al., 2024; Brucks and Toubia, 2025; Brand et al., 2023; Duetting
et al., 2024; Dubey et al., 2024; Hajiaghayi et al., 2024; South et al., 2025). Forwar d snowballing
tracked citations of three central included studies and admitted five. Thr ee extend the agent
purchasing audit (Allouah et al., 2026) toward two-sided agentic markets, purchasing operations,
and information markets (Alavi and Nozari, 2026; Cao and Hu, 2026; Ventirozos and Shar dlow,
2026). One extends the anthropomorphic advertising analysis (Kim et al., 2025) to conversational
advertising and consumer welfare (Hermann et al., 2026), and one extends the pla tform
regulation analysis (Bostoen and Krämer, 2026) to liability allocation (Zhang and He, 2026). The
final corpus contains 140 primary studies; the register preserves the original study identifiers P1
to P141 with P75 recorded in the exclusion log, and Appendix A lists the corpus.
3.7 Data extraction and coding
A structured extraction form captured eight fields for every primary st udy. They are
bibliographic data, research wave (first wave before 2022, second wave from  2022), provenance
track (database, backward, or forward snowballing), influence direction, c ustomer journey stage,
delegation depth, method family, and a one-line coded finding. Two of these sch emes required
development rather than adoption, and both were built iteratively. The influence-direction scheme
began deductively from the intuitive distinction between agents as marketi ng targets and agents
as marketing channels. It was then refined inductively over the corpus unti l every study fit

13
exactly one primary direction. The result is six values: marketing to age nts, marketing through
agents, marketing by agents, consumer delegation and response, market outcomes, and
governance and infrastructure. The delegation-depth ladder began from autonomy levels implicit
in the systems literature and stabilized after iteration at five  values, D0 to D4, defined in
Section 5. The decisive test was that first-wave decision aids, current voi ce assistants, and
mandate-based payment designs all locate unambiguously. Journey stages follow the esta blished
purchase-journey stages with a cross-journey value for studies spanning stages (Lem on and
Verhoef, 2016). Method families group the recorded study designs into eight values: exper iment,
design and system, conceptual and methods, survey, legal and policy, formal m odel, simulation
and audit, and field study; the family mapping is released with the coding scheme . The complete
scheme with category definitions, the full coded matrix, and the per-study findings are in the
replication package; every count, table, and data figure in this article re computes from that
matrix.
3.8 Quality assurance
Six safeguards address the standard threats. Against retrieval bias, w e used three databases
with complementary coverage, a validation set fixed before execution an d fully recovered, and
snowballing in both directions with verified lineage. Snowballing contributed 28 of the 140
studies, and it specifically repairs the vocabulary drift that any fixed se arch string suffers in a
fast-moving field. Against selection bias: paired criteria fixed before screening, a three-author
calibration with measured agreement, and criterion-coded decisions preserved record by record.
Against extraction error: full-text reading of all included studies, wi th optical character
recognition applied where source files lacked a text layer, and verific ation of every quantitative
claim in this article against the source document before inclusion. Against  source-quality
distortion: separation of trade press before screening, labeling of working papers, and the
credibility screen EC9. Against synthesis opacity: concept-centric writing wi th the coded register
throughout, and figures whose every element derives from the coded matrix. Against
irreproducibility: release of the complete decision trail and coded ma trix. After the three-author
calibration, the remaining screening and the coding were divided between the authors.
4 Corpus overview
4.1 Temporal structure: two waves and the bridge between them
Figure 2 shows the corpus over time, and we read its shape as informative . The first wave
contributes 35 studies published between 1994 and 2021, with its agent-systems core
concentrated between 1998 and 2010; the second wave contributes 105 studies, of which 96
appeared in 2024 or later and 56 in the first seven months of 2026 alone. Betwe en the systems
core and the LLM era lies the bridge decade described in Section 2.1. Its  thirteen studies from
2011 to 2021 show agent building receding while four other things accumulate: the psychology
of algorithm reliance, the legal category of the algorithmic consumer , residual shopbot market
evidence, and the landmark disclosure field experiment (Dietvorst et al. , 2015; Logg et al., 2019;
Castelo et al., 2019; Gal and Elkin-Koren, 2016; Pathak, 2012; Luo et al., 2019). The tem poral
structure is therefore, on our reading, not a boom, a silence, and a boom, but a ca pability wave, a
preconditions decade, and a second capability wave that arrives with its behaviora l and legal

14
groundwork partly laid. This reading matters for how the old studies are used, a nd the corpus
uses them in three distinct roles. Some are foundational theory whose constructs the second wave
still runs on: the buyer-behavior mapping of agents to journey stages (Guttman et al ., 1998),
persuasion knowledge (Friestad and Wright, 1994), and the algorithmic consumer as a legal-
economic category (Gal and Elkin-Koren, 2016). Some are baseline evidence tha t no second-
wave study has yet matched in ecological validity. The shopbot brand-premium field study
(Smith and Brynjolfsson, 2001), the price-panel test of the law of one pric e at a live comparison
agent (Snaith, 2003), and the machine-selling disclosure experiment on a production c hannel
(Luo et al., 2019) remain the field’s principal field results. Early evi dence that shopping agents
can counter the inaction inertia that follows a missed sale complements t hem (Andrews, 2008).
And some are cautionary mechanism studies whose dynamics recur: seller ga ming of comparison
agents (Hajaj et al., 2015; Hajaj et al., 2017) anticipates generative engine opt imization, and
pricebot price-war cycling (Greenwald and Kephart, 1999) anticipates the algorithmic
coordination question (Schlechtinger et al., 2023). Reading the corpus without the se studies
would make the second wave look unprecedented; reading it with them turns seve ral second-
wave results into replications across a technology generation, which is a materially stronger
evidential claim.

Figure 2: Primary studies per publication year (N=140; 2026 covers January to July). Stacked
segments distinguish the first wave of shopbot and pre-LLM agent research from the sec ond,
LLM-based wave; the annotated spans mark the agent-systems era, the bridge decade in which
delegation psychology and the legal vocabulary matured, and the LLM era.
4.2 Disciplinary and outlet structure
The corpus crosses five literatures, and the crossing points are informative . Marketing and
consumer research contribute the largest block, including work in Journal of Marketing Research,
Journal of Consumer Psychology, Journal of Business Research, Psychology and Marketing,
Journal of Retailing, Journal of Retailing and Consumer Services, Journal of A dvertising
Research, Journal of Service Research, and Journal of Marketing Analytics (Schultz and Kaiser,

15
2025). Information systems contributes the delegation-interface and field-exper imental work,
including Information Systems Research, Decision Support Systems, Electronic Mar kets, and the
major IS conferences. Computer science contributes the audits, benchmar ks, attacks, and system
designs through KDD, AAMAS, AAAI, and a fast-moving working-paper frontier. Economics
and operations contribute the mechanism design and market models, and law contri butes the
liability, competition, and consumer-protection analyses. The pattern that matters, observed
during full-text coding rather than through a formal citation analysis, is asy mmetric awareness.
The computer science studies in the corpus engage marketing constructs frequently, citing
persuasion, brand, and choice, while the marketing studies engage the computational  frontier
rarely. The two-wave gap of Section 2.1 thus repeats as a two-community ga p within the second
wave. One consequence is duplicated discovery: nudge sensitivity of agents is establi shed
computationally (Allouah et al., 2026) while marketing studies separately establ ish consumer
perception of agentic nudging (Choubey and Chakraborty, 2026), with neither literature citing the
other. The framework in Section 9 is designed to make such pairs visible, and t he community
entry points in Section 9.4 are designed to route them to each other.
4.3 Methods and the maturity of the evidence
Figure 3 profiles the corpus by method family and by primary influence direc tion.
Experiments dominate with 47 studies, followed by design and system contributions (32),
conceptual and methods work (27), surveys (8), legal and policy analyses (8), formal economic
models (7), simulation and audit studies (6), and field studies (5). Two readings f ollow. The
optimistic one: the field has passed the purely conceptual stage quickly, and causa l designs are
the modal contribution, including multi-study packages that combine several experiments with a
field component (Shamim et al., 2026; Lei et al., 2025; Liu et al., 2025). The cr itical one: only
five studies have field data or a field experiment as their primary desi gn (Adam et al., 2025;
Zhang et al., 2026; Snaith, 2003; Luo et al., 2019; Smith and Brynjolfsson, 2001), two of  them a
generation old; several experimental packages add a field component (Li u et al., 2025; Lei et al.,
2025; Frank et al., 2026), but no study analyzes production transaction data at scale. A reading
convention follows from this profile. Throughout the synthesis we name the evidence type behind
each claim: an experiment, a field study, a survey, a formal model, a desi gn contribution, or a
conceptual analysis. Unless several studies are cited, a finding rests on a si ngle study whose
boundary conditions are still open. The consequence is a specific evidential a symmetry that
recurs throughout this review: mechanisms are established with experimental confide nce, while
market consequences rest on models, simulations, and dated field anchors. The asymmetry is not
a reason for agnosticism, because the mechanisms are consistent across studies. But they come
almost entirely from laboratory and online-panel settings, so their external validity in live
markets is largely untested. That is the reason for the measurement a genda of Section 10, which
exists to close exactly this gap.

16

Figure 3: Corpus profile (N=140). Panel (a) reports the eight method families; panel (b) reports
the six primary influence directions. Both recompute from the released coding matrix.
5 RQ1: Actors and the delegation ladder
5.1 Actor families in three institutional roles
The corpus describes commerce-capable agents operated from three inst itutional roles, on
behalf of consumers, of firms, and of platforms, and keeping the roles apart i s a precondition for
the influence analysis of Section 6. On the consumer side, the lineage r uns from first-wave
decision aids, comparison engines, and negotiation marketplaces (Häubl and Trifts,  2000; Yuan,
2003; Karacapilidis and Moraıtis, 2001) through voice assistants whose recom mendation
behavior and choice framing are now well studied (Flavián et al., 2023; Rohde n et al., 2025;
Rabassa et al., 2022) to general-purpose assistants and autonomous shopping systems tha t span
the journey (Patil et al., 2026; De Bellis and Johar, 2020; Potluri and Chittim alla, 2026).
Specialized designs extend the family: agents for subjective product needs (Da mmu et al., 2025),
governed basket execution with inventory-aware actions (Liu and Chen, 2026), and dee ply
personalized super-assistants spanning many life domains (Hasselwander et al ., 2026). On the
firm side, the corpus documents selling agents entering sales roles (Gonzalez  et al., 2026; Luo et
al., 2019) and influencers delegating audience replies to social agents (Zhang et al., 2026). A
production line of marketing-by-agents sits behind them. It spans campaign and cont ent
generation (Aslam et al., 2026; Ahn and Kim, 2025), banner design (Wang et al., 2025),
advertising keyword generation (Chen et al., 2025), branding and personalization systems (Puri et
al., 2026), agentic traffic optimization (Zhang, 2025), cross-border selection and marketing
agents (Xiao et al., 2025), and agentic analytics with interpretability and e valuation layers (Rudra
et al., 2026; Rudra and Agrawal, 2025; Lu et al., 2026). On the platform and infr astructure side
sit the payment, identity, and authorization designs (Chua et al., 2026; Vaziry et al., 2025;
Bhushan et al., 2026; South et al., 2025), trust-aware purchasing frameworks and mul ti-agent
commerce architectures (Gadi et al., 2026; Mishra et al., 2025), and the  semantic and security
scaffolding of decentralized retail (Bernovskis and Sceulovs, 2026; Pachaiyappan, 2026). A
fourth family is synthetic: agents standing in for market participants in research itself, as silicon
respondents (Sarstedt et al., 2024; Brand et al., 2023), simulated consumer populati ons (Chu et

17
al., 2025), and benchmark shoppers (Ling et al., 2026; Wang et al., 2026b). The same underlying
capability therefore appears in four institutional roles, and a study’s cont ribution is legible only
relative to the role.
5.2 The delegation ladder
Comparing this literature requires a common scale for how much authority t he agent holds,
which no primary study supplies. We therefore code every study on a five-leve l delegation
ladder, defined in Table 3 and summarized with corpus counts in Figure 4. The ladder’s ordering
principle is where consumer oversight sits relative to the act. At D 0 and D1, oversight precedes
every consequential action; at D2 it is continuous; at D3 it is delimi ted in advance by a mandate;
at D4 it is retrospective. The scale absorbs the corpus without remainder: f irst-wave decision aids
sit at D1 (Häubl and Trifts, 2000), conversational co-shopping and eye-tracked  delegation
interfaces at D2 (Balaskas et al., 2026; Lee, 2026), mandate-scoped executor s and one-click
delegation studies at D3 (Choubey and Chakraborty, 2026; Frank et al., 2026; Gadi et a l., 2026),
and autonomous purchasing designs, audits, and market models at D4 (Allouah et al., 2026; Chua
et al., 2026; Cao and Hu, 2026).
Table 3: The delegation ladder. Counts give primary studies whose empirical or design foc us sits
at each level (N=140; D0 is an anchor level and attracts no coded studies because purely
informational interfaces are outside scope).
Level Name Definition Corpus count
D0 Informer Surfaces information; the consumer performs
every task
0 (anchor level)
D1 Advisor Recommends, ranks, or filters; the consumer
decides and executes
61
D2 Co-pilot Executes sub-tasks interactively under continuous
consumer oversight
15
D3 Scoped executor Completes bounded transactions under an
explicit, limited mandate
17
D4 Autonomous
delegate
Plans and transacts across the journey; consumer
oversight is retrospective
47

18

Figure 4: The delegation ladder with corpus counts. Delegated autonomy increases f rom left to
right; the axis beneath marks the movement of consumer oversight from before the  act to after it.
The distribution is bimodal: evidence concentrates at the advisor level, discourse  at the
autonomous level, and the operational middle is thin.
The distribution across the ladder is the single most consequential descriptive  fact in the
corpus, because the two peaks rest on opposite kinds of evidence, the reverse of wha t one would
expect. D1 holds 61 studies, and its evidence is behavioral: 26 experiments, 4 field studies, and
22 working systems. D4 holds 47 studies, but only six of them involve human participant s or
field data at all; the level is carried by 19 conceptual analyses, 8 legal analyses, 5 formal models,
7 system designs, and the audit work. The middle of the ladder, where products w ill actually
operate first, holds 32 studies. In short, the level we understand behaviorally is the le vel being
automated away, and the level being built is the level we understand least  behaviorally. Stated as
a finding: the behavioral science of full delegation consists of six empirica l studies. Every trust
result in Section 7 and every market model in Section 8 should be read a gainst that base rate, and
the agenda in Section 10 treats populating D2 to D4 with human evidence as its first priority.
5.3 Reading the waves against each other
The two waves divide the ladder in a way that sharpens the continuity thesi s. The first wave
contributed 13 of the 61 advisor-level studies and, strikingly, 13 of the 47 autonomous-level
studies. Its negotiation protocols, bidding mechanisms, and market designs (Wang et al., 1999;
Kehagias et al., 2005; Iyer and Pazgal, 2003) imagined D4 while its deployed systems operated at
D1, and its field-defining survey explained the gap institutionally (He et al., 2003). The second
wave repeats the pattern at higher capability: its consumer evidence st ill concentrates at D1 and
D2, while its D3 and D4 contributions are dominated by infrastructure designs, audi ts, and law
rather than by consumer behavior (Chua et al., 2026; South et al., 2025; Allouah et  al., 2026;
Busch, 2025). The gap between what agents can do and what consumers observably let the m do
has therefore survived the technology shift so far. That persistence is one reason the corpus’s

19
governance layer, the subject of Section 7, treats verifiable mandates rather than raw capability as
the binding constraint, echoing the first wave’s own diagnosis that trust and interoper ation, not
intelligence, gate delegation (He et al., 2003).
6 RQ2: The influence triad
Marketing influence in agentic commerce runs in three directions that the literature routinely
conflates: to the agent, through the agent, and by the agent. Figure 5 defines  the triad; the
subsections synthesize each direction and then the ways the directions com bine, which is where
the strategically decisive patterns appear.

Figure 5: The influence triad. The agent is target (marketing to agents), channel (mark eting
through agents), and producer (marketing by agents); the consumer grants the mandate that
gives the triad its stakes. Counts give primary studies whose principal contribution sit s in each
direction.
6.1 Marketing to agents: the machine as target
Consider a merchant whose pages an assistant never cites. In a controlle d experiment,
rewriting those pages with citations, statistics, and clearer structure  raised their presence in
generated answers by up to 40 percent (Aggarwal et al., 2024). That is marketing t o agents.
Eleven studies make the agent itself the marketing target, and together t hey establish two things:
machine visibility can be deliberately manufactured, and the same tech niques that make content
legible to agents also enable manipulation. Both patterns replicate a fir st-wave precedent. The
foundational result is experimental: generative engine optimization, restruc turing content with
citations, quotations, statistics, and authority signals, raises a source’s visi bility in generated
answers by up to 40 percent, with effects varying across domains and query type s (Aggarwal et
al., 2024). Around that result has grown a practice literature formalizi ng visibility strategy and
monitoring for the new gatekeepers (Anca, 2026; Uppin and Uppin, 2025). An industrial

20
complement shows that retail catalogs themselves can be made machine-r eadable at scale, using
brand knowledge bases and LLM agents to repair and match product data (Ce ker et al., 2026).
Observational work adds two cautions. Agents interacting with live web adve rtising respond to
keyword relevance and structured data rather than to visual salience (Stöckl and Nitu, 2025). And
measured brand presence in generated recommendations is itself unstable: identical queries return
different brands across systems, model versions, and points in time (Kumar a nd Lakkaraju, 2024;
Allouah et al., 2026). The manipulation side is documented with unusual directness. Strategic text
sequences inserted in product pages raise a target product’s rank in model r ecommendations
(Kumar and Lakkaraju, 2024). LLM-driven shilling frameworks (coordinated fak e identities that
promote or demote items) with feedback memory outperform traditional a ttack baselines against
recommender systems (Li et al., 2026a). Advertisement embedding attacks hijack model outputs
through service interception or backdoored open-source checkpoints, with a backdoored
checkpoint reproducing the attacker’s preset responses in full (Guo et al., 2025). And indirect
prompt injection steers autonomous web navigation agents from inside the pages  they read
(Johnson et al., 2025). The first wave saw the same sequence: as soon as compariso n agents
concentrated demand, sellers manipulated them through selective disclosure and strategic
ordering (Hajaj et al., 2015; Hajaj et al., 2017). The lesson carried across twenty-five years is that
any machine gatekeeper of demand creates an optimization market on its inputs. The practical
difference this time is that the inputs are natural language, so t hat market is open to every content
producer rather than to price-feed engineers alone.
6.2 Marketing through agents: the machine as channel
Consider a shopper who must decide under time pressure: in that condition, i dentical
recommendations persuade more when delivered by an AI agent than by a human, bec ause
scrutiny of the machine is suspended (Shamim et al., 2026). That is marketing through agents.
Twenty-three studies treat the agent as the channel through which firms rea ch people, and they
connect into a chain that runs from message design to consumer welfare , welfare here meaning
realized consumer surplus and autonomy rather than a technical term. At the message end,
modality shapes persuasion. In a single experiment series, text-based ass istants outperformed
voice on concrete product actions, raising product-link requests from 29.0 to 48.1 perc ent, with
mental imagery as the proposed mechanism (Nguyen et al., 2026). Whether t he gap holds across
product categories and tasks is untested. Conversational cues carry weight ma chines were not
expected to have. Conversational fillers such as a hesitant hmm, added to humani ze agents,
backfire in selling contexts: across one field experiment and four studies, t hey trigger suspicion
of ulterior motives and lower purchase intentions (Liu et al., 2025). Chatbot interfaces themselves
shift product and price perceptions (Sidlauskiene et al., 2023), and endorser de sign shifts ad
engagement between human-like and cartoon-like agents (Park et al., 2025). Anthropomo rphic
agents that visibly use personal data trigger an uncanny valley of mind, th e discomfort that arises
when a machine appears to read one’s thoughts, in personalized advertising; algorithmic
disclosure of data handling mitigates it (Kim et al., 2025).
Perceived motives are decisive: perceived benevolence, the inference t hat the agent serves the
customer rather than the company, shapes compliance when ulterior motive s are salient (Farmer
and Harding, 2026), and persuasion knowledge theory supplies the mechanism (Friestad and
Wright, 1994). Timing and pressure matter in ways that flip the human advantage: i n checkout
charity, AI-led appeals outperform human appeals under high time pressu re because they impose

21
lower social demands, across four studies (Shamim et al., 2026). Field evi dence scales the
channel. In one large-scale field experiment, undisclosed chatbots sold as effectively as proficient
human workers and four times more effectively than inexperienced ones, whil e pre-conversation
disclosure of machine identity cut purchase rates by 79.7 percent, with discl osure timing as the
documented boundary condition (Luo et al., 2019). Live-stream commerce experiments a dd a
second boundary condition: under high persuasion intensity, AI streamers outperform hum an
streamers because intense appeals from a machine are attributed t o programmed execution rather
than strategic manipulation, which lowers suspicion and lifts purchase inte ntion (Lu and Li,
2026).
The channel’s manipulative side and its governance are studied with equal energy. Agent-
executed nudging raises an autonomy paradox in which consumers perceive both assistanc e and
manipulation, mediated by persuasiveness, trust, and ethical acceptance (Choube y and
Chakraborty, 2026). Biased option sets from voice assistants create dependence r isks that
consumers’ product expertise and purchase habits dampen (Rabassa et al., 2022). Empat hic voice
assistants can steer choices toward sustainability targets (Mari and Alabed, 2025), and
personalization by agents can undermine the very autonomy it serves, the ema ncipation paradox
(Anandan Karichalil and Kaul, 2026). Disclosure design, not merely disclosure presence,
emerges as the operative lever: when an AI agent presents an unfavorabl e personalized price,
agent presence softens rejection through perceived-justice and privacy pat hways, and
environment-based explanations outperform user-based ones (Peng et al., 2023). At the  market
end of the chain, mechanism design moves advertising inside the generated answer i tself. Token
auctions aggregate advertiser preferences into a single generated output (Duetting et al., 2024),
auctions allocate slots in LLM summaries with incentive guarantees (Dubey et al., 2024), and
retrieval-augmented auctions price placement inside answers (Hajiaghayi e t al., 2024). Welfare
analysis names the stakes of conversational advertising for consumers and platforms (Hermann et
al., 2026). The composed chain, message design to motive inference to disclosure architecture to
auction, is the through-direction’s contribution, and its weakest empirical link is at  the end: the
auction layer is formally mature and behaviorally untested.
6.3 Marketing by agents: the machine as producer
Consider an influencer who lets an AI answer follower comments: in a f ield study, receiving
such a reply raised users’ subsequent commenting by about 41 percent (Zhang et a l., 2026). That
is marketing by agents. Twenty-two studies make agents the producers of ma rketing work, and
the direction is where deployment runs furthest ahead of consumer-facing evid ence. Content and
campaign production is operational. Design contributions cover autonomous content gener ation
and management for social media marketing (Aslam et al., 2026), multim odal banner design
agencies (Wang et al., 2025), self-reflective ad keyword generation (C hen et al., 2025), hyper-
personalized branding systems (Puri et al., 2026), and agent-driven marketplace t raffic
optimization (Zhang, 2025). One deployment study measures engagement differences across
Twitter/X, Discord, and Telegram (Ahn and Kim, 2025). Selling itself is being reorga nized. Sales
scholarship maps how agentic AI redefines selling roles and sales processes (Gonzalez et al.,
2026). Field evidence on delegated B2B data curation shows the customer resp onse is task-
contingent: algorithmic requesters match or beat human requesters for data e nrichment, while
customers prefer humans for data reconciliation, where error concerns dominate (Adam et al.,
2025). And a difference-in-differences field study of influencer reply dele gation finds that

22
receiving an AI reply raises users’ subsequent commenting by about 41 percent, w ith gains
concentrated among loyal followers and attenuated for commercialized inf luencers (Zhang et al.,
2026).
An analytics layer is forming around the producers: interpretable multi- agent decision support
(Rudra et al., 2026), heuristic-first evaluation frameworks that judge out put quality, actionability,
and trust (Rudra and Agrawal, 2025), and agentic A/B testing that runs LLM agent s through live
websites as synthetic participants (Lu et al., 2026). The synthetic-consumer strand supplies both
the promise and the sharpest caution. LLMs can generate silicon samples for c onsumer and
market research (Sarstedt et al., 2024; Brand et al., 2023), and multi-age nt populations reproduce
social patterns such as conformity toward popular establishments (Chu et al ., 2025). The caution
is that prompt architecture itself induces methodological artifacts: response-order and label biases
that differ across models. Moving from GPT-3 to GPT-4 changes the arti facts without removing
them, not necessarily for the better (Brucks and Toubia, 2025). Benchmarks give the direction its
evaluation substrate: persona-guided shopping simulation (Ling et al., 2026) and inte nt-grounded
real-catalog benchmarks (Wang et al., 2026b) standardize what a competent shoppi ng agent
means, and strategy-level frameworks map the field’s opportunities and firm-perf ormance stakes
(Puvvadi et al., 2025; FOLTEAN and HERA, 2026; Mirzayi and Talajouran, 2025). The
direction’s open flank is the consumer: almost none of the production literat ure measures how
people respond to being marketed to by machine-made campaigns at scale , which the agenda
addresses through the disclosure and susceptibility propositions.
6.4 Compositions: where the directions interact
The three directions do not stay separate in deployment; they combine, and t hree
combinations, patterns in which one direction feeds another, organize much of  what is
strategically novel. The first is legibility-to-persuasion. To-direction wor k makes offers visible to
agents (Aggarwal et al., 2024; Ceker et al., 2026), and through-direction work conver ts visibility
into influence on the human. Firms therefore optimize two coupled funnel s, one into the model’s
answer and one from the answer into the person, and auction design (Dubey et al ., 2024)
monetizes the seam between them. The second is the synthetic optimization loop. By-direction
producers generate content, agentic testing evaluates it with agent judges ( Lu et al., 2026; Rudra
and Agrawal, 2025), and to-direction results imply the winning content is whatever agents prefer.
The loop can therefore drift toward machine-readable persuasion wit hout any human in the
training signal, and the prompt-artifact results (Brucks and Toubia, 2025) sa y the drift’s direction
depends on the model version. The third is proxy manipulation: when the buyer is an age nt,
influencing the proxy rather than the principal becomes the rational strate gy, a framework the
corpus states explicitly (Bilgihan et al., 2026) and the attack literature o perationalizes (Kumar
and Lakkaraju, 2024; Li et al., 2026a; Johnson et al., 2025). All three compositions  share a
governance implication developed in Section 7: the integrity of agentic commerce depends on the
integrity of the agent’s information diet, which no single firm controls.

23
7 RQ3: Trust, acceptance, and the governance infrastructure
7.1 What determines whether consumers delegate
The delegation direction is the corpus’s largest at 42 studies. We read its findings causally in
one direction: the six families in Table 4 are antecedents that shape t rust, and trust in turn shapes
the willingness to delegate; experienced delegation then feeds back on tr ust, but that feedback is
thinly studied. Signals of the agent’s competence and performance are the  first family. Chain-of-
thought explanations raise perceived knowledge and behavioral intentions, mediated by trust and
privacy concerns (Ebrahimi et al., 2026), and extended acceptance framewor ks confirm
performance expectancy as a core path (Zhao et al., 2025; Balakrishnan a nd Dwivedi, 2024).
Transparency operates through cognitive trust: algorithmic transparency shows a  strong path to
cognitive trust, while outcome accountability builds affective trust (Wang e t al., 2026a). Eye-
tracking evidence adds that the smallest amount of transparency that ch anges decisions is the
amount users can act on. Cues must be actionable and consistent with users’ decision criteria, and
comfort concentrates where outcomes are immediately observable and actions reversible
(Balaskas et al., 2026; Elkhoudary, 2025). Practitioner-facing treatments nam e the underlying
tension a transparency paradox (Bansal and Bansal, 2026).
Motive inference is the third family: benevolence attributions (Farmer  and Harding, 2026),
ulterior-motive access (Shamim et al., 2026), and persuasion knowledge (Frie stad and Wright,
1994) govern whether help reads as service or as selling. Social and affecti ve design is double-
edged. Empathic voice design raises consumer responses in voice commerce (Mari et al., 2024),
and fluent language embodiment shapes credibility conditional on consumption goals ( Schwede
et al., 2026). But humanizing fillers can backfire through ulterior-motive sus picion (Liu et al.,
2025), anthropomorphism helps only until it starts to feel intrusive, the uncanny regi on (Kim et
al., 2025), and empathic steering of sustainable choices raises its own concerns (Mari and
Alabed, 2025). Risk perception, the fifth family, is not a simple deterrent . An inverted-U
relationship appears in autonomous shopping: moderate perceived risk sustains e ngagement by
preserving vigilance, while both very low and very high risk suppress it (Wa ng et al., 2026a). A
privacy calculus governs what consumers disclose to agents in the first plac e (Dey and Kumar,
2026), and perceived benefits, particularly experiential benefits, drive a cceptance of high-
autonomy assistants in scarcity settings, with behavioral evidence from real ad clicks (Frank et
al., 2026). Individual and cultural differences close the list: value dimensions in conversational
commerce (Schultz and Kaiser, 2025), acceptance antecedents of super-as sistants and latent
classes of delegation willingness in the Philippines (Hasselwander et al., 2026; Hasselwander,
2026), millennial attribute preferences (Sharma et al., 2024), and cross-c ountry first-wave
comparisons (Pilı́k et al., 2016).
A note on causal direction before the families. In nearly all of these studies the antecedent is
manipulated or measured first, and trust, acceptance, or delegation inte ntion is the outcome, so
the documented arrows run from antecedent to trust. Feedback in the other direction, from
experienced delegation back onto trust, is essentially unstudied, and the table should be read with
that asymmetry in mind.

24
Table 4: Six antecedent families of consumer trust and delegation, with representativ e primary
studies and the headline pattern each family contributes.
Antecedent
family
Documented effect (antecedent to
trust or delegation intention)
Representative studies
Agent
competence and
performance
Perceived competence raises trust;
explanations of reasoning raise
perceived knowledge and intentions
Ebrahimi et al., 2026; Zhao et al.,
2025; Balakrishnan and Dwivedi,
2024
Transparency and
control
Transparency builds cognitive trust
when cues are actionable and actions
reversible
Wang et al., 2026a; Balaskas et al.,
2026; Elkhoudary, 2025
Motive inference Benevolence attributions and ulterior-
motive access decide whether help
reads as selling
Farmer and Harding, 2026;
Shamim et al., 2026; Friestad and
Wright, 1994
Social and
affective design
Humanizing cues are double-edged:
empathy helps, fillers backfire, and
heavy anthropomorphism starts to feel
intrusive
Mari et al., 2024; Liu et al., 2025;
Kim et al., 2025; Mari and Alabed,
2025
Risk and benefit
calculus
Risk shows an inverted-U; experiential
benefits drive high-autonomy
acceptance
Wang et al., 2026a; Frank et al.,
2026; De Bellis and Johar, 2020
Individual and
cultural
differences
Value dimensions, segments, and
demographics stratify delegation
willingness
Schultz and Kaiser, 2025;
Hasselwander et al., 2026;
Hasselwander, 2026; Sharma et al.,
2024; Pilı́k et al., 2016
Beyond the antecedents, the delegation literature contributes three findings that reframe what
delegation does to the consumer. Delegation changes downstream behavior, not only choice .
Across one field study and four experiments, consumers behave less ethically after encounters
with servant-framed agents than partner-framed ones, through anticipatory m oral disengagement
(Lei et al., 2025). And agents shift intertemporal preferences toward sooner rewards by
lengthening perceived delay (Li et al., 2026b). Delegation redistributes cogni tion: first-wave
decision aids already restructured consideration sets (Häubl and Trifts, 2000; Cooke et al., 2002),
and current assistants inherit that architecture with larger scope (Vasil eva, 2025). And delegation
raises identity-level questions the survey and critical literatures ma ke explicit: from consumer
sovereignty toward algorithm dependency (Binswanger, 2025), algorithmic consumer cult ure
(Airoldi and Rokka, 2022), and a taxonomy of consumers’ relationships with conversational
agents and their wellbeing implications (Alabed et al., 2024). The wave-one comparison again
sharpens the picture. The first wave stated its trust problem as social willingness plus institutional
readiness (He et al., 2003). The second wave has now measured the social side in detail, while the
institutional side has become its own research program, to which we turn.
7.2 Governance and transaction infrastructure
Seventeen studies form the governance direction, and their joint claim is tha t delegation depth
is an institutional variable before it is a psychological one. The design str and builds the mandate.

25
Conversational payment systems pair agent-to-agent protocols with three-mandate verification
separating intent, cart, and payment (Chua et al., 2026), and authenticated dele gation frameworks
bind agent actions to authorizing humans with scoped permissions (South et al., 2025).
Blockchain identities and micropayment rails extend agent-to-agent protocols (Vaziry et al.,
2025), risk-adaptive authorization scales checks with transaction risk (Bhushan et al., 2026), and
trust-aware purchasing architectures demonstrate live marketplace inte gration (Gadi et al., 2026).
Semi-autonomous commerce models, semantic-web retail taxonomies, and sec urity risk analyses
complete the stack (Sümer et al., 2025; Bernovskis and Sceulovs, 2026; Pac haiyappan, 2026).
The first wave’s secure negotiation protocols are the direct ancestors  (Wang et al., 1999), and the
industry protocols now deployed (Google, 2025; OpenAI and Stripe, 2025; Visa, 2025;
Mastercard, 2025) implement, in production form, what the design strand prototypes.
The legal strand allocates the risk the designs create. Payments law maps the regulatory
perimeter of agent-initiated payment and its fraud-detection consequen ces, including the growing
difficulty of distinguishing automated systems presenting human credentials (A mariles et al.,
2026). Consumer law confronts doctrines built on human assent: contract format ion, information
duties, and withdrawal rights all presume a person at the interface, a nd agent transactions strain
each (Busch, 2025; Solanki, 2026). Liability is analyzed as a dynamic allocation among
developers, users, and platforms, scaled by the agent’s degree of autonomy and the  foreseeability
of its conduct (Zhang and He, 2026). Competition analysis asks whether the Digita l Markets
Act’s gatekeeper duties anticipated assistant-layer gatekeeping and finds t he fit imperfect
(Bostoen and Krämer, 2026). Trademark analysis asks what brand distinctiveness m eans when
the beholder is a model (de Amstalden and Schafer, 2020), and anti-manipulati on doctrine is
tested against autonomous tactics that emerge without human intent (Brenner, 2026) . The
strand’s founding text predates the wave: the algorithmic consumer was named, and its
competition consequences anticipated, in 2017 (Gal and Elkin-Koren, 2016). Read together, t he
two strands converge on this review’s central governance thesis: the unit that  must be trusted,
verified, and litigated is not the agent but the mandate, the authenticate d, scoped grant of
authority. The same object that makes payment safe (Chua et al., 2026; S outh et al., 2025) is the
object that makes liability assignable (Zhang and He, 2026; Busch, 2025) and market ing
attribution possible, a convergence the discussion develops into the instrument of mandate-bas ed
attribution.
8 RQ4: Market-level consequences
8.1 What the audits show about machine demand
The market direction’s most consequential second-wave evidence is a si ngle large audit of
commercially deployed purchasing agents (Allouah et al., 2026). Because it is one study, its
findings should be read as the first stylized facts of machine demand rat her than settled
regularities. Agent choices exhibit homogeneity, concentrating demand on a few modal  products
while ignoring others entirely. Position biases are large even in text-only int erfaces, and they are
unstable across providers and model versions, to the point that two successive mode l generations
exhibit nearly opposite position preferences. Agents penalize sponsored tags whi le rewarding
platform endorsements, and their sensitivities to price, ratings, and revie ws vary sharply across
models. Every one of these facts has a first-wave shadow with the human in the loop: demand

26
concentration at ranked interfaces, position effects, and the survival of brand premia at a shopbot
where comparison was nearly free (Smith and Brynjolfsson, 2001). The differenc e is that the
second wave’s chooser is a manufactured artifact whose biases are ven dor-set and shift with
updates. What used to be consumer psychology becomes platform configuration, and mode l-
version risk becomes a new category of demand risk that brand managers have never had to price.
8.2 Structure, pricing, and coordination
Formal and simulation work extends the audit facts into market structure. Two-sided models
of agentic markets identify preference leakage as a structural for ce. Because a buyer agent’s
dialogue must be coherent with its principal’s preferences, sellers can infe r willingness to pay
nearly one for one from conversation alone, collapsing the information asymme try that protects
consumer surplus; confidentiality instructions are only partly effective (Alavi  and Nozari, 2026).
Operations models of solicit-then-suggest purchasing derive how agents should bala nce asking
questions against showing products, with solicitation depth and assortment breadth as formal
substitutes (Cao and Hu, 2026). Optimal solicitation follows a water-fill ing rule: the agent keeps
asking where uncertainty about the consumer is deepest, until further questions a dd less than
showing products would. Information-market designs price verified product informat ion itself,
creating micro-transaction markets for the inputs agents buy on (Ventirozos and Shardlow, 2026).
A formal welfare model builds hallucination risk into the market’s ba sic structure: users differ in
how much accuracy matters to them, and agents choose how much costly fact-ch ecking to
perform. Market shares and verification effort settle where the two meet, so sectors in which
errors are costly end up with more verification (Iyidogan and Ozkes, 2025).
On coordination, reinforcement learning pricing agents in market simulation converge to
supra-competitive prices without communicating and even without observing rivals’ prices
(Schlechtinger et al., 2023), and policy-oriented analyses extend the competi tion concern to
autonomous pricing at market scale (KYDYRBAYEVA et al., 2026). Both update the  first
wave’s pricebot dynamics, where price-setting agents generated cyclic al price wars (Greenwald
and Kephart, 1999; Leloup, 2003) and analytical work showed comparison agents virtu ally co-
locating competitors (Iyer and Pazgal, 2003). Interface-control analysis com pletes the structural
picture: as answers replace result lists, control of the assistant la yer concentrates gatekeeping
power that inherited a search market already at 80 percent desktop and 90 perce nt mobile
concentration (Ortiz-Freuler and Castells, 2025). Macro syntheses of the agent economy (Tan and
Huang, 2025), Hayekian doubts about whether delegated agents can transmit dispersed
knowledge (McDavid et al., 2026), algorithmic consumer culture (Airoldi and Rokka , 2022), and
updated impact assessments from both waves (Redmond, 2002; Ma et al., 2010) round out the
direction.
8.3 The continuity thesis
Across RQ4 the two waves keep producing the same shapes: gatekeeper concentr ation,
gaming of the gatekeeper’s inputs, persistent dispersion despite comparison, br and value
surviving machine mediation, and algorithmic pricing dynamics that surprise t heir designers. The
second wave adds three genuinely new elements: linguistic manipulability of t he chooser,
vendor-controlled and version-unstable choice weights, and a payment layer that make s full
delegation transactable. The continuity is the review’s license to use first-w ave field evidence as

27
baseline; the three new elements are its research frontier, and t he framework that follows assigns
each of them a place.
9 The Agentic Commerce Reference Framework
9.1 Construction and architecture
The syntheses of Sections 5 to 8 were built construct by construct; the field a lso needs to see
them together, because findings in each layer condition what is possible in the ot hers. The
Agentic Commerce Reference Framework (ACRF), Figure 6, consolidates the coded corpus into
four layers crossed by the customer journey. It was constructed bottom-up: the coding scheme’s
directions group into layers by the question each answers. What must hold for de legation to be
possible is L1, the 17 governance and infrastructure studies. Who delegates, and  how deeply, is
L2, the 42 delegation studies and the ladder. How influence operates is L3, the 56 studies of the
influence triad, and what markets do as a result is L4, the 25 market st udies. Every block in the
figure is populated by identifiable primary studies, which distinguishes the AC RF from
stakeholder frameworks assembled by intuition: it is an evidence map first and an architecture
second. It can also be tested block by block. If new studies in a block contradict the block’s stated
pattern, or if a proposed cross-layer dynamic fails to appear where the  framework predicts it, the
framework is revised or rejected at that point rather than defended as a whole.

Figure 6: The Agentic Commerce Reference Framework. Four layers organize the  coded corpus
by the question each answers; the horizontal axis is the customer journey; t he side arrows denote
enablement running upward and regulatory and design pressure running downward. Study
counts per layer sum to the corpus (N=140).

28
9.2 Cross-layer dynamics
By a dynamic we mean a recurring cause-and-effect pattern that c rosses layer boundaries. The
four below were derived by reading the coded corpus layer by layer and asking which findings in
one layer presuppose or produce findings in another. Each is an analytic gene ralization over a
named cluster of studies, cited with it, not an empirical estimat e. They are summarized in
Figure 7. D1, enablement, runs upward: infrastructure determines reachable delegation depth
(Chua et al., 2026; South et al., 2025), depth determines which influence sur faces exist, and only
executed delegation aggregates into machine demand. The first wave ill ustrates the dependence
by what it lacked. Its designs had full-autonomy ambitions, but the mandate, payme nt, and
identity infrastructure they would have needed did not exist, and the systems stalled (He et al.,
2003; Wang et al., 1999). D2, pressure, runs downward: market findings such as lea kage (Alavi
and Nozari, 2026) and audit instability (Allouah et al., 2026) generate the  regulatory and design
agendas of L1 (Bostoen and Krämer, 2026; Busch, 2025), and consumer findings such as the
autonomy paradox (Choubey and Chakraborty, 2026) constrain acceptable influence design. D3,
the adversarial diagonal, is the framework’s warning light. An attack ex ecuted in L3, a strategic
text sequence or an injected instruction (Kumar and Lakkaraju, 2024; Johnson et al., 2025) ,
defeats a trust assumption located in L1 and distorts demand measured in L4, whil e remaining
invisible in L2 because the consumer sees only a confident recommendation. No singl e-layer
research design can even observe this path, which is why the corpus’s attac k studies and its
consumer studies currently pass each other without contact. D4, the legibilit y loop, couples L3’s
production and selection stages: agents generate marketing content (Aslam et al., 2026; Wang et
al., 2025), agentic testing selects what performs (Lu et al., 2026), agent choos ers reward
machine-readable content (Aggarwal et al., 2024; Allouah et al., 2026), and rising agent-mediated
share feeds the loop. Its end point, marketing optimized for machine reade rs with humans as
bystanders, is exactly the machine-marketing scenario the discipline is being asked to theorize
(Sarstedt et al., 2026). Each dynamic is stated so that evidence could contra dict it: D1 fails if
delegation depth rises in a market whose mandate infrastructure has not  changed, D2 fails if
documented harms produce no design or regulatory response, and D4 fails if age nt-mediated
demand stops responding to machine-optimized content.

29

Figure 7: Cross-layer dynamics of the ACRF, recurring patterns of influence betw een layers
stated as analytic generalizations over the coded study clusters cited in the text. D1: enablement
runs upward from infrastructure to market outcomes. D2: empirical and regulatory press ure
runs downward. D3: the adversarial diagonal, in which an influence-layer attack defeat s an
infrastructure assumption and distorts market outcomes while remaining invisible at t he
delegation layer. D4: the legibility loop, in which agent-produced content, agent- based testing,
and agent choosers select for machine-legible marketing.
9.3 The evidence map and its gaps
Crossing the journey axis with the influence directions yields the evidence m ap of Figure 8,
and its empty cells are as informative as its full ones. Evidence concentrat es in three regions:
cross-journey studies of delegation, production, and governance (67 studies, reflecti ng that
general-purpose agents resist stage assignment); evaluation-stage persuasion and de legation (29);
and transaction-stage delegation, market, and governance work (30). Three gaps stand out;
calling them consequential is our judgment as reviewers, and others may weight  them differently.
Post-purchase holds three studies, so returns, complaints, warranty claims , loyalty, and
repurchase under delegation are nearly unstudied, despite being where mandate m isuse would
surface (Andrews, 2008). Search-stage work is entirely to-direction: el even studies of visibility
and none of what consumers experience when discovery is delegated. And the to- direction has no
post-transaction presence at all: how firms remain visible to an agent that already bought from
them, the machine analogue of retention marketing, is an open field. The map converts these gaps
into the agenda’s location targets.

30

Figure 8: Evidence map: primary studies by customer journey stage and primary influenc e
direction (N=140). Darker cells hold more studies; empty cells are research gaps discuss ed in
the text.
9.4 Using the framework across research communities
The ACRF is designed as shared infrastructure for the several communities the corpus spans,
and its use differs by community in ways worth stating explicitly, summarize d in Table 5. For
marketing and analytics scholars, the framework is a variable map: L3 names the treatment space,
L2 the moderator space, L4 the outcome space, and L1 the identificati on opportunities, since
protocol rollouts and mandate designs are natural experiments in delegation de pth. For consumer
research and human-computer interaction, the ladder plus the L2 antecedent  families define the
design space of oversight. The framework’s D3 diagonal adds the safety-releva nt fact that
interface trust cues can be true while the layer beneath them i s compromised, which makes
calibrated rather than maximal trust the design goal (Balaskas et al., 2026; Wang et al., 2026a).
For information systems and software engineering, the framework assigns the  evaluation
agenda: benchmarks and audits (Ling et al., 2026; Wang et al., 2026b; Allouah et al., 2026)
instrument L3’s chooser, while L1’s designs (Chua et al., 2026; South et al., 2025) need
conformance testing, red-teaming against the documented attack classes (Kuma r and Lakkaraju,
2024; Johnson et al., 2025; Guo et al., 2025), and telemetry standards that make mandat es
observable. For economics and operations, L4’s models (Alavi and Nozari, 2026; Cao and  Hu,
2026; Duetting et al., 2024) acquire empirical counterparts as L1 telemet ry matures, and the
framework locates which parameters, leakage rates, position elasticit ies, concentration indices,
are measurable where. For law and policy, the framework separates conduct that existing doctrine
reaches from conduct that falls between layers, which is where the corpus’s legal strand
concentrates (Busch, 2025; Bostoen and Krämer, 2026; Zhang and He, 2026). The framework’ s
ambition is that a study in any of these communities can state, in one sentenc e, which blocks it
occupies and which dynamics it touches; the agenda that follows is written in exactly that
grammar.

31
Table 5: Community entry points into the ACRF. Propositions RP1 to RP10 and instruments I1 to
I5 are defined in Section 10.2.
Community Primary framework use Agenda entry
points
Marketing and analytics Variable map: L3 treatments, L2 moderators,
L4 outcomes, L1 identification
RP1, RP2, RP5,
RP6; I1, I2, I5
Consumer research and HCI Oversight design space on the ladder;
calibrated trust under the D3 diagonal
RP4, RP6, RP8; I3
Information systems and
software engineering
Evaluation and conformance: benchmarks,
audits, red-teaming, mandate telemetry
RP3, RP9; I3, I4
Economics and operations Parameter estimation for L4 models from L1
telemetry
RP7
Law and policy Locating conduct between layers; liability
and disclosure design
RP8, RP10
10 Discussion
10.1 Theoretical implications
Four implications follow from the synthesis, each anchored in the coded evidence  rather than
in speculation, and each addressed to a named home literature. First , for consumer research and
the Persuasion Knowledge Model, persuasion knowledge is displaced twice, and the
displacement is measurable. Consumers hold persuasion knowledge about machine per suaders,
with benevolence inference and identity disclosure as its levers (Farmer and H arding, 2026; Luo
et al., 2019; Kim et al., 2025), while agents themselves lack persuasion knowledge  almost
entirely, responding to strategic text, injected instructions, and framing (Kumar and Lakkaraju,
2024; Johnson et al., 2025; Allouah et al., 2026). Theory therefore needs a machine-side analogue
of Friestad and Wright (1994): a persuasion knowledge model whose target is a model , with
attack-recognition playing the role coping tactics play in the human account. The susceptibility
parameters are already being measured; what is missing is the construct that organizes them.
Second, for behavioral economics and the choice-architecture tradition, c hoice architecture
becomes two-stage, and the stages obey different laws. Designers arrange c ontext for agents,
whose sensitivities are vendor-set and version-unstable (Allouah et al., 2026;  Brucks and Toubia,
2025); agents arrange options for humans, whose responses follow the through-direction’s
psychology (Nguyen et al., 2026; Choubey and Chakraborty, 2026). Established nudge results do
not transfer across the seam: a sponsored tag that attracts a human repels a machine chooser
(Allouah et al., 2026). Choice architecture theory needs the seam as an ex plicit object, including
who controls each stage and what happens when the stages conflict.
Third, for information systems and marketing research on technology adoption and delegation,
delegation is a mandate relation, not only an attitude, and measurement should f ollow the
construct. The trust literature predicts stated willingness (Wang et al., 2026a; Zhao et al., 2025);
the governance literature defines the artifact that actually grants a uthority (Chua et al., 2026;

32
South et al., 2025); and the ladder’s inversion shows how little behavioral evidence  exists where
mandates actually bind. Treating the mandate, its scope, its verification, its revocation, as the unit
of analysis unifies the psychological and institutional strands and gives delegation a de pendent
variable that is observable in systems rather than in surveys.
Fourth, for method, the two-wave structure is an identification strategy, not background.
Where results replicate across waves, brand premia under machine media tion (Smith and
Brynjolfsson, 2001; Allouah et al., 2026), gatekeeper gaming (Hajaj et al., 2015; Aggar wal et al.,
2024), algorithmic pricing surprises (Greenwald and Kephart, 1999; Schlechtinger et  al., 2023),
the mechanism is robust to a complete change of technology, which is the strongest robustness
check available in a young field. Where results diverge, linguistic manipula bility, version
instability, transactable mandates, the divergence isolates what is genuinely ne w and therefore
where new theory is needed. We offer the two-wave design as a template:  fields experiencing
technology-driven rebirth can treat their own first wave as a control condition r ather than as
obsolete prologue.
10.2 Research agenda
The framework’s gaps convert into a ten-proposition agenda organized in thr ee streams,
measure, model, govern, summarized in Figure 9 with Table 6 stating each proposit ion and its
anchoring evidence. The propositions are anchored in evidence in the sense that ea ch generalizes
a documented mechanism; none has been tested in the stated form, and testing t hem as stated is
what the agenda proposes. The measurement stream comes first deliber ately, because the
constructs of the modeling propositions cannot be estimated without the instruments: the corpus’s
central evidential asymmetry, experimental mechanism confidence versu s absent production
evidence, cannot be closed by more experiments. RP1 calls for share of  model voice, a brand’s
presence in generated answers and agent choice sets, measured longitudinally w ith stability
diagnostics, because visibility is manufacturable (Aggarwal et al., 2024) and unst able (Allouah et
al., 2026). RP2 calls for agent-resolved attribution, separating human sessions, co- pilot sessions,
and mandate-executed transactions in analytics pipelines, because the ladder ’s levels are causally
different customers. RP3 calls for gated agent panels, standing populations of inst rumented
agents transacting on live markets under research protocols, the field’s l east glamorous and
highest-value infrastructure need, extending the audit design (Allouah et al., 2026) and t he
benchmark substrate (Ling et al., 2026; Wang et al., 2026b) into continuous measurement.
The modeling stream translates the theoretical implications into te stable form. RP4, machine
persuasion knowledge, predicts that attack susceptibility is a stable, mea surable agent trait with a
learnable defense curve (Kumar and Lakkaraju, 2024; Li et al., 2026a; Johnson et al., 2025). RP5,
two-stage choice architecture, predicts systematic divergence between huma n-optimal and agent-
optimal presentation of identical offers (Allouah et al., 2026; Nguyen et al.,  2026). RP6,
mandate-level delegation, predicts that scope, verification, and revocation de sign causally shift
delegation depth and downstream satisfaction, testable the moment L1 syste ms expose mandate
parameters (Chua et al., 2026; South et al., 2025; Choubey and Chakraborty, 2026). RP7, a gentic
market equilibrium, calls for empirical estimation of the leakage, solicitation, and concentration
parameters the formal models define (Alavi and Nozari, 2026; Cao and Hu, 2026; Iyidogan and
Ozkes, 2025). The governance stream tests designs rather than assumes them. R P8, disclosure
inside answers, asks what identity and sponsorship disclosure achieve when the pe rsuasion
happens inside a generated answer, extending the disclosure evidence (Luo et al., 2019; Peng et

33
al., 2023; Hermann et al., 2026) to the new surface. RP9, susceptibility stre ss testing, proposes
standardized adversarial audits of commercial agents before deployment, m erging the attack
literature with the evaluation frameworks (Guo et al., 2025; Rudra and  Agrawal, 2025). RP10,
liability and verifiability, asks which mandate architectures make responsibility assignable in
practice, joining the legal allocation analyses (Zhang and He, 2026; B usch, 2025) to the
verification designs (South et al., 2025; Chua et al., 2026).

Figure 9: The research agenda: three streams, ten propositions, five analytics instru ments, and
the community entry points mapped in Table 5.

Table 6: Research agenda propositions with anchoring evidence.
RP Proposition Anchoring evidence
RP1 Share of model voice is measurable, unstable
over time, and open to deliberate influence
Aggarwal et al., 2024; Allouah et al.,
2026; Uppin and Uppin, 2025
RP2 Agent-resolved attribution separates causally
distinct customer types along the ladder
Vasileva, 2025; Chua et al., 2026
RP3 Gated agent panels can generate evidence from
live deployments that experiments cannot
Allouah et al., 2026; Ling et al., 2026;
Wang et al., 2026b
RP4 Machine persuasion knowledge: susceptibility is
a stable agent trait with a defense curve
Kumar and Lakkaraju, 2024; Li et al.,
2026a; Johnson et al., 2025
RP5 Two-stage choice architecture: human-optimal
and agent-optimal presentation diverge
Allouah et al., 2026; Nguyen et al.,
2026; Dubey et al., 2024
RP6 Mandate design causally shifts delegation depth
and downstream satisfaction
South et al., 2025; Chua et al., 2026;
Choubey and Chakraborty, 2026

34
RP7 Leakage, solicitation, and concentration
parameters are empirically estimable
Alavi and Nozari, 2026; Cao and Hu,
2026; Iyidogan and Ozkes, 2025
RP8 Disclosure inside generated answers changes
trust and choice differently than interface
disclosure
Luo et al., 2019; Peng et al., 2023;
Hermann et al., 2026
RP9 Standardized susceptibility stress tests predict
field manipulation losses
Guo et al., 2025; Rudra and Agrawal,
2025; Pachaiyappan, 2026
RP10 Mandate verifiability determines practical
liability assignability
Zhang and He, 2026; Busch, 2025;
South et al., 2025
10.3 Instruments for marketing analytics
Because the community builds measurement, we state the agenda’s operat ional core as five
instruments. I1, model-voice tracking: standing queries against the major assista nt and agent
surfaces, logging brand and source presence with version metadata, the successor t o share of
search (RP1). I2, the machine-legibility audit: a firm-side diagnosti c scoring catalog and content
machine-readability, structured data coverage, and third-party verifiabili ty, the successor to
technical SEO audits (Aggarwal et al., 2024; Ceker et al., 2026) (RP1, RP5). I3, gated agent
panels: instrumented agent populations transacting under research governance, t he successor to
consumer panels (RP3). I4, susceptibility stress tests: standardized adversa rial batteries scoring
an agent’s resistance to the documented attack classes before it is allow ed to spend (Kumar and
Lakkaraju, 2024; Guo et al., 2025) (RP4, RP9). I5, mandate-based attribution: analyt ics keyed to
authenticated mandate identifiers rather than to sessions, which the pa yment protocols make
technically possible for the first time (Chua et al., 2026; Google, 2025) (R P2, RP10). Each
instrument is specified so that a methods paper could build it; we regar d the five as the concrete
deliverables the machine-marketing agenda (Sarstedt et al., 2026) requires from analytics.
10.4 Managerial implications
For managers the synthesis reduces to four decisions. First, treat machine vi sibility as a
managed asset now. The GEO evidence (Aggarwal et al., 2024) and the audit f acts (Allouah et
al., 2026) imply that a share of demand is already being allocated by choosers a  firm can measure
and influence, and the machine-legibility audit (I2) is the entry point. Se cond, decide the firm’s
disclosure policy before regulation decides it: the disclosure penalty (Luo e t al., 2019), the
design-dependence of acceptance (Peng et al., 2023), and the transparency r esults (Wang et al.,
2026a; Balaskas et al., 2026) say that identity and explanation design are effec tiveness variables,
not compliance details. Third, segment customers by delegation depth: the ladder’ s levels differ
in what reaches them, what persuades them, and what retains them, so a D1 advisor user and a D3
mandate holder should not sit in one funnel (RP2). Fourth, price model-version ri sk: demand
allocated by agents can reshuffle on a provider’s update cycle (Allouah et a l., 2026), a volatility
channel outside any existing brand-tracking regime, and I1’s version metadata is the safeguard.
10.5 Policy implications
Three implications address regulators and standard-setters. First, the mand ate is the regulatory
object: verification of authority, scope, and revocation (Chua et al., 2026; South et al., 2025) is
where consumer protection, payments regulation (Amariles et al., 2026), and lia bility (Zhang and

35
He, 2026) technically converge, and mandating verifiable delegation would serve all  three at
once. Second, disclosure rules must follow the persuasion into the answer. I dentity disclosure at
the interface is well studied (Luo et al., 2019), but sponsorship inside generated recommendations
(Dubey et al., 2024; Hermann et al., 2026) is a surface that current advertising di sclosure regimes
do not reach, and RP8 defines the evidence needed. Third, susceptibility auditing bel ongs in
conformity assessment: the attack literature (Kumar and Lakkaraju, 20 24; Guo et al., 2025;
Johnson et al., 2025) demonstrates exploitable channels in exactly the systems be ing wired to
payments, and standardized stress testing (I4, RP9) is implementable wi th existing audit
institutions.
11 Limitations
Four limitations bound the claims. First, construct drift: the field’s vocabulary moved during
the very window searched, and although snowballing in both directions repairs much of the drift,
retrieval anchored partly in current terminology can underrepresent adja cent phrasings; the
released search trail lets successors test sensitivity. Second, screenin g and coding after the three-
author calibration: the paired criteria, the measured calibration agreem ent, the coded decision
trail, and recomputable matrix mitigate but do not eliminate individual judgm ent risk, and an
independent recoding of the register is an invited replication. Third, evidence ma turity: 96 of the
105 second-wave studies appeared in 2024 or later, a meaningful share as working pape rs, all
labeled in the register. Conclusions there carry the uncertainty of unreviewed work. The peer-
reviewed subset supports every headline claim, but effect sizes may sett le. Fourth, the corpus’s
own evidential asymmetry limits the synthesis symmetrically. With fi ve field studies and no
production transaction data, market-level statements rest on models, audits, and dated field
anchors. That is why the agenda leads with measurement rather than with more theory. The
corpus is also consumer-centric by design. Whether the influence triad, the delegation ladder, and
the trust families transfer to business-to-business buying centers, with thei r formal roles and
multi-person decision units, is untested; the two included B2B studies (Adam et al., 2025; Xiao et
al., 2025) are too few to say.
12 Conclusion
This review assembled and coded 140 primary studies across two researc h waves to answer
four questions about commerce when the customer can be a machine. The ac tors form four
institutional families whose authority we measure on a five-level del egation ladder. Along that
ladder the evidence runs opposite to deployment: behavioral studies are rich wher e agents merely
advise, while only six empirical studies observe agents that act. Marketing infl uence runs to,
through, and by agents, three directions with different mechanics, different mat urities, and
compositions, the legibility funnel, the synthetic optimization loop, proxy manipulat ion, that
define the new strategic terrain. Consumer delegation is governed by six antecedent families, but
its binding constraint is institutional: the verifiable mandate is where psy chology, payments, and
liability now converge. And machine demand already shows recurring empiri cal regularities,
concentration, instability, and manipulability, that echo the first wave’s f ield evidence while
adding what is genuinely unprecedented. The Agentic Commerce Reference F ramework holds
these results in one structure in which every claim lists its supporting studies, the ten propositions

36
and five instruments convert its gaps into work, and the replication packag e makes every number
checkable. Marketing has begun to ask what it becomes when the customer is a machine (Sarstedt
et al., 2026). This review’s answer is that the question is researchable now, that  two waves of
evidence already constrain it, and that the discipline best positioned to lead is the  one that builds
the instruments first.
Data availability
A replication package accompanies the article1. It contains the corpus register with provenance
for all 141 screened identifiers and the 140 included studies, the criter ion-coded screening
decisions at every stage, and the full extraction and coding matrix with t he coding scheme and
method-family mapping. It also holds the search strings and the per-database execution records.
Declarations
Competing interests.  The author(s) declare no competing interests.
Funding. No external funding was received for this work.
Ethics. The study synthesizes published literature and involved no human participants.
Use of generative AI.  During the preparation of this work, the authors used AI-based tools
mainly for proofreading, editing, shortening, rephrasing, and refinement, in line  with ARISMA
principles (Moghaddam and Alipour, 2026). All the analytical reasoning, methodologica l
choices, and significant contributions presented in this paper are solely those of the authors.
References
Adam, M., Mishra, A. N., and Benlian, A. (2025). Agent-based data curation pr actices: customer
responses to human versus algorithmic data requesters in established business- to-business
relationships. Information Systems Research.
Aggarwal, P., Murahari, V., Rajpurohit, T., Kalyan, A., Narasimhan, K., and Deshpa nde, A.
(2024). Geo: Generative engine optimization. In Proceedings of the 30th ACM SIGKDD
conference on knowledge discovery and data mining, pages 5–16.
Aggarwal, P. and Vaidyanathan, R. (2003). The perceived effectiveness of virt ual shopping
agents for search vs. experience goods. ADVANCES IN CONSUMER RESEARCH, VOL 30 ,
30:347–348.
Ahn, J. and Kim, M. (2025). Autonomous ai agents for multi-platform social media mar keting: A
simultaneous deployment study. Electronics, 14(21):4161.
Airoldi, M. and Rokka, J. (2022). Algorithmic consumer culture. Consumption Markets &
Culture, 25(5):411–428.

1 https://figshare.com/s/af06b7238fc45bed37fb

37
Alabed, A., Javornik, A., Gregory-Smith, D., and Casey, R. (2024). More than just a cha t: A
taxonomy of consumers’ relationships with conversational ai agents and their wel l-being
implications. European Journal of Marketing, 58(2):373–409.
Alavi, S. and Nozari, S. (2026). When agents shop for you: Role coherence in ai-m ediated
markets. arXiv preprint arXiv:2604.26220.
Allouah, A., Besbes, O., Figueroa, J. D., Kanoria, Y., and Kumar, A. (2026). What is your ai
agent buying? evaluation, biases, model dependence, & emerging implications of agenti c e-
commerce. In Proceedings of the ACM Web Conference 2026, pages 8697–8700.
Amariles, D. R., Charlotin, D., and He-Guelton, L. (2026). Ai agents in payments: A pplications,
risks and regulations. European Journal of Risk Regulation, pages 1–24.
Anandan Karichalil, R. and Kaul, D. (2026). The emancipation paradox: When ai-enhanc ed
personalization undermines consumer agency and what socially responsible marketing requires.
Journal of Macromarketing, page 02761467261447188.
Anca, P. (2026). Generative engine optimization (geo): A new paradigm of digital visibility in the
age of ai-powered search. Annals of’Constantin Brancusi’University of Targu-Jiu. Economy
Series/Analele Universităţii’Constantin Brâncuşi’din Târgu-Jiu Seria Economie, 2:119.
Andrews, D. (2008). Mysimon sez: Reducing negative consequences of missed sales vi a online
shopping agents. ACR North American Advances.
Aslam, K., Nair, L. A., Sebastian, R. R., Seemon, S., and Thomas, A. R. (2026). Autonomous
content generation and management for startup social media marketing using agentic ai. In 2026
2nd International Conference on Advances in Intelligent Computing and Applications (AICAPS) ,
pages 1–5. IEEE.
Balakrishnan, J. and Dwivedi, Y. K. (2024). Conversational commerce: entering the next stage of
ai-powered digital assistants. Annals of Operations Research, 333(2):653–687.
Balaskas, S. (2026). From recommendations to delegation: A systematic  review mapping agentic
ai in e-commerce and its consumer effects. Inf., 17(3):222.
Balaskas, S., Komis, K., Yfantidou, I., and Skandali, D. (2026). When interface s “act for you”:
An eye-tracking experiment on delegation, transparency cues, and trust in age ntic shopping
assistants. Multimodal Technologies and Interaction, 10(3):22.
Bansal, P. and Bansal, R. (2026). The transparency paradox: Rebuilding trust in ai  shopping
agents through explainability. In Reshaping E-Commerce Through AI Shopping Agents , pages
375–406. IGI Global Scientific Publishing.
Bernovskis, A. and Sceulovs, D. (2026). The semantic web of retail: A tax onomic integration of
web 3.0, decentralized e-commerce, and agentic commerce. Journal of Risk and Financial
Management, 19(5):330.
Bhushan, B., Pappu, K., Jadav, V., and Jaiswal, N. (2026). Risk-adaptive authorization fo r
agentic ai systems. In SoutheastCon 2026, pages 1–6. IEEE.

38
Bilgihan, A., Lorenz, M. P., Zhang, Y., and Ostinelli, M. (2026). Persuading the proxy: a
framework for ai-mediated marketing decisions. International Journal of Contemporary
Hospitality Management, 38(6):1995–2033.
Binswanger, M. (2025). From consumer sovereignty to algorithm-dependency? the ca se of
shopping agents. In International Conference on Society 5.0, pages 38–49. Springer.
Bostoen, F. and Krämer, J. (2026). How future-proof is the dma? a case study of a i agents.
Journal of Competition Law & Economics, page nhag005.
Brand, J., Israeli, A., and Ngwe, D. (2023). Using llms for market research. Harvard business
school marketing unit working paper, 1(23-062).
Brenner, Z. (2026). The market dreams of machines: Anti-manipulation regulati on, autonomous
tactics, and the age of ai agentics. UC Davis Bus. LJ, 26:131.
Brucks, M. and Toubia, O. (2025). Prompt architecture induces methodological art ifacts in large
language models. PloS one, 20(4):e0319159.
Busch, C. (2025). Consumer law for ai agents. German Law Journal, 26(7):1367–1382.
Cao, S. and Hu, M. (2026). A solicit-then-suggest model of agentic purchasing. arXiv preprint
arXiv:2603.20972.
Castelo, N., Bos, M. W., and Lehmann, D. R. (2019). Task-dependent algorithm ave rsion.
Journal of marketing research, 56(5):809–825.
Ceker, H., Luo, G., Koo, K. K., Mathur, P., You, W., Amdekar, A., Barton, R., KL, N., Bansal,
V., and Bouyarmane, K. (2026). Using brand knowledge bases and llm agents to enhance e-
commerce retailers’ catalog quality. In Proceedings of the Nineteenth ACM International
Conference on Web Search and Data Mining, pages 1343–1344.
Chattaraman, V., Kwon, W.-S., E. Gilbert, J., and Li, Y. (2014). Virtual shopping agents: Persona
effects for older users. Journal of Research in Interactive Marketing, 8(2):144–162.
Chen, B., Wang, Z., and Takamatsu, S. (2025). Oms: On-the-fly, multi-objecti ve, self-reflective
ad keyword generation via llm agent. In Proceedings of the 2025 Conference on Empirical
Methods in Natural Language Processing, pages 18594–18612.
Choubey, V. and Chakraborty, D. (2026). How do consumers perceive digital nudging by agentic
ai in e-commerce? Journal of Retailing and Consumer Services, 93:104918.
Chu, M.-L., Terhorst, L., Reed, K., Ni, T., Chen, W., and Lin, R. (2025). Llm-based multi-agent
system for simulating and analyzing marketing and consumer behavior. In 2025 IEEE
International Conference on E-Business Engineering (ICEBE), pages 72–79. IEEE.
Chua, J. K., Tse, C. H., Huang, D., and Wang, Z. (2026). Convpaymas: Conversational payment
multi-agent system with agent-to-agent protocol and three-mandate verificati on. In Proc. of the
25th International Conference on Autonomous Agents and Multiagent Systems , pages 4071–
4073.

39
Cooke, A. D., Sujan, H., Sujan, M., and Weitz, B. A. (2002). Marketing the unfamiliar:  the role
of context and item-specific information in electronic agent recommenda tions. Journal of
marketing research, 39(4):488–497.
Dammu, P. P. S., Alonso, O., and Poblete, B. (2025). A shopping agent for addressing subje ctive
product needs. In Proceedings of the Eighteenth ACM International Conference on Web Search
and Data Mining, pages 1032–1035.
Davenport, T., Guha, A., Grewal, D., and Bressgott, T. (2020). How artificial intel ligence will
change the future of marketing. Journal of the academy of marketing science, 48(1):24–42.
de Amstalden, M. and Schafer, B. (2020). When brand distinctiveness is in the ai of the beholder:
Trademark law for autonomous intelligent shopping agents. NZYB Int’l L., 18:51.
De Bellis, E. and Johar, G. V. (2020). Autonomous shopping systems: Identifying and
overcoming barriers to consumer adoption. Journal of Retailing, 96(1):74–87.
Dey, S. and Kumar, S. (2026). Privacy calculus and disclosure in llms: The r ole of privacy
controls, nudges, and perceived anthropomorphism. International Journal of Information
Management, 89:103071.
Dietvorst, B. J., Simmons, J. P., and Massey, C. (2015). Algorithm aversion: people erroneousl y
avoid algorithms after seeing them err. Journal of experimental psychology: General, 144(1):114.
Dubey, A., Feng, Z., Kidambi, R., Mehta, A., and Wang, D. (2024). Auctions with llm
summaries. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 713–722.
Duetting, P., Mirrokni, V., Paes Leme, R., Xu, H., and Zuo, S. (2024). Mechanism design for
large language models. In Proceedings of the ACM Web Conference 2024, pages 144–155.
Ebrahimi, P., Hoffmann, S., and Schneider, J. (2026). Opening the black box: How  reasoning-
enabled ai agents influence user perceptions and behavior in sustainable  consumption.
International Journal of Information Management, 90:103075.
Elkhoudary, A. (2025). Trust in agentic ai: Transparency and autonomy. In International Multi-
Disciplinary Conference-Integrated Sciences and Technologies, pages 431–454. Springer.
Farmer, M. and Harding, R. D. (2026). Artificial persuasion: profit motives and the
persuasiveness of ai sales agents. Journal of Personal Selling & Sales Management, pages 1–21.
Flavián, C., Akdim, K., and Casaló, L. V. (2023). Effects of voice assistant recommenda tions on
consumer behavior. Psychology & Marketing, 40(2):328–346.
FOLTEAN, F. S. and HERA, O. D. (2026). Agentic ai in marketing: Opportunities, cha llenges
and impact on firm performance. Artificial Intelligence Technologies in Management and
Engineering, pages 185–204.
Frank, D.-A., Folwarczny, M., and Otterbring, T. (2026). Consumer acceptanc e of high-
autonomy ai assistants is driven by perceived benefits in online shopping settings char acterized
by scarcity. Psychology & Marketing, 43(3):538–555.

40
Friestad, M. and Wright, P. (1994). The persuasion knowledge model: How people cope wi th
persuasion attempts. Journal of consumer research, 21(1):1–31.
Gadi, K. S., Solleti, S. R. R., Guntupalli, K. M., and Raja, A. (2026). Agentic purcha se: A trust-
aware multi-agent framework for autonomous e-commerce with live marke tplace integration. In
2026 IEEE World AI IoT Congress (AIIoT), pages 0245–0251. IEEE.
Gal, M. S. and Elkin-Koren, N. (2016). Algorithmic consumers. Harv. JL & Tech., 30:309.
Gonzalez, G. R., Habel, J., and Hunter, G. K. (2026). Ai agents, agentic ai, and the  future of
sales. Journal of Business Research, 202:115799.
(2025). Announcing agent payments protocol (AP2). Google Cloud.
https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-
ap2-protocol. Accessed: 28 July 2026.
Greenwald, A. R. and Kephart, J. O. (1999). Shopbots and pricebots. In International Workshop
on Agent-Mediated Electronic Commerce, pages 1–23. Springer.
Grewal, D. and Lindsey-Mullikin, J. (2006). The moderating role of the price frame on the effects
of price range and the number of competitors on consumers’ search intentions.  Journal of the
Academy of Marketing Science, 34(1):55–62.
Guo, Q., Tang, J., and Huang, X. (2025). Attacking llms and ai agents: Advertisement embedding
attacks against large language models. In 2025 IEEE International Conference on Future
Machine Learning and Data Science (FMLDS), pages 674–679. IEEE.
Guttman, R. H., Moukas, A. G., and Maes, P. (1998). Agent-mediated electronic comme rce: A
survey. The Knowledge Engineering Review, 13(2):147–159.
Hajaj, C., Hazon, N., and Sarne, D. (2015). Improving comparison shopping agents’ compet ence
through selective price disclosure. Electronic Commerce Research and Applications , 14(6):563–
581.
Hajaj, C., Hazon, N., and Sarne, D. (2017). Enhancing comparison shopping agents through
ordering and gradual information disclosure. Autonomous Agents and Multi-Agent Systems ,
31(3):696–714.
Hajiaghayi, M., Lahaie, S., Rezaei, K., and Shin, S. (2024). Ad auctions for llms vi a retrieval
augmented generation. Advances in Neural Information Processing Systems, 37:18445–18480.
Hasselwander, M. (2026). Ai agent, take over?! task delegation to agent ic ai systems in the
philippines. AI & SOCIETY, pages 1–16.
Hasselwander, M., Sunio, V., Lah, O., and Mogaji, E. (2026). Toward agentic ai: User
acceptance of a deeply personalized ai super assistant (aisa). Journal of Retailing and Consumer
Services, 89:104620.
Häubl, G. and Trifts, V. (2000). Consumer decision making in online shopping envir onments:
The effects of interactive decision aids. Marketing science, 19(1):4–21.

41
He, M., Jennings, N. R., and Leung, H.-F. (2003). On agent-mediated electronic commerce. IEEE
Transactions on knowledge and data engineering, 15(4):985–1003.
Hermann, E., Puntoni, S., and Schweidel, D. (2026). From advice to advertising: Conver sational
ai advertising, platform monetization, and consumer welfare. The Wharton S chool Research
Paper, Available at SSRN: https://ssrn.com/abstract=5634270.
Hoffman, D. L. and Novak, T. P. (2018). Consumer and object experience in the inter net of
things: An assemblage theory approach. Journal of Consumer Research, 44(6):1178–1204.
Huang, M.-H. and Rust, R. T. (2021). A strategic framework for artificial i ntelligence in
marketing. Journal of the academy of marketing science, 49(1):30–50.
Ishida, T., Murakami, Y., Lin, D., and Lhaksmana, K. M. (2025). Ai agents: From concept to
code to commerce. In 2025 International Conference on Information and Communication
Technology (ICoICT), pages 1–7. IEEE.
Iyer, G. and Pazgal, A. (2003). Internet shopping agents: Virtual co-locati on and competition.
Marketing Science, 22(1):85–106.
Iyidogan, E. and Ozkes, A. I. (2025). Agentic ai and hallucinations. Economics Letters , page
112520.
Johnson, S., Pham, V., and Le, T. (2025). The dangers of indirect prompt injection at tacks on
llm-based autonomous web navigation agents: A demonstration. In Proceedings of the 2025
Conference on Empirical Methods in Natural Language Processing: System Demonstrations ,
pages 729–738.
Karacapilidis, N. and Moraıtis, P. (2001). Building an agent-mediated elec tronic commerce
system with decision analysis features. Decision Support Systems, 32(1):53–69.
Kehagias, D. D., Symeonidis, A. L., and Mitkas, P. A. (2005). Designing pricing mechanisms f or
autonomous agents based on bid-forecasting. Electronic Markets, 15(1):53–62.
Kim, W., Ryoo, Y., and Choi, Y. K. (2025). That uncanny valley of mind: when
anthropomorphic ai agents disrupt personalized advertising. International Journal of Advertising,
44(8):1684–1713.
Kumar, A. and Lakkaraju, H. (2024). Manipulating large language models to increase  product
visibility. arXiv preprint arXiv:2404.07981.
KYDYRBAYEVA, E., SHOMSHEKOVA, B., ABZHAKOV, A., ASHIMOVA, A., and
NURTAYEVA, A. (2026). Autonomous ai agents in digital markets: Economic implic ations for
competition, pricing, and regulation. Applied Computer Science, 22(2):126–137.
Lee, S. (2026). Meaning over quantity: An exploratory study on how relationship intimac y
shapes giver query formulation in llm-based gift recommendation. In Proceedings of the
Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems , pages
1–6.

42
Lei, S., Xie, L., and Peng, J. (2025). Unethical consumer behavior following artificial intelligence
agent encounters: The differential effect of ai agent roles and its boundar y conditions. Journal of
Service Research, 28(4):598–613.
Leloup, B. (2003). Pricing with local interactions on agent-based electronic ma rketplaces.
Electronic Commerce Research and Applications, 2:187–198.
Lemon, K. N. and Verhoef, P. C. (2016). Understanding customer experience throughout the
customer journey. Journal of marketing, 80(6):69–96.
Li, C., Wang, Z., Ma, H., Li, W., Wu, H., Song, Y., and Gao, M. (2026a). Agentattack: Llm
agents for multi-strategy shilling attacks in recommenders. Expert Systems with Applications ,
page 131163.
Li, Y., Lin, S., Gong, H., Wang, X., and Janiszewski, C. (2026b). Time is shrinking in the eye  of
ai: Ai agents influence intertemporal choice. Journal of Consumer Psychology, 36(1):59–77.
Lim, W. M., Kumar, S., Verma, S., and Chaturvedi, R. (2022). Alexa, what do we  know about
conversational commerce? insights from a systematic literature review. Psychology & Marketing,
39(6):1129–1155.
Ling, E. C., Tussyadiah, I., Tuomi, A., Stienmetz, J., and Ioannou, A. (2021). Factors infl uencing
users’ adoption and use of conversational agents: A systematic review. Psychology & marketing,
38(7):1031–1051.
Ling, Y., Yuan, C., Dong, S., Yang, Y., Mocherla, N., and Goyal, A. (2026). Shopperbench: A
benchmark for personalized shopping with persona-guided simulation. In Proceedings of the 19th
Conference of the European Chapter of the Association for Computational Linguistics (Vo lume
5: Industry Track), pages 837–846.
Liu, G., Liu, M. W., and Zhu, Q. (2025). Hmm, the effect of ai conversational fillers on consumer
purchase intentions. Marketing Letters, 36(3):593–605.
Liu, X. and Chen, X. (2026). Governed agentic ai for retail baskets: A c onsumer world model
with inventory-aware actions. Production and Operations Management , page
10591478261458079.
Logg, J. M., Minson, J. A., and Moore, D. A. (2019). Algorithm appreciation: People prefe r
algorithmic to human judgment. Organizational behavior and human decision processes ,
151:90–103.
Longoni, C. and Cian, L. (2022). Artificial intelligence in utilitarian vs.  hedonic contexts: The
“word-of-machine” effect. Journal of Marketing, 86(1):91–108.
Lu, Y., Hsu, T.-Y., Gu, H., Cui, L., Xie, Y., Headden III, W. P., Yao, B., Veeragouni, A ., Liu, J.,
Nag, S., et al. (2026). Agent a/b: Automated and scalable a/b testing on live we bsites with
interactive llm agents. In Proceedings of the Extended Abstracts of the 2026 CHI Conference on
Human Factors in Computing Systems, pages 1–12.

43
Lu, Y. and Li, G. (2026). Ai vs. human streamers: How digital agents shape c onsumer persuasion
processing in live streaming commerce. Journal of Theoretical and Applied Electronic
Commerce Research, 21(6):195.
Luo, X., Tong, S., Fang, Z., and Qu, Z. (2019). Frontiers: Machines vs. humans: The impact of
artificial intelligence chatbot disclosure on customer purchases. Marketing science , 38(6):937–
947.
Ma, Z., Liao, K., and Lee, J. J.-Y. (2010). Examining comparative shopping agents from  two
types of search results. Information Systems Management, 27(1):3–9.
Maes, P., Guttman, R. H., and Moukas, A. G. (1999). Agents that buy and sell. Communications
of the ACM, 42(3):81–ff.
Mari, A. and Alabed, A. (2025). Ai with a conscience: Empathic voice assista nts for sustainable
shopping decisions. In International Conference on Sustainability and Innovation Processes and
Systems, pages 92–103. Springer.
Mari, A., Mandelli, A., and Algesheimer, R. (2024). Empathic voice assistants: Enhanci ng
consumer responses in voice commerce. Journal of Business Research, 175:114566.
(2025). Mastercard unveils Agent Pay, pioneering agentic payments technology to power
commerce in the age of AI. Press release. https://www.mastercard.com/global/en/news-and-
trends/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-
to-power-commerce-in-the-age-of-ai.html. Accessed: 28 July 2026.
McDavid, B., Kiesling, L., and Chassin, D. (2026). Markets, agency, and trust: Ai agent s and the
knowledge problem. The Review of Austrian Economics, pages 1–26.
Mirzayi, S. and Talajouran, E. (2025). From decision support to decision making: autonomous ai
agents shaping the marketing. In 2025 11th International Conference on Web Research (ICWR) ,
pages 194–199. IEEE.
Mishra, M. K., Vyas, C., Mazumdar, B., and Mishra, V. (2025). Harnessing the power of
machine learning in multi-agent systems for b2c e-commerce optimizati on. In 2025 3rd
International Conference on Communication, Security, and Artificial Intelligence (I CCSAI),
volume 3, pages 2157–2161. IEEE.
Moghaddam, M. T. and Alipour, M. (2026). Arisma: Guidelines for ai-and llm-assiste d
systematic reviews, scoping reviews, and mapping studies. Agentics 2026, arXiv preprint
arXiv:2608.25050.
Nguyen, M., Barari, M., and Zhang, Y. (2026). The voice or the script? unlocking a i agent
persuasion through modality and mental imagery. Journal of Retailing and Consumer Services ,
92:104775.
and Stripe (2025). Agentic Commerce Protocol. Technical specification.
https://github.com/agentic-commerce-protocol/agentic-commerce-protocol. Accessed: 28 July
2026.

44
Ortiz-Freuler, J. and Castells, M. (2025). From search engines to ai agents:  Interface control and
the restructuring of communication power. New Media & Society, page 14614448261437812.
Pachaiyappan, N. (2026). Agentic commerce: A comprehensive analysis of cybersec urity risks,
privacy challenges, and trust mechanisms in autonomous ai-driven marketplaces. I n 2026 IEEE
5th International Conference on AI in Cybersecurity (ICAIC), pages 1–6. IEEE.
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D.,
Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., et al. (2021). The pri sma 2020
statement: an updated guideline for reporting systematic reviews. bmj, 372.
Park, S., Chu, Y., and Chung, J.-H. (2025). Designing ai agents for new product endorsement:  do
human-like or cartoon-like ai-generated endorsers evoke more positive ad engageme nt from
consumers? Journal of Advertising Research, 65(2):259–277.
Pathak, B. (2010). A survey of the comparison shopping agent-based decision support systems .
Journal of Electronic Commerce Research, 11(3):178.
Pathak, B. K. (2012). Comparison shopping agents and online price dispersion: A search  cost
based explanation. Journal of theoretical and applied electronic commerce research, 7(1):64–76.
Patil, R. K., Rice, D. H., and Janiszewski, C. (2026). Human–ai partnerships: Living and working
with ai assistants, ai agents, and ai companions. Journal of Consumer Psychology.
Paul, J., Lim, W. M., O’Cass, A., Hao, A. W., and Bresciani, S. (2021). Scientific  procedures and
rationales for systematic literature reviews (spar-4-slr). International journal of consumer studies,
45(4):O1–O16.
Peng, X., Peng, X., and Xu, D. (2023). Why users accept discriminatory pricing: The r oles of AI
agent’s presence and explanation. In ICIS 2023. Association for Information Systems.
Pilı́k, M., Klimek, P., Jurickova, E., and Pálka, P. (2016). Comparison shopping agents and czech
online customers’ shopping behaviour. International Journal of Entrepreneurial Knowledge ,
4(2).
Potluri, L. K. M. and Chittimalla, S. K. (2026). Multi-agent retrieval-augment ed conversational
systems for end-to-end autonomous shopping assistants. In 2026 International Conference on
Machine Learning and Autonomous Systems (ICMLAS), pages 937–944. IEEE.
Puntoni, S., Reczek, R. W., Giesler, M., and Botti, S. (2021). Consumers and arti ficial
intelligence: An experiential perspective. Journal of marketing, 85(1):131–151.
Puri, S., Pradhan, J. A., Bernabe, B. G., and Ray, A. K. (2026). Agentic ai in branding: D riving
hyper-personalization and real-time adaptation. Global Business Review , page
09721509251414773.
Puvvadi, M., Arava, S. K., Santoria, A., Chennupati, S. S. P., and Puvvadi, H. V. (2025). S urvey
of marketing agents, agent-based models, and generative ai in marketing. In 2025 Global
Conference in Emerging Technology (GINOTECH), pages 1–7. IEEE.

45
Rabassa, V., Sabri, O., and Spaletta, C. (2022). Conversational commerce: do bi ased choices
offered by voice assistants’ technology constrain its appropriation? Technological Forecasting
and Social Change, 174:121292.
Raja, S. V. S., Orazi, D. C., Cheng, Y., and Belli, A. (2026). A meta-analysis of the effects of ai
agent implementation on customer-level outcomes. Journal of Business Research, 210:116172.
Redmond, W. H. (2002). The potential impact of artificial shopping agents in e-comm erce
markets. Journal of Interactive Marketing, 16(1):56–66.
Rohden, S. F., Espartel, L. B., and Lopes, J. C. (2025). From voice to choice: Understanding the
consumer response to voice assistant and human recommendations. International Journal of
Consumer Studies, 49(6):e70128.
Rudra, A. and Agrawal, M. (2025). A heuristic-first evaluation framework for m arketing ai
agents: Judging quality, actionability, and trust. In 2025 IEEE International Conference on
Advances in Data-Driven Analytics And Intelligent Systems (ADACIS), pages 1–5. IEEE.
Rudra, A., Karumuri, M. S., and Agrawal, M. (2026). Explainable ai for marketing intelligence:
Interpretable multi-agent systems for data-driven decision support. In SoutheastCon 2026, pages
1–5. IEEE.
Sarstedt, M., Adler, S. J., and Imschloss, M. (2026). Machine marketing: rethinking t he customer
in the age of generative ai. Journal of Marketing Analytics, pages 1–11.
Sarstedt, M., Adler, S. J., Rau, L., and Schmitt, B. (2024). Using large language  models to
generate silicon samples in consumer and marketing research: Challenges, oppor tunities, and
guidelines. Psychology & Marketing, 41(6):1254–1270.
Schlechtinger, M., Kosack, D., Paulheim, H., Fetzer, T., and Krause, F. (2023). The  price of
algorithmic pricing: Investigating collusion in a market simulation with a i agents. In AAMAS,
pages 2748–2750.
Schultz, C. D. and Kaiser, S. (2025). Consumer value dimensions in conversational and  mobile
commerce: Cd schultz and s. kaiser. Journal of Marketing Analytics, 13(3):587–605.
Schumacher, K., Roberts, R., and Giebel, K. (2025). The agentic commerce opportunity: How ai
agents are ushering in a new era for consumers and merchants. McKinsey & Company.
Schwede, M., Hammerschmidt, M., and Morana, S. (2026). Fluent voice, credible choic e–how
language embodiment and consumption goals shape voice commerce success. Journal of Service
Management, 37(1):33–54.
Sen, R., King, R. C., and Shaw, M. J. (2006). Buyers’ choice of online search strate gy and its
managerial implications. Journal of Management Information Systems, 23(1):211–238.
Shamim, I., Ghosh, T., and Sreejesh, S. (2026). Human versus ai in checkout charity:  How time
pressure, persuasion knowledge, and ulterior motive shape donation and store pat ronage
intentions. Journal of Consumer Behaviour, 25(2):517–533.

46
Sharma, M., Joshi, S., Luthra, S., and Kumar, A. (2024). Impact of digital assi stant attributes on
millennials’ purchasing intentions: A multi-group analysis using pls-sem, arti ficial neural
network and fsqca. Information Systems Frontiers, 26(3):943–966.
Sidlauskiene, J., Joye, Y., and Auruskeviciene, V. (2023). Ai-based chatbots in c onversational
commerce and their effects on product and price perceptions: J. sidlausk iene et al. Electronic
Markets, 33(1):24.
Smith, M. D. and Brynjolfsson, E. (2001). Consumer decision-making at an internet shopbo t:
Brand still matters. The Journal of Industrial Economics, 49(4):541–558.
Snaith, S. M. (2003). Can a shopping agent enforce the law of one price?(ant hology). Atlantic
Economic Journal, 31(1):117–118.
Snyder, H. (2019). Literature review as a research methodology: An overview a nd guidelines.
Journal of business research, 104:333–339.
Solanki, S. (2026). Algorithms against manipulation: Safeguarding consumer rights i n ai
shopping. In Reshaping E-Commerce Through AI Shopping Agents , pages 127–160. IGI Global
Scientific Publishing.
South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., and
Pentland, A. (2025). Authenticated delegation and authorized ai agents. arXiv preprint
arXiv:2501.09674.
Stöckl, A. and Nitu, J. (2025). Are ai agents interacting with online ads? In 2025 5th
International Conference on Electrical, Computer and Energy Technologies (ICECET) , pages 1–
8. IEEE.
Sümer, M. Ş., Özsoy, T., Okay, F. Y., and Kök, İ. (2025). Smart agents as cust omers: A semi-
autonomous digital commerce model for industry 5.0. In 2025 7th International Congress on
Human-Computer Interaction, Optimization and Robotic Applications (ICHORA) , pages 1–7.
IEEE.
Tan, L. J. and Huang, K. (2025). The ai agent economy. In Agentic AI: Theories and Practices ,
pages 99–134. Springer.
Thaler, R. H., Sunstein, C. R., and Milligan, S. (2009). Nudge: Improving decisions about health,
wealth, and happiness, volume 47. HeinOnline.
Uppin, U. and Uppin, V. (2025). Boosting brand recognition within large language models a nd
ai-driven search systems. In 2025 Artificial Intelligence for Business (AIxB) , pages 119–121.
IEEE.
Vasileva, S. (2025). The impact of ai along the customer journey mapping: How a i agents are
changing customer journey. In Proceedings of the International Conference on Business
Excellence, volume 19, pages 1088–1102. Bucharest University of Economic Studies.
Vaziry, A., Garzon, S. R., and Küpper, A. (2025). Enhancing the a2a protocol with blockc hain-
based identities and x402 micropayments for agentic ai. In International Joint Conference on
Computational Intelligence, pages 454–472. Springer.

47
Ventirozos, F. and Shardlow, M. (2026). Paying to know: Micro-transaction markets f or verified
product information in agentic e-commerce. arXiv preprint arXiv:2606.24783.
(2025). Visa introduces Trusted Agent Protocol: An ecosystem-led framework for AI commerce.
Press release. https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-unveils-
trusted-agent-protocol-for-ai-commerce.html. Accessed: 28 July 2026.
Wan, Y., Menon, S., and Ramaprasad, A. (2009). The paradoxical nature of elec tronic decision
aids on comparison-shopping: The experiments and analysis. Journal of theoretical and applied
electronic commerce research, 4(3):80–96.
Wang, H., Shimose, Y., and Takamatsu, S. (2025). Banneragency: Advertising banner de sign
with multimodal llm agents. In Proceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing, pages 4304–4329.
Wang, J. et al. (2026a). Letting the bot decide: Trust and risk perceptions in aut onomous retail
purchase decisions. Journal of Retailing and Consumer Services, 93:104867.
Wang, J., Xiao, K., Sun, Q., Zhao, H., Luo, T., Zhang, J. D., and Zeng, X. (2026b).
Shoppingbench: A real-world intent-grounded shopping benchmark for llm-based agents. I n
Proceedings of the AAAI Conference on Artificial Intelligence, volume 40, pages 33521–33529.
Wang, X. F., Yi, X., Lam, K., Zhang, C., and Okamoto, E. (1999). Secure agent-mediated
auctionlike negotiation protocol for internet retail commerce. In International Workshop on
Cooperative Information Agents, pages 291–302. Springer.
Webster, J. and Watson, R. T. (2002). Analyzing the past to prepare for the  future: Writing a
literature review. MIS quarterly, 26(2):xiii–xxiii.
Xiao, G., You, W., Fan, C., Hu, Y., and Tseng, S.-P. (2025). Design and implementation of a n ai
agent for product selection and intelligent marketing in cross-border e -commerce. In 2025 13th
International Conference on Orange Technology (ICOT), pages 1–4. IEEE.
Yuan, S.-T. (2003). A personalized and integrative comparison-shopping engine and it s
applications. Decision Support Systems, 34(2):139–156.
Zhang, M. M., Gao, Y., Li, J., and Johnson, S. L. (2026). When influencers delegate replies: How
social ai agents shape user engagement. Information Systems Research.
Zhang, W. (2025). Ai-driven e-commerce traffic engine: A multi-age nt system for optimizing
amazon sales. In International Conference on Cognitive Computing, pages 65–73. Springer.
Zhang, Z. and He, J. (2026). Who bears the responsibility? legal liability alloc ation for ai agent
conduct in platform ecosystem. Cogent Social Sciences, 12(1):2691325.
Zhao, X., You, W., Zheng, Z., Shi, S., Lu, Y., and Sun, L. (2025). How do consumers trust and
accept ai agents? an extended theoretical framework and empirical e vidence. Behavioral
Sciences, 15(3):337.

48
A The corpus
Table 7 lists the 140 primary studies with their register identifiers and c odes. Track: DB
database, BS backward snowballing, FS forward snowballing. Direction, journey stage,
delegation depth, and method family are defined in Section 3; identifier  P75 was excluded at full
text (EC5) and is retained in the register’s exclusion log.
Table 7: The 140 primary studies with register identifiers and codes.
ID Study Wave Track Direction Stage Depth Method
ID Study Wave Track Direction Stage Depth Method
P1 Puvvadi et al., 2025 W2 DB By agents Cross-
journey
D1 Design
P2 Cooke et al., 2002 W1 DB Delegation Evaluation D1 Experiment
P3 Adam et al., 2025 W2 DB By agents Post-
purchase
D1 Field
P4 Patil et al., 2026 W2 DB Delegation Cross-
journey
D2 Experiment
P5 Mari et al., 2024 W2 DB Through
agents
Evaluation D1 Experiment
P6 Alabed et al., 2024 W2 DB Delegation Cross-
journey
D2 Experiment
P7 Airoldi and Rokka,
2022
W2 DB Market Cross-
journey
D4 Formal
P8 Yuan, 2003 W1 DB Delegation Cross-
journey
D2 Experiment
P9 Karacapilidis and
Moraıtis, 2001
W1 DB Delegation Cross-
journey
D2 Experiment
P10 Gonzalez et al., 2026 W2 DB Delegation Cross-
journey
D4 Experiment
P11 Li et al., 2026b W2 DB Delegation Evaluation D1 Experiment
P12 Ortiz-Freuler and
Castells, 2025
W2 DB Market Cross-
journey
D4 Conceptual
P13 Wan et al., 2009 W1 DB Delegation Cross-
journey
D1 Experiment
P14 Andrews, 2008 W1 DB Delegation Cross-
journey
D1 Experiment
P15 Grewal and Lindsey-
Mullikin, 2006
W1 DB Delegation Cross-
journey
D2 Experiment
P16 Aggarwal and
Vaidyanathan, 2003
W1 DB Delegation Cross-
journey
D2 Experiment
P17 Iyidogan and Ozkes,
2025
W2 DB Market Cross-
journey
D4 Formal

49
ID Study Wave Track Direction Stage Depth Method
P18 Pathak, 2012 W1 DB Market Cross-
journey
D4 Conceptual
P19 Iyer and Pazgal, 2003 W1 DB Market Cross-
journey
D4 Experiment
P20 Redmond, 2002 W1 DB Market Cross-
journey
D4 Conceptual
P21 Kim et al., 2025 W2 DB Through
agents
Evaluation D1 Experiment
P22 Wang et al., 2026a W2 DB Delegation Transaction D3 Survey
P23 Nguyen et al., 2026 W2 DB Through
agents
Evaluation D1 Experiment
P24 Park et al., 2025 W2 DB Through
agents
Evaluation D1 Experiment
P25 Choubey and
Chakraborty, 2026
W2 DB Through
agents
Transaction D3 Survey
P26 Farmer and Harding,
2026
W2 DB Through
agents
Evaluation D1 Experiment
P27 Zhang et al., 2026 W2 DB Through
agents
Post-
purchase
D1 Field
P28 Liu et al., 2025 W2 DB Through
agents
Evaluation D1 Experiment
P29 Chattaraman et al.,
2014
W1 DB Through
agents
Cross-
journey
D1 Experiment
P30 Shamim et al., 2026 W2 DB Through
agents
Transaction D1 Experiment
P31 Anandan Karichalil
and Kaul, 2026
W2 DB Through
agents
Cross-
journey
D1 Conceptual
P32 Sen et al., 2006 W1 DB Delegation Transaction D3 Experiment
P33 Lei et al., 2025 W2 DB Delegation Transaction D3 Experiment
P34 Kehagias et al., 2005 W1 DB Market Cross-
journey
D4 Design
P35 KYDYRBAYEVA et
al., 2026
W2 DB Market Cross-
journey
D4 Conceptual
P36 Schlechtinger et al.,
2023
W2 DB Market Cross-
journey
D4 Sim./audit
P37 Aslam et al., 2026 W2 DB By agents Cross-
journey
D1 Design
P38 Frank et al., 2026 W2 DB Delegation Transaction D3 Experiment
P39 Rohden et al., 2025 W2 DB Delegation Evaluation D1 Experiment

50
ID Study Wave Track Direction Stage Depth Method
P40 Sidlauskiene et al.,
2023
W2 DB Delegation Evaluation D1 Experiment
P41 Flavián et al., 2023 W2 DB Delegation Evaluation D1 Experiment
P42 Chua et al., 2026 W2 DB Governance Transaction D4 Conceptual
P43 Balaskas et al., 2026 W2 DB Delegation Post-
purchase
D2 Experiment
P44 Elkhoudary, 2025 W2 DB Delegation Transaction D4 Conceptual
P45 Vaziry et al., 2025 W2 DB Governance Transaction D4 Design
P46 Bhushan et al., 2026 W2 DB Governance Transaction D4 Design
P47 Ebrahimi et al., 2026 W2 DB Delegation Transaction D2 Experiment
P48 Rudra and Agrawal,
2025
W2 DB By agents Cross-
journey
D1 Design
P49 Amariles et al., 2026 W2 DB Governance Transaction D4 Legal
P50 Bostoen and Krämer,
2026
W2 DB Governance Cross-
journey
D4 Legal
P51 Busch, 2025 W2 DB Governance Cross-
journey
D4 Legal
P52 Rabassa et al., 2022 W2 DB Through
agents
Evaluation D1 Survey
P53 Sümer et al., 2025 W2 DB Governance Transaction D4 Conceptual
P54 Wang et al., 1999 W1 DB Governance Transaction D4 Design
P55 Tan and Huang, 2025 W2 DB Market Cross-
journey
D4 Conceptual
P56 Ma et al., 2010 W1 DB Market Cross-
journey
D4 Experiment
P57 Snaith, 2003 W1 DB Market Evaluation D1 Field
P58 Solanki, 2026 W2 DB Governance Cross-
journey
D4 Legal
P59 Xiao et al., 2025 W2 DB By agents Cross-
journey
D4 Design
P60 Hajaj et al., 2017 W1 DB To agents Search D2 Design
P61 Chen et al., 2025 W2 DB By agents Cross-
journey
D1 Design
P62 Dey and Kumar, 2026 W2 DB Through
agents
Cross-
journey
D2 Conceptual
P63 Liu and Chen, 2026 W2 DB Delegation Transaction D3 Experiment
P64 Lu and Li, 2026 W2 DB Through
agents
Evaluation D1 Experiment
P65 Bansal and Bansal, W2 DB Delegation Cross- D1 Experiment

51
ID Study Wave Track Direction Stage Depth Method
2026 journey
P66 de Amstalden and
Schafer, 2020
W2 DB Governance Cross-
journey
D4 Legal
P67 Lee, 2026 W2 DB Delegation Cross-
journey
D2 Experiment
P68 Wang et al., 2025 W2 DB By agents Cross-
journey
D1 Design
P69 Allouah et al., 2026 W2 DB Market Transaction D4 Sim./audit
P70 Brenner, 2026 W2 DB Governance Cross-
journey
D4 Legal
P71 Hajaj et al., 2015 W1 DB To agents Search D1 Design
P72 Ceker et al., 2026 W2 DB To agents Search D1 Design
P73 Potluri and
Chittimalla, 2026
W2 DB By agents Cross-
journey
D2 Design
P74 Li et al., 2026a W2 DB To agents Search D1 Design
P76 Uppin and Uppin,
2025
W2 DB To agents Search D1 Design
P77 Rudra et al., 2026 W2 DB By agents Cross-
journey
D1 Design
P78 Lu et al., 2026 W2 DB By agents Cross-
journey
D1 Design
P79 Bernovskis and
Sceulovs, 2026
W2 DB Governance Cross-
journey
D4 Conceptual
P80 Pachaiyappan, 2026 W2 DB Governance Cross-
journey
D4 Conceptual
P81 Puri et al., 2026 W2 DB By agents Cross-
journey
D1 Design
P82 Anca, 2026 W2 DB To agents Search D1 Design
P83 Stöckl and Nitu, 2025 W2 DB To agents Search D1 Sim./audit
P84 Guo et al., 2025 W2 DB To agents Search D1 Sim./audit
P85 Bilgihan et al., 2026 W2 DB Through
agents
Evaluation D1 Conceptual
P86 Johnson et al., 2025 W2 DB To agents Search D3 Sim./audit
P87 Luo et al., 2019 W1 DB Through
agents
Evaluation D1 Field
P88 Ling et al., 2026 W2 DB By agents Cross-
journey
D1 Design
P89 Wang et al., 2026b W2 DB By agents Cross-
journey
D1 Design

52
ID Study Wave Track Direction Stage Depth Method
P90 Leloup, 2003 W1 DB Market Transaction D4 Conceptual
P91 Greenwald and
Kephart, 1999
W1 DB Market Transaction D4 Conceptual
P92 Hasselwander et al.,
2026
W2 DB Delegation Transaction D3 Experiment
P93 Hasselwander, 2026 W2 DB Delegation Cross-
journey
D4 Survey
P94 Chu et al., 2025 W2 DB By agents Cross-
journey
D1 Design
P95 Ahn and Kim, 2025 W2 DB By agents Cross-
journey
D1 Design
P96 Ishida et al., 2025 W2 DB Market Cross-
journey
D4 Conceptual
P97 Binswanger, 2025 W2 DB Delegation Cross-
journey
D4 Experiment
P98 FOLTEAN and
HERA, 2026
W2 DB By agents Cross-
journey
D1 Design
P99 Schwede et al., 2026 W2 DB Delegation Evaluation D1 Experiment
P100 McDavid et al., 2026 W2 DB Market Cross-
journey
D4 Conceptual
P101 Schultz and Kaiser,
2025
W2 DB Delegation Cross-
journey
D2 Survey
P102 Mirzayi and
Talajouran, 2025
W2 DB By agents Cross-
journey
D4 Design
P103 Vasileva, 2025 W2 DB Delegation Cross-
journey
D2 Experiment
P104 Zhao et al., 2025 W2 DB Delegation Transaction D3 Survey
P105 Balakrishnan and
Dwivedi, 2024
W2 DB Delegation Cross-
journey
D1 Experiment
P106 Peng et al., 2023 W2 DB Through
agents
Evaluation D3 Experiment
P107 Gadi et al., 2026 W2 DB Governance Transaction D3 Conceptual
P108 Sharma et al., 2024 W2 DB Delegation Cross-
journey
D3 Survey
P109 Zhang, 2025 W2 DB By agents Cross-
journey
D1 Design
P110 Mari and Alabed,
2025
W2 DB Through
agents
Evaluation D1 Design
P111 Mishra et al., 2025 W2 DB Market Cross-
journey
D4 Conceptual

53
ID Study Wave Track Direction Stage Depth Method
P112 Dammu et al., 2025 W2 DB By agents Cross-
journey
D1 Design
P113 Pilı́k et al., 2016 W1 DB Delegation Transaction D3 Survey
P114 Guttman et al., 1998 W1 BS Market Transaction D4 Conceptual
P115 Maes et al., 1999 W1 BS Market Transaction D4 Conceptual
P116 He et al., 2003 W1 BS Market Transaction D4 Conceptual
P117 Häubl and Trifts,
2000
W1 BS Delegation Evaluation D1 Experiment
P118 Smith and
Brynjolfsson, 2001
W1 BS Market Transaction D4 Field
P119 Gal and Elkin-Koren,
2016
W1 BS Governance Cross-
journey
D4 Legal
P120 De Bellis and Johar,
2020
W1 BS Delegation Transaction D3 Experiment
P121 Longoni and Cian,
2022
W2 BS Delegation Evaluation D1 Experiment
P122 Castelo et al., 2019 W1 BS Delegation Evaluation D1 Experiment
P123 Dietvorst et al., 2015 W1 BS Delegation Evaluation D1 Experiment
P124 Logg et al., 2019 W1 BS Delegation Evaluation D1 Experiment
P125 Puntoni et al., 2021 W1 BS Delegation Cross-
journey
D1 Conceptual
P126 Hoffman and Novak,
2018
W1 BS Delegation Cross-
journey
D2 Conceptual
P127 Friestad and Wright,
1994
W1 BS Through
agents
Evaluation D1 Conceptual
P128 Aggarwal et al., 2024 W2 BS To agents Search D1 Design
P129 Kumar and Lakkaraju,
2024
W2 BS To agents Search D1 Sim./audit
P130 Sarstedt et al., 2024 W2 BS By agents Cross-
journey
D1 Conceptual
P131 Brucks and Toubia,
2025
W2 BS By agents Cross-
journey
D1 Experiment
P132 Brand et al., 2023 W2 BS By agents Cross-
journey
D1 Experiment
P133 Duetting et al., 2024 W2 BS Through
agents
Evaluation D4 Formal
P134 Dubey et al., 2024 W2 BS Through
agents
Evaluation D4 Formal
P135 Hajiaghayi et al., W2 BS Through Evaluation D4 Formal

54
ID Study Wave Track Direction Stage Depth Method
2024 agents
P136 South et al., 2025 W2 BS Governance Cross-
journey
D4 Design
P137 Alavi and Nozari,
2026
W2 FS Market Transaction D3 Formal
P138 Cao and Hu, 2026 W2 FS Market Transaction D3 Formal
P139 Ventirozos and
Shardlow, 2026
W2 FS Market Transaction D3 Design
P140 Hermann et al., 2026 W2 FS Through
agents
Evaluation D4 Conceptual
P141 Zhang and He, 2026 W2 FS Governance Cross-
journey
D4 Legal
