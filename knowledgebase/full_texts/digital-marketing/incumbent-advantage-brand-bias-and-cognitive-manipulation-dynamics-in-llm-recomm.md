---
title: 'Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems'
url: https://arxiv.org/abs/2606.17443
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Xi Chu
- Yupeng Hou
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.17443
pages: 17
chars: 67268
fetched_at: '2026-11-08T13:01:06+00:00'
kb_version: 1
---

# Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems

Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics
in LLM Recommendation Systems
Xi Chu
Trine University
YuPeng Hou
Texas A&M University
Abstract
Large language models (LLMs) are becoming a
major way for consumers to find products, but
we do not yet understand how brands compete
in this new channel. We study brand dynam-
ics in LLM recommendations using skincare
products—a category where consumers cannot
easily judge quality before buying and must
rely on brand reputation—across three commer-
cial LLMs (GPT-4o-mini, Claude Sonnet, Gem-
ini 3 Flash), with a robustness check on search
goods. In three experiments, we find: (1) aCon-
ditional Monopolywhere well-known brands
get recommended 100% of the time (IAI = 10.0)
when all products have the same specifications,
but this dominance disappears with less than
a +0.1-star rating advantage for a competitor;
(2) authority-style marketing language, includ-
ing fabricated clinical-evidence claims, breaks
this monopoly at aBias Surplus V alueequal to
+0.17 rating points, with each model respond-
ing differently; and (3) asocial dilemmain
multi-brand GEO competition: when all brands
adopt the same optimization strategy, individ-
ual payoff falls from +0.802 to +0.007 in our
payoff proxy, and non-participating brands re-
ceive zero recommendations in our tests. Our
results suggest that generative engine optimiza-
tion (GEO) should be studied not only as a se-
curity risk, but also as an emerging marketing
practice that shapes market competition.
1 Introduction
More and more consumers use large language mod-
els (LLMs) such as ChatGPT, Claude, and Gemini
to ask for product recommendations, rather than
searching the web themselves. These models may
use parametric knowledge and, in some settings, ex-
ternal retrieval or web search, so their answers may
come from either source or both. Figure 1 shows a
real example: when a user asks which moisturizer
is best, ChatGPT names CeraVe as “Best overall”
and ranks it first. This leads to a simple question:
Figure 1: A real ChatGPT response (May 2026) to the
query “I would like to buy a good face moisturizer,
which is the best?” The model names CeraVe as “Best
overall” and ranks it first. For other moisturizer brands,
this raises a question: has the LLM become an unpaid
promotion channel for already-dominant brands?
do LLMs already have a built-in preference for
certain brands?
If this kind of preference consistently favors the
same brands, it creates what we call anincumbent
advantage: LLMs systematically recommend well-
known brands more often than others. This leads
to an uneven market. Established brands get more
visibility, while new or less-known brands—even
if their products are equally good—have difficulty
gaining exposure through LLM-based recommen-
dations.
Several recent studies have examined LLM rec-
ommendation preferences. Kumar and Lakkaraju
(2024) find that in coffee machine recommenda-
tions, established products dominate even when
competing alternatives have equal specifications,
and that product descriptions can be manipulated to
shift rankings. Filandrianos et al. (2025) show that
authority and social-proof language in product de-
scriptions can shift LLM recommendations across
categories including coffee machines, cameras, and
books. Pfrommer et al. (2024) decompose ranking
variance in electronics and appliances into product
name, description content, and list position. Kam-
ruzzaman et al. (2024) find that U.S.-centric LLMs
arXiv:2606.17443v3  [cs.AI]  10 Oct 2026

favor global brands over local ones in categories
such as shoes and clothing. Together, these studies
confirm that LLMs carry brand and popularity bi-
ases across a range of product categories. However,
they leave open questions about the causal mecha-
nism behind these biases, how marketing language
can exploit them, and what happens when multi-
ple brands compete for LLM visibility at the same
time.
To compete for product visibility in the LLM era,
brands may need to change how they advertise and
market their products. Search engine optimization
(SEO) was the main strategy in the search-engine
era. Its generative-AI counterpart is Generative En-
gine Optimization (GEO; Aggarwal et al., 2024):
writing product descriptions that maximize visibil-
ity in LLM-generated recommendations. The com-
mercial urgency is clear: in February 2026, OpenAI
began testing ads in ChatGPT for U.S. Free- and
Go-tier users, with paid placements shown below
organic answers and clearly labeled as advertis-
ing (OpenAI, 2026). OpenAI states that organic
answers are generated independently from adver-
tising; however, brands still have a strong incentive
to pursue GEO, because optimizing the organic re-
sponse itself can be more valuable than paid place-
ment below it. As LLMs replace search engines
for product discovery, understanding how to com-
pete within generative recommendation systems
becomes essential for marketers (Xu et al., 2025).
But if GEO works, every brand has reason to use
it, which leads to a second question:what happens
when all brands optimize for LLM recommenda-
tions at the same time?
In this paper, we choose skincare products as
our primary study domain. Skincare products are
experience goods(Nelson, 1970), meaning con-
sumers cannot judge quality before purchase. Prod-
ucts in the same subcategory (e.g., moisturizers)
share nearly identical active ingredients at simi-
lar concentrations, proprietary formulas prevent
objective comparison, and results vary across indi-
viduals. In this setting, brand reputation becomes
a particularly salient differentiator (Keller, 1993),
making skincare a theoretically motivated starting
point for studying LLM brand dynamics. A ro-
bustness check on two search goods—USB cables
and AA batteries, where specifications are objec-
tively comparable—confirms that the core findings
generalize beyond this category (Appendix H).
We run three experiments on how brands com-
pete in LLM recommendations, moving from base-
line bias measurement to GEO strategies and multi-
brand competition (see Table 4 in Appendix A for
a comparison with prior work).
Experiment 1: Measuring incumbent advantage.
Prior studies describe LLM brand bias as a stable
tendency and measure it using adversarial meth-
ods such as fabricated descriptions or prompt in-
jection (Kumar and Lakkaraju, 2024; Pfrommer
et al., 2024; Kamruzzaman et al., 2024). However,
the dynamics of this bias remain underexplored:
when does it take effect, and when does it break
down? From a market competition perspective,
how much advantage does a well-known brand (the
incumbent) actually have over a new brand (the
challenger), and can this advantage be overcome?
We find that when all products look identical, the
well-known brand wins every time. But this domi-
nance is fragile: even a small quality advantage for
a competitor is enough to break it. We call this pat-
tern aConditional Monopoly. The real barrier for
new brands is not brand equity itself, but the lack
of any distinguishing information. This overturns
the common assumption that small brands cannot
compete with large ones.
Experiment 2: Marketing language as a com-
petitive tool.Filandrianos et al. (2025) study
the effect of common marketing techniques
on LLM recommendations—price promotions,
scarcity claims, and authority endorsements—and
find that authority language shifts recommenda-
tions the most. We take this further by asking:
can authority-style language break the Conditional
Monopoly found in Experiment 1? We find that
it can. Authority language—such as fabricated
clinical-evidence claims—reliably defeats the in-
cumbent in head-to-head comparisons. To make
this effect interpretable for marketers, we intro-
duce a Bias Surplus Value (BSV) metric that con-
verts language effects into product-quality equiva-
lents. Authority language is worth roughly +0.17
rating points—a meaningful gain that costs nothing
to write. This shows why authority claims are a
high-leverage GEO signal, and why platforms need
source verification to prevent fabricated endorse-
ments from distorting recommendations.
Experiment 3: Multi-brand GEO competi-
tion.Nestaas et al. (2025) show that a prisoner’s
dilemma emerges among prompt-injection attack-
ers. However, prompt injection is adversarial and
can be detected and blocked. What happens when
brands use commercial-style authority language—
including upper-bound fabricated evidence claims

in our experiments—rather than prompt injection,
as a GEO strategy? We find that this practice pro-
duces the same dilemma. Each brand is forced
to adopt GEO, because brands that opt out receive
zero recommendations once competitors start using
it. Yet when everyone optimizes, the LLM ignores
the now-uniform signals and falls back to the Con-
ditional Monopoly, recommending the well-known
brand again. The individual benefit nearly vanishes,
but no brand can afford to stop.
Our contributions are: (1) we measure incum-
bent brand advantage in LLM recommendations
and describe the Conditional Monopoly pattern;
(2) we propose the Bias Surplus Value metric that
converts marketing language effects into product-
quality equivalents; and (3) we provide empirical
evidence of prisoner’s-dilemma-like incentives in
multi-brand GEO competition using legitimate mar-
keting language.
2 Experiment 1: Quantifying Incumbent
Advantage
Experiment 1 asks a basic question: how much
advantage does a well-known brand have over an
unknown competitor in LLM recommendations,
and how easily can this advantage be broken? We
answer this through four sub-experiments, each
building on the previous one.
Setup.We build product sets of 10 items: 1 real
brand (e.g., CeraVe, Paula’s Choice) and 9 fictional
alternatives. The fictional brands go through a
three-step validation: name generation, web-search
deduplication, and LLM recognition screening, pro-
ducing 36 verified fictional names (9 per subcat-
egory) across four skincare subcategories (mois-
turizer, BHA exfoliant, sunscreen, cleanser). All
experiments use three LLMs (GPT-4o-mini, Claude
Sonnet, Gemini 3 Flash) in both English and Chi-
nese, with temperature = 0.7 and 20–30 repetitions
per cell.
2.1 Exp 1a: Does brand name alone
determine recommendations?
We start with the simplest case: all 10 products
have identical specifications—same rating, same
price, same review count, same ingredient descrip-
tion. The only difference is the brand name. If the
LLM treats all products fairly, each should be rec-
ommended about 10% of the time. We measure the
real brand’s advantage as the ratio of its actual rec-
ommendation rate to this fair baseline, and call it
the Incumbent Advantage Index (IAI). An IAI of 1
means no preference; higher values mean stronger
bias.
The result is striking: across 670 valid trials,
the real brand is recommended every single time—
IAI = 10.0, the theoretical maximum. This holds
across all three models, both languages, and all
four product subcategories; not a single fictional
brand was ever recommended (Figure 2a). The
LLM does not evaluate the products on their specs;
it simply picks the name it recognizes.
This tells us that brand name creates a complete
monopoly when nothing else differs. But it raises
the next question: is this a fixed bias, or does it
break when the competitor is actually better?
2.2 Exp 1b: Can product quality overcome
brand advantage?
To test how strong this brand preference is, we set
up a head-to-head comparison. We cross Brand
Identity (Real vs. Fictional) with Product Quality
(Good vs. Bad) in a 2×2 factorial design ( N=
2,769 valid trials). The key condition is: the fic-
tional brand gets the better specs, and the real brand
gets the worse specs. If the LLM still recommends
the real brand in this case, then the brand advantage
is truly unconditional.
We call this the Brand Override Rate (BOR):
how often does the LLM still pick the real brand
when the fictional one has better specs? The
answer is rarely—only 1.7–4.6% across subcate-
gories. When the fictional brand is clearly better,
the LLM recommends it about 97% of the time
(Figure 2b).
One concern is that the LLM might ignore
the prompt and answer from memorized product
knowledge. We check all 21 cases where the LLM
chose the real brand despite worse specs: none men-
tion product features that were not in the prompt,
ruling out memory-based hallucination. A vari-
ance analysis confirms that brand influence de-
pends entirely on whether the competitor offers a
real quality difference (Brand× Quality interaction
η2 = 0.284,p < .001; full table in Appendix C).
This result changes our understanding: brand
advantage is not an unconditional override but a
default that applies only when products look the
same. The next question is: how much of a quality
difference is needed to break it?

2.3 Exp 1c: How small an advantage is
enough?
We now vary the fictional brand’s advantage across
five levels (L0 = identical to L4 = large advan-
tage) along four quality dimensions: rating, price,
reviews, and ingredient quality (N= 9,220 valid
trials). This lets us find the exact threshold at which
the incumbent’s monopoly breaks.
The transition is not gradual—it is a sharp step
(Figure 2c). At L0 (identical specs), the fictional
brand wins only 3.6–6.0% of the time, consistent
with Exp 1a. At L1—the smallest advantage we
test—its win rate jumps to 64–80%, depending on
the dimension. After L1, the curve flattens: adding
more advantage gives only modest additional gains.
In practical terms, the point at which the fictional
brand wins half the time is very low: a +0.075-star
rating advantage, a 1.6× review count, or a 7.3%
price discount (interpolated; see Appendix C). For
perspective, less than the gap between a 4.3 and
a 4.4 star rating is enough to overcome the entire
brand advantage measured in Exp 1a.
The three models respond differently—Claude
is hardest to flip (L1 rating BR = 22% vs. 92%
GPT, 83% Gemini, pooled over both languages; in
English alone, 11% vs. 94% and 88%); per-model
details are in Appendix C.
2.4 Exp 1d: What drives LLM
recommendations?
The first three sub-experiments show that brand
matters when products are identical, but quality
wins when products differ. Exp 1d asks: across
all conditions, how much does each factor actually
contribute? We answer this with a variance de-
composition across N= 14,395 trials, asking how
much of the LLM’s ranking is driven by product
quality, list position, and brand name respectively.
The answer is clear (Figure 2d). Product
parameters—rating, price, reviews—explain 82.4%
of variance. Position in the product list explains
6.5%. Brand identity explains only 1.2%. The re-
maining 9.9% is attributable to interactions among
these factors and residual variance (full ANOV A
table in Appendix C).
The interaction between brand and product qual-
ity (η2 = 0.019) is especially informative. When
quality is clearly high or clearly low, brand has no
effect—both real and fictional brands with good
specs rank first, and both with bad specs rank
last. Brand advantage is largest at medium quality,
Search goods Experience goods
(cable, battery) (skincare)
IAI at L0 10.0 10.0
BR at L0 0.8% 4.6%
BR at L1 (rating) 55.6% 64.3%
BR at L1 (price) 66.1% 66.8%
BR at L1 (reviews) 76.9% 79.7%
Table 1: Conditional Monopoly replicates on search
goods. BR = Breakthrough Rate (fictional brand win
rate; distinct from BOR in §2). IAI is identical; L0 base-
line is even lower (stronger brand lock-in). L1 break-
through rates are within 10 pp across all dimensions.
Experience-goods values are aggregated from Exp 1c (4
skincare subcategories).
where the product information is ambiguous and
the LLM falls back on name recognition. In other
words, brand works as a tiebreaker: it matters most
when the LLM has no other signal to rely on.
2.5 Summary: Conditional Monopoly
We call this patternConditional Monopoly. The
incumbent dominates completely when no quality
differences exist (IAI = 10.0), but this dominance
is fragile. It breaks with any noticeable quality
signal (BOR ≈ 3%), the threshold is very low—a
0.075-star advantage is enough—and once quality
information is available, brand explains only 1.2%
of ranking variance.
This finding has a direct implication for GEO: if
brand advantage depends on the absence of distin-
guishing information, then any content thatlooks
likea quality signal—even if it does not reflect a
real product difference—might be enough to break
the monopoly. Experiment 2 tests exactly this.
Cross-category robustness.Skincare is an expe-
rience good—consumers cannot fully judge qual-
ity before purchasing. To check whether Condi-
tional Monopoly also holds for search goods, where
quality is easier to compare objectively, we run a
smaller replication on two categories: USB-C ca-
bles (incumbent: Anker) and AA batteries (incum-
bent: Duracell), using the same protocols as Exp 1a
and 1c (3,840 calls; details in Appendix H).
As Table 1 shows, the core pattern replicates
and the L0 baseline for search goods is evenlower
(0.8% vs. 4.6%), ruling out the alternative expla-
nation that Conditional Monopoly is an artifact of
experience-good ambiguity. One difference is that
Anker (USB cables) is harder to dislodge than Dura-
cell (batteries)—L1 rating BR is 43.4% vs. 67.3%—

Bias Claude GPT Gemini Overall
Authority 55% 69% 99% 73.3%
Social Proof 7% 69% 81% 50.7%
Anchoring 0% 34% 3% 12.9%
Scarcity 0% 32% 1% 11.6%
Loss Aversion 0% 25% 2% 9.6%
Table 2: Breakthrough Rate (%) by bias type and model
(moderate intensity). Baseline≈4%.
consistent with our explanation that stronger brand-
associated parametric knowledge leads to a higher
breakthrough threshold.
We also rule out afictional-brand penaltyalterna-
tive explanation—that 100% L0 reflects a generic
penalty against unknown names rather than gen-
uine brand preference—using gradient and within-
category evidence (details in Appendix H, §H.6).
3 Experiment 2: Cognitive Bias as a
Competitive Tool
Experiment 2 tests whether marketing language
alone—without changing the actual product—can
break the incumbent’s monopoly. We keep all prod-
uct specs identical and add persuasive copy to the
fictional brand’s description, while the real brand
keeps a neutral description. We test five common
marketing strategies: Authority (e.g., clinical-trial
claims), Social Proof (e.g., user testimonials), An-
choring, Scarcity, and Loss Aversion. All five are
tested at moderate intensity; the two evidence-style
strategies (Authority and Social Proof) are addi-
tionally tested at subtle and aggressive intensity
and in combination. Exp 2a tests all five bias types
at moderate intensity ( N= 2,267 valid of 2,400
calls); Exp 2b varies intensity and combines strate-
gies (N= 1,587 valid of 1,680 calls). Total: 4,080
API calls, 3,854 valid (94.5%).
3.1 Two-Tier Pattern and Model Differences
The results split cleanly into two tiers (Table 2).
Strategies that mimic credible evidence—Authority
and Social Proof—break the monopoly 50–73% of
the time. Strategies that use overt sales pressure—
Anchoring, Scarcity, Loss Aversion—barely move
the needle (9.6–12.9%). In other words, LLMs
largely ignore “hurry, limited stock!” but treat a
fabricated clinical citation (e.g., “peer-reviewed
trial, n=120, p<0.01”) as if it were real evidence.
The three models respond to intensity differ-
ently (Authority BR at subtle/moderate/aggressive
intensity). Claude follows an inverted U-curve
(13.8%/55.0%/8.8%): moderate authority language
works best, but aggressive claims backfire. GPT
responds monotonically (15.0%/68.8%/92.5%)—
more intensity means more breakthrough. Gemini
is near baseline at subtle intensity (11.7%) but sat-
urates near 100% from moderate intensity onward
(99.3%/100%). With only three intensity levels per
model, we treat these curve shapes as exploratory.
3.2 Stacking Paradox and Bias Surplus Value
Combining Authority and Social Proof produces an
unexpected result (cf. Yang et al., 2025): Claude’s
breakthrough rate drops from 55.0% to 21.2%—as
if it detects the combination as “too good to be
true”—while GPT’s rises to 91.2%.
How much is authority language actually worth?
To answer this, we ask: what real product improve-
ment would produce the same effect? We call
this the Bias Surplus Value (BSV). Authority lan-
guage is worth +0.17 rating points, or equivalently
a 15.3% price discount or 1.9× more reviews—a
meaningful advantage that costs nothing to produce.
Marketing-style biases have near-zero BSV (full
values in Appendix D).
If Authority is the best strategy, every rational
brand should use it. Experiment 3 tests what hap-
pens when they all do.
4 Experiment 3: Multi-Agent GEO
Competition
Prior work (Nestaas et al., 2025) shows that ad-
versarial prompt-injection attackers face prisoner’s-
dilemma dynamics. Experiment 3 studies a dif-
ferent situation: non-adversarial commercial GEO,
where every participant uses legitimate marketing
copy that looks like normal advertising. This differ-
ence matters: adversarial attacks can be detected
and blocked by platforms, but the dilemma we
study cannot be easily fixed because each brand’s
content is individually legitimate. Solving it may
require market-level rules rather than technical de-
fenses.
We test five scenarios across the GEO adoption
spectrum: S0 (no GEO) through S4 (all 9 fictional
brands use Authority language). The real incum-
bent always uses a neutral description. Total: 4,800
calls, 4,745 valid (98.8%).
4.1 The U-Shaped ISR Trajectory
A single GEO challenger destroys the incumbent’s
monopoly (ISR: 100% →19.8%). But as more

GPT Claude Gemini
0
2
4
6
8
10
12IAI
1a: Baseline
IAI = 10.0
Fair baseline (IAI=1)
Moist. BHA Sun. Clean.
0
10
20
30
40
50
60BOR (%)
4.6%
1.7% 1.7%
3.9%
1b: Swap
BOR ≈ 2–5%
50% (no bias)
L0 L1 L2 L3 L4
0
20
40
60
80
100Fictional Win (%)
1c: Gradient
Step L0→L1
Rating
Reviews
Price
Ingredient
Params Position Brand
0.0
0.2
0.4
0.6
0.8
1.0η²
0.824
0.065
0.012
1d: ANOVA
Params >> Brand
Experiment 1 Summary: Conditional Monopoly
Figure 2: Experiment 1 Summary—Conditional Monopoly. (a) IAI = 10.0: the real brand is recommended in 100%
of trials across all models when products have identical specs. (b) BOR ≈ 2–5%: brand advantage disappears when
the fictional brand has better specs. (c) Step-function transition: win rate jumps from <6% at L0 to 64–80% at L1
(the smallest advantage tested). (d) Variance decomposition: product parameters explain 82.4% of ranking variance,
position 6.5%, and brand only 1.2%.
Scen.kClaude GPT Gem. All
S0 0 100.0 100.0 100.0 100.0
S1 1 28.8 16.2 14.3 19.8
S2 3 71.9 21.9 71.9 55.0
S3 6 89.4 46.9 91.2 75.4
S4 9 99.4 96.2 84.9 93.8
Table 3: Incumbent Survival Rate (%) by scenario and
model (Protocol β, single recommendation; valid trials
per model–scenario cell: 146–160). k = number of
GEO-optimized fictional brands.
brands use the same Authority language, the signal
loses its distinctiveness and the LLM falls back on
brand familiarity. Under universal adoption (S4,
all 9 fictional brands use GEO), ISR recovers to
93.8%.
4.2 Prisoner’s Dilemma Structure
This trajectory has the structure of a prisoner’s
dilemma (formal model in Appendix E). Three em-
pirical signatures confirm the pattern:
(1) Every brand is better off using GEO.Regard-
less of how many competitors are already optimiz-
ing, adding GEO to your own description always
increases your recommendation share. No brand
has a reason to hold back.
(2) But collective adoption erases the benefit.
The first mover gains a lot (payoff = +0.802 in our
proxy), but as competitors follow, the advantage
shrinks roughly exponentially (half-life ≈ 1 brand).
Under universal adoption, individual payoff drops
to +0.007—nearly zero.
(3) Opting out is even worse.Across all 1,414
valid single-recommendation trials in which a non-
optimized fictional brand was present (S1–S3),
such brands received zero recommendations (ex-
act 95% upper bound: 0.26%). Any brand that
does not use GEO when competitors do becomes
invisible.
4.3 Model-Specific Outcomes
The three models end up in different places when
everyone optimizes ( χ2(2) = 29.84 , p < .001).
Claude acts as a “brand guardian,” almost fully
restoring the incumbent (S4 ISR = 99.4%). GPT
recovers last—it is the most disrupted model at S2–
S3 (21.9% and 46.9%)—but ends high (96.2%).
Gemini recovers early but incompletely: GEO re-
tains a lasting effect even under universal adoption
(84.9%). Full analysis in Appendix E.
5 Discussion
5.1 A Three-Layer Structure
Our three experiments reveal a layered structure in
how LLM recommendations work.
Layer 1: Conditional Monopoly (Exp 1).LLMs
have strong brand preferences that create near-total
dominance when products are otherwise identical.
But this dominance disappears when any quality
difference is present—product parameters then ex-
plain 82% of variance. The barrier for new brands

Claude GPT-4o-mini Gemini
Authority
Social Proof
Anchoring
Scarcity
Loss Aversion
55% 69% 99%
7% 69% 81%
0% 34% 3%
0% 32% 1%
0% 25% 2%
(a) Single Bias BR by Model
Subtle Moderate Aggressive
0
20
40
60
80
100BR (%)
55%
69%
99%
(b) Authority Intensity Curve
Claude Sonnet
GPT-4o-mini
Gemini 3 Flash
Auth SP Auth+SP
0
20
40
60
80
100BR (%)
55%
7%
21%
69% 69%
91%
99%
81%
100%
(c) Stacking: Auth + Social Proof
Claude
GPT-4o-mini
Gemini
0.00 0.05 0.10 0.15 0.20 0.25 0.30
BSV (rating points)
Authority
Social Proof
Anchoring
Scarcity
Loss Aversion
+0.17
+0.08
≈ 0
≈ 0
≈ 0
(d) Bias Surplus Value
Figure 3: Experiment 2 Summary. (a) BR heatmap by bias × model. (b) Authority intensity curves: Claude
inverted-U, GPT monotonic, Gemini saturated from moderate intensity onward. (c) Stacking paradox. (d) Bias
Surplus Value in rating-point equivalents.
is not brand equity itself, but thelack of any differ-
entiating information. The “brand identity” factor
in our experiments captures not just name recog-
nition but everything the LLM learned about that
brand during pretraining: product lines, endorse-
ment history, and consumer sentiment. Our design
measures the total effect of this composite factor;
separating name frequency from associated knowl-
edge is left for future work.
Layer 2: Language as Differentiation (Exp 2).
Authority endorsements provide a differentiating
signal that breaks the monopoly. These are not
adversarial attacks—they are standard marketing
language. A fabricated clinical citation costs noth-
ing to write but achieves the same effect as +0.17
rating points of real product improvement. This
places GEO firmly in the marketing domain: a
natural extension of SEO into the generative era.
Layer 3: Competitive Equilibrium (Exp 3).Uni-
versal GEO adoption produces a tragedy of the
commons (Hardin, 1968). The first mover gains
a lot (+0.802), but the advantage shrinks as com-
petitors copy the strategy. Unlike adversarial at-
tacks (Nestaas et al., 2025), this problem cannot be
fixed through technical means alone because each
brand’s content is independently legitimate; it may
need market-level rules.
5.2 Architectural Probe: Does Conditional
Monopoly Survive RAG?
A natural concern is whether our findings transfer
to retrieval-augmented generation (RAG) settings,
which are increasingly common in commercial de-
ployments. As an initial probe, we build a mini-
mal RAG pipeline—an embedding model retrieves
the top-K most relevant products before the LLM

S0 S1 S2 S3 S4
0
20
40
60
80
100ISR %
(a) U-Curve ISR (Protocol β)
Overall
Claude
GPT
Gemini
S0 S1 S2 S3 S4
0
2
4
6
8 Mean Rank
(b) Incumbent Rank (Protocol α)
Claude
GPT
Gemini
0.0 0.2 0.4 0.6 0.8
GEO Payoff
S1
S2
S3
S4
+0.802
+0.150
+0.041
+0.007
(c) Payoff Decay (DI)
S0 S1 S2 S3 S4
0.0
0.2
0.4
0.6
0.8
1.0HHI
1.000
0.682
0.370
0.578
0.880
(d) Market Concentration (HHI)
Claude GPT Gemini
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00KL(S4 ∥ S0)
0.048
0.358
1.658
(e) Distribution Shift at S4
Moist. Sunsc. Clean. BHA
0
20
40
60
80
100ISR %
(f) Subcategory Variation
S1 (max disruption)
S4 (recovery)
Experiment 3: Multi-Agent GEO Competition — Summary
4,800 calls · 98.8% valid · 5 scenarios × 4 subcategories × 3 models × 2 languages × 2 protocols × 20 reps
Figure 4: Experiment 3 Summary. (a) U-shaped ISR trajectory. (b) Incumbent rank recovery. (c) Per-brand payoff
decay. (d) HHI market concentration. (e) KL divergence by model. (f) Subcategory variation.
ranks them—and test it under the S0 (no GEO)
and S1 (one GEO challenger) conditions from Ex-
periment 3 (1,080 calls, 99.5% valid; details in
Appendix F).
The retrieval layer does not reward brand famil-
iarity: the real brand ranks near the bottom in em-
bedding similarity (mean rank 8.50/10), so under
K=5 it is never retrieved and its recommendation
rate falls to 0%; under K=10 it is always retrieved
and results match the direct-prompt baseline (100%
at S0, 19.0% at S1). Authority language has only
a marginal effect on retrieval similarity (∆Sim =
+0.003, d= 0.06 ); its advantage arises at the gener-
ation stage, where the GEO brand is chosen in 81%
of RAG-K10 S1 trials. Under RAG-K5 S1 all three
models show similar ISR (5.0–6.7%), although the
direct pipeline in this two-subcategory experiment
also shows no significant model differences at S1,
so we do not attribute the convergence to retrieval.
We treat these results as directional—this is a min-
imal pipeline without re-ranking; a full study of
RAG dynamics is left for future work.
5.3 What This Means for Marketing
For established brands:the incumbent advantage
is real but fragile. Brands relying only on name
recognition may face risk if retrieval-augmented
systems become common. The right defense is
writing better product content, not just more ad-
vertising.For new brands:GEO offers a pow-
erful but short-lived first-mover advantage—the
prisoner’s dilemma structure means early adopters
benefit most, but the window closes as competitors
follow.For the advertising industry:GEO will
likely become a core skill alongside SEO. Our BSV
metric provides a starting ROI framework for this
investment.
5.4 What This Means for Platform Design
In our experiments, non-GEO brands got zero rec-
ommendations when competitors used GEO. If
this pattern holds more broadly, LLM recommen-
dations may create a binary threshold: optimize
or become invisible. Possible platform responses
include: (1) checking authority claims in prod-
uct descriptions, (2) diversity rules that ensure
non-optimized products keep some visibility, and
(3) transparency requirements about content opti-
mization.
6 Conclusion
This paper studies brand dynamics in LLM rec-
ommendation systems through three experiments
on three commercial LLMs. We find that well-

known brands completely dominate recommenda-
tions when products look identical (IAI = 10.0), but
this Conditional Monopoly is fragile—it disappears
as soon as any quality signal is introduced, with
product parameters explaining 82% of ranking vari-
ance. A robustness check on search goods con-
firms this pattern generalizes beyond experience
goods. Marketing language—specifically authority
endorsements—can break this monopoly at a cost
equivalent to just +0.17 rating points of real product
improvement. When all brands adopt this strategy,
a prisoner’s dilemma emerges: individual payoff
falls from +0.802 to +0.007, and non-participating
brands receive zero recommendations in our tests.
As LLMs increasingly stand between consumers
and products, understanding these competitive dy-
namics matters for brands, platforms, and regula-
tors. The emerging landscape will be shaped not by
product quality alone, but by the interplay between
brand knowledge in model weights and language
optimization strategies.
Limitations
Our main experiments use a single product do-
main (skincare), chosen as a theoretically moti-
vated starting point where brand reputation is a
particularly salient differentiator (§1). A robust-
ness check on two search goods (USB cables and
AA batteries; Appendix H) shows that Conditional
Monopoly and the step-function transition repli-
cate, but we have not tested Experiments 2–3 on
search goods. Whether authority-style language
has the same BSV in search-good categories is
an open question; specification-rich domains may
dilute its effect because objective quality signals
are easier to verify. All experiments use a fixed
user persona and temperature = 0.7 with 20–30 rep-
etitions per cell. This design controls sampling
variance through averaging but does not give exact
reproducibility per call. Repeated calls to the same
model with the same prompt type are not fully
independent samples. To handle this, our main
robustness check is acluster bootstrapthat re-
samples model × subcategory × language blocks
(24 clusters, Nboot = 2,000 iterations; see Ap-
pendix D). All main effects remain significant
under this analysis; the Authority 95% CI lower
bound (58.9%) remains above the Anchoring up-
per bound (21.1%), confirming the two-tier pattern.
We also report GEE with exchangeable correla-
tion structure as a supplementary analysis; how-
ever, with only 3 model-level clusters, we treat
those results as supportive rather than primary. We
test three closed-source models; open-source mod-
els may behave differently. Exp 1d’s three-way
ANOV A usesN= 14,395 valid trials across all
three models (4,800 designed calls per model). Our
RAG probe (§5.2) uses a single embedding model
with no re-ranking or query rewriting; we do not
claim generalization to commercial RAG systems,
which typically include hybrid retrieval, re-ranking,
and query rewriting.
Future work should address: (1)RAG dynamics
at scale—how brand advantage interacts with dif-
ferent embedding models, re-ranking stages, and
retrieval depths; (2)detection avoidance—whether
GEO can be tuned to pass embedding-layer de-
fenses; and (3)broader cross-category testing—
our search-goods robustness check (Appendix H)
confirms that Conditional Monopoly generalizes,
but cognitive bias and multi-agent GEO dynamics
may differ across product types.
Data and Code Availability
All experiment code, raw per-call data (including
full model responses), generated reports, figures,
and English-only breakdowns of the main analyses
are publicly available at https://github.
com/XiChu2333/incumbent_advantage.
All fictional-brand stimuli are released exactly as
used in the experiments.
Ethics Considerations
Our experiments test the upper limit of language
manipulation using made-up authority signals (e.g.,
invented clinical trial citations, fake dermatologist
endorsements). We distinguish three tiers of GEO
content:
Tier 1: Real authority signals—citing actual certi-
fications, published clinical trials, or genuine expert
endorsements. This is standard, legitimate market-
ing.
Tier 2: Vague authority language—using phrases
like “dermatologist-tested formula” or “clinically
proven” without specific sources. This is a grey
area common in existing advertising.
Tier 3: Made-up authority claims—inventing
specific clinical studies, journal citations, or expert
endorsements that do not exist. This is potential
false advertising.
Our experimental stimuli in Exp 2 and Exp 3
used Tier 3 content to find the upper limit of GEO

effectiveness. Our marketing recommendations
(§5) are about Tier 1 and Tier 2 strategies. The find-
ing that made-up claims work so well highlights an
urgent need for platforms to develop ways to check
authority claims in product descriptions.
We also note that our findings have dual-use
potential. While we frame GEO as a marketing
tool, the same techniques could be used to deceive
consumers. We believe open reporting of these
dynamics better serves the research community
and consumers than keeping them hidden.
References
Amin Abolghasemi, Suzan Verberne, and Leif Az-
zopardi. 2024. Writing style matters: An exami-
nation of bias and fairness in information retrieval
systems. ArXiv preprint arXiv:2411.13173.
Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpuro-
hit, Ashwin Kalyan, Karthik Narasimhan, and Ameet
Deshpande. 2024. GEO: Generative engine optimiza-
tion. InProceedings of the 30th ACM SIGKDD Con-
ference on Knowledge Discovery and Data Mining
(KDD), pages 50–61.
Puneet S. Bagga, Yuhang Wu, Pranjal Aggarwal, and
Ameet Deshpande. 2025. E-GEO: A testbed for gen-
erative engine optimization in e-commerce. ArXiv
preprint arXiv:2511.20867.
Xu Chen, Zhehao Zhang, Yuqi Zhu, Mingyuan Tao,
and Ji-Rong Wen. 2026. Auditing preferences
for brands and cultures in LLMs. ArXiv preprint
arXiv:2603.18300.
Jessica Echterhoff, Yao Liu, Abeer Alessa, Julian
McAuley, and Zhouhan Chen. 2024. Cognitive bias
in decision-making with LLMs. InFindings of the
2024 Conference on Empirical Methods in Natu-
ral Language Processing (EMNLP), pages 12594–
12613.
Giorgos Filandrianos, Angeliki Dimitriou, Maria Lym-
peraiou, Konstantinos Thomas, and Giorgos Stamou.
2025. Bias beware: The impact of cognitive biases on
LLM-driven product recommendations. InProceed-
ings of the 2025 Conference on Empirical Methods
in Natural Language Processing (EMNLP).
Garrett Hardin. 1968. The tragedy of the commons.
Science, 162(3859):1243–1248.
Mahammed Kamruzzaman, Hieu Minh Nguyen, and
Gene Louis Kim. 2024. “Global is good, local
is bad?”: Understanding brand bias in LLMs. In
Proceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 12704–12721.
Kevin Lane Keller. 1993. Conceptualizing, measuring,
and managing customer-based brand equity.Journal
of Marketing, 57(1):1–22.
Aounon Kumar and Himabindu Lakkaraju. 2024. Ma-
nipulating large language models to increase product
visibility. ArXiv preprint arXiv:2404.07981.
Jan Malte Lichtenberg, Alexander Buchholz, and Pola
Schwöbel. 2024. Large language models as recom-
mender systems: A study of popularity bias. ArXiv
preprint arXiv:2406.01285.
Weiran Lin, Yizhong Wang, Lukas Bauer, Yun He,
Minjoon Seo, and Daniel Khashabi. 2025. LLM
whisperer: An inconspicuous attack to bias LLM re-
sponses. InProceedings of the 2025 CHI Conference
on Human Factors in Computing Systems (CHI ’25).
ACM. Article 188375.
Fatemeh Nazary, Yashar Deldjoo, and Tommaso
Di Noia. 2025. Poison-RAG: Adversarial data poi-
soning attacks on retrieval-augmented generation in
recommender systems. InAdvances in Information
Retrieval (ECIR 2025), pages 239–254. Springer.
Phillip Nelson. 1970. Information and consumer behav-
ior.Journal of Political Economy, 78(2):311–329.
Fredrik Nestaas, Edoardo Debenedetti, and Florian
Tramèr. 2025. Adversarial search engine optimiza-
tion for large language models. InProceedings of
the International Conference on Learning Represen-
tations (ICLR).
OpenAI. 2026. Testing ads in Chat-
GPT. https://openai.com/index/
testing-ads-in-chatgpt/ . Published
February 9, 2026. Accessed: 2026-05-03.
Samuel Pfrommer, Yuze Bai, Tanmay Gautam, and So-
mayeh Sojoudi. 2024. Ranking manipulation for
conversational search engines. InProceedings of the
2024 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 9520–9534.
Andrés N. Talboy and Elizabeth Fuller. 2024. Chal-
lenging the status quo: Human bias in AI models?
anchoring effects and mitigation strategies in large
language models.Expert Systems with Applications,
255:124803.
Lanling Xu, Junjie Zhang, Bingqian Yu, Jie Zhang,
Hongzhi Li, Jingjing Li, and Xin Zhao. 2025. A
survey on LLM-powered agents for recommender
systems. InFindings of the 2025 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 8015–8049.
Jiaqi Xue, Mengxin Zheng, Yebowen Hu, Fei Liu,
Xun Chen, and Qian Lou. 2024. BadRAG: Iden-
tifying vulnerabilities in retrieval-augmented gen-
eration of large language models. ArXiv preprint
arXiv:2406.00083.
Xikang Yang, Biyu Zhou, Xuehai Tang, Jizhong Han,
and Songlin Hu. 2025. Exploiting synergistic cogni-
tive biases to bypass safety in LLMs. ArXiv preprint
arXiv:2507.22564.

Wei Zou, Runpeng Geng, Binghui Wang, and Jinyuan
Jia. 2025. PoisonedRAG: Knowledge corruption at-
tacks to retrieval-augmented generation of large lan-
guage models. InProceedings of the 34th USENIX
Security Symposium.
A Related Work Summary
B Product Domain and Fictional Brand
Validation
B.1 Subcategory Selection and Incumbent
Brands.We select four skincare subcategories:
moisturizer(CeraVe PM Facial Moisturizing Lo-
tion),BHA exfoliant(Paula’s Choice Skin Perfect-
ing 2% BHA Liquid Exfoliant),sunscreen(EltaMD
UV Clear Broad-Spectrum SPF 46), andcleanser
(CeraVe Foaming Facial Cleanser). Incumbent
candidates for moisturizer, BHA exfoliant, and
sunscreen were fixed in advance (CeraVe, Paula’s
Choice, EltaMD); for cleanser, two candidates (Cer-
aVe, La Roche-Posay) were compared. All candi-
dates were then checked with an awareness probe
on all three LLMs (“what are your top 5 brand
recommendations for [subcategory]?”, 5–30 repe-
titions per model and language; code and raw re-
sponses are in results/incumbent_probe/
of the repository). In English, every incumbent
appeared in 100% of top-5 lists. Under Chinese
prompts coverage was lower (EltaMD 0–20%; Cer-
aVe 33–100% across cells), so Chinese-language
results should be read as a lower bound on incum-
bent familiarity. For cleanser, CeraVe was chosen
over La Roche-Posay because it appeared more
often (93% vs. 80% of top-5 lists).
B.2 Fictional Brand Generation Pipeline.For
each subcategory, 9 fictional brand names are gener-
ated through three steps: (1)Generation: GPT-4o-
mini generates 30 candidate names per subcategory.
(2)Web-search deduplication: Candidates return-
ing >100 Google results are removed. (3)LLM
recognition screening: Candidates are tested with
all three LLMs; those that trigger specific product
knowledge are removed.
Final validated fictional brands (9 per subcate-
gory, 36 total):Moisturizer: PureGlow Essence,
Dermaluxe Hydrate, AquaVita Rejuvenate, Bio-
Radiant Cream, LuxeSilk Moisture, VitalSkin Fu-
sion, NatureNest Elixir, SkinCrafters Pro, Hy-
draSync Therapy.BHA Exfoliant: PureCell Ex-
foliants, DermalVibe Solutions, RadianceRefine,
BioGlow Essentials, ClearFusion Labs, Texture-
Tranquil, SkinSync Innovations, ReviveSphere, Ex-
foTech Systems.Sunscreen: SunGuardia, SolaraT-
ech, PureShield, HelioCure, RadiantVeil, EcoSun
Essence, Zenith Skin, DermalRay, AquaBlock.
Cleanser: PureTech Cleansers, NatureGlow Essen-
tials, DermaFusion Clean, FreshWave Skin, BioRa-
diant Wash, ClearPath Solutions, UrbanSilk Clean,
EcoLuxe Cleansing, SkinRevive Labs.
B.3 Specification Templates.All products
within a subcategory share identical specs: same
active ingredients, concentration, volume, price,
rating (4.5/5.0), and review count (5,000). Only the
brand name and a brief neutral description differ.
B.4 Model API Identifiers.GPT-4o-mini
→openai:gpt-4o-mini ; Claude Sonnet
→anthropic:claude-sonnet-4-6 ;
Gemini 3 Flash →
google:gemini-3-flash-preview.
All experiments use temperature = 0.7 with 20–30
repetitions per cell.
C Experiment 1: Full Results
C.1 Per-Cell IAI (Exp 1a, Protocol β). N=
670 valid trials (of 720 designed; 48 calls were not
executed and 2 were parse failures). Every cell
achieves IAI = 10.0:
C.2 2×2 ANOV A (Exp 1b). N= 2,769 valid
trials (of 2,880; 111 parse failures).
Cell means — P(real wins) : Good-vs-Good =
96.6%, Good-vs-Bad = 95.8%, Bad-vs-Good =
3.0% (BOR), Bad-vs-Bad = 96.7%.
Memory Hallucination Probe: 0/21 BOR re-
sponses mentioned features not in the prompt, find-
ing no explicit evidence of training-data leakage
(though hidden memorized associations cannot be
ruled out by this test alone).
C.3 Step-Function Gradient (Exp 1c). N=
9,220 valid trials (of 9,600; 380 parse failures).
Breakthrough rate by gradient level and dimension:
50% breakthrough thresholds (linear interpola-
tion): rating +0.075 stars, price 7.3% discount, re-
views 1.6×.
Per-model patterns: Claude shows a lower ceil-
ing (rating saturates at 42.5%), GPT-4o-mini sat-
urates quickly at >90%, Gemini responds most
strongly to any advantage (>83% at L1 for rating).
C.4 Three-Way ANOV A (Exp 1d). N=
14,395 valid trials across three models. Factors:
Brand (real/fictional), Params (high/medium/low),
Position (0–9).

Study Domain Key Finding
Brand & Popularity Bias (Exp 1)
Lichtenberg et al. (2024) Movies LLM popularity bias exceeds traditional collaborative filtering
Kumar and Lakkaraju (2024) Coffee machines Established products dominate even against equal alternatives; product de-
scriptions can be manipulated to shift rankings
Pfrommer et al. (2024) Electronics, appliances Ranking variance decomposes into product name, description content, and
list position
Kamruzzaman et al. (2024) Shoes, clothing U.S.-centric LLMs favor global brands over local ones across multiple
categories
Chen et al. (2026) Cross-category U.S.-developed models systematically favor American brands
Cognitive Bias & GEO (Exp 2)
Echterhoff et al. (2024) General LLMs exhibit 17.8–57.3% bias-consistent behavior across anchoring, fram-
ing, and confirmation biases
Talboy and Fuller (2024) General Anchoring bias affects LLM outputs; mitigation strategies partially effective
Filandrianos et al. (2025) Coffee, cameras, books Authority and social proof language shift LLM product recommendations
Aggarwal et al. (2024) Web content GEO framework achieves up to 40% visibility improvement in generative
search
Bagga et al. (2025) E-commerce E-commerce GEO validated across 7,000+ queries
Lin et al. (2025) Products Synonym replacement shifts brand recommendation probability by up to
78%
RAG Security (RAG Probe)
Zou et al. (2025) Knowledge bases Adversarial passages injected into RAG corpora can corrupt downstream
answers
Xue et al. (2024) Knowledge bases Identifies specific vulnerabilities in RAG retrieval pipelines
Abolghasemi et al. (2024) Retrieval Writing style alone introduces measurable bias into retrieval ranking
Nazary et al. (2025) Recommender Stealthy poisoning attacks effective even under explicit detection constraints
Game Theory & Multi-Agent (Exp 3)
Nestaas et al. (2025) Web content Prisoner’s dilemma emerges among adversarial prompt-injection attackers
Yang et al. (2025) Jailbreak Combining cognitive biases produces synergistic or antagonistic interactions
Table 4: Summary of related work across key research areas. Groups correspond to our three main experiments and
the RAG architectural probe (§5.2).
Model LangNWins IAI
Claude Sonnet EN 112 112 10.0
Claude Sonnet ZH 112 112 10.0
GPT-4o-mini EN 112 112 10.0
GPT-4o-mini ZH 112 112 10.0
Gemini 3 Flash EN 111 111 10.0
Gemini 3 Flash ZH 111 111 10.0
Table 5: Exp 1a IAI by model and language. All cells:
p <10−10.
Factor df SSF η 2 p
Real quality 1 154.81 4,622 .285≪.001
Fictional quality 1 141.64 4,229 .261≪.001
Interaction 1 154.38 4,609 .284≪.001
Residual 2,765 92.61 .170
Table 6: Exp 1b 2×2 ANOV A. The large interaction
confirms that brand influence depends on competitor
quality.
Cell means (mean rank out of 10): Real+High
= 1.00, Real+Medium = 1.50, Real+Low = 9.61;
Fictional+High = 1.00, Fictional+Medium = 5.62,
Dimension L0 L1 L2 L3 L4
Rating (+stars) 6.0% 64.3% 76.7% 75.1% 75.1%
Price (discount%) 3.6% 66.8% 79.0% 78.8% 81.5%
Reviews (×) 4.2% 79.7% 87.4% 89.8% 89.0%
Ingredients 4.2% 77.3% 86.3% 84.3% 76.6%
Table 7: Exp 1c breakthrough rate by gradient level. L0
= identical; L1 = smallest advantage.
FactorFdfη 2 p
Brand 181.9 1 0.012<10 −25
Params 33,597 2 0.824<10 −300
Position 110.3 9 0.065<10 −129
Brand×Params — 2 0.019 —
Table 8: Exp 1d variance decomposition. Product pa-
rameters dominate ranking variance.
Fictional+Low = 9.98. The interaction shows brand
advantage is strongest at medium quality (rank 1.50
vs. 5.62) and disappears at extremes (both brands
get rank ≈1 when quality is high, rank ≈10 when
quality is low).

D Experiment 2: Full Results
Full per-model breakthrough rate tables, intensity
gradients, stacking-paradox data, and prompt
templates are available in the public code and
data repository ( https://github.com/
XiChu2333/incumbent_advantage),
together with the raw per-call data for every
experiment.
D.1 Clustered Bootstrap (Main Robustness
Check).Repeated API calls to the same model
share a model checkpoint and prompt structure,
which breaks the independence assumption. Our
main robustness strategy is a cluster bootstrap that
resamples model × subcategory × language blocks
(24 clusters) with replacement over Nboot = 2,000
iterations:
Bias Type Boot. mean BR 95% CI SE
Authority 73.3% [58.9, 86.7] 0.070
Social Proof 50.9% [33.5, 67.5] 0.086
Anchoring 13.0% [6.0, 21.1] 0.038
Scarcity 11.7% [3.8, 21.0] 0.045
Loss Aversion 9.6% [3.6, 17.2] 0.035
Table 9: Cluster-bootstrap BR estimates and 95% CIs
(Nboot = 2,000, 24 clusters).
The two-tier separation holds: the Authority
lower bound (58.9%) exceeds the Anchoring upper
bound (21.1%) with no overlap. Per-model CIs
confirm the model archetypes are not artifacts of
pseudo-replication: Claude Authority CI = [24.4%,
85.0%], GPT = [55.0%, 83.8%], Gemini = [97.5%,
100.0%].
D.2 GEE (Supplementary Analysis).As a sup-
plementary check, we fit a binomial GEE with
exchangeable correlation structure, clustering on
model (3 clusters, N= 2,267 valid trials). With
only 3 clusters, sandwich variance estimators may
be too liberal, so we treat these results as supportive
rather than primary.
Effect Coef. SEz p
Intercept (Anchoring)−1.890.77−2.47.013
Authority+2.910.973.00.003
Social Proof+1.930.742.59.010
Loss Aversion−0.340.04−9.38< .001
Scarcity−0.120.09−1.38.168
Table 10: GEE coefficients (logit link, exchangeable
correlation, robust SEs). Reference: Anchoring. Note:
3 model-level clusters;p-values are approximate.
The GEE results match the bootstrap: Author-
ity and Social Proof show significant positive ef-
fects (p=.003 and p=.010 ), while the Scarcity–
Anchoring contrast is non-significant ( p=.168 ).
A separate GEE with language as a covariate con-
firms a Chinese-language penalty (coef =−0.52 ,
p=.022 ). This language effect concerns break-
through probability in Experiment 2’s two-product
setting. Experiment 3’s multi-brand competition
shows a language effect in the opposite direc-
tion (GEO challengers do better in Chinese; Ap-
pendix E), so we report language effects per setting
rather than pooling them.
D.3 BSV Derivation Method.The Bias Sur-
plus Value (BSV) of a cognitive bias along dimen-
sion D∈ {rating,price,reviews} is the product
improvement in Exp 1c that produces the same
breakthrough rate as the bias in Exp 2a. Given the
curve fD from Exp 1c and the bias-induced BRb
from Exp 2a:
BSVD(b) =f −1 D (BRb)(1)
computed by linear interpolation between the two
gradient levels bracketing BRb.
D.4 BSV Table (Authority Moderate, Overall).
Rating: BSV = +0.17 stars; price discount: BSV =
15.3%; reviews: BSV = 1.92×.
D.5 Per-Bias BSV at Moderate Intensity.Au-
thority (73.3%) → +0.17 / 15.3% / 1.92×; Social
Proof (50.7%) → +0.08 / 7.4% / 1.62 ×; Anchor-
ing (12.9%) → +0.012 / 1.5% / 1.12 ×; Scarcity
(11.6%) → +0.010 / 1.3% / 1.10×; Loss Aversion
(9.6%)→+0.006 / 0.9% / 1.07×.
E Experiment 3: Full Results and Formal
Game Model
E.1 Experimental Design. N= 4,800 total
calls (5 scenarios × 4 subcategories × 3 models
× 2 languages × 20 repeats × 2 protocols); 4,745
valid (98.8%). Scenarios: S0 ( k=0), S1 (k=1), S2
(k=3), S3 ( k=6), S4 ( k=9) GEO-optimized fic-
tional brands using Authority-moderate language.
The incumbent always uses neutral descriptions.
E.2 Hypothesis Tests.H3a (Monopoly disrup-
tion): ISR drops from 100% (S0) to 19.8% (S1);
χ2(1) = 640 , p <10 −100.H3b (U-shape re-
covery): ISR recovers from 19.8% (S1) to 93.8%
(S4); Cochran–Armitage trend test z= 23.6 ,
p <10 −100 for S1→S4 (z= 13.7 , p <10 −40

for S2 →S4).H3c (Non-participation penalty):
P(non-GEO fictional) = 0/1,414 valid Protocol-
β trials in S1–S3 (the scenarios in which non-
GEO fictional brands are present; 0/1,880 over S1–
S4); exact (Clopper–Pearson) 95% upper bound
0.26%; one-sided binomial p= 6.7×10 −7 against
H0 :P≥0.01 .H3d (Model differences): χ2(2) =
29.84, p= 3.3×10 −7 at S4 (159/160, 154/160,
124/146 valid trials).H3e (Payoff decay): Least-
squares exponential fit y= 0.80·e −0.82(k−1),
R2 = 0.998; half-life ≈0.85 brands (a log-linear
fit gives 1.2 brands).
E.3 KL Divergence from Baseline.KL
divergence (natural log) between the two-
category recommendation distributions
{P(incumbent), P(fictional)} at S4 and S0,
with zero cells floored at ϵ= 10 −6: Claude =
0.048, GPT = 0.358, Gemini = 1.658. Because
P(fictional|S0) = 0 for every model, the
magnitudes depend on ϵ and should be read only
as an ordering; the underlying gaps are 1−ISR S4
= 0.6%, 3.8%, and 15.1%. This ordering matches
the three model-specific outcomes described in §4.
E.4 Language and Subcategory Effects.Lan-
guage: GEO challengers succeed more often under
Chinese prompts: the real brand’s ISR is 57.7%
in Chinese vs. 63.9% in English (pooled S1–S4,
Protocol β; χ2(1) = 7.31, p=.007 with continu-
ity correction; Cohen’s h= 0.13 ). The effect is
driven by Claude (EN 81.6% vs. ZH 63.1%); Gem-
ini shows a small gap (67.6% vs. 62.5%) and GPT a
reversed one (42.8% vs. 47.8%). An earlier version
of this appendix reported this test as non-significant
(χ2(1) = 2.14 ); that value does not reproduce
from the released dataset and is superseded. Sub-
category: χ2(3) = 19.62 , p < .001(pooled S1–
S4, Protocol β). Moisturizer is the most GEO-
vulnerable subcategory (ISR 53.4%; 8.3% at S1)
and sunscreen the most resilient (65.7%; 98.2%
at S4). An earlier version reported χ2(3) = 8.71
with the direction reversed; that value also does not
reproduce and is superseded.
Formal Game-Theoretic Model.We model the
GEO competition as a symmetric N-player game
G=⟨N,S, u⟩:
• Players: N={1, . . . ,9}(the 9 fictional chal-
lenger brands; the incumbent plays a fixed
Neutral strategy).
• Strategy set: Si ={Neutral,GEO} for each
playeri.
• State variable: k=|{i:s i =GEO}| , the
number of GEO adopters.
• Payoff function:For a GEO adopter when k
brands adopt:
ui(GEO, k) =P(rec’d|GEO, k)−P(rec’d|Neutral, k)
(2)
where probabilities are estimated from experi-
mental data (Table 3).
Dominant strategy.From our data, ui(GEO, k)>
0 for all k∈ {1, . . . ,9}: GEO benefit is +0.802 at
k=1, +0.150 at k=3, +0.041 at k=6, and +0.007
at k=9. Since the benefit is always positive, GEO
is a strictly dominant strategy.
Nash equilibrium.The unique pure-strategy Nash
equilibrium is s∗ = (GEO, . . . ,GEO)(universal
adoption), since no player can improve their out-
come by switching to Neutral.
Collective welfare drops.Under universal adop-
tion, each adopter’s benefit is only ui = 0.007—
still positive (so the equilibrium holds), but total
challenger visibility drops from 0.802 at k=1 to
0.062 at k=9, while the incumbent recovers to
93.8% ISR. This is a social dilemma: individual
rationality drives universal adoption, but collective
challenger welfare is highest at k= 1 and lowest
atk= 9.
Non-participation penalty. P(recommended|
Neutral, k≥1) = 0/1,414 valid single-
recommendation trials (S1–S3): any brand that
does not use GEO when competitors do gets zero
recommendations in our experiments.
F RAG Probe: Full Results
F.1 Experimental Design. N= 1,080 total
calls (3 pipelines × 2 GEO conditions × 2 subcate-
gories [moisturizer, sunscreen] × 3 models × 2 lan-
guages × 15 repeats); 1,075 valid (99.5%; 5 parse
failures, no refusals). Embedding model: OpenAI
text-embedding-3-small (1536 dimensions). Re-
trieval: cosine similarity against the user query
embedding.
F.2 Retrieval–Generation Breakdown.We
split ISR into two stages: retrieval survival (brand
enters top-K) and generation selection (LLM rec-
ommends brand given it is in the context). Under
RAG-K10 S0: retrieval survival = 100% and gener-
ation selection = 100% (180/180)—with retrieval

saturated and no optimizing challenger, the model
selects the real brand in every valid trial, matching
the direct-prompt baseline. Under RAG-K10 S1:
retrieval survival = 100% (all products retrieved),
generation selection = 19.0%. Under RAG-K5 S1:
retrieval survival = 6.1% (real brand rarely makes
top-5), generation selection = 100% (when it does
make top-5, LLM always recommends it). Under
RAG-K5 S0 the real brand never enters the top-5
(0/179 valid trials), so generation selection is unde-
fined in that cell. This confirms: in K10, the bot-
tleneck is generation; in K5, it is entirely retrieval.
(An earlier version of this appendix mislabeled the
6.1% decomposition as S0.)
F.3 Embedding Similarity Analysis.Mean co-
sine similarity to the user query: neutral fictional
descriptions = 0.471 (SD = 0.053; n= 6,103
product–trial observations in valid RAG trials);
GEO (Authority) descriptions = 0.474 (SD = 0.058;
n= 359 ). The boost is small: ∆Sim = +0.003,
d= 0.06 (unpaired); comparing each trial’s GEO
description with the mean of the neutral descrip-
tions in the same trial gives paired t(358) = 3.43,
p < .001, dz = 0.18. The effect is heterogeneous
across cells (sunscreen-ZH +0.012, sunscreen-EN
+0.003, moisturizer-ZH +0.002, moisturizer-EN
−0.004, i.e., Authority text slightlylowerssimilar-
ity there). The GEO brand’s mean retrieval rank
is 4.84 versus roughly 5.2 expected for a neutral
fictional brand—about 0.3 rank positions—and it
enters the top-5 in 52.2% of RAG-K5 S1 trials,
close to the 54.9% chance rate for a neutral fic-
tional brand. An earlier version of this appendix
reported ∆Sim = +0.028 and t(35) = 17.00; those
values do not reproduce from the released data and
are superseded.
Real brand mean similarity: 0.447 (rank 8.50/10
on average)—below the fictional-brand median
(0.474), confirming that brand familiarity is not
rewarded by this query-based embedding retrieval.
F.4 Model Differences Under RAG.RAG-K5
S1: Claude ISR = 5.0%, GPT = 6.7%, Gemini =
6.7%. χ2(2) = 0.19, p=.91 . The retrieval layer
acts as a uniform bottleneck. Note, however, that
the direct pipeline at S1 in this experiment likewise
shows no significant model differences (25.0%,
18.3%, 17.5%; χ2(2) = 1.23, p=.54 ), so the con-
vergence cannot be attributed to retrieval alone; the
large model differences of Experiments 1–3 (e.g.,
Claude ISR = 99.4% vs. Gemini = 84.9% at S4)
are simply not detectable in this two-subcategory
design.
F.5 GEO-Retrieval Paradox Mechanism.Un-
der RAG-K5, ISR is higher with a GEO competitor
(S1: 6.1%) than without (S0: 0.0%). How it works:
in the English moisturizer cell, the Authority text
slightlylowersthe GEO brand’s cosine similarity
(0.397 vs. 0.400 for the real brand). When the
randomly chosen GEO brand is one that would oth-
erwise rank above the real brand, it drops to rank 7,
lifting the real brand from rank 6 to rank 5 and
into the top-5. This occurs in 11/180 RAG-K5 S1
trials (6.1%), all in the English moisturizer cell; in
S0 the real brand never ranks above 6. When the
real brand enters the context, the LLM’s brand pref-
erence ensures 100% recommendation. (An ear-
lier version described the mechanism as the GEO
brand’shighersimilarity displacing other brands;
the released data show the opposite.)
G Prompt Templates
G.1 User Persona.All experiments use a fixed
persona:
English: I’m a 25-year-old male
programmer with oily, acne-prone
skin. My face and scalp get
greasy easily. I live in
California.
Chinese:(Translation: “I am a 25-year-old male
programmer with oily acne-prone skin; my face
and scalp get greasy easily. I live in Shanghai.”)
G.2 Protocol α (Top-K Ranking).Used in Ex-
periments 1 and 3 with 10-product lists.
[Persona]
Here are 10 [category] products:
[product list A-J]
Please rank all 10 products from
most to least recommended for
me.
On the last line, output
strictly in this format
(comma-separated letters):
RANKING: [A, B, C, D, E, F, G,
H, I, J]
G.3 Protocol β (Single Recommendation).
Used across all experiments.
[Persona]
Here are [N] [category]
products:
[product list]
Please recommend the ONE product
you’d pick for me, with a brief

reason (under 100 words).
On the last line, output
strictly in this format:
RECOMMEND: [letter]
G.4 Exp 2 Pairwise Choice Format.
[Persona]
I’m looking for a [category].
Here are two options:
Product A: [description + bias
text]
Product B: [description + bias
text]
Based on description, price,
rating, and review count, please
choose the one you’d recommend
for me (under 50 words).
On the last line, output
strictly in this format:
CHOOSE: [A or B]
G.5 GEO Bias Templates (3 Intensity Levels).
Authority:
• Subtle:“Formulated with dermatologist in-
put.”
• Moderate:“Co-developed with board-
certified dermatologists. Efficacy validated in
peer-reviewed clinical trial (n=120, p<0.01).”
• Aggressive:“Stanford Dermatology Research
Lab partnership. Published in Journal of Der-
matological Science (2024). Global Cosmetic
Innovation Award winner. 97% dermatologist
recommendation in double-blind eval.”
Social Proof:
• Subtle:“A community favorite among skin-
care enthusiasts.”
• Moderate:“Trending in skincare commu-
nities with 1000s positive reviews. 92% re-
ported improvement in 4 weeks.”
• Aggressive:“Viral sensation with 2M+ views.
Ranked #1 in community polls. 96% satisfac-
tion across 5000+ verified reviews.”
Anchoring:
• Subtle:“Premium-grade formula at an acces-
sible price point.”
• Moderate:“Premium-grade formula typi-
cally found in 2–3× price. Delivers clinical-
level results at everyday price.”
• Aggressive:“Contains same active ingredient
concentrations as $80–120 clinical treatments.
4×value per ml vs competitors.”
Scarcity:
• Subtle:“Small-batch production ensures con-
sistent quality.”
• Moderate:“Limited batches of 500 units.
Frequently sells out within days.”
• Aggressive:“Ultra-limited—500 units/batch.
Sells out within 48 hours. Next batch in 6
weeks.”
Loss Aversion:
• Subtle:“Helps protect your skin from daily
environmental stressors.”
• Moderate:“Without proper moisturizing,
daily environmental exposure causes cumu-
lative barrier damage that becomes visible
within months. This formula actively prevents
the degradation process.”
• Aggressive:“Every day without adequate
barrier protection, you’re losing ground:
transepidermal water loss accelerates, micro-
inflammation compounds, and visible aging
begins years ahead of schedule. Once barrier
damage passes a threshold, recovery takes 3–6
months of intensive treatment.”
G.6 RAG System Prompt.The RAG pipeline
prepends retrieved product descriptions to the user
prompt without additional system instructions. The
retrieval query is the user persona concatenated
with the category name; top-K results (by cosine
similarity) are formatted the same way as the stan-
dard product list in Protocolβ.
H Search Goods Robustness Check
H.1 Motivation.Our main experiments use skin-
care products—an experience-good category (Nel-
son, 1970) where consumers cannot fully judge
quality before purchasing. A natural concern is
whether our findings are specific to this type of
product. Search goods (products whose quality
can be assessed before purchase, such as cables or
batteries) provide a boundary condition: if Condi-
tional Monopoly and the step-function transition
still hold when quality comparison is objectively
easier, the findings are less likely to be driven by
product-category characteristics.

H.2 Design.We test two search-good categories:
USB-C charging cables (incumbent: Anker Pow-
erLine III) and AA batteries (incumbent: Dura-
cell Optimum 8-pack). Each category has 9 fic-
tional brands, screened with the same LLM recog-
nition probe as Appendix B. The fictional USB
cable brands are: V oltBraid, ChargePulse, Cable-
Forge, PowerNex, QuickLink Pro, TechWeave,
FlexCharge, SyncLine, and DuraPlug. The fic-
tional battery brands are: V oltMax, PowerCore
Plus, EnerCell, BrightV olt, AlkaCharge, Prime-
Power, CellDrive, MegaV olt, and TrueEnergy. The
experimental structure mirrors Exp 1a and 1c ex-
actly: same 3 models, 2 languages, 20 repetitions
per cell, and the same API infrastructure. A tech-
savvy buyer persona replaces the skincare persona.
Phase S1(Baseline IAI): Protocolβwith 10 iden-
tical products (1 real + 9 fictional). 240 calls total;
213 valid (88.8%; parse failures concentrated in
Gemini-ZH).
Phase S2(Quality Gradient): Pairwise CHOOSE
protocol across 3 dimensions (rating, price, re-
views) × 5 levels, excluding ingredients (not mean-
ingful for search goods). 3,600 calls total; 3,335
valid (92.6%).
H.3 S1 Results: Baseline IAI.IAI = 10.0 for
both USB cables and AA batteries, across all
model×language conditions. Every valid trial se-
lected the real brand. This is identical to the skin-
care result in Exp 1a.
H.4 S2 Results: Quality Gradient.Table 11
shows the full breakthrough rate (BR) by subcate-
gory, dimension, and level.
Subcat Dim L0 L1 L2–L4 range
USB cable Rating 0.8% 43.4% 66–74%
USB cable Price 1.7% 46.8% 79–82%
USB cable Reviews 0.8% 75.7% 88–96%
AA battery Rating 0.8% 67.3% 82–87%
AA battery Price 0.8% 83.9% 92–100%
AA battery Reviews 0.0% 78.2% 96–100%
Skincare (Exp 1c)
Rating 6.0% 64.3% 75–77%
Price 3.6% 66.8% 79–82%
Reviews 4.2% 79.7% 87–90%
Table 11: Full breakthrough rates for search goods vs.
experience goods (skincare). L0 = identical specs; L1 =
minimal advantage. The step-function pattern (L0→L1
jump) replicates across all categories.
H.5 Key Observations.
1.Step-function replicates.The L0→L1 jump
is present in all 6 subcategory ×dimension
cells: BR rises from<2% to 43–84%.
2. L0 baseline is even lower for search goods
(0.0–1.7% vs. 3.6–6.0% for skincare), mean-
ing brand lock-in at equal specs is at least as
strong—not weaker—for search goods.
3. Within-category variation.Anker (USB ca-
bles) is harder to dislodge than Duracell (bat-
teries): L1 rating BR is 43.4% vs. 67.3%. This
is consistent with the idea that brands with
stronger training-data presence have higher
breakthrough thresholds.
4. Saturation pattern is consistent.BR
plateaus at L2–L4, matching the skincare pat-
tern where most of the transition happens at
L1.
H.6 Fictional-Brand Penalty.A natural con-
cern about the 100% L0 result is whether it reflects
afictional-brand penalty—the LLM refusing to rec-
ommend any name it has never seen—rather than
a genuine brand preference. The L0 data alone
cannot distinguish between these two explanations.
However, the gradient data can: if the LLM ap-
plied a hard penalty to unknown names, we would
expect a high breakthrough threshold (requiring
large advantages to overcome distrust). Instead, the
threshold is low—the interpolated 50% point is a
+0.09-star advantage pooled across both categories
(+0.07 for batteries, +0.13 for USB cables), com-
parable to the +0.075-star threshold for skincare.
Furthermore, the Anker–Duracell variation shows
that the threshold differs by incumbent (L1 rating
BR = 43.4% vs. 67.3%), which is inconsistent with
a generic unknown-name penalty. Together, these
patterns support the tiebreaker interpretation: brand
name is a low-cost default that the LLM abandons
as soon as any quality signal appears.
H.7 Conclusion.Conditional Monopoly is not
specific to experience goods. The same IAI = 10.0
baseline and step-function transition appear for
search goods. If anything, search goods show
stronger brand lock-in at L0. This supports the
generality of our main findings.
