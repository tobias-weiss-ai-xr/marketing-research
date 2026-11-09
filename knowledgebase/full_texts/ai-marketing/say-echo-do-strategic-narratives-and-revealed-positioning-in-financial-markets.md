---
title: 'Say, Echo, Do: Strategic Narratives and Revealed Positioning in Financial Markets'
url: https://arxiv.org/abs/2609.38545
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Ali Atiah Alzahrani
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.38545
pages: 31
chars: 94023
fetched_at: '2026-11-08T13:24:55+00:00'
kb_version: 1
---

# Say, Echo, Do: Strategic Narratives and Revealed Positioning in Financial Markets

Say, Echo, Do: Strategic Narratives and
Revealed Positioning in Financial Markets
Ali Atiah Alzahrani∗
Riyadh, Saudi Arabia
Abstract
Machine-learning signals built from financial text treat what institutions say, and
what the media repeat, as evidence about value. But whoever shapes a narrative may
be trading against it. We study markets with three observable voices: institutional
statements (Say), media repetition (Echo) and revealed positioning (Do). We
ask when words should be followed and when they should be faded. In a linear–
quadratic model of an informed institution that speaks and trades before a partly
credulous crowd, talking an asset down while buying it is optimal exactly when
φ2 <2λk < φ. A distribution-free identity then shows that when the observable
Say–Do covariance is negative, words carry negative predictive content and should
be faded. For measurement, we derive (i) an exact factorised posterior over which
articles are echoes, combining arrival times with embedding similarity; (ii) a return-
aligned contrastive objective that attains its bound exactly when squared embedding
distances are an increasing affine function of squared outcome distances, with
the tightest loss-based certificate of which neighbour rankings survive imperfect
training; and (iii) a path-signature statistic for who moved first. In a controlled
market with known ground truth, echo sentiment predicts returns with a significantly
negative sign in all 29 simulated markets, the rolling Say–Do correlation flags
false-alarm events with an AUC of 0.90, and return-aligned embeddings organise
headlines by consequence rather than topic. We also report where the tools fail.
1 Introduction
A bank downgrades a stock. Within hours newswires rewrite the note, commentators repeat it and
social media amplifies it. The price falls, but by less than the volume of bad news would suggest, and
weeks later it is higher than before. The next round of disclosures shows that some institutions were
buying throughout. Traders call this afalse alarm.
Most machine-learning pipelines for financial text would score this episode as strongly negative.
Sentiment classifiers, domain encoders and prompted language models map a document to a number
that is assumed to move with value (Ke et al., 2019; Araci, 2019; Lopez-Lira and Tang, 2023). That
assumption fails when text isstrategic. The author of a narrative may profit from the crowd’s reaction
to it, and repetition inflates a signal without adding information. The useful question is therefore not
only what a text says. It is also whether its author’s money agrees, and whether the text is news or an
echo of earlier news.
∗First draft, September 2026. Corresponding author: aliatiah100@gmail.com. The views expressed are those of the author
and do not reflect the views of any other individual or entity. This material is for research purposes only and does not constitute
investment advice.
Preprint.
arXiv:2609.38545v1  [q-fin.TR]  29 Sep 2026

Voices Measurement (§4) Theory (§3) Decision
Say
statements, notes
Echo
rewrites, reposts
Do
holdings, flow
return-aligned embeddings: what
similar stories did next
(Theorems 7 and 8)
semantic declustering: is each
article news or echo? (Theorem 6)
rolling dCov(Say,Do) ; Lévy area:
who moved first? (Theorem 9)
optimal speech: false alarms
iff φ2 <2λk < φ (Theorem 3)
fade the echo, follow the news
(Theorem 1 and Corollary 2)
words vs deeds (Theorem 4):
Cov(r,Say) =λCov(Do,Say)−φσ 2 ε
followorfade
words, echo
and news;
always
follow deeds
Figure 1: Overview. Three observable voices are turned into measurements, and the theory says
which sign each measurement should carry. The central object is the Say–Do covariance: when
institutions’ words and positions move in opposite directions, their words should be faded.
We separate three voices that any market participant can observe (Figure 1).Sayis what institutions
state: ratings, notes, management tone.Echois how the media repeat and amplify it.Dois where
capital is revealed to have gone: holdings, insider trades, futures positioning, order flow. Words
are cheap and easy to observe, repetition is mostly redundant, and positions are costly, slow to be
disclosed and hard to fake.
Contributions.
• A theory of strategic narratives(Section 3). We solve for the optimal message and trade of an
informed institution facing a partly credulous crowd. False alarms, in which the institution talks
an asset down while buying it, are optimal in an explicit wedge of parameters. A distribution-
free identity shows that a negative Say–Do covariance means words should be faded. Media
virality selects which kind of manipulation appears, and adaptive trust can cycle and, numerically,
become chaotic: repeated re-estimation of the reading rule fails to converge, as in repeated risk
minimisation under performativity (Perdomo et al., 2020).
• Measurement with guarantees(Section 4). An exact posterior over echo parentage that uses both
timing and meaning. A return-aligned contrastive objective that attains its lower bound exactly
when embedding geometry reproduces outcome geometry, together with the tightest certificate,
among those based on the excess loss alone, of which neighbour rankings survive imperfect
training. A signature statistic that identifies lead and lag.
• A controlled evaluation(Section 5). A simulated market in which every ground-truth quantity is
known, a synthetic headline benchmark, and a report of both successes and failures, including
where the theory adds nothing a linear model cannot learn. Code, tests and every experiment are
released athttps://github.com/AliAtiah/say-echo-do.
What we do not claim.A “strategic” reading means only that words and money moved in opposite
directions, in a particular order. It is not evidence of deception. We do not test the theory on market
data; our experiments are simulated so that the truth is known.
2 Related work
Financial text.Media pessimism predicts price pressure and reversal (Tetlock, 2007), and prices
drift after news but reverse after no-news moves (Chan, 2003). Supervised text factors (Ke et al.,
2019), domain encoders (Araci, 2019) and prompted language models (Lopez-Lira and Tang, 2023)
predict returns, subject to look-ahead leakage (Glasserman and Lin, 2023). These methods take text
at face value. We model the author’s incentive to shape it, and use revealed positions to discount it.
Strategic behaviour and performativity.Cheap talk (Crawford and Sobel, 1982), costly talk with
credulous receivers (Kartik et al., 2007) and reputational manipulation (Bénabou and Laroque, 1992)
2

study how informed agents shape beliefs. Closest to us, informed traders can profit by spreading
rumours and trading against them (van Bommel, 2003), and promotional articles move prices (Kogan
et al., 2023). Order flow reveals private information (Kyle, 1985). In machine learning, strategic
classification (Hardt et al., 2016) and performative prediction (Perdomo et al., 2020) study predictions
that change the data they are evaluated on. Our institution games a known reading rule, and our
credibility cycles are a closed-form case in which repeated re-estimation of that rule fails to converge.
Point processes, representations and signatures.We build on the cluster representation of Hawkes
processes (Hawkes, 1971; Hawkes and Oakes, 1974). Our declustering posterior has the structure
of space–time ETAS declustering (Zhuang et al., 2002), with embeddings in place of locations and
offspring marks that depend on the parent’s. Text-aware point processes cluster document streams or
infer diffusion networks (Du et al., 2015; He et al., 2015), and neural Hawkes models learn intensities
(Mei and Eisner, 2017), but none attributes each article to news or echo. Our embedding objective is
the stochastic neighbour embedding loss (Hinton and Roweis, 2002) with market outcomes as the
input space, a link between contrastive learning and SNE that is known (Hu et al., 2023; Damrich et
al., 2023). It is close to contrastive learning with continuous labels (van den Oord et al., 2018; Khosla
et al., 2020; Dufumier et al., 2021; Zha et al., 2023). Our additions are the characterisation of when
the bound is attained, which is elementary, and a tight certificate for imperfect training. Lévy area is
the antisymmetric part of the level-two path signature (Lyons, 1998; Chevyrev and Kormilitzin, 2016;
Kidger et al., 2019), and has been used to detect lead–lag between asset returns (Bennett et al., 2022).
3 Theory: three voices and strategic speech
3.1 A three-voice market
Value is v∼ N(0, σ2 v). The market observes K public channels y=hv+ν with Gaussian noise,
labelled by voice: statements, independent news and echo. Informed traders submit x=β(v−p) ,
noise traders submit u∼ N(0, σ2 u), and a narrative-sensitive crowd sets the pricep=φ ⊤y+λ(x+u) ,
where φ collects the crowd’snarrative multipliers(Assumptions 1 and 2, Section A). Write r=v−p
for the forward return,w ⋆ =σ 2 vΣ−1 y hfor the Bayes weights, andκ= (1 +λβ) −1.
Theorem 1(Follow or fade).Under Assumptions 1 and 2, E[r|y] =κ(w ⋆ −φ) ⊤y and Var(r|
y) =κ 2(σ2 v|y +λ 2σ2 u) =: ς 2, where σ2 v|y = Var(v|y) . The return loads negatively on channel k
(fade) iffφ k > w⋆ k, and positively (follow) iffφ k < w⋆ k.
Corollary 2(Fade the echo, follow the news).Under Assumptions 1 and 2: (i) if channel e is a
garbling of the others, e=a ⊤y−e +ξ with ξ∼ N(0, σ2 ξ ), σ2 ξ >0 , independent of (v,y −e, u),
then w⋆ e = 0 and the return loads on e with coefficient −κφe, so any crowd weight on echo
is reversed; (ii) if channel n=v+ν n with νn ∼ N(0, σ2 n) independent of (v,y −n, u), and
s2 := Var(v|y −n)>0 , then w⋆ n =s 2/(s2 +σ 2 n)∈(0,1) , and returns drift in the direction of n
whenever the crowd underweights it,φ n < w⋆ n.
Two further results, proved in Section A, are used in the experiments. When positioning is observed
with noise, the optimal forecast depends on words and deeds only through a weightedSay–Do gap
(Theorem 13). And the price move net of the narrative, calledabsorption, predicts continuation if
and only if informed flow dominates noise,βσ 2 v|y > λσ2 u (Theorem 14).
3.2 Strategic speech
We now let an institution choose what it says. It knows v (any distribution with mean zero and finite
variance), publishes a message m that the public sees with noise, ˜m=m+ε , and trades x. The
price is p=φ˜m+λx , where φ is the crowd’s credulity, and misreporting costs k 2 (m−v) 2. The
institution maximisesx(v−φm−λx)− k 2 (m−v) 2 (Assumption 3). Leta= 2λk.
Theorem 3(Optimal speech and its taxonomy).Under Assumption 3, a unique optimum exists iff
a > φ2 (otherwise the objective is unbounded), and then m∗ =ψv and x∗ =χv with ψ= a−φ a−φ2
3

shading
falsealarm
exaggerate
no optimum
truth
virality
0 0.5 1 1.5
0
1
2
crowd credulityφ
deterrencea= 2λk
a
1.6 1.8 2 2.2 2.4
0
0.5
1
truth2-cyclechaos
deterrencea= 2λk
long-run credulityφ t
b
Figure 2:a: regime map of Theorem 3. False alarms occupy the thin wedge φ2 < a < φ, and
virality moves a market to the right.b: bifurcation diagram of adaptive trust (Theorem 5). Dots
show the numerically computed long-run attractor, and dashed curves show the closed-form 2-cycle.
Trust converges to truth only when a >2; below a= 5 3 period-doubling continues, and simulations suggest chaos.
and χ= k(1−φ) a−φ2 . For a > φ2, φ >0 and good news (v >0) there are four regimes: (i)truth( φ= 1 :
ψ= 1 , χ= 0 ); (ii)shading( φ <1, a > φ: 0< ψ <1, χ >0); (iii)false alarm( φ2 < a < φ <1:
ψ <0< χ, talk it down and buy); and (iv)exaggeration( φ >1: ψ >1, χ <0, talk it up and sell).
On the boundarya=φ <1the institution says nothing,ψ= 0.
Sketch.The objective is a concave quadratic iff its Hessian has determinant a−φ 2 >0 . The
first-order conditions giveψandχ, and the regimes follow from the signs ofa−φand1−φ.
Theorem 4(Say–Do covariance identity).Under Assumption 3, let the message rule m(v) be
arbitrary and the trade optimal given the message. Then r=λx−φε pathwise, so for any
distribution ofv,
Cov(r,˜m) =λCov(x,˜m)−φ σ2 ε ,E[r|x] =λx.
In the equilibrium of Theorem 3,Cov(x,˜m) =ψχσ2 v <0 exactly in the false-alarm and exaggeration
regimes.
Sketch.Given its message, the institution’s optimal trade solves v−φm= 2λx ; substituting into
r=v−φ(m+ε)−λx gives the pathwise identity. Theorem 4 is the paper’s central tool. Both sides
are estimable and no distributional assumption is needed. A negative rolling dCov(Say,Do) says that
an institution’s words should be faded; following them requires λCov(Do,Say)> φσ 2 ε. Deeds are
always followed.
Virality and adaptive trust.If each article moves the price by φ0 and messages spread through a
Hawkes cascade with branching ratio n, effective credulity is φ=φ 0/(1−n) . Virality then decides
which manipulation appears: false alarms in deep markets (a <1) and exaggeration in shallow ones
(a >1), each inside an explicit window of the echo share (Proposition 18). If instead the crowd
re-estimates its credulity each round as the regression slope of value on (noiseless) messages, then
φt+1 =F a(φt) with Fa(φ) = (a−φ 2)/(a−φ) , on the admissible set where φ2 < a, φ̸=a and
ψ(φ)̸= 0. Trust then behaves like a predictor that is retrained on the data its own use generates.
Theorem 5(Credibility cycles).Under the learning rule above, truth ( φ= 1 ) is the unique admissible
fixed point for a >1, and it is locally stable iff λk >1. For 1< a <2 there is a unique 2-cycle
φ± = 1 2  a± p a(2−a)  that alternates between shading and exaggeration, with multiplier 5a−9 a−1 .
It is locally stable iff 5 6 < λk <1. It is born from truth in a flip bifurcation at a= 2 and loses
stability in a second flip ata= 5 3.
4

4 Measuring the voices
4.1 Echo: semantic declustering
Articles about an asset arrive at times τ1 <· · ·< τN with embeddings zj ∈S D−1. We model them
as a Hawkes process with baselineµand kernelg. In its cluster representation, each article is either
an immigrant (news) or an offspring of an earlier article (echo) (Hawkes and Oakes, 1974). We let
an echo’s embedding depend on its parent’s, z∼f(· |z l), for example von Mises–Fisher with
concentration κ, while news has density f0 (Assumption 5). Let π(j) denote the parent of article j,
withπ(j) = 0for news.
Theorem 6(Semantic declustering).Under Assumption 5, given all times and embeddings, the
parent labels are independent, with
P(π(j) = 0| ·) =µf0(zj) Λj ,P(π(j) =l| ·) = g(τj −τ l)f(z j |z l) Λj ,
where Λj =µf 0(zj) + P l<j g(τj −τ l)f(z j |z l). Consequently, writing psem j =µf 0(zj)/Λj:
(i) if each sentiment sj is a function of zj (for example ⟨ws,z j⟩), then snew = P j psem j sj is the
MMSE estimate of total news sentiment; (ii) EH(π(j)| T,z)≤EH(π(j)| T) , so meaning never
increases the expected posterior entropy of parentage.
Sketch.In the cluster representation, the density of a labelled configuration is a product over articles
of the parent stream’s intensity times the mark density, so the posterior over labellings factorises. The
posterior uses only each article’s past, so the split is causal. It costs O(N) per article, and κ is fitted
by maximum marked likelihood. (In our simulator echoes copy their parent’s sentiment, so condition
(i) holds only approximately.)
4.2 Consequence: return-aligned embeddings
For documents with embeddings zj and post-event outcome vectors ρj ∈R M (returns at several
horizons, volume, implied volatility), let Sjk =⟨z j,z k⟩ and Djk =∥ρ j −ρ k∥2. Define soft targets
and model probabilities over neighboursk̸=jand a soft-InfoNCE loss:
qjk ∝e −Djk /2b2 , p jk (Z)∝e Sjk /τ ,L(Z) =− X
j
X
k̸=j
qjk logp jk (Z).
This is the loss of stochastic neighbour embedding (Hinton and Roweis, 2002), with market outcomes
playing the role of the input space.
Theorem 7(When the bound is attained). L(Z)≥ P j H(q j·), with equality iff Sjk =c− τ 2b2 Djk
for a constant c and all j̸=k . At equality ∥zj −z k∥2 = 2(1−c) + τ b2 ∥ρj −ρ k∥2, an increasing
affine function of squared outcome distance, so nearest neighbours in embedding space are nearest
neighbours in outcome space. (Equality requires this geometry to be realisable onS D−1.)
Sketch.Per anchor, the loss equals H(q j·) + KL(qj·∥pj·). Equality forces the logits to differ from
−Djk /2b2 by an anchor constant, and the symmetry of S and D makes the constants equal. In
practice training never reaches the bound, but the leftover loss can still certify some rankings.
Theorem 8(Neighbour certificate).For any embedding Z, let ϵj := KL(qj·∥pj·(Z)) be the excess
loss at anchor j. For k, l̸=j , the embedding ranks k closer to j than l if (i) qjk −q jl > p2ϵj
(Pinsker), or if (ii)q jk > qjl and
∆jkl :=q jk log 2qjk qjk +q jl +q jl log 2qjl qjk +q jl > ϵj.
Condition (i) implies (ii), and (ii) is the weakest condition valid for every distribution within KL
distanceϵ j ofq j·: ifϵ j ≥∆ jkl, one such distribution tieskandl.
Because targets are of order 1/N, form (ii) tolerates an excess loss at least 1/(qjk +q jl)≈N/2
times larger than form (i). The proof is a data-processing argument on a three-cell coarse-graining
(Section C).
5

Algorithm 1Say–Echo–Do scoring of one event (all inputs available at decision time)
Require: articles (τj,z j, sj)j≤N (the statement is j= 1 ); statement Say; disclosed positioning Do; paths of
positioning X and tone; the firm’s past (Say,Do) ; Hawkes (µ, g)and κ fitted on past events; window W ,
thresholdc
1:forj= 1, . . . , Ndosemantic declustering, Theorem 6
2:Λ j ←µf 0(zj) + P l<j g(τj −τ l)f(z j |z l);p j ←µf 0(zj)/Λj
3:s new ← P j>1 pjsj;s echo ← P j(1−p j)sj Corollary 2
4:A← price reaction − narrative-implied move (fitted on past events, or analogues in the return-aligned
space)
5:ˆc←corr(Say,Do)over the lastWevents;dsgn← −1ifˆc <−celse+1Theorem 4
6:A ± ←sgn(X T −X 0)· AT (X,−tone)Theorem 9
7:returnDfrom (1), with weights fitted on past events
4.3 Who moved first: Lévy area
For paths X (positioning) and Y (headline gloom), the Lévy area AT = 1 2 R T 0 (Xu −X 0)dY u −
(Yu −Y 0)dX u is the antisymmetric level-two signature term.
Theorem 9(Expected area identifies lead–lag).Let (X, Y)be zero-mean and jointly weakly sta-
tionary with C 1 (mean-square) paths and cross-covariance C(h) =E[X sYs+h]∈C 1. Then
E[AT ] =T C′(0)− 1 2  C(T)−C(−T)  . If moreover Yt =γX t−ℓ +Z t with ℓ̸= 0 , Z stationary
and independent of X, and X has an even C 1 autocovariance R with R′(h)<0 for h >0, then the
long-run area rate has sign sgn(γℓ). If γ >0 (gloom follows positioning), a positive area means
money moved first.
4.4 From signals to a decision
Each measurement enters a composite score with the sign a result assigns to it:
D=ω 1snew −ω 2secho +ω 3 Do+dsgnω4 Say+ω 5A+ω 6A±,(1)
where dsgnis the sign of the rolling Say–Do covariance (Theorem 4), A is absorption and A± is the
Lévy area signed by the direction of the position change. Algorithm 1 computes every term causally.
The weights should be fitted on past data, and a fitted weight whose sign contradicts the theory is a
diagnostic that an assumption fails. Section D adds a causal regime filter, a detection bound, adaptive
conformal intervals and Kelly sizing under estimation risk.
5 Experiments
We test the tools where the truth is known and every quantity must be estimated from what an
econometrician would see. We ask five questions.Q1: can echo be separated from news, and do
the two carry opposite signs?Q2: does the Say–Do covariance find the institutions whose words
should be faded?Q3: do absorption and lead–lag carry their predicted signs?Q4: do theory-based
features improve forecasts?Q5: do return-aligned embeddings organise text by consequence, and is
the certificate informative?
Simulated market.There are 300 firms with 60 events each. Each firm hosts one institution, drawn
with equal probability as non-strategic (it reports value and does not trade) or strategic in the shading,
false-alarm or exaggeration regime of Theorem 3. At each event, value is v∼ N(0,1), the institution
trades χv over the ten days before it speaks, and then it publishes Say=ψv+noise . The media
publish a Hawkes cascade in which the statement and independent news items are immigrants. Echoes
copy their parent’s sentiment and, through a von Mises–Fisher perturbation (κ= 30 , D= 16 ), its
embedding. The branching ratio is set so that effective credulity is φ. The crowd prices every article,
the forward return is v−p plus heavy late-arriving noise, and positions are disclosed with error.
Methods see article times, embeddings and sentiment, statements, noisy positions, price reactions
and daily paths. They never see value, regimes, parentage or parameters. The one exception is a
supervised false-alarm detector trained on labelled training events.
6

Table 1: Theory tests on test events of the main market (five seeds). t: firm-clustered, averaged over
seeds; last column: seeds with |t|>2 and the predicted sign. Controls: Say and Do for the first two
rows, Do for the third.
Regressor Source PredictiontAs predicted
Echo sentiments echo Corollary 2−(fade)−8.05/5
News sentiments new Corollary 2+(follow)+2.13/5
Say, where rollingcorr(Say,Do)<−0.2Theorem 4−(fade)−3.34/5
Absorption, institution trades Theorem 14 either−11.1–
Absorption, institution does not trade Theorem 14− −3.64/5
Signed Lévy area Theorem 9+ +1.01/5
0.5 0.75 1
all five
Say–Do corr.
Say×Do
Lévy area
echo share
absorption
AUC (false-alarm events)
a
5 10 20 40
0.8
0.9
1
past eventsW
switch accuracy
b
1 10 100
0
0.5
1
training step
share / IC
same consequence
same topic
analog IC
c
Figure 3:a: AUC for flagging false-alarm events, for each feature alone (reported as max(AUC,1−
AUC)) and for a detector on all five trained with true labels (mean ± s.d., five seeds; dashed line:
chance).b: accuracy of the Say–Do switch in labelling words to fade.c: return-aligned training
moves headlines’ ten nearest neighbours from sharing a topic to sharing a consequence; the dashed
line is the analog IC of TF-IDF neighbours (three seeds).
Protocol.For each firm, the first 30 events are for training and the last 30 for testing. Hawkes
parameters, κ, the narrative-implied move, and all model weights and standardisations use training
events only. We report the cross-sectional information coefficient (IC) per test period with its t-
statistic, and firm-clustered regressions for the theory tests. The main market uses 5 seeds, robustness
variants 3, and sample-size variants 2: 29 distinct markets in all. The noise scale was calibrated
once so that a linear model on the raw voices reaches an IC of about 0.17. Forecasting with the true
mispricingv−pthen reaches only0.181, so Q4 has little headroom. Full details are in Section F.
Q1: echo is separable, and fading it pays.Semantic declustering recovers the echo concentration
( ˆκ= 30.27±0.07, true 30) and the echo share (0.422, true 0.427). Timing alone gives 0.368 against
0.430 on the same markets, because it mistakes echoes for news. Echo sentiment predicts returns
with a significantly negative sign in all 29 markets (Table 1). Meaning sharpens the test: on identical
markets its t-statistic weakens from −7.5 to −6.0 when timing alone is used. News carries the
predicted positive sign in every market, but it is significant in only21of29.
Q2: the Say–Do covariance finds the manipulators.The rolling Say–Do correlation alone
separates false-alarm events from all others with an AUC of 0.895. A supervised detector that adds
four features reaches 0.934±0.010 (Figure 3a). Used as the switch in (1), the correlation labels
a firm’s words correctly (fade or follow) 85% of the time from 5 past events and 96% from 40
(Figure 3b). In the flagged group, statements predict returns with the sign reversed. Two caveats
matter for real data. Controlling for echo sentiment removes this effect ( t= +0.2 ; −0.3 with
news also controlled), because a statement’s price impact travels through its echoes. And Do’s own
coefficient is imprecise, because Say and Do are nearly collinear within strategic regimes and because
the institution’s price impact is small next to later information.
7

Table 2: Out-of-sample IC, main market (5 seeds;
oraclev−p:0.181).
Forecast IC
Follow the tone−0.119±0.013
Follow Say−0.047±0.006
Theory composite, unit weights0.049±0.010
Fade the price reaction0.162±0.018
Boosting: raw voices0.109±0.015
Boosting: raw + theory features0.118±0.019
Linear: raw voices0.169±0.017
Linear: raw + theory features0.171±0.018
Table 3: Text benchmark (3 seeds). Week-ahead
analog IC; share of 10 nearest neighbours with
the same consequence (chance 0.25). Ceiling:
0.936.
Method IC Conseq.
TF-IDF neighbours0.192 0.506
Random 16-d projection0.039 0.327
Ridge on words−0.019–
Boosting on words0.837–
Return-aligned, 16-d0.892 1.000
Q3: absorption tests the narrative model; lead–lag is weak.Estimated absorption predicts strong
reversal in all 29 markets, even where the theory allows continuation. Decomposing it shows why.
Only 12–19% of its variance is the institution’s trade and 2–4% is noise trading. Most of the rest is
narrative misfit: a linear narrative model ignores that a statement’s impact scales with the size of its
echo cascade. With the true absorption λ(x+u) , the coefficient is insignificant in both groups, so
these experiments do not test Theorem 14. They do show that its sign must be estimated. The signed
Lévy area has the predicted sign in27of29markets but is significant in only9.
Q4: little forecasting headroom.Following the tone or institutional statements loses money, and
fading the price reaction is a strong baseline (Table 2). Adding theory features to a linear model
changes the IC by at most about 0.005 in any seed. For boosting they help a little, raising the IC from
0.109 to 0.118 and improving it in 18 of 29 markets. The unit-weight composite is weak ( 0.049),
mostly because its absorption term has the wrong sign here. With the oracle at 0.181, this comparison
has little power. It is consistent with Theorem 1, which says the optimal forecast is linear in the
voices, although the simulated price is only approximately linear in them (Q3). The theory’s clearest
contributions here are its signs and the diagnostics of Q1 and Q2.
Q5: return-aligned embeddings organise text by consequence.In a synthetic corpus, each
headline mixes irrelevant topic words, tone words and one cue that decides whether the move reverses
or continues. We train a 16-dimensional projection of TF-IDF vectors with L (Section G). The ten
nearest neighbours of a test headline switch from sharing its topic (85% under TF-IDF) to sharing
its consequence (100%) (Figure 3c). The analog forecast reaches an IC of 0.892 against a ceiling of
0.936 (Table 3). Ridge regression fails because the outcome is a tone×cue interaction. The certificate
never made a wrong claim, but it certified nothing under realistic outcome noise: the excess loss
per anchor stays at 0.02–0.03 while targets are of order 0.007. With noise-free outcomes and sharp
targets, form (ii) certifies45%of comparisons, and form (i) still certifies none.
Robustness.Table 4 changes one assumption at a time. Fat-tailed values, power-law echo delays,
partial disclosure and a saturating crowd leave the echo and news signs intact, and detection stays at
an AUC of at least 0.857. The controlled reversed-words test, already insignificant in the reference
market, takes the wrong sign in all three seeds under a saturating crowd (Section G). Ignoring
meaning, or weak meaning (κ= 5 ), underestimates the echo share by about six points and weakens
the echo test.
6 Limitations and conclusion
Limitations.The price-formation results are exact in linear–Gaussian economies with reduced-
form crowd pricing, and they pin down signs and sufficient statistics, not magnitudes. The simulator
shares the theory’s structure and is far more predictable than any real market, so our experiments
show that the toolscanwork, not that they will. The false-alarm detector needs labels that real data
provide only after the fact. Absorption needs a nonlinear narrative model before its sign can be
8

Table 4: Robustness (three seeds each; “reference” is the main market on the same seeds). IC: linear
model with theory features.t: firm-clustered. Echo share: estimated (true).
Variant IC echotnewstAUC echo share
Reference0.190−7.5 +3.6 0.941 0.425(0.430)
Fat-tailed values (t3)0.141−8.1 +2.4 0.924 0.423(0.428)
Saturating crowd0.101−5.9 +3.2 0.942 0.425(0.430)
Power-law echo delays0.177−7.9 +2.1 0.939 0.417(0.429)
30% of trade disclosed, noisier0.191−7.5 +4.1 0.857 0.425(0.430)
Weak meaning (κ= 5)0.188−7.2 +1.9 0.941 0.373(0.429)
Timing only (reference markets)0.189−6.0 +2.6 0.940 0.368(0.430)
trusted, and the certificate needs outcome targets smoother than raw returns. The text benchmark is
synthetic, and the week-ahead outcome is fully determined by two words.
Conclusion.Treating financial text as a strategic signal changes what should be learned from it.
Words whose covariance with deeds is negative should be faded, and so should repetition. The echo
prediction held in all 29 simulated markets, and the Say–Do switch in four of five main-market seeds.
The natural next step is a point-in-time study on real disclosures, echo cascades and positioning,
testing the echo and Say–Do predictions first.
Broader impact.These tools are meant for detection, research and investor protection, and they use
public information only. They could help regulators and investors discount manipulative narratives.
The same understanding could in principle help someone design narratives that move prices, which is
market manipulation and illegal. A strategic reading is never evidence that anyone lied (Section H).
References
Araci, D. (2019). FinBERT: Financial sentiment analysis with pre-trained language models. arXiv:1908.10063.
Bénabou, R., and Laroque, G. (1992). Using privileged information to manipulate markets: Insiders, gurus, and
credibility.Quarterly Journal of Economics, 107(3), 921–958.
Bennett, S., Cucuringu, M., and Reinert, G. (2022). Lead–lag detection and network clustering for multivariate
time series with an application to the US equity market.Machine Learning, 111, 4497–4538.
Bhattacharyya, A. (1943). On a measure of divergence between two statistical populations defined by their
probability distributions.Bulletin of the Calcutta Mathematical Society, 35, 99–109.
Bouchaud, J.-P., Bonart, J., Donier, J., and Gould, M. (2018).Trades, Quotes and Prices: Financial Markets
Under the Microscope. Cambridge University Press.
Chan, W. S. (2003). Stock price reaction to news and no-news: Drift and reversal after headlines.Journal of
Financial Economics, 70(2), 223–260.
Chevyrev, I., and Kormilitzin, A. (2016). A primer on the signature method in machine learning.
arXiv:1603.03788.
Crawford, V . P., and Sobel, J. (1982). Strategic information transmission.Econometrica, 50(6), 1431–1451.
Damrich, S., Böhm, N., Hamprecht, F. A., and Kobak, D. (2023). From t-SNE to UMAP with contrastive
learning.International Conference on Learning Representations.
Du, N., Farajtabar, M., Ahmed, A., Smola, A. J., and Song, L. (2015). Dirichlet–Hawkes processes with applica-
tions to clustering continuous-time document streams.Proceedings of the 21st ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining, 219–228.
Dufumier, B., Gori, P., Victor, J., Grigis, A., Wessa, M., Brambilla, P., Favre, P., Polosan, M., McDonald,
C., Piguet, C. M., Phillips, M., Eyler, L., and Duchesnay, E. (2021). Contrastive learning with continuous
proxy meta-data for 3D MRI classification.Medical Image Computing and Computer Assisted Intervention
(MICCAI), LNCS 12902, 58–68.
9

Evans, G. W., and Honkapohja, S. (2001).Learning and Expectations in Macroeconomics. Princeton University
Press.
Ezekiel, M. (1938). The cobweb theorem.Quarterly Journal of Economics, 52(2), 255–280.
Gibbs, I., and Candès, E. (2021). Adaptive conformal inference under distribution shift.Advances in Neural
Information Processing Systems, 34.
Glasserman, P., and Lin, C. (2023). Assessing look-ahead bias in stock return predictions generated by GPT
sentiment analysis. arXiv:2309.17322.
Hardt, M., Megiddo, N., Papadimitriou, C., and Wootters, M. (2016). Strategic classification.Proceedings of the
ACM Conference on Innovations in Theoretical Computer Science (ITCS), 111–122.
Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy.Nature, 585,
357–362.
Hawkes, A. G. (1971). Spectra of some self-exciting and mutually exciting point processes.Biometrika, 58(1),
83–90.
Hawkes, A. G., and Oakes, D. (1974). A cluster process representation of a self-exciting process.Journal of
Applied Probability, 11(3), 493–503.
He, X., Rekatsinas, T., Foulds, J., Getoor, L., and Liu, Y . (2015). HawkesTopic: A joint model for network
inference and topic modeling from text-based cascades.Proceedings of the 32nd International Conference on
Machine Learning, PMLR 37, 871–880.
Hinton, G. E., and Roweis, S. (2002). Stochastic neighbor embedding.Advances in Neural Information Process-
ing Systems, 15.
Hu, T., Liu, Z., Zhou, F., Wang, W., and Huang, W. (2023). Your contrastive learning is secretly doing stochastic
neighbor embedding.International Conference on Learning Representations.
Kailath, T. (1967). The divergence and Bhattacharyya distance measures in signal selection.IEEE Transactions
on Communication Technology, 15(1), 52–60.
Kartik, N., Ottaviani, M., and Squintani, F. (2007). Credulity, lies, and costly talk.Journal of Economic Theory,
134(1), 93–116.
Ke, Z. T., Kelly, B. T., and Xiu, D. (2019). Predicting returns with text data. NBER Working Paper 26186.
Khosla, P., Teterwak, P., Wang, C., Sarna, A., Tian, Y ., Isola, P., Maschinot, A., Liu, C., and Krishnan, D. (2020).
Supervised contrastive learning.Advances in Neural Information Processing Systems, 33.
Kidger, P., Bonnier, P., Perez Arribas, I., Salvi, C., and Lyons, T. (2019). Deep signature transforms.Advances in
Neural Information Processing Systems, 32.
Kogan, S., Moskowitz, T. J., and Niessner, M. (2023). Social media and financial news manipulation.Review of
Finance, 27(4), 1229–1268.
Kyle, A. S. (1985). Continuous auctions and insider trading.Econometrica, 53(6), 1315–1335.
Llorente, G., Michaely, R., Saar, G., and Wang, J. (2002). Dynamic volume-return relation of individual stocks.
Review of Financial Studies, 15(4), 1005–1047.
Lopez-Lira, A., and Tang, Y . (2023). Can ChatGPT forecast stock price movements? Return predictability and
large language models. arXiv:2304.07619.
Lyons, T. J. (1998). Differential equations driven by rough signals.Revista Matemática Iberoamericana, 14(2),
215–310.
May, R. M. (1976). Simple mathematical models with very complicated dynamics.Nature, 261, 459–467.
Mei, H., and Eisner, J. (2017). The neural Hawkes process: A neurally self-modulating multivariate point process.
Advances in Neural Information Processing Systems, 30.
Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous-time case.Review of
Economics and Statistics, 51(3), 247–257.
10

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V ., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P.,
Weiss, R., Dubourg, V ., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., and Duchesnay,
E. (2011). Scikit-learn: Machine learning in Python.Journal of Machine Learning Research, 12, 2825–2830.
Perdomo, J. C., Zrnic, T., Mendler-Dünner, C., and Hardt, M. (2020). Performative prediction.Proceedings of
the 37th International Conference on Machine Learning, PMLR 119, 7599–7609.
Tetlock, P. C. (2007). Giving content to investor sentiment: The role of media in the stock market.Journal of
Finance, 62(3), 1139–1168.
van Bommel, J. (2003). Rumors.Journal of Finance, 58(4), 1499–1520.
van den Oord, A., Li, Y ., and Vinyals, O. (2018). Representation learning with contrastive predictive coding.
arXiv:1807.03748.
Virtanen, P., Gommers, R., Oliphant, T. E., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific
computing in Python.Nature Methods, 17, 261–272.
Zha, K., Cao, P., Son, J., Yang, Y ., and Katabi, D. (2023). Rank-N-Contrast: Learning continuous representations
for regression.Advances in Neural Information Processing Systems, 36.
Zhuang, J., Ogata, Y ., and Vere-Jones, D. (2002). Stochastic declustering of space-time earthquake occurrences.
Journal of the American Statistical Association, 97(458), 369–380.
11

Appendix
The appendix contains the full model and the proofs (Sections A to C), the decision layer (Section D),
numerical checks of every closed form (Section E), the complete experimental protocol and results
(Sections F and G) and a discussion of broader impacts (Section H). Results stated in the main text
are restated here with their original numbers.
A The three-voice market: model and proofs
A.1 Auxiliary lemmas
Lemma 10(Gaussian conditioning).If (a,b) is jointly Gaussian with Var(b)≻0 , then E[a|b] =
Ea+ Cov(a,b) Var(b) −1(b−Eb) and Var(a|b) = Var(a)−Cov(a,b) Var(b) −1 Cov(b,a) .
The same formulas hold conditionally on a further jointly Gaussian vector.
Proof. Let e=a−Ea−Cov(a,b) Var(b) −1(b−Eb) . Then Cov(e,b) = 0 , and joint Gaussianity
makes e independent of b. Hence E[a|b] is as stated, and Var(a|b) = Var(e) , which expands to
the stated formula.
Lemma 11(Bhattacharyya coefficient of Gaussians).For pi =N(m i,Σ) on Rd, R √p0p1 =
exp

− 1 8 (m1 −m 0)⊤Σ−1(m1 −m 0)  .
Proof. With ¯m= (m 0 +m 1)/2 and δ=m 1 −m 0, the identity 1 2 (x−m 0)⊤Σ−1(x−
m0) + 1 2 (x−m 1)⊤Σ−1(x−m 1) = (x− ¯m)⊤Σ−1(x− ¯m) + 1 4 δ⊤Σ−1δ gives √p0p1 =
N(x; ¯m,Σ)e −δ⊤Σ−1δ/8. Integrate overx.
A.2 Model
Assumption 1(Fundamentals and public signals).The asset’s terminal value is v∼ N(0, σ2 v). A
vector ofKpublic channels is observed,
y=hv+ν∈R K,ν∼ N(0,Σ ν)independent ofv,
with Σy :=σ 2 vhh⊤ + Σν ≻0 . Channels are labelled by voice: institutional statements (Say),
independent news, and media repetition (Echo).
Assumption 2(Price formation).Noise traders submit u∼ N(0, σ2 u), independent of (v,ν) . In-
formed traders who know v submit x=β(v−p) with β >0. The price is set by a narrative-sensitive
crowd and linear impact:
p=φ ⊤y+λ(x+u), λ >0,
whereφ∈R K collects the crowd’snarrative multipliers.
Throughout, κ := (1 +λβ) −1 ∈(0,1) , the Bayes weights are w⋆ :=σ 2 vΣ−1 y h (so that E[v|y] =
w⋆⊤y), andσ 2 v|y := Var(v|y) =σ 2 v −σ 4 vh⊤Σ−1 y h. The forward return isr :=v−p.
Lemma 12(Price and return).Under Assumptions 1 and 2,
p=κ

φ⊤y+λβv+λu  , r=κ  v−φ ⊤y−λu  .
Proof. Substituting x=β(v−p) gives p(1 +λβ) =φ ⊤y+λβv+λu . Then r=v−p=
κ

(1 +λβ)v−φ ⊤y−λβv−λu  =κ(v−φ ⊤y−λu).
A.3 Follow or fade
Theorem 1(Follow or fade).Under Assumptions 1 and 2, E[r|y] =κ(w ⋆ −φ) ⊤y and Var(r|
y) =κ 2(σ2 v|y +λ 2σ2 u) =: ς 2, where σ2 v|y = Var(v|y) . The return loads negatively on channel k
(fade) iffφ k > w⋆ k, and positively (follow) iffφ k < w⋆ k.
12

v
Saym
Newsn
Echoe
Dox
pricep u
x=β(v−p)
garbling ofm
Figure 4: Information structure. The echo channel is a downstream garbling of the institutional
statement, while news is an independent signal of v. Informed demand reacts to the price (dashed),
and the price aggregates every channel.
Proof. By Lemma 12, r=κ(v−φ ⊤y−λu) . Joint Gaussianity gives E[v|y] = Cov(v,y)Σ −1 y y=
σ2 vh⊤Σ−1 y y=w ⋆⊤y, and E[u|y] = 0 by independence. For the variance, r−E[r|y] =
κ

(v−E[v|y])−λu

, and the two terms are independent giveny.
Corollary 2(Fade the echo, follow the news).Under Assumptions 1 and 2: (i) if channel e is a
garbling of the others, e=a ⊤y−e +ξ with ξ∼ N(0, σ2 ξ ), σ2 ξ >0 , independent of (v,y −e, u),
then w⋆ e = 0 and the return loads on e with coefficient −κφe, so any crowd weight on echo
is reversed; (ii) if channel n=v+ν n with νn ∼ N(0, σ2 n) independent of (v,y −n, u), and
s2 := Var(v|y −n)>0 , then w⋆ n =s 2/(s2 +σ 2 n)∈(0,1) , and returns drift in the direction of n
whenever the crowd underweights it,φ n < w⋆ n.
Proof. Part (i). σ(y) =σ(y −e, ξ)and ξ is independent of (v,y −e), so E[v|y] =E[v|y −e], a
linear function of y−e alone. If E[v|y] =w ⋆⊤y=w ′⊤y with w′ e = 0, then (w⋆ −w ′)⊤y= 0
almost surely, so (w⋆ −w ′)⊤Σy(w⋆ −w ′) = 0, and Σy ≻0 forces w⋆ =w ′. Hence w⋆ e = 0, and
Theorem 1 gives the loadingκ(0−φ e).
Part (ii).Conditionally on y−n, v∼ N(µ ′, s2) with µ′ linear in y−n, and n=v+ν n. The
scalar Gaussian update gives E[v|y] =µ ′ + s2 s2+σ2 n (n−µ ′), whose coefficient on n is w⋆ n. Apply Theorem 1.
A.4 The Say–Do gap
Theorem 13(Say–Do gap optimality).In addition to y, the econometrician observes a positioning
proxyˆx=x+ξ x,ξ x ∼ N(0, σ2 x)independent of(v,ν, u). Let
cx := βς 2 β2ς 2 +σ 2x , θ := σ2 x β2ς 2 +σ 2x ∈(0,1].
Then
(i)E[r|y,ˆx] =θ κ(w ⋆ −φ) ⊤y+c x ˆxandVar(r|y,ˆx) =θ ς2 < ς2 wheneverσ 2 x <∞;
(ii) if theSaychannel m=y 1 is overweighted, φ1 > w⋆ 1, the forecast depends on (m,ˆx)only
through theSay–Do gap
Gγ :=γ m−ˆx, γ := θκ(φ1 −w ⋆ 1) cx >0,
entering with coefficient−c x <0.
Proof. By Lemma 12, x=β(v−p) =βr , so ˆx=βr+ξ x. Conditionally on y, (r,ˆx)is Gaussian
with Cov(r,ˆx|y) =βς 2, Var(ˆx|y) =β 2ς 2 +σ 2 x and E[ˆx|y] =βE[r|y] . Gaussian conditioning
13

(Lemma 10) gives
E[r|y,ˆx] =E[r|y] +c x

ˆx−βE[r|y]

= (1−βc x)E[r|y] +c x ˆx,
with 1−βc x =θ , and Var(r|y,ˆx) =ς 2 −c xβς 2 =θς 2. For (ii), the terms in m and ˆxare
−θκ(φ1 −w ⋆ 1)m+c x ˆx=−cx(γm−ˆx).
Say
bullish words
Do(buying)
bearish words
selling
Say = Do
talks bearish, buys
⇒bullish signal
talks bullish, sells
⇒bearish signal
consistent: follow
consistent: follow
a false alarm
gapG
Figure 5: The Say–Do plane. Theorem 13 shows that the optimal forecast is a decreasing function
of the signed distance from the line ˆx=γm. Top-left is the false-alarm zone; bottom-right is the
false-euphoria zone.
A.5 Absorption
Theabsorptionof a narrative shock is the price move net of the narrative-implied move,a :=p−φ ⊤y.
Theorem 14(Absorption sign).Under Assumptions 1 and 2,
E[r|y, a] =E[r|y] +c A

a−E[a|y]

, c A =
β σ2 v|y −λ σ2 u
λ

β2σ2 v|y +σ 2u  .
Absorption therefore predictscontinuationin its own direction if and only if βσ 2 v|y > λσ2 u, and
reversalif and only if βσ 2 v|y < λσ2 u. In the limits, cA = 1/(λβ) when σu = 0 (absorption is sufficient
forr) andc A =−1whenβ= 0(pure noise fully reverts).
Proof. Write ˜v:=v−E[v|y] , independent of u given y. By Lemma 12, r−E[r|y] =κ(˜v−λu) .
Sincea=λ(x+u) =λβr+λu,
a−E[a|y] =λβκ(˜v−λu) +λu=λβκ˜v+λ(1−λβκ)u=λκ(β˜v+u),
using 1−λβκ=κ . Hence Cov(r, a|y) =λκ 2(βσ 2 v|y −λσ 2 u) and Var(a|y) =λ 2κ2(β2σ2 v|y +σ 2 u),
and Lemma 10 givesc A as their ratio. The limits follow by substitution.
Lemma 15(Robustness to a misspecified multiplier).For any ˆφ∈R K, let ˆa:=p− ˆφ⊤y. Then
σ(y,ˆa) =σ(y, a)and henceE[r|y,ˆa] =E[r|y, a].
Proof.ˆa=a+ (φ− ˆφ)⊤yis an invertible affine function ofagiveny, and conversely.
14

Remark16 (Kyle calibration).Plugging in the single-period equilibrium intensities of Kyle (1985),
β=σ u/σv|y and λ=σ v|y /(2σu), gives βσ 2 v|y =σ uσv|y > 1 2 σuσv|y =λσ 2 u and cA = 1 2:
absorption is informative and predicts continuation.
Remark17 (Relation to volume–return dynamics).Theorem 14 is in the spirit of Llorente et al.
(2002), where high-volume returns continue when informed trading dominates and reverse when
hedging dominates. The difference is that we condition on thenarrative: the object is the price move
net of what the public story implied. By Lemma 15, its information content survives misestimation
of the crowd’s multiplier.
B Strategic speech: model and proofs
Assumption 3(Strategic institution).An institution knows v, which has an arbitrary distribution
with mean zero and variance σ2 v <∞ . It publishes a message m and trades x. The public observes
˜m=m+ε , where ε has mean zero and variance σ2 ε and is independent of v. The price is
p=φ˜m+λx , where φ≥0 is the crowd’s effective credulity andλ >0is price impact. Misreporting
costs k 2 (m−v) 2 withk >0(legal, reputational). The institution maximises
J(x, m) =E

x(v−p)|v

− k 2 (m−v) 2 =x(v−φm−λx)− k 2 (m−v) 2.
We writea := 2λkfor thedeterrence–impact product.
Assumption 4(Echo amplification).Each article moves the price by φ0 per unit of message, and the
message propagates through a Hawkes cascade with branching ratio n∈[0,1) . By Proposition 23,
the expected cascade size is(1−n) −1, so the effective credulity isφ=φ 0/(1−n).
Theorem 3(Optimal speech and its taxonomy).Under Assumption 3, a unique optimum exists iff
a > φ2 (otherwise the objective is unbounded), and then m∗ =ψv and x∗ =χv with ψ= a−φ a−φ2
and χ= k(1−φ) a−φ2 . For a > φ2, φ >0 and good news (v >0) there are four regimes: (i)truth( φ= 1 :
ψ= 1 , χ= 0 ); (ii)shading( φ <1, a > φ: 0< ψ <1, χ >0); (iii)false alarm( φ2 < a < φ <1:
ψ <0< χ, talk it down and buy); and (iv)exaggeration( φ >1: ψ >1, χ <0, talk it up and sell).
On the boundarya=φ <1the institution says nothing,ψ= 0.
Proof.J is quadratic in (x, m)with Hessian H=

−2λ−φ
−φ−k

. Since −2λ <0 , H is negative
definite iff detH=a−φ 2 >0 . In that case J is strictly concave and its unique maximiser solves the
first-order conditions v−φm−2λx= 0 and −φx−k(m−v) = 0 . Substituting x= (v−φm)/(2λ)
into the second condition gives m(a−φ 2) =v(a−φ) . Then x= (1−φψ)v/(2λ) , and 1−φψ=
a(1−φ)/(a−φ 2) gives χ. If detH <0 , H has a positive eigenvalue with eigenvector d, and
J(td)→ ∞ast→ ∞.
For the taxonomy, take v >0. ψ >0⇐ ⇒a > φ(the denominator is positive); ψ <1⇐ ⇒φ2 <
φ⇐ ⇒φ <1; andsgnχ= sgn(1−φ). Whenφ >1,a > φ 2 > φ, soψ >1.
Theorem 4(Say–Do covariance identity).Under Assumption 3, let the message rule m(v) be
arbitrary and the trade optimal given the message. Then r=λx−φε pathwise, so for any
distribution ofv,
Cov(r,˜m) =λCov(x,˜m)−φ σ2 ε ,E[r|x] =λx.
In the equilibrium of Theorem 3,Cov(x,˜m) =ψχσ2 v <0 exactly in the false-alarm and exaggeration
regimes.
Proof. Given m, the trade maximisesx(v−φm−λx) , so x= (v−φm)/(2λ) , that is, v−φm= 2λx .
Hence r=v−φ(m+ε)−λx= 2λx−λx−φε . Since x and m are functions of v, which is
independent of ε, we have Cov(ε,˜m) =σ 2 ε, and E[ε|x] = 0 . The equilibrium covariance is
Cov(χv, ψv), andψχ <0exactly in regimes (iii) and (iv) of Theorem 3.
15

B.1 Virality
Proposition 18(Manipulation dichotomy).Under Assumptions 3 and 4 with φ0 ∈(0,1) , call a
regimemanipulativeifCov(Say,Do)<0.
(i) If a <1, the only reachable manipulative regime is the false alarm. It occurs if and only if
max{0,1−φ 0/a}< n <1−φ 0/√a.
(ii) If a >1, the only reachable manipulative regime is exaggeration. It occurs if and only if
1−φ 0 < n <1−φ0/√a.
(iii) Ifn >1−φ 0/√a, no interior optimum exists.
Proof.φ=φ 0/(1−n) increases continuously from φ0 to ∞ on [0,1) . The false alarm requires
φ2 < a < φ <1, hence a <1 . Exaggeration requires 1< φ < √a, hence a >1 . The two
are therefore mutually exclusive. The conditions φ > a, φ >1 and φ < √a are equivalent to
n >1−φ 0/a, n >1−φ 0 and n <1−φ 0/√a respectively. For a <1 we have √a <1, so
φ <√aalready impliesφ <1. Part (iii) is Theorem 3.
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7
−2
0
2
false-alarm
window
exagger-
ation
window
truthψ= 1
media branching ration(echo share)
speech slopeψ=∂m ∗/∂v
a= 0.6(deep market)
a= 1.5(shallow market)
Figure 6: Proposition 18 with φ0 = 0.4. As the echo share rises, a deep market (small a) passes
through a false-alarm window where the speech slope turns negative. A shallow market (large a)
instead passes through an exaggeration window with ψ >1. Both windows end where no interior
optimum exists.
B.2 Adaptive trust
Suppose that after each round the crowd resets its credulity to the least-squares slope of value on
message under the previous round’s strategy, a cobweb-type learning rule (Ezekiel, 1938; Evans and
Honkapohja, 2001). With noiseless messagesm t =ψ(φ t)v, this gives
φt+1 = Cov(v, mt) Var(mt) = 1 ψ(φt) =F a(φt), F a(φ) := a−φ 2 a−φ ,
on the admissible setD a ={φ:φ 2 < a, φ̸=a, ψ(φ)̸= 0}.
Theorem 5(Credibility cycles).Under the learning rule above, truth ( φ= 1 ) is the unique admissible
fixed point for a >1, and it is locally stable iff λk >1. For 1< a <2 there is a unique 2-cycle
φ± = 1 2  a± p a(2−a)  that alternates between shading and exaggeration, with multiplier 5a−9 a−1 .
It is locally stable iff 5 6 < λk <1. It is born from truth in a flip bifurcation at a= 2 and loses
stability in a second flip ata= 5 3.
Proof. The theorem collects four facts: (i) φ= 1 is the unique admissible fixed point of Fa when
a >1, and there is none when a≤1 ; (ii) F ′ a(1) =−1/(a−1) , so truth is locally asymptotically
stable iff a >2 , that is, λk >1 ; (iii) for 1< a <2 , Fa has exactly one 2-cycle φ±, with
16

φ− <1< φ +, both points admissible, and multiplier (5a−9)/(a−1) , so the cycle is stable iff
5
3 < a <2, that is, 5 6 < λk <1; along it the market alternates between shading ( φ− <1 ) and
exaggeration (φ+ >1 ); (iv) the multiplier equals 1 at a= 2 and −1 at a= 5 3 (flip bifurcations). We
prove them in turn.
(i) Fa(φ) =φ⇐ ⇒a−φ 2 =aφ−φ 2 ⇐ ⇒φ= 1 . Admissibility of φ= 1 requires
1< a . (ii) F ′ a(φ) = (a−2aφ+φ 2)/(a−φ) 2, so F ′ a(1) = (1−a)/(a−1) 2 =−1/(a−1) ,
and |F ′ a(1)|<1⇐ ⇒a >2 . (iii) Using a−F a(φ) = (a 2 −aφ−a+φ 2)/(a−φ) , a direct
computation gives
Fa(Fa(φ))−φ= −a(φ−1)

2φ2 −2aφ+a 2 −a 
(a−φ) 2  a−F a(φ)  .
The quadratic factor has rootsφ±, which are real and distinct from1 for 1< a <2(at φ= 1 it equals
(a−1)(a−2)̸= 0 ). They are not fixed points, so they form the unique 2-cycle, and φ− <1< φ +
because φ± = 1 only at a∈ {1,2}. For admissibility, φ2 ± =a  1± p a(2−a)  /2< a since
a(2−a)<1 for a̸= 1 ; φ± < asince
p
a(2−a)< a⇐ ⇒a >1 ; and ψ(φ±)>0 . For
the multiplier, on the cycle φ2 =aφ−(a 2 −a)/2 , so the numerator of F ′ a is a(3−a−2φ)/2 .
Vieta’s formulas give φ+ +φ − =a and φ+φ− = (a 2 −a)/2 . Then (3−a−2φ +)(3−a−
2φ−) = 5a 2 −14a+ 9 = (5a−9)(a−1) and (a−φ +)(a−φ −) =a(a−1)/2 . Hence
F ′ a(φ+)F ′ a(φ−) = (a2/4)(5a−9)(a−1) a2(a−1)2/4 = 5a−9 a−1 . For 1< a <2, |5a−9|< a−1⇐ ⇒ 5 3 < a <2.
(iv) Ata= 2,
p
a(2−a) = 0and the multiplier equals1. Ata= 5 3 it equals−1.
Remark19 (Relation to reputation models).Bénabou and Laroque (1992) obtain credibility dynamics
from Bayesian updating about a random honest type. Here the dynamics arise from a deterministic
cobweb in credulity, and the thresholds λk= 1 and λk= 5 6 are explicit. The mechanism is the same
as the period-doubling route to chaos in simple nonlinear maps (May, 1976). The prediction is new
and testable: the rolling Say–Do covariance should be negatively autocorrelated in markets where the
product of price impact and misreporting cost is moderate.
C Measurement: proofs and additional results
C.1 Hawkes processes and declustering
Let articles about an asset arrive at times 0< τ1 <· · ·< τN ≤T with sentiment marks s1, . . . , sN .
Definition 20(Linear Hawkes process).A simple point process on [0, T]with conditional intensity
λ(t) =µ+
X
τl<t
g(t−τ l), µ >0, g≥0, n :=
Z ∞
0
g(s)ds <1.
For the exponential kernelg(s) =αe −βgs, the branching ratio isn=α/β g.
By the cluster representation (Hawkes and Oakes, 1974), the process is the superposition of an
immigrant Poisson stream of rate µ (news) and, for each point τl, an offspring Poisson stream of rate
g(· −τl) on (τl, T](echo). Let π(j)∈ {0,1, . . . , j−1}denote the parent of article j, with π(j) = 0
meaning immigrant.
Proposition 21(Posterior parentage factorises; cf. Zhuang et al., 2002).Conditionally on the full
sampleT={τ 1, . . . , τN }on[0, T], the parent labelsπ(1), . . . , π(N)are independent, with
P

π(j) = 0| T

= µ λ(τj) =: pj,P  π(j) =l| T  = g(τj −τ l) λ(τj) , l < j.
Proof. Write ρ0(t) =µ and ρl(t) =g(t−τ l)1{t > τl}. In the cluster representation, a labelled
configuration is a realisation of the independent Poisson streams, so its density with respect to the
reference measure of labelled configurations is the product of the Poisson likelihoods of the streams,
Y
k
h
exp

−
Z T
0
ρk
 Y
j:π(j)=k
ρk(τj)
i
= exp

−
Z T
0
λ(t)dt
 NY
j=1
ρπ(j) (τj),
17

time
downgrade
copies, reposts, reaction pieces
new data new data
time
story rateλ(t)
baselineµ
new information echo (triggered)
Figure 7: Echo versus news. Top: each new article (blue) triggers a cascade of echoes (red). Bottom:
the intensity jumps with every arrival and decays to the baselineµ. Proposition 21 assigns each article
its exact posterior probability of being news.
because P k ρk(t) =λ(t) . Summing over labellings, the product factorises over j, and P k ρk(τj) =
λ(τj) recovers the standard Hawkes likelihood e−
R
λ Q
j λ(τj). Dividing, the posterior of the
labelling is Q j ρπ(j) (τj)/λ(τj), a product of independent categorical laws.
Remark22.The posterior uses only the past of τj, although it conditions on the whole sample: future
arrivals are informative abouttheirparents, not about π(j). The echo split is therefore causal and
free of look-ahead (cf. Zhuang et al., 2002).
Proposition 23(Branching ratio is the long-run echo share).For the stationary process ( n <1), the
mean intensity isΛ =µ/(1−n), and the long-run fraction of articles that are echoes equalsn.
Proof. Each immigrant founds a Galton–Watson cluster whose generations have expected sizes
1, n, n2, . . ., so its expected total size is (1−n) −1. Immigrants arrive at rate µ, so articles arrive
at rate Λ =µ/(1−n) (equivalently, stationarity gives Λ =µ+ Λ
R
g). The immigrant fraction is
µ/Λ = 1−n.
Proposition 24(MMSE news–echo split).Assume that, given T , the marks are independent of the
labels. Then the minimum-mean-square-error estimates of the news and echo sentiment totals are
snew :=E h X
j
1{π(j) = 0}s j

 T,s i = X
j
pjsj, s echo = X
j
(1−p j)sj.
Proof. Conditional expectation minimises mean-square error. By linearity and the assumption,
E[1{π(j) = 0}s j | T,s] =sjP(π(j) = 0| T) =p jsj, using Proposition 21.
C.2 Semantic declustering
Assumption 5(Semantically marked cascade).In the cluster representation, immigrant articles carry
embeddings z∼f 0 independently, and an offspring of article l carries z∼f(· |z l), for example
the von Mises–Fisher density f(z|z l) =C D(κ)e κ⟨z,z l⟩ on SD−1. Marks are conditionally
independent given the parent labels.
Theorem 6(Semantic declustering).Under Assumption 5, given all times and embeddings, the
parent labels are independent, with
P(π(j) = 0| ·) =µf0(zj) Λj ,P(π(j) =l| ·) = g(τj −τ l)f(z j |z l) Λj ,
18

where Λj =µf 0(zj) + P l<j g(τj −τ l)f(z j |z l). Consequently, writing psem j =µf 0(zj)/Λj:
(i) if each sentiment sj is a function of zj (for example ⟨ws,z j⟩), then snew = P j psem j sj is the
MMSE estimate of total news sentiment; (ii) EH(π(j)| T,z)≤EH(π(j)| T) , so meaning never
increases the expected posterior entropy of parentage.
Proof. As in Proposition 21, the density of a labelled configuration is the product of the stream
likelihoods times the mark densities, e−
R T
0 λ Q j ρπ(j) (τj)f π(j) (zj), where f0 is the immigrant mark
density and fl =f(· |zl). This factorises over j; summing over labellings gives e−
R
λ Q
j Λj, and
the posterior is the product of the stated categorical laws. For (i), marks are now conditioned on,
so no independence assumption is needed: E[1{π(j) = 0}s j | T,z] =s j psem j whenever sj is a
function of zj, as it is for sj =⟨w ⊥ s ,z j⟩. For (ii), integrating the marks out sequentially shows
that the timing-only posterior is that of Proposition 21, and conditioning does not increase expected
entropy.
time
B: earnings warning
6 hours ago
A: unrelated
macro story
20 min ago
C: new article,
near-copy of B
timing
meaning
Parent of C
news A B
timing only
timing + meaning
Figure 8: Semantic declustering (Theorem 6), illustrative numbers. Timing alone attributes article C
to the most recent story A. Adding embedding similarity attributes it to B, of which it is a near-copy.
C is thus correctly classified as echo of B, and its sentiment enterss echo.
C.3 Return-aligned embeddings
Theorem 7(When the bound is attained). L(Z)≥ P j H(q j·), with equality iff Sjk =c− τ 2b2 Djk
for a constant c and all j̸=k . At equality ∥zj −z k∥2 = 2(1−c) + τ b2 ∥ρj −ρ k∥2, an increasing
affine function of squared outcome distance, so nearest neighbours in embedding space are nearest
neighbours in outcome space. (Equality requires this geometry to be realisable onS D−1.)
Proof. For each anchor, − P k qjk logp jk =H(q j·) + KL(qj·∥pj·)≥H(q j·) by Gibbs’ inequality,
with equality iff pj· =q j·. Two softmax vectors coincide iff their logits differ by a constant, so
equality holds iff Sjk /τ+D jk /2b2 =c j/τ for all k̸=j . By symmetry of S and D, for every
pair j̸=k , cj =S jk + τ 2b2 Djk =S kj + τ 2b2 Dkj =c k, so all cj equal a common c. The converse
is immediate. On the sphere, ∥zj −z k∥2 = 2−2S jk. The neighbour statement follows because
∥zj −z k∥2 is an increasing affine function of∥ρ j −ρ k∥2.
Theorem 8(Neighbour certificate).For any embedding Z, let ϵj := KL(qj·∥pj·(Z)) be the excess
loss at anchor j. For k, l̸=j , the embedding ranks k closer to j than l if (i) qjk −q jl > p2ϵj
(Pinsker), or if (ii)q jk > qjl and
∆jkl :=q jk log 2qjk qjk +q jl +q jl log 2qjl qjk +q jl > ϵj.
Condition (i) implies (ii), and (ii) is the weakest condition valid for every distribution within KL
distanceϵ j ofq j·: ifϵ j ≥∆ jkl, one such distribution tieskandl.
19

Proof. Throughout, pj· is a softmax of Sj·/τ, so pjk > pjl is equivalent to Sjk > Sjl, and on the
sphere∥z j −z k∥2 = 2−2S jk. It therefore suffices to showp jk > pjl.
(i) By Pinsker’s inequality, P k |pjk −q jk | ≤p2ϵj. Hence pjk −p jl ≥(q jk −q jl)− |pjk −q jk | −
|pjl −q jl|>0.
(ii) Merge all outcomes other than k and l into one cell. By the data-processing inequality, the
three-cell divergence satisfies KL3(q∥p)≤ϵ j. Consider the set {p:p k ≤p l}. The divergence is
convex in p, and its unconstrained minimiser p=q lies outside this set because qjk > qjl. The
constrained minimum is therefore attained on the boundary pk =p l =t , with prest = 1−2t . Setting
the derivative in t to zero gives t= (q jk +q jl)/2 and prest =q rest, where the divergence equals ∆jkl.
So every p with pjk ≤p jl has KL3(q∥p)≥∆ jkl > ϵj, which is impossible. The boundary point
withp rest split in proportion toqshows that the bound is attained, which gives tightness.
For (i)⇒(ii), write π=q jk /(qjk +q jl). Then ∆jkl = (q jk +q jl) KL

Bern(π)∥Bern( 1 2 )  ≥
2(qjk +q jl)(π− 1 2 )2 = (qjk −qjl )2 2(qjk +qjl ) ≥ (qjk −qjl )2 2 , by Pinsker for two points andq jk +q jl ≤1.
Remark25 (Realisability and regularisation).Equality requires the matrix with unit diagonal and
off-diagonal entries c− τ 2b2 Djk to be positive semidefinite of rank at most D. Otherwise the
minimiser is the closest realisable geometry in the KL sense. In practice we add a semantic anchorP
j KL(p(0) j· ∥pj·) to the frozen encoder, which interpolates between topic geometry and outcome
geometry.
Generic embedding
organised bytopic
oil stories
bank stories
fine-tune on
market outcomes
Market-aligned embedding
organised byconsequence
news that got overdone
news that stuck
price later reversed price kept moving oil story bank story
Figure 9: Theorem 7 in pictures. Before fine-tuning, stories cluster by subject. At the optimum,
distances mirror market aftermaths, so “news that got overdone” becomes a region of the map.
C.4 Topic-orthogonal sentiment, surprise and analog forecasting
Lemma 26(Topic invariance).Let U∈R D×r have orthonormal columns spanning topic directions
and w⊥ s := (I−U U ⊤)ws. Then (i) ⟨w⊥ s ,z+Ut⟩=⟨w ⊥ s ,z⟩ for all t∈R r, and (ii) w⊥ s =
arg min{∥w−w s∥:U ⊤w=0}.
Proof. (i) U ⊤w⊥ s =U ⊤ws −U ⊤U U⊤ws =0 . (ii) w⊥ s is the orthogonal projection of ws onto
kerU ⊤.
A causal sequence model predicts the next embedding ˆzt from past coverage and market state; the
innovation isε t =z t − ˆzt.
Proposition 27(Calibrated surprise).If the predictive law is zt | Ft− ∼ N(ˆzt,Σ) with Σ≻0 ,
then St :=ε ⊤ t Σ−1εt ∼χ 2 D and st/ p w⊥⊤s Σw⊥s ∼ N(0,1) with st :=⟨w ⊥ s ,ε t⟩. Moreover
St =−2 logp(z t | Ft− )−Dlog 2π−log det Σ : Mahalanobis surprise is Shannon surprisal up to
constants.
20

Proof.Σ −1/2εt ∼ N(0, ID), so St is a sum of D squared independent standard normals. The
projection of a Gaussian vector is Gaussian with variance w⊤Σw. The last identity is the Gaussian
log-density.
Definition 28.Given a story z and a market state ζ, theMarket Interpretation Function M(z,ζ) is
the conditional law of the abnormal return over the reaction window, with meanµ(z,ζ).
Thedéjà vuestimator averages the reactions of historical analogues with weights kj ≥0 , normalised
asω j =k j/ P l kl:ˆµ(z) = P j ωjARj.
Proposition 29(Bias–variance of analog forecasting).Suppose ARj =µ(z j) +e j with E[ej |
z1:N ] = 0, conditionally uncorrelated errors of variance at most σ2, and µ L-Lipschitz for a metric
d. Then

E[ˆµ(z)|z 1:N ]−µ(z)

 ≤L X
j
ωjd(z,z j),
Var

ˆµ(z)|z1:N

≤ σ2
Neff
, N eff :=
 X
j
ω2 j
−1
.
Proof. The bias is P j ωj(µ(zj)−µ(z)) , bounded termwise by Lipschitz continuity. The variance
is P j ω2 j Var(ej | ·)≤σ2 P j ω2 j .
C.5 Lévy area
Definition 30(Lévy area).ForC 1 pathsX, Y: [0, T]→R,
AT (X, Y) = 1 2
Z T
0
(Xu −X 0)dY u −(Y u −Y 0)dX u = 1 2  SXY T −S Y X T  ,
where SXY T = R 0<s<t<T dXs dYt is a level-two signature term (Lyons, 1998; Chevyrev and Kormil-
itzin, 2016).
Proposition 31(Structural properties).(i) A(X, Y) =−A(Y, X); (ii) A(aX+c, bY+d) =
abA(X, Y); (iii) A is invariant under C 1 increasing reparametrisations of time; (iv) if(X, Y)traces
a positively oriented simple closed curve, A equals the enclosed area; (v) for a piecewise-linear path
through(X i, Yi)n i=0,
A= 1 2
n−1X
i=0

(Xi −X 0)(Yi+1 −Y i)−(Y i −Y 0)(Xi+1 −X i)

.
Proof. (i)–(ii) are immediate from the definition. (iii) follows from the change of variables u=ψ(s)
in both integrals. (iv) is Green’s theorem applied to 1 2 (x dy−y dx). (v): on the segment from i to
i+ 1 , Xu −X 0 = (Xi −X 0) +t∆X and Yu −Y 0 = (Yi −Y 0) +t∆Y for t∈[0,1] . The segment
contributes 1 2 [(Xi −X 0)∆Y−(Y i −Y 0)∆X] + 1 2 R 1 0 (t∆X∆Y−t∆Y∆X)dt , and the last integral
vanishes.
Theorem 9(Expected area identifies lead–lag).Let (X, Y)be zero-mean and jointly weakly sta-
tionary with C 1 (mean-square) paths and cross-covariance C(h) =E[X sYs+h]∈C 1. Then
E[AT ] =T C′(0)− 1 2  C(T)−C(−T)  . If moreover Yt =γX t−ℓ +Z t with ℓ̸= 0 , Z stationary
and independent of X, and X has an even C 1 autocovariance R with R′(h)<0 for h >0, then the
long-run area rate has sign sgn(γℓ). If γ >0 (gloom follows positioning), a positive area means
money moved first.
Proof. Mean-square differentiability gives E[Xs ˙Yt] =∂ tC(t−s) =C ′(t−s) and, since E[YsXt] =
C(s−t),E[Y s ˙Xt] =−C ′(s−t). Therefore
E[(Xu −X 0) ˙Yu] =C ′(0)−C ′(u),E[(Y u −Y 0) ˙Xu] =−C ′(0) +C ′(−u).
21

The integrands are integrable by Cauchy–Schwarz and stationarity, so Fubini’s theorem gives
E[AT ] = 1 2
Z T
0

2C ′(0)−C ′(u)−C ′(−u)  du=T C ′(0)− 1 2  C(T)−C(0)  − 1 2  C(0)−C(−T)  ,
which simplifies to the claim.
For the lag statement: C(h) =E[X s(γXs+h−ℓ +Z s+h)] =γR(h−ℓ) , so C ′(0) =γR ′(−ℓ) =
−γR′(ℓ) by evenness. If ℓ >0 then R′(ℓ)<0 ; if ℓ <0 then R′(ℓ) =−R ′(−ℓ)>0 . Since
E[AT ]/T→C ′(0) when C is bounded, the long-run area rate has the sign of −γR′(ℓ), that is, of
γℓ.
positioning
(buying→)
headline gloom
area>0
1.money buys
2.gloom rises
Money led the story
strategic: stronger signal
positioning
(buying→)
headline gloom
area<01.gloom
2.then buying
Money followed the story
reactive: weaker signal
Figure 10: Theorem 9: the orientation of the loop in the (positioning, gloom) plane reveals who
moved first, and its enclosed area (Proposition 31(iv)) measures how strongly.
D From signals to positions
Events belong to latent regimes Kt ∈ {I,O,S}(informational, overreaction, strategic) following a
Markov chain, with emissionso t |K t =k∼f k, whereo t collects(s new, secho, G, A,A, . . .).
Proposition 32(Causal filtering and mixture optimality).The filtered probabilities πt(k) =P(K t =
k| Ft) are Ft-measurable and satisfy πt ∝f(o t)⊙P ⊤πt−1. The MSE-optimal forecast is the
mixture of experts
E[rt+h | Ft] =
X
k
πt(k)E[r t+h | Ft, Kt =k].
Smoothed probabilities P(Kt =k| FT ), T > t, are not Ft-measurable in general and must not be
used for forecasting.
Proof. The recursion is Bayes’ rule with prediction step P ⊤πt−1. The mixture follows from the
tower property. Smoothed probabilities depend ono t+1:T .
Theorem 33(Exponential detectability of strategic episodes).Consider an episode of n events that
are i.i.d. given a fixed regime, with o∼ N(m0,Σ) under the null regime and N(m 1,Σ) under the
strategic regime, and priorsπ 0, π1. The Bayes (MAP) misclassification probability satisfies
Pe ≤ √π0π1 e−n∆2/8 ≤ 1 2 e−n∆2/8,∆ 2 := (m1 −m 0)⊤Σ−1(m1 −m 0).
Consequentlyn≥(8/∆ 2) log  1/(2ϵ)  events suffice forP e ≤ϵ.
Proof.P e =
R
min{π0p⊗n 0 , π1p⊗n 1 } ≤√π0π1 R q p⊗n 0 p⊗n 1 = √π0π1 BCn, using min{a, b} ≤√
ab, where BC =
R √p0p1 is the Bhattacharyya coefficient (Bhattacharyya, 1943; Kailath, 1967).
22

For equal-covariance Gaussians, completing the square gives BC =e −∆2/8 (Lemma 11). Finally√π0π1 ≤ 1 2.
0 10 20 30 40
10−4
10−2
number of events in the episoden
bound onP e
∆ = 0.5
∆ = 1
∆ = 1.5
∆ = 2
Figure 11: Theorem 33. Detection error falls exponentially in the length of a strategic episode, at a
rate set by the Mahalanobis separation∆of the regime fingerprints.
Forecast intervals use adaptive conformal inference (Gibbs and Candès, 2021). Let ˆCt(α′) be nested
prediction sets with ˆCt(α′) =R for α′ ≤0 and ˆCt(α′) =∅ for α′ ≥1 . Set errt =1{r t /∈ˆCt(αt)}
andα t+1 =α t +γ(α−err t)withα 1 ∈[0,1]andγ >0.
Theorem 34(Deterministic long-run coverage; Gibbs and Candès, 2021, Prop. 4.1).Forevery
sequence of outcomes, including adversarial or regime-switching ones,

 1 T TX t=1 errt −α

 ≤ max{α1,1−α 1}+γ γ T .
Proof (reproduced for completeness). First, αt ∈[−γ,1 +γ] for all t, by induction. If αt <0 , then
errt = 0 and αt+1 =α t +γα∈(α t, γα). If αt >1 , then errt = 1 and αt+1 =α t −γ(1−α)∈
(1−γ(1−α), α t). If αt ∈[0,1] , then αt+1 ∈[α t −γ(1−α), α t +γα] . In each case the
interval lies in [−γ,1 +γ] . Telescoping the update gives αT+1 −α 1 =γ P t≤T (α−err t), hence
| 1 T P errt −α|=|α T+1 −α 1|/(γT)≤max{1 +γ−α 1, α1 +γ}/(γT).
Theorem 35(Kelly shrinkage under estimation risk; classical, included for completeness).Let an
asset have excess drift µ and volatility σ, with continuous rebalancing at a constant fraction f, so
that the long-run excess log-growth rate isg(f) =f µ− 1 2 f 2σ2 (Merton, 1969). Let ˆµbe an estimate
withEˆµ=µandVar ˆµ=s 2, independent of future returns, and usef=cˆµ/σ 2. Then
Eg= cµ2 − 1 2 c2(µ2 +s 2) σ2 , c ⋆ = µ2 µ2 +s 2 = SNR 1 + SNR,SNR := µ2 s2 ,
with optimal growth µ4/  2σ2(µ2 +s 2)  . Full Kelly (c= 1 ) yields (µ2 −s 2)/(2σ2), which is negative
whenevers >|µ|.
Proof.E[f µ] =cµ 2/σ2 and E[f 2]σ2/2 =c 2(µ2 +s 2)/(2σ2). The resulting concave quadratic in c
is maximised atc ⋆, and substitution gives the remaining expressions.
Proposition 36(Well-posed portfolio construction).For ˆΣ≻0 , risk aversion γr >0 , cost coeffi-
cientsc i, ηi ≥0, factor exposuresBand bounds¯w, G >0, the programme
max
w
α⊤w− γr 2 w⊤ ˆΣw− X
i
ci|wi −w 0 i | − X
i
ηiσi
|wi −w 0 i |3/2 √Vi
s.t.B ⊤w=0,1 ⊤w= 0,|w i| ≤¯w,∥w∥ 1 ≤G
has a unique solution. The3/2-power term integrates square-root impact (Bouchaud et al., 2018).
23

0 0.2 0.4 0.6 0.8 1 1.2 1.4 1.6
−0.2
0
0.2
0.4
full Kelly
Kelly fractionc
expected growth×σ 2/µ2
SNR= 4
SNR= 1
SNR= 0.5
Figure 12: Theorem 35. Expected growth as a function of the Kelly fraction for three signal-to-noise
ratios; dots mark c⋆ = SNR/(1 + SNR). With noisy edge estimates, full Kelly destroys growth. The
conformal interval width of Theorem 34 suppliess.
Proof. The feasible set is a nonempty ( w=0 is feasible), compact and convex polytope. The
objective is continuous and strictly concave: it is a linear term, minus a strictly convex quadratic,
minus convex functions | · |and | · |3/2. A continuous function attains its maximum on a compact set,
and strict concavity makes the maximiser unique.
E Numerical verification
Every closed form in this paper was checked against an independent computation (Table 5). Theory
values are exact functions of the model parameters. The Gaussian results of Section 3.1 were checked
by regression on 2×10 6 simulated draws. Theorem 4 was checked with fat-tailed values ( t3)
and Laplace message noise, which tests its distribution-free claim. Optimal speech was compared
with numerical optimisation, Theorem 6 with brute-force enumeration of every parent labelling, and
Theorem 9 with a smooth Gaussian process with a known lag. Both forms of Theorem 8 were checked
on 3,000 random pairs of target and model distributions: no certified pair was ever misordered, and
the exact form certified 3.6 times as many pairs as the Pinsker form (the ratio depends on how
instances are drawn; see scripts/check_certificate.py). The t3 exaggeration case converges
most slowly because the fourth moment of a t3 variable is infinite; the pathwise identity r=λx−φε
itself holds to machine precision.
Exactness does not by itself show that meaninghelps. We therefore simulated cascades in which each
echo is a von Mises–Fisher copy of its parent with concentration κ (Assumption 5; Hawkes µ= 0.6 ,
α= 1 , β= 1.25 ; 16-dimensional embeddings; about 2,000–2,800 articles per run) and asked each
method to recover the true parent of every article. Timing alone recovers about one parent in four at
every concentration. Adding meaning raises accuracy to 95% when echoes are close copies, and it
nearly eliminates the error in each article’s probability of being an echo (Figure 13).
F Experimental details
The market.There are 300 firms and 60 events per firm. Each firm hosts one institution whose
parameters are fixed across events. A quarter of the institutions are non-strategic: they report value
and do not trade. The rest are strategic, with credulity φ and deterrence a= 2λk drawn inside
the shading, false-alarm or exaggeration region of Theorem 3. Each firm’s regime is drawn with
probability one quarter for each of the four. At each event:
(1) value is drawn,v∼ N(0,1);
(2) the institution trades x=χv , spread evenly over the ten days before it speaks, and then
publishes Say=ψv+N(0,0.3 2), with(ψ, χ)from Theorem 3;
24

Table 5: Theory versus independent checks (2×10 6 draws, seed 0).
Result Quantity Theory Check
Three-voice economy (Section 3.1)
Corollary 2 Bayes weight on the echo channel0−0.0006
Theorem 1 return loading on the echo channel−0.1840−0.1843
Theorem 13 loading on positioning,c x 0.4012 0.4004
Theorem 14 absorption coefficient,c A −0.1997−0.2004
Strategic speech (Section 3.2)
Theorem 3 speech slopeψ(φ= 0.6,a= 0.5)−0.7143−0.7143
Theorem 3 trade slopeχ(φ= 0.6,a= 0.5)1.4286 1.4286
Theorem 4Cov(r,Say),t 3 values, false alarm−2.294−2.293
Theorem 4Cov(r,Say),t 3 values, exaggeration−7.608−7.676
Theorem 5 2-cycle points ata= 1.95{0.8189,1.1311} {0.8189,1.1311}
Theorem 5 2-cycle multiplier ata= 1.8 0 9×10 −16
Measurement (Sections 4.1 to 4.3)
Theorem 6 largest error of the factorised posterior0 1.1×10 −16
Theorem 9 Lévy-area rate, lag0.5 0.2356 0.2360
Theorem 8 wrongly ordered certified pairs,3,000
random cases
0 0
Sizing (Section D)
Theorem 35 growth at the shrunk Kelly fractionc ⋆ 0.01056 0.01055
Theorem 35 growth at full Kelly−0.0300−0.0300
2 5 10 20 40 80
0
0.2
0.4
0.6
0.8
1
echo concentrationκ
parent accuracy
timing only
timing + meaning
a
2 5 10 20 40 80
0
0.1
0.2
0.3
echo concentrationκ
mean|P(echo)−1{echo} |
b
Figure 13: Meaning makes echo detection work (Theorem 6).a: accuracy of the most likely parent.
b: mean absolute error of each article’s echo probability. Grey: timing only (κ= 0 in the posterior).
Red: timing and meaning.
(3) the media publish a Hawkes cascade over the next ten days. The statement is the first
article. Independent news items arrive at rate 0.4 per day, each carrying the sentiment
v+N(0,1.5 2). Every article can be echoed, with branching ratio n= 1−φ 0/φ so that the
crowd’s effective credulity isφ (Proposition 18). Echoes arrive after exponential delays with
rate 1.5, copy their parent’s sentiment up to noise N(0,0.15 2), and copy its 16-dimensional
embedding up to a von Mises–Fisher perturbation withκ= 30(Assumption 5);
(4) the crowd prices every article, p= P j wjsj +λ(x+u) , where wj =φ 0 for the statement
and its echoes,w j = 0.04for news and its echoes, andu∼ N(0,0.4 2)is noise trading;
(5) the forward return is r=v−p+η , where η∼ N(0,102) is information that arrives later,
and positioning is revealed with error, Do=x+N(0,0.5 2).
What the methods see.Every method sees the article times, embeddings and sentiment scores, the
statement, the noisy positioning, the price reaction, and daily paths of positioning and cumulative tone
from ten days before the statement to ten days after it. No forecasting method sees value, regimes,
25

parentage or any model parameter. The one exception is the false-alarm detector of Q2, which is
trained on the true regime labels of the training half, as a supervised detector would be on labelled
historical episodes.
Protocol.The first 30 events of each firm form the training set and the last 30 the test set. Every
estimated quantity uses the training half only. This includes the Hawkes parameters (pooled maximum
likelihood), the echo concentration κ (marked likelihood), the narrative-implied price move, all
regression and boosting weights, and all standardisations. The features of an event use only that
event’s articles and price reaction and the firm’s earlier events. Table 6 lists the features.
Table 6: Features built from the theory. All are computed causally.
Feature Construction Source
News, echos new = P j P(newsj)s j over articles other than the
statement;s echo = P j P(echoj)s j
Proposition 24 and Theorem 6
Say–Do switch correlation of Say and Do over the firm’s previous20
events; words are faded when it is below−0.2
Theorem 4
Absorption price reaction minus the narrative-implied move, fitted
linearly on Say,s new ands echo (pooled, or per firm; tone is
their sum)
Theorem 14
Lead–lag Lévy area of (positioning,−tone) over the event window,
signed by the direction of the positioning change
Theorem 9
Composite unit weights on the standardised terms above, with the
switch applied to Say
Section 4.4
Calibration, and what we changed.The features, tests and strategies were fixed before we
looked at any of their results. The simulator’s scale was then calibrated as follows. A pilot run
exposed two degenerate properties of the raw simulator: prices moved about 3.3 times as much as
fundamentals, and fading the tone alone reached an information coefficient of 0.89. We lowered the
per-article impact of news from 0.12 to 0.04 and restricted the credulity of non-strategic institutions
to (0.4,0.95) . We then chose the scale of the late information η so that a linear regression on the
raw voices, which uses no theory at all, reaches an out-of-sample information coefficient of about
0.17. That is far more predictable than any real market. We chose it so that differences between
methods are visible with 300 firms, and only comparisons between methods should be read from the
results. The calibration also caps what any method can achieve. Forecasting with the true mispricing
v−p gives an IC of 0.181 (between 0.165 and 0.206 across seeds), only about 0.01 above the linear
baseline.
Metrics.For forecasts we report the cross-sectional information coefficient (IC) in each of the
30 test periods, its average and its t-statistic across periods, and the per-period Sharpe ratio of a
dollar-neutral portfolio with weights proportional to the standardised score. The theory tests are
pooled regressions of test-period returns on standardised features, with standard errors clustered by
firm. The main market is simulated with five seeds, every robustness variant with three, and every
sample size with two. Together these give 29 distinct simulated markets. The “timing only” variant
re-analyses three of them, so there are32analyses in all.
Compute and software.All experiments ran on a cloud container with 2 CPU cores and 7 GB of
memory; no GPU was used. One main-market seed (simulation, Hawkes fit, declustering of about
25,000 articles, all strategies and tests) takes about 40 seconds, and one text-experiment run takes
about 4.5 minutes on one core. The full suite of Section 5, including robustness, sample-size, text and
diagnostic runs, takes roughly one hour. We used NumPy and SciPy (BSD-3-Clause), scikit-learn
(Pedregosa et al., 2011) (BSD-3-Clause) and autograd (MIT). Versions: NumPy 2.4.4 (Harris et al.,
2020), SciPy 1.17.1 (Virtanen et al., 2020), scikit-learn 1.8.0. Pilot runs used for calibration took
about as much compute as one main-market seed each. The code, released under the MIT licence
26

with tests for every theorem, regenerates every table and figure. Comments in the code refer to the
theorem numbering of an extended version of this paper.
Hyperparameters.Text benchmark:the projection W∈R V×16 is initialised with independent
N(0,1/V) entries and trained with Adam (learning rate 0.05, β1 = 0.9, β2 = 0.999) for 600 steps
on random batches of 256 headlines; τ= 0.1 was fixed in advance and not tuned; the bandwidth b is
the median pairwise outcome distance over 400 training headlines, and 0.3b in the sharp-target run;
analog forecasts use a Gaussian kernel with bandwidth 0.05 on embedding distance; the certificate
is evaluated on 150 random training anchors. The ridge baseline uses α= 1 , and gradient boosting
uses scikit-learn’s histogram-based regressor with 300 iterations and learning rate 0.05.Simulated
market:both boosting models use the same settings; the false-alarm detector is an ℓ2-regularised
logistic regression (C= 1 ) on standardised features; the Say–Do window is W= 20 past events (at
least5) and the switch threshold is−0.2. None of these values was tuned on test data.
G Additional results
Q1: repetition can be separated from news, and fading it works.The semantic declustering step
recovers the echo concentration almost exactly (ˆκ= 30.27±0.07 against a true 30) and the share
of articles that are echoes ( 0.422 against 0.427). On the same simulated markets, declustering by
timing alone estimates an echo share of 0.368 against a true 0.430, because it mistakes many echoes
for news. The prediction of Corollary 2 holds without exception. Echo sentiment predicts returns
with a significantly negative sign in every one of the 29 simulated markets, with a mean t-statistic of
−8.0 in the main market (Table 7). Meaning sharpens the test: on identical markets, the t-statistic
weakens from −7.5 to −6.0 when timing alone is used. The news prediction of Corollary 2 also
holds, but more weakly. The sign is positive in every market, the mean t-statistic is +2.1, and the
effect is significant in 21 of the 29 markets. News is harder to detect because each news article is a
noisy signal of value and the crowd underreacts to it only modestly.
Table 7: Theory tests on the test half of the main market (five seeds). Coefficients are in units of
fundamental value per training standard deviation of the feature. t: firm-clustered, averaged over
seeds. The last column counts seeds with|t|>2and the predicted sign.
Regressor (controls) Prediction Coef.tAs predicted
News sentiments new (Say, Do)+(Corollary 2)+0.35 +2.13/5
Echo sentiments echo (Say, Do)−(Corollary 2)−1.52−8.05/5
Say, fade group (Do)−(Theorem 4)−3.34/5
Say, fade group (Do, news, echo)− −0.06−0.31/5
Say, follow group (Do, news, echo) either+0.10 +0.4–
Do (Say by group, news, echo)+ +0.14 +0.91/5
Absorption, all events either (Theorem 14)−1.27−11.6–
institution does not trade− −1.25−3.64/5
institution trades either−1.27−11.1–
Absorption, firm-level multiplier either−0.72−9.0–
institution does not trade− −1.03−4.05/5
Signed Lévy area+(Theorem 9)+0.23 +1.01/5
Q2: the Say–Do covariance finds the institutions whose words should be faded.On its own,
the rolling correlation between Say and Do separates the events of false-alarm institutions from
all others with an AUC of 0.895 (Figure 3a). A logistic classifier that adds four other observable
features, trained on the true labels of the training half, reaches 0.934±0.010 on later events of the
same firms. Real data would supply such labels only through episodes identified after the fact. The
single-feature AUCs are reported as max(AUC,1−AUC) , so the values near 0.5 for absorption and
echo share mean “uninformative”. Used as the switch of Section 4.4, the same correlation labels
correctly whether a firm’s words should be faded (false-alarm and exaggerating institutions, the two
27

regimes in which Cov(Say,Do)<0 ) 85% of the time from five past events and 96% of the time
from forty (Figure 3b). In the group it flags, statements predict returns with the sign reversed: the
average t-statistic is between −3.0 and −3.3 at every window length, and it is significant in four of
five seeds. In the other group the average t-statistic is between −0.6 and −1.0. We report that sign
as an empirical finding. The identity does not cover non-strategic institutions, whose silence in the
market is not optimal given the crowd’s credulity.
Two caveats matter for real data. First, once news and echo sentiment are added as controls, the
reversed coefficient on Say in the flagged group is no longer significant (t=−0.3 ). Echo sentiment
alone is enough to remove it (t= +0.2 on average), while news alone only weakens it (t=−2.0 ). In
this market most of a statement’s price impact travels through its echoes, so the echo control absorbs
it. Second, Do’s own coefficient is imprecise, for two reasons. With Say, news and echo all controlled
its t-statistic is +0.9, partly because Say and Do are nearly collinear within the strategic regimes
(their correlation is −0.87 for false alarms, −0.78 for exaggeration and +0.54 for shading), so a
regression cannot divide credit between them. Even with Say removed, the t-statistic averages only
+1.6, because the institution’s price impact is small next to the information that arrives later. The
collinearity is also why Theorem 13 works with the gap between the two voices rather than with
either voice alone.
Q3: absorption measures the narrative model as much as the market; lead–lag is weak.
Absorption predicts strongreversal( t=−11.6 ), and it does so in all 29 markets. It does
so both where institutions trade, where Theorem 14 allows either sign, and where they do not
(t=−3.6 ), where it predicts reversal. The second result looks like a confirmation, but it is not, and
experiments/diagnostics.pyshows why.
Absorption is the residual of the price reaction after the narrative-implied move has been removed.
Here only 12–19% of the residual’s variance is the institution’s trade and 2–4% is noise trading.
Almost all of the rest isnarrative misfit, the part of the crowd’s reaction that a linear narrative model
fails to capture. The misfit has a simple source. The statement’s price impact is multiplied by the
size of its echo cascade, and secho pools the statement’s echoes, which the crowd weights heavily,
with the more numerous echoes of news, which it weights lightly. Adding Say times cascade size
to the narrative model weakens the reversal from t≈ −12to t≈ −3.5on average. If we replace
the estimate with the true absorption λ(x+u) , which a perfect narrative model would recover, the
coefficient is insignificant in both groups: t ranges from −1.2 to +0.5 where institutions trade and
from −1.4 to +0.8 where they do not. Lemma 15 protects absorption against a wrong multiplier. It
does not protect it against a price that is not linear in the channels the model uses.
Our experiments therefore neither confirm nor refute Theorem 14: the simulated trades are too
small relative to later information to reveal either sign. What they do show is practical. The sign of
estimated absorption depends on the narrative model and must be estimated, never assumed. In the
unit-weight composite, the absorption term enters with the wrong sign for this market, and removing
it doubles the composite’s IC from0.049to0.096.
The signed Lévy area has the predicted positive sign in 27 of the 29 markets, but it is significant in
only 9 (t= +1.0 in the main market). It is more useful for detecting false alarms (AUC 0.63) than
for predicting returns.
Q4: the theory adds little forecasting power, but there was little to add.Figure 14 ranks twelve
forecasts. Following the tone loses money. Following institutional statements loses money too,
because half of the institutions are in regimes whose words should be faded, and even the others’
statements are already priced through their echoes. Fading the price reaction is a strong baseline
(IC 0.162). A linear regression on the raw voices does slightly better (0.169). Adding the theory’s
features to that regression changes almost nothing (0.171, at most about 0.005 better in any seed).
For gradient boosting the features help a little: 0.109 becomes 0.118 in the main market, and the
features improve boosting by more than 0.001 in 18 of the 29 markets. The unit-weight composite of
Section 4.4 is weak (0.049), mostly because of the absorption term discussed above.
28

This comparison has little power, and we do not read much into it. Forecasting with the true mispricing
v−p , which no method can observe, reaches only 0.181, so there is about 0.01 of IC between the
linear baseline and perfection. With so little room, the result is consistent with the theory adding
nothing and also with it adding a great deal of what is left. Two points are nonetheless clear. First,
Theorem 1 says the optimal forecast is linear in the voices, and a regression free to learn the weights
comes close to the ceiling, as that theorem suggests. Second, the unit-weight composite is not a good
trading rule; the composite of Section 4.4 should be used with fitted weights. The theory’s clearest
contributions in these experiments are the signs it predicts and the diagnostics of Q1 and Q2, not
extra forecasting power.
−0.1 −0.05 0 0.05 0.1 0.15 0.2
Linear: raw + theory
Linear: raw voices
Fade the price reaction
Fade the tone
Boosting: raw + theory
Boosting: raw voices
News minus echo
Theory composite (unit weights)
Follow Do
Composite with firm-level absorption
Follow Say
Follow the tone
out-of-sample information coefficient (mean±s.d., five seeds)
fitted models
theory, unit weights
single-voice rules
Figure 14: Out-of-sample forecasts in the main simulated market. The fitted models use the training
half. “Raw voices” are Say, Do, tone, article count and the price reaction; “theory” adds the features
of Table 6.
Robustness.Table 8 changes one assumption at a time on three new seeds. Fat-tailed values and
power-law echo delays (a misspecified kernel) leave the echo, news and detection results intact.
Partial disclosure, in which only 30% of the trade is disclosed and positioning is measured with twice
the noise, leaves the echo and news results intact but lowers the detection AUC to0.857. A saturating
crowd, which prices 1.5 tanh(s/1.5) instead of s, halves the IC of every forecast, but detection is
unaffected and the echo and news signs survive. The controlled test of reversed words (Table 7, fourth
row) does not: under the saturating crowd its t-statistic has the wrong sign in all three seeds. When
meaning is weak (κ= 5 ) or ignored, the echo share is underestimated by about six percentage points
and the echo test weakens, as Theorem 6 leads one to expect. More events per firm strengthen the
echo test, somewhat more slowly than the square root of the sample: over two seeds the t-statistic is
−5.4,−6.9and−9.3with20,40and80events, while detection stays at an AUC of0.93–0.94.
Q5: return-aligned embeddings organise text by consequence.For the embedding results we
generated a corpus of short synthetic headlines. Each headline mixes four topic words, two tone
words, one cue that decides whether the move isoverdone(it reverses within a week) orfundamental
(it continues), three filler words and a company code. Topic words are numerous and have nothing to
do with outcomes, so a generic bag-of-words geometry groups headlines by topic. Each headline has
a three-part outcome: the next-day move, the week-ahead move and the change in implied volatility.
We trained a 16-dimensional linear projection of TF-IDF vectors with the loss of Theorem 7 (τ= 0.1 ,
bandwidth by the median heuristic, 600 Adam steps on batches of 256) on 2,000 headlines, and tested
it on1,000new ones.
29

Table 8: Robustness: one change at a time, three seeds each. “Reference” is the main market on the
same seeds. IC: out-of-sample information coefficient. Echo share: estimated (true).
ICt-statistic
Variant fade price linear + theory echo news Lévy AUC echo share
Reference0.184 0.187 0.190−7.5 +3.6 +3.6 0.941 0.425(0.430)
Fat tails (t3 values)0.134 0.137 0.141−8.1 +2.4 +0.5 0.924 0.423(0.428)
Saturating crowd0.090 0.099 0.101−5.9 +3.2−0.0 0.942 0.425(0.430)
Power-law echo delays0.171 0.176 0.177−7.9 +2.1 +1.9 0.939 0.417(0.429)
30% of trade disclosed0.184 0.183 0.191−7.5 +4.1 +2.9 0.857 0.425(0.430)
Weak meaning (κ= 5)0.173 0.187 0.188−7.2 +1.9 +2.2 0.941 0.373(0.429)
Timing only (reference markets)0.184 0.187 0.189−6.0 +2.6 +3.7 0.940 0.368(0.430)
Training moves the geometry from topic to consequence (Table 9 and Figure 15a). In TF-IDF space
the ten nearest neighbours of a test headline share its topic 85% of the time and its consequence (tone
and cue together) 51% of the time. After training they share its consequence 100% of the time and
its topic 34% of the time, close to the chance level of 25%. The analog forecast of Proposition 29
predicts the week-ahead move with an IC of0.892, against 0.192 for TF-IDF neighbours and a ceiling
of 0.936 set by the outcome noise. Linear regression on the same words fails completely ( −0.02),
because the outcome depends on theinteractionof tone and cue, which a linear model of word counts
cannot express. Gradient boosting captures the interaction (0.837) but falls short of the embedding.
That comparison favours the embedding, which is trained on all three outcomes: the next-day move
reveals the tone and the volatility change reveals the cue, while boosting sees only the week-ahead
target.
The certificate is the negative result (Figure 15b). After training, the mean excess loss per anchor is
0.021–0.026 across seeds. That is small, but target probabilities over 149 neighbours are of order
1/149≈0.007 , and neither form of Theorem 8 certifies a single comparison. Two things stand
in the way. The median-heuristic bandwidth makes the targets almost flat, and the part of each
outcome that the text cannot predict leaves an excess loss that no embedding can remove. When we
remove both obstacles, using noise-free outcomes and a bandwidth of 0.3 times the median, the exact
form (ii) certifies 45% of the ordered comparisons with no errors, while the Pinsker form (i) still
certifies none. With the sharp bandwidth and realistic outcome noise, the excess loss stays at 0.14
and nothing is certified, even though the analog IC rises to 0.931, close to its ceiling. The certificate
never made a wrong claim in any run. It becomes informative, however, only when outcomes are
close to predictable from the text, which real returns are not.
Table 9: Text experiment: 1,000 test headlines, mean ± s.d. over three seeds. Neighbour columns:
share of the ten nearest training headlines with the same consequence (tone and cue) or the same
topic; chance is0.25for both. The ceiling for the IC is0.936.
Method Week-ahead IC Same consequence Same topic
TF-IDF neighbours (generic)0.192±0.003 0.506 0.846
Random 16-d projection (generic)0.039±0.016 0.327 0.622
Ridge regression on words (supervised)−0.019±0.016– –
Gradient boosting on words (supervised)0.837±0.008– –
Return-aligned embedding, 16-d0.892±0.009 1.0000.344
H Broader impacts and responsible use
Intended use.The framework is designed to help investors, researchers and supervisors read
financial narratives critically, by asking whether words agree with revealed positions and whether a
story is news or repetition. It uses public information and lawful disclosures only.
30

1 10 100 600
0
0.5
1
TF-IDF IC
training step
share or IC
neighbours: same consequence
neighbours: same topic
analog IC
a
1 10 100 600
0
0.1
0.2
0.3
0.4
0.5
training step
certified share of comparisons
exact (ii), noise-free, sharp
Pinsker (i), same run
exact (ii), realistic noise
b
Figure 15: Return-aligned training.a: the ten nearest neighbours of test headlines switch from
sharing a topic to sharing a consequence, and the analog forecast improves with them (mean of three
seeds).b: share of ordered outcome comparisons certified by Theorem 8 on 150 training anchors.
With noise-free outcomes and a bandwidth of 0.3 times the median, the exact form certifies about
half of them. The Pinsker form certifies none, and with realistic outcome noise neither form certifies
any. No certified comparison was ever wrong.
Interpretation.A strategic reading means that narrative and capital moved in opposite directions
in a particular order. It is not evidence of deception. Firms maintain information barriers between
research and trading, and positioning can diverge from published views for legitimate reasons, such
as hedging, client flow and differing horizons. Outputs should never be used to accuse individuals or
firms without independent evidence.
Misuse.Understanding how narratives move prices could in principle help someone design them.
Creating or spreading narratives intended to move prices is market manipulation and illegal in most
jurisdictions. We release no data, trained models or tools for generating text, and the simulator
describes aggregate behaviour, not specific market participants.
Market effects.If many participants faded the same echoes, the returns we describe would shrink,
and crowding could create new risks. Theorem 5 is itself a warning that reading rules and the texts
they read co-evolve.
31
