---
title: When Does Static Willingness to Pay Mislead? A Framework for Dynamic Hedonic Valuation
url: https://arxiv.org/abs/2603.02456
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Josephine Auer
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.02456
pages: 45
chars: 112935
fetched_at: '2026-11-08T13:02:01+00:00'
kb_version: 1
---

# When Does Static Willingness to Pay Mislead? A Framework for Dynamic Hedonic Valuation

When Does Static Willingness to Pay Mislead?
A Framework for Dynamic Hedonic Valuation∗
Josephine Auer†
MIT
August 21, 2026
Abstract
Many policy counterfactuals depend on how consumers value product attributes such as sugar, caffeine,
alcohol, or emissions. Standard hedonic and differentiated-products models typically impose time-
separable preferences. But when attributes are habit forming, current consumption can shift future
marginalvaluations,sostaticwillingness-to-paymaybeinsufficientforpolicycounterfactuals. Idevelop
a nonparametric revealed-preference framework for dynamic hedonic valuation, deriving necessary and
sufficientconditionsforrationalisingobservedpricesandchoices. Usingcerealscannerdata,Ishowthat
the hedonic representation restricts prices, while habits improve behavioural coherence conditional on
that representation. The framework diagnoses when static willingness-to-pay is defensible for policy.
Keywords: Hedonicvaluation, habitformation, identification, revealedpreference, intertemporalchoice,
nonparametric analysis
JEL Classification: D11, D12, D90, C61, C14, L66
∗IamespeciallygratefultoNikhilAgarwal,IsaiahAndrews,MiguelBallester,AbhijitBanerjee,NanoBarahona,ColinCamerer,
IanCrawford,GlennEllison,DrewFudenberg,EricGao,MattPolisson,AugustusSmith,andChenZhenforhelpfulcommentsand
discussions.
†E-mail:joauer@mit.edu
1
arXiv:2603.02456v6  [econ.TH]  20 Aug 2026

1 Introduction
Taxes, regulations, and product standards often target characteristics rather than products themselves. Soda
taxes target sugar, nutrition policy targets sodium and other dietary attributes, tobacco and alcohol policy
target addictive substances, and environmental standards target emissions or energy efficiency. Applied
economists routinely value such characteristics using hedonic or differentiated-products demand models,
and the resulting willingness-to-pay (WTP) measures are then used to interpret welfare and policy counter-
factuals.1 The usual interpretation is static: a price or demand coefficient attached to a characteristic is read
as a contemporaneous marginal valuation.
This static interpretation is restrictive when the characteristic itself is habit forming. If consuming an
additional gram of sugar today lowers tomorrow’s marginal utility through fatigue, satiation, or health-
related costs, then the observed willingness to pay for that gram combines a current benefit with a negative
continuationvalue. Inthatcase,astaticresearcherunderstatescontemporaneousWTPbytreatingthewhole
price as a current marginal value. If current consumption instead raises future marginal utility through
reinforcement or craving, the static interpretation moves in the opposite direction. A static coefficient can
sometimes serve as a reduced-form summary of marginal value, but it is not generally a primitive taste
parameter and need not be sufficient for counterfactuals that change future preference states.
Thecentralquestionofthispaperiswhencharacteristic-basedvaluationiscoherent,andwhenitrequires
a dynamic rather than static interpretation. Existing models of habit formation are typically formulated
overgoods, not characteristics. A large literature studies intertemporal dependence in the consumption of
cigarettes,alcohol,food,anddigitalproductsbymodellingutilityasafunctionofpastandcurrentquantities
(Becker and Murphy, 1988; Becker et al., 1991; Gruber and Kőszegi, 2004; Demuynck and Verriest,
2013; Crawford, 2010; Allcott et al., 2022). A central lesson of this literature is that price responses are
inherently dynamic: past consumption and expected future conditions affect current demand, so temporary
and permanent price changes need not be equivalent. For characteristic-based valuation, this raises an
additional question. If policy targets an attribute rather than a product, the analyst must know whether
attribute-level WTP is itself a static object. Existing habit models do not answer this question because they
characterisedynamicdependenceinproductquantities;whenvaluationisconductedincharacteristicsspace,
the dynamic structure must also be specified in characteristics space.
1Hedonic and characteristic-based demand models are central in empirical industrial organisation and applied micro; see, e.g.,
Smith and Desvousges (1986), Heckman and Scheinkman (1987), Berry et al. (1995), Nevo (2001), Gibbons and Machin (2003),
Bajari and Kahn (2005), and Greenstone and Gallagher (2008). For examples valuing potentially habit-forming food attributes
under static hedonic preferences, see Dubois et al. (2020), Haeck et al. (2022), and Le Fur and Outreville (2022).
2

I provide a nonparametric revealed-preference (RP) framework for evaluating the static interpretation of
characteristic-basedvaluation. Theframeworkaskswhetherobservedpricesandchoicescanberationalised
by preferences over current characteristics and lagged consumption of a habit-forming subset of those
characteristics. The exercise is consumer by consumer, so valuations over characteristics, discounting, and
habit formation may differ freely across households. The payoff is a model-free test of when characteristic
WTPhasacoherentwelfareinterpretation,beforetheresearcherimposesaparametricdemandspecification.
The first contribution is a sharp Afriat-type characterisation of dynamic hedonic rationalisability. The
test asks whether there exist characteristic shadow prices and a discount factor such that two requirements
hold. First, observed goods prices must admit the shadow-price representation implied by the maintained
goods-to-characteristics technology. Second, observed choices must satisfy dynamic RP inequalities at
those shadow prices. This extends static characteristics-based rationalisability (e.g., Blow et al. (2008)) to
allowhabitsovercharacteristics,whilepreservingthenonparametriclogicofSamuelson(1948),Houthakker
(1950), Afriat (1967), and Browning (1989).
The second contribution is to show how dynamics alter the interpretation of characteristic prices. In a
statichedonicmodel,thepriceofagoodpurchasedinpositivequantityequalsthevalueofthecharacteristics
bundledinthatgood. Inthedynamicmodel,thesamepriceequalscontemporaneousmarginalvaluationplus
the discounted continuation value generated by habit-forming attributes. The observed characteristic price
can therefore be interpreted as purely contemporaneous marginal value only under an exclusion restriction:
currentconsumptionofthecharacteristicmusthavenofutureutilityeffect. Dynamicwedgesalsomatterfor
differentiated-products demand, where characteristic coefficients are often converted into WTP for policy-
relevant attributes (Berry et al., 1995; Nevo, 2001). Even if such a coefficient is correctly identified in a
static demand system, it does not by itself identify how current consumption shifts future preference states.
Section 2.2 makes this point concrete with a temporary attribute-tax example: static and dynamic models
can agree on the immediate price response but disagree about the post-tax consequences of the policy.
Methodologically, theRPexerciseplaysadifferentrolefromstochasticdemandestimation. Ratherthan
absorbing deviations into unobserved product characteristics or taste shocks, it characterises the observable
implications of the welfare interpretation itself. Latent characteristics can still be added to the model if
desired, but then the interpretation being tested is the enlarged one, not the claim that observed policy-
relevant attributes alone support static WTP. This diagnostic has substantive content: it makes static WTP
as a welfare object empirically refutable, and shows whether any failure points to the price representation,
the dynamic specification, or the measurement of the relevant state.
Thethirdcontributionoperationalisesthisdiagnosticbydecomposingempiricalfailureintotwodistinct
3

margins. A characteristics-based valuation exercise can fail because observed prices cannot be represented
through the maintained characteristics technology; this is a structural failure of the hedonic price system.
It can also fail because, conditional on such shadow prices existing, observed choices are not dynamically
rationalisable;thisisabehaviouralfailureofintertemporalchoice. Forappliedwork,thisdistinctionmatters
because a failed valuation exercise has different implications depending on whether the problem is the
characteristics technology itself or the static interpretation of behaviour at admissible shadow prices. For
example,ifsodapricesdonotadmitashadowpriceforsugarunderthemaintainedcharacteristicstechnology,
then a soda-tax calculation cannot be grounded in hedonic WTP for sugar. If such shadow prices exist, but
only the dynamic model rationalises behaviour, the admissible WTP object combines current utility from
sugar with the future utility effects of current sugar consumption.
Icomplementthebinarytestwithdiagnosticsthatmeasurehowsevereviolationsareoneachmargin. On
the structural margin, I compute the distance from observed prices to the hedonic price manifold implied by
the characteristics technology. On the behavioural margin, I adapt a Critical Cost Efficiency Index (CCEI)
(Afriat, 1973; Varian, 1990) to measure the smallest relaxation of the dynamic RP inequalities needed for
rationalisability. These diagnostics distinguish small departures from consistency from large ones and show
whether empirical discipline comes primarily from the price representation or from intertemporal choice.
Iapplytheframeworktohousehold-levelscannerdataoncold-cerealpurchases. Cerealisanaturalsetting
for the exercise because products bundle measurable nutritional and descriptive characteristics, purchases
are repeated over time, and certain attributes—such as sugar and sodium—are plausibly habit-forming and
relevant for nutrition policy. More generally, the same framework applies to any setting with repeated
purchases, observed expenditures, and measured product characteristics.
The application yields three findings. First, moving from goods to characteristics space sharply lowers
raw rationalisability rates because characteristic-based models impose real restrictions on the price system.
Second, the associated distance measures show that many of these structural violations are modest in dollar
terms, so binary rejection alone overstates their economic severity. Third, conditional on the hedonic
price representation being admissible, allowing for habits improves behavioural coherence relative to static
characteristics models: it raises raw rationalisability rates for some households and moves the distribution
of CCEI values closer to one more generally. These patterns show that the framework is not simply a more
flexible fit criterion: it diagnoses when static characteristic-based valuation is empirically defensible and
when a dynamic interpretation is additionally required.
The results clarify when prices and choices support characteristic-based valuation, when that valuation
requires a dynamic interpretation, and what this implies for policy counterfactuals built from static WTP.
4

If observed prices do not admit a characteristics-based representation, no static or dynamic hedonic inter-
pretation is coherent under the maintained technology. If the price representation is admissible but static
separability fails, then characteristic prices can no longer be read purely as contemporaneous WTP. In that
case, a static WTP coefficient is not generally a primitive taste parameter: it may mix contemporaneous
marginal value with omitted habit states and continuation values. The diagnostic asks whether the data
support treating static WTP as a defensible welfare object for the counterfactual at hand. The continuation
component is generally set identified rather than point identified, so the framework is best understood as a
diagnostic of admissibility and interpretation rather than as a full structural estimator of welfare primitives.
The remainder of the paper is organised as follows. Section 2 introduces the dynamic hedonic model,
derives the valuation wedge, and uses a temporary-tax example to show how static and dynamic counter-
factuals can diverge, making the static interpretation an empirical restriction. Section 3 situates the result
within the related RP literature by showing that static hedonic and dynamic goods-based models arise as
special cases. Section 4 applies the framework to household scanner data on cereal purchases.
Relatedwork.Thispaperfirstrelatestothehedonicvaluationanddifferentiated-productsdemandliteratures
following Rosen (1974) and Berry et al. (1995) (henceforth BLP).2 Empirical work in this tradition often
uses observed prices or demand coefficients to value product characteristics that enter welfare and policy
counterfactuals. My point of departure is the static interpretation of those values. When some attributes
are habit forming, observed prices or demand coefficients can confound current tastes with continuation
values,sotheeconomicinterpretationofWTPforcharacteristicsbecomesanempiricalquestionratherthan
a maintained one. This distinction is first-order when WTP estimates are used to evaluate taxes, subsidies,
or standards that target the characteristics themselves.
The interpretation problem studied here is distinct from the familiar price-endogeneity problem in
differentiated-products demand. In BLP-style models, instruments and supply-side restrictions are used
to separate demand from marginal costs, markups, and unobserved product quality. My exercise instead
conditionsonthepricesfacedbyahouseholdandaskswhetherthosepricesandchoicesadmitacharacteristic-
based welfare interpretation. The two issues are complementary: even if a demand system has recovered
a static WTP coefficient for sugar, sodium, or emissions, that coefficient does not reveal whether current
consumptionofthecharacteristicshiftsfuturemarginalutility. Inthatsense,thepaperaddsaninterpretation
diagnostic to structural hedonic and demand approaches such as Bajari and Benkard (2005): it asks when
recovered WTP objects can be read statically, and when counterfactuals require a dynamic state variable.
2Rosen’s (1974) hedonic method has been widely applied across housing, environmental economics, health, education, and
industrial organisation; see, for example, Smith and Desvousges (1986), Gibbons and Machin (2003), Bajari and Kahn (2005), and
Greenstone and Gallagher (2008).
5

The paper is also related to the rational addiction literature initiated by Becker and Murphy (1988).3
That literature shows why current consumption may affect future marginal utility, but it is formulated at the
level of goods. The distinction matters when persistence is more naturally attached to attributes such as
sugar, sodium, nicotine, or caffeine than to the composite products that bundle them (cf. Koob and Moal,
1997). Relative to empirical work on addiction over nutrient profiles (e.g. Richards and Patterson, 2006),
my approach replaces functional-form restrictions with a nonparametric RP characterisation and asks when
habits over characteristics are consistent with observed prices and choices.
Methodologically, the paper contributes to two nonparametric RP literatures that have developed sep-
arately: tests of preferences over characteristics (Blow et al., 2008) and RP analyses of intertemporal
dependence (Crawford, 2010), both rooted in the foundational work of Afriat (1967), Diewert (1973), and
Varian (1982). I build on these tools to answer a valuation question that neither literature addresses on its
own: when do observed prices and choices support a dynamic interpretation of WTP for characteristics?
Answering this question requires both a goods-to-characteristics price representation and intertemporal ra-
tionalisability at the implied shadow prices. Static hedonic RP tests and dynamic goods-based RP tests
thereforeariseaslimitingcases,buttheinteractionbetweenthetworestrictionsistheobjectofinterest. This
interaction yields a novel taxonomy of empirical failure and tractable diagnostics for its severity.
Finally, the framework is distinct from models of inventory behaviour and stockpiling in consumer
demand (Hendel and Nevo, 2006). Storage can generate persistence in purchases under time-separable
preferences, whereas habit formation in my setting operates through state dependence in the flow utility
function over characteristics. The empirical framework therefore treats persistence induced by habits as
conceptually different from persistence induced by intertemporal substitution, even though distinguishing
thetwoinpurchasedatarequiresamaintainedlinkbetweenpurchasesandtheunderlyingconsumptionstate.
Takentogether,thepapershowswhencharacteristic-basedvaluationisadmissible,andwhentheresulting
valuations require a dynamic rather than static interpretation. Moving to characteristics space imposes
demanding structural restrictions on the admissible price system; allowing for dynamics changes the set
of admissible behavioural patterns and the interpretation of shadow prices conditional on satisfying those
restrictions.
2 Model
I begin by formalising a dynamic hedonic environment in which goods map into characteristics and habits
attach to a subset of those characteristics. I observe a single consumer for𝑡=1,...,𝑇, with purchases
3Empirical applications have largely focused on goods such as alcohol, cigarettes, caffeine, and illicit drugs; see, for example,
Becker et al. (1994), Grossman et al. (1998), Gruber and Kőszegi (2004), and Demuynck and Verriest (2013).
6

x𝑡∈R 𝐾 + and present-value pricesρ𝑡∈R 𝐾 +. Observed goods prices are taken as given from the consumer’s
perspective, so the object of the analysis is not price determination but whether observed choices can be
rationalised. Goods map into𝐽measured characteristics via a time-invariant linear technologyz𝑡 =Ax 𝑡
followingGorman(1956),whereAisa𝐽×𝐾matrix(typically𝐽 <𝐾). 4 ItreatAasknownandstableover
time; it captures objectively defined product attributes, while valuation is encoded in preferences. Although
the model is written for one consumer, the empirical RP exercise is applied household by household,
so valuations over characteristics, discounting, and habit formation are all allowed to vary freely across
consumers.
I partition characteristics asz𝑡 =((z 𝑐 𝑡)′,(z 𝑎 𝑡)′)′, wherez𝑐 𝑡 ∈R 𝐽1 are non-habit-forming characteristics
andz𝑎 𝑡 ∈R 𝐽2 arehabit-formingcharacteristics,with𝐽 1+𝐽 2=𝐽. Theanalystdefinesthispartition. Crucially,
this formulation allows intertemporal dependence to operate at the level of attributes rather than goods, so
persistence in behaviour need not be attributed to non-habit-forming components bundled within a product.
Although preferences are defined over characteristics, choice and budget constraints remain in goods space.
To clarify the economic content of the model, it is useful to fix ideas with a simple example. Suppose
the consumer chooses between two cereal products, where each good bundles two measurable attributes: a
contemporaneous “taste” characteristic (e.g., nuttiness) and a habit-forming “sensory” characteristic (e.g.,
salt or sugar intensity). The key modelling choice is that habits attach to the latter attribute rather than to
the cereal good itself: consuming a high-intensity product today can change tomorrow’s marginal value of
intensity (due to sensory fatigue or craving), even if the consumer switches cereal product. In this example,
the model’s structural content is that observed goods prices must be representable as shadow values on
attributes givenz𝑡 =Ax 𝑡, while its behavioural content is that those shadow values must admit a concave,
dynamically consistent utility representation.
Preferences are represented by a felicity (i.e., flow utility) function𝑢:R𝐽+𝐽 2 →Rthat depends on
current characteristics and one lag of the habit-forming subset,𝑢(z𝑐 𝑡,z𝑎 𝑡,z𝑎 𝑡−1), as in the one-lag “short
memory habits” specification of Boyer (1978, 1983) and Becker et al. (1994). The multi-lag extension is
straightforward and deferred to Supplemental Appendix??. I assume quasi-linearity in an outside good𝑦𝑡
with unit price, as is standard in empirical IO and hedonic demand models for narrow product categories
(Berry et al., 1995; Nevo, 2001). I also maintain local non-satiation, concavity, and superdifferentiability
of𝑢; I impose no further sign or monotonicity restrictions on the habit-forming components. I refer to this
4I adopt a linear transformation from goods to characteristics space as it is the most widely used specification. Most results
extend to a non-linear setting wherez=F(x)is increasing and strictly concave; see Supplemental Appendix??for an analogue
oftheconsistencydefinition. Thekeydifferencetothelinearcasearisesinthemarginalproduct: whereas𝜕z/𝜕x=A ′ isconstant
in the linear model, the marginal product varies with demand under a non-linear transformation.
7

environment as thehabits-over-characteristicsmodel.
The consumer chooses{(x𝑡,𝑦𝑡)}𝑇 𝑡=1 to solve
max
{(x 𝑡,𝑦 𝑡)} 𝑇 𝑡=1
𝑇∑︁
𝑡=1
𝛽𝑡−1 𝑢(˜z𝑡)+𝑦 𝑡  s.t. 𝑇∑︁
𝑡=1
ρ′ 𝑡 x𝑡+
𝑇∑︁
𝑡=1
𝛽𝑡−1𝑦𝑡 =𝑊,˜z 𝑡 = ˜A˜x𝑡,(1)
where𝛽∈(0,1]isadiscountfactorand𝑊ispresent-valuelifetimewealth. Thesinglepresent-valuebudget
should be read as the standard quasilinear lifecycle formulation: the consumer can reallocate expenditure
across observed periods, while the outside good absorbs wealth effects. I use the augmented notation
˜z𝑡 := (z𝑐 𝑡)′,(z 𝑎 𝑡)′,(z 𝑎 𝑡−1)′′,˜x 𝑡 :=(x′ 𝑡,x′ 𝑡−1)′, ˜A:= '›
«
A0 𝐽×𝐾
0𝐽2×𝐾 A𝑎
“ﬁ
‹
,(2)
so˜z𝑡∈R 𝐽+𝐽 2,˜x𝑡∈R 2𝐾, and ˜Ais a(𝐽+𝐽 2)×2𝐾block matrix. Throughout, I treatx 0 (equivalently, the
initial habit stockz𝑎 0) as fixed and exogenous. Because the model has one lag and a finite horizon, there is
no continuation term beyond𝑇; equivalently, I setπ1 𝑇+1≡0by convention. The key question is whether
theobservables{(ρ 𝑡,x𝑡)}𝑇 𝑡=1 canberationalisedby(1),and,ifso,whattestablerestrictionsthisimposeson
prices and choices.
2.1 Consistency
I now ask whether the observed data can be rationalised by optimising behaviour under the habits-over-
characteristicsmodel. Thisnotionofconsistencyencompassesboththeexistenceofahedonicshadow-price
representation (a structural requirement) and the coherence of intertemporal behaviour conditional on that
representation. Here “structural” does not refer to price determination. Rather, it refers to whether the
maintained goods-to-characteristics technology can rationalise observed prices through a corresponding
system of characteristic shadow prices.
Definition2.1(Consistency).Thedata{(ρ 𝑡,x𝑡)}𝑇 𝑡=1 areconsistentwiththeone-laghabits-over-characteristics
model for givenAif there exist𝛽∈(0,1]and a locally non-satiated, concave, superdifferentiable felicity
function𝑢such that{x 𝑡}𝑇 𝑡=1 solves (1).
The following lemma unpacks Definition 2.1 into the first-order pricing restrictions implied by the
consumer’s problem. The main revealed-preference characterisation, which eliminates the unknown utility
function, is stated in Theorem 2.1.
8

Lemma 2.1(First-Order Pricing Conditions).The data{ρ 𝑡,x𝑡}𝑇 𝑡=1 are consistent with the one-lag
habits-over-characteristics model for a given technology matrixAif and only if there exist a locally
non-satiated, concave, superdifferentiable utility function𝑢(·)and a discount factor𝛽∈(0,1]such that
for all𝑡∈{1,...,𝑇},
ρ𝑡≥A′π0 𝑡+(A 𝑎)′π1 𝑡+1,(★)
with equality for all goods𝑘such that𝑥𝑘 𝑡 >0, where the discounted shadow prices are
π0 𝑡 =𝛽 𝑡−1
 𝜕z𝑐 𝑡𝑢(˜z𝑡) 𝜕z𝑎 𝑡𝑢(˜z𝑡)  ,(3)
π1 𝑡 =𝛽 𝑡−1𝜕z𝑎 𝑡−1𝑢(˜z𝑡),(4)
and˜z𝑡 = ˜A˜x𝑡, withπ1 𝑇+1≡0.
Proof:See Appendix A.□
2.2 Dynamic wedges in willingness to pay
Lemma 2.1 shows why habits can matter for characteristic-based valuation. The shadow priceπ0 𝑡 is the
discounted marginal valuation of contemporaneous characteristics, whileπ1 𝑡 captures the marginal utility
effect of past consumption of habit-forming characteristics. For any good purchased in positive quantity,
condition(★)implies that its price equals the sum of current characteristic values and the discounted
continuation value generated by habit-forming attributes.
This decomposition creates a wedge between static and dynamic WTP. In a static hedonic model, the
price of a good is interpreted as the value of the characteristics bundled in that good. With habits, the
same price also internalises the future utility effect of current consumption. For example, when current
consumption lowers future marginal utility (i.e.,𝜕z𝑎 𝑡𝑢(˜z𝑡+1)<0), goods prices satisfy
𝜌𝑘 𝑡 =a′ 𝑘π0 𝑡+a𝑎′ 𝑘 π1 𝑡+1 <a′ 𝑘π0 𝑡,
so ignoring intertemporal dependence understates contemporaneous WTP for goods with negatively rein-
forcing attributes. If current consumption instead raises future marginal utility through reinforcement or
craving, the inequality reverses. The observed characteristic price can therefore be interpreted as purely
9

contemporaneous marginal value only when the continuation component is zero.
The distinction matters for counterfactuals that change current consumption of habit-forming character-
istics. To see this, consider the one-characteristic case with unit characteristic content, so that𝑎𝑘 =𝑎 𝑎 𝑘 =1.
For an interior purchase, the pricing condition reduces to
𝜌𝑘 𝑡 =𝜋 0 𝑡+𝜋 1 𝑡+1,
where𝜋 0 𝑡 is the discounted contemporaneous marginal value of the characteristic and𝜋1 𝑡+1 is the discounted
marginal effect of today’s characteristic consumption on tomorrow’s utility. A static model observes the
sum𝜌 𝑘 𝑡 and treats it as a current marginal valuation. The dynamic shadow price may still be the consumer’s
relevantprivatelifetimemarginalvalueattheobservedstate. Whatthestaticrepresentationlacksisthestate
variable that carries current characteristic consumption forward: in the dynamic model, currentz𝑎 𝑡 enters
tomorrow’s utility.
Example: a temporary attribute tax.Suppose current sugar consumption raises future marginal utility
for sugar through reinforcement. A temporary sugar tax today reduces current sugar consumption and, by
lowering tomorrow’s habit stock, also shifts tomorrow’s demand for sugar after the tax has expired. The
intuition is simple: if consuming sugar today makes sugar more valuable tomorrow, then reducing sugar
today lowers tomorrow’s desire for sugar as well. A static model can capture the contemporaneous price
response,butitcannotdescribehowtheinducedchangeinz 𝑎 𝑡 changesfuturemarginalvaluations. Thesame
nominal tax imposed later need not have the same effect, because the consumer reaches the later date with a
different habit stock.
A two-period calculation makes the policy content transparent. Continue with the one-good, one-
characteristic case above, so that𝐴=𝐴 𝑎 =1and𝑧 𝑡 =𝑥 𝑡: buying one unit of the good delivers one unit
of the habit-forming characteristic. Assume wealth is high enough that the interior solution is feasible;
quasi-linearity then removes income effects from the choice of𝑧1 and𝑧 2. Finally, assume no initial habit
stock,𝛽=1, and concave felicity
𝑢(𝑧𝑡,𝑧𝑡−1)=3𝑧 𝑡− 1 2𝑧2 𝑡+ 1 2𝑧𝑡𝑧𝑡−1− 3 8𝑧2 𝑡−1.
Thecross-partial𝜕 2𝑢/𝜕𝑧𝑡𝜕𝑧𝑡−1 =1/2capturesreinforcement: ahigherlaggedhabitstockraisesthecurrent
marginal value of the characteristic. With no tax and prices𝜌1 =𝜌 2 =1, the interior first-order conditions
10

imply
𝑧2=2+ 1 2𝑧1, 7 4𝑧1=2+ 1 2𝑧2,
so𝑧 1 =2and𝑧 2 =3. Now impose a temporary tax𝜏=0.3only in period 1. The first-order conditions
become
𝑧2=2+ 1 2𝑧1, 7 4𝑧1=1.7+ 1 2𝑧2,
so𝑧 1 =1.8and𝑧 2 =2.9. Even if a time-separable static model matched the period-1 reduction from2to
1.8, it would predict no post-tax effect in period 2 once the tax expires, because period-2 utility contains
no state inherited from period 1. The dynamic model instead predicts an additional reduction from3to2.9
because the period-1 tax changes the habit stock entering period-2 utility.
The same calculation also illustrates the price wedge in (★). In period 1, the tax-inclusive price equals
contemporaneous marginal value plus the continuation value of current consumption:
𝜌1+𝜏=(3−𝑧 1)|   {z   }
𝜋0 1
+
 1
2𝑧2− 3 4𝑧1

|          {z          }
𝜋1 2
.
At the taxed allocation, this gives1.3=1.2+0.1. A static interpretation can recover the full net marginal
value1.3attheobservedstate. Whatitcannotrecoveristhestate-dependenceinthatvalue. Inthecalculation,
the continuation component is𝜋1 2 =0.1: it is the marginal value of changing the lagged characteristic that
enters period-2 utility. The same object explains the post-tax demand effect, since the period-2 first-order
condition gives𝑧2 =2+ 1 2𝑧1. When the period-1 tax lowers𝑧1, it lowers period-2 demand even though the
tax has expired.
Theexternal-costconsequencesofthepolicycanthereforechange. Supposesugarconsumptiongenerates
an external social costℎ𝑧𝑡 that is not internalised by the consumer. A static evaluation of the temporary
tax counts only the period-1 external-cost saving,ℎ(2−1.8)=0.2ℎ. The dynamic evaluation counts the
same contemporaneous saving plus the post-tax saving,ℎ(3−2.9)=0.1ℎ, for a total external-cost saving
of0.3ℎ. Thus even when the two models agree on the immediate effect of the tax, they disagree about its
totalexternal-damageconsequences. Moregenerally,anypolicycalculationthattradesthesebenefitsagainst
implementationcostsorotherwelfarecomponentscandeliveradifferentranking. StaticWTPmaytherefore
be adequate for valuing a marginal unit at the observed state, but it is not generally sufficient for evaluating
policies whose effects propagate through habit stocks. The framework below provides a diagnostic for
whetherthedatasupportastaticinterpretation,orinsteadpointtodynamicstateeffectsthatacounterfactual
11

should take seriously.
The same logic applies to differentiated-products demand models (Berry et al., 1995; Nevo, 2001).
These models are often used to evaluate taxes, subsidies, or product standards that move consumption
of characteristics such as sugar, sodium, emissions, or energy efficiency. If preferences are dynamically
dependent over those characteristics, a static coefficient may still recover net WTP at the observed state, but
it need not be sufficient for counterfactuals that move current consumption of habit-forming characteristics.
This restriction is distinct from the usual equilibrium price problem in BLP-style demand estimation, where
instruments and supply-side restrictions separate demand from marginal costs, markups, and unobserved
product quality. Even if standard instruments and supply-side restrictions successfully identify the relevant
staticdemandcoefficient,theydonotbythemselvesidentifyhowcurrentconsumptionshiftsfuturepreference
states.
Foranapplieddemandresearcher,thepracticalroleofthetestisasadiagnosticpre-testandinterpretation
check. Givenamaintainedcharacteristicstechnology,thefirststepistoaskwhetherobservedpricessupport
characteristicshadowvalues. Conditionalonthatrepresentation,thesecondstepistoaskwhetherbehaviour
at those shadow values is consistent with static separability, or whether allowing current characteristics to
affectfuturemarginalutilityimprovesrationalisability. Thedistance-baseddiagnosticsdevelopedbeloware
useful even when the model rejects: large violations warn against treating recovered characteristic WTP as
a static welfare primitive, while small violations support the static model as a useful approximation. The
framework is therefore complementary to structural demand estimation: it clarifies when the WTP objects
recovered by such models can be read statically, and when they require a dynamic interpretation.
In sum, the model’s empirical content is governed by two restrictions: astructuralrequirement
that observed goods prices admit characteristic shadow prices consistent with the maintained goods-to-
characteristics technology, and abehaviouralrequirement that these shadow prices be consistent with
concave, dynamically stable preferences.
2.3 Afriat conditions for habits-over-characteristics
I now state the central theoretical result of the paper. It shows that the model has two distinct sources of
empirical content: a structural requirement that observed goods prices admit characteristic shadow prices
givenA, and a behavioural requirement that these shadow prices be consistent with concave, dynamically
stable preferences.
12

Theorem 2.1.The following statements are equivalent:
(A) The data{ρ𝑡;x𝑡}𝑡∈{1,...,𝑇} are consistent with the one-lag habits model for given technologyA.
(B) There exist𝑇 𝐽-vector discounted shadow prices

π0 𝑡 	 𝑡∈{1,...,𝑇} ,𝑇 𝐽2-vector discounted shadow
prices

π1 𝑡 	 𝑡∈{1,...,𝑇} and a discount factor𝛽∈(0,1]such that,
0≤
𝑀∑︁
𝑚=1
˜π′ 𝑡𝑚 ˜z𝑡𝑚+1−˜z𝑡𝑚  ∀𝑀≥2,∀(𝑡 1,...,𝑡 𝑀)∈{1,...,𝑇} 𝑀, 𝑡𝑀+1 =𝑡 1 (B1)
𝜌𝑘 𝑡 ≥a′ 𝑘π0 𝑡+a𝑎′ 𝑘 π1 𝑡+1 ∀𝑘,𝑡∈{1,...,𝑇}(B2)
𝜌𝑘 𝑡 =a′ 𝑘π0 𝑡+a𝑎′ 𝑘 π1 𝑡+1 if𝑥 𝑘 𝑡 >0,∀𝑘,𝑡∈{1,...,𝑇}(B3)
wherea𝑘 isthe𝐽-vectorcorrespondingtothe𝑘-thcolumnofA,a 𝑎 𝑘 isthe𝐽 2-vectorcorresponding
to the last𝐽2 rows of the𝑘-th column ofA, and˜π𝑡 := 1 𝛽𝑡−1  π0′ 𝑡 ,π 1′ 𝑡 ′ , withπ1 𝑇+1≡0.
Proof:See Appendix A.□
Theorem 2.1 says exactly when the observed purchases can be interpreted as optimal choices over
characteristics with one-period habits. Formally, the data are rationalisable if and only if there exist shadow
prices and a discount factor satisfying conditions (B1)–(B3). When such objects exist, one can construct a
concave, locally non-satiated utility function over characteristics that rationalises observed choices; when
theydonot,nosuchrepresentationispossible. Giventheboundaryconventionstatedabove,thefinal-period
pricingrestrictionissimply(B2)–(B3)withπ 1 𝑇+1 =0. Thetheoremthereforedeliversasharp,nonparametric
test of dynamic consistency in characteristics space.
It is useful to interpret the economic content of the three conditions. Condition (B1) imposes cyclical
monotonicityontheshadowprices. Economically, itrulesout“cycles”inrevealedmarginalvaluationsover
augmented characteristic bundles: there should be no sequence of observed trades in characteristics space
thatwouldallowacostlessimprovementbyreturningtothestartingpoint. Formally,cyclicalmonotonicityis
equivalent to concavity of the instantaneous utility function (Rockafellar, 1970). This condition is precisely
the behavioural discipline of the model.
Conditions(B2)and(B3)imposethestructuralpricingrestrictionsimpliedbythehabits-over-characteristics
model. They require that observed goods prices be representable as linear combinations of contemporane-
ous and forward-looking shadow prices. Economically, current goods prices must internalise both current
marginal utility from characteristics and the continuation value induced by habit formation. In the running
13

cereal example, the price of a high salt or sugar cereal must reflect not only current taste for nuttiness and
sensoryintensity,butalsohowtoday’ssensoryintensityalterstomorrow’smarginalutility. Theseequalities
therefore encode the intertemporal wedge introduced by past consumption directly into the price system.
Finally,notethatthemechanismtestedherediffersconceptuallyfrominventory-drivenpersistence(Hen-
delandNevo,2006): stockpilinggeneratesserialcorrelationinpurchasesthroughintertemporalsubstitution
and storage under time-separable preferences. Contrastingly, persistence in my framework operates through
state dependence in utility over characteristics, so current consumption of habit-forming attributes carries a
continuation value by shifting future marginal valuations. In purchase data, however, the two mechanisms
need not be empirically separable without additional structure linking purchases to consumption.
In practice, the test is implemented as a sequence of linear feasibility problems. For a fixed value of
𝛽, the researcher constructs the augmented characteristic bundles˜z𝑡, searches for shadow prices satisfying
the pricing restrictions (B2)–(B3), and checks whether those shadow prices satisfy the Afriat inequalities.
Gridding over𝛽then gives the reported rationalisability result. The apparently large family of cycle
restrictions in (B1) can be replaced by pairwise Afriat inequalities, so the implementable problem contains
only a quadratic number of behavioural constraints; Supplemental Appendix??gives the explicit linear
programme.
Interpreting the Afriat test requires care. A positive result establishes existence: there existssome
concave utility function and discount factor consistent with the data. The representation, however, is not
unique. Distinct utility functions—beyond simple monotone transformations—may rationalise the same
dataset. Moreover, rationalisability depends on the level of temporal and product aggregation; for example,
time aggregation may smooth consumption in a way that mimics habit persistence.
A negative result is likewise not diagnostic of the precise source of failure. Rejection may reflect habit
persistenceextendingbeyondonelag, non-concavitiesinpreferences, misspecificationofthecharacteristics
technology,oranincorrectpartitionofAintocontemporaneousandhabit-formingcomponents(forinstance,
treating “taste” preferences like nuttiness as static when the data in fact suggest that exposure today shifts
future marginal valuations). The Afriat test should therefore be interpreted as a sharp but reduced-form
diagnostic of dynamic rationalisability, rather than as a structural identification device.
2.4 A necessary price-span screen
Beforerunningthefullfeasibilitytest,onecanapplyalow-dimensionaldiagnosticthataskswhetherobserved
pricescaninprinciplebewrittenascharacteristicshadowvalues. Thissubsectionderivesthecorresponding
necessary condition. It can be evaluated period by period: failure immediately falsifies the model, while
14

satisfaction means only that the data pass this preliminary price screen.
The restriction isstructuralin the sense that it concerns only whether the maintained goods-to-
characteristics technology can in principle supportanyshadow-price representation of observed prices.
If the condition fails, no candidate preferences—static or dynamic—can rationalise the data because the
implied shadow-price system does not exist.
Letρ + 𝑡 denote the𝐾 + 𝑡 ≤𝐾-dimensional vector of discounted prices of goods consumed in strictly
positive quantities in period𝑡. LetB𝑡 denote the𝐽×𝐾 + 𝑡 submatrix ofAcollecting the contemporaneous
characteristics of those goods, and letB𝑎 𝑡 denote the𝐽 2×𝐾 + 𝑡 submatrix collecting the corresponding
habit-forming characteristics. For interior dates, Theorem 2.1 implies that
ρ+ 𝑡 =B′ 𝑡 π0 𝑡+(B 𝑎 𝑡)′π1 𝑡+1 = h B′ 𝑡

(B𝑎 𝑡)′ i  π0 𝑡 π1 𝑡+1  =: ˜B𝑡  π0 𝑡 π1 𝑡+1  ,(5)
where ˜B𝑡 is the𝐾+ 𝑡 ×(𝐽+𝐽 2)augmented technology matrix. BecauseB 𝑎 𝑡 is formed by rows ofB𝑡, the
augmented matrix ˜B𝑡 has the same column space asB′ 𝑡, so habit formation tilts shadow prices within the
same𝐽-dimensional price manifold rather than expanding it. At a genuine terminal date, the same pricing
equation holds withπ1 𝑇+1 =0; the interior-date formulation is the one directly relevant for the empirical
implementation, which does not treat the final observed purchase period as terminal.
Consistency therefore requires the observed price vectorρ+ 𝑡 to lie in the column space of˜B𝑡, yielding
the following necessary condition.
Proposition2.1.Ifthedata{ρ 𝑡,x𝑡}𝑇 𝑡=1 areconsistentwiththeone-laghabits-over-characteristicsmodel
for technologyA, then for every𝑡≤𝑇−1,
rank( ˜B𝑡|ρ+ 𝑡)=rank( ˜B𝑡)≤min{𝐾 + 𝑡, 𝐽},(NC)
where|denotes horizontal concatenation.
Violationof (NC)atanysingledateissufficienttorejectthemodel, providingasharp, low-dimensional
falsification criterion that can be evaluated period by period. The restriction coincides with the necessary
spanningconditionunderintertemporalseparabilityinBlowetal.(2008): habitformationchangesthelevel
ofshadowpricesbutdoesnotexpandthepricemanifoldimpliedbythemappingfromgoodstocharacteristics.
As such, (NC) is a structural constraint driven by the geometry ofArather than by the curvature or stability
15

ofpreferences. Because(NC)isonlynecessary,however,itdoesnotguaranteeconsistency: evenwhen(NC)
holds, the inequalities for goods consumed at zero quantities may still be infeasible. Nevertheless, (NC)
substantially reduces the feasible set and provides a fast diagnostic for empirical implementation.
Beyond its falsification role, the rank restriction also has limited identification content. For any𝑡, (5)
requires the observed price vectorρ+ 𝑡 to lie in the column space of˜B𝑡. BecauseB 𝑎 𝑡 is formed by rows
ofB 𝑡, the augmented matrix˜B𝑡 has the same column space asB′ 𝑡, so the feasible set of price vectors is
at most𝐽-dimensional. When habit formation is present (𝐽2 >0), the mapping from(π 0 𝑡,π 1 𝑡+1)toρ + 𝑡 is
therefore not one-to-one: reallocating shadow value between contemporaneous and lag components along
the habit-forming directions can leaveρ+ 𝑡 unchanged. Viewed through (5) alone, the decomposition into
contemporaneous and habit components is thus generically set-identified. In the running cereal example,
prices may identify the overall shadow value of “nuttiness” and “sensory intensity,” but not separately how
much of the value of sensory intensity reflects current taste versus its continuation value through habits.
The full characterisation in Theorem 2.1 can nevertheless sharpen this conclusion. Condition (B1)
links the stacked discounted shadow prices˜π𝑡 across dates through cyclical monotonicity evaluated at the
observed augmented bundles˜z𝑡, and therefore uses quantity variation as well as prices. These additional
restrictions can shrink the admissible set of decompositions relative to the price-span argument embodied
in (NC). For example, the data may satisfy Theorem 2.1 under the dynamic model while violating the static
restrictionπ 1 𝑡 ≡0, in which case the zero-habit specification is excluded from the identified set. Absent
furtherstructure,however,Theorem2.1stillneednotpoint-identify,orsign,thehabitcomponentseparately
from the contemporaneous one: (B1) disciplines the joint evolution of the stacked vectors˜π𝑡, but does not
in general undo the non-uniqueness in the decomposition induced by (5).
2.5 Missing prices
I now relax the assumption that prices are observed for all market goods. In many applications, prices are
recorded only for goods that are actually purchased, giving rise to a missing price problem.5 Missing prices
complicate RP analysis because imputing unobserved prices requires auxiliary assumptions. An alternative
is to treat missing prices as unknowns and ask whether there exist values that render the data rationalisable.
Thisexistenceapproachshouldbeunderstoodasapartial-identificationdevice: withoutfurtherrestrictions,
one can always rationalise non-purchases by assigning prohibitively high unobserved prices, so the goal is
to characterise when the observed prices alone already force a violation (or allow rationalisation) under the
5Throughout, I assume that the technology matrixAis known and time-invariant. This reflects settings where characteristics
can be directly observed or constructed (e.g., nutritional content, design features, emissions ratings), even when market prices are
only recorded for purchased items; in practice, missing prices are far more common than missing characteristics.
16

maintained technology. I now formalise this approach.
Letρ + 𝑡 denote the𝐾+ 𝑡 ≤𝐾sub-vector of period-𝑡discounted prices for goods with strictly positive
demand, and letB𝑡 andB 𝑎 𝑡 denote the corresponding𝐽×𝐾 + 𝑡 and𝐽 2×𝐾+ 𝑡 sub-matrices ofAandA 𝑎. Let
ρ0 𝑡,B 0 𝑡, andB𝑎,0 𝑡 denote the complementary sub-vectors and sub-matrices associated with zero demand.
The full discounted price vector isρ𝑡 =(ρ + 𝑡,ρ 0 𝑡). I can then state an Afriat-type characterisation for the
habits-over-characteristics model with missing prices.
Theorem 2.2.The following statements are equivalent:
(A+) Thereexistmissingprices{ρ 0 𝑡}𝑇 𝑡=1 suchthatthecompletedprice-quantitydataareconsistentwith
the model for technologyA.
(B+) There exist shadow discounted prices{π0 𝑡}𝑇 𝑡=1,{π 1 𝑡}𝑇 𝑡=1 and a discount factor𝛽∈(0,1]such that,
0≤
𝑀∑︁
𝑚=1
˜π′ 𝑡𝑚 ˜z𝑡𝑚+1−˜z𝑡𝑚  ∀𝑀≥2,∀(𝑡 1,...,𝑡 𝑀)∈{1,...,𝑇} 𝑀, 𝑡𝑀+1 =𝑡 1 (B1+)
ρ+ 𝑡 =B′ 𝑡 π0 𝑡+(B 𝑎 𝑡)′π1 𝑡+1 ∀𝑡∈{1,...,𝑇}(B2 +)
where˜π𝑡 := 1 𝛽𝑡−1  π0′ 𝑡 ,π 1′ 𝑡 ′ , withπ1 𝑇+1≡0.
Proof:See Appendix A.□
RelativetoTheorem2.1,themissing-pricetestconditionsonlyonpurchased-goodpricesandistherefore
weaker. In empirical settings where the initial stock is unobserved and the observed sample window is not
treated as the consumer’s terminal horizon, the implementable counterpart is the observable interior-date
analogueofTheorem2.2,whichevaluatestherestrictionsondatesforwhichboththelaggedbundleandthe
one-step-ahead continuation term are observed.
3 Corollaries and nesting results
Before turning to the empirical application, I record two immediate corollaries that situate the habits-over-
characteristics model within the RP literature. First, when characteristics coincide with market goods, the
framework collapses to the habits-over-goods model of Crawford (2010). Second, under intertemporal
separabilityandexponentialdiscounting,itreducestothecharacteristics-basedmodelofBlowetal.(2008).
Both results follow directly from Theorem 2.1 once the model is specialised to the relevant limiting cases.
Formal definitions and derivations for these special cases are provided in Appendix A.
17

3.1 Habits-over-goods as a special case
When characteristics coincide with market goods—that is, when𝐽=𝐾and the technology matrix satisfies
A=I 𝐽—the habits-over-characteristics framework reduces to a standard habits-over-goods model. In
this case, the distinction between goods and characteristics disappears, and the intertemporal first-order
conditions involve current and lagged consumption of habit-forming goods directly. To match Crawford
(2010), I maintain the additional assumption that all goods are consumed in strictly positive quantities.
Throughout this subsection, I adopt the terminal conventionρ𝑎,1 𝑇+1 ≡0, so the final-period habit-good
restriction has no continuation term. I also normalise the marginal utility of lifetime wealth to one,𝜆=1,
without loss of generality.
Definition3.1.Thedata

ρ𝑐 𝑡,ρ𝑎 𝑡 ;x𝑐 𝑡,x𝑎 𝑡 	𝑇 𝑡=1 areconsistentwiththeone-laghabits-over-goodsmodelif
there exists a locally non-satiated, superdifferentiable, and concave utility function𝑢(·)and a positive
constant𝛽such that for all𝑡∈{1,...,𝑇}:
ρ𝑐 𝑡 =𝛽 𝑡−1𝜕x𝑐 𝑡𝑢(¯x𝑡),(6)
ρ𝑎 𝑡 =𝛽 𝑡−1𝜕x𝑎 𝑡𝑢(¯x𝑡)+𝛽 𝑡𝜕x𝑎 𝑡𝑢(¯x𝑡+1),(7)
whereρ𝑐 𝑡 andρ𝑎 𝑡 denotepresent-valuepricesofnon-habit-formingandhabit-forminggoods,respectively.
Given this definition, I obtain the following result, equivalent to that in Crawford (2010).6
Corollary 3.1.The following statements are equivalent:
(A’) The data

ρ𝑐 𝑡,ρ𝑎 𝑡 ;x𝑐 𝑡,x𝑎 𝑡 	𝑇 𝑡=1 are consistent with the one-lag habits-over-goods model.
(B’) There exist𝑇shadow price vectors
n
ρ𝑎,0 𝑡
o𝑇
𝑡=1
,𝑇shadow price vectors
n
ρ𝑎,1 𝑡
o𝑇
𝑡=1
, and a positive
constant𝛽such that:
0≤
𝑀∑︁
𝑚=1
˜ρ′ 𝑡𝑚(¯x𝑡𝑚+1−¯x𝑡𝑚) ∀𝑀≥2,∀(𝑡 1,...,𝑡 𝑀)∈{1,...,𝑇} 𝑀, 𝑡𝑀+1 =𝑡 1,(B1’)
𝜌𝑎,𝑘 𝑡 =e 𝑘ρ𝑎,0 𝑡 +e𝑘ρ𝑎,1 𝑡+1 if𝑥 𝑘 𝑡 >0,∀𝑘,𝑡∈{1,...,𝑇},(B3’)
where¯x𝑡 :=(x 𝑐′ 𝑡 ,x𝑎′ 𝑡 ,x𝑎′ 𝑡−1)′,e𝑘isthe𝑘-thstandardbasisvector,and˜ρ 𝑡 := 1 𝛽𝑡−1
h
ρ𝑐′ 𝑡 ,ρ𝑎,0′ 𝑡 ,ρ𝑎,1′ 𝑡
i′
.
Proof:See Appendix A.□
6Equivalence uses the normalisation of the marginal utility of lifetime wealth𝜆=1, which can be imposed without loss of
generality.
18

3.2 Intertemporally separable preferences over characteristics
If habit formation is absent so thatz𝑡 =z 𝑐 𝑡 for all𝑡, the model reduces to a characteristics-based frame-
work with intertemporally separable preferences. Unlike Blow et al. (2008), who remain agnostic about
intertemporalallocation, myformulationembedsthisstaticcharacteristicsmodelwithinalifecycleproblem
with exponential discounting.7 The presence of a single intertemporal budget constraint implies a single
shadow value of lifetime wealth, so observed choices must satisfy both intratemporal utility maximisation
over characteristics and intertemporal optimality. Consistency with this lifecycle formulation is defined as
follows. As in the rest of the paper, I normalise the marginal utility of lifetime wealth to one.
Definition 3.2.The data {ρ𝑡;x𝑡}𝑇 𝑡=1 areconsistentwith intertemporally separable preferences over
characteristics and a life-cycle model for given technologyAif there exists a locally non-satiated,
superdifferentiable, and concave utility function𝑢(·)such that, for all𝑡∈{1,...,𝑇},
ρ𝑡≥A′π𝑡,(8)
with equality for all𝑘such that𝑥𝑘 𝑡 >0, wherez 𝑡 =Ax 𝑡,ρ𝑡 denotes the vector of present-value prices,
andπ𝑡 :=𝜕 z𝑡𝑢(z𝑡).
ThisrecoversthehedonicpricingequationofGorman(1956)andthefirst-orderconditionofBlowetal.
(2008) when the static characteristics model is embedded in a lifecycle framework. From this, I obtain the
following characterisation.
Corollary 3.2.The following are equivalent:
(A”) The data{ρ𝑡;x𝑡}𝑇 𝑡=1 are consistent with intertemporally separable preferences over characteristics and a
life-cycle model.
(B”) There exist𝑇shadow price vectors{π𝑡}𝑇 𝑡=1 such that:
0≤
𝑀∑︁
𝑚=1
π′ 𝑡𝑚(z𝑡𝑚+1−z𝑡𝑚) ∀𝑀≥2,∀(𝑡 1,...,𝑡 𝑀)∈{1,...,𝑇} 𝑀, 𝑡𝑀+1 =𝑡 1,(B1”)
𝜌𝑘 𝑡 ≥a′ 𝑘π𝑡 ∀𝑘,𝑡∈{1,...,𝑇},(B2”)
𝜌𝑘 𝑡 =a′ 𝑘π𝑡 if𝑥 𝑘 𝑡 >0,∀𝑘,𝑡∈{1,...,𝑇},(B3”)
wherea 𝑘 is the𝑘th column ofA.
Proof:See Appendix A.□
7By a lifecycle problem I mean that the consumer chooses the entire consumption path to maximise lifetime utility subject to a
single present-value budget constraint under exponential discounting.
19

Together, these corollaries clarify the paper’s value added. The framework unifies existing RP results
in goods space and in characteristics space within a single dynamic hedonic model, and it shows how the
interpretation of prices changes once habit formation over attributes is allowed. Relative to intertemporal
separability, the dynamic model introduces continuation values into the shadow-price system and delivers
diagnostics—viafeasibilityof (B1)–(B3)andtherankcondition(NC)—thatseparatefailuresofthehedonic
price representation from failures of dynamically coherent preferences.
4 Testing dynamic valuation in cereal purchases
Thissectionappliestheframeworktohousehold-levelcerealpurchasesasadiagnosticofwhencharacteristic-
basedvaluationisadmissibleinscannerdata,andwhenitrequiresadynamicratherthanstaticinterpretation.
Using these data, I show that most differences in raw rationalisability across models are driven by the
structuralrestrictions imposed by the hedonic representation of observed prices. Conditional on those
restrictions, allowing for habits improves behavioural coherence, though the gains are more visible in the
severityofviolationsthaninbinarypassrates. Thegoaloftheapplicationisnottoestimateacereal-demand
model,buttoillustratetheframeworkinarealisticscannersettingwhereonlypurchasesareobservedandthe
mapping from purchases to underlying consumption states must be treated as a maintained approximation
rather than as a directly observed object.
Theempiricalexerciseproceedssequentially. First,Iaskastructuralquestion: doobservedwithin-period
price vectors admit a hedonic representation? Equivalently, do they satisfy the equalities implied by the
goods-to-characteristicstechnology(i.e.,(B2 +)inTheorem2.2),sothatcharacteristicshadowpricesarewell
defined? Theseequalitiesactasagatekeeper: iftheyfail,thebehaviouraltestisnoteconomicallymeaningful
because the relevant shadow prices do not exist. Second, conditional on structural feasibility, I ask a
behaviouralquestion: doobservedpurchasesequencessatisfythedynamicRPinequalities(i.e.,(B1 +))when
evaluated at the implied shadow prices? Put differently, once prices can be written as characteristic shadow
values, I ask whether the household’s sequence of purchases is consistent with stable dynamic preferences
over those characteristics. In the data, these inequalities are applied to purchase-period bundles, so the
resulting exercise should be read as a diagnostic of dynamic coherence under the maintained approximation
that purchases track the relevant underlying consumption state at the chosen aggregation.
The sequential decomposition yields two findings. First, most variation in raw pass rates when moving
fromgoodsspacetocharacteristicsspacereflectsthehedonicprice-systemrestrictionsratherthandifferences
in behavioural fit; empirically, however, restoring hedonic consistency typically requires only modest price
adjustments. Second, conditional on satisfying those structural restrictions, allowing for habits improves
20

behavioural coherence. The binary gains are concentrated, but the continuous violation measures show that
dynamic valuation generally moves behaviour closer to rationalisability. These results should therefore be
read as evidence about which restrictions bind in scanner data, and when static valuation remains a useful
approximation.
Market goods are UPC-level products and characteristics are their nutritional content and a small set of
descriptive indicators. The key empirical challenge is that prices are observed only for purchased items.
Accordingly, I implement the missing-price test of Section 2.5.8 In this setting, behavioural discipline is
inherently limited by sparse price support and modest intertemporal budget variation, so the diagnostic
provides a lower bound on the model’s behavioural content. In environments with richer price and quantity
support, the same framework may generate sharper behavioural restrictions.
Thesescanner-datafeaturesalsoaffecthowfailuresshouldbeinterpreted. Unmeasuredproductattributes,
temporarypromotions,inventorybehaviour,andpurchase–consumptionmismatchcanallgenerateviolations
of an exact RP model. I therefore use pass rates together with distance measures to evaluate whether
a maintained valuation exercise is a useful approximation, rather than treating failure as literal evidence
against rational choice.
4.1 Data
I use household-level scanner data on cold cereal purchases from the IRI Academic Datasets’BehaviorScan
panel. The panel covers two U.S. markets (Pittsfield, MA, and Eau Claire, WI) over 2010–2011, with
purchases recorded at checkout via household ID cards and Universal Product Codes (UPCs). I restrict
attentiontostatichouseholdsthatparticipateinall12monthsofacalendaryear,sorecruitmentandattrition
occur only at year-end.
I compute household-specific time periods to accommodate heterogeneity in purchase frequencies. For
household𝑖,let𝑆 𝑖 denotethespanfromfirsttolastpurchaseand𝐺 𝑖 thelongestinterpurchasegap(including
endpoints). I set𝑇 𝑖 =⌊𝑆 𝑖/𝐺𝑖⌋and partition𝑆 𝑖 into𝑇 𝑖 equal-length bins, which guarantees at least one
purchase in each period by construction. Households with𝑇𝑖 <3are excluded to ensure at least two
observed transitions in the one-lag model. This aggregation is conservative for a one-lag specification: it
ensures that the lagged bundle is observed rather than imputed, hence dynamic restrictions are evaluated on
realised purchase transitions. After additionally dropping households with purchases lacking characteristics
information (described below), the analysis sample contains𝑁=2,282households.9 Table 1 summarises
8Imputing prices for unpurchased goods is feasible (e.g., using regional price indices), but it introduces auxiliary assumptions
that can blur whether failures reflect preferences or the imputation procedure.
9AppendixBdocumentsthefullsequenceofsampleconstructionandreportsbalancetestscomparinghouseholdsexcludeddue
to missing characteristics data with the final analysis sample. Differences are modest in magnitude, suggesting limited scope for
21

the resulting panel structure and the scale and variety of the implied choice problems.
Table 1: Sample and household-level panel structure
Statistic Mean Median
Households (𝑁) 2,282
Months covered 2010–2011 (24 months)
Distinct products (𝐾) 801
Characteristics (𝐽) 23
Time periods per household (𝑇𝑖) 7.0 6.0
Period length (days) 106 98
Units purchased per household-period 7.9 6.0
Total units purchased (24 months) 55.1 42.0
Expenditure per household-period ($) 22.1 19.5
Total expenditure (24 months, $) 154.2 116.5
Distinct products purchased (24 months) 32.3 25.0
Notes:Statistics are computed across𝑁=2,282households.𝑇 𝑖 denotes the number of constructed time periods for household𝑖,
defined as𝑇𝑖 =⌊𝑆 𝑖/𝐺𝑖⌋, where𝑆𝑖 is the span between first and last purchase and𝐺𝑖 the longest interpurchase gap. Units are
package counts; expenditures and package counts are aggregated within household-periods and totals are over 24 months.
Households purchase on average 7.9 units per period (median 6.0). Combined with a median period
length of 98 days, this pattern is consistent with ongoing consumption rather than extreme purchase spikes.
While promotions may induce some stockpiling, explaining the observed interpurchase gaps purely through
inventoryaccumulationwouldrequireimplausiblylargestockbuild-upsrelativetototalquantitiespurchased.
Atthesametime,within-periodbasketsremainnarrowinUPCvariety: themedianhousehold-periodcontains
only two distinct purchased products, even though households typically buy several units. I therefore
interpreteachhousehold-periodasameaningfuldynamicchoiceobservation, butnotasaliteralmeasureof
contemporaneousnutrientintake: itaccommodatesidiosyncraticshoppingfrequencieswhilepreservingthe
temporal structure required for testing whether aggregated purchase bundles behave in a manner consistent
with the dynamic RP restrictions.10
Figure 1 shows substantial heterogeneity in shopping frequency (median𝑇𝑖 =6; median period length
98 days). Within each period I aggregate UPC-level quantities and nominal expenditures and compute unit
valuesasexpenditure-to-quantityratios. 11 Becauseunpurchasedgoodshavenoobservedunitvalues,thetest
treats missing prices as unknowns and searches for completions consistent with rationalisability. Reported
pass rates are therefore upper bounds: a household that fails cannot be rescued by any price imputation,
selection on observables.
10Similar coarse aggregation is common in empirical work on dynamic demand when purchase occasions are intermittent (e.g.,
Crawford (2010) uses quarterly panels in an application to tobacco). I obtain qualitatively similar cross-model comparisons under
a common monthly aggregation (i.e.,𝑇𝑖 =24for all𝑖), albeit in a much smaller effective sample because zero-purchase months
become pervasive.
11Expendituresarerecordedinnominaldollarsandconvertedtopresent-valuetermsforthelifecycleformulationusingamonthly
interest-rateseries(30-YearFixedRateMortgageAverage,FRED(FreddieMac,2025));resultsareunchangedundernominalvalues
given the short sample window.
22

while a household that passes does so under at least one completion.
Figure 1: Distribution of constructed time periods and period lengths
(a) Distribution of𝑇𝑖 across households
 (b) Distribution of period lengths (days)
Notes:Left panel shows the distribution of𝑇𝑖 across households (𝑁=2,282). Right panel shows the distribution of
household-level average period length in days.𝑇𝑖 =⌊𝑆 𝑖/𝐺𝑖⌋, where𝑆𝑖 is the span between first and last purchase and𝐺𝑖 the
longest interpurchase gap.
The model is defined over characteristics rather than market goods. For each UPC I construct a vector
of nutritional and descriptive attributes by merging the IRI product file to the (now-defunct) NuVal shelf-
labelling database and, where NuVal is missing, supplementing with data from the FatSecret Platform API,
followingtheapproachinBarahonaetal.(2023). Istandardiseallnutrientstoa100gbasissothatcontinuous
characteristicsarecomparableacrossproducts. Sincescannerquantitiesarerecordedinpackagecounts,the
resulting characteristics matrix should be interpreted as a linear summary of purchased product attributes.
To handle IRI’s placeholder codes for some private-label items, I first map System-88 pseudo-UPCs to their
correspondingrealUPCspriortomerging. Themergedcharacteristicscoverover97%ofpurchase-weighted
observations; I drop unmatched purchase records and then drop households with any remaining unmatched
purchases, so every household in the analysis sample has a complete characteristics mapping for all of its
observed purchases.
I construct𝐽=23characteristics. Eight are continuous Nutrition Facts Panel measures (calories,
carbohydrates, total fat, saturated fat, fibre, protein, sodium, and sugar). The remaining 15 are binary
indicators capturing salient ingredients and descriptors (10 indicators) and the five most prevalent brands
(Kellogg’s, General Mills, Post, Quaker, and Kashi). Table 2 reports the binary definitions. In the baseline
specification I treat sugar and sodium as habit-forming characteristics (𝐽2 =2) and take the remaining
characteristicsasnon-habit-forming,motivatedbyevidencethatsugarandsaltmayactivaterewardpathways
in ways analogous to addictive substances (Avena et al., 2008; Cocores and Gold, 2009). Section 4.2.1
23

reports robustness to alternative partitions. Additional descriptive evidence on purchase intensity, brand
concentration, and the distributions of prices and characteristics is reported in Appendix B.
Table 2: Binary product characteristics used in the hedonic representation
Binary characteristic Construction
whole grain contains ‘whole grain’ or ‘wholegrain’ in ingredient list
organic contains the term ‘organic’ at least once in ingredient list
oat-based contains ‘oat’ as part of the first listed ingredient
granola contains ‘granola’ in product description
health halos contains ‘source of’, ‘natural’, ‘low calorie’, or ‘low fat’ in product description
fruity contains ‘fruit’ in the product description
nutty contains ‘nut’ in product description
chocolatey contains ‘chocolate’ in product description
honey flavour contains ‘honey’ in product description
gluten-free contains ‘gluten free’ in product description
Kellogg’s cereal brand is Kellogg’s
General Mills cereal brand is General Mills
Post cereal brand is Post
Quaker cereal brand is Quaker
Kashi cereal brand is Kashi
Notes:Characteristics are defined at the UPC level using ingredient lists and product descriptions from the merged
IRI–NuVal–FatSecret dataset. Indicators equal one if the stated textual condition is satisfied. Brand indicators correspond to the
five most prevalent national brands in the sample. Continuous nutritional characteristics (calories, carbohydrates, total fat,
saturated fat, fibre, protein, sodium, and sugar, standardised per 100g) are defined separately in Appendix B.
4.2 Results
4.2.1 Rationalisability scores
Two patterns emerge in the raw rationalisability outcomes: allowing for habits increases pass rates within
characteristics space, and goods-based representations exhibit substantially higher pass rates. As the se-
quential logic of the paper makes clear, however, these raw differences conflate structural and behavioural
components. Section 4.2.2 decomposes these margins and quantifies the severity of violations.
The test is implemented at the household level, allowing full heterogeneity in pass/fail outcomes and
in the shadow-price structure of rationalisable households. Because habits enter with a one-period lag,
the empirical exercise uses the observable interior-date analogue of Theorem 2.2. Structural equalities are
imposed on𝑡=2,...,𝑇−1, since period𝑡=1depends on the unobserved initial stock and I do not treat
the last observed purchase period as the consumer’s terminal horizon. The behavioural Afriat inequalities
arethen evaluatedon theretained dates𝑡=2,...,𝑇, sothe finalobservedperiod continuesto disciplinethe
shadow-price sequence. Unless otherwise specified, I impose a lifecycle model with a single intertemporal
budget constraint, so the marginal utility of income is constant across periods.
Under the baseline habits-over-characteristics specification, 1,248 of 2,282 households (54.69%) satisfy
24

thetest. Varyingthesetofhabit-formingcharacteristicshasessentiallynoeffectonclassification: restricting
habitstosugaralone(54.60%),sodiumalone(54.65%),orallowingall23characteristicstobehabit-forming
(54.69%)changesthepassratebyatmost0.09percentagepointsandreclassifiesnomorethantwohouseholds.
Inthisapplication, thedatathereforedonotisolatesugarorsodiumasuniquelyresponsibleforthedynamic
improvement; rather, the main empirical action comes from the maintained hedonic representation, with
habits mattering at the behavioural margin once that representation is imposed. Table 3 reports the full set
of specifications.
Table 3: Household-level pass rates: habits-over-characteristics specifications
Model Description Lifecycle model Pass rate
Habits-over-characteristics 𝐽2=2(sugar and sodium) Yes 54.69%
Habits-over-sugar𝐽 2=1(sugar) Yes 54.60%
Habits-over-sodium 𝐽2=1(sodium) Yes 54.65%
Habits-over-all-characteristics𝐽 2=𝐽=23Yes 54.69%
Notes:A household passes if there exist characteristic shadow prices satisfying the interior-date structural equalities (B2+) in
Theorem 2.2 on𝑡=2,...,𝑇−1and the corresponding dynamic RP conditions (B1 +) on𝑡=2,...,𝑇; by Theorem 2.2, this is
equivalent to the existence of a valid completion of missing prices in the background. Pass rates are computed over𝑁=2,282
households.𝐽=23denotes the total number of characteristics and𝐽2 the number assumed to be habit-forming. All specifications
impose a lifecycle model with a single intertemporal budget constraint.
Raw pass rates differ sharply across representations (Table 4). Moving from characteristics to goods
sharply increases rationalisability from 54.7% to 99.6% under dynamic preferences. This large difference
is driven by the much greater dimensional flexibility of goods-based representations, which impose no
cross-goodpricerestrictions. Onecouldmechanicallyraisecharacteristics-spacepassratesbyaddinglatent
product attributes to the technology matrix. This plays a role analogous to absorbing residual variation
into unobserved product characteristics, but it would change the object being tested: whether an enlarged
characteristic space rationalises choices, rather than whether observed policy-relevant characteristics alone
supportthevaluationinterpretation. Holdingfixedtheobservedcharacteristics,thestructuralrestrictionsbite
through the geometry of the active purchased bundle rather than through broad within-period variety. Many
of the apparent “failures” in characteristics space nevertheless correspond to economically small deviations
from those hedonic restrictions. Section 4.2.2 makes this precise by separating structural and behavioural
sources of empirical discipline and quantifying the magnitude of violations.
By contrast, removing habits within characteristics space reduces the pass rate from 54.7% to 52.4%.
Whilethisdifferenceinlevelsismodest,thepairedcomparisonsbelowshowthatthereclassificationisentirely
directional, with households failing under static preferences but passing once dynamics are introduced. The
next subsection shows that this modest binary gain is only part of the evidence: allowing for habits also
reduces the severity of behavioural violations on average.
25

Table 4: Household-level pass rates across characteristics and goods representations
Model Description Lifecycle model Pass rate
Habits-over-characteristics 𝐽2=2(sugar and sodium) Yes 54.69%
Characteristics (no habits)𝐽 2=0Yes 52.37%
Habits-over-all-goods 𝐾=𝐽=𝐽 2,A=identity(𝐾) Yes 99.56%
Goods (no habits)𝐾=𝐽=𝐽 1,A=identity(𝐾) Yes 92.59%
Goods (no habits) (GARP) 𝐾=𝐽=𝐽 1,A=identity(𝐾) No 99.69%
Notes:A household passes if there exist characteristic shadow prices satisfying the interior-date structural equalities (B2+) in
Theorem 2.2 on𝑡=2,...,𝑇−1and the corresponding dynamic RP conditions (B1 +) on𝑡=2,...,𝑇; by Theorem 2.2, this is
equivalent to the existence of a valid completion of missing prices in the background. Pass rates are computed over𝑁=2,282
households. In characteristics models,𝐽=23and𝐽 2 denotes the number of habit-forming characteristics. In goods models,𝐾
denotes the number of goods andA=identity(𝐾)implies no cross-good price restrictions. “Lifecycle model” indicates whether a
single intertemporal budget constraint is imposed.
The reclassification pattern is strongly directional. Removing habits from the baseline characteristics
model reclassifies 53 households, all of whom fail under static preferences but pass once intertemporal
dependence is introduced (p-value<10−15). These households provide the cleanest empirical illustration
of the valuation wedge in Section 2.2: the maintained characteristics technology can support a hedonic
interpretation, but only if current characteristics are allowed to carry continuation values. By contrast,
changing the allocation of habit-forming characteristics reclassifies at most three households and yields no
statistically significant differences. Table 5 reports the full set of paired comparisons.
Comparisons with goods-based models reveal even larger directional differences. In these cases, most
switching households fail the characteristics-based test but pass the corresponding goods-based alternative.
As shown in the next subsection, this pattern reflects the much greater dimensional flexibility of the goods
representation, which imposes no cross-good price restrictions, rather than tighter behavioural alignment.
Table 5: Paired model comparisons (exact McNemar tests)
Comparison (baseline vs alternative) Pass 0 Pass1 Δ(pp) Switchers𝑝-value
Baseline: Habits-over-characteristics 54.69
Habits-over-all-characteristics 54.69 54.69 0.00 0 1.000
Habits-over-sugar 54.69 54.60 0.09 2 0.500
Habits-over-sodium 54.69 54.65 0.04 1 1.000
Characteristics (no habits) 54.69 52.37 2.32 53 <10−15
Habits-over-all-goods 54.69 99.56 -44.87 1024<10 −15
Goods (no habits) 54.69 92.59 -37.91 1039 <10−15
Goods (no habits) (GARP) 54.69 99.69 -45.00 1031<10 −15
Notes:Pass 0 is the baseline pass rate (habits-over-characteristics with𝐽2=2), Pass1 is the alternative model pass rate, andΔ(pp)
reports Pass0 minus Pass1 in percentage points. “Switchers” is𝑛(1→0)+𝑛(0→1), i.e., the number of households whose
pass/fail classification differs across the paired models.𝑝-values are from exact McNemar (binomial) tests based on the switchers.
Taken together, these results indicate that while the preciseallocationof habits across characteristics
plays little role in classification, introducing intertemporal dependence in characteristics space improves
26

rationalisability for a limited but directionally important subset of households. In this application, the main
empirical action comes from the maintained hedonic representation, while habits matter at the behavioural
margin. Theevidence istherefore notthat cerealpurchases reveal largesugar orsodium habits. It is thatthe
framework separates a demanding price-representation problem from a behavioural question about whether
static valuation is a useful approximation.
4.2.2 Structural and behavioural sources of empirical discipline
IfthetestistoserveasaninterpretationcheckforrecoveredWTPobjects,rejectioncannotbetheendofthe
analysis. Abinarypass/failoutcomesayswhetherthemaintainedmodelholdsexactly,butnotwhetheritfails
marginally or substantially. It also does not reveal whether the problem is the hedonic price representation
orintertemporalbehaviour. Ithereforeseparaterationalisabilityintostructuralandbehaviouralcomponents
and quantify violations on each margin using distance measures. The construction exploits the fact that
representation theorems induce measures of rationality violations through the distance to their defining
restrictions (e.g., Andrews (2026)).
In the hedonic setting, this distinction admits a natural decomposition. The two possible sources of
failure map directly into the model’s restrictions. Rationalisability in the habits-over-characteristics model
requiresjointsatisfactionoftwoconceptuallydistinctrestrictions.Structuralequalities(B2 +)linkobserved
prices to product characteristics through the hedonic technology and act as overidentifying restrictions
on the admissible shadow-price representation. This is the gatekeeper stage of the empirical analysis.
Behaviouralinequalities(B1+)constrainintertemporalchoicethroughshadowpricesandthediscountfactor
(Theorem 2.2). Separating these margins clarifies where empirical discipline originates in characteristics-
based valuation and how it differs from more flexible goods-based representations.
The structural equalities require that, in each household-period, the observed price vectorρ+ 𝑡 lies in
the column space of the augmented characteristics matrix˜B𝑡 :=
h
B′ 𝑡|(B 𝑎 𝑡)′
i
. In principle this is a
dimensionality-reduction restriction: prices must be representable through a lower-dimensional character-
istics technology rather than arbitrary goods-specific shifters. In the scanner environment studied here,
however, the active choice sets are typically narrow, so the empirical bite of the restriction depends on the
realisedrankofthepurchasedbundle. Whenthepurchased-goodmatrixhasfullrowrank,thecolumnspace
of ˜B𝑡 spansallofR 𝐾+ 𝑡 andthestructuralequalitiesaremechanicallysatisfied. Non-zerostructuraldistances
thereforearisepreciselyinthosehousehold-periodswheretheactivebundleisrankdeficient,eitherbecause
thehouseholdbuystoofewlinearlyindependentproductsorbecausethepurchasedUPCshavehighlysimilar
characteristic profiles.
Thisisempiricallyplausibleincerealdata,wherecloselyrelatedUPCsoftendifferonlyinpackagesize,
27

branding,orminorformulationdetailsandthereforecarryverysimilarmeasuredcharacteristicvectors. Even
afterconditioningonarichsetofnutritionalanddescriptivecharacteristics,scannerpricesalsoreflectretailer
pricing strategies, temporary promotions, and mark-ups driven by market power or shelf placement that do
notcorrespondtoattributeshouseholdsconsume. Whentheactivebundleislowrank,thoseretailer-specific
price components cannot be absorbed by the hedonic system and therefore appear as structural residuals.
To quantify the severity of these violations, I compute for each household-period the Euclidean distance
𝑑𝑡 =
ρ+ 𝑡− ˜B𝑡 ˜B+ 𝑡 ρ+ 𝑡 ,
where ˜B+ 𝑡 denotes the Moore–Penrose pseudoinverse and ˜B𝑡 ˜B+ 𝑡 is the orthogonal projector onto the
equalitymanifoldimpliedbythehedonicrepresentation. Equivalently,observedpricesadmittheorthogonal
decomposition
ρ+ 𝑡 = ˜B𝑡 ˆπ𝑡 +r 𝑡,
whereˆπ𝑡 minimises∥ρ+ 𝑡− ˜B𝑡 π∥andr 𝑡 is orthogonal to the column space of˜B𝑡. The distance𝑑𝑡 =∥r 𝑡∥,
measured in dollars, therefore captures the minimal joint price adjustment required for a hedonic price
representation to exist. For example,𝑑𝑡 =1.0means that the minimum adjustment vector to prices has
Euclideannorm1dollar;equivalently,thesumofsquaredpriceadjustmentsacrossthegoodspurchasedthat
period is 1.
One response to violations of the hedonic equalities is to augment the technology with latent character-
istics, as in Blow et al. (2008), thereby expanding the price manifold until the equalities hold. In the limit,
sufficiently rich product-specific latent attributes collapse the characteristics model toward a goods-space
representation, mechanically reducing structural violations. I do not pursue this route here. My objective is
not to restore rationalisability by construction, but to ask how much discipline is imposed by the observed,
policy-relevant characteristics and to separate structural misspecification from behavioural inconsistency.
Figure 2 plots the distribution of mean distances across households for both characteristics- and goods-
basedspecifications. Thecharacteristicsmodelsexhibitawide,right-skeweddistributioncentredabovezero.
Inthisapplication,thosedistancesshouldbereadasevidencethatmanyactivebundlesfailtospantheirown
purchased-good price space once prices are projected through the maintained characteristics technology.
Even so, the implied unit-price violations are often modest in magnitude: most household-periods require
a minimum joint price adjustment with Euclidean norm below 1 dollar to restore hedonic consistency. As
a rough benchmark, average household cereal expenditure is $22.1 per period. By contrast, goods-based
models impose no cross-good price restrictions and therefore satisfy the structural equalities mechanically,
28

yielding𝑑 𝑡 =0.
Figure 2: Mean distance-to-manifold
Notes:Histograms of the household-level mean of the structural distance measure across periods. Distances are measured in
dollars and represent the minimal joint price adjustment required for the hedonic price equalities to hold. Left panel reports the
characteristics specification; right panel the goods specification.
Animportantimplicationofthisgeometryisthatallcharacteristics-basedspecificationsimposeidentical
structural restrictions. Habit-forming characteristics enter˜B𝑡 only as duplicated rows ofB𝑡 and therefore
neither increase its rank nor enlarge the feasible price set. Structural restrictiveness is thus governed
entirely by the hedonic representation itself, not by the allocation of habits across characteristics. In the
present data, this means that structural rejection is best understood as a statement about the linear algebra
of narrow purchased bundles—their rank and characteristic collinearity—rather than about the dynamic
specification per se. Moreover, these structural restrictions operate at the level of prices and characteristics
and are conceptually distinct from inventory dynamics: even if households smooth consumption through
inventories, prices must still admit a hedonic representation for shadow prices to be well defined.
To measure behavioural restrictiveness, I adapt the Critical Cost Efficiency Index (CCEI) following
Afriat (1973) and Varian (1990). The CCEI measures the smallest proportional relaxation of revealed
affordability required for the behavioural inequalities in (B1+) to admit a solution.12 Economically, a CCEI
12The CCEI is interpreted here strictly as a measure of RP slack, following its original cost-efficiency interpretation in Afriat
(1973). As emphasized by Echenique (2022), it shouldnotbe interpreted as a welfare loss or a measure of foregone surplus.
29

of𝜂indicates that the revealed-affordability comparisons in the lifecycle RP test need only be relaxed by at
most(1−𝜂)×100%for the observed intertemporal choice path to become rationalisable. Values close to
one therefore indicate that behaviour is nearly dynamically rational, while lower values signal more severe
violations. The index is defined only for households whose prices lie exactly on the equality manifold,
because characteristic shadow prices—and hence the behavioural inequalities themselves—are well defined
only when the hedonic equalities hold. In this sense, the CCEI plays an analogous role to a goodness-of-fit
statistic for intertemporal choice: it quantifies how much slack must be introduced before the model can
rationalise observed behaviour, holding the price system fixed.
Figure 3 shows that behavioural violations are generally modest, but systematically smaller when habits
areallowed. Allcharacteristics-basedspecificationsexhibitsubstantialmassnearunity,indicatingthatonce
the hedonic structure is satisfied, only limited perturbations are needed to rationalise behaviour. However,
the static characteristics model without habits displays a thicker lower tail, reflecting greater intertemporal
inconsistency even when structural feasibility holds. A parallel pattern arises in the goods domain: the
habits-over-goods specification yields CCEIs tightly concentrated near one, while the static goods model
exhibits a wider distribution with more mass below 0.95. These patterns indicate that allowing for habits
reduces measured behavioural violations by absorbing intertemporal reversals that the static model cannot
rationalise.
This behavioural improvement matters for interpretation. For households that satisfy the dynamic
characteristics model but fail the static counterpart, the data reject the restriction that characteristic shadow
prices can be read purely as contemporaneous marginal valuations. In those cases, a valuation exercise that
treats sugar or sodium prices as static WTP imposes an additional timing restriction not supported by the
observed purchase path. The empirical test therefore identifies when the dynamic wedge characterised in
Section 2.2 is supported.
Theabovedistancemeasuresshowwhereandhowseverelythemodelfails,buttheydonotbythemselves
showwhethertherestrictionsaredemandinginthisscannerenvironment. Thisisthefit-versus-restrictiveness
concern emphasised by Selten (1991): a model may rationalise many datasets because it captures structure,
orbecausenearbyalternativeswouldalsopass. Ithereforecomplementthedecompositionwithasimulation
benchmark in the spirit of Fudenberg et al. (2023), which evaluates how unusually well the model fits
the observed data relative to nearby feasible perturbations of the scanner environment. The benchmark
preserves each household’s zero pattern and total expenditure while allowing prices and quantities to vary
locally, thereby inducing a comparison distribution over structural and behavioural discrepancy measures.
Full details are provided in Supplemental Appendix??.
30

Figure 3: Critical Cost Efficiency Index (CCEI)
Notes:Histograms of household-level CCEI values across model specifications. The CCEI is the smallest proportional relaxation
of the behavioural RP inequalities required for feasibility; values closer to one indicate smaller violations. Computed only for
households satisfying the structural price equalities. Vertical axis is on a log scale.
Onthestructuralmargin,thebenchmarkconfirmsthatthehedonicequalitiesimposesubstantialempirical
discipline. Observed scanner prices are, on average, closer to the equality manifold than locally perturbed
price systems, yet are rarely extreme outliers relative to the induced comparison distribution. This indicates
that the hedonic restrictions are demanding and not trivially satisfied. By contrast, goods-based models
impose no cross-good price restrictions and therefore cannot fail on the structural margin, accounting for
their much higher raw pass rates.
On the behavioural margin, CCEI values are extremely close to one in both the observed and locally
perturbeddata,leavinglittlescopeforbehaviourtoappearunusuallyefficientinaquantilesense. Thisreflects
theempiricalenvironment—sparseactivechoicesetsandlimitedintertemporalbudgetvariation—ratherthan
a lack of behavioural content in the model.
Taken together, the price geometry, behavioural slack measures, and simulation benchmark clarify the
interpretation of raw pass rates. Structural restrictions embedded in the hedonic representation largely
determinedifferencesacrossgoodsandcharacteristicsmodels,butinthisapplicationtheydosothroughthe
rank properties of the active purchased bundles rather than through a broad market-level dimension count
31

alone. Conditionalonthoserestrictions, allowingforhabitformationsystematicallyimprovesintertemporal
coherencerelativetostaticpreferences. Goods-basedmodelsachievehighpassratesprimarilybecausethey
impose little structural content, not because they deliver a tighter account of behaviour.
4.2.3 Discount factors
The RP conditions are evaluated conditional on the discount factor𝛽. Supplemental Appendix??reports
thefractionofrationalisablehouseholdsconsistentwitheachvalueonafinegrid𝛽∈[0.95,1]. Acceptance
probabilitiesareuniformlyhighacrossthegridunderbothhabits-over-characteristicsandhabits-over-goods
specifications, with no economically meaningful monotonic pattern.
These results indicate that, conditional on the hedonic price restrictions, the behavioural inequalities
impose only weak discipline on intertemporal discounting in this environment. The identification sets for𝛽
are wide, cautioning against interpreting discount factors recovered from nonparametric dynamic RP tests
as tightly identified structural parameters in scanner data.
4.2.4 Predictors of rationalisability
Pass/fail outcomes are primarily associated with the scale and complexity of the observed choice problem
rather than with demographics per se. Table 6 reports average marginal effects from probit regressions of
the pass indicator on household characteristics. Column (1) includes demographics only; Column (2) adds
measures of purchasing intensity and variety.
In the demographic-only specification, households with children are 10.6 percentage points less likely
to pass. Once purchasing controls are added, this effect attenuates and becomes statistically insignificant.
By contrast, scale measures remain economically large and significant: an interquartile increase in two-year
cereal expenditure is associated with roughly a 25 percentage point lower probability of passing, while a
comparable increase in product variety reduces the probability by about 8 percentage points.
Takentogether,theseresultssuggestthathouseholdcompositionmattersprimarilythroughthescaleand
complexity of the observed choice problem. Larger and more diverse purchasing patterns generate a greater
number of structural and behavioural constraints, increasing the likelihood that at least one is violated. For
instance, when a household purchases products with sharply different nutritional profiles across periods,
the implied cross-attribute shadow-price system must rationalise a wider range of price–quantity trade-offs
than in households that repeatedly buy a narrow set of similar cereals. Demographics per se have limited
explanatorypoweroncethiseffectivedimensionalityisaccountedfor. Thedemographics-onlyspecification
hasalmostnoexplanatorypower(McFaddenpseudo-𝑅 2=0.009),whereasthespecificationwithpurchasing
controls reaches a more substantial 0.176.
32

Table 6: Determinants of rationalisability: probit average marginal effects
Dependent variable: Pr(Pass)
(1) demographics only (2) w/ purchasing controls
young child−0.106−0.081
(0.084) (0.079)
children−0.106 ∗∗ −0.012
(0.033) (0.030)
age group HH head0.004−0.006
(0.012) (0.011)
education HH head−0.00004 0.001
(0.008) (0.007)
Pittsfield0.005−0.001
(0.021) (0.022)
high income HH† −0.036 0.008
(0.025) (0.023)
total units purchased0.00002
(0.001)
total expenditure−0.002 ∗∗∗
(0.0003)
total unique products−0.003 ∗∗
(0.001)
Pseudo-𝑅2 (McFadden)0.009 0.176
Observations 2,187 2,187
∗p<0.1;∗∗p<0.05;∗∗∗p<0.01.
†High-income indicator equals one for pre-tax income≥75k.
Notes:Entries report average marginal effects from probit models of an indicator for passing the habits-over-characteristics test.
Column (1) includes demographic controls only; column (2) additionally includes purchasing intensity measures. Standard errors
in parentheses are based on the delta method. 95 observations omitted due to missing demographic data.
5 Conclusion
This paper provides a nonparametric foundation for valuing characteristics when those characteristics may
be habit forming. Policies often target attributes such as sugar, sodium, alcohol, caffeine, or emissions, and
appliedworkofteninterpretscharacteristicpricesordemandcoefficientsasstaticWTP.Ishowthatapurely
contemporaneous interpretation is valid only under a restriction: current consumption of the characteristic
must carry no continuation value.
The main result is an Afriat-type characterisation of dynamic hedonic valuation. Observed prices and
choices admit a dynamic characteristics-based interpretation if and only if there exist characteristic shadow
prices and a discount factor satisfying structural price equalities and dynamic behavioural inequalities. The
33

structural equalities require observed goods prices to be representable through the maintained goods-to-
characteristics technology. The behavioural inequalities require choices to be dynamically rationalisable at
the implied shadow prices.
The framework clarifies why dimensionality reduction and dynamics play different roles. Moving from
goodstocharacteristicsyieldsparsimonybutimposesgeometricdisciplineontheadmissiblerepresentation
of prices. Accommodating dynamic preferences does not relax that discipline. Rather, it changes the be-
haviouralrestrictionsimposedoncecharacteristicshadowpricesexist: choicesthatviolatestaticseparability
maystillberationalisablewhencurrentcharacteristicsareallowedtoaffectfuturemarginalvaluations. This
distinctionmattersforpolicybecausestaticWTPmaybeinformativeatafixedstate,whilestaticanddynamic
counterfactuals can diverge when policy effects propagate through habit stocks.
Thecerealapplicationillustratesthislogicinapurchase-basedscannersetting. Goods-basedbenchmarks
passatveryhighrates,whilecharacteristics-basedmodelsfailmoreoftenbecauseobservedpricesfrequently
violate the hedonic spanning restriction. The associated distance measures show, however, that many
structural violations are economically modest. Conditional on structural admissibility, behaviour is close
to dynamically rational, and allowing for habit formation improves behavioural coherence relative to static
characteristics models for a subset of households.
The framework is best understood as a diagnostic of admissibility and interpretation rather than as a
pointestimatorofwelfareprimitives. Rationalisabilitydoesnotidentifyauniquedynamicpreferencerepre-
sentation, and the continuation component of characteristic prices is generally set identified without further
structure. This limitation is also informative: it shows exactly which additional assumptions are required
before static WTP, dynamic WTP, or policy counterfactuals can be given a unique welfare interpretation.
Empirical failure should be read in the same spirit: it points to an incomplete maintained representation
rather than literal irrationality.
Several directions for future work follow directly. Richer data with denser price support, more frequent
observation, and greater intertemporal budget variation would sharpen both structural and behavioural
restrictions. On the modelling side, extensions to stochastic choice, richer unobserved heterogeneity, and
environments in which utility depends on current goods while habits attach to lagged characteristics would
broadenthescopeofthetest. ThebroadermessageisthatWTPforproductcharacteristics,whetherrecovered
frompricesordemandsystems,isnotautomaticallyasufficientstatisticforpolicycounterfactuals: thispaper
providesadisciplinedframeworkfortestingwhethercharacteristicshadowvaluesexist,whethertheycanbe
read statically, and when their use in counterfactuals should account for continuation effects.
34

Appendix
A Proofs
Proof of Lemma 2.1.
Substituting the technology constraint˜z𝑡 = ˜A˜x𝑡 into the consumer’s lifetime problem in (1) and using
the lifetime budget constraint to substitute out the outside good, the relevant Lagrangian can be written as
L({x𝑡})=
𝑇∑︁
𝑡=1
𝛽𝑡−1𝑢( ˜A˜x𝑡)−
( 𝑇∑︁
𝑡=1
ρ′ 𝑡 x𝑡−𝑊
)
,(9)
wherex 0 is treated as fixed,𝑊is interpreted as lifetime wealth net of outside-good consumption, and I
normalise the multiplier on lifetime wealth to one.
Usingthechainrule(Felippa,2004),therelevantderivativesare𝜕𝑢( ˜A˜x𝑡)/𝜕x𝑡 =[I 𝐾×𝐾 |0 𝐾×𝐾] ˜A′𝜕𝑢(˜z𝑡)
and𝜕𝑢( ˜A˜x𝑡+1)/𝜕x𝑡 =[0 𝐾×𝐾 |I 𝐾×𝐾] ˜A′𝜕𝑢(˜z𝑡+1).13 Here𝜕𝑢(˜z𝑡):=[𝜕 z𝑐 𝑡𝑢(˜z𝑡)′,𝜕 z𝑎 𝑡𝑢(˜z𝑡)′,𝜕 z𝑎 𝑡−1𝑢(˜z𝑡)′]′.
For interior dates𝑡∈{1,...,𝑇−1}, the relevant first-order necessary conditions associated with the
Lagrangian in (9) now follow immediately as,
𝜕x𝑡L=0⇒ρ 𝑡 =𝛽 𝑡−1
h
I𝐾×𝐾

 0𝐾×𝐾 i ˜A′𝜕𝑢(˜z𝑡)+𝛽 h 0𝐾×𝐾

 I𝐾×𝐾 i ˜A′𝜕𝑢(˜z𝑡+1)  .(10)
But recall from (2) that˜Ais a2𝐾×(𝐽+𝐽 2)block matrix. Since the supergradient𝜕𝑢(˜z𝑡)can also be
partitioned as a𝐽+𝐽 2 block vector,𝜕𝑢(˜z𝑡):=[(𝜕 z𝑐 𝑡𝑢(˜z𝑡))′,(𝜕 z𝑎 𝑡𝑢(˜z𝑡))′,𝜕 z𝑎 𝑡−1𝑢(˜z𝑡)′]′, these FOCs reduce
to:
ρ𝑡 =𝛽 𝑡−1 '›
«
A′
 𝜕z𝑐 𝑡𝑢(˜z𝑡) 𝜕z𝑎 𝑡𝑢(˜z𝑡)  +𝛽(A 𝑎)′ h 𝜕z𝑎 𝑡𝑢(˜z𝑡+1) i“ﬁ ‹ .(11)
At the terminal date, the continuation term vanishes. Hence the corresponding FOC reduces to
ρ𝑇 =𝛽 𝑇−1 A′
 𝜕z𝑐 𝑇𝑢(˜z𝑇) 𝜕z𝑎 𝑇𝑢(˜z𝑇)  ,(12)
which is exactly the same pricing condition as in (11) under the conventionπ1 𝑇+1≡0. Since I assume𝑢to
be concave, the associated KKT conditions are sufficient for a global maximum. Hence, allowing for corner
13Since𝑢(·)isassumedtobeconcavebutnotnecessarilydifferentiable,each𝜕𝑢(˜z 𝑡)denotesasupergradient. Assuch,expressions
likethosebelowshouldformallybeinterpretedassetinclusionsratherthanstrictequalities—e.g.,0∈𝜕 x𝑡L. When𝑢isdifferentiable
at˜z𝑡, the supergradient is a singleton and the equality holds exactly.
35

solutions, I replace the stationarity equalities in (11) and (12) with inequalities to obtain the full set of price
and data pairs{ρ𝑡,x𝑡}𝑇 𝑡=1 consistent with an interior or corner solution to the consumer’s maximisation
problem. This gives rise to my formal definition ofconsistencyin Definition 2.1 and Lemma 2.1.□
Proof of Theorem 2.1.
(𝐴)⇒(𝐵): Assume(𝐴)holds. Then, by Lemma 2.1,ρ 𝑡≥A ′π0 𝑡+(A 𝑎)′π1 𝑡+1 for all𝑡∈{1,...,𝑇},
with equality for all𝑘such that𝑥𝑘 𝑡 >0, whereπ 1 𝑇+1≡0. Element wise, this states that for all𝑘and for all
𝑡∈{1,...,𝑇},𝜌 𝑘 𝑡 ≥a′ 𝑘π0 𝑡+a𝑎′ 𝑘 π1 𝑡+1,and where𝑥 𝑘 𝑡 >0,𝜌 𝑘 𝑡 =a′ 𝑘π0 𝑡+a𝑎′ 𝑘 π1 𝑡+1.This gives us restrictions
(B2) and (B3), respectively.
It remains to show (B1) holds. Using the augmented notation˜z𝑡 :=((z 𝑐 𝑡)′,(z 𝑎 𝑡)′,(z 𝑎 𝑡−1)′)′ and˜π𝑡 :=
1
𝛽𝑡−1

π0′ 𝑡 ,π 1′ 𝑡 ′ itfollowsfromtheshadow-pricedefinitionsin(3)thatforanyelementofthesuperdifferential
of𝑢at˜z𝑡,
𝜕𝑢(˜z𝑡)′= h 𝜕z𝑐 𝑡𝑢(˜z𝑡)′,𝜕 z𝑎 𝑡𝑢(˜z𝑡)′ ,𝜕 z𝑎 𝑡−1𝑢(˜z𝑡)′ i = 1 𝛽𝑡−1  π0′ 𝑡 ,π 1′ 𝑡  =˜π′ 𝑡.
The concavity and superdifferentiability of𝑢(˜z𝑡)imply𝑢(˜z 𝑠)−𝑢(˜z𝑡)≤𝜕𝑢(˜z 𝑡)′(˜z𝑠−˜z𝑡)for all𝑠,𝑡∈
{1,...,𝑇}. Combining this concavity result with the optimising behaviour above gives𝑢(˜z𝑠)−𝑢(˜z𝑡)≤
˜π′ 𝑡(˜z𝑠−˜z𝑡)for all𝑠,𝑡∈{1,...,𝑇}. Take any finite ordered cycle(𝑡 1,...,𝑡 𝑀)from𝜏, with𝑡 𝑀+1 =𝑡 1.
Summing the corresponding inequalities𝑢(˜z𝑡𝑚+1)−𝑢(˜z𝑡𝑚)≤˜π′ 𝑡𝑚(˜z𝑡𝑚+1−˜z𝑡𝑚),for𝑚=1,...,𝑀gives
0≤ ˝𝑀 𝑚=1 ˜π′ 𝑡𝑚(˜z𝑡𝑚+1−˜z𝑡𝑚), which is restriction (B1).
(𝐵)⇒(𝐴): Restriction (B1) imposes that the finite dataset( ˜π𝑡,˜z𝑡),𝑡=1,...,𝑇is cyclically monotone as
definedbyBrowning(1989). Bythestandardfinite-sampleAfriatinequalities(Afriat,1967;Diewert,1973;
Varian, 1982), this is equivalent to the existence of𝑇numbers{𝑉𝑡}𝑇 𝑡=1 such that𝑉𝑠≤𝑉𝑡+˜π′ 𝑡(˜z𝑠−˜z𝑡)for
all𝑠,𝑡∈𝜏. ApplyingAfriat’stheoremtothefinitedataset {˜π𝑡,˜z𝑡}𝑡∈𝜏 thenimpliesthatthereexistsalocally
non-satiated and concave utility function rationalising these observations. One such representation is the
Afriat envelope,
𝑢(˜z):=min
𝑡∈𝜏

𝑉𝑡+˜π′ 𝑡(˜z−˜z𝑡) 	 .
Since𝑢(·)is the minimum of finitely many affine functions, it is proper, concave, and superdifferentiable.
Moreover, the Afriat inequalities imply that at each observed˜z𝑡 the𝑡-th affine function supports𝑢, so that
˜π𝑡∈𝜕𝑢(˜z𝑡),∀𝑡∈𝜏.Selectingonesuchsupergradientateachobservedpointandpartitioningitconformably
yields the following relationships between shadow prices and supergradients of the utility function:
π0 𝑡 =𝛽 𝑡−1
 𝜕z𝑐 𝑡𝑢(˜z𝑡) 𝜕z𝑎 𝑡𝑢(˜z𝑡)  andπ 1 𝑡 =𝛽 𝑡−1 h 𝜕z𝑎 𝑡−1𝑢(˜z𝑡) i .(13)
36

Since these hold for all𝑡∈𝜏, the latter condition can be forwarded one period to obtain,
π1 𝑡+1 =𝛽 𝑡
h
𝜕z𝑎 𝑡𝑢(˜z𝑡+1)
i
(14)
for all𝑡∈{1,...,𝑇−1}. Substituting expressions (13) and (14) into condition (B2) re-written in matrix
form,ρ𝑡≥A′π0 𝑡+(A 𝑎)′π1 𝑡+1,I obtain,
ρ𝑡≥A′𝛽𝑡−1
 𝜕z𝑐 𝑡𝑢(˜z𝑡) 𝜕z𝑎 𝑡𝑢(˜z𝑡)  +(A 𝑎)′𝛽𝑡 h 𝜕z𝑎 𝑡𝑢(˜z𝑡+1) i .(15)
At the terminal date, condition (B2) reduces underπ1 𝑇+1≡0toρ 𝑇≥A′𝛽𝑇−1
h
𝜕z𝑐 𝑇𝑢(˜z𝑇)′ 𝜕z𝑎 𝑇𝑢(˜z𝑇)′
i′
.
In the event that a good𝑘is consumed in strictly positive amounts, then substituting expressions (13) and
(14) into condition (B3) yields the same expression as in (15), but with equality; the terminal-date analogue
again follows by settingπ1 𝑇+1≡0. By Lemma 2.1, this means that the data{ρ𝑡;x𝑡}𝑡∈{1,...,𝑇} are consistent
with the one-lag habits model for given technologyA.□
Proof of Theorem 2.2.
(𝐴+)⇒(𝐵 +): Given{ρ 0 𝑡}𝑡∈{1,...,𝑇} Ihaveafullsetofprices,{ρ 𝑡}𝑡∈{1,...,𝑇} ,suchthatthedatasatisfiesthe
model. Hence, by Theorem 2.1, condition(𝐵)holds. Hence,(𝐵+)also holds.
(𝐵+)⇒(𝐴 +): I have shadow discounted prices  π0 𝑡 	 𝑡∈{1,...,𝑇} and  π1 𝑡 	 𝑡∈{1,...,𝑇} such that (B1+) and
(B2+) hold. Use these shadow prices to construct the unobserved prices asρ0 𝑡 =(B 0 𝑡)′π0 𝑡+(B 𝑎,0 𝑡 )′π1 𝑡+1,
withπ 1 𝑇+1≡0. Using these constructed prices, it follows by comparison with Theorem 2.1 that (A+) holds.
□
Habits over goods as a special case of the characteristics model (Definition 3.1).
The(one-lag)habits-over-characteristicsmodelneststhehabits-over-goodsmodelofCrawford(2010)as
a special case. To see this, consider a trivial characteristics model where𝐽=𝐾and the technology matrix
Ais the𝐽×𝐽identity matrix. Then:
z𝑡 =
 z𝑐 𝑡 z𝑎 𝑡  =  x𝑐 𝑡 x𝑎 𝑡  =x 𝑡,
wherex 𝑐 𝑡 andx 𝑎 𝑡 denote the𝐽 1 non-habit-forming and𝐽 2 habit-forming goods, respectively. Under this
assumption, the matrices(A𝑐)′ and(A 𝑎)′ take on block-structured forms. The matrix(A𝑐)′ is a𝐾×𝐽 1
matrixwhosefirst𝐽 1rowsforma𝐽 1×𝐽 1identitymatrix,withallremainingentriesequaltozero. Conversely,
37

(A𝑎)′ is a𝐾×𝐽 2 matrix whose bottom𝐽2 rows comprise a𝐽2×𝐽 2 identity matrix, while the entries in the
first𝐾−𝐽 2 rows are zero.
Substituting the identity structure ofAinto Equation (★) and defining the augmented bundle¯x𝑡 :=
x𝑐′ 𝑡 ,x𝑎′ 𝑡 ,x𝑎′ 𝑡−1
′
=˜z𝑡, the FOC becomes,
ρ𝑡 =
 ρ𝑐 𝑡 ρ𝑎 𝑡  ≥  π𝑐,0 𝑡 0𝐾−𝐽 1  +  0𝐾−𝐽 2 π𝑎,0 𝑡  +  0𝐾−𝐽 2 π1 𝑡+1  =𝛽 𝑡−1  𝜕x𝑐 𝑡𝑢(¯x𝑡) 0𝐾−𝐽 1  +𝛽 𝑡−1  0𝐾−𝐽 2 𝜕x𝑎 𝑡𝑢(¯x𝑡)  +𝛽 𝑡  0𝐾−𝐽 2 𝜕x𝑎 𝑡𝑢(¯x𝑡+1)  ,
whereπ 𝑐,0 𝑡 ,π 𝑎,0 𝑡 andρ 𝑐 𝑡,ρ 𝑎 𝑡 are the subvectors ofπ0 𝑡 andρ 𝑡 corresponding to non-habit-forming and
habit-forminggoods,respectively,andthefinalequalityfollowsusingtheshadow-pricedefinitionsin3. For
all𝑘such that𝑥 𝑘 𝑡 >0, these inequalities hold with equality. Thus, under the restriction𝐽=𝐾andA=I 𝐽,
Definition 2.1 simplifies as in Definition 3.1.
Proof of Corollary 3.1.
FollowsdirectlyfromTheorem2.1 undertherestriction𝐽=𝐾andA=I 𝐽. Equivalently, one mayderiveit
from Definition 3.1 by replicating the proof of Theorem 2.1.□
Intertemporally separable preferences over characteristics (Definition 3.2).
To formalise this nesting result, assumez𝑡 =z 𝑐 𝑡 and embed the model in a lifecycle framework with a
single intertemporal budget constraint and maintain the normalisation that the marginal utility of lifetime
wealth equals one. Then the shadow price in Equation (3) reduces toπ𝑡 =𝜕 z𝑡𝑢(z𝑡),noting that𝛽no
longer appears due to intertemporal separability.14 Under these assumptions, Definition 2.1 reduces to that
in Definition 3.2.
Proof of Corollary 3.2.
Corollary 3.2 is immediate from Theorem 2.1 upon setting𝐽1=𝐽and𝛽=1.
InowshowthatthisCorollaryisequivalenttoTheorem1ofBlowetal.(2008)whenthestaticcharacteristics
modelisembeddedinalifecycleframework. Equivalencebetween(A”)andtheP”conditionintheirtheorem
followsdirectlyfromDefinition3.2. Equivalenceofconditions(B2”)and(B3”)with(A2)and(A3)inBlow
et al. (2008) is straightforward after aligning notation.
The key step is to show that condition (B1”) is equivalent to condition (A1) in Blow et al. (2008), which
states that there exist𝑇scalars𝑉𝑡 and𝑇vectorsπ 𝑡 such that:
𝑉𝑠≤𝑉𝑡+𝜆𝑡 π′ 𝑡(Ax𝑠−Ax𝑡) ∀𝑠,𝑡.(A1)
14This is equivalent to setting𝛽=1, which is without loss of generality in this setting.
38

In Blow et al. (2008),𝜆𝑡 denotes the (time-𝑡) marginal utility of wealth. Under my single lifetime budget
constraint I have𝜆𝑡≡𝜆, and I maintain the normalisation𝜆=1throughout.
To show that (B1”) implies (A1), note that (B1”) imposes cyclical monotonicity on the finite dataset
{π𝑡,z𝑡}𝑇 𝑡=1. By the standard finite-sample Afriat inequalities (Afriat, 1967; Diewert, 1973; Varian, 1982),
this is equivalent to the existence of𝑇numbers{𝑉𝑡}𝑇 𝑡=1 such that𝑉𝑠≤𝑉𝑡+π′ 𝑡(z𝑠−z𝑡)for all𝑠,𝑡. Since
z𝑡 =Ax 𝑡 in the static characteristics model, this becomes𝑉𝑠≤𝑉𝑡+π′ 𝑡(Ax𝑠−Ax𝑡)for all𝑠,𝑡, which is
(A1) under the normalisation𝜆𝑡≡1.
Conversely,suppose(A1)holds. Under𝜆=1,rearrangingyields0≤(𝑉 𝑡−𝑉𝑠)+π ′ 𝑡(Ax𝑠−Ax𝑡). Takeany
finiteorderedcycle(𝑡 1,...,𝑡 𝑀)with𝑡 𝑀+1 =𝑡 1. Summingthecorrespondinginequalitiesover𝑚=1,...,𝑀
makes the Afriat numbers telescope, yielding0≤˝𝑀 𝑚=1 π′ 𝑡𝑚(Ax𝑡𝑚+1−Ax𝑡𝑚), which is (B1”).
I conclude that Corollary 3.2 provides an equivalent characterisation to Blow et al. (2008) when the static
characteristicsmodelisembeddedinalifecycleframework. Thishighlightstheadditionalempiricalrestric-
tionsimposedbyintertemporaloptimisation: aconsumerconsistentwithintratemporalutilitymaximisation
over characteristics must also allocate expenditure across periods to maximise lifetime utility.□
B Additional data description and summary statistics
This appendix reports additional descriptive statistics for the scanner panel, including sample selection
details, purchase intensity, brand concentration, price distributions, and characteristics distributions.
B.1 Sample selection
I begin by documenting the construction of the estimation sample from the raw 2010–2011 scanner panel.
Table 7 reports the sequential filtering steps and resulting sample sizes. The first four restrictions impose
minimumactivityandpanel-lengthrequirementsrequiredforfeasibilityoftherevealedpreferenceframework
and are therefore purely mechanical. The final restriction—dropping households whose purchased UPCs
lack complete characteristics data—is the only potentially selective cut and is evaluated separately using
balance tests.
As shown in Table 7, most sample attrition occurs due to mechanical feasibility restrictions, while the
potentially selective exclusion due to missing characteristics data affects a comparatively smaller subset of
households.
39

Table 7: Sample construction and filtering
Step Households UPCs (K) Purely
mechanical
raw scanner (2010–11 combined) 4697 1139 Yes
drop HHs with only one observed purchase occasion 4505 1136 Yes
drop HHs with only one constructed time period (𝑇𝑖≤1) 3673 1131 Yes
drop HHs with𝑇𝑖≤2(not meaningful for habit formation) 2972 1121 Yes
drop HHs who purchase UPCs with missing characteristics data 2282 801 No
Notes:Rows report sequential sample restrictions applied to the 2010–11 scanner panel.𝑇𝑖 denotes the number of
household-specific constructed time periods. The restriction𝑇𝑖≤2ensures at least two transitions for identification of one-lag
habit formation. “Purely mechanical” indicates whether the restriction is driven by panel structure rather than missing product
characteristics.
Table 8: Demographic balance: excluded versus final sample
Characteristic Overall N = 2,972 Excluded N = 690 Final Sample N = 2,282 p-value
Family size 0.012
1 550 (19%) 118 (17%) 432 (19%)
2 1,362 (46%) 293 (42%) 1,069 (47%)
3+ 1,060 (36%) 279 (40%) 781 (34%)
Marital status >0.9
Married 307 (10%) 70 (10%) 237 (10%)
Not married 2,658 (90%) 617 (90%) 2,041 (90%)
Region<0.001
Eau Claire 1,597 (54%) 278 (40%) 1,319 (58%)
Pittsfield 1,375 (46%) 412 (60%) 963 (42%)
Children 0.032
Any children 667 (22%) 176 (26%) 491 (22%)
No children 2,305 (78%) 514 (74%) 1,791 (78%)
Occupation0.9
Blue collar/service 1,149 (39%) 267 (39%) 882 (39%)
Office/sales (sales/clerical) 454 (15%) 100 (14%) 354 (16%)
Other/unknown 215 (7.2%) 55 (8.0%) 160 (7.0%)
Retired 254 (8.5%) 62 (9.0%) 192 (8.4%)
White collar (prof/manager) 900 (30%) 206 (30%) 694 (30%)
Education0.8
≤High school 1,737 (61%) 400 (60%) 1,337 (61%)
College+ 203 (7.1%) 46 (6.9%) 157 (7.2%)
Some college/tech 911 (32%) 219 (33%) 692 (32%)
Notes:Counts are n (%). The “Excluded” column reports households removed due to missing UPC
characteristicinformation; allotherpanel-lengthrestrictionsaresatisfiedinbothgroups. p-valuesare
from Pearson chi-squared tests of equality across excluded and retained households.
To assess whether exclusion due to missing characteristics data induces observable selection, Table 8
compares demographic characteristics between the baseline sample—defined as households satisfying all
mechanical feasibility restrictions—and the final analysis sample. Reported p-values correspond to Pearson
chi-squared tests of equality in distributions across groups.
40

Across most dimensions, observable characteristics are similar between excluded and retained house-
holds. Whilesomedifferencesarisealonggeographiclocationandhouseholdcomposition,thesedifferences
are modest in magnitude, and joint tests fail to reject equality across the majority of demographic character-
istics. Overall, the balance results suggest limited scope for selection on observables arising from the final
exclusion.
B.2 Characteristics summary statistics
Tables 9 and 10 report descriptive statistics for the 23 characteristics used in the analysis. Nutritional
attributes are expressed per 100g serving. Calories cluster tightly across products, while carbohydrates and
sugar are generally high and fat content is low. Sodium exhibits substantial cross-product variation. Among
binary attributes, whole-grain indicators and health-related descriptors are common, whereas organic and
gluten-free labels are rare. Brand indicators reflect the dominance of Kellogg’s and General Mills in the
sample.
Table 9: Nutritional characteristics of cereal products (per 100g)
Characteristic units mean sd q1 median q3
calories kcal 379 38 364 379 400
carbohydrates g 81 7 78 82 85
total fat g 4 4 2 3 5
saturated fat g 1 1 0 0 1
fiber g 8 5 3 7 10
protein g 8 3 6 7 10
sodium mg 435 239 277 467 600
sugar g 25 12 18 25 33
Notes:Summary statistics computed across the UPCs in the final sample after excluding two products with missing serving-size
entries. Nutritional values are standardised per 100g serving and rounded to the nearest integer.
Table 10: Binary product characteristics
Characteristic Share (%) Characteristic Share (%)
whole grain 57 honey flavour 15
organic 8 gluten-free 3
oat-based 24 Kellogg’s 18
granola 10 General Mills 13
health halos 33 Post 11
fruity 6 Quaker 7
nutty 11 Kashi 4
chocolatey 5
Notes:Shares denote the percentage of the𝐾=801UPCs in the final sample exhibiting the indicated characteristic. Values are
rounded to the nearest integer.
41

B.3 Purchase intensity, brand concentration, and prices
Figure4ashowsthedistributionofpurchasecountsperhousehold-period. Figure4breportsthedistributions
of average period consumption and expenditure. Figure 4c reports the distribution of the number of distinct
brands purchased per period. Figure 4d plots the distribution of average unit values across UPCs.
Figure 4: Purchase intensity, brand concentration, and prices
(a) Units purchased per household-period
 (b) Average purchasing intensity across households
(c) Distinct brands purchased per household-period
 (d) Average unit values by UPC
Notes:Panel (a) reports a histogram of total cereal units purchased by household𝑖in period𝑡, pooled across all households and
constructed time periods. Panel (b) shows the distributions of household-level averages of units purchased per period and
expenditure per period across the sample. Panel (c) reports a histogram of the number of distinct cereal brands purchased by a
household within a constructed time period. Panel (d) shows the distribution of average unit values (expenditure divided by
quantity) computed at the UPC level over the sample period.
42

References
Afriat,S.N.(1967). TheConstructionofUtilityFunctionsfromExpenditureData.InternationalEconomic
Review, 8(1):67–77.
Afriat, S. N. (1973). On a system of inequalities in demand analysis: An extension of the classical method.
International Economic Review, 14(2):460–472.
Allcott,H.,Gentzkow,M.,andSong,L.(2022).Digitaladdiction.AmericanEconomicReview,112(7):2424–
2463.
Andrews, I. (2026). Revealed rationality: Label-free regularization from representation theorems. First
version: February 21, 2026. Working paper, Department of Economics, MIT and NBER.
Avena,N.M.,Rada,P.,andHoebel,B.G.(2008). Evidenceforsugaraddiction: Behavioralandneurochem-
ical effects of intermittent, excessive sugar intake.Neuroscience & Biobehavioral Reviews, 32(1):20–39.
Bajari, P. and Benkard, C. L. (2005). Demand estimation with heterogeneous consumers and unobserved
product characteristics: A hedonic approach.Journal of Political Economy, 113(6):1239–1276.
Bajari, P. and Kahn, M. E. (2005). Estimating Housing Demand With an Application to Explaining Racial
Segregation in Cities.Journal of Business & Economic Statistics, 23(1):20–33.
Barahona, N., Otero, C., and Otero, S. (2023). Equilibrium effects of food labeling policies.Econometrica,
91(3):839–868.
Becker, G. S., Grossman, M., and Murphy, K. M. (1991). Rational Addiction and the Effect of Price on
Consumption.The American Economic Review, 81(2):237–241.
Becker, G. S., Grossman, M., and Murphy, K. M. (1994). An Empirical Analysis of Cigarette Addiction.
The American Economic Review, 84(3):396–418.
Becker, G. S. and Murphy, K. M. (1988). A Theory of Rational Addiction.Journal of Political Economy,
96(4):675–700.
Berry, S., Levinsohn, J., and Pakes, A. (1995). Automobile Prices in Market Equilibrium.Econometrica,
63(4):841–890.
Blow, L., Browning, M., and Crawford, I. (2008). Revealed preference analysis of characteristics models.
The Review of Economic Studies, 75(2):371–389.
Boyer,M.(1978).AHabitFormingOptimalGrowthModel.InternationalEconomicReview,19(3):585–609.
Boyer, M. (1983). Rational demand and expenditures patterns under habit formation.Journal of Economic
Theory, 31(1):27–53.
Browning,M.(1989).ANonparametricTestoftheLife-CycleRationalExpectionsHypothesis.International
43

Economic Review, 30(4):979–992.
Cocores, J. A. and Gold, M. S. (2009). The Salted Food Addiction Hypothesis may explain overeating and
the obesity epidemic.Medical Hypotheses, 73(6):892–899.
Crawford, I. (2010). Habits Revealed.The Review of Economic Studies, 77(4):1382–1402.
Demuynck, T. and Verriest, E. (2013). I’ll never forget my first cigarette: A revealed preference analysis of
the “habits as durables” model.International Economic Review, 54(2):717–738.
Diewert,W.E.(1973). AfriatandRevealedPreferenceTheory.TheReviewofEconomicStudies,40(3):419.
Dubois,P.,Griffith,R.,andO’Connell,M.(2020). HowWellTargetedAreSodaTaxes?AmericanEconomic
Review, 110(11):3661–3704.
Echenique, F. (2022). On the meaning of the critical cost efficiency index.
Felippa, C. A. (2004).Introduction to finite element methods. University of Colorado.
FreddieMac(2025). 30-yearfixedratemortgageaverageintheunitedstates(mortgage30us). FRED,Federal
Reserve Bank of St. Louis. Retrieved August 16, 2025.
Fudenberg, D., Gao, W., and Liang, A. (2023). How Flexible is that Functional Form? Quantifying the
Restrictiveness of Theories.SSRN Electronic Journal.
Gibbons, S. and Machin, S. (2003). Valuing English primary schools.Journal of Urban Economics,
53(2):197–219.
Gorman, W. M. (1956). A Possible Procedure for Analysing Quality Differentials in the Egg Market.The
Review of Economic Studies, 47(5):843–856.
Greenstone, M. and Gallagher, J. (2008). Does hazardous waste matter? evidence from the housing market
and the superfund program.The Quarterly Journal of Economics, 123(3):951–1003.
Grossman, M., Chaloupka, F. J., and Sirtalan, I. (1998). An Empirical Analysis of Alcohol Addiction:
Results from the Monitoring the Future Panels.Economic Inquiry, 36(1):39–48.
Gruber,J.andKőszegi,B.(2004). Taxincidencewhenindividualsaretime-inconsistent: thecaseofcigarette
excise taxes.Journal of Public Economics, 88(9-10):1959–1987.
Haeck, C., Lawson, N., and Poirier, K. (2022). Estimating consumer preferences for different beverages
using the BLP approach.Economics & Human Biology, 46:101138.
Heckman, J. and Scheinkman, J. (1987). The Importance of Bundling in a Gorman-Lancaster Model of
Earnings.The Review of Economic Studies, 54(2):243–255.
Hendel,I.andNevo,A.(2006). Salesandconsumerinventory.TheRANDJournalofEconomics,37(3):543–
561.
Houthakker, H. S. (1950). Revealed Preference and the Utility Function.Economica, 17(66):159–174.
44

Koob, G. F. and Moal, M. L. (1997). Drug Abuse: Hedonic Homeostatic Dysregulation.Science,
278(5335):52–58.
Le Fur, E. and Outreville, J. F. (2022). The Willingness to Pay for Cider Products: Results of a Survey on
Habits and Consumption Behavior.Wine Business Journal, 5(1).
Nevo, A. (2001). Measuring Market Power in the Ready-to-Eat Cereal Industry.Econometrica, 69(2):307–
342.
Richards, T. J. and Patterson, P. M. (2006). Native American Obesity: An Economic Model of the "Thrifty
Gene" Theory.American Journal of Agricultural Economics, 88(3):542–560.
Rockafellar, R. T. (1970).Convex Analysis, volume 28 ofPrinceton Mathematical Series. Princeton
University Press, Princeton, NJ.
Rosen,S.(1974).HedonicPricesandImplicitMarkets: ProductDifferentiationinPureCompetition.Journal
of Political Economy, 82(1):34–55.
Samuelson, P. A. (1948). Consumption Theory in Terms of Revealed Preference.Economica, 15(60):243–
253.
Selten, R. (1991). Properties of a measure of predictive success.Mathematical Social Sciences, 21(2):153–
167.
Smith, V. K. and Desvousges, W. H. (1986). The Value of Avoiding a Lulu: Hazardous Waste Disposal
Sites.The Review of Economics and Statistics, 68(2):293–299.
Varian, H. R. (1982). The Nonparametric Approach to Demand Analysis.Econometrica, 50(4):945–973.
Varian, H. R. (1990). Goodness-of-fit in optimizing models.Journal of Econometrics, 46(1-2):125–140.
45
