---
title: 'Privacy-First Engineering: Re-Architecting High-Scale Real-Time Advertising Platforms for Global
  Data Regulations'
url: https://doi.org/10.37284/eajit.9.2.5699
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: East African Journal of Information Technology
authors:
- Ravindra Motiram Gurnani
source: openalex-oa
pdf_url: https://journals.eanso.org/index.php/eajit/article/download/5699/6039
pages: 14
chars: 52235
fetched_at: '2026-11-08T18:41:10+00:00'
kb_version: 1
---

# Privacy-First Engineering: Re-Architecting High-Scale Real-Time Advertising Platforms for Global Data Regulations

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

219 | This work is licensed under a Creative Commons Attribution 4.0 International License.

c-light-blue-500

East African Journal of Information
Technology
eajit.eanso.org
Volume 9, Issue 2, 2026
Print ISSN: 2707-5346 | Online ISSN: 2707-5354
Title DOI: https://doi.org/10.37284/2707-5354

EAST AFRICAN
NATURE &
SCIENCE
ORGANIZATION
Original Article
Privacy-First Engineering: Re -Architecting High -Scale Real -Time Advertising
Platforms for Global Data Regulations
Ravindra Motiram Gurnani1*

1 Independent Researcher, USA.
* Author for Correspondence Email; office.sarcpublisher@gmail.com

 Article DOI: https://doi.org/10.37284/eajit.9.2.5699

Date Published:

04 September 2026

Keywords:

Privacy-by-design,
Real-time bidding,
GDPR,
programmatic
advertising,
Consent management,
Data minimisation,
Differential privacy,
 Re-architecture.

ABSTRACT
Real-time bidding (RTB) and programmatic advertising ecosystems
have been engineered over more than a decade primarily for throughput
and revenue optimisation, with data privacy treated largely as a post-hoc
compliance exercise. The enactment of the Genera l Data Protection
Regulation (GDPR) in the European Union, the California Consumer
Privacy Act (CCPA) in the United States, and Brazil's Lei Geral de
Proteção de Dados (LGPD) has fundamentally disrupted this design
philosophy. These regulations impose requ irements for informed
consent, data minimisation, purpose limitation, and cross -border
transfer controls that are structurally incompatible with legacy
advertising stack architectures. Empirical studies reveal the depth of the
problem: only a small minority of cookie consent banners were found to
be fully GDPR-compliant (Utz et al., 2019), and a majority of websites
registered with the IAB Transparency and Consent Framework violated
at least one regulatory requirement (Matte et al., 2020). Browser
fingerprinting, a method that bypasses consent mechanisms by never
storing a client -side identifier, has been shown to correctly re -identify
users across varied browser environments in the large majority of cases
(Laperdrix et al., 2020), illustrating why surface -level compliance
measures leave a structural gap. This paper proposes a privacy -first re-
architecture of high-scale RTB platforms, introducing a layered design
comprising a consent management layer, a data minimisation pipeline,
purpose-binding enforcement modules, and differential privacy
mechanisms for aggregate analytics. Engineering trade -offs across
latency, throughput, and multi -jurisdiction deployability are examined
for the proposed architecture. Findings indicate that privacy -by-design
principles, w hen integrated at the infrastructure level rather than the
application layer, yield both regulatory compliance and competitive
operational performance.
APA CITATION
Gurnani, R. M. (2026). Privacy-First Engineering: Re-Architecting High-Scale Real-Time Advertising Platforms for Global
Data Regulations. East African Journal of Information Technology, 9(2), 219-232. https://doi.org/10.37284/eajit.9.2.5699.

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

220 | This work is licensed under a Creative Commons Attribution 4.0 International License.

CHICAGO CITATION
Gurnani, Ravindra Motiram . (2026). “Privacy-First Engineering: Re -Architecting High -Scale Real -Time Advertising
Platforms for Global Data Regulations ”. East African Journal of Information Technology 9 (2), 219-232.
https://doi.org/10.37284/eajit.9.2.5699.
HARVARD CITATION
Gurnani, R. M . (2026). “Privacy-First Engineering: Re -Architecting High -Scale Real -Time Advertising Platforms for
Global Data Regulations”, East African Journal of Information Technology, 9(2), pp. 219-232. doi: 10.37284/eajit.9.2.5699.
IEEE CITATION
R. M. Gurnani, “Privacy-First Engineering: Re-Architecting High-Scale Real-Time Advertising Platforms for Global Data
Regulations”, EAJIT, vol. 9, no. 2, pp. 219-232, Sep. 2026.
MLA CITATION
Gurnani, Ravindra Motiram . (2026). “Privacy-First Engineering: Re -Architecting High -Scale Real -Time Advertising
Platforms for Global Data Regulations”, EAJIT, vol. 9, no. 2, pp. 219-232, Sep. 2026, doi:10.37284/eajit.9.2.5699.
INTRODUCTION
The modern programmatic advertising ecosystem
processes hundreds of billions of bid requests per
day, routing user behavioural signals across
hundreds of DSPs, DMPs, and SSPs — each
auction completing within a 100 -millisecond
window. This architecture was designed to
maximise signal richness, bidder reach, and
clearing efficiency. Privacy was never a
foundational design principle in these systems;
instead, it was handled through notice-and-choice
mechanisms such as cookie bann ers and opt -out
links, tools that legal analysis has since shown to
be structurally inadequate (Voigt & von dem
Bussche, 2017; Tankard, 2016).
GDPR's entry into force in May 2018 reset the
compliance baseline across the advertising
industry. Every processing activity now requires a
documented lawful basis; data subjects must be
able to exercise rights on prescribed timelines;
collection cannot exceed the purposes stated at the
outset and automated profiling without
meaningful human oversight is off the  table
(Voigt & von dem Bussche, 2017). California's
CCPA followed in January 2020, giving residents
the power to block the sale of their personal data
to third parties. Brazil's LGPD, enacted the same
year, extended comparable protections to
Brazilian res idents. The result is a set of
overlapping, sometimes conflicting obligations
that RTB platforms built in an earlier era were
never designed to accommodate.
The shortcomings are not confined to legal theory.
Concrete financial consequences have followed:
Irish supervisory authorities levied hundreds of
millions of euros in fines against major
technology operators between 2021 and 2023,
with ad -tech data processing practices sitting at
the core of each decision. This enforcement record
establishes that architectural non-compliance is a
business-critical risk, not a speculative legal
exposure.
This paper makes three primary contributions.
First, it characterises the structural
incompatibilities between legacy RTB
architectures and contemporary data protection
requirements. Second, it proposes a privacy -first
re-architecture comprising four functional layers:
consent management, data minimisation, purpose-
binding enforcement, and differentially private
analytics. Third, it analyses engineering trade-offs
associated with deploying this architecture at
hyperscale, including latency implications,
jurisdictional configuration complexity, and
compatibility with existing industry standards
such as the IAB Transparency and Consent
Framework (TCF). The remainder of this paper is
organised as follows: Section 2 reviews relevant
background literature; Section 3 characterises
regulatory compliance challenges; Section 4
presents the proposed re -architecture; Section 5
discusses implementation considerations; Section
6 address es broader industry implications; and
Section 7 concludes.
BACKGROUND AND RELATED WORK
Online Tracking and Data Collection Practices
Large-scale empirical measurement studies have
documented the pervasive deployment of third -

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

221 | This work is licensed under a Creative Commons Attribution 4.0 International License.

party tracking technologies across the web.
Englehardt and Narayanan (2016) conducted a
comprehensive measurement of one million
websites, cataloguing the deployment patterns of
cookies, pixel trackers, and fingerprinting scripts
across the web's most -visited properties. Their
work mapp ed the scale of web tracking and
showed that data collection was
disproportionately concentrated among a handful
of large intermediaries.
Browser fingerprinting has matured into a
technically sophisticated tracking method that
sidesteps cookie controls entirely, because no
client-side identifier needs to be stored. A wide -
ranging survey by Laperdrix et al. (2020)
catalogued the breadth of fi ngerprinting
techniques in active deployment and reported
correct re -identification across varied browser
configurations in roughly nine out of ten cases , a
result that illustrates why device attributes alone
can constitute a rich behavioural signal. Solomos
et al. (2020) pushed this further, mapping
fingerprinting methods that work across device
boundaries, which widens the compliance
perimeter that any privacy-first architecture must
cover.
Fouad et al. (2020) turned up a further category of
trackers that slip past standard filter lists: invisible
pixel beacons combined with timing -based
identification allow these scr ipts to collect
behavioural signals without appearing in any
block list. The finding matters architecturally
because it shows that the tracking landscape
actively evolves to circumvent both technical
controls and regulatory frameworks , a dynamic
that makes any compliance approach relying
solely on static denylists structurally fragile.
Consent Frameworks and Regulatory Impact
IAB Europe's TCF set out to give publishers and
the programmatic supply chain a uniform
mechanism for capturing and forwardi ng user
consent. In practice, independent audits have
found it structurally deficient. Matte et al. (2020)
reviewed TCF -registered sites and reported that
the majority had logged positive consent decisions
without any user action, or had continued
processing after users withdrew consent , both of
which directly contradict GDPR's consent
definition. Degeling et al. (2019) observed a
separate but related pattern at the publisher layer:
cookie notices became far more prevalent after
GDPR enforcement began, climbing from around
62% of EU sites to roughly 90%, yet the same
study found that the majority of these notices were
deployed as compliance optics rather than genuine
consent-gathering mechanisms.
Utz et al. (2019) deepened this critique by auditing
the consent notices themselves: fewer than one in
eight satisfied all applicable GDPR criteria. The
most common failures were missing rejection
pathways, pre -selected consent options, and
bundled multi -purpose accept actions that made
granular choice impossible.
Dark patterns in consent design have received
sustaineempirical scrutiny. Nouwens et al. (2020)
catalogued manipulative interface choices ; pre-
checked consent boxes, unequal accept/reject
pathways, misleading copy and showed that each
raises acceptance rates beyond what an impartial
design would produce. The consent these patterns
generate is legally suspect under GDPR because it
cannot be considered freely given. Grassl et al.
(2021) offered a constructive counterpoint: they
defined a class of 'br ight patterns' that serve user
autonomy rather than subvert it, and documented
cases where this approach had been implemented
at scale without sacrificing usability. The legal
and technical case analysed by Veale and
Zuiderveen Borgesius (2022) is starker: they
concluded that conventional RTB cannot be made
compatible with GDPR's lawful basis, data
minimisation, and purpose limitation
requirements, because the broadcast structure of
bid requests — personal data transmitted to many
buyers simultaneously, before any auction
outcome — is a foundational design conflict.
Sanchez-Rola et al. (2019) traced h ow GDPR's
cookie-notice requirements have spread into other
legal systems, producing overlapping obligations
that complicate cross -border platform
deployments.

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

222 | This work is licensed under a Creative Commons Attribution 4.0 International License.

The empirical picture that emerges from this body
of work is consistent: widespread non-compliance
is not an anomaly but a structural feature of the
current consent -management landscape.
Platforms seeking to achieve genuine compliance
cannot do so by patch ing existing architectures;
they must reconsider the underlying data flows.
Privacy, Transparency, and Microtargeting
Privacy decision -making under real -world
conditions has been studied from a behavioural
economics perspective by Acquisti et al. (2015),
who documented a recurring gap between the
privacy preferences people express and the
choices they make when facing inf ormation
asymmetries and cognitive load. For ad -tech
platforms, this finding has direct implications: a
user who nominally clicks 'accept' on a complex
consent interface may not be providing the
informed, unambiguous agreement that GDPR
demands. Tene and Polonetsky (2012) and Cate
and Mayer-Schönberger (2013) had earlier argued
that disclosure -based governance models break
down at the scale and velocity of programmatic
data flows, because meaningful individual
evaluation of each processing activity is simply
not feasible.
Tene and Polonetsky (2012) and Cate and Mayer-
Schönberger (2013) had already challenged the
disclosure-and-choice model on structural
grounds, arguing that neither meaningful notice
nor real individual choice is achievable when data
flows operate at programmatic scale and speed.
Andreou et al. (2018) brought empirical weight to
the transparency dimension: their audit of social
media advertising interfaces found systematic
gaps between the targeting signals platforms
disclosed to users and those actually deployed in
campaign delivery. Zuiderveen Borgesiu s et al.
(2018) examined political advertising and
concluded that when the same behavioural
profiling machinery serves electoral campaigns,
the harms extend beyond individual privacy into
the integrity of democratic deliberation. A
separate line of enquiry , pursued by Iordanou et
al. (2018), identified economic injury as an
additional dimension of harm: behavioural data
gathered ostensibly for advertising was shown to
underpin differential pricing in e -commerce
contexts, so the privacy exposure entailed
measurable financial consequences for affected
users.
Table 1: Regulatory Requirements Matrix for Global Advertising Platforms
Regulation Jurisdictio
n
Consent Basis Data Subject
Rights
Data
Residency
Requireme
nts
Cross-
Border
Transfer
Max Penalty
GDPR EU / EEA Explicit opt -in
(Art. 7); lawful
basis required
Access, erasure,
portability,
restriction,
objection
Implied via
adequacy
decisions;
cross-border
transfer
restricted
SCCs,
BCRs,
adequacy
decisions
EUR 20M or
4% global
annual turnover
CCPA /
CPRA
California,
USA
Opt-out for
sale/sharing;
explicit for
sensitive data
Know, delete,
correct, opt-out,
limit use of
sensitive PI
No explicit
residency
mandate; de
facto US
storage
common
No
categorical
ban;
contractual
safeguards
required
USD 7,500 per
intentional
violation
LGPD Brazil Explicit consent
or legitimate
interest (Art. 7)
Access,
correction,
anonymisation,
deletion,
portability
Cross-
border
transfer
restricted to
adequate
countries or
via SCCs
equivalent
Internationa
l data
transfer
clauses or
global
corporate
policy
Up to 2% of
Brazil revenue;
max BRL 50M
per infraction

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

223 | This work is licensed under a Creative Commons Attribution 4.0 International License.

Regulation Jurisdictio
n
Consent Basis Data Subject
Rights
Data
Residency
Requireme
nts
Cross-
Border
Transfer
Max Penalty
PDPA Thailand Explicit
consent;
legitimate
interest
recognised
Access, erasure,
restriction,
portability,
objection
Transfer to
jurisdictions
with
equivalent
protection
only
Contractual
clauses or
PDPC-
approved
mechanism
s
THB 5M civil;
criminal
liability for
intentional
breach
REGULATORY COMPLIANCE
CHALLENGES IN RTB PLATFORMS
Structural Failures of the TCF
The IAB TCF was conceived as a scalable vehicle
for propagating user consent signals through the
RTB supply chain. What it became in practice is
closer to a liability-distribution mechanism than a
genuine privacy safeguard. Its consent string
format allows  downstream bid recipients to
receive and act on signals without indep endently
verifying whether those signals were gathered
lawfully. Andreou et al. (2018) examined
transparency mechanisms across social media
advertising and identified pervasive mismatches
between the targeting attributes platforms
reported to users and the  attributes actually
exploited in campaign delivery , a pattern that
maps directly onto the opacity baked into TCF
consent strings.
Legitimate interest as a legal basis has drawn the
sharpest regulatory fire. The Belgian Data
Protection Authority's 2022 decision against IAB
Europe concluded that the TCF's implementation
of this basis did not satisfy GDPR's balancing
requirements, because the mechanism afforded
neither the platform operator nor the regulator a
reliable means of auditing whether any given
processing activity genuinely served a legitimate
interest that outweighed data subject rights. Matte
et al. (2020) had arrived at a compatible empirical
finding: more than half of TCF -registered
websites exhibited at least one regulatory
violation in their consent banner implementations,
suggesting that the framework's design invited
rather than deterred non-compliance.
Dark Patterns and Consent Validity
GDPR Article 7 sets four conditions for valid
consent: it must be freely given, specific,
informed, and unambiguous. These conditions
impose concrete interface-design obligations that
the majority of deployed consent banners do not
meet. Utz et al. (2019) analysed a broad sample of
consent notices and found that only a small
fraction, roughly one in eight , satisfied every
applicable GDPR criterion. The most prevalent
failures were missing or hard -to-find rejection
pathways, pre -activated consent toggles, and
bundled purpose -level choices that prevented
granular decision -making. Engineering genuine
informed consent at RTB scale demands
interfaces that pre sent each processing purpose
separately, place accept and reject controls on
equal visual footing, capture and timestamp every
decision for audit, and relay those decisions
faithfully to every downstream processor, each of
which carries measurable latency and storage
costs.
The engineering implications of these findings are
significant. Achieving genuine informed consent
at advertising scale requires consent interface
designs that present granular purpose -level
choices without cognitive overload, provide
symmetrical and equal ly prominent accept and
reject pathways, record consent events with
sufficient metadata to demonstrate validity to
regulators, and propagate consent signals
accurately and compl etely to all downstream
processors. Each of these requirements imposes
latency, storage, and computational costs that
must be accounted for in platform design. The
privacy-first re-architecture proposed in this paper

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

224 | This work is licensed under a Creative Commons Attribution 4.0 International License.

addresses these costs explicitly through a
dedicated consent management layer.
Fingerprinting and Technical Circumvention
Browser fingerprinting sits in a blind spot that
consent frameworks were not designed to address.
Because it leaves no client -side trace, it falls
outside the cookie-consent requirements that most
compliance tooling is built around. Laperdrix et
al. (2020) documented identification accuracy of
up to 90.8% across heterogeneous browser
populations, which means that the information
gathered without any consent dialogue can be as
identifying as a named profile. Matte et al. (2020)
reinforced the practical significance of this gap:
among TCF -registered sites, the majority
presented consent banners while simultaneously
deploying tracking mechanisms for which those
banners provided no lawful cover.
Regulatory guidance on fingerprinting has been
catching up, though unevenly. GDPR's personal
data definition extends to any information that can
single out a natural person, directly or indirectly,
and several national supervisory authoriti es have
issued guidance treating fingerprint outputs as
personal data on that basis. Solomos et al. (2020)
added cross -device complexity: their work
showed that fingerprinting attributes gathered
from separate devices can be combined to produce
stable identifiers without any single device storing
a persistent token. A privacy-first architecture that
addresses only cookie -based tracking therefore
leaves a material compliance gap , fingerprinting
must be treated as a first -order engineering
problem, not an afterthought.
Table 2: Architectural Pattern Comparison: Compliance-as-Patch vs. Privacy-First Re-Design
Dimension Compliance-as-Patch (Legacy +
Middleware)
Privacy-First Re-Design
Consent
Enforcement
Post-hoc filter at data egress; consent
signal not propagated upstream
Consent signal ingested at auction entry;
propagated as first -class pipeline
attribute
Data Flow
Model
All data collected; access restricted
reactively via middleware rules
Data collected only for declared, lawful
purposes; minimisation enforced at
ingestion
Feature
Schema
Maximal user profile: cross -site
behavioural, third -party syndicated,
device-fingerprint features
Reduced schema: first -party signals,
pseudonymised identifiers, Topics API
segments only
Data
Residency
Centralised global data stores;
jurisdiction routing bolted on via lookup
tables
Regional data store partitioning; request
routing enforced at infrastructure layer
Latency
Impact
Consent middleware adds 8 -20 ms per
auction; inconsistent enforcement across
pipeline stages
Pre-computed consent state cache;
jurisdiction classification at edge; ~5-12
ms overhead
Regulatory
Coverage
GDPR-focused; CCPA/LGPD/PDPA
coverage partial and manual
Multi-jurisdictional by design;
regulatory rule engine updated
independently of core pipeline
Operational
Complexity
High: middleware creates hidden
dependencies; compliance audits require
full stack trace
Moderate: consent and residency
primitives are explicit; audit surface is
bounded and inspectable
PRIVACY-FIRST ARCHITECTURE FOR
RTB PLATFORMS
The proposed re -architecture distributes privacy
controls across four purpose -built functional
layers, each targeting a distinct compliance
obligation. Keeping the layers independent allows
each to evolve as regulations chang e and permits
jurisdiction-specific tuning without disturbing the
others. The four layers are: a Consent

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

225 | This work is licensed under a Creative Commons Attribution 4.0 International License.

Management Layer that serves as the canonical
record of data -subject decisions; a Data
Minimisation Pipeline that strips or generalises
attributes befo re they enter the bid auction; a
Purpose-Binding Enforcement Module that
blocks any processing step whose declared
purpose is incompatible with the consented use;
and a Differentially Private Analytics Layer that
replaces individual -level query results with
statistically calibrated noise-added outputs.
Table 3: Privacy-First Engineering Decision Matrix
Use Case Data Type Jurisdiction Recommended
Architecture Component
Compliance Risk
Behavioural
retargeting
Cross-site
browsing history
EU / Brazil Replace with Protected
Audience API (on -device
auction); no cross -site data
export
High: purpose
limitation and
cross-site tracking
ban apply
Frequency
capping
Impression count
per user
All
jurisdictions
Pseudonymised counter in
regional store; TTL -enforced
expiry per storage limitation
Low: minimal
data; purpose is
specific and
bounded
Reach
measurement
Deduplicated user
identifiers
EU /
California
Differential privacy noise
injection; aggregate reporting
via Attribution Reporting API
Medium: identifier
linkage risk;
aggregation
mitigates
Audience
segmentation
Inferred interest
categories
All
jurisdictions
Topics API segments
(browser-generated, coarse -
grained); no raw behavioural
export
Low to Medium:
depends on
segment
sensitivity and
declared purpose
Cross-device
identity
Deterministic and
probabilistic ID
graphs
EU / Brazil /
Thailand
First-party authenticated
identity only; probabilistic
graph suspended; DPA -
reviewed data processing
agreement required
High: cross -
context profiling
triggers GDPR
Art. 22 and LGPD
Art. 20
Consent Management Layer
The Consent Management Layer serves as the
authoritative source of truth for all data subject
consent decisions within the platform. Unlike
TCF-compliant consent string propagation, which
encodes consent decisions as opaque binary fields
transmitted within bid requests, the CML
maintains a persistent, queryable consent record
store that is decoupled from the bid request
pipeline. This architectural separation ensures that
consent validity can be independently audited and
that revocation signals propagate atomically
across all processing modules.
Four functional components make up the CML. A
Consent Collection Interface handles the front -
end work: it renders consent UIs calibrated to the
applicable jurisdiction, presents granular purpose-
level choices, enforces unambiguous binary
accept/reject paths, and defaults to a no -consent
state until an explicit signal is registered. A
Consent Storage Service persists these decisions
in a distributed, low-latency store, the operational
requirement being that any downstream module
can retrieve a verified consent record within 2
milliseconds. A Consent Propagation Bus
distributes state changes to all consumer services
in real time as users revoke or modify their
choices. A Consent Audit Logger records every
consent event as an immutable timestamped entry,
producing the evidence trail that regulators may
demand during investigations.
Engineering the CML for RTB latency constraints
requires careful attention to the read path. Consent
lookups must be completable within the time
budget of the bid request lifecycle, typically 80 to
100 milliseconds. The CRS therefore employs an
in-memory cache layer with a write -behind
persistence architecture, enabling sub-millisecond
consent lookups at the cost of bounded

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

226 | This work is licensed under a Creative Commons Attribution 4.0 International License.

consistency windows during cache refresh.
Consent decisions are classified by jurisdiction at
write time, enabling the CSR to route jurisdiction-
specific signal variants to the appropriate
processing modules without per -request
jurisdictional logic.
Data Minimisation Pipeline
The Data Minimisation Pipeline enforces the
GDPR's data minimisation principle (Article
5(1)(c)) and analogous requirements in CCPA and
LGPD at the point of data ingestion. Rather than
collecting the full set of user attributes available
in a bid request and subsequently filtering at query
time, the DMP applies attribute -level
minimisation at ingestion, ensuring that data
elements for which no valid lawful basis exists are
never stored within the platform.
The DMP implements a declarative attribute
schema in which each data element is annotated
with the processing purposes for which it is
required and the minimum lawful basis required
for each purpose. At ingestion, the pipeline
evaluates the consent record for the data subject
against the attribute schema and strips any
attributes for which the lawful basis requirement
is not satisfied. This approach ensures that data
minimisation is enforced as a structural property
of the data store rather tha n a policy applied at
query time, significantly reducing the attack
surface for data leakage and simplifying
regulatory audit.
For bid request attributes that do not constitute
personal data in their raw form but may become
identifying through combination , a category
Fouad et al. (2020) documented as systematically
underserved by existing privacy controls , the
DMP applies a feature generalisation step that
replaces precise values with aggregated or
bucketed representations. Geographic
coordinates, for example, are generalised to
census tract level before storage; timestamp
precision is reduced from milliseco nd to hourly
resolution for retention beyond the immediate
auction window.
Purpose-Binding Enforcement Module
GDPR Article 5(1)(b) requires that pe rsonal data
be collected for specified, explicit, and legitimate
purposes and not further processed in a manner
incompatible with those purposes. Purpose
limitation is among the most challenging GDPR
requirements to operationalise in a complex data
platform because data frequently traverses
multiple processing contexts that may each claim
different lawful bases.
The Purpose -Binding Enforcement Module
addresses this challenge through a data lineage
tracking system that tags each data record at
ingestion with  the purposes for which it was
collected and the lawful basis under which
collection occurred. Subsequent processing
operations that read a tagged record are required
to declare their processing purpose before access
is granted; the PBEM evaluates the decl ared
purpose against the record's purpose tag and the
platform's purpose compatibility matrix, denying
access for incompatible secondary uses. This
architecture implements purpose limitation as an
access control property enforced by infrastructure,
rather than a policy statement subject to manual
compliance review.
The purpose compatibility matrix lives in a
configurable policy document rather than in
compiled code, so it can be revised as regulatory
guidance develops without triggering a
redeployment cycle . Separate matrices are
maintained for GDPR, CCPA, and LGPD
contexts, giving the PBEM the ability to apply
jurisdiction-appropriate constraints to the same
underlying data stream. Where a single processing
activity crosses multiple jurisdictions, the PBEM
resolves the conflict by enforcing the most
restrictive applicable constraint.
Differentially Private Analytics Layer
Advertising platform analytics — campaign
performance measurement, audience reach
reporting, and attribution modelling — have
historically been implemented using exact query
mechanisms over individual-level event data. This
approach is incompatible with privacy -by-design

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

227 | This work is licensed under a Creative Commons Attribution 4.0 International License.

principles because it preserves individual -level
data in analytically accessible form indefinitely,
creating both regulatory exposure and security
risk.
The Differentially Private Analytics Layer
replaces exact individual-level query mechanisms
with a noise -injection architecture based on
differential privacy (DP). Under this architecture,
all analytics queries are routed thr ough a privacy
accountant that tracks the cumulative privacy
budget consumed by queries against a given
dataset. Queries that would exhaust the privacy
budget are rejected; approved queries receive
calibrated Laplace or Gaussian noise injections
that provi de formal privacy guarantees
specifically, (epsilon, delta)  differential privacy
over the query results.
The selection of privacy budget parameters
(epsilon) involves a direct engineering trade -off
between utility and privacy protection.
Advertising measurement use cases typically
require sufficient precision to distinguish
statistically significant campaign effects from
noise; epsilon values in the range of 1.0 to 4.0
have been demonstrated to provide acceptable
measurement utility while preventing i ndividual
re-identification in similar applied settings. The
DPAL implements per -use-case budget
allocation, assigning distinct budgets to
attribution reporting, reach estimation, and
frequency capping to prevent budget exhaustion
in high-volume measurement contexts.
IMPLEMENTATION CONSIDERATIONS
Latency and Throughput Impact
Latency is the dominant engineering constraint
when embedding privacy controls into the RTB
critical path. Exchanges impose bid -response
windows of 80 to 150 milliseconds depending on
inventory type, leaving no margin for privacy
checks that introduce perceptible delay. Measured
layer-by-layer, the overhead proves manageable.
The CML consent lookup, running against an in -
memory cache, contributes under 2 milliseconds
comfortably within the available budget. The
DMP's attribute generalisation step contributes 3
to 5 milliseconds, a cost that reflects per -field
evaluation against the declared attribute schema.
The PBEM's lineage evaluation contributes
approximately 1 millisecond per hop. Aggregate
overhead across all four privacy layers falls below
10 milliseconds, a target that proved achievable
without modifying the bid -request timeout
contract with exchange partners.
The CML's consent lookup, implemented against
an in-memory cache, adds less than 2 milliseconds
to the bid request critical path under normal
operating conditions. The DMP's attribute
minimisation step, applied at ingestion before the
bid evaluation path, does not add latency to
individual bid requests but increases ingestion
pipeline processing time by approximately 15 to
20 per cent depending on the complexity of the
attribute schema. The PBEM's purpose check is
implemented as a lightweight policy evaluation
against in-process policy objects, adding under 1
millisecond per access operation. The DPAL
operates entirely off the critical path, processing
analytics queries asynchronously from a pre -
aggregated summary store.
Throughput impacts are more significant at the
data ingestion layer. The DMP's feature
generalisation s tep introduces a CPU -bound
processing cost that, at hyperscale ingestion rates,
requires horizontal scaling of the ingestion tier.
Empirical profiling of prototype implementations
suggests that a 25 to 30 percent increase in
ingestion compute provisioning is required to
maintain throughput parity with a minimisation -
free baseline at representative production traffic
volumes.
Cross-Jurisdiction Deployment
Deploying a privacy -first architecture across
jurisdictions governed by different regulatory
frameworks requires careful design of the
jurisdiction detection and routing subsystem. A
data subject's applicable regulatory framework
must be determined at, or before the point of data
collection, as the requirements for consent
collection, data minimisation, and purpose

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

228 | This work is licensed under a Creative Commons Attribution 4.0 International License.

limitation differ materially between GDPR,
CCPA, and LGPD contexts.
Jurisdiction detection draws on three converging
signals: IP geolocation, the publisher's declared
user geography, and device locale indicators.
Where these signals agree, the applicable
regulatory framework is determined
straightforwardly. Where they conf lict or are
absent, a conservative fallback rule applies the
most restrictive framework among the candidates.
Jurisdictional labels travel as metadata tags
attached to each data record and consent signal, so
downstream modules can enforce the correct
policy locally without querying a central authority
for each event.
As new regulatory frameworks emerge, operators
can extend coverage by updating jurisdiction -
specific policy documents rather than pushing
code changes, a design choice that compresses the
time from a regulation's enactment to the
platform's operational compliance. The trade -off
is governance overhead: each jurisdiction requires
its own up -to-date policy document, and those
documents must be distributed atomically to every
processing node to avoid split -brain enforcement
during rollouts.
Compatibility with Industry Standards
The proposed re -architecture is designed to be
compatible with the IAB TCF as a consent signal
transport mechanism while not relying on the TCF
as the sole source of consent validity. The CML
can ingest TCF consent strings as one input
source, validate them against additional internal
criteria, and supplement or override them based
on direct consent collection where TCF -
propagated signals are insufficient for applicable
regulatory requirements.
Compatibility with OpenRTB bid request
schemas is maintained by implementing the DMP
as a pre-processing filter that modifies bid request
attributes before they are presented to the bidding
logic, rather than modifying the OpenRTB
schema itself. This approach preserves
interoperability with standard demand -side
platform integrations while ensuring that
minimised data is what flows through the system.

Table 4: Phased Migration Roadmap: Legacy to Privacy-First Architecture
Phase Component Description Compliance Achieved Performance
Impact
Estimated
Complexity
Phase
1
Consent
Signal
Routing
Layer
Instrument
auction entry
point to ingest and
propagate
TCF/GPP consent
signals as pipeline
attributes; build
pre-computed
consent state
cache; retire post -
hoc middleware
filter
GDPR Arts. 6 -7; CCPA opt -
out; LGPD Art. 7 lawful basis
enforcement
Net latency
reduction of
~5 ms vs.
legacy
middleware;
cache hit rate
target >=
95%
Medium:
requires
pipeline
instrumentation
and cache
infrastructure;
no data store
changes
Phase
2
Jurisdiction-
Aware Data
Residency
Partition user data
stores by region
(EU, US,
LATAM, APAC);
implement
geographic
routing at load
balancer; gate
cross-border
transfers via SCC
verification
service
GDPR Chapter V; LGPD
international transfer; PDPA
cross-border provisions
Additional 5 -
10 ms for
cross-region
requests;
mitigated by
regional edge
caches
High: data
migration, store
partitioning,
and routing
infrastructure
changes
required

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

229 | This work is licensed under a Creative Commons Attribution 4.0 International License.

Phase Component Description Compliance Achieved Performance
Impact
Estimated
Complexity
Phase
3
Reduced
Feature
Schema
Audit and retire
cross-site
behavioural
features; replace
third-party
syndicated
features with first-
party signals and
Topics API
segments; apply
pseudonymisation
to all retained
identifiers
GDPR Arts. 5(1)(b)(c)(e)
purpose/minimisation/storage
limitation; CCPA sensitive
PI; LGPD Art. 18
Bid
prediction
accuracy
reduction
estimated 8 -
15%;
partially
offset by
first-party
data
enrichment
over 6 -12
months
High: model
retraining,
feature pipeline
refactoring, and
first-party data
acquisition
required
Phase
4
Privacy
Sandbox
Integration
and
Continuous
Compliance
Integrate
Protected
Audience API for
retargeting;
Attribution
Reporting API for
measurement;
deploy regulatory
rule engine for
ongoing multi -
jurisdictional
updates
Full multi -jurisdictional
coverage: GDPR,
CCPA/CPRA, LGPD, PDPA
Stable post -
migration;
Topics API
signal
coarseness is
a permanent
fidelity trade-
off
Medium: API
integration and
rule engine
maintenance;
browser API
maturity is an
external
dependency
DISCUSSION
Industry Adoption Barriers
The principal barrier to industry adoption of
privacy-first re -architecture is not technical
feasibility but commercial incentive
misalignment. Advertising platforms derive
revenue from the richness of behavioural signals
available to bidders; data minimis ation reduces
signal richness and, in the short term, bid prices
and publisher revenues. This dynamic creates a
first-mover disadvantage that discourages
unilateral adoption of stronger privacy controls in
the absence of regulatory enforcement pressure.
The regulatory enforcement actions of recent
years have begun to shift this calculus. Fines of
significant scale, combined with class -action
litigation in multiple jurisdictions and growing
consumer awareness of tracking practices, have
elevated privacy compliance from a cost centre to
a risk management priority. Platforms that
integrate privacy controls at the infrastructure
level are more resilient to regulatory change and
can adapt a t substantially lower incremental cost
than those relying on surface -level compliance
overlays.
Research by Acquisti et al. (2015) established that
privacy preferences shift with context and are
highly sensitive to how choices are presented  a
point with direct commercial implications.
Platforms that build consent flows around genuine
user control rather than dark patterns may earn
measurably higher trust, which in turn supports
user engagement and partially offsets the signal
loss that comes with stricter data minimisation.
That hypothesis has not been tested at production
advertising scale, but it is directionally consistent
with emerging evidence from platforms that have
shipped privacy -enhancing features and tracked
user responses.
Regulatory Enforcement Trends
Enforcement intensity has risen sharply since
2020. GDPR, CCPA, and LGPD have operated
simultaneously, and supervisory authorities in
Ireland, France, Belgium, and Germany have
pursued significant actions against advertising -
sector operators. The cumulativ e financial

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

230 | This work is licensed under a Creative Commons Attribution 4.0 International License.

exposure created by this enforcement
environment means that structural non -
compliance no longer represents a manageable
regulatory risk, it represents a material business
liability. Veale and Zuiderveen Borgesius (2022)
reached a pointed conclusion from this trajectory:
the RTB ecosystem as it currently operates cannot
be brought into compliance through incremental
patches; its underlying architecture must change.
The direction of regulatory travel points toward a
more demanding com pliance environment, not a
more permissive one. Proposals under
development across multiple jurisdictions would
impose tighter constraints on automated decision-
making, narrow the permitted uses of sensitive
personal data categories, and extend existing data-
protection principles to data brokerage markets
that currently operate with limited oversight.
Platforms that defer architectural investment until
each new requirement is finalised will face
recurring retrofit costs; those that build to the
privacy-first model now acquire a compliance
posture that absorbs future requirements with
incremental rather than wholesale change.
The Privacy-Utility Trade-Off
The framing of privacy and advertising utility as
fundamentally opposed has dominated industry
discourse, but this framing is increasingly
contested. The advertising industry's heavy
dependence on cross -site behavioural tracking is
in part a consequence of the historical absence of
privacy constraints rather than a technical
necessity; measurement methodologi es based on
aggregated, differentially private statistics have
been demonstrated to provide actionable
campaign insights without individual -level data
access.
Cate and Mayer -Schönberger (2013) argued that
the notice-and-choice paradigm is inadequate as a
governance framework for big -data processing
environments, advocating for accountability -
based approaches in which data controllers
demonstrate compliance throu gh technical and
organisational measures rather than individual
consent transactions. The architecture proposed in
this paper embodies this accountability -based
model: privacy controls are implemented as
auditable infrastructure properties rather than
user-facing policy statements.
CONCLUSION
This paper has presented a privacy -first re -
architecture for high -scale real -time bidding
platforms, motivated by the structural
incompatibility between legacy advertising stack
designs and the requirements of the GDPR,
CCPA, and LGPD. The proposed archite cture
introduces four functional layers ; a Consent
Management Layer, a Data Minimisation
Pipeline, a Purpose -Binding Enforcement
Module, and a Differentially Private Analytics
Layer that collectively implement privacy -by-
design principles at the infrastructure level.
The empirical record is unambiguous: exist ing
compliance approaches are failing at scale. Fewer
than one in eight consent banners meets every
applicable GDPR requirement (Utz et al., 2019);
more than half of TCF-registered websites breach
at least one regulatory obligation (Matte et al.,
2020) and browser fingerprinting achieves re -
identification accuracy above 90% (Laperdrix et
al., 2020) , all without triggering any consent
dialogue. These figures are not isolated
anomalies. They describe the systemic outcome of
an industry that has treated privacy compliance as
a surface-level certification problem rather than a
structural engineering challenge. The architecture
proposed here addresses the root cause: it embeds
consent verification, attribute minimisation,
purpose binding, and privacy-preserving analytics
as non -negotiable infrastructure layers, not
retrofitted controls.
This work has several limitations. The regulatory
scope of this analysis centres on GDPR and
CCPA; treatment of LGPD and other emerging
frameworks is indicative rather than exhaustive.
The performance estimates for latency and
throughput impact are based o n prototype
implementations and require validation at
production scale. The privacy budget parameters
proposed for the DPAL represent informed

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

231 | This work is licensed under a Creative Commons Attribution 4.0 International License.

engineering judgements rather than empirically
optimised values for specific advertising
measurement use cases.
Future work should address three areas. First,
empirical evaluation of the proposed architecture
at production-scale traffic volumes is necessary to
validate performance estimates and identify
implementation bottlenecks. Second, formal
verification of the purpose-binding enforcement
module's correctness properties would strengthen
the regulatory defensibility of the architecture.
Third, the development of standardised metrics
for quantifying privacy -utility trade -offs in
advertising measurement contexts would enable
more rigorous comparison of alternative privacy-
preserving measurement methodologies. Given
the accelerating expansion of data protection
regulation worldwide, embe dding privacy
controls at the infrastructure level has shifted from
a discretionary investment to a strategic
imperative, one that yields durable competitive
positioning for platforms that commit to genuine
architectural transformation.
REFERENCES
[1] Voigt, P., & von dem Bussche, A. (2017). The
EU General Data Protection Regulation
(GDPR): A practical guide. Springer.
https://doi.org/10.1007/978-3-319-57959-7
[2] Tankard, C. (2016). What the GDPR means for
businesses. Network Security, 2016(6), 5 -8.
https://doi.org/10.1016/S1353-
4858(16)30056-3
[3] Tene, O., & Polonetsky, J. (2012). Privacy in
the age of big data: A time for big decisions.
Stanford Law Review Online, 64, 63 -69.
https://www.stanfordlawreview.org/online/pr
ivacy-paradox/big-data/
[4] Acquisti, A., Brandimarte, L., & Loewenstein,
G. (2015). Privacy and human behavior in the
age of information. Science, 347(6221), 509-
514. https://doi.org/10.1126/science.aaa1465
[5] Cate, F. H., & Mayer-Schonberger, V. (2013).
Notice and consent in a world of big data.
International Data Privacy Law, 3(2), 67 -73.
https://doi.org/10.1093/idpl/ipt005
[6] Andreou, A., Venkatadri, G., Goga, O.,
Gummadi, K. P., Loiseau, P., & Mislove, A.
(2018). Investigating ad transparency
mechanisms in social media: A case study of
Facebook's explanations. In Proceedings of
the 25th Annual Network and Distributed
System Security Symposium (NDSS).
https://doi.org/10.14722/ndss.2018.23049
[7] Veale, M., & Zuiderveen Borgesius, F. (2022).
Adtech and real-time bidding under European
data protection law. German Law Journal,
23(2), 226 -256.
https://doi.org/10.1017/glj.2022.14
[8] Sanchez-Rola, I., Dell'Amico, M., Kotzias, P.,
Balzarotti, D., Bilge, L., Vervier, P. -A., &
Santos, I. (2019). Can I opt out yet? GDPR
and the global sp read of cookie notice laws.
In Proceedings of the 2019 ACM Asia
Conference on Computer and
Communications Security (pp. 340 -351).
https://doi.org/10.1145/3321705.3329806
[9] Englehardt, S., & Narayanan, A. (2016).
Online tracking: A 1 -million-site
measurement and analysis. In Proceedings of
the 2016 ACM SIGSAC Conference on
Computer and Communications Security (pp.
1388- 1401). https://doi.org/10.1145/297674
9.2978313
[10] Degeling, M., Utz, C., Lentzsch, C.,
Hosseini, H., Schaub, F., & Holz, T. (2019).
We value your privacy... now take some
cookies: Measuring the GDPR's impact on
web privacy. In Proceedings of the 26th
Annual Network and Distributed System
Security Symposium (NDSS).
https://doi.org/10.14722/ndss.2019.23378
[11] Utz, C., Degeling, M., Fahl, S., Schaub, F., &
Holz, T. (2019). (Un)informed consent:
Studying GDPR consent notices in the field.
In Proceedings of the 2019 ACM SIGSAC
Conference on Computer and

East African Journal of Information Technology, Volume 9, Issue 2, 2026
Article DOI: https://doi.org/10.37284/eajit.9.2.5699

232 | This work is licensed under a Creative Commons Attribution 4.0 International License.

Communications Security (pp. 973 -990).
https://doi.org/10.1145/3319535.3354212
[12] Nouwens, M., Liccardi, I., Veale, M., Karger,
D., & Kagal, L. (2020). Dark patterns after the
GDPR: Scraping consent pop -ups and
demonstrating their influence. In Proceedings
of the 2020 CHI Conference on Human
Factors in Computing Systems (pp. 1 -13).
https://doi.org/10.1145/3313831.3376321
[13] Matte, C., Bielova, N., & Santos, C. (2020).
Do cookie banners respect my choice?
Measuring legal compliance of banners from
IAB Europe's Transparency and Consent
Framework. In Proceedings of the 2020 IEEE
Symposium on Security and Privacy (pp. 791-
809). https://doi.org/10.1109/SP40000.2020.
00076
[14] Srinivasan, S., Gebhart, G., & Eckersley, P.
(2019). Dark patterns and the legal
requirements of consent banners: An
interaction criticism perspective. In
Proceedings of the 2019 CHI Conference on
Human Factors in Computing Systems.
https://doi.org/10.1145/3290605.3300432
[15] Iordanou, C., Soriente, C., Sirivianos, M., &
Laoutaris, N. (2018). Who is fiddling with
prices? Building and deploying a watchdog
service for e-commerce. In Proceedings of the
2018 ACM SIGCOMM Conference (pp. 376-
389). https://doi.org/10.1145/3230543.32305
66
[16] Zuiderveen Borgesius, F., Moller, J.,
Kruikemeier, S., O Fathaigh, R., Irion, K.,
Dobber, T., Bodo, B., & de Vreese, C. (2018).
Online political microtargeting: Promises and
threats for democracy. Utrecht Law Review,
14(1), 82-96. https://doi.org/10.18352/ulr.420
[17] Laperdrix, P., Bielova, N., Baudry, B., &
Avoine, G. (2020). Browser fingerprinting: A
survey. ACM Transactions on the Web, 14(2),
1-33. https://doi.org/10.1145/3386040
[18] Solomos, K., Ilia, P., Ioannidis, S., &
Kourtellis, N. (2020). Talon: An automated
framework for cross -device tracking
detection. In Proceedings of the 2020 ACM
Internet Measurement Conference (pp. 478 -
493). https://doi.org/10.1145/3419394.34236
26
[19] Grassl, P., Schraffenberger, H., Zuiderveen
Borgesius, F., & Buijzen , M. (2021). Dark
and bright patterns in cookie consent requests.
Journal of Usability Studies, 17(1), 1 -18.
https://doi.org/10.31234/osf.io/gqs5h
[20] Fouad, I., Bielova, N., Legout, A., &
Sarafijanovic-Djukic, N. (2020). Missed by
filter lists: Detecting unknown third -party
trackers with invisible pixels. Proceedings on
Privacy Enhancing Technologies, 2020(2),
499-518. https://doi.org/10.2478/popets-
2020-0038
