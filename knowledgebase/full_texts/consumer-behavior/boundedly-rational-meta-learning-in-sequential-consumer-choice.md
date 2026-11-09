---
title: Boundedly Rational Meta-Learning in Sequential Consumer Choice
url: https://arxiv.org/abs/2605.16532
category: consumer-behavior
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Mehrzad Khosravi
- Max Kleiman-Weiner
- Hema Yoganarasimhan
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.16532
pages: 94
chars: 202546
fetched_at: '2026-11-08T13:00:40+00:00'
kb_version: 1
---

# Boundedly Rational Meta-Learning in Sequential Consumer Choice

Boundedly Rational Meta-Learning in Sequential Consumer Choice
Mehrzad Khosravi*
University of Washington
Max Kleiman-Weiner
University of Washington
Hema Yoganarasimhan
University of Washington
Abstract
Many consumer decisions involve repeated choices under uncertainty, where experience
in one context may inform decisions in another. For example, experience with a brand in one
market or usage context may shape beliefs about that brand in a new context. We study whether
such cross-context transfer takes the form of meta-learning, in which experience across contexts
updates higher-order beliefs that guide learning in a new context. In a hierarchical laboratory task,
participants choose among airlines across routes and observe noisy binary outcomes. Participants
improve both within and across routes, indicating cross-route knowledge transfer. We compare
human choices with no-transfer, fully integrated meta-learning, and boundedly rational meta
dynamic programming policies, BRMDP(D), where D is the number of hyper-posterior draws
used to approximate integration. Trial-by-trial likelihood comparisons show that low-D policies,
especially BRMDP(1), best predict participant choices. The results suggest that consumers
transfer information across contexts using coarse representations of higher-order uncertainty.
Keywords:consumer learning, meta-learning, Bayesian learning, bounded rationality, cognitive science,
sequential decision-making, dynamic programming
*We are grateful to the participants of the 2025 INFORMS Marketing Science Conference, the 2025 Conference on AI, ML, and
Business Analytics, the 2026 Haring Symposium, the thirteenth triennial choice symposium 2026, and the University of Washington
marketing seminar for helpful feedback and comments, which have significantly improved this paper. We also thank Cheng-Yu
Hung for his thoughtful discussion notes at the 2026 Haring Symposium. Please address all correspondence to: mehrzad@uw.edu,
maxkw@uw.edu, and hemay@uw.edu.
arXiv:2605.16532v2  [cs.LG]  21 Aug 2026

1 Introduction
1.1 Sequential Decision-Making and Meta-Learning
Many consumer decisions are repeated choices under uncertainty rather than isolated one-shot decisions.
For example, households choose among brands or providers across purchase occasions, observe stochastic
outcomes, and balance exploiting the current best option with learning through exploration. This exploration–
exploitation trade-off is central in classic models of consumer learning and dynamic choice (Ching et al.,
2017; Hutchinson and Eisenstein, 2008). Yet in many markets, the relevant learning sequence does not restart
when a consumer enters a new context. The same brand may reappear in a new category, channel, usage
occasion, or location, and the consumer must decide how much prior experience should carry over. In these
settings, experience in one context can become informative in another, especially when direct experience in
the new context is still limited.
Consider the example of a traveler who chooses among several airlines for repeated trips on a route
(Meyer and Shi, 1995). Over time, they learn which airline performs better on that route. When they travel to
a new destination, however, they face a related decision problem: the same airlines are available, but their
performance may differ on the new route. A natural question is whether they start from scratch—treating the
new route as unrelated—or leverage past experience to form a better initial belief about each airline. Similar
forms of knowledge-transfer arise when consumers evaluate brand extensions or related products. In such
cases, experience with one product can shape beliefs about the brand and influence expectations in a new
category (Wernerfelt, 1988).
To formalize these ideas, we consider two forms of learning. The first iswithin-context learning, in which
consumers update beliefs about alternatives using feedback from the current route, product category, or usage
context. The second iscross-context learning, in which consumers use experience from prior contexts to
inform beliefs and decisions in a new but related context. We focus on a particular form of cross-context
learning—meta-learning—in which experience across contexts is used to learn higher-order regularities that
shape beliefs in a new context. In the airline example, within-context learning corresponds to discovering
which airline performs well on the current route, while meta-learning corresponds to using experience from
earlier routes to learn about the airline-level distribution that generates route-specific performance.
The central question is therefore not just whether consumers transfer information across contexts, but
howthey do so. One possibility is that each new context is treated as independent, with consumers relying

solely on within-context learning. Another is that consumers act as fully integrated Bayesian meta-learners,
carrying all prior uncertainty into the next context and using it in forward-looking planning. A third possibility
lies between these extremes: consumers may transfer brand-level information, but only through coarse or
simplified summaries of prior experience. This paper distinguishes among these possibilities.
These distinctions matter for measurement, theory, and managerial decision-making. Yet despite extensive
work on consumer learning and sequential decision-making (see §2), we still know relatively little about how
consumers transfer knowledge across contexts when feedback is noisy, experience is sparse, and horizons are
short. In particular, we lack evidence on whether cross-context transfer resembles fully integrated Bayesian
meta-learning or a cognitively simpler approximation.
1.2 Research Agenda and Challenges
We address these gaps by developing a framework that compares human behavior with algorithmic bench-
marks in an environment that creates structured opportunities for meta-learning. Our research agenda is
organized around three questions. First, do consumers transfer knowledge acquired in one context to an-
other when learning is based on sparse, stochastic feedback? Second, if consumers do transfer knowledge,
how closely does their behavior resemble an optimal meta-learning policy that fully exploits cross-context
structure? Third, if behavior departs from this optimum, which boundedly rational model best captures the
observed dynamics and the conditions under which transfer is stronger or weaker?
Answering these questions requires overcoming four challenges.
• The first isdesign: we need an experimental environment that is sufficiently realistic to capture key
features of consumer choice—repeated decisions, noisy outcomes, and brand regularities across contexts—
while remaining controlled enough to isolate cross-context or meta learning. In particular, the environment
must allow consumers to learn within a context and then encounter a new context in which the same
alternatives reappear.
• The second isdiagnosis: before estimating formal models, we need reduced-form evidence that separates
improvement within a context from improvement across contexts. Such evidence can establish whether
participants carry information forward to later contexts.
• The third ismodeling: meta-learning requires integrating higher-order uncertainty across contexts, which
can make a fully integrated dynamic program computationally demanding even in small problems. Thus,
a useful model class must include a no-transfer benchmark as well as meta-learning policies that vary in

how finely they integrate prior uncertainty.
• The fourth iscomparison: we need a formal comparison framework that evaluates competing transfer
mechanisms on the same decision histories and information sets, so that cross-context learning can be
distinguished from within-context learning, task familiarity, and generic decision noise.
1.3 Our Approach and Findings
To address these four challenges, we develop a four-part pipeline that mirrors this structure: a hierarchical
laboratory environment that creates controlled opportunities for meta-learning; reduced-form behavioral
diagnostics that document within-route learning and cross-route transfer; dynamic-programming-based policy
classes that formalize no transfer, fully integrated transfer, and boundedly rational transfer; and a trial-by-trial
likelihood framework that compares these mechanisms on the same decision histories.
The laboratory environment is an interactive, incentive-aligned airline choice task. Participants choose
among three fictitious airlines over a sequence of routes, with multiple flights on each route. Outcomes are
binary (on-timevs.delayed), as in a Bernoulli finite-horizon multi-armed bandit. The key design feature
is hierarchical structure: each airline has a latent brand-level distribution over route-specific performance.
Thus, routes are neither identical nor unrelated. Experience on one route can inform beliefs on later routes,
allowing us to study within-route learning and cross-route knowledge transfer in a controlled setting, while
the hierarchical structure creates scope for meta-learning.
The reduced-form evidence is consistent with both within-route as well as across-route meta-learning.
Participants not only improve within routes as they accumulate direct experience, but they also improve
across routes: they start with better airlines in later routes, choose the best-performing airline more often
on later routes, and their pseudo-regret declines across routes. These patterns suggest that participants do
not treat each new route as a fresh learning problem. They appear to carry forward information from earlier
routes and use it to make better initial decisions in later ones.
These reduced-form patterns provide evidence of cross-context transfer, but they do not distinguish
among the different explanations for the observed improvement. Similar aggregate patterns could arise
because participants become more familiar with the task, because they transfer information across routes in a
fully integrated Bayesian manner, or because they transfer information more coarsely using an approximate
representation of prior experience. Distinguishing among these explanations requires a common framework
that maps each candidate learning process into sequential choices.

We therefore develop three dynamic-programming-based policy classes. The baseline Dynamic Pro-
gramming (DP) policy is Bayes-optimalwithin a routeunder our Bernoulli–Beta model, but treats routes
as independent and allows no cross-route knowledge transfer. The Meta Dynamic Programming (MetaDP)
policy is the fully integrated Bayesian benchmark: it updates beliefs across routes and carries the resulting
prior uncertainty into within-route dynamic planning. Finally, we introduce Boundedly Rational Meta
Dynamic Programming policies, denoted BRMDP(D), which approximate full meta-learning by representing
the hyper-posterior with D draws. Small values of D correspond to coarse integration of prior uncertainty,
while larger values approach the fully integrated MetaDP benchmark. This formulation is motivated by the
resource-rationality perspective in cognitive science, which interprets apparent suboptimality as the efficient
use of limited computational resources (Bhui et al., 2021; Lieder and Griffiths, 2020).
We then compare these policies with human behavior using a trial-by-trial likelihood framework. Follow-
ing model comparison methods from sequential choice research (Daw et al., 2011), we evaluate each policy on
the same observed decision histories. We compute participant-level likelihoods for DP and MetaDP directly
and develop a Monte Carlo likelihood estimator for BRMDP(D), which integrates over the latent internal
draws implied by the boundedly rational policy. This common likelihood framework allows us to isolate the
incremental explanatory power of cross-route transfer and to ask whether transfer is best characterized as
absent, fully integrated, or boundedly rational.
The likelihood results favor boundedly rational meta-learning. Low- D specifications, especially
BRMDP(1), fit the choice data better than both the no-transfer DP benchmark and the fully integrated
MetaDP benchmark. Thus, the data reject both extremes. Participants do not behave as if they ignore
cross-route information, but they also do not behave like fully integrated Bayesian meta-planners. Instead,
they appear to transfer knowledge across routes using a coarse representation of prior uncertainty. As D
increases and BRMDP(D) approaches MetaDP, model fit deteriorates and the policy must rely on more
decision noise to resemble human behavior. We also compare BRMDP(1) with simpler knowledge-transfer
policies that carry airline-specific information across routes without learning higher-order beliefs;BRMDP(1)
continues to fit choices better than these benchmarks. Robustness checks across experimental environments,
alternative priors, shorter planning horizons, and softmax choice rules confirm the same qualitative
conclusion.

1.4 Contributions and Implications
The paper makes three main contributions. Substantively, it not only shows that consumers meta-learn, but
also provides evidence onhowthey do so. We study the cross-context information transfer process in a
dynamic setting where consumers repeatedly face exploration–exploitation trade-offs, receive sparse and
stochastic feedback, and must decide how much experience from one context should inform choices in the
next. The main substantive finding is that meta-learning is present but approximate: among the policies
we consider, consumer choices are better described by a policy that carries forward brand-level regularities
across adjacent contexts, but does so through a coarse representation of prior uncertainty rather than full
Bayesian integration.
Methodologically, to our knowledge, this is the first paper to introduce and empirically test a MetaDP
model and a boundedly rational BRMDP(D) model of consumer meta-learning in sequential choice. The
MetaDP model provides a fully integrated Bayesian benchmark that combines cross-context belief updating
with finite-horizon dynamic programming. The BRMDP(D) model provides a tractable boundedly rational
alternative that limits the integration of prior uncertainty through a small number of hyper-posterior draws.
We also develop a likelihood-based comparison framework that evaluates DP, MetaDP, andBRMDP(D) on
the same observed histories, allowing us to test whether consumers behave like no-transfer learners, fully
integrated meta-learners, or boundedly rational meta-learners.
Our results have implications for both research and practice. For researchers, the implication is that
cross-context learning should not be treated as a binary modeling choice between no transfer and full Bayesian
integration. Models that match aggregate learning patterns can still imply the wrong underlying mechanism
if they ignore how consumers represent and use transferred uncertainty. Our framework provides a way to
test whether cross-context transfer is absent and, when it is present, whether it is better described by full or
approximate meta-learning. This matters for empirical work on consumer learning, brand spillovers, dynamic
demand, and counterfactual policy analysis.
For managers, the results imply that early experiences can shape downstream demand through transferable
brand-level beliefs. But managers should not assume that consumers either ignore prior contexts or integrate
all prior uncertainty fully. When behavior is closer to BRMDP(1), demand in a new context is better
viewed as arising from a mixture of consumers with coarse transferred priors rather than from a single
representative consumer with one integrated posterior. This matters for pricing, promotion, trial, and route-

entry interventions: a no-transfer model can be too conservative after favorable early experience, while a
fully integrated model can miss profitable targeted interventions by averaging away coarse heterogeneity in
consumer priors.
The remainder of this paper is organized as follows. In §2, we review related literature. In §3, we
define the hierarchical Bernoulli–Beta environment and describe the experimental task. In §4, we present
reduced-form evidence of meta-learning through best-airline selection and pseudo-regret. In §5, we introduce
the DP, MetaDP, and BRMDP policy classes. In§6, we present the likelihood-based comparison framework
and empirical model comparisons. In §7, we discuss managerial implications and stylized counterfactuals,
and conclude in§8.
2 Related Literature
Our research sits at the intersection of several related literatures. Within marketing and economics, it relates
most directly to three streams of work: cross-category or cross-context belief transfer, structural models of
sequential consumer learning under uncertainty, and boundedly rational dynamic choice. More broadly, it
also connects to two strands of cognitive science research: hierarchical Bayesian learning and boundedly
rational or resource-rational accounts of decision-making. Below, we discuss each of these literatures and
how our work contributes to them.
Marketing research has long recognized that experience with a brand in one category can shape beliefs
and choices in another. In the umbrella-branding and spillover literature, experience with a brand in one
category affects perceived quality, perceived risk, preferences, and choice in a second category (McCoy
et al., 2022; Montgomery and Wernerfelt, 1992; Wernerfelt, 1988). A series of empirical papers studies
cross-category spillovers and establishes the presence of cross-category learning (Coscelli and Shum, 2004;
Erdem, 1998; Sridhar et al., 2012). The vast majority of these papers consider static settings and do not
account for sequential decision-making or forward-looking behavior, except for (Che et al., 2015). This
literature generally assumes that consumers are Bayesian learners and behave in a fully optimal way when
transferring information from one context to another. It does not testhowconsumers carry information
from one context to another in sequential decision problems with sparse and noisy feedback. Conceptually,
this literature establishes that information can transfer across categories or contexts. Our contribution is to
examine whether experience across contexts is used to learn higher-order structure governing context-specific
performance—a form of transfer we refer to asmeta-learning—and, if so, how consumers integrate the

resulting uncertainty. We model and empirically distinguish among no cross-context transfer, fully integrated
meta-learning, and boundedly rational approximations to meta-learning.
A second relevant stream studies sequential consumer learning under uncertainty within a single context.
Beginning with Erdem and Keane (1996), this literature models brand choice as Bayesian learning in dynamic
discrete-choice settings, often allowing consumers to be forward-looking and to recognize the information
value of experimentation; see Ching et al. (2017) for a review. These models correspond to the no-transfer
DP benchmark in our framework: they capture within-context learning over time, but treat each new context
as starting from the same prior. Relative to this work, our framework adds cross-context belief transfer. We
ask whether information accumulated in one context shapes the priors consumers bring to the next and, if so,
whether that transfer is fully integrated or approximate.
A third stream asks whether consumers actually solve such sequential problems in the fully optimal
manner assumed by standard structural models discussed above.Work in economics, marketing, and decision
research has long noted that dynamic optimization can be descriptively demanding, even in relatively simple
environments (Hutchinson and Meyer, 1994; Meyer and Shi, 1995) and Meyer and Hutchinson (2016) show
that assuming agents behave as if they solve Bellman equations can produce brittle counterfactuals and
misleading managerial implications when the underlying behavioral process is misspecified. A growing
stream of research proposes and tests boundedly rational approximations to dynamic choice, including biased
beliefs and inattention, non-Bayesian belief updating, limited-horizon planning, index-based rules, directed
cognition models, and myopic value-of-information heuristics (Gabaix et al., 2006; Grubb and Osborne, 2015;
Jindal and Aribarg, 2021; Lin et al., 2015; Liu and Ansari, 2020; Tehrani and Ching, 2024; Yang et al., 2015).
While this literature also considers bounded-rational approaches, it has largely focused on approximating the
DP problemwithina single context. The main distinction in our paper is that the boundedness we study lies
in the transfer process across contexts—that is, in how consumers approximate the integration of higher-order
priors across routes or categories—rather than in how they approximate DP within a given context.1
More broadly, our work builds on two strands of cognitive science research. First, modeling learning as
inference over hierarchical Bayesian models (Griffiths et al., 2024). This line of research investigates how
humans update beliefs across multiple knowledge categories to learn from sparse and ambiguous data. Kemp
et al. (2007) show that humans (and even young children) form and updateoverhypotheses, i.e., priors over
priors that enable learning across categories. For instance, if a parent points to the family pet’s face and says
1We note that approximations of DP proposed in this literature can also be embedded within our formulation; see§6.3 for details.

“dog”, the child must consider multiple consistent hypotheses. Is a “dog” the whole animal? Does it refer
to just the face? Or is the name of that specific animal “dog” but other similar animals will have different
names? Children disambiguate these possibilities by learning higher-order priors (i.e., overhypotheses) such
as, “new words are more likely to refer to the whole object and not just a part of the object” so that “dog”
most likely refers to the whole animal (Xu and Tenenbaum, 2007). These hierarchical priors enable humans
to learn new concepts from just a few examples (Tenenbaum et al., 2011). They have also been useful for
building human-like computer vision systems that can quickly learn new visual concepts (Salakhutdinov
et al., 2012).
Cognitive scientists have also used these models to explain how people leverage hierarchical priors in
spatial decision-making. Schulz et al. (2020) conducted laboratory experiments on a spatial multi-armed
bandit where each arm was tied to a letter on a single row of a keyboard. They show that subjects can quickly
exploit the spatial structure in the task and learn linear patterns, e.g., expected rewards increase/decrease
from ‘a’ to ‘;’. These linear patterns helped subjects more efficiently balance exploration and exploitation.
Once subjects have learned that the rewards were aligned linearly across the keys (arms), they could quickly
leverage this knowledge by just checking the relative values of the endpoints (‘a’ and ‘;’) to see whether
rewards increase or decrease along the row of the keyboard and then exploit from there. This provides
experimental support for the idea that humans employ a form of hierarchical learning in decision-making
under uncertainty. Here, our goal is to build off these basic insights from cognitive science to systematically
test formal models of consumer meta-learning and decision-making that leverage hierarchical priors over
brands and products.
The second related branch of cognitive science to our paper is the study of humans as “bounded-rational”
decision-makers. This literature aims to provide a theory that explains how humans make rational decisions in
some conditions while being biased in others. In this view, bounded-rational analysis models judgments as the
optimal use of limited time, memory, and attention, deriving simple algorithms that trade accuracy for cost,
thereby reconciling near-optimal behavior with classic biases (Lieder and Griffiths, 2020). Evidence comes
from two complementary strands: within-person “wisdom of the crowd,” where averaging a person’s two
independent estimates improves accuracy, revealing probabilistic internal representations; and sampling-based
decisions, where people appear to act from only a few samples of a posterior (Vul and Pashler, 2008; Vul et al.,
2014). Formal analyses show that when samples and deliberation time are costly, using one or a few samples
can maximize long-run reward, reproducing probability matching, speed–accuracy trade-offs, and Hick-law-

like scaling. Complementary information-theoretic accounts treat cognitive effort as an information-capacity
constraint, linking efficient coding and rational inattention to softmax (stochastic) choice, perseveration, and
context-dependent value representations; under these limits, “noise” and reference dependence emerge as
rational adaptations (Bhui et al., 2021). Our study contributes to this literature by providing a framework for
testing bounded rationality in human knowledge transfer across a sequential decision-making context.
Taken together, our contribution is not simply to add another dynamic choice model. Rather, we:
(1) present a methodological framework that integrates cross-context spillovers, sequential exploration-
exploitation, and bounded rationality in a single framework, and (2) we compare no-transfer, fully integrated,
and boundedly rational transfer models on common information sets and trial-by-trial choice data from a real
experiment. This lets us speak directly to whether consumers meta-learn across contexts and whether that
meta-learning is fully optimal or only approximate.
3 Model Environment and Experimental Task
We now define the decision environment we study and describe how we implement it in the laboratory.
Because our focus is meta-learning, we need an environment that can support both learning within a context
and knowledge transfer across related contexts, with higher-order structure linking those contexts. To that
end, we build on the airline choice problem in the seminal work by Meyer and Shi (1995), which considers
a setting in which a consumer makes a sequence of choices about which airline brand to fly with on a
single route. This setting has two key advantages. First, it has been shown to work well in studies with
real participants because it is simple enough for subjects to understand and complete repeatedly. Second,
the setup is quite flexible. While their work only considers single-route settings, we can easily extend the
environment to multi-route scenarios.
3.1 Single-Route Decision Problem
We begin with the consumer’s problem on a single route. Consider a consultant based in Seattle who has
recently secured a contract with a client in Dallas, requiring repeated trips on the Seattle–Dallas route.
There are K airlines serving this route, and for each trip the consultant must choose one airline. As a busy
professional, they care about whether their flights are on time.2 At the outset, they have no direct experience
with the airlines on this route, but they can learn from realized outcomes as they accumulate flights.
2For expositional ease, we treat on-time arrivals as the primary quality metric. However, our framework is agnostic about the quality
metric used; one could instead use comfort or a broader utility measure that combines multiple service dimensions.

We consider a setting with three fictitious airlines 3—Ascend, Summit, and DynaAir—so that K = 3,
and assume that the consultant takes T = 10 flights on a given route. Figure 1 illustrates the sequential
decision-making process in an environment in which the consultant initially has no experience with any
airline. On each subsequent flight, they face the standard exploration–exploitation trade-off: they canexploit
their current knowledge by choosing the airline that has performed best so far, orexploreby selecting a less
familiar airline in the hope of discovering a better-performing option.
Figure 1: An example of a consultant in a single-route environment, with some experience with Ascend and Summit Airways before
the fifth flight. For the fifth flight, they must decide whether to exploit their current information or explore a less familiar airline.
In this single-route setting, the consultant’s objective is to choose a policy π that maximizes the expected
number of on-time flights over the finite horizon:
Definition 1.We define the consumer’s objective in a single-route setting as
maxπ E
" TX
t=1
γt−1Yt

 π # s.t.Y t ∈ {0, 1}, (1)
whereY t ∈ {0, 1}is the outcome of flightt(1≡on-time) andγ∈(0, 1]is the discount factor.
3.2 Multi-Route Decision Problem
We now extend the problem to multiple routes. After finishing one contract, the consultant may sign another
one in a different city and therefore face a new route.4 The same airlines are available, but their performances
may differ across routes because of variation in scheduling, crew allocation, operational hubs, gate access, or
route-specific conditions. Figure 2 illustrates this extension to a multi-route problem.
If there are M routes and the consultant makesT flights on each route, then the full horizon containsM×T
decisions. As in the single-route setting, outcomes are binary. The key difference is that when the consultant
begins route m, they have already accumulated information from earlier routes, and this information can
3We use fictitious airlines to avoid confounding the experiment with participants’ preexisting beliefs, brand familiarity, loyalty,
or idiosyncratic past experiences with real carriers. Using fictional names helps standardize the initial information set across
participants and ensures that learning in the task reflects experience generated within the experiment rather than outside knowledge.
4This is a common situation for many professionals, especially contract-based workers such as lawyers, construction contractors,
salespeople, or actors.

Figure 2: An example of a multi-route environment. The consultant learns about airline performance on the Seattle–Dallas route and
may use that knowledge to inform decisions on the Seattle–Miami route. In this example, they conclude that Ascend performed best
on the first route but remain uncertain about airline performance on the second.
shape their beliefs about airline performance on the current route.
Let Hm =

(Am,1, ym,1), . . ., (Am,T, ym,T)

be the observed history for route m, We can then define
the start-of-route history object as H1:m−1 = (H1, . . ., Hm−1) for the concatenated history of the previous
routes. Then the problem on route m is the same as in the single-route setting, except that it is conditioned on
H1:m−1. Thus, the consultant’s objective is to choose policyπ m on route m as follows.
Definition 2.We define the consultant’s objective on routemin the multi-route setting as
maxπm E
" TX
t=1
γt−1Ym,t

 H1:m−1,π m # s.t.Y m,t ∈ {0, 1}, (2)
whereY m,t is the outcome of flightton routem.
This formulation creates scope for meta-learning. Experience on earlier routes may not only improve
decisions within those routes, but also shape the beliefs the consultant brings to a new route and thereby
improve their choices on later routes.
3.3 Hierarchical Environment
We now formalize the environment that generates outcomes. In the single-route case, each airline would have
one unknown on-time rate for that route. In the multi-route case, however, each airline-route pair has its
own route-specific on-time rate, and these route-specific rates are themselves related through a higher-level
airline-specific distribution.
We model the true on-time rate of airlinek on route m, denoted by θ∗ m,k, as a draw from an airline-specific
Beta distribution. These airline-level Beta distributions capture the idea that some airlines tend to be better

than others across routes, even though route-specific performance still varies stochastically. The consumer
does not observe the underlying parameters of these airline-level distributions. They only observe the realized
outcomes of the flights they take.
Figure 3: Graphical representation of the hierarchical Bayesian environment. Airline k’s on-time rate on route m, denoted θ∗ m,k, is
drawn from an airline-specific Beta(α∗ k, β∗ k ) distribution. These Beta distributions and route-level on-time rates are properties of the
environment and are not observable to the consumer. The only observable component is the realized outcome of each chosen flight.
Figure 3 provides a graphical representation of this hierarchical structure. Formally, we define the
environment through the following hierarchical generative process (Koller and Friedman, 2009):
• Stage 1: For each route m, draw the true on-time rate of airlinek from an airline-specific Beta distribution:
θ∗ m,k ∼Beta(α ∗ k,β ∗ k),∀k∈ {1,. . ., K},∀m∈ {1,. . ., M}, (3)
where M is the number of routes.
• Stage 2: Let Am,t denote the airline chosen on route m, flight t. Conditional on the chosen airline, draw
the realized outcome from a Bernoulli distribution with meanθ ∗ m,k:
Ym,t |A m,t = k∼Bernoulli(θ ∗ m,k), Y m,t ∈ {0, 1}. (4)
Throughout the paper, we use uppercase Yt and Ym,t to denote outcome random variables, and lowercase
yt and ym,t to denote their realizations.
This hierarchical structure is central to the paper. It ensures that routes are neither identical nor completely
unrelated. Because route-specific performances are drawn from stable airline-level distributions, experience
on one route can inform future routes. That is exactly what creates scope for meta-learning, where a
participant can use experience from earlier routes to infer the airline-level distributions governing route-
specific performance. We list all the notation we used so far in Table 1 for convenience.

Table 1: Notation for the problem definition, model environment, and experimental task.
Notation Definition
k∈ {1,. . ., K}Airline index
m∈ {1,. . ., M}Route index
t∈ {1,. . ., T}Flight index within a route
K Number of airlines
M Number of routes
T Number of flights per route
γDiscount factor applied to future payoffs within a route
θ∗ m,k True on-time rate of airline k on route m
(α∗ k,β ∗ k ) Environment’s true Beta parameters for airline k across routes
At Airline chosen at flight t within a route
Am,t Airline chosen at flight t on route m
Yt Outcome random variable at flight t in the single-route setting
Ym,t Outcome random variable at flight t on route m
yt Realized outcome at flight t in the single-route setting
ym,t Realized outcome at flight t on route m
π,π m Decision policy in the single-route problem (π) and on route m in the multi-route problem (πm)
H1:m−1 History available at the beginning of route m consisting of past actions and realized outcomes
from routes 1,. . ., m−1
3.4 Experimental Task
We implement the hierarchical learning environment in an interactive, web-based sequential decision task
framed as repeated airline choice across routes. In each round, participants choose among three fictional
airlines—Ascend, Summit, and DynaAir—and then receive immediate binary feedback indicating whether
the selected flight was on time or delayed. Figure 4 illustrates the interface.
Each route constitutes a distinct context. The airline identities remain fixed across routes, but their route-
specific on-time rates vary from one route to the next according to the hierarchical environment described in
§3.3. The interface displays the three airline options and provides immediate feedback after each choice. It
also includes a minimal progress summary to keep incentives transparent, while avoiding the presentation
of explicit statistical summaries that could substitute for participants’ own learning. Participants could
respond using keyboard shortcuts mapped to the three airlines, consistent with the on-screen prompts. Before
beginning the main task, participants received instructions explaining the choice environment, feedback
structure, and bonus scheme, and they completed a short demonstration to familiarize themselves with the
interface; see Web Appendix A for details.
The experiment consists of M = 10 routes, each containing T = 10 flights, for a total of 100 sequential
decisions per participant. We recruited 305 participants through the Prolific platform and compensated
them at an effective rate of approximately $8 per hour. To maintain incentive alignment, we also offered a

(a) Before the participant chooses an airline.
 (b) After the participant chooses Ascend and gets an on-time flight.
Figure 4: Airline choice environment used in the experiments.Route Countrepresents the number of the current route that the
participant is flying on, andFlight Countrepresents the flight number on the current route.Total On-Time Flightsshows the
accumulated number of on-time flights so far.Total Earned Pointsshows the points that the participant has gotten so far over all
flights. Each on-time flight earns 10 points, and each 10 points earns $.005 bonus payment. After each choice, participants receive
immediate binary feedback (on-time vs. delayed) before proceeding to the next flight.
performance-contingent bonus tied directly to realized outcomes: participants earned $.005 for each on-time
flight during the experiment. Because the task involved 100 flight decisions in total, the maximum attainable
bonus was $.50. This payment structure aligned participants’ monetary incentives with the objective of the
decision problem—maximizing the number of on-time flights—while preserving the simple, immediate-
feedback structure of the task. This payment method is common in cognitive science and decision theory
literature, used to make the experiments incentive-aligned (Schulz and Gershman, 2019; Shanks et al., 2002;
Wu et al., 2018).
Throughout the experiment, we record the chosen airlineAm,t, the realized outcomeym,t, and the response
time for each flight t on route m. In addition, because the task is generated from the hierarchical environment
in §3.3, we retain the latent route-specific on-time rates {θ∗ m,k}K k=1 used to generate outcomes. Participants
do not observe these latent rates, but we use them to compute benchmark performance measures in the
subsequent analysis.
3.5 Experimental Parameters
We parameterize each airline-level Beta distribution by its mean ( µ) and variance ( σ2), because these
quantities are more interpretable than the corresponding (α, β) parameters. For a Beta distribution, there is
a one-to-one mapping between (α, β) and (µ, σ2), given by µ = α α+β and σ2 = αβ (α+β)2(α+β+1) . The means

determine the airlines’ typical on-time performance across routes, while the variance determines how much
route-specific performance fluctuates around those means. We use subscripts L, M, and H to denote the
airlines with the lowest, middle, and highest overall performance, respectively.
Table 2 reports the experimental parameters and the number of participants assigned to each condition.
We present the actual empirical mean and variance that the participants experienced in Web Appendix G.
Low Var. High Var.
Far Means µL = .2,µ M = .5,µ H = .8,σ 2 = .02 (N = 76) µL = .2,µ M = .5,µ H = .8,σ 2 = .04 (N = 76)
Close Means µL = .4,µ M = .6,µ H = .8,σ 2 = .02 (N = 76) µL = .4,µ M = .6,µ H = .8,σ 2 = .04 (N = 77)
Table 2: Three-airline experiment parameters. Means (µL, µM, µH) define the airlines’ typical across-route on-time rates, and σ2
governs across-route variability in those rates through the airline-level Beta distributions.
The experiment follows a 2× 2 design that varies two features of the environment: the separation between
airline means and the amount of across-route variance. This yields four conditions: (1) Far Means with Low
Variance, (2) Far Means with High Variance, (3) Close Means with Low Variance, and (4) Close Means with
High Variance.
These two dimensions map naturally to different aspects of learning. Mean separation primarily shapes
within-route learning. When the airline means are farther apart, the airlines tend to be more distinguishable
within a given route, so participants can identify the better-performing airline with fewer observations. When
the means are closer together, the route-specific on-time rates of the airlines are more similar, making
feedback less diagnostic and within-route learning slower and noisier.
Variance primarily shapes cross-route learning. When variance is low, each airline’s route-specific
performance remains relatively stable around its overall mean, so experience from earlier routes provides a
useful guide for later routes. This makes it easier for participants to infer persistent differences across airlines
and transfer that knowledge across contexts. When variance is high, airline performance fluctuates more
across routes, reducing the predictive value of prior experience from earlier routes and weakening the scope
for cross-route transfer.
Taken together, these manipulations determine how informative the environment is for both learning
within a route and generalizing across routes. The Far Means–Low Variance condition provides the cleanest
environment for learning, because airlines are easier to distinguish within routes and their relative performance
is more stable across routes. By contrast, the Close Means–High Variance condition is the most difficult,

because the airlines are both harder to distinguish within a route and less predictable across routes. This
design, therefore, allows us to examine not only whether consumers meta-learn but also whether the strength
of such learning depends on how informative the environment is.
4 Behavioral Evidence of Meta-Learning
We now examine the main behavioral patterns in the experiment. The central empirical question is whether
participants exhibit only within-route learning or whether they also transfer knowledge across routes. As
discussed above, the experimental design allows for both types of learning. Within a route, participants
can learn about the route-specific performance of the three airlines from realized outcomes. Across routes,
participants may infer more general regularities about the airlines and use those regularities to improve
decisions on later routes.
To study these patterns, we use best-airline selection and pseudo-regret as our main performance measures.
Best-airline selection captures whether participants pick the best airline for any given flight. Pseudo-regret
complements this measure by capturing the expected reward loss relative to the best airline on a given route,
and is a standard performance metric in the stochastic bandit literature (Auer et al., 2002; Bubeck et al., 2012;
Lai and Robbins, 1985; Lattimore and Szepesv´ari, 2020). In our setting, focusing on the best-airline selection
and theexpectedreward loss are important because flight outcomes are stochastic. Even when a participant
chooses the better airline on a route, the realized flight may still be delayed, and even an inferior airline
may occasionally arrive on time. A performance measure based directly on realized outcomes, therefore,
combines decision quality with idiosyncratic outcome noise. Instead, the two measures we use place greater
emphasis on the quality of the choices.
Best-airline selection.Let Am,t denote the airline chosen on flight t of route m, and let θ∗ m,k denote the true
on-time rate of airline k on route m. We define the best-airline selection as:
Ibest m,t =1{A m,t = argmax k θ∗ m,k}, (5)
which equals 1 if the participant chooses the airline with the highest on-time rate on that route, and 0 otherwise.
We also denote the total number of times that the participant chooses the best airline on route m as Ibestm :
Ibest m =
TX
t=1
Ibest m,t . (6)
This metric measures the participant’s overall success in finding the best airline on each route.

Pseudo-regret.We define flight-wise pseudo-regret, rm,t, as the difference between the highest true on-time
rate on route m and the true on-time rate of the airline chosen at flight t on that route:
rm,t = ¯θ∗ m −θ ∗ m,Am,t, where ¯θ∗ m = max k θ∗ m,k (7)
is the highest true on-time rate among the airlines on route m. This quantity measures the expected
performance loss from the participant’s choice relative to the best available airline on that route. It equals
zero when the participant selects an optimal airline and is positive otherwise.
We then aggregate flight-wise pseudo-regret within each route to obtain route-level pseudo-regret:
Rm =
TX
t=1
rm,t =
TX
t=1
¯θ∗ m −θ ∗ m,Am,t  . (8)
This measure summarizes how much expected performance is lost over the full sequence of decisions on
route m. Because the experimental environment records the latent route-specific on-time rates for all airlines,
both rm,t and Rm are directly computable for every participant and route.
These metrics provide a useful behavioral benchmark for distinguishing within-route learning from meta-
learning across routes. If participants learn only within a route, then best-airline selection should increase, and
pseudo-regret should decline over flights within that route, but there should be little systematic improvement
from earlier routes to later ones. By contrast, if participants transfer knowledge across routes, then later
routes should begin with higher best-airline selection and lower pseudo-regret. Combined with within-route
learning, this should result in better overall visible performance on later routes. Thus, within-route changes
in best-airline selection and pseudo-regret reflect route-specific learning, whereas across-route shifts are
diagnostic of meta-learning.
4.1 Best-Airline Selection and Regret Patterns
We begin with the most direct descriptive evidence. Figure 5 plots the mean best-airline selection per flight
across all routes for the four experimental conditions. Each line corresponds to a distinct route, with earlier
routes shown in lighter shades. If participants improve only within a route, the lines should slope upward
within each route but remain broadly similar across routes. If participants meta-learn across routes, later-route
lines should shift upward relative to earlier-route lines. Similarly, Figure 6 plots the mean pseudo-regret per
flight across routes for all the experimental conditions. In the pseudo-regret plots, we consider downward-
sloping lines as evidence of within-route learning, and later routes lying below earlier ones as evidence of

meta-learning.
0.4
0.6
0.8
Far Means - Low Var.
Route 10
Route 1
Far Means - High Var.
1 4 7 10
0.4
0.6
0.8
Close Means - Low Var.
1 4 7 10
Close Means - High Var.
Flight
Mean best-airline selection
Figure 5: Participants’ mean best-airline selection over flights for different routes. Later routes generally lie above earlier ones,
indicating improvement across routes in addition to the within-route improvement in best-airline selection.
0.1
0.2
0.3
Far Means - Low Var.
Route 10
Route 1
Far Means - High Var.
1 4 7 10
0.1
0.2
0.3
Close Means - Low Var.
1 4 7 10
Close Means - High Var.
Flight
Mean regret
Figure 6: Participants’ mean pseudo-regret over flights for different routes. Each line represents a distinct route, and earlier routes are
in lighter shades. Later routes generally lie below earlier ones, indicating improvement across routes in addition to the within-route
decline in regret.
Figures 5 and 6 reveal two clear patterns. First, the best-airline selection tends to increase, and pseudo-
regret tends to decline within routes. This indicates that participants learn from realized outcomes and
improve their choices over the ten flights of a given route. Second, both metrics also improve across routes.
Accordingly, later routes generally start from a better baseline and remain above the earlier ones in the
best-airline selection plots, and below the initial routes in the pseudo-regret plots, especially in the Far Means
environments. This improvement suggests that participants do not treat each new route as an entirely fresh
problem. Instead, they appear to carry information from previous routes into subsequent ones.

This pattern provides reduced-form evidence of meta-learning in our setting. Participants are not merely
learning which airline performs best on the current route; they are also learning something more general that
helps them make better choices when a new route begins. At the same time, the across-route improvement is
not identical across experimental conditions. It is visually strongest in environments where airline differences
are easier to distinguish and weaker in more difficult environments where means are closer together, and
across-route variance is higher.
4.2 Route-Level Evidence on Best-Airline Selection and Pseudo-Regret
We now formalize the descriptive evidence from the previous section using route-level regressions of best-
airline selection and pseudo-regret on route number. This route-level analysis complements the flight-level
plots by testing whether participants perform better on later routes than on earlier ones, which is the central
reduced-form implication of meta-learning.
Let Zi,m denote the route-level outcome of interest (Ibest i,m or Ri,m) for participant i on route m. We estimate
Zi,m =α+λm +ω ⊤ m×1 experiment,i  +ξ i + ui,m, (9)
where m is the route number,1 experiment,i is a 3-vector of condition dummies for the non-baseline environ-
ments, ξi denotes participant fixed effects, and ui,m is an idiosyncratic error term. The omitted condition is
Far Means–Low Var., so the coefficient onm captures the across-route performance trend in that baseline
condition, while the interaction terms capture how that trend differs in the other three environments. Par-
ticipant fixed effects absorb time-invariant heterogeneity across participants, so identification comes from
within-participant changes in performance over routes.
Best-Airline Selection Pseudo-Regret
Coefficient Std. Errorp-value Coefficient Std. Errorp-value
Route number (m) .294 (.040)<.001−.129 (.017)<.001
Far Means–High Var.×m−.113 (.059) .055 .043 (.024) .082
Close Means–Low Var.×m−.205 (.058)<.001 .099 (.021)<.001
Close Means–High Var.×m−.167 (.054) .002 .092 (.023)<.001
Constant 5.002 (.198)<.001 1.403 (.083)<.001
Participant fixed effects✓ ✓
R2 (within) .041 .052
Observations 3,050 3,050
Participants (clusters) 305 305
Table 3: Regression results for route-level best-airline selection and pseudo-regret over route number with condition-specific slopes
(baseline condition: Far Means–Low Var.). Participant-clustered standard errors are in parentheses. Reportedp-values are from
two-sided cluster-robust Wald tests.

Table 3 reports the results. Two findings stand out. First, performance improves across routes in the
baseline condition. The coefficient on route number is positive for best-airline selection (.294, SE = .040,
p < .001) and negative for pseudo-regret ( −.129, SE = .017,p < .001). This indicates that participants
perform better on later routes than on earlier ones. Second, the rate of improvement depends on the
environment. Relative to the Far Means–Low Var. condition, improvement is significantly weaker in the
Close Means–Low Var. and Close Means–High Var. conditions, as indicated by the negative and positive
interaction coefficients in the best-airline-selection and pseudo-regret specification, respectively. By contrast,
the Far Means–High Var. interaction is smaller and not statistically distinguishable from the baseline slope.
Taken together, these results show that participants do not treat each route as an independent learning
problem. Performance improves not only within routes but also across routes, consistent with participants
carrying information from earlier to later routes. The strength of this cross-route improvement depends on
the informativeness of the environment: it is strongest when airlines are easier to distinguish on average and
weaker when the underlying differences are smaller.
So far, we have analyzed best-airline selection and pseudo-regret, both of which rely on the latent on-time
rates θ∗ m,k. One concern is that these measures evaluate improvement relative to environmental properties
that participants never observe, rather than using information available to the participants themselves. In
Web Appendix E.1, we address this concern using only each participant’s observed choices and outcomes,
focusing on the first choice on each route. We show that participants are more likely to choose an airline
whose posterior mean, constructed from their own earlier-route experience, is higher. This pattern provides
additional evidence of cross-route knowledge transfer and is consistent with meta-learning.
Overall, these reduced-form patterns are consistent with cross-route belief transfer, but they do not
distinguish among the mechanisms that could generate it. In particular, they do not tell us whether participants
behave like fully optimal meta-learners or according to a boundedly rational approximation. Indeed, similar
choices can be generated by very different cognitive processes. Structural work shows that distinguishing
among these processes requires a fully specified model of how consumers form, update, and use beliefs over
time (Ching et al., 2013; Crawford and Shum, 2005; Erdem and Keane, 1996; Hutchinson and Eisenstein,
2008). Furthermore, recent work in consumer behavior argues for explicit Bayesian formulations of belief
dynamics in experimental and survey data (Hofacker et al., 2024). Aggregate statistics are useful as a
diagnostic, but they are not sufficient to identify the underlying computations that govern transfer learning in
choice.

Second, the choice of behavioral model has direct consequences for the managerial counterfactuals one
wants to draw. Meyer and Hutchinson (2016) argue that small differences in how learning is modeled can
produce qualitatively different policy implications. When a firm carries a misspecified learning model, the
resulting beliefs and the policies derived from them can be systematically biased (Bohren and Hauser, 2025).
In our setting, the gap between full integration of cross-route uncertainty (MetaDP) and a coarse, boundedly
rational version of the same logic (BRMDP) maps to different choices in a managerial decision-making
problem (see §7). A model that matches the reduced-form but misses the underlying mechanism can make
the wrong decisions even if it captures the broad direction of learning. We therefore turn to the formal
policy classes—DP, MetaDP, and BRMDP—and compare them to the observed choice sequences in a
likelihood-based framework.
5 Dynamic Programming Models of Learning and Meta-Learning
We model meta-learning as cross-route knowledge transfer in which experience across routes updates
beliefs about the higher-order distributions that generate route-specific performance. To characterize this
process, we introduce three dynamic-programming-based policy classes that differ in whether they transfer
information across routes and, among the meta-learning policies, in how fully they integrate higher-order
uncertainty. The baseline dynamic programming policy (DP) is Bayes-optimal within a route but treats routes
independently, so each route begins from the same uninformative priors. The meta dynamic programming
policy (MetaDP) updates higher-order beliefs across routes and fully integrates the resulting uncertainty into
within-route dynamic planning. Finally, the boundedly rational meta dynamic programming policy (BRMDP)
approximates MetaDP by limiting how finely the consumer integrates uncertainty across prior hypotheses.5
We build these policies in steps. We begin with Bayesian updating within a route, which is common
to all three policy classes. We then present the no-transfer DP benchmark. Next, we develop Bayesian
updating across routes and use it to define MetaDP. Finally, we introduce BRMDP as a boundedly rational
approximation to MetaDP. Framing the model family in this way makes clear that the three policies differ not
in the basic information structure of the environment, but in how they use available information and how
much computation they allocate to planning.
For convenience, Table 4 summarizes the core notation for the within-route learning and the baseline DP.
5We introduce a suite of non-meta learning policies in Web Appendices E.8 and E.9 and compare them with our best-performing
meta-learning policy.

Table 4: Notation for within-route Bayesian updating and baseline dynamic programming
Notation Definition
(αk,β k) Prior Beta parameters for airline k in the baseline DP policy
α,βVectors of prior Beta parameters across airlines
ˆαk, ˆβk Posterior Beta parameters for airline k within a route
ˆα, ˆβVectors of posterior Beta parameters across airlines
N+ k, N− k Cumulative numbers of on-time and delayed flights for airline k within a route
N+,N − Vectors of on-time and delayed counts across airlines within a route
N+ k,m, N− k,m Numbers of on-time and delayed flights for airline k on route m
N+m,N −m Vectors of on-time and delayed counts across airlines on route m
Tk,m Number of times airline k is chosen on route m, equal to N+ k,m + N− k,m
ˆθk,t Posterior mean on-time rate of airline k at flight t in the baseline DP policy
ek Unit vector with a 1 in position k and zeros elsewhere
sDPt State in the baseline DP policy: (N+,N −;α,β)
Vϵ(k|s DPt ) Baseline DP action value from choosing airline k at state s DPt under policy noiseϵ
Wϵ(·) Baseline DP state value under policy noiseϵ
πDPϵ (· | ·)ϵ-greedy baseline DP choice rule
5.1 Bayesian Updating within a Route
We begin with Bayesian updating within a route. This is the common building block for all three policy
classes. Because each flight outcome is binary (on-timeversusdelayed), we model outcomes as Bernoulli
and place a Beta prior on each airline’s on-time rate. The Beta prior is conjugate to the Bernoulli likelihood
and therefore yields closed-form posterior updates (Gelman et al., 1995).
Let ( ˆα, ˆβ) denote the current posterior parameter vectors, where ˆα =  ˆα1, . . ., ˆαK  , ˆβ =  ˆβ1, . . ., ˆβK  ,
and ( ˆαk, ˆβk) are the posterior parameters for airline k. These posterior parameters summarize the information
accumulated from past realized outcomes within the route and define the consumer’s current beliefs about
each airline’s on-time rate.
Let N+ k and N− k denote the cumulative numbers of on-time and delayed flights experienced with airline k
up to flight t. Then the posterior mean on-time rate of airline k at time t is
ˆθk,t = ˆαk ˆαk + ˆβk = αk + N+ k αk +β k + N+ k + N− k , (10)
where (αk, βk) are the prior Beta parameters for airlinek. We suppress time subscripts on N+ k, N− k , ˆαk, and ˆβk
because the posterior for airline k depends only on the cumulative number of on-time and delayed outcomes
observed for that airline up to flight t, not on the calendar position of those observations.
To simplify notation, letN + = (N+ 1, . . ., N+ K),N − = (N− 1 , . . ., N− K). For example, if the consumer
chooses airline k and the realized outcome is on time, then N+ k ←N + k + 1, or equivalentlyN + ← N+ +e k,

wheree k is the unit vector with a 1 in the kth position and zeros elsewhere.
At the end of each flight t∈ {1, . . ., T}, suppose the consumer chose airline k. After observing the
realized outcome yt ∈ {0, 1}, they update the posterior accordingly. Because of conjugacy, the posterior
remains in the Beta family after each update. Algorithm 1 summarizes these updating steps. This within-route
updating rule is shared by all the policies considered in the paper.
Algorithm 1Bayesian Updating within a Route (Bernoulli–Beta)
1:Input:current counts (N +,N −) and posterior parameters ( ˆα, ˆβ); action At = k; realized outcome yt ∈ {0, 1}
2:ify t = 1then ▷flight ison-time
3:N + ←N + +e k,N − ←N −
4:(equivalently,ˆα k ←ˆαk + 1, ˆβk ← ˆβk)
5:else ▷flight isdelayed
6:N + ←N +,N − ←N − +e k
7:(equivalently,ˆα k ←ˆαk, ˆβk ← ˆβk + 1)
8:end if
9:Updated posterior mean: ˆθk,t ← ˆαk
ˆαk + ˆβk
5.2 Baseline Dynamic Programming Policies (DP)
We now introduce the baseline dynamic programming policies. These policies provide the no-transfer
benchmark for the paper. They use the Bayesian updating rule from §5.1, but they treat each route as an
independent learning problem. As a result, every new route begins from the same uninformative priors, and
no information is carried over from earlier routes. This benchmark is useful because it isolates what can be
learned from repeated outcomeswithina route alone.
We consider two variants of the baseline DP policy. The first is a deterministic benchmark that always
chooses a value-maximizing airline. The second is a stochastic ϵ-greedy version that assigns most of its
probability to value-maximizing airlines while allowing for uniform choice noise. Because neither policy
transfers information across routes, we suppress the route subscript m throughout this subsection.
State representation.At flight t, the state issDPt = (N+,N −; α, β). Given this state, the posterior parameters
are given by ˆα = α +N +, ˆβ = β +N −, and the flight index is pinned down by ∥N+∥1 + ∥N−∥1 = t− 1.
Because the horizon is finite, the problem is non-stationary through the number of flights remaining.

State transitions.The within-route Bayesian updating rule from §5.1 governs transitions from sDPt to sDP t+1.
After choosing airline k at flight t,
On-time with probability ˆθk,t : (N ′+,N ′−) = (N+ +e k,N −),
Delayed with probability 1− ˆθk,t : (N ′+,N ′−) = (N+,N − +e k).
These transition probabilities apply to all DP variants.
Deterministic DP benchmark.Under the deterministic benchmark, the consumer chooses a value-
maximizing airline at every state. This corresponds to the special case ϵ = 0. The action value from
choosing airline k at state sDPt is
V0(k|s DP t ) = ˆθk,t +γE h W0(sDP t+1)

 sDP t , At = k i , (11)
where ˆθk,t is the posterior mean on-time rate of airline k. Because outcomes are binary, ˆθk,t is also the
expected current-period payoff.
Substituting the state-transition probabilities into Equation (11) yields
V0(k|N +,N −;α,β) = ˆθk,t +γ h ˆθk,t W0(N+ +e k,N −;α,β) +  1− ˆθk,t  W0(N+,N − +e k;α,β) i , (12)
where
W0(N+,N −;α,β) = max k V0(k|N +,N −;α,β) (13)
is the expected value of being in state (N+,N −; α, β). Thus, the deterministic DP benchmark chooses an
airline in arg maxk V0(k|s DPt ), breaking ties uniformly when needed. At the terminal flight, there is no
continuation value, so V0(k|s DP T ) = ˆθk,T.
This policy can be solved using backward induction from t = T to t = 1 and then used to compute the
action values at every feasible state; see Web Appendix B.1 for details of the backward induction algorithm.
Stochastic ϵ-greedy DP policy.Although the deterministic benchmark is a useful normative reference,
it imposes a sharp behavioral implication: at every state, the consumer always selects a value-maximizing
airline, exactly following the policy. Prior work shows that consumers often deviate from exact dynamic
optimization in sequential choice settings. As such, a more natural policy is the ϵ-greedy policy, which
provides a parsimonious stochastic relaxation of the deterministic benchmark (Sutton et al., 1998). In
our behavioral interpretation, ϵ captures value-independent choice noise rather than information-seeking

exploration, which is already accounted for by the continuation value.
Under the ϵ-greedy policy, the consumer assigns total probability 1−ϵ to the set of value-maximizing air-
lines and distributes the remaining probabilityϵ uniformly across all K airlines. At state sDPt = (N+,N −; α, β),
the policy is
πDP ϵ ˜k|N +,N −;α,β  = (1−ϵ) 1
n
˜k∈arg max
k
Vϵ

k|N +,N −;α,β o

arg max k Vϵ  k|N +,N −;α,β 

 + ϵ K. (14)
The first term assigns total probability 1−ϵ to the set of value-maximizing airlines and splits that mass evenly
in case of ties. The second term distributes the choice-noise probability uniformly across all airlines. When
ϵ = 0, the policy collapses to the deterministic DP benchmark. An alternative way to induce stochasticity is to
use a softmax policy (Bhui et al., 2021). We consider this formulation in an extension in Web Appendix E.6
and focus on theϵ−greedy formulation in the main text.
Because future selves follow the same ϵ-greedy rule, the continuation value must average over the action
probabilities induced by that rule. The corresponding state value is
Wϵ

N+,N −;α,β  =E k∼πDPϵ (·|N+,N−;α,β)  Vϵ  k|N +,N −;α,β  . (15)
Substituting Equation (14) gives
Wϵ

N+,N −;α,β  = (1−ϵ) max
k
Vϵ

k|N +,N −;α,β  + ϵ K KX k=1 Vϵ  k|N +,N −;α,β  . (16)
The recursive action value under theϵ-greedy policy is therefore
Vϵ

k|N +,N −;α,β  = ˆθk,t +γ h ˆθk,t Wϵ  N+ +e k,N −;α,β  +  1− ˆθk,t  Wϵ  N+,N − +e k;α,β i . (17)
At the terminal flight,Vϵ

k| N+,N −; α, β  = ˆθk,T, and Wϵ  N+,N −; α, β  = (1−ϵ) maxk ˆθk,T+ ϵ K PK k=1 ˆθk,T.
Backward induction over Equation (17) then yields Vϵ and Wϵ at all feasible states. Setting ϵ = 0 yields the
deterministic benchmark, while ϵ >0 gives the stochastic ϵ-greedy policy. See Web Appendix C.1 for the
DP pseudocode.
5.3 Bayesian Updating across Routes
The baseline DP benchmark treats every route as a fresh learning problem. We now relax that restriction and
allow the consumer to transfer information across routes. To model meta-learning, we introduce a hyper-
posterior over candidate airline-level prior specifications. Updating this hyper-posterior allows experience on

earlier routes to change beliefs about the distributions that generate route-specific performance.
Two features of our formulation are new relative to prior bandit meta-learning work of Kveton et al.
(2021). First, we keep the posterior update in closed form via Beta–Binomial marginal likelihoods, which
makes it possible to discretize the hyper-posterior coarsely. This discretization is what allows us to define a
one-parameter family of boundedly rational models in §5.5. Second, we use the resulting hyper-posterior as
an input to a finite-horizon dynamic program within each route. We formalize that extension in §5.4. For
now, we focus only on the updating rule itself.
For convenience, Table 5 summarizes the notation used for cross-route learning and the MetaDP policy.
Table 5: Notation for cross-route learning and MetaDP
Notation Definition
(α(j) k ,β (j) k ) Beta prior parameters for airline k under hypothesis P (j)
(α(j),β (j)) Vectors of prior Beta parameters across airlines under hypothesis P (j)
P={P (j)}J j=1 Set of candidate prior hypotheses used for cross-route learning
P∗ The element ofPthat is the true prior in the environment
Q Initial hyper-prior over hypotheses inP
Qm(j) Hyper-posterior weight before route m on hypothesis P (j)
fm(j) Marginal likelihood of route-m outcomes under hypothesis P (j)
ˆθ(j) k,t,m Posterior mean on-time rate of airline k at flight t on route m under hypothesis
P(j)
sMetaDPt,m State in MetaDP at flight t on route m: (N+m,N −m; Qm)
V(j) ϵ (k| ·) Hypothesis-conditioned MetaDP action value under prior hypothesis P (j)
¯Vϵ(k| ·) Integrated MetaDP action value, averaged over hypotheses using Q m
¯Wϵ(·) Integrated MetaDP state value under theϵ-greedy rule
πMetaDPϵ (· | ·)ϵ-greedy MetaDP choice rule
Hypothesis space and hyper-prior.Recall from Equation (3) that at the beginning of each route m, the
environment draws the true on-time rate of airline k, denoted θ∗ m,k, from an airline-specific Beta distribution:
θ∗ m,k ∼Beta(α ∗ k,β ∗ k),∀k∈ {1,. . ., K},∀m∈ {1,. . ., M}.
These route-specific on-time rates are unobserved. However, by the time the consumer reaches route m, they
have accumulated experience from the previous m− 1 routes. To capture cross-route learning, we define two
objects: a finite set of prior hypotheses and a hyper-prior over them.
Let P = {P(j)}J j=1 denote the set of prior hypotheses. Each hypothesis P(j) specifies airline-specific Beta
prior parameters {(α(j) k , β(j) k )}K k=1. Intuitively, P collects the candidate prior specifications that the consumer
regards as plausible across routes. We assume that the environment’s true prior is one element of this class,

denoted P∗ = P(j∗), j∗ ∈ {1, . . ., J}. Because the consumer does not know which hypothesis is P∗, they begin
with a hyper-prior Q1.6 More generally, before route m, their beliefs are summarized by the hyper-posterior
Qm, where
Qm(j) = Pr

P∗ = P(j) | {(N+ k,r, N− k,r)K k=1}m−1 r=1

,
JX
j=1
Qm(j) = 1.
Thus, cross-route learning amounts to updatingQm after each route so that the weight shifts toward hypotheses
that better explain the observed route-level outcomes.
Hyper-posterior update.After route m, the consumer updates the hyper-posterior by Bayes’ rule:
Qm+1(j) = fm(j)·Q m(j) PJ
ℓ=1 fm(ℓ)·Q m(ℓ)
, (18)
where
fm(j) =
KY
k=1
Γ(α(j) k +β (j) k )
Γ(α(j) k )Γ(β (j) k ) ·
Γ(α(j) k + N+ k,m)Γ(β (j) k + N− k,m)
Γ(α(j) k +β (j) k + Tk,m) . (19)
For route m, N+ k,m and N− k,m denote, respectively, the numbers of on-time and delayed flights experienced with
airline k, and Tk,m = N+ k,m + N− k,m is the number of times airline k is chosen on that route. This route-level
evidence term is the Beta–Binomial marginal likelihood induced by Beta–Bernoulli conjugacy.
Equation (18) is Bayes’ rule over the finite hypothesis class P: the next hyper-posterior Qm+1(j) equals
the current weight Qm(j) times how well hypothesis j explains the observed on-time/delay counts. With
Beta–Bernoulli conjugacy, this “fit” reduces to the Beta–Binomial terms (Gamma ratios) in Equation (19).
Hypotheses whose priors place more mass on the observed N+ k,m and N− k,m gain weight, and mismatched
hypotheses lose weight. Over routes, Qm shifts posterior mass toward the true prior P∗. For convenience, let
N+m = (N+ 1,m, . . ., N+ K,m),N −m = (N− 1,m, . . ., N− K,m) denote the vectors of on-time and delayed counts across
all airlines on route m. Algorithm 2 summarizes the resulting cross-route Bayesian updating rule.
Algorithm 2Cross-Route Hyper-Posterior Update
1:Inputs:P={(α (j),β (j))}J j=1, initial hyper-prior Q1
2:form = 1,. . ., Mdo
3:Play route m with a within-route policy and collect counts{N +m,N −m}
4:forj = 1,. . ., Jdo
5:Compute evidence f m(j) using Equation (19)
6:Q m+1(j)←normalized f m(j) Qm(j) (Equation (18))
7:end for
8:end for
6A reasonable choice for this hyper-prior is an uninformative one, which gives equal weights to each prior hypothesis–i.e. Q1(j) =
1/J,∀j∈ {1,. . ., J}.

Illustrative example.A simple two-airline example clarifies these objects. Suppose the consumer is
choosing between Ascend and Summit Airways and considers two hypotheses: j = 1, under which Ascend is
better than Summit, and j = 2, under which Summit is better than Ascend. One possible parameterization
is shown in Table 6. The consumer starts with hyper-prior Q1 = (.5, .5), reflecting equal initial weight on
the two hypotheses. Further, suppose that Ascend is actually better than Summit, and the true airline-level
Beta parameters are (α∗ A, β∗ A) = (3, 1) and (α∗ S, β∗ S) = (2, 1). Consequently, P∗ = P(1), since P(1) contains the
true priors in Table 6. The consumer does not observe this directly. Instead, after each route, they use the
realized flight outcomes to update Qm. As more routes are observed, the hypothesis that better explains the
accumulated outcomes receives increasing weight.
Ascend is Better
(j = 1)
Summit is Better
(j = 2)
α β α β
Ascend 3 1 2 1
Summit 2 1 3 1
Q1(j) .5 .5
Table 6: Example of two prior hypotheses. Here, P(1) =  Beta(3, 1),Beta(2, 1)  encodes the belief that Ascend is better than Summit,
while P(2) =  Beta(2, 1), Beta(3, 1)  encodes the reverse ranking. The consumer starts with hyper-prior Q1 = (.5, .5).
5.4 Meta Dynamic Programming Policy (MetaDP)
We now introduce the first policy class that allows cross-route learning: Meta Dynamic Programming
(MetaDP). This policy combines the hyper-posterior from §5.3 with finite-horizon dynamic programming
within each route. The consumer learns across routes by updating the distribution over prior hypotheses, and
then uses that learned distribution directly in route-level planning.
The construction combines two ideas from separate literatures. Within machine learning, the recent meta-
bandit literature shows how an algorithm can learn priors by maintaining a hyper-posterior over candidate task
priors and using it across tasks (Basu et al., 2021; Guan and Xiong, 2024; Hong et al., 2022; Kveton et al.,
2021; Nabi et al., 2022). However, this literature focuses on algorithmic development and pure performance,
not building models of human consumers. From the dynamic decision-making literature in marketing (and
more broadly), we adopt the Bellman recursion that values current actions partly for the information they
generate and the effect of that information on future choices (Bellman, 1956, 1966; DeGroot, 2005). These
models typically take a single fixed prior as given and do not formalize how that prior itself is learned from

prior experience in related contexts.
MetaDP draws on these two literatures. Its key feature is that it propagates the full hyper-posterior
through the within-route Bellman recursion. Rather than selecting one prior hypothesis and solving the
route conditional on that choice, the consumer evaluates each airline by integrating over all candidate priors,
weighted by their probabilities in the current hyper-posterior. This integrated belief is used to plan over the
remaining horizon. First, prior uncertainty enters both as the route’s initial beliefs and also as the within-route
continuation values that govern exploration and exploitation. Second, MetaDP serves as a rational benchmark.
It is the policy a Bayesian consumer would adopt if they could integrate exactly over the hyper-posterior
at every decision. We will use this benchmark in §5.5 as the reference point against which to define a
one-parameter family of boundedly rational approximations.
Route-level state.At flight t on route m, the MetaDP state is sMetaDPt,m = (N +m,N −m; Qm), whereN +m =
(N+ 1,m, . . ., N+ K,m) andN −m = (N− 1,m, . . ., N− K,m) are the within-route counts of on-time and delayed flights
across airlines. As before, the flight index is pinned down by∥N +m∥1 +∥N −m∥1 = t−1.
The hypothesis set P = {P(j)}J j=1 is fixed across routes and is therefore treated as part of the model
primitive rather than a changing state variable. Because cross-route learning occurs only after the route ends,
the hyper-posterior Qm remains fixed throughout route m; within the route, only the count vectors evolve.
Hypothesis-conditioned action values.For each hypothesis P (j) ∈ P, let
ˆθ(j) k,t,m = α(j) k + N+ k,m α(j) k +β (j) k + N+ k,m + N− k,m ,
denote the posterior mean on-time rate of airline k at flight t on route m under hypothesis j. Conditional on
P(j), the action value from choosing airline k is
V(j) ϵ  k|N + m,N − m, Qm;P  = ˆθ(j) k,t,m
+γ
h
ˆθ(j) k,t,m ¯Wϵ  N+ m +e k,N − m, Qm;P 
+

1− ˆθ(j) k,t,m  ¯Wϵ  N+ m,N − m +e k, Qm;P i .
(20)
The immediate payoff depends on hypothesis j through ˆθ(j) k,t,m. The continuation term, however, uses the
integrated state value ¯Wϵ, because future choices are made using the full hyper-posterior Qm rather than any
single hypothesis.

Integrated action and state values.Because Qm is a discrete distribution over hypotheses and remains
fixed during route m, the consumer evaluates each airline by averaging the hypothesis-conditioned action
values using the weights Qm(j):
¯Vϵ  k|N + m,N − m, Qm;P  = JX
j=1
Qm(j) V(j) ϵ  k|N + m,N − m, Qm;P  . (21)
This integrated action value is the defining feature of MetaDP. Unlike a procedure that would sample a single
prior hypothesis and then optimize conditionally on that draw, MetaDP carries prior uncertainty directly into
the Bellman recursion by averaging across all hypotheses at every state.
At the terminal flight, there is no continuation value, so Equation (21) reduces to
¯Vϵ  k|N + m,N − m, Qm;P  = JX
j=1
Qm(j) ˆθ(j) k,T,m,∥N + m∥1 +∥N − m∥1 = T−1. (22)
Applying theϵ-greedy rule to these integrated action values gives the policy-induced state value:
¯Wϵ  N+ m,N − m, Qm;P  = (1−ϵ) max k ¯Vϵ  k|N + m,N − m, Qm;P  + ϵ K KX k=1 ¯Vϵ  k|N + m,N − m, Qm;P  . (23)
The policy assigns total probability 1 −ϵ to the airlines with the highest integrated action value, while it
distributes the choice-noise probabilityϵuniformly across all airlines. Settingϵ= 0 yields the deterministic
MetaDP benchmark. Equations (20)–(23) are solved by backward induction over t = T, T− 1, . . ., 1 within
route m.
Policy execution across routes.At each within-route state, the consumer chooses an airline using the
ϵ-greedy rule applied to the integrated action values:
˜k∼π MetaDP ϵ  · |N+ m,N − m, Qm;P  , (24)
where
πMetaDP ϵ ˜k|N + m,N − m, Qm;P  = (1−ϵ) 1
n
˜k∈arg max
k
¯Vϵ  k|N +m,N −m, Qm;P o

arg max k ¯Vϵ  k|N +m,N −m, Qm;P 

 + ϵ K. (25)
Thus, within-route learning updates the counts (N +m,N −m), while cross-route learning updates the hyper-
posterior only after the route is completed. After finishing route m, the consumer uses the realized route-level
counts to updateQm to Qm+1 via Algorithm 2, and then solves the next route using the updated hyper-posterior.

See Web Appendix C.2 for the MetaDP pseudocode.
Interpretation.MetaDP is our benchmark for fully integrated meta-learning. The consumer updates a
hyper-posterior across routes and carries that uncertainty into the within-route Bellman recursion. As a result,
experience from earlier routes affects later behavior both through the beliefs with which a new route begins
and through the continuation values that shape forward-looking exploration and exploitation within that route.
This full integration is computationally demanding. Solving MetaDP requires the consumer to maintain and
update the hyper-posterior over prior hypotheses and to propagate that uncertainty through a finite-horizon
dynamic programming problem within each route. This computational burden motivates the next model,
BRMDP, which preserves the logic of cross-route learning while approximating the integration step.
5.5 Boundedly Rational Meta Dynamic Programming (BRMDP)
We now introduce Boundedly Rational Meta Dynamic Programming (BRMDP), a tractable approximation to
MetaDP. BRMDP simplifies the representation of prior uncertainty within the route-level dynamic program
using an approximation of the hyper-prior. Instead of integrating exactly over the full hyper-posteriorQm, the
consumer represents that distribution using a finite number of draws. This formulation is motivated by two
converging lines of cognitive-science evidence. First, in single-context judgment and choice tasks, people
behave as if they use only a small number of samples (often just a single one) from the relevant posterior
rather than the full distribution (Vul et al., 2014). Second, recent work on human planning shows that people
adapt the representational and computational effort they devote to forward planning to the demands of the task.
For example, during decision-making, people prune deep search trees, simplify state representations, and
select planning depths (Callaway et al., 2022; Eluchans et al., 2025; Ho et al., 2023). In both cases, departures
from full Bayesian or DP-optimal computation reflect a cost–benefit trade-off in cognitive resources.
Drawing on these ideas, BRMDP generates a family of policies indexed by the number of hyper-posterior
draws, D. Intuitively, D governs how well the consumer integrates uncertainty over prior hypotheses across
routes. Smaller values of D reduce computational cost but move behavior farther from MetaDP across
routes. Larger values of D yield a closer approximation to MetaDP, but at a higher computational cost.
One clear divergence from the prior cognitive work is that the bounded-resource approximation operates at
themeta-Bayesian level, i.e., over the hyper-posterior rather than the within-task posterior. The empirical
question we take up in §6 is which value of D best describes the way participants actually integrate prior
uncertainty across routes. Table 7 summarizes the BRMDP-specific notation introduced below.

Table 7: Notation for BRMDP
Notation Definition
xm = (x1,m,. . ., xJ,m) Vector of sampled hypothesis counts before route m in BRMDP
D Number of hyper-posterior draws used in BRMDP
wj(xm) BRMDP weight on hypothesis j at route m, equal to x j,m/D
sBRMDPt,m State in BRMDP at flight t on route m: (N+m,N −m;x m)
V(j) ϵ (k| ·) BRMDP action value under hypothesis P (j) and sampled mixturex m
˜Vϵ(k| ·) BRMDP integrated action value under sampled mixturex m
˜Wϵ(·) BRMDP state value under sampled mixturex m
πBRMDP ϵ,D (· | ·) BRMDP choice rule with policy noiseϵand D hyper-posterior draws
Approximation through hyper-posterior draws.Under MetaDP, the consumer evaluates each action by
integrating over all prior hypotheses using the full hyper-posterior Qm. Equivalently, one can view MetaDP
as the limiting case of averaging over infinitely many draws fromQm. BRMDP replaces that exact integration
with a finite-sample approximation.
At the start of route m, the consumer draws D<∞hypothesis indices independently with replacement
from Qm. This yields the count vector
xm = (x1,m,. . ., xJ,m)∼Multinomial(D, Q m),
where xj,m is the number of times hypothesisj appears among the D draws. These counts define route-specific
mixture weights
wj(xm) = xj,m ∥xm∥1 = xj,m D , JX j=1 wj(xm) = 1. (26)
The vectorx m therefore provides a sampled approximation to the hyper-posterior. Rather than evaluating
each hypothesis in proportion to its exact probability Qm(j), the consumer evaluates hypotheses in proportion
to their empirical frequencies in the D draws. When D<J , some hypotheses may receive zero weight, which
reduces computation by allowing the consumer to ignore sufficiently unlikely possibilities. As D→ ∞, the
empirical weights converge almost surely to the exact hyper-posterior weights, wj(xm) →Q m(j), and the
BRMDP mixture converges to the fully integrated MetaDP mixture.
Using these sampled weights, we denote the BRMDP state during route m as sBRMDPt,m = (N+m,N −m;x m),
wherex m is fixed throughout route m.

Hypothesis-conditioned action values under sampled integration.Conditional on hypothesis P(j), the
action value from choosing airline k is
V(j) ϵ  k|N + m,N − m,x m;P  = ˆθ(j) k,t,m
+γ
h
ˆθ(j) k,t,m ˜Wϵ  N+ m +e k,N − m,x m;P 
+

1− ˆθ(j) k,t,m  ˜Wϵ  N+ m,N − m +e k,x m;P i .
(27)
This recursion is the same forward-looking Bellman logic used in MetaDP, except that future values are
computed under the sampled mixturex m rather than the exact hyper-posterior Qm.
Integrated action and state values under sampled integration.Replacing Qm(j) in Equation (21) with
wj(xm) gives the sampled integrated action value:
˜Vϵ  k|N + m,N − m,x m;P  = JX
j=1
wj(xm) V(j) ϵ  k|N + m,N − m,x m;P  . (28)
At the terminal flight, there is no continuation value, so
˜Vϵ  k|N + m,N − m,x m;P  = JX
j=1
wj(xm) ˆθ(j) k,T,m,∥N + m∥1 +∥N − m∥1 = T−1. (29)
Applying theϵ-greedy rule to these sampled integrated action values gives the policy-induced state value:
˜Wϵ  N+ m,N − m,x m;P  = (1−ϵ) max k ˜Vϵ  k|N + m,N − m,x m;P  + ϵ K KX k=1 ˜Vϵ  k|N + m,N − m,x m;P  . (30)
Equations (27)–(30) are solved by backward induction over t = T, T−1,. . ., 1 within route m.
BRMDP choice rule.Action selection applies the same ϵ-greedy logic as in MetaDP, but now to the
sampled integrated action values ˜Vϵ. Thus, the BRMDP policy is
πBRMDP ϵ,D ˜k|N + m,N − m,x m;P  = (1−ϵ) 1
n
˜k∈arg max
k
˜Vϵ  k|N +m,N −m,x m;P o

arg max k ˜Vϵ  k|N +m,N −m,x m;P 

 + ϵ K. (31)
Equations (27)–(31) define the BRMDP policy. See Web Appendix C.3 for the BRMDP pseudocode.
Interpretation and limiting cases.BRMDP provides a tractable way to model a boundedly rational
consumer’s inherent reward–computation trade-off. The parameter D governs how accurately the consumer
integrates cross-route prior uncertainty. As D→ ∞, the empirical weights converge to the exact hyper-
posterior weights, and BRMDP converges to MetaDP. At the other extreme, small values of D produce

simpler and more approximate policies in which the consumer plans using a coarse representation of prior
uncertainty. In this sense, BRMDP nests a family of boundedly rational meta-learning policies between the
fully rational MetaDP benchmark and simpler heuristics.
Taken together, the three policy classes span the main behavioral possibilities of interest in this paper.
The baseline DP policy captures a consumer who learns only within a route and treats each new route as a
fresh problem. MetaDP captures a fully integrated meta-learner who transfers information across routes and
incorporates that information into full-horizon dynamic planning. BRMDP spans intermediate cases in which
the consumer also transfers information across routes, but does so approximately, using a limited number of
hypothesis draws.
6 Empirical Comparison of the Policies
We now compare the behavior of humans in our experiment with that of the three classes of algorithms
discussed above. We first present descriptive comparisons from the data and simulations in §6.1 and then
present likelihood-based estimation in§6.2.
6.1 Qualitative Comparison of Human and Simulated Policy Dynamics
Before turning to formal likelihood comparisons, we begin with a descriptive comparison between human
behavior and simulated policy paths. Figures 7 and 8 plot mean best-airline selection and mean pseudo-regret
over flights and routes for the Far Means–Low Var. condition (see Web Appendix E.2 for the corresponding
plots for the other experimental conditions). For the policy curves, we simulate each policy 2,000 times in
the same calibrated environment and compute the same route-by-flight performance measures used for the
human data. The figures, therefore, provide a common descriptive benchmark for comparing the qualitative
dynamics of humans and policies, rather than a formal goodness-of-fit exercise. As an initial comparison, we
set ϵ = 0 for all policies to obtain their noise-free performance. Later, we explain how we include ϵ in our
likelihood-based analysis.
For the baseline DP policy, we use uninformative priors, (α, β) = (1,1). For MetaDP and BRMDP, we
construct the hypothesis class from the experimental mean grid {.2, .4, .5, .6, .8}, which yields 5 3 = 125
candidate prior hypotheses for the three airlines. We then map each candidate mean µ(j) k into a Beta prior by
setting α(j) k = µ(j) k and β(j) k = 1 −µ (j) k . As an illustrative member of the boundedly rational policy class, we
plot BRMDP(1), where BRMDP(1) denotes a policy with one hyper-posterior draw (D = 1).
The figures suggest that the qualitative trajectory of human behavior is closer to BRMDP(1) than to

1 4 7 10
0.50
0.75
DP
Route 10
Route 5
Route 1
1 4 7 10
MetaDP
1 4 7 10
BRMDP(1)
1 4 7 10
Human
Mean best-airline selection Flight
Figure 7: Mean best-airline selection over flights for different routes in the Far Means–Low Var. condition. BRMDP(1) more closely
resembles participant behavior. Policy curves are averages over 2,000 simulated runs.
1 4 7 10
0.1
0.2
0.3
DP
Route 10
Route 5
Route 1
1 4 7 10
MetaDP
1 4 7 10
BRMDP(1)
1 4 7 10
Human
Mean regret
Flight
Figure 8: Mean pseudo-regret over flights for different routes in the Far Means–Low Var. condition. BRMDP(1) represents behavior
closer to participants. Policy curves are averages over 2,000 simulated runs.
either DP or MetaDP. Because DP does not transfer information across routes, its best-airline-selection and
pseudo-regret profiles are nearly the same from one route to the next. MetaDP lies at the opposite extreme:
it improves sharply at the beginning of later routes, reflecting aggressive and fully integrated cross-route
learning. Human behavior does not closely match either pattern.
By contrast, BRMDP(1) produces trajectories that more closely resemble the human data. In both cases,
performance at the beginning of a route improves gradually across routes: best-airline selection starts lower
and rises over flights, while pseudo-regret starts higher and declines, with later routes beginning from better
baselines than earlier ones. Thus, this descriptive comparison already points to an intermediate form of
cross-route learning—stronger than DP, but less sharp than fully integrated MetaDP. The likelihood-based
analysis that follows formalizes this comparison and evaluates that conclusion more rigorously.
6.2 Likelihood-Based Model Comparison
Having introduced the three policy classes—DP, MetaDP, and BRMDP—we now compare them to the
experimental data. The central question is straightforward: which of these policies most closely matches
the sequence of choices participants actually make? To answer this question, we use likelihood-based
comparison to evaluate competing hypotheses about the decision-making policies consumers adopt (Kass and
Raftery, 1995). Following the trial-by-trial approach of Daw et al. (2011), we evaluate each model on the full

observed decision path rather than on aggregate outcomes alone, and we extend that logic to our multi-route,
hierarchical setting.
This framework is especially useful in our context because the candidate policies differ not only in how
they learnwithina route, but also in whether and how they transfer informationacrossroutes. As a result, the
likelihood comparison speaks directly to the paper’s main substantive question: do consumers behave like
no-transfer learners, fully rational meta-learners, or boundedly rational meta-learners?
Throughout, we condition on the realized flight outcomes when evaluating choice probabilities. This is
standard in dynamic choice applications: the policy determines the probability of each action, while realized
outcomes affect future choices only through belief updating. Accordingly, a model fits the data well if, after
observing the same history that the participant observed, it assigns high probability to the participant’s next
choice. See Web Appendix D for a detailed explanation of the likelihood estimation procedure.
Estimation Results.We now turn from likelihood construction to likelihood comparison. Throughout this
subsection, the baseline DP policy uses uninformative priors, (α, β) = (1,1). For MetaDP and BRMDP, we
construct the hypothesis class from the discrete mean grid used in the experiments,{.2, .4, .5, .6, .8}. Taking
all ordered triples with replacement yields 53 = 125 candidate prior hypotheses for the three airlines.7 We
then map each candidate meanµ (j) k into a Beta prior as follows:α (j) k =µ (j) k andβ (j) k = (1−µ (j) k ).
We also set the discount factor to γ = 1. This is a practical and economically sensible choice in our
short-horizon task, where rewards are realized at the end of the experiment, and discounting is therefore less
salient (Liu and Ansari, 2020). More importantly, γ is not separately identified in our setting without an
instrument that shifts continuation values while leaving current payoffs unchanged (Magnac and Thesmar,
2002; Rust, 1987). Accordingly, we treatγ= 1 as a maintained assumption throughout.
For each policy and experimental condition, we aggregate participant-level log-likelihoods. A higher
log-likelihood means the policy assigns a higher probability to the observed sequence of choices, conditioned
on the same histories participants observed. This comparison is informative because the three policy families
embody different behavioral mechanisms. DP captures within-route learning without cross-route transfer.
MetaDP captures fully integrated cross-route learning. BRMDP spans an intermediate class in which
consumers transfer knowledge across routes, but approximately, through a limited number of prior draws.
7In this calibration, the true environment’s prior means lie in the hypothesis class. However, participants are not aware of these
means, so their prior means could be misspecified. In Web Appendix E.4, we relax this assumption and show that the likelihood
estimations for a case with misspecified prior means are directionally the same as the main results.

We evaluate the total log-likelihood over a grid of 20 noise values, spanningϵ∈ [.01, .5]. This allows us
to compare policies without tying the conclusion to one particular choice of noise parameter. We vary D over
{1, 3, 6, 10}. Figure 9 and Table 8 report the resulting fit profiles for DP, MetaDP, and BRMDP for the Far
Means–Low Variance experiment. See Web Appendix E.3 for the results for the other three conditions. Here,
we assume the policies solve the dynamic programming problem, taking the full ten flights of each route into
account. Nevertheless, we present similar results for shorter planning horizons in Web Appendix E.5.
0.1 0.2 0.3 0.4 0.5
ϵ
0.0
0.2
0.4
0.6
0.8
1.0
Normalized Log-Likelihood
Far Means - Low Var.
BRMDP(D)
MetaDP
DP
D=1
D=3
D=6
D=10
Figure 9: Log-likelihood comparison across policies for 20 values of ϵ. Monte Carlo likelihood calculations use B = 2,000 samples.
We normalized the log-likelihood values via (l. −l min)/(lmax −l min) for better visualizations and unified plots. BRMDP(1) represents
the highest values, indicating a better fit.
Table 8: Log-likelihood by policy andε
Policy .268 .294 .319 .345 .371 .397 .423 .448 .474 .500
DP -6161.5 -6116.6 -6086.3 -6068.6-6062.2-6066.0 -6079.1 -6100.8 -6130.6 -6168.1
BRMDP(1) -5737.1 -5721.2-5717.6-5724.9 -5741.9 -5768.0 -5802.2 -5844.2 -5893.5 -5949.8
BRMDP(3) -5884.9 -5857.4 -5846.3-5844.5-5849.3 -5861.0 -5880.0 -5942.4 -5978.7 -6022.9
BRMDP(6) -6078.9 -6024.3 -5988.4-5970.1-5978.1 -6006.2 -5991.6 -6009.2 -6037.9 -6074.8
BRMDP(10) -6181.9 -6122.4 -6079.2 -6050.1 -6033.8-6028.8-6034.3 -6049.5 -6073.8 -6106.7
MetaDP -6506.1 -6415.5 -6344.3 -6290.0 -6250.5 -6224.5 -6210.6-6207.9-6215.6 -6233.1
Notes:Only the last 10 (largest) ε values are shown. Boldfaced values represent the largest log-likelihood within each policy
row.
There are two main takeaways from this analysis. First, for a range of smaller D values, the BRMDP
policy has a higher log-likelihood than the baseline DP benchmark. 8 This superiority shrinks and eventually
8Since the finite-simulation Jensen bias is downward, the exact BRMDP log-likelihoods would be higher in expectation than the

reverses as D becomes larger, and the policy moves closer to the fully integrated MetaDP benchmark.
This pattern suggests that participants do transfer information across routes, but they do so in a boundedly
rational way rather than as fully optimal meta-learners. Second, for larger values of D, and consequently
more integrated meta-learning, the maximum log-likelihood tends to occur at larger noise values. Under
the ϵ-greedy specification, a larger noise parameter means that the policy places less weight on the value-
maximizing airline and more weight on uniform exploration across all airlines. As a result, choices become
less tightly tied to the policy’s computed action values and therefore more stochastic. This indicates that as
the policy becomes more optimal, it becomes more distant from observed human behavior unless paired with
substantial decision noise.
The likelihood results provide further support for the paper’s substantive conclusion. They reject both
behavioral extremes. On the one hand, participants are not pure within-route learners: DP fits systematically
worse than a range of bounded meta-learning models. On the other hand, participants are not fully optimal
meta-planners: the highest-fitting models use relatively small D, not the full MetaDP benchmark. The data,
therefore, point to boundedly rational meta-learning: among the policies we consider, consumers generalize
from prior routes using simplified representations of prior uncertainty. This aggregate result also holds
broadly across participants. In Web Appendix E.7, participant-level out-of-sample comparisons show that,
in every condition, the median predictive-likelihood share favors BRMDP(1) over both DP and MetaDP,
although there remains meaningful heterogeneity across participants.
This pattern aligns with theories from cognitive science that view human behavior as resource-rational
rather than unbounded (Bhui et al., 2021; Gershman, 2018; Griffiths et al., 2019; Lieder and Griffiths, 2020;
Simon, 1955). Among these theories are those that show evidence for approximate Bayesian inference done
by drawing a small number of posterior samples. Under these models, one- or few-sample decision-making
has been shown to account for behavior in single-context judgment and choice tasks (Chater et al., 2020; Vul
et al., 2014). Our results extend this picture. First, in our model, the logic of approximation through sampling
operates at themeta-levelof prior uncertainty across tasks, not only at the within-task level: BRMDP(1),
which represents the cross-route hyper-posterior with a single draw, fits human choice data better than
BRMDP(D> 1) and MetaDP variants. Second, our findings emerge in a setting that requires forward-looking
planning, not one-shot judgment. This suggests that coarse internal sampling may control how consumers
integrate prior uncertainty into sequential, finite-horizon decisions. These new findings complement recent
reported simulated values. Thus, the strong fit of BRMDP(1) is conservative.

work that examines human cognition as the output of a meta-learning process over distributions of related
tasks (Binz et al., 2024; Lai and Gershman, 2024). Once such a meta-level prior is in place, our model
characterizes how a boundedly rational agent can use it for efficient decision-making.
6.3 Robustness Checks and Extensions
We subject both the reduced-form evidence of knowledge transfer and the policy-comparison results to a
series of robustness checks. These analyses address several alternative explanations for our main findings:
that the behavioral evidence is an artifact of researcher-observed outcome measures; that BRMDP(1)’s
advantage is specific to one experimental environment or prior specification; that it reflects assumptions about
planning horizon or stochastic choice; that cross-route improvement is driven by task familiarity rather than
knowledge transfer; or that any simple form of cross-route transfer would fit equally well. We also evaluate
whether BRMDP(1)’s advantage persists out of sample and across participants. Across these exercises, the
main conclusion remains unchanged. We summarize the results below and provide the full analyses in Web
Appendix E.
• Choice-path evidence of knowledge transfer.Our main reduced-form measures in §4 (best-airline
selection and pseudo-regret) use the true route-specific on-time rates, which participants do not observe.
Web Appendix E.1 therefore examines transfer using only participants’ own observed choices and
outcomes. Before each new route, we construct airline-specific posterior means from either all earlier
routes or only the immediately preceding route and relate these beliefs to the participant’s first choice
on the new route. Under both history definitions, participants are significantly more likely to begin a
new route with an airline whose posterior mean is higher. Thus, the evidence for cross-route knowledge
transfer is visible directly in the choice path and does not rely on latent environmental parameters.
• Robustness across experimental environments.The main-text qualitative and likelihood comparisons
focus on the Far Means–Low Var. condition, where airlines are relatively easy to distinguish, and their
performance is comparatively stable across routes. In Web Appendices E.2 and E.3, we repeat the
comparisons in all four experimental conditions. BRMDP(1) continues to outperform both DP and
MetaDP in predicting participants’ choices across these environments. Its relative advantage is therefore
not confined to the setting most favorable to cross-route learning.
• Prior-mean misspecification.Our main specification constructs the candidate prior class from the pooled
mean grid across the experimental conditions, so the true environmental means are contained in the

hypothesis class. Web Appendix E.4 deliberately misspecifies this class by swapping the mean sets across
experiments: we use .2, .5, .8when the true means are .4, .6, .8, and vice versa. BRMDP(1) retains the
highest likelihood and the policy ordering remains directionally consistent with the main results. Thus,
the advantage of coarse integration is not driven by including the true prior means in the candidate class.
• Planning-horizon robustness.The main analysis assumes that consumers plan over the full ten-flight
route horizon. Because prior work suggests that shorter planning horizons can better describe human
sequential choice (Camerer et al., 2004; Meyer and Shi, 1995), in Web Appendix E.5 we re-solve all
policies using rolling two- and five-flight planning horizons. BRMDP(1) remains the best-fitting policy
under both specifications. The preference for coarse integration of higher-order uncertainty therefore
persists even when consumers are allowed to be substantially more myopic within a route.
• Alternative stochastic choice rule.Our main specification uses an ϵ-greedy rule to map action values
into stochastic choices. Because the policy ranking could in principle reflect this mapping rather than the
learning process itself, Web Appendix E.6 replaces ϵ-greedy choice with a smooth softmax rule (Bhui
et al., 2021). BRMDP(1) remains the best-fitting policy. Its relative advantage therefore does not depend
on the particular form of stochasticity used to translate action values into choice probabilities.
• Out-of-sample predictive validation.Next, we ask whether BRMDP(1)’s in-sample advantage gen-
eralizes to held-out choices. Web Appendix E.7 conducts two validation exercises using the exact
BRMDP(1) likelihood. First, we estimate the choice-noise parameter using all other participants in
the same condition and predict the held-out participant. Second, we select the noise parameter using
routes 1–5 and evaluate predictive fit on routes 6–10. In every experimental condition and in both
exercises, the mean participant-level predictive log-likelihood difference favors BRMDP(1) over both
DP and MetaDP, with 95% participant-bootstrap confidence intervals entirely above zero. The median
participant-level predictive-likelihood share also exceeds .5 against both benchmarks in every condition.
Thus, BRMDP(1)’s advantage persists for held-out participants and future choices and reflects a broad
pattern across participants rather than a small number of influential observations, although meaningful
individual heterogeneity remains.
• No-transfer learning with improving execution.Cross-route improvement could arise even without
knowledge transfer if participants simply become more familiar with the task and execute the same
within-route strategy more consistently over time. To examine this possibility, in Web Appendix E.8,

we introduce Dynamic Programming with Improving Execution (DPIE), a no-transfer DP policy whose
choice noise is allowed to decline across routes. We estimate the declining noise profile using leave-
one-participant-out validation within each experimental condition. BRMDP(1) achieves a higher mean
predictive log-likelihood than DPIE in all four conditions. Thus, improvements in task execution alone
do not account for the predictive advantage of cross-route learning.
•Non-meta-learning knowledge-transfer benchmarks.Finally, our main comparison focuses on meta-
learning policies, but BRMDP(1) could fit well simply because it carries airline-specific information
across routes rather than because it learns and represents higher-order uncertainty. To distinguish these
explanations, in Web Appendix E.9, we consider three knowledge-transfer policies that do not maintain
a hyper-posterior. The first, Knowledge Transfer Mean-Updating (KTMU), pools observations from
earlier and current routes and chooses myopically based on the resulting posterior means. This provides
a simple form of knowledge transfer that effectively treats past and current experience as coming from
the same context. The second, ν-Knowledge Transfer Mean-Updating (ν-KTMU), instead summarizes
earlier experience as a transferred prior with a fixed effective sample size ν. This allows past experience
to shape beliefs on a new route without treating all earlier observations as if they were generated in
the current context, while remaining myopic in its choices. Finally, ν-Knowledge Transfer Dynamic
Programming (ν-KTDP) uses the same transferred prior but incorporates it into a finite-horizon dynamic
program, allowing us to separate the role of forward-looking planning from the higher-order learning
embodied in BRMDP. Across all four experimental conditions, BRMDP(1) has a higher likelihood than
these non-meta-learning benchmarks throughout the displayed ϵ grid. Its advantage therefore cannot be
explained simply by pooling past outcomes, transferring a smoothed brand-level mean across routes, or
combining such transfer with forward-looking planning.
7 Managerial Implications and Takeaways
The results above have implications not only for model fit, but also for the managerial counterfactuals one
would draw from the model. In many repeated-choice settings, consumers do not appear to treat each new
route, product category, or usage context as an entirely fresh problem. Instead, they carry forward brand-level
beliefs from prior experience. This means that quality inferences can spill over across contexts, so that
experiences in one setting may shape demand in another.
At the same time, our likelihood results indicate that this transfer is not best described by either extreme

benchmark. Consumers do not behave as if they ignore cross-context information altogether, but neither
do they appear to fully integrate all prior uncertainty in the manner implied by MetaDP. Rather, the best-
fitting low-D BRMDP specifications suggest that consumers transfer knowledge using coarse summaries of
prior experience. This distinction matters because pricing, promotion, trial, and launch decisions are often
nonlinear in consumer beliefs. As a result, the wrong behavioral model can generate the wrong managerial
recommendation even when it captures the broad direction of learning.
The results yield three main managerial takeaways. Most broadly, they imply that brand-level learning
can carry across adjacent contexts and therefore affect downstream demand beyond the initial setting. They
also imply that the behavioral model used for counterfactual analysis matters: a firm that assumes either
no transfer or full integration may mischaracterize how consumers respond to new offerings. Finally, they
suggest that when consumers behave more like BRMDP(1), effective managerial policies should be designed
for a market composed of consumers with coarse transferred priors rather than for a single fully integrated
representative consumer. We discuss these implications below. Detailed numerical illustrations are provided
in Web Appendix F.
• Early experiences matter beyond the initial context.Because consumers appear to carry brand-level
priors across routes, categories, or adjacent usage contexts, a firm’s early performance can affect later
demand even when the consumer encounters the brand in a new setting. This increases the long-run value
of high-signal early experiences and increases the downstream cost of salient early failures. The pricing
example in Web Appendix F.1 illustrates this point: after favorable prior experience, a no-transfer DP
forecast can be too conservative because it ignores the demand created by transferable brand-level beliefs.
• The choice of learning model matters for managerial counterfactuals.The likelihood results in §6
favor BRMDP(1) over either DP or fully integrated MetaDP. Accordingly, a manager who forecasts
demand using either a no-transfer model or a fully integrated meta-learning model may choose the wrong
price, promotion, or trial policy even when the model captures the broad direction of learning. In the
spirit of Meyer and Hutchinson (2016), the issue is not only model fit; it is that the wrong behavioral
model can imply the wrong policy. The counterfactuals in Web Appendix F.1 illustrate both directions
of error: DP can underprice or overinvest in support because it ignores transfer, while MetaDP can
miss profitable targeted interventions because it collapses heterogeneous coarse priors into a single
representative posterior.

• Coarse integration implies mixture demand.When consumers behave more like BRMDP(1), the
market looks less like a representative consumer with one integrated posterior and more like a mixture of
consumers using coarse sampled priors. This matters whenever firm decisions are nonlinear in beliefs, as
in pricing, promotions, launch trials, or assortment visibility. In such settings, DP can under-react because
it ignores transfer, whereas MetaDP can misstate threshold responses because it averages away coarse
heterogeneity in consumers’ priors. The route-entry examples in Web Appendix F.2 show the same logic
for featured placement and trial credits.
Taken together, these implications suggest that managers should treat early experiences as investments
in transferable brand beliefs, but should avoid assuming that consumers integrate such beliefs fully and
continuously. When behavior is closer to BRMDP(1), launch demand and intervention response are better
viewed as mixture outcomes generated by coarse transferred priors. Managerial policies that recognize
this mixture structure are likely to produce more reliable counterfactuals than policies that assume no
meta-learning or those that assume a fully integrated representative-consumer benchmark.
8 Conclusion
Many everyday purchase sequences contain opportunities to carry knowledge across contexts. We study
this form of learning-to-learn in a hierarchical Bernoulli bandit setting and compare human behavior with
dynamic-programming policies that differ in how they use cross-context information. Our framework
nests a no-transfer DP benchmark that treats contexts independently, a fully integrated MetaDP benchmark
that carries cross-context beliefs into dynamic planning, and a boundedly rational BRMDP(D) family that
approximates MetaDP by limiting the integration of hyper-posterior uncertainty.
Using data from a carefully designed multi-context experiment, we first present clear evidence of
knowledge transfer. Pseudo-regret declines across routes, best-airline selection improves across routes, and
later routes begin from a better choice baseline, indicating that people do not treat each route in isolation
but instead carry structure forward. Next, we use the set of policy classes we developed and trial-by-trial
likelihood comparisons to show that a boundedly rational meta-learning policy best accounts for behavior.
Low-D BRMDP(D) specifications, especially BRMDP(1), fit the human choice data better than both the
no-transfer DP benchmark and the fully integrated MetaDP benchmark. Thus, the likelihood results reject
both extremes: participants do not ignore cross-route information, but they also do not appear to integrate
prior uncertainty as fully as MetaDP requires. As D increases and BRMDP approaches MetaDP, the fit to the

data worsens, suggesting that the best account is not simply a noisier version of full Bayesian integration. The
main substantive conclusion is that consumers transfer knowledge across contexts using meta-learning, but
they do so approximately, using a coarse representation of prior uncertainty. The paper considers a spectrum
of meta-learning policies and identifies the one that best describes human choices: a policy that learns and
reuses higher-order beliefs about brand performance across contexts through a structured, forward-looking
process, while relying on a computationally parsimonious representation of uncertainty.
Methodologically, the paper introduces and empirically tests two new model classes for consumer meta-
learning in sequential choice. The first is MetaDP, a fully integrated Bayesian meta-learning model that
combines cross-context belief updating with finite-horizon dynamic programming. The second isBRMDP(D),
a boundedly rational approximation that limits the integration of cross-context uncertainty through a finite
number of hyper-posterior draws. We also develop a route-level Monte Carlo likelihood estimator for BRMDP,
which integrates over consumers’ latent internal draws and allows DP, MetaDP, and BRMDP to be compared
on identical information sets and observed histories.
For managers, this implies that early, high-signal experiences that shape brand priors can yield downstream
gains beyond the initial context, but the behavioral model used for counterfactual analysis also matters. A
no-transfer model can understate the effect of favorable prior experience or lead firms to overinvest in support
that consumers no longer need. A fully integrated MetaDP model can also mislead because it collapses coarse
heterogeneity in consumers’ transferred priors into a single representative posterior. When behavior is closer
to BRMDP(1), demand in a new context is better viewed as arising from a mixture of consumers with coarse
transferred priors. This has direct implications for pricing, promotion, featured placement, and trial-credit
decisions, especially because these policies are nonlinear in consumer beliefs.
References
Auer, Peter, Nicol`o Cesa-Bianchi and Paul Fischer (2002), ‘Finite-time analysis of the multiarmed bandit
problem’,Machine Learning47(2-3), 235–256.
Basu, Soumya, Branislav Kveton, Manzil Zaheer and Csaba Szepesv´ari (2021), ‘No regrets for learning the
prior in bandits’,Advances in neural information processing systems34, 28029–28041.
Bellman, Richard (1956), ‘A problem in the sequential design of experiments’,Sankhy ¯a: The Indian Journal
of Statistics (1933-1960)16(3/4), 221–229.
Bellman, Richard (1966), ‘Dynamic programming’,science153(3731), 34–37.
Bhui, Rahul, Lucy Lai and Samuel J Gershman (2021), ‘Resource-rational decision making’,Current Opinion
in Behavioral Sciences41, 15–21.
Binz, Marcel, Ishita Dasgupta, Akshay K Jagadish, Matthew Botvinick, Jane X Wang and Eric Schulz (2024),
‘Meta-learned models of cognition’,Behavioral and Brain Sciences47, e147.

Bohren, J Aislinn and Daniel N Hauser (2025), ‘Misspecified models in learning and games’,Annual Review
of Economics17.
Bubeck, S ´ebastien, Nicolo Cesa-Bianchi et al. (2012), ‘Regret analysis of stochastic and nonstochastic
multi-armed bandit problems’,Foundations and Trends® in Machine Learning5(1), 1–122.
Callaway, Frederick, Bas Van Opheusden, Sayan Gul, Priyam Das, Paul M Krueger, Thomas L Griffiths and
Falk Lieder (2022), ‘Rational use of cognitive resources in human planning’,Nature human behaviour
6(8), 1112–1125.
Camerer, Colin F, Teck-Hua Ho and Juin-Kuan Chong (2004), ‘A cognitive hierarchy model of games’,The
quarterly journal of economics119(3), 861–898.
Chater, Nick, Jian-Qiao Zhu, Jake Spicer, Joakim Sundh, Pablo Le´on-Villagr´a and Adam Sanborn (2020),
‘Probabilistic biases meet the bayesian brain’,Current Directions in Psychological Science29(5), 506–512.
Che, Hai, T ¨ulin Erdem and T Sabri ¨Onc¨u (2015), ‘Consumer learning and evolution of consumer brand
preferences’,Quantitative Marketing and Economics13, 173–202.
Ching, Andrew T, T¨ulin Erdem and Michael P Keane (2013), ‘Learning models: An assessment of progress,
challenges, and new developments’,Marketing Science32(6), 913–938.
Ching, Andrew T, T¨ulin Erdem and Michael P Keane (2017), ‘Empirical models of learning dynamics: A
survey of recent developments’,Handbook of marketing decision modelspp. 223–257.
Coscelli, Andrea and Matthew Shum (2004), ‘An empirical model of learning and patient spillovers in new
drug entry’,Journal of econometrics122(2), 213–246.
Crawford, Gregory S and Matthew Shum (2005), ‘Uncertainty and learning in pharmaceutical demand’,
econometrica73(4), 1137–1173.
Daw, Nathaniel D et al. (2011), ‘Trial-by-trial data analysis using computational models’,Decision making,
affect, and learning: Attention and performance XXIII23(1), 3–38.
DeGroot, Morris H (2005),Optimal statistical decisions, John Wiley & Sons.
Eluchans, Mattia, Gian Luca Lancia, Antonella Maselli, Marco D’Alessandro, Jeremy Raboff Gordon and
Giovanni Pezzulo (2025), ‘Adaptive planning depth in human problem-solving’,Royal Society Open
Science12(4).
Erdem, T¨ulin (1998), ‘An empirical analysis of umbrella branding’,Journal of Marketing Research35(3), 339–
351.
Erdem, T¨ulin and Michael P Keane (1996), ‘Decision-making under uncertainty: Capturing dynamic brand
choice processes in turbulent consumer goods markets’,Marketing science15(1), 1–20.
Gabaix, Xavier, David Laibson, Guillermo Moloche and Stephen Weinberg (2006), ‘Costly information
acquisition: Experimental analysis of a boundedly rational model’,American Economic Review96(4), 1043–
1068.
Gelman, Andrew, John B Carlin, Hal S Stern and Donald B Rubin (1995),Bayesian data analysis, Chapman
and Hall/CRC.
Gershman, Samuel J (2018), ‘Deconstructing the human algorithms for exploration’,Cognition173, 34–42.
Griffiths, Thomas L, Frederick Callaway, Michael B Chang, Erin Grant, Paul M Krueger and Falk Lieder
(2019), ‘Doing more with less: meta-reasoning and meta-learning in humans and machines’,Current
Opinion in Behavioral Sciences29, 24–30.
Griffiths, Thomas L, Nick Chater and Joshua B Tenenbaum (2024),Bayesian models of cognition: Reverse
engineering the mind, MIT Press.
Grubb, Michael D and Matthew Osborne (2015), ‘Cellular service demand: Biased beliefs, learning, and bill
shock’,American Economic Review105(1), 234–271.
Guan, Jiechao and Hui Xiong (2024), ‘Improved bayes regret bounds for multi-task hierarchical bayesian
bandit algorithms’,Advances in Neural Information Processing Systems37, 72964–72999.
Ho, Mark K, Jonathan D Cohen and Thomas L Griffiths (2023), ‘Rational simplification and rigidity in
human planning’,Psychological Science34(11), 1281–1292.

Hofacker, Charles F, Huong NL Nguyen and Matteo Fina (2024), ‘Bayesian inference and consumer
behavioral theory’,Psychology & Marketing41(12), 3144–3156.
Hong, Joey, Branislav Kveton, Manzil Zaheer and Mohammad Ghavamzadeh (2022), Hierarchical bayesian
bandits,in‘International Conference on Artificial Intelligence and Statistics’, PMLR, pp. 7724–7741.
Hutchinson, J Wesley and Eric M Eisenstein (2008), ‘Consumer learning and expertise’,Handbook of
consumer psychology4, 103–132.
Hutchinson, J Wesley and Robert J Meyer (1994), ‘Dynamic decision making: Optimal policies and actual
behavior in sequential choice problems’,Marketing Letters5, 369–382.
Jindal, Pranav and Anocha Aribarg (2021), ‘The importance of price beliefs in consumer search’,Journal of
Marketing Research58(2), 321–342.
Kass, Robert E and Adrian E Raftery (1995), ‘Bayes factors’,Journal of the american statistical association
90(430), 773–795.
Kemp, Charles, Andrew Perfors and Joshua B Tenenbaum (2007), ‘Learning overhypotheses with hierarchical
bayesian models’,Developmental science10(3), 307–321.
Koller, Daphne and Nir Friedman (2009),Probabilistic graphical models: principles and techniques, MIT
press.
Kveton, Branislav, Mikhail Konobeev, Manzil Zaheer, Chih-wei Hsu, Martin Mladenov, Craig Boutilier and
Csaba Szepesvari (2021), Meta-thompson sampling,in‘International Conference on Machine Learning’,
PMLR, pp. 5884–5893.
Lai, Lucy and Samuel J Gershman (2024), ‘Human decision making balances reward maximization and
policy compression’,PLOS Computational Biology20(4), e1012057.
Lai, Tze Leung and Herbert Robbins (1985), ‘Asymptotically efficient adaptive allocation rules’,Advances in
applied mathematics6(1), 4–22.
Lattimore, Tor and Csaba Szepesv´ari (2020),Bandit algorithms, Cambridge University Press.
Lieder, Falk and Thomas L Griffiths (2020), ‘Resource-rational analysis: Understanding human cognition as
the optimal use of limited computational resources’,Behavioral and brain sciences43, e1.
Lin, Song, Juanjuan Zhang and John R Hauser (2015), ‘Learning from experience, simply’,Marketing
Science34(1), 1–19.
Liu, Jia and Asim Ansari (2020), ‘Understanding consumer dynamic decision making under competing
loyalty programs’,Journal of Marketing Research57(3), 422–444.
Magnac, Thierry and David Thesmar (2002), ‘Identifying dynamic discrete decision processes’,Econometrica
70(2), 801–816.
McCoy, John, Rachele Ciulli and Eric Bradlow (2022), ‘Two-for-one conjoint: Bayesian cross-category
learning for shared-attribute categories’,Available at SSRN 4136593.
Meyer, Robert J and J Wesley Hutchinson (2016), ‘(when) are we dynamically optimal? a psychological field
guide for marketing modelers’,Journal of Marketing80(5), 20–33.
Meyer, Robert J and Yong Shi (1995), ‘Sequential choice under ambiguity: Intuitive solutions to the armed-
bandit problem’,Management science41(5), 817–834.
Montgomery, Cynthia A and Birger Wernerfelt (1992), ‘Risk reduction and umbrella branding’,Journal of
Businesspp. 31–50.
Nabi, Sareh, Houssam Nassif, Joseph Hong, Hamed Mamani and Guido Imbens (2022), ‘Bayesian meta-prior
learning using empirical bayes’,Management Science68(3), 1737–1755.
Rust, John (1987), ‘Optimal replacement of gmc bus engines: An empirical model of harold zurcher’,
Econometrica: Journal of the Econometric Societypp. 999–1033.
Salakhutdinov, Ruslan, Joshua B Tenenbaum and Antonio Torralba (2012), ‘Learning with hierarchical-deep
models’,IEEE transactions on pattern analysis and machine intelligence35(8), 1958–1971.
Schulz, Eric, Nicholas T Franklin and Samuel J Gershman (2020), ‘Finding structure in multi-armed bandits’,
Cognitive psychology119, 101261.

Schulz, Eric and Samuel J Gershman (2019), ‘The algorithmic architecture of exploration in the human
brain’,Current opinion in neurobiology55, 7–14.
Shanks, David R, Richard J Tunney and John D McCarthy (2002), ‘A re-examination of probability matching
and rational choice’,Journal of Behavioral Decision Making15(3), 233–250.
Simon, Herbert A (1955), ‘A behavioral model of rational choice’,The quarterly journal of economics
pp. 99–118.
Sridhar, Karthik, Ram Bezawada and Minakshi Trivedi (2012), ‘Investigating the drivers of consumer
cross-category learning for new products using multiple data sets’,Marketing Science31(4), 668–688.
Sutton, Richard S, Andrew G Barto et al. (1998),Reinforcement learning: An introduction, V ol. 1, MIT press
Cambridge.
Tehrani, Shervin Shahrokhi and Andrew T Ching (2024), ‘A heuristic approach to explore: The value of
perfect information’,Management Science70(5), 3200–3224.
Tenenbaum, Joshua B, Charles Kemp, Thomas L Griffiths and Noah D Goodman (2011), ‘How to grow a
mind: Statistics, structure, and abstraction’,science331(6022), 1279–1285.
Vul, Edward and Harold Pashler (2008), ‘Measuring the crowd within: Probabilistic representations within
individuals’,Psychological Science19(7), 645–647.
Vul, Edward, Noah Goodman, Thomas L Griffiths and Joshua B Tenenbaum (2014), ‘One and done? optimal
decisions from very few samples’,Cognitive science38(4), 599–637.
Wernerfelt, Birger (1988), ‘Umbrella branding as a signal of new product quality: An example of signalling
by posting a bond’,The RAND Journal of Economicspp. 458–466.
Wu, Charley M, Eric Schulz, Maarten Speekenbrink, Jonathan D Nelson and Bj¨orn Meder (2018), ‘General-
ization guides human exploration in vast decision spaces’,Nature human behaviour2(12), 915–924.
Xu, Fei and Joshua B Tenenbaum (2007), ‘Word learning as bayesian inference.’,Psychological review
114(2), 245.
Yang, Liu, Olivier Toubia and Martijn G De Jong (2015), ‘A bounded rationality model of information search
and choice in preference measurement’,Journal of Marketing Research52(2), 166–183.

Web Appendix
Boundedly Rational Meta-Learning in Sequential Consumer Choice
Contents
A Experimental Instructions 3
B Backward Induction Details 6
B.1 Backward Induction Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
B.2 State and Action Value Counts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
C Dynamic Programming-Based Learning Algorithms 10
C.1 Baseline DP Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
C.2 MetaDP Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
C.3 BRMDP Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
D Likelihood Estimation Details 12
D.1 DP and MetaDP Likelihood Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
D.2 BRMDP Likelihood Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
D.3 Why is Exact Meta-Learning Likelihood Estimation Not Feasible? . . . . . . . . . . . . . . 14
D.4 Algorithm for Monte Carlo Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
E Robustness Checks and Extensions 17
E.1 Choice-Path Evidence of Knowledge Transfer . . . . . . . . . . . . . . . . . . . . . . . . . 17
E.2 Qualitative Human-Algorithms Comparison . . . . . . . . . . . . . . . . . . . . . . . . . . 20
E.3 Log-Likelihood Results for All Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . 21
E.4 Robustness to Prior Means Misspecification . . . . . . . . . . . . . . . . . . . . . . . . . . 21
E.5 Planning-Horizon Robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
E.6 Softmax Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
E.7 Out-of-Sample Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
E.7.1 Leave-One-Participant-Out Prediction . . . . . . . . . . . . . . . . . . . . . . . . . 24
1

E.7.2 Validation on Future Routes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
E.8 No-Transfer DP with Improving Execution (DPIE) . . . . . . . . . . . . . . . . . . . . . . 29
E.9 Non-Meta-Learning Knowledge-Transfer Benchmarks . . . . . . . . . . . . . . . . . . . . 31
E.9.1 Knowledge Transfer Mean-Updating (KTMU) . . . . . . . . . . . . . . . . . . . . 31
E.9.2 Shrinkage Knowledge Transfer Mean-Updating (ν-KTMU) . . . . . . . . . . . . . 34
E.9.3 Shrinkage Knowledge Transfer Dynamic Programming (ν-KTDP) . . . . . . . . . . 36
F Stylized Managerial Counterfactuals 39
F.1 Stylized Counterfactuals for Pricing and Promotion . . . . . . . . . . . . . . . . . . . . . . 39
F.2 Stylized Counterfactuals for Route-Entry Interventions . . . . . . . . . . . . . . . . . . . . 41
G Environment Check 46
2

Web Appendix A: Experimental Instructions
In this section, we provide the experimental instructions we give to participants.
Figure W1: Overview of the experimental task and participants’ objective.
Figure W2: Structure of the experimental task, including routes, flights, and airline options.
3

Figure W3: Illustration that airline performance can vary across routes in the experimental environment.
Figure W4: Keyboard mappings used to select airlines in the experimental task.
4

Figure W5: Instruction-check questions used to verify participants’ understanding of the task.
5

Web Appendix B: Backward Induction Details
B.1 Backward Induction Algorithm
The Dynamic Programming (DP) policy, as outlined in §5.2, requires the computation of value functions
for every possible state at each flight. In this section, we evaluate an ϵ-greedypolicy: we compute the
value of choosing a particular airline k, indexed by the noise level ϵ as Vϵ

k| N+,N −; α, β, t  , and the
correspondingpolicy valueof being in a given state under ϵ-greedy, denoted Wϵ

N+,N −; α, β, t  . Backward
induction proceeds from the final decision point (t = T) recursively to the first flight (t = 1), and considers the
expectation implied by theϵ-greedy policy when calculating the optimal values.
A state at any given time t in the decision process is fully characterized by the priors, accumulated history
of choices, and outcomes. In our Bernoulli bandit setting with Beta priors, we can identify each state as
sDP t = (N+,N −;α,β),
whereN + = (N+ 1, . . ., N+ K) andN − = (N− 1 , . . ., N− K) are the on-time and delayed counts up to flight t− 1, and
(α, β) are the prior parameters. The posteriors satisfy ˆα = α +N +, ˆβ = β +N −, equivalently, componentwise
ˆαk,t =α k + N+ k,t−1,
ˆβk,t =β k + N− k,t−1 ,
and the flight index enters through∥N +∥1 +∥N −∥1 = t−1.
Base Case: Final Flight (t = T):At the final flight T, there are no subsequent flights to consider. Thus, the
choice-specific value reduces to the immediate expected reward,
Vϵ

k|N +,N −;α,β  = ˆθk,T = αk + N+ k,T−1 αk +β k + N+ k,T−1 + N− k,T−1 . (W1)
The state value averages these one-step values according to the ϵ-greedy rule. With a uniform choice-noise
kernel q(k) = 1/K,
Wϵ

N+,N −;α,β  = (1−ϵ) max
k
ˆθk,T + ϵ K KX k=1 ˆθk,T, (W2)
We calculate these values for all feasible DP states sDP T that we can reach at time T (i.e., for allN +,N − with
∥N+∥1 +∥N −∥1 = T−1).
6

Recursive Step for Flights t<T :For any flight t<T , we work backward, assuming we have computed
Vϵ(· | ·) and Wϵ(·). The Bellman recursion with the state value Wϵ gives:
Vϵ

k|N +,N −;α,β  = ˆθk,t
+γ
h
ˆθk,t Wϵ  N+ +e k,N −;α,β 
+

1− ˆθk,t  Wϵ  N+,N − +e k;α,β i .
(W3)
Given the set of choice-specific values {Vϵ(k| N+,N −; α, β)}K k=1, the policy state value under a uniform
choice-noise kernel is
Wϵ

N+,N −;α,β  = (1−ϵ) max
k′
Vϵ

k′ |N +,N −;α,β  + ϵ K KX
k′=1
Vϵ

k′ |N +,N −;α,β  , (W4)
This recursive calculation is repeated by decrementing t from T− 1 down to 1. After completing this process,
we have the value functions Vϵ

k| N+,N −; α, β, t  and Wϵ  N+,N −; α, β, t  for all states. At any decision
point t, the ϵ-greedy policy assigns total probability 1 −ϵ to the value-maximizing airlines and distributes the
choice-noise probabilityϵuniformly across all K airlines; thus, q(k) = 1/K for all k.
Computational Considerations:The number of possible states ( ˆα, ˆβ) can be very large, making the
computation of value functions intensive. A state is defined by the 2K parameters (ˆα1, . . ., ˆαK, ˆβ1, . . ., ˆβK)
or, equivalently, by the counts (N+ 1,t−1, N− 1,t−1, . . ., N+ K,t−1, N− K,t−1) such that their sum equals t− 1. As we
mentioned before, even for K = 3 airlines and T = 10 flights, this can lead to a substantial number of states
(e.g., 5005 states), underscoring the computational challenge of implementing full DP. In the next section,
we explain how we count the number of possible states and action values for a given number of airlines and
flights.
B.2 State and Action Value Counts
In this section, we explain how we can count the number of states and action values in the backward induction
algorithm for DP. The main goal here is to show that the state space and, consequently, the amount of
calculation growth, is polynomial in T for fixed K, and combinatorial in K. Let K denote the number of
airlines and T the finite horizon (number of flights). As in§5.2, the state at flight t∈ {1,. . ., T}is
(N+,N −;α,β), (W5)
7

where for each airline k∈ {1, . . ., K}, the Beta posterior parameters are obtained from the Beta–Bernoulli
learning process via ˆαk = αk + N+ k and ˆβk = βk + N− k . We use uninformative priors, such as ( α, β) like
αk = βk = 1 ∀k∈ {1, . . ., K}. After t− 1 flights, let N+ k and N− k be, respectively, the numbers of on-time
and delayed outcomes observed for airline k up to (but not including) flight t. Then
KX
k=1
(N+ k + N− k ) = t−1. (W6)
Thus, at flight t the feasible DP states are in one-to-one correspondence with theincrementvectors

N+ 1, N− 1 ,. . ., N+ K, N− K  ∈Z 2K ≥0 satisfying (W6).
Importantly, the priors (α, β) only shift the posteriors and do not affect the number of distinct states; counting
depends solely on the nonnegative-integer solutions to (W6).
The number of solutions to (W6) is the number of weak compositions of t− 1 into 2K parts. By the
classical stars-and-bars argument,
St = #
n
sDP t feasible at flight t o = (t−1) + (2K−1) 2K−1  = t + 2K−2 2K−1  . (W7)
where St is the total number of possible states at flight t. Each such state contributes one state value–V∗(sDPt )
in the deterministic case, or Wϵ(sDPt ) under the ϵ-greedy policy, as defined in Equation (W4). Equation (W7)
is the exact count of the distinct state values that the DP policy must compute via backward induction for
flights t = 1,. . ., T.9 Summing (W7) over flight t = 1,. . ., T yields
Stotal =
TX
t=1
St =
TX
t=1
t + 2K−2
2K−1

=
T−1X
n=0
n + 2K−1
2K−1

=
T + 2K−1
2K

, (W8)
where the last equality follows from the hockey-stick (or Christmas stocking) identity. Equation (W8) is the
exact count of the distinct values V∗(·) that the DP policy must compute via backward induction for flights
t = 1,. . ., T.10
If, instead of state-values, one tabulates all choice-specific values V

k| N+,N −; α, β, t  for every airline
k at every state, the count is simply
K×S total = K
T + 2K−1
2K

. (W9)
9In a finite-horizon problem, t is part of the state because the continuation value is non-stationary.
10If one explicitly includes the terminal boundary condition at t = T + 1, it adds a single terminal state;(W8) counts only flight t≤T .
8

In our canonical example with K = 3 airlines and T = 10 flights, we have
Stotal =
10 + 2·3−1
2·3

=
15
6

= 5005.
For reference, the number of states at the final decision epoch t = 10 is, from (W7),
S10 =
10 + 2·3−2
2·3−1

=
14
5

= 2002.
If we enumerate all action-values, the total count is K×S total = 3×5005 = 15015.
9

Web Appendix C: Dynamic Programming-Based Learning Algorithms
In this section, we present the algorithms for the three policy classes that we formulate in §5—DP, MetaDP,
and BRMDP.
C.1 Baseline DP Algorithm
DP is the first algorithm that we explain as our baseline in §5.2. This algorithm treats each route as
a completely separate problem and begins solving it with uninformative priors. Accordingly, it has no
meta-learning mechanism.
Algorithm W1Baseline Dynamic Programming Policies (DP)
1:Inputs:priors (α,β), policy noiseϵ
2: Precompute (backward induction):for each t = T, T− 1, . . ., 1 and each feasible state (N+,N −) with
∥N+∥1 + ∥N−∥1 = t− 1, compute Vϵ(· |N+,N −) and Wϵ(N+,N −) using Equations (10), (16), and (17).
3:Forward play (execute the policy within a route)
4:Initialize counts (N +,N −)←0
5:fort = 1toTdo
6:Sample A t ∼π DPϵ (· |N+,N −;α,β) (Equation (14))
7:Observe realized outcome y t ∈ {0, 1}and update (N+,N −) as in Algorithm 1
8:end for
C.2 MetaDP Algorithm
MetaDP is our algorithm described in §5.4 for transferring knowledge in an optimal, Bayesian manner. It
carries a hyper-posterior across routes and uses it to the fullest extent.
C.3 BRMDP Algorithm
We propose BRMDP as a boundedly rational policy in §5.5. In the core specification, this policy uses the
number of hyper-posterior draws, D, to control how finely prior uncertainty is represented during route-level
planning.
10

Algorithm W2Meta Dynamic Programming (MetaDP)
1:Inputs:hypothesis setP={(α (j),β (j))}J j=1, initial hyper-prior Q1, policy noiseϵ
2:form = 1,. . ., Mdo
3:Backward induction within routem: treatQ m as fixed
4:foreach t = T, T−1,. . ., 1 and each feasible state (N +m,N −m) with∥N +m∥1 +∥N −m∥1 = t−1do
5:ift = Tthen
6:Compute ¯Vϵ(· |N+m,N −m, Qm;P) using Equation (22)
7:else
8:For each hypothesis j and airline k, compute V (j) ϵ (k|N +m,N −m, Qm;P) using Equation (20)
9:Compute ¯Vϵ(· |N+m,N −m, Qm;P) using Equation (21)
10:end if
11:Compute ¯Wϵ(N+m,N −m, Qm;P) using Equation (23)
12:end for
13:Forward play within routem:initialize (N +m,N −m)←0
14:fort = 1,. . ., Tdo
15:Choose airline A m,t ∼π MetaDPϵ (· |N+m,N −m, Qm;P) (Equation (25))
16:Observe outcome y m,t ∈ {0, 1}and update (N+m,N −m) as in Algorithm 1
17:end for
18:Update the hyper-posterior from Q m to Qm+1 using Algorithm 2
19:end for
Algorithm W3Boundedly Rational Meta Dynamic Programming (BRMDP)
1:Inputs:P={(α (j),β (j))}J j=1, initial hyper-prior Q1, policy noiseϵ, draws D
2:form = 1,. . ., Mdo
3:Route weights:drawx m ∼Multinomial(D, Q m) and set wj(xm)←x j,m/D for j = 1,. . ., J
4:Backward induction within routem
5:fort = Tdown to1do
6:foreach feasible state (N +,N −) such that∥N +∥1 +∥N −∥1 = t−1do
7:ift = Tthen
8:For all k: compute ˜Vϵ(k|N +,N −,x m;P) using Equation (29)
9:else
10:For each j, k: compute V (j) ϵ (k|N +,N −,x m;P) using Equation (27)
11:For each k: compute ˜Vϵ(k|N +,N −,x m;P) using Equation (28)
12:end if
13:Compute ˜Wϵ(N+,N −,x m;P) using Equation (30)
14:end for
15:end for
16:Forward play within routem
17:Reset counts:(N +m,N −m)←0
18:fort = 1,. . ., Tdo
19:Choose A m,t ∼π BRMDP ϵ,D (· |N+m,N −m,x m;P)
20:Observe y m,t ∈ {0, 1}and update (N+m,N −m) as in Algorithm 1
21:end for
22:Cross-route update:update Q m to Qm+1 as in Algorithm 2
23:end for
11

Web Appendix D: Likelihood Estimation Details
D.1 DP and MetaDP Likelihood Estimation
Observed histories and likelihood logic.Recall that we defined H1:m−1 = ( H1, . . ., Hm−1) as the
concatenated history of the previous routes before route m in §3.2. Further, let the within-route history
available before flight t on route m be Hm,t−1 =

(Am,1, ym,1), . . ., (Am,t−1, ym,t−1)

. Then, the full
information set before decision t on route m is denoted as Im,t−1 =

H1:m−1, Hm,t−1

. Further, letN + m,t−1
andN − m,t−1 denote the vectors of on-time and delayed counts implied by Hm,t−1. The current flight index is
pinned down by these counts through t =∥N + m,t−1∥1 +∥N − m,t−1∥1 + 1.
The identification logic is simple. Each policy maps the observed history into a state, and each state
implies a probability for the action actually chosen. Multiplying those trial-by-trial probabilities along the
observed path gives the route-level likelihood; summing logs gives the participant-level log-likelihood.
DP likelihood.We begin with the baseline DP policy from §5.2. Under baseline DP, previous routes are
irrelevant because the policy does not transfer information across routes. Hence, although we write the
likelihood as a function ofI m,t−1 for notational symmetry, only the current-route counts matter:
P

Am,t = ˜k| Im,t−1,π DP,ϵ  =π DP ϵ ˜k|N + m,t−1,N − m,t−1;α,β  (W10)
where πDPϵ ˜k| N+ m,t−1,N − m,t−1; α, β  is defined in Equation (14). Then, the participant-level log-likelihood
is
ℓDP =
MX
m=1
TX
t=1
logπ DP ϵ  Am,t |N + m,t−1,N − m,t−1;α,β  . (W11)
In practice, we set α =1and β =1, so DP starts each route from uninformative priors. This makes DP the
natural no-transfer benchmark.
MetaDP likelihood.For MetaDP, the logic is the same, but the relevant state is richer. In addition to the
current-route counts, the policy uses the hyper-posterior Qm, which summarizes what has been learned from
routes 1,. . ., m−1. Thus, the probability of the observed action at flight t on route m is
P

Am,t = ˜k| Im,t−1,π MetaDP,ϵ  =π MetaDP ϵ ˜k|N + m,t−1,N − m,t−1, Qm;P  (W12)
where πMetaDPϵ ˜k| N+ m,t−1,N − m,t−1, Qm; P  is defined in Equation(25). Because Qm is updated only between
routes, it is fixed throughout route m and fully determined by H1:m−1. The resulting participant-level log-
12

likelihood is
ℓMetaDP =
MX
m=1
TX
t=1
logπ MetaDP ϵ  Am,t |N + m,t−1,N − m,t−1, Qm;P  . (W13)
Taken together, Equations(W11) and (W13) identify two benchmark extremes. DP treats every route as
a fresh problem; MetaDP carries forward all cross-route information and uses it in fully forward-looking
planning. Therefore, comparing these likelihoods reveals whether the data support no transfer or full transfer.
D.2 BRMDP Likelihood Estimation
Why BRMDP is more difficult to estimate.Estimating the likelihood of BRMDP from §5.5 is more
challenging because the researcher does not observe consumers’ route-level internal draws from the hyper-
posterior. Recall that before route m, a BRMDP consumer draws D hypothesis indices from the hyper-
posterior Qm, forms the count vectorx m, converts it into weights wj(xm) = xj,m/D, and then solves the
route-level dynamic program conditional on that sampled mixture. Conditional onx m, the policy generates
well-defined trial-by-trial choice probabilities. Unconditionally, however,x m is latent, so the route likelihood
must integrate over all possible count vectors.
This route-level integration is important. The latent drawx m is made once per route and then held fixed
throughout that route. Therefore, the expectation is taken over route-level latent states, not independently at
each flight. The exact route-m likelihood is
P(D) m =E xm∼Multinomial(D,Qm)
" TY
t=1
πBRMDP ϵ,D  Am,t |N + m,t−1,N − m,t−1,x m;P 
#
. (W14)
Becausex m is a count vector from D i.i.d. categorical draws with probabilities Qm, its probability mass
function is multinomial:
Pr(xm =x|Q m) = D! QJ
j=1 xj!
JY
j=1
Qm(j)xj,
JX
j=1
xj = D.
Substituting this into Equation (W14) yields the exact finite-sum representation
P(D) m = X
x∈NJP
j xj=D
Pr(xm =x|Q m)
TY
t=1
πBRMDP ϵ,D  Am,t |N + m,t−1,N − m,t−1,x;P  . (W15)
The participant-level log-likelihood is then
ℓ(D) BRMDP =
MX
m=1
log P(D) m . (W16)
13

This expression makes the identification problem transparent. The BRMDP likelihood differs from
MetaDP likelihood not because the policy rule is unknown, but because the policy depends on latent internal
randomness that must be integrated out. In other words, BRMDP is identified through the distribution of
route-level sampled mixtures that it induces.
Monte Carlo estimator.Exact evaluation of Equation (W15) is infeasible once D or J becomes even
moderately large, because the number of possible count vectors grows combinatorially. We therefore
approximate the route-level expectation by Monte Carlo (see Web Appendix D.3 for additional computational
details). For each route m, we draw B i.i.d. samplesx (b) m ∼Multinomial (D, Qm). Conditional on each draw,
we solve the induced BRMDP problem once, evaluate the observed route path, and then average the resulting
route probabilities:
bP (D) m = 1 B BX b=1 exp ( TX t=1 logπ BRMDP ϵ,D  Am,t |N + m,t−1,N − m,t−1,x (b) m ;P o , bℓ(D) BRMDP = MX m=1 log bP (D) m . (W17)
By construction, bP (D) m is an unbiased and consistent estimator of the exact route likelihood P(D) m . As B
increases, this average concentrates on the true marginal likelihood P(D) m , giving a consistent estimate of
how likely the observed choices are under a boundedly rational sampler. The corresponding log-likelihood
bℓ(D) BRMDP is therefore a simulation-based approximation to the BRMDP fit. 11
Intuitively, the BRMDP likelihood integrates over the agent’s unobserved internal randomness: instead
of conditioning on a particular prior-samplex m, we average the product of choice probabilities across all
samples that the policy could draw from Qm. Because enumerating those samples is intractable for moderate
D and J, we approximate this integral by Monte Carlo—simulatex m ∼Multinomial (D, Qm), solve the
induced BRMDP problem once per draw, and average the resulting route-level probabilities. Please see
Algorithm W4 in Appendix D.4 for a detailed summary of this Monte Carlo procedure.
D.3 Why is Exact Meta-Learning Likelihood Estimation Not Feasible?
The sum in Equation (W15) ranges over all count vectors x∈N J with PJ j=1 xj = D. By stars-and-bars, the
number of terms is
NX(D, J) =
D + J−1
J−1

≍ DJ−1
(J−1)! . (W18)
11For finite B, log bP (D) m is not an unbiased estimator of log P(D) m . Since the logarithm is concave, Jensen’s inequality implies
E
h
log bP (D) m i ≤logE h bP (D) m i = log P(D) m . Thus, the simulated BRMDP log-likelihood has a finite-simulation downward bias. This
bias vanishes as B→ ∞.
14

For each x, we must run one integrated backward induction to obtain the corresponding route-level choice
probabilities. Using the state convention from Appendix B.2, at flight t there are
t + 2K−2
2K−1

distinct within-route states. Summing over decision epochs t = 1,. . ., T gives
S(T, K) =
TX
t=1
t + 2K−2
2K−1

=
T−1X
n=0
n + 2K−1
2K−1

=
T + 2K−1
2K

≍ T2K
(2K)!. (W19)
Evaluating all choice-specific values over these states costs at least
costDP(T, K) =Θ

K S(T, K)

. (W20)
Hence, a per-route lower bound on exact evaluation is
workexact m ≳N X(D, J)×cost DP(T, K) =Θ
D + J−1
J−1

K
T + 2K−1
2K

. (W21)
Even moderate values are prohibitive:
(J, D, K, T) = (8, 50, 4, 40) : N X =
57
7

= 2.64×10 8, S =
47
8

= 3.14×10 8,
⇒work exact m ≳N X ·KS≈3.33×10 17;
(J, D, K, T) = (10, 100, 5, 40) : N X =
109
9

= 4.26×10 12, S =
49
10

= 8.22×10 9,
⇒work exact m ≳1.75×10 23.
Memory also binds: one double per state needs 8S(T, K) bytes, so S = 3.14 × 108 already implies roughly
2.5 GB for a single value array (and several arrays are required). Because the integrated values ¯Vϵ depend on
w = x/D, distinct x prevent reuse and preserve the
D+J−1
J−1

factor.
Conclusion. Exact evaluation scales as
workexact m =Θ
 K
(J−1)!(2K)! DJ−1T2K

, (W22)
which grows combinatorially in ( J, D) and as a high-degree polynomial in T, rendering Equation (W15)
intractable beyond small cases. This motivates the route-level Monte Carlo estimator in Equation (W17).
15

D.4 Algorithm for Monte Carlo Procedure
We provide the pseudocode for the algorithm we use to compute the BRMDP log-likelihood using the Monte
Carlo method.
Algorithm W4BRMDP(D) Monte Carlo Log-Likelihood
1: Input:observed data; prior sets P; initial hyper-prior Q1; policy noise ϵ; hyper-draws D; Monte Carlo
samples B
2:Initialize: bℓ(D) BRMDP ←0
3:form = 1 to Mdo
4:a m ← −∞; s(b) m ←0 for all b = 1,. . ., B
5:forb = 1 to Bdo▷route-level Monte Carlo over latent count vectors
6:Drawx (b) m ∼Multinomial(D, Q m) and set wj(x(b) m )←x (b) j,m/D
7: Precompute ˜Vϵ(· | ·,x (b) m ; P) and ˜Wϵ(·,x (b) m ; P) by backward induction using Equations (27)–(30)
8:Initialize (N +,N −)←0
9:fort = 1 to Tdo▷evaluate the policy on the observed route history
10:s (b) m ←s (b) m + log h πBRMDP ϵ,D  Am,t |N +,N −,x (b) m ;P i
11:Update (N +,N −) using the observed outcome ym,t as in Algorithm 1
12:end for
13:a m ←max(a m, s(b) m )
14:end for
15:log bP (D) m ←a m + log  1 B PB b=1 exp{s(b) m −a m} 
16: bℓ(D) BRMDP ← bℓ(D) BRMDP + log bP (D) m
17:Compute{N + k,m, N− k,m, Tk,m}K k=1 from{(A m,t, ym,t)}T t=1
18:Update the hyper-posterior from Q m to Qm+1 using Algorithm 2
19:end for
20:return bℓ(D) BRMDP
16

Web Appendix E: Robustness Checks and Extensions
E.1 Choice-Path Evidence of Knowledge Transfer
The best-airline selection and pseudo-regret measures in §4 evaluate participants’ choices relative to the
route-specific on-time rates θ∗ m,k. These environmental properties provide natural measures of decision
quality, but participants do not observe them. We therefore complement those measures with a choice-path
analysis that relates the first choice on each new route to a posterior summary of the participant’s own earlier
outcomes. This analysis shows whether, before observing any feedback on the current route, a participant
is more likely to choose an airline that performed well in their earlier experience. A positive correlation
between each airline’s observed performance and the participants’ chance of selecting that airline at the start
of each route corroborates the reduced-form results we already have.
To construct the posterior summaries, we add the participant index i to the choice and outcome notation
from §3.4. Thus, Ai,m,t is participant i’s choice on flight t of route m, N+ i,k,m and N− i,k,m count the on-time and
delayed outcomes that participant i observes after choosing airline k on that route, and Ti,k,m = N+ i,k,m +N− i,k,m.
LetH i,1:m−1 denote the corresponding participant-specific history available at the beginning of route m.
We summarize this history using the same independent Beta(1, 1) prior that the baseline updating model
employs. First, the cumulative posterior mean for airline k before route m is
bθcum i,k,m−1 = 1 + Pm−1 em=1 N+ i,k, em 2 + Pm−1 em=1 Ti,k, em , m = 2,. . ., M. (W23)
This posterior uses every outcome that the participant observed on routes 1, . . ., m− 1. To distinguish
accumulated experience from one-route carryover, we also construct a posterior using only the immediately
preceding route:
bθlast i,k,m−1 = 1 + N+ i,k,m−1 2 + Ti,k,m−1 . (W24)
If the participant does not choose an airline in the relevant history, its posterior mean remains 1/2. These
auxiliary posteriors provide descriptive summaries of the outcomes that participants observed. In particular,
they differ from the hyper-posterior Qm and do not impose the finite hypothesis class that MetaDP and
BRMDP use.
17

For each history definition, we also identify the airline or tied airlines with the largest posterior mean:
Bcum i,m−1 = arg max k∈{1,...,K} bθcum i,k,m−1,
Blast i,m−1 = arg max k∈{1,...,K} bθlast i,k,m−1, (W25)
and retain all ties. The cumulative set reflects the participant’s full earlier history, whereas the previous-route
set isolates the information from route m−1.
We estimate alternative-level conditional logits for the first choice on routes m = 2, . . ., M. Let ζ∈
{cum, last} index the history definition, let e(i) denote participant i’s experimental condition, and let δe(i),k
denote condition-specific airline fixed effects. Following the condition-interaction structure in Equation (9),
let1 experiment,i denote the three-vector of indicators for the non-baseline experimental conditions. We omit
Far Means–Low Var. The posterior-mean specifications are
Pr

Ai,m,1 = k

 Hi,1:m−1  = exp
n
ψζ bθζ i,k,m−1 + (ψint ζ )⊤  bθζ i,k,m−1 ×1 experiment,i  +δ e(i),k o
PK
k′=1 exp
n
ψζ bθζ i,k′,m−1 + (ψint ζ )⊤  bθζ i,k′,m−1 ×1 experiment,i  +δ e(i),k′ o. (W26)
For the posterior-best specifications, letι ζ i,k,m−1 =1{k∈ Bζ i,m−1}. We then estimate
Pr

Ai,m,1 = k

 Hi,1:m−1  = exp
n
φζ ιζ i,k,m−1 + (φint ζ )⊤  ιζ i,k,m−1 ×1 experiment,i  +δ e(i),k o
PK
k′=1 exp
n
φζ ιζ i,k′,m−1 + (φint ζ )⊤  ιζ i,k′,m−1 ×1 experiment,i  +δ e(i),k′ o. (W27)
The coefficients ψζ and φζ capture the posterior relationships in the Far Means–Low Var. condition. The
elements of ψint ζ and φint ζ measure how those relationships differ in the other three conditions. We treat each
participant-route as one choice set containing all three airlines. The choice-set likelihood conditions out the
participant-route intercept. A separate participant fixed effect would enter all three alternatives in a choice
set equally and would therefore cancel from Equations (W26) and (W27). We cluster standard errors at the
participant level to account for repeated route-entry choices.
18

Posterior Mean Posterior-Best Indicator
All Earlier Routes Previous Route All Earlier Routes Previous Route
Coef.p-value Coef.p-value Coef.p-value Coef.p-value
Posterior coefficient 1.978<.001 1.879<.001 .847<.001 .710<.001
(.340) (.375) (.133) (.131)
Far Means–High Var.−.151 .739−.152 .758−.043 .821−.024 .890
(.453) (.491) (.188) (.172)
Close Means–Low Var.−.401 .438−.893 .082−.416 .025−.397 .027
(.518) (.514) (.186) (.180)
Close Means–High Var. .148 .791 .105 .844−.012 .952−.030 .869
(.557) (.533) (.191) (.180)
Condition–airline fixed effects✓ ✓ ✓ ✓
Participant–route choice sets✓ ✓ ✓ ✓
Choice sets 2,745 2,745 2,745 2,745
Alternative-level observations 8,235 8,235 8,235 8,235
Participants (clusters) 305 305 305 305
Table W1: Conditional-logit regression results for the first airline choice on routes 2,. . ., 10. The first two specifications estimate
Equation W26, and the final two estimate Equation (W27). Participant-clustered standard errors are in parentheses. Thep-values
on the coefficient rows are from two-sided Wald tests. The posterior coefficient represents the relationship in the baseline Far
Means–Low Var. condition; the remaining rows report interactions. All specifications include condition-specific airline fixed effects
and condition on the participant-route choice set.
Table W1 shows that, in the baseline Far Means–Low Var. condition, the cumulative posterior mean is
positively associated with the participant’s first choice on a new route (1.978, SE = .340,p < .001). The
previous route posterior mean yields a similar result (1.879, SE = .375,p < .001). Relative to the baseline
condition, the cumulative-posterior interaction estimates are−.151 for Far Means–High Var. (p= .739), −.401
for Close Means–Low Var. (p= .438), and .148 for Close Means–High Var. (p= .791); the corresponding
previous-route interaction estimates are −.152 (p= .758), −.893 (p= .082), and .105 (p= .844). These
estimates indicate that the relationship between posterior means and route entry choices is broadly similar
across the four experimental environments.
The posterior-best specifications show a positive baseline relationship, too. When an airline belongs to
the cumulative posterior-best set, the odds that the participant chooses it first are 2.332 times the odds for an
airline outside that set (.847, SE = .133,p < .001). When the posterior uses only the immediately preceding
route, the corresponding odds ratio is 2.034 (.710, SE = .131,p < .001). Relative to the baseline condition,
the Close Means–Low Var. interaction estimates are−.416 (p= .025) in the cumulative specification and
−.397 (p= .027) in the previous-route specification, indicating a weaker posterior-best relationship in that
condition. The cumulative interaction estimates for Far Means–High Var. and Close Means–High Var. are
19

−.043 (p= .821) and −.012 (p= .952), respectively; the corresponding previous-route interaction estimates
are−.024 (p= .890) and−.030 (p= .869).
These estimates complement the performance results in the main text. The main analysis shows that
choices improve relative to the properties of the experimental environment. The choice-path analysis instead
links the first choice on a new route to posterior summaries that use the participant’s own earlier outcomes.
The estimates reveal this relationship when the posterior uses only the previous route and when it uses all
earlier routes. The condition interactions reveal no statistically detectable variation in the continuous posterior-
mean relationship across the experimental environments, whereas the discrete posterior-best relationship
weakens in one condition.
E.2 Qualitative Human-Algorithms Comparison
In §4.1, we present the pseudo-regret plot and the best airline selection plot of the Far Means–Low Variance
experiment. In this section, we provide the plots for all experiments. Beyond the trends we mentioned in the
main text, we also see that experiments with close means yield tighter pseudo-regret and best-airline selection
lines. This is expected because these environments represent airlines that are more similar to one another,
making the distinction more difficult.
0.50
0.75
DP
Route 10
Route 5
Route 1
MetaDP BRMDP(1)
Far Means
Low Var.
Human
0.50
0.75
Far Means
High Var.
0.50
0.75
Close Means
Low Var.
1 4 7 10
0.50
0.75
1 4 7 10 1 4 7 10 1 4 7 10
Close Means
High Var.
Mean best-airline selection
Flight
Figure W6: Mean best-airline selection over flights for different routes. Each line represents a distinct route, and earlier routes are
shown in lighter shades.
20

0.1
0.2
0.3
DP
Route 10
Route 5
Route 1
MetaDP BRMDP(1)
Far Means
Low Var.
Human
0.1
0.2
0.3
Far Means
High Var.
0.1
0.2
0.3
Close Means
Low Var.
1 4 7 10
0.1
0.2
0.3
1 4 7 10 1 4 7 10 1 4 7 10
Close Means
High Var.
Mean regret
Flight
Figure W7: Mean pseudo-regret over flights for different routes. Each line represents a distinct route, and earlier routes are shown in
lighter shades.
E.3 Log-Likelihood Results for All Experiments
In §6.2, we present the likelihood estimation results for one of the experiments (Far Means–Low Variance).
Figure W8 reports results for all the experiments. We can see from the plot that the conclusions are the same
as those we described in the main text.
E.4 Robustness to Prior Means Misspecification
In §6.2, we assumed that the prior class contains the true environment’s prior means by including all the prior
means from our experiments. Accordingly, we use {.2, .4, .5, .6, .8}, as the set of participants’ prior means.
Thus, the candidate classes always include the true prior means. In this section, we show the robustness of
the results by using misspecified prior means in our estimations. We acknowledge that there are infinitely
many misspecified prior classes we could use here; nevertheless, we present results for one class, in which
we simply swap the prior means between experiments. In this way, we use {.4,.6,.8} for the Far Means -
Low/High variance experiments where the environment’s means are{.2, .5, .8}, and vice versa. Figure W9
reports the estimation results for these new prior classes. As we can see, the results are directionally in
line with our main results, where BRMDP(1) achieves the highest log-likelihood values, MetaDP shows the
21

0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(D)
MetaDP
DP
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood
Normalized Log-Likelihood
ϵ
Figure W8: Log-likelihood comparison across policies for 20 values of the noise parameter ϵ. We set γ = 1 for all policies and report
BRMDP(D) fits for D∈ {1, 3, 6, 10}. Monte Carlo likelihood calculations use B = 2,000 samples. On each chart, we normalized the
log-likelihood values via (l. −l min)/(lmax −l min) for better visualizations and unified plots. Higher values indicate a better fit.
lowest fit, and the other algorithms fall between them. Additionally, among the BRMDP class of algorithms,
the more a policy performs optimally in solving the airline choice problem, the poorer it fits the behavioral
data.
E.5 Planning-Horizon Robustness
In the main text, all policies are solved over the full route horizon. As a supplementary robustness check, we
also report the results from four experiments under the alternative truncation cases h = 2 and h = 5.
E.6 Softmax Specification
Throughout the paper, we use the ϵ-greedy rule to map action values into choice probabilities. As a robustness
check, we also estimate the same policies under a softmax rule. The immediate payoff, posterior updating,
and backward-induction logic remain the same. The only change is that, instead of using the ϵ-greedy state
value, the continuation value is computed using a softmax-weighted average of the action values.
For example, in MetaDP, once we compute the integrated action values ¯Vτ  k| N+m,N −m, Qm; P  , the
softmax rule assigns choice probabilities according to
πMetaDP τ ˜k|N + m,N − m, Qm;P  = exp

¯Vτ ˜k|N +m,N −m, Qm;P  /τ 
PK
k′=1 exp
 ¯Vτ  k′ |N +m,N −m, Qm;P  /τ ,
22

0.0
0.5
1.0
Far Means - Low Var.
BRMDP(D)
MetaDP
DP
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
0.0 0.2 0.4
ϵ
0.0
0.5
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
0.0 0.2 0.4
ϵ
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood of Policies
Normalized Log-Likelihood
Figure W9: Log-likelihood comparison across policies for 20 values of the noise parameter ϵ, with misspecified prior means. We set
γ = 1 for all policies and report BRMDP(D) fits for D∈ {1, 3, 6, 10}. Monte Carlo likelihood calculations use B = 2,000 samples.
On each chart, we normalized the log-likelihood values via (l. −l min)/(lmax −l min) for better visualizations and unified plots. Higher
values indicate a better fit.
0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(D)
MetaDP
DP
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood
Normalized Log-Likelihood
ϵ
(a) Robustness check with h = 2.
0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(D)
MetaDP
DP
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood
Normalized Log-Likelihood
ϵ (b) Robustness check with h = 5.
Figure W10: Four-experiment grids of normalized log-likelihood over ϵ. The backward induction truncated at h = 2 and h = 5,
respectively.
whereτis the temperature parameter. In this way, the induced state value is
¯Wτ  N+ m,N − m, Qm;P  = KX
k=1
πMetaDP τ  k|N + m,N − m, Qm;P  ¯Vτ  k|N + m,N − m, Qm;P  .
23

Thus, compared with the ϵ-greedy specification, the action-value recursion changes only through this
continuation term: the policy averages the future action values using softmax probabilities rather than the
uniform choice-noise probabilities of the ϵ-greedy rule. The same substitution applies to DP and BRMDP,
replacing Vϵ, ¯Vϵ, and ˜Vϵ by theirτ-indexed counterparts.
In the softmax specification, τ governs the noise in the policy. Accordingly, as τ→ 0, the decision rule
becomes deterministic, choosing the highest-value airline. In contrast, as τ→ ∞, the decision rule becomes
a uniform one choosing airlines with equal probability. Accordingly, instead of plotting log-likelihood over
a grid of ϵ values, Figure W11 plots the results over a grid of temperature values between .1 and 5. The
qualitative conclusion is unchanged: BRMDP(1) remains the best-fitting specification, and BRMDP agents
with higher D values perform worse. As D increases, the BRMDP performance approaches that of our most
optimal policy, MetaDP. The only difference between the results here and the ones in 6.2 is that MetaDP
outperforms DP for a wide range ofτvalues.
E.7 Out-of-Sample Validation
We next assess whether BRMDP(1)’s superior fit generalizes out of sample, both to held-out participants and to
choices on future routes. We focus on the three policies central to our analysis: DP, BRMDP(1), and MetaDP.
In both validation exercises, we estimate the exact likelihood of BRMDP(1). When D = 1, the finite sum in
Equation (W15) contains only the J = 125 possible hypothesis draws, making full enumeration feasible. For
each validation method and experimental condition, we first report the mean within-participant log-likelihood
difference, with participant-bootstrap 95% confidence intervals. We then examine the participant-level
distribution using normalized per-choice likelihood shares.
E.7.1 Leave-One-Participant-Out Prediction
Our first validation method compares the policies’ ability to describe the choices of held-out participants
within each experimental condition. For each policy and each leave-one-out participant, we estimate the ϵ
that maximizes the aggregate log-likelihood among all remaining participants. We then evaluate the selected
policy on the held-out participant’s complete observed choice sequence. Repeating this procedure for every
participant ensures that each participant’s predictive log-likelihood is obtained using a value of ϵ without
incorporating that participant’s data.
Figure W12 reports the resulting within-participant paired log-likelihood differences. In every experi-
mental condition, the mean differences between BRMDP(1) and both DP and MetaDP are positive, and the
24

0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(D,h)
MetaDP
DP
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
10−1 100
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
10−1 100
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood
Normalized Log-Likelihood
Temperature (τ )
Figure W11: Log-likelihood comparison across policies for 20 values of the temperature parameter τ. We set γ = 1 for all policies
and report BRMDP(D) fits for D∈ {1, 3, 6, 10}. Monte Carlo likelihood calculations use B = 2,000 samples. On each chart, we
normalized the log-likelihood values via (l. −l min)/(lmax −l min) for better visualizations and unified plots. Higher values indicate a
better fit.
corresponding 95% confidence intervals lie entirely above zero (p < .001 for all mean differences). This
result shows the overall superiority of BRMDP(1) over both DP and MetaDP in predicting participants’
choices using an out-of-sample approach.
Participant-level distribution of predictive fit.The paired mean differences in Figure W12 establish
whether BRMDP(1) predicts held-out participants betteron average. However, an average difference alone
does not reveal whether this advantage is broadly distributed across participants or is generated by a relatively
small number of participants with large likelihood improvements. Thus, we also examine the participant-level
distribution of predictive fit.
For participant i, let ℓDP,i, ℓMetaDP,i, and ℓ(1) BRMDP,i denote the leave-one-participant-out predictive log-
likelihoods under DP, MetaDP, and BRMDP(1), respectively. Because each held-out participant makes T
choices on each of the M routes, we can calculate the corresponding per-choice log-likelihoods by dividing
25

0
5
Far Means - Low Var. Far Means - High Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
0
5
Close Means - Low Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
Close Means - High Var.
Mean Participant Log-Likelihood Diﬀerence
Figure W12: Leave-one-participant-out predictive log-likelihood differences. Points show the mean within-participant log-likelihood
difference between BRMDP(1) and the indicated benchmark. Error bars are paired participant-bootstrap 95% confidence intervals
based on 10,000 resamples. The dashed line denotes equal predictive fit; positive values favor BRMDP(1).
these quantities by MT. We then calculate the normalized BRMDP(1) likelihood shares separately for the
two benchmark comparisons (DP and MetaDP). Let ρi,Benchmark denote BRMDP(1)’s normalized per-choice
predictive-likelihood share for participant i relative to the indicated benchmark. We define
ρi,Benchmark ≡
exp

ℓ(1) BRMDP,i/(MT) 
exp

ℓ(1) BRMDP,i/(MT)  + exp  ℓBenchmark,i/(MT) ,
Benchmark∈ {DP, MetaDP}.
(W28)
Each expression exponentiates the two per-choice log-likelihoods and normalizes them to sum to one.
Consequently, a value of .5 indicates that BRMDP(1) and the relevant benchmark assign the same per-choice
predictive likelihood to participant i. Values above .5 favor BRMDP(1), whereas values below .5 favor the
benchmark. The per-choice normalization prevents the resulting shares from being driven mechanically
toward zero or one by the number of evaluated choices.
Figure W13 shows that the median normalized likelihood share lies above .5 for both comparisons in
every experimental condition. The distributions relative to MetaDP are shifted more clearly above .5, while
those relative to DP are generally closer to, but still above, the equal-fit line. Nevertheless, the median of
each distribution favors BRMDP(1). Thus, the positive mean differences in Figure W12 do not result solely
from a small number of participants with unusually large likelihood gains. Instead, BRMDP(1)’s predictive
advantage is present across a broad portion of the participant distribution. At the same time, the mass below
26

.5 indicates meaningful heterogeneity among participants.
0.450
0.475
0.500
0.525
0.550
0.575
Far Means - Low Var. Far Means - High Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
0.450
0.475
0.500
0.525
0.550
0.575
Close Means - Low Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
Close Means - High Var.
Normalized BRMDP(1) Likelihood Share
Figure W13: Participant-level distributions of normalized predictive-likelihood shares under leave-one-participant-out validation.
Each violin represents the distribution across held-out participants within one experimental condition. The embedded boxplot reports
the median, interquartile range, and conventional 1.5-IQR whiskers. The dashed line at .5 denotes equal predictive likelihood; values
above .5 favor BRMDP(1) over the indicated benchmark.
E.7.2 Validation on Future Routes
Our second out-of-sample validation method compares the policies’ ability to describe choices on future
routes. Within each experimental condition and for each participant, we estimate ϵ separately for DP,
BRMDP(1), and MetaDP using choices from the early routes 1–5. We then hold the estimated values fixed
and evaluate the policies on choices from later routes 6–10. The likelihoods for these later routes remain
conditional on each participant’s realized earlier-route history, consistent with the cross-route updating
process defined in the main analysis.
Figure W14 shows that BRMDP(1) predicts choices on routes 6–10 better than both DP and MetaDP in
27

all four experimental conditions. Similar to the previous results, the mean differences between BRMDP(1)
and both DP and MetaDP are positive in every experimental condition, and the corresponding 95% confidence
intervals lie entirely above zero (p < .01 for all mean differences). Therefore, the superior fit of BRMDP(1)
persists when we estimate the policy-noise parameter ϵ exclusively from earlier routes. This result is
particularly informative about the transfer mechanism: the coarse integration of prior uncertainty embodied
by BRMDP(1) better predicts how participants use their accumulated experience in subsequent routes than
either no transfer or fully integrated meta-learning.
0
5
Far Means - Low Var. Far Means - High Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
0
5
Close Means - Low Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
Close Means - High Var.
Mean Participant Log-Likelihood Diﬀerence
Figure W14: Predictive log-likelihood differences on future routes. Points show the mean within-participant log-likelihood difference
between BRMDP(1) and the indicated benchmark. Error bars are paired participant-bootstrap 95% confidence intervals based on
10,000 resamples. The dashed line denotes equal predictive fit; positive values favor BRMDP(1).
Participant-level distribution of predictive fit.Figure W15 presents the participant-level distributions
corresponding to the future-route mean differences in Figure W14. We use the same normalization defined
above, but calculate the predictive log-likelihoods using routes 6–10 and divide them byMT/2, the number of
choices evaluated for each participant.
The participant-level distributions reinforce the conclusions from the paired mean differences. In every
experimental condition, the median normalized likelihood share is above .5 relative to both DP and MetaDP.
The distributions relative to both DP and MetaDP are again clearly shifted above the equal-fit line. Therefore,
BRMDP(1)’s advantage in predicting future-route choices is not driven solely by a small set of participants
with large improvements. It appears across a broad portion of the participant distribution, although the density
below .5 again shows that the preferred policy varies for some participants. Taken together with the positive
28

0.3
0.4
0.5
0.6
0.7
Far Means - Low Var. Far Means - High Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
0.3
0.4
0.5
0.6
0.7
Close Means - Low Var.
BRMDP(1)− DP BRMDP(1)− MetaDP
Close Means - High Var.
Normalized BRMDP(1) Likelihood Share
Figure W15: Participant-level distributions of normalized predictive-likelihood shares on future routes. Each violin represents
the distribution across participants, and the embedded boxplot reports the median, interquartile range, and conventional 1.5-IQR
whiskers. The dashed line at .5 denotes equal predictive likelihood; values above .5 favor BRMDP(1) over the indicated benchmark.
paired mean differences, these results show that the predictive advantage of boundedly rational meta-learning
persists both on average and across participants’ later-route behavior.
E.8 No-Transfer DP with Improving Execution (DPIE)
Across-route improvement could arise without belief transfer if participants become more familiar with the
task or execute their choices more consistently. The baseline DP uses the same choice-noise parameter on
every route, so it cannot represent this form of generic improvement. We therefore consider a no-transfer DP
whose execution improves across routes.
Let ϵm denote the choice-noise parameter on route m, and denote the resulting policy by DPIE. The
policy uses the same DP action values and the same choice rule as Equation (14), but allows choice noise to
29

decline across routes:
πDP-IE m

· |sDP t

≡π DP ϵm

· |sDP t

,ϵ 1 ≥ϵ 2 ≥ · · · ≥ϵM. (W29)
Every route still begins from the independent Beta(1, 1) priors of the baseline DP, and belief updating uses
only outcomes from the current route. Onlyϵ m changes across routes.
We index each noise profile by its endpoints ( ϵ1, ϵM). For each candidate pair, we determine the
intermediate values rather than selecting a separate choice-noise parameter for every route. Specifically, we
first set
logit(eϵm) = logit(ϵ1) + log m log M  logit(ϵM)−logit(ϵ 1)  , logit(x) = log  x 1−x  , (W30)
and assign ϵm to the evaluated grid value closest to eϵm. Thus, the values between the two endpoints follow a
fixed path that is linear in log-odds against the log of the route number. The grid contains 20 equally spaced
values from .01 to .50 and 20 equally spaced values from .525 to .99. The expanded range avoids restricting
the no-transfer alternative at the main grid’s upper bound.
We use leave-one-participant-out (LOO) validation separately within each experimental condition. For
each omitted participant, we select the DPIE endpoint pair that maximizes the summed log-likelihood of all
other participants in that condition. We separately select the constant ϵ for exact BRMDP(1) on those same
training participants, and then evaluate both selected policies on the omitted participant.
DPIE Endpoints BRMDP(1) minus DPIE
Experimental Condition Meanϵ 1 Meanϵ M Mean Differencep-value
Far Means–Low Var. .507 .340 3.59<.001
(.81)
Far Means–High Var. .500 .281 3.02<.001
(.86)
Close Means–Low Var. .629 .420 2.39<.001
(.67)
Close Means–High Var. .535 .345 3.21<.001
(.70)
Table W2: Leave-one-participant-out predictive comparison of BRMDP(1) and DPIE. Bootstrap standard errors are in parentheses.
Positive differences favor BRMDP(1). The endpoint columns average the LOO-selected values of ϵ1 and ϵM across held-out-
participant folds within each condition. Standard errors and two-sidedp-values use 10,000 participant-level bootstrap resamples.
Table W2 reports the pairwise comparisons. BRMDP(1) has a higher mean predictive log-likelihood in
every condition (p < .001). The selected DPIE profile declines strictly in every fold, while no fold selects the
30

expanded upper boundary of .99. Thus, improving execution without belief transfer does not account for
BRMDP(1)’s predictive advantage within this policy class.
E.9 Non-Meta-Learning Knowledge-Transfer Benchmarks
Our main model comparison builds on the consumer-learning literature by using forward-looking dynamic
programming and spans different degrees of rationality in cross-route knowledge transfer. Accordingly, we
use meta-learning policies as a narrower set of algorithms that transfer knowledge through a bilevel approach
that learns a higher-level distribution from which each route’s parameters are generated. A natural alternative
could transfer airline-specific information across routes without maintaining a hyper-posterior. Such a policy
could pool all past outcomes or carry forward a lower-dimensional summary of them, and it could use
the resulting beliefs either myopically or in a forward-looking dynamic program. If one of these simpler
policies fits as well as BRMDP, the comparative-fit result would concern cross-route information transfer
more generally, rather than the hyper-posterior updating and sampled integration embodied in BRMDP.
To examine these possibilities, we introduce three non-meta-learning knowledge-transfer benchmarks.
The Knowledge Transfer Mean-Updating policy, denoted KTMU, pools all observations for an airline
across routes and chooses according to the resulting posterior mean. This represents the simplest form of a
knowledge transfer policy, which ignores the route changes and future choices. Theν-KTMU policy separates
the historical mean from the strength with which it is transferred, using ν as an effective prior sample size,
but remains myopic. Consequently, larger values of ν give earlier-route experience more influence over
current beliefs, whereas smaller values allow outcomes from the current route to receive more weight. The
ν-KTDP policy uses the same transferred prior as ν-KTMU and introduces forward-looking choice through
the finite-horizon Bellman recursion. None of the three policies maintains the finite hypothesis class P,
updates the hyper-posterior Qm, or draws candidate prior hypotheses. Together, they allow us to distinguish
the role of simple outcome pooling, the strength of transferred experience, and forward-looking planning
from the higher-order learning mechanism in MetaDP and BRMDP.
E.9.1 Knowledge Transfer Mean-Updating (KTMU)
KTMU is the simplest of the three benchmarks. It treats all observations for a given airline as evidence about
a single airline-specific on-time rate, pools those observations across routes, and chooses according to the
resulting posterior means. KTMU therefore transfers knowledge because earlier routes affect later choices,
but it is not a meta-learning policy under our narrower definition because it does not update a higher-order
31

belief about the distribution of route-specific parameters. It is also myopic in the sense of limited-horizon
models of sequential choice (Gabaix et al., 2006; Tehrani and Ching, 2024), current choices depend on current
posterior means alone, without a continuation value.
Pooled mean updating.For each airline k, KTMU begins with a uniform, uninformative Beta(1, 1) prior.
We define the pooled counts available before flight t on route m as
¯N+ k,m,t−1 =
m−1X
r=1
N+ k,r + N+ k,m,t−1,
¯N− k,m,t−1 =
m−1X
r=1
N− k,r + N− k,m,t−1. (W31)
Here, the bar distinguishes the counts pooled across routes from the within-route counts N+ k,m,t−1 and
N− k,m,t−1. Under KTMU, the consumer behaves as if each airline has a single route-invariant on-time rate,
denoted byθ KTMU k . This perceived rate is distinct from the environment’s true route-specific rateθ ∗ m,k. The
KTMU posterior is
θKTMU k | Im,t−1 ∼Beta  1 + ¯N+ k,m,t−1, 1 + ¯N− k,m,t−1  , (W32)
with posterior mean
ˆθKTMU k,t,m = 1 + ¯N+ k,m,t−1 2 + ¯N+ k,m,t−1 + ¯N− k,m,t−1 . (W33)
Let
GKTMU m,t = arg max k∈{1,...,K} ˆθKTMU k,t,m (W34)
denote the set of airlines with the highest pooled posterior mean. We apply the same ϵ-greedy choice-noise
rule used in the main specification:
πKTMU ϵ

ek| N+ m,t−1, N− m,t−1  = (1−ϵ) 1
n
ek∈ GKTMUm,t
o

GKTMUm,t

 + ϵ K. (W35)
Thus, total probability 1 −ϵ is assigned to the airlines with the highest posterior mean, with ties resolved
uniformly, while the remaining probability ϵ is distributed uniformly across all K airlines. In contrast to DP,
MetaDP, and BRMDP, KTMU contains no information-seeking mechanism that utilizes a continuation value.
Algorithm W5 summarizes the policy.
32

Algorithm W5Knowledge Transfer Mean-Updating Policy (KTMU)
1:Inputs:number of airlines K, routes M, flights T, and choice noiseϵ
2:Initialize once: N+ 1,0 ←0and N− 1,0 ←0
3:form = 1,. . ., Mdo
4:fort = 1,. . ., Tdo
5:For every airline k, compute
ˆθKTMU k,t,m ← 1 + ¯N+ k,m,t−1 2 + ¯N+ k,m,t−1 + ¯N− k,m,t−1
6:Set
GKTMU m,t ←arg max k ˆθKTMU k,t,m
7:Compute
πKTMU ϵ

· |N+ m,t−1, N− m,t−1 
using Equation (W35)
8:Choose
Am,t ∼π KTMU ϵ

· |N+ m,t−1, N− m,t−1 
9:Observe y m,t ∈ {0, 1}
10:Update
N+ m,t ← N+ m,t−1 + ym,teAm,t
11:Update
N− m,t ← N− m,t−1 + (1−y m,t)eAm,t
12:end for
13:ifm<Mthen
14:Carry the pooled counts into the next route:
N+ m+1,0 ← N+ m,T, N− m+1,0 ← N− m,T
15:end if
16:end for
Likelihood comparison.For estimation, we evaluate KTMU along each participant’s observed sequence
of choices and outcomes. The participant-level log-likelihood is
ℓKTMU(ϵ) =
MX
m=1
TX
t=1
logπ KTMU ϵ

Am,t | N+ m,t−1, N− m,t−1  . (W36)
We update the pooled counts using the participant’s realized history. Figure W16 adds KTMU to the likelihood
comparison for all four experimental conditions. Across every condition and throughout the displayed ϵ grid,
KTMU has a lower likelihood than every other policy. It even fits worse than the no-transfer DP benchmark,
despite carrying all past outcomes forward.
33

0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(D,h)
MetaDP
DP
KTMU
D=1
D=3
D=6
D=10
Far Means - High Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
D=1
D=3
D=6
D=10
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
D=1
D=3
D=6
D=10
Normalized Log-Likelihood
Normalized Log-Likelihood
ϵ
Figure W16: Normalized log-likelihood comparison including the Knowledge Transfer Mean-Updating policy. Each panel
corresponds to one experimental condition and reports the likelihood over 20 values of the choice-noise parameter ϵ. We set γ = 1
and h = 10 for the dynamic-programming policies and report BRMDP(D) for D∈ {1, 3, 6, 10}. BRMDP likelihood calculations use
B = 2,000 Monte Carlo samples. Within each panel, we normalize the log-likelihood as ( ℓ−ℓ min)/(ℓmax −ℓ min). Higher values
indicate a better fit.
E.9.2 Shrinkage Knowledge Transfer Mean-Updating (ν-KTMU)
KTMU gives every earlier outcome the same weight as a current-route outcome. Consequently, the amount
of information transferred to a new route grows with the number of times an airline was chosen on previous
routes. This form of transfer could severely impair performance on a route where an airline becomes the best
option after many routes of poor results. For example, if Ascend performs poorly on the first eight routes but
becomes the best airline on route nine, KTMU will react very slowly to this environmental change because
its posterior mean remains heavily weighted against Ascend. The ν-KTMU policy relaxes this restriction by
separating the historical mean for each airline from the strength with which that mean is carried into the new
route. For compactness, define the historical counts available before route m as
N+ k,<m =
m−1X
r=1
N+ k,r, N − k,<m =
m−1X
r=1
N− k,r. (W37)
For m≥2, the smoothed historical mean for airline k is
ˆθpast k,m = 1 + N+ k,<m 2 + N+ k,<m + N− k,<m . (W38)
34

The policy uses this mean to initialize the airline’s route-m Beta prior:
θ(ν) m,k | H1:m−1 ∼Beta  α(ν) k,m,β (ν) k,m  ,  α(ν) k,m,β (ν) k,m  =



(1, 1), m = 1,

ν ˆθpast k,m ,ν  1− ˆθpast k,m  , m≥2. (W39)
On the first route, before a historical mean is available, the policy therefore retains the uninformativeBeta(1, 1)
prior. On every later route, α(ν) k,m + β(ν) k,m = ν, so the parameter ν >0 is the effective prior sample size assigned
to earlier-route experience. After observing the current-route counts before flight t, the posterior mean is
ˆθ(ν) k,t,m = α(ν) k,m + N+ k,m,t−1 α(ν) k,m +β (ν) k,m + N+ k,m,t−1 + N− k,m,t−1 = ν ˆθpast k,m + N+ k,m,t−1 ν+ N + k,m,t−1 + N− k,m,t−1 , m≥2. (W40)
Thus, a smaller ν allows current-route outcomes to move beliefs more quickly, while a larger ν preserves the
influence of earlier routes for more flights. The policy remains myopic. It defines
Gν-KTMU m,t = arg max k∈{1,...,K} ˆθ(ν) k,t,m (W41)
and applies the sameϵ-greedy rule as KTMU:
πν-KTMU ϵ

ek| Im,t−1;ν

= (1−ϵ)
1
n
ek∈ Gν-KTMUm,t
o

Gν-KTMUm,t

 + ϵ K. (W42)
Thus, the ν-KTMU policy is a controlled-shrinkage generalization of KTMU, but KTMU is not nested by a
single fixed value of ν. In particular, Equation (W33) is recovered if the effective prior sample size is allowed
to vary by airline and route according to
νKTMU k,m = 2 + N+ k,<m + N− k,<m. (W43)
Fixing ν instead prevents the transferred prior from becoming mechanically more concentrated merely
because more routes have been completed.
Likelihood comparison.For either shrinkage benchmark g∈ {ν-KTMU, ν-KTDP}, the participant-level
log-likelihood is
ℓg(ϵ,ν) =
MX
m=1
TX
t=1
logπ g ϵ  Am,t | Im,t−1;ν  . (W44)
Thus, ϵ governs choice noise, while ν governs the strength of the prior transferred from earlier routes. The
likelihood is exact because ν-KTMU contains no latent route-level draw and requires only sequential posterior
updating. Figure W17 compares fixed values ν∈ {.5, 1, 5, 10} with BRMDP(1) over the same 20-point ϵ
35

grid. We denote a ν-KTMU policy with ν = ˙νas ν-KTMU( ˙ν). As in our previous results, BRMDP(1) lies
above every displayed ν-KTMU profile throughout the ϵ grid in all four conditions. Allowing the strength of
the transferred historical mean to vary therefore does not close the fit gap; within the shrinkage family, the
weaker-transfer specifications generally fit better than the stronger-transfer specifications.
0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(1)
ν-KTMU(0.5)
ν-KTMU(1)
ν-KTMU(5)
ν-KTMU(10)
Far Means - High Var.
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
ϵ
Normalized Log-Likelihood
Figure W17: Normalized log-likelihood profiles for BRMDP(1) and the myopic shrinkage benchmark. Each panel corresponds
to one experimental condition and reports the sample log-likelihood over 20 values of ϵ for fixed ν∈ {.5, 1, 5, 10}. Within
each condition, the normalization range is shared across BRMDP(1), both shrinkage-policy families, and the full evaluated grid
ν∈ {.5, 1, 2, 5, 10, 20}. Higher values indicate a better fit.
E.9.3 Shrinkage Knowledge Transfer Dynamic Programming (ν-KTDP)
Both KTMU and ν-KTMU choose directly from posterior means, so their likelihood disadvantage relative to
BRMDP could reflect the absence of forward-looking planning rather than the absence of a hyper-posterior.
The ν-KTDP policy isolates this distinction. It initializes every route with the same shrinkage prior in
Equation (W39), but uses that prior in the finite-horizon dynamic program introduced in§5.2.
36

At flight t on route m, the state is
sν-KTDP t,m =  N+ m,t−1,N − m,t−1;α (ν) m ,β (ν) m  , (W45)
where the prior vectors collect the airline-specific parameters in Equation (W39). The posterior mean ˆθ(ν) k,t,m
is given by Equation (W40). The action value satisfies
Vν-KTDP ϵ

k|N + m,t−1,N − m,t−1;α (ν) m ,β (ν) m  = ˆθ(ν) k,t,m
+γ
h
ˆθ(ν) k,t,mWν-KTDP ϵ  N+ m,t−1 +e k,N − m,t−1;α (ν) m ,β (ν) m 
+

1− ˆθ(ν) k,t,m  Wν-KTDP ϵ  N+ m,t−1,N − m,t−1 +e k;α (ν) m ,β (ν) m i . (W46)
As in the baseline DP, the corresponding state value averages over future choices induced by the same
ϵ-greedy rule:
Wν-KTDP ϵ

sν-KTDP t,m

= (1−ϵ) max
k
Vν-KTDP ϵ

k|s ν-KTDP t,m

+ ϵ K KX k=1 Vν-KTDP ϵ  k|s ν-KTDP t,m  . (W47)
The choice probability is therefore
πν-KTDP ϵ

ek|s ν-KTDP t,m

= (1−ϵ)
1
n
ek∈arg max k Vν-KTDPϵ  k|s ν-KTDPt,m o

arg maxk Vν-KTDPϵ  k|s ν-KTDPt,m 

 + ϵ K. (W48)
At the final flight, Equation(W46) reduces to the posterior mean because there is no continuation value. At the
start of the next route, the policy recomputes the historical mean and shrinkage prior from the completed-route
counts. Thus, ν-KTDP transfers airline-specific experience and values information within a route, but it never
constructsP, updates Q m, or integrates over higher-order uncertainty.
Likelihood comparison.We evaluate ν-KTDP with the same likelihood in Equation(W44). The likelihood
remains exact, but the policy additionally requires backward induction for each transferred prior. Figure W18
compares the forward-looking shrinkage specifications with BRMDP(1) over the sameϵ and ν grid used for ν-
KTMU. BRMDP(1) again lies above every displayed profile throughout the ϵ grid in every condition. Adding
a continuation value to the transferred historical mean therefore does not eliminate BRMDP(1)’s likelihood
advantage. As with ν-KTMU, weaker-transfer specifications generally fit better than stronger-transfer
specifications.
37

0.0
0.2
0.4
0.6
0.8
1.0
Far Means - Low Var.
BRMDP(1)
ν-KTDP(0.5)
ν-KTDP(1)
ν-KTDP(5)
ν-KTDP(10)
Far Means - High Var.
0.1 0.2 0.3 0.4 0.5
0.0
0.2
0.4
0.6
0.8
1.0
Close Means - Low Var.
0.1 0.2 0.3 0.4 0.5
Close Means - High Var.
ϵ
Normalized Log-Likelihood
Figure W18: Normalized log-likelihood profiles for BRMDP(1) and the forward-looking shrinkage benchmark. Each panel
corresponds to one experimental condition and reports the sample log-likelihood over 20 values of ϵ for fixed ν∈ {.5, 1, 5, 10}.
We set γ = 1 and h = 10 for both dynamic-programming policies. The normalization follows Figure W17, so the vertical scale is
common across the two figures within each condition. Higher values indicate a better fit.
Taken together, the three benchmarks narrow the interpretation of the main result. BRMDP(1)’s advantage
is not explained by cross-route transfer alone, by calibrating the strength of a transferred historical mean,
or by combining that mean with forward-looking planning. The data instead favor the boundedly rational
representation of higher-order uncertainty embodied in BRMDP(1) over these lower-dimensional forms of
knowledge transfer.
38

Web Appendix F: Stylized Managerial Counterfactuals
This appendix provides stylized counterfactuals that illustrate the managerial implications discussed in §7.
These examples are not estimated market outcomes from our laboratory task. Instead, they are simple
numerical illustrations of how the paper’s preferred behavioral model can imply different firm policies than
DP or MetaDP when consumer behavior is closer to BRMDP(1).
F.1 Stylized Counterfactuals for Pricing and Promotion
Consider a first-purchase decision on a new route or in a new category for a focal brand. Normalize the
outside option and marginal cost to zero, and suppose the consumer buys if expected quality exceeds price:
u = ˆθ−p, buy if ˆθ≥p. (W49)
Interpret market demand as the share of otherwise identical consumers who face the same prior history.
For transparency, suppose the consumer’s hyper-posterior is formed on two hypotheses:
HH :θ∼Beta(8, 2) (µ H = .8), H L :θ∼Beta(4, 6) (µ L = .4), (W50)
with initial hyper-prior Q1(HH) = Q1(HL) = .5. Under DP, consumers treat the new route as unrelated and
start from the uninformative prior Beta(1, 1), so expected quality is .5. Under MetaDP, all consumers use the
integrated posterior mean .8QH + .4QL. Under BRMDP(1), a fraction QH of consumers behave as if they
drew HH, while a fraction QL behave as if they drew HL. Therefore, launch demand is
qDP(p) =1{p≤.5}, (W51)
qMetaDP(p) =1{p≤.8Q H + .4QL}, (W52)
qBRMDP(1)(p) = QH 1{p≤.8}+ Q L 1{p≤.4}. (W53)
The key point is that
E
h
1{ˆθ≥p}
i
̸=1
n
E[ˆθ]≥p
o
, (W54)
so a firm that collapses heterogeneous coarse priors into one representative posterior can choose the wrong
price or promotion.
Example 1: after strong favorable experience, DP underprices.Suppose the focal brand performed very
well on the previous route, generating two on-time flights out of two. This history shifts posterior weight
39

toward the high-quality hypothesis:
QH = .783, Q L = .217.
The firm is now choosing a launch price for the new route. DP ignores cross-route transfer and therefore
recommends a conservative introductory price, while MetaDP and BRMDP(1) both imply stronger demand.
Under true BRMDP(1) behavior, however, the profit-maximizing price is even higher because the market
contains a large high-belief segment rather than a single representative consumer.
Table W3: Pricing after strong favorable experience
Observed history Posterior weights Firm action True BRMDP(1) out-
come
Interpretation
Previous route yields
2/2 successes
QH = .783, Q L = .217 DP setsp= .50
MetaDP setsp=
.713
BRMDP(1)-
optimal price
isp= .80
Atp= .50, true profit
is .392
Atp= .713, true profit
is .558
Atp= .80, true profit
is .626
DP underprices
because it ignores
transferable learn-
ing. Even MetaDP
underprices because
it smooths the
high-belief segment
into an average
posterior.
To see the BRMDP(1) logic directly, note that demand on the new route is
qBRMDP(1)(p) =



1, p≤.4,
.783, .4<p≤.8,
0, p>.8.
Hence true profit, π(p) = p qBRMDP(1)(p), is maximized atp= .8. The managerial implication is that a
no-transfer model can make the firm too conservative precisely when prior experience should justify more
aggressive monetization.
Example 2: after mixed experience, MetaDP rejects a profitable coupon.Now suppose the prior route
generated mixed evidence: one on-time and one delayed. This history leaves substantial posterior weight on
both hypotheses:
QH = .4, Q L = .6.
The firm starts from a list price ofp= .56, which is the price suggested by MetaDP because the integrated
posterior mean is .8(.4) + .4(.6) = .56. The managerial question is whether to offer a launch coupon of .16,
40

reducing the effective price to .40. Under MetaDP, the coupon appears unnecessary because the representative
consumer already buys atp= .56. Under BRMDP(1), by contrast, the coupon is profitable because it brings
the low-prior segment into the market.
Table W4: Promotion decision after mixed experience
Observed history Posterior weights MetaDP recommen-
dation
True BRMDP(1)
outcome
Interpretation
Previous route yields
1 on-time and 1 de-
layed
QH = .4, Q L = .6 Set list pricep= .56
and reject the coupon
Atp= .56, true de-
mand is .4 and rev-
enue is .224
With a coupon, effec-
tive price becomes
.40, true demand
rises to 1, and rev-
enue rises to .40
MetaDP rejects a
profitable promotion
because it averages
away the low-prior
segment that BR-
MDP(1) preserves.
Under BRMDP(1), demand in this case is
qBRMDP(1)(p) =



1, p≤.4,
.4, .4<p≤.8,
0, p>.8.
So at the MetaDP list pricep= .56, only the high-prior segment buys. A coupon that reduces the effective
price to .40 activates the full market. The managerial implication is that full integration can make the firm too
aggressive on price and too reluctant to use targeted launch promotions.
These examples are stylized, but the broader implication is general. When consumers transfer beliefs
across contexts using coarse sampled priors, managers should expect launch demand to look more like a
mixture of segments than a single representative-consumer curve. As a result, the direction of the policy
error need not be constant: DP can under-react after strong favorable experience, while MetaDP can over- or
under-react depending on the decision threshold. This cautions against using either no-transfer DP or fully
integrated MetaDP as the default basis for pricing and promotion counterfactuals.
F.2 Stylized Counterfactuals for Route-Entry Interventions
We next illustrate the managerial implications of the model comparison with two stylized counterfactuals
that stay close to our experimental task. Both focus on the beginning of a new route, when consumers have
little route-specific information but may transfer beliefs from prior routes. Specifically, we consider two
41

route-entry decisions: whether to feature a focal airline as the recommended option on the first flight, and
whether to encourage an early trial of that airline through a one-time intervention.
This subsection is explicitly a misspecified-forecasting exercise. Consistent with the likelihood results,
we take consumers’ true behavior to be BRMDP(1). The manager, however, does not know this and instead
chooses route-entry interventions as if consumers followed either DP or MetaDP. The purpose of the examples
below is therefore to show how a manager can make the wrong decision when the behavioral model used for
forecasting is misspecified.
We focus on the beginning of a new route, which is the part of the task where cross-route priors matter
most. Let airline A denote the focal airline and B the best competing airline. Let z∈ {0, 1} denote a
route-entry intervention chosen by the manager. When z = 1, the intervention adds utility b> 0 to choosing
airline A on the first flight of the new route. Depending on the example, this intervention can be interpreted
as featured placement or a one-time trial credit. Let rB denote the route-entry utility of the best competing
airline B. A consumer chooses airline A on the first flight iff
ˆθA + zb≥r B. (W55)
If airline A earns margin m from a first-flight booking and the intervention costs c per customer, then the
manager’s payoff is
Π(z) = m q(z)−cz, (W56)
where q(z) is the share of consumers who choose airline A on the first flight. A manager who assumes model
M∈ {DP, MetaDP}chooses
zM ∈arg max
z∈{0,1}
ΠM(z), (W57)
whereas the correct decision is
zBRMDP(1) ∈arg max
z∈{0,1}
ΠBRMDP(1)(z). (W58)
For simplicity, we focus on first-flight acquisition value. Adding continuation value from later flights would
strengthen the same logic, because early-route choices affect subsequent learning within the route.
To keep the exposition transparent, we again use the two-hypothesis representation of transferred beliefs
about airline A:
HH :θ A ∼Beta(8, 2) (µ H = .8), H L :θ A ∼Beta(4, 6) (µ L = .4). (W59)
42

Let QH and QL denote the current hyper-posterior weights on HH and HL. Then route-entry demand for
airline A is
qDP(z) =1{.5 + zb≥r B}, (W60)
qMetaDP(z) =1{(.8Q H + .4QL) + zb≥r B}, (W61)
qBRMDP(1)(z) = QH 1{.8 + zb≥r B}+ Q L 1{.4 + zb≥r B}. (W62)
The key nonlinearity is that
E
h
1{ˆθA + zb≥r B}
i
̸=1
n
E[ˆθA] + zb≥r B
o
. (W63)
This is exactly why a manager using MetaDP can choose differently from a manager who correctly recognizes
that consumers behave according to BRMDP(1).
The two examples below isolate different misspecifications. Example 1 shows how a manager who
assumes DP can overinvest in route-entry support because DP ignores transferred beliefs that consumers
already carry into the new route. Example 2 shows how a manager who assumes MetaDP can underinvest in
a trial incentive because MetaDP averages away a responsive high-prior segment.
Example 1: assuming DP leads the airline to overinvest in featured placement.Suppose airline A
generated two on-time flights out of two on the previous route. This shifts posterior weight toward the
favorable hypothesis:
QH = .783, Q L = .217.
Consider a featured-placement intervention with bonus b = .25, competing-airline utility rB = .60, first-flight
margin m = .10, and per-customer cost c = .05. A manager who assumes DP predicts that without featured
placement no consumer chooses airline A, while with featured placement all consumers do. Under true
BRMDP(1) behavior, however, a large share of consumers already chooses airline A even without the
intervention because favorable experience from the earlier route carries over.
Thus, a manager using DP chooses zDP = 1, while the correct decision under BRMDP(1) is zBRMDP(1) =
0. The error arises because DP ignores the favorable beliefs consumers already transfer into the new route
and therefore overstates the value of paying for route-entry support.
43

Table W5: Manager assumes DP, but consumers follow BRMDP(1)
Intervention Predicted share un-
der DP
Actual share under
BRMDP(1)
Predicted payoff un-
der DP
Actual payoff under
BRMDP(1)
z = 0: no
featured place-
ment
qDP(0) = 0 q BRMDP(1)(0) = .783 .10×0 = 0 .10×.783 = .078
z = 1:
featured
placement
qDP(1) = 1 q BRMDP(1)(1) = 1 .10×1−.05 = .05 .10×1−.05 = .05
Example 2: assuming MetaDP leads the airline to underinvest in a trial credit.Now suppose airline A
generated a mixed prior-route experience: one on-time and one delayed. This yields
QH = .4, Q L = .6.
Consider a one-time trial credit with bonus b = .05, competing-airline utility rB = .82, first-flight margin
m = .10, and per-customer cost c = .02. Under MetaDP, the integrated route-entry belief about airline A is
.8(.4) + .4(.6) = .56,
so even with the credit the representative consumer still does not choose airline A. A manager using MetaDP
therefore rejects the intervention. Under true BRMDP(1) behavior, however, the credit is enough to move the
high-prior segment, even though it does not move the low-prior segment.
Table W6: Manager assumes MetaDP, but consumers follow BRMDP(1)
Intervention Predicted share under
MetaDP
Actual share under
BRMDP(1)
Predicted payoff un-
der MetaDP
Actual payoff under
BRMDP(1)
z = 0: no trial
credit
qMetaDP(0) = 0 q BRMDP(1)(0) = 0 .10×0 = 0 .10×0 = 0
z = 1: trial
credit
qMetaDP(1) = 0 q BRMDP(1)(1) = .4 .10 × 0 − .02 = −.02 .10×.4−.02 = .02
Hence, a manager using MetaDP chooses zMetaDP = 0, while the correct decision under BRMDP(1)
is zBRMDP(1) = 1. The error arises because MetaDP compresses the market into a single representative
consumer and therefore misses a responsive high-prior segment that is profitable to target with a small trial
incentive.
Taken together, these examples show that the managerial problem is one of behavioral misspecification.
The underlying consumer behavior is BRMDP(1), but a manager who assumes either DP or MetaDP
44

can choose the wrong route-entry intervention. The direction of the mistake depends on the source of
misspecification. Assuming DP can make the manager overinvest in route-entry support because it ignores
transferred beliefs consumers already have. Assuming MetaDP can make the manager underinvest in targeted
interventions because it averages away coarse segment structure. More broadly, when behavior is closer to
BRMDP(1), managers should evaluate route-entry policies using a mixture of coarse transferred priors rather
than a no-transfer benchmark or a fully integrated representative-consumer benchmark.
45

Web Appendix G: Environment Check
We calculate the means and variances of the generated data and report them in Table W7 to verify that
the environment produces distributions close to the theoretical targets. The empirical statistics show that
participants faced conditions that are close to the theoretical ones we intended.
Condition
(target means; variance)
Lower Airline Middle Airline Higher Airline
Mean Var. Mean Var. Mean Var.
Far Means–Low Var.
(.2, .5, .8); .02 .201 .020 .499 .020 .799 .019
Far Means–High Var.
(.2, .5, .8); .04 .191 .038 .506 .038 .799 .039
Close Means–Low Var.
(.4, .6, .8); .02 .412 .019 .606 .019 .800 .021
Close Means–High Var.
(.4, .6, .8); .04 .404 .041 .605 .039 .810 .035
Table W7: Comparison of generated and theoretical means and variances across airlines under different parameters.
46
