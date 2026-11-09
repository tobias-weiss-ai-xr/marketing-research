---
title: 'Modelling Customer Lifetime Value under Endogenous Marketing Interventions: A Structural Bayesian
  Approach'
url: https://doi.org/10.31033/ijemr/16.4.2026.1938
category: survey
subcategory: framework
date: 2026-08
venue: International Journal of Engineering and Management Research
authors:
- Sudipkumar Ghanvat
- Shreya Joshi
- Aditi Shintre
source: openalex-oa
pdf_url: https://ijemr.vandanapublications.com/index.php/j/article/download/1938/2040
pages: 11
chars: 41387
fetched_at: '2026-11-08T19:47:52+00:00'
kb_version: 1
---

# Modelling Customer Lifetime Value under Endogenous Marketing Interventions: A Structural Bayesian Approach

International Journal of Engineering
and Management Research
2026 Volume 16 Number 4 August
E-ISSN:2250-0758
P-ISSN:2394-6962
Research Article
Customer Lifetime Value
Publisher
www.vandanapublications.com
Modelling Customer Lifetime Value under Endogenous Marketing
Interventions: A Structural Bayesian Approach
Ghanvat S1, Joshi S2, Shintre A3*
DOI:10.31033/IJEMR/16.4.2026.1938
1 Sudipkumar Ghanvat, Sr. Director & Head - Data & AI, VRIO Digital Dallas, United States of America.
2 Shreya Joshi, Sr. Data Analyst, American Airlines, Texas, United States of America.
3* Aditi Shintre, Research Engineer, Neowesolutize Technology Pvt. Ltd., Pune, Maharashtra, India.
Customer lifetime value (CLV) is the present value of future profits from customer relationships and
serves as a fundamental metric for resource allocation in modern marketing. Extant probabilistic
approaches—notably the Pareto/NBD and BG/NBD models—estimate CLV from observed purchase
histories but often overstate marketing effectiveness by treating marketing interventions as
exogenous. In practice, however, firms allocate marketing strategically, targeting customers based
on observable and unobservable characteristics that also predict purchase behavior, thereby inducing
endogeneity. We develop a structural Bayesian framework that jointly models (i) the customer
purchase process as a function of latent autonomous propensity and marketing responsiveness, and
(ii) the firm’s marketing assignment process as a function of observable customer attributes and
estimated response signals. By integrating causal inference principles with hierarchical Bayesian
modeling, the proposed framework mitigates bias arising from endogenous marketing assignment
and enables more reliable estimation of marketing effects on CLV. Monte Carlo simulations calibrated
to retail e-commerce settings show that conventional CLV models can overestimate marketing
elasticity by 20–40%, with bias increasing in targeting sophistication. The proposed approach
recovers more accurate heterogeneous treatment effects, supporting improved customer
segmentation and more effective budget allocation. Methodologically, this research extends causal
inference to the lifetime value setting; substantively, it quantifies and corrects a key source of bias
in contemporary CLV practice.
Keywords: Customer Lifetime Value (CLV), Endogeneity in Marketing, Structural Bayesian Modeling,
Causal Inference, Targeted Marketing Optimization
Corresponding Author How to Cite this Article To Browse
Aditi Shintre, Research Engineer, Neowesolutize
Technology Pvt. Ltd., Pune, Maharashtra, India.
Email:
Ghanvat S, Joshi S, Shintre A, Modelling Customer
Lifetime Value under Endogenous Marketing
Interventions: A Structural Bayesian Approach. Int J
Engg Mgmt Res. 2026;16(4):65-75.
Available From
https://ijemr.vandanapublications.com/index.php/j/a
rticle/view/1938
Manuscript Received Review Round 1 Review Round 2 Review Round 3 Accepted
2026-07-10 2026-07-25 2026-08-12
Conflict of Interest Funding Ethical Approval Plagiarism X-checker Note
None Nil Yes 4.18
© 2026 by Ghanvat S, Joshi S, Shintre A and Published by Vandana Publications. This is an Open Access article licensed under a Creative
Commons Attribution 4.0 International License https://creativecommons.org/licenses/by/4.0/ unported [CC BY 4.0].
Int J Engg Mgmt Res 2026;16(4) 65

1. Introduction
Customer lifetime value (CLV)—the present value of
future cash flows attributable to a customer over
the duration of the relationship—has emerged as a
central metric for assessing customer profitability
and guiding strategic allocation of marketing
resources. Organizations rely on CLV estimates to
determine optimal acquisition spending, identify
high-value customers for retention, and evaluate
the long-term value of customer portfolios. Given its
central role in decision-making, the accuracy of CLV
estimation is critical: biased estimates can misdirect
marketing investments, leading to inefficient
resource allocation and suboptimal targeting
strategies.
The past two decades have witnessed substantial
advances in probabilistic CLV modeling. The
canonical Pareto/NBD model (Shahabikargar et al.,
2026) and its successor, the BG/NBD (Beta-
Geometric/Negative Binomial Distribution) model
(van Oostenbruggen and Cavicchia, 2022),
represent the methodological state of practice in
both academic research and industry applications.
These frameworks decompose customer behavior
into latent purchase and attrition processes, while
hierarchical Bayesian extensions allow for
heterogeneity and improved predictive performance.
Further extensions incorporating time-varying
covariates and customer-level observables have
enhanced their empirical applicability. However,
despite these advances, most CLV models rely on
the simplifying assumption that marketing
interventions are exogenous. In practice, firms
allocate marketing strategically, targeting customers
based on observable characteristics and inferred
propensities that are themselves correlated with
purchase behavior.
This non-random assignment of marketing
introduces an endogeneity problem with important
implications (Malodia et al., 2023). When customers
exposed to marketing exhibit higher purchase rates
than unexposed customers, it is unclear whether the
observed difference reflects the causal effect of
marketing or the selective targeting of inherently
higher-propensity customers (Ascarza, 2018).
Ignoring this selection mechanism leads to upwardly
biased estimates of marketing effectiveness,
thereby overstating returns on marketing
investment.
Such bias propagates through CLV calculations,
distorting customer valuation, segmentation, and
budget allocation decisions (Ali and Shabn, 2024).
This paper makes three contributions. First, we
formalize the identification challenge arising from
endogenous marketing assignment in CLV models,
showing how strategic targeting induces correlation
between marketing exposure and unobserved
determinants of purchase behavior. Second, we
develop a structural Bayesian framework that jointly
models customer purchase behavior and firm
marketing assignment decisions, thereby improving
identification of causal marketing effects in the
presence of selection bias. Third, using Monte Carlo
simulations, we demonstrate that accounting for
endogenous marketing substantially alters CLV
estimates and customer rankings, with meaningful
implications for targeting and resource allocation.
By integrating insights from causal inference with
hierarchical probabilistic modelling, the proposed
framework advances both the methodological and
practical understanding of CLV estimation.
2. Literature Review
2.1 Traditional and Probabilistic Customer
Lifetime Value Models
The contemporary study of customer lifetime value
originated with foundational conceptual work by
Shaw and Stone (1988) establishing CLV as a metric
for evaluating long-term customer profitability in
database marketing contexts. Early implementations
employed deterministic calculations of discounted
future cash flows, but these approaches proved
inadequate for non-contractual settings wherein the
precise timing of customer defection remains
unobserved.
The field advanced substantively with the
introduction of probabilistic frameworks designed for
non-contractual purchase environments. Schmittlein
et al. (1987) proposed the Pareto/NBD model, which
specifies that customer purchase behavior follows a
Poisson process with heterogeneous purchase rates
distributed via gamma distribution, while customer
attrition (silent churn) follows an exponential
distribution parameterized through a Pareto
distribution across the customer base.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4)66

This model elegantly segregates two latent
customer processes—the purchasing process
(during the active customer lifetime) and the
attrition process (the unobserved defection
moment)—enabling prediction of purchase
frequency and defection probability from transaction
histories alone.
Fader et al. (2005) advanced the field by proposing
the BG/NBD model, substituting the Pareto attrition
process with a Beta-Geometric process to achieve
computational tractability while preserving
predictive accuracy. When combined with the
Gamma-Gamma monetary model for purchase-
value heterogeneity, these probabilistic frameworks
have attained wide adoption in industry applications
spanning e-commerce, retail, and subscription-
based business models. Recent extensions
incorporate time-invariant customer-level covariates
(Fader & Hardie, 2007) and allow hierarchical
structure to recover cohort-level parameter
heterogeneity (Gupta et al., 2006).
More recent work has extended these models to
incorporate time-varying covariates, nonstationary
purchase behavior, and scalable implementations
suitable for large customer databases, reflecting the
increasing integration of CLV modeling with modern
data environments.
Critically, all extant CLV models embody the
assumption that marketing intervention does not
influence the latent customer purchase and attrition
processes; instead, marketing is either omitted from
model specifications entirely or incorporated as an
exogenous covariate. This assumption is violated
when firms make marketing assignment decisions
endogenously based upon customer characteristics
correlated with purchase propensity. The
consequences are substantial: omitted marketing
endogeneity induces positive selection bias in
estimates of customer heterogeneity parameters,
specifically confounding unobserved autonomous
purchase propensity with marketing-driven
increments in purchase probability.
2.2 Bayesian Hierarchical Methods and
Heterogeneity
Hierarchical Bayesian approaches have
fundamentally transformed CLV modeling by
enabling flexible recovery of individual-level
customer parameters while leveraging population-
level information through appropriate prior
distributions.
Pioneering applications (Erdem & Keane, 1996)
demonstrated that hierarchical Bayes estimation
substantially improves prediction, particularly for
customers with sparse transaction histories, by
inducing shrinkage of individual-level estimates
toward population means.
The hierarchical Bayesian framework exhibits
particular utility in accommodating observed
covariates that vary across customers. By
permitting population-level hyperparameters to
depend upon observable customer characteristics,
the framework enables parameter heterogeneity to
correlate systematically with customer attributes
(e.g., acquisition channel, geographic location,
demographic segment). This structure proves
natural for CLV modeling wherein customer
purchase propensity manifestly varies with
observable characteristics.
Nevertheless, even sophisticated hierarchical
Bayesian CLV models maintain silence regarding the
causal impact of marketing interventions. They
continue to treat marketing assignment as
exogenous, thereby failing to address the
fundamental problem that firm targeting decisions
induce correlation between marketing exposure and
unobserved customer characteristics that
simultaneously predict purchase behavior. This
limitation reflects a gap between the models' formal
specification (as purely customer demand-side
processes) and actual firm practice (wherein
marketing assignment reflects managerial
expectations about customer responsiveness).
2.3 Endogeneity in Marketing and Causal
Inference
The marketing econometrics literature has
extensively developed methodology for addressing
endogeneity in specific domains—price setting,
promotional elasticity, advertising response—yet has
not systematically applied these techniques to the
CLV setting. Chintagunta et al. (2006) provide a
comprehensive taxonomy of endogeneity sources
applicable to marketing: omitted variables
(unobserved factors affecting both treatment and
outcome), simultaneity (bidirectional causality
between treatment and outcome), measurement
error, and selection bias (non-random assignment to
treatment). Selection bias—wherein treatment
receipt is correlated with unobserved factors
predicting outcomes—constitutes the primary threat
in CLV estimation contexts.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4) 67

Econometric solutions to endogeneity have achieved
substantial sophistication. Instrumental variable
estimation (Grace, 2021) leverages exogenous
variation in treatment to identify causal effects;
propensity score matching (Rosenbaum & Rubin,
1983) balances treatment and control groups on
observed covariates to mitigate confounding;
regression discontinuity designs (Imbens &
Lemieux, 2008) exploit threshold rules generating
quasi-random assignment; and structural
econometric models (Berry, 1994; Dube et al.,
2005) jointly specify demand and strategic decision
processes to avoid endogeneity. However, these
methodologies predominantly target point-in-time
treatment effects—the immediate impact of an
intervention on an outcome measured at a specific
time horizon.
More recently, advances in causal machine learning
and uplift modeling have emphasized the estimation
of heterogeneous treatment effects at the individual
level, focusing on identifying customers who are
most responsive to marketing interventions rather
than those with the highest predicted outcomes.
However, such approaches are typically applied to
short-term outcomes and are not integrated with
lifetime value estimation frameworks, leaving a gap
between causal targeting methods and CLV-based
decision-making.
CLV estimation presents distinct identification
challenges relative to standard treatment effect
estimation because it requires modeling cumulative
customer behavior over extended periods. Customer
responses to marketing interventions manifest not
as instantaneous outcome realizations but as
sequences of purchases over remaining customer
lifetimes. This dynamic aspect necessitates
integration of causal inference methodology with
temporal models capable of capturing how
marketing impact accumulates throughout the
customer relationship. Recent work by Hitsch et al.
(2024) on heterogeneous treatment effects and
optimal targeting policies provides methodological
foundation for this integration, establishing that
indirect and direct CATE (conditional average
treatment effect) estimation methods yield
substantively different targeting recommendations,
suggesting sensitivity to model specification in
endogenous settings.
The present research bridges this gap by extending
causal inference methodology to the CLV domain.
We integrate structural econometric approaches—
specifically, joint modeling of customer purchase
behavior and firm marketing strategy—with
hierarchical Bayesian estimation to recover more
reliable estimates of causal marketing effects on
long-term customer value. To our knowledge,
existing literature does not jointly model customer
purchase behavior and firm marketing assignment
decision-making within a unified framework
designed to estimate causal effects on customer
lifetime value.
3. Conceptual Framework
Formal identification of causal marketing effects
requires careful modeling of two distinct behavioral
processes: (i) customer purchase behavior as a
function of intrinsic propensity and marketing
exposure, and (ii) firm targeting behavior as a
function of observed customer characteristics and
estimated propensity. We next articulate the
economic logic underlying each process and the
identification challenge arising from their
interaction.
3.1 Customer Decision Process
We conceptualize customer purchase behavior as
determined by two latent factors: (i) an
autonomous purchase rate λ ᵢ  reflecting the
customer's intrinsic propensity to engage with the
firm (driven by category need, brand affinity, and
competitive alternatives), and (ii) a marketing
elasticity coefficient m ᵢ  reflecting the customer's
estimated responsiveness to firm-directed
marketing stimuli. The purchase probability in
period t for customer i, conditional upon remaining
active (i.e., not yet churned), depends upon both
factors in additive form within a linear probability
framework: autonomous propensity provides a
baseline purchase inclination, while marketing
exposure incrementally increases purchase
probability by an amount proportional to the
customer's elasticity.
Both λ ᵢ  and m ᵢ  remain unobserved by the analyst;
their values must be inferred from observed
purchase histories using Bayesian procedures.
Unobserved heterogeneity in these parameters
across the customer base reflecting the manifest
fact that customers differ in intrinsic purchase
propensity and response to marketing constitutes
an essential feature of the model. Additionally,
customer attrition (the silent defection characteristic
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4)68

of non-contractual settings) depends upon
customer-specific factors orthogonal to firm
marketing activity, reflecting that customers exit
relationships through means beyond the firm's
control (switching to competitors, category exit, life
circumstances).
3.2 Firm's Marketing Assignment Process
The firm observes certain customer characteristics,
historical purchase frequency and recency,
demographic attributes, channel engagement
patterns and employs this information to make
targeting decisions. Marketing expenditure on each
customer (the "targeting intensity") reflects the
firm's beliefs about the customer's profitability and
responsiveness. Importantly, the firm's targeting
decisions are not irrational; they reflect the firm's
optimization problem: allocate limited marketing
budgets toward customers perceived as most likely
to generate profitable responses.
The firm's targeting intensity Z ᵢ  depends on both
observable customer characteristics (e.g., recency,
frequency from RFM metrics) and the firm's
estimated or observed signals of the customer's
latent purchase propensity. Denote the firm's
targeting function as depending upon observable
attributes and a profitability index combining the
firm's estimate of autonomous purchase propensity
and marketing elasticity. This functional form
captures that firms target more heavily toward
customers they believe will respond profitably,
whether through intrinsically high purchase rates or
high estimated responsiveness to marketing.
This strategic targeting creates the fundamental
endogeneity problem. Since targeting intensity Z ᵢ
depends upon factors correlated with the
unobserved latent characteristics (λ ᵢ , m ᵢ ) that
appear in the customer purchase equation,
marketing exposure becomes correlated with the
unobserved components of the outcome equation.
Consequently, standard regression approaches that
ignore the targeting process will estimate biased
treatment effects, with the direction and magnitude
of bias determined by the correlation structure
between targeting decisions and unobserved
propensity factors.
3.3 The Endogeneity Mechanism and Resulting
Bias
The observed correlation between marketing
exposure and purchase outcomes conflates two
distinct causal flows. First, there is the direct causal
impact of marketing on customer purchases (the
"treatment effect" of interest). Second, there is
selection bias: high-propensity customers are
preferentially targeted, so observed purchase
differences reflect both causal marketing effects and
the concentration of marketing on customers
naturally disposed toward purchase.
Consider a concrete illustration. A firm observes
that customers in the top quintile of past purchase
frequency receive 50% of the email budget and
achieve 2.5× higher purchase rates than customers
in the bottom quintile who receive 5% of the email
budget. A naive analyst might estimate that email
marketing increases purchase probability by 250%.
However, if the firm's targeting criteria (past
purchase frequency) strongly predict autonomous
purchase propensity λ ᵢ —customers with high past
purchase frequency are intrinsically high-propensity
customers—then much of the 2.5× difference
reflects selection, not causality. The firm may be
spending email budget on customers who would
purchase anyway, reducing the true causal elasticity
of email.
Correcting this bias requires joint modeling. By
explicitly specifying how the firm's targeting
decisions depend upon customer characteristics and
propensity factors, and by leveraging the structure
of customer purchase histories, we can construct
predictions of what targeting would have occurred
under alternative firm decision-making rules. This
counterfactual reasoning enables statistical
adjustment for selection bias and recovery of causal
effects. The key identifying assumption is that
customer purchase history (frequency, recency,
timing patterns) predicts latent propensity λ ᵢ  and
elasticity m ᵢ , but conditional on observable targeting
rules (e.g., RFM-based segmentation), residual
variation in purchase timing does not directly
influence future marketing assignment beyond what
is captured by the firm's implemented targeting
criteria.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4) 69

Figure 1: Conceptual framework showing the
endogenous relationship between customer
behavior and firm marketing decisions.
4. Model Development
We specify a fully Bayesian hierarchical model in
two modules: (i) the demand module formalizing
customer purchase behavior as a function of latent
heterogeneity and marketing exposure, and (ii) the
assignment module formalizing firm marketing
targeting behavior as a function of observable
characteristics and propensity signals. Formal
specification enables Bayesian inference via Markov
Chain Monte Carlo (MCMC) estimation, yielding
posterior distributions over parameters and
posterior predictive distributions for counterfactual
customer lifetime value under alternative targeting
regimes.
4.1 Demand Module: Customer Purchase
Process
Let y ᵢₜ  ∈  {0, 1} denote the binary indicator that
customer i made a purchase in period t. Conditional
upon customer i remaining active (not yet churned),
the purchase probability is specified as:
where Φ(·) denotes the standard normal cumulative
distribution function, λ ᵢ  represents the customer's
autonomous purchase propensity, m ᵢ  represents the
customer's marketing elasticity (interpretable as the
causal effect under model assumptions), and Z ᵢₜ
represents the contemporaneous marketing
exposure intensity for customer i in period t,
measured on a standardized scale. The specification
admits a probit functional form with normally
distributed latent utility; alternative specifications
(logit, linear probability) are feasible.
Customer heterogeneity in propensity and elasticity
is accommodated through hierarchical prior
distributions, permitting parameters to vary across
customers while enabling information pooling.
Specifically:
Weakly informative priors are specified on the
hyperparameters to allow the data to drive
inference while preventing overfitting.
The hyperparameters μλ, σλ, μm, σm characterize
the population-level distribution of customer
preferences and treatment effects. By estimating
these hyperparameters from data rather than
imposing them a priori, the model learns the cross-
customer variation in purchase propensity and
marketing responsiveness. This hierarchical
structure ensures that customer-level parameter
estimates—particularly those based upon limited
transaction histories—are shrunk toward the
population mean, improving prediction by exploiting
correlations in customer behavior.
The critical innovation relative to extant CLV models
is the explicit inclusion of the marketing exposure
term m ᵢ  · Z ᵢₜ  in the purchase equation. Standard
probabilistic CLV models (Pareto/NBD, BG/NBD)
omit marketing entirely, leaving marketing effects to
be absorbed into unobserved heterogeneity. By
explicitly modelling marketing, we enable direct
estimation of the treatment effect m ᵢ  and allow
assessment and correction of endogeneity bias
through the targeting module.
The likelihood is constructed from conditional
purchase probabilities across customers and time
periods.
Customer attrition is modelled through a separate
binary indicator Activeit ∈ {0,1}, which transitions
from 1 to 0 upon silent defection. The attrition
process depends upon customer-specific factors
(autonomous churn propensity) that are
independent of marketing activity, reflecting that
customers defect through mechanisms—competitive
switching, category exit—outside firm control.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4)70

The joint specification of purchase and attrition
processes is analogous to the Pareto/NBD
framework but with the added marketing covariate
in the purchase equation.
4.2 Assignment Module: Marketing Targeting
Process
The firm's targeting intensity for customer i is
modeled as a latent index that depends upon
observable customer characteristics and unobserved
propensity factors:
The assignment module is not estimated as a
standalone likelihood; rather, it is incorporated
structurally to characterize how marketing is
assigned given observed customer characteristics
and inferred purchase propensities, allowing the
model to account for selection effects through
shared dependence on latent parameters. The key
insight is that targeting depends upon propensity
factors: if λ̂ ᵢ  is correlated with the firm's estimate
of unobserved λ ᵢ , and if m̂ ᵢ  is correlated with the
true elasticity m ᵢ , then marketing exposure Z ᵢ
becomes correlated with the unobserved error term
in the demand equation, inducing endogeneity bias.
The identifying assumption is that, conditional upon
observable targeting criteria that appear explicitly in
the firm's targeting rule, purchase history and its
components (frequency, recency) serve as valid
predictors of latent propensity λ ᵢ , and elasticity m ᵢ ,
while residual variation in purchase timing provides
additional information that is not fully exploited by
the firm's targeting mechanism. In particular,
conditional on observable targeting rules, such
variation does not systematically influence future
marketing assignment beyond what is captured by
the firm's implemented criteria. This assumption is
most plausible in settings where firms employ
transparent or rule-based targeting strategies (e.g.,
RFM segmentation or cohort-based rules), rather
than fully optimized or high-dimensional propensity
models that incorporate all available behavioral
signals.
4.3 Identification and Bayesian Inference
Identification of causal marketing effects is
facilitated by the structure of the assignment
module combined with the temporal sequence of
firmdecisions and customer outcomes. Identification
is achieved through the joint specification of the
demand and assignment processes within a
hierarchical Bayesian framework, rather than relying
on a strict instrumental variable.
The firm makes targeting decisions Zi based upon
information known at the time of targeting
(observable characteristics and signals of propensity
estimated from historical data). Customer purchases
occur subsequently. Conditional upon the observable
criteria Xi that explicitly appear in the firm's
targeting rule—and are therefore known to be used
by the firm—the randomness in purchase timing
contains information about latent propensity and
elasticity that is not fully captured by the firm's
targeting mechanism, helping to separate selection
effects from marketing impact.
Bayesian inference proceeds via Markov Chain
Monte Carlo (MCMC) estimation. The hierarchical
structure yields conjugate conditional posterior
distributions for some parameters, enabling efficient
Gibbs sampling within blocks (e.g., individual and
conditional upon hyperparameters). Non-conjugate
blocks (e.g., hyperparameters μλ, σλ, μm, σm) are
estimated via Metropolis-Hastings sampling with
adaptive proposals. Model specification includes
weakly informative priors on hyperparameters—
normal priors with large variances on means, half-
normal priors on standard deviations—to avoid
overfitting, allowing data to dominate inference.
Posterior inference enables two key outputs. First,
posterior means and credible intervals for individual
customer parameters (λ ᵢ , m ᵢ )quantify heterogeneous
propensities and treatment effects, enabling
customer-level segmentation based on estimated
marketing responsiveness. Second, posterior
predictive distributions enable counterfactual CLV
calculations: the analyst can sample from the
posterior distribution, set marketing exposure to
alternative levels (e.g., zero for all customers, or
optimized targeting rules), and draw samples of
resulting future purchases. Averaging these
counterfactual purchase samples yields posterior
predictive CLV distributions under alternative
marketing scenarios, supporting robust decision-
making under uncertainty.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4) 71

5. Implications
5.1 Theoretical and Methodological
Contributions
This research contributes to the intersection of two
previously distinct literatures. The CLV literature has
produced increasingly sophisticated probabilistic
models but has been deliberately abstracted from
marketing strategy and the endogenous nature of
firm interventions. The causal inference and
econometric literatures have developed powerful
methodologies for identifying treatment effects but
have focused on point-in-time outcomes rather than
on lifetime value, where outcomes accumulate over
extended horizons and depend upon both customer
characteristics and strategic firm decisions. This
work integrates these perspectives by extending
causal inference theory to CLV estimation,
demonstrating how methods from structural
econometrics can mitigate endogeneity bias in
foundational customer analytics models.
Methodologically, the hierarchical Bayesian
specification enables estimation of heterogeneous
treatment effects—the estimated impact of
marketing varies across customers as a function of
their characteristics. This capability directly
addresses a limitation of traditional CLV models,
which estimate only population-level parameters;
firms require segment-specific or even individual-
level estimates of marketing elasticity to implement
effective targeted marketing. The hierarchical
structure facilitates information borrowing across
customers, stabilizing heterogeneous effect
estimates even for small customer segments.
5.2 Managerial Implications
Correcting for endogenous marketing assignment
yields three categories of managerial implications.
First, CLV estimates are recalibrated. Customers
appearing high-value under traditional CLV models
may be revealed as moderate-value once we
account for the fact that they received
disproportionate marketing because of high
autonomous propensity. Conversely, customers with
lower observed purchase rates but high estimated
elasticity—customers for whom marketing is
genuinely effective—may be revealed as higher-
value. This recalibration can be substantial; our
simulations demonstrate customer-level CLV
revisions ranging from −30% to +40%.
Second, the corrected model enables superior
budget allocation. Traditional CLV frameworks
suggest concentrating marketing on customers with
high autonomous purchase propensity (who will
likely buy anyway). The corrected framework
instead directs marketing toward customers with
high elasticity those for whom marketing is most
effective in a causal interpretation sense under the
model even if their autonomous propensity is
modest. This reallocation of marketing budgets from
high-propensity/low-elasticity segments to low-
propensity/high-elasticity segments can
substantially increase firm profitability.
Third, the framework enables valid scenario
analysis. Marketing managers frequently
contemplate counterfactual allocations: "How would
CLV change if we reduced email frequency by
20%?" or "What additional CLV would we realize by
shifting budget from digital to direct mail?" Valid
answers require well-identified estimates of
marketing effects. Our framework provides posterior
predictive distributions of CLV under alternative
marketing regimes, enabling probabilistic scenario
analysis. Decision-makers can quantify not only
point estimates of CLV under alternative strategies
but also credible intervals reflecting estimation
uncertainty.
6. Simulation Evidence
To validate the magnitude of endogeneity bias and
the efficacy of our proposed correction, we conduct
Monte Carlo simulation studies calibrated to
approximate realistic e-commerce retail
environments. We generate synthetic customer
purchase and marketing exposure data from a
known data-generating process, then estimate both
standard CLV models (ignoring marketing) and our
proposed structural Bayesian model (jointly
modelling purchase and targeting), comparing
recovered parameter estimates to ground truth.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4)72

Figure 2: Estimated marketing effects across
targeting regimes, showing bias in traditional CLV
models and correction under the proposed
framework.
Key Results
Traditional CLV models (Pareto/NBD without
marketing) estimate elasticity at 0.96, representing
a 60% overestimate (true effect = 0.60). The
structural Bayesian model recovers elasticity of 0.62
(95% credible interval: 0.50–0.75), closely
recovering the underlying simulated effect.
The endogeneity bias scales systematically with
targeting intensity: under top 20% targeting, naive
elasticity reaches 1.24 (107% overestimate); under
randomized 50% targeting, bias falls to 0.08 (13%
overestimate). This pattern confirms the theoretical
prediction that bias increases with targeting
sophistication.
CLV Implications
For CLV implications: a customer with low
observable purchase frequency but high estimated
elasticity (mi = 0.80) appears to have CLV = $140
under traditional estimates; under the corrected
model, CLV = $210, a 50% increase reflecting the
customer's higher responsiveness to marketing.
Conversely, a customer with high frequency but low
elasticity appears to have CLV = $680 under
traditional estimates; under the corrected model,
CLV = $480, a 29% decrease reflecting that much
of their purchase activity reflects autonomous
propensity rather than marketing effectiveness.
7. Conclusion
This paper identifies and addresses a systematic
bias affecting customer lifetime value estimation:
the overestimation of marketing effectiveness
arising from endogenous assignment of marketing
based upon customer characteristics correlated with
purchase behavior.
We develop a structural Bayesian framework jointly
modeling customer purchase decisions and firm
marketing allocation decisions, enabling improved
identification and estimation of marketing effects on
long-term customer value.
The research makes contributions across three
dimensions. Methodologically, it extends causal
inference techniques from point-in-time treatment
effects to the lifetime value setting, where outcomes
accumulate over time. Theoretically, it bridges
previously separate literatures (CLV modeling and
marketing econometrics) and demonstrates how
insights from causal inference improve foundational
customer analytics models. Practically, it enables
firms to more accurately assess which customers
are valuable, direct marketing expenditures toward
customers exhibiting higher estimated
responsiveness, and conduct scenario analysis of
alternative marketing strategies.
Promising directions for future research include: (1)
relaxing the linear utility specification to
accommodate nonlinear marketing response and
saturation effects characteristic of high-frequency
marketing; (2) modeling the firm's optimization
problem to derive endogenous optimal targeting
policies rather than treating targeting as
exogenously specified; (3) extending the framework
to multiproduct settings with competitive brand
choice; (4) incorporating dynamic customer
information states wherein the firm's propensity
estimates improve over time; and (5) empirical
validation using customer databases with measured
marketing exposure and complete transaction
records.
The proposed framework relies on assumptions
regarding the firm's targeting process and model
specification; deviations from these assumptions
may affect the accuracy of estimated effects.
The central insight that marketing endogeneity
creates substantial bias in CLV estimates and that
joint modeling of customer behavior and firm
strategy can mitigate this bias—will become
increasingly important as firms develop more
sophisticated ML-driven targeting algorithms,
making the endogeneity problem more acute rather
than less.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4) 73

References
[1] Ali, N., & Shabn, O. S. (2024). Customer lifetime
value (CLV) insights for strategic marketing success
and its impact on organizational financial
performance. Cogent Business & Management,
11(1), 2361321.
https://doi.org/10.1080/23311975.2024.2361321
[2] Ascarza, E. (2018). Retention futility: Targeting
high-risk customers might be ineffective. Journal of
marketing Research, 55(1), 80-98.
https://doi.org/10.1509/jmr.16.0163
[3] Berry, S. T. (1994). Estimating discrete-choice
models of product differentiation. RAND Journal of
Economics, 25(2), 242-262.
https://doi.org/10.2307/2555829
[4] Chintagunta, P. K., Erdem, T., Rossi, P. E., &
Wedel, M. (2006). Structural modeling in marketing:
Review and research opportunities. Journal of
Marketing Research, 43(3), 347-356.
https://doi.org/10.1287/mksc.1050.0161
[5] Dubé, J. P., Hitsch, G. J., & Manchanda, P.
(2005). An empirical model of advertising dynamics.
Quantitative Marketing and Economics, 3(2), 107-
144. https://doi.org/10.1007/s11129-005-0334-2
[6] Elwert, F., & Winship, C. (2014). Endogenous
selection bias: The problem of conditioning on a
collider variable. Annual Review of Sociology, 40,
31-53. https://doi.org/10.1146/annurev-soc-
071913-043455
[7] Erdem, T., & Keane, M. P. (1996). Decision-
making under uncertainty: Capturing dynamic brand
choice processes in turbulent consumer goods
markets. Marketing Science, 15(1), 1-20.
https://doi.org/10.1287/mksc.15.1.1
[8] Fader, P. S., & Hardie, B. G. (2007).
Incorporating time-invariant covariates into the
Pareto/NBD and BG/NBD models. Working Paper,
University of Pennsylvania and London Business
School.
[9] Fader, P. S., Hardie, B. G., & Lee, K. L. (2005).
Counting your customers the easy way: An
alternative to the Pareto/NBD model. Marketing
Science, 24(2), 275-284.
https://doi.org/10.1287/mksc.1040.0098
[10] Grace, J. B. (2021). Instrumental variable
methods in structural equation models. Methods in
Ecology and Evolution, 12(7), 1148-1157.
https://doi.org/10.1111/2041-210X.13600
[11] Gupta, S., Hanssens, D., Hardie, B., Kahn, W.,
Kumar, V., Lin, N., Ravishanker, N., & Sriram, S.
(2006). Modeling customer lifetime value. Journal of
Service Research, 9(2), 139-155.
https://doi.org/10.1177/1094670506293810
[12] Hitsch, G. J., Misra, S., & Zhang, W. W. (2024).
Heterogeneous treatment effects and optimal
targeting policy evaluation. Quantitative Marketing
and Economics, 22, 115-168.
https://doi.org/10.1007/s11129-023-09278-5
[13] Imbens, G. W., & Lemieux, T. (2008).
Regression discontinuity design: A practical guide.
Journal of Econometrics, 142(2), 615-635.
https://doi.org/10.1016/j.jeconom.2007.05.001
[14] Malodia, S., Dhir, A., Hasni, M. J. S., &
Srivastava, S. (2023). Field experiments in
marketing research: a systematic methodological
review. European Journal of Marketing, 57(7),
1939-1965. https://doi.org/10.1108/EJM-03-2022-
0240
[15] Rosenbaum, P. R., & Rubin, D. B. (1983). The
central role of the propensity score in observational
studies for causal effects. Biometrika, 70(1), 41-55.
https://doi.org/10.1093/biomet/70.1.41
[16] Schmittlein, D. C., Morrison, D. G., & Colombo,
R. C. (1987). Counting your customers: Who are
they and what will they do next?. Management
Science, 33(1), 1-24.
https://doi.org/10.1287/mnsc.33.1.1
[17] Shahabikargar, M., Beheshti, A., Zhang, X.,
Foo, J., & Jolfaei, A. (2026). A comprehensive
survey on customer churn analysis studies. Journal
of Information and Telecommunication, 10(1), 24-
70.
https://doi.org/10.1080/24751839.2025.2528440
[18] Shaw, R., & Stone, M. (1988). Database
marketing: Strategy and implementation. Gower
Publishing Company.
[19] van Oostenbruggen, V., & Cavicchia, C. (2022).
A review of dynamic customer segmentation
methods in e-commerce business contexts.
[20] Wooldridge, J. M. (2010). Econometric analysis
of cross section and panel data. (2nd ed.). MIT
Press.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4)74

Disclaimer / Publisher's Note: The statements, opinions
and data contained in all publications are solely those of
the individual author(s) and contributor(s) and not of
Journals and/or the editor(s). Journals and/or the editor(s)
disclaim responsibility for any injury to people or property
resulting from any ideas, methods, instructions or products
referred to in the content.
Ghanvat S, et al. Modelling Customer Lifetime Value
Int J Engg Mgmt Res 2026;16(4) 75
