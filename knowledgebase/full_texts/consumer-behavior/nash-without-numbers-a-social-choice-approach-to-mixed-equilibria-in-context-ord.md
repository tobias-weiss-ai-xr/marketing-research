---
title: 'Nash without Numbers: A Social Choice Approach to Mixed Equilibria in Context-Ordinal Games'
url: https://arxiv.org/abs/2605.07996
category: consumer-behavior
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Ian Gemp
- Crystal Qian
- Marc Lanctot
- Kate Larson
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.07996
pages: 28
chars: 85623
fetched_at: '2026-11-08T13:03:34+00:00'
kb_version: 1
---

# Nash without Numbers: A Social Choice Approach to Mixed Equilibria in Context-Ordinal Games

Nash without Numbers: A Social Choice Approach to
Mixed Equilibria in Context-Ordinal Games
Ian Gemp
Google DeepMind
New York, NY , USA
imgemp@google.com
Crystal Qian
Google DeepMind
New York, NY USA
cjqian@google.com
Marc Lanctot
Google DeepMind
Montreal, CA
lanctot@google.com
Kate Larson
Google DeepMind &
University of Waterloo
Waterloo, CAN
katelarson@google.com
Abstract
Nash equilibrium serves as a fundamental mathematical tool in economics and
game theory. However, it classically assumes knowledge of player utilities, whereas
economics generally regards preferences as more fundamental. To leverage equi-
librium analysis in strategic scenarios, one must first elicit numerical utilities
consistent with player preferences, a delicate and time-consuming process. In this
work, we forgo precise utilities and generalize the Nash equilibrium to a setting
where we only assume a player is capable of providing anordinalranking of
their actions within thecontextof other players’ joint actions. The key technical
challenge is to rethink the definition of abest-response. While the classical defi-
nition identifies actions maximizing expected payoff, we naturally look towards
social choice theory for how to aggregate preferences to identify the most preferred
actions. We define this generalized notion of acontext-ordinalNash equilibrium,
establish its existence under mild conditions on aggregation methods, introduce
notions of regularization, approximation, and regret, explore complexity for sim-
ple settings, and develop learning rules for computing such equilibria. In doing
so, we provide a generalization of Nash equilibrium and demonstrate its direct
applicability to elicited preferences in human experiments.
1 Introduction
Game theory seeks to define rational (utility-maximizing) behavior in the presence of rational co-
players. However, not all strategic scenarios admit precise numerical utilities. In elections, for
instance, voters may strategically cast ballots in order to achieve desired election results. One can
imagine pursuing tactical voting without ever ascribing any precise numerical value to each electoral
outcome. We later study human data from such settings in experiments.
The dominant solution concept in game theory is the notion of a Nash equilibrium (NE), a strategy
profile from which no single player has any incentive to deviate [50]. Traditionally, an incentive to
deviate would mean that a player has an opportunity to take an action that achieves higher expected
utility. However, how can one compute anexpectedutility in a setting where numerical utilities are
not available?
Instead of assuming access to numerical utilities, one can more generally assume each player is
capable of ranking the possible outcomes [24]. Given the other players play a deterministic strategy,
Preprint.
arXiv:2605.07996v1  [cs.GT]  8 May 2026

25%
30%
45%
{
 ≻
 ≻
 }{
 ≻
 ≻
 }
{
 ≻
 ≻
 }Opp. Strategy
Our vote
when opp.
plays
Figure 1: An NE is a strategy profile where each player best responds to its co-players. In a game
without payoffs, but where players can rank their actions, we use social choice (voting) theory to
define a best response. Consider playing an opponent in rock-paper-scissors (
 ,
 ,
 ); their mixed
strategy is [25%,30%,45%] . When the opponent plays, e.g.,
 , our rank vote over our own actions
is {
 ≻
 ≻
 }. Imagine a population of votes with representation proportional to the opponent’s
mixed strategy—25% of the votes are {
 ≻
 ≻
 }, 30% are {
 ≻
 ≻
 }, etc. We define a best
response as the outcome of a voting rule on this population. For example,Bordaelects
 as our best
response.
a rational player would simply deviate to the action that results in the outcome they most prefer.
Any utility function onemightelicit through careful measurement would also achieve its maximum
for that action, and so we can still consider the player to be utility-maximizing despite the lack
of utilities. Unfortunately, it is unclear how to translate this notion in the case where co-players’
strategies are mixed (i.e.,randomized). Previous work has either switched from using probability
theory topossibilitytheory [ 6] or introduced an additional, disinterested player to recover a mediated
equilibrium [23]. Neither is able to recover a Nash equilibrium under a traditional probabilistic
framework.
A critical obstacle towards defining a Nash equilibrium in this setting is how to aggregate ordinal
outcomes under mixed (probabilistic) strategies. In this work, we look towards a field that has
spent centuries studying the problem of preference aggregation, a veritable “mathematics without
numbers” [40], namelysocial choice theory. With this viewpoint, we successfully construct a notion
of a mixed Nash equilibrium called acontext-ordinalNash equilibrium that generalizes the classical
definition. An example of a context-ordinal equilibrium is depicted and explained in Figure 1.
Given this new definition, many questions emerge. We establish its existence under mild conditions
on aggregation (voting) rules, introduce notions of regularization, approximation, and regret, study
complexity for simple settings, and develop learning rules for computing such equilibria. In doing so,
we provide a generalization of Nash equilibrium that can be directly applied to elicited preferences,
thefundamental data of human interactions, which we demonstrate in two experiments: (i) general
agent evaluation in Arcade, and (ii) empirical analysis of ranked-choice human leader selection (Lost
at Sea, [15, 54]).
2 Background & Related Work
First, we review background on classical non-cooperative game theory, social choice, and prior
models of equilibria assuming access to only player preferences.
2.1 Non-Cooperative Game Theory
A classical normal-form game (NFG) is a tuple ⟨N,A= (" n i=1 Ai), u= (u 1, . . . , un)⟩ where
N={1, . . . , n}is the set of players, Ai is player i’s finite set of actions, and ui :A →R
is player i’s utility function. Players may randomize over their action sets, that is, playmixed
strategies: Xi = ∆Ai. Their utility functions naturally extend to this domain using expected value:
ui :X= (" n j=1 Xj)→R=E a∼x[ui(a)] where x∈ X and a∈ A. Let x−i denote the mixed
strategy profile for players noti.
2

A Nash equilibrium (NE) is a profile x from which no player has any incentive to deviate: ui(x)≥
ui(z, x−i)∀i, z∈ Xi. Equivalently, each player’s strategy is a best response:
xi ∈BR i(x−i) = arg max
z∈Xi
ui(z, x−i)∀i.(1)
2.2 Social Choice (Voting) Theory
Much of social choice theory studies procedures for aggregating voter preferences over alternatives
such that desirable axioms are satisfied [18]. The syntax a≻a ′ indicates a voter strictly prefers a to
a′; a⪰a ′, weakly prefers. A voter is indifferent between the two if a′ ⪰a and a⪰a ′, abbreviated
a∼a ′. Each voter specifies all their preferences with a preference relation ρ. The set of all possible
preference relations over a set of alternativesAisP(A).
A voting rule that determines the “winner(s)” (a non-empty subset, possibly with ties), is a social
choice function (SCF). One that returns a ranking over the alternatives is a social welfare function
(SWF). An SWF can be converted to an SCF by selecting the subset that achieves the top-rank. A
probabilistic SCF (pSCF) returns a distribution (lottery) over alternatives. An SCF can be converted to
a pSCF by converting its output to a lottery with probability mass only on the winners. In addition, we
assume a voting rule can take as input a lottery over possible votes, rather than the actual set of voters’
votes. For example, if the set of votes is ({a≻a ′},{a≻a ′},{a≺a ′}) for three voters and two
alternatives a and a′, then a voting rule can also accept the lottery [2/3 :{a≻a ′},1/3 :{a ′ ≻a}] .
We call thesedoublyprobabilistic SCFs (Def. 2). For intuition, we sometimes explain this concept
using an infinite population of votes, each distinct vote (ballot) occurring with a given frequency. For
example, Fig. 1 shows ballot{
 ≻
 ≻
 }occurring in30%of votes.
2.3 Ordinal Games and Equilibria
Ordinal games[ 24] forgo numerical payoffs and instead assume each player can rank all joint
outcomes, e.g., player 1 of 2 would rank (R, S)∼(S, P)∼(P, R)≻(R, R)∼(P, P)∼... in
rock-paper-scissors. Cruz and Simaan [24] proposed a notion of approximate equilibrium for2-player
ordinal games parameterized byorder {m, n}, indicating that player 1 (2) seeks their mth (nth)
ranked action when deviating. A traditional pure strategy NE in an ordinal game is equivalent to a
{1,1}-NE; such an NE is not guaranteed to exist though.
Conitzer [23] raises the issue of defining mixed NE in ordinal games and conjectures that it “cannot
be done without access to cardinal utilities”. Instead, Conitzer [23] leverages the folk theorems in
infinitely repeated games to construct an equilibrium that is consistent with both repeated games and
mediated games. This mediated equilibrium is specified with a joint distribution x and correlated
co-player distribution x−i for every player i. These equilibria are proven to be robust in the sense
that for any utility function that satisfies the ordinal constraints of the game, the pair x and (x−i)i
remains a mediated equilibrium.
Other work defines mixed strategies in terms ofpossibilitydistributions rather than probability
distributions [6]. A possibilistic mixed strategy maps each action to an ordinal scale that can be
interpreted as a preference or likelihood toward playing that action. A corresponding mixed NE can
then be defined in terms of mixed possibilistic strategies.
In contrast to the mediated equilibrium, we aim to define a single factorized equilibrium profile
x= (x 1, . . . , xn). And in contrast to the possibilistic framework, we will define mixed strategies
traditionally as probability distributions. In addition, it is unclear how any of the frameworks
above might handle noisy ordinal preferences, a practically important scenario we explore later in a
stochastic Condorcet election domain.
Lastly, both frameworks assume the ordinal game (OG) setting [ 24], which we argue 1) is over-
specified for the purposes of defining a suitable NE concept and 2) is unnatural when a player’s
actions are incomparable under different co-player action profiles (see Sec 5.1).
3 Context-Ordinal Games & Equilibria
To ascertain if a player would want to alter their strategy from a purported equilibrium, we only need
to look at their possible choices, assuming their co-players’ strategies remain fixed. In particular, it
3

isnotessential, as in an OG, to know how a player i might want their co-players to change their
strategies to benefit them (i). This leads us to the idea of acontext-ordinal game(COG), where each
player ranks possible outcomes given actions chosen by everyone else. We encourage the reader to
consult Fig. 1 before continuing.
Definition 1(Context-Ordinal Game).Acontext-ordinal game(COG) is a tuple ⟨N,A=
("n i=1 Ai), ρ⟩where N={1, . . . , n}is the set of players, Ai is player i’s finite set of ac-
tions, and ρ={ρ 1, . . . , ρn} contains each player’s conditional preference relation. Each
ρi :" n j̸=i Aj → P(Ai)maps the co-players’ joint action to playeri’s preferences overA i.
For a strategy profile to be a Nash equilibrium, each player’s strategy must be a best response to
the remaining players. We generalize the arg max in (1) to mean any distribution over the player’s
actions that “tie” for top-ranked according to a social choice rule (a doubly pSCF).
Definition 2(Doubly Probabilistic SCF).A doubly pSCF (dpSCF) is a correspondence ν: ∆ P(A i) →
2∆Ai from a lottery over votes to a convex set of distributions over actions.
The next definition is the key to defining our mixed Nash equilibrium concept.
Definition 3(Best Response with Social Choice).Player i’s co-players play a−i with probability
x−i(a−i). For each a−i played, player i conditionally specifies preferences ρi(a−i) over their
actions Ai, referred to as a “vote”1. Let vi(x−i) be the resulting population of votes where each vote
ρi(a−i), occurs with probability x−i(a−i). Player i’s best response, BRi(x−i), is the result of the
dpSCF voting ruleν i on this population of votes.
The following NE definition is standard. Our primary innovation is Def. 3 of a best response.
Definition 4(Context-Ordinal Nash Equilibrium).A strategy profile x is a context-ordinal Nash
equilibrium (CO-NE) iffx i ∈BR i(x−i)for all i.
In words, x is an NE if every player’s mixed strategy only places mass on winning candidate actions.
See Appx. A.3 for a definition of a correlated equilibrium.
Our definition is naturally robust to mis-specification of utilities (assuming they exist), a key focus
of [23]. The underlying utilities are allowed to change as long as the partial ranking of actions does
not. Because our definition only observes the partial ranking, the NE is invariant to these changes in
utility.
3.1 Existence of Mixed Context-Ordinal NE
The social choice best response operator BRi for each player i maps from a partial profile x−i to a
non-empty, convex subset of the simplex. Denote upper hemicontinuous by u.h.c.
Theorem 1(Kakutani 1941).If eachBR i is u.h.c., then an NE exists in mixed strategies.
A set-valued mapping BRi is u.h.c. if for every convergent sequence of co-player strategies {xt −i}t,
e.g., the distribution over votes illustrated in Fig. 1, and for any convergent sequence of player i’s
best responses{x t i}t withx t i ∈BR i(xt −i), thelim t→∞ xt i lies inBR i(limt→∞ xt −i).
Traditional SCFs may exhibit discontinuities in their elected candidates as the population of votes
slightly changes. By considering the distributions returned by dpSCFs, we can more naturally study
their u.h.c. properties. The u.h.c. definition handles subtleties that arise, for example, when the
distribution of votes changes from one that prefers candidate A to one in which candidate A and B
are tied. In the latter case, any distribution over A and B is valid and samples a suitable winning
candidate: BRi(limt→∞ xt −i) = [z,1−z], z∈[0,1] . And if the limit of the winning candidate
distribution specifically selected A (limt→∞ xt i = [1,0] ), that would still satisfy the u.h.c. condition
because A is in the set of valid candidate distributions.
We identify several u.h.c. families of voting rules: a) score voting where each vote assigns candidates
numerical scores and the candidate with highest (x−i-weighted) score wins, b) positional voting [56],
e.g., Borda counts, c) probabilistic voting [ 17], e.g., maximal lotteries [ 30, p. 30], d) and social
grading functions [10]. Scoring and positional voting rules induce normal-form games. Classical NE
implicitly uses score voting (see Appx. A.2) where voters score candidate actions with their precise
1If preferences are stochastic, the vote itself may be represented as a lottery over votes.
4

1.ˆx−i ∼Dir

1+ 1 q x−i 
2.
 ∼Cat(µ i)
3. H ∼Bern(p)
22%
31%
47%
{
 ≻
 ≻
 }
{
 ≻
 ≻
 }
vu={
 ≻
 ∼
 }
{
 ≻
 ≻
 }
T
H
T
Figure 2: Algorithm 1 applied to the example from Fig. 1.Step 1:Original co-player strategy x−i =
[25%,30%,45%] is perturbed via ˆx−i ∼Dir(1+ 1 q x−i), yielding [22%,31%,47%] ; as q→0 ,
ˆx−i →x −i.Step 2:A usurper action u=
 is sampled from Cat(µi), giving vu ={
 ≻
 ∼
 }
with
 top-ranked and all others tied.Step 3:Each vote is independently replaced by vu with
probability p (coin flip). When p= 0 the population is unchanged; when p= 1 all votes become vu.
A voting rule νi determines a best response from this perturbed population. Results are averaged over
trials to obtain the finalregularizedbest response.
payoffs. Later we introduce regularized best responses, rendering any dpSCF voting rule u.h.c. and
ensuring existence of their NE.
Complexity of CO-NEIn Appx. D, we study complexity of CO-NE and show that there exist
intuitively adversarial 2-player games that when studied under simple voting rules (e.g., Borda
counts) map to normal-form games that are not zero-sum. The implication is that CO-NE are not
polynomial-time computable. Whereas prior work sought to define equilibria of ordinal games that lie
in P at the expense of a departure from traditional representation, our aim is to define an equilibrium
notion that generalizes Nash: probabilistic, factorizes, and gracefully reduces to classical NE under
assumptions, e.g., score voting where score=utility.
4 Learning and Approximation
Gradient descent serves as the workhorse of learning in games. Its interpretation as a proximal
operator is important here because it allows us to view (projected) gradient descent as the solution to a
regularized optimization problem. This view appears in related algorithms like follow the regularized
leader [48, 59] and mirror descent as well [11]:
x′ i = ΠXi [xi +η∇ xi ui(xi, x−i)] = arg max
z∈Xi
ui(z, x−i)− 1 2η ||z−x i||2 (2)
where x′ i denotes the next iterate, ΠXi denotes the Euclidean projection onto the setXi, and η is a step
size parameter (equiv., inverse regularization coefficient). Convergence of gradient descent is typically
analyzed in terms of the successive distance between iterates,||x′ i −x i||. Notice that in unconstrained
settings when the projection operator acts as an identity, this simplifies to ||η∇xi ui(xi, x−i)|| and is
hence proportional to the norm of the gradient. Gradient norms are used as both performance metrics
and constructing loss functions to develop other algorithms [33]. It should not come as a surprise
then that our first task is to replicate a technique to regularize our best response definition. Doing
so will provide us with methods for learning as well as metrics to measure performance of those
learning algorithms.
4.1 Regularization of Best Responses
Regularization is a useful tool in game theory for selecting equilibria [47, 36], aiding convergence [52],
imitating target play [ 34, 8], and online learning (FTRL) [ 57]. An exemplar is KL-divergence:
KL(µ∥x) = P A µ(a) log(µ(a)/x(a)), which measures how much an approximate distribution x differs from a true distribution µ. The reverse KL, KL(x∥µ) was used in [7] to regularize learned
strategies in Diplomacy towards recorded human play.
Given that COGs lack utilities, making how to achieve direct regularization unclear, we take the
approach of regularizing via random perturbation. LetBR(p,q,µi) i denote the regularized best response
5

operator parameterized by target distribution µi ∈∆ Ai, perturbation hyperparameter q≪1 , and
regularization strengthp∈[0,1]. We setµ i = 1/|Ai|1always.
A regularized best-response in COGs should satisfy the following desiderata for everyx −i:
(C1) Maximum regularization (p= 1) results inµ i for any target distributionµ i;
(C2) Zero regularization (p= 0) returns an element ofBR i from Def. 3;
(C3) Any regularization results in a single-valued best response;
(C4) The regularized best response is a continuous function ofx −i.
For clarity, we use a concrete example in Fig. 2 to describe our approach which satisfies the above
conditions and defer Algorithm 1 and a more rigorous discussion to Appx. B.
Next, we will leverage regularization to construct notions of approximation and regret in COGs. Later
in Section 5, we also use it to construct algorithms, e.g., FTRL, to approximate context-ordinal Nash
equilibria in experiments. Appx. F reviews learning algorithms.
4.2 Performance Metrics
Approximate Nash equilibria are most often judged on how much any player can gain by deviating,
referred to asexploitability,ϵ= max i ϵi, where:
ϵi(x) = max
z∈∆Ai
ui(z, x−i)−u i(x),(3)
and ϵi is sometimes referred to asimmediateregret. That is because of the tight connection between
game theory and online learning [ 35]. (External) regret for a sequence of strategies [xi,t]t∈[1,T]
measures exploitability over T rounds of play: maxz∈∆Ai
PT
t=1 ui(z, x−i,t)−u i(xt). COGs do not provide utilities so we explore alternative notions of approximation and regret.
4.2.1 Strategy Space
We can measure a distance to NE in strategy space asϵ= max i ϵi,
ϵi(x) = min z∈BRi(x−i) D(z, xi)(4)
and D is continuous and non-negative. For example, D could be earth mover’s distance which results
inϵ i summing the amount of probability mass that playerihas placed on strictly losing candidates.
As defined, this function may be discontinuous because of jumps in the u.h.c. best response set BRi.
We can replace the feasible set by theregularizedbest response BR(p,q,µi) i which is continuous. By
Berge’s maximum theorem [5, Theorem 17.31],
ϵ(p,q,µi) i (x) = min
zi∈BR
(p,q,µi )
i (x−i)
D(zi, xi)(5)
is continuous in x. Figure 5 in Appx. E illustrates this measure for the classic Chicken game. While
this measure is suitable for immediate regret, it is unclear how to extend it to regret which evaluates a
sequence of strategies.
4.2.2 Meta-Game Analysis
Another choice directly asks “would you prefer to have played a fixed z∗ i in hindsight?” To define the
best fixed z∗ i in hindsight, simply collect all the “votes” generated at each round t by the co-players
in proportion to their strategies x−i,t. Use the (dpSCF) voting rule to aggregate the votes across all
rounds and return the best probabilistic strategyz ∗ i .
To measure the regret, consider the same sequence of co-player strategies as before, but apply the
voting rule, only considering the hindsight and online actions in proportion to their appearance in their
mixed strategies. For example, if at t=t ′, z∗ i = [1,0] and xi,t′ = [0.5,0.5] , in proportion to each
a−i ∼x −i played at time t′, generate two votes with equal representation: the first action compared
against itself and the first action against the second. As before, collect all of the generated votes and
6

(a) Exploitability
 (b) Hindsight Winrate
Figure 3: We evaluate our (SGF-based) FTRL approach ( ps indicates thesolver’s BR(ps,q,µi) i pa-
rameter) on the Atari evaluation game according to the metrics in Section 4.2. (a) EMD as defined
in Section 4.2.1 with p= 0 , eqn. (5); (b) Hindsight winrate from Section 4.2.2. Panel (b) sets
ps = 1/t+ 1. FTRL can also be considered asmoothed-FP approach [29].
apply the voting rule (equiv. best response operator BRi) to determine the winner. We present the
probability of hindsight being selected byBR (p,q=0.1,µi=[1/2,1/2]) i in Figure 3b over iterations.
In Appx. E.2, we explore one more additional metric derived from the social choice perspective,
namelymargin of victory, which measures the proportion of votes ( x−i) that must be altered for a
given strategyx i to become a best responsex i ∈BR i(x−i).
4.3 Approximating Classical Nash Equilibria
The focus of this work is on games with only revealed ordinal preferences. Nevertheless, one might
still hope to approximate a classical NE of the game that is defined byhiddencardinal utilities. We
obtain non-trivial approximation bounds for that setting by appealing to results from the study of
distortionwithin social choice. Let ui ▷ρ i mean any utility ui consistent with preferences ρi. Then
the (additive+) distortion of a voting ruleν i,
d+(νi) = max ρi,x max ui▷ρi [ui(x)−u i(BRi, x−i)],(6)
captures the cost of electing candidates using ordinal information instead of voters’ more nuanced
cardinal utilities (ordinal information is assumed consistent with utilities).
It is typically assumed that each voter attributes cardinal utilities to candidates such that they are
non-negative and sum-to-1, “one person, one vote” [53]. This property does not generally hold in
games—a player’s payoffs do not sum-to-1 under each possible co-player action a−i. Nevertheless,
equilibria are invariant to affine transformations of payoffs, so we can shift and scale each player’s
payoffs such that they are all non-negative with positive sum. This still leaves varying payoff-sums
(s), but we can recover a bound on the suboptimality of the best responses computed using voting
rules versus expected payoff maximization.
Theorem 2.Let νi be a dpSCF voting rule and BRi its induced best response (Def. 3). Let
d+(νi, ui, x−i) = max z ui(z, x−i)−u i(BRi, x−i)≥0 denote the suboptimality of the best re-
sponse to x−i computed using νi. Finally, let s(ui) ={ P ai∈Ai ui(ai, a−i)}a−i∈A−i denote the set of playeri’s payoff sums under each co-player action profile. Then
d+(νi, ui, x−i)≤ ¯d+(νi,s(u i)) =κ + + (min k sk)d+(νi)(7)
whereκ + = (maxk sk −min k sk)andd +(νi)is theadditivedistortionν i from (6).
Theorem 3 shows our regularized best response BR(p,q,µi) i only introduces an additional distor-
tion to d+(νi) that is at most linear in p for small p. We similarly derive a multiplicative bound
d(νi, ui, x−i) = max z ui(z,x−i) ui(BRi,x−i) ≤κd(ν i) where κ= maxk sk mink sk . There exist voting rules νi that
guarantee additive distortion of 1/4≤d +(νi)≤ 1/2(1− 1/|Ai|2) and achieve ˜O( p |Ai|) for multi-
plicative distortiond(ν i)[21].
7

(a) Agent Marginals
 (b) Game Marginals
 (c) Agent Marginals Diffs
Figure 4: Atari: We present two different CO-NEs computed using the FTRL-inspired approach:
(SGF-NE) both agents use social grading functions and (SGF/Borda-NE) where the task agent
instead uses Borda. We compare them to the NE of an agent vs task performance matrix with scores
normalized to [0,1] as in [9]. Figure 4c supports convergence of our FTRL-inspired solver. Figure 3
displays additional performance information for the SGF-NE approach.
One of the earliest decentralized learning algorithms, (weakened) fictitious-play (WFP), iterates by
approximately best responding to the co-player’s historical play. The upper bound on the approxima-
tion error just derived in Theorem 2 can be used to directly derive bounds on the approximation error
of an equilibrium computed using WFP.
Corollary 1(Theorem 1 [ 22]).The WFP profile xT = [x(1) T , x(2) T ] after T rounds is an ϵT -NE where
ϵT ≤ T+1 2T + T−1 2T maxi ¯d+(ν,s(u i)).
Shift and scale the payoffs w.l.o.g. so that maxk sk = 1. Theorem 2 combined with Corollary 1 and
the known distortion bounds listed above imply there exists a voting rule ν such that FP converges to,
at worst, a (1− 1/4mink sk)-NE in 2-player general-sum. Note that 1/2 is the known lower bound for
approximating NE with constant size support [26]. With only access to ordinal feedback, FP achieves
3/4formin k sk = 1, a loss of 1/4in expected payoff.
Recent work provides algorithms for approximating coarse correlated equilibria assuming player’s
rankings over actions are drawn according to a Placket-Luce model consistent with true underlying
utilities [43]. This allows them to estimate the utilities by observing sampled rankings, i.e., invert the
model. In contrast, we do not assume it is possible to discover the underlying utilities. For example,
if a user deterministically reveals their preferences to be a single ranking, we can never learn the gaps
in utility between actions. Our aim in this work is to develop a theory that natively handles ordinal
information without (implicitly) working with any presumed underlying cardinal information.
5 Applications
We demonstrate our theory in two different domains: a) game-theoretic evaluation of AI agents and
b) a tactical voting setting with stochastic election outcomes and preferences.
5.1 General Agent Evaluation in the Arcade Learning Environment
We consider a game-theoretic [9, 44, 45] evaluation experiment with Atari agent vs task performance
data [37, Table 5] (c.f. Figure 7). In this setting, the performance matrix A plays the role of the payoff
matrix in a zero-sum bi-matrix game: minx maxy x⊤Ay where x (y) is the distribution over agents
(tasks). The solution surfaces a distribution over agents that is robust against an adversarially chosen
task distribution (NE-Norm in Figure 4). We instead run a version of FTRL (FTPL) [48, 59] using
our proposed regularized best response. We use social grading functions (SGF-NE) as the voting
rule and assign each agent one of four grades on a task based on quartiles. Figure 4 also considers a
heterogeneous setting where the agent player uses SGF and task player uses Borda (SGF/Borda-NE).
Figure 3 presents performance of our FTRL-style solver according to the metrics discussed in
Sections 4.2: exploitability (4) and hindsight winrate. All indicate our algorithm is effectively
learning. Figure 4 displays the learned equilibrium for the agent and task player along with a plot
supporting convergence of the iterates. Prior work espousing voting-as-evaluation found the rainbow
8

Table 1: Election: (Pure) Strategies arenota CO-NE.
playeri combinatorial actiona implicitly def.ρ i(a−i)
voter vote wtl pref
≻
 ≻
 2
 ≻
 ≻
 ≻
≻
 ≻
 9
 ≻
 ≻
 ≻
≻
 ≻
 5
 ≻
 ≻
 ≻
≻
 ≻
 10
 ≻
 ≻
 ≻
agent top-ranked according to 9 different popular voting rules [ 41, Table 2]. Their result can be
interpreted as equivalent to ours if we constrained the distribution over games to be uniform. Instead,
our theory uniquely allows one to show that rainbow is the strongest agent even if the distribution
over games is chosen adversarially.
5.2 Voting Equilibrium from Human Election Data: Lost at Sea
In theLost at Seaelection scenario [ 15], groups of four participants deliberate and then elect one
member to complete aleader’s task, a quiz whose score determines the payout to the group. The
election proceeds as follows. Each participant submits both awillingness-to-leadself-nomination
score (wtl∈ {0, . . . ,10}) and a vote ranking the other participants. The election mechanism selects
the two participants with highest wtl, splitting ties randomly, and executes a runoff between them.
Note that because no one could vote for themselves, only the votes of participants that are not
candidates impact the result; see more details on the election in Appx. H.2.1.
Separately, participants submitted rankings (pref) over who is elected. Given fixed co-player actions
a−i and the election outcomes oi resulting from each possible action ai ∈ Ai, we can rank the actions
bypref(o i), e.g., if for
 ,a→o=
 anda ′ →o ′ =
 , thena≻a ′.
V oters can manipulate the election by pulling themselves out of the race (loweringwtl). Alternatively,
if they know that the other players prefer a different candidate, they can reorder their vote to put their
second favorite higher, therefore increasing the odds of that candidate being elected.
Therefore, each participant’s strategy space (|Ai|= 66 ) consists of their wtl (11 options) and vote in
the election (3! = 6 options). Note that because the election mechanism is stochastic, we are forced
to confront the issue of how to aggregate stochastic outcomes. We can construct player i’s lottery
hierarchically; first sample a−i ∼x −i, then independently sample each election outcome given ai
(more details in Appx. H.2.2).
We utilize election ranking data from [54], an online variation of theLost at Seatask. The dataset
contains 115 elections involving 460 participants, interacting under pseudonymous, animal-based
identifiers. Assuming each voter acted deterministically, we find that approximately 30% of the 115
elections exhibited pure maximal lottery Nash equilibrium profiles. The remaining 70% contained at
least 1 player with an incentive to deviate, suggesting humans were not voting optimally with respect
to their reported preferences.
We select two elections for detailed analysis in Appx. H.2, one in equilibrium and one not. Election
data for one of those elections is shown in Table 1. We also demonstrate solving for an equilibrium of
the election, assuming Borda as the voting rule. We then re-use existing NFG solvers to approximate
a limiting logit equilibrium (LLE) [47], which we then analyze. For example, in one election,
would prefer itself to win, but
 is low-ranked by everyone. Given that
 is unlikely to win, the
LLE strategically suggests
 submit a low wtl to steer the election towards
 , its third favorite,
given its second favorite
 is not in the runoff. Note also that the LLEs are mixed strategies—they
mix over many (vote,wtl) combos.
Whereas strategic voting theory assumes well-studied election rules [49], our COG formalism enabled
a black-box analysis of a bespoke one.
9

6 Conclusion
We proposed the first (probabilistic) mixed-strategy Nash equilibrium that generalizes to games with
ordinal preferences. The key was to replace expected utility maximization for aggregating payoffs
with social choice functions for aggregating preferences. We prove existence, develop practical
notions of approximation and algorithms with rates, and demonstrate their use in AI evaluation and
(stochastic) election manipulation.
References
[1] Ilan Adler, Constantinos Daskalakis, and Christos H Papadimitriou. A note on strictly competi-
tive games. InInternational Workshop on Internet and Network Economics, pages 471–474.
Springer, 2009.
[2] Akshay Agrawal, Brandon Amos, Shane Barratt, Stephen Boyd, Steven Diamond, and J Zico
Kolter. Differentiable convex optimization layers.Advances in Neural Information Processing
Systems, 32, 2019.
[3] Alfred V Aho.Data Structures and Algorithms. Addison-Wesley, 1983.
[4] Hamidreza Alipour and Mohak Goyal. Utilitarian distortion under probabilistic voting.arXiv
preprint arXiv:2602.11152, 2026.
[5] Charalambos D Aliprantis and Kim C Border.Infinite Dimensional Analysis: A Hitchhiker’s
Guide. Springer Science & Business Media, 2006. ISBN 978-3-540-29587-7. doi: 10.1007/
3-540-29587-9_17.
[6] Nahla Ben Amor, Hélène Fargier, and Régis Sabbadin. Equilibria in ordinal games: A framework
based on possibility theory. InProceedings of the Twenty-Sixth International Joint Conference
on Artificial Intelligence (IJCAI’17), page 105–111, 2017.
[7] Anton Bakhtin, David J Wu, Adam Lerer, Jonathan Gray, Athul Paul Jacob, Gabriele Farina,
Alexander H Miller, and Noam Brown. Mastering the game of no-press diplomacy via human-
regularized reinforcement learning and planning.arXiv preprint arXiv:2210.05492, 2022.
[8] Anton Bakhtin, David J Wu, Adam Lerer, Jonathan Gray, Athul Paul Jacob, Gabriele Farina,
Alexander H Miller, and Noam Brown. Mastering the game of no-press diplomacy via human-
regularized reinforcement learning and planning. InThe Eleventh International Conference on
Learning Representations, 2023.
[9] David Balduzzi, Karl Tuyls, Julien Perolat, and Thore Graepel. Re-evaluating evaluation.
Advances in Neural Information Processing Systems, 31, 2018.
[10] Michel Balinski and Rida Laraki. A theory of measuring, electing, and ranking.Proceedings of
the National Academy of Sciences, 104(21):8720–8725, 2007. doi: 10.1073/pnas.0702634104.
URLhttps://www.pnas.org/doi/abs/10.1073/pnas.0702634104.
[11] Amir Beck and Marc Teboulle. Mirror descent and nonlinear projected subgradient methods for
convex optimization.Operations Research Letters, 31(3):167–175, 2003.
[12] Michel Benaïm and Mathieu Faure. Consistency of vanishingly smooth fictitious play.Mathe-
matics of Operations Research, 38(3):437–450, 2013.
[13] Michel Benaım and Morris W Hirsch. Mixed equilibria and dynamical systems arising from
fictitious play in perturbed games.Games and Economic Behavior, 29(1-2):36–72, 1999.
[14] Oliver Biggar and Iman Shames. The graph structure of two-player games.Scientific Reports,
13(1):1833, 2023.
[15] Andreas Born, Eva Ranehill, and Anna Sandberg. Gender and Willingness to Lead: Does
the Gender Composition of Teams Matter?The Review of Economics and Statistics, 104(2):
259–275, 03 2022. ISSN 0034-6535. doi: 10.1162/rest_a_00955. URL https://doi.org/
10.1162/rest_a_00955.
10

[16] James Bradbury, Roy Frostig, Peter Hawkins, Matthew James Johnson, Chris Leary, Dougal
Maclaurin, George Necula, Adam Paszke, Jake VanderPlas, Skye Wanderman-Milne, and
Qiao Zhang. JAX: composable transformations of Python+NumPy programs, 2018. URL
http://github.com/google/jax.
[17] Florian Brandl, Felix Brandt, and Hans Georg Seedig. Consistent probabilistic social choice.
Econometrica, 84(5):1839–1880, 2016.
[18] Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang, and Ariel D Procaccia.Handbook
of Computational Social Choice. Cambridge University Press, 2016.
[19] George W Brown. Iterative solution of games by fictitious play.Act. Anal. Prod Allocation, 13
(1):374, 1951.
[20] Ozan Candogan, Ishai Menache, Asuman Ozdaglar, and Pablo A Parrilo. Flows and decomposi-
tions of games: Harmonic and potential games.Mathematics of Operations Research, 36(3):
474–503, 2011.
[21] Ioannis Caragiannis, Swaprava Nath, Ariel D Procaccia, and Nisarg Shah. Subset selection via
implicit utilitarian voting.Journal of Artificial Intelligence Research, 58:123–152, 2017.
[22] Vincent Conitzer. Approximation guarantees for fictitious play. In2009 47th Annual Allerton
Conference on Communication, Control, and Computing (Allerton), pages 636–643. IEEE,
2009.
[23] Vincent Conitzer. The complexity of computing robust mediated equilibria in ordinal games. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 9607–9615,
2024.
[24] JB Cruz and Marwan A Simaan. Ordinal games and generalized Nash and Stackelberg solutions.
Journal of Optimization Theory and Applications, 107:205–222, 2000.
[25] Constantinos Daskalakis, Ian Gemp, Yanchen Jiang, Renato Paes Leme, Christos Papadimitriou,
and Georgios Piliouras. Charting the shapes of stories with game theory.arXiv preprint
arXiv:2412.05747, 2024.
[26] Tomas Feder, Hamid Nazerzadeh, and Amin Saberi. Approximating nash equilibria using
small-support strategies. InProceedings of the 8th ACM Conference on Electronic Commerce,
pages 352–354, 2007.
[27] Peter C Fishburn. Probabilistic social choice based on simple voting comparisons.The Review
of Economic Studies, 51(4):683–692, 1984.
[28] Gerald B Folland.Real Analysis: Modern Techniques and Their Applications, 2nd ed.John
Wiley & Sons, 1999.
[29] Drew Fudenberg and David K Levine. Consistency and cautious fictitious play.Journal of
Economic Dynamics and Control, 19(5-7):1065–1089, 1995.
[30] Drew Fudenberg and Jean Tirole.Game Theory. MIT press, 1991.
[31] Ian Gemp, Kevin R McKee, Richard Everett, Edgar Duéñez-Guzmán, Yoram Bachrach, David
Balduzzi, and Andrea Tacchetti. D3c: Reducing the price of anarchy in multi-agent learning.
InProceedings of the 21st International Conference on Autonomous Agents and Multiagent
Systems, pages 498–506, 2022.
[32] Ian Gemp, Rahul Savani, Marc Lanctot, Yoram Bachrach, Thomas Anthony, Richard Everett,
Andrea Tacchetti, Tom Eccles, and János Kramár. Sample-based approximation of nash in large
many-player games via gradient descent. InProceedings of the 21st International Conference
on Autonomous Agents and Multiagent Systems, pages 507–515, 2022.
[33] Ian Gemp, Luke Marris, and Georgios Piliouras. Approximating nash equilibria in normal-
form games via stochastic optimization. InThe Twelfth International Conference on Learning
Representations, 2024.
11

[34] Ian Gemp, Andreas Alexander Haupt, Luke Marris, Siqi Liu, and Georgios Piliouras. Con-
vex markov games: A new frontier for multi-agent reinforcement learning. InForty-second
International Conference on Machine Learning, 2025.
[35] Geoffrey J Gordon, Amy Greenwald, and Casey Marks. No-regret learning in convex games. In
Proceedings of the 25th International Conference on Machine learning, pages 360–367, 2008.
[36] John C Harsanyi, Reinhard Selten, et al. A general theory of equilibrium selection in games.
MIT Press Books, 1, 1988.
[37] Matteo Hessel, Joseph Modayil, Hado Van Hasselt, Tom Schaul, Georg Ostrovski, Will Dabney,
Dan Horgan, Bilal Piot, Mohammad Azar, and David Silver. Rainbow: Combining improve-
ments in deep reinforcement learning. InProceedings of the AAAI conference on artificial
intelligence, volume 32, 2018.
[38] Josef Hofbauer and William H Sandholm. On the global convergence of stochastic fictitious
play.Econometrica, 70(6):2265–2294, 2002.
[39] Shizuo Kakutani. A generalization of brouwer’s fixed point theorem.Duke Mathematical
Journal, 8(3):457, 1941.
[40] John G. Kemeny. Mathematics without numbers.Daedalus, 88(4):577–591, 1959. ISSN
00115266. URLhttp://www.jstor.org/stable/20026529.
[41] Marc Lanctot, Kate Larson, Yoram Bachrach, Luke Marris, Zun Li, Avishkar Bhoopchand,
Thomas Anthony, Brian Tanner, and Anna Koop. Evaluating agents using social choice theory.
arXiv preprint arXiv:2312.03121, 2023.
[42] Davide Legacci, Panayotis Mertikopoulos, Christos Papadimitriou, Georgios Piliouras, and
Bary Pradelski. No-regret learning in harmonic games: Extrapolation in the face of conflicting
interests.Advances in Neural Information Processing Systems, 37:123637–123674, 2024.
[43] Mingyang Liu, Yongshan Chen, Zhiyuan Fan, Gabriele Farina, Asuman Ozdaglar, and Kaiqing
Zhang. Online learning and equilibrium computation with ranking feedback.arXiv preprint
arXiv:2603.19221, 2026.
[44] Siqi Liu, Ian Gemp, Luke Marris, Georgios Piliouras, Nicolas Heess, and Marc Lanctot. Re-
evaluating open-ended evaluation of large language models. InThe Thirteenth International
Conference on Learning Representations, 2025.
[45] Luke Marris, Siqi Liu, Ian Gemp, Georgios Piliouras, and Marc Lanctot. Deviation ratings: A
general, clone-invariant rating method.arXiv preprint arXiv:2502.11645, 2025.
[46] Roberto-Rafael Maura-Rivero, Marc Lanctot, Francesco Visin, and Kate Larson. Jackpot!
alignment as a maximal lottery.arXiv preprint arXiv:2501.19266, 2025.
[47] Richard D McKelvey and Thomas R Palfrey. Quantal response equilibria for normal form
games.Games and Economic Behavior, 10(1):6–38, 1995.
[48] H Brendan McMahan. A survey of algorithms and analysis for adaptive online learning.Journal
of Machine Learning Research, 18(90):1–50, 2017.
[49] Roger B Myerson and Robert J Weber. A theory of voting equilibria.American Political science
review, 87(1):102–114, 1993.
[50] John F Nash Jr. Equilibrium points in n-person games.Proceedings of the national academy of
sciences, 36(1):48–49, 1950.
[51] Panos M Pardalos and Stephen A Vavasis. Quadratic programming with one negative eigenvalue
is np-hard.Journal of Global optimization, 1(1):15–22, 1991.
[52] Julien Perolat, Remi Munos, Jean-Baptiste Lespiau, Shayegan Omidshafiei, Mark Rowland,
Pedro Ortega, Neil Burch, Thomas Anthony, David Balduzzi, Bart De Vylder, et al. From
poincaré recurrence to convergence in imperfect information games: Finding equilibrium via
regularization. InInternational Conference on Machine Learning, pages 8525–8535. PMLR,
2021.
12

[53] Ariel D Procaccia and Jeffrey S Rosenschein. The distortion of cardinal preferences in voting.
InInternational Workshop on Cooperative Information Agents, pages 317–331. Springer, 2006.
[54] Crystal Qian, Aaron Parisi, Clémentine Bouleau, Vivian Tsai, Maël Lebreton, and Lucas
Dixon. To mask or to mirror: Human-AI alignment in collective reasoning. 2025. URL
https://arxiv.org/abs/2510.01924.
[55] Julia Robinson. An iterative method of solving a game.Annals of Mathematics, 54(2):296–301,
1951.
[56] Donald G Saari.Basic Geometry of Voting, volume 12. Springer Science & Business Media,
1995.
[57] Shai Shalev-Shwartz et al. Online learning and online convex optimization.Foundations and
Trends® in Machine Learning, 4(2):107–194, 2012.
[58] Samuel Sokota, Ryan D’Orazio, J Zico Kolter, Nicolas Loizou, Marc Lanctot, Ioannis
Mitliagkas, Noam Brown, and Christian Kroer. A unified approach to reinforcement learning,
quantal response equilibria, and two-player zero-sum games. InThe Eleventh International
Conference on Learning Representations, 2023.
[59] Arun Suggala and Praneeth Netrapalli. Follow the perturbed leader: Optimism and fast parallel
algorithms for smooth minimax games.Advances in Neural Information Processing Systems,
33:22316–22326, 2020.
13

A Context Ordinal Equilibria
A.1 Doubly Probabilistic Social Choice Functions
Many voting rules satisfy or can be adapted to satisfy Definition 2 of a doubly pSCF. Scoring
rules (e.g. plurality, Borda, veto, etc.) can compute solutions taking a lottery (or distribution) over
preference relations as input. So can k-approval. Rules are divided into C1, C2, and C3 by Fishburn
[27] depending on what information is needed to compute them. C1 uses only pairwise majority
relationships (e.g., Copeland), C2 uses weighted pairwise majority relationships (e.g., ranked pairs,
Borda), and then C3 is other rules (e.g., Dodgson). The lottery representation enables at least C1 and
C2rules.
Axioms’ Effect on dpSCFsSocial choice theory is axiomatic. We discuss a few axioms and
how they are important to dpSCFs here. For example, ifdictatorshipwas possible, player j could
induce arbitrarily small mass on some action profile such that it completely overwrites player i’s
best response regardless of the other outcomes possible; this would be akin to shifting mass onto an
outcome with infinite payoff in an NFG.Clone-invarianceasserts that duplicate actions (i.e., actions
that are ranked the same under every co-player action profile) will appear symmetrically in the best
response; this ensures equilibria exist that have symmetric mass and payoff across cloned actions.
Paretianvoting rules ensure that if a player ranks an action above another under all co-player action
profiles, the aggregate voting rule will as well; translating to COGs, if an action has higher payoff
than all other actions under all co-player actions, this action will be a best response. These properties
can be taken for granted in classical games that use expected value to aggregate scores, but it is
critical and fortuitous that social choice has already developed these tools for use in COGs. Note
that Borda fails clone-invariance. It also fails Condorcet consistency, which is a major motivation for
works that explore alternatives to the standard RLHF pipeline (see [46] which advocates for maximal
lotteries).
A.2 COGs as NFGs
As mentioned in Section 3.1, scoring and positional voting rules induce normal-form games. This
can be seen by filling out player i’s payoff tensor Ui(·, a−i) one “slice” at a time. For each player i
and each possible co-player action profile a−i, retrieve player i’s preference relation ρi(a−i) which
results in a vector of numerical scores for each of playeri’s actions:U i(·, a−i)←ρ i(a−i). Scoring
and positional voting rules simply take an average of these scores proportional to their representation
in the population of votes which is precisely equivalent to computing the expected payoff for each
action as is standard in NFG calculations.
A.3 Correlated Equilibria
Correlated equilibria (CE) are also important in classical game theory, particularly in n-player,
general-sum settings, and have natural counterparts here.
A correlated equilibrium is a joint distributionx over action profiles such that no player has any incen-
tive to unilaterally deviate even after observing their recommended action (sampled from x). As be-
fore, we represent this as a best-response inclusion problem. Define BRi(ai|x) =ν i(vi(x(A−i|ai)))
where the conditional distribution x(A−i|ai) =x(a i,A −i)/x(ai) and the marginal distribution
x(ai) = P a′ −i∈A−i x(ai, a′ −i). Define scalar-set multiplication as a·BR i(ai|x) ={a·v|v∈
BRi(ai|x)}. Then 0∈x(a i)·(BR i(ai|x)−e ai ) for all i represents the condition for a context-ordinal
CE wheree ai is the standard Euclidean basis vector.
Interestingly,coarsecorrelated equilibria (CCE) cannot be (classically) defined in COGs. In both NE
and CE, a player considers deviating from their current strategy to an alternative strategy under a
fixed context, either a co-player strategy or conditional belief. In a CCE, the expected utility of a joint
distribution is compared against a fixed action. This requires aggregating utilityacrosscontexts with
different weights, so a player must effectively be able to compare their own actions under different
co-player action profiles. In the COG definition, we specifically assume that a player can only rank
their actions under a fixed co-player action profile, which rules out this possibility.
14

(a) Classic
 (b) Classic (EMD)
 (c) ML (EMD)
 (d) Borda (EMD)
Figure 5: Exploitability (ϵ) landscapes for a 2-action (Swerve/Straight) Chicken game using various
regularized social choice BR(p=0,q=0.1,µ=[1/2,1/2])s. Panel (a) displays traditional exploitability based
on cardinal payoffs whereas (b), (c), and (d) measure earth mover’s distance (EMD). Maximal
lotteries (ML) and Borda coincide in two candidate (action) settings.
However, we discussed a generalized notion ofexternal regretin Section 4.2.2 which suggests an
alternative route towards CCE. A CCE can instead be defined as a joint distribution such that no
player has an incentive to deviate to any fixed strategy (in hindsight), i.e., all players simultaneously
experience zero external regret.
A.4 Exploitability Landscapes
Figure 5 shows how CO-NE differ from classical NE on a simple 2-player, 2-action Chicken game.
Panels a and b display the traditional exploitability landscape and earth mover’s distance (EMD)
landscape for a classical NE respectively. Panel c shows the EMD landscape for a CO-NE defined
using maximal lotteries as the voting rule. Panel d shows the same landscape but for Borda as the
voting rule.
B Regularized Best Response
Algorithm 1Regularized Best Response
1:Given:p,µ i,ν i,γ(·|x −i, q),M
2:BR i =0 |Ai|
3:form= 1toMdo
4:ˆx −i ∼γ(·|x −i, q)
5:u∼Cat(µ i)
6:v u ={a u ≻a j |j∈[|A i|], j̸=u}
7:v u =v u ∪ {aj ∼a k |j, k∈[|A i|]/{u}, j̸=k}
8:V={v: 0|v∈ P(A i)}
9:for alla −i ∈ A−i do
10:bit∼Bern(p)
11:f req= ˆx −i(a−i)
12:ifbit== 1then
13:V(v u) +=f req
14:else
15:V(ρ i(a−i)) +=f req
16:end if
17:end for
18:BR i +=ν i(V)/M
19:end for
20:Output:BR i
We now describe our approach to regularizing best responses. Algorithm 1 provides pseudocode.
Recall from Definition 3 that every action profile a−i induces a vote ρi(a−i) orballot typeand this
vote is represented in a population of votes with frequency x−i(a−i). We will represent random
perturbations as randomly swapping votes for votes from another distribution dependent on the given
µi. Consider the following random process. Draw a randomusurperfrom µi. Set theusurper ballot
such that the usurper is ranked strictly first; the remaining players can be ranked arbitrarily but we
set all others tied for second in experiments. For every co-player action profile, replace the original
ballot with the usurper ballot with probability p. Apply the (dpSCF) voting rule to this perturbed
15

Figure 6: Best Response Regularization in Chicken.
population of votes to compute a sampled best response. Take the expectation over these sampled
best responses to return an expected best response.
If p= 0 , then the best response remains the same as before. If p= 1 , all ballots are replaced by the
usurper ballot and any voting rule satisfying majority rule will select the usurper as the sampled best
response. As the usurper is selected according to µi, the expected best response will also be equal to
µi.
At this point, we have introduced two new parameters, p and µi. Denote this parameterized best
response byBR (p,µi) i .
To achieve a single-valued best response, we will replace all non-singleton best responses, which are
necessarily convex subsets of the simplex, with their centroid, i.e, the uniform distribution over the
winning candidates. Note this now means BR(p,µi) i is no longer u.h.c. as it could jump at ties, e.g.,
A≻B→B∼A→B≻A leads to [1,0]→[0.5,0.5]→[0,1] . Recall one of our desiderata is to
ensure continuity, a stronger condition than u.h.c.
To render the best response BR(p,µi) i (x−i) continuous with respect to x−i, we can introduce a
trembling handby taking the expectation over a Dirichlet perturbation, Dir(α), with density ρ where
α=1+ 1/qx −i withq >0:
BR(p,q,µi) i (x−i) =E x′ −i∼Dir(α)[BR(p,µi) i (x′ −i)] =
Z
X−i
BR(p,µi) i (x′ −i)ρ(x′ −i|α)dx′ −i.(8)
For any fixed q >0, the Dirichlet density ρ(x′ −i|α) is continuous in its parameters α and thus also in
x−i. Notice that BR(p,µi) i (x′ −i) is independent of x−i, therefore the integrand is continuous in x−i
for every fixedx ′ −i. Becauseq >0, this impliesα≥1and so the densityρis uniformly bounded.
Combined with the fact that best responses are probability distributions (and thus bounded), the
integrand is dominated by a constant integrable function. We then invoke the Dominated Convergence
Theorem [28][p. 56, Theorem 2.27] to conclude thatBR (p,q,µi) i (x−i)is continuous.
Lastly, note that as limq→0+, Dir(α) converges weakly to a Dirac delta at x−i, meaning we achieve
continuity while recovering an element of the original best response set in the limit. The Dirichlet
also as full support over the simplex for q >0, consistent with the “trembling hand” interpretation
of sampling all distributions with positive probability. In summary, p regularizes BRi towards µi; q
smooths.
Definition 5(Regularized Best Response).Let BR(p,q,µi) i (x−i) denote the expectation of a dpSCF
(Def. 2), in which, with probability p, ballot types are replaced with ballots top-ranked by an action
sampled from µi, non-singleton dpSCF outputs are replaced with their centroid, and the underlying
voting distribution x−i is replaced with a full-support distribution γ such that γ converges to a Dirac
delta distribution onx −i asq→0and uniform asq→ ∞.
Proposition 1.The regularized best response function BR(p,q,µi) i (x−i) with p∈[0,1] , q >0, and
µi ∈∆ Ai satisfies desiderata (C1), (C3), (C4). In the limitq→0, (C2) is satisfied.
16

B.1 Empirical Demonstration
Figure 6 displays the results of a simple experiment, regularizing a maximal lottery best response in a
chicken game towards a uniform strategy. A chicken game is a symmetric game in which you prefer
to go “straight” unless your co-player does, in which case you would rather “swerve” to avoid a
collision, i.e., ρ(“swerve”) → “straight” ≻ “swerve” and ρ(“straight”) → “swerve” ≻ “straight”. We
find that setting q= 0.1 is sufficient to achieve both continuity and correctness of the best response
over the range ofp.
For Figures 5a and 5b, the precise payoff matrices used for player 1 and 2 were U (1) =

3/4 1/2
1 0

andU (2) =

3/4 1
1/2 0

respectively.
C Distortion
Traditionally, distortion expresses the ratio of the maximum social welfare possible given knowledge
of voters’ cardinal scores for each candidate to the social welfare achieved by a voting rule applied to
those same voters’ preferences. Bounds on distortion are typically derived assuming voters’ cardinal
scores are non-negative and sum-to-1. Many voting rules process votes as ordinal rankings which
destroys the more detailed cardinal information which means distortion is commonly strictly greater
than 1.
We derive a lemma below that extends a distortion bound given each voterk’s scores sum-to-sk.
In what follows, election outcomes may be probabilistic, which we represent as a distribution x over
candidates. The expected welfare SW s of this election outcome given access to the scaled voting
scores is
SW s(x) = 1 K X k skv⊤ k x(9)
where K is the number of voters and vk is a vector of voter k’s unit-normalized scores for each
candidate.
Lemma 2.Assumeνis a voting rule that only processes ordinal rankings. Then
d(ν,s)≤κd(ν)(10)
where κ= maxk sk mink sk and d(ν) is an upper bound on the distortion of the voting rule ν when each voter’s ballot scores are non-negative and sum-to-1.
Proof. Let xcs be the distribution over candidates that maximizes welfare assuming access to the
voters’scaledcardinal scores:
xcs = arg max
xcs
1
K
X
k
skv⊤ k xcs.(11)
Let xc be the distribution over candidates that maximizes welfare assuming access to the voters’
un-scaled, i.e., unit-normalized, cardinal scores:
xc = arg max
xc
1
K
X
k
v⊤ k xc.(12)
The social welfare ofx cs is then upper bounded as
SW s(xcs) = 1 K X k skv⊤ k xcs ≤ 1 K (max k sk)( X k v⊤ k xcs)≤ 1 K (max k sk)( X k v⊤ k xc).(13)
Let xν be the distribution over candidates returned by the voting rule ν. The social welfare of xν is
then lower bounded as
SW s(xν) = 1 K X k skv⊤ k xν ≥ 1 K (min k sk)( X k v⊤ k xν).(14)
17

The distortion is the ratio of the two and is upper bounded as
d(ν,s) = SW s(xcs) SW s(xν) ≤ maxk sk mink sk P k v⊤ k xcsP k v⊤ k xν (15)
≤ maxk sk
mink sk
P
k v⊤ k xcP
k v⊤ k xν (16)
= maxk sk
mink sk
d(ν).(17)
Given a strategy profile x for an n-player COG, we can use Lemma 2 above to understand the
suboptimality of a player’s best response if they opt for a social choice rule (dpSCF) rather than
a traditional best response using expected utility theory. To apply Lemma 2, we will assume the
underlying payoffs of the game are non-negative with strictly positive sum. Note that an affine
transformation of the payoff matrix does not change the set of equilibria so this assumption is without
loss of generality.
Simply let si be a vector containing the payoff sums for player i under each possible joint action of
the co-players. Then apply Lemma 2 by looking up the distortion bound for the chosen voting rule νi.
Theorem 2.Assumeνis a voting rule that only processes ordinal rankings. Then distortion
d+(ν,s)≤κ + + (min
k
sk)d+(ν)(18)
where κ= (max k sk −min k sk) and d+(ν) is an upper bound on theadditivedistortion of the
voting ruleνwhen each voter’s ballot scores are non-negative and sum-to-1.
Proof. As in Lemma 2, let SW s denote the social welfare function with scaled votes. Let SW
denote the social welfare function assuming unit-normalized scores, which implies SW≤1 . We are
interested in the additive distortion:
d+(ν,s) =SW s(xcs)−SW s(xν)(19)
≤(max
k
sk)SW(x c)−(min k sk)SW(x ν)(20)
= (max
k
sk −min k sk)SW(x c) + (min k sk)(SW(x c)−SW(x ν))(21)
≤κ + + (min
k
sk)d+(ν).(22)
Theorem 3.The additional distortion introduced by our regularization process is
d+(νp,i, ui, x−i)≤κ + + (min k sk)(d+(ν) +  1−(1−p) |A−i| ).(23)
By Bernoulli’s inequality, the quantity

1−(1−p) |A−i| behaves as|A −i|pfor smallp.
Proof. The regularized voting process replaces each vote with a usurper vote with probability p.
Therefore, with probability (1−p) |A−i|, no votes are replaced. The voting rule returns xν in this
case. Taking the expectation of these outputs, we can then determine
xνp = (1−p) |A−i|xν +  1−(1−p) |A−i| z(24)
where xνp denotes the perturbed output (regularized best response) and z denotes the expected output
under the remaining perturbation events. The distortion of our perturbed voting rule, denoted νp, can
be decomposed into the distortion of the original voting rule ν and the gap between the perturbed and
18

original:
d+(νp) =SW(x cs)−SW(x ν)| {z }
distortion
+SW(x ν)−SW(x νp )| {z }
perturbation error
(25)
≤d +(ν) +SW(x ν)−SW(x νp )(26)
=d +(ν) +SW(x ν)−SW((1−p) |A−i|xν +  1−(1−p) |A−i| z)(27)
=d +(ν) +  1−(1−p) |A−i| SW(x ν)−SW(z)  (28)
≤d +(ν) +  1−(1−p) |A−i| (29)
≤d +(ν) +|A −i|p(30)
where (28) follows from linearity of social welfare, (29) from social welfare being bounded to [0,1] ,
and the last step from Bernoulli’s inequality.
Plugging this result into Theorem 2 achieves the claim.
C.1 Weakened Fictitious-Play (WFP)
We consider fictitious-play run for T rounds with approximate best responses whose error is upper
bounded byd +(ν,s). We can trace the argument put forth in [22] to prove the following.
Corollary 1(Theorem 1 [ 22]).The fictitious-play profile xT = [x (1) T , x(2) T ] after T rounds is an
ϵT -NE whereϵ T ≤ T+1 2T + 1 2 d+(ν,s).
Proof.We simply trace [22, Theorem 1] with approximate best responses.
By symmetry, it suffices to show that x(1) T = 1 T PT t=1 x(1) t is an ϵT -best response to x(2) T =
1
T
PT
t=1 x(2) t . Let BR1 be a best response to x(2) T . The corresponding best-response utility for
player 1 is u1(BR1, x(2) T ) = 1 T PT t=1 u1(BR1, x(2) t ). For 2≤t ′ ≤T+ 1 , because x(1) t′ is a best
response tox (2) t′−1, all utilities are non-negative, and the utilities are bilinear, we have
u1(x(1) t′ , x(2) T ) =u 1(x(1) t′ , 1 T
TX
t=1
x(2) t )(31)
=
TX
t=1
(1/T)u1(x(1) t′ , x(2) t )(32)
=
t′−1X
t=1
(1/T)u1(x(1) t′ , x(2) t ) +
TX
t=t′
(1/T)u1(x(1) t′ , x(2) t )(33)
≥
t′−1X
t=1
(1/T)u1(x(1) t′ , x(2) t )(34)
=
 t′ −1
T

u1(x(1) t′ , 1 (t′ −1)
t′−1X
t=1
x(2) t )(35)
=
 t′ −1
T

u1(x(1) t′ , x(2) t′−1)(36)
≥
 t′ −1
T

[u1(BR1, x(2) t′−1)−d +(ν,s)](37)
=u 1(BR1, 1 T
t′−1X
t=1
x(2) t )−
t′−1X
t=1
(1/T)d+(ν,s)(38)
=
t′−1X
t=1
(1/T)[u1(BR1, x(2) t )−d +(ν,s)](39)
19

where (37) follows by the fact that x(1) t′ is an approximate best response to x(2) t′−1; most importantly, it
at least−d +(ν,s)better than any other strategy (includingBR 1) in responding tox (2) t′−1.
Continuing, for the case where player 1 playsx (1) T , we have
u1(x(1) T , x(2) T ) =u 1( 1 T
TX
t′=1
x(1) t′ , x(2) T )(40)
=
TX
t′=1
(1/T)u1(x(1) t′ , x(2) T )(41)
= (1/T)u1(x(1) t′=1, x(2) T ) +
TX
t′=2
(1/T)u1(x(1) t′ , x(2) T )(42)
≥0 +
TX
t′=2
(1/T)u1(x(1) t′ , x(2) T )(43)
≥
TX
t′=1
(1/T)
t′−1X
t=1
(1/T)[u1(BR1, x(2) t )−d +(ν,s)]summand equals0fort ′ = 1
(44)
= (1/T2)
T−1X
t=1
TX
t′=t+1
[u1(BR1, x(2) t )−d +(ν,s)]re-index sum of lower triangular (t ′ ×t) matrix
(45)
= (1/T2)
TX
t=1
(T−t)[u 1(BR1, x(2) t )−d +(ν,s)].(46)
On the other hand,
u1(BR1, x(2) T ) =u 1(BR1, 1 T
TX
t=1
x(2) t )(47)
= (1/T)
TX
t=1
u1(BR1, x(2) t )(48)
= (1/T2)
TX
t=1
T u1(BR1, x(2) t ).(49)
It follows that the suboptimality for player1of playingx (1) T is
u1(BR1, x(2) T )−u 1(x(1) T , x(2) T )≤( 1/T2)
TX
t=1
tu1(BR1, x(2) t ) + (1/T2)
TX
t=1
(T−t)d +(ν,s)(50)
≤( 1/T2)
TX
t=1
t+ ( 1/T2)d+(ν,s)
TX
t=1
(T−t)(51)
= (1/T2)(T+ 1)( T/2) + (1/T2)d+(ν,s)
T−1X
t=0
t(52)
= (1/T2)(T+ 1)( T/2) + (1/T2)d+(ν,s)(T−1)( T/2)(53)
= (T+ 1) (2T) + (T−1) (2T) d+(ν,s).(54)
20

C.1.1 Distortion of Regularized Best Responses
The bounds above are derived for unregularized best responses. There exists a new result in the
distortion literature that examines multiplicative distortion under a different perturbation model [4].
If this line of work were to continue and uncover additive bounds, we might be able to apply them
here to obtain bounds for a different form of regularized best responses.
C.1.2 First Order Stochastic Dominance
We clarify a relationship between first order stochastic dominance (FSD) and social choice based best
responses. Within the context of COGs, let xi and x′ i be two mixed strategies from which we can
sample actions ai and a′ i. Let ui :A →Rbe any isotone (order-preserving) utility function that is
consistent with the given preference relation ρi. In other words, if ai ≻a ′ i in the context of a−i, then
ui(ai, a−i)> ui(a′ i, a−i) and if ai ∼a ′ i in the context of a−i, then ui(ai, a−i) =u i(a′ i, a−i). Then
x strictly FSD-dominates x′ i if E[ui(xi, x−i)]>E[u i(x′ i, x−i)] holds for every ui where ui has been
extended to act on distributions in the standard way.
Consider x′ i player i’s current strategy. Assume xi strictly FSD-dominates x′ i as above. Under which
voting rules does playerihave a strict incentive to deviate?
Within social choice theory, the property that an aggregation rule never selects a lottery that is
stochastically dominated by another is known as SD-efficiency.
Both positional scoring rules and Maximal Lotteries are SD-efficient, hence, no strategies in their
induced best responses sets will ever be FSD-dominated by another strategy.
D Complexity
It is natural to attempt to understand the complexity of computing voting equilibria. Given two-player,
zero-sum games represent a natural complexity boundary in the classical payoff setting, we first
explore whether this boundary translates to the voting setting.
D.1 Two-Player, Zero-Sum
First off, it is not immediately possible to translate the notion of 2-player, zero-sum to a COG.
First, there no longer exist payoffs that can be summed. Second, players are not required to express
preferences over unilateral changes in actions by the other player.
As mentioned in Section 3.1, score and positional voting rules induce normal-form games with
payoffs from which we can then analyze traditional two-player, zero-sum definitions. However, we
show that COGs defined to be intuitively adversarial fail these necessary conditions. In particular,
adversarial COGs are neitherharmonicnorstrictly-competitive. Harmonic games [ 20, 42] generalize
the classical two-player, zero-sum definition in a way that relies on only the weightedresponse graph,
a graph of joint action nodes with arrows indicating favorable (including ties) deviations for players.
Strictly competitive games [1] are two-player, zero-sum up to shift and scale of each player’s payoffs.
We provide a practical example of this phenomenon in Figure 7 motivated by game-theoretic evalua-
tion [44, 45], specificallyNash averaging[ 9]. In that setting, one often considers games where it is
unclear how to compare performance on one task X (e.g., measured with perplexity) with another
task Y (e.g., measured with accuracy), whereas ranking models on a common task is clear.
D.1.1 Harmonic
A finite (cardinal) game is harmonic [ 42, Def. 1] when it admits a collection of action weights
βi,ai ∈(0,∞),a i ∈ Ai,i∈[N], such that X
i
X
a′ i∈Ai
βi,a′ i [ui(a)−u i(a′ i, a−i)] = 0∀a∈ A.(55)
In other words, there exists a weighting of the weighted response graph such that the net flow at
every (joint action) node is zero. The condition above is linear in the action weights, so we can
simply construct a matrix A of the terms ui(a)−u i(a′ i, a−i) and check if there exists weights
21

Figure 7: Adversarial COGs are not necessarily strictly competitive, nor harmonic, however, they are
preference-zero-sum. Preferences over agents for each task are indicated in (a) by gold, silver, and
bronze. Preferences over tasks are directly opposed and are indicated in (b) by 0 (not preferred) and
1 (preferred). The gold arrow in (a) highlights that the agent player can improve their outcome by
switching from agent C (silver) to agent A (gold) when playing task X. Assuming Borda as the voting
rule (and the payoffs induced in its associated NFG representation), the corresponding black arrow
in (b) shows the task player is indifferent (although recall preferences over agents are not explicitly
represented in a COG for the task player). Hence, this game is not strictly competitive either. The
associated (weighted) response graph is shown in (c); weights are calculated again assuming Borda.
Appx. D.1.1 shows that there does not exist a node weighting that makes the net flow at every node
zero, ruling out the game asharmonic. However, if one reverses all horizontal edges in the graph
(gray), it is possible to construct a common payoff game (values in gray) with the same (unweighted)
response graph, proving the game ispreference-zero-sum.
(a) Agent Preferences
Tasks
Agents X Y
A
B
C
(b) Task Preferences
Tasks
Agents X Y
A 0 1
B 1 0
C 0 1
(c) (Weighted) Response Graph
AX AY
BX BY
CX CY
+1
+2
+1
+1
+1
+1
+1
+2
+1
2 1
0 2
1 0
β= [β 1A, β1B, β1C, β2X , β2Y ] that set Aβ=0 , i.e., check that A is full column-rank (equiv., empty
null-space). In the case of Figure 7, the terms ui(a)−u i(a′ i, a−i) are indicated in black next to the
directed edges. The rows ofAare ordered[AX, AY, BX, BY, CX, CY]:
A=


0 2 1 0−1
0−1 1 1 0
−2 0−1 0 1
1 0 2−1 0
−1 1 0 0−1
−1−2 0 1 0

 .(56)
This matrix has full column-rank, therefore its null space contains only the zeros vector. So there
does not exist an action weighting β with βi,ai ∈(0,∞) to render the net flow zero. Therefore, it is
not harmonic.
D.1.2 Preference-Zero-Sum
While COGs do not admit a direct payoff structure, they do provide corresponding (unweighted)
response graphs. The COG in Figure 7doessatisfy the definition of preference-zero-sum [ 14] which
relies only on the unweighted response graph. A preference zero-sum game’s corresponding response
graph has only one sink component [14, Corollary 4.11], which we can calculate in time linear in
the graph Θ(V+E) , polynomial in the size of the game, using, e.g., Kosaraju-Sharir’s algorithm [3,
Algorithm p. 224 & 229]. The sink component conveys information about evolution, learning,
and omits strictly dominated strategies. Nevertheless, we are unaware of any efficiency results for
computing equilibria only assuming the preference-zero-sum property.
Hence, two-player, zero-sum does not appear to represent a complexity boundary in COGs similarly
to classical NFGs.
D.2 Two-Player, Known-Support
We now consider instead the even simpler problem of computing an equilibrium of a 2-player game
given we know the support.
Probabilistic voting rules are sometimes avoided simply due to humans’ aversion to a randomized
election outcome. However, given our context-ordinal Nash equilibrium solution concept already
allows for randomized play, it seems natural to consider them.
22

(a) Exploitability
 (b) Hindsight Winrate
 (c) AUC of (b)
 (d) Hindsight MoV
Figure 8: We evaluate our (SGF-based) FTRL approach (ps is thesolver’s parameter) on the Atari
evaluation game according to the metrics in Section 4.2 and Appx. E. (a) EMD as defined in
Section 4.2.1, eqn. (5); (b,c) Hindsight winrate and area measurement from Section 4.2.2—(c) plots
the ’s seen in (b) at t= 100 with p on the x-axis; (d) margin of victory (MoV) as described in
Section E.2. Panels (b) and (d) set ps = 1/t+ 1. FTRL can also be considered asmoothed-FP
approach.
Here, we specifically consider maximal lotteries as the underlying voting rule of a 2-player COG.
Maximal lotteries (ML) are a probabilistic, Condorcet consistent voting rule, i.e., they select the
action that beats every other action in a heads up comparison if one exists; otherwise, they specify a
distribution over candidates that will be preferred to every other voting rule by a majority of voters in
expectation. The maximal lottery problem can be formulated as a symmetric, two-player, zero-sum
bi-matrix game (minx maxy x⊤Ay) where each entry in A, called themarginmatrix, equals the net
frequency with which one candidate was ranked above another in the population of votes. Here,
we assume the NE has full support. Therefore, the maximum lottery best response must return a
fully-mixed result.
In a COG, the margin matrix depends on the population of votes through the other player’s strategy.
Let the margin matrix be Ai ∈R |Ai|×|Ai|. Ai here depends on x−i, i.e., Ai =A i(x−i). The value
of a symmetric, zero-sum game is zero and all actions in the support achieve this value at the NE,
so we know that Aiy=A ixi =u M L i (xi) =0 ; we are looking for a symmetric NE of that game
so y=x=x i. It can be shown that Aixi = [x ⊤ −iWiℓxi]ℓ =0 where Wiℓ is a constant matrix
dependent only on the fixed preference data ρi and ℓ∈[|A i|]. Therefore, we are looking for an xi
andx −i that satisfyx ⊤ −iWiℓxi = 0∀i, ℓsubject tox i restricted to the given support for each player.
Empirically, we find that the resulting quadratic constraints are generally not convex (the relevant
matrices are not positive semi-definite). This ultimately results in a system of quadratic equality
constraints (QCQP), an NP-hard problem [51]. Note a solution exists; we state QCQP complexity to
express the general difficulty of computing its solution.
E Metrics
E.1 Meta-Game Analysis Continued
The meta-game analysis in Section 4.2.2 suggested measuring regret as the probability of electing a
fixed hindsight action over the online algorithm for fixed regularization parametersp.
Alternatively, we can deploy our regularized best response to plot a curve showing the probability of
selecting one of the algorithms (xi,t or z∗ i ) as we vary the noise p from 0 to 1 with µi as uniform and
q≪1 held fixed. Area between the curve and a constant line at 0.5 would provide a notion of how
strong the selection bias is towards one algorithm or another. We present the probability of hindsight
being selected by BR(p,q=0.1,µi=[1/2,1/2]) i in Figure 8b along with this accompanying area metric in
Figure 8c.
E.2 Game Space
The classical approach (3) can be reinterpreted as taking the game as fixed, then finding the closest
strategy z to xi that achieves optimality (rationality) for player i, and finally reporting the difference
between those two strategies in payoff space. Instead, we can take the strategy xi as fixed, find the
“closest” game such that player i’s current strategy is rationalized, and then report the difference
between those two games. This dual approach, also considered in other works [25, 31], is actually
23

analogous to the standard view taken in social choice. Specifically,margin of victorycounts the
number of votes that must be altered for a given candidate to win the election.
In our lottery / infinite voter population model, it is easy to solve; we simply calculate what proportion
of votes in the population need to be altered for candidates to tie. Moreover, this concept extends to
the online setting via the meta-game approach described above by measuring how many votes must
be altered in the vote population generated across all T rounds. Figure 8d displays this approximation
metric.
F Algorithms
We discuss several practical learning algorithms inspired by work on normal-form games. A best
response operator regularized towards strategyµ i with regularizerR(z, µi),p t >0,
BR(pt,q,µi) i ([x−i,t]) = arg max z {−ptR(z, µi) + ¯ui,t(z,[x −i,t])}(57)
forms the crux of many of these techniques including:
• Follow the regularized leader [48, 59] is a no-regret learning algorithm with time-average
convergence to coarse-correlated equilibria [35]; setx i,0 = arg minz R(z, µi); then
xi,t+1 = arg max
z
{− 1 t+ 1 R(z, µi) +
tX
t′=1
1
t+ 1 ui,t′(z, x−i,t)}(58)
= arg max
z
{− 1 t+ 1 R(z, µi) + ¯ui,t(z,[x −i,t])}(59)
which, c.f. (57), suggestsBR (pt,q,µi)(x−i,t)withp t = 1/(t+ 1);
• Fictitious play is a related algorithm in which each player best responds to the historical
play of its co-players [19, 55]; smooth (regularized) variants enjoy regret guarantees [38, 29,
12, 13],
• Homotopy [32] and adaptive regularization [58, 52] methods all guide the algorithm through
solving a curricula of games (using regularized best responses) that ends at the solution of
the original game of interest.
And, in the case where a voting rule (e.g., scoring rule) induces a traditional normal-form game
(see Appx. A.2), we can re-use any normal-form game solver as well. We examine both the follow
the regularized leader (FTRL) and homotopy style of approaches in Section 5.
G Visualization
The ability to visualize and analyze an equilibrium solution is important for diagnostics, particularly
in game-theoretic evaluation [44, 45]. In these works, an action ai’s rating is its expected payoff at
equilibrium, and visualizations are given to show how each of another player’s actions aj contribute
to the rating of ai. Here, we aim to provide analogous tools for COGs despite the lack of utility
functions.
As mentioned earlier, some voting rules induce NFGs, for which we can reuse prior visualization and
analysis techniques. For the more general case, we can consider breaking down the probability mass
placed on an action ai at equilibrium into its contributions from each of player j’s actions. To do
so, we leverage techniques in cooperative game theory, specifically Shapley values, although other
power indices are possible. Shapley values satisfy an efficiency property that ensures the sum of the
contributions from each action aj equals the probability mass placed on ai (xi,ai). The key primitive
used in defining a Shapley value, and cooperative game theory general, is the characteristic function
which acts on sets of actions. We define the characteristic function, ci applied to a subset of actions,
ˆAj ⊆ Aj, to be the probability mass placed on ai in player i’s best response when only actions ˆAj
are available to player j; we select the uniform distribution over winning actions as the unique best
response value. We define player j’s strategy over ˆAj to be proportional to its original distribution
over ˆAj (i.e., normalized to sum to1), akin to omitting abstained votes.
24

For example in Chicken, the Shapley value breakdown of the final expected rank for the row player’s
actions at NE,[0.5,0.5], are:
" swerve straight
swerve-0.25 0.75
straight0.75 -0.25
#
.(60)
When the row player swerves, if the column player swerves, the row player could have achieved a
better outcome by going straight, so the column player’s decision to swerve contributes negatively
(−0.25) to the row player’s rating of swerve. On the other hand, if the column player goes straight,
the row player’s decision to swerve achieves a much better outcome than if the row player had chosen
to go straight which would have resulted in a collision.
H Experiments
H.1 Atari
In the Atari experiments, the two sources of stochasticity arise from a) the random usurper ballots and
b) the Dirichlet sampling process described in Section 4.1. Recall that this noise is used to regularize
and render the best response operator continuous. We use this regularized best response operator
BR(p,q,µi) i both as part of the FTRL-inspired update and to evaluate the learned strategy profile (see
Section 4.2). We fix a solver_seed for the random noise generated for the FTRL solver as well as a
separate eval_seed to evaluate the solution returned by the solver. Every time the regularized best
response operator is evaluated, we sample a best response according to the procedure described in
Section 4.2 (and Algorithm 1) num_samples times; we then average the sampled best responses to
give the regularized best response. Table 2 lists the hyperparameters used in the Atari experiments.
Figure 3 displays the mean and standard error over this set of random experiments.
q µi # ofsolver_seeds # ofeval_seeds num_samples
Figures 3a & 8c 0.1 uniform 10 1000 100
Figures 3b & 8d 0.1 uniform 10 100 100
Table 2: Atari Hyperparameters.
25

H.2 Lost at Sea
H.2.1 Election instructions
The following reproduces the exact instructions on the election process provided to participants in the
Lost at Seadataset from [54].
Below is an overview of the election process.
1. Indicating interest- You will first be asked to indicate how much you want to become
the group leader on a scale from 0 to 10.
2. Ranking your teammates- You will rank your three teammates, with your preferred
leader at position 1, the second most preferred leader at position 2, and the third most
preferred leader at position 3. You cannot vote for yourself.
We will use your answers to these two questions to select the leader:
• The two group members who express the most interest in becoming the leader will
be selected as candidates for the election. If several group members choose the same
number, the computer will randomly determine the order of these group members.
• The highest-ranked candidate among the two will be elected as leader. If both candi-
dates tie, the decision will be made randomly.
With this process, you are asked to rank your team members before knowing who the candidates
are. Only the rankings of the two group members who are not candidates will be considered.
This ensures that you cannot vote strategically to increase your own chances of being elected as
the leader. Therefore, it is in the interest of all group members to provide their true, preferred
ranking of the other group members.
H.2.2 Stochastic Outcomes
To handle stochastic election outcomes, we consider the distribution defined by the following
stochastic process. First sample a co-player action profile a−i ∼x −i. Then, independently sample a
single (counterfactual) election outcome for every one of player i’s actions given a−i. We then rank
player i’s actions given that realized set of outcomes. We then repeat and aggregate these preferences
using the chosen social choice voting rule.
H.2.3 Election Case Study: Human PlayNotin Equilibrium
We examine the election data in Table 1, which contains both the actions the players took (wtls &
votes) as well as their prefs for election outcomes. We do not know whether the players’ actions
were sampled from a mixed strategy. For the sake of this analysis, we assume the players chose the
actions listed in the table deterministically. Under this assumption, calculations suggest the strategy
profile listed in Table 1 is not a maximal lottery (ML) NE.
In particular, Koala is not playing a best-response. It is identified that if they reduced their wtl to
remove themselves from the runoff, then the two competing candidates would be Lion and Chicken
ranked 1st and 2nd by their preference rankings ( pref). Across the players, Chicken wins once
against Lion (Pig’s vote) and loses once (Koala’s vote). The winner is then either Chicken or Lion
with equal probability. This is compared to the status quo where Koala enters a high wtl such that
Koala and Lion enter the runoff. Koala beats Lion twice (Pig and Chicken both rank it higher) so
Koala is deterministically elected, however, strangely, Koala ranks itself 3rd in its own preference
ranking (pref) despite its highwtl.
Player Chicken is identified as not playing a best response by our sample best response estimate
(p= 0 , q= 0.1 , num_samples= 100 ), but this is false. The sample best response we compute
actually achieves the same value, but probabilistically. This is likely due to the sample estimate not
having converged yet. The suggested best response is to submit a much higher wtl (10) in order to
force the runoff to be between Lion and Chicken, ranked 0 and 2 by Chicken. They have equal wins
so will be selected randomly giving Lion an average score of 1 for the outcome regardless of the vote
26

Figure 9: Election (Table 1) LLE Equilibrium.
they pair with wtl=10 since their vote cannot contain a comparison between Chicken (themselves)
and Lion by rules of the election.
Next, we demonstrate solving for an equilibrium of the voting game. In this demonstration, we use
Borda as the voting rule. As mentioned earlier, Borda is a scoring rule which induces a normal-form
game on the COG. We then re-use existing NFG solving techniques to approximate a limiting logit
equilibrium (LLE) [ 47]. We use the Jax [ 16] package polarix with min_temperature0.1 to
compute the LLE. Note that we use Borda here for efficiency sake, but it is possible to apply the
same general technique to maximal lotteries with differentiable convex optimization libraries such as
CVXPYLAYERSin JAX [2, 16].
In the LLE shown in Figure 9, Chicken and Lion spread most mass over high wtl actions, so they are
likely to be in the running. This means Pig and Koala’s votes will have impact in the election. Both
Chicken and Lion want themselves to win and are ranked favorably by Pig and Koala although not in
the same order. Pig prefers Chicken. Koala prefers Lion. Expectedly, Pig ranks Chicken above Lion
in all its votes in the LLE support. Koala ranks Lion higher in all its votes. This should lead to Lion
and Chicken being elected with equal probability (confirmed empirically in simulation).
According to the players’ outcome preferences (pref), the essential (bipartisan) set of a Maximal
Lottery consists of Koala, Chicken, and Lion. Why are Chicken and Lion in the support of the LLE,
but Koala is not? Koala actually prefers both Lion and Chicken to itself, so it withdraws from the
election to steer the result towards either of the two (preferably Lion). The story is similar with Pig,
who ranks themselves last.
H.2.4 Election Case Study: Human Play in Equilibrium
We similarly examine the election data in Table 3. Calculations suggest each player’s strategy listed
in Table 3isa max-entropy, maximal lottery best response to each other (i.e., a Nash equilibrium).
We use the same settings as before (p= 0,q= 0.1,num_samples= 100).
In particular, computing the max-entropy, maximal lottery for Bear reveals its best responding actions
(essential set). We summarize Bear’s best response strategies as follows:
27

Table 3: Election A: (Pure) Strategies are in Equilibrium.
voter vote wtl pref
Bear
 ≻
 ≻
 5
 ≻
 ≻
 ≻
Rabbit
 ≻
 ≻
 8
 ≻
 ≻
 ≻
Dog
 ≻
 ≻
 3
 ≻
 ≻
 ≻
Frog
 ≻
 ≻
 6
 ≻
 ≻
 ≻
• When wtl≤ 6, Bear always ranks Rabbit over Frog because it is possible Bear is not
selected in a runoff (wtl=6), and therefore its vote (and Dog’s) matters. In this case, Rabbit
wins, which is Bear’s ideal outcome;
• If Bear’s wtl> 6, then Bear is selected as the candidate against Rabbit and Bear’s vote
doesn’t matter (Dog and Frog’s do). Rabbit wins, which is Bear’s ideal outcome.
Borda LLEComputing an LLE of this election using Borda (Table 3), we find the following
equilibrium description with equilibrium presented in Figure 10. Rabbit and Dog spread most of their
mass over low wtl actions, which removes them from the running. Bear and Frog spread their mass
over high wtl actions, so they are likely to be in the running. Dog would prefer itself to win, but Dog
is low-ranked by everyone. Given that others might not let Dog win the election, Dog submits a low
wtl to steer the election towards Bear, its third favorite, given Rabbit is not in the runoff. Rabbit is
high ranked by all but wants to avoid Frog being elected, which could happen if Rabbit and Frog are
in a runoff. By submitting a low wtl, Rabbit can influence the election away from Frog and towards
Bear which is Rabbit’s 2nd ranked option. Bear ranks itself lower than Frog, so would be happy
with Frog winning. Frog essentially feels similarly, but with itself and Bear swapped in the ranking.
After sampling ten thousand election outcomes under the LLE, we observe that Bear is elected > 99%
of the time. It is interesting that the LLE arrives at Bear being elected because Rabbit is the strong
Condorcet winner.
Figure 10: Election (Table 3) LLE Equilibrium.
28
