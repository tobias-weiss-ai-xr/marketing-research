---
title: 'Breaking the Illusion of Artificial Consensus: Clone-Robust Weighting for Arbitrary Metric Spaces'
url: https://arxiv.org/abs/2602.24024
category: social-media
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Damien Berriaud
- Roger Wattenhofer
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.24024
pages: 18
chars: 94802
fetched_at: '2026-11-08T12:59:17+00:00'
kb_version: 1
---

# Breaking the Illusion of Artificial Consensus: Clone-Robust Weighting for Arbitrary Metric Spaces

Breaking the Illusion of Artificial Consensus: Clone-Robust
Weighting in Arbitrary Metric Spaces
Damien Berriaud
ETH Zürich
Zürich, Switzerland
dberriaud@ethz.ch
Supanat Wangsutthitham
ETH Zürich
Zürich, Switzerland
swangsutthit@ethz.ch
Roger Wattenhofer
ETH Zürich
Zürich, Switzerland
wattenhofer@ethz.ch
Abstract
Social media, pseudonymous identities and generative AI have
made online platforms highly vulnerable to Coordinated Inauthen-
tic Behavior: by generating large numbers of similar posts, influence
campaigns create an illusion of widespread support, exploiting the
tendency of users and algorithms alike to mistake frequency for con-
sensus. Clone-robust weighting functions address this problem by
assigning influence in a way that is insensitive to near-duplication,
as measured by a metric, while remaining symmetric, continuous
and local. While prior constructions were restricted to Euclidean
spaces, we present a computationally efficient framework for ar-
bitrary metric spaces, based on neighborhood graphs and graph
weighting functions satisfying a simple locality condition. As a
consequence, the visibility an attacker gains from near-duplicates
is bounded independently of their number. We further argue that,
in democratically sensitive settings such as news feeds, such guar-
antees must come with explainability, and introduce sharing coeffi-
cients that quantify how influence is transferred between elements
of prior volumetric constructions. In the graph setting, we show
that sharing measures based on the deletion of vertices or edges
are incompatible with locality, and instead define sharing through
the addition of clones. Finally, we characterize the resulting inter-
pretability properties and construct clone-robust graph weighting
functions satisfying them.
Keywords
Clone-Robustness, Graph Weighting Function, Metric Spaces, Re-
dundancy
1 Introduction
As you scroll through an online feed, you encounter a particular
claim and dismiss it without much thought. Later, you see it again,
phrased more cautiously; then as a joke, a meme, and a confident
argument using technical language. Each instance looks different,
comes from a different account, and appeals to a different audience.
None is particularly convincing in isolation, yet the doubt slowly
creeps in: is there some truth to this after all?
On online platforms, influence is implicitly tied to frequency:
an opinion posted repeatedly tends to be perceived as more preva-
lent or credible than it truly is. This popularity bias is amplified
when repetition is manufactured, e.g., by paid accounts posting
on command (troll farming), by campaigns disguised as sponta-
neous grassroots support (astroturfing), or more generally through
what platforms call Coordinated Inauthentic Behavior (CIB). As a
result, a small but hyper-active faction can hijack the conversation
and drown out opposing opinions by saturating platforms with
variations of the same unfounded claim.
If redundancy were a discrete phenomenon, this problem would
be easy to address: exact duplicates could be detected automatically,
merged, or made to share their influence. Generative AI, however,
entirely breaks this fragile assumption. Thousands of variations
of a single claim can now be produced at negligible cost, differing
in wording, tone or framing, and spanning a whole continuum
of similarity, from near-identical paraphrases to loosely related
arguments. No threshold can then reliably separate duplicates from
independent content: redundancy is not a binary property of pairs
of messages, but a matter of degree, calling for a metric perspective.
This shift, however, raises a new challenge: how should influence
be assigned so that approximate clones share it locally, without
allowing dense clusters of near-copies to overwhelm distant and un-
related opinions? This question is not specific to online platforms:
it arises whenever redundant inputs are aggregated, e.g., when eval-
uating models on benchmarks or aggregating human preferences
in reinforcement learning (Section 2). Clone-robust weighting in
metric spaces provides a principled framework to address it, which
we study here with CIB as our leading example.
Contribution & Outline.We first propose to determine the prob-
ability of appearance of messages through clone-robust weighting
functions, which assign positive weights, respect the symmetries
of the underlying space, vary continuously, and only redistribute
weight locally when near-duplicates are added (Section 3). To con-
struct such functions, we recover a binary notion of similarity from
the metric: for each distance threshold, we connect sufficiently
similar elements in a neighborhood graph, in which approximate
clones are equivalent for most thresholds (Section 4). Anygraph
weighting functionsatisfying symmetry and locality then induces,
by aggregation across radii, a clone-robust weighting function that
is efficiently computable and applies to arbitrary metrics, inde-
pendently of the topology they induce (Theorem 4.3). As a conse-
quence, the visibility gained by injecting near-duplicates of a post is
bounded independently of their number (Corollary 4.4). We further
argue that robustness requires explainability, and introducesharing
coefficientsfor prior clone-robust constructions, quantifying how
influence is transferred between elements (Section 5). Seeking simi-
lar measures for graph weighting functions, we show that sharing
based on the deletion of vertices or edges is incompatible with local-
ity (Theorems 6.2 and 6.4), and instead define sharing through the
addition of clones (Section 6). We characterize how the resulting
interpretability properties relate to each other and to locality, and
provide a general construction of clone-robust graph weighting
functions satisfying them with optimal locality (Theorem 6.13).
arXiv:2602.24024v2  [cs.GT]  13 Oct 2026

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer1
2 Related Work
Measuring CIB on Online Platforms.Coordinated inauthentic
behavior has become a central concern for social media platforms,
from coordinated accounts fabricating trending topics and deleting
their activity to evade detection [Elmas et al ., 2021], to botnets
posting LLM-generated content that state-of-the-art text classifiers
cannot distinguish from human posts [Yang and Menczer, 2024].
Since individual items are increasingly hard to flag in isolation, the
dominant detection paradigm instead measuressimilarity between
accounts[Mannocci et al., 2026]: accounts are linked through shared
behavioral traces such as co-retweets, URLs, hashtag sequences
or images, weighted by cosine or TF-IDF similarity [Nizzoli et al.,
2021, Pacheco et al ., 2021], through embeddings of their textual
content [Luceri et al., 2024], through the similarity of their action
sequences [Cresci et al., 2016] or activity time series [Chavoshi et al.,
2016], and, on video-first platforms, through reused captions and
media [Luceri et al., 2026]. These similarity spaces provide precisely
the input required by our framework. Rather than thresholding
them to classify and remove suspected accounts, an operation that
is brittle to the choice of threshold and to borderline cases, clone-
robust weighting functions continuously discount near-duplicate
content in proportion to its redundancy, so that platforms can
mitigate the amplification effect of CIB campaigns without having
to label any individual account as inauthentic. Closest in spirit,
Nizzoli et al. [2021] quantify coordination as a matter of degree,
by tracking which communities survive as a similarity threshold
is progressively raised; our framework instead aggregates over all
thresholds at once, through the measure𝜈, and uses the result to
reweight content rather than to label communities.
Reweighting Redundant Data.In machine learning, training data
rarely reflect the distribution of interest, and a standard remedy is to
reweight samples in the loss, e.g., according to their difficulty [Fre-
und and Schapire, 1997, Jiang et al., 2015] or through meta-learning
on a small unbiased validation set [Ren et al., 2019, Shu et al., 2019].
Closest to our setting is the problem of redundancy among training
samples, as arises in imbalanced datasets. These are commonly han-
dled by weighting samples inversely to their class frequency [Cao
et al., 2019, Jamal et al., 2020, Lin et al., 2017], which amounts to the
class-uniform weighting𝑤 CU when redundancy is known exactly.
Cui et al. [2019] refine this by accounting for overlap between sam-
ples through aneffective number of samples, so that each sample
only contributes the additional coverage it provides, an idea closely
related to the private weight of Section 5.
Clone-Robust Aggregation and Evaluation.Robustness to clones
has a long history in social choice, both for alternatives—through
independence of clones [Tideman, 1987] and composition consis-
tency [Brandl et al ., 2016, Laffond et al ., 1996]—and for agents,
through false-name-proofness [Conitzer and Yokoo, 2010, Nehama
et al., 2022, Todo et al., 2009]. It has recently resurfaced in the evalu-
ation of machine learning models, where benchmarking is cast as a
game between benchmarks and models and independence of clones
is sought through suitable aggregation mechanisms [Balduzzi et al.,
2018, Gao et al., 2025, Liu et al ., 2025, Marris et al ., 2025]. These
works, however, mostly consider exact clones. Robustness toap-
proximateclones was concurrently introduced by [Procaccia et al .,
2025] for preference aggregation in RLHF, weighting alternatives
by the volume of their Voronoi cells, and formalized axiomatically
by [Berriaud and Wattenhofer, 2025] for weighting functions in
Euclidean spaces. The latter rests on four principles:positivity(ev-
ery element receives positive weight),symmetry(weights respect
the symmetries of the space),continuity(weights vary smoothly
under small perturbations), andlocality(adding an element only
affects the weights of nearby ones). It also highlighted the lim-
itations of Voronoi-based weights and introduced geometrically
grounded alternatives. The present work extends this axiomatic
framework to arbitrary metric spaces and complements it with
sharing coefficients that make the resulting weights interpretable.
3 Clone-Robust Weighting Functions
Consider an algorithmic news aggregator that collects posts from
multiple media outlets and users into a centralized feed. When a
user refreshes their feed, the system gathers all newly available
posts into a finite set 𝑆⊆𝑀 , where 𝑀 denotes the space of all
possible posts. The algorithm then selects a probability distribution
𝜋𝑆 over𝑆 and populates the user’s feed by independently1 sampling
posts according to𝜋𝑆.
The space of posts 𝑀 is equipped with a notion of distance,
given by an operator𝑑 :𝑀×𝑀↦→R ≥0, which satisfiesidentity, i.e.,
𝑑(𝑥,𝑥)= 0,symmetry, i.e., 𝑑(𝑥,𝑦)=𝑑(𝑦,𝑥) , andtriangle inequality,
i.e.,𝑑(𝑥,𝑧)≤𝑑(𝑥,𝑦)+𝑑(𝑦,𝑧) , for all𝑥,𝑦,𝑧∈𝑀. Note that𝑑 is in
general a pseudo-metric rather than a metric, as it does not satisfy
separability: distinct posts 𝑥≠𝑦 may satisfy𝑑(𝑥,𝑦)= 0, for in-
stance when two identical posts originate from different accounts.
Since𝑑 determines what is considered a duplication in the first
place, and media revenue may depend on post visibility, it should
be chosen in a transparent and agreed-upon manner. Our frame-
work leaves this choice entirely open:𝑑 may be derived from any
existing measure of similarity between posts or accounts [Luceri
et al., 2024, 2026, Pacheco et al., 2021], and refined independently
of the weighting itself. We thus take the pseudo-metric𝑑 as given,
and study how it should shape the distribution𝜋𝑆.
Formally, we introduce aweighting function 𝑓 , which assigns to
each finite subset𝑆⊆𝑀 a probability distribution over its elements,
𝑓:𝑆∈
Ø
𝑛≥1
P𝑛(𝑀)↦→𝜋 𝑆∈Δ(𝑆),
whereP𝑛(𝑀) denotes the family of all subsets of𝑀 with cardinality
𝑛∈N , and Δ(𝑆)=

𝜋𝑆 :𝑆↦→[ 0, 1]| ˝ 𝑥∈𝑆 𝜋𝑆(𝑥)= 1 	 denotes the
simplex over the elements of𝑆.
We next discuss a collection of axioms capturing desirable proper-
ties for such weighting functions, each motivated by a way in which
weights could otherwise be manipulated. First, weights should re-
spect the symmetries of the underlying pseudo-metric space: posts
that are isomorphic within𝑆 should receive equal weight. Second,
since perfect clones (i.e., distinct posts at distance zero) are always
isomorphic, we extend this requirement to approximate clones
and ask that nearby posts receive similar weights. Moreover, the
weighting should be robust to perturbations of the set𝑆 itself, i.e.,𝑓
should be continuous. Together, they prevent weights from chang-
ing abruptly under small variations of the posts, which generative
1We assume that the probability of sampling the same post twice is negligible, i.e.,
𝐾 2∥𝜋𝑆∥ 2 2≪1, where𝐾denotes the total number of posts in the feed.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer2
AI easily produces. Third, we require protection against duplication
attacks. When approximate copies of a post are added, the weight
of posts farther than a disambiguation threshold 𝛼> 0should
remain unaffected, so that weight is only redistributed locally. The
threshold𝛼 thus sets the scale beyond which posts are considered
unrelated, and this locality is what bounds the visibility an attacker
can gain by duplication (Corollary 4.4). Finally, we impose a non-
censorship requirement: every post must receive strictly positive
weight, simultaneously ensuring that an attacker cannot drive the
weight of a post to zero through duplication. Note that these axioms
are agnostic to the quality or relevance of posts and only address
redundancy: promoting the “best” among clones would be the role
of a downstream ranking layer, combining its relevance scores
with the clone-robust weights. We now provide a formal definition
of these desiderata, with the regularity properties expressed via
Lipschitz-like conditions.
Definition 3.1 (Clone-Robust Weighting Function).Let
𝛼> 0be a disambiguation factor, let 𝑛∈N >0, and let 𝐿𝑛,𝐿′ 𝑛,𝐿′′ 𝑛 > 0
be Lipschitz constants. A weighting function𝑓 is said to satisfy a given
property at cardinality𝑛 if the corresponding condition holds for every
subset𝑆∈P 𝑛(𝑀) , every𝑥,𝑦∈𝑆 , every self-isometry 𝜎 :𝑆↦→𝑆 and
every finite subset𝑍⊆𝑀\𝑆.
•Positivity, i.e.,𝑓(𝑆)(𝑥)>0.
•Symmetry, i.e.,𝑓(𝑆)(𝑥)=𝑓(𝑆)(𝜎(𝑥)).
• Lipschitz Clone Fairness, i.e.,|𝑓(𝑆)(𝑥)−𝑓(𝑆)(𝑦)|≤𝐿 𝑛𝑑(𝑥,𝑦).
• Lipschitz Continuity, i.e., |𝑓(𝑆)(𝑥)−𝑓(𝜋(𝑆))(𝜋(𝑥))| ≤
𝐿′ 𝑛 max𝑢∈𝑆 𝑑(𝑢,𝜋(𝑢)) , for each bijection 𝜋 :𝑆↦→𝜋(𝑆)⊆𝑀.
•𝜶-Lipschitz Locality , i.e., if𝑑(𝑥,𝑦)≥𝛼 , then|𝑓(𝑆∪𝑍)(𝑦)−
𝑓(𝑆)(𝑦)|≤𝐿 ′′ 𝑛 max𝑧∈𝑍 𝑑(𝑥,𝑧).
A weighting function satisfying the above properties for every𝑛∈N >0
is called𝜶-clone-robust.
Note that the above properties strengthen the axioms proposed
in [Berriaud and Wattenhofer, 2025] by providing quantitative Lip-
schitz control—where differences are explicitly bounded in propor-
tion to distance—rather than the qualitative uniform continuity-
type guarantees of the form “for all𝜀> 0, there exists𝛿> 0... . ”
Moreover, the present locality property generalizes the original
formulation in [Berriaud and Wattenhofer, 2025] by considering
the addition of arbitrary finite subset𝑍instead of singletons only.
4 Construction based on Neighborhood Graphs
A central difficulty in clone-robust weighting is that similarity
between posts varies gradually with distance, while local sharing of
influence is easily defined only when similarity is all-or-nothing, as
captured by an equivalence relation. To reconcile both perspectives,
we threshold the metric to recover a binary notion of closeness.
Let𝑆⊆𝑀 be finite and 𝑟≥ 0be a radius. We define the 𝑟-
neighborhood graph𝐺𝑟(𝑆)= 𝑆,𝐸𝑟(𝑆) as the undirected graph on
𝑆 with edge set𝐸𝑟(𝑆)={(𝑥,𝑦)∈𝑆 2|𝑑(𝑥,𝑦)≤𝑟} . Adjacency in
𝐺𝑟(𝑆) is a similarity relation that is generally not transitive:𝑥∼𝑦
and𝑦∼𝑧 do not imply 𝑥∼𝑧 , although the triangle inequality
gives𝑑(𝑥,𝑧) ≤ 2𝑟, i.e., 𝑥∼𝑧 in𝐺2𝑟(𝑆) . To recover a transitive
notion of similarity, we consider the closed neighborhood𝑁𝐺[𝑥]=
{𝑥}∪{𝑦∈𝑉|(𝑥,𝑦)∈𝐸} of a node 𝑥 in a graph𝐺=(𝑉,𝐸) . It
induces an equivalence relation on 𝑉 , where𝑥≡ 𝐺 𝑦 if and only
if𝑁𝐺[𝑥]=𝑁 𝐺[𝑦], and we denote by[𝑥]𝐺 the equivalence class
of𝑥. We further write𝑑𝐺 for the shortest-path distance in𝐺, with
𝑑𝐺(𝑥,𝑦)=∞if𝑥and𝑦are not connected.
Perfect clones in𝑆, i.e., elements𝑥,𝑦∈𝑆 with𝑑(𝑥,𝑦)= 0, are
naturally always equivalent in𝐺𝑟(𝑆). More importantly, approx-
imate clones are also equivalent in 𝐺𝑟(𝑆) for “most values of 𝑟, ”
as illustrated in Figure 1. Hence, the graphs(𝐺𝑟(𝑆))𝑟≥0 and their
equivalence classes are essentially invariant under the addition
of clones, motivating the notion ofclone-robust graph weighting
function.
Definition 4.1 (Clone-Robust Graph Weighting Functions).
A graph weighting function 𝑤 associates with each finite graph a
probability distribution over its vertices, i.e., 𝑤 : (𝑉,𝐸) ∈ G ↦→
𝑝𝑉∈Δ(𝑉), whereG denotes the set containing all finite undirected
unweighted graphs.
Let𝑘> 0be a positive disambiguation factor. We say that a graph
weighting function𝑤 satisfies a given property if it verifies the corre-
sponding condition for every graph𝐺∈Gand vertex𝑥∈𝑉(𝐺).
• Symmetry, i.e.,𝑤(𝐺)(𝑥)=𝑤(𝜎(𝐺))(𝜎(𝑥)) for every graph
isomorphism𝜎:G↦→G.
•𝒌-Locality , i.e., 𝑤(𝐺)(𝑧)=𝑤(𝐺\{𝑦})(𝑧) for each pair of
vertices𝑦,𝑧∈𝑉(𝐺)where𝑦≡ 𝐺 𝑥,𝑦≠𝑥, and𝑑 𝐺(𝑥,𝑧)>𝑘.
A graph weighting function satisfying the above properties is called
𝒌-clone-robust.
We next construct a simple instance of1-clone-robust graph
weighting function.
Example 4.2.For a finite undirected graph 𝐺=(𝑉,𝐸) , the equiv-
alence relation≡𝐺 partitions𝑉 into classes of structurally identical
vertices. A natural way to assign weights in such a graph is to let each
class account for the same fraction of the distribution, and treat all
vertices within a class equally (cf. Figure 2). We call the resulting rule
theclass-uniform graph weighting function. Formally, if 𝑉/≡𝐺
denotes the set of equivalence classes in𝐺, we set
𝑤 CU(𝐺)(𝑥)≔ 1 |𝑉/≡𝐺|·|[𝑥] 𝐺|, 𝑥∈𝑉.
The function𝑤 CU satisfies the required properties: symmetry holds be-
cause graph isomorphisms preserve equivalence classes, and 1-locality
follows from the fact that adding a new vertex to an existing equiva-
lence class affects only the weights of vertices within that class.
Clone-robust graph weighting functions are of special interest
because they enable the construction of clone-robust weighting
functions for arbitrary pseudo-metric.
Theorem 4.3.Let 𝑤 be a𝑘-clone-robust graph weighting function,
𝛼 be a positive radius and 𝜈 be a probability density function with
support[0,𝛼] and value bounded from above by𝜈. Then the weighting
function𝑓𝜈,𝑤 is𝑘·𝛼 -clone-robust, where𝑓𝜈,𝑤 is defined for every subset
𝑆⊆𝑀of cardinality|𝑆|=𝑚∈N >0 and𝑥∈𝑆by
𝑓𝜈,𝑤(𝑆)(𝑥):=
∫ 𝛼
0
𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝑥)𝑑𝑟.
Moreover,𝑓𝜈,𝑤(𝑆)(𝑥) can be computed in time 𝑂𝑚2(𝑊(𝑚)+𝐶 𝜈+
𝐶𝑑+log𝑚) , where 𝑊(𝑚) ,𝐶𝜈 and𝐶𝑑 are the worst-case costs of
evaluating𝑤 on a graph with 𝑚 vertices, the cumulative distribution
of𝜈at a single argument, and the pseudo-metric𝑑.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer3
𝑟
0
𝑑(𝑥,𝑦) 𝑑(𝑥,𝑧 1) 𝑑(𝑥,𝑧 2) 𝑑(𝑥,𝑧 3) 𝑑(𝑥,𝑧 4)
𝑑(𝑦,𝑧 1) 𝑑(𝑦,𝑧 2) 𝑑(𝑦,𝑧 3) 𝑑(𝑦,𝑧 4)
0
1
2 3
4
5
6
7

V/≡G

 =5
1
5·3
1
5·3
1
5·3
1
5·1
1
5·2
1
5·2
1
5·1
1
5·1
Figure 1: Impact of adding a vertex 𝑦 that is an approximate
clone of𝑥. By the triangle inequality, each distance 𝑑(𝑦,𝑧)
with𝑧∈𝑆 lies within an interval of length2 𝑑(𝑥,𝑦) centered
at𝑑(𝑥,𝑧) . Thus, for all radii 𝑟≥ 0outside the blue forbidden
intervals, the vertices 𝑥 and𝑦 are equivalent in𝐺𝑟(𝑆∪{𝑦}) .
Figure 2: Illustration of the class-uniform weighting 𝑤 CU on
a small graph. Nodes are grouped into |𝑉/≡𝐺|= 5equiva-
lence classes:{0, 1, 2} in blue,{3} in orange,{4, 5} in green,
{6}in pink, and{7}in purple. Each class receives the same
total weight, distributed uniformly among its vertices.
A precise formulation of Theorem 4.3 providing the exact Lips-
chitz constants, its full proof, as well as an algorithm achieving the
stated complexity, are detailed in Appendix A. Interestingly, note
that positivity is not required from graph weighting function 𝑤;
this property rather emerges for𝑓𝜈,𝑤 from symmetry and locality
alone at neighborhood graphs of radii 𝑟 close to 0. Furthermore,
the strict equality at the singleton level in the locality condition for
graphs (Definition 4.1) can be applied iteratively, which yields the
locality property of𝑓 𝜈,𝑤 for arbitrary finite set𝑍(Definition 3.1).
Besides its Lipschitz-style guarantees, this graph-based approach
offers two crucial advantages over prior constructions [Berriaud and
Wattenhofer, 2025]. First, the exact evaluation of𝑓𝜈,𝑤 remains com-
putationally tractable under suitable choices of𝜈 and polynomial-
time graph weighting functions like𝑤𝐶𝑈. Second, this formulation
is topologically invariant, and the weighting procedure depends
only on the underlying metric𝑑 rather than the specific choice of
embedding space𝑀. As such, it remains unaffected by isometric
embeddings—such as the addition of dummy dimensions when
𝑀=R 𝑛—and offers a uniform framework across all metric spaces
instead of being restricted to Euclidean settings.
Implications for Online News Feeds.Recall that the feed of a user
is populated by sampling posts according to 𝜋𝑆 =𝑓(𝑆) . Under
uniform weighting, an attacker injectingℓ similar messages into a
feed of|𝑆| posts obtains a shareℓ/(|𝑆|+ℓ) , which tends to one as
ℓ grows. In contrast, Theorem 4.3 bounds the visibility of such a
campaign independently of its size.
Corollary 4.4.Let 𝑓𝜈,𝑤 be as in Theorem 4.3, and 𝑆⊆𝑀 be a
finite set of posts. Consider an attacker who promotes a target message
𝑡∈𝑆 by injecting a finite set of variants𝐴⊆𝑀\𝑆 , all within distance
𝜌of𝑡. Then the total visibility of the campaign satisfies
∑︁
𝑎∈𝐴∪{𝑡}
𝑓𝜈,𝑤(𝑆∪𝐴)(𝑎) ≤
∑︁
𝑦∈𝑆
𝑑(𝑡,𝑦)<𝑘𝛼
𝑓𝜈,𝑤(𝑆)(𝑦) +2 𝜈|𝑆| 2𝜌.
Proof. Every𝑦∈𝑆 with𝑑(𝑡,𝑦)≥𝑘𝛼 satisfies𝑓𝜈,𝑤(𝑆∪𝐴)(𝑦)≥
𝑓𝜈,𝑤(𝑆)(𝑦)− 2𝜈|𝑆|𝜌 by Lipschitz(𝑘𝛼) -locality, applied with𝑥=𝑡
and𝑍=𝐴 . Summing over these at most|𝑆| elements, using that
𝑓𝜈,𝑤(𝑆∪𝐴) and 𝑓𝜈,𝑤(𝑆) both sum to one, and dropping the non-
negative weights of the remaining items within distance 𝑘𝛼 of𝑡
yields the claim.□
The bound does not depend on the number|𝐴| of injected variants,
only on their spread𝜌: for𝜈 uniform, i.e.,𝜈= 1/𝛼, the second term
scales with𝜌/𝛼 . Since the bound holds for every𝜌, an attacker can
only escape it by spreading content further apart, i.e., by producing
genuinely dissimilar messages. Conversely, a defender who esti-
mates the distance𝜌 beyond which content no longer reinforces the
same claim can choose𝛼 to minimize the right-hand side, balancing
the weight of the𝑘𝛼-neighborhood of𝑡against the spread term.
As an illustrative toy experiment, we consider a feed of26posts
in the plane, including a grassroots cluster of6similar posts from
independent users, into which an attacker injects20close variants
of a target post. Under uniform weighting, the campaign captures
close to half of the feed, whereas clone-robust weighting reduces it
to a share comparable to that of a few independent posts (Figure 3a).
Note though that the grassroots cluster is discounted as well: if
coordinated and genuine agreement cannot be told apart in the
metric space, any protection against redundancy necessarily affects
both. We then vary the size of the campaign in random feeds of
30posts: whereas its share tends to one under uniform weight-
ing, it saturates under clone-robust weighting, at a level roughly
proportional to𝜌/𝛼 (Figure 3b). This matches the second term of
Corollary 4.4: below radius roughly2𝜌, i.e., on a fraction2𝜌/𝛼 of
the integration range, the variants are not yet equivalent and cap-
ture most of the weight, whereas they form a single class at larger
radii. The first term is pessimistic here, as neighbors only yield
weight to the campaign once equivalent to it, i.e., as𝛼 approaches
the diameter of the feed.
5 Explainability of Volumetric Weighting
Functions
Clone-robust weighting functions were introduced in [Berriaud
and Wattenhofer, 2025] to replace ad-hoc empirical weighting with
a mathematically rigorous alternative. By explicitly demanding a
pseudo-metric between posts, this approach forces the designer
to quantify their assumptions about the underlying space and en-
sures the resulting weights are consistent with them. However, a
principled weighting procedure does not by itself guarantee trans-
parency. In a news aggregator designed to combat duplication at-
tacks, transparency must extend beyond the algorithm’s code to
the interpretability of its outcomes, answering for instance:“Why is

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer4
13%→10%
46%→9%
𝛼
Total share: uniform→clone-robust
(a) Feed under attack (20 variants)
1 10 100 1000
0
20
40
60
80
100
# Posts in the campaign
Campaign share (%)
(b) Campaign size
uniform
𝛼=0.25
𝛼=0.5
𝛼=1
0 2 4
−20
−10
0
𝛼
Distance to the target/𝛼
Weight change (%)
(c) One more variant
uniform
clone-robust
target + variants
its neighbors
grassroots
other posts
uniform
clone-robust
radius𝛼
Figure 3: Clone-robust weighting 𝑓𝜈,𝑤 CU , with𝜈 uniform on[0,𝛼] , on synthetic feeds in R2. (a) A feed of26posts after an attacker
injects20variants within distance 𝜌= 0.05𝛼 of a target post; marker area is proportional to weight, and uniform weights are
aggregated for the campaign and the grassroots. (b) Campaign share in random feeds of30posts in a5 × 5square (𝜌= 0.05):
mean and5–95%range over40feeds. (c) Weight change of each post in (a) when a fifth variant is added to a campaign of four.
my post downweighted?”Since clone-robust functions force similar
posts to share their weight locally, it is natural to askhow much
weight two distinct elements share. To address this, we introduce
thesharing coefficient, which quantifies how two elements of a
set𝑆 affect each other’s weight, and enables comparisons such as
whether𝑥“shares more weight” with𝑦than with𝑧.
We first observe that the clone-robust weighting functions of [Berri-
aud and Wattenhofer, 2025] naturally admit such a notion of sharing.
Recall the following weighting function on(R𝑛,𝑑 2), with𝑑2(𝑥,𝑦)=˝𝑛
𝑖=1(𝑥𝑖−𝑦𝑖)2 1/2, defined for a finite subset𝑆⊆R 𝑛 and an ele-
ment𝑥∈𝑆by
𝑔𝑟(𝑆)(𝑥):= 1 𝑍 ∫ 𝐵𝑟(𝑥) 1 |𝑆∩𝐵 𝑟(𝑧)| 𝑑𝑧, 𝑍:=Vol  Ø 𝑦∈𝑆 𝐵𝑟(𝑦)  ,
where𝐵𝑟(·) denotes the Euclidean ball of radius𝑟> 0, and Vol(𝑋)
is the𝑛-dimensional Lebesgue measure of𝑋⊆R 𝑛. As in [Berriaud
and Wattenhofer, 2025],𝑔𝑟 can be read as a voting rule: every point𝑧
of the space is a voter who splits one unit of vote equally among the
|𝑆∩𝐵 𝑟(𝑧)| posts within distance𝑟, and𝑔𝑟(𝑆)(𝑥) is the normalized
total vote received by𝑥. Clones thus compete for the same voters,
rather than each gaining its own. This suggests asharing coefficient,
where𝜒𝑔𝑟,𝑆 𝑦→𝑥 is the vote that𝑦 would gain if every voter ignored𝑥:
a voter𝑧∈𝐵 𝑟(𝑥)∩𝐵 𝑟(𝑦) seeing𝑘=|𝑆∩𝐵 𝑟(𝑧)| posts would then
give𝑦an additional 1 𝑘−1− 1 𝑘 = 1 𝑘(𝑘−1) .
Definition 5.1 (Sharing coefficient of 𝑔𝑟 ).For a finite set
𝑆⊆R 𝑛 and distinct elements 𝑥,𝑦∈𝑆 , the sharing coefficient 𝜒𝑔𝑟,𝑆 is
defined by
𝜒𝑔𝑟,𝑆 𝑦→𝑥 := 1 𝑍 ∫ 𝐵𝑟(𝑥)∩𝐵𝑟(𝑦) 1 |𝑆∩𝐵 𝑟(𝑧)|·(|𝑆∩𝐵 𝑟(𝑧)|−1) 𝑑𝑧,and
𝜒𝑔𝑟,𝑆 𝑥→𝑥 :=𝑔𝑟(𝑆)(𝑥)− ∑︁
𝑦≠𝑥
𝜒𝑔𝑟,𝑆 𝑦→𝑥.
We refer to ˝ 𝑦≠𝑥 𝜒𝑔𝑟,𝑆 𝑥→𝑦 as the shared weight of 𝑥, and to 𝜒𝑔𝑟,𝑆 𝑥→𝑥 as its
private weight.
Well-definedness and symmetry.For every 𝑧∈𝐵 𝑟(𝑥)∩𝐵 𝑟(𝑦), the
set𝑆∩𝐵 𝑟(𝑧) contains both𝑥 and𝑦, so the integrand is a positive
simple function on the integration domain, and𝜒𝑔𝑟,𝑆 is well defined.
Moreover,𝑥 and𝑦 only enter through the domain of integration
and do so symmetrically; hence𝜒 𝑔𝑟,𝑆 𝑥→𝑦 =𝜒 𝑔𝑟,𝑆 𝑦→𝑥.
Non-negativity and locality.Since the integrand is positive,𝜒𝑔𝑟,𝑆 𝑥→𝑦≥
0, with equality if and only if𝐵𝑟(𝑥)∩𝐵 𝑟(𝑦) has measure zero, i.e.,
𝑑2(𝑥,𝑦)≥ 2𝑟. This is exactly the locality parameter of𝑔𝑟 : elements
at distance at least2𝑟 do not affect each other. Moreover, the private
weight can be rewritten as
𝜒𝑔𝑟,𝑆 𝑥→𝑥 = 1 𝑍 Vol  𝐵𝑟(𝑥)\ Ø 𝑦≠𝑥 𝐵𝑟(𝑦)  ,
since a voter seeing𝑘≥ 2posts redistributes its entire share 1 𝑘 of𝑥
among the𝑘− 1others, so only voters who see 𝑥 alone contribute.
Hence𝜒𝑔𝑟,𝑆 𝑥→𝑥≥ 0, with equality if and only if𝐵𝑟(𝑥) is covered by
the other balls up to a null set.
Effect of element removal.By construction, removing 𝑥 from𝑆
has two effects on the weights of the remaining elements. First,
voters in𝐵𝑟(𝑥)∩𝐵 𝑟(𝑦) no longer vote for𝑥, so every𝑦 gains its
shared weight𝜒𝑔𝑟,𝑆 𝑦→𝑥 , anadditive local increase. Second, voters who
only saw𝑥 disappear, which shrinks the normalization factor to
Vol— 𝑦≠𝑥𝐵𝑟(𝑦) =𝑍 1−𝜒 𝑔𝑟,𝑆 𝑥→𝑥 , aglobal multiplicative rescaling
governed by the private weight of𝑥. Together, these effects yield
𝑔𝑟(𝑆\{𝑥})(𝑦)=

𝑔𝑟(𝑆)(𝑦)+𝜒 𝑔𝑟,𝑆 𝑦→𝑥  1−𝜒 𝑔𝑟,𝑆 𝑥→𝑥 −1 .(1)
Notably, since0 ≤𝜒 𝑔𝑟,𝑆 𝑦→𝑥 ≤𝑔 𝑟(𝑆)(𝑥)< 1(also when 𝑦=𝑥 ),
both local transfer and global rescaling increase the weights of the
remaining elements.
Sharing monotonicity.At first glance, one might expect a clone-
robust weighting function to share more weight with closer neigh-
bors than with more distant ones, i.e.,𝑑(𝑥,𝑦)≤𝑑(𝑥,𝑧) should imply
𝜒𝑆 𝑥→𝑦≥𝜒 𝑆 𝑥→𝑧 for an appropriate sharing coefficient 𝜒. However,
clones complicate this intuition: if the shared weight is additive over
perfect clones, the individual values must decrease as clones are
added. Consequently,𝜒𝑔𝑟,𝑆 𝑥→𝑦 may be smaller than𝜒𝑔𝑟,𝑆 𝑥→𝑧 even though
𝑦 is closer to 𝑥 than𝑧 is, as depicted in Figure 4. A stronger no-
tion of domination than distance comparison is therefore required,
and𝜒𝑔𝑟 satisfies the following monotonicity, based on inclusion of
intersecting regions.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer5
𝑥𝑦1
𝑦2
𝑧𝜒𝑔𝑟,𝑆 𝑥→𝑦 1
∝ 1 3· 1 2
𝜒𝑔𝑟,𝑆 𝑥→𝑧
∝ 1 2· 1 1
Figure 4: Consider the set 𝑆={𝑥,𝑦 1,𝑦 2,𝑧}. Since𝑦1 is closer
to𝑥 than𝑧, it shares more volume with 𝑥 than𝑧 does, i.e.,
Vol𝐵𝑟(𝑥)∩𝐵 𝑟(𝑦1)≥Vol 𝐵𝑟(𝑥)∩𝐵 𝑟(𝑧). However, the clone
𝑦2 dilutes𝑦 1’s sharing coefficient, and𝜒 𝑔𝑟,𝑆 𝑥→𝑦 1≤𝜒 𝑔𝑟,𝑆 𝑥→𝑧.
Property 5.2 (Sharing Domination).Let 𝑥,𝑦,𝑧 be three distinct
elements of a finite set 𝑆⊆R 𝑛 such that𝑦 intersection-dominates
𝑧 with respect to𝑥, i.e.,𝐵𝑟(𝑥)∩𝐵 𝑟(𝑧)⊆𝐵 𝑟(𝑥)∩𝐵 𝑟(𝑦). Then𝑧 shares
less weight with𝑥than𝑦does, that is,𝜒 𝑔𝑟,𝑆 𝑧→𝑥≤𝜒 𝑔𝑟,𝑆 𝑦→𝑥.
Proof. The integrands of𝜒𝑔𝑟,𝑆 𝑦→𝑥 and𝜒𝑔𝑟,𝑆 𝑧→𝑥 are identical and non-
negative, so the claim follows from the inclusion of their integration
domains.□
Intersection-domination is indeed stronger than distance-domination:
if𝑦 intersection-dominates𝑧 with respect to𝑥 and𝐵𝑟(𝑥)∩𝐵 𝑟(𝑧)≠
∅, then𝑑2(𝑥,𝑦)≤𝑑 2(𝑥,𝑧) , since Vol𝐵𝑟(𝑥)∩𝐵 𝑟(𝑢) is strictly de-
creasing in𝑑2(𝑥,𝑢) on[0, 2𝑟) and vanishes beyond. We next show
that𝜒𝑔𝑟 satisfies another natural form of monotonicity calleddilu-
tion, i.e., sharing decreases as clones are added.
Property 5.3 (Sharing Dilution).Let (𝑀,𝑑) be a pseudo-metric
space that induces (R𝑛,𝑑 2) by metric identification. Let 𝑥0 be in a
finite set 𝑆⊆𝑀 , and let (𝑥𝑖)𝑖∈N >0 ∈ 𝑀\𝑆  N>0 be a sequence
of perfect clones of 𝑥0, i.e., 𝑑(𝑥 0,𝑥𝑖)= 0for all 𝑖> 0. We define
𝑆𝑖 =𝑆∪{𝑥 1,...,𝑥 𝑖} for all𝑖∈N. Then, for any 𝑦∈𝑆\{𝑥 0} and
integers𝑖<𝑗, it holds that𝜒 𝑔𝑟,𝑆𝑖 𝑦→𝑥0≥𝜒 𝑔𝑟,𝑆𝑗 𝑦→𝑥0.
Proof. Only the integrand of 𝜒𝑔𝑟,𝑆𝑖 𝑦→𝑥0 depends on 𝑖, and it de-
creases in𝑖. Moreover,𝜒 𝑔𝑟,𝑆0 𝑥0→𝑥0≥𝜒 𝑔𝑟,𝑆𝑖 𝑥0→𝑥0 =0for all𝑖>0.□
We similarly construct in Appendix C a sharing coefficient for the
second family of clone-robust weighting functions of [Berriaud and
Wattenhofer, 2025], and show that it inherits most of the desirable
properties of𝜒 𝑔𝑟.
6 Co-Design of Sharing Measures and Graph
Weighting Functions
Since the requirements of Theorem 4.3 are easily satisfied (cf. Ex-
ample 4.2), explainability could actively guide the design of further
graph-weighting functions. As such, a natural next step is to de-
fine analogous sharing coefficients for the graph setting with a
set of natural interpretability axioms. This explicit co-design be-
tween weighting functions and their associated sharing measures—
enforcing complementary and desirable properties—will increase
the overall transparency of the weighting process.
6.1 Impossibility of Sharing under Arbitrary
Perturbations
Given the construction in Section 5, a natural first approach to
defining a meaningful sharing coefficient is to quantify the transfer
of weight resulting from the deletion of a vertex. Following the
decomposition in Equation (1), we postulate that such a deletion
results in an additive local weight transfer followed by a global
multiplicative rescaling.
Definition 6.1 (Vertex-Sharing).Let 𝑤 be a 𝑘-clone-robust
graph weighting function, 𝐺∈G , and 𝑥∈𝑉(𝐺) . We call vertex-
sharing coefficients of𝑥any family  v 𝜒𝑤,𝐺 𝑦→𝑥  𝑦∈𝑉(𝐺) such that
v
𝜒𝑤,𝐺 𝑦→𝑥 = 1− v 𝜒𝑤,𝐺 𝑥→𝑥 ·𝑤(𝐺\{𝑥})(𝑦)−𝑤(𝐺)(𝑦),∀𝑦≠𝑥(2)
and
v
𝜒𝑤,𝐺 𝑦→𝑥 = 0whenever 𝑑𝐺(𝑥,𝑦)>𝑘 . We say that𝑤 satisfiesvertex-
sharing non-negativityif, for every graph 𝐺 and vertex𝑥∈𝑉(𝐺) ,
there exist non-negative vertex-sharing coefficients of𝑥.
Equation (2) alone does not determine the coefficients ( |𝑉(𝐺)|
unknowns but only |𝑉(𝐺)|− 1equations per vertex 𝑥), which
motivates the additional locality condition: consistently with the
𝑘-locality of𝑤, vertices far from 𝑥 should not share any weight
with it. A single such vertex then fixes the private weight
v
𝜒𝑤,𝐺 𝑥→𝑥 ,
while any further one imposes a consistency constraint on𝑤: all
vertices outside𝑥’s𝑘-hop neighborhood must scale their weights
by a common multiplicative factor upon deletion of𝑥. Moreover,
non-negativity can be thought of as a form of monotonicity, requir-
ing that 𝑥 shares at least as much with vertices inside its 𝑘-hop
neighborhood as with vertices outside of it. In particular, it implies
𝑤(𝐺)(𝑦)≤ 1− v 𝜒𝑤,𝐺 𝑥→𝑥 ·𝑤(𝐺\{𝑥})(𝑦)≤𝑤(𝐺\{𝑥})(𝑦) for all
𝑦≠𝑥 , thus the following result shows that this is incompatible
with clone-robustness.
Theorem 6.2.For every 𝑘> 0and every 𝑘-clone-robust graph
weighting function𝑤, there exist a finite graph 𝐺∈G and distinct
vertices𝑥,𝑦∈𝑉(𝐺) such that𝑤(𝐺\{𝑥})(𝑦)<𝑤(𝐺)(𝑦) . In partic-
ular,𝑤does not satisfy vertex-sharing non-negativity.
Given this negative result, we seek more permissive notions of
sharing. Unlike metric spaces, graphs offer a distinct structural
operation: one can also measure the weight transfer resulting from
thedeletion of an edge 𝑒, where𝐺−𝑒≔(𝑉(𝐺),𝐸(𝐺)\{𝑒}) and
𝑑𝐺(𝑒,𝑧)≔min 𝑥∈𝑒 𝑑𝐺(𝑥,𝑧).
Definition 6.3 (Edge-Sharing).Let 𝑤 be a𝑘-clone-robust graph
weighting function, 𝐺∈G , and 𝑒={𝑥,𝑦}∈𝐸(𝐺) . We call edge-
sharing coefficients of 𝑒 any family  e 𝜒𝑤,𝐺 𝑧→𝑒  𝑧∈𝑉(𝐺) for which there
exists a contracting factor𝜂 𝐺,𝑒∈(0,1]such that,
e
𝜒𝑤,𝐺 𝑧→𝑒 =𝑤(𝐺−𝑒)(𝑧)−𝜂 𝐺,𝑒𝑤(𝐺)(𝑧),∀𝑧∈𝑉(𝐺)(3)
and
e
𝜒𝑤,𝐺 𝑧→𝑒 = 0whenever 𝑑𝐺(𝑒,𝑧)>𝑘 . We say that 𝑤 satisfiesby-
stander contractionif, for every graph 𝐺 and edge 𝑒, there exist
edge-sharing coefficients of 𝑒 such that
e
𝜒𝑤,𝐺 𝑧→𝑒 ≤ 0for every 𝑧∉𝑒 ,
and that𝑤 satisfiesendpoint expansionif, for every graph 𝐺 and
edge𝑒={𝑥,𝑦} , there exists an expanding factor 𝜇𝐺,𝑒≥ 1such that
𝑤(𝐺−𝑒)(𝑢)=𝜇 𝐺,𝑒𝑤(𝐺)(𝑢)for both𝑢∈𝑒.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer6
In words, deleting𝑒 uniformly rescales the weights of vertices far
from𝑒 by𝜂𝐺,𝑒 , the surrounding vertices yield relative weight to ac-
commodate this local expansion, and both endpoints gain weight in
the same proportion as they become more independent; in particu-
lar, endpoint expansion implies
e
𝜒𝑤,𝐺 𝑥→𝑒 =(𝜇 𝐺,𝑒−𝜂𝐺,𝑒)𝑤(𝐺)(𝑥)≥ 0.
Unfortunately, these requirements are again incompatible with
clone-robustness.
Theorem 6.4.No1-clone-robust graph weighting function satisfies
both endpoint expansion and bystander contraction.
Both proofs follow a sequence of small graphs, each obtained from
the previous one by adding or removing a vertex or an edge, whose
weights are pinned down step by step by symmetry, locality and
clone-robustness until a contradiction arises; details are deferred
to Appendix A.
6.2 Clone-Sharing Coefficients and Desirable
Properties
These negative results, particularly Theorem 6.2, underscore the
difficulty of reconciling locality constraints with weight monotonic-
ity under arbitrary graph perturbations. A natural solution is to
restrict our focus to operations that are inherently compatible with
locality, such as the deletion or addition of clones. Because generic
nodes may not have existing clones to delete, we opt for the latter
operation and use the resulting change in weight as a proxy for the
weight already shared with the original node.
Definition 6.5 (Clone-Sharing Coefficient).Let 𝑤 be a graph
weighting function,𝐺∈G be a finite graph, and 𝑥,𝑦 be two vertices
in𝑉(𝐺). For𝑖∈N , let𝐺𝑖 𝑥 denote the graph𝐺 augmented with𝑖 clones
of𝑥, i.e.,𝑉(𝐺 𝑖 𝑥)=𝑉(𝐺)∪{𝑥 1,...,𝑥 𝑖} with𝑥𝑗 ∉𝑉(𝐺) and𝑥𝑗≡𝐺𝑖𝑥 𝑥
for all1 ≤𝑗≤𝑖. We then define the clone-sharing coefficient
c
𝜒𝑤,𝐺 by
c
𝜒𝑤,𝐺 𝑦→𝑥 :=𝑤(𝐺)(𝑦)−𝑤(𝐺 1 𝑥)(𝑦).
This formulation is consistent with the vertex-deletion paradigm of
Equation (2): since𝐺=𝐺 1 𝑥\{𝑥 1}, the absence of a multiplicative
factor corresponds to the requirement
v
𝜒𝑤,𝐺1𝑥 𝑥 1→𝑥1 = 0, which results
from the locality constraints of both𝑤 and
v
𝜒𝑤. Moreover, if𝑤 is
𝑘-local, then
c
𝜒𝑤,𝐺 𝑦→𝑥 =0for all𝑥,𝑦∈𝑉(𝐺)such that𝑑 𝐺(𝑥,𝑦)>𝑘.
Guided by the interpretability properties established for𝜒𝑔𝑟 in
Section 5, we next define similar properties for
c
𝜒𝑤, as requirements
on the weighting function𝑤.
Definition 6.6.A graph weighting function 𝑤 satisfiesclone-
sharing non-negativityif
c
𝜒𝑤,𝐺 𝑦→𝑥≥ 0holds for every finite graph
𝐺∈ G and vertices 𝑥,𝑦∈𝑉(𝐺). We moreover say that 𝑤 satis-
fies 𝒌-clone-sharing positivityif the inequality is strict whenever
𝑑𝐺(𝑥,𝑦)≤𝑘.
We next adapt intersection-domination (Property 5.2) to graphs,
replacing balls by 𝑘-hop neighborhoods 𝑁𝑘 𝐺[𝑣] :={𝑢∈𝑉(𝐺) |
𝑑𝐺(𝑢,𝑣)≤𝑘} , and require the sharing coefficient to be monotone
with respect to it.
Definition 6.7.A graph weighting function 𝑤 satisfies𝑘-clone-
sharing dominationif
c
𝜒𝑤,𝐺 𝑧→𝑥≤ c 𝜒𝑤,𝐺 𝑦→𝑥 holds for every graph𝐺∈G
and vertices 𝑥,𝑦,𝑧∈𝑉(𝐺) such that 𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑧]⊆𝑁 𝑘 𝐺[𝑥]∩
𝑁𝑘 𝐺[𝑦]. We moreover say that𝑤 satisfies𝑘-strong clone-sharing
dominationwhen equality holds if and only if the two intersections
are equal.
Parallel to Property 5.3, we finally require that the shared weight
decreases monotonically as additional clones are introduced.
Definition 6.8.A graph weighting function 𝑤 satisfiesclone-
sharing dilutionif
c
𝜒𝑤,𝐺𝑖𝑥 𝑦→𝑥 ≥ c 𝜒𝑤,𝐺𝑗 𝑥 𝑦→𝑥 holds for every graph 𝐺∈G ,
vertices𝑥,𝑦∈𝑉(𝐺) and integers0 ≤𝑖<𝑗. We moreover say that𝑤
satisfies 𝒌-strong clone-sharing dilutionif the inequality is strict
whenever𝑑𝐺(𝑥,𝑦)≤𝑘.
To ground these definitions, we evaluate them against the class-
uniform graph weighting function𝑤 CU introduced in Example 4.2.
Example 6.9 (Clone-Sharing Properties of 𝑤 CU).Adding
clones of a vertex𝑥 does not change the number of equivalence classes,
i.e.,|𝑉/≡𝐺𝑖𝑥|=|𝑉/≡ 𝐺|, but it increases the size of the class of 𝑥, i.e.,
|[𝑥]𝐺𝑖𝑥|=|[𝑥] 𝐺|+𝑖 . Consequently, the weight of any vertex 𝑦. 𝐺 𝑥
remains unaffected, and the clone-sharing coefficient takes the simple
form
c
𝜒𝑤CU,𝐺 𝑦→𝑥 =
( 1
|𝑉/≡𝐺|

1
|[𝑥] 𝐺|− 1 |[𝑥] 𝐺|+1

>0if𝑦≡ 𝐺 𝑥,
0if𝑦. 𝐺 𝑥.
From this expression, we immediately deduce that𝑤 CU:
• Satisfiesclone-sharing non-negativity, but fails1-positivity,
since a neighbor𝑦. 𝐺 𝑥has
c
𝜒𝑤CU,𝐺 𝑦→𝑥 =0.
• Satisfiesclone-sharing dilution, but fails1-strong dilu-
tion. For𝑦≡ 𝐺 𝑥, the difference 1 |[𝑥] 𝐺|+𝑖− 1 |[𝑥] 𝐺|+𝑖+1 decreases
as𝑖grows, but for𝑦. 𝐺 𝑥the coefficient is zero for every𝑖.
• Fails1-clone-sharing domination. Indeed, let 𝑥 be a leaf
and𝑦 its neighbor, with 𝑦. 𝐺 𝑥. Taking 𝑧=𝑥 , we have
𝑁𝐺[𝑥]∩𝑁 𝐺[𝑧]=𝑁 𝐺[𝑥]=𝑁 𝐺[𝑥]∩𝑁 𝐺[𝑦], so domination
requires0<
c
𝜒𝑤CU,𝐺 𝑧→𝑥 ≤ c 𝜒𝑤CU,𝐺 𝑦→𝑥 =0, a contradiction.
We generalize the observations of Example 6.9 in three ways. First,
clone-sharing dilution is strictly stronger than clone-sharing non-
negativity.
Lemma 6.10.Clone-sharing dilution (resp. 𝑘-strong dilution) im-
plies clone-sharing non-negativity (resp. 𝑘-clone-sharing positivity),
but the converse does not hold.
Second, domination is considerably harder to satisfy: the failure of
𝑤 CU is not an isolated case, as strong domination at scale𝑘 requires
locality at scale at least2𝑘.
Lemma 6.11. 𝑘-strong clone-sharing domination is not compatible
with𝑗-locality, for any𝑗≤2𝑘−1.
Finally, Example 6.9 shows that clone-sharing dilution does not
imply clone-sharing domination; we show that the converse fails
too.
Lemma 6.12.Clone-sharing dilution and clone-sharing domination
do not imply each other.
The proofs of Lemmas 6.10, 6.11 and 6.12 are detailed in Appendix B.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer7
6.3 Constructing Interpretable Clone-Robust
Graph Weighting Functions
It remains to be seen whether the above clone-sharing properties
can actually be satisfied. We next provide a general framework
for constructing such graph weighting functions, based on two
operators on the space𝑊 of graph weighting functions. First, the
quotient lift operator𝑄 maps𝑤∈𝑊 to the graph weighting function
𝑄𝑤∈𝑊defined, for each graph𝐺∈Gand vertex𝑥∈𝑉(𝐺), by
𝑄𝑤(𝐺)(𝑥)≔ 𝑤𝐺/≡[𝑥]𝐺 

[𝑥]𝐺

 ,
where𝐺/≡ denotes the quotient graph obtained by collapsing each
class of clones[𝑥]𝐺 into a single vertex. Second, for 𝑘≥ 1, the
𝑘-hop diffusion operator 𝐷𝑘 maps𝑤∈𝑊 to the graph weighting
function𝐷 𝑘𝑤∈𝑊defined by
𝐷𝑘𝑤(𝐺)(𝑥)≔
∑︁
𝑦∈𝑁𝑘 𝐺[𝑥]
𝑤(𝐺)(𝑦)

𝑁𝑘 𝐺[𝑦]

 .
That is, each vertex spreads its weight uniformly over its 𝑘-hop
neighborhood, i.e.,𝐷𝑘 performs one step of the lazy random walk
on the𝑘-th power of𝐺.
Theorem 6.13.Let 𝑤 be a symmetric graph weighting function
and𝑘≥ 1. Then 𝑄𝑤 is a1-clone-robust graph weighting function
satisfying clone-sharing dilution. It fails 𝑘-clone-sharing positivity,
and it fails𝑘-clone-sharing domination whenever𝑤 is positive. More-
over,𝐷𝑘◦𝑄𝑤 is a2𝑘-clone-robust graph weighting function satisfy-
ing clone-sharing dilution and 𝑘-clone-sharing domination. If 𝑤 is
positive, it furthermore satisfies 𝑘-strong clone-sharing dilution and
𝑘-strong clone-sharing domination.
In particular,𝑤 CU =𝑄𝑤 U, where𝑤 U(𝐺)(𝑥)≔ 1/|𝑉(𝐺)| denotes
the uniform graph weighting function, so Example 6.9 is a special
case of Theorem 6.13. Moreover, the locality of𝐷𝑘◦𝑄𝑤 is optimal, as
no𝑗-clone-robust graph weighting function with𝑗≤ 2𝑘− 1satisfies
𝑘-strong clone-sharing domination (Lemma 6.11). Note finally that
𝐷𝑘 cannot be replaced by the𝑘-fold composition𝐷𝑘 ≔𝐷 1◦···◦𝐷 1,
even though it diffuses weight over the same𝑘-hop neighborhoods.
Lemma 6.14.There exists a symmetric graph weighting function
𝑤 such that, for every ℓ≥ 2and 𝑘≥ 1, the graph weighting function
𝐷ℓ◦𝑄𝑤 satisfies neither clone-sharing dilution nor 𝑘-clone-sharing
domination.
The proofs of Theorem 6.13 and Lemma 6.14 are detailed in Appen-
dices A and B respectively.
7 Discussion
In this section, we discuss our findings, their practical implementa-
tion and open challenges.
Summary of results.This work introduces a novel approach to
constructing clone-robust weighting functions, extending [Berri-
aud and Wattenhofer, 2025] along three dimensions: topological
invariance (supporting arbitrary metrics), efficient exact evaluation,
and Lipschitz—rather than uniform—continuity guarantees. In the
context of CIB, locality bounds the visibility a campaign can gain
by mass-producing near-duplicates (Corollary 4.4), as illustrated on
synthetic feeds. On the explainability side, sharing coefficients for
the volumetric construction of [Berriaud and Wattenhofer, 2025]
provide intuition for the graph setting, where our impossibility
results show that locality is fundamentally at odds with measur-
ing sharing through vertex or edge deletion. Sharing must thus be
defined through the addition of clones, under which dilution and
domination can be achieved jointly, at the price of a doubled, yet
unavoidable, locality radius.
Practical Instantiation in Newsfeeds.Translating this framework
into a real-world news aggregator introduces several operational
challenges, and our synthetic experiment is merely illustrative. First,
computational scalability: while computing weights across millions
of posts is prohibitive, the practical scale is arguably bounded by the
user’s attention budget. Because this is orders of magnitude smaller,
our framework can be flexibly integrated downstream, operating
directly on a pre-filtered candidate set. Second, the defense’s effi-
cacy fundamentally relies on thechoice of metric. While standard
text similarity may be vulnerable to generative AI obfuscation, our
metric-agnostic framework can directly build on the similarity mea-
sures developed for CIB detection [Cresci et al., 2016, Luceri et al.,
2024, Mannocci et al., 2026, Nizzoli et al., 2021]; identifying the most
suitable ones, together with the parameters𝛼 and𝜈, warrants an
independent empirical investigation. However, an inherent trade-
off remains: any geometric defense will inevitably penalize genuine
grassroots coordination if it is metrically indistinguishable from
bot activity. Whereas existing algorithms favor faithfully gauging
support, our work explores the side of resisting redundancy. Finally,
transparent defenses inviteadversarial adaptation: attackers may
inject clones just beyond the threshold𝛼 to evade weight redistribu-
tion. If semantic impact decays with distance, however, defenders
can fix the maximal spread𝜌 of clones they wish to protect against,
beyond which clones are no longer considered persuasive, and
choose𝛼to minimize the bound of Corollary 4.4.
Future Work.This work opens several avenues for future re-
search. First, our computational results in Appendix D suggest that
Theorem 6.4 extends to the weaker requirement of non-negative
endpoint sharing, with a contradiction arising on graphs with seven
vertices; extracting a human-checkable proof, and extending these
impossibility results to 𝑘≥ 2, remain open. Second, our clone-
sharing coefficients are defined at the level of graph weighting
functions; lifting them to the integrated weighting𝑓𝜈,𝑤 , similarly
to Appendix C, would provide explanations directly in the met-
ric space of posts. Third, while the operator𝐷𝑘◦𝑄 yields several
desirable properties, it still lacks an axiomatic characterization; al-
ternative constructions, such as maximal-clique-based weighting
functions (Appendix E), could provide deeper insights into prop-
erties like dilution and domination and open the way to such a
characterization. Finally, an empirical study on real data should
implement and validate the full defense pipeline, from the choice
of metric and of the admissible spread 𝜌 to the calibration of 𝛼,
measuring both the suppression of coordinated campaigns and the
cost to genuine content. It should also assess how our theoretical
properties translate in practice.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer8
CRediT Author Statement
Damien Berriaud:Conceptualization, Methodology, Validation,
Formal Analysis, Investigation, Writing, Visualization, Supervi-
sion.Supanat Wangsutthitham:Methodology, Software, Formal
Analysis, Investigation, Writing—First Draft, Visualization.Roger
Wattenhofer:Supervision, Funding Acquisition.
Acknowledgments
We thank Felix Quernheim for suggesting the simplified proof of
Theorem 6.13 presented here, which replaces our original, more
involved argument.
References
David Balduzzi, Karl Tuyls, Julien Perolat, and Thore Graepel. 2018. Re-evaluating
Evaluation. doi:10.48550/arXiv.1806.02643
Damien Berriaud and Roger Wattenhofer. 2025. Clone-Robust Weights in Metric
Spaces: Handling Redundancy Bias for Benchmark Aggregation. doi:10.48550/
arXiv.2502.03576 arXiv:2502.03576 [cs].
Florian Brandl, Felix Brandt, and Hans Georg Seedig. 2016. Consistent Probabilistic
Social Choice. doi:10.48550/arXiv.1503.00694 arXiv:1503.00694 [cs].
Kaidi Cao, Colin Wei, Adrien Gaidon, Nikos Arechiga, and Tengyu Ma. 2019. Learning
Imbalanced Datasets with Label-Distribution-Aware Margin Loss. doi:10.48550/
arXiv.1906.07413
Nikan Chavoshi, Hossein Hamooni, and Abdullah Mueen. 2016. DeBot: Twitter Bot
Detection via Warped Correlation. In2016 IEEE 16th International Conference on
Data Mining (ICDM). IEEE, Piscataway, NJ, USA, 817–822. doi:10.1109/ICDM.2016.
0096 ISSN: 2374-8486.
Vincent Conitzer and Makoto Yokoo. 2010. Using Mechanism Design to Prevent False-
Name Manipulations.AI Magazine31, 4 (Dec. 2010), 65–77. doi:10.1609/aimag.
v31i4.2315
Stefano Cresci, Roberto Di Pietro, Marinella Petrocchi, Angelo Spognardi, and Maurizio
Tesconi. 2016. DNA-Inspired Online Behavioral Modeling and Its Application to
Spambot Detection.IEEE Intelligent Systems31, 5 (Sept. 2016), 58–64. doi:10.1109/
MIS.2016.29
Yin Cui, Menglin Jia, Tsung-Yi Lin, Yang Song, and Serge Belongie. 2019. Class-Balanced
Loss Based on Effective Number of Samples. doi:10.48550/arXiv.1901.05555
Tuğrulcan Elmas, Rebekah Overdorf, Ahmed Furkan Özkalay, and Karl Aberer. 2021.
Ephemeral Astroturfing Attacks: The Case of Fake Twitter Trends. In2021 IEEE
European Symposium on Security and Privacy (EuroS&P). IEEE, Piscataway, NJ, USA,
403–422. doi:10.1109/EuroSP51992.2021.00035
Yoav Freund and Robert E Schapire. 1997. A Decision-Theoretic Generalization of
On-Line Learning and an Application to Boosting.J. Comput. System Sci.55, 1 (Aug.
1997), 119–139. doi:10.1006/jcss.1997.1504
Mingqi Gao, Yixin Liu, Xinyu Hu, Xiaojun Wan, Jonathan Bragg, and Arman Cohan.
2025. Re-evaluating Automatic LLM System Ranking for Alignment with Human
Preference. doi:10.48550/arXiv.2501.00560 arXiv:2501.00560 [cs].
Muhammad Abdullah Jamal, Matthew Brown, Ming-Hsuan Yang, Liqiang Wang, and
Boqing Gong. 2020. Rethinking Class-Balanced Methods for Long-Tailed Visual
Recognition from a Domain Adaptation Perspective. doi:10.48550/arXiv.2003.10780
Lu Jiang, Deyu Meng, Qian Zhao, Shiguang Shan, and Alexander G. Hauptmann. 2015.
Self-paced curriculum learning. InProceedings of the 29th AAAI Conference on
Artificial Intelligence. AAAI Press, Palo Alto, CA, USA, 2694–2700. doi:10.1609/aaai.
v29i1.9608
Gilbert Laffond, Jean Lainé, and Jean-François Laslier. 1996. Composition-consistent
tournament solutions and social choice functions.Social Choice and Welfare13, 1
(Jan. 1996), 75–93. doi:10.1007/BF00179100
Tsung-Yi Lin, Priya Goyal, Ross Girshick, Kaiming He, and Piotr Dollár. 2017. Focal
Loss for Dense Object Detection. In2017 IEEE International Conference on Computer
Vision (ICCV). IEEE, Piscataway, NJ, USA, 2999–3007. doi:10.1109/ICCV.2017.324
Siqi Liu, Ian Gemp, Luke Marris, Georgios Piliouras, Nicolas Heess, and Marc Lanctot.
2025. Re-evaluating Open-ended Evaluation of Large Language Models. doi:10.
48550/arXiv.2502.20170 arXiv:2502.20170 [cs].
Luca Luceri, Valeria Pantè, Keith Burghardt, and Emilio Ferrara. 2024. Unmasking the
Web of Deceit: Uncovering Coordinated Activity to Expose Information Operations
on Twitter. InProceedings of the ACM Web Conference 2024 (WWW ’24). Association
for Computing Machinery, New York, NY, USA, 2530–2541. doi:10.1145/3589334.
3645529
Luca Luceri, Tanishq Vijay Salkar, Ashwin Balasubramanian, Gabriela Pinto, Chenning
Sun, and Emilio Ferrara. 2026. Coordinated Inauthentic Behavior on TikTok:
Challenges and Opportunities for Detection in a Video-First Ecosystem.Proceedings
of the International AAAI Conference on Web and Social Media20, 1 (May 2026),
1533–1550. doi:10.1609/icwsm.v20i1.42711
Lorenzo Mannocci, Michele Mazza, Anna Monreale, Maurizio Tesconi, and Stefano
Cresci. 2026. Detection and Characterization of Coordinated Online Behavior: A
Survey. arXiv:2408.01257 [cs.SI] https://arxiv.org/abs/2408.01257
Luke Marris, Siqi Liu, Ian Gemp, Georgios Piliouras, and Marc Lanctot. 2025. Deviation
Ratings: A General, Clone-Invariant Rating Method. doi:10.48550/arXiv.2502.11645
arXiv:2502.11645 [cs].
Ilan Nehama, Taiki Todo, and Makoto Yokoo. 2022. Manipulation-resistant false-name-
proof facility location mechanisms for complex graphs.Autonomous Agents and
Multi-Agent Systems36, 1 (Jan. 2022). doi:10.1007/s10458-021-09535-5 Article 12.
Leonardo Nizzoli, Serena Tardelli, Marco Avvenuti, Stefano Cresci, and Maurizio
Tesconi. 2021. Coordinated Behavior on Social Media in 2019 UK General Election.
Proceedings of the International AAAI Conference on Web and Social Media15 (May
2021), 443–454. doi:10.1609/icwsm.v15i1.18074
Diogo Pacheco, Pik-Mai Hui, Christopher Torres-Lugo, Bao Tran Truong, Alessandro
Flammini, and Filippo Menczer. 2021. Uncovering Coordinated Networks on Social
Media: Methods and Case Studies.Proceedings of the International AAAI Conference
on Web and Social Media15 (May 2021), 455–466. doi:10.1609/icwsm.v15i1.18075
Ariel D. Procaccia, Benjamin Schiffer, and Shirley Zhang. 2025. Clone-Robust AI
Alignment. doi:10.48550/arXiv.2501.09254 arXiv:2501.09254 [cs].
Mengye Ren, Wenyuan Zeng, Bin Yang, and Raquel Urtasun. 2019. Learning to
Reweight Examples for Robust Deep Learning. doi:10.48550/arXiv.1803.09050
Jun Shu, Qi Xie, Lixuan Yi, Qian Zhao, and al. 2019. Meta-Weight-Net: Learning an
Explicit Mapping For Sample Weighting. doi:10.48550/arXiv.1902.07379
T. N. Tideman. 1987. Independence of clones as a criterion for voting rules.Social
Choice and Welfare4, 3 (Sept. 1987), 185–206. doi:10.1007/BF00433944
Taiki Todo, Atsushi Iwasaki, Makoto Yokoo, and Yuko Sakurai. 2009. Characterizing
False-name-proof Allocation Rules in Combinatorial Auctions. InProceedings of
the 8th International Conference on Autonomous Agents and Multiagent Systems
(AAMAS). IFAAMAS, Richland, SC, USA, 265–272.
Kai-Cheng Yang and Filippo Menczer. 2024. Anatomy of an AI-powered malicious
social botnet.Journal of Quantitative Description: Digital Media4 (May 2024).
doi:10.51685/jqd.2024.icwsm.7
A Proof of the Main Theorems
This appendix contains the proofs of the results of Sections 4 and 6.
We first establish a lemma on cluster graphs, used repeatedly below:
on disjoint unions of cliques, symmetry and locality alone determine
the weights. We then prove Theorem 4.3 and make its evaluation
procedure explicit, before turning to the two impossibility results
of Section 6.1 and to the construction of Theorem 6.13.
Lemma A.1.Let 𝑤 be a𝑘-clone-robust graph weighting function
for some𝑘> 0, and let𝐺 be a cluster graph with at least one vertex,
i.e., a finite graph whose connected components 𝐶1,...,𝐶 𝑚, with𝑚≥
1, are cliques. Then 𝑤 coincides with 𝑤 CU on𝐺, i.e., for every 𝑖∈
{1,...,𝑚}and𝑥∈𝐶 𝑖 ,
𝑤(𝐺)(𝑥)= 1 𝑚·|𝐶 𝑖| =𝑤 CU(𝐺)(𝑥).
Proof. In a cluster graph, 𝑁𝐺[𝑥]=𝐶 𝑖 for every 𝑥∈𝐶 𝑖. The
equivalence classes of≡𝐺 are therefore exactly the cliques𝐶1,...,𝐶 𝑚,
and the second equality holds by definition of𝑤 CU. We prove the
first equality by induction on𝑛(𝐺) :=|𝑉(𝐺)|−𝑚≥ 0, the number
of vertices in excess of one per component.
Base case.If 𝑛(𝐺)= 0, every component is a single vertex and𝐺
has no edges. Every permutation of𝑉(𝐺) is then a graph automor-
phism of𝐺, so symmetry of𝑤 implies that all𝑚 vertices receive
the same weight, i.e.,𝑤(𝐺)(𝑥)=1/𝑚for all𝑥∈𝑉(𝐺).
Induction step.Let 𝑛(𝐺) ≥1, and assume the claim holds for
all cluster graphs𝐺′ with𝑛(𝐺′)=𝑛(𝐺)− 1. Some clique𝐶𝑖 then
contains two distinct vertices𝑥≠𝑦 , which are equivalent in𝐺. The
graph𝐺′ =𝐺\{𝑦} is again a cluster graph with𝑚 components,
𝐶𝑖\{𝑦} and𝐶𝑗 for 𝑗≠𝑖 , and𝑛(𝐺′)=𝑛(𝐺)− 1. Every𝑧∉𝐶 𝑖 lies
in another component and satisfies𝑑𝐺(𝑥,𝑧)=∞>𝑘 . By𝑘-locality
and the induction hypothesis, 𝑤(𝐺)(𝑧)=𝑤(𝐺 ′)(𝑧)= 1/(𝑚|𝐶𝑗|)
for every𝑧∈𝐶 𝑗 with𝑗≠𝑖 . Since𝑤(𝐺) is a probability distribution,

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer9
𝐶𝑖 receives total weight
1−
∑︁
𝑗≠𝑖
|𝐶𝑗|· 1 𝑚|𝐶𝑗| =1− 𝑚−1 𝑚 = 1 𝑚.
Finally, every permutation of𝐶𝑖 that fixes all other vertices is an
automorphism of𝐺, so symmetry splits this weight equally among
the vertices of𝐶𝑖, which yields 𝑤(𝐺)(𝑥)= 1/(𝑚|𝐶𝑖|) for all𝑥∈
𝐶𝑖.□
We now turn to Theorem 4.3, whose proof treats each property
in turn; positivity relies on Lemma A.1, since every neighborhood
graph at a radius below the smallest positive distance in 𝑆 is a
cluster graph. We first recall its statement.
Theorem 4.3.Let 𝑤 be a𝑘-clone-robust graph weighting function,
𝛼 be a positive radius, and 𝜈 be a probability density function with
support[0,𝛼]and value bounded by 𝜈.
For every finite subset𝑆⊆𝑀and every𝑥∈𝑆, define
𝑓𝜈,𝑤(𝑆)(𝑥)=
∫ 𝛼
0
𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝑥)𝑑𝑟.
Then𝑓𝜈,𝑤 is a weighting function of(𝑀,𝑑) and satisfies the following
properties for all𝑆∈P(𝑀)and all𝑥∈𝑆:
•Positivity, i.e.,𝑓 𝜈,𝑤(𝑆)(𝑥)>0;
• Symmetry, i.e., 𝑓𝜈,𝑤(𝑆)(𝑥)=𝑓 𝜈,𝑤(𝑆)(𝜎(𝑥)) for every self-
isometry𝜎:𝑆↦→𝑆.
• Lipschitz Clone Fairness, i.e.,|𝑓𝜈,𝑤(𝑆)(𝑥)−𝑓 𝜈,𝑤(𝑆)(𝑦)|≤
2𝜈|𝑆|𝑑(𝑥,𝑦)for each𝑦∈𝑆.
• Lipschitz Continuity, i.e.,|𝑓𝜈,𝑤(𝑆)(𝑥)−𝑓 𝜈,𝑤(𝜋(𝑆))(𝜋(𝑥))|≤
2𝜈|𝑆| 2 max𝑥∈𝑆 𝑑(𝑥,𝜋(𝑥)) , for each bijection𝜋 :𝑆↦→𝜋(𝑆)⊆
𝑀.
• Lipschitz(𝑘𝛼) -Locality, i.e., if𝑑(𝑥,𝑦)≥𝑘𝛼 , then|𝑓𝜈,𝑤(𝑆∪
𝑍)(𝑦)−𝑓 𝜈,𝑤(𝑆)(𝑦)|≤
2𝜈|𝑆|max 𝑧∈𝑍 𝑑(𝑥,𝑧)for each𝑦∈𝑆
Moreover,𝑓𝜈,𝑤(𝑆)(𝑥) can be computed in time 𝑂𝑚2(𝑊(𝑚)+𝐶 𝜈+
𝐶𝑑+log𝑚) , where𝑊(𝑚) ,𝐶𝜈 and𝐶𝑑 are the respective worst-case
evaluation complexity of:𝑤 over all graphs with𝑚 vertices; the cumu-
lative distribution of𝜈 at a single real argument; and the pseudo-metric
𝑑.
Proof. Let𝑆 be a finite subset of𝑀 and𝑥 be an element in𝑆.
We denote byD𝑥 𝑆 ={𝑑(𝑥,𝑧)|𝑧∈𝑆} the set of distances between
𝑥 and the elements of𝑆, and byD𝑆 = — 𝑥∈𝑆D𝑥 𝑆 the set of pairwise
distances in𝑆. Note that0 =𝑑(𝑥,𝑥) belongs to both sets, and that
|D𝑥 𝑆\{ 0}|≤|𝑆|− 1and |D𝑆\{ 0}|≤|𝑆|(|𝑆|− 1)/2byidentityand
symmetryof the pseudo-metric𝑑.
• Well-definedness and Positivity:Let0 <𝑟 1 <···<𝑟 ℓ be
the increasing list of the distinct positive values inD𝑆, where
ℓ :=|D 𝑆\{ 0}|≤|𝑆|(|𝑆|− 1)/2, and set𝑟0 := 0and 𝑟ℓ+1 :=∞ .
The edge set𝐸𝑟(𝑆) is constant on each semi-open interval
𝐼𝑗 =[𝑟 𝑗,𝑟 𝑗+1),𝑗∈{ 0,...,ℓ} , which partition R≥0. Hence the
map𝑟↦→𝑤(𝐺 𝑟(𝑆))(𝑥) is piecewise constant with at most
ℓ+ 1pieces. Since 𝜈 is a bounded measurable function, the
map𝑟↦→𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝑥) is integrable and 𝑓𝜈,𝑤(𝑆)(𝑥) is
well defined.
For positivity, note that for 𝑟∈𝐼 0 =[ 0,𝑟 1), two elements
of𝑆 are adjacent in𝐺𝑟(𝑆) if and only if they are at distance
zero. By the triangle inequality, being at distance zero is
an equivalence relation, so 𝐺𝑟(𝑆) is a cluster graph, and
Lemma A.1 yields 𝑤(𝐺𝑟(𝑆))(𝑥) ≥ 1/|𝑆| 2. Since 𝜈 and𝑤
are non-negative and the support of𝜈 is[0,𝛼] , the interval
[0,min(𝑟 1,𝛼)) has positive𝜈-measure, and we conclude that
𝑓𝜈,𝑤(𝑆)(𝑥) ≥
∫ min(𝑟 1,𝛼)
0
𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝑥)𝑑𝑟
≥ 1 |𝑆| 2
∫ min(𝑟 1,𝛼)
0
𝜈(𝑟)𝑑𝑟>0.
• Evaluation Complexity:To evaluate 𝑓𝜈,𝑤(𝑆)(𝑥) , we pro-
ceed in three steps, as detailed in Algorithm 1. Let Γ denote
the cumulative distribution function of𝜈.
(1) Distances.Compute 𝑑(𝑢,𝑣) for all𝑢,𝑣∈𝑆 , which yields
D𝑆 in time𝑂(|𝑆| 2𝐶𝑑). Discard the values greater than or
equal to𝛼 and sort the remaining ones, at an additional
cost𝑂(|𝑆| 2 log|𝑆|) . This yields the threshold radii0 =𝑟 0 <
𝑟1 <···<𝑟 ℓ𝛼 <𝛼 , where ℓ𝛼 ≤ℓ≤|𝑆|(|𝑆|− 1)/2; we
further set𝑟 ℓ𝛼+1 :=𝛼.
(2) Graphs at threshold radii.For each 𝑖∈ {0,...,ℓ 𝛼}, con-
struct𝐺𝑟𝑖(𝑆) incrementally from𝐺𝑟𝑖−1(𝑆) by adding the
edges between elements at distance exactly𝑟𝑖. Then evalu-
ate𝑤(𝐺𝑟𝑖(𝑆))(𝑥) and Γ(𝑟𝑖+1), at cost𝑂(𝑊(|𝑆|)+𝐶 𝜈) per
index.
(3) Integration.Since 𝐺𝑟(𝑆)=𝐺 𝑟𝑖(𝑆) for all 𝑟∈ [𝑟 𝑖,𝑟𝑖+1),
we have𝑓𝜈,𝑤(𝑆)(𝑥)= ˝ℓ𝛼 𝑖=0 Γ(𝑟𝑖+1)−Γ(𝑟 𝑖)𝑤(𝐺𝑟𝑖(𝑆))(𝑥) ,
which is accumulated along the loop.
Overall, the above procedure results in worst-case time com-
plexity𝑂 |𝑆| 2(𝑊(|𝑆|)+𝐶 𝜈+𝐶𝑑+log|𝑆|) .
• Symmetry:Let 𝜎 :𝑆↦→𝑆 be a self-isometry and𝑟≥ 0be
a positive radius. Note that 𝜎 is a graph automorphism of
𝐺𝑟(𝑆) : indeed,𝑢,𝑣∈𝑆 are adjacent in𝐺𝑟(𝑆) if and only if
𝑑(𝜎(𝑢),𝜎(𝑣))=𝑑(𝑢,𝑣)≤𝑟 , that is if and only if 𝜎(𝑢) and
𝜎(𝑣) are adjacent in𝐺𝑟(𝑆). By symmetry of𝑤, we then have,
i.e.,
𝑓𝜈,𝑤(𝑆)(𝜎(𝑥))=
∫ 𝛼
0
𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝜎(𝑥))𝑑𝑟,
=
∫ 𝛼
0
𝜈(𝑟)𝑤(𝐺 𝑟(𝑆))(𝑥)𝑑𝑟=𝑓 𝜈,𝑤(𝑆)(𝑥),
and𝑓 𝜈,𝑤(𝑆)is symmetric.
• Lipschitz Clone-Fairness:Let 𝑦 be an element of𝑆, and let
𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆)= — 𝑧∈𝑆[𝑑(𝑥,𝑧)−𝑑(𝑥,𝑦),𝑑(𝑥,𝑧)+𝑑(𝑥,𝑦)] de-
note the union of closed balls of R of radius𝑑(𝑥,𝑦) centered
around the elements ofD 𝑥 𝑆 .
For a radius𝑟 in[0,𝛼]\ 𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆), note that𝑥 and𝑦 are
equivalent in𝐺𝑟(𝑆). Indeed, for𝑢∈𝑆 with𝑟≥𝑑(𝑥,𝑢) , we
also have𝑟≥𝑑(𝑥,𝑢)+𝑑(𝑥,𝑦)≥𝑑(𝑦,𝑢) by definition of𝑟
and the triangle inequality, hence𝑢 is connected to both𝑥
and𝑦 in𝐺𝑟(𝑆). For𝑢∈𝑆 such that𝑟<𝑑(𝑥,𝑢) , a similar
argument gives 𝑟<𝑑(𝑥,𝑢)−𝑑(𝑥,𝑦)≤𝑑(𝑦,𝑢) and𝑢 is a
neighbor of neither 𝑥 nor𝑦. In particular, the case 𝑢=𝑥 ,
with𝑑(𝑥,𝑥)=0∈D 𝑥 𝑆 , ensures that𝑥and𝑦are adjacent.
Let𝜎 :𝑆→𝑆 be the transposition that exchanges𝑥 and𝑦,
i.e.,𝜎(𝑥)=𝑦 ,𝜎(𝑦)=𝑥 and𝜎(𝑧)=𝑧 for all𝑧∈𝑆\{𝑥,𝑦}.
Since𝑥 and𝑦 have the same closed neighborhood, 𝜎 is a

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer10
graph automorphism of𝐺𝑟(𝑆) for all𝑟∈[ 0,𝛼]\𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆),
and thesymmetryof𝑤implies
|𝑓𝜈,𝑤(𝑆)(𝑥)−𝑓 𝜈,𝑤(𝑆)(𝑦)|
≤
∫ 𝛼
0
𝜈(𝑟)

𝑤(𝐺𝑟(𝑆))(𝑥)−𝑤(𝐺 𝑟(𝑆))(𝜎(𝑥))

𝑑𝑟,
(𝑎)
≤
∫
[0,𝛼]∩𝐵𝑑(𝑥,𝑦) (D𝑥 𝑆)
𝜈(𝑟)𝑑𝑟,
(𝑏)
≤2 𝜈|𝑆|𝑑(𝑥,𝑦).
(4)
Inequality(𝑎) uses that the difference of weights is null on
[0,𝛼]\ 𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆) bysymmetryof 𝑤, and bounded by one
on[0,𝛼]∩ 𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆). Inequality(𝑏) uses the bound on
the probability density function 𝜈, as well as the fact that
the Lebesgue measure of[0,𝛼]∩ 𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆) is bounded by
that of𝐵𝑑(𝑥,𝑦)(D𝑥 𝑆), which is in turn bounded by|D𝑥 𝑆|≤|𝑆|
times the measure of each interval2𝑑(𝑥,𝑦).
• Lipschitz Continuity:Let 𝑇 be a finite subset of𝑀 of car-
dinality|𝑇|=|𝑆| , and let 𝜋 : 𝑆→𝑇 be a bijective map.
We denote the maximal distance between elements of𝑆 and
their image in 𝑇 as𝛿 :=max 𝑢∈𝑆 𝑑(𝑢,𝜋(𝑢)) and consider
𝐵2𝛿(D𝑆)= — 𝑢,𝑣∈𝑆[𝑑(𝑢,𝑣)− 2𝛿,𝑑(𝑢,𝑣)+ 2𝛿] the union of
closed balls of R of radius2𝛿 centered around the elements
ofD𝑆.
For a radius𝑟∈[ 0,𝛼]\ 𝐵2𝛿(D𝑆), note that𝐺𝑟(𝑆) and𝐺𝑟(𝑇)
are isomorphic, i.e.,𝑢,𝑣∈𝑆 are connected in𝐺𝑟(𝑆) if and
only if 𝜋(𝑢) and 𝜋(𝑣) are connected in 𝐺𝑟(𝑇). Indeed, if
𝑟≥𝑑(𝑢,𝑣) , then we also have𝑟≥𝑑(𝑢,𝑣)+ 2𝛿≥𝑑(𝑢,𝑣)+
𝑑(𝑢,𝜋(𝑢))+𝑑(𝑣,𝜋(𝑣)) ≥𝑑(𝜋(𝑢),𝜋(𝑣)) by definition of 𝑟
and𝛿, as well as by the triangle inequality. Hence 𝜋(𝑢) is
connected to𝜋(𝑣) in𝐺𝑟(𝑇). Similarly if𝑟<𝑑(𝑢,𝑣) , we also
have𝑟<𝑑(𝑢,𝑣)− 2𝛿≤𝑑(𝑢,𝑣)−𝑑(𝑢,𝜋(𝑢))−𝑑(𝑣,𝜋(𝑣))≤
𝑑(𝜋(𝑢),𝜋(𝑣))and𝜋(𝑢)is not a neighbor of𝜋(𝑣)in𝐺 𝑟(𝑇).
Similarly to Equation 4, we conclude using thesymmetryof
𝑤, i.e.,

𝑓𝜈,𝑤(𝑆)(𝑥)−𝑓 𝜈,𝑤(𝜋(𝑆))(𝜋(𝑥))

≤ ∫
[0,𝛼]∩𝐵2𝛿(D𝑆)
𝜈(𝑟)𝑑𝑟,
≤2 𝜈|𝑆| 2 max
𝑢∈𝑆
𝑑(𝑢,𝜋(𝑢)).
The last inequality uses that the Lebesgue measure of R≥0∩
𝐵2𝛿(D𝑆) is bounded by the cardinality|D𝑆\{ 0}|≤|𝑆|(|𝑆|−
1)/2times the diameter of each interval4 𝛿, plus2𝛿 for the
interval[0, 2𝛿] centered at0, which in total is at most2|𝑆| 2𝛿.
• Lipschitz(𝑘𝛼) -Locality:Let 𝑦 be an element of𝑆 such that
𝑑(𝑥,𝑦)≥𝑘𝛼 , let𝑍={𝑧 1,...,𝑧 |𝑍|}⊆𝑀\𝑆 be finite, and let
𝑧∈𝑍 be a maximizer of𝑑(𝑥,𝑧) . Denote Λ :=𝐵𝑑(𝑥,𝑧)(D𝑥 𝑆)∪
[0, 2𝑑(𝑥,𝑧)] . For a radius𝑟 in[0,𝛼)\Λ and any𝑍′⊆𝑍 , note
first that the graph distance between𝑥 and𝑦 in𝐺𝑟(𝑆∪𝑍 ′)
strictly exceeds𝑘. This is due to triangle inequality: suppose
𝑑𝐺𝑟(𝑆∪𝑍′)(𝑥,𝑦)=𝑙 . Observe that any path of length 𝑙 in
𝐺𝑟(𝑆∪𝑍 ′) can cover the distance in metric space at most𝑙𝑟 .
Since𝛼>𝑟 , we have𝑙𝛼>𝑙𝑟 . The path connecting𝑥 and𝑦
must be of length, by definition, at least𝑑(𝑥,𝑦)≥𝑘𝛼 , so we
have
𝑙𝛼>𝑙𝑟≥𝑑(𝑥,𝑦)≥𝑘𝛼.
Dividing by𝛼 gives𝑙>𝑘 , so we know that𝑑𝐺𝑟(𝑆∪𝑍′)(𝑥,𝑦)>
𝑘. Furthermore, every𝑧′∈𝑍 ′ is equivalent to𝑥 in𝐺𝑟(𝑆∪𝑍′).
Indeed, for𝑢∈𝑆 , the triangle inequality gives |𝑑(𝑧′,𝑢)−
𝑑(𝑥,𝑢)|≤𝑑(𝑥,𝑧 ′)≤𝑑(𝑥,𝑧) , while𝑟∉[𝑑(𝑥,𝑢)−𝑑(𝑥,𝑧),𝑑(𝑥,𝑢)+
𝑑(𝑥,𝑧)] , so𝑢 is adjacent to𝑧′ if and only if it is adjacent to
𝑥; and since𝑟> 2𝑑(𝑥,𝑧) , the elements of𝑍′∪{𝑥} are pair-
wise adjacent. In particular,𝑧𝑖 is equivalent to𝑥 in𝐺𝑟(𝑆∪
{𝑧1,...,𝑧 𝑖}) for every𝑖, irrespective of the order in which
the elements of 𝑍 are enumerated. Denote 𝑓𝑖 ≔𝑓 𝜈,𝑤(𝑆∪
{𝑧1,𝑧 2,...,𝑧 𝑖})(𝑦) and𝑤𝑟 𝑖 ≔𝑤(𝐺 𝑟(𝑆∪{𝑧 1,𝑧 2,...,𝑧 𝑖}))(𝑦) .
We follow a similar approach to one in Equation 4, while also
expanding the integrand to a telescopic sum using triangle
inequality and iteratively use𝑘-localityof 𝑤 to collapse them
to 0, i.e.,

𝑓|𝑍|−𝑓 0

≤ ∫ 𝛼
0
𝜈(𝑟)

𝑤𝑟 |𝑍|−𝑤𝑟 0

𝑑𝑟
=
∫
[0,𝛼)\Λ
𝜈(𝑟)

𝑤𝑟 |𝑍|−𝑤𝑟 0

𝑑𝑟
+
∫
[0,𝛼)∩Λ
𝜈(𝑟)

𝑤𝑟 |𝑍|−𝑤𝑟 0

 |       {z       }
≤1
𝑑𝑟
≤
∫
[0,𝛼)\Λ
𝜈(𝑟)
|𝑍|∑︁
𝑖=1

𝑤𝑟 𝑖−𝑤𝑟 𝑖−1|      {z      }
0

𝑑𝑟
+
∫
[0,𝛼)∩Λ
𝜈(𝑟)𝑑𝑟
≤0+2 𝜈|𝑆|𝑑(𝑥,𝑧).
The last inequality uses that the Lebesgue measure ofΛ∩R≥0
is at most|D 𝑥 𝑆\{0}|·2𝑑(𝑥,𝑧)+2𝑑(𝑥,𝑧)≤2|𝑆|𝑑(𝑥,𝑧).
□
The complexity bound relies on the fact that𝑟↦→𝐺 𝑟(𝑆) is piece-
wise constant, changing only at the pairwise distances in 𝑆. Al-
gorithm 1 makes the resulting procedure explicit: it sorts these
distances once, then evaluates 𝑤 on each distinct neighborhood
graph, weighted by the𝜈-mass of the corresponding radius interval.
We next prove the two impossibility results of Section 6.1. Both
proofs follow the same pattern: starting from cluster graphs, whose
weights are fixed by Lemma A.1, we add or remove single vertices or
edges and propagate the resulting constraints until a contradiction
arises. We begin with vertex sharing, for which a single graph
suffices.
Theorem 6.2.For every 𝑘> 0and every 𝑘-clone-robust graph
weighting function𝑤, there exists a finite graph 𝐺∈G and distinct
vertices𝑢,𝑣∈𝑉(𝐺)such that𝑤(𝐺\{𝑢})(𝑣)<𝑤(𝐺)(𝑣).
Proof.Let𝑤be𝑘-clone-robust, and suppose for contradiction
that𝑤(𝐺\{𝑢})(𝑣) ≥𝑤(𝐺)(𝑣) for every graph 𝐺 and distinct
vertices𝑢,𝑣∈𝑉(𝐺) . Consider the graph𝐺≔𝑃 3∪ 3𝐾1, consisting
of a path𝑎−𝑏−𝑐and three isolated vertices𝑑,𝑒,𝑓:
𝑎 𝑏 𝑐 𝑑 𝑒 𝑓
By symmetry of𝑤, the isolated vertices𝑑,𝑒,𝑓 receive a common
weight𝛼, the leaves 𝑎,𝑐 a common weight 𝛽, and we write 𝛾≔

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer11
ALGORITHM 1:Evaluate𝑓 𝜈,𝑤(𝑆)(𝑥)
Input: Finite subset𝑆⊆𝑀 , element𝑥∈𝑆 , graph weighting function
𝑤, radius𝛼>0, cumulative distribution functionΓassociated
with probability density𝜈over[0,𝛼].
Output:Value of𝑓 𝜈,𝑤(𝑆)(𝑥).
Initialize empty dictionaryE:R→2 𝑆×𝑆 ;
foreach𝑦,𝑧∈𝑆do
Compute𝑟←𝑑(𝑦,𝑧);
if𝑟<𝛼then
Append(𝑦,𝑧)toE(𝑟);
end
end
Extract and sort keys ofEin ascending order to obtain distinct radii
0=𝑟 0 <𝑟 1 <···<𝑟 ℓ𝛼 <𝑟 ℓ𝛼+1 =𝛼;
Initialize𝑓 𝜈,𝑤(𝑆)(𝑥)←0;
Initialize graph𝐺with vertex set𝑆and edge setE(𝑟 0);
Γcurr←0;
for𝑖=0toℓ 𝛼 do
Compute𝑤𝑖←𝑤(𝐺)(𝑥);
ComputeΓ next←Γ(𝑟 𝑖+1);
Update𝑓 𝜈,𝑤(𝑆)(𝑥)←𝑓 𝜈,𝑤(𝑆)(𝑥)+(Γ next−Γ curr)·𝑤 𝑖;
UpdateΓ curr←Γ next;
Add edge setE(𝑟 𝑖+1)to graph𝐺;
end
return𝑓 𝜈,𝑤(𝑆)(𝑥);
𝑤(𝐺)(𝑏), so that
3𝛼+2𝛽+𝛾=1.
We now remove single vertices from𝐺; in both cases, the result-
ing graph is a cluster graph, whose weights are given by Lemma A.1.
• Removing the leaf 𝑐 yields𝐺\{𝑐}=𝐾 2∪ 3𝐾1, with four
components, so that 𝑎 and𝑏 receive weight 1 4· 1 2 = 1 8 . By
assumption,𝛽=𝑤(𝐺)(𝑎)≤ 1 8 and𝛾=𝑤(𝐺)(𝑏)≤ 1 8 .
• Removing the center𝑏 yields𝐺\{𝑏}= 5𝐾1, so that𝑑 receives
weight 1 5 . By assumption,𝛼=𝑤(𝐺)(𝑑)≤ 1 5 .
Combining these bounds, we get
1=3𝛼+2𝛽+𝛾≤ 3 5+ 2 8+ 1 8 = 39 40,
a contradiction.□
The proof of Theorem 6.4 applies the same strategy to the longer
sequence of graphs depicted in Figure 5, where each arrow indicates
the operation relating two graphs. Unlike the previous proof, it uses
1-locality between vertices at distance two, which is why it is only
stated for𝑘=1.
Theorem 6.4.There exists no1-clone-robust graph weighting func-
tion that simultaneously satisfies endpoint expansion and bystander
contraction.
Proof. Suppose for contradiction that 𝑤 is a1-clone-robust
graph weighting function satisfying both endpoint expansion and
bystander contraction. We successively determine the weights of
the graphs depicted in Figure 5. Throughout,𝜇 denotes the expand-
ing constant of the edge considered in each step, and weights of
cluster graphs are given by Lemma A.1.
• Path𝑃3.Removing𝑒={ 2, 3} yields𝐾2∪𝐾1, in which vertices
2and3have weights 1 4 and 1 2 . Endpoint expansion gives 1
4 =𝜇𝑤(𝑃 3)( 2) and 1 2 =𝜇𝑤(𝑃 3)( 3), so that 𝑤(𝑃 3)( 3)=
2𝑤(𝑃 3)( 2). By symmetry and normalization,𝑤(𝑃 3)( 2)= 1 5
and𝑤(𝑃 3)(1)=𝑤(𝑃 3)(3)= 2 5 .
• Paw𝐺𝑝, obtained by adding a clone4of vertex1to 𝑃3. Since
𝑑𝐺𝑝(1, 3)= 2,1-locality gives 𝑤(𝐺𝑝)( 3)= 2 5 . Removing
{2, 3} yields𝐾3∪𝐾 1, so that endpoint expansion gives 1 2 =
𝜇· 2 5 and 1 6 =𝜇𝑤(𝐺 𝑝)( 2), i.e.,𝜇= 5 4 and𝑤(𝐺𝑝)( 2)= 2 15 . By
symmetry and normalization,𝑤(𝐺 𝑝)(1)=𝑤(𝐺 𝑝)(4)= 7 30 .
• Path𝑃4 =𝐺𝑝−{ 2, 4}.Endpoint expansion gives 𝑤(𝑃 4)( 4)=
7
30𝜇 and𝑤(𝑃 4)( 2)= 2 15𝜇. By symmetry of𝑃4 and normaliza-
tion,2  7 30+ 4 30 𝜇= 1, so that𝜇= 15 11 ,𝑤(𝑃 4)( 3)=𝑤(𝑃 4)( 4)= 7
22 , and𝑤(𝑃 4)(1)=𝑤(𝑃 4)(2)= 2 11 .
• Graph𝐺0 =𝑃 4−{ 2, 3}, consisting of the path4 − 1− 2
and the isolated vertex3. Endpoint expansion on{2, 3} gives
𝑤(𝐺 0)( 2)/𝑤(𝐺 0)( 3)= 2/11 7/22 = 4 7 . Moreover,𝐺0−{ 1, 2}=
𝐾2∪ 2𝐾1 assigns 1 6 to vertex1and 1 3 to vertex2, so that
endpoint expansion on{1, 2} gives𝑤(𝐺 0)( 1)= 1 2𝑤(𝐺 0)( 2).
Using𝑤(𝐺 0)( 4)=𝑤(𝐺 0)( 2) by symmetry, normalization
yields𝑤(𝐺 0)( 3)= 7 17 ,𝑤(𝐺 0)( 2)=𝑤(𝐺 0)( 4)= 4 17 , and
𝑤(𝐺 0)(1)= 2 17 .
• Star𝑆=𝐾 1,3 =𝐺 0+{ 1, 3}.Endpoint expansion on {1, 3}
gives𝑤(𝑆)( 3)/𝑤(𝑆)( 1)= 7/17 2/17 = 7 2 . By symmetry and nor-
malization,𝑤(𝑆)( 1)= 2 23 and every leaf of 𝑆 has weight 7
23 .
• Graph𝐺1, obtained by adding a clone5of vertex4to 𝐺0.
Since 𝑑𝐺1(4, 2)= 2and 𝑑𝐺1(4, 3)=∞ ,1-locality gives
𝑤(𝐺 1)( 2)= 4 17 and𝑤(𝐺 1)( 3)= 7 17 . Removing{1, 2} yields
𝐾3∪ 2𝐾1, so that endpoint expansion gives 1 3 =𝜇· 4 17 and 1
9 =𝜇𝑤(𝐺 1)(1), i.e.,𝜇= 17 12 and𝑤(𝐺 1)(1)= 4 51 .
• Cricket𝐺𝑐 =𝐺 1+{ 1, 3}, which is also obtained by adding
a clone5of vertex4to 𝑆. Since 𝑑𝐺𝑐(4, 2)=𝑑 𝐺𝑐(4, 3)=
2,1-locality gives 𝑤(𝐺𝑐)( 2)=𝑤(𝐺 𝑐)( 3)= 7 23 . Endpoint
expansion on{1, 3} gives 7 17 =𝜇· 7 23 and 4 51 =𝜇𝑤(𝐺 𝑐)( 1), i.e.,
𝜇= 23 17 and𝑤(𝐺𝑐)( 1)= 4 69 . By symmetry and normalization,
𝑤(𝐺𝑐)(4)=𝑤(𝐺 𝑐)(5)= 1 6 .
• Bowtie𝐺𝑏 =𝐺 𝑐+{ 2, 3}.The bowtie is also obtained by
adding a clone of the pendant vertex3to the paw 𝐺𝑝, whose
vertices1and4lie at distance2from it. Hence,1-locality
and symmetry imply that all four non-central vertices of
𝐺𝑏 have weight 7 30 , and normalization gives𝑤(𝐺𝑏)( 1)= 1 15 .
We finally apply bystander contraction to𝑒={ 2, 3}, with
𝐺𝑏−𝑒=𝐺 𝑐 and contracting constant𝜂. Since4 ∉𝑁 𝐺𝑏[2]∪
𝑁𝐺𝑏[3], equality holds for vertex4, i.e., 1 6 =𝜂· 7 30 , so that
𝜂= 5 7 . For the non-incident vertex1, bystander contraction
then requires
4
69 =𝑤(𝐺 𝑐)(1)≤𝜂𝑤(𝐺 𝑏)(1)= 5 7· 1 15 = 1 21,
which is false since4·21=84>69, a contradiction.
□
Finally, we prove Theorem 6.13. The proof first expresses𝐷𝑘◦𝑄𝑤
as a sum over equivalence classes, from which locality and each
clone-sharing property follow by direct computation.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer12
1 2 3
𝑃3
1 2 3
4
𝐺𝑝
4 1 2 3
𝑃4
4 1 2 3
𝐺0
1
2
3
4
𝑆
1
2
3
4
5
𝐺1
1
2
3
4
5
𝐺𝑐
1
2
3
4
5
𝐺𝑏
Figure 5: The sequence of graphs used in the proof of Theorem 6.4.
Theorem 6.13.Let 𝑤 be a symmetric graph weighting function
and𝑘≥ 1. Then 𝑄𝑤 is a1-clone-robust graph weighting function
satisfying clone-sharing dilution. It fails 𝑘-clone-sharing positivity,
and it fails𝑘-clone-sharing domination whenever𝑤 is positive. More-
over,𝐷𝑘◦𝑄𝑤 is a2𝑘-clone-robust graph weighting function satisfy-
ing clone-sharing dilution and 𝑘-clone-sharing domination. If 𝑤 is
positive, it furthermore satisfies 𝑘-strong clone-sharing dilution and
𝑘-strong clone-sharing domination.
Proof. We first state a helpful decomposition and then prove
each point one after the other.
• Class decomposition.For each class 𝐶∈𝑉(𝐺)/≡ 𝐺, we
denote𝑊𝐶 :=𝑤(𝐺/≡)(𝐶) and𝑛𝐶 :=|𝑁 𝑘 𝐺[𝑢]| for any𝑢∈𝐶 .
Grouping the terms of𝐷𝑘◦𝑄𝑤(𝐺)(𝑣) by classes and using
𝑄𝑤(𝐺)(𝑢)=𝑊 [𝑢]/|[𝑢]𝐺|, each class𝐶⊆𝑁 𝑘 𝐺[𝑣] contributes
|𝐶|·𝑊 𝐶/(|𝐶|𝑛 𝐶), so that
𝐷𝑘◦𝑄𝑤(𝐺)(𝑣)=
∑︁
𝐶⊆𝑁𝑘 𝐺[𝑣]
𝑊𝐶
𝑛𝐶
,(5)
where the sum ranges over the classes 𝐶∈𝑉(𝐺)/≡ 𝐺 con-
tained in𝑁 𝑘 𝐺[𝑣].
• Well-definedness and symmetry.Since 𝑤(𝐺/≡) is a prob-
ability distribution,˝ 𝑢∈𝑉(𝐺) 𝑄𝑤(𝐺)(𝑢)= ˝ 𝐶|𝐶|·𝑊 𝐶/|𝐶|=
1. Since each vertex 𝑢 distributes its mass uniformly over
𝑁𝑘 𝐺[𝑢],𝐷𝑘 maps probability distributions to probability dis-
tributions. Any graph isomorphism 𝜎 maps equivalence
classes to equivalence classes, induces an isomorphism of
the quotient graphs, and preserves𝑘-neighborhoods; hence
both𝑄𝑤and𝐷 𝑘◦𝑄𝑤inherit the symmetry of𝑤.
• Locality.Let 𝑦≡ 𝐺 𝑥 with𝑦≠𝑥 , let𝐺′ ≔𝐺\{𝑦} , and let
𝑧∈𝑉(𝐺 ′). Since𝐺 and𝐺′ have the same quotient graph,
they also have the same weights𝑊𝐶, and the same classes
except for[𝑥]𝐺′, which loses one element. If 𝑑𝐺(𝑥,𝑧)> 1,
then𝑧∉[𝑥] 𝐺, and therefore 𝑄𝑤(𝐺′)(𝑧)=𝑊 [𝑧]/|[𝑧]|=
𝑄𝑤(𝐺)(𝑧). Thus,𝑄𝑤is1-local.
If𝑑𝐺(𝑥,𝑧)> 2𝑘, then[𝑥]𝐺 ⊈𝑁 𝑘 𝐺[𝑧], so that the classes
contained in 𝑁𝑘[𝑧] are the same in 𝐺 and𝐺′. Moreover,
removing𝑦 only changes𝑛𝐶 for the classes𝐶⊆𝑁 𝑘 𝐺[𝑥] , and
no such class can be contained in𝑁𝑘 𝐺[𝑧], since it would yield
𝑑𝐺(𝑥,𝑧)≤ 2𝑘. Hence, every term of Equation (5) is the same
in𝐺 and𝐺′, and𝐷𝑘◦𝑄𝑤(𝐺 ′)(𝑧)=𝐷 𝑘◦𝑄𝑤(𝐺)(𝑧) , i.e., it
is2𝑘-local.
• Clone-sharing coefficients.Fix 𝑥,𝑦∈𝑉(𝐺) and𝑖≥ 0,
with𝐺 0 𝑥 ≔𝐺 . Note that 𝐺𝑖 𝑥 has the same quotient graph
and weights𝑊𝐶 as𝐺, the class of 𝑥 has size 𝑐+𝑖 where
𝑐 :=|[𝑥] 𝐺|, and the classes contained in𝑁𝑘[𝑦] are the same
as in 𝐺. Moreover, its 𝑘-neighborhood sizes are 𝑛𝐶+𝑖 if
𝐶⊆𝑁 𝑘 𝐺[𝑥], and𝑛 𝐶 otherwise. Therefore, we have
c
𝜒𝑄𝑤,𝐺𝑖𝑥 𝑦→𝑥 =    𝑊[𝑥]  1 𝑐+𝑖 − 1 𝑐+𝑖+1  if𝑦≡ 𝐺 𝑥, 0otherwise, (6)
and, using that only the classes contained in both𝑁𝑘 𝐺[𝑦] and
𝑁𝑘 𝐺[𝑥]contribute in Equation (5),
c
𝜒𝐷𝑘◦𝑄𝑤,𝐺𝑖𝑥 𝑦→𝑥 = ∑︁
𝐶⊆𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑦]
𝑊𝐶
(𝑛𝐶+𝑖)(𝑛 𝐶+𝑖+1) .(7)
• Properties of𝑄𝑤 .Note that the clone-sharing coefficients
of𝑄𝑤 in Equation (6) are non-increasing in𝑖, so𝑄𝑤 satisfies
clone-sharing dilution. To show that𝑄𝑤 fails𝑘-positivity
(and𝑘-domination for positive𝑤), let𝐺=𝑃 3 with vertices
𝑎−𝑏−𝑐 . Since𝑏. 𝐺 𝑎 and𝑑𝐺(𝑎,𝑏)= 1≤𝑘 , Equation (6)
gives
c
𝜒𝑄𝑤,𝐺 𝑏→𝑎 = 0, which violates𝑘-positivity. Moreover, let
𝐺′ ≔𝐺 1 𝑎. Since 𝑁𝑘 𝐺′[𝑏]=𝑉(𝐺 ′) and 𝑁𝑘 𝐺′[𝑎1]=𝑁 𝑘 𝐺′[𝑎],
we have 𝑁𝑘 𝐺′[𝑎]∩𝑁 𝑘 𝐺′[𝑎1]=𝑁 𝑘 𝐺′[𝑎]=𝑁 𝑘 𝐺′[𝑎]∩𝑁 𝑘 𝐺′[𝑏],
so that𝑘-domination, applied in both directions, requires
c
𝜒𝑄𝑤,𝐺′ 𝑎1→𝑎 = c 𝜒𝑄𝑤,𝐺′ 𝑏→𝑎 . However, if 𝑤 is positive, Equation (6)
with𝑐=2gives
c
𝜒𝑄𝑤,𝐺′ 𝑎1→𝑎 = 𝑊[𝑎] 6 >0= c 𝜒𝑄𝑤,𝐺′ 𝑏→𝑎 .
•Properties of𝐷 𝑘◦𝑄𝑤.
a) Dilution:every term of Equation (7) is non-negative and
non-increasing in𝑖, so𝐷𝑘◦𝑄𝑤 satisfies clone-sharing dilu-
tion. If𝑤 is positive and𝑑𝐺(𝑥,𝑣)≤𝑘 , then[𝑥]𝐺⊆𝑁 𝑘 𝐺[𝑥]∩
𝑁𝑘 𝐺[𝑣] , and the term of𝐶=[𝑥] 𝐺, with𝑊[𝑥] > 0, is strictly
decreasing in𝑖. Hence,𝐷 𝑘◦𝑄𝑤satisfies𝑘-strong dilution.
b) Domination:let 𝑦,𝑧∈𝑉(𝐺) such that𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑧]⊆
𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑦], and letΛ :=(𝑁 𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑦])\𝑁 𝑘 𝐺[𝑧]. Since
both intersections are unions of classes, Equation (7) with
𝑖=0yields
c
𝜒𝐷𝑘◦𝑄𝑤,𝐺 𝑦→𝑥 − c 𝜒𝐷𝑘◦𝑄𝑤,𝐺 𝑧→𝑥 = ∑︁
𝐶⊆Λ
𝑊𝐶
𝑛𝐶(𝑛𝐶+1)
≥0,
(8)

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer13
so𝐷𝑘◦𝑄𝑤 satisfies𝑘-domination. Note that𝐷𝑘◦𝑄𝑤 also
satisfies𝑘-strong domination if𝑤 is positive, because the
sum is empty and the difference null exactly when the two
intersections coincide.
□
B Proofs of Clone-Sharing Lemmas
This appendix proves the lemmas of Section 6 relating the clone-
sharing properties to each other and to locality, namely Lemmas 6.10,
6.11 and 6.12, followed by Lemma 6.14 on iterated diffusion. We
also show that locality cannot be strengthened to the addition of
arbitrary neighbors (Lemma B.1).
We start with the relation between clone-sharing dilution and
non-negativity. The forward direction is a telescoping argument;
for the converse, we construct a weighting on a single connected
component of small diameter, so that locality imposes no constraint
inside it.
Lemma 6.10.Clone-sharing dilution (resp. 𝑘-strong dilution) im-
plies clone-sharing non-negativity (resp. 𝑘-positivity). However, the
converse does not hold: there exists a2-clone-robust graph weighting
function that satisfies clone-sharing non-negativity but fails clone-
sharing dilution.
Proof.We show the two directions one after the other.
• (Strong) dilution =⇒ non-negativity (positivity).Let
𝐺 be a graph and 𝑥,𝑦∈𝑉(𝐺) . Set 𝐺 0 𝑥 ≔𝐺 and write
𝑤𝑖 ≔𝑤(𝐺 𝑖 𝑥)(𝑦) and 𝜒𝑖 ≔ c 𝜒𝑤,𝐺𝑖𝑥 𝑦→𝑥 =𝑤 𝑖−𝑤 𝑖+1 for𝑖≥ 0,
where the second equality uses (𝐺𝑖 𝑥)1 𝑥 =𝐺 𝑖+1 𝑥 . Summing
these differences yields𝑤𝑁 =𝑤 0−˝𝑁−1 𝑖=0 𝜒𝑖 for every𝑁≥ 1.
Assume first that 𝑤 satisfies clone-sharing dilution. Then
𝜒𝑖≤𝜒 0 for all𝑖≥ 0, so that1 ≥𝑤 𝑁≥𝑤 0−𝑁𝜒 0≥−𝑁𝜒 0
for every𝑁≥1. Letting𝑁→∞forces𝜒 0≥0.
Assume now that𝑤 satisfies𝑘-strong clone-sharing dilution,
which in particular implies dilution, and that𝑑𝐺(𝑥,𝑦)≤𝑘 .
Since adding clones of𝑥 preserves𝑑𝐺(𝑥,𝑦) , strong dilution
gives 𝜒0 >𝜒 1, while the above argument applied to 𝐺 1 𝑥 in
place of𝐺gives𝜒 1≥0. Hence𝜒 0 >0.
• The converse does not hold.Let C denote the set of con-
nected graphs of diameter at most2. Adding or removing
a clone preserves graph distances between the remaining
vertices, so𝐺∈C if and only if𝐺 1 𝑥∈C , for every𝑥∈𝑉(𝐺) .
For𝐺∈G and𝑣∈𝑉(𝐺) , let𝑐𝑣 ≔|[𝑣] 𝐺| denote the size of
the equivalence class of𝑣, and define
𝑤(𝐺)(𝑣):=
 

1+1/𝑐 2 𝑣
𝑀(𝐺) if𝐺∈C,
𝑤 CU(𝐺)(𝑣)otherwise,
where𝑀(𝐺)≔ ˝ 𝑣∈𝑉(𝐺)  1+ 1 𝑐2𝑣  = ˝ 𝐶∈𝑉(𝐺)/≡ 𝐺  |𝐶|+ 1 |𝐶|  .
a)𝑤 is a2-clone-robust graph weighting function.On C, the
weights are positive and sum to1by definition of 𝑀(𝐺).
Moreover, they only depend on class sizes, which are pre-
served by graph isomorphisms; outsideC,𝑤=𝑤 CU is sym-
metric.
For2-locality, let𝑦≡ 𝐺 𝑥 with𝑦≠𝑥 , and𝑧 with𝑑𝐺(𝑥,𝑧)> 2.
As𝐺 and𝐺\{𝑦} lie on the same side of the case distinction,
either𝐺∈ C and no such 𝑧 exists, or 𝑤(𝐺)(𝑧)=𝑤(𝐺\
{𝑦})(𝑧)by1-locality of𝑤 CU.
b)𝑤 satisfies clone-sharing non-negativity.If 𝐺∉C , this
follows from Example 6.9. If𝐺∈C , adding a clone of𝑥 only
increases𝑐𝑥 by one, so that
𝑀(𝐺 1 𝑥)−𝑀(𝐺)=  𝑐𝑥+1+ 1 𝑐𝑥+1  −  𝑐𝑥+ 1 𝑐𝑥 
=1− 1 𝑐𝑥(𝑐𝑥+1) ≥ 1 2 >0.
Hence, the denominator of𝑤(·)(𝑦) strictly increases, while
its numerator stays the same if𝑦. 𝐺 𝑥 and strictly decreases
if𝑦≡ 𝐺 𝑥. In both cases,
c
𝜒𝑤,𝐺 𝑦→𝑥 >0.
c)𝑤 fails clone-sharing dilution.Let𝐻≔𝑃 3∈C with vertices
𝑎−𝑏−𝑐 . The graphs𝐻,𝐻 1 𝑏 and𝐻 2 𝑏 have class sizes(1, 1, 1),
(1, 2, 1) and(1, 3, 1) respectively, so that𝑀(𝐻)= 6,𝑀(𝐻 1 𝑏)= 13
2 ,𝑀(𝐻 2 𝑏)= 22 3 , and
𝑤(𝐻)(𝑎)= 1 3, 𝑤(𝐻 1 𝑏)(𝑎)= 4 13, 𝑤(𝐻 2 𝑏)(𝑎)= 3 11.
Therefore, we have
c
𝜒𝑤,𝐻 𝑎→𝑏 = 1 3− 4 13 = 1 39 < 5 143 = 4 13− 3 11 = c 𝜒 𝑤,𝐻 1 𝑏 𝑎→𝑏,
which violates clone-sharing dilution.
□
We next show that strong clone-sharing domination forces a
large locality radius. A single path suffices: two vertices far from𝑥
must share nothing with it by locality, while their neighborhoods
intersect that of𝑥differently.
Lemma 6.11. 𝑘-strong clone-sharing domination is not compatible
with𝑗-locality, for any𝑗≤2𝑘−1.
Proof. Since 𝑗-locality implies(2𝑘− 1)-locality for every 𝑗≤
2𝑘− 1, it suffices to treat𝑗= 2𝑘− 1. Suppose for contradiction that
𝑤 satisfies both𝑘-strong clone-sharing domination and(2𝑘− 1)-
locality. Consider the path𝐺≔𝑃 2𝑘+2 with vertices0, 1,..., 2𝑘+ 1,
and let 𝑥≔ 0,𝑢≔ 2𝑘 and𝑣≔ 2𝑘+ 1. On one hand, we have
c
𝜒𝑤,𝐺 𝑢→𝑥 = 0 = c 𝜒𝑤,𝐺 𝑣→𝑥 since𝑑𝐺(𝑥,𝑢)= 2𝑘 and𝑑𝐺(𝑥,𝑣)= 2𝑘+ 1both
exceed2𝑘− 1. On the other hand, 𝑁𝑘 𝐺[𝑥]={ 0,...,𝑘} ,𝑁𝑘 𝐺[𝑢]=
{𝑘,...,2𝑘+1}and𝑁 𝑘 𝐺[𝑣]={𝑘+1,...,2𝑘+1}, so that
𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑣]=∅⊊{𝑘}=𝑁 𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑢].
By𝑘-strong clone-sharing domination, the strict inclusion yields
c
𝜒𝑤,𝐺 𝑢→𝑥 > c 𝜒𝑤,𝐺 𝑣→𝑥 , which contradicts the previous equality.□
The next lemma separates dilution and domination. One direc-
tion follows directly from Theorem 6.13 applied to𝑤 U; for the other,
we construct an explicit2𝑘-clone-robust graph weighting function.
Lemma 6.12.Clone-sharing dilution and clone-sharing domination
do not imply each other. Specifically, 𝑤 CU is𝑘-clone-robust and satis-
fies clone-sharing dilution, but fails 𝑘-clone-sharing domination, for
every𝑘> 0. Conversely, for every𝑘> 0, there exists a2𝑘-clone-robust
graph weighting function that satisfies 𝑘-clone-sharing domination
but fails clone-sharing dilution.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer14
Proof. To see that dilution does not imply domination, apply
Theorem 6.13 to the uniform graph weighting function𝑤 U, which
is positive: 𝑤 CU =𝑄𝑤 U is1-clone-robust, hence 𝑘-clone-robust
for every𝑘> 0, satisfies clone-sharing dilution, and fails𝑘-clone-
sharing domination.
We thus focus on proving that domination does not imply dilu-
tion. Fix𝑘> 0. We call a vertex𝑣∈𝑉(𝐺)𝑘 -centralif 𝑁𝑘 𝐺[𝑣]=𝑉(𝐺) ,
and denote by 𝑍𝑘(𝐺) the set of 𝑘-central vertices of 𝐺 and by
𝑚≔|𝑍 𝑘(𝐺)| its cardinality. LetC𝑘 be the set of connected graphs
of diameter at most2𝑘. Adding or removing a clone preserves all
graph distances between the remaining vertices, and the clone𝑥 1 of
𝑥 satisfies𝑁𝑘[𝑥 1]=𝑁 𝑘[𝑥] . Hence,𝐺∈C 𝑘 if and only if𝐺 1 𝑥∈C𝑘,
and𝑍𝑘(𝐺 1 𝑥)=𝑍 𝑘(𝐺)∪{𝑥 1} if𝑥∈𝑍 𝑘(𝐺) , while𝑍𝑘(𝐺 1 𝑥)=𝑍 𝑘(𝐺)
otherwise.
• Construction.Let𝜂 := 1 2(𝑘+2) and consider the non-increasing
functionℎ(𝛽) :=𝜂1[𝛽≤𝑘+ 2], satisfying𝛽ℎ(𝛽)≤ 1 2 . For
every graph𝐺and𝑣∈𝑉(𝐺), we define
𝑤(𝐺)(𝑣):=
 

1−𝑚ℎ(𝑚)
𝑛 +ℎ(𝑚)1[𝑣∈𝑍 𝑘(𝐺)]if𝐺∈C 𝑘,
𝐷𝑘◦𝑄𝑤 U(𝐺)(𝑣)otherwise,
where𝑛 :=|𝑉(𝐺)| is the number of vertices in𝐺 and𝑚 :=
|𝑍𝑘(𝐺)| its number of 𝑘-central vertices. In words, on C𝑘
every vertex receives the same base weight, and𝑘-central
vertices receive an additional bonus as long as there are at
most𝑘+2of them.
Note that this is a well-defined graph weighting function: on
C𝑘, the weights sum to(1−𝑚ℎ(𝑚))+𝑚ℎ(𝑚)= 1, and they
are positive since 𝑚ℎ(𝑚)≤(𝑘+ 2)𝜂= 1 2 . Outside ofC𝑘,
Theorem 6.13 ensures that𝐷𝑘◦𝑄𝑤 U is a graph weighting
function.
•𝑤 is2𝑘-clone-robust.On C𝑘, the weights only depend on
𝑛,𝑚 and on whether𝑣 is𝑘-central, all of which are invariant
under graph isomorphisms; outsideC𝑘, the weighting func-
tion coincides with the symmetric function𝐷𝑘◦𝑄𝑤 U. Hence
𝑤 is symmetric. For2𝑘-locality, let𝑦≡ 𝐺 𝑥 with𝑦≠𝑥 , and𝑧
with𝑑𝐺(𝑥,𝑧)> 2𝑘. Since𝐺 and𝐺\{𝑦} lie on the same side
of the case distinction, either𝐺∈C 𝑘 and no such𝑧 exists,
or𝑤(𝐺)(𝑧)=𝑤(𝐺\{𝑦})(𝑧) follows from the2𝑘-locality of
𝐷𝑘◦𝑄𝑤 U (Theorem 6.13).
•𝑤 satisfies𝑘-clone-sharing domination.Let 𝐺∈G , and
let𝑥,𝑦,𝑧∈𝑉(𝐺) such that𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑧]⊆𝑁 𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑦].
If𝐺∉C 𝑘, then
c
𝜒𝑤,𝐺 𝑦→𝑥≥ c 𝜒𝑤,𝐺 𝑧→𝑥 follows from Theorem 6.13,
so assume 𝐺∈ C𝑘. The graph 𝐺 1 𝑥 has𝑛+ 1vertices and
𝑚′𝑘-central vertices, where𝑚′ =𝑚+ 1if 𝑥∈𝑍 𝑘(𝐺) and
𝑚′ =𝑚 otherwise, and𝑍𝑘(𝐺 1 𝑥)∩𝑉(𝐺)=𝑍 𝑘(𝐺) . Hence, for
every𝑣∈𝑉(𝐺),
c
𝜒𝑤,𝐺 𝑣→𝑥 = 1−𝑚ℎ(𝑚) 𝑛 − 1−𝑚 ′ℎ(𝑚′) 𝑛+1 ,
+1[𝑣∈𝑍 𝑘(𝐺)] ℎ(𝑚)−ℎ(𝑚 ′),
where the first term is independent of𝑣 andℎ(𝑚)−ℎ(𝑚′)≥ 0
sinceℎ is non-increasing. Therefore, subtracting the expres-
sions for𝑣=𝑦and𝑣=𝑧, the first term cancels and
c
𝜒𝑤,𝐺 𝑦→𝑥− c 𝜒𝑤,𝐺 𝑧→𝑥 = 1[𝑦∈𝑍 𝑘(𝐺)]−1[𝑧∈𝑍 𝑘(𝐺)] 
× ℎ(𝑚)−ℎ(𝑚 ′).
If 𝑥∉𝑍 𝑘(𝐺) , then 𝑚′ =𝑚 and the difference vanishes.
Otherwise, 𝑥∈𝑍 𝑘(𝐺) gives 𝑁𝑘 𝐺[𝑥]=𝑉(𝐺) , so that the
hypothesis reads𝑁𝑘 𝐺[𝑧]⊆𝑁 𝑘 𝐺[𝑦]. If𝑧∈𝑍 𝑘(𝐺) , then𝑉(𝐺)=
𝑁𝑘 𝐺[𝑧]⊆𝑁 𝑘 𝐺[𝑦], so𝑦∈𝑍 𝑘(𝐺) and the difference vanishes.
If𝑧∉𝑍 𝑘(𝐺) , then the first factor is non-negative, and so is
the difference. In all cases,
c
𝜒𝑤,𝐺 𝑦→𝑥≥ c 𝜒𝑤,𝐺 𝑧→𝑥 .
•𝑤 fails clone-sharing dilution.Let 𝐺=𝑃 𝑘+2∈C 𝑘 with
vertices0,...,𝑘+ 1, and let 𝑥= 1. Vertices1,...,𝑘 are𝑘-
central, so that𝐺𝑖 𝑥 has𝑛=𝑘+ 2+𝑖 vertices and𝑚=𝑘+𝑖
𝑘-central vertices, including𝑥. Using1−(𝑘+ 1)𝜂= 𝑘+3 2(𝑘+2)
and1−(𝑘+2)𝜂= 1 2 , we get
𝑤(𝐺 1 𝑥)(𝑥)= 1 2(𝑘+2) +𝜂= 1 𝑘+2 ,
𝑤(𝐺 2 𝑥)(𝑥)= 1 2(𝑘+4) + 1 2(𝑘+2) ,
𝑤(𝐺 3 𝑥)(𝑥)= 1 𝑘+5 ,
and therefore
c
𝜒𝑤,𝐺2𝑥 𝑥→𝑥 − c 𝜒𝑤,𝐺1𝑥 𝑥→𝑥 =  𝑘+3 (𝑘+2)(𝑘+4) − 1 𝑘+5  − 1 (𝑘+2)(𝑘+4) ,
= 1 (𝑘+4)(𝑘+5) >0,
which violates clone-sharing dilution.
□
We next show that 1-locality cannot be meaningfully strength-
ened: requiring for example that the addition of neighbors—rather
than only equivalent nodes—leaves the weights of distant vertices
unchanged contradicts symmetry.
Lemma B.1.No graph weighting function 𝑤 can simultaneously
satisfysymmetry, and the followingstrong localityproperty: for
every graph𝐺∈G and vertices𝑥,𝑦,𝑧∈𝑉(𝐺) with𝑦∈𝑁 𝐺[𝑥] and
𝑧∉𝑁 𝐺[𝑥], we have𝑤(𝐺)(𝑧)=𝑤(𝐺\{𝑦})(𝑧).
Proof. Consider the graph𝐺 consisting of a central vertex 𝑑
connected to three disjoint paths of length three. Explicitly, for each
𝑖= 1, 2, 3, consider the path𝑃𝑖 :𝑎𝑖−𝑏𝑖−𝑐𝑖 and connect its endpoint
𝑐𝑖 to the central vertex𝑑.
Now consider the subgraph𝐺\(𝑃 2∪𝑃 3). By symmetry, vertices
𝑎1 and𝑑 must receive the same non-negative weight, say𝑤1, and
vertices𝑏1 and𝑐1 must receive the same weight, say𝑤2. We more-
over have2(𝑤1+𝑤 2)= 1since 𝑤(𝐺\(𝑃 2∪𝑃 3)) is a probability
distribution.
We now add back vertex𝑐2: by strong locality, the weight of ver-
tices𝑎1 and𝑏1 must remain unchanged, i.e.,𝑤(𝐺\(𝑃 3∪{𝑎2,𝑏 2}))(𝑎 1)=
𝑤1 and𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑏 1)=𝑤 2. By symmetry, we moreover
know that𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑐 2)=𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑎 1)
and𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑑)=𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑏 1), an we
conclude that𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))(𝑐 1)= 1− 2(𝑤1+𝑤 2)= 0since
𝑤(𝐺\(𝑃 3∪{𝑎 2,𝑏 2}))is a probability distribution.
We now iteratively add back𝑏2 and𝑎2; the same reasoning holds
and we get 𝑤(𝐺\𝑃 3)(𝑐 1)=𝑤(𝐺\𝑃 3)(𝑑)=𝑤(𝐺\𝑃 3)(𝑐 2)= 0,
𝑤(𝐺\𝑃 3)(𝑎 1)=𝑤(𝐺\𝑃 3)(𝑎 2)=𝑤 1 and𝑤(𝐺\𝑃 3)(𝑏 1)=𝑤(𝐺\
𝑃3)(𝑏 2)=𝑤 2.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer15
Finally, we iteratively add back vertices 𝑐3,𝑏3 and𝑎3. Impor-
tantly, the weights of𝑎1,𝑎 2,𝑏 1,𝑏 2 cannot change under strong lo-
cality, and we conclude that all the newly introduced vertices must
receive weight zero. We finally conclude using symmetry that𝑤1 =
𝑤(𝐺)(𝑎 1)=𝑤(𝐺)(𝑎 3)= 0and 𝑤2 =𝑤(𝐺)(𝑏 1)=𝑤(𝐺)(𝑏 3)= 0:
this is a contradiction.
□
Finally, we prove Lemma 6.14, which justifies the use of 𝐷𝑘
rather than iterated one-hop diffusion in Theorem 6.13. We take
𝑤=𝑤 U, so that𝑄𝑤=𝑤 CU, and exhibit explicit graphs on which
each property fails.
Lemma 6.14.There exists a symmetric graph weighting function
𝑤 such that, for every ℓ≥ 2and 𝑘≥ 1, the graph weighting function
𝐷ℓ◦𝑄𝑤 satisfies neither clone-sharing dilution nor 𝑘-clone-sharing
domination.
Proof. We consider the uniform graph weighting function𝑤 U,
denote ˆ𝑤:=𝐷 ℓ◦𝑄𝑤 U, and note that𝑄𝑤 U =𝑤 CU.
• Reduction.It suffices to exhibit a graph 𝐺 and a vertex
𝑥 with
c
𝜒 ˆ𝑤,𝐺 𝑥→𝑥 < 0. Indeed, this violates clone-sharing non-
negativity, hence dilution by Lemma 6.10. Moreover, since
𝑁𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑧]⊆𝑁 𝑘 𝐺[𝑥]=𝑁 𝑘 𝐺[𝑥]∩𝑁 𝑘 𝐺[𝑥] for every𝑧∈
𝑉(𝐺) ,𝑘-domination would imply
c
𝜒 ˆ𝑤,𝐺 𝑥→𝑥 ≥ c 𝜒 ˆ𝑤,𝐺 𝑧→𝑥 for all 𝑧,
and summing over𝑧∈𝑉(𝐺)would give
|𝑉(𝐺)|·
c
𝜒 ˆ𝑤,𝐺 𝑥→𝑥 ≥ ∑︁
𝑧∈𝑉(𝐺)
c
𝜒 ˆ𝑤,𝐺 𝑧→𝑥 =1− 1− ˆ𝑤(𝐺 1 𝑥)(𝑥 1)≥0.
• Construction.For 𝑡≥ 1, let 𝐺 be the tree in which 𝑥 is
adjacent to 𝑏1 and𝑏2, and each 𝑏𝑗 is adjacent to 𝑡 leaves
𝑐𝑗,1,...,𝑐 𝑗,𝑡 :
𝑥
𝑏1 𝑏2
𝑐1,1 𝑐1,𝑡 𝑐2,1 𝑐2,𝑡... ...
All equivalence classes of𝐺 are singletons, so for every𝑖≥ 0,
𝐺𝑖 𝑥 has𝑁≔ 3+2𝑡 classes:𝑋≔{𝑥,𝑥 1,...,𝑥 𝑖} and singletons.
Hence𝑄𝑤 U(𝐺𝑖 𝑥) assigns 1 𝑁(𝑖+1) to each vertex of𝑋 and 1 𝑁
to every other vertex. Let𝐵 :={𝑏 1,𝑏 2} and𝐶 :={𝑐 𝑗,𝑚 : 𝑗∈
{1,2},𝑚∈{1,...,𝑡}}. By symmetry, the lazy random walk
on𝐺𝑖 𝑥 projected onto the types 𝑋,𝐵,𝐶 is a Markov chain
with transition matrix
𝑇≔
'››
«
𝜃𝑖 1−𝜃 𝑖 0
𝑖+1
𝑖+𝑡+2
1
𝑖+𝑡+2
𝑡
𝑖+𝑡+2
0 1 2 1 2
“ﬁﬁ
‹
, 𝜃 𝑖 ≔ 𝑖+1 𝑖+3 ,
with rows and columns ordered as𝑋,𝐵,𝐶 , and anℓ-step walk
ending in𝑋ends at𝑥with probability 1 𝑖+1 . Therefore,
ˆ𝑤(𝐺𝑖 𝑥)(𝑥)= 1 𝑁(𝑖+1)  (𝑇ℓ)𝑋𝑋+2(𝑇 ℓ)𝐵𝑋+2𝑡(𝑇 ℓ)𝐶𝑋  .(9)
• Asymptotics.Fix 𝑖 and let 𝑡→ ∞. In the limit, a walk
starting from{𝐵,𝐶} never enters𝑋 , and its transition matrix
𝑅(the restriction of𝑇to{𝐵,𝐶}) converges to
𝑅∞ ≔
0 1
1
2
1
2

.
We let𝜌𝑚 ≔(𝑅 𝑚 ∞)𝐶𝐵 ≥ 0denote the probability that this
limiting walk, started in 𝐶, is in 𝐵 after𝑚 steps. Since 𝑋
can only be entered from 𝐵, decomposing walks from 𝐶
according to their first entrance into𝑋gives
(𝑇ℓ)𝐶𝑋 =
ℓ−1∑︁
𝑚=0
(𝑅𝑚)𝐶𝐵𝑇𝐵𝑋(𝑇ℓ−1−𝑚)𝑋𝑋.
Using(𝑅𝑚)𝐶𝐵−−−−→ 𝑡→∞ 𝜌𝑚, with𝑡·𝑇 𝐵𝑋 = 𝑡(𝑖+1) 𝑖+𝑡+2 −−−−→ 𝑡→∞ 𝑖+ 1,
and(𝑇 𝑛)𝑋𝑋−−−−→ 𝑡→∞ 𝜃𝑛 𝑖 for every𝑛, we get
(𝑇ℓ)𝑋𝑋→𝜃 ℓ 𝑖,(𝑇 ℓ)𝐵𝑋→0,
𝑡(𝑇 ℓ)𝐶𝑋→(𝑖+1)
ℓ−1∑︁
𝑚=0
𝜌𝑚𝜃ℓ−1−𝑚 𝑖 .
Multiplying Equation (9) by2𝑡 and using2 𝑡/𝑁→ 1, we
conclude that
𝐿(𝑖):=lim
𝑡→∞
2𝑡· ˆ𝑤(𝐺𝑖 𝑥)(𝑥)
= 1 𝑖+1  𝜃ℓ 𝑖+2(𝑖+1) ℓ−1∑︁ 𝑚=0 𝜌𝑚𝜃ℓ−1−𝑚 𝑖 
= 𝜃ℓ 𝑖
𝑖+1 +2
ℓ−1∑︁
𝑚=0
𝜌𝑚𝜃ℓ−1−𝑚 𝑖 .
• Conclusion.Since lim𝑡→∞ 2𝑡·
c
𝜒 ˆ𝑤,𝐺 𝑥→𝑥 =𝐿( 0)−𝐿( 1), it suffices
to show that𝐿( 0)<𝐿( 1): then
c
𝜒 ˆ𝑤,𝐺 𝑥→𝑥 < 0for 𝑡 large enough,
and the reduction step concludes the proof.
We compare the two first terms of 𝐿(𝑖) , using𝜃0 = 1 3 and
𝜃1 = 1 2 . For the first term,𝜃ℓ 0 = 1 3ℓ < 1 2ℓ+1 = 𝜃ℓ 1 2 , as(3/2)ℓ >
2for ℓ≥ 2. For the second term, the sum is a polynomial in𝜃𝑖
with non-negative coefficients𝜌𝑚, hence it is non-decreasing
in𝜃𝑖, and𝜃 0 <𝜃 1.
□
C Sharing coefficient for the family𝑓 𝜈
All the above constructions extend naturally to the second family
of weighting functions introduced in [Berriaud and Wattenhofer,
2025]. Given a probability density𝜈 supported on[0,𝛼] , this family
is defined by
𝑓𝜈(𝑆)(𝑥)=
∫ 𝛼
0
𝜈(𝑟)𝑔 𝑟(𝑆)(𝑥)𝑑𝑟.
We extend the sharing coefficient of𝑔𝑟 to𝑓𝜈 by similarly integrating
𝜒𝑔𝑟 over all radii.
Definition C.1 (Sharing coefficient of 𝑓𝜈 ).Let 𝑆⊆R 𝑛 be
finite, and let𝑥,𝑦∈𝑆. The sharing coefficient of𝑓 𝜈 is defined by
𝜒𝑓𝜈,𝑆 𝑦→𝑥 ≔
∫ 𝛼
0
𝜈(𝑟)𝜒 𝑔𝑟,𝑆 𝑦→𝑥𝑑𝑟,
which, for𝑦=𝑥, defines the private weight𝜒 𝑓𝜈,𝑆 𝑥→𝑥 of𝑥.

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer16
Both quantities are well defined, since0 ≤𝜒 𝑔𝑟,𝑆 𝑦→𝑥≤𝑔𝑟(𝑆)(𝑥)≤
1for every 𝑟, so that the integrand is bounded. Moreover, most
qualitative properties of𝜒 𝑔𝑟 directly carry over to𝜒 𝑓𝜈 :
• Non-negativity and locality. 𝜒𝑓𝜈,𝑆 𝑦→𝑥≥ 0, with equality if and
only if𝑑(𝑥,𝑦)≥ 2𝛼, which is the locality parameter of 𝑓𝜈.
Indeed, 𝜒𝑔𝑟,𝑆 𝑦→𝑥 vanishes exactly for 𝑟≤𝑑(𝑥,𝑦)/ 2, and 𝜈 is
supported on[0,𝛼].
• Decomposition.Integrating the definition of the private weight
of𝑔𝑟 ,𝑓𝜈(𝑆)(𝑥) decomposes into private and shared parts, i.e.,
𝑓𝜈(𝑆)(𝑥)=𝜒 𝑓𝜈,𝑆 𝑥→𝑥+ ∑︁
𝑦≠𝑥
𝜒𝑓𝜈,𝑆 𝑦→𝑥.
•Domination.If𝑦intersection-dominates𝑧with respect to𝑥
for every𝑟∈[ 0,𝛼] , then Property 5.2 holds for every radius,
and integrating yields𝜒 𝑓𝜈,𝑆 𝑦→𝑥≥𝜒 𝑓𝜈,𝑆 𝑧→𝑥 .
• Dilution.Similarly, integrating Property 5.3 over 𝑟 shows
that𝜒𝑓𝜈,𝑆𝑖 𝑦→𝑥 is non-increasing as perfect clones of𝑥 are added.
The only property that does not directly extend to𝑓𝜈 is the sim-
ple multiplicative form of the element-removal effect. Integrating
Equation (1) with respect to𝜈gives
𝑓𝜈(𝑆\{𝑥})(𝑦)=
∫ 𝛼
0
𝜈(𝑟)
𝑔𝑟(𝑆)(𝑦)+𝜒 𝑔𝑟,𝑆 𝑦→𝑥
1−𝜒 𝑔𝑟,𝑆 𝑥→𝑥 𝑑𝑟≥𝑓 𝜈(𝑆)(𝑦)+𝜒 𝑓𝜈,𝑆 𝑦→𝑥,
where the inequality uses1 −𝜒 𝑔𝑟,𝑆 𝑥→𝑥 ∈( 0, 1]. Thus, removing an
element𝑥 still induces alocal additive increaseof at least 𝜒𝑓𝜈,𝑆 𝑦→𝑥 in
the weight of each remaining element𝑦, and in particular never de-
creases it. However, since the rescaling factor(1−𝜒𝑔𝑟,𝑆 𝑥→𝑥)−1 depends
on𝑟, the global rescaling is in general no longer purely multiplica-
tive, i.e.,𝑓𝜈(𝑆\{𝑥})(𝑦) differs from 𝑓𝜈(𝑆)(𝑦)+𝜒 𝑓𝜈,𝑆 𝑦→𝑥  1−𝜒 𝑓𝜈,𝑆 𝑥→𝑥 −1
unless𝜒 𝑔𝑟,𝑆 𝑥→𝑥 is constant across radii.
D Feasibility of the Edge-Sharing Constraints
We complement Theorem 6.4 by testing computationally whether
its weaker variant, which replaces endpoint expansion by non-
negative endpoint sharing,
e
𝜒𝑤,𝐺 𝑢→𝑒≥ 0for 𝑢∈𝑒 , is compatible with
clone-robustness: each endpoint may then scale by its own factor,
which need only be at least the global factor𝜂𝐺,𝑒 . That is, we look
for a1-clone-robust graph weighting function𝑤 such that, for every
graph𝐺and edge𝑒∈𝐸(𝐺), there exists𝜂 𝐺,𝑒∈(0,1]with
𝑤(𝐺−𝑒)(𝑧)≥𝜂 𝐺,𝑒𝑤(𝐺)(𝑧)for𝑧∈𝑒,
𝑤(𝐺−𝑒)(𝑧)≤𝜂 𝐺,𝑒𝑤(𝐺)(𝑧)for𝑧∉𝑒,
with equality whenever𝑑𝐺(𝑒,𝑧)>1.
Formulation.Restricting to all graphs on at most 𝑛 vertices, we
introduce one variable𝑤𝐺,𝑣 ∈[ 0, 1] for each graph𝐺, up to iso-
morphism (using a canonical labelling), and each vertex𝑣∈𝑉(𝐺) ,
and one variable𝜆𝐺,𝑒 ≔ 1/𝜂𝐺,𝑒≥ 1for each edge 𝑒∈𝐸(𝐺) . The
constraints are: (i) normalization, ˝ 𝑣∈𝑉(𝐺) 𝑤𝐺,𝑣 = 1for every 𝐺;
(ii) symmetry,𝑤𝐺,𝑢 =𝑤𝐺,𝜎(𝑢) for every automorphism𝜎 of𝐺 and
𝑢∈𝑉(𝐺) ; (iii)1-locality, 𝑤𝐺′,𝑧 =𝑤 𝐺,𝑧 whenever𝐺′ is obtained
from𝐺 by adding a clone of a vertex 𝑥 and𝑧∉𝑁 𝐺[𝑥] ; (iv) the
edge-sharing constraints above, rewritten as𝜆𝐺,𝑒𝑤𝐺−𝑒,𝑧−𝑤𝐺,𝑧≥ 0
for𝑧∈𝑒 ,≤ 0for 𝑧∉𝑒 , and = 0whenever 𝑑𝐺(𝑒,𝑧)> 1. The
constraints in (iv) are bilinear in(𝜆,𝑤) , so the resulting problem
is a non-convex quadratically constrained feasibility program. As
a sanity check of the encoding, additionally requiring a common
expansion factor𝜇𝐺,𝑒≥ 1for both endpoints, as in Theorem 6.4,
makes the program infeasible already for𝑛=5.
Implementation.A first encoding using the SMT solverZ3, through
Python and then Rust, did not terminate within a day for𝑛= 5. We
therefore switched to the numerical solverGurobi, which handles
non-convex quadratic constraints by spatial branch-and-bound and
thus provides global feasibility and infeasibility guarantees, up to
numerical tolerances. A Rust program enumerates all graphs up
to isomorphism and writes the program in LP file format, which is
then passed to the solver.
Results.Gurobi finds a feasible assignment for all208graphs
on at most𝑛= 6vertices, but reports the program infeasible for
𝑛= 7(1,252graphs, about21 ,000variables and85 ,000bilinear con-
straints), both with default settings (after12minutes) and with its
most conservative numerical settings (after2.7hours on a personal
computer). In contrast, dropping the equality for vertices far from𝑒
yields a program that is feasible for all graphs on at most7vertices,
so this locality requirement drives the contradiction. This strongly
suggests that Theorem 6.4 still holds under non-negative endpoint
sharing, although extracting a human-checkable proof is left for
future work. The code is available here.
E Graph Weigthing Functions based on
Maximal Clique Covers
One approach to constructing neighborhood-based graph weight-
ing functions relies on the following observation: the set of maximal
cliques of a graph, denoted byK(𝐺) , is invariant under the removal
of equivalent nodes. Indeed, for any finite graph𝐺 and two equiva-
lent vertices𝑥≡ 𝐺 𝑦, we have, i.e.,
K(𝐺\{𝑥})={𝐾\{𝑥}|𝐾∈K(𝐺)}.
Moreover,K(𝐺) forms a cover of the vertex set 𝑉(𝐺) , that is,—
𝐾∈K(𝐺) 𝐾=𝑉(𝐺) . We refer to such a cover of 𝑉(𝐺) by max-
imal cliques as amaximal-clique-cover (MCC).
Starting from an MCC–sayK(𝐺) –one can construct a clone-
robust weighting function by assigning weight uniformly to each
maximal clique and then distributing each clique’s weight among
its constituent nodes. A key design question is how to handle ver-
tices that belong to multiple maximal cliques. The most straightfor-
ward approach is to divide each clique’s weight uniformly among
its vertices and compute each node’s total weight as the sum of
its contributions across cliques. Formally, we define theadditive
maximal-clique weighting rule𝑤 MCCA as follows, i.e.,
𝑤 MCCA(𝐺)(𝑣)= 1 |K(𝐺)| ∑︁ 𝐾∈K(𝐺):𝑣∈𝐾 1 |𝐾|, 𝑣∈𝑉(𝐺).
Alternatively, one can introduce a notion of varying participa-
tion: each node contributes equally to all cliques it belongs to, and
the total weight within each clique is then shared proportionally to
the participation of a node within that clique. The resulting node
weights are obtained by summing each node’s contributions across
all cliques. Formally, we define for each vertex𝑣∈𝑉(𝐺) the number
of maximal cliques it belongs to as𝑐𝑣 :=|{𝐾∈K(𝐺)|𝑣∈𝐾}|. We
then interpret1/𝑐𝑣 as the fraction of participation of𝑣 in each clique
it belongs to, and compute the total participation within a clique

Damien Berriaud, Supanat Wangsutthitham, and Roger Wattenhofer17
𝐾 as𝑃𝐾 := ˝ 𝑣∈𝐾 1 𝑐𝑣. Then each maximal clique gets total mass
1/|K(𝐺)| and redistributes it proportionally to the participation of
its nodes, leading to
𝑤 MCCP(𝐺)(𝑣)= 1 |K(𝐺)| ∑︁ 𝐾∈K(𝐺):𝑣∈𝐾 1 𝑐𝑣·𝑃𝐾 , 𝑣∈𝑉(𝐺).
Note that both 𝑤 MCCA and𝑤 MCCP are clearly 1-clone-robust
graph weighting functions: they verify symmetry becauseK(𝐺) is
invariant under graph isomorphism, and locality since the removal
of a clone only affects the weights of nodes within the same cliques,
i.e., its neighbors.
