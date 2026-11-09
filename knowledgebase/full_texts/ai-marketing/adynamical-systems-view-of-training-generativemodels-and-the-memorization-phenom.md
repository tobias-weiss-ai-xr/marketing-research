---
title: Adynamical systems view of training generativemodels and the memorization phenomenon
url: https://arxiv.org/abs/2605.19483
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Siva Athreya
- Chiranjib Bhattacharya
- Vivek S. Borkar
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.19483
pages: 12
chars: 55203
fetched_at: '2026-11-08T13:27:59+00:00'
kb_version: 1
---

# Adynamical systems view of training generativemodels and the memorization phenomenon

A dynamical systems view of training generative models and
the memorization phenomenon
Siva Athreyaa, Chiranjib Bhattacharyab, Vivek S. Borkarc
aInternational Institute for Theoretical Sciences, Survey No. 151, Hesarghatta Road, Shivakote Hobli, Bengaluru 560089, India
bDepartment of Computer Science and Automation, Indian Institute of Science, Bengaluru 560012, India
cDepartment of Electrical Engineering, Indian Institute of Technology Bombay, Powai, Mumbai 400076, India
Abstract
Using recent works of one of the authors (VSB) on collapse in generative models and two time scale dynamics in stochastic
gradient descent in high dimensions, we give a system theoretic explanation of the memorization phenomenon in generative
models. This relies purely on the dynamic aspects of the training phase. Specifically, we use a result of Austin [2016] to
motivate a stylized model for the loss function for stochastic gradient descent (SGD) wherein the loss function has a strong
dependence on some variables and weak dependence on the rest in a precise sense. This naturally leads to two distinct time
scales in the constant step size SGD that is commonly used in machine learning. This fact has been used to explain the double
descent phenomenon in SGD in Borkar [2026]. In conjunction with a mathematical model for collapse phenomenon in SGD
developed in Borkar [2025a], we analyze the constant step size SGD using the recent results of Azizian et al. [2024] in order
to explain the phenomenon ofmemorizationwherein a generative model that is concurrently being tuned yields the same or
similar outputs for significant stretches of time. This gives a novel perspective on the aforementioned phenomena reported in
machine learning literature and their interrelationships, using a dynamical systems viewpoint.
Key words:diffusion models; learning; memorization; two time scales; collapse
1 Introduction
An important issue with generative models such as dif-
fusion models is that of ‘memorization’ in their train-
ing process. This refers to the empirically observed phe-
nomenon whereby it eventually starts regenerating the
same or similar samples as before for a stretch of time.
There is already a considerable body of work about this
topic. For a small sampler, see Baptista et al. [2025],
Buchanan et al. [2025], Chen et al. [2024], Gu et al.
[2023], Hintersdorf et al. [2024], Kim et al. [2025], Pham
et al. [2025], Wang et al. [2024], Wen et al. [2024], Ye
et al. [2025]. The objective of this article is to present
a different take on this problem from a dynamical sys-
tems viewpoint. This essentially means that we shift the
focus to the training algorithm, treating it as a dynami-
cal system. The algorithm in question broadly falls into
the class of ‘stochastic approximation algorithms with
⋆ Corresponding author: V. S. Borkar.
Email addresses:athreya@icts.res.in(Siva Athreya),
chiru@iisc.ac.in(Chiranjib Bhattacharya),
borkar.vs@gmail.com(Vivek S. Borkar).
Markov noise’ Benveniste et al. [1990] (see also Borkar
[2025c], Chapter 8, for updates and a concise overview).
Using this fact and the known theoretical aspects of this
class of algorithms, we look at the phenomenon based on
the temporal evolution of the training scheme. This leads
to significant additional insights that are not apparent in
a static view, which is usually based upon statistical me-
chanics models applied to the loss function landscape. In
particular, we are not interested in the ‘thermodynamic
limit’ of statistical mechanical quantities as the domain
of the loss landscape grows to infinity, in order to char-
acterize critical phenomena. We are more interested in
the asymptotic behaviour of the learning algorithm that
explores this landscape. This explicitly incorporates the
temporal aspects of learning in the analysis and facili-
tates additional insights into the observed phenomena.
This is not to say that this work is the first work to take
a dynamic viewpoint, but it does go deeper into the dy-
namics to give a clean picture of how the phenomenon
of memorization emerges, building upon a related but in
some sense simpler phenomenon, viz., that of ‘collapse’.
We argue that memorization emerges as a collapse-like
Preprint submitted to Automatica 20 May 2026
arXiv:2605.19483v1  [cs.LG]  19 May 2026

phenomenon wherein a diffusion model, being a gener-
ative model, starts collapsing into a fixed output as in
the pure collapse phenomenon, except that it is concur-
rently being modulated by the score learning scheme.
This in conjunction with some other factors render this
phenomenon intermittent. This also leads to some addi-
tional intuition about what specifics of a given problem
can encourage or discourage memorization. This ties
together in a unified manner a variety of phenomena
reported in machine learning.
A broad outline of our results is as folllows:
(1) Based on an important result of Austin [2016] re-
called in section 2.2, we first observe that the prob-
lem structure, specifically the high dimensionality
of the parameter space, naturally leads to multiple
time scales in the learning algorithm. (See equa-
tions (2.11)-(2.12) below.) Two time scale dynam-
ics is well studied in systems and control. This mo-
tivates a stylized multiple time scale model similar
to the one used in Borkar [2026] in order to explain
the temporal double descent phenomenon. Specif-
ically, the stochastic approximation scheme is now
a constant step size two time scale stochastic ap-
proximation with Markov noise. The two temporal
time scales in the training algorithm is an emer-
gent phenomenon here due to the different spatial
scales as observed in Borkar [2025b], and are not
put there ‘by hand’ as in the classical two time
scale stochastic approximation schemes introduced
in Borkar [1997], Borkar [2025b].
(2) We observe that the Markov chain in question
comes from a generative model, which, in the clas-
sical set up, is known to exhibit the phenomenon of
collapse. Using the recent results of Borkar [2025a],
which takes a somewhat different view of collapse,
we explain the role of collapse in the present context
in section 3. This analysis is based on a dynamic
interpretation of the onset of collapse in terms of
an absorbing Markov chain, taken from Borkar
[2025a]. Specifically, a generative model leads to
a probability measure-valued Markov chain that
is absorbing, which is tantamount to saying that
it asymptotically collapses to a Dirac measure
concentrated at a random probability measure.
This will be our formal mathematical definition of
collapse. See Theorem 5 below for a precise formu-
lation.
(3) We briefly recall a rigorous theory for constant step
size stochastic approximation due to Azizian et al.
[2024] in section 4.2. This is in fact grounded in the
theory of stochastic dynamical systems with small
noise as developed in Freidlin and Wentzell [2012],
but with a key difference that is highlighted later.
This leads to a complete picture of the dynamic
behaviour of the generative model tuning scheme,
which includes some surprises as well. We push this
theory a little further in order to give some addi-
tional insights about the asymptotic behaviour of
constant step size SGD using some classical results
of Hwang [1981]. In particular, this sheds light on
the observed preference of flatter minima by the
SGD.
(4) We then link this with the phenomenon of memo-
rization in the context of generative models. This
is a more complex phenomenon than collapse due
to additional dynamical effects that prevent a pure
collapse. What this leads to is an intermittent
collapse-like situation punctuated by regular evo-
lution. The memorization phenomenon reported in
the literature stands for a generative model that is
being trained, going through phases of repeating
itself. We interpret memorization as repeated col-
lapse with model drift on a slower time scale which
renders such repetition intermittent. See Theorem
11 below.
(5) We then explain the role of noise in mitigating or
eliminating the onset of memorization in this frame-
work. This phenomenon has already been observed
in the literature, most notably in Wu et al. [2025],
which we build upon. We explain this in the light
of the theory for constant step size stochastic ap-
proximation Azizian et al. [2024]. This leads to a
complete picture of the dynamic behaviour of the
generative model training scheme, which includes
some surprises as well.
The article is organized as follows. Section 2 summarizes
the key background material required in order to un-
derstand the subsequent developments, split into three
sections. Section 2.1 recalls the standard formalism of
diffusion models. Section 2.2 recalls a theorem of Austin
[2016] that we use in order to motivate our formalism.
Section 2.3, a critical one, recalls the two time scale
stochastic approximation formalism in the context of
stochastic gradient descent (SGD for short). It is criti-
cal because the variant used here goes well beyond the
standard framework thereof from Borkar [1997], Borkar
[2025b] and subsequent works on the topic, in that the
noise structure is much more complex. In fact there are
some subtleties that have been overlooked in this respect
in prior usage of this paradigm, which we underscore.
They cannot be wished away and we opt to make a com-
monly used simplification in order to proceed. The issue
is taken up again in the Appendix where some remedies
from existing literature are highlighted. Section 3 details
a mathematical model of the collapse phenomenon from
Borkar [2025b] which our model of memorization builds
upon.
Section 4 is the core material of this article. Section 4.1
recalls the ‘vanilla’ case of convergent two time scale
SGD with decreasing step sizes, mimicking the treat-
ment of Borkar [2025b]. This is purely as a backdrop for
2

what follows, in order to contrast with decreasing step
size the situation arising in constant step size SGD that
is our focus, and in order to highlight the fact that the
phenomena which we try to explain are some emergent
effects ofconstant step size SGD, not present in the clas-
sical decreasing step size paradigm. As constant step size
has its advantage and is the preferred choice in prac-
tice in the machine learning community, it is important
that we clarify these subtleties. With this backdrop, sec-
tion 4.2 analyzes the effects of constant step size in de-
tail, clarifying and quantifying its asymptotic behaviour,
building upon the important recent contributions of Az-
izian et al. [2024]. Section 4.3 then positions the memo-
rization phenomenon in this context and explains its oc-
currence and non-occurrence in different empirical sce-
narios. As mentioned above, we revisit the subtleties
about SGD with Markov noise of the kind we have and
the difficulties in using the standard paradigms. We also
propose in an Appendix as a remedy two schemes from
literature that use a single function evaluation and ana-
lyze one of them in detail to illustrate the issue.
Two main takeaways from this exercise that go beyond
the specific technical contributions would be, first, high-
lighting the role of constant step size in the observed
phenomena in SGD, and two, the subtleties of Markov
noise and its algorithmic implications.
2 T echnical preliminaries
This section is devoted to recalling the technical back-
ground for our main results. This is split into two
distinct sub-sections. We begin with the simplest clas-
sical formulation of diffusion models as our underlying
template for a tunable generative model in sub-section
2.1. The next sub-section recalls an important result
of Austin [2016] that motivates our basic formulation,
which we describe in sub-section 2.3. We follow this in
sub-section 2.4 with a short intuitive tutorial on two
time scale stochastic approximation with the so called
Markov noise. We only state the variant relevant for our
purposes, viz., stochastic gradient descent, in order to
not cloud the main results with excessive technicalities.
Notation:Recall that a Polish spaceSis a Hausdorff
topological space that is separable (i.e., has a count-
able dense set) and admits a compatible complete met-
ric (i.e., it has a metricd:S×S→Rsatisfying: 1.
xn →x ∞ inSif and only ifd(x n, x∞)→0, and, 2.
ifd(x n, xm)→0 asm, n→ ∞, then there exists an
x∞ ∈Ssuch thatx n →x ∞. The uniqueness of this limit
is easy to prove.) LetCb(S) denote the space of bounded
continuous functionsS→R. Likewise,C([0, T];R d)
will denote the Banach space of continuous functions
[0, T]→R d with the maximum norm. We shall denote
byP(S) the space of probability measures onSwith
the coarsest topology that renders continuous the maps
µ∈ P(S)7→µ(f) :=
R
f dµ∈Rfor allf∈C b(S).
This space is Polish with one choice of a complete met-
ric being the Prohorov metric (Billingsley [1968]). Polish
spaces turns out to be the correct level of generality for
most applications of probability theory because most of
the standard theory of convergence of probability mea-
sures (among other things) extends to Polish spaces and
not beyond. Also, Polish spaces include most function
spaces of importance in stochastic processes, and even
more importantly, because Polish spaces of probability
measures on Polish spaces are Polish, a blessing prob-
abilists appreciate only too well. For a Polish spaceS,
the law of anS-valued random variableX(say) will be
denoted byL(X)∈ P(S).
We use the abbreviation ‘ODE’ for ‘Ordinary Differ-
ential equations’. Also, by ‘a.s.’, an abbreviation for
‘almost surely’, we mean ‘with probability 1’, following
the standard usage in probability theory.
2.1 Diffusion models
We describe here the classical diffusion model Song et al.
[2020] (see Yang et al. [2023] for a comprehensive sur-
vey of early work on this topic). We confine this brief
introduction to the simplest model, which is the stable
linear diffusion process, also calledOrnstein-Uhlenbeck
process. This is given by a linear stochastic differential
equation inR d :
dX(t) =−υX(t)dt+dW(t),0≤t≤T.(2.1)
Suppose we consider the time-reversed processY(t) =
X(T−t), t∈[0, T], and simulate it fort∈[0, T]. Then
one would get at time 0 a noisy version ofX(0). This can
be taken to be a sample from the distribution from which
X(0) was drawn. This is the standard interpretation of
this procedure.
The difficulty is in reversing the diffusion. It can be
shown Anderson [1982], F¨ ollmer [2005], Haussmann and
Pardoux [1986] thatY(t), t∈[0, T], satisfies the stochas-
tic differential equation
dY(t) = (Y(t) +∇logp(Y(t)|X(0), t))dt+W(t),
t∈[0, T],(2.2)
wherep(·|X(0), t) is the conditional probability density
ofX(t) givenX(0) and∇denotes the gradient operator.
The problem then is to learn this ‘score function’ (x, t)7→
∇logp(·|x, t). This is to be learnt by minimizing the
empirical mean square error
F(θ) := eE  ∥sθ(X(t), t)−ζ(t)∥ 2 ,(2.3)
3

wheres θ(·,·) is a parametrized approximation of the
score function, usually a deep neural network (DNN)
parametrized by a vector parameterθ∈R d, and
ζ(t) is a sample based estimate of the score function
∇logp(X(t)|X(0),0). eE[· · ·] denotes the empirical
mean of (X(0), X(t)) over samples, i.e. the sample av-
erage.
The phenomenon we are interested in is the empirically
observed fact that the diffusion model, modulated by
the score function that is being concurrently learned in
a suitably parametrized form, tends to output the same
image or very similar images for significant stretches of
time. This is calledmemorization.
While flagged in particular in the context of diffusion
models, this formalism underlies all generative models
that are being tuned by a training algorithm. So we
abstract out the problem placing it in the context of
an abstract and idealized generative model borrowed
from Borkar [2025a]. Then in order to keep matters (in
particular, the notation) simple, we also abstract out
the underlying stochastic approximation algorithm with
Markov noise and analyze it as such in subsection 2.4.
We return to the implications for generative models in
section 4.
2.2 Austin ’s theorem
A recent work Borkar [2026] proposed a dynamic view of
‘double descent’ in SGD based on a stylized model which
we borrow here. This model uses the fact that given a
bound on the Lipschitz constant of a Lipschitz function
of a very large number of parameters, the function will
depend mostly on a subset of the parameter set. Some-
thing of a folklore in the machine learning community,
this is made precise in the recent work of Austin [2016].
We state Austin’s theorem below.
Let (X, d) be a compact metric space andµa proba-
bility measure on its Borelσ-algebra whose support is
connected and locally connected. ForN≥2, define the
metricd N (·,·) onX N :=X× · · · ×X(Ntimes) by:
dN ([x1,· · ·, xN ],[y 1,· · ·, yN ]) :=max 1≤i≤N d(xi, yi)
<∞.
Letω: [0,∞)→[0,∞] be a continuous non-decreasing
‘modulus of continuity’. Define Γ S(·) := projection
L2(µ)→its subspace corresponding to coordinates
i∈S⊂ {1,· · ·, N}.
Theorem 1(Austin ’s theorem) For everyϵ >0, there
exists an integerp≥1depending onX, ϵandω, with the
following property: For everyN >1, iff:X N →Rhas
modulus of continuity at mostωfor the metricd N , then
there exists anS⊂[1,· · ·, N]with|S| ≤psuch that
∥f−Γ S(f)∥ L1(µN ) < ϵ.
In other words, a hard constraint on the modulus of con-
tinuity forces the function to depend mostly on a subset
of variables, in a precise sense. Note that modulus of con-
tinuity = 1 corresponds to Lipschitz continuity, which is
the typical case of interest in machine learning because
input-output maps of standard feedforward networks do
satisfy this condition. What the foregoing then implies is
that a hard bound on the Lipschitz constant of an over-
parametrized DNN implies that the input-output map
depends mostly on a subset of parameters in a precise
sense, something of a folklore in machine learning.
2.3 A stylized model
In Borkar [2026], the above observation was used to mo-
tivate a stylized model for explaining phenomena such as
grokking or double descent, as follows. Writez= (x, y)∈
Rd wherex∈R s, y∈R r for somer, s≥1 withs+r=d.
Assume that the objective functionF:R d →R,d≫1,
has the form : for some 0< ϵ≪ 1 2 ,
F(z) =f(x, ϵy).(2.4)
This captures the relative strength of the dependence of
Fonxandy. Specifically,Fdepends significantly more
onxthan ony. We shall adopt this paradigm here.
Remark 2As pointed out in Borkar [2026], this clear
cut separation of spatial scales is a indeed stylized model.
The actual case can be much more complex, e.g., there
can be more than two scales or a continuum of scales.
For the analysis here, it suffices to have twodominant
scales.
2.4 The effect of Markov noise on SGD
In this sub-section, we summarize what is perhaps the
most technical part of the background material required
for our analysis, viz. SGD with Markov noise. LetZ n
for eachnrepresent the trajectories generated in a sin-
gle forward-backward pass of the generative model, with
state space given by a Polish spaceSand with transi-
tion probabilities modulated by the parameters of the
parametric candidate score function that is being tuned..
For example, for the classical diffusion model described
above,S=C([0, T];R d)2.
Let (x, y, w)∈Rs ×R r ×S7→f(x, y, w)∈Rdenote
the empirical loss function. As beforez= (x, y), also,
zn = (xn, yn). Consider the SGD
zn+1 =z n −a∇ zf(z n, Zn),(2.5)
4

where{Z n}is aMarkov noisein stochastic approxi-
mation parlance Benveniste et al. [1990], Chapter 8 of
Borkar [2025c]. That is,
P(Z n+1 ∈A|z 0, Zm, m≤n) =
pzn (A|Zn)∀ABorel⊂S, n≥0.(2.6)
Herep z(·|·) is a transition kernel onSparametrized
byz. Assume that it is Lipschitz inz, uniformly with
respect to the other arguments.
Letting∇ 1,∇ 2 denote the partial gradients w.r.t.x, y
resp., the SGD (2.5) splits into
xn+1 =x n −a∇ 1f(x n, ϵyn, Zn),(2.7)
yn+1 =y n −ϵa∇ 2f(x n, ϵyn, Zn).(2.8)
Note that we have replaced∇ x,∇ y by∇ 1,∇ 2 resp., to
indicate that the gradient is with respect to the first
and the second argument respectively. The need to do
so will soon become apparent. Note also that (2.8) has
the effective stepsize ofb:=ϵa≪a. This allows (2.7)
to treat the slowly varyingy n as essentially a constant
parameter, i.e.y n ≡y.
Using the theory of stochastic approximation with
Markov noise, we consider instead, modulo small (i.e.
o(a)) errors, the related dynamics
xn+1 =x(n)−a
Z
∇1f(x n, ϵyn, z)π(xn,yn)(dz)

,
(2.9)
yn+1 =y(n)−ϵa
Z
∇2f(x n, ϵyn, z)π(xn,yn)(dz)

.
(2.10)
The intuition, which has been made rigorous in literature
Benveniste et al. [1990], Borkar [2025c], is that{Z n}
evolves on the ‘natural’ clockn≥0 which is much faster
than the ‘algorithmic’ clockna, n≥0, of{(x n, yn)}for
a≪1. Hence{(x n, yn)}see only the average effect of
the{Z n}, i.e.Z n contribution averaged out with respect
to its stationary distributionπ (xn,yn) for slowly varying
(xn, yn).
Remark 3The notation∇ 1,∇ 2 now makes it clear that
the gradients do not account for the additional depen-
dence onx n, yn in their role as subscripts ofπ ···(dz).
Hence the terms in parentheses in(2.9)-(2.10)are not
necessarily gradients. Note, however, that this observa-
tion applies only when an actual gradient is used. In
most cases, one uses an approximate gradient that re-
quires only function evaluations, but no explicit differ-
entiation. Examples are classical finite difference meth-
ods such as the Kiefer-Wolfowitz algorithm Kiefer and
Wolfowitz [1952], simultaneous perturbation stochastic
approximation (SPSA) Spall [2003], methods based on
local regression Mukherjee et al. [2010] or on stochastic
perturbation Flaxman et al. [2005]. These schemes are
not free of problems, but these problems are of a different
kind. For the time being, we ignore them and revisit the
matter in the Appendix.
In view of Remark 3, we use the coupled iterations
xn+1 =x(n)−a∇ 1
Z
f(x n, ϵyn, z)π(xn,yn)(dz)

,
(2.11)
yn+1 =y(n)−ϵa∇ 2
Z
f(x n, ϵyn, z)π(xn,yn)(dz)

,
(2.12)
which are assumed to hold approximately (i.e. witho(a)
errors). The difference with (2.9)-(2.10) is that the gra-
dients with respect tox, yresp. now are over both occur-
rences of these variables, i.e., they also account for these
variables where they appear as subscripts ofπ (·,·). .
Remark 4We started with a stylized model wherez=
(x, y)andF(z) =f(x, ϵy). In practice, even if we assume
a clear separation of time scales implicit here, it is pos-
sible that multiple models with this property fit the data.
In fact the splitz= (x, y)and the concomitant represen-
tationF(z) =f(x, ϵy)may be an emergent phenomenon
during the iteration. In that case, the above analysis ap-
plies post any such emergence. More on this in section
4.2.
3 The collapse phenomenon
In this section we shall explain memorization by relat-
ing it to another, simpler phenomenon called ‘collapse’.
There has been a considerable interest and research in
machine learning in the phenomenon dubbed as ‘col-
lapse’ of generative models, see Alemohammad et al.
[2024], Dohmatob et al. [2024a,b], Gerstgrasser et al.
[2024], Marchi et al. [2024], Shumailov et al. [2024, 2023],
Suresh et al. [2024] for a sampler. This list in fact repre-
sents a broad spectrum of related phenomena. We sum-
marize here the formalism of a particularly simple case
studied in Borkar [2025a], as it captures the essence of
the phenomenon is precise mathematical terms, relating
it to the dynamics of an absorbing Markov chain in the
space of probability measures. While an idealization, it
allows us to understand the underlying dynamics and
then treat observed manifestations thereof as a pertur-
bation of this stylized model. .
Consider a Polish spaceSand a prescribedµ 0 ∈ P(S).
The generic generative model we shall consider is as fol-
lows. Leta∈[0,1]. LetP θ denote a prescribed paramet-
ric family inP(S) forθ∈a closed parameter set Θ of
some Polish space, withP θ0 =µ 0 for someθ 0 ∈Θ. We
allow nonparametric fits by allowing the possibility that
Θ =P(S). At eachn≥0, proceed as follows.
5

(1) We generateN≫1S-valued i.i.d. random vari-
ables{X i n,1≤i≤N}with their common law
being given byaµ 0 + (1−a)µ n.
(2) We fit a distributionP θ(n+1) to{X i n,1≤i≤N}
(the classical case uses the empirical distribution).
(3) We assume that this is done in a way such thatµ n
is theconditional barycenterofµ n+1 for alln, in
the sense that, w. p. 1,
E[µn+1(A)|X i m,1≤i≤N,0≤m≤n] =µ n(A)
(3.1)
for allA∈ B(S). Equivalently,
E
Z
f dµn+1

X i m,1≤i≤N,0≤m≤n 
=
Z
f dµn ∀f∈C b(S).(3.2)
Letζ n ∈ P(P(S)) denote the law ofµn forn≥0.
Note that (3.1) is always true in the case of successively
generated empirical distributions mentioned above. An-
other situation where it is true is some schemes wherein
one considers a parametric family parametrized byθ
(say) and updates the conditional law of the trueθus-
ing Bayes rule (Suresh et al. [2024]). In general, however,
this assumption is an approximation. We shall return to
this issue later.
The main results of Borkar [2025a] are summarized as
follows.
Theorem 5(i){µ n}forms a time homogeneous
Markov chain inP(S)such thatµ n is the conditional
barycenter of the law ofµ n+1 for alln.
(ii)Fora= 0,µ n →δ γ w. p.1for a randomγ∈S.
Part (ii) above follows from the simple observation that
if a time-homogeneous Markov chain converges a.s., it
must converge to an absorbing state. It captures math-
ematically the commonly understood notion ofcollapse.
We take this as our formal definition of collapse. In
particular, this is the definition we use in this article.
Barycenter of the random Dirac measureδ γ remainsµ 0.
The result of Theorem 5 (i) is better viewed asdegener-
ationrather than collapse as argued in Borkar [2025a],
because the samples can be viewed as noisy versions of
µ0, worse for smaller values ofa.
As already mentioned, we shall view memorization as
an intermittently repeated manifestation of the collapse
phenomenon.
4 Main results
We begin with a brief overview of the convergent case
of two time scale SGD in sub-section 4.1 as a backdrop,
using decreasing step sizes. This is in order to flag and
underscore the observed phenomena, both the desired
and the anomalous ones, as consequences of constant
step size, which is the task undertaken in sub-section 4.2.
Subsection 4.3 then explains how the occurrence of mem-
orization or the lack thereof comes about. All this will
be in the framework of two time scale SGD with Markov
noise introduced above, which is our abstraction for the
score function learning scheme, with Markov noise pro-
vided by the generative model being tuned. The classical
diffusion model provides a template for the same.
4.1 The convergent case
We now return to two time scale stochastic approxi-
mation, but with an important tweak, viz., the use of
decreasing step sizes. This is a simpler case to analyze
and helps motivate the case of interest here, i.e. con-
stant step size, later on. Suppose the step sizesaand
ϵain the foregoing are replaced by decreasing stepsizes
{an},{b n} ∈(0,1) satisfying the Robbins-Monro condi-
tions
X
n
an =
X
n
bn =∞,
X
n
(a2 n +b 2 n)<∞,
along with the time scale separation
bn =o(a n).
Then the classical two time scale stochastic approxima-
tion theory (Borkar [2025c] Section 8.1) leads to the fol-
lowing conclusions. We only sketch the arguments, which
closely follow the classical analyssis of two time scale
stochastic approximation Borkar [2025b]
Theorem 6The iterations(2.11)-(2.12)can be ex-
pressed as
xn+1 =x n −a n∇1Γ(xn, yn) +o(a n),(4.1)
yn+1 =y n −b n∇2Γ(xn, yn) +o(b n),(4.2)
for a suitably definedΓ :R d →R d.
PROOF.(Sketch) This proof follows by standard the-
ory of two time scale stochastic approximation We only
sketch the arguments here at an intuitive level, refer-
ring the reader to sections 8.2-8.3 of Borkar [2025c] for
details. Observe that in the stochastic gradient descent
6

(2.11)-(2.12) , there arethreetime scales:
1. The ‘Markov noise’{Z n}taking values inSevolves
on the ‘natural’ clock ofn= 0,1,2,· · ·, which is the
fastest of the three time scales.
2. Asa n ≪1 for largen, (2.11) moves on amedium
time scale Pn m=0 am, n= 0,1,2,· · ·,which is slow rela- tive to natural, i.e., thefasttime scale.
3. In turn, becauseb n =o(a n), (2.12) evolves on the
slowest time scale Pn m=0 bm, n= 0,1,2,· · ·, dubbed the
slowtime scale.
Then{Z n}seesz n = (x n, yn) as quasi-static, i.e.,
(xn, yn)≈(x, y), whence Theorem 5 applies and
L(Zn)→δ γ(z) inP(S) for a possibly randomγ(z)∈S.
Since this happens on the natural time scale, the it-
erates (x n, yn) on the slower time scales see{Z n}as
≈δ γ(xn,yn). Letting Γ(z) = Γ(x, y) :=f(x, y, γ(x, y)),
we have (4.1)-(4.2).
This is a two time scale gradient descent Borkar [2025b].
Suppose that
λ(y) :=argmin xΓ(x, y)
is uniquely defined and Lipschitz, and Γ(·, y) has no other
critical points. Also, suppose further that Γ(λ(·),·) has
a unique minimumy ∗. Then this reduces to the special
case of Borkar [2025c], Section 8.1, which precisely says
thatλ(x n)−y n →0 a.s. in the more general context of
two time scale stochastic approximation (not only SGD).
Theorem 7Suppose{Z n}is being generated by a pure
generative model as above with parameters(x n, yn), n≥
0,being tuned by(2.7)-(2.8). Then asymptotically,{Z n}
exhibits collapse.
PROOF.By the standard analysis of two time scale
algorithms,x n ≈λ(y n) and therefore modulo some
asymptotically negligible error (i.e.,o(b n)) terms,
yn+1 =y n −b n∇Γ(λ(yn), yn) +o(b n).
Recall thatλ(y) = argmin(Γ(·, y)) Thus it follows from
Danskin’s theorem (Danskin [2012]) that∇Γ(λ(y), y) =
∇min x Γ(x, yn), making it an SGD . Nowyn →y ∗ (say).
Thenx n →λ(y ∗) and{Z n}is asymptotically a pure
Markov chain generative model that will exhibit pure
collapse by Theorem 5 (i).
In case of multiple local minima of Γ(·, y), we get con-
vergence to one of the local minima if the noise is ‘rich
enough’ in all directions in a suitable sense, so that the
iterates get pushed away from equilibria other than local
minima, a.s. This is the ‘avoidance of traps’ by stochas-
tic approximation algorithms, see Borkar [2025c], Sec-
tion 3.4, and the references therein. As this is standard
fare of the classical stochastic approximation theory, we
skip the details.
However, we arenotusing decreasing step sizes. We ar-
gue in the next subsection that memorization as it is
known in practice is explicitly a phenomenon caused by
the fact that we use a constant step size.
4.2 The role of stepsizes
A very detailed mathematical analysis of the asymptotic
behaviour of the classical SGD inR d with constant step
size, given by
xn+1 =x n −a(∇f(X n) +M(X n)),(4.3)
can be found in Azizian et al. [2024]. We take it as a
starting point and make a precise quantitative state-
ment about how the limiting distribution concentrates
on global minima of the large deviations rate function
in thea↓0 limit. We first summarize below some qual-
itative statements taken verbatim from Azizian et al.
[2024]. HereM(x) is a family of random variables that
is zero mean with uniformly positive definite covariance
matrix and sub-gaussian tails, twice continuously differ-
entiable inx, with∥M(x)∥satisfying a uniform linear
growth condition in∥x∥.
Remark 8The above model correctly captures the stan-
dard scenario in SGD as applied in machine learning.
Supposeℓ(θ, Xn, Yn)denotes the empirical loss at time
n, parametrized by the parameterθ. The gradient de-
scent will use the instantaneous gradient∇θℓ(θn, Xn, Yn)
where{(X n, Yn)}are i.i.d.,∇ θ denotes the gradient in
theθvariable, andθ n is the current parameter estimate.
ReplacingX n in(4.3)by(X n, Yn)and setting
f(θ) :=E[ℓ(θ, Xn, Yn)],
M(X n, Yn) :=∇ θℓ(θ, Xn, Yn)− ∇f(θ),
we get(4.3).
The key conclusions of Azizian et al. [2024], taken ver-
batim from there, are:
(1)In the long run, the critical region offis visited ex-
ponentially more often than any non-critical region.
(2)The iterates of SGD are concentrated with exponen-
tially high probability in the vicinity of a region that
minimizes a certain “energy functional” which de-
pends onfand the statistics of the noise in SGD.
7

Importantly, the ground state of this func-
tional does not necessarily coincide with the
global minimum off.
(3)Among the remaining connected components of
critical points, each component is visited with fre-
quency which is exponentially proportional to its
energy, according to the Boltzmann–Gibbs distribu-
tion of statistical physics with temperature equal to
the method’s step-size.
(4)Every connected component of non-minimizing crit-
ical points off– i.e., local maximizers or saddle
points – is “dominated” by a component of local min-
imizers that is visited exponentially more often.
This applies to our case with ‘negative energy’ in place of
‘energy’ in bullet 3. The analysis of Azizian et al. [2024],
which is too extensive and intricate to include here in
toto, is inspired by the analysis of Freidlin and Wentzell
[2012] for small noise limit of diffusion processes.
Remark 9In some recent works Li et al. [2026], Mandt
et al. [2017], the Freidlin-Wentzell theory is directly in-
voked to claim that the stationary distribution of(4.3)
concentrates on the global minima ofF. This is based on
viewing the noise on the time scale of stepsize √a, which
allows us to view the constant step size SGD as a discrete
analog of the Langevin diffusion
dx(t) =−∇F(x(t))dt+dW(t),
whereW(·)is a standard Wiener process inR d. However,
it is clear from Remark 8 that the noise should be scaled
byaand not by √a. This is precisely what leads to the
comment in boldface in the second bullet in the remarks
from Azizian et al. [2024] cited above. We comment on
this issue again in the concluding section.
We next refine the above analysis in view of the results
of Hwang [1981], which allows us to explain another
phenomenon observed in practice - SGD prefers simpler
(read ‘flatter’) minima. LetV(·) denote the rate function
for the large deviations for thea↓0 limit in the station-
ary distribution for constant stepsize SGD established in
Azizian et al. [2024]. Assume thatV(·) is twice continu-
ously differentiable and has finitely many isolated global
minima atm i,1≤i≤ℓ, where∇ 2Vis non-singular.
Theorem 10Asa↓0, the asymptotic probability
weights atm i,1≤i≤ℓ, are given by
Qd
j=1 Λk j
− 1 2
,
whereΛ k j >0,1≤j≤d,are the eigenvalues of
∇2V(m k).
PROOF.Asa↓0, the stationary distribution becomes
proportional toe − V(x) a and thus concentrates on the
global minima of this ‘potential’V(·) by the results of
Azizian et al. [2024]. SupposeVis twice continuously
differentiable and its Hessian∇2Vis nonsingular at each
global minimumm i,1≤i≤ℓ. Then by a result of
Hwang [1981], the asymptotic probability mass at the
global minimumm k (say) is proportional to

det

∇2V(m k) − 1 2 =


nY
j=1
Λk j


− 1 2
,
where Λ k j >0,1≤j≤m,are the eigenvalues of
κ(mk) :=∇ 2V(m k).
Thus the small noise limit favours the global minimami
where det(∇2V(m i)) is low, whence not all eigenvalues
can be high. This suggests that only few eigendirections
matter, supporting the intuition that simpler minima
that afford a compact description in the local eigenbasis
are favoured.
4.3 The onset of memorization
We now combine the foregoing to explain the intermit-
tent phenomenon of memorization that occurs in the
training of generative models. We saw in subsection 3
that in the decreasing step size case with convergent it-
erations on both time scales, a collapse would occur even
with concurrent tuning of the parameters of the genera-
tive model. The catch is that with constant step size and
multiple equilibria, we do not expect convergence. Focus-
ing on the fast time scale alone, an isolated minimum ofR
f((·, y), z)π(·,y)(dz) would be parametrized byy, so if
ydrifts on a smaller time scale, the minimum overxmay
drift and / or jump, as in, e.g., the well known relaxation
oscillations in mechanics (Berglund and Gentz [2005]).
Evenwithina single time scale, a gradient descent can
jump between multiple stable equilibria, though only
rarely as the results of Azizian et al. [2024] show. How
rare is rare enough will depend on the magnitude ofa.
We next give a stylized picture of memorization in a
simplified framework. Consider the case when (2.11)-
(2.12) represent the SGD for training a diffusion model.
Let
φ(x, y) :=
Z
f(x, ϵy, z)π(x,y)(dz).
Suppose for eachy∈R r,φ(·, y) has multiple isolated
local minima labelledλ i(y),1≤i≤m,whereλ i’s are
locally Lipschitz. Suppose also thatφ(λ i(y), y) has mul-
tiple isolated local minima, labelled ˆy1,· · ·,ˆyk resp. As-
sume thatϵ≪1.
Theorem 11Supposeˆy i ̸=argmin(φ(·,ˆy i))for all
i,1≤i≤k. Then the dynamics(2.11)-(2.12)can ex-
hibit memorization in the sense thatx n −λ(y n)≈0for
aλ:R r →R s for long stretches ofn, with{y n}evolving
on a much slower time scale than{x n}.
8

PROOF.From standard stochastic approximation
theory (specifically, the ‘ODE approach’, see Chapter 2
of Borkar [2025c] or Benveniste et al. [1990]),{(x n, yn)}
track the the coupled ODEs
˙x(t) =−∇1φ(x(t), y(t)),(4.4)
˙y(t) =−ϵ∇2φ(x(t), y(t)).(4.5)
Consider now (2.9)-(2.10) as representing our scheme for
tuning a generative model such as the diffusion model,
with{Z n}as the input coming from the generative
model. Then becauseϵ≪1, (2.7) seesy n as quasi-static
and starts trackingλ(y i) for some 1≤i≤k. Then, in
a small neighbourhoodO(y i) ofy i,{y n}starts tracking
the ODE
˙y(t) =−∇φ(λ(y(t)), y(t)),
where we use Danskin’s theorem as before. How-
ever, sincey i /∈argminφ(·, yi), the vector field
−∇φ(λ(y(t)), y(t)) remains bounded away from zero in
O(yi), whencey(t) exitsO(y i). Because of the presence
ofϵon the right hand side of (4.2), this movement is
slow andx(t) does not change much, thus leading to a
non-negligible time whenx(t)≈λ i(t). Since (x n, yn)
track (x(t), y(t)) on a moving time window, (x n, yn)
mimic this behaviour, leading to memorization.
Fork= 2, one would get the well known relaxation
oscillations phenomenon in mechanics already alluded to
above (Berglund and Gentz [2005]). Here the trajectory
spends substantial time in the neighbourhoods of two
points, occasionally making a relatively rapid transition
from one to the other. This is distinct from the occasional
jump between multiple equilibria in the frameworks of
Azizian et al. [2024] or Freidlin and Wentzell [2012] -
as already noted, these are on an exponentially small
time scale, i.e., rare. Memorization, when it occurs, is
intermittent, but not rare. This is because the transitions
are not purely noise-driven, but aided by a drift in the
dynamics itself on a slower albeit non-negligible time
scale.
Even so, there were many idealizations in the foregoing,
most prominently in assuming the conditional barycen-
ter property of the random probability distributions gen-
erated by the generative model. The probability mea-
sureP θ(n) need not be the exact conditional barycenter
ofP θ(n+1) forn≥1. We have already observed that
the conditional barycenter property holds for generative
models that use successive empirical distributions based
on simulated samples and in some idealized bayesian
frameworks. Also, while the schemes for estimating the
score function do have an apparent semblance to the
SGD model used here (recall (2.3)), these are far more
complicated. Thus the foregoing analysis addresses to
some extent an idealized situation, although it captures
the spirit of the phenomenon adequately to underscore
the underlying mechanisms. There are other minor sim-
plifications which too will contribute to our analysis not
being fully accurate. We club them together with the
above as sources of error. In reality, the memorization
phenomenon is often not so drastic and sometimes not
there at all. This is where the approximation errors play
a role. We shall simplify the analysis by treating approx-
imation errors as persistent external noise. Then the sit-
uation is similar to that of Theorem 5 (i) rather than
that of Theorem 5 (ii) that was invoked above in our
modelling of memorization. Thus the underlying phe-
nomenon is not pure collapse, but a corruption of col-
lapse by persistent noise. This is why when memoriza-
tion occurs, it need not be exact repeated duplication of
past outputs, but a bias towards noisy versions thereof
to a varying degree and duration. This ‘degree’ will de-
pend on many parameters, which we discuss next.
It is observed in Wu et al. [2025] that a large step size
discourages memorization. This is not a surprise because
of the known fact that a large step size leads to higher
levels of noise in the iteration, while maintaining a faster
trend towards the goal (Borkar [2025c], Chapter 9). This
is evident if you consider the iteration as a noisy dis-
cretization of the corresponding ODE limit. This view-
point treats the step sizeaas a time step. Thus larger
aimplies faster tracking of the ODE. Butaalso multi-
plies the noise, so it leads to higher fluctuations. This is
a standard trade-off in stochastic iterative algorithms.
Naturally, bigger step size leads to more noise which, as
already argued, discourages memorization. .
To touch base with what we started with, the classi-
cal diffusion model takes an image as an input to an
Ornstein-Uhlenbeck process run till you get ‘almost’
noise, then take that noisy image as an input to a
time-reversed diffusion to generate an image which pu-
tatively is another image from the same distribution
as the one that generated the original image. The drift
function of the reversed diffusion has the unknown term
∇logp(X(t)|X(0), t) wherep(·|X(0), t) is the proba-
bility density ofX(t) at timet, starting atX(0). This
is thescore functionwhose parametric approximation
is learnt iteratively. We then haveS=C([0, T];R d)2
and the iteration (2.5) is our surrogate for the learn-
ing algorithm for the score function. The well known
memorization phenomenon in this particular context is
the diffusion model generating the same image over and
over again every now and then. But while the problem
of diffusion model training was our starting motivation,
we prefer to remain at the the level of abstraction we
have been using hitherto and avoid being too specific,
because diffusion models and generative models in en-
eral are fast moving fields and anything ultra-specific
that we say will soon be dated.
9

5 Conclusions and future directions
We have presented a dynamic view of the phenomenon
of memorization reported in the training of diffusion
models, drawing upon some analysis of the related phe-
nomenon of ‘collapse’ in machine learning. This also
leads to some qualitative feel for the various factors af-
fecting its occurrence and intensity, and throws up some
interesting directions for further research. The work is
grounded in some recent developments in stochastic ap-
proximation with constant step size due to Azizian et al.
[2024] and flags its importance in the analysis of machine
learning algorithms.
Going forward, one important problem is to estimate
the error in the global minima of the Freidlin-Wentzell
potentialVfor the constant stepsize stochastic approx-
imation, and those of the function Γ ′(·) := Γ(λ(·),·) be-
ing minimized. Γ′ would be the Freidlin-Wentzell poten-
tial for the Langevin dynamics andipso facto, an ap-
proximation for the Freidlin-Wentzell potential for its
discretization, viz., the Langevin algorithm. Γ ′ has an
explicit control theoretic expression given by
Γ′(x) = inf
Ax
Z ∞
0
∥u(t)∥2dt,
whereA x is the set of all trajectories of the control sys-
tem
˙x(t) =∇F(x(t)) +u(t), t≥0,
that satisfyx(0) =xandx(t)→one of the global min-
ima ofF, see Freidlin and Wentzell [2012], Section 6.4,
Sheu [1986], Biswas and Borkar [2009] for results in this
vein for increasing level of generality. The results of Az-
izian et al. [2024] indicates that an analogous expression
should hold forV(·). The respective potentials, being
value functions of suitable control problems, should be
unique viscosity solutions to the appropriate Hamilton-
Jacobi equations in a suitable class of functions, e.g.,
continuous functions with appropriate bounds on their
growth rates at infinity. This should facilitate a compar-
ison between the two. This remains a research problem
for the future.
Acknowledgements
SA was supported by the Department of Atomic Energy,
Government of India, under project no. RTI4001, CB
was supported by research grant from Shell Markets In-
dia and VSB was supported by a National Science Chair
from the Government of India. A part of the work was
done while VSB was visiting International Centre for
Theoretical Sciences, Bengaluru. VSB thanks Dr. Anik
Kumar Paul for helpful discussions regarding the mate-
rial in the Appendix, which helped clarify some subtle
issues.
References
S. Alemohammad, J. Casco-Rodriguez, L. Luzi, A. I.
Humayun, H. Babaei, D. LeJeune, A. Siahkoohi, and
R. Baraniuk. Self-consuming generative models go
mad. InThe Twelfth International Conference on
Learning Representations, May 7-11, 2024, Vienna,
pages 7–11, 2024.
B. D Anderson. Reverse-time diffusion equation mod-
els.Stochastic Processes and their Applications, 12(3):
313–326, 1982.
T Austin. On the failure of concentration for theℓ ∞–
ball.Israel Journal of Mathematics, 211(1):221–238,
2016.
W. Azizian, F. Iutzeler, J. Malick, and P. Mertikopou-
los. What is the long-run distribution of stochastic
gradient descent? a large deviations analysis, 2024.
R. Baptista, A. Dasgupta, N. B. Kovachki, A. Oberai,
and A. M. Stuart. Memorization and regularization
in generative diffusion models, 2025.
A. Benveniste, M. M´ etivier, and P. Priouret.Adaptive
Algorithms and Stochastic Approximations. Springer.,
1990.
N. Berglund and B. Gentz. Noise-induced phenomena
in slow-fast dynamical systems: A sample-paths ap-
proach.Springer: Berlin Heidelberg, 2005.
P Billingsley.Convergence of Probability Measures. John
Wiley & Sons, 1968.
A. Biswas and V. S. Borkar. Small noise asymptotics for
invariant densities for a class of diffusions: a control
theoretic view.Journal of Mathematical Analysis and
Applications, 360:476–484, 2009.
V. S. Borkar. Stochastic approximation with two time
scales.Systems and Control Letters, 29:291–294, 1997.
V. S Borkar. A theoretical basis for model collapse in
recursive training.Proccedns of the 61st Allerton Con-
ference on Communication, Control and Computing,
Uni. of Illinois at Urbana-Champaign, Sept. 17-19,
2025, arXiv preprint arXiv:2506.09401, 2025a.
V. S Borkar. Stochastic approximation with two time
scales: The general case.Stochastic Processes and their
Applications, page 104759, 2025b.
V. S Borkar.Stochastic Approximation: A Dynamical
Systems Viewpoint (Second edition). Hindustan Pub-
lishing Agency and Springer, 2022/2025, 2025c.
V. S Borkar. A dynamic view of some anomalous phe-
nomena in sgd for over-parametrized neural networks.
Systems & Control Letters, 207:106285 using the re-
sults of?, 2026.
S. Buchanan, D. Pai, Y. Ma, and V. De Bortoli. On the
edge of memorization in diffusion models, 2025.
C. Chen, D. Liu, and C. Xu. Towards memorization-free
diffusion models. InProceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recogni-
tion, 8425-8434, pages 8425–8434, 2024.
J. M. Danskin.The theory of max-min and its application
to weapons allocation problems. Springer, 2012.
E. Dohmatob, Y. Feng, and J. Kempe. Model collapse
demystified: The case of regression, 2024a. 2024a.
10

E. Dohmatob, Y. Feng, P. Yang, and J. Kempe. A tale
of tails: Model collapse as a change of scaling laws.
InForty-first International Conference on Machine
Learning, 2024b, 2024b.
A. D. Flaxman, A. T. Kalai, and H. B. McMahan. On-
line convex optimization in the bandit setting: gra-
dient descent without a gradient.Proceedings of the
16th Annual ACM-SIAM Symposium on Discrete Al-
gorithms, Vancouver, BC, pages 385–394, 2005.
M. I. Freidlin and A. D. Wentzell.Random Perturbations
of Dynamical Systems(3rd Edition). Springer, 2012.
F¨ ollmer. H., 2005. an entropy approach to the time
reversal of diffusion processes. InStochastic Dif-
ferential Systems Filtering and Control: Proceedings
of the IFIP-WG 7/1 Working Conference Marseille-
Luminy, France, March 12–17, 1984 (pp. 156-163).
Springer: Berlin Heidelberg, pages 156–163, 2005.
M. Gerstgrasser, R. Schaeffer, A. Dey, R. Rafailov,
H. Sleight, J. Hughes, T. Korbak, R. Agrawal, D. Pai,
and A. et al. Gromov. Is model collapse inevitable?
breaking the curse of recursion by accumulating real
and synthetic data, 2024.
X. Gu, C. Du, T. Pang, C. Li, M. Lin, and Y. Wang. On
memorization in diffusion models, 2023.
U. G. Haussmann and E. Pardoux. Time reversal of dif-
fusions.The Annals of Probability, pages 1188–1205,
1986.
D. Hintersdorf, L. Struppek, K. Kersting, A. Dziedzic,
and F. Boenisch. Finding nemo: Localizing neurons
responsible for memorization in diffusion models.Ad-
vances in Neural Information Processing Systems, 37:
88236–88278, 2024.
C.-R Hwang. A generalization of laplace’s method.Pro-
ceedings of the American Mathematical Society, 82(3):
446–451, 1981.
J. Kiefer and J. Wolfowitz. Stochastic estimation of the
maximum of a regression function.Annals of Mathe-
matical Statistics, 23(3):462–466, 1952.
J. Kim, S. Kim, and J.S. Lee. How diffusion models
memorize, 2025.
X. Li, Z. Shen, Y. P. Hsieh, and N. He. Minima selection
in stochastic optimization: a long-time, small-stepsize
perspective.Preprint, 2026.
S. Mandt, M. D. Hoffman, and D. M. Blei. Stochastic
gradient descent as approximate bayesian inference.
Journal of Machine Learning Research, 18:1–35, 2017.
M. Marchi, S. Soatto, P. Chaudhari, and P. Tabuada.
Heat death of generative models in closed-loop learn-
ing, 2024.
S. Mukherjee, Q. Wu, and D.-X. Zhou. Learning gra-
dients on manifolds.Bernoulli 16(1), pages 181–207,
2010.
B. Pham, G. Raya, M. Negri, M.J. Zaki, L. Ambro-
gioni, and D. Krotov. Memorization to generalization:
Emergence of diffusion models from associative mem-
ory, 2025.
S.-J. Sheu. Asymptotic behavior of the invariant den-
sity of a diffusion markov process with small diffusion.
SIAM Journal on Mathematical Analysis, 17:451–460,
1986.
I. Shumailov, Z. Shumaylov, Y. Zhao, Y. Gal, N. Paper-
not, and R. Anderson. The curse of recursion: Train-
ing on generated data makes models forget, 2023.
I. Shumailov, Z. Shumaylov, Y. Zhao, N. Papernot,
R. Anderson, and Y. Gal. Ai models collapse when
trained on recursively generated data.Nature, 631
(8022):755–759, 2024.
Y. Song, J. Sohl-Dickstein, D.P. Kingma, A. Kumar,
S. Ermon, and B. Poole. Score-based generative mod-
elling through stochastic differential equations, 2020.
J. C Spall.Introduction to Stochastic Search and Opti-
mization: Estimation. Simulation and Control, Wiley-
Interscience, 2003.
A. T. Suresh, A. Thangaraj, and A. N. K. Khandavally.
Rate of model collapse in recursive training.Proceed-
ings of the 28th International Conference on Artifi-
cial. Intelligence and Statistics (Y. Li, S. Mandt, S.
Agrawal and E. Khan, eds.), PMLR vol. 258, 2025:
1396–1404, 2024.
H. Wang, Y. Han, and D. Zou. On the discrepancy and
connection between memorization and generation in
diffusion models. InICML 2024 Workshop on Foun-
dation Models in the Wild, 2024.
Y. Wen, Y. Liu, C. Chen, and L. Lyu. Detecting, explain-
ing, and mitigating memorization in diffusion models.
InThe Twelfth International Conference on Learning
Representations, Vienna, 2024.
Y.H. Wu, P. Marion, G. Biau, and C. Boyer. Taking a big
step: Large learning rates in denoising score match-
ing prevent memorization. InProceedings of the 38th
Annual Conference on Learning Theory, 2025.
L. Yang, Z. Zhang, Y. Song, S. Hong, R. Xu, Y. Zhao,
W. Zhang, B. Cui, and M. H. Yang. Diffusion models:
A comprehensive survey of methods and applications.
ACM computing surveys, 56(4):1–39, 2023.
Z. Ye, Q. Zhu, M. Tao, and M. Chen. Provable sepa-
rations between memorization and generalization in
diffusion models, 2025.
11

Appendix B: The problem of gradient
The notation∇ 1,∇ 2 in (2.9)-(2.10) makes it clear that
the gradients do not account for the additional depen-
dence onx n, yn in their role as subscripts ofπ ···(dz).
Hence (2.9)-(2.10) do not necessarily constitute an in-
stance of SGD. Note, however, that this observation
applies only when an actual gradient is used. As al-
ready pointed out, in most cases, one uses an approx-
imate gradient that requires only function evaluations,
but no explicit differentiation. Examples are classical fi-
nite difference methods such as the Kiefer-Wolfowitz al-
gorithm Kiefer and Wolfowitz [1952], two sample simul-
taneous perturbation stochastic approximation (SPSA)
Spall [2003], methods based on local regression Mukher-
jee et al. [2010], single sample SPSA Spall [2003] and
stochastic perturbation based methods Flaxman et al.
[2005]. However, the schemes that require two function
approximations are not free of problems. They require
iterate values at two time instants,tandt+δfor some
0< δ≪1. The finite difference approximation then re-
quires that two separate copies of Markov noise be avail-
able: one whose transitions are modulated byx(n) and
another whose transitions are modulated byx(n)+ a
small perturbation. This is not feasible in on-line train-
ing and doubles the simulation budget in off-line train-
ing. Schemes that use a single function evaluation ap-
pear to be the only ones that are free of these problems.
Consider for example the noisy estimator for∇F(x n)
given by
f(x n +δξ n, Zn)ξn
δ ..
Here{ξ n}ared-dimensional i.i.d. zero mean vectors
with identity covariance matrix. This is adapted from
the proposal of Flaxman et al. [2005] to accommodate
Markov noise.
Letνdenote the common law ofξ n, n≥0. LetF n :=
theσ-fieldσ(x m, Zm, ξm, m≤n), n≥0, where{Z n}is
a Markov noise with
P(Z n ∈A|F n) =p xn+δξn (A|Zn)
for a transition kernelp x(·|·) as in (2.6). We can view
{(Zn, ξn)}as an extended Markov noise. Suppose the
stationary law of (Z n, ξn) givenx m ≡xis given by
πn(dz, dy|x) =ν(dy)η x+δy (dz) whereη x(dz) is the
unique stationary distribution ofp x(dz′|z). Then
E
 f(x n +δξ n, Zn)ξn
δ

 Fn 
= 1 δ Z Z (f(x n +δy, z)yπn(dz, dy)
= 1 δ Z f(x n +δy, z)yηxn+δy (dz)ν(dy)
= 1 δ Z Z f(x n, z)yηxn (dz)ν(dy)
+ 1 δ Z Z (∇f(x n, z)ηxn (dz))δyy T ν(dy) +o(δ)
=
Z
∇xf(x n, z)ηxn (dz) +o(δ)
=∇ x
Z
f(x, z)ηx(dz)


x=xn
+o(δ)
=∇F(x n) +o(δ)
forF(·) :=
R
f(·, z)η·(dz).
Here in the fourth equality, we have used the fact that
ξn has zero mean and identity covariance matrix, i.e.,R
yν(dy) = the zero vector and
R
yy T ν(dy) = the iden-
tity matrix. Hence we have
∇F(x n))≈E
 f(x n +δξ n, Zn)ξn
δ

 Fn 
as desired.
An alternative scheme is based on single function eval-
uation based SPSA of Spall [2003] wherein we estimate
∂F
∂x(i) (xn) by
f(x n +δξ n, Zn)
δξn(i)
withξ n(i),1≤i≤d, n≥0, i.i.d. taking values±1 with
equal probability. This too can be analyzed along above
lines.
Both cases suffer from the small divisor problem leading
to high variance and need additional averaging in order
to control it. They are, however, theoretically kosher
unlike (2.9)-(2.10) and also avoid the complications of
schemes that require two or more samples.
12
