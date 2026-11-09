---
title: 'A dual-LSTM model for CLV distributions: Diverging paths and bimodalities'
url: https://doi.org/10.1007/s11747-026-01193-x
category: cx-retail
subcategory: framework
date: 2026-09
venue: Journal of the Academy of Marketing Science
authors:
- Mainak Sarkar
- Arnaud De Bruyn
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s11747-026-01193-x.pdf
pages: 20
chars: 98528
fetched_at: '2026-11-08T18:40:16+00:00'
kb_version: 1
---

# A dual-LSTM model for CLV distributions: Diverging paths and bimodalities

ORIGINAL EMPIRICAL RESEARCH
Journal of the Academy of Marketing Science
https://doi.org/10.1007/s11747-026-01193-x
Dennis Herhausen served as Area Editor for this article.
 Mainak Sarkar
mainaks@umich.edu
Arnaud De Bruyn
debruyn@essec.edu
1 College of Business, University of Michigan-Dearborn,
Dearborn, MI, USA
2 ESSEC Business School, Avenue Bernard Hirsch,
Cergy 95000, France
Abstract
Virtually all customer lifetime value (CLV) models reduce the future of a customer to a single number, its expected value,
implicitly assuming managers are indifferent to how that value materializes. Yet in a survey of management consultants
from a leading global strategy firm, 79% would distinguish between two customers with identical expected CLV but dif -
ferent distributional profiles. This paper argues for a distributional view of CLV and develops a dual-LSTM framework:
two interacting long short-term memory networks that jointly predict customer behavior and firm marketing strategy.
Because customer responses and firm actions co-evolve dynamically through Monte Carlo simulation, the model generates
rich CLV distributions that capture self-fulfilling prophecies, diverging loyalty paths, and bimodal outcomes that tradi -
tional approaches cannot structurally anticipate. Calibrated on nine years of individual-level data from 21,939 donors, the
dual-LSTM consistently outperforms six benchmarks (including the Pareto/NBD, hierarchical Bayesian extensions, and
state-of-the-art deep learning alternatives) on 19 of 24 evaluation metrics. Ranking customers by the right tail of their
CLV distribution, rather than by expected CLV , improves targeting lift by up to 8.3%. Most critically, bimodal customers
identified by the dual-LSTM—those at a fork in their customer journey—are significantly more responsive to marketing
solicitations than observably identical unimodal customers (ROI of an additional solicitation at + 77% vs. -50%), a finding
no other benchmark model replicates. These results demonstrate that CLV distributions are both estimable and actionable,
enabling firms to allocate resources where marketing interventions yield the greatest marginal impact.
Keywords Customer lifetime value · Customer relationship management · Deep learning · Artificial intelligence
Received: 13 March 2025 / Accepted: 29 July 2026
© The Author(s) 2026
A dual-LSTM model for CLV distributions: Diverging paths and
bimodalities
Mainak Sarkar1  · Arnaud De Bruyn2
doing so, they quietly assume that managers are risk-neutral,
indifferent between two customers with identical CLV but
very different risk profiles, and that they care only about the
average of the distribution, not the specific paths that lead
there. Neither assumption survives contact with practice.
In a survey of 38 management consultants from one of the
“Big 5” global consulting firms, only 21% would treat two
such customers alike; the remaining 79% would differenti -
ate their strategies, citing considerations ranging from firm
valuation and sales-force motivation to “land and expand”
opportunities and production planning. Managers, in other
words, care a great deal about how customer lifetime value
will materialize, not merely how much, and yet the models
they rely on are silent on precisely that dimension.
We argue that real CLV distributions are shaped by the
interplay of customer behavior and firm strategy: a decision
to target an active customer or neglect an inactive one can
amplify upside potential or accelerate downside risk, setting
off self-fulfilling prophecies that spread out, and sometimes
Introduction
Customer lifetime value (CLV) is among the most widely
used metrics in customer relationship management, and a rich
body of models has made CLV prediction an indispensable
tool for marketing managers, financial analysts, and CRM
strategists alike. Yet virtually all of these models reduce a
customer’s future to a single number: its expected value. In

1 3
Journal of the Academy of Marketing Science
split, the distribution of future outcomes. Capturing these
dynamics calls for a model that does three things at once:
account for latent attrition, endogenously incorporate the
firm’s adaptive strategy, and remain flexible enough to allow
complex distributional shapes to emerge from the data. No
existing model does all three.
We further argue for a shift in how CLV is conceived
and used: not as a single point estimate, but as a distribu -
tion of possible outcomes, each with its own upside poten -
tial (the right tail of the distribution), downside risk (the left
tail), and, in the cases we find most revealing, bimodality, a
distribution with two distinct peaks that signals a customer
poised at a fork in their journey. To recover such distribu -
tions, we develop a dual-LSTM model: two interacting
long short-term memory neural networks, one predicting
the firm’s marketing strategy and the other the customer’s
behavior. In each period, the firm model predicts the like -
lihood of a solicitation; the customer model observes that
prediction and then predicts a donation in the same period.
Treating each prediction as a Bernoulli draw and repeating
the Monte Carlo simulations yields rich CLV distributions
in which customer behavior and firm action co-evolve over
time.
This design lets us pursue three questions. First, does
jointly modeling the firm’s strategy and the customer’s
behavior improve CLV predictions relative to models that
ignore or exogenize the firm’s actions? Second, does the
dual-LSTM recover the full CLV distribution, not merely
its expectation, more accurately than existing alternatives?
Third, are the distributional patterns it surfaces, bimodal
ones in particular, managerially actionable?
We answer these questions using a large fundraising
database spanning nine years of individual-level donation
and solicitation histories for 21,939 donors. We benchmark
the dual-LSTM against six competing models, including the
Pareto/NBD, Abe’s hierarchical Bayesian extension, a SUR
bivariate probit, an ElasticNet regression, a single-LSTM,
and a single-transformer, across seven families of evalua -
tion criteria over a thirty-six-month holdout period. The
dual-LSTM model outperforms all six benchmarks on 19 of
24 success metrics. To gauge whether the model’s distribu-
tional predictions actually matter, we then use a Coarsened
Exact Matching design that pairs bimodal and unimodal
customers on all observable characteristics at the end of the
calibration period and tests their differential responsiveness
(and profitability) to subsequent solicitations.
This paper makes three contributions. First, we show that
incorporating the firm’s adaptive marketing strategy endog-
enously improves predictive accuracy across a wide range
of metrics, challenging the common practice of treating firm
policy as exogenous and giving researchers and practitioners
alike reason to model how the firm itself will act, not just
how customers will respond. Second, we demonstrate that
the dual-LSTM recovers CLV distributions with markedly
greater precision than existing alternatives, and that ranking
customers by the right tail of their distribution rather than by
expected value improves targeting lift, advancing the field
from a point-estimate paradigm toward a distributional one
in which the shape of the distribution is both estimable and
consequential. Third, and most important for practice, we
provide direct evidence that these distributional patterns are
actionable: bimodal customers respond significantly more
strongly to the firm’s solicitations than observably identical
unimodal customers do, a result that no benchmark model
reproduces. The dual-LSTM thus pinpoints the customers
for whom marketing yields the greatest marginal return,
allowing firms to direct resources where they matter most.
The remainder of this paper is organized as follows. In
§ 2, we discuss the importance and practical utility of mov-
ing beyond CLV averages to estimate CLV distributions. In
§ 3, we review the relevant CLV literature and its current
strengths and limitations. In § 4, we develop the proposed
CLV specification based on two interacting LSTM models.
In § 5, we calibrate and validate the model and compare it
to six benchmarks. We conclude in § 6 with suggestions for
future research.
CLV distributions
The introduction argued that managers are not indifferent to
how CLV materializes. In this section, we provide empirical
evidence for that claim and illustrate why CLV distributions
are hard to predict without modeling the firm’s strategy.
Survey of management consultants
We surveyed 38 consultants from one of the “Big 5” global
consulting firms, participating in a highly selective, custom
executive education program. Given their roles and mis -
sions, they have experience across a wide range of indus -
tries and advise stakeholders at various levels of the client
organization. We presented them with two customers with
identical expected CLV but contrasting risk profiles (see
Fig. 1) and asked them which customer should receive more
relationship-building effort.
Only 8 out of 38 consultants (21%) recommended treat -
ing both customers similarly. 50% favored the high-poten -
tial customer, while 29% favored the low-risk one. Their
justifications (reported in the Web Appendix) ranged from
risk management and production stability to sales force
motivation, “land and expand” strategies, and even firm
valuation —with consultants on opposite sides of the debate
both invoking valuation concerns in their favor—.

1 3
Journal of the Academy of Marketing Science
For the purposes of this paper, we are agnostic about
whether managers should prefer customers with higher
upside potential or lower downside risk, as such a distinc -
tion depends on the decision-maker’s purpose and the firm’s
circumstances. What is clear is that most CLV models do
not allow such a distinction, even though it matters a great
deal to managers.
CLV distributions are shaped by customer–firm
interactions
Why are CLV distributions so hard to predict? A key reason
is that they emerge from the intertwined dynamics of cus -
tomer behaviors and firm strategy; dynamics that most CLV
models do not capture.
We illustrate this with a group of 222 donors from our
empirical database who, at the start of the observation
period, are relatively homogeneous: all acquired four years
prior, were active at least once in the last 12 months, and
had precisely three donations since acquisition. Over the
next five years, their CLV outcomes diverge dramatically
(cf. Figure 2, left panel). Many donors churn entirely (N = 0
donations), while others remain loyal and give every year
(N = 5). The resulting distribution is strongly bimodal—a
pattern that a Pareto/NBD model, for instance, completely
fails to anticipate (Fig. 2, right panel)—.
What drives this divergence? Fig. 3 traces the customer–
firm interactions year by year. In Year 1, all 222 donors
receive roughly the same level of solicitations (≈ 14) and
donate at similar rates (73%). But when some donors fail
to give in Year 1—a stochastic event for an otherwise
homogeneous group—the charity reacts by reducing its
solicitations in Year 2 (9.1 vs. 14.7 for Year 1 donors).
Fewer solicitations correlate with fewer donations, which
trigger even fewer solicitations, and so on. By Year 3,
the gap is stark: one group receives 16.4 solicitations and
donates 0.92 times per year, while the other receives only
5.5 solicitations and donates 0.22 times per year. This
more-than-fourfold difference in donor activity cannot be
easily attributed to donors’ characteristics at the beginning
of the period but is substantially shaped by the organiza -
tion’s strategic reaction to an initial, seemingly random
decision to give or not.
These self-reinforcing cycles, where firms nurture active
customers and neglect inactive ones, amplifying initial dif -
ferences into diverging loyalty paths, are not unique to fund-
raising. They arise wherever firm actions are endogenous to
customer behavior: in B2B sales (high-potential prospects
receive more calls), in retailing (loyalty-card holders receive
more promotions), in airlines (top-tier fliers receive more
benefits), and in direct marketing (responsive customers are
targeted more frequently). In each case, the firm’s strategic
decisions spread the CLV distribution and, in extreme cases,
can generate bimodal patterns in which middle-of-the-road
outcomes become unlikely.
Capturing these dynamics—and the CLV distributions
they produce—requires a model that meets two criteria
simultaneously: it should incorporate the firm’s adaptive
strategy as a driver of CLV outcomes, and its structure
should be flexible enough to let complex distributional pat -
terns emerge from the data. We review the extent to which
existing CLV models meet these criteria in the next section.
Fig. 2 Frequency plot of the num-
ber of donors who have made 0,
1, 2… donations over five years.
Left: ground truth observed in the
data, which is strongly bimodal.
Right: for illustration purposes
only, predictions made by a Pareto/
NBD model, which fails to capture
the complex pattern of CLV distri-
bution and predicts a unimodal
distribution and a mode at zero

Fig. 1 Two customers with identi-
cal expected CLV presented to
management consultants from
one of the “Big 5” global consult-
ing firms

1 3
Journal of the Academy of Marketing Science
Customer lifetime value literature
Customer lifetime value (CLV), defined as “the present
value of all future profits obtained from a customer over
[their] life of relationship with the firm” (Gupta et al., 2006),
has served as the canonical metric for forward-looking cus-
tomer management. Virtually every published CLV model
(see Web Appendix) reduces it to a single number per cus -
tomer: the posterior mean of a future cash flow. The omis -
sion of the surrounding distribution would be harmless if
that distribution were uninformative, that is, smooth, uni -
modal, and well summarized by its mean, which is precisely
what the existing literature produces. However, the reason
has less to do with what CLV materializes (see Fig. 2) than
with how it is modeled.
Most CLV models simulate a single stochastic process:
the customer. The firm is either absent or fixed. Run that
process forward many times, and the only sources of vari -
ability are sampling noise and, in latent-attrition models, the
moment of an unobserved death. Both produce smooth, uni-
modal densities centered on the mean. Nothing in the simu-
lation is set up to generate the structures managers actually
care about: diverging customer trajectories, self-reinforcing
loyalty cycles, and fragile customers at the “fork in the road”
where their trajectory could go either way. Such structures
arise only when a firm and a customer interact dynamically
over time, with each adjusting stochastically to the other.
The literature has been organized around the assumption
that the firm does not.
The first and oldest stream, the latent-attrition family that
begins with the Pareto/NBD framework of Schmittlein et
al. (1987), assumes away firm policy. Customers purchase
as a Poisson process until an unobserved death point, ignor-
ing the firm’s actions altogether. More than three decades
of refinements, such as the BG/NBD reformulation (Fader
et al., 2005a), the discrete-time BG/BB for charity and sub-
scription data (Fader et al., 2010), or the hierarchical Bayes
extension (Abe, 2009), have improved fit at the margins
without questioning that assumption. That literature does
not claim that the firm’s strategy is irrelevant; whatever
the firm did during calibration is silently absorbed into the
parameters and is assumed to continue. Its impact is inte -
grated and averaged in the model parameters.
A second stream uses firm marketing during estimation
but freezes it during predictions. Manchanda et al. ( 2004)
established the broader methodological case that marketing-
mix variables are rarely random and that conditioning on
them silently biases the response surface, a warning that
has since reshaped how CLV studies handle marketing dur-
ing calibration. Schweidel & Knox ( 2013) embed direct-
marketing solicitations into a latent-attrition likelihood and
show that ignoring marketing distorts both attrition and
donation predictions. Bachmann et al. (2021) integrate firm
policy as a time-varying contextual factor. The deep-learn -
ing CLV models of Valendin et al. (2022) and Lu & Kannan
(2026) enter past marketing data into the input stream. The
models do not, however, change what the model predicts
forward: in the holdout, the customer process runs alone,
Fig. 3 Number of donations made (and solicitations received) by the same 222 individuals reported in Fig. 2, based on their behaviors each year

1 3
Journal of the Academy of Marketing Science
and the firm reappears only as a covariate the analyst sup -
plies by hand, exogenously.
A third stream embraces firm marketing as a dynamic
input. The regression-based always-a-share family (Ven -
katesan & Kumar, 2004; Kumar et al., 2008; Rust et al.,
2011) treats CLV as a sum of period-by-period predicted
purchases driven in part by marketing contacts that the
analyst can vary. Esteban-Bravo et al. ( 2014) formalize
the choice of those contacts as a stochastic dynamic pro -
gramming problem and derive the optimal solution. In
each case, the projection generates a contact schedule for
the holdout, either as a rule the analyst specifies or as the
optimum that maximizes predicted CLV under the response
model. Four difficulties follow. First, none of these models
carries a latent-attrition component, so they cannot repro -
duce the steady deceleration in aggregate purchases that
any non-contractual cohort eventually exhibits (Fader &
Hardie, 2009), and they tend to overpredict transactions as
the horizon lengthens. Second, when these models are used
prescriptively, the projection commits one to a causal read-
ing of the customer response coefficients. The authors in
this stream are typically careful1 to flag this as a limitation:
isolating the causal effect of marketing from observational
data is notoriously hard, since the firm chose its historical
targeting based on customer characteristics correlated with
the response itself (Manchanda et al., 2004; Simester et al.,
2020). Third, the firm-policy rule is something the analyst
writes down, such as a heuristic or an optimum, rather than
something the data informs. Real-world firm strategies are
far more stochastic: a budget line is not approved; a man -
ager decides to expand a campaign’s reach to meet its quar-
terly sales objectives; organizational constraints interfere;
some budget remains that must be spent before the end of
the fiscal year. No deterministic rule can encode such com -
plex realities. Fourth, a deterministic firm policy generates a
smooth CLV distribution by construction, because the only
remaining variation is, again, customer-side noise.
What is missing is a CLV model in which the firm’s pol-
icy is itself a stochastic process, learned from the firm’s own
history, sampled forward jointly with the customer process,
and free to react to the customer’s evolving state period by
period. Such a model would let the firm and the customer
co-adapt over time, would absorb the frictions and idiosyn-
crasies inherent in any actual targeting policy, and would
let the resulting CLV distribution reflect the structure of the
interaction rather than the noise of a one-sided process. The
1  The Venkatesan and Kumar ( 2004) limitations section explicitly
notes endogeneity in marketing decisions; Rust et al. ( 2011) flag that
their simulation cannot identify causal effects without experimental
variation; Kumar et al. (2008) ran their reallocation as a quasi-experi-
ment partly to address this.
dual-LSTM we develop next is, to our knowledge, the first
to do so.
A dual-LSTM model of customer lifetime
value
Overview
The marketing literature has seen a rise in novel AI and
machine learning approaches to address problems that were
not easily addressable before (see De Bruyn et al., 2020; Ma
& Sun, 2020). Among them, deep-learning recurrent neural
networks (RNN) appear particularly suited for predicting
CLV . In Sarkar and De Bruyn (2021), the authors deploy a
long short-term memory (LSTM) model (a particular RNN;
see below) to predict customers’ likelihood of responding to
a one-shot marketing campaign. They do not rely on sum -
marized features such as recency or frequency but instead
feed the model with raw behavioral sequence data, e.g., past
purchases. Valendin et al. ( 2022) extend this framework
to multi-period predictions, whereas Lu & Kannan ( 2026)
demonstrate the advantages of attention mechanisms for
focusing on diverse outcomes. Building on this literature,
we summarize our model as follows:
First, not only do we build an LSTM model to predict
customers’ behaviors for the next period, but we also build
another independent model to predict the firm’s policy 2,
allowing each model to “feed” on the outputs of the other
over time and capture the intertwined nature of firm policy
and customer behaviors. At each period, the firm behavior
LSTM model takes the entire raw sequence of past obser -
vations (two vectors of solicitations and donations, plus
monthly dummy indicators) and predicts the likelihood of
a solicitation that month. Importantly, the firm model is not
prescriptive; it does not recommend what the firm should
do. Rather, it serves as a covariate generator for the cus -
tomer model, predicting what the firm is likely to do based
2  Deep-learning joint models do not explicitly model error correlations
as econometric joint models do. We develop two independent deep
learning models instead of a single multi-task model to prevent task-
conflict (negative transfer), which could degrade the performance of
both models. Beyond the risk of negative transfer, the sequential archi-
tecture is necessary to capture same-period marketing acceleration:
the customer model observes the firm model’s predicted solicitation
for month t before predicting the donation in month t. A multi-output
model would predict both outputs simultaneously, preventing the cus-
tomer model from conditioning on the firm’s same-period action and
missing the rapid effect of a solicitation on donation within the same
month. The alternative —predicting same-month donation alongside
next-month solicitation— would require the two outputs to draw on
different data sequences, which cannot be accommodated within a sin-
gle shared architecture. It is precisely this need to capture marketing
acceleration that necessitates the sequential, two-model design.

1 3
Journal of the Academy of Marketing Science
on its historical behavioral patterns. The customer behavior
model then predicts the likelihood that the customer will
make a donation in the same month, as depicted in Fig. 4.
Second, each model yields a probabilistic prediction of
the likelihood that a donation and a solicitation will occur
in period N + 1. We then treat that probability as a Bernoulli
draw to simulate a potential outcome for period N + 1. That
simulated outcome is then integrated into the panel data and
used to predict a likely outcome in period N + 2, and so on.
Third, we repeat these Monte Carlo simulations hundreds
of times for each customer over a sufficiently long period
(e.g., three or six years), not only to estimate a customer’s
expected CLV but also to generate a distribution of potential
CLV outcomes.
The machine learning approach we propose is more
complex and technically involved than traditional BTYD
models (more on that later). However, it offers four distinct
advantages over the existing alternatives proposed in the
CLV literature.
First, the dual-LSTM model reckons that marketing solic-
itations are useful covariates for predicting customer behav-
ior. By endogenously predicting firm actions and integrating
them into the modeling framework, the approach captures
the highly dynamic and intertwined nature of firm policies
and customer behaviors, thereby potentially improving CLV
predictions. For instance, it could account for the fact that
the firm solicits responsive customers more often, predict -
ing a higher purchase likelihood. Or it could capture that
barely solicited donors are less likely to donate, leading to
reduced marketing efforts.
Second, the model can capture the typical “slowing
down” in aggregate purchases over time and replicate latent
customer attrition. LSTM models are state-dependent mod-
els—their hidden states carry information over time—and
can successfully capture long-term trends. To our knowl -
edge, all previous approaches that claimed to capture latent
attrition explicitly modeled it as a binary process (alive vs.
dead). An LSTM approach can capture it implicitly.
Third, since our approach does not explicitly model cus-
tomer death, the problem of “dead” customers not being
able to “return” does not arise. This dual-LSTM model
allows customers to buy again after an extended period of
inactivity. Since these LSTM models are state-dependent
and firm policy is endogenous in the model, this renewed
customer activity could, in turn, trigger a virtuous cycle of
new solicitations and new purchases.
Finally, for each customer, the outcome is a CLV distri -
bution rather than a point estimate. Since in our simulations
firm policy and customer behaviors are endogenous and
interact dynamically over time, this dual-LSTM approach
can simulate virtuous (or vicious) cycles and diverging
paths in loyalty and profitability, thereby yielding richer
CLV distributions. The Web Appendix further positions the
dual-LSTM within the CLV literature.
LSTM model
Recurrent neural networks (RNN) are a kind of artificial
neural network particularly well suited to model and predict
sequential tasks. An RNN is formed by a chain of repeat -
ing modules, where each module passes task-relevant infor-
mation to the next module (Olah, 2015). Each module has
a multi-dimensional hidden state that is updated to form a
powerful representation of relevant information necessary
to predict future steps in the sequence.
RNN models vary in the nature and complexity of the
“modules” implemented at each step. Since we expect cus -
tomer and firm behaviors to exhibit long-term dependencies
(i.e., we expect behaviors in the distant past to remain rel -
evant to inform us about future behaviors), our model relies
on a special variant of the RNN called the long short-term
memory (LSTM) neural network. LSTM has been shown to
Fig. 4  Overview of the dual-LSTM model. ( a) The firm-customer
strategic interactions are represented as two vectors of monthly incre -
ments. (b) Based on that sequence (and monthly dummies), the first
model predicts whether the firm will solicit the customer next month.
(c) Based on the same sequence and the first model’ s prediction for
the same month, the second model predicts whether the customer
will donate. (d) The generated data is integrated into the sequence as
ground truth, thereby moving the model one step further. (e) The whole
process is repeated (e.g., 100 times) to generate a CLV distribution

1 3
Journal of the Academy of Marketing Science
be highly effective at capturing long-term dependencies in
sequential data (Hochreiter and Schmidhuber, 1997; Gers
et al., 2000).
The LSTM neural network is composed of a chain of
repeating modules, in which each module passes task-rele -
vant information to the next (Olah, 2015). Each module has
a multi-dimensional hidden state, updated with non-linear
dynamics to form a powerful representation of task-relevant
information up to that position in the sequence. Each mod -
ule in the LSTM neural network is governed by the set of
equations below, where x<t> is a vector that describes the
current state or period (in our application: donation in the
month (0/1), solicitation in the month (0/1), and monthly
dummies):
c∼<t> = tanh (Wc[a<t−1>,x <t>]+ bc) (1)
τu = σ (Wu[a<t−1>,x <t>]+ bu) (2)
τf = σ (Wf [a<t−1>,x <t>]+ bf ) (3)
τo = σ (Wo[a<t−1>,x <t>]+ bo) (4)
c<t> = τu ∗ c∼<t> + τf ∗ c<t−1> (5)
a<t> = τo ∗ tanh (c<t>) (6)
A key element of the LSTM model is its hidden state
(referred to as a<t> here). This memory is governed by a
gating mechanism consisting of three gates. The update
gate (“u”) controls when information is added to the mod -
el’s memory. The forget gate (“f”) controls when a piece
of information needs to be “erased.” The output gate (“o”)
controls when a stored piece of information is triggered to
influence the predictions at the current step. These three
gates are represented in Equations 2-4, and Figure 5 shows
the model’s “long-term” memory, along with an internal
recurrence captured in Equations 5-6, where the state of the
model at the previous step can affect current predictions (the
“short-term” memory).
The parameters Wc, Wu, Wf, and Wo are shared across the
modules; they contribute to predictions at each time step.
The gating mechanism and the internal recurrence allow the
hidden state to learn task-relevant information sequentially.
Consequently, it can leverage information observed at one
point in the sequence to improve predictions many steps
later.
For instance, imagine that a B2B firm launches a major
marketing campaign during the Christmas season for all its
customers who purchased during the previous year. During
the model calibration phase, the LSTM model will learn
to “tag” (update gate) a customer in its long-term memory
as soon as a purchase is observed in the data. During the
Christmas season, the model will use that stored memory to
predict (output gate) that the customer will be the recipient
of a major marketing campaign. Finally, once the December
campaign happens, the model will also learn to forget (for -
get gate) the memory that triggered that campaign, since it
will not be relevant anymore to make further predictions.
This illustration highlights several key points of our
modeling framework.
First, properly calibrating an LSTM model is a delicate
endeavor. In particular, it is governed by several hyperpa -
rameters (e.g., how many hidden cells we use to store the
model’s memory) that need to be fine-tuned.
Second, an LSTM model can learn complex patterns
and data-generation processes. While this ability is useful
for improving predictions of customer behaviors (see, for
instance, Sarkar & De Bruyn, 2021; Valendin et al., 2022), it
is crucial for predicting firm policies, which are usually far
more challenging to capture.
Third, if the model correctly predicts that a customer will
be the recipient of a major marketing campaign; that a major
Fig. 5 An LSTM model has three
key components: a forget gate
(f), an update gate (u), and an
output gate (o). The hidden state
represents the long-term memory
of the LSTM cell and is partially
erased (i.e., by the forget gate)
or enriched (i.e., by the update
gate) at each step. The output of
the previous step is the short-term
memory component and is fully
updated at each step

1 3
Journal of the Academy of Marketing Science
marketing campaign is correlated with a higher purchase
likelihood down the road; and that additional purchases
are, in turn, correlated with more marketing solicitations in
the future; such a dual-LSTM model can potentially simu -
late virtuous—or vicious—cycles in customer activity and
diverging paths in customer loyalty, hence generate richer
and more managerially relevant CLV distributions (a conse-
quence of the model we will explore later in greater detail).
Model calibration
The data required for our dual-LSTM model takes the form
of panel data where, for each period, we encode whether the
customer has made a purchase (0/1), whether the firm has
sent a solicitation (0/1), as well as additional relevant pre -
dictors such as seasonality indicators (i.e., dummy variables
for each month).
During the calibration phase, we split the calibration data
into the training set (80%) and the validation set (20%). The
training set is used to learn the parameters, while the valida-
tion set is used to estimate the generalization error (Good -
fellow et al., 2016).
The LSTM neural network has multiple hyperparam -
eters, and the best hyperparameters can be found through
Bayesian optimization (Sarkar & De Bruyn, 2021). There-
fore, we set the following ranges and do 100 Bayesian opti-
mization runs.
1. Hidden cells: [80, 150];
2. L2 regularization: [0, 0.0001];
3. Learning rate for optimizer: [0.0001, 0.01]
We set the batch size at 1,024 and all other settings at their
default values. For the learning algorithm, we use the Adam
optimizer in both applications.
Model predictions
In the following 36-month holdout period, we use both
LSTM models in parallel, letting them interact sequentially
over time. At each step in the holdout period, the custom -
er’s response may correlate with the firm’s strategy, and the
firm’s strategy may correlate with customer behaviors, cre -
ating complex dynamics over time.
For any given month, we first predict whether a solicita -
tion is likely to happen. Then, we integrate that solicitation
(or lack thereof) immediately to predict the likelihood of a
donation in the same month. The monthly predictions are
sequential (first the firm policy, then the customer behav -
ior), which mirrors the fact that (a) marketing campaigns
can generate responses very quickly, including during the
period they are launched, whereas (b) solicitations are
planned weeks in advance and do not incorporate donation
behaviors immediately. This ordering reflects institutional
reality confirmed by discussions with the fundraising teams:
solicitation campaigns are planned and dispatched weeks
in advance as monthly batch mailings, with targeting lists
finalized well before the mailing month. Donor responses,
by contrast, can arrive within days of receiving a solicita -
tion. The firm’s action in month t is therefore determined
before the customer’s response in month t is observed.
Effects that unfold over subsequent months are captured by
the LSTM’s hidden state, which carries information forward
through time via its gating mechanism.
We continue this approach sequentially till the end
of the holdout period. Each simulation gives us a real -
istic customer-firm interaction sequence where, at each
step, customer behavior predictions incorporate the firm’s
solicitations as covariates, and vice versa. Repeating these
simulations multiple times for each customer allows us to
generate a distribution of possible CLV paths.
Next, we test the performance of this dual-LSTM model
in an empirical application.
Empirical application
Data set
To demonstrate the potential merits of the dual-LSTM
model, we seek a data set where the firm (a) tracks its mar -
keting activity at the individual level and (b) dynamically
adapts its marketing policy based on customer behaviors
(Donkers et al., 2006). The CLV literature abounds with
illustrations in a fundraising context that meet these two
criteria.
The data set period covers nine years and three months
of donation and solicitation histories. We set aside the last
three years (years 7, 8, and 9) for out-of-sample predictions.
Additionally, we exclude individuals acquired in the two
years preceding the out-of-sample period (years 5 and 6) to
ensure sufficient data for model calibration. The final data
set comprises 21,939 donors acquired over four years and
three months (years 1, 2, 3, and 4). We observe these donors
for an additional two years, ensuring each customer has at
least two years and, at most, six years and three months of
history.
For each donor, we observe the donations made and the
marketing activity received during this calibration period.
Discussions with the fundraising team confirmed that the
charity used exclusively behavioral characteristics (recency,
frequency, monetary value) to target donors. No variables
beyond those shared with the research team were used for
targeting purposes. In addition, the database contained the

1 3
Journal of the Academy of Marketing Science
complete history of firm-customer interactions (no external
loyalty program, no interactions or solicitations outside the
direct marketing efforts already recorded in the database).
We use the next three years for holdout prediction, which
is standard in the marketing literature (Kumar, 2018) since
(1) future cash flows tend to be heavily discounted and con-
tributions beyond the first three years are small; (2) there
are many uncertainties related to customer needs, technol -
ogy, and the business environment, which make predictions
beyond three years less valuable; and (3) CLV predictions
tend to be updated on a rolling basis anyway.
Benchmarks
We compare the performance of the dual-LSTM model
against six distinct models, with each benchmark chosen to
test a specific aspect of the dual-LSTM’s contribution.
In addition to our dual-LSTM model, we include a sin-
gle-LSTM model that does not predict (and hence does not
incorporate) solicitation histories. Because a firm’s strategy
largely depends on its customers’ behaviors and is endog -
enous to them, one could argue that observing the latter may
be enough to build reliable CLV predictions. In other words,
customer behaviors and firm strategy are so intertwined that
taking only the former into account may suffice to tell the
whole story. This view would also argue that although most
CLV models are built exclusively on customer data, their
parameters implicitly incorporate the firm’s strategy. Com -
paring our dual-LSTM model to a simple-LSTM version
that ignores marketing solicitations will allow us to test that
hypothesis.
Second, we include a single-transformer model  based
on Vaswani et al. ( 2017), built solely on customer behav -
iors (similar to the single-LSTM model). Transformers
have proven to be the state-of-the-art deep learning frame -
work for natural language processing (NLP) tasks and AI
chatbots. Transformers use self-attention mechanisms (Lu
& Kannan, 2026) to process the entire sequence at once,
enabling them to have access to the global context of a
sequence (a feature that proves particularly useful in NLP
tasks where the meaning of a word might change depend -
ing on the context in which it is used). However, recent
research on time-series-based applications, such as stock
price prediction, has shown that the LSTM can outperform
the transformer in non-NLP tasks with strong sequential
dependencies (Bilokon & Qiu, 2023; Sonata and Heryadi,
2024). In particular, the attention mechanism is extremely
valuable in situations where some events that happen early
in a sequence (e.g., in NLP, at the start of a paragraph) have
a critical impact on later predictions. In a CLV context, (1)
no one event (e.g., donation or solicitation) likely supplants
the others in terms of predictive power; and (2) since the
data is divided into monthly increments, events of impor -
tance for prediction purposes should never be too far away
in the sequence. Consequently, whether a transformer model
could beat an LSTM model in our CLV context remains an
empirical question.
Third, the Pareto/NBD model (Schmittlein et al., 1987),
which is hailed as the “gold standard” in the CLV literature
(Jerath et al., 2011; Bachmann et al., 2021).
Fourth, since our dual-LSTM model makes precise indi-
vidual-level predictions, we also compare it to Abe’ s hier-
archical Bayesian version of the Pareto/NBD (Abe, 2009).
Fifth, we test a Seemingly Unrelated (SUR) Bivari -
ate Probit model, similar to Rust et al. ( 2011), where the
errors of the two model components—likelihood of dona -
tions and solicitations—are correlated. Additionally, like in
Rust et al. (2011), the model accounts for the correlation in
donation propensity across time for each individual donor.
Please refer to the Web Appendix for features included in
the model.
Sixth, we develop an always-a-share ElasticNet regres-
sion model  that endogenously incorporates firm strategy
(computational details provided in the Web Appendix). It
allows us to compare our model to another always-a-share
model that incorporates firm strategy but lacks the model
components (i.e., LSTM hidden states) necessary to capture
long-term dependencies and latent attrition. The Elastic -
Net is a versatile model that prevents overfitting by mixing
L1 and L2 regularization, governed by a hyperparameter
(alpha), which we fine-tune during the calibration process.
It uses the same model features as the SUR Bivariate Probit
model.
Criteria
We evaluate the performance of the dual-LSTM and six
benchmarks over the 36-month holdout period by com -
paring each model’s predictions against the ground truth.
We use seven criteria: (1) aggregate-level predictions; (2)
individual-level predictions; (3) identification of high-value
customers; (4) identification of high-potential customers; (5)
recovery of CLV distributions; (6) identification of bimodal
customers; and (7) responsiveness of bimodal customers to
marketing solicitations. We detail and report each criterion
in the following sections.
Aggregate-level predictions
CLV models should be able to accurately predict the firm’s
future, and this is the first criterion by which we compare
the seven models.
We observe a total of 5,930 donations during the thirty-
six-month holdout period (cf. Table 1). The Pareto/NBD

1 3
Journal of the Academy of Marketing Science
model predicts 5,998 donations, overpredicting by a mere
1.1% (although yearly prediction errors vary between
− 5.1% and + 8.4%). Abe’s model underpredicts it by
32.1% (4,028 donations). The single-transformer model
comes second at the aggregate level, over-predicting by
only + 4.9% (6,220 donations). However, it does so by
underpredicting donations in Year 1 and overpredicting in
Year 3. As expected, the two models that do not capture
latent attrition (the SUR Bivariate Probit model and the
ElasticNet regression model) both overpredict the total
number of donations by 8.1% (6,408) and 12.6% (6,680),
respectively.
Compared to these benchmarks, the dual-LSTM model
predicts an average of 6,239 donations, overpredicting the
target metric by 5.2%. The dual-LSTM model outperforms
most other benchmarks at the aggregate level, including the
single-LSTM model, but is marginally beaten by the Pareto/
NBD model and the single-transformer model. Given the
relative simplicity of the Pareto/NBD, this result is remark-
able. It further confirms its “gold standard” status.
Individual-level predictions
Once we turn our attention to individual-level predictions—
arguably a key metric for customer prioritization—a differ -
ent story emerges (see Table 2). In terms of MAE (aggregate
predictions over 36 months), the dual-LSTM model outper-
forms all other benchmarks (0.3184), followed by the Elas-
ticNet model (0.3273) and the simple LSTM model (0.3272).
The other benchmarks fare worse, with errors ranging from
+ 3.1% (single-transformer) to + 15.7% (Abe’s model). The
always-a-share CLV models (ElasticNet and SUR Bivariate
Probit) fare poorly on the RMSE metric, likely because of
their inability to capture latent attrition. Note that the poor
results in terms of RMSE, which relies on squared errors,
are mostly driven by extreme values. Both the SUR Bivari-
ate Probit and ElasticNet models predict some lifetime val -
ues above 30 donations, whereas the maximum observed in
the data is 14.
Identification of high-value customers
One of the critical applications of CLV models is to rank
customers in decreasing order of expected contributions
(Malthouse & Blattberg, 2005). While individual-level pre-
dictions are crucial, not all customers matter equally: cor -
rectly identifying the most valuable customers is far more
important than identifying the least valuable ones.
An appropriate measure of model performance is the lift
at x%. At the beginning of the holdout period, the database
contains 21,939 donors. Of these individuals, 3,066 donors
have made a total of 5,930 gifts. If we rank the 21,939
donors in decreasing order of predicted CLV and focus on
the first x% of the list, we can measure each model’s ability
to identify individuals likely to contribute the most to the
organization on average.
For instance, the top 439 individuals (top 2% of the data-
base) identified by the dual-LSTM model have made a total
of 1,100 donations, or 18.5% of the donations observed dur-
ing the holdout period, for a lift of 18.5% / 2% = 9.27. In
contrast, the top 2% of the database identified by the SUR
Bivariate Probit model only made 957 donations, for a lift
of 8.07.
Table 3 reports the lifts of each model at the typical
thresholds of 1%, 2%, 5%, and 10%. The dual-LSTM sys -
tematically outperforms all other models, including the
single-LSTM model, which usually—but not consistently—
comes a close second.
Table 1  Aggregate predictions of the dual-LSTM and six bench -
marked models compared to the ground truth over a holdout period of
thirty-six months
Year 1 Year 2 Year 3 Total
Years 1–3
Ground truth 2,412 1,924 1,594 5,930
Dual-LSTM 2,321
(-3.8%)
2,060
(+7.1%)
1,858
(+16.6%)
6,239
(+5.2%)
Single-LSTM 2,220
(-7.9%)
2,075
(+7.8%)
2,034
(+27.6%)
6,329
(+6.7%)
Single-Transformer 2,262
(-6.2%)
1,907
(-0.9%)
2,051
(+28.7%)
6,220
(+4.9%)
Pareto/NBD 2,290
(-5.1%)
1,980
(+2.9%)
1,728
(+8.4%)
5,998
(+1.1%)
Abe 1,553
(-35.6%)
1,323
(-31.2%)
1,152
(-27.7%)
4,028
(-32.1%)
SUR Bivariate Probit 2,231
(-7.5%)
2,079
(+8.1%)
2,098
(+31.6%)
6,408
(+8.1%)
ElasticNet 2,221
(-7.9%)
2,125
(+10.4%)
2,334
(+46.4%)
6,680
(+12.6%)
Table 2  Individual-level predictions (mean absolute errors and root-
mean-squared errors) of the dual-LSTM and six benchmarked models.
The percentages indicate the increase in error relative to the dual-
LSTM model
MAE RMSE
Dual-LSTM 0.3184 0.6367
Single-LSTM 0.3272
(+2.8%)
0.6411
(+0.7%)
Single-Transformer 0.3282
(+3.1%)
0.6536
(+2.7%)
Pareto/NBD 0.3344
(+5.1%)
0.6539
(+2.7%)
Abe 0.3685
(+15.7%)
0.7707
(+21.0%)
SUR Bivariate Probit 0.3660
(+15.0%)
1.0729
(+68.5%)
ElasticNet 0.3273
(+2.8%)
1.0723
(+68.4%)

1 3
Journal of the Academy of Marketing Science
Identification of high-potential customers
So far, all the success metrics we have reported have focused
on expected CLV (aggregate or individual). Still, our survey
of management consultants has highlighted the relevance of
the underlying CLV distributions (i.e., the specific outcomes
that lead to the expected CLV). We have reported that two
customers with identical expected CLV may not be equal in
the eyes of managers if they have widely different downside
risks or upside potentials.
In our fundraising database, as in many contexts, churn and
inactivity are the norm rather than the exception; therefore,
we will focus on targeting donors based solely on their upside
potential. Imagine a scenario where the fundraising manager
of the charity wishes to invite donors with the highest upside
potential, i.e., people who are most likely to make two dona-
tions or more over the next three years, to a gala dinner.
Traditionally, we would rank-order individuals by
expected CLV , categorize them as having donated twice or
more or not, and compute the models’ lift. We report the
results in Table 4. Unsurprisingly, the dual-LSTM model
performs well, providing the best lift in three of four cases,
followed by the single-LSTM model.
But what if, instead of ranking customers based on their
expected CLV , we ranked them based on the share of their
CLV distribution that falls at two donations or above, i.e.,
based on the right tail (upside potential) of their CLV dis -
tributions? If a percentage of customers have high upside
potential despite a moderate expected CLV , targeting based
on upside potential (rather than average CLV) could yield a
greater lift. We report the results in Table 5.
The results tell an interesting story. Selecting customers
based on their upside potential (the right tail of CLV distri -
butions, rather than expected CLV) as predicted by the dual-
LSTM model improves the lift by + 8.28% at 1% selection
(from 9.30 to 10.07). Selecting based on upside potential
results in a higher lift than selecting based on average CLV .
The improvement disappears when a wider pool of custom-
ers is selected (at 5% and 10%); in our context, high-poten-
tial customers are rare, so they are all selected as soon as the
reach is sufficient.
Recovery of CLV distributions
While some models likely reconstruct the underlying struc-
ture of CLV distributions better than others, identifying
high-potential customers focuses only on accurately predict-
ing the right-hand end of the distribution. But what about
the whole distribution? And since CLV distributions are
never fully observed—only one of their possible outcomes
materializes—how can we assess the model’s performance?
We report two distribution-related success metrics. First,
we compute the log-likelihood of each model’s predictions
during the holdout period . Imagine a customer with an
equal probability of placing 2, 3, 4, 5, or 6 orders within the
next three years (probability of each CLV outcome = 0.2),
with an expected CLV of four purchases. If a model predicts
a CLV distribution with a strong peak at four and associates
low probabilities with any other outcome, its prediction will
be right on in terms of expected CLV . However, its log-like-
lihood will suffer when unanticipated CLV outcomes (such
as 2 or 6 purchases) are observed in the data.
Second, we report the average Continuous Ranked Prob-
ability Score (CRPS). This metric evaluates the accuracy of
probabilistic forecasts of real-valued outcomes by measur -
ing the discrepancy between the forecast’s cumulative dis -
tribution function (CDF) and the observed CDF.
All seven models can generate CLV distributions. The
Pareto/NBD draws from its posterior distributions of λ and
µ per customer. The single-LSTM and single-transformer
Table 3 Lift of the seven models
Lift at 1% Lift at 2% Lift at 5% Lift at 10%
Dual-LSTM 10.76 9.27 7.99 5.94
Single-LSTM 10.25 8.69 7.55 5.91
Single-Transformer 9.90 8.12 7.43 5.88
Pareto/NBD 9.93 8.89 7.39 5.87
Abe 6.85 6.52 6.26 5.77
SUR Bivariate
Probit
9.07 8.07 7.24 5.78
ElasticNet 9.66 8.62 7.48 5.89
Table 4  Lift of the benchmarked models. The target variable is the
number of individuals who will make two donations or more over the
next three years. The ranking is based on expected CLV
Lift at 1% Lift at 2% Lift at 5% Lift at 10%
Dual-LSTM 9.30 9.40 9.02 6.71
Single-LSTM 9.43 9.08 8.66 6.68
Single-Transformer 9.04 8.37 8.38 6.60
Pareto/NBD 8.79 9.04 8.79 6.63
Abe 7.44 7.06 6.93 6.48
SUR Bivariate Probit 7.76 7.86 7.92 6.50
ElasticNet 8.40 8.92 8.31 6.68
Table 5  Lift of the benchmarked models. The target variable is the
number of individuals who will make two donations or more over the
next three years. The ranking is based on the right tail of their CLV distri-
butions (the probability of two or more donations)
Lift at 1% Lift at 2% Lift at 5% Lift at 10%
Dual-LSTM 10.07 9.69 9.04 6.70
Single-LSTM 9.75 9.24 8.66 6.68
Single-Transformer 8.92 9.14 8.35 6.61
Pareto/NBD 9.11 9.20 8.11 6.66
Abe 7.31 7.02 6.67 6.05
SUR Bivariate
Probit
8.15 7.99 7.93 6.43
ElasticNet 8.72 9.27 8.44 6.68

1 3
Journal of the Academy of Marketing Science
use the same Bernoulli-draw simulation process as the
dual-LSTM. The SUR Bivariate Probit and ElasticNet
generate distributions through repeated path simula -
tions with stochastic draws. Abe’s model draws from its
hierarchical posterior. No model produces a degenerate
distribution.
On both metrics, the dual-LSTM model outperforms
all the other benchmark models (see Table 6), indicating it
recovers the full CLV distributions with greater accuracy.
Identification of bimodal customers
Bimodalities in CLV distributions are a special case, but
they are managerially relevant as they indicate individu -
als at the fork of their customer journey. In this section, we
explore whether various CLV models can identify bimodal
customers and whether these bimodalities can be confirmed
in practice.
We develop an algorithm to detect modes (see Web
Appendix) in the distributions generated by the seven bench-
marks. We use a tolerance measure to ensure the detected
modes are not due to random noise in the simulations.
The tolerance measure indicates the minimum difference
between two consecutive frequencies in the distribution for
a peak to be considered a mode. We use a tolerance measure
of 20 (among 1,000 simulations) for our analyses. We report
the results in Table 7, and report example distributions in the
Web Appendix.
We find that six of the seven CLV models predict bimodal
distributions with varying frequencies. How commonly
these bimodalities are predicted appears to depend largely
on the model’s flexibility. The flexibility of the deep learning
models (dual-LSTM, single-LSTM, and single-transformer)
allows them to identify at least 5 times as many bimodal
customers as the classic Pareto/NBD model. Although the
regression-based models (SUR Bivariate Probit and Elastic-
Net) model customer-firm interactions, they do not appear
flexible enough to predict the diverging paths that could
lead to bimodal CLV distributions.
Interestingly, the single-LSTM predicts the highest num-
ber of bimodalities yet is systematically outperformed by
the dual-LSTM model (see Tables 4, 5, 6 and 7, and 8). We
suspect that the single-LSTM model is versatile enough to
predict diverging paths in customers’ CLV but, lacking the
firm’s strategy covariates, cannot predict when they happen
with precision, hence creating bimodalities more random
and less systemic than those of the dual-LSTM model.
The number of bimodal CLV distributions, while small
in absolute terms, is managerially significant. The ability
to capture bimodalities and modes at the tail impacts the
manager’s understanding of a customer’s upside potential
(i.e., “best-case scenario”). The tails of these CLV distribu-
tions are especially critical, knowing that, in our empirical
application, 0.9% of the initial customer base contributed
13.9% of the donations. Identifying 157 bimodal distribu -
tions might seem trivial. It is far less so when one remem -
bers that a mere 918 individuals in the original list of 21,939
donors accounted for 51.4% of the donations over the three-
year holdout period. The managerial significance of the 157
bimodal customers lies not in their volume but in their dif -
ferential responsiveness to marketing. As we show in the
next section, bimodal customers respond significantly more
strongly to solicitations (or lack thereof), meaning that mar-
keting resources directed toward them yield higher returns.
The relatively modest number of bimodalities found
in the CLV distributions should also be interpreted in the
light of customers’ journeys, as they represent the number
of bimodalities found at a specific point in time in the
data. To illustrate that point, Fig. 6 displays the predicted
CLV distribution of a particular donor at the end of their
first, third, fourth, and fifth year of tenure with the char -
ity. Twelve months after their acquisition (upper-left), this
particular donor has not reiterated their support yet, and
the dual-LSTM model predicts that they will likely fall in
the large category of one-time churners with a large mode
at zero. At the end of their third year (upper-right), against
all odds, the donor has made two additional donations but
appears at a fork in the road with a CLV distribution that is
strongly bimodal. A year later (lower-left), the likelihood
that they will not contribute again in the next five years
has skyrocketed; the CLV distribution is still bimodal,
but the probability mass at zero has increased. At the end
of the fifth year (lower-right), the CLV distribution has
become unimodal again, with a 72.9% probability at zero.
Over the eight years of observations for this donor, the
CLV distribution is bimodal for three years (years 2, 3,
4), where the uncertainty about the path she will follow is
highest at the end of the third year. When we report 157
bimodal distributions at the time of these analyses, one has
Table 6  Log-likelihood and CRPS in the holdout period, both indicat-
ing the extent to which each model correctly predicts the full range of
the CLV distribution. Since some probabilities are computed through
simulations, some predicted probabilities might be zero, and the log-
likelihood would collapse. To prevent it, we set a floor probability of
0.005 for all models
Log-likelihood(holdout
period)
AverageCRPS
Dual-LSTM -10,199 0.1740
Single-LSTM -10,262 0.1750
Single-Transformer -10,745 0.1823
Pareto/NBD -10,466 0.1822
Abe -12,478 0.2220
SUR Bivariate Probit -10,928 0.2121
ElasticNet -11,302 0.2170

1 3
Journal of the Academy of Marketing Science
to remember that many donors had a bimodal distribution
in the past, and many will have bimodal distributions in the
future.
One of the inherent difficulties in predicting bimodal dis-
tributions is that they cannot be observed ex-post. If a cus -
tomer is predicted to have a 50% chance of being loyal and
very active and a 50% chance of churning for good, only
one scenario will materialize.
However, one way to verify that the bimodal distribu -
tions predicted by the dual-LSTM are not simply a model -
ing fluke but instead indicate customers who are at a fork
in the road is to compare the CLV realizations to their
expectations.
Imagine two customers: one is correctly predicted to
make five purchases with 100% certainty (unimodal CLV).
The second will place ten orders or none, with a 50%
chance for each scenario (bimodal CLV). Their expected
CLV is identical (= 5), and the predictions are spot on in
both cases, but the realization of the second will be far
away from its CLV expectation (either 0 or 10), whereas
the realization of the first will be very close (= 5). Even
though the bimodal distribution cannot be observed ex-
post, we can verify its accuracy nonetheless.
We analyze the 21,782 unimodal and 157 bimodal
customers (as predicted by the dual-LSTM model) sep -
arately, and we report the mean absolute error (MAE)
and the root mean squared error (RMSE) for each group
based on the predictions from the seven models. As
expected, the MAE (across all models) on all bimodal
customers is + 317% larger on average than for unimodal
customers (from 0.333 to 1.387). The average RMSE is
+ 156% larger as well, providing supporting evidence
that predicted bimodalities were correctly predicted. The
dual-LSTM model is the highest-performing model (see
Table 8).
Responsiveness of bimodal customers to marketing
solicitations
If bimodal CLV distributions represent a fork in the road
of the customer’s future path, timely marketing to these
bimodal customers should be impactful, nudging them
from a low-value trajectory toward a high-value one. In
other words, customers with bimodal CLV distributions
should be more responsive to marketing than unimodal
customers with comparable characteristics. We test this
hypothesis below.
Table 7 Analysis of the CLV distributions predicted by the dual-LSTM and six benchmark models over a three-year holdout period. The dual-
LSTM, the single-LSTM, and the single-transformer models identify far more diverging paths and bimodalities
Table 8  Individual-level predictions (mean absolute errors and root-
mean-squared errors) of the seven models computed separately on the
(predicted) 21,782 unimodal and 157 bimodal customers as identified
by the dual-LSTM. The stark increase in MAE (from predicted uni -
modal to bimodal customers) confirms the likely presence of bimo -
dalities
Unimodal
customers
Bimodalcustomers
MAE RMSE MAE RMSE
Dual-LSTM 0.312 0.629 1.141
(+265.7%)
1.296
(+106.0%)
Single-LSTM 0.322 0.634 1.104
(+242.8%)
1.308
(+106.3%)
Single-Transformer 0.322 0.646 1.154
(+258.4%)
1.364
(+111.1%)
Pareto/NBD 0.328 0.645 1.195
(+264.3%)
1.408
(+118.3%)
Abe 0.360 0.758 1.487
(+313.1%)
1.823
(+140.5%)
SUR Bivariate Probit 0.356 1.043 1.686
(+373.6%)
3.132
(+200.3%)
ElasticNet 0.317 1.042 1.709
(+439.1%)
3.173
(+204.5%)

1 3
Journal of the Academy of Marketing Science
Matching design
To mitigate observable differences between bimodal and
unimodal customers, we implement Coarsened Exact
Matching (CEM). We define the treatment indicator Bimo-
dali as 1 if customer i exhibits at least two modes in the
simulated CLV distribution produced by the dual-LSTM
model, and 0 otherwise. Matching is performed using cus -
tomer characteristics measured at the end of the calibra -
tion period: customer tenure, donation frequency, donation
recency, expected CLV from the dual-LSTM simulations,
solicitation frequency, and solicitation recency. CEM pro -
ceeds by coarsening each continuous baseline covariate into
decile-based bins and then exactly matching treated and
control customers within the resulting multidimensional
strata. Of the 157 bimodal customers predicted by the dual-
LSTM, 146 were matched with 1,307 unimodal customers
with identical characteristics. Table 9 reports the covariate
balance before and after matching. All post-match standard-
ized mean differences fall below the conventional |SMD| <
0.20 threshold, with the largest imbalance at 0.152.
We note that the dual-LSTM model is explicitly predic -
tive, not causal. The CEM design mitigates observable con-
founds between bimodal and unimodal customers, but we
do not claim full causal identification of the effect of solici-
tations on donations. The associations we report may reflect
selection effects or other non-causal pathways (Simester et
al., 2020).
Outcome model  To measure the responsiveness of matched
bimodal and unimodal customers, we investigate the impact
of solicitations in the first year post-matching on donations
received during the same period. We use a one-year window
because shorter periods (three or six months) yield too few
donations per customer to measure responsiveness reliably,
whereas longer windows (two or three years) are likely con-
taminated by adaptive marketing, reduced sensitivity due
to over-solicitation of responsive customers, and other con-
founds. To account for potential lagged effects of solicita -
tions on donations, we additionally report a specification
where the solicitation window is restricted to the first six
months post-matching while the donation window remains
at twelve months.
We estimate the following linear regression on the CEM-
matched sample, using the CEM weights:
HoldoutDonations i = βo + β1 HoldoutM arketingi+
β2 Bimodali + β3(HoldoutM arketingi × Bimodali)+γ
′
Xi + εi  (7)
where HoldoutMarketingi is the number of solicitations
received during the holdout period, Bimodali is the treat -
ment indicator, and Xi is a vector of matching covariates
included to absorb residual imbalance. The coefficient of
Table 9 Covariate balance before and after Coarsened Exact Match -
ing (CEM; decile coarsening). Notes: Lower absolute SMDs indicate
better balance
SMD (Unmatched) SMD (Matched)
Customer tenure -0.275 -0.002
Past donation frequency 1.393 -0.119
Past donation recency -8.887 0.021
Expectation CLV 3.481 -0.105
Past marketing frequency 0.901 -0.002
Past marketing recency -53.393 -0.152
Fig. 6 CLV distribution (five-year
predictions) of the same donor at
the end of their first (upper-left),
third (upper-right), fourth (lower-
left), and fifth year (lower-right)
with the charity. Each distribu-
tion has 1,000 data points, for as
many simulations of the path that
donor could follow over the next
five years. Please note that, for
clarity, years three and four use a
different y-axis scale

1 3
Journal of the Academy of Marketing Science
interest is β₃, which captures whether bimodal customers
respond more strongly to solicitations than their unimodal
counterparts. We report the results in Table 10.
The results tell an interesting story. The interaction
between holdout marketing and bimodal status is positive
and statistically significant in both specifications: β₃=0.049
(p = 0.046) for the six-month solicitation window, and
β₃=0.021 (p = 0.011) for the twelve-month window. Bimodal
customers are more responsive to the firm’s marketing than
observably identical unimodal customers, supporting our
hypothesis that bimodal customers are indeed at a fork in
their customer journey, and that marketing to these custom-
ers can lead to stronger returns.
Examining the first three parameters, unimodal and
bimodal customers respond similarly to marketing solici -
tations at around N = 4 solicitations. Below that threshold,
donations from bimodal customers drop off more steeply
than those of unimodal customers. Yet at just 7 solicitations,
marketing effectiveness among bimodal customers reaches
twice that of their unimodal counterparts. In short, bimodal
customers are more volatile; they disengage faster when
neglected but respond more strongly when actively solicited,
as predicted. This pattern also speaks to downside risk: the
absence of marketing is more harmful for bimodal custom -
ers than for unimodal ones. Managers should therefore view
bimodal status not only as an opportunity for upside but also
as a warning that neglect carries disproportionate costs.
To translate Eq. (7) into meaningful figures, we compute
the marginal return on one additional solicitation under
industry-typical assumptions: an average gift of $75 and a
unit cost of $1.25 per solicitation. Holding observable donor
characteristics constant through CEM matching, an extra
solicitation to a unimodal donor yields 0.0084 incremental
donations, generating $0.63 in expected revenue against a
$1.25 cost, an ROI of − 50%, which suggests that the typi -
cal unimodal donor in our database is oversolicited on aver-
age. The same solicitation to a bimodal donor yields 0.0295
incremental donations, generating $2.21 in revenue, an ROI
of + 77%, leaving significant upside potential untapped.
The asymmetry is stark: a more-than-threefold gap in
responsiveness.
Do these results generalize beyond the dual-LSTM model?
One could argue that the bimodal classifications we use as a
treatment variable simply reflect the flexibility of the dual-
LSTM model, and that any model flexible enough to identify
bimodalities would yield a similar result. To test this, we rep-
licated the CEM matching and regression analyses using the
bimodal classifications produced by each benchmark model:
the single-LSTM, the single-transformer, the ElasticNet, the
SUR Bivariate Probit, and the Pareto/NBD. In none of these
cases does the interaction term HoldoutMarketing × Bimodal
reach statistical significance under CEM matching (see Web
Appendix for complete results). In other words, when com-
peting models classify customers as “bimodal,” those clas -
sifications do not correspond to observable differences in
marketing responsiveness. Only the dual-LSTM model’s
distributional predictions map onto actionable heterogeneity
in the data, consistent with our argument that both modeling
customer-firm interactions and the flexibility of a deep learn-
ing specification are required to capture meaningful bimodal
patterns. Of particular interest, the single-LSTM model iden-
tifies the largest number of bimodal customers (489) yet pro-
duces the weakest interaction effect. This is consistent with
our earlier observation that the single-LSTM, lacking firm
strategy covariates, generates bimodalities that are more ran-
dom and less managerially meaningful than those predicted
by the dual-LSTM model.
Methodological considerations
We chose CEM as our primary matching design for two
reasons. First, CEM does not rely on a parametric propen -
sity score model, which could be misspecified. Second, as
Table 10 Responsiveness of bimodal vs. unimodal customers to the
firm’s marketing (CEM Matching; linear regression). Notes: All mod-
els are estimated on the CEM-matched sample using CEM weights.
P-values reported in parentheses. Values in bold indicate p < 0.05
Donations = 12 months
Solicitations = 6 months
Donations = 12 months
Solicitations = 12 months
Holdout
marketing
0.0220
(0.117)
0.0084
(0.086)
Bimodal -0.1840
(0.205)
-0.2285
(0.090)
Holdout
marketing ×
Bimodal
0.0488
(0.046)
0.0211
(0.011)
Customer
tenure
0.0009
(0.0042)
0.0010
(0.037)
Past donation
frequency
-0.0084
(0.640)
-0.0078
(0.666)
Past donation
recency
-0.0011
(0.270)
-0.0011
(0.292)
Expectation
CLV
0.3858
(< 0.001)
0.3829
(< 0.001)
Past marketing
frequency
-0.0028
(0.011)
-0.0030
(0.006)
Past marketing
recency
0.0285
(0.103)
0.0300
(0.083)
Constant -0.1466
(0.354)
-0.1445
(0.343)
Observations
(N)
1,453 1,453
R² 0.1063 0.1086
Adj. R² 0.1007 0.1031

1 3
Journal of the Academy of Marketing Science
reported in Table 9, CEM achieves excellent covariate bal -
ance, with all post-match SMDs well below the conventional
threshold. As a robustness check, we also implemented
Propensity Score Matching (PSM) with nearest-neighbor
matching (5:1 ratio, with replacement, caliper of 0.2).
The PSM results are consistent with the CEM estimates,
although post-match balance is somewhat weaker (the larg-
est SMD is 0.366 for Expectation CLV; see Web Appen -
dix for details). We further verified the robustness of these
findings using Poisson PML with sandwich standard errors
(to account for the count nature of the dependent variable),
and the substantive conclusions remain unchanged across
all four combinations of matching method (CEM vs. PSM)
and regression specification (linear vs. Poisson). We report
all robustness checks in the Web Appendix.
Summary
The above results, once combined, tell a compelling story
about the value of combining deep learning flexibility with
endogenous firm strategy in CLV prediction.
On the one hand, the ElasticNet model incorporates the
firm strategy endogenously in its predictions and seems to
predict CLV at the individual level well. However, it does
not contain an attrition component and fails to capture the
slowing down of donations over time. By the third year, it
overpredicts donations by + 46.4%, showing that the overall
trend is poorly estimated. The SUR Bivariate Probit model
overpredicts donations by + 31.6%, too.
The Pareto/NBD model, on the other hand, captures
long-term trends remarkably well and achieves the best out-
of-sample performance in the aggregate. When it comes
to individual-level prediction errors (MAE and RMSE) or
the ability to rank customers by order of expected contri -
bution or upside potential, however, performance is more
disappointing.
The deep learning models are highly flexible and achieve
strong performance, especially when it comes to predicting
individual CLV . However, only when the flexibility of deep
learning models is associated with the richness of incor -
porating the firm’s strategy (i.e., the dual-LSTM model)
does the model shine. Of the 24 success metrics reported
in the preceding pages, the dual-LSTM model outperforms
all other benchmarks 19 times (79%) and ranks second an
additional 3 times (for a total of 92%).
Perhaps more importantly, the dual-LSTM model is the
only model whose distributional predictions translate into
differential managerial outcomes. The matching analysis
reveals that bimodal customers, as identified by the dual-
LSTM model, are significantly more responsive to the
firm’s marketing solicitations than observably identical
unimodal customers. This finding is robust across matching
methods (CEM and PSM), regression specifications (lin -
ear and Poisson PML), and solicitation windows (six and
twelve months). Bimodal customers disengage faster when
neglected but respond more strongly when actively solic -
ited, consistent with the intuition that they stand at a genu -
ine fork in their customer journey, where timely marketing
intervention can nudge them from a low-value trajectory
toward a high-value one.
Crucially, this result is unique to the dual-LSTM model.
When we replicate the identical matching and regression
analyses using the bimodal classifications produced by
the six benchmark models, none yields a statistically sig -
nificant positive interaction between marketing solicitations
and bimodal status (see Web Appendix). The single-LSTM
model is particularly instructive: despite identifying the
largest number of bimodal customers (489, compared to
157 for the dual-LSTM), it produces the weakest interaction
effect, with estimates near zero. This pattern reinforces our
earlier observation that the single-LSTM, lacking firm strat-
egy covariates, generates bimodalities that are more random
and less systematic, and hence less managerially actionable.
In other words, it is precisely the combination of deep learn-
ing flexibility and endogenous firm policy—the defining
features of the dual-LSTM architecture—that enables the
model to identify customers for whom marketing interven -
tions yield demonstrably stronger returns.
Conclusions
General discussion
In our survey of management consultants from a leading
global strategy firm, 79% drew a sharp distinction between
two customers with identical expected CLV but different
distributional profiles, splitting roughly evenly between
risk-averse and upside-seeking preferences. Consequently,
this paper has argued that customer lifetime value (CLV) is
more naturally understood as a distribution than as a num -
ber, and that the architecture required to recover that distri -
bution must let firm and customer co-evolve over time. The
dual-LSTM model we have developed delivers both.
Within the CLV distributions, the dual-LSTM surfaces a
particular kind of structure the other models cannot identify:
bimodalities. When the firm and the customer co-adapt over
time stochastically, small initial differences can amplify into
diverging paths and predict CLV bimodal distributions. One
peak corresponds to the donor who stays engaged. The other,
to the donor who fades out. We identify 157 such custom -
ers in our database at a particular point in time, observably
indistinguishable from their unimodal peers along recency,
frequency, monetary value, expected CLV , and marketing

1 3
Journal of the Academy of Marketing Science
exposure, yet substantively different in what they do next.
Holding these covariates constant through coarsened exact
matching, an additional solicitation produces 3.5 times
more incremental donations from a bimodal donor than
from an observationally identical unimodal one (β₃=0.021,
p = 0.011, twelve-month window). The result survives
matching design, regression specification, and solicita -
tion window, and is, in our data, unique to the dual-LSTM.
When we replicate the matching analysis using the bimodal
classifications from each of the six benchmark models, none
yields a statistically significant interaction.
On more conventional grounds, the dual-LSTM outper -
forms six well-established benchmarks on most evaluation
metrics. It beats the Pareto/NBD gold standard at the indi -
vidual level, the regression-based always-a-share family
on distributional recovery, and the recent transformer and
sequence-to-sequence deep-learning alternatives on the
joint task of attrition and policy modeling. These improve -
ments alone would barely justify the additional complexity
of training two coupled LSTMs. What does justify it is that
the same model produces the distributional structure that
allows bimodal customers to be identified and their differ -
ential responsiveness measured.
The contribution sits in deliberate tension with a recent
and visible direction in the field. A growing body of work has
sought to move CLV from a predictive metric to a prescrip-
tive decision tool, using causal inference frameworks, rein-
forcement learning, and dynamic optimization to determine
what the firm should do, not just what will happen (Manda-
nia et al., 2025; Ogundipe, 2025; Umezurike et al., 2025;
Kalishina, 2025). The direction is intellectually compelling,
but operationally complex. It requires randomized or quasi-
experimental data to identify causal effects (Ogundipe, 2025;
Umezurike et al., 2025), repeated exploration of actions via
A/B tests or multi-armed bandits with attendant short-term
performance risk (Mandania et al., 2025; Kalishina, 2025),
complex feature engineering and temporal cross-validation
pipelines (Sun et al., 2023; Cowan et al., 2023), continuous
model updating and feedback loops (Abass et al., 2025), or
the integration of multiple data sources before any interven-
tion optimization can proceed (Doğan et al., 2024; Naphade,
2025). Implementation-oriented work further documents
that rolling sophisticated CLV models into production
demands substantial engineering and change management,
often at odds with managers’ preference for simpler heu -
ristics (Curiskis et al., 2023; Chadaga et al., 2025). The
dual-LSTM sidesteps these barriers. It operates on standard
observational data—the kind of transactional and solicita -
tion histories most firms already collect—and requires no
experimental variation, no counterfactual estimation pro -
tocol, and no reinforcement-learning infrastructure. It still
delivers distributional insights, including the identification
of bimodal customers who are demonstrably more respon -
sive to marketing, that prescriptive models aspire to and
rarely achieve without far heavier investment.
Managerial implications
For a manager reading the dual-LSTM’s output, the first
question is no longer “what is this customer worth?” but
“what shape is the customer’s value?” Two customers with
the same expected CLV can sit on very different ground.
One has a tight, unimodal distribution: low downside risk,
modest upside, a known quantity. The other has a fat right
tail or a second mode: less certain, but with material prob -
ability of becoming exceptional. The two require different
management. The first is best treated as a stable contribu -
tor whose marketing should focus on retention. The second
is best treated as an upside potential bet whose marketing
should focus on conversion. The survey of strategy con -
sultants we ran at the outset of this work confirmed that
managers, when asked, choose between these two profiles
in roughly equal numbers, with the split reflecting on the
manager’s risk aversion rather than any objective property
of the customer.
The most immediate operational consequence is a change
in how customers are ranked. Standard practice ranks by
expected CLV and targets the top decile or quintile. The
dual-LSTM allows a second ranking, by the right-tail prob-
ability that a customer will exceed a threshold the manager
defines (for instance, the probability of making two or more
donations over the next three years). The two rankings over-
lap, but not perfectly. In our data, the top 1% of customers
under the right-tail ranking captures high-potential donors at
a lift of 10.07, against 9.30 under the expected-CLV ranking
using the same model (Tables 4 and 5). The right-tail rank-
ing is the appropriate target when the manager is acquiring
or developing customers whose ceiling matters more than
their floor: new donor cohorts, upper-tier prospects in B2B
sales, premium segments in retail. The mean cannot tell the
manager which of two equal-expected-value customers has
the higher ceiling. The distribution can.
Bimodal customers warrant a distinct discussion. These
are the donors in our database who sit at a fork in their jour-
ney, with significant probability of either becoming substan-
tially more engaged or fading out entirely. We show they are
3.5 times more responsive to an additional solicitation than
observationally identical unimodal donors. These donors
are more responsive in both directions, which means the
firm actions carry more downside risk and upside poten -
tial than they do with a stable donor. The dual-LSTM is,
to our knowledge, the only model in the current empirical
literature that lets a manager identify them prospectively,
before the fork resolves. The differential responsiveness

1 3
Journal of the Academy of Marketing Science
has direct financial consequences. Under industry-typical
assumptions, the marginal return on one additional contact
is − 50% for a unimodal donor and + 77% for a bimodal
one (Table 10, twelve-month window). The typical donor
in our database appears oversolicited. The bimodal donor
does not. A reallocation that quietly shifts contact volume
from the unimodal mass to the bimodal segment would, by
these figures alone, generate net revenue at no incremental
marketing cost.
Limitations and future research
Empirically, the model captures the trajectory of aggregate
donations less cleanly than we would like: across the three-
year holdout, observed donations decline by 34% from
Year 1 to Year 3, while the model predicts a 20% decline.
The gap suggests room for structural improvements in
deep recurrent architectures to capture latent attrition more
crisply. The model also costs more than its main competitor.
LSTM modules are now standard in deep-learning toolkits,
but they remain harder to specify, tune, and deploy than a
Pareto/NBD that runs in a spreadsheet. The gain in distri -
butional fidelity has to be weighed against the engineering
overhead. Finally, the database we analyzed contained no
donor descriptors, such as demographics, channel of acqui-
sition, or donor history with comparable causes, since these
were stripped to preserve anonymity. Including them, when
available, would likely improve predictions, especially for
newly acquired donors whose behavioral histories are short.
We must also discuss in more depth a more fundamental
limitation. The dual-LSTM, like all CLV models calibrated
on observational data, is endogenous to the firm policy in
place at the time of data collection. Its predictions about
how customers will react to solicitations are reliable only
to the extent that the policy in question has been observed
with sufficient frequency in the past. The model should not,
therefore, be used as a simulator inside a reinforcement-
learning framework to discover an “optimal” firm policy.
Such optimization would inevitably explore regions of the
action space that are underrepresented in the training data
and where predictions are unreliable (Simester et al., 2020;
De Bruyn et al., 2020). Developing constrained optimiza -
tion approaches that respect the boundaries of the observed
data—ideally drawing on randomized training data and con-
strained search algorithms (Liu, 2023)—is, in our view, the
most promising near-term direction for extending the model
from prediction toward prescription.
Several other technical extensions follow naturally from
the panel structure. First, the model presently incorporates
only marketing solicitations; other covariates (e.g., offline
advertising exposure, brand-perception measures, chan -
nel of acquisition) could be added directly without altering
the architecture. Second, following Fader et al. ( 2005b), a
separate purchase-amount model could be layered onto the
incidence predictions; the LSTM framework should accom-
modate dynamic amount predictions, although the addi -
tion could shift the distributional patterns we observe (for
instance, if high-value donors carry systematically different
bimodality profiles). Third, with forward predictions of firm
policy already endogenized, the model is well positioned to
incorporate marketing and maintenance costs into the CLV
calculation itself. Finally, given that CLV predictions serve
as building blocks in customer-based corporate valuation
(Gupta et al., 2004; McCarthy et al., 2017), the implications
of bimodality and distributional structure for firm valuation
are, to our knowledge, unexplored. A donor base with many
bimodal customers is worth a different amount, since the
outcome is riskier, than a donor base with the same expected
revenue and unimodal distributions throughout.
The dual-LSTM was built and tested on a charitable fun-
draising database, but the architecture is general. Anywhere
a firm and customers interact dynamically over time, and
the firm’s policy adapts to what the customer does, the same
approach should apply. B2B sales pipelines, where account
managers escalate or de-escalate contact based on engage -
ment signals (Rust et al., 2011), are a natural fit. Email
marketing campaigns, where send frequency responds to
click and open behavior (Zhang et al., 2017), are another.
Price-discount coupons in retail (Park et al., 2018), loyalty-
program contacts in airlines and hotels, and personalized
push notifications in subscription services all share the
structural property—firm policy reacts to customer behav -
ior, customer behavior reacts to firm policy—that makes
the dual architecture useful. None of these settings has, to
our knowledge, been studied with a model that endogenizes
both sides. Doing so would tell us whether the bimodality
and the differential responsiveness we observe in fundrais -
ing are a property of this particular context or a general fea-
ture of dynamically interactive customer–firm systems. Our
wager is on the latter.
The major contribution of this work lies in reframing
CLV as a distributional, dynamic construct shaped by the
interaction between firm and customer over time, and in
providing a model that captures the dynamic, recovers the
distribution, and delivers actionable managerial insight—
the bimodal segment, the right-tail ranking, the financial-
reallocation case— without the experimental, prescriptive,
and infrastructural burden that the recent CLV literature has
come to assume. The expected CLV is, and has always been,
a valuable summary. It need not be the only one.
Supplementary Information The online version contains supplementary
material available at  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 7 / s 1 1 7 4 7 - 0 2 6 - 0 1 1 9 3 - x     .
Acknowledgments Not Applicable.

1 3
Journal of the Academy of Marketing Science
Author Contribution Mainak Sarkar contributed to conceptualization,
literature review, data preparation, model implementation, data analy-
sis, and writing. Arnaud De Bruyn contributed to conceptualization,
literature review, procuring the data, data preparation, data analysis,
and writing.
Funding No funds, grants, or other support was received.
Declarations
Ethical Approval  The plan for the managerial survey has been re -
viewed by the Research Ethics Board at ESSEC Business School, ref-
erence number 2025-051.
Competing interest Both authors have no conflict of interest to de -
clare that are relevant to this article.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Abass, O., Balogun, O., & Didi, P. (2025). A cross-market framework
for optimizing customer experience and lifetime value in telecom
portfolios. Engineering and Technology Journal.
Abe, M. (2009). Counting your customers one by one: A hierarchical
Bayes extension to the Pareto/NBD model. Marketing Science,
28(3), 541–553.
Bachmann, P., Meierer, M., & Näf, J. (2021). The role of time-varying
contextual factors in latent attrition models for customer base
analysis. Marketing Science, 40(4), 783–809.
Bemmaor, A. C., & Glady, N. (2012). Modeling purchasing behavior
with sudden death: A flexible customer lifetime model. Manage-
ment Science, 58(5), 1012–1021.
Bilokon, P., & Qiu, Y . (2023). Transformers versus LSTMs for elec-
tronic trading. arXiv preprint arXiv:2309.11400.
Chadaga, A., Legg, M., & Liu, B. (2025). Enhancing customer lifetime
value using data science and predictive modeling. Technium Busi-
ness and Management, 12, 112–125.
Cowan, G., Mercuri, S., & Khraishi, R. (2023). Modelling cus -
tomer lifetime-value in the retail banking industry. arXiv,
abs/2304.03038.
Curiskis, S., Dong, X., Jiang, F., & Scarr, M. (2023). A novel approach
to predicting customer lifetime value in B2B SaaS companies.
Journal of Marketing Analytics, 11, 587–601.
De Bruyn, A., Viswanathan, V ., Beh, Y . S., Brock, J. K. U., & von Wan-
genheim, F. (2020). Artificial intelligence and marketing: Pitfalls
and opportunities. Journal of Interactive Marketing, 51, 91–105.
Dew, R., & Ansari, A. (2018). Bayesian nonparametric customer base
analysis with model-based visualizations. Marketing Science ,
37(2), 216–235.
Doğan, O., Hızıroğlu, A., Pişirgen, A., & Seymen, O. (2024). Business
analytics in customer lifetime value: An overview analysis (p. 15).
Data Mining and Knowledge Discovery.
Donkers, B., Paap, R., Jonker, J. J., & Franses, P. H. (2006). Deriving
target selection rules from endogenously selected samples. Jour-
nal of Applied Econometrics, 21(5), 549–562.
Esteban-Bravo, M., Vidal-Sanz, J. M., & Yildirim, G. (2014). Valuing
customer portfolios with endogenous mass and direct marketing
interventions using a stochastic dynamic programming decompo-
sition. Marketing Science, 33(5), 621–640.
Fader, P. S., & Hardie, B. G. S. (2009). Probability models for cus -
tomer-base analysis. Journal of Interactive Marketing , 23(1),
61–69.
Fader, P. S., Hardie, B. G. S., & Lee, K. L. (2005a). Counting your
customers the easy way: An alternative to the Pareto/NBD model.
Marketing Science, 24(2), 275–284.
Fader, P. S., Hardie, B. G. S., & Lee, K. L. (2005b). RFM and CLV:
Using iso-value curves for customer base analysis. Journal of
Marketing Research, 42(4), 415–430.
Fader, P. S., Hardie, B. G. S., & Shang, J. (2010). Customer-base anal-
ysis in a discrete-time noncontractual setting. Marketing Science,
29(6), 1086–1108.
Gers, F. A., Schmidhuber, J., & Cummins, F. (2000). Learning to
forget: Continual prediction with LSTM. Neural Computation ,
12(10), 2451–2471.
Glady, N., Lemmens, A., & Croux, C. (2015). Unveiling the relation -
ship between the transaction timing, spending and dropout behav-
ior of customers. International Journal of Research in Marketing,
32(1), 78–93.
Goodfellow, I., Bengio, Y ., & Courville, A. (2016). Deep learning .
MIT Press.
Gopalakrishnan, A., Bradlow, E. T., & Fader, P. S. (2017). A cross-
cohort changepoint model for customer-base analysis. Marketing
Science, 36(2), 195–213.
Gupta, S. (1991). Stochastic models of interpurchase time with time-
dependent covariates. Journal of Marketing Research , 28(1),
1–15.
Gupta, S., Lehmann, D. R., & Stuart, J. A. (2004). Valuing Customers.
Journal of Marketing Research, 41(1), 7–18.
Gupta, S., Hanssens, D., Hardie, B., Kahn, W., Kumar, V ., Lin, N., &
Sriram, S. (2006). Modeling customer lifetime value. Journal of
Service Research, 9(2), 139–155.
Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory.
Neural Computation, 9(8), 1735–1780.
Jerath, K., Fader, P. S., & Hardie, B. G. S. (2011). New perspectives on
customer death using a generalization of the Pareto/NBD model.
Marketing Science, 30(5), 866–880.
Kalishina, D. (2025). Algorithmic customer churn prediction and tar -
geted intervention: Optimizing customer lifetime value in data-
sparse SME environments. World Journal of Advanced Research
and Reviews, 26(1), 593–603.
Kumar, V . (2018). A theory of customer valuation: Concepts, metrics,
strategy, and implementation. Journal of Marketing, 82(1), 1–19.
Kumar, V ., & Shah, D. (2009). Expanding the role of marketing: From
customer equity to market capitalization. Journal of Marketing ,
73(6), 119–136.
Kumar, V ., Venkatesan, R., Bohling, T., & Beckmann, D. (2008). Prac-
tice Prize Report—The power of CLV: Managing customer life -
time value at IBM. Marketing Science, 27(4), 585–599.
Littler, S. (2024). Cumulative Gains and Lift Curves: Measuring the
Performance of a Marketing Campaign, available at  h t t  p s : /  / s e  l e
c  t - s  t a t  i s t i  c s  . c o  . u k /  b l o  g / c  u m u  l a t  i v e -  g a  i n s - a n d - l i f t - c u r v e s - m e a s u r i
n g - t h e - p e r f o r m a n c e - o f - a - m a r k e t i n g - c a m p a i g n /
Liu, X. (2023). Dynamic coupon targeting using batch deep reinforce-
ment learning: An application to livestream shopping. Marketing
Science, 42(4), 637–658.

1 3
Journal of the Academy of Marketing Science
Lu, Z., & Kannan, P. K. (2026). AI for Customer Journeys: A Trans -
former Approach. Journal of Marketing Research, 63(1), 1–26.
Ma, L., & Sun, B. (2020). Machine learning and AI in marketing—
Connecting computing power to human insights. International
Journal of Research in Marketing, 37(3), 481–504.
Malthouse, E. C., & Blattberg, R. C. (2005). Can we predict customer
lifetime value? Journal of Interactive Marketing, 19(1), 2–16.
Manchanda, P., Rossi, P. E., & Chintagunta, P. K. (2004). Response
modeling with nonrandom marketing-mix variables. Journal of
Marketing Research, 41(4), 467–478.
Mandania, R., Cadogan, J., Liu, J., & Kazmi, N. (2025). Optimizing
promotional campaigns to maximize customer lifetime value: A
dynamic learning approach. Journal of Service Research.
McCarthy, D. M., Fader, P. S., & Hardie, B. G. (2017). Valuing sub -
scription-based businesses using publicly disclosed customer
data. Journal of Marketing, 81(1), 17–35.
Naphade, D. (2025). Customer lifetime value (CLTV): Predictive
modeling, scalable data pipelines, and business strategy . Inter-
national Research Journal of Modernization in Engineering Tech-
nology and Science.
Ogundipe, O. O. (2025). Predictive Modeling of Customer Lifetime
Value in ECommerce Using Deep Learning and Causal Inference.
Global Journal of Intelligent Technologies, 5(1), 4–12.
Olah, C. (2015). Understanding LSTM networks. Available at  h t t  p s : /  / c
o  l a h  . g i t h u b . i o / p o s t s / 2 0 1 5 - 0 8 - U n d e r s t a n d i n g - L S T M s /
Park, C. H., Park, Y . H., & Schweidel, D. A. (2018). The effects of
mobile promotions on customer purchase dynamics. Interna-
tional Journal of Research in Marketing, 35(3), 453–470.
Pfeifer, P. E., & Carraway, R. L. (2000). Modeling customer relation-
ships as Markov chains. Journal of Interactive Marketing, 14(2),
43–55.
Platzer, M., & Reutterer, T. (2016). Ticking away the moments: Tim -
ing regularity helps to better predict customer activity. Marketing
Science, 35(5), 779–799.
Raman, V . (2021). The Lost Art of Decile Analysis, available at  h t t    p  s : / /
w  w  w  .  k   d n  u  g  g e  t  s  . c o  m / 2 0 2 1 / 0 7 / l o s t - a r t - d e c i l e - a n a l y s i s . h t m l
Reinartz, W. J., & Kumar, V . (2003). The Impact of Customer Rela-
tionship Characteristics on Profitable Lifetime Duration. Journal
of Marketing, 67(1), 77–99.
Reutterer, T., Platzer, M., & Schröder, N. (2021). Leveraging purchase
regularity for predicting customer behavior the easy way. Interna-
tional Journal of Research in Marketing, 38(1), 194–215.
Romero, J., Van der Lans, R., & Wierenga, B. (2013). A partially hid-
den Markov model of customer dynamics for CLV measurement.
Journal of Interactive Marketing, 27(3), 185–208.
Rust, R. T., Kumar, V ., & Venkatesan, R. (2011). Will the frog change
into a prince? Predicting future customer profitability. Interna-
tional Journal of Research in Marketing, 28(4), 281–294.
Sarkar, M., & De Bruyn, A. (2021). LSTM response models for direct
marketing analytics: Replacing feature engineering with deep
learning. Journal of Interactive Marketing, 53, 80–95.
Schmittlein, D. C., & Peterson, R. A. (1994). Customer base analysis:
An industrial purchase process application. Marketing Science ,
13(1), 41–67.
Schmittlein, D. C., Morrison, D. G., & Colombo, R. (1987). Counting
your customers: Who are they and what will they do next? Man-
agement Science, 33(1), 1–24.
Schweidel, D. A., & Knox, G. (2013). Incorporating direct market -
ing activity into latent attrition models. Marketing Science, 32(3),
471–487.
Simester, D., Timoshenko, A., & Zoumpoulis, S. I. (2020). Target -
ing prospective customers: Robustness of machine-learning
methods to typical data challenges. Management Science, 66(6),
2495–2522.
Sonata, I., & Heryadi, Y . (2024, July). Comparison of LSTM and
Transformer for time series data forecasting. In 2024 7th Inter -
national Conference on Informatics and Computational Sciences
(ICICoS) (pp. 491–495). IEEE.
Sun, Y ., Liu, H., & Gao, Y . (2023). Research on customer lifetime
value based on machine learning algorithms and customer rela -
tionship management analysis model. Heliyon, 9.
Umezurike, S., Akinrinoye, O., Kufile, O., Onifade, A., Otokiti, B., &
Ejike, O. (2025). Predictive analytics for customer lifetime value
in subscription-based digital service platforms . International
Journal of Social Science Exceptional Research.
Valendin, J., Reutterer, T., Platzer, M., & Kalcher, K. (2022). Customer
base analysis with recurrent neural networks. International Jour-
nal of Research in Marketing.
Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez,
A. N., Kaiser, L., & Polosukhin, I. (2017). Attention is all you
need. Advances in Neural Information Processing Systems , 30,
5998–6008.
Venkatesan, R., & Kumar, V . (2004). A customer lifetime value frame-
work for customer selection and resource allocation strategy.
Journal of Marketing, 68(4), 106–125.
Venkatesan, R., Kumar, V ., & Bohling, T. (2007). Optimal customer
relationship management using Bayesian decision theory:
An application for customer selection. Journal of Marketing
Research, 44(4), 579–594.
Zhang, X., Kumar, V ., & Cosguner, K. (2017). Dynamically manag-
ing a profitable email marketing program. Journal of Marketing
Research, 54(6), 851–866.
Publisher’s note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
