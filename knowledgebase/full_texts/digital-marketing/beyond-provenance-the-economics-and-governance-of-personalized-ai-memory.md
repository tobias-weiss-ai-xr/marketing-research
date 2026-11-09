---
title: 'Beyond Provenance: The Economics and Governance of Personalized AI Memory'
url: https://arxiv.org/abs/2609.25521
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Jianan Chen
- Yufei Qin
- Yaosen Lin
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.25521
pages: 27
chars: 148296
fetched_at: '2026-11-08T13:20:03+00:00'
kb_version: 1
---

# Beyond Provenance: The Economics and Governance of Personalized AI Memory

Beyond Provenance: The Economics and
Governance of Personalized AI Memory
Jianan Chen
Purdue University
West Lafayette, IN, USA
chen3873@purdue.edu
Yufei Qin
Princeton University
Princeton, NJ, USA
yq9378@princeton.edu
Yaosen Lin
University of California San Diego
La Jolla, CA, USA
yal003@ucsd.edu
Abstract—Personalized AI memories, defined as persistent
decision-relevant states distilled by platforms from long-run
human–AI interaction, are increasingly portable, provenance-
certifiable, and tradable. Provenance answers the question of
origin, but it does not settle who holds which rights over a
memory, nor how wider deployment affects its future supply. We
develop a unified model in which memory use is non-rival, while
refresh, the maintenance of continued validity, is relationally
co-produced by the represented individual and the platform.
Even assuming perfect provenance and complete information, the
model still yields a set of inherent limitations. First, there is an
extraction ceiling: decision value is bounded by lived experience.
Second, a rights-separation theorem shows that no budget-
balanced ownership assignment can make both co-producers
residual claimants, and that control rights and cash-flow rights
operate on distinct margins. Third, a depletion result indicates
that reach-expanding policies such as portability, interoperability,
and competition raise current access but shrink the long-run
memory stock. Fourth, we offer a formal comparison between
memory ownership as it ought to be (subject-held) and as it is
(platform-held); the welfare ranking reduces to two measurable
quantities, both dominated by interior renewable-claim bundles.
Finally, endogenous-quality and market-formation results show
that uncompensated markets pollute their own raw material,
that transparency and compensation are complements, and that
the de facto platform-ownership regime is self-perpetuating. On
the design side, the analysis points to separated provenance,
performance, and permission credentials; compensation indexed
to quality-deployment; and portability and salience, rather than
nominal ownership, as the binding policy margins.
Index Terms—AI agents; personalized memory; markets for
information; data governance; property rights; consent; certifi-
cation.
I. INTRODUCTION
Personalized AI memory is shifting from a product fea-
ture to a persistent asset. Technical work has increasingly
converged on agent architectures that accumulate, consolidate,
and retrieve long-term memory across sessions [1], [2], with
recent surveys organizing the literature by memory forms,
functional roles, and write/read dynamics [2]. One vision
paper argues that the resulting artifacts should be managed
as human-centric assets rather than as agent-side state [3].
Marketplace infrastructure already exists: recent work binds
a memory artifact to verifiable computational provenance and
adds a marketplace layer for listing, transferring, and govern-
ing certified artifacts, where certification attests to authenticity,
effort-backed production, and compatibility with the execution
context [4]. Parallel efforts specify portability protocols for
moving memory across heterogeneous agents [5]. Meanwhile,
legal scholarship has begun to ask who owns a simulated
identity built from a person’s data [6].
What makes this class of memory economically distinctive
is not that the data pertains to a person, but what a buyer
actually obtains. Purchasing a single fact saves one lookup;
purchasing a representation of how a person weighs tradeoffs
alters multiple future decisions at once. This concentration of
decision relevance is both the source of value and the locus
of exposure.
The urgency is not speculative. Regulators have already
demonstrated the cost of improvised governance over asset
classes derived from people. In the 23andMe bankruptcy,
deletion rights and oversight for genetic data sourced from
millions of individuals were negotiated by a coalition of state
attorneys general only after the asset had entered the estate.
Personalized memory follows the same trajectory, with two
features that complicate governance: it is continuously re-
created rather than collected once, and the person it describes
continues to produce it.
The puzzle is that verified effort is not economic value.
Provenance answers where a memory came from, but it does
not answer whether the artifact faithfully represents its subject,
whether it suits the buyer’s task and host model, whether its
extraction and sale were authorized, or whether its accuracy
harms the person it describes. The point is sharper than a
general call for more metadata: the strongest certification
currently proposed attests that an artifact iseffort-backed
[4], yet verified production effort is precisely what does not
imply decision value. A memory may be authentically and
expensively produced from a real interaction history and still
be worthless to a buyer; conversely, it may be highly valuable
to a buyer while imposing uncompensated exposure on its
subject.
Behind this observation lies a public debate that structures
our inquiry. One side holds that memoryoughtto belong to the
person it represents; the legal case for treating an AI twin as its
subject’s property rests on the classical criteria of ownership:a
defined asset, exclusive control, and demonstrable value [6].
The other side counters that memoryisheld by the platforms
that extract it, because subjects generally lack the technical and
behavioral means to retain it. The debate is typically framed
arXiv:2609.25521v1  [cs.GT]  22 Sep 2026

as a choice between these two answers. We show that they
are, in fact, two poles of a single institutional space, each
undermining distinct dimensions of the asset’s production, and
that the efficient arrangement is neither.
We model a persistent, decision-relevant state whose con-
tinued validity is co-produced by a natural person’s feedback
and a platform’s engineering investment, and which can be
redeployed at negligible copying cost. To isolate the structural
implications, we grant the marketplace every condition its
builders aim to secure: provenance isperfectand information
iscomplete. Consequently, all failures derived below persist
even under perfectly functioning infrastructure and cannot
be dismissed as artifacts of imperfect verification or user
confusion.
The paper rests on a single core mechanism:use can be
non-rival, while refresh is relationally supplied.Copying a
memory costs nothing and consumes no resources. Maintain-
ing its truth, however, is costly: it requires continuing input
from the person it describes, who bears exposure from every
deployment and whose incentive to keep supplying that input
is precisely what the rights bundle determines. The asset is a
non-rival good with a rival maintenance technology, and nearly
every result follows from taking that combination seriously.
The paper yields four main contributions.
•Conceptual.We build on existing technical taxonomies of
memory rather than proposing new ones, and supplement
them with the economic dimensions that any market
mechanism must accommodate: use-indexed fidelity, de-
ployment specificity, person linkage, an entanglement
index, and rights treated as a designable institution rather
than as a definitional premise (Section III).
•Theoretical.Five results, all obtained under perfect prove-
nance and complete information. First, anextraction
ceilingbounds decision value by the lived interaction
history, with equality only when extraction is a sufficient
statistic (Proposition 1); hence the supply of high-fidelity
memory is ultimately constrained by experience that
someone must live. Second, arights-separation theorem
shows that no budget-balanced assignment of cash-flow
rights renders both co-producers residual claimants, so
neither individual nor platform ownership implements
first-best refresh; moreover, control rights and cash-flow
rights operate on distinct margins and cannot substitute
for each other (Theorem 1). Third, adepletion result
establishes that policies widening reach, namely portabil-
ity, interoperability, and competition, raise current access
but shrink next-period new memory and the long-run
stock (Theorem 2); nonrivalry of copying therefore does
not imply monotone welfare gains from broader deploy-
ment. Fourth, anought–is resolutionshows that subject
ownership and platform ownership are twin corners of
the rights space, each extinguishing one supply margin
because the non-owning party supplies no refresh; their
welfare ranking reduces to two measurable quantities:
exposure intensity and the ratio of subject to platform
refresh productivity, and both corners are dominated by
interior bundles (Proposition 4). The corner observed in
practice is moreover self-perpetuating, as the platform’s
equilibrium play sustains precisely the low portability and
low salience that make subject control infeasible. Fifth, a
•Computational.We construct a synthetic memory econ-
omy in which every estimand has a known ground truth,
enabling validation of the paper’s estimators at an interior
operating point rather than merely proposing them in
the abstract (Section VIII). In practice, the computa-
tional exercise amended rather than merely illustrated
the theory. The Gaussian entanglement frontier turned
out to be an information-saturation limit rather than a
separate identity; the second-best scope haircut exists
only where the subject’s refresh margin is live; and the
productivity ratio underlying the coverage prescription is
systematically attenuated by measurement in high-fidelity
systems.
•Institutional.A failure-instrument matrix in which each
row carries a theorem pointer, together with a design
rule for which the model supplies three independent
reasons: provenance, performance, and permission cre-
dentials must remain separate rather than fused into a
single composite score (Section VII).
•Computational.A synthetic memory economy in which
every estimand has a known ground truth, so that the
paper’s estimators can be validated at an interior oper-
ating point rather than merely proposed (Section VIII).
It amended the theory rather than illustrating it. The
Gaussian entanglement frontier turned out to be an
information-saturation limit rather than an identity, the
second-best scope haircut exists only where the subject’s
refresh margin is live, and the productivity ratio behind
the coverage prescription is systematically attenuated by
measurement in high-fidelity systems.
The rest of the paper proceeds as follows. Section II surveys
the relevant literatures by the module each supplies. Section III
presents the model; Section IV establishes the main results;
Section V endogenizes fidelity and participation; Section VI
solves for the optimal rights bundle; Section VII translates the
results into institutional instruments; Section VIII measures,
calibrates, and tests them; Section IX discusses the limits;
Section X concludes.
II. RELATEDWORK
We organize related work by the module each literature
supplies to our model, and indicate where extrapolation from
that work stops. Since our object lies at the intersection of
several literatures that rarely interact, the point of this section
is less to survey than to identify which piece of machinery
comes from where, and which question none has yet posed.
Onagent memory: architectures and taxonomies, cognitive-
architecture work distinguishes working from long-term mem-
ory and subdivides the latter into episodic, semantic, and
procedural forms [1]; recent surveys organize the field by three
joint lenses:forms(token-level, parametric, latent),functions

(factual, experiential, working), anddynamics(formation, evo-
lution, and retrieval) [2]. These provide our object’s coor-
dinates, and we adopt their boundaries: externally persisted,
cross-session state, distinct from model weights, from a static
retrieval corpus, and from transient context. Within those
coordinates, our focal object occupies a single cell: it is cross-
session and interaction-inferred in origin, externally persisted
in separable form, semantic-preference or procedural-policy
in function, and continuously consolidated and retrieved for
future action. “Preference/policy memory” is our economic
label for that cell, not a proposed cognitive category; the
personalized-agent literature supplies the existence proof that
memory of this kind steers real actions taken on a user’s behalf
[7]. We take these architectures as given and do not propose
new ones. What this body of work does not attempt, and what
we do, is the market and governance analysis of the artifacts
it produces.
Onmemory as an asset and verifiable marketplaces, two
strands supply the phenomenon we study. The first argues for
moving from agent-centric to human-centric memory manage-
ment and treats memory as an asset with a subject [3]. It
supplies the asset vision and the object, but it does not model
price formation, private information, equilibrium, or welfare,
and its single-owner framing sits uneasily with co-production;
we therefore treat ownership as an outcome to be derived
rather than a premise to be assumed. The second supplies
working infrastructure: provenance binding, a marketplace
layer for listing, transferring, and governing certified artifacts,
where certification attests to authenticity, effort-backed pro-
duction, and compatibility with the execution context [4],
alongside companion protocols for verified transfer across
heterogeneous agents [5]. We retain their modules (lineage
attestation, compatibility classes, and credential separation)
and our identification strategy goes further by treating their
engineering asperfectly successful. The gap we exploit is
that their certification targets production effort; much of what
follows argues why verified effort and decision value diverge
even when verification works perfectly. Portability work is
more than adjacent: the parameter our model uses to represent
exit is precisely what such protocols would move, and one of
our results explains why no incumbent supplies it voluntarily.
Onownership of a simulated identity, the normative pole of
our organizing question has been argued directly: individuals
should hold moral and legal ownership of the AI twins
built from their data, on a human-centric property framework
requiring a defined asset, exclusive control, and demonstrable
value, with an accompanying policy program of private-by-
default governance and portability standards [6]. That analysis
is legal and conceptual, and offers no price formation or
welfare analysis; that is where we begin. Our engagement with
it is two-sided and, we believe, favorable to that literature on
the point that matters most. On one hand, we find that subject
ownership, even taken literally, is itself only second best: it
internalizes exposure fully but monopolizes deployment and
extinguishes the platform’s engineering margin, in exactly the
way that platform ownership extinguishes the subject’s refresh
margin. The normative target, accordingly, is a claim structure
rather than an owner. On the other hand, that literature’s
portabilityprescription is vindicated by our model, but for
a reason its own framework does not supply: portability and
salience, rather than the name on the title, turn out to be
the binding margins, and no equilibrium actor provides them.
Reform that reassigns ownership while leaving those two
conditions in place changes neither the scale of deployment
nor the flow of refresh.
Indata economics, nonrivalry and the welfare stakes of
data control are the foundation we build on [8], and the
externalities that one person’s transaction imposes on others
provide the machinery behind our market-formation results
[9]. Two departures matter. First, we separate thesubject
from theseller; the person described need not be the party
selling, and that separation is the wedge our rights results
exploit. Second, against the thin-market presumption that the
data literature usually carries, we find that identity-entangled
memory markets tend to over-thicken at scale, not uncondi-
tionally, but because the positive thickness externality saturates
while relational leakage does not, and because correlation is
strongest precisely among similar individuals. Nonrivalry of
copying is where our object starts rather than where it ends,
because the maintenance technology is rival even when use is
not.
Fromproperty rights and team incentives, our central rights
result builds on two classic frameworks from the property-
rights and team-incentives literature: team moral hazard with
budget balance [10] and the property-rights approach to non-
contractible investment [11]. The memory-specific content fills
the roles as follows: the two investors are a natural person
and a platform; the investments are lived experience and en-
gineering, respectively; and the asset itself is a representation
of one of the investors. That last feature has no analogue in
the classical setting, and it is precisely what gives exposure
its negative sign in the subject’s stake. As a consequence,
expanding deployment drives the two margins in opposite
directions.
Frominformation, certification, and disclosure, we draw on
three strands: hidden quality [12], the incentive of a monopoly
certifier to coarsen its reports [13], and the disclosure-versus-
expropriation trade-off in selling ideas [14], [15]. A lemons
application to memory would be true without being memory-
specific, and our main results concern distortions that survive
symmetric information entirely. The one place this literature
becomes load-bearing is certification, where the certifier’s
proper economic role is not to substitute for the subject’s
consent but to render fidelity contractible, thereby indexing
compensation to measured quality.
Finally, amongadjacent asset classes, we draw three ref-
erence points: software economics for copying, versioning,
and licensing; trade secrecy for value-through-exclusivity; and
reputation theory supplies a living, transferable asset whose
top holders rationally under-maintain [16], [17]. The last of
these is the closest existing analogue to our refresh margin, and
it is also why freshness recertification outperforms a one-time

badge. Prompt markets are the nearest neighbour, but serve
as a boundary rather than a template: a prompt is a control
input whose value need not be a function of history, whereas
memory is by construction a statistic of realized interaction.
None of these is a synonym for personalized memory, and
none transfers wholesale. What is new is endogenous, persis-
tent, person-linkedstatethat its subject continues to produce.
III. MODEL
A. Problem statement and focal object
We do not ask what a memory file is worth, nor do we com-
press the research question into “should the individual or the
platform own the memory.” We ask: for a persistent decision-
relevant state whosecontinued validityis co-produced by a
natural person’s feedback and a platform’s engineering invest-
ment, and which can be redeployed at negligible copying cost:
how should deployment rights, cash-flow rights, update rights,
and exit rights be configured, and how do these configurations
change the formation, the traded scale, and the long-run stock
of memory?
The model contains two independent wedges and one
aggregation bridge: (i) arefresh-incentive wedge, because
future quality is co-produced but neither party’s input is fully
contractible; (ii) adeployment wedge, because digital states
are reusable, but each deployment creates buyer value while
imposing use-specific exposure on the represented person; and
(iii) areach bridge, because market thickness enters only by
expanding license reach, transmitting the deployment wedge
into refresh and long-run stock. The paper’s master mechanism
is thatuse can be non-rival, while refresh is relationally
supplied.
The subjecti’s latent preference/decision rule at timetis
πit(a|x)for contextsx∈ Xand actionsa∈ A; interactions
generate a historyH it; a platform’s extraction technology
forms the states it =E h(Hit), which a hosthloads through a
behavioral kernelK h(a|x, s it). The focal class is externally
persisted, cross-session,identity-entangledpreference/policy
memory used to predict or act on behalf of a specific natural
person.
a) Scope.:Most of what this paper excludes is excluded
by Definition 2 rather than by separate stipulation, which is
one reason to state the object formally.Persistenceexcludes
transient working memory and in-context state;Separability
excludes parametric memory inseparable from model weights,
and is therefore also the technical precondition for any of this
to be tradable at all;Person linkageL i(m)>0excludes
pure public facts, which have subjects only in a trivial sense.
Two further exclusions are deliberate rather than implied. Raw
interaction archives that cannot be meaningfully separated into
artifacts are outside the unit of trade of Definition 7. Mem-
ory describing two or more subjects raises an authorization
problem that one person’s consent cannot solve; Theorem 4
supplies the machinery for its externality, but the full rights al-
location is companion-paper scope. None of these is excluded
as unimportant.
b) Reader’s map.:Section III-B defines the objects;
Sections III-C–III-D state assumptions and the economic envi-
ronment; Section III-E characterizes the refresh subgame used
throughout. Section IV develops the main results; Section V
endogenizes fidelity (pollution) and participation (formation);
Section VII translates the results into instruments; Section VIII
gives the measurement interface.
B. Formal definitions
Definition 1 (State decomposition):The decision-relevant
state of personiattisω it = (ω c t , ωg k(i), ωp it), whereω c is
acommoncomponent,ω g aclasscomponent fori’s compat-
ibility classk(i), andω p apersonalcomponent following
ωp it =ρ ωp i,t−1 +ε it, ε it ∼ N(0, σ2 ε ), ρ∈(0,1),(1)
with within-class cross-subject correlationCorr(ω p it, ωp jt) =
ϱ≥0.
Remark 1:One decomposition yields all four coordinates
that would otherwise be introduced separately:(ω c, ωg)gov-
ern transferable value;ω p governs personalization value and
subject exposure; the weight ofω g relative toω c is deployment
specificity;ρis staleness;ϱis the relational externality.
Definition 2 (Memory artifact):Leth t i =
(xis, pis, ais, yis)s≤t be the interaction history generating the
σ-algebraF h it. An objectm= (φ,Π, ℓ)is apersonalized
memory artifactof subjectiiff:
•(Derivation)φ=E(h t i)for anF h it-measurable extraction
operatorE: memory is a statistic of realized interaction,
which separates it from a prompt, a control inputp t
whose value need not be a function of history;
•(Persistence)φremains retrievable after the generating
episode closes (excluding working memory / transient
context);
•(Separability) there is a decoderRetsuch thatπ θ′(· |
x,Ret(φ, x))is well defined for hostsθ ′ ̸=θ(excluding
weight-inseparable parametric memory; this is the tech-
nical precondition of tradability);
•(Efficacy)∃xwithπ θ(· |x,Ret(φ, x))̸=π θ(· |
x,Ret(∅, x));
•(Person linkage)L i(m) :=I(ω p i·;φ)>0, whereI
denotes mutual information.
Π(m)is the lineage DAG recording the generative structure
(ht i,E); aprovenance credentialCert Π is a proof system about
Π;perfect provenanceis the strongest case in whichCert Π
reveals the full truth of(h t i,E).ℓis the scoped license defined
below.
Definition 3 (Use-indexed fidelity):For a useu=
(Au,L u, µu 0 )(action set, loss, prior), writeV u(·) :=
E[Lu(a∗(·), ω)]for the expected loss of the optimal action
under the stated information, withV u(µu 0 |φ)its poste-
rior counterpart, and assume the nondegeneracy condition
Vu(µu 0 )> Vu(ω)(the prior is not already first-best). Define
qu(m) := Vu(µu 0 )−V u(µu 0 |φ) Vu(µu 0 )−V u(ω) ∈[0,1],(2)

the normalized decision value ofmin useu:0= no better
than the prior,1= as good as knowingω. Fidelity is thus a
derived, measurable, use-dependentquantity, not a free scalar.
For a buyerbwith useu b we writev bm :=q ub (m)forb’s
normalized value of artifactm.
Definition 4 (Deployment specificity):For a family of
usesU ′ (across buyers, tasks, hosts),σ(m;U ′) := 1−
minu∈U ′ qu(m)/max u∈U ′ qu(m)∈[0,1].
Lemma 1 (No unconditional global quality score):If there
exist buyersb, b′ and artifactsj, kwithv bj > vbk andv b′j <
vb′k, then no buyer-independent scalar scoreS(m)ranksj, k
correctly for both buyers.
Proof:Immediate: any strict ranking byScontradicts
one buyer; equality ranks neither. With Definition 3, crossing
rankings are generic wheneverσ >0.
Corollary 1 (Staleness is derived):Under Definition 1,
for memory generated attand used att+k, the personal
component ofq u decays by the factorρ 2k (exactly, in the
Gaussian case). The depreciation rate is an implication of
preference drift, not an assumption.
Remark 2 (Bridge to the reduced form):In the law of motion
(6) below, the personal-component contribution to depreciation
isδ p = 1−ρ 2; the reduced-formδadditionally absorbs
class/common drift and technological obsolescence, and is
thereforeclass-specific and calibratable, not free.
Definition 5 (Use trichotomy and exposure):Partition uses
by their effect on subjecti:U=U self ∪ Uother ∪ Uadv
(acting fori; general lessons for others; extraction, imitation,
or discrimination againsti). Letadv :U → U adv map each
use to the adversarial decision problem sharing its sufficient
statistics (the best inference/imitation attack implementable
from what the deployment reveals). Subject exposure from
deployingmin useuis
Hi(m, u) =λi ·q adv(u)(m),(3)
i.e., harm is proportional to the decision value the deployment
hands to an adversarial decision problem, with private sensitiv-
ityλ i. That harm rises with fidelity is therefore not assumed:
it holds exactly when the buyer’s and the adversary’s decision
problems share sufficient statistics.
Definition 6 (Entanglement coefficient):Letu B be the buyer
use,u S the adversarial use, andGthe set of garblings ofφ.
Define
κ⋆(m;u B, uS) := 1− supz∈G0 quB (z(φ)) quB (φ) ∈[0,1],(4)
whereG 0 :={z∈ G:q uS (z(φ)) = 0}is the set of
zero-exposure garblings, with the conventionsup∅:= 0
(if no zero-exposure garbling exists,κ ⋆ = 1).κ ⋆ is the
share of buyer value thatcannotbe obtained without subject
exposure.κ ⋆ = 0: a zero-exposure, full-value transformation
exists (anonymization, aggregation, synthetic personas have
full purchase).κ ⋆ = 1: any positive buyer value entails
positive exposure.No privacy technology can improve the
frontier; only institutions remain.This is the formal content
of “identity-entangled memory,” a continuous and measurable
index, orthogonal toσ.
Remark 3 (Robust version):The exact-zero constraint
is knife-edge; the robust object isκ ⋆ ϵ with constraint
quS (z(φ))≤ϵ, andκ ⋆ = lim ϵ↓0 κ⋆ ϵ whenever the value of
the garbling program is continuous atϵ= 0; empirical work
should reportκ ⋆ ϵ at statedϵ.
Lemma 2 (κ ⋆ versus identity-replacement estimates):Let
ι(m) = 1−Vb(m−s)/Vb(m)be the identity-replacement coun-
terfactual (value retained after naively erasing the subject).
Thenκ ⋆(m)≤ι(m), with equality iff naive erasure is the
optimal zero-exposure garbling.
Proof:m −s is a feasible element of the constraint set
definingκ ⋆; the supremum weakly improves on it.
Remark 4:Empirical identity-replacement audits therefore
overestimateentanglement: smarter garblings may preserve
more value. Reportιas an upper-bound estimator of the
theoretical objectκ ⋆.
Definition 7 (Scoped deployment license):The
unit of trade is not “a person’s memory” but
ℓ= (m, b, u, h,[t0, t1], k,access mode,audit,revocation rule):
a grant to recipientbfor specified uses, hosts, horizon, call
budget, and audit/revocation terms. What is non-rival is the
physical occupation of the digital original by one deployment;
authorization, refresh input, compliance, inference cost, and
subject exposure are not thereby zero.
Definition 8 (Rights bundle / institution):An institution is
not an owner dummy butg= (c, α, τ, υ, ϕ, ρx, ad): deploy-
ment controlc∈ {P, S, J}; subject revenue shareα∈[0,1];
enforceable per-quality-deployment compensationτ; update
rightsυ; functional portabilityϕ∈[0,1]; revocation/recall
rulesρ x; audit probabilitya d. “Individual ownership” and
“platform ownership” are corner combinations. The core the-
orems endogenize(c, α, τ); the remaining components enter
feasible sets, outside options, or extensions.
Definition 9 (Prompt–memory boundary):A current-round
promptp t that only enters the control input is not memory
under Definition 2; ifs t+1 =Upd(s t, pt)and the state is later
retrieved, the persisted content can become a representation of
memory. The same string can play both roles; the asset object
is fixed by causal role and rights structure, not by file format.
Definition 10 (Memory stock and market thickness):With
Mt the measure of supplying subjects and ¯ψt their mean
precision contribution, the market-available precision of the
common component isΨ t = (σ2 0 + 1/(Mt ¯ψt))−1, increasing,
concave, and bounded by1/σ 2 0, whereσ 2 0 >0is common
noise that aggregation cannot remove.M t is the thickness
object entering the reach bridgen=N(M),N ′ ≥0, used in
Sections IV and V.
C. Assumptions
Assumption 1 (Perfect provenance benchmark):All logs,
model versions, and generation chains are authentic and cer-
tified:Cert Π is perfect.(Identification strategy: any failure
below is not about fabrication.)

Assumption 2 (Complete-information benchmark):Subject
and platform know uses and parameters; each buyer knows her
own type and fit.(Headline results do not rely on consumer
error or lemons.)
Assumption 3 (Joint inputs; effort noncontractibility):Re-
fresh output is co-produced by subject efforteand platform
effortx; efforts are noncontractible item-by-item, while real-
ized output is ex post verifiable [10], [11].
Assumption 4 (Functional forms):Quadratic effort costs;
installed capabilitiesη S, ηP >0; complementarityγ≥0
bounded by the stability condition of Lemma 3; buyer types
θ∼U[0,1](a normalization; general regular inverse demand
preserves signs).
Assumption 5 (Linear exposure benchmark):Per unit of
quality and per deployment, monetizable exposure isλ≥
0.(Microfoundation:λaggregates Definition 5’sλ i qadv(u)
over the served use distribution of the focal class, and
is therefore use-class-specific. The misrepresentation variant
λP f+λ M (1−f)is treated as robustness.)
Assumption 6 (Scope commitment; quasilinear TU bench-
mark):The rights bundle can be committed before refresh
efforts; utilities are quasilinear.(Monetary IR does not exhaust
consent; inalienable-use constraints enter as hard constraints,
Section VII.)
D. Environment
a) Players.:A minimal production unit: subjectS; plat-
formP; a continuum of buyers with typesθ∼U[0,1]; a
social planner as welfare benchmark.
b) Downstream demand.:A license is worthv θ(Q) =
θQto typeθ, whereQ >0is current effective quality (average
focal fit normalized in; in the language of Section III-B,Qis
the class-average use-indexed fidelityq u delivered to served
uses, scaled by the stock). Serving the topn∈[0,1]share at
a uniform price givesp(Q, n) =Q(1−n)and, per unit ofQ:
R(n) =n(1−n), C(n) = n2 2 ,
B(n) =R(n) +C(n) =n− n2 2 , (5)
extractable license revenue, buyer surplus, and gross use
value. Copying does not consumeQ, but the subject bears
H(Q, n) =λQn.
c) Refresh technology.:The effective stock evolves as
Qt+1 = (1−δ)Q t +Y(e t, xt), δ∈(0,1],(6)
Y(e, x) =ηSe+η P x+γex,
KS(e) = cS e2 2 , K P (x) = cP x2 2 . (7)
Installed capabilitiesη S, ηP >0rule out the zero-effort co-
ordination equilibrium that an essential-inputs Cobb–Douglas
would admit unconditionally;γ= 0is the conservative
additive benchmark in which all headline results already hold.
d) Stakes.:With private per-quality flowsu S, uP ≥0
and rights(α, τ), the capitalized marginal stakes in a unit of
refresh are
wS(n) =u S +αR(n) + (τ−λ)n,(8)
wP (n) =u P + (1−α)R(n)−τ n,(9)
T(n) =w S +w P =u S +u P +R(n)−λn,
Ω(n) =u S +u P +B(n)−λn=T(n) +C(n).(10)
Prices, revenue shares, andτare internal transfers and do
not enterΩtwice; buyer surplusC(n)is the part no private
rights bundle automatically captures. (Fines paid to third
parties reducew P without raisingw S: a separate liability
wedge, not conflated withτ.) A common capitalization factor
Γ(β, δ) =β/(1−β(1−δ))is normalized to one under sta-
tionarity; restoring it rescales all flow terms without changing
the comparisons below. Effort-stage payoffs and incremental
welfare are
πS =w SY− cS e2 2 +F, π P =w P Y− cP x2 2 −F,
W= ΩY− cS e2 2 − cP x2 2 , (11)
with fixed transferFallocating rents but not marginal incen-
tives.
e) Timing.:(1) institutiongandF; (2) scope com-
mitmentnby the controller named inc; (3) simultaneous
noncontractible(e, x); (4) realization and verification ofY
(lineage perfect; fidelity auditable on pre-registered tasks);
(5) licensing atp(Q, n); (6) deployment, payments, exposure;
(7) transition by (6). Equilibrium: subgame perfection under
rational expectations; bounded attention only in the robustness
section.
f) Participation.:Buyer IR holds ex post iffθ≥1−n.
Subject and platform IR,Π S ≥ ¯US,Π P ≥ ¯UP , can be met
byFwhenever joint surplus suffices, butFcannot repair
the slopes of (8)–(9). Inalienable uses impose the stronger
constraintℓ∈ Ri(m), which monetary IR does not replace.
E. The refresh subgame
LetA S =w S/cS,A P =w P /cP ,∆ γ = 1−γ 2ASAP .
Lemma 3 (Unique active refresh equilibrium):Ifw S >0,
wP >0,∆ γ >0, the effort subgame has a unique strictly
positive Nash equilibrium
eE = AS(ηS +γA P ηP ) ∆γ , x E = AP (ηP +γA SηS) ∆γ ;
in the additive benchmarkγ= 0,
eE = ηSwS
cS
, x E = ηP wP
cP
,
Y E =k SwS +k P wP , k S := η2 S cS , k P := η2 P cP . (12)
Ifw j ≤0, participantjcorners at zero; interior derivatives
are used only on the active region. The planner’s problem
replaces both stakes byΩand requires1−γ 2Ω2/(cScP )>0
for a unique interior first best.
kS andk P , theinstalled refresh productivitiesof subject
feedback and platform engineering, are the two empirical

primitives on which every institutional comparison below
turns.
F . Where each object binds
No object above is defined for its own sake; each is
consumed at a named point downstream. Definition 1’sϱ
is the relational externality driving over-participation in Sec-
tion V (formation);ρdelivers Corollary 1 and calibratesδ
(Remark 2). Definition 2’sSeparabilityand Definition 8’s
portabilityϕare theobjective feasibility conditionsfor subject
control compared in Section IV-E: the formal content of
“whether users can in fact own their memory.” Definition 3
and Lemma 1 rule out scalar quality scores and power the
evaluation design of Sections VI-F and VIII. Definitions 5–
6 microfound the reduced-formλ(Assumption 5) and bound
what privacy technology can substitute for institutions (κ ⋆,
tested in Section VIII). Definition 7 fixes the priced unit in
Section IV’s licensing stage. Definition 8 is the space in which
Sections IV-B and IV-E locate thede factoandnormative
corner institutions and Corollary 3 locates the interior opti-
mum. Definition 9 guards the paper’s boundary against prompt
markets. Definition 10 supplies the thickness objectMwhose
reach bridgen=N(M)closes the loop from Section V back
into Theorem 2.
IV. MAINRESULTS: NON-RIVALUSE, RELATIONALLY
SUPPLIEDREFRESH
This section develops the model’s results in three layers,
organized by a question the paper keeps distinct from the
model itself: memory ownershipas it ought to be, held by
the person the memory represents, versusas it is, held by
platforms under current technical and behavioral conditions.
Definition 8 makes both expressible as corner institutions in
one bundle space, so their comparison is a theorem, not a
stance. Section IV-A bounds what any extraction technology
can deliver. Section IV-B freezes the stock and isolates the
deployment wedge: who controls scope matters, and the direc-
tion of the platform’s distortion reverses in the exposure inten-
sity, which recovers, as a special case, the distortion-reversal
regimes of the static monopoly model. Sections IV-C–IV-D
open therefresh-incentive wedge: no rights bundle makes both
co-producers residual claimants, and because the represented
person remains an endogenous supplier of refresh, broader
deployment can raise current access while shrinking the long-
run stock: the paper’s headline. Section IV-E then confronts
the two ownership corners directly: each destroys the other
party’s supply margin, their welfare ranking reduces to two
measurable quantities, andneitheris the normative target.
A. The extraction ceiling
Proposition 1 (Extraction ceiling):Under Definition 2
(Derivation),φ=E(h t)withEmeasurable with respect to
F h t , soω→h t →φis a Markov chain. Hence for every use
u,q u(φ)≤q u(ht), with equality iffφis a sufficient statistic of
ht foru. No extraction technology, however sophisticated, can
deliver more decision value than the lived interaction history
contains.
Proof:Data-processing: any decision rule based onφis
a garbling of one based onh t; Blackwell’s theorem orders the
normalized values in Definition 3.
Remark 5:Two consequences follow. (i) Supply of high-
fidelity memory is ultimately bounded byexperience, which
must be lived by someone: this is the microfoundation for
the depletion logic of Theorem 2. (ii) Claims that extraction
quality can substitute indefinitely for interaction quality are
falsified within the model. The result is elementary as math-
ematics; its role is to fix the direction of scarcity before any
institutional question is asked.
B. The static deployment wedge: scope control and distortion
reversal
Freeze the stock atQ >0(no refresh margin) and let the
controller named incchoose reachnafter(α, τ)are set. This
diagnostic benchmark isolates what deployment controlalone
does; every force in it survives into the dynamic model, where
it is joined by the refresh margin.
Proposition 2 (Scope divergence):In the fixed-stock bench-
mark, the platform-controlled, subject-controlled, and welfare-
maximizing scopes are
nP =
h
1−τ /(1−α)
2
i
[0,1]
, n S =
h
1−(λ−τ)/α
2
i
[0,1]
,
nW = [1−λ] [0,1],
(13)
maximizing(1−α)R(n)−τ n,αR(n)+(τ−λ)n, andB(n)−
λnrespectively. In theτ= 0,0< α <1special case,n P = 1 2
independently of bothαandλ: revenue shares do not move the
platform’s scope, and the platform’s scope does not respond
to exposure. (Forτ̸= 0,n P does vary withα.)
Corollary 2 (Distortion reversal, unified-model version):Set
α=τ= 0,u S =u P = 0(pure platform control, thede facto
cornerg P of Section IV-E). Thenw P (n)−Ω(n) = n(2λ−n) 2 ,
so at any scope the platform’s marginal refresh stake exceeds
the social stake iffλ > n/2; andnP = 1 2 versusn W = 1−λ.
Hence three regimes:
•Low exposure(λ < 1 4): the platform under-deploys and
its investment stake falls short of the social stake, the
classic monopoly shortfall on both margins;
•Intermediate exposure( 1 4 < λ < 1 2): the platform’s
engineering stake already exceeds the social stake while
deployment is still too narrow (over-extraction with
under-deployment);
•High exposure(λ > 1 2): the platform over-invests on its
margin and over-deploys.
In all three regimes the subject margin is degenerate:w S =
−λn≤0, soe E = 0. Under pure platform control the subject
supplies no refresh at any exposure level, and total quality can
remain underprovided even where the platform over-invests
(wheneverk S is large).
Proof:First-order conditions of the three programs in
Proposition 2 (interior cases; corners by the projection). The
stake comparison is direct from (8)–(10).

Remark 6 (Relation to the static monopoly model):The ear-
lier draft’s Theorem 1 obtains the same three-regime structure
in a model where the platform buys fidelityqat convex cost
and person linkage prices exposureλqper deployment: under-
both forλ/A <1−1/
√
2, over-fidelity/under-deployment in
between, over-both forλ/A >1/2. Corollary 2 shows those
regimes are not an artifact of that parametrization: they re-
emerge inside the unified model as the fixed-stock limit, with
thresholds ( 1 4, 1 2 underU[0,1]demand) determined by demand
curvature. What the static model could not see, because it had
no subject input, is the third margin: the represented person’s
refresh supply is already destroyed ineveryregime under pure
platform control. The regimes discipline rhetoric on both sides
(“markets under-provide quality” holds only at low exposure;
“platforms strip-mine identities” only past the thresholds), and
the middle regime implies that neither a pure quality subsidy
nor a pure output subsidy is the right instrument: each moves
the other margin adversely.
C. Rights separation
We now restore the refresh margin, and the next result says
that the deployment wedge cannot be repaired by reassign-
ing ownership: no budget-balanced bundle makesbothco-
producers residual claimants, and control rights and cash-flow
rights operate on different margins.
Theorem 1 (Rights separation):Assume Lemma 3’s con-
ditions, a strictly positive first best, noncontractible efforts,
incentives only via marginal claims on realized refresh, ex
post budget balance, and no external subsidy.
(i)(Team-incentive impossibility.)First-best efforts re-
quirew S = Ωandw P = Ω; but any budget-balanced
bundle allocating private cash flows and monetizable
exposure satisfiesw S +w P =T= Ω−C <2Ω.
Hence no scalar owner and no single revenue-share
rule implements first-best refresh on both margins, even
under perfect price discrimination (C= 0), since then
wS +w P = Ω<2Ω.
(ii)(Control–cash-flow non-equivalence.)With bQ(n) =
(1−δ)Q t +Y E(n), an interior ex-ante platform-
controlled scope satisfiesw ′ P bQ+k SwP w′ S = 0, while
an interior subject-controlled scope satisfiesw ′ S bQ+
kP wSw′ P = 0: generically different conditions at the
same(α, τ). By Proposition 2, in theτ= 0special
case varyingαleavesn P unchanged while movingn S;
varying the controller movesnat fixedα. Cash-flow
rights cannot substitute for scope control, nor conversely.
Proof sketch:(i) Decentralized FOCsc Se=w SYe,
cP x=w P Yx against first-best FOCs withΩ; positivity of
Ye, Yx forces both stakes to equalΩ, contradicting budget
balance; this is Holmstr¨om-type team moral hazard, with buyer
surplus widening the wedge. (ii) Substitute Lemma 3 into
(11), differentiate innusing bQ′ =k Sw′ S +k P w′ P ; corners
atα∈ {0,1}treated separately. The theorem excludes only
budget-balanced marginal-revenue implementations; verifiable
effort, external subsidies, or performance contracts change the
domain.
Corollary 3 (Optimal marginal-stake allocation):In the
additive benchmark, fixingnand total private stakeT >0
withw P =T−w S, decentralized welfareW(w S) =
kS(ΩwS − w2 S 2 ) +k P (ΩwP − w2 P 2 )is uniquely maximized on
the budget-balanced set at
w⋆ S = Proj[0,T]
n (kS −k P )Ω +k P T
kS +k P
o
, w ⋆ P =T−w ⋆ S,
(14)
with∂w ⋆ S/∂kS >0and∂w ⋆ S/∂kP <0in the interior:
measurably higher subject refresh productivity tilts optimal
marginal claims toward the subject. The unconstrained revenue
share implementingw ⋆ S iseα= (w⋆ S −u S −(τ−λ)n)/R(n); it
is implementable iffeα∈[0,1]withw P >0and IR-feasibleF;
otherwise the projectedαis only the nearest feasible boundary
and doesnotattainw ⋆ S.
Remark 7:Corollary 3 is the constructive counterpart of
Theorem 1: given that first best is out of reach, the second-
best allocation of marginal claims is an estimable formula
in(k S, kP ), the two primitives the measurement interface of
Section VIII targets. “Who should hold renewable claims”
is thereby converted from an ideological question into an
econometric one.
D. Non-rival use, rival refresh
The headline result combines both wedges; to state it, define
the equilibrium stake elasticitiesε j :=∂lnY E/∂lnw j >0
forj∈ {S, P}, evaluated on the active region (in the additive
benchmark,ε S =k SwS/Y E andε P =k P wP /Y E, the effort-
supply shares).
Theorem 2 (Non-rival use, rival refresh):Fix(α, τ)and
work in the active region. SinceY E depends onnonly through
the stakes,
dlnY E
dn =ε S
α(1−2n) +τ−λ
wS
+ε P
(1−α)(1−2n)−τ
wP
,
so broader licensing reduces new refresh iff
εS
λ−τ−α(1−2n)
wS
> εP
(1−α)(1−2n)−τ
wP
.(15)
(The one-directional narrative, in which expansion erodes the
subject stake while raising the platform stake, applies when
w′ S <0< w ′ P ; the algebra of (15) is valid regardless.) In the
additive benchmark,
dY E
dn =k S[α(1−2n) +τ−λ] +k P [(1−α)(1−2n)−τ],
and withα=τ= 0:dY E/dn <0⇐ ⇒kSλ > kP (1−2n);
forn≥ 1 2 andλ >0,Y E′(n)<0unambiguously. In steady
state ¯Q(n) =Y E(n)/δ, sosign ¯Q′(n) = signY E′(n):poli-
cies that raise reach (portability, interoperability, competition)
can increase current access while reducing the next period’s
new memory and the long-run stock.
Proof:Chain rule on (12) (additive case) and on
Lemma 3’s closed forms (general case), withw ′ S(n) =α(1−
2n) +τ−λandw ′ P (n) = (1−α)(1−2n)−τfrom (8)–(9);
the steady state solvesδ ¯Q=Y E.

Corollary 4 (Access gains do not imply continuation-welfare
gains):WithW E(n) = ΩY E − kS w2 S 2 − kP w2 P 2 andΩ ′(n) =
1−n−λ: even whenΩ ′(n)>0(a marginal deployment
has positive static social value),W E′(n)<0on an open
parameter region compatible with0< λ < 1 2. Nonrivalry
of copying is not sufficient for monotone welfare gains from
broader deployment: as long as the represented person remains
an endogenous supplier of refresh, deployment scope enters
the future supply function.
Proposition 3 (Fixed buyouts create no refresh margin;
renewable claims do, with financing caveats):On the same
active branch (participation, rights,nunchanged), a fixed
buyout priceFsatisfies∂e E/∂F=∂x E/∂F= 0; an alien-
ating sale leavingw sale S ≤0inducese sale = 0. A renewable
claim∆w S >0raises subject effort by∆e= (η S/cS)∆wS
always, but its effect on total refresh depends on financing: if
funded by new extractable surplus or outside funds (locally
wP constant),∆Y=k S∆wS and∆ ¯Q= (k S/δ)∆wS;
if a budget-balanced reallocation (∆w P =−∆w S), then
∆Y= (k S −k P )∆wS, which is positive iff the subject is the
more productive refresher, and welfare-improving only when
it moves stakes toward Corollary 3’sw ⋆ S. When continuation
refresh has substantial value, the essence of “memory as an
asset” is not minting a transferable token but designing a
relational contract that keeps paying for refresh.
E. Ownership as it ought to be and as it is
The public debate the paper addresses has a normative pole
(memoryoughtto belong to the person it represents) and a
positive pole (memoryis, under current conditions, held by the
platforms that extract it). In the space of Definition 8 these are
two corner institutions:
gS = (c=S, α=1, τ=0)(theoughtcorner),
gP = (c=P, α=0, τ=0)(theiscorner).
The comparison below is stated in the additive benchmark with
uS =u P = 0; all closed forms are exact there.
Proposition 4 (The ought and the is):
(i)(Symmetric margin destruction.)Underg P ,w S =
−λn≤0ande E = 0; underg S,w P = 0andx E = 0.
Each corner converts a co-production technology into
single-input production: whoever does not own supplies
no refresh.
(ii)(Scope.)Because the non-owner’s margin is dead, each
owner’s ex-ante payoff isπ j =w j(n)(1−δ)Q t +
kj wj (n)2
2 , monotone in the own stake, so the ex-ante
scope choice coincides with the fixed-stock program of
Proposition 2. The ought corner internalizes exposure
fully but monopolizes:n S = 1−λ 2 = nW 2 , so deployment
is always exactly half the first best, never excessive. The
is corner is exposure-blind:n P = 1 2, with the reversal
regimes of Corollary 2.
(iii)(Welfare ranking is an empirical question.)Corner
welfares are
WS = kS(1−λ) 4 16 , W P = kP (1−2λ) 16 ,(16)
so the ought corner dominates the is corner iffk S(1−
λ)4 > kP (1−2λ): always whenλ≥ 1 2, and at low
exposure iff the subject is (roughly) the more productive
refresher,k S/kP >(1−2λ)/(1−λ) 4. The ownership
debate thereby reduces to two measurable quantities:
exposure intensityλand the refresh-productivity ratio
kS/kP .
(iv)(Neither corner is the normative target.)Fix either
corner’s scopenand the implied total stakeT(n)>0.
Whenever Corollary 3’s optimum is interior (0<(k S −
kP )Ω +kP T <(kS +k P )T, which holds for allk S/kP
in a neighborhood of1), reallocating marginal claims
from the corner tow ⋆ S ∈(0, T)strictly raises welfare,
and re-optimizingnraises it further. The corners are
dominated by interior renewable-claim bundles: the cor-
rect normative object is not “who owns” but the stake
profile(w ⋆ S, w⋆ P ).
Proof:(i) Substitute into (8)–(9) and apply Lemma 3’s
corner branch. (ii) Envelope on the owner’s effort choice; the
FOC reduces tow ′ j(n) = 0, giving Proposition 2’s scopes. (iii)
W E = Ωk jwj − kj w2 j 2 at each corner’s scope; direct substitu-
tion. (iv) Strict concavity ofW(w S)in Corollary 3. (With the
capitalization factor restored, the steady-state flow versions are
WS ∝k S(3−δ)(1−λ) 4 andW P ∝k P (3−δ−4λ); theδ= 1
case reduces to the displayed threshold, and the comparative
statics are unchanged.)
Remark 8 (Compensated platform control; the earlier draft’s
Proposition 2 recovered):A third bundle completes the map:
gA = (c=P, α=0, τ=λ), platform control with full per-
quality-deployment compensation, the formalization of “im-
peccable consent.” Because compensation makes the platform
internalizeλ, it choosesthe same scope as the ought corner,
nA = 1−λ 2 = nW 2 , exactly the earlier draft’s Proposition 2
(“deployment exactly half the first best under full compen-
sation”), now derived inside the unified model. The opposite
margin, however, survives:w P = (1−λ)2 4 ,w S = 0. Corner
welfares become perfectly symmetric,W A = kP (1−λ)4 16 versus
WS = kS (1−λ)4 16 : once the deployment wedge is priced,
the choice between subject ownership and fully-compensating
platform ownership ispurelythe question of whose refresh
input is more productive. One caution:W A < W P iff
(1−λ) 4 <1−2λ, i.e. for allλbelowλ † ≈0.456: in this
distortion-free benchmark, mandating full compensation at low
exposurelowerswelfare, because it taxes the only live refresh
margin. The efficiency case for compensation is not this static
one; it is Section V’s pollution channel, where compensation
buys authenticity from strategic subjects.
Remark 9 (Why theisprevails, and what follows):The
is corner is not an accident of law; it is selected by feasi-
bility. Subject control presupposes the objective conditions
the model names:Separability(Definition 2), meaning the
artifact must be extractable from the host at all; functional
portabilityϕ(Definition 8), meaning that exporting it must
preserve behavioral value; and attentionζ, meaning the subject
must perceive her exposure. Whenϕ≈0orζ≪1,g S

is technologically or behaviorally infeasible, and the market
defaults tog P regardless of what anyone thinksoughtto
hold. Section V sharpens this from a constraint into an
equilibrium: with naive subjects present, the platform profits
from opacity and zero compensation (obfuscation substitutes
for compensation), so the conditions that keepg S infeasible
are themselves maintained by the incumbent’s optimal play:
the is perpetuates itself. Two policy consequences follow. First,
by Theorem 1(ii),renaming the owner without movingϕandζ
changes neither scope nor refresh: nominal ownership reform
is not the binding margin, portability and salience are. Second,
by (iii)–(iv), when those conditions can be moved, the target is
not the ought corner but the interior renewable-claim bundle,
since the ought, taken literally, would destroy the platform’s
refresh margin exactly as the is destroys the subject’s.
F . Taking stock
The section has delivered three results, one mechanism, and
a resolution of the ought–is question. Proposition 1 fixes the
ultimate scarcity: decision value is bounded by lived experi-
ence. Proposition 2 and Corollary 2 show that with the stock
frozen, person linkage already reverses the direction of the
platform’s distortion, and silently destroys the subject’s supply
margin. Theorem 1 shows the reversal cannot be repaired
by reassigning ownership: co-production plus budget balance
leaves at least one margin under-incentivized, and control
and cash flow are non-substitutable instruments. Theorem 2
delivers the dynamic consequence: because refresh is relation-
ally supplied, reach-expanding policy can trade current access
against the long-run stock, and Corollary 4 shows the trade can
be welfare-negative even when each marginal deployment is
statically valuable. Proposition 4 then closes the framing: the
ought and the is are twin corners that each destroy one supply
margin; their ranking is an empirical question in(λ, k S/kP );
and both are dominated by interior bundles that keepbothco-
producers on renewable claims. Everything above holds under
perfect provenance and complete information: the failures are
in the asset’s person linkage and its co-produced renewal, not
in verification or beliefs. Section V endogenizes what was held
fixed here: the subject’s option to distort her revealed behavior
(pollution), the participation margin that determines thickness
(formation), and with them the mechanism by which the is
corner reproduces itself.
V. ENDOGENOUSQUALITY ANDMARKETFORMATION
Section IV held two things fixed that no real memory
market holds fixed: theauthenticityof the subject’s revealed
behavior, and thesetof subjects who supply at all. This
section endogenizes both, and in doing so completes the
positive theory promised in Section IV-E: theiscorner is
not merely inefficient; it isself-perpetuating, because the
platform’s equilibrium play maintains the very conditions that
make subject control infeasible. Throughout, Assumptions 1–
2 remain in force: everything below happens under perfect
provenance, and the only informational friction we add, the
naive shareν, is aboutawareness of extraction, not about
fabricated lineage or hidden quality.
A. Setup: distortion, awareness, and compensation coverage
Before extraction, anawaresubject can distort her revealed
behavior at strictly convex costκ d(d),κ d(0) =κ ′ d(0) = 0,
κ′′ d >0, reducing effective fidelity to˜q= (1−d)Q(closed
forms useκ d(d) =c dd2/2). Distortion is the individually
rational counterpart of Proposition 1: the subject cannot raise
the ceiling of what her history contains, but she can lower
what extraction recovers from it.
Two objects are derived from Section III rather than intro-
duced by assumption. The subject’scompensation coverage
per unit of quality-deployment is
s:=τ+ αR(n) n ,(17)
her total receipts per quality-deployment under the rights
bundleg; her net exposure per unit of effective quality is then
(λ−s)D, whereDis thedeployment scale. In the single-unit
model of Section III,D=n; we keep it as a separate symbol
because the aggregate market of Section V-C multiplies it by
thickness. A shareν∈[0,1)of subjects isnaive(unaware that
extraction occurs); the platform chooses opacityo∈ {0,1}
(o= 1preserves naivety;o= 0, or a transparency mandate
T= 1, converts naive into aware). Naivety is the discrete
counterpart of the attention parameterζof Section V-G.
B. Pollution and instrument complementarity
Theorem 3 (Pollution and complementarity):
(i)(Endogenous fidelity ceiling.)The aware subject’s dis-
tortion satisfies
κ′ d(d∗) = (λ−s) + QD,(18)
sod ∗ >0iff exposure is uncompensated (s < λ), and
in that case effective fidelity˜q ∗ = (1−d ∗)Qis strictly
decreasing in market scaleD: the platform-controlled
memory market pollutes its own raw material as it
grows. In the quadratic benchmarkd ∗ = min{1,(λ−
s)nQ/cd}.
(ii)(Compensation is quality control.)Ifs≥λ, thend ∗ =
0and, sinces≥λimpliesw S =u S +αR+ (τ−λ)n≥
uS ≥0with strict inequality whenever coverage is strict,
refresh effort recovers along with authenticity. Paying
the subject is not (only) redistribution; it purchases
authenticity. Asset quality is a function of the institution.
(iii)(Obfuscation equilibrium and instrument comple-
mentarity.)Naive subjects neither distort nor chill and
are the platform’s cheapest high-quality supply, so for
ν >0the platform’s one-shot optimum is(o, s) =
(1,0): obfuscation substitutes for compensation. Con-
sequently: a transparency mandate alone (T= 1,s= 0)
converts naive into distorting subjects, so effective qual-
ity and buyer surplus fall; compensation alone (T= 0,
s≥λ) restores the aware subjects’ authenticity but
leaves the naive exposed without informed consent;

only the pair (T= 1ands≥λ), or subject control
itself, restores authenticity and voluntariness together.
Transparency and compensation are complements, not
substitutes.
(iv)(Commitment.)A promiseds≥λis not credible in the
one-shot game: once˜qis supplied, compensation is a
pure transfer and the platform reneges; anticipating this,
aware subjects distort. A rule-based cession of revenue
rights (tokenized royalties or governance commitments
in the sense of [18]) implementss≥λand is in the
platform’s own interest iff
(1−ν)R(n)Q > c d :(19)
few naive suppliers, cheap distortion technology, high
stakes. Where the inequality fails (abundant naivety),
the platform strictly prefers opacity, which is part (iii)’s
equilibrium.
Proof:(i) The aware subject minimizes(λ−s) +(1−
d)QD+κ d(d); the FOC is (18), andd ∗ >0iff the marginal
benefit atd= 0is positive, i.e.s < λ;∂d ∗/∂D=
(λ−s)Q/κ ′′ d >0by the implicit function theorem, so
∂˜q∗/∂D <0. (ii) Ats≥λthe objective is nonincreasing
ind;d ∗ = 0; the stake bound is (8). (iii) Platform flow
profit per subject is[R(n)−sn]˜q(s;awareness); a naive subject
supplies˜q=Qat anys, so profit from the naive is maximized
ats= 0, ando= 1preserves that supply at zero cost;
an aware subject ats= 0suppliesQ(1−d ∗(0)). Hence
Π(o=1, s=0)−Π(o=0, s=0) =νR(n)Q d∗(0)>0forν >0,
d∗(0)>0: opacity strictly dominates voluntary transparency.
The welfare statements follow cell by cell:(T=1, s=0)re-
places naive supplyQbyQ(1−d ∗(0))(quality and buyer
surplus fall byR- andC-proportionality);(T=0, s≥λ)leaves
a measureνof subjects bearingλ˜qDwithout informed choice:
monetary compensation reaches them, but voluntariness (the
constraintℓ∈ R i(m), Assumption 6) does not; both in-
struments together setd ∗ = 0with all subjects aware. (iv)
The renege gain issn˜q >0, so anys >0is sequentially
irrational without a binding rule. Under the rule, per-subject
profit is(R(n)−λn)QagainstR(n)Q[ν+ (1−ν)(1−d ∗(0))]
under opacity; in the quadratic benchmark the difference is
λnQ[(1−ν)R(n)Q−c d]/cd, positive iff (19).
Remark 10 (Misrepresentation robustness):With exposure
λP ˜q+λM (1−˜q), distortion’s private return falls; for largeλM
the subject prefers high-fidelity-or-exit, and the policy content
of (iii) extends from compensation togenuinely feasible exit
rights.
Corollary 5 (Theiscorner is self-perpetuating):In the
obfuscation equilibrium of Theorem 3(iii), the platform’s
optimal play (a) maintainso= 1, keeping the aware share (and
hence effective attentionζ) low, and (b) supplies no functional
portability, sinceϕ >0only improves the subject’s outside
option and the feasibility ofg S without raising platform rev-
enue. The objective conditions for subject control identified in
Section IV-E (Separability exercised throughϕ, and awareness
ζ) are therefore endogenously unmet on the equilibrium path:
absent intervention that targetsϕandζdirectly, the de facto
cornerg P reproduces itself. By Theorem 1(ii), intervention
that renames the owner while leavingϕandζin place does
not disturb this equilibrium.
Proof:(a) is Theorem 3(iii). (b): platform revenue
[R(n)−sn]˜qis independent ofϕ, whileϕ >0weakly raises
the subject’s outside option ¯US and hence theFneeded for
IR: portability is weakly costly, strictly so when exit is an
equilibrium threat. The last sentence is Theorem 1(ii).
C. Setup: participation and thickness
Subjects are heterogeneous in sensitivityλ i ∼G(smooth,
positive densityg). Subjects withλ i below a threshold list;
the listing mass is the market thicknessM=G( ˆλ)of
Definition 10, and the match value of a listing is
Θ(M) := ˜Θ(Ψ(M)), ˜Θ′ >0,(20)
increasing in the market precisionΨ(M) = (σ 2 0+1/(M ¯ψ))−1:
thicker markets aggregate the common component better,
and buyers pay for that precision.Θinherits Definition 10’s
curvature: increasing, concave, andbounded, withΘ ′(M)→0
asMgrows. Aggregation saturates becauseσ 2 0 >0is
noise no thickness can remove. Letv >0be the match-
surplus fundamental per listing, of which the listing subject
appropriates the coverage shares(Section V-A).
Each listing also leaks: by Definition 1, within-class per-
sonal components are correlated (ϱ >0), so a listed artifact
is informative aboutnon-listingpeers; define therelational
leakage intensityΛ(ϱ)≥0,Λ(0) = 0,Λ ′ >0: a listing
imposes expected exposureΛ(ϱ) ¯λnl ˜qDon correlated non-
listers, where ¯λnl is their mean sensitivity. Private listing
decisions ignore this term entirely; it bypasses even perfect
consent, because the person harmed never signed anything.
D. Formation, the three wedges, and over-participation
Theorem 4 (Formation and the direction of the participation
distortion):
(i)(Threshold equilibria and selection.)Equilibria are
threshold rules: subjects withλ i ≤ ˆλ∗ list, where ˆλ∗
solves
ˆλ=s vΘ(G( ˆλ)).(21)
Thickness–participation complementarity (Θ ′ >0) can
generate multiple equilibria: a self-fulfilling thin trap
coexisting with a thick market. With private noise about
the fundamentalv, a global-games perturbation selects a
unique threshold and restores unambiguous comparative
statics (standard transplant of [19]).
(ii)(Three wedges; the direction is aniff.)The planner’s
threshold satisfies
ˆλW =vΘ(G) +vΘ ′(G)G−Λ(ϱ)P( ˆλW ),(22)
whereP( ˆλ) := ¯λnl(ˆλ) ˜qD×(mass of affected peers per
listing) is the marginal relational harm. Comparing with
(21), the market threshold exceeds the planner’s (over-
participation) iff
Λ(ϱ)P >(1−s)vΘ| {z }
appropriability wedge
+vΘ ′(G)G| {z }
thickness externality
.(23)

The marginal lister ignores one negative externality
(relational leakage) and two positive margins (unappro-
priated match surplus and her contribution to everyone
else’sΘ); which force wins is a measurable comparison,
not an axiom.
(iii)(Why person-linked memory markets tend to be
too thick.)As the market thickens, the right side of
(23) attenuates and the left side does not:Θ ′(M)→0
by Definition 10’s saturation, whileΛ(ϱ)Pis anchored
by the class correlationϱ, which for preference/policy
memory is largest exactly among similar people, the
defining feature of the focal class (Definition 1). Hence
for anyϱ >0and coveragesclose to full appropriation,
there is a finite thickness beyond which (23) holds and
every additional lister is socially excessive. Naive par-
ticipation (ν >0, orζ <1) shifts the market threshold
further right at unchanged welfare, amplifying over-
participation independently. In contrast to thin-market
underprovision in the received data-economics litera-
ture, identity-entangled memory markets over-thicken at
scale.
(iv)(Non-monotone welfare.)WelfareW( ˆλ) =R ˆλ
0 [vΘ(G(ˆλ))−ℓ]dG(ℓ)−Λ(ϱ)G( ˆλ) ¯λnl(ˆλ)˜qD
is non-monotone in the threshold: it rises while low-λ
subjects enter and falls once (23) binds. There are
parameter regions (Λ(ϱ)large, mass ofGat highλ,
or large naive share) where marginal growth subsidies
destroy welfare and where the voluntary formation
of the market is itself welfare-negative: relational
externalities bypass participants’ revealed preference,
and naive participation is not informed revelation.
Proof sketch:(i) Best responses are monotone in the
conjectured threshold; existence by Tarski; multiplicity when
svG′Θ′ >1somewhere; global-games uniqueness by strategic
complementarity plus dominance regions atvextremes. (ii)
DifferentiateWat the threshold:W ′(ˆλ) =g( ˆλ)[vΘ− ˆλ+
vΘ′G−ΛP]; the market condition replaces the bracket by
svΘ− ˆλ; subtract. (iii)Ψ ′(M) = ¯ψ/(M ¯ψσ 2 0 + 1)2 →0;
Λ(ϱ)Pbounded away from zero forϱ >0with nondegenerate
¯λnl; naive listers useζλ i < λi in the private cutoff while
Wevaluates trueλ i. (iv) Sign change ofW ′ from (ii)–(iii);
the formation statement comparesW( ˆλ∗)withW(0) = 0.
Appendix B gives the full argument, including the single-
crossing condition under which the two thresholds can be
ordered.
Remark 11 (Correction relative to an earlier draft):An
earlier statement claimed over-participation unconditionally
whenever relational leakage is positive. That is false as stated:
the marginal lister also confers the two unpricedpositive
margins in (23), and at low thickness they can dominate: a
thin memory market can genuinely be too thin. The defensible
claim is theiffin (ii) plus the saturation argument in (iii): the
presumption of over-participation is an asymptotic property
of thick, high-ϱ, well-appropriated markets, and (23) tells the
econometrician exactly which three objects to measure. Reg-
ulators should track relational-externality density, not listing
counts (cf. Section VII).
E. Selection into authorization
Formation determineswho lists; institutions determinewhat
listing signals. Fix a class of artifacts with heterogeneous
effective fidelity˜qand subjects private inλ i ∼G, independent
of˜q; a marketplace pays a royalty per deployment.
Proposition 5 (An authorization badge is not a fidelity
certificate):
(i) Under aflatroyaltyrper deployment, subjectiautho-
rizes iffλ i ˜qD≤r, soPr(authorized|˜q) =G(r/(˜qD)),
strictly decreasing in˜q: the authorized pool is first-order
stochastically worse in fidelity, so the badge is a negative
quality signal.
(ii) If misrepresentation harm dominates (exposure decreas-
ing in˜q), the direction reverses; authorization is generi-
cally informative about fidelity in a direction set by the
harm technology, never a neutral stamp.
(iii) Under the quality-indexed royalty of Definition 8 (com-
pensationτperquality-deployment, i.e.r(˜q) =τ˜qD),
the authorization condition becomesλ i ≤τ: participa-
tion is independent of˜qand selection is shut down.
Proof:(i) The cutoffr/(˜qD)falls in˜q; FOSD is mono-
tonicity ofG. (ii) Replaceλ i ˜qbyλ ih(˜q)withh ′ <0and
repeat. (iii)˜qDcancels.
Remark 12:Proposition 5(iii) is the reason Definition 8
definesτper quality-deployment rather than per deployment:
the indexation is not a modeling convenience but the instru-
ment that makes authorizationuninformative about quality,
which is what allows permission credentials and performance
credentials to be issued separately (Section VII). The econom-
ically correct role of an independent certifier is therefore not
to substitute for consent but to make˜qcontractible, enabling
exactly this indexation. Under flat royalties, empirical fidelity
comparisons between authorized and unauthorized pools are
confounded by (i); Section VIII turns this into a test.
F . The reach bridge: thickness feeds depletion
Corollary 6 (Thickness transmits into the stock):With the
reach bridgen=N(M),N ′ ≥0(Definition 10), the long-run
stock responds to thickness as
d ¯Q
dM = 1 δ dY E dn N ′(M),(24)
withdY E/dnfrom Theorem 2; and effective delivered quality
is˜q(s)× ¯Q, with˜qfrom Theorem 3. Hence market growth acts
on the memory stock through three multiplicative channels:
participation (Theorem 4), reach (Theorem 2), and authenticity
(Theorem 3). It can therefore raise measured access while
lowering both the stock and its fidelity when coveragesis
low. Full tipping dynamics and the relational-data-externality
fixed point are developed in the aggregate extension.

G. Limited attention
If the subject perceives only a shareζ∈[0,1]of true
exposure, her perceived stake replacesλbyζλ; effortrises
as attention falls (∂e E/∂ζ=−η Sλn/cS <0), distortion
falls, and observed consent weakly expands. But welfare must
be evaluated at the trueλ: higher measured participation and
higher measured quality under low attention are not evidence
of higher welfare; they are Theorem 3(iii)’s obfuscation equi-
librium in continuous form.ζ= 1recovers full rationality,
and the sophistication-selection conjecture (Section IX) is the
cross-sectional implication: the market sources its best raw
material from those least able to protect themselves.
H. Where this leaves the institution space
Theorems 3–4 add the last two rows to the paper’s in-
strument logic. Compensation coveragesisquality policy
(Theorem 3(ii)) and, indexed per quality-deployment,selection
policy(Proposition 5(iii)); transparencyTisvoluntariness
policy, worthless for quality on its own (Theorem 3(iii));
portabilityϕand attentionζarefeasibility policyfor subject
control, and no private actor supplies them in equilibrium
(Corollary 5); participation volume is not a health metric,
and the object to monitor is relational-externality density (23).
None of these instruments substitutes for another, and none is
delivered by provenance, which has been perfect on every page
of this section.
VI. THEOPTIMALRIGHTSBUNDLE
Sections IV–V were diagnostic: the ownership corners each
destroy a supply margin (Proposition 4), uncompensated mar-
kets pollute their raw material (Theorem 3), and formation can
over-thicken (Theorem 4). This section is constructive, solving
for thesecond-best rights bundle: the choice of(α, τ, n)that
maximizes welfare subject to the frictions the model takes
as primitive, namely noncontractible efforts, budget balance,
and the subject’s option to distort. Two regimes are analyzed:
commitment(a planner, or a marketplace constitution, fixes
scope and compensation directly) anddelegation(the planner
fixes only the cash-flow bundle(α, τ); the controller named
incchooses scope). Throughout we work in the additive
benchmark withu S =u P = 0; general flows are restored
in Appendix E.
A. Coverage is the single static instrument
The bundle(α, τ)appears to give the designer two com-
pensation instruments, but it does not.
Proposition 6 (Instrument collapse and the financing slope):
(i) At any scopen, the stakes (8)–(9) depend on(α, τ)only
through the coverages=τ+αR(n)/nof Section V-A:
wS =u S +(s−λ)n, w P =u P +R(n)−s n.(25)
Revenue shares and per-quality royalties are perfect
substitutes for refresh incentives at fixed scope.
(ii) They are not substitutes across scopes: holding(α, τ)
fixed,∂s/∂n=−α. Royalty-financed coverage is reach-
invariant; share-financed coverage dilutes as reach ex-
pands, and under pure share financing (τ= 0) coverage
crosses the authenticity floorλexactly atn= 2n S,
twice the subject’s own preferred scope (Proposition 2).
Expansion under share financing therefore drives the
market into Theorem 3’s pollution region mechanically,
with no change in the written contract.
(iii) Both instruments are quality-indexed in the sense of
Proposition 5(iii): neither induces selection on fidelity.
The designer’s static choice is one number,s; theα–
τsplit matters only through (ii) and through delegation
(Section VI-D).
Proof:(i)αR+τ n=n sby definition ofs; substitute
into (8)–(9). (ii)s(n) =τ+α(1−n); solves(n) =λand
compare with Proposition 2’sn S. (iii) Both scale receipts with
˜q; apply Proposition 5(iii).
B. The second-best bundle under commitment
The commitment program is
max
n∈[0,1], s≥0
W E(n, s) = Ω(n)YE − kS w2 S 2 − kP w2 P 2 (26)
subject to Lemma 3 andw P ≥0, on the no-pollution region
s≥λfirst; Section VI-C opens the polluted region.
Theorem 5 (The second-best bundle):
(i) At any scope, optimal coverage implements Corol-
lary 3’s stake profile:
s∗(n) =λ+ w⋆ S(n) n ,(27)
so the subject’s compensation exceeds bare exposure by
exactly her optimal renewable claim per unit of reach.
(ii)(The authenticity floor is self-enforcing.)s ∗(n)≥λ
iffw ⋆ S(n)≥0iff
kS
kP
≥ C(n) Ω(n) = n 2−2λ−n :(28)
whenever the subject’s relative refresh productivity ex-
ceeds the buyer-surplus share of social value, the second
best pays above exposure without any authenticity man-
date; Theorem 3(ii)’s floor is implied, not imposed.
(iii)(Closed form, symmetric productivities.)Fork S =
kP =k, the concentrated programW ∗(n) =k n2(1−
λ−n)

3(1−λ)−n

/4has the unique interior maximizer
n∗ = 3−
√
3
2 (1−λ)≈0.634 (1−λ),
s∗ =λ+
√
3−1
4 (1−λ),
(29)
strictly between the subject-corner scope 1−λ 2 and the
static welfare scope1−λ.
(iv)(The one-third depletion haircut.)In the polar single-
margin cases (the projection binds:w ⋆ S ∈ {0, T}), the
concentrated program yieldsn ∗ = 2 3 (1−λ). Hence
across all productivity ratios,
n∗ ∈ h 3− √ 3 2 , 2 3 i ×(1−λ)≈[0.63,0.67]×(1−λ),(30)

decreasing inλ: the dynamic second best deploys
roughly two-thirds of the static first-best reach, almost
independently of who the productive refresher is. The
missing third is the price of keeping refresh incentives
alive: the depletion externality of Theorem 2, now
internalized as a scope haircut.
Proof:(i)–(ii):∂W E/∂s=n[(k S −k P )Ω−k SwS +
kP wP ]; the root reproduces Corollary 3’sw ⋆ S, ands ∗ −λ=
w⋆ S/n; the productivity condition isw ⋆ S ≥0rearranged
withΩ =T+C. (iii): substitutes ∗(n), factor, take the
interior root of the FOC; the second candidate exceeds1−λ
and is infeasible. (iv): with a cornered stake the program is
maxn kj[ΩT− T 2 2 ], whose FOC has the interior root 2 3 (1−λ).
Appendix C shows that the concentrated program is unimodal
on(0,1−λ)for every productivity ratio, gives the closed
form (44) forn ∗ at an arbitrary ratio, and establishes that the
band (30) is exact and attained, so no quasiconcavity regularity
condition is needed.
Remark 13:Theorem 5 converts Section IV-E’s ought–
is stalemate into a design rule with two estimable inputs.
The scope rule barely needs the productivity split (n ∗ moves
within a four-point band); the compensation rule needs it
exactly (s ∗ is linear inw ⋆ S, which is linear ink S −k P ). An
econometrician who can estimate onlyλcan already set scope
nearly optimally; setting compensation requires Section VIII’s
decomposition of refresh into subject and platform contribu-
tions.
C. When is pollution tolerated?
Dropping the constraints≥λand letting effective quality
carry Theorem 3’s multiplier˜q(s) = 1−d ∗(s)(quadratic
benchmark,d ∗ = (λ−s) +nQ/cd), the objective acquires
a kink ats=λ. Writea 1 := 1−λ−n >0and
a2 := 2−2λ−n >0on the active region.
Proposition 7 (Three coverage regimes):The second-best
coverage satisfies:
(a)Strict renewable claim,s ∗ > λ, iffk S/kP > n/a2
(Theorem 5(ii));
(b)Floor exactly,s ∗ =λ: the subject is fully covered but
holds no net claim; no pollution and zero distortion,
which is the corner regime between (a) and (c);
(c)Tolerated pollution,s ∗ < λ, iff
cd

(kP −k S)a 2 −2k P a1

> Q kP n a1a2,(31)
i.e., only when the platform is the strongly dominant
refresherandthe distortion technology is stiff (c d large
relative to the stakesQR): the subject is simultaneously
unproductive and defenseless, so buying her authenticity
is not worth the platform stake it costs.
Proof:One-sided derivatives of the kinked objective at
s=λ: from above,sign = sign(w ⋆ S); from below, the
displayed expression, computed in closed form in Appendix D.
Remark 14 (Normative caveat):Regime (c) is a transferable-
utility statement and nothing more: it prices the subject’s
distortion, not her autonomy. Under Assumption 6 the
inalienable-use constraintℓ∈ R i(m)can exclude (c) out-
right, and under the misrepresentation variant (Remark 10)
the regime shrinks further, since low fidelity then harms the
subject directly. We report (c) because suppressing it would
hide what pure efficiency logic recommends, and that is
precisely the kind of claim a welfare analysis should expose
to normative scrutiny rather than bury.
D. Delegated scope: who should control deployment
Suppose the planner sets only(α, τ)and the controller
named incchooses scope ex ante (Theorem 1(ii)’s conditions).
Can the commitment optimum(n ∗, s∗)be reproduced? By
Proposition 6, delegation gives the planner two instruments
for two targets (the controller’s scope FOC and the coverage
identity), so the question is feasibility, not counting.
Theorem 6 (Delegated implementation is asymmetric):
(i)(Platform control.)The unique candidate pair is
α∗ = s∗ −1 + 2n ∗
n∗ , τ ∗ = (1−α ∗)(1−2n ∗),(32)
and it is feasible (τ ∗ ≥0,α ∗ ∈[0,1]) only ifn ∗ ≤ 1 2.
In the symmetric benchmark this holds iff
λ≥λ c = 3−
√
3
6 ≈0.211.(33)
For low-exposure classes the platform under-deploys and
per-quality royalties can only shrink its reach further;
implementingn ∗ > 1 2 requiresτ ∗ <0, that is,
per-deployment subsidies (cf. Proposition 3’s financing
caveat).
(ii)(Subject control.)The unique candidate pair is
α∗ = w⋆ S
(n∗)2 , τ ∗ =λ−α ∗(1−2n ∗),(34)
and in the symmetric benchmark it is feasible for every
λ∈(0,1), with the remarkably simple formα ∗ =
1
2
√
3 ≈0.289(constant inλ) andτ ∗ >0increasing inλ.
(iii)(Reading.)The feasibility map answers Section IV-E’s
control question constructively: theoughtcontroller is
delegation-feasible for every exposure class, while theis
controller is delegation-feasible only where exposure is
high (λ≥λ c), which are exactly the classes where, by
Corollary 2, platform scope is least distorted to begin
with. Where the de facto regime cannot be steered to
the second best with nonnegative royalties, the options
are direct scope regulation (Section VI-B), deployment
subsidies, or reassigning control; only the last also
repairs the feasibility conditions of Corollary 5.
Proof:Substitute the controller FOCs of Proposition 2
into the coverage identity: under platform controls=
(1−2n) +αnalong the FOC locus, under subject control
s=λ+αn; solve each pair for(α, τ). Feasibility bounds
by direct evaluation; the symmetric constants follow from
n∗ = 3−
√
3
2 (1−λ)andw ⋆ S =T /2, whenceα ∗ = (1−λ−
n∗)/(2n∗) = 1 2 √ 3.

E. Taking stock: the constitution of a memory market
Assembling Sections IV–VI, the second-best constitution of
a personalized-memory market has five components, none of
which is “an owner.”Coverages ∗ =λ+w ⋆ S/n: compensation
above exposure by the subject’s optimal renewable claim,
royalty-financed rather than share-financed where reach is
expected to grow (Proposition 6(ii)), committed through rules
rather than promises (Theorem 3(iv)).Scopen ∗ ≈ 2 3 (1−λ):
the static welfare rule with a one-third depletion haircut
(Theorem 5(iv)), either set directly or delegated subject to
Theorem 6’s feasibility map.TransparencyT= 1, which is
complementary to coverage, not a substitute (Theorem 3(iii)).
Feasibility infrastructure, portabilityϕand salienceζ, sup-
plied by policy because no equilibrium actor supplies them
(Corollary 5). Andformation monitoringkeyed to relational-
externality density rather than listing counts (Theorem 4). The
ought–is question dissolves on contact with this list: what the
subject should hold is not the asset but a claim structure; what
the platform should hold is not the asset but a residual stake
plus scope constrained by its own feasibility region; and what
neither should hold is the other’s margin.
F . Information and market-design extensions (compressed)
Everything above holds under complete information (As-
sumption 2). Relaxing it adds a familiar layer, which we
compress because it is the least memory-specific part of the
problem and is developed in Appendix F: private fidelity
generates an Akerlof pool [12] whose repair is performance
certification, distinct from provenance certification and subject
to certifier market power in the sense of Lizzeri [13]; pre-
purchase evaluation leaks the asset, pushing high-κ ⋆ classes
toward query-sandbox access and audited replay [15]; and
compatibility-indexed evaluation is forced by Lemma 1 re-
gardless of information structure. The certifier’s economically
correct role was already pinned down with complete informa-
tion (Remark 12): make˜qcontractible so that coverage can
be quality-indexed; certification serves authorization and never
substitutes for it. Multi-subject relational memory remains
companion-paper scope, with Theorem 4’s machinery as the
vehicle.
VII. GOVERNANCE ANDDESIGNIMPLICATIONS
A. Reading the model as a design document
Every claim in this section is a corollary of Sections IV–
VI, cited by result; none is a prior. This discipline matters
because governance debates about AI memory currently run on
intuitions (“data wants to be shared,” “users should own their
data,” “markets will under-provide quality”), each of which the
model shows to be true only on a bounded parameter region,
and each of which, applied outside its region, prescribes the
wrong instrument. Three kinds of actors implement what
follows: themarketplace constitution(rules a platform or
exchange can adopt unilaterally and commit to), theregulator
(mandates that no equilibrium actor supplies privately), and
infrastructure(credentials and benchmarks that make the other
two contractible). The failure–instrument matrix (Table I)
assigns cures to diseases; Section VII-B states the general
lessons; Section VII-C assigns the work.
Two structural properties of the matrix deserve emphasis.
No column dominates: every instrument in the fourth column
fails against at least one failure other than its own, which
is why the matrix cannot be collapsed into a single score
or a single reform (Section VII-D).The failure column is
ordered by visibility: failures 1–4 are legible in a single
transaction; failures 5–10 are equilibrium objects, visible only
in aggregates (refresh rates, stock trajectories, pool compo-
sition, participation densities). That is why Section VIII’s
measurement interface is part of governance, not an academic
afterthought.
B. Ten derived implications
1)There is no universal owner(Thm. 1; Prop. 4). Two
noncontractible investors both need marginal incentives;
budget balance forbids giving both the full margin;
and each ownership corner destroys the other party’s
supply. “Who owns the memory” is the wrong regulatory
question.
2)Renewable claims are conditional, and the condition
is estimable(Cor. 3; Thm. 5(ii)). The subject should
hold a positive continuation claim iffk S/kP ≥C/Ω;
this requires no operational control and is an economet-
ric threshold, not an ideological one.
3)Compensation is quality policy(Thm. 3(ii);
Thm. 5(ii)). Paying subjects buys authenticity (an
efficiency argument independent of fairness), and in
the second best the authenticity floor is self-enforcing
wherever the subject is a productive refresher.
4)Transparency and compensation are complements
(Thm. 3(iii)). Mandating either alone converts naive
supply into distorted supply or leaves the naive exposed;
only jointly do authenticity and voluntariness recover.
5)How compensation is financed matters as much as
its level(Prop. 6(ii)). Share-financed coverage dilutes
mechanically as reach expands and crosses the authen-
ticity floor at twice the subject-preferred scope; growing
markets should be royalty-financed.
6)Access metrics are not welfare metrics(Thm. 2;
Cor. 4). Reach-expanding policy can raise measured
access while shrinking the long-run stock; evaluation of
portability and interoperability mandates must include
the refresh margin.
7)Participation volume is not a health metric(Thm. 4).
The marginal lister carries one negative and two positive
externalities; the regulator’s object is the three-wedge
comparison (23) (relational density against appropriabil-
ity and thickness), stratified by memory class, not listing
counts.
8)Ownership reform without feasibility infrastructure
is inert(Thm. 1(ii); Cor. 5; Thm. 6). Renaming the
owner while portabilityϕand salienceζstay low
changes neither scope nor refresh, and the incumbent

TABLE I
THE FAILURE–INSTRUMENT MATRIX. EACH ROW IS A DERIVED ASSIGNMENT:THE FAILURE IN COLUMN TWO IS NOT REPAIRED BY THE INSTRUMENTS
IN COLUMN THREE ACTING ALONE,AND IS MATCHED TO THE INSTRUMENT IN COLUMN FOUR BY THE RESULT IN COLUMN FIVE.
# Failure Not fixable by (alone) Matched instrument Source
1 Fabricated lineage performance scores; consent
badges
provenance credential (existing TEE infrastruc-
ture)
A.1 (presupposed)
2 Low fidelity; poor buyer–task–
host fit
provenance; any global score performance certification; compatibility-class
tests; sandbox and audited replay
Lem. 1; §VI-F
3 Unauthorized extraction, sale,
or use
provenance; performance scoped licenseℓ: purpose, recipient, horizon, call
budget, revocation
Def. 7
4 Unpriced subject exposure price and reputation coverages ∗ =λ+w ⋆ S /n, indexed per quality- deployment Thm. 5(i); Prop. 5(iii)
5 Refresh underinvestment on ei-
ther margin
reassigning “the owner” interior renewable claims(w ⋆ S , w⋆ P ); control and cash flow set separately Thm. 1; Cor. 3; Prop. 4
6 Long-run depletion from reach
expansion
nonrivalry intuition; access
metrics
scope haircutn ∗ ≈ 2 3 (1−λ); sequence porta- bility with coverage Thm. 2; Thm. 5(iv)
7 Behavioral pollution; obfusca-
tion equilibrium
transparency alone; compen-
sation alone
transparencyandcoverage floor jointly; rule-
based commitment
Thm. 3
8 Coverage dilution as the market
grows
share-financed compensation royalty-financed coverage (τ), reach-invariant Prop. 6(ii)
9 Over-participation and
relational harm
focal-subject consent relational-density monitoring (23); affected-party
and collective governance
Thm. 4; Cor. 6
10 Self-perpetuating de facto con-
trol
renaming the owner portabilityϕand salienceζmandates; delegation
per the feasibility map
Cor. 5; Thm. 6
maintains those conditions in equilibrium;ϕandζare
the binding policy margins.
9)The scope rule is robust; the compensation rule
is information-hungry(Thm. 5(iii)–(iv)).n ∗ sits in a
four-point band around two-thirds of the static optimum
regardless of the productivity split, so scope can be set
with an estimate ofλalone; coverage requires the full
decomposition(k S, kP ).
10)Monetary IR does not exhaust consent(A.6; Rem. 14).
For inalienable uses the constraint isℓ∈ R i(m),
not a higher royalty; and where pure efficiency logic
recommends tolerated pollution (Prop. 7(c)), that rec-
ommendation is exactly what normative scrutiny should
target rather than inherit.
C. Who implements what
The five components of Section VI-E’s constitution di-
vide cleanly across the three actors. Themarketplacecan
adopt unilaterally: quality-indexed coverage ats ∗ with rule-
based commitment (Theorem 3(iv) shows commitment is in
its own interest when(1−ν)RQ > c d); scoped licenses
and audited replay; compatibility-class evaluation; royalty
financing. Theregulatormust supply what no equilibrium
actor will: the transparency mandateT(Theorem 3(iii));
portability and salience infrastructure (Corollary 5); relational-
density monitoring and, for high-ϱclasses, participation review
(Theorem 4); scope defaults or deployment subsidies where
delegation is infeasible (Theorem 6(i)); and the inalienable-
use boundary itself.Infrastructure(TEE provenance, class-
indexed benchmarks, audit logs) is what makes the first two
contractible; its role is enabling, not substitutive: certification
serves authorization (Remark 12). The assignment explains a
pattern the matrix alone does not: the instruments that fixvisi-
blefailures (rows 1–4) are mostly marketplace-implementable,
while the instruments that fixequilibriumfailures (rows 5–10)
almost all require the regulator or a standards body. Markets
for person-linked memory self-correct their transactions, not
their dynamics.
D. The no-fusion rule
The matrix compresses into one design rule:a marketplace
should not issue a fused “memory trust score.”The model
now supplies three independent reasons for it. First,crossing
rankings: no buyer-independent scalar orders artifacts correctly
for all buyers (Lemma 1), so any global score misprices
fit. Second,direction-flipping: the information content of an
authorization badge depends on the harm technology’s sign
and the royalty structure (Proposition 5); a fused score would
hard-code one sign and mislead whenever the other obtains.
Third,regime-dependence: whether high measured coverage
signals health or a binding floor, and whether thick partici-
pation signals success or relational over-supply, depends on
parameters (Proposition 7; Theorem 4) that a scalar cannot
carry. Provenance credentials, performance and fit reports, and
permission credentials answer different questions, fail differ-
ently, and, by the results above, actively mislead when merged.
The minimal credential dimensionality claim is formalized as
a conjecture in Section IX.
VIII. MEASUREMENT, CALIBRATION,ANDEVIDENCE
A. What the model exposes
The model was written so that its primitives are measurable
rather than postulated, and Section VII showed that most of
its governance content is a comparison between measured
quantities: the productivity ratiok S/kP againstC/Ω(The-
orem 5(ii)), the three wedges of (23), the sign ofdY E/dn
in (15). A paper that ends at the theorems therefore leaves its
own design rules unusable. This section closes that gap in three
layers: a numerical companion that maps the parameter regions
(Section VIII-B); a synthetic memory economy in which every

0.0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
exposure intensity λ
10−1
100
101
refresh-productivity ratio kS/kP
strict renewable claim
s * > λ; floor self-enforcing
floor binds;
delegation to
platform infeasible
floor binds;
delegation feasible
measured
( ̂λ, ̂kS/ ̂kP)
C/Ω = 0.46
λc = 0.21
Fig. 1. The institutional parameter map. The horizontal boundary is Theo-
rem 5(ii)’s self-enforcing coverage floor evaluated at the second-best scope,
kS /kP =C/Ω = (3−
√
3)/(1 +
√
3)≈0.46, independent ofλ, because
n∗ scales with1−λ. The vertical boundary is Theorem 6(i)’s delegation
thresholdλ c = (3−
√
3)/6≈0.21. The marker is the point recovered by
the testbed of Section VIII-C.
estimand has a known ground truth, so that estimators can be
validatedand the theorems can actually fail (Sections VIII-C–
VIII-F); and pre-registered designs for platforms holding real
interaction data (Section VIII-G). The middle layer is the one
no observational study can supply: on real data one never sees
qu’s ground truth, so an estimate ofk S cannot be checked
against anything.
B. Layer 1: the parameter map
Figure 1 plots the two boundaries that decide which in-
struments a memory class needs. Above the horizontal line
the subject is a productive enough refresher that the second
best pays her above bare exposure without any authenticity
mandate; below it, the floor binds and Proposition 7’s regimes
apply. Left of the vertical line the de facto platform-controlled
regime cannot be steered to the second best with nonnegative
royalties, so scope regulation or deployment subsidies are
required. Two measured numbers place a memory class on this
map, and nothing else about the class matters for the choice of
instrument, which is the practical content of Sections VI–VII.
C. Layer 2: a synthetic memory economy
We build an environment that instantiates Definitions 1, 2,
3, 5 and 6 exactly. Subjecti’s state isω i = (ω c, ωg k(i), ωp i )
over disjoint coordinate blocks, each block an AR(1) with its
own persistence (ρ c = 0.995,ρ g = 0.97,ρ= 0.85): every
component drifts, and at different rates. Interaction generates
y=⟨ω, x⟩+νwithx∼N(0, I);subject efforteraises
the informativeness of each interaction,σ 2 ν(e) =σ 2 ν0/(1 +
aSe), andplatform effortx P raises the share of the history’s
information that extraction retains,ψ(x P ) = 1−e −aP xP . The
memory artifact is the resulting Gaussian belief; its stationary
information stock has the closed formJ ∗ jj =ψF/(1−ρ 2 j ).
Three properties make this environment the right instrument.
First, fidelity isexact: with quadratic loss,V u(ω) = 0, so
Definition 3 reduces to a variance-reduction ratio,q u = 1−
w⊤Σφw/w⊤Σ0w, computed rather than estimated. Second,
the extraction ceiling is atestrather than an assumption:
ψis a free parameter that can be pushed to the sufficient-
statistic limit. Third, demand isderived: buyers differ in
a use’s personal-loading shareχ b and in intensityA b, and
R(n), C(n), B(n)are read off the realized value distribution.
The resulting demand curve is not the uniform benchmark’s
(regressing derivedRonn(1−n)gives a negativeR 2, and
derivedRpeaks atn≈0.64rather than 1 2), so agreement
between the structural optimum and the closed forms of Sec-
tions IV–VI is informative rather than tautological. Likewiseλ
is derived, asλ 0 times the adversarial-to-buyer decision-value
ratio the environment produces.
Every result below is reported as a family rather than a
point. The parameters that were set by hand (state persistence
ρ, the dimensiond p of the personal block, the fidelity regime,
buyer-intensity dispersion, the cost ratioc S/cP , and the seed)
are perturbed, and each figure plots the resulting family. This
separates structural conclusions from calibration artifacts, and
in two cases the perturbation itself identifies the mechanism
behind a result.
D. What can fail, and what cannot
A synthetic testbed can produce three kinds of statement,
and conflating them is the standard way computational sections
overclaim. We label each result in Table II accordingly.
Anidentity checkcannot fail: it is true by construction
in the Gaussian environment, and what it verifies is the
implementation, not the theory. Proposition 1 restricted to
garblings of the subject’s own history is of this kind (extraction
there is a scalar contraction of the information matrix, so the
ordering follows from positive semi-definite monotonicity), as
is theρ 2k decay of Corollary 1. We report these because an
implementation that failed them would be wrong, not because
passing them is evidence.
Atesthas a direction in which it fails, and some of ours do.
The informative form of the ceiling is therefore not the in-class
check but its complement: an extractor that isnota garbling
of the subject’s history (one that imputes from a population
prior, say) breaches the ceiling in68%of checks, by up to
0.045in fidelity units. That is the content of Proposition 1: it
is a statement about what memory extraction cannot do, and
it fails precisely for artifacts that are not, in the definitional
sense, memory. The entanglement conjecture, the audit bound,
the depletion condition and the scope haircut are all tests in
this sense, and one of them fails outright below.
Anillustrationevaluates a closed form or an imposed rule
rather than an equilibrium. Theorem 3’s distortiond ∗ and
Proposition 5’s authorization rule are computed, not solved
for; “d ∗ = 0iffs≥λ” is then an arithmetic property of the
expression, not a finding. We keep them as consistency checks
and label them as such. What the environment does supply

TABLE II
LAYER-2RESULTS,REPORTED OVER THE PERTURBATION SWEEPS RATHER
THAN AT A SINGLE CALIBRATION. “VIOLATIONS”COUNTS STRICT
VIOLATIONS OF THE STATED INEQUALITY ACROSS THE WHOLE SWEEP.
ROWS MARKED ILLUSTRATION EVALUATE A CLOSED FORM OR AN
IMPOSED RULE RATHER THAN AN EQUILIBRIUM AND CANNOT FAIL;SEE
SECTIONVIII-D. ALL FIGURES ARE READ FROM THE COMMITTED
R E S U L T S/*.J S O N.
Target Test Result
Prop. 1
extraction ceiling
qu(φ)≤q u(ht)over
11,200 (use, budget)
pairs, in class and out
0 violations in class;
gap→3.1×10 −7
asψ→1; breached
in68%of out-of-class
checks
Cor. 1
staleness
personal-component
decay vs.ρ 2k
max error
1.6×10 −15 over
ρ∈[0.75,0.95]
Rem. 2
δis derived
ˆδacross use classes
χ∈[0,1]
8.8×range atρ=
0.85;13.8×atρ=
0.75
Lem. 3
refresh technology
fitY=η S e+η P x+
γex
R2 = 0.82;
ˆkS /ˆkP = 0.73;
γ <0at¯q= 0.81
but>0under
saturation
Conj. (Gaussian
frontier)
κ⋆ vs.χ, aligned ad-
versary, four fidelity
regimes
failsat low fidelity
(error0.38); error≈
0.36 (1−¯q);<2×
10−3 once¯q >0.99
Lem. 2
κ⋆ ≤ι optimal garbling vs. feasible identity re-
placement
0 violations; audit
overstates by65%–
91%, rising ind p
Thm. 2
depletion (15)
sign ofd ¯Q/dnat
fixed(α, τ), derived
demand
86.4%mean agree-
ment over 36 calibra-
tions,83.9%ungated;
51%worst cell
Thm. 5(ii)
coverage floor
sign(s∗ −λ)vs.
kS /kP ≷C/Ω
10 of 12 cells at the
structuralk-ratio; 8 of
12 at theestimated
one
Thm. 3(i)
pollution
ILLUSTRATION:d ∗
evaluated from the
closed form, not from
an equilibrium
consistency check
only; measured
quality pass-through
0.16per unit of
distortion
Prop. 5
selection
ILLUSTRATION:
corr(˜q,authorized)
under an imposed
authorization rule, flat
vs. indexed
flat:−0.45to−0.24;
indexed:|r| ≤0.03
throughout
there is the pass-through: each unit of distortion destroys0.16
units of realized quality, which the closed form does not say.
E. Identification results
Table II collects the results; Figures 2–6 plot each with its
perturbation family.
Proposition 1 survives 11,200 checks with no violation and
binds with equality in the sufficient-statistic limit, as stated.
Corollary 1 holds to machine precision, and the persistence
parameter is recovered exactly from fidelity decay alone
(ˆρ= 0.85000against a truth of0.85), which is the identi-
fication argument behind the class-specific staleness estimates
Section VII asks regulators to collect, and Figure 2(b) shows
the recovery is exact across the whole range of persistence
we tried, not at one calibration. Figure 2(a) makes Remark 2
quantitative: atρ= 0.85measured one-period depreciation
runs from0.032for a use loading entirely on the common
component to0.278for a purely personal one, and the spread
widens as drift rises: a13.8×range atρ= 0.75. A single
δfor “memory” is therefore not a summary of anything;
depreciation must be estimated per use class, and the same
artifact is fresh for one buyer and stale for another.
Two findings amend the paper. First, the Gaussian entan-
glement conjecture isnotan identity: it is a high-fidelity
limit, and it fails cleanly when the memory is far from the
information ceiling (Figure 3(a)). Against an adversary aligned
to the buyer’s personal loading,κ ⋆ approachesχfrom below
as the artifact becomes informative, with a maximum error of
0.38at¯q= 0.34,0.16at¯q= 0.67,9.0×10 −3 at¯q= 0.98
and6.0×10 −4 at¯q= 1.00. The convergence is first order in
the fidelity gap: a log–log fit of|κ ⋆ −χ|on1−¯qreturns a
slope of1.02, so the defensible statement is
κ⋆ aligned =χ+O(1−¯q),|κ ⋆ −χ| ≈0.36 (1−¯q).(35)
This replaces a claim we made in an earlier draft, and the
way it was produced is worth stating plainly, because it is the
kind of error a synthetic testbed invites. The first version of
this experiment separated “fidelity regimes” by the extraction
budget alone while holding the information environment at its
default, where the stationary stock sits aboveq= 0.99regard-
less: all three nominal regimes returned¯q∈[0.990,0.9997],
the error was2.2×10 −3 everywhere, and the conjecture looked
exact in every regime; it was never tested outside saturation.
Separating the regimes by the information environment instead
(the number of interactions and the observation noise, which
is what actually moves the stock) reproduces the failure at
low fidelity in two independently implemented pipelines. The
conjecture should be stated as a proposition qualified byboth
the adversary’s alignment and an information-saturation limit,
with (35) as its rate. The practical reading is more useful
than the identity would have been: the Gaussian frontier is a
good approximation exactly for the mature, heavily refreshed
artifacts that are worth trading, and a poor one for thin
memory, where an aligned adversary extracts materially less
than the personal loading share suggests.
Second, and more consequentially,κ ⋆ is sharplyadversary-
indexed. Lemma 2 holds (no violations anywhere in the
sweep), but its bound is slack by an order of magnitude for any
adversary that targets a specific attribute rather than the whole
identity: identity-replacement audits overstate entanglement by
65%to91%, because erasing the personal coordinates destroys
the entire personal block while the optimal zero-exposure
garbling need only remove one direction of it. The comparison
is only meaningful against afeasibleerasure. Withholding
the personal coordinates leaves the Schur complement of the
personal block, not the raw non-personal sub-matrix; zeroing
rows and columns instead retains more information than any
garbling can deliver, and produces spurious violations of
Lemma 2:0.117in these regimes, against0once the erasure
is made feasible. (For diagonal information matrices the two

0.00 0.25 0.50 0.75 1.00
personal-loading share χ of the use
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
0.45
measured depreciation ̂δ
ρ = 0.75
ρ = 0.8
ρ = 0.85
ρ = 0.9
ρ = 0.95
(a) One δ does not describe a class
0.75 0.80 0.85 0.90 0.95
true persistence ρ
0.75
0.80
0.85
0.90
0.95
̂ρ from fidelity decay alone
identity line
max error
1.55 × 10−15
(b) Staleness identifies ρ
Fig. 2. Staleness. (a) Measured one-period depreciation against the use’s personal-loading shareχ, for five values of the state persistenceρ: a singleδ
describes a memory class only if every buyer loads identically on the personal component, and the spread widens as drift rises. (b) Persistence recovered
from fidelity decay alone, against its true value; the maximum error over the five calibrations is1.4×10 −15.
0.0 0.2 0.4 0.6 0.8 1.0
personal-loading share χ
0.0
0.2
0.4
0.6
0.8
1.0
κ ⋆ , aligned adversary
 κ⋆ =χ
(a) The Gaussian frontier is exact
low fidelity
mid fidelity
high fidelity
0.0 0.2 0.4 0.6 0.8 1.0
personal-loading share χ
0
20
40
60
80
100
audit overstatement (%)
(b) More identity dimensions, worse audits
dp = 3  (mean 65%)
dp = 6  (mean 84%)
dp = 10  (mean 91%)
Fig. 3. Entanglement. (a) Against an adversary aligned with the buyer’s personal loading,κ ⋆ =χon the diagonal in every fidelity regime: the three curves
coincide, which is the result. (b) The gap between an identity-replacement audit and the true entanglement, as a percentage of the audit, againstχand across
the dimensiond p of the personal block. The overstatement rises withd p because a targeted garbling has more directions to preserve while naive erasure
destroys them all.
coincide, which is why nothing computed from the closed-
form stationary stock is affected.) The perturbation identifies
the mechanism rather than merely sizing the gap (Figure 3(b)):
the overstatement rises monotonically in the dimension of the
personal block (65%atd p = 3,84%atd p = 6,91%at
dp = 10), which is what the garbling program predicts, since
each additional identity dimension is one more direction a
targeted release can keep. Richer personal state makes naive
erasure worse, not safer. Remark 4’s caution that audits are
an upper bound is correct but far too mild. The operational
implication is thatκ ⋆ must be reported against anamed
adversary class; an unqualifiedκ ⋆ near1, read off an identity-
replacement audit, will justify institutional pessimism (“no
privacy technology can improve the frontier”) in classes where
a targeted garbling would in fact retain most of the buyer value.
A third finding concerns the refresh technology itself, and
it is a finding about theestimatorrather than about the
technology. At the calibration where the refresh margin is
interior (¯q= 0.81) the fitted interaction termγisnegative,
about12%of the linear terms’ magnitude, because the true
technology is concave in the multiplicative information index
ψ(x)F(e), which a linear-plus-interaction specification reads
as mild substitutability. Assumption 4’s restrictionγ≥0is
therefore not innocuous as a description, though it is harmless
as a benchmark: every headline result is stated for the additive
caseγ= 0, which the measurement supports as the right
neutral specification. The assumption should be relaxed to
allow either sign, and the reason is sharper than a single sign.
Re-run at the information-rich calibration, where steady-state
fidelity exceeds0.99, the same regression attenuatesˆη S by a
factor of48andγflips positive. The sign of the interaction
term is not a property of the refresh technology at all; it is

0.2 0.4 0.6 0.8 1.0
license reach n
0.55
0.60
0.65
0.70
0.75
0.80
steady-state stock ̄Q α = 0.55, τ = 0.0
α = 0.35, τ = 0.3
α = 0.0, τ = 0.6
α = 0.8, τ = 0.0
predicted
turning region
(a) The stock turns over at interior reach
α = 0.0
τ = 0.6
α = 0.35
τ = 0.3
α = 0.55
τ = 0.0
α = 0.8
τ = 0.0
cash-flow rights bundle
50
60
70
80
90
100
sign agreement (%)
9 calibrations per bundle
(b) Stable across rights and seeds
cell mean
Fig. 4. Depletion. (a) Steady-state stock against license reach at four fixed cash-flow bundles, one representative calibration: the stock rises, turns over at an
interior reach, and falls; that is Theorem 2’s mechanism, with the region where the predicted derivative changes sign shaded. (b) Sign agreement between the
predicted and realized derivative, over the interior region where the prediction is non-vacuous, for each bundle across nine calibrations (three dispersions×
three seeds).
0.2 0.3 0.4 0.5 0.6
measured exposure ̂λ
0.6
0.7
0.8
0.9
1.0
haircut n * /nW
uniform-demand band
(a) A live subject margin deepens the haircut
subject margin live
subject margin dead
0.3 0.6 1
buyer-intensity dispersion
0.6
0.7
0.8
0.9
1.0
haircut n * /nW
0.93
0.82
0.71
(b) Deeper where demand is dispersed
Fig. 5. The scope haircut. (a)n ∗/nW against measured exposure, separating calibrations in which the subject’s refresh margin is live at the optimum from
those in which it is not; the uniform-demand band of Theorem 5(iv) is shaded. (b) The same haircuts grouped by buyer-intensity dispersion, live margins
only: the haircut deepens as demand becomes more disperse, and the uniform band is approached only at the dispersed end.
a property of where on the saturation curve the economy is
sitting when the analyst measures it.
The same attenuation contaminates the productivity ratio the
paper’s institutional prescriptions turn on. The environment
implements a structural ratio(a 2 S/cS)/(a2 P /cP ); Lemma 3’s
regression recoversˆη2/c, and these are not the same number.
Across the cost sweep the estimated ratio is uniformly3.80×
below the structural one (0.24against0.93,0.73against2.78,
2.44against9.26), with a strikingly constant attenuation factor,
which is itself a usable diagnostic. Because the ratio enters
Theorem 5(ii) through a comparison withC/Ω, the bias is not
innocuous: the theorem’s prescription is recovered in 10 of 12
cells at the structural ratio but only 8 of 12 at the estimated
one, and every one of the extra failures is a case where the
estimate falls below a threshold the truth clears. This qualifies
the section’s own claim: what the testbed validates is that
the paper’s estimators are consistentat an interior operating
point; it also shows that they are biased toward understating
the subject’s refresh productivity as fidelity rises, which would
bias real institutional advice toward too little coverage. Any
empirical estimate of(k S, kP )must be reported together with
the fidelity level at which it was taken, or a saturated system
will look like one with no refresh margin at all.
F . Equilibrium results
The depletion condition (15) is the paper’s headline and
the test most able to fail, since demand here is not the
uniform benchmark’s. Theorem 2 requires that scope be swept
at fixed cash-flow rights(α, τ), and Proposition 6(ii) makes
this essential, since fixed rights put coverage on a declining
path. Sweeping scope that way reproduces the mechanism
directly (Figure 4(a)): the steady-state stock rises with reach,
turns over at an interior scope, and falls, with the turning

0.0 0.2 0.4 0.6 0.8 1.0
deployment scale D
0.0
0.2
0.4
0.6
0.8
equilibrium distortion d *
all s = λ curves lie on zero
darker: costlier distortion cd
(a) Scale pollutes unless covered
s = 0
s = 0.5λ
s = λ
30 40 50 60 70 80 90
authorization rate (%)
−0.5
−0.4
−0.3
−0.2
−0.1
0.0
0.1
corr( ̃q, authorized)
(b) Indexation shuts selection down
flat royalty
quality-indexed royalty
Fig. 6. Pollution and selection. (a) Equilibrium distortion against deployment scale, for three coverage levels and three distortion costs: distortion grows with
scale whenever coverage falls short of exposure and is identically zero once it does not. (b) The correlation between fidelity and authorization, against the
authorization rate, under a flat and under a quality-indexed royalty.
point moving across rights bundles. Over 36 calibrations (four
bundles×three dispersions×three seeds) the predicted
and realized signs ofd ¯Q/dnagree on86.4%of the interior
points where the predicted derivative is non-negligible, and on
83.9%unconditionally, with a worst cell of51%(Figure 4(b)).
The gate matters and we state it: “non-negligible” means a
predicted derivative at least5%of the cell’s largest, which
retains94%of the live points. An earlier version gated on the
upper half of|pred|within each cell, which is a rank rule (it
discards half of every cell whatever the magnitudes are), and
returned98.9%. That figure was an artifact of the gate, not a
property of the mechanism, and the honest number is the low-
to-mid eighties either way. The condition survives a demand
curve it was not derived for, and survives it at every seed,
but it is a mechanism that predicts the sign of a derivative
correctly five times in six, not nineteen times in twenty.
Theorem 5(ii)’s coverage floor is correct in 10 of 12 cells
of aλ×(k S/kP )sweep when the productivity ratio is the
structural one, and in 8 of 12 when it is the ratio an analyst
would estimate; the difference is the attenuation discussed
above. Both failures in the structural case occur whereC/Ω
is near or above1, i.e. where exposure consumes most of
the social stake and the comparison is delicate, which is a
boundary the theorem should state.
Theorem 5(iv)’s scope haircut requires the most substantial
amendment. Under derived demand the haircut is real but
its magnitude is not the uniform band:n ∗/nW = 0.83on
average over 36 calibrations, ranging0.69–0.98. Itsexistence,
however, is sharply conditional in a way the closed form does
not say. Figure 5(a) shows the haircut appearing exactly when
the subject’s refresh margin is live, and vanishing (mean0.99,
and exactly1.000in nine of fourteen such cells) whenever the
optimum leavesw S ≤0. Because the amendment turns on a
binary classification, it is worth saying that the classification
is not delicate: the split is structural (w S >0at the optimum)
rather than a threshold on a discretized effort grid, and every
cell classified as live sits at least29grid steps (an effort
of0.22) away from the corner. Nothing here is knife-edge
in the argmax. This is the correct statement of the result
and it is stronger than the band:the second best withholds
reach only to protect a refresh margin that exists, so the
haircut is not a universal constant but the shadow price of
a live subject stake. The perturbation also says what the
magnitude depends on (Figure 5(b)): the haircut deepens
monotonically in buyer-intensity dispersion (0.93,0.82,0.71
across the three dispersion levels), and the uniform-demand
band is approached only at the dispersed end, which is the
sense in which[0.63,0.67]is a special case rather than a
constant. Where the platform is the overwhelmingly dominant
refresher, the static and dynamic scope rules coincide, and
the case for restricting reach on depletion grounds disappears
with the margin it was protecting. Theorem 5(iv) should
be restated directionally, with[0.63,0.67]presented as the
uniform-demand special case it is.
Finally, Theorem 3(i) and Proposition 5 are illustrated rather
than tested, and we mark them so (Figure 6). The distortiond ∗
is evaluated from the theorem’s own closed form rather than
solved for as an equilibrium of the subject’s distorted problem,
so “distortion is zero exactly when coverage reaches the floor,
and rises linearly in deployment scale otherwise” is a property
of that expression and holds at every distortion cost by
construction. What the environment adds is the consequence:
feedingd ∗ back through the synthetic economy, each unit of
distortion costs0.16units of realized quality, so the pollution
channel is economically material and not merely formal.
Solving the distorted equilibrium properly is the obvious
next iteration of the testbed. The selection direction flips as
predicted with the royalty structure and stays flipped across
the whole range of authorization rates: under a flat royalty the
correlation between fidelity and authorization runs from−0.45
to−0.24, while under quality-indexed royalties it never leaves
±0.03. Proposition 5(iii) is thus not a knife-edge: indexation

shuts selection down cleanly, whatever the royalty level.
G. Layer 3: designs for platforms
Layer 2 validates estimators; it cannot establish external
magnitudes. Three designs transfer directly to a platform
holding real interaction data, and each is stated so that a null
result is interpretable. (i)Refresh decomposition: randomize
prompts for subject feedback (corrections, confirmations, pref-
erence edits) against engineering interventions (consolidation
cadence, retrieval budget) in a factorial design; regress held-
out task performance on both arms to recover(ˆη S,ˆηP ,ˆγ)
and hencek S/kP , reporting the fidelity level at which the
estimate is taken. (ii)Scope randomization: randomize license
reachnacross matched memory cohorts at fixed(α, τ)and
track subsequent refresh flow, testing (15) directly; the de-
sign must hold cash-flow rights fixed rather than coverage,
or the mechanism is assumed away. (iii)Royalty-structure
randomization: assign flat versus quality-indexed royalties
across subject cohorts and compare the fidelity composition
of the authorized pools, testing Proposition 5. For (23) the
three wedges are separately measurable: relational density
from within-class predictive leakage onto non-listing peers,
appropriability from the coverage share, and thickness from
the price response to market size. Theorem 4’s direction is
thus an empirical comparison, not a presumption. Each design
should pre-register the estimand and the sign that would falsify
the corresponding result.
H. Threats, scope, and replication
The Gaussian-linear environment buys exactness at the cost
of realism: real memory is not a belief over a linear-Gaussian
state, real extraction is not a precision-scaling operator, and
real adversaries are not linear functionals. What Layer 2
establishes is therefore internal: that the paper’s estimators
recover what they claim to recover when ground truth exists,
and that its theorems are not artifacts of the uniform-demand
parametrization. The perturbation sweeps let us say which is
which. Four conclusions are stable across every parameter
we varied and are properties of the class of environments
rather than of this one: the extraction ceiling (a data-processing
inequality), theρ 2k staleness law (any AR(1) state), the sign
of the depletion condition, and the selection reversal. Three
are directional but not numerical: the haircut always exists
when the subject margin is live and always vanishes when it
is not, but its depth moves with demand dispersion; the audit
overstatement is always large but runs from65%to91%with
the dimension of identity; andδ’s spread across use classes is
always wide but scales with drift. Point magnitudes should be
read as demonstrations that these quantities are large enough
to matter, not as estimates of their real-world values.
One conclusion is explicitlynotstable, and we flag it be-
cause the instability is the finding: the Gaussian entanglement
frontier holds only as the memory approaches the information
ceiling, with an error first order in the fidelity gap (35). Any
statement of that result that does not carry a fidelity qualifier
is false in thin-memory regimes. The episode also carries a
methodological point that generalizes past this paper. Two of
the errors we found in our own first pass had the same shape:
a “regime” sweep that varied a parameter which does not in
fact move the quantity being regimed, and a sign test gated
by a rank rule rather than an absolute threshold. Both made a
result look stronger than it was, and neither was visible from
the output alone, but only from asking what the experiment
could have returned had the theory been false. A synthetic
testbed makes that question answerable, and Section VIII-D
exists so that a reader can check it row by row rather than
taking our word for it. A companion exercise replicating
the identification tests on LLM agents with genuine memory
pipelines is the natural external-validity check; its design is
fixed by the interfaces used here.
All experiments, the environment, and the figure code are
in the replication package; every number in Table II and every
panel of Figures 1–6 is regenerated by three scripts at a fixed
seed, with all reported figures read from the committed result
files rather than transcribed. The full sweep runs in about
five minutes on one core. The calibration is disclosed rather
than implicit: the equilibrium and robustness experiments
use a hand-selected operating point (m= 3,σ ν0 = 2.4,
cS =c P = 0.02) chosen so that both efforts are interior, since
at unit costs every equilibrium effort corners at zero and every
equilibrium test is vacuous. One caveat for replicators: the
welfare optimum is an argmax over segments that are locally
flat, so platform-level differences of order10 −5 in ¯Qcan move
summary figures by one to three percentage points, so compare
with a tolerance rather than bitwise.
IX. DISCUSSION ANDLIMITATIONS
The identification strategy that gives this paper its force
is also the source of most of its limits. By granting perfect
provenance (Assumption 1) and complete information (As-
sumption 2) we bought the right to say that every failure here
survives the success of the infrastructure now being built. What
we gave up is any claim about the failures that arisebecause
that infrastructure is imperfect: misattributed lineage, forged
effort attestations, buyers who cannot evaluate what they are
buying. Those are real and, on current evidence, quantitatively
large. They are simply not what this paper is about, and a
reader should not treat our silence on them as a judgment
that they are second order. The same holds for the direction
of our conclusions: because the benchmark is generous to the
market, our failure results are, if anything, conservative, while
our efficiency results are not.
The most consequential simplification is the scalarλ. Com-
pressing exposure into one number that enters utility linearly
makes the rights problem tractable and makes the ought–
is comparison of Proposition 4 reduce to two measurable
quantities. It also assumes what a great deal of the surrounding
normative literature denies: that the harm of being represented,
deployed, and inferred from is the kind of thing that trades
against money at some rate. Dignitary harm, chilling effects
on what a person is willing to tell a system that remembers,
and the distinct injury of beingaccuratelyknown by a party

one did not choose are not obviously commensurable with a
royalty. We have handled this inside the model in the only
way a transferable-utility benchmark permits: inalienable uses
enter as hard constraints rather than as priced quantities, and
Remark 14 flags the one place where pure efficiency logic
recommends tolerating subject distortion as a result to be
scrutinized rather than adopted. That is a containment strategy,
not a solution. A model in which some uses are lexically
prior to compensation would change the second-best bundle
of Theorem 5, and we do not know in which direction.
Three structural restrictions bound the environment. First,
there is one platform: the portability results (Theorem 1(ii)
and Corollary 5) say that a monopolist will not supplyϕ
andζvoluntarily, which is a statement about a monopo-
list. Whether competition between platforms substitutes for a
portability mandate is genuinely open, and it is the extension
we would run first: the na¨ıve argument that competition forces
portability runs into the observation that lowϕraises every
incumbent’s stake symmetrically, so the incentive to withhold
it is common rather than strategic. Second, the “platform” is a
single investor, whereas in practice the engineering margin
is supplied by a model provider, an application developer,
and an infrastructure operator whose contracts with each other
are themselves incomplete; Theorem 1 is a two-investor result
and the budget-balance obstruction only sharpens with more
parties, but theallocationquestion does not have an obvious
extension. Third, memory has one subject: Definition 2’s
person-linkage condition is stated for a single individual, and
Section III excludes multi-subject artifacts by construction.
This is the exclusion we are least comfortable with, because
most real interaction history describes more than one person:
a conversation, a household, a clinical encounter. Theorem 4
supplies the machinery for the externality (relational leakage
onto non-listing peers is precisely the third wedge) but not the
rights allocation, and no single subject’s consent can authorize
an artifact whose subject is plural.
Two modelling choices are assumptions we would like to
see tested rather than limitations we can bound. We assume
exposure rises with fidelity: an accurate memory is a more
dangerous one. Remark 10 shows that the opposite case, harm
frommisrepresentation, adds a term that pushes the subject’s
refresh incentive up rather than down, which would weaken the
depletion mechanism without reversing it, but the two harms
plainly coexist and their relative magnitude is an empirical
matter that our sign restriction settles by assumption. The
second-best bundle of Section VI is also computed under
commitment (Assumption 6). Without it the coverage floor
is renegotiation-proof only in the region where Theorem 5(ii)
makes it self-enforcing, which is exactly the region where the
subject is a productive refresher; the commitment assumption
is therefore doing real work outside that region, and the
delegation results of Section VI-D are a partial rather than
a complete substitute for it.
Finally, three propositions remain conjectural in different
senses. The Gaussian entanglement frontier is now understood,
not assumed: the testbed established thatκ ⋆ =χis an
information-saturation limit with error first order in the fidelity
gap (35). What remains open is whether that rate survives
outside the Gaussian-linear environment, where “one direction
of the personal block” has no clean meaning; we would expect
the qualitative conclusion (targeted garbling dominates identity
replacement, increasingly so in the dimension of identity) to
be robust, and the constant not to be. Sophistication selection,
the conjecture that the subjects most able to evaluate a rights
bundle are also those with the most valuable memory, would if
true make Proposition 5’s composition effect worse than we re-
port and is straightforwardly testable on any live marketplace.
And the no-fusion rule of Section VII-D establishes that prove-
nance, performance, and permission must not be collapsed into
one score; it does not establish that three credentials suffice.
Lemma 1 rules out one dimension, notk, and we do not have
a lower bound on credential dimensionality. Section VIII-H
states the separate question of what the synthetic testbed can
and cannot license; the LLM-agent replication described there
is the natural next external-validity check.
It is worth naming what would overturn the paper rather than
merely qualify it. The entire ought–is apparatus rests on the
subject’s refresh margin being live: onk S being non-trivial in
real systems. If the empirical answer is that engineering effort
dominates and users contribute almost nothing to the continued
validity of their own memory, then Theorem 2’s depletion
channel is vacuous, the scope haircut vanishes with the margin
it protects (which is exactly what our own dead-margin cells
show), and platform ownership becomes not merely the de
facto arrangement but the efficient one. We do not believe
that is the world we are in, and Section VIII-G’s first design
is built to find out. But it is the finding that would falsify us,
and it is measurable now.
X. CONCLUSION
Provenance is necessary infrastructure, but it is not a
complete market institution. Underperfectprovenance and
complete information (the world the builders of memory mar-
ketplaces are trying to reach, granted here in full), the market
for personalized AI memory still fails, and it fails in structured,
identifiable, correctable ways. Verified production effort does
not imply decision value. No budget-balanced assignment of
cash-flow rights makes both co-producers residual claimants.
Widening reach can raise access today and shrink the stock
tomorrow. Audits that replace a person’s identity overstate how
entangled the artifact really is, by more the richer that identity
becomes. None of these is a verification failure, and none is
repaired by better attestation.
Behind all of them is one mechanism: use can be non-rival
while refresh is relationally supplied. Copying a memory costs
nothing; keeping it true requires the continued participation of
the person it describes, who bears exposure from every deploy-
ment. An asset with a nonrival use and a rival maintenance
technology does not behave like data, and the institutions that
work for data do not transfer to it.
That mechanism also resolves the public argument this
paper took as its organizing question. Memoryoughtto belong

to its subject; memoryisheld by platforms. Both positions
are right about what they see and both are answers to the
wrong question, because they are twin corners of one rights
space and each extinguishes a different side of the asset’s
production: whoever does not own supplies no refresh. The
efficient arrangement is interior, the de facto corner is self-
perpetuating through precisely the parameters (portability and
salience) that determine whether the normative corner is even
reachable, and reform that renames the owner while leaving
those parameters in place changes neither scope nor refresh.
The regulatory question is not who owns the memory but what
claim structure the subject holds, and whether the conditions
for exercising it exist.
What follows from that is buildable now: credentials that
keep provenance, performance, and permission separate rather
than fusing them into a single trust score; compensation in-
dexed to measured fidelity rather than flat, which is what shuts
down adverse selection into authorization; licenses scoped
by deployment class rather than sold outright; renewable
rather than perpetual claims, because an asset that must be
maintained cannot be alienated once; staleness reported per
use class, since the same artifact is fresh for one buyer
and stale for another; entanglement reported against a named
adversary rather than as an unqualified number; and portability
and salience treated as mandates rather than as features an
incumbent might choose to supply. Each of these carries a
theorem pointer in Section VII, and each is cheaper to require
before the asset class matures than after.
That timing is the practical point: in the 23andMe
bankruptcy, deletion rights over genetic data derived from mil-
lions of people were negotiated by state attorneys general only
after the asset had entered the estate. Personalized memory
is on the same trajectory and is harder in two ways: it is
continuously re-created rather than collected once, and the
person it describes keeps producing it. The institutions are
cheap to specify today and expensive to retrofit; the window
is open now.
APPENDIXA
PROOF OFTHEOREM1
Part (i).Work in the additive benchmark of Lemma 3;
the argument forγ̸= 0is identical because the planner’s
problem replaces both stakes byΩin the same system. Given
stakes(w S, wP ), the effort subgame has first-order conditions
cSe=w SηS andc P x=w P ηP , soe E =η SwS/cS andx E =
ηP wP /cP . The planner maximizesΩY−c Se2/2−c P x2/2,
whose first-order conditions arec Se= Ωη S andc P x= Ωη P .
Sinceη S, ηP >0and both problems are strictly concave in
own effort,e E =e F Bif and only ifw S = Ω, andx E =x F B
if and only ifw P = Ω. First-best refresh on both margins
therefore requiresw S =w P = Ω, hencew S +w P = 2Ω.
Ex post budget balance with no external subsidy restricts
the bundle to allocate the realized private cash flow and
the monetizable exposure, so by (8)–(10) the stakes satisfy
wS +wP =T= Ω−C. Because buyer surplus is nonnegative,
C≥0and thereforeT≤Ω<2ΩwheneverΩ>0, which the
assumption of a strictly positive first best guarantees. The two
requirements are incompatible, and the conclusion does not
depend on how the transferFis set, sinceFmoves rents and
not marginal claims. Perfect price discrimination is the tightest
case: it setsC= 0and still leavesw S +w P = Ω<2Ω.
Any scalar owner is the special casew S ∈ {0, T}, so
ownership assignment cannot restore first best either. The
result is Holmstr¨om-type team moral hazard with one memory-
specific amplification: the planner’s weightΩcontains buyer
surplus that no budget-balanced private bundle appropriates,
so the wedge is at leastCeven before any incentive conflict
between the parties.
Part (ii).Fix(α, τ)and write bQ(n) = (1−δ)Q t +Y E(n)
withY E =k SwS(n)+kP wP (n). Suppose the platform names
scope at stage 2, anticipating stage-3 play. Its objective is
πP (n) =w P (n) bQ(n)−c P (xE)2/2withx E =η P wP /cP .
Differentiating,
π′ P =w ′ P bQ+w P  kSw′ S +k P w′ P  −c P xE dxE dn
=w ′ P bQ+k SwP w′ S,
becausec P xE(dxE/dn) =k P wP w′ P cancels the own-effort
term in bQ′. This is an envelope argument: the platform’s own
effort is already optimal, so only thecrosseffect of scope on
the subject’s effort survives. The symmetric computation for
a subject-controlled scope givesπ ′ S =w ′ S bQ+k P wSw′ P . An
interior scope therefore solves
w′ P bQ+k SwP w′ S = 0orw ′ S bQ+k P wSw′ P = 0(36)
according to who controls it. The two conditions coincide at
a commonnonly if bQ(w ′ P −w ′ S) =k P wSw′ P −k SwP w′ S, a
single equation in the primitives, so they differ on a set of full
measure in(α, τ, λ, kS, kP ). The corner casesα∈ {0,1}are
handled by evaluating (36) with the corresponding stake set to
its bound, which removes one term without equating the two
conditions.
For the sharper statement, specialize to the fixed-stock
benchmark of Proposition 2, where bQis a constant and the
two conditions reduce tow ′ P = 0andw ′ S = 0. Withτ= 0and
0< α <1these given P = 1/2andn S = [1−λ/α] [0,1]/2.
Varyingαmovesn S but leavesn P at1/2, while changing the
identity of the controller moves scope at fixedα. Cash-flow
rights and scope control therefore act on different margins and
neither substitutes for the other.
Two scope conditions of the theorem’s proof are worth
recording as limits of its reach. It excludes only budget-
balanced implementations that operate through marginal
claims on realized refresh. Verifiable effort, an external subsidy
financed outside the pair, or a performance contract written on
a signal other thanYall enlarge the domain and can restore
first best; none of them is available under Assumption 1 alone,
which verifies lineage rather than effort.

APPENDIXB
PROOF OFTHEOREM4(II)–(IV)
Throughout,Gdenotes the participation mass at the pre-
vailing threshold,gits density, andP( ˆλ)the marginal re-
lational harm defined in the statement, normalized so that
d
dˆλ

Λ(ϱ)G(ˆλ)¯λnl(ˆλ)˜qD  =g( ˆλ) Λ(ϱ)P(ˆλ).
Part (ii).Differentiating the welfare functional in part (iv)
of the statement,
W ′(ˆλ) =g( ˆλ) h vΘ(G)− ˆλ+vΘ ′(G)G−Λ(ϱ)P i ,(37)
where the third term collects the effect of the marginal entrant
on every inframarginal participant’s thickness and the fourth
collects the relational harm she imposes on non-listing peers.
Setting the bracket to zero gives (22). The private cutoff
instead equates the lister’s own compensated benefit to her
own exposure, ˆλ=svΘ(G), which is (21).
To compare the two fixed points rather than the two condi-
tions, define the excess functions
ΦM (ˆλ) :=svΘ(G( ˆλ))− ˆλ,Φ W (ˆλ) :=W ′(ˆλ)/g(ˆλ),
whose zeros are the market and planner thresholds. Subtract-
ing,
ΦM (ˆλ)−Φ W (ˆλ) = Λ(ϱ)P−(1−s)vΘ−vΘ ′(G)G(38)
at every ˆλ, so the right side is positive exactly when (23) holds.
Assume the regularity condition
svΘ ′(G(ˆλ))g( ˆλ)<1for all ˆλin the support ofG,(39)
which is the negation of the multiplicity condition in part (i)
and makesΦ M strictly decreasing, and assume the analogous
bound forΦ W . Each excess function then crosses zero at
most once and from above, so the pointwise ordering in (38)
transfers to the fixed points: ˆλ∗ > ˆλW if and only if (23)
holds. Without (39) the market has multiple thresholds, and
the comparison should be read equilibrium by equilibrium or
after the global-games selection of part (i).
Part (iii).By Definition 10, thickness enters throughΘ =
Ψ(M)withΨ ′(M) = ¯ψ/(M ¯ψσ 2 0 + 1)2, soΨ ′(M)→0as
M→ ∞andΘconverges to a finite ceilingΘ ∞. Hence
vΘ′(G)G→0along any sequence of thickening markets,
while(1−s)vΘ→(1−s)vΘ ∞, which vanishes as coverage
approaches full appropriation. The left side of (23) does not
attenuate: forϱ >0and non-degenerate ¯λnl there isP >0
withΛ(ϱ)P≥Λ(ϱ)P >0uniformly, because the correlation
that generates leakage is a property of the class rather than
of its size. Therefore for everyϱ >0and everyssufficiently
close to one there is a finite thickness beyond which (23)
holds, and every further lister is socially excessive. The naive-
participation statement follows by noting that a subject with
salienceζ <1applies the cutoffζλ i < λi, which shifts ˆλ∗
to the right, whileWcontinues to be evaluated at the trueλ i,
so the wedge in (38) widens at unchanged welfare weights.
Part (iv).Non-monotonicity is immediate from (37): near
ˆλ= 0the bracket isvΘ(0)−Λ(ϱ)P(0), which is positive
whenever thickness value dominates leakage at the bottom of
the exposure distribution, and the bracket is strictly decreasing
under the regularity condition, soWrises and then falls once
(23) binds. For the formation statement, integrate (37) from
the no-market point, at whichW(0) = 0:
W( ˆλ∗) =
Z ˆλ∗
0
h
vΘ(G)−ℓ+vΘ ′(G)G−Λ(ϱ)P i g(ℓ)dℓ.
V oluntary formation is welfare-negative precisely when this
integral is negative, which occurs when the bracket is negative
over ag-weighted majority of the participating range. Three
sufficient configurations follow directly. First,Λ(ϱ)large
enough thatΛ(ϱ)P(0)> vΘ(0)makes the bracket negative
from the start. Second, mass ofGconcentrated at highℓmakes
−ℓdominate over most of the range. Third, a large naive
share raises ˆλ∗ into the region where the bracket has already
turned negative. In each case marginal growth subsidies reduce
welfare. The reason the conclusion can contradict participants’
revealed preference is structural rather than behavioral: rela-
tional externalities fall on parties who never chose, and naive
participation is not informed revelation.
APPENDIXC
PROOF OFTHEOREM5(III)–(IV)
Work in the uniform benchmarkR(n) =n(1−n),C(n) =
n2/2,B(n) =n−n 2/2withu S =u P = 0, and writem:=
1−λfor the static welfare scope, so that
T(n) =n(m−n),Ω(n) = n(2m−n) 2 , C= Ω−T.
(40)
Both are positive onn∈(0, m), which is the active region.
By Theorem 5(i) optimal coverage implements Corollary 3’s
profile, so withk S =a,k P =bthe concentrated objective is
W(n) = max w∈[0,T] V(n, w)with
V(n, w) = Ω

aw+b(T−w)

− aw2 2 − b(T−w) 2 2 ,
which is strictly concave inwwith unconstrained maximizer
wunc = [(a−b)Ω +bT]/(a+b), sow ⋆ S = Proj [0,T] wunc
as claimed. Writeκ:=a/b. Sincew unc ≥0is equivalent to
κ≥C/Ωandw unc ≤Ttoκ≤Ω/C, the stake is interior
exactly on
n
2m−n ≤κ≤ 2m−n n ,(41)
usingC/Ω =n/(2m−n)from (40). This is the same
inequality as the self-enforcing floor (28), which is why parts
(ii) and (iv) are two readings of one condition.
Interior branch.Substitutingw unc intoVand simplifying,
Wint(n) = n2 8(a+b) h (a2 +b 2)(2m−n) 2
+ 2ab

2m2 −4mn+n 2i , (42)
a quartic innvanishing atn= 0. Differentiating and dividing
by the positive factorn(a+b)/2,
W ′ int(n)∝n 2 −3mn+ 2m 2θ(κ),
θ(κ) := κ2 +κ+ 1 (κ+ 1) 2 . (43)

The quadratic in (43) opens upward with rootsn ± = m 2  3±√
9−8θ

. Becauseθ(κ)∈[3/4,1)for allκ >0, with
the minimum atκ= 1, we have
√
9−8θ∈(1,
√
3 ]
and thereforen + ≥2m > m, which is infeasible, while
n− ∈[ (3− √ 3)m/2, m). HenceWint is strictly increasing on
(0, n−)and strictly decreasing on(n −, m), so it is unimodal
with the unique interior maximizern −. Settingκ= 1gives
θ= 3/4,
Wint(n) = k 4 n2(m−n)(3m−n), n − = 3−
√
3
2 m,
which is part (iii). Optimal coverage follows from (27): at
κ= 1the stake isw ⋆ S =T /2, sos ∗ =λ+T /(2n) =λ+
(m−n)/2, and evaluating atn − givess ∗ =λ+
√
3−1
4 m.
Finallym/2<(3−
√
3)m/2< mplacesn ∗ strictly between
the subject-corner scope and the static welfare scope.
Cornered branch.If the projection binds, one stake is
zero and the other isT; writek j for the productive party’s
coefficient. ThenY E =k jTand the effort cost isk jT 2/2, so
Wcor(n) =k j
h
ΩT− T 2 2 i = kj m 2 n2(m−n),
using (40). Its derivative is proportional ton(2m−3n), so
Wcor is unimodal on(0, m)with maximizern= 2 3 m, which
is part (iv)’s polar case.
The band is exact and attained.The two branches are not
alternatives to be compared globally, since (41) determines
which one is operative at eachn, and the switch points
depend onκ. Evaluate (41) atn= 2 3 m: the bounds are1/2
and2. Hence forκ∈(1/2,2)the stake is interior at the
cornered branch’s own maximizer, so the operative solution
is the interior one; and forκ≤1/2orκ≥2the projection
binds there and the operative solution is the cornered one. The
two descriptions agree at the boundary: atκ= 1/2(and by
symmetry atκ= 2) we getθ= 7/9,
√
9−8θ= 5/3and
n− = 2 3 m, so the concentrated program and its maximizer are
continuous inκ. Collecting,
n∗
1−λ =
( 1
2

3−
p
9−8θ(κ)

, 1 2 ≤κ≤2,
2
3 ,otherwise,
(44)
and sinceθranges over[3/4,7/9]on[1/2,2], the ratio ranges
over
 3− √ 3
2 , 2 3  , attaining its minimum atκ= 1and its
maximum at everyκ /∈(1/2,2). This proves (30) as an
exact and attained band rather than a numerical finding, and it
supersedes the regularity condition under which the theorem
was originally stated: the concentrated program is unimodal on
(0,1−λ)for every productivity ratio, so no quasiconcavity
assumption is needed. The monotonicity inλis immediate,
becauseλenters (44) only through the factorm= 1−λ.
The economic content of (44) is that the haircut is almost
insensitive towhorefreshes and sensitive only tothatsomeone
does. The ratio moves by less than four percentage points
across the entire range of productivity ratios, which is why
Remark 13’s claim about estimation requirements holds: an
analyst who knows onlyλcan set scope nearly optimally,
whereas coverage requires the split.
APPENDIXD
PROOF OFPROPOSITION7
On the polluted regions < λthe aware subject distorts by
d∗ = (λ−s)nQ/c d from Theorem 3(i), and receipts are scaled
by effective quality˜q(s) = 1−d ∗(s), so the objective (26)
becomes
W −(n, s) = ˜q(s) Ω(n)YE(s)− kS w2 S 2 − kP w2 P 2 ,
with˜q′(s) =nQ/c d >0, while fors≥λwe have˜q≡1and
W + =W E. The objective is continuous ats=λand kinked
there. Using∂w S/∂s=n,∂w P /∂s=−nand∂Y E/∂s=
n(kS −k P ), and evaluating ats=λwherew S = 0,w P =T
andY E =k P T,
∂W
∂s

s=λ+
=n

(kS −k P )Ω +k P T

=n(k S +k P )w unc,
(45)
∂W
∂s

s=λ−
=n
h
(kS −k P )Ω +k P T+ Q cd Ωk P T i .(46)
The extra term in (46) is the pollution-relief value of raising
coverage: a marginal increase inslowers the distortion and
so raises˜q, which is worth˜q ′ΩY E = (nQ/cd)ΩkP T.
Regime (a) follows from (45): the derivative from above is
positive, so the optimum lies strictly inside the no-pollution re-
gion, exactly whenw unc >0, which by (41) isk S/kP > n/a2
witha 2 = 2−2λ−n= 2Ω/n. Regime (b) is the boundary
casew unc = 0, at which the subject is exactly covered and
holds no net claim.
Regime (c) requires the derivative from below to be negative
at the kink, so that welfare rises as coverage falls below the
floor. By (46) this is
(kP −k S)Ω−k P T > Q cd Ωk P T.
SubstitutingΩ =na 2/2andT=na 1 witha 1 = 1−λ−n
and multiplying by2c d/ngives exactly (31). Equivalently,
(kS +k P )w unc <− Q cd Ωk P T,
so tolerated pollution requires the unconstrained stake to be
not merely negative but negative by more than the pollution-
relief value. This is the formal content of the reading given
in the statement: the platform must be the strongly dominant
refresher, so thatw unc is far below zero,andthe distortion
technology must be stiff, so thatc d is large and the relief term
is small. Either condition alone is insufficient, which is why
regime (c) is a corner of the parameter space rather than the
generic case.
APPENDIXE
GENERAL PRIVATE FLOWS
Section VI setsu S =u P = 0. Restoring them changes the
accounting but not the structure. From (8)–(10),
T(n) =u S +u P +R(n)−λn,Ω(n) =T(n) +C(n),
and the instrument collapse of Proposition 6(i) becomesw S =
uS + (s−λ)nandw P =u P +R(n)−sn, so coverage

remains the single static instrument. Corollary 3’s stake profile
is unchanged as a statement aboutw ⋆ S, because it is derived
at fixedTand does not reference howTis composed. The
only substantive change is the map from the optimal stake to
the optimal coverage: instead of (27) we obtain
s∗(n) =λ+ w⋆ S(n)−u S
n .(47)
A subject who already receives a private flowu S from the re-
lationship needs proportionally less explicit coverage to reach
the same stake, and the authenticity floors ∗ ≥λnow holds if
and only ifw ⋆ S ≥u S rather thanw ⋆ S ≥0. The floor is therefore
harder to clear when the subject’s outside private flow is large,
which is the formal version of a familiar objection: a platform
can point to the free service a user already enjoys as a reason
to pay less, and the model agrees arithmetically while noting
that the substitution leaves the stake, and hence refresh, exactly
where it was. The comparative statics of Theorem 5 carry over
withTandΩredefined; the closed forms of parts (iii) and (iv)
are specific tou S =u P = 0and to uniform demand, and (44)
should be recomputed for other primitives.
APPENDIXF
INFORMATION EXTENSIONS
Assumption 2 is maintained throughout the body. This
appendix records what relaxing it adds, and why we regard
the additions as the least memory-specific part of the problem.
Hidden fidelity.Suppose the seller observes˜qand the buyer
observes only its class distribution. Since willingness to pay
isA bqu and use-indexed fidelity is increasing in˜q, a uniform
price prices the conditional mean, high-fidelity artifacts with-
draw, and the pool unravels in the manner of [12]. Two features
of our object change the repair rather than the diagnosis.
First, the certifiable object is not authenticity butperformance
on a named use class, because Lemma 1 rules out a single
scalar quality index; the certificate must therefore be indexed
by buyer, task, and host model, which is a richer and more
expensive credential than a provenance attestation. Second, a
monopoly certifier has the Lizzeri incentive to coarsen what
it reveals [13], and coarsening is especially damaging here
because it collapses precisely the use-indexing that makes
the certificate informative. This is a second and independent
argument for the no-fusion rule of Section VII-D.
Evaluation leaks the asset.A buyer who must assess fit
before paying learns some of what he would be paying for,
which is the disclosure problem of [14], [15]. The severity
is indexed by the entanglement coefficient of Definition 6:
for lowκ ⋆ classes a garbled sample is nearly as informative
as the artifact and leaks little, whereas for highκ ⋆ classes
any sample informative about fit is also informative about
the person. The implied market design is therefore class-
dependent, moving from open samples at lowκ ⋆ to query
sandboxes and audited replay at highκ ⋆, where the buyer
evaluates through an interface that returns task performance
without releasing the state.
What does not change.The results of Sections IV–VI are
statements about distortions that survive symmetric informa-
tion, so none of them is repaired by these additions and
none is driven by them. The certifier’s economically correct
role was already pinned down under complete information
in Remark 12: make˜qcontractible so that coverage can be
quality-indexed, which is what shuts down the selection effect
of Proposition 5. Certification serves authorization and does
not substitute for it, and that ordering is unaffected by who
knows what.
REFERENCES
[1] T. R. Sumers, S. Yao, K. Narasimhan, and T. L. Griffiths, “Cognitive
architectures for language agents,”Transactions on Machine Learning
Research, 2024, arXiv:2309.02427.
[2] Y . Hu, S. Liu, Y . Yue, G. Zhang, B. Liu, F. Zhuet al., “Memory
in the age of AI agents,”arXiv preprint arXiv:2512.13564, 2025,
revised January 2026. Organizes agent memory by forms, functions,
and dynamics; three realizations (token-level, parametric, latent); factual
/ experiential / working types.
[3] Y . Pan, Q. Huang, and W. Yang, “Memory as asset: From agent-centric to
human-centric memory management,”arXiv preprint arXiv:2603.14212,
2026, vision paper: memory as a human-centric asset.
[4] M. Li, L. Gao, H. Xu, J. Li, P. Yu, L. Cheng, Y . Zhao, and M. An-
navaram, “Infrastructure for valuable, tradable, and verifiable agent
memory,”arXiv preprint arXiv:2603.24564, 2026, provenance binding
plus a marketplace layer; certification attests that memories are authentic,
effort-backed, and produced in a compatible execution context.
[5] S. K. Ravindran, “Portable agent memory: A protocol for
cryptographically-verified memory transfer across heterogeneous
AI agents,”arXiv preprint arXiv:2605.11032, 2026, single-author
protocol paper; the portability margin of our rights bundle.
[6] P. Jurcys, A. Greenwald, M. Fenwick, V . Loikkanen, S. Porsdam Mann,
and B. D. Earp, “Who owns my AI twin? Data ownership in a new
world of simulated identities,”arXiv preprint arXiv:2601.09877, 2026,
also published in journal form. Human-centric property framework;
conceptual and legal, no price formation or welfare analysis.
[7] W. Zhang, X. Zhang, C. Zhang, L. Yang, J. Shang, Z. Wei, H. P. Zou,
Z. Huang, Z. Wang, Y . Gao, X. Pan, L. Xiong, J. Liu, P. S. Yu, and X. Li,
“PersonaAgent: Bridging memory and action for personalized LLM
agents,” inFindings of the Association for Computational Linguistics:
ACL 2026, 2026, pp. 26 421–26 439, arXiv:2506.06254.
[8] C. I. Jones and C. Tonetti, “Nonrivalry and the economics of data,”
American Economic Review, vol. 110, no. 9, pp. 2819–2858, 2020.
[9] D. Acemoglu, A. Makhdoumi, A. Malekian, and A. Ozdaglar, “Too
much data: Prices and inefficiencies in data markets,”American Eco-
nomic Journal: Microeconomics, vol. 14, no. 4, pp. 218–256, 2022.
[10] B. Holmstr ¨om, “Moral hazard in teams,”The Bell Journal of Economics,
vol. 13, no. 2, pp. 324–340, 1982.
[11] O. Hart and J. Moore, “Property rights and the nature of the firm,”
Journal of Political Economy, vol. 98, no. 6, pp. 1119–1158, 1990.
[12] G. A. Akerlof, “The market for “lemons”: Quality uncertainty and the
market mechanism,”The Quarterly Journal of Economics, vol. 84, no. 3,
pp. 488–500, 1970.
[13] A. Lizzeri, “Information revelation and certification intermediaries,”The
RAND Journal of Economics, vol. 30, no. 2, pp. 214–231, 1999.
[14] J. J. Anton and D. A. Yao, “Expropriation and inventions: Appropriable
rents in the absence of property rights,”American Economic Review,
vol. 84, no. 1, pp. 190–209, 1994.
[15] ——, “The sale of ideas: Strategic disclosure, property rights, and
contracting,”The Review of Economic Studies, vol. 69, no. 3, pp. 513–
531, 2002.
[16] S. Tadelis, “What’s in a name? reputation as a tradeable asset,”American
Economic Review, vol. 89, no. 3, pp. 548–563, 1999.
[17] S. Board and M. Meyer-ter Vehn, “Reputation for quality,”Economet-
rica, vol. 81, no. 6, pp. 2381–2462, 2013.
[18] M. Sockin and W. Xiong, “Decentralization through tokenization,”The
Journal of Finance, vol. 78, no. 1, pp. 247–299, 2023.
[19] S. Morris and H. S. Shin, “Unique equilibrium in a model of self-
fulfilling currency attacks,”American Economic Review, vol. 88, no. 3,
pp. 587–597, 1998.
