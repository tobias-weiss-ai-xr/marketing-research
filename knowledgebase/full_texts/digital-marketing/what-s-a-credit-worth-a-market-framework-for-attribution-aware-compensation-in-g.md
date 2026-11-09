---
title: What's a Credit Worth? A Market Framework for Attribution-Aware Compensation in Generative Music
url: https://arxiv.org/abs/2607.00641
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Luyang Zhang
- Xirui Jiang
- Junwei Deng
- Beibei Li
- Jiaqi W. Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.00641
pages: 29
chars: 102246
fetched_at: '2026-11-08T13:11:13+00:00'
kb_version: 1
---

# What's a Credit Worth? A Market Framework for Attribution-Aware Compensation in Generative Music

What’s a Credit Worth? A Market Framework for
Attribution-Aware Compensation in Generative Music
Luyang Zhang1∗ Xirui Jiang2∗ Junwei Deng3
Beibei Li1 Jiaqi W. Ma3 Chris Donahue1
1Carnegie Mellon University 2University of Michigan, Ann Arbor
3University of Illinois Urbana-Champaign
{luyangz, beibeili}@andrew.cmu.edu
xirui@umich.edu
{junweid2, jiaqima}@illinois.edu
Abstract
Advances in generative AI are rapidly increasing the quality and commercial
value of generated music, and this progress depends on large catalogs of creators’
recordings. This raises a central question for platform design: how should creators
be compensated when their work is used to train generative AI models that in turn
produce commercial outputs? We develop a framework for fairly compensating
creators in generative-music markets, where each creator’s payment depends on a
data-attribution score estimating their contribution to model outputs. Compared
to past compensation frameworks, our framework has two unique considerations:
(1) attribution is traced to entire creator catalogs, not individual songs, and (2)
theinformativeness(signal-to-noise ratio) of the attribution score is an input to
the payment mechanism. The framework yields a closed-form payment rule per
creator and measures the welfare cost of inaccurate attribution for both creators
and the platform. Whether the welfare-optimal contract is royalty-based or takes
the form of fixed-fee licensing depends on how informative attribution is for that
creator’s catalog. We show that better attribution translates directly into welfare
gains for both creators and the platform, yet under multi-platform competition
a platform only captures gains from attribution improvements when its signal
becomes the most precise in the market. To ground our framework in empirical
behavior, we train acoustic and symbolic music generation models and measure the
informativeness of scalable attribution techniques against a leave-one-catalog-out
ground truth. Our experiments reveal that noisy attribution signals push payment
toward fixed-fee licensing and diminish welfare for both creators and the platform,
providing an economic motivation for further research on improved attribution.
1 Introduction
Generative music models trained on copyrighted recordings are reshaping how music is produced
and consumed. As their output capabilities have advanced, AI music is crowding music streaming
services [16], copyright disputes have emerged [51], and regulators have responded with disclosure
mandates [23], suggesting the absence of a reliable and fair compensation rule. Training-data
provenance is rarely disclosed, and licensing, where it exists, is negotiated at the catalog or genre
level for flat fees that ignore two key factors: (1) that some data contributes more than others for a
given generated output [38], and (2) that flat licensing fees do not grow proportionally to revenue
∗Equal contribution.
Preprint.
arXiv:2607.00641v1  [cs.CY]  1 Jul 2026

from generated outputs. This raises a central question: how should creators be compensated when
their work trains generative AI models that are then used commercially?
Answering this question requires combining two technical fields. The first isdata attribution, which
estimates how much each creator’s catalog contributed to a given model output. The second is
payment design, which turns those estimates into contracts that handle noise, risk, and creator
participation. For data attribution, machine-learning methods [27, 42, 37] can estimate each creator’s
contribution, but the estimates carry noise that varies by creator and by method. Past work in data
attribution for music AI [6, 12, 17] seek to measure or reduce this noise, but do not factor it into the
payment mechanism. For payment design, contract theory [35] supplies general tools for payment
under noisy signals, but has rarely been combined with the attribution methods that produce the
signal. We unify these isolated literatures.
To this end, we develop a framework for fairly compensating creators in generative-music markets,
where each creator’s payment depends on a data-attribution score estimating their contribution to
model outputs. The framework’s central concept isinformativeness, a measure of how well the noisy
attribution signal tracks the true contribution. While most work in data attribution tracks influence
per-datum (i.e., per song), we make a simplifying assumption that tracking influenceper-catalogmay
suffice for compensation, as creators’ catalogs naturally group the training data by distinct payee. In
practice, herecreatorcan refer to any type of music rights holder, e.g., an independent aritst, or a
record label. We derive a closed-form payment rule per creator that balances a fixedlicensingfee and
royaltiesproportional to the catalog attribution score, along with a closed-form expression for the
welfare loss caused by imperfect informativeness.
The framework yields several implications about how attribution informativeness shapes contracts,
welfare, and creator incentives. For music AI platforms, it is optimal to adopt royalty-based payment
when the attribution to a creator’s catalog is precise, and fixed-fee licensing when it is noisy.We
show that both creators and the AI platform can benefit from more precise attribution.Under
multi-platform competition, the leading platform is mostly incentivized to improve the attribution
quality, since better signals widen its lead and let it capture more value from creators. For creators, the
welfare-optimal contract form (royalty-based or fixed-fee licensing) is determined by the platform’s
attribution informativeness for their catalog. When their own beliefs about that informativeness
diverge from the platform’s measurement, both creators and the platform incur welfare losses.
Under this framework, we propose a leave-one-catalog-out measurement pipeline and study it
empirically across two settings. The first setting applies a latent audio diffusion model Stable Audio
Open [24] on 22 catalogs of Creative Commons music data [ 8] and measure informativeness of
EKFAC [46] and D-TRAK [62]. The second setting (symbolic generation) trains a music language
model [58] on 100 catalogs of commercial melodies and harmonies from TheoryTab [20] and evaluate
LoGra [11] and TRAK [48]. We observe that two attribution methods canrankcreators similarly
yet differ by orders of magnitude in thescoresthat determine payment. In the audio setting, current
attribution noise makes fixed-fee licensing welfare-optimal for nearly all creators. Creators with
highly identifiable styles would benefit from royalty-based payment, but current audio attribution is
too noisy to track their contribution. The symbolic setting reproduces the same diagnostic — current
attribution methods sit below the royalty threshold across both modalities — confirming that the
precision shortfall is a property of current ML broadly, not a quirk of audio diffusion. Platforms
deploying attribution-based compensation should therefore benchmark multiple methods rather than
commit to one, benefiting both creators and the platform.
Our contributions are threefold:
• Framework.The first principal-agent framework bridging data attribution and contract
design for generative music markets. It yields closed-form expressions for the optimal
payment rule per creator (royalty-based or fixed-fee licensing) and for the welfare cost of
imperfect attribution.
• Measurement.The first empirical benchmark of attribution informativeness in generative
music models, with experiments that reflect the model paradigms and content modalities of
today’s commercial music AI systems under tractable attribution methods.
• Implications.Combined theoretical and empirical analysis yields concrete implications for
the generative music industry, establishing attribution quality and market transparency as
measurable economic primitives and providing a basis for industry policy and governance.
2

Figure 1: The attribution-aware compensation framework for generative music. Each creator’s
contract form follows from how precisely their contribution can be attributed to a generated output.
2 Related work
Data pricing and contract design.Several works study the design of data markets—marketplace
design [2], the price of information [7], and pricing data for an ML buyer [10]—alongside macroeco-
nomic analyses of data as a nonrival good [40, 13, 1]. Contract theory provides the payment-design
tools: Holmström [35] characterizes optimal payment under noisy signals, Mussa and Rosen [47]
treats contract design when creators differ, and Guruganesh et al. [32] extends both algorithmically.
Most recently, Zhang et al. [61] propose data pricing for general LLM data market, assuming risk-
neutral creators and a reliable attribution score. None of these works combine ML data-attribution
methods with contract design, nor do they treat signal informativeness as a heterogeneous quantity
across creators that the payment rule must explicitly accommodate.
Data attribution and music attribution.General data-attribution methods estimate per-datum
contribution to model outputs. Data Shapley [27, 39] provides an axiomatic per-datum attribution;
influence functions [42, 28] and TracIn [50] trace predictions to training examples; datamodels [37]
and TRAK [48] fit linear surrogates for the data-to-output mapping. Recent extensions scale these
methods to approximate unrolled differentiation [ 5], datamodel-based selection [ 22], LLM-scale
influence [31], LoRA-tuned models [43], and diffusion models [26]. In the music domain specifically,
fingerprinting [60] catches near-exact matches, embedding methods [57, 54] measure distributional
similarity, and Barnett et al.[6], Choi et al. [12], Deng et al. [17] apply attribution to generative music
for royalty assignment. This past work broadly seeks to improve informativeness in data attribution;
we instead factor its (often imperfect) informativeness into a payment structure for music data.
Generative music models.A growing line of generative music models are trained on large catalogs of
audio recordings. Modern approaches involve two families of methods: codec LMs [59] are language
models trained on tokenized music representations [ 19, 18, 3, 14], while other approaches train
diffusion models on latent audio representations [34, 52, 25, 24]. Output quality from these methods
is now sufficient for substantial commercial value and competition with human artists, e.g., music AI
startup Suno recently reported 300m in annual recurring revenue [56], and a streaming service Deezer
reported that 44% of newly uploaded tracks are AI generated [ 16]. Recent open-weight models
[9, 29] have broadened access to high quality music generation outside major labs. The increasing
value and proliferation of this technology motivates urgent study of mechanisms for economic and
creative sustainability, such as the payment mechanisms that we consider here.
3 A framework for attribution-aware compensation
Here we formalize our proposed music AI data payment framework as a market solution that
incorporates creators and AI platform. Beyond characterizing the equilibrium payment rule, the
framework reveals how attribution shapes contracts, welfare, and competition across the market.
3.1 Framework for musical market and data attribution
We model a single music AI platform that licenses training catalogs from many creators and pays
each through a contract whose form depends on how well the platform can attribute generated outputs
back to that creator’s catalog. The setup has four primitives — the market and its creators, the
3

data-attribution layers, an informativeness measure, and the contract space with creator preferences
over fixed-fee and royalty bundles.
Market and Creators.The market has three participants — N creators, an AI platform, and its users.
We focus on the platform–creator interaction, taking user demand as exogenous (observable from
platform logs). The platform operates a generative music service. A user request r arrives, and the
platform earns gross utility u(x, r)where x∈ {0,1}N indicates the catalogs active in the training
set. User requests r are drawn from a distribution D that the platform can estimate empirically from
request logs; we make no iid assumption across requests.
Each creator j∈ {1, . . . , N}controls a distinct, non-overlapping catalog Cj (e.g., an artist’s discog-
raphy, or a label’s collection) to be licensed wholesale — all or nothing. We further treat attribution
informativeness as accessible to both creators and the platform. The underlying methods (EKFAC,
D-TRAK, TRAK) are publicly available open-source academic tools, so creators with model access
(or third-party auditors acting on their behalf, e.g., royalty collection societies or music-tech consortia)
can independently verify the platform’s measurements rather than rely on its claims.
Each creator has a risk-aversion parameter αj >0 — how strongly they prefer steady payments to
volatile ones [49]. The platform’s utility u is non-additive across creators, reflecting the non-additive
nature of data attribution (two creators with similar styles add less joint value than two distinct ones).
Data attribution.The central informational primitive is attribution — how much each creator’s
catalog contributed to a generated output. The latent true attribution a∗ j ∈R is the counterfactual
contribution of catalog Cj to the platform’s outputs over a billing period (e.g., monthly in streaming).
The measured attribution ˆaj is a noisy estimate produced by an ML method (e.g., data Shapley
[27], influence functions [42], audio fingerprinting), and is what the platform pays on. Unlike most
data-pricing settings [2, 10, 61], music has a perceptual property — listeners can recognize an artist’s
style in generated output, soa ∗ j may be semantically meaningful, not a marginal predictive effect.
We analyze two cases regarding information transparency.Information symmetryis the baseline in
information economics [4, 35, 33, 7], aligned with music-industry practice as audio fingerprinting
[60], open-weight models, and third-party auditors (collection societies, music-tech consortia) enable
independent verification of attribution scores.Information asymmetryis a more practical case, where
platforms use proprietary or white-box attribution methods (like influence functions or EKFAC) that
creators cannot reproduce without model access. The welfare gap between the two cases (Section 3.3)
measures how much attribution transparency is worth to creators and the platform.
Informativeness.The quantity used by the attribution-aligned royalty benchmark (Theorem 1) is the
informativeness Ij of the payment signal — how well the noisy measurement tracks the catalog’s
true value to the platform. In plain terms, Ij is the OLS slope of true contribution on measured
attribution. Under classical measurement error ( ˆaj =a ∗ j +ξ j, ξj ⊥a ∗ j , E[ξj] = 0), Ij ∈[0,1] —
taking the value 0 when the signal carries no information about value and 1 when it is a perfect linear
predictor. Multiplicative scale bias or sign-flipped calibration can yield bIj /∈[0,1]; we treat such
cases as calibration flags rather than as violations of the definition. Formally,
Ij := Cov(ˆaj, a∗ j ) Var(ˆaj) ,(1)
which depends only on the joint distribution of attribution scores (ˆaj, a∗ j ), not on platform revenue.
The definition requires only finite second moments and the regression-slope identification of a∗ j on
ˆaj; the [0,1] bound is conditional on the classical-noise regime noted above. Period-total revenueπ is
the dollar revenue base on which royalties are calculated. We consider π as u(x,·) summed over the
period, taking u as the platform’s gross per-request revenue. The framework also covers cases where
the platform values non-monetary outcomes such as user retention or market position, in which caseπ
is the revenue component within u(x,·) . We adopt the centering convention E[ˆaj] =E[a ∗ j ] = 0 [35]
and assume π⊥(ˆa j, a∗ j ), letting us factor π out of payment-variance calculations. Under additive
Gaussian measurement noise ˆaj =a ∗ j +ξ j with ξj ∼ N(0, σ2 ξ,j ) independent of a∗ j , Ij reduces to
the signal-to-noise-ratio (SNR) form Ij = SNRj /(1 + SNRj), where SNRj := Var(a∗ j )/σ2 ξ,j [53].
The SNR is a foundational measurement-quality metric, widely used across signal processing and
information theory [55, 15]. We use this Gaussian parametrization for examples and simulations; the
structural results (Theorem 1 and Proposition 1) hold for any noise distribution with finite second
moments via the covariance form in eq. (1).
4

Contracts and preferences.The platform–creator interaction is described by three primitives —
the contract space, the creator’s utility, and outside option. The platform offers each creator a linear
contractθ j = (fj, ρj)— a fixed feef j ≥0and a royalty rateρ j ∈[0,1]— with total payment
wj(θj) =x j [fj +ρ j vj], v j = ˆaj π,(2)
nesting three canonical industry forms (pure fixed fee with ρj = 0, pure royalty with fj = 0, and
hybrid with fj >0, ρj >0 ). Creator j evaluates contracts using mean–variance utility — the creator
values expected payment minus a multiple of payment variance [35],
Uj(θj) =f j +ρ j E[vj]− αj 2 ρ2 j Var(vj).(3)
This preference primitive matches a music-industry fact — liquidity-constrained creators value
payment-stream stability, not just expected payment [ 44]. Creator j participates if Uj(θj)≥ ¯Uj,
where ¯Uj is the utility the creator would obtain by not licensing to the platform (e.g., distributing
independently). As more catalogs are licensed and model quality improves, AI-generated music substi-
tutes for the creator’s standalone work. The outside option therefore shrinks, ¯Uj = ¯U 0 j −δ j(x−j, q),
where ¯U 0 j is the creator’s standalone revenue andδ j captures the displacement loss.
3.2 Equilibrium contract and welfare cost
Now we separate the static profit-max contract for a single creator from an attribution-aligned
benchmark for royalty design. Both expressions reduce to closed forms in informativeness Ij and
risk aversion αj, which lets us read off when the benchmark recommends royalty-dominant versus
fixed-fee-dominant payment and how much alignment-relevant surplus is exposed to imperfect
attribution.
We first state the platform’s static licensing problem for a single creator. The platform maximizes
max
θj =(fj ,ρj )
E[π a∗ j ]−f j −ρ j E[vj]s.t.U j(θj)≥ ¯Uj.(4)
The tension is theinformational wedge— the platform pays based on the noisy attributed revenue
vj = ˆajπ but receives value from a∗ j π. Under (4) alone with binding IR, the royalty-induced risk
premium is shifted back onto the platform through the fixed fee, leaving no first-order profit benefit
to a positive ρj (Lemma 1). We therefore characterize anattribution-aligned royalty benchmark:
the royalty rate that balances payment–contribution co-movement against the risk premium induced
by noisy royalty exposure. This benchmark is relevant when the platform, an auditor, or a policy
environment values payment–contribution alignment in addition to expected net surplus. At the
optimum the participation constraint binds, so fj = ¯Uj −ρ jE[vj] + (αj/2)ρ2 j Var(vj) and the
problem reduces to a one-dimensional optimization inρ j.
Lemma 1(Static profit-max baseline).Under (4) with binding IR, substituting the binding-IR fee
fj = ¯Uj −ρ jE[vj] + (αj/2)ρ2 j Var(vj)yields
Πj(ρj) =E[π a∗ j ]− ¯Uj − αj 2 ρ2 j Var(vj),
strictly decreasing in ρ2 j whenever Var(vj)>0 . The unique maximizer is the pure fixed-fee contract
(ρ∗ j , f∗ j ) = (0, ¯Uj). A non-degenerate royalty therefore requires an alignment criterion beyond
expected net surplus; Theorem 1 characterizes the benchmark rate under that criterion.
Theorem 1(Attribution-aligned royalty benchmark).Therisk-adjusted alignment criterion
max
ρj ∈[0,1]
ρj Cov(vj, a∗ j π)− αj 2 ρ2 j Var(vj),(5)
which treats payment–contribution covariance as a design target and penalizes the risk premium
induced by noisy royalty exposure, admits the unique maximizer
ρ∗ j = clip  Ij αj ,[0,1]  .(6)
The interior solution reduces to ρ∗ j =I j/αj; under additive Gaussian noise it further reduces to
ρ∗ j = SNRj /[αj(1 + SNRj)]. The lower boundary binds when Ij/αj <0 , and the upper boundary
binds when Ij/αj >1 . Empirical sign flips (negative bKj, equivalently bIj <0 ; observed for 6/22
5

creators under EKFAC and 3/22 under D-TRAK; see Table 1) and bIj >1 (over-amplified signal)
are reported as calibration flags. The criterion (5) should be read as an explicit benchmark, not as
the maximizer of (4); it is motivated by Holmstrom’s informativeness principle, while Appendix B.3
discusses a complementary endogenous-quality channel. Proof in Appendix B.
The benchmark rate balances alignment against risk transfer. ρ∗ j →1/α j as Ij →1 (royalty-
dominant when attribution is precise), and ρ∗ j →0 as Ij →0 (fixed-fee-dominant when attribution is
too noisy). If the benchmark is implemented through the linear contract, the fixed fee is pinned by the
binding participation constraint, f ∗ j = ¯Uj −ρ ∗ j E[vj] + (αj/2)(ρ∗ j )2 Var(vj). Attribution precision
therefore determines the benchmark split between fixed fee and royalty, while the outside option
determines the transfer level needed for participation. Because the fixed fee implements the transfer
level, surplus-splitting variants that share the same alignment criterion leave the benchmark royalty
ρ∗ j unchanged; asymmetric-criterion extensions are deferred to a future revision.
Theorem 1 yields royalty-dominant benchmark contracts for high-informativeness creators, hybrid
benchmark contracts at mid informativeness, and fixed-fee-dominant benchmark contracts at low
informativeness; Section 4 calibrates these regimes on measured creator pools. The wedge between
the noisy signal and the true value also creates an alignment loss: noisy attribution forces any royalty
component to load risk onto a signal that imperfectly tracks the creator’s true contribution.
Proposition 1(Loss under the attribution-aligned benchmark).Under the attribution-aligned bench-
mark, the loss relative to the perfect-attribution benchmark (Ij = 1) is
Lj = Var(vj) 2αj (1− Ij)2,(7)
and the marginal welfare gain from improving informativeness is

 ∂Lj ∂Ij

 = Var(vj) αj (1− Ij),(8)
which is largest for the noisiest creators (those with Ij farthest from 1). Gaussian-shortcut forms
withSNR j appear in Appendix A. Proof in Appendix B.
This benchmark loss is concentrated among low-informativeness creators (the convex (1− Ij)2
scaling), and the water-filling allocation in Appendix G.3 routes the bulk of a marginal attribution-
improvement budget to them. When the benchmark is implemented through the linear contract, the
creator is compensated for royalty risk through the fixed fee, so the loss appears as surplus that the
platform must spend on risk compensation rather than as value either side can recover from a noisy
signal. Because Lj is computable from measurable quantities, it provides an attribution-method
comparison criterion grounded in cardinal calibration rather than rank correlation alone (Section 4).
Relation to classical contract theory.The signal-informativeness logic behind Theorem 1 is classical
[35, 47, 45]; what is new is that the noisy signal is itself an ML artifact the platform can invest in and
creators can post-process. Linearity is justified under mean-variance utility with Gaussian noise [36];
alternatives in Appendix F.
3.3 Market and policy implications
In real markets, multiple platforms compete for the same catalogs, the same pricing scheme often
applies to many creators, creators choose effort levels, and platforms and creators may not see the
same attribution quality. This subsection translates the framework into stakeholder-specific insights,
covering what platforms should invest in, what creators should expect, what AI researchers should
target, and what regulators should build into institutional infrastructure.
Platforms.Attribution quality is a feature competitors cannot match by lowering fees. The platform
with the most precise attribution holds a sustained advantage; a trailing platform earns nothing on
its attribution investment until it overtakes the leader, even though the market as a whole gains
throughout. Investing in better attribution is therefore the main way to build a lasting lead; lowering
fees only changes who captures the value that better attribution already created.
Proposition 2(Attribution moat).Consider K≥2 platforms competing for catalogs under exclu-
sive licensing, in the equilibrium where each platform’s royalty matches its own informativeness
6

(formalized as Theorem 2 in Appendix E). Assume Gaussian noise and homogeneous demand
(µ(k) j =µ j). Let ∆Ij =I (1) − I(2) >0 denote the gap between leader and trailer, and
σ2 a∗ := Var(a ∗ j ). Then (i) for ϵ∈[0,∆I j], Platform 2’s private return to its own attribution
improvement is exactly zero (dead zone); (ii) for ϵ >∆Ij, Platform 2 captures the creator and earns
Π(2) j (ϵ) = (ϵ−∆I j)σ2 a∗ E[π2]/(2αj); (iii) total welfare is weakly increasing in ϵ throughout, so the
social return is strictly positive while the private return is zero up to the gap, revealingsystematic
underinvestmentin attribution by trailing platforms. Proof and welfare bounds in Appendix E.
The reason why this effect is especially severe in music because catalogs are typically licensed
wholesale. A trailing platform may be unable to bid for a fraction of a catalog to capture partial value;
it earns zero until its attribution precision overtakes the leader’s.
Creators.Two compensation patterns systematically reduce creator welfare. First, the industry
default of uniform compensation policies (Spotify’s per-stream pro-rata, flat-fee blanket licenses,
regulator-set statutory rates) disproportionately hurts creators with distinctive styles. These are
exactly the ones most costly for platforms to lose. A distinctive creator’s contribution cannot be
reproduced by blending other creators’ work, so their exit removes value the platform cannot recover
by reweighting what remains. Losses compound when several distinctive creators exit, costing more
than the sum of their individual exits would suggest.
Second, even within personalized contracts, a sufficiently high royalty rate can reduce creator
effort, because the volatility risk eventually outweighs the higher expected reward (formalized in
Appendix B.3). The contracts of industry norms (“one rate for everyone”) and what looks generous
on paper (“high per-stream pay”) can be the ones that reduce welfare the most.
Proposition 3(Selective exit under uniform contracts).Suppose the platform offers a uniform
contract ( ¯f ,¯ρ)to every creator and let S exit ={j:U j( ¯f ,¯ρ)<¯Uj} be the exit set. If ¯ρis set to the
population average of the creator-specific optima, then (i) creators with the highest outside options
¯Uj exit first, and because distinctive creators tend to have both high ¯Uj and high complementary
value in u, S exit is disproportionately composed of the creators whose loss is most costly to the
platform; (ii) whenuis non-additive, the welfare loss from the exits is superlinear in|S exit|,
u(x, r)−u(x\ Sexit, r)> X
j∈S exit

u(x, r)−u(x\ {j}, r)

.(9)
Proof, the total-welfare-gap decomposition, and comparative statics on¯ρin Appendix D.
Each additional exit costs more than the previous because distinctive musical styles cannot be replaced.
In fields where contributors are interchangeable, losing one costs only what that single contributor
was worth, but in music a high-informativeness creator’s distinctive style cannot be rebuilt from
others, so their exit eliminates every musical combination their style enabled.
AI researchers.The framework gives attribution-method designers two targets. First, two methods
that rank creators identically can prescribe payments differing by orders of magnitude, so numerical
scores matter too, not just rankings. The welfare loss formula Lj (Proposition 1) measures the
gap. Methods used to set creator payments should therefore be evaluated on welfare, not just rank
correlation. Second, some attribution methods let creators cheat in a specific way. A creator can
report scores that look more uniform across outputs than the true scores actually are; this benefits the
creator because the platform pays a premium for steady, low-risk contributions. No filter or detection
step added to the contract can stop this manipulation. The fix has to come from the attribution method
itself, by choosing methods whose mathematical structure prevents this kind of smoothing.
Regulation and institutional design.There are two market failures contracts cannot fix. When
creators and platforms hold different beliefs about attribution quality, creator effort goes off-target
and the resulting welfare loss cannot be undone by adjusting the contract. Only transparency about
the platform’s measured bIj closes the belief gap directly. Without transparency, creators who
overestimate their informativeness over-supply effort while the platform profits from their oversupply;
creators who underestimate exit instead, costing the platform the surplus their participation would
have created. Manipulating attribution scores by shrinking the spread of reports (without changing the
average) is impossible to deter under any linear contract; the only fix is institutional. The attribution
pipeline must have oversight by someone other than the creator (third-party auditor, collection society,
or regulator-mandated infrastructure). Together these results mark where contract design hits its limit
and institutional intervention becomes necessary, not optional.
7

Proposition 4(Score-smoothing manipulation cannot be deterred).Under ˆaj ⊥π (or π≡1 ), for
any mean-preserving shrinkage (compressing the spread of reported scores toward their mean while
keeping the average unchanged) gϵ(ˆa) = (1−ϵ)ˆa+ϵ¯awith ϵ∈(0,1] , the creator’s utility change is
∆U shrink j (ϵ) = αj 2 (ρ∗ j )2 ϵ(2−ϵ) Var(ˆaj)E[π 2]>0.(10)
Profitable for every ρj >0 and thereforeimpossible to deter under any linear contract; full IC
analysis in Appendix C.
Royalty contracts work by tying payment to the attribution score. That same dependency becomes a
vulnerability when creators can change the score before reporting it. The fix is for the platform to
compute attribution itself, rather than trust the numbers creators report.
The framework converts the cost of inaccurate attribution into a concrete per-creator number Lj,
which can be measured, compared across attribution methods, and used to direct investment where it
helps most (Corollary 4 in Appendix G.3). The largest welfare gains from improving attribution go to
creators who look least valuable under today’s noisy measurement.
4 Empirical instrument and measurement
Data-attribution methods are usually evaluated by rank correlation, but the welfare formula in §3 uses
cardinal calibration, not just ranks. We apply the framework’s instrument across two settings, audio
latent diffusion (Stable Audio Open [24]) with EKFAC [46] and D-TRAK [62], and a symbolic LM
(Anticipatory Music Transformer [58]) with LoGra [11] and TRAK [48], and ask whether current
attribution delivers what royalty regimes need. A market-simulation companion in Appendix G.4
draws priors from the same measurement.
4.1 Setting 1 — Latent-diffusion audio attribution
Setup.We fine-tune Stable Audio Open [ 24] on 22 artist catalogs from MTG-Jamendo [8], retraining
22 leave-catalog-out variants alongside one full-catalog model, and evaluate on 200 generated
outputs. Ground truth is the loss-delta on each generation when its creator’s catalog is held out of
training (formal definition and sanity checks in Appendix G.1). We benchmark EKFAC [ 46] and
D-TRAK [62] and report three quantities per (method, creator). These are informativeness bIj from
§3, calibration scale bKj (regression slope of measured attribution on truth), and calibrated SNR
[SNR
cal
j = dVar(a∗ j )/dVar(ˆaj/ bKj −a ∗ j ).
Cardinal measurement uncovers signal rank metrics miss.Both audio methods produce a small
but real cardinal signal against the ground truth, several-fold stronger than rank correlations alone
(Figure 2(a); per-method numbers in Table 1). Rank-based evaluation [48, 37] discards exactly the
cardinal calibration that the welfare loss formulaL j in Proposition 1 uses.
Rank-equivalent methods disagree on calibration.EKFAC and D-TRAK match on Spearman
but produce calibration scales bKj differing by roughly 103× (Figure 2(b)). Several creators show
attribution scores with opposite signs across methods, including the pool’s most genre-coherent
catalog (a 31-track classical artist) under EKFAC. Because welfare loss Lj in Proposition 1 depends
on calibration, methods that look equivalent under rank correlation prescribe materially different
contracts.
Current attribution closes about 10% of the welfare gap.Current methods close only the first
10% of the welfare gap that royalty-grade attribution would close. At most 1 of 22 creators clears the
royalty threshold— the precision at which royalty payment delivers more welfare than a fixed fee —
under either audio method (Figure 2(c)); the other 21 sit where each unit of precision improvement
pays off most (Figure 2(d)). Per-creator headline statistics and bootstrap CIs are in Appendix G.2.
4.2 Setting 2 — Symbolic music attribution
We also conduct pilot measurements in the symbolic domain, consistent with parameters of a
commercially deployed music co-creation product [ 21, 41]. The pilot fine-tunes an Anticipatory
8

Spearman Pearson
0.0
0.1
0.2
0.3
0.4mean correlation
~3× gap, all methods
Cardinal vs rank
(A) EKFAC
(A) D-TRAK
(S) LoGra
(S) TRAK
(A) EKFAC(A) D-TRAK(S) LoGra(S) TRAK
10 8
10 5
10 2
101
104
|scale factor|  (log)
Calibration scale
(A) EKFAC(A) D-TRAK(S) LoGra(S) TRAK
0.0
0.5
1.0
1.5
2.0calibrated SNR
royalty
threshold
SNR distribution
(A) EKFAC(A) D-TRAK(S) LoGra(S) TRAK
0
10
20
30
40
50
60% gap closed
SNR=1
target
10.6% 9.8%
6.5%
1.4%
Welfare gap closed
Figure 2: Attribution measurement on two settings, audio diffusion (Stable Audio Open with EKFAC
and D-TRAK, 22 catalogs) and symbolic language modeling (Anticipatory Music Transformer with
LoGra and TRAK, 100 artists). Across both settings and all four methods, almost no creator’s
attribution is precise enough for royalty payment to beat a fixed fee under the attribution-aligned
benchmark, which is fixed-fee-dominant for nearly the entire measured pool.(a)Per-query rank and
cardinal correlation against the leave-catalog-out ground truth.(b)Per-creator calibration scale, log
axis.(c)Calibrated-SNR distribution per method, dashed line at the royalty threshold.(d)Welfare
gap closed atα=2.
Music Transformer [58] on 100 TheoryTab artists, generates 500 outputs per model under the same
leave-catalog-out protocol, and measures the same three quantities using LoGra [11] and TRAK [48].
Cross-domain consistency confirms a shortfall across methods.Two completely different settings
(audio diffusion vs. symbolic transformer, four different attribution methods, two domains) return the
same diagnosis. Symbolic Spearman and Pearson sit in the same regime as Setting 1’s, calibrated
SNR is roughly an order of magnitude below the royalty threshold, and no creator clears the threshold
under either symbolic method. The attribution-precision shortfall is a property of current ML methods
broadly, not an artifact of any single architecture or modality.
The instrument discriminates between methods more sharply on symbolic.On symbolic data,
LoGra clearly outperforms TRAK; on audio, EKFAC and D-TRAK look more comparable on rank
but differ by orders of magnitude in calibration scale. The cross-method calibration gap on symbolic
(∼10 13) is even larger than on audio (∼10 3), so the rank-vs-cardinal split that the framework first
flagged in Setting 1 is amplified, not erased, by switching model class. Methods that look similar
under rank correlation prescribe materially different contracts on the same pool.
Implication for the framework’s prescription.Both settings sit deep inside the noisy regime where
each unit of attribution improvement pays off most. The cross-setting consistency strengthens the
central empirical conclusion. Under current attribution capability, the attribution-aligned benchmark
is fixed-fee-dominant across the model classes we measured, and royalty-heavy regimes require
precision improvements not yet delivered by any tested method.
4.3 Musical market simulation
We instantiate the framework’s attribution-aligned benchmark on the per-creator quantities measured
above, then ask how much SNR improvement would be needed to make royalty regimes viable under
that benchmark.
Contract form across the population.For each creator j and risk-aversion level α the benchmark
royalty rate is ρ∗ j = bI cal j /α after clipping to [0,1] (regime classification in Figure 3(a)). At α= 2 ,
no creator out of 22 clears the royalty threshold under either audio method (Figure 3(b)); the only
royalty-eligible case under any setting is a31-track classical-music catalog at α≤1 on D-TRAK. The
framework’s prescription is near-universal fixed-fee at typical risk aversion, matching the dominant
industry pattern of blanket licensing. The Setting 2 (symbolic) population yields a similarly fixed-fee-
dominant prescription.
Welfare counterfactual under attribution improvements.We ask how much SNR improvement
would be needed to close more of the gap (Figure 3(c), formula in Appendix G.4). Closing 50%
requires 25–40× improvement in calibrated SNR, raising the median creator from today’s ≈0.05 to
≈1. This is a concrete precision target for royalty-based AI music compensation to become viable.
Multi-platform competition.Treating EKFAC and D-TRAK as two competing platforms in the
Bertrand equilibrium of Theorem 2 yields a per-creator winner (EKFAC for 14 of 22 creators, D-
9

0.00 0.25 0.50
calibrated cal
0.00
0.25
0.50
0.75
1.00optimal *
royalty
hybrid
fixed fee
Contract form
= 0.5
= 2
EKFAC
D-TRAK
0.5 1 2 3 4 5
risk aversion
0
10
20
30creators (of 22)
Regime vs
fixed fee hybrid
royalty
100
 0 100 101
precision scaling s
0
25
50
75
100% gap closed
50%
Welfare frontier
EKFAC
D-TRAK
10 10
 10 7
EKFAC surplus
10 11
10 9
10 7
10 5
D-TRAK surplus EKFAC wins 14
D-TRAK wins 8
Bertrand competition
Figure 3: Framework prescription on the measured creator pool, 22 catalogs under EKFAC and
D-TRAK.(a)Optimal royalty rate versus calibrated informativeness at α=2, with hybrid and royalty
thresholds.(b)Contract-form counts across risk-aversion levels under EKFAC.(c)Welfare gap
closed as calibrated SNR is scaled.(d)Per-creator surplus, EKFAC versus D-TRAK, log–log axes.
TRAK for 8; Figure 3(d)). The per-creator surplus gap between methods realizes Proposition 2’s
underinvestment prediction on a measured pool rather than a hypothetical one. The median gap is
small enough that neither platform gains enough from improving its own attribution to overtake the
other, even where investing would help society overall. Full per-creator analysis is in Appendix G.4.
5 Conclusion
We propose a framework for compensating music creators whose work trains generative AI, where
each creator’s contract form follows from how accurately the platform can trace generated outputs
back to their catalog. As generative AI takes a larger share of music production, the choice of
attribution technology will increasingly shape who gets paid, and our framework gives platforms,
creators, and policymakers a shared way to reason about that choice. Future work could extend it to
catalogs that grow over time, generative models spanning music and other media, and institutional
setups for attribution oversight.
References
[1] D. Acemoglu, A. Makhdoumi, A. Malekian, and A. Ozdaglar. Too much data: Prices and
inefficiencies in data markets.American Economic Journal: Microeconomics, 14(4):218–256,
2022.
[2] A. Agarwal, M. Dahleh, and T. Sarkar. A marketplace for data: An algorithmic solution. In
Proceedings of the 2019 ACM Conference on Economics and Computation, pages 701–726,
2019.
[3] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caber, N. Zeghidour, and
C. Frank. MusicLM: Generating music from text, 2023. arXiv preprint arXiv:2301.11325.
[4] G. A. Akerlof. The market for “lemons”: Quality uncertainty and the market mechanism.The
Quarterly Journal of Economics, 84(3):488–500, 1970.
[5] J. Bae, W. Lin, J. Lorraine, and R. Grosse. Training data attribution via approximate unrolled
differentiation. InAdvances in Neural Information Processing Systems (NeurIPS), 2024.
[6] J. Barnett, H. Flores Garcia, and B. Pardo. Exploring musical roots: Applying audio embed-
dings to empower influence attribution for a generative music model, 2024. arXiv preprint
arXiv:2401.14542.
[7] D. Bergemann, A. Bonatti, and A. Smolin. The design and price of information.American
Economic Review, 108(1):1–48, 2018.
[8] D. Bogdanov, M. Won, P. Tovstogan, A. Porter, and X. Serra. The MTG-Jamendo dataset for
automatic music tagging. InMachine Learning for Music Discovery Workshop, International
Conference on Machine Learning (ICML), 2019.
[9] A. Caillon, B. McWilliams, C. Tarakajian, I. Simon, I. Manco, J. Engel, N. Constant, Y . Li,
et al. Live music models. InAdvances in Neural Information Processing Systems (NeurIPS),
Creative AI Track, 2025. arXiv preprint arXiv:2508.04651.
[10] Y . Chen, H. Liu, and A. Karbasi. Selling data to a machine learner. InInternational Conference
on Machine Learning (ICML), 2022.
10

[11] Sang Keun Choe, Hwijeen Ahn, Juhan Bae, Kewen Zhao, Minsoo Kang, Youngseog Chung,
Adithya Pratapa, Willie Neiswanger, Emma Strubell, Teruko Mitamura, et al. What is
your data worth to gpt? llm-scale data valuation with influence functions.arXiv preprint
arXiv:2405.13954, 2024.
[12] W. Choi, J. Koo, K. W. Cheuk, J. Serrà, M. A. Martinez-Ramirez, Y . Ikemiya, N. Murata,
Y . Takida, W.-H. Liao, and Y . Mitsufuji. Large-scale training data attribution for music generative
models via unlearning. InAdvances in Neural Information Processing Systems (NeurIPS),
Creative AI Track, 2025.
[13] L. W. Cong, W. Wei, D. Xie, and L. Zhang. Data, ai, and economic growth. Nber working
paper, NBER, 2022.
[14] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y . Adi, and A. Défossez. Simple
and controllable music generation. InAdvances in Neural Information Processing Systems
(NeurIPS), 2023.
[15] T. M. Cover and J. A. Thomas.Elements of Information Theory. Wiley-Interscience, 2nd
edition, 2006.
[16] Deezer. Deezer: AI-generated tracks now represent 44% of all new uploaded mu-
sic. Deezer Newsroom, 2026. URL https://newsroom.deezer.com/2026/04/ai-
generated-tracks-represent-44-of-new-uploaded-music/ . Published April 20,
2026.
[17] J. Deng, X. Jiang, S. Zhang, S. Zhang, H. Lakkaraju, R. Gao, C. Donahue, and J. Ma. Com-
putational copyright: Towards a royalty model for music generative AI, 2023. arXiv preprint
arXiv:2312.06646.
[18] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever. Jukebox: A generative
model for music, 2020. arXiv preprint arXiv:2005.00341.
[19] S. Dieleman, A. van den Oord, and K. Simonyan. The challenge of realistic music generation:
modelling raw audio at scale. InAdvances in Neural Information Processing Systems (NeurIPS),
2018.
[20] Chris Donahue, John Thickstun, and Percy Liang. Melody transcription via generative pre-
training. InISMIR, 2022.
[21] Chris Donahue, Shih-Lun Wu, Yewon Kim, Dave Carlton, Ryan Miyakawa, and John Thickstun.
Hookpad aria: A copilot for songwriters.arXiv preprint arXiv:2502.08122, 2025.
[22] L. Engstrom, A. Feldmann, and A. M ˛ adry. DsDm: Model-aware dataset selection with data-
models. InInternational Conference on Machine Learning (ICML), 2024.
[23] European Parliament and Council of the European Union. Regulation (EU) 2024/1689 laying
down harmonised rules on artificial intelligence (AI act). Technical report, European Parliament
and Council of the European Union, 2024. Official Journal of the European Union.
[24] Z. Evans, J. D. Parker, C. J. Carr, Z. Zukowski, J. Taylor, and J. Pons. Stable Audio Open, 2024.
arXiv preprint arXiv:2407.14358.
[25] S. Forsgren and H. Martiros. Riffusion: Stable diffusion for real-time music generation, 2022.
URLhttps://riffusion.com/about.
[26] K. Georgiev, J. Vendrow, H. Salman, S. M. Park, and A. Madry. The journey, not the destination:
How data guides diffusion models, 2023. arXiv preprint arXiv:2312.06205.
[27] A. Ghorbani and J. Zou. Data Shapley: Equitable valuation of data for machine learning. In
Proceedings of the 36th International Conference on Machine Learning, pages 2242–2251,
2019.
[28] R. Giordano, W. Stephenson, R. Liu, M. Jordan, and T. Broderick. A Swiss army infinitesimal
jackknife. InProceedings of the 22nd International Conference on Artificial Intelligence and
Statistics, pages 1139–1147, 2019.
[29] J. Gong, Y . Song, W. Zhao, S. Wang, S. Xu, J. Guo, and X. Yang. ACE-Step 1.5: Pushing the
boundaries of open-source music generation, 2026. arXiv preprint arXiv:2602.00744.
[30] R. Grosse, J. Bae, C. Anil, N. Elhage, A. Tamkin, A. Tajdini, B. Steiner, D. Li, E. Durmus,
E. Perez, E. Hubinger, K. Lukosiute, K. Nguyen, N. Joseph, S. McCandlish, J. Kaplan, and S. R.
11

Bowman. Studying large language model generalization with influence functions, 2023. arXiv
preprint arXiv:2308.03296.
[31] R. Grosse, J. Bae, C. Anil, et al. Studying large language model generalization with influence
functions, 2023. arXiv preprint arXiv:2308.03296.
[32] G. Guruganesh, J. Schneider, and J. R. Wang. Contracts under moral hazard and adverse
selection. InProceedings of the 22nd ACM Conference on Economics and Computation (EC),
2021.
[33] J. Hirshleifer. The private and social value of information and the reward to inventive activity.
The American Economic Review, 61(4):561–574, 1971.
[34] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. InAdvances in Neural
Information Processing Systems (NeurIPS), 2020.
[35] B. Holmström. Moral hazard and observability.The Bell Journal of Economics, 10(1):74–91,
1979.
[36] B. Holmström and P. Milgrom. Aggregation and linearity in the provision of intertemporal
incentives.Econometrica, 55(2):303–328, 1987.
[37] A. Ilyas, S. M. Park, L. Engstrom, G. Leclerc, and A. Madry. Datamodels: Predicting predictions
from training data. InProceedings of the 39th International Conference on Machine Learning,
pages 9525–9587, 2022.
[38] International Federation of the Phonographic Industry (IFPI). Global music report 2025.
Technical report, IFPI, 2025.
[39] R. Jia, D. Dao, B. Wang, F. A. Hubis, N. Hynes, N. M. Gürel, B. Li, C. Zhang, D. Song, and
C. Spanos. Towards efficient data valuation based on the Shapley value. InProceedings of the
22nd International Conference on Artificial Intelligence and Statistics, pages 1167–1176, 2019.
[40] C. I. Jones and C. Tonetti. Nonrivalry and the economics of data.American Economic Review,
110(9):2819–2858, 2020.
[41] Yewon Kim, Sung-Ju Lee, and Chris Donahue. Amuse: Human-ai collaborative songwriting
with multimodal inspirations. InProceedings of the 2025 CHI conference on human factors in
computing systems, pages 1–28, 2025.
[42] P. W. Koh and P. Liang. Understanding black-box predictions via influence functions. In
Proceedings of the 34th International Conference on Machine Learning, pages 1885–1894,
2017.
[43] Y . Kwon, E. Wu, K. Wu, and J. Zou. DataInf: Efficiently estimating data influence in LoRA-
tuned LLMs and diffusion models. InInternational Conference on Learning Representations
(ICLR), 2024.
[44] H. Markowitz. Portfolio selection.The Journal of Finance, 7(1):77–91, 1952.
[45] E. Maskin and J. Riley. Monopoly with incomplete information.The RAND Journal of
Economics, 15(2):171–196, 1984.
[46] Bruno Kacper Mlodozeniec, Runa Eschenhagen, Juhan Bae, Alexander Immer, David Krueger,
and Richard E. Turner. Influence functions for scalable data attribution in diffusion models.
InInternational Conference on Learning Representations (ICLR), 2025. URL https://
openreview.net/forum?id=esYrEndGsr.
[47] M. Mussa and S. Rosen. Monopoly and product quality.Journal of Economic Theory, 18(2):
301–317, 1978.
[48] S. M. Park, K. Georgiev, A. Ilyas, G. Leclerc, and A. Madry. TRAK: Attributing model behavior
at scale. InProceedings of the 40th International Conference on Machine Learning, pages
27074–27113, 2023.
[49] J. W. Pratt. Risk aversion in the small and in the large.Econometrica, 32(1/2):122–136, 1964.
[50] G. Pruthi, F. Liu, S. Kale, and M. Sundararajan. Estimating training data influence by tracing
gradient descent. InAdvances in Neural Information Processing Systems (NeurIPS), 2020.
[51] Recording Industry Association of America (RIAA). Major record labels file copyright in-
fringement suits against AI music generators Suno and Udio. Press release, Recording Industry
Association of America (RIAA), 2024. Press release, June 2024.
12

[52] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer. High-resolution image synthesis
with latent diffusion models. InProceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR), 2022.
[53] L. L. Scharf.Statistical Signal Processing: Detection, Estimation, and Time Series Analysis.
Addison-Wesley, 1991.
[54] J. Serrà, E. Gómez, and P. Herrera. Audio cover song identification and similarity: Background,
approaches, evaluation, and beyond. InAdvances in Music Information Retrieval, pages
307–332. Springer, 2010.
[55] C. E. Shannon. A mathematical theory of communication.The Bell System Technical Journal,
27(3):379–423, 1948.
[56] A. Silberling. AI music generator Suno hits 2M paid subscribers and $300M in annual recurring
revenue. TechCrunch, 2026. URL https://techcrunch.com/2026/02/27/ai-music-
generator-suno-hits-2-million-paid-subscribers-and-300m-in-annual-
recurring-revenue/. Published February 27, 2026.
[57] J. Spijkervet and J. A. Burgoyne. Contrastive learning of musical representations. InProceedings
of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021.
[58] John Thickstun, David Hall, Chris Donahue, and Percy Liang. Anticipatory music transformer.
TMLR, 2024.
[59] A. van den Oord, O. Vinyals, and K. Kavukcuoglu. Neural discrete representation learning. In
Advances in Neural Information Processing Systems (NeurIPS), 2017.
[60] A. L.-C. Wang. An industrial-strength audio search algorithm. InProceedings of the 4th
International Conference on Music Information Retrieval (ISMIR), pages 7–13, 2003.
[61] L. Zhang, C. Jiao, B. Li, and C. Xiong. Fairshare data pricing via data valuation for large
language models. InAdvances in Neural Information Processing Systems (NeurIPS), 2025.
[62] X. Zheng, T. Pang, C. Du, Q. Liu, J. Jiang, and M. Lin. Intriguing properties of data attribution
on diffusion models. InInternational Conference on Learning Representations (ICLR), 2024.
13

A Gaussian special case and simplifying conditions
The main results (Theorem 1, Propositions 1–3) hold for any noise structure through the general
informativeness measure Ij. The closed-form SNR expressions used in examples and simulations
require three additional conditions, stated here for reference.
Additive Gaussian noise. ˆaj =a ∗ j +ξ j, with ξj ∼ N(0, σ2 ξ,j ) independent of a∗ j and π. This
yields Ij = SNR j /(1 + SNRj) and the closed-form ρ∗ = 1 αj · SNRj 1+SNRj . Under the additional
revenue-independence condition below, the welfare loss in eq.(7) reduces to the Gaussian-shortcut
form
Lj = E[π2] Var(a∗ j ) 2αj SNRj(1 + SNRj) ,(11)
and the marginal welfare gain from improvingSNR j is

 ∂Lj ∂SNR j

 = E[π2] Var(a∗ j ) (2 SNRj +1) 2αj SNR2 j (1 + SNRj)2 ,(12)
which scales as1/SNR 2 j at low precision.
Multiplicative-bias regime and calibration.A common generalization is ˆaj =K j ·a ∗ j +ξ j
with ξj ⊥a ∗ j and ξj ∼ N(0, σ2 ξ,j ), which arises naturally for gradient-based attribution methods
that estimate scores up to a method-specific scale (Section 3.1). Under this model, the calibrated
estimator ˜aj = ˆaj/Kj satisfies ˜aj =a ∗ j +ξ j/Kj, returning the additive Gaussian regime with
SNRcal j =K 2 j ·SNR j. The benchmark payment rule should be evaluated on the calibrated signal
when the Gaussian shortcut is used: I cal j = SNR cal j /(1 + SNRcal j ), while the raw uncalibrated
regression slope satisfies I raw j = SNR cal j /[Kj(1 + SNRcal j )]. Thus the welfare-loss formula in
equation (7) requires the calibrated [SNR
cal
when expressed via the Gaussian shortcut. The proof is a
one-line algebra exercise onCov(ˆa, a∗) =K j Var(a∗)andVar(ˆa) =K 2 j Var(a∗) + Var(ξ).
Revenue independence. a∗ j ⊥π|x : individual attribution does not predict total platform revenue,
conditional on the active set. This simplifies Var(a∗ j ·π) =E[π 2] Var(a∗ j ) and is plausible when
individual contributions are small relative to the full catalog.
Non-additive utility.The selective-exit result (Proposition 3) and the cross-creator substitution
argument apply to settings where u(x, r)is non-additive across creators — some creators are
complements (superadditive), others substitutes (submodular). This is a property of the platform’s
value function, not a distributional assumption on the attribution signal.
B Full proofs and the quality-choice extension
This appendix contains the full proofs of the main-text results, followed by the formal extension to
endogenous quality choice in Appendix B.3, referenced from the main-text forward pointer.
B.1 Proof of Theorem 1
Proof of Theorem 1. The theorem maximizes the risk-adjusted alignment criterion (5), which is
distinct from the platform-profit objective (4). The latter is handled by Lemma 1 and gives the pure
fixed-fee baseline.
Under the model assumptions π⊥(ˆa j, a∗ j ) and the centering convention E[ˆaj] =E[a ∗ j ] = 0 ,
independence and zero means give
Cov(vj, a∗ j π) =E[π 2] Cov(ˆaj, a∗ j ),Var(v j) =E[π 2] Var(ˆaj).
The first-order condition for (5) gives the interior maximizer
ρint j = Cov(vj, a∗ j π) αj Var(vj) = Cov(ˆaj, a∗ j ) αj Var(ˆaj) = Ij αj .
14

The second-order condition is −αj Var(vj)<0 , so the criterion is strictly concave whenever
Var(vj)>0 . Imposing the contract-space constraint ρj ∈[0,1] projects the interior maximizer onto
the feasible interval, yieldingρ ∗ j = clip(Ij/αj,[0,1]).
For the Gaussian special case,ˆaj =a ∗ j +ξj with ξj independent of a∗ j gives Ij = SNRj /(1+SNR j),
so the interior benchmark rate isρ ∗ j = SNRj /[αj(1 + SNRj)].
B.2 Proof of Proposition 1
Proof of Proposition 1. For the attribution-aligned benchmark, the reduced criterion as a function of
ρj is
Jj(ρj) =− αj 2 ρ2 j Var(vj) +ρ j Cov(vj, a∗ j π),
up to terms independent of ρj. Under the model assumptions (π⊥(ˆa j, a∗ j ) and centering E[ˆaj] =
E[a∗ j ] = 0), the covariance identity Cov(vj, a∗ j π) =I j Var(vj) holds. Completing the square around
ρ∗ j =I j/αj gives
− αj
2 ρ2 j Var(vj) +ρ jIj Var(vj) =− αj Var(vj) 2  ρj −ρ ∗ j 2 + Var(vj) 2αj I 2 j .
Thus
Jj(ρj) = Var(vj) 2αj I 2 j − αj Var(vj) 2  ρj −ρ ∗ j 2 .(13)
The benchmark loss reported in the main text is the quadratic gap induced by moving from the
perfect-attribution benchmark rate ρFB j = 1/αj to the noisy-attribution benchmark rate ρ∗ j =I j/αj,
evaluated under the same variance normalization:
Lj = αj Var(vj) 2  ρFB j −ρ ∗ j 2 = Var(vj) 2αj (1− Ij)2.
In the Gaussian special case, substitute Ij = SNRj /(1 + SNRj) and the variance convention used
in the simulations to obtain the SNR form stated in Appendix A.
B.3 Endogenous quality choice
The static framework of Section 3 takes the creator’s contributiona∗ j as exogenous. We now allow
the creator to choose effort qj that scales their contribution multiplicatively, so platform value from
creatorjisq j ·a ∗ j π.
Setup.Adopt the following extension of the main-text assumptions:
(Q1) Multiplicative scaling.Quality enters multiplicatively: platform value from creator j is qj ·a ∗ j π.
Under multiplicative scaling,I j is invariant toq j (theq 2 j cancels inCovoverVar).
(Q2) Participation.Outside option ¯Uj does not depend on ρj; the IR constraint binds at the optimum.
(Q3) Sequential timing.The platform commits to θj = (fj, ρj), after which the creator chooses
effortq j to maximize
Uj(θj, q) =fj +ρ jqµj − Aj 2 ρ2 j q2 − γj 2 q2,
whereµ j :=E[v j],A j :=α jσ2 v,j,D j(ρ) :=A jρ2 +γ j, andγ j >0is the marginal effort cost.
(Q4) Unbiased attribution. E[ˆajπ] =E[a ∗ j π], so the platform’s expected gross benefit from effort is
qjµj.
Proof of the endogenous-quality-choice result. The creator’s objective is strictly concave in q
(∂2Uj/∂q 2 =−D j <0 ). The corner q= 0 is excluded since ∂Uj/∂q

 q=0 =ρµ >0 . The interior
FOC gives qint =ρµ/D . Differentiating: dq∗/dρ=µ(γ−Aρ 2)/D2, positive iff ρ < p γ/A. The
peak is obtained by substituting ρmax = p γ/A into qint. Comparative statics in γj and αj follow
fromDbeing strictly increasing in both.
15

Welfare-maximizing royalty.The hump-shape implies that the welfare-maximizing royalty—which
maximizes the effort surplusWj(ρ) =µ 2 j ρ(2−ρ)/[2D j(ρ)]—generically exceeds the alignment-only
optimumρ ∗ j =I j/αj.
Proposition 5(Effort-only optimal royalty).The unique maximizer ofW j on(0,1)is
ρ∗∗ j = −γj +
q
γ2 j + 4Ajγj
2Aj
,0< ρ ∗∗ j <1.
Proof.W ′ j(ρ) =µ 2 j h(ρ)/Dj(ρ)2 where h(ρ) =−A jρ2 −γ jρ+γ j. Setting h= 0 and applying the
quadratic formula yields the positive root. The intermediate-value theorem confirms the root lies in
(0,1)sinceh(0) =γ j >0andh(1) =−A j <0.
Proposition 6(Royalty hierarchy).Under (Q1)–(Q4) with βj :=A j/γj <1 and ρ∗ j < ρ∗∗ j , we have
ρ∗∗ j > ρ∗ j . A sufficient condition is αj ≥1 and βj <1 . As γj → ∞, ρ∗∗ j →1 and the effort channel
becomes negligible: total welfare is governed by the alignment channel and the optimal payment rule
converges toρ ∗ j =I j/αj.
Proof. Since Wj is strictly increasing on (0, ρ∗∗ j ) (from W ′ j >0 when h >0) and ρ∗ j < ρ∗∗ j by
hypothesis, W ′ j(ρ∗ j )>0 , so raising the royalty above ρ∗ j improves effort welfare. The alignment loss
Lj is ρ-independent under (Q1), so there is no first-order cost. As γj → ∞, q∗ j →0 and Wj(ρ)→0
uniformly; the static alignment channel dominates, and the optimum converges toρ ∗ j .
The economic interpretation is that the alignment channel of Theorem 1 captures only the cost of
measurement noise; under endogenous effort, the royalty also serves a moral-hazard role, and the
welfare-optimal rate trades off the two. At pilot parameters ( α= 2 , β≈0.02 ), ρ∗∗ j ≈0.98 for all
three creators, an order of magnitude above the alignment-onlyρ ∗ j ≤0.378.
Note on remaining proofs.The cross-tier substitution argument from Section 3.1 is in Appendix D,
where the uniform-contract proof handles the welfare gap between personalized and uniform rates.
The dynamic Bellman equation and two-regime characterization for participation appear in Ap-
pendix I.
C Incentive compatibility: full analysis
This appendix develops the full incentive-compatibility machinery underlying the score-smoothing
analysis (Section 3.3). We give the proof of the three-tier hierarchy, characterize when monitoring
frictions deter Tier 2 (mean inflation) bias, work out the screening problem when risk aversion αj is
private information, derive a complementary statistical detection test for Tier 3 (variance shrinkage),
and show that the IC hierarchy is invariant to the competitive environment under exclusive licensing.
Throughout we use the notation of Section 3.1: vj = ˆajπ, σ2 v,j = Var(vj), ρ∗ j =I j/αj, and the
creator’s mean–variance utility (3). The single-platform variance σ2 v,j is the K= 1 specialization of
the per-platform varianceV (k) j = Var(v(k) j )used in Appendix E.
C.1 Proof of the three-tier hierarchy
We give the formal version of the three-tier hierarchy whose Tier 3 conclusion appears as Proposition 4
in the main text.
Proposition 7(Three-tier creator manipulation hierarchy).Fix ρ∗ j =I j/αj from Theorem 1. Con-
sider three post-contractual distortions of the reportedˆaj:
(T1) Noise inflation.The creator adds independent noise η⊥(ˆa, a∗, π)with E[η] = 0, Var(η) =
Ση >0at private costc≥0. The creator’s utility change is
∆U noise j =− αj 2 (ρ∗ j )2ΣηE[π2]−c <0.
Tier 1 is automatically deterred for everyα j >0andρ ∗ j >0.
16

(T2) Mean inflation.The creator adds bias b≥0 at quadratic cost (κ/2)b2, κ >0. The interior-bias
maximizer is
b∗ j = max  0, ρ∗ j ¯π−αj(ρ∗ j )2 Cov(vj, π) κ+α j(ρ∗ j )2σ2π  .
Under π≡1 this simplifies to b∗ j =I j/(αjκ)>0 . Tier 2 is not self-policing: external monitoring
(κlarge enough) is required to enforce truthfulness.
(T3) Variance shrinkage.Assume ˆaj ⊥π or π≡1 . For any mean-preserving shrinkage gϵ(ˆa) =
(1−ϵ)ˆa+ϵ¯awithϵ∈(0,1],
∆U shrink j (ϵ) = αj 2 (ρ∗ j )2 ϵ(2−ϵ) Var(ˆaj)E[π 2]>0.
Tier 3 is impossible to deter under any linear contract withρ j >0.
Proof. (T1).Let ˜v=v+ηπ . By independence and E[η] = 0, E[ηπ] =E[η]E[π] = 0 , so the mean
is preserved. By the tower property, Cov(v, ηπ) =E[ˆaπ2E[η|ˆa, a∗, π]] = 0. Independence gives
Var(ηπ) =E[η 2]E[π2] = Σ ηE[π2]. Hence Var(˜v) = Var(v) + ΣηE[π2], and the creator’s utility
change is−(α j/2)(ρ∗ j )2ΣηE[π2]−c, which is strictly negative.
(T2).Adding b replaces v with v+bπ . The creator solves maxb≥0 ρ∗ j ¯πb−(αj/2)(ρ∗ j )2(b2σ2 π +
2bCov(v, π))−(κ/2)b2. The objective is strictly concave (SOC: −κ−α j(ρ∗ j )2σ2 π <0 ); the interior
FOC and theb≥0constraint give the statedb ∗ j .
(T3).Under ˆaj ⊥π , mean preservation: E[gϵ(ˆa)π] = ¯a¯π=E[ˆaπ]. Apply the product-of-
independents variance identity (Lemma 2): Var(gϵ(ˆa)π) = (1−ϵ)2 Var(ˆa)E[π2] + ¯a2 Var(π) and
Var(ˆaπ) = Var(ˆa)E[π2]+ ¯a2 Var(π). The variance reduction is ϵ(2−ϵ) Var(ˆa)E[π2]; the ¯a2 Var(π)
term cancels exactly. Mean payment is unchanged, so the utility change is (αj/2)(ρ∗ j )2 ϵ(2−
ϵ) Var(ˆa)E[π2]>0.
Lemma 2(Product of independents).For X⊥Y with finite second moments, Var(XY) =
Var(X)E[Y 2] +E[X] 2 Var(Y).
Proof.Var(XY) =E[X 2Y 2]−E[XY] 2 =E[X 2]E[Y 2]−E[X] 2E[Y] 2 = (Var(X) +
E[X] 2)E[Y 2]−E[X] 2E[Y] 2 = Var(X)E[Y 2] +E[X] 2 Var(Y).
Tightness.Each hypothesis binds. Tier 1: at αj = 0 the variance penalty vanishes and Tier 1 fails
weakly when c= 0 . Tier 2: κ= 0⇒b ∗ → ∞. Tier 3: Var(ˆaj) = 0 removes any variance to reduce,
and ρ∗ j = 0 disconnects payment from ˆa. The condition ˆaj ⊥π (or π≡1 ) is used in Tier 3; the
general-π analysis (Remark 1) shows the SNR2 ratio bound is tight in the uniform-demand limit and
strictly bounded above otherwise.
C.2 SNR-squared manipulation–welfare ratio
Corollary 1(SNR 2 manipulation–welfare ratio).Under π≡1 , the ratio of the maximum Tier 3
manipulation gain (atϵ= 1) to the welfare loss from Proposition 1 is
∆U max j
Lj
=
 Ij
1− Ij
2
= SNR2 j .
Proof. From Proposition 7, ∆U max j = (α j/2)(ρ∗ j )2 Var(ˆaj) =I 2 j Var(ˆaj)/(2αj) at E[π2] = 1 .
Under π≡1 , Var(vj) = Var(ˆaj). Substituting into Proposition 1: Lj = Var(ˆaj)(1− Ij)2/(2αj).
The ratio isI 2 j /(1− Ij)2 = SNR2 j.
Remark 1(General- π upper bound).When π is stochastic and ˆaj ⊥π , Lemma 2 gives Var(vj) =
Var(ˆaj)E[π2] + ¯a2 Var(π)≥Var(ˆaj)E[π2], so
∆U max j
Lj
= SNR2 j · Var(ˆaj)E[π2] Var(ˆaj)E[π2] + ¯a2 Var(π) ≤SNR 2 j ,
with equality iff ¯a= 0or Var(π) = 0. The bound is therefore conservative in the natural direction:
SNR2 j is an upper bound on the manipulation–welfare ratio, attained in the uniform-demand limit.
17

The policy implication is that monitoring expenditure should scale super-linearly in attribution
precision: the most precisely measured creators are simultaneously the lowest-loss and the most
exposed to Tier 3 manipulation.
C.3 Statistical detection of Tier-3 manipulation
Although Tier 3 cannot bedeterredby any linear contract, it can often bedetectedfrom a finite
history of reportedˆa.
Remark 2(Variance-ratio test).Under a Gaussian model, a variance-ratio test on the empirical
distribution of reportedˆaoverTperiods has statistic
Tstat = (T−1) dVar(ˆarep)/Var(ˆacal),
distributed χ2 T−1 under truthful reporting, where Var(ˆacal) is the calibration-time variance. Power
≥0.95atT≥50for shrinkageϵ≥0.3.
Combined with platform-computed attribution, this yields a layered defense: institutional prevention
plus statistical detection.
C.4 Mussa–Rosen screening with private risk aversion
Suppose risk aversion αj is private information, drawn from a distribution G on [α,¯α]with density g
satisfying the monotone hazard rate (MHR) condition: φ(α) :=α+G(α)/g(α) is strictly increasing.
Proposition 8(Optimal contract menu under private types).Under MHR, the platform’s revenue-
maximizing IC menu offers
ρSB j (α) = min  1, Ij φ(α)  ,
implementable in dominant strategies without ironing. Per-type deadweight loss from screening
(whereρ SB <1) is
DWLj(α) = αVar(v j) 2  ρ∗ j −ρ SB j 2 = I 2 j Var(vj) (φ(α)−α) 2 2α φ(α)2 .
Proof. Single-crossing: ∂2U/∂ρ∂α=−ρVar(v j)<0 for ρ >0 . Envelope: (U ∗)′(α) =
−ρ(α)2 Var(vj)/2≤0 . Substituting and integrating by parts gives the pointwise problem
maxρ[ρIj Var(vj)−(φ(α)/2)ρ 2 Var(vj)], with FOC ρSB =I j/φ(α). MHR gives φ′ >0 , so
monotonicity holds without ironing. The cap min(1,·) enforces ρ≤1 , binding for φ(α)<I j. The
DWL formula follows by substitutingρ ∗ =I j/αandρ SB =I j/φ(α).
Separation of signal IC and menu IC.When the manipulation game is timed sequentially (report
type → receive contract → observe ˆa→choose manipulation), the creator’s utility Hessian over
(b, ϵ,ˆα)is block-diagonal between the post-contractual signal block (b, ϵ)and the pre-contractual
type block ˆα. The platform’s design problem therefore decouples: institutional/monitoring controls
handle the signal channel (Appendix C.1), and the Mussa–Rosen menu of Proposition 8 handles the
type channel. Under stochastic π with Cov(ˆajπ, π)̸= 0, off-diagonal coupling reappears and the
separation is at most approximate.
C.5 Dynamic self-policing and competition invariance
Suppose detected Tier 2 bias triggers a transition to inactive status, with continuation-value gap
V A −V I >0 (positive in both thin- and thick-margin regimes by the dynamic results in Appendix I).
Under constant detection Pr(detect|b >0) = Pr 0, equilibrium is bang-bang: b∈ {0, b∗ static}, with
truthfulness requiring the discount factor to satisfy
δ≥δ const j := (ρ∗ j ¯π)2 2(κ+α j(ρ∗ j )2σ2π) Pr0(V A −V I ) .
Under proportional detection Pr(detect|b) =ϕ db the unique interior bias is b∗ j,dyn =ρ ∗ j ¯π/[κ+
αj(ρ∗ j )2σ2 π +δϕ d(V A −V I )]>0 , strictly decreasing in δ, ϕd, and V A −V I. Exact truthfulness is
unattainable under proportional detection, but the bias is suppressed below the static optimum.
18

Proposition 9(Manipulation incentives are unchanged by competition).Under exclusive licensing
and Bertrand competition with K≥2 platforms, the three-tier IC hierarchy of Proposition 7 is
invariant to the number of competitorsKand to ¯Uj.
Proof. By Theorem 2 (multi-platform Bertrand equilibrium), ρ∗(k) j =I (k) j /αj is independent of K
and ¯Uj because the effective outside option ˆUj enters platform k’s objective additively through f (k) j
and cancels in the ρ-derivative. The Tier 1, Tier 2, and Tier 3 manipulation utilities depend only
on (ρ∗(k) j , αj,Var(ˆaj),E[π 2], κ, σ2 π,Cov(v, π)), none of which depend on K or ¯Uj under exclusive
licensing.
Under non-exclusive licensing the variance of combined per-period payment includes a cross-platform
term 2ρAρB Cov(vA j , vB j ), which depends on ρB and through it on the rival’s market structure; IC
conditions then becomeK-dependent.
C.6 Failure modes
Two boundary cases warrant comment.Risk-neutral limit:the cap ρj ≤1 binds at αj =I j; for
αj <I j, ρ∗ j = 1. At αj = 0 the Tier 1 variance penalty vanishes, and Tier 1 IC fails weakly when
c= 0 .Pairwise additive pooling:if creator i pools their attribution report with creator j’s, reporting
ˆai + ˆaj, creator i’s payoff variance changes by (ρ∗ i )2[Var(ˆaj) + 2 Cov(ˆai,ˆaj)], so additive pooling
is unprofitable iff Cov(ˆai,ˆaj)>−Var(ˆa j)/2. In music markets, where stylistic similarity drives
positive cross-catalog correlation in measured attribution, this condition is typically satisfied and
pooling is deterred.
D Welfare cost of uniform contracts
Proof of Proposition 3.We prove each claim in turn.
Claim 1 (Selective exit of high-outside-option creators).Under a uniform contract ( ¯f ,¯ρ), creator j
participates if and only ifU j( ¯f ,¯ρ)≥¯Uj. Expanding:
¯f+ ¯ρE[vj]− αj 2 ¯ρ2 Var(vj)≥ ¯Uj.
Rearranging, creator j exits if ¯Uj > ¯f+ ¯ρE[vj]− αj 2 ¯ρ2 Var(vj). The right-hand side is the utility the
uniform contract provides. Creators with high ¯Uj (strong standalone careers) are the first for whom
this inequality is violated. In the music setting, distinctive creators tend to have both high ¯Uj (their
original recordings command high streaming revenue and sync fees) and high complementary value
in u (their unique styles cannot be replicated by combining others). Hence S exit is disproportionately
composed of the most valuable creators.
Moreover, when ¯ρis set to the population-average optimal royalty, creators with high SNRj (who
should receive high ρ∗ j under Theorem 1) are offered a ¯ρthat istoo lowfor them—capturing less of
their high attributed value—while creators with low SNRj are offered a ¯ρthat istoo high—imposing
excessive attribution noise risk. The mismatch is worst at the extremes, and the creators most harmed
by the mismatch are the distinctive ones whose optimalρ ∗ j is far above¯ρ.
Claim 2 (Superlinear loss from joint exit).For any set A⊆ S , the loss from removing A
simultaneously is:
u(x, r)−u(x\A, r).
If u is superadditive across the creators in A (i.e., these creators are complements), then by definition:
u(x, r)−u(x\A, r)≥
X
j∈A
[u(x, r)−u(x\ {j}, r)]
when |A| ≥2 and the creators in A interact superadditively. The inequality is strict when com-
plementarities are strict. Since S exit is concentrated among distinctive creators (Claim 1), and
distinctive creators tend to be complements (a reggae producer and a classical composer together
enable cross-genre generation that neither supports alone), the loss is superlinear in|S exit|.
19

Claim 3 (Welfare gap decomposition).Under the optimal creator-specific contracts from Theorem 1,
all creators participate (by construction, ρ∗ j and f ∗ j are set so that Uj(θ∗ j ) = ¯Uj), and the platform’s
welfare is W ∗ = P j E[π a∗ j ]− P j ¯Uj − P j R∗ j , where R∗ j = αj 2 (ρ∗ j )2 Var(vj) is the minimized
risk premium.
Under the uniform contract, the platform’s welfare has two sources of loss:
1. For creators who remain (j /∈ Sexit), the risk premium is Runiform j = αj 2 ¯ρ2 Var(vj), which
is generically larger thanR ∗ j since¯ρ̸=ρ ∗ j . The excess isL uniform j =R uniform j −R ∗ j .
2. For creators who exit ( j∈ Sexit), the platform loses their entire contribution, which by
Claim 2 is superlinear.
Summing these two terms yields the uniform-contract welfare gap.
E Multi-platform Bertrand competition
This appendix gives the formal results behind the attribution-moat analysis (Section 3.3): the proof
of the multi-platform Bertrand equilibrium, equilibrium uniqueness, the moat result with both
homogeneous and heterogeneous demand, and the welfare comparisons. We use the notation of
Section 3.1 extended across K≥2 platforms: platform k has creator-specific informativeness
I (k) j ∈(0,1) and signal variance V (k) j := Var(v(k) j ), the multi-platform analogue of Var(vj) from
§3.1 withv (k) j = ˆa(k) j π.
E.1 Setting and surplus decomposition
We assume(C1)exclusive licensing (each creator licenses to at most one platform per period);(C2)
heterogeneous informativeness I (k) j across platforms;(C3)additive separability of platform k’s total
surplus across the creators it acquires; and, where indicated,(C4)centered Gaussian noise with
E[ˆa(k)] =E[a ∗] = 0.
By Theorem 1 applied to platformk, the per-creator surplus under royaltyρis
Σ(k) j (ρ) =µ (k) j +ρI (k) j V (k) j − αj 2 ρ2V (k) j ,
where µ(k) j is the base value from including creator j’s catalog. The maximizer is ρ∗(k) j =I (k) j /αj
with maximized surplus
Σ∗(k) j =µ (k) j + (I (k) j )2V (k) j 2αj .
Under (C4) and centered attribution, the V-cancellation identity V (k) j =σ 2 a∗ E[π2]/I (k) j gives the
simpler form
Σ∗(k) j −µ (k) j = I (k) j σ2 a∗ E[π2] 2αj ,
linear inI (k) j .
E.2 Bertrand equilibrium
Theorem 2(Multi-platform Bertrand equilibrium).Under (C1)–(C4), the simultaneous Bertrand–
Nash equilibrium for creator j across K≥2 platforms has the following structure.(i) Royalty.Each
platform offers ρ∗(k) j =I (k) j /αj, independent of K and rivals’ offers.(ii) Allocation.Creator j joins
k∗ j = arg maxk Σ∗(k) j if Σ ∗(k∗ j ) j ≥ ¯Uj, and otherwise exits.(iii) Rents.The winning platform earns
Πj = Σ
∗(k∗ j )
j − ˆUj, where ˆUj = max( ¯Uj,Σ ∗(2) j ) and Σ∗(2) j is the second-highest maximized surplus;
the creator earnsU ∗ j = ˆUj.
20

Proof of Theorem 2. Step 1 (royalty FOC).Under the binding IR constraint, f (k) j = ˆUj −ρ jE[v(k) j ] +
(αj/2)ρ2 j V (k) j , where ˆUj = max( ¯Uj,max l̸=k Σ∗(l) j ) is the effective outside option. Platform k’s
profit from creator j is Π(k) j (ρ) = Σ(k) j (ρ)− ˆUj. Since ˆUj enters as a subtracted constant, the FOC
∂Σ(k) j /∂ρ= 0 is independent of ˆUj, K, and rival platforms; hence ρ∗(k) j =I (k) j /αj in equilibrium.
The SOC is −αjV (k) j <0 , confirming a maximum. Competition affects only the level of rents
(throughf j), not the slope of incentives (throughρ j).
Step 2 (Bertrand rent).The creator joins k∗ j = arg maxk Σ∗(k) j if at all. To attract j, platform k∗ j
must offer Uj ≥ ˆUj = max( ¯Uj,Σ ∗(2) j ), where Σ∗(2) j is the second-highest surplus. Any Uj > ˆUj is
suboptimal; any Uj < ˆUj loses the creator. In the Bertrand limit, the winning platform sets Uj = ˆUj
and earnsΠ j = Σ∗(k∗) j − ˆUj.
Step 3 (allocation).Creator j joins k∗ j if Σ∗(k∗) j ≥ ¯Uj; otherwise no platform can profitably cover the
outside option, andjexits. Equilibrium creator payoff:U ∗ j = ˆUj = max( ¯Uj,Σ ∗(2) j ).
Proposition 10(Equilibrium uniqueness).The Bertrand equilibrium of Theorem 2 is unique in pure
strategies.
Proof. Exhaustive deviation analysis. (a) The winner cannot increase profit by changing ρ (concavity
of Σ(k) j in ρ). (b) The winner cannot increase profit by lowering Uj below ˆUj (loses the creator). (c)
A loser cannot profitably attract creator j by offering Uj >Σ ∗(l) j (negative profit). (d) A loser cannot
profitably attract creatorjby offeringU j < ˆUj (creator rejects).
E.3 Vertical differentiation rent and the moat
Corollary 2(Rent from being the attribution-precision leader).Under (C4) and homogeneous
demand (µ(k) j =µ j for allk),
Πj =
(I (k∗) j − I(2) j )σ2 a∗ E[π2]
2αj
.
Proof. The Bertrand profit is Πj = Σ∗(k∗) j −Σ ∗(2) j . Evaluating both maximized surpluses under V-
cancellation gives Σ∗(k) j =µ j +I (k) j σ2 a∗ E[π2]/(2αj), and subtraction yields the stated formula.
We now give the formal version of Proposition 2.
Proof of Proposition 2.(i) Dead zone.Under homogeneous demand and (C4),Σ ∗(k) j −µ j is linear
in I (k) j . Platform 2 becomes the winner only when I (2) +ϵ >I (1), i.e., ϵ >∆Ij. For ϵ≤∆I j,
Platform 2 remains the runner-up; its surplus improvement raises the creator’s effective outside option
but generates zero rent for itself.
(ii) Post-flip rent.Direct application of Corollary 2 with the updated informativenessI (2) +ϵ.
(iii) Social return.In the dead zone, W=U ∗ j +Πj = Σ(1) j , constant in ϵ: the creator’s outside-option
gain is exactly offset by the leader’s rent reduction. After the flip, W= Σ (2) j (ϵ) =µ+ (I (2) +
ϵ)σ2 a∗ E[π2]/(2αj), strictly increasing.
Remark 3(Heterogeneous demand).With heterogeneous demand µ(k), the flipping threshold be-
comes
ϵflip = ∆Ij + 2αj(µ(1) −µ (2)) σ2 a∗ E[π2] ,
extending the dead zone when the leader has a demand advantage and shrinking it when the trailer
does.
21

E.4 Welfare comparisons
Proposition 11(Welfare loss under competition).Under Theorem 2,
Lcomp = X
j
L
(k∗ j )
j ,L (k) j = V (k) j 2αj (1− I(k) j )2.
Under (C4) and homogeneous demand, the competitive allocation minimizes total welfare loss among
allocations satisfying (C1)–(C3).
Proof. Under Bertrand, each creator joins k∗ j = arg maxk Σ∗(k) j . Under homogeneous demand,
Σ∗(k) j −µ is increasing in I (k) j , while L(k) j =σ 2 a∗ E[π2](1− I(k) j )2/(2αjI (k) j ) is strictly decreasing
in I (k) j . Therefore competitive allocation assigns each creator to their max- I platform, which
simultaneously minimizes loss; total loss is the sum, by (C3).
Corollary 3(Diminishing returns to entry).Under exchangeable informativeness draws, E[∆WK]
is strictly decreasing in K. For I ∼Uniform[0,1], the marginal gain from adding the (K+1)-th
platform is proportional to1/((K+1)(K+2)).
Proof. Standard order-statistics calculation. E[I(K) ] =K/(K+ 1) , and E[∆WK]∝E[I (K+1) −
I(K) ] = 1/((K+ 1)(K+ 2)), strictly decreasing inK.
E.5 Royalty invariance under moral hazard
The royalty invariance of Theorem 2 extends to environments with endogenous quality choice
(Appendix B.3). Under Q1–Q4 and (C1)–(C3), both the static optimal royalty ρ∗(k) j =I (k) j /αj and
the equilibrium effort q∗ j (ρ∗(k) j ) =ρ ∗(k) j µj/Dj(ρ∗(k) j ) depend only on platform k’s own primitives
(I (k) j , αj, µj, γj), not on K or ¯Uj. The effort-channel welfare Wj(ρ) =µ 2 j ρ(2−ρ)/(2D j(ρ))
inherits the invariance, so the welfare-maximizing royalty ρ∗∗ j is also K-invariant. Contract structure
(royalty, effort, per-creator welfare) is competition-invariant if and only if the surplus function
decomposes asΠ (k) j (ρ) = Σ(k) j (ρ)− ˆUj with ˆUj not depending onρ.
E.6 Tension with non-additive utility
The additive-separability assumption (C3) is the tractable baseline; it conflicts with the non-additive
ut that drives the superlinear loss in the selective-exit analysis. For ut = P j sj +ϵ P j<l cjl,
the Bertrand equilibrium of Theorem 2 is the ϵ= 0 limit, with first-order corrections that may
move complementary creators onto the same platform. Quantifying these corrections in general
requires solving for equilibrium platform assignments simultaneously and is left to future work; the
perturbation argument ensures the headline moat result is robust to weak complementarities.
F Discussion of modeling choices
Mean-variance vs. expected utility.We adopt mean-variance preferences for tractability and because
they are standard in the contract theory literature when the principal designs linear payment schemes.
The qualitative results — that royalty optimality increases in SNR — hold under general risk-averse
expected utility (CARA, CRRA) with appropriate regularity conditions.
Independence of attribution noise.The assumption that ξj is independent across creators simpli-
fies the variance decomposition but can be relaxed. Correlated attribution errors (e.g., systematic
overattribution to popular creators) introduce additional distortions analyzed in ongoing work.
Static vs. dynamic model.Our model is static: creators make a one-shot licensing decision. In
practice, contracts are renegotiated, and creators observe realized payments before deciding whether
to continue. Extending to a dynamic model with learning about SNR and renegotiation is a natural
next step.
22

Endogenous attribution cost.We treat the attribution technology (and hence σ2 ξ,j) as a platform
choice but do not fully solve for the joint optimization over contracts and attribution investment. The
first-order condition for optimal investment equates the marginal cost of reducingσ2 ξ,j to the marginal
welfare gain |∂Lj/∂σ 2 ξ,j |, summed across all creators. This joint optimization is straightforward
given Proposition 1 but requires specifying the cost function C attr, which we leave to empirical
calibration.
G Additional empirical experiments and the attribution-investment portfolio
This appendix collects the additional empirical experiments and the formal water-filling rule that
allocates an attribution-improvement budget across creators. The marginal-gain formula from
Proposition 1 stays in the main text; the optimization that uses it appears here.
G.1 Detailed empirical setup
We expand on the main-text setup paragraph in Section 4.1.
Ground-truth attribution.For each creatorj, the loss-delta ground truth is
a∗ j =ℓ  yfull

 r;ϕ −j −ℓ  yfull

 r;ϕ full ,(14)
where ϕfull are the model weights of the full-catalog fine-tune, ϕ−j are the weights of the leave-
creator-j-out fine-tune, r is the prompt, and yfull is the generation produced by ϕfull at r. This follows
the counterfactual-loss formulation in the data-attribution literature [42, 48, 37], applied at the catalog
level rather than the example level. The loss-delta target is model-internal rather than perceptual,
which lets every measured bIj be validated against a quantity the model itself optimizes; perceptual
ground truth (e.g., listener-judged stylistic resemblance) is a complementary target left to future work.
Catalog selection.The N= 22 artist catalogs are drawn from MTG-Jamendo’s autotagging split,
with at least ten tracks per artist and at least 40% within-artist genre coherence. Catalogs span four
prolificness bands by track count — 8 low (10–15 tracks), 8 mid (16–25), 5 high (26–50), and 1
extra-high (>50 , capped at 50) — and ten primary genres (electronic, classical, hip-hop, pop, rap,
latin, alternative, heavy metal, pop-rock, experimental). The total training set is 475 tracks; each
leave-catalog-out fine-tune drops the corresponding catalog and retrains.
Model and fine-tuning.We fine-tune Stable Audio Open [ 24] on the curated training set with the
V AE frozen, training only the diffusion transformer. Each of theN+ 1 = 23 models (one full + 22
leave-catalog-out) is fine-tuned from the public checkpoint with matched hyperparameters; we use
the same prompted-continuation set ofT= 200evaluation prompts across all models.
Attribution-method implementation.For both EKFAC influence functions [ 30] and D-TRAK [62],
we compute per-sample attribution scores against each of the T generated outputs and aggregate to
the catalog level by summation. EKFAC uses block-diagonal Fisher approximation; D-TRAK uses
random projections of training and query gradients followed by a kernel-based score.
Quantity definitions.For each method m and creator j we report four quantities: bI (m) j is the
regression slope of a∗ on ˆa(m) across the T outputs; bK (m) j = dCov(ˆa(m), a∗)/dVar(a∗) is the
multiplicative-bias scale; [SNR
(m,cal)
j is the Gaussian-shortcut SNR computed from the calibrated
estimator ˜aj,t = ˆaj,t/ bK (m) j ; and bρ(m) j is the per-creator Pearson correlation between ˆa(m) and a∗
across the T outputs. Bootstrap 95% confidence intervals are computed by resampling the T outputs
with replacement,1,000replicates per quantity.
Sanity checks.The ground truth a∗ is positive in 97.6% of 4400 creator–output pairs (mean
0.0042, std 0.0059), confirming that leave-catalog-out retraining reliably worsens loss in the expected
direction. The four-quantity tuple satisfies the identity bIj = [SNR cal j /  bKj(1 + [SNR cal j )  up to
numerical precision on the exported data, validating the calibration relation in Appendix A.
Headline statistics.Table 1 consolidates the headline measurement numbers referenced throughout
Section 4.1.
23

Table 1: Headline measurement statistics on Stable Audio Open with N= 22 artist catalogs and
T= 200 generated outputs, under EKFAC and D-TRAK. Each correlation row reports the per-clip
cross-creator correlation averaged over clips, with 95% bootstrap CIs in brackets. The | bKj| row
reports the median across the22creators.
Quantity EKFAC influence D-TRAK
Mean cross-artist Spearman0.050 [0.021,0.080] 0.054 [0.022,0.087]
Mean cross-artist Pearson0.188 (p <10 −4) 0.177 (p <10 −12)
Pearson / Spearman ratio3.76×3.24×
Median| bKj|7 966 5.25
Creators with bKj <0(sign-flipped)6/22 3/22
Creators with [SNR
cal
j >0.1 11/22 3/22
Creators with [SNR
cal
j >1 0/22 1/22
Aggregate welfare lossL (m) atα= 2 1.67×10 −4 1.69×10 −4
Welfare gain over no-attribution10.6% 9.8%
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
creator index
0.75
0.50
0.25
0.00
0.25
0.50
0.75
Pearson with a *
Per-creator correlation with ground truth
EKFAC D-TRAK
0.25
 0.00 0.25 0.50 0.75
EKFAC per-creator Pearson
0.4
0.2
0.0
0.2
0.4
0.6
0.8
D-TRAK per-creator Pearson
rank correlation
= 0.51, p = 0.015
Cross-method agreement
Figure 4: Per-creator detail behind the main-text headline numbers.(a)Per-creator Pearson with
95% bootstrap confidence intervals. Most intervals span zero at T= 200 ; a small subset of creators
show significant positive correlation under both methods.(b)Cross-method agreement on per-creator
Pearson, with the diagonal in dashed grey and an OLS fit in red. The methods agree at rank correlation
ρ= 0.51 (p= 0.015 ) on which creators are detectable, even though their absolute scales differ by
three orders of magnitude.
G.2 Per-creator measurement diagnostics
Figure 4 reports per-creator measurements that aggregate to the headline statistics in the main text
Table 1. At T= 200 the per-creator bootstrap intervals are wide and span zero for most creators on
both methods. A small subset of creators show statistically significant positive Pearson under both
methods, and the per-creator Pearson values are correlated across methods at Spearman ρ= 0.51
(p= 0.015 ), so methods agree on roughly which creators are detectable even though their cardinal
scales differ by orders of magnitude.
Figure 5 reports two scaling diagnostics that motivate the framework’s marginal-welfare investment
rule. The variance of the loss-delta ground truth grows roughly linearly with catalog size on a log–log
scale, with Pearson r= 0.69 (p <0.001). This scaling is a necessary condition for attribution to
discriminate small from large catalogs, since per-creator informativeness is a regression slope on the
ground-truth distribution; without dispersion in a∗, the slope is undefined. The right panel overlays
the closed-form marginal welfare gain |∂L/∂SNR| from Proposition 1 (computed at the median
Var(a∗)) with per-creator measured points. Per-creator points scatter above and below the median
curve in proportion to each creator’s own Var(a∗). The shaded region marks the precision range that
holds most of the current pool, where the marginal welfare gain from improved attribution is largest
— the same region the water-filling rule below routes the bulk of an attribution-improvement budget
into.
24

2 × 101 3 × 101 4 × 101
catalog size (tracks)
10 5
10 4
variance of ground truth
r = 0.69 (log-log)
Ground-truth signal scales with catalog size
10 2
 10 1
 100
calibrated precision
10 6
10 5
10 4
10 3
10 2
10 1
100
101
marginal welfare gain
most current creators
sit in this region
Marginal welfare gain by precision
closed form (median creator)
EKFAC
D-TRAK
Figure 5: Scaling and marginal-welfare diagnostics.(a)Ground-truth signal variance versus catalog
size, log–log axes (Pearson r= 0.69 , p <0.001); larger catalogs perturb the model more when re-
moved and are therefore more informative.(b)Closed-form marginal welfare gain from Proposition 1
(grey curve, evaluated at the median Var(a∗)) overlaid with per-creator measured points. Most of
the current creator pool sits in the shaded steep-slope region, where attribution-investment yields the
highest welfare return.
G.3 Optimal attribution-investment portfolio
Suppose the platform has a budget B >0 to invest in improving attribution precision and faces a
per-creator improvement technology gj : [0, ¯βj]→R + that is strictly increasing, strictly concave,
C 1, with gj(0) = 0 and g′ j(0)<∞ . Investing βj units of budget in creator j raises their SNR from
Sj to Sj +g j(βj). Adopt additive-Gaussian noise (centered: E[ˆaj] = 0, or π deterministic). The
platform allocates the budget to maximize total welfare-loss reduction.
Corollary 4(Optimal attribution-investment portfolio).The welfare-maximizing allocation {β∗ j }
solving
max
β≥0,P j βj =B
NX
j=1

Lj(Sj)− Lj(Sj +g j(βj))

satisfies the following:
1.Existence and uniqueness.β ∗ is unique by strict concavity of the composed objective.
2.Priority index.DefineM j :=ϕ j ·g ′ j(0)where
ϕj = Λj(2Sj + 1) S2 j (1 +S j)2 ,Λ j = E[π2] Var(a∗ j ) 2αj
is the marginal welfare gain from an infinitesimal SNR improvement. Creator j receives
investment iffM j exceeds the shadow priceλ ∗ of the budget constraint.
3. Closed form under square-root technology.If gj(β) =γ j
√β, the first-order approximation
of the optimal allocation is
βapprox j = (ϕjγj)2 P
k(ϕkγk)2 ·B.
Budget shares follow a square law in marginal welfare gains.
4.Comparative statics.∂β j/∂Sj <0,∂β j/∂αj <0,∂β j/∂Var(a ∗ j )>0.
Proof. (i) L(S) is strictly convex for S >0: L′′ = Λ(6S2 + 6S+ 2)/[S 3(1 +S) 3]>0 . The gain
Gj(s) :=L(S j)− L(Sj +s) is therefore strictly concave in s. Composition of strictly increasing
concave Gj with strictly concave gj is strictly concave, so hj(βj) :=G j(gj(βj)) is strictly concave
on [0, ¯βj]. The sum P j hj(βj) is strictly concave on the compact convex constraint set; existence
and uniqueness follow from Weierstrass plus strict concavity.
25

(ii)KKT: h′ j(β∗ j ) =λ ∗ if β∗ j >0 , else h′ j(0)≤λ ∗. With h′ j(0) =G ′ j(0)g′ j(0) =ϕ j ·g ′ j(0) =M j,
strict concavity gives the if-and-only-if characterization.
(iii)Linearize Gj(s)≈ϕ js for small s. Then hj(βj)≈ϕ jγj
p
βj. The FOC ϕjγj/(2
p
βj) =λ
yields
p
βj =ϕ jγj/(2λ); squaring and enforcing the budget constraint gives the stated formula.
(iv)Direct differentiation ofβ j ∝ϕ 2 j.
Pilot calibration.At the pilot parameters used throughout the paper ( αj = 2, E[π2] = 1 , three
creators with I ∈ {0.617,0.755,0.209}), the budget shares are 19.3% (pop), 5.5% (reggae), and
75.1% (classical). The classical creator receives three quarters of the budget despite having the
smallest Var(a∗), because their low SNR places this creator on the steepest part of the welfare-loss
curve. This generalizes the main-text observation that the moderate-precision regime has the highest
marginal return: when Var(ˆa)and αj heterogeneity is taken into account, low-informativeness
creators with moderate noise dominate the priority ranking.
Approximation guarantee.The closed-form allocation captures at least fraction 1/(1 + ¯ϵ)of
the optimal welfare gain under the Prop-1-convention objective, where ¯ϵ= maxj gj(B)/[(S j +
gj(B))Sj]. At pilot with B= 0.00751 (1% of mean SNR), ¯ϵ= 0.069and the guarantee is ≥93.5% .
Augmented water-filling.The priority index extends to incorporate quality dividends (from Ap-
pendix B.3), retention dividends (from the dynamic results in Appendix I), and IC costs (from
Proposition 8): ˜ϕj =ϕ j + ∆q j + ∆r j −∆ IC j , with ˜βapprox j ∝( ˜ϕjγj)2. The augmented allocation
concentrates investment more heavily on low-informativeness creators in the pilot calibration.
G.4 Multi-platform Bertrand competition between attribution methods
We treat the two state-of-the-art attribution methods evaluated in Part I — EKFAC influence functions
and D-TRAK — as two competing platforms in the Bertrand equilibrium of Theorem 2. Each platform
offers each creator the platform-specific attribution-aligned benchmark contract from Theorem 1
computed using its own bI cal,(m) j . Under exclusive licensing, creator j joins the platform with the
higher maximized surplus Σ∗(m) j , and the trailing platform’s private return to attribution improvement
is zero up to the leader’s lead.
Surplus proxy.We use the leading-order surplus from Theorem 1 after the binding-IR substitution,
Σ∗(m) j ∝ bI cal,(m) j 2 · Var(a∗ j ) 2α ,
which captures the per-creator surplus magnitude up to a normalization absorbed into the dead-zone
width.
Per-creator equilibrium.Of the 22 creators, EKFAC wins 14 and D-TRAK wins 8 (Figure 6 (a)).
The two methods produce non-trivial divergence on roughly one-third of the population, where the
trailing platform’s private return is exactly zero — the dead zone of Proposition 2.
Dead-zone distribution.Dead-zone widths span four orders of magnitude across creators, from
∼10 −11 (near-tie) to ∼10 −5 (large gap), with median around 10−7 (Figure 6 (b)). Most creators
have nearly indifferent surplus across methods — a small minority drives the population-level
dead-zone width that under-investing platforms face.
Industry-pattern reference.Table 2 relates current music-industry payment models to the frame-
work’s contract space θj = (fj, ρj). Existing models occupy the boundary (pure fixed fee or pure
royalty); AI training licenses are a setting where the attribution-aligned benchmark can place creators
in the interior of the contract space, and the framework’s prescription on the measured creator pool
(Section 4.3) gives a concrete instantiation of where those creators would sit under the benchmark.
H Bargaining with large rights holders
When a creator is sufficiently irreplaceable (e.g., a major label controlling a unique catalog), the
platform cannot credibly offer take-it-or-leave-it terms. Instead, the two parties bargain bilaterally
over the contract θj = (fj, ρj). Let ¯Π0 denote the platform’s payoff if negotiation fails (it generates
26

0 1 2 3 4 5 6 7 8
EKFAC surplus 1e 6
0
2
4
6
8D-TRAK surplus
1e 6
DTRAK
wins
EKFAC
wins
Per-creator surplus by method
11
 10
 9
 8
 7
 6
 5
log10 |surplus gap|
0
2
4
6creators
Dead-zone width distribution (log scale)
median 10^-7.1
Figure 6: Bertrand competition between EKFAC and D-TRAK as two platforms.(a)Per-creator
surplus on each platform; points above the diagonal favour D-TRAK, below favour EKFAC.(b)Dis-
tribution of dead-zone widths (absolute surplus gap) on a logarithmic axis, spanning four orders of
magnitude with median around10 −7.
Table 2: Existing music industry payment models as special cases of the framework’s contract space
θj = (fj, ρj). Most current models occupy the boundary (pure fixed fee or pure royalty); AI training
licenses are a setting where the attribution-aligned benchmark can produce interior contracts.
Industry model Payment formθ= (f, ρ)Attribution signal SNR regime
Blanket license (ASCAP/BMI) Fixed fee(f,0)None N/A
Pro-rata streaming (Spotify) Royalty(0, ρ)Stream counts Low (coarse)
Sync license (film/TV) Fixed fee(f,0)Negotiated N/A
User-centric (SoundCloud) Royalty(0, ρ)Per-user streams Medium
AI training license (proposed) Hybrid(f, ρ)Attribution method Varies
without creator j) and ¯Uj the creator’s outside option. The incremental joint surplus from agreement
is
Sj =E[π·a ∗ j ]− ¯Π0 − ¯Uj.
If βj ∈(0,1) is the creator’s bargaining power, the Nash bargaining solution splits the surplus so that
creator j receives ¯Uj +β jSj. The royalty rate ρj is still chosen to minimize the risk premium (as in
Theorem 1), but the fixed fee fj adjusts to implement the bargaining split rather than extracting all
surplus above the outside option. The key interaction with attribution precision: when attribution is
noisy, both parties prefer to shift toward fixed fees (reducing the noisy component), but the creator’s
bargaining power determines how the risk-premium savings are divided. A high-βj creator captures
most of the efficiency gain from better attribution.
I Dynamic participation
The static framework of Section 3 assumes a one-shot licensing decision. In practice, creators observe
realized payments and decide whether to continue licensing. This appendix gives the formal dynamic
extension: a Bellman equation for the platform’s value from each active creator, the steady-state
participation rate, and a two-regime characterization of when the platform optimally pays a retention
rent.
I.1 Setup
(D1) Myopic exit rule.At the end of period t, creator j exits iff wj,t < ¯Uj. This captures liquidity-
constrained creators or behavioral anchoring on ¯Uj.
(D2) Re-entry.An exited creator returns the next period with probabilityλ j ∈(0,1).
(D3) Stationary contract.The platform commits to θj = (f ∗ j , ρ∗ j ) from Theorem 1 each period, plus
an optional retention rents j ≥0added tof j.
(D4) Discount factor.The platform discounts atδ∈(0,1).
27

(D5) Gaussian payments.w j,t |x j,t = 1∼ N(E[wj],(ρ ∗ j )2σ2 v,j ).
Define net surplus Nj :=E[a ∗ j,tπt]− ¯Uj >0 and net margin µnet j :=N j − Lj >0 (creator profitable
net of alignment loss). For brevity we writeσ 2 v,j := Var(vj,t)throughout this appendix.
I.2 Static exit probability and theα-cancellation
Theorem 3(Dynamic participation).Under (D1)–(D5) and Theorem 1’s payment rule:
(a) Static exit probability.With zero retention rent,
pstatic j = Φ(−dj), d j = Ijσv,j 2 .
The exit buffer dj is independent of risk aversion αj: ρ∗ j ∝1/α j exactly offsets the risk-aversion
scaling in the variance penalty.
(b) Bellman equation.The platform’s value from an active creator with retention rents≥0is
V A j (s) = Πj(s) 1−δ˜σj(s) ,
where Πj(s) =µ net j −s , σj(s) = 1−Φ(−d j −s/(ρ ∗ j σv,j )) is the retention probability, ˜σj(s) =
ωj + (1−ω j)σj(s) is the effective continuation probability, and ωj =δλ j/(1−δ(1−λ j)) is the
re-entry discount factor.
(c) Steady-state participation.In the ergodic steady state,
n∗ j = λj λj +p j(δ) .
Proof. (a)Under binding IR, E[wj] = ¯Uj +R ∗ j with R∗ j = (α j/2)(ρ∗ j )2σ2 v,j =I 2 j σ2 v,j /(2αj).
Payment standard deviation is ρ∗ j σv,j =I jσv,j /αj. Exit iff wj,t < ¯Uj, so pj = Φ(−R∗ j /(ρ∗ j σv,j )).
The ratio simplifies:d j =R ∗ j /(ρ∗ j σv,j ) =I jσv,j /2, manifestly independent ofα j.
(b)Bellman: V A(s) = Π(s)+δ[σ(s)V A(s)+(1−σ(s))V I ], V I =δ[λV A(s)+(1−λ)V I ]. Solving
the second for V I =ωV A and substituting into the first yields V A(s)[1−δ(σ+ (1−σ)ω)] = Π(s) ,
i.e.,V A(s) = Π(s)/[1−δ˜σ(s)].
(c)Flow balance of the two-state Markov chain: pjnj =λ j(1−n j), giving nj =λ j/(λj +p j).
I.3 Two-regime characterization
Proposition 12(Two-regime characterization).The platform optimally sets s∗ j >0 (thick-margin
regime) if and only if
µnet j > µcrit j := pstatic j +ω j σ′ j(0) .
Otherwises ∗ j = 0(thin-margin regime) and exit occurs at the static ratep static j .
Proof. Define Γ(s) =F(s)−G(s) with F=δ(1−ω)Πσ ′ and G= 1−δ˜σ . The first-order
condition for the Bellman is Γ(s∗) = 0 , and (F−G) ′ =δ(1−ω)Πσ ′′ <0 on the domain
by log-concavity of the normal CDF. Strictly decreasing Γ implies at most one zero. Evaluate
Γ(0) =δ(1−ω)µ netσ′(0)−(1−δ˜σ(0)) ; the FOC has an interior root iff Γ(0)>0 , which
rearranges toµ net > µcrit. Otherwise the corner solutions ∗ = 0is optimal.
Patient-limit behavior.In the thin-margin regime, pj(δ) =p static j for every δ: patience is irrelevant
when margins are thin, and the exit rate is fully determined by the static buffer. In the thick-margin
regime, s∗ j (δ) is strictly increasing in δ with a finite patient limit s∞ j = lim δ→1 s∗ j (δ) satisfying
Πj(s∞)σ′ j(s∞) =λ j(1−σ j(s∞)), and the patient-limit exit probabilityp∞ j = 1−σ j(s∞)< pstatic j .
The retention rent paid by a patient platform is bounded above by the net margin.
28

Comparative statics. ∂pstatic j /∂Ij =−(σ v,j /2)ϕ(dj)<0 (higher informativeness reduces exit)
and ∂pstatic j /∂σv,j =−(I j/2)ϕ(dj)<0 . The latter is initially counterintuitive—higher signal
variancereducesexit—and reflects the fact that the risk premium grows quadratically in σv while the
payment standard deviation grows only linearly, so the buffer-to-std-dev ratiodj scales withσ v.
Retention dividend.Improving Ij raises the steady-state participation rate and yields a marginal
welfare gain
∆ret j = λj(Nj − Lj)σv,j ϕ(dj) 2(λj +p j)2 .
This dividend feeds the augmented water-filling rule of Appendix G.3.
Music-specific stakes.In the music context, the dynamic margin matters because creator exit
destroys not just supply volume butstylistic diversity: the loss of a distinctive reggae producer or
classical composer cannot be compensated by adding more generic pop producers, and the steady-
state participation rate of the most distinctive long-tail catalogs is the operative variable for the
platform’s long-run generation quality. Combined with the static results in the selective-exit analysis,
the dynamic framework predicts that uniform compensation drives a persistent participation gap
concentrated on the most valuable cohort.
J Synthetic data value chains
The platform may use its generative model not only to serve end users but also to producesynthetic
music datafor downstream purposes: fine-tuning specialized models, licensing to third parties, or
reducing dependence on future human-created music licensing. This creates a multi-stage value
chain: the platform licenses original music → trains a model → generates synthetic data → extracts
downstream value.
In stage 1, the platform generates output y with attributed value vj for creator j. In stage 2, the
platform uses its model to produce synthetic data ˜D and extracts downstream value V syn( ˜D). The
total value attributable to creator j’s original data is not justvj but vj + ∆vsyn j , where ∆vsyn j captures
j’s marginal contribution to the synthetic data’s downstream value.
A payment rule based only on vj systematically underpays creators whose data is valuable for
synthetic generation. This has three implications for the framework:
• Amplified displacement.Synthetic data generated in a creator’s style continues competing in
the market without further licensing, compounding the displacement effectδ j over time.
• Compounding attribution noise.Measuring ∆vsyn j requires attributing value through a chain
(original data → model → synthetic data → downstream value), and the noise at each stage
compounds. The effective SNR for the full-chain attribution is lower than the single-stage
SNR, strengthening the case for fixed-fee components that do not depend on per-output
measurement.
•Payment rule implications.If the platform extracts significant synthetic-data value without
compensating original creators, pure per-output royalties understate total value extraction.
This strengthens the case for hybrid payments that include an upfront component reflecting
the data’s option value for future synthetic generation.
29
