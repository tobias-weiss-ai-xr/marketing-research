---
title: Reasonably reasoning AI agents can avoid game-theoretic failures in zero-shot, provably
url: https://arxiv.org/abs/2603.18563
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Enoch Hyunwook Kang
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.18563
pages: 109
chars: 201393
fetched_at: '2026-11-08T13:02:38+00:00'
kb_version: 1
---

# Reasonably reasoning AI agents can avoid game-theoretic failures in zero-shot, provably

Reasonably reasoning AI agents avoid game-theoretic failures in
zero-shot, provably
Enoch Hyunwook Kang∗
Foster School of Business, University of Washington
Abstract
AsautonomousAIagentsincreasinglymediateonlineplatformmarkets,afundamentalquestion
emerges: do these markets generate stable strategic outcomes? In repeated strategic environ-
ments,theNashequilibriumprovidesanaturalbenchmarkforthisstability. However,empirical
evidence on off-the-shelf LLM agents is mixed, leaving it unclear whether independently de-
ployed agents can converge to equilibrium behavior without explicit strategic post-training. In
this paper, we provide an affirmative answer. Extending the Bayesian learning literature in
theoretical economics, we prove that AI agents, acting as Bayesian posterior samplers rather
than expected utility maximizers, are guaranteed to eventually become weakly close to a Nash
equilibrium in infinitely repeated games. We further extend this analysis to settings in which
stage payoffs are unknown ex ante, and agents observe only their privately realized stochastic
payoffs, and obtain the same convergence guarantees. Finally, we empirically evaluate these
theoretical implications across five repeated-game environments, ranging from the Prisoner’s
Dilemma to marketing promotion games. Taken together, our findings suggest that strategic
stabilityinAI-mediatedmarketscanemergefromtheintrinsicreasoningandlearningproperties
of modern AI agents, without the need for unrealistic universal fine-tuning.
∗ehwkang@uw.edu
1
arXiv:2603.18563v2  [cs.AI]  25 Apr 2026

1 Introduction
Afundamentaltransitionisunderwayinonlineplatformmarketplaces: autonomousAIagentsarebeginning
to act on behalf of consumers in search, evaluation, and purchasing decisions (Gaarlandt et al., 2025;
Shahidi et al., 2025). Rather than humans directly browsing rankings, comparing listings, and clicking
throughinterfaces,AIagentscanparsewebpagesorinteractthroughAPIstoevaluateproductsandtransact.
As a result, an increasing share of economically relevant platform activity may soon be mediated not by
human attention directly, but by interaction among autonomous agents operating within platform-designed
environments (Rothschild et al., 2025).
Thisshiftmakesatheoreticalquestionnewlyurgent. Inmarketsmediatedbyhumanparticipants,economists
oftenanalyzeoutcomesthroughthelensofstablestrategicbehavioremergingfromrepeatedinteraction. As
autonomousAIagentsincreasinglyactonbehalfofusers,itbecomesunclearwhethermarketspopulatedby
suchagentswillexhibitthesamekindofpredictablestrategicstability. Thecoreissue, therefore, isnotonly
whether an individual AI agent performs well, but whether many interacting AI agents collectively produce
stable and predictable market outcomes. In digital markets, such interaction arises naturally in pricing,
promotion, bidding, negotiation, matching, and recommendation environments, where each agent’s payoff
depends on how other agents behave over time (Bianchi et al., 2024; T. Guo et al., 2024; Lopez-Lira, 2025;
Y. Li et al., 2024; Zhu et al., 2025; Bansal et al., 2025). In such settings, what matters for prediction is
whether the system settles into a stable strategic pattern of play(Carichon et al., 2025).
Nash equilibrium in repeated games is a natural benchmark for such stability. In repeated strategic environ-
ments, Nash equilibrium provides a starting point for analyzing long-run behavior, incentives, and strategic
predictability (Abreu and Rubinstein, 1988; Dal Bó and G. R. Fréchette, 2011; Dal Bó and G. R. Fréchette,
2018; Proto, Rustichini, and Sofianos, 2019). In this sense, asking the question ofwhether AI agents con-
verge toward Nash-like play in repeated gamesis the first step toward understanding strategic outcomes in
AI-mediated markets; failure to approach this benchmark can be regarded as agame-theoretic failure. That
is,ifagentsdonotreachbehaviorthatisatleastimmunetoprofitableunilateraldeviationsinrepeatedgames,
then the resulting play lacks even the most basic form of strategic stability and is difficult to interpret as
strategically coherent. This makes Nash convergence in repeated games a useful baseline question before
considering richer models of dynamic interaction, such as Markov Perfect Equilibrium (Aguirregabiria,
Collard-Wexler, and Ryan, 2021).
This question is not merely theoretical. Recent work by Calvano et al. (2020) and Fish, Gonczarowski, and
Shorrer (2024), together with related empirical studies of algorithmic interaction, suggests that autonomous
algorithmic and AI systems can generate strategically consequential repeated-game behavior in economi-
cally important environments. Pricing algorithms can sustain supra-competitive outcomes without explicit
communication, rapid reactive pricing technologies can elevate prices even in competitive equilibrium, and
real-worldadoptionofrepeatedalgorithmicpricinghasbeenassociatedwithhighermarginsinconcentrated
markets (Assad et al., 2024).
2

On the other hand, empirical evaluations of LLMs reveal that widely used, off-the-shelf AI models (e.g.,
GPT,Claude,Gemini,Kimi,DeepSeek)asAIagentsfrequentlyfailtoexhibitpredictedequilibriumbehavior
in strategic interactions and often resort to brittle heuristics or produce inconsistent policies (X. Guo et al.,
2024; J.-t. Huang et al., 2024; Hua et al., 2024; Buscemi et al., 2025). In practice, simply prompting
standard AI models to engage in repeated games often yields strategies that diverge significantly from
rational, equilibrium-based play predicted by classical game theory, although some successes have been
reported(Akataetal.,2025). SuchbrittlenessandinconsistencyraiseconcernsaboutdeployingAIagentsin
societallycrucialdomainsthatrequirereliablestrategicdecision-making. Accordingly,whetheroff-the-shelf
reasoning LLM agents can be guaranteed to converge to a Nash equilibrium in repeated strategic interaction
stably remains an open problem.
Oneprominentapproachtoaddressingthisproblemistheuseoftargeted,universalpost-trainingprocedures
(Y.Lietal.,2024;Duqueetal.,2025),i.e.,requiringallAIagentstoundergothesameadditionalfine-tuning
alignment steps to instill strategically desirable behavior. However, relying on the universal deployment of
such fine-tuning approaches across diverse, independently developed AI agents competing with one another
isimpractical. Consequently,thereisacompellingneedforassurancethatoff-the-shelfAIagentswithsome
“reasonable”reasoningcapabilitiesautonomouslyadapttheirstrategiesandreachastableequilibrium. This
critical observation motivates the central research question explored in this paper:
Can off-the-shelf reasoning AI agents stably converge to Nash equilibrium in repeated strategic interaction
without post-training?
Inthispaper,weshowthatreasoningLLM-basedAIagentsareguaranteedtoevolvetowardNashcontinuation
play along realized play paths, without relying on specialized explicit post-training procedures.
Atahighlevel,ourargumentbuildsonasimpleideafromtheeconomicsofrepeatedinteraction: ifagentscan
learn from observed play what their opponents are likely to do and respond well to those learned forecasts,
their behavior should move toward Nash-like play over time. The classicalBayesian learningliterature
in theoretical economics formalizes this logic by showing that when agents Bayesian-update beliefs from
observed histories andexactlybest respond to those beliefs, equilibrium behavior eventually emerges along
realized play paths (Kalai and Lehrer, 1993a; Norman, 2022).
Wetakethislogicasourstartingpointbutadaptittothesettingofoff-the-shelfreasoningLLMagents. The
central difficulty is that such agents are not expected-utility maximizers (Yamin et al., 2026; Ge, Yongyan
Zhang, and Vorobeychik, 2026). Rather than best-responding, i.e., deterministically choosing the exact
optimal action against their current beliefs, they behave more naturally as stochastic posterior samplers
(Arumugam and Griffiths, 2025). Our first theoretical contribution is therefore to show that, under mild
and realistic assumptions, posterior-sampling LLM agents nevertheless achieveasymptoticbest-response
learningalongtherealizedplaypath. OursecondcontributionistoshowthattheclassicalBayesianlearning
literature’s logic extends to this weaker asymptotic notion, so that exact best responses need not be assumed
3

to recover eventual proximity to a Nash equilibrium of the continuation game.
Toformalizethisargument,weisolatetworeasoningcapabilitiesandcallagentssatisfyingthem“reasonably
reasoning” agents:Bayesian updatingandasymptotic best-response learning. By Bayesian updating, we
mean the capacity to learn opponents’ strategies from observed interaction histories and thereby form
increasinglyaccuratebeliefsaboutfutureplay. Byasymptoticbest-responselearning,wemeanthat,relative
to those inferred beliefs, the agent’s continuation behavior eventually becomes approximately optimal along
the realized path. Combined with recent findings that LLMs behave as Bayesian in-context learners under
stationary,repeatedsettings(Coda-Fornoetal.,2023;Luetal.,2024;Cahyawijaya,Lovenia,andFung,2024;
Xie et al., 2021; X. Wang et al., 2023; Wakayama and Suzuki, 2025; Falck, Z. Wang, and Holmes, 2024),
this yields our conclusion that reasoning LLM agents can satisfy the ‘reasonably reasoning’ conditions and
therefore eventually exhibit Nash equilibrium along realized paths in infinitely repeated interactions.
Wealsodevelopaweakerbutpracticallyimportantbenchmarkformyopicreasoning. Ifanagentonlypredicts
opponents’nextactions and best responds period by period, then one should not expect convergence to rich
repeated-game equilibria supported by continuation incentives. Nevertheless, we show that such one-step
predict–then–act reasoning is still sufficient for eventual convergence to astage-gameε-Nash equilibrium
along the realized path. This result provides a useful theoretical benchmark for simpler prompting-based
procedures, such as SCoT (Akata et al., 2025), and clarifies what myopic reasoning can and cannot achieve
relative to continuation-level planning.
Beyond the benchmark with common-knowledge stage payoffs, we also consider the practically relevant
case in which payoffs are not known to agents ex ante and each agent observes only its own privately
realized stochastic payoffs. To model this, we can modify the agents’ posterior sampling to not only
sample an opponent-strategy hypothesis, but also sample a hypothesis for the agent’s own mean payoff
matrix (equivalently, its own payoff kernel within the known noise family). Under the analogous learning
conditions,posteriorsamplingrecoversthesameasymptoticon-pathε-best-responsepropertyandtherefore
inherits the zero-shot Nash convergence guarantees.
These theoretical results generate three distinct empirical predictions. First, because one-step predict–
then–act reasoning is sufficient only forstage-gameequilibrium convergence, simple myopic procedures
(e.g., SCoT) should often succeed when the objective is merely to reach some stage-game Nash action.
Second,becausenontrivialrepeated-gameequilibriadependoncontinuationvalues,myopicreasoningshould
generally fail to sustain such paths, whereas agents that infer opponent strategies and evaluate continuation
plans should succeed. Third, when payoffs are not known ex ante and must be learned from noisy private
observations, the same separation should persist, although under a more demanding informational problem.
To examine whether these implications arise in practice for a concrete off-the-shelf model, we instantiate
Qwen 3.5-27B (Qwen Team, 2026), a small open reasoning model, with three different decision rules:
theBasemodel agent, the myopicSCoTagent, and the reasonably reasoning (RR) agent implemented via
4

posterior-sampling best response (PS-BR). We then study their behavior in symmetric self-play across five
repeated-game environments, ranging from the Prisoner’s Dilemma to marketing promotion games. The
resulting simulations confirm the predictions of the theory developed above.
Thispaperisstructuredasfollows. Section2discussesrelatedwork. Section3introducestherepeated-game
setup and the operational belief notation used in the main text; the more formal predictive-representative
construction is deferred to Appendix A. Section 4 defines reasonably reasoning agents and relates their
Bayesian and best-response learning properties to in-context and test-time inference in language models.
Section 5 presents the main zero-shot Nash convergence results. Section 6 extends the analysis to unknown,
stochastic payoffs. Section 7 provides empirical evidence for the theory.
2 Related works
BayesianLearning.ThetheoreticalanalysisofreasonablyreasoningagentsisbasedlargelyontheBayesian
learning literature. Bayesian learning in repeated games is defined by a fundamental tension between the
abilitytologicallylearnopponents’strategiesandtheabilitytorespondtothemoptimally. Thefoundational
possibility result in Kalai and Lehrer, 1993a showed that if players’ prior beliefs contain a "grain of truth"
(absolutecontinuity)regardingthetruedistributionofplay,thenstandardBayesianupdatingguaranteesthat
their predictions will eventually converge to the truth, thereby naturally culminating in a Nash equilibrium.
However, Nachbar (1997) and Nachbar (2005) subsequently proved a negative result: requiring players to
simultaneouslymaintainthisgrainoftruthandperfectlybest-respondacrossallpossiblecounterfactualgame
histories leads to a mathematical contradiction, as the infinite sets of learnable strategies and optimizing
strategies are often mutually singular. Norman, 2022 resolved this tension by introducing “optimizing
learnability”, the crucial insight that agents do not need to perfectly learn unreached counterfactuals; they
only need to accurately predict and best-respond along the realized path of play. Nonetheless, Norman
identified that a stubborn impossibility persists in a specific class of games called MM* games, where
adversarial payoff geometries prevent learning and optimization from coexisting even on-path.
This paper systematically navigates these classic boundaries to guarantee zero-shot Nash convergence for
LLM agents. We actively employ Kalai and Lehrer, 1993a grain of truth (Assumption 2) to guarantee
predictive accuracy via the classic merging of opinions, and avoid Nachbar (1997) and Nachbar (2005)’s
impossibility by formally adopting the on-path relaxation and non-MM* in Norman (2022).
StrategiccapabilitiesofLLMagents.AsLLMsareincreasinglydeployedasinteractiveagents,agrowing
literature studies whether LLMs behave strategically in canonical games, emphasizing preference represen-
tation, belief formation, and (approximate) best responses rather than taking equilibrium play for granted
(H. Sun et al., 2025; Jia et al., 2025). In one-shot normal-form, bargaining, and negotiation tasks, off-the-
shelf models often follow plausible but context-sensitive heuristics: behavior can depart from equilibrium
predictions and change markedly under small framing or instruction variations (F. Guo, 2023; C. Fan et al.,
2023; Hua et al., 2024). Strategic performance can improve with model scale and reasoning scaffolds, but
the remaining variance across prompts and settings is substantial (Kader and Lee, 2024).
5

These issues become more acute under repeated games, where payoffs depend on stable, history-contingent
policies. Multi-agent evaluation benchmarks report large cross-model and cross-game heterogeneity and
frequent non-equilibrium dynamics, especially in coordination and social-dilemma regimes (Mao et al.,
2023; Duan et al., 2024; J.-t. Huang et al., 2024). Controlled repeated-game experiments similarly find that
cooperation/reciprocity can emerge, but is fragile to opponent choice and to seemingly minor prompt or
protocol changes (Akata et al., 2025; Fontana, Pierri, and Aiello, 2024; Willis et al., 2025). In market-style
repeated settings, recent work further documents collusive or supra-competitive outcomes among LLM
agentsandhighlightssensitivitytocommunicationopportunitiesandwordingchoices(Fish,Gonczarowski,
and Shorrer, 2024; Agrawal et al., 2025).
Overall, existing results demonstrate meaningful strategic adaptation but do not provide general, zero-shot
guarantees that heterogeneous, independently deployed off-the-shelf agents will converge to predictable
equilibrium behavior. Our paper targets this gap by identifying two basic theory-of-mind capabilities,
Bayesian updating of opponent strategies and asymptotic best-response learning, and proving that, under
mildconditions,theyimplyNashcontinuationplayalongrealizedpathsinrepeatedgames,withoutrequiring
explicit post-training or cross-agent coordination.
LLM agents as Bayesian in-context learners.A growing body of work linksin-context learning(ICL),
i.e., test-time adaptation that conditions prior history on a prompt without parameter updates, to Bayesian
inference over latent task hypotheses. In stylized transformer meta-learning settings, Xie et al. (2021) argue
that transformers trained over a task distribution can implement an implicit Bayesian update and produce
posterior-predictivebehaviorfromin-contextdata;relatedanalysesformalizeICLas(approximate)Bayesian
model averaging and study how this view depends on model parameterization and drives generalization
(Yufeng Zhang et al., 2023). Moving beyond specific constructions, Falck, Z. Wang, and Holmes (2024)
proposeamartingale-basedperspectivethatyieldsdiagnosticsandtheoreticalcriteriaforwhenanin-context
learner’s predictive sequence is consistent with Bayesian updating, while Wakayama and Suzuki (2025)
provide a broader meta-learning theory in which ICL is provably equivalent to Bayesian inference with
accompanying generalization guarantees. Empirically, LLMs also exhibitmeta-adaptation across tasks
presented in-context (Coda-Forno et al., 2023), and several abilities that appear “emergent” under scaling
can be substantially attributed to improved ICL mechanisms (Lu et al., 2024). Complementing these
viewpoints, X. Wang et al. (2023) model LLM ICL through a latent-variable lens, where demonstrations
act as evidence about an unobserved task variable—clarifying why behavior can be highly sensitive to the
specific examples and their ordering—and related results document few-shot in-context adaptation even
in low-resource language learning regimes (Cahyawijaya, Lovenia, and Fung, 2024). For agentic and
repeated-interactionsettings,theseBayesian-ICLperspectivesmotivatemodelinganLLMagent’suseofthe
interaction transcript as maintaining and updating a posterior over opponent strategies/types; autoregressive
generation can then be interpreted as sampling-based decision-making from the induced posterior (K. W.
Zhang et al., 2024; Welleck et al., 2024), providing a concrete bridge between in-context learning and
belief-based strategic behavior.
6

Expected utility maximization and best response.Standard learning-in-games analyses often assume
agents compute an exact best response to their posterior at every history (Kalai and Lehrer, 1993a; Norman,
2022). Thisisapoorbehavioralmodelforoff-the-shelfLLMagents,whoseactionsareinducedbystochastic
decodingandthusimplementadistributionoverchoicesratherthanadeterministicmaximizationofexpected
utility. In probabilistic decision tasks, Yamin et al. (2026) find systematic belief–decision incoherence,
suggesting that elicited probabilities should not be treated as beliefs that the model then perfectly best-
responds to. In risky-choice experiments, Ge, Yongyan Zhang, and Vorobeychik (2026) similarly document
substantialdeparturesfromexpected-utilitymaximizationandlargesensitivitytoprompting/modeltype,with
behavior better described as noisy sampling. Arumugam and Griffiths (2025) argues that LLMs naturally
implementposteriorsampling. Theseresultsmotivatereplacingexactbestresponsewithaweaker,sampling-
compatible notion, e.g., posterior-sampling policies, which are shown to achieveasymptoticbest-response
performance along the realized path.
3 Setup
3.1 Infinitely repeated game
We study interaction among a finite set of agentsI={1,2,...,N}in an infinitely repeated (discounted)
game with perfect monitoring of actions and common-knowledge stage payoffs. We define the game as the
tuple
G=
(
I,{Ai}i∈I,{ui}i∈I,{λi}i∈I
)
where:
•Iis the finite set of AI agents
•A i is the finite set of actions available to agenti
•A= ∏ i∈IAi is the joint action space, where a joint action profile at roundtis denoteda t =(
at 1,...,a t |I|
)
∈A. (at i indicates the action of agentiat roundt)
•u i :A→[0,1]is agenti’s (known) stage-game payoff function
•λ i∈(0,1)is the private discount factor used by agentito value future payoffs.
At each roundt= 1,2,..., each agentisimultaneously chooses an actiona t i∈A i, forming a joint action
profileat∈A, which is publicly observed. Agentithen receives the stage payoff
ui(at)∈[0,1](1)
These stage payoffs induce a standard infinitely repeated game with perfect monitoring of actions.
Indefiningthepayoffs{u i}i∈I,werestrictattentiontothefollowingstandardassumptionfromtheBayesian
learningliterature(Norman,2022). Intuitively,thisexcludesgameswithoutapure-strategyequilibrium,e.g.,
7

rock-scissors-paper;moreimportantlyforourpurposes,itexcludesthepayoffenvironmentsinwhichrealized
playneednotadmitanearbyNashinterpretation. Sincetheobjectofthepaperisequilibriumpredictionand
analysisofrealizedplay,thisrestrictionisolatesthepartofthegamespacewherethatquestioniswellposed.
Assumption 1(Non-MM⋆ game (Norman, 2022)).Consider the infinitely repeated game induced by the
true stage payoffs{ui}i∈I in equation (1). For each playeri, define the stage-game minmax payoff and
pure-action maxmin payoff as
φi := min σ−i∈∆(A−i) max σi∈∆(Ai) ui (σi,σ−i),Φ ⋆ i := max ai∈Ai min a−i∈BR−i(ai) ui (ai,a−i),
whereBR−i (ai)denotesthesetofopponents’(joint)bestresponsestoa i inthestagegame. Wecallthatthe
stage game isMM⋆ ifΦ ⋆ i <φ i for everyi. We assume the stage game is notMM⋆ (equivalently,Φ⋆ i≥φ i
holds for somei).
3.2 Strategy
We define the joint action history at roundtasht = ( a1,a 2,...,a t−1) ,and
Ht = {( a1,a 2,...,a t−1 ) :a s∈Afors≤t−1 } .
LetH 0 :={∅}denote the empty history. Denote the complete set of possible histories asH=⋃ t≥0Ht.
(Throughout this paper, we allow AI agents’ strategies to have bounded memory; See Appendix D.)
Definition 1(Strategy).A strategy for agentiis a function
fi :H→∆ (A i),
which maps every joint action history to a distribution over agenti’s actionsAi.
LetF i denote the space of all strategies of agenti. A strategy profile is a tuplef= (f1,...,f N)∈F= ∏
i∈IFi. LetH∞ denote the space of infinite play paths, i.e.,
H∞ = {( a1,a 2,... ) :a t∈Afor allt∈N } .
Definition2(Play-pathdistribution).Astrategyprofilef= (f 1,...,f N)∈Finducesauniqueprobability
distributionµ f overH∞ (theplay-path distribution), defined on cylinder sets by
µf
(
C
(
a1,...,a t
))
:=
t∏
s=1
∏
i∈I
fi (hs) (as i ),
whereh s = (a1,...,a s−1)andC(h) :={z∈H ∞ :z= (h,...)}. By Kolmogorov’s extension theorem
8

(Durrett, 2019), these finite-dimensional probabilities define a unique probability measureµf on(H∞,B),
whereBis the productσ-algebra.
For the upcoming discussions, we fix some notations. Given that we fix a historyht, for any continuation
profileg(i.e.,aprofilethatspecifiesplayafterhistoriesextendingh t),letµ g ht denotetheinduceddistribution
onH ∞ over the future joint-action sequence(at,at+1,...)when play starts at historyh t and followsg
thereafter. Formally, we identify the tail(at,at+1,...)withy∈H ∞ by settingy 1 =a t,y 2 =a t+1, and
so on, and regardµg ht as a measure on this reindexed space. For a full profileg∈F, we writeµg ht for
the continuation distribution induced by its restrictiong|ht. Ifµg(C(ht))>0, thenµ g ht coincides with the
conditional distributionµg(·|h t).
3.3 Beliefs
Each agentiholds a priorµ 0 i over opponents’ strategy profilesF−i and updates it by Bayes’ rule as public
historiesareobserved. Forthemaintext,therelevantobjectistheinducedposteriorpredictivecontinuation
law: after historyht, the agent needs a forecast of future opponents’ play, not a full existence argument for
how that forecast is represented.
Given any own strategygi∈F i and any beliefµi over opponents’ strategies, let
Pµi,gi i (E) :=
∫
F−i
µ(gi,f−i)(E)dµi(f−i),for measurableE⊆H ∞.
denote the predictive play-path distribution induced byµi. We writeP0,gi i :=P µ0 i,gi i for the prior predictive
distribution. At any historyht where Bayes’ rule is defined, the posteriorµt i(·|h t)induces an analogous
posterior predictive continuation law.
To keep the main text operational, we writefi,t −i for any continuation model that reproduces playeri’s
posterior predictive continuation law for the purpose of continuation-value calculations, andfi −i for the
analogous model associated with the prior predictive law. The standard existence and selection details for
these representative continuation models are deferred to Appendix A.
3.4 Subjective utility and Nash equilibrium
Subjective Expected Utility.An agent evaluates the optimality of a continuation strategy based on their
subjective beliefs at a given history. Fix a historyht and letσi∈F i(ht)be a continuation strategy for agent
ifromh t onward. For any opponents’ continuation profileg−i, denote byµ(σi,g−i) ht the induced distribution
over future play paths when play starts atht and follows(σi,g−i)thereafter.
Followingthestandardliterature(KalaiandLehrer,1993b),wedefinethebelief-explicitsubjectiveexpected
utilityof playingσi starting atht as
Vi(σi|h t;g−i) =E y∼µ (σi,g−i) ht
[
(1−λ i)
∞∑
k=0
λk iui(yk+1)
]
,(2)
9

wherey= (y 1,y 2,...)represents the future path of joint actions relative to timet, withyk+1 denoting the
joint action at stepk+ 1of this future path (i.e., at absolute timet+k).
Wheng−i =f i,t −i, we write
Vi(σi|h t) :=V i(σi|h t;f i,t −i).(3)
For any belief about opponents’ continuation playg−i at historyht, we define the set ofε-best-response
continuation strategies for agentiatht as
BRε i (g−i|h t) =
{
σi∈F i(ht) :V i(σi|h t;g−i)≥sup
σ′ i∈Fi(ht)
Vi(σ′ i|h t;g−i)−ε
}
.
Nash equilibrium.The true performance of a strategy profilef∈Ffor agentiis given by:
Ui(f) =E z∼µf
[
(1−λ i)
∞∑
t=1
λt−1 i ui
(
zt
)]
,
wherez t∈Ais the joint action at roundt, andλi∈(0,1)is agenti’s discount factor. The factor(1−λ i)
is a normalization ensuring thatUi(f)∈[0,1]wheneveru i(a)∈[0,1]for alla∈A.
Definition 3(ε-Nash equilibrium).A strategy profilef= (f 1,...,f N)∈Fis anε-Nash equilibrium if,
for every agenti∈I,
Ui(f)≥sup
f′ i∈Fi
Ui
(
f′ i,f−i ) −ε.
4 Reasonably Reasoning Agents
Asdiscussedearlier,oneofthekeyideasofthisworkisthatreasoningLLM-basedAIagentsarefundamen-
tally “reasonably reasoning” agents. In this section, we formally define the class of reasonably reasoning
agents,andthendemonstratewhyreasoning-LLMagentsarenaturallyreasonablyreasoningagents. Thedef-
initionisolatestwoingredients: (i)Bayesianupdatingand(ii)anon-path,asymptoticnotionofε-consistency.
Definition 4(Reasonably Reasoning Agent).Fix a repeated game and a strategy profilef= (f i)i∈I
generating the objective play-path distributionµf (Definition 2). Playeriis aReasonably Reasoning(RR)
agent if the following hold.
•Bayesian updating:Playerihas a priorµ 0 i over opponents’ strategy profilesF−i and forms posteriors
(µt i)t≥0 byBayes’rule. Letf i,t −i denoteanycontinuationmodelreproducingplayeri’sposteriorpredictive
continuation law at historyht (Section 3.3), so that for every continuation strategyσi,
Vi(σi|h t) =V i(σi|h t;f i,t −i).
10

•Asymptoticε-consistency on-path:For everyε>0,
µf
({
z:∃T i(z,ε)<∞s.t.∀t≥T i(z,ε), fi
⏐⏐
ht(z)∈BR ε i ( fi,t −i ⏐⏐ ht(z)|h t(z) )}) = 1.
Intuitively, the “Bayesian updating” condition ensures that agents update their strategic beliefs coherently
given observations. The “asymptoticε-consistency” condition captures the idea that after a possibly long
initial stumbling phase, agents eventually learn to play (approximately) optimal continuation strategies
relativetotheirownbeliefsalongtherealizedpathofplay. ItgeneralizesNorman’sε-consistency(Norman,
2022),whichrequiresε-bestrespondingatalltimes(notonlyeventually)onafull-measuresetofpaths. This
generalization is critical, as LLM-based AI agents are not expected-utility maximizers but rather posterior
belief samplers (Arumugam and Griffiths, 2025; Yamin et al., 2026; Ge, Yongyan Zhang, and Vorobeychik,
2026).
The Bayesian-learning component of Definition 4 is intentionally predictive. In repeated interaction, the
objectanagentneedsforplanningistheposteriorpredictivelawoverfutureplayconditionalontherealized
history, not a perfectly identified label for the opponent’s entire strategy. The notationfi,t −i from Section 3.3
is just a convenient continuation-model wrapper for that predictive law.
This distinction matters because repeated-game strategies are history-contingent reaction rules. Realized
actionschangeovertime,butlearningisaboutrefininguncertaintyovertheunderlyingruleand,operationally,
over its implications for continuation play. Continuation values are computed by integrating payoffs against
the induced posterior predictive law. The formal representative construction is standard and recorded in
Appendix A; the main text only needs the predictive object itself.
To guarantee that Bayesian updating is well-defined and that predictive beliefs can converge to the truth
on-path, we impose the standard grain-of-truth condition.
Assumption 2(Grain of truth (Kalai and Lehrer, 1993a)).For each playeri, the objective play-path
distributionµ f is absolutely continuous with respect toi’s prior predictive distribution underfi, i.e.µf≪
P 0,fi i . Equivalently, any event that playeriassigns zero probability under their prior predictive model has
zero probability under the true play distribution induced byf.
Under Assumption 2, classical merging-of-opinions results (Blackwell and Dubins, 1962) imply that player
i’s posterior predictive continuation beliefs become accurate alongµf-almost every realized play path. We
formalize this later by showing that absolute continuity implies strong path prediction (Lemma 5.1).
4.1 LLM agents are Bayesian updating agents
The Bayesian-learning abstraction above matches what we can operationally observe from LLM agents:
history-conditioned predictive distributions. An LLM, when prompted with the game rules and the realized
interactionhistory, inducesaconditionaldistributionovernexttokens, whichcanbearrangedtocorrespond
11

to a distribution over a discrete label for an opponent strategy.
This“asifBayesian”framingisappropriatefortworeasons. First,thetechnicalapparatusalreadyworksatthe
level of history-conditioned predictive distributions. The notationfi,t −i is only a representative continuation
modelusedtoevaluatecontinuationvaluesunderthoseforecasts,andtheformalrepresentativeconstruction
is deferred to Appendix A. Second, recent theory and empirical evidence indicate that AI agents, most
of which are auto-regressive LLM models, can implement Bayesian or approximately Bayesian in-context
learning in repeated, stationary environments (Xie et al., 2021; Yufeng Zhang et al., 2023; Falck, Z. Wang,
and Holmes, 2024; Wakayama and Suzuki, 2025). Interpreting the prompt history as data and the model’s
induced distribution as a posterior predictive therefore provides a principled bridge between LLM behavior
and Bayesian-learning agents in repeated games.
Finally, Assumption 2 should be understood as a modeling requirement on the LLM agent’ssupport: the
agent’spredictivemodelshouldnotruleout(assignzeroprobabilityto)eventsthatcanactuallyoccurunder
the true interaction induced byf. In practice, this corresponds to ensuring that the agent’s elicited beliefs
are sufficiently expressive so that the true on-path behavior is not ruled out. Mild smoothing can be useful
in implementation, but the finite-menu argument below does not require an exogenous tremble.
4.2 LLM agents achieve asymptoticε-consistency
InLLMagents,actionsareproducedthroughstochasticdecodingratherthanthroughadeterministicargmax
computation. Empirically, this introduces substantial decision noise and breaks the literal expected-utility-
maximization view of behavior (Yamin et al., 2026; Ge, Yongyan Zhang, and Vorobeychik, 2026). A better
approximation is that the agent samples a latent strategic hypothesis from its current posterior and then
reasons conditional on that sample (Arumugam and Griffiths, 2025; Cai et al., 2024). The goal of this
subsection is to show that such sampling-based behavior can still satisfy the asymptoticε-consistency part
of Definition 4.
The big picture has three steps. First, we formalize the LLM decision rule asposterior-sampling best
response(PS-BR): infer one opponent-strategy hypothesis from the current posterior, then optimize against
that sampled hypothesis. Second, we quantify the loss from sampling a single hypothesis rather than
optimizing against the full posterior predictive continuation. Third, we impose a menu-level learnability
condition saying that, along the realized path, the posterior over the finite retained menu eventually puts
almostallmassonlabelsthatarecontinuation-payoff-equivalenttothetruthfromthereachedhistoryonward.
Once these three pieces are combined, the stochasticity of LLM decoding remains real at any fixed date, but
it becomes asymptotically irrelevant for on-path optimality.
LLMs naturally induce posterior-sampling best response (PS-BR).Reasoning LLM-based AI agents
are naturally scaffolded as “infer, then respond” systems (Zhou et al., 2023; Riemer et al., 2024). PS-BR
isolates exactly that logic: sample one opponent hypothesis from the current posterior, then choose a best
response to that sampled hypothesis. This preserves the sampling-based flavor of LLM behavior while still
12

making the optimization step explicit.
Definition 5(Posterior sampling best response (PS-BR)).Fix playeriand a historyh t. Given posterior
µt i(·|h t)over opponents’ strategy profiles, PS-BR chooses a continuation strategy by:
1. sampling ˜f−i∼µ t i(·|h t);
2. playing any best responseσi∈BR i( ˜f−i|h t)in the continuation game afterht.
Denote the resulting (randomized) continuation strategy byσPS i,t (·|h t).
Remark1.In our experiments, step 1 is implemented by querying the model to output one opponent-
strategy label from an allowed finite menu, and step 2 is implemented by evaluating a finite set of candidate
self-strategies against that sampled label via roll-out and selecting the value-maximizing candidate. See
Appendix E for the implementation details. The theoretical point is not the engineering scaffold itself, but
the structure it captures: LLM agents need not act like deterministic expected-utility maximizers; they can
act like posterior samplers whose draws are then optimized against.
The first question is what is lost by best-responding to one sampled label rather than to the full posterior
predictive continuation. The next lemma gives a simple worst-case bound: the gap is controlled by how
often two independent posterior samples disagree.
Lemma 4.1(PS-BR is aDt i-best response).Fix playeriand a historyh t. Supposeµt i(·|h t)is supported
on a finite setS−i and write
pt(g−i) :=µ t i(g−i|h t), g −i∈S−i.
Define the posterior collision complement
Dt i(ht) := 1− ∑
g−i∈S−i
pt(g−i)2 = Pr
˜g,˜g′∼µt i(·|ht)
[
˜g̸= ˜g′] .
Letσ PS i,t (·|h t)be PS-BR atht. Then
Vi(σPS i,t |h t)≥sup σi Vi(σi|h t)−D t i(ht).
Equivalently,σ PS i,t (·|h t)∈BR Dt i(ht) i ( fi,t −i ⏐⏐ ht|h t) .
Lemma 4.1 gives the first key idea. PS-BR is already close to a best response whenever posterior dispersion
over strategically different labels is small. If the posterior were concentrated on one label, the gap would
be zero. But the exact posterior point concentration is stronger than we need. For Nash convergence, the
onlyposteriordisagreementthatmattersisdisagreementthatchangesthecontinuationoptimizationproblem
from the reached history.
13

This observation is what lets us weaken the learning requirement. In general repeated games, full posterior
concentration over an unrestricted strategy space is too much to ask and is closely related to the classic
impossibility phenomena in Nachbar (1997) and Nachbar (2005). We therefore ask only for strategy
learnabilityup to continuation-payoff equivalence. The key point is that PS-BR samples labels, but Nash
convergenceonlycaresaboutthecontinuationoptimizationprobleminducedbythoselabels. Iftworetained
labels generate exactly thesame continuation value for every continuationstrategy available to playeriafter
areachedhistory,thenPS-BRisstrategicallyindifferentbetweenthem: samplingoneortheotherleavesthe
objective being optimized unchanged.
Definition 6(On-path continuation-payoff equivalence).Fix playeriand a historyh t. For opponents’
continuation profilesg−i,g′ −i∈F−i, write
g−i∼ht i g′ −i
if
Vi(σi|h t;g−i) =V i(σi|h t;g′ −i)for everyσ i∈F i(ht).
Equivalently,g−i andg′ −i induce the same continuation optimization problem for playeriafterht.
Therelevantlearningrequirementisthereforethat,ifaplayerkeepsfollowingasinglestrategy,theopponent
will eventually infer either that strategy itself or the strategically equivalent strategy class.
Assumption 3(Strategy menu identifiability).Fix playeri. Assume the support ofµ 0 i is finite; write
S−i := supp(µ 0 i )⊆F −i. This assumption concerns only the finite retained strategy menuS−i used by
playerifor posterior sampling; it is not a restriction on the full repeated-game strategy spaceF−i. Assume:
1.(Menu grain of truth)f−i∈S−i andµ 0 i (f−i)>0.
2.(On-path identifiability up to equivalent strategy class)If a player keeps following one strategy, then
the opponent will eventually infer either that strategy itself or the strategically equivalent strategy class.
Formally, for each historyht, define the strategically equivalent class
Ei(ht) :={g−i∈S−i :g−i∼ht i f−i}.
Then
µf
({
z:µ t i(Ei(ht(z))|h t(z))−→1 }) = 1.
Remark2.ForstrategymenususedinoursimulationsinSection7, Assumption3iseasilyjustified: weuse
deterministic,finite,non-duplicativestrategymenus,wherewrongretainedlabelsarehard-refutedoncethey
predict a different observed action, while labels that would share the same cooperative path and punishment
regime as the benchmark equilibrium automaton are excluded by construction. Appendix C.1 records this
14

stronger hard-refutation route, and Appendix I verifies it for the menus used in the experiment.
OnceAssumption3holds,theposteriormassinsidethetruecontinuation-payoffequivalenceclassisharmless
for PS-BR, because every label in that class induces the same continuation objective. Only posterior mass
outside that class can create an optimization gap. The proposition below shows that when this strategically
relevant posterior mass vanishes on the realized path, PS-BR delivers exactly the asymptotic on-pathε-
consistency required in Definition 4.
Proposition 4.2(PS-BR-selected continuation plans are asymptoticallyε-consistent on-path).Fix playeri.
Suppose playeriuses PS-BR at every history and Assumption 3 holds fori. Then for everyε>0,
µf
({
z:∃T i(z,ε)<∞s.t.∀t≥T i(z,ε), σPS i,t (·|h t(z))∈BR ε i ( fi,t −i ⏐⏐ ht(z)|h t(z) )}) = 1.
Proposition 4.2 is the formal resolution of the sampling-versus-best-response tension in LLM agents at the
level of theselected continuation plan. Standard stochastic decoding prevents exact best responding at
any fixed history. But the proposition shows that the continuation plan selected by PS-BR is eventually
approximately optimal along the realized path. That is the only role of the assumption in this subsection;
everythingelsefollowsfromthefactthatresidualuncertaintyinsidethetruecontinuation-payoffequivalence
class is already harmless for PS-BR.
The proof of Lemma 4.1 and the proof of Proposition 4.2 are deferred to Appendix C.
5 Zero-shot Nash convergence
We now show that the reasonably reasoning agents we defined in Section 4, together with a learnability
conditiononbeliefs,generateplaythatiseventuallyweaklyclosetoNashequilibriumplayalongtherealized
path. This argument follows the weak-subjective-equilibrium framework in Norman, 2022, adapted to the
LLM-agent setup discussed in Section 4.
5.1 Weak subjective equilibrium
We work with the standard weak distance on play-path distributions. LetBt be theσ-algebra generated by
cylinder events of lengtht.
Definition 7(Weak distance).For probability measuresµ,νover infinite play paths, define
d(µ,ν) :=
∞∑
t=1
2−t sup
E∈Bt
⏐⏐µ(E)−ν(E) ⏐⏐.
For a historyht withµ(C(h t))>0andν(C(h t))>0, define the conditional (continuation) weak distance
dht(µ,ν) :=d(µ(·|C(h t)), ν(·|C(h t))).
15

We use weak distance to compare continuations of play after a realized history.
Definition 8(Weak similarity in continuation).Fix a historyht. Two profilesfandgareη-weakly similar
in continuation afterht if
dht(µf,µg)≤η.
Weak subjective equilibrium is Norman’s key intermediate notion: players best respond (up toξ) to their
subjectivemodel, and their subjective model is weakly close (withinη) to the objective continuation distri-
bution.
Definition 9(Weak subjective equilibrium (Norman, 2022)).Fixξ,η≥0and a historyh t. A continuation
profilef
⏐⏐
ht isaweakξ-subjectiveη-equilibriumafterh t ifforeveryplayerithereexistsasupportingprofile
fi = (fi,f i −i)such that:
1.(Subjective best response)f i
⏐⏐
ht∈BR ξ i ( fi −i ⏐⏐ ht|h t) , where payoffs are evaluated underµfi .
2.(Weak predictive accuracy)d ht(µf,µfi )≤η.
Definition 10(Learns to predict the path of play (strong)).Playerilearns to predict the path of play under
fif for everyη >0,
µf
({
z:∃T i(z,η)<∞s.t.∀t≥T i(z,η), dht(z)(µf,µfi )≤η }) = 1,
wheref i = (fi,f i −i)is a supporting predictive profile for playeri(Section 3.3; formal construction in
Appendix A).
Remark3(ConnectiontoOptimizingLearnability).AlongstandingchallengeinBayesianlearningingames
is Nachbar (1997) and Nachbar (2005)’s inconsistency result, which shows that requiring an agent to learn
and best-respond onall possiblecontinuation paths is often mathematically impossible. However, Norman
(2022) resolved this by introducingoptimizing learnability, the insight that agents only need to learn the
continuationplayalongtherealizedpathsgeneratedbytheiroptimizingchoices. OurRRdefinitionnaturally
instantiates Norman’s insight: Definition 4 and Definition 10 requireε-consistency and predictive accuracy
strictlyµf-almostsurely(i.e.,strictlyontherealized,optimizingplaypath). Therefore,theon-pathmerging
ofopinionsguaranteedbyBlackwellandDubins(1962)isentirelysufficientforzero-shotNashconvergence,
bypassing Nachbar’s impossibility.
Crucially, the learning of the true path (strong path prediction) relies purely on the absolute continuity of
beliefs. Itdoesnotrequireexactstrategyidentification,anditislogicallydistinctfromtheequivalence-class
condition used for PS-BR. Strong path prediction can therefore be verified directly from Assumption 2 via
the classic merging of opinions result. The following Lemma 5.1 formalizes this idea.
Lemma 5.1(Absolute continuity implies strong path prediction).Fix playeri. Suppose the objective play-
16

path distributionµf is absolutely continuous with respect to playeri’s prior predictive distributionP0,fi i
(Assumption 2). Then playerilearns to predict the path of play underfin the sense of Definition 10.
The proof is deferred to Appendix C.
5.2 From learning to zero-shot Nash convergence
We first show that asymptoticε-consistency, together with strong prediction, implies that the realized
continuation play is eventually a weak subjective equilibrium.
Proposition 5.2.Suppose each playerisatisfies the asymptotic best-response condition from Definition 4
and learns to predict the path of play underf(Definition 10). Then for anyξ >0andη >0,
µf
({
z:∃T(z)<∞s.t.∀t≥T(z), f
⏐⏐
ht(z) is a weakξ-subjectiveη-equilibrium afterht(z) }) = 1.
Finally, we convert a weak subjective equilibrium into proximity to a Nash equilibrium.
Theorem5.3(Zero-shotNashconvergencealongrealizedplay).Supposeeveryplayersatisfiestheasymptotic
best-response condition from Definition 4 and learns to predict the path of play underf. Then for every
ε>0,
µf({ z:∃T(z)<∞s.t.∀t≥T(z),∃ ˆfε,t,z anε-Nash equilibrium
of the continuation game afterht(z)withd ht(z)(µf,µ ˆfε,t,z )≤ε }) = 1.
Corollary5.4(Zero-shotNashconvergenceforPS-BR).Assumethatforeveryplayeri,Assumption3holds
and playeriuses PS-BR (Definition 5). Assume moreover that, in the continuation game after each reached
history, the continuation actually played is the PS-BR plan selected at that history. Then the conclusion of
Theorem 5.3 holds.
The proofs of Theorem 5.3 and Corollary 5.4 are deferred to Appendix C. For the sparse simulation
menus used in our applications, Appendix C.1 shows that the needed concentration premise follows from
deterministic hard refutation on the finite menu. The richer engineering rollout menu may be broader; our
identification claim is only for the sparse appendix menu.
Themainabstracttheorem,Theorem5.3,togetherwiththePS-BRcorollary5.4,mayseemcounterintuitive:
ifeachagentislearning,thenwhateachagentistryingtopredictchangesovertime,sowhyshouldbehavior
everstabilize? Thisconcernisvalidformanymyopiclearningmodels,wherethelearnertreatstheopponent
as having a fixed action distribution even though the opponent is also adapting. The promise of Bayesian
learning (Kalai and Lehrer, 1993a) is that, under a suitable grain-of-truth condition, agents’posterior
predictiveforecasts about future play can nonetheless become accurate (merge) along the realized path.
In repeated games, the correct object of inference is not a fixed action, but the opponent’srepeated-game
17

strategy: afixedcontingentplan(mappinghistoriestoactions)thatmaybehighlynonstationary. Inparticular,
evenifanopponentupdatesbeliefsandchangesitsperiod-by-periodbestresponse,onceitsprior,updaterule,
and decision rule are fixed from time 0, its behavior defines a single mappingf−i :H→∆(A −i)(hence
a fixed repeated-game strategy in our sense). Agents’ beliefs change because they refine uncertainty about
this fixed mapping (and its on-path implications), not because the mapping is being rewritten exogenously
over time.
Indeed,ourmainresultsdonotrequirethatposteriorsoveropponentstrategiesliterallystopmoving. Instead,
they require on-path stabilization in two weaker senses:
1.Stability of forecasts (predictive merging).Under the grain-of-truth condition (Assumption 2), Bayesian
updating implies that, alongµf-almost every realized historyht(z), the agent’sposterior predictive
distribution over future play becomes close to the true continuation distribution (formalized later by
Definition 10 and Lemma 5.1). Importantly, this can happen even if the posterior overstrategy labels
doesnotconcentrate: distinctstrategyhypothesesmaybeobservationallyequivalentontherealizedpath,
and any remaining disagreement can persist only on counterfactual histories that are not reached.
2.Stability of (approximate) best responses.Once an agent’s predictive belief about continuation play
is accurate on-path, playing anε-best response to that belief is also nearly optimal against the true
continuation play. Moreover, best-responsesetsneed not vary wildly: when the payoff gap between the
best action and the runner-up is nontrivial, small changes in beliefs do not change which continuation
strategies areε-optimal. This is exactly why our RR definition imposes onlyasymptoticon-pathε-
consistency (Definition 4), rather than requiring perfect best-response optimality at every time and every
counterfactual history.
Even if beliefs keep updating forever, behavior can still stabilize because decisions depend on thepredictive
implications of beliefs on the realized continuation game. If the posterior mass shifts among hypotheses
that induce (nearly) the same continuation distribution afterht(z), then the agent’s best-response problem
is (nearly) unchanged, so play remains stable. For our sampled-label PS-BR implementation, we formalize
exactly this logic through the equivalence-class condition in Assumption 3: the posterior may keep moving,
butonlynegligiblemasscanremainonretainedlabelsthatwouldinduceadifferentcontinuationoptimization
problem. The proof of Proposition 4.2 then shows that the resulting sampling randomness is strategically
innocuous, because the induced best-response gap is bounded by twice the posterior mass outside the true
equivalence class. This yields eventual on-pathε-best-response continuation plans.
5.3 Zero-shot stage-game Nash convergence for myopic rules
Theorem 5.3 and Corollary 5.4 establish eventual on-path convergence to a Nash equilibrium of the con-
tinuation game. That guarantee is deliberately strong: it concerns repeated-game optimality and therefore
requires beliefs over opponents’ full continuation strategies. Yet this level of reasoning may be unnecessary
when the object of interest is onlystage-wisestrategic optimality. If we ask instead whether the realized
18

mixed action profile at each history is eventually an approximate Nash equilibrium of the one-shot stage
game, then predicting the opponents’ next joint action may suffice. This reduction captures the logic of
SCoT (Akata et al., 2025), which implements a “predict the next move, then best respond” procedure rather
than full continuation planning. The purpose of this subsection is to justify this simplification formally. We
analyzetwoone-stepvariants: myopicPS-BR,whichbestrespondstoaone-steppredictivebelief,andSCoT
(Akata et al., 2025), which best responds to a deterministic point prediction of the opponents’ next action.
5.3.1 Myopic PS-BR
myopic PS-BRretains the Bayesian-learning-plus-best-response structure of the previous subsection, but
truncates both objects to one period: the agent forms a one-step predictive belief over the opponents’ next
joint action and then plays a myopic best response to that belief.
For notational convenience, as already used above, for any opponents’ profileg−i and historyh, we write
g−i(h)∈∆(A −i)
for the induced distribution over the opponents’ joint next action at historyh. In particular, wheng−i is an
actual profile of opponents’ mixed actions, this is the product distribution
g−i(h) =
⨂
j̸=i
gj(h).
Definition 11(One-shot stage-gameε-best response and stageε-Nash).Forαi∈∆(A i)andq∈∆(A −i),
define
ui(αi,q) :=
∑
ai∈Ai
∑
a−i∈A−i
αi(ai)q(a−i)ui(ai,a−i).
Forε≥0, define
brε i (q) :=
{
αi∈∆(A i) :u i(αi,q)≥sup
α′ i∈∆(Ai)
ui(α′ i,q)−ε
}
.
We also write
bri(q) := br0 i (q).
At a historyht, write
f−i(ht) := ⨂
j̸=i
fj(ht)∈∆(A −i)
for the actual current joint mixed action of playeri’s opponents. The current mixed-action profile
f(ht) := (f1(ht),...,f N(ht))∈ ∏
j∈I
∆(Aj)
19

is astageε-Nash equilibriumif
fi(ht)∈br ε i ( f−i(ht) ) for everyi∈I.
Fix playeriand letf i = (fi,f i −i), wherefi −i is the prior-predictive reference model from Section 3.3. Let
fi,t −i denote a continuation model reproducing playeri’s predictive continuation law at historyht. We write
qt i(·|h t) :=f i,t −i(ht)∈∆(A −i)
for playeri’s one-step posterior predictive belief about the opponents’ next joint action. When the posterior
µt i(·|h t)is supported on a finite setS−i⊆F−i, this is
qt i(·|h t) = ∑
g−i∈S−i
µt i(g−i|h t)g−i(ht)(·).
Definition 12(Myopic posterior-sampling best response (myopic PS-BR)).Fix playeriand a historyht.
Supposeµt i(·|h t)is supported on a finite setS−i. For eachg−i∈S−i, choose a mixed action
αg−i,ht i ∈br i ( g−i(ht) ) .
Myopic PS-BR:
1. samples ˜f−i∼µ t i(·|h t);
2. uses the mixed actionα
˜f−i,ht
i .
The induced ex ante mixed action is
αmPS i,t (·|h t) := ∑
g−i∈S−i
µt i(g−i|h t)αg−i,ht i (·).
Whenever playeriuses myopic PS-BR, we identify
fi(ht) =α mPS i,t (·|h t).
Lemma 5.5(Stage best responses are stable under nearby beliefs).Fix playeriand define
∥p−q∥ TV := sup
B⊆A−i
|p(B)−q(B)|forp,q∈∆(A −i).
Ifαi∈br ξ i (q), then
αi∈br ξ+2∥p−q∥ TV i (p).
20

Lemma 5.6(Myopic PS-BR is aDt i-stage best response).Fix playeriand a historyht. Supposeµt i(·|h t)
is supported on a finite setS−i and write
pt(g−i) :=µ t i(g−i|h t), g −i∈S−i.
Define
Dt i(ht) := 1− ∑
g−i∈S−i
pt(g−i)2.
Letα mPS i,t (·|h t)be myopic PS-BR and let
qt i(·|h t) = ∑
g−i∈S−i
pt(g−i)g−i(ht)(·)
be the one-step posterior predictive belief. Then
ui
(
αmPS i,t , qt i(·|h t) ) ≥sup
αi∈∆(Ai)
ui
(
αi, qt i(·|h t) ) −Dt i(ht).
Equivalently,
αmPS i,t (·|h t)∈br Dt i(ht) i ( qt i(·|h t) ) .
Lemma 5.7(Strong path prediction implies one-step predictive accuracy).Fix playeri. Suppose playeri
learns to predict the path of play underf(Definition 10). Then
µf
({
z:∀η >0,∃T i(z,η)<∞s.t.∀t≥T i(z,η),
‖‖qt i(·|h t(z))−f −i(ht(z)) ‖‖ TV≤η }) = 1.
For stage-game Nash convergence, exact identification of the opponents’ full continuation strategy is again
stronger than needed. What matters is only whether the retained labels induce the sameone-step stage
decision problemat the reached history. The relevant comparison is now myopic rather than intertemporal:
two labels are equivalent if, at the current history, they make every current mixed action deliver the same
expectedstagepayofftoplayeri. Inthatcase,distinguishingbetweenthemhasnoeffectonthecurrentstage
best-response problem.
Definition13(On-pathstage-payoffequivalence).Fixplayeriandahistoryh t. Foropponents’continuation
profilesg−i,g′ −i∈F−i, write
g−i≈ht i g′ −i
if
ui(αi,g−i(ht)) =u i(αi,g′ −i(ht))for everyα i∈∆(A i).
Equivalently,g−i andg′ −i induce the same one-step stage optimization problem for playeriat historyht.
21

Assumption 4(Strategy identifiability).Fix playeri. Assume the support ofµ0 i is finite; write
S−i := supp(µ0 i )⊆F −i.
This assumption again concerns only the finite retained strategy menuS−i used for posterior sampling, not
the full strategy spaceF−i. Assume:
1.(Menu grain of truth)f−i∈S−i andµ 0 i (f−i)>0.
2.(On-path concentration only up to stage-payoff equivalence)For each historyht, define
Est i (ht) :={g−i∈S−i :g−i≈ht i f−i}.
Then
µf
({
z: 1−µ t i(Est i (ht(z))|h t(z))−→0 }) = 1.
As in the continuation-value case, Assumption 4 is a menu-level condition and does not require exact
identification of the literal opponent label. It requires only that, on the realized path, posterior mass within
theretainedmenueventuallyfallsonlabelsthatarestage-payoff-equivalenttothetruthatthereachedhistory.
Any residual posterior uncertainty inside that one-step equivalence class is harmless for myopic PS-BR,
because it leaves the current stage optimization problem unchanged.
Lemma 5.8(Stage-equivalence concentration controls the myopic PS-BR gap).Fix playeriand a history
ht. Let
βt i(ht) := 1−µ t i(Est i (ht)|h t),
whereE st i (ht)is the true stage-payoff equivalence class from Assumption 4. LetαmPS i,t (·|h t)be myopic
PS-BR. Then
ui
(
αmPS i,t , f−i(ht) ) ≥sup
αi∈∆(Ai)
ui
(
αi, f−i(ht) ) −β t i(ht).
Equivalently,
αmPS i,t (·|h t)∈br βt i(ht) i ( f−i(ht) ) .
The proof logic is the exact myopic analogue of the continuation-level PS-BR argument above. Posterior
mass on the true stage-payoff equivalence class is strategically harmless, because every label in that class
induces the same current stage payoff function over playeri’s mixed actions. Only the remaining posterior
mass on stage-distinct labels can create a myopic best-response gap.
Theorem 5.9(Stage-game Nash convergence under myopic PS-BR).Assume that for every playeri, As-
22

sumption 4 holds and playeriuses myopic PS-BR (Definition 12) at every history. Then for everyε>0,
µf
({
z:∃T(z)<∞s.t.∀t≥T(z), f(h t(z))is a stageε-Nash equilibrium }) = 1.
5.4 SCoT (Akata et al., 2025)
The secondreduction isSCoT (Akataet al., 2025). Insteadof bestresponding tothe full one-steppredictive
distribution,theagentfirstformsadeterministicpointpredictionoftheopponents’nextjointactionandthen
best responds to that point prediction. In general, this is not equivalent to best responding to a mixed belief,
so the argument is different from the classical Bayesian-learning-plus-best-response route. Nevertheless,
when all players use deterministic point-prediction rules, the true next action along the realized path is pure
at every history, and predictive accuracy is enough to make the point prediction eventually correct. This
gives eventual stage-game Nash convergence under a different mechanism than myopic PS-BR.
Definition 14(Social Chain of Thought (SCoT) (Akata et al., 2025)).Fix playeri. At each historyht, let
qt i(·|h t) :=f i,t −i(ht)∈∆(A −i)
denote playeri’s one-step predictive distribution over opponents’ next joint action.
ASCoTrule for playericonsists of:
1. a deterministic MAP (maximum a posteriori) selector
ˆat −i(ht)∈arg max a−i∈A−i qt i(a−i|h t);
2. a deterministic pure best-response selector
bi :A−i→A i such thatb i(a−i)∈arg max ai∈Ai ui(ai,a−i)for everya −i∈A−i.
The induced strategy is
fi(ht) :=δ bi(ˆat −i(ht))∈∆(A i).
Thus a SCoT player uses a pure action at every history.
Lemma 5.10(Deterministic truth implies asymptotic purity and eventual MAP correctness).Fix playeri
andsupposeplayerilearnstopredictthepathofplayunderfinthesenseofDefinition10. Assumethatfor
every historyh∈Hthere exists an actiona ⋆ −i(h)∈A −i such that
f−i(h) =δ a⋆ −i(h).
23

Then
µf
({
z:∃T i(z)<∞s.t.∀t≥T i(z),ˆat −i(ht(z)) =a ⋆ −i(ht(z)) }) = 1.
In particular, alongµf-almost every realized pathz,
qt i ( a⋆ −i(ht(z))|h t(z) ) −→1and1−max a−i∈A−i qt i(a−i|h t(z))−→0.
Theorem 5.11(One-shot stage-game Nash convergence for SCoT).Suppose every playeri∈Iuses SCoT
inthesenseofDefinition14,andsupposeeveryplayerlearnstopredictthepathofplayunderfinthesense
of Definition 10. Then
µf
({
z:∃T(z)<∞s.t.∀t≥T(z), f(h t(z))is a stage Nash equilibrium }) = 1.
Equivalently, alongµf-almost every realized path, the current mixed-action profile eventually becomes a
stage0-Nash equilibrium.
Corollary5.12(Bayesianstage-gameNashconvergenceforSCoT).Supposeeveryplayerusesdeterministic
MAP-SCoT and Assumption 2 holds for every player. Then the conclusion of Theorem 5.11 holds:
µf
({
z:∃T(z)<∞s.t.∀t≥T(z), f(h t(z))is a stage Nash equilibrium }) = 1.
Remark4.Theorem 5.11 relies on the fact that whenall playersuse SCoT with deterministic tie-breaking,
the true current action profile is pure at every history. This is why asymptotic purity need not be imposed
separately: it is implied by Bayesian one-step predictive accuracy toward a pure truth. If opponents are
allowed to play genuinely mixed current actions, this argument breaks down, and additional conditions such
as asymptotic purity or BR-invariance are again needed.
The SCoT result is therefore naturally paired with the grain-of-truth assumption (Assumption 2) and the
corresponding merging-of-opinions argument, rather than with Assumptions 3 and 4, which are tailored to
posterior-sampling rules such as PS-BR and myopic PS-BR.
The proofs are deferred to Appendix C. Taken together, Theorem 5.9 and Theorem 5.11 show that, for the
weaker objective ofstage-gameNash convergence, full continuation planning is not necessary. However,
these one-step results are inherently limited to stage-game equilibrium. They do not by themselves recover
more demandingcontinuation-gameorhistory-contingent repeated-gameequilibria, whose incentive struc-
tureissustainedbythevalueoffuturepathsofplay. Establishingconvergencetothosericherrepeated-game
equilibriarequiresaprocedure,suchasPS-BR,thatreasonsoverfullcontinuationstrategiesratherthanonly
over the next-period action.
24

6 Extension to unknown, stochastic, and private payoffs
Sections 3–5 assumed that the stage payoff functionsui :A→[0,1]are common knowledge and determin-
istic. Wenowdropthatassumptionandalloweachagenttoobserveonlyitsownprivatelyrealizedstochastic
payoffs. Thekeysimplifyingchoiceinthisextensionisthatthecontinuationgameisstillevaluatedonpublic
histories: privatereward histories areused to updatea posterior overplayeri’s ownmean payoffmatrix, but
the continuation strategies being compared remain public-history strategies, exactly as in Section 3. This
keeps the equilibrium benchmark on the realized public play path and removes the need for an additional
hidden-history-collapse assumption.
6.1 Private-payoff repeated game and observable histories
Fix the same action sets(Ai)i∈I and discount factors(λi)i∈I as in Section 3. For each playeri, letRi⊆R
denotethepayoffspaceandletν i(dr)beadominatingbasemeasure(countingmeasureinthediscretecase,
Lebesgue measure in the continuous case).
We assume that the payoff noise family is known. Concretely, for each playerithere is a known family of
densities
ψi(r;µ), r∈R i, µ∈R,
where the parameterµis the mean payoff. The true unknown object is playeri’s mean payoff matrix
ui :A→[0,1].
(Asusual, anyboundedpayoff matrixcanbeaffinely normalizedinto[0,1]withoutchangingbest responses
or Nash inequalities.)
At roundt, after the public joint actionat∈Ais realized, playeriprivately observes
rt i∼q ui i (·|a t),whereq ui i (dr|a) :=ψ i(r;ui(a))νi(dr).(4)
Thus the true payoff kernel is determined by the true mean matrixui.
For payoff learning, playeri’s observable history at timetis
xt i := (ht,r 1:t−1 i )∈X t i :=H t×Rt−1 i , X i := ⋃
t≥1
Xt i.
The continuation plans remain the public history strategies from Section 3: after a realized public history
ht, candidate continuation plans are elements ofFi(ht).
The full sample space is
Ω :=
∏
t≥1
(
A×
∏
i∈I
Ri
)
,
25

whose typical element is
ω= (a 1,r 1,a 2,r 2,...), r t = (rt 1,...,r t N).
We writeht(ω) = (a1,...,a t−1)andx t i(ω) = (ht(ω),r 1:t−1 i (ω)).
Letβ i :X i→∆(A i)denote playeri’s actual one-step behavioral rule in the private-payoff environment,
and letβ= (β i)i∈I. Together with the true mean matricesu= (ui)i∈I, the behavioral profileβinduces a
unique lawPβ,u onΩ 1.
The induced public-history strategy profilef= (fi)i∈I∈Fis then defined by
fi(ht) :=P β,u(at i∈·|h t), i∈I.
Its public-action law is exactly the public marginal ofPβ,u, which we denote byµf.
Because continuation play is evaluated on public histories, the relevant continuation payoff afterht is
Uui i (g|h t) :=E y∼µg ht
[
(1−λ i)
∞∑
k=0
λk iui(yk+1)
]
,
for any continuation profilegafterht. A continuation profileg ⏐⏐ ht is anε-Nash equilibrium of the private-
payoff continuation game afterht if, for everyi∈I,
Uui i (g|h t)≥sup
g′ i∈Fi(ht)
Uui i (g′ i,g−i|h t)−ε.
6.2 Known-noise, unknown-mean parametrization
We now impose the finite-menu structure used by PS-BR. For playeri, letMi be a finite menu of candidate
mean payoff matrices
mi :A→[0,1].
Eachmi∈M i induces a payoff kernel
qmi i (dr|a) :=ψ i(r;mi(a))νi(dr).
Thus sampling a payoff-matrix label is exactly sampling a payoff kernel, expressed in mean-matrix coordi-
nates.
1This is by the Ionescu–Tulcea theorem (Ionescu Tulcea, 1949); see Pollard, 2002 also.
26

Givenxt i = (ht,r 1:t−1 i ), playeri’s posterior over candidate mean matrices is
πt i(mi|x t i)∝π 0 i (mi)
t−1∏
s=1
ψi(rs i ;mi(as)), m i∈M i.(5)
As in Sections 4–5, we model playeri’s beliefs about the opponents through a finite menu of public-action
continuation models
g−i :H→∆(A −i).
LetS−i denote the finite retained menu and let
µt i(·|h t)
be playeri’s posterior overS−i.
6.3 Subjective continuation values and PS-BR
Fix playeri, an observable historyxt i = (ht,r 1:t−1 i ), an opponents’ continuation modelg−i∈S−i, and a
continuation strategyτi∈F i(ht).
Because continuation play is public-history based, a candidate mean matrix affects only the continuation
objective, not the induced public-action law. We therefore define themi-subjective continuation value by
Vmi i (τi|h t;g−i) :=E y∼µ (τi,g−i) ht
[
(1−λ i)
∞∑
k=0
λk imi(yk+1)
]
.(6)
Forε≥0, define
BRε i,mi(g−i|h t) :=
{
τi∈F i(ht) :V mi i (τi|h t;g−i)≥sup
τ′ i∈Fi(ht)
Vmi i (τ′ i|h t;g−i)−ε
}
,
and write
BRi,mi(g−i|h t) := BR0 i,mi(g−i|h t).
Playeri’s mixed subjective continuation value is
V mix,t i (τi|x t i) :=E g−i∼µt i(·|ht)
mi∼πt i(·|xt i)
[
Vmi i (τi|h t;g−i) ] .(7)
For the true mean matrixui, define
Vui,t i (τi|x t i) :=E g−i∼µt i(·|ht) [ Vui i (τi|h t;g−i) ] .(8)
27

Letg i,t −i denote any representative continuation model for the posterior predictive continuation law induced
byµt i(·|h t). Concretely,gi,t −i is chosen so that for every continuation strategyτi∈F i(ht),
Vui,t i (τi|x t i) =V ui i (τi|h t;gi,t −i).(9)
WhenS−i ={g 1 −i,...,g K −i}is finite, one convenient choice is
gi,t −i(h)(a−i) =
K∑
k=1
µt,h i (gk −i)gk −i(h)(a−i), h⪰h t,
whereµt,h i is the continuation posterior obtained by updatingµt i(·|h t)along the continuation historyh.
Because payoff uncertainty affects only the continuation objective, not the induced public transition law of
a fixed continuation strategy, playeri’s posterior predictive law over future public action paths under the
realized continuationfi
⏐⏐
ht is simply
Πt i(·|x t i) :=µ (fi,gi,t −i) ht .(10)
We can now state the private-payoff PS-BR rule.
Definition15(Posterior-samplingbestresponse(PS-BR)withprivatepayoffs).Fixplayeriandanobservable
historyxt i = (ht,r 1:t−1 i ). Given: (i)theposteriorµt i(·|h t)overopponents’continuationmodels,and(ii)the
posteriorπ t i(·|x t i)over playeri’s own mean payoff matrices, PS-BR chooses apublic-history continuation
strategyby:
1. sample an opponents’ continuation model˜g−i∼µ t i(·|h t);
2. sample a mean payoff matrix˜mi∼π t i(·|x t i);
3. play any continuation strategyτi∈BR i,˜mi(˜g−i|h t).
Denotetheresultingrandomizedcontinuationstrategybyσ PS i,t (·|x t i). Itscurrent-roundprescriptioninduces
the actual one-step behavioral rule via
βi(xt i) :=σ PS i,t (ht),
and the induced public-history profilefis defined from the resulting actual lawPβ,u as above.
6.4 Learning requirements in the private-payoff game
The opponent-side learning object is the same public continuation problem as in Section 4.2, now evaluated
under playeri’s true mean matrixui.
Fix playeriand let
S−i := supp(µ0 i )⊆F −i
28

be the finite retained opponents’ menu used by playerifor posterior sampling. For each public historyht,
define
Epriv i (ht) := { g−i∈S−i :V ui i (τi|h t;g−i) =V ui i (τi|h t;f−i)for everyτi∈F i(ht) } .
ThusE priv i (ht)is the true continuation-payoff equivalence class in the private-payoff extension after public
historyh t.
Assumption 5(Private-payoff analogue of Assumption 3).Using the retained opponents’ menuS−i above,
assume:
1.(Menu grain of truth)f−i∈S−i andµ 0 i (f−i)>0.
2.(On-path learnability up to equivalence)AlongPβ,u-almost every realized path,
µt i(Epriv i (ht(ω))|h t(ω))−→1.
Asbefore,AppendixC.1recordsstrongersufficientroutesviaretained-menuidentificationanddeterministic
hard refutation of wrong retained public-action labels.
On the payoff side, the relevant object is again a continuation-decision class rather than literal identification
of the retained mean matrix.
Definition 16(On-path payoff equivalence).Fix playeriand a public historyht. Let
S−i := supp(µ0 i )⊆F −i
be playeri’s retained opponents’ menu, and letgi,t −i be the posterior-predictive representative continuation
model from Section 6.3. For candidate mean matricesmi,m′ i∈M i, write
mi≈ht i m′ i
if for every opponents’ continuation model
g−i∈S−i∪{g i,t −i}
the equality
Vmi i (τi|h t;g−i) =V m′ i i (τi|h t;g−i)for everyτ i∈F i(ht)
holds. Equivalently,m i andm ′ i induce the same continuation optimization problem for every retained
opponents’ model that can matter for PS-BR afterht.
29

Assumption 6(Pointwise public-history payoff learnability).Fix playeriand let
Mi := supp(π0 i )
be the finite retained mean-payoff menu used by playerifor posterior sampling. This assumption concerns
onlyplayeri’sownretainedpayoffmenu,nottheopponents’payoffmatricesandnotthefullspaceofpayoff
kernels. For each public historyht, define
Ui(ht) :={m i∈M i :m i≈ht i ui}.
For each observable historyxt i = (ht,r 1:t−1 i ), define the pointwise payoff-learning error
δt i(xt i) := 1−π t i(Ui(ht)|x t i).
Assume:
1.(Menu grain of truth)The true mean matrixui∈M i andπ 0 i (ui)>0.
2.(On-path concentration up to payoff equivalence)AlongPβ,u-almost every realized path,
δt i(xt i(ω))−→0.
For every public historyht, let
αt i(ht) := 1−µ t i(Epriv i (ht)|h t).
Thusα t i(ht)is the opponents-side learning error, whileδ t i(xt i)is the own-payoff continuation-decision
learning error at the realized observable historyxt i = (ht,r 1:t−1 i ). Because continuation strategies are
public-history based, payoff uncertainty affects the player’s continuation objective but not the induced
predictive public-action law: for every observable historyxt i = (ht,r 1:t−1 i ),
Πt i(·|x t i) =µ (fi,gi,t −i) ht .
6.5 PS-BR gap and asymptotic consistency
The asymptotic-consistency argument now has the same shape as before, but with two distinct error terms.
Theopponent-sideerrorα t i(ht)measuresposteriormassonretainedpubliccontinuationmodelsthatremain
strategically distinct under the true mean matrix. The payoff-side errorδt i(xt i)measures posterior mass
outside the true own-payoff continuation-decision class.
Let
pt(g−i,mi) :=µ t i(g−i|h t)πt i(mi|x t i),(g −i,mi)∈S −i×Mi.
30

Define the joint collision complement
Dt,joint i (xt i) := 1− ∑
(g−i,mi)∈S−i×Mi
pt(g−i,mi)2.
Lemma6.1(PS-BRisaD t,joint i -bestresponsetothemixedsubjectivevalue).Fixplayeriandanobservable
historyx t i = (ht,r 1:t−1 i ). Letσ PS i,t be PS-BR from Definition 15. Then
V mix,t i (σPS i,t |x t i)≥sup
τi∈Fi(ht)
V mix,t i (τi|x t i)−D t,joint i (xt i).
Equivalently,σ PS i,t is aDt,joint i (xt i)-best response to the mixed subjective continuation value(7).
Because continuation values are normalized to lie in[0,1], and hypotheses insideUi(ht)leave the relevant
subjective continuation-value functional unchanged, for everyτi∈F i(ht),
⏐⏐V mix,t i (τi|x t i)−V ui,t i (τi|x t i) ⏐⏐≤δ t i(xt i).(11)
Lemma 6.2(PS-BR gap under opponents’ equivalence and payoff concentration).Fix playeriand an
observable historyxt i = (ht,r 1:t−1 i ). Letσ PS i,t be PS-BR from Definition 15. Then
Vui,t i (σPS i,t |x t i)≥sup
τi∈Fi(ht)
Vui,t i (τi|x t i)−2α t i(ht)−4δ t i(xt i).
Equivalently,σ PS i,t isa ( 2αt i(ht) + 4δt i(xt i) ) -bestresponsetothetrue-meansubjectivecontinuationvalue(8).
Proposition 6.3(PS-BR-selected continuation plans are asymptoticallyε-consistent in the private-payoff
game).Fix playeri. Assume: (i) Assumption 5 holds for playeri’s finite retained menu of opponents’
continuation models, (ii) Assumption 6 holds for playeri’s own finite retained mean-matrix menu, and (iii)
playeriuses PS-BR at every observable history. Then for everyε>0,
Pβ,u
({
ω:∃T i(ω,ε)<∞s.t.∀t≥T i(ω,ε), σPS i,t (·|x t i(ω))∈BR ε i,ui ( gi,t −i|h t(ω) )}) = 1.
6.6 Zero-shot Nash convergence with private payoffs
The zero-shot argument now lifts directly to the public continuation game at the abstract level. Because
the continuation strategies being compared are public-history based, the player’s observable historyxt i =
(ht,r 1:t−1 i )affects future public play only through belief updating. No additional assumption is needed to
collapse hidden private histories into a single public continuation law.
The theorem below is the abstract private-payoff analogue of Theorem 5.3: it concerns the induced public-
history strategy profilefitself. Proposition 6.3 should therefore be read as a planner-side result about the
31

continuationplanselectedbyPS-BRatarealizedobservablehistory. Toconvertthatselected-planstatement
into an actual-behavior result for a particular implementation, one needs the implementation to execute the
selected continuation plan as the continuation after the current public history.
Becausecontinuationplayispublic-historybased,noseparateobservable-processgrain-of-truthassumption
is needed in this section. The menu grain-of-truth part of Assumption 5 already implies the ordinary public
grain-of-truth condition: sincef−i∈S−i withµ 0 i (f−i)>0, the prior predictive public play-path law under
fi assigns positive mass to the true continuation law.
Lemma 6.4(Menu grain of truth implies strong public-path prediction in the private-payoff game).Fix
playeri. Under the menu grain-of-truth part of Assumption 5,
d
(
Πt i(·|x t i(ω)),µf ht(ω) ) −→0forP β,u-a.e.ω.
The proof is deferred to Appendix C.
Definition 17(Weak subjective equilibrium in the private-payoff game).Fixξ,η≥0and a public history
ht. Acontinuationprofileg ⏐⏐ ht isaweakξ-subjectiveη-equilibriumafterh t if,foreveryplayeri,thereexists
a supporting profilegi = (gi,gi −i)such that
1.(Subjective best response)g i
⏐⏐
ht∈BR ξ i,ui(gi −i|h t).
2.(Weak predictive accuracy)d ht(µg,µgi )≤η.
Proposition 6.5(Learning and asymptotic consistency imply weak subjective equilibrium in the private–
payoff game).Suppose that, for every playeriand everyξ >0,
Pβ,u
({
ω:∃T i(ω,ξ)<∞s.t.∀t≥T i(ω,ξ), fi
⏐⏐
ht(ω)∈BR ξ i,ui ( gi,t −i|h t(ω) )}) = 1,
and suppose Lemma 6.4 holds for every player. Then for everyξ >0andη >0,
Pβ,u
({
ω:∃T(ω)<∞s.t.∀t≥T(ω), f
⏐⏐
ht(ω) is a weakξ-subjectiveη-equilibrium afterht(ω) }) = 1.
Theorem 6.6(Zero-shot Nash convergence with private payoffs).Assume that, for every playeriand every
ξ >0,
Pβ,u
({
ω:∃T i(ω,ξ)<∞s.t.∀t≥T i(ω,ξ), fi
⏐⏐
ht(ω)∈BR ξ i,ui ( gi,t −i|h t(ω) )}) = 1,
and suppose Lemma 6.4 holds for every player. Then for everyε>0,
Pβ,u
({
ω:∃T(ω)<∞s.t.∀t≥T(ω),∃ ˆfε,t,ω anε-Nash equilibrium of the continuation game
32

afterh t(ω)withd ht(ω)
(
µf,µ ˆfε,t,ω) ≤ε }) = 1.
Theorem 6.6 is the direct private-payoff analogue of Theorem 5.3. Because the continuation game remains
public-history based, private payoff observations affect the theorem only through the player’s posterior over
its own retained mean-payoff menu. The payoff-learning problem remains entirely own-payoff: each player
learns its own retained mean-payoff menu only up to the on-path continuation-decision class relevant for
continuation optimality, not the opponents’ payoff matrices and not necessarily every off-path entry of its
own matrix.
7 Experiments
In this section, we empirically evaluate whether off-the-shelf reasoning LLM agents exhibit the theoretical
properties derived in previous sections, i.e., whether they converge toward Nash equilibrium behavior
in repeated strategic interaction. After discussing the experiment setup common to all simulations in
Section 7.1, we study three empirical implications of the theory:
1. For convergence to some equilibrium-consistent late-run behavior, simple predict–then–act reasoning
may already be sufficient (Section 7.2).
2. For convergence to aparticularnontrivial repeated-game cooperative equilibrium sustained by con-
tinuation incentives, myopic approaches should generally fail, whereas PS-BR should succeed once
equilibrium-selection frictions are reduced (Section 7.3).
3. PS-BRshouldremaineffectiveevenwhenthepayoffmatrixisnotgivenexanteandmustbelearnedfrom
noisy private payoff observations (Section 7.4).
7.1 Setup
Baselines.We use Qwen 3.5-27B (Qwen Team, 2026), a small-scale open-source LLM. The empirical
design is a controlled within-model intervention: we hold fixed the underlying model, game description,
public history, role mapping, and strategy-label context, and vary only the reasoning procedure applied to
thatcommoninformation. Thus,themaincomparisonsareintendedtoisolatetheeffectofaddingreasoning
on top of the same model and task interface, rather than differences in model scale, training, or task-specific
prompt optimization. We evaluate three decision procedures:
•Base: directactionselectionfromthecommonrules,history,andstrategy-labelcontext(prompttemplates
in Appendix G.1). To isolate the behaviors of LLM without reasoning, we explicitly suppress the default
reasoning capabilities of Qwen 3.5-27B.
•SCoT: chain-of-thought style “predict–then–act” prompting (Akata et al., 2025) added on top of Base.
This is a natural empirical benchmark for the one-step reasoning result in Section 5.3; it uses the same
rules, history, and strategy-label context, but separates opponent-action prediction from action choice
33

(Appendix G.2).
•PS-BR: Reasonable reasoning (posterior-sampling best response) added on top ofBase(Definition 5;
implementation details in Appendix E). It uses the same game, history, and strategy-label information to
infer an opponent strategy label, then chooses actions by rollout-based strategy evaluation; the known-
payoff prompt is in Appendix G.3, and the unknown-payoff prompt/configuration is in Appendix G.4.
Benchmarks.We consider five repeated-game environments in total: BoS, PD, Promo, Samaritan, and
Lemons.
(1) Battle of the Sexes (BoS; coordination with asymmetric equilibria).Actions each period:JorF.
Per-period payoff matrix (Player 1, Player 2):
P2:JP2:F
P1:J (10,7) (0,0)
P1:F (0,0) (7,10)
The non-trivial cooperative Nash equilibrium (pure):(J,J)and(F,F). One non-trivial cooperative Nash
equilibrium is both of them sticking to one action:
•PlayJafter every history (outcome(J,J)every period).
•PlayFafter every history (outcome(F,F)every period).
Suchanon-trivialcooperativeNashequilibriumisparticularlyplausiblewhenamonetarytransferunderlies
the game. Another non-trivial cooperative Nash equilibrium is turn-taking:
•Play(J,J)in odd periods and(F,F)in even periods.
•After any history, continue the same odd/even phase convention.
(2) Prisoner’s Dilemma (PD; social dilemma).Actions each period:JorF. Per-period payoff matrix
(Player 1, Player 2):
P2:JP2:F
P1:J (3,3) (−5,5)
P1:F (5,−5) (0,0)
One-shot stage-game Nash equilibrium:(F,F). A baseline pure Nash equilibrium of the repeated game is
stationaryplayof(F,F)aftereveryhistory. Anontrivialcooperativebenchmarkstrategyprofileusedinthe
empirical PS-BR implementation is a contrite finite-punishment rule:
•Cooperative phase: play(J,J)every period.
•If a player choosesJwhile the opponent choosesF, the exploited player switches toFfor three rounds
and then returns toJ.
34

•A player who previously choseFagainstJdoes not counter-retaliate during the opponent’s three-round
retaliation window; after that window ends, both players return to(J,J).
(3) Promo (Lal, 1990, Appendix J.1)Actions each period:R(Regular),P(Promotion), orZ(price-war
punishment). Per-period payoff matrix (Player 1, Player 2):
P2:RP2:PP2:Z
P1:R (1,1) (−1,4) (−2,−2)
P1:P (4,−1) (0,0) (−2,−2)
P1:Z (−2,−2) (−2,−2) (−2,−2)
One-shot stage-game Nash equilibrium (pure):(P,P). A baseline pure Nash equilibrium of the repeated
game is the stationary play of(P,P)after every history. A nontrivial cooperative pure Nash equilibrium
described in Lal, 1990 is:
•Cooperative phase:(P,R)in the odd round, and(R,P)in the even round.
•If the opponent deviates from the cooperation, playZfor two periods and revert to the cooperative phase.
(4)Samaritan(altruism/one-sidedmoralhazard).Player1(Helper): Help(H)orNo-help(N). Player
2 (Recipient): Work (W) or Shirk (S). Per-period payoff matrix (Helper, Recipient):
Recipient:WRecipient:S
Helper:H (2,−1) (0,0)
Helper:N (1,−2) (−1,−3)
One-shot stage-game Nash equilibrium (pure):(H,S). The helper has a dominant action (help), and the
recipient best responds by shirking. A nontrivial cooperative Nash equilibrium exists for sufficiently patient
players:
•Cooperative phase: play(H,W)every period.
•If the recipient ever shirks, switch forever to punishment(N,W).
•If,duringpunishment,thehelpereverdeviatesbyhelping,therecipientswitchesforeverto(H,S)behavior.
(5) Lemons (adverse selection).Player 1 (Seller): High Quality (HQ) or Low Quality (LQ). Player 2
(Buyer): Buy (B) or Don’t buy (D). Per-period payoff matrix (Seller, Buyer):
Buyer:BBuyer:D
Seller:HQ (3,3) (−1,0)
Seller:LQ (4,−1) (0,0)
35

One-shot stage-game Nash equilibrium (pure):(LQ,D). Seller has strict dominant actionLQ; buyer
best-responds toLQwithD. A baseline pure Nash equilibrium of the repeated game is the stationary play
of(LQ,D)after every history. A nontrivial cooperative benchmark strategy profile used in the empirical
PS-BR implementation is:
•Cooperative phase: play(HQ,B)every period.
•If the seller choosesHQwhile the buyer choosesD, the seller switches toLQfor three rounds and then
returns toHQ.
•If the buyer choosesBwhile the seller choosesLQ, the buyer switches toDfor three rounds and then
returns toB.
•A player who caused the other’s retaliation window accepts that three-round retaliation and does not
counter-retaliate during it; after the window ends, play returns to(HQ,B).
Interaction protocol.In experiments 1-3, each run uses two fresh copies of the same model (Qwen 3.5
27B, Qwen Team (2026)) in symmetric self-play.
Within a run, actions are chosen simultaneously, all actions are perfectly publicly observed, and no com-
munication channel is available beyond the public action/payoff history. Across runs, model weights and
prompts are reset. Hence, any learning is purely in-context within the realized supergame. For each game,
model configuration, and horizon treatment, we run 20 independent supergames. This yields a distribution
of outcomes for each specification rather than a single realized history.
Infinitely repeated game implementation.Our main implementation follows the standard laboratory
approach to simulate infinitely repeated games:random terminationwith a guaranteed 200-round prefix. In
benchmark gameg, the first 200 rounds are guaranteed; at the end of round 200 and after each subsequent
round, the supergame continues with commonly known probabilityδg = 0.75and terminates otherwise.
We choose this continuation probability so that the analytical benchmark equilibria used in Section H are
sequentially rational in the indefinitely repeated game, while the empirical cooperative target profiles also
face strong continuation incentives. Such random termination is the standard benchmark implementation of
aninfinitelyrepeatedgame,andmatchedfinitecontrolsarethecleanestwaytoisolatecontinuationincentives
(Bó, 2005; G. R. Fréchette and Yuksel, 2017).
7.2 Experiment 1. Nash convergence
Here, we test the first hypothesis: that simple predict–then–act reasoning may already be sufficient for
convergence to some equilibrium-consistent late-run behavior.
7.2.1 Experiment design
In Section 5.3, we showed that if agents myopically learn to predict opponents’ next actions and then best
respond to those predictions, the realized path eventually converges to a stage-gameε-Nash equilibrium.
36

SCoT (Akata et al., 2025) operationalizes precisely such a predict–then–act rule.
Operationally, the three methods receive the same task information: game rules, compact public action
history, action set, allowed strategy labels and descriptions, role mapping, and the same strategy-prior line
when that treatment is enabled. They differ only in how this common information is used.Baseasks for
the next action directly from the enriched action prompt (Appendix G.1).SCoTfirst asks for the opponent’s
next action using the same strategy-context block and then asks for an action conditional on that prediction
(Appendix G.2).PS-BRuses the analogous strategy-label inference prompt to sample an opponent strategy
label and then selects an action by rollout-based strategy evaluation (Appendix G.3).
For comparability across specifications, we retain a late-run equilibrium-follow statistic as one reported
outcome. Because the random-termination treatment logs a guaranteed 200-round prefix, we evaluate late-
run play over rounds190–200. In each round of that window, we record whether the realized joint action
coincideswitheitheraone-shotNashactionoranon-pathactionofthebenchmarkcooperativerepeated-game
equilibrium for that game. We then average these indicators within run and across runs.
The matched finite-horizon control plays a separate role. If a method’s apparent success in the indefinite
treatment merely reflects convergence in long but finitely repeated interaction, then similar success should
appear in the matched finite game. If, instead, a gap emerges in favor of random termination, that gap is
evidence that continuation incentives matter for the method’s behavior.
Our primary comparison is therefore not only acrossBase,SCoT, andPS-BR, but also across the indefinite
and matched finite implementations for each game.
7.2.2 Results
Table1: Equilibrium-followpercentageintheterminalwindow(rounds190–200)forany(one-shotNashor
cooperative on-path action) Nash equilibrium. Reported scores are averaged over 20 trials.
Game Base SCoT PS-BR
BoS100.0%100.0%100.0%
PD100.0%100.0%100.0%
Promo100.0%100.0%100.0%
Samaritan100.0%100.0%100.0%
Lemons 0.0%100.0%100.0%
Table1showsthatonthebroad“anyNash”metric,terminal-windowperformanceunderrandomtermination
remainsnearceilinginmostenvironments. Itdeliberatelycreditstwodistinctkindsofequilibrium-consistent
play: one-shot Nash actions and on-path actions of the benchmark cooperative repeated-game equilibrium.
In PD, for example, both mutual defection and mutual cooperation count as equilibrium-consistent under
this metric; in BoS, coordinating on either diagonal counts as success. In these runs,PS-BRandSCoT
reach 100.0% in all five games, whileBasereaches 100.0% in BoS, PD, Promo, and Samaritan. This
37

pattern supports the paper’s first, weaker empirical prediction: myopic stage-game equilibrium consistency
is relatively easy for the model to reach, especially once the task is only to settle on some equilibrium-
consistent late-run action profile rather than to sustain a particular repeated-game path.
TheSCoTresultiscloselyalignedwiththetheoryinSection5.3: explicitmyopicpredict–then–actreasoning
issufficientforconvergencetoan“anyNash”outcome,includingamyopicstage-gameNashoutcome. More
surprisingly, thestrongBaseperformanceonthispermissive metricsuggeststhatthe underlyingmodelmay
already inherently encode at least the myopic strategic-equilibrium concept, even without the explicit SCoT
reasoning. ThisalignswiththefactthatrecentLLMmodelsareoftentrainedunderreasoningtasksandcan
implicitly reason, i.e., without explicit test-time reasoning steps (B. Wang et al., 2024), despite the fact that
implicit reasoning does not in general exhibit deep reasoning (Lin et al., 2025).
Note that Table 1 by itself does not identify whether that behavior can support richer continuation-level
reasoning beyond myopic strategic one-stage reasoning. Because the outcome metric is deliberately “any
Nash,” high scores may reflect only convergence to locally stable stage-game play rather than understanding
of the cooperative repeated-game equilibrium. That distinction is the object of Experiment 2.
7.3 Experiment 2. Nontrivial Nash convergence
Wenowmovefromaskingwhetherplayconvergestosomeequilibrium-consistentactionprofiletotheharder
question of whether agents can track aspecificnontrivial cooperative repeated-game equilibrium sustained
by continuation incentives.
7.3.1 Experiment design
The repeated-games literature shows that cooperation depends critically on strategic uncertainty and on
beliefs about the opponent’s strategy, not merely on the existence of a cooperative equilibrium (Dal Bó
and G. R. Fréchette, 2018; Dal Bó and G. Fréchette, 2025). Likewise, elicited beliefs over actions and over
supergamestrategieshelprationalizerepeated-gamechoices(Aoyagi,G.R.Fréchette,andYuksel,2024). We
therefore propose the prompt-induced cooperative-target treatment as abelief-conditioned implementation
test: the prompt reduces selection frictions and asks whether the model can represent and execute a specific
history-contingent cooperative target once favorable beliefs are supplied.
Thisdesignfollowstwolessonsfromtherepeated-gamesliterature. First,behaviorinrepeatedgamesdepends
strongly on experience and on strategic uncertainty; whether cooperation is supportable in equilibrium is
necessary but not sufficient to generate high cooperation (Dal Bó and G. R. Fréchette, 2011; Dal Bó and
G.R.Fréchette,2018;DalBóandG.Fréchette,2025). Second,beliefsoveropponents’actionsandstrategies
are central objects in repeated games, so experiments that manipulate or diagnose those beliefs can reveal
whether observed play reflects genuine repeated-game reasoning rather than incidental path matching (Dal
Bó and G. R. Fréchette, 2019; Aoyagi, G. R. Fréchette, and Yuksel, 2024).
Concretely, for each game, we provide a prompt that specifies one benchmark cooperative repeated-game
38

strategy profile and asks the agent to expect the opponent may follow that profile strongly; this informa-
tion enters through the strategy-context block in the Base and SCoT templates (Appendices G.1 and G.2)
and through the PS-BR strategy-label inference prompt (Appendix G.3). In PD, for example, the prompt
specifies sustained cooperation, followed by a contrite three-round retaliate-and-forgive response after ex-
ploitativedefection. InPromo,itspecifiesthealternating(P,R),(R,P),(P,R),...cooperativephasewith
the corresponding punishment rule. Analogous game-specific cooperative strategy profiles are used in BoS,
Samaritan, and Lemons, aligned with the benchmark constructions in Section 7.1; in Lemons, the bench-
mark is the analogous three-round retaliate-and-forgive reputation rule. Such a prompt reduces strategic
uncertainty, thereby making a specific cooperative target salient (Dal Bó and G. R. Fréchette, 2018; Dal Bó
and G. Fréchette, 2025). The score in this experiment checks whether the realized joint action matches the
prescribed cooperative action profile for that round on the benchmark path, then averages those indicators
withinrunandacrossruns. Underthisinterpretation,successinExperiment2shouldbereadasevidenceof
target-path implementation conditional on favorable beliefs.
7.3.2 Results.
Table 2: Equilibrium-follow percentage in the terminal window (rounds 190–200) for the prompt-specified
nontrivial cooperative target path. Reported scores are averaged over 20 trials.
Game Base SCoT PS-BR
BoS 0.0% 0.0%100.0%
PD 0.0% 0.0% 99.5%
Promo 0.0% 0.0%100.0%
Samaritan 0.0% 0.0% 99.5%
Lemons 0.0% 0.0%100.0%
Table 2 shows that once the metric is restricted to the prompt-specified cooperative action path, PS-BR runs
are near ceiling in all five benchmark games.PS-BRreaches 100.0% in BoS, Promo, and Lemons, and
99.5% in PD and Samaritan. By contrast,BaseandSCoTreach 0.0% in every game.
ThiscontrastwithTable1isthepaper’smainempiricaltest. Becausethecooperative-targetpromptreduces
equilibrium-selection frictions by making one favorable strategy profile salient, the remaining performance
gapisolateswhethertheagentcanactuallyrepresenttheopponent’sstrategyandactoncontinuationincentives
rather than merely match a locally safe action. Once the evaluation requires tracking a specific history-
contingent cooperative prescription rather than merely landing on some equilibrium-consistent action, the
near-ceilingperformancefromExperiment1disappearsforthesimplermethods. Undertherounds190–200
terminal-window criterion, onlyPS-BRachieves near-perfect scores across all five environments.
This finding supports the theory’s negative implication for myopic reasoning. Whether myopic reasoning is
madeexplicitthroughSCoTorappearsimplicitlyinBase,itcanbeenoughtoreachsomestage-gameNash-
consistent behavior, but it does not guarantee understanding of the long-term cooperation concept sustained
39

bycontinuationvalues. Thefailureofbothbaselinesonthecooperative-pathmetricthereforeclarifiesthatthe
high“anyNash”scoresinExperiment1shouldnotbeinterpretedasevidenceofcooperativerepeated-game
reasoning.
More broadly, Experiment 2 directly supports the paper’s core argument that off-the-shelf reasoning agents
can exhibit zero-shot repeated-game stability without post-training when they can infer opponent strategies
and evaluate continuation plans. Table 1 showed that most methods can reach some equilibrium-consistent
late-runbehavior,mostlythestage-Nashequilibrium. Table2showsthatmaintainingacooperativerepeated-
game prescription is much less robust, and that the ability to do so sharply favorsPS-BR. The fact that the
same advantage appears not only in BoS and PD but also in Promo, Samaritan, and Lemons ties the result
backtothepaper’smotivatingmarket-styleenvironments,suggestingthatthetheorymattersbeyondstylized
matrix games and into promotion, moral-hazard, and adverse-selection settings.
7.4 Experiment 3: Nontrivial Nash convergence under unknown payoffs
7.4.1 Setup
Experiment 3 keeps the benchmark games, cooperative target profiles, and horizon treatments from Ex-
periment 2, but removes common-knowledge stage payoffs. The question is now whether the same belief-
conditionedcooperative-targetbenchmarkcanbeimplementedwhenagentsmustsimultaneouslyinferpayoff
incentives from noisy private observations.
As in Experiment 2, we use the standard random-termination implementation as the main treatment and the
matched finite-horizon game as the control. Agents still observe the full public action history, but they do
notreceivethestage-gamepayoffmatrixintheprompt. Instead,afterpublicjointactiona t isrealized,player
ireceives only a private payoff observation
rt i =u g i (at) +ϵi,t, ϵ i,t i.i.d.∼ N(0,σ2 g),(12)
independent across players and rounds.
To mirror the finite payoff-menu setup used in Section 6, we equip each agent with a finite hypothesis class
over its ownmeanpayoff matrix. Fix a gamegand playeri, and define the offset set
K:={−2,−1.5,−1,−0.5,0,+0.5,+1,+1.5,+2}.
The finite menu of candidate mean matrices is
Mi,g :={m:A→R:m(a) =u g i (a) +kaσg for eacha∈A,withk a∈K}.
In particular, the true mean matrix belongs toMi,g.
40

Operationally, playerimaintains a posterior overMi,g using the Gaussian likelihood
πt i(m|h t,r 1:t−1 i )∝π 0 i (m)
t−1∏
s=1
ϕ(rs i ;m(as),σ 2 g),
whereϕ(·;µ,σ 2 g)istheGaussiandensity. PS-BRthensamplesonecandidatemeanmatrixfromthisposterior
and evaluates continuation strategies against the induced payoff kernel.
AsdiscussedinSection6,thisdesignisintendedtojustifyonlyon-path,decision-relevantpayofflearning,not
global recovery of the full payoff matrix. The prompt-specified cooperative target and its finite punishment
branches concentrate play on a small recurrent set of joint actions. Hence, under the Gaussian noise family,
any retained payoff hypothesis that remains strategically relevant but mis-specifies one of those recurrently
reached profiles accumulates repeated likelihood loss under the realized private rewards and is eliminated,
while hypotheses that differ only on unreached or decision-irrelevant profiles need not be separated. This is
exactly the recurrent-separation verification route discussed in Section 6 and Appendix C.1.
The prompt-induced cooperative-target benchmark is kept in action-strategy form but now omits the payoff
matrix (see Appendix G.4; for the Base and SCoT baselines, we use the templates in Appendices G.1 and
G.2 with the payoff matrix omitted from the rules text). Thus, the prompt still lowers strategic uncertainty
about the opponent’s intended continuation play, while leaving the agent to learn the payoff incentives that
make those continuations attractive or unattractive. This design directly targets the practical case in which
repeated-game agents must infer incentives from experience rather than from a fully specified stage game.
As in Experiment 2, we evaluate both on-path follow-through and off-path equilibrium understanding, and
we compare performance under random termination with the matched finite-horizon control.
7.4.2 Results.
We report two complementary terminal-window metrics under unknown stochastic payoffs: convergence to
any Nash equilibrium action (Table 3) and follow-through on the prompt-specified cooperative target path
(Table 4).
41

Table 3: Unknown stochastic payoffs: equilibrium-
follow percentage in the terminal window (rounds
190–200) foranyNash equilibrium. Reported
scores are averaged over 20 trials.
Game Base SCoT PS-BR
BoS100.0%100.0%100.0%
PD100.0%100.0%100.0%
Promo100.0% 70.9%100.0%
Samaritan 69.1% 60.0%90.5%
Lemons 94.5%100.0%100.0%
Table 4: Unknown stochastic payoffs: equilibrium-
follow percentage in the terminal window (rounds
190–200)fortheprompt-specifiedcooperativetarget
path. Reported scores are averaged over 20 trials.
Game Base SCoT PS-BR
BoS 0.0% 0.0%78.6%
PD 0.0% 15.0%72.7%
Promo 0.0% 3.6%75.9%
Samaritan 5.0% 4.5%79.1%
Lemons 10.0% 5.0%75.0%
On the broader “any Nash” metric (Table 3), all three methods again remain strong in the terminal window,
though performance is more uneven across games than in the known-payoff case.Basereaches 100.0%
in BoS, PD, and Promo, and remains high in Lemons at 94.5%, though it falls to 69.1% in Samaritan.
SCoTattains 100.0% in BoS, PD, and Lemons, but is weaker in Promo (70.9%) and Samaritan (60.0%).
PS-BRreaches 100.0% in BoS, PD, Lemons, and Promo, and 90.5% in Samaritan. Thus, as in the known-
payoff case, payoff uncertainty does not prevent substantial equilibrium-consistent terminal behavior on this
permissive metric, but it makes the non-planner baselines less uniformly reliable in Promo, Samaritan, and
Lemons.
The stricter cooperative-path metric in Table 4 again reveals a sharper distinction. Under unknown payoffs,
the PS-BR runs perform best in all five games: BoS (78.6%), PD (72.7%), Promo (75.9%), Samaritan
(79.1%),andLemons(75.0%).Baseismuchweaker,with0.0%inBoS,PD,andPromo,5.0%inSamaritan,
and 10.0% in Lemons;SCoTremains lower across all games, with 0.0% in BoS, 15.0% in PD, 3.6% in
Promo, 4.5% in Samaritan, and 5.0% in Lemons.
Experiment3alsoalignswiththetheoreticalresultsproposedinSection6,suggestingthatagentscanextend
the strategic-equilibrium reasoning observed in the idealized known-payoff setting to the more realistic
unknown-payoff setting. The extension is neither as stable nor as fast as in Experiment 2, because agents
must learn decision-relevant payoff incentives while also coordinating on the repeated-game path. This is
consistent with the theory’s payoff-learning extension: equilibrium reasoning can survive the removal of ex
ante payoff knowledge, but speed of convergence may be much slower.
8 Conclusion
In this paper, we theoretically highlight the promising prospect that general-purpose AI agents can attain
game-theoretic robustness through their inherent reasoning capabilities rather than through unrealistic,
bespoke, unified training. By demonstrating that LLMs can evolve toward equilibrium behavior on the
fly, we take a step toward safer and more autonomous multi-agent AI systems that remain effective across
42

the myriad interactive scenarios they will encounter in the real world. The results bridge the gap between
AI agents and classical game theory, indicating that the rich knowledge and inferential power of modern
LLMsmaybeharnessedtomeetlongstandingchallengesinmulti-agentlearningandinteraction. Ultimately,
enablingLLM-basedagentstonaturallyexhibitequilibrium-likebehaviorduringplaynotonlyadvancesour
theoretical understanding of their behavior but also paves the way for their deployment in societally crucial
domains that require reliable strategic decision-making.
43

References
Gaarlandt, Jur et al. (2025). “AI agents are changing how people shop. Here’s what that means for brands.”
In:Harvard Business Review26, p. 2.
Shahidi, Peyman et al. (2025).The Coasean Singularity? Demand, Supply, and Market Design with AI
Agents. Tech. rep. National Bureau of Economic Research.
Rothschild, David M et al. (2025). “The agentic economy”. In:arXiv preprint arXiv:2505.15799.
Bianchi, Federico et al. (2024). “How well can llms negotiate? negotiation arena platform and analysis”. In:
arXiv preprint arXiv:2402.05863.
Guo,Taichengetal.(2024).“Largelanguagemodelbasedmulti-agents:Asurveyofprogressandchallenges”.
In:arXiv preprint arXiv:2402.01680.
Lopez-Lira, Alejandro (2025). “Can large language models trade? testing financial theories with llm agents
in market simulations”. In:arXiv preprint arXiv:2504.10789.
Li, Yang et al. (2024). “Aligning individual and collective objectives in multi-agent cooperation”. In:
Advances in Neural Information Processing Systems37, pp. 44735–44760.
Zhu, Shenzhe et al. (2025). “The automated but risky game: Modeling and benchmarking agent-to-agent
negotiations and transactions in consumer markets”. In:arXiv preprint arXiv:2506.00073.
Bansal, Gagan et al. (2025). “Magentic Marketplace: An Open-Source Environment for Studying Agentic
Markets”. In:arXiv preprint arXiv:2510.25779.
Carichon, Florian et al. (2025). “The coming crisis of multi-agent misalignment: Ai alignment must be a
dynamic and social process”. In:arXiv preprint arXiv:2506.01080.
Abreu, Dilip and Ariel Rubinstein (1988). “The structure of Nash equilibrium in repeated games with finite
automata”. In:Econometrica: Journal of the Econometric Society, pp. 1259–1281.
DalBó,PedroandGuillaumeRFréchette(2011).“Theevolutionofcooperationininfinitelyrepeatedgames:
Experimental evidence”. In:American Economic Review101.1, pp. 411–429.
– (2018). “On the determinants of cooperation in infinitely repeated games: A survey”. In:Journal of
Economic Literature56.1, pp. 60–114.
Proto, Eugenio, Aldo Rustichini, and Andis Sofianos (2019). “Intelligence, personality, and gains from
cooperation in repeated interactions”. In:Journal of Political Economy127.3, pp. 1351–1390.
Aguirregabiria, Victor, Allan Collard-Wexler, and Stephen P Ryan (2021). “Dynamic games in empirical
industrial organization”. In:Handbook of industrial organization. Vol. 4. 1. Elsevier, pp. 225–343.
Calvano, Emilio et al. (2020). “Artificial intelligence, algorithmic pricing, and collusion”. In:American
Economic Review110.10, pp. 3267–3297.
Fish, Sara, Yannai A Gonczarowski, and Ran I Shorrer (2024). “Algorithmic collusion by large language
models”. In:arXiv preprint arXiv:2404.008067.2, p. 5.
Assad,Stephanieetal.(2024).“Algorithmicpricingandcompetition:EmpiricalevidencefromtheGerman
retail gasoline market”. In:Journal of Political Economy132.3, pp. 723–771.
44

Guo, Xudong et al. (2024).Embodied LLM Agents Learn to Cooperate in Organized Teams. arXiv:2403.
12482 [cs.AI].url:https://arxiv.org/abs/2403.12482.
Huang,Jen-tseetal.(2024).“HowFarAreWeontheDecision-MakingofLLMs?EvaluatingLLMs’Gaming
Ability in Multi-Agent Environments”. In:arXiv preprint arXiv:2403.11807.
Hua,Wenyueetal.(2024).“Game-theoreticLLM:Agentworkflowfornegotiationgames”.In:arXivpreprint
arXiv:2411.05990.
Buscemi, Alessio et al. (2025). “Fairgame: a framework for ai agents bias recognition using game theory”.
In:arXiv preprint arXiv:2504.14325.
Akata,Elifetal.(2025).“Playingrepeatedgameswithlargelanguagemodels”.In:NatureHumanBehaviour
9.7, pp. 1380–1390.
Duque, Juan Agustin et al. (2025). “Advantage Alignment Algorithms”. In:The Thirteenth International
Conference on Learning Representations.url:https://openreview.net/forum?id=QFO1asgas2.
Kalai, Ehud and Ehud Lehrer (1993a). “Rational learning leads to Nash equilibrium”. In:Econometrica:
Journal of the Econometric Society, pp. 1019–1045.
Norman, Thomas WL (2022). “The possibility of Bayesian learning in repeated games”. In:Games and
Economic Behavior136, pp. 142–152.
Yamin, Khurram et al. (2026). “Do LLMs Act Like Rational Agents? Measuring Belief Coherence in
Probabilistic Decision Making”. In:arXiv preprint arXiv:2602.06286.
Ge, Luise, Yongyan Zhang, and Yevgeniy Vorobeychik (2026). “Mind the (DH) Gap! A Contrast in Risky
Choices Between Reasoning and Conversational LLMs”. In:arXiv preprint arXiv:2602.15173.
Arumugam, Dilip and Thomas L Griffiths (2025). “Toward efficient exploration by large language model
agents”. In:arXiv preprint arXiv:2504.20997.
Coda-Forno, Julian et al. (2023). “Meta-in-context learning in large language models”. In:Advances in
Neural Information Processing Systems36, pp. 65189–65201.
Lu, Sheng et al. (2024). “Are emergent abilities in large language models just in-context learning?” In:
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1:
Long Papers), pp. 5098–5139.
Cahyawijaya, Samuel, Holy Lovenia, and Pascale Fung (2024). “Llms are few-shot in-context low-resource
language learners”. In:arXiv preprint arXiv:2403.16512.
Xie, Sang Michael et al. (2021). “An explanation of in-context learning as implicit bayesian inference”. In:
arXiv preprint arXiv:2111.02080.
Wang, Xinyi et al. (2023). “Large language models are latent variable models: Explaining and finding
gooddemonstrationsforin-contextlearning”.In:AdvancesinNeuralInformationProcessingSystems36,
pp. 15614–15638.
Wakayama,TomoyaandTaijiSuzuki(2025).“In-contextlearningisprovablyBayesianinference:ageneral-
ization theory for meta-learning”. In:arXiv preprint arXiv:2510.10981.
45

Falck, Fabian, Ziyu Wang, and Chris Holmes (2024). “Is in-context learning in large language models
bayesian? a martingale perspective”. In:arXiv preprint arXiv:2406.00793.
Qwen Team (Feb. 2026).Qwen3.5: Towards Native Multimodal Agents.url:https://qwen.ai/blog?
id=qwen3.5.
Nachbar, John H (1997). “Prediction, optimization, and learning in repeated games”. In:Econometrica:
Journal of the Econometric Society, pp. 275–309.
– (2005). “Beliefs in repeated games”. In:Econometrica73.2, pp. 459–480.
Sun, Haoran et al. (2025). “Game theory meets large language models: A systematic survey with taxonomy
and new frontiers”. In:arXiv preprint arXiv:2502.09053.
Jia, Jingru et al. (2025). “LLM Strategic Reasoning: Agentic Study through Behavioral Game Theory”. In:
arXiv preprint arXiv:2502.20432.
Guo, Fulin (2023).GPT in Game Theory Experiments.doi:10.48550/arXiv.2305.05516. arXiv:
2305.05516 [econ.GN].
Fan, Caoyun et al. (2023).Can Large Language Models Serve as Rational Players in Game Theory? A
Systematic Analysis. AAAI 2024.doi:10.48550/arXiv.2312.05488. arXiv:2312.05488 [cs.AI].
Kader,GavinandDongwooLee(2024).“TheEmergenceofStrategicReasoningofLargeLanguageModels”.
In:arXiv preprint arXiv:2412.13013.
Mao,Shaoguangetal.(2023).ALYMPICS:LLMAgentsMeetGameTheory–ExploringStrategicDecision-
Making with AI Agents.doi:10.48550/arXiv.2311.03220. arXiv:2311.03220 [cs.CL].
Duan, Jinhao et al. (2024).GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-
Theoretic Evaluations.doi:10.48550/arXiv.2402.12348. arXiv:2402.12348 [cs.CL].
Fontana, Nicoló, Francesco Pierri, and Luca Maria Aiello (2024). “Nicer Than Humans: How do Large
Language Models Behave in the Prisoner’s Dilemma?” In:arXiv preprint arXiv:2406.13605.
Willis, Richard et al. (2025). “Will Systems of LLM Agents Cooperate: An Investigation into a Social
Dilemma”. In:arXiv preprint arXiv:2501.16173.
Agrawal,Kushaletal.(2025).EvaluatingLLMAgentCollusioninDoubleAuctions.doi:10.48550/arXiv.
2507.01413. arXiv:2507.01413 [cs.GT].
Zhang, Yufeng et al. (2023). “What and how does in-context learning learn? bayesian model averaging,
parameterization, and generalization”. In:arXiv preprint arXiv:2305.19420.
Zhang,KellyWetal.(2024).“Posteriorsamplingviaautoregressivegeneration”.In:NeurIPS2024Workshop
on Bayesian Decision-making and Uncertainty.
Welleck,Seanetal.(2024).“Fromdecodingtometa-generation:Inference-timealgorithmsforlargelanguage
models”. In:arXiv preprint arXiv:2406.16838.
Durrett, Rick (2019).Probability: Theory and Examples.5th ed. See Theorem 2.1.21(Kolmogorov’s exten-
sion theorem). Cambridge University Press.doi:10.1017/9781108591034.
Kalai, Ehud and Ehud Lehrer (1993b). “Subjective equilibrium in repeated games”. In:Econometrica61.5,
pp. 1231–1240.
46

Blackwell, David and Lester Dubins (1962). “Merging of opinions with increasing information”. In:The
Annals of Mathematical Statistics33.3, pp. 882–886.
Cai, Tiffany Tianhui et al. (2024). “Active Exploration via Autoregressive Generation of Missing Data”. In:
arXiv preprint arXiv:2405.19466.
Zhou, Pei et al. (2023). “How far are large language models from agents with theory-of-mind?” In:arXiv
preprint arXiv:2310.03051.
Riemer,Matthewetal.(2024).“Position:Theoryofmindbenchmarksarebrokenforlargelanguagemodels”.
In:arXiv preprint arXiv:2412.19726.
Ionescu Tulcea, Cassius T (1949). “Mesures dans les espaces produits”. In:Atti Accad. Naz. Lincei Rend7,
pp. 208–211.
Pollard, David (2002).A user’s guide to measure theoretic probability. 8. Cambridge University Press.
Lal, Rajiv (1990). “Price promotions: Limiting competitive encroachment”. In:Marketing science9.3,
pp. 247–262.
Bó, Pedro Dal (2005). “Cooperation under the shadow of the future: experimental evidence from infinitely
repeated games”. In:American economic review95.5, pp. 1591–1604.
Fréchette,GuillaumeRandSevgiYuksel(2017).“Infinitelyrepeatedgamesinthelaboratory:Fourperspec-
tives on discounting and random termination”. In:Experimental Economics20.2, pp. 279–308.
Wang, Boshi et al. (2024). “Grokking of implicit reasoning in transformers: A mechanistic journey to the
edge of generalization”. In:Advances in Neural Information Processing Systems37, pp. 95238–95265.
Lin, Tianhe et al. (2025). “Implicit reasoning in transformers is reasoning through shortcuts”. In:Findings
of the Association for Computational Linguistics: ACL 2025, pp. 9470–9487.
Dal Bó, Pedro and Guillaume Fréchette (2025).Coordination and Cooperation. Tech. rep. National Bureau
of Economic Research.
Aoyagi, Masaki, Guillaume R Fréchette, and Sevgi Yuksel (2024). “Beliefs in repeated games: An experi-
ment”. In:American Economic Review114.12, pp. 3944–3975.
Dal Bó, Pedro and Guillaume R Fréchette (2019). “Strategy choice in the infinitely repeated prisoner’s
dilemma”. In:American Economic Review109.11, pp. 3929–3952.
Kuhn,HaroldW(1953).“Extensivegamesandtheproblemofinformation”.In:ContributionstotheTheory
of Games2.28, pp. 193–216.
Aumann, Robert J (1961).Mixed and behavior strategies in infinite extensive games. Princeton University
Princeton.
Abreu, Dilip (1988). “On the theory of infinitely repeated games with discounting”. In:Econometrica:
Journal of the Econometric Society, pp. 383–396.
47

Notation Summary
Symbol Meaning
Repeated-game primitives
I={1,...,N}Finite set of players / AI agents.
Ai, A=
∏
i∈IAi Player-iaction set;Ais the joint action space.
at = (at 1,...,a t N)∈AJoint action profile at roundt.
ui :A→[0,1]Stage payoff in the common-knowledge benchmark; in the private-payoff extension, the
true mean payoff matrix generating playeri’s private stochastic rewards.
λi∈(0,1)Player-idiscount factor.
φi,Φ ⋆ i Stage-game minmax payoff and pure-action maxmin payoff used in the Non-MM⋆
condition.
Histories, strategies, and induced laws
ht = (a1,...,a t−1)Public history observed before roundt.
H 0, Ht, H, H∞ Emptyhistory; historiesoflengtht−1; allfinitepublichistories; allinfiniteplaypaths.
C(h)Cylinder set of infinite paths having prefixh.
fi :H→∆(A i)Public-history strategy of playeriin the benchmark repeated game.
Fi,F=
∏
i∈IFi Individual and joint strategy spaces in the benchmark model.
µf Play-path distribution induced by strategy profilef.
µg ht Continuation distribution after historyht when continuation profilegis played
thereafter.
Ui(f)Objective discounted payoff of playeriunder profilef.
Beliefs and subjective continuation values
µ0 i, µ t i(·|h t)Player-iprior and posterior over opponents’ strategy profiles.
Pµi,gi i Predictive play-path distribution induced by own strategygi and beliefµi over
opponents’ strategies.
fi −i, f i,t −i Representative continuation models for playeri’s prior predictive and posterior
predictive beliefs about opponents’ play.
Vi(σi|h t;g−i)
Vi(σi|h t) Subjective continuation value of continuation strategyσi against continuation model g−i; shorthandVi(σi|h t) =V i(σi|h t;f i,t −i).
BRε i (g−i|h t)Set ofε-best-response continuation strategies at historyh t.
g−i∼ht i g′ −i,E i(ht)On-path continuation-payoff equivalence; the true equivalence class inside the finite
menu.
µf≪P 0,fi i Grain-of-truth condition: playeri’s prior predictive does not rule out events that occur
under the true play distribution.
d(µ,ν), d ht(µ,ν)Weak distance between play-path distributions and its continuation version after history
ht.
ξ, η, εApproximation tolerances for subjective best response, predictive accuracy, and Nash /
best-response error.
Posterior-sampling and one-step reasoning
48

Symbol Meaning
S−i, L i,T (g−i;z)Finite strategy menu of candidate opponent strategies in PS-BR; finite-history
likelihood of hypothesisg−i along realized pathz.
pt(g−i) =µ t i(g−i|h t)Posterior mass on opponent hypothesisg −i.
σPS i,t (·|h t)Continuation strategy chosen by posterior-sampling best response (PS-BR) at history
ht.
Dt i(ht) = 1− ∑ g−i∈S−i pt(g−i)2 Posterior collision complement; upper-bounds the generic PS-BR best-response gap
under exact posterior concentration.
DKL(p∥q)Kullback–Leibler divergence between two distributions.
qt i(·|h t),br ε i (q)One-step posterior predictive belief over opponents’ next joint action; stage-game
ε-best-response set to next-action distributionq.
g−i≈ht i g′ −i,E st i (ht), β t i(ht)On-path stage-payoff equivalence; the true stage-equivalence class inside the finite
menu; posterior mass outside that class.
αmPS i,t (·|h t)Mixed action induced by myopic PS-BR at historyh t.
ˆat −i(ht), b i(·)SCoT MAP prediction of opponents’ next action; deterministic pure best-response
selector.
Private-payoff extension
rt i Privately observed stochastic payoff of playeriat roundt.
Ri, ν i(dr), ψ i(r;µ)Payoff space, dominating base measure, and known noise-family density indexed by
meanµ.
xt i = (ht,r 1:t−1 i ), X t i, Xi Player-iobservable history used for payoff learning at timet, its time-tstate space, and
the full observable-history space.
Ω, P β,u Full sample space of public actions and private rewards; actual law induced by the
observable-history behavioral ruleβand the true mean payoffsu.
βi :X i→∆(A i)Actual one-step behavioral rule in the private-payoff environment.
Uui i (g|h t)Objective continuation payoff after public historyh t under the true mean matrixui.
Mi, π t i(mi|x t i)Finite menu of candidate mean payoff matrices and player-iposterior over that menu.
qmi i (dr|a)Payoff kernel induced by candidate mean matrixm i at joint actiona.
Vmi i (τi|h t;g−i)
BRε i,mi(g−i|h t) Subjective continuation value and correspondingε-best-response set when playeri evaluates payoffs using candidate mean matrixmi.
V mix,t i (τi|x t i)
Vui,t i (τi|x t i) Mixture continuation value under the joint opponent/payoff posteriors; the same object evaluated under the true mean matrixui.
gi,t −i,Π t i(·|x t i)Representative continuation model for playeri’s posterior predictive public-action
belief; posterior predictive law over future public-action paths.
E priv i (ht),U i(ht), αt i(ht), δt i(xt i)True opponents-side continuation-payoff equivalence class in the private-payoff game;
true own-payoff continuation-decision class; opponents-side learning error; pointwise
own-payoff continuation-decision learning error at observable historyxt i.
Bounded-memory appendix notation
suffixκ(h),F κ i ,S κ, Tκ Lastκjoint actions of historyh; bounded-memory strategy space; finite suffix-state
space; deterministic state-update map in the finite-state reduction.
49

A Predictive beliefs and representative continuation models
Themaintextworksdirectlywithposteriorpredictivecontinuationlaws. Thisappendixrecordsthestandard
representative construction that justifies the notationfi −i andf i,t −i used there.
Fix playeriand a (possibly mixed) beliefµi over opponents’ strategy profilesF−i. For any own strategy
gi∈F i, define the predictive play-path distribution
Pµi,gi i (E) :=
∫
F−i
µ(gi,f−i)(E)dµi(f−i)for measurableE⊆H ∞.
Lemma A.1(Existence of predictive representatives).Fix playeriand a beliefµi over opponents’ strategy
profilesF−i. There exists a behavior-strategy profile¯f−i∈F−i such that, for every own strategygi∈F i,
µ(gi, ¯f−i) =P µi,gi i .
Whenµi has finite support{g1 −i,...,g K −i}, one convenient choice is
¯f−i(h)(a−i) =
K∑
k=1
µi(gk −i|h)g k −i(h)(a−i),
for historieshwhere Bayes’ rule is defined.
Lemma A.1 is the standard mixed-to-behavior reduction for extensive-form games with perfect recall; see
Kuhn(1953),Aumann(1961),andKalaiandLehrer(1993a). Weuseitonlyasnotation-savinginfrastructure.
Applying Lemma A.1 to the priorµ0 i yields a representative continuation modelfi −i∈F−i such that, for
everygi,
µ(gi,fi −i) =P 0,gi i .
At any historyht where Bayes’ rule is defined, applying the same lemma to the posteriorµt i(·|h t)yields
a representative continuation modelfi,t −i. For notational convenience, we may choose these representatives
continuation-consistently:
fi,t −i ⏐⏐ ht :=f i −i ⏐⏐ ht.(13)
This is the selection convention used in the appendix proofs.
B Continuity and Finite-Horizon Robustness
Lemma B.1(Continuity of discounted payoff).For each agentiand everyδ >0, there existsρi(δ)>0
such that for any strategy profilesf,g∈F,
d(µf,µg)≤ρ i(δ)⇒ ⏐⏐Ui(f)−U i(g) ⏐⏐≤δ.
50

In particular, ifρ(δ) = mini∈Iρi(δ)andd(µ f,µg)≤ρ(δ), then ⏐⏐Ui(f)−U i(g) ⏐⏐≤δfor alli∈I.
B.1 Finite-horizon variants and robustness
For a finite horizonT∈N, we denote byFT the set of behaviour strategies specified on histories of length
at mostT; two full strategies that coincide on these histories induce the same distribution over histories up
to timeTand the same truncated payoff. Forf∈FT, define theT-period discounted payoff
UT i (f) =E z∼µf
[
(1−λ i)
T∑
t=1
λt−1 i ui(zt) ] .
Definition 18(Finite-horizon weakξ-subjectiveη-equilibrium).Letξ,η≥0and a fixed horizonT. A
truncated strategy profilef∈F T is afinite-horizon weakξ-subjectiveη-equilibriumif for each agenti∈I
there exists a supporting truncated profilefi∈F T such that:
•f i i =f i;
•U T i (fi,f i −i)≥sup gi∈FT i UT i (gi,f i −i)−ξ;
•d(µ fi ,µf)≤ηwhendis computed using only cylinder events inBt witht≤T.
Wenowshowthatfinite-horizonweaksubjectiveequilibriacanbe“patched”intoapproximatefinite-horizon
Nash equilibria without changing the induced distribution of play up to timeT.
Lemma B.2(Finite-horizon purification forη= 0Norman, 2022).Fix a finite horizonTand a profile
f∈F T. Supposefisafinite-horizonweakψ-subjective0-equilibriumforsomeψ≥0. Thenthereexistsa
truncated strategy profileˆf∈F T such that:
• ˆfis aψ-Nash equilibrium of theT-period game, i.e., for alli∈Iand allgi∈F T i ,
UT i ( ˆfi, ˆf−i)≥U T i (gi, ˆf−i)−ψ;
•the induced distributions of histories of length at mostTcoincide: for everyE∈BT,µ ˆf(E) =µ f(E).
We next extend this to the case whereη >0but small, using a compactness and limit argument.
Lemma B.3(Finite-horizon robustness).Fix a finite horizonTandψ >0. For everyθ >0there exists
¯ηT (ψ,θ)>0such that: iff∈F T is a finite-horizon weakψ-subjectiveη-equilibrium withη≤¯ηT (ψ,θ),
then there exists aψ-Nash equilibriumˆf∈F T satisfying
d(µ
ˆf,µf)≤θ
(again withdcomputed on cylinder events of length at mostT).
51

Wenowpatchfinite-horizonrobustnesstotheinfinite-horizongamebytruncatingthepayoffatasufficiently
large horizon and using Lemma B.1; the resulting infinite-horizon patching lemma is recorded below.
Lemma B.4(Infinite-horizon patching).Fixξ >0andε>0. There existsˆη(ξ,ε)>0such that iff∈F
isaweakξ-subjectiveη-equilibriuminthesenseofDefinition9withη≤ˆη(ξ,ε),thenthereexistsastrategy
profile ˆf∈Fsatisfying:
• ˆfis a(ξ+ε)-Nash equilibrium of the infinite-horizon game;
•d(µ ˆf,µf)≤ε.
Remark5(Continuation-gameanaloguefortheprivate-payoffextension).Becausetheprivate-payoffsection
nowworksdirectlywithpublic-historycontinuationgamesafterh t,LemmasB.2–B.4alreadyapplydirectly.
No separate hidden-history continuation-game variant is needed.
52

C Proofs
Proof of Lemma B.1.Fixiandδ >0. Choose a finite horizonT∈Nlarge enough that
(1−λ i)
∞∑
t=T+1
λt−1 i ≤ δ 4.(14)
For any profileg∈F, define the truncated payoff
UT i (g) =E z∼µg
[
(1−λ i)
T∑
t=1
λt−1 i ui(zt)
]
.
Then for anygwe have
⏐⏐Ui(g)−U T i (g) ⏐⏐≤(1−λ i) ∞∑
t=T+1
λt−1 i ≤ δ 4
by (14), using thatui(·)∈[0,1].
Now fixf,g∈F. We can decompose
⏐⏐Ui(f)−U i(g) ⏐⏐≤ ⏐⏐Ui(f)−U T i (f) ⏐⏐ + ⏐⏐UT i (f)−U T i (g) ⏐⏐ + ⏐⏐UT i (g)−U i(g) ⏐⏐.
By the bound above, the first and third terms are each at mostδ/4. It remains to control|UT i (f)−U T i (g)|.
For eacht∈{1,...,T}and each joint action profilea∈A, let
αf t (a) =µ f( {z∈H ∞ :z t =a} ) , α g t (a) =µ g( {z∈H ∞ :z t =a} ) .
Sinceui(a)∈[0,1]for alla, we have
⏐⏐⏐⏐⏐ ∑ a∈A ui(a) ( αf t (a)−α g t (a) ) ⏐⏐⏐⏐⏐≤sup E∈Bt ⏐⏐µf(E)−µ g(E) ⏐⏐.
Hence
⏐⏐UT i (f)−U T i (g) ⏐⏐ =
⏐⏐⏐⏐⏐ T∑ t=1 (1−λ i)λt−1 i ∑ a∈A ui(a) ( αf t (a)−α g t (a) ) ⏐⏐⏐⏐⏐
≤
T∑
t=1
(1−λ i)λt−1 i sup
E∈Bt
⏐⏐µf(E)−µ g(E) ⏐⏐.
By the definition (7) ofd(µf,µg), for eachtwe have
2−t sup
E∈Bt
⏐⏐µf(E)−µ g(E) ⏐⏐≤d(µ f,µg),
53

hence
sup
E∈Bt
⏐⏐µf(E)−µ g(E) ⏐⏐≤2 td(µf,µg).
Thus
⏐⏐UT i (f)−U T i (g) ⏐⏐≤d(µ f,µg) T∑
t=1
(1−λ i)λt−1 i 2t.
The finite sum on the right depends only onTandλi; call itCi(T). Define
ρi(δ) = min
{ δ
4Ci(T),1
}
.
Ifd(µf,µg)≤ρ i(δ), then
⏐⏐UT i (f)−U T i (g) ⏐⏐≤C i(T)ρi(δ)≤ δ 4.
Combining the three bounds gives
⏐⏐Ui(f)−U i(g) ⏐⏐≤ δ 4 + δ 4 + δ 4 < δ.
Settingρ(δ) = min i∈Iρi(δ)yields the final claim.
Proof of Lemma B.2.For each playeri, letfi = (fi,f i −i)be a supporting truncated profile from Defini-
tion 18. Becauseη= 0,
µfi (E) =µ f(E)for everyE∈B T.
Thusf i andfinduce the same distribution over histories of length at mostT.
For each playeri, letDi denote the set of historiesht,t≤T, such that alongh t the earliest departure from
the profilefis a unilateral deviation by playeri. Define a truncated profileˆfas follows:
•on histories that are still consistent withf, setˆf=f;
•on every descendant of a history inDi, set ˆf=f i;
•on any remaining off-path histories, choose arbitrary actions.
Because every history in⋃ iDi is off-path underf, these replacements do not change the play distribution
when all players followˆf. Henceµ ˆf(E) =µ f(E)for allE∈B T, proving item 2.
Now fix playeriand an arbitrary deviationgi∈F T i . Under the profile(gi, ˆf−i), play coincides withf
until the first deviation byi, and from that point onward the continuation of the other players is exactlyfi −i.
Therefore
UT i (gi, ˆf−i) =U T i (gi,f i −i).
54

Similarly, sinceµˆf =µ f =µ fi onB T andf i i =f i = ˆfi,
UT i ( ˆfi, ˆf−i) =U T i (fi,f i −i).
Using the defining inequality for the supporting profilefi,
UT i ( ˆfi, ˆf−i) =U T i (fi,f i −i)≥sup
g′ i∈FT i
UT i (g′ i,f i −i)−ψ= sup
g′ i∈FT i
UT i (g′ i, ˆf−i)−ψ.
Since this holds for every playeri,ˆfis aψ-Nash equilibrium of theT-period game, proving item 1.
Proof of Lemma B.3.Suppose, towards a contradiction, that there existT,ψ >0andθ >0such that for
everym∈Nthere is a finite-horizon weakψ-subjectiveη m-equilibriumf (m)∈F T withη m≤1/mand
such that noψ-Nash equilibrium lies within weak distanceθofµf (m) (measured onBT).
Foreachmandeachi∈I,letf i,(m)beasupportingtruncatedprofilewitnessingthatf (m)isafinite-horizon
weakψ-subjectiveη m-equilibrium, i.e.,fi,(m) i =f (m) i ,
UT i (f (m) i ,f i,(m) −i )≥sup
gi∈FT i
UT i (gi,f i,(m) −i )−ψ, d(µ fi,(m) ,µf (m) )≤η m.
BecausethehorizonTandactionsetsarefinite,thespaceofbehaviourstrategiesF T isafinite-dimensional
product of simplices and hence compact in the product topology. Thus, by sequential compactness, there
exists a subsequence (which we relabel for notational convenience) such that
f (m)→f ⋆ andf i,(m)→f i,⋆ for alli∈I,
asm→∞, in the product topology onFT.
The mapf↦→µ f on finite histories (up to timeT) is continuous with respect to this topology and the weak
topology induced byd(restricted toBT), so
µf (m) →µ f⋆ , µ fi,(m) →µ fi,⋆ .
Sinced(µfi,(m) ,µf (m) )≤η m→0, we must haved(µfi,⋆ ,µf⋆ ) = 0, soµfi,⋆ =µ f⋆ onB T.
Moreover, the best-response inequality passes to the limit. Fixiand anygi∈F T i . For allm,
UT i (f (m) i ,f i,(m) −i )≥sup
g′ i∈FT i
UT i (g′ i,f i,(m) −i )−ψ≥U T i (gi,f i,(m) −i )−ψ.
BycontinuityofU T i intheproducttopology(animmediateconsequenceofLemmaB.1restrictedtohorizon
55

T), takingm→∞yields
UT i (f⋆ i,f i,⋆ −i )≥U T i (gi,f i,⋆ −i )−ψ.
Sinceg i was arbitrary andfi,⋆ i =f ⋆ i (by pointwise convergence offi,(m) i tof i,⋆ i and off (m) i tof ⋆ i ), we
conclude that
UT i (f⋆ i,f i,⋆ −i )≥sup
gi∈FT i
UT i (gi,f i,⋆ −i )−ψ.
Together withd(µfi,⋆ ,µf⋆ ) = 0, this shows thatf⋆ is a finite-horizon weakψ-subjective0-equilibrium of
theT-period game.
By Lemma B.2, there exists a profileˆf⋆∈F T such that ˆf⋆ is aψ-Nash equilibrium of theT-period game
andµ ˆf⋆ coincides withµf⋆ on histories of length at mostT. In particular,d(µˆf⋆ ,µf⋆ ) = 0.
Sinceµ f (m) →µ f⋆ in the weak metricd(restricted toBT), we haved(µf (m) ,µ ˆf⋆ )→0asm→∞. Thus
forallsufficientlylargem,d(µ f (m) ,µ ˆf⋆ )≤θ. But ˆf⋆ isaψ-Nashequilibrium,contradictingtheassumption
that noψ-Nash equilibrium lies within weak distanceθofµ f (m) . This contradiction shows that such a
sequence(f (m))cannot exist, and hence there must exist¯ηT (ψ,θ)>0with the stated property.
Proof of Lemma B.4.Fixξ >0andε>0. ChooseafinitehorizonTlargeenoughthat,foralli∈Iandall
profilesh∈F, ⏐⏐Ui(h)−U T i (h) ⏐⏐ ≤ ε 8,(15)
and also ∑
t>T
2−t ≤ ε 4.(16)
Such aTexists because the tails of both geometric series are uniformly small.
Letfbe a weakξ-subjectiveη-equilibrium with supporting profiles{fi}i∈I as in Definition 9, i.e., for each
i,
fi i =f i, U i(fi,f i −i)≥sup
gi∈Fi
Ui(gi,f i −i)−ξ, d(µ fi ,µf)≤η.
Consider the truncated profilesf(T) and(f i)(T) obtained by restricting the prescriptions offandf i to
histories of length at mostT. For eachiwe have(fi i )(T) =f (T) i and, since the weak distance on histories
up toTis bounded by the full weak distance,
d(µ(fi)(T) ,µf (T) )≤d(µ fi ,µf)≤η.
Wenowshowthatf (T) isafinite-horizonweakψ T-subjectiveη-equilibriumforaslightlyrelaxedparameter
56

ψT. Fixiand note that for any profileh,
|Ui(h)−U T i (h)|≤ ε 8
by (15). Using the weak subjective inequality forfandfi, we obtain
UT i (f (T) i ,(f i −i)(T) ) =U T i (fi,f i −i)
≥U i(fi,f i −i)− ε 8
≥sup
gi∈Fi
Ui(gi,f i −i)−ξ− ε 8.
For any truncated deviationg(T) i ∈F T i we can extend it arbitrarily to a full strategygi∈F i, and then
Ui(gi,f i −i)≥U T i (g(T) i ,(f i −i)(T) )− ε 8,
again by (15). Taking the supremum overg(T) i yields
UT i (f (T) i ,(f i −i)(T) )≥sup
g(T) i ∈FT i
UT i (g(T) i ,(f i −i)(T) )−ξ− ε 4.
Thus, if we define
ψT :=ξ+ ε 4,
then for eachithe truncated profilesf(T) and(f i)(T) satisfy
UT i (f (T) i ,(f i −i)(T) )≥sup
g(T) i ∈FT i
UT i (g(T) i ,(f i −i)(T) )−ψ T,
andd(µ (fi)(T) ,µf (T) )≤η, sof (T) is a finite-horizon weakψT-subjectiveη-equilibrium in the sense of
Definition 18.
Applying Lemma B.3 with thisT,ψ=ψ T andθ=ε/2, there exists¯η T (ψT,ε/2)>0such that if
η≤¯ηT (ψT,ε/2)then there is aψT-Nash equilibrium ˜f (T)∈F T for theT-period game with
d(µ
˜f (T) ,µf (T) )≤ ε 2.
Define
ˆη(ξ,ε) := ¯ηT
(
ξ+ ε 4, ε 2 ) .
Assume henceforth thatη≤ˆη(ξ,ε)so that this conclusion holds.
Extend ˜f (T) arbitrarilytoafullstrategyprofile ˆf∈FbyspecifyingitsbehaviourafterperiodTinanyway.
57

Then ˆfand ˜f (T) coincideonperiodst≤T,andsimilarlyfandf (T) coincideont≤T. Theweakdistance
between ˆfandfcan be bounded as
d(µ
ˆf,µf)≤d(µ ˆf,µ ˜f (T) ) +d(µ ˜f (T) ,µf (T) ) +d(µf (T) ,µf).
The second term is at mostε/2by construction. For the first and third terms, any discrepancy betweenˆf
and ˜f (T) (respectively,fandf (T)) occurs only at timest>T, so each of these weak distances is bounded
by the tail∑ t>T 2−t≤ε/4by (16). Hence
d(µ
ˆf,µf)≤ ε 4 + ε 2 + ε 4 =ε.
It remains to show thatˆfis a(ξ+ε)-Nash equilibrium of the infinite-horizon game. Fixi∈Iand any
deviationg i∈F i. Letg (T) i denote the truncation ofgi to aT-period strategy, i.e., its prescriptions on
historiesoflengthatmostT; clearlyU T i (gi, ˆf−i) =U T i (g(T) i , ˜f (T) −i )since ˆfand ˜f (T) coincideonthefirstT
periods.
Because ˜f (T) is aψT-Nash equilibrium of theT-period game,
UT i ( ˜f (T) i , ˜f (T) −i )≥U T i (g(T) i , ˜f (T) −i )−ψ T.
Using the truncation bound (15), we obtain
Ui( ˆfi, ˆf−i)≥U T i ( ˆfi, ˆf−i)− ε 8 =U T i ( ˜f (T) i , ˜f (T) −i )− ε 8
and
Ui(gi, ˆf−i)≤U T i (gi, ˆf−i) +ε 8 =U T i (g(T) i , ˜f (T) −i ) +ε 8.
Combining these inequalities yields
Ui( ˆfi, ˆf−i)≥U T i ( ˜f (T) i , ˜f (T) −i )− ε 8
≥U T i (g(T) i , ˜f (T) −i )−ψ T− ε 8
≥U i(gi, ˆf−i)−ψ T− ε 4.
Recalling thatψT =ξ+ε/4, we have
ψT + ε 4 =ξ+ ε 2≤ξ+ε,
so for every deviationgi,
Ui( ˆfi, ˆf−i)≥U i(gi, ˆf−i)−(ξ+ε).
58

Thus ˆfis a(ξ+ε)-Nash equilibrium.
C.1 Auxiliary retained-menu identification assumption
The main text works with the concentration-up-to-equivalence condition in Assumption 3. For concrete
verification, it is convenient to record stronger sufficient routes. The logic is one-way: exact retained-menu
identification is stronger than what PS-BR needs, but it is easy to check in sparse deterministic menus. We
first state a deterministic hard-refutation condition, and then the more general likelihood-ratio formulation
that only requires on-path elimination of wrong retained hypotheses.
Assumption 7(Deterministic hard refutation on a strategy menu).Fix playeri. Assume the support ofµ0 i
is finite; writeS−i := supp(µ0 i )⊆F −i. Assume every element ofS−i is a deterministic public automaton.
Moreover,
1.(Menu grain of truth)f−i∈S−i andµ 0 i (f−i)>0.
2.(On-path finite separation)For everyg−i∈S−i\{f−i},
µf
({
z:∃t≥1s.t.g −i(ht(z))̸=f −i(ht(z)) }) = 1.
Assumption 8(Retained-menu identification).Fix playeri. Assume the support ofµ 0 i is finite; write
S−i := supp(µ0 i )⊆F −i. For anyg−i∈S−i and realized pathz∈H ∞, define the finite-history likelihood
Li,T (g−i;z) :=
T−1∏
t=1
g−i(ht(z))(at −i(z)), T≥1,
withtheconventionthatonceafactoriszero,alllaterlikelihoodsremainzero. Thenthefollowingconditions
hold:
1.(Menu grain of truth)f−i∈S−i andµ 0 i (f−i)>0.
2.(On-path elimination of wrong retained hypotheses)For everyg−i∈S−i\{f−i},
Li,T (g−i;z)
Li,T (f−i;z) −→0µ f-a.s. inz.
LemmaC.1(Deterministicon-pathseparationimpliesretained-menuidentification).SupposeAssumption7
holds. Then Assumption 8 holds.
Proof of Lemma C.1.Item 1 of Assumption 8 is exactly Assumption 7(1). It remains to verify Item 2.
59

Fixg−i∈S−i\{f−i}and define
τg(z) := inf{t≥1 :g −i(ht(z))̸=f −i(ht(z))}.
By Assumption 7(2),τg(z)<∞forµ f-almost everyz. Fix such a pathzand lett=τ g(z). Sincef−i is
deterministicandthetrueopponents’strategyunderµ f isf−i,therealizedopponentactiona t −i(z)isexactly
theuniqueactionassignedprobabilityonebyf −i(ht(z)). Becauseg−i(ht(z))̸=f −i(ht(z))andg −i isalso
deterministic, it assigns probability zero to that realized action:
g−i(ht(z))(at −i(z)) = 0.
Henceg−i is hard-refuted at timet, and by definition of the likelihood,
Li,T (g−i;z) = 0for allT >t.
On the other hand, along the true path generated by the deterministic strategyf−i,
f−i(hs(z))(as −i(z)) = 1for everys≥1,
so
Li,T (f−i;z) = 1for everyT≥1.
Therefore
Li,T (g−i;z)
Li,T (f−i;z) = 0for all sufficiently largeT.
This proves Assumption 8(2).
LemmaC.2(Posteriorconcentrationunderretained-menuidentification).FixplayeriandsupposeAssump-
tion 8 holds. Thenµf-a.s. inz,
µt i(f−i|h t(z))−→1,and hencemax g−i∈S−i\{f−i} µt i(g−i|h t(z))−→0.
Corollary C.3(Retained-menu identification implies the main-text concentration condition).Suppose As-
sumption 8 holds. Then Assumption 3 holds.
Proof.For every historyh t, the true labelf−i belongs to its own continuation-payoff equivalence class
Ei(ht). Therefore,
µt i(Ei(ht(z))|h t(z))≥µ t i(f−i|h t(z)).
60

By Lemma C.2, the right-hand side converges to1on aµf-full-measure set of realized paths. Hence
µt i(Ei(ht(z))|h t(z))−→1µ f-a.s. inz,
which is exactly Assumption 3(2).
Corollary C.4(Deterministic hard refutation implies the main-text concentration condition).Suppose As-
sumption 7 holds. Then Assumption 3 holds.
Proof.ByLemmaC.1,Assumption7impliesAssumption8. Theclaimthereforefollowsimmediatelyfrom
Corollary C.3.
Corollary C.5(Retained-menu identification implies the private-payoff opponents-side concentration con-
dition).Suppose playeri’s finite retained opponents’ menu and posterior satisfy Assumption 8. Then
Assumption 5 holds.
Proof.The exact same Bayes-ratio argument as in Lemma C.2 yields
µt i(f−i|h t(ω))−→1P β,u-a.s. inω.
For every public historyht(ω), the true opponents’ modelf−i belongs to its own continuation-payoff
equivalence classEpriv i (ht(ω)). Therefore,
µt i(Epriv i (ht(ω))|h t(ω))≥µ t i(f−i|h t(ω))−→1,
which is exactly Assumption 5(2).
Corollary C.6(Deterministic hard refutation implies the private-payoff opponents-side concentration con-
dition).Suppose playeri’s finite retained opponents’ menu satisfies Assumption 7. Then Assumption 5
holds.
Proof.ByLemmaC.1,Assumption7impliesAssumption8. Theclaimthereforefollowsimmediatelyfrom
Corollary C.5.
The more general retained-menu identification condition (Assumption 8) and Lemma C.2 remain useful as
a stronger appendix-level route: they show that exact posterior concentration can also be obtained when
wrongretainedlabelsareeliminatedasymptoticallybylikelihood-ratiodecayratherthanbyfinite-timehard
refutation. But for the sparse simulation menus used in our applications, Corollary C.4 is the practically
relevant route. Those menus are built to exclude duplicate labels that would remain observationally or
strategically equivalent to the benchmark equilibrium automaton on the realized path. As a result, a wrong
61

retaineddeterministiclabeliseventuallycontradictedbysomeobservedpublicaction, sodeterministichard
refutation directly verifies the main-text concentration condition.
The next appendix condition is the private-payoff analogue of the public-action verification route above. In
themaintext,Assumption6isstatedasmenu-levelconcentrationonplayeri’strueown-payoffcontinuation-
decision class rather than as literal global identification of the full retained mean matrix. No claim is made
about learning the opponents’ payoff matrices. The intended economic logic is again on-path: playerineed
not learn its own payoffs everywhere, only at the reached action profiles that matter for the continuation
decision problem. For concrete verification, it is convenient to record a stronger route based on likelihood-
ratio elimination of wrong retained mean matrices along the realized private payoff history.
Assumption9(Identificationofplayeri’sownpayoffmenu).FixplayeriandletM i = supp(π0 i )befinite.
Assume:
1.(Menu grain of truth)The true mean matrixui∈M i andπ 0 i (ui)>0.
2.(Known common Gaussian noise family)There existsσ2 i >0such that
rt i|a t∼N(u i(at),σ 2 i ),
and each menu elementmi∈M i induces the Gaussian payoff kernel
qmi i (dr|a) =ϕ(r;m i(a),σ 2 i ) dr.
Equivalently, for everymi∈M i, the finite-history payoff likelihood is
Ki,T (mi;ω) :=
T−1∏
t=1
ϕ
(
rt i(ω);mi(at(ω)),σ 2 i ) , T≥1,
whereϕ(·;µ,σ 2 i )denotes the Gaussian density with meanµand varianceσ2 i.
3.(On-path elimination of wrong retained payoff hypotheses)For everymi∈M i\{ui},
Ki,T (mi;ω)
Ki,T (ui;ω) −→0P β,u-a.s. inω.
LemmaC.7(Own-payoff-menuidentificationimpliespointwisepayoffposteriorconcentration).Fixplayer
iand suppose Assumption 9 holds. Then
πt i(Ui(ht(ω))|x t i(ω))−→1forP β,u-a.e.ω.
Thenextassumptionisaconcretesufficientrouteforthepayoff-menuidentificationconditionunderthesame
62

known common Gaussian setting used in Experiment 3. Its role is to formalize the idea that wrong retained
own-payoff hypotheses do not have to be contradicted everywhere: it is enough that each such hypothesis
disagreewiththetruthatsomejointactionthattherealizeddynamicsrevisitoftenenoughforprivatereward
evidence to accumulate.
Assumption 10(Gaussian recurrent mean-gap separation).Fix playeriand letM i = supp(π0 i )be finite.
Assume:
1.(Menu grain of truth)The true mean matrixui∈M i andπ 0 i (ui)>0.
2.(Known common Gaussian noise family)There existsσ2 i >0such that, for everym i∈M i and every
a∈A,
qmi i (dr|a) = 1√ 2πσi exp
(
−(r−m i(a))2
2σ2 i
)
dr.
3.(On-path recurrent mean separation)For everymi∈M i\{ui}, there exist a joint actiona⋆(mi)∈A
and a constantρi(mi)>0such that
mi(a⋆(mi))̸=u i(a⋆(mi))
and, under the true interaction lawPβ,u,
lim inf
T→∞
1
T
T∑
t=1
1{at =a ⋆(mi)}≥ρ i(mi)a.s.
Lemma C.8(Gaussian recurrent mean-gap separation implies payoff-menu identification).Suppose As-
sumption 10 holds. Then Assumption 9 holds.
Proof of Lemma C.8.Item1ofAssumption9isexactlyItem1ofAssumption10. Item2ofAssumption10
supplies the known common Gaussian noise family appearing in Item 2 of Assumption 9. It remains to
verify Item 3.
Fixmi∈M i\{ui}and define
∆t :=u i(at)−m i(at), ε t :=r t i−ui(at).
Under the true interaction lawPβ,u,ε t is conditionally mean-zero Gaussian with varianceσ2 i givenat. For
Gaussian likelihoods,
log ϕ(rt i;ui(at),σ 2 i ) ϕ(rt i;mi(at),σ 2 i ) = ∆2 t 2σ2 i + ∆tεt σ2 i .
63

Therefore, pathwise,
log Ki,T (ui;ω) Ki,T (mi;ω) = 1 2σ2 i T−1∑ t=1 ∆2 t + 1 σ2 i T−1∑ t=1 ∆tεt.
BecauseAandM i are finite, there existsCi(mi)<∞such that|∆ t|≤C i(mi)for allt. Let
Ht :=σ(h t+1,r 1:t−1 i ), Y t := ∆tεt.
Thenat, hence∆t, isHt-measurable, and
E[Yt|H t] = ∆t E[εt|H t] = 0.
Also,
sup
t
E[Y 2 t ]≤C i(mi)2σ2 i <∞.
Hence ∞∑
t=1
E[Y 2 t ]
t2 <∞,
so the martingale strong law implies
1
T
T∑
t=1
Yt−→0a.s.
By Assumption 10(3), there exista⋆(mi)∈Aandρ i(mi)>0such thatm i(a⋆(mi))̸=u i(a⋆(mi))and
lim inf
T→∞
1
T
T∑
t=1
1{at =a ⋆(mi)}≥ρ i(mi)a.s.
Therefore,
lim inf
T→∞
1
T
T∑
t=1
∆2 t≥ρ i(mi) ( ui(a⋆(mi))−m i(a⋆(mi)) )2>0a.s.
Combining the last three displays yields
lim inf
T→∞
1
T log Ki,T (ui;ω) Ki,T (mi;ω) >0P β,u-a.s.
Hence
Ki,T (mi;ω)
Ki,T (ui;ω) −→0P β,u-a.s. inω,
which is exactly Item 3 of Assumption 9.
64

Proof of Lemma 4.1.For eachg−i∈S−i define the continuation value envelope
M(g−i) := sup
σi
Vi(σi|h t;g−i)∈[0,1].
Foreachg −i picka(measurable)bestresponseσ g−i i ∈BR i(g−i|h t),sothatV i(σg−i i |h t;g−i) =M(g −i).
By definition, PS-BR first samples˜g−i ∼p t(·)and then playsσ ˜g−i i . Evaluating against the posterior
predictive belief and using linearity in the mixing over opponent hypotheses,
Vi(σPS i,t |h t) = ∑
˜g−i∈S−i
pt(˜g−i)
∑
g−i∈S−i
pt(g−i)Vi(σ˜g−i i |h t;g−i)
≥
∑
g−i∈S−i
pt(g−i)2Vi(σg−i i |h t;g−i)
=
∑
g−i∈S−i
pt(g−i)2M(g−i).
On the other hand,
sup
σi
Vi(σi|h t) = sup
σi
∑
g−i∈S−i
pt(g−i)Vi(σi|h t;g−i)≤ ∑
g−i∈S−i
pt(g−i)M(g−i).
Subtracting and usingM(g−i)≤1,
sup
σi
Vi(σi|h t)−V i(σPS i,t |h t)≤ ∑
g−i∈S−i
(
pt(g−i)−p t(g−i)2
)
M(g−i)
≤
∑
g−i∈S−i
(
pt(g−i)−p t(g−i)2
)
= 1−
∑
g−i∈S−i
pt(g−i)2 =D t i(ht).
This proves the claim.
Proof of Lemma C.2.Fixanyg−i∈S−i\{f−i}andarealizedpathz∈H ∞ inthefull-measureeventfrom
Assumption 8(2). By Bayes’ rule, for everyT≥1,
µT i (g−i|h T (z))
µT i (f−i|h T (z)) = µ0 i (g−i) µ0 i (f−i) Li,T (g−i;z) Li,T (f−i;z).
Assumption 8(2) implies that the likelihood ratio on the right converges to0, hence
µT i (g−i|h T (z))
µT i (f−i|h T (z))−→0.
65

Since this holds for everyg−i̸=f−i and the menu is finite,
RT (z) :=
∑
g−i∈S−i\{f−i}
µT i (g−i|h T (z))
µT i (f−i|h T (z))−→0µ f-a.s.
But
1 =µ T i (f−i|h T (z)) + ∑
g−i̸=f−i
µT i (g−i|h T (z)) =µ T i (f−i|h T (z)) ( 1 +RT (z) ) ,
so
µT i (f−i|h T (z)) = 1 1 +RT (z)−→1.
Consequently,
max
g−i∈S−i\{f−i}
µT i (g−i|h T (z))−→0.
Proof of Proposition 4.2.Fixε>0and work on a realized pathzin the full-measure event from Assump-
tion 3(2). For eacht, write
E:=E i(ht(z))andβ t i(ht(z)) := 1−µ t i(E|h t(z)).
By Assumption 3(2),
βt i(ht(z))−→0µ f-a.s. inz.
Fix such a historyht(z). For each sampled label˜g−i∈S −i, letσ ˜g−i i denote the continuation strategy
chosen by PS-BR when˜g−i is sampled. If˜g−i∈E, then by Definition 6, every label inEinduces the same
continuation-value functional afterht(z). Denote that common functional by
Wi(σi|h t(z)).
Let
Mi(ht(z)) := sup
σi
Wi(σi|h t(z)).
Because PS-BR best responds to the sampled label, for every˜g−i∈Ewe have
Wi(σ˜g−i i |h t(z)) =M i(ht(z)).
Now evaluate PS-BR under the full posterior predictive continuation value. Writingpt(g−i) =µ t i(g−i|
66

ht(z)), we have
Vi(σPS i,t |h t(z)) = ∑
˜g−i∈S−i
pt(˜g−i)
∑
g−i∈S−i
pt(g−i)Vi(σ˜g−i i |h t(z);g−i)
≥
∑
˜g−i∈E
pt(˜g−i)
∑
g−i∈E
pt(g−i)Wi(σ˜g−i i |h t(z))
=
(
1−β t i(ht(z)) )2Mi(ht(z)).
On the other hand, for any continuation strategyσi,
Vi(σi|h t(z)) = ∑
g−i∈E
pt(g−i)Wi(σi|h t(z)) + ∑
g−i/∈E
pt(g−i)Vi(σi|h t(z);g−i)
≤
(
1−β t i(ht(z)) ) Mi(ht(z)) +β t i(ht(z)),
where the last inequality uses that continuation values lie in[0,1]. Therefore
sup
σi
Vi(σi|h t(z))−V i(σPS i,t |h t(z))≤ ( 1−β t i(ht(z)) ) Mi(ht(z)) +β t i(ht(z))− ( 1−β t i(ht(z)) )2Mi(ht(z))
=β t i(ht(z)) +β t i(ht(z)) ( 1−β t i(ht(z)) ) Mi(ht(z))
≤2β t i(ht(z)).
Hence
σPS i,t (·|h t(z))∈BR 2βt i(ht(z)) i ( fi,t −i ⏐⏐ ht(z)|h t(z) ) .
Becauseβ t i(ht(z))→0, there exists a finite timeT i(z,ε)such that2β t i(ht(z))≤εfor allt≥T i(z,ε).
Therefore, for allt≥Ti(z,ε),
σPS i,t (·|h t(z))∈BR ε i ( fi,t −i ⏐⏐ ht(z)|h t(z) ) ,
which is exactly the claimed planner-side asymptoticε-consistency statement.
Proof of Lemma 5.1.Letµfi ≡P 0,fi i bethedistributioninducedbythepredictivereferenceprofile(f i,f i −i)
representing the prior predictive. By Assumption 2,µf≪µ fi .
By the merging of opinions theorem (Kalai and Lehrer, 1993a; Blackwell and Dubins, 1962), absolute
continuityguaranteesthattheconditionalpredictivedistributionsoverfutureplaypathsmergealmostsurely
in total variation. Specifically, forµf-almost every pathz∈H∞:
lim
t→∞
sup
E∈B
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐ = 0,
whereBis the productσ-algebra onH∞.
67

Recall from Definition 7 that the continuation weak distance is bounded by the total variation distance.
For any finite lengthk, theσ-algebraBk generated by cylinder events of lengthkis a sub-σ-algebra ofB.
Therefore:
sup
E∈Bk
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐≤sup
E∈B
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐.
Using this bound, the continuation weak distancedht(z)(µf,µfi )satisfies:
dht(z)(µf,µfi ) = ∞∑
k=1
2−k sup
E∈Bk
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐
≤
∞∑
k=1
2−k sup
E∈B
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐
= sup
E∈B
⏐⏐µf(E|C(h t(z)))−µ fi (E|C(h t(z))) ⏐⏐.
Since the total variation distance on the right-hand side converges to zero ast→∞forµf-almost everyz,
we have:
lim
t→∞
dht(z)(µf,µfi ) = 0µ f-a.s.
By the definition of the limit, for anyη >0, thereµ f-a.s. exists a finite timeTi(z,η)such that for
allt≥T i(z,η),d ht(z)(µf,µfi )≤η. This precisely satisfies the strong path prediction requirement in
Definition 10.
Proof of Proposition 5.2.Fixξ,η >0. For each playeri, the asymptoticε-consistency on-path condition
implies thatµf-a.s. inzthere existsT br i (z)such that for allt≥T br i (z),
fi
⏐⏐
ht(z)∈BR ξ i ( fi,t −i ⏐⏐ ht(z)|h t(z) ) .
By the representative choice (13), we may equivalently writefi,t −i ⏐⏐ ht(z)≡f i −i ⏐⏐ ht(z), so for allt≥T br i (z),
fi
⏐⏐
ht(z)∈BR ξ i ( fi −i ⏐⏐ ht(z)|h t(z) ) ,
which is exactly the subjective best-response condition in Definition 9.
Similarly, strong prediction implies thatµf-a.s. inzthere existsT pred i (z)such that for allt≥T pred i (z),
dht(z)(µf,µfi )≤η,
which is the weak predictive accuracy condition in Definition 9.
LetT(z) := max i{T br i (z), Tpred i (z)}, which is finiteµf-a.s. sinceIis finite. Then for allt≥T(z)
68

and every playeri, both conditions in Definition 9 hold with supporting profilefi, sof ⏐⏐ ht(z) is a weak
ξ-subjectiveη-equilibrium afterh t(z).
Proof of Theorem 5.3.Fixε >0and setξ:=ε/2. Letˆη(·,·)be the function from the infinite patching
lemma (Lemma B.4 in Appendix B), and setη:= ˆη(ξ,ε/2).
By Proposition 5.2,µf-a.s. inzthere existsT(z)such that for allt≥T(z), the continuation profilef ⏐⏐ ht(z)
is a weakξ-subjectiveη-equilibrium afterh t(z). Applying Lemma B.4 at each suchtyields anε-Nash
equilibrium ˆfε,t,z of the continuation game afterht(z)satisfyingd ht(z)(µf,µ ˆfε,t,z )≤ε.
Proof of Corollary 5.4.ByProposition4.2,underAssumption3,eachplayer’sselectedPS-BRcontinuation
planeventuallysatisfiestheasymptoticbest-responseconditionontherealizedpath. Underthecontinuation-
planimplementationconditioninthecorollary,thisisexactlytheasymptoticε-consistencypremiserequired
in Theorem 5.3. Because Assumption 3(1) places positive prior mass on the true opponent strategy,
Assumption 2 follows. Lemma 5.1 therefore guarantees each player learns to predict the path of play under
f. Theorem 5.3 then applies.
Proof of Lemma C.7.Fix anymi∈M i\{u i}and a realized pathω∈Ω. By Bayes’ rule (5) and the
definition ofKi,T in Assumption 9,
πT i (mi|x T i (ω))
πT i (ui|x T i (ω)) = π0 i (mi) π0 i (ui) Ki,T (mi;ω) Ki,T (ui;ω) .
By Assumption 9(3), the likelihood ratio on the right converges to0for everymi̸=u i, hence
πT i (mi|x T i (ω))
πT i (ui|x T i (ω)) −→0P β,u-a.s. inω.
SinceMi is finite,
∑
mi∈Mi\{ui}
πT i (mi|x T i (ω))
πT i (ui|x T i (ω)) −→0P β,u-a.s.
Using
1 =π T i (ui|x T i (ω))

1 + ∑
mi∈Mi\{ui}
πT i (mi|x T i (ω))
πT i (ui|x T i (ω))

,
we obtain
πT i (ui|x T i (ω))−→1forP β,u-almost everyω.
ByDefinition16,thetruemeanmatrixu i belongstoitsowncontinuation-decisionclassU i(hT (ω))atevery
69

public history. Hence
πT i (Ui(hT (ω))|x T i (ω))≥π T i (ui|x T i (ω))−→1P β,u-a.s.
which is exactly the stated pointwise payoff posterior concentration.
Proof of Lemma 6.1.Fix playeriand an observable historyxt i = (ht,r 1:t−1 i ). LetM:=S −i×Mi, and
for eachm= (g−i,mi)∈Mdefine the continuation value functional
Vm i (τi|x t i) :=V mi i (τi|h t;g−i)∈[0,1],
and the value envelope
M(m) := sup
τi∈Fi(ht)
Vm i (τi|x t i)∈[0,1].
For eachm∈Mfix a (measurable) best responseτm i attainingM(m), i.e.,V m i (τm i |x t i) =M(m).
ByDefinition15,PS-BRsamples(˜g−i,˜mi)∼p t(·)andthenplaysτ (˜g−i,˜mi) i . LetσPS i,t denotethisrandomized
continuation strategy atxt i.
BecauseV mix,t i is linear in both the opponents-mixture and the payoff-matrix mixture, we can write
V mix,t i (τi|x t i) = ∑
(g−i,mi)∈M
pt(g−i,mi)V (g−i,mi) i (τi|x t i) = ∑
m∈M
pt(m)V m i (τi|x t i).
Therefore, evaluating PS-BR under the mixed subjective objective gives
V mix,t i (σPS i,t |x t i) = ∑
˜m∈M
pt( ˜m)Vmix,t i (τ ˜m i |x t i)
=
∑
˜m∈M
pt( ˜m)
∑
m∈M
pt(m)V m i (τ ˜m i |x t i)
≥
∑
m∈M
pt(m)2Vm i (τm i |x t i) = ∑
m∈M
pt(m)2M(m).
On the other hand,
sup
τi∈Fi(ht)
V mix,t i (τi|x t i) = sup
τi∈Fi(ht)
∑
m∈M
pt(m)V m i (τi|x t i)≤ ∑
m∈M
pt(m) sup
τi∈Fi(ht)
Vm i (τi|x t i) = ∑
m∈M
pt(m)M(m).
Subtracting and usingM(m)≤1for allm,
sup
τi∈Fi(ht)
V mix,t i (τi|x t i)−V mix,t i (σPS i,t |x t i)≤ ∑
m∈M
(
pt(m)−p t(m)2) M(m)
≤
∑
m∈M
(
pt(m)−p t(m)2) = 1− ∑
m∈M
pt(m)2 =D t,joint i (xt i).
70

This proves the claim.
Proof of Lemma 6.2.Fix an observable historyxt i = (ht,r 1:t−1 i ). Write
pt(g−i,mi) :=µ t i(g−i|h t)πt i(mi|x t i),
let
Ft :=E priv i (ht)×U i(ht), r t := ∑
(g−i,mi)∈Ft
pt(g−i,mi) = (1−α t i(ht))(1−δ t i(xt i)).
For each sampled pair(˜g−i,˜mi), letτ ˜g−i,˜mi i denote the continuation strategy selected by PS-BR. If
(˜g−i,˜mi)∈F t,then˜g−i∈E priv i (ht)and˜mi∈U i(ht). ByDefinition16,˜miinducesthesamecontinuation-
value functional as the true mean matrixui against the sampled opponents’ model˜g−i. By the definition
ofE priv i (ht), every˜g−i∈E priv i (ht)is continuation-payoff equivalent tof−i underu i. Therefore, for every
(˜g−i,˜mi)∈F t and everyτi∈F i(ht),
V ˜mi i (τi|h t; ˜g−i) =V ui i (τi|h t;f−i).
Let
Mi(ht) := sup
τi∈Fi(ht)
Vui i (τi|h t;f−i).
For every(˜g−i,˜mi)∈F t, PS-BR chooses a best response to that pair, hence
Vui i (τ ˜g−i,˜mi i |h t;f−i) =M i(ht).
Evaluating against the mixed subjective objective gives
V mix,t i (σPS i,t |x t i) = ∑
(˜g−i,˜mi)
pt(˜g−i,˜mi)
∑
(g−i,mi)
pt(g−i,mi)Vmi i (τ ˜g−i,˜mi i |h t;g−i)
≥
∑
(˜g−i,˜mi)∈Ft
pt(˜g−i,˜mi)
∑
(g−i,mi)∈Ft
pt(g−i,mi)Vui i (τ ˜g−i,˜mi i |h t;f−i)
=r 2 tMi(ht).
For any continuation strategyτi∈F i(ht),
V mix,t i (τi|x t i)≤r tMi(ht) + (1−r t),
since all continuation values lie in[0,1]. Therefore
sup
τi∈Fi(ht)
V mix,t i (τi|x t i)−V mix,t i (σPS i,t |x t i)≤(1−r t) +rtMi(ht)−r 2 tMi(ht)
71

≤2(1−r t)
= 2
(
αt i(ht) +δt i(xt i)−α t i(ht)δt i(xt i) )
≤2α t i(ht) + 2δt i(xt i).
Using (11),
Vui,t i (σPS i,t |x t i)≥V mix,t i (σPS i,t |x t i)−δ t i(xt i)
≥sup
τi∈Fi(ht)
V mix,t i (τi|x t i)−2α t i(ht)−3δ t i(xt i)
≥sup
τi∈Fi(ht)
Vui,t i (τi|x t i)−2α t i(ht)−4δ t i(xt i).
This proves the claim.
Proof of Proposition 6.3.Work on the full-measure event on which both convergence statements hold:
αt i(ht(ω))−→0andδ t i(xt i(ω))−→0.
The first follows from Assumption 5; the second follows from Assumption 6. By Lemma 6.2, for every
observable historyxt i = (ht,r 1:t−1 i ),
sup
τi∈Fi(ht)
Vui,t i (τi|x t i)−V ui,t i (σPS i,t |x t i)≤2α t i(ht) + 4δt i(xt i).
Using the representative identity (9), this is exactly
sup
τi∈Fi(ht)
Vui i (τi|h t;gi,t −i)−V ui i (σPS i,t |h t;gi,t −i)≤2α t i(ht) + 4δt i(xt i).
Fixε>0. On the full-measure event above, chooseTi(ω,ε)such that for allt≥T i(ω,ε),
2αt i(ht(ω)) + 4δt i(xt i(ω))≤ε.
Then for all sucht,
σPS i,t (·|x t i(ω))∈BR ε i,ui ( gi,t −i|h t(ω) ) ,
which is exactly the claimed planner-side asymptoticε-consistency statement.
Proof of Lemma 6.4.Fix playeri. By the menu grain-of-truth part of Assumption 5, the true opponents’
public-historystrategyf −i belongstoplayeri’sretainedmenuwithpositivepriormass. Therefore,forevery
72

measurable eventE⊆H ∞,
P 0,fi i (E) =
∫
F−i
µ(fi,g−i)(E)dµ 0 i (g−i)≥µ 0 i (f−i)µ (fi,f−i)(E) =µ 0 i (f−i)µf(E).
Henceµf≪P 0,fi i ,i.e.,theordinarypublicgrain-of-truthconditionfromAssumption2holdsautomatically.
Applying Lemma 5.1 therefore yields
dht(ω)
(
µf,µfi) −→0forP β,u-a.e.ω,
wheref i = (fi,f i −i)is the representative predictive profile for playeri. By the continuation-consistent
representativechoicefromAppendixA,theconditionallawµ fi ht(ω) isexactlytheposteriorpredictivepublic-
action lawΠt i(·|x t i(ω)). Hence
d
(
Πt i(·|x t i(ω)),µf ht(ω) ) −→0forP β,u-a.e.ω.
Proof of Proposition 6.5.Fixξ,η >0. For each playeri, the assumed asymptoticξ-consistency condition
implies thatPβ,u-a.s. there existsTbr i (ω)such that for allt≥T br i (ω),
fi
⏐⏐
ht(ω)∈BR ξ i,ui ( gi,t −i|h t(ω) ) .
Also, Lemma 6.4 implies thatPβ,u-a.s. there existsTpred i (ω)such that for allt≥T pred i (ω),
dht(ω)
(
µf,µ (fi,gi,t −i) ) ≤η.
Let
T(ω) := max
i∈I
{T br i (ω),T pred i (ω)}.
Then for allt≥T(ω)and every playeri, both conditions in Definition 17 hold with supporting profile
(fi,gi,t −i).
Proof of Theorem 6.6.Fixε>0and setξ:=ε/2. Letˆη(·,·)be the function from Lemma B.4, and set
η:= ˆη(ξ,ε/2).
By the assumed asymptotic on-pathξ-consistency condition together with Lemma 6.4, the hypotheses of
Proposition 6.5 hold. ThereforePβ,u-a.s. there existsT(ω)such that for allt≥T(ω), the continuation
profilef
⏐⏐
ht(ω) is a weakξ-subjectiveη-equilibrium afterht(ω). Applying Lemma B.4 at each suchtyields
73

a continuation profileˆfε,t,ω that is anε-Nash equilibrium afterht(ω)and satisfies
dht(ω)
(
µf,µ ˆfε,t,ω) ≤ε/2≤ε.
This is exactly the stated conclusion.
Proof of Lemma 5.5.Fix playeri, letp,q∈∆(A −i), and supposeαi∈br ξ i (q).
For anyαi∈∆(A i)define
ϕαi(a−i) :=
∑
ai∈Ai
αi(ai)ui(ai,a−i), a −i∈A−i.
Sinceui(ai,a−i)∈[0,1], we haveϕ αi(a−i)∈[0,1]for alla −i∈A−i. Also,
ui(αi,p)−u i(αi,q) =
∑
a−i∈A−i
ϕαi(a−i)
(
p(a−i)−q(a −i)
)
.
Set
S+ :={a−i∈A−i :p(a−i)≥q(a −i)}.
Because0≤ϕ αi≤1, we have
ui(αi,p)−u i(αi,q) =
∑
a−i∈S+
ϕαi(a−i)
(
p(a−i)−q(a −i)
)
+
∑
a−i/∈S+
ϕαi(a−i)
(
p(a−i)−q(a −i)
)
≤
∑
a−i∈S+
(
p(a−i)−q(a −i)
)
=p(S +)−q(S +)
≤∥p−q∥ TV.
Applying the same argument withpandqinterchanged yields
ui(αi,q)−u i(αi,p)≤∥p−q∥ TV.
Therefore
|ui(αi,p)−u i(αi,q)|≤∥p−q∥ TV for everyαi∈∆(A i).(17)
Now supposeαi∈br ξ i (q). Then
ui(αi,q)≥sup
α′ i∈∆(Ai)
ui(α′ i,q)−ξ.
74

Using (17),
ui(αi,p)≥u i(αi,q)−∥p−q∥ TV
≥sup
α′ i∈∆(Ai)
ui(α′ i,q)−ξ−∥p−q∥ TV
≥sup
α′ i∈∆(Ai)
(
ui(α′ i,p)−∥p−q∥ TV ) −ξ−∥p−q∥ TV
= sup
α′ i∈∆(Ai)
ui(α′ i,p)−ξ−2∥p−q∥ TV.
Hence
αi∈br ξ+2∥p−q∥ TV i (p).
Proof of Lemma 5.6.Fix playeriand historyht. For eachg−i∈S−i define
M(g−i) := sup
αi∈∆(Ai)
ui
(
αi,g−i(ht) ) ∈[0,1].
By Definition 12, for eachg−i∈S−i we have chosen
αg−i,ht i ∈br i ( g−i(ht) ) ,
so
ui
(
αg−i,ht i ,g−i(ht) ) =M(g −i).
Writept(g−i) =µ t i(g−i|h t). The ex ante mixed action induced by myopic PS-BR is
αmPS i,t (·|h t) = ∑
˜g−i∈S−i
pt(˜g−i)α ˜g−i,ht i (·),
and the one-step posterior predictive belief is
qt i(·|h t) = ∑
g−i∈S−i
pt(g−i)g−i(ht)(·).
By bilinearity ofui(·,·),
ui
(
αmPS i,t ,qt i ) = ∑
˜g−i∈S−i
pt(˜g−i)
∑
g−i∈S−i
pt(g−i)ui
(
α˜g−i,ht i ,g−i(ht) )
≥
∑
g−i∈S−i
pt(g−i)2ui ( αg−i,ht i ,g−i(ht) )
75

=
∑
g−i∈S−i
pt(g−i)2M(g−i).
On the other hand, again by bilinearity,
sup
αi∈∆(Ai)
ui(αi,qt i) = sup
αi∈∆(Ai)
∑
g−i∈S−i
pt(g−i)ui
(
αi,g−i(ht) )
≤
∑
g−i∈S−i
pt(g−i) sup
αi∈∆(Ai)
ui
(
αi,g−i(ht) )
=
∑
g−i∈S−i
pt(g−i)M(g−i).
Subtracting,
sup
αi
ui(αi,qt i)−u i(αmPS i,t ,qt i)≤ ∑
g−i∈S−i
(
pt(g−i)−p t(g−i)2) M(g−i)
≤
∑
g−i∈S−i
(
pt(g−i)−p t(g−i)2)
= 1−
∑
g−i∈S−i
pt(g−i)2
=D t i(ht).
This proves the claim.
Proof of Lemma 5.8.Fix a historyht and write
pt(g−i) :=µ t i(g−i|h t),E st :=E st i (ht), p st E :=µ t i(Est i (ht)|h t) = 1−β t i(ht).
For eachg−i∈S−i, letαg−i,ht i ∈br i(g−i(ht))be the mixed action selected in Definition 12. Ifg−i∈E st,
then by Definition 13,g−i(ht)induces exactly the same one-step stage optimization problem as the true
current opponents’ mixed actionf−i(ht). Henceαg−i,ht i is also a best response tof−i(ht). Let
Mi(ht) := sup
αi∈∆(Ai)
ui(αi,f−i(ht)).
Using linearity of stage payoffs in the player’s own mixed action,
ui
(
αmPS i,t ,f−i(ht) ) = ∑
g−i∈S−i
pt(g−i)ui
(
αg−i,ht i ,f−i(ht) )
≥
∑
g−i∈E st
pt(g−i)Mi(ht)
= (1−β t i(ht))Mi(ht).
76

SinceMi(ht)≤1, we obtain
Mi(ht)−u i ( αmPS i,t ,f−i(ht) ) ≤β t i(ht),
which is exactly the stated bound.
Proof of Lemma 5.7.Fix playeriand letfi = (fi,f i −i)be the supporting profile from Definition 10. Fix a
realizedpathz∈H ∞inthefull-measureeventfromDefinition10. Bydefinitionofq t i andtherepresentative
choice (13),
qt i(·|h t(z)) =f i,t −i(ht(z)) =f i −i(ht(z)).
Letη >0. By Definition 10, there existsTi(z,η/2)<∞such that for allt≥T i(z,η/2),
dht(z)(µf,µfi )≤η/2.
Fix such at. For any subsetB⊆A−i, define the one-step cylinder event
EB :={y∈H ∞ :y 1 −i∈B}∈B 1.
By the definition of continuation measures,
µf ht(z)(EB) =f−i(ht(z))(B), µ fi ht(z)(EB) =f i −i(ht(z))(B) =q t i(B|h t(z)).
Therefore,
‖‖qt i(·|h t(z))−f −i(ht(z)) ‖‖ TV = sup B⊆A−i ⏐⏐⏐qt i(B|h t(z))−f −i(ht(z))(B) ⏐⏐⏐
= sup
B⊆A−i
⏐⏐⏐µfi ht(z)(EB)−µ f ht(z)(EB) ⏐⏐⏐
≤sup
E∈B 1
⏐⏐⏐µfi ht(z)(E)−µ f ht(z)(E) ⏐⏐⏐.
By Definition 7,
dht(z)(µf,µfi ) = ∞∑
k=1
2−k sup
E∈Bk
⏐⏐⏐µf ht(z)(E)−µ fi ht(z)(E) ⏐⏐⏐.
In particular,
1
2 sup E∈B 1
⏐⏐⏐µf ht(z)(E)−µ fi ht(z)(E) ⏐⏐⏐≤d ht(z)(µf,µfi ),
so
sup
E∈B 1
⏐⏐⏐µf ht(z)(E)−µ fi ht(z)(E) ⏐⏐⏐≤2d ht(z)(µf,µfi )≤η.
77

Hence ‖‖qt i(·|h t(z))−f −i(ht(z)) ‖‖ TV≤η
for allt≥T i(z,η/2). Sinceη >0was arbitrary, this proves the claim.
Proof of Theorem 5.9.Fixε>0. For each playeri, work on the full-measure event from Assumption 4(2),
so that along the realized pathz,
βt i(ht(z)) := 1−µ t i(Est i (ht(z))|h t(z))−→0.
Because playeriuses myopic PS-BR, we have
fi(ht(z)) =α mPS i,t (·|h t(z)).
ChooseTi(z,ε)such that
βt i(ht(z))≤εfor allt≥T i(z,ε).
Then for everyt≥Ti(z,ε), Lemma 5.8 implies
fi(ht(z))∈br ε i ( f−i(ht(z)) ) .
Intersecting these full-measure events over the finite player set and taking
T(z) := max
i∈I
Ti(z,ε)<∞,
we obtain that for allt≥T(z)and all playersi,
fi(ht(z))∈br ε i ( f−i(ht(z)) ) .
By Definition 11, this means thatf(ht(z))is a stageε-Nash equilibrium for allt≥T(z).
Proof of Lemma 5.10.Fix playeriand letfi = (fi,f i −i)be the supporting profile from Definition 10. Fix
a realized pathzin the full-measure event from Definition 10. By definition ofqt i and the representative
choice (13),
qt i(·|h t(z)) =f i,t −i(ht(z)) =f i −i(ht(z)).
For eacht, define the one-step cylinder event
Et(z) :={y∈H ∞ :y 1 −i =a ⋆ −i(ht(z))}∈B 1.
78

Because the true opponents’ next action at historyht(z)is pure,
f−i(ht(z)) =δ a⋆ −i(ht(z)),
so
µf ht(z)(Et(z)) = 1.
Also, by the on-path identification above,
µfi ht(z)(Et(z)) =f i −i(ht(z)) ( a⋆ −i(ht(z)) ) =q t i ( a⋆ −i(ht(z))|h t(z) ) .
Hence
1−q t i ( a⋆ −i(ht(z))|h t(z) ) = ⏐⏐⏐µf ht(z)(Et(z))−µ fi ht(z)(Et(z)) ⏐⏐⏐
≤sup
E∈B 1
⏐⏐⏐µf ht(z)(E)−µ fi ht(z)(E) ⏐⏐⏐.
As in the proof of Lemma 5.7,
sup
E∈B 1
⏐⏐⏐µf ht(z)(E)−µ fi ht(z)(E) ⏐⏐⏐≤2d ht(z)(µf,µfi ).
Because playerilearns to predict the path of play,
dht(z)(µf,µfi )−→0.
Therefore
qt i ( a⋆ −i(ht(z))|h t(z) ) −→1.
It follows immediately that
1−max
a−i∈A−i
qt i(a−i|h t(z))≤1−q t i ( a⋆ −i(ht(z))|h t(z) ) −→0,
which proves asymptotic purity.
Finally, because
qt i ( a⋆ −i(ht(z))|h t(z) ) −→1,
there existsTi(z)<∞such that for allt≥T i(z),
qt i ( a⋆ −i(ht(z))|h t(z) ) > 1 2.
For sucht, the actiona⋆ −i(ht(z))is the unique maximizer ofqt i(·|h t(z)), because all other probabilities
79

sum to
1−q t i ( a⋆ −i(ht(z))|h t(z) ) < 1 2.
Hence the deterministic MAP selector must satisfy
ˆat −i(ht(z)) =a ⋆ −i(ht(z))for allt≥T i(z).
This proves the claim.
Proof of Theorem 5.11.Becauseeveryplayerj∈IusesdeterministicMAP-SCoT,foreveryhistoryh∈H
we have
fj(h) =δ a⋆ j (h) for somea⋆ j(h)∈A j.
Hence for every playeriand every historyh,
f−i(h) =δ a⋆ −i(h) for somea⋆ −i(h)∈A −i.
For each playeri, apply Lemma 5.10. There is a full-measure event on which there existsTi(z)<∞such
that for allt≥T i(z),
ˆat −i(ht(z)) =a ⋆ −i(ht(z)).
BecausetheplayersetIisfinite,theintersectionofthesefull-measureeventsoverallplayersstillhasmeasure
one.
Fix a realized pathzin that intersection. For any playeriand anyt≥Ti(z), Definition 14 gives
fi(ht(z)) =δ bi(ˆat −i(ht(z))) =δ bi(a⋆ −i(ht(z))).
By definition of the pure best-response selectorbi,
bi(a−i)∈arg max ai∈Ai ui(ai,a−i)for everya −i∈A−i.
Therefore
δbi(a⋆ −i(ht(z)))∈br i
(
δa⋆ −i(ht(z))
)
= bri
(
f−i(ht(z)) ) .
So for every playeriand allt≥Ti(z),
fi(ht(z))∈br i ( f−i(ht(z)) ) .
Define
T(z) := max
i∈I
Ti(z)<∞.
80

Then for allt≥T(z)and every playeri,
fi(ht(z))∈br i ( f−i(ht(z)) ) .
By Definition 11, this means thatf(ht(z))is a stage Nash equilibrium for allt≥T(z).
Proof of Corollary 5.12.By Lemma 5.1, Assumption 2 implies that every player learns to predict the path
of play underfin the sense of Definition 10. Theorem 5.11 therefore applies directly.
81

D Bounded-memory strategies and finite-state reduction
Manypracticalagentpolicies(includingmenu-basedplanners)dependonlyonaboundedwindowofrecent
interaction. Following the bounded-recall restriction in Norman (2022), we formalize this as abounded-
memorycondition.
For a historyh= (a1,...,a t−1)∈Hlet|h|:=t−1denote its length. Forκ∈N, define
suffixκ(h) := (a t−min{κ,t−1},...,a t−1)∈
κ⋃
m=0
Am,
i.e., the lastmin{κ,|h|}joint actions ofh(withsuffix κ(∅) =∅).
Definition 19(κ-memory (bounded-recall) strategy).A strategyfi :H→∆(A i)hasmemory at mostκif
for all historiesh,h′∈H,
suffixκ(h) = suffixκ(h′) =⇒f i(h) =f i(h′).
LetF κ i ⊆F i denote the set ofκ-memory strategies for playeri, and writeFκ :=∏ i∈IFκ i .
Let
Sκ :=
κ⋃
m=0
Am
be the finite set of action-suffixes of length at mostκ. Define the deterministic state update mapTκ :
Sκ×A→S κ by
Tκ(s,a) := suffix κ((s,a)),
i.e., append the new joint actionato the suffixsand keep the lastκentries. For any play pathz=
(a1,a 2,...)∈H ∞, define the induced memory state at timet:
st(z) := suffix κ(ht(z))∈S κ.
Lemma D.1(Finite-state Markov property under bounded memory).Iff∈F κ, then for everyt≥1and
every historyht withs= suffix κ(ht), the next-period action distribution depends onht only throughs:
µf(at =a|h t) = ∏
i∈I
fi(s)(ai).
Moreover, the induced state process satisfiesst+1 =T κ(st,at)almost surely, so(s t)t≥1 is a time-
homogeneous Markov chain onSκ.
82

Proof.Fixtand historyh t. By Definition 2,
µf(at =a|h t) = ∏
i∈I
fi(ht)(ai).
Iff∈F κ, thenfi(ht) =f i(suffixκ(ht)) =f i(s)for eachi, giving the displayed equality. The state update
is deterministic by construction ofTκ:s t+1 = suffixκ(ht+1) = suffixκ((ht,at)) =T κ(suffixκ(ht),at) =
Tκ(st,at). Thus(st)is Markov with kernel induced by the conditional law ofat givenst.
Lemma D.2(Continuation distributions depend only on the memory state).Letg∈Fκ and leth,h′∈H
satisfysuffix κ(h) = suffixκ(h′). Then the continuation play-path distributions coincide:
µg h =µ g h′.
Proof.By Lemma D.1, the conditional distribution of the next action profile and all future evolution under
gdependsonthepastonlythroughthecurrentmemorystates= suffix κ(·). Sincehandh ′ inducethesame
state, the induced kernels for(at,at+1,...)are identical from either starting history. Therefore the induced
continuation measures coincide.
D.1 Best responses to bounded-memory opponents are bounded-memory
A key benefit of bounded-memory opponents is that each player faces a finite-state discounted MDP in the
continuationgame. Inparticular, thebest-responsesearchinBR ε i (g−i|h t)canberestrictedwithoutlossto
bounded-memory policies.
Lemma D.3(Markovian best responses toκ-memory opponents).Fix playeri, a historyh t, and an
opponents’ continuation profileg−i∈F κ −i. Then there exists a best responseσ⋆ i ∈BR i(g−i|h t)that is
stationary Markovwith respect to the memory state. That is, there exists a mapπi :S κ→∆(A i)such that
for every continuation history¯h⪰h t,
σ⋆ i (¯h) =π i(suffixκ(¯h)).
Consequently, for everyε≥0,
sup
σi∈Fi(ht)
Vi(σi|h t;g−i) = sup
σi∈Fκ i (ht)
Vi(σi|h t;g−i),
andBR i(g−i|h t)∩F κ i (ht)̸=∅.
Proof.Lets 0 := suffixκ(ht)∈S κ. Fixg−i∈F κ −i. Define a controlled Markov process onSκ as follows.
In states, the player choosesai∈A i, the opponents’ joint action is drawn asa−i∼g−i(s)∈∆(A −i), the
stage payoff isui(ai,a−i), and the next state iss′ =T κ(s,(ai,a−i)).
83

For any bounded functionv:Sκ→R, define the Bellman operatorTby
(Tv)(s) := max
α∈∆(Ai)
E ai∼α
a−i∼g−i(s)
[
(1−λ i)ui(ai,a−i) +λiv
(
Tκ(s,(ai,a−i))
)]
.
Becauseλi∈(0,1),Tis a contraction in∥·∥ ∞: for anyv,wand anys,
|(Tv)(s)−(Tw)(s)|≤max α E
[
λi|v(s′)−w(s ′)| ] ≤λ i∥v−w∥ ∞.
HenceThas a unique fixed pointV⋆ :S κ→R.
For eachs, the maximization overα∈∆(A i)attains its maximum because∆(A i)is compact and the
objectiveiscontinuousandlinearinα. Fixamaximizerπ i(s)∈∆(A i)foreachsanddefinetheassociated
policy evaluationoperator
(Tπiv)(s) :=E ai∼πi(s)
a−i∼g−i(s)
[
(1−λ i)ui(ai,a−i) +λiv
(
Tκ(s,(ai,a−i))
)]
.
Then(T πiV⋆)(s) = (TV ⋆)(s) =V ⋆(s)for alls, soV ⋆ is a fixed point ofTπi. SinceT πi is also a
λi-contraction, its fixed point is unique; denote it byVπi. We concludeVπi =V ⋆.
Now defineσ⋆ i to be the stationaryMarkov continuation strategy induced byπi, i.e.σ⋆ i (¯h) =π i(suffixκ(¯h))
for all¯h⪰h t. By construction, the induced continuation value fromht isVi(σ⋆ i|h t;g−i) =V ⋆(s0).
It remains to show optimality againstallcontinuation strategies, including those with unbounded memory.
Letσi be any continuation strategy and define itsstatewise value envelope
Wσi(s) := sup
{
Vi(σi| ¯h;g−i) : ¯h⪰h t,suffix κ(¯h) =s } .
Fixanysandϵ>0,andchoose ¯hwithsuffix κ(¯h) =sandV i(σi| ¯h;g−i)≥W σi(s)−ϵ. Letα:=σ i(¯h)∈
∆(Ai)be the first-step mixed action. Conditioning on the first joint action(ai,a−i)and using that the next
state iss′ =T κ(s,(ai,a−i)), we have
Vi(σi| ¯h;g−i) =E
[
(1−λ i)ui(ai,a−i) +λiVi(σi|( ¯h,(ai,a−i));g−i)
]
≤E
[
(1−λ i)ui(ai,a−i) +λiWσi(s′) ] .
Therefore,
Wσi(s)−ϵ≤E ai∼α a−i∼g−i(s)
[
(1−λ i)ui(ai,a−i) +λiWσi(Tκ(s,(ai,a−i)))
]
≤(TW σi)(s).
Lettingϵ↓0givesW σi ≤ TWσi pointwise. By monotonicity ofTand contraction, iterating yields
Wσi≤T nWσi for alln, andTnWσi→V ⋆ uniformly asn→∞. HenceW σi(s)≤V ⋆(s)for alls, and in
84

particular
Vi(σi|h t;g−i)≤W σi(s0)≤V ⋆(s0) =V i(σ⋆ i|h t;g−i).
Thusσ ⋆ i isabestresponse. Thefinaldisplayedequalityofsupremafollowsbecauseanoptimalpolicyexists
withinF κ i (ht).
D.2 A checkable route to on-path elimination under bounded memory
Assumption 8(2) requires only that every wrong retained hypothesis becomes negligible relative to the true
one along the realized path. This appendix-level condition is itself stronger than necessary if two retained
labels are continuation-payoff- equivalent from reached histories, but it is a convenient route to posterior
concentration for our sampled-label PS-BR proof. Under bounded memory, recurrent-state KL separation
provides a transparent sufficient route to this eventual on-path elimination.
Lemma D.4(State-frequency decomposition of on-path KL averages).Fix playeri,κ∈N, andf−i,g−i∈
Fκ −i. For a realized pathz, definest(z) = suffixκ(ht(z))and empirical state frequencies
ˆπz T (s) := 1 T T∑ t=1 1{st(z) =s}, s∈S κ.
Then for everyTand everyz,
1
T
T∑
t=1
DKL
(
f−i(ht(z)) ‖‖‖g−i(ht(z)) ) = ∑
s∈Sκ
ˆπz T (s)D KL
(
f−i(s)
‖‖‖g−i(s) ) .
In particular, for any fixed states,
lim inf
T→∞
1
T
T∑
t=1
DKL
(
f−i(ht(z)) ‖‖‖g−i(ht(z)) ) ≥ ( lim inf T→∞ ˆπz T (s) ) ·D KL ( f−i(s) ‖‖‖g−i(s) ) .
Proof.Iff −i,g−i∈F κ −i, thenforeachtwehavef −i(ht(z)) =f−i(st(z))andg −i(ht(z)) =g−i(st(z))by
Definition 19. Therefore,
1
T
T∑
t=1
DKL
(
f−i(ht(z)) ‖‖‖g−i(ht(z)) ) = 1 T T∑ t=1 DKL ( f−i(st(z)) ‖‖‖g−i(st(z)) ) .
Grouping the sum by the value ofst(z)yields the stated decomposition. The inequality follows by lower
bounding the sum by a single state’s contribution and takinglim inf.
Corollary D.5(A sufficient condition for on-path elimination under bounded memory).Fix playeriand
85

supposeS−i⊆F κ −i. Fixg−i∈S−i\{f−i}and define
τi(g−i) := inf{t≥1 :g −i(ht)(at −i) = 0},
with the conventioninf∅=∞. Assume thatµ f-a.s. one of the following holds:
(a) (Hard refutation)τi(g−i)<∞.
(b) (Common-support recurrent separation) On the survival event{τi(g−i) =∞}, common support holds
on the visited suffix states, and there existss∈Sκ such that
DKL
(
f−i(s)∥g−i(s)
)
>0,lim inf
T→∞
ˆπz T (s)≥ρ i(g−i)>0.
Then Assumption 8(2) holds for thisg−i.
Proof.If case (a) holds, then along any such pathzthe denominator likelihoodLi,T (g−i;z)becomes zero
from timeτi(g−i)(z) + 1onward whileLi,T (f−i;z)>0, so
Li,T (g−i;z)
Li,T (f−i;z) = 0
for all sufficiently largeT. Hence Assumption 8(2) is immediate.
Now consider case (b). On the survival event{τi(g−i) =∞}, define
Xt(z) := log f−i(ht(z))(at −i(z)) g−i(ht(z))(at −i(z)).
Because the menu and suffix-state space are finite and common support holds on the visited states, the
positive probabilities that can appear in the denominator are bounded away from zero on this event. Thus
(Xt)is uniformly bounded there. Let
Yt :=X t−Eµf [Xt|F t].
Then(Yt,Ft)is a bounded martingale-difference sequence, so by the martingale strong law,
1
T
T∑
t=1
Yt−→0µ f-a.s. on{τi(g−i) =∞}.
Moreover, on the survival event,
Eµf [Xt|F t] =D KL
(
f−i(ht) ‖‖‖g−i(ht) ) .
86

Therefore,
1
T logLi,T (f−i;z) Li,T (g−i;z) = 1 T T−1∑ t=1 Xt = 1 T T−1∑ t=1 DKL ( f−i(ht) ‖‖‖g−i(ht) ) +o(1).
Lemma D.4 and the positive-frequency assumption on statesimply
lim inf
T→∞
1
T logLi,T (f−i;z) Li,T (g−i;z) ≥ρ i(g−i)·D KL ( f−i(s)∥g−i(s) ) >0
µf-a.s. on{τi(g−i) =∞}. Hence
logLi,T (g−i;z) Li,T (f−i;z) −→−∞,so Li,T (g−i;z) Li,T (f−i;z) −→0
µf-a.s. on{τi(g−i) =∞}. Therefore Assumption 8(2) holds in case (b) as well.
All statements in Sections 4–5 are formulated on the full history spaceHand therefore apply without
modification when the realized profilef(and/or the menu strategies in the appendix-level retained-menu
identificationcondition,Assumption8)lieinF κ. Relativetothemain-textconcentration-up-to-equivalence
assumption(Assumption3),theappendixrecordsstrongersufficientretained-menuidentificationconditions
(Assumption8andthedeterministichard-refutationconditionAssumption7)andaddstwofinite-statetools:
(i) best responses toκ-memory opponents can be taken to be stationary Markov (Lemma D.3); and (ii)
on-path elimination can be verified by recurrent-state KL separation under common support or by finite-
time hard refutation (Lemma D.4 and Corollary D.5). Thus bounded memory is not required for the main
concentrationresult,butitgivesatransparentfinite-staterouteforcheckingstrongersufficientconditionsfor
the appendix-level PS-BR identification argument.
87

E Implementation details of the strategy-level PS-BR planner
This appendixdetails the implementation usedin our experiments. Ateach round, an agent samplesa latent
opponent strategy from its inference based on the previous history, evaluates candidate self-strategies by
rollout, and plays the current action induced by the best rollout-value strategy.
E.1 Opponent strategy sampling
Fixplayeriatroundtwithlocalhistoryh t i = ((a1 i,a 1 −i),...,(a t−1 i ,at−1 −i )). Foropponent-strategyinference,
the implementation rewrites this to the opponent-view history
˜ht −i = ((a1 −i,a 1 i ),...,(a t−1 −i ,at−1 i )),
so each tuple is ordered as(opponent action, your action). The opponent strategy inference is performed
once per real decision round(with configured label-sampling temperature) and then held fixed across allK
rollout samples used to evaluate candidate self-strategies at that round. Inference supports two modes:
•llm-label(default):constructanin-contextpromptcontainingthegamerules,observedhistory,andthe
allowed strategy labels (with short descriptions), then ask the model to outputexactly one label. Parsing
is label-constrained; if parsing fails repeatedly, a deterministic label fallback is used.
•likelihood:infer from a hand-coded likelihood over the menu (described below), with no model call.
llm-labelmodedetails.Inllm-labelmode,ifthemodelcallitselffails,theimplementationfallsback
tolikelihoodmode for that decision round.
The template used in code is:
{rules_text}
Observed action history tuple format: (opponent action, your action).
Infer the opponent strategy from the FIRST action in each tuple.
Round 1: {opp_action_1}, {self_action_1}
Round 2: {opp_action_2}, {self_action_2}
...
You are inferring the opponent strategy in repeated {game_name}.
Observed rounds so far: {observed_rounds}.
Objective: sample one opponent strategy label according to your
posterior belief over allowed labels.
Estimate that posterior using ALL observed rounds
(do not ignore older rounds), and focus on recent patterns.
The opponent may change strategy over time; if you detect a shift,
prioritize the most recent consistent behavior while still
accounting for earlier rounds.
Internally assign a compatibility score from 0 to 100 to every
88

allowed label, convert them into relative posterior weights, and
sample exactly one final label from those weights.
Output rule: do NOT output scores, reasoning, or ranking.
Respond with exactly one label only.
**Output only the label.**
Allowed labels:
- {label_1}: {description_1}
- {label_2}: {description_2}
...
wheregame_nameis the active repeated-game name (e.g., BoS, PD, Promo, Samaritan’s dilemma, or
Lemons), andobserved_rounds=t-1.
When collusive-prior guidance is enabled (–collusive-mode), the prompt appends a strong-prior line. In
our code this prior ismad0for Promo opponent 1 andmad1for Promo opponent 2.
Likelihood-modedetails.Toscorestrategys,theimplementationevaluateshistoryundertheopponent’s
perspective ˜ht −i = ((a1 −i,a 1 i ),...,(a t−1 −i ,at−1 i )):
logLt(s) =
t−1∑
u=1
log
(
1{au −i =J}p u s +1{au −i =F}(1−p u s) ) ,
with clipping to[10−6,1−10 −6]for numerical stability. Given temperatureτ >0(implemented as
τ= max{sample_temperature,10 −5}), weights are
wt(s)∝exp
(logLt(s)
τ
)
,
and one opponent strategy is sampled from this categorical distribution.
E.2 Rollout value and strategy selection
Givenasampledopponentstrategys −i,foreverycandidateself-strategys i∈M g,theplannerrollsoutfrom
roundtto ¯t, where
¯t=



min{T, t+H−1}, H >0,
T, H= 0,
Tis the game horizon, andHis the planning horizon.
Forrolloutsamplem∈{1,...,K},ateachsimulatedroundr,actionsaresampledfromthefixedopponent
strategys−i and the currently evaluated candidatesi:
ˆar,m i ∼Bernoulli ( pr si ) ,ˆa r,m −i ∼Bernoulli ( pr s−i ) ,
89

Algorithm 1Strategy-level PS-BR loop for two-player games
Require:gameg, total roundsT, menuM g, samplesK, horizonH, discountγ, temperatureτ, inference
mode∈{llm-label,likelihood}
1:Initializeh 1←∅,x 1 1←(h 1,∅),x 1 2←(h 1,∅),C 1←0, andC 2←0
2:fort= 1,...,Tdo
3:fori∈{1,2}do
4:Letx t i = (ht,r 1:t−1 i )be playeri’s current local history
5:Construct opponent-view history ˜ht −i by swapping tuple order in the public historyht
6:Infer one strategy labels −i∈M g from rules, history˜ht −i
7:for alls i∈M g do
8:fork= 1,...,Kdo
9:V (k) i (si|s−i)←RolloutValue(g,i,s i,s−i,xt i,t,T,H,γ)
10: ¯Vi(si|s−i)← 1 K ∑K k=1V (k) i (si|s−i)
11:s ⋆ i←arg maxsi∈Mg ¯Vi(si|s−i)▷deterministic tie-break
12:Sample real actiona t i from strategys⋆ i at historyxt i
13:Sample realized rewards(r t 1,rt 2)from the environment payoff law at(at 1,at 2)
14:C 1←C 1 +rt 1 andC 2←C 2 +rt 2
15:Seth t+1←(h t,(at 1,at 2))
16:Setx t+1 1 ←(h t+1,r 1:t 1 )andx t+1 2 ←(h t+1,r 1:t 2 )
wherep r si andp r s−i are the round-rprobabilities of actionJinduced bys i ands−i under the simulated
history prefix generated so far. The rollout value for candidatesi against sampled opponent strategys−i is
V (m) i (si|s−i) =
¯t∑
r=t
γr−tui(ˆar,m i ,ˆar,m −i ),
with discountγ.
The estimated value of strategysi is
¯Vi(si|s−i) = 1 K K∑ m=1 V (m) i (si|s−i),
and the chosen strategy is
s⋆ i∈arg maxsi ¯Vi(si|s−i),
withdeterministichash-basedtie-breakingwhenneeded. Theexecutedactionatrealroundtisthensampled
froms⋆ i at the current history.
For Experiment 3, the environment payoff law in Algorithm 1 is the known Gaussian noise family centered
at the true mean matrix. On the player’s own side, playeriadditionally samples˜mi∼π t i(·|x t i), rollout
values are computed under˜mi in place of the trueui, and playeri’s local information history stores only
90

(ht,r 1:t−1 i ); in particular, the update step above never reveals or conditions onr1:t−1 −i .
91

F Social chain-of-thought prompting (SCoT)
This appendix shows that SCoT can be viewed as a special case of PS-BR. Thesocial chain-of-thought
prompting intervention of Akata et al. (2025) is a particularly simple two-stage “predict-then-act” instance
of PS-BR.
F.1 SCoT as a two-stage “predict-then-act” operator
In Akata et al. (2025), SCoT is implemented byprompt-chainingin each round of a repeated game:
1.Prediction prompt (belief elicitation).Given the public historyh t, the model is asked to predict the
opponent’s next move (or, more generally, to describe what the other player will do next).
2.Actionprompt(bestresponsetotheelicitedbelief).Themodelisthenaskedtochooseitsactiongiventhe
predicted opponent move, typically phrased as “given your prediction, what is best for you to do now?”
This“separatebeliefreport,thenact”structureforcesanexplicittheory-of-mindstepbeforeactionselection,
and empirically improves coordination in some repeated games.
F.2 Mapping SCoT as a special case of PS-BR
Fix agentiat historyh t. LetA−i denote the opponents’ joint action space, and define the agent’sposterior
predictiveover opponents’ next action as
qt i(·|h t)∈∆(A −i).
In our paper’s belief language,qt i(·|h t)is the one-step marginal induced by the agent’s posterior predictive
continuation belieffi,t −i|ht.
SCoT can then be expressed as the following generic operator:
1.Inference:produce˜a t −i as an imputation of the missing opponents’ next action. Operationally, this is
obtained by querying the model with the prediction prompt.
2.Optimize given the imputation:choosea t i as an (approximate) best response to the imputed˜at −i (and the
known payoffs), e.g.
at i∈arg max ai∈Ai ui(ai,˜at −i)(myopic).
More generally, one may replaceui by the continuation objective, i.e., chooseat i (or a continuation
strategy) that maximizes the discounted value conditional on˜at −i and the induced continuation play.
Two special cases are worth separating because they clarify the relationship to PS-BR.
(i) Deterministic SCoT = point estimation.In the implementation studied by Akata et al. (2025), the
model is often run in a near-deterministic regime (e.g., decoding choices consistent with temperature≈0),
so the prediction step behaves like a point estimate (roughly “MAP” under the model’s implicit predictive
92

distribution). Inthisview,SCoTisaninference-and-optimizeheuristicthatcanstillimproveplaybymaking
the model’s implicit prediction problem explicit.
(ii) Myopic PS-BR = sampling-based estimation.If instead the prediction prompt is decoded stochas-
tically (e.g., sampling at nonzero temperature), then˜at −i becomes a draw from the model’s own predictive
distribution:
˜at −i∼q t i(·|h t).
G Prompts
G.1Baseprompts
InBase, each player’s round-tprompt is the direct action query augmented with the same strategy-label
context used elsewhere:
rules text+compact history+“You are currently playing roundt”+action query+strategy-label context.
The compact history prefix used in code is:
Observed action history (your action, opponent action):
Round 1: <self_1>, <opp_1>
...
Round t-1: <self_{t-1}>, <opp_{t-1}>
Round-level action query templates (Base).
•BoS:
Q: Which Option do you choose, J or F?
A:
•PD (order randomized each round):
Q: Which action do you choose, J or F?
A:
•Harmony:
Q: Which action do you choose, C or D?
A:
•Promo:
Q: Which action do you choose, R, P, or Z?
A:
•Samaritan (Helper prompt):
93

Q: Which action do you choose, H or N?
A:
•Samaritan (Recipient prompt):
Q: Which action do you choose, W or S?
A:
•Lemons (Seller prompt):
Q: Which action do you choose, HQ or LQ?
A:
•Lemons (Buyer prompt):
Q: Which action do you choose, B or D?
A:
Before the final “A:” token, code injects the following strategy-context block (same helper used inBaseand
theSCoTprediction prompt):
In repeated <GameName>, a strategy maps prior history to a player’s next action
(possibly probabilistically).
Allowed strategies:
- <label_1>: <short description>
- ...
Role mapping in this prompt:
- Player A is the other player.
- Player B is you.
Observed rounds so far: <t-1>.
Context: full history prefix up to round <t-1>.
Strongly expect Player A to play with strategy ’<prior_label>’. [if available]
Allowed action tokens: <tokens>. [if available]
Output rule: do NOT output scores, reasoning, or ranking.
Respond with exactly one action only.
G.2SCoTprompts
SCoTusestwopromptsperplayerperround. TheStage-1predictionpromptreceivesthesamestrategy-label
context block asBase; the Stage-2 action prompt then conditions on the elicited prediction.
Stage 1 (prediction prompt).The prediction queries are:
•BoS:
Q: Which action do you predict the other player will choose, J or F?
94

A:
•PD (order randomized each round):
Q: Which action do you predict the other player will choose, J or F?
A:
•Harmony:
Q: Which action do you predict the other player will choose, C or D?
A:
•Promo:
Q: Which action do you predict the other player will choose, R, P, or Z?
A:
•Samaritan (Helper predicts Recipient):
Q: Which action do you predict the other player will choose, W or S?
A:
•Samaritan (Recipient predicts Helper):
Q: Which action do you predict the other player will choose, action H or action N?
A:
•Lemons (Seller predicts Buyer):
Q: Which Option do you predict the other player will choose, Option B or Option D?
A:
•Lemons (Buyer predicts Seller):
Q: Which Option do you predict the other player will choose, Option HQ or Option LQ?
A:
As implemented, the Stage-1 prediction prompt is enriched with the same strategy-context block shown
above.
Stage 2 (action prompt conditioned on Stage-1 prediction).After receiving prediction<PRED>, code
uses:
•BoS:
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option J and Option F),
compare which gives you a better result, and then choose.
Which Option do you think is the best to choose for you in this round, Option J or Option F?
95

Output only one letter: J or F.
A:
•PD (with randomized<opt1>, <opt2>):
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option <opt1> and Option <opt2>),
compare which gives you a better result, and then choose.
Which Option do you think is the best to choose for you in this round, Option <opt1> or Option <opt2>?
Output only one letter: J or F.
A:
•Harmony:
Q: Given that you think the other player will choose <PRED> in round <t>,
imagine the outcome for both of your possible actions (C and D),
compare which gives you a better result, and then choose.
Which action do you think is best for you in this round, C or D?
Output only one action: C or D.
A:
•Promo:
Q: Given that you think the other player will choose <PRED> in round <t>,
imagine the outcome for your possible actions (R, P, and Z),
compare which gives you a better result, and then choose.
Which action do you think is best for you in this round, R, P, or Z?
Output only one action: R, P, or Z.
A:
•Samaritan (Helper):
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option H and Option N),
compare which gives you a better result, and then choose.
Which Option do you think is best to choose for you in this round, Option H or Option N?
Output only one letter: H or N.
A:
•Samaritan (Recipient):
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option W and Option S),
compare which gives you a better result, and then choose.
Which Option do you think is best to choose for you in this round, Option W or Option S?
Output only one letter: W or S.
96

A:
•Lemons (Seller):
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option HQ and Option LQ),
compare which gives you a better result, and then choose.
Which Option do you think is best to choose for you in this round, Option HQ or Option LQ?
Output only one letter: HQ or LQ.
A:
•Lemons (Buyer):
Q: Given that you think the other player will choose Option <PRED> in round <t>,
imagine the outcome for both of your possible actions (Option B and Option D),
compare which gives you a better result, and then choose.
Which Option do you think is best to choose for you in this round, Option B or Option D?
Output only one letter: B or D.
A:
G.3PS-BRprompts for known deterministic payoffs
PS-BRdoes not query the LLM for direct action choice. Actions are produced by rollout-based strategy
evaluation after sampling one opponent strategy per round. The prompt-facing LLM call is foropponent
strategy-label inferenceinllm-labelmode.
Opponent strategy inference prompt (llm-label).At roundt, for playeri, history is rewritten to
opponent view
˜ht −i = ((a1 −i,a 1 i ),...,(a t−1 −i ,at−1 i )),
so tuples are(Player A action, Player B action)with:
•Player A = opponent whose strategy is inferred.
•Player B = current decision-maker.
The prompt template is:
You are inferring Player A’s strategy (the opponent) in repeated <GameName>.
In a repeated-game setting, a strategy is a rule that maps prior history to the
player’s next action (possibly probabilistically).
<rules_text>
Observed rounds so far: <t-1>.
Allowed labels:
- <label_1>: <description_1>
- ...
97

Observed action history tuple format: (Player A action, Player B action).
Player A is the opponent whose strategy label you must infer.
Player B is you (the decision-maker).
Context: full history prefix up to round <...>.
Target: observed Player A action at round <...>.
Choose the allowed label that makes this observed Player A target most compatible
with the context.
At round <...>, use this mapping:
Context history as (Player A, Player B), rounds <...>:
round <k>: Player A=<...>, Player B=<...>
Observed target Player A action at round <...>: <...>
Strongly expect Player A to play with strategy ’<prior_label>’.
Player A’s strategy may have changed over time, so weigh recent rounds more heavily
than earlier rounds.
Output rule: do NOT output scores, reasoning, or ranking.
Respond with exactly one label only.
**Output only the label.**
Likelihood mode (no prompt).If–strategy-inference likelihoodis used, no LLM prompt is
issued for strategy inference; the label is sampled from a hand-coded likelihood over the finite menu.
G.4PS-BRprompts for unknown stochastic payoffs
Underthetheorem-alignedimplementationusedforExperiment3,PS-BRunderunknownstochasticpayoffs
stillsamplesbothanopponentstrategyhypothesisandapayoffhypothesisateachroundbeforerollout-based
strategyevaluation. Theopponent-strategysideishandledexactlyasintheknowndeterministic-payoffcase.
The payoff side is not open-ended JSON inference. Instead, Experiment 3 uses the known-common-noise
/ unknown-mean construction from Section 6: playerimaintains a posterior over a finite menuMi,g of
candidate mean payoff matrices under the Gaussian noise family with known varianceσ2 g.
Opponent strategy inference prompt (llm-label).The opponent strategy is inferred from the joint
action history, exactly as in the known deterministic payoffs case. The prompt template remains identical to
the one detailed in the previous subsection.
Finite-menu Gaussian payoff posterior (experiment configuration).At roundt, playeriupdates
πt i(m|h t,r 1:t−1 i )∝π 0 i (m)
t−1∏
s=1
ϕ(rs i ;m(as),σ 2 g), m∈M i,g,
whereϕ(·;µ,σ 2 g)is the Gaussian density andrs i |a s∼N(m(a s),σ 2 g)under candidate mean matrixm.
The implementation then samples one matrix label˜mi∼π t i and evaluates continuation strategies against
98

the induced payoff kernel
q ˜mi i (·|a) =N( ˜mi(a),σ 2 g).
Product structure of the menu.Although the theorem-level menuMi,g is finite but large, it has product
form over joint actions. With a product prior over the offsets(ka)a∈A and the Gaussian likelihood above,
the posterior factorizes by joint action. Operationally, the implementation therefore updates the discrete
posterior for each action-specific offsetka∈Kseparately and samples a full mean matrix by drawing one
offsetforeachjointaction. Thisisexactlyequivalenttosamplingfromthefullfinitemenu,withoutexplicitly
enumerating all of its elements.
Likelihoodmode(experimentconfiguration).InthereportedExperiment3runs,–payoff-inference
likelihoodisused. NoLLMpromptisissuedforpayoffinference;thesampledmean-matrixlabelisdrawn
fromtheGaussianposteriorabove. Opponentstrategyinferenceishandledeitherbythellm-labelprompt
described above or by the corresponding likelihood mode, depending on the strategy-inference setting.
Heuristicpromptmode.Anopen-endedjsonpayoff-tablepromptcanstillbeusedasaheuristicvariant,
but it is not the theorem-aligned implementation analyzed in Section 6 and instantiated in Experiment 3.
H Computation of minimum continuation probabilities
In Section 7, our repeated treatments follow the standard random-termination implementation to model
infinitely repeated game behavior: after each round, the supergame continues with probabilityδg and
otherwise terminates. In the experimental design,δg is chosen to exceed the analytical support thresholds
used in this appendix, while the matched finite-horizon control is chosen to match the expected supergame
length.
For each benchmark gameg, define
δg := inf
{
δ∈[0,1) :the benchmark cooperative equilibrium in gamegis sequentially rational
}
.
We now computeδg for the five benchmark environments in Section 7.1. For BoS, Promo, and Samaritan,
the benchmark cooperative equilibria are exactly those specified there. For PD and Lemons, however, the
empirical engineering code now uses contrite finite-punishment variants; the closed-form threshold calcu-
lations below retain analytically simpler hard-trigger surrogates for those two games. Thus the benchmark
cooperative equilibria used in this appendix are: BoS coordination or turn-taking, the hard-trigger surro-
gate in PD, alternating promotions with finite punishment in Promo, the(H,W)path with punishment in
Samaritan, and the hard-trigger surrogate in Lemons.
Proposition H.1.For the benchmark cooperative equilibria in the five environments,
δBoS = 0, δPD = 2 5, δPromo = √ 10−3, δSamaritan = 1 2, δLemons = 1 4.
99

Numerically,
δBoS = 0, δPD = 0.4, δPromo≈0.1623, δSamaritan = 0.5, δLemons = 0.25.
Proof.We check the one-shot deviation constraints for each benchmark cooperative equilibrium.
BoS.The stage payoffs are
(J,J) = (10,7),(F,F) = (7,10),(J,F) = (F,J) = (0,0).
In the benchmark cooperative paths, whether players stick to(J,J), stick to(F,F), or alternate between
them, each prescribed on-path action is already a stage-game best response to the opponent’s prescribed
action. A unilateral deviation from a coordinated outcome changes the deviator’s current payoff from10or
7to0. Hence no continuation incentive is needed. Therefore
δBoS = 0.
This is a degenerate case: BoS belongs in the benchmark set because it is one of the five environments in
Section 7.1, but its cooperative paths are not supported by the shadow of the future in the same sense as the
other four games.
PD.For the analytical hard-trigger surrogate of the PD benchmark, the cooperative equilibrium is grim-
trigger cooperation:
(J,J)every period until a deviation, then(F,F)forever.
The stage payoffs are
(J,J) = (3,3),(F,J) = (5,−5),(J,F) = (−5,5),(F,F) = (0,0).
If a player cooperates on path forever, the continuation value is
3 + 3δ+ 3δ 2 +···= 3 1−δ .
If she deviates once fromJtoF, she gets5today and then0forever. Thus cooperation is sequentially
rational iff
3
1−δ ≥5,
which gives
δ≥ 2 5.
Hence
δPD = 2 5.
100

Promo.The benchmark cooperative equilibrium alternates
(P,R)in odd periods,(R,P)in even periods,
and after a deviation the players playZfor two periods and then return to the alternating path.
LetV P be the continuation value for a player in a period in which she is assignedP, and letVR be the
continuation value for a player in a period in which she is assignedR. Using the stage payoffs
(P,R) = 4,(R,P) =−1,
we have
VP = 4 +δVR, V R =−1 +δV P.
Solving,
VP = 4−δ 1−δ 2, V R = 4δ−1 1−δ 2.
TheonlybindingdeviationisbytheplayerassignedR. Ifsheobeys,shereceivesV R. Ifinsteadshedeviates
toP, thenagainstthe opponent’sprescribedPshegets0today, then−2ineachof thenexttwopunishment
periods, and then returns to the alternating path at aP-phase. So the deviation payoff is
0−2δ−2δ 2 +δ 3VP.
Thus sequential rationality requires
VR≥−2δ−2δ 2 +δ 3VP.
Substituting the formulas forVR andVP,
4δ−1
1−δ 2≥−2δ−2δ 2 +δ 3 4−δ 1−δ 2.
Multiplying by1−δ 2>0and simplifying yields
δ4 + 6δ3−2δ 2−6δ+ 1≤0.
Since
δ4 + 6δ3−2δ 2−6δ+ 1 = (δ 2−1)(δ 2 + 6δ−1),
and1−δ 2>0forδ∈[0,1), this is equivalent to
δ2 + 6δ−1≥0.
101

The unique root in[0,1)is
δ=
√
10−3.
Therefore
δPromo =
√
10−3.
Samaritan.The benchmark cooperative equilibrium is:
(H,W)every period;
if the recipient ever shirks, switch forever to(N,W); if, during punishment, the helper deviates by helping,
switch forever to(H,S).
The stage payoffs are
(H,W) = (2,−1),(H,S) = (0,0),(N,W) = (1,−2),(N,S) = (−1,−3).
First, the recipient must preferWon the cooperative path. If she obeys forever, her value is
−1
1−δ .
If she deviates toS, she gets0today and then(N,W)forever, so her deviation value is
δ −2 1−δ .
Thus
−1
1−δ ≥δ −2 1−δ ,
which is equivalent to
δ≥ 1 2.
Second, along the punishment path(N,W), the helper must prefer not to deviate back toH. If she obeys
punishment forever, her value is
1
1−δ .
If she deviates once toH, she gets2today and then triggers(H,S)forever, which gives0thereafter. Thus
1
1−δ ≥2,
102

equivalently,
δ≥ 1 2.
Hence the binding threshold is
δSamaritan = 1 2.
Lemons.For the analytical hard-trigger surrogate of the Lemons benchmark, the cooperative equilibrium
is:
(HQ,B)every period until a low-quality sale occurs,
after which the buyer switches forever toDand the seller then plays dominantLQ.
The stage payoffs are
(HQ,B) = (3,3),(LQ,B) = (4,−1),(HQ,D) = (−1,0),(LQ,D) = (0,0).
The binding deviation is the seller’s temptation to replaceHQbyLQwhen the buyer is expected to buy. If
the seller cooperates forever, her value is
3
1−δ .
If she deviates once toLQ, she gets4today and then the buyer boycotts forever, yielding0thereafter. Thus
3
1−δ ≥4,
which gives
δ≥ 1 4.
Therefore
δLemons = 1 4.
Collecting the five thresholds proves the result.
Table 6 summarizes the thresholds. For the matched finite-horizon controls, a natural choice is
Hg =
⌈
1
1− δg
⌉
,
which matches the expected supergame length up to integer rounding, in the spirit of Bó (2005)’s random-
termination versus matched-finite comparison.
Two interpretive remarks are useful here. First, among the five benchmark games, only BoS hasδg = 0,
because its benchmark cooperative outcomes are already stage-game best responses. Second, the other four
103

Table 6: Minimum continuation probabilities for supporting the benchmark cooperative equilibria
Gameg δg Hg =
⌈
1
1−δg
⌉
BoS0 1
PD 2 5 2
Promo
√
10−3≈0.1623 2
Samaritan 1 2 2
Lemons 1 4 2
thresholds are genuine continuation-value thresholds: they are the minimum shadow-of-the-future levels
needed to make the benchmark cooperative repeated-game path sequentially rational.
I Game-specific strategy menus
For the analysis under the retained-menu identification assumption, we use sparse deterministic menus.
Each menu contains one benchmark cooperative-equilibrium automaton together with seven deterministic
constant or periodic heuristics that are not on-path observationally equivalent to it. Because the retained
labels are deterministic, once a wrong label prescribes a different action from the benchmark at a reached
public history, the realized action assigns that label zero likelihood from that date onward. Accordingly, we
exclude labels such asalways_cooperate,always_help,always_work,always_buy,always_hq, and
any alternative trigger label that shares the same cooperative path and punishment regime as the benchmark
equilibrium label. The richer empirical rollout menu used for engineering experiments can remain broader;
the menus below are the sparse appendix menus used for the identification argument. For thealt_*and
*_cyclelabels below, the phase convention is treated as part of the public automaton state.
Proposition I.1(Verification for the sparse simulation menus).For each game and player role, the sparse
public-actionmenuspecifiedinthisappendixsatisfiesAssumption7forthebenchmarkequilibriumautomaton
used in the corresponding simulation analysis. Consequently, by Corollaries C.4 and C.6, Assumptions 3
and 5 hold for those simulation menus.
Proof.Each listed menu is deterministic by construction, so the deterministic-menu part of Assumption 7
holdsimmediately. Menugrainoftruthalsoholdsbyconstruction,sincetherelevantbenchmarkequilibrium
automaton is explicitly included in the retained menu for each game and role.
It remains to verify on-path finite separation. Fix a game, a player role, and the benchmark profileffor the
corresponding simulation instance, and letf−i denote the benchmark opponent automaton in the retained
menu. Along the realized path underf, every wrong retained labelg−i differs fromf−i after finitely many
public histories for an explicit structural reason:
•InBoS,thebenchmarkisoneoftheeightlisteddeterministicperiodicwords,andeveryotherretainedlabel
is a different periodic word. Hence there is a smallest round at which the two words prescribe different
104

actions.
•InPD,thebenchmarkisgrim_eq,whichprescribesJateveryreachedhistoryontherealizedcooperative
path. Each wrong retained label prescribesFby round1,2,3, or4:all_Fat round1,alt_JFand
alt_FJbyround2,JJF_cycleandJFF_cyclebyround3,andJJJF_cycleandJFFF_cyclebyround
4.
•In Promo, the benchmark is one of the two alternating cartel labels. The other cartel label starts in the
opposite phase and therefore differs at round1. The remaining six labels are constant or period-3rules;
each either starts with the wrong action or repeats an action (or usesZ) within the first three rounds,
whereas the benchmark alternates betweenPandRwithout usingZon the realized path.
•IntheSamaritanhelpermenu,helper_eqprescribesHateveryreachedhistoryontherealizedcooperative
path, while every wrong label prescribesNby round1,2,3, or4. In the recipient menu,recipient_eq
prescribesWateveryreachedhistoryontherealizedcooperativepath,whileeverywronglabelprescribes
Sby round1,2,3, or4.
•IntheLemonssellermenu,seller_eqprescribesHQateveryreachedhistoryontherealizedcooperative
path,whileeverywronglabelprescribesLQbyround1,2,3,or4. Inthebuyermenu,buyer_eqprescribes
Bateveryreachedhistoryontherealizedcooperativepath,whileeverywronglabelprescribesDbyround
1,2,3, or4.
Lett g be the first such disagreement round. Because the menus are deterministic, the realized benchmark
action att g has probability one underf−i and probability zero underg−i. Thereforeg −i(htg(z))̸=
f−i(htg(z))on the realized path, sog−i is refuted in finite time. This proves Assumption 7(2).
(1) BoS menu.Use the same 8-label menu for both players.
•coord_J: playJevery round.
•coord_F: playFevery round.
•alt_JF: playJ,F,J,F,....
•alt_FJ: playF,J,F,J,....
•JJF_cycle: repeatJ,J,F.
•JFF_cycle: repeatJ,F,F.
•JJFF_cycle: repeatJ,J,F,F.
•JJJF_cycle: repeatJ,J,J,F.
105

All eight BoS labels are deterministic and pairwise distinct as action words, so any wrong retained label is
contradicted in finite time.
(2) PD menu.Use the same 8-label menu for both players.
•grim_eq: playJuntil the opponent first playsF; thereafter playFforever.
•all_F: playFevery round.
•alt_JF: playJ,F,J,F,....
•alt_FJ: playF,J,F,J,....
•JJF_cycle: repeatJ,J,F.
•JFF_cycle: repeatJ,F,F.
•JJJF_cycle: repeatJ,J,J,F.
•JFFF_cycle: repeatJ,F,F,F.
There is only one prefix-then-absorbing trigger label,grim_eq. Every other retained label is a constant or
periodic word, so it cannot coincide forever with a realized grim path.
(3) Promo menu (actions:R= regular,P= promotion,Z= punishment/price war).Use the same
8-label menu for both players.
•cartel_phase0: cooperative pathP,R,P,R,...; after any deviation from the prescribed phase path,
playZ,Zfor two periods, then return to phase 0.
•cartel_phase1: cooperative pathR,P,R,P,...; after any deviation from the prescribed phase path,
playZ,Zfor two periods, then return to phase 1.
•all_R: playRevery round.
•all_P: playPevery round.
•all_Z: playZevery round.
•RRP_cycle: repeatR,R,P.
•PPR_cycle: repeatP,P,R.
•RRZ_cycle: repeatR,R,Z.
The two cooperative cartel labels are distinct at round 1, and none of the six alternatives shares their
alternating path or their two-period punishment block.
106

(4) Samaritan menus (Helper actions:H= Help,N= No-help; Recipient actions:W= Work,S=
Shirk).The game is asymmetric, so we use separate menus.
Helper menu.
•helper_eq: playHuntil the recipient first playsS; thereafter playNforever.
•all_N: playNevery round.
•alt_HN: playH,N,H,N,....
•alt_NH: playN,H,N,H,....
•HHN_cycle: repeatH,H,N.
•HNN_cycle: repeatH,N,N.
•HHHN_cycle: repeatH,H,H,N.
•HNNN_cycle: repeatH,N,N,N.
Recipient menu.
•recipient_eq: start withW; continueWthrough the cooperative phase and through punishment. If
punishment has already begun and the helper later playsHagain, switch toSforever.
•all_S: playSevery round.
•alt_WS: playW,S,W,S,....
•alt_SW: playS,W,S,W,....
•WWS_cycle: repeatW,W,S.
•WSS_cycle: repeatW,S,S.
•WWWS_cycle: repeatW,W,W,S.
•WSSS_cycle: repeatW,S,S,S.
Foreachrole,thereisonlyonetrigger-styleequilibriumlabel. Theothersevenlabelsareconstantsorcycles,
so they cannot remain observationally equivalent to that equilibrium label on any realized path.
(5)Lemonsmenus(Selleractions:HQ=High-quality,LQ=Low-quality; Buyeractions:B=Buy,D
= Don’t buy).This game is also asymmetric, so we use separate menus.
Seller menu.
•seller_eq: playHQuntil the buyer first playsD; thereafter playLQforever.
107

•all_LQ: playLQevery round.
•alt_HQ_LQ: playHQ,LQ,HQ,LQ,....
•alt_LQ_HQ: playLQ,HQ,LQ,HQ,....
•HHQ_LQ_cycle: repeatHQ,HQ,LQ.
•HQ_LQ_LQ_cycle: repeatHQ,LQ,LQ.
•HHHQ_LQ_cycle: repeatHQ,HQ,HQ,LQ.
•HQ_LQ_LQ_LQ_cycle: repeatHQ,LQ,LQ,LQ.
Buyer menu.
•buyer_eq: playBuntil the first observedLQ; thereafter playDforever.
•all_D: playDevery round.
•alt_BD: playB,D,B,D,....
•alt_DB: playD,B,D,B,....
•BBD_cycle: repeatB,B,D.
•BDD_cycle: repeatB,D,D.
•BBBD_cycle: repeatB,B,B,D.
•BDDD_cycle: repeatB,D,D,D.
Again,onlyoneretainedlabelhasthereputation/boycottprefix-then-absorbingformforeachrole. Allother
retained labels are constants or cycles, so they are finitely refuted against that equilibrium label.
J Promo game
J.1 Promo game (Lal, 1990): alternating promotions with finite punishment
Lal (1990) studies repeated price competition in a market with two identical “national” brands that have
loyal consumers and a third “local” brand with little/no loyalty. The local brand disciplines prices in the
switching segment, creating a tension for the national brands between (i) extracting rents from loyals via a
high “regular” price and (ii) defending the switchers via temporary price cuts. A key result is that, even
when the corresponding one-shot stage game has no Nash equilibrium, analternating promotionspattern –
only one national brand is on promotion in a given period and the roles alternate over time – can arise as a
pure-strategy Nash equilibriumof the infinite-horizon discounted game, supported by a credible number of
punishment periods.
108

To obtain a compact repeated-game benchmark, we discretize Lal, 1990’s richer price-choice problem into
three representative regimes per firm:
•Regular(R): charge the high “regular” price
•Promotion(P): charge the low promotional price
•Punishment/price war(Z): charge a very low price used only in punishment phases.
Theresulting3×3payoffmatrixinAppendix7isareduced-formencodingoftheordinalincentivestructure:
a unilateral promotion against a regular-price rival yields the highest current-period gain (the “temptation”
payoff); simultaneous promotions are less profitable thanalternatingpromotions; and outcomes involving
Zare jointly bad, standing in for the “intense competition/price war” phase used to deter deviations.
The canonical nontrivial Nash equilibrium is analternatingpath: play(P,R)in odd rounds and(R,P)
in even rounds (or vice versa). After any deviation from the prescribed phase, switch to a punishment
phase (e.g.,(Z,Z)for a fixed number of rounds) for a few periods and then return to the alternating path
(as defined as Abreu, 1988), or revert permanently to a low-payoff punishment regime (grim trigger). For
sufficientlypatientplayers,thediscountedlossfromthepunishmentphaseoutweighstheone-shotdeviation
gain, making the alternating-promotions path incentive compatible.
109
