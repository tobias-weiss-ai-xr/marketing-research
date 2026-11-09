---
title: Micro and Macro Perspectives on Production-Based Markups
url: https://arxiv.org/abs/2604.13224
category: consumer-behavior
subcategory: empirical
date: 2026-04
venue: ''
authors:
- John Fernald
- Amit Gandhi
- Dimitrije Ruzic
- James Traina
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.13224
pages: 90
chars: 172615
fetched_at: '2026-11-08T13:00:30+00:00'
kb_version: 1
---

# Micro and Macro Perspectives on Production-Based Markups

Micro and Macro Perspectives
on Production-Based Markups
John Fernald, Amit Gandhi, Dimitrije Ruzic, and James Traina*
April 2026
Abstract
We review the “production approach” to estimating markups, the ra-
tio of price to marginal cost. The approach is uniquely scalable: it re-
quires no model of consumer demand or market structure and applies
broadly across firms, industries, and time. Our organizing insight is that
the production-based markup is a residual. Like the Solow residual, it
is clean in theory but potentially contaminated by misspecification and
mismeasurement. This framing helps explain why small differences in
implementation can produce starkly different results from the same data.
In some cases, markups have risen sharply. In others, they have not. De-
spite the disagreements in the literature, the importance of understand-
ing and measuring market power cannot be overstated. We provide con-
ceptual rationales for this disagreement, offer practical guidance on data
and estimation, and call for greater transparency about how much of the
variation attributed to markups may instead reflect technology.
JEL Codes: D24, D43, E22, E23, L11, L16, O33, O47
*Fernald: john.fernald@insead.edu. Gandhi: amitgandhi@gmail.com. Ruzic: dim-
itrije.ruzic@insead.edu. Traina: james.traina@nyu.edu. We thank Susanto Basu, Arshia
Hashemi, seminar participants at INSEAD, the Federal Reserve Banks of San Francisco and
Richmond, and the University of Arizona, as well as our editor David Romer and several
excellent anonymous referees for helpful comments and feedback.
arXiv:2604.13224v1  [econ.GN]  14 Apr 2026

2
1. Introduction
We review the “production approach” to estimating markups. Intuitively,
markups are about pricing; pricing relates to marginal cost, and marginal cost
reflects the production constraints facing firms. The increased availability of
firm-level microdata and new econometric methods makes it easier to esti-
mate production functions and infer markups. Our review focuses on this
recent firm-level literature, with a goal of bridging micro and macro perspec-
tives. Questions of market power matter for many fields, from industrial or-
ganization (IO) to international trade to macroeconomics. We highlight the
challenges in moving from firm-level analyses to industry and economy-wide
conclusions.
Hall (1986, 1988, 1990) introduced the production approach. He showed
that cost minimization implies the markupµcan be written in a remarkably
simple way as the ratio of a flexible input’s output elasticityγto the cost of
that input as a share of total revenue,s. That is,µ=γ/s. Markups can be
read directly from producer behavior. It is not necessary to specify the de-
mand system or market structure. This makes it attractive compared to typ-
ical methods from IO that are tailored to narrow industries. The production
approach scales to large panels of firms across the economy and over time.
Hall and a large body of work that followed apply his insight to industry
data in growth rates. De Loecker and Warzynski (2012) highlight challenges in
applying Hall’s industry approach to firm-level data. They propose a variant
of Hall’s method that focuses on a single input and uses modern methods for
estimating firm-level production functions. A selling point is that the new
approach allows estimation of firm-by-firm markups.
In recent years, interest in market power has soared. The interest reflects
in part that markups may have risen sharply, and in part that rising markups
might provide a unified explanation for a range of macroeconomic puzzles

3
(De Loecker et al., 2020). These include declining labor shares, rising eco-
nomic profits, slow productivity growth, weak investment, and declining dy-
namism.1
More broadly, modern macroeconomics rests on a foundation of imperfect
competition. In endogenous growth models, firms charge a markup to cover
innovation costs (Romer, 1990). In New Keynesian models, firms are mo-
nopolistically competitive price-setters, not perfectly competitive price-takers
(Rotemberg and Woodford, 1999). Firm-level markup estimates, applied at
scale, allow economists to incorporate rich heterogeneity, strengthening the
microfoundations of macro analysis. IO and trade increasingly need the same
scalability: IO is moving from individual markets to cross-industry patterns
(D¨opper et al., 2025), and trade needs markup estimates across countries and
industries (Feenstra and Weinstein, 2017).
However, the empirical evidence for rising markups is far from settled.
Some production-approach specifications (such as De Loecker et al. 2020)
show dramatic increases in recent decades. But others do not (such as Fos-
ter et al. 2024; Traina 2018; Benkard et al. 2025b).
To put the empirical disagreements in context, our review emphasizes that
production-based markups are a residual. Using the equilibrium first-order
condition for a fully flexible input, the markup absorbs the entire gap be-
tween the output elasticity and the revenue share. Unlike a regression error
or a structural demand shock, this residual is itself the object of interest: an
equilibrium ratio that holds under any model of competition. Three things
can go wrong: wrong first-order condition, wrong output elasticity, or wrong
revenue share. All three deserve scrutiny.
The residual framing is analogous to the Solow (1957) residual. The
1References to these puzzles include, respectively, Elsby et al. (2013), Karabarbounis
and Neiman (2014); Barkai (2020), Karabarbounis and Neiman (2019); Fernald et al. (2024),
Guti´errez and Philippon (2017), Crouzet and Eberly (2019); and Davis et al. (2007). Syverson
(2025) provides a complementary survey covering both markups and markdowns.

4
Solow residual absorbs all output growth not explained by input growth.
Under standard conditions, it is a clean measure of technology change.
But just as a large literature shows that non-technological factors contami-
nate the Solow residual as a measure of technology, 2 (mis)measurement and
(mis)specification can contaminate production-based markups as a measure
of market power. Differences across papers—even those using the same
data—can therefore yield different residuals. Contamination is the price of
scalability: the approach avoids specifying demand or market structure, but
what it omits shows up in the markup.
Even if we resolve all the empirical disagreements, the implications of
market power depend on its cause. The production approach we introduce
in Section 2 is a measurement tool; it is silent on structural drivers. The first-
order condition is an equilibrium relationship. It holds regardless of what
generates the markup, so demand and market structure need not be speci-
fied. But for some questions, we need the structure. For example, are ris-
ing markups “bad,” reflecting barriers to entry, or “good,” reflecting returns
to innovation? Answering that question requires structure that the produc-
tion approach was never designed to provide. The IO literature offers that
structure for narrow markets. The production approach offers breadth. Both
perspectives are needed. We return to these issues at the end of the paper.
Unfortunately, the devil is in the implementation. Implementing the pro-
duction approach requires substantive choices, each of which layers on dif-
ferent auxiliary assumptions. The “garden of forking paths” (Borges, 1941;
Gelman and Loken, 2014) in Section 3 documents the sensitivity across two
(of multiple) such choices. One is which input to treat as flexible, usually la-
bor or materials. Another is how much variation to allow in output elasticities
2Non-technological factors in the Solow residual include markups (Hall, 1986, 1988, 1990),
factor utilization (Basu et al., 2006; Fernald, 2014), aggregation (Basu and Fernald, 1997;
Baqaee and Farhi, 2020), and mismeasurement (Corrado et al., 2009; Byrne et al., 2016).

5
across firms and over time. Several studies use the same data and estimation
techniques to show these choices matter. The results are stark. Some specifi-
cations imply sharply rising markups; others do not.
The remainder of the review examines what we know about the sources of
this sensitivity.
Section 4 asks whether the source of empirical disagreements is concep-
tual. The first-order condition may be missing wedges that contaminate the
markup estimate, including adjustment costs, monopsony power, or bargain-
ing frictions that drive a gap between observed input prices and the alloca-
tive costs to which firms actually respond. The production function may also
allow too little variation in output elasticities, forcing genuine technological
heterogeneity into the markup residual instead. A recurring theme is the ten-
sion between markups and technology: assumptions that restrict elasticity
variation load that variation onto the markup. A related conceptual fork, also
taken up in Section 4, is the choice between gross-output and value-added
production functions. With markups, both the theoretical and the empirical
case for value-added production functions is weak (Basu and Fernald, 1995;
Gandhi et al., 2017; Ruzic, 2024).
Sections 5 and 6 examine the interplay of data and estimation that re-
searchers implementing the production approach need to understand. Section
5 focuses on the data constraint: missing inputs, misclassification of variable
and fixed costs, and limited sample coverage can all distort revenue shares or
bias estimated elasticities. Section 6 examines the econometric challenge of re-
covering output elasticities when inputs respond to unobserved productivity
and prices. Estimation in this setting is harder than often recognized because
the standard toolkit was largely built for perfect competition and better data
than what we typically have.
Despite these challenges, the importance of understanding and measuring
market power cannot be overstated. Markups shape resource allocation, wel-

6
fare, and how shocks propagate across firms and industries—and no other
method estimates them at comparable scale. The difficulty of the measure-
ment problem is not a reason to set the production approach aside, but a rea-
son to invest in improving it.
Therefore, Section 7 closes with three calls to arms, all centered on the ten-
sion between market power and technology. First, we call for transparency:
systematic reporting of how much revenue-share variation is explained by
markups versus output elasticities. Second, we call for testing: comparing
production-based markups against demand-based estimates from IO, quasi-
experimental evidence, and simulations. Third, we call for more work map-
ping firm-level markup and technological heterogeneity into macroeconomic
models. Getting the implementation right matters precisely because the ap-
proach is so broadly applicable.
We now turn to laying out the production approach at the heart of this
review.
2. The production approach to markup estimation
Production functions and markups are inextricably linked through factor de-
mand. Intuitively, firms with market power raise prices and reduce out-
put, which in turn leads them to use fewer inputs. Hall (1986, 1988, 1990)
showed how to use this insight to estimate markups assuming little other
than cost minimization. The rest of the firm’s profit maximization problem is
not needed.
The first four subsections present the main conceptual material. Subsec-
tion 2.1 presents the key cost-minimizing first-order condition (FOC). Subsec-
tion 2.2 describes how Hall and others implemented this approach using data
in growth rates, emphasizing three lessons that remain relevant for the newer
microdata literature. Subsection 2.3 introduces that newer literature, which

7
applies the FOC to a single input and usually estimates production relation-
ships in levels. Subsection 2.4 previews the key conceptual choices that drive
the empirical disagreements documented in the rest of the review.
2.1 The unifying first-order condition
Consider a production function for firmiin periodt:
Yit =F(X 1 it, . . . , XN it , Ait),(1)
whereY it is gross output,X 1 it, . . . , XN it are inputs, andA it denotes productivity.
The firm seeks to minimize the cost of producing any value of gross output
¯Yit. An input is fully flexible if it is chosen in the current period and affects
only current-period costs. LetVdenote the set of fully flexible inputs. All
other inputs are taken as predetermined. The firm takes input pricesW j it as
given. The cost-minimization problem is:
min
{X j it}j∈V
NX
j=1
W j itX j it
s.t. ¯Yit =F(X 1 it, . . . , XN it , Ait).
(2)
The cost-minimizing first-order condition (FOC) for optimal input demand is:
W j it =λ it ∂F ∂X j it ,(3)
where the Lagrange multiplierλ it is the firm’s marginal cost: the shadow
value of relaxing the production constraint by one unit. The same marginal
costλ it enters the FOC for any input the firm can freely adjust. To interpret
this condition, we define three terms:
•µ it ≡ Pit λit is the firm’s markup of output priceP it over marginal cost,

8
•γ j it ≡ ∂F ∂X j it X j it Yit is the elasticity of output with respect to inputX j it, and
•s j it ≡ W j itX j it PitYit is the factor’s share in revenue.
With these definitions, the FOC implies the key relationship at the heart of the
production approach:
γj it =µ it sj it.(4)
For any input, market power (µ it >1) implies that the output elasticityγ j it
exceeds its revenue shares j it. The markup is a property of the firm, so the
sameµ it enters the FOC for every input. Hence, any flexible input can, in
principle, be used to identify the markup.3
Throughout, we typically work with a special case of (1) that separates
inputs into capitalK it, laborL it, and intermediate inputsM it:
Yit =F(K it, Lit, Mit, Ait).(5)
For a multi-product firm,Y it is an index over outputs; each input is an index
over heterogeneous types. A flexible inputX it ∈ {Kit, Lit, Mit}satisfies FOC
(4). We next trace out how Hall and others implemented this approach us-
ing data in growth rates. We then turn to its more recent implementation in
microdata, which focuses on a single input and, where necessary, estimates
production relationships in levels.
3Section 4.1 discusses what happens when inputs face frictions beyond the static cost min-
imization problem (2). For instance, some inputs such as capital may face adjustment costs;
others may be subject to input-market power `a la Robinson (1933). In such cases, the FOC
acquires additional terms relative to (4) because the input priceW j it is not taken as given. In
principle, one can still estimate markups from such inputs by modeling and measuring the
additional frictions.

9
2.2 The production approach in growth rates
In a series of papers, Hall (1986, 1988, 1990) pioneered the production ap-
proach by applying FOC (4) to all inputs simultaneously. His motivation was
that when output rises in a boom for reasons beyond a firm’s own productiv-
ity, the gap between output growth and input growth reveals the markup. As
Hall (1986, p. 285) writes,
Macroeconomic fluctuations reveal a good deal about market structure.
Students of industrial organization have not generally exploited cyclical
movements in their research; they have concentrated almost entirely on
cross-sectional analysis.
In implementing this idea, Hall followed Solow (1957) and log-
differentiated the production function (5). Substituting the output elasticities
γj it in the resulting expression for the revenue sharess j it and the markupµ it
using FOC (4) yields the “Hall equation”:
∆yit =µ it

sK it ∆kit +s L it∆lit +s M it ∆mit  + ∆ait ≡µ it ∆xit + ∆ait,(6)
where lowercase letters denote logs,∆x j it ≡∆ logX j it, and∆x it is revenue-
share-weighted input growth.4 Appropriately estimated, the relationship be-
tween input and output growth reveals the markupµ it. Because the Hall
equation applies FOC (4) to all inputs, the approach must grapple with inputs
such as capital that may not be fully flexible. Basu and Fernald (2001) and
Basu et al. (2001) generalize the cost-minimization problem (2) to account for
dynamic inputs and survey the literature that estimates variants of the Hall
equation with industry data. Estimation typically assumes a time-invariant
markup.
4Hall (1990), equation 5.29. Factor-specific technology growth is subsumed into∆a it by
normalizing the elasticity of output with respect to technology,∂logF/∂logA it, to one. Sec-
tion 4.2 discusses non-factor-neutral technology. Classic growth accounting (Solow, 1957;
Jorgenson and Griliches, 1967) imposesµ it = 1. Ifµ it >1, the Solow residual equals
(µit −1)∆x it + ∆ait and varies systematically with input growth.

10
Most estimates using industry data find gross-output markups on the or-
der of 3 to 6 percent (for example, Basu and Fernald, 1997). Ahmad et al. (2026)
update the growth-rate approach with industry data from 1949 through 2016
and find markups remain modest. These results are at odds with many recent
firm-level findings. Some differences could arise from using industry rather
than firm data. However, De Loecker and Warzynski (2012) use firm-level
data and also find relatively modest markups using the Hall growth-rate ap-
proach; they find larger ones using their preferred implementation method,
which is discussed in Section 2.3 and the remainder of the paper.
In addition to estimates of markups, the Hall literature provides three
lessons that will return regularly in the remainder of this paper.
First, one wants robustness to the functional form of the production func-
tion (1) or (5). Because (6) is derived by log-differentiating the production
function, in principle it provides a local approximation valid for any pro-
duction function. There is no need to choose a specific functional form. The
functional-form robustness is slightly attenuated by the econometric need to
have a time-invariant markup parameter, so it is perhaps best considered a
first-order approximation to any production function.
Second, markups are not the same as pure economic profits. For exam-
ple, a firm might charge a markup to cover fixed or overhead costs. The
degree of returns to scale (RTS),γ it, is the ratio of average cost to marginal
cost:γ it =AC it/MCit (Varian 1984, p. 68; Syverson, 2025). The firm earns
pure economic profitsΠ it if revenues (P iYi) exceed the cost of production
(Costit = P j W j itX j it). Let the rate of pure economic profit in revenue bes Πit.
Using insights from Hall (1990), Basu and Fernald (1997) derive a useful rela-
tionship between markups, returns to scale, and the profit rate:
γit
µit
= 1−s Πit.(7)

11
The ratio of returns to scale to the markup equals one minus the profit
share.5 Economic profits arise when markups exceed the degree of returns-
to-scale, that is, whenµ it > γit. For example, increasing returns (γ it >1)
could arise from fixed or overhead costs that raise average but not marginal
costs. The firm can charge a markup simply to cover those fixed or overhead
costs, with no pure profit left over. This distinction matters for interpreting
production-based markup estimates: high measured markups need not imply
high profits, and rising profit shares need not imply rising markups.
Third, because of equation (7), the production-approach literature follow-
ing Hall (1990) gave equal weight to markups and returns to scale. Macro
modeling that assumed imperfect competition also typically assumed increas-
ing returns in the form of fixed costs to keep profit rates from being too large
(Rotemberg and Woodford, 1999). The newer literature, by contrast, typically
estimates markups while treating returns to scale and output elasticities as
nuisance parameters.
All three lessons remain relevant as we interpret the new literature.
Most of the literature following the Hall growth-rate approach uses indus-
try data. A few papers, however, use firm microdata. These include Klette
(1999) and Dobbelaere and Mairesse (2013). Klette (1999) uses a panel of Nor-
wegian establishments. Rather than taking growth rates over time, Klette
takes a local approximation in the cross-section in order to flexibly approx-
imate any functional form.
5Section 4.1 discusses refinements in the presence of adjustment costs or input-market
power such as monopsony. The equation holds with adjustment costs as long as dynamic
factors such as capital are priced at their appropriate shadow costs. Monopsony power re-
quires an extra term, since profits can arise from input-price markdowns as well as from
output-market markups.

12
2.3 The new literature on production-based markups
The production approach to markup estimation has expanded rapidly with
the increasing availability of firm microdata. The new literature typically
implements Hall’s insights about production-based markups differently than
Hall and the literature discussed in the previous subsection. The new litera-
ture uses firm or establishment data, focuses on a single fully flexible input,
and (typically) estimates production functions in levels. This review focuses
on one important modern implementation of the production approach: the
firm-level, single-input, levels-based framework that builds primarily on De
Loecker and Warzynski (2012).
De Loecker (2011b) and De Loecker and Warzynski (2012) argue that the
growth-rate approach is poorly suited to microdata: first-differencing exac-
erbates measurement error in short panels (Griliches and Mairesse, 1998); in
addition, the types of aggregate demand instruments used in the growth-rate
literature have low power with limited firm-level cross-sectional variation.
(Of course, as Section 6 discusses, not all econometric methods to address
endogeneity concerns use instrumental variables.) In addition, the Hall ap-
proach assumes that markups are constant over time; the variants used by
Klette (1999) and Dobbelaere and Mairesse (2013) impose that the markups
are the same for all firms in an industry. De Loecker and Warzynski (2012)
emphasize that they are particularly focused on estimating markups at a firm-
by-firm level.
De Loecker and Warzynski (2012) outline how focusing on a single input—
rather than a weighted bundle of inputs as in the Hall approach—can help
overcome these shortcomings. The approach has three steps:
• correctly select a flexible inputX j it,
• measure its revenue sharebsj it, and

13
• specify a production function and estimate the output elasticitybγj it.
The markup then follows directly from FOC (4):bµit =bγj it/bsj it.
The first two steps are linked. We need a fully flexible input so that the
input’s revenue share can potentially be observed in the data at the relevant
market price. For quasi-fixed inputs such as capital—chosen in a prior period
or subject to adjustment costs—the revenue share depends on an unobserv-
able shadow price, making it more difficult to recover the allocative cost the
FOC requires.
For the third step, estimating the production function generally requires
including all inputs to avoid omitted-variable bias, even though only one in-
put’s elasticity is needed for the markup. Consider a Cobb-Douglas produc-
tion function in capital, labor, and materials:
yit =γ Kkit +γ Llit +γ M mit +a it.(8)
For example, omitting capital—even if it is not the input used to measure the
markup—leads to omitted-variable bias. Firms that use more capital also tend
to use more labor and materials, so the omission will load on their coefficients.
An important question in the third step is how flexibly to model the pro-
duction technology. The choice of functional form determines how many de-
grees of freedom output elasticities have to explain revenue shares. The Cobb-
Douglas function (8) is the simplest choice, but it restricts output elasticities
to be common across firms and time. Researchers can relax this by allowing
elasticities to vary across time or industries, or by moving to a more flexible
functional form altogether. A translog production function adds squared and
cross terms in the inputs, giving it more flexibility: as a second-order approx-
imation to any arbitrary production technology, it lets elasticities vary with
input intensity.6
6With two inputs, the baseline translog with Hicks-neutral technology isyit =α 0+αKkit+

14
Researchers can also relax assumptions on productivity. One such general-
ization allows for input-augmenting technical change, where productivity has
both a Hicks-neutral componentA H it and, say, a labor-augmenting component
AL it. The production function then becomesY it =A H it F(K it, AL itLit, Mit), which
in constant elasticity of substitution (CES) form is:
Yit =A H it
h
(1−α l −α m)K
σ−1
σ
it +α l

AL itLit  σ−1 σ +α mM σ−1 σ it i σ σ−1 .(9)
With this technology, output elasticities depend on both input intensity and
the input-augmenting productivity. We return to this choice and its conse-
quences in the next sections.
The production approach is broadly applicable precisely because it rests
on cost minimization rather than a specific model of demand or competition.
Demand-side approaches, such as Berry et al. (1995), require detailed product-
level data, an explicit model of consumer demand, and assumptions about
strategic interaction and firm conduct. Such approaches can be highly infor-
mative within a narrowly defined industry but require extensive customiza-
tion for each setting. Cost minimization, by contrast, is a more general prin-
ciple: regardless of how complex or dynamic the profit-maximization prob-
lem may be, firms typically aim to produce at the lowest possible cost. This
breadth makes the production approach attractive for cross-industry and ag-
gregate analysis. It comes, however, at a cost.
The production-based markup is measured as a residual: it takes what-
ever value makes FOC (4) hold given the observed revenue share and
the estimated elasticity. This framing has an important implication. Any
misspecification—of the FOC itself, of the production function, or of the
econometric method used to estimate it—gets absorbed into the estimated
αLlit + 1 2 βKK (kit)2 +β KL kitlit + 1 2 βLL(lit)2 +a it. The output elasticity for labor is then
γL it =α L +β KL kit +β LLlit, which varies across firms with their input intensity.

15
markup. So does any mismeasurement of the revenue share. The markup is,
in this sense, the residual claimant of the production approach: it ensures the
identity holds, absorbing whatever the estimation does not pin down. This is
both the approach’s strength—it requires minimal assumptions—and its cen-
tral vulnerability, which the rest of this review unpacks.
2.4 Key conceptual choices in implementation
In principle, the method of implementing the production approach laid out
in Section 2.3 is simple: choose a flexible input, measure its revenue share,
estimate its output elasticity, and compute the ratio. In practice, each step
involves choices that can substantially affect the estimated markups. Which
choices create the most sensitivity? We begin with three conceptual issues.
Which input to use.FOC (4) implies any flexible input should yield the
same markup. In practice, markups estimated from different inputs often
diverge sharply—in both levels and trends. Section 3 documents these di-
vergences using direct comparisons across inputs within the same datasets.
Section 4.1 explains why they might arise.
How flexibly to model output elasticities.Having chosen an input, the
researcher must specify a production function and estimate its output elastic-
ity. A Cobb-Douglas function restricts elasticities to be common across firms;
a translog or CES function allows them to vary with input intensity. When
the assumed functional form is too restrictive, genuine variation in technol-
ogy gets forced into the markup residual—making measured markups rise or
fall even when true market power is unchanged. Section 3 documents how
sensitive markup trends are to this choice. Section 4.2 discusses the resulting
bias.
Value added versus gross output.Macroeconomists often want a “value-
added markup” because GDP aggregates value added across producers. But

16
value-added and gross-output markups are conceptually distinct and cannot
be used interchangeably in calibrating macro models. A separate issue is esti-
mation. Basu and Fernald (1995) show that markups invalidate value added
as a production measure except under the Leontief assumption that interme-
diates enter in fixed proportion to gross output—an assumption with little
empirical support. Section 4.3 takes up both issues in detail.
Despite these choices—and the sensitivity to them documented through-
out this review—the production approach remains the most broadly appli-
cable tool available for measuring firm-level markups across industries and
countries. That is precisely why getting the choices right, and being transpar-
ent about them, matters so much.
3. The garden of forking paths
Existing empirical evidence suggests that the main implementation choices
have stark implications for the measurement of markups. What seems like a
clean, mechanical implementation quickly gives way to a garden of forking
paths.
This section highlights two important forks in that garden: (1) which input
to use, and (2) how flexibly to specify technology. These are not the only forks,
but they are particularly well documented: Each has been studied empirically
using variants of the same data, and each has been shown to materially affect
the estimated markups. Later sections explore additional forks, including the
specification of the first-order condition (Section 4), data construction (Sec-
tion 5), and econometric method (Section 6).
We present empirical evidence on these two forks, using studies that offer
direct comparisons across choices within the same dataset. We defer most
interpretation to Section 4. A recurring finding is uncertainty about markup
levels and trends: it is easy to find plausible specifications in which markups

17
are relatively constant.
3.1 First fork: Which input to use?
Any fully flexible input that satisfies the conditions in the cost-minimization
problem (2) should yield the same markup. In practice, markup estimates
based on different inputs often diverge in both levels and trends; and, the di-
vergences are far too large to dismiss as sampling error. We highlight this fork
because, in many applications of the production approach, the input choice is
unexamined: researchers simply assert that a given input is flexible.
Table 1a presents results from three papers that compare markup estimates
across inputs using the same dataset. The differences are stark, and they lead
to opposite conclusions about the direction and magnitude of changes in mar-
ket power.
Table 1a: Garden of Forking Paths
First Fork: which input to use for the production approach?
Production-Based Markups using Different Inputs
Raval (2023)Labor Materials
U.S. (1970–2010) Increase of 90% Decrease of 50%
Chile (1978–1996) Decrease of 20% Increase of 15%
Colombia (1978–1996) Decrease of 30% Increase of 10%
India (1998–2014) Decrease of 40% No change
Indonesia (1991–2000) Decrease of 10% Increase of 5%
Doraszelski & Jaumandreu (2019)
Labor Materials
Spain (1990-2012) Exporters charge higher markups Exporters charge smaller markups
Raval (2023)Energy Non-Energy (Raw) Materials
Chile (1978–1996) Increase of 20% Increase of 15%
Colombia (1978–1996) Decrease of 70% Increase of 20%
India (1998–2014) Decrease of 25% Increase of 5%
Indonesia (1991–2000) Increase of 40% Decrease of 5%
Traina (2018)Cost of Goods Sold Operating Expenses
Compustat, 1950–2016 Increase: 1.19 to 1.45 Increase: 1.15 to 1.17
Sources: Figures 2 and 5 from Raval (2023), Table 1 from Doraszelski & Jaumandreu (2019), and Figure 2 from
Traina (2018). Raval and Doraszelski & Jaumandreu entries report approximate percentage changes in average
markups, rounded to nearest 5 percent. Traina entries report markup levels.
The input choice can reverse the sign of markup trends entirely. Raval

18
(2023) uses manufacturing census data from five countries to show labor- and
materials-based markup estimates diverge far beyond what sampling error
could explain, implying at least one set of identifying assumptions is wrong.
In the United States, labor-based markups nearly double between 1970 and
2010, while materials-based markups fall by half. In Chile and Colombia,
labor-based markups fall while materials-based markups rise. Within all five
countries, labor and materials markups are negatively correlated across firms,
in both levels and trends. These patterns persist across specifications and
estimation methods.
The input choice also shapes cross-sectional comparisons, not just trends.
Doraszelski and Jaumandreu (2019) compare exporters and non-exporters in
Spain and find the conclusion about which group charges higher markups
flips depending on the input used. Exporters appear to charge higher
markups when labor is used, but lower markups when materials are used
instead.
Even within a single broad input category, the choice of subset matters.
The middle panel of Table 1a shows additional results from Raval (2023) com-
paring energy and non-energy materials. In Colombia, markups based on
energy fall 70% while markups based on non-energy materials rise 20%. In
India and Indonesia, the markup trends switch signs entirely. These patterns
matter because input flexibility is often assumed rather than demonstrated:
implementations of the production approach frequently use materials on the
asserted grounds that they are more flexible than labor, yet even within mate-
rials, markup estimates diverge sharply across subsets.
The same sensitivity appears in financial data. Studies using Compustat—
the most widely used dataset for broad-coverage markup estimation—must
choose between Cost of Goods Sold (COGS), which covers direct produc-
tion costs, and Operating Expenses (OPEX), which adds Selling, General, and
Administrative expenses (SG&A) such as marketing, executive salaries, and

19
R&D. Traina (2018) finds this choice is decisive. Using COGS alone implies
markups rose from 1.19 to 1.45 between 1950 and 2016, a 26 percentage point
increase. Using OPEX, which includes SG&A, implies markups rose from 1.15
to 1.17, an increase of just 2 percentage points. Including SG&A wipes out
most of the rise. This sensitivity has both a measurement and an economet-
ric interpretation. From a measurement perspective, SG&A may simply be a
variable cost that belongs in the revenue-share denominator. From an econo-
metric perspective, even if SG&A is quasi-fixed, omitting it from the produc-
tion function biases the estimated elasticity of the included input upward, just
as omitting capital does. We develop these interpretations in Section 5.
Benkard et al. (2025b) document a related concern: De Loecker et al.
(2020)’s replication code drops all observations with missing SG&A—27%
of the sample—even though SG&A is not used in their markup calculation.
Firms with missing SG&A systematically have higher COGS ratios and lower
measured markups, creating trended upward selection bias. Both findings
implicate SG&A in the measured markup increase, though through different
mechanisms: input measurement in Traina (2018) and sample construction in
Benkard et al. (2025b). The interpretation remains contested. De Loecker and
Eeckhout (2025) reply and defend their original sample selection; Benkard et
al. (2025a) reply to the reply.
The choice of input shapes substantive conclusions about markups. While
the logic of the production approach implies any flexible input should yield
the same markup, different inputs—whether labor, materials, energy, or ac-
counting aggregates—often imply divergent and even contradictory trends.
Nearly every input is subject to some friction that can drive a wedge between
the observed price and the allocative shadow price the FOC requires. If fric-
tionless input markets are the exception rather than the rule, the divergence
across inputs in Table 1a is what we might naturally expect.

20
3.2 Second fork: How flexibly to model output elasticities?
Having chosen a flexible input, the researcher must decide how to estimate its
output elasticity. This choice determines how many degrees of freedom out-
put elasticities have to explain variation in revenue shares, and therefore how
much of that variation gets attributed to technology versus to the markup
residual. When the assumed functional form is too restrictive, genuine vari-
ation in output elasticities gets forced into estimated markups, making them
appear to rise or fall even when true market power is unchanged.
Table 1b documents the consequences of different elasticity estimation
strategies in three studies that apply multiple approaches to the same data.
Table 1b: Garden of Forking Paths
Second Fork: how to estimate the output elasticity for a given input?
De Loecker, Eeckhout & Unger (2020)
Compustat, 1980-2016
Cost Share Cobb-Douglas Overhead
Increase: 1.29 to 1.73 Increase: 1.21 to 1.61 Increase: 0.98 to 1.32
Foster, Haltiwanger & T uttle (2024)
U.S. Manuf., 1977-2012
Cost Share Cobb-Douglas Translog
4-digit industry Increase: 1.25 to 1.50 Stable: 1.25 to 1.25 Decrease: 1.00 to 0.99
2-digit industry Increase: 1.40 to 1.80 Increase: 1.35 to 1.48 Increase: 1.30 to 1.60
Demirer (2025)Cobb-Douglas Labor-augmenting
US (1961–2018) Increase: 1.30 to 1.50 Increase: 1.25 to 1.30
Chile (1979–1996) Increase: 1.35 to 1.40 Decrease: 1.26 to 1.22
Colombia (1978–1991) Stable: 1.40 to 1.40 Decrease: 1.30 to 1.28
India (1998–2014) Stable: 1.31 to 1.31 Increase: 1.20 to 1.29
Turkey (1983–2000) Increase: 1.25 to 1.31 Decrease: 1.20 to 1.10
Sources: Figures 7A, 1 and 8A from De Loecker, Eeckhout & Unger (2020), Figures 2 and 3 from Foster, Halti-
wanger & Tuttle (2024), and Figures 6 and OA-5 from Demirer (2025). Entries report the direction and approxi-
mate markup levels at the start and end of each sample period. De Loecker, Eeckhout & Unger (2020) use cost
of goods sold as the flexible input. Foster, Haltiwanger & Tuttle (2024) use materials. Demirer (2025) uses the
combination of labor and materials.
One way to forego more elaborate estimation and specification of technol-
ogy is to proxy output elasticities with shares of payments to each factor in
total costs. As Section 4.2 discusses, under the assumption of constant RTS
and competitive input markets, these cost shares equal output elasticities; no
additional estimation required. De Loecker et al. (2020) implement a version

21
of this by fixing the output elasticity at its historical average cost share across
firms, applying the same value to every firm in a given industry and period.
They find this yields markup trends broadly similar to their Cobb-Douglas
benchmark—markups rising from around 1.29 to 1.73 under cost shares, com-
pared to 1.21 to 1.61 under Cobb-Douglas—suggesting the upward trend is
not merely an artifact of the estimated elasticity rising over time. Even when
they extend the production function to include a fixed (overhead) input, the
upward trend in markups remains.7
That similarity between their cost-share and Cobb-Douglas estimates is re-
vealing: the estimated output elasticity is not doing much independent work
across the two specifications. But it also reflects the fact that using an average
cost share gives output elasticities essentially no additional degrees of free-
dom to explain cross-firm variation in revenue shares relative to Cobb Dou-
glas. An alternative, which we discuss in Section 4.2, is to estimate a separate
output elasticity for each firm and period; this alternative gives elasticities
more room to explain the data before the markup residual absorbs what re-
mains. Cost-share proxies carry their own assumptions, and the choice be-
tween them and more elaborate elasticity estimates is itself a fork in the gar-
den.
Even within a single functional form, the level of industry aggregation at
which elasticities are estimated can reverse markup trends entirely. Foster et
al. (2024) use U.S. Census of Manufacturing plant data from 1977 to 2012, with
materials as the flexible input. Under Cobb-Douglas at the 2-digit industry
level, markups rise from 1.35 to 1.48. At the 4-digit level, they are stable at 1.25
7This specification, which they call PF2, includes SG&A as a productive input along with
COGS and capital. It is similar to the Traina (2018) OPEX specification from Table 1a, except
that they do not combine COGS and SG&A. Unlike Traina, they still find a sharply rising
markup. The PF2 specification and the associated profit analysis were added in the published
version; the earlier working paper used COGS as the sole variable input without discussing
overhead as a potential production input.

22
throughout.8 The mechanism is simple: coarser industry groupings restrict
how much output elasticities can vary across firms, forcing more cross-firm
technological heterogeneity into the residual claimant of FOC (4), the markup.
Moving to a more flexible functional form changes the picture further, and
its effect interacts with the aggregation level. Under translog at the 4-digit
level, Foster et al. (2024) find markups decline slightly (1.00 to 0.99)—where
Cobb-Douglas showed stability and cost shares showed a rise. At the 2-digit
level, translog produces a larger rise (1.30 to 1.60) than Cobb-Douglas. The
underlying plant-level revenue shares are identical across all specifications:
any divergence reflects how different estimation choices assign variation be-
tween output elasticities and markups through FOC (4), not differences in the
data.
Assumptions about the nature of productivity matter as much as func-
tional form. Demirer (2025) finds that moving beyond Hicks-neutral produc-
tivity to incorporate labor-augmenting productivity reverses markup trends
in multiple countries. In U.S. manufacturing, Cobb-Douglas with Hicks-
neutral technology implies markups rose from 1.30 to 1.50 between 1961 and
2018; labor-augmenting CES implies a much more modest increase from 1.25
to 1.30. In Chile and Turkey the trends flip sign: rising under Cobb-Douglas
but falling under labor-augmenting CES. The rationale, developed further in
Section 4.2, is that labor-augmenting productivity gives output elasticities an
additional degree of freedom to explain changes in relative factor costs, leav-
ing less variation in input sharesbsj it to load onto the markup.
In sum, the choice of technology specification shapes substantive conclu-
sions about markups just as much as the choice of input does. The logic of the
production approach implies that output elasticities should absorb genuine
8Industry-level aggregates such as KLEMS data do exist but average over the firm hetero-
geneity that drives markup dispersion; the production approach’s value is precisely that it
recovers firm-level markups. The Foster et al. (2024) results underscore the point: 2-digit and
4-digit industry aggregation yield different markup trends from identical plant-level data.

23
technological variation. But restrictive functional forms, industry aggrega-
tion, or assumptions about the nature of technological progress can all limit
how much variation in revenue shares gets attributed to technology rather
than to the markup. When the specification restricts how output elasticities
can vary, the variation that elasticities cannot absorb gets loaded onto the
markup instead.
4. Conceptual rationales for the garden
This section highlights two theoretical hypotheses that can help reconcile the
discrepancies from the garden of forking paths: (1) the central first-order con-
dition could be missing non-markup frictions and (2) the estimated produc-
tion technology could be insufficiently flexible. These two hypotheses can, in
principle, generate the observed empirical divergences, and they both have
support in the literature. They are not the only hypotheses, since there could
also be non-conceptual sources of bias arising from inadequacies in the data
(Section 5) or econometric issues in estimating output elasticities (Section 6).
4.1 Do we have the right first-order condition?
The key FOC (4) assumes a static cost-minimization problem in which the firm
takes input prices as given. When these assumptions fail, the effective cost of
an input to the firm, that is, the price that actually governs its hiring decision,
differs from the observed market price. This gap introduces an unobserved
wedgeτ j it between the output elasticityγ j it and the revenue shares j it:9
γj it =µ itsj it  1 +τ j it  . (10)
9We follow Doraszelski and Jaumandreu (2019) in writing all deviations from FOC (4) in
this form.

24
Suppose we ignore the wedge. Even with correct values forγ j it ands j it, the
production approach recoversµ it(1 +τ j it), not the true markupµ it. Suppose
also that different inputs face different wedges. They will then yield different
markups—the pattern in Table 1a.
A fundamental implication of (10) is that a single FOC cannot separately
identify two unknowns. Observed revenue sharess j it reflect both the true
markupµ it and the wedgeτ j it, but the FOC alone cannot tell us how much
revenue-share variation is due to one versus the other. Since heterogeneous
markups are themselves a form of distortion, they could in principle be folded
into the broader category of wedges. But not all wedges are markups, and
conflating the two leads to misinterpretation. Separately identifying markups
from other wedges determines whether we are measuring market power or
something else entirely.
Separate identification requires bringing in additional modeling assump-
tions, and typically additional data. The choice of what to assume determines
what gets identified. In quantifying misallocation, Restuccia and Roger-
son (2008) and Hsieh and Klenow (2009) impose structure on markups—
assuming common output elasticitiesγ j t within industries and a common de-
mand elasticity that pins down the markup, so that all firm-specific variation
in revenue shares is absorbed by exogenous distortion wedges(1 +τ j it).10 De
Loecker and Warzynski (2012) take the opposite approach: they impose struc-
ture on the wedges (by effectively assuming they are common across firms),
which allows all variation in revenue shares to be attributed to markups. Both
approaches achieve identification, but by assumption rather than by data. A
third path is to render either markups or wedges, or both, a function of ob-
servables. Choi et al. (2024), for instance, use a demand model to quantify
10Restuccia and Rogerson (2017) survey the misallocation literature; see also Haltiwanger
et al. (2018) on measurement. Peters (2020); Edmond et al. (2023); Baqaee and Farhi (2020);
Baqaee et al. (2024) discuss heterogeneous markups as a source of misallocation.

25
markups and then use the residual variation in revenue shares to identify
input-market wedges.
These wedges can arise for three distinct reasons, each discussed in turn
below.
The first source of wedges arises when observed input prices are not
the allocative prices that govern firms’ optimization. Even in a static
setting, government-induced frictions—tariffs, taxes, quotas, or size-based
regulations—can drive a gap between the price a firm pays and the shadow
cost it responds to. A specific form of this wedge is input-market power
(Robinson, 1933). Concretely, suppose the firm is a monopsonist in the la-
bor market. It faces upward-sloping labor supply: it must pay a higher wage
to hire more. The firm then acts as if the wage wereW j it(1 +ϵ j it), whereϵ j it is
the elasticity of the input price with respect to quantity hired. The result is a
“markdown” of the observed wage relative to the marginal revenue product.
Production-based markup estimates will conflate that markdown wedge with
markupµ it. Following Dobbelaere and Mairesse (2013), several papers use
the divergence of markup estimates across inputs to quantify input-market
power, treating the gap betweenˆµL it andˆµM it as informative about the mark-
down rather than as a nuisance.11
The second source of wedges arises when the cost-minimization problem
is inherently dynamic, yet the researcher imposes a static framework. Cap-
ital is the classic case: today’s investment affects future production costs, so
the relevant shadow price of capital incorporates adjustment costs and future
expectations, not just today’s rental rate. As Basu and Fernald (2002) and Do-
raszelski and Jaumandreu (2019) show, the resulting shadow price can still be
written asW j it(1 +τ j it), whereτ j it depends on stocks, flows, and expectations,
11Studies of labor-market power have a long history (such as Manning, 2003). In addition
to Dobbelaere and Mairesse (2013), recent examples include Berger et al. (2022); Yeh et al.
(2022); Jarosch et al. (2024); Kirov and Traina (2022); Rubens (2023).

26
so the factor-demand equation retains the form of (10).12 Adjustment costs are
not limited to capital, nor are they inherently inefficient (Asker et al., 2014).
Cooper et al. (2024) find labor adjustment costs are important and rising in
U.S. manufacturing; ignoring them and treating labor as fully flexible gener-
ates what they estimate as substantial and rising dispersion in production-
based markups despite there being no variation in actual markups. Even
materials and other intermediate inputs may face dynamic frictions through
supply-chain relationships and delivery lags (Liu and Tsyvinski, 2024; Dhyne
et al., 2022; Acemoglu and Tahbaz-Salehi, 2025).
A related concern is that observed wages may not equal the allocative
shadow cost even if the firm minimizes costs and there are no adjustment
costs or input-market frictions. Most employment relationships are long-
term. Hall (1980) argues wages should be understood as installment pay-
ments on a firm’s long-term obligation to its workers, not as spot prices
that reflect the current marginal value of labor. If so, the observed wage at
any point in time can differ substantially from the shadow cost that governs
the firm’s current hiring decision (Basu and House, 2016; Kudlyak, 2024).
Similar issues can arise in firm-to-firm transactions governed by relational
contracts, where observed transfer prices may reflect long-term relationship
value rather than current marginal cost.13 In both cases, using observed prices
in place of allocative shadow costs introduces a time-varying wedgeτ j it into
(10).
The third source of wedges arises when the firm’s optimization problem
does not take the form of cost minimization at all. Wage bargaining is the
leading example, as in search-and-matching models. 14 The outcome of the
12Basu et al. (2001, p. 245) and Doraszelski and Jaumandreu (2019) consider adjustment
costs in the context of production approach to markups. See also Berndt and Fuss (1986) and
Hulten (1986).
13Rosen (1985) surveys implicit contracts in labor markets. Macchiavello and Morjaria
(2023) survey relational contracts between firms.
14Rogerson et al. (2005) survey search-and-matching models of the labor market, which are

27
bargaining problem can be interpreted as a wedgeτ j it in equation (10) (Do-
raszelski and Jaumandreu, 2019).15 For example, even if true markups are con-
stant, changes in bargaining power or workers’ outside options can change
the impliedτ j it and the estimated markupˆµit.
In short, frictionless input markets are likely the exception, not the rule.
The three sources of wedges discussed above—non-allocative prices, dynamic
frictions, and non-cost-minimizing behavior—are all empirically relevant and
likely widespread. Differences in estimated markups across inputs, as in Ta-
ble 1a, most plausibly reflect differences in these unobserved wedgesτj it rather
than differences in true markups. That divergence is itself a diagnostic: it sig-
nals the presence of frictions or misspecification, not necessarily rising market
power. At the same time, the quantitative importance of these wedges for av-
erage markuplevelsremains an open question. If adjustment-cost wedges
fluctuate around their steady-state value, longer-run markup trends may be
more reliable than period-by-period estimates—though even steady-state ad-
justment costs need not be zero (Basu et al., 2001).
4.2 How (flexibly) should we model production?
A second conceptual hypothesis for the discrepancies in the garden is that the
assumed production function is too restrictive. When the production function
is too restrictive, variation in revenue shares that truly reflects technological
differences across firms will instead load onto the only other object allowed
by FOC (4), the markup. This is the mirror image of the wedge problem in
also inherently dynamic. They discuss different specifications of the bargaining process.
15Here is a simple bargaining model where the outcome yields equation (10). The wage is
set to split the match surplus; the worker’s outside option isU t and the worker’s bargaining
share isβ t. The match surplus is the difference between the worker’s marginal product and
outside option:W j it =U t +β t

Pit
µit
∂Fit
∂X j it −U t

.Rearranging yields an expression of the form
(10), where

1 +τ j it

≡
h
1
βt − 1−βt βt · Ut W j it
i
.

28
Section 4.1. There, the FOC is misspecified. Here, the FOC may be correctly
specified but the production function imposes a wedgeτ j it between the true
output elasticityγ j it and the measured one:bγ j it = 1 1+τ j it γj it. If a researcher ob-
servess j it but the estimated elasticitybγj it is compressed by a restrictive func-
tional form, the production approach recovers(1 +τ j it)µit rather than the true
markupµ it.
How restrictive functional forms load variation onto markups.The ratio
of FOCs across two inputs shows precisely how a restrictive functional form
can generate divergences in measured markups. Suppose labor and materials
are both fully flexible and satisfy FOC (4). Letˆµ j it denote the markup esti-
mated using inputX j. For each firmi, the ratio of the estimated FOCs for
labor to materials exactly satisfies:
sL it
sM it · ˆµL it ˆµM it = ˆγL it ˆγM it .(11)
With Cobb-Douglas estimated at the industry level, the right-hand side is con-
stant across firms, soˆµL it/ˆµM it must account for all variation ins L it/sM it . If firms
truly share the same Cobb-Douglas function—so the true output elasticities
γL andγ M are identical across firms—then any cross-firm variation inˆµL it/ˆµM it
reflects only sampling error. If not, the restriction forces technology differ-
ences into the markup ratio.
We could permit more variability in output elasticities through two main
approaches: estimating at a finer level of aggregation or using a more flexible
functional form. Each offers different degrees of freedom for elasticities to
explain variation in revenue shares.
One simple fix is to estimate elasticities at finer industry levels. Even
with a Cobb-Douglas form, allowing coefficients to vary across four-digit
industries rather than pooling at two digits lets elasticities explain more of
the observed variation in revenue shares. Coarser estimates risk conflating

29
markup and technology heterogeneity. Table 1b shows exactly this: at two
digits markups rise, at four digits they don’t—evidence coarser elasticities
force technology variation into measured markups (Foster et al., 2024). In
practice, however, going much finer is difficult: estimating separate produc-
tion functions at the firm or product level is practically impossible with the
sample sizes available in most datasets.
Doraszelski and Jaumandreu (2019), Raval (2023), and Demirer (2025) go
further, arguing the resolution is to use a more flexible functional form and to
relax Hicks-neutrality. Labor-augmenting technical progress can potentially
resolve the markup discrepancies in both Tables 1a and 1b—even when in-
puts are fully flexible and do not face non-markup wedgesτ j it. Suppose the
production function is CES with labor-augmenting technical progress, as in
(9). Then the ratio (11) becomes:
sL it
sM it · ˆµL it ˆµM it =  αl αm  Lit Mit σ−1 σ (AL it) σ−1 σ (12)
Relative output elasticities(γ L it/γM it )now depend on relative factor intensi-
ties(L it/Mit)and labor-augmenting productivityA L it. Even ifA L it is common
across firms within a period (that is,A L it =A L t ), this extra degree of freedom
can explain variation in relative factor costs instead of forcing it into markup
differences. Demirer (2025) finds allowing for labor-augmenting productivity
reduces estimated markup levels and flattens their upward trend compared
with Cobb-Douglas or Hicks-neutral CES/translog specifications.16
A more flexible production function can giveˆγL it/ˆγM it more scope to fit the
data. Three questions guide this choice:
• At what level of aggregation should industries be grouped for estima-
16The labor-augmenting view rests on difficult-to-test assumptions about the nature of pro-
ductivity. Since at least Solow (1957) and Sato (1967), it has been recognized technological bias
is difficult to distinguish from differential patterns of substitution.

30
tion?
• How flexible should the production function be?
• Is productivity Hicks-neutral, or input-biased (such as labor-
augmenting)?
Each can matter through the same mechanism: allowing output elasticities to
vary more across firms. When elasticities vary, differences in revenue shares
can be attributed to technology rather than to markups.
Constant returns to scale: a useful restriction with real costs.Constant
RTS is the most common functional form restriction in the production ap-
proach, and it has a clear upside: under constant RTS and competitive input
markets, output elasticities equal cost shares directly, requiring no additional
estimation. To see why, recall from Section 2.2 that the degree of returns to
scaleγ it equals the ratio of average to marginal cost, and the markup equals
price over marginal cost. Together these imply:
γj it =γ it cj it,(13)
wherec j it =W j itX j it/Costit is inputj’s share of total costs. When RTS are con-
stant (γ it = 1) and input markets competitive, the output elasticity equals
the cost share directly:γ j it =c j it. This is appealing because cost shares vary
across firms and over time, giving output elasticities firm-specific variation
that a single industry-level Cobb-Douglas coefficient cannot provide. That
additional variation means cost shares can potentially absorb more of the
cross-firm heterogeneity in revenue shares, leaving less to be loaded onto the
markup.
The cost of this approach is that it replaces one set of difficult-to-test
assumptions with another. Rather than assuming a restrictive production
function—whose estimation will also encounter the endogeneity concerns

31
discussed in Section 6—the researcher assumes RTS are constant and that
input markets are competitive. None of these assumptions are easy to ver-
ify. Just as a misspecified production function loads true technology variation
onto markups, incorrect assumptions regarding RTS and input markets also
lead to mismeasurement.
If true returns to scale vary across firms or over time—because of fixed
costs, scale economies, or technology differences—that variation would be in-
terpreted as markup variation. The same is true of deviations from perfect
competition in input markets: if monopsony power varies across firms and
over time, using cost shares will load that variation into the markup. Sec-
tion 4.1 engaged with deviations from perfect competition in input markets.
Deviations from constant RTS are equally plausible. Ruzic and Ho (2021) find
that a secular decline in returns to scale—from increasing toward constant—
helps rationalize long-run trends in factor shares and improves the measure-
ment of misallocation, suggesting that time-varying RTS are empirically rel-
evant and that assuming them away loads their trend into rising markups
instead. Basu et al. (2006) and Ahmad et al. (2026) find evidence consistent
with approximately constant RTS at the three-digit industry level, but hetero-
geneity across industries and firm types may still matter for cross-sectional
comparisons. McAdam et al. (2024) find in a panel of European firms that
the typical four-digit industry has close to constant returns but that there is
considerable heterogeneity.
4.3 Gross output versus value added
A final specification choice—whether to use a gross-output or value-added
production function—is conceptually distinct from functional form flexibility
but equally consequential. So far, we have assumed that firms produce gross
output via production function (5), combining capital and labor with interme-

32
diate inputs purchased from other firms.
But many papers in the production-approach literature have chosen to es-
timate value-added production functions. Value added nets out intermediates
and, as a production measure, assumes that firms produce real value added as
a function of capital, labor, and technology. Nominal value added is the value
of gross output less the cost of intermediate inputs:P itYit −W M it Mit. Real
value added in firm-level data is gross output less (real) intermediate inputs:
Yit −M it.17 Conceptually, real value added is an unintuitive construct: gross
output is shoes, while value added is “shoes lacking leather, made without
power” (Domar, 1961, p.761).
Is value added nevertheless a valid measure of output in terms of esti-
mating output elasticities and markups? Our view is no. The use of value
added as a production measure is rejected by the available empirical evidence.
Gandhi et al. (2017) show that imposing a value-added structure inflates mea-
sured productivity dispersion by a factor of five relative to a gross-output
specification. Even with perfect competition, value added requires separa-
bility:Y it =F(V(K it, Lit, Ait), Mit). Ruzic (2024) finds that this separability
assumption fails, echoing earlier findings (such as Jorgenson et al., 1987). Un-
der imperfect competition, the case weakens further: Basu and Fernald (1995)
find, in the context of the Hall-style growth-rate literature (Section 2.2), that
using value added leads to biased markup estimates.
Regardless of whether estimation is done with gross output versus value
added, macroeconomists often want value-added measures. After all, the
broadest measure of aggregate output, GDP , nets out those intermediate
transactions by definition. The approach in the representative-firm macro lit-
erature has been to take gross-output markups and convert them to equiva-
17Basu and Fernald (1995) discuss alternative definitions of value added as production
measures. In national accounting, real value added is implicitly defined such that a chain-
aggregate of materials and value added yields real gross output.

33
lents in value-added terms. Just as value added and gross output are different
(but related) objects, gross-output markups cannot be simply plugged into a
macro model as if they were value-added markups.
The mapping may be model-specific. Rotemberg and Woodford (1995)
derive the most commonly used mapping from gross-output to value-added
markups in a representative-firm model where each firm purchases interme-
diate inputs in fixed proportion to gross output. Because every firm in a sup-
ply chain charges a markup, the cumulated value-added markup exceeds the
gross-output markup through double marginalization. Specifically, ifs M de-
notes the intermediate input share of revenue:
µV = 1−s M
1−µs M ·µ.(14)
Since the gross-output markupµexceeds one, the multiplier(1−s M )/(1−µsM )
also exceeds one, so value-added markups are always at least as large as their
gross-output counterparts. The gap grows quickly. De Loecker et al. (2020)
find a sales-weighted average gross-output markup of 1.6 in recent years.
With an economy-wide intermediate input share of 50%, equation (14) would
imply a corresponding value-added markup of 4. As Basu (2019) highlights,
taken as the relevant macro parameter, a value-added markup of that mag-
nitude would imply strongly negative technological change and a negative
return to capital—implications that strain credulity. But the calculation does
make clear that the average gross-output markup cannot simply be plugged
into a representative-firm macro model.
4.4 Takeaways from the garden of forking paths
The garden of forking paths illustrates disparate markup trends need not be
mere statistical noise—they can reflect genuine conceptual choices. The forks

34
matter, and researchers face several options for navigating them.
First, the choice of input should be grounded in a persuasive case the
central FOC is likely to hold. This requires arguing from institutional detail
rather than default conventions. In some contexts, that might mean focusing
on a subset of materials—such as energy inputs in industries where they are
purchased on competitive spot markets—or on categories of labor, such as
temporary-contract workers, whose wages are more likely to reflect contem-
poraneous market conditions than long-term contracts (such as van Heuvelen
et al. 2021). Making the case for flexibility is ultimately about convincing the
reader the observed input price is the allocative one to which the firm re-
sponds when minimizing costs.
Second, when plausible frictions—such as input market power, adjust-
ment costs, or regulatory constraints—threaten the link between the first-
order condition and markups, the researcher may need to add more struc-
ture to the estimation by modeling the source of the wedge. 18 One can use
two inputs to estimate two frictions (such as markups and markdowns); or
incorporate dynamic optimization to account for capital or labor adjustment
costs; or use auxiliary data to calibrate or instrument for these frictions.19 Such
structure can help avoid loading non-markup distortions into the measured
markup.
Third, researchers can choose a production technology that is sufficiently
flexible to explain variation in revenue shares without forcing it into the
markup residual. This might involve estimating elasticities at a more gran-
ular industry level, moving beyond Cobb-Douglas to CES or translog speci-
fications, or allowing for input-augmenting technical change. These choices
18For example, Choi et al. (2024) model product-market power, input-market power, and
input-specific distortions inside the same FOC, identifying two with model structure and
inferring one as a residual.
19Examples of each approach include Dobbelaere and Mairesse (2013); Doraszelski and
Jaumandreu (2019); Kirov and Traina (2022); Cooper et al. (2024).

35
expand the scope for output elasticities to capture genuine technological het-
erogeneity so it is not mistaken for market power.
Ultimately, the production approach’s central vulnerability—that the
markup absorbs all misspecification—is also a guide to best practice. If
the estimates from different inputs agree, that convergence is evidence that
wedges are small and the production function is well specified. If they
disagree, as they often do in Tables 1a and 1b, that divergence is itself in-
formative: it signals the presence of frictions or misspecification that the
researcher should investigate rather than paper over. A complementary
approach is to focus on longer-run averages and trends rather than period-
by-period estimates. If the frictions that contaminate individual markup
estimates are roughly mean-zero over time, longer-run trends may still be
informative about market power even when cross-sectional comparisons are
unreliable (Basu et al., 2001).
The conceptual challenges discussed in this section compound with a sep-
arate set of problems: even a correctly specified model produces misleading
markup estimates if the underlying data are inadequate, as Section 5 docu-
ments.
5. The data constraint
The production approach needs two ingredients: a revenue shares j it and an
output elasticityγ j it. Data shortcomings can affect both. Mismeasured or
misclassified costs—such as the COGS/SG&A boundary discussed below—
distort the revenue share directly. Missing or noisy inputs contaminate the
production-function regressions used to estimate output elasticities. Estima-
tion biases can compound direct measurement errors in shares, leaving the
overall bias in estimated markups difficult to signa priori. This section fo-
cuses on the data problems; Section 6 takes up some of the econometric chal-

36
lenges they create. Microdata have long been known to fall short of theoretical
ideals (Grunfeld and Griliches, 1960; Griliches and Ringstad, 1971). These dif-
ficulties might help explain why markup estimates diverge so much across
studies. They also point to directions for future research, as we highlight at
the end of this section.
We first discuss how measurement error biases markups, then catalog spe-
cific data shortcomings, assess sample representativeness, and draw on his-
torical parallels to offer recommendations.
5.1 Why measurement error matters
Why do data problems matter for markup estimation? The production
markupˆµit is the ratio of an estimated output elasticityˆγj it to a measured rev-
enue shares j it. This ratio structure means that measurement errors can distort
markups in ways that are predictable in form but difficult to sign overall.
First, micro datasets consistently miss some inputs. For example, propri-
etary software, informal labor arrangements, and other intangibles often do
not appear in production surveys. Similarly, the skill composition of the labor
force or variations in factor utilization can also be considered as missing in-
puts. To see why missing inputs matter, suppose we know a priori that returns
to scale are constant. As discussed in Section 2.2, the markup then equals rev-
enue divided by total cost:ˆµ it =P itYit/Costit. If we miss any inputs, we
understate economic costs and overstate the markup. The bias approximately
equals the input’s cost share times the measurement error.20
Now suppose instead we estimate output elasticities econometrically,
rather than imposing constant returns. Missing inputs lead to omitted vari-
able bias. Suppose we take materials as the fully flexible input and estimate
20Measuring inputjas ˆX j = (1 +ϵ)X j yields markupˆµ=µ/(1 +ϵc j)with an error of
about−ϵc j percent.

37
a Cobb-Douglas production function. If we omit a portion of, say, intangible
capital, then all regression coefficients are potentially biased. The bias in the
estimated output elasticity of materials,ˆγ M, depends on the partial correla-
tion between omitted capital and materials, conditional on included variables.
Because this is a conditional correlation, the bias can be positive or negative
even if the unconditional correlation is positive—so the direction is not obvi-
ous without knowing the data.
A parallel concern is whether output itself is mismeasured. We defer this
question to Section 6, where unobserved firm-level output prices enter as the
second layer of endogeneity.
Second, even when inputs are not systematically missing, they may be
measured with noise. Classical measurement error in a single input attenuates
its own estimated elasticity. However, the effect on the coefficients for other
(accurately measured) inputs is, in general, ambiguous, depending on condi-
tional correlations in the data. In practice, multiple inputs might be mismea-
sured. The net effect on output elasticities and markups depends on which in-
puts carry more noise and how correlated different inputs are; it cannot gen-
erally be signed without dataset-specific knowledge. For instance, suppose
materials are mismeasured, leading (on its own) to attenuation bias inˆγ M.
But measurement error in labor could partially or totally offset the attenua-
tion: when noise obscures labor’s true variation, ordinary least squares (OLS)
assigns some of labor’s productive contribution to materials, which tends to
pushˆγM back up.
One input that almost surely suffers sizeable measurement error, probably
larger than the noise in labor, is capital. Book values, uncertain depreciation
schedules, and missing intangibles all make capital hard to measure accu-
rately. Collard-Wexler and De Loecker (2016) suggest that Monte Carlo sim-
ulations can help assess the quantitative (and directional) bias that arises. In
their simulations, when the variance of capital’s measurement error is 40% of

38
capital’s conditional variance, capital’s coefficients can be biased downward
by a factor of two. But, for estimating the output elasticity for materials, the
sizeable mismeasurement of capital has a more muted effect than does mea-
surement error in labor. Capital adjusts slowly—firms cannot instantly buy
or sell machines—whereas materials respond more freely to current condi-
tions. Capital and materials therefore move together less than do labor and
materials. Hence, mismeasured capital is less able to pushˆγ M upward. The
upshot is that the net bias in estimated markups from capital mismeasure-
ment is smaller than one might fear. But it is still present and its direction
depends on the specifics of the data.
Nonetheless, the practical stakes are high. Even in this simplified setup,
plausible measurement error levels can shift markup estimates by 5–15%
(Collard-Wexler and De Loecker, 2016), though the direction depends on con-
ditional correlations among inputs, not just on which input is mismeasured.
If the variance of the measurement error is relatively constant, the bias mainly
affects the level of markups. Such a bias, even if constant, could vary across
inputs, as reported in Section (3). If the variance of the measurement error is
changing over time, it could also influence estimated trends.
5.2 Specific measurement shortcomings in standard datasets
The previous subsection focused on the general mechanics of how missing
inputs or classical measurement error could affect results. This subsection
highlights five specific shortcomings in many datasets researchers regularly
use. The shortcomings illustrate the general problems of missing inputs and
classical measurement error, as well as raising additional issues. We order the
five based on our subjective view of how difficult they are in practice.

39
Revenue vs. quantity data are the most fundamental problem.Most mi-
cro datasets record revenues, not physical quantities and prices separately.
In U.S. microdata, both Compustat and individual Census surveys offer pre-
dominantly revenue-based output measures. Separating price from quantity
is possible only for a narrow slice of the economy—Foster et al. (2008) study
just 11 manufacturing products, including coffee, ready-mixed concrete, and
motor gasoline. Such data are generally unavailable at the scale needed to
study broad sectors or the whole economy. That said, survey data from some
other countries—Colombia and India, for instance—sometimes separate out-
put price from quantity. And, many customs datasets used in international
trade also contain unit values.
When Foster et al. (2008) do separate prices from quantities, they uncover
a striking puzzle: physical productivity isinverselycorrelated with price, yet
revenue productivity ispositivelycorrelated with price. The resolution reveals
why revenue data creates problems for markup estimation. A physically pro-
ductive firm has lower costs and can profitably charge less—hence the neg-
ative price correlation. Revenue productivity mixes efficiency with pricing
power: high revenue productivity could reflect genuine efficiency or simply
high markups. Without observing prices and quantities separately, we risk
conflating operational excellence with market power.21 We return to this chal-
lenge in Section 6.
Missing inputs and input quality create hard-to-detect biases.Microdata
rarely contain direct information on input quality, which can bias produc-
tion function estimates as well as productivity comparisons across firms
21Research from other countries reinforces these concerns. Garcia-Marin and Voigtl ¨ander
(2019) show that using revenue productivity rather than physical productivity underesti-
mates export efficiency gains in Chilean plant data. Lenzu et al. (2024) combine firm-level
output prices and quantities with quasi-experimental variation in credit supply in Belgium
and show that revenue-based measures underestimate the long-run elasticity of physical pro-
ductivity to credit supply by half.

40
(Griliches, 1957; Fox and Smeets, 2011; Grieco et al., 2016). Sometimes inputs
are not recorded at all. Autor et al. (2020) study labor shares in U.S. Census
microdata for six large sectors; only in manufacturing can they construct la-
bor shares of value added, because most sectoral Census microdata lack sys-
tematic information on intermediate inputs. Even in manufacturing, inputs
of business services are often missing. As discussed in the previous section,
these omissions are likely to bias estimated output elasticities, whether esti-
mated via cost-shares or regression.
The economics of COGS vs. SG&A is less clear than it seemsCompustat
reports total employees and book value of capital, but lacks the detailed in-
put classifications available in Census surveys—and intermediate inputs are
missing entirely.22 Instead, firms classify costs under Generally Accepted Ac-
counting Principles (GAAP) as either Cost of Goods Sold (COGS) or Selling,
General, and Administrative (SG&A) expenses. COGS covers costs directly
attributed to production: direct materials, direct labor, and manufacturing
overhead. SG&A covers everything else: executive salaries, marketing, R&D,
and administrative overhead. De Loecker et al. (2020) argue that this ac-
counting structure offers an advantage over Census surveys: whereas Cen-
sus data lump production and overhead workers together, GAAP requires
firms to separate production costs from overhead, providing a principled split
that standard input classifications cannot. They treat COGS as the sole flexi-
ble input and exclude SG&A entirely from the production function. In their
data sample, the COGS share of revenue has trended down in recent decades,
while their estimated output elasticity for COGS does not change much. They
22Compustat’s staff expense variable covers only 5–20% of firm-years depending on sample
construction, with non-random selection toward larger firms and specific industries. Even
Brynjolfsson and Hitt (2003), who used Compustat for production function estimation, had
to impute labor costs for firms with missing staff expense data. The headcount variable is
more widely available but is unaudited and misses labor quality, non-employee labor, and
outsourced services.

41
interpret the declining revenue share as implying rising markups.
But the mapping between accounting categories and economic inputs is
not clear-cut. Even if SG&A is partly quasi-fixed rather than fully variable,
omitting a productive input from the production function biases the estimated
elasticity of the remaining inputs upward—just as omitting capital does. The
bias worsens as the omitted input’s share of costs rises, and the SG&A share of
operating expenses has grown steadily. Traina (2018) shows this matters enor-
mously: including SG&A with COGS as the flexible input eliminates most of
the rise in estimated markups since 1980. Within-firm changes in SG&A are
approximately smooth across ranks (Traina, 2018), suggestive of routine ex-
penses that vary with output rather than the lumpy adjustments expected of
fixed costs.
The stakes are high. As documented in Section 3, a firm with $70 million
in COGS and $20 million in SG&A generating $100 million in revenue faces
a flexible input share of either 0.70 (COGS only) or 0.90 (COGS+SG&A). As-
suming an output elasticityγ= 1, the implied markups are either 43% or 11%.
Whether the declining COGS share reflects changing production economics or
evolving accounting practices remains an open question whose resolution, as
Jorgenson and Griliches (1967) emphasized, requires understanding the data
before interpreting the results.
Capital measurement is a well-known but only partially addressable prob-
lem.Micro datasets typically provide book values of capital—historical pur-
chase prices adjusted by accounting depreciation rules—rather than economic
values reflecting productive capacity. Book values can diverge dramatically
from true productive input: a fully depreciated but still-productive machine
carries zero book value; a recently purchased but obsolete asset maintains a
high one (Becker et al., 2006).
The problem deepens with intangible assets. A growing literature docu-

42
ments the importance of intangible capital—brand equity, organizational cap-
ital, and other assets beyond software and R&D (Corrado et al., 2009)—but
these typically appear in accounting data as operating expenses rather than
capitalized assets.23 Karabarbounis and Neiman (2019) document substantial
growth in “factorless income”—the apparent profits remaining after subtract-
ing measured payments to labor and capital from GDP . This could reflect true
market-power rents, an understated user cost of capital, or returns to unmea-
sured intangible capital.
Under the cost-share approach, any understatement of true costs translates
directly into inflated markup estimates. Econometric corrections can help:
Liˇzal and Galuˇsˇc´ak (2012), Collard-Wexler and De Loecker (2016), and Kim et
al. (2016) show that correcting for capital mismeasurement can nearly double
estimated capital elasticities. The cost-share approach also requires a measure
of the user cost of capital: because most capital is owned rather than rented,
the user cost must be imputed from depreciation rates, expected capital gains,
risk premia, and tax adjustments (Hall and Jorgenson, 1967; Jorgenson et al.,
1987). Getting this right is itself a major measurement challenge.
Measuring the cost of inflexible inputs requires prices that are rarely ob-
served.For inputs that cannot be freely adjusted—capital and, in the short
run, certain types of labor—the relevant cost concept is the shadow price, not
the market price. When a firm cannot instantly hire or fire workers, or cannot
costlessly buy or sell capital, the shadow value of those inputs reflects adjust-
ment costs and future expectations, not just today’s market wage or rental
rate. Using observed market prices to measure the cost of inflexible inputs
therefore introduces systematic error into both the revenue share and the esti-
23Koh et al. (2020) argue that the measured decline in the U.S. labor share is entirely ac-
counted for by the capitalization of intellectual property products in the national accounts—
illustrating how changes in accounting treatment, rather than changes in market power, can
shift measured factor shares.

43
mated elasticity simultaneously, that is, into the two ingredients whose ratio
defines the markup. This problem cuts across all of the measurement chal-
lenges above, since capital and quasi-fixed labor are precisely the inputs most
likely to be mismeasured in other dimensions as well (Fox and Smeets, 2011;
Ornaghi, 2006; Kim and Traina, 2025).
5.3 Representativeness: are we capturing the right firms?
A key selling point of the production approach is that it can be applied at
scale. In this regard, even perfect measurement at the firm level would not
resolve the challenge that the firms we observe most comprehensively might
not be representative of the economy we want to understand.
The U.S. Census of Manufactures is the gold standard for production func-
tion estimation: broad coverage, detailed input data, and separation of plants
from firms (Dunne et al., 1988; Baily et al., 1992; Foster et al., 2008; Syverson,
2011). But manufacturing now accounts for only about 12% of U.S. private-
industry value added. If markups in services or finance differ systematically
from those in manufacturing, studies based on Census manufacturing data
are learning about a shrinking and un(der)representative slice of the econ-
omy. The problem is not just coverage: manufacturing firms have relatively
clear distinctions between production workers and overhead, and between
raw materials and administrative expenses. Service firms blur these bound-
aries. A software engineer at a technology firm: production labor or over-
head? As the economy shifts toward services, accounting categories designed
for manufacturing become less economically meaningful. Census microdata
remain best-in-class in coverage and sample size, and researchers are exploit-
ing within-sector detail—for example, Dhyne et al. (2022) use Belgian firm-to-
firm transaction data that capture input linkages and allow direct observation
of intermediate input prices—but the representativeness problem does not go

44
away.
Given manufacturing’s declining share, researchers increasingly turn to
Compustat, which offers broad sectoral coverage and is easy to access. Com-
pustat covers only public firms, which account for roughly half of industry
sales (Davis et al., 2007), and some 40 percent of those sales come from for-
eign operations, complicating the interpretation of domestic market power.
Several papers (Ali et al., 2008; Keil, 2017; Decker and Williams, 2023) find
that common concentration measures at the 4-digit NAICS level based on
Compustat are only weakly correlated with those from the more comprehen-
sive economic census. Sample construction choices also matter: Benkard et al.
(2025b) show that unreported sample restrictions in De Loecker et al. (2020)
drop 27% of available Compustat observations. With the full sample, they
find that markup increases are more muted and concentrated in Finance and
Insurance, where cost measurement is especially problematic.
Whatever the dataset, a basic diagnostic is to check whether micro aggre-
gates match published national accounts totals. Fernald and Piga (2023) find
that factor shares in the U.S. Census of Manufactures are wildly different from
those in the national accounts: in 1977, labor’s share of value added in man-
ufacturing plants was only 31%, compared to 58% in the BEA-BLS KLEMS
dataset for the same sector. Such large discrepancies in factor shares trans-
late directly into different markup estimates—what looks like a high markup
might just be missing labor compensation or business services. The gap be-
tween micro data and national accounts reflects more than coverage differ-
ences: national accounts integrate multiple data sources—tax records, bank-
ing surveys, innovation surveys—that researchers rarely access, and micro
data should not be expected to aggregate to published totals without under-
standing that integration.

45
5.4 Historical lessons and recommendations
Measurement challenges are not new and are, of course, pervasive. How
economists confronted earlier episodes offers lessons for the production ap-
proach to markups.
Both macroeconomics and industrial organization were confronted with
residuals that potentially conflated true economic phenomena with measure-
ment artifacts. In macroeconomics, the puzzle was aggregate total factor pro-
ductivity. Solow (1957) found that (what we now call) the Solow residual,
explained 88 percent of growth in U.S. output-per-hour growth from 1909
to 1949. Jorgenson and Griliches (1967) argued that much or most of this
residual 88 percent largely reflected measurement error in output and inputs.
They issued what has been called a “manifesto” for improving measurement
(Berman and Jaffe, 2024, p. 579).24 They applied index-number theory to con-
struct better measures: Divisia output indexes, hedonic price adjustments,
theory-based indexes of labor composition, and user-cost weights for hetero-
geneous capital. More than half a century of research in national accounting
circles has refined these measures at an industry and aggregate level. Such
data are not just the sum over firm-level datasets, because they combine mul-
tiple data sources and allow statistically representative surveys. This is a rea-
son why the growth-rate implementation of production-approach markups
has mostly used industry data (Section 2.2).
Industrial organization faced a parallel crisis. The “structure-conduct-
performance” (SCP) paradigm (Bain, 1951; Bresnahan, 1989; Schmalensee,
1989) tried to infer market power from correlations between industry concen-
24Measurement progress since the 1960s owes much to Jorgenson and Griliches, whose
contributions extend well beyond their joint work. Griliches emphasized microdata, while
Jorgenson focused on macrodata and industry aggregates (Berman and Jaffe, 2024; Fernald,
2024). Despite these advances, their hypothesis that total factor productivity is merely mea-
surement error falls short: from 1948–2024, total factor productivity still accounts for roughly
half of labor-productivity growth (Fernald, 2014).

46
tration and accounting profit rates. It failed on two fronts: causal ambiguity
(Demsetz, 1973) (even with perfect data, the correlation between concentra-
tion and profits is uninterpretable without additional economic structure) and
the gap between accounting profitability (at best a markup of price over av-
erage variable cost) and true economic marginal cost (Fisher and McGowan,
1983). The same capital measurement problems that bedevil the production
approach—risk premia, inflation, depreciation rules, missing intangibles—
made accounting profitability an unreliable proxy for true economic returns.
The IO response was to abandon broad cross-industry regressions in favor of
deep, structurally disciplined studies of specific industries, using institutional
knowledge to pin down the assumptions that aggregate approaches cannot
test (Berry et al., 2019).
The production approach to markups tries to be broad like the macro tra-
dition and agnostic about the structure of demand like early IO—and in doing
so it has to face the measurement challenges of both. Like the SCP paradigm,
it is sometimes forced to use accounting costs and book values. Like early ag-
gregate productivity accounting, it must take a stand on input measurement
without the cross-checking that comes from integrating multiple data sources.
The implication is not that the approach is hopeless, but that substantive
progress can require both better data—the Jorgenson-Griliches response—and
more disciplined structural assumptions—the IO response.
Four practical recommendations follow from this history. First, the
Jorgenson-Griliches agenda of improving underlying data remains as relevant
today as in 1967. Better measurement of inputs—especially capital services,
intangible investments, firm-level prices, and the boundary between produc-
tion and overhead labor—would strengthen the foundation for production-
based markup estimation (Griliches and Mairesse, 1998; Lev, 2001). Second,
because the direction of bias from classical measurement error is ambiguous—
as discussed in Section 5.1—simulation can help assess the seriousness of a

47
problem in a given application. Collard-Wexler and De Loecker (2016) is an
example: They conduct dataset-specific simulations to bound measurement
biases before drawing conclusions about markup levels or trends. Third, an
easy check is to report how micro aggregates compare to published national
accounts totals—large discrepancies are a warning sign that something im-
portant is being missed, as Fernald and Piga (2023) illustrate for manufac-
turing. Fourth, when measurement problems cannot be resolved, researchers
should be explicit about the resulting bias and whether it can plausibly ex-
plain the patterns attributed to market power. These measurement problems
also feed directly into the econometric challenges of estimating output elas-
ticities, which Section 6 takes up next.
6. Practice and pitfalls in estimating output
elasticities
Production-based markups are only as reliable as the output elasticities that
underpin them. The measurement challenges documented in Section 5—
particularly unobserved output prices—feed directly into this estimation
problem. The challenge is that most tools for estimating those elasticities
were built for a world of perfect competition, and using them to measure
departures from perfect competition creates problems that run deeper than
is commonly appreciated. The applied economist has a rich toolbox, but its
tools force tradeoffs: some are restrictive for an IO economist who wants to
remain agnostic about the structure of production and competition; others are
overly general for a macroeconomist who wants to calibrate a specific model.
We organize the discussion in four parts. First, we build up the estima-
tion problem in two steps, showing how moving from physical output to
revenue data adds unobserved prices to the regression residual and creates

48
a new source of bias. Second, we show what goes wrong if those extra terms
are ignored—including a striking result that naive estimation with revenue
data can be entirely uninformative about markups. Third, we evaluate the
main econometric tools the literature has developed, asking how each fares
once we take the richer residual seriously. Fourth, we offer an assessment of
what the toolkit can and cannot deliver.
6.1 The problem: two layers of endogeneity
The fundamental challenge in estimating output elasticities is endogeneity:
firms choose their inputs in response to forces the econometrician cannot ob-
serve, so input choices are correlated with the regression residual. This prob-
lem has two layers in realistic settings, and understanding each layer sep-
arately is the key to understanding why estimating output elasticities is so
challenging.
Layer 1: Physical productivity.The cleanest statement of the problem starts
from the physical production function. For concreteness, take the Cobb-
Douglas production function (8) with three inputs and a firm-specific pro-
ductivity terma it:
yit =γ Kkit +γ Llit +γ M mit +a it,(15)
where all variables are in logs andγ X denotes the output elasticity of input
X. The residual here is just productivitya it. The endogeneity problem is the
classic “transmission bias” (Marschak and Andrews, 1944): a firm that draws
a high productivity shock may want to use more materials, som it anda it
move together. OLS attributes that comovement to technology and overstates

49
ˆγM.25 Because the production approach calculates markups asˆµit = ˆγM /sM it ,
overstatingˆγM directly overstates measured markups. This first layer is well
understood, and the econometric toolkit was largely built to address it.
Layer 2: Unobserved output prices.Few datasets contain firm-level output
quantities. Instead, researchers observe firm revenuerit =p it +y it, wherep it is
the firm’s (log) output price. Addingp it to both sides of (15) gives the revenue
production function that is actually estimated:
rit =γ Kkit +γ Llit +γ M mit +a it +p it| {z }
residual
.(16)
The residual now contains the firm’s output price as well as its productiv-
ity. This matters because output prices are correlated with input choices for
a different reason than productivity: firms with more market power charge
higher prices, restrict output, and therefore use fewer inputs. Under imperfect
competition, Klette and Griliches (1996) show that output prices and input
quantities are negatively correlated, biasing output elasticitiesdownward—
the opposite direction from Layer 1. The two biases need not cancel. More
fundamentally, the revenue-based residuala it +p it conflates technology and
demand-side forces in a way that standard tools, designed for (15), were not
built to handle. De Loecker et al. (2016) confirm this is not a theoretical curios-
ity: using Indian manufacturing data where firm-level prices are observed,
they find that revenue-based and quantity-based markup estimates diverge
substantially.
An additional complication arises when input quantities are also unob-
served. Most datasets record only input expenditurese M it =w M it +m it, so
25Henceforth, we assume the bias is positive. It need not be. Suppose firms have market
power, prices are sticky, and all firms receive the same productivity improvement. Marginal
cost falls but firms do not adjust prices. The rising markup dampens input demand, leaving
the overall OLS bias ambiguous.

50
firm-specific input pricesw M it enter the residual as well.26 We focus primarily
on the first two layers—productivity and output prices—which are likely the
dominant sources of bias in practice.
A unifying look at input demand.To see why all three components cause
endogeneity, it helps to look at what determines a firm’s materials choice.
Under Cobb-Douglas production, the first-order condition for materials gives
their conditional demand:
mit = 1 1−γ M  ait +p it + logγ M −w M it −logµ it +γ Kkit +γ Llit  .(17)
Every component of the composite residual—productivitya it, output price
pit, and input pricew M it —drives materials demand. That is the root of the
problem: the very flexibility that makes materials a good candidate for the
production-approach FOC ensures that materials respond to forces the econo-
metrician commonly cannot observe.
6.2 What goes wrong if you ignore the extra layers
Ignoring the richer residual has serious consequences, even for sophisticated
estimation strategies. This section traces those consequences before turning
to potential fixes.
Even setting aside output and input prices, OLS applied to (15) over-
statesˆγM because productive firms use more materials. Since markups are
computed asˆµit = ˆγM /sM it , the overstatement flows directly into estimated
markups. This is the transmission bias, and it is the reason the literature
moved away from OLS toward more sophisticated approaches. The deeper
26The composite residual becomesε it =a it +p it −γ M wM it . If firms with market power in
input markets face lower prices and purchase more, input expenditures are correlated with
the input-price term—a source of endogeneity discussed further in Section 4.1.

51
problem is that moving to revenue data in (16) adds a second source of bias
that can partially offset or further amplify the first, in ways that are difficult
to signex ante.
The most striking consequence of ignoring Layer 2 is a result due to Bond
et al. (2021): 27 if output elasticities are estimated from revenue data without
correcting for omitted prices, the production-approach markup formula is
tautologically uninformative. The logic is direct. With revenue data, OLS
recovers not the output elasticityγ M but a revenue elasticityˆγ revenue,M =
γM /µit—a ratio that already embeds the markup. Plugging this into the
markup formula then gives:
ˆµrevenue it = ˆγrevenue,M sM it = γM /µit γM /µit = 1.
The procedure mechanically returns markups of one, regardless of its true
value.
One response to missing firm-level prices is to deflate revenues by an in-
dustry price indexp t. Hashemi et al. (2022) show that this “fix” resolves the
problem only under perfect competition—where markups equal one and the
exercise is unnecessary. To see the logic, the price deviation in the residual be-
comes˜pit =p it −p t. Under perfect competition, the deflation works because
firms charge the same quality-adjusted price, so˜p it is zero and, thus, uncor-
related with inputs. But under imperfect competition—the case of interest—
firm-level prices reflect market power and are correlated with input choices.
Klette and Griliches (1996) show this biases elasticity estimates downward,
and De Loecker et al. (2016) show the bias is empirically meaningful. Rev-
enue productivity may still be a useful object in some settings (Foster et al.,
2008), but it is not physical productivity.
Both layers of the residual create a fundamental circularity: estimating
27DeSouza (2009) derives the same result in an earlier and less widely known paper.

52
output elasticities requires controlling for markups (because markups affect
input demand through (17)); but markups are what we are trying to mea-
sure using those elasticities. This means that any estimation strategy that ig-
nores markups is potentially misspecified in a way that contaminates the ob-
ject of interest. The circularity also explains why firm-level price data are so
valuable: they allow researchers to separate the productivity and price com-
ponents of the residual directly, breaking the loop. Such data are increas-
ingly available in manufacturing and trade datasets for homogeneous goods,
though services and differentiated products remain challenging.
6.3 The toolkit: what each approach handles and what it
does not
The literature has developed a range of tools to address endogeneity in pro-
duction function estimation. Each was designed primarily for Layer 1—a
world where the residual is just productivity. We evaluate each tool by asking:
how well does it travel to the richer-residual world of (16)?
Fixed effectsremove time-invariant components of the residual, but leave
the time-varying components that matter most for markup estimation. In-
troduced by Mundlak (1961) for agricultural production, where productivity
largely reflects time-invariant characteristics like soil fertility, firm fixed effects
absorb the permanent part of productivity, output prices, and input prices—a
genuine contribution. But time-varying productivity shocks, demand fluctu-
ations, and input-price variation all remain in the residual and remain corre-
lated with input choices.
Fixed effects also exacerbate a separate problem: measurement error in
capital. Because within-firm variation in capital is dominated by investment
and depreciation, both of which are measured with error, demeaning ampli-

53
fies that noise. Griliches and Mairesse (1998) document that panel methods
applied to micro data have produced disappointing results, with unreason-
ably low capital coefficients and implausible returns to scale. Becker et al.
(2006) show in an in-depth study of capital measurement that different ways
of measuring capital which ought to be equivalent—such as perpetual in-
ventory methods or inferring capital from capital-producing sectors—lead to
meaningfully different production function estimates. Measurement concerns
were the primary reason fixed effects were largely abandoned for production
function estimation (De Loecker and Warzynski, 2012).
Instrumental variablesare the most conceptually transparent solution, but
the bar for a valid instrument is very high in the richer-residual world. A
valid instrumentz it must be correlated with the input choice but uncorre-
lated withallcomponents of the composite residual: productivity and output
prices at minimum, and input prices when expenditures proxy for quanti-
ties. The input demand equation (17) clarifies what could work in principle:
any variable that shifts input demand without entering the production func-
tion. Input pricesw M it are the natural candidate—when available at the firm
level, they can isolate cost-driven variation in inputs (Doraszelski and Jau-
mandreu, 2013). But firm-level input prices are often weak or correlated with
local demand conditions that also affect output prices, undermining validity
(Gandhi et al., 2020).28 Aggregate demand instruments—government spend-
ing, oil price shocks, monetary policy—have been used in industry time-series
approaches (Section 2.2). But they face similar concerns if demand shocks si-
multaneously shift costs or induce entry and exit. Despite these limitations,
instrument relevance is testable, and IV deserves serious consideration when
28Even if a firm takes input prices as given, general equilibrium effects can create prob-
lems. If all firms in a market receive a positive productivity shock, the market price for their
output may fall, creating a correlation between the shocka it and the output pricep it that
contaminates the residual.

54
strong instruments are available: its assumptions are transparent in a way
that alternatives are not.
Control functionsare the current workhorse of the production function lit-
erature, largely because they avoid the need for external instruments. How-
ever, their key assumptions are individually questionable under imperfect
competition and must hold simultaneously. The approach, developed by Ol-
ley and Pakes (1996) and extended by Levinsohn and Petrin (2003), uses ob-
servable firm decisions as proxy variables for unobserved productivity. Olley
and Pakes (1996) originally used investment as the proxy. But investment is
often lumpy and infrequent. Hence, Levinsohn and Petrin (2003) proposed in-
termediate inputs, which adjust more smoothly and respond more directly to
productivity shocks. The idea is that if a firm’s investment or materials choice
responds monotonically to productivity, we can invert that relationship to ex-
press unobserved productivity as a function of observables:
ait =h −1(kit, lit;m it).(18)
Substituting this into the production function removes the endogenous pro-
ductivity term. In practice, the approach proceeds in three steps:
1.First stage: Regress output on inputs and the control variable (typically
with a flexible polynomial) to estimate the combined production and
control functionϕ t(kit, lit, mit). The residual from this regression is in-
terpreted as measurement error. The fitted valueˆy it provides output
cleansed of classical measurement error. Individual production function
parameters are not yet identified, since the materials coefficient cannot
be separated from the part ofh −1(·)that depends on materials.
2.Second stage: For candidate parameters(γ K, γL, γM ), back out productiv-
ity asˆait(γ) = ˆyit −γ Kkit −γ Llit −γ M mit.

55
3.Third stage: Productivity is assumed to be Markovian. Hence, we can
regressˆait onˆai,t−1 to decompose it into a predictable component and an
innovationξ it. Becauseξ it is orthogonal to inputs chosen before the inno-
vation is realized, lagged inputs form the basis of moment conditions for
generalized method of moments (GMM) estimation:E[ξ it(γ)·z i,t−1] = 0.
With revenue data, however, this step recovers revenue productivity
ait +p it rather than physical productivity, and the Markov assumption
must hold for the composite—a strong requirement when demand and
technology respond to different forces.
Ackerberg et al. (2015) refine the approach by assuming labor is chosen before
materials, addressing collinearity between the proxy and the flexible input.
But identification remains fragile. The output elasticity of a flexible input—
the object needed for markup inference—is underidentified in many standard
settings because the proxy’s dual role (absorbing productivityandgenerating
identifying variation) creates collinearity: when materials optimally adjust to
productivity, they become collinear with it, leaving no independent variation
to identify how inputs transform into output. Gandhi et al. (2020) show these
identification concerns are even more severe in gross-output settings, where
intermediates enter both the production function and the control. Flynn et
al. (2019) extend the analysis to settings with markups, showing that lagged
flexible instruments can generate spurious skewness in the estimated markup
distribution; imposing constant RTS resolves this identification failure.
Three assumptions are load-bearing—and each is strained by imperfect
competition. First, what is known as thescalar unobservableassumption re-
quires productivity to be theonlyunobserved driver of the proxy variable.
But in the richer-residual world, input choices also respond to output prices
and markups, so the proxy can reflect multiple unobservables and not be in-
vertible. For instance, Ackerberg et al. (2007) show that when there are two la-

56
tent state variables—productivity and an unobserved markup determinant—
two independent controls are needed, not one. Second,monotonicityrequires
the proxy to be strictly increasing in productivity, but when more produc-
tive firms charge lower prices (the Klette-Griliches logic), revenue productiv-
itya it +p it may not be monotonic ina it. The monotonicity assumption can
also fail for macroeconomic reasons: with sticky prices or inelastic short-run
demand, firms may initiallyreduceflexible input use following a positive pro-
ductivity shock and only expand later, as documented by Gal´ı (1999) and Basu
et al. (2006). Doraszelski and Li (2025) show that invertibility is testable and
propose modifications when it fails. Third, theMarkovassumption on pro-
ductivity must now hold for the composite residuala it +p it, which requires
productivity and prices to evolve in lockstep—implausible when demand re-
sponds to different forces than technology.
Proposed remedies tend to reintroduce the structural assumptions the pro-
duction approach was designed to avoid. Doraszelski and Jaumandreu (2019)
show imperfect competition renders the control function uninvertible when
input choices depend on unobserved markup determinants. One response is
to add market shares as a second control variable (De Loecker et al., 2020;
De Ridder et al., 2024), but this requires assumptions about the competi-
tive environment. Kirov et al. (2026) advocate including observable price
controls directly in the first-order conditions (see also Kasahara and Sugita,
2020; Ackerberg and De Loecker, 2024). These strategies capture price vari-
ation that drives input choices, but their validity rests on assumptions about
firm behavior—precisely the structural detail the production approach aims
to avoid. These problems concern whether control functions succeed on their
own terms—but there is a more basic gap. Even when the proxy assump-
tions hold, the method addresses Layer 1 (unobserved productivity) with-
out resolving Layer 2: inverting materials demand recoversa it, notp it, so the
Bond et al. uninformativeness problem remains unless firm-level prices or an

57
explicit demand model supplement the control function. Control functions
remain the workhorse; researchers should be explicit about which layers of
the residual they address and which they leave unresolved. At minimum,
researchers should report whether their proxy addresses output-price varia-
tion, input-price variation, or both, and conduct sensitivity checks—such as
the invertibility test of Doraszelski and Li (2025)—to assess whether the scalar
unobservable assumption is plausible in their setting.
Dynamic panel methodsreplace the scalar unobservable assumption with
time-series assumptions, but those assumptions must now hold for the full
composite residual. These methods difference the production function to re-
move fixed effects and use lagged inputs as instruments for current input
changes, relying on the assumption that lagged inputs are uncorrelated with
productivity innovations (Arellano and Bond, 1991; Blundell and Bond, 1998,
2000). System GMM combines differenced and level equations to improve ef-
ficiency. With revenue data, however, the error term becomes∆a it + ∆pit, so
the moment conditions require both productivity and prices to follow simi-
lar time-series processes—a demanding and implausible requirement when
demand and technology respond to different forces. Bond and S ¨oderbom
(2005) also note that lagged instruments only have identifying power in the
presence of frictions such as adjustment costs, but adjustment costs violate
the static first-order condition that underpins the markup calculation itself.
Brand (2019) proposes treating observed output as a noisy signal of produc-
tivity, allowing unobservables to evolve nonlinearly, and using lagged output
as an instrument when productivity is persistent and measurement error is
not. A valuable validation would use datasets that separate output prices
from quantities to test whether physical and revenue productivity have time-
series properties consistent with the approach—those assumptions underpin
the estimated elasticities and hence any markups inferred from them. These

58
refinements are promising, but the fundamental tension between the time-
series assumptions and the composite residual remains.
Structural demand modelingis the most direct solution to the omitted-
price problem, but it sacrifices the production approach’s model-free appeal.
If we are willing to specify a demand system, we can derive estimating equa-
tions in terms of observed revenue rather than unobserved quantities. For
example, Klette and Griliches (1996) propose combining the production func-
tion with an isoelastic CES demand curve:
yit =y t −η(p it −p t),(19)
whereηis the (absolute value of the) price elasticity of demand andy t,p t are
industry (not firm) quantity and price indexes. Substituting into the produc-
tion function yields a revenue-based estimating equation whose coefficients
are combinations of output elasticities and the demand elasticity:
rit −p t = η−1 η  γKkit +γ Llit +γ M mit  + 1 η yt + η−1 η ait.(20)
Output elasticities can then be separated from demand elasticities and esti-
mated using control function methods. De Loecker (2011a) extend this ap-
proach to multiproduct firms; Ruzic and Ho (2021) and Choi et al. (2024) ex-
tend it to models with heterogeneous markups and oligopolistic competition.
The benefit is transparency: structural assumptions are explicit rather than
buried in econometric corrections, and a fuller model supports richer coun-
terfactual analysis. The cost is that markups become functions of the assumed
demand and conduct model—returning, in effect, to traditional IO methods.
If demand and competition must be specified to estimate output elasticities,
the production approach’s central appeal—avoiding those specifications—is

59
substantially weakened.
These methods face the same fundamental tension: the FOC that delivers
µ=γ/sassumes a flexibly adjusted input, but identifyingγoften requires
frictions or structure that violate this very assumption.
6.4 Recommendations for applied work
No existing method fully resolves the endogeneity problem. That is worth
stating plainly. The production approach’s promise of estimating markups
without specifying market structure remains, in its most ambitious form, un-
fulfilled. What follows is practical guidance given that reality.
First, firm-level price data are the cleanest fix when available. Collect-
ing firm-specific output and input prices can eliminate the output-price bias
directly, rather than routing around it econometrically. Manufacturing and
trade datasets increasingly contain quantity information for homogeneous
goods, allowing researchers to construct firm-level prices. De Ridder et al.
(2024) provide the most systematic assessment using French manufactur-
ing data, comparing revenue-based and quantity-based markup estimates.
Their simulations—calibrated to a specific oligopoly model (both Cournot
and Bertrand cases)—yield a 0.93 correlation between revenue-based and true
log markups. But in the French data, the correlation between revenue-based
and quantity-based markups is only 0.3, well below the simulation bench-
mark. If that gap is representative, conclusions about markup trends and
dispersion drawn from revenue data alone should be treated with caution.
Services and differentiated products remain challenging, but where quantity
data exist, they should be used. For differentiated products, combining scan-
ner data with production records—as in De Ridder et al. (2024)—can approx-
imate firm-level prices even when true quantities are unavailable. Expanding
such matched datasets should be a priority for the field.

60
Second, instrumental variables deserve serious consideration when strong
instruments are available. IV is the most assumption-transparent method in
the toolkit: the exclusion restriction is explicit and testable, unlike the scalar
unobservable and monotonicity assumptions underlying control functions.
When firm-level input prices are available and strong, they provide a natural
instrument that addresses both layers of endogeneity simultaneously. The
main caveat is factor market power: if firms with monopsony power in labor
or materials markets face systematically lower input prices, input prices are
correlated with the input-price term in the residual, violating the exclusion
restriction.
Third, control functions remain the workhorse, but researchers should be
explicit about what they leave unresolved. The approach is valuable precisely
because it requires fewer external instruments than IV , and its practical imple-
mentation is well-developed (Olley and Pakes, 1996; Levinsohn and Petrin,
2003; Ackerberg et al., 2015). But in settings with meaningful price disper-
sion or market power, the scalar unobservable assumption is likely violated,
the monotonicity assumption is strained, and the Markov assumption on the
composite residual is implausible. Researchers using control functions should
report sensitivity to these assumptions and, where possible, test invertibility
following Doraszelski and Li (2025).
Fourth, the applied economist should be honest about the gap between
the toolkit and the problem. Each method makes different compromises be-
tween identification strength and the assumptions underlying markup infer-
ence. Fixed effects and deflation work only under restrictive conditions. IV
needs variation uncorrelated with all three residual components—a high bar.
Control functions assume productivity is the sole unobservable, failing when
demand affects input choices. Dynamic panels rely on implausible joint time-
series assumptions for the composite residual. Structural demand modeling
addresses these issues by imposing explicit structure, but sacrifices the model-

61
free appeal of the production approach. The right choice depends on the re-
search question, the institutional setting, and the data available. What should
not vary is the obligation to be transparent: state clearly which sources of bias
the chosen method addresses, and which it does not. Acknowledging these
limits honestly is the foundation; Section 7 builds on it with concrete recom-
mendations for making production-based markup estimation more reliable
and more transparent.
7. A Call to Arms
We began this review with a unifying FOC linking revenue shares, output
elasticities, and markups. We end by using that same FOC to launch three
methodological calls to arms. First, a transparency decomposition quantify-
ing how much revenue-share variation reflects markups versus output elas-
ticities. Second, systematic comparisons of production- and demand-based
markups. Third, more work mapping firm-level markup heterogeneity into
macroeconomic models.
7.1 Transparency: An R-squared for revenue shares
A recurring question in this review is: how much of the observed variation
in revenue shares—across firms and over time—reflects demand-side forces
like markups, and how much reflects technological differences like output
elasticities?
Implementations of the production approach frequently impose strong
parametric restrictions on output elasticities. As a result, variation in revenue
shares gets disproportionately loaded onto markups. To see why, take logs of

62
FOC (4) for inputX j:
lns j it = lnγ j it −lnµ it.(21)
This identity says that every firm-level deviation in a revenue share must be
accounted for by either the output elasticity or the markup. The variance
decomposition makes this explicit:
Var(lns j it) =Var(lnγ j it) +Var(lnµ it)−2Cov(lnγ j it,lnµ it).
When estimation restricts how much output elasticities can vary—
compressing Var(lnbγj it)—markups can inherit the leftover variation by
construction. The concern then is that parametric restrictions on output
elasticities mechanically inflate the dispersion of estimated markups and
hence markups’ explanatory power for revenue shares.
Consider this stark Cobb-Douglas example. Suppose we estimate a single
output elasticitybγj shared by all firms in a given period. Then Var(lnbγj it) = 0
and Cov(lnbγj it,lnbµit) = 0by construction, and the identity collapses to:
Var(lns j it) =Var(lnbµit).
All revenue-share variation is attributed to the production-based markup. A
regression oflns j it onlnbµit would yield anR 2 of exactly one—not necessarily
because true markups explain all the variation, but because the parametric
restriction on output elasticities forced all the variation of revenue shares into
the residual claimant, the production-based markup. AnR 2 of one means
the decomposition has no testable implications: it cannot distinguish a world
where markups truly explain all variation from one where a restrictive func-
tional form simply leaves no room for output elasticities to explain any.
A simpleR 2 diagnostic.Rather than requiring a full variance decomposi-

63
tion, a simple regression offers a practical transparency check. Consider:
lns j it =α+βln ˆγ j it +ε it,
withαthe constant,βthe slope coefficient andε it the error term. TheR 2 of this
regression measures the share of revenue-share variation linearly explained
by the estimated output elasticity. The remaining1−R 2—the residual—
captures the share attributed to the estimated markup. Consistent with the
rest of this review, the markup is the residual: whatever revenue-share varia-
tion the output elasticity cannot explain. Researchers can also run this within
dimensions of interest (year, industry, or industry-year) by including fixed ef-
fects; the withinR 2 then quantifies relative explanatory power conditional on
those controls.
Table 2 applies this diagnostic to Compustat data using replication code
from existing papers. The Output Elasticity columns report theR 2 from the
above regression; the Markup columns report1−R2. All estimates correspond
to the headline specification in De Loecker et al. (2020), which uses Cost of
Goods Sold (COGS) as the flexible input.

64
Table 2: AnR 2 Decomposition of Revenue-Share Variation: Output Elasticities
vs Markups
Full Sample Industry-Year
Output
Elasticity
Markup Output
Elasticity
Markup
De Loecker, Eeckhout & Unger (2020)
Replication File
Cobb-Douglas, Industry-Year 0.04 0.96 0.00 1.00
Cost Shares under Constant RTS
Cost Share, 2-digit NAICS 0.00 1.00 0.00 1.00
Cost Share, 4-digit NAICS 0.01 0.99 0.00 1.00
De Ridder, Grassi & Morzenti (2024)
Markup T oolbox: T ranslog, 2nd order
No interactions of inputs, Firm-Year 0.01 0.99 0.01 0.99
Interactions of inputs, Firm-Year 0.11 0.89 0.07 0.93
Note: All rows use the same Compustat sample (N= 190,388, 1980–2016), cleaned following the DLEU (2020)
protocol with support restrictions from De Ridder, Grassi & Morzenti (2024). Cost of Goods Sold (COGS) is the
flexible input throughout; SG&A is excluded to match the DLEU specification. We report theR2 from regressions
of formlns j it =α+βln ˆγ j it +ε it in the Output Elasticity columns: the share of revenue-share variation linearly
explained by the estimated output elasticity. The Markup columns report1−R 2: the residual share, attributed to
markups. Cost-share rows proxy output elasticities with median industry-year COGS cost shares under constant
RTS.
Start with the Cobb-Douglas benchmark from De Loecker et al. (2020),
which estimates sector-year output elasticities. Adding industry-year fixed
effects to the regression sets the output elasticity’s explanatory power to ex-
actly zero by construction: a single elasticity applies to every firm in a given
industry-year, so all within-industry variation in revenue shares is attributed
to markups. More striking is how little changes in the full sample. Time-
varying elasticities can absorb some revenue-share variation, but only about
4 percent of it; the markup residual explains the remaining 96 percent.
Cost-share proxies under constant RTS (Section 4.2) tell a starker story. Be-
cause median industry-year cost shares assign one elasticity per industry-year
cell, they have zero within-cell variation by construction. In the full sample,
cost shares explain at most 1 percent of revenue-share variation; the markup
residual absorbs the rest.
A natural response is to estimate elasticities more flexibly. Translog pro-

65
duction functions allow estimated coefficients to interact with firm-specific
inputs, producing output elasticities that vary across firms and time. The bot-
tom panel of Table 2 reports results using the De Ridder et al. (2024) toolbox.
Even here, the pattern persists. A translog without cross-input interactions
explains about 1 percent of revenue-share variation with output elasticities,
whether in the full sample or within industry-year. Adding cross-input inter-
actions raises the elasticity share to 11 percent in the full sample and 7 per-
cent within industry-year—the highest of any specification, but the markup
residual still explains the vast majority. The additional flexibility helps at the
margin, but the residual claimant—the markup—still dominates.
At face value, these translog results seem consistent with output elas-
ticities simply not varying much. But there is a data problem: identifying
translog terms requires enough similar firms to estimate how input ratios af-
fect output. Compustat has few firms in narrow industries, and its inputs—
Cost of Goods Sold and book capital—are coarse. Whether the lowR 2 for
elasticities reflects a real finding or a data limitation is hard to say with these
data alone.
These results illustrate a broader point: the more that estimation restricts
output elasticity variation, the more that revenue-share variation is mechan-
ically attributed to markups. The R 2 provides a helpful diagnostic but does
not by itself reveal how much output elasticity variation is truly present in the
data. Greater transparency on this front should be a priority for the literature,
and theR 2 diagnostic offers a simple, low-cost way to achieve it.29
29Becauselns= lnγ−lnµis an identity, the full variance decomposition includes a co-
variance term. For the specifications in Table 2, this term is small enough that the simple
regressionR 2 closely tracks the variance shares. The advantage of the regression is that it
requires no additional computation beyond what applied researchers already produce.

66
7.2 Stress-testing market power
A high value avenue for research is to stress-test production-based markup
estimates. Three strategies are especially promising: comparing production-
based markups against demand-based markups common in industrial organi-
zation; using simulated data—where the truth is known—to evaluate estima-
tor performance; and, exploiting natural experiments to test whether markup
estimates detect real shifts in competitive conditions.
First, the industrial organization literature has long estimated markups
from the demand side. In principle, both demand and production approaches
measure the same object—the ratio of price to marginal cost—but they do so
through different data, assumptions, and methods. Comparing them in set-
tings where both can be applied offers a valuable methodology and reality
check. When both approaches agree, we gain confidence that the empirical
signal is real. When they diverge, the comparison can pinpoint what each
method is and is not capturing. Such cross-method comparisons remain sur-
prisingly rare, and that is a missed opportunity.
The demand approach derives markups from a model of consumer be-
havior and firm pricing, typically applied to a narrowly defined industry—
the classic example is Berry et al. (1995)’s study of the automobile market.
Researchers specify a structural demand system, recover price elasticities
from observed market shares and prices, and use a conduct model (such
as Bertrand competition) to back out markups. The approach enables de-
tailed welfare and counterfactual analysis but requires rich market-level data,
functional-form assumptions about preferences and competition, and can be
sensitive to instrument selection.
Do demand and production approaches to markups agree in practice? The
evidence is mixed. Grieco et al. (2024) study the U.S. automobile industry
from 1980 to 2018 using both methods. Their demand-based estimates show

67
markups declining substantially over this period, while production-based es-
timates from De Loecker et al. (2020) point in a different direction, both in lev-
els and in trends. The authors trace much of the divergence to demand-side
improvements in product quality and variety that production-based meth-
ods may not fully capture, a revealing finding about what each approach ac-
tually measures. A more encouraging comparison comes from De Loecker
and Scott (2025)’s study of the U.S. beer industry, where both methods de-
liver broadly similar average markups, at least for certain years and specifi-
cations. A broader comparison comes from D¨opper et al. (2025) who estimate
demand-based markups across over 100 consumer product categories. They
find evidence of rising markups for 2006–2019 that are consistent with De
Loecker et al. (2020) in direction though not in magnitude.
Second, a complementary strategy is to use simulated data—where the
true markups are known—to evaluate how well production-based estimators
perform. De Ridder et al. (2024) conduct Monte Carlo simulations of this
kind. Their results suggest that, in their specific model environment, using
revenue rather than quantity data leads to biased markup estimates, though
they argue that trends and dispersion are better recovered than levels. As we
discussed in Section 6, however, the one available empirical test—comparing
revenue-based and quantity-based markups in French manufacturing data—
yields a correlation of just 0.3, well below what the simulations would sug-
gest. Whether simulation-based optimism about trends and dispersion sur-
vives contact with real data remains an important open question. Controlled
simulation exercises nonetheless help map out the conditions under which
production-based estimation can be trusted.
Third, natural experiments that generate plausibly independent shifts in
competitive conditions can help test whether markup estimates detect the
expected response. Miller et al. (2017) use the MillerCoors joint venture as
such a test, showing that demand-based markup estimates correctly pick

68
up the resulting price increases. Carrillo et al. (2023) take a different ap-
proach: quasi-random variation in public procurement contracts for con-
struction services in Ecuador identifies features of the marginal product dis-
tribution, allowing tests for misallocation and estimates of welfare losses.
Hughes and Majerovitz (2025) go further, using a randomized experiment
providing grants to Sri Lankan microenterprises to estimate the dispersion
of marginal products—and hence the costs of misallocation—without impos-
ing any production function assumptions. These settings not only help assess
production-based methods but, when combined with structural estimation,
can generate insights about firm behavior under imperfect competition that
reduced-form approaches alone cannot deliver.
Stress testing should become a standard component of markup research,
but this does not mean every paper must do everything. The production ap-
proach already demands substantial expertise across multiple fields, as this
review has illustrated, and research benefits from specialization. Some re-
searchers will push the frontier of measurement; others will focus on as-
sessment through demand modeling, experimental design, or simulation.
What we advocate is a collective effort: studies with rich data should com-
pare multiple approaches; papers introducing new methods should demon-
strate performance in simulations; empirical applications should seek quasi-
experimental corroboration where available. Through this division of labor,
the literature can build confidence in its measurements of market power and
develop a clearer understanding of when and why different methods diverge.
7.3 Aggregation: Macro implications of micro markups
Despite the conceptual and empirical challenges outlined earlier, firm-level
markup estimates can meaningfully inform our understanding of productiv-
ity, welfare, and resilience to shocks. We highlight three research questions

69
to guide the agenda for bridging micro measurement and macro modeling:
What economic forces underlie measured markups? How much firm-level
heterogeneity is needed to explain macroeconomic outcomes? And how do
markups interact with the economy’s network of input-output linkages?
First, knowing that markups exist is not enough; for policy analysis, we
need to know why firms charge them. Markups can arise from very different
sources: consumer demand elasticities, strategic pricing in oligopoly markets,
the need to recover fixed costs, search frictions (Menzio, 2025), or increasing
returns to scale. The production approach, by design, recovers equilibrium
markups without taking a stand on what generates them. This makes it a
powerful tool for documenting patterns in the data, but leaves economists
without guidance on how to embed markups into structural models where
the source of markup rents determines the welfare and growth implications.
Conflating different sources of markups can lead to misleading policy
conclusions. Markups can represent pure economic profits that reduce effi-
ciency and invite antitrust scrutiny. Or they can be a necessary byproduct of
cost recovery: firms with high fixed costs or increasing returns must charge
prices above marginal cost just to break even. If we treat all production-based
markups as stemming from a single source—say, barriers to entry—when
they partly reflect fixed costs or scale economies, our policy prescriptions
can be misleading. Making progress requires treating production parameters
themselves, not just markup estimates, as central objects of interest.30
Future research can help quantify the relative prevalence of “good” and
“bad” markups from the long-standing macro-IO debates. Some markups re-
flect entry barriers or inefficient conduct that depresses output and growth
(Bresnahan, 1989; Berry et al., 2019; Covarrubias et al., 2020). Others reflect
30Indeed, in the 1990s production-approach literature, markups and returns to scale were
treated as equally relevant. Basu and Fernald (1997) emphasized returns to scale because of
the focus of some models at the time, but their estimates mapped to markups via equation
(7).

70
Schumpeterian incentives: Aghion et al. (2005) find an inverted-U relation-
ship between competition and innovation, with markups balancing positive
incentive effects against negative efficiency costs (see Gilbert 2006 for a re-
view). Klette and Kortum (2004) and Peters (2020) model markups as the re-
turn to innovation. More recently, Autor et al. (2020) find evidence consistent
with superstar firms whose high markups reflect efficient scale and innova-
tion. By contrast, Aghion et al. (2023) argue that comparable markups can
hinder growth when they stem from process inefficiencies and R&D misallo-
cation, that is, “bad” rents. Quantifying how prevalent each type is would
help researchers understand how to rationalize production-based estimates
in macroeconomic models.31
Second, how much heterogeneity matters for macro outcomes is a central
open question. In other words: do we need the full distribution of firm-level
markups to draw reliable macro conclusions, or does a representative firm get
us close enough? On the household side, macroeconomists debate whether
simplified two-agent New Keynesian (TANK) models capture enough het-
erogeneity, or whether richer heterogeneous-agent New Keynesian (HANK)
models are required despite being harder to work with (Gal ´ı et al., 2007; Ka-
plan et al., 2018). An analogous question arises for firms, and tractability
pushes modelers toward parsimony; but ignoring important dimensions of
heterogeneity risks distorting key counterfactuals.
Economic theory has not yet resolved how to aggregate firm-level
markups into representative macro models. Standard business-cycle and
growth models typically rely on a representative firm producing value added
from capital and labor, without intermediate inputs; mapping firm-level
gross-output markups into that framework is not straightforward. Rotem-
berg and Woodford (1995, 1999) show that strong assumptions are needed
31Aghion et al. (2023) and De Ridder (2024) argue that good rents can morph into bad rents
as technological winners erect barriers to entry, ultimately reducing innovation and growth.

71
to translate gross-output production with market power into value-added
production. Basu and Fernald (1997) argue that the right way to aggregate
firm-level elasticities and markups depends on model specifics; for example,
they provide a stylized example where the answer depends on whether
marginal inputs are allocated proportionally to average inputs over the busi-
ness cycle. No general answer yet exists for how much micro heterogeneity
needs to be preserved when calibrating representative-firm models.32
Ongoing empirical debates underscore why this heterogeneity question
is so important. Revenue shares vary widely across firms but not randomly:
Large, expanding firms tend to have low labor shares, with potentially impor-
tant macro consequences (Autor et al., 2020; Kehrig and Vincent, 2021). Van
Reenen (2018) documents increasing differences between firms in sales, pro-
ductivity, and wages; when the measured aggregate markup increases, this in-
crease is driven largely by reallocation toward larger, more productive firms.
In rationalizing these patterns, workhorse models often feature firm hetero-
geneity in productivity (Ericson and Pakes, 1995; Hopenhayn, 1992; Melitz,
2003) and demand elasticities (Atkeson and Burstein, 2008), but typically as-
sume common production technologies within industries. If empirical evi-
dence of heterogeneous output elasticities proves robust, existing modeling
frameworks will need to evolve. The choice of how to aggregate also matters:
Edmond et al. (2023) show sales-weighted markups rise much more steeply
than cost-weighted ones, with the gap reflecting allocative inefficiency from
dispersion.33
32Growth accounting has long emphasized that microeconomic heterogeneity can explain
macro aggregates. Basu and Fernald (1997, 2002) extend the accounting in Jorgenson et al.
(1987) to allow for heterogeneity in markups and returns to scale. The misallocation litera-
ture also emphasizes micro heterogeneity; Baqaee and Rubbo (2023) review the more recent
literature, including Baqaee and Farhi (2020).
33Markup heterogeneity need not imply misallocation. Bornstein and Peter (2025) show
that under nonlinear pricing, markup heterogeneity across firms is an equilibrium feature
that does not reflect inefficiency.

72
Third, more research should help evaluate how the economy’s network
structure shapes the welfare consequences of markups. A long tradition of
network analysis—from Leontief (1941) to work reviewed by Carvalho and
Tahbaz-Salehi (2019) and Baqaee and Rubbo (2023)—shows that intermediate
input flows can amplify or attenuate distortions, so the location and propaga-
tion of markups through the network are as important as their average level.
Notably, upstream markups are likely more costly to the economy than
downstream ones because they distort production directly rather than sim-
ply redistributing income. A markup on goods sold to final consumers may
redistribute income from consumers to firms, with limited real effects, es-
pecially if labor is supplied inelastically. A markup on intermediate inputs
sold to other producers acts more like a tax on production, distorting input
choices and depressing aggregate productivity: it pushes the economy inside
its production-possibilities frontier and violates the Diamond and Mirrlees
(1971) production-efficiency theorem. Basu (1995), Basu and Fernald (2002),
Bigio and La’O (2020), and Baqaee and Farhi (2020) formalize these effects.
Whether markups actually generate misallocation also depends critically
on how firms contract with one another. When firms transact on spot mar-
kets, markups compound along supply chains through “double marginaliza-
tion,” magnifying inefficiencies at each stage. But when upstream and down-
stream firms bargain directly—as in many long-term supplier relationships—
markups need not generate misallocation even when they appear large. The
macro consequences of markup heterogeneity therefore cannot be read off
from markup estimates alone; they depend on network position and the in-
stitutional arrangements through which firms trade. Future research should
clarify when markups primarily redistribute income, when they distort pro-
duction, and how to incorporate these distinctions into tractable macro mod-
els.

73
7.4 Takeaways for practice
The preceding discussion points to three research priorities, each at a different
stage of development.
First, researchers should report theR 2 decomposition of revenue-share
variation into markup and output-elasticity components; if the markup ex-
plains nearly all the variation, that is a warning that the specification could
be leaving too little room for technology. This diagnostic is available now and
costs nothing beyond what applied researchers already compute.
Second, where the setting allows, production-based markups should be
tested against outside evidence—demand-based estimates, simulations with
known truth, or quasi-experimental shifts in competitive conditions. Such
comparisons remain surprisingly rare, and expanding them is the most
promising near-term path to putting the literature on firmer empirical foot-
ing.
Third, aggregation from firm to macro requires more careful attention to
when markup heterogeneity reflects misallocation versus equilibrium dis-
persion, and to how network position shapes the welfare consequences of
markups. This is the least resolved of the three and the most important for
macroeconomists who want to use production-based estimates in general-
equilibrium models.
Progress on all three fronts—transparency, testing, and aggregation—
requires confronting the same fundamental challenge that runs through this
entire review: production-based markups are residuals, and residuals are
only as informative as the models, data, and econometrics that generate them.

74
8. Conclusion
The production approach to markups is both powerful and fragile. Its power
comes from its minimal structure. With cost minimization and a flexible input,
all we need is the input’s share in revenue and its output elasticity to back out
a markup. Its fragility comes from the same source. Because markups are
residuals, whatever the model, the data, or the econometrics fail to capture
gets loaded onto the markup. Researchers make a series of choices, each with
its own risks.
For markup estimation, Hall (1986, 1988, 1990) marked an important shift
from “craft to mass production” (Basu, 2024). Craft methods in the IO liter-
ature focus on careful studies of narrow industries with rich structural de-
tail. Macroeconomists and trade economists need scale. Hall’s production
approach and the large literature applying his insights allow such scale.
Nevertheless, mass production in manufacturing requires much more than
just a clear factory blueprint. For the factory to produce, it requires sourcing
of reliable and high-quality inputs; it requires local institutional knowledge
to acquire the needed permits and address planning commissions; and much
besides. Similarly, applying the blueprint for production-based markups laid
out in Section 2.3 is not just an off-the-shelf exercise. This review has high-
lighted many of the challenges that need to be acknowledged and, ideally,
addressed.
Production-based markup estimates should not be taken at face value. The
disagreements across studies are not minor: using the same data, different
inputs imply opposite trends, different production functions yield markedly
different levels, and different estimation methods produce divergent results.
These disagreements reflect non-markup frictions, specification choices, data
limitations, and econometric pitfalls—and they signal that the production ap-
proach’s assumptions are difficult to satisfy in practice. More systematic at-

75
tention to the checks developed in the preceding sections would sharpen the
evidence on market power and reduce the risk that conclusions rest on ar-
tifacts of specification or measurement. To move forward, we need trans-
parency, testing, robustness, and better data.
What should economists do with the evidence? We should acknowledge
how much remains uncertain, while pressing ahead on both theory and mea-
surement. On the theoretical side, there is no reason to wait. Markups shape
resource allocation and welfare. They interact with misallocation, innovation,
network structure, and cyclical dynamics. They also shape how shocks prop-
agate across firms and industries. But we also need evidence on the structures
that actually drive markups, in order to guide theorizing. The way forward
is to use the approach honestly: report what the residual absorbs, test esti-
mates against outside evidence, and treat specification choices as consequen-
tial rather than interchangeable. Measurement leaves us with residuals. The
challenge is to combine institutional knowledge and economic theory to show
what those residuals mean for growth, welfare, and policy.
References
Acemoglu, Daron and Alireza Tahbaz-Salehi, “The Macroeconomics of Supply Chain
Disruptions,”Review of Economic Studies, 2025,92(2), 656–695.
Ackerberg, Daniel and Jan De Loecker, “Production Function Identification Under
Imperfect Competition,” Discussion Paper DP19640, CEPR, Paris & London 2024.
, C Lanier Benkard, Steven Berry, and Ariel Pakes, “Econometric Tools for Analyz-
ing Market Outcomes,” in James J. Heckman and Edward E. Leamer, eds.,Hand-
book of Econometrics, Vol. 6, Elsevier, 2007, pp. 4171–4276.
, Kevin Caves, and Garth Frazer, “Identification Properties of Recent Production

76
Function Estimators,”Econometrica, 2015,83(6), 2411–51.
Aghion, Philippe, Antonin Bergeaud, Timo Boppart, Peter J Klenow, and Huiyu Li,
“A Theory of Falling Growth and Rising Rents,”Review of Economic Studies, 2023,
90(6), 2675–2702.
, Nick Bloom, Richard Blundell, Rachel Griffith, and Peter Howitt, “Competition
and Innovation: An Inverted-U Relationship,”Quarterly Journal of Economics, 2005,
120(2), 701–728.
Ahmad, Mumtaz, John Fernald, and Hashmat Khan, “Returns to Scale in U.S. Pro-
duction, Redux,” 2026. Unpublished manuscript, INSEAD.
Ali, Ashiq, Sandy Klasa, and Eric Yeung, “The Limitations of Industry Concentration
Measures Constructed with Compustat Data: Implications for Finance Research,”
Review of Financial Studies, 2008,22(10), 3839–3871.
Arellano, Manuel and Stephen Bond, “Some Tests of Specification for Panel Data:
Monte Carlo Evidence and an Application to Employment Equations,”Review of
Economic Studies, 1991,58(2), 277–297.
Asker, John, Allan Collard-Wexler, and Jan De Loecker, “Dynamic Inputs and Re-
source (Mis) Allocation,”Journal of Political Economy, 2014,122(5), 1013–1063.
Atkeson, Andrew and Ariel Burstein, “Pricing-to-Market, Trade Costs, and Interna-
tional Relative Prices,”American Economic Review, 2008,98(5), 1998–2031.
Autor, David, David Dorn, Lawrence Katz, Christina Patterson, and John Van
Reenen, “The Fall of the Labor Share and the Rise of Superstar Firms,”Quarterly
Journal of Economics, 2020,135(2), 645–709.
Baily, Martin, Charles Hulten, and David Campbell, “Productivity Dynamics in Man-
ufacturing Plants,”Brookings Papers on Economic Activity: Microeconomics, 1992,
1992(1), 187–267.
Bain, Joe, “Relation of Profit Rate to Industry Concentration: American Manufactur-
ing, 1936–1940,”Quarterly Journal of Economics, 1951,65(3), 293–324.

77
Baqaee, David and Elisa Rubbo, “Micro Propagation and Macro Aggregation,”An-
nual Review of Economics, 2023,15(1), 91–123.
and Emmanuel Farhi, “Productivity and Misallocation in General Equilibrium,”
Quarterly Journal of Economics, 2020,135(1), 105–63.
Baqaee, David Rezza, Emmanuel Farhi, and Kunal Sangani, “The Darwinian Returns
to Scale,”Review of Economic Studies, 2024,91(3), 1373–1405.
Barkai, Simcha, “Declining Labor and Capital Shares,”Journal of Finance, 2020,75(5),
2421–63.
Basu, Susanto, “Intermediate Goods and Business Cycles: Implications for Produc-
tivity and Welfare,”American Economic Review, 1995,85(3), 512–531.
, “Are Price-Cost Markups Rising in the United States? A Discussion of the Evi-
dence,”Journal of Economic Perspectives, 2019,33(3), 3–22.
, “Basu Remarks on Bob Hall,” Unpublished slides, presented at “Celebrating the
Work of Bob Hall,” Hoover Institution, Stanford University November 2024.
and Christopher L. House, “Chapter 6 - Allocative and Remitted Wages: New
Facts and Challenges for Keynesian Models,” in John B. Taylor and Harald Uhlig,
eds.,Handbook of Macroeconomics, Vol. 2, Elsevier, 2016, pp. 297–354.
and John Fernald, “Are Apparent Productive Spillovers a Figment of Specification
Error?,”Journal of Monetary Economics, 1995,36(1), 165–188.
and , “Returns to Scale in US Production: Estimates and Implications,”Journal
of Political Economy, 1997,105(2), 249–83.
and , “Why Is Productivity Procyclical? Why Do We Care?,” in “New Devel-
opments in Productivity Analysis,” National Bureau of Economic Research, 2001,
pp. 225–302.
and , “Aggregate Productivity and Aggregate Technology,”European Economic
Review, 2002,46(6), 963–91.

78
, , and Matthew D. Shapiro, “Productivity Growth in the 1990s: Technology,
Utilization, or Adjustment?,”Carnegie-Rochester Conference Series on Public Policy,
2001,55(1), 117–165.
, John G. Fernald, and Miles S. Kimball, “Are Technology Improvements Contrac-
tionary?,”American Economic Review, 2006,96(5), 1418–1448.
Becker, Randy A., John Haltiwanger, Ron S. Jarmin, Shawn D. Klimek, and Daniel J.
Wilson, “Micro and Macro Data Integration: The Case of Capital,” in Dale Jorgen-
son, J. Steven Landefeld, and William Nordhaus, eds.,A New Architecture for the US
National Accounts, Chicago: University of Chicago Press, 2006, pp. 541–610.
Benkard, C. Lanier, Nathan H. Miller, and Ali Yurukoglu, “Rejoinder to “The Rise of
Market Power and the Macroeconomic Implications: Reply to Benkard, Miller, and
Yurukoglu (2025)”,” 2025. Working paper.
, , and , “The Rise of Market Power and the Macroeconomic Implications:
Comment,” Working Paper 34513, National Bureau of Economic Research 2025.
Berger, David, Kyle Herkenhoff, and Simon Mongey, “Labor Market Power,”Ameri-
can Economic Review, 2022,112(4), 1147–1193.
Berman, Eli and Adam B. Jaffe, “Zvi Griliches (1930–1999),” in Robert A. Cord,
ed.,The Palgrave Companion to Harvard Economics, Cham, Switzerland: Palgrave
Macmillan, 2024, pp. 573–596.
Berndt, Ernst R. and Melvyn A. Fuss, “Productivity Measurement with Adjustments
for Variations in Capacity Utilization and Other Forms of Temporary Equilibrium,”
Journal of Econometrics, 1986,33(1), 7–29.
Berry, Steven, James Levinsohn, and Ariel Pakes, “Automobile Prices in Market Equi-
librium,”Econometrica, 1995,63(4), 841–890.
, Martin Gaynor, and Fiona Scott Morton, “Do Increasing Markups Matter?
Lessons from Empirical Industrial Organization,”Journal of Economic Perspectives,
2019,33(3), 44–68.

79
Bigio, Saki and Jennifer La’O, “Distortions in Production Networks,”Quarterly Jour-
nal of Economics, 2020,135(4), 2187–2253.
Blundell, Richard and Stephen Bond, “Initial Conditions and Moment Restrictions in
Dynamic Panel Data Models,”Journal of Econometrics, 1998,87(1), 115–143.
and , “GMM Estimation with Persistent Panel Data: An Application to Produc-
tion Functions,”Econometric Reviews, 2000,19(3), 321–40.
Bond, Stephen and M ˚ans S ¨oderbom, “Adjustment Costs and the Identification of
Cobb-Douglas Production Functions,” Technical Report W05/04, Institute for Fis-
cal Studies, London 2005.
Bond, Steve, Arshia Hashemi, Greg Kaplan, and Piotr Zoch, “Some Unpleasant
Markup Arithmetic: Production Function Elasticities and Their Estimation from
Production Data,”Journal of Monetary Economics, 2021,117, 511–33.
Borges, Jorge Luis, “El jard´ın de senderos que se bifurcan,” in “El jard´ın de senderos
que se bifurcan,” Buenos Aires: Sur, 1941.
Bornstein, Gideon and Alessandra Peter, “Nonlinear Pricing and Misallocation,”
American Economic Review, 2025,115(11), 3853–3908.
Brand, James, “Estimating Productivity and Markups Under Imperfect Competi-
tion,” Technical Report, Working paper 2019.
Bresnahan, Timothy F, “Empirical Studies of Industries with Market Power,” in
Richard Schmalensee and Robert D. Willig, eds.,Handbook of Industrial Organiza-
tion, Vol. 2, Elsevier, 1989, pp. 1011–1057.
Brynjolfsson, Erik and Lorin M Hitt, “Computing Productivity: Firm-Level Evi-
dence,”Review of Economics and Statistics, 2003,85(4), 793–808.
Byrne, David M, John Fernald, and Marshall B Reinsdorf, “Does the United States
Have a Productivity Slowdown or a Measurement Problem?,”Brookings Papers on
Economic Activity, 2016,2016(1), 109–182.
Carrillo, Paul, Dave Donaldson, Dina Pomeranz, and Monica Singhal, “Misalloca-
tion in Firm Production: A Nonparametric Analysis Using Procurement Lotteries,”

80
Technical Report, National Bureau of Economic Research 2023.
Carvalho, Vasco M. and Alireza Tahbaz-Salehi, “Production Networks: A Primer,”
Annual Review of Economics, 2019,11(1), 635–663.
Choi, Jaedo, Andrei A Levchenko, Dimitrije Ruzic, and Younghun Shim, “Superstars
or Supervillains? Large Firms in the South Korean Growth Miracle,” Working Pa-
per 32648, National Bureau of Economic Research 2024.
Collard-Wexler, Allan and Jan De Loecker, “Production Function Estimation and
Capital Measurement Error,” Working Paper, National Bureau of Economic Re-
search 2016.
Cooper, Russell, John C. Haltiwanger, and Jonathan Willis, “Declining Responsive-
ness at the Establishment Level: Sources and Productivity Implications,” NBER
Working Papers 32130, National Bureau of Economic Research, Inc Feb 2024.
Corrado, Carol, Charles Hulten, and Daniel Sichel, “Intangible Capital and US Eco-
nomic Growth,”Review of Income and Wealth, 2009,55(3), 661–685.
Covarrubias, Matias, Germ´an Guti´errez, and Thomas Philippon, “From Good to Bad
Concentration? US Industries over the Past 30 Years,”NBER Macroeconomics An-
nual, 2020,34(1), 1–46.
Crouzet, Nicolas and Janice Eberly, “Understanding Weak Capital Investment: The
Role of Market Concentration and Intangibles,” Technical Report, National Bureau
of Economic Research 2019.
Davis, Steven J, John Haltiwanger, Ron Jarmin, and Javier Miranda, “Volatility and
Dispersion in Business Growth Rates: Publicly Traded versus Privately Held
Firms,” in “NBER Macroeconomics Annual 2006, Volume 21,” Cambridge, MA:
MIT Press, 2007, pp. 107–180.
De Loecker, Jan, “Product Differentiation, Multiproduct Firms, and Estimating the
Impact of Trade Liberalization on Productivity,”Econometrica, 2011,79(5), 1407–
1451.

81
, “Recovering Markups from Production Data,”International Journal of Industrial
Organization, 2011,29(3), 350–355.
and Frederic Warzynski, “Markups and Firm-Level Export Status,”American Eco-
nomic Review, 2012,102(6), 2437–71.
and Jan Eeckhout, “The Rise of Market Power and the Macroeconomic Implica-
tions: Reply to Benkard, Miller, and Yurukoglu (2025),” 2025. Working paper.
and Paul T Scott, “Markup Estimation Using Production and Demand Data: An
Application to the US Brewing Industry,”Review of Economic Studies, 2025. Ac-
cepted.
, Jan Eeckhout, and Gabriel Unger, “The Rise of Market Power and the Macroeco-
nomic Implications,”Quarterly Journal of Economics, 2020,135(2), 561–644.
, Pinelopi K Goldberg, Amit K Khandelwal, and Nina Pavcnik, “Prices, Markups,
and Trade Reform,”Econometrica, 2016,84(2), 445–510.
De Ridder, Maarten, “Market Power and Innovation in the Intangible Economy,”
American Economic Review, 2024,114(1), 199–251.
, Basile Grassi, and Giovanni Morzenti, “The Hitchhiker’s Guide to Markup Esti-
mation,” POID Working Papers 063, Centre for Economic Performance, LSE 2024.
Decker, Ryan A. and Jacob Williams, “A Note on Industry Concentration Measure-
ment,” FEDS Notes 2023-02-03, Board of Governors of the Federal Reserve System
(U.S.) 2023.
Demirer, Mert, “Production Function Estimation with Factor-Augmenting Technol-
ogy: An Application to Markups,” Technical Report, Working paper 2025.
Demsetz, Harold, “Industry Structure, Market Rivalry, and Public Policy,”Journal of
Law and Economics, 1973,16(1), 1–9.
DeSouza, Sergio A, “Estimating Mark-ups from Plant-Level Data,”Journal of Indus-
trial Economics, 2009,57(2), 353–363.

82
Dhyne, Emmanuel, Ayumu Ken Kikkawa, and Glenn Magerman, “Imperfect Com-
petition in Firm-to-Firm Trade,”Journal of the European Economic Association, 2022,
20(5), 1933–1970.
Diamond, Peter A. and James A. Mirrlees, “Optimal Taxation and Public Production
I: Production Efficiency,”American Economic Review, 1971,61(1), 8–27.
Dobbelaere, Sabien and Jacques Mairesse, “Panel Data Estimates of the Production
Function and Product and Labor Market Imperfections,”Journal of Applied Econo-
metrics, 2013,28(1), 1–46.
Domar, Evsey D., “On the Measurement of Technological Change,”The Economic Jour-
nal, 1961,71(284), 709–729.
D¨opper, Hendrik, Alexander MacKay, Nathan Miller, and Joel Stiebale, “Rising
Markups and the Role of Consumer Preferences,”Journal of Political Economy, 2025,
133(8), 2462–2505.
Doraszelski, Ulrich and Jordi Jaumandreu, “R&D and Productivity: Estimating En-
dogenous Productivity,”Review of Economic Studies, 2013,80(4), 1338–1383.
and , “Using Cost Minimization to Estimate Markups,” 2019. Working Paper.
and Lixiong Li, “Production Function Estimation without Invertibility: Imper-
fectly Competitive Environments and Demand Shocks,” Working Paper 33939, Na-
tional Bureau of Economic Research June 2025.
Dunne, Timothy, Mark Roberts, and Larry Samuelson, “Patterns of Firm Entry and
Exit in US Manufacturing Industries,”RAND Journal of Economics, 1988,19(4), 495–
515.
Edmond, Chris, Virgiliu Midrigan, and Daniel Yi Xu, “How Costly Are Markups?,”
Journal of Political Economy, 2023,131(7), 1619–1675.
Elsby, Michael WL, Bart Hobijn, and Ays ¸eg¨ul S ¸ahin, “The Decline of the US Labor
Share,”Brookings Papers on Economic Activity, 2013,2013(2), 1–63.
Ericson, Richard and Ariel Pakes, “Markov-Perfect Industry Dynamics: A Frame-
work for Empirical Work,”Review of Economic Studies, 1995,62(1), 53–82.

83
Feenstra, Robert C. and David E. Weinstein, “Globalization, Markups, and US Wel-
fare,”Journal of Political Economy, 2017,125(4), 1040–1074.
Fernald, John, “A Quarterly, Utilization-Adjusted Series on Total Factor Productiv-
ity,” Working Paper Series 2012-19, Federal Reserve Bank of San Francisco 2014.
, “Dale W. Jorgenson (1933–2022),” in Robert A. Cord, ed.,The Palgrave Companion
to Harvard Economics, Cham, Switzerland: Palgrave Macmillan, 2024, pp. 597–631.
and Eugenio Piga, “Comment on: Bottlenecks: Sectoral Imbalances and the US
Productivity Slowdown,” in “NBER Macroeconomics Annual 2023, volume 38,”
Chicago: University of Chicago Press, 2023.
, Robert Inklaar, and Dimitrije Ruzic, “The Productivity Slowdown in Advanced
Economies: Common Shocks or Common Trends?,”Review of Income and Wealth,
2024,70(4), 869–895.
Fisher, Franklin and John McGowan, “On the Misuse of Accounting Rates of Return
to Infer Monopoly Profits,”American Economic Review, 1983,73(1), 82–97.
Flynn, Zach, James Traina, and Amit Gandhi, “Measuring Markups with Production
Data,” 2019. Working Paper.
Foster, Lucia, John Haltiwanger, and Chad Syverson, “Reallocation, Firm Turnover,
and Efficiency: Selection on Productivity or Profitability?,”American Economic Re-
view, 2008,98(1), 394–425.
Foster, Lucia S, John C Haltiwanger, and Cody Tuttle, “Rising Markups or Changing
Technology?,” Working Paper 30491, National Bureau of Economic Research 2024.
Fox, Jeremy and Val´erie Smeets, “Does Input Quality Drive Measured Differences in
Firm Productivity?,”International Economic Review, 2011,52(4), 961–989.
Gal´ı, Jordi, “Technology, Employment, and the Business Cycle: Do Technology
Shocks Explain Aggregate Fluctuations?,”American Economic Review, 1999,89(1),
249–271.
, J. David L ´opez-Salido, and Javier Vall ´es, “Understanding the Effects of Gov-
ernment Spending on Consumption,”Journal of the European Economic Association,

84
2007,5(1), 227–270.
Gandhi, Amit, Salvador Navarro, and David Rivers, “How Heterogeneous Is Pro-
ductivity? A Comparison of Gross Output and Value Added,” Technical Report
201727, Center for Human Capital and Productivity, University of Western Ontario
2017.
, , and , “On the Identification of Gross Output Production Functions,”Journal
of Political Economy, 2020,128(3), 810–53.
Garcia-Marin, Alvaro and Nico Voigtl ¨ander, “Exporting and Plant-Level Efficiency
Gains: It’s in the Measure,”Journal of Political Economy, 2019,127(4), 1777–1825.
Gelman, Andrew and Eric Loken, “The Statistical Crisis in Science,”American Scien-
tist, 2014,102(6), 460–465.
Gilbert, Richard, “Looking for Mr. Schumpeter: Where Are We in the Competition–
Innovation Debate?,”Journal of Economic Literature, 2006,44(3), 537–583.
Grieco, Paul, Charles Murry, and Ali Yurukoglu, “The Evolution of Market Power in
the US Automobile Industry,”Quarterly Journal of Economics, 2024,139(2), 1201–
1253.
, Shengyu Li, and Hongsong Zhang, “Production Function Estimation with Unob-
served Input Price Dispersion,”International Economic Review, 2016,57(2), 665–690.
Griliches, Zvi, “Specification Bias in Estimates of Production Functions,”Journal of
Farm Economics, 1957,39(1), 8–20.
and Jacques Mairesse, “Production Functions: The Search for Identification,”
in Steinar Strøm, ed.,Econometrics and Economic Theory in the Twentieth Century:
The Ragnar Frisch Centennial Symposium, Cambridge: Cambridge University Press,
1998, pp. 169–203.
and Vidar Ringstad,Economies of Scale and the Form of the Production Function:
An Econometric Study of Norwegian Manufacturing Establishment Data, Amsterdam:
North-Holland Publishing Company, 1971.

85
Grunfeld, Yehuda and Zvi Griliches, “Is Aggregation Necessarily Bad?,”Review of
Economics and Statistics, 1960,42(1), 1–13.
Guti´errez, Germ ´an and Thomas Philippon, “Investmentless Growth: An Empirical
Investigation,”Brookings Papers on Economic Activity, 2017,2017(2), 89–190.
Hall, Robert, “Employment Fluctuations and Wage Rigidity,”Brookings Papers on Eco-
nomic Activity, 1980,11(1, Tenth Anniversary Issue), 91–142.
Hall, Robert E., “Market Structure and Macroeconomic Fluctuations,”Brookings Pa-
pers on Economic Activity, 1986,2, 285–322.
, “The Relation Between Price and Marginal Cost in US Industry,”Journal of Political
Economy, 1988,96(5), 921–47.
, “Invariance Properties of Solow’s Productivity Residual,” in Peter Diamond, ed.,
Growth/ Productivity/Unemployment: Essays to Celebrate Robert Solow’s Birthday, Cam-
bridge, MA: MIT Press, 1990, pp. 71–112.
and Dale W. Jorgenson, “Tax Policy and Investment Behavior,”American Economic
Review, 1967,57(3), 391–414.
Haltiwanger, John, Robert Kulick, and Chad Syverson, “Misallocation Measures: The
Distortion That Ate the Residual,” Working Paper 24199, National Bureau of Eco-
nomic Research 2018.
Hashemi, Arshia, Ivan Kirov, and James Traina, “The Production Approach to
Markup Estimation Often Measures Input Distortions,”Economics Letters, 2022,
217, 110673.
Hopenhayn, Hugo, “Entry, Exit, and Firm Dynamics in Long Run Equilibrium,”
Econometrica, 1992,60(5), 1127–50.
Hsieh, Chang-Tai and Pete Klenow, “Misallocation and Manufacturing TFP in China
and India,”Quarterly Journal of Economics, 2009,124(4), 1403–48.
Hughes, David and Jeremy Majerovitz, “Measuring Misallocation with Experi-
ments,” Technical Report, CEPR 2025.

86
Hulten, Charles R., “Productivity Change, Capacity Utilization, and the Sources of
Efficiency Growth,”Journal of Econometrics, 1986,33(1), 31–50.
Jarosch, Gregor, Jan Sebastian Nimczik, and Isaac Sorkin, “Granular Search, Market
Structure, and Wages,”Review of Economic Studies, 2024,91(6), 3569–3607.
Jorgenson, Dale W. and Zvi Griliches, “The Explanation of Productivity Change,”
Review of Economic Studies, 1967,34(99), 249–280.
, Frank M. Gollop, and Barbara M. Fraumeni,Productivity and US Economic Growth,
Cambridge, MA: Harvard University Press, 1987.
Kaplan, Greg, Benjamin Moll, and Giovanni L. Violante, “Monetary Policy According
to HANK,”American Economic Review, 2018,108(3), 697–743.
Karabarbounis, Loukas and Brent Neiman, “The Global Decline of the Labor Share,”
Quarterly Journal of Economics, 2014,129(1), 61–103.
and , “Accounting for Factorless Income,”NBER Macroeconomics Annual, 2019,
33(1), 167–228.
Kasahara, Hiroyuki and Yoichi Sugita, “Nonparametric Identification of Production
Function, Total Factor Productivity, and Markup from Revenue Data,” 2020. arXiv
preprint arXiv:2011.00143.
Kehrig, Matthias and Nicolas Vincent, “The Micro-Level Anatomy of the Labor Share
Decline,”Quarterly Journal of Economics, May 2021,136(2), 1031–1087.
Keil, Jan, “The Trouble with Approximating Industry Concentration from Compus-
tat,”Journal of Corporate Finance, 2017,45(C), 467–479.
Kim, Ginha and James Traina, “Markups, Production Technology, and the Cost of
Capital in Financial Markets,” Working Paper, New York University 2025.
Kim, Kyoo Il, Amil Petrin, and Suyong Song, “Estimating Production Functions with
Control Functions When Capital Is Measured with Error,”Journal of Econometrics,
2016,190(2), 267–279.

87
Kirov, Ivan and James Traina, “Labor Market Power and Technological Change in US
Manufacturing,” PhD Thesis, University of Chicago 2022.
, Paolo Mengano, and James Traina, “Measuring Markups with Revenue Data,”
International Journal of Industrial Organization, 2026,99, 103263.
Klette, Tor Jakob, “Market Power, Scale Economies and Productivity: Estimates from
a Panel of Establishment Data,”The Journal of Industrial Economics, 1999,47(4),
451–476.
and Samuel Kortum, “Innovating Firms and Aggregate Innovation,”Journal of
Political Economy, 2004,112(5), 986–1018.
and Zvi Griliches, “The Inconsistency of Common Scale Estimators When Output
Prices Are Unobserved and Endogenous,”Journal of Applied Econometrics, 1996,11
(4), 343–61.
Koh, Dongya, Ra ¨ul Santaeul `alia-Llopis, and Yu Zheng, “Labor Share Decline and
Intellectual Property Products Capital,”Econometrica, 2020,88(6), 2609–2628.
Kudlyak, Marianna, “How Cyclical Is the User Cost of Labor?,”Journal of Economic
Perspectives, May 2024,38(2), 159–80.
Lenzu, Simone, David Rivers, and Joris Tielens, “Financial Shocks, Productivity, and
Prices,” 2024. Working Paper.
Leontief, Wassily,The Structure of American Economy, 1919–1929: An Empirical Applica-
tion of Equilibrium Analysis, Cambridge, MA: Harvard University Press, 1941.
Lev, Baruch,Intangibles: Management, Measurement, and Reporting, Brookings Institu-
tion Press, 2001.
Levinsohn, James and Amil Petrin, “Estimating Production Functions Using Inputs
to Control for Unobservables,”Review of Economic Studies, 2003,70(2), 317–41.
Liu, Ernest and Aleh Tsyvinski, “A Dynamic Model of Input–Output Networks,”
Review of Economic Studies, 01 2024,91(6), 3608–3644.

88
Liˇzal, Lubom´ır and Kamil Galuˇsˇc´ak, “The Impact of Capital Measurement Error Cor-
rection on Firm-Level Production Function Estimation,” Technical Report 1026,
William Davidson Institute, University of Michigan 2012.
Macchiavello, Rocco and Ameet Morjaria, “Relational Contracts: Recent Empirical
Advancements and Open Questions,” LSE Research Online Documents on Eco-
nomics 123003, London School of Economics and Political Science, LSE Library
Nov 2023.
Manning, Alan,Monopsony in Motion: Imperfect Competition in Labor Markets, Prince-
ton University Press, 2003.
Marschak, Jacob and William H Andrews, “Random Simultaneous Equations and the
Theory of Production,”Econometrica, 1944,12(3/4), 143–205.
McAdam, Peter, Philipp Meinen, Chris Papageorgiou, and Patrick Schulte, “Returns
to Scale: New Evidence from Administrative Firm-Level Data,” Working Paper,
Deutsche Bundesbank 2024.
Melitz, Marc, “The Impact of Trade on Intra-Industry Reallocations and Aggregate
Industry Productivity,”Econometrica, 2003,71(6), 1695–725.
Menzio, Guido, “Markups: A Search-Theoretic Perspective,”Journal of Political Econ-
omy, 2025. Forthcoming.
Miller, Nathan H., Marc Remer, Conor Ryan, and Gloria Sheu, “Understanding the
Price Effects of the MillerCoors Joint Venture,”Econometrica, 2017,85(6), 1763–
1791.
Mundlak, Yair, “Empirical Production Function Free of Management Bias,”Journal of
Farm Economics, 1961,43(1), 44–56.
Olley, Steven and Ariel Pakes, “The Dynamics of Productivity in the Telecommuni-
cations Equipment Industry,”Econometrica, 1996,64(6), 1263–97.
Ornaghi, Carmine, “Assessing the Effects of Measurement Errors on the Estimation
of Production Functions,”Journal of Applied Econometrics, 2006,21(6), 879–891.

89
Peters, Michael, “Heterogeneous Markups, Growth, and Endogenous Misallocation,”
Econometrica, 2020,88(1), 305–43.
Raval, Devesh, “Testing the Production Approach to Markup Estimation,”Review of
Economic Studies, 2023,90(1), 1–36.
Restuccia, Diego and Richard Rogerson, “Policy Distortions and Aggregate Produc-
tivity with Heterogeneous Establishments,”Review of Economic Dynamics, 2008,11
(4), 707–20.
and , “The Causes and Costs of Misallocation,”Journal of Economic Perspectives,
August 2017,31(3), 151–74.
Robinson, Joan,The Economics of Imperfect Competition, 2 ed., London: Macmillan,
1933. Originally published in 1933; reprint edition 1969. Palgrave Economics &
Finance Collection, Economics and Finance (R0).
Rogerson, Richard, Robert Shimer, and Randall Wright, “Search-Theoretic Models of
the Labor Market: A Survey,”Journal of Economic Literature, 2005,43(4), 959–988.
Romer, Paul, “Endogenous Technological Change,”Journal of Political Economy, 1990,
98(5, Part 2), S71–S102.
Rosen, Sherwin, “Implicit Contracts: A Survey,”Journal of Economic Literature, 1985,
23(3), 1144–1175.
Rotemberg, Julio J. and Michael Woodford, “Dynamic General Equilibrium Models
with Imperfectly Competitive Product Markets,” in Thomas F. Cooley, ed.,Frontiers
of Business Cycle Research, Princeton, New Jersey: Princeton University Press, 1995,
pp. 243–293.
and , “The Cyclical Behavior of Prices and Costs,” in J. B. Taylor and M. Wood-
ford, eds.,Handbook of Macroeconomics, Vol. 1, Amsterdam: North-Holland, 1999,
chapter 16, pp. 1051–1135.
Rubens, Michael, “Market Structure, Oligopsony Power, and Productivity,”American
Economic Review, 2023,113(9), 2382–2410.

90
Ruzic, Dimitrije, “The Factor Bias of External Inputs: Implications for Substitution
between Capital and Labor,” 2024. Working Paper.
and Sui-Jade Ho, “Returns to Scale, Productivity Measurement, and Trends in U.S.
Manufacturing Misallocation,”Review of Economics and Statistics, 2021,103(1), 23–
37.
Sato, Kazuo, “A Two-Level Constant-Elasticity-of-Substitution Production Func-
tion,”Review of Economic Studies, 1967,34(2), 201–218.
Schmalensee, Richard, “Inter-Industry Studies of Structure and Performance,” in
Richard Schmalensee and Robert D. Willig, eds.,Handbook of Industrial Organiza-
tion, Vol. 2, Elsevier, 1989, pp. 951–1009.
Solow, Robert, “Technical Change and the Aggregate Production Function,”Review
of Economics and Statistics, 1957,39(3), 312–20.
Syverson, Chad, “What Determines Productivity?,”Journal of Economic Literature,
2011,49(2), 326–65.
, “Markups and Markdowns,”Annual Review of Economics, 2025,17, 57–76.
Traina, James, “Is Aggregate Market Power Increasing? Production Trends Using
Financial Statements,” Working Paper, Stigler Center 2018.
van Heuvelen, Gerrit Hugo, Leon Bettendorf, and Gerdien Meijerink, “Markups in a
Dual Labour Market: The Case of the Netherlands,”International Journal of Indus-
trial Organization, 2021,77(C), 102762.
Van Reenen, John, “Increasing Differences Between Firms: Market Power and the
Macro-Economy,” in “Changing Market Structures and Implications for Monetary
Policy,” Federal Reserve Bank of Kansas City, 2018. Jackson Hole Symposium.
Yeh, Chen, Claudia Macaluso, and Brad Hershbein, “Monopsony in the US Labor
Market,”American Economic Review, July 2022,112(7), 2099–2138.
