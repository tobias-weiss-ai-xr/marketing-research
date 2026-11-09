---
title: 'Beyond Rational Illusion: Behaviorally Realistic Strategic Classification'
url: https://arxiv.org/abs/2605.19674
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Xinpeng Lv
- Yunxin Mao
- Renzhe Xu
- Chunyuan Zheng
- Yikai Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.19674
pages: 29
chars: 103752
fetched_at: '2026-11-08T13:39:03+00:00'
kb_version: 1
---

# Beyond Rational Illusion: Behaviorally Realistic Strategic Classification

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Xinpeng Lv 1 Yunxin Mao1 Renzhe Xu 2 Chunyuan Zheng 3 Yikai Chen 1 Haoxuan Li 3 Yang Shi4
Jinxuan Yang5 Yuanlong Chen6 Yuanxing Zhang4 Shaowu Yang1 Wenjing Yang1 Zhouchen Lin 3
Haotian Wang 1
Abstract
Strategic classification (SC) studies the interac-
tion between decision models and agents who
strategically manipulate their features for favor-
able outcomes. Existing SC frameworks typi-
cally rely on the idealized assumption that agents
are strictly rational. However, evidence from be-
havioral economics and psychology consistently
shows that real-world decision-making is often
shaped by cognitive biases, deviating from pure
rationality. To formalize this limitation, we iden-
tify and define a new problem setting, termed
thebehaviorally realistic strategic classification
problem, where agents’ strategic manipulations
deviate from full rationality due to psychological
biases. Motivated by the identified limitation, we
propose theProspect-Guided Strategic Frame-
work(Pro-SF) to address the problem, a prin-
cipled framework grounded in prospect theory
to model and learn under behaviorally realistic
strategic responses. Specifically, to capture behav-
iorally realistic strategic manipulations, our frame-
work reformulates the Stackelberg-style interac-
tion between agents and the decision-maker by
incorporating three key mechanisms inspired by
prospect theory, including the asymmetry between
benefits and costs, different subjective reference
points, and non-rational probability distortion. Ex-
periments on synthetic and real-world datasets
establish Pro-SF as a behaviorally grounded ap-
proach to strategic classification, bridging ma-
1College of Computer, National University of Defense Technol-
ogy, Changsha, China 2Institute for Theoretical Computer Science,
Shanghai University of Finance and Economics, Shanghai, China
3State Key Lab of General AI, School of Intelligence Science
and Technology, Peking University, Beijing, China 4School of
Computer Science, Peking University, Beijing, China 5Faculty of
Engineering, University of Sydney, Sydney, Australia6Faculty of
Computing, Harbin Institute of Technology, Harbin, China. Corre-
spondence to: Haotian Wang<wanghaotian13@nudt.edu.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
chine learning and behavioral economics for more
reliable deployment in the real world.
1. Introduction
Machine learning models are playing an increasingly crit-
ical role in diverse human-serving domains, such as hir-
ing (S´anchez-Monedero et al., 2020), credit scoring (Jagtiani
& Lemieux, 2019), and college admissions (Kuvcak et al.,
2018). In such settings, individuals may strategically mod-
ify their observable features to obtain favorable decisions.
This phenomenon reflects Goodhart’s Law (Strathern, 1997):
“When a measure becomes a target, it ceases to be a good
measure.” Once a model’s decision rule becomes known or
anticipated, agents often engage in ’gaming’ behaviors to
manipulate outcomes. For example, a loan applicant might
temporarily inflate their reported income to appear more
creditworthy. To anticipate such manipulations, strategic
classification (SC) (Hardt et al., 2016) provides a special-
ized machine learning (ML) framework by considering the
Stackelberg-style interaction between decision makers and
strategic agents (Ghalme et al., 2021; Singh & Kulkarni,
2024; Chen et al., 2020), serving as a key bridge between
ML and social sciences.
Given its growing influence, it is increasingly essential to
critically examine the foundational principles of SC. To be
specific, the framework of SC rests on a simplified assump-
tion thatagents are perfectly rational(Hardt et al., 2016;
Milli et al., 2019). Consequently, under this view, an agent
modifies features if, and only if, the expected benefit out-
weighs the cost. However, like a double-edged sword, the
assumption of fully rational agents might result in conflicts
with realistic scenarios, as individuals often behave in ways
that deviate sharply from rational utilities:
• Example 1.In financial investment (Banerji et al., 2020),
individuals often react more strongly to a potential $80
loss than to a potential $100 gain of equal probability. The
same magnitude of outcome thus triggers disproportionate
behavioral responses.
• Example 2.In credit scoring (Banerji et al., 2020), con-
sider loan approval requires applicants to exceed a thresh-
1
arXiv:2605.19674v2  [cs.AI]  6 Jun 2026

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
(b) Credit Scoring (Reference Bias)
Credit Score
Needed
Loan
Admission Point
Need 80
Impossible!
640 700
Need 20
Try it!
(a) Financial Investment ( Loss Aversion)
Venture
May Gain $100
May Loss $80
Invest
Don’t
Invest
Decide
Investor
(c) Disease Screening (Probability Distortion)
Hospital
Rare Disease
Prob=0.5%
Its
Me!
Healthy
Person
Repeated
Testing
Psychologically
InflatedRefer
Figure 1.Illustrative real-life scenarios of behavioral biases: (a) financial investment shaped by loss aversion, (b) credit scoring influenced
by reference bias, and (c) disease screening affected by probability distortion.
old A. Those whose subjective reference point B is just
below A tend to make marginal adjustments, whereas
those far below the threshold usually forgo effort.
• Example 3.In disease screening (Dwyer et al., 2022),
consider a rare disease with a true prevalence of only
0.5%. Although the objective probability of infection is
negligible, some individuals persist in seeking repeated
testing, subjectively inflating the small chance of illness.
Unfortunately, the non-rational behaviors characterized in
the three examples, i.e., asymmetry between the benefit and
cost, behaviors based on different reference points, and dis-
torted probability towards events, are not considered in con-
ventional SC frameworks. More broadly, extensive evidence
from behavioral economics and psychology shows that real-
world decision making systematically deviates from rational
optimization (Carroll & Johnson, 1990; Tversky & Kahne-
man, 1992; Jones, 1999; Ariely & Jones, 2008). Therefore,
we highlight that the rational-agent assumption, while math-
ematically convenient, often collapses in real-world settings.
This mismatch motivates the need for a refined SC frame-
work to capture such realistic behavioral deviations more
precisely, which raises a central research challenge:
Can existing SC methods account for strategic manip-
ulations shaped by psychological biases, beyond the
conventional rational-utility paradigm?
In response to this question, we first definebehaviorally
realistic strategic classification(BR-SC)as a new prob-
lem where agents’ manipulations reflect realistic behavioral
patterns driven by psychological biases, rather than fully
rational best-response rules. Accordingly, the classifier is de-
signed to account for these manipulations, ensuring robust-
ness in deployment. Fortunately, prospect theory (Kahne-
man & Tversky, 2013) and followed behavioral economics
highlight three pervasive mechanisms for realistic behav-
iors: (1)Loss aversion.Individuals tend to weigh potential
losses more heavily than equivalent gains (see Fig. 1(a)). (2)
Reference bias.Individual decision depends on subjective
reference points, which differ across individuals based on
their personal circumstances, expectations, or prior expe-
riences (Fig. 1(b)). (3)Probability distortion.Individuals
overweight small-probability events, showing a tendency to
“gamble” on unlikely opportunities (see Fig. 1(c)).
These behavioral mechanisms result in two consequential
failure modes for existing SC methods,over-defenseand
under-defense, which degrade robustness of decision mod-
els for SC (see detailed derivation in Sec. 4). Therefore, we
propose theProspect-Guided Strategic Framework(Pro-
SF)to address the BR-SC problem. Pro-SF introduces a
paradigm shift for SC by integrating three key principles
(i.e., asymmetry between gains and losses, subjective refer-
ence points, and probability distortion) into the Stackelberg
game framework of SC. This paradigm shift captures how
agents actually manipulate their features in practice and re-
defines both the dynamics of agents’ strategic manipulation
and the decision maker’s optimization objective.
Our main contributions are summarized as follows:
• We identify and formalize the limitations of the rational-
agent assumption in strategic classification by introduc-
ing a new problem setting, termedbehaviorally realistic
strategic classification(BR-SC). We further characterize
two failure modes induced by rational-agent modeling,
namelyover-defenseandunder-defense.
• We propose theprospect-guided strategic frame-
work(Pro-SF), which integrates loss aversion, reference
bias, and probability distortion into the Stackelberg game
framework, providing a more realistic solution for strate-
gic classification.
• We conduct extensive experiments on synthetic and real-
world datasets to demonstrate that Pro-SF achieves robust
performance across diverse behavioral regimes. Ablation
studies and sensitivity analyses further illustrate how each
behavioral component contributes to robustness.
2. Related Work
2.1. Strategic Classification
Strategic classification (SC) studies how individuals manip-
ulate features to obtain favorable decisions (Hardt et al.,
2016). Prior work largely focuses on designing decision
rules that are robust to such manipulations (Dong et al.,
2018; Shavit et al., 2020; Chen et al., 2020; Harris et al.,
2021; Zrnic et al., 2021; Tsirtsis et al., 2024; Liu et al., 2024;
Lv et al., 2026a), as well as leveraging strategic behavior
2

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
to incentivize genuine improvement via causal or action-
based formulations (Miller et al., 2020; Chen et al., 2023;
Horowitz & Rosenfeld, 2023; V o et al., 2024; Efthymiou
et al., 2026; Chang et al., 2024; Wang et al., 2022; 2025;
Yang et al., 2025). Related settings include performative
prediction, where repeated deployment alters the data distri-
bution (Perdomo et al., 2020; Rosenfeld et al., 2020; Hardt
et al., 2022; Mendler-D¨unner et al., 2022; Wang et al.; Lv
et al., 2026b), and societal-level regulation of strategic be-
havior, e.g., optimizing long-term welfare or mitigating
demographic disparities (Haghtalab et al., 2020; Estornell
et al., 2023a; Xie & Zhang, 2024; Zhang et al., 2022; Es-
tornell et al., 2023b; Keswani & Celis, 2023; Lv et al.,
2026c). Recent evidence suggests that human strategic
manipulation deviates substantially from the rational as-
sumption (Ebrahimi et al., 2025; Xie et al., 2025), motivat-
ing our behaviorally realistic formulation (BR-SC) and the
prospect-theoretic framework (Pro-SF).More related work
on strategic classification is included in Appendix A.1.
2.2. Behavioral Economics in Machine Learning
Behavioral economics (Mullainathan & Thaler, 2000) chal-
lenges the classical assumption that agents act as perfectly
rational utility maximizers, emphasizing instead that choices
are systematically shaped by cognitive biases and contextual
factors (Tversky & Kahneman, 1992; Ariely & Jones, 2008).
A central framework crystallizing these insights isprospect
theory(Tversky & Kahneman, 1992; Kahneman & Tversky,
2013), which models how individuals evaluate outcomes
relative to reference points, exhibit asymmetric sensitivity to
gains and losses, and distort probabilities. These principles
have influenced multiple domains: in economics and social
science, they inform finance, consumer behavior, and public
policy (Borkar & Chandak, 2021; Mercer, 2005; Vis, 2011);
in computational settings, they shape reinforcement learn-
ing (Shen et al., 2014; Prashanth et al., 2016), mechanism
design (Kuvcak et al., 2018; Leoneti & Gomes, 2021), and
resource allocation (Holmes Jr et al., 2011).More related
workis included in Appendix A.3.
3. Preliminary
We briefly review the strategic classification (SC) paradigm.
Random variables are denoted by uppercase letters (e.g., X,
Y ), their realizations by lowercase (e.g., x, y), and boldface
for vectors or matrices (e.g.,x,X).
3.1. Rational Strategic Classification Model
The strategic classification problem is modeled as a Stack-
elberg game (Li & Sethi, 2017), where adecision maker
defines a classification function f:R d → {−1,1}, and
decision subjects(agents) strategically manipulate their fea-
tures from x to x′ at a cost c:X × X →R≥0 (Hardt et al.,
2016; Miller et al., 2020). The optimal manipulated feature
x′ is determined by the best-response functionb R(x):
Definition 3.1(Rational Strategic Manipulation).The opti-
mal modified feature vectorx ′ is determined by:
x′ =b R(x) = arg max x′∈X [f(x ′)−λc(x, x′)],(1)
where f(x ′)∈ {−1,1} is the classification result after
modification, c(x, x′) is the manipulation cost, λ >0 is a
trade-off parameter, and X is the feature space. Usually,
the cost of manipulation is modeled as the Mahalanobis
distance (Gavish et al., 2022; Chen et al., 2023).
From the decision maker’s perspective, the classification
rule f is designed to remain robust under such strategic
manipulation:
Definition 3.2(Decision Optimization).To mitigate ma-
nipulation, the decision maker optimizes f to maximize
expected accuracy against strategic manipulation:
f ∗ ∈arg max
f∈F
E(x,y)∼D

1

f(b R(x)) =y

,(2)
where F is the set of all feasible classification rules, 1
denotes the indicator function, andyis the observed label.
3.2. The Achilles’ Heel of Strategic Classification
The rational-agent assumption underlying Eq. (1) and
Eq. (2) is mathematically convenient but behaviorally re-
strictive. Concretely, a large body of work in behavioral
economics and psychology shows that human decision mak-
ing systematically departs from perfect rationality (Tversky
& Kahneman, 1992; Ariely & Jones, 2008; Kahneman &
Tversky, 2013; Borkar & Chandak, 2021). Among these,
Prospect Theory(Tversky & Kahneman, 1992; Kahneman
& Tversky, 2013) provides a unifying framework, capturing
how individuals evaluate uncertain outcomes. Accordingly,
we focus on three particularly relevant deviations from ra-
tionality that serve as the foundation for our behaviorally
realistic formulation:
• Loss aversion in manipulation.Agents subjectively in-
flate perceived effort (e.g., manipulation cost) relative to
gains. Consequently, agents may give up manipulations
that would be beneficial under a rational-utility model be-
cause the perceived loss outweighs the perceived benefit.
• Reference bias.Agents evaluate outcomes relative to
a subjective reference point (e.g., an expected outcome)
rather than an absolute term. This means the utility of a
successful manipulation varies across individuals, violat-
ing the rational-utility assumption commonly used in the
classical SC paradigm.
• Probability distortion.Agents may distort perceived
acceptance probabilities, e.g., overweighting small proba-
3

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
bilities. As a result, they can misjudge how much manip-
ulation is needed to cross the decision threshold, leading
to sub-optimal or insufficient adjustments.
4. Theory: Behavioral Mismatch and Failure
Modes
We now provide a theoretical analysis of why classifiers
trained under the rational-agent assumption can systemati-
cally fail in practice due to behavioral mismatch. We then
formalize two characteristic failure modes:over-defense
andunder-defense.
4.1. Behavioral Mismatch and Deployment Bias
Without loss of generality, the agent’s strategic manipulation
can be summarized by a behavioral response function bθ(·)
induced by a utilityU θ(x, x′):
bθ(x)∈arg max x′∈X Uθ(x, x′),(3)
where θ denotes a general behavioral parameterization. Let
(X, Y)∼ Dand X ′ =b θ(X); the post-manipulation distri-
bution is then defined as Dθ := Law(X′, Y), which differs
from the original feature distribution.
Classical strategic classification assumes that agents re-
spond by maximizing a rational utility, yielding a rational
response bR(x) and a corresponding distribution DR :=
Law(bR(X), Y). This creates abehavioral mismatch: the
classifier is trained on the post-manipulation distributionDR
induced by bR, but is deployed under the distribution Dθ in-
duced by bθ. Therefore, we have the following proposition,
with a detailed proof in Appendix B.
Proposition 4.1(Irreducible deployment bias under be-
havioral mismatch).Let fR denote a classifier opti-
mized on DR, and define the deployment error δ(θ) :=
E(x,y)∼Dθ [L(fR(x), y)]. Suppose Dθ ̸=D R, and that this
mismatch affects a non-zero mass of samples near the de-
cision boundary, i.e., there exist ϵ >0 and γ >0 such
that
P(x,y)∼Dθ

|s(x)−τ| ≤γ, y̸=1{s(x)≥τ}

≥ϵ.(4)
Then δ(θ)>0 , i.e., a non-vanishing deployment error
persists under the rational-agent assumption.
Next, we show that behavioral mismatch manifests through
twodirectionaland practically failure modes:over-defense
andunder-defense.
4.2. Over-defense
Over-defense arises when a classifier trained under the
rational-agent assumption anticipates manipulations that
do not occur in practice (Fig. 2a). Agents who perceive
themselves as far from acceptance due to loss aversion or
reference bias, may choose not to manipulate, even when
manipulation would be optimal under a rational utility.
Definition 4.2(Over-defense).Let fR denote a classifier
trained under the rational-agent assumption. fR exhibits
over-defenseif it adjusts its decision rule to defend against
strategic manipulations that are unlikely to occur at deploy-
ment, leading to degraded classification performance.
Example 1(Over-defense in a linear classifier).Consider a
linear classifier f(x) = sign(w ⊤x−τ) . Under the rational-
agent assumption, it is trained to defend against agents who
minimally manipulate their features to cross the decision
boundary. If, in practice, some agents do not manipulate
at all, this anticipation causes the learned threshold to shift
from τ to τ ′ > τ. Consequently, some instances that satisfy
w⊤x≥τ —and would be accepted without any manipula-
tion—are now rejected:
w⊤x≥τbutw ⊤x < τ′ ⇒f ′ R(x) =−1.(5)
This illustrates how defending against nonexistent manipu-
lations induces false negatives.
Over-defense shifts the decision boundary to counter ma-
nipulations that do not occur in practice, thereby converting
genuinely positive instances into false negatives. We for-
malize the resulting accuracy degradation in the following
proposition (see proof in Appendix C).
Proposition 4.3(Accuracy Degradation from Over-defense).
Let fR be a classifier trained under the rational-agent as-
sumption. Suppose there exists a non-negligible set of agents
who abstain from manipulation due to behavioral biases,
even though rational agents at the same features would
manipulate. If the over-defense-induced boundary shift is
sufficiently large relative to the residual training error on
this abstention set, then
E[L(fR(x), y)]>E[L(f R(bR(x)), y)],(6)
whereLis the loss function for classification.
4.3. Under-defense
Under-defense occurs when agents manipulate more ag-
gressively than anticipated by a classifier trained under the
rational-agent assumption (Fig. 2b). Behaviorally, probabil-
ity distortion may cause agents to overestimate their chances
of acceptance, while loss aversion amplifies the fear of re-
jection, leading them to overshoot the manipulation level
predicted by rational utility maximization.
Definition 4.4(Under-defense).A classifier fR with the
rational-agent assumption exhibitsunder-defenseif it de-
fends only against rational manipulations, while agents in
practice make larger adjustments that exceed this defense,
resulting in degraded classification performance.
4

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Give up manipulation
I’m far from
acceptance
Classifier
boundary
< AcceptShift
(a)Over-defense
Excessive
manipulate
Classifier
boundary
<Accept
Over-fear of
rejection
Shift
 (b)Under-defense
Rational +Los. +Refe. +Prob.
0.65
0.70
0.75
0.80
0.85Accuracy %
0.00
0.04
0.08
0.12
0.16
Error %
Accuracy
over-defense error
under-defense error (c)Effect of Deviations
Figure 2.Illustration of two failure modes induced by the rational-agent assumption. (a) Over-defense caused by agents giving up
manipulation. (b) Under-defense caused by excessive manipulation. (c) Effects of cumulative behavioral deviations on a rational-based
classifier (Los.= loss aversion,Refe.= reference bias,Prob.= probability distortion).
Example 2(Under-defense in a linear classifier).Consider
a linear classifier f(x) = sign(w ⊤x−τ) . Under rational
assumptions, agents are expected to manipulate minimally
to the decision boundary. If, in practice, some agents over-
shoot this endpoint, a classifier trained only against rational
manipulations fails to correctly classify these instances:
fR(bR(x)) =ybutf R(x∗)̸=y.(7)
Under-defense leaves parts of the manipulated feature space
unprotected, allowing strategic agents to bypass the intended
defense. We formalize the resulting performance degrada-
tion in the following proposition (see proof in Appendix D).
Proposition 4.5(Accuracy Degradation from Under-de-
fense).Let fR be a classifier trained under the rational-
agent assumption. Suppose there exists a non-negligible set
of agents who overshoot the rational manipulation endpoint
due to behavioral biases, landing in regions where fR pro-
vides no defense. If the overshoot-induced disagreement is
sufficiently large relative to the residual training error on
this overshoot set, then
E

L(fR(bθ(x)), y)

>E

L(fR(bR(x)), y)

,(8)
where bR(x) denotes the rational manipulation endpoint
and bθ(x) the actual manipulated feature under behavioral
biases.
As shown in Fig. 2c, as agents are increasingly influenced by
psychological biases, the performance of a classifier trained
under the rational-agent assumption deteriorates.
5. Prospect-Guided Strategic Framework
5.1. Problem Formulation
To better reflect real-world strategic behavior, we formal-
ize a practical strategic classification setting, termedbe-
haviorally realistic strategic classification problem(BR-
SC). Unlike classical strategic classification, which assumes
agents follow rational best-response manipulations, BR-SC
allows the manipulations of agents to be influenced by psy-
chological biases.
Problem 5.1(Behaviorally Realistic Strategic Classification
(BR-SC)).The BR-SC problem consists of two coupled
components:
• Behavioral manipulation model.Given a data distribu-
tion D over (x, y), a cost function c, and a classifier f,
agents are modeled by a behaviorally realistic manipula-
tion functionb θ(x).
• Classifier learning under behavioral responses.Based
on the behavioral manipulation model bθ(x), the decision
maker aims to train a classifier f ∗ ∈ Fthat performs ro-
bustly under behaviorally biased strategic manipulations.
Example 3(loan approval).Consider a loan approval sys-
tem, in the BR-SC problem, applicants may still act strategi-
cally, but their decisions are often influenced by psychologi-
cal biases, such as loss aversion, subjective reference points,
and distorted beliefs about approval probability. As a result,
strategic responses in real-world deployment systematically
deviate from idealized rational best responses, giving rise to
a more realistic strategic classification problem.
To address theBR-SCproblem, we introduce theProspect-
Guided Strategic Framework(Pro-SF), which leverages
prospect theory to capture realistic agent manipulations and
reframe the learning objective for the classifier.
5.2. Modeling Prospect-Guided Utility for Agents
We specify an explicit utility-based model for agents’ strate-
gic behavior. In particular, we adopt a prospect-guided
utility that incorporates three irrational mechanisms: loss
aversion, probability distortion, and reference bias.
Loss aversion in manipulation.To capture loss aversion
in agents’ manipulations, we adopt a prospect-style value
function that evaluates perceived gains and losses on asym-
metric scales. Specifically, given a candidate manipulation
x, the agent’s subjective value is defined as
v(x) =v gain(x)α −κ(v loss(x))β,(9)
where vgain(x) and vloss(x) denote the positive and negative
components of the perceived outcome, respectively. The
5

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Loss
Aversion
Reference
Bias
Probability
Distortion
Based on Rationality
Original
Reject
After Manipulation
 → ′
Strategic
Manipulation
Accept
 Reject
Based on Pro-SF
Formulate agent realistic behavior
Figure 3.From rational to behaviorally realistic modeling: Pro-SF reformulates agent realistic behavior and provides robust outcomes.
parameters α, β∈(0,1] encode diminishing sensitivity,
whileκ >1amplifies the perceived weight of losses.
This value function introduces an explicit asymmetry be-
tween gains and losses.
For example, when κ= 1.25 , a perceived gain of 9 and
a perceived loss of 8 are evaluated asymmetrically as 9
versus 10 (i.e., κ·8 = 10 ), causing the loss component
to dominate the decision.
Probability distortion.Agents often distort probabilities
rather than evaluating them objectively, overweighting small
chances of success and underweighting near certainties.
Let p∈[0,1] denote the objective probability of acceptance.
The agent’s subjective probability w(p) is modeled via the
probability weighting function:
w(p) = pγ
pγ + (1−p) γ1/γ , γ∈(0,1],(10)
where γ controls the curvature: smaller values yield a more
pronounced inverse-S shape, leading to stronger overweight-
ing of small probabilities and underweighting of large ones.
For example, with γ= 0.6 , a small objective probabil-
ity p= 0.05 is overweighted (i.e., w(p) = 0.2> p ),
while a large objective probability p= 0.8 is under-
weighted (i.e.,w(p) = 0.6< p).
Remark 1.Eq. (10) follows standard probability-weighting
functions used in prospect theory, which produce an inverse-
S shape probability weighting (Kahneman & Tversky, 2013;
Barberis et al., 2016; Gonzalez & Wu, 1999).
Reference bias.Without loss of generality, let s(x)∈[0,1]
denote the system-defined likelihood of acceptance, where
s(x) = 1 corresponds to meeting the passing threshold.
Rather than evaluating s(x) precisely, agents often form a
coarse-grained subjective reference point r that reflects lim-
ited sensitivity in self-assessment. We model this reference
point via a quantization operator:
r= 1 K j K s(x) k ,(11)
where K sets the step size 1/K (yielding K+1 discrete
levels), mapping r onto equally spaced discrete levels (e.g.,
K= 5givesr∈ {0,0.2,0.4,0.6,0.8,1.0}).
For example, a student after an exam may only estimate
their score within a rough range (e.g., “around 70–80”)
rather than a precise value (e.g.,73).
Unified Prospect-Based Utility.We now unify the three
behavioral components into a single prospect-based utility
that governs agents’ manipulation choices.
Definition 5.2(Prospect-based utility in strategic manipula-
tion).For an agent with subjective reference point r∈[0,1] ,
the prospect-based utility UP for manipulating features from
xtox ′ is
UP(x, x′;ϕ) =w + p(x′)  1−r α
−κ w− 1−p(x ′)  rβ −κ·(λc(x, x ′)β),
(12)
where p(x′)∈[0,1] denotes themodel-impliedprobability
of being classified as positive after manipulation, and ϕ=
{α, β, κ, γ}denotes the Prospect-Theoretic parameter set.
The parameters α, β∈(0,1] capture diminishing sensitivity,
κ >1 encodes loss aversion, λ >0 controls the strength of
manipulation cost, and w+, w− are probability-weighting
functions that distort objective probabilities into subjective
decision weights.
Remark 2.We treat the manipulation cost c(x, x′) as an
effort expenditure that contributes to the agent’s subjective
loss, consistent with the loss-aversion principle in prospect
theory (Passarelli & Del Ponte, 2020). In special cases
where effort is treated as an objective friction rather than a
psychologically salient loss, the cost term can be simplified
to−λ c(x, x′)β.
As illustrated in Fig. 3, Pro-SF reformulates agents’ strate-
gic manipulation by jointly accounting for loss aversion,
reference dependence, and probability distortion.
Remark 3(Information structure of agents).In our setting,
agents do not have direct access to the current classifier
fθ. Instead, they observe historical outcomes and use past
feedback to form a subjective belief about their likelihood
of acceptance, captured by p(x′)∈[0,1] in Eq. (12). This
belief is further distorted by psychological biases rather than
computed directly from fθ, positioning our setting between
6

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Algorithm 1Prospect-Guided Strategic Framework
Require: Dataset D={(x i, yi)}n i=1; a classifier f∈ F;
manipulation costc(·)
1:Parameters:α, β∈(0,1],κ >1,γ∈(0,1],K∈N
2:Initialize classifierf∈ F
3: Perceive agents’ manipulation with prospect-guided
utility (Eq.(12)):
4:Anticipateloss aversionwith Eq. (9)
5:Anticipateprobability distortionwith Eq. (10)
6:Anticipatereference biaswith Eq. (11)
7:Train classifier against manipulated data:
8:Construct ˜D={(b P(xi), yi)}n i=1 with Eq. (13)
9:Learnf ∗ ∈arg min
f∈F
E(x,y)∼D

L(f(b P(x)), y)

10:Returnf ⋆
the full-information assumption (Hardt et al., 2016) and a
no-information extreme.
5.3. Integrating Pro-SF into Strategic Classification
We finally specify the strategic-response model and the
learning objective under Pro-SF. The whole process of Pro-
SF is illustrated in Algm. 1.
Definition 5.3(Prospect-guided Strategic Manipulation).
Given a classifier f∈ Fand data distribution D, an agent
strategically manipulates features in response tof:
bP(x)∈arg max x′∈X UP(x,x ′;ϕ),(13)
where UP(·;ϕ) is the prospect-based utility defined in
Eq.(12).
Definition 5.4(Learning objective of Pro-SF).The deci-
sion maker trains a classifier f that minimizes the expected
classification loss under prospect-guided manipulation:
f ∗ ∈arg min
f∈F
E(x,y)∼D

L(f(b P(x)), y)

,(14)
whereLis a loss function for classification.
5.4. Equilibrium Analysis
The Stackelberg game induced by Pro-SF inherits well-
defined game-theoretic properties. Specifically, we establish
three structural guarantees for the Pro-SF game:
• A Stackelberg equilibrium always exists under standard
compactness conditions on the action space and classifier
parameter space.
• The equilibrium is locally stable, i.e., the best-response
dynamics between the classifier and agents converge to
the equilibrium from any sufficiently close initialization.
• The equilibrium is locally unique within its neighborhood
of attraction.
Formal statements and proofs are provided in Appendix F.
Learnability of behavioral parameters.The Prospect-
Theoretic parameter set ϕ={α, β, κ, γ} used in Pro-
SF is inferred from observed manipulation behavior pairs
{xi, x′ i}n i=1 via maximum likelihood:
ϕ∗ = arg max
ϕ
X
i
logP ϕ(x′ i |x i),(15)
where Pϕ(x′ i |x i) is modeled using a discrete-choice (soft-
max) likelihood over a finite candidate set of feasible ma-
nipulations (see details in Appendix I).
6. Experiment
6.1. Experimental Setup
Dataset.We evaluate our framework on five datasets, includ-
ing four real-world and one synthetic benchmarks:Credit,
Adult,Diabetes,German,Spam, andSynthetic(see detailed
description in Appendix G.1).
Agent behavior paradigms.To evaluate robustness under
different behavioral assumptions, we consider three strategic
manipulations:
• Fully rational.The classical strategic classification
paradigm, where agents manipulate their features to max-
imize utility in Eq. (1) (Hardt et al., 2016).
• Non-rational.Agents stochastically deviate from the ra-
tional best-response strategy, driven by behavioral mech-
anisms in behavioral economics (Kahneman & Tversky,
2013; Kuvcak et al., 2018; Leoneti & Gomes, 2021).
• Mixed behavioral.A heterogeneous population in which
a proportion π of agents behave fully rationally, while the
remaining (1−π) exhibit non-rational strategic behavior.
Metric.We useaccuracyas the primary metric and in-
troduce two additional metrics:over-defense error(ODE)
andunder-defense error(UDE). ODE measures false rejec-
tions caused by the classifier being overly defensive. UDE
measures false acceptances due to non-rational manipulation
of agents and insufficient defense of the classifier.
Baseline.We mainly conduct experiments with linear mod-
els, consistent with previous standard approaches (Chen
et al., 2023; Shavit et al., 2020; Ghalme et al., 2021) with
Mahalanobis distance for manipulation cost (Gavish et al.,
2022).
Implementation.We implement the classifier f as a lo-
gistic regression model trained with cross-entropy loss and
learning rate 10−3. In prospect-theoretic utility, we set the
curvature parameters α= 0.8 and β= 0.7 , the loss aver-
sion coefficient κ= 2.25 , and the probability-weighting
parameter γ= 0.7 by default. In the mixed agent behavior
7

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 1.Performance (%) of rational-based models and Pro-SF models within different agent manipulation paradigms.
Classifier Manipulation Datasets
Adult Credit Diabetes German Spam Synthetic
Rational-based
Rational78.53 ±0.87 76.12±1.34 70.25±1.52 74.31±1.41 83.87±1.21 81.62±1.28
Non-rational72.42 ±1.85 69.54±2.11 64.73±1.89 68.21±2.03 78.38±1.94 73.20±2.22
Mixed Behavior74.31 ±1.51 72.12±1.87 66.81±1.65 70.43±1.92 78.16±1.63 75.15±1.74
Pro-SF (ours)
Rational75.31 ±0.93 77.02±1.25 71.23±1.43 75.18±1.38 82.92±1.18 80.41±1.12
Non-rational81.50 ±1.23 82.41±1.37 74.52±1.26 79.35±1.42 89.34±1.27 85.20±1.31
Mixed Behavior78.68 ±1.77 79.13±1.63 72.01±1.58 76.24±1.71 86.71±1.52 82.34±1.56
Table 2.Performance of our ablation study on behavioral mechanisms.
Classifier Behavioral Factors Metrics
Refe. Prob. Los. Accuracy(%)↑Over-defense error(%)↓Under-defense error(%)↓
fP ro−sf ✓ ✓ ✓78.92 ±0.13 5.17 ±0.11 3.22 ±0.09
fRef e+P rob ✓ ✓ ✗77.72 ±0.27 6.24 ±0.08 5.29 ±0.12
fRef e+Los ✓ ✗ ✓77.80 ±0.16 7.21 ±0.10 5.05 ±0.07
fP rob+Los ✗ ✓ ✓77.45 ±0.09 6.28 ±0.06 4.79 ±0.13
fRef e ✓ ✗ ✗75.33 ±0.11 9.12 ±0.09 7.27 ±0.10
fP rob ✗ ✓ ✗73.50 ±0.15 9.26 ±0.08 9.23 ±0.12
fLos ✗ ✗ ✓75.91 ±0.11 7.14 ±0.11 7.05 ±0.09
Note:1)Refe.= Reference bias. 2)Prob.= Probability distortion. 3)Los.= Loss aversion.
paradigm, the proportion is set as π= 0.2 . More implemen-
tation details are included in Appendix G.3
6.2. Ablation Study
To better understand the design of our Pro-SF, we conduct
the following ablation studies.
Ablation on behavioral mechanisms.We first examine
the necessity of the three core behavioral mechanisms: loss
aversion, probability weighting, and reference bias. Starting
from the full model, we construct variants byneutraliz-
ingone component at a time. For example, therational-
weightingvariant removes probability distortion by setting
w+(p) =pandw −(1−p) = 1−p.
Parameter sensitivity.We further assess robustness to
parameter choices by varying one parameter (or parameter
pair). Specifically, we consider:
•(α, β)∈ {(0.85,0.8),(0.85,0.75),(0.8,0.8),(0.8,0.7)};
•κ∈ {1.75,2.0,2.25,2.5,2.75};
•γ∈ {0.6,0.65,0.7,0.8},
•rdetermined by the reference granularityK∈ {3,4,5}.
A notation table is provided in Appendix G.2 ( Table 4) and
more results are included in Appendix G.4(Fig. 6) 1 .
1The tested parameter ranges are determined based on our
parameter learning objective (Eq. (15)) and ranges commonly
adopted in prospect-theoretic and behavioral economics litera-
An alternative of probability distortion modelingis the
two-parameterPrelecfunction (Prelec, 1998), w(p) =
exp

−η(−lnp) ϕ , ϕ, η >0 . We examine this func-
tion in Appendix G.4 (Table 6).
6.3. Result and Analysis
Overall performance.As shown in Table 1, Pro-SF con-
sistently outperforms rational-based models when agents
exhibit behavioral deviations, both in the non-rational and
the more realistic mixed settings, across all datasets. At
the same time, Pro-SF maintains competitive performance
under the fully rational paradigm, indicating that incorporat-
ing behavioral modeling does not compromise performance
when classical assumptions hold. Overall, these results
demonstrate that Pro-SF provides robust performance across
diverse strategic environments.
Ablation on behavioral mechanisms.Table 2 shows that
each component contributes meaningfully, and the full Pro-
SF (all three enabled) consistently performs best.Reference
biasyields the largest marginal gain: removing it hurts most
because the model can no longer capture abstention, which
is key to correcting over-defense. Droppingprobability
weightingreduces robustness to distorted tail probabilities
and increases under-defense, while removingloss aversion
eliminates gain–loss asymmetry and weakens boundary sta-
bility. Overall, multi-mechanism variants outperform single-
ture (Kahneman & Tversky, 2013; Borkar & Chandak, 2021).
8

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
1.75 2.00 2.25 2.50 2.75
 (loss parameter)
76.1
76.2
76.3
76.4Accuracy (%)
=0.60
=0.65
=0.70
=0.80
(a)α= 0.8, β= 0.8
1.75 2.00 2.25 2.50 2.75
 (loss parameter)
76.1
76.2
76.3
76.4Accuracy (%)
=0.60
=0.65
=0.70
=0.80
 (b)α= 0.85, β= 0.8
1.75 2.00 2.25 2.50 2.75
 (loss parameter)
76.1
76.2
76.3
76.4Accuracy (%)
=0.60
=0.65
=0.70
=0.80
 (c)α= 0.85, β= 0.7
1.75 2.00 2.25 2.50 2.75
 (loss parameter)
76.1
76.2
76.3
76.4Accuracy (%)
=0.60
=0.65
=0.70
=0.80
 (d)α= 0.8, β= 0.7
Figure 4.Parameter ablation results with parameters(α, β, κ, γ)andr∈ {0,0.2,0.4,0.6,0.8}.
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.8, = 0.7)
=0.65
=0.70
=0.80
(a)r∈ {0,0.3,0.6,0.9}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.8, = 0.7)
=0.65
=0.70
=0.80
 (b)r∈ {0,0.4,0.7}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.85, = 0.8)
=0.65
=0.70
=0.80
 (c)r∈ {0,0.3,0.6,0.9}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.85, = 0.8)
=0.65
=0.70
=0.80
 (d)r∈ {0,0.4,0.7}
Figure 5.Parameter ablation results with parametersκ, γ, rwith different(α, β).
mechanism ones, indicating strong complementarity: refer-
ence bias governswhetheragents move, whereas probability
weighting and loss aversion determinehow farthey move.
Parameter sensitivity.Fig. 4 and Fig. 5 examine the ef-
fect of varying the Pro-SF parameters. Overall, accuracy
remains stable across wide ranges, showing that Pro-SF
does not rely on fine-tuned hyperparameters. Specifically,
adjusting the loss aversion coefficient κ only changes out-
comes marginally, suggesting robustness to different levels
of risk sensitivity. Variations in the probability distortion
parameter γ shift the relative emphasis on tail events but do
not alter the overall trend. Different bins of r only cause
some fluctuations in performance, but are all better than the
rational classifier. Finally, different curvature settings(α, β)
yield consistent results, confirming that Pro-SF maintains
effectiveness under diverse utility shapes.
7. Conclusion
This work challenges the classical rational-agent assump-
tion in strategic classification and formalizes the problem
ofbehaviorally realistic strategic classification. We theo-
retically characterize the impact of behavioral mismatch on
deployment performance, and propose theProspect-Guided
Strategic Framework, which incorporates three key psycho-
logical mechanisms underlying strategic manipulation and
provides a behaviorally grounded solution for SC in the real-
world. Future work will extend this framework to richer and
more diverse deployment settings.
Acknowledgement
This work was jointly supported by the National Nat-
ural Science Foundation of China (Nos. 62276004,
62325604, 62525213), the Beijing Natural Science
Foundation (No. L257007), the Beijing Major Science
and Technology Project (No. Z251100008425006), the
Shanghai Sailing Program (No. 24YF2711600), the
Provincial Natural Science Foundation of Heilongjiang
Province (No. LH2023C069), the Provincial Natural Sci-
ence Foundation of Hunan Province (No. 2025JJ10008),
the NUDT Youth Independent Innovation Science
Fund (No. ZK25-20), the NUDT Innovation Foundation
for Postgraduate (No. XJQY2025011), and the State Key
Laboratory of General Artificial Intelligence.
Impact Statement
This paper presents work whose goal is to advance the field
of Machine Learning. There are many potential societal
consequences of our work, none of which we feel must be
specifically highlighted here.
References
Ariely, D. and Jones, S.Predictably irrational. Harper-
Collins New York, 2008.
Banerji, J., Kundu, K., and Alam, P. A. An empirical inves-
tigation into the influence of behavioral biases on invest-
ment behavior.SCMS Journal of Indian Management, 17
(1):81–98, 2020.
9

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Barberis, N., Mukherjee, A., and Wang, B. Prospect the-
ory and stock returns: An empirical test.The review of
financial studies, 29(11):3068–3107, 2016.
Barberis, N., Jin, L. J., and Wang, B. Prospect theory and
stock market anomalies.The Journal of Finance, 76(5):
2639–2687, 2021.
Becker, B. and Kohavi, R. Adult. UCI Ma-
chine Learning Repository, 1996. DOI:
https://doi.org/10.24432/C5XW20.
Borkar, V . S. and Chandak, S. Prospect-theoretic q-learning.
Systems & Control Letters, 156:105009, 2021.
Carroll, J. S. and Johnson, E. J.Decision research: A field
guide.Sage Publications, Inc, 1990.
Chang, T., Warrenburg, L., Park, S.-H., Parikh, R., Makar,
M., and Wiens, J. Who’s gaming the system? a causally-
motivated approach for detecting strategic adaptation.Ad-
vances in Neural Information Processing Systems, 37:
42311–42348, 2024.
Chen, Y ., Liu, Y ., and Podimata, C. Learning strategy-
aware linear classifiers.Advances in Neural Information
Processing Systems, 33:15265–15276, 2020.
Chen, Y ., Wang, J., and Liu, Y . Learning to incen-
tivize improvements from strategic agents.Transac-
tions on Machine Learning Research, 2023. ISSN 2835-
8856. URL https://openreview.net/forum?
id=W98AEKQ38Y.
Chen, Y ., Mao, Y ., Zheng, C., Zou, H., Gu, S., Liu, S., Shi,
Y ., Yang, W., Kuang, K., and Wang, H. Detecting unob-
served confounders: A kernelized regression approach.
arXiv preprint arXiv:2601.00200, 2026.
Dong, J., Roth, A., Schutzman, Z., Waggoner, B., and Wu,
Z. S. Strategic classification from revealed preferences. In
Proceedings of the 2018 ACM Conference on Economics
and Computation, pp. 55–70, 2018.
Dwyer, A. A., Uveges, M. K., Dockray, S., and Smith, N.
Exploring rare disease patient attitudes and beliefs regard-
ing genetic testing: implications for person-centered care.
Journal of Personalized Medicine, 12(3):477, 2022.
Ebrahimi, R., Vaccaro, K., and Naghizadeh, P. The double-
edged sword of behavioral responses in strategic classi-
fication: Theory and user studies. InProceedings of the
2025 ACM Conference on Fairness, Accountability, and
Transparency, pp. 868–886, 2025.
Efthymiou, V ., Podimata, C., Sen, D., and Ziani, J. Incen-
tivizing desirable effort profiles in strategic classification:
The role of causality and uncertainty.Advances in Neu-
ral Information Processing Systems, 38:146550–146586,
2026.
Eilat, I., Finkelshtein, B., Baskin, C., and Rosenfeld, N.
Strategic classification with graph neural networks. In
11th International Conference on Learning Representa-
tions, ICLR 2023, 2023.
Estornell, A., Chen, Y ., Das, S., Liu, Y ., and V orobeychik,
Y . Incentivizing recourse through auditing in strategic
classification. InIJCAI, 2023a.
Estornell, A., Das, S., Liu, Y ., and V orobeychik, Y . Group-
fair classification with strategic agents. InProceedings
of the 2023 ACM Conference on Fairness, Account-
ability, and Transparency, FAccT ’23, pp. 389–399,
New York, NY , USA, 2023b. Association for Com-
puting Machinery. ISBN 9798400701924. doi: 10.
1145/3593013.3594006. URL https://doi.org/
10.1145/3593013.3594006.
Evans, B. P. and Prokopenko, M. Bounded rationality for
relaxing best response and mutual consistency: the quan-
tal hierarchy model of decision making.Theory and
Decision, 96(1):71–111, 2024.
Gavish, M., Su, P.-C., Talmon, R., and Wu, H.-T. Optimal
recovery of precision matrix for mahalanobis distance
from high-dimensional noisy observations in manifold
learning.Information and Inference: A Journal of the
IMA, 11(4):1173–1202, 2022.
Ghalme, G., Nair, V ., Eilat, I., Talgam-Cohen, I., and Rosen-
feld, N. Strategic classification in the dark. InInterna-
tional Conference on Machine Learning, pp. 3672–3681.
PMLR, 2021.
Gonzalez, R. and Wu, G. On the shape of the probability
weighting function.Cognitive psychology, 38(1):129–
166, 1999.
Haghtalab, N., Immorlica, N., Lucier, B., and Wang, J. Z.
Maximizing welfare with incentive-aware evaluation
mechanisms.arXiv preprint arXiv:2011.01956, 2020.
Hardt, M. and Mendler-D¨unner, C. Performative prediction:
Past and future.Statistical Science, 40(3):417–436, 2025.
Hardt, M., Megiddo, N., Papadimitriou, C., and Wootters,
M. Strategic classification. InProceedings of the 2016
ACM conference on innovations in theoretical computer
science, pp. 111–122, 2016.
Hardt, M., Jagadeesan, M., and Mendler-D¨unner, C. Perfor-
mative power.Advances in Neural Information Process-
ing Systems, 35:22969–22981, 2022.
Harris, K., Heidari, H., and Wu, S. Z. Stateful strate-
gic regression. In Ranzato, M., Beygelzimer, A.,
Dauphin, Y ., Liang, P., and Vaughan, J. W. (eds.),
Advances in Neural Information Processing Systems,
10

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
volume 34, pp. 28728–28741. Curran Associates, Inc.,
2021. URL https://proceedings.neurips.
cc/paper_files/paper/2021/file/
f1404c2624fa7f2507ba04fd9dfc5fb1-Paper.
pdf.
Harris, K., Ngo, D. D. T., Stapleton, L., Heidari, H., and Wu,
S. Strategic instrumental variable regression: Recovering
causal relationships from strategic responses. InInterna-
tional Conference on Machine Learning, pp. 8502–8522.
PMLR, 2022.
Hofmann, H. Statlog (German Credit Data). UCI
Machine Learning Repository, 1994. DOI:
https://doi.org/10.24432/C5NC77.
Holmes Jr, R. M., Bromiley, P., Devers, C. E., Holcomb,
T. R., and McGuire, J. B. Management theory applica-
tions of prospect theory: Accomplishments, challenges,
and opportunities.Journal of Management, 37(4):1069–
1107, 2011.
Hopkins, Mark, Reeber, Erik, Forman, George, Suermondt,
and Jaap. Spambase. UCI Machine Learning Repository,
1999. DOI: https://doi.org/10.24432/C53G6X.
Horowitz, G. and Rosenfeld, N. Causal strategic classifica-
tion: A tale of two shifts. InInternational Conference on
Machine Learning, pp. 13233–13253. PMLR, 2023.
Hossain, S., Micha, E., Chen, Y ., and Procaccia, A. Strate-
gic classification with externalities. InInternational Con-
ference on Learning Representations, volume 2025, pp.
28338–28361, 2025.
Jagtiani, J. and Lemieux, C. The roles of alternative data and
machine learning in fintech lending: evidence from the
lendingclub consumer platform.Financial Management,
48(4):1009–1029, 2019.
Jones, B. D. Bounded rationality.Annual review of political
science, 2(1):297–321, 1999.
Kahneman, D. and Tversky, A. Prospect theory: An analysis
of decision under risk. InHandbook of the fundamentals
of financial decision making: Part I, pp. 99–127. World
Scientific, 2013.
Keswani, V . and Celis, L. E. Addressing strategic manipula-
tion disparities in fair classification. InProceedings of the
3rd ACM Conference on Equity and Access in Algorithms,
Mechanisms, and Optimization, pp. 1–11, 2023.
Kleinberg, J. and Raghavan, M. How do classifiers induce
agents to invest effort strategically?ACM Transactions on
Economics and Computation (TEAC), 8(4):1–23, 2020.
Kou, Z., Xie, Y ., Wang, H., Wang, J., Xie, M., Chen, S., Jia,
Y ., Liu, T., and Geng, X. Rankmatch: A novel approach
to semi-supervised label distribution learning leverag-
ing rank correlation between labels. InProceedings of
the 39th Conference on Neural Information Processing
Systems (NeurIPS 2025), San Diego, California, USA,
December 2025. Neural Information Processing Systems
Foundation.
Kou, Z., Wu, J., Huang, W., He, W., Xie, M.-K., Wang, C.,
Jia, Y ., Jiang, D., Liu, Y ., Geng, X., and Yang, Q. Fed-
harmony: Harmonizing heterogeneous label correlations
in federated multi-label learning. InProceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), 2026.
Kuvcak, D., Jurivcic, V ., and DJambic, G. Machine learning
in education-a survey of current research trends.Annals
of DAAAM & Proceedings, 29, 2018.
Laibson, D. Golden eggs and hyperbolic discounting.The
Quarterly Journal of Economics, 112(2):443–478, 1997.
Leoneti, A. B. and Gomes, L. F. A. M. A novel version of the
todim method based on the exponential model of prospect
theory: The exptodim method.European Journal of
Operational Research, 295(3):1042–1055, 2021. ISSN
0377-2217. doi: https://doi.org/10.1016/j.ejor.2021.03.
055. URL https://www.sciencedirect.com/
science/article/pii/S0377221721002812.
Levanon, S. and Rosenfeld, N. Strategic classification made
practical. InInternational Conference on Machine Learn-
ing, pp. 6243–6253. PMLR, 2021.
Li, T. and Sethi, S. P. A review of dynamic stackelberg game
models.Discrete & Continuous Dynamical Systems-
Series B, 22(1), 2017.
Liu, S., Fan, C., Cheng, K., Wang, Y ., Cui, P., Sun, Y ., and
Liu, Z. Inductive meta-path learning for schema-complex
heterogeneous information networks.IEEE Transactions
on Pattern Analysis and Machine Intelligence, 46(12):
10196–10209, 2024.
Liu, S., He, Y ., Wang, H., Yang, W., Wang, Y ., Cui, P., and
Liu, Z. Environment inference for learning generaliz-
able dynamical system.Advances in Neural Information
Processing Systems, 38:164076–164105, 2026.
Lopez-Rojas, E., Elmir, A., and Axelsson, S. Paysim: A
financial mobile money simulator for fraud detection.
In28th European modeling and simulation symposium,
EMSS, Larnaca, pp. 249–255. Dime University of Genoa,
2016.
11

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Lv, X., Mao, Y ., Li, H., Liang, K., Yang, J., Huang, W.,
Chi, H., Chen, H., Lan, L., Yang, W., et al. Breaking
the gradient barrier: Unveiling large language models for
strategic classification.Advances in Neural Information
Processing Systems, 38:49145–49180, 2026a.
Lv, X., Mao, Y ., Xu, R., Zheng, C., Chen, Y ., Li, H., Yang,
J., Kuang, K., Chen, Y ., Geng, M., et al. When tabular
foundation models meet strategic tabular data: A prior
alignment approach.arXiv preprint arXiv:2605.19662,
2026b.
Lv, X., Zheng, C., Mao, Y ., Xu, R., Zou, H., Gu, S., Xu,
L., Chen, H., Chen, Y ., Yang, W., et al. Partial fair-
ness awareness: Belief-guided strategic mechanism for
strategic agents. InProceedings of the AAAI Conference
on Artificial Intelligence, volume 40, pp. 24207–24215,
2026c.
Mendler-D¨unner, C., Ding, F., and Wang, Y . Anticipat-
ing performativity by predicting from predictions.Ad-
vances in neural information processing systems, 35:
31171–31185, 2022.
Mercer, J. Prospect theory and political science.Annu. Rev.
Polit. Sci., 8(1):1–21, 2005.
Miller, J., Milli, S., and Hardt, M. Strategic classification is
causal modeling in disguise. InInternational Conference
on Machine Learning, pp. 6917–6926. PMLR, 2020.
Milli, S., Miller, J., Dragan, A. D., and Hardt, M. The
social cost of strategic classification. InProceedings of
the Conference on Fairness, Accountability, and Trans-
parency (FAT* ’19), pp. 230–239, New York, NY , USA,
2019. Association for Computing Machinery. ISBN
9781450363242. doi: 10.1145/3287560.3287576.
Mofakhami, M., Mitliagkas, I., and Gidel, G. Performa-
tive prediction with neural networks. InInternational
Conference on Artificial Intelligence and Statistics, pp.
11079–11093. PMLR, 2023.
Mullainathan, S. and Thaler, R. H. Behavioral economics.
Working Paper w7948, National Bureau of Economic
Research, October 2000.
O’donoghue, T. and Rabin, M. Doing it now or later.Amer-
ican economic review, 89(1):103–124, 1999.
Passarelli, F. and Del Ponte, A. Prospect theory, loss aver-
sion, and political behavior. InOxford Research Encyclo-
pedia of Politics. 2020.
Payne, K. An analysis of ai decision under risk: Prospect
theory emerges in large language models.arXiv preprint
arXiv:2508.00902, 2025.
Perdomo, J., Zrnic, T., Mendler-D¨unner, C., and Hardt, M.
Performative prediction. InInternational Conference on
Machine Learning, pp. 7599–7609. PMLR, 2020.
Prashanth, L., Jie, C., Fu, M., Marcus, S., and Szepesv´ari, C.
Cumulative prospect theory meets reinforcement learning:
Prediction and control. InInternational Conference on
Machine Learning, pp. 1406–1415. PMLR, 2016.
Prelec, D. The probability weighting function.Economet-
rica, 66(3):497–527, 1998.
Rosenfeld, N., Hilgard, A., Ravindranath, S. S., and Parkes,
D. C. From predictions to decisions: Using lookahead
regularization.Advances in Neural Information Process-
ing Systems, 33:4115–4126, 2020.
S´anchez-Monedero, J., Dencik, L., and Edwards, L. What
does it mean to’solve’the problem of discrimination in hir-
ing? social, technical and legal perspectives from the uk
on automated hiring systems. InProceedings of the 2020
conference on fairness, accountability, and transparency,
pp. 458–468, 2020.
Shavit, Y ., Edelman, B., and Axelrod, B. Causal strate-
gic linear regression. InInternational Conference on
Machine Learning, pp. 8676–8686. PMLR, 2020.
Shen, Y ., Tobia, M. J., Sommer, T., and Obermayer, K. Risk-
sensitive reinforcement learning.Neural computation, 26
(7):1298–1328, 2014.
Singh, M. K. and Kulkarni, A. A. Optimal stochastic de-
cision rule for strategic classification. In2024 National
Conference on Communications (NCC), pp. 1–6. IEEE,
2024.
Strathern, M. ‘improving ratings’: audit in the british uni-
versity system.European Review, 5(3):305–321, 1997.
doi: 10.1002/(SICI)1234-981X(199707)5:3&#60;305::
AID-EURO184&#62;3.0.CO;2-4.
Teboul, A. Diabetes health indicators
dataset, 2015. URL https://www.
kaggle.com/datasets/alexteboul/
diabetes-health-indicators-dataset.
Todd, P. M. and Gigerenzer, G. Pr´ecis of simple heuristics
that make us smart.Behavioral and brain sciences, 23
(5):727–741, 2000.
Tsirtsis, S., Tabibian, B., Khajehnejad, M., Singla, A.,
Sch¨olkopf, B., and Gomez-Rodriguez, M. Optimal de-
cision making under strategic behavior.Management
Science, 2024.
Tversky, A. and Kahneman, D. Advances in prospect theory:
Cumulative representation of uncertainty.Journal of Risk
and uncertainty, 5(4):297–323, 1992.
12

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Vis, B. Prospect theory and political decision making.Po-
litical Studies Review, 9(3):334–343, 2011.
V o, K. Q., Aadil, M., Chau, S. L., and Muandet, K. Causal
strategic learning with competitive selection. InProceed-
ings of the AAAI Conference on Artificial Intelligence,
volume 38, pp. 15411–15419, 2024.
Wang, H., Zou, H., Li, H., Chi, H., Shi, Y ., Zhang, Y ., Yang,
W., Liu, X., and Lin, Z. Transformers with endogenous
in-context learning: Bias characterization and mitigation.
InThe Fourteenth International Conference on Learning
Representations.
Wang, H., Yang, W., Yang, L., Wu, A., Xu, L., Ren, J., Wu,
F., and Kuang, K. Estimating individualized causal effect
with confounded instruments. InProceedings of the 28th
ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pp. 1857–1867, 2022.
Wang, H., Kuang, K., Lan, L., Wang, Z., Huang, W., Wu,
F., and Yang, W. Out-of-distribution generalization with
causal feature separation.IEEE Transactions on Knowl-
edge and Data Engineering, 36(4):1758–1772, 2023.
Wang, H., Li, H., Zou, H., Chi, H., Lan, L., Huang, W., and
Yang, W. Effective and efficient time-varying counterfac-
tual prediction with state-space models. InThe Thirteenth
International Conference on Learning Representations,
2025.
Xie, T. and Zhang, X. Non-linear welfare-aware strategic
learning. InProceedings of the AAAI/ACM Conference
on AI, Ethics, and Society, volume 7, pp. 1660–1671,
2024.
Xie, T., Rauch, P., and Zhang, X. How strategic agents re-
spond: Comparing analytical models with llm-generated
responses in strategic classification.arXiv preprint
arXiv:2501.16355, 2025.
Yang, W., Lv, X., Mao, Y ., Xu, L., Jin, R., Chen, H., Ren,
J., Yang, J., Chen, Y ., and Wang, H. Advanced strategic
improvement with decision interactions. InJoint Euro-
pean Conference on Machine Learning and Knowledge
Discovery in Databases, pp. 426–444. Springer, 2025.
Yeh, I.-C. Default of Credit Card Clients. UCI
Machine Learning Repository, 2009. DOI:
https://doi.org/10.24432/C55S3H.
Zhang, X., Khalili, M. M., Jin, K., Naghizadeh, P., and
Liu, M. Fairness interventions as (Dis)Incentives for
strategic manipulation. In Chaudhuri, K., Jegelka, S.,
Song, L., Szepesvari, C., Niu, G., and Sabato, S. (eds.),
Proceedings of the 39th International Conference on Ma-
chine Learning, volume 162 ofProceedings of Machine
Learning Research, pp. 26239–26264. PMLR, 17–23 Jul
2022. URL https://proceedings.mlr.press/
v162/zhang22l.html.
Zrnic, T., Mazumdar, E., Sastry, S., and Jordan, M. Who
leads and who follows in strategic classification?Ad-
vances in Neural Information Processing Systems, 34:
15257–15269, 2021.
13

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Appendix Contents
•Additional Related Work
•Proof of Proposition 4.1
•Proof of Proposition 4.3
•Proof of Proposition 4.5
•Pro-SF Improves Deployment Guarantees
•Existence of Stackelberg Equilibrium under Pro-SF
•Additional Experiments
•Validation with Real-World Manipulation Data
•Learnability of Behavioral Parameters
•Behavioral Illustration
A. Additional Related Work
A.1. More Strategic Machine Learning Work
Several additional directions in strategic machine learning complement the studies highlighted in Section 2.
Robustness extensions.Beyond classical defenses, researchers have explored stochastic classifiers (Singh & Kulkarni,
2024), differentiable optimization layers for end-to-end robustness (Levanon & Rosenfeld, 2021), and graph-based models to
capture inter-agent dependencies (Eilat et al., 2023). Multi-agent formulations further investigate externalities and collective
dynamics in strategic settings (Hossain et al., 2025; Kou et al., 2025; 2026).
Positive manipulation.A growing body of work highlights the constructive potential of strategic behavior. For example,
classifiers that incentivize authentic qualification gains have been proposed in education and hiring contexts (Kleinberg &
Raghavan, 2020; Harris et al., 2022; Liu et al., 2026). These approaches complement causal frameworks (Miller et al., 2020;
Chen et al., 2023; 2026), which distinguish between manipulable and improvable features.
Performative prediction extensions.Beyond the foundational contributions (Perdomo et al., 2020; Rosenfeld et al.,
2020; Hardt et al., 2022; Mendler-D ¨unner et al., 2022), further work explores neural methods for dynamic feedback
loops (Mofakhami et al., 2023) and more recent advances in model-induced distribution shifts (Hardt & Mendler-D¨unner,
2025).
Fairness perspectives.In addition to direct fairness interventions (Zhang et al., 2022; Estornell et al., 2023b; Keswani &
Celis, 2023; Lv et al., 2026c), several studies consider fairness as an incentive-alignment mechanism that influences agents’
strategic behavior, thereby connecting individual manipulation with broader social equity.
A.2. Position of Our Work
Our work, Pro-SF, is designed tocomplementthe classical strategic classification paradigm rather than overturn it. The
rational-agent model remains a useful idealization—and a natural baseline—for analyzing strategic behavior under well-
specified utilities and costs. Our contribution is to provide a behaviorally grounded formulation for settings where strategic
responses systematically deviate from this idealization due to psychological biases. Importantly, Pro-SF is fully compatible
with classical SC: when behavioral mechanisms are absent (e.g., κ= 1 and probability weighting reduces to the identity),
Pro-SF reduces to the standard rational-response formulation.
A.3. Additional Behavioral Economics Background
Beyond the works highlighted in Section 2, a broader body of literature illustrates how behavioral economics explains
systematic deviations from rationality and informs computational models.
14

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Bounded rationality and heuristics.Human decision-making is constrained by limited cognitive resources and often
relies on simplified rules rather than exhaustive optimization (Todd & Gigerenzer, 2000; Evans & Prokopenko, 2024; Wang
et al., 2023). This perspective suggests that agents may respond in partial, myopic, or context-dependent ways instead of
precise best responses.
Temporal and framing effects.Individuals overweight immediate costs relative to delayed benefits and respond differently
to equivalent options depending on presentation (Laibson, 1997; O’donoghue & Rabin, 1999). These effects imply that
manipulations which appear objectively beneficial may still be avoided or inconsistently adopted.
Extended applications.Behavioral frameworks have been applied across diverse algorithmic domains. Examples include
portfolio optimization and asset pricing in finance (Barberis et al., 2021), multi-criteria decision methods (Leoneti &
Gomes, 2021), fairness-aware allocation in management science (Holmes Jr et al., 2011), and human–AI decision support
systems (Payne, 2025). Collectively, these studies demonstrate the versatility of prospect-theoretic and behavioral models in
explaining and predicting non-rational behavior.
B. Proof of Proposition 4.1
B.1. Assumptions and Setup
We work under a threshold classifier fR(x) =1{s(x)≥τ} , where s:X →R is the decision score and τ∈R is the
threshold, with the0–1lossL(f(x), y) =1{f(x)̸=y}. The deployment error reduces to:
δ(θ) =P (x,y)∼Dθ

fR(x)̸=y

.(16)
The key assumption is theboundary-mass condition: there exist constantsϵ >0andγ >0such that
P(x,y)∼Dθ

|s(x)−τ| ≤γ, y̸=1{s(x)≥τ}

≥ϵ.(17)
This condition states that under the true behavioral distribution Dθ, a non-negligible fraction of deployment samples falls
within aγ-neighborhood of the decision boundary and carries labels that disagree with the classifier’s prediction.
B.2. Discussion: Naturality of the Boundary-Mass Condition
The boundary-mass condition (17) is not an artificial regularity assumption; it is a direct and natural consequence of the
behavioral mismatch betweenD θ andD R in strategic classification settings.
Why the condition holds in practice.The classifier fR is trained on the rational post-manipulation distribution DR, and its
decision boundary τ is calibrated to correctly separate the positive and negative classes under DR. When agents deviate
from rational behavior—due to loss aversion, reference bias, or probability distortion—the actual deployment distribution
Dθ differs from DR. This shift systematically places a portion of the agent population near the decision boundary with
incorrect labels underf R, for two concrete reasons:
• Over-defense: agents subject to loss aversion or reference bias may abstain from manipulation even when rational agents
would manipulate to cross τ. These abstaining agents remain on the “wrong side” of the boundary that fR was trained to
defend, contributing label-disagreeing mass nearτ.
• Under-defense: agents subject to probability distortion may overshoot the rational manipulation endpoint, landing on the
other side ofτin a region wheref R was not designed to classify correctly.
In both cases, the mass accumulates specifically near the decision boundary because the classifier fR was optimized to be
accurate far from τ; the boundary region is precisely where the mismatch between DR and Dθ is most consequential. The
parameters ϵ and γ quantify the severity of this mismatch: larger behavioral deviations produce larger ϵ and γ, as confirmed
empirically in Fig. 2c.
Relation to distribution shift.Condition (17) is strictly weaker than requiring Dθ ̸=D R globally; it only requires the
distributional difference to manifest in a decision-relevant region. This is precisely the regime that matters for classification
performance: differences far from the boundary have no impact on accuracy, while differences near the boundary do.
15

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
B.3. Proof
Define the boundary disagreement set:
A:=
n
(x, y) :|s(x)−τ| ≤γ, y̸=1{s(x)≥τ}
o
.(18)
For any(x, y)∈ A, the classifier predictsfR(x) =1{s(x)≥τ} ̸=y, soL(f R(x), y) = 1. Therefore:
δ(θ) =E (x,y)∼Dθ

1{fR(x)̸=y}

(19)
≥E (x,y)∼Dθ

1{(x, y)∈ A}

(20)
=P (x,y)∼Dθ

(x, y)∈ A

(21)
≥ϵ,(22)
where the last inequality uses the boundary-mass condition (17). Hence δ(θ)≥ϵ >0 , establishing that the deployment
error is strictly bounded away from zero and cannot be eliminated by optimizing under the rational-agent assumption.
C. Proof of Proposition 4.3
C.1. Assumptions and Setup
Recall that bR(x) denotes the rational best response (Eq. (1)), and fR is the classifier optimized under the rational-agent
assumption, i.e., an empirical risk minimizer of
Rtrain(f) =E

L(f(b R(X)), Y)

(cf. Eq. (2)). (23)
Intuitively, fR is trained as if every agent manipulates to the rational endpoint bR(x). Under behavioral biases, however,
some agents abstain from manipulation entirely. This training–deployment mismatch is the root cause of over-defense.
We define theabstention set:
A=

x:b R(x)̸=xand the agent actually stays atx

,(24)
i.e., inputs where the rational model predicts manipulation but the behavioral agent abstains. We assume P(A)>0 , so
abstention occurs with non-negligible probability.
On the abstention setA, we define two key quantities:
τA := Pr

fR(X)̸=f R(bR(X))|X∈A

,(25)
εR := Pr

fR(bR(X))̸=Y|X∈A

.(26)
Here τA measures the probability that fR predicts differently at the true feature x versus the rational endpoint bR(x)—
capturing the extent to which the decision boundary has shifted due to over-defense. The quantity εR is the residual training
error off R at the rational endpointsb R(x), which is small when the classifier fits the training distribution well.
C.2. Discussion: Naturality of the Assumptions
Why P(A)>0 holds in practice.The abstention set A is non-empty whenever behavioral biases cause agents to
forgo manipulation that rational agents would undertake. This is precisely the over-defense scenario: agents subject to
loss aversion perceive the manipulation cost as disproportionately large, and agents subject to reference bias may assess
themselves as too far from the acceptance threshold to bother trying. Both mechanisms are well-documented in behavioral
economics (Kahneman & Tversky, 2013) and are directly captured by Pro-SF. The assumption P(A)>0 therefore holds
whenever any fraction of the agent population exhibits these biases, which is the defining condition of the BR-SC problem.
Why τA >2ε R holds in practice.The classifier fR is trained on the post-manipulation distribution DR, so its decision
boundary τ is optimized to correctly classify agents at their rational endpoints bR(x). Consequently, εR is small: fR
performs well at bR(x) by construction. In contrast, τA can be large: since fR shifts its boundary outward to defend against
rational manipulations, it systematically misclassifies agents who stay at x∈A and are on the “wrong side” of the shifted
boundary. The condition τA >2ε R thus formalizes the intuition that over-defense hurts most when the boundary shift is
non-trivial and the classifier is well-trained—a regime that is typical in practice, as confirmed by the monotone increase of
over-defense error with behavioral deviation in Fig. 2c.
16

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
C.3. Proof
Step 1: Loss decomposition on A.For any classifier f and any (x, y)with x∈A , the difference in 0–1 loss between the
true featurexand the rational endpointb R(x)satisfies:
L(f(x), y)− L(f(bR(x)), y) =1{f(x)̸=y, f(b R(x)) =y} −1{f(x) =y, f(bR(x))̸=y}.(27)
Taking conditional expectation overX∈A:
E

L(f(X), Y)− L(f(bR(X)), Y)|X∈A

= Pr(f(X)̸=Y, f(b R(X)) =Y|X∈A)−Pr(f(X) =Y, f(b R(X))̸=Y|X∈A).(28)
Step 2: Lower bound via set inclusions.We apply the following two inclusions:
{f(X)̸=Y, f(b R(X)) =Y} ⊇ {f(X)̸=f(b R(X))} \ {f(bR(X))̸=Y},(29)
{f(X) =Y, f(b R(X))̸=Y} ⊆ {f(b R(X))̸=Y}.(30)
Inclusion (29) states that whenever f disagrees between x and bR(x), this contributes to the first term unlessbR(x) is already
mislabeled. Inclusion (30) states that the second term is bounded by the training error at bR(x). Substituting into (28) gives
the lower bound:
E

L(f(X), Y)− L(f(bR(X)), Y)|X∈A

≥Pr(f(X)̸=f(b R(X))|X∈A)−2 Pr(f(b R(X))̸=Y|X∈A).
(31)
Step 3: Apply to fR and globalize.Substituting f=f R into (31) and using the definitions of τA and εR in Eqs. (25)–(26):
E

L(fR(X), Y)− L(fR(bR(X)), Y)|X∈A

≥τ A −2ε R.(32)
Multiplying byP(A)>0and adding the contribution fromX /∈A:
E[L(fR(X), Y)]−E[L(f R(bR(X)), Y)]≥P(A) (τ A −2ε R).(33)
Under the conditionτ A >2ε R, the right-hand side is strictly positive, yielding:
E[L(fR(x), y)]>E[L(f R(bR(x)), y)].(34)
Remark 4.Geometrically, fR shifts its decision boundary outward to guard against the rational endpoints bR(x). On the
abstention set A, agents remain at x, which now falls on the wrong side of the shifted boundary. The quantity τA −2ε R
measures the net excess deployment error due to this over-defense: τA count the fraction of abstaining agents misclassified
by the shifted boundary, while 2εR accounts for the small residual error fR already makes at the rational endpoints it was
trained on.
D. Proof of Proposition 4.5
D.1. Assumptions and Setup
Recall that bR(x) denotes the rational best response (Eq. (1)), and fR is the classifier optimized under the rational-agent
assumption, i.e., an empirical risk minimizer of
Rtrain(f) =E

L(f(b R(X)), Y)

(cf. Eq. (2)). (35)
Intuitively, fR is trained to defend against manipulations that end exactly at bR(x). Under behavioral biases such as
probability distortion and loss aversion, however, agents may overshoot the rational endpoint and land at bθ(x) with
bθ(x)̸=b R(x). Since fR was never trained to handle these overshoot points, its defense is insufficient—the essence of
under-defense.
We define theovershoot set:
B=

x:b R(x)̸=xandb θ(x)̸=b R(x)with overshoot beyondb R(x)

,(36)
17

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
i.e., inputs where the agent manipulates further than the rational endpoint along the manipulation direction. We assume
P(B)>0, so overshoot occurs with non-negligible probability.
On the overshoot setB, we define two key quantities:
τB := Pr

fR(bθ(X))̸=f R(bR(X))|X∈B

,(37)
εR := Pr

fR(bR(X))̸=Y|X∈B

.(38)
Here τB measures the probability that fR predicts differently at the overshoot point bθ(x) versus the rational endpoint
bR(x)—capturing how often agents land in regions where fR’s defense fails. The quantity εR is the residual training error
off R at the rational endpoints, which is small when the classifier fits the training distribution well.
D.2. Discussion: Naturality of the Assumptions
Why P(B)>0 holds in practice.The overshoot set B is non-empty whenever behavioral biases drive agents beyond the
rational manipulation endpoint. Two mechanisms in Pro-SF directly produce this:
• Probability distortion: agents overweight small probabilities of acceptance, causing them to perceive a higher chance of
success than actually exists. This inflated belief motivates more aggressive manipulation, pushing agents past the rational
endpointb R(x).
• Loss aversion: the fear of rejection amplifies the perceived cost of falling just short of the acceptance threshold, leading
agents to overshoot as a precautionary measure to ensure they clear the boundary.
Both mechanisms are integral to the BR-SC problem setting, so P(B)>0 holds whenever any fraction of the population
exhibits these biases—which is the defining condition of the problem we study.
Why τB >2ε R holds in practice.The classifier fR is trained on DR, so it is well-calibrated at the rational endpoints
bR(x): the residual error εR is small by construction. In contrast, τB can be large because the overshoot region bθ(x) lies
outside the support of the training distribution DR. The classifier fR has no training signal in this region, so its predictions
there are unreliable. The condition τB >2ε R. Therefore, captures the typical regime where the classifier performs well on
its training distribution but poorly on the unseen overshoot region—a standard manifestation of distribution shift, confirmed
empirically by the monotone increase of under-defense error with behavioral deviation in Fig. 2c.
D.3. Proof
Step 1: Loss decomposition on B.For any classifier f and any (x, y)with x∈B , the difference in 0–1 loss between the
overshoot pointb θ(x)and the rational endpointb R(x)satisfies:
L(f(b θ(x)), y)− L(f(bR(x)), y) =1{f(bθ(x))̸=y, f(b R(x)) =y} −1{f(bθ(x)) =y, f(b R(x))̸=y}.(39)
Taking conditional expectation overX∈B:
E

L(f(b θ(X)), Y)− L(f(bR(X)), Y)|X∈B

= Pr(f(b θ(X))̸=Y, f(b R(X)) =Y|X∈B)−Pr(f(b θ(X)) =Y, f(b R(X))̸=Y|X∈B).(40)
Step 2: Lower bound via set inclusions.We apply the following two inclusions:
{f(b θ)̸=Y, f(b R) =Y} ⊇ {f(bθ)̸=f(b R)} \ {f(bR)̸=Y},(41)
{f(b θ) =Y, f(b R)̸=Y} ⊆ {f(bR)̸=Y}.(42)
Inclusion (41) states that whenever f disagrees between bθ(x) and bR(x), this contributes to the loss increase unlessbR(x) is
already mislabeled. Inclusion (42) states that the loss-decreasing term is bounded by the training error at bR(x). Substituting
into (40) gives the lower bound:
E

L(f(b θ(X)), Y)−L(f(bR(X)), Y)|X∈B

≥Pr(f(b θ(X))̸=f(b R(X))|X∈B)−2 Pr(f(b R(X))̸=Y|X∈B).
(43)
18

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Step 3: Apply to fR and globalize.Substituting f=f R into (43) and using the definitions of τB and εR in Eqs. (37)–(38):
E

L(fR(bθ(X)), Y)− L(fR(bR(X)), Y)|X∈B

≥τ B −2ε R.(44)
Multiplying byP(B)>0and adding the contribution fromX /∈B:
E[L(fR(bθ(X)), Y)]−E[L(f R(bR(X)), Y)]≥P(B) (τ B −2ε R).(45)
Under the conditionτ B >2ε R, the right-hand side is strictly positive, yielding:
E

L(fR(bθ(x)), y)

>E

L(fR(bR(x)), y)

.(46)
□
Remark 5.Geometrically, fR learns to guard the rational endpoints bR(x), but the overshoot region around bθ(x) lies
outside the support of its training distribution. The quantity τB −2ε R measures the net excess deployment error: τB counts
the fraction of overshooting agents that land wheref R makes a different and incorrect prediction, while2ε R discounts the
small residual errorf R already makes at the rational endpoints it was trained on.
E. Pro-SF Improves Deployment Guarantees
In this appendix, we show that, by reducing the mismatch between the training-time post-manipulation distribution and
the deployment distribution, Pro-SF yields a strictly stronger deployment-performance guarantee than training under the
rational-agent assumption.
E.1. Setup.
Let Dθ denote the true post-manipulation (deployment) distribution induced by the behavioral response bθ. Let DR denote
the post-manipulation distribution induced by the rational response bR. Similarly, let DP denote the post-manipulation
distribution induced by the Prospect-Guided responseb P (Pro-SF). Define the population risk under a distributionDby
RD(f) :=E (x,y)∼D

L(f(x), y)

,(47)
where the loss satisfies0≤ L ≤1. Let
fR ∈arg min f RDR (f), f P ∈arg min f RDP (f)(48)
be classifiers optimized on the rational and Pro-SF induced training distributions, respectively. Finally, let
R⋆ := inf
f
RDθ (f)(49)
denote the Bayes-optimal (best achievable) deployment risk under the true post-manipulation distributionD θ.
E.2. Lemma (TV controls expectation shift).
For any two distributionsP, QonX × Yand any measurable functiong:X × Y →[0,1],

EP [g]−E Q[g]

 ≤TV(P, Q).(50)
Proof. This is a standard property of total variation distance: by the variational characterization,TV(P, Q) = supA |P(A)−
Q(A)|= sup 0≤g≤1 |EP [g]−E Q[g]|.Applying it to the giveng∈[0,1]yields (50).
Proposition (excess deployment risk is controlled by mismatch).For any surrogate training distribution bD and the
corresponding optimizer bf∈arg min f R bD(f),the deployment excess risk satisfies
RDθ ( bf)−R ⋆ ≤2 TV  Dθ, bD  .(51)
19

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Proof. Let f ⋆ ∈arg min f RDθ (f) be a Bayes-optimal classifier under Dθ. By Lemma (50) applied to the bounded loss,
for any classifierf,
RDθ (f)≤R bD(f) + TV(Dθ, bD), R bD(f)≤R Dθ (f) + TV(Dθ, bD).(52)
Using bfoptimal for bD,
R bD( bf)≤R bD(f ⋆).(53)
Now chain the inequalities:
RDθ ( bf)≤R bD( bf) + TV(Dθ, bD)
≤R bD(f ⋆) + TV(Dθ, bD)
≤R Dθ (f ⋆) + 2 TV(Dθ, bD)(by (52))
=R ⋆ + 2 TV(Dθ, bD).
Rearranging gives (51).
E.3. Corollary.
Applying (51) with bD=D R and bD=D P yields
RDθ (fR)−R ⋆ ≤2 TV  Dθ,D R  ,(54)
and
RDθ (fP )−R ⋆ ≤2 TV  Dθ,D P  .(55)
Therefore, whenever Pro-SF reduces behavioral mismatch in the sense that
TV

Dθ,D P

<TV

Dθ,D R

,(56)
it provides astrictly strongerdeployment-performance guarantee than training under the rational-agent assumption, since
the right-hand side upper bound in (55) is strictly smaller than that in (54).
F. Existence of Stackelberg Equilibrium Under Pro-SF
This appendix establishes three structural properties of the Stackelberg game induced by Pro-SF: existence of a Stackelberg
equilibrium (Proposition F.2), local stability under best-response dynamics (Proposition F.3), and local uniqueness of the
equilibrium (Corollary F.4).
F.1. Setup
The Pro-SF game follows the classic Stackelberg structure with two players:
•Leader(classifier): chooses a parameter vectorθ∈Θ, whereΘ⊂R d is the classifier parameter space.
• Follower(agent): observes θ and chooses a manipulated feature vector x′ ∈ Xto maximize the prospect-based utility
UP (x, x′;ϕ)defined in Eq. (12).
Given any classifier parameterθ, the agent’s best-response function is:
bP (x;θ)∈arg max x′∈X UP (x, x′;ϕ),(57)
and the leader’s objective induced by this response is:
F(θ) =E (x,y)∼D[L(fθ(bP (x;θ)), y)].(58)
20

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Definition F.1(Stackelberg Equilibrium under Pro-SF).A pair (θ∗, b∗(·)) is aStackelberg equilibriumof the Pro-SF game
if:
(i)Follower optimality: for everyx∈ X,
b∗(x)∈arg max
x′∈X UP (x, x′;ϕ);(59)
(ii)Leader optimality:
θ∗ ∈arg min
θ∈Θ
E(x,y)∼D[L(fθ(b∗(x)), y)].(60)
F.2. Proposition: Existence of Stackelberg Equilibrium
Proposition F.2(Existence).Under the Pro-SF framework, suppose the following conditions hold:
(i) The feasible manipulation spaceX ⊂R p is compact;
(ii) The classifier parameter spaceΘ⊂R d is compact;
(iii) The prospect-based utilityU P (x, x′;ϕ)is continuous inx ′ for every fixedxandϕ;
(iv) The classifier scoref θ(x′)is continuous in bothx ′ andθ, and the loss functionLis continuous.
Then the Pro-SF game admits at least one Stackelberg equilibrium(θ ∗, b∗(·)).
Proof.We establish existence in three steps.
Step 1: Existence of the follower’s best response.Fix any θ∈Θ and x∈ X. We verify that UP (x, x′;ϕ) satisfies
condition (iii) by inspecting each component in Eq. (12):
• The classifier scorep(x ′) =σ(f θ(x′))is continuous inx ′ by condition (iv) and the continuity of the sigmoidσ;
• The value functionv(·)in Eq. (9) is a power function with exponentsα, β∈(0,1], hence continuous onR ≥0;
• The probability-weighting functionsw +(·)andw −(·)in Eq. (10) are smooth for allγ∈(0,1];
• The reference pointr∈[0,1]is a fixed scalar determined by Eq. (11), independent ofx ′;
• The manipulation costc(x, x′)(e.g., Mahalanobis distance) is continuous inx ′ for fixedx.
Since UP (x, x′;ϕ) is a finite composition of continuous functions, it is continuous in x′. By condition (i), X is compact.
Applying the Weierstrass extreme-value theorem, the maximum
max
x′∈X UP (x, x′;ϕ)(61)
is attained, so the argmax set is non-empty:
bP (x;θ) := arg max x′∈X UP (x, x′;ϕ)̸=∅.(62)
Hence the follower’s best-response functionb P (x;θ)exists for everyx∈ Xandθ∈Θ.
Step 2: Existence of the leader’s optimum.Given the follower’s best-response mapping bP (·;θ) established in Step 1, the
leader’s objective is:
F(θ) =E (x,y)∼D[L(fθ(bP (x;θ)), y)].(63)
We show that F is continuous on Θ. By the maximum theorem (Berge, 1963), since UP (x, x′;ϕ) is continuous in (x′, θ)
and X is compact, the correspondence θ7→arg max x′ UP (x, x′;ϕ) is upper hemicontinuous, and the value function
θ7→max x′ UP (x, x′;ϕ) is continuous in θ. Under a measurable selection of bP (x;θ) , the composed map θ7→f θ(bP (x;θ))
21

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
is continuous in θ by condition (iv). Since L is continuous and the expectation preserves continuity (by the dominated
convergence theorem, as L is bounded), F(θ) is continuous on Θ. Since Θ is compact by condition (ii), the Weierstrass
theorem guarantees the existence of
θ∗ ∈arg min
θ∈Θ
F(θ).(64)
Step 3: Construction of the equilibrium.Let b∗(x) :=b P (x;θ ∗) for every x∈ X . By Step 1, b∗(x)∈
arg maxx′ UP (x, x′;ϕ) for every x, so follower optimality holds. By Step 2, θ∗ minimizes F(θ) =E[L(f θ(b∗(x)), y)]over
Θ, so leader optimality holds. Therefore,(θ ∗, b∗(·))is a Stackelberg equilibrium of the Pro-SF game.
Remark 6.Condition (i) is naturally satisfied in practice: real-world features (income, credit score, health metrics) all
lie within known finite ranges. Condition (ii) is enforced by standard regularization in classifier training. Conditions (iii)
and (iv) hold for all classifiers and cost functions used in our experiments.
F.3. Proposition: Local Stability of Stackelberg Equilibrium
To analyze stability, we introduce the local best-response mappings of the two players. Given an equilibrium (θ∗, b∗),
suppose there exist neighborhoodsU ⊂Θofθ ∗ andVofb ∗ (in an appropriate function space) such that:
• The follower’s best response is locally single-valued and continuously differentiable in θ, defining a mapping Φ :U → V,
θ7→b θ, whereb θ(x) = Φ(θ)(x);
• The leader’s best response to a given follower mapping b is locally single-valued and continuously differentiable in b,
defining a mappingΨ :V → U,b7→θ b.
Since(θ ∗, b∗)is a Stackelberg equilibrium, we haveb ∗ = Φ(θ∗)andθ ∗ = Ψ(b∗). Define the composed mapping:
T:= Ψ◦Φ :U → U, T(θ) = Ψ(Φ(θ)).(65)
Note thatθ ∗ is a fixed point ofT:
T(θ ∗) = Ψ(Φ(θ∗)) = Ψ(b∗) =θ ∗.(66)
Proposition F.3(Local Stability).Let (θ∗, b∗) be a Stackelberg equilibrium under Pro-SF , and let T= Ψ◦Φ be the
composed mapping defined in Eq. (65). Suppose T is locally contractive on U: there exists q∈(0,1) such that for all
θ1, θ2 ∈ U,
∥T(θ 1)−T(θ 2)∥ ≤q∥θ 1 −θ 2∥.(67)
Then(θ ∗, b∗)is locally stable: for any initializationθ 0 ∈ U, the best-response iteration
θt+1 =T(θ t), b t := Φ(θ t),(68)
satisfiesθ t →θ ∗ andb t →b ∗ ast→ ∞, with geometric rate:
∥θt −θ ∗∥ ≤q t ∥θ0 −θ ∗∥.(69)
Proof.We establish the result in four steps.
Step 1:θ ∗ is a fixed point ofT.Since(θ ∗, b∗)is a Stackelberg equilibrium:
b∗ = Φ(θ∗), θ ∗ = Ψ(b∗).(70)
Therefore:
T(θ ∗) = (Ψ◦Φ)(θ ∗) = Ψ(b∗) =θ ∗.(71)
Henceθ ∗ is a fixed point ofTinU.
Step 2: Convergence of the leader by Banach fixed-point theorem.Since T:U → Uis a contraction with constant
q∈(0,1)on the complete metric spaceU(as a closed subset ofR d), the Banach fixed-point theorem guarantees:
(a)Thas auniquefixed point inU, which isθ ∗;
22

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
(b) For anyθ 0 ∈ U, the iterationθt+1 =T(θ t)converges geometrically:
∥θt −θ ∗∥ ≤q t ∥θ0 −θ ∗∥ →0ast→ ∞.(72)
Step 3: Convergence of the follower.Since Φ :U → Vis continuous (by the assumption that the follower’s best response
is continuously differentiable inθ), the geometric convergenceθ t →θ ∗ implies:
bt := Φ(θ t)→Φ(θ ∗) =b ∗ ast→ ∞.(73)
Step 4: Conclusion.Combining Steps 2 and 3, we have (θt, bt)→(θ ∗, b∗) geometrically as t→ ∞, for any initialization
θ0 ∈ U. This establishes that the best-response dynamics return to (θ∗, b∗) from any sufficiently close initialization, i.e., the
Stackelberg equilibrium is locally stable.
Remark 7.The contraction condition (67) is interpretable in terms of the underlying problem structure: it holds when the
manipulation cost is sufficiently strong relative to the gain from manipulation in a neighborhood of the equilibrium, so that
small perturbations to the classifier induce only small perturbations to agents’ responses, and vice versa. This is a standard
sufficient condition for stability in Stackelberg games and leader-follower systems (Li & Sethi, 2017).
F.4. Corollary: Local Uniqueness of Stackelberg Equilibrium
Corollary F.4(Local Uniqueness).Under the conditions of Proposition F .3, (θ∗, b∗) is the unique Stackelberg equilibrium
inU.
Proof. Suppose (θ, b)is any Stackelberg equilibrium contained in U × V. By follower optimality, b= Φ(θ) . By leader
optimality,θ= Ψ(b). Substituting,
θ= Ψ(b) = Ψ(Φ(θ)) =T(θ).(74)
Hence θ is a fixed point of T in U. By Step 2(a) of Proposition F.3, the Banach fixed-point theorem guarantees that T has a
unique fixed point inU, which isθ ∗. Thereforeθ=θ ∗, and consequently:
b= Φ(θ) = Φ(θ ∗) =b ∗.(75)
Hence(θ, b) = (θ∗, b∗), establishing that(θ ∗, b∗)is the unique Stackelberg equilibrium inU × V.
G. Additional Experiment
G.1. Dataset
We evaluate our framework on five datasets, including four real-world and one synthetic benchmarks:
•Credit(Yeh, 2009): Credit card default prediction based on financial records.
•Adult(Becker & Kohavi, 1996): Income classification from census features.
• Diabetes(Teboul, 2015): A medical dataset containing clinical and demographic attributes for diabetes risk assessment.
•German(Hofmann, 1994): Credit risk classification based on personal and financial profiles.
•Spam(Hopkins et al., 1999): Email spam detection based on textual and statistical features.
•Synthetic(Lopez-Rojas et al., 2016): Simulated mobile transaction data for fraud detection.
G.2. Notation Table
In the modeling process of Section 5, we designed a series of formulas and parameters. Here, we provide a notation
table (Tab. 4) to facilitate a clearer understanding of our Pro-SF.
We preprocess each dataset following standard practice (categorical encoding, normalization, and train/validation/test splits).
23

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 3.Summary of the public datasets used in our experiments.
Dataset #Features #Instances #Classes
Adult (Becker & Kohavi, 1996) 14 48,842 2
Credit (Yeh, 2009) 23 30,000 2
German (Statlog) (Hofmann, 1994) 20 1,000 2
Spambase (Hopkins et al., 1999) 57 4,601 2
CDC Diabetes (Teboul, 2015) 21 253,680 2
Synthetic (PaySim) (Lopez-Rojas et al., 2016) 10 6,362,620 2
Table 4.Notation of prospect-guided utility and default experimental values.
Symbol Meaning Default Value (Experiment)
α, βCurvature parameters (diminishing sensitivity)α= 0.8, β= 0.7
κLoss aversion coefficient2.25
γProbability distortion parameter0.7
rReference point (discretized probability){0,0.2,0.4,0.6,0.8}
w(p)Probability weighting functions Inverse-S function (Eq. (10))
c(x′,x)Manipulation cost function Mahalanobis distance
G.3. Implementation Details
All experiments are conducted on a single NVIDIA TITAN V (24GB) GPU. We implement the classifier f as a logistic
regression model trained with cross-entropy loss and learning rate 10−3. In prospect-theoretic utility, we set the curvature
parameters α= 0.8 and β= 0.7 , the loss aversion coefficient κ= 2.25 , and the probability-weighting parameter γ= 0.7
by default. In the mixed agent behavior paradigm, the proportion is set as π= 0.2 . This choice reflects a realistic scenario
where only a minority of agents behave in a fully rational manner, while the majority exhibit behavioral biases (Tversky &
Kahneman, 1992; Ariely & Jones, 2008). Ablation studies are conducted on theCreditandSyntheticdatasets under themixed
agent regime, representing real-world and controlled settings. To ensure robustness, we perform 10-fold cross-validation on
all datasets.
In simulating agents’ real-world manipulation process, we argue that agents need to exhibit heterogeneous behavioral biases.
To capture this diversity, we randomly divide agents into several subgroups (e.g., three or four groups), and assign each
subgroup different parameter combinations. This design mimics the fact that individuals in reality adopt distinct subjective
strategies when manipulating their features. By contrast, when training the classifier to anticipate manipulations, we adopt
a fixed parameter setting across all agents. This stabilizes the optimization process and ensures fair comparison across
experiments, while still allowing evaluation against heterogeneous agent behaviors at deployment.
For example, in one experimental run, the agents are randomly split into three groups. The first group is assigned
(κ= 2.00, γ= 0.70), the second group(κ= 2.25, γ= 0.75), and the third group(κ= 1.80, γ= 0.65).
G.4. More Ablation Studies
More Ablation resultsof our parameter analysis (includingπ, r,(α, β), κ, andγ) are shown in Table 5 and Fig. 6.
An alternative of probability distortion.The two-parameterPrelecfunction (Prelec, 1998) is :
w(p) = exp

−η(−lnp) ϕ , ϕ, η >0.(76)
Compared to the one-parameter form used in the main text, the Prelec function provides greater flexibility. The parameter ϕ
controls the shape of the curve: when ϕ <1, the function takes an inverse-S form (small probabilities are given too much
weight and large probabilities too little), while ϕ >1 produces an S-shape (the opposite pattern). In line with behavioral
evidence, we restrict to the case ϕ <1 , which produces the inverse- S form. The parameter η adjusts how strong this
distortion is overall, with largerηleading to a stronger down-weighting of probabilities across the board.
The ablation experimental results are summarized in Table 6.
24

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 5.Overall accuracy (%) of rational-based classifiers and prospect-guided models across datasets under different π in mixed behavior.
Classifier Mixedπ Datasets
Adult Credit Diabetes German Spam Synthetic
Rational-based
0.173.96 ±1.55 71.84±1.90 66.51±1.62 70.10±1.88 78.85±1.71 72.88±1.70
0.274.31 ±1.51 72.12±1.87 66.81±1.65 70.43±1.92 79.16±1.63 73.15±1.74
0.474.53 ±1.57 72.37±1.85 67.05±1.68 70.64±1.95 79.42±1.59 73.41±1.73
Pro-SF (ours)
0.178.92 ±1.74 79.32±1.66 72.23±1.55 76.45±1.68 86.02±1.61 82.60±1.58
0.278.68 ±1.77 79.13±1.63 72.01±1.58 76.24±1.71 85.71±1.52 82.34±1.56
0.478.50 ±1.79 78.92±1.65 71.84±1.60 76.08±1.73 85.38±1.56 82.14±1.57
Table 6.Accuracy comparison between the normalized power function and the Prelec probability weighting across multiple datasets under
different parameter settings.
Weighting Datasets
Credit Adult Diabetes German Spam Synthetic
γ= 0.65 78.68 ±1.25 79.13±1.10 72.01±1.05 76.24±1.20 85.71±1.18 82.34±1.15
Prelec(ϕ= 0.65, η= 1.00) 78.50 ±1.28 79.00±1.12 71.80±1.08 76.10±1.18 85.42±1.21 82.10±1.14
γ= 0.70 78.78 ±1.22 79.22±1.09 72.12±1.06 76.31±1.17 85.89±1.16 82.27±1.13
Prelec(ϕ= 0.68, η= 1.00) 78.70 ±1.24 79.10±1.10 71.96±1.07 76.20±1.15 85.60±1.19 82.15±1.12
γ= 0.80 78.82 ±1.20 79.24±1.08 72.18±1.05 76.33±1.15 86.02±1.15 82.12±1.11
Prelec(ϕ= 0.75, η= 1.00) 78.79 ±1.22 79.20±1.09 72.05±1.06 76.30±1.14 85.78±1.17 82.08±1.10
G.5. Results Analysis
Additional parameter analysis results are summarized in Table 5 and Fig. 6, covering the mixture ratio π, the reference
point r, the weighting parameters (α, β), the loss-aversion factor κ, and the probability distortion parameter γ. As shown in
Table 5, the proposed Pro-SF consistently outperforms the rational baseline across datasets, and the performance advantage
holds for different proportions of mixed behavioral agents.
As shown in Fig. 6, when the discrete reference points are set to four or five bins, the accuracy remains stable, showing that
the framework is robust under reasonably fine discretizations. However, when only three bins are used, we observe a slight
performance drop. This is because with only three bins, the reference points become too sparse, forcing many agents with
different true self-assessments to be grouped into the same anchor. As a result, the model cannot capture the finer granularity
of subjective evaluations, and the induced manipulations are less accurately represented. This mismatch slightly weakens
the behavioral modeling and leads to a small drop in accuracy.
Moreover, Fig. 6 show ablations under two different (α, β)settings. In both cases, the accuracy curves remain stable,
indicating that the results are not sensitive to moderate shifts of these parameters. Across a wide range of κ and γ values,
accuracy fluctuations are small (within ±0.3%), confirming that the framework is not overly dependent on fine-tuning these
behavioral parameters.
Through extensive experimental design, we identified parameter settings of the normalized power function and the Prelec
function that yield comparable weighting curves. As shown in Table 5, when evaluated under these matched configurations,
the resulting accuracies across datasets are nearly identical. For example, results with r= 0.7 are largely similar to results
with ϕ= 0.68, η= 1.0 . This means our framework can work with both types of probability distortion, as long as the
parameters are set to produce comparable shapes.
25

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.85, = 0.75)
=0.65
=0.70
=0.80
(a)r∈ {0,0.2,0.4,0.6,0.8}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.85, = 0.75)
=0.65
=0.70
=0.80
 (b)r∈ {0,0.3,0.6,0.9}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.85, = 0.75)
=0.65
=0.70
=0.80
 (c)r∈ {0,0.4,0.7}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.8, = 0.8)
=0.65
=0.70
=0.80
(d)r∈ {0,0.2,0.4,0.6,0.8}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.8, = 0.8)
=0.65
=0.70
=0.80
 (e)r∈ {0,0.3,0.6,0.9}
2.0 2.25 2.5 2.75
 (loss parameter)
75.8
76.0
76.2
76.4Accuracy (%)
( = 0.8, = 0.8)
=0.65
=0.70
=0.80
 (f)r∈ {0,0.4,0.7}
Figure 6.Parameter ablation results with parametersκ, γ, rwith different(α, β).
H. Validation with Real World Manipulation Data
In this section, we provide further empirical support for our behavioral modeling. Recent work (Ebrahimi et al., 2025)
conducted controlled human-subject experiments across several strategic-classification scenarios (e.g., hiring, medical
decision-making). Their statistical findings show that:
• Human manipulation behaviorsystematically deviates from the rational best-response assumption;
• Individuals do not track the optimal boundary or follow theoretically optimal manipulation trajectories;
• Over-reaction and under-reaction behaviors appear frequently in practice.
These results provide direct evidence thatbehavioral biases must be incorporatedinto strategic-classification models,
supporting the foundation of our Prospect-Based Utility.
To further validate our framework, we evaluate Pro-SF on two real human manipulation datasets released in (Ebrahimi et al.,
2025): the job hiring dataset and the medical treatment dataset.
We compare two models:
•Rational-SF: the classical rational strategic-classification model;
• Pro-SF: our proposed Prospect-based strategic framework, behavioral parameters used in Pro-SFϕ={α= 0.78, β=
0.72, κ= 2.20, γ= 0.74}..
For each dataset, we report:
•Classification Accuracy;
• Manipulation Deviation: the average ℓ2 distance between real human manipulation x→x ′ and model-predicted
manipulationˆx′.
26

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 7.Results on Human Manipulation Datasets: Job Hiring and Medical Treatment.
Job Hiring Dataset Medical Treatment Dataset
Model Accuracy↑Manip. Dev.↓ Model Accuracy↑Manip. Dev.↓
Rational-SF 68.4% 0.297 Rational-SF 71.9% 0.267
Pro-SF 79.8% 0.148 Pro-SF 78.3% 0.181
Across both datasets, Pro-SF consistently achieves higher predictive accuracy, lower Manipulation deviation, and more
stable alignment with human behavior.
These findings indicate thatPro-SF closely matches actual human manipulation patterns, offering strong empirical
support for its validity.
I. Learnability of Behavioral Parameters
This appendix studies whether the behavioral parameters ϕ= (α, β, κ, γ)in the prospect-based utility can beidentified from
observed strategic manipulation behavior. We show that these parameters can be reliably inferred from both real human
manipulation data and heterogeneous agent populations, and that classifier performance remains stable under estimation
noise.
I.1. Inverse Behavioral Inference via Discrete Choice
Given observed manipulation pairs (xi, x′ i), we estimate the behavioral parameters by solving an inverse decision problem.
Rather than assuming agents optimize over the full continuous feature space, we adopt a bounded rationality perspective and
assume that agents choose among a finite set of salient manipulation options.
Formally, for each original feature vector x, we construct a candidate manipulation set C(x) consisting of feasible local
manipulations (including x itself). The likelihood of observing a manipulation x′ i is modeled using a softmax (Boltzmann)
choice rule:
Pϕ(x′ i |x i) = exp

τ UP(xi, x′ i;ϕ)  P
x′′∈C(xi)
exp

τ UP(xi, x′′;ϕ)  ,(77)
whereτ >0controls decision stochasticity.
This formulation follows standard practice in inverse decision modeling, random utility models, and quantal response
equilibria, and reflects that agents consider only a limited set of plausible manipulation options rather than optimizing
globally.
The behavioral parameters are then inferred via maximum likelihood estimation:
ϕ∗ = arg max
ϕ
X
i
logP ϕ(x′ i |x i).(78)
I.2. Learning Parameters from Real Human Manipulation Data
We first evaluate whether the behavioral parameters can be learned from real human decision data. We use two real-world
manipulation datasets introduced in (Ebrahimi et al., 2025): ajob hiringtask and amedical treatmenttask.
For each dataset, we estimate ˆϕ using the likelihood objective above and evaluate the resulting Pro-SF classifier. Table 8
reports the learned parameters and classification accuracy.
These results demonstrate that prospect-based behavioral parameters areidentifiable from real human manipulation
trajectories, supporting that Pro-SF does not rely on hand-tuned assumptions.
27

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 8.Learned behavioral parameters and accuracy on real human manipulation datasets.
Dataset Learned Parameters ˆϕAccuracy (%)
Job Hiring{α=0.79, β=0.73, κ=2.18, γ=0.72}79.8
Medical Treatment{α=0.81, β=0.70, κ=2.25, γ=0.71}78.3
I.3. Heterogeneous Strategic Populations
To further test robustness, we consider mixed agent populations containing both rational and behavioral agents. For a given
proportionπof rational agents:
• Behavioral agents (1−π) : each agent draws individual parameters ϕi from a distribution Pϕ and selects manipulations
according to a noisy prospect-based decision:
x′ i = arg max x′ UP(xi, x′;ϕ i) +ϵ i, ϵ i ∼ N(0, σ2).(79)
• Rational agents (π): agents follow the classical strategic classification model, maximizing acceptance probability
minus manipulation cost.
We evaluate settingsπ∈ {0.2,0.4,0.6}, corresponding to increasing dominance of rational behavior.
I.4. Learned Parameters and Performance
Tables 9, 10, and 11 report the learned parameters ˆϕ and the corresponding post-gaming accuracy achieved by the classifier
trained with the estimated behavioral model.
Table 9.Learned parameters and accuracy withπ= 0.2(20% rational agents).
Dataset Learned Parameters ˆϕAccuracy (%)
Adult{α= 0.78, β= 0.72, κ= 2.20, γ= 0.74}81.42
Credit{α= 0.80, β= 0.70, κ= 2.15, γ= 0.71}82.30
German{α= 0.81, β= 0.70, κ= 2.25, γ= 0.72}79.21
Synthetic{α= 0.79, β= 0.71, κ= 2.28, γ= 0.73}85.05
Table 10.Learned parameters and accuracy withπ= 0.4(40% rational agents).
Dataset Learned Parameters ˆϕAccuracy (%)
Adult{α= 0.78, β= 0.74, κ= 2.20, γ= 0.74}81.32
Credit{α= 0.80, β= 0.70, κ= 2.10, γ= 0.70}82.20
German{α= 0.80, β= 0.72, κ= 2.18, γ= 0.71}79.25
Synthetic{α= 0.77, β= 0.75, κ= 2.20, γ= 0.72}84.91
Tables 9–11 report the inferred parameters and post-manipulation accuracy. Across all values of π, the estimated parameters
remain stable and yield consistent classification performance.
These results indicate that: (i) behavioral parameters are learnable from heterogeneous strategic behavior; (ii) Pro-SF is
robust to parameter estimation noise; and (iii) accurate modeling does not require access to agents’ true latent parameters.
J. Behavioral Illustration
We provide two illustrative contexts that highlight these mechanisms and motivate our formulation.
28

Beyond Rational Illusion: Behaviorally Realistic Strategic Classification
Table 11.Learned parameters and accuracy withπ= 0.6(60% rational agents).
Dataset Learned Parameters ˆϕAccuracy (%)
Adult{α= 0.78, β= 0.76, κ= 2.05, γ= 0.70}81.28
Credit{α= 0.78, β= 0.74, κ= 2.03, γ= 0.68}82.16
German{α= 0.80, β= 0.73, κ= 2.10, γ= 0.69}79.08
Synthetic{α= 0.78, β= 0.75, κ= 2.15, γ= 0.70}84.84
J.1. Financial Investment.
Consider two individuals facing the same investment opportunity: investing $10,000 with a 60% chance of gaining $20,000
and a 40% chance of losing the entire principal.
A classical rational utility model predicts that both investors should take the action because the expected payoff is positive.
In practice, however, behavior diverges. An individual with $100,000 in savings may choose to invest, whereas another with
only $20,000 may refrain, even though the expected value is identical.
This discrepancy arises because the two individuals have differentreference points: a $10,000 loss represents 10% of the
former’s wealth but 50% of the latter’s. When combined with loss aversion, the same monetary loss induces a substantially
larger psychological cost for the low-wealth individual. The Prospect-Based Utility accounts for this effect through the
reference-point term r and the asymmetric loss-weighting parameter κ, leading to distinct optimal decisions for the two
agents.
J.2. Disease Screening.
In health-risk environments, individuals often display behavior that cannot be explained by classical rational models. Even
when the true prevalence of a disease is extremely low (e.g., 0.1%), people may repeatedly undergo medical testing or
stockpile medication.
Such behavior reflects probability distortion: very small probabilities are overweighted and treated as non-negligible risks.
Moreover, external events (e.g., alarms, exposure, or stress) may shift one’s psychological reference point from “I am
healthy” to “I might already be at risk,” sharply increasing the perceived cost of inaction. Under classical SC models, a 0.1%
risk should induce only minimal adjustment.
In contrast, Prospect-Based Utility naturally captures this form of overreaction through the weighting function w(p) and the
dynamic reference pointr.
Together, these examples illustrate behavioral patterns that classical rational utilities cannot encode, motivating the need for
a prospect-theoretic formulation in strategic classification.
29
