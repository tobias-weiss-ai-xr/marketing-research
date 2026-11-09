---
title: 'Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce'
url: https://arxiv.org/abs/2606.24783
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Filippos Ventirozos
- Matthew Shardlow
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.24783
pages: 8
chars: 34891
fetched_at: '2026-11-08T13:36:05+00:00'
kb_version: 1
---

# Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce

/coinsPaying to Know: Micro-Transaction Markets for Verified Product
Information in Agentic E-Commerce
Filippos Ventirozos, Matthew Shardlow
Manchester Metropolitan University
Manchester, United Kingdom
f.ventirozos@mmu.ac.uk
Abstract
Commercial NLP treats the shopping chatbot
as a recommender or a conversion tool: its
job is to match a user to a catalogue entry and
close a sale. We argue that the arrival of agent-
native micro-payment rails (e.g., x402, AP2)
changes what is scarce. When the buyer is
an autonomous agent that can investigate ex-
haustively, the bottleneck is no longermatching
products butacquiring trustworthy, decision-
relevant informationabout them. We envision
agentic e-commerce as a micro-transaction mar-
ket for verified information: buyer agents spend
fractions of a cent to progressively unlock
seller- and reviewer-supplied data—service his-
tories, third-party test reports, bills of materi-
als, audited sales and support metrics—paid
for à la carte under a freemium model, with
reviewer trust scored reputationally. We sketch
the architecture of such a market and argue
that it rewards genuine product quality and
yields truer competition than ranking-based
storefronts. We then translate the vision into
concrete NLP problems—cost-optimal infor-
mation acquisition, data pricing and negoti-
ation, real-time entity resolution, grounded
value exchange, and privacy-preserving per-
sona modelling—and argue that these, not chat
fluency, deserve the field’s attention.
1 Introduction
Conversational agents are moving fromanswering
product questions toactingon them. With agent-
native payment standards such as Google’s Agent
Payments Protocol (Google, 2025) and emerging
agent-to-agent economic infrastructure utilizing
x402 micropayments (Vaziry et al., 2025), an LLM
can now hold a budget and settle a purchase on its
owner’s behalf—at sub-cent granularity, without
human intervention. The storefront is becoming an
API, and the buyer is becoming a program.
Yet applied NLP still largely studies these sys-
tems as recommenders and conversion engines—
agents that match a shopper to a catalogue entry
and persuade them to buy (Yu et al., 2026; Salvi
et al., 2026). This framing quietly assumes that
the hard part is matching. We contend that once
buyers are tireless agents that can query, compare,
and verify at scale, matching becomes cheap; what
stays scarce istrustworthy, decision-relevant infor-
mationabout a product. Today that information
is either free but unverified (SEO-optimised copy,
unaudited star ratings) or locked in silos, and dis-
covery is mediated by a marketplace whose ranking
incentives need not align with the buyer’s.
Position.We take the position thatin agentic
e-commerce, value migrates from matching prod-
ucts to pricing and trading verified information
about them. We envision amicro-transaction in-
formation marketin which a buyer’s agent spends
micro-payments to progressively unlock data that
a seller (or a third-party reviewer) has chosen to
expose, paid à la carte under a freemium model.
A product that withstands scrutiny can afford to
reveal more; an agent that prices its data well earns
proportionally more. The result, we argue, is a mar-
ket that rewards genuine quality and approximates
true competition, rather than “the first sponsored
result.”
Two running examples.The two scenarios be-
low are illustrative rather than a survey: both are
automotive, chosen to span a high- and a low-stakes
purchase, and the same mechanism carries to other
categories. Both are deliberately idealised; we
bracket the ways such a market could beskewed
and treat the most pressing in our Limitations and
Ethical Considerations.1
/car High stakes: a used car.Consider a buyer
agent instructed to find a reliable used hatchback
1Among them: collusion among sellers, reviewers, or data
vendors; reputation gaming and Sybil-staked reviews; strategic
non-disclosure of unfavourable evidence; persona-based price
discrimination; and access barriers that entrench incumbents—
each beyond the scope of this position paper.
1
arXiv:2606.24783v1  [cs.CL]  23 Jun 2026

under £9,000. The public listing exposes only
cheap-to-broadcast facts: make, model, mileage,
location, photographs, and asking price. The buyer
agent then buys evidence from distinct stakehold-
ers, in a progressively costly trail.2 From the seller
it pays £0.25 for a redacted service-history digest
(dates, mileage, garage identities) and £1.50 for a
richer pack with invoice hashes, diagnostic codes,
and tyre/brake measurements; from registry, fi-
nance, or insurer vendors, a small fee for write-off,
stolen, outstanding-finance, and mileage-anomaly
checks. Only if the car remains a candidate does
it commit a larger amount—say £20 as a deposit
toward an independent condition report.
Each payment benefits a different party. The
buyer reduces hidden risk and avoids wasted view-
ings; the seller monetises verified transparency;
data vendors are paid for facts rather than advertis-
ing; and the marketplace obtains structured, com-
parable evidence. More importantly, the sequence
of paid requests is a better serious-buyer signal
than clicks, dwell time, chatbot engagement, or
a refundable viewing reservation—happening cur-
rently in marketplaces. A seller can distinguish a
browser from an agent that has already spent £3–
£5 resolving the specific uncertainties that block
purchase, and can allocate scarce salesperson time,
document retrieval, test-drive slots, and negotiation
effort accordingly. If a hard constraint is violated—
for example an undisclosed write-off marker or
outstanding finance—the buyer agent walks away
immediately; if not, its paid information trail re-
veals both seriousness and remaining uncertainty.
🔧 Low stakes: an auxiliary belt.Now con-
sider a snapped auxiliary belt for a vehicle that
the user needs back on the road. The part may
cost only £15–£35, so the agent should not buy
expensive reports. Instead, it caps investigation at
a few pence and purchases only small, high-value
facts: fractions of a penny for an OEM part-number
cross-reference and VIN/engine-code fitment con-
firmation, £0.03 for a certified supplier-reputation
profile (verified-purchase reviews, false-fitment re-
turn and dispute rates), and £0.05 for a materials-
and-provenance certificate covering belt compound,
batch identity, and an OEM/licensed-aftermarket
authorisation claim.
Here the reputable supplier benefits most. A
seller with accurate fitment data, low return rates,
2Prices here are illustrative; what matters is the rising cost
of evidence, not the exact tariff.
genuine materials, and authorised designs can
make those facts machine-readable and priceable,
rather than competing only through SEO, spon-
sored placement, or inflated star ratings. The
buyer avoids the wrong part; the seller reduces
returns and support queries; the fitment database
earns for a small but decisive datum; and the orig-
inal manufacturer, designer, or material supplier
can be credited when their contribution genuinely
matters. This echoes the product-passport and
responsible-sourcing vision in blockchain prove-
nance projects, where claims about source, certifi-
cation, and custody travel with the physical product
rather than being rewritten as marketing copy (The
Provenance Team, 2015; European Commission
CORDIS, 2023).
Both examples are, in spirit, a commercial re-
alisation of the Semantic Web: machine-readable,
linked facts about things, but now with provenance,
prices, and negotiation (Berners-Lee et al., 2001).
The goal is fairer representation. Products should
compete on addressable evidence that agents can
verify, price, and compare, not merely on ranking
position, advertising budget, or persuasive copy.
The NLP decision is therefore not “rank the cata-
logue,” but decide which stakeholder’s evidence is
worth buying next, ground it to a shared schema,
and interpret the resulting payment trail as an eco-
nomic signal.
Frontiers for NLP.We argue these are frontier
problems the applied-NLP community must take
up to move forward: meaningfulinter-agent com-
munication—buyer and seller agents trading priced,
grounded, negotiated evidence, as described here—
will not emerge from better chat alone, but from
progress on cost-optimal acquisition, data pricing,
real-time grounding, and verifiable value exchange.
Solving them turns conversational shopping into
agentic procurement automation: agents that inves-
tigate, negotiate, and settle purchases end-to-end
on a principal’s behalf.
Roadmap.Section 2 situates the shift; Section 3
develops the vision and its architecture (Figure 1);
Section 4 translates it into open NLP problems;
Section 5 concludes.
2 The Emerging Ecosystem: Agentic
Commerce and the Information Gap
Agent-native payment rails.The enabling sub-
strate is programmable payment. The x402 pro-
2

tocol revives the dormant HTTP 402 (“Payment
Required”) status code so that a server can demand
payment for a resource and a client—human or
agent—can settle it inline, in stablecoins, at sub-
cent amounts and sub-second latency (Vaziry et al.,
2025). Google’s Agent Payments Protocol (AP2)
targets the complementary problem ofauthoriza-
tion—establishing that an agent’s purchase faith-
fully reflects its owner’s intent, and assigning ac-
countability for it (Google, 2025); in our setting,
x402-style rails price the individual data request,
while AP2-style authorization binds it to the user’s
budget and constraints. Payments at this granularity
make a previously absurd idea practical: charging
a fraction of a cent for a single datum.
A different data paradigm.This reframes the
data problem. Classical e-commerce personalisa-
tion infers intent from noisy click-stream signals;
conversational commerce promised richer, explicit
“zero-party” signals volunteered in dialogue. In
both cases, however, theplatform harvests the
buyer’sdata. We invert the flow: the priceable
asset is theseller’s verified information about the
product, and the buyer agent is the one paying for it.
Where a star rating is a cheap, gameable summary,
a cryptographically attestable service record, an
audited return-rate, or a paid conversation with an
identified prior owner is costly to fake and therefore
informative.
The shrinking storefront.As buyers become
agents, the front-facing storefront—the search
box, the ranked grid, the “recommended for you”
carousel—loses its privileged position; agents
transact against APIs and negotiate over evidence
rather than scroll. The competitive question shifts
fromwho ranks first?towho can substantiate their
claims most cheaply and credibly?
3 The Vision: A Micro-Transaction
Market for Verified Information
Figure 1 sketches the market. A user delegates
intent, a budget, and constraints to a buyer agent;
the buyer agent acquires evidence from a supply
side of sellers, data vendors, and reviewers, settling
micro-payments through a pricing engine over an
x402/AP2 rail. We develop the mechanism below.
3.1 Why not give the data away?
Listing a product already costs money, and that
fee funds the marketplace. We propose to make
information itselfthe unit of exchange. A listing
exposes some attributes for free and prices the rest:
the buyer agent knows the basics, asks for more,
and pays per disclosure. Crucially, this is freemium
with feedback. A popular product—or one whose
data reliably converts scrutiny into sales—can com-
mand higher prices for its information, and a seller-
side pricing agent that learns to price each datum
well captures proportionally more revenue. De-
mand for specific data is itself signal: an agent
that pays to see torque figures reveals a different
intent than one buying a service history, so the
queries asked sharpen the seller’s price prediction
over time.
3.2 What are the constraints, and how do
agents negotiate them?
Both sides operate under constraints.Hardcon-
straints are inviolable: a seller’s reserve price
or deadline to sell; a buyer’s budget or a non-
negotiable specification.Softconstraints are tun-
able: how much to charge for each datum, how
much to spend before escalating, how long to keep
searching. Pricing and acquisition therefore be-
come a negotiation (Liu et al., 2026; Zhang et al.,
2026): buyer and seller agents exchange offers
over bundles of evidence, and a buyer rationally
abandons a product the moment an unmet hard con-
straint is revealed—makingwhat was asked, and
when the buyer walked awaya rich pricing signal.
A recurring design question is how often either
agent should return to its human principal to relax
a constraint.
3.3 What is actually sold, and who verifies it?
Beyond seller-attested attributes (materials, suppli-
ers, audited sales and support metrics), the market
admits third parties: independent test labs, and
trusted reviewers who can be paid for an opinion or
booked for a live session with the buyer. Because
paid testimony invites fraud, reviewers carry a rep-
utation/trust score settled by staking—borrowing
the incentive logic of decentralised oracles and pre-
diction markets (Peterson et al., 2020)—so that
a reviewer later contradicted by outcomes loses
standing and earning power.
3.4 How should a buyer agent decide what to
buy, and when to stop?
On the buyer’s side, every paid query is a tool
call with a price tag, and the agent’s competence
is largely itsacquisition policy: which datum to
3

User Buyer Agent Marketplace: Listing & Pricing Engine Sellers · Data vendors · Reviewers intent, budget, constraints x402/AP2 micro-payments evidence requests
verified data payloads
NLP @ buyer:preference
elicitation; cost-optimal
acquisition; grounding check
NLP @ market:real-
time entity resolution;
data pricing & negotia-
tion; reviewer trust scoring
Figure 1: Agentic e-commerce as a micro-transaction market forverified information. The buyer agent spends
micro-payments (x402/AP2) to progressively unlock seller- and reviewer-supplied data; the heavy NLP lifting
(dashed) is acquisition policy, pricing/negotiation, entity resolution, trust scoring, and grounding—not catalogue
ranking.
buy next, and when to stop. This is the central
open problem we return to in §4; here we only
note that it adds an explicit monetary objective to
ordinary tool use—weighing the expected value
of reduced uncertainty against both payment cost
and the user’s attention—and that the agent should
surface the trade-off to its owner when the marginal
cost of investigation approaches the value at stake.
3.5 At the limit, why buy the finished product
at all?
Taken to its conclusion, an agent with enough veri-
fied information about a product’s bill of materials
and suppliers need not buy the finished good at all:
it can source the components and commission as-
sembly, buying the final product only when integra-
tion, warranty, or brand is worth the premium. This
is information-driven competition at its sharpest—
and a provocation about where the value, and the
data, ultimately sit.
4 Open Challenges for the Applied NLP
Community
The vision is only as credible as the NLP it de-
mands. We frame the open problems as five NLP
tasks that recur as a purchase unfolds—acquire evi-
dence, price and negotiate it, resolve and ground it,
generate without fabricating, and model the buyer—
each a place where the industry track is well placed
to make progress.
4.1 Cost-aware tool use
Treating priced data and reviewer time as tools
turns shopping intocost-aware tool use: sequential
decision-making under a budget that estimates the
expected value of each available datum, buys the
most cost-effective one, and stops when marginal
value falls below price—or below the cost of bother-
ing a human.3 The hard part is calibration: an agent
should pay for external data only out ofepistemic
necessity—when its own parameters cannot resolve
the uncertainty (Wang et al., 2026b)—rather than
reaching for a tool reflexively and buying facts it
already reliably knows (Zeng et al., 2026). And be-
cause each datum carries its own price, the familiar
tool-use question of whether to call a tool is over-
taken by a sharper one—whichtool to call when
every option costs differently—so tool selection
under heterogeneous prices becomes a far more
pronounced problem here than in standard tool use,
where external calls are free or uniformly cheap.
Because the spend is committed before the answer
is known, this also demands prospective control:
triaging which queries to make under a fixed budget
(Nazi and Dipta, 2026), trading information gain
against both payment cost and the user’s attention.
4.2 Negotiation dialogue
Pricing a single datum, and negotiating bundles of
evidence, casts product investigation asnegotia-
tion dialogue—a long-standing NLP task (Lewis
et al., 2017; He et al., 2018)—now at the inter-
section of dialogue andmechanism design(Liu
et al., 2026; Zhang et al., 2026). It is also agame:
buyer and seller hold private valuations, each learns
fromwhichdata the other will buy or disclose, and
both act strategically—so a competent agent rea-
sons about best responses under incomplete infor-
mation, not merely about a fair price. Progress
is gated onevaluation, since we cannot A/B test
against real buyers cheaply or ethically. Existing
benchmarks probe negotiation, economic decision-
3NLP work on curbing excessive, low-value tool calls is a
natural starting point (Li et al., 2026; Schick et al., 2023); our
setting differs in making the objective explicitly monetary.
4

making, and agentic purchasing (Zhang et al., 2026;
Fish et al., 2025; Liu et al., 2026; Allouah et al.,
2026; Yu et al., 2026), yet none pricesinforma-
tion itselfas a good bought under a micro-payment
budget, nor scores the welfare and efficiency of
paid-evidence acquisition. A practical path is to
extend the community’s Wizard-of-Oz and LLM-
based user simulators (Budzianowski et al., 2018;
Davidson et al., 2023; Sekuli´c et al., 2024) intoeco-
nomicsimulators—populations of buyer and seller
agents with private valuations and constraints—so
that pricing and negotiation can be measured on
welfare and calibration, not just deal rate.
4.3 Entity resolution and knowledge-base
construction
For evidence to be priced and compared, it must be
addressable and mean the same thing to both par-
ties. Messy, multi-vendor evidence (“full service
history, one owner from new”) must be resolved on
the fly to a standardised product ontology, so that
the same attribute from different sellers is compara-
ble and individually priceable—entity and attribute
resolution under latency and incomplete-schema
pressure, which is what lets a buyer agent ask for,
and pay for, exactly one missing field. The ontol-
ogy and the rules for mapping onto it are market-
specific—fitment rules for parts, failure modes for
vehicles, compliance regimes for regulated goods—
so an agent entering a particular market may dock
a dedicatedexpert domain adapterfor resolution
(Pfeiffer et al., 2021), rather than rely on a single
general resolver. Buyer and seller must alsoagree
they are discussing the same referent before a price
means anything, a pragmatic-grounding step closer
to consensus-and-repair than to one-shot record
linkage. At marketplace scale this becomes con-
tinuous, provenance-taggedautomated knowledge-
base construction: the lineage of never-ending ex-
traction systems (Carlson et al., 2010), but with
every belief carrying a price and a verifiable source.
4.4 Grounded generation and hallucination
detection
If a buyer agent fabricates an attribute—or a seller
agent embellishes one—to keep a transaction alive,
the market collapses: its entire premise is that
paidinformation is more trustworthy than free in-
formation. Generation must be constrained to a
real, attestable inventory, extending grounding and
citation methods for commercial dialogue (Zeng
et al., 2025) toward verifiable provenance for every
priced claim, with hallucinationdetectiona first-
class check on both sides of a trade—and with per-
suasive optimisation (Salvi et al., 2026) bounded
so that agents compete on evidence, not rhetoric.
4.5 Preference elicitation and persona
modelling
Almost no agent today carries a model of theper-
son—their tastes, thresholds, and how and when
they want to be notified—yet matching verified
products to a buyer presupposes exactly this, mak-
ing it the challenge that touches the user most di-
rectly.
Elicitation.Durable preferences must be inferred
from dialogue and behaviourwithoutinterrogating
the user: an agent that asks twenty questions be-
fore every purchase is worse than the storefront it
replaces. The task is mixed-initiative preference
elicitation that separates stable traits (brand affini-
ties, a budget band, ethical constraints such as “buy
from the original manufacturer to support it”) from
purchase-specific intent, and that knows when one
clarifying question is worth more than another paid
datum. Long-horizon, preference-grounded shop-
ping benchmarks are a start (Yu et al., 2026), but
most assume preferences aregivenrather than dis-
covered; the game-theoretic “solicit-then-suggest”
model shows that multi-round solicitation reduces
matching error far more than broadening final rec-
ommendations (Cao and Hu, 2026).
Representation and storage.How the persona
is stored is itself a research question. A natural-
language or slot-structured profile is inspectable,
editable, and portable, but leaks easily and must be
reasoned over at every turn (Ramos et al., 2024); a
parametric per-user “personal model” (Mind Lab,
2026) is compact and expressive but opaque and
hard to edit. One promising path is to use com-
posable domain adapters (Pfeiffer et al., 2021)
to dynamically dock category-specific expertise
onto these personal weights. Preferences also drift,
so any representation needs calibrated updating;
recent work distils interaction history into com-
pact preference memory for reranking (Peng et al.,
2026).
Alignment and notification timing.The agent
must align to what the user wantsnow, not merely
extrapolate past behaviour, and must resist a per-
sona that adversarial listings have nudged. Align-
ment also governswhento interrupt: today’s assis-
5

tants show aneagerness biasthat interrupts prema-
turely (Wang et al., 2026a), while the subjectivity
of intervention timing means generalised triggers
risk alarm fatigue (Modgil, 2026). This subsumes
the earlier question of when to escalate to the princi-
pal to relax a constraint—a personalised judgement
weighing the value of a clarification against its dis-
ruption cost.4 The same persona that personalises
service becomes a liability if mis-stored, or if it
leaks willingness-to-pay through role-coherence
failures (Alavi and Nozari, 2026)—which we treat
as an ethical question below.
5 Conclusion
We have argued that as e-commerce becomes agen-
tic, the scarce and valuable good is not the rank-
ing butverified information, and that a micro-
transaction market for that information—now tech-
nically feasible on agent-native payment rails—
would reward genuine quality and sharpen com-
petition. For applied NLP this is a redirection:
away from optimising chat fluency and conver-
sion, and toward the pipeline that turns dialogue
into priced, grounded, negotiable evidence—cost-
optimal acquisition, data pricing, real-time entity
resolution, and hallucination-free value exchange.
We invite the industry track to build and benchmark
that pipeline.
Limitations
This is a forward-looking position, not a deployed
system or an empirical study; our claims about mar-
ket efficiency and competition are hypotheses, not
measurements. The vision presupposes adoption
that may not materialise: sellers must be willing
to expose verified data, buyers must trust agents
with budgets, and agent-native payment rails (x402,
AP2) are early and unevenly supported. Monetary
figures in our running example (e.g., £0.25 for a
service-history digest) are illustrative only. Finally,
the economic mechanisms we sketch—freemium
data pricing and reviewer staking—are described
at the level of a vision; their incentive compatibil-
ity and resistance to collusion require formal and
empirical study that we do not provide here.
4Framing a contested purchase as a debate the user adju-
dicates (Irving et al., 2018; Khan et al., 2024) is one way to
keep a human in control of an agent acting on their behalf.
Ethical Considerations
Consent and transparency.A market thatpays
forinformation must not become one that quietly
extractsit. Buyers should be told when their agent
is purchasing data, from whom, and at what cost;
sellers and reviewers should consent to what is
exposed. We explicitly reject covert harvesting of
a user’s own data as a business model.
Privacy and PII.Verified product data can carry
personal data about people—a previous owner, a
named reviewer, a support transcript. Any datum
that is packaged and sold must be scrubbed of per-
sonally identifiable information unless its subject
has consented; pipelines should treat PII removal
as a first-class step, with attention to GDPR/CCPA
obligations and to LLM memorisation of transac-
tion data.
Manipulation and trust.The channel that prices
evidence can be attacked: SEO-style and prompt-
injection attacks may hijack what an agent per-
ceives, and persuasive optimisation (Salvi et al.,
2026) may push agents to win on rhetoric rather
than fact—hence our insistence on grounded value
exchange and reputationally-staked reviewers (Pe-
terson et al., 2020; Irving et al., 2018).
Persona storage and ownership.Where the per-
sona lives, and who controls it, is an ethical design
decision, not an implementation detail. A profile
rich enough to shop well is rich enough to exploit:
a seller who can read it can price-discriminate up
to the user’s willingness to pay, and a leaked or
stolen persona is a ready-made target for profil-
ing and scams. Furthermore, agents are suscepti-
ble to “role-coherence” leakages, where natural-
language persona descriptions or multi-turn conver-
sational responses inadvertently expose a buyer’s
reservation prices and budget to strategic sellers
(Alavi and Nozari, 2026). We argue the persona
should beuser-held, portable, and inspectable,
with data minimisation and purpose limitation by
default; and that the agent’s own paid queries—
which reveal the persona to sellers (§3)—warrant
privacy-preserving acquisition. Parametric per-
sonal models (Mind Lab, 2026) also complicate
the GDPR/CCPA right to erasure, since a prefer-
ence encoded in weights cannot simply be deleted:
reconciling personalised agents with rectification
and the “right to be forgotten” is an open and press-
ing problem.
6

Power and access.A data market can entrench
incumbents who can afford to substantiate claims.
Designing it so that small, honest sellers arere-
wardedfor transparency rather than priced out is a
precondition for the “truer competition” we claim.
References
Soogand Alavi and Salar Nozari. 2026. When agents
shop for you: Role coherence in AI-mediated mar-
kets.Preprint, arXiv:2604.26220. Working paper,
University of Iowa.
Amine Allouah, Omar Besbes, Josué D. Figueroa, Yash
Kanoria, and Akshit Kumar. 2026. What is your AI
agent buying? evaluation, biases, model dependence,
& emerging implications of agentic e-commerce.
InProceedings of the ACM Web Conference 2026
(WWW).
Tim Berners-Lee, James Hendler, and Ora Lassila. 2001.
The semantic web.Scientific American, 284(5):34–
43.
Paweł Budzianowski, Tsung-Hsien Wen, Bo-Hsiang
Tseng, Iñigo Casanueva, Stefan Ultes, Osman Ra-
madan, and Milica Gaši ´c. 2018. MultiWOZ – a
large-scale multi-domain wizard-of-oz dataset for
task-oriented dialogue modelling. InProceedings
of the 2018 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 5016–
5026.
Shengyu Cao and Ming Hu. 2026. A solicit-then-
suggest model of agentic purchasing.Preprint,
arXiv:2603.20972. Working paper, University of
Toronto. Presented at the Marketplace Innovation
Workshop (MIW) 2026.
Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr
Settles, Estevam R. Hruschka, and Tom M. Mitchell.
2010. Toward an architecture for never-ending lan-
guage learning. InProceedings of the Twenty-Fourth
AAAI Conference on Artificial Intelligence (AAAI),
pages 1306–1313.
Sam Davidson, Salvatore Romeo, Raphael Shu, James
Gung, Arshit Gupta, Saab Mansour, and Yi Zhang.
2023. User simulation with large language mod-
els for evaluating task-oriented dialogue.Preprint,
arXiv:2309.13233.
European Commission CORDIS. 2023. Blockchain
protocol for responsible mineral sourcing. https://
cordis.europa.eu/project/id/946437/repor
ting. Horizon 2020 project report: MINESPIDER,
Grant agreement ID 946437, Accessed: 2026-06-16.
Sara Fish, Julia Shephard, Minkai Li, Ran I. Shorrer, and
Yannai A. Gonczarowski. 2025. EconEvals: Bench-
marks and litmus tests for economic decision-making
by LLM agents.Preprint, arXiv:2503.18825.
Google. 2025. Agent payments protocol (AP2): An
open protocol for agent-led payments. Google Cloud
Blog, https://cloud.google.com/blog/produc
ts/ai-machine-learning/announcing-agent
s-to-payments-ap2-protocol . Announced 16
September 2025; accessed 2026-06-17.
He He, Derek Chen, Anusha Balakrishnan, and Percy
Liang. 2018. Decoupling strategy and generation in
negotiation dialogues. InProceedings of the 2018
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 2333–2343, Brus-
sels, Belgium. Association for Computational Lin-
guistics.
Geoffrey Irving, Paul Christiano, and Dario Amodei.
2018. AI safety via debate.Preprint,
arXiv:1805.00899.
Akbir Khan, John Hughes, Dan Valentine, Laura
Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward
Grefenstette, Samuel R. Bowman, Tim Rocktäschel,
and Ethan Perez. 2024. Debating with more per-
suasive LLMs leads to more truthful answers. In
Proceedings of the 41st International Conference on
Machine Learning (ICML).
Mike Lewis, Denis Yarats, Yann Dauphin, Devi Parikh,
and Dhruv Batra. 2017. Deal or no deal? end-to-
end learning of negotiation dialogues. InProceed-
ings of the 2017 Conference on Empirical Methods
in Natural Language Processing (EMNLP), pages
2443–2453, Copenhagen, Denmark. Association for
Computational Linguistics.
Zeping Li, Hongru Wang, Yiwen Zhao, Guanhua Chen,
Yixia Li, Keyang Chen, Yixin Cao, Guangnan Ye,
Hongfeng Chai, and Zhenfei Yin. 2026. Rethink-
ing the role of entropy in optimizing tool-use be-
haviors for large language model agents.Preprint,
arXiv:2602.02050.
Xianyang Liu, Shangding Gu, and Dawn Song.
2026. AgenticPay: A multi-agent LLM negotia-
tion system for buyer–seller transactions.Preprint,
arXiv:2602.06008.
Mind Lab. 2026. On the scaling of PEFT: Towards mil-
lion personal models of trillion parameters.Preprint,
arXiv:2606.02437.
Manvendra Modgil. 2026. The saturation trap and the
subjectivity of intervention timing: Why affect-based
triggers and LLM judges fail to time interventions on
autonomous agents.Preprint, arXiv:2606.04296.
Zabir Al Nazi and Shubhashis Roy Dipta. 2026.
TRIAGE: Evaluating prospective metacognitive con-
trol in LLMs under resource constraints.Preprint,
arXiv:2605.13414.
Zhiyuan Peng, Xuyang Wu, Huaixiao Tou, Yi Fang,
and Yu Gong. 2026. MemRerank: Preference mem-
ory for personalized product reranking.Preprint,
arXiv:2603.29247.
7

Jack Peterson, Joseph Krug, Micah Zoltu, Austin K.
Williams, and Stephanie Alexander. 2020. Augur: A
decentralized oracle and prediction market platform.
Preprint, arXiv:1501.01042.
Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé,
Kyunghyun Cho, and Iryna Gurevych. 2021.
AdapterFusion: Non-destructive task composition for
transfer learning. InProceedings of the 16th Confer-
ence of the European Chapter of the Association for
Computational Linguistics (EACL), pages 487–503.
Association for Computational Linguistics.
Jerome Ramos, Hossein A. Rahmani, Xi Wang, Xiao Fu,
and Aldo Lipani. 2024. Transparent and scrutable
recommendations using natural language user pro-
files. InProceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 13971–13984, Bangkok,
Thailand. Association for Computational Linguistics.
Francesco Salvi, Alejandro Cuevas, and Ma-
noel Horta Ribeiro. 2026. Commercial per-
suasion in AI-mediated conversations.Preprint,
arXiv:2604.04263.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta
Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola
Cancedda, and Thomas Scialom. 2023. Toolformer:
Language models can teach themselves to use tools.
InAdvances in Neural Information Processing Sys-
tems (NeurIPS).
Ivan Sekuli´c, Silvia Terragni, Victor Guimarães, Nghia
Khau, Bruna Guedes, Modestas Filipavicius, An-
dré Ferreira Manso, and Roland Mathis. 2024. Re-
liable LLM-based user simulator for task-oriented
dialogue systems. InProceedings of the 1st Work-
shop on Simulating Conversational Intelligence in
Chat (SCI-CHAT 2024) at EACL, pages 18–27.
The Provenance Team. 2015. Blockchain: The solution
for transparency in product supply chains. https:
//www.provenance.org/news-insights/blockc
hain-the-solution-for-transparency-in-pro
duct-supply-chains. White paper, updated 2023,
Accessed: 2026-06-16.
Awid Vaziry, Sandro Rodriguez Garzon, and Axel Küp-
per. 2025. Towards multi-agent economies: Enhanc-
ing the A2A protocol with ledger-anchored identities
and x402 micropayments for AI agents.Preprint,
arXiv:2507.19550.
Danqing Wang, Da Yin, Ruta Desai, Lei Li, Asli Ce-
likyilmaz, and Ansong Ni. 2026a. Learning to inter-
rupt in language-based multi-agent communication.
Preprint, arXiv:2604.06452.
Hongru Wang, Cheng Qian, Manling Li, Jiahao Qiu,
Boyang Xue, Mengdi Wang, Heng Ji, Amos Storkey,
and Kam-Fai Wong. 2026b. Position: Agent should
invoke external tools only when epistemically nec-
essary. InProceedings of the 43rd International
Conference on Machine Learning (ICML). Position
Paper Track.
Zijian Yu, Kejun Xiao, Huaipeng Zhao, Tao Luo, and
Xiaoyi Zeng. 2026. Shopping companion: Bench-
marking and training LLM agents for long-horizon
preference-grounded e-commerce tasks.Preprint,
arXiv:2603.14864.
Jingying Zeng, Hui Liu, Zhenwei Dai, Xianfeng Tang,
Chen Luo, Samarth Varshney, Zhen Li, and Qi He.
2025. Cite before you speak: Enhancing context-
response grounding in e-commerce conversational
LLM-agents.Preprint, arXiv:2503.04830.
Yirong Zeng, Shen You, Yufei Liu, Qunyao Du, Xiao
Ding, Yutai Hou, Yuxian Wang, Wu Ning, Haonan
Song, Dandan Tu, Bibo Cai, and Ting Liu. 2026.
The tool-overuse illusion: Why does LLM prefer
external tools over internal knowledge?Preprint,
arXiv:2604.19749.
Erica Zhang, Fangzhao Zhang, Aneesh Pappu, Batu
El, Jose Blanchet, Susan Athey, Jiashuo Liu, and
James Zou. 2026. TERMS-Bench: Diagnosing
LLM negotiation agents beyond deal rate.Preprint,
arXiv:2605.13909.
8
