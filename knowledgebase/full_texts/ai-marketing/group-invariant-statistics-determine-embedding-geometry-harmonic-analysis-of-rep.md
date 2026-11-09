---
title: 'Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations
  from Bach to the Night Sky'
url: https://arxiv.org/abs/2610.00647
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Liam Storan
- Andreas Tolias
- Nina Miolane
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.00647
pages: 31
chars: 103543
fetched_at: '2026-11-08T13:25:46+00:00'
kb_version: 1
---

# Group-Invariant Statistics Determine Embedding Geometry: Harmonic Analysis of Representations from Bach to the Night Sky

Preprint. Under review.
GROUP-INVARIANTSTATISTICSDETERMINEEMBED-
DINGGEOMETRY:
HARMONICANALYSIS OFREPRESENTATIONS FROM
BACH TO THENIGHTSKY
Liam Storan∗
Stanford University
Andreas Tolias
Stanford University
Nina Miolane
University of California, Santa Barbara
ABSTRACT
The representations that language models learn for concepts such as months,
weekdays, and places display consistent geometric structure: circles and saddle-
shaped “Pringle” manifolds. Recent work traced these structures totranslation
symmetryin word co-occurrence statistics, deriving the observed Fourier geome-
try when co-occurrence depends only on distance on an abelian lattice of concepts.
We demonstrate that more general notions of symmetry lead to equally structured
predictions. Considering symmetries defined by arbitrary finite groups, com-
pact groups, and homogeneous spaces, we prove that whenever the co-occurrence
statistics of a word family are invariant under a groupG, the learned word embed-
dings consist of matrix elements of the irreducible representations (irreps) ofG.
Circles and Pringles arise whenGis cyclic, in which case the irreps are Fourier
modes. We verify the irrep structure in three experimental settings. (i) The cyclic
groupZ 12: for the months of the year we recover the known circular geometry.
(ii) A dihedral group acting on the major and minor triads: we unify two classical
observations—that transposition and chord inversion form a group (T /I) acting
on chords (music theory), whichimpliesthat the well-known “circle of fifths”
emerges in learned chord embeddings (machine learning). (iii) We explain and re-
produce a recently discovered spherical representation of celestial objects in large
language models (LLMs) as a spherical-harmonic embedding derived from our
theory. Our results demonstrate that the geometry of learned representations is
often a consequence of the statistical symmetry of underlying data.
1 INTRODUCTION
Large language models (LLMs) organize concepts geometrically in their activations. Months of the
year lie on circles (Engels et al., 2025), latitude and longitude of cities can be linearly decoded from
LLM activations (Gurnee & Tegmark, 2024), and celestial objects reside on a sphere inside a LLM’s
residual stream (Berdnikov & Liokumovich, 2026). A compelling explanation for the ubiquitous
circular geometry was given by Karkada et al. (2026): when the co-occurrence of words in text
is only a function of their distance on some “cyclic latent lattice”, the optimal embedding under
a quadratic word-embedding model (Karkada et al., 2025) consists of Fourier modes which in turn
generates circles. For example, they found that the measured co-occurrence of January and February
is about the same as November and December in general text, which explains why language models
embed the 12 months on a circle.
Contributions.Cyclic symmetry is just one example of structure that can exist in data (Figure 1).
Here, we ask and answer the general question:what does an arbitrary symmetry of co-occurrence
statistics imply for embedding geometry?The answer is a complete picture of the components used
to construct word embedding geometry, assembled from group harmonic analysis. Specifically, our
contributions are:
∗Correspondence: lstoran@stanford.edu
1
arXiv:2610.00647v1  [cs.LG]  30 Sep 2026

Preprint. Under review.
jan
feb
mar
apr
may
jun
jul
aug
sep
oct
nov
dec
cyclic ℤ12: months →
circle
dihedral D12: triads →
dodecagonal prism
C
c
G
g
D
d
A
a
E
e
B
b
F♯
f♯
C♯
c♯
G♯
g♯
D♯
d♯
A♯
a♯
F
f
Polaris
Vega
Sirius
Betelgeuse
Antares
Acrux Fomalhaut
spherical SO(3)/SO(2): sky objects →
sphere
Figure 1:Months, musical chords, and celestial objects exhibit distinct latent geometries, dic-
tated by the symmetry of their word co-occurrence statistics in text corpora.Left: month statistics
are approximately invariant under cyclic shift (Z12), which places them on a circle.Middle: musical
chord statistics are approximately invariant under transposition and inversion (D 12), which places
them on a dodecagonal prism.Right: celestial object statistics are approximately invariant under 3D
rotations (SO(3)), which places them on a sphere.
•A general theory of word embedding geometry under group symmetry: if the words form
a torsor for a groupG(i.e., if we can form a bijection between the words and group elements,
Theorem 4.1) or a homogeneous spaceG/K(Theorem 4.2), the embedding’s entries are matrix
elements of the irreps ofGthat can be expressed analytically.
•A non-Abelian validation of the theorythat unifies existing, but disconnected, observations
from music theory: we use our theory to reconcile two classical observations about music: the
existence of transposition symmetry (T /I) in music theory (Crans et al., 2009), and the so-called
circle of fifths that emerges in learned chord embeddings (Lahnala et al., 2021). Specifically, we
show that Bach’s chorales have approximatelyT /I-invariant chord statistics (invariance captures
R2 = 0.822of the co-occurrence structure), and that this statistical symmetryforcesthe observed
geometry. The empirical circle of fifths matches our theoretical predictions at a per-chord cosine
of0.98. We observe the same structure in ChordBERT, a masked language model for symbolic
chord sequences.
•A continuous validation of the theorythat challenges existing results on LLM activations: We
reanalyze the sky-sphere LLM activations of Berdnikov & Liokumovich (2026) and show that
the representation of celestial objects is not a sphere, as the authors initially reported, but is actu-
allyspherical-harmonics. Specifically the eigenmodes of the LLM activations are degree-ordered
spherical-harmonic blocks (ℓ=1,ℓ=2,ℓ=3), in five of the seven models examined. We reproduce
these harmonic results using four public-domain astronomy books (131k tokens, selected by a
“star guide” criterion) and examining classical word embeddings. We show that co-occurrence
statistics place the objects on the true celestial sphere at a statistically significant per-object co-
sine0.55(median0.68), which is within the range of accuracy that an idealized spherical model
predicts for a sample of this size. The same symmetry fingerprint, present in a131k-token field
guide and in a123B-parameter LLM’s activations, sharpens in the model, as expected if training
supplies vastly more such text.
Together, these results show that word embeddings admit analytical expressions determined by the
symmetry of their co-occurrence statistics in quadratic embedding models, and suggest that LLM
activations might be described by the same rule.
2 RELATED WORK
We review work linking word statistics to their embeddings, focusing on symmetry-driven statistics,
and survey the role of group theory in interpretability research.
From word statistics to their embeddings.Early work has linked the structure of word embed-
dings to their co-occurrence statistics, but did not connect that structure to any symmetry of these
2

Preprint. Under review.
statistics. Skip-gram with negative sampling implicitly factorizes a shifted Pointwise Mutual Infor-
mation (PMI) matrix (Levy & Goldberg, 2014). GloVe (Global Vectors for Word Representation)
fits log co-occurrence directly (Pennington et al., 2014). Karkada et al. (2025) derive a quadratic
word-embedding model in which trained embeddings realize a low-rank factorization of the normal-
ized statisticsM ⋆ (Eq. 1), the premise we adopt (Assumption A.1).
Word statistics described by a symmetric group and their embeddings.Karkada et al. (2026)
prove that translation-invariant statistics onZ D L yield sinusoidal embeddings and validate this for
periodic concepts; our Appendix B.6 recovers their Proposition 1 as the cyclic case. Engels et al.
(2025) found the day/month circles empirically. Gurnee & Tegmark (2024) linearly decoded mea-
surements of space and time from activations. Berdnikov & Liokumovich (2026) discovered the sky
sphere, asking explicitly whether the statistics-based paradigm explains it, which our Section 7 ad-
dresses. The linear representation hypothesis and the geometry of categorical concepts (Park et al.,
2024; 2025) concern complementary, non-manifold structure.
Group theory in interpretability.Beyond word embeddings, group theory has been successfully
used to describe representations emerging across neural network architectures. Networks trained on
group operations learn irrep-based algorithms: Fourier features for modular addition (Nanda et al.,
2023) and general irreducible representations for finite groups (Chughtai et al., 2023; Marchetti
et al., 2026). Those results concern models trainedon a group operation. By contrast, our work
concerns models trained onnatural corpora whose statistics happen to be group-invariant, with the
group acting on concepts rather than being the task.
3 BACKGROUND ONGROUPTHEORY
We briefly review the concepts from group theory that our results are built from. We refer to Diaconis
(1988); Folland (2016) for details.
Groups.Agroupis a setGequipped with an associative binary operation(g, h)7→gh, an identity
element1∈Gwith1g=g1 =g, and an inverseg −1 ∈Gfor eachg∈Gwithg −1g=gg −1 = 1.
A group isAbelianifgh=hgfor allg, h∈G, and non-Abelian otherwise. The cyclic groupZ n
(integers modulonunder addition) is Abelian. The dihedral groupD n of rotations and reflections
of a regularn-gon is not, since rotating and reflecting do not generally commute.Z n andD n are
finite, but groups can also be continuous, i.e., the groupSO(3)of all possible 3D rotations. We will
useZ 12,D 12 andSO(3)to characterize the word embeddings of the months of the year, musical
chords, and celestial objects, respectively (Figure 1).
Group actions.A (left)actionofGon a setLis a map(g, x)7→g·xwith1·x=xand
g·(h·x) = (gh)·x∀g∈G,∀x∈L. In our theory,Lis a set of words: for example, the months
of the year, on which the cyclic groupG=C 12 acts. The action istransitiveif everyx∈Lcan be
moved to everyy∈Lby someg∈G. The action isfreeifg·x=ximpliesg= 1, i.e, only the
identity can fix ax∈L. When the action is both free and transitive,Lis aG-torsor: choosing any
base pointx 0 ∈Lyields a bijectionG→L,g7→g·x 0. For example, the action ofG=C 12 on
the months is free and transitive, such that the months themselves can be thought of as elements of
C12 after choosing a base point (Figure 1 left). When the action is transitive but not free, each point
xhas a nontrivialstabilizerK={g∈G:g·x=x}, andLis identified with thehomogeneous
spaceG/Kof left cosetsgK. The sphereL=S 2 =SO(3)/SO(2)of the celestial objects is our
example of a homogeneous space (Figure 1 right):SO(3)acts transitively onS 2, the stabilizer of a
point is the groupSO(2)of rotations about the axis through the point.
Irreducible representations.Our theory shows that word embeddings can be computed analyti-
cally using irreducible representations of group, which we define now. Aunitary representationof
Gof dimensiond ρ is a mapρ:G→U(d ρ)into the unitary group such thatρ(gh) =ρ(g)ρ(h)
for allg, h∈G. It isirreducible(anirrep) if no proper nonzero subspace ofC dρ is mapped to
itself by everyρ(g). Any unitary representation decomposes into a direct sum of irreps. A finite
group has finitely many irreps up to unitary equivalence. All irreps of Abelian groups (e.g.,C 12)
are one-dimensional: theirρ(g)are complex scalars for any irrepρand group elementg. Higher
dimensional irreps may exist for non-Abelian groups (e.g.,D 12 andSO(3)): theirρ(g)are gener-
ally complex matrices of sized ρ ×d ρ. Our theory will often refer to the entries of those matrices.
3

Preprint. Under review.
Lastly, irreps are used to define thegroup Fourier transformof any functionfover a finite groupG
as ˆf(ρ) = P g f(g)ρ(g) †. The sum becomes an integral ifGis compact.
4 THEORY:FROM INVARIANT STATISTICS TO HARMONIC GEOMETRY
We state the framework and main results. Complete statements and proofs are in Appendices A–D.
Word embeddings.For wordsx, yin an-word family, we writeP x, Py theirunigram probabil-
ities–how often wordx, resp.y, appears in text – andP xy theirco-occurrence probability–how
oftenx, yappear together (formal definitions in Appendix A). We define then×nnormalized
co-occurrence matrixelement-wise by
M ⋆ xy = Pxy −P xPy 1
2 (Pxy +P xPy) ,(1)
andP M⋆Pitsdoubly centered version, whereP= I− 1 n 11⊤ is the centering projector.
Recent work shows that the matrixP M⋆Pspecifies which word embeddings will be learned from
text corpora. Specifically, Karkada et al. (2025) established that therleading PCA scores of a
set ofnword2vec-style embeddings inddimensions W∈R n×d can be approximated with the
positive eigenpairs{

λi, vi)}i≤r ofP M⋆P, taken in decreasing order. Namely, up to an orthogonal
transform and realification, the projection of W x ∈R d along the firstrprincipal components of
Wis approximately
√λivi(x)  i≤r . We use this characterization of empirical word embeddings
throughout our paper, as also done in Karkada et al. (2026).
Assumption: Statistical invariance.Our starting point is the assumption that a givenn-word
family carries a symmetry, as in the real-world examples of Figure 1. Specifically, we assume that a
symmetry groupGacts on a word setLand that the co-occurrence matrix verifies:
M ⋆ g·x, g·y=M ⋆ x,y,∀g∈G,∀x, y∈L.(2)
We say that the word statistics areinvariantto the groupG. If the wordsLform aG-torsor, fixing
any word as the group identity 1 creates a bijection between the word set and the group:L≃G.
Abusing notation, Assumption 2 implies thatM ⋆ g,h =C(g −1h)for a kernelC:G→Rwith
C(g −1) =C(g)∀g, h∈G, the latter property forced by the symmetry ofM ⋆. If instead the
action is transitive with stabilizerK, the word set is the homogeneous spaceL≃G/KandCis
bi-K-invariant.
Theory: Structure of word embeddingsUsing the characterization of word embeddings and the
statistical invariance assumption above, we derive two theorems giving the analytical expression of
word embeddings under group symmetry. Their formal versions are in Thm. B.3 and Thm. D.1.
Theorem 4.1(Finite group, informal).LetGbe a finite group of ordern, and let the word setL
be aG-torsor satisfying Assumption 2. For each nontrivial real irrepρofG, let bC(ρ)be the group
Fourier coefficient atρof the kernelCassociated withM ⋆, with eigenvaluesλ (1) ρ , . . . , λ(dρ) ρ . Then,
denotingpc r the top-rscore mappc r :R d →R r, the word embeddingW g of anyg∈Gverifies:
pcr(Wg) =
"s
λ(s) ρ dρ
n ρ(g)as
#
(ρ,s,a)
,(3)
for some choices of(ρ, s, a)sorted in decreasing order ofλ(s) ρ >0, and up to orthogonal transform
and realificaction.
A version of Theorem 4.1 also holds for compact groups, see Thm. C.5. These theorems demonstrate
that word embeddings of aG-torsor word set appear like the matrix elements of the irreps ofG. The
text source determines, through its kernelC, which columns of the irreps will be most pronounced
1The base word choice is inconsequential as shown in Lemma B.4.
4

Preprint. Under review.
2 4 6
empirical mode
−0.5
0.0
0.5
1.0
1.5
2.0
2.5eigenvalue
(a) Eigenvalues Pair
k=1
k=2
k=3
k=4
0 2 4 6
circular distance, d
1.0
1.2
1.4
1.6
1.8C(d)
(b) Statistical Invariance Holds
individual month pairs
mean co-occurrence
C(d)
PC 1
PC 2
jan
feb
mar apr
may
jun
julaug
sep
octnov
dec
PC 3
PC 4
janfeb
mar
apr
may
jun
jul
aug
sep
oct
nov
dec
(c) Circles Follow
empirical theory
Figure 2:Month statistics areZ 12-invariant→embed as circles (known result, re-derived).
M ⋆ is formed using month co-occurrences in the corpustext8, using month-sense disambiguation
for “may.” The approximateZ 12-invariance ofM ⋆ causes circles to emerge in the months’ word
embeddings. See App. E for all details. (a) Spectrum ofP M ⋆P(corpus bootstrap error bars,
2.5%−97.5%), wavenumber assigned by dominant Fourier mode. The first 4 eigenvalues split into
approximate pairs with the same wavenumber, a hint thatZ12-invariance could be present in the data.
(b) Averaged kernelC(d)of the individual month pair co-occurrences. The data follow the kernel
rather than just averaging to it (average predicts raw data withR2 = 0.87), asserting an approximate
invariance toZ 12. (c) The two circular planes. Left:k= 1plane with median31 ◦/month. Right:
k= 2plane with median66 ◦/month.
(largestλ (s) ρ ). Furthermore, if the dimension prescribed to the word embeddings is too small, irrep
elements with sufficiently smallλ (s) ρ are truncated.
Next, we consider homogeneous spaces. We save the general discussion for the Appendix and focus
on the particular case of the sphereS 2 for clarity, which is the case relevant for our experiments.
Theorem 4.2(Homogeneous spaceS 2).LetLbe a finite word set in which each wordxis as-
signed a distinct pointp x ∈S 2, and satisfying Assumption 2. For each degreeℓ≥1, let
cℓ = 1 2 R 1 −1 C(t)P ℓ(t)dtforP ℓ the degree-ℓLegendre polynomial andCa kernel correspond-
ing toM ⋆. Then, denotingpc r the top-rscore mappc r :R d →R r, the word embeddingW x of any
x∈Lsatisfies:
pcr(Wx) =
h√cℓ Y m ℓ (px) i (ℓ,m) ,(4)
for some choice of(ℓ, m), sorted in decreasing order ofcℓ >0, whereY m ℓ denotes a real spherical
harmonic of degreeℓ, and and up to orthogonal transform and realificaction. Since there are2ℓ+ 1
spherical harmonics of degreeℓ, the embedding contains subspaces of dimension2ℓ+ 1.
Realification.Embeddings are real, while the eigenvectors above are in general complex. Hence,
we must convert them to real coordinates, using a methodology that depends on the type of irrep
(Proposition B.6). In our experiments, irreps can be realified (if needed) in a simple, formulaic way.
5 THE CYCLIC CASE:MONTHS AND THE PRINGLE
We test the theory on a known case: the cyclic groupG=Z 12 acting on the twelve months. We
utilize thetext8corpus (Wikipedia dump, 17M tokens, (Mahoney, 2011)). We recover the same
results as (Karkada et al., 2026), but using group theory instead of their Fourier analysis.
PredictionsAll irreps ofZ 12 are 1-dimensional complex Fourier modes, indexed by a wavenum-
berk∈ {0, . . . ,11}. The theory predicts that the embedding of monthm∈ {0, . . . ,11}belongs to
a direct product of circles of the form

cos(2πkm/12),sin(2πkm/12)

with nonzerok. The radii
of these circles is obtained through the discrete Fourier transform of the kernelC(d), the average
co-occurrence of monthsd∈ {0, . . . ,6}months apart. Specifically,
q
bC(d)is the radius of the
circle withk=d.These radii are the corpus supplied scalars for ranking the irreps.
5

Preprint. Under review.
(a)  Statistical Invariance Holds (b)  Dihedral Irreps Follow
majors minors
majorsminors
M⋆
majors minors
ΠT/I M⋆
PC 1
PC 2
C
C#
D
D#
E
F
F#
G
G#
A
A#
B
c
c#
d
d#
e
f
f#
g
g#
a
a#
b
Bach
PC 1
PC 2
C
C#
D
D#
E
FF#
G
G#
A
A#
B
c
c#
d
d#
e
f
f#
g
g#
a
a#
b
ChordBERT
−1.5
−1.0
−0.5
0.0
0.5
1.0
1.5
major minor empirical theory
Figure 3:Chord statistics areT /I-invariant→embed as dihedral irreps.See Appendix F for
all details. (a) Left: EmpiricalM ⋆ over the24triads from371Bach chorales. Majors and minors
are listed fromCtoBin chromatic order. Right:Π T /IM ⋆ is the projection ofM ⋆ onto matrices
that areT /I-invariant. Importantly,Π T /IM ⋆ captures much of the structure ofM ⋆ (R2 = 0.822),
demonstrating an approximateT /I-invariance inM ⋆. (b) Uppercase and lowercase refer to major
and minor chords respectively. An orthogonal transform is used to align theoretical predictions with
empirical embeddings in each case. Left: due to the statistical invariance in (a), a dihedral irrep,
in the form of interleaved circles of majors and minors, emerges in the Bach chord embeddings.
Our predictions obtain a per-chord cosine similarity of0.98with the real embeddings. Right: Our
empirical embeddings are the average activation of each triad in the layer 3 (selected for high isotypic
energy, Figure 7) residual stream of ChordBERT across all 371 chorales. The same dihedral structure
emerges. We use the Gram matrix of these centered embeddings (normalized by the root mean
square of its diagonal) as a proxy forM ⋆. This gives us theoretical predictions with a per-chord
cosine sim. of0.91.
Results: The embeddings realize the cyclic irrepsAs we see in Figure 2 B, the averaged kernel
is faithful to the individual months’ co-occurrences. Although the statistics will never be perfectly
invariant, they are close enough that our theoretical circular predictions line up nicely with the
actual embeddings in Figure 2 C. The first 4 empirical PCs of the embeddings match the theoretical
predictions at a per-month cosine of 0.96 (median 0.97), under one aligning orthogonal transform
per plane, compared to a label-shuffle null of mean 0.35. The classic Pringle lives in the first 3
dimensions of these embeddings, a sinusoidal on top of a circular base.
6 THE NONABELIAN CASE:DIHEDRAL CHORD GEOMETRY INBACH
We test the theory on a novel case: the dihedral groupG=D 12 acting on the24major and minor
triads, which form aD 12-torsor under the transposition–inversion groupT /I ∼= D12. We utilize
the chord sequences from the371Bach chorales,music21Cuthbert & Ariza (2010):24k chord
tokens, full sonority vocabulary of92types with the24triads as the analyzed subsystem. See App. F
for details.
Predictions.The24major and minor triads form aD 12-torsor under the transposition-inversion
groupT /I ∼= D12. Hence, Theorem 4.1 applies.D 12 has four1-dimensional embeddings
and five2-dimensional irreps (E 1 . . . , E5). From foresight, none of the1-dimensional irreps
are strongly present in the empirical embeddings, so we will neglect them. We predict that
the embeddings of the majorsm∈ {0, . . . ,11}are a direct product of circles of the form
cos(2πhm/12 +ϕ),sin(2πhm/12 +ϕ)

, while the embeddings of the minorsn∈ {0, . . . ,11}
are instead a direct product of circles of the form

cos(2πhn/12−ϕ),sin(2πhn/12−ϕ)

, existing
in the same set of planes, whereϕis some constant (dependent on the corpus) andh∈ {1, . . . ,5}.
Furthermore, we predict that these interleaved circles of majors and minors share the same radius, a
corpus determined value computed as in Thm. 4.1.
Statistical assumption is verified: Chord co-occurrence statistics exhibit dihedral symmetry
We formM ⋆ with a3-token window from our collected24k chord tokens. We can find the projection
ofM ⋆ onto matrices that are invariant with respect to some groupG,Π GM ⋆, by the element-wise
6

Preprint. Under review.
computationΠ GM ⋆ x,y = 1 |G| P g∈G M ⋆ gx,gy , i.e., replacing entries that would be equivalent under
invariance by their average. Transposition invariance only,Π Z12 M ⋆ x,y (26 independent parameters),
explainsR 2 = 0.830ofM ⋆. FullT /Iinvariance,Π T /IM ⋆ (19 independent parameters), still ex-
plainsR 2 = 0.822with 7 less parameters. It would be impossible forT /Iinvariance to outperform
Z12 as it strictly adds restrictions on which elements must be equal, yet it has near identical perfor-
mance. Furthermore, it is not the case thatT /IandZ 12 score highly due to some trivial reason. A
chord-relabeling null givesp= 5×10 −4: none of2000random relabelings yields aT /I-invariance
R2 approaching the observed0.822.
Result I: The embeddings realize the dihedral irrepsWe factorizeM ⋆ and analyze its leading
plane. Our prediction of interleaved circles of major and minors emerges (Figure 3 B, left). The
plane’s isotypic energy (loosely speaking, value from 0 to 1 on how much asubspacecorresponds
to a given irrep), is very high at 0.958 (E 5), far above a chance level ofd 2 ρ/24 = 4/24≈0.17.
(App. Fig. 6). Most importantly, our theoretical predictions for the 24 chords give aper-chordcosine
of0.98. In fact, our theoretical predictions for the first 3 planes of embeddings (6 dimensions) are
all high at0.98/0.94/0.80, respectively (Appendx F).
Result II: The circle of fifthsIn particular, the leading plane isthe circle of fifths, a classic orga-
nizing structure of tonal harmony, realized as interleaved circles at the corpus dictated radius. The
circle of fifths has been foundempiricallyin chord embeddings before, on a far larger and entirely
different music source of∼89k popular songs (Lahnala et al., 2021); the present resultderivesit. It
is a column of the 2-dimensionalE 5 irrep ofD 12.
Result III: Same structure in chord representation modelObtaining dihedral irreps in our
chord embeddings is theoretically guaranteed once statistical invariance is established. However,
in ChordBERT He et al. (2026), a 4.71M parameter transformer, the circle of fifths also emerges
(Figure 3 B, right). The structures we predict for word embeddings potentially have wide spread
appearances across many architectures; if a structure is useful in one setting, it is likely helpful
elsewhere.
Competing symmetry models and data efficiencyAlthough the chord statistics appears to fol-
low a dihedral (T /I) structure, other conjectures for the underlying symmetry could perform even
better. We compare seven other natural hypotheses about the structure of the co-occurrence matrix
in F. Some notable examples includeZ 12 (transposition-only invariance as before, 26 independent
parameters), and the raw empiricalM ⋆ itself (300 independent parameters). TheT /Isymmetry
has (at least) comparable predictive performance on held-out chorales to each of other models, even
those with more parameters. Furthermore, theT /Isymmetry is the most efficient hypothesis at
gaining predictive power when fit on a fewer number of chorales. Both of these observations point
toT /Ibeing the most stringent form of symmetry the data reliably follows.
7 THE CONTINUOUS CASE:THE SKY SPHERE AS A HARMONIC EMBEDDING
Berdnikov & Liokumovich (2026) discovered that large language models, prompted aboutcelestial
proximity, represent188stars and constellations on a decodable sphere in the residual stream, and
posed the question of this geometry’s origin. Our theory answers this question.
PredictionsThe sphere is the homogeneous spaceS 2 =SO(3)/SO(2). Although an LLM’s
residual stream is not strictly in our theory, which considers word embeddings, we use Theorem 4.2
to predict what to expect in its structure. If the “effective” statistics are invariant (co-occurrence of
celestial objects is a function only of angular separation), each dimension of the representation takes
the form of a spherical harmonic.
The dimensions corresponding toℓ= 1, first order spherical harmonics, are precisely a sphere when
plotted, as has been seen in Berdnikov & Liokumovich (2026). However, our theory further predicts
the presence of spherical harmonics of higher orders (e.g.ℓ= 2,3, . . .).
7

Preprint. Under review.
0 50 100 150
true θ (deg)
−0.4
−0.2
0.0
0.2
0.4
0.6
0.8
C(θ)
(a) Structural Invariance
fitted kernel C(θ)
±1 std. dev.
ℓ=1 ℓ=2 ℓ=3 ℓ=4
1
3
5
7
9
11
13
15 empirical mode
0.0
0.2
0.4
0.6
0.8
1.0
degree purity
Mistral Large 2 Books
100
200
300
true RA (deg)
(b) Spherical Harmonics Follow (c) Spherical Structure Across Sources
empirical theory
Figure 4:LLM’s structure is function of true celestial angles→spherical harmonics emerge,
same structure also in text.Mistral Large 2 (123B) residual stream for188sky objects (Berdnikov
& Liokumovich, 2026) at layer 72 (where positions∈R 3 on the celestial sphere can be best linearly
decoded). See Appendix G for all details. (a) Weighted Nadaraya–Watson regression kernel predicts
Gram matrix of LLM activations over objects from actual angular separation. Standard deviation
follows the curves shape, suggesting structure is largely dependent on the true angle, our proxy for
statistical invariance ofM ⋆. (b) Spherical harmonic purity of the model’s PCs: blocks of spherical
harmonics appear.ℓ= 0mode is removed by centering. (c) Comparison withℓ= 1harmonics
(sphere) evaluated at true celestial positions after a fitting rotation (and global scaling for the LLM).
Color bar shows right ascension Left: LLM residual steam with a randomly selected 75/188 objects
shown. Best-aligned3-dimensional subspace is found within the first four empirical modes (same
search repeated for permutation null). Per-object cosine sim. of0.92(median0.97) against an object
permutation null of0.12(95% 0.17). Right: Top 3 PCs of book corpus’s centeredM ⋆. Per-object
cosine sim. of0.55(median0.68) against a null0.22(95% 0.32).
A small technical detail: our theory assumes a uniform sampling onS 2, which celestial objects
do not exactly obey. To prevent any of our estimators being strongly influenced by over-sampled
regions of the sphere, we employ inverse density weighting (see Appendix G).
(Effective) statistical assumption is verified: Gram matrix of activations is function of true
angular separation.Figure 4 analyzes the released activations for Mistral Large 2,X∈R 188×16
(mean across prompts for each object, top 16 PCs, App. G). As a proxy forM ⋆, we consider the
doubly centered, Gram matrixP XX T P∈R 188×188 (normalized by the root mean square of its
diagonal). In place of statistical invariance, we ask forstructural invariance: off diagonal-elements
of this matrix are a function of only the true angular separation between the corresponding celestial
objects. In Figure 4 A, we see this approximately holds. The standard deviation of a regressed
kernel, predicting the upper triangle of the Gram matrix from objects’ true angular separation, hugs
the curve’s shape. As further evidence, an averaging of all the upper triangular elements, grouped in
bins of10 ◦, gives anR 2 = 0.49for predicting the original matrix (against a object permutation null
of0.002).
Results: The embeddings realize the spherical harmonicsAs seen in Figure 4 B the eigen-
modes formdegree-ordered harmonic blocks: modes1–4areℓ=1,5–8areℓ=2, and thenℓ=3
emerges. A completely random direction would have a purity on the order of10 −2 so the values
in this heatmap are far above chance. Five of seven models in Berdnikov & Liokumovich (2026)
demonstrate the same spherical harmonic ordering (Table 2). Notably, theℓ=1energy occupies four
modes rather than three because PC1is largely occupied by a star/constellation type direction, as
noted by Berdnikov & Liokumovich (2026).
Results: The same structure appears in an independent corpus.The harmonic structure should
be visible in text embeddings themselves, specifically in thegenrewhose discourse is organized by
sky position: star observing guides. However, many astronomy books are organized by topics such
as mythology or famous constellations rather than by complete “tours of the sky”. Hence, from 24
open-source general astronomy books, we utilize the metricD= corr(M ⋆ ij,cosθ ij)with a one-
sided location-permutationp <0.05(discussed in App. G) to select our corpus. Although passing
this criterion would certainly be required for developing spherical harmonics in the embeddings,
linear correlation with the true cosines does not by itself ensure the structure will be present. Four
8

Preprint. Under review.
guides pass (Dfrom0.22to0.45,131k tokens in total). V olume is not enough to score highly on
this metric,genreis critical:text8(17M tokens,130×the guides) givesD= 0.01(p= 0.48).
text8’s counts are dominated by non-sky versions of the terminology. (Table 3; App. G). Notably,
the guides’M ⋆ over39well-counted objects yields a kernel of similar form as the model’s activation
kernel (correlation0.95with Figure 4 A).
Figure 4 C compares the LLM activations in layer 72 (where celestial positions are best linearly
decoded) and the book corpus’s embeddings with degree-1 spherical harmonics evaluated at the
celestial object’s true positions. For the books, we view the first 3 PCs of its embeddings, while
for the model, we look at the mostℓ= 1aligned3D-subspace in its first 4 PCs, hypothesizing that
the structure could besmearedacross dimensions. In both settings the spherical structure emerges,
although in a much sharper fashion for the model. We perform the same analysis for degree-2
harmonics. Locating the mostℓ= 2aligned subspace in PCs 5-12 of the model (based on Figure 4
B), we obtain a per-object cosine similarity of0.73(median0.82) compared to a object permutation
null of0.17(95%:0.21). Similarly, looking at PCs 4-8 of the books’ centeredM ⋆, we see a per-
object cosine sim. of0.39(median0.44)against a null of0.27(95% 0.35). In either case, theℓ= 2
structure is weaker than that ofℓ= 1, but it is certainly still present.
Book corpus’s weaker harmonic structure results from less data:It may at first seem surprising
that the books exhibit a lesser strength of spherical harmonic structure than the LLM residual stream.
We argue that the book corpus’s performance is typical for its size. We simulate new data assuming
the zonal kernel fit to the books exactly specifies the true underlying statistics, and see how well
dipole harmonics tend to align with the synthetic data (details in G). Figure 5 demonstrates that
our book corpus is actually a typical (if not good) draw at its size (≈93%from 1000 simulations).
At around roughly∼32–64×the corpus size, we would expect the dipole structure in the textual
embeddings to be just as present as in the model. The idea that a123B parameter LLM could
have consumed this amount of relevant stargazing material is very plausible. Hence, a possible
explanation for the difference in structure quality between the model and textual embeddings is
simply data volume.
8 DISCUSSION
1/4 1/2 1 2 4 8 16 32 64 128
pair-count multiplier (x book corpus)
0.0
0.2
0.4
0.6
0.8
1.0per-object cosine similarity
Mistral Large 2
per-object cosine
similarity (0.92)
simulated: zonal truth + Poisson counts
5-95% of simulations
book corpus (0.55)
Figure 5:Weaker harmonic structure in book cor-
pus could be a sample size effect.We take the zonal
kernel fit to the books as ground truth and simulate new
syntheticM ⋆’s, using Poisson counts for off-diagonal
elements at various multiples of the corpus’s size. (full
methodology in App. G). We measure how well the
simulated data aligns with dipole spherical harmonics,
using the same analysis pipeline as in Figure 4. Per-
object cos. sim. (mean with 5–95% band) captures the
observed corpus (star) at1×and crosses the LLM’s
performance (0.92, dashed) at∼32–64×the books’
counts: aneffective corpus sizefor the model.
A unifying theory of structured embed-
dings.A Pringle traced by the months,
the circle of fifths in Bach’s chords, and a
globe of spherical harmonics in a language
model’s activations initially appear unre-
lated. However, all three are predictions
from the same theory. Underlying symme-
try in the statistics of data, when present,
is a powerful restraint on permissible em-
beddings.
LimitationsThe theory’s scope is set by
its premise: it considers only families
of words whose co-occurrence statistics
are, at least approximately, invariant un-
der some group—a strong structural prop-
erty that many word families will sim-
ply not have. Months, chords, and ce-
lestial objects were chosen because their
statistics demonstrably carry such an in-
variance. Yet, for most of language such
structure might not be immediately clear.
For LLMs there is the further caveat that
our theorems concern trained word em-
beddings, and their application to activa-
tions rests on an empirical premise.
9

Preprint. Under review.
ACKNOWLEDGMENTS
We thank Hasan Atakan Bedel, Qiqi Xian, Katrin Franke, and Imran Thobani for their useful com-
ments on the manuscript. A.T. acknowledges support from the Amaranth Foundation (Enigma
Project). N.M. acknowledges funding from the NSF grant 2313150 and partial support from a
Goodfire Research Grant with access to Silico, Goodfire’s interpretability research agent.
REFERENCES
Aleksandr Berdnikov and Yevgeny Liokumovich. Sky sphere representation in language models,
2026. URLhttps://arxiv.org/abs/2607.27092.
Bilal Chughtai, Lawrence Chan, and Neel Nanda. A toy model of universality: Reverse engineering
how networks learn group operations. InInternational Conference on Machine Learning, pp.
6243–6267. PMLR, 2023.
Alissa S Crans, Thomas M Fiore, and Ramon Satyendra. Musical actions of dihedral groups.The
American Mathematical Monthly, 116(6):479–495, 2009.
Michael Scott Cuthbert and Christopher Ariza. Music21: A toolkit for computer-aided musicol-
ogy and symbolic music data. In J. Stephen Downie and Remco C. Veltkamp (eds.),ISMIR,
pp. 637–642. International Society for Music Information Retrieval, 2010. ISBN 978-90-393-
53813. URLhttp://dblp.uni-trier.de/db/conf/ismir/ismir2010.html#
CuthbertA10.
Feng Dai and Yuan Xu.Approximation theory and harmonic analysis on spheres and balls. Springer,
2013.
Persi Diaconis.Group representations in probability and statistics. Institute of Mathematical Statis-
tics, 1988.
Josh Engels, Eric Michaud, Isaac Liao, Wes Gurnee, and Max Tegmark. Not all language model
features are one-dimensionally linear. InInternational Conference on Learning Representations,
volume 2025, pp. 84591–84622, 2025.
G.B. Folland.A Course in Abstract Harmonic Analysis, Second Edition. Textbooks in Mathematics.
Taylor & Francis Group, 2016. ISBN 9781498727136.
Wes Gurnee and Max Tegmark. Language models represent space and time. InInternational Con-
ference on Learning Representations, volume 2024, pp. 2483–2503, 2024.
Yulong He, Ivan Smirnov, and Yanming Li. Modeling stylistic co-evolution in symbolic music
heritage collections, 2026. URLhttps://arxiv.org/abs/2607.23957.
Dhruva Karkada, James Simon, Yasaman Bahri, and Michael DeWeese. Closed-form training dy-
namics reveal learned features and linear structure in word2vec-like models. InAdvances in
Neural Information Processing Systems, volume 38, Main Conference, pp. 3967–4000. Curran
Associates, Inc., 2025. doi: 10.52202/085713-0140.
Dhruva Karkada, Daniel J Korchinski, Andres Nava, Matthieu Wyart, and Yasaman Bahri. Sym-
metry in language statistics shapes the geometry of model representations.arXiv preprint
arXiv:2602.15029, 2026.
Allison Lahnala, Gauri Kambhatla, Jiajun Peng, Matthew Whitehead, Gillian Minnehan, Eric Gul-
dan, Jonathan K. Kummerfeld, Anıl C ¸ amcı, and Rada Mihalcea. Chord embeddings: Analyzing
what they capture and their role for next chord prediction and artist attribute prediction. InArti-
ficial Intelligence in Music, Sound, Art and Design, pp. 171–186, Cham, 2021. Springer Interna-
tional Publishing. ISBN 978-3-030-72914-1.
Omer Levy and Yoav Goldberg. Neural word embedding as implicit matrix factorization. InAd-
vances in Neural Information Processing Systems, volume 27. Curran Associates, Inc., 2014.
Matt Mahoney. Large text compression benchmark (text8).http://mattmahoney.net/dc/
textdata.html, 2011.
10

Preprint. Under review.
Giovanni Luca Marchetti, Daniel Kunin, Adele Myers, Francisco Acosta, and Nina Miolane. Se-
quential group composition: A window into the mechanics of deep learning. InInternational
Conference on Machine Learning (ICML), 2026.
Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. Progress measures
for grokking via mechanistic interpretability. InInternational Conference on Learning Represen-
tations, 2023.
Kiho Park, Yo Joong Choe, and Victor Veitch. The linear representation hypothesis and the geom-
etry of large language models. InProceedings of the 41st International Conference on Machine
Learning, volume 235 ofProceedings of Machine Learning Research, pp. 39643–39666. PMLR,
2024.
Kiho Park, Yo Joong Choe, Yibo Jiang, and Victor Veitch. The geometry of categorical and hierar-
chical concepts in large language models. InInternational Conference on Learning Representa-
tions, volume 2025, pp. 76441–76463, 2025.
Jeffrey Pennington, Richard Socher, and Christopher Manning. GloVe: Global vectors for word rep-
resentation. InProceedings of the 2014 Conference on Empirical Methods in Natural Language
Processing (EMNLP), pp. 1532–1543, Doha, Qatar, October 2014. Association for Computational
Linguistics. doi: 10.3115/v1/D14-1162.
Jean-Pierre Serre.Linear Representations of Finite Groups, volume 42 ofGraduate Texts in Math-
ematics. Springer-Verlag, New York, 1977. ISBN 978-0-387-90190-9.
APPENDIXOVERVIEW
Appendices A–D contain the complete theory while Appendices E–G contain all experimental de-
tails. Specifically, the appendix is organized as follows.
Appendix A discusses howword2vec-style embeddings can be approximated by an eigendecom-
position of a co-occurrence matrix of the words, and states the “statistical invariance under a group”
assumption necessary for our theory to apply. Appendix B considers embedding structure when the
words are invariant under a finite group (Theorem B.3), and considers two special cases: the cyclic
and dihedral cases, which are relevant to our “months” and “chords” experiments. Appendix C
generalizes the theory to compact groups. Appendix D further treats homogeneous spacesG/K,
considering the special case of Gelfand Pairs and in particularS 2, which is relevant to our sky-
sphere experiments.
Appendices E, F, G give the experimental details for the month, music, and sky-sphere experiments,
respectively. Finally, Appendix H discusses reproducibility, while Appendix I gives our AI use
statement.
A WORDEMBEDDINGS ANDSTATISTICALINVARIANCE
A.1 FROM STATISTICS TO EMBEDDINGS
LetLbe a finite set ofnwords. Following Karkada et al. (2026), for arbitrary wordsx, y∈Lwe
consider thenormalized co-occurrence matrixdefined by
M ⋆ xy = Pxy −P xPy 1
2 (Pxy +P xPy) ,(5)
whereP xy is the probability that wordsx, yco-occur within a context window andPx is the unigram
probability (both defined below). SinceP xy =P yx, the matrixM ⋆ is symmetric.
Estimation conventions.Throughout the paper,P xy ∀x, y∈LandP x ∀x∈Lare estimated
from a respective corpusCofNtokens as follows. Fix a functionf(δ)≥0supported on token gaps
11

Preprint. Under review.
δ= 1, . . . , B, with total massF:=PB δ=1 f(δ). We define a weighted count matrix
Wx,y =
X
i
δC[i],x
BX
d=1
f(d)(δ C[i+d],y +δ C[i−d],y )
whereC[i]is thei th token in the corpus. For multiple corpora, we can form a singleW xy through
summation. Note that this definition enforcesW xy =W yx. Then, with additive smoothingα≥0,
and the number of mentions of wordxbeingn x we define
Pxy = Wxy +α 2F N , P x = nx N ,(6)
so that2F Nis the total window mass (Ntokens, each opening a two-sided window of mass2F,
neglecting edge effects). We can further define anopportunity normalizedco-occurrence rate:
Rxy = Pxy PxPy = Wxy +α nxny ·2F/N = Wxy +α E0[Wxy] ,(7)
whereE 0[Wxy] =n xny ·2F/Nis the expected value ofW x,y when mentions are placed indepen-
dently (neglecting edge effects). We have thatM ⋆ xy = 2(Rxy −1)/(R xy + 1) = 2 tanh(1 2 lnR xy), soM ⋆ is strictly increasing inR xy and saturates at±2.
Per-system choices of(B, f, α)are stated in the experimental appendices (months:B= 16,f(δ) =
B+1−δ,α= 0; chords:B= 3, flat:f(δ) = 1,α= 0.5; sky:B= 30, flat:f(δ) = 1,α= 0.25).
Word EmbeddingsKarkada et al. (2025) shows that the matrixP M ⋆Pcan be used to generate
word embeddings. Specifically, therleading PCA scores of a set ofnword2vec-style embed-
dings inddimensions W∈R n×d can be approximated with the positive eigenpairs{  λi, vi)}i≤r
ofP M⋆P, taken in decreasingλ i order. Up to an orthogonal transform and realification, the pro-
jection of W x ∈R d (for wordx) along the firstrprincipal components of Wis approximately√λivi(x)  i≤r . This is how we generate all empirical word embeddings in this paper.
Furthermore, transforming the generation of word embeddings into an eigendecomposition is in-
credibly fruitful for theory. WheneverM ⋆ obeys certain symmetries, we can theoretically predict
its eigenpairs, which we discuss in the upcoming sections.
A.2 STATISTICALINVARIANCE UNDER AGROUP
Definition A.1(Torsor).A (left)G-torsoris a setLwith a (left) action ofGthat is free and tran-
sitive: for everyx, y∈Lthere is exactly oneg∈Gwithg·x=y. A torsor is “a group that
has forgotten its identity element”: it becomes isomorphic toGonce a base point is chosen, but no
choice is canonical.
Example A.2.The24major and minor triads form a torsor under the transposition–inversion group
T /I∼= D12 and the12months form aZ 12-torsor.
Definition A.3(Statistical invariance under a group).We say that aG-torsor word setLis statisti-
cally invariant under the groupGif itsM ⋆ obeys
M ⋆ g·x, g·y =M ⋆ x,y for allg∈G, x, y∈L.
Lemma A.4(Kernel).Consider aG-torsor word setL. Fix a base pointx 0 ∈Land identifyL ∼= G
viag7→g·x 0. Then, abusing notation, Definition A.3 is equivalent to the existence of some (kernel)
C:G→Rwith
M ⋆ g,h =C(g −1h)∀g, h∈G,(8)
and symmetry ofM ⋆ forcesC(g −1) =C(g)∀g∈G(note we change from the main text convention
of denoting1as identity to the more standarde).
Proof.First, we assume thatM ⋆ is invariant under the groupG. Then we defineC:G→Rby
C(g) =M ⋆ e,g ∀g∈G. Hence, from statistical invariance, for anyg, h∈G,M ⋆ g,h =M ⋆ e,g−1h =
C(g −1h).
12

Preprint. Under review.
Now, we assume thatM ⋆ g,h =C(g −1h)∀g, h∈G. Hence, for anya∈G, we have thatM ⋆ a·g,a·h =
C(g −1a−1ah) =C(g −1h) =M ⋆ g,h, which is precisely statistical invariance underG. Finally,
C(g −1h) =M ⋆ g,h =M ⋆ h,g =C(h −1g) =C((g −1h)−1)∀g, h∈G, which gives us thatC(g) =
C(g −1)∀g∈G.
B FINITE GROUPS
Throughout this section,Gis a finite group with|G|=n. Furthermore, we assume we have a
G-torsor word setLwhoseM ⋆ in statistically invariant underG. Under some arbitrary choice of
base point, this allows us to associate a real kernelC:G→RwithM ⋆ as in Lemma A.4.
B.1 HARMONIC ANALYSIS PRELIMINARIES
Let bGdenote a complete set of inequivalentunitaryirreducible representationsρ:G→U(d ρ), so
that P ρ∈ bG d2 ρ =n. We note the Schur orthogonality relations for matrix coefficients: forρ, σ∈ bG,
X
g∈G
ρab(g) σce(g) = n dρ δρσ δac δbe,(9)
and the generalized Fourier transform ofC,
bC(ρ) = X
g∈G
C(g)ρ(g)∈C dρ×dρ .(10)
whered ρ is the dimension of the irrepρ.
Lemma B.1.UnderCreal withC(g −1) =C(g), each bC(ρ)is Hermitian.
Proof. bC(ρ) † = P g C(g)ρ(g) † = P g C(g)ρ(g −1) = P g C(g −1)ρ(g) = P g C(g)ρ(g) = bC(ρ).
Accordingly each bC(ρ)admits an orthonormal eigenbasis{u (s) ρ }dρ s=1 ⊂C dρ with real eigenvalues,
bC(ρ)u (s) ρ =λ (s) ρ u(s) ρ , λ (s) ρ ∈R.
B.2 CENTERING REMOVES EXACTLY THE TRIVIAL REPRESENTATION
Lemma B.2(Centering).The constant vector1is an eigenvector ofM ⋆ with eigenvalueµ 0 =P
g C(g).M ⋆ is real symmetric so we may construct an orthogonal eigenbasis for its eigenspace
with1explicitly included.P M ⋆P(withP= I− 1 n 11⊤) has these same eigenpairs asM ⋆ except that the pair(µ 0,1)is replaced by(0,1); no other eigenvector or eigenvalue is altered.
Proof.M ⋆1=  P g C(g)  1from equation 8, so1is indeed an eigenvector. Furthermore, if
M ⋆v=λvwithv⊥1thenP v=v. Hence,P M ⋆P v=P M⋆v=λP v=λv, whileP M ⋆P1=
0.
For obtaining our word embeddings fromP M⋆P, we can diagonalizeM ⋆ and discard the constant
mode. This constant mode corresponds to the trivial representation of the group,ρ(g) = 1∀g∈G.
B.3 EMBEDDINGTHEOREM FOR FINITE GROUPS
Theorem B.3(Diagonalization of invariant statistics; finite case).LetGbe a finite group with
nelements. Assume we have aG-torsor (Definition A.1) word setLwhoseM ⋆ (Equation 5) is
statistically invariant underG. Under an arbitrary choice of base point (arbitrary from Lemma
B.4), we associate withM ⋆ a kernelC:G→Ras in Lemma A.4. From Lemma B.1, bC(ρ)admits
an orthonormal eigenbasis{u s ρ}dρ s=1 ⊂C d with real eigenvaluesλ (s) ρ . Let bGdenote a complete
13

Preprint. Under review.
set of irreducible unitary representations ofGas usual. For eachρ∈ bG, each eigenvector index
s∈ {1, . . . , dρ}and each row indexa∈ {1, . . . , dρ}, we define
ψρ,a,s(g) :=
q
dρ
n

ρ(g)u (s) ρ  a.(11)
Then:
(i) Eachψ ρ,a,s is an eigenvector ofM ⋆ with eigenvalueλ (s) ρ :M ⋆ ψρ,a,s =λ (s) ρ ψρ,a,s.Fur-
thermore, there exists a choice of equivalent irreducible unitary representations,ρ ′, such
that we have eigenvectors
q
dρ
n ρ′(g)as.
(ii) The family{ψ ρ,a,s :ρ∈ bG,1≤a, s≤d ρ}is an orthonormal basis ofℓ 2(G) ∼= Cn
(P ρ d2 ρ =nvectors).
(iii) Hence, the spectrum ofM ⋆ is{λ (s) ρ :ρ∈ bG, s∈[d ρ]}, each occurring with multiplicity
(at least)d ρ and
P M⋆P= X
ρ̸=ρtriv
dρX
s=1
λ(s) ρ
dρX
a=1
ψρ,a,s  ψρ,a,s† .
whereP=I− 1 n 11T .
Proof.(i) Substitutingh=gk,
(M ⋆ψρ,a,s)(g) = X
h
C(g −1h)ψ ρ,a,s(h) =
q
dρ
n
X
k
C(k)

ρ(g)ρ(k)u (s) ρ  a
=
q
dρ
n
h
ρ(g) bC(ρ)u (s) ρ
i
a
=λ (s) ρ ψρ,a,s(g).
This proves the first claim. Now, for some irrepρ, letUρ =
h
u(1) ρ | · · · |u(dρ) ρ
i
. Note thatU ρ is unitary
since bC(ρ)is Hermitian. Let us define the equivalent unitary irrepρ′ :=U † ρ ρ Uρ. Furthermore, bC(ρ)
=U †ΛUwhereΛ = diag  λ(1) ρ , . . . , λ(dρ) ρ  .Hence,
bC(ρ ′) = X
g∈G
C(g)U † ρ ρ Uρ =U † ρ [C(ρ)U ρ = Λ.
We can choose the basis vectors{e i}dρ i=1 as the eigenbasis for bC(ρ ′). Plugging into our formula for
the eigenvectors above, we obtain
r
dρ
n [ρ(g)es]a =
r
dρ
n ρ(g)as
(ii) Orthonormality: expandingψ ρ,a,s(g) = p dρ/n P b ρab(g) (u(s) ρ )b and applying (9),
⟨ψρ,a,s, ψσ,c,t⟩=
√
dρdσ
n
X
b,e
(u(s) ρ )b(u(t) σ )e X
g
ρab(g)σce(g) =δ ρσ δac ⟨u(t) ρ , u(s) ρ ⟩Cdρ =δ ρσδacδst.
Completeness follows by counting: there are P ρ d2 ρ =northonormal vectors in ann-dimensional
space. (iii) is immediate from (i)–(ii) and Lemma B.2.
Two freedoms are apparent in Theorem B.3: the choice of equivalent irreps, and the choice of eigen-
basis of bC(ρ). We show the third potential source of freedom, choosing the base point, produces
no permissibleψ ρ,a,s outside of the previous two freedoms in Lemma B.4. Both of these freedoms
do not amount to “structural” changes. We spare the small derivations, but one can see the first
freedom amounts to a unitary rotation of our eigenbasis in theacoordinate; i.e., the basis vec-
tors{ψ ρ,a,s}dρ a=1 are unitarily rotated within their subspace. Additionally, the choice of eigenbasis
amounts to a unitary rotation acrosssinψ ρ,a,s (for fixedρ, a) for which allψ ρ,a,s posses the same
eigenvalue.
14

Preprint. Under review.
Lemma B.4(Choice of base point).Consider aG-torsor word setL. We can fix a base pointx 0 ∈L
and identifyL ∼= Gviag7→g·x 0. Under the alternative choice of base pointx ′ 0 =b·x 0, the group
elements assigned to the wordx,g x, becomesg x b−1 . Firstly, this relabeling has no effect onM ⋆
nor its eigendecomposition (what we denote asM ⋆’s indices has no effect on its numerical values).
Hence, we can freely choose any base point without any effect on the word embeddings.
What may change is our eigenvectors in equation 11. Fortunately, the proposed change of base
point produces the same set of permissibleψ ρ,a,s’s as in Theorem B.3, with the usual freedoms of
choosing equivalent irreps and an eigenbasis of bC(ρ).
Proof.M ⋆ x,y =C(g −1 x gy)whereg x, gy are the elements ofGassigned to wordsx, ybefore the
base point change. Since the matrix elements do not change, after selecting the new base point,
g→gb −1, and we have that
M ⋆ x,y =C ′(g′−1 x g′ y) =C ′(bg−1 x gyb−1).
Hence,C ′(bkb−1) =C(k)∀k∈G, soC ′(k) =C(b −1kb). whereC ′ is the new kernel. We can
see that
bC ′(ρ) =ρ(b) bC(ρ)ρ(b) −1.
Therefore, we can choose our eigenbasis of bC ′(ρ)to be{ρ(b)u (s) ρ }dρ s=1. The formula for the a
modifiedψthen becomes
r
dρ
n [ρ(g′)ρ(b)u(s) ρ ]a =
r
dρ
n [ρ(g)u(s) ρ ]a,
unchanged from before. Furthermore, if we used our freedom of choice of equivalent irreps or
eigenbasis of bC ′(ρ)when constructing the modifiedψ, those same freedoms are present in the
original set of permissibleψ’s. Hence, the sets of permissibleψbefore and after the base change are
the same.
Similar results to Lemma B.4 can be shown in the cases thatGis replaced with a compact group
(Appendix C), or homogeneous space (Appendix D).
B.4 SPECIAL CASE:KERNEL IS CLASS FUNCTION
The natural analogue of the Karkada et al. (2026) assumption that statistics depend only ondistance
in some cyclic latent space is that our kernelC, as in Lemma A.4, is aclass function. I.e., it is
constant on conjugacy classes of some respective groupG. An explanation as to why follows.
Let’s assumeM ⋆ g,h =D(g, h)∀g, h∈Gfor some “distance function”D:G×G→R. Intuitively,
distances between points shouldn’t change as we move them together through space. This suggests
the condition thatDis bi-invariant underG. In other words,
D(ag, ah) =D(ga, ha) =D(g, h)∀a, g, h∈G.
Hence,
C(g) =D(e, g) =D(a, ag) =D(e, aga−1) =C(aga −1)∀a, g∈G,
soCbeing a class function is indeed the natural analogue.
Proposition B.5(Fourier transform of class functionCis scaled identity).IfCis a class function,
then for everyρ∈ bG,
bC(ρ) = ˆc ρ Idρ ,ˆc ρ = 1 dρ X g∈G C(g)χ ρ(g)∈R,
whereχ ρ = trρ. Consequently in Theorem B.3 the eigenvalueˆc ρ has multiplicityd 2 ρ , one for each
matrix coefficient ofρ, and we can takeψ ρ,a,b(g) = p dρ/n ρ(g)ab.
15

Preprint. Under review.
Proof.For anya∈G,
ρ(a)−1 bC(ρ)ρ(a) = X
g∈G
C(g)ρ(a −1ga) = X
g∈G
C(aga −1)ρ(g) = X
g∈G
C(g)ρ(g) = bC(ρ),
so bC(ρ)commutes withρ. Hence, by Schur’s lemma bC(ρ)must be a scalar (which we will denote
ˆcρ) times the identity matrix. Taking traces of bC(ρ) = ˆcρIdρ givesd ρˆcρ = P g C(g)χ ρ(g), the
desired relation.
The consequences for Theorem B.3 follow as every unit vector ofC dρ is now an eigenvector of
bC(ρ). Additionally, note that our eigenvalues of bC(ρ),ˆcρ, are still real as before since
ˆcρ = 1 dρ X g∈G C(g) χρ(g) = 1 dρ X g∈G C(g)χ ρ(g−1) = 1 dρ X g∈G C(g −1)χρ(g) = 1 d X g∈G C(g)χ ρ(g) = ˆcρ
B.5 REALIFICATION OFEIGENFUNCTIONS
Embeddings are real, while the eigenvectors (11) are in general complex.M ⋆ is a real symmetric
matrix, so it always possible to find a real orthonormal basis for its eigenspace. The only question
is whether it is somehow possible to modify our theory’s outputted irrep-based eigenvectors in a
formulaic manner as to obtain real embeddings.
The answer depends on the “type” of irrep we are considering. Namely, we consider its Frobenius-
Schur indicator
ν(ρ) = 1 n X g∈G χρ(g2)∈ {1,0,−1},
withχ ρ(g2)denoting the trace ofρ(g 2).ν= 1,0,−1are denoted asrealtype,complextype, and
quaternionictype, respectively.
Proposition B.6(Realification Protocols).Transforming the eigenvectors(11)into real form de-
pends on the type (Frobenius-Schur indicator) of the given irrep. The different methodologies are as
follows.
(a)Real type(ν(ρ) = 1). This is the simplest case. Sinceρis real type, it is guaranteed to
be expressible as real matrices upon some appropriate change of basis. Furthermore, after
enforcing the reality ofρ, the eigenvectors of bC(ρ),{u (s) ρ }d s=1, can be chosen real as bCis
now a real symmetric matrix. Together, these enforce the reality of the eigenvectors in(11).
(b)Complex type(ν(ρ) = 0). Sinceρis of complex type, no change of basis can convert it
to real matrices. Hence, a different approach is required. Namely, for irrepsρand¯ρ, and
a, s∈[d ρ], we generate new real orthonormal eigenvectors through
ψρ,a,s, ψ¯ρ,a,s→ √ 2 Reψ ρ,a,s, √ 2 Imψ ρ,a,s (12)
(c)Quaternionic type(ν(ρ) =−1). Sinceρis of quaternionic type, it is impossible to express
it as real matrices. Furthermore, unlike the complex case, there is generally no “simple”
way to arrive at real eigenvectors which are clean functions of our eigenvectors in equation
(11). An approach instead is to take the real and imaginary components of eachψρ,a,s and
just apply Gram-Schmidt to arrive at real, orthogonal eigenvectors.
Proof.(a) Proof already discussed in proposition.
(b) Sinceρis of complex type, it is well known thatρ̸ ∼= ρ.ρand ρare genuinely nonequivalent
irreps which correspond to different eigenvectors in equation (11). The reality of our proposed
substitution is immediate. All that is left is to demonstrate that the proposed vectors are indeed
eigenvectors ofM ⋆ and are orthonormal.
We begin by proving thatReψ ρ,a,s andImψ ρ,a,s are eigenvectors with the same eigenvalueλ (s) ρ .
Namely,
Reψ ρ,a,s = 1 2 (ψρ,a,s + ψρ,a,s),Imψ ρ,a,s = 1 2i (ψρ,a,s − ψρ,a,s)
16

Preprint. Under review.
Note that
ψρ,a,s =
r
dρ
n
h
ρ(g)u(s) ρ
i
a
.
u(s) ρ is an eigenvector of bC(ρ), which in turn equals bC(ρ)from the reality ofC. Hence,
ψρ,a,s =
r
dρ
n
h
ρ(g)u(s) ρ
i
a
=ψ ρ,a,s,
so ψρ,a,s =ψ ρ,a,s is another eigenvector ofM ⋆. Furthermore,ψ ρ,a,s andψ ρ,a,s share the same
eigenvalue since
M ⋆ψρ,a,s = M ⋆ψρ,a,s = λ(s) ρ ψρ,a,s =λ (s) ρ ψρ,a,s,
taking advantage ofM ⋆ being real symmetric. Therefore,Reψ ρ,a,s andImψ ρ,a,s are indeed eigen-
vectors with eigenvalueλ (s) ρ .
Finally, checking the orthonormality of
√
2 Reψ ρ,a,s and √ 2 Imψ ρ,a,s is relatively simple asψ ρ,a,s
andψ ρ,a,s = ψρ,a,s are orthonormal with respect to any of the original eigenvectors.
(c) Gram-Schmidt returns real vectors if real vectors are first provided. Furthermore, define the
eigen-subspaceW λ ={ϕ:M ⋆ϕ=λϕ}.W λ andW λ′ are orthogonal forλ̸=λ ′ sinceM ⋆ is real
symmetric. Hence, if Gram-Schmidt is providedkvectors inW λ it will returnkvectors inW λ, i.e.,
it will return other eigenvectors.
All that is left to show is that the real and imaginary components of theψ’s are all eigenvectors and
span the space of all eigenvectors ofM ⋆. Firstly, note that sinceM ⋆ is real with real eigenvalues,
the real and imaginary components of anyψ ρ,as are automatically eigenvectors. Namely,
M ⋆ψρ,a,s =λ (s) ρ ψρ,a,s ⇒M ⋆ Reψ ρ,a,s +iM ⋆ Imψ ρ,a,s =λ (s) ρ Reψ ρ,a,s +iλ (s) ρ Imψ ρ,a,s
splits into two separate eigenvalue-eigenvector equations. Finally, these real and imaginary com-
ponents of theψspan the space of all eigenvectors automatically since theψspan the space of all
eigenvectors. Hence, Gram-Schmidt will not be missing any eigenvectors.
Only quaternionic type irreps would provide real eigenvectors whose structure do not fall neatly
from our equation 11. Fortunately, these types of irreps are arguably “rarer” in more typical groups,
and do not appear in any of our experiments.
B.6 SPECIAL CASES:CYCLIC AND DIHEDRAL GROUPS
We briefly state the structure Theorem B.3 predicts for the cyclic (Z 12) and dihedral (D 12) cases
relevant to our experiments.
Cyclic:G=Z 12 (months).All irreps are one-dimensional: charactersχ k(m) =e 2πikm/12,
indexedk= 0, . . . ,11. The generalized Fourier transform is actually the discrete Fourier transform.
Namely, bC(ρ)become scalars
ˆck =
11X
d=0
C(d)e −2πikd/12 = X
d
C(d) cos(2πkd/12),
which are real sinceC(d) =C(−d). After realification, the conjugate pairs(χ k, χ−k),k=
1, . . . ,5, fuse into two-dimensional cosine/sine planes sharing the eigenvalueˆck.k= 0is the
constant mode (removed by centering) andk= 6the one-dimensional alternating mode, which em-
pirically tends to be neglected in natural data. The predicted embedding of monthmis therefore, up
to one orthogonal transform per plane,
m7− →
p
ˆck cos
 2πkm
12

,
p
ˆck sin
 2πkm
12

k∈K
,K={k≥1 : ˆc k >0,decreasingˆc k}:
concentric circles traversed at30k ◦ per month, radius √ˆck.
17

Preprint. Under review.
Dihedral:G=D 12 (major/minor triads).LetT m andI m denote them th major and minor triad
respectively form∈ {0, . . . ,11}(with base chord C).D12 =Z 12 ⋊ Z2 has four one-dimensional
irreps and five two-dimensional irrepsE h,h= 1, . . . ,5, withE h(Tm) =R(2πhm/12)and
Eh(Im) =R(2πhm/12)F.R(θ)denotes typical 2D rotation matrix byθandF= diag(1,−1).
Note that all irreps are of real type. We will neglect the one-dimensional irreps as they do not tend
to prevalent, as least for our experiments. For eachE h, bC(E h)is a real symmetric2×2matrix
with eigenpairs(λ (s) h , u(s) h ),s= 1,2. Writingu (s) h = (cosφ,sinφ), each realized mode(h, s)with
λ(s) h >0contributes a plane in which (up to one orthogonal transform per plane)
Tm →
q
λ(s) h  cos  2πhm 12 +φ  ,sin  2πhm 12 +φ   , I m → q λ(s) h  cos  2πhm 12 −φ  ,sin  2πhm 12 −φ   ,
two interleaved twelve-point circles ofequal radius(forced by orthogonality ofE h), stepping30h ◦
per semitone, with relative offset2φ.
C COMPACT GROUPS
The finite theory extends to compact groups with only minor adjustments: sums become (Haar) in-
tegrals, matrices become integral operators, and the spectral theorem for compact self-adjoint oper-
ators supplies the discrete spectrum that makes “top eigenvalues” (and hence low-rank embeddings)
meaningful.
One practical detail: in this section, we are intrinsically assuming that we have a bijection between
a continuous groupGand some set of words. In reality, one has a finite set of words which sample
the continuous group. Hence, for theorem C.5, one forms predicted word embeddings by taking
the eigenfunctions and sampling them at the group elements corresponding to the words, forming
vectors.
C.1 HARMONICANALYSISPRELIMINARIES
We letGbe a compact Hausdorff topological group with normalized Haar measuredg(
R
G dg= 1),
and work in the Hilbert spaceL 2(G)with⟨f 1, f2⟩= R G f1f2 dg. Let bGbe the (now countably
infinite, in general) set of equivalence classes of unitary irrepsρ:G→U(d ρ). The Peter–Weyl
theorem states that the matrix coefficients{
p
dρ ρab :ρ∈ bG,1≤a, b≤d ρ}form a complete
orthonormal basis ofL 2(G), with orthogonality
Z
G
ρab(g) σce(g)dg= 1 dρ δρσ δac δbe.(13)
The generalized Fourier transform of someC∈L 2(G)now takes the form
bC(ρ) =
Z
G
C(g)ρ(g)dg∈C dρ×dρ .
C.2 INTEGRAL OPERATOR AND THE DISCRETE SPECTRUM
We naturally extend the notion of the previous real symmetric matrixM⋆ to an integral operatorM.
Namely, we first define the integral operatorMon somef∈L 2(G)by
(Mf)(g) :=
Z
G
k(g, h)f(h)dh
wherek∈L 2(G×G)
The reality and symmetry ofM ⋆ translate to requiring thatkis both real and symmetric in its inputs.
Finally, the statistical invariance ofM ⋆ with respect to some finite groupGbecomes the property
thatMcommutes with left translationL b ∀b∈G, where(L bf)(g) =f(b −1g). I.e.,ML b =L bM
∀b∈G.
18

Preprint. Under review.
From these properties,Mtakes the form of
(Mf)(g) :=
Z
G
C(g −1h)f(h)dh(14)
for some real kernelC∈L 2(G)withC(g −1) =C(g).
Lemma C.1(Hilbert–Schmidt).ForC∈L 2(G),Mis a Hilbert–Schmidt (hence compact) opera-
tor, with∥M∥ HS =∥C∥ L2.
Proof.By left invariance of Haar measure,
∥M∥2 HS =
Z
G
Z
G
|C(g −1h)|2 dh dg=
Z
G
 Z
G
|C(u)| 2du  dg=∥C∥ 2 L2 <∞.
Lemma C.2(Self-adjointness).IfCis real withC(g −1) =C(g), thenM=M ∗.
Proof. k(g, h) =C(h −1g) = C  (g−1h)−1 =C(g −1h) =k(g, h).
The properties ofMbeing Hilbert-Schmidt and self-adjoint allow us to sensibly discuss its top
eigenvalues as the well known result in Corollary C.3 describes.
Corollary C.3(Discrete real spectrum).LetGbe a compact group with normalized Haar mea-
sure, and letC∈L 2(G)be real withC(g −1) =C(g). Then the operator(Mf)(x) =R
G C(x −1y)f(y)dyonL 2(G)is Hilbert–Schmidt (Lemma C.1) and self-adjoint (Lemma C.2).
Consequently:L 2(G)admits an orthonormal basis of eigenfunctions ofM. The eigenvalues{µ k}
are real with P k µ2 k =∥C∥ 2 L2 <∞and every nonzero eigenvalue has finite multiplicity and µk →0.
Lemma C.4(Centering).The constant function1(already unit-norm) is an eigenfunction:M1=
µ01withµ 0 =
R
G C. WithP= I−Π 0, where(Π 0f)(g) =
R
G f dhis the projection onto constants,
PMPretains every eigenpair ofMexcept that(µ 0,1)becomes(0,1).
Proof.Identical to Lemma B.2, with sums replaced by integrals.
C.3 EMBEDDINGTHEOREM FORCOMPACTGROUPS
Lemma B.1 itself holds verbatim. Only the proof changes slightly as the sums become Haar integrals
and we utilize the inversion invariance of the Haar measure. Hence, bC(ρ)is Hermitian, giving
orthonormal eigenpairs bC(ρ)u (s) ρ =λ (s) ρ u(s) ρ ,λ (s) ρ ∈R.
Our setup allows us to state a theorem that is largely equivalent to the finite case.
Theorem C.5(Diagonalization; compact case).LetGbe a compact group with normalized Haar
measuredg. Let integral operatorMtake the form as in Equation 14, soMhas a discrete real spec-
trum from Corollary C.3. Let the kernel ofMbeC:G→R. Then bC(ρ)admits an orthonormal
eigenbasis{u (s) ρ }dρ s=1 ⊂C d with real eigenvaluesλ (s) ρ as mentioned above.
Furthermore, define functions
ψρ,a,s(g) = p dρ  ρ(g)u (s) ρ  a, ρ∈ bG,1≤a, s≤d ρ,
Then:
(i) Eachψ ρ,a,s is an eigenfunction ofMwith eigenvalueλ (s) ρ .
(ii) The family{ψ ρ,a,s :ρ∈ bG,1≤a, s≤d ρ}is an orthonormal basis ofL 2(G).
19

Preprint. Under review.
(iii) Hence, the spectrum ofMis{λ (s) ρ :ρ∈ bG, s∈[d ρ]} ∪ {0}, each nonzero eigenvalue
occurring with finite multiplicity, at leastd ρ, and
PMP=
X
ρ̸=ρtriv
dρX
s=1
λ(s) ρ
dρX
a=1
ψρ,a,s ⟨ψρ,a,s,· ⟩,
wherePis defined in C.4.
Proof.We spare writing every detail as the proof is largely a copy of the finite case. (i) The eigen-
function computation is the integral version of Theorem B.3(i). (ii) Orthonormality comes from (13)
while completeness results from Peter–Weyl. (iii) follows immediately from (i) and (ii).
RemarkC.6 (Kernel is class function, compact case).The discussion in Appendix B.4 is largely the
same in the compact case. Eigenvalues still take on multiplicities ofd 2 ρ, and we can express our
eigenfunctions asψ ρ,a,s = p dρ ρ(g)a,b.
RemarkC.7 (Realification, compact case).The discussion in Appendix B.5 is largely analogous.
The Frobenius-Schur indicator becomesν(ρ) =
R
G χρ(g2)dg∈ {1,0,−1}, and Proposition B.6 holds nearly verbatim. (Note that in the quaternionic case, Gram-Schmidt can be applied to functions
as it works on inner product spaces in general, not just vectors)
D HOMOGENEOUS SPACES, GELFAND PAIRS,AND THE SPHERE
Our final generalization considers words in bijection with a homogeneous space ofG. As mentioned
at the start of Appendix C, assuming we have a word set in bijection with a continuous set is not
realistic. In practice, we have a finite word set which samples a homogeneous space. We in turn
sample our predicted eigenfunctions in Theorem D.1 at these points when making actual predictions.
D.1 SETUP
LetK≤Gbe a closed subgroup of the compact groupG, and considerX=G/K, a homogeneous
space withG-invariant probability measuredx. Words are identified with points ofX.
As in Appendix B, we consider an operatorMof the form
(Mf)(g) :=
Z
G
C(g −1h)f(h)dh
whereCis real,C(g) =C(g −1), andf∈L 2(G). However, we now require thatCis bi-K-
invariant:C(k 1gk2) =C(g)fork 1, k2 ∈K(so its value is independent of the particular represen-
tative of some cosetgK).Mdescends to operating onf∈L 2(X)through
(Mf)(y) :=
Z
X
κ(y, x)f(x)dx(15)
whereκ∈L 2(X×X)is real symmetric andG-invariant (κ(gx, gy) =κ(x, y)∀g∈G). We
could equivalently replaceκwith a kernelCdefined byC(g) =κ(eK, gK)∀g∈G. Note that
Cis immediately bi-K-invariant, and has the usual properties of being real and obeyingC(g) =
C(g −1)∀g∈G. This gives us the alternative form ofM
(Mf)(gK) =
Z
G
C(g −1h)f(hK)dh,(16)
expressed instead as an integral over the group.
Let bGbe the set of equivalence classes of unitary irreps ofG,ρ:G→U(V ρ). Recall that
L2(G/K) ∼= M
ρ∈ bG
V ⊕mρ ρ , m ρ = dimV K ρ ,(17)
whereV K ρ ={v∈V ρ :ρ(k)v=v∀k∈K}is the subspace ofK-fixed vectors. An irrep
contributes exactly as many copies ofV ρ as it hasK-fixed directions.
20

Preprint. Under review.
D.2 EMBEDDINGTHEOREM FORHOMOGENEOUSSPACES
Theorem D.1(Diagonalization; homogeneous space).LetK≤Gbe a closed subgroup of compact
groupGand letX=G/K. Assume we have an integral operatorMas in Equation 16 with kernel
C:G→R. Let bGbe the set of equivalence classes of unitary irreps ofG,ρ:G→U(V ρ). We
define
Bρ :=P K ˆC(ρ)P K
whereP K =
R
K ρ(k)dkis the orthogonal projection ofV ρ ontoV K ρ . It can be seen thatB ρ is
Hermitian and preservesV K ρ , so its restriction toV K ρ admits an orthonormal eigenbasis{u s ρ}mρ s=1 ⊂
V k ρ with real eigenvaluesλ (s) ρ . Furthermore, define functions
ψρ,a,s(gK) = p dρ  ρ(g)u (s) ρ  a, ρ∈ bG,1≤a≤d ρ,1≤s≤m ρ
wherem ρ =dimV K ρ . Then:
(i)ψ ρ,a,s are well-defined onX.
(ii) Eachψ ρ,a,s is an eigenfunction ofMwith eigenvalueλ (s) ρ .
(iii) The family{ψ ρ,a,s :ρ∈ bG,1≤a≤d ρ,1≤s≤m ρ}is an orthonormal basis ofL 2(X).
(iv) Hence, the spectrum ofMonL 2(X)is{λ (s) ρ :ρ∈ bG, s∈[m ρ]} ∪ {0}; each nonzero
eigenvalue occurs with finite multiplicity, at leastd ρ, and
PMP=
X
ρ̸=ρtriv
mρ̸=0
mρX
s=1
λ(s) ρ
dρX
a=1
ψρ,a,s ⟨ψρ,a,s,· ⟩,
wherePis defined in C.4.
Proof.(i) For anyk∈K,
ψρ,a,s(gkK) = p dρ  ρ(g)ρ(k)u (s) ρ  a = p dρ  ρ(g)u (s) ρ  a =ψ ρ,a,s(gK),
usingu (s) ρ ∈V K ρ .
(ii) The computation of Theorem B.3 applies in a similar fashion: substitutingh=gk,
(Mψρ,a,s)(gK) =
Z
G
C(g −1h)ψ ρ,a,s(hK)dh= p dρ h ρ(g) bC(ρ)u (s) ρ i a .
Sinceu (s) ρ ∈V K ρ and bC(ρ)agrees withB ρ onV K ρ (asP Ku(s) ρ =u (s) ρ andP K bC(ρ) = bC(ρ)by
bi-K-invariance),
bC(ρ)u (s) ρ =B ρ u(s) ρ =λ (s) ρ u(s) ρ ,
henceMψ ρ,a,s =λ (s) ρ ψρ,a,s.
(iii) Orthonormality: under the identification ofL 2(X)with the right-K-invariant functions in
L2(G), the inner products may be computed onG, where Schur orthogonality gives
⟨ψρ,a,s, ψσ,c,t⟩L2(X) =⟨ψ ρ,a,s, ψσ,c,t⟩L2(G) =δ ρσ δac ⟨u(t) ρ , u(s) ρ ⟩Vρ =δ ρσ δac δst.
Completeness: by (17), theρ-isotypic component ofL 2(X)has dimensiond ρ mρ. The functions
{ψρ,a,s : 1≤a≤d ρ,1≤s≤m ρ}ared ρmρ orthonormal elements of this component and
therefore span it. Taking the union overρ∈ bGgives completeness.
(iv) This result follows directly from (i)-(iii). We note that the trivial irrep is dropped due to centering
as usual.
Note that our discussion of realification as in Appendix B.5 applies largely unchanged for homoge-
neous spaces, just as for the compact group case.
21

Preprint. Under review.
D.3 GELFAND PAIRS
Definition D.2.(G, K)for compactGis aGelfand pairifm ρ = dimV K ρ ≤1for everyρ∈ bG,
i.e. the decomposition (17) ismultiplicity-free.
Corollary D.3(Diagonalization; Gelfand pair).Assume(G, K)is a Gelfand pair withm p =
dimV K ρ ≤1for everyρ∈ bG. Theorem D.1 can be simplified. For eachρwithm ρ = 1, fix a
unitu ρ ∈V K ρ . ThenB ρ becomes the1×1scalar
λρ =
Z
G
C(g)φ ρ(g)dg, φ ρ(g) :=⟨ρ(g)u ρ, uρ⟩.
The spectrum ofMis the scalar sequence{λ ρ}, each with eigenspace of dimension at leasetd ρ,
spanned byψ ρ,a(gK) = p dρ [ρ(g)uρ]a. The functionsφ ρ are often denoted as spherical functions.
Proof.SincedimV K ρ = 1, the restriction ofB ρ toV K ρ =Cu ρ is multiplication by the scalar
λρ =⟨B ρuρ, uρ⟩. AsP Kuρ =u ρ andP K is self-adjoint,⟨B ρuρ, uρ⟩=⟨ bC(ρ)u ρ, uρ⟩. Hence,
λρ =
Z
G
C(g)⟨ρ(g)u ρ, uρ⟩dg=
Z
G
C(g)φ ρ(g)dg
D.4 SPECIALCASE: THE SPHERE
We consider the particular case of the sphere which is relevant to our experiments. TakeG=SO(3),
K=SO(2),X=G/K=S 2. We state 3 well known facts about the sphere (Dai & Xu, 2013).
(1) The irreps ofSO(3):ρ ℓ ℓ≥0, are real and have dimension 2ℓ+ 1, each withdimV K ρℓ = 1.
Hence,(SO(3), SO(2))is a Gelfand pair.
(2)L 2 functions on the sphere have the isotypic decompositionL2(S2) = L ℓ Hℓ, whereH ℓ are the degree-ℓspherical harmonics. Alternatively, for eachℓ≥0, let
Ψℓ := span

ψρℓ,a : 1≤a≤2ℓ+ 1 	 ⊂L 2(S2)
span of the modes of Corollary D.3 for the irrepρ ℓ. We must have thatH ℓ = Ψℓ as they correspond
to the same isotypic component. Hence, instead of usingψ ρ,a(gK)as our orthonormal basis, we
can instead use the real degreeℓspherical harmonics{Y m ℓ }ℓ≥0,|m|≤ℓ.
(3) The spherical functions in Corollary D.3 become Legendre polynomials,φ ρℓ (g) =P ℓ(cosθ g)
wherecosθ g =⟨gx 0, x0⟩,x 0 =eK∈S 2. The inner product is done with respect to the points on
the sphere realized inR 3.
Finally, note that the kernelκ(x, y)onS 2 is invariant underG=SO(3)iffκ(x, y) =c(⟨x, y⟩),
i.e., the kernel is only some functioncof the inner product between two points. Therefore, recall
that our alternative form of the kernelCobeysC(g) =κ(eK, gK). HenceC(g) =c(⟨x 0, gK⟩) =
c(cosθ g). Altogether, applying Corollary D.3 gives us that
MY=λ ℓY∀Y∈ H ℓ
whereλ ℓ is given by
λℓ =
Z
G
C(g)φ ρ(g)dg=
Z
G
c(cosθ g)Pℓ(cosθ g)dg=
1
4π
Z 2π
0
Z π
0
c(cosθ)P ℓ(cosθ) sinθ dθ dϕ=1 2 Z 1 −1 c(t)Pℓ(t)dt
and eachλ ℓ has multiplicity as least2ℓ+ 1. (Centering, i.e. consideringPMP, will setλ 0 = 0)
22

Preprint. Under review.
E MONTHS:EXPERIMENTAL DETAILS
Corpus.text8(Mahoney, 2011): the first10 8 bytes of cleaned English Wikipedia (17,005,207
whitespace tokens; lowercase, punctuation stripped, digits spelled out). Counts of2,771–3,650per
month after filtering “may” (see below). Using this corpus, we form the normalized co-occurrence
matrixM ⋆ ∈R 12×12 as in equation 5 (settings areB= 16,f(δ) =B+1−δ). We factorize
M ⋆ to form our empirical word embeddings (centering removes the constant mode). Visually, The
leading PCs are circular: PCs1–2are thek=1circle (λ= 2.17,1.59), while PCs3–4arek=2circle
(0.88,0.76).
Sense disambiguation for “may”.Raw counts:19,115for “may”,∼6×the other months, domi-
nated by the verb, which inflates the unigramP x in Eq. 1. Fortunately, we can roughly select cases
where “may” is used as a month. Namely, we keep an occurrence of “may” iff its two following
tokens are both digits, or its preceding token is a digit, or an adjacent token is another month. This
retains3,129occurrences (16.4%), in line with the other months. This improves our per-month
cosine prediction from0.90to0.96.
Wavenumber assignment/purity (the coloring of Figure 2 A).Define the vectorsc k :=
cos(2πkt/12)
11
t=0 ands k :=

sin(2πkt/12)
11
t=0 inR 12, and letF k := span{c k, sk}be the “Fourier plane” of wavenumberk= 1, . . . ,5(fork= 6, the one-dimensional span of the alternating
vectorc 6). DenoteP k as the orthogonal projector ontoF k. These subspaces orthogonally decom-
pose the centered space, so for any unit eigenvectorvofP M⋆Pthe “energies”∥P kv∥2 sum to1over
k= 1, . . . ,6. We assignvthe wavenumber capturing the most energy,k∗(v) = arg maxk∥Pkv∥2,
and call the winning energy itspurity.∥P k∗ v∥2 ∈[0,1]:1is perfectly in one of these subspaces,
while a uniformly random unit direction scores2/12≈0.17in expectation (1/12fork= 6).
Leading-mode purities:0.99,0.86(k=1pair) and0.92,0.88(k=2pair).
Corpus Bootstrap (errors bars of Figure 2 A).The corpus is divided into40contiguous seg-
ments (∼425k tokens each). A resample draws 40 of these segmentswith replacement, forming
a newM ⋆ from which new eigenvalues can be computed.300resamples give percentile (2.5%–
97.5%) intervals.
Theory vs. Empirical (Figure 2 C).Our theoretical predictions take the form as in Appendix
B.6, usingM ⋆ to estimate the kernelC(by averaging over appropriate elements). We align our
predictions to each empirical plane with by solving an orthogonal Procrustes problem. The first
PCs align with our theoretical predictions at a per month cosine of0.96(median0.97). A month
label-shuffle null has mean per-month cosine of0.35(95% 0.53) across 500 shuffles.
F MUSIC:EXPERIMENTAL DETAILS
Corpus and chord extraction.All371Bach chorales from themusic21corpus (Cuthbert &
Ariza, 2010). Scores are “chordified” into beat-level sonorities. Each sonority is reduced to its pitch-
class set and matched against the24major/minor triads (inversions and octave doublings identified;
sevenths and other sonorities retained as their own types). This yields24,374chord tokens over a
vocabulary of92types, of which the24triads (78%of tokens) are the subsystem under considera-
tion. We form ourM ⋆ ∈R 24×24 from this corpus as in equation 5 (settings areB= 3,f(δ) = 1,
α= 0.5).
Accessing quality of statistical hypotheses.Suppose we have a groupG ′ (which acts on the
24 triads) under which we suspect thatM ⋆ could be approximately statistically invariant. We can
score how well this hypothesis holds by first constructing the projection ofM ⋆ onto matrices that
are exactly statistically invariant,Π G′M ⋆ x,y = 1 |G′| P g∈G′ M ⋆ gx, gy, setting matrix elements which
would be equal to their average. In general, a hypothesis need not be a group; it must only specify
which elements ofM ⋆ would be equal in an ideal situation. We then compute our score
R2 =
P
c nc

M ⋆c − M ⋆2
P
x,y

M ⋆xy − M ⋆2 ,
23

Preprint. Under review.
A1 A2 B1 B2 E1 E2 E3 E4 E5
0.0
0.2
0.4
0.6
0.8
1.0isotypic energy
chance d2 ρ /24
plane 1 (λ = 19.1, 15.9)
plane 2 (λ = 7.8, 6.3)
plane 3 (λ = 3.7, 3.4)
Figure 6: Irrep content of the top three embedding planes: we consider the first six modes of the cen-
teredM ⋆. One-dimensional irreps areA 1, A2, B1, B2 and two-dimensional irreps areE 1, . . . E5.
A1 corresponds to the trivial irrep which centering automatically removes. We compute the iso-
typic energy of each plane for each irrep. One irrep dominates per plane (E 5, E2, E3; energies
0.958,0.873,0.662vs. chance1/6). Eigenvalues of centeredM ⋆ are listed in legend; notice they
approximately pair.
E5 E4 E3 E2 E1 B2 B1 A2
1
2
3
4
5 empirical mode
0.80 0.03 0.05 0.08 0.01 0.00 0.00 0.03
0.78 0.02 0.01 0.09 0.02 0.00 0.00 0.06
0.01 0.25 0.12 0.15 0.02 0.05 0.00 0.40
0.01 0.49 0.10 0.35 0.01 0.02 0.00 0.02
0.01 0.49 0.12 0.03 0.02 0.11 0.01 0.21
0.0
0.2
0.4
0.6
0.8
1.0
isotypic energy
Figure 7: Irrep content of ChordBERT layer 3 PCs: one-dimensional irreps areB 1, B2, A2, and
two-dimensional irreps areE 1, E2, E3, E4, E5. We do not show the remaining trivial irrepA 1 as it
is removed automatically from centering. The first 2 PCs demonstrate high isotypic energy inE 5.
wherecruns over the equivalence classes of pairs under the candidate invariance,n c is the number
of entries in classc, M ⋆c is the class mean of equivalence classc, and M ⋆ is the grand mean over
all entries. In other words, this is the fraction of the entry-wise variance ofM ⋆ explained by the
class-wide averaging.
TheT /Igroup obtains anR 2 of0.822. An illustration of its performance is shown in Figure 3 A.
None of2000random relabeling of the chords are able to surpass this value. TheZ 12 hypothesis,
which is the same asT /Ibut with only transposition-invariance, scores barely higher at0.830. It
is impossible forT /Ito surpassZ 12 as it has additional restrictions, yet it performs essentially the
same. This is strong evidence that theT /Isymmetry is valid. Other hypotheses, as defined in
Table1score notably worse (Z 24:0.699,P LR:0.442,Z 12 ×Z 12 : 0.440, latentZ 12 : 0.632,
T /Iconjugacy classes:0.435). Notably theT /Iconjugacy class hypothesis, which adds even more
restrictions to theT /Ihypothesis, scores much worse, suggesting thatT /Iis the sharpest symmetry
that is reliably present in the data.
24

Preprint. Under review.
Isotypic energy.TheT /Iaction on the24triads is a permutation representationL(g)∈R 24×24
(the regular representation acting onC 24). By the canonical Peter–Weyl decomposition of the regu-
lar representation,C 24 ∼= L ρ V ⊕dρ ρ : every irrep appears, with multiplicity equal to its dimension. In
other words, the spaceC 24 can be canonically decomposed into “isotypic” subspaces corresponding
to each given irrep ofT /I. The orthogonal projector onto theρ-component is given by
Pρ = dρ 24 X g∈T /I χρ(g)L(g).
See Serre (1977) for more details on orthogonal projectors onto isotypic components. ForT /I
acting on triads, the two-dimensional irrepsE h,h∈[5], each have isotypic dimensiond 2 ρ = 4.
Theisotypic energyof an empirical plane (defined by orthonormalv 1,v 2) in irrepρis defined as 1
2 (∥Pρv1∥2 +∥P ρv2∥2)∈[0,1]with chance level for a random planed 2 ρ/24(1/24 and 1/6 for one and two-dimensional irreps respectively). Note that the isotypic energy is invariant to the choice of
v1,v 2. For computing the isotypic energy of a single vectorv, we compute∥P ρv∥2 ∈[0,1]instead.
See Figure 6 and Figure 7 for the isotypic energies corresponding to Bach chorales and ChordBERT
layer 3 respectively.
ChordBERT activationsWe input the 371 Bach Chorales separately into ChordBERT (He et al.
(2026)) and in layer 3’s residual stream average the activations corresponding to each of the 24 triads
over every single one of its occurrences. We focus on layer 3 in particular as its first 2 modes have
very high isotypic energy in irrepE5 (Figure 7), suggesting the potential presence of a circle of fifths
(which does indeed emerge, Figure 3 B).
Theory vs. Empirical (Figure 4 B)For the left subplot we use theM ⋆ formed from the 371 Bach
chorales to form empirical embeddings. On the right, we instead consider the averaged embeddings
per triad in layer 3 of ChordBERT, as discussed above. In place ofM⋆ we consider the Gram matrix
across the centered embeddings (∈R 24×24), normalized by the root mean square of its diagonal.
Our theoretical predictions take the form as in AppendixB.6in both subplots, with the kernelC
being estimated fromM ⋆ or the Gram matrix respectively (by averaging over appropriate elements).
A fitting orthogonal transformation aligns the theoretical predictions with the empirical embeddings
in both cases. The per-chord cosine is0.98(median0.99)for the chorales and0.91(median0.95)
for ChordBERT. A chord relabeling null with 500 permutations gives0.40(95% 0.56) and0.29
(95% 0.48) respectively in each case.
Furthermore, recall from Figure 6 that the first three planes of the Bach chorale embeddings all
have high isotypic energy in their respective 2D irreps. This suggests comparing our theoretical
predictions against the first 6 dimensions of the empirical embeddings fromM ⋆, using one fitting
orthogonal transformation per plane. We obtain a per-chord cosine similarity of0.95(median0.96)
overall with per-plane values of0.98,0.94, and0.80, respectively. Our theory certainly holds pre-
dictive power beyond the first 2 dimensions, but weakens as we look as less prevalent modes.
Model comparison protocol.Chorales are split into disjoint halves (10random splits). Each
hypothesis is fit on the training half. Namely, the empiricalM ⋆ is projected onto a matrix which
satisfies the hypothesisG ′, i.e.,Π ′ GM ⋆ as defined above (the RAW model uses the trainingM⋆ itself
without projection).Π
′
GM ⋆ then predicts theheld-outhalf’s embeddings. Namely, the first 6 modes
of the centeredM ⋆ (of the held out data) are aligned with the modes ofΠ G′ M ⋆ (from the training
data) using one orthogonal transform per plane. Per-chord cosines are then computed. Results
for various hypotheses (Table 1) are shown in Figure 8 A. The data itself without any imposed
invariances,“RAW”, performs the best by a small margin. However,Z 12 andT /Idon’t do much
worse. As mentioned before, the fact thatT /Iperforms about as well asZ 12, when it has more
restrictions and less independent parameters, is a great indication thatT /Iis a natural symmetry of
the data. Figure 8 B performs a similar analysis as in A, but instead refits on nested subsets with a
fixed held out test set.T /Iattains a cosine similarity with the held out data of0.892at12chorales,
the best performance of all models at this point; RAW requires around50training chorales to match.
Changing window size for constructingM ⋆.As seen in Figure 9, we constructM ⋆ and consider
the corresponding embeddings for a variety of window sizes. We see that the fitted rotation angle
25

Preprint. Under review.
T/I Z12 Z24 PLR Z12xZ12 latent
Z12
T/I
conj.
class
RAW
0.0
0.2
0.4
0.6
0.8
1.0per-chord cosine similarity
(a) held-out embedding prediction
plane 1
plane 2
plane 3
12 25 50 100 186
# training chorales
0.750
0.775
0.800
0.825
0.850
0.875
0.900
0.925per-chord cosine similarity
(b) data efficiency
T/I Z12 Z24 latent Z12 RAW
Figure 8: (a) Held-out embedding prediction per plane for the eight hypotheses of Table 1: mean
±sample standard deviation over10random splits of the chorales into disjoint training/test halves.
(b) Data efficiency: Training sets are nested subsets drawn without replacement from one fixed
half of the371chorales, the other half serving as a fixed test set. Each point averages15redraws
(shaded:±1sample standard deviation), except the rightmost, where the training set is the entire
pool and no redraw is possible. The19-parameterT /Ihypothesis converges by∼12chorales. The
300-parameter unconstrained model (RAW) needs≈4×more data to match it.
1 2 3 5 8 16
window size
0
25
50
75
100
125
150
175rotation angle (deg)
(a)
plane 1 plane 2 plane 3
1 2 3 5 8 16
window size
0.0
0.2
0.4
0.6
0.8
1.0isotypic energy
 chance = 1/6
(b)
plane 1 (E5)
plane 2 (E2)
plane 3 (E3)
1 2 3 5 8 16
window size
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0eigenvalues
(c)
mode 1
mode 2
mode 3
mode 4
mode 5
mode 6
Figure 9: We use various window sizes for constructing the centeredM ⋆ (the original size was 3)
which we then use to form 6-dimensional chord embeddings. (a) Rotation angles are computed by
fitting a rotation matrix to each pair of dimensions (plane) of the embeddings; we consider the angle
between chords in chromatic order separately for both the majors and minors. (b) Isotypic energy of
each plane in its respective irrep. Chance level is alwaysd 2 ρ/24 = 1/6for the considered irreps. (c)
eigenvalues of the centeredM ⋆.
and isotypic energy remain largely consistent. Plane 3’s values change somewhat, but this kind of
behavior is understandable in weaker modes of the data. Finally, we also consider the eigenvalues
of the centeredM ⋆ in Figure 9 C. While rotation angle and isotypic energy are largely functions of
the statistical symmetries of the data, the eigenvalues are very dependent on the corpus; corpora that
have the same symmetries can still have wildly different eigenvalues. Hence, it is not too surprising
to see that the eigenvalues have noticeably more drift than the other considered quantities.
G SKY:EXPERIMENTAL DETAILS
LLM activationsReleased data of Berdnikov & Liokumovich (2026):188named sky objects
(stars, constellations, etc.)×25proximity-style prompts, residual-stream activations at all layers
exported as the top-16PCA coordinates per layer. We use mean activations across the prompts for
each layer. The layer from which the true celestial positions can be linearly decoded the best is
selected as the working layer (layer72of89for Mistral Large 2). In place ofM ⋆, we consider
Gram matrix (∈R 188×188) of the sky objects’ activations, normalized by the root mean square of
its diagonal. We will denote this matrix asG Gram for convenience. We will also use 188 andn
interchangeably in this section.
26

Preprint. Under review.
Model Params Indep. Invariance assumed onM ⋆ over the24triads
T /I24 19Statistical invariance underT /I.
Z12 48 26Statistical invariance under only transposition ofT /I.
Z24 24 13Invariance under a “transposition” that moves along both
majors and minors as in the circular order seen in Figure
3 B. This hypothesis predicts embeddings where the major
and minor circles are perfectly inter-spaced.
P LR24 19Statistical invariance under the classicP LRgroup of music
theory
Z12 ×Z 12 26 15Statistical invariance under transposition, but separately for
both majors and minors. (letm, m+ 1, m+ 2be sequen-
tial major chord indices whilen, n+ 1, n+ 2correspond
to minors) E.g.,M ⋆ m,m+1 =M ⋆ m+1,m+2 andM ⋆ n,n+1 =
M ⋆ n+1,n+2 but in general we haveM ⋆ m,m+1 ̸=M ⋆ n+1,n+2)
Major and minor cross terms ofM ⋆ are set to one con-
stant. This hypothesis essentially assumes independent cir-
cular structures in majors and minors.
latentZ 12 12 7Majors are identified with their relative minors (music the-
ory term, this identification looked reasonable from Figure
3 B), and invariance under transposition is assumed. This
hypothesis corresponds to the embeddings forming a single
circle with majors on top of minors.
T /Iconjugacy class9 9We begin with statistical invariance underT /I. Each equiv-
alence class corresponds to a group element. We add the
restriction that if two or more of these group elements corre-
spond to the same conjugacy class ofT /I(different type of
class, group theoretic concept), then the equivalence classes
are combined.
RAW576 300No invariance, the raw matrix
Table 1: The eight statistical hypotheses of the music model comparison. Each hypothesis is applied
toM ⋆ by setting elements ofM ⋆ which would be equal under the hypothesis to their average (Ex-
cept RAW which isM ⋆ itself).Paramscounts the model’s number of equivalence classes without
considering the symmetry ofM ⋆.Indep.counts the number of free parameters once this symmetry
merges equivalence classes together.
Need for weighted estimators.Our theory in AppendixDintrinsically assumes a continuous
setting in which an infinite set of words are in bijection with the sphere. Of course, this is not
practical. In reality, we are discretizing the theory by sampling points onS 2 which correspond to
sky objects on the celestial sphere. If all celestial objects were sampled uniformly on the sphere,
no weighted estimators would be required. However, the celestial objects we consider sample the
sphere in a “lightly” non-uniform fashion. Acceptable estimators could still be obtained by ignoring
this small bias, but we decide to be proactive in counteracting it.
Inverse density weightingEssentially all estimators in this section incorporate inverse density-
weighted. We fit a densityˆρto our188objects using an on-sphere Gaussian kernel density estimator
(KDE). Namely, letx 1, . . . , xn ∈S 2 be the sky-object positions andθ ij = arccos(⟨x i, xj⟩)the
great-circle angle. Withh= 0.35rad, the on-sphere Gaussian KDE is
ˆρ(xi) =
nX
j=1
exp

− θ2 ij
2h2
!
.
A weightw i is now associated with each objecti. These weights inversely related toˆρ, and are
renormalized to sum to 1:
˜wi = 1 ˆρ(xi) , w i = ˜wiPn k=1 ˜wk .
Hence, areas of the sphere which were previously over or under-sampled are counterbalanced.
Empirical Word EmbeddingsThe integral operator in Appendix D on somef∈L 2(S)dis-
cretizes as(Mf)≈ P j M ⋆ ijf(x j), where the typical normalized co-occurence matrixM ⋆ emerges.
27

Preprint. Under review.
However, with reweighting, this is lightly modified toP j M ⋆ ijwjf(x j). Something else affected by
reweighting is centering. The previousP=I−11 T /nis modified toP w =I−1w T .
Altogether, for computing empirical embeddings, using say theM ⋆ from our book corpus, we solve
generalized eigenproblem
PwM ⋆W Pwv=λv(18)
with diagonalW∈R 188×188 andW ii =w i.
RegressionsAll regressions in this section incorporate reweighting.
(i) Kernel estimation(LLMs would useG Gram in place of the book corpus’sM ⋆) The kernelC(as
in Theorem 4.2) is the weighted estimate ofE[M ⋆ |t],
˜C(t) =
P
i<j wiwj Kh(t−t ij)M ⋆ ijP
i<j wiwj Kh(t−t ij) , t ij =⟨x i, xj⟩,
wheret i,j is the true cosine between two objectsx i,x j on the celestial sphere.K h is a 1D Gaussian
with standard deviationh= 0.08. Note, the kernel as described here is a function of cosine similarity
while in the main paper it is a function of angle. The two forms are interchangeable.
The local standard deviation of this fit is computed as follows. Let
κij(t) =w iwj Kh(t−t ij)
For convenience, write
ˆm1(t) = ˜C(t),ˆm 2(t) =
P
i<j κij(t) (M⋆ ij)2 P
i<j κij(t) .
The local standard deviation of the kernel fit is then
ˆσ(t) =
q
max

ˆm2(t)−ˆm1(t)2,0  ,
i.e. the estimate of
q
Var(M⋆ ij |t ij =t).
(ii) Decoding: Consider the unit vectorsx i ∈R 3 representing thencelestial objects. Suppose we
are trying to linearly decode these positions from someU∈R n×k, e.g., the residual stream of any
of the LLMs. Let ˆB= arg min B P i wi∥xi −B ⊤Ui∥2 whereB∈R k×3 andU i ∈R k. We report
the quality of the fit of ˆBas
R2 dec = 1−
Pn
i=1 wi∥xi − ˆB⊤Ui∥2 Pn
i=1 wi∥xi −¯xw∥2 ,
where xw =
Pn
i=1 wixiPn
i=1 wi . This metric chooses the working layer of each model whereUbecome the centered activations of each given LLM (Table 1).
(iii) Gram zonality:(books would useM ⋆ in place ofG Gram in this section). Writet ij =⟨x i, xj⟩
andθ ij = arccos(t ij). Using only upper-triangle pairsi < jwith weightsω ij =w iwj, partition
θ∈[0, π]intoB= 18equal bins. In binbset
ˆµb =
P
(i,j)∈b ωij Mij P
(i,j)∈b ωij
With ˆMij = ˆµb(ij) and ¯M= P i<j ωijMij  P i<j ωij,
R2 zonal = 1−
P
i<j ωij(Mij − ˆMij)2 P
i<j ωij(Mij − ¯M) 2 .
A permutation null (shuffle object labels, keep{Mij}, refit the bin means) supplies a chance baseline
forR 2 zonal.
28

Preprint. Under review.
Model layerR 2 zonal R2 dec canon2 (top-3) degree sequence
Qwen3-235B 90 0.581 0.928 0.941 1 1 1 2 2 2 2 2
Mistral-Large-123B 72 0.490 0.905 0.911 1 1 1 2 2 2 2 3
GLM-4.5-Air 46 0.484 0.904 0.911 1 1 1 2 2 2 2 2
Qwen3-32B 62 0.440 0.865 0.871 1 1 2 1 2 2 2 3
Llama-3.3-70B 63 0.395 0.898 0.911 1 1 2 1 2 2 3 3
Mixtral-8x22B 56 0.238 0.836 0.84 1 1 1 2 1 2 2 4
GPT-OSS-120B 31 0.072 0.634 0.64 scrambled
Table 2: Mistral-Large-123B is the same as Mistral Large 2. Each model is evaluated at the layer
where celestial positions on the sphere (∈R 3) can be linearly decoded best from the activations
(R2 dec).R 2 zonal: the fraction of the activation Gram matrix structure explained by true angular sepa-
ration alone. Canon2 (top-3): average squared canonical cosines between the three leading activation
modes and the dipole harmonics (subspace overlap;1= identical). Degree sequence: the harmonic
degree (ℓ) of each successive eigenmode—a clean harmonic embedding reads1 1 1 2 2 2 2 2 3. . .
Five of seven models show strongly harmonic structure (relatively high zonalityR 2 with degree-
ordered modes). Mixtral-8x22B is borderline, and GPT-OSS-120B is the true outlier, with weak
spherical harmonic structure by every measure.
Sampling Spherical HarmonicsSampled real spherical harmonics(Y m ℓ (xi))n i=1 are only ap-
proximately orthonormal at finiteN. We orthonormalize them with Gram-Schmidt in the weighted
inner product⟨·,·⟩ w (⟨u, v⟩w = Pn i=1 wiuivj whereu, v∈R n.) We conduct this degree by degree, beginning withℓ= 1and moving upwards (ending for whatever degree is high enough for our pur-
poses). This yields a matrixQ ℓ ∈R n×(2ℓ+1) for eachℓ, whose columns are an orthonormal basis
of the sampled degree-ℓsubspace, withQ ⊤ ℓ Qℓ′ = 0forℓ̸=ℓ ′ by construction. TheseQ ℓ are the
orthonormalized spherical harmonics we show as our theoretical predictions in Figure 4 C.
Degree energies (Figure 4 B):Consider a unit eigenvectorvof the weighted eigenproblem in equa-
tion 18. The “degree-ℓ” energy ofv,E ℓ(v), is the squared orthogonal projection onto that subspace,
Eℓ(v) =∥Q ⊤ ℓ v∥2 =
ℓX
m=−ℓ
⟨qℓm, v⟩2 ∈[0,1],
computed forℓ= 0, . . . ,4. The vector’s assigned degree isℓ∗(˜u) = arg maxℓ Eℓ(˜u), and itspurity
in that degree isE ℓ∗ (˜u). This is the color bar of 4 B. Note that the considered degrees in this figure
consider P ℓ≤4(2ℓ+1) = 25of then= 188dimensions, so energies need not sum to1. The chance
energy level for a random direction is(2ℓ+1)/n(≈0.016/0.027forℓ= 1,2), so purities of0.5–0.9
sit two orders of magnitude above chance. Finally, note thatE 0(˜u) = 0exactly due to centering.
Selection of Star-Guide CorpusCandidate pool:24public-domain astronomy books (Project
Gutenberg,∼1.6M words). Not every astronomy book carries the sky’s geometry in its statistics.
Many are organized by mythology, best telescope practices, or by a handful of famous constellations.
A minority are written as a generaltour of the sky, directing the reader from object to nearby object
with co-mentions largely determined by geometrical positions. The metric below selects for this
property.
Tokenization maps every object alias to a canonical token. Each book’sM ⋆ (equation 5,B=
30, f(δ) = 1, α= 0.25) is formed using objects with≥5mentions (fallback3, marked†in
Table 3). Consider the normalized co-occurence rateR ij = Pij PiPj as in equation 7; this counts how
much more or less often a pair of objectsiandjco-occur relative to how much their individual
prevalences would predict. We would ideally select books where pairs of objects have highR ij
if they are geometrically close and vis-versa. Furthermore, recall thatM ⋆ ij is a strictly increasing
function ofR ij while also being bounded, which prevents any issues withR ij’s heavy tail.
This line of reasoning leads us to select our books by
D= corr

M ⋆ ij,cosθ ij  over unordered pairs,p <0.05
withpcoming from a one-sided location-permutation null (500 trials).θ i,j is the true angle between
two astronomical objectsiandjon the celestial sphere. Passing books areA Field Book of the
29

Preprint. Under review.
Book Author, year ment.D(p) coher. (z)λ 1 (p) kernel corr
Round the Year with the StarsOlcott, 1912 361+0.45 (0.00)30 (8.8) +1.98 (0.00) +0.86
A Field Book of the StarsOlcott, 1907 345+0.34 (0.00)46 (14.3) +1.69 (0.00) +0.85
Astronomy for Young AustraliansBonwick, 1866 116+0.26 (0.01) † 46 (9.6) +1.16 (0.01) +0.74 †
Astronomy with an Opera-GlassServiss, 1888 364+0.22 (0.00)33 (7.4) +0.86 (0.03) +0.75
Half-Hours with the Telescope Proctor, 1868 101 +0.14 (0.15) † 25 (3.5) +0.34 (0.08) +0.50 †
Recreations in Astronomy Warren, 1879 158 +0.11 (0.12) † 18 (3.8) +0.19 (0.17) +0.61 †
Astronomy for Amateurs Flammarion, 1904 136 +0.02 (0.38) † 25 (4.2)−0.03 (0.50) +0.11 †
Pleasures of the Telescope Serviss, 1901 156 +0.01 (0.45) † 21 (2.6) +0.01 (0.51)−0.12 †
Astronomy for Young Folks Lewis, 1922 301−0.08 (0.83) 26 (8.2)−0.21 (0.72)−0.21
text8(general Wikipedia, 17M tok) –, – 792+0.01(.48) 79 (4.6)+0.00(.53)+0.18
Table 3: Corpus selection (leading 9 candidates of24).Selection columnD= corr(M ⋆,cosθ)
with one-sided object celestial sphere location-permutationp; boldface: selected atp <0.05with
500 shuffles. Coherence is the median angular hop between successive distinct mentions in degrees.
z= ( ¯m null −m obs)/σnull is the hop’s deficit below the object textual position order-shuffled null
(500 shuffles), with¯mnull andσ null, the mean and standard deviation of the median hop across all
shuffles.λ 1 is the empiricalc 1 from Theorem 4.2 using the book’s kernel; 500 shuffles with object
celestial sphere location-permutation are used to computep. Kernel corr is the correlation with the
LLM activation kernel. All listed books contain≥15well-counted (≥5mentions, †: fall back of 3
mentions) objects.
Stars(Olcott 1907;D= +0.34,p < .004),Round the Year with the Stars(Olcott 1912;+0.45,
p < .004),Astronomy with an Opera-Glass(Serviss 1888;+0.22,p=.01),Astronomy for Young
Australians(Bonwick 1866;+0.26,p=.01). In total we obtain131k tokens of star guide prose
with39sufficiently counted objects. Notably, the selected 4-book corpus kernel correlates with the
model’s activation kernel at0.95, so they have similar structure.
Simpler statistics fail in instructive ways: narrativecoherence(median angular hop between succes-
sive distinct mentions vs. a shuffled null, Table 3) completely ignores whether successive mentions
actually fall within ourM ⋆’s window. Alternatively, a metric completely based on co-occurrences
within the window, something like the meancosθof all co-mentions in the same window, also typi-
cally fails. These metrics are often confounded by jointly famous pairs (e.g. Castor–Pollux) that are
often mentioned together, but ignores all the geometrically close pairs that are never mentioned.D
avoids these problems by working withM ⋆ and considering all pairs.
A caught negative shows the metric working:Astronomy for Young Folks(monthly chapters revis-
iting the same famous celestial objects) is strongly coherent (z= 8.1) yet fails on our selection
metric (D=−0.08,p= 0.83). Similarly, a large generic corpus will generally not perform well at
this metric. For example,text8(17M tokens of cleaned Wikipedia,130×the size of the selected
guides) demonstrably does not. ItsD= +0.01(p= 0.48) and coherencez= 4.6and are both
far behind the selected corpus (Table 3).text8is dominated by celestial terms with alternative
meanings (algol, peacock, mimosa, etc.). Any signal it does possess seems to arise from jointly
famous pairs of celestial objects, a confounding thatDremoves as discussed before.
Theory vs. Empirical (Figure 4 C).We compare the centered Mistral Large 2 activations and the
modes of the book corpus’s centeredM ⋆ with the dipole (degree 1) spherical harmonics evaluated
at the object’s true positions. Note that spherical harmonics as orthonormalized as in the Sampling
Spherical Harmonics paragraph above. We will utilize the sameQ ℓ.
Subspace alignment:There are2ℓ+ 1spherical harmonics of degreeℓ, but the number of modes of
the LLM activations with high degreeℓpurity often exceed2ℓ+ 1(Figure 4 B). Hence, for com-
paring our theoretical predictions with the empirical LLM activations, we first find the “best aligned
subspace” (within some span of PC modes) in the activations with our theoretical predictions. For
the dipole (ℓ=1) alignment, we use PCs 1-4, while for quadrupole (ℓ= 2) alignment, we instead
use PCs 5-12.
The actual alignment for degreeℓis conducted with canonical angles. LetU∈R n×k have columns
of PCA modes under consideration, wherek≥2ℓ+ 1. Let the singular value decomposition (SVD)
30

Preprint. Under review.
ofQ T ℓ Utake the usual form ofQ T ℓ U= ΦΣΨ T , whereΦ∈R (2ℓ+1)×(2ℓ+1),Σ∈R (2ℓ+1)×k, and
Ψ∈R k×k. Our best aligned subspace is thenUΨ :,1:2ℓ+1; this becomes our empirical data.
Note that this procedure is not conducted for the book corpus. We directly consider itsM ⋆ modes
1-3 for dipole and 4-8 for quadrupole.
Point by point alignment:After any potential subspace alignment, we solve an orthogonal Procrustes
problem to align our theoretical predictions point wise with the empirical data for either the LLMs
or the books. A global scaling is also fit for the LLMs, but not for the books. For the books, we
utilize our theoretically predicted scaling as in Theorem 4.2.
Objection permutation null:Our null in Figure 4 (and for the quadrupole case) consists of randomly
assigning objects to different positions and performing the exact same analysis. We utilize 300
permutations.
Size effect on books worse performance (Figure 5).We take the fitted zonal kernel to the books
( ˜Cin Regressions (i) section above) as ground truth and generate synthetic corpora that differ from
the real one only in being exactly zonal. Concretely, for each pair the kernel value is converted back
to count units by the following (cf. App. A for all definitions):
Rfit ij = 2 + ˜C(t ij) 2− ˜C(t ij) ,rate ij =n inj 2F N ×R fit ij .
Off-diagonal counts are drawn asW ij ∼Poisson(m·rate ij)at multipliersm∈
{0.25,0.5,1,2,4,8,16,32,128}(token count scaled fromNtomN) and are used to generate a
newM ⋆. Each draw is then scored by the same pipeline as the observed corpus: per-object co-
sine is found for the top 3 modes of the centeredM ⋆ after an aligning orthogonal transform.1000
draws per multiplier are used. Notably, one asymmetry is forced: a simulated draw has no measured
diagonal (pair counts are drawn off-diagonal only), so its diagonal is set to the refit ˜C(1).
The observed value sits at the∼93rd percentile of the matched simulations atm= 1(star in Fig-
ure 5; band at1×:[0.27,0.56], observed0.55), and the curve rises monotonically toward1, passing
the level of the model’s per object cosine sim. between32×and64×the corpus’s counts. Hence,
we can say that the “effective corpus size” of the LLM is roughly in this range. It is plausible that
the model could have easily consumed this amount of stargazing material during its training.
H REPRODUCIBILITY
Code for all experiments is available athttps://github.com/liamstoran01/group_
invariant_statistics.git.
I AI USESTATEMENT
In this work, we used generative AI tools for formulating mathematical claims, providing critical
ingredients for proving mathematical claims, implementing methods in code, assisting the writing
of proofs, refining hypotheses, providing feedback on computational experiments, and interpreting
results. We have not used generative AI tools for generating synthetic data sets, helping develop
theoretical models or conceptual frameworks, assisting with translation, cleaning and reformatting
a dataset, or supporting qualitative and thematic data analysis. Additionally, we used generative AI
tools for creating code, drafting parts of the paper, analyzing existing literature, proposing keywords
for the paper, and helping to find relevant sources. We have reviewed all AI-assisted work. Any
generated code or mathematics were reviewed and edited for correctness. An independent literature
survey was conducted. We take responsibility for the final content of this work, including text,
claims or artifacts produced with the aid of generative AI.
31
